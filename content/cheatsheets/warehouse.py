# Data Warehouse · a laminated reference card in four pages, for Vol. 9 · Data Pipelines & Analytics.
# Rendered by scripts/build_notes.py (render_cheatsheet); Diagram, code and box come from scripts/cheatsheet.py.
# Generic warehouse SQL (MERGE, window functions); dbt where a tool is named. The homeware shop's tables throughout.
# Boxes flow into a 3-column grid (dense packing), so order them to fill rows: wide (2) + narrow (1).

SLUG = "warehouse"
TITLE = "Data Warehouse"
SUBTITLE = "dimensional modelling, history, loading patterns and trustworthy reports"
DESC = ("A four-page data warehouse cheat sheet: grain and fact table types, the bus matrix, slowly changing dimensions, "
        "point-in-time joins, idempotent load patterns, MERGE, late data, data tests, reconciliation and serving.")
VERSION = "v1 · Nov 2026"
BLURB = ("Four laminated pages: modelling (grain, facts, dimensions), history (SCD types and point-in-time joins), "
         "loading (idempotent patterns, MERGE, late data) and trust (tests, reconciliation, aggregates, metrics).")
LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
        '<rect x="12" y="12" width="10" height="10" rx="2" fill="none" stroke="var(--b-dev)" stroke-width="2.4"/>'
        '<path d="M12 12 6 6M22 12l6-6M12 22l-6 6M22 22l6 6" stroke="var(--b-feat)" stroke-width="2.4"/>'
        '<circle cx="6" cy="6" r="2.4" fill="var(--b-feat)"/><circle cx="28" cy="6" r="2.4" fill="var(--b-feat)"/>'
        '<circle cx="6" cy="28" r="2.4" fill="var(--b-feat)"/><circle cx="28" cy="28" r="2.4" fill="var(--b-feat)"/></svg>')


# ---------------------------------------------------------------- page 1 · modelling
def design():
    d = Diagram("Four design steps in order: choose the business process, declare the grain, pick the dimensions, "
                "then the facts. On the right, the result: fact_sales in the middle with date, product, customer and shop dimensions.",
                880, 200)
    steps = [("1 · process", "orders, stock", "dev"), ("2 · grain", "one row = …", "bug"),
             ("3 · dims", "who · what · when", "feat"), ("4 · facts", "the numbers", "main")]
    for i, (label, sub, tone) in enumerate(steps):
        d.node(f"s{i}", 14 + i * 120, 40, 108, 54, label, sub, tone)
        if i:
            d.arrow(f"s{i - 1}", f"s{i}")
    d.text(14, 128, "Grain before columns. If you can't say what one row is, stop.")
    d.text(14, 148, "Facts are numbers at that grain; dimensions are what you filter and group by.")
    d.node("f", 640, 72, 120, 50, "fact_sales", "line · qty · amount", "main")
    for nid, x, y, label in [("d1", 500, 14, "dim_date"), ("d2", 774, 14, "dim_product"), ("d3", 500, 140, "dim_customer"), ("d4", 774, 140, "dim_shop")]:
        d.node(nid, x, y, 96, 40, label, None, "ink", "soft")
    d.arrow("f", "d1", sides="lr")
    d.arrow("f", "d2", sides="rl")
    d.arrow("f", "d3", sides="lr")
    d.arrow("f", "d4", sides="rl")
    return d.svg()


PAGE_MODEL = dict(
    title="Modelling",
    kicker="grain, fact table types, dimensions, the bus matrix",
    figure=design(),
    boxes=[
        box("Fact table types", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th></th><th>one row per</th><th>loaded by</th><th>example</th></tr></thead>
<tbody>
<tr><th>transaction</th><td>event</td><td>append / merge</td><td>order line</td></tr>
<tr><th>periodic snapshot</th><td>thing per period</td><td>one partition per period</td><td>stock per shop per month</td></tr>
<tr><th>accumulating</th><td>process instance</td><td>merge, updated per milestone</td><td>order: paid → shipped → delivered</td></tr>
<tr><th>factless</th><td>event or coverage, no number</td><td>insert</td><td>product on promotion per day</td></tr>
</tbody></table></div>
<p class="fine">Ask the question first; the type follows. One grain per table, always.</p>''', "main", "wide", "pick by question"),
        box("The grain sentence", '''
<ul class="checks">
<li>“One row per <b>order line</b>”</li>
<li>“One row per <b>product · shop · month</b>”</li>
<li>“One row per <b>order</b>, updated”</li>
<li>Measures must be true <b>at</b> that grain</li>
<li><b>!</b> Order-level shipping on every line → summed 3×</li>
<li>Store the finest grain you can afford</li>
</ul>''', "bug"),
        box("Can I add it up?", '''
<dl class="kv">
<dt>additive</dt><dd>sum across everything: qty, amount</dd>
<dt>semi-additive</dt><dd>not across time: stock on hand, balance → last or avg</dd>
<dt>non-additive</dt><dd>ratios, %: store the parts, divide at the end</dd>
<dt>distinct count</dt><dd>doesn't roll up: count from facts or merge HLL sketches</dd>
</dl>''', "feat"),
        box("Bus matrix", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>process ↓ · dimension →</th><th>date</th><th>product</th><th>customer</th><th>shop</th><th>promo</th></tr></thead>
<tbody>
<tr><th>sales</th><td>✕</td><td>✕</td><td>✕</td><td>✕</td><td>✕</td></tr>
<tr><th>returns</th><td>✕</td><td>✕</td><td>✕</td><td>✕</td><td></td></tr>
<tr><th>web sessions</th><td>✕</td><td>✕</td><td>✕</td><td></td><td>✕</td></tr>
<tr><th>stock</th><td>✕</td><td>✕</td><td></td><td>✕</td><td></td></tr>
</tbody></table></div>
<p class="fine">Each column is <b>one conformed dimension</b>, built once, shared by every fact. Compare processes by <b>drilling across</b>: aggregate each fact, then join (page 4).</p>''', "dev", "wide", "plan the warehouse"),
        box("Keys", '''
<ul class="checks">
<li>Dimensions get a <b>surrogate key</b> per version</li>
<li>Keep the source's <b>natural key</b> beside it</li>
<li>Facts store <b>surrogate keys</b> only for joins</li>
<li>Unknown member: key <code>-1</code>, “not yet known”</li>
<li>Date key as <code>20260331</code> is fine</li>
</ul>''', "ink"),
        box("dim_date, built once", code('''
SELECT d                              AS date,
  CAST(to_char(d,'YYYYMMDD') AS int)  AS date_key,
  extract(isodow FROM d)              AS weekday,
  date_trunc('month', d)              AS month,
  extract(quarter FROM d)             AS quarter,
  d IN (SELECT day FROM holidays_nl)  AS is_holiday,
  fiscal_period(d)                    AS fiscal_period
FROM generate_series(DATE '2015-01-01',
                     DATE '2035-12-31', interval '1 day') d;
''') + '<p class="fine">Local calendar, fiscal periods and holidays live here, not in every report.</p>', "rel", "wide"),
        box("Naming", '''
<dl class="kv">
<dt><code>raw.*</code></dt><dd>as received</dd>
<dt><code>stg_*</code></dt><dd>one clean row per key</dd>
<dt><code>dim_*</code> · <code>fct_*</code></dt><dd>marts</dd>
<dt><code>agg_*</code> · <code>rpt_*</code></dt><dd>served summaries</dd>
<dt><code>*_key</code> · <code>*_id</code></dt><dd>surrogate · natural</dd>
</dl>''', "warn"),
    ],
)


# ---------------------------------------------------------------- page 2 · history
def versions():
    d = Diagram("Type 2 history for the kettle. Version 812, Kitchen, is valid from 1 September 2025 up to 12 May 2026. "
                "Version 977, Small appliances, is valid from 12 May 2026 onwards. The 31 March sale stores key 812.",
                880, 170)
    d.text(14, 24, "valid time →", "dt strong")
    d.node("v1", 14, 40, 430, 44, "812 · K-100 · Kitchen", "[2025-09-01, 2026-05-12)", "dev")
    d.node("v2", 448, 40, 418, 44, "977 · K-100 · Small appliances", "[2026-05-12, 9999-12-31)", "feat")
    d.node("f", 230, 116, 190, 40, "sale 31 Mar → key 812", None, "main", "chip")
    d.arrow("f", "v1", sides="tb")
    d.text(470, 128, "half-open: >= from AND < to · one time zone")
    d.text(470, 148, "facts keep the key they were loaded with")
    return d.svg()


PAGE_HIST = dict(
    title="History",
    kicker="slowly changing dimensions, point-in-time joins, three pasts",
    figure=versions(),
    boxes=[
        box("SCD types", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>type</th><th>on change</th><th>past reports</th><th>use for</th></tr></thead>
<tbody>
<tr><th>0</th><td>never change</td><td>fixed</td><td>original signup date</td></tr>
<tr><th>1</th><td>overwrite</td><td><b>move</b> to new value</td><td>typos, descriptions</td></tr>
<tr><th>2</th><td>new row, new key, valid dates</td><td>keep old value</td><td>category, region, segment</td></tr>
<tr><th>3</th><td><code>previous_x</code> column</td><td>one step back</td><td>“old vs new” for one re-org</td></tr>
<tr><th>4</th><td>mini-dimension for fast columns</td><td>banded values</td><td>age band, spend band</td></tr>
<tr><th>6</th><td>2 + <code>current_x</code> on every row</td><td>both views</td><td>regions: as was and as is</td></tr>
</tbody></table></div>''', "dev", "wide", "decide per column"),
        box("Type 2 columns", code('''
product_key  bigint  -- surrogate
sku          text    -- natural key
category     text    -- type 2
description  text    -- type 1
valid_from   timestamp
valid_to     timestamp  -- or 9999-12-31
is_current   boolean
hashdiff     char(32)  -- tracked cols
loaded_at    timestamp  -- recorded
'''), "feat"),
        box("Load: close, then insert", code('''
BEGIN;
UPDATE dim_product d
SET    valid_to = s.effective_from, is_current = false
FROM   stg_products s
WHERE  d.sku = s.sku AND d.is_current
  AND  d.hashdiff <> s.hashdiff;

INSERT INTO dim_product (sku, category, valid_from, valid_to, is_current, hashdiff)
SELECT s.sku, s.category, s.effective_from, '9999-12-31', true, s.hashdiff
FROM   stg_products s
LEFT JOIN dim_product d ON d.sku = s.sku AND d.is_current
WHERE  d.sku IS NULL;   -- new keys + just-closed keys
COMMIT;
''') + '<p class="fine">Date versions by the <b>effective date</b> from the source when there is one, not the load date.</p>', "main", "wide"),
        box("Point-in-time lookup", code('''
SELECT s.order_line_id, p.product_key
FROM   stg_order_lines s
JOIN   dim_product p
  ON   p.sku = s.sku
 AND   s.sold_at >= p.valid_from
 AND   s.sold_at <  p.valid_to;
''') + '<p class="fine">Once, at fact load. Reports then join on <code>product_key</code>.</p>', "rel"),
        box("Three pasts", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>question</th><th>called</th><th>how</th></tr></thead>
<tbody>
<tr><td>Kitchen revenue in March</td><th>as it was</th><td>type 2 join on the fact's key</td></tr>
<tr><td>this year by today's regions</td><th>as it is</td><td><code>current_region</code> (type 6) or join via natural key to the current row</td></tr>
<tr><td>what did we report on 15 July?</td><th>as reported</td><td>filed report table, or recorded time (bitemporal)</td></tr>
</tbody></table></div>''', "hot", "wide"),
        box("History traps", '''
<ul class="checks nul">
<li><b>!</b> Facts joined on the <b>natural key</b> → every version matches, totals double</li>
<li><b>!</b> <code>BETWEEN</code> on validity → boundary in two versions</li>
<li><b>!</b> Versions dated by load day → backdated moves land late</li>
<li><b>!</b> Missing version → fact dropped; use an <b>inferred member</b></li>
<li><b>!</b> Type 2 on <code>last_login</code> → millions of versions a day</li>
<li><b>!</b> Nightly snapshot → changes between runs are lost</li>
</ul>
<p class="fine">Test every load: one current row per key; no overlapping ranges (<code>a.from &lt; b.to AND b.from &lt; a.to</code>).</p>''', "warn"),
    ],
)


# ---------------------------------------------------------------- page 3 · loading
def layers():
    d = Diagram("Layers and how each is loaded. The app database is extracted by CDC or a watermark into raw, appended. "
                "Staging keeps the latest row per key. Marts are merged on the key, newer only, or have their slice replaced. "
                "Reports read marts only.", 880, 150)
    for i, (nid, label, sub, tone) in enumerate([("src", "app DB", "PostgreSQL", "ink"), ("raw", "raw", "append only", "warn"),
                                                 ("stg", "staging", "latest per key", "dev"), ("mart", "marts", "facts + dims", "main"),
                                                 ("rpt", "reports", "marts only", "rel")]):
        d.node(nid, 14 + i * 176, 44, 140, 54, label, sub, tone)
    d.arrow("src", "raw", "CDC / watermark", ly=34)
    d.arrow("raw", "stg", "dedupe", ly=34)
    d.arrow("stg", "mart", "MERGE / replace", ly=34)
    d.arrow("mart", "rpt", "read", ly=34)
    d.text(14, 128, "Every arrow must be safe to run twice. Raw is never edited, so everything after it can be rebuilt.")
    return d.svg()


PAGE_LOAD = dict(
    title="Loading",
    kicker="extract, dedupe, merge, replace, late data, backfills",
    figure=layers(),
    boxes=[
        box("Load patterns", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th></th><th>safe twice?</th><th>late updates</th><th>use for</th></tr></thead>
<tbody>
<tr><th>append</th><td>no</td><td>no</td><td>raw only</td></tr>
<tr><th>delete + insert a slice</th><td>yes</td><td>if you reload the slice</td><td>facts by event date</td></tr>
<tr><th>partition overwrite</th><td>yes</td><td>if you reload the partition</td><td>big facts, BigQuery / Spark</td></tr>
<tr><th>MERGE on key, newer only</th><td>yes</td><td>yes, any day</td><td>CDC-fed staging and facts</td></tr>
<tr><th>full rebuild</th><td>yes</td><td>yes</td><td>small dims, after logic changes</td></tr>
</tbody></table></div>''', "main", "wide", "idempotent or not"),
        box("Latest row per key", code('''
SELECT * FROM (
  SELECT r.*, ROW_NUMBER() OVER (
           PARTITION BY id
           ORDER BY lsn DESC) AS rn
  FROM raw.order_lines_changes r
) x
WHERE rn = 1;  -- op 'd' = deleted
''') + '<p class="fine">Order by <b>log position</b>, never arrival time.</p>', "dev"),
        box("MERGE, newer only", code('''
MERGE INTO fct_sales t
USING stg_sales_changes s
   ON t.order_line_id = s.order_line_id
  AND t.order_date IN (SELECT d FROM touched_days)  -- prune partitions
WHEN MATCHED AND s.lsn > t.source_lsn AND s.is_deleted THEN DELETE
WHEN MATCHED AND s.lsn > t.source_lsn THEN
  UPDATE SET qty = s.qty, amount = s.amount, source_lsn = s.lsn
WHEN NOT MATCHED AND NOT s.is_deleted THEN
  INSERT (order_line_id, order_date, product_key, qty, amount, source_lsn)
  VALUES (s.order_line_id, s.order_date, s.product_key, s.qty, s.amount, s.lsn);
'''), "main", "wide"),
        box("Watermark extract", code('''
SELECT * FROM order_lines
WHERE updated_at >
        :wm - interval '10 min'
  AND updated_at <=
        now() - interval '1 min';
-- MERGE, then save the max
''') + '<p class="fine">Overlap &gt; longest transaction. Can\'t see hard deletes: CDC or key compare.</p>', "bug"),
        box("Late data: rebuild touched days", code('''
CREATE TEMP TABLE touched_days AS
SELECT DISTINCT CAST(sold_at AT TIME ZONE 'Europe/Amsterdam' AS date) AS d
FROM   stg_batch;

DELETE FROM fct_sales WHERE order_date IN (SELECT d FROM touched_days);
INSERT INTO fct_sales SELECT * FROM stg_sales_enriched
WHERE  order_date IN (SELECT d FROM touched_days);
''') + '<p class="fine">Event time decides the day. Past the lateness window → book an adjustment in today\'s period.</p>', "rel", "wide"),
        box("Three clocks", '''
<dl class="kv">
<dt>event time</dt><dd>which day it belongs to</dd>
<dt>commit order</dt><dd>which version wins (LSN)</dd>
<dt>load time</dt><dd>debugging only</dd>
</dl>
<p class="fine">No <code>now()</code> in transforms: pass the logical date in.</p>''', "warn"),
        box("dbt incremental", code('''
{{ config(
    materialized='incremental',
    unique_key='order_line_id',
    incremental_strategy='merge',
    incremental_predicates=[
      "DBT_INTERNAL_DEST.order_date >= dateadd(day, -35, current_date)"],
    on_schema_change='fail') }}
select ... from {{ ref('stg_order_lines') }}
{% if is_incremental() %}
where _lsn > (select max(source_lsn) from {{ this }})
{% endif %}
'''), "feat", "wide"),
        box("Backfill", code('''
# same job, past dates
dbt build -s fct_sales+ \\
  --vars '{from: 2026-03-01,
           to: 2026-04-01}'
''') + '<p class="fine">If a backfill needs its own script, the daily job isn\'t idempotent yet.</p>', "ink"),
    ],
)


# ---------------------------------------------------------------- page 4 · trust & serving
def wap():
    d = Diagram("Write, audit, publish. The load writes fct_sales_next. Audits check keys, counts and sums. If they pass, "
                "an atomic swap publishes it; if they fail, yesterday's table stays and an alert fires.", 880, 150)
    d.node("w", 14, 50, 170, 54, "write", "fct_sales_next", "dev")
    d.node("a", 260, 50, 190, 54, "audit", "keys · counts · sums", "warn")
    d.node("p", 560, 14, 170, 50, "publish", "atomic swap", "main")
    d.node("k", 560, 88, 170, 50, "keep yesterday", "alert · “as of Sun”", "bug")
    d.arrow("w", "a")
    d.arrow("a", "p", "pass", ly=30)
    d.arrow("a", "k", "fail", tone="bug", ly=128)
    d.text(750, 60, "readers only see")
    d.text(750, 78, "audited tables")
    return d.svg()


PAGE_TRUST = dict(
    title="Trust & serving",
    kicker="tests, reconciliation, drill across, aggregates, one metric definition",
    figure=wap(),
    boxes=[
        box("Reconcile with the source", code('''
-- same query on the source replica and the warehouse, compare
SELECT CAST(placed_at AT TIME ZONE 'Europe/Amsterdam' AS date) AS day,
       count(*)        AS lines,
       sum(line_total) AS revenue
FROM   order_lines JOIN orders USING (order_id)
WHERE  placed_at >= now() - interval '60 days'
GROUP  BY 1;
''') + '<p class="fine">Old days must match exactly. A difference names the day to replay. The best single test you can run.</p>', "main", "wide", "nightly"),
        box("Data tests", '''
<ul class="checks">
<li>keys <b>unique</b> and <b>not null</b></li>
<li>foreign keys resolve (or point at <code>-1</code>)</li>
<li>values in range: <code>0 &lt; price &lt; 2,000</code></li>
<li>count and sum within ±30 % of the same weekday</li>
<li>quarantined rows &lt; 1 % of the batch</li>
<li>freshness: newest event &lt; 45 min old</li>
</ul>
<p class="fine">Row failures → quarantine table with a reason. Batch failures → don't publish.</p>''', "bug"),
        box("Drill across", code('''
WITH s AS (SELECT p.category, sum(f.qty) sold
           FROM fct_sales f JOIN dim_product p USING (product_key)
           GROUP BY 1),
     r AS (SELECT p.category, sum(x.qty) returned
           FROM fct_returns x JOIN dim_product p USING (product_key)
           GROUP BY 1)
SELECT category, sold, coalesce(returned, 0) returned,
       round(100.0 * coalesce(returned, 0) / sold, 1) AS return_pct
FROM s LEFT JOIN r USING (category);
''') + '<p class="fine"><b>!</b> Never join two facts row to row: aggregate each, then join.</p>', "dev", "wide"),
        box("Aggregates", code('''
SELECT order_date, shop_key,
  category, sum(amount) revenue,
  count(*) lines,
  HLL_COUNT.INIT(customer_key)
    AS cust_sketch
FROM fct_sales
JOIN dim_product USING (product_key)
GROUP BY 1, 2, 3;
''') + '<p class="fine">Store sums and counts; averages = sum / count. Distinct counts: merge sketches.</p>', "rel"),
        box("One metric, defined once", code('''
metrics:
  - name: revenue
    label: Revenue (net, after returns, excl. gift cards)
    type: simple
    type_params: { measure: amount_net }
    filter: "{{ Dimension('product__is_gift_card') }} = false"
  - name: average_order_value
    type: ratio          # sum / count, never avg of avgs
    type_params: { numerator: revenue, denominator: orders }
'''), "feat", "wide", "metrics layer"),
        box("Only your rows", code('''
CREATE ROW ACCESS POLICY shop_only
AS (shop_id INT) RETURNS BOOLEAN ->
  shop_id = TRY_TO_NUMBER(
    CURRENT_SESSION_CONTEXT('shop_id'))
  OR IS_ROLE_IN_SESSION('HEAD_OFFICE');
''') + '<p class="fine">Tenant from a <b>signed token</b>, never the URL. Tenant in every cache key.</p>', "hot"),
        box("Before you publish a number", '''
<ul class="checks">
<li>The <b>grain</b> of every table it reads is written down</li>
<li>Its definition lives in <b>one</b> place, with an owner</li>
<li>It says <b>as it was</b> or <b>as it is</b></li>
<li>The page shows <b>data as of</b></li>
<li>Filed numbers are <b>stored</b> when they're sent</li>
</ul>''', "ink", "wide"),
        box("Freshness", code('''
SELECT now() - max(sold_at) AS age
FROM   fct_sales;
-- alert > 45 min in opening hours
'''), "warn"),
    ],
)

PAGES = [PAGE_MODEL, PAGE_HIST, PAGE_LOAD, PAGE_TRUST]
