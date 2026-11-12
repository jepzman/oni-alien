# Vol. 3 · Growing: Table Partitioning, Multitenancy, Connection Pooling, Star Schema.

# ------------------------------------------------------------------ 12 Table Partitioning
tp_problem = Doodle(760, 260, "Doodle of one giant events table with two billion rows from five years. Queries for last week still wade through huge indexes, vacuum runs for days, and deleting data older than a year means a DELETE of 400 million rows that bloats the table and locks things up.",
                    "One table, five years, two billion rows: everything about it is slow, including deleting old data.")
tp_problem.table(20, 30, "events · 2 billion rows", ["2022 …", "2023 …", "2024 …", "2025 …", "2026 · last week ← we want this"], w=330, hl=(4,))
tp_problem.note(560, 50, "indexes: 400 GB", "red")
tp_problem.note(560, 90, "VACUUM: 3 days", "red")
tp_problem.note(560, 130, "DELETE … < 2025:", "red")
tp_problem.note(560, 156, "400M rows, hours, bloat", "red")
tp_problem.note(190, 220, "last week = 0.1% of the table", "pen")

tp_analogy = Doodle(760, 250, "Doodle of a filing cabinet with one drawer per year. To find a March 2026 receipt you open only the 2026 drawer. To throw away 2019 you pull out the whole drawer and empty it, without touching the others.",
                    "One drawer per year: open only the drawer you need; throw old years out drawer by drawer.")
tp_analogy.icon("cabinet", 60, 30, 2.6, fill="y")
tp_analogy.note(140, 228, "2024 · 2025 · 2026")
tp_analogy.arrow(240, 170, 400, 170, color="green", label="open only 2026", lx=320, ly=156)
tp_analogy.icon("receipt", 410, 130, 1.0)
tp_analogy.arrow(240, 60, 560, 60, color="red", label="pull out 2019, bin it", lx=400, ly=46)
tp_analogy.icon("bin", 570, 30, 1.3)

tp_how = Doodle(760, 290, "Range partitioning by month. The parent table events is split into partitions events_2026_09, events_2026_10 and events_2026_11, each a normal table with its own small indexes. A query for last week is routed only to the November partition, which is called partition pruning. Old months are detached and dropped instantly.",
                "Split by month: queries touch only the partitions they need; old months are dropped in a second.")
tp_how.box(250, 10, 260, 50, "events (parent)", "y", size=18)
for i, (t, f) in enumerate([("2026_09", "paper"), ("2026_10", "paper"), ("2026_11", "green")]):
    x = 30 + i * 240
    tp_how.arrow(380, 64, x + 100, 100)
    tp_how.box(x, 104, 200, 64, f"events_{t}", f, size=16, sub="own indexes")
tp_how.note(590, 200, "WHERE at > now() − 7 days", "green")
tp_how.note(590, 226, "→ scans only 2026_11", "green")
tp_how.box(30, 210, 300, 56, "DROP old partition: 1 s", "pink", stroke="red", size=17)
tp_how.arrow(130, 206, 130, 172, dash=True, color="red")

PARTITION = dict(
    slug="partitioning",
    kicker="a.k.a. “one drawer per year”",
    tldr="Split one huge table into <b>partitions</b>, smaller tables behind one name, by a <b>key you always filter on</b> (usually time, sometimes tenant or region). Queries <b>touch only the partitions they need</b> (pruning), maintenance runs per partition, and old data is removed by <b>dropping a partition</b> in a second instead of a giant DELETE. All inside one database.",
    chips=[("Family", "scaling data"), ("Kinds", "range, list, hash"), ("Built in", "PostgreSQL 10+, MySQL, SQL Server, Oracle"), ("Not the same as", "sharding (many databases)")],
    problem="""  <p class="lead">Append-heavy tables like events, logs, orders and metrics grow <span class="hl-pink">forever</span>. At billions of rows, everything gets heavy, even the queries that only want last week.</p>
  <ul>
    <li>Indexes no longer fit in memory, so “recent” queries slow down too.</li>
    <li>VACUUM, reindexing and backups take days.</li>
    <li>Deleting old data with <code>DELETE</code> is slow, bloats the table and floods replicas.</li>
  </ul>""",
    problem_figs=[tp_problem],
    analogy_side="the filing cabinet",
    analogy="""  <p>An office files receipts in a cabinet with <b>one drawer per year</b>. Looking for March 2026? Open the 2026 drawer only. Time to throw away 2019? <b>Pull out the whole drawer</b> and empty it, without sorting through the others.</p>
  <ul>
    <li>Each drawer is a <b>partition</b>.</li>
    <li>“Look only in 2026” is <b>partition pruning</b>.</li>
    <li>Emptying a drawer is <b>DROP / DETACH PARTITION</b>.</li>
  </ul>""",
    analogy_figs=[tp_analogy],
    map=[("The cabinet", "The parent table <code>events</code>"),
         ("A drawer per year", "A partition per month or year"),
         ("Open only the 2026 drawer", "Partition pruning on <code>WHERE at &gt; …</code>"),
         ("Bin the 2019 drawer", "<code>DROP TABLE events_2019</code>"),
         ("Add a drawer each January", "Create next month's partition ahead of time")],
    how_side="one name, many smaller tables",
    how="""  <p>The app still queries <code>events</code>. The database routes rows to the right partition on insert, and <b>skips partitions</b> that can't match the WHERE clause on read.</p>""",
    how_figs=[tp_how],
    steps=[("Pick the key you always filter on", "Usually time (<code>created_at</code>); queries without it must check every partition."),
           ("Pick the size", "Partitions of roughly 10–100 GB, or one per month; hundreds is fine, tens of thousands isn't."),
           ("Create partitions ahead of time", "A job (or pg_partman) creates next month's partition before rows arrive; add a DEFAULT partition as a safety net."),
           ("Index per partition", "Indexes on the parent are created on every partition and stay small."),
           ("Retire old data by dropping", "<code>DETACH PARTITION … CONCURRENTLY</code>, archive it, then drop.")],
    vocab=[("Partition", "One piece of a partitioned table."),
           ("Partition key", "Column(s) deciding which partition a row goes to."),
           ("Range / list / hash", "Split by ranges, by listed values, or by a hash."),
           ("Partition pruning", "Skipping partitions that can't match the query."),
           ("Detach", "Turning a partition back into a standalone table."),
           ("Sharding", "Partitioning across separate database servers.")],
    code=dict(file="events.sql", note="PostgreSQL 14+", src="""
CREATE TABLE events (
  id         bigint GENERATED ALWAYS AS IDENTITY,
  account_id bigint NOT NULL,
  kind       text   NOT NULL,
  at         timestamptz NOT NULL,
  PRIMARY KEY (id, at)                 -- the key must include the partition column
) PARTITION BY RANGE (at);

CREATE TABLE events_2026_11 PARTITION OF events
  FOR VALUES FROM ('2026-11-01') TO ('2026-12-01');
CREATE TABLE events_default PARTITION OF events DEFAULT;

CREATE INDEX ON events (account_id, at);   -- created on every partition

-- only events_2026_11 is scanned (see "Partitions removed" in EXPLAIN)
SELECT count(*) FROM events WHERE at > now() - interval '7 days';

-- retention: seconds, not hours
ALTER TABLE events DETACH PARTITION events_2025_10 CONCURRENTLY;
DROP TABLE events_2025_10;
"""),
    tools="tools: PostgreSQL declarative partitioning + pg_partman, TimescaleDB hypertables (automatic time partitions), MySQL partitioning, SQL Server partition schemes, BigQuery/Snowflake partitioned and clustered tables, Citus for partitioning across servers.",
    gains=["<b>Fast recent queries</b> thanks to pruning and small indexes.",
           "<b>Instant retention</b>: drop a partition, not 400M rows.",
           "<b>Maintenance per partition</b>: vacuum, reindex, archive.",
           "<b>Cold partitions</b> can move to cheaper storage."],
    losses=["<b>Queries without the key</b> scan every partition.",
            "<b>Unique keys must include</b> the partition column.",
            "<b>Partitions must be created</b> ahead of time.",
            "<b>More objects</b> to manage and monitor."],
    baseline="Each line compares <b>one huge table</b> to the same data <b>range-partitioned by month</b>.",
    ratings=[(4, 3, "More tables behind one name; key rules to learn."),
             (2, 4, "Pruning skips most of the data for time-filtered queries."),
             (3, 4, "Smaller indexes per partition are cheaper to update."),
             (4, 3, "Global uniqueness needs the partition key."),
             (2, 4, "Billions of rows stay workable in one database."),
             (3, 4, "Old partitions are dropped or archived cheaply."),
             (4, 3, "Queries without the key get slower."),
             (2, 5, "Retention and vacuum become small, routine jobs."),
             (3, 3, "Changing the partition key later is a big migration.")],
    pitfalls=[("Partitioning by a column you don't filter on", "Every query scans all 60 partitions.", "partition by the column in almost every WHERE."),
              ("Too many tiny partitions", "Daily partitions for 10 years: planning gets slow.", "aim for fewer, bigger partitions."),
              ("Forgetting to create next month", "Inserts fail at midnight on the 1st.", "automate with pg_partman; keep a DEFAULT partition and alert on it."),
              ("Expecting it to scale writes", "One server still takes all writes.", "for more write capacity, shard across servers (Vol. 1).")],
    use=["Time-series, events, logs, metrics, audit and history tables.",
         "Data with a retention policy (keep 13 months).",
         "Tables past ~100 GB where most queries hit a recent slice."],
    skip=["Tables that fit comfortably in memory.",
          "Queries that rarely filter on any one column.",
          "When you need more write throughput than one server (shard instead)."],
    related=["<b>Indexing</b>", "<b>History tables</b>", "<b>Sharding</b> (Vol. 1)", "<b>Star schema</b>"],
    quiz=[("What is partition pruning?", "The planner skipping partitions that can't contain rows matching the WHERE clause."),
          ("Why is dropping a partition better than DELETE for retention?", "It removes a whole table instantly, with no row-by-row delete, bloat or vacuum."),
          ("How is partitioning different from sharding?", "Partitioning splits a table within one database server; sharding spreads data across several servers."),
          ("Why must the primary key include the partition column (in PostgreSQL)?", "Uniqueness is enforced per partition, so the key must determine the partition to be globally unique.")],
    remember="One <span class=\"hl\">drawer</span> per month. Open only the one you need; <span class=\"hl\">bin</span> old drawers whole.",
    sources=["PostgreSQL docs, “Table Partitioning”.",
             "pg_partman documentation.",
             "Timescale docs, “Hypertables”.",
             "Markus Winand, “Partitioning” on use-the-index-luke.com."],
)

# ------------------------------------------------------------------ 13 Multitenancy
mt_problem = Doodle(760, 260, "Doodle of a SaaS app with three customer companies, Acme, Globex and Initech, in one table. A developer forgets the where tenant_id clause in one new report query, and Acme's admin suddenly sees Globex's invoices.",
                    "Many customers in one table, and one missing WHERE away from a data leak.")
mt_problem.table(20, 30, "invoices", ["acme · #1 · €900", "globex · #2 · €4,100", "initech · #3 · €75", "acme · #4 · €320"], w=260, hl=(1,))
mt_problem.note(460, 50, "new report:", "pen")
mt_problem.note(460, 76, "SELECT * FROM invoices", "pen")
mt_problem.note(460, 102, "-- forgot WHERE tenant_id", "red")
mt_problem.box(380, 160, 300, 60, "Acme sees Globex's data", "pink", stroke="red", size=18)

mt_analogy = Doodle(760, 260, "Doodle of an apartment building. Tenants share the foundation, the lift and the plumbing, but each flat has its own locked door. Some buildings put each tenant in a separate house instead: more private, more expensive.",
                    "An apartment block: shared building, separate locked flats.")
mt_analogy.box(40, 30, 280, 200, None, "paper", rx=2)
for r in range(2):
    for c in range(3):
        mt_analogy.box(56 + c * 88, 46 + r * 90, 76, 74, None, "y" if (r + c) % 2 else "green", rx=2)
        mt_analogy.icon("lock", 82 + c * 88, 74 + r * 90, 0.4)
mt_analogy.note(180, 252, "shared building, own locked door", "pen")
mt_analogy.icon("store", 470, 70, 1.3)
mt_analogy.icon("store", 600, 70, 1.3)
mt_analogy.note(580, 180, "or: a house each", "pen")
mt_analogy.note(580, 206, "(more private, more €)", "pen")

mt_how = Doodle(760, 300, "Three multitenancy models side by side. Shared tables with a tenant_id column and row-level security: cheapest, most tenants. Schema per tenant: one schema each in one database. Database per tenant: strongest isolation, highest cost. An arrow from left to right shows isolation and cost going up, tenant count going down.",
                "Three models: more isolation costs more. Most SaaS starts with shared tables + row-level security.")
models = [("shared tables", "tenant_id + RLS", "green"), ("schema each", "acme.*, globex.*", "y"), ("database each", "acme_db, globex_db", "blue")]
for i, (t, sub, f) in enumerate(models):
    x = 20 + i * 250
    mt_how.box(x, 40, 220, 90, t, f, sub=sub, size=19)
mt_how.arrow(40, 180, 700, 180, label="isolation ↑ · cost per tenant ↑", lx=370, ly=168)
mt_how.arrow(700, 230, 40, 230, label="tenants per server ↑ · ops effort ↓", lx=370, ly=262)

TENANT = dict(
    slug="multitenancy",
    kicker="a.k.a. “the apartment block”",
    tldr="Serve many customers (tenants) from one system while <b>keeping their data apart</b>. Choose a model: <b>shared tables with a <code>tenant_id</code></b> (cheapest, most common), <b>a schema per tenant</b>, or <b>a database per tenant</b> (strongest isolation). With shared tables, let the database enforce isolation with <b>row-level security</b>, so one forgotten WHERE can't leak data.",
    chips=[("Family", "SaaS data design"), ("Models", "shared · schema-per-tenant · database-per-tenant"), ("Guard", "row-level security (RLS)"), ("Pairs with", "partitioning, sharding, connection pooling")],
    problem="""  <p class="lead">A SaaS app holds data for hundreds of companies. Running a database for each is expensive; putting them all in one table is cheap but <span class="hl-pink">one missing filter away from a leak</span>. And one big customer can slow everyone down.</p>
  <ul>
    <li>A new query forgets <code>WHERE tenant_id = ?</code> and shows another company's data.</li>
    <li>One tenant's heavy export slows every other tenant (noisy neighbour).</li>
    <li>An enterprise customer asks for their data in their own region, or deleted on request.</li>
  </ul>""",
    problem_figs=[mt_problem],
    analogy_side="the apartment block",
    analogy="""  <p>An apartment block <b>shares the foundation, lift and plumbing</b>, which keeps rent low. But every flat has <b>its own locked door</b>. Someone who wants total privacy can rent a <b>house of their own</b>, at a much higher price.</p>
  <ul>
    <li>The building is your <b>shared database</b>; flats are <b>rows tagged with tenant_id</b>.</li>
    <li>The lock on each door is <b>row-level security</b>.</li>
    <li>A house each is <b>database per tenant</b>.</li>
  </ul>""",
    analogy_figs=[mt_analogy],
    map=[("The shared building", "One database and one set of tables"),
         ("The flat number", "<code>tenant_id</code> on every row"),
         ("A lock on each door", "Row-level security policies"),
         ("A house each", "Database (or schema) per tenant"),
         ("The noisy neighbour", "One tenant's load hurting others")],
    how_side="pick a model, then lock the doors",
    how="""  <p>Most SaaS products start with <b>shared tables</b> and add <b>row-level security</b>, then move their biggest or most demanding customers to dedicated databases later.</p>""",
    how_figs=[mt_how],
    steps=[("Choose the model", "Shared tables for many small tenants; schema or database per tenant for few, large or regulated ones. Hybrids are common."),
           ("Put tenant_id everywhere", "On every tenant-owned table, first in composite indexes and keys: <code>(tenant_id, id)</code>."),
           ("Enforce it in the database", "Enable row-level security with a policy that compares <code>tenant_id</code> to the session's <code>app.tenant_id</code> setting."),
           ("Set the tenant per request", "<code>SET LOCAL app.tenant_id = …</code> at the start of each transaction (pooler-safe)."),
           ("Plan for big tenants", "Per-tenant limits, partitioning or sharding by tenant_id, and a way to move a tenant to its own database.")],
    vocab=[("Tenant", "One customer organisation using the shared system."),
           ("Isolation", "Guarantee that tenants can't see or affect each other."),
           ("Row-level security", "Database rules that filter rows per session."),
           ("Noisy neighbour", "One tenant hogging shared resources."),
           ("Silo / pool / bridge", "Database-per-tenant / shared / mixed models."),
           ("Tenant-aware key", "Primary or index key starting with tenant_id.")],
    code=dict(file="tenancy.sql", note="PostgreSQL row-level security", src="""
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
ALTER TABLE invoices FORCE ROW LEVEL SECURITY;      -- applies to the table owner too

CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::bigint)
  WITH CHECK (tenant_id = current_setting('app.tenant_id')::bigint);

CREATE INDEX ON invoices (tenant_id, created_at DESC);

-- per request, inside the transaction (safe with transaction poolers)
BEGIN;
SET LOCAL app.tenant_id = '42';
SELECT * FROM invoices;            -- only tenant 42's rows, even without WHERE
COMMIT;
"""),
    tools="tools: PostgreSQL row-level security, Citus (shard by tenant_id), Supabase RLS, Rails <code>acts_as_tenant</code>, Django <code>django-tenants</code> (schema per tenant), AWS SaaS Factory guidance, Nile and Neon for database-per-tenant.",
    gains=["<b>Low cost per tenant</b> with shared tables.",
           "<b>One schema, one deploy</b> for everyone.",
           "<b>Isolation enforced by the database</b>, not just app code.",
           "<b>A path to dedicated databases</b> for big customers."],
    losses=["<b>Noisy neighbours</b> share resources.",
            "<b>tenant_id everywhere</b>: keys, indexes, joins.",
            "<b>Per-tenant restore</b> is harder in shared tables.",
            "<b>Mistakes are expensive</b> (a leak is a breach)."],
    baseline="Each line compares <b>shared tables with app-level WHERE filters only</b> to <b>shared tables with tenant-first keys and row-level security</b>.",
    ratings=[(4, 3, "Policies and session settings to understand."),
             (3, 4, "Tenant-first indexes keep each tenant's data together."),
             (3, 3, "RLS checks cost very little per row."),
             (2, 5, "A forgotten WHERE can no longer leak data."),
             (3, 4, "Ready to shard or move tenants by tenant_id."),
             (4, 4, "Still one shared database."),
             (4, 3, "Cross-tenant reports need a privileged role."),
             (3, 3, "Policies must be tested with every migration."),
             (3, 4, "Tenants can be moved to dedicated databases later.")],
    pitfalls=[("Isolation only in app code", "One new endpoint forgets the filter: breach.", "enforce with RLS; test that tenant A can't read tenant B."),
              ("Session settings with a pooler", "A <code>SET</code> leaks to the next request on the same connection.", "use <code>SET LOCAL</code> inside a transaction."),
              ("tenant_id not first in indexes", "Queries for one tenant scan everyone's rows.", "lead keys and indexes with tenant_id."),
              ("Schema per tenant at 10,000 tenants", "Migrations take hours and catalogs bloat.", "use shared tables for the long tail.")],
    use=["SaaS products serving many organisations.",
         "Tenants with similar schemas and features.",
         "You need cheap onboarding for many small customers."],
    skip=["A handful of huge, regulated customers (give each a database).",
          "Single-customer internal apps.",
          "Tenants needing very different schemas."],
    related=["<b>Table partitioning</b>", "<b>Connection pooling</b>", "<b>Surrogate keys</b>", "<b>Sharding</b> (Vol. 1)"],
    quiz=[("Name the three classic multitenancy models.", "Shared tables with a tenant_id, schema per tenant, and database per tenant."),
          ("What does row-level security add?", "The database filters rows by tenant automatically, so a query that forgets WHERE tenant_id can't see other tenants' data."),
          ("Why SET LOCAL rather than SET with a connection pooler?", "SET LOCAL lasts only for the transaction, so the setting can't leak to the next request that reuses the connection."),
          ("Why put tenant_id first in indexes?", "Queries always filter by tenant, so a tenant-first index jumps straight to that tenant's rows.")],
    remember="Share the <span class=\"hl\">building</span>, lock every <span class=\"hl\">door</span>, and let the <span class=\"hl\">database</span> hold the keys.",
    sources=["PostgreSQL docs, “Row Security Policies”.",
             "AWS whitepaper, “SaaS Tenant Isolation Strategies”.",
             "Microsoft Azure Architecture Center, “Multitenant SaaS database tenancy patterns”.",
             "Citus docs, “Multi-tenant Applications”."],
)

# ------------------------------------------------------------------ 14 Connection Pooling
cp_problem = Doodle(760, 260, "Doodle of 400 serverless functions each opening their own database connection. The database allows 100 connections, each one uses about ten megabytes of memory and a process. New requests fail with too many connections, and opening each connection costs extra milliseconds.",
                    "Every request opens its own connection: the database runs out long before the CPU does.")
for i in range(8):
    cp_problem.box(20 + (i % 2) * 70, 20 + (i // 2) * 52, 56, 40, "λ", "blue", size=18)
cp_problem.note(90, 240, "× 400 functions", "pen")
for i in range(6):
    cp_problem.arrow(170, 40 + i * 36, 450, 90 + i * 10, color="red")
cp_problem.db(540, 70, None, w=110, h=70)
cp_problem.note(595, 190, "max 100 connections", "red")
cp_problem.note(595, 216, "“too many clients already”", "red")

cp_analogy = Doodle(760, 250, "Doodle of a taxi rank. Instead of every traveller buying a car for one trip, a small fleet of taxis waits at the rank. Travellers take the next free taxi and return it for the next person.",
                    "A taxi rank: a few cars, shared by many travellers, one trip at a time.")
for i in range(3):
    cp_analogy.icon("truck", 300 + i * 100, 50, 1.2, fill="y")
cp_analogy.note(450, 150, "a few taxis at the rank", "green")
for i in range(5):
    cp_analogy.circle(40 + i * 46, 200, 14, "paper")
cp_analogy.note(130, 240, "many travellers, waiting briefly", "pen")
cp_analogy.arrow(250, 180, 320, 120)
cp_analogy.note(620, 220, "✗ buy a car per trip", "red")

cp_how = Doodle(760, 280, "Connection pooling. Four hundred app requests talk to a pooler such as PgBouncer. The pooler keeps twenty real connections open to the database and lends one to a request only for the length of a transaction, then returns it to the pool. Requests wait briefly in a queue when all twenty are busy.",
                "Many clients → a pooler → a few long-lived database connections, lent out per transaction.")
for i in range(6):
    cp_how.box(10, 20 + i * 40, 90, 30, "req", "blue", size=15)
    cp_how.arrow(106, 35 + i * 40, 240, 140)
cp_how.note(55, 270, "400 clients", "pen")
cp_how.box(246, 90, 200, 100, "pooler", "y", sub="lend per transaction")
cp_how.msgs(270, 200, 5, size=16)
cp_how.note(346, 250, "short queue when busy", "pen")
for i in range(4):
    cp_how.arrow(452, 110 + i * 22, 560, 110 + i * 22, color="green")
cp_how.db(640, 100, None, w=110, h=70)
cp_how.note(750, 220, "20 real connections", "green", anchor="end")

POOL = dict(
    slug="connection-pooling",
    kicker="a.k.a. “the taxi rank”",
    tldr="Opening a database connection is <b>slow and expensive</b> (a process, memory, a TLS handshake), and databases allow only a few hundred. Keep a <b>small pool of open connections</b> and <b>lend one per request or transaction</b>. Use the pool in your app, and an <b>external pooler</b> (PgBouncer, RDS Proxy) when many app instances or serverless functions share one database.",
    chips=[("Family", "scaling access"), ("In-app", "HikariCP, node-postgres Pool, SQLAlchemy pool"), ("External", "PgBouncer, pgcat, Supavisor, RDS Proxy"), ("Pairs with", "multitenancy, bulkhead (Vol. 1)")],
    problem="""  <p class="lead">Each PostgreSQL connection is a whole server process using megabytes of memory, and connecting takes a TCP + TLS + auth round trip. When every request or function <span class="hl-pink">opens its own</span>, the database runs out of connections long before it runs out of CPU.</p>
  <ul>
    <li>Autoscaling to 50 app pods × 20 connections = 1,000 connections: “too many clients”.</li>
    <li>Serverless functions open a fresh connection on every cold start.</li>
    <li>Thousands of mostly idle connections still cost memory and slow the database down.</li>
  </ul>""",
    problem_figs=[cp_problem],
    analogy_side="the taxi rank",
    analogy="""  <p>Nobody buys a car for a single trip across town. A <b>taxi rank</b> keeps a few cars ready; travellers take the <b>next free one</b> and it comes back for the next person. If all taxis are out, you <b>wait a moment</b> in the queue.</p>
  <ul>
    <li>Each taxi is an <b>open connection</b>.</li>
    <li>The rank is the <b>pool</b>; the dispatcher is the <b>pooler</b>.</li>
    <li>The queue is how a pool <b>protects the database</b> from overload.</li>
  </ul>""",
    analogy_figs=[cp_analogy],
    map=[("Buying a car per trip", "Opening a connection per request"),
         ("The taxis at the rank", "Open, reusable connections"),
         ("Taking the next free taxi", "Borrowing a connection from the pool"),
         ("Queueing when all are out", "Waiting for a free connection (with a timeout)"),
         ("The dispatcher", "PgBouncer / RDS Proxy in front of the database")],
    how_side="few connections, shared quickly",
    how="""  <p>Databases do best with <b>a small number of busy connections</b>, roughly a few per CPU core. A pool turns many short-lived clients into that shape.</p>""",
    how_figs=[cp_how],
    steps=[("Pool in the app", "Create one pool per process at start-up; never connect per request."),
           ("Size it small", "Start near <code>cores × 2</code> on the database side, then measure; bigger pools often make things slower."),
           ("Add an external pooler for many clients", "Many pods or serverless functions → PgBouncer/RDS Proxy in <b>transaction</b> mode."),
           ("Always return connections", "Use <code>try/finally</code> or the pool's helper; a leaked connection is gone for good."),
           ("Set timeouts", "Acquire timeout, statement timeout and idle-in-transaction timeout, so one stuck request can't hold a connection forever.")],
    vocab=[("Connection pool", "A set of open connections reused by many requests."),
           ("Pooler", "A proxy that pools connections for many clients."),
           ("Session pooling", "A client keeps one connection for its whole session."),
           ("Transaction pooling", "A connection is lent only for one transaction."),
           ("Connection leak", "Borrowing a connection and never returning it."),
           ("Acquire timeout", "How long to wait for a free connection.")],
    code=dict(file="db.ts", note="node-postgres", src="""
import { Pool } from "pg";

// one pool per process, created once
export const pool = new Pool({
  max: 10,                          // per app instance; total = instances × max
  idleTimeoutMillis: 30_000,
  connectionTimeoutMillis: 2_000,   // fail fast instead of hanging
  statement_timeout: 5_000,
});

export async function inTx<T>(fn: (c: PoolClient) => Promise<T>) {
  const c = await pool.connect();   // borrow
  try {
    await c.query("BEGIN");
    const out = await fn(c);
    await c.query("COMMIT");
    return out;
  } catch (e) { await c.query("ROLLBACK"); throw e; }
  finally { c.release(); }          // always give it back
}
"""),
    tools="tools: HikariCP (Java), node-postgres <code>Pool</code>, SQLAlchemy and Django <code>CONN_MAX_AGE</code>, Prisma Accelerate, PgBouncer, pgcat, Odyssey, Supavisor, Amazon RDS Proxy, ProxySQL (MySQL).",
    gains=["<b>No connection storms</b>: the database sees a steady, small number.",
           "<b>Lower latency</b>: no handshake per request.",
           "<b>Less database memory</b> spent on idle connections.",
           "<b>Back-pressure</b>: queueing protects the database under load."],
    losses=["<b>Pool sizing</b> needs measuring and tuning.",
            "<b>Transaction pooling breaks session features</b> (SET, advisory locks, some prepared statements).",
            "<b>Another hop and component</b> with an external pooler.",
            "<b>Leaks</b> quietly drain the pool."],
    baseline="Each line compares <b>a connection per request</b> to <b>an in-app pool plus an external pooler</b> in transaction mode.",
    ratings=[(4, 3, "Pool sizes and pooling modes to understand."),
             (3, 4, "No connect handshake on each request."),
             (3, 4, "Same, for writes."),
             (3, 3, "Neutral, if session state is handled with SET LOCAL."),
             (1, 5, "Thousands of clients share a few dozen connections."),
             (2, 4, "Far less memory spent on idle connection processes."),
             (3, 3, "Neutral."),
             (2, 4, "No “too many clients” outages during scale-ups."),
             (3, 3, "Neutral.")],
    pitfalls=[("Huge pools", "max = 200 per pod “to be safe”; the database thrashes.", "keep pools small and measure; more connections ≠ more speed."),
              ("Session state in transaction mode", "A <code>SET search_path</code> leaks to other clients or vanishes.", "use <code>SET LOCAL</code> inside transactions, or session mode."),
              ("Forgetting release()", "After an exception path the pool slowly empties and requests hang.", "always release in <code>finally</code>; enable leak detection."),
              ("Connect per serverless call", "Each cold start opens a new connection.", "put a pooler or data proxy between functions and the database.")],
    use=["Every app that talks to a relational database.",
         "Many app instances, autoscaling or serverless functions.",
         "Databases with expensive connections (PostgreSQL)."],
    skip=["Embedded databases like SQLite in a single process.",
          "HTTP-based database APIs that pool for you.",
          "A one-off script that runs a few queries."],
    related=["<b>Bulkhead</b> (Vol. 1)", "<b>Multitenancy</b>", "<b>Rate limiter</b> (Vol. 1)", "<b>Batch loading</b>"],
    quiz=[("Why are PostgreSQL connections expensive?", "Each is a separate backend process with its own memory, and creating one needs a TCP, TLS and authentication round trip."),
          ("Session vs transaction pooling?", "Session pooling ties a server connection to a client for its whole session; transaction pooling lends it only for one transaction, allowing far more clients."),
          ("Why can a bigger pool make things slower?", "Too many active connections compete for CPU, locks and memory, causing contention and context switching."),
          ("How do you avoid connection leaks?", "Always release connections in a finally block (or use the pool's helpers) and set acquire timeouts.")],
    remember="Don't buy a <span class=\"hl\">car</span> per trip. Keep a small <span class=\"hl\">taxi rank</span>, and always bring the taxi back.",
    sources=["PgBouncer documentation, “Features” and pooling modes.",
             "HikariCP wiki, “About Pool Sizing”.",
             "AWS docs, “Using Amazon RDS Proxy”.",
             "PostgreSQL wiki, “Number Of Database Connections”."],
)

# ------------------------------------------------------------------ 15 Star Schema
ss_problem = Doodle(760, 260, "Doodle of an analyst writing a report on the normalized app database: sales by product category by month by country needs a twelve-table join through orders, order items, products, categories, customers, addresses and countries. It runs for minutes and slows down checkout.",
                    "Analytics on the app's schema: a 12-table join for every question, fighting checkout for the same database.")
names = ["orders", "items", "products", "categories", "customers", "addresses", "countries", "promos"]
for i, n in enumerate(names):
    x, y = 20 + (i % 4) * 130, 30 + (i // 4) * 90
    ss_problem.box(x, y, 116, 44, n, "paper", size=15)
    if i % 4:
        ss_problem.line(f"M{x - 14} {y + 22} h14", color="red")
    if i >= 4:
        ss_problem.line(f"M{x + 58} {y - 46} v46", color="red")
ss_problem.note(640, 60, "12-table join", "red")
ss_problem.note(640, 90, "4 minutes", "red")
ss_problem.note(640, 120, "checkout slows", "red")
ss_problem.note(280, 240, "“sales by category, by month, by country?”", "pen")

ss_analogy = Doodle(760, 260, "Doodle of a till receipt. The receipt lines are the facts: what was bought, how many, for how much. Around it are labels you sort them by: the date, the shop, the product and the customer card. Any summary is just grouping receipt lines by labels.",
                    "Receipt lines are facts; date, shop, product and customer are the labels you group them by.")
ss_analogy.icon("receipt", 330, 70, 1.8, fill="y")
for (x, y, t) in [(160, 40, "date"), (600, 40, "shop"), (160, 220, "product"), (600, 220, "customer")]:
    ss_analogy.box(x - 70, y - 22, 140, 44, t, "green", size=17)
ss_analogy.arrow(320, 100, 236, 50)
ss_analogy.arrow(440, 100, 526, 50)
ss_analogy.arrow(320, 160, 236, 210)
ss_analogy.arrow(440, 160, 526, 210)
ss_analogy.note(385, 252, "sum lines, group by labels", "pen")

ss_how = Doodle(760, 300, "Star schema. A central fact table fact_sales holds one row per order line with foreign keys to dimensions and numeric measures: quantity and amount. Around it four dimension tables: dim_date, dim_product, dim_customer and dim_store, each with descriptive columns like month, category, country and region. Every report is one join from the fact to a few dimensions.",
                "One fact table of numbers in the middle, descriptive dimensions around it: every report is a one-hop join.")
ss_how.table(270, 80, "fact_sales", ["date_key · product_key", "customer_key · store_key", "qty · amount"], w=230, fill="y", hl=(2,))
dims = [(20, 10, "dim_date", ["day · month · year"]), (540, 10, "dim_product", ["name · category"]),
        (20, 200, "dim_customer", ["segment · country"]), (540, 200, "dim_store", ["city · region"])]
for (x, y, n, cols) in dims:
    ss_how.table(x, y, n, cols, w=200, fill="green")
ss_how.arrow(266, 110, 224, 60)
ss_how.arrow(504, 110, 536, 60)
ss_how.arrow(266, 170, 224, 210)
ss_how.arrow(504, 170, 536, 210)
ss_how.icon("star", 360, 220, 0.8, fill="y")

STAR = dict(
    slug="star-schema",
    kicker="a.k.a. “receipts and labels”",
    tldr="For analytics, shape data as a <b>fact table</b> of events with numbers (sales lines: quantity, amount) in the middle, surrounded by <b>dimension tables</b> that describe them (date, product, customer, store). Every report is <b>“sum the facts, group by dimension columns”</b>, a one-hop join that warehouses run very fast. Keep it in a <b>separate analytics database</b>, loaded from the app's data.",
    chips=[("Family", "analytics modelling"), ("Origin", "Ralph Kimball, dimensional modelling (1990s)"), ("Lives in", "Snowflake, BigQuery, Redshift, ClickHouse, DuckDB"), ("Pairs with", "change data capture, materialized views")],
    problem="""  <p class="lead">The app's normalized schema is great for <b>writing</b> orders, and painful for <b>asking questions</b>. “Sales by category, by month, by country” becomes a <span class="hl-pink">twelve-table join</span>, run on the same database that takes payments.</p>
  <ul>
    <li>Every analyst rebuilds the same joins, slightly differently, with different answers.</li>
    <li>Report queries scan huge tables and slow checkout down.</li>
    <li>History is lost: when a product changes category, last year's report changes too.</li>
  </ul>""",
    problem_figs=[ss_problem],
    analogy_side="receipts and labels",
    analogy="""  <p>Think of a shop's <b>till receipts</b>. Each line is a <b>fact</b>: this product, this many, this price. Around them are <b>labels</b>: the date, the shop, the product's category, the customer's loyalty card. Any summary you can imagine is just “add up receipt lines, grouped by labels”.</p>
  <ul>
    <li>Receipt lines are the <b>fact table</b>; labels are <b>dimensions</b>.</li>
    <li>Drawn on paper, the fact sits in the middle with dimensions around it: a <b>star</b>.</li>
  </ul>""",
    analogy_figs=[ss_analogy],
    map=[("A receipt line", "A row in <code>fact_sales</code> (one order line)"),
         ("Quantity and price", "Measures: <code>qty</code>, <code>amount</code>"),
         ("Date, shop, product, customer", "Dimension tables"),
         ("“Group by category and month”", "<code>GROUP BY p.category, d.month</code>"),
         ("Last year's labels kept", "Slowly changing dimensions (type 2)")],
    how_side="facts in the middle, dimensions around",
    how="""  <p>Dimensions are deliberately <b>denormalized</b> (category sits right on the product row), so every question is one join away from the fact table, and columnar warehouses scan just the columns they need.</p>""",
    how_figs=[ss_how],
    steps=[("Pick the grain", "One fact row = one what? “One order line” is the usual answer; state it explicitly."),
           ("List the measures", "The numbers you add up: quantity, amount, discount, cost."),
           ("Build dimensions", "Flat, descriptive tables with a surrogate key: date (with month, quarter, holiday), product (with category), customer, store."),
           ("Keep history in dimensions", "Type 2: when a product changes category, add a new dimension row with valid dates, so old facts keep the old label."),
           ("Load it separately", "ETL/ELT (often with dbt) from the app database or a CDC stream into a warehouse, on a schedule.")],
    vocab=[("Fact table", "Events with numeric measures, at a fixed grain."),
           ("Dimension", "Descriptive context you filter and group by."),
           ("Grain", "What exactly one fact row represents."),
           ("Measure", "A number you aggregate (sum, count, avg)."),
           ("Slowly changing dimension", "Rules for keeping dimension history (type 1, 2…)."),
           ("OLAP vs OLTP", "Analytics workloads vs transactional workloads.")],
    code=dict(file="reports.sql", note="any warehouse", src="""
CREATE TABLE fact_sales (
  date_key     int    NOT NULL REFERENCES dim_date,
  product_key  int    NOT NULL REFERENCES dim_product,
  customer_key int    NOT NULL REFERENCES dim_customer,
  store_key    int    NOT NULL REFERENCES dim_store,
  qty          int    NOT NULL,
  amount       numeric(12, 2) NOT NULL       -- grain: one order line
);

-- sales by category, month and country: one hop to each dimension
SELECT p.category, d.month, c.country, sum(f.amount) AS revenue
FROM fact_sales f
JOIN dim_product  p ON p.product_key  = f.product_key
JOIN dim_date     d ON d.date_key     = f.date_key
JOIN dim_customer c ON c.customer_key = f.customer_key
WHERE d.year = 2026
GROUP BY p.category, d.month, c.country
ORDER BY revenue DESC;
"""),
    tools="tools: Snowflake, BigQuery, Redshift, ClickHouse, DuckDB, dbt for building facts and dimensions, Fivetran/Airbyte/Debezium for loading, BI tools like Metabase, Looker and Power BI that expect star schemas.",
    gains=["<b>Fast, simple reports</b>: sum facts, group by dimensions.",
           "<b>One shared definition</b> of revenue, customers and products.",
           "<b>History kept</b> with slowly changing dimensions.",
           "<b>Analytics off the app database</b>: checkout stays fast.",
           "<b>BI tools understand it</b> out of the box."],
    losses=["<b>A pipeline to build and run</b> (ETL/ELT, scheduling).",
            "<b>Data is a little behind</b> the app.",
            "<b>Duplicated, denormalized data</b> in dimensions.",
            "<b>Bad for transactional writes</b>: it's for reading."],
    baseline="Each line compares <b>running analytics on the normalized app database</b> to <b>a star schema in a separate warehouse</b>.",
    ratings=[(2, 4, "Reports read like the question; the pipeline is extra."),
             (1, 5, "One-hop joins over columnar storage."),
             (3, 3, "App writes are untouched; loads are batch."),
             (3, 4, "One agreed definition of each metric, with history."),
             (2, 5, "Warehouses scale to billions of fact rows."),
             (3, 2, "A second copy of the data, denormalized."),
             (2, 5, "Any slice by any dimension is easy."),
             (3, 3, "One more pipeline to monitor."),
             (3, 4, "New dimensions and measures plug in.")],
    pitfalls=[("Fuzzy grain", "Some fact rows are orders, some are order lines; totals double.", "write down the grain; one fact table per grain."),
              ("Overwriting dimensions", "A product moves category and last year's report changes.", "use type 2 slowly changing dimensions where history matters."),
              ("Snowflaking everything", "Dimensions normalized into sub-tables; joins are back.", "keep dimensions flat unless they're huge."),
              ("Querying the app database directly", "Analysts run heavy reports on production.", "load into a warehouse (or at least a read replica).")],
    use=["Dashboards, BI and business reporting.",
         "Questions that slice numbers by many attributes.",
         "Teams that need one shared definition of key metrics."],
    skip=["Transactional app tables (keep those normalized).",
          "Tiny datasets where a few SQL queries are enough.",
          "Real-time operational views that must be exact right now."],
    related=["<b>Normalization</b>", "<b>Materialized views</b>", "<b>Change data capture</b>", "<b>CQRS</b> (Vol. 1)"],
    quiz=[("What goes in a fact table, and what in a dimension?", "Facts hold events with numeric measures at a fixed grain; dimensions hold descriptive attributes to filter and group by."),
          ("What is the grain?", "The precise meaning of one fact row, for example one order line."),
          ("Why denormalize dimensions?", "So every question is one join from the fact table, which is simpler and faster for analytics."),
          ("What does a type 2 slowly changing dimension do?", "Adds a new dimension row (with validity dates) when an attribute changes, so old facts keep their old labels.")],
    remember="Receipts in the <span class=\"hl\">middle</span>, labels <span class=\"hl\">around</span>. Every report is “add up, group by”.",
    sources=["Ralph Kimball &amp; Margy Ross, <i>The Data Warehouse Toolkit</i> (3rd ed.).",
             "Kimball Group, “Dimensional Modeling Techniques”.",
             "dbt Labs, “Building a Kimball dimensional model with dbt”.",
             "Microsoft Power BI docs, “Understand star schema and the importance for Power BI”."],
)

NOTES = [PARTITION, TENANT, POOL, STAR]
