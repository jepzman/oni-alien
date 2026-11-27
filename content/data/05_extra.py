# Vol. 3 · extra notes (November 2026): Upserts, Bitemporal Data, Vector Indexes.
# Numbered 16–18 so earlier note URLs and PDF names stay the same; each sits in its own collection on the index.

# ------------------------------------------------------------------ 16 Upserts
up_problem = Doodle(760, 270, "Doodle of a nightly price import done as check-then-write. Two import workers both look for SKU 812, both find nothing, and both try to insert it. One succeeds; the other fails with a duplicate-key error at row 4,120 of 10,000, and the job stops halfway with half the prices updated.",
                    "Check, then insert: two workers see “not there” at the same moment.")
up_problem.box(20, 30, 150, 54, "worker A", "blue", size=17)
up_problem.box(20, 170, 150, 54, "worker B", "green", size=17)
up_problem.arrow(174, 50, 300, 90, label="SKU 812? none", lx=200, ly=40, anchor="start")
up_problem.arrow(174, 194, 300, 140, label="SKU 812? none", lx=200, ly=226, anchor="start")
up_problem.table(310, 80, "products", ["… 811", "(812 missing)"], w=170, fill="y", soft=(1,))
up_problem.box(540, 40, 200, 60, "INSERT 812 ✓", "green", size=16)
up_problem.box(540, 150, 200, 70, "INSERT 812 ✗", "pink", stroke="red", sub="duplicate key · job stops", size=16, subsize=13)
up_problem.note(380, 258, "row 4,120 of 10,000: half the prices updated, half not", "red", size=16)

up_analogy = Doodle(760, 250, "Doodle of a hotel front desk. A guest gives a booking reference. If a booking exists, the clerk updates it with the new dates; if not, the clerk creates one. It happens in one step at the desk, so two clerks can never create two bookings for the same reference.",
                    "One desk, one reference: update the booking if it exists, create it if it doesn't.")
up_analogy.icon("receipt", 40, 70, 1.6, fill="y")
up_analogy.note(90, 200, "ref BK-812")
up_analogy.arrow(170, 120, 290, 120)
up_analogy.box(300, 70, 200, 100, "front desk", "blue", sub="one step", size=19, subsize=15)
up_analogy.arrow(504, 100, 576, 60, label="exists", lx=540, ly=60)
up_analogy.arrow(504, 140, 576, 190, label="new", lx=540, ly=192)
up_analogy.box(580, 30, 160, 56, "update dates", "green", size=16)
up_analogy.box(580, 160, 160, 56, "create booking", "y", size=16)

up_how = Doodle(760, 260, "How an upsert works. Each incoming row is inserted. If the unique key, here the SKU, already exists, the database updates that row instead, in the same atomic statement. A WHERE clause skips the update when nothing changed or when the incoming data is older than the stored row.",
                "INSERT … ON CONFLICT (sku) DO UPDATE: the unique key decides, the database does both halves.")
up_how.box(20, 90, 150, 70, "incoming row", "y", sub="sku 812 · €4.10", size=16, subsize=14)
up_how.arrow(174, 125, 246, 125)
up_how.box(250, 70, 200, 110, "unique key", "blue", sub="sku already there?", size=19, subsize=14)
up_how.arrow(454, 100, 546, 50, label="no", lx=496, ly=60)
up_how.arrow(454, 150, 546, 200, label="yes", lx=496, ly=196)
up_how.box(550, 20, 190, 60, "insert it", "green", size=17)
up_how.box(550, 170, 190, 70, "update it", "green", sub="only if newer or different", size=17, subsize=13)

UPSERTS = dict(
    slug="upserts",
    kicker="a.k.a. “insert, or update if it's already there”",
    tldr="When you don't know whether a row exists yet (imports, syncs, counters, “save settings”), don't check first and then write: two writers will both see “not there”. Put a <b>unique constraint</b> on the natural key and use one atomic statement: <b><code>INSERT … ON CONFLICT … DO UPDATE</code></b> (PostgreSQL, SQLite), <b><code>MERGE</code></b> (SQL standard) or <b><code>ON DUPLICATE KEY UPDATE</code></b> (MySQL). Add a condition so old data never overwrites newer data.",
    chips=[("Family", "writing safely"), ("Needs", "a unique constraint on the key"), ("Also called", "merge, insert-or-update"), ("Pairs with", "idempotent consumer, change data capture")],
    problem="""  <p class="lead">A nightly job imports 10,000 prices. For each one it asks “does this SKU exist?”, then inserts or updates. With two workers, both ask about SKU 812 at the same moment, both hear “no”, both insert, and one crashes with a <span class="hl-pink">duplicate-key error halfway through</span>.</p>
  <ul>
    <li><b>Check-then-write races</b>: the gap between the SELECT and the INSERT is where the second writer gets in.</li>
    <li>Without a unique constraint, the race doesn't crash: it silently creates <b>two rows for one SKU</b>.</li>
    <li>Retried messages and re-run imports must not create duplicates or fail on rows they already wrote.</li>
  </ul>""",
    problem_figs=[up_problem],
    analogy_side="the hotel front desk",
    analogy="""  <p>At a hotel desk you give your <b>booking reference</b>. If there's a booking, the clerk changes the dates; if not, the clerk makes one. Both happen <b>at the desk, in one step</b>, and the reference is unique, so two clerks can't create two bookings for it.</p>""",
    analogy_figs=[up_analogy],
    map=[("The booking reference", "The unique key (SKU, email, external id)"),
         ("The desk deciding in one step", "One atomic statement: insert or update"),
         ("Change the dates", "<code>DO UPDATE SET …</code>"),
         ("Make a new booking", "The insert half"),
         ("“Your old request? We already have newer dates”", "<code>WHERE excluded.updated_at &gt; products.updated_at</code>")],
    how_side="one statement, decided by the unique key",
    how="""  <p>The database tries the insert. If it would break the unique constraint, it updates the existing row instead. Both halves happen under the same row lock, so there's no gap for another writer. The rows that were proposed are available as <code>EXCLUDED</code> (PostgreSQL) or <code>source</code> (MERGE).</p>""",
    how_figs=[up_how],
    steps=[("Pick the natural key", "What makes a row “the same row”: the SKU, the email, the partner's id, (user_id, setting)."),
           ("Make it unique", "A UNIQUE constraint or index on exactly those columns. Without it, there is nothing to conflict on."),
           ("Write one statement", "<code>INSERT … ON CONFLICT (sku) DO UPDATE SET …</code>, or <code>MERGE</code>, or MySQL's <code>ON DUPLICATE KEY UPDATE</code>."),
           ("Guard the update", "Skip it when nothing changed (<code>IS DISTINCT FROM</code>) or when the incoming row is older."),
           ("Batch it", "Upsert hundreds of rows per statement with a multi-row VALUES list or <code>UNNEST</code>; it's far faster than one round trip per row.")],
    vocab=[("Upsert", "Insert a row, or update it if its key already exists."),
           ("Natural key", "The real-world value that identifies a row (SKU, email)."),
           ("ON CONFLICT", "PostgreSQL and SQLite's upsert clause."),
           ("MERGE", "The SQL standard statement for insert / update / delete by match."),
           ("EXCLUDED", "The row you tried to insert, inside DO UPDATE."),
           ("Race condition", "A bug that depends on two operations interleaving.")],
    code=dict(file="import_prices.sql", note="PostgreSQL 15+", src="""
-- the natural key must be unique, or there is nothing to conflict on
ALTER TABLE products ADD CONSTRAINT products_sku_key UNIQUE (sku);

-- one statement for a whole batch: insert new SKUs, update known ones
INSERT INTO products (sku, price_cents, updated_at)
SELECT * FROM unnest($1::text[], $2::int[], $3::timestamptz[])
ON CONFLICT (sku) DO UPDATE
   SET price_cents = EXCLUDED.price_cents,
       updated_at  = EXCLUDED.updated_at
 WHERE products.updated_at < EXCLUDED.updated_at          -- never let old data win
   AND products.price_cents IS DISTINCT FROM EXCLUDED.price_cents;

-- the standard spelling (PostgreSQL 15+, SQL Server, Oracle)
MERGE INTO products p
USING staging_prices s ON p.sku = s.sku
WHEN MATCHED AND s.updated_at > p.updated_at THEN
  UPDATE SET price_cents = s.price_cents, updated_at = s.updated_at
WHEN NOT MATCHED THEN
  INSERT (sku, price_cents, updated_at) VALUES (s.sku, s.price_cents, s.updated_at);
"""),
    tools="tools: PostgreSQL <code>ON CONFLICT</code> and <code>MERGE</code>, SQLite <code>ON CONFLICT</code>, MySQL <code>ON DUPLICATE KEY UPDATE</code>, SQL Server / Oracle <code>MERGE</code>, ORMs: Prisma <code>upsert</code>, Django <code>update_or_create</code> and <code>bulk_create(update_conflicts=True)</code>, Rails <code>upsert_all</code>.",
    gains=["<b>No races</b>: the check and the write are one atomic step.",
           "<b>Safe to re-run</b>: imports and retried messages don't duplicate rows.",
           "<b>Fast in batches</b>: one statement for hundreds of rows.",
           "<b>Simpler code</b>: no “does it exist?” branch."],
    losses=["<b>Needs a unique key</b>, which some legacy tables don't have.",
            "<b>Dialects differ</b>: ON CONFLICT, MERGE and MySQL's syntax aren't interchangeable.",
            "<b>Easy to overwrite newer data</b> without a guard.",
            "<b>Hidden work</b>: triggers, sequences and row locks still fire on the conflict path."],
    baseline="Each line compares <b>SELECT, then INSERT or UPDATE in code</b> to <b>one upsert statement on a unique key</b>.",
    ratings=[(3, 4, "One statement instead of a branch."),
             (3, 3, "Neutral."),
             (2, 4, "One round trip, batchable."),
             (2, 5, "No duplicates, no lost race."),
             (2, 4, "No locking dance between workers."),
             (3, 3, "Neutral (the unique index costs a little)."),
             (3, 3, "Neutral."),
             (2, 4, "Re-runnable imports, fewer 3 a.m. failures."),
             (3, 3, "Neutral.")],
    pitfalls=[("No unique constraint", "ON CONFLICT has nothing to conflict on, so every run inserts new rows.", "add the UNIQUE constraint first, and clean up existing duplicates."),
              ("Old data wins", "A delayed retry with yesterday's price overwrites today's.", "guard the update with a version or timestamp comparison."),
              ("DO NOTHING hides problems", "Conflicting rows are skipped silently, including ones that should have updated.", "use DO NOTHING only when the existing row is always right; count what was skipped."),
              ("MERGE assumed to be race-free", "On some databases (SQL Server) MERGE can still race without a lock hint.", "read your database's notes; add HOLDLOCK / SERIALIZABLE where advised, or use ON CONFLICT.")],
    use=["Imports and syncs from another system.",
         "Consumers that may receive the same message twice.",
         "Settings and preferences: one row per user and key.",
         "Counters and aggregates keyed by day or by item."],
    skip=["The key isn't really unique in your domain (two people can share an email).",
          "Creating and updating need different rules or permissions; keep them separate.",
          "You need to know which happened and act differently; use RETURNING (xmax) or two explicit paths."],
    related=["<b>Idempotent consumer</b> (Vol. 1)", "<b>Optimistic locking</b>", "<b>Change data capture</b>", "<b>Surrogate keys</b>"],
    quiz=[("Why does “SELECT, then INSERT” fail under concurrency?", "Two writers can both run the SELECT before either inserts; both see “not there” and both try to insert."),
          ("What does ON CONFLICT need in order to work?", "A unique constraint or unique index on the columns you name; that's what defines a conflict."),
          ("What is EXCLUDED?", "The row you tried to insert, available inside DO UPDATE so you can copy its values."),
          ("How do you stop a late, older message from overwriting newer data?", "Add a WHERE to the update that compares a version or timestamp: update only if the incoming row is newer.")],
    quiz_sit=[("A partner sends product updates as webhooks, sometimes twice and sometimes out of order. Your handler does SELECT, then INSERT or UPDATE, and you see duplicate products and prices going backwards. What do you change?",
               "Add a unique constraint on the partner's product id, replace the handler's branch with one upsert, and guard the update with the partner's updated_at (or a version), so duplicates collapse and older messages can't overwrite newer ones.")],
    try_it="Write an import that does SELECT then INSERT, and run two copies at once against the same 1,000 rows. Count the duplicate-key errors (or the duplicate rows, if there's no unique constraint). Replace it with <code>INSERT … ON CONFLICT DO UPDATE</code> on a unique key, run both copies again, and then re-run the whole import to check it changes nothing.",
    remember="One <span class=\"hl\">unique key</span>, one <span class=\"hl\">statement</span>. And never let old data win.",
    sources=["PostgreSQL documentation, “INSERT … ON CONFLICT” and “MERGE”.",
             "MySQL documentation, “INSERT … ON DUPLICATE KEY UPDATE”.",
             "Michael J. Swart, “Mythbusting: Concurrent Update/Insert Solutions” (2011), on MERGE races in SQL Server.",
             "SQLite documentation, “UPSERT”."],
)

# ------------------------------------------------------------------ 17 Bitemporal data
bt_problem = Doodle(760, 260, "Doodle of an overwritten correction. On 5 March an invoice is sent using a price of 10 euros, valid from 1 March. On 20 March someone corrects the price for 1 March to 12 euros by updating the row. Now nobody can explain the invoice: the database says the price on 1 March was 12 euros, and the old value is gone.",
                    "The correction is right. But now the 5 March invoice can't be explained.")
bt_problem.box(20, 40, 210, 70, "5 March: invoice", "y", sub="used €10 for 1 March", size=16, subsize=13)
bt_problem.box(20, 160, 210, 70, "20 March: fix", "blue", sub="UPDATE price = €12", size=16, subsize=13)
bt_problem.table(330, 70, "prices", ["sku 812 · from 1 Mar · €12"], w=260, fill="y")
bt_problem.arrow(234, 195, 326, 110)
bt_problem.note(460, 180, "the €10 is gone", "red", size=17)
bt_problem.note(460, 210, "“why did we charge €10?”", "red", size=17)

bt_analogy = Doodle(760, 250, "Doodle of a ship's logbook. An entry says the ship was at a certain position on Monday at noon. On Thursday the navigator finds a mistake and adds a correction in red ink, dated Thursday, saying the Monday position was different. The Monday entry is never erased: you can read what the log said on any day, and what really happened.",
                    "A logbook: corrections are added in red, dated, never rubbed out.")
bt_analogy.icon("book", 40, 50, 1.8, fill="y")
bt_analogy.box(190, 40, 260, 60, "Mon 12:00 · pos A", "paper", sub="written Monday", size=16, subsize=13)
bt_analogy.box(190, 140, 260, 60, "Mon 12:00 · pos B", "pink", stroke="red", sub="correction, written Thursday", size=16, subsize=13)
bt_analogy.note(600, 90, "when it happened:", size=16)
bt_analogy.note(600, 114, "Monday (both lines)", "pen", size=16)
bt_analogy.note(600, 170, "when we wrote it:", size=16)
bt_analogy.note(600, 194, "Monday, then Thursday", "pen", size=16)

bt_how = Doodle(760, 300, "The two time lines of a bitemporal row. Valid time is when the price applied in the real world: from 1 March. Recorded time is when the database believed it: the 10 euro row was believed from 1 March until 20 March, then closed; the 12 euro row has been believed since 20 March. A query can ask: what did we believe on 5 March about 1 March? The answer is 10 euros.",
                "Two time axes per row: when it was true, and when we knew it.")
bt_how.line("M80 30 V250 H740", thin=True)
bt_how.note(740, 276, "valid time (when it was true) →", anchor="end", size=15)
bt_how.text(70, 40, "recorded", "t-s", anchor="end", size=14)
bt_how.text(70, 58, "time ↓", "t-s", anchor="end", size=14)
bt_how.text(70, 90, "1 Mar", "t-s", anchor="end", size=14)
bt_how.text(70, 160, "20 Mar", "t-s", anchor="end", size=14)
bt_how.box(140, 74, 600, 70, "€10 · valid from 1 Mar", "paper", sub="recorded 1 Mar → 20 Mar (closed)", size=16, subsize=13)
bt_how.box(140, 150, 600, 70, "€12 · valid from 1 Mar", "green", sub="recorded 20 Mar → now", size=16, subsize=13)
bt_how.line("M300 40 V240", color="red", dash=True)
bt_how.note(310, 46, "5 Mar: what did we believe? → €10", "red", anchor="start", size=15)

BITEMPORAL = dict(
    slug="bitemporal-data",
    kicker="a.k.a. “what was true, and what did we know?”",
    tldr="A history table answers “what was the value on that day?”. Some questions need more: “what did <b>we believe</b> on 5 March about the price on 1 March?” <b>Bitemporal</b> rows carry two time ranges: <b>valid time</b> (when the fact was true in the world) and <b>recorded time</b> (when the database held that belief). A correction never updates in place: it closes the old row's recorded range and adds a new row, so every past report can be reproduced exactly.",
    chips=[("Family", "modelling time"), ("Builds on", "history tables (one time axis)"), ("Standard", "SQL:2011 application-time and system-versioned tables"), ("Pairs with", "event sourcing, audit logging")],
    problem="""  <p class="lead">An invoice on 5 March used a price of €10 valid from 1 March. On 20 March someone finds the price was really €12 and fixes the row. Correct, and now <span class="hl-pink">nobody can explain the invoice</span>: the database says the 1 March price was €12, and the €10 it believed at the time is gone.</p>
  <ul>
    <li>A plain history table keeps <b>versions over time</b>, but a back-dated correction rewrites what that time looked like.</li>
    <li>Auditors, regulators and support ask “why did the system do that, on that day?” and need the data <b>as it was known then</b>.</li>
    <li>Insurance, payroll, pricing and contracts change <b>in the past</b> all the time: retroactive raises, late claims, corrected rates.</li>
  </ul>""",
    problem_figs=[bt_problem],
    analogy_side="a ship's logbook",
    analogy="""  <p>A ship's log is never rubbed out. When the navigator finds on Thursday that Monday's position was wrong, they add a <b>correction in red ink, dated Thursday</b>, next to the Monday entry. You can now read two things: <b>where the ship really was on Monday</b>, and <b>what the log said on any given day</b>.</p>""",
    analogy_figs=[bt_analogy],
    map=[("When the ship was there (Monday)", "Valid time: <code>valid_from</code> / <code>valid_to</code>"),
         ("When the line was written (Monday, then Thursday)", "Recorded time: <code>recorded_from</code> / <code>recorded_to</code>"),
         ("A correction in red ink", "Close the old row's recorded range, insert a new row"),
         ("Never rubbing out", "No UPDATE of facts, no DELETE"),
         ("Reading the log as of Tuesday", "Query <code>AS OF</code> a recorded time")],
    how_side="two time ranges per row",
    how="""  <p>Each row says: <b>this value applied for this period</b> (valid time), and <b>we held this belief for this period</b> (recorded time). The database sets recorded time itself, from the transaction clock; people set valid time. A query fixes both: “price valid on 1 March, as recorded on 5 March”.</p>""",
    how_figs=[bt_how],
    steps=[("Decide which facts need it", "Prices, rates, contracts, entitlements: facts that are corrected after they've been used. Most tables only need a history table."),
           ("Add both ranges", "<code>valid_period</code> and <code>recorded_period</code> as ranges (or four timestamp columns), with “open” meaning until further notice."),
           ("Forbid overlaps", "An exclusion constraint (or the database's temporal support) stops two current beliefs about the same moment."),
           ("Correct by closing and inserting", "In one transaction: end the old row's recorded range now, insert the corrected row with recorded time from now."),
           ("Query with both times", "“As known now” for normal screens; “as known on date X” to reproduce a past report or invoice.")],
    vocab=[("Valid time", "When a fact was true in the real world (also: application or business time)."),
           ("Recorded time", "When the database held the fact (also: transaction or system time)."),
           ("Bitemporal", "Tracking both time axes on the same row."),
           ("As-of query", "A query fixed to a past recorded time."),
           ("Retroactive change", "A correction that applies to a period in the past."),
           ("Exclusion constraint", "A PostgreSQL rule that stops overlapping ranges for the same key.")],
    code=dict(file="prices_bitemporal.sql", note="PostgreSQL ranges", src="""
CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE TABLE prices (
  sku            text      NOT NULL,
  price_cents    int       NOT NULL,
  valid_period   daterange NOT NULL,                            -- when it applied
  recorded_period tstzrange NOT NULL DEFAULT tstzrange(now(), NULL),  -- when we believed it
  EXCLUDE USING gist (sku WITH =, valid_period WITH &&, recorded_period WITH &&)
);

-- correct the price for March, on 20 March: close the old belief, add the new one
BEGIN;
UPDATE prices SET recorded_period = tstzrange(lower(recorded_period), now())
 WHERE sku = '812' AND valid_period && '[2026-03-01,2026-04-01)' AND upper_inf(recorded_period);
INSERT INTO prices (sku, price_cents, valid_period) VALUES ('812', 1200, '[2026-03-01,2026-04-01)');
COMMIT;

-- what did we believe on 5 March about the price on 1 March?
SELECT price_cents FROM prices
 WHERE sku = '812' AND valid_period @> date '2026-03-01'
   AND recorded_period @> timestamptz '2026-03-05 12:00';
"""),
    tools="tools: PostgreSQL ranges + exclusion constraints (temporal_tables / periods extensions), SQL Server and MariaDB system-versioned tables (recorded time), IBM Db2 and Oracle bitemporal support, XTDB (bitemporal by design), Datomic (recorded time).",
    gains=["<b>Every past report can be reproduced</b>, exactly as it was.",
           "<b>Corrections are safe</b>: they never destroy what was believed.",
           "<b>Clear audit answers</b>: what we knew, and when we knew it.",
           "<b>Retroactive changes</b> (late raises, corrected rates) fit naturally."],
    losses=["<b>Harder queries</b>: every read must pick both times.",
            "<b>More rows</b>: every correction adds one.",
            "<b>Easy to get wrong</b> by hand; constraints and helpers are a must.",
            "<b>Patchy database support</b> for valid time."],
    baseline="Each line compares <b>a history table with one time axis</b> to <b>bitemporal rows with valid and recorded time</b>.",
    ratings=[(4, 2, "Two time ranges in every query."),
             (4, 3, "Range indexes help, but reads do more."),
             (4, 3, "Corrections are two writes in a transaction."),
             (3, 5, "Nothing believed is ever lost."),
             (3, 3, "Neutral: grows with corrections, not reads."),
             (3, 2, "Extra rows and range indexes."),
             (3, 5, "Any “as of” question can be asked."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral.")],
    pitfalls=[("Bitemporal everything", "Every table gets four timestamps and every query gets harder.", "use it only for facts that are corrected after they're used; keep history tables elsewhere."),
              ("Updating in place", "Someone “just fixes” a price with a plain UPDATE.", "allow changes only through a function or procedure, and revoke direct UPDATE."),
              ("Overlapping beliefs", "Two current rows claim different prices for the same day.", "an exclusion constraint on (key, valid range, recorded range)."),
              ("App clock for recorded time", "Recorded time set by the app drifts or can be faked.", "let the database set it from the transaction time.")],
    use=["Prices, rates, tariffs and contracts used in invoices.",
         "Insurance, payroll and benefits, where changes are back-dated.",
         "Regulated reporting that must be reproducible.",
         "Any “why did the system decide that, then?” question."],
    skip=["Facts are never corrected after use; a history table is enough.",
          "You only need “who changed what, when”; use an audit log.",
          "The team can't keep every query honest about both times."],
    related=["<b>History tables</b>", "<b>Event sourcing</b> (Vol. 1)", "<b>Audit logging</b> (Vol. 5)", "<b>Star schema</b>"],
    quiz=[("What is the difference between valid time and recorded time?", "Valid time is when a fact was true in the world; recorded time is when the database held it as its belief."),
          ("Why can't a history table answer “what did we believe on 5 March”?", "A back-dated correction rewrites the version for that period, so the earlier belief is lost."),
          ("How is a correction stored?", "Close the old row's recorded range at now, and insert the corrected row with recorded time from now, in one transaction."),
          ("Who should set recorded time?", "The database, from the transaction clock, so it can't drift or be faked.")],
    quiz_sit=[("A customer disputes a March invoice. The rate table was corrected in April with a back-dated change, and support can't see the rate the invoice used. What should the table have been, and what do you do now?",
               "Bitemporal: corrections close the old belief and add a new row, so “rate for March as known on the invoice date” stays answerable. Now: use backups or the audit log to reconstruct the old rate for this dispute, and convert the rate table so the next correction keeps both."),],
    try_it="Take a table of prices or rates you own. Add valid and recorded ranges in a copy (with the exclusion constraint above), load a few months of data, then make a back-dated correction. Write two queries: the current price for a past date, and the price for that date as known a week before the correction.",
    remember="Two clocks: <span class=\"hl\">when it was true</span>, and <span class=\"hl\">when we knew it</span>. Correct in red ink, never with an eraser.",
    sources=["Richard T. Snodgrass, <i>Developing Time-Oriented Database Applications in SQL</i> (1999).",
             "Martin Fowler, “Bitemporal History” (2021).",
             "Krishna Kulkarni and Jan-Eike Michels, “Temporal features in SQL:2011”, <i>SIGMOD Record</i> (2012).",
             "PostgreSQL documentation, “Range Types” and “Exclusion Constraints”."],
)

# ------------------------------------------------------------------ 18 Vector indexes
vi_problem = Doodle(760, 260, "Doodle of semantic search done by brute force. A shopper searches for budget trainers. Each of 5 million product embeddings is compared with the query, one by one. The answer is good, cheap running shoes, but it takes 2.4 seconds and uses a whole CPU core per query.",
                    "Compare the query with every row: the right answer, far too slowly.")
vi_problem.box(14, 90, 206, 70, "“budget trainers”", "y", sub="query vector", size=16, subsize=13)
vi_problem.arrow(224, 125, 270, 125)
vi_problem.msgs(280, 70, 12, fill="paper", size=26, gap=6)
vi_problem.msgs(280, 110, 12, fill="paper", size=26, gap=6)
vi_problem.msgs(280, 150, 12, fill="paper", size=26, gap=6)
vi_problem.note(470, 210, "compare with all 5,000,000 vectors", "red", size=17)
vi_problem.note(470, 240, "2.4 s per search · one CPU core busy", "red", size=17)

vi_analogy = Doodle(760, 260, "Doodle of finding a book in a library arranged by topic. Instead of reading every spine, you go to the floor for the right subject, then the right section, then look along the nearby shelves. You might miss a book shelved in a strange place, but you find almost everything nearby in seconds.",
                    "Go to the right floor, then the right shelf, then look around: almost always enough.")
vi_analogy.row([("floor", "sports", "paper"), ("section", "running", "y"), ("shelf", "shoes", "green")], x=20, y=40, h=80, gap=50, size=19, subsize=15, arrows=True)
vi_analogy.note(380, 170, "you don't read all 5 million spines", "pen", size=17)
vi_analogy.note(380, 202, "and once in a while you miss one shelved oddly", "red", size=16)

vi_how = Doodle(760, 290, "How an HNSW vector index searches. The graph has layers: a sparse top layer with long links and a dense bottom layer with short ones. A search enters at the top, greedily moves to the neighbour closest to the query, drops a layer, and repeats, ending with a small neighbourhood in the bottom layer from which the nearest items are returned.",
                "HNSW: long hops on the sparse top layers, short hops at the bottom. A few hundred comparisons, not millions.")
for i, (y, n, lab) in enumerate([(40, 4, "top layer: few nodes, long links"), (120, 8, "middle layer"), (200, 16, "bottom: every item, short links")]):
    xs = [80 + k * (560 / (n - 1)) for k in range(n)]
    vi_how.line(f"M{xs[0]:.0f} {y} H{xs[-1]:.0f}", thin=True)
    for x in xs:
        vi_how.circle(round(x), y, 7, fill="paper")
    vi_how.note(80, y - 14, lab, anchor="start", size=14)
vi_how.arrow(80, 40, 453, 40, color="green")
vi_how.arrow(456, 46, 477, 113, color="green")
vi_how.arrow(487, 120, 553, 120, color="green")
vi_how.arrow(561, 127, 565, 191, color="green")
vi_how.circle(565, 200, 11, fill="green")
vi_how.note(565, 232, "nearest ✓", "green", size=16)
vi_how.note(300, 264, "tune: m (links per node) · ef (how wide each search looks)", "pen", size=16)

VECTOR_INDEXES = dict(
    slug="vector-indexes",
    kicker="a.k.a. “nearest by meaning, without checking everything”",
    tldr="Search by meaning turns text, images or products into <b>embeddings</b>: long lists of numbers where similar things are close together. Finding the closest ones by comparing against every row is exact but slow. An <b>approximate nearest-neighbour (ANN) index</b>, usually <b>HNSW</b> or <b>IVF</b>, finds almost all of the true nearest items in milliseconds. You trade a little <b>recall</b> for a lot of speed, so measure recall, and plan how filters and re-embedding work before you rely on it.",
    chips=[("Family", "reading fast"), ("Common kinds", "HNSW graph · IVF clusters · product quantization"), ("Lives in", "pgvector, a search engine, or a vector database"), ("Pairs with", "indexing, cache-aside, AI app patterns (Vol. 7)")],
    problem="""  <p class="lead">“Budget trainers” should find “cheap running shoes”: no shared words, same meaning. Embeddings make that possible, but finding the nearest of <b>5 million</b> vectors by comparing each one takes <span class="hl-pink">2.4 seconds and a whole CPU core per search</span>.</p>
  <ul>
    <li>A normal B-tree index can't help: “close in meaning” isn't a sort order.</li>
    <li>Exact search grows with the table; ten times more products means ten times slower.</li>
    <li>Search, recommendations and retrieval for AI features all need this lookup, many times per page.</li>
  </ul>""",
    problem_figs=[vi_problem],
    analogy_side="a library arranged by topic",
    analogy="""  <p>In a library arranged by topic, you don't read every spine. You go to the <b>sports floor</b>, then the <b>running section</b>, then look along <b>nearby shelves</b>. You find almost everything you'd want in seconds. Now and then a book shelved somewhere odd is missed: that's the price of not checking everything.</p>""",
    analogy_figs=[vi_analogy],
    map=[("A book's place in the topic layout", "Its embedding: a vector of, say, 768 numbers"),
         ("Floor → section → shelf", "The index's coarse-to-fine search (HNSW layers, IVF clusters)"),
         ("Looking along nearby shelves", "Checking a small candidate set (<code>ef_search</code>, <code>probes</code>)"),
         ("The oddly shelved book you miss", "Recall below 100%: approximate, not exact"),
         ("Re-shelving after a new system", "Re-embedding everything when the model changes")],
    how_side="search a graph, not the whole table",
    how="""  <p><b>HNSW</b> links each vector to its nearest neighbours in several layers. A search enters at the sparse top, hops greedily toward the query, drops a layer, and repeats, comparing a few hundred vectors instead of millions. <b>IVF</b> instead groups vectors into clusters and searches only the few clusters nearest the query. HNSW is usually faster and more accurate; IVF builds faster and uses less memory.</p>""",
    how_figs=[vi_how],
    steps=[("Store embeddings with their model", "A vector column plus the model name and version, so you know which vectors belong together."),
           ("Choose the distance", "Cosine for most text models (or inner product on normalised vectors); use the one the model was trained for."),
           ("Build an ANN index", "pgvector: <code>CREATE INDEX … USING hnsw (embedding vector_cosine_ops)</code>; or IVF with a list count."),
           ("Measure recall", "Run 100 real queries exactly (no index) and with the index; recall@10 = share of the true top 10 the index found. Tune until it's good enough, often 95%+."),
           ("Plan filters and updates", "Decide how “in stock, in the shopper's country” combines with the search, and how you re-embed when the model changes.")],
    vocab=[("Embedding", "A vector of numbers that places similar items close together."),
           ("Nearest-neighbour search", "Finding the vectors closest to a query vector."),
           ("ANN", "Approximate nearest neighbour: fast, finds most of the true nearest."),
           ("HNSW", "Hierarchical navigable small world: a layered graph index."),
           ("IVF", "Inverted file index: vectors grouped into clusters."),
           ("Recall@k", "Share of the true top k results the index returns.")],
    code=dict(file="search.sql", note="PostgreSQL + pgvector 0.8", src="""
CREATE EXTENSION IF NOT EXISTS vector;

ALTER TABLE products ADD COLUMN embedding vector(768);       -- from one embedding model
ALTER TABLE products ADD COLUMN embedding_model text;          -- which one (re-embed on change)

CREATE INDEX products_embedding_hnsw ON products
  USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);

-- per query: look wider for better recall, and keep filtering inside the index scan
SET hnsw.ef_search = 100;
SET hnsw.iterative_scan = relaxed_order;   -- keep searching if filters remove too many

SELECT id, name, embedding <=> $1 AS distance      -- <=> is cosine distance
  FROM products
 WHERE in_stock AND country = $2
 ORDER BY embedding <=> $1
 LIMIT 10;
"""),
    tools="tools: pgvector (PostgreSQL), OpenSearch / Elasticsearch k-NN, Redis vector search, SQLite sqlite-vec, Qdrant, Weaviate, Milvus, FAISS (library), ann-benchmarks.com for comparing index types.",
    gains=["<b>Milliseconds instead of seconds</b> at millions of vectors.",
           "<b>Search by meaning</b>, not just matching words.",
           "<b>One store</b> with pgvector: vectors next to the rows they describe.",
           "<b>Tunable</b>: trade recall for speed per query."],
    losses=["<b>Approximate</b>: some true matches are missed.",
            "<b>Memory hungry</b>: HNSW indexes like to fit in RAM.",
            "<b>Slow builds</b> and slower inserts than a B-tree.",
            "<b>Filters are tricky</b> and model changes mean re-embedding everything."],
    baseline="Each line compares <b>exact search over every vector</b> to <b>an HNSW index on the same vectors</b>.",
    ratings=[(4, 3, "An index to tune and a recall number to watch."),
             (1, 5, "Milliseconds instead of seconds."),
             (4, 2, "Each insert updates the graph."),
             (5, 4, "Results are approximate."),
             (1, 4, "Grows roughly with log n, not n."),
             (4, 2, "The graph often doubles the memory."),
             (3, 3, "Neutral: filters need care."),
             (4, 3, "Index builds and memory to watch."),
             (3, 2, "A model change means re-embedding and rebuilding.")],
    pitfalls=[("Filtering after the search", "The index returns the 10 nearest, then the WHERE removes 9 out-of-stock ones, and the shopper sees one result.", "use iterative or filtered index scans, partial indexes per common filter, or ask for more candidates."),
              ("Mixing models", "New products embedded with a new model, old ones with the old model: distances mean nothing.", "store the model with each vector; re-embed everything before switching queries."),
              ("Never measuring recall", "The index silently returns worse results after a parameter change.", "keep a fixed set of queries with exact answers and check recall@10 in CI or a nightly job."),
              ("Index bigger than memory", "HNSW pages are read from disk and latency jumps.", "size RAM for the index, use smaller vectors (or half precision), or quantize.")],
    use=["Semantic search, “similar items” and recommendations.",
         "Retrieval for AI features (RAG) over your own documents.",
         "Deduplicating near-identical text or images.",
         "More than a few thousand vectors per query."],
    skip=["A few thousand vectors: exact search is fast enough and has perfect recall.",
          "Keyword or exact-match search does the job (SKUs, names, codes).",
          "You can't afford to re-embed when the model changes, and need results to stay stable."],
    related=["<b>Indexing</b>", "<b>Cache-aside</b> (Vol. 1)", "<b>Materialized views</b>", "<b>Multitenancy</b>"],
    quiz=[("Why can't a B-tree index speed up nearest-neighbour search on embeddings?", "A B-tree orders values along one dimension; closeness in a 768-dimension space isn't a sort order."),
          ("What does recall@10 measure?", "The share of the true 10 nearest items (from exact search) that the approximate index returned."),
          ("HNSW or IVF: which is usually faster and more accurate, and what does it cost?", "HNSW; it costs more memory and slower builds than IVF."),
          ("Why store the model name with each vector?", "Vectors from different models aren't comparable; you must know which to re-embed when the model changes.")],
    quiz_sit=[("Product search uses pgvector with HNSW. In one country, shoppers often get only two or three results, though many products match. The query filters by country after ordering by distance. What is happening, and what do you change?",
               "The index returns its nearest candidates first, and the country filter removes most of them. Use iterative index scans (or raise ef_search), add a partial index per large country, or include the country in the search, and measure recall for filtered queries specifically.")],
    try_it="Load 100,000 sentences or product titles with embeddings into PostgreSQL with pgvector. Time 100 queries with exact search, then build an HNSW index and time them again. Compute recall@10 for the index against the exact results, then change <code>hnsw.ef_search</code> from 40 to 200 and watch speed and recall move together.",
    remember="Close in <span class=\"hl\">meaning</span>, found in <span class=\"hl\">milliseconds</span>. Approximate, so measure recall.",
    sources=["Yu. A. Malkov and D. A. Yashunin, “Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs” (2016/2018).",
             "Hervé Jégou, Matthijs Douze and Cordelia Schmid, “Product quantization for nearest neighbor search” (2011).",
             "pgvector documentation (github.com/pgvector/pgvector).",
             "ann-benchmarks.com: benchmarks of approximate nearest-neighbour libraries."],
)

NOTES = [UPSERTS, BITEMPORAL, VECTOR_INDEXES]
