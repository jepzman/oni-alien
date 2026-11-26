# Vol. 3 · going deeper (November 2026): a longer chapter inside four key notes.
# Each chapter starts where the note stops. Merged into the notes by scripts/build_notes.py (load_content),
# like revisions.py; the shape is the same `deep_dive` field Book 3 uses.

# ------------------------------------------------------------------ Indexing
ix_d1 = Doodle(760, 300, "Two query plans for the same query. Before the index: Limit, then Sort on placed_at, then a sequential scan of orders that reads 2.4 million rows and throws away all but 20, in 1,840 milliseconds. After the composite index: Limit, then an index-only scan on orders_customer_recent that reads 4 pages, in 0.09 milliseconds.",
               "Same query, two plans. Read them from the bottom up: the deepest line runs first.")
ix_d1.head(190, 26, "before", size=20, color="red")
ix_d1.box(40, 40, 300, 50, "Limit (20 rows)", "paper", size=17)
ix_d1.arrow(190, 120, 190, 94)
ix_d1.box(40, 124, 300, 50, "Sort by placed_at", "pink", sub="sorts 31 rows in memory", size=17, subsize=14)
ix_d1.arrow(190, 204, 190, 178)
ix_d1.box(40, 208, 300, 58, "Seq Scan on orders", "pink", stroke="red", sub="reads 2,400,000 · keeps 31", size=17, subsize=14)
ix_d1.note(190, 292, "1,840 ms · 41,000 pages read", "red")
ix_d1.head(570, 26, "after", size=20, color="green")
ix_d1.box(420, 40, 300, 50, "Limit (20 rows)", "paper", size=17)
ix_d1.arrow(570, 150, 570, 94)
ix_d1.box(420, 154, 300, 70, "Index Only Scan", "green", sub="orders_customer_recent", size=17, subsize=14)
ix_d1.note(570, 292, "0.09 ms · 4 pages read", "green")

ix_d2 = Doodle(760, 330, "The same rows in two indexes. In an index on customer_id then placed_at, all of customer 42's orders sit next to each other, newest first, so the database reads one short run and stops. In an index on placed_at then customer_id, customer 42's orders are scattered between other customers', so the database must read far more entries and sort them.",
               "Equality column first: customer 42's rows form one run, already in the order you want.")
ix_d2.table(20, 30, "(customer_id, placed_at)", ["41 · 9 Nov", "42 · 14 Nov", "42 · 12 Nov", "42 · 3 Nov", "43 · 15 Nov", "43 · 1 Nov"],
            w=320, fill="green", hl=(1, 2, 3), size=17)
ix_d2.note(180, 250, "one run · read 3 · stop", "green")
ix_d2.table(420, 30, "(placed_at, customer_id)", ["15 Nov · 43", "14 Nov · 42", "12 Nov · 42", "9 Nov · 41", "3 Nov · 42", "1 Nov · 43"],
            w=320, fill="pink", hl=(1, 2, 4), size=17)
ix_d2.note(580, 250, "scattered · read many, then sort", "red")
ix_d2.note(380, 312, "rule of thumb: equality → sort → range")

ix_d3 = Doodle(760, 250, "One insert into the orders table writes the row to the table and also one entry into each of its six indexes, plus the write-ahead log for every one of them. Two of the six indexes have never been used by a query.",
               "Every index is paid for on every insert, and most updates.")
ix_d3.box(20, 90, 150, 70, "INSERT", "y", sub="one order", size=19)
ix_d3.box(230, 20, 150, 50, "table row", "blue", size=16)
for i, (name, used) in enumerate([("pk (id)", True), ("customer, date", True), ("status", True), ("email", True), ("legacy_ref", False), ("created_by", False)]):
    x = 230 + (i % 3) * 176
    y = 100 + (i // 3) * 66
    ix_d3.box(x, y, 160, 50, name, "green" if used else "pink", stroke="" if used else "red", sub=None if used else "0 scans", size=15, subsize=13)
ix_d3.arrow(174, 110, 226, 50)
ix_d3.arrow(174, 125, 226, 125)
ix_d3.arrow(174, 140, 226, 190)
ix_d3.note(560, 52, "7 writes + WAL for each", "pen", size=16)

INDEXING_DEEP = dict(
    side="reading plans, column order, the cost of writes",
    intro="The note says “index what you filter, join and sort on, then measure”. This chapter is the measuring part: how to read a plan in four lines, how to pick the column order of a composite index, what each index costs on the write side, and the usual reasons the planner walks past an index you built.",
    parts=[
        ("Reading a plan in four lines", """  <p>Run the slow query with <code>EXPLAIN (ANALYZE, BUFFERS)</code>. The output is a tree; the most indented line runs first and feeds the line above it. For most problems you only need four things from it:</p>
  <ul>
    <li><b>The scan type</b> at the bottom. <i>Seq Scan</i> reads the whole table. <i>Index Scan</i> uses the index and then visits the table. <i>Index Only Scan</i> answers from the index alone. <i>Bitmap Heap Scan</i> collects matches from an index first, then reads the table pages in order: good for medium-sized results.</li>
    <li><b>Rows removed by filter.</b> 2,400,000 read to keep 31 means the database is doing the filtering the index should do.</li>
    <li><b>Estimated vs actual rows.</b> If the planner expected 10 and got 300,000, its statistics are wrong: run <code>ANALYZE</code> on the table and look again.</li>
    <li><b>A Sort node.</b> A sort above a scan means the index doesn't deliver rows in the order you asked for. Often the fix is the same index with the sort column added.</li>
  </ul>
  <p>Then read <b>Buffers</b>: pages read from cache and disk. Time changes with load; pages read are a steadier way to compare two plans.</p>""", [ix_d1]),
        ("Choosing the column order", """  <p>A composite index is sorted by the first column, then by the second inside each value of the first, and so on, like a phone book by surname then first name. That gives a simple rule for most queries: <b>columns you compare with = first, then the column you sort by, then columns you compare with a range</b> (&lt;, &gt;, BETWEEN).</p>
  <p>For <code>WHERE customer_id = 42 ORDER BY placed_at DESC LIMIT 20</code>, the index <code>(customer_id, placed_at DESC)</code> puts customer 42's orders in one run, newest first. The database reads 20 entries and stops. The index <code>(placed_at, customer_id)</code> holds the same data, but customer 42's orders are spread across every date, so the database reads many more entries and sorts them.</p>
  <p>Two more points. A range column ends the useful part of the index: in <code>(customer_id, placed_at, status)</code> with a range on placed_at, the status column can only be filtered, not searched. And <b>one index can serve several queries</b> that share its leading columns: <code>(customer_id, placed_at)</code> also serves <code>WHERE customer_id = 42</code> on its own, so you don't need a separate index for that.</p>""", [ix_d2]),
        ("What every index costs", """  <p>Each index is a second copy of some columns that must stay in step with the table. Insert one order into a table with six indexes and the database writes the row, six index entries, and the write-ahead log for all seven. Updates to an indexed column do the same work again. Indexes also take disk and, more importantly, memory: the hot parts of every index compete with the table for the cache.</p>
  <p>So check what you are paying for. In PostgreSQL, <code>pg_stat_user_indexes</code> counts scans per index since the statistics were last reset. An index with <code>idx_scan = 0</code> after a month of normal traffic (and after checking replicas and month-end jobs) is a candidate to drop. Indexes that are a prefix of another, such as <code>(customer_id)</code> next to <code>(customer_id, placed_at)</code>, are usually redundant too.</p>
  <p>Drop with <code>DROP INDEX CONCURRENTLY</code>, one at a time, and keep the definition in a migration so it can come back in minutes.</p>""", [ix_d3]),
        ("Why the planner ignores your index", """  <p>When an index exists but the plan still shows a Seq Scan, the reason is usually one of these:</p>
  <ul>
    <li><b>The filter matches too much.</b> <code>status = 'delivered'</code> matches 90% of rows; reading the table in order is cheaper than jumping around. Index the rare values with a partial index instead.</li>
    <li><b>The column is wrapped.</b> <code>WHERE lower(email) = …</code> or <code>WHERE placed_at::date = …</code> can't use a plain index on the column. Index the expression, or rewrite the filter as a range.</li>
    <li><b>The types don't match.</b> Comparing a text column to a number can force a cast on every row.</li>
    <li><b>The pattern starts with a wildcard.</b> <code>LIKE '%lamp'</code> can't use a B-tree. Use a trigram index or full-text search.</li>
    <li><b>Statistics are stale</b> after a large load. Run <code>ANALYZE</code>.</li>
    <li><b>The table is small.</b> A few hundred rows fit in a couple of pages; a scan is genuinely the fastest plan. That's fine.</li>
  </ul>
  <p>Don't force the planner with hints. Fix the reason, then read the plan again.</p>""", []),
    ],
)

# ------------------------------------------------------------------ Optimistic locking
ol_d1 = Doodle(760, 340, "Two support agents load customer 7 at version 7. Ben saves first with If-Match version 7; the server updates the row to version 8 and returns 200. Ana saves next with If-Match version 7; the conditional update matches no row, so the server returns 412 Precondition Failed with the current version 8, and Ana's screen shows what changed.",
               "The version travels with the data: out in the ETag, back in If-Match.")
for x, who in [(110, "Ana"), (380, "API + database"), (650, "Ben")]:
    ix = 160 if who == "API + database" else 90
    ol_d1.box(x - ix // 2, 14, ix, 40, who, "blue" if who != "API + database" else "y", size=17)
    ol_d1.line(f"M{x} 58 V326", thin=True, dash=True)
ol_d1.arrow(380, 86, 116, 86, label="GET · ETag: v7", lx=248, ly=78)
ol_d1.arrow(380, 120, 644, 120, label="GET · ETag: v7", lx=512, ly=112)
ol_d1.arrow(650, 170, 386, 170, label="PUT · If-Match: v7", lx=518, ly=162)
ol_d1.arrow(380, 206, 644, 206, color="green", label="200 · now v8", lx=512, ly=198)
ol_d1.arrow(110, 250, 374, 250, label="PUT · If-Match: v7", lx=242, ly=242)
ol_d1.arrow(380, 290, 116, 290, color="red", label="412 · current is v8", lx=248, ly=282)
ol_d1.note(126, 320, "Ana sees what Ben changed", "red", anchor="start", size=16)

ol_d2 = Doodle(760, 256, "A three-way merge. The base version, Ana's version and Ben's version of a customer are compared field by field. Ben changed the phone number and Ana changed the address, so both changes are kept automatically. If both had changed the same field to different values, that one field would be a real conflict for a person to decide.",
               "Compare both edits with the version they started from: only the same field changed twice is a real conflict.")
ol_d2.table(20, 30, "base (v7)", ["name: Joost", "phone: 0612…", "address: Kade 4"], w=160, fill="paper", size=15)
ol_d2.table(210, 30, "Ben (saved v8)", ["name: Joost", "phone: 0687…", "address: Kade 4"], w=170, fill="blue", hl=(1,), size=15)
ol_d2.table(410, 30, "Ana (from v7)", ["name: Joost", "phone: 0612…", "address: Dam 1"], w=170, fill="y", hl=(2,), size=15)
ol_d2.arrow(590, 90, 618, 90)
ol_d2.table(620, 30, "merged (v9)", ["name: Joost", "phone: 0687…", "address: Dam 1"], w=130, fill="green", hl=(1, 2), size=14)
ol_d2.note(380, 178, "different fields → keep both, no question asked", "green")
ol_d2.note(380, 210, "same field, different values → ask the person", "red")
ol_d2.note(380, 240, "(they're the only real conflict)", size=16)

OPTIMISTIC_DEEP = dict(
    side="HTTP versions, merging, contention, bigger objects",
    intro="The note shows the version check in one UPDATE. In a real application the version has to travel to the browser and back, someone has to decide what a conflict looks like on screen, and there are workloads where optimistic locking is the wrong tool. This chapter covers all three, and what to version when the thing you edit is more than one row.",
    parts=[
        ("Carrying the version over HTTP", """  <p>HTTP already has the parts. When the API returns a resource, it sends its version in an <b>ETag</b> header (<code>ETag: "v7"</code>). When the client saves, it sends the version it started from in <b>If-Match</b>. The server turns that into the conditional UPDATE from the note. If no row matched, it answers <b>412 Precondition Failed</b> and includes the current version, so the client can show what changed.</p>
  <p>Some APIs put the version in the body instead and answer <b>409 Conflict</b>. Either works; pick one and use it everywhere. Two rules matter more:</p>
  <ul>
    <li><b>Require the version on writes.</b> A PUT without If-Match should be rejected (428 Precondition Required), or the check is optional and someone will skip it.</li>
    <li><b>Don't trust a client-made version.</b> The version comes from the server; the client only returns it.</li>
  </ul>
  <p>In an HTML form, the version is a hidden field. In a single-page app, keep it with the data in the cache, and update it from every successful save.</p>""", [ol_d1]),
        ("What to do with a conflict", """  <p>“Reload and try again” is the simplest policy, and it is fine when edits are small. When a person has spent ten minutes on a form, throwing their work away is not fine. There are three better options, from simple to clever:</p>
  <ul>
    <li><b>Show both.</b> Keep the person's input on screen, show the current values next to it, and let them choose per field.</li>
    <li><b>Merge different fields automatically.</b> Compare both edits with the version they started from (a three-way merge). If they changed different fields, keep both changes and save. Only the same field changed to different values needs a person.</li>
    <li><b>Last writer wins, on purpose.</b> For fields where the newest value is simply right (a “last seen” time, a status set by a device), skip the check for that field.</li>
  </ul>
  <p>To merge, the client needs the base version's values, not just its number. Keep them with the form when it loads.</p>""", [ol_d2]),
        ("When contention is high", """  <p>Optimistic locking bets that conflicts are rare. When many writers hit the same row (a stock counter during a sale, a shared budget, a seat map), the bet fails: most updates miss, retry, and miss again, and the database does the work several times.</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Situation</th><th scope="col">Better tool</th></tr></thead><tbody>
    <tr><td>A counter goes up or down</td><td>An atomic update: <code>SET qty = qty - 1 WHERE sku = $1 AND qty &gt; 0</code>. No version needed.</td></tr>
    <tr><td>A short read-decide-write on a hot row</td><td>A pessimistic lock: <code>SELECT … FOR UPDATE</code> inside a short transaction.</td></tr>
    <tr><td>Many writers to one thing, order matters</td><td>Put the changes on a queue and let one worker apply them.</td></tr>
    <tr><td>Rare conflicts, people editing</td><td>Optimistic locking, as in the note.</td></tr>
  </tbody></table></div>
  <p>If you do retry automatically, retry a few times with a short random wait, and only for changes a program made. Never silently re-apply a person's edit on top of data they haven't seen.</p>""", []),
        ("Versioning something bigger than a row", """  <p>An order with lines, a document with sections: the thing the user edits is several rows. Give the <b>whole object one version</b>, on its top row (the aggregate root), and increase it whenever anything inside changes, in the same transaction. Two people editing different lines of the same order then conflict, which is usually right: the order total depends on all of them.</p>
  <p>The same idea appears outside SQL. Event stores append with an <b>expected version</b> (see Event Sourcing in Vol. 1). DynamoDB has <b>conditional writes</b>, and object stores such as S3 accept <b>If-Match</b> on uploads. Each one is the same compare-and-set: “write this only if it is still the version I read.”</p>""", []),
    ],
)

# ------------------------------------------------------------------ Change data capture
cdc_d1 = Doodle(760, 250, "How a CDC connector starts. First it opens a consistent snapshot of the tables at log position 1000 and emits every existing row as a read event. Then it streams changes from the log starting exactly at position 1000, so no change is missed or doubled between the two phases.",
                "Snapshot first, then the log from the same position: nothing falls through the gap.")
cdc_d1.arrow(30, 160, 740, 160)
cdc_d1.note(740, 186, "log position →", anchor="end", size=16)
cdc_d1.box(30, 50, 300, 80, "1 · snapshot", "y", sub="every existing row · op = r", size=19)
cdc_d1.box(400, 50, 340, 80, "2 · stream the log", "green", sub="op = c / u / d, in commit order", size=19)
cdc_d1.line("M360 30 V200", color="pen", dash=True)
cdc_d1.note(360, 226, "LSN 1000: snapshot taken here, stream starts here", "pen", size=17)

cdc_d2 = Doodle(760, 270, "A replication slot with a stopped consumer. The database keeps every write-ahead log segment after the consumer's last confirmed position. The consumer stopped on Friday; by Monday 60 gigabytes of log are kept and the disk is almost full.",
                "A slot keeps the log until its consumer confirms it. A stopped consumer keeps it forever.")
for i in range(9):
    kept = i >= 2
    cdc_d2.box(20 + i * 80, 60, 70, 60, f"seg {i + 1}", "pink" if kept else "paper", stroke="red" if kept else "", size=15)
cdc_d2.arrow(195, 160, 195, 126, color="red", label="consumer stopped here (Fri)", lx=200, ly=180, anchor="start")
cdc_d2.arrow(720, 30, 720, 56, label="now (Mon)", lx=716, ly=24, anchor="end")
cdc_d2.note(470, 214, "kept: ~20 GB a day × 3 days = 60 GB", "red")
cdc_d2.note(470, 248, "alert on slot lag · cap it with max_slot_wal_keep_size", "pen", size=17)

CDC_DEEP = dict(
    side="snapshots, ordering, the slot, contracts",
    intro="The note sets up CDC in six steps. This chapter covers what happens in production: how the connector gets the rows that existed before it started, what order events really arrive in, how a stopped consumer can fill the database's disk, and how to stop other teams from depending on your table layout.",
    parts=[
        ("The first run: snapshot, then stream", """  <p>A new connector has a problem: the log only holds recent changes, but the search index needs every product, including the ones created years ago. So it starts in two phases. It opens a <b>consistent snapshot</b> of the tables at one log position and emits every existing row as a read event (<code>op: "r"</code>). Then it starts reading the log <b>from exactly that position</b>. Changes made during the snapshot arrive afterwards as normal events, so nothing is lost and nothing is applied twice.</p>
  <p>On a large table the snapshot can take hours and adds read load. Run it at a quiet time, or use an incremental snapshot (Debezium can snapshot in chunks while streaming). Consumers must handle a row arriving as a snapshot read and then as an update: one more reason they must be idempotent.</p>""", [cdc_d1]),
        ("What order events arrive in", """  <p>The log is in commit order, but the topic it lands in usually isn't one line. Kafka splits a topic into partitions and only keeps order <b>inside a partition</b>. Connectors use the row's primary key as the message key, so <b>all changes to one row stay in order</b>. Changes to different rows, and to different tables, can be read in any order by a consumer.</p>
  <p>Design consumers for that:</p>
  <ul>
    <li><b>Never assume a parent arrives before its child.</b> An order line may arrive before its order. Store it and link it later, or look the parent up.</li>
    <li><b>Use the log position to ignore old news.</b> Each event carries its position (<code>lsn</code>). If you already applied a later position for that row, skip the event.</li>
    <li><b>Transactions are split up.</b> One transaction that touched three tables becomes three events. If a consumer needs “all of it or none”, use the outbox pattern and publish one event per business change.</li>
  </ul>""", []),
        ("The slot that fills the disk", """  <p>PostgreSQL keeps write-ahead log segments until every <b>replication slot</b> has confirmed it has read them. That is what makes CDC reliable after a restart. It is also how CDC takes production down: if the connector stops for a weekend, the database keeps every segment written since, and the disk fills.</p>
  <p>Three defences:</p>
  <ul>
    <li><b>Alert on slot lag</b> in bytes (the query is on the note's card), long before the disk is at risk: for example at 5 GB and 20 GB.</li>
    <li><b>Cap it.</b> <code>max_slot_wal_keep_size</code> lets the database drop log a slot hasn't read. The slot then breaks and the connector needs a new snapshot, which is better than a full disk.</li>
    <li><b>Remove unused slots.</b> A slot for a connector that no longer exists keeps the log for nobody. Check <code>pg_replication_slots</code> after every decommission.</li>
  </ul>""", [cdc_d2]),
        ("Tables are not a contract", """  <p>Raw CDC events mirror your table layout. If other teams consume them, every column rename becomes their incident, and you can no longer change your own schema freely. Treat it like any other API:</p>
  <ul>
    <li><b>Inside your team</b> (cache, search index, your own read models), raw table events are fine; you change both sides together.</li>
    <li><b>For other teams</b>, publish business events through an outbox table and let CDC carry those (Debezium's outbox router does this). The event shape is designed and versioned, and your tables stay private.</li>
    <li><b>Register the schemas</b> (Avro, Protobuf or JSON Schema in a registry) and check compatibility in CI: adding an optional field is fine, renaming or removing one is a breaking change.</li>
  </ul>
  <p>And remember deletes: a delete event, and the empty “tombstone” that follows it in Kafka, must be handled by every consumer, or deleted products live on in the search index.</p>""", []),
    ],
)

# ------------------------------------------------------------------ Multitenancy
mt_d1 = Doodle(760, 300, "Three tenancy models side by side. Pool: all tenants share tables with a tenant id column; cheapest, one migration, weakest isolation. Bridge: a schema per tenant in one database; medium isolation, migrations run once per tenant. Silo: a database per tenant; strongest isolation and per-tenant backup and location, highest cost, many databases to run.",
               "Same app, three ways to keep tenants apart. Most products mix them.")
mt_d1.row([("pool", "shared tables", "green"), ("bridge", "schema per tenant", "y"), ("silo", "database per tenant", "blue")], y=24, h=70, gap=24, size=20, subsize=15)
for i, lines in enumerate([["€ per tenant: lowest", "1 migration", "isolation: RLS", "10,000 tenants: fine"],
                           ["€ per tenant: low", "1 migration × tenants", "isolation: schema", "10,000 tenants: slow"],
                           ["€ per tenant: high", "1 migration × tenants", "isolation: full", "own backup and region"]]):
    x = 14 + i * (244 + 24) + 122
    for k, s in enumerate(lines):
        mt_d1.text(x, 128 + k * 34, s, size=16)
mt_d1.note(380, 282, "typical: pool for most, silo for the few who need it", "pen")

mt_d2 = Doodle(760, 280, "Routing by tenant. Each request carries a tenant id. The app looks it up in a small catalog table that says which database holds that tenant. Most tenants point to the shared pool. Tenant 42, the biggest customer, points to its own database after it was moved; moving it only changed its row in the catalog.",
               "A catalog of where each tenant lives makes moving one a data copy and a one-row switch.")
mt_d2.box(20, 100, 140, 70, "request", "paper", sub="tenant = 42", size=18)
mt_d2.arrow(164, 135, 236, 135)
mt_d2.table(240, 60, "tenant catalog", ["7 → pool-1", "19 → pool-1", "42 → silo-42", "63 → pool-2"], w=200, fill="y", hl=(2,), size=16)
mt_d2.arrow(444, 150, 556, 196, color="green")
mt_d2.arrow(444, 110, 556, 70, dash=True)
mt_d2.db(620, 40, "pool-1 (shared)", w=90)
mt_d2.db(620, 170, "silo-42", w=90, fill="green")
mt_d2.note(340, 262, "move = copy rows · verify · flip one catalog row", "pen", size=17)

MULTITENANCY_DEEP = dict(
    side="choosing a model, noisy neighbours, moving a tenant, testing isolation",
    intro="The note picks shared tables with row-level security as the usual start. This chapter is about living with that choice: when to pick another model, what to do when one tenant slows everyone down, how to move a big customer to its own database without downtime, and how to test that one tenant can never see another's data.",
    parts=[
        ("Choosing a model with numbers", """  <p>The three models trade cost and operations against isolation. Count before you choose:</p>
  <ul>
    <li><b>Pool</b> (shared tables): one database to run and one migration per change. Isolation depends on every query having the tenant filter, which row-level security enforces. Fits thousands of small tenants.</li>
    <li><b>Bridge</b> (schema per tenant): stronger separation and easy per-tenant export. But a migration runs once per tenant: at 10,000 tenants and 2 seconds each, that is over five hours per change, and some will fail halfway.</li>
    <li><b>Silo</b> (database per tenant): full isolation, per-tenant backup, restore and data location (a customer that must stay in Germany). Costs the most, and you need automation to run hundreds of databases.</li>
  </ul>
  <p>Most products end up <b>mixed</b>: the pool for almost everyone, a silo for the few customers who pay for it or are required to have it. Design for that from day one: tenant id in every table and every key, and a catalog of where each tenant lives.</p>""", [mt_d1]),
        ("Noisy neighbours", """  <p>In the pool, one tenant's month-end report can take the CPU everyone else needs. You first need to <b>see</b> it: tag every query with the tenant (in <code>application_name</code> or a SQL comment) so slow-query logs and <code>pg_stat_statements</code> can be grouped by tenant. Then limit it:</p>
  <ul>
    <li><b>Rate limits per tenant</b> at the API, not just per user.</li>
    <li><b>Time limits</b>: a <code>statement_timeout</code> for interactive requests, and longer ones only for jobs.</li>
    <li><b>Separate heavy work</b>: run reports and exports on a read replica or a warehouse, and queue large jobs with a per-tenant concurrency limit.</li>
    <li><b>Fair queues</b>: if jobs share workers, take turns between tenants, so one tenant's 50,000 jobs don't wait in front of everyone else's 5.</li>
  </ul>
  <p>If a tenant still needs more than its share every day, that is a sign it belongs in its own database, which is the next part.</p>""", []),
        ("Moving a big tenant out", """  <p>Because every row has a tenant id and the app finds tenants through a catalog, moving one is a data job, not a rewrite:</p>
  <ol>
    <li>Create the new database with the same schema (same migrations).</li>
    <li>Copy the tenant's rows: a filtered dump for a small tenant, or logical replication or CDC filtered on <code>tenant_id</code> for a large one, so the copy keeps up while it runs.</li>
    <li>Verify: row counts and checksums per table, then run read-only traffic against the copy and compare answers.</li>
    <li>Switch: pause the tenant's writes for seconds, let the copy catch up, and change its row in the catalog. New requests go to the new database.</li>
    <li>Keep the old rows for a week in case you must move back, then delete them.</li>
  </ol>
  <p>The hard parts are global ids and shared tables (users that belong to several tenants, global sequences). Use keys that are unique across all databases (UUIDs, or tenant id plus a local id) so copied rows never collide.</p>""", [mt_d2]),
        ("Testing that isolation holds", """  <p>A data leak between tenants is the worst bug a SaaS product can have, so test isolation on purpose, not just features:</p>
  <ul>
    <li><b>A two-tenant test</b>: seed tenants A and B with similar data, run every API endpoint as A, and fail if any response contains an id of B's.</li>
    <li><b>A schema check in CI</b>: every table with a <code>tenant_id</code> column must have row-level security turned on and forced. Query <code>pg_class</code> for <code>relrowsecurity</code> and <code>relforcerowsecurity</code> and fail on any gap.</li>
    <li><b>The right database role</b>: the app must connect as a role that does <b>not</b> bypass RLS. Owners and superusers skip policies unless forced.</li>
    <li><b>Background jobs</b>: jobs and scripts run outside a request, so they often forget <code>SET LOCAL app.tenant_id</code>. With RLS forced, a forgotten setting returns no rows (or an error) instead of everyone's rows. Test that it fails closed.</li>
  </ul>""", []),
    ],
)

REVISIONS = {
    "indexing": dict(deep_dive=INDEXING_DEEP),
    "optimistic-locking": dict(deep_dive=OPTIMISTIC_DEEP),
    "change-data-capture": dict(deep_dive=CDC_DEEP),
    "multitenancy": dict(deep_dive=MULTITENANCY_DEEP),
}
