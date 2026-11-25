# Deep dive 14 · One Number Everywhere. Builds on Vol. 9 notes 08 (conformed dimensions), 10 (one big table vs star),
# 15 (metrics layer) and 16 (aggregates & rollups). Example: the homeware shop's Monday meeting, where week 14's
# revenue is €1.92M on the finance dashboard, €2.31M on marketing's and €2.05M in a spreadsheet, and average order
# value differs too. The dive follows "revenue" and "average order value" from that meeting to one definition.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
three_svg = '''
  <rect class="bx-g" x="20" y="30" width="220" height="90" rx="8"/><text class="lbl" x="130" y="64" text-anchor="middle">finance</text><text class="soft" x="130" y="92" text-anchor="middle">€1.92M · AOV €46.10</text>
  <rect class="bx" x="270" y="30" width="220" height="90" rx="8"/><text class="lbl" x="380" y="64" text-anchor="middle">marketing</text><text class="soft" x="380" y="92" text-anchor="middle">€2.31M · AOV €55.40</text>
  <rect class="bx-y" x="520" y="30" width="220" height="90" rx="8"/><text class="lbl" x="630" y="64" text-anchor="middle">spreadsheet</text><text class="soft" x="630" y="92" text-anchor="middle">€2.05M · AOV €48.30</text>
  <text class="bad" x="380" y="160" text-anchor="middle" font-size="18">week 14 · three revenues, three average order values</text>
  <text class="soft" x="380" y="190" text-anchor="middle">every number is “right” for the SQL that made it</text>
'''
recap = '''
<p>Monday, 09:00. Week 14 revenue is <b>€1.92M</b> on the finance dashboard, <b>€2.31M</b> on marketing's and <b>€2.05M</b> in the spreadsheet the regional managers use. Average order value disagrees too. Forty minutes go on reconciling, and nobody decides anything. Four notes in the volume deal with this; together they are a system.</p>
''' + tbl(["Note", "In one line"], [
    ["Conformed Dimensions", "one product, one customer, one calendar, shared by every fact"],
    ["One Big Table vs Star", "model as a star, serve wide tables to the tools that want them"],
    ["Metrics Layer", "define each business number once, in code, and let every tool ask for it"],
    ["Aggregates & Rollups", "pre-compute summaries at the grains people ask for, so it's fast"],
]) + fig(760, 210, "Three dashboards for week 14. Finance shows revenue of 1.92 million euros and average order value of 46.10. Marketing shows 2.31 million and 55.40. The spreadsheet shows 2.05 million and 48.30. Each number is right for the SQL that produced it.",
         three_svg, "Three numbers, each correct for its own SQL. The problem isn't arithmetic; it's definition.") + mn("Nothing here is a bug in the usual sense. Every query does what it says. They just say different things.") + '''
<p class="full">The metrics layer note says “define it once”. This dive is about what that takes in practice: the joins that silently multiply numbers, the definitions nobody wrote down, how a metrics layer turns a question into SQL, how to keep it fast and cheap when 300 managers open it at once, and how to change a definition without breaking last quarter's board pack.</p>
<h3>Why the three numbers differ</h3>
''' + tbl(["Source", "Revenue", "What its SQL actually does"], [
    ["finance", "€1.92M", "net of VAT, after returns booked against the original sale, gift cards excluded"],
    ["marketing", "€2.31M", "gross including VAT, before returns, gift cards included, joined to order discounts (drill 1)"],
    ["spreadsheet", "€2.05M", "net of VAT, before returns, gift cards excluded, week = Sunday to Saturday"],
], hot=(1,)) + '''
<p class="full">Only marketing's number contains an outright bug (the discount, drill 1). The other differences are choices: VAT, returns, gift cards, the first day of the week. Fixing the bug takes an afternoon. Agreeing the choices takes a meeting with the finance director, and making them stick takes the rest of this dive.</p>
'''

# ------------------------------------------------------------------ 2 mechanism
compile_svg = '''
  <rect class="bx-y" x="10" y="20" width="220" height="70" rx="8"/><text class="lbl" x="120" y="50" text-anchor="middle">question</text><text class="soft" x="120" y="74" text-anchor="middle">revenue × category × week</text>
  <rect class="bx" x="270" y="20" width="220" height="70" rx="8"/><text class="lbl" x="380" y="50" text-anchor="middle">semantic model</text><text class="soft" x="380" y="74" text-anchor="middle">entities · measures · dims</text>
  <rect class="bx-g" x="530" y="20" width="220" height="70" rx="8"/><text class="lbl" x="640" y="50" text-anchor="middle">generated SQL</text><text class="soft" x="640" y="74" text-anchor="middle">safe joins · filters</text>
  <path class="ln" d="M230 55 H268" marker-end="url(#a)"/><path class="ln" d="M490 55 H528" marker-end="url(#a)"/>
  <rect class="bx" x="530" y="130" width="220" height="60" rx="8"/><text class="lbl" x="640" y="166" text-anchor="middle">cache / aggregate?</text>
  <path class="ln" d="M640 90 V128" marker-end="url(#a)"/>
  <rect class="bx" x="270" y="130" width="220" height="60" rx="8"/><text class="lbl" x="380" y="166" text-anchor="middle">warehouse</text>
  <path class="ln" d="M530 160 H492" marker-end="url(#a)"/>
  <rect class="bx" x="10" y="130" width="220" height="60" rx="8"/><text class="lbl" x="120" y="166" text-anchor="middle">result · any tool</text>
  <path class="ln" d="M270 160 H232" marker-end="url(#a)"/>
'''
mechanism = '''
<p>A metrics layer is a compiler. You give it a <b>question</b> (a metric, some dimensions, filters, a time grain) and it writes the SQL, using a <b>semantic model</b> that knows the tables, how they join, and how each measure aggregates.</p>
''' + fig(760, 205, "How a metrics layer answers a question. The question, revenue by category by week, goes to the semantic model, which knows entities, measures and dimensions. It generates SQL with safe joins and the metric's filters. The layer checks for a cache or pre-aggregation, runs the query on the warehouse, and returns the result to whatever tool asked.",
          compile_svg, "Question in, SQL out. Every tool gets the same SQL for the same question.") + '''
<h3>What the model knows</h3>
''' + tbl(["Part", "For the shop", "Used to"], [
    ["<b>semantic model</b>", "<code>sales</code> on <code>fct_sales</code>, grain order line", "know what one row is"],
    ["<b>entities</b>", "order_line (primary), order, product, customer, shop", "find safe join paths between models"],
    ["<b>dimensions</b>", "<code>order_date</code> (time), category, region, channel", "group and filter"],
    ["<b>measures</b>", "<code>amount_net</code> (sum), orders (count distinct order_id)", "aggregate correctly at any grain"],
    ["<b>metrics</b>", "revenue, orders, average order value", "the names people use, with filters and owners"],
]) + mn("Entities are the key idea. They tell the layer that sales and returns can both be reached from product, and that order is coarser than order line.") + full('''<h3>The SQL it writes</h3>
<p>For “revenue by category by ISO week, web channel only”, the layer writes roughly this. Note what it decides for you: which table, which join, where the filter goes, how the week is computed.</p>
''' + code("generated.sql", "what the layer sends to the warehouse", '''
SELECT
  date_trunc('week', s.order_date)       AS metric_time__week,
  p.category                             AS product__category,
  sum(s.amount_net)                      AS revenue
FROM fct_sales s
LEFT JOIN dim_product p ON s.product_key = p.product_key
WHERE s.channel = 'web'
  AND NOT p.is_gift_card                  -- the metric's own filter
GROUP BY 1, 2
''') + '''<h3>Ratios are computed last</h3>
<p>Average order value is a <b>ratio metric</b>: revenue divided by orders. The layer computes both at the requested grain and divides at the end, so AOV by region is region revenue over region orders, never the average of shops' averages (drill 3).</p>
''' + code("ratio.sql", "numerator and denominator at the same grain", '''
WITH num AS (SELECT region, sum(amount_net) AS revenue FROM … GROUP BY region),
     den AS (SELECT region, count(DISTINCT order_id) AS orders FROM … GROUP BY region)
SELECT region, revenue / nullif(orders, 0) AS average_order_value
FROM num JOIN den USING (region)
''') + '''<p>The same goes for metrics built from two facts, such as return rate (returns over sales): each side is aggregated on its own and joined on the shared dimensions, the drill-across from the conformed dimensions note, done automatically.</p>
<h3>Questions the layer refuses</h3>
<p>A good layer says no. Ask for “conversion rate by product category” and sessions have no product, so there is no correct answer; the layer returns an error instead of a number. Ask for revenue by a dimension reachable only through a many-to-many path (products in several promotions) and it refuses, because any answer would double count. These refusals feel annoying the first week. They are the reason the numbers can be trusted afterwards: hand-written SQL would have produced something, and someone would have put it on a slide.</p>
<h3>Symmetric aggregates</h3>
<p>Some tools (Looker most famously) take a different route around fan traps: when a join could repeat a coarse row, they sum distinct values keyed by the coarse row's primary key, so order 9001's discount counts once however many lines it joins. It works, and it is why every model must declare primary keys correctly. A wrong key there produces a quietly wrong number, so test keys for uniqueness in the pipeline before the layer relies on them.</p>''')

# ------------------------------------------------------------------ 3 drills
fan_svg = '''
  <rect class="bx-y" x="20" y="40" width="200" height="60" rx="8"/><text class="lbl" x="120" y="66" text-anchor="middle">order 9001</text><text class="soft" x="120" y="88" text-anchor="middle">discount €5</text>
  <rect class="bx" x="330" y="10" width="200" height="40" rx="8"/><text class="soft" x="430" y="36" text-anchor="middle">line: kettle</text>
  <rect class="bx" x="330" y="60" width="200" height="40" rx="8"/><text class="soft" x="430" y="86" text-anchor="middle">line: mugs</text>
  <path class="ln" d="M222 60 L326 32" marker-end="url(#a)"/><path class="ln" d="M222 80 L326 80" marker-end="url(#a)"/>
  <text class="bad" x="640" y="40" text-anchor="middle" font-size="18">sum(discount) = €10</text>
  <text class="soft" x="640" y="70" text-anchor="middle">the order's €5, once per line</text>
  <text class="soft" x="380" y="140" text-anchor="middle">fan trap: an order-level number joined down to its lines</text>
'''
drills = mn("Every drill here passed review and ran for months. The numbers were plausible, just wrong.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · fan trap</a></li><li><a href="#drill-2">2 · chasm trap</a></li><li><a href="#drill-3">3 · average of averages</a></li>
  <li><a href="#drill-4">4 · customers summed</a></li><li><a href="#drill-5">5 · which week</a></li><li><a href="#drill-6">6 · half a filter</a></li>
</ul>
''' + drill(1, "The discount counted per line", [
    ("Timeline", "Marketing wants revenue after discounts. Discounts are stored per order (<code>orders.discount</code>), revenue per line. The dashboard joins orders to lines and sums both. Order 9001, two lines and a €5 discount, shows a €10 discount. Across the week, discounts are overstated by 2.5×, the average lines per order."),
    ("Tempting mistake", "Divide the discount by the number of lines in the dashboard formula. It fixes this tile and breaks the next one, where lines are filtered by category and the divisor is wrong again.", True),
    ("Why", "A <b>fan trap</b>: a measure at a coarse grain (order) joined to a finer grain (line) is repeated once per fine row, then summed.", True),
    ("What saves you", "Keep each measure at its own grain and aggregate it there: order measures from the order fact, line measures from the line fact, joined after aggregation. Or allocate the discount to lines in the pipeline (by line amount), so it becomes a line measure with a documented rule. A metrics layer that knows the grains refuses to sum an order measure through a join to lines."),
], "a measure is summed only at its own grain. Coarse numbers joined to fine rows multiply.") + fig(760, 160, "Drill 1, the fan trap. Order 9001 has a 5 euro discount and two lines, the kettle and the mugs. Joining the order to its lines repeats the discount on each line, so summing it gives 10 euros.",
                  fan_svg, "One order, two lines, the discount twice.") + drill(2, "Sales and returns, multiplied", [
    ("Timeline", "The category manager's report puts units sold and units returned side by side. The SQL joins <code>fct_sales</code> and <code>fct_returns</code> to <code>dim_product</code> in one query and sums both. For the kettle, 400 sales and 12 returns become 4,800 and 4,800."),
    ("Tempting mistake", "Add DISTINCT to the sums. Two kettle sales of the same quantity then count once, and the numbers become wrong in a new, quieter way.", True),
    ("Why", "A <b>chasm trap</b>: two facts joined through a shared dimension in one query produce every sale × every return for each product. Each sum is multiplied by the other side's row count.", True),
    ("What saves you", "Drill across: aggregate each fact to the shared dimension first, then join the small results. Never join two fact tables row to row. In a metrics layer, declare both as separate semantic models with the product entity; the layer generates the two-step query."),
], "two facts meet only after each has been aggregated.") + drill(3, "The average of averages", [
    ("Timeline", "The regional AOV is computed by averaging the shops' AOVs. Delft has 2,000 orders at €44; the small Leiden pop-up has 40 orders at €90. The region's AOV comes out at €67. The real one, all revenue over all orders, is €44.90."),
    ("Tempting mistake", "Weight the average by orders in the dashboard. That is the ratio of sums written by hand, and the next author won't know to do it.", True),
    ("Why", "An average of averages gives every shop the same weight whatever its size. It is only right when every group is the same size.", True),
    ("What saves you", "Store and aggregate the parts (revenue, orders) and divide last, at whatever grain is asked. Make AOV a ratio metric, so no tool can average it. The same applies to conversion rate, margin percentage and every other ratio."),
], "ratios are sums divided at the end, never averages of ratios.") + drill(4, "More customers than people", [
    ("Timeline", "The monthly dashboard sums weekly unique customers: 61,000 + 58,000 + 63,000 + 60,000 = 242,000 “customers in March”. The CRM says 180,000 people bought in March. Regulars who buy every week were counted four times."),
    ("Tempting mistake", "Label the tile “customer-weeks”. Honest, but nobody reads labels, and the board still hears 242,000 customers.", True),
    ("Why", "Distinct counts don't add up across periods or groups that share members. Each week's set overlaps the others.", True),
    ("What saves you", "Count distinct at the grain asked, from the fact table, or store mergeable sketches (HyperLogLog) in aggregates and merge them. Mark the measure non-additive in the semantic model so a tool can't sum it."),
], "distinct counts are recounted or merged, never summed.") + drill(5, "Which week is week 14?", [
    ("Timeline", "Finance's week 14 is the ISO week, Monday to Sunday. The spreadsheet's week starts on Sunday. Marketing's dashboard truncates UTC timestamps. Easter Sunday's €160,000 of sales lands in three different weeks."),
    ("Tempting mistake", "Ask everyone to set their tool to ISO weeks. Some tools can't, defaults come back with every new dashboard, and the time zone problem remains.", True),
    ("Why", "“Week” has at least three definitions, and the time zone moves sales near midnight. Each tool picked its own default.", True),
    ("What saves you", "One calendar dimension (<code>dim_date</code>) with ISO week, fiscal week and fiscal period as columns, keyed on the local date computed once in the pipeline. The metrics layer exposes only those, so “week” means the business's week everywhere."),
], "time grains come from one calendar, in the business's time zone.") + drill(6, "Conversion with half a filter", [
    ("Timeline", "Web conversion rate is orders divided by sessions. A dashboard filters “channel = app” by joining the filter to orders only. App orders over all sessions: conversion drops from 3.1 % to 0.9 %, and the app team spends a week investigating a problem that doesn't exist."),
    ("Tempting mistake", "Tell the app team to filter sessions too. They will, on this dashboard, until the next ratio someone builds.", True),
    ("Why", "A filter applied to the numerator but not the denominator changes what the ratio means. Hand-written SQL makes this easy; nothing complains.", True),
    ("What saves you", "Ratio metrics in the layer apply every filter to both parts, or refuse when a dimension isn't available on one of them (sessions have no product category, so “conversion by category” must be refused or defined separately)."),
], "a ratio's filters apply to both parts, or the question is refused.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["measures aggregate at their own grain", "1"],
    ["facts meet after aggregation (drill across)", "2"],
    ["ratios are sums divided last", "3, 6"],
    ["distinct counts are recounted or merged", "4"],
    ["one calendar in the business time zone", "5"],
    ["the layer refuses questions it can't answer correctly", "6"],
]))

# ------------------------------------------------------------------ 4 hard problem
hard = '''
<p>The drills are traps a good layer prevents. The harder problem is that the three revenues in chapter 1 are all <b>correct SQL for different definitions</b>, and nobody chose between them. A metrics layer makes a definition executable; it doesn't make the decision. Defining a number means answering a handful of questions explicitly, and getting the right person to sign it.</p>
<h3>The questions behind “revenue”</h3>
''' + tbl(["Question", "Options", "The shop's answer"], [
    ["VAT?", "gross incl. VAT · net", "net"],
    ["returns?", "ignore · on the return date · against the original sale", "against the original sale"],
    ["gift cards?", "when sold · when redeemed · excluded", "excluded; redemptions count when spent"],
    ["discounts?", "before · after, allocated to lines", "after, allocated by line amount"],
    ["shipping fees?", "included · excluded", "excluded (other income)"],
    ["cancelled orders?", "included until cancelled · never", "never"],
    ["which date?", "placed · paid · shipped", "placed, local time"],
    ["which category?", "as it was · as it is", "as it was (type 2)"],
], hot=(1, 7)) + mn("Returns and the category choice moved more money between the three dashboards than anything else.") + full('''<p>Each row is a business decision. The finance director owns revenue; marketing can have its own metric, <code>gross_merchandise_value</code>, with its own owner, as long as it is never labelled “revenue”. Names are part of the definition.</p>
<h3>Naming rules</h3>
<p>Most disagreements start with two things sharing a name. The shop adopts three rules. One name, one definition: there is exactly one <code>revenue</code>, and variants carry what makes them different in the name (<code>revenue_incl_vat</code>, <code>gross_merchandise_value</code>). Units in the name when they aren't obvious (<code>margin_pct</code>, <code>delivery_days</code>). No people or teams in names (<code>revenue_marketing</code> means nothing a year later). The layer enforces the first rule mechanically, because two metrics can't share a name.</p>
<h3>Writing it down so it can't drift</h3>
<p>Every certified metric gets a short specification next to its code: the answers above, the owner, the grain, the additivity, and a sentence a non-engineer can read. The code implements the specification; review checks they match.</p>
''' + code("metrics/revenue.yml", "definition and specification in one place", '''
metrics:
  - name: revenue
    label: Revenue
    description: >
      Net of VAT, after discounts (allocated to lines), returns booked against
      the original sale, excluding gift cards, shipping and cancelled orders.
      Dated by order placed, Europe/Amsterdam. Categories as they were.
    type: simple
    type_params: { measure: amount_net_after_returns }
    filter: |
      {{ Dimension('product__is_gift_card') }} = false
      and {{ Dimension('order__is_cancelled') }} = false
    meta: { owner: finance-director, certified: true, since: 2026-12-01 }
''', plain=True) + '''<h3>Returns, worked through</h3>
<p>Order 9001 was placed on 31 March for €45.45 net. One mug, €6.61 net, came back on 3 April. Where does the return go?</p>
''' + tbl(["Booking rule", "March revenue", "April revenue", "Consequence"], [
    ["ignore returns", "€45.45", "€0", "overstates revenue; return-heavy categories look better than they are"],
    ["on the return date", "€45.45", "−€6.61", "March is final at close; April carries March's returns"],
    ["against the original sale", "€38.84", "€0", "March is right but keeps changing for 60 days after close"],
]) + '''<p>The shop chooses “against the original sale” for analysis, because category managers want return-adjusted performance by the month it was sold, and files a snapshot at close for finance (chapter 8). Accounting books the return in April. The difference between the two is real, predictable and documented, so the monthly reconciliation can explain it line by line instead of arguing about it.</p>
<h3>Changing a definition</h3>
<p>Definitions change: the business decides shipping is revenue after all. Changing the metric in place rewrites every past report, including the board pack filed last quarter. Treat it like an API change: publish the new definition under a version or a new name, show both side by side for a period, tell every consumer, record the change with a date, then switch the main name and keep the old one available but marked deprecated. Filed numbers stay filed (the history deep dive covers why).</p>''')

# ------------------------------------------------------------------ 5 variants
variants = '''
<p>There are four common ways to get one number everywhere. Here is each one run against the drills and the shop's tools: two BI tools, spreadsheets, notebooks and the embedded franchisee portal.</p>
''' + tbl(["", "A · definitions in each tool", "B · one big table, documented", "C · semantic model inside one BI tool", "D · headless metrics layer"], [
    ["where revenue lives", "every dashboard's SQL", "a column per measure in a wide table", "LookML, a Power BI model", "dbt Semantic Layer, Cube"],
    ["drill 1, fan trap", "each author's problem", "<b>baked in</b> if the table mixes grains", "prevented by declared grains", "prevented by declared grains"],
    ["drill 3, ratios", "each author's problem", "users average the column", "ratio measures", "ratio metrics"],
    ["reaches spreadsheets, notebooks, the portal", "copies", "yes, it's a table", "<b>only that BI tool</b>", "yes, by API and SQL"],
    ["new questions", "new SQL each time", "only the columns that exist", "any joinable dimension", "any joinable dimension"],
    ["effort to start", "none", "low", "medium", "medium to high"],
], hot=(3,)) + mn("Most shops end up with D behind their main BI tool, or with C when one tool really is all they use.") + full('''<p>Variant A is where everyone starts and why the Monday meeting happens. Variant B is a sensible first step: one wide table per subject (<code>obt_sales</code>) with clearly named, pre-computed measure columns removes most disagreement, but it can't stop someone averaging the AOV column, and every new question needs a new column. Variant C is excellent when one BI tool is the only consumer: Looker and Power BI models know grains and ratios. But the spreadsheet and the franchisee portal can't use it, so their numbers drift. Variant D puts the model outside any tool, so every consumer asks the same layer.</p>
<h3>Variant B, done well</h3>
<p>If a layer is not possible yet, a wide table can still remove most of the Monday arguments. Give it one grain per table, pre-computed measure columns named after the agreed definitions (<code>revenue</code>, never <code>amount</code>), the parts of every ratio rather than the ratio itself (<code>revenue</code> and <code>orders</code>, not <code>aov</code>), a calendar from <code>dim_date</code>, and column descriptions copied from the specification. It is variant D's definitions without the compiler, and it makes the later move to a layer a matter of pointing the model at tables that are already right.</p>
<h3>The shop's choice</h3>
''' + tbl(["Consumer", "Reads"], [
    ["finance and management dashboards", "the metrics layer, through the BI tool's connector"],
    ["regional managers' spreadsheets", "the metrics layer's spreadsheet add-in, or a scheduled extract it produces"],
    ["analysts' notebooks", "the metrics layer's SQL or Python API for metrics; raw marts for exploration"],
    ["the franchisee portal", "the layer's API with a security context per franchisee"],
    ["ad-hoc exploration", "marts directly, clearly labelled “not certified”"],
]) + '''<p>Exploration stays free. Only numbers that leave the analytics team need to come from the layer.</p>
<h3>Getting from A to D without a big bang</h3>
<ol>
<li><b>Find the numbers that matter.</b> List the ten metrics that appear in management reports. Ignore the other four hundred for now.</li>
<li><b>Define them, one meeting each.</b> Owner, specification, code, fixtures. Put them in the layer and certify them.</li>
<li><b>Move the top dashboards.</b> Repoint the five most-viewed dashboards' tiles to the layer, compare old and new values side by side for two weeks, explain every difference, then switch.</li>
<li><b>Mark the rest.</b> Every tile not coming from the layer gets a “not certified” label. People stop putting those on slides on their own.</li>
</ol>
<p>At the shop this took six weeks for revenue, orders, AOV, margin and return rate. The Monday meeting got shorter after the second week, when finance and marketing were looking at the same tile with two clearly named metrics on it.</p>''')

# ------------------------------------------------------------------ 6 numbers
numbers = '''
<p>A metrics layer adds a hop to every query, and it concentrates load: everybody's dashboards now run through it. The numbers decide whether it feels instant.</p>
<h3>Monday morning, worked out</h3>
''' + tbl(["", "Without caching", "With pre-aggregations"], [
    ["dashboard opens 08:55–09:15", "300", "300"],
    ["queries per open (tiles)", "8", "8"],
    ["queries reaching the warehouse", "2,400", "~40 (cache misses and refreshes)"],
    ["rows scanned per query", "60 M lines (a year)", "~20,000 (daily aggregate rows)"],
    ["median tile time", "4–6 s", "&lt; 300 ms"],
]) + mn("Pre-aggregations are aggregates (Vol. 9) that the layer builds and routes to by itself.") + full('''<h3>A latency budget</h3>
<p>People decide whether to trust a dashboard partly by how it feels. Set targets and measure them per tile: under one second for the management dashboard's tiles (pre-aggregated, cached), under five seconds for exploratory questions the layer compiles to the fact tables, and an honest spinner with a message beyond that. Tiles that regularly miss the first target are the list of pre-aggregations to build next.</p>
<h3>Sizing the pre-aggregations</h3>
<p>The common dashboard grain is day × shop × category: 365 × 31 × 200 = about 2.3 million rows a year, a few dozen megabytes. Week × region × category is under 100,000. The layer answers any question at or above a stored grain from it (summing additive measures, merging sketches) and falls back to the fact for anything finer. Refresh only the days a batch touched, as with any aggregate.</p>
<h3>Distinct counts, approximately</h3>
<p>Unique customers can't be summed (drill 4). A HyperLogLog sketch with 2<sup>14</sup> registers is about 16 KB and accurate to about ±0.8 %. Stored per day × shop × category, merged at query time, it answers “unique customers by region this quarter” from the aggregate. Mark such metrics as approximate in their description; finance reports that need exact counts query the fact.</p>
<h3>Cache freshness</h3>
<p>A cache keyed on the query and invalidated when the underlying data publishes (write–audit–publish gives a clean moment) is always consistent with the warehouse. A time-based cache of 15 minutes is simpler, but after a correction the dashboard and the warehouse disagree for up to 15 minutes, which is exactly the kind of disagreement this whole exercise was meant to end.</p>
<h3>What the layer itself costs</h3>
<p>A headless layer is a small service: a couple of containers for the API and the cache, plus the storage for pre-aggregations. At the shop's size that is far less than the warehouse compute it saves on Monday mornings. The real cost is people: someone has to own the model, review metric changes and answer “why is this number different”. Budget a part-time owner from the start; a metrics layer nobody maintains drifts back into variant A within a year, with extra steps.</p>''')

# ------------------------------------------------------------------ 7 testing
testing = '''
<p>Metric bugs look like plausible numbers. Tests must therefore pin numbers down: known inputs with known outputs, the same metric through different paths, and agreement with the books.</p>
''' + tbl(["Test", "Checks", "Catches"], [
    ["<b>metric unit tests</b>", "tiny fixtures with hand-computed totals, including a two-line order with a discount", "drills 1, 3, 6"],
    ["<b>metric diff in CI</b>", "every pull request recomputes key metrics for the last 90 days and shows what changed", "unintended definition changes"],
    ["<b>cross-path consistency</b>", "revenue via the API, via the BI tool and via the extract agree to the cent", "a tool bypassing the layer"],
    ["<b>ledger reconciliation</b>", "monthly revenue within 0.1 % of the finance ledger, differences explained", "definitions drifting from accounting"],
    ["<b>additivity checks</b>", "sum of shops equals the region; sum of days equals the month", "non-additive measures summed"],
], hot=(1, 3)) + mn("The metric diff on pull requests is the single most useful habit: reviewers see “revenue for March changes by −€41,200” before merging.") + full(code("metric_fixture.yml", "order 9001 as a test", '''
# two lines, an order discount of €5 incl. VAT (€4.13 net), one mug returned
given:
  orders:      [{order_id: 9001, discount_net: 4.13, placed: 2026-03-31}]
  order_lines: [{line: 1, order_id: 9001, sku: K-100, amount_net: 32.23},
                {line: 2, order_id: 9001, sku: M-210, amount_net: 13.22}]
  returns:     [{line: 2, qty: 1, amount_net: 6.61, returned: 2026-04-03}]
expect:
  revenue:             {2026-03-31: 34.71}   # 45.45 − 4.13 discount − 6.61 return
  orders:              {2026-03-31: 1}
  average_order_value: {2026-03-31: 34.71}
''', plain=True) + '''<p>Write the expected values by hand from the specification, not by running the query. The point is that a person and the code agree on what the definition means. When they don't, one of them is wrong, and it is worth finding out which before the board does.</p>
<h3>Reconciling with the ledger, worked</h3>
<p>Finance's general ledger for March says €7.912M net sales. The layer says €7.884M. The gap is €28,000, 0.35 %, above the 0.1 % threshold. Broken down by cause:</p>
''' + tbl(["Cause", "Amount", "Expected?"], [
    ["returns booked in April by accounting, against March by the layer", "+€41,200 in the layer's favour", "yes, documented"],
    ["shipping fees: ledger books them as sales, the layer excludes them", "−€63,800", "yes, documented"],
    ["two days of Delft till sales missing from the warehouse", "−€5,400", "<b>no</b>: a pipeline gap"],
]) + '''<p>The first two lines are definitions and stay. The third is a bug the reconciliation found: a till upload that never arrived. After replaying it, the unexplained part is zero, which is the real target. The threshold is for the unexplained remainder, not for the total gap.</p>
<h3>Testing through the tools</h3>
<p>Once a week, a job asks every consumer path for the same three numbers (revenue, orders, AOV for last week): the layer's API, the BI tool's export, the spreadsheet extract, the franchisee portal for one franchisee summed with the others. Any difference means a path has its own SQL somewhere. It is the cheapest way to find the dashboard someone built straight on the marts last month.</p>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>Running a metrics layer is mostly governance: who owns which number, how definitions change, and which numbers people may trust.</p>
''' + tbl(["Practice", "How it looks at the shop"], [
    ["<b>owners</b>", "every certified metric has a named business owner who approves changes"],
    ["<b>certification</b>", "certified metrics carry a badge in every tool; everything else says “not certified”"],
    ["<b>change log</b>", "each definition change has a date, a reason and the size of the effect on the last 12 months"],
    ["<b>deprecation</b>", "old metrics stay queryable for a quarter, marked deprecated, then retired"],
    ["<b>month-end freeze</b>", "no definition changes between the last working day and the close"],
]) + mn("A metric without an owner is a metric that will be changed by whoever is in a hurry.") + full('''<h3>Retiring a metric</h3>
<p>Metrics accumulate: <code>revenue_old</code>, <code>revenue_marketing_2024</code>, <code>aov_excl_outliers</code>. Each one is a chance for the Monday meeting to come back. Every quarter, list metrics with no queries in 90 days and propose retiring them to their owners; list duplicates that differ only in one filter and merge them into one metric with a dimension. Retiring is as deliberate as adding: marked deprecated, announced, removed after a quarter. The certified list should get shorter as often as it gets longer.</p>
<h3>Three metrics about the metrics</h3>
''' + tbl(["Metric", "Means", "Act when"], [
    ["share of dashboard queries through the layer", "how much is governed", "below 80 %: find the dashboards on raw marts"],
    ["cache hit rate on Monday morning", "how fast it feels", "below 90 %: add a pre-aggregation"],
    ["uncertified metrics used in management reports", "trust leaking", "any: certify them or remove them"],
]) + '''<h3>Announcing a change</h3>
<p>When shipping fees become part of revenue, the owner sends one short note to everyone who uses the metric: what changes, from which date, the effect on the last twelve months (from the metric diff: +3.1 % on average, +4.8 % in December), what happens to filed reports (nothing: they stay as filed), and where the old definition can still be found (<code>revenue_v1</code>, until the end of the quarter). Five sentences prevent five meetings.</p>
<h3>The runbook</h3>
''' + tbl(["Situation", "Do"], [
    ["two dashboards disagree", "check both go through the layer; if one doesn't, move it; if both do, compare the generated SQL"],
    ["finance's ledger and revenue differ by 0.4 %", "list the difference by day and type (returns, gift cards, shipping); fix the definition or document the gap"],
    ["a definition must change", "new version beside the old, metric diff to show the effect, owner sign-off, announce, switch, deprecate"],
    ["the layer is slow on Monday", "look at the slowest uncached queries; add a pre-aggregation at their grain"],
    ["a team wants “just a quick number”", "explore on marts; if the number leaves the team, it goes through the layer"],
]))

# ------------------------------------------------------------------ 9 tools
tools_ch = '''
<p>Metrics layers come in two kinds: inside a BI tool, or standalone (“headless”) and reachable from many tools. All of them compile questions into SQL from a semantic model; they differ in reach, caching and how much modelling they expect.</p>
''' + tbl(["Tool", "Kind", "Gives you", "Leaves to you"], [
    ["dbt Semantic Layer (MetricFlow)", "headless, in the dbt project", "metrics next to the models, safe joins via entities, ratio and cumulative metrics, APIs and BI connectors", "caching depends on the platform; the definitions"],
    ["Cube", "headless service", "data model, pre-aggregations with routing, caching, REST, GraphQL and SQL APIs, security context per user", "running the service; the definitions"],
    ["Looker (LookML)", "inside the BI tool", "a mature model with explores, symmetric aggregates against fan-out, aggregate awareness", "reaching tools other than Looker"],
    ["Power BI semantic models", "inside the BI tool", "DAX measures, relationships, aggregations, row-level security", "non-Microsoft consumers; DAX skills"],
    ["Malloy, AtScale and others", "language or headless", "a modelling language or OLAP-style layer", "smaller ecosystems"],
]) + mn("Looker's symmetric aggregates solve the fan trap by de-duplicating on primary keys inside the sum. It's clever, and it's why declaring primary keys matters in every tool.") + full('''<h3>What the tools map to</h3>
''' + tbl(["Chapter", "Tool feature"], [
    ["2 · compiling questions", "MetricFlow query planning, Cube's data model, LookML explores"],
    ["3 · fan and chasm traps", "entities and join paths; symmetric aggregates; refusing unsafe joins"],
    ["4 · definitions", "metric descriptions and <code>meta</code> (owner, certification)"],
    ["6 · speed", "Cube pre-aggregations, Looker aggregate awareness, Power BI aggregations, warehouse result caches"],
    ["7 · metric diff", "dbt's state comparison in CI with a metrics query, or a small script against the layer's API"],
    ["8 · certification", "badges and endorsements in BI tools, the layer's metadata"],
]) + '''<h3>Choosing one</h3>
''' + tbl(["If", "Then"], [
    ["one BI tool is genuinely the only consumer", "its own semantic model (LookML, Power BI)"],
    ["the team already models in dbt", "dbt Semantic Layer, so metrics live beside the models"],
    ["many consumers and an app that embeds numbers", "a headless layer with caching and a security context (Cube, or dbt's layer with a caching platform)"],
    ["none of the above yet", "variant B: one documented wide table per subject, and the definitions written down; move to a layer when the second tool arrives"],
]) + '''<p>None of them chooses whether returns are booked against the original sale. That is chapter 4, and it is the part that ends the Monday meeting.</p>''')

# ------------------------------------------------------------------ 10 lab
lab = '''
<p><b>The lab.</b> Franchisees join the portal in July. They want three numbers for their own shops: revenue, gross margin percentage and return rate. Head office wants the same numbers across all shops for the board. The product cost table is maintained by purchasing and changes monthly; returns can arrive up to 60 days after the sale.</p>
<ol>
<li>Define gross margin percentage: what are its parts, and at which grain are they stored?</li>
<li>Return rate: units or money? Against which date? Where can it be computed?</li>
<li>Which cost applies to a sale in March if the cost changes in April?</li>
<li>How does a franchisee see only their shops, through the same metrics?</li>
<li>The board wants “margin by region” as a single number per region. A slide averages shops' margins. What do you say?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · Gross margin %</summary><p>A ratio metric: (revenue − cost of goods) / revenue, both summed at the line grain and divided last. Store <code>cost_of_goods</code> on each sales line at load time, so it is a line measure like revenue.</p></details>
<details><summary>2 · Return rate</summary><p>Decide with the owner; the shop picks money: returned revenue / revenue, returns booked against the original sale date. It needs both facts, so it is a drill-across metric on the shared dimensions (product, shop, date of sale). Recent periods are incomplete for 60 days: say so on the dashboard.</p></details>
<details><summary>3 · Which cost</summary><p>The cost valid on the sale date, looked up at load time from a type 2 cost history and stored on the line. Then March margin never changes when April's cost is entered.</p></details>
<details><summary>4 · Franchisees</summary><p>The portal calls the layer with a security context from a signed token; the layer adds the franchisee's shops as a filter to every query, on both parts of every ratio. Same definitions, fewer rows.</p></details>
<details><summary>5 · The slide</summary><p>An average of shop margins is drill 3: it weights the pop-up the same as Delft. Ask the layer for margin by region; it sums revenue and cost per region and divides.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Definitions", ["Every certified metric has an owner and a written specification", "Names are unique: no two metrics called revenue", "VAT, returns, discounts, gift cards and dates are decided, not defaulted", "Changes are versioned, diffed and announced"]),
    ("Model", ["Each semantic model has a stated grain and primary key", "Measures declare additivity", "Ratios are numerator and denominator, divided last", "Facts meet only through conformed dimensions"]),
    ("Time", ["One calendar dimension with ISO and fiscal weeks", "Local business dates computed once in the pipeline", "Late-arriving periods are labelled incomplete"]),
    ("Reach", ["Dashboards, spreadsheets, notebooks and the portal all read the layer", "Exploration on marts is labelled “not certified”", "Row-level security passes through the layer"]),
    ("Speed", ["Pre-aggregations at the common grains", "Cache invalidated on publish", "Approximate metrics say so"]),
    ("Tests", ["Metric unit tests with hand-computed fixtures", "Metric diff on every pull request", "Monthly reconciliation with the ledger", "Weekly cross-path consistency check"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="one-number-everywhere", no=14, title="One Number Everywhere",
    sub="From a Monday meeting with three revenues to one definition every tool uses: the traps that multiply numbers, how a metrics layer writes SQL, what a definition must decide, and how to keep it fast and trusted.",
    summary="A deep dive on metrics layers: how questions compile to SQL, six failure drills (fan and chasm traps, averages of averages, distinct counts, weeks, half-filtered ratios), defining a metric, four variants, caching numbers, testing metrics, governance, tools, a lab and a checklist.",
    builds_on="Vol. 9, notes 08, 10, 15 and 16",
    builds_on_links=[("Conformed Dimensions", "../../pipelines/notes/conformed-dimensions.html"), ("One Big Table vs Star", "../../pipelines/notes/one-big-table.html"),
                     ("Metrics Layer", "../../pipelines/notes/metrics-layer.html"), ("Aggregates &amp; Rollups", "../../pipelines/notes/aggregates-rollups.html")],
    notes=[("pipelines", "conformed-dimensions"), ("pipelines", "one-big-table"), ("pipelines", "metrics-layer"), ("pipelines", "aggregates-rollups")],
    facts=[("Example", "week 14 revenue: €1.92M, €2.31M or €2.05M?")],
    blurb="Fan and chasm traps, averages of averages, what “revenue” must decide, how a metrics layer writes SQL, and keeping it fast.",
    chapters=[
        dict(id="recap", nav="Recap", title="Four notes in sixty seconds",
             gist="Conformed dimensions share one calendar and one product list, wide tables serve tools, a metrics layer defines each number once, and aggregates keep it fast. The Monday meeting with three revenues for one week is what happens without them working together.",
             body=recap),
        dict(id="compiler", nav="Mechanism", title="The real mechanism: a compiler for questions",
             gist="A metrics layer takes a question (metric, dimensions, filters, time grain) and writes SQL from a semantic model that knows each table's grain, how tables join through entities, and how each measure aggregates. Ratios and two-fact metrics are computed part by part and combined last.",
             body=mechanism,
             check=[("What do entities give the layer?", "Safe join paths between semantic models, and which grains are coarser or finer."),
                    ("How is average order value by region computed?", "Region revenue divided by region orders, both aggregated at region level; never the average of shop averages.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways a correct-looking query gives a wrong number: an order discount summed per line, two facts joined through a dimension, an average of averages, weekly unique customers added up, three definitions of a week, and a ratio filtered on one side only.",
             body=drills,
             check=[("Discounts are 2.5× too high after joining orders to lines. Name the trap.", "A fan trap: an order-level measure repeated for each line and then summed."),
                    ("Why can't weekly unique customers be added up for the month?", "Regulars appear in several weeks; distinct counts must be recounted or merged.")]),
        dict(id="definitions", nav="Definitions", title="The hard problem: deciding what a number means",
             gist="The three revenues were correct SQL for different definitions. Defining a metric means deciding VAT, returns, discounts, gift cards, dates and as-was categories, writing the answers next to the code, giving it an owner, and changing it like an API: versioned, diffed and announced.",
             body=hard,
             check=[("Marketing wants revenue including VAT. What do you do?", "Give it its own name and owner (e.g. gross merchandise value); “revenue” stays the finance definition."),
                    ("Why not change a definition in place?", "It silently rewrites every past report, including filed ones; version it, show both, then switch.")]),
        dict(id="variants", nav="Variants", title="Four ways to one number",
             gist="Definitions in every tool is where the problem starts. A documented wide table helps but can't stop averaging. A semantic model inside one BI tool works until a spreadsheet or portal needs the number. A headless metrics layer serves every consumer from one model.",
             body=variants,
             check=[("Why isn't a BI tool's semantic model enough for the shop?", "Spreadsheets, notebooks and the franchisee portal can't use it, so their numbers drift."),
                    ("Does exploration have to go through the layer?", "No; only numbers that leave the analytics team, labelled certified.")]),
        dict(id="numbers", nav="Numbers", title="Keeping it fast",
             gist="Three hundred dashboard opens on a Monday are 2,400 queries. Pre-aggregations at day × shop × category answer most of them from a few million rows in milliseconds. Sketches make distinct counts mergeable. Invalidate caches on publish, not on a timer.",
             body=numbers,
             check=[("Why invalidate the cache on publish rather than every 15 minutes?", "So the dashboard never disagrees with the warehouse after a correction."),
                    ("How are unique customers answered from an aggregate?", "Store HyperLogLog sketches per row and merge them at query time.")]),
        dict(id="testing", nav="Testing", title="Testing numbers",
             gist="Pin numbers down: hand-computed fixtures for each metric, a metric diff on every pull request, the same metric through every consumer path, monthly reconciliation with the finance ledger, and additivity checks.",
             body=testing,
             check=[("What does a metric diff in CI show reviewers?", "How much each key metric changes over recent periods if the pull request is merged."),
                    ("Why write expected fixture values by hand?", "So a person and the code independently agree on what the definition means.")]),
        dict(id="running", nav="Running it", title="Running it: governance",
             gist="Every certified metric has an owner, a badge, a change log and a deprecation path; definitions freeze at month end. Watch how much traffic goes through the layer, the Monday cache hit rate, and uncertified numbers in management reports.",
             body=running,
             check=[("Two dashboards disagree. First check?", "Whether both go through the layer; one usually has its own SQL on the marts."),
                    ("What is a month-end freeze?", "No definition changes between the last working day and the close.")]),
        dict(id="tools", nav="Tools", title="Tools",
             gist="dbt's Semantic Layer and Cube are headless layers reachable from many tools; LookML and Power BI models live inside their BI tool. All compile questions to SQL and help with traps and speed. None decides what revenue means.",
             body=tools_ch),
        dict(id="lab", nav="Lab", title="A lab and the checklist",
             gist="The lab defines gross margin and return rate for franchisees and the board: ratios from line-level parts, costs fixed at the sale date, returns against the sale, security through the layer. The checklist turns the dive into review questions.",
             body=lab),
    ],
    sources="dbt Labs, “About MetricFlow” and semantic models documentation. Cube documentation, “Data modeling” and “Pre-aggregations”. Looker documentation, “Symmetric aggregates”. Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), on additivity and drilling across. Benn Stancil, “The missing piece of the modern data stack” (2021). Philippe Flajolet et al., “HyperLogLog” (2007).",
)
