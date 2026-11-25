# Deep dive 12 · From App Database to Warehouse. Builds on Vol. 3 notes 11 (change data capture), 16 (upserts)
# and 15 (star schema). Example, from the star schema note: a homeware shop's sales, one fact row per order line.
# One order is followed through the whole dive: order 9001, placed at 23:58 on 31 March, a kettle (€39) and two
# mugs (€8 each), €55 in all; one mug is returned on 3 April. Examples use PostgreSQL as the source and generic
# warehouse SQL (MERGE) as the target.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
map_svg = '''
  <rect class="bx" x="10" y="70" width="120" height="64" rx="8"/><text class="lbl" x="70" y="98" text-anchor="middle">app DB</text><text class="soft" x="70" y="120" text-anchor="middle">PostgreSQL</text>
  <rect class="bx-y" x="170" y="70" width="120" height="64" rx="8"/><text class="lbl" x="230" y="98" text-anchor="middle">raw</text><text class="soft" x="230" y="120" text-anchor="middle">every change</text>
  <rect class="bx" x="330" y="70" width="120" height="64" rx="8"/><text class="lbl" x="390" y="98" text-anchor="middle">staging</text><text class="soft" x="390" y="120" text-anchor="middle">current rows</text>
  <rect class="bx-g" x="490" y="70" width="120" height="64" rx="8"/><text class="lbl" x="550" y="98" text-anchor="middle">marts</text><text class="soft" x="550" y="120" text-anchor="middle">facts + dims</text>
  <rect class="bx" x="650" y="70" width="100" height="64" rx="8"/><text class="lbl" x="700" y="98" text-anchor="middle">report</text><text class="soft" x="700" y="120" text-anchor="middle">finance</text>
  <path class="ln" d="M130 102 H168" marker-end="url(#a)"/><path class="ln" d="M290 102 H328" marker-end="url(#a)"/><path class="ln" d="M450 102 H488" marker-end="url(#a)"/><path class="ln" d="M610 102 H648" marker-end="url(#a)"/>
  <text class="soft" x="150" y="58" text-anchor="middle">extract</text><text class="soft" x="310" y="58" text-anchor="middle">dedupe</text><text class="soft" x="470" y="58" text-anchor="middle">model</text><text class="soft" x="630" y="58" text-anchor="middle">query</text>
  <path class="ln-d" d="M170 170 H450"/><text class="soft" x="310" y="194" text-anchor="middle">CDC + upserts: chapters 2, 4, 5</text>
  <path class="ln-d" d="M490 170 H750"/><text class="soft" x="620" y="194" text-anchor="middle">star schema: chapters 2, 3</text>
  <path class="ln-r" d="M230 136 V150 H70 V136" marker-end="url(#ar)"/><text class="bad" x="150" y="226" text-anchor="middle" font-size="16">nothing writes back</text>
'''
recap = '''
<p>A homeware shop sells on the web and in 30 shops. Finance wants revenue by category by day, without slowing down checkout. Three notes from the data volume, put together, give the answer: copy the changes out of the app database, load them so a rerun never double-counts, and shape them as a star for reporting.</p>
''' + tbl(["Note", "In one line"], [
    ["Change Data Capture", "read the database's own change log and stream every committed insert, update and delete"],
    ["Upserts", "insert the row, or update it if the key already exists, in one atomic statement"],
    ["Star Schema", "a fact table of numbers at a stated grain, with flat dimension tables around it"],
]) + fig(760, 240, "The pipeline this deep dive follows. The app database is the source. Changes are extracted into a raw layer that keeps every change. Staging deduplicates them into the current rows. Marts model them as facts and dimensions. The finance report queries the marts. Change data capture and upserts cover the first half, the star schema the second. Nothing in the pipeline writes back to the app database.",
         map_svg, "Four layers, one direction. The notes cover the boxes; this dive covers the arrows.") + mn("The CDC note's going-deeper chapter covers the snapshot, ordering and the slot that fills the disk. This dive starts where it ends: at the warehouse door.") + '''
<p class="full">The notes describe each piece on a good day. In production the pipeline runs every 15 minutes for years, and it is rerun, backfilled, paused for a weekend and pointed at a source table that someone renamed. The questions this dive answers are the ones finance asks: why did March revenue change after we closed March, why is yesterday’s number missing three orders, and why does the warehouse say €55 when the app says €47?</p>
<h3>The order we will follow</h3>
''' + tbl(["When", "What happens to order 9001"], [
    ["31 Mar 23:58", "customer 77 signs up and orders a kettle (€39) and two mugs (€8 each): €55, web store"],
    ["1 Apr 00:00", "payment confirms 40 seconds later; the transaction commits after midnight"],
    ["3 Apr", "one mug is returned: the line changes from 2 × €8 to 1 × €8, the order is now €47"],
    ["12 May", "the kettle moves from category <i>Kitchen</i> to <i>Small appliances</i>"],
], mono=()) + '''
<p class="full">Each event on that list breaks a naive pipeline in a different way. By the end of the dive the same order will be counted once, in the right day, with the right amount, under the category it had when it was sold.</p>
'''

# ------------------------------------------------------------------ 2 the real mechanism
layers_svg = '''
  <rect class="bx-y" x="10" y="20" width="350" height="120" rx="8"/>
  <text class="lbl" x="24" y="46">raw.order_lines_changes</text>
  <text class="soft" x="24" y="74">op c · lsn 1000 · id 51 · qty 2 · €16</text>
  <text class="soft" x="24" y="98">op u · lsn 5200 · id 51 · qty 1 · €8</text>
  <text class="soft" x="24" y="122">append only, never edited</text>
  <rect class="bx" x="400" y="20" width="350" height="120" rx="8"/>
  <text class="lbl" x="414" y="46">stg.order_lines</text>
  <text class="soft" x="414" y="74">id 51 · qty 1 · €8 · lsn 5200</text>
  <text class="soft" x="414" y="98">latest version per key,</text>
  <text class="soft" x="414" y="122">deletes flagged</text>
  <rect class="bx-g" x="10" y="180" width="350" height="120" rx="8"/>
  <text class="lbl" x="24" y="206">mart.fact_sales</text>
  <text class="soft" x="24" y="234">line 51 · date 2026-03-31 · product_key 812</text>
  <text class="soft" x="24" y="258">customer_key 4410 · store_key 1 (web)</text>
  <text class="soft" x="24" y="282">qty 1 · amount €8</text>
  <rect class="bx" x="400" y="180" width="350" height="120" rx="8"/>
  <text class="lbl" x="414" y="206">report</text>
  <text class="soft" x="414" y="234">31 Mar · Kitchen · €47</text>
  <text class="soft" x="414" y="258">sum(amount) group by day, category</text>
  <text class="soft" x="414" y="282">one join per dimension</text>
  <path class="ln" d="M360 80 H398" marker-end="url(#a)"/><path class="ln" d="M575 140 V160 H185 V178" marker-end="url(#a)"/><path class="ln" d="M360 240 H398" marker-end="url(#a)"/>
'''
mechanism = '''
<p>The CDC note ends with a stream of change events. The star schema note starts with a clean fact table. Between them sit two layers that the notes skip, and most of the hard work happens there.</p>
''' + fig(760, 310, "Order line 51, the two mugs of order 9001, in each layer. The raw layer holds both change events: created with quantity 2 and 16 euros at log position 1000, updated to quantity 1 and 8 euros at position 5200. Staging holds only the latest version. The fact table holds one row for the line with its date, product, customer and store keys, quantity 1 and 8 euros. The report sums it with the kettle into 47 euros for Kitchen on 31 March.",
          layers_svg, "One line of order 9001 in every layer. Raw remembers everything; each layer after it forgets on purpose.") + '''
<h3>What each layer promises</h3>
''' + tbl(["Layer", "Holds", "Promise", "Rebuilt from"], [
    ["<b>raw</b>", "every change event exactly as received, plus load metadata", "never edited, never deleted (until retention)", "the source, by a new snapshot"],
    ["<b>staging</b>", "one row per source key: the latest version, typed and renamed, deletes flagged", "matches the source as of the last log position read", "raw, at any time"],
    ["<b>marts</b>", "facts at a stated grain, dimensions with surrogate keys", "business meaning: one definition of revenue", "staging, at any time"],
    ["<b>report</b>", "queries, extracts and dashboards", "reads marts only", "nothing to rebuild"],
]) + mn("“Medallion” (bronze, silver, gold) is the same three layers under other names.") + '''
<p>The key line is the last column. Because raw is kept, every later layer can be thrown away and rebuilt. That is what makes it safe to fix a bug in the revenue definition: change the SQL, rebuild the marts, and last year is corrected too. Without raw, the only copy of last year is the wrong one.</p>
''' + full('''<h3>ETL or ELT</h3>
<p>In classic <b>ETL</b> a separate tool transformed the data before it reached the warehouse, and only the result was stored. In <b>ELT</b> the raw data is loaded first and transformed inside the warehouse with SQL, usually by dbt. ELT won for one reason: warehouses got cheap and fast enough to keep raw data and rerun the transforms. This pipeline is ELT. The extract step does no business logic at all; it copies.</p>
<h3>Staging: from events to rows</h3>
<p>Staging turns a pile of change events into the table as it is now. For each key, keep the event with the highest log position, and flag the key if that event is a delete, so the next layer can remove it too:</p>
''' + code("stg_order_lines.sql", "latest version per key", '''
SELECT *, op = 'd' AS is_deleted
FROM (
  SELECT coalesce(after, before).*, op, lsn,
         ROW_NUMBER() OVER (PARTITION BY coalesce(after, before).id ORDER BY lsn DESC) AS rn
  FROM raw.order_lines_changes
) latest
WHERE rn = 1;
''') + '''<p>Order by log position, never by the time the event arrived. Events can arrive out of order after a connector restart or a retry; the log position is the order the database committed them in.</p>
<h3>Marts: from rows to facts</h3>
<p>The fact table’s grain is one order line, as the star schema note recommends. Each fact row looks up its dimension keys: the date from <code>placed_at</code>, the product version, the customer and the store. Two details matter more than they look:</p>
<ul>
<li><b>The date is the shop’s local date.</b> Order 9001 was placed at 23:58 in Amsterdam, which is 21:58 UTC. An order at 00:30 on 1 April Amsterdam time is 22:30 UTC on 31 March. Finance closes months in local time, so the date key is computed in local time, once, in the pipeline, not in every report.</li>
<li><b>Amounts are stored, not recomputed.</b> The line total comes from the source as it was charged. Recomputing <code>qty × current price</code> in the warehouse gives a different answer the day prices change.</li>
</ul>''')

# ------------------------------------------------------------------ 3 drills
wm_svg = '''
  <path class="ln" d="M20 150 H740" marker-end="url(#a)"/><text class="soft" x="740" y="176" text-anchor="end">wall clock →</text>
  <path class="ln-d" d="M300 40 V200"/><text class="soft" x="300" y="222" text-anchor="middle">00:00:30 extract runs</text>
  <rect class="bx" x="40" y="70" width="200" height="50" rx="8"/><text class="lbl" x="140" y="92" text-anchor="middle">9001 written</text><text class="soft" x="140" y="112" text-anchor="middle">updated_at 23:58:10</text>
  <rect class="bx-r" x="420" y="70" width="200" height="50" rx="8"/><text class="lbl" x="520" y="92" text-anchor="middle">9001 commits</text><text class="soft" x="520" y="112" text-anchor="middle">00:00:40, still 23:58:10</text>
  <text class="soft" x="300" y="30" text-anchor="middle">watermark saved: 23:59:58</text>
  <path class="ln-r" d="M520 124 V140"/><text class="bad" x="520" y="200" text-anchor="middle" font-size="16">next run asks “after 23:59:58”: never seen</text>
'''
scd_svg = '''
  <path class="ln" d="M20 170 H740" marker-end="url(#a)"/>
  <text class="soft" x="60" y="196" text-anchor="middle">31 Mar</text><text class="soft" x="400" y="196" text-anchor="middle">12 May</text><text class="soft" x="700" y="196" text-anchor="middle">today</text>
  <rect class="bx-g" x="40" y="40" width="356" height="56" rx="8"/><text class="lbl" x="218" y="64" text-anchor="middle">product_key 812 · Kitchen</text><text class="soft" x="218" y="86" text-anchor="middle">valid 2025-09-01 → 2026-05-12</text>
  <rect class="bx-y" x="404" y="40" width="336" height="56" rx="8"/><text class="lbl" x="572" y="64" text-anchor="middle">product_key 977 · Small appliances</text><text class="soft" x="572" y="86" text-anchor="middle">valid 2026-05-12 → (current)</text>
  <circle cx="60" cy="140" r="7" class="bx-r"/><text class="soft" x="76" y="146">fact for order 9001 points at 812</text>
  <path class="ln-d" d="M400 30 V170"/>
'''
drills = mn("Each drill is a real way to get a wrong number. Guess the cause before you read it.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · after midnight</a></li><li><a href="#drill-2">2 · counted twice</a></li><li><a href="#drill-3">3 · renamed column</a></li>
  <li><a href="#drill-4">4 · deleted, still sold</a></li><li><a href="#drill-5">5 · last year changed</a></li><li><a href="#drill-6">6 · early fact</a></li>
</ul>
''' + drill(1, "The order that committed after midnight", [
    ("Timeline", "The extract reads <code>WHERE updated_at &gt; :watermark</code> and saves the largest <code>updated_at</code> it saw. Order 9001 is written at 23:58:10 but its payment step keeps the transaction open, and it commits at 00:00:40. The 00:00:30 run could not see it and saved a watermark of 23:59:58. The next run asks for rows after 23:59:58. Order 9001 is never loaded."),
    ("Tempting mistake", "“Use the database clock at commit time.” There is no column for that, and <code>now()</code> inside a transaction returns its start time, which is exactly the problem.", True),
    ("Why", "A timestamp is set when the row is written; the row becomes visible when the transaction commits. Any transaction that is open while the extract runs can commit later with an older timestamp. Long transactions, replicas that lag and clocks on several app servers all widen the gap.", True),
    ("What saves you", "Either read the log (CDC), which is ordered by commit, or re-read a safety window: <code>updated_at &gt; :watermark − 10 minutes</code>, and make the load idempotent (drill 2) so the overlap does no harm. Set the window longer than the longest transaction you allow, and enforce that with <code>idle_in_<wbr>transaction_<wbr>session_<wbr>timeout</code>."),
], "a timestamp watermark misses late commits. Overlap the window and make the load idempotent, or read the log.") + fig(760, 236, "Timeline of drill 1. Order 9001 is written with updated_at 23:58:10. The extract runs at 00:00:30 and saves a watermark of 23:59:58. Order 9001 commits at 00:00:40, still with updated_at 23:58:10. The next run asks for rows changed after 23:59:58 and never sees it.",
                  wm_svg, "Written before the watermark, visible after it: invisible to a timestamp extract.") + drill(2, "March counted twice", [
    ("Timeline", "On 1 April the load for 31 March fails halfway. The on-call engineer reruns it. The load appends rows. Half of 31 March is now in the fact table twice, and the dashboard shows the best day of the year."),
    ("Why", "Appending is not idempotent: running it twice gives a different result from running it once. Every pipeline is rerun eventually: after a failure, a fix, a backfill or a retry by the scheduler.", True),
    ("What saves you", "Make every load safe to repeat. Either replace the whole slice (<code>DELETE</code> the day, then <code>INSERT</code> it, in one transaction, or overwrite the partition), or <code>MERGE</code> on the line’s key so a second run updates the same rows. Add a uniqueness test on the fact key that fails the run (chapter 7)."),
], "every load must give the same result when run twice. Replace a slice or merge on a key; never blindly append.") + drill(3, "The column that was renamed on a Tuesday", [
    ("Timeline", "The app team renames <code>line_total</code> to <code>amount_gross</code> in a normal release. CDC carries the new field. Staging still selects <code>line_total</code>, which is now always NULL. Revenue is €0 for every new line. Nobody notices until the weekly finance meeting."),
    ("Why", "The pipeline depends on the app’s table layout, but nobody told the app team it was a contract. The warehouse accepted NULLs without complaint because nothing said they were wrong.", True),
    ("What saves you", "Fail loudly: a <code>not_null</code> test on the amount and a volume check (“revenue today is 0 % of the usual”) stop the run before the marts publish. Then fix the cause: a schema check in the app’s CI that knows which columns the warehouse reads, or, better, a published contract or outbox event instead of raw tables (the CDC note’s going-deeper chapter)."),
], "silent NULLs are worse than a failed run. Test what the report depends on, and make the source schema a contract.") + drill(4, "The cancelled order still in revenue", [
    ("Timeline", "Fraud cancels order 9733, and a clean-up job hard-deletes its lines. The timestamp extract looks for changed rows; a deleted row has no row left to change. The warehouse keeps the €310 sale forever."),
    ("Why", "Incremental extracts by timestamp only see rows that exist. Deletes leave nothing behind to select.", True),
    ("What saves you", "CDC sees deletes as events (<code>op = d</code>), and staging drops the key. Without CDC: ask the app team for soft deletes on tables the warehouse reads, or run a periodic key comparison (all ids in the source against all ids in staging) and delete the missing ones. A nightly reconciliation of order counts and totals per day (chapter 8) catches what both miss."),
], "an extract that cannot see deletes will slowly overstate. Read deletes from the log, or reconcile keys.") + drill(5, "Last year’s revenue changed overnight", [
    ("Timeline", "On 12 May the kettle moves from <i>Kitchen</i> to <i>Small appliances</i>. The product dimension is a copy of the current product table, so it overwrites the category. The March report, closed and filed, now shows €39 less for Kitchen and €39 more for Small appliances."),
    ("Why", "Overwriting a dimension (type 1) rewrites history: every old fact now joins to today’s label. Sometimes that is what you want (a typo fix). For a category used in filed reports it is not.", True),
    ("What saves you", "Keep history in the dimension (type 2): close the old row and add a new one with a new surrogate key and valid dates. Facts keep the key they were loaded with, so March still joins to <i>Kitchen</i>. Decide per column: typos are type 1, categories and regions are type 2. If someone wants old sales under the new category, that is a different question with its own join (“current category”), not a silent change."),
], "a dimension that overwrites changes the past. Version the columns that reports group by.") + fig(760, 230, "Drill 5 as a timeline. Product 812, the kettle in Kitchen, is valid from September 2025 until 12 May 2026. A new version, product key 977 in Small appliances, is valid from 12 May. The fact row for order 9001, sold on 31 March, keeps pointing at key 812, so March still reports it under Kitchen.",
                  scd_svg, "Two versions of one kettle. The fact keeps the key it was sold under.") + drill(6, "The fact that arrived before its customer", [
    ("Timeline", "Customer 77 signed up one minute before ordering. Orders come from the app by CDC every 15 minutes; customers come from the CRM in a nightly batch. The 00:15 fact load joins order 9001 to <code>dim_customer</code>, finds no row for customer 77, and the inner join drops both lines. €55 is missing until someone reloads the day by hand."),
    ("Why", "Facts and dimensions come from different sources on different schedules. An inner join treats “not loaded yet” as “does not exist”.", True),
    ("What saves you", "Never drop a fact for a missing dimension. Either point it at an <b>unknown member</b> (key −1, “not yet known”) and re-key it when the dimension arrives, or insert an <b>inferred member</b>: a placeholder row for customer 77 that the nightly load fills in. Monitor the share of facts pointing at unknown members; above a few percent, a source is late."),
], "an inner join between sources on different schedules loses data. Facts always load; missing dimensions get a placeholder.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["read the log, or overlap the watermark window", "1"],
    ["every load is idempotent: replace a slice or merge on a key", "2"],
    ["tests on what reports depend on fail the run; the source schema is a contract", "3"],
    ["deletes are read from the log or found by reconciling keys", "4"],
    ["dimensions version the columns reports group by", "5"],
    ["facts never wait for dimensions; unknown and inferred members", "6"],
]))

# ------------------------------------------------------------------ 4 the hard problem
hard = '''
<p>Five of the six drills come down to one property. A correct pipeline is one where <b>running any part of it again, for any period, gives the right answer</b>. Reruns after failures, backfills after bug fixes, replays after a source outage and duplicate events from a connector restart are then all the same, boring operation. Everything in this chapter serves that one promise.</p>
<h3>Three clocks</h3>
''' + tbl(["Clock", "Order 9001", "Used for"], [
    ["<b>event time</b>: when it happened in the business", "31 Mar 23:58 (placed_at)", "which day the sale belongs to"],
    ["<b>commit order</b>: when the database made it visible", "log position 1000, then 5200 for the return", "which version of a row is the latest"],
    ["<b>load time</b>: when the warehouse got it", "1 Apr 00:15, then 3 Apr 10:30", "freshness, debugging, nothing else"],
], hot=(0,)) + mn("Mixing up event time and load time is the single most common warehouse bug. It looks fine until the first late event.") + '''
<p>Every decision uses the right clock. The fact row’s date comes from event time. Which version wins comes from commit order. Load time is recorded but never decides anything. The return on 3 April changes a fact for 31 March: an update to a day that is already loaded. A pipeline that only processes “today’s” rows by load time will put the €8 return on 3 April’s report or not at all.</p>
''' + full('''<h3>Four ways to load, compared</h3>
''' + tbl(["Load method", "Idempotent?", "Handles late updates", "Cost", "Use for"], [
    ["<b>append</b>", "no", "no", "cheapest", "raw layer only, where duplicates are expected and deduped later"],
    ["<b>replace a slice</b> (delete + insert a day, or overwrite a partition)", "yes, per slice", "if you reload the affected slices", "rewrites whole slices", "facts by event date, when you know which days changed"],
    ["<b>MERGE on key</b>, newer only", "yes", "yes, any day", "reads the target to match keys", "facts and staging fed by CDC"],
    ["<b>full rebuild</b>", "yes", "yes", "rereads everything", "small tables, dimensions, and the fix after a logic change"],
]) + '''<p>The pipeline uses three of them: append into raw, MERGE from raw into staging and facts, and full rebuilds for small dimensions and after logic changes.</p>
<h3>The merge, written properly</h3>
''' + code("fact_sales_merge.sql", "idempotent and order-safe", '''
MERGE INTO mart.fact_sales AS t
USING (
  SELECT * FROM stg.order_lines_enriched
  WHERE lsn > :last_merged_lsn          -- only what changed since the last run
) AS s
ON t.order_line_id = s.order_line_id
WHEN MATCHED AND s.lsn > t.source_lsn AND s.is_deleted THEN DELETE
WHEN MATCHED AND s.lsn > t.source_lsn THEN   -- newer only: replays and old events do nothing
  UPDATE SET qty = s.qty, amount = s.amount, source_lsn = s.lsn,
             product_key = s.product_key, customer_key = s.customer_key
WHEN NOT MATCHED AND NOT s.is_deleted THEN
  INSERT (order_line_id, date_key, product_key, customer_key, store_key, qty, amount, source_lsn)
  VALUES (s.order_line_id, s.date_key, s.product_key, s.customer_key, s.store_key, s.qty, s.amount, s.lsn);
''') + '''<p>Three details make it safe. The key is the source’s line id, so a second run matches the same rows. The guard <code>s.lsn &gt; t.source_lsn</code> means an older event arriving late, or the same event twice, changes nothing: it is the upsert note’s “skip if older” clause. And <code>:last_merged_lsn</code> is only advanced after the merge commits, so a crash halfway means the next run repeats the batch, which the first two details make harmless.</p>
<h3>No hidden clocks in the transforms</h3>
<p>A transform that calls <code>now()</code> or <code>current_date</code> gives a different answer on every run, so it cannot be rerun for last Tuesday. Pass the period being processed in as a parameter (the scheduler’s logical date) and use only that. Then a backfill is simply the normal job, run for old dates:</p>
''' + code("backfill.sh", "the same job, for a past range", '''
# rebuild March after fixing the revenue definition
dbt build --select fact_sales+ --vars '{"from": "2026-03-01", "to": "2026-04-01"}'
''', plain=True) + '''<p>If the backfill needs a different script from the daily run, the daily run is not idempotent yet.</p>''')

# ------------------------------------------------------------------ 5 variants
variants = '''
<p>There are three common ways to get order lines out of the app database. Here is each one, with the drills from chapter 3 run against it.</p>
''' + tbl(["", "A · nightly full copy", "B · incremental by timestamp", "C · CDC into raw, merge every 15 min"], [
    ["how", "dump <code>order_lines</code> and replace the warehouse copy", "select rows with <code>updated_at</code> past a watermark, merge them", "a connector reads the log into raw; a job merges raw into staging and facts"],
    ["load on the source", "a full scan every night", "an index range scan on <code>updated_at</code>", "reads the log; almost none on tables"],
    ["freshness", "up to 24 hours", "the schedule, often hourly", "about 15–20 minutes"],
    ["drill 1, late commits", "<b>safe</b>: everything is reread", "<b>misses them</b> unless the window overlaps", "<b>safe</b>: the log is in commit order"],
    ["drill 2, rerun", "<b>safe</b>: replace is idempotent", "safe only with MERGE", "safe with the newer-only MERGE"],
    ["drill 4, deletes", "<b>safe</b>: gone rows are gone", "<b>blind</b> to hard deletes", "<b>safe</b>: delete events"],
    ["history of changes", "none: only last night’s state", "only the versions it happened to see", "every version, in raw"],
    ["needs from the app team", "read access", "an indexed, trusted <code>updated_at</code> on every table", "logical replication, a slot, a schema contract"],
    ["breaks when", "the table grows past the night", "someone updates without touching <code>updated_at</code>", "the connector stops and the slot fills the disk"],
], hot=(3, 5)) + mn("Variant A is underrated. For tables under a few million rows it is correct by construction, and easy to explain.") + '''
<p class="full">Variant B is the one most teams start with and the one with the most silent failures: a bulk <code>UPDATE</code> from a script that does not set <code>updated_at</code>, a hard delete, a long transaction. Every one of them produces a number that looks plausible. Variant C costs more to run, but its failures are loud: the connector stops, lag grows, an alert fires.</p>
<h3>Choosing per table</h3>
''' + tbl(["Table", "Rows", "Changes", "Pick"], [
    ["<code>stores</code>", "30", "a few a year", "A: full copy, type 2 dimension built in the warehouse"],
    ["<code>products</code>", "40,000", "hundreds a day", "A nightly, or C if prices must be fresh"],
    ["<code>customers</code> (from the CRM)", "2 million", "thousands a day, no log access", "B with an overlap window, plus a weekly key reconciliation"],
    ["<code>orders</code>, <code>order_lines</code>", "60 million lines", "100,000 a day, updates and deletes", "C"],
]) + full('''<p>Mixing variants is normal and is not a compromise. What must be consistent is the layer contract from chapter 2: whichever way data arrives, staging holds the latest row per key and marts are rebuilt from staging. The facts and dimensions do not care how the rows got there.</p>
<h3>Where the transform runs</h3>
<p>All three variants load into raw and transform in the warehouse (ELT). The older alternative, a tool that transforms in flight and loads only the result, still makes sense in one case: data that must be masked or dropped before it may be stored at all, such as card numbers or health data. Then the extract step removes those fields and nothing else, so it stays a copy with redactions, not a second place where business logic lives.</p>''')

# ------------------------------------------------------------------ 6 numbers
numbers = '''
<p>The shop takes about 40,000 orders a day at 2.5 lines each: 100,000 new lines a day, plus about 8,000 updates from returns and status changes. Five years of history is 60 million lines.</p>
<h3>How much moves</h3>
''' + tbl(["Variant", "Data moved per day", "Source work", "Worked out"], [
    ["A · full copy of order lines", "about 25 GB", "a 60-million-row scan nightly", "60 M rows × ~400 bytes"],
    ["B · incremental", "about 45 MB", "one index range scan per run", "108,000 rows × ~400 bytes"],
    ["C · CDC", "about 90 MB", "reading the log, which is written anyway", "108,000 events × ~800 bytes (before and after)"],
]) + mn("CDC moves more bytes than B, because each event carries before and after. It still does far less work on the source.") + '''
<h3>How fresh</h3>
<p>With CDC the connector delivers events within seconds. The merge runs every 15 minutes and takes about 3. The worst case for a sale to appear in the report is one full interval plus the run: about 18 minutes, and about 10 on average. Halving the interval halves the average but doubles the number of merges, each of which reads part of the fact table.</p>
''' + full('''<h3>What a merge costs</h3>
<p>A MERGE has to find the matching target rows. If the fact table is partitioned by event date, and the batch only touches recent days, the warehouse reads only those partitions. Returns make that harder: they update facts weeks old.</p>
''' + tbl(["Batch touches", "Partitions read", "Data scanned per merge"], [
    ["only today", "1", "~40 MB"],
    ["the last 30 days (returns)", "30", "~1.2 GB"],
    ["no date filter in the merge", "all 1,800", "~70 GB, 96 times a day"],
], hot=(2,)) + '''<p>The last row is a real bill: a merge without a partition filter can cost more than the rest of the warehouse together. Add the affected dates to the merge condition (<code>AND t.date_key IN (dates in this batch)</code>) so the warehouse can prune.</p>
<h3>The slot on the source</h3>
<p>The source writes about 20 GB of write-ahead log a day. If the connector stops, PostgreSQL keeps all of it for the slot: a weekend is 60 GB, the disk from the CDC note’s drill. Cap it with <code>max_slot_wal_keep_size</code> (say 100 GB) and alert when lag passes 30 minutes. If the cap is hit, the slot is lost and the connector needs a new snapshot, which is slow but recoverable, because raw and the merge are idempotent.</p>
<h3>A backfill, timed</h3>
<p>After a fix to the revenue definition, a year of facts must be rebuilt. One day of facts rebuilds in about 4 minutes. Serially, 365 days take about 24 hours; eight days in parallel take about 3. Plan backfills against the warehouse’s concurrency limit and run them outside the merge schedule, or the daily merges queue behind them and freshness drops for the day.</p>''')

# ------------------------------------------------------------------ 7 testing
testing = '''
<p>Pipeline bugs rarely crash. They produce a number that is wrong by a few percent, and the first person to notice is in finance. Tests therefore check data as well as code, and they run on every load, not only in CI.</p>
''' + tbl(["Test", "Checks", "Runs", "Catches"], [
    ["<b>unit tests on transforms</b>", "fixed input rows give the expected output rows", "CI", "logic bugs: the return, the time zone, the unknown customer"],
    ["<b>the rerun test</b>", "loading a batch twice gives the same table as loading it once", "CI", "drill 2"],
    ["<b>schema tests</b>", "keys are unique and not null, foreign keys resolve", "every load", "duplicates, missing dimensions"],
    ["<b>volume and range checks</b>", "row count and revenue within the usual band for the weekday", "every load", "drill 3, half-loaded days"],
    ["<b>reconciliation</b>", "counts and sums per day match the source", "nightly", "drills 1 and 4, everything else"],
    ["<b>source contract check</b>", "the columns the warehouse reads still exist with the same types", "the app’s CI", "drill 3, before it ships"],
], hot=(4,)) + mn("If you can only afford one test, make it the reconciliation. It checks the outcome, so it catches causes you never thought of.") + full('''<h3>A unit test for order 9001</h3>
<p>Write the drills as fixtures. The return on 3 April is a perfect case: it must change the fact for 31 March, not add one for 3 April.</p>
''' + code("test_fact_sales.yml", "dbt unit test", '''
unit_tests:
  - name: return_updates_the_original_day
    model: fact_sales
    given:
      - input: ref('stg_order_lines_enriched')
        rows:
          - {order_line_id: 51, date_key: 20260331, qty: 2, amount: 16, lsn: 1000}
          - {order_line_id: 51, date_key: 20260331, qty: 1, amount: 8,  lsn: 5200}
    expect:
      rows:
        - {order_line_id: 51, date_key: 20260331, qty: 1, amount: 8}
''', plain=True) + '''<h3>Reconciliation, the test that checks the outcome</h3>
<p>Every night, compute the same small summary on both sides and compare: per event date, the number of order lines and the sum of their amounts. Run it on the source’s read replica, for the last 60 days, so late returns are included.</p>
''' + code("reconcile.sql", "same query on both sides, then compare", '''
SELECT date(placed_at AT TIME ZONE 'Europe/Amsterdam') AS day,
       count(*)              AS lines,
       sum(line_total)       AS revenue
FROM order_lines JOIN orders USING (order_id)
WHERE placed_at >= now() - interval '60 days'
GROUP BY 1;
''') + '''<p>Expect small, explainable differences for the last hour (in flight) and none for older days. A difference on an old day is a bug every time: a missed late commit, a delete that never arrived, a duplicated reload.</p>
<h3>Write, audit, publish</h3>
<p>Data tests are only useful if a failing one stops bad data reaching the report. Build each run’s marts in a hidden schema, run the tests there, and swap them in only when they pass. If they fail, finance sees yesterday’s correct numbers with a “data as of” note, rather than today’s wrong ones.</p>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>A pipeline that runs every 15 minutes needs three numbers on a dashboard, each with an alert, and a short runbook for the five things that go wrong.</p>
''' + tbl(["Metric", "What it means", "Alert when"], [
    ["<b>freshness</b>: now minus the newest event time in the marts", "how old the report is", "over 45 minutes in opening hours"],
    ["<b>completeness</b>: the reconciliation difference per day", "whether the numbers are right", "any day older than one hour differs"],
    ["<b>unknown-member share</b>: facts with a −1 key", "whether a source is late", "over 2 % of yesterday’s facts"],
]) + mn("Freshness is measured on the data, not on the job. A job that succeeds while loading nothing is the classic false green.") + full('''<p>Behind those three, the engineering view: connector lag and slot size on the source, run duration and rows per run, and tests failed per run. Show “data as of 10:42” on the finance dashboard itself, from the freshness metric, so users can see when it is stale without asking.</p>
<h3>The runbook</h3>
''' + tbl(["Symptom", "First check", "Repair"], [
    ["freshness alert", "is the connector running? is the merge job failing?", "restart the connector; it resumes from its saved log position. Fix the job and let the next run catch up"],
    ["one old day differs in reconciliation", "compare keys for that day: missing in warehouse, or extra?", "missing: replay that day from raw. Extra: check for a delete that was never read"],
    ["slot near its size cap", "connector lag and errors", "fix the consumer first; if the slot is dropped, take a new incremental snapshot"],
    ["a wrong definition found (e.g. revenue included tax)", "which marts use it, from lineage", "fix the SQL, backfill the affected range (chapter 4), tell finance which reports changed"],
    ["the source schema changed", "the failed test’s column", "map the new column in staging, rerun from raw; nothing upstream is lost"],
]) + '''<h3>Closing a month</h3>
<p>Finance closes March on 5 April, and late events keep coming: a return in May still updates a March fact. Agree a rule with finance and write it down. The usual one: the warehouse is always current, and the filed March report is a <b>snapshot</b> taken at close (a copy of the month’s summary, stored with the date it was taken). Later changes appear as adjustments in the month they were made, not as edits to a filed month. That is a finance decision, not a technical one, but the pipeline has to support both views.</p>''')

# ------------------------------------------------------------------ 9 tools
tools_ch = '''
<p>Every piece of this pipeline exists as a product. Each does one box or arrow well and leaves the same few decisions to you.</p>
''' + tbl(["Job", "Common tools", "Gives you", "Still yours"], [
    ["read changes from the source", "Debezium (with Kafka Connect), AWS DMS, Fivetran, Airbyte", "snapshot plus log streaming, schema changes as events", "slot monitoring, the size cap, the contract with the app team"],
    ["land raw data", "Kafka plus a sink connector, cloud storage, the warehouse’s streaming ingest", "append-only storage, retention", "how long raw is kept: it decides how far back you can rebuild"],
    ["transform (staging, marts)", "dbt, SQLMesh", "incremental models, MERGE, snapshots (type 2), tests, lineage", "the grain, the keys, the newer-only guard, no hidden clocks"],
    ["schedule and retry", "Airflow, Dagster, Prefect, dbt Cloud", "dependencies, retries, backfills by date, logical dates", "making every task idempotent so retries are safe"],
    ["check data quality", "dbt tests, Great Expectations, Soda, Elementary", "unique, not null, ranges, anomalies, reports", "the reconciliation, and what blocks publishing"],
    ["store and query", "Snowflake, BigQuery, Redshift, ClickHouse, Databricks, DuckDB", "columnar scans, partitions, MERGE", "partition filters in merges, cost per query"],
]) + mn("A managed connector removes the work in the first row, not the decisions in the last column.") + full('''<h3>What the tools map to</h3>
''' + tbl(["Chapter", "Tool feature"], [
    ["2 · layers", "dbt sources (raw), staging models, marts; Debezium topics per table"],
    ["3 · drill 5", "dbt snapshots, which build type 2 dimensions from a source table"],
    ["4 · idempotent merge", "dbt incremental models with <code>unique_key</code> and <code>incremental_predicates</code>"],
    ["4 · no hidden clocks", "Airflow’s data interval, Dagster partitions"],
    ["7 · tests", "dbt unit tests and data tests, contracts on models"],
    ["8 · freshness", "dbt source freshness, Elementary or the scheduler’s data-age sensors"],
]) + '''<p>A small team can run the whole thing on DuckDB or a single PostgreSQL warehouse with dbt and a cron job until volumes justify more. The design (raw kept, idempotent merges, three clocks, reconciliation) is the same at every size; only the boxes get bigger.</p>''')

# ------------------------------------------------------------------ 10 lab + checklist
lab = '''
<p><b>The lab.</b> The shop starts selling gift cards. A card is bought (an order line, as now), then spent across several later orders, and may expire unspent after two years. Card balances live in a new <code>gift_cards</code> table that the app updates on every purchase and spend. Finance wants two reports: gift card sales by day, and the total outstanding balance at the end of each day. Design the pipeline before you open the answers.</p>
<ol>
<li>What is the grain of each report, and is it a new fact table?</li>
<li>Which extract variant for <code>gift_cards</code>, and why?</li>
<li>How do you get the balance at the end of 31 March, if you load on 2 April?</li>
<li>A card is spent in a shop whose till uploads its sales a day late. What breaks, and what saves you?</li>
<li>How do you prove the balance report is right?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The grain</summary><p>Card sales are order lines and already land in <code>fact_sales</code> with a product of type gift card. The balance is different: one row per card per day, a <b>periodic snapshot</b> fact (<code>fact_gift_card_daily</code>). Do not try to read balances out of transaction facts at query time; store the end-of-day state.</p></details>
<details><summary>2 · Extract</summary><p>CDC (variant C). Balances change on every spend, and you need every version to rebuild a past day’s balance. A nightly copy would only give the balance at copy time.</p></details>
<details><summary>3 · Balance at the end of 31 March</summary><p>From raw: for each card, the latest change event whose event time is on or before 31 March 23:59:59 local time. Because raw keeps every version, the snapshot for any day can be built, or rebuilt, at any time, which also makes the job idempotent.</p></details>
<details><summary>4 · The late till</summary><p>The spend has an event time of yesterday but arrives today, so yesterday’s balance snapshot was wrong when built. Rebuild snapshots for the days touched by each batch (the event dates in the batch), not just today. Same rule as chapter 4: event time decides the day.</p></details>
<details><summary>5 · Proof</summary><p>Reconcile every night: the sum of balances in the app for “now” equals the latest snapshot plus today’s changes, and for each past day, sales minus spends minus expiries equals the change in total balance. A difference names the day to replay.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Layers", ["Raw keeps every change, append only, with a stated retention", "Staging holds the latest row per key, ordered by log position", "Marts rebuild from staging; reports read marts only", "No business logic in the extract"]),
    ("Extract", ["Each table has a chosen variant and a reason", "Timestamp extracts overlap their window", "Deletes are read from the log or found by reconciling keys", "The slot has a size cap and a lag alert"]),
    ("Loading", ["Every load is idempotent: replace a slice or merge on a key", "Merges are newer-only by log position", "Merges filter on the partitions they touch", "No now() in transforms; the period is a parameter"]),
    ("Modelling", ["The grain of each fact is written down", "Date keys use the business’s time zone", "Columns reports group by are type 2", "Missing dimensions get unknown or inferred members"]),
    ("Trust", ["Keys tested unique and not null on every load", "Volume checks stop a bad run before publishing", "Nightly reconciliation of counts and sums per day", "The source schema is checked in the app’s CI"]),
    ("Operations", ["Freshness measured on data and shown on the dashboard", "Runbook for replay, backfill and re-snapshot", "Month-close rule agreed with finance"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="app-db-to-warehouse", no=12, title="From App Database to Warehouse",
    sub="One order followed from checkout to the finance report: extract, raw, staging and marts, and why the number is right after a rerun, a late commit, a return and a renamed column.",
    summary="A deep dive on getting data from an app database into a warehouse: raw, staging and marts, six failure drills, idempotent loads and the three clocks, full copy vs timestamp vs CDC, the numbers, testing and reconciliation, running it, tools, a lab and a checklist.",
    builds_on="Vol. 3, notes 11, 15 and 16",
    builds_on_links=[("Change Data Capture", "../../data/notes/change-data-capture.html"), ("Star Schema", "../../data/notes/star-schema.html"),
                     ("Upserts", "../../data/notes/upserts.html")],
    notes=[("data", "change-data-capture"), ("data", "star-schema"), ("data", "upserts"),
           ("pipelines", "incremental-extract"), ("pipelines", "idempotent-loads"), ("pipelines", "layered-zones")],
    facts=[("Example", "order 9001: €55 at 23:58 on 31 March, one mug returned on 3 April")],
    blurb="Raw, staging and marts, six ways to get a wrong number, idempotent loads, three extract variants and reconciliation.",
    chapters=[
        dict(id="recap", nav="Recap", title="Three notes in sixty seconds",
             gist="Change data capture copies every committed change out of the app database, upserts make loading safe to repeat, and a star schema shapes the result for reports. This deep dive follows one order through the pipeline that joins them, and through everything that later happens to it.",
             body=recap),
        dict(id="layers", nav="The layers", title="The real mechanism: raw, staging, marts",
             gist="Raw keeps every change event, untouched. Staging keeps the latest row per key, ordered by log position. Marts hold facts at a stated grain and versioned dimensions. Because raw is kept, every later layer can be thrown away and rebuilt, which is what makes fixes and backfills safe.",
             body=mechanism,
             check=[("Why order staging by log position rather than by arrival time?", "Events can arrive out of order after retries or restarts; the log position is the order the database committed them in."),
                    ("Why compute the date key in local time in the pipeline?", "Finance closes days and months in local time. Doing it once in the pipeline means every report agrees.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways to get a wrong number: a late commit hidden behind a timestamp watermark, a rerun that doubles a day, a renamed column that loads NULLs, a hard delete the extract cannot see, a dimension overwrite that changes last year, and a fact dropped because its customer had not arrived yet.",
             body=drills,
             check=[("A timestamp extract misses a few orders near midnight. Likely cause and fix?", "Transactions that commit after the run with an older updated_at. Overlap the window and make the load idempotent, or switch to CDC."),
                    ("Why point a fact at an unknown member instead of waiting for the dimension?", "An inner join drops the fact silently. A placeholder keeps the revenue and can be re-keyed when the dimension arrives.")]),
        dict(id="rerun", nav="Rerun anything", title="The hard problem: rerun anything",
             gist="A correct pipeline gives the right answer when any part is run again for any period. Use three clocks for three jobs: event time decides the day, commit order decides the version, load time decides nothing. Load with newer-only merges on the source key, and keep hidden clocks out of the transforms.",
             body=hard,
             check=[("The same change event is merged twice. What stops it doing harm?", "The merge matches on the source key and only updates when the event’s log position is newer than the stored one."),
                    ("Why is now() in a transform a problem?", "The transform gives a different answer each run, so it cannot be rerun or backfilled for a past period.")]),
        dict(id="variants", nav="Variants", title="Full copy, timestamp or CDC",
             gist="A nightly full copy is simple and correct but slow and heavy. Incremental by timestamp is light but misses late commits and deletes. CDC into raw with frequent merges is fresh and sees everything, at the cost of a connector and a slot to run. Choose per table; keep the layer contract the same.",
             body=variants,
             check=[("Which variant is blind to hard deletes?", "Incremental by timestamp: a deleted row leaves nothing to select."),
                    ("When is a nightly full copy the right answer?", "For small tables that change rarely, such as stores or products: it is correct by construction.")]),
        dict(id="numbers", nav="Numbers", title="The pipeline in numbers",
             gist="100,000 new lines and 8,000 updates a day: 25 GB for a full copy, tens of megabytes incrementally. CDC with a 15-minute merge gives a report about 10 minutes old on average. A merge without a partition filter scans the whole fact table each run. A year’s backfill takes a day serially, three hours in parallel.",
             body=numbers,
             check=[("Why does CDC move more bytes than a timestamp extract?", "Each change event carries the row before and after the change."),
                    ("How do you stop a merge from scanning the whole fact table?", "Add the event dates touched by the batch to the merge condition so the warehouse reads only those partitions.")]),
        dict(id="testing", nav="Testing", title="Testing data, not just code",
             gist="Unit test the transforms with the drills as fixtures, test that a rerun changes nothing, check keys, volumes and ranges on every load, and reconcile counts and sums per day against the source every night. Build into a hidden schema and publish only when the tests pass.",
             body=testing,
             check=[("Which single test catches the most causes, and why?", "The nightly reconciliation of counts and sums per day: it checks the outcome, whatever the cause."),
                    ("What does write–audit–publish protect finance from?", "Seeing a wrong number: a failed test keeps yesterday’s correct marts in place.")]),
        dict(id="running", nav="Running it", title="Running it",
             gist="Watch freshness measured on the data, the reconciliation difference per day and the share of facts with unknown members. Keep a runbook for restarting the connector, replaying a day from raw, re-snapshotting and backfilling. Agree with finance how a closed month handles late changes.",
             body=running,
             check=[("Why measure freshness on the data rather than the job?", "A job can succeed while loading nothing; only the newest event time shows how old the report really is."),
                    ("A return in May changes a March sale. What does the filed March report show?", "Usually the snapshot taken at close; the change appears as an adjustment in May. Agree the rule with finance.")]),
        dict(id="tools", nav="Tools", title="Tools",
             gist="Debezium or a managed connector reads the log, Kafka or storage lands raw data, dbt builds staging and marts with incremental merges, snapshots and tests, a scheduler handles dependencies and backfills, and a columnar warehouse stores it. The grain, the keys and idempotency stay your job.",
             body=tools_ch),
        dict(id="lab", nav="Lab", title="A lab and the checklist",
             gist="The lab adds gift cards: card sales fit the existing fact table, but outstanding balances need a periodic snapshot fact rebuilt from raw, with late till uploads handled by event time. The checklist turns the deep dive into review questions for any pipeline.",
             body=lab),
    ],
    sources="Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i> (3rd ed.): grain, slowly changing dimensions, late-arriving dimensions and inferred members. Maxime Beauchemin, “Functional Data Engineering” (idempotent, deterministic tasks). Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, chapters 10–11. The Debezium, dbt (incremental models, snapshots, unit tests) and PostgreSQL logical replication documentation. Joe Reis and Matt Housley, <i>Fundamentals of Data Engineering</i>.",
)
