# Vol. 3 · Changing safely: Optimistic Locking, Expand & Contract Migrations, Change Data Capture.

# ------------------------------------------------------------------ 09 Optimistic Locking
ol_problem = Doodle(760, 260, "Doodle of a lost update. Ana and Ben open the same wiki page, version 3. Ana saves a fix to the intro. A minute later Ben saves his edit to the ending, based on the old version, and silently overwrites Ana's fix.",
                    "Two people edit the same row; the last save silently wipes out the first.")
ol_problem.box(20, 30, 140, 50, "Ana", "green", size=18)
ol_problem.box(20, 170, 140, 50, "Ben", "blue", size=18)
ol_problem.table(300, 80, "page #7", ["v3 · “Hello wrold…”"], w=220, fill="y")
ol_problem.arrow(166, 50, 296, 100, label="① read v3, fix intro, save", lx=300, ly=40)
ol_problem.arrow(166, 196, 296, 130, color="red", label="② save old copy + new ending", lx=300, ly=210)
ol_problem.note(640, 120, "Ana's fix:", "red")
ol_problem.note(640, 146, "gone, silently", "red")

ol_analogy = Doodle(760, 250, "Doodle of a shared document with a version stamp. Before you hand back your copy, the librarian checks that the stamp on your copy still matches the master. If someone else handed theirs back first, the stamp has changed, and you're told to merge first.",
                    "The librarian checks your copy's version stamp before accepting it.")
ol_analogy.icon("recipe", 40, 40, 1.8, fill="y")
ol_analogy.icon("stamp", 120, 120, 1.0)
ol_analogy.note(90, 220, "your copy · stamped v3")
ol_analogy.arrow(220, 100, 400, 100, label="hand it back", lx=310, ly=86)
ol_analogy.box(410, 60, 300, 80, "master is now v4?", "pink", stroke="red", size=19)
ol_analogy.note(560, 175, "“someone got there first,", "red")
ol_analogy.note(560, 200, "merge and try again”", "red")

ol_how = Doodle(760, 280, "Optimistic locking with a version column. Ana and Ben both read version 3. Ana's update says where version equals 3, succeeds, and bumps it to 4. Ben's update also says where version equals 3, matches zero rows, and the app tells Ben the page changed and shows him the new version to merge.",
                "UPDATE … WHERE version = 3. The first save wins; the second matches 0 rows and must retry.")
ol_how.box(20, 30, 140, 50, "Ana", "green", size=18)
ol_how.box(20, 180, 140, 50, "Ben", "blue", size=18)
ol_how.table(330, 90, "page #7", ["version = 3 → 4"], w=220, fill="y")
ol_how.arrow(166, 54, 326, 110, color="green", label="WHERE version = 3 → 1 row ✓", lx=180, ly=26, anchor="start")
ol_how.arrow(166, 204, 326, 140, color="red", label="WHERE version = 3 → 0 rows", lx=180, ly=254, anchor="start")
ol_how.box(560, 170, 190, 70, "changed! merge?", "pink", stroke="red", size=16)
ol_how.arrow(400, 160, 554, 200, dash=True, color="red")

OPTLOCK = dict(
    slug="optimistic-locking",
    kicker="a.k.a. “check the version stamp”",
    tldr="Give each row a <b><code>version</code></b> number. When you save, say <b><code>UPDATE … SET version = version + 1 WHERE id = ? AND version = ?</code></b> with the version you read. If <b>0 rows</b> match, someone else changed it first: <b>reload, merge or retry</b> instead of silently overwriting. No locks are held while the user thinks.",
    chips=[("Family", "concurrency control"), ("Opposite", "pessimistic locking (SELECT … FOR UPDATE)"), ("HTTP cousin", "ETag + If-Match"), ("Pairs with", "idempotent consumer, history tables")],
    problem="""  <p class="lead">Read, edit, save. When two people (or two requests) do it on the same row at once, the second save <span class="hl-pink">silently wipes out</span> the first. This is the <b>lost update</b>, and nothing errors.</p>
  <ul>
    <li>Two admins edit a product; one price change disappears.</li>
    <li>Two requests add to a counter; one increment vanishes.</li>
    <li>Locking the row while the user edits for ten minutes blocks everyone else.</li>
  </ul>""",
    problem_figs=[ol_problem],
    analogy_side="the version stamp",
    analogy="""  <p>Imagine checking out a copy of a shared document stamped <b>v3</b>. When you hand it back, the librarian looks at the master. Still v3? Your changes go in, and the master becomes <b>v4</b>. Already v4? Someone got there first, so you're asked to <b>merge</b> before trying again.</p>
  <ul>
    <li>Nobody is blocked while you work: it's <b>optimistic</b> that conflicts are rare.</li>
    <li>The stamp check happens in <b>one step</b> at hand-in: a conditional UPDATE.</li>
  </ul>""",
    analogy_figs=[ol_analogy],
    map=[("The stamp on your copy", "The <code>version</code> you read"),
         ("Checking the master's stamp", "<code>WHERE version = :read_version</code>"),
         ("Master becomes v4", "<code>SET version = version + 1</code>"),
         ("“Someone got there first”", "0 rows updated → conflict"),
         ("Merge and hand in again", "Reload, merge or retry")],
    how_side="a conditional update",
    how="""  <p>The check and the write are <b>one atomic statement</b>, so there's no gap for another writer to sneak in. The database does the hard part.</p>""",
    how_figs=[ol_how],
    steps=[("Add a version column", "<code>version int NOT NULL DEFAULT 0</code> (or use <code>updated_at</code>, or PostgreSQL's <code>xmin</code>)."),
           ("Send it to the client", "Include it in the form or as an HTTP <code>ETag</code>."),
           ("Update conditionally", "<code>… WHERE id = $1 AND version = $2</code>, bumping the version."),
           ("Check the row count", "1 = saved. 0 = conflict: return HTTP 409 / 412 with the latest data."),
           ("Decide the conflict policy", "Show a merge screen, retry automatically (for counters), or let the user choose.")],
    vocab=[("Lost update", "A write that overwrites another without noticing."),
           ("Optimistic locking", "Detect conflicts at write time; no locks held."),
           ("Pessimistic locking", "Lock the row first (SELECT … FOR UPDATE)."),
           ("Version column", "A counter bumped on every write."),
           ("Compare-and-set", "Write only if the value is still what you saw."),
           ("ETag / If-Match", "HTTP headers for the same idea.")],
    code=dict(file="save_page.ts", note="node-postgres", src="""
// the client sends back the version it loaded
async function savePage(id: number, body: string, version: number) {
  const r = await db.query(
    `UPDATE pages SET body = $1, version = version + 1, updated_at = now()
     WHERE id = $2 AND version = $3
     RETURNING version`,
    [body, id, version],
  );
  if (r.rowCount === 0) {
    const latest = await db.query("SELECT * FROM pages WHERE id = $1", [id]);
    throw new Conflict(409, latest.rows[0]);   // UI shows a merge screen
  }
  return r.rows[0].version;                    // the new version for next time
}

// simple counters don't need versions: let the database do the maths
// UPDATE stock SET qty = qty - 1 WHERE sku = $1 AND qty > 0
"""),
    tools="tools: JPA/Hibernate <code>@Version</code>, Rails <code>lock_version</code>, Entity Framework <code>[ConcurrencyCheck]</code> / rowversion, Django <code>django-concurrency</code>, HTTP ETag + If-Match, DynamoDB condition expressions.",
    gains=["<b>No lost updates</b>: conflicts are detected, not hidden.",
           "<b>No locks held</b> while users think.",
           "<b>Scales well</b> when conflicts are rare.",
           "<b>Works across HTTP</b> with ETags."],
    losses=["<b>Conflicts must be handled</b> in the UI or with retries.",
            "<b>Wasted work</b> when conflicts are frequent.",
            "<b>Every write path</b> must check the version.",
            "<b>One more column</b> on each table."],
    baseline="Each line compares <b>plain read-modify-write</b> to the same updates with a <b>version check</b>.",
    ratings=[(4, 3, "A version column and a conflict path."),
             (3, 3, "Neutral."),
             (4, 4, "One conditional UPDATE, no lock waits."),
             (2, 5, "Lost updates become visible conflicts."),
             (3, 4, "No long-held locks, so more concurrency."),
             (3, 3, "One small column."),
             (3, 3, "Neutral."),
             (3, 4, "No mystery “my change disappeared” tickets."),
             (3, 3, "New write paths must remember the check.")],
    pitfalls=[("Checking, then writing", "SELECT the version, compare in code, then UPDATE: another write sneaks in between.", "put the check in the UPDATE's WHERE clause."),
              ("Ignoring the row count", "The UPDATE matched 0 rows and the app said “Saved!”.", "treat 0 rows as a conflict, every time."),
              ("Optimistic under heavy contention", "A hot counter retries forever.", "use atomic SQL (<code>qty = qty - 1</code>) or a pessimistic lock."),
              ("Bypass paths", "Admin scripts update rows without bumping the version.", "bump it in a trigger, or in every write path.")],
    use=["Forms and editors where people edit the same records.",
         "APIs where clients read, change and write back.",
         "Low-to-medium contention on any given row."],
    skip=["Hot rows updated many times per second (use atomic SQL or a queue).",
          "Insert-only data that's never updated.",
          "Short transactions where SELECT … FOR UPDATE is simpler."],
    related=["<b>History tables</b>", "<b>Expand &amp; contract</b>", "<b>Idempotent consumer</b> (Vol. 1)", "<b>Optimistic UI</b> (Vol. 2)"],
    quiz=[("What is a lost update?", "Two read-modify-write cycles overlap and the second save overwrites the first without any error."),
          ("Why put the version check in the WHERE clause?", "Check and write happen atomically; there's no gap where another writer can change the row."),
          ("What should the API return on a conflict?", "An error like HTTP 409 or 412 with the latest data so the client can merge or retry."),
          ("When is pessimistic locking better?", "When contention is high and retries would waste lots of work, for short transactions.")],
    remember="Hand it back only if the <span class=\"hl\">stamp</span> still matches. 0 rows means <span class=\"hl\">someone got there first</span>.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i>, “Optimistic Offline Lock”.",
             "Kung &amp; Robinson, “On Optimistic Methods for Concurrency Control” (1981).",
             "RFC 9110, HTTP “If-Match” and “ETag”.",
             "Vlad Mihalcea, “Optimistic vs. Pessimistic Locking”."],
)

# ------------------------------------------------------------------ 10 Expand & Contract Migrations
ec_problem = Doodle(760, 260, "Doodle of a risky migration. A deploy renames the column name to full_name and ships new code at the same time. For several minutes old app servers still query name and crash, the table is locked during the change, and rolling back the code no longer works.",
                    "Rename + deploy in one go: old servers break, the table locks, rollback is impossible.")
ec_problem.box(20, 40, 180, 60, "old app v1", "blue", sub="SELECT name")
ec_problem.box(20, 150, 180, 60, "new app v2", "green", sub="SELECT full_name")
ec_problem.table(330, 70, "users", ["name → full_name"], w=230, fill="pink", stroke="red")
ec_problem.arrow(206, 70, 326, 100, color="red", label="column gone!", lx=250, ly=50)
ec_problem.arrow(206, 180, 326, 120)
ec_problem.icon("lock", 600, 60, 1.0, color="red")
ec_problem.note(640, 150, "table locked", "red")
ec_problem.note(640, 176, "rollback broken", "red")

ec_analogy = Doodle(760, 260, "Doodle of a road being moved. Engineers build the new road first while traffic uses the old one, then open both, then move the signs, and only when no cars use the old road do they dig it up.",
                    "Build the new road, open both, move the traffic, then remove the old road.")
ec_analogy.line("M20 80 h300", dash=True)
ec_analogy.note(170, 66, "old road")
ec_analogy.line("M20 160 h300", color="green")
ec_analogy.note(170, 190, "new road", "green")
for i, t in enumerate(["① build new", "② open both", "③ move traffic", "④ remove old"]):
    ec_analogy.box(380, 20 + i * 56, 200, 44, t, "y" if i < 3 else "pink", size=17)
ec_analogy.note(670, 120, "traffic never", "pen")
ec_analogy.note(670, 146, "stops", "pen")

ec_how = Doodle(760, 300, "Expand and contract timeline. Step one, expand: add a nullable full_name column. Step two: deploy code that writes both columns. Step three: backfill old rows in small batches. Step four: deploy code that reads full_name. Step five, contract: stop writing name, then drop it. Each step is backward compatible and can be rolled back.",
                "Five small deploys. At every step, the old code and the new code both work.")
steps_ec = [("1 · expand", "ADD full_name", "green"), ("2 · dual-write", "write both", "y"), ("3 · backfill", "in batches", "y"), ("4 · read new", "read full_name", "y"), ("5 · contract", "DROP name", "pink")]
for i, (t, sub, f) in enumerate(steps_ec):
    x = 10 + i * 150
    ec_how.box(x, 60, 138, 80, t, f, sub=sub, size=16, subsize=15)
    if i:
        ec_how.arrow(x - 10, 100, x - 2, 100)
ec_how.line("M20 190 h720", color="green")
ec_how.note(380, 220, "old + new code both work at every step → each deploy can roll back", "green")
ec_how.note(380, 260, "days or weeks apart is fine", "pen")

EXPAND = dict(
    slug="expand-contract",
    kicker="a.k.a. “parallel change”",
    tldr="Never change the schema and the code in one risky step. <b>Expand</b> first (add the new column or table alongside the old one), <b>migrate</b> code and data in small, <b>backward-compatible</b> deploys (dual-write, backfill, switch reads), and only <b>contract</b> (drop the old thing) once nothing uses it. Every step can be <b>rolled back</b>, and there's <b>no downtime</b>.",
    chips=[("Family", "schema evolution"), ("a.k.a.", "parallel change, zero-downtime migration"), ("Tools", "Flyway, Liquibase, gh-ost, pgroll"), ("Pairs with", "feature flags, blue–green deploys")],
    problem="""  <p class="lead">During a deploy, <span class="hl-pink">old and new code run at the same time</span>. A migration that renames or drops a column breaks whichever version doesn't expect it, and big ALTERs can <span class="hl-pink">lock a busy table</span>.</p>
  <ul>
    <li>Old servers crash with “column name does not exist”.</li>
    <li>An ALTER on a 200M-row table holds a lock and the site stalls.</li>
    <li>The code rollback fails because the schema already moved on.</li>
  </ul>""",
    problem_figs=[ec_problem],
    analogy_side="moving a road without closing it",
    analogy="""  <p>To move a road, engineers don't close the old one and start digging. They <b>build the new road</b> beside it, <b>open both</b>, <b>move the signs</b> so traffic shifts over, and only when the old road is empty do they <b>dig it up</b>. Traffic never stops.</p>
  <ul>
    <li>Building the new road is the <b>expand</b> migration.</li>
    <li>Both roads open is <b>dual-writing</b>.</li>
    <li>Digging up the old road is the <b>contract</b> migration.</li>
  </ul>""",
    analogy_figs=[ec_analogy],
    map=[("Build the new road", "<code>ADD COLUMN full_name</code> (nullable)"),
         ("Both roads open", "Code writes both columns"),
         ("Repaint old cars' plates", "Backfill old rows in batches"),
         ("Move the signs", "Code reads the new column"),
         ("Dig up the old road", "Stop writing it, then <code>DROP COLUMN name</code>")],
    how_side="small steps, each backward compatible",
    how="""  <p>The rule: <b>every migration must work with the code that's currently running and the code about to run</b>. Splitting a change into expand → migrate → contract makes that true.</p>""",
    how_figs=[ec_how],
    steps=[("Expand", "Add the new column/table as nullable or with a default; no locks, no breakage."),
           ("Dual-write", "Deploy code that writes old and new (or a trigger that syncs them)."),
           ("Backfill", "Copy existing data in small batches (say 1,000 rows at a time) to avoid long locks and replication lag."),
           ("Switch reads", "Deploy code that reads the new column; keep writing both so rollback works."),
           ("Contract", "Stop writing the old column, wait a release, then drop it. Add NOT NULL with a validated CHECK first, not in one lock-heavy step.")],
    vocab=[("Backward compatible", "The old code still works with the new schema."),
           ("Expand", "Add new structures without removing old ones."),
           ("Contract", "Remove what nothing uses any more."),
           ("Dual-write", "Writing to the old and new places at once."),
           ("Backfill", "Filling the new structure from existing data."),
           ("Online schema change", "Altering a table without blocking traffic.")],
    code=dict(file="migrations/", note="one file per deploy", src="""
-- 0042_expand.sql            (deploy 1)
ALTER TABLE users ADD COLUMN full_name text;   -- nullable: instant

-- app v2 writes both name and full_name     (deploy 2)

-- 0043_backfill.sql          (run in batches until 0 rows)
UPDATE users SET full_name = name
WHERE id IN (SELECT id FROM users WHERE full_name IS NULL LIMIT 1000);

-- app v3 reads full_name, still writes both  (deploy 3)

-- 0044_not_null.sql          (cheap validation, no long lock)
ALTER TABLE users ADD CONSTRAINT full_name_nn CHECK (full_name IS NOT NULL) NOT VALID;
ALTER TABLE users VALIDATE CONSTRAINT full_name_nn;

-- app v4 stops writing name                  (deploy 4)
-- 0045_contract.sql          (deploy 5, a release later)
ALTER TABLE users DROP COLUMN name;
"""),
    tools="tools: Flyway, Liquibase, Rails/Django migrations, Strong Migrations (Rails) and django-pg-zero-downtime-migrations linters, gh-ost and pt-online-schema-change (MySQL), pgroll and Reshape (PostgreSQL), feature flags for switching reads.",
    gains=["<b>Zero downtime</b> schema changes.",
           "<b>Every step can roll back</b>.",
           "<b>Small, boring deploys</b> instead of a big-bang night.",
           "<b>Works with rolling deploys</b> and many app versions."],
    losses=["<b>More deploys</b> and more calendar time.",
            "<b>Temporary duplication</b> (two columns, dual writes).",
            "<b>Easy to forget the contract</b> step.",
            "<b>Backfills</b> need care on huge tables."],
    baseline="Each line compares a <b>one-shot migration deployed with the code</b> to the same change done as <b>expand → migrate → contract</b>.",
    ratings=[(4, 3, "Five small steps instead of one big one."),
             (3, 3, "Neutral."),
             (3, 3, "Dual writes cost a little, temporarily."),
             (3, 4, "Batched backfills and validated constraints, no half-states."),
             (3, 4, "Works on huge tables without long locks."),
             (3, 3, "Briefly stores data twice."),
             (3, 3, "Neutral."),
             (1, 5, "No maintenance windows, every step reversible."),
             (2, 5, "Schema changes become routine and safe.")],
    pitfalls=[("Never contracting", "Three years later the table has <code>name</code>, <code>full_name</code> and <code>display_name</code>.", "ticket the contract step when you start; track it."),
              ("One huge backfill UPDATE", "A single statement rewrites 200M rows, bloats the table and lags replicas.", "batch it, pause between batches, watch lag."),
              ("Locking ALTERs", "Adding NOT NULL or a default on old databases rewrites the table under a lock.", "use NOT VALID + VALIDATE, and set a short <code>lock_timeout</code>."),
              ("Renaming in place", "<code>RENAME COLUMN</code> breaks the running code instantly.", "add new, migrate, drop old, or use a view as an alias.")],
    use=["Any production database with traffic during deploys.",
         "Rolling or blue–green deployments with several app versions live.",
         "Large tables where locks would hurt."],
    skip=["Brand-new tables nobody uses yet.",
          "Apps where a short maintenance window is genuinely fine.",
          "Prototypes and local databases."],
    related=["<b>Optimistic locking</b>", "<b>Change data capture</b>", "<b>History tables</b>", "<b>Strangler fig</b> (planned, Vol. 1)"],
    quiz=[("Why is renaming a column in one step dangerous?", "During the deploy old code still uses the old name and crashes, and rolling back the code no longer matches the schema."),
          ("What are the three phases?", "Expand (add new), migrate (dual-write, backfill, switch reads), contract (remove old)."),
          ("Why backfill in batches?", "To avoid long locks, table bloat and replication lag from one giant UPDATE."),
          ("How do you add NOT NULL safely to a big PostgreSQL table?", "Add a CHECK … IS NOT NULL constraint as NOT VALID, then VALIDATE it separately.")],
    remember="Build the <span class=\"hl\">new road</span> first. Dig up the <span class=\"hl\">old one</span> last, when it's empty.",
    sources=["Danilo Sato, “ParallelChange” (martinfowler.com).",
             "Pramod Sadalage &amp; Scott Ambler, <i>Refactoring Databases</i>.",
             "GitLab docs, “Avoiding downtime in migrations”.",
             "PostgreSQL docs, “ALTER TABLE” (NOT VALID, VALIDATE CONSTRAINT)."],
)

# ------------------------------------------------------------------ 11 Change Data Capture
cdc_problem = Doodle(760, 260, "Doodle of dual writes. The app saves an order to the database and then also sends it to the search index, the cache and the warehouse. When the search call times out after the database commit, search is now missing the order, and nobody notices for days.",
                    "The app writes to four places itself. One call fails, and the copies drift apart.")
cdc_problem.box(20, 100, 140, 60, "app", "blue")
for i, (t, ok) in enumerate([("database", True), ("search", False), ("cache", True), ("warehouse", True)]):
    y = 10 + i * 62
    cdc_problem.box(420, y, 180, 48, t, "green" if ok else "pink", stroke="" if ok else "red", size=17)
    cdc_problem.arrow(166, 130, 414, y + 24, color="" if ok else "red")
cdc_problem.note(680, 100, "timeout!", "red")
cdc_problem.note(680, 126, "order missing", "red")
cdc_problem.note(680, 152, "from search", "red")

cdc_analogy = Doodle(760, 250, "Doodle of a court stenographer typing every word said in the courtroom. Reporters don't interrupt the judge to ask what happened; they read the stenographer's transcript, in order, as it's typed.",
                    "The court stenographer: every word goes into the transcript, and everyone else reads that.")
cdc_analogy.icon("board", 40, 60, 1.3)
cdc_analogy.note(85, 160, "the courtroom", "pen")
cdc_analogy.arrow(150, 90, 280, 90)
cdc_analogy.icon("receipt", 290, 40, 1.6, fill="y")
cdc_analogy.note(340, 170, "the transcript")
for i, t in enumerate(["newspaper", "lawyers", "archive"]):
    cdc_analogy.arrow(400, 90, 540, 50 + i * 50)
    cdc_analogy.note(560, 56 + i * 50, t, "green", anchor="start")
cdc_analogy.note(380, 228, "nobody interrupts the judge", "pen")

cdc_how = Doodle(760, 290, "Change data capture pipeline. The app writes only to the database. Every commit lands in the write-ahead log. A connector such as Debezium reads the log and publishes change events, insert, update and delete with before and after values, to a Kafka topic. Search, cache and warehouse consumers each read the stream at their own pace.",
                "The app writes once. A connector tails the database log and streams every committed change.")
cdc_how.box(10, 110, 96, 60, "app", "blue")
cdc_how.arrow(112, 140, 138, 140)
cdc_how.db(185, 110, "database", w=80)
cdc_how.icon("receipt", 238, 100, 0.9, fill="y")
cdc_how.note(266, 190, "WAL / binlog", "pen")
cdc_how.arrow(298, 140, 334, 140)
cdc_how.box(340, 110, 124, 60, "connector", "y", size=17)
cdc_how.arrow(470, 140, 498, 140)
cdc_how.msgs(504, 130, 3, size=16)
for i, t in enumerate(["search", "cache", "warehouse"]):
    cdc_how.arrow(580, 140, 606, 60 + i * 80, color="green")
    cdc_how.box(612, 40 + i * 80, 140, 44, t, "green", size=16)
cdc_how.note(260, 260, "{ op: 'u', before: {…}, after: {…}, lsn }", "pen")

CDC = dict(
    slug="change-data-capture",
    kicker="a.k.a. “the court stenographer”",
    tldr="Don't make the app write the same change to the database <i>and</i> the search index <i>and</i> the cache. Write <b>only to the database</b>, and let a connector <b>read the database's own log</b> (the WAL or binlog) and publish <b>every committed insert, update and delete</b> as an event. Other systems <b>follow the stream</b>, in order, and catch up after outages.",
    chips=[("Family", "data integration"), ("Reads", "PostgreSQL WAL, MySQL binlog, SQL Server CDC, Mongo change streams"), ("Tools", "Debezium, Kafka Connect, AWS DMS, Fivetran"), ("Pairs with", "transactional outbox, materialized views")],
    problem="""  <p class="lead">Data rarely stays in one place: search, caches, analytics and other services all want a copy. Making the app <span class="hl-pink">write to every one of them</span> (dual writes) means any failure leaves the copies <span class="hl-pink">out of sync</span>.</p>
  <ul>
    <li>The database commits, the search call times out: search is missing the order forever.</li>
    <li>Nightly batch exports are hours stale and hammer the database.</li>
    <li>Changes made by scripts or admin SQL never reach the other systems.</li>
  </ul>""",
    problem_figs=[cdc_problem],
    analogy_side="the court stenographer",
    analogy="""  <p>In court, nobody stops the judge to ask what was just said. A <b>stenographer types every word</b> into a transcript, in order. Newspapers, lawyers and the archive all read the <b>transcript</b>, each at their own pace.</p>
  <ul>
    <li>The database already keeps that transcript for crash recovery: the <b>write-ahead log</b>.</li>
    <li>CDC just lets other systems <b>read it</b>.</li>
  </ul>""",
    analogy_figs=[cdc_analogy],
    map=[("The courtroom", "The database where the app writes"),
         ("The stenographer's transcript", "The WAL / binlog: every committed change, in order"),
         ("Reading the transcript", "A CDC connector (Debezium) tailing the log"),
         ("Newspapers, lawyers, archive", "Search, cache, warehouse, other services"),
         ("“Where did I stop reading?”", "The stored log position (offset / LSN)")],
    how_side="tail the log, publish the changes",
    how="""  <p>Because CDC reads <b>committed</b> changes from the log, it catches every write path (app, scripts, admin SQL), keeps their <b>order</b>, and never sees a transaction that rolled back.</p>""",
    how_figs=[cdc_how],
    steps=[("Enable logical decoding", "PostgreSQL: <code>wal_level = logical</code> plus a publication; MySQL: row-based binlog."),
           ("Run a connector", "Debezium (on Kafka Connect or Debezium Server) takes a snapshot, then streams changes."),
           ("Publish events", "One topic per table: <code>{op, before, after, source.lsn}</code>, keyed by primary key so a row's changes stay in order."),
           ("Consume idempotently", "Consumers upsert by key and can replay from an offset after an outage."),
           ("Watch the slot", "A stalled consumer makes the database keep WAL forever; alert on replication slot lag."),
           ("Decide the contract", "Raw table events leak your schema; for other teams, publish curated events (outbox) instead.")],
    vocab=[("CDC", "Change data capture: streaming row changes out of a database."),
           ("WAL / binlog", "The database's own ordered log of changes."),
           ("Log-based CDC", "Reading the log (vs. polling or triggers)."),
           ("Replication slot", "PostgreSQL bookmark for where a consumer is in the WAL."),
           ("Snapshot", "Initial full copy before streaming changes."),
           ("Dual write", "The app writing to two systems itself (the anti-pattern).")],
    code=dict(file="cdc.sql + event.json", note="PostgreSQL + Debezium", src="""
-- postgresql.conf: wal_level = logical
CREATE PUBLICATION app_changes FOR TABLE orders, customers;

-- Debezium creates a replication slot and streams each change:
{
  "op": "u",                                   // c = insert, u = update, d = delete
  "before": { "id": 9041, "status": "paid" },
  "after":  { "id": 9041, "status": "shipped" },
  "source": { "table": "orders", "lsn": 2398123408 },
  "ts_ms": 1762941660000
}

-- keep an eye on how far behind consumers are
SELECT slot_name, pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), confirmed_flush_lsn))
FROM pg_replication_slots;
"""),
    tools="tools: Debezium (PostgreSQL, MySQL, SQL Server, MongoDB, Oracle), Kafka Connect, AWS DMS, Google Datastream, Fivetran, Airbyte, Estuary, PostgreSQL logical replication, MongoDB change streams, DynamoDB Streams.",
    gains=["<b>One write, many copies</b>, always in sync eventually.",
           "<b>Catches every write path</b>, including scripts and admin SQL.",
           "<b>Ordered and replayable</b>: consumers catch up after outages.",
           "<b>Near real time</b> instead of nightly exports.",
           "<b>Little extra load</b> on the database (reads the log)."],
    losses=["<b>More infrastructure</b>: connectors, Kafka, monitoring.",
            "<b>Eventual consistency</b> for the copies.",
            "<b>Your table schema becomes an API</b> if others consume raw events.",
            "<b>Stuck slots</b> can fill the database disk."],
    baseline="Each line compares <b>dual writes and nightly exports from the app</b> to <b>log-based CDC</b> feeding the same systems.",
    ratings=[(3, 2, "A connector and a stream to run and understand."),
             (3, 3, "Neutral for the source database."),
             (2, 4, "The app writes once instead of four times."),
             (2, 5, "Committed changes only, in order, from every writer."),
             (2, 4, "Consumers scale independently of the database."),
             (3, 3, "Topics and retained WAL take space."),
             (2, 4, "Every change is available to new consumers."),
             (3, 2, "Slot lag, connector restarts and schema changes to watch."),
             (2, 4, "New consumers plug in without touching the app.")],
    pitfalls=[("A forgotten replication slot", "A consumer stops, PostgreSQL keeps every WAL file, the disk fills.", "alert on slot lag; set <code>max_slot_wal_keep_size</code>."),
              ("Exposing raw tables to other teams", "Renaming a column breaks three downstream services.", "publish curated events (transactional outbox) for external contracts."),
              ("Non-idempotent consumers", "A connector restart replays events and doubles counts.", "upsert by key, track offsets."),
              ("Forgetting deletes", "The search index keeps rows deleted in the database.", "handle <code>op = d</code> and tombstones.")],
    use=["Keeping search indexes, caches and warehouses in sync.",
         "Replacing nightly batch exports with near-real-time feeds.",
         "Migrating data to a new database with little downtime.",
         "Audit streams of every change."],
    skip=["A single database with no copies to keep in sync.",
          "Publishing business events to other teams (prefer the outbox).",
          "Teams that can't run and monitor streaming infrastructure yet."],
    related=["<b>Transactional outbox</b> (Vol. 1)", "<b>Materialized views</b>", "<b>History tables</b>", "<b>Publish–subscribe</b> (Vol. 1)"],
    quiz=[("Why are dual writes unsafe?", "The two writes aren't atomic; if one fails after the other succeeds, the systems drift apart silently."),
          ("Why does log-based CDC never emit rolled-back changes?", "It reads committed transactions from the write-ahead log."),
          ("What happens if a CDC consumer stops for a week in PostgreSQL?", "The replication slot keeps WAL from being removed, so disk usage grows until the consumer resumes or the slot is dropped."),
          ("CDC or outbox for events other teams consume?", "Outbox: it publishes deliberate business events, so your internal table schema isn't a public contract.")],
    remember="The database already keeps a <span class=\"hl\">transcript</span>. Let everyone <span class=\"hl\">read it</span>, instead of telling each one yourself.",
    sources=["Debezium documentation, “Debezium Architecture” and PostgreSQL connector.",
             "Martin Kleppmann, “Turning the database inside-out” (talk) and <i>DDIA</i> ch. 11.",
             "PostgreSQL docs, “Logical Replication” and “Replication Slots”.",
             "Gunnar Morling, “Reliable Microservices Data Exchange With the Outbox Pattern”."],
)

NOTES = [OPTLOCK, EXPAND, CDC]
