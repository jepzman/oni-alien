# Deep dive 13 · History in the Warehouse. Builds on Vol. 3 notes 04 (history tables) and 17 (bitemporal data) and
# Vol. 9 notes 06 (slowly changing dimensions) and 05 (late-arriving data). Example: the homeware shop from Vol. 9.
# Three changes are followed through the dive: the kettle (SKU K-100) moves from Kitchen to Small appliances on
# 12 May; customer 77 moves from Utrecht to Rotterdam on 1 February but the CRM only learns it on 20 February;
# the Delft shop moves from region North to region South on 1 July.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
recap_svg = '''
  <path class="ln" d="M20 200 H740" marker-end="url(#a)"/>
  <text class="soft" x="60" y="226" text-anchor="middle">1 Feb</text><text class="soft" x="150" y="226" text-anchor="middle">20 Feb</text>
  <text class="soft" x="330" y="226" text-anchor="middle">12 May</text><text class="soft" x="520" y="226" text-anchor="middle">1 Jul</text>
  <path class="ln-d" d="M60 40 V196"/><path class="ln-d" d="M150 40 V196"/><path class="ln-d" d="M330 40 V196"/><path class="ln-d" d="M520 40 V196"/>
  <rect class="bx-y" x="158" y="50" width="166" height="50" rx="8"/><text class="lbl" x="241" y="72" text-anchor="middle">customer 77 moves</text><text class="soft" x="241" y="92" text-anchor="middle">CRM learns 20 Feb</text>
  <rect class="bx" x="340" y="110" width="170" height="50" rx="8"/><text class="lbl" x="425" y="132" text-anchor="middle">kettle recategorised</text><text class="soft" x="425" y="152" text-anchor="middle">Kitchen → Small appl.</text>
  <rect class="bx-g" x="530" y="50" width="200" height="50" rx="8"/><text class="lbl" x="630" y="72" text-anchor="middle">Delft changes region</text><text class="soft" x="630" y="92" text-anchor="middle">North → South</text>
'''
recap = '''
<p>Four notes deal with the past. In a warehouse they meet, because every report about last year has to decide which version of the world to use.</p>
''' + tbl(["Note", "In one line"], [
    ["History Tables (Vol. 3)", "keep every past version of a row, with when it was valid"],
    ["Bitemporal Data (Vol. 3)", "record when a fact was true <i>and</i> when you knew it"],
    ["Slowly Changing Dimensions (Vol. 9)", "per column, overwrite (type 1) or add a dated version with a new key (type 2)"],
    ["Late-Arriving Data (Vol. 9)", "file each event in the period it happened, even when it reaches you late"],
]) + fig(760, 240, "This year's three changes on a timeline. Customer 77 moves from Utrecht to Rotterdam on 1 February, and the CRM learns about it on 20 February. On 12 May the kettle moves from Kitchen to Small appliances. On 1 July the Delft shop moves from region North to region South.",
         recap_svg, "Three changes, three kinds of trouble: one recorded late, one that rewrites categories, one that rewrites the map.") + mn("The SCD note covers types 1 to 6 on one product. This dive is about running them for years.") + '''
<p class="full">The notes describe each idea on one row. The warehouse holds thousands of changing rows, facts that point at them, and people asking for the past in three different ways without saying which. This dive follows three changes at the shop through one year and answers the questions they cause: why March changed, why the same customer counts twice, and what the report said on 15 July.</p>
<h3>Three people, three questions about last year</h3>
''' + tbl(["Who", "Asks", "Which past they mean"], [
    ["finance", "“What was Kitchen's revenue in March?”", "as it was: the category when it was sold"],
    ["regional managers", "“How did the South region do this year?”", "as it is: today's regions, applied to the whole year"],
    ["the auditor", "“What did your report say on 15 July?”", "as it was reported: what the warehouse knew that day"],
]) + '''
<p class="full">All three are fair, and each needs a different mechanism. Most warehouse history bugs are one of these answered with the machinery of another.</p>
'''

# ------------------------------------------------------------------ 2 mechanism
anat_svg = '''
  <rect class="bx-y" x="10" y="20" width="740" height="40" rx="6"/>
  <text class="lbl" x="24" y="46">key</text><text class="lbl" x="110" y="46">sku</text><text class="lbl" x="200" y="46">category</text>
  <text class="lbl" x="400" y="46">valid_from</text><text class="lbl" x="540" y="46">valid_to</text><text class="lbl" x="670" y="46">current</text>
  <rect class="bx" x="10" y="66" width="740" height="40" rx="6"/>
  <text class="soft" x="24" y="92">812</text><text class="soft" x="110" y="92">K-100</text><text class="soft" x="200" y="92">Kitchen</text>
  <text class="soft" x="400" y="92">2025-09-01</text><text class="soft" x="540" y="92">2026-05-12</text><text class="soft" x="670" y="92">no</text>
  <rect class="bx-g" x="10" y="112" width="740" height="40" rx="6"/>
  <text class="soft" x="24" y="138">977</text><text class="soft" x="110" y="138">K-100</text><text class="soft" x="200" y="138">Small appliances</text>
  <text class="soft" x="400" y="138">2026-05-12</text><text class="soft" x="540" y="138">9999-12-31</text><text class="soft" x="670" y="138">yes</text>
  <path class="ln-d" d="M540 160 V176"/><text class="soft" x="540" y="196" text-anchor="middle">exclusive: [from, to)</text>
  <path class="ln-d" d="M110 160 V176"/><text class="soft" x="110" y="196" text-anchor="middle">natural key: same for both</text>
  <path class="ln-d" d="M24 160 V216"/><text class="soft" x="34" y="232">surrogate key: one per version, stored on facts</text>
'''
mechanism = '''
<p>A type 2 dimension is a history table with two extra promises: each version has its own <b>surrogate key</b>, and facts store that key, so they keep the version they were loaded with.</p>
''' + fig(760, 245, "The product dimension for the kettle. Two rows share natural key K-100. Row with surrogate key 812 is Kitchen, valid from 1 September 2025 to 12 May 2026, not current. Row 977 is Small appliances, valid from 12 May 2026 to 31 December 9999, current. The validity range includes its start and excludes its end.",
          anat_svg, "Two versions of one kettle. The end date of one is the start date of the next, and belongs to the next.") + '''
<h3>The columns, and why each exists</h3>
''' + tbl(["Column", "Purpose"], [
    ["<code>product_key</code>", "surrogate key per version; facts store it, so joins are one equality"],
    ["<code>sku</code>", "natural key from the source; ties all versions together"],
    ["tracked columns", "category, brand: a change here creates a version"],
    ["type 1 columns", "description, spelling: a change here updates every version"],
    ["<code>valid_from</code>, <code>valid_to</code>", "half-open range in business time: <code>&gt;= from AND &lt; to</code>"],
    ["<code>is_current</code>", "a convenience for “as it is” joins; derivable from <code>valid_to</code>"],
    ["<code>hashdiff</code>", "hash of the tracked columns, to detect a change cheaply"],
    ["<code>loaded_at</code>", "when the warehouse wrote the row (the other clock, chapter 4)"],
]) + mn("Use a far-future date such as 9999-12-31 for the open end, not NULL. Range joins and BETWEEN-style checks stay simple.") + full('''<h3>One load, step by step</h3>
<p>Each run compares today's source rows with the current dimension rows. Three outcomes per natural key: new (insert a first version), changed in a tracked column (close the current version, insert a new one), changed only in type 1 columns (update all versions in place).</p>
''' + code("dim_product_load.sql", "two statements, one transaction", '''
BEGIN;
-- 1 · close current versions whose tracked columns changed
UPDATE dim_product d
SET    valid_to = s.effective_from, is_current = false
FROM   stg_products s
WHERE  d.sku = s.sku AND d.is_current AND d.hashdiff <> s.hashdiff;

-- 2 · insert new versions (changed keys) and first versions (new keys)
INSERT INTO dim_product (sku, name, category, brand, valid_from, valid_to, is_current, hashdiff, loaded_at)
SELECT s.sku, s.name, s.category, s.brand,
       coalesce(s.effective_from, DATE '1900-01-01'), DATE '9999-12-31', true, s.hashdiff, now()
FROM   stg_products s
LEFT JOIN dim_product d ON d.sku = s.sku AND d.is_current
WHERE  d.sku IS NULL;           -- no current row: new key, or just closed above
COMMIT;
''') + '''<p>Where does <code>effective_from</code> come from? Ideally from the source: the date the category change takes effect. If the source has none, the load date is used, which is the origin of drill 3.</p>
<h3>Facts pick their version once</h3>
<p>The fact load joins on the natural key and the event time, finds exactly one version, and stores its surrogate key. After that, every report joins facts to dimensions on one integer column, and the past never moves.</p>
''' + code("fact_lookup.sql", "point-in-time lookup, at load time", '''
SELECT s.order_line_id, p.product_key, s.amount
FROM   stg_order_lines s
JOIN   dim_product p
  ON   p.sku = s.sku
 AND   s.sold_at >= p.valid_from
 AND   s.sold_at <  p.valid_to;
''') + '''<p>Order 9001's kettle, sold on 31 March, gets key 812 and will say <i>Kitchen</i> forever. A kettle sold on 20 May gets 977.</p>
<h3>When a member disappears</h3>
<p>Products are discontinued and customers close accounts. Deleting the dimension row would break every fact that points at it, so a delete in the source becomes a <b>closed version</b>: set <code>valid_to</code> to the deletion time, <code>is_current</code> to false, and insert nothing. The natural key then has no current version, which is exactly right: “current products” no longer includes it, and last year's sales still join. If the same SKU comes back later, the load sees a new key and inserts a fresh first version; the gap between the two versions is real and the no-gaps test (chapter 7) should allow it for keys that were deleted. Personal data is different: a customer who asks to be forgotten is anonymised in every version (chapter 8), not closed.</p>''')

# ------------------------------------------------------------------ 3 drills
fan_svg = '''
  <rect class="bx-y" x="20" y="40" width="230" height="56" rx="8"/><text class="lbl" x="135" y="64" text-anchor="middle">fact: kettle, 31 Mar</text><text class="soft" x="135" y="84" text-anchor="middle">sku K-100 · €39</text>
  <rect class="bx" x="460" y="20" width="270" height="44" rx="8"/><text class="soft" x="595" y="48" text-anchor="middle">812 · K-100 · Kitchen</text>
  <rect class="bx" x="460" y="76" width="270" height="44" rx="8"/><text class="soft" x="595" y="104" text-anchor="middle">977 · K-100 · Small appliances</text>
  <path class="ln-r" d="M252 60 L456 42" marker-end="url(#ar)"/><path class="ln-r" d="M252 76 L456 98" marker-end="url(#ar)"/>
  <text class="bad" x="380" y="160" text-anchor="middle" font-size="18">join on sku only: one sale, two rows, €78</text>
'''
drills = mn("Each drill is a report that looked fine until someone compared it with something else.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · sold twice</a></li><li><a href="#drill-2">2 · midnight</a></li><li><a href="#drill-3">3 · backdated</a></li>
  <li><a href="#drill-4">4 · no version yet</a></li><li><a href="#drill-5">5 · 700 million rows</a></li><li><a href="#drill-6">6 · lost change</a></li>
</ul>
''' + drill(1, "The kettle that sold twice", [
    ("Timeline", "An analyst writes a quick report joining <code>fact_sales</code> to <code>dim_product</code> on <code>sku</code>, because the fact table also has the SKU. Since 12 May the kettle has two versions. Every kettle sale now joins to both rows, and kettle revenue for the year doubles."),
    ("Why", "The natural key identifies the product, not the version. Joining on it matches every version. The error appears only after the first type 2 change, so it passes every test written before that.", True),
    ("What saves you", "Join facts on the surrogate key, always. If a natural key must be on the fact (for debugging), name it so nobody joins on it by accident, and add a test that the join on the surrogate key and the sum of facts give the same total. Grant analysts a view that has only the safe join."),
], "facts join dimensions on the surrogate key. A natural-key join multiplies rows the day history begins.") + fig(760, 180, "Drill 1. The kettle sale from 31 March, with SKU K-100 and 39 euros, joined on SKU alone, matches both versions of the kettle, 812 Kitchen and 977 Small appliances. One sale becomes two rows and 78 euros.",
                  fan_svg, "One sale, two versions, double the revenue.") + drill(2, "The sale at midnight", [
    ("Timeline", "The kettle's category change is stored with <code>valid_to = 2026-05-12 00:00</code> on the old row and <code>valid_from = 2026-05-12 00:00</code> on the new one. The lookup uses <code>BETWEEN valid_from AND valid_to</code>. A sale at exactly 00:00:00 on 12 May matches both versions; one in the web shop's time zone at 23:30 UTC on 11 May matches the wrong one."),
    ("Why", "<code>BETWEEN</code> includes both ends, so a shared boundary belongs to two versions. And the change was dated in local time while sales were in UTC.", True),
    ("What saves you", "Half-open ranges everywhere (<code>&gt;= from AND &lt; to</code>) and one time zone for every validity column and every event time, converted once in staging. Add a test that every fact matches exactly one version."),
], "half-open ranges, one time zone. A boundary belongs to the next version only.") + drill(3, "Customer 77 moved before we knew", [
    ("Timeline", "Customer 77 moves to Rotterdam on 1 February and tells the shop on 20 February. The CRM changes the city that day. The dimension load dates the new version from 20 February, the day it saw the change. Three orders between 1 and 20 February stay in Utrecht in the regional report forever."),
    ("Why", "The pipeline used load time as business time. The CRM knew the move date (the customer gave it), but the extract only copied the current city.", True),
    ("What saves you", "Extract the effective date when the source has one (<code>moved_on</code>), and date versions by it. Then decide what to do with facts already loaded: re-key the three February orders to the Rotterdam version (as was, corrected), or leave them and record the correction (as reported). Both are valid; the choice must be made, written down and applied the same way every time (chapter 4)."),
], "date versions by when the change took effect, not when you saw it, and decide how corrections reach old facts.") + drill(4, "The order that arrived before its customer", [
    ("Timeline", "A new customer signs up and orders within a minute. Orders arrive by CDC every 15 minutes; customers arrive from the CRM nightly. At 00:15 the order's lookup finds no customer version. The inner join drops it, and the day is €55 short until someone reloads it."),
    ("Why", "Facts and dimensions come from different sources on different schedules. “No version yet” was treated as “no customer”.", True),
    ("What saves you", "Never drop a fact for a missing version. Insert an <b>inferred member</b>: a version for the natural key with placeholder attributes, flagged as inferred, valid from the beginning of time. The nightly load then <i>updates</i> that inferred version in place (it never had real attributes to preserve) rather than adding a new one. Monitor how many facts point at inferred members."),
], "facts always load; a missing version becomes an inferred member, filled in when the dimension arrives.") + drill(5, "Seven hundred million customers", [
    ("Timeline", "<code>last_login_at</code> is on the CRM's customer table, and the snapshot tracks every column. Each day about 1.9 million of the 2 million customers log in or are touched. After a year <code>dim_customer</code> has 700 million rows, the fact lookup takes an hour, and “customers by city” needs a de-duplication nobody understands."),
    ("Why", "Type 2 on a fast-changing column turns a slowly changing dimension into a daily snapshot. Every version is a copy of every other column.", True),
    ("What saves you", "Track type 2 only on columns people group or filter by (city, segment, tier). Exclude fast-changing columns from change detection, or move them out: last login becomes an activity fact, and banded values (age band, spend band) go in a small <b>mini-dimension</b> referenced from the fact."),
], "type 2 is for slow, meaningful changes. Fast-changing columns belong in facts or mini-dimensions.") + drill(6, "The change that never happened", [
    ("Timeline", "The kettle's brand is changed by mistake at 10:00 and changed back at 15:00. The nightly snapshot sees no difference and records nothing. That is fine. But the price team made a real change at 09:00 and another at 16:00 on the same day, and only the 16:00 value was recorded. A report on promotions that ran that afternoon uses the wrong price."),
    ("Why", "A periodic snapshot (dbt snapshots run nightly, or any daily compare) sees only the state at each run. Changes between runs are lost, and short-lived values never existed as far as the warehouse knows.", True),
    ("What saves you", "Decide the resolution history needs. For most dimensions, daily is fine and losing a five-hour typo is a feature. Where intra-day changes matter (prices, stock), build history from the change log (CDC events, with their commit times) instead of from snapshots, or from the source's own history table."),
], "a snapshot only knows what it saw. If changes between runs matter, build history from the change log.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["facts store and join on the surrogate key", "1"],
    ["half-open ranges, one time zone", "2"],
    ["version by effective date; a written rule for corrections", "3"],
    ["inferred members, never dropped facts", "4"],
    ["type 2 only for slow, meaningful columns; mini-dimensions for the rest", "5"],
    ["history from the change log when intra-day changes matter", "6"],
]))

# ------------------------------------------------------------------ 4 hard problem
axes_svg = '''
  <path class="ln" d="M60 230 H730" marker-end="url(#a)"/><path class="ln" d="M60 230 V20" marker-end="url(#a)"/>
  <text class="soft" x="730" y="256" text-anchor="end">valid time: when it was true →</text>
  <text class="soft" x="70" y="22">recorded time: when we knew ↑</text>
  <path class="ln-d" d="M200 226 V30"/><text class="soft" x="200" y="250" text-anchor="middle">1 Feb</text>
  <path class="ln-d" d="M64 140 H730"/><text class="soft" x="56" y="144" text-anchor="end">20 Feb</text>
  <rect class="bx-r" x="200" y="142" width="530" height="84" rx="4"/><text class="lbl" x="465" y="190" text-anchor="middle">we still said Utrecht</text>
  <rect class="bx-g" x="200" y="40" width="530" height="96" rx="4"/><text class="lbl" x="465" y="94" text-anchor="middle">we know: Rotterdam</text>
  <rect class="bx" x="64" y="40" width="132" height="186" rx="4"/><text class="lbl" x="130" y="138" text-anchor="middle">Utrecht</text>
'''
hard = '''
<p>Customer 77's move has two dates: it <b>happened</b> on 1 February and it was <b>recorded</b> on 20 February. A report about February asked on 10 February and the same report asked on 1 March should give different answers, and both answers were right when given. Holding both is what the bitemporal note is about, and it is the hard problem of warehouse history.</p>
''' + fig(760, 265, "Two time axes for customer 77. Horizontally, valid time: when the city was true. Vertically, recorded time: when the warehouse knew. Before 1 February the city is Utrecht. From 1 February it is Rotterdam, but for anything recorded before 20 February the warehouse still said Utrecht; from 20 February on it knows Rotterdam.",
          axes_svg, "Valid time runs left to right, recorded time bottom to top. The red block is what we believed before we knew.") + '''
<h3>Three questions, three mechanisms</h3>
''' + tbl(["Question", "Called", "Answered by"], [
    ["“Kitchen revenue in March”", "as it was", "type 2 versions in valid time; facts keep their surrogate key"],
    ["“This year by today's regions”", "as it is", "type 1 columns, or the current attributes copied onto every version (type 6), or a join through the natural key to the current row"],
    ["“What did the report say on 15 July?”", "as it was reported", "versions also stamped with recorded time (bitemporal), or a filed snapshot of the report itself"],
], hot=(2,)) + mn("If nobody will ever ask the third question, don't build for it. Regulated businesses will be asked.") + full('''<h3>Answering “as it is” without breaking “as it was”</h3>
<p>Type 6 adds <code>current_region</code> to every version of every shop, updated in place whenever the shop changes. A report groups by <code>region</code> for as it was and by <code>current_region</code> for as it is, from the same facts and the same join. The cost: every change touches every old version of that shop, which is cheap for 30 shops and expensive for 2 million customers. For large dimensions, join from the version to its current row through the natural key instead:</p>
''' + code("as_is.sql", "today's region for the whole year", '''
SELECT cur.region AS region_today, sum(f.amount) AS revenue
FROM   fact_sales f
JOIN   dim_shop  v   ON v.shop_key = f.shop_key                 -- the version sold under
JOIN   dim_shop  cur ON cur.shop_code = v.shop_code AND cur.is_current
WHERE  f.order_date >= DATE '2026-01-01'
GROUP  BY 1;
''') + '''<h3>Answering “as it was reported”</h3>
<p>Add recorded time to the dimension: <code>recorded_from</code> and <code>recorded_to</code>. A correction never updates a row; it closes the old row's recorded range and inserts new rows. To see what the warehouse believed on 15 July, filter versions by <code>recorded_from &lt;= '2026-07-15' AND recorded_to &gt; '2026-07-15'</code> and then join by valid time as usual. Facts need the same treatment if they are corrected, which is why the cheaper answer is often to <b>snapshot the report</b> at filing time (chapter 8): store the numbers that were sent, with the date.</p>
<h3>Corrections: the rule you must write down</h3>
<p>Drill 3 forces a choice whenever a change arrives with an effective date in the past:</p>
''' + tbl(["Rule", "Old facts", "Good for"], [
    ["<b>Correct the past</b>", "re-keyed to the corrected version", "analysis: the truth as best known now"],
    ["<b>Keep what was loaded</b>", "unchanged; the version starts at the load date", "operational reports that must not move"],
    ["<b>Both (bitemporal)</b>", "corrected in valid time, old belief kept in recorded time", "audit and regulated reporting"],
]) + '''<p>Most shops pick the first for analysis and file a snapshot of each closed month for audit. That covers all three questions with one type 2 dimension and a folder of filed reports.</p>''')

# ------------------------------------------------------------------ 5 variants
variants = '''
<p>Four common ways to keep dimension history, with the drills and the three questions run against each.</p>
''' + tbl(["", "A · type 2 + surrogate keys on facts", "B · type 6 (A plus current columns)", "C · history table, point-in-time join at query time", "D · daily full snapshot of the dimension"], [
    ["how", "versions with keys; facts store the key", "as A, plus <code>current_*</code> columns updated in place", "versions with valid dates; facts keep natural key and event time", "a copy of the whole dimension per day"],
    ["as it was", "an equality join", "an equality join", "a range join on every query", "join on natural key and date"],
    ["as it is", "join through the natural key", "a column", "join to the current version", "join to today's copy"],
    ["as it was reported", "no (add recorded time)", "no (add recorded time)", "no (add recorded time)", "partly: snapshots are what you knew each day"],
    ["drill 1 (fan-out)", "avoided by the key", "avoided by the key", "<b>risk on every query</b>", "risk without the date in the join"],
    ["drill 3 (backdated)", "re-key facts to correct", "re-key facts to correct", "<b>free</b>: re-date the version, queries follow", "copies before 20 Feb keep Utrecht"],
    ["drill 5 (fast columns)", "explodes", "explodes", "explodes", "<b>size is fixed</b>: rows × days"],
    ["size, 2 M customers, 1 yr", "≈ 2.2 M rows", "≈ 2.2 M rows", "≈ 2.2 M rows", "≈ 730 M rows"],
], hot=(4, 5)) + mn("Variant C is how many lakehouses work now: cheap compute makes range joins affordable, and backdating gets easy.") + full('''<p>Variant A is the classic and still the default for facts that are queried many times: the range join happens once, at load time. Variant B adds as-is reporting for small dimensions. Variant C moves the range join to query time, which costs every query but makes corrections trivial: change a version's dates and every report follows, no fact reloads. It needs a view or metrics layer that always writes the date condition, or drill 1 returns. Variant D is the simplest to build (copy the table daily) and the most honest about what you knew each day, but it costs a full copy per day and loses intra-day changes.</p>
<h3>Choosing per dimension</h3>
''' + tbl(["Dimension", "Rows", "Changes", "Pick"], [
    ["<code>dim_shop</code>", "31", "a few a year, re-orgs", "B: regions both as was and as is"],
    ["<code>dim_product</code>", "40,000", "category and brand changes weekly", "A, with type 1 for descriptions"],
    ["<code>dim_customer</code>", "2 million", "moves, segment changes; backdated often", "A for city and segment, mini-dimension for bands; or C if corrections are frequent"],
    ["<code>dim_date</code>", "a few thousand", "never", "no history needed"],
]) + '''<h3>Making variant C safe</h3>
<p>The danger of query-time joins is drill 1 on every report someone writes. Give analysts a view that already contains the date condition, and grant them only the view:</p>
''' + code("sales_as_it_was.sql", "variant C, the only way analysts reach products", '''
CREATE VIEW sales_as_it_was AS
SELECT f.*, p.category, p.brand
FROM   fact_sales f
JOIN   product_history p
  ON   p.sku = f.sku
 AND   f.sold_at >= p.valid_from
 AND   f.sold_at <  p.valid_to;
''') + '''<p>Mixing them is normal. What must be consistent is the rule for corrections (chapter 4) and the habit of joining on keys or always writing the date condition.</p>''')

# ------------------------------------------------------------------ 6 numbers
numbers = '''
<p>The shop's dimensions are small next to its facts: 60 million order lines a year against a few million dimension rows. The numbers that matter are growth rates and join costs.</p>
<h3>How fast dimensions grow</h3>
''' + tbl(["Dimension", "Base rows", "Tracked changes a year", "Rows after 1 year", "After 5 years"], [
    ["products", "40,000", "~3 per product", "160,000", "640,000"],
    ["customers (city, segment)", "2,000,000", "~10 % move, ~15 % change segment", "2,500,000", "4,500,000"],
    ["customers (every column, drill 5)", "2,000,000", "~1.9 M touched a day", "~700,000,000", "billions"],
    ["shops", "31", "~2 re-orgs", "~90", "~350"],
]) + mn("A dimension that grows faster than its fact table is a sign that something which should be a fact was modelled as an attribute.") + full('''<h3>Where the range join is paid</h3>
<p>Variant A pays the point-in-time lookup once per fact row, at load: about 160,000 new order lines a day joined to 160,000 product versions, which takes seconds. Every report afterwards joins on an integer. Variant C pays it on every query: a year of sales, 60 million lines, range-joined to 160,000 versions. Modern warehouses do this in a few seconds for one report; a dashboard opened 300 times on a Monday pays it 300 times. Pre-join in an aggregate (by day, category as it was) and the difference disappears for the common reports.</p>
<h3>The cost of type 6</h3>
<p>Every change to a current attribute updates all versions of that member. For 31 shops a re-org touches a few hundred rows. For 2 million customers, a nightly segment recalculation that changes 300,000 customers' current segment updates every version of each of them, about 400,000 rows, every night. Fine in a columnar warehouse, but it makes the dimension a full rewrite target; prefer the join through the natural key for large dimensions.</p>
<h3>Sizing a mini-dimension</h3>
<p>Drill 5's fix moves fast-changing attributes into bands. Customers get an age band (6 values), a spend band over the last 12 months (5), a loyalty tier (4) and a newsletter flag (2). Every combination is one row: 6 × 5 × 4 × 2 = 240 rows, whatever the number of customers. Each fact stores both <code>customer_key</code> and <code>customer_profile_key</code>, looked up at load time, so “sales by spend band at the time” is a plain join. The bands change every month for many customers; the mini-dimension never grows. Keep bands coarse: if the combinations go past a few hundred thousand, it is a fact table in disguise.</p>
<h3>Daily snapshots, priced</h3>
<p>A daily copy of 2 million customers with 40 columns is about 400 MB compressed per day, 146 GB a year. Storage is cheap; scanning it is not. Point-in-time queries on snapshots must always filter by date first, or they scan the year. Partition by snapshot date and keep, for example, daily copies for 90 days and month-end copies after that.</p>''')

# ------------------------------------------------------------------ 7 testing
testing = '''
<p>History bugs don't fail loudly: a report is a little off, and only for periods after a change. Tests must check the shape of the history itself, on every load.</p>
''' + tbl(["Test", "Checks", "Catches"], [
    ["<b>one current version</b>", "exactly one <code>is_current</code> row per natural key", "half-applied loads"],
    ["<b>no overlaps</b>", "no two versions of a key share a moment", "drill 2, double matches"],
    ["<b>no gaps</b>", "each version's <code>valid_to</code> equals the next one's <code>valid_from</code>", "facts that match no version"],
    ["<b>facts match their version</b>", "each fact's event time is inside its version's range", "re-keying bugs, drill 3"],
    ["<b>joins don't multiply</b>", "sum of facts equals sum after joining every dimension", "drill 1"],
    ["<b>version growth</b>", "new versions per day within the usual band", "drill 5 before it costs a fortune"],
], hot=(1,)) + mn("The overlap test is the one to write first. Almost every history bug ends in two versions claiming the same moment.") + full(code("test_no_overlap.sql", "returns the offending pairs; must return none", '''
SELECT a.sku, a.product_key, b.product_key
FROM   dim_product a
JOIN   dim_product b
  ON   a.sku = b.sku
 AND   a.product_key < b.product_key
 AND   a.valid_from < b.valid_to
 AND   b.valid_from < a.valid_to;
''') + '''<h3>Facts that point at the wrong version</h3>
<p>After any re-keying (chapter 8) or a change to the lookup, check that each fact's event time lies inside the version it stores. It is a join on the key and a range check, cheap enough to run on the last 60 days every night.</p>
''' + code("test_fact_in_version.sql", "must return no rows", '''
SELECT f.order_line_id, f.sold_at, p.product_key, p.valid_from, p.valid_to
FROM   fact_sales f
JOIN   dim_product p ON p.product_key = f.product_key
WHERE  f.order_date >= current_date - 60
  AND  NOT (f.sold_at >= p.valid_from AND f.sold_at < p.valid_to);
''') + '''<h3>Unit tests for the load</h3>
<p>Feed the dimension load small, hand-made sequences and assert the resulting versions. The useful cases are exactly the drills:</p>
<ul>
<li>A change, then nothing: one closed version, one current.</li>
<li>A change and its undo within one run: no new version (or two, if history is built from the log; test whichever you chose).</li>
<li>A backdated change: the new version starts at the effective date, and the old one ends there.</li>
<li>A type 1 change: no new version, every version updated.</li>
<li>An inferred member followed by the real one: one version, updated, still the same key.</li>
<li>The same batch loaded twice: no change (idempotent).</li>
</ul>
<h3>Testing the three pasts</h3>
<p>Write one small fixture with all three of this year's changes in it: the kettle sold in March and in June, customer 77's February orders, and a Delft sale in May and one in August. Then assert one answer per question. March Kitchen revenue includes the March kettle and not the June one (as it was). The whole year by today's regions puts both Delft sales in South (as it is). The February regional report rebuilt with the correction puts customer 77 in Rotterdam, and the filed February report still says Utrecht (as it was reported). Three questions, five rows of data, and every later change to the dimension load is checked against them in seconds.</p>
<h3>Report tests across a change</h3>
<p>Pick a filed report, say March by category, and keep its numbers as a fixture. After any change to the dimension load, rebuild and compare: March must not move unless a deliberate correction says so.</p>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>History is a slow-moving thing to operate. Most of the work is noticing the unusual day and handling corrections with a rule rather than a script.</p>
''' + tbl(["Metric", "Means", "Alert when"], [
    ["<b>new versions per day</b>, per dimension", "how fast history grows", "more than 3× the usual (a bulk update or a new tracked column)"],
    ["<b>inferred members</b> still unfilled", "facts waiting for their dimension", "older than 2 days, or over 1 % of yesterday's facts"],
    ["<b>backdated changes</b> per day", "corrections reaching into closed periods", "any into a filed month"],
]) + mn("A spike in new versions is nearly always one script upstream that touched every row.") + full('''<h3>The runbook</h3>
''' + tbl(["Situation", "Do"], [
    ["a bulk update created a version for every row", "delete the versions created by that run (by <code>loaded_at</code>), reopen the previous ones, exclude the touched column from change detection, rerun"],
    ["a backdated change arrives for a filed month", "apply the written rule (chapter 4): re-key facts for analysis; the filed report snapshot stays as filed; log the correction"],
    ["the dimension load had a bug for weeks", "rebuild the dimension from raw (all change events or daily copies are still there), then re-key facts for the affected period"],
    ["a customer asks to be forgotten", "erase or anonymise the personal columns in every version, in raw and in snapshots; keep keys so facts still add up"],
    ["regions are reorganised", "a new version per shop with the new region from the effective date; <code>current_region</code> updated; publish both views to managers"],
]) + '''<h3>Re-keying facts after a correction</h3>
<p>When customer 77's move is backdated to 1 February, the three February orders still point at the Utrecht version. If the written rule is “correct the past”, re-key them in one idempotent statement, restricted to the affected key and dates, and log what changed:</p>
''' + code("rekey_customer_77.sql", "only the facts the correction touches", '''
UPDATE fact_sales f
SET    customer_key = c.customer_key
FROM   dim_customer c
WHERE  c.customer_no = :customer_no
  AND  f.customer_no = c.customer_no
  AND  f.sold_at >= c.valid_from AND f.sold_at < c.valid_to
  AND  f.customer_key <> c.customer_key
  AND  f.order_date >= :effective_from;   -- the corrected range only
''') + '''<p>Run it after the dimension load, inside the same write–audit–publish cycle, so aggregates and reports are rebuilt for the touched days before anyone sees a half-corrected February.</p>
<h3>Filing reports</h3>
<p>For anything sent outside the analytics team (month-end to finance, quarterly to the board, anything to a regulator), store what was sent: the numbers, the date, the version of the definitions. A table of filed results is cheaper and clearer than a bitemporal warehouse, and it answers the auditor's question exactly.</p>
''' + code("filed_reports.sql", "keep what you sent", '''
INSERT INTO filed_report_lines (report, period, filed_on, dimension_value, measure, value)
SELECT 'monthly_revenue_by_category', '2026-03', current_date, category, 'revenue', revenue
FROM   rpt_revenue_by_category
WHERE  month = '2026-03';
'''))

# ------------------------------------------------------------------ 9 tools
tools_ch = '''
<p>Many tools build history for you. Each gives one of the two clocks well and leaves the other, and the corrections rule, to you.</p>
''' + tbl(["Tool", "Gives you", "Clock", "Leaves to you"], [
    ["dbt snapshots", "type 2 tables from any source, by timestamp or by comparing columns; hard deletes as closed versions", "recorded (snapshot run time) unless you feed an effective date", "which columns to track; resolution is one run"],
    ["SQL Server temporal tables, MariaDB system versioning", "every update keeps the old row automatically, queryable with <code>FOR SYSTEM_TIME AS OF</code>", "recorded (system) time", "business-time validity; schema changes"],
    ["PostgreSQL: <code>periods</code>, <code>temporal_tables</code> extensions; SQL:2011 <code>PERIOD</code>", "application-time and system-time periods, overlap constraints", "either or both", "tool support varies by version"],
    ["Delta Lake change data feed, Iceberg snapshots", "every version of the table, and time travel to past states", "recorded (commit) time", "retention: time travel is not an archive"],
    ["Snowflake time travel", "the table as of up to 90 days ago", "recorded", "it is for recovery, not reporting"],
    ["AutomateDV, data vault satellites", "insert-only history per source, point-in-time tables", "recorded (load date), plus effective dates if modelled", "building stars on top"],
]) + mn("Time travel answers “what did the table look like on 15 July”, briefly. It is not a substitute for modelling history.") + full('''<h3>What the tools map to</h3>
''' + tbl(["Chapter", "Tool feature"], [
    ["2 · the load", "dbt snapshots (<code>check</code> strategy with <code>check_cols</code>), MERGE"],
    ["3 · drill 4", "dbt incremental models upserting inferred members"],
    ["3 · drill 6", "CDC (Debezium) into raw, history built from events"],
    ["4 · as it was reported", "system-versioned tables, filed report tables"],
    ["7 · tests", "dbt tests, <code>dbt_utils.mutually_exclusive_ranges</code> for overlaps and gaps"],
    ["8 · erasure", "the warehouse's delete or update across snapshot tables, plus raw retention"],
]) + '''<h3>Choosing the resolution</h3>
<p>Every snapshot-based tool records history at the frequency it runs. Run the customer snapshot nightly and a customer who changes segment twice in a day appears to have changed once. That is usually right for dimensions: reports group by the state that lasted, not by an hour-long typo. For the few attributes where every change matters (prices during a promotion, stock levels), take history from the change stream instead, where each event carries its own commit time, and keep the snapshot for everything else.</p>
<h3>The shop's snapshot, configured</h3>
''' + code("snapshots/customers.sql", "dbt: tracked columns only, effective date from the source", '''
{% snapshot customers_snapshot %}
{{ config(unique_key='customer_no',
          strategy='check',
          check_cols=['city', 'segment'],     -- not last_login_at (drill 5)
          hard_deletes='invalidate') }}
select customer_no, city, segment, moved_on,  -- effective date travels along
       name, email                             -- type 1: fixed up in the dimension model
from {{ ref('stg_customers') }}
{% endsnapshot %}
''') + '''<p>The snapshot dates versions by its run time. The dimension model on top of it then uses <code>moved_on</code>, when present, as <code>valid_from</code>, which handles drill 3 without hand-written version logic.</p>
<p>dbt snapshots are the most common starting point. Feed them an effective date column where the source has one, track only the columns that matter, and you have variant A or C with very little code.</p>''')

# ------------------------------------------------------------------ 10 lab
lab = '''
<p><b>The lab.</b> On 1 July the shop reorganises: regions North and South become North, South and Coast, and the Delft shop moves from North to South. Franchisees join the same month and will see their own shops' history. Three requests arrive the same week:</p>
<ol>
<li>Finance: “The half-year report by region, exactly as we filed it on 5 July.”</li>
<li>The new regional managers: “The whole of this year by the new regions, so we have a baseline.”</li>
<li>The auditor: “Show that the June figures in the filed report haven't changed since.”</li>
<li>A franchisee who bought the Delft shop: “My shop's sales since 1 January, by month.”</li>
<li>Someone proposes making region type 1, “so everything is in the new regions and simple”. What do you answer?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · As filed</summary><p>From the filed report table: the half-year numbers stored on 5 July. Not recomputed: the point is that they don't change.</p></details>
<details><summary>2 · As it is</summary><p><code>dim_shop</code> as type 6: each shop has a new version from 1 July with the new region, and <code>current_region</code> on every version. The managers' report groups by <code>current_region</code> over the whole year.</p></details>
<details><summary>3 · Unchanged since</summary><p>Rebuild June by region as it was (type 2 versions) and compare with the filed table. If a backdated correction has touched June since, the difference is listed in the corrections log with its date and reason.</p></details>
<details><summary>4 · The franchisee</summary><p>Join through the natural key (the shop code), not the version, so all of Delft's history counts, whatever region it was in. Row-level security on the shop code keeps other shops out (Vol. 9, embedded reporting).</p></details>
<details><summary>5 · Type 1 region</summary><p>No. It would silently rewrite the filed half-year report and every past regional comparison. Type 6 gives the managers the “everything in new regions” view with one column, without changing the past.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Design", ["Every column is classified: type 0, 1 or 2", "Fast-changing attributes are facts or mini-dimensions", "Validity is half-open, in one time zone", "The open end is a far-future date"]),
    ("Loading", ["Versions are dated by effective date where the source has one", "Change detection uses a hash of tracked columns only", "Missing versions become inferred members", "Loads are idempotent"]),
    ("Facts", ["Facts store the surrogate key, found by event time", "Nobody joins facts on the natural key", "Re-keying after corrections follows a written rule"]),
    ("Three questions", ["As it was: type 2 joins", "As it is: type 6 or a join through the natural key", "As reported: filed report snapshots, or recorded time"]),
    ("Tests", ["One current version per key", "No overlaps, no gaps", "Every fact inside its version's range", "Filed reports rebuilt and compared after load changes"]),
    ("Operations", ["New versions per day monitored", "Unfilled inferred members alerted", "Erasure covers every version, raw and snapshots"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="history-in-the-warehouse", no=13, title="History in the Warehouse",
    sub="Three changes followed through a year: a recategorised kettle, a customer whose move was recorded late, and a shop that changed region. Which past each report means, and how to keep all three.",
    summary="A deep dive on dimension history in a warehouse: type 2 mechanics, six failure drills, as it was, as it is and as it was reported, four variants compared, growth numbers, testing history, running it, tools, a lab and a checklist.",
    builds_on="Vol. 3, notes 04 and 17 · Vol. 9, notes 05 and 06",
    builds_on_links=[("History Tables", "../../data/notes/history-tables.html"), ("Bitemporal Data", "../../data/notes/bitemporal-data.html"),
                     ("Slowly Changing Dimensions", "../../pipelines/notes/slowly-changing-dimensions.html"),
                     ("Late-Arriving Data", "../../pipelines/notes/late-arriving-data.html")],
    notes=[("data", "history-tables"), ("data", "bitemporal-data"), ("pipelines", "slowly-changing-dimensions"), ("pipelines", "late-arriving-data")],
    facts=[("Example", "the kettle on 12 May, customer 77's move, Delft's new region")],
    blurb="Type 2 mechanics, six history bugs, as it was vs as it is vs as reported, four ways to keep history, and tests for it.",
    chapters=[
        dict(id="recap", nav="Recap", title="Four notes in sixty seconds",
             gist="History tables keep past versions, bitemporal data adds when you knew, slowly changing dimensions decide per column, and late-arriving data files events by when they happened. In a warehouse they meet in one question: which version of the past does this report mean?",
             body=recap),
        dict(id="mechanism", nav="Mechanism", title="The real mechanism: versions and keys",
             gist="A type 2 dimension keeps one row per version, with a surrogate key, the natural key, a half-open validity range and a hash of the tracked columns. Each load closes changed versions and inserts new ones. Facts find their version by event time once, at load, and store its key.",
             body=mechanism,
             check=[("Why use a far-future date instead of NULL for the open end?", "Range conditions stay simple and index-friendly; no special case for the current version."),
                    ("When does a fact find its dimension version?", "Once, at load time, by matching the natural key and the event time to a validity range; then it stores the surrogate key.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways history goes wrong: a natural-key join that doubles sales, a midnight boundary that belongs to two versions, a backdated move dated by load time, a fact dropped before its customer arrived, a fast-changing column that explodes the dimension, and changes between snapshots that were never seen.",
             body=drills,
             check=[("Kettle revenue doubled after 12 May. First thing to check?", "Whether a report joins facts to the dimension on the natural key instead of the surrogate key."),
                    ("Why not track last_login_at as type 2?", "It changes daily for most customers, turning the dimension into a daily copy; it belongs in a fact.")]),
        dict(id="three-pasts", nav="Three pasts", title="The hard problem: three pasts",
             gist="People mean three things by “last year”: as it was (type 2 in valid time), as it is (current attributes applied to the past), and as it was reported (what the warehouse knew on a date). Keep valid and recorded time apart, and write down one rule for corrections that reach into the past.",
             body=hard,
             check=[("Which mechanism answers “this year by today's regions”?", "Current attributes on every version (type 6) or a join through the natural key to the current row."),
                    ("What's the cheapest way to answer “what did the report say on 15 July”?", "Store the filed report's numbers when it is sent, with the date.")]),
        dict(id="variants", nav="Variants", title="Four ways to keep history",
             gist="Type 2 with keys on facts makes as-it-was joins cheap. Type 6 adds as-it-is columns for small dimensions. A history table with point-in-time joins at query time makes corrections free but every query pays. Daily snapshots are simple and honest about what you knew, and costly in size.",
             body=variants,
             check=[("Which variant makes backdated corrections easiest?", "A history table joined at query time: re-date the version and every report follows, without re-keying facts."),
                    ("Why is type 6 costly on large dimensions?", "Every change to a current attribute updates every version of that member.")]),
        dict(id="numbers", nav="Numbers", title="History in numbers",
             gist="Products grow from 40,000 to 160,000 versions a year; customers from 2 to 2.5 million; tracking last login would make 700 million. Range joins cost seconds once at load, or on every query at query time. A daily snapshot of customers is 146 GB a year compressed.",
             body=numbers,
             check=[("A dimension grows faster than its fact table. What does that suggest?", "A fast-changing value is modelled as an attribute instead of as a fact."),
                    ("Where does variant A pay for the range join?", "Once per fact row, at load time; reports join on integer keys afterwards.")]),
        dict(id="testing", nav="Testing", title="Testing history",
             gist="Test the shape of history on every load: one current version per key, no overlaps, no gaps, every fact inside its version, and joins that don't multiply. Unit test the load with the drills as cases, and rebuild filed reports to check they don't move.",
             body=testing,
             check=[("Which single test catches most history bugs?", "No overlapping versions per natural key."),
                    ("How do you check a load change didn't rewrite the past?", "Rebuild a filed report from the warehouse and compare it with the kept numbers.")]),
        dict(id="running", nav="Running it", title="Running it",
             gist="Watch new versions per day, unfilled inferred members and backdated changes. Keep a runbook for bulk-update explosions, backdated corrections, rebuilding from raw, erasure across every version, and re-organisations. File reports that leave the team.",
             body=running,
             check=[("New versions per day jump 50×. Likely cause?", "A bulk update upstream touched every row, or a fast-changing column started being tracked."),
                    ("A customer asks to be forgotten. Where must you act?", "Every version in the dimension, plus raw and any snapshots; keep keys so facts still add up.")]),
        dict(id="tools", nav="Tools", title="Tools",
             gist="dbt snapshots build type 2 tables, temporal tables keep system-time history, the SQL:2011 period extensions add both clocks, and lakehouse time travel shows past table states. Each gives one clock well; effective dates, resolution and the corrections rule stay yours.",
             body=tools_ch),
        dict(id="lab", nav="Lab", title="A lab and the checklist",
             gist="The lab reorganises regions mid-year: finance wants the filed half-year, managers want the year in new regions, the auditor wants proof June didn't move, and a franchisee wants their shop's whole history. The checklist turns the dive into review questions.",
             body=lab),
    ],
    sources="Ralph Kimball and Margy Ross, <i>The Data Warehouse Toolkit</i>, 3rd ed. (2013), chapter 5 (types 0–7, mini-dimensions, inferred members). Richard Snodgrass, <i>Developing Time-Oriented Database Applications in SQL</i> (1999). Tom Johnston, <i>Bitemporal Data</i> (2014). The SQL:2011 temporal features. dbt documentation, “Snapshots”. Microsoft documentation, “Temporal tables”.",
)
