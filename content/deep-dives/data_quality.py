# Deep dive 15 · Data Quality & Pipeline Observability. Builds on Vol. 9 notes 11 (write–audit–publish),
# 12 (data contracts), 13 (quality checks & quarantine) and 14 (DAG orchestration & lineage).
# Example: the homeware shop's sales pipeline during week 23, when five things go wrong in five days and only one is
# caught before the finance dashboard. The dive follows those five incidents to a pipeline that catches all of them.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
week_svg = '''
  <path class="ln" d="M20 160 H740" marker-end="url(#a)"/>
  <text class="soft" x="90" y="186" text-anchor="middle">Mon</text><text class="soft" x="230" y="186" text-anchor="middle">Tue</text>
  <text class="soft" x="370" y="186" text-anchor="middle">Wed</text><text class="soft" x="510" y="186" text-anchor="middle">Thu</text><text class="soft" x="650" y="186" text-anchor="middle">Fri</text>
  <rect class="bx-r" x="30" y="40" width="120" height="90" rx="8"/><text class="lbl" x="90" y="76" text-anchor="middle">empty load</text><text class="soft" x="90" y="100" text-anchor="middle">job green</text>
  <rect class="bx-r" x="170" y="40" width="120" height="90" rx="8"/><text class="lbl" x="230" y="76" text-anchor="middle">duplicates</text><text class="soft" x="230" y="100" text-anchor="middle">after restart</text>
  <rect class="bx-g" x="310" y="40" width="120" height="90" rx="8"/><text class="lbl" x="370" y="76" text-anchor="middle">renamed col</text><text class="soft" x="370" y="100" text-anchor="middle">caught ✓</text>
  <rect class="bx-r" x="450" y="40" width="120" height="90" rx="8"/><text class="lbl" x="510" y="76" text-anchor="middle">prices × 100</text><text class="soft" x="510" y="100" text-anchor="middle">Delft tills</text>
  <rect class="bx-r" x="590" y="40" width="120" height="90" rx="8"/><text class="lbl" x="650" y="76" text-anchor="middle">a shop missing</text><text class="soft" x="650" y="100" text-anchor="middle">total looks fine</text>
  <text class="bad" x="380" y="222" text-anchor="middle" font-size="18">five incidents, one caught before finance saw it</text>
'''
recap = '''
<p>Week 23 at the shop. The pipeline from the dive on app databases and warehouses is running: CDC, raw, staging, marts, a revenue dashboard. It has tests. Five things go wrong in five days, and the tests catch one of them.</p>
''' + tbl(["Note", "In one line"], [
    ["Write–Audit–Publish", "build hidden, test hidden, swap in only if the tests pass"],
    ["Data Contracts", "the producing team agrees the schema and rules, and its CI enforces them"],
    ["Quality Checks &amp; Quarantine", "row checks send bad rows aside; batch checks stop a bad publish"],
    ["DAG Orchestration &amp; Lineage", "run steps when inputs are ready, and know what feeds what"],
]) + fig(760, 240, "Week 23 from Monday to Friday. Monday, an empty load that the scheduler marked green. Tuesday, duplicate rows after a connector restart. Wednesday, a renamed column, which was caught. Thursday, Delft's tills sending prices a hundred times too high. Friday, one shop's sales missing while the total looked normal. Five incidents, one caught before finance saw it.",
         week_svg, "Five incidents in five days. Each passed the tests that existed.") + mn("Every incident here comes from a real category of data failure: freshness, uniqueness, schema, distribution, completeness.") + '''
<p class="full">Each note solves one piece. This dive is about the system they make together: where each kind of check belongs, why most pipelines test the wrong things, how strict to be without drowning in alerts, how to test the tests themselves, and what to do in the hour after a check fires. By the end, all five of week 23's incidents are caught before the dashboard, four of them automatically.</p>
<h3>Why the tests gave false confidence</h3>
<p>The shop had 41 tests and a green CI badge. Every one of them passed during week 23, and every one was correct. They checked that columns weren't null, that statuses were known, that prices were positive: properties of individual rows. None checked whether the data had arrived, whether all of it had arrived, or whether it agreed with the source. A test suite can be thorough and still miss everything that matters, if it measures the wrong dimension.</p>
<h3>Week 23, one line each</h3>
''' + tbl(["Day", "What happened", "Why the tests missed it"], [
    ["Mon", "the partner file arrived empty; the load succeeded with zero rows", "the job was green; nothing checked the data's age"],
    ["Tue", "the CDC connector restarted and replayed an hour of events", "uniqueness was tested on staging, not on the fact"],
    ["Wed", "<code>line_total</code> renamed to <code>amount_gross</code>", "caught: a not-null test failed the run ✓"],
    ["Thu", "Delft's tills sent prices in cents", "the range check allowed up to €10,000"],
    ["Fri", "the Rotterdam shop's upload failed", "the day's total was within ±30 % of normal"],
], hot=(2,))

# ------------------------------------------------------------------ 2 mechanism
layers_svg = '''
  <rect class="bx" x="10" y="80" width="120" height="56" rx="8"/><text class="lbl" x="70" y="113" text-anchor="middle">source</text>
  <rect class="bx-y" x="160" y="80" width="120" height="56" rx="8"/><text class="lbl" x="220" y="113" text-anchor="middle">raw</text>
  <rect class="bx" x="310" y="80" width="120" height="56" rx="8"/><text class="lbl" x="370" y="113" text-anchor="middle">staging</text>
  <rect class="bx-g" x="460" y="80" width="120" height="56" rx="8"/><text class="lbl" x="520" y="113" text-anchor="middle">marts</text>
  <rect class="bx" x="610" y="80" width="130" height="56" rx="8"/><text class="lbl" x="675" y="113" text-anchor="middle">dashboard</text>
  <path class="ln" d="M130 108 H158" marker-end="url(#a)"/><path class="ln" d="M280 108 H308" marker-end="url(#a)"/><path class="ln" d="M430 108 H458" marker-end="url(#a)"/><path class="ln" d="M580 108 H608" marker-end="url(#a)"/>
  <text class="soft" x="70" y="40" text-anchor="middle">1 · contract</text><text class="soft" x="70" y="60" text-anchor="middle">producer CI</text>
  <text class="soft" x="220" y="40" text-anchor="middle">2 · arrival</text><text class="soft" x="220" y="60" text-anchor="middle">schema, volume</text>
  <text class="soft" x="370" y="40" text-anchor="middle">3 · rows</text><text class="soft" x="370" y="60" text-anchor="middle">quarantine</text>
  <text class="soft" x="520" y="40" text-anchor="middle">4 · audit</text><text class="soft" x="520" y="60" text-anchor="middle">before publish</text>
  <text class="soft" x="675" y="40" text-anchor="middle">5 · monitor</text><text class="soft" x="675" y="60" text-anchor="middle">freshness, drift</text>
  <path class="ln-d" d="M20 170 H740"/><text class="soft" x="380" y="196" text-anchor="middle">6 · reconcile with the source, nightly, end to end</text>
'''
mechanism = '''
<p>A check is only useful where it can stop something. The pipeline has six places to check data, and each catches a different kind of failure at a different cost.</p>
''' + fig(760, 210, "Six checkpoints along the pipeline. One, the contract in the producer's continuous integration. Two, on arrival in raw: schema and volume. Three, row checks in staging, with quarantine. Four, the audit before publishing the marts. Five, monitors on what the dashboard reads: freshness and drift. Six, a nightly reconciliation with the source, end to end.",
          layers_svg, "Six checkpoints. The earlier a check runs, the less it costs when it fires.") + '''
<h3>What each checkpoint is for</h3>
''' + tbl(["Checkpoint", "Checks", "On failure", "Week 23"], [
    ["1 · contract (producer CI)", "schema changes against the agreed contract", "the producer's build fails", "Wed, before release"],
    ["2 · arrival (raw)", "file or batch present, row count, schema", "stop the run, alert the source owner", "Mon"],
    ["3 · rows (staging)", "not null, types, accepted values, ranges, foreign keys", "row to quarantine; too many → stop", "Thu, with the right range"],
    ["4 · audit (before publish)", "unique keys, counts and sums by segment, reconciliation of the batch", "don't publish; yesterday stays", "Tue, Fri"],
    ["5 · monitor (after publish)", "freshness, volume and distribution over time", "alert; banner on the dashboard", "Mon, as a backstop"],
    ["6 · reconcile (nightly)", "counts and sums per day against the source", "a named day to replay", "everything else"],
], hot=(3,)) + mn("Checkpoints 1 to 4 prevent. Checkpoints 5 and 6 detect. You need both, because prevention is only as good as your imagination.") + full('''<h3>The five dimensions of data quality</h3>
<p>Every check tests one of five things. Sorting the shop's existing tests this way showed the gap at once: almost all of them tested validity, and none tested completeness or freshness.</p>
''' + tbl(["Dimension", "Question", "Typical check", "Shop's tests before week 23"], [
    ["<b>freshness</b>", "is it recent?", "newest event time vs now", "0"],
    ["<b>volume / completeness</b>", "is it all there?", "row counts by segment vs the usual", "1 (total only)"],
    ["<b>uniqueness</b>", "is anything doubled?", "key unique in every published table", "2 (staging only)"],
    ["<b>validity</b>", "are values allowed?", "not null, types, ranges, accepted values", "37"],
    ["<b>consistency</b>", "does it agree with elsewhere?", "reconciliation, sums across layers", "0"],
], hot=(0, 1, 4)) + '''<p>Validity tests are easy to write, so pipelines collect them. Freshness, completeness and consistency are the ones that catch outages, and they are the ones people forget.</p>
<h3>Where results go</h3>
<p>A check that only prints to a log can't be trended, alerted on consistently or shown on a dashboard. Every check writes one row per run to a results table: the check, the table, the partition, the status, the measured value, the threshold, and the severity. Chapter 6's alert arithmetic, chapter 7's fault tests and chapter 8's health dashboard are all queries on this one table.</p>
''' + code("check_results.sql", "one row per check per run", """
CREATE TABLE check_results (
  run_id text, run_day date, checked_at timestamp,
  check_name text, table_name text, partition_key text,
  dimension text,            -- freshness | volume | uniqueness | validity | consistency
  severity text,             -- block | quarantine | warn
  status text,               -- passed | warned | quarantined | blocked
  measured numeric, threshold_low numeric, threshold_high numeric
);
""") + '''<h3>Checks belong in the DAG</h3>
<p>A check scheduled separately from the pipeline can run before the data it checks, or after users have already seen it. Make checks steps in the same DAG: arrival checks between landing and staging, the audit between building and publishing, so a blocking failure stops everything downstream by itself. Monitors and reconciliation run after the publish step, as their own branch, so their failures alert without holding anything back.</p>''')

# ------------------------------------------------------------------ 3 drills
drills = mn("Each drill is one day of week 23, with the check that would have caught it.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · green and empty</a></li><li><a href="#drill-2">2 · replayed hour</a></li><li><a href="#drill-3">3 · cents</a></li>
  <li><a href="#drill-4">4 · a shop missing</a></li><li><a href="#drill-5">5 · new status</a></li><li><a href="#drill-6">6 · the ignored alert</a></li>
</ul>
''' + drill(1, "Green and empty", [
    ("Timeline", "Monday 05:00 the marketplace partner's file arrives with a header and no rows. The load runs, inserts zero rows, and succeeds. The scheduler shows green. The dashboard shows Sunday's marketplace sales as €0, which looks like a slow Sunday."),
    ("Tempting mistake", "Make the job fail on zero rows. Then a genuine quiet holiday fails it too, and the next time someone adds “allow empty” to make it pass.", True),
    ("Why", "Job status says the code ran without error. It says nothing about the data. An empty or stale input is not an error to the code.", True),
    ("What saves you", "Check the data, not the job: on arrival, compare row count with the same weekday's usual (zero against 3,200 fails); on the dashboard's tables, alert when the newest event is older than its freshness target. Show “data as of” on the dashboard, so users see staleness themselves."),
], "a green job is not fresh data. Monitor the data's age and volume, not the scheduler.") + drill(2, "The hour that happened twice", [
    ("Timeline", "Tuesday the CDC connector restarts after a deploy and replays an hour of order-line events from its last saved position. Staging dedupes them; the fact load appends from a temporary table that didn't. 4,100 lines are doubled in <code>fct_sales</code>. Revenue for Tuesday morning is up 30 %."),
    ("Tempting mistake", "Add a dedupe step to the fact load. Right fix for this load, but the next table built by someone else will have the same gap.", True),
    ("Why", "Uniqueness was tested where it was easiest (staging), not where it matters (every published table). Replays are normal for at-least-once systems.", True),
    ("What saves you", "Make the fact load idempotent (a MERGE on the line id), and test the primary key of <b>every published table</b> in the audit before publish. The unique test on <code>fct_sales.order_line_id</code> stops the publish; yesterday's correct table stays up."),
], "test keys where data is published, not where it is convenient. Replays will happen.") + drill(3, "Prices in cents", [
    ("Timeline", "Thursday a firmware update on Delft's tills sends unit prices in cents. The €39 kettle arrives as 3,900. The range check allows prices up to €10,000 (there's a €4,000 sofa), so every row passes. Delft's revenue for the day is €1.4 million."),
    ("Tempting mistake", "Tighten the range to €2,000. Then the sofa is quarantined every time it sells.", True),
    ("Why", "A range across all products is too wide for any one product. The rows were valid in isolation; the change was in their distribution.", True),
    ("What saves you", "Check against each product's own history: unit price within ±50 % of the product's list price, or a distribution check per shop (median price per line jumping 100× in one shop). Add a batch check on revenue per shop against its usual for the weekday."),
], "valid in isolation isn't right. Compare values with their own history, per product or per shop.") + drill(4, "The shop that wasn't there", [
    ("Timeline", "Friday the Rotterdam shop's till upload fails. The day's total is €640,000 instead of about €690,000: 7 % low, well inside the ±30 % volume band. Nothing fires. Rotterdam's manager asks on Monday why their shop sold nothing on Friday."),
    ("Tempting mistake", "Narrow the band to ±5 %. Then normal weather and promotions fire it twice a week.", True),
    ("Why", "One shop is 7 % of the total. A completeness check on the total can't see a missing part smaller than the total's normal variation.", True),
    ("What saves you", "Check completeness by segment: every shop that was open has rows today, and each shop's volume is within its own band. A missing segment is a hard fail, however small. The list of expected segments comes from a dimension (shops open today), not from yesterday's data."),
], "completeness is checked per segment. A missing part hides inside a healthy total.") + drill(5, "The status nobody expected", [
    ("Timeline", "The app team adds an order status, <code>partially_refunded</code>. The accepted-values test on status fails, the run stops, and the dashboard stays on yesterday's data for a day while two teams argue whether the test or the app is wrong."),
    ("Tempting mistake", "Remove the accepted-values test, because it “breaks every release”.", True),
    ("Why", "The test was right to notice; the response was wrong. A new value isn't bad data, it's an undeclared change. Failing the whole publish for it treated a contract gap as corrupt data.", True),
    ("What saves you", "Put accepted values in the data contract, so the app's CI flags the new status before release and the data team adds handling first. In the pipeline, make unknown values a <b>warn</b> that quarantines the affected rows and alerts, rather than an <b>error</b> that blocks everything; reserve errors for what makes the published numbers wrong."),
], "a new value is a contract change. Catch it in the producer's CI; in the pipeline, quarantine and warn, don't block everything.") + drill(6, "The alert that cried wolf", [
    ("Timeline", "The shop has 240 tests and 30 anomaly monitors. Each fires falsely about once a month. That's eight or nine alerts a day in the team channel. On the Thursday of week 23 the real alert for Delft's prices is the sixth message that morning. Nobody opens it."),
    ("Tempting mistake", "Mute the noisy channel. The real alerts go with it.", True),
    ("Why", "Alert volume, not alert quality, decides whether alerts are read. Many slightly-wrong checks are worse than a few strong ones.", True),
    ("What saves you", "Tier by consequence: page or message only for checks protecting published numbers (freshness, keys, segment completeness, reconciliation); send the rest to a daily digest. Measure each check's false alert rate and fix or remove any above one a quarter. Every alert names the table, the dashboards affected (from lineage) and the owner."),
], "few strong alerts that get read beat many weak ones that don't.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["monitor data freshness and volume, not job status", "1"],
    ["unique keys tested on every published table", "2"],
    ["distribution checks per product or segment", "3"],
    ["completeness per expected segment, from a dimension", "4"],
    ["new values caught by contracts; warn and quarantine, don't block", "5"],
    ["alerts tiered by consequence, with owners and impact", "6"],
]))

# ------------------------------------------------------------------ 4 hard problem
hard = '''
<p>Writing checks is easy. Deciding <b>which checks</b>, <b>how strict</b>, and <b>what happens when they fire</b> is the hard part. Too loose and week 23 happens; too strict and the pipeline stops for every holiday, until someone disables the checks. The way out is the same as for services: decide what users need from the data, write it down as objectives, and derive the checks from them.</p>
<h3>Data SLOs for the revenue dashboard</h3>
''' + tbl(["Objective", "Target", "Measured by", "Week 23 would have…"], [
    ["<b>freshness</b>", "data at most 45 min old in opening hours, 99 % of the time", "newest event time in <code>fct_sales</code>", "caught Monday"],
    ["<b>completeness</b>", "every open shop present, every day", "shops with rows vs shops open", "caught Friday"],
    ["<b>uniqueness</b>", "no duplicate order lines, ever", "unique test on publish", "caught Tuesday"],
    ["<b>accuracy</b>", "daily revenue within 0.1 % of the source after 24 h", "nightly reconciliation", "caught Thursday by morning"],
], hot=(1,)) + mn("A data SLO is a promise to the dashboard's users, not to the engineers. Write it in their words: “at most 45 minutes old”.") + full('''<p>Each objective tells you what to check, where, and how bad a miss is. Freshness and completeness block nothing; they alert and show a banner, because old-but-correct beats nothing. Uniqueness blocks the publish, because duplicated revenue is worse than yesterday's revenue. Accuracy is measured after the fact and points at a day to replay.</p>
<h3>An error budget for data</h3>
<p>A 99 % freshness objective in opening hours (about 300 hours a month) allows three hours a month of stale data. That budget is useful in two directions. When it is nearly spent, the team stops adding features to the pipeline and fixes reliability. When it is barely touched month after month, the team can stop gold-plating and accept a riskier change, such as moving to a new connector. Week 23 spent the whole monthly budget on Monday morning alone.</p>
<h3>Setting thresholds that survive holidays</h3>
''' + tbl(["Approach", "Example", "Good for", "Watch out"], [
    ["<b>fixed</b>", "row count &gt; 50,000", "nothing that varies", "fails every Sunday and holiday"],
    ["<b>same weekday band</b>", "within ±30 % of the median of the last 6 same weekdays", "daily volume", "holidays and big promotions"],
    ["<b>calendar-aware</b>", "band from the same weekday, holidays from <code>dim_date</code> excluded or modelled", "retail with seasonality", "needs a maintained calendar"],
    ["<b>learned anomaly</b>", "a tool fits a seasonal model per table", "many tables, little time", "opaque; review what it flags"],
    ["<b>hard rule</b>", "every open shop has rows", "completeness, keys", "none: it's a definition"],
]) + '''<p>Use hard rules wherever a check can be stated as a definition (keys, required segments, reconciliation), and statistical bands only for genuinely variable quantities. Most of week 23's failures were catchable with hard rules.</p>
<h3>Block, quarantine or warn</h3>
''' + tbl(["Severity", "Use when", "Effect"], [
    ["<b>block</b> (error)", "the published number would be wrong: duplicate keys, a missing segment, failed reconciliation of the batch", "don't publish; yesterday stays; page the owner"],
    ["<b>quarantine</b>", "some rows are bad, the rest fine: invalid values, unknown codes", "rows set aside; publish the rest; alert if over 1 %"],
    ["<b>warn</b>", "something changed that may be fine: a new value, a volume at the edge of its band", "publish; daily digest; review"],
]) + '''<p>Every check gets one of the three, chosen from the objective it protects. The common mistake is making everything a block (the pipeline stops weekly, checks get disabled) or everything a warn (week 23).</p>''')

# ------------------------------------------------------------------ 5 variants
variants = '''
<p>Four common ways to get data quality, compared on week 23. Real pipelines combine them; the question is which to start with.</p>
''' + tbl(["", "A · tests in the transform (dbt tests)", "B · A + write–audit–publish", "C · an observability tool on every table", "D · contracts at the source"], [
    ["where", "after each model builds", "before the swap into published tables", "on published tables, continuously", "in the producer's CI and at arrival"],
    ["Mon, empty file", "only with a volume test", "only with a volume test", "<b>yes</b>: freshness and volume monitors", "yes: arrival check"],
    ["Tue, duplicates", "yes, if tested on the fact", "<b>yes, and not published</b>", "after the fact", "no"],
    ["Wed, renamed column", "yes, failed run", "yes, not published", "after the fact", "<b>yes, before release</b>"],
    ["Thu, cents", "only with per-product checks", "only with per-product checks", "<b>likely</b>: distribution anomaly", "partly: unit in the contract"],
    ["Fri, a shop missing", "only with segment checks", "only with segment checks", "maybe, if segmented", "no"],
    ["stops bad data reaching users", "no: tables are already built", "<b>yes</b>", "no: detects after", "yes, for schema changes"],
    ["cost to start", "low", "low to medium", "medium (licence or setup)", "medium (needs the producer)"],
], hot=(6,)) + mn("B is the backbone; C is the net under it; D moves the most common failures upstream to where they're cheapest.") + full('''<p>Variant A alone tests tables that users can already see, so a failure is detected, not prevented. Adding write–audit–publish (B) turns the same tests into a gate. An observability tool (C) watches everything continuously and learns seasonal patterns, which covers what nobody thought to test, but it sees problems after publishing and needs its alerts tuned (drill 6). Contracts (D) catch schema and value changes in the producer's pull request, the cheapest moment, but only for producers that adopt them.</p>
<h3>An observability tool, tuned</h3>
<p>Switched on across all 400 tables, a monitoring tool's first week at the shop produced 60 anomaly alerts, most of them correct statistically and useless in practice: a staging table nobody reads, a backfill that was planned. Tuning took a month: monitors only on tables with a consumer (from lineage), the shop's holiday calendar fed in, planned backfills announced to the tool, and each monitor given an owner and a tier. After that it caught two things nobody had a test for in its first quarter: a slow drift in the share of web orders without a customer, and a lookup table that stopped updating.</p>
<h3>The shop's plan after week 23</h3>
''' + tbl(["Week", "Add", "Covers"], [
    ["1", "freshness target and “data as of” banner on the dashboard; volume check on arrival", "Mon"],
    ["1", "unique-key tests on every published table, inside the audit", "Tue"],
    ["2", "segment completeness: every open shop present; per-shop revenue band", "Fri"],
    ["2", "per-product price check against list price", "Thu"],
    ["3", "contract for <code>order_lines</code> and order statuses, checked in the app's CI", "Wed, and new statuses"],
    ["4", "alert tiers and a daily digest; anomaly monitors on the 20 most-used tables", "drill 6, the unknown unknowns"],
]))

# ------------------------------------------------------------------ 6 numbers
numbers = '''
<p>Data quality has a budget: compute for the checks, and attention for the alerts. Attention runs out first.</p>
<h3>The alert arithmetic</h3>
''' + tbl(["", "Before", "After tiering"], [
    ["checks", "270", "270"],
    ["false alert rate per check", "~1 a month", "~1 a quarter (tuned or removed)"],
    ["alerts that interrupt someone", "~9 a day", "~0.3 a day (only blocking and SLO checks)"],
    ["alerts in the daily digest", "0", "~3 a day"],
    ["share of real incidents seen within an hour", "~20 %", "~90 %"],
]) + mn("A check that fires falsely once a month looks harmless. Two hundred of them are nine interruptions a day.") + full('''<h3>What the checks cost to run</h3>
<p>Most checks are an aggregate over one day's partition: a count, a sum, a group by shop. On the shop's warehouse each costs well under a second and a few megabytes scanned. Uniqueness on a published table is the expensive one if done naively (a full scan for duplicates); restrict it to the partitions the batch touched, which is enough because untouched partitions were checked when they were published. The nightly reconciliation reads 60 days of source data from a replica: the biggest single check, and the most valuable.</p>
<h3>Choosing a band width, worked</h3>
<p>Rotterdam's Friday revenue over the last six Fridays: €46k, €51k, €44k, €49k, €62k (a promotion), €48k. The median is €48.5k. A band of ±30 % around it (€34k to €63k) contains every normal Friday, including the promotion. A missing upload (€0) is far outside. A till that drops half its rows (€24k) is outside too. A ±10 % band would have fired on the promotion and on one ordinary Friday. The rule of thumb the shop uses: set the band just wide enough that the last eight same weekdays all pass, then check that the faults you care about (zero, half, double) all fail. If they don't, the quantity is too noisy for a band and needs a hard rule instead.</p>
<h3>Time to detect, time to fix</h3>
''' + tbl(["Incident", "Detected before", "Detected after", "Fixed after"], [
    ["Mon, empty file", "Monday 14:00, by a user", "05:45, freshness alert", "partner resend, 06:30"],
    ["Tue, duplicates", "Tuesday 11:00, by finance", "never published", "MERGE fix, same morning"],
    ["Thu, cents", "Friday 09:00, by Delft's manager", "05:10, price check quarantines Delft's rows", "firmware rollback, 07:00"],
    ["Fri, a shop missing", "Monday, by Rotterdam's manager", "Friday 22:15, completeness check", "upload retried, 22:40"],
]) + '''<p>Detection time is set by where the check runs and when the data arrives. A check on arrival detects within minutes of the source failing; a check on the dashboard's tables only after the next publish; a user only when they look.</p>''')

# ------------------------------------------------------------------ 7 testing the tests
testing = '''
<p>Checks are code, and untested code is wrong in ways you find out about later. The shop learned in week 23 that 37 validity tests had given it confidence and no protection. The fix is to test the checks the way you'd test a smoke alarm: make some smoke.</p>
<h3>Fault injection for data</h3>
''' + tbl(["Fault injected (in a test environment)", "Check that must fire", "Severity expected"], [
    ["empty partner file", "arrival volume; freshness", "block arrival; alert"],
    ["replay the last hour of CDC events", "unique key on <code>fct_sales</code>", "block publish"],
    ["rename <code>line_total</code>", "contract in CI; not-null on amount", "fail build; block"],
    ["multiply one shop's prices by 100", "per-product price check; shop revenue band", "quarantine; block if &gt; 1 %"],
    ["drop one shop's rows", "segment completeness", "block publish"],
    ["add a new status value", "contract; accepted values", "fail build; warn and quarantine"],
], hot=(4,)) + mn("If a fault can't be injected safely, at least write it down. A list of failures you can't detect is more useful than confidence you haven't earned.") + full('''<p>Run the suite in CI against a small seeded copy of the warehouse whenever checks or models change, and quarterly against a full-size test environment. Each fault has an expected check and severity; a test fails if the wrong check fires, or the right one fires at the wrong severity.</p>
''' + code("faults/missing_shop.sql", "inject, run the pipeline, assert", '''
-- 1 · inject: remove Rotterdam from today's till batch in the test environment
DELETE FROM test_raw.till_sales
WHERE  shop_code = 'RTM' AND sold_at::date = :test_day;

-- 2 · run the normal pipeline for :test_day (same DAG, test target)

-- 3 · assert: the completeness check blocked the publish
SELECT 1 FROM check_results
WHERE  check_name = 'segment_completeness_shops'
  AND  run_day = :test_day AND status = 'blocked';   -- must return one row
''') + '''<h3>Replaying a real bad week</h3>
<p>Synthetic faults test what you imagined. Real incidents test what happened. The shop kept week 23's raw files and change events, so it can replay the whole week through the new pipeline in a test environment and check that all five incidents are now caught, at the right checkpoint and severity. Every future incident's raw data is kept the same way, for 90 days, and added to the replay suite. Over a year that becomes a library of real failures, which is worth more than any list of imagined ones.</p>
<h3>A coverage map</h3>
<p>List the published tables down the side and the five quality dimensions across, and mark which have a check with a tested fault. Week 23's map was full of validity and empty everywhere else. The map is the quickest way to see where the next incident will come from, and it fits on one page for a review.</p>
<h3>Reviewing new checks</h3>
<p>Every new check in a pull request answers three questions in its description: which objective does it protect, what severity, and what fault proves it works. Checks that can't answer the first question are usually validity tests nobody needs.</p>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>When a check fires, the next hour decides whether people keep trusting the dashboard. Data incidents deserve the same handling as service incidents, scaled down.</p>
''' + tbl(["Step", "What it looks like"], [
    ["<b>1 · acknowledge</b>", "the owner named in the alert takes it within 15 minutes in opening hours"],
    ["<b>2 · tell consumers</b>", "the dashboard banner says what is affected and since when; lineage lists the reports"],
    ["<b>3 · contain</b>", "yesterday's published data stays (WAP did this); quarantine holds the bad rows"],
    ["<b>4 · fix and replay</b>", "fix at the source or in staging; replay the affected days through the normal pipeline"],
    ["<b>5 · learn</b>", "a short review: which checkpoint caught it, which should have, what check to add"],
]) + mn("Most data incidents need no all-hands. They need one owner, one banner, and one replay.") + full('''<h3>Impact from lineage</h3>
<p>Every alert includes what lineage says is downstream: “<code>fct_sales</code> not published for 2026-06-05. Affects: revenue dashboard, regional report, franchisee portal (Delft), board pack draft.” The people who own those see it once, in their own channel, instead of finding out from a user.</p>
''' + code("alert.txt", "what a good data alert says", '''
[BLOCKED] fct_sales · 2026-06-05 · segment_completeness_shops
  Missing: RTM (Rotterdam). Expected 31 open shops, got 30.
  Published data stays at 2026-06-04 23:59.
  Downstream: revenue dashboard, regional report, franchise portal (RTM)
  Owner: data-platform on call · Source owner: retail-it (tills)
  Runbook: wiki/data/runbooks/missing-shop
''', plain=True) + '''<h3>Telling users, in their words</h3>
<p>The dashboard banner is the most important message in a data incident, and the easiest to get wrong. “Pipeline failure in fct_sales” means nothing to a regional manager. “Friday's sales for Rotterdam are missing. Other shops are complete. Expected fix: Saturday 10:00.” tells them what they can and can't use. The banner text comes from the check: the check knows the segment, the day and the dimension, so the message can be generated, not written in a hurry.</p>
<h3>On call for data</h3>
<p>The shop doesn't run a night rota for data. Blocking checks page the data platform's on-call engineer in opening hours (07:00 to 22:00), and everything outside those hours waits for the morning, because yesterday's data stays published and a few hours of staleness is inside the error budget. The exception is month-end close week, when finance needs fresh data at night and the rota extends for five days.</p>
<h3>The data health dashboard</h3>
''' + tbl(["Panel", "Shows"], [
    ["SLOs", "freshness and completeness for the top 10 tables over 30 days, against target"],
    ["blocked publishes", "how often, which checks, how long until fixed"],
    ["quarantine", "rows waiting per table, oldest age, reasons"],
    ["alerts", "per check: fired, real, false; the false-rate leaderboard"],
    ["reconciliation", "difference per day for the last 60 days, unexplained part highlighted"],
]) + '''<h3>The review after an incident</h3>
<p>Five questions, ten minutes: what happened, how it was detected and how long that took, which checkpoint should have caught it earlier, what check or contract change prevents it, and what fault test proves the new check works. Week 23's five reviews produced the plan in chapter 5.</p>''')

# ------------------------------------------------------------------ 9 tools
tools_ch = '''
<p>The tools fall into four groups. Most teams use one from the first two groups and add the others as the warehouse grows.</p>
''' + tbl(["Group", "Tools", "Gives you", "Leaves to you"], [
    ["tests in the pipeline", "dbt tests and dbt-expectations, Great Expectations, Soda, Deequ", "declarative checks, severities, results stored per run", "which checks, where, and the WAP gate"],
    ["observability", "Elementary, Monte Carlo, Bigeye, Metaplane, Soda Cloud", "freshness, volume and distribution monitors, learned seasonality, incidents", "tuning alerts; deciding what blocks"],
    ["contracts", "Data Contract CLI, ODCS, dbt model contracts, schema registries, Gable", "schema and rule checks in CI, compatibility rules", "getting producers to adopt them"],
    ["lineage and orchestration", "OpenLineage with Marquez, DataHub, dbt docs, Airflow and Dagster", "what feeds what, SLAs on deadlines, asset checks", "including dashboards and exports in lineage"],
]) + mn("Dagster's asset checks and Airflow's data-aware scheduling put checks in the DAG itself, so a failed check stops downstream steps without extra glue.") + full('''<h3>Build or buy</h3>
<p>The checks in chapters 2 to 4 are mostly SQL, and a pipeline framework runs them for free. What is worth buying is what's tedious to build: learned seasonal baselines for hundreds of tables, column-level lineage across warehouse and BI tools, and an incident view that groups related alerts. The shop's rule: build the checks that protect its SLOs (they encode business knowledge), and consider a tool once there are more tables with consumers than people can watch, which happened at about 150.</p>
<h3>What the tools map to</h3>
''' + tbl(["Chapter", "Tool feature"], [
    ["2 · checkpoints", "dbt source freshness (arrival), dbt tests (rows, audit), observability monitors (after publish)"],
    ["3 · drill 3", "dbt-expectations distribution tests, anomaly monitors per segment"],
    ["3 · drill 4", "tests with a <code>group_by</code> or per-segment monitors"],
    ["4 · severity", "dbt <code>severity: warn|error</code> and thresholds, Soda warn/fail levels"],
    ["4 · WAP", "dbt <code>build</code> runs tests before downstream models; Iceberg branches; Snowflake swap"],
    ["7 · fault injection", "a test target in dbt and the scheduler; seeded fixtures"],
    ["8 · impact", "OpenLineage, the observability tool's lineage, or dbt exposures for dashboards"],
]) + code("models/marts/schema.yml", "week 23's lessons in dbt", '''
models:
  - name: fct_sales
    config: { contract: { enforced: true } }
    tests:
      - dbt_utils.unique_combination_of_columns: { combination_of_columns: [order_line_id] }
      - segment_completeness:                       # custom: every open shop has rows
          segment: shop_key
          expected_from: ref('dim_shop_open_days')
          config: { severity: error }
    columns:
      - name: unit_price
        tests:
          - price_within_list_band: { tolerance: 0.5, config: { severity: warn } }
sources:
  - name: partner
    freshness: { error_after: { count: 6, period: hour } }
    loaded_at_field: _loaded_at
''', plain=True))

# ------------------------------------------------------------------ 10 lab
lab = '''
<p><b>The lab.</b> The shop starts selling through a second marketplace. The marketplace drops a CSV of orders on an SFTP server every night around 03:00, sometimes twice (a correction file), sometimes late. Its columns change without warning about twice a year. Marketplace sales will appear on the revenue dashboard and in the franchisee portal.</p>
<ol>
<li>What do you check on arrival, and what happens if the file isn't there by 05:00?</li>
<li>The correction file repeats yesterday's orders with some changes. How do you stay correct?</li>
<li>Write the data SLOs for marketplace revenue on the dashboard.</li>
<li>The marketplace won't sign a contract. What do you do instead?</li>
<li>Which faults do you inject before go-live?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · Arrival</summary><p>File present, header matches the expected columns, row count within the same-weekday band, file not seen before (checksum). Not there by 05:00: alert the marketplace owner, publish everything else, and show “marketplace data as of yesterday” on the dashboard. Don't block the shop's own sales for a partner's file.</p></details>
<details><summary>2 · Corrections</summary><p>Land every file in raw with its name and arrival time. Load by MERGE on the marketplace's order id, newer file wins, so the correction replaces the original rows (idempotent loads). A unique test on the published table catches any slip.</p></details>
<details><summary>3 · SLOs</summary><p>Freshness: marketplace data at most 30 hours old (it's a daily file). Completeness: one file per day. Uniqueness: no duplicate marketplace order ids. Accuracy: daily totals match the marketplace's settlement report within 0.5 % after a week.</p></details>
<details><summary>4 · No contract</summary><p>Write the contract yourself, as your expectation, and enforce it on arrival: a changed header blocks the marketplace load (not the rest), quarantines the file, and alerts. Keep the column mapping in staging so a rename is a one-line fix and a replay.</p></details>
<details><summary>5 · Faults</summary><p>Missing file, empty file, the same file twice, a correction file, a renamed column, prices in a different currency or unit, and one day's file arriving two days late. Each with its expected check and severity.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Objectives", ["Every published table people use has freshness and completeness objectives", "Objectives are written in the users' words", "Each check names the objective it protects"]),
    ("Checkpoints", ["Contracts in producers' CI where possible", "Arrival checks: presence, schema, volume", "Row checks quarantine with reasons", "Audit before publish: keys, segments, batch reconciliation", "Monitors on published tables; nightly reconciliation"]),
    ("Strictness", ["Hard rules wherever a check is a definition", "Bands use the same weekday and the calendar", "Each check is block, quarantine or warn, chosen deliberately"]),
    ("Alerts", ["Only blocking and SLO checks interrupt people", "Every alert names table, impact and owner", "False alert rate tracked per check"]),
    ("Testing", ["A fault for every important check, run in CI", "A coverage map by table and dimension", "New checks state objective, severity and proving fault"]),
    ("Incidents", ["Owner, banner, contain, replay, review", "Lineage includes dashboards and exports", "A data health dashboard the team looks at weekly"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="data-quality-observability", no=15, title="Data Quality & Pipeline Observability",
    sub="Five incidents in one week, one caught: where each kind of check belongs, how strict to be, how to test the checks, and what to do in the hour after one fires.",
    summary="A deep dive on data quality and pipeline observability: six checkpoints, the five quality dimensions, six failure drills, data SLOs and severities, four variants, alert arithmetic, fault injection for data, incident handling, tools, a lab and a checklist.",
    builds_on="Vol. 9, notes 11, 12, 13 and 14",
    builds_on_links=[("Write–Audit–Publish", "../../pipelines/notes/write-audit-publish.html"), ("Data Contracts", "../../pipelines/notes/data-contracts.html"),
                     ("Quality Checks &amp; Quarantine", "../../pipelines/notes/quality-checks.html"), ("DAG Orchestration &amp; Lineage", "../../pipelines/notes/dag-orchestration.html")],
    notes=[("pipelines", "write-audit-publish"), ("pipelines", "data-contracts"), ("pipelines", "quality-checks"), ("pipelines", "dag-orchestration")],
    facts=[("Example", "week 23: five incidents in five days, one caught")],
    blurb="Six checkpoints, five quality dimensions, data SLOs, alerts people read, and fault injection to prove the checks work.",
    chapters=[
        dict(id="recap", nav="Recap", title="Four notes in sixty seconds",
             gist="Write–audit–publish gates what users see, contracts catch changes in the producer's CI, quality checks quarantine bad rows and stop bad batches, and the DAG knows what feeds what. Week 23 had all four in some form, and still let four of five incidents through.",
             body=recap),
        dict(id="checkpoints", nav="Checkpoints", title="The real mechanism: six checkpoints",
             gist="Checks can run in the producer's CI, on arrival, on rows in staging, as an audit before publish, as monitors on published tables, and as a nightly reconciliation. Each catches different failures. Sorted by the five quality dimensions, most pipelines test validity and forget freshness, completeness and consistency.",
             body=mechanism,
             check=[("Which checkpoints prevent and which detect?", "Contract, arrival, row checks and the audit prevent bad data being published; monitors and reconciliation detect after."),
                    ("Which quality dimensions catch outages most often?", "Freshness, completeness and consistency, the ones pipelines usually don't test.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six incidents: a green job that loaded nothing, a replayed hour duplicated in the fact table, prices in cents that passed a wide range, a missing shop hidden in a normal total, a new status that blocked everything, and a real alert lost among false ones.",
             body=drills,
             check=[("A shop's sales are missing but the daily total is within its band. Which check catches it?", "Completeness per segment: every open shop has rows, from the shop dimension."),
                    ("Why not make every failed check block the publish?", "New values and edge-of-band volumes aren't wrong numbers; blocking for them stops the pipeline often until checks get disabled.")]),
        dict(id="slos", nav="Objectives", title="The hard problem: which checks, how strict",
             gist="Start from what users need: data SLOs for freshness, completeness, uniqueness and accuracy, written in their words. Derive checks from them, prefer hard rules over statistical bands, use calendar-aware bands where values vary, and give every check a severity: block, quarantine or warn.",
             body=hard,
             check=[("What should a freshness miss do to the dashboard?", "Alert and show a banner with the data's age; old but correct beats nothing."),
                    ("When is a statistical band the right check?", "Only for genuinely variable quantities like daily volume; definitions such as keys and required segments are hard rules.")]),
        dict(id="variants", nav="Variants", title="Four ways to data quality",
             gist="Tests in the transform detect after tables are visible. Adding write–audit–publish turns them into a gate. An observability tool watches every table for the unexpected. Contracts move schema and value changes into the producer's CI. The backbone is the gate; the others are nets.",
             body=variants,
             check=[("Why do tests alone not stop bad data reaching users?", "They run after the tables are built and visible; without a gate, failures are detected, not prevented."),
                    ("What does an observability tool add?", "Continuous freshness, volume and distribution monitoring on every table, including things nobody wrote a test for.")]),
        dict(id="numbers", nav="Numbers", title="Data quality in numbers",
             gist="Two hundred and seventy checks that each fire falsely once a month make nine interruptions a day. Tiering cuts that to one every few days, and real incidents get seen. Checks are cheap if scoped to the partitions a batch touched. Detection time depends on where the check runs.",
             body=numbers,
             check=[("Why scope uniqueness tests to touched partitions?", "Untouched partitions were checked when published; a full scan every run is cost without benefit."),
                    ("What decides how fast an incident is detected?", "Where the check runs relative to the failure: on arrival within minutes, after publish later, by a user last.")]),
        dict(id="testing", nav="Testing checks", title="Testing the checks",
             gist="Inject faults into a test environment (an empty file, a replay, a rename, prices × 100, a missing shop, a new value) and assert the right check fires at the right severity. Keep a coverage map by table and quality dimension, and make every new check name its objective and proving fault.",
             body=testing,
             check=[("What does a fault-injection test assert?", "That a specific fault triggers the expected check at the expected severity, and no other."),
                    ("What three things should a new check's pull request state?", "The objective it protects, its severity, and the fault that proves it works.")]),
        dict(id="incidents", nav="Running it", title="Running it: data incidents",
             gist="Acknowledge, tell consumers with a banner and the lineage list, contain (write–audit–publish keeps yesterday), fix and replay through the normal pipeline, and review in ten minutes. A data health dashboard shows SLOs, blocked publishes, quarantine and the false-alert leaderboard.",
             body=running,
             check=[("What should every data alert include?", "The table, the failed check, what stays published, the downstream reports from lineage, the owners and a runbook link."),
                    ("How is a bad day fixed?", "Fix at the source or in staging, then replay the affected days through the normal pipeline.")]),
        dict(id="tools", nav="Tools", title="Tools",
             gist="Pipeline test frameworks declare checks, observability tools monitor and learn seasonality, contract tools move checks into producers' CI, and lineage tools connect alerts to impact. None decides which checks matter or what blocks a publish.",
             body=tools_ch),
        dict(id="lab", nav="Lab", title="A lab and the checklist",
             gist="The lab onboards a marketplace that drops a nightly CSV, sometimes twice, sometimes late, with columns that change unannounced: arrival checks, idempotent corrections, SLOs, a self-written contract and the faults to inject. The checklist turns the dive into review questions.",
             body=lab),
    ],
    sources="Barr Moses, Lior Gavish and Molly Vorwerck, <i>Data Quality Fundamentals</i> (2022). Andrew Jones, <i>Driving Data Quality with Data Contracts</i> (2023). Google, <i>Site Reliability Engineering</i> (2016), chapter 4 on service level objectives. dbt documentation, “Data tests”, “Source freshness” and “Model contracts”. Great Expectations, Soda and Elementary documentation. The OpenLineage specification.",
)
