# Vol. 9 · Modelling the warehouse: Slowly Changing Dimensions, Fact Table Types, Conformed Dimensions & the Bus
# Matrix, Data Vault, One Big Table vs Star. Same homeware shop; the kettle (product 812) changes category on 12 May.

# ------------------------------------------------------------------ 06 Slowly Changing Dimensions
scd_problem = Doodle(760, 260, "Doodle of a filed report that changed. In April, the March report shows Kitchen revenue of 412 thousand euros. On 12 May the kettle moves to the Small appliances category, and the product dimension is overwritten. Run again in June, the same March report shows Kitchen at 371 thousand euros. Nobody changed March's sales.",
                     "Same March, same sales, a different report: the dimension was overwritten in May.")
scd_problem.box(20, 40, 300, 110, "March report · April", "green", sub="Kitchen €412k", size=19, subsize=17)
scd_problem.box(440, 40, 300, 110, "March report · June", "pink", stroke="red", sub="Kitchen €371k", size=19, subsize=17)
scd_problem.arrow(326, 95, 434, 95, color="red", label="12 May: kettle → Small appliances", lx=380, ly=180)
scd_problem.note(380, 230, "dim_product overwritten · history rewritten", "red")

scd_analogy = Doodle(760, 240, "Doodle comparing a whiteboard and an address book. On the whiteboard, an old address is wiped and the new one written: the old one is gone. In the address book, the old address is crossed out with an end date and the new one written below with a start date: both remain.",
                     "A whiteboard forgets. An address book crosses out and dates.")
scd_analogy.box(20, 40, 300, 140, "whiteboard", "paper", sub="wipe, rewrite", size=21, subsize=16)
scd_analogy.note(170, 210, "type 1: the old value is gone", "red")
scd_analogy.icon("book", 370, 60, 1.4, fill="y")
scd_analogy.note(470, 80, "Utrecht · until 2026-02", "pen", anchor="start")
scd_analogy.note(470, 112, "Rotterdam · from 2026-02", "green", anchor="start")
scd_analogy.note(560, 210, "type 2: both kept, with dates", "green")

scd_how = Doodle(760, 290, "Type 2 in the product dimension. Row with surrogate key 812: SKU K-100 kettle, category Kitchen, valid from 1 September 2025 to 12 May 2026, not current. Row 977: the same SKU, category Small appliances, valid from 12 May 2026, current. The fact row for order 9001, sold 31 March, points at key 812, so March still reports Kitchen.",
                 "Type 2: a new row with a new key for each version. Facts keep the key they were sold under.")
scd_how.table(20, 30, "dim_product", ["812 · K-100 · Kitchen", "  2025-09-01 → 2026-05-12", "977 · K-100 · Small appliances", "  2026-05-12 → ∞ · current"], w=360, fill="y", hl=(2, 3))
scd_how.table(470, 60, "fact_sales", ["line 51 · 2026-03-31", "product_key 812 · €39"], w=270, fill="green")
scd_how.arrow(464, 112, 386, 74)
scd_how.note(570, 220, "lookup: the key valid on the sale date", "pen")
scd_how.note(570, 250, "new sales from 12 May get 977", "pen")

SCD = dict(
    slug="slowly-changing-dimensions",
    kicker="a.k.a. “SCD type 1, type 2”",
    tldr="Dimension values change: a product moves category, a customer moves city. Decide <b>per column</b> what a change means. <b>Type 1</b> overwrites (fix a typo; history follows the new value). <b>Type 2</b> adds a <b>new row with a new surrogate key</b> and valid dates, so old facts keep the label they had. Type 3 keeps a “previous” column; type 6 mixes them. Use type 2 for anything reports group by.",
    chips=[("Family", "modelling"), ("Origin", "Ralph Kimball (1990s)"), ("Lives in", "dbt snapshots, Delta/Iceberg MERGE"), ("Pairs with", "history tables, surrogate keys")],
    problem="""  <p class="lead">In April the March report says Kitchen sold <b>€412k</b>. On 12 May the kettle moves to <i>Small appliances</i> and the product table is copied over the old dimension. In June, the same March report says Kitchen sold <span class="hl-pink">€371k</span>. Nobody touched March's sales.</p>
  <ul>
    <li>Filed reports change without anyone noticing.</li>
    <li>“Sales by region last year” moves customers to where they live now.</li>
    <li>Nobody can answer “what category was it in when we sold it?”</li>
  </ul>""",
    problem_figs=[scd_problem],
    analogy_side="whiteboard vs address book",
    analogy="""  <p>On a <b>whiteboard</b> you wipe the old address and write the new one: the old one is gone. In an <b>address book</b> you cross out the old address with an end date and write the new one underneath with a start date. Letters sent last year still went to the old address, and you can see that.</p>""",
    analogy_figs=[scd_analogy],
    map=[("Wiping the whiteboard", "Type 1: <code>UPDATE dim SET category = …</code>"),
         ("Crossing out with a date", "Type 2: close the old row (<code>valid_to</code>), insert a new one"),
         ("A new line in the book", "A new surrogate key for the new version"),
         ("Letters sent last year", "Old facts keep the old key"),
         ("“Previous address” box", "Type 3: a <code>previous_category</code> column")],
    how_side="one new row per version, facts keep their key",
    how="""  <p>A type 2 dimension has a <b>surrogate key</b> per version, the source's natural key (the SKU), and <code>valid_from</code>, <code>valid_to</code> and <code>is_current</code>. When a tracked column changes, the load closes the current row and inserts a new one. When a fact is loaded, it looks up the version that was valid at the event time, and keeps that key forever.</p>""",
    how_figs=[scd_how],
    steps=[("Classify every column", "Type 1 (corrections, descriptions), type 2 (anything reports group or filter by), or type 0 (never changes, e.g. original signup date)."),
           ("Add version columns", "Surrogate key, natural key, <code>valid_from</code>, <code>valid_to</code>, <code>is_current</code>."),
           ("Detect changes", "Compare tracked columns (or a hash of them) with the current row on each load."),
           ("Close and insert", "Set <code>valid_to</code> on the old row, insert the new one with a new key, in one transaction."),
           ("Look up by event time", "Facts join on the natural key where the sale time is between <code>valid_from</code> and <code>valid_to</code>.")],
    vocab=[("Type 0", "Keep the original value forever."),
           ("Type 1", "Overwrite; history follows the new value."),
           ("Type 2", "New row and key per version, with valid dates."),
           ("Type 3", "A column for the previous value."),
           ("Type 6", "Type 2 rows plus a current-value column on every row (1 + 2 + 3)."),
           ("Natural key", "The source's id for the thing (SKU), shared by all versions.")],
    code=dict(file="snapshots/products_snapshot.sql + fact lookup", note="dbt · generic SQL", src="""
{% snapshot products_snapshot %}
{{ config(unique_key='sku', strategy='check',
          check_cols=['category', 'brand', 'name']) }}   -- type 2 columns
select sku, name, brand, category from {{ ref('stg_products') }}
{% endsnapshot %}

-- fact load: the version valid when it was sold
select s.order_line_id, p.product_key, s.amount
from   stg_order_lines s
join   dim_product p
  on   p.sku = s.sku
 and   s.sold_at >= p.valid_from
 and   s.sold_at <  coalesce(p.valid_to, '9999-12-31')
"""),
    tools="tools: dbt snapshots (timestamp or check strategy), Delta Lake and Iceberg MERGE, Snowflake streams and tasks, SQL Server temporal tables as a source, AutomateDV.",
    then_now=dict(src="Kimball, 1996",
                  then="<i>The Data Warehouse Toolkit</i> named types 1, 2 and 3 and set out how to load them in ETL code, with surrogate keys generated by the ETL server and careful hand-written change detection.",
                  now="The idea is unchanged and everywhere. dbt snapshots and MERGE build type 2 in a few lines; temporal tables and CDC give the history for free; columnar storage makes the extra rows cheap. Some teams skip type 2 dimensions and join facts to a full history table at query time instead.",
                  verdict="core",
                  take="Still the way to keep reports stable as the business reorganises. Decide per column, and default to type 2 for anything people group by."),
    gains=["<b>Filed reports stay filed</b>: March is March forever.",
           "<b>Both views</b>: “as it was” and, with type 6, “as it is now”.",
           "<b>Audit</b>: you can say when a category changed.",
           "<b>Cheap</b>: dimensions are small; extra rows cost little."],
    losses=["<b>More complex loads</b>: change detection, closing rows.",
            "<b>Lookups by date</b> are easy to get wrong (boundaries).",
            "<b>Surprise for users</b>: “why is the kettle in two categories?”",
            "<b>Fast-changing columns</b> explode the row count."],
    baseline="Each line compares <b>a dimension copied over the old one every night (type 1 only)</b> to <b>per-column type 1 and type 2 with surrogate keys</b>.",
    ratings=[(4, 3, "Versions and valid dates to understand."),
             (3, 3, "Neutral."),
             (2, 5, "Past reports keep their labels."),
             (3, 4, "History lives in the dimension, not in last night's copy."),
             (4, 4, "Dimensions stay small; facts unchanged."),
             (4, 4, "A few extra rows."),
             (2, 4, "Ask “as it was” or “as it is now”."),
             (2, 4, "Changes are visible, with dates."),
             (3, 3, "New tracked columns need a decision each.")],
    pitfalls=[("Type 2 on everything", "A last-login column creates a new customer version every day.", "type 2 only for columns people group or filter by; move fast-changing ones to a fact or a mini-dimension."),
              ("Joining facts on the natural key", "Every fact matches every version and sales are multiplied.", "store the surrogate key on the fact, or join with the date range."),
              ("Overlapping or gapped dates", "A sale at exactly midnight matches two versions, or none.", "half-open ranges: <code>&gt;= valid_from AND &lt; valid_to</code>, and test for overlaps."),
              ("Late-arriving changes", "A category change is backdated after facts were loaded with the old key.", "re-key affected facts, or accept the change from its load date; decide with the business.")],
    use=["Categories, regions, segments, price bands: anything reports group by.",
         "Reports that are filed, audited or compared year on year.",
         "Dimensions that change slowly (weekly or less).",
         "Regulated reporting that must be reproducible."],
    skip=["Typos and corrections: type 1.",
          "Values that change every day: model them as facts.",
          "Small reports where “as it is now” is all anyone asks."],
    related=["<b>History tables</b> (Vol. 3)", "<b>Bitemporal data</b> (Vol. 3)", "<b>Surrogate keys</b> (Vol. 3)", "<b>Conformed dimensions</b>"],
    quiz=[("What does a type 2 change do?", "Closes the current dimension row and inserts a new one with a new surrogate key and valid dates."),
          ("Why do facts store the surrogate key, not the natural key?", "The surrogate key names one version; the natural key matches every version and multiplies rows."),
          ("When is type 1 right?", "For corrections and descriptions where the past should show the fixed value."),
          ("What is type 6?", "Type 2 rows that also carry the current value on every row, so reports can choose “as it was” or “as it is now”.")],
    quiz_sit=[("Regional managers want last year's sales by the region each shop belongs to now, but finance wants them by the region at the time. One dimension, two answers. What do you build?",
               "A type 6 shop dimension: type 2 rows with the historical region, plus a current_region column updated on every version. Finance groups by region, managers by current_region, both from the same fact table.")],
    try_it="Make a three-row product dimension with type 2 columns, a fact table pointing at it, and a monthly report. Change one product's category, apply type 1, and rerun the report for an old month. Undo, apply type 2, and rerun.",
    remember="Cross it out and <span class=\"hl\">date it</span>. Facts remember the <span class=\"hl\">key they were sold under</span>.",
    sources=["Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), chapter 5.",
             "Kimball Group, “Slowly Changing Dimension Techniques” (design tips).",
             "dbt documentation, “Snapshots”.",
             "Databricks documentation, “SCD type 2 with MERGE”."],
)

# ------------------------------------------------------------------ 07 Fact Table Types
ft_problem = Doodle(760, 260, "Doodle of three questions asked of one sales fact table. Stock on hand at the end of each month needs summing every movement for five years in every query. Days from order to delivery needs joining four status tables to themselves. Which promotions sold nothing has no rows at all to count. All three are slow or impossible.",
                    "Three questions, one transaction table: slow, painful, or impossible.")
ft_problem.table(280, 90, "fact_sales", ["one row per order line"], w=220, fill="y")
ft_problem.box(10, 20, 240, 60, "stock at month end?", "pink", stroke="red", size=17)
ft_problem.box(520, 20, 230, 60, "order → delivery days?", "pink", stroke="red", size=16)
ft_problem.box(260, 190, 260, 60, "promos that sold nothing?", "pink", stroke="red", size=16)
ft_problem.arrow(250, 60, 300, 100, color="red")
ft_problem.arrow(520, 60, 480, 100, color="red")
ft_problem.arrow(390, 186, 390, 152, color="red")
ft_problem.note(130, 120, "sum 5 years of moves", "red", size=15)
ft_problem.note(640, 120, "4 self-joins", "red", size=15)

ft_analogy = Doodle(760, 250, "Doodle of four bank documents. A transaction list shows each payment. A monthly statement shows the balance at month end. A mortgage application tracker shows one line per application with the dates of each milestone. A class register shows who attended, with no amounts at all.",
                    "Payments, the monthly balance, the application tracker, the class register.")
ft_analogy.row([("transactions", "each payment", "y"), ("statement", "balance each month", "blue"), ("tracker", "one line, milestones", "green"), ("register", "who was there", "paper")], y=50, h=100, gap=16, size=18, subsize=14)
ft_analogy.note(380, 200, "four documents, four kinds of question", "pen")

ft_how = Doodle(760, 300, "Four fact table types. Transaction: one row per order line, amounts add up across everything. Periodic snapshot: one row per product per shop per month, stock on hand, which adds across shops but not across months. Accumulating snapshot: one row per order, updated as it is paid, picked, shipped and delivered, with a date per milestone and lags. Factless: one row per product on promotion per day, with no measure.",
                 "Pick the type by the question. Grain first, then measures.")
ft_how.table(20, 20, "fct_sales", ["grain: order line", "qty · amount (add)"], w=340, fill="y")
ft_how.table(400, 20, "fct_stock_monthly", ["grain: product · shop · month", "on_hand (not across months)"], w=340, fill="blue")
ft_how.table(20, 160, "fct_order_lifecycle", ["grain: order (updated)", "paid · shipped · delivered dates"], w=340, fill="green")
ft_how.table(400, 160, "fct_promo_coverage", ["grain: product · promo · day", "no measure"], w=340, fill="paper")

FT = dict(
    slug="fact-table-types",
    kicker="a.k.a. “transaction, snapshot, accumulating, factless”",
    tldr="Not every question is a sum of events. <b>Transaction</b> facts store one row per event (sales lines). <b>Periodic snapshots</b> store the state of something each period (stock at month end). <b>Accumulating snapshots</b> store one row per process instance, updated at each milestone (order placed → delivered). <b>Factless</b> facts record that something happened or applied, with no number (products on promotion). Start every fact table by writing down its <b>grain</b>.",
    chips=[("Family", "modelling"), ("Origin", "Kimball dimensional modelling"), ("Key word", "grain"), ("Pairs with", "star schema, aggregates")],
    problem="""  <p class="lead">The shop has one fact table: order lines. Then three questions arrive. <b>Stock on hand at each month end</b> means summing five years of stock movements in every query. <b>Days from order to delivery</b> means joining four status tables to themselves. <b>Promotions that sold nothing</b> has <span class="hl-pink">no rows to count</span>, because nothing was sold.</p>""",
    problem_figs=[ft_problem],
    analogy_side="four bank documents",
    analogy="""  <p>Your bank gives you four kinds of document. A <b>transaction list</b> (every payment), a <b>monthly statement</b> (the balance on the last day), an <b>application tracker</b> for your mortgage (one line, with the date of each step), and, at school, a <b>class register</b> (who was there, no amounts). Each answers different questions, and you wouldn't compute your balance from twenty years of payments every time.</p>""",
    analogy_figs=[ft_analogy],
    map=[("Transaction list", "Transaction fact: one row per order line"),
         ("Monthly statement", "Periodic snapshot: stock per product per shop per month"),
         ("Application tracker", "Accumulating snapshot: one row per order, milestone dates"),
         ("Class register", "Factless fact: product on promotion per day"),
         ("“Balance” can't be added across months", "Semi-additive measure")],
    how_side="choose by the question, state the grain",
    how="""  <p>The <b>grain</b> says what one row is. Write it down before choosing columns: “one row per order line”, “one row per product per shop per month”, “one row per order”. Measures must fit the grain, and the type follows from the question. Transaction measures add up across everything. Snapshot balances add across shops but not across time (average or take the last). Accumulating rows are <b>updated</b> as milestones happen, so they need idempotent merges.</p>""",
    how_figs=[ft_how],
    steps=[("Write the grain", "One sentence: “one row per …”. If you can't, the table isn't designed yet."),
           ("Pick the type from the question", "Events → transaction; state over time → periodic snapshot; a process with steps → accumulating; coverage or attendance → factless."),
           ("Add dimensions at that grain", "Date, product, shop, customer, promotion."),
           ("Mark measure additivity", "Additive, semi-additive (balances), non-additive (ratios: store the parts)."),
           ("Load accordingly", "Append or merge; snapshot each period; update milestones; insert coverage rows.")],
    vocab=[("Grain", "What one fact row represents."),
           ("Additive", "Can be summed across every dimension (amount)."),
           ("Semi-additive", "Sums across some dimensions, not time (stock on hand)."),
           ("Non-additive", "Can't be summed (a ratio); store numerator and denominator."),
           ("Lag", "Days between two milestones in an accumulating row."),
           ("Coverage table", "A factless fact recording what applied, e.g. promotions.")],
    code=dict(file="fact_tables.sql", note="generic warehouse DDL", src="""
-- periodic snapshot: state at the end of each month
CREATE TABLE fct_stock_monthly (
  month_key int, product_key int, shop_key int,
  on_hand int,               -- semi-additive: sum across shops, not months
  on_order int
);

-- accumulating snapshot: one row per order, updated at each milestone
CREATE TABLE fct_order_lifecycle (
  order_id bigint PRIMARY KEY,
  placed_date_key int, paid_date_key int, shipped_date_key int, delivered_date_key int,
  days_to_ship int, days_to_deliver int,
  order_amount numeric
);

-- factless: which products were on which promotion, each day
CREATE TABLE fct_promo_coverage (date_key int, product_key int, promo_key int, shop_key int);

-- “promoted but sold nothing” = coverage EXCEPT sales
SELECT date_key, product_key, promo_key FROM fct_promo_coverage
EXCEPT
SELECT date_key, product_key, promo_key FROM fct_sales;
"""),
    tools="tools: any warehouse; dbt incremental models for snapshots (one partition per period) and merges for accumulating rows; BI tools need semi-additive measures declared (LookML, Power BI, Cube).",
    then_now=dict(src="Kimball &amp; Ross, 2002",
                  then="The second edition of <i>The Data Warehouse Toolkit</i> set out the three fact table types plus factless facts as the core of dimensional design, built because summing raw transactions was too slow on row stores.",
                  now="Columnar engines can sum billions of transactions quickly, so some snapshots are now views over transactions. But the questions haven't changed: balances still can't be summed over time, and processes still have milestones. Metrics layers now ask you to declare the same additivity rules.",
                  verdict="core",
                  take="Still the vocabulary every analytics engineer needs. Write the grain first, every time."),
    gains=["<b>Each question gets a fast, natural shape</b>.",
           "<b>Clear grain</b> stops double counting.",
           "<b>Process metrics</b> (lags) become one column.",
           "<b>“What didn't happen”</b> becomes answerable."],
    losses=["<b>More tables</b> to build and explain.",
            "<b>Snapshots duplicate</b> state every period.",
            "<b>Accumulating rows are updated</b>, so loads must merge.",
            "<b>Semi-additive traps</b> for unaware users."],
    baseline="Each line compares <b>answering every question from one transaction fact</b> to <b>a fact table of the right type per question</b>.",
    ratings=[(3, 3, "More tables, but each one is obvious."),
             (3, 3, "Neutral."),
             (2, 4, "Grain and additivity are explicit."),
             (3, 4, "Snapshots per period rebuild independently."),
             (2, 4, "No five-year scans for a month-end number."),
             (3, 3, "Snapshots cost storage, save compute."),
             (2, 5, "Balances, lags and gaps are all askable."),
             (3, 3, "Neutral."),
             (3, 4, "New processes get their own table.")],
    pitfalls=[("Mixed grain", "Order-level shipping cost stored on every order line, then summed.", "store measures only at their own grain, or allocate them explicitly."),
              ("Summing balances over time", "“Total stock in Q1” adds three month-ends together.", "declare on_hand semi-additive; use last or average over time."),
              ("Ratios stored as facts", "Average margin per line is averaged again in the report.", "store the parts (revenue, cost) and divide at query time."),
              ("Accumulating rows appended", "Each milestone adds a new row, and orders are counted four times.", "merge on the order id; one row per order.")],
    use=["Any new fact table: start with the grain.",
         "Balances and levels: stock, account balances, headcount.",
         "Processes with steps: orders, claims, tickets, onboarding.",
         "Coverage or eligibility: promotions, rosters, enrolments."],
    skip=["When one transaction fact and a fast engine already answer the question well.",
          "Processes with many loops and unknown steps: an event table fits better.",
          "Snapshots nobody reads; generate them on demand from transactions."],
    related=["<b>Star schema</b> (Vol. 3)", "<b>Aggregates and rollups</b>", "<b>Idempotent loads</b>", "<b>Metrics layer</b>"],
    quiz=[("What is the grain of a fact table?", "A precise statement of what one row represents, e.g. one row per order line."),
          ("Why can't you sum stock on hand across months?", "It is a balance (semi-additive): each month-end repeats the stock; take the last or the average over time."),
          ("How does an accumulating snapshot change over time?", "Its row for each order is updated as milestones happen, filling in dates and lags."),
          ("How do you find promotions that sold nothing?", "Compare a factless coverage table with the sales fact: coverage rows with no matching sales.")],
    quiz_sit=[("Customer service wants “average days from order to delivery, by carrier, by week”. Today they join orders to four status tables and it takes minutes. What do you build?",
               "An accumulating snapshot, fct_order_lifecycle: one row per order with a date key per milestone and days_to_deliver, merged on order_id as statuses arrive. The question becomes an average of one column grouped by carrier and week.")],
    try_it="Take your sales table and write its grain in one sentence. Then write the grain for “stock at month end” and for “order to delivery”. If either needs a new table, sketch its columns and mark each measure additive, semi-additive or non-additive.",
    remember="<span class=\"hl\">Grain first</span>. Payments, balances, trackers and registers are different documents.",
    sources=["Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), chapters 2–4.",
             "Kimball Group, “Fact Tables” and “Factless Fact Tables” design tips.",
             "Cube and LookML documentation on non-additive and semi-additive measures.",
             "Christopher Adamson, <i>Star Schema: The Complete Reference</i> (2010)."],
)

# ------------------------------------------------------------------ 08 Conformed Dimensions & Bus Matrix
cd_problem = Doodle(760, 260, "Doodle of two marts that can't be combined. The sales mart has a product dimension from the ERP with category Kitchen. The web mart built its own product dimension from the website's catalogue with category Kitchenware. Return rate by category, combining both, gives mismatched rows and a question mark.",
                    "Two teams, two product dimensions: “Kitchen” here, “Kitchenware” there, and no way to combine.")
cd_problem.table(20, 40, "sales: dim_product", ["K-100 · Kitchen"], w=260, fill="y")
cd_problem.table(480, 40, "web: dim_product_cms", ["kettle-k100 · Kitchenware"], w=260, fill="blue")
cd_problem.box(270, 160, 220, 70, "return rate?", "pink", stroke="red", size=20)
cd_problem.arrow(150, 106, 270, 180, color="red")
cd_problem.arrow(610, 106, 490, 180, color="red")
cd_problem.note(380, 120, "different keys, different names", "red")

cd_analogy = Doodle(760, 240, "Doodle of city maps that share one key. The transport map, the bike map and the tourist map all use the same district names and the same symbols, so you can lay one over another and they line up.",
                    "Maps that share one key and one set of district names line up when you overlay them.")
for i, t in enumerate(["transport", "bikes", "tourist"]):
    cd_analogy.icon("map", 60 + i * 150, 50, 1.3)
    cd_analogy.note(100 + i * 150, 150, t)
cd_analogy.box(520, 50, 220, 100, "one key", "green", sub="same names, same symbols", size=21, subsize=14)
cd_analogy.note(380, 210, "overlay any two: they line up", "pen")

cd_how = Doodle(760, 300, "A bus matrix. Rows are business processes: sales, returns, web sessions and stock. Columns are conformed dimensions: date, product, customer and shop. A cross marks each dimension a process uses. Every fact table uses the same shared dimension tables, so any two processes can be compared by the attributes they share.",
                 "The bus matrix: processes down, shared dimensions across. One product dimension for all.")
cols = ["date", "product", "customer", "shop"]
rows = [("sales", "XXXX"), ("returns", "XXXX"), ("web sessions", "XXX."), ("stock", "XX.X")]
for i, c in enumerate(cols):
    cd_how.head(270 + i * 120, 40, c, size=19)
for r, (name, marks) in enumerate(rows):
    y = 70 + r * 52
    cd_how.box(20, y, 180, 44, name, "y", size=18)
    for i, m in enumerate(marks):
        cd_how.box(220 + i * 120, y, 100, 44, "✕" if m == "X" else "", "green" if m == "X" else "paper", size=20)
cd_how.note(380, 292, "drill across: aggregate each fact separately, then join on shared attributes", "pen", size=16)

CD = dict(
    slug="conformed-dimensions",
    kicker="a.k.a. “one product, one customer, one calendar”",
    tldr="Build each dimension <b>once</b> (date, product, customer, shop) and share it across every fact table: sales, returns, web sessions, stock. Then any two processes can be compared by the attributes they share. Plan it with a <b>bus matrix</b>: business processes as rows, shared dimensions as columns. Combine facts by <b>drilling across</b>: aggregate each fact on its own, then join the results on the shared attributes.",
    chips=[("Family", "modelling"), ("Origin", "Kimball's enterprise data warehouse bus (1990s)"), ("Tool", "the bus matrix"), ("Pairs with", "bounded context, metrics layer")],
    problem="""  <p class="lead">The sales team built <code>dim_product</code> from the ERP; the web team built its own from the website catalogue. The kettle is <i>Kitchen</i> in one and <i>Kitchenware</i> in the other, with different ids. “Return rate by category” combines both, and <span class="hl-pink">nothing lines up</span>.</p>
  <ul>
    <li>Each mart answers its own questions; none can be combined.</li>
    <li>The same customer has three ids in three marts.</li>
    <li>Every cross-team question becomes a one-off mapping project.</li>
  </ul>""",
    problem_figs=[cd_problem],
    analogy_side="maps with one key",
    analogy="""  <p>A city's transport map, bike map and tourist map share <b>one key</b>: the same district names and the same symbols. Lay one over another and they line up. If each map named the districts its own way, you couldn't plan a bike-and-tram trip.</p>""",
    analogy_figs=[cd_analogy],
    map=[("The shared key", "Conformed dimensions"),
         ("Each themed map", "A fact table for one business process"),
         ("District names", "Shared attributes: category, region, month"),
         ("Overlaying two maps", "Drilling across: compare two facts"),
         ("The list of maps and what each shows", "The bus matrix")],
    how_side="shared dimensions, planned on one grid",
    how="""  <p>Pick the business processes (rows) and the dimensions they share (columns). Build each column once, owned by one team, with one surrogate key and one set of attributes. A coarser fact (stock by month and category) uses a <b>shrunken</b> dimension that is a strict subset (<code>dim_month</code>, <code>dim_category</code>), so it still conforms.</p>
  <p>To compare processes, never join two fact tables row to row (that multiplies rows). Aggregate each fact to the shared attributes first, then join the small results.</p>""",
    how_figs=[cd_how],
    steps=[("List business processes", "Sales, returns, web sessions, stock: each becomes a fact table."),
           ("Draw the bus matrix", "Mark which dimensions each process needs."),
           ("Build each dimension once", "One owner, one key, one set of attribute names and values; map sources to it."),
           ("Shrink, don't fork", "Coarser grains use subsets (month, category) of the same dimension."),
           ("Drill across", "Aggregate each fact separately, join on shared attributes.")],
    vocab=[("Conformed dimension", "A dimension shared, identically, by several facts."),
           ("Bus matrix", "Processes × dimensions grid, used to plan a warehouse."),
           ("Drill across", "Combining results from two facts via shared attributes."),
           ("Shrunken dimension", "A conformed subset at a coarser grain (month, category)."),
           ("Fan-out", "Rows multiplied by joining two facts directly."),
           ("Master data", "The agreed, cleaned version of core entities across systems.")],
    code=dict(file="return_rate_by_category.sql", note="drill across", src="""
with sales as (
    select p.category, sum(f.qty) as sold
    from fct_sales f join dim_product p using (product_key)
    where f.date_key between 20260101 and 20260331
    group by 1
),
returns as (
    select p.category, sum(r.qty) as returned
    from fct_returns r join dim_product p using (product_key)   -- the same dimension
    where r.date_key between 20260101 and 20260331
    group by 1
)
select s.category, s.sold, coalesce(r.returned, 0) as returned,
       round(100.0 * coalesce(r.returned, 0) / s.sold, 1) as return_rate_pct
from sales s left join returns r using (category);
"""),
    tools="tools: dbt (one model per dimension, referenced by every mart), metrics layers that join facts through shared dimensions (dbt Semantic Layer, Cube, LookML explores), master data tools for the source mapping.",
    then_now=dict(src="Kimball, 1998",
                  then="<i>The Data Warehouse Lifecycle Toolkit</i> introduced the bus architecture: build marts one process at a time, but on conformed dimensions agreed up front, recorded in a bus matrix.",
                  now="More sources and more teams make it matter more: SaaS tools, web events and acquisitions each bring their own customer and product. Metrics layers rely on conformed dimensions to join facts safely, and data mesh teams publish them as shared data products.",
                  verdict="grown",
                  take="Agree the shared dimensions before the second fact table. The bus matrix is still the cheapest planning tool in analytics."),
    gains=["<b>Cross-process questions</b> just work.",
           "<b>One definition</b> of category, region, customer.",
           "<b>Incremental build</b>: add processes one at a time.",
           "<b>Safe joins</b> through shared attributes."],
    losses=["<b>Agreement takes time</b> between teams.",
            "<b>A shared owner</b> becomes a dependency.",
            "<b>Source mapping</b> (ERP id to web id) is real work.",
            "<b>Changes ripple</b> to every mart that uses the dimension."],
    baseline="Each line compares <b>each mart with its own dimensions</b> to <b>conformed dimensions shared through a bus matrix</b>.",
    ratings=[(3, 4, "One product, one customer, one calendar."),
             (3, 3, "Neutral."),
             (2, 5, "Cross-team numbers agree."),
             (3, 3, "Neutral."),
             (2, 4, "New processes plug into existing dimensions."),
             (3, 3, "Less duplication, more coordination."),
             (2, 5, "Any two processes can be compared."),
             (3, 3, "Neutral."),
             (3, 3, "Changes need agreement, but happen once.")],
    pitfalls=[("Joining two facts directly", "Sales joined to returns on product multiplies rows and doubles totals.", "aggregate each fact first, then join (drill across)."),
              ("“Almost conformed”", "The web team adds two extra categories, so totals differ by a few percent.", "a shrunken or extended dimension must map exactly; test that sums match."),
              ("No owner", "Everyone edits dim_customer and it drifts.", "one owning team; others request changes."),
              ("Waiting for the perfect model", "A year of meetings before the first mart.", "agree the matrix and the first two dimensions, then build process by process.")],
    use=["Two or more business processes share dimensions.",
         "Several teams build marts.",
         "Data comes from several source systems for the same entities.",
         "You want a metrics layer to join facts safely."],
    skip=["One fact table, one team: just build the star.",
          "Exploration sandboxes that will be thrown away.",
          "Forcing unrelated domains to share a dimension they don't share."],
    related=["<b>Star schema</b> (Vol. 3)", "<b>Bounded context</b> (Vol. 7)", "<b>Metrics layer</b>", "<b>Slowly changing dimensions</b>"],
    quiz=[("What makes a dimension conformed?", "It is shared, identically (same keys, attributes and values), by several fact tables."),
          ("What is a bus matrix?", "A grid of business processes against shared dimensions, marking which process uses which dimension."),
          ("Why not join two fact tables directly on product?", "Each side has many rows per product, so the join multiplies rows; aggregate each side first."),
          ("What is a shrunken dimension?", "A conformed subset at a coarser grain, such as month from date or category from product.")],
    quiz_sit=[("The shop buys a second chain whose product codes differ from yours. Management wants combined sales by category next month. What do you do?",
               "Keep one dim_product as the conformed dimension. Map the new chain's codes to it (or add its products with your category values) in staging, owned by the dimension's team, and load the new chain's sales into the same fct_sales. Test that category totals match the new chain's own reports.")],
    try_it="Draw a bus matrix for your own data: four business processes down the side, five dimensions across. Mark the crosses. Circle every dimension that exists twice today under different names.",
    remember="One <span class=\"hl\">key</span> for every map. Aggregate first, <span class=\"hl\">then</span> compare.",
    sources=["Ralph Kimball et al., <i>The Data Warehouse Lifecycle Toolkit</i> (1998; 2nd ed. 2008).",
             "Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), chapter 4.",
             "Kimball Group, “The Matrix: Revisited” (design tip).",
             "dbt Labs, “The dbt Semantic Layer: joins through entities”."],
)

# ------------------------------------------------------------------ 09 Data Vault
dv_problem = Doodle(760, 260, "Doodle of a star schema under pressure from many sources. The shop's ERP, web store, CRM, loyalty app and an acquired chain's ERP all feed customers into one dim_customer. Every new source or changed source forces the dimension and its load to be rewritten. The auditor asks what the CRM said about customer 77 on 1 March, and nobody can say.",
                    "Five sources, one dimension rewritten every time one changes, and no answer for the auditor.")
for i, t in enumerate(["ERP", "web", "CRM", "loyalty", "chain B"]):
    dv_problem.box(20, 10 + i * 48, 120, 40, t, "blue", size=17)
    dv_problem.arrow(146, 30 + i * 48, 300, 120, color="red" if i == 4 else "")
dv_problem.table(306, 90, "dim_customer", ["rewritten again"], w=200, fill="y", stroke="red")
dv_problem.note(640, 80, "“what did the CRM", "red")
dv_problem.note(640, 104, "say on 1 March?”", "red")
dv_problem.note(640, 160, "nobody knows", "red")

dv_analogy = Doodle(760, 250, "Doodle of a library card catalogue. One card per book, identified by ISBN, never changes. Cross-reference cards link a book to its author. Dated annotation slips from each librarian are pinned behind a book's card, never erased, only added.",
                    "One card per book, cross-reference cards, and dated slips that are only ever added.")
dv_analogy.box(30, 60, 200, 100, "book card", "y", sub="ISBN only", size=21, subsize=16)
dv_analogy.box(290, 60, 180, 100, "cross-ref", "blue", sub="book ↔ author", size=21, subsize=16)
dv_analogy.box(530, 40, 210, 50, "slip · 2024 · Ann", "green", size=16)
dv_analogy.box(530, 100, 210, 50, "slip · 2026 · Raj", "green", size=16)
dv_analogy.arrow(236, 110, 284, 110, both=True)
dv_analogy.arrow(526, 90, 476, 100)
dv_analogy.note(380, 220, "never erased, only added", "pen")

dv_how = Doodle(760, 310, "A small data vault. Hub customer holds only the business key, customer number, with a hash key, load date and source. Hub order likewise. A link joins order and customer hashes. Satellites hang off the customer hub: one with CRM attributes such as name and city, one with loyalty attributes such as tier, each insert-only with a load date. Stars for reporting are built on top.",
                 "Hubs hold keys, links hold relationships, satellites hold dated details. Stars sit on top.")
dv_how.table(10, 20, "sat_customer_crm", ["name · city · load_date"], w=230, fill="green")
dv_how.table(10, 130, "sat_customer_loyalty", ["tier · load_date"], w=230, fill="green")
dv_how.table(280, 20, "hub_customer", ["customer_hk · customer_no", "load_date · source"], w=240, fill="y")
dv_how.table(280, 170, "link_order_customer", ["order_hk · customer_hk"], w=240, fill="blue")
dv_how.table(560, 170, "hub_order", ["order_hk · order_no", "load_date · source"], w=190, fill="y")
dv_how.arrow(244, 50, 276, 50)
dv_how.arrow(244, 160, 300, 108)
dv_how.arrow(400, 166, 400, 108)
dv_how.arrow(524, 200, 556, 200)
dv_how.note(380, 280, "stars for reports are built on top", "pen")

DV = dict(
    slug="data-vault",
    kicker="a.k.a. “hubs, links and satellites”",
    tldr="When many sources describe the same things and keep changing, put an <b>insert-only integration layer</b> between staging and the marts. <b>Hubs</b> hold business keys (customer number). <b>Links</b> hold relationships (order ↔ customer). <b>Satellites</b> hold descriptive attributes, per source, <b>dated and never updated</b>. A new source adds satellites without touching what exists, and you can answer “what did each source say, when?”. Stars for reporting are built on top.",
    chips=[("Family", "modelling"), ("Origin", "Dan Linstedt (2000); Data Vault 2.0 (2013)"), ("Lives in", "AutomateDV, WhereScape, VaultSpeed"), ("Pairs with", "layered zones, star schema")],
    problem="""  <p class="lead">Customers reach the warehouse from the ERP, the web store, the CRM, the loyalty app, and now the ERP of a chain the shop bought. Each new or changed source means <b>rewriting <code>dim_customer</code></b> and its load. Then an auditor asks what the CRM said about customer 77 on 1 March, and <span class="hl-pink">nobody can say</span>.</p>""",
    problem_figs=[dv_problem],
    analogy_side="the library card catalogue",
    analogy="""  <p>An old library catalogue has <b>one card per book</b>, identified by its ISBN, that never changes. <b>Cross-reference cards</b> link a book to its authors. Behind each card, librarians pin <b>dated slips</b> with notes; nobody erases a slip, they add a newer one. A new librarian adds their own slips without rewriting anyone else's.</p>""",
    analogy_figs=[dv_analogy],
    map=[("The book card (ISBN)", "Hub: one row per business key"),
         ("Cross-reference card", "Link: one row per relationship between keys"),
         ("Dated slips behind the card", "Satellites: descriptive attributes with load dates"),
         ("Each librarian's own slips", "One satellite per source"),
         ("Never erasing", "Insert-only loads")],
    how_side="keys, relationships and dated details, apart",
    how="""  <p>Splitting keys, relationships and attributes means each changes independently. Hubs and links almost never change shape. A new source adds a satellite. A changed source adds columns to its own satellite. Every table is <b>insert-only</b> with a load date and record source, so the vault is a full, auditable history. Hash keys computed from business keys let every table load in parallel without lookups.</p>
  <p>The vault is not for reporting. Stars (often as views) are built on top for the marts.</p>""",
    how_figs=[dv_how],
    steps=[("Find the business keys", "Customer number, order number, SKU: what the business uses, not database ids."),
           ("Build hubs", "One per key, with a hash key, load date and source."),
           ("Build links", "One per relationship or transaction between hubs."),
           ("Build satellites", "Split by source and by how fast attributes change; insert a row when the hash of attributes changes."),
           ("Build marts on top", "Star schemas (views or tables) read the latest or point-in-time satellite rows.")],
    vocab=[("Hub", "Unique list of business keys for one concept."),
           ("Link", "Unique list of relationships between hubs."),
           ("Satellite", "Descriptive, dated attributes of a hub or link."),
           ("Hash key", "A hash of the business key, used as the join key."),
           ("Hashdiff", "A hash of a satellite's attributes, to detect changes."),
           ("PIT table", "Point-in-time helper that speeds up “as of” queries.")],
    code=dict(file="vault.sql", note="generic warehouse SQL", src="""
CREATE TABLE hub_customer (
  customer_hk  char(32) PRIMARY KEY,   -- md5(upper(trim(customer_no)))
  customer_no  text, load_date timestamp, record_source text);

CREATE TABLE sat_customer_crm (
  customer_hk char(32), load_date timestamp, hashdiff char(32),
  name text, city text, record_source text,
  PRIMARY KEY (customer_hk, load_date));

-- insert-only: add a satellite row only when the attributes changed
INSERT INTO sat_customer_crm
SELECT s.customer_hk, :load_ts, s.hashdiff, s.name, s.city, 'crm'
FROM   stg_crm_customers s
LEFT JOIN (SELECT customer_hk, hashdiff,
                  row_number() OVER (PARTITION BY customer_hk ORDER BY load_date DESC) rn
           FROM sat_customer_crm) cur
  ON cur.customer_hk = s.customer_hk AND cur.rn = 1
WHERE  cur.hashdiff IS DISTINCT FROM s.hashdiff;
"""),
    tools="tools: AutomateDV (formerly dbtvault) for dbt, datavault4dbt, WhereScape, VaultSpeed, Coalesce; any warehouse with MERGE or insert-select.",
    then_now=dict(src="Linstedt, 2000",
                  then="Dan Linstedt designed the data vault in the 1990s for large enterprise warehouses: a normalised, auditable integration layer loaded by hand-written ETL, with sequence keys and many sources.",
                  now="Data Vault 2.0 (2013) replaced sequence keys with hash keys for parallel loads, and tools now generate most of the SQL. It is common in banks, insurers and large multi-source shops, usually under a layer of stars. Smaller teams with a few sources mostly skip it for staging plus stars.",
                  verdict="rethought",
                  take="Worth it when many changing sources and audit needs meet. Generate it with a tool; never hand-write a vault for three sources."),
    gains=["<b>New sources are additive</b>: new satellites, no rewrites.",
           "<b>Full, auditable history</b> per source.",
           "<b>Parallel loads</b>: hash keys, no lookups.",
           "<b>Resilient to source change</b>: damage stays in one satellite."],
    losses=["<b>Many tables and joins</b>: a vault is hard to query directly.",
            "<b>Needs a layer on top</b> for any report.",
            "<b>Steep learning curve</b> and modelling rules.",
            "<b>Overkill</b> for a few stable sources."],
    baseline="Each line compares <b>staging loaded straight into star dimensions</b> to <b>a data vault between staging and the stars</b>.",
    ratings=[(4, 2, "Hubs, links, satellites, hash keys, PIT tables."),
             (3, 3, "Neutral: parallel loads offset the extra layer."),
             (3, 4, "Every source's version is kept, nothing overwritten."),
             (3, 5, "Insert-only; stars rebuild from the vault."),
             (3, 5, "Built for many sources and parallel loads."),
             (3, 2, "More tables, more storage, more tooling."),
             (3, 3, "Neutral: reports still read stars."),
             (2, 4, "Record source and load date on every row."),
             (2, 5, "New sources and columns are additive.")],
    pitfalls=[("Reporting from the vault", "Analysts join twelve tables to get a customer's city.", "build stars or views on top; grant only those."),
              ("Source keys as business keys", "Each system's internal id becomes a hub, and nothing integrates.", "find the key the business uses, and map sources to it."),
              ("One giant satellite", "Fast-changing points and slow-changing names share one satellite; it grows on every change.", "split satellites by source and by rate of change."),
              ("Hand-written vault", "Hundreds of near-identical load scripts with subtle differences.", "generate loads from metadata with a tool or macros.")],
    use=["Many sources for the same entities, and more coming.",
         "Sources that change shape often.",
         "Audit or regulation needs “what did each source say, when”.",
         "Several teams loading in parallel."],
    skip=["A few stable sources: staging plus type 2 stars is enough.",
          "A small team without tooling to generate the SQL.",
          "Purely analytical sandboxes."],
    related=["<b>Layered zones</b>", "<b>Slowly changing dimensions</b>", "<b>Bitemporal data</b> (Vol. 3)", "<b>Conformed dimensions</b>"],
    quiz=[("What do hubs, links and satellites hold?", "Hubs: business keys. Links: relationships between keys. Satellites: dated descriptive attributes."),
          ("Why are vault tables insert-only?", "So the full history per source is kept and loads are simple, parallel and auditable."),
          ("What happens when a new source arrives?", "It adds its own satellites (and maybe hubs or links) without changing existing tables."),
          ("Why build stars on top of a vault?", "A vault is hard to query; stars give analysts simple, fast tables.")],
    quiz_sit=[("Your shop has three sources and two analysts. A consultant proposes a data vault. Is it worth it?",
               "Probably not yet: three stable sources fit staging plus type 2 dimensions in stars, which is far simpler. Revisit if sources multiply (acquisitions), change often, or an auditor needs per-source history; then generate the vault with a tool.")],
    try_it="Model the shop's customers from two sources (CRM and loyalty app) as one hub and two satellites. Load two days of data where only the loyalty tier changes on day 2. Count rows in each satellite, then write the query for “the customer's city and tier on day 1”.",
    remember="Keys in <span class=\"hl\">hubs</span>, relationships in <span class=\"hl\">links</span>, dated details in <span class=\"hl\">satellites</span>. Never erase a slip.",
    sources=["Dan Linstedt and Michael Olschimke, <i>Building a Scalable Data Warehouse with Data Vault 2.0</i> (2015).",
             "Hans Hultgren, <i>Modeling the Agile Data Warehouse with Data Vault</i> (2012).",
             "AutomateDV documentation.",
             "Kimball Group and Data Vault Alliance articles comparing the approaches."],
)

# ------------------------------------------------------------------ 10 One Big Table vs Star
obt_problem = Doodle(760, 260, exact=True, label="Doodle of a store manager in the BI tool facing seven tables with tangled join lines: fact sales, date, product, category, customer, shop and region. They drag the wrong join, the total doubles, and they export to Excel instead.",
                     caption="Seven tables and a tangle of joins: the store manager gives up and exports to Excel.")
for i, t in enumerate(["fact_sales", "dim_date", "dim_product", "dim_customer", "dim_shop", "dim_region", "dim_promo"]):
    x, y = 20 + (i % 4) * 150, 30 + (i // 4) * 90
    obt_problem.box(x, y, 136, 44, t, "y" if i == 0 else "paper", size=15)
for d in ["M156 52 H170", "M88 74 V120", "M110 74 L238 120", "M130 74 L388 120", "M150 34 Q320 -4 470 34", "M140 32 Q240 4 320 32", "M238 74 L170 120"]:
    obt_problem.line(d, color="red")
obt_problem.icon("screen", 640, 120, 1.0)
obt_problem.note(380, 230, "wrong join → total doubled → “I'll use Excel”", "red")

obt_analogy = Doodle(760, 240, "Doodle comparing a printed phone book and a card index. The phone book has everything on one line: name, street, city, number, easy to read, but fixing one address means reprinting. The card index has cross-references between cards: harder to read, easy to update one card.",
                     "A printed phone book is easy to read and expensive to correct. A card index is the reverse.")
obt_analogy.icon("book", 60, 50, 1.6, fill="y")
obt_analogy.note(110, 170, "phone book: one line, all of it")
obt_analogy.note(110, 196, "fix one address → reprint", "red")
obt_analogy.icon("cards", 470, 50, 1.6, fill="blue")
obt_analogy.note(520, 170, "card index: cross-references")
obt_analogy.note(520, 196, "fix one card, done", "green")

obt_how = Doodle(760, 290, "The usual compromise. The modelled layer stays a star: fact sales with date, product, customer and shop dimensions. On top, a wide table or view, obt_sales, flattens one row per order line with every column a tool needs: date, month, category, brand, segment, city, region, quantity and amount. Columnar storage reads only the columns a query uses.",
                 "Model as a star; serve a wide table where a tool or a team needs one.")
obt_how.box(20, 60, 260, 150, "star", "green", sub="facts + dimensions", size=24, subsize=16)
obt_how.arrow(286, 135, 360, 135, label="flatten", lx=323, ly=120)
obt_how.table(366, 50, "obt_sales", ["line · date · month", "category · brand", "segment · city · region", "qty · amount"], w=280, fill="y")
obt_how.note(506, 230, "one row per order line, 60 columns", "pen")
obt_how.note(506, 256, "columnar: unused columns cost nothing to read", "pen")
obt_how.note(150, 240, "the source of truth", "green")

OBT = dict(
    slug="one-big-table",
    kicker="a.k.a. “OBT, the wide table”",
    tldr="A <b>one big table</b> joins the fact with every dimension column into one wide, flat table: easy for BI tools, spreadsheets and ML, and cheap to scan on columnar engines. A <b>star</b> keeps facts and dimensions apart: reusable, easy to change, history-friendly. The common answer is both: <b>model as a star, serve wide tables</b> (or views) where a tool or team needs them, and rebuild them from the star.",
    chips=[("Family", "modelling"), ("Debate", "Kimball vs Inmon vs wide tables"), ("Lives in", "BigQuery, ClickHouse, Snowflake, Druid"), ("Pairs with", "star schema, metrics layer")],
    problem="""  <p class="lead">A store manager opens the BI tool and sees seven tables with lines between them. They drag product next to shop, the tool picks the wrong join path, the <span class="hl-pink">total doubles</span>, and they go back to Excel exports.</p>
  <ul>
    <li>Business users can't (and shouldn't have to) choose joins.</li>
    <li>Some BI and ML tools work best on one flat table.</li>
    <li>But a 300-column table rebuilt from scratch every night is expensive and fragile.</li>
  </ul>""",
    problem_figs=[obt_problem],
    analogy_side="phone book vs card index",
    analogy="""  <p>A <b>printed phone book</b> puts everything on one line: name, street, city, number. It's easy to read and terrible to correct: one moved family means a reprint. A <b>card index</b> with cross-references is harder to read, and you fix one card when something changes. Libraries kept the card index and printed directories from it.</p>""",
    analogy_figs=[obt_analogy],
    map=[("The phone book line", "One wide row: fact plus all dimension columns"),
         ("The card index", "The star: facts and dimensions apart"),
         ("Reprinting", "Rebuilding the wide table after a dimension change"),
         ("Printing from the index", "Building wide tables from the star"),
         ("Readers who just want a number", "BI users, spreadsheets, ML features")],
    how_side="star underneath, wide on top",
    how="""  <p>Columnar engines store each column separately and compress repeated values, so a wide table with “Kitchen” repeated a million times costs little, and a query reads only the columns it names. That made one big tables practical. What they still cost: every dimension change (a type 1 fix, a new attribute) means rebuilding the wide table, and nothing is shared between wide tables.</p>
  <p>Keep the star as the modelled source of truth. Build wide tables or views from it for the tools that need them, and treat them as disposable outputs.</p>""",
    how_figs=[obt_how],
    steps=[("Model the star first", "Facts at a clear grain, conformed dimensions, type 2 where needed."),
           ("Find the consumers", "Which tool or team needs flat data? Self-service BI, a spreadsheet extract, an ML feature set."),
           ("Build the wide table from the star", "A view first; a table if it's slow. Only the columns they use."),
           ("Rebuild it, don't edit it", "It's an output: regenerate from the star on every load."),
           ("Keep definitions upstream", "Measures live in the star or the metrics layer, not in the wide table.")],
    vocab=[("OBT", "One big table: facts and dimension columns flattened together."),
           ("Columnar storage", "Each column stored separately, read only when needed."),
           ("Denormalisation", "Copying attributes onto rows to avoid joins."),
           ("Inmon EDW", "A normalised enterprise warehouse feeding marts (top-down)."),
           ("Kimball bus", "Dimensional marts on conformed dimensions (bottom-up)."),
           ("Fan-out", "Rows multiplied by a join, inflating totals.")],
    code=dict(file="models/marts/obt_sales.sql", note="dbt · served from the star", src="""
{{ config(materialized='table', partition_by={'field': 'order_date', 'data_type': 'date'}) }}

select
    f.order_line_id, f.order_date, d.month, d.week, d.is_holiday,
    p.sku, p.category, p.brand,
    c.segment, c.city as customer_city,
    s.shop_name, s.region,
    f.qty, f.amount
from {{ ref('fct_sales') }}    f
join {{ ref('dim_date') }}     d using (date_key)
join {{ ref('dim_product') }}  p using (product_key)
join {{ ref('dim_customer') }} c using (customer_key)
join {{ ref('dim_shop') }}     s using (shop_key)
"""),
    tools="tools: BigQuery (nested and repeated fields), ClickHouse and Druid (wide event tables), Snowflake, Databricks; BI semantic models (Power BI, Looker) can hide a star behind one flat view.",
    then_now=dict(src="Inmon, 1992 · Kimball, 1996",
                  then="Inmon argued for a normalised enterprise warehouse feeding marts; Kimball for dimensional stars. Both avoided flattening everything: on row stores, wide tables wasted disk and every query read every column.",
                  now="Columnar engines skip unused columns and compress repeated strings, so wide tables are cheap to scan, and some engines (ClickHouse, Druid) prefer them. Joins also got much cheaper. The debate moved from “which shape” to “which shape for whom”.",
                  verdict="rethought",
                  take="Model as a star, serve wide tables to the tools that want them. Neither shape alone fits every reader."),
    gains=["<b>Easy for users</b>: no joins to choose, no fan-out.",
           "<b>Fast scans</b> on columnar engines.",
           "<b>Good for tools</b>: BI self-service, spreadsheets, ML.",
           "<b>Simple to document</b>: one table, one grain."],
    losses=["<b>Rebuild on any dimension change</b>.",
            "<b>No reuse</b>: each wide table repeats the same joins.",
            "<b>Schema churn</b>: hundreds of columns, many unused.",
            "<b>History is frozen</b> into whatever the row said at build time."],
    baseline="Each line compares <b>users querying a star directly</b> to <b>a star underneath with wide tables built on top</b>.",
    ratings=[(3, 4, "Users see one table; engineers keep the star."),
             (3, 3, "Neutral: one more build step."),
             (3, 4, "No wrong joins in self-service."),
             (4, 4, "Wide tables rebuild from the star."),
             (3, 4, "Columnar scans of one table are fast."),
             (3, 2, "Extra storage and rebuilds."),
             (3, 4, "Every attribute is a drag-and-drop column."),
             (3, 3, "Neutral."),
             (3, 3, "Changes flow from the star, but each wide table must rebuild.")],
    pitfalls=[("Only the wide table", "No star underneath; every new question copies and edits the 300-column SQL.", "keep the star as the source of truth."),
              ("Mixed grain in one table", "Order totals repeated on every line get summed by users.", "one grain per wide table; put order-level data in its own table."),
              ("Measures defined in the wide table", "Each wide table computes margin slightly differently.", "define measures once, upstream or in the metrics layer."),
              ("Everything, just in case", "600 columns nobody reads, rebuilt hourly.", "include what consumers use; add columns on request.")],
    use=["Self-service BI for non-technical users.",
         "Columnar engines that prefer wide tables (ClickHouse, Druid).",
         "ML feature tables and spreadsheet extracts.",
         "A dashboard with a fixed set of columns."],
    skip=["As the only model of the warehouse.",
          "Dimensions that change often and must be correct everywhere at once.",
          "Many-to-many relationships that would multiply rows."],
    related=["<b>Star schema</b> (Vol. 3)", "<b>Normalization</b> (Vol. 3)", "<b>Metrics layer</b>", "<b>Aggregates and rollups</b>"],
    quiz=[("What is a one big table?", "A wide, flat table that joins facts with all their dimension columns."),
          ("Why are wide tables cheap on columnar engines?", "Queries read only the columns they name, and repeated values compress well."),
          ("What does a wide table cost when a dimension changes?", "It has to be rebuilt, because the old values are copied into every row."),
          ("What is the usual compromise?", "Model as a star and build wide tables or views from it for the tools that need them.")],
    quiz_sit=[("A product manager asks you to drop the star and keep only one big table, “because that's what everyone uses”. What do you answer?",
               "Keep the star as the source of truth and generate the wide table from it on every load. Users keep their one table; you keep type 2 history, conformed dimensions for other facts, and the ability to rebuild everything when a definition changes.")],
    try_it="Build a view that flattens your star into one table, and point a BI tool at it. Count the clicks to answer “sales by region by month” with the star and with the view. Then change one product's category and see what each needs to reflect it.",
    remember="Keep the <span class=\"hl\">card index</span>. Print <span class=\"hl\">phone books</span> from it for whoever wants one.",
    sources=["W. H. Inmon, <i>Building the Data Warehouse</i> (1992).",
             "Ralph Kimball, <i>The Data Warehouse Toolkit</i> (1996).",
             "Fivetran, “Star schema vs. OBT for data warehouse performance” (benchmark, 2022).",
             "ClickHouse documentation, “Denormalizing data”."],
)

NOTES = [SCD, FT, CD, DV, OBT]
