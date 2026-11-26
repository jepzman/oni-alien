# Vol. 9 · Serving reports: Metrics Layer, Aggregates & Rollups, Lambda vs Kappa, Multi-tenant & Embedded Reporting.
# Same homeware shop: 30 shops and a web store; shop managers and, later, franchisees see their own numbers.

# ------------------------------------------------------------------ 15 Metrics Layer
ml_problem = Doodle(760, 260, "Doodle of three revenue numbers for the same week. The finance dashboard says 1.92 million euros: net of VAT, after returns. The marketing dashboard says 2.31 million: gross, including VAT. The spreadsheet says 2.05 million: net, but without gift cards. The Monday meeting is spent arguing about which is right.",
                    "Three “revenue” numbers for one week, and a meeting spent arguing about them.")
ml_problem.box(20, 40, 220, 100, "finance", "green", sub="€1.92M · net, after returns", size=21, subsize=13)
ml_problem.box(270, 40, 220, 100, "marketing", "blue", sub="€2.31M · gross, incl. VAT", size=21, subsize=13)
ml_problem.box(520, 40, 220, 100, "spreadsheet", "y", sub="€2.05M · no gift cards", size=21, subsize=13)
ml_problem.note(380, 190, "all three are called “revenue”", "red")
ml_problem.note(380, 222, "Monday's meeting: 40 minutes on which one is right", "pen")

ml_analogy = Doodle(760, 240, "Doodle of a franchise recipe card. Every branch of a burger chain makes the burger from the same card: the same weights, the same steps. Head office changes the card once, and every branch follows.",
                    "Every branch cooks from one recipe card. Change the card once, every branch follows.")
ml_analogy.icon("recipe", 320, 30, 1.9, fill="y")
for i, t in enumerate(["branch A", "branch B", "branch C"]):
    ml_analogy.arrow(420, 90, 560, 40 + i * 60)
    ml_analogy.box(566, 18 + i * 60, 170, 46, t, "green", size=18)
ml_analogy.note(130, 100, "head office edits it once", "pen")
ml_analogy.arrow(220, 100, 310, 100)

ml_how = Doodle(760, 300, "A metrics layer. Revenue is defined once in code: the sum of net amount from fact sales, excluding gift cards, by order date, sliceable by product, shop and customer. Dashboards, spreadsheets and notebooks ask the layer for revenue by category by week, and the layer writes the SQL, chooses the joins and applies the filters.",
                 "Define the number once, in code. Every tool asks the layer, and the layer writes the SQL.")
ml_how.box(230, 20, 300, 110, "revenue", "y", sub="sum(amount_net) · no gift cards", size=23, subsize=13)
ml_how.note(115, 56, "owner · description", "pen")
ml_how.note(115, 84, "dimensions · in git", "pen")
for i, t in enumerate(["dashboard", "spreadsheet", "notebook"]):
    ml_how.box(20 + i * 260, 200, 200, 60, t, "blue", size=19)
    ml_how.arrow(120 + i * 260, 196, 330 + i * 50, 134, both=True)
ml_how.note(380, 290, "“revenue by category by week” → generated SQL", "pen", size=16)

ML = dict(
    slug="metrics-layer",
    kicker="a.k.a. “semantic layer”",
    tldr="Define each business number <b>once, in code</b>: what it sums, which rows it excludes, its time dimension, the dimensions it can be split by, its owner. Dashboards, spreadsheets and notebooks don't write their own SQL for it; they <b>ask the metrics layer</b>, which generates the query, picks the joins safely and computes ratios correctly. Change the definition once and every tool follows.",
    chips=[("Family", "serving reports"), ("Also called", "semantic layer, headless BI"), ("Lives in", "dbt Semantic Layer, Cube, LookML, Malloy"), ("Pairs with", "conformed dimensions, aggregates")],
    problem="""  <p class="lead">For the same week the finance dashboard says revenue was <b>€1.92M</b> (net, after returns), marketing's says <b>€2.31M</b> (gross, including VAT), and a spreadsheet says <b>€2.05M</b> (net, but without gift cards). All three are called “revenue”, and Monday's meeting is spent <span class="hl-pink">arguing about which is right</span>.</p>
  <ul>
    <li>Every tool has its own copy of the SQL, and each drifts.</li>
    <li>Ratios are averaged wrongly (average of averages).</li>
    <li>Nobody knows who owns the definition.</li>
  </ul>""",
    problem_figs=[ml_problem],
    analogy_side="the franchise recipe card",
    analogy="""  <p>Every branch of a burger chain cooks from the same <b>recipe card</b>: same weights, same steps. When head office changes the sauce, it changes the card once, and every branch follows. Branches can choose how to plate it, not what's in it.</p>""",
    analogy_figs=[ml_analogy],
    map=[("The recipe card", "The metric definition in code"),
         ("Head office", "The metric's owner"),
         ("Every branch", "Dashboards, spreadsheets, notebooks, APIs"),
         ("Choosing how to plate", "Choosing dimensions and filters"),
         ("Changing the card once", "One pull request changes revenue everywhere")],
    how_side="one definition, many tools",
    how="""  <p>The layer knows the model: facts, dimensions, how they join (through conformed dimensions), and which measures are additive. A metric is a named measure plus filters and a time dimension. When a tool asks for “revenue by category by week”, the layer writes the SQL, joins only along safe paths (no fan-out), and computes ratios as a ratio of sums, not an average of ratios.</p>""",
    how_figs=[ml_how],
    steps=[("Pick the top ten numbers", "Revenue, orders, average order value, return rate: the ones in meetings."),
           ("Agree each definition", "With its owner: what's in, what's out, net or gross, which date."),
           ("Write them in code", "Measures, filters, time dimension, allowed dimensions, description, owner; reviewed in git."),
           ("Point tools at the layer", "BI tools, spreadsheets and notebooks query it instead of tables."),
           ("Retire copies", "Remove hand-written revenue SQL from dashboards as they move over.")],
    vocab=[("Metric", "A named business number with a fixed definition."),
           ("Measure", "The aggregation behind it (sum of net amount)."),
           ("Dimension", "What you can split a metric by."),
           ("Entity", "A join key the layer uses to connect models (customer, product)."),
           ("Ratio metric", "Numerator and denominator summed first, then divided."),
           ("Headless BI", "Definitions served by an API, independent of the dashboard tool.")],
    code=dict(file="models/metrics/revenue.yml", note="dbt Semantic Layer (MetricFlow)", src="""
semantic_models:
  - name: sales
    model: ref('fct_sales')
    defaults: { agg_time_dimension: order_date }
    entities:
      - { name: order_line, type: primary, expr: order_line_id }
      - { name: product,    type: foreign, expr: product_key }
      - { name: shop,       type: foreign, expr: shop_key }
    dimensions:
      - { name: order_date, type: time, type_params: { time_granularity: day } }
    measures:
      - { name: amount_net, agg: sum }
      - { name: orders,     agg: count_distinct, expr: order_id }

metrics:
  - name: revenue
    label: Revenue (net, after returns, excl. gift cards)
    type: simple
    type_params: { measure: amount_net }
    filter: "{{ Dimension('product__is_gift_card') }} = false"
  - name: average_order_value
    type: ratio                      # sum / count, never an average of averages
    type_params: { numerator: revenue, denominator: orders }
"""),
    tools="tools: dbt Semantic Layer (MetricFlow), Cube, Looker (LookML), Malloy, AtScale, Power BI semantic models; definitions reach Excel, Google Sheets and notebooks through the layer's API or SQL interface.",
    gains=["<b>One number per name</b>, in every tool.",
           "<b>Safe joins and correct ratios</b>, generated for you.",
           "<b>Owned, reviewed definitions</b> with descriptions.",
           "<b>Tool freedom</b>: change dashboards without re-deriving revenue."],
    losses=["<b>Another layer</b> to run and learn.",
            "<b>Not every tool connects</b> well to every layer.",
            "<b>Agreeing definitions</b> is political work.",
            "<b>Unusual questions</b> may need the raw SQL anyway."],
    baseline="Each line compares <b>each dashboard and spreadsheet writing its own revenue SQL</b> to <b>metrics defined once in a metrics layer</b>.",
    ratings=[(2, 4, "One place to read what revenue means."),
             (3, 3, "Neutral."),
             (2, 5, "Same definition, correct ratios, safe joins."),
             (3, 3, "Neutral."),
             (2, 4, "New tools and teams reuse definitions."),
             (3, 3, "A layer to run; fewer duplicate queries."),
             (3, 4, "Any allowed dimension, no SQL needed."),
             (2, 4, "Usage and ownership per metric are visible."),
             (2, 5, "Change a definition once.")],
    pitfalls=[("Metrics layer as a dump", "Four hundred metrics, half of them “revenue_v2_final”.", "start with the numbers in meetings; one owner each; deprecate duplicates."),
              ("Definitions still in dashboards", "The layer exists, but old dashboards keep their own SQL.", "migrate and remove the copies; flag dashboards that bypass the layer."),
              ("Averages of averages", "Average order value averaged across shops gives every shop equal weight.", "define ratios as sums divided, in the layer."),
              ("No business owner", "Engineers decide what revenue means.", "every metric has a named business owner who approves changes.")],
    use=["Several tools or teams report the same numbers.",
         "Numbers are discussed in meetings and disagree.",
         "Ratios and averages are common.",
         "You want self-service without everyone writing SQL."],
    skip=["One dashboard, one analyst.",
          "Exploratory analysis of brand-new data.",
          "Before the underlying model (facts, dimensions) is stable."],
    related=["<b>Conformed dimensions</b>", "<b>Aggregates and rollups</b>", "<b>One big table vs star</b>", "<b>Ubiquitous language</b> (Vol. 7)"],
    quiz=[("What does a metrics layer store?", "Named business metrics defined once in code: measure, filters, time dimension, allowed dimensions, owner."),
          ("How should average order value be computed across shops?", "Total revenue divided by total orders, not the average of each shop's average."),
          ("Why does the layer generate the joins?", "So queries only join along safe paths and don't multiply rows."),
          ("What's the first step in adopting one?", "Agree definitions for the handful of numbers used in meetings, each with an owner.")],
    quiz_sit=[("Marketing wants “revenue” to include VAT, finance wants it net. Both will use the same metrics layer. What do you do?",
               "Define two clearly named metrics, revenue_net (owner: finance) and revenue_gross_incl_vat (owner: marketing), with descriptions, and make dashboards label which one they show. “Revenue” alone points to the company's official one, agreed by finance.")],
    try_it="Search your BI tool and spreadsheets for every place revenue is calculated. Write down each formula. Agree one with its owner, define it in a metrics layer (or a single SQL view if that's what you have), and repoint the two most-used dashboards.",
    remember="One <span class=\"hl\">recipe card</span>. Every branch cooks from it.",
    sources=["dbt documentation, “About MetricFlow” and “Build your metrics”.",
             "Cube documentation, “Data modeling”.",
             "Benn Stancil, “The missing piece of the modern data stack” (2021).",
             "Looker documentation, “LookML terms and concepts”."],
)

# ------------------------------------------------------------------ 16 Aggregates & Rollups
ag_problem = Doodle(760, 260, "Doodle of a slow executive dashboard. Every time it opens it sums 2 billion order lines. It takes 40 seconds, and on Monday at 9 o'clock 300 managers open it at once, the warehouse queues queries and the bill spikes.",
                    "Every open sums 2 billion rows. Monday 09:00, three hundred managers open it at once.")
ag_problem.icon("screen", 40, 50, 1.5)
ag_problem.note(85, 160, "40 s ⏳", "red")
ag_problem.arrow(150, 90, 280, 90, color="red")
ag_problem.table(286, 40, "fct_sales", ["2,000,000,000 rows", "scanned on every open"], w=240, fill="y", stroke="red")
ag_problem.box(580, 40, 160, 90, "× 300", "pink", stroke="red", sub="Monday 09:00", size=22, subsize=15)
ag_problem.note(380, 220, "queued queries, a spiking bill, managers back to spreadsheets", "red")

ag_analogy = Doodle(760, 240, "Doodle of till Z-reports. At closing each till prints a daily summary of its totals. Head office adds up thirty summaries instead of every receipt, and still has the receipts if it needs detail.",
                    "Head office adds up thirty daily till summaries, not every receipt.")
for i in range(5):
    ag_analogy.icon("receipt", 20 + i * 44, 50, 0.9)
ag_analogy.note(130, 160, "thousands of receipts")
ag_analogy.arrow(250, 90, 330, 90)
ag_analogy.box(336, 50, 170, 80, "Z-report", "y", sub="one per till per day", size=21, subsize=14)
ag_analogy.arrow(512, 90, 580, 90)
ag_analogy.box(586, 50, 150, 80, "head office", "green", sub="adds 30 lines", size=19, subsize=14)
ag_analogy.note(380, 210, "receipts are kept for when detail is needed", "pen")

ag_how = Doodle(760, 300, "Aggregates. From fct_sales with 2 billion order lines, a daily table by shop and category is built: about 2 million rows a year. A monthly table by region and category is built from that: a few thousand rows. Each query is answered by the smallest table that has the grain it needs, and only days that changed are rebuilt.",
                 "Each level is built from the one below. Queries go to the smallest table that can answer them.")
ag_how.box(20, 200, 220, 70, "fct_sales", "y", sub="2 B lines", size=21, subsize=15)
ag_how.arrow(246, 225, 290, 160)
ag_how.box(296, 110, 220, 70, "agg_daily", "blue", sub="shop · category · day: 2 M/yr", size=21, subsize=13)
ag_how.arrow(522, 135, 566, 70)
ag_how.box(572, 20, 170, 70, "agg_monthly", "green", sub="region · category", size=20, subsize=13)
ag_how.note(560, 160, "dashboard asks “by month”", "pen", anchor="start", size=16)
ag_how.note(560, 186, "→ reads agg_monthly", "pen", anchor="start", size=16)
ag_how.note(380, 290, "rebuild only the days a batch touched", "green")

AG = dict(
    slug="aggregates-rollups",
    kicker="a.k.a. “summary tables, OLAP cubes”",
    tldr="When dashboards keep summing billions of rows to show the same daily and monthly totals, <b>pre-compute them</b> at coarser grain: sales by shop, category and day; then by region and month. Additive measures (sums, counts) roll up safely; distinct counts need <b>sketches</b> such as HyperLogLog. Rebuild only the periods that changed, and let queries use the <b>smallest table that can answer</b>.",
    chips=[("Family", "serving reports"), ("Also called", "rollups, summary tables, cubes, pre-aggregations"), ("Lives in", "materialized views, ClickHouse, Druid, Cube"), ("Pairs with", "materialized views, fact table types")],
    problem="""  <p class="lead">The executive dashboard sums <b>2 billion order lines</b> every time it opens. It takes 40 seconds; on Monday at 09:00 three hundred managers open it at once, queries queue, and <span class="hl-pink">the warehouse bill spikes</span>. The answers are the same daily totals as an hour ago.</p>""",
    problem_figs=[ag_problem],
    analogy_side="till Z-reports",
    analogy="""  <p>At closing, every till prints a <b>Z-report</b>: the day's totals. Head office adds up thirty Z-reports, not every receipt, and still keeps the receipts in case someone asks about one sale.</p>""",
    analogy_figs=[ag_analogy],
    map=[("The receipts", "The detailed fact table"),
         ("A Z-report per till per day", "An aggregate table at shop · category · day"),
         ("Adding thirty Z-reports", "Querying the aggregate instead of the fact"),
         ("Keeping the receipts", "The detailed fact stays for drill-down"),
         ("Reprinting one day's Z-report", "Rebuilding only changed days")],
    how_side="coarser tables, built from finer ones",
    how="""  <p>Choose grains from the questions: most dashboards ask by day, shop and category, or by month and region. Build each aggregate from the level below it, incrementally by day, and rebuild the days a batch touched (late data). Sums and counts roll up; averages must be stored as sum and count; distinct counts (unique customers) don't add up, so store a HyperLogLog sketch per row and merge sketches.</p>
  <p>Point dashboards at the right level, or let the BI tool or metrics layer pick it automatically (“aggregate awareness”).</p>""",
    how_figs=[ag_how],
    steps=[("Find the slow, frequent queries", "Group them by the dimensions and grain they ask for."),
           ("Design a few aggregates", "Usually daily and monthly, at the dimensions dashboards use."),
           ("Store additive parts", "Sums and counts; sum and count for averages; sketches for distinct counts."),
           ("Refresh incrementally", "Rebuild the days touched by each batch, idempotently."),
           ("Route queries", "Point dashboards at aggregates, or use aggregate awareness; test totals against the fact.")],
    vocab=[("Aggregate table", "A pre-computed summary at a coarser grain."),
           ("Rollup", "Summarising from a fine grain to a coarser one."),
           ("Aggregate awareness", "A tool choosing the smallest table that can answer."),
           ("HyperLogLog", "A small sketch for approximate distinct counts that can be merged."),
           ("OLAP cube", "Pre-aggregated measures over all combinations of dimensions."),
           ("Drill-down", "Going from a summary to the detail behind it.")],
    code=dict(file="agg_sales_daily.sql", note="generic SQL · BigQuery-style HLL", src="""
-- rebuild only the days the latest batch touched
DELETE FROM agg_sales_daily WHERE order_date IN (SELECT d FROM touched_days);
INSERT INTO agg_sales_daily
SELECT order_date, shop_key, category,
       sum(amount_net)                       AS revenue,
       count(*)                              AS lines,
       count(DISTINCT order_id)              AS orders,
       HLL_COUNT.INIT(customer_key)          AS customers_sketch   -- mergeable
FROM   fct_sales JOIN dim_product USING (product_key)
WHERE  order_date IN (SELECT d FROM touched_days)
GROUP  BY 1, 2, 3;

-- monthly, from daily: sums add, sketches merge
SELECT date_trunc(order_date, MONTH) AS month, category,
       sum(revenue) AS revenue,
       HLL_COUNT.MERGE(customers_sketch) AS unique_customers
FROM   agg_sales_daily GROUP BY 1, 2;
"""),
    tools="tools: materialized views (BigQuery, Snowflake, Redshift, PostgreSQL), ClickHouse projections and AggregatingMergeTree, Apache Druid and Pinot rollup at ingestion, Cube pre-aggregations, Looker aggregate awareness, Power BI aggregations, HyperLogLog functions in most warehouses.",
    gains=["<b>Fast dashboards</b>: thousands of rows instead of billions.",
           "<b>Lower cost</b>: scan once per load, not per view.",
           "<b>Predictable load</b> on Monday mornings.",
           "<b>Detail kept</b> for drill-down."],
    losses=["<b>More tables to keep consistent</b> with the fact.",
            "<b>Fixed grains</b>: a new dimension means a new aggregate.",
            "<b>Distinct counts</b> become approximate (sketches).",
            "<b>Refresh lag</b> between fact and aggregate."],
    baseline="Each line compares <b>dashboards summing the detailed fact table every time</b> to <b>incrementally refreshed aggregate tables at the grains they use</b>.",
    ratings=[(4, 3, "More tables, each simple."),
             (3, 3, "Neutral: refreshed with the load."),
             (4, 4, "Totals tested against the fact."),
             (3, 4, "Rebuild touched days from the fact."),
             (2, 5, "Dashboard cost stops growing with history."),
             (2, 5, "Scan once per load, not per view."),
             (4, 3, "Only the dimensions you aggregated by."),
             (3, 3, "Neutral."),
             (3, 3, "New questions may need new aggregates.")],
    pitfalls=[("Averaging averages", "Monthly average order value is the mean of daily averages.", "store revenue and orders; divide at query time."),
              ("Summing distinct counts", "Unique customers per day summed for the month count regulars many times.", "store sketches and merge them, or count from the fact."),
              ("Full rebuild every hour", "The aggregate rereads two billion rows each time.", "rebuild only touched days."),
              ("Aggregate drift", "A fix to the fact is never reflected in the aggregate.", "build aggregates in the same DAG after the fact, and test totals match.")],
    use=["Dashboards that many people open often.",
         "Fixed, common grains (day, month, shop, region).",
         "Very large fact tables.",
         "Cost or latency limits on the warehouse."],
    skip=["Ad-hoc analysis that needs any dimension.",
          "Small facts that scan in a second anyway.",
          "Exact distinct counts that can't be approximate."],
    related=["<b>Materialized views</b> (Vol. 3)", "<b>Fact table types</b>", "<b>Metrics layer</b>", "<b>Late-arriving data</b>"],
    quiz=[("Why can't you sum daily unique customers to get monthly ones?", "Customers who bought on several days would be counted several times; use sketches or count from the fact."),
          ("How should an aggregate store averages?", "As the sum and the count, so averages at any level are computed correctly."),
          ("What is aggregate awareness?", "A tool picking the smallest aggregate table that can answer a query."),
          ("How do aggregates handle late data?", "Rebuild the days a batch touched, the same as the fact.")],
    quiz_sit=[("The regional dashboard needs “unique customers per region per month”, and the fact has 2 billion rows. What do you store in the daily aggregate?",
               "A HyperLogLog sketch of customer keys per shop per day, merged to region and month at query time (or in a monthly aggregate). It's small, mergeable, and accurate to about 1 %, which is usually fine for a dashboard; an exact count can come from the fact when needed.")],
    try_it="Time your slowest dashboard query. Build a daily aggregate for its dimensions, point the query at it, and time it again. Then check that the totals match the fact for a few days.",
    remember="Add up the <span class=\"hl\">Z-reports</span>, keep the <span class=\"hl\">receipts</span>.",
    sources=["Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), on aggregate navigation.",
             "Philippe Flajolet et al., “HyperLogLog” (2007).",
             "Google BigQuery documentation, “HLL functions” and “Materialized views”.",
             "Cube documentation, “Pre-aggregations”."],
)

# ------------------------------------------------------------------ 17 Lambda vs Kappa
lk_problem = Doodle(760, 260, "Doodle of two numbers for one promotion day. Store managers want today's sales live, so a streaming counter was added beside the nightly batch. During the day it shows 48,200 euros; next morning the batch says 46,900 euros, because the stream counted duplicates and missed late events. The logic is written twice, in Java and in SQL.",
                    "Live: €48,200. Next morning: €46,900. Two code paths, two answers.")
lk_problem.box(20, 30, 280, 90, "stream counter", "blue", sub="live · €48,200 · Java", size=20, subsize=14)
lk_problem.box(460, 30, 280, 90, "nightly batch", "y", sub="next day · €46,900 · SQL", size=20, subsize=14)
lk_problem.arrow(306, 75, 454, 75, both=True, color="red", label="≠", lx=380, ly=60)
lk_problem.note(380, 170, "duplicates counted live, late events missed", "red")
lk_problem.note(380, 202, "every rule written twice, in two languages", "red")

lk_analogy = Doodle(760, 240, "Doodle of election night. Television projections are fast and approximate; the official count comes later and is final. That is lambda. Kappa is one count that is published as it goes, and can be recounted from the kept ballots if a counting rule was wrong.",
                    "Election night: fast projections plus an official count, or one count you can redo from the ballots.")
lk_analogy.icon("tv", 40, 40, 1.3)
lk_analogy.note(80, 150, "projection: fast", "pen")
lk_analogy.icon("ledger", 200, 40, 1.3, fill="y")
lk_analogy.note(240, 150, "official: later", "pen")
lk_analogy.note(160, 200, "lambda: two counts", "red")
lk_analogy.icon("box", 470, 40, 1.4, fill="green")
lk_analogy.note(510, 150, "kept ballots", "pen")
lk_analogy.arrow(560, 80, 640, 80)
lk_analogy.box(646, 50, 100, 60, "count", "green", size=20)
lk_analogy.note(600, 200, "kappa: one count, redo from the box", "green")

lk_how = Doodle(760, 300, "Lambda and kappa side by side. Lambda: events go to a batch layer that recomputes everything nightly and a speed layer that covers today; a serving layer merges both. Kappa: events go into a replayable log; one stream job computes results continuously; to change logic, start version two of the job from the beginning of the log, let it catch up, then switch readers.",
                 "Lambda: two paths merged. Kappa: one path, and replay the log to fix it.")
lk_how.head(190, 26, "lambda", size=22)
lk_how.box(20, 50, 130, 56, "events", "y", size=19)
lk_how.box(190, 40, 160, 40, "batch layer", "blue", size=17)
lk_how.box(190, 96, 160, 40, "speed layer", "blue", size=17)
lk_how.box(390, 60, 110, 56, "merge", "paper", size=18)
lk_how.arrow(154, 70, 186, 60)
lk_how.arrow(154, 86, 186, 116)
lk_how.arrow(354, 60, 386, 80)
lk_how.arrow(354, 116, 386, 100)
lk_how.head(190, 186, "kappa", size=22)
lk_how.box(20, 210, 130, 56, "events", "y", size=19)
lk_how.box(190, 210, 160, 56, "replayable log", "green", size=17)
lk_how.box(390, 210, 150, 56, "stream job v1", "green", size=17)
lk_how.box(590, 210, 150, 56, "job v2 replays", "paper", size=17, dash=True)
lk_how.arrow(154, 238, 186, 238)
lk_how.arrow(354, 238, 386, 238)
lk_how.arrow(270, 270, 640, 270, curve=(460, 300), dash=True)
lk_how.note(640, 90, "two codebases", "red")

LK = dict(
    slug="lambda-vs-kappa",
    kicker="a.k.a. “batch plus speed, or one replayable stream”",
    tldr="To get <b>fresh</b> numbers without losing <b>correct</b> ones, <b>lambda</b> runs a batch layer (complete, recomputed) and a speed layer (recent, approximate) and merges them, at the cost of writing every rule twice. <b>Kappa</b> uses one stream job over a <b>replayable log</b>; to fix logic, replay the log through a new version. Today: one code path, stream only if minutes matter, and often a 5–15 minute micro-batch is enough.",
    chips=[("Family", "serving reports"), ("Origin", "Nathan Marz (2011), Jay Kreps (2014)"), ("Lives in", "Kafka, Flink, Spark, streaming warehouses"), ("Pairs with", "late-arriving data, event sourcing")],
    problem="""  <p class="lead">On promotion days the store managers want today's sales live. A streaming counter was added beside the nightly batch. All day it shows <b>€48,200</b>; next morning the batch says <span class="hl-pink">€46,900</span>. The stream counted retried events twice and missed late till uploads, and every rule exists twice: once in Java, once in SQL.</p>""",
    problem_figs=[lk_problem],
    analogy_side="election night",
    analogy="""  <p>On election night, TV <b>projections</b> are fast and approximate, and the <b>official count</b> comes later and is final: two counts, by two teams. Another way: publish <b>one count</b> as ballots are counted, keep every ballot in the box, and if a counting rule was wrong, <b>recount from the box</b> with the corrected rule.</p>""",
    analogy_figs=[lk_analogy],
    map=[("TV projection", "Lambda's speed layer"),
         ("The official count", "Lambda's batch layer"),
         ("Two counting teams", "Two codebases for the same rules"),
         ("Ballots kept in the box", "A replayable log (Kafka with long retention)"),
         ("Recounting with the new rule", "Kappa: replay the log through job v2")],
    how_side="two paths, or one path you can replay",
    how="""  <p><b>Lambda</b>: the batch layer recomputes everything from the master data; the speed layer covers only what the batch hasn't processed yet; a serving layer merges them. Correct in the end, but two implementations that must agree.</p>
  <p><b>Kappa</b>: all events go into a log that keeps them long enough to replay. One stream job uses event time, windows and watermarks, and writes idempotently. To change logic, start version 2 from the start of the log, let it catch up, switch readers, stop version 1.</p>""",
    how_figs=[lk_how],
    steps=[("Ask how fresh it must be", "Seconds? Minutes? If 15 minutes is fine, micro-batch the normal pipeline."),
           ("Keep a replayable log", "Kafka or similar with retention long enough to rebuild (or raw in the warehouse)."),
           ("Write one job, in event time", "Windows and watermarks; allowed lateness; idempotent sink."),
           ("Replay to change logic", "Run v2 from the start beside v1, compare, switch readers."),
           ("Reconcile", "Compare stream results with the warehouse daily; differences mean a bug.")],
    vocab=[("Lambda architecture", "Batch layer + speed layer + serving layer."),
           ("Kappa architecture", "One stream processing path over a replayable log."),
           ("Speed layer", "Approximate, recent results until the batch catches up."),
           ("Replay", "Reprocessing a log from an earlier offset."),
           ("Exactly-once sink", "Output that isn't duplicated after retries."),
           ("Micro-batch", "Running a batch pipeline every few minutes.")],
    code=dict(file="sales_live.sql", note="Flink SQL", src="""
CREATE TABLE till_sales (
  order_line_id BIGINT, shop_id INT, amount DECIMAL(12,2), sold_at TIMESTAMP(3),
  WATERMARK FOR sold_at AS sold_at - INTERVAL '10' MINUTE      -- allowed lateness
) WITH ('connector' = 'kafka', 'topic' = 'till-sales', 'scan.startup.mode' = 'earliest-offset');

-- one job: revenue per shop per 15 minutes, in event time
INSERT INTO shop_revenue_15m                                  -- upsert sink, keyed
SELECT shop_id, window_start, SUM(amount) AS revenue
FROM TABLE(TUMBLE(TABLE till_sales_dedup, DESCRIPTOR(sold_at), INTERVAL '15' MINUTE))
GROUP BY shop_id, window_start;

-- till_sales_dedup: ROW_NUMBER() OVER (PARTITION BY order_line_id ORDER BY sold_at) = 1
"""),
    tools="tools: Apache Kafka (long retention, tiered storage), Apache Flink and Spark Structured Streaming, Kafka Streams, streaming databases and incremental views (Materialize, RisingWave), Snowflake dynamic tables, BigQuery continuous queries, Databricks Delta Live Tables.",
    then_now=dict(src="Marz, 2011 · Kreps, 2014",
                  then="Nathan Marz proposed lambda because Hadoop batch jobs were the only way to be complete and correct, so a separate, approximate speed layer covered the hours they took. Jay Kreps answered with kappa: keep the log and reprocess it with one stream job instead.",
                  now="Stream processors now have event-time windows, watermarks and exactly-once sinks, so one path can be correct. Streaming warehouses and incremental views blur the line further. Many teams find that the normal batch pipeline every 5–15 minutes is all the freshness they need.",
                  verdict="rethought",
                  take="One code path. Stream only if minutes matter, keep the data replayable, and reconcile against the warehouse."),
    gains=["<b>Fresh numbers</b> during the day.",
           "<b>Kappa: one implementation</b> of every rule.",
           "<b>Replay</b> fixes logic for the whole history.",
           "<b>Lambda: batch remains the safety net</b>."],
    losses=["<b>Lambda: rules written twice</b>, and they drift.",
            "<b>Kappa: long log retention</b> and replay time.",
            "<b>Streaming is harder to run</b>: state, checkpoints, lateness.",
            "<b>Often unnecessary</b>: micro-batches would do."],
    baseline="Each line compares <b>a nightly batch with a separate live counter (lambda)</b> to <b>one replayable stream job in event time (kappa)</b>.",
    ratings=[(2, 3, "One path, though streaming concepts are new."),
             (5, 5, "Both are fresh during the day."),
             (3, 4, "One set of rules, event time, dedupe."),
             (4, 4, "Replay the log through a new version."),
             (3, 4, "Stream processors scale out."),
             (2, 3, "No duplicate codebase; streaming infra costs."),
             (3, 3, "Neutral: same outputs."),
             (2, 3, "Lag and watermarks to watch."),
             (2, 4, "Change rules once, replay.")],
    pitfalls=[("Streaming without need", "A Flink cluster for a dashboard people check twice a day.", "micro-batch the normal pipeline every 15 minutes first."),
              ("Processing time windows", "Late till uploads land in the wrong window.", "window by event time with watermarks and allowed lateness."),
              ("Log too short to replay", "Kafka keeps 7 days; the fix needs 90.", "keep raw events in the warehouse or tiered storage long enough to replay."),
              ("No reconciliation", "Live and daily numbers differ by 3 % and nobody knows why.", "compare stream output with the warehouse every day.")],
    use=["Decisions that need numbers within minutes (stock, fraud, promotions).",
         "Events already flowing through a log.",
         "A team able to run stream processing.",
         "Logic that must be identical live and historically."],
    skip=["Freshness of 15 minutes or more is enough: micro-batch.",
          "Reports read once a day.",
          "No replayable source of events."],
    related=["<b>Late-arriving data</b>", "<b>Event sourcing</b> (Vol. 1)", "<b>Change data capture</b> (Vol. 3)", "<b>Idempotent loads</b>"],
    quiz=[("What are lambda's three layers?", "A batch layer, a speed layer and a serving layer that merges them."),
          ("How does kappa change logic for past data?", "By replaying the log from the start through a new version of the job, then switching readers."),
          ("What is lambda's main cost?", "Every rule is implemented twice, and the two drift apart."),
          ("When is neither needed?", "When a batch pipeline run every 5–15 minutes is fresh enough.")],
    quiz_sit=[("Store managers want stock levels “live” on promotion days. Your batch pipeline is idempotent and runs hourly. What do you try first?",
               "Run the same pipeline every 10–15 minutes for the stock tables (micro-batch), and show “as of” on the dashboard. Only if minutes still matter, move the stock calculation to one stream job over the CDC log, with event-time windows and daily reconciliation against the warehouse.")],
    try_it="Write down, for your three most important dashboards, how old the data can be before a decision changes. If every answer is “an hour” or more, schedule the batch more often and stop there.",
    remember="One <span class=\"hl\">count</span>, kept <span class=\"hl\">ballots</span>. Recount when the rule changes.",
    sources=["Nathan Marz and James Warren, <i>Big Data</i> (2015).",
             "Jay Kreps, “Questioning the Lambda Architecture” (O'Reilly, 2014).",
             "Tyler Akidau et al., <i>Streaming Systems</i> (2018).",
             "Apache Flink documentation, “Windowing TVF” and “Deduplication”."],
)

# ------------------------------------------------------------------ 18 Multi-tenant & Embedded Reporting
er_problem = Doodle(760, 260, "Doodle of a leaking shop dashboard. Each shop manager gets a my-shop dashboard that filters on a shop id in the web address. The Delft manager changes shop=12 to shop=13 and sees Leiden's revenue. The same dashboards query the production database and slow down checkout on Saturdays.",
                    "Change shop=12 to shop=13 in the address bar, and you're reading another shop's revenue.")
er_problem.box(20, 40, 340, 60, "…/dashboard?shop=12", "blue", size=19)
er_problem.arrow(366, 70, 414, 70, color="red")
er_problem.box(420, 40, 320, 60, "…/dashboard?shop=13", "pink", stroke="red", size=19)
er_problem.note(580, 130, "Leiden's revenue, seen from Delft", "red")
er_problem.db(190, 160, "production database", w=90)
er_problem.note(500, 200, "and every view queries production:", "red")
er_problem.note(500, 226, "checkout slows on Saturdays", "red")

er_analogy = Doodle(760, 240, "Doodle of apartment mailboxes. One building, one wall of boxes. The postman sorts mail into the boxes; each resident's key opens only their own box. Nobody is handed the whole sack and asked to take only their own letters.",
                    "One wall of mailboxes: each key opens one box. Nobody gets the whole sack.")
for i in range(4):
    er_analogy.box(40 + i * 90, 50, 80, 60, f"{i + 1}", "y" if i != 1 else "green", size=20)
er_analogy.icon("key", 150, 140, 0.8)
er_analogy.note(200, 220, "your key, your box", "green")
er_analogy.icon("bucket", 540, 50, 1.4, color="red")
er_analogy.note(590, 170, "“take your own from the sack”", "red")
er_analogy.note(590, 200, "never", "red")

er_how = Doodle(760, 300, "Safe embedded reporting. The shop manager signs in to the portal. The portal's backend issues a short-lived signed embed token that says shop 12. The reporting layer reads the shop from the token, never from the address, and applies a row-level security policy so every query only sees shop 12's rows. Queries run on the warehouse or a serving store with per-tenant aggregates and caching, not on production.",
                 "The tenant comes from a signed token, and the database enforces it on every row.")
er_how.box(20, 30, 170, 70, "manager", "blue", sub="signs in", size=20, subsize=14)
er_how.arrow(196, 65, 250, 65)
er_how.box(256, 30, 200, 70, "portal backend", "y", sub="token: shop = 12", size=19, subsize=14)
er_how.arrow(462, 65, 516, 65)
er_how.box(522, 30, 220, 70, "reporting layer", "green", sub="reads shop from token", size=19, subsize=14)
er_how.arrow(632, 106, 632, 160)
er_how.box(470, 166, 270, 80, "row-level security", "green", sub="WHERE shop = token.shop", size=19, subsize=14)
er_how.note(220, 180, "warehouse or serving store,", "pen")
er_how.note(220, 206, "per-shop aggregates, cached", "pen")
er_how.note(220, 240, "never production", "red")

ER = dict(
    slug="embedded-reporting",
    kicker="a.k.a. “row-level security for reports”",
    tldr="When customers, shops or franchisees see reports inside your product, each must see <b>only their own rows</b>, and their dashboards mustn't slow the app down. Take the tenant from a <b>signed token</b> issued by your backend, never from the URL; enforce it with <b>row-level security</b> in the data layer, not only in the dashboard; and serve from the <b>warehouse or a serving store</b> with per-tenant aggregates and caching, not from production.",
    chips=[("Family", "serving reports"), ("Also called", "customer-facing analytics, embedded BI"), ("Lives in", "row access policies, signed embedding, Cube"), ("Pairs with", "multitenancy (Vol. 3), least privilege (Vol. 5)")],
    problem="""  <p class="lead">Each shop manager gets a “my shop” dashboard that filters on <code>?shop=12</code> in the address. The Delft manager changes it to <code>13</code> and <span class="hl-pink">sees Leiden's revenue</span>. The same dashboards query the production database, and on Saturdays checkout slows down.</p>
  <ul>
    <li>Tenant filters in the browser are suggestions, not security.</li>
    <li>Every new report must remember to filter, and one will forget.</li>
    <li>Reporting load competes with customers paying.</li>
  </ul>""",
    problem_figs=[er_problem],
    analogy_side="apartment mailboxes",
    analogy="""  <p>An apartment building has <b>one wall of mailboxes</b>. The postman sorts mail into them, and <b>each resident's key opens only their own box</b>. Nobody is handed the whole sack and trusted to take only their own letters.</p>""",
    analogy_figs=[er_analogy],
    map=[("The wall of boxes", "One shared reporting table, all tenants"),
         ("Your key", "A signed token with your tenant id"),
         ("The lock on each box", "A row-level security policy"),
         ("The postman sorting mail", "Per-tenant aggregates built by the pipeline"),
         ("“Take yours from the sack”", "Filtering in the browser: never")],
    how_side="tenant from a token, enforced on every row",
    how="""  <p>Your backend, which knows who signed in, issues a <b>short-lived signed token</b> (a JWT) with the tenant id and the reports allowed. The embedded dashboard passes it to the reporting layer, which sets the tenant for the session. A <b>row-level security policy</b> on the tables then adds the tenant condition to every query, including ones a careless report author writes.</p>
  <p>Serve from the warehouse or a fast serving store, with aggregates per tenant and a cache. Give big tenants their own extracts or limits so one franchisee's export can't slow the others.</p>""",
    how_figs=[er_how],
    steps=[("Put tenant ids on every row", "Shop, franchisee or customer id on facts and aggregates."),
           ("Issue signed embed tokens", "From your backend, with tenant id, allowed reports and a short expiry."),
           ("Enforce row-level security", "A policy in the warehouse or semantic layer that reads the tenant from the session."),
           ("Serve away from production", "Warehouse or serving store; per-tenant aggregates; cache; per-tenant query limits."),
           ("Test the boundary", "An automated test that signs in as shop 12 and tries to read shop 13.")],
    vocab=[("Tenant", "A customer, shop or franchisee whose data must stay separate."),
           ("Row-level security", "A database rule limiting which rows a session can see."),
           ("Signed embedding", "Embedding a report with a token your backend signs."),
           ("Security context", "The tenant and roles attached to a query."),
           ("Serving store", "A fast store for app-facing analytics (ClickHouse, Pinot, Druid)."),
           ("Noisy neighbour", "One tenant's heavy use slowing others.")],
    code=dict(file="row_access.sql + embed.ts", note="Snowflake-style policy · TypeScript", src="""
-- the database enforces the tenant on every query
CREATE ROW ACCESS POLICY shop_only AS (shop_id INT) RETURNS BOOLEAN ->
  shop_id = TRY_TO_NUMBER(CURRENT_SESSION_CONTEXT('shop_id'))   -- set from the token
  OR IS_ROLE_IN_SESSION('HEAD_OFFICE');
ALTER TABLE agg_sales_daily ADD ROW ACCESS POLICY shop_only ON (shop_id);

// the portal backend: the tenant comes from the signed-in user, never the URL
app.get("/reports/embed", requireLogin, (req, res) => {
  const token = jwt.sign(
    { shop_id: req.user.shopId, reports: ["my-shop"], exp: nowSeconds() + 600 },
    process.env.EMBED_SECRET,
  );
  res.json({ url: `${REPORTS_URL}/embed/my-shop#token=${token}` });
});
"""),
    tools="tools: Snowflake row access policies, BigQuery row-level security, PostgreSQL RLS, Cube security context, signed embedding in Metabase, Looker, Power BI Embedded and Superset guest tokens; serving stores ClickHouse, Apache Pinot, Druid.",
    gains=["<b>Tenants see only their own data</b>, whatever the URL says.",
           "<b>Enforced once</b>, in the data layer, for every report.",
           "<b>App stays fast</b>: reports never touch production.",
           "<b>New reports are safe by default</b>."],
    losses=["<b>Token plumbing</b> between app, BI tool and warehouse.",
            "<b>Policies to test</b> on every table and aggregate.",
            "<b>Serving costs</b> for app-facing query volumes.",
            "<b>Cross-tenant questions</b> need a separate, privileged role."],
    baseline="Each line compares <b>dashboards on production filtered by a URL parameter</b> to <b>signed tokens, row-level security and a separate serving layer</b>.",
    ratings=[(3, 3, "One policy instead of a filter in every report."),
             (2, 3, "Warehouse freshness instead of live production."),
             (1, 5, "No tenant can read another's rows."),
             (3, 3, "Neutral."),
             (1, 4, "Report load leaves production; aggregates per tenant."),
             (3, 3, "Serving costs, but no slow checkouts."),
             (3, 3, "Neutral within a tenant."),
             (2, 4, "Access is logged per tenant and token."),
             (2, 4, "New reports inherit the policy.")],
    pitfalls=[("Tenant from the URL or the browser", "Anyone can edit it.", "tenant only from a token your backend signs."),
              ("Filters in each report", "One new report forgets the WHERE and shows everyone's numbers.", "row-level security on the tables, so forgetting is impossible."),
              ("Long-lived tokens", "A token copied into an email works for months.", "expire tokens in minutes and re-issue on page load."),
              ("Shared caches across tenants", "A cached result for shop 12 is served to shop 13.", "include the tenant in every cache key.")],
    use=["Reports shown inside your product to customers or partners.",
         "Internal dashboards where managers must see only their area.",
         "Many tenants on shared tables.",
         "Reporting load that must not touch production."],
    skip=["Head office reporting where everyone may see everything.",
          "A tiny number of tenants with separate databases already.",
          "Data so sensitive it should be physically separate per tenant."],
    related=["<b>Multitenancy</b> (Vol. 3)", "<b>Least privilege</b> (Vol. 5)", "<b>Aggregates and rollups</b>", "<b>Metrics layer</b>"],
    quiz=[("Where must the tenant id come from?", "From a token signed by your backend for the signed-in user, never from the URL or browser."),
          ("Why enforce tenancy with row-level security rather than report filters?", "So every query is filtered, including reports that forget, and nobody can bypass it."),
          ("Why not serve embedded reports from production?", "Report queries compete with the app and slow it down; serve from the warehouse or a serving store."),
          ("What must cache keys include?", "The tenant, so one tenant's cached results are never served to another.")],
    quiz_sit=[("A franchisee asks for a CSV export of “all their sales ever” every morning, and it slows other franchisees' dashboards. What do you do?",
               "Give heavy exports their own path: a nightly per-tenant extract written to storage, or a query queue with per-tenant limits. Dashboards keep using aggregates; the export never competes with them. Row-level security still applies to the export query.")],
    try_it="Open one of your dashboards and look for where the tenant comes from. Try changing it in the address or the request. Then add a test that signs in as one tenant and tries to read another's data, and keep it in CI.",
    remember="Your <span class=\"hl\">key</span>, your <span class=\"hl\">box</span>. Never hand out the sack.",
    sources=["Snowflake documentation, “Understanding row access policies”.",
             "PostgreSQL documentation, “Row security policies”.",
             "Cube documentation, “Security context” and “Multitenancy”.",
             "OWASP, “Broken Object Level Authorization” (API Security Top 10)."],
)

NOTES = [ML, AG, LK, ER]
