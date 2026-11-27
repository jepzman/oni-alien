# Deep dive 09 · Sharding & Partitioning. Builds on Vol. 1 note 15 (sharding) and Vol. 3 note 12 (table partitioning).
# Example: the mug shop, grown up, with the numbers from the sharding note: an orders database of 4 TB growing
# 300 GB a month, 40,000 writes a second at peak, sharded by customer id; and the partitioning note's table of
# events, two billion rows over five years, split by month.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
ladder_svg = '''
  <rect class="bx" x="10" y="120" width="150" height="70" rx="8"/><text class="lbl" x="85" y="150" text-anchor="middle">one table</text><text class="soft" x="85" y="172" text-anchor="middle">one database</text>
  <rect class="bx-y" x="200" y="90" width="160" height="70" rx="8"/><text class="lbl" x="280" y="120" text-anchor="middle">partitions</text><text class="soft" x="280" y="142" text-anchor="middle">same database</text>
  <rect class="bx" x="400" y="60" width="160" height="70" rx="8"/><text class="lbl" x="480" y="90" text-anchor="middle">+ read copies</text><text class="soft" x="480" y="112" text-anchor="middle">same writes</text>
  <rect class="bx-g" x="600" y="30" width="150" height="70" rx="8"/><text class="lbl" x="675" y="60" text-anchor="middle">shards</text><text class="soft" x="675" y="82" text-anchor="middle">many databases</text>
  <path class="ln" d="M160 140 L198 128" marker-end="url(#a)"/><path class="ln" d="M360 112 L398 100" marker-end="url(#a)"/><path class="ln" d="M560 84 L598 72" marker-end="url(#a)"/>
  <text class="soft" x="85" y="214" text-anchor="middle">simplest</text><text class="soft" x="280" y="186" text-anchor="middle">old data out in a second</text>
  <text class="soft" x="480" y="156" text-anchor="middle">more reads</text><text class="soft" x="675" y="126" text-anchor="middle">more writes, more storage</text>
  <text class="soft bad" x="675" y="148" text-anchor="middle">hardest to undo</text>
'''
recap = '''
<p>The shop did well. The orders database is 4 TB, grows 300 GB a month, and takes 40,000 writes a second at the evening peak. Next to it, a table of order events holds two billion rows from five years. Two notes cover the two tools for this.</p>
''' + tbl(["Note", "In one line", "Where it happens"], [
    ["Table Partitioning", "split one big table into smaller tables behind one name, usually by month", "inside one database"],
    ["Sharding", "split the data across many databases by a key, and route each query to the right one", "across many databases"],
]) + fig(760, 230, "Four steps on a ladder, from left to right. One table in one database is the simplest. Partitions in the same database let old data go in a second. Adding read copies gives more reads but the same writes. Shards in many databases give more writes and more storage, and are the hardest to undo.",
         ladder_svg, "Climb one step at a time. Each step solves a different problem, and the last one is very hard to come back down.") + mn("The sharding note has a going-deeper chapter on moving shards, hot keys and cross-shard queries. This dive builds on it.") + '''
<p class="full">The two words are often used as if they were one idea. They are not. Partitioning reorganises a table inside one database and is mostly invisible to the application. Sharding splits the data across machines and changes how almost every query, transaction and unique id works. This deep dive covers when each is worth it, the one decision that sharding hangs on, and what running a sharded system is like on an ordinary Tuesday.</p>
'''

# ------------------------------------------------------------------ 2 partitioning
partition = '''
<p>Start inside one database. The events table is slow because it is huge, not because the machine is too small. Partitioning by month turns one two-billion-row table into sixty tables of about 33 million rows each, behind the same name.</p>
''' + code("order-events.sql", "one parent, one partition per month", '''
CREATE TABLE order_events (
  order_id   BIGINT      NOT NULL,
  at         TIMESTAMPTZ NOT NULL,
  type       TEXT        NOT NULL,
  data       JSONB,
  PRIMARY KEY (order_id, at)              -- must include the partition key
) PARTITION BY RANGE (at);

CREATE TABLE order_events_2026_11 PARTITION OF order_events
  FOR VALUES FROM ('2026-11-01') TO ('2026-12-01');
''') + tbl(["What you gain", "Why"], [
    ["queries for recent data read only recent partitions", "the planner skips partitions that cannot match the <code>WHERE</code> (pruning)"],
    ["old data leaves in a second", "<code>DROP</code> or <code>DETACH</code> a partition instead of deleting a billion rows"],
    ["maintenance in small pieces", "vacuum, reindex and backup work per partition"],
    ["indexes that fit in memory", "each partition's index is small, and the hot ones are recent"],
]) + mn("Partitioning makes big tables manageable. It does not make one machine bigger.") + full('''<h3>The rules that bite</h3>
''' + tbl(["Rule", "Consequence"], [
    ["every query should filter on the partition key", "<code>WHERE order_id = 42</code> with no date checks all sixty partitions"],
    ["primary keys and unique constraints must include the partition key", "you cannot enforce “one event id is unique” across the whole table by itself"],
    ["partitions must exist before rows arrive", "a job creates next month's partition ahead of time (drill 6)"],
    ["a default partition catches rows with no home", "useful as a safety net; but once it holds rows for a month, creating that month's partition has to move them"],
    ["thousands of partitions slow down planning", "keep partitions large: tens of GB, or one per month"],
]) + '''<h3>Choosing the partition key</h3>
<p>Choose the column that nearly every query filters on, and by which old data leaves. For events, logs and metrics that is time, and the partitions are months. For data that is kept for ever and read by owner, partitioning by a hash of the owner spreads maintenance but rarely speeds up queries. If no single column appears in most queries, partitioning will make reads slower, not faster.</p>
<p>Partitioning is also a good rehearsal for sharding. The same questions come up: which key, what happens to queries without it, what happens to unique constraints. They are much cheaper to answer inside one database.</p>
<h3>Partitioning a table that already exists</h3>
<p>The events table already holds two billion rows, and a table cannot be turned into a partitioned one in place. There is a gentle route that needs no big copy.</p>
<ol>
  <li>Create the new partitioned parent with a new name, and partitions for this month and the next three.</li>
  <li>Attach the whole old table to it as one partition, covering everything up to today. Add the matching <code>CHECK</code> constraint first, validated separately, so attaching it does not scan two billion rows under a lock.</li>
  <li>Swap the names in one short transaction. New rows now land in monthly partitions; old rows stay in the one big partition.</li>
  <li>Leave the big partition alone until it ages out, or move one month at a time into proper partitions during quiet hours.</li>
</ol>
<p>It is the expand-and-contract idea again: a new shape beside the old one, then a switch that takes a second.</p>''')

# ------------------------------------------------------------------ 3 before sharding
before = '''
<p>Sharding is the step at the top of the ladder because it is the hardest to undo. Before taking it, be sure what problem you are solving, and that a cheaper step does not solve it.</p>
''' + tbl(["Symptom", "Try first", "Shard when"], [
    ["reads are slow", "indexes (deep dive 10), a cache, read copies", "rarely: reads alone almost never need sharding"],
    ["the table is huge, queries on recent data are slow", "partitioning, archiving old rows", "never for this alone"],
    ["writes are at the limit of one primary", "batching, fewer indexes, a larger machine", "the largest sensible machine is still not enough"],
    ["storage grows faster than one machine can hold", "move cold data to cheaper storage", "even the hot data will not fit in a year"],
    ["backups and restores take too long", "incremental backups, partitioned maintenance", "a restore of the whole database is longer than you can be down"],
    ["one part of the product dominates", "split that part into its own service with its own database", "that part on its own still outgrows one machine"],
], hot=(2, 3)) + mn("Splitting by function, orders here and payments there, is often the cheapest “sharding” of all.") + '''
<p>For the shop, two rows are tinted, and the numbers decide. The orders database grows 300 GB a month; in two years it will be 11 TB. Peak writes are 40,000 a second and rising; tested on the largest machine the team will run, one primary sustains about 10,000 with all its indexes. Both say the same thing: one database will not be enough, and partitioning will not change that.</p>
''' + full('''<h3>What sharding costs, said out loud</h3>
<ul>
  <li><b>Every query</b> must know its shard key, or ask every shard.</li>
  <li><b>Every transaction</b> must fit in one shard, or become a saga.</li>
  <li><b>Every unique id and constraint</b> must be designed to work across shards.</li>
  <li><b>Every operational task</b>, from backups to migrations, now runs on many databases.</li>
  <li><b>Every engineer</b> must learn where the line between shards is.</li>
</ul>
<p>None of these is a reason not to shard. All of them are reasons to shard once, with a key chosen carefully, and not to start before the numbers say so.</p>''')

# ------------------------------------------------------------------ 4 the key
key = '''
<p>The shard key decides which queries are cheap, which transactions are possible, and where the load lands. It is also the hardest decision to change later, because changing it means moving every row. A good key has five properties.</p>
''' + tbl(["Property", "Question", "Why"], [
    ["<b>In most queries</b>", "do the common queries say which key they want?", "a query without the key asks every shard"],
    ["<b>Groups what changes together</b>", "do the rows one transaction touches share the key?", "a transaction can only be atomic inside one shard"],
    ["<b>Many values</b>", "are there far more key values than shards?", "few values cannot be spread evenly"],
    ["<b>Even load</b>", "is any one value much busier than the rest?", "one busy value makes one hot shard"],
    ["<b>Never changes</b>", "can a row's key be updated?", "a changed key means moving the row to another shard"],
]) + '''
<h3>Candidates for the shop's orders</h3>
''' + tbl(["Key", "In most queries", "Groups changes", "Even", "Verdict"], [
    ["<b>customer id</b>", "yes: order history, checkout, account", "yes: a customer's orders, basket, addresses", "mostly; a few big business customers", "chosen"],
    ["order id", "only lookups by id", "no: the customer's other data is elsewhere", "yes", "spreads well, groups nothing"],
    ["country", "often", "partly", "no: one country is most of the traffic", "too few values"],
    ["order date", "for reports", "no", "no: all writes go to today's shard", "a hot shard by design (drill 1)"],
], hot=(0,)) + mn("A shard key is chosen for the writes and the common reads. Everything else is answered another way (chapter 8).") + full('''<h3>Ids that know their shard</h3>
<p>Sharding by customer creates a new problem: a request arrives with only an order id. Which shard holds order 7713? Two answers work.</p>
''' + tbl(["Approach", "How", "Cost"], [
    ["<b>a lookup table</b>", "a small global table: order id → customer id", "one extra read for every lookup by order id; one more system"],
    ["<b>put the shard in the id</b>", "the order id is made with the customer's logical shard inside it", "ids must be generated by your code, not a database sequence"],
]) + code("order-id.ts", "64-bit ids that carry their logical shard", '''
// 41 bits of milliseconds since 2024 · 10 bits of logical shard (0-1023) · 12 bits of counter
export function newOrderId(customerId: bigint, now = Date.now()): bigint {
  const shard = logicalShard(customerId);                 // hash(customerId) % 1024
  return (BigInt(now - EPOCH_2024) << 22n) | (BigInt(shard) << 12n) | nextCounter();
}

export const shardOfOrder = (orderId: bigint) => Number((orderId >> 12n) & 1023n);
''') + '''<p>Ids made this way also sort roughly by time, which keeps index inserts near the end of the index, and they never collide across shards, which a sequence in each database would. Database sequences are the first thing that breaks when a team shards without planning.</p>
<h3>When no single key fits</h3>
<p>Sometimes two access paths are equally important and want different keys. A messaging feature is read by conversation and also listed per user. A ride-sharing trip belongs to a rider and to a driver. Three honest options exist.</p>
<ul>
  <li><b>Pick the path that writes</b>, shard by its key, and serve the other path from a second copy filled from events (chapter 8). Writes stay atomic; the second path lags by seconds.</li>
  <li><b>Use a composite key</b> for very large owners: customer id for most customers, customer and branch for the café chain. The router needs to know which customers are split, which the shard map can record.</li>
  <li><b>Store it twice on purpose</b>, once per key, written by a saga. This is the most work and the right answer only when both paths must be fast and current.</li>
</ul>
<p>What does not work is choosing a key that serves neither path well as a compromise. A key is either in the query or it is not.</p>''')

# ------------------------------------------------------------------ 5 drills
drills = mn("Each of these is cheap to avoid before sharding and expensive after.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · today's shard</a></li><li><a href="#drill-2">2 · the giant</a></li><li><a href="#drill-3">3 · the fan-out</a></li>
  <li><a href="#drill-4">4 · two shards, one change</a></li><li><a href="#drill-5">5 · the move</a></li><li><a href="#drill-6">6 · the 1st of the month</a></li>
</ul>
''' + drill(1, "Every write goes to one shard", [
    ("Timeline", "A team shards its events by date range: one shard per quarter. It looks tidy. Every new event is from today, so every write goes to the current quarter's shard. The other eleven sit idle."),
    ("What you see", "One shard at 100 % CPU, the rest under 5 %. Sharding has added complexity and removed no load.", True),
    ("What saves you", "Never shard by a value that moves with time. Shard by something with many values that are written in parallel, such as a customer id, hashed. Inside each shard, partition by month if you also want old data to leave cheaply. Time is a fine partition key and a poor shard key."),
], "a shard key must spread today's writes, not just the total.") + drill(2, "One customer bigger than a shard", [
    ("Timeline", "A café chain signs up as a business customer and orders for 900 branches through one account. Its orders, all under one customer id, are 8 % of all writes. With 32 shards, its shard carries three times the load of the others."),
    ("What you see", "One shard always behind, its replicas lagging, and every other customer who happens to hash to it suffers. Moving shards does not help: one key cannot be split across shards.", True),
    ("What saves you", "Measure load per key, not just per shard, so a giant is seen early. Then give it its own place: route that customer to a dedicated shard through the shard map. If even that is not enough, make the key more precise for that customer only, for example customer and branch."),
], "averages hide giants. Watch the busiest keys, and give a giant its own shard.") + drill(3, "The search that asked every shard", [
    ("Timeline", "Support's “find orders by email address” screen does not know the customer id, so it asks all 32 shards and merges the results. At first it is used a few times an hour. Then a fraud tool starts calling it 50 times a second."),
    ("What you see", "Every shard does 50 extra queries a second, and the search's response time is the slowest of 32 shards, so it is often slow even when the shards are fine. One feature has put load on the entire fleet.", True),
    ("What saves you", "Treat a query without the shard key as an exception that needs a design. Keep a small lookup table from email to customer id, sharded by email, and the search becomes two single-shard lookups. Count fan-out queries in a metric and review every new one."),
], "a query without the shard key costs every shard. Give common ones a lookup of their own.") + drill(4, "One change across two shards", [
    ("Timeline", "Two customer accounts are merged after a duplicate sign-up. The code moves orders from customer A, on shard 5, to customer B, on shard 19: insert on 19, then delete on 5. The process is restarted between the two."),
    ("What you see", "Orders that exist under both customers. There is no transaction that covers two databases, so nothing rolled the first step back.", True),
    ("What saves you", "Accept that a change across shards is not atomic and design it as a saga: each step idempotent, recorded, and resumable or reversible (the Saga deep dive). Better still, make such changes rare by choosing a key that keeps related rows together."),
], "atomicity ends at the shard boundary. Anything that crosses it is a saga.") + drill(5, "Writes lost during a shard move", [
    ("Timeline", "Logical shard 371 is moved to a new machine. The copy has caught up, the map is switched, and the old copy is deleted. But some app servers cached the old map for a minute and kept writing to the old machine after the switch."),
    ("What you see", "A few hundred orders written to a database that was then deleted. Customers were charged; the orders are gone.", True),
    ("What saves you", "Make the switch impossible to miss. Pause writes to the moving shard, let the copy catch up, change the map and bump its version, and have the old copy refuse writes for that shard from then on. Every write carries the map version it was routed with, so a stale router gets an error and fetches the new map instead of writing to the wrong place. Keep the old copy for days, not minutes."),
], "a shard move ends when the old copy refuses writes, not when the map changes.") + drill(6, "Midnight on the 1st", [
    ("Timeline", "The job that creates next month's event partition failed quietly in October. At 00:00 on 1 November, every insert into <code>order_events</code> fails: there is no partition for November."),
    ("What you see", "Checkout fails at midnight, because placing an order writes an event. The fix takes a minute; finding it takes forty, in the middle of the night.", True),
    ("What saves you", "Create partitions well ahead: three months, not one. Alert when fewer than two future partitions exist. A default partition prevents the outage, but rows that land there must be moved before the real partition can be created, so it is a safety net with its own runbook, not a fix."),
], "partitions are created months ahead, and an alert counts them.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Decision", "Drill"], [
    ["the shard key spreads current writes; time is for partitions, not shards", "1"],
    ["load is measured per key; giants get their own shard", "2"],
    ["queries without the key are counted, reviewed and given lookups", "3"],
    ["changes across shards are sagas", "4"],
    ["moves fence the old copy and version the map", "5"],
    ["partitions are made months ahead and counted by an alert", "6"],
]))

# ------------------------------------------------------------------ 6 routing
route_svg = '''
  <rect class="bx" x="10" y="70" width="120" height="50" rx="8"/><text class="lbl" x="70" y="100" text-anchor="middle">customer 7</text>
  <rect class="bx" x="170" y="70" width="120" height="50" rx="8"/><text class="lbl" x="230" y="94" text-anchor="middle">hash % 1024</text><text class="soft" x="230" y="112" text-anchor="middle">never changes</text>
  <rect class="bx-y" x="330" y="70" width="130" height="50" rx="8"/><text class="lbl" x="395" y="100" text-anchor="middle">logical 371</text>
  <rect class="bx-g" x="500" y="50" width="120" height="90" rx="8"/><text class="lbl" x="560" y="80" text-anchor="middle">shard map</text><text class="soft" x="560" y="102" text-anchor="middle">0–31 → db1</text><text class="soft" x="560" y="122" text-anchor="middle">352–383 → db12</text>
  <rect class="bx" x="660" y="70" width="90" height="50" rx="8"/><text class="lbl" x="705" y="100" text-anchor="middle">db12</text>
  <path class="ln" d="M130 95 H168" marker-end="url(#a)"/><path class="ln" d="M290 95 H328" marker-end="url(#a)"/><path class="ln" d="M460 95 H498" marker-end="url(#a)"/><path class="ln" d="M620 95 H658" marker-end="url(#a)"/>
  <text class="soft" x="560" y="170" text-anchor="middle">version 18 · changes when a shard moves</text>
  <text class="soft" x="230" y="170" text-anchor="middle">fixed at design time</text>
'''
routing = '''
<p>The sharding note's going-deeper chapter introduced logical shards: hash every key into a large fixed number of slots, and keep a small map from slots to machines. This chapter is about living with that map.</p>
''' + fig(760, 190, "How customer 7 is routed. The customer id is hashed modulo 1024, a step fixed at design time, giving logical shard 371. The shard map, which has a version number and changes when a shard moves, says logical shards 352 to 383 live on database db12. The request goes to db12.",
          route_svg, "Two steps. The first never changes; the second is a small table you can edit.") + tbl(["Where the router lives", "How", "Good for"], [
    ["<b>a library in the app</b>", "every app instance holds the map and connects to shards directly", "few services, one language, full control"],
    ["<b>a proxy</b>", "the app talks to one endpoint; the proxy routes (Vitess, Citus coordinator, ProxySQL)", "many services and languages; the app looks unsharded"],
    ["<b>the database itself</b>", "a distributed database splits and moves ranges by itself", "teams that would rather not build any of this"],
]) + mn("The map is tiny and read constantly. Cache it everywhere, and give it a version so a stale copy is detected.") + full('''<h3>The map is critical state</h3>
<p>Every request depends on it, so it is stored in a consistent store (a consensus store, or a table that only an admin tool writes), cached by every router, and checked by version. A router that sends a write with map version 17 to a shard that knows version 18 gets a clear error and reloads. That one check is what drill 5 was missing.</p>
<h3>A move, with the checks that make it safe</h3>
''' + tbl(["#", "Step", "Check before the next step"], [
    ["1", "copy the logical shard's rows to the new machine", "row counts match for that shard"],
    ["2", "stream later changes until the copy is seconds behind", "lag under a few seconds, steady"],
    ["3", "pause writes for that logical shard only", "no writes in flight"],
    ["4", "wait for the copy to catch up completely", "lag zero; a checksum of the rows matches"],
    ["5", "update the map, version + 1; old machine refuses that shard", "routers report the new version"],
    ["6", "resume writes; keep the old copy for a week", "no errors on the moved shard"],
]) + '''<p>The pause in step 3 lasts a second or two and affects about 1/1,024 of customers. Moving in many small pieces is what makes resharding routine instead of a weekend project.</p>
<h3>The first split is the hard one</h3>
<p>Moving a logical shard between two shards is routine once the router exists. Going from one database to many for the first time is the risky project, and it is much safer done in phases, months apart.</p>
''' + tbl(["Phase", "What changes", "What it proves"], [
    ["1 · shard-aware, one shard", "the router, the map and the new ids go live; every logical shard maps to the existing database", "every query carries its key; nothing fans out by accident; ids work"],
    ["2 · fix what phase 1 found", "lookup tables, second copies, sagas for the cross-customer changes", "the code no longer needs everything in one place"],
    ["3 · move logical shards off", "one range at a time to new machines, with the checks above", "each move is small, reversible and boring"],
]) + '''
<p>Phase 1 changes no data at all, so it can be rolled back with a deploy, and it surfaces every query that assumed one database while that assumption is still true. Teams that skip it discover those queries on the day the data is split, when rolling back means moving terabytes back.</p>
<h3>How many logical shards?</h3>
<p>Enough that you will never need more machines than slots: 1,024 or 4,096 is usual. Each machine holds a range of slots, so going from 32 machines to 64 means moving half the slots of each, one at a time. The number of logical shards is the one number you cannot change cheaply, so err on the large side.</p>''')

# ------------------------------------------------------------------ 7 numbers
numbers = '''
<p>The shop's sizing, from the measurements in chapter 3.</p>
''' + tbl(["Question", "Reasoning", "Answer"], [
    ["Data in two years", "4 TB + 24 × 300 GB", "about 11 TB"],
    ["Comfortable size per shard", "restores in under an hour, indexes for hot data fit in memory", "500 GB"],
    ["Shards for storage", "11 TB ÷ 500 GB", "22"],
    ["Peak writes in two years", "40,000 a second, growing 50 % a year", "about 90,000"],
    ["Shards for writes", "90,000 ÷ 5,000 per shard, keeping half of the tested 10,000 as headroom", "18"],
    ["Physical shards to start with", "the larger of 22 and 18, rounded to a power of two", "32"],
    ["Logical shards", "far more than 32; never need to change", "1,024: 32 per machine"],
], hot=(5,)) + mn("Plan for two years, start with what you need for one. Moving logical shards later is routine.") + '''
<h3>The fan-out tax</h3>
<p>A query that asks every shard waits for the slowest one. If each shard answers within 50 ms 99 times in 100, the chance that all 32 do is 0.99<sup>32</sup>, about 72 %. So more than one fan-out query in four is slower than the shards' own slow case. With 64 shards it is nearly one in two.</p>
''' + tbl(["Shards asked", "Queries that hit at least one slow shard"], [
    ["1", "1 %"], ["8", "8 %"], ["32", "28 %"], ["64", "47 %"],
], hot=(2, 3)) + full('''<h3>Headroom for moving</h3>
<p>A move reads a whole logical shard from a busy machine and writes it to another. Do it at 60 % of capacity and nobody notices. Do it at 95 %, because the shard is nearly full, and the extra reads push the source over the edge on the day you most need it to behave. Plan moves from the growth graph, months before a shard reaches its size limit, not from an alert.</p>
<p>This is why chapter 8 works so hard to keep queries on one shard. The arithmetic gets worse as the system grows, which is exactly when the fan-out queries become popular.</p>
<h3>Partition sizes for the events table</h3>
''' + tbl(["Quantity", "Value"], [
    ["rows", "2 billion over 60 months: about 33 million a month"],
    ["size per month", "about 10 GB with indexes"],
    ["partitions kept", "24 months online, older ones detached to cheap storage"],
    ["created ahead", "3 months, alert below 2"],
]) + '''<p>Inside each shard, the same rule applies: the events of that shard's customers are partitioned by month. Sharding and partitioning are not alternatives; large systems use both, for different reasons.</p>''')

# ------------------------------------------------------------------ 8 queries that don't fit
cross = '''
<p>The shard key serves the common path. Every system also has queries that cut across it. Each has a standard answer, and none of them is “query every shard and hope”.</p>
''' + tbl(["Need", "Answer"], [
    ["look up by another unique field: email, order id", "a lookup table sharded by that field, or the shard inside the id (chapter 4)"],
    ["list by another dimension: all orders for a product", "a second copy of the data shaped for it, kept up to date from events (the CQRS and Reliable Messaging dives)"],
    ["reports and totals over everything", "a data warehouse fed by change data capture; never the live shards"],
    ["small reference data: products, prices, countries", "copied to every shard, so joins stay local"],
    ["a unique rule across customers: one account per email", "enforce it in the email lookup table, sharded by email, before creating the customer"],
    ["a change touching two shards", "a saga (drill 4)"],
]) + mn("Every row in this table is a second copy of something. Sharding turns one database into a small system of copies.") + full('''<h3>Lookup tables</h3>
''' + code("email-lookup.sql", "on the shard that owns the email, not the customer", '''
-- sharded by hash(email); one row per email address
CREATE TABLE email_owner (
  email        TEXT PRIMARY KEY,
  customer_id  BIGINT NOT NULL
);
-- sign-up: claim the email first (unique here), then create the customer on its own shard
''') + '''<p>The order of steps matters. Claim the email in its lookup shard first, then create the customer. If the second step fails, a sweeper releases claims older than an hour that have no customer. The other order leaves customers whose email anyone else can claim.</p>
<h3>Tables that join stay together</h3>
<p>Orders, order lines, baskets and addresses are all sharded by customer id, so a customer's rows land on the same shard and join locally. This is called co-location, and it is the reason to shard related tables by the same key even when a table could use its own. A table sharded by its own id, such as order lines by line id, would turn every “show my order” into a fan-out. When choosing the key for a new table, ask first: which existing table does it join with most?</p>
<h3>Reference data, copied everywhere</h3>
<p>Products and prices change rarely and are joined constantly. A copy in every shard, updated from an event stream, keeps the order history page a single-shard query. Accept that a price change reaches the 32 shards a few seconds apart, and never charge from the copy: the Caching dive's rule, “show from a copy, decide on the original”, applies here too.</p>
<h3>Schema changes on 32 databases</h3>
<p>A migration now runs 32 times. Run it shard by shard, with the expand and contract steps from the Zero-Downtime Change dive, and make the code accept both schemas, because for an hour some shards will have the new column and some will not. A tool that runs a migration across all shards and reports which have it is worth building early.</p>''')

# ------------------------------------------------------------------ 9 testing and running
running = '''
<p>Sharding bugs hide in single-database test setups, because with one database every query happens to find its rows. The first rule of testing is to never have just one shard.</p>
''' + tbl(["Test", "How", "Catches"], [
    ["<b>Four shards in every test environment</b>", "even locally: four small databases, or four schemas", "queries that only work because everything is in one place"],
    ["<b>Routing</b>", "for random keys, the row is written to and found on the shard the router names", "a hash or map mismatch between services"],
    ["<b>No hidden fan-out</b>", "the test fails if a request touches more than one shard, unless allowed by name", "drill 3, before it ships"],
    ["<b>Cross-shard sagas</b>", "crash between steps; rerun; check no duplicates or orphans", "drill 4"],
    ["<b>Move rehearsal</b>", "move a logical shard under load in staging; count rows and compare checksums", "drill 5"],
    ["<b>Partition clock</b>", "set the clock to the last day of the month, insert, advance, insert", "drill 6"],
]) + mn("One shard in tests is like one thread in a concurrency test: everything passes and proves nothing.") + '''
<h3>What to watch, per shard</h3>
''' + tbl(["Metric", "Alert when"], [
    ["size and growth", "a shard will pass 500 GB within 60 days"],
    ["writes, CPU, slow-case response time", "one shard is more than 1.5 × the average: the skew ratio"],
    ["top 20 keys by writes and reads", "one key is more than 2 % of its shard's load"],
    ["fan-out queries per second, by name", "a new name appears, or one grows"],
    ["future partitions", "fewer than two exist"],
    ["map version seen by each router", "a router is behind for more than a minute"],
]) + full('''<h3>Runbook: one shard is hot</h3>
<ol>
  <li><b>Which keys?</b> The top-keys list for that shard. One key: drill 2. Many keys: the shard holds too many logical shards.</li>
  <li><b>One giant key:</b> move it to its own shard through the map; then talk to the product team, because a customer that size probably needs its own limits.</li>
  <li><b>Many keys:</b> move some logical shards to a quieter or new machine, one at a time (chapter 6).</li>
  <li><b>Neither:</b> look for a fan-out query or a report pointed at the shards by mistake.</li>
</ol>
<h3>Runbook: a shard is nearly full</h3>
<ol>
  <li><b>How soon?</b> The growth graph says when it passes the limit. More than a month away: plan moves. Less than a week: move the biggest logical shards first.</li>
  <li><b>Is it one key?</b> A single customer growing fast is drill 2 in slow motion; give it its own shard.</li>
  <li><b>Is old data still here?</b> Partitions that should have been detached are the cheapest space to recover.</li>
  <li><b>Then move</b> logical shards to a new machine, one at a time, with the checks from chapter 6.</li>
</ol>
<h3>Backups and restores</h3>
<p>Thirty-two databases back up independently, so a restore of “the system at 14:00” restores 32 databases to slightly different moments. For a single customer, all data is on one shard, so a restore is consistent for that customer. Across customers, accept small differences, or use point-in-time recovery on every shard to the same timestamp. Rehearse restoring one shard: it is the most likely real case.</p>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>Tools</h3>
''' + tbl(["Kind", "Examples", "What it does for you"], [
    ["Partitioning in one database", "PostgreSQL declarative partitioning with pg_partman; MySQL partitioning", "partitions, pruning, and pg_partman's creation of future partitions"],
    ["Sharding on PostgreSQL", "Citus", "distributed tables by a key, a coordinator that routes, reference tables copied everywhere"],
    ["Sharding on MySQL", "Vitess, PlanetScale", "routing, logical shards, online moves, a proxy that looks like one MySQL"],
    ["Distributed SQL", "CockroachDB, YugabyteDB, Google Spanner, TiDB", "splits and moves ranges automatically; cross-range transactions, at a cost in latency"],
    ["Key-value and wide-column stores", "DynamoDB, Cassandra, MongoDB", "partition key chosen per table; scaling handled for you; queries limited to what the key allows"],
]) + mn("Distributed SQL removes the routing work, not the key decision. A bad key is slow there too.") + '''
<h3>Lab</h3>
<p>The shop opens a marketplace: independent sellers list their own mugs. Customers still see their order history. Sellers get a dashboard of their own orders, and the biggest seller will have 5 % of all orders.</p>
<ol class="keep">
  <li>Keep customer id as the shard key, or change it?</li>
  <li>How is the seller dashboard served?</li>
  <li>An order with mugs from three sellers is placed. What is atomic and what is not?</li>
  <li>What happens to the biggest seller's dashboard load?</li>
  <li>Old orders must be kept for seven years but are rarely read. Where do they go?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The key</summary><p>Keep customer id. Placing an order and reading one's history are the busiest paths and both are per customer. Changing the key would also mean moving 11 TB.</p></details>
<details><summary>2 · Seller dashboard</summary><p>A second copy of order lines, sharded by seller id, filled from the order events (outbox or CDC). The dashboard reads only that copy, one shard per seller, and may be a few seconds behind, which a dashboard can be.</p></details>
<details><summary>3 · Three sellers</summary><p>The order and its lines are written in one transaction on the customer's shard: atomic. The three sellers' copies are updated from events afterwards, each idempotently: not atomic, and that is fine because nothing is decided from them.</p></details>
<details><summary>4 · The biggest seller</summary><p>In the seller-sharded copy it is a giant (drill 2). Give it its own shard through the map, and cache its dashboard figures for a minute.</p></details>
<details><summary>5 · Seven years</summary><p>Inside each shard, order lines are partitioned by month. After two years a partition is detached and exported to cheap object storage in a columnar format; the warehouse can still query it, and the live shards stay small.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Before sharding", ["The problem is writes or storage, measured and projected two years ahead", "Indexes, partitioning, archiving, read copies and a larger machine were considered", "Splitting by function was considered first"]),
    ("Partitioning", ["The partition key is in nearly every query", "Unique constraints include the partition key, or uniqueness is enforced elsewhere", "Partitions are created three months ahead and counted by an alert", "Old partitions are detached or dropped on a schedule"]),
    ("The shard key", ["It is in the common queries and groups what changes together", "It has many values and spreads today's writes, not just the total", "It never changes for a row", "Ids are generated across shards and carry or find their shard"]),
    ("Routing", ["Keys hash into a fixed, large number of logical shards", "The shard map is versioned, cached and checked on every write", "Moves fence the old copy and verify counts and checksums"]),
    ("Queries that cross", ["Fan-out queries are named, counted and reviewed", "Lookups by other unique fields have their own sharded tables", "Reports read a warehouse, not the shards", "Changes across shards are sagas"]),
    ("Operations", ["Every test environment has several shards", "Size, skew and the busiest keys are watched per shard", "Migrations run shard by shard and report progress", "Restoring a single shard has been rehearsed"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="sharding-partitioning", no=9, title="Sharding & Partitioning",
    sub="Partitions inside one database, shards across many: when each is worth it, the key everything hangs on, and life after the split.",
    summary="A deep dive on sharding and partitioning: partitioning inside one database, when to shard, choosing the shard key, six failure drills, logical shards and the shard map, sizing and the fan-out tax, queries that cross shards, testing and operations.",
    builds_on="Vol. 1, note 15 and Vol. 3, note 12",
    builds_on_links=[("Sharding", "../../distributed/notes/sharding.html"), ("Table Partitioning", "../../data/notes/partitioning.html")],
    notes=[("distributed", "sharding"), ("data", "partitioning")],
    facts=[("Example", "a 4 TB orders database at 40,000 writes a second")],
    blurb="Partitioning first, the shard key, six failure drills, logical shards and the map, the fan-out tax, queries that cross shards.",
    chapters=[
        dict(id="recap", nav="Recap", title="Two notes in sixty seconds",
             gist="Partitioning splits one big table into smaller tables inside one database. Sharding splits data across many databases by a key. They solve different problems and are often used together. Sharding is the step that is hardest to undo, so it comes last.",
             body=recap),
        dict(id="partition", nav="Partitioning", title="Partition first",
             gist="Partitioning a huge table by month lets queries read only recent partitions, lets old data leave in a second, and keeps maintenance small. Every query should filter on the partition key, unique constraints must include it, and partitions must exist before their rows arrive.",
             body=partition,
             check=[("A query on the partitioned events table filters only by order id. What happens?", "It checks every partition, because nothing in the WHERE clause lets the planner skip any."),
                    ("Why can't a partitioned table enforce that an event id alone is unique?", "Unique constraints are enforced per partition, so they must include the partition key.")]),
        dict(id="before", nav="Before sharding", title="Before you shard",
             gist="Shard for writes or storage that one machine will not handle, measured and projected. Reads, huge tables and slow backups have cheaper fixes: indexes, caching, read copies, partitioning, archiving, or giving one part of the product its own database.",
             body=before,
             check=[("Reads are slow and the CPU is busy with reporting queries. Shard?", "No. Move reports to a read copy or warehouse, and fix the indexes."),
                    ("What is the cheapest kind of split, often overlooked?", "By function: giving one part of the product, such as payments, its own database.")]),
        dict(id="key", nav="The shard key", title="The shard key: the hard problem",
             gist="The shard key decides which queries are cheap, which transactions are possible and where load lands, and it is very costly to change. It should appear in most queries, group rows that change together, have many values, spread today's writes and never change. Ids must be designed to work across shards.",
             body=key,
             check=[("Why is order date a poor shard key and a good partition key?", "As a shard key it sends every current write to one shard. As a partition key inside one database it only decides which table rows land in, and lets old months be dropped."),
                    ("A request arrives with only an order id. Name two ways to find its shard.", "A lookup table from order id to customer id, or an order id that carries its logical shard in some of its bits.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways sharded and partitioned systems hurt: a key that sends today's writes to one shard, one customer bigger than a shard, a search that asks every shard, a change that crosses two shards, writes lost during a shard move, and a missing partition at midnight on the 1st.",
             body=drills,
             check=[("Shard load is even on average but one shard is always behind. What do you look at first?", "The busiest keys on that shard: one giant key is the usual cause, and moving shards will not fix it."),
                    ("What makes a shard move safe from routers with an old map?", "The old machine refuses writes for the moved shard, and every write carries its map version so a stale router is told to reload.")]),
        dict(id="routing", nav="Routing", title="Routing and the shard map",
             gist="Hash keys into a large fixed number of logical shards, and keep a small, versioned map from logical shards to machines. Routing can live in the app, in a proxy or in the database. Moves copy, catch up, pause briefly, switch the map and fence the old copy, one logical shard at a time.",
             body=routing,
             check=[("Why 1,024 logical shards for 32 machines?", "So machines can be added later by moving logical shards, without ever changing how keys hash."),
                    ("Which number in this design can you not change cheaply?", "The number of logical shards, because changing it changes the shard of every key.")]),
        dict(id="numbers", nav="Numbers", title="Sizing, worked out",
             gist="Size for two years: storage per shard small enough to restore quickly, writes per shard with headroom; start with the larger answer and many logical shards. A query that asks every shard waits for the slowest: with 32 shards, more than a quarter of such queries hit a slow one.",
             body=numbers,
             check=[("Each of 64 shards answers within 50 ms 99 % of the time. What share of fan-out queries are slower than that?", "About 47 %: 1 − 0.99⁶⁴."),
                    ("Why start with 32 shards when 22 would hold the data?", "Writes also need room, the next two years must fit, and powers of two make moving logical shards even.")]),
        dict(id="cross", nav="Across shards", title="Queries that don't fit the key",
             gist="Lookups by another unique field get their own table sharded by that field. Lists by another dimension get a second copy filled from events. Reports go to a warehouse. Small reference data is copied to every shard. Changes across shards are sagas, and schema changes run shard by shard.",
             body=cross,
             check=[("Why claim the email in the lookup table before creating the customer?", "So two sign-ups cannot both get the same email. A failed second step leaves only a claim, which a sweeper releases."),
                    ("Product prices are copied to every shard. Can checkout use the copy?", "Show from it, yes; charge from it, no. The price for payment is read from the source.")]),
        dict(id="running", nav="Running it", title="Testing it and running it",
             gist="Never test with one shard. Check routing, fail on hidden fan-out, crash sagas between steps, rehearse moves and test the end of the month. Watch size, skew and the busiest keys per shard, the fan-out queries and the future partitions, and rehearse restoring a single shard.",
             body=running,
             check=[("Why does a single-database test environment hide sharding bugs?", "Every query finds its rows wherever it looks, so wrong routing and hidden fan-out never fail."),
                    ("The skew ratio for one shard is 2.4. Next step?", "Look at the busiest keys on that shard to tell a giant key from too many logical shards on one machine.")]),
        dict(id="tools", nav="Tools & lab", title="Tools, a lab and the checklist",
             gist="pg_partman for partitions; Citus and Vitess add sharding to PostgreSQL and MySQL; distributed SQL databases move ranges for you but still need a good key. The lab adds a marketplace with sellers, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017), chapter 6, “Partitioning”. The PostgreSQL documentation on table partitioning, and the pg_partman, Citus and Vitess documentation. Jeffrey Dean and Luiz André Barroso, “The Tail at Scale” (2013), for fan-out latency. The Notion engineering blog, “Herding elephants: lessons learned from sharding Postgres at Notion” (2021).",
)
