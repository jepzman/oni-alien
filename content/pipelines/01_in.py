# Vol. 9 · Getting data in: ETL vs ELT, Incremental Extract, Idempotent Loads, Layered Zones, Late-Arriving Data.
# The shop: a homeware chain with a web store and 30 shops. Orders, order lines, products, customers in PostgreSQL;
# a columnar warehouse for reports. Order 9001 (a kettle €39 and two mugs €8, 31 March 23:58) recurs from deep dive 12.

# ------------------------------------------------------------------ 01 ETL vs ELT
etl_problem = Doodle(760, 270, "Doodle of the shop's old nightly ETL job. It reads orders from the app database, applies tax rules and category mapping in a Python script on a separate server, and writes only daily totals by category into the warehouse. Fourteen months later a tax bug is found. The raw orders were never kept in the warehouse, and the source has changed since, so the old totals cannot be recomputed.",
                     "Transform first, keep only the result: when the rule turns out wrong, the past can't be fixed.")
etl_problem.db(70, 90, "app database", w=90)
etl_problem.arrow(124, 110, 214, 110)
etl_problem.box(220, 60, 210, 100, "nightly script", "blue", sub="tax rules · categories", size=19, subsize=15)
etl_problem.arrow(436, 110, 520, 110)
etl_problem.table(526, 60, "daily_totals", ["day · category", "revenue"], w=200, fill="y")
etl_problem.note(325, 210, "tax bug found: 14 months wrong", "red")
etl_problem.note(625, 170, "raw orders: never kept", "red")
etl_problem.note(380, 250, "“recompute it?” “from what?”", "pen")

etl_analogy = Doodle(760, 250, "Doodle comparing a meal kit and a full pantry. A meal kit arrives pre-cut for one recipe: if the recipe was wrong, the ingredients are already cut. A pantry stocked with whole groceries lets you cook any recipe later, and cook it again if the first attempt was wrong.",
                     "A meal kit is cut for one recipe. A full pantry lets you cook anything, and cook it again.")
etl_analogy.box(20, 40, 300, 120, "meal kit", "pink", sub="pre-cut for one recipe", size=21, subsize=16)
etl_analogy.note(170, 190, "ETL: shaped before it arrives", "red")
etl_analogy.icon("fridge", 420, 40, 1.4, fill="green")
etl_analogy.arrow(520, 90, 600, 60)
etl_analogy.arrow(520, 110, 600, 110)
etl_analogy.arrow(520, 130, 600, 160)
for i, t in enumerate(["soup", "curry", "soup, again"]):
    etl_analogy.note(610, 66 + i * 50, t, "green", anchor="start")
etl_analogy.note(540, 230, "ELT: keep it whole, cook later", "green")

etl_how = Doodle(760, 280, "ELT. Extract and load copy the app database's tables as they are into raw tables in the warehouse. Transformations are SQL models that run inside the warehouse: staging cleans the raw tables, marts shape them into facts and dimensions. Because raw is kept, every model can be changed and rerun over the whole history.",
                 "Copy first, unchanged. Transform with SQL inside the warehouse, as often as you like.")
etl_how.db(60, 100, "app database", w=86)
etl_how.arrow(110, 120, 170, 120, label="E + L", lx=140, ly=100)
etl_how.box(176, 80, 150, 80, "raw", "y", sub="as it came", size=21, subsize=15)
etl_how.arrow(332, 120, 392, 120, label="T", lx=362, ly=100)
etl_how.box(398, 80, 150, 80, "staging", "blue", sub="clean, typed", size=21, subsize=15)
etl_how.arrow(554, 120, 604, 120, label="T", lx=579, ly=100)
etl_how.box(610, 80, 130, 80, "marts", "green", sub="facts + dims", size=21, subsize=15)
etl_how.line("M180 214 H736", dash=True)
etl_how.note(458, 240, "all inside the warehouse · SQL in git · rerun over all history", "pen")
etl_how.arrow(660, 166, 260, 166, curve=(460, 210), dash=True)

ETL = dict(
    slug="etl-vs-elt",
    kicker="a.k.a. “load first, transform later”",
    tldr="<b>ETL</b> transforms data on its way to the warehouse and stores only the result. <b>ELT</b> copies the source data into the warehouse <b>unchanged</b>, then transforms it there with SQL. Cheap columnar storage made ELT the default: keep the raw data, and any transform can be fixed and <b>rerun over the whole history</b>. Transform before loading only what must never be stored, such as card numbers.",
    chips=[("Family", "getting data in"), ("Origin", "ETL tools of the 1990s; ELT with cloud warehouses, 2012+"), ("Lives in", "dbt, SQLMesh, Fivetran, Airbyte"), ("Pairs with", "layered zones, idempotent loads")],
    problem="""  <p class="lead">Since 2019 the shop's nightly job reads orders, applies tax rules and the category mapping in a Python script, and writes <b>daily totals by category</b> to the warehouse. Fourteen months later finance finds that refunds were taxed twice. The raw orders were <span class="hl-pink">never stored in the warehouse</span>, and the app has changed since, so the past cannot be recomputed.</p>
  <ul>
    <li><b>Logic in the extract</b>: business rules live in a script on a server nobody owns, untested and unversioned.</li>
    <li><b>Only the answer is kept</b>: “revenue by hour” or “by customer segment” needs a new job, and has no history.</li>
    <li><b>A bug is permanent</b>: the input is gone, so the output can never be corrected.</li>
  </ul>""",
    problem_figs=[etl_problem],
    analogy_side="meal kit vs pantry",
    analogy="""  <p>A <b>meal kit</b> arrives cut and portioned for one recipe. Convenient, but if the recipe was wrong, the vegetables are already diced. A <b>pantry</b> of whole groceries takes more room, and you cook any recipe from it later, or cook it again.</p>
  <ul>
    <li>Pantries were expensive when shelf space was. Cloud warehouses made shelf space cheap.</li>
    <li>Some things you still prepare before they come in: you don't store what you're not allowed to keep.</li>
  </ul>""",
    analogy_figs=[etl_analogy],
    map=[("Meal kit, pre-cut", "ETL: transformed in flight, only the result stored"),
         ("Whole groceries in the pantry", "Raw tables, copied unchanged"),
         ("The recipe", "SQL models (staging, marts) run in the warehouse"),
         ("Cooking again after a mistake", "Fix the model, rerun over all history"),
         ("Not storing what you mustn't", "Masking card numbers or health data before loading")],
    how_side="extract, load, then transform in SQL",
    how="""  <p>The <b>extract and load</b> step is a copy and nothing more: tables land in a <code>raw</code> schema as they were in the source, with a load timestamp. The <b>transform</b> step is a set of SQL models in git that build staging tables and then marts. They run inside the warehouse, so they scale with it, and they can be tested and reviewed like any other code.</p>""",
    how_figs=[etl_how],
    steps=[("Copy, don't change", "A connector (Fivetran, Airbyte, Debezium or your own) lands source tables in raw, unchanged."),
           ("Mask only what must be", "Drop or hash card numbers and secrets before landing; nothing else happens in flight."),
           ("Write transforms as SQL models", "One file per table: staging models clean, mart models shape. Versioned in git."),
           ("Test and review them", "Unique keys, not-null columns, accepted values, run in CI and on every load."),
           ("Rerun freely", "A changed rule means change the model and rebuild; the raw data is still there.")],
    vocab=[("ETL", "Extract, transform, load: shape the data before it reaches the warehouse."),
           ("ELT", "Extract, load, transform: land raw data, shape it inside the warehouse."),
           ("Raw", "Source data stored as it arrived, never edited."),
           ("Model", "One SQL SELECT that builds one table or view (dbt's word)."),
           ("Connector", "The tool that copies data from a source into the warehouse."),
           ("Reverse ETL", "Copying warehouse results back into apps such as a CRM.")],
    code=dict(file="models/marts/fct_daily_revenue.sql", note="dbt · any warehouse", src="""
-- the rule lives here, in git, and can be rerun over all history
select
    s.order_date,
    p.category,
    sum(s.amount_net)                  as revenue_net,
    sum(s.amount_net * s.tax_rate)     as tax
from {{ ref('fct_sales') }}   s
join {{ ref('dim_product') }} p using (product_key)
where not s.is_refund_tax_line          -- the 2019 bug, fixed once, for every year
group by 1, 2
"""),
    tools="tools: loaders Fivetran, Airbyte, Stitch, Debezium, cloud DMS; transforms dbt, SQLMesh, Dataform; classic ETL suites Informatica, SSIS, Talend (still common for masking and mainframe sources).",
    then_now=dict(src="Kimball &amp; Caserta, 2004",
                  then="<i>The Data Warehouse ETL Toolkit</i> describes a separate ETL server that cleans, conforms and loads data, because warehouse disk and CPU were expensive. Only the finished, conformed tables were stored; the staging area was temporary.",
                  now="Columnar cloud warehouses split storage from compute, and keeping raw data costs little. Transforms became SQL in git, tested and reviewed (dbt, from 2016). ETL survives where data must be masked before landing, and inside streaming jobs that enrich events in flight.",
                  verdict="rethought",
                  take="Load first and keep raw; transform in the warehouse. Transform before loading only what must never be stored."),
    gains=["<b>History can be fixed</b>: change a rule and rebuild every year from raw.",
           "<b>New questions are cheap</b>: the detail is there, not just yesterday's totals.",
           "<b>Logic is code</b>: SQL in git, reviewed, tested, with lineage.",
           "<b>One engine</b>: transforms scale with the warehouse, not a side server."],
    losses=["<b>More storage</b>: raw and every layer are kept.",
            "<b>Sensitive data lands</b> unless you mask it in flight on purpose.",
            "<b>Warehouse compute bills</b> grow with every rebuild.",
            "<b>SQL sprawl</b>: hundreds of models need naming rules and ownership."],
    baseline="Each line compares <b>a nightly script that stores only daily totals</b> to <b>raw tables plus SQL models in the warehouse</b>.",
    ratings=[(2, 4, "One copy step, logic in readable SQL."),
             (3, 3, "Neutral: both run on a schedule."),
             (2, 4, "Bugs can be fixed for every past day."),
             (1, 5, "Any model can be rebuilt from raw."),
             (2, 4, "Transforms scale with the warehouse."),
             (4, 3, "Raw storage and rebuilds cost money."),
             (1, 5, "Every column of every row is there to ask about."),
             (2, 4, "Tests and lineage come with the models."),
             (2, 5, "A new column is a new line of SQL.")],
    pitfalls=[("Transforming in the loader", "Business rules creep into connector settings and scripts again.", "keep the load a plain copy; every rule is a model."),
              ("Raw that isn't raw", "Someone “cleans up” raw in place, and the original is gone.", "make raw append-only and read-only for everyone but the loader."),
              ("Personal data landed by accident", "A new source column with card numbers lands in raw and is queryable.", "mask or drop listed columns in flight, and scan raw for patterns."),
              ("Rebuild everything, every hour", "Full rebuilds of large models eat the compute budget.", "build big models incrementally (idempotent loads); rebuild fully only after a logic change.")],
    use=["A warehouse with cheap storage and SQL compute.",
         "Rules that change and need to apply to the past.",
         "Analysts who ask new questions every week.",
         "Several sources that have to be combined."],
    skip=["Data that must be masked or dropped before it may be stored: do that part in flight.",
          "Streams that must be enriched in milliseconds; transform in the stream processor.",
          "A tiny report from one table, where a view on a read replica is enough."],
    related=["<b>Layered zones</b>", "<b>Idempotent loads</b>", "<b>Star schema</b> (Vol. 3)", "<b>Change data capture</b> (Vol. 3)"],
    quiz=[("What does ELT change compared with ETL?", "The data is loaded unchanged first, and transformed inside the warehouse with SQL, so raw data is kept."),
          ("Why can an ELT pipeline fix last year's numbers?", "Raw data is still stored; change the model and rebuild it over all history."),
          ("When should you still transform before loading?", "For data that must never be stored, such as card numbers: mask or drop it in flight."),
          ("What is a model in dbt?", "A SQL SELECT in a file that builds one table or view, referencing other models.")],
    quiz_sit=[("Finance finds that a discount was counted twice in revenue since January. Your pipeline stores only monthly totals. What do you change, beyond fixing the formula?",
               "Start landing the order lines unchanged in raw and build revenue as a SQL model from them. Then the fix is a change to one model and a rebuild; for January to now, reload the order lines from the source (or a backup) once.")],
    try_it="Take one report built by a script. Land its source tables unchanged in a <code>raw</code> schema (DuckDB is enough), rewrite the logic as two SQL views (staging, then the report), and change one rule. Rebuild and compare last year's numbers before and after.",
    remember="Keep the <span class=\"hl\">groceries</span>, not just the meal. Transform in the warehouse, and you can always cook it again.",
    sources=["Ralph Kimball and Joe Caserta, <i>The Data Warehouse ETL Toolkit</i> (2004).",
             "Joe Reis and Matt Housley, <i>Fundamentals of Data Engineering</i> (2022), chapter 8.",
             "dbt Labs, “What is ELT?” and the dbt documentation on models.",
             "Tristan Handy, “The Analytics Engineer” (2019)."],
)

# ------------------------------------------------------------------ 02 Incremental Extract
inc_problem = Doodle(760, 260, "Doodle of a nightly full copy that no longer fits the night. The job copies all 60 million order lines, 25 gigabytes, starting at 01:00. At 06:10 it is still running when the first shops open, and the read replica it copies from is lagging, slowing the app.",
                     "The full copy grew past the night: 60 million rows, 25 GB, still running at opening time.")
inc_problem.line("M40 130 H720")
for i, t in enumerate(["01:00", "02:00", "03:00", "04:00", "05:00", "06:00"]):
    inc_problem.note(60 + i * 128, 160, t, size=16)
    inc_problem.line(f"M{60 + i * 128} 124 v12")
inc_problem.box(60, 70, 610, 44, "copying order_lines · 60 M rows · 25 GB", "y", size=18)
inc_problem.box(600, 190, 150, 50, "shops open", "pink", stroke="red", size=17)
inc_problem.note(400, 230, "still copying at 06:10 · replica 4 min behind", "red")

inc_analogy = Doodle(760, 240, "Doodle of a meter reader. Each month the reader notes the meter value and bills only the difference since last month's reading. The previous reading is written on the card, like a bookmark.",
                     "The meter reader bills the difference since the last reading on the card.")
inc_analogy.icon("gauge", 60, 60, 1.6)
inc_analogy.note(110, 190, "meter now: 41,380")
inc_analogy.box(260, 60, 220, 90, "last reading", "y", sub="card: 40,910", size=20, subsize=16)
inc_analogy.arrow(486, 105, 560, 105)
inc_analogy.box(566, 60, 170, 90, "bill 470", "green", sub="only the change", size=20, subsize=16)
inc_analogy.note(370, 210, "save today's reading on the card, after the bill is sent", "pen")

inc_how = Doodle(760, 300, "How an incremental extract works. A watermarks table stores the last updated_at loaded for order_lines, 23:50. The next run selects rows whose updated_at is later than the watermark minus a ten minute safety overlap. It merges them into staging by key, and only after that commits does it save the new watermark, the largest updated_at it saw.",
                 "Read past the watermark minus an overlap, merge by key, then move the watermark.")
inc_how.table(20, 40, "etl_watermarks", ["order_lines · 23:50"], w=220, fill="y")
inc_how.arrow(246, 70, 316, 70)
inc_how.box(322, 30, 230, 80, "SELECT changed", "blue", sub="updated_at > 23:50 − 10 min", size=19, subsize=14)
inc_how.arrow(558, 70, 616, 70)
inc_how.box(622, 30, 120, 80, "MERGE", "green", sub="on line id", size=20, subsize=14)
inc_how.arrow(682, 116, 682, 190)
inc_how.box(560, 196, 190, 70, "save watermark", "y", sub="max seen: 00:14", size=18, subsize=14)
inc_how.arrow(554, 230, 130, 102, curve=(320, 250), dash=True)
inc_how.note(300, 280, "only after the merge commits", "pen")
inc_how.note(330, 150, "overlap re-reads a little:", "pen")
inc_how.note(330, 174, "harmless, because MERGE", "pen")

INC = dict(
    slug="incremental-extract",
    kicker="a.k.a. “high-water mark”",
    tldr="Instead of copying a whole table every night, copy only the rows that <b>changed since the last run</b>, found by a column such as <code>updated_at</code> and a saved <b>watermark</b>. Two rules make it safe: re-read a small <b>overlap</b> behind the watermark (transactions commit late) and <b>merge by key</b> so the overlap does no harm. It cannot see hard deletes; for those use CDC or a key comparison.",
    chips=[("Family", "getting data in"), ("Needs", "a trusted, indexed updated_at"), ("Also called", "delta load, high-water mark"), ("Pairs with", "idempotent loads, change data capture")],
    problem="""  <p class="lead">The shop copies all of <code>order_lines</code> every night. At 60 million rows and 25 GB it now starts at 01:00 and is <span class="hl-pink">still running when the shops open</span>, while the replica it reads from falls behind and slows the app. Only about 108,000 rows changed since yesterday.</p>
  <ul>
    <li>The work grows with the <b>size of the table</b>, not with the size of the change.</li>
    <li>The report can't be fresher than once a night.</li>
    <li>Every run puts the heaviest possible read on the source.</li>
  </ul>""",
    problem_figs=[inc_problem],
    analogy_side="the meter reader",
    analogy="""  <p>A meter reader doesn't count every unit since the house was built. They write down today's value and bill the <b>difference since the last reading</b>, which is on the card. The card is updated only after the bill goes out, so a lost bill never skips a month.</p>""",
    analogy_figs=[inc_analogy],
    map=[("The meter", "A column that only grows: <code>updated_at</code>, an id, a version"),
         ("Last reading on the card", "The watermark, saved per table"),
         ("Billing the difference", "<code>WHERE updated_at &gt; :watermark</code>"),
         ("Updating the card after billing", "Save the watermark only after the load commits"),
         ("A house that was demolished", "A deleted row: it has no reading to change")],
    how_side="watermark, overlap, merge, then move the watermark",
    how="""  <p>Keep a small table of watermarks, one per source table. Each run reads rows changed after the watermark <b>minus an overlap</b>, merges them into staging on the primary key, and then stores the largest <code>updated_at</code> it saw. The overlap exists because a row is stamped when it is written but becomes visible when its transaction commits, which can be later than the next run.</p>""",
    how_figs=[inc_how],
    steps=[("Find a reliable change column", "<code>updated_at</code> set by the database (a trigger or default), never by app clocks; or an always-increasing id for append-only tables."),
           ("Index it", "So each run is a short range scan, not a full scan."),
           ("Read with an overlap", "<code>updated_at &gt; watermark − 10 min</code>: longer than your longest transaction."),
           ("Merge by key", "So rows read twice are updated, not duplicated."),
           ("Save the watermark last", "In the same transaction as the merge, or after it commits, never before.")],
    vocab=[("Watermark", "The last change position loaded, saved between runs."),
           ("Overlap window", "How far behind the watermark each run re-reads."),
           ("Delta", "The rows that changed since the last run."),
           ("Full refresh", "Copy the whole table again."),
           ("Hard delete", "A row removed from the table; invisible to timestamp extracts."),
           ("Reconciliation", "Comparing counts, sums or keys between source and copy.")],
    code=dict(file="extract_order_lines.sql", note="source: PostgreSQL", src="""
-- 1 · read the delta, with a safety overlap behind the watermark
SELECT *
FROM   order_lines
WHERE  updated_at >  :watermark - interval '10 minutes'
  AND  updated_at <= now() - interval '1 minute'   -- leave in-flight rows for next time
ORDER  BY updated_at;

-- 2 · in the warehouse: MERGE the rows into stg_order_lines on order_line_id

-- 3 · only then move the watermark
UPDATE etl_watermarks
SET    last_value = :max_updated_at_seen
WHERE  table_name = 'order_lines';

-- in the source, once: make updated_at trustworthy
CREATE TRIGGER order_lines_touch BEFORE UPDATE ON order_lines
FOR EACH ROW EXECUTE FUNCTION set_updated_at_now();
"""),
    tools="tools: Airbyte and Fivetran (“incremental” sync modes with a cursor column), dbt <code>is_incremental()</code>, AWS Glue job bookmarks, Azure Data Factory watermark pattern; for deletes and exact ordering use CDC (Debezium) instead.",
    gains=["<b>Work grows with change</b>, not with table size.",
           "<b>Fresher</b>: cheap enough to run every 15 minutes or hourly.",
           "<b>Light on the source</b>: an index range scan, not a full scan.",
           "<b>No new infrastructure</b>: just SQL and one small table."],
    losses=["<b>Blind to hard deletes</b>.",
            "<b>Trusts one column</b>: a script that skips <code>updated_at</code> hides its changes.",
            "<b>Late commits</b> are missed without an overlap.",
            "<b>Only the latest version</b> is seen; changes between runs are lost."],
    baseline="Each line compares <b>a nightly full copy of the table</b> to <b>an incremental extract by watermark with overlap and merge</b>.",
    ratings=[(4, 3, "A watermark and an overlap to understand."),
             (1, 4, "Cheap enough to run hourly or more."),
             (5, 3, "Deletes and untouched updates slip through."),
             (4, 3, "Reruns are safe with MERGE; backfills need a reset."),
             (1, 4, "Work follows the change, not the table."),
             (2, 4, "Far less data read and moved."),
             (3, 3, "Neutral: same columns land."),
             (3, 3, "Watermark lag is one more thing to watch."),
             (3, 3, "Neutral.")],
    pitfalls=[("No overlap", "A transaction that commits after the run with an older timestamp is skipped forever.", "re-read a window longer than your longest transaction, and cap transaction time."),
              ("updated_at set by the app", "A bulk UPDATE script doesn't set it, and its changes never arrive.", "set it in the database with a trigger or default, so every write path updates it."),
              ("Watermark moved too early", "The job saves the watermark, then fails loading; those rows are skipped.", "save it in the same transaction as the load, or after it commits."),
              ("Deletes forgotten", "Cancelled orders that were hard-deleted stay in revenue.", "use soft deletes, CDC, or a periodic comparison of all keys.")],
    use=["Large tables where only a small share changes each day.",
         "Sources where you can't get log access for CDC.",
         "Append-only tables with an increasing id (events, logs).",
         "SaaS APIs that offer “changed since” queries."],
    skip=["Small tables: a full copy is simpler and always right.",
          "Tables with hard deletes you must see: use CDC.",
          "You need every intermediate version, not just the latest: use CDC."],
    related=["<b>Change data capture</b> (Vol. 3)", "<b>Idempotent loads</b>", "<b>Late-arriving data</b>", "<b>Soft delete</b> (Vol. 3)"],
    quiz=[("Why re-read an overlap behind the watermark?", "Rows are stamped when written but visible when committed; a long transaction can commit after the run with an older timestamp."),
          ("Why must the load merge rather than append?", "The overlap reads some rows twice; a merge updates them, an append would duplicate them."),
          ("When should the watermark be saved?", "After the load commits, or in the same transaction, so a failed load is retried rather than skipped."),
          ("What can an incremental extract by timestamp never see?", "Hard-deleted rows, because no row is left to select.")],
    quiz_sit=[("A support script fixes 3,000 order totals with a plain UPDATE once a month. The warehouse never shows the fixes. Why, and what do you change?",
               "The script doesn't set updated_at, so the extract never sees those rows. Set updated_at in the database with a trigger on every update, then re-extract the affected period once (reset the watermark or run a targeted backfill).")],
    try_it="In PostgreSQL, open a transaction, insert a row with <code>updated_at = now()</code>, and keep it open. In another session, run your extract and save the watermark. Commit the first transaction and run the extract again. Did it find the row? Add a 10-minute overlap and a merge, and try again.",
    remember="Read <span class=\"hl\">past the bookmark, minus a little</span>, merge by key, and move the bookmark last.",
    sources=["Ralph Kimball and Joe Caserta, <i>The Data Warehouse ETL Toolkit</i> (2004), on change data capture by audit columns.",
             "Airbyte documentation, “Incremental sync: append and deduped”.",
             "PostgreSQL documentation, “Transaction isolation” and <code>idle_in_transaction_session_timeout</code>.",
             "dbt documentation, “Incremental models”."],
)

# ------------------------------------------------------------------ 03 Idempotent Loads
idem_problem = Doodle(760, 260, "Doodle of a rerun that doubled a day. The load for 31 March fails halfway after appending 52,000 of 100,000 rows. The engineer reruns it. The load appends all 100,000 again. The fact table now holds 152,000 rows for 31 March, and the dashboard shows the best day of the year.",
                      "Append, fail, rerun, append again: half of 31 March is counted twice.")
idem_problem.box(20, 40, 200, 70, "run 1", "blue", sub="appends 52k · fails", size=20, subsize=15)
idem_problem.box(20, 150, 200, 70, "run 2 (rerun)", "blue", sub="appends 100k", size=19, subsize=15)
idem_problem.arrow(226, 75, 330, 110)
idem_problem.arrow(226, 185, 330, 150)
idem_problem.table(336, 70, "fact_sales · 31 Mar", ["52,000 rows (run 1)", "100,000 rows (run 2)"], w=250, fill="y")
idem_problem.note(690, 110, "152,000", "red", size=22)
idem_problem.note(690, 140, "best day ever?", "red")
idem_problem.note(460, 230, "the rerun was the right move; the load wasn't safe to repeat", "pen")

idem_analogy = Doodle(760, 240, "Doodle of a bookkeeper's ledger. The bookkeeper doesn't add lines for a day again when re-doing it; they rub out the whole page for 31 March and rewrite it from the receipts. Doing it twice gives the same page.",
                      "Re-doing a day means rewriting its page from the receipts, not adding more lines.")
idem_analogy.icon("ledger", 40, 50, 1.6, fill="y")
idem_analogy.note(100, 190, "page: 31 March")
idem_analogy.arrow(170, 110, 290, 110, label="rub out", lx=230, ly=96)
idem_analogy.icon("receipt", 300, 50, 1.4)
idem_analogy.arrow(390, 110, 510, 110, label="rewrite", lx=450, ly=96)
idem_analogy.box(520, 60, 210, 90, "same page", "green", sub="every time", size=21, subsize=16)
idem_analogy.note(380, 220, "once or five times: the result is the same", "pen")

idem_how = Doodle(760, 290, "Two idempotent ways to load a batch for 31 March. Replace the slice: in one transaction, delete every row for 31 March and insert the batch, or overwrite the 31 March partition. Merge on key: match each incoming line on order_line_id, update it if the incoming version is newer, insert it if new. Both give the same table however many times they run.",
                  "Replace the whole slice, or merge on a key. Either way, run it twice and nothing changes.")
idem_how.box(20, 110, 160, 70, "batch", "y", sub="31 Mar · 100k lines", size=20, subsize=14)
idem_how.arrow(186, 130, 300, 70)
idem_how.arrow(186, 160, 300, 220)
idem_how.box(306, 30, 434, 80, "replace the slice", "blue", sub="delete 31 Mar + insert, in one transaction", size=20, subsize=15)
idem_how.box(306, 180, 434, 80, "MERGE on order_line_id", "green", sub="update if newer · insert if new", size=20, subsize=15)
idem_how.note(523, 146, "or overwrite partition 2026-03-31", "pen", size=16)

IDEM = dict(
    slug="idempotent-loads",
    kicker="a.k.a. “safe to run twice”",
    tldr="Every load will be rerun one day: after a failure, a fix, a backfill or a scheduler retry. Make sure running a batch twice gives <b>the same table</b> as running it once. Either <b>replace the whole slice</b> (delete and insert a day, or overwrite its partition, in one transaction) or <b>MERGE on a key</b> with a “newer only” guard. Never blindly append, and keep hidden clocks such as <code>now()</code> out of the transform.",
    chips=[("Family", "getting data in"), ("Also called", "rerunnable, deterministic loads"), ("Origin", "functional data engineering (Beauchemin, 2018)"), ("Pairs with", "upserts, incremental extract")],
    problem="""  <p class="lead">The load for 31 March fails halfway, after appending 52,000 of 100,000 lines. The on-call engineer does the right thing and reruns it. The load appends all 100,000 again, and <span class="hl-pink">31 March now holds 152,000 lines</span>. The dashboard shows the best day of the year.</p>
  <ul>
    <li>Append-only loads turn every retry into duplicates.</li>
    <li>Engineers learn to fear reruns, and fix data by hand instead.</li>
    <li>Backfills after a bug fix need special scripts, and get them wrong.</li>
  </ul>""",
    problem_figs=[idem_problem],
    analogy_side="rewriting the ledger page",
    analogy="""  <p>A careful bookkeeper redoing 31 March doesn't add the day's lines again at the bottom. They <b>rub out the page for 31 March</b> and rewrite it from the receipts. Do it once or five times: the page is the same.</p>""",
    analogy_figs=[idem_analogy],
    map=[("The page for one day", "A slice: the partition or rows for one date"),
         ("Rubbing out the page", "<code>DELETE … WHERE order_date = :day</code> or overwrite the partition"),
         ("Rewriting from receipts", "Insert the batch, built only from its inputs"),
         ("Correcting one line by its number", "MERGE on <code>order_line_id</code>"),
         ("The same page every time", "Idempotent: f(f(x)) = f(x)")],
    how_side="replace a slice, or merge on a key",
    how="""  <p><b>Replace the slice</b> when a batch is “everything for this day”: delete the day and insert it, in one transaction, or use the warehouse's partition overwrite. <b>Merge on a key</b> when a batch is “these rows changed”, as with CDC or an incremental extract: match on the source key and update only if the incoming version is newer, so a replayed or out-of-order row changes nothing.</p>
  <p>Idempotent also means <b>deterministic</b>: the transform must use only its inputs and the period it was given, never <code>now()</code> or <code>current_date</code>, or a rerun for last Tuesday gives a different answer.</p>""",
    how_figs=[idem_how],
    steps=[("Choose the slice or the key", "Daily batches: slice by event date. Change streams: the source's primary key."),
           ("Make it one transaction", "Delete and insert together, or a single MERGE, so a crash leaves the old slice or the new one, never half."),
           ("Guard merges with a version", "Update only when the incoming <code>updated_at</code> or log position is newer."),
           ("Pass the period in", "The scheduler's logical date is a parameter; no <code>now()</code> inside."),
           ("Test it", "Run the load twice in CI and compare: the tables must be identical.")],
    vocab=[("Idempotent", "Doing it twice has the same effect as doing it once."),
           ("Deterministic", "The same inputs always give the same output."),
           ("Partition overwrite", "Replace one partition's contents atomically."),
           ("Logical date", "The period a run is for, as opposed to when it ran."),
           ("Backfill", "Running the normal job for past periods."),
           ("Newer-only guard", "A merge condition that ignores older versions.")],
    code=dict(file="load_fact_sales.sql", note="generic warehouse SQL", src="""
-- A · replace the slice: one day, one transaction
BEGIN;
DELETE FROM fact_sales WHERE order_date = :day;
INSERT INTO fact_sales
SELECT * FROM stg_sales_enriched WHERE order_date = :day;
COMMIT;

-- B · merge on the key, newer versions only
MERGE INTO fact_sales t
USING stg_sales_changes s
   ON t.order_line_id = s.order_line_id
WHEN MATCHED AND s.updated_at > t.updated_at THEN
  UPDATE SET qty = s.qty, amount = s.amount, updated_at = s.updated_at
WHEN NOT MATCHED THEN
  INSERT (order_line_id, order_date, product_key, qty, amount, updated_at)
  VALUES (s.order_line_id, s.order_date, s.product_key, s.qty, s.amount, s.updated_at);
"""),
    tools="tools: dbt incremental strategies (<code>merge</code>, <code>delete+insert</code>, <code>insert_overwrite</code>), BigQuery and Spark partition overwrite, Snowflake and Databricks MERGE, Airflow and Dagster logical dates and partitions for backfills.",
    gains=["<b>Reruns are boring</b>: retry, fix and backfill with the same job.",
           "<b>No duplicates</b> after failures or scheduler retries.",
           "<b>Late updates handled</b> (merge): a return can update an old day.",
           "<b>Backfills are just runs</b> for past dates."],
    losses=["<b>Slice replace rewrites</b> whole days even for one changed row.",
            "<b>MERGE reads the target</b> to find matches, which costs on huge tables.",
            "<b>Needs a real key</b> or a clean slice boundary.",
            "<b>Discipline</b>: one <code>now()</code> breaks determinism."],
    baseline="Each line compares <b>an append-only load</b> to <b>a load that replaces its slice or merges on a key</b>.",
    ratings=[(4, 4, "Same amount of SQL, different verbs."),
             (3, 3, "Neutral."),
             (2, 5, "No duplicates or half-loaded days."),
             (1, 5, "Run any batch again, any time."),
             (4, 3, "MERGE and slice rewrites cost more at scale."),
             (4, 3, "Some extra reads and rewrites."),
             (3, 3, "Neutral."),
             (3, 4, "Uniqueness tests catch the rest."),
             (3, 4, "Logic changes are a rebuild, not a migration.")],
    pitfalls=[("Delete and insert in two transactions", "A crash between them leaves the day empty.", "one transaction, or an atomic partition overwrite."),
              ("Merge without a guard", "A late, older event overwrites the newer row.", "compare <code>updated_at</code> or log position in the WHEN MATCHED clause."),
              ("Hidden clock", "<code>current_date</code> in a model means a rerun on Thursday rebuilds the wrong day.", "use the run's logical date, passed in."),
              ("Duplicates in the batch itself", "Two versions of one key in a batch make MERGE fail or pick one at random.", "dedupe the batch to the latest version per key first.")],
    use=["Every load into staging, facts and dimensions.",
         "Any job a scheduler may retry automatically.",
         "Pipelines that are backfilled after logic changes.",
         "Change streams that may deliver an event twice."],
    skip=["The raw landing layer: append there on purpose, and dedupe downstream.",
          "One-off exports nobody will ever rerun (but they usually are).",
          "Append-only logs where duplicates are filtered by an id later."],
    related=["<b>Upserts</b> (Vol. 3)", "<b>Idempotent consumer</b> (Vol. 1)", "<b>Incremental extract</b>", "<b>Late-arriving data</b>"],
    quiz=[("What makes a load idempotent?", "Running it twice gives the same table as running it once."),
          ("Why must delete and insert be in one transaction?", "Otherwise a failure between them leaves the slice empty or half-loaded."),
          ("Why add a newer-only guard to a MERGE?", "So a replayed or out-of-order older version doesn't overwrite a newer row."),
          ("Why is now() a problem inside a transform?", "A rerun for a past period then gives a different answer; the period should be a parameter.")],
    quiz_sit=[("Your scheduler retries failed tasks three times. A load into fact_sales appends rows and sometimes fails on a timeout after committing. Revenue is occasionally 2× for a day. What do you change?",
               "Make the load replace its day (delete and insert in one transaction, or partition overwrite) or merge on order_line_id, so retries after a commit change nothing. Add a uniqueness test on order_line_id that fails the run.")],
    try_it="Write a load that appends a day's rows into a table. Run it twice and count rows. Change it to delete-and-insert in one transaction, run it three times, and compare the table with <code>EXCEPT</code> against a single run. Then add <code>current_date</code> somewhere and see your test break.",
    remember="Rub out the <span class=\"hl\">whole page</span>, or match by <span class=\"hl\">line number</span>. Never just add more lines.",
    sources=["Maxime Beauchemin, “Functional Data Engineering: a modern paradigm for batch data processing” (2018).",
             "dbt documentation, “About incremental strategy”.",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017), chapter 10.",
             "Google Cloud, BigQuery documentation on partition overwrite with MERGE and write dispositions."],
)

# ------------------------------------------------------------------ 04 Layered Zones
lz_problem = Doodle(760, 270, "Doodle of analysts querying raw change tables directly. Five dashboards each read raw.order_lines_changes and each removes duplicates its own way, so they show five different revenue numbers. Someone also deleted bad rows from raw to clean it, and the original data is gone.",
                    "Every dashboard cleans raw its own way: five dashboards, five revenues, and raw “cleaned” in place.")
lz_problem.table(270, 90, "raw.order_lines_changes", ["c · u · u · d · …"], w=250, fill="y")
for i, (x, y, t) in enumerate([(20, 20, "€412k"), (20, 190, "€409k"), (600, 20, "€415k"), (600, 190, "€398k"), (310, 200, "€412k")]):
    lz_problem.box(x, y, 140, 50, t, "paper", size=18)
for (x1, y1, x2, y2) in [(160, 45, 266, 104), (160, 215, 266, 136), (600, 45, 524, 104), (600, 215, 524, 136), (380, 200, 380, 152)]:
    lz_problem.arrow(x1, y1, x2, y2, color="red")
lz_problem.note(395, 74, "DELETE … “bad rows”", "red")

lz_analogy = Doodle(760, 240, "Doodle of a restaurant kitchen in three stations. The delivery bay keeps crates exactly as delivered, labelled. The prep station washes and chops into containers. The pass plates the dishes customers see. Nobody plates straight from a crate.",
                    "Delivery bay, prep station, the pass. Guests only ever see what leaves the pass.")
lz_analogy.row([("delivery bay", "crates as delivered", "y"), ("prep station", "washed, chopped", "blue"), ("the pass", "plated dishes", "green")], y=50, h=90, gap=60, size=20, subsize=15, arrows=True)
lz_analogy.icon("box", 90, 160, 0.8)
lz_analogy.icon("kitchen", 350, 156, 0.8)
lz_analogy.icon("plate", 600, 160, 0.9)

lz_how = Doodle(760, 300, "Three layers. Raw: append-only, exactly as received, with load metadata, readable only by pipelines. Staging: typed and renamed columns, one row per key, deletes flagged. Marts: facts and dimensions with business definitions, the only layer reports read. Each layer reads only from the one before it.",
                "Each layer reads only the one before it. Reports read only marts. Nobody edits raw.")
lz_how.box(20, 40, 220, 130, "raw", "y", sub="as received · append only", size=24, subsize=15)
lz_how.box(270, 40, 220, 130, "staging", "blue", sub="typed · one row per key", size=24, subsize=15)
lz_how.box(520, 40, 220, 130, "marts", "green", sub="facts · dims · definitions", size=24, subsize=15)
lz_how.arrow(244, 105, 266, 105)
lz_how.arrow(494, 105, 516, 105)
lz_how.note(130, 200, "pipelines only", "pen")
lz_how.note(380, 200, "data engineers", "pen")
lz_how.note(630, 200, "analysts, dashboards", "pen")
lz_how.arrow(630, 270, 630, 214, label="reports read here", lx=630, ly=292)
lz_how.note(250, 270, "rebuild staging and marts from raw at any time", "green")

LZ = dict(
    slug="layered-zones",
    kicker="a.k.a. “medallion: bronze, silver, gold”",
    tldr="Give the warehouse three layers with clear promises. <b>Raw</b> holds data exactly as received, append-only. <b>Staging</b> holds one clean, typed row per source key. <b>Marts</b> hold facts and dimensions with business definitions, and are the <b>only layer reports read</b>. Each layer is built only from the one before it, so staging and marts can always be rebuilt from raw.",
    chips=[("Family", "getting data in"), ("Also called", "medallion (bronze/silver/gold), landing/staging/presentation"), ("Lives in", "dbt projects, lakehouses"), ("Pairs with", "ETL vs ELT, write–audit–publish")],
    problem="""  <p class="lead">Analysts query the raw change tables directly. Each dashboard removes duplicates and deletes its own way, so five dashboards show <span class="hl-pink">five different revenue numbers</span>. To “help”, someone deletes bad rows from raw, and now the original data is gone as well.</p>
  <ul>
    <li><b>Cleaning logic is copied</b> into every report, each slightly different.</li>
    <li><b>A fix means editing forty dashboards</b>, and missing some.</li>
    <li><b>Raw edited in place</b> can never be replayed.</li>
  </ul>""",
    problem_figs=[lz_problem],
    analogy_side="a restaurant kitchen",
    analogy="""  <p>A kitchen has a <b>delivery bay</b> where crates are kept as delivered and labelled, a <b>prep station</b> where vegetables are washed and chopped into containers, and <b>the pass</b> where dishes are plated. Guests only see what leaves the pass, and nobody plates straight from a crate.</p>""",
    analogy_figs=[lz_analogy],
    map=[("Crates as delivered", "Raw: append-only, exactly as received"),
         ("The delivery label", "Load metadata: source, load time, log position"),
         ("Washed and chopped", "Staging: typed, renamed, one row per key"),
         ("Plated dishes", "Marts: facts and dimensions"),
         ("Guests only see the pass", "Reports and dashboards read only marts")],
    how_side="three promises, one direction",
    how="""  <p>Each layer makes one promise. <b>Raw</b>: nothing is ever changed or lost. <b>Staging</b>: one current, typed row per source key, nothing else (no joins between sources, no business rules). <b>Marts</b>: business meaning, one definition per measure. Data flows one way, and permissions follow the layers: analysts can't even see raw.</p>""",
    how_figs=[lz_how],
    steps=[("Land in raw", "One table per source table, append-only, with <code>_loaded_at</code>, <code>_source</code> and the log position."),
           ("One staging model per raw table", "Rename, cast, dedupe to the latest row per key, flag deletes. No joins."),
           ("Build marts from staging", "Facts and dimensions, joins and business rules live here."),
           ("Lock the layers", "Pipelines write raw; only marts are granted to analysts and BI tools."),
           ("Name by layer", "<code>raw.</code>, <code>stg_</code>, <code>fct_</code>, <code>dim_</code>, so lineage is readable at a glance.")],
    vocab=[("Raw / bronze", "Source data as received, never edited."),
           ("Staging / silver", "Cleaned, typed, one row per key."),
           ("Mart / gold", "Business-ready tables for one area, e.g. sales."),
           ("Lineage", "Which tables each table is built from."),
           ("Grant", "Permission to read a schema or table."),
           ("Retention", "How long raw data is kept before deletion.")],
    code=dict(file="models/staging/stg_order_lines.sql", note="dbt", src="""
-- staging: rename, cast, latest version per key, deletes flagged. No business rules.
with ranked as (
    select
        cast(id as bigint)            as order_line_id,
        cast(order_id as bigint)      as order_id,
        cast(qty as int)              as qty,
        cast(line_total as numeric)   as amount,
        _op = 'd'                     as is_deleted,
        _lsn,
        row_number() over (partition by id order by _lsn desc) as rn
    from {{ source('raw', 'order_lines_changes') }}
)
select * from ranked where rn = 1

-- project layout:  models/staging/stg_*.sql   models/marts/fct_*.sql, dim_*.sql
"""),
    tools="tools: dbt (sources, staging and marts folders, grants), Databricks medallion architecture, Snowflake and BigQuery schemas with role-based grants, Dagster asset groups.",
    gains=["<b>One cleaning, one definition</b>: every report agrees.",
           "<b>Replay</b>: rebuild everything from raw after any fix.",
           "<b>Clear ownership</b>: each layer has a promise and an owner.",
           "<b>Safer access</b>: analysts never touch raw or personal fields."],
    losses=["<b>More tables and storage</b>: three copies of some data.",
            "<b>More latency</b>: each layer is one more step.",
            "<b>Ceremony</b> for a tiny project with one source.",
            "<b>Layer drift</b>: rules sneak into staging unless reviewed."],
    baseline="Each line compares <b>reports reading raw source copies</b> to <b>raw, staging and marts with one-way flow</b>.",
    ratings=[(2, 4, "Each layer has one clear job."),
             (3, 3, "Neutral, a step or two of extra latency."),
             (2, 5, "One cleaning and one definition for all."),
             (1, 5, "Raw is kept, everything else rebuilds."),
             (2, 4, "Teams work on separate layers."),
             (4, 3, "Extra storage and compute per layer."),
             (2, 4, "Marts answer most questions directly."),
             (2, 4, "Tests per layer locate the fault."),
             (2, 4, "Source changes stop at staging.")],
    pitfalls=[("Business rules in staging", "Revenue logic creeps into a staging model and is hidden from mart reviewers.", "staging only renames, casts and dedupes; rules belong in marts."),
              ("Reports on staging", "A dashboard reads stg_ tables “just this once”, and breaks at the next source change.", "grant only marts to BI roles."),
              ("Raw without retention", "Raw grows forever, with personal data nobody needs.", "set a retention per source and a deletion process for personal data."),
              ("Layers by name only", "Schemas are called bronze and gold but anything reads anything.", "enforce the one-way rule with permissions and a lineage check in CI.")],
    use=["Several reports or teams use the same sources.",
         "Data arrives as change events or with duplicates.",
         "You need to rebuild after fixes.",
         "Raw data contains fields analysts shouldn't see."],
    skip=["One source, one report, one person: a view may do.",
          "Real-time paths where each layer's delay is too much; keep the stream short.",
          "Adding a fourth and fifth layer “for flexibility”."],
    related=["<b>ETL vs ELT</b>", "<b>Write–audit–publish</b>", "<b>Star schema</b> (Vol. 3)", "<b>Least privilege</b> (Vol. 5)"],
    quiz=[("What does each of the three layers promise?", "Raw: nothing changed or lost. Staging: one clean row per key. Marts: business definitions for reports."),
          ("Why should reports read only marts?", "So cleaning and definitions live in one place, and source changes stop at staging."),
          ("What belongs in a staging model?", "Renaming, casting, deduping to the latest row per key and flagging deletes; no joins or business rules."),
          ("Why must raw never be edited?", "It is the only copy that lets every other layer be rebuilt.")],
    quiz_sit=[("A data scientist asks for read access to raw because “marts don't have the column I need”. What do you do?",
               "Don't grant raw. Add the column to the staging model (rename and cast it) and expose it in the right mart, or build a mart for their use case. Then everyone gets it, cleaned once, and permissions on personal data stay intact.")],
    try_it="Take a dashboard that reads source tables directly. List every cleaning step its SQL does. Move those steps into one staging model, point the dashboard at a mart built from it, and check its number matches before and after.",
    remember="Crates in the <span class=\"hl\">bay</span>, chopping at the <span class=\"hl\">station</span>, guests at the <span class=\"hl\">pass</span>.",
    sources=["Databricks, “What is a medallion architecture?”.",
             "dbt Labs, “How we structure our dbt projects”.",
             "Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), chapter 1.",
             "Joe Reis and Matt Housley, <i>Fundamentals of Data Engineering</i> (2022)."],
)

# ------------------------------------------------------------------ 05 Late-Arriving Data
late_problem = Doodle(760, 270, "Doodle of a late till upload. The Delft shop's till goes offline on Saturday and uploads its sales on Monday morning. The pipeline files rows by the day they were loaded, so Saturday is short by 8,400 euros and Monday is 8,400 too high. Saturday's report has already been sent.",
                      "Sales from Saturday arrive on Monday, and get filed under Monday.")
for i, (d, h, fill, stroke) in enumerate([("Sat", 90, "pink", "red"), ("Sun", 120, "blue", ""), ("Mon", 170, "pink", "red")]):
    late_problem.box(80 + i * 200, 220 - h, 120, h, d, fill, stroke=stroke, size=20)
late_problem.note(140, 100, "−€8,400", "red")
late_problem.note(540, 22, "+€8,400", "red")
late_problem.arrow(160, 150, 520, 80, color="red", curve=(330, 40), dash=True)
late_problem.note(350, 260, "filed by load date, not by sale date", "pen")

late_analogy = Doodle(760, 240, "Doodle of a letter with a postmark. The tax office counts a return as filed on the date of the postmark, even if it reaches the desk three days later. The clerk reopens the folder for that date.",
                      "A letter counts from its postmark, not from the day it reaches the desk.")
late_analogy.icon("envelope", 60, 70, 1.6)
late_analogy.circle(150, 80, 30, "y", label="31/3")
late_analogy.arrow(200, 110, 330, 110, label="arrives 3 Apr", lx=265, ly=96)
late_analogy.icon("cabinet", 340, 60, 1.3)
late_analogy.arrow(430, 110, 540, 110)
late_analogy.box(546, 70, 190, 80, "folder: 31 March", "green", size=18)
late_analogy.note(380, 220, "filed by postmark, folder reopened", "pen")

late_how = Doodle(760, 300, "Handling late data. Every row carries its event time. Facts are partitioned by event date. When Monday's batch arrives it contains Saturday and Monday events, so the job finds the event dates in the batch and rebuilds exactly those two partitions. Events older than the seven-day window go to an adjustments table instead.",
                  "Each batch rebuilds the days its events belong to, not the day it arrived.")
late_how.box(20, 100, 190, 90, "Monday's batch", "y", sub="events: Sat, Mon", size=19, subsize=15)
late_how.arrow(216, 145, 290, 145)
late_how.note(115, 222, "its distinct event dates", "pen")
late_how.box(330, 30, 160, 60, "rebuild Sat", "green", size=19)
late_how.box(330, 200, 160, 60, "rebuild Mon", "green", size=19)
late_how.arrow(296, 145, 326, 60)
late_how.arrow(296, 145, 326, 230)
late_how.box(540, 110, 200, 70, "older than 7 days?", "pink", sub="→ adjustments", size=17, subsize=15)
late_how.arrow(496, 145, 534, 145, dash=True)
late_how.note(410, 140, "Sun untouched", "pen", size=16)

LATE = dict(
    slug="late-arriving-data",
    kicker="a.k.a. “event time, not load time”",
    tldr="Data arrives late: tills upload after an outage, partners resend, returns change old orders. File every row by its <b>event time</b> (when it happened), never by load time. Let each batch <b>rebuild the periods its events belong to</b>, not just “today”. Pick a <b>lateness window</b> (say 7 days) after which closed periods are not changed and late data becomes an <b>adjustment</b> in the current period.",
    chips=[("Family", "getting data in"), ("Also called", "late data, out-of-order events"), ("Two clocks", "event time vs processing time"), ("Pairs with", "idempotent loads, bitemporal data")],
    problem="""  <p class="lead">The Delft shop's till loses its connection on Saturday and uploads its sales on Monday morning. The pipeline files rows by <b>load date</b>, so Saturday is <span class="hl-pink">€8,400 short</span>, Monday is €8,400 too high, and Saturday's report has already gone to the regional managers.</p>
  <ul>
    <li>The wrong day gets the revenue; both days are wrong.</li>
    <li>A pipeline that only processes “today's partition” never fixes Saturday.</li>
    <li>Returns days later change orders from closed weeks.</li>
  </ul>""",
    problem_figs=[late_problem],
    analogy_side="the postmark",
    analogy="""  <p>The tax office counts your return as filed on the <b>postmark</b> date, even if it reaches the desk three days later. The clerk reopens the folder for that date. After the year is closed, a late letter is handled as a correction in the current year, not by rewriting last year's books.</p>""",
    analogy_figs=[late_analogy],
    map=[("The postmark", "Event time: <code>sold_at</code>, <code>placed_at</code>"),
         ("The day it reaches the desk", "Load time: <code>_loaded_at</code>"),
         ("Reopening that date's folder", "Rebuild the event-date partition"),
         ("The year is closed", "The lateness window has passed"),
         ("A correction in the current year", "An adjustment row dated today")],
    how_side="event time decides the period",
    how="""  <p>Carry the event time on every row from the source, and partition facts by event date. When a batch arrives, look at which event dates it contains and rebuild (or merge into) exactly those partitions. That is idempotent, so a late batch, a resend or a replay all do the right thing.</p>
  <p>Decide with the business how late is too late. Within the window, the past is corrected. After it, periods are closed: the late row is booked as an adjustment in the current period, and the closed report never changes.</p>""",
    how_figs=[late_how],
    steps=[("Keep event time", "Every fact row has the time it happened, in a known time zone."),
           ("Partition by event date", "Not by load date; load time is a column for debugging."),
           ("Rebuild touched dates", "Each batch finds its distinct event dates and replaces or merges those partitions."),
           ("Set a lateness window", "With finance: e.g. 7 days, or until month close."),
           ("Book later data as adjustments", "Dated in the current period, linked to the original date, and measure lateness.")],
    vocab=[("Event time", "When it happened in the business."),
           ("Processing time", "When the pipeline handled it."),
           ("Lateness", "Processing time minus event time."),
           ("Lateness window", "How long a closed period may still change."),
           ("Adjustment", "A correction booked in the current period."),
           ("Watermark (streaming)", "The point after which a window is considered complete.")],
    code=dict(file="load_fact_sales_late.sql", note="generic warehouse SQL", src="""
-- which days does this batch touch?
CREATE TEMP TABLE touched AS
SELECT DISTINCT CAST(sold_at AT TIME ZONE 'Europe/Amsterdam' AS date) AS d
FROM   stg_till_sales_batch;

-- inside the window: rebuild those days only (idempotent)
DELETE FROM fact_sales
WHERE  order_date IN (SELECT d FROM touched WHERE d >= current_period_start - 7);
INSERT INTO fact_sales
SELECT * FROM stg_sales_enriched
WHERE  order_date IN (SELECT d FROM touched WHERE d >= current_period_start - 7);

-- outside the window: an adjustment in today's period
INSERT INTO fact_sales_adjustments (booked_on, original_date, store_key, amount)
SELECT :run_date, order_date, store_key, amount
FROM   stg_sales_enriched
WHERE  order_date IN (SELECT d FROM touched WHERE d < current_period_start - 7);
"""),
    tools="tools: dbt incremental models with <code>incremental_predicates</code> on the touched dates, BigQuery and Spark dynamic partition overwrite, Apache Beam and Flink event-time windows with allowed lateness, Kafka timestamps.",
    gains=["<b>Right day, right number</b>, even after outages.",
           "<b>Replays and resends are safe</b>: same dates, same result.",
           "<b>Closed periods stay closed</b>, with a clear rule.",
           "<b>Lateness is measured</b>, so slow sources are visible."],
    losses=["<b>Old reports change</b> within the window; users must know.",
            "<b>More work per batch</b>: several partitions, not one.",
            "<b>A business rule to agree</b>: the window and adjustments.",
            "<b>Time zones</b> become your problem, explicitly."],
    baseline="Each line compares <b>filing rows by load date and processing only today</b> to <b>filing by event time and rebuilding touched dates</b>.",
    ratings=[(4, 3, "Two clocks and a window to explain."),
             (3, 3, "Neutral: same schedule."),
             (2, 5, "Revenue lands on the day it happened."),
             (2, 5, "Resends rebuild the same dates."),
             (4, 3, "Batches may touch many partitions."),
             (4, 3, "Rewrites of older partitions cost a little."),
             (3, 4, "Daily numbers mean what they say."),
             (2, 4, "Lateness becomes a metric."),
             (3, 3, "Neutral.")],
    pitfalls=[("Partitioned by load date", "Late rows land in today, and nothing ever moves them.", "partition facts by event date; keep load time as a column."),
              ("Only today is processed", "The job rebuilds today's partition and ignores the Saturday rows in the batch.", "rebuild every distinct event date in the batch."),
              ("Time zone at random", "Some days are cut in UTC and others in local time; orders near midnight jump days.", "convert to the business time zone once, in staging."),
              ("No window", "A return two years later changes a filed annual report.", "agree a window; after it, book adjustments.")],
    use=["Sources that can be offline: tills, mobile apps, devices.",
         "Partners that resend or batch their data.",
         "Facts that change after the event (returns, corrections).",
         "Any report by day, week or month."],
    skip=["Operational counters where “what arrived today” is the question.",
          "Append-only logs analysed only by arrival time.",
          "When you need every past version, not just the corrected one: use bitemporal tables."],
    related=["<b>Idempotent loads</b>", "<b>Bitemporal data</b> (Vol. 3)", "<b>Lambda vs Kappa</b>", "<b>Fact table types</b>"],
    quiz=[("What is the difference between event time and processing time?", "Event time is when it happened; processing time is when the pipeline handled it."),
          ("Why rebuild the event dates in a batch rather than today?", "Late rows belong to the day they happened; only rebuilding those dates puts them there."),
          ("What happens to data older than the lateness window?", "It is booked as an adjustment in the current period, so closed periods don't change."),
          ("Why convert to one time zone in staging?", "So orders near midnight fall on the same day in every report.")],
    quiz_sit=[("A partner sends last month's sales corrections on the 3rd of each month, but finance closes the month on the 2nd. What do you agree and build?",
               "Agree that the month closes on the 2nd and later corrections are adjustments: load them into an adjustments fact dated in the current month with the original date kept, and show “adjustments to prior months” as its own line. Alternatively, finance moves the close to the 4th.")],
    try_it="Take a table of sales with <code>sold_at</code>. Load three days, then load a batch with one row from day 1. Rebuild only “today”, and compare day 1 with the source. Then rebuild the distinct dates in the batch, and compare again.",
    remember="File it by the <span class=\"hl\">postmark</span>. Reopen only that folder, and only while the year is open.",
    sources=["Tyler Akidau et al., <i>Streaming Systems</i> (2018), chapters 2–3 on event time and watermarks.",
             "Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), on late-arriving facts.",
             "Google Cloud, “Dataflow: windowing and allowed lateness”.",
             "dbt documentation, “incremental_predicates”."],
)

NOTES = [ETL, INC, IDEM, LZ, LATE]
