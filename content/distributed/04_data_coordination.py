# Scaling data collection (Sharding, Leader-Follower Replication, Cache-Aside) and Coordination (Leader Election).

# ------------------------------------------------------------------ 15 Sharding
sh_problem = Doodle(760, 260, "Doodle of one huge database server holding 4 terabytes and taking 40,000 writes per second. Its disk, CPU and memory are maxed out and the biggest machine money can buy is already in use.",
                    "Scaling up has a ceiling. Eventually one machine can't hold or handle everything.")
sh_problem.db(200, 50, None, w=240, h=150, fill="pink", stroke="red")
sh_problem.head(200, 140, "ONE database", size=22)
sh_problem.text(200, 170, "4 TB · 40k writes/s", size=18)
sh_problem.note(500, 70, "disk 96% full", "red", anchor="start")
sh_problem.note(500, 110, "CPU 100% at peak", "red", anchor="start")
sh_problem.note(500, 150, "backups take 9 hours", "red", anchor="start")
sh_problem.note(500, 190, "already the biggest machine ✗", "red", anchor="start")
sh_problem.arrow(340, 120, 490, 120, dash=True)

sh_analogy = Doodle(760, 250, "Doodle of a library's card catalogue split into drawers by surname: A to F, G to M, N to S and T to Z. To find Tagunicar you go straight to the T to Z drawer. Each drawer is small and several people can search different drawers at once.",
                    "Split by the first letter: you know exactly which drawer to open, and four people can search at once.")
for i, lab in enumerate(["A–F", "G–M", "N–S", "T–Z"]):
    x = 40 + i * 140
    sh_analogy.box(x, 60, 120, 120, lab, "green" if lab == "T–Z" else "y", size=26)
    sh_analogy.line(f"M{x + 40} 150 h40", thin=True)
sh_analogy.note(600, 40, "“Tagunicar”? → T–Z drawer", "pen")
sh_analogy.arrow(600, 50, 520, 70, curve=(580, 60))
sh_analogy.note(330, 220, "each drawer small · four people search at once", "pen")

sh_how = Doodle(760, 320, "Sharding by hashing the customer id. A router computes hash of customer id modulo the number of shards, or looks it up on a consistent hash ring, and sends the query to the shard that owns that key. Each shard is its own database holding about a quarter of the customers.",
                "The shard key decides where each row lives; the router sends each query to exactly one shard.")
sh_how.box(20, 40, 180, 60, "get customer c-731", "blue", size=17)
sh_how.arrow(206, 70, 276, 70)
sh_how.box(282, 30, 200, 80, "router", "y", sub="hash(c-731) % 4 = 2")
for i in range(4):
    x = 30 + i * 185
    sh_how.db(x + 70, 200, None, w=120, h=56, fill="green" if i == 2 else "paper")
    sh_how.head(x + 70, 244, f"shard {i}", size=18)
    sh_how.text(x + 70, 296, "~25% of customers", size=15)
    sh_how.arrow(382, 114, x + 70, 186, color="green" if i == 2 else "", dash=i != 2)

SHARDING = dict(
    slug="sharding",
    kicker="a.k.a. “split the data, split the load”",
    tldr="When one database can't hold or handle all the data, <b>split it horizontally</b>: each <b>shard</b> is a separate database holding only some of the rows, chosen by a <b>shard key</b> (e.g. customer id). A router sends every query to the shard that owns its key, so <b>storage and load spread across many machines</b>.",
    chips=[("Family", "data / scaling"), ("Lives in", "the data layer (or the database itself)"), ("Also called", "horizontal partitioning"), ("Pairs with", "consistent hashing, replication, CQRS")],
    problem="""  <p class="lead">You can make one database server bigger (<b>scale up</b>) only so far. At some point the data or the write load <span class="hl-pink">outgrows the biggest machine</span>.</p>
  <ul>
    <li>The dataset is 4 TB and growing 300 GB a month; disks and backups can't keep up.</li>
    <li>40,000 writes per second at peak; one primary can't take more.</li>
    <li>Indexes no longer fit in memory, so every query gets slower.</li>
    <li>Read replicas help reads, but every write still goes to one primary.</li>
  </ul>""",
    problem_figs=[sh_problem],
    analogy_side="the library card catalogue",
    analogy="""  <p>An old library catalogue doesn't keep every card in one giant drawer. It's split into drawers by the <b>first letter of the surname</b>: A–F, G–M, N–S, T–Z.</p>
  <ul>
    <li>To find “Tagunicar”, you go straight to T–Z. You never look in the others. That's routing by the <b>shard key</b>.</li>
    <li>Four people can search four drawers at once. That's <b>parallel load</b>.</li>
    <li>But if lots of surnames start with S, the N–S drawer overflows: a <b>hot shard</b>. You'd have to re-split the drawers: <b>resharding</b>.</li>
    <li>“Find every book borrowed on Tuesday” means opening every drawer: a <b>cross-shard query</b>.</li>
  </ul>""",
    analogy_figs=[sh_analogy],
    map=[("The whole catalogue", "The full dataset"),
         ("A drawer (A–F)", "A shard: one database with some of the rows"),
         ("First letter of the surname", "The shard key"),
         ("Going straight to the right drawer", "Routing a query to one shard"),
         ("An overflowing S drawer", "A hot shard / skewed key"),
         ("Re-splitting the drawers", "Resharding / rebalancing")],
    how_side="pick a key, route by it",
    how="""  <p>Everything depends on the <b>shard key</b>. Common strategies:</p>
  <ul>
    <li><b>Range</b> (A–F, G–M; or dates): simple and good for range scans, but easily skewed (“everyone's writing to this month's shard”).</li>
    <li><b>Hash</b> (hash(key) % N): spreads evenly, but range queries hit every shard, and changing N moves most keys.</li>
    <li><b>Consistent hashing</b>: keys and shards sit on a ring; adding a shard moves only about 1/N of the keys.</li>
    <li><b>Directory / lookup</b>: a table says which shard each tenant lives on; flexible, but the table must be fast and available.</li>
  </ul>""",
    how_figs=[sh_how],
    steps=[("Choose the shard key", "High cardinality, even spread, and present in most queries. <code>customer_id</code> or <code>tenant_id</code> are classic; <code>country</code> or <code>created_date</code> are usually skewed."),
           ("Keep related data together", "Put a customer's orders, addresses and payments on the same shard, so most queries and transactions stay on one shard."),
           ("Route every query", "In the app, a proxy (Vitess, ProxySQL) or the database itself (Citus, MongoDB, Cassandra, DynamoDB)."),
           ("Plan for cross-shard work", "Reports and global search go to a separate store (CQRS read model, data warehouse) instead of scatter-gather on every request."),
           ("Plan to reshard", "Start with many small logical shards mapped onto few machines, so growth means moving shards, not re-splitting data.")],
    vocab=[("Shard", "One partition of the data, usually its own database."),
           ("Shard key", "The column that decides which shard a row lives on."),
           ("Hot spot", "A shard getting far more load than the others."),
           ("Consistent hashing", "Hash ring where adding a node moves only ~1/N of keys."),
           ("Scatter-gather", "Sending a query to all shards and merging results."),
           ("Resharding", "Moving data to a new shard layout.")],
    code=dict(file="shard-router.ts", note="many logical shards on a few machines", src="""
const LOGICAL_SHARDS = 1024;                      // fixed forever
const placement = new Map<number, string>([       // logical shard -> DB, can change
  ...range(0, 512).map((s) => [s, "db-a"] as const),
  ...range(512, 1024).map((s) => [s, "db-b"] as const),
]);

function shardFor(customerId: string): number {
  return murmurhash(customerId) % LOGICAL_SHARDS;
}

export function dbFor(customerId: string) {
  return pools.get(placement.get(shardFor(customerId))!);   // one shard per query
}

// all of a customer's data lives together, so this is a normal local transaction
await dbFor("c-731").transaction(async (tx) => { /* order + payment rows */ });
"""),
    tools="sharded databases and helpers: Vitess (MySQL), Citus (Postgres), MongoDB sharding, Cassandra / ScyllaDB, DynamoDB partitions, CockroachDB / Spanner / YugabyteDB (automatic ranges), Kafka partitions for streams.",
    gains=["<b>Near-unlimited scale</b> for storage and writes by adding shards.",
           "<b>Smaller indexes per shard</b>, so queries stay fast.",
           "<b>Fault isolation</b>: a shard outage affects only its slice of users.",
           "<b>Parallel work</b>: backups, migrations and queries run per shard.",
           "<b>Data locality</b>: shards can live in the user's region."],
    losses=["<b>Cross-shard queries and joins</b> are slow or impossible.",
            "<b>Cross-shard transactions</b> need sagas or 2PC.",
            "<b>Resharding is hard</b> and risky.",
            "<b>Hot spots</b> if the key is skewed.",
            "<b>Much more operational complexity</b>: N databases to run."],
    baseline="Each line compares <b>one large database</b> (possibly with read replicas) to the same data <b>sharded across many databases</b>.",
    ratings=[(4, 2, "Routing, shard keys, cross-shard limits and resharding to master."),
             (3, 2, "More servers, tooling and expertise."),
             (3, 3, "Schema changes must roll across every shard."),
             (4, 3, "Need tests for routing, skew and cross-shard behaviour."),
             (2, 5, "Add shards to grow storage and write throughput."),
             (2, 3, "Adding shards takes planning; not instant."),
             (2, 4, "One shard down affects only its slice of data."),
             (2, 4, "Single-shard queries are fast; scatter-gather is slow."),
             (3, 2, "Changing the shard key later is very expensive.")],
    pitfalls=[("A skewed shard key", "Sharding by country puts 60% of users on the US shard.", "high-cardinality keys (customer id), or hash them."),
              ("Most queries need all shards", "The main screen searches across all customers, so every request hits every shard.", "shard by what most queries filter on; build a separate read model for the rest."),
              ("hash(key) % N with real machines", "Going from 4 to 5 servers moves ~80% of all keys at once.", "consistent hashing or many fixed logical shards mapped to machines."),
              ("Sharding too early", "A 50 GB database is split into 16 shards “for the future”.", "scale up, add read replicas, tune and cache first. Shard when you must."),
              ("Celebrity / hot keys", "One tenant is 100× bigger than the rest and overloads its shard.", "give big tenants dedicated shards; split hot keys.")],
    use=["Data or write volume exceeds what one machine can handle.",
         "Most queries are scoped to one key (customer, tenant, device).",
         "You need data in specific regions (data residency).",
         "You want to limit the blast radius of a database failure."],
    skip=["The data fits on one machine with headroom (most systems!).",
          "Reads are the bottleneck: try replicas and caching first.",
          "Queries routinely join across all entities.",
          "Your database can partition for you automatically. Use that."],
    related=["<b>Leader–follower replication</b> · each shard is replicated", "<b>Cache-aside</b>", "<b>CQRS</b> · global read models", "<b>Saga</b> · cross-shard work", "<b>Consistent hashing</b>"],
    quiz=[("Why is hash(key) % N a problem when N changes?", "Most keys map to a different shard when N changes, so nearly all data has to move at once."),
          ("What makes a good shard key?", "High cardinality, an even spread of data and load, and present in most queries so they hit one shard."),
          ("How do you run a report across all customers in a sharded system?", "Scatter-gather across shards for occasional use, or better, feed all shards into a separate analytics/read store."),
          ("Replication vs sharding?", "Replication copies the same data to several machines (availability, read scale); sharding splits different data across machines (write and storage scale). Real systems do both.")],
    remember="Split by the key your queries <span class=\"hl\">already use</span>. Shard late, shard many small pieces, and keep each customer's data together.",
    sources=["Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, chapter 6 “Partitioning”.",
             "Microsoft Azure Architecture Center, “Sharding pattern”.",
             "Vitess docs, “Sharding” and “VSchema”.",
             "Karger et al., “Consistent Hashing and Random Trees” (1997)."],
)

# ------------------------------------------------------------------ 16 Leader-Follower Replication
rp_problem = Doodle(760, 250, "Doodle of a single database server. When it fails, the whole app is down and recent data may be lost. Meanwhile reporting queries and app queries compete for the same machine.",
                    "One copy of the data is one disk failure away from an outage, and every read lands on the same box.")
rp_problem.db(160, 60, None, w=200, h=120, fill="pink", stroke="red")
rp_problem.head(160, 140, "the only copy", size=20)
rp_problem.icon("cross", 260, 40, .7, color="red")
rp_problem.note(450, 70, "disk dies → app down for hours", "red", anchor="start")
rp_problem.note(450, 110, "→ last backup was 6 hours ago", "red", anchor="start")
rp_problem.note(450, 160, "reports + app reads fight for CPU", "red", anchor="start")
rp_problem.note(450, 200, "no copy near users in Europe", "red", anchor="start")

rp_analogy = Doodle(760, 260, "Doodle of a teacher writing on the main whiteboard while students copy the notes into their own notebooks. Students answer questions from their notebook copies. Only the teacher writes on the board. A student who looks away briefly is a line or two behind.",
                    "Only the teacher writes on the board; everyone copies it. Read from any copy; it may be a line behind.")
rp_analogy.box(240, 30, 280, 120, None, "paper")
rp_analogy.head(380, 60, "main board", size=20)
rp_analogy.text(380, 92, "1. cache-aside", size=16)
rp_analogy.text(380, 114, "2. replication", size=16)
rp_analogy.text(380, 136, "3. …", size=16)
rp_analogy.note(380, 22, "only the teacher writes here", "pen")
for i, x in enumerate([60, 300, 540]):
    rp_analogy.icon("book", x + 40, 180, 1.0)
    rp_analogy.arrow(380, 154, x + 70, 180, dash=True)
rp_analogy.note(130, 256, "up to date")
rp_analogy.note(370, 256, "up to date")
rp_analogy.note(610, 256, "one line behind", "red")

rp_how = Doodle(760, 320, "Leader-follower replication. All writes go to the leader, which records them in its log and streams the log to two followers. Followers apply the changes and serve read queries. If the leader fails, one follower is promoted to be the new leader. Synchronous replication waits for a follower to confirm; asynchronous does not.",
                "Writes go to the leader; its change log streams to followers, which serve reads and can take over.")
rp_how.box(20, 40, 140, 56, "writes", "blue")
rp_how.box(20, 210, 140, 56, "reads", "blue")
rp_how.arrow(166, 68, 266, 88)
rp_how.db(330, 60, None, w=120, h=70, fill="y")
rp_how.head(330, 120, "leader", size=19)
rp_how.text(330, 172, "change log →", size=16)
rp_how.arrow(396, 90, 536, 60, label="sync (wait for ack)", lx=470, ly=48)
rp_how.arrow(396, 120, 536, 210, dash=True, label="async (don't wait)", lx=560, ly=160, anchor="start")
rp_how.db(610, 40, None, w=110, h=60, fill="green")
rp_how.head(610, 92, "follower 1", size=17)
rp_how.db(610, 190, None, w=110, h=60, fill="green")
rp_how.head(610, 242, "follower 2", size=17)
rp_how.arrow(166, 238, 548, 230, color="green", label="read from followers", lx=330, ly=290)
rp_how.note(660, 300, "leader dies → promote one", "red")

REPLICATION = dict(
    slug="replication",
    kicker="a.k.a. “one writes, many copy”",
    tldr="Keep <b>copies of the same data</b> on several machines. One node, the <b>leader</b>, accepts all writes and streams its change log to <b>followers</b>, which apply the changes in order. Followers serve <b>reads</b> and can be <b>promoted</b> if the leader fails.",
    chips=[("Family", "data / availability"), ("Lives in", "the database layer"), ("Also called", "primary–replica, master–slave (old term)"), ("Pairs with", "leader election, sharding, CQRS")],
    problem="""  <p class="lead">A single database server is both a <span class="hl-pink">single point of failure</span> and a single bottleneck.</p>
  <ul>
    <li>If its disk or machine dies, the app is down until it's restored, and data since the last backup is lost.</li>
    <li>All reads land on one machine: app queries, reports and analytics compete for CPU.</li>
    <li>Users far away (another continent) get slow responses from one location.</li>
    <li>Maintenance (patching, upgrades) means downtime.</li>
  </ul>""",
    problem_figs=[rp_problem],
    analogy_side="the teacher's board",
    analogy="""  <p>In class, <b>only the teacher writes on the board</b>. Every student copies it into their own notebook. When you need to check something, you read your own copy instead of crowding round the board.</p>
  <ul>
    <li>If the teacher steps out, a student with good notes can take over at the board (a <b>failover</b>).</li>
    <li>A student who looked away is a line or two behind: <b>replication lag</b>. Reading from their notebook might miss the latest line.</li>
    <li>For an exam answer that must be exactly right, you check the board itself: <b>read from the leader</b>.</li>
  </ul>""",
    analogy_figs=[rp_analogy],
    map=[("The teacher at the board", "The leader (primary)"),
         ("Students' notebooks", "Followers (replicas)"),
         ("Copying line by line, in order", "Streaming the change log (WAL / binlog)"),
         ("A student a line behind", "Replication lag"),
         ("Checking your own notebook", "Reads served by followers"),
         ("A student takes over the board", "Promoting a follower on failover")],
    how_side="a log, shipped in order",
    how="""  <p>The leader writes every change to a <b>log</b> (Postgres WAL, MySQL binlog). Followers receive the log and replay it in the same order, so they end up with the same data.</p>""",
    how_figs=[rp_how],
    steps=[("Send all writes to the leader", "One place decides the order of writes, so there are no write conflicts."),
           ("Stream the log", "The leader ships each change to followers. <b>Synchronous</b>: the commit waits for at least one follower (no data loss on failover, slower). <b>Asynchronous</b>: it doesn't wait (fast, but recent writes can be lost)."),
           ("Read from followers", "Route read-only queries, reports and analytics to followers. Accept that they may lag by milliseconds or seconds."),
           ("Handle read-your-writes", "After a user changes something, read their data from the leader (or wait for the follower to catch up) for a short time."),
           ("Fail over safely", "Detect the leader is down, promote the most up-to-date follower, repoint clients, and make sure the old leader can't keep accepting writes (fencing).")],
    vocab=[("Leader / primary", "The node that accepts writes."),
           ("Follower / replica", "A node that copies the leader's changes."),
           ("Replication lag", "How far behind a follower is."),
           ("Sync vs async", "Whether a commit waits for followers to confirm."),
           ("Failover", "Promoting a follower when the leader fails."),
           ("Split brain", "Two nodes both acting as leader at once.")],
    code=dict(file="db.ts", note="route reads and writes", src="""
const leader   = new Pool({ host: "db-leader" });
const follower = new Pool({ host: "db-replicas" });          // load-balanced replicas

export async function placeOrder(order: Order) {
  await leader.query("INSERT INTO orders ...", [order.id]);   // writes: leader only
  recentlyWrote.set(order.customerId, Date.now());
}

export async function myOrders(customerId: string) {
  // read-your-writes: just after a write, read from the leader
  const fresh = Date.now() - (recentlyWrote.get(customerId) ?? 0) < 5_000;
  const pool = fresh ? leader : follower;
  return pool.query("SELECT * FROM orders WHERE customer_id = $1", [customerId]);
}
"""),
    tools="built in: Postgres streaming replication (+ Patroni for failover), MySQL replication / Group Replication, AWS RDS / Aurora read replicas and Multi-AZ, MongoDB replica sets, Redis replicas + Sentinel.",
    gains=["<b>High availability</b>: a follower can take over in seconds.",
           "<b>Read scale</b>: add followers for more read capacity.",
           "<b>Isolation</b>: reports and backups run on followers.",
           "<b>Lower latency</b> with followers near users in other regions.",
           "<b>Durability</b>: data exists on several machines."],
    losses=["<b>Replication lag</b>: followers can return stale data.",
            "<b>Writes don't scale</b>: still one leader.",
            "<b>Failover is tricky</b>: lost async writes, split brain.",
            "<b>More machines</b> and monitoring.",
            "<b>App complexity</b> for routing and read-your-writes."],
    baseline="Each line compares <b>a single database server</b> to the same database with <b>a leader and replicated followers</b>.",
    ratings=[(4, 3, "Lag, routing reads and failover behaviour to understand."),
             (4, 3, "Extra servers (often managed, but billed)."),
             (2, 4, "Upgrades can roll through followers, then fail over."),
             (3, 3, "Need tests for lag and failover; mostly neutral."),
             (2, 4, "Reads scale out; writes still go to one leader."),
             (2, 3, "Adding a follower takes time to copy data."),
             (1, 4, "A failed leader is replaced by a follower."),
             (3, 4, "Reads spread out; sync replication slows writes a little."),
             (3, 3, "Neutral.")],
    pitfalls=[("Reading your own write from a follower", "A user updates their profile, the page reloads from a lagging follower and shows the old name.", "read-your-writes from the leader for a short window, or wait for the follower's position."),
              ("Assuming async = no data loss", "The leader dies with 2 seconds of unreplicated writes; they're gone after failover.", "synchronous (or semi-sync) to at least one follower for important data."),
              ("Split brain", "The old leader comes back and keeps accepting writes alongside the new one.", "fencing (see note 18), a consensus-based failover manager."),
              ("Followers as backups", "Someone runs DELETE without WHERE, and it replicates everywhere within milliseconds.", "replicas are not backups; keep point-in-time backups too."),
              ("Unmonitored lag", "A follower falls 3 hours behind and serves very stale reports.", "alert on lag; remove lagging followers from the read pool.")],
    use=["You need the database to survive a machine or zone failure.",
         "Reads far outnumber writes.",
         "Reports and analytics shouldn't slow the app.",
         "Users in several regions need fast reads."],
    skip=["Writes are the bottleneck (shard instead, or as well).",
          "Every read must be perfectly up to date and you can't route to the leader.",
          "A dev/test database where downtime doesn't matter.",
          "Your managed database already does it (just turn it on)."],
    related=["<b>Leader election</b> · failover", "<b>Sharding</b> · each shard is replicated", "<b>CQRS</b>", "<b>Cache-aside</b>", "<b>Multi-leader / leaderless</b> replication"],
    quiz=[("Sync vs async replication: which can lose data on failover?", "Asynchronous: the leader may have acknowledged writes that never reached a follower before it died."),
          ("Does adding followers increase write capacity?", "No. All writes still go through the single leader; followers add read capacity and availability."),
          ("What is read-your-writes consistency?", "A user always sees their own recent changes, e.g. by reading from the leader just after they write."),
          ("Why are replicas not a backup?", "Mistakes like accidental deletes replicate to every follower; backups let you go back in time.")],
    remember="One <span class=\"hl\">writer</span>, many readers, and every reader might be a little behind. Know which reads can wait and which must ask the leader.",
    sources=["Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, chapter 5 “Replication”.",
             "PostgreSQL docs, “High Availability, Load Balancing, and Replication”.",
             "AWS docs, “Working with read replicas” (RDS).",
             "Patroni docs, “Replication modes”."],
)

# ------------------------------------------------------------------ 17 Cache-Aside
ca_problem = Doodle(760, 250, "Doodle of the product page hitting the database for the same popular product 5,000 times a minute. Each query takes 40 milliseconds and the database CPU is at 85 percent, even though the product details rarely change.",
                    "The same unchanged answer is computed thousands of times a minute.")
ca_problem.box(20, 90, 150, 70, "product page", "blue", size=18)
for dy in (-24, -8, 8, 24):
    ca_problem.arrow(176, 125 + dy, 420, 125 + dy / 2, color="red" if dy > 0 else "")
ca_problem.note(300, 80, "5,000 × /min, same product", "red")
ca_problem.db(500, 80, None, w=150, h=90, fill="pink", stroke="red")
ca_problem.head(500, 140, "CPU 85%", size=19)
ca_problem.note(660, 70, "40 ms each", "red", anchor="start")
ca_problem.note(660, 110, "data changes", "pen", anchor="start")
ca_problem.note(660, 134, "once a day", "pen", anchor="start")

ca_analogy = Doodle(760, 250, "Doodle of a kitchen fridge and a grocery store. When you want milk you check the fridge first. If it's there, great, that took seconds. If not, you go to the store, buy milk, and put some in the fridge for next time. Milk has a use-by date so you throw it out after a while.",
                    "Check the fridge first. Empty? Go to the store, and put some in the fridge on the way back.")
ca_analogy.icon("cup", 30, 100, 1.1)
ca_analogy.note(60, 190, "want milk")
ca_analogy.arrow(100, 130, 220, 130, label="① check fridge", lx=160, ly=118)
ca_analogy.icon("fridge", 230, 70, 1.6)
ca_analogy.note(275, 200, "hit: 10 s ✓", "green")
ca_analogy.arrow(320, 110, 520, 110, dash=True, label="② empty? go to the store", lx=420, ly=98)
ca_analogy.icon("store", 530, 70, 1.6)
ca_analogy.note(585, 200, "miss: 20 min", "red")
ca_analogy.arrow(530, 160, 322, 160, label="③ put some in the fridge", lx=426, ly=184)
ca_analogy.note(380, 240, "use-by date = TTL", "pen")

ca_how = Doodle(760, 320, "Cache-aside flow. On a read, the app checks Redis first. On a hit it returns the cached value. On a miss it reads from the database, stores the result in the cache with a time-to-live, then returns it. On a write, the app updates the database and then deletes the cache key so the next read reloads it.",
                "Reads: cache first, database on a miss, then fill the cache. Writes: update the database, then delete the key.")
ca_how.box(20, 120, 140, 70, "app", "blue")
ca_how.box(320, 20, 170, 70, "Redis cache", "y")
ca_how.db(405, 200, None, w=140, h=60, fill="paper")
ca_how.head(405, 255, "database", size=18)
ca_how.arrow(166, 130, 314, 60, label="① GET product:42", lx=150, ly=56, anchor="start")
ca_how.arrow(314, 80, 166, 150, color="green", label="hit → return", lx=272, ly=140, anchor="start")
ca_how.arrow(166, 175, 330, 220, dash=True, label="② miss → SELECT", lx=170, ly=244, anchor="start")
ca_how.arrow(480, 196, 480, 96, label="③ SET … EX 300", lx=490, ly=150, anchor="start")
ca_how.box(580, 210, 160, 80, "on write:", "pink", sub="UPDATE db, DEL key", stroke="red")

CACHE = dict(
    slug="cache-aside",
    kicker="a.k.a. “check the fridge first”",
    tldr="Keep a copy of frequently read data in a fast cache (like Redis). The <b>application</b> checks the cache first; on a <b>miss</b> it reads the database and <b>puts the result in the cache</b> with an expiry (TTL). On a write, it updates the database and <b>deletes the cached copy</b>, so the next read loads fresh data.",
    chips=[("Family", "data / performance"), ("Lives in", "the application (cache is a side store)"), ("Also called", "lazy loading"), ("Pairs with", "TTLs, read replicas, CQRS")],
    problem="""  <p class="lead">Many systems read the same data <span class="hl-pink">far more often than it changes</span>: product details, prices, user profiles, configuration.</p>
  <ul>
    <li>The product page asks the database for the same popular item 5,000 times a minute.</li>
    <li>Each query takes 40 ms and uses CPU, so the database gets busy doing repeated work.</li>
    <li>Users wait for every one of those queries, and the database needs a bigger (pricier) machine.</li>
  </ul>""",
    problem_figs=[ca_problem],
    analogy_side="the fridge and the grocery store",
    analogy="""  <p>When you want milk, you <b>check the fridge first</b>. If it's there, you're done in seconds. If not, you go to the store (slow), buy some, and <b>put it in the fridge</b> so next time is quick.</p>
  <ul>
    <li>Milk has a <b>use-by date</b>. After that you throw it out and buy fresh. That's a <b>TTL</b>.</li>
    <li>If you switch to oat milk, you throw out the old carton straight away so nobody pours the wrong one: <b>invalidate on write</b>.</li>
    <li>The fridge is small, so the stuff you rarely use gets pushed out: <b>eviction (LRU)</b>.</li>
    <li>If ten flatmates find the fridge empty at once and all run to the store, that's a <b>cache stampede</b>.</li>
  </ul>""",
    analogy_figs=[ca_analogy],
    map=[("The fridge", "The cache (Redis, Memcached)"),
         ("The grocery store", "The database (slow, authoritative)"),
         ("Milk is in the fridge", "Cache hit"),
         ("Fridge empty, go to the store", "Cache miss → read the database"),
         ("Use-by date", "TTL (time to live)"),
         ("Throw out old milk when you switch", "Delete the key when the data changes")],
    how_side="lazy loading + invalidation",
    how="""  <p>The cache doesn't talk to the database; <b>the app sits beside both</b> and manages the cache itself (that's the “aside”).</p>""",
    how_figs=[ca_how],
    steps=[("Read: try the cache", "<code>GET product:42</code>. Hit? Return it. This is often under 1 ms."),
           ("Miss: load and fill", "Read from the database, then <code>SET product:42 … EX 300</code> (5-minute TTL), then return."),
           ("Write: update, then delete", "Update the database first, then <code>DEL product:42</code>. Deleting (not overwriting) avoids racing writers putting old values back."),
           ("Always set a TTL", "Even with invalidation, a TTL bounds how long any mistake or missed delete can serve stale data. Add a little random jitter to TTLs."),
           ("Protect against stampedes", "When a hot key expires, let one request reload it (a lock or “single flight”) while others wait or get the stale value.")],
    vocab=[("Cache hit / miss", "Found in the cache / not found, go to the source."),
           ("TTL", "How long a cached item lives before expiring."),
           ("Invalidation", "Removing a cached item because the source changed."),
           ("Eviction (LRU)", "Dropping least-recently-used items when memory is full."),
           ("Cache stampede", "Many requests missing at once and hammering the DB."),
           ("Hit ratio", "Hits ÷ all lookups; the main health metric.")],
    code=dict(file="product-cache.ts", note="cache-aside with Redis", src="""
export async function getProduct(id: string): Promise<Product> {
  const key = `product:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);                       // hit

  const product = await db.one("SELECT * FROM products WHERE id = $1", [id]);  // miss
  const ttl = 300 + Math.floor(Math.random() * 60);           // TTL + jitter
  await redis.set(key, JSON.stringify(product), { EX: ttl });
  return product;
}

export async function updatePrice(id: string, price: number) {
  await db.query("UPDATE products SET price = $1 WHERE id = $2", [price, id]);
  await redis.del(`product:${id}`);                           // delete, don't set
}
"""),
    tools="caches: Redis / Valkey, Memcached, AWS ElastiCache, Azure Cache for Redis; in-process caches (Caffeine, MemoryCache) for tiny hot data; CDNs do the same idea for HTTP responses.",
    gains=["<b>Much faster reads</b>: sub-millisecond instead of tens of milliseconds.",
           "<b>Less database load</b>, so a smaller or cheaper database.",
           "<b>Absorbs read spikes</b> on hot items.",
           "<b>Only caches what's actually used</b> (lazy loading).",
           "<b>Cache outage is survivable</b>: the app falls back to the database."],
    losses=["<b>Stale data</b> for up to the TTL, or longer if invalidation is missed.",
            "<b>Cache invalidation is famously hard</b> to get right.",
            "<b>First request after a miss is slower</b> (extra round trip).",
            "<b>Another system</b> to run, size and monitor.",
            "<b>Stampedes and hot keys</b> need extra care."],
    baseline="Each line compares <b>reading everything from the database</b> to the same app using <b>cache-aside with Redis</b>.",
    ratings=[(4, 3, "Simple to add, tricky to keep correct (invalidation, stampedes)."),
             (3, 4, "A small cache often replaces a much bigger database."),
             (4, 4, "Neutral."),
             (4, 3, "Need tests for misses, invalidation and stale data."),
             (3, 4, "Reads scale cheaply; the DB sees far less load."),
             (2, 4, "Hot items are served from memory during spikes."),
             (3, 3, "Can fall back to the DB, but a cold cache after an outage hurts."),
             (2, 5, "Hits are sub-millisecond."),
             (4, 3, "Every data change must remember its cache keys.")],
    pitfalls=[("Updating the cache instead of deleting", "Two writers race; the older value is written to the cache last and stays there until TTL.", "update the DB, then delete the key."),
              ("No TTL", "A missed invalidation serves the wrong price for weeks.", "always set a TTL as a safety net."),
              ("Cache stampede", "A hot key expires and 2,000 requests hit the database at the same moment.", "single-flight locking, early refresh, TTL jitter."),
              ("Caching everything", "Rarely read data fills memory and evicts the hot items.", "cache what's read often; measure the hit ratio."),
              ("Caching per-user data under shared keys", "User A's cart is shown to user B.", "include every varying input (user, locale, permissions) in the key.")],
    use=["Data is read much more often than it changes.",
         "Slight staleness (seconds to minutes) is acceptable.",
         "Database load or latency is the bottleneck.",
         "The same items are requested by many users."],
    skip=["Data changes constantly and must always be exact (balances, stock at checkout).",
          "Every request is unique (low hit ratio).",
          "The database is already fast enough.",
          "You can't find all the places that change the data."],
    related=["<b>Leader–follower replication</b> · read replicas", "<b>CQRS</b> · purpose-built read models", "<b>Read-through / write-through</b> caches", "<b>CDN</b>", "<b>Rate limiter</b>"],
    quiz=[("Why delete the cache key on write instead of setting the new value?", "Concurrent writers can race and leave an older value in the cache; deleting forces the next read to load the latest value from the database."),
          ("What is a cache stampede and one way to prevent it?", "Many requests miss on the same expired hot key and hit the database together. Use a lock/single-flight so one request reloads, or refresh early, or add TTL jitter."),
          ("Cache-aside vs read-through: who loads the data on a miss?", "In cache-aside the application loads it and fills the cache; in read-through the cache library/service loads it from the database itself."),
          ("What's the main metric to watch?", "The hit ratio (plus latency and evictions).")],
    remember="Fridge first, store second, and <span class=\"hl\">throw out</span> what changed. Every cached thing gets an expiry date.",
    sources=["Microsoft Azure Architecture Center, “Cache-Aside pattern”.",
             "AWS whitepaper, “Database Caching Strategies Using Redis”.",
             "Facebook, “Scaling Memcache at Facebook” (NSDI 2013).",
             "Redis docs, “Client-side caching” and key expiration."],
)

# ------------------------------------------------------------------ 18 Leader Election
le_problem = Doodle(760, 260, "Doodle of three copies of a billing job running on three servers. Every night at midnight all three send the monthly invoices, so every customer gets three invoices. If only one server ran the job and it died, nobody would get an invoice.",
                    "Run the job everywhere and it happens three times. Run it on one fixed server and it stops when that server dies.")
for i in range(3):
    y = 30 + i * 70
    le_problem.box(20, y, 160, 50, f"server {i + 1}", "paper", size=18)
    le_problem.arrow(186, y + 25, 400, 130, color="red", label="00:00 send invoices" if i == 0 else None, lx=290, ly=60)
le_problem.box(406, 90, 170, 80, "customer", "pink", sub="3 invoices ✗", stroke="red")
le_problem.note(380, 250, "…but pin it to server 1 only, and when server 1 dies: 0 invoices", "red")

le_analogy = Doodle(760, 250, "Doodle of a group project where the team chooses one note-taker, who holds the meeting's talking stick. The note-taker's turn lasts a fixed time and must be renewed. If they leave, the stick goes back on the table and someone else picks it up.",
                    "One person holds the talking stick. If they leave or their turn expires, someone else picks it up.")
le_analogy.icon("baton", 330, 80, 1.6)
le_analogy.note(380, 200, "the talking stick", "pen")
for i, (x, y) in enumerate([(80, 60), (80, 160), (580, 60), (580, 160)]):
    le_analogy.box(x, y, 120, 50, ["Ana", "Ben", "Cy", "Dee"][i], "green" if i == 0 else "paper", size=19)
le_analogy.arrow(206, 85, 320, 120, color="green", label="holds it (for 30 s)", lx=240, ly=60, anchor="start")
le_analogy.note(380, 240, "leaves? stick is free → next one grabs it", "pen")

le_how = Doodle(760, 320, "Leader election with a lease. Three instances try to acquire a lease key in a coordination service such as etcd or ZooKeeper. Instance B wins with fencing token 7 and must renew the lease every few seconds. Followers watch the key. If B stops renewing, the lease expires and another instance acquires it with token 8. The database rejects writes carrying an older token.",
                "Whoever holds the lease leads. It must keep renewing; each new leader gets a higher fencing token.")
le_how.box(270, 20, 220, 80, "etcd / ZooKeeper", "y", sub="lease: leader = B, token 7")
for i, (name, st) in enumerate([("A", "follower"), ("B", "LEADER"), ("C", "follower")]):
    x = 40 + i * 250
    le_how.box(x, 170, 170, 70, f"instance {name}", "green" if name == "B" else "paper", sub=st)
    if name == "B":
        le_how.arrow(x + 85, 166, 380, 104, color="green", label="renew every 3 s", lx=x + 110, ly=150, anchor="start")
    else:
        le_how.arrow(x + 85, 166, 380, 104, dash=True)
le_how.note(125, 150, "watching…", "pen")
le_how.box(240, 270, 280, 46, "DB: reject token < 7", "pink", stroke="red", size=17)
le_how.arrow(375, 244, 380, 266)

LEADER = dict(
    slug="leader-election",
    kicker="a.k.a. “exactly one of us does it”",
    tldr="When a job must be done by <b>exactly one</b> instance at a time (a scheduler, a shard owner, the primary database), the instances <b>elect a leader</b> through a coordination service. The leader holds a <b>lease that it must keep renewing</b>; if it dies or stalls, the lease expires and <b>another instance takes over</b>. A <b>fencing token</b> stops a stale old leader from doing damage.",
    chips=[("Family", "coordination"), ("Lives in", "a consensus store (etcd, ZooKeeper, Consul)"), ("Built on", "Raft / Paxos / ZAB"), ("Pairs with", "replication, sharding, distributed locks")],
    problem="""  <p class="lead">You run several copies of a service for availability, but some work <span class="hl-pink">must happen exactly once</span>.</p>
  <ul>
    <li>A nightly invoice job runs on all three instances, so customers get three invoices.</li>
    <li>Pin it to “server 1” instead, and when server 1 dies, nobody gets invoices.</li>
    <li>Two database nodes both think they're the primary and accept conflicting writes (<b>split brain</b>).</li>
    <li>Two workers both think they own partition 5 and process it twice.</li>
  </ul>""",
    problem_figs=[le_problem],
    analogy_side="the talking stick",
    analogy="""  <p>In a group meeting, only the person holding the <b>talking stick</b> takes the official notes. Everyone agrees who holds it. Their turn lasts a fixed time and they have to <b>renew</b> it by saying “still here”. If they leave, the stick goes back on the table and the next person picks it up.</p>
  <ul>
    <li>Exactly one note-taker at a time, but never zero for long.</li>
    <li>If Ana nods off and wakes up later, she might still think she's the note-taker. So each new turn gets a <b>number</b>, and the official notebook only accepts notes from the latest number: a <b>fencing token</b>.</li>
  </ul>""",
    analogy_figs=[le_analogy],
    map=[("The team", "Instances of a service"),
         ("Holding the talking stick", "Being the leader (holding the lease)"),
         ("“Still here” every few seconds", "Lease renewal / heartbeat"),
         ("Turn expires → stick back on the table", "Lease expiry → new election"),
         ("Agreeing who has the stick", "Consensus (Raft/Paxos) in etcd / ZooKeeper"),
         ("Turn number on the notes", "Fencing token: higher number wins")],
    how_side="leases, watches and fencing",
    how="""  <p>Don't invent your own election algorithm. Use a <b>strongly consistent coordination service</b> that already runs consensus, and build on its leases.</p>""",
    how_figs=[le_how],
    steps=[("Campaign", "Each instance tries to create the key <code>/election/billing</code> with a lease (e.g. 15 s TTL). The store guarantees only one succeeds."),
           ("Lead and renew", "The winner becomes leader and renews its lease well before it expires (e.g. every 5 s). It stops leading the moment a renewal fails."),
           ("Watch", "Followers watch the key. When it disappears (leader crashed or partitioned away), they campaign again."),
           ("Fence", "Every new leadership term gets a higher number (fencing token). Downstream systems reject writes with an older token, so a paused old leader can't overwrite the new one's work."),
           ("Design for the gap", "During failover there's briefly no leader. Make the work resumable and idempotent so a new leader can pick up where the last one stopped.")],
    vocab=[("Leader", "The one instance currently allowed to do the job."),
           ("Lease", "Time-limited leadership that must be renewed."),
           ("Consensus", "Agreement among nodes despite failures (Raft, Paxos)."),
           ("Split brain", "Two nodes acting as leader at the same time."),
           ("Fencing token", "A number that increases with every new leader."),
           ("Quorum", "A majority of nodes needed to make a decision.")],
    code=dict(file="billing-scheduler.ts", note="etcd-style election (pseudo-client)", src="""
const election = etcd.election("billing-scheduler", { leaseTtlSeconds: 15 });

for (;;) {
  const term = await election.campaign(myId);         // blocks until we win
  log.info(`leader for term ${term.token}`);           // token always increases
  try {
    while (await term.isStillLeader()) {               // lease auto-renewed
      const job = await nextDueJob();
      if (job) await runInvoices(job, { fencingToken: term.token });
      await sleep(1_000);
    }
  } finally {
    await term.resign();                                // step down cleanly
  }
}

// downstream: refuse work from an old leader
// UPDATE jobs SET ... WHERE id = $1 AND last_token <= $2
"""),
    tools="building blocks: etcd (Kubernetes uses it; client-go leaderelection with Lease objects), Apache ZooKeeper / Curator recipes, HashiCorp Consul sessions, Postgres advisory locks for small setups; Raft inside CockroachDB, Kafka KRaft, Patroni.",
    gains=["<b>Exactly-one execution</b> without a single fixed server.",
           "<b>Automatic failover</b> when the leader dies.",
           "<b>No split brain</b> when combined with fencing.",
           "<b>Simple model for singleton jobs</b> (schedulers, compactors).",
           "<b>Foundation for replication and sharding</b> ownership."],
    losses=["<b>Depends on a consensus cluster</b> that must itself be highly available.",
            "<b>Failover gap</b>: a few seconds with no leader.",
            "<b>The leader is a bottleneck</b> for its work.",
            "<b>Subtle bugs</b> around clocks, GC pauses and partitions.",
            "<b>Hard to test</b> without fault injection."],
    baseline="Each line compares running a singleton job on <b>one fixed server</b> to <b>several instances with lease-based leader election</b> and fencing.",
    ratings=[(4, 2, "Leases, renewals, fencing and partitions are subtle."),
             (4, 3, "A consensus cluster (or managed equivalent) to run."),
             (2, 4, "Instances can be replaced or upgraded one at a time."),
             (3, 2, "Needs failure injection: pauses, partitions, clock skew."),
             (2, 2, "Only one leader works at a time; shard leadership to scale."),
             (2, 2, "Leadership doesn't help with spikes."),
             (1, 4, "The job survives a server dying; fencing prevents split brain."),
             (3, 3, "Neutral; elections add a short pause on failover."),
             (2, 3, "Leadership can move with the fleet instead of being pinned.")],
    pitfalls=[("Rolling your own election", "A homemade “lowest IP wins” scheme breaks during a network partition and two leaders appear.", "use etcd / ZooKeeper / Consul or a library built on them."),
              ("No fencing", "The old leader pauses for 20 s (GC), its lease expires, a new leader starts, then the old one wakes and keeps writing.", "fencing tokens checked by the resource being written."),
              ("Lease shorter than pauses", "A 2-second lease with frequent 3-second GC pauses causes constant leader flapping.", "lease TTL comfortably above worst-case pauses; renew at about 1/3 of TTL."),
              ("Trusting the local clock", "Leader decides it still holds the lease based on its own clock, which drifted.", "rely on the coordination service's view and stop work as soon as renewal fails."),
              ("Leader does everything", "All work goes through one leader, which becomes the bottleneck.", "elect leaders per shard/partition, not one global leader.")],
    use=["A job must run exactly once at a time (scheduler, cron, compaction).",
         "One node must own a resource (a shard, a partition, the primary DB).",
         "You need automatic failover for that role.",
         "You already run (or can use) etcd, ZooKeeper or Consul."],
    skip=["The work can be split and done by everyone (use competing consumers).",
          "Duplicates are harmless and the job is idempotent anyway.",
          "A managed scheduler or database already handles failover for you.",
          "A single instance with a fast restart is good enough."],
    related=["<b>Leader–follower replication</b> · failover", "<b>Sharding</b> · leader per shard", "<b>Service discovery</b> · same stores", "<b>Distributed lock</b>", "<b>Idempotent consumer</b>"],
    quiz=[("Why does a leader need a lease that expires?", "So that if the leader crashes or is cut off, leadership is automatically released and another instance can take over."),
          ("What problem does a fencing token solve?", "A stale leader that was paused or partitioned can't overwrite the new leader's work, because resources reject requests with an older (lower) token."),
          ("Why use etcd or ZooKeeper instead of a simple database row?", "They provide consensus-backed, strongly consistent leases and watches that stay correct during network partitions and node failures."),
          ("Your leader is overloaded. What's the usual fix?", "Partition the work and elect a leader per partition/shard, spreading leadership across instances.")],
    remember="Exactly <span class=\"hl\">one</span> leader, never for free: borrow leadership with a lease, keep renewing it, and fence off the ghosts of leaders past.",
    sources=["Martin Kleppmann, “How to do distributed locking” (fencing tokens).",
             "Diego Ongaro &amp; John Ousterhout, “In Search of an Understandable Consensus Algorithm (Raft)”.",
             "Microsoft Azure Architecture Center, “Leader Election pattern”.",
             "Kubernetes docs, “Leases” (coordination.k8s.io)."],
)

NOTES = [SHARDING, REPLICATION, CACHE, LEADER]
