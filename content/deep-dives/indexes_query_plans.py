# Deep dive 10 · Indexes & Query Plans. Builds on Vol. 3 notes 05 (indexing), 06 (batch loading, fixing N+1) and
# 07 (keyset pagination). Example, from the indexing note: the orders table with 10 million rows, and customer 42's
# "my orders" page: WHERE customer_id = 42 ORDER BY placed_at DESC LIMIT 20. Examples use PostgreSQL.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
life_svg = '''
  <rect class="bx" x="10" y="60" width="120" height="56" rx="8"/><text class="lbl" x="70" y="86" text-anchor="middle">SQL text</text><text class="soft" x="70" y="106" text-anchor="middle">what you want</text>
  <rect class="bx" x="170" y="60" width="110" height="56" rx="8"/><text class="lbl" x="225" y="93" text-anchor="middle">parse</text>
  <rect class="bx-y" x="320" y="60" width="130" height="56" rx="8"/><text class="lbl" x="385" y="86" text-anchor="middle">planner</text><text class="soft" x="385" y="106" text-anchor="middle">picks the cheapest</text>
  <rect class="bx" x="490" y="60" width="120" height="56" rx="8"/><text class="lbl" x="550" y="86" text-anchor="middle">executor</text><text class="soft" x="550" y="106" text-anchor="middle">reads pages</text>
  <rect class="bx" x="650" y="60" width="100" height="56" rx="8"/><text class="lbl" x="700" y="93" text-anchor="middle">rows</text>
  <path class="ln" d="M130 88 H168" marker-end="url(#a)"/><path class="ln" d="M280 88 H318" marker-end="url(#a)"/><path class="ln" d="M450 88 H488" marker-end="url(#a)"/><path class="ln" d="M610 88 H648" marker-end="url(#a)"/>
  <rect class="bx-g" x="300" y="160" width="170" height="44" rx="8"/><text class="lbl" x="385" y="187" text-anchor="middle">statistics</text>
  <path class="ln" d="M385 158 V118" marker-end="url(#a)"/><text class="soft" x="480" y="146">guesses from samples</text>
  <path class="ln-d" d="M320 36 H610"/><text class="soft" x="465" y="26" text-anchor="middle">EXPLAIN ANALYZE shows this part</text>
'''
recap = '''
<p>The orders table has 10 million rows. Customer 42 opens “my orders”, which asks for their 20 newest orders. Without the right index the database reads all 10 million rows to find 312. Three notes from the data volume deal with making reads like this fast.</p>
''' + tbl(["Note", "In one line"], [
    ["Indexing", "a sorted copy of some columns with pointers to the rows, so a query jumps instead of scanning"],
    ["Batch Loading (Fixing N+1)", "fetch related rows in one query, not one query per row"],
    ["Keyset Pagination", "ask for rows after the last one shown, not for page 5,000"],
]) + fig(760, 215, "The life of one query. The SQL text says what you want. It is parsed, then the planner picks the cheapest way to answer it, using statistics that are guesses from samples of the data. The executor then reads pages and returns rows. EXPLAIN ANALYZE shows the planner's choice and what the executor actually did.",
         life_svg, "You write what you want. The planner decides how, from guesses. Most slow queries are a bad guess or a missing option.") + mn("The indexing note's going-deeper chapter covers reading a plan in four lines and choosing column order. This dive starts there.") + '''
<p class="full">The notes teach the tools. This deep dive is about the system that uses them: a planner that decides from statistics, which can be wrong; a table that serves many queries at once, so indexes are chosen for a workload, not a query; and a plan that can change overnight with no deploy. The goal is to be able to answer the most common question in database work: “this was fast yesterday, why is it slow today?”</p>
'''

# ------------------------------------------------------------------ 2 the planner
planner = '''
<p>SQL says what you want, never how to get it. For the “my orders” query the planner could read the whole table and sort, or walk an index on <code>customer_id</code>, or walk an index on <code>placed_at</code> backwards until it has found 20 rows for customer 42. It estimates the cost of each option and picks the cheapest.</p>
<h3>Where the estimates come from</h3>
''' + tbl(["Statistic", "Kept per column", "Used to guess"], [
    ["number of distinct values", "about 9 million customers… or 4 statuses", "how many rows <code>= x</code> matches"],
    ["most common values and how common", "<code>DELIVERED</code> 90 %, <code>PENDING</code> 0.1 %", "matches for frequent values"],
    ["a histogram of the rest", "placed_at spread over five years", "matches for ranges such as “last week”"],
    ["correlation with physical order", "placed_at follows insert order closely", "whether index reads are scattered or sequential"],
]) + mn("Statistics are a sample, refreshed by ANALYZE. Until then, the planner plans for the table as it was.") + '''
<p>From these, the planner estimates how many rows each step returns, multiplies by the cost of reading pages, and adds up. The costs are in arbitrary units: reading a page in sequence costs 1, reading a page at random costs 4 by default.</p>
''' + full('''<h3>When a full scan is the right answer</h3>
<p>An index lookup reads a few index pages and then one table page per matching row, at random. A full scan reads every page, but in sequence. If a query wants a large share of the table, the scan wins.</p>
''' + tbl(["Query matches", "Likely plan", "Why"], [
    ["312 rows of 10 million", "index scan", "a few hundred random reads beat 125,000 sequential ones"],
    ["5 % of the table", "it depends", "500,000 random reads is close to reading everything"],
    ["40 % of the table", "full scan", "the index would visit most pages anyway, out of order"],
]) + '''<p>“The planner ignored my index” is often the planner being right. Check the actual row count before arguing with it.</p>
<h3>Three ways the guesses go wrong</h3>
''' + tbl(["Cause", "Example", "Fix"], [
    ["<b>stale statistics</b>", "2 million rows loaded an hour ago; the planner thinks the table is small (drill 3)", "<code>ANALYZE</code> after bulk loads"],
    ["<b>correlated columns</b>", "<code>city = 'Rotterdam' AND country = 'NL'</code>: the planner multiplies two probabilities as if unrelated and expects 50 times too few rows", "extended statistics: <code>CREATE STATISTICS … (dependencies)</code>"],
    ["<b>costs set for old disks</b>", "random reads priced at 4 on an SSD where they cost about the same as sequential ones", "lower <code>random_page_cost</code> to about 1.1 on SSDs"],
]) + '''<p>The third row is worth checking on every database you run. With the default setting on fast storage, the planner will prefer full scans in many places where an index would be quicker.</p>
<h3>Asking for the plan safely</h3>
<p><code>EXPLAIN</code> on its own shows the plan the planner would choose and its estimates, without running anything. <code>EXPLAIN ANALYZE</code> runs the query and adds what really happened, which is what you need to compare estimates with reality. Two cautions. It really runs: an <code>UPDATE</code> or <code>DELETE</code> under <code>EXPLAIN ANALYZE</code> changes data, so wrap it in a transaction and roll back. And it runs with the values you typed; to see the plan the application gets, use the same parameter values, and for prepared statements, the same way of sending them (drill 4).</p>''')

# ------------------------------------------------------------------ 3 reading a plan
plans = '''
<p>Here is the “my orders” query before and after the index from the note, as <code>EXPLAIN (ANALYZE, BUFFERS)</code> prints it. Read from the most indented line upward: it runs first.</p>
''' + code("before.txt", "no suitable index: 1.9 seconds", '''
Limit  (actual time=1912.4..1912.4 rows=20 loops=1)
  Buffers: shared hit=2113 read=121887
  ->  Sort  (actual time=1912.4..1912.4 rows=20 loops=1)
        Sort Key: placed_at DESC
        Sort Method: top-N heapsort  Memory: 27kB
        ->  Seq Scan on orders  (cost=0.00..248000.00 rows=290 width=72)
                                (actual time=0.9..1911.8 rows=312 loops=1)
              Filter: (customer_id = 42)
              Rows Removed by Filter: 9999688
Execution Time: 1912.6 ms
''', plain=True) + code("after.txt", "index on (customer_id, placed_at DESC): 0.1 ms", '''
Limit  (actual time=0.041..0.088 rows=20 loops=1)
  Buffers: shared hit=24
  ->  Index Scan using orders_customer_placed on orders  (cost=0.43..92.10 rows=290 width=72)
                                                         (actual time=0.040..0.084 rows=20 loops=1)
        Index Cond: (customer_id = 42)
Execution Time: 0.11 ms
''', plain=True) + tbl(["Line", "Before", "After", "What it tells you"], [
    ["bottom node", "Seq Scan", "Index Scan", "how rows are found"],
    ["Rows Removed by Filter", "9,999,688", "none", "work the index should have done"],
    ["estimated vs actual rows", "290 vs 312", "290 vs 20 (stopped early)", "estimates are fine; this is a missing index, not bad statistics"],
    ["Sort node", "yes", "no", "the index returns rows already in order, so the database stops after 20"],
    ["Buffers", "124,000 pages", "24 pages", "the steadiest number to compare plans by"],
]) + mn("Compare plans by pages read, not by milliseconds. Time depends on what else the server was doing.") + '''
<h3>Plans with joins</h3>
<p>The page also shows each order's lines. The join adds a node with two children, and a new number to watch: <code>loops</code>.</p>
''' + code("join.txt", "the inner side runs once per outer row", '''
Nested Loop  (actual time=0.06..0.41 rows=46 loops=1)
  ->  Index Scan using orders_customer_placed on orders o  (actual rows=20 loops=1)
        Index Cond: (customer_id = 42)
  ->  Index Scan using order_lines_order_id on order_lines l  (actual rows=2 loops=20)
        Index Cond: (order_id = o.id)
''', plain=True) + full('''<p>The inner scan ran 20 times, once for each order, returning about 2 rows each time. The figures on a looped line are per loop: multiply by <code>loops</code> for the total. A nested loop with <code>loops=200000</code> and a slow inner side is the most common shape of a join gone wrong.</p>
''' + tbl(["Join method", "How", "Good when"], [
    ["<b>Nested loop</b>", "for each outer row, look up matching inner rows", "the outer side is small and the inner side has an index on the join column"],
    ["<b>Hash join</b>", "build a hash table of one side, stream the other through it", "both sides are large, equality join, no useful order"],
    ["<b>Merge join</b>", "walk two inputs already sorted on the join key", "both sides come sorted, often from indexes"],
]) + '''<p>None is good or bad by itself. A nested loop is perfect for 20 orders and a disaster for 2 million, which is what happens when the planner expected 20 (drill 3).</p>
<h3>Two more scan types</h3>
''' + tbl(["Scan", "What it does", "When you see it"], [
    ["<b>Bitmap Index Scan + Bitmap Heap Scan</b>", "collects every matching row's position from the index first, sorts them by page, then reads each table page once", "medium result sizes, or when two indexes are combined with AND or OR"],
    ["<b>Index Only Scan</b>", "answers from the index without visiting the table", "every column the query needs is in the index, and the table is recently vacuumed"],
]) + '''<p>An Index Only Scan line also reports <code>Heap Fetches</code>: rows it had to check in the table after all, because the page was not yet marked as fully visible. A high number there means vacuum is behind, and the index-only scan is quietly doing the table reads it was meant to avoid.</p>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Each of these is a query that “used to be fast”. Guess the cause before reading it.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · lower()</a></li><li><a href="#drill-2">2 · wrong type</a></li><li><a href="#drill-3">3 · after the import</a></li>
  <li><a href="#drill-4">4 · the rare status</a></li><li><a href="#drill-5">5 · 61 queries</a></li><li><a href="#drill-6">6 · fourteen indexes</a></li>
</ul>
''' + drill(1, "The index on email that never gets used", [
    ("Timeline", "Sign-in looks up <code>WHERE lower(email) = lower($1)</code>, so that capital letters do not matter. There is an index on <code>email</code>. The plan is a full scan of 9 million customers."),
    ("Why", "The index is sorted by <code>email</code>, not by <code>lower(email)</code>. A function on the column means the database must compute it for every row before comparing.", True),
    ("What saves you", "Index the expression the query uses: <code>CREATE INDEX ON customers (lower(email))</code>. Or store emails lowercase in the first place, or use a case-insensitive type. The same applies to <code>date(placed_at)</code>, <code>col + 1</code> and anything else that wraps the column."),
], "an index helps only when the query compares the indexed value itself. Wrap the column, lose the index.") + drill(2, "The id that arrived as the wrong type", [
    ("Timeline", "After an ORM upgrade, order lookups by customer go from 1 ms to 2 seconds. The SQL text looks the same. The plan shows <code>Filter: ((customer_id)::numeric = '42'::numeric)</code>."),
    ("Why", "The new driver sends the parameter as a decimal number. To compare a whole-number column with a decimal, the database converts the column, on every row, which is drill 1 in disguise.", True),
    ("What saves you", "Make parameter types match column types: declare them in the query or the mapping. Read the plan's filter line after any driver or ORM upgrade: a <code>::</code> cast on the column side is the sign. MySQL has the same trap with text columns compared to numbers."),
], "a type mismatch converts the column, and a converted column cannot use its index.") + drill(3, "The plan changed after the nightly import", [
    ("Timeline", "At 02:00 a job loads 2 million order lines from a partner. At 02:05 the reconciliation report starts. Yesterday it took 40 seconds. Today it is still running at 06:00."),
    ("What you see", "The plan expects 200 rows from the new lines and chooses a nested loop with an index lookup per row. There are 2 million. Statistics are from yesterday, because the automatic analyse had not run yet.", True),
    ("What saves you", "Run <code>ANALYZE</code> at the end of every bulk load, as part of the job. Log the plans of slow queries automatically (chapter 8), so a plan change is visible the next morning, not in a 4-hour incident."),
], "after a bulk change, refresh the statistics before anything queries the new data.") + drill(4, "Fast for one status, slow for another", [
    ("Timeline", "The warehouse screen runs <code>WHERE status = $1 ORDER BY placed_at</code>, as a prepared statement. For <code>PENDING</code>, 0.1 % of rows, it is instant. After a few calls it becomes slow for <code>PENDING</code> too."),
    ("Why", "After five executions PostgreSQL may switch a prepared statement to a generic plan, one made without looking at the value. That plan is chosen for an average status, which is <code>DELIVERED</code> at 90 %: a full scan.", True),
    ("What saves you", "Give the rare value its own index and query: a partial index <code>ON orders (placed_at) WHERE status = 'PENDING'</code> serves the warehouse screen exactly and stays tiny. Where a value-dependent plan is essential, the statement can be told to plan for each value (<code>plan_cache_mode</code>)."),
], "skewed data needs value-aware plans. Rare values deserve their own partial index.") + drill(5, "Sixty-one queries for one page", [
    ("Timeline", "The order history page shows 20 orders, each with its lines and each line's product name. Every query is under a millisecond. The page takes 900 ms."),
    ("What you see", "One query for the orders, 20 for the lines, 40 for the products: 61 round trips. Each is fast; the waiting between them is not. With a slow network to the database it is 3 seconds.", True),
    ("What saves you", "Batch loading, from the note: one query for the orders, one for all their lines (<code>WHERE order_id = ANY($1)</code>), one for all their products. Three round trips, whatever the page size. Add a test that counts queries per request (chapter 9), because N+1 returns every time someone adds a field."),
], "count queries per request. A page should make a fixed number, not one per row.") + drill(6, "Fourteen indexes on one table", [
    ("Timeline", "Over three years each new screen added an index to <code>orders</code>. There are now fourteen. Checkout has slowed down by 40 %, and the write-ahead log has tripled."),
    ("Why", "Every insert writes the row and fourteen index entries. Every update to an indexed column, and <code>updated_at</code> is indexed, writes new entries in every index, because PostgreSQL can only skip index updates when no indexed column changed.", True),
    ("What saves you", "Find indexes that are never used and drop them: nine of the fourteen had no scans in a month, on the leader <i>and</i> on every replica. Merge indexes that share leading columns. Do not index columns that change on every update unless a frequent query needs them."),
], "every index is paid for on every write. Keep only the ones a real query uses.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["index the expression the query uses, never a wrapped column", "1"],
    ["parameter types match column types; read the filter line after upgrades", "2"],
    ["ANALYZE after bulk loads; log slow plans automatically", "3"],
    ["rare values get partial indexes; watch generic plans on skewed data", "4"],
    ["a fixed number of queries per request, tested", "5"],
    ["unused and overlapping indexes are found and dropped", "6"],
]))

# ------------------------------------------------------------------ 5 indexing a workload
workload = '''
<p>Indexing one query is easy: put its equality columns first, then its sort, then its ranges. The hard problem is that a table serves many queries, every index costs every write, and the best set is the smallest one that serves the queries that matter.</p>
<h3>Start from where the time goes</h3>
<p>Rank queries by <b>total</b> time, calls × average time. A 2-second report run twice a day matters less than a 4 ms query run 3,000 times a second.</p>
''' + tbl(["#", "Query on orders (from pg_stat_statements)", "Calls / s", "Avg", "Share of total time"], [
    ["Q1", "<code>customer_id = ? ORDER BY placed_at DESC LIMIT 20</code>", "900", "1.9 s", "most of it"],
    ["Q2", "<code>status = 'PENDING' ORDER BY placed_at</code>", "40", "300 ms", "a lot"],
    ["Q3", "<code>customer_id = ? AND placed_at &gt; ?</code>", "120", "1.1 s", "a lot"],
    ["Q4", "<code>id = ?</code>", "3,000", "0.05 ms", "little: the primary key serves it"],
    ["Q5", "monthly revenue by country", "0.001", "40 s", "little, but it hurts when it runs"],
], hot=(0, 1, 2)) + '''
<h3>The smallest set that serves them</h3>
''' + tbl(["Index", "Serves", "Note"], [
    ["<code>(customer_id, placed_at DESC)</code>", "Q1 and Q3", "one index, two queries: they share the leading column"],
    ["<code>(placed_at) WHERE status = 'PENDING'</code>", "Q2", "partial: holds 0.1 % of rows, so it is tiny and cheap to keep"],
    ["primary key on <code>id</code>", "Q4", "already there"],
    ["none", "Q5", "runs on a read copy or the warehouse, where a scan is fine"],
]) + mn("Three questions for every new index: which query, how often, and which existing index could serve it instead?") + full('''<h3>Shapes worth knowing</h3>
''' + tbl(["Shape", "Example", "Use when"], [
    ["<b>composite</b>", "<code>(customer_id, placed_at)</code>", "queries filter on one column and sort or range on another"],
    ["<b>covering</b>", "<code>(customer_id, placed_at) INCLUDE (total, status)</code>", "a hot query needs a few extra columns; the database answers from the index alone (Index Only Scan)"],
    ["<b>partial</b>", "<code>… WHERE status = 'PENDING'</code>", "queries always target a small, well-defined subset"],
    ["<b>expression</b>", "<code>(lower(email))</code>", "queries compare a computed value (drill 1)"],
    ["<b>GIN</b>", "on a JSONB column or a text search vector", "queries look inside documents, arrays or words"],
    ["<b>BRIN</b>", "on <code>placed_at</code> of a huge append-only table", "rows are stored roughly in the column's order; tiny, but coarse"],
]) + '''<h3>One composite index or two single ones?</h3>
<p>With separate indexes on <code>customer_id</code> and on <code>placed_at</code>, the planner can combine them with a bitmap AND. It works, but it has to read every entry for customer 42 and every entry in the date range, intersect them, and then sort, because a bitmap loses the index order. The composite index <code>(customer_id, placed_at DESC)</code> walks straight to customer 42's newest orders and stops after 20. Combining single-column indexes is a reasonable fallback for rare ad-hoc filters, such as an admin screen with ten optional fields. For the queries that carry the product, give them the composite index they need.</p>
<h3>Finding what to drop</h3>
''' + code("unused-indexes.sql", "never scanned since statistics were last reset", '''
SELECT relname AS table_name, indexrelname AS index_name, idx_scan,
       pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;
''') + '''<p>Three cautions before dropping anything. The counts are per server, so check every replica: a report may use an index only there. Unique indexes enforce a rule even if no query ever scans them. And a monthly job will look unused if statistics were reset two weeks ago. When in doubt, mark the index invisible first where the database supports it, or drop it in a quiet week with its <code>CREATE</code> statement at hand.</p>''')

# ------------------------------------------------------------------ 6 numbers
btree_svg = '''
  <rect class="bx-y" x="320" y="16" width="120" height="38" rx="6"/><text class="lbl" x="380" y="41" text-anchor="middle">root</text>
  <rect class="bx" x="90" y="88" width="130" height="38" rx="6"/><text x="155" y="113" text-anchor="middle">1 – 3,000,000</text>
  <rect class="bx-y" x="315" y="88" width="130" height="38" rx="6"/><text x="380" y="113" text-anchor="middle">… – 6,000,000</text>
  <rect class="bx" x="540" y="88" width="130" height="38" rx="6"/><text x="605" y="113" text-anchor="middle">… – 9,000,000</text>
  <path class="ln" d="M350 54 L170 86"/><path class="ln" d="M380 54 V86" marker-end="url(#a)"/><path class="ln" d="M410 54 L590 86"/>
  <rect class="bx" x="200" y="160" width="110" height="34" rx="6"/><rect class="bx-y" x="325" y="160" width="110" height="34" rx="6"/><rect class="bx" x="450" y="160" width="110" height="34" rx="6"/>
  <text class="soft" x="380" y="182" text-anchor="middle">42, 42, 42 …</text>
  <path class="ln" d="M360 126 L260 158"/><path class="ln" d="M380 126 V158" marker-end="url(#a)"/><path class="ln" d="M400 126 L500 158"/>
  <rect class="bx-g" x="320" y="226" width="120" height="34" rx="6"/><text x="380" y="248" text-anchor="middle">20 table rows</text>
  <path class="ln" d="M380 194 V224" marker-end="url(#a)"/>
  <text class="soft" x="600" y="36">level 1: 1 page</text><text class="soft" x="690" y="113">level 2</text><text class="soft" x="600" y="182">leaves: 30,000 pages</text>
  <text class="soft" x="470" y="248">then the rows themselves</text>
'''
numbers = '''
<p>A few numbers make index behaviour predictable instead of mysterious.</p>
''' + fig(760, 270, "A B-tree index on 10 million orders. One root page points to a few hundred pages on the second level, which point to about 30,000 leaf pages. Finding customer 42 reads the root, one second-level page and one leaf, which lists customer 42's entries in order; then the matching table rows are read.",
          btree_svg, "Three page reads to find customer 42 among 10 million rows, then one read per row returned.") + tbl(["Quantity", "Reasoning", "Value"], [
    ["entries per index page", "8 KB page, about 30 bytes per entry for two columns and a pointer", "about 250"],
    ["levels for 10 million rows", "250 × 250 = 62,500 leaves can hold 15 million entries", "3"],
    ["levels for 10 billion rows", "250 × 250 × 250 × 250", "5"],
    ["index size", "10 million × 30 bytes, plus room in pages", "about 400 MB"],
    ["table size", "10 million rows × about 100 bytes", "about 1 GB, 125,000 pages"],
    ["full scan", "125,000 pages, sequential", "1–2 s from disk"],
    ["index lookup for 20 rows", "3 index pages + 20 table pages", "under 1 ms, mostly from memory"],
]) + mn("Depth grows with the logarithm: a thousand times more rows adds two levels. That is why indexes keep working as tables grow.") + full('''<h3>What indexes cost</h3>
''' + tbl(["Cost", "For the orders table"], [
    ["each insert", "1 table write + 1 write per index; with 3 indexes, 4 page changes, with 14, 15"],
    ["each update of an indexed column", "a new entry in every index (drill 6)"],
    ["memory", "the hot parts of every index want to stay in memory; 14 indexes of 400 MB compete for it"],
    ["vacuum and replication", "more index pages to clean and more log to ship"],
]) + '''<h3>OFFSET against keyset, in pages</h3>
''' + tbl(["Page of 20", "OFFSET reads", "Keyset reads"], [
    ["1", "20 rows", "20 rows"],
    ["50", "1,000 rows", "20 rows"],
    ["5,000", "100,000 rows", "20 rows"],
], hot=(2,)) + '''<p>An export that walks all 500,000 orders of a big customer with OFFSET reads 6 billion rows in total; with keyset it reads 500,000. The keyset pagination note explains the query; the index from chapter 5, with <code>id</code> added as a final tie-breaker, makes it work.</p>''')

# ------------------------------------------------------------------ 7 joins, N+1, pagination
access = '''
<p>Many slow pages are not one bad query but a bad pattern of queries. Three patterns account for most of them.</p>
<h3>1 · Batch the related rows</h3>
''' + code("order-history.ts", "three queries, whatever the page size", '''
const orders = await db.many(
  `SELECT id, placed_at, total FROM orders
   WHERE customer_id = $1 ORDER BY placed_at DESC, id DESC LIMIT 20`, [customerId]);

const lines = await db.many(
  `SELECT order_id, product_id, qty FROM order_lines WHERE order_id = ANY($1)`,
  [orders.map((o) => o.id)]);

const products = await db.many(
  `SELECT id, name FROM products WHERE id = ANY($1)`,
  [[...new Set(lines.map((l) => l.product_id))]]);
''') + '''
<p>Each <code>ANY</code> query needs an index on the column it looks up: <code>order_lines(order_id)</code> and the primary key of products. A JOIN would also work; the point is the fixed number of round trips. ORMs offer the same thing as eager loading, and GraphQL servers as a DataLoader.</p>
<h3>2 · Page by key</h3>
''' + code("next-page.sql", "keyset: the last row shown is the bookmark", '''
SELECT id, placed_at, total
FROM orders
WHERE customer_id = $1
  AND (placed_at, id) < ($2, $3)      -- the last row of the previous page
ORDER BY placed_at DESC, id DESC
LIMIT 20;
-- served by an index on (customer_id, placed_at DESC, id DESC)
''') + mn("The index order must match the ORDER BY exactly, tie-breaker included, or the database sorts again.") + full('''<h3>3 · Ask only for what you show</h3>
''' + tbl(["Habit", "Why it matters for plans"], [
    ["select named columns, not <code>*</code>", "a covering index can answer the query alone; <code>*</code> always visits the table"],
    ["avoid exact <code>count(*)</code> on big lists", "counting 2 million rows reads them all; show “more than 1,000” or an estimate"],
    ["filter in SQL, not in code", "fetching 10,000 rows to keep 20 moves the full scan into your application"],
    ["one query per screen region, not per item", "the same rule as batch loading, applied to the whole page"],
]) + '''<h3>OR, IN and optional filters</h3>
<p>Search screens with optional fields tend to produce one query with many <code>OR</code>s: <code>(status = $1 OR $1 IS NULL) AND (placed_at &gt; $2 OR $2 IS NULL)</code>. It looks tidy and plans badly, because the planner must choose one plan that works whether or not each filter is set, and that is usually a full scan. Build the <code>WHERE</code> clause from the filters actually given, so each combination gets its own plan. A list of values, <code>status = ANY($1)</code>, is fine: an index handles it as several lookups.</p>
<h3>Ranges and the column order</h3>
<p>The indexing note's rule, equality columns first, then sort, then ranges, has one consequence that surprises people. In an index on <code>(customer_id, placed_at, status)</code>, a query with a range on <code>placed_at</code> can only <i>filter</i> by status, not jump to it: the range ends the useful part. If status is often an equality condition, put it before the range: <code>(customer_id, status, placed_at)</code>.</p>''')

# ------------------------------------------------------------------ 8 running it
running = '''
<p>Plans change without deploys: data grows, statistics refresh, values shift. Running a database well means seeing those changes before customers do.</p>
''' + tbl(["Tool", "Shows", "Setting for the shop"], [
    ["<b>pg_stat_statements</b>", "every query shape with calls, total time, rows and pages", "always on; review the top 10 by total time weekly"],
    ["<b>auto_explain</b>", "the actual plan of any query slower than a threshold, in the log", "log plans slower than 500 ms, with timing for a sample"],
    ["<b>slow query log</b>", "the text of slow queries", "on, at 500 ms"],
    ["<b>pg_stat_user_tables</b>", "sequential scans per table, last analyse time", "alert on a table with many large scans that used to have none"],
]) + mn("Rank by total time, not by slowest. The worst query is usually a fast one called very often.") + '''
<h3>Graphs per query shape</h3>
''' + tbl(["Graph", "Means trouble when"], [
    ["slow-case response time", "it jumps on a day without a deploy: a plan changed"],
    ["rows read per row returned", "it climbs: the query is filtering more and more; an index stopped fitting"],
    ["calls per request", "it grows with page size: N+1"],
    ["pages read from disk, not memory", "it rises for an index-heavy query: the working set no longer fits in memory"],
]) + full('''<h3>Runbook: “this query was fast yesterday”</h3>
<ol>
  <li><b>Get today's plan</b> from auto_explain, and yesterday's if you logged it. Compare the bottom nodes and the estimated against actual rows.</li>
  <li><b>Estimates far off?</b> Run <code>ANALYZE</code> on the tables involved and look again (drill 3). If they are still off, look for correlated columns.</li>
  <li><b>Estimates fine, plan still bad?</b> Look for a cast on a column (drill 2), a function on a column (drill 1), or a generic plan for a skewed value (drill 4).</li>
  <li><b>Same plan, more time?</b> More data, or less memory: compare pages read from disk. The fix is usually an index that fits, or partitioning old rows away (the Sharding & Partitioning dive).</li>
  <li><b>Did an index disappear?</b> Check recent migrations. A dropped “unused” index that a monthly job needed shows up exactly like this.</li>
</ol>
<h3>Does the working set fit in memory?</h3>
<p>An index lookup of three pages is fast when those pages are in memory and much slower when each is a disk read. The pages that matter are the hot ones: the upper levels of every index (always in memory, they are small) and the leaves and table pages for recent data. Watch the share of pages served from memory per query shape. When it falls for an index-heavy query, the hot data has outgrown memory: more memory, fewer or smaller indexes, or partitioning old rows away will help; a new index will not.</p>
<h3>Changing indexes on a live table</h3>
<p>Build indexes with <code>CREATE INDEX CONCURRENTLY</code> so writes continue, give the statement a lock timeout, and check afterwards that it finished valid. The Zero-Downtime Change dive has the details; the short version is that an ordinary <code>CREATE INDEX</code> on a busy table blocks every write until it is done.</p>''')

# ------------------------------------------------------------------ 9 testing
testing = '''
<p>Query performance is hard to test because it depends on data size and shape, which test databases rarely have. A few kinds of test still catch most regressions.</p>
''' + tbl(["Test", "How", "Catches"], [
    ["<b>Query count per request</b>", "a test helper counts queries while a request runs and fails above a fixed number", "N+1 (drill 5), every time it returns"],
    ["<b>Plan check on realistic data</b>", "seed a test database with production-like volume and skew; assert key queries use the expected index", "missing indexes, casts, functions on columns"],
    ["<b>Migration lint</b>", "fail a migration that creates an index without CONCURRENTLY, or adds a 15th index to a hot table", "locks and write amplification"],
    ["<b>Hypothetical index</b>", "try an index without building it (HypoPG) and read the plan", "whether an index would be used, before paying for it"],
    ["<b>Load test with real distributions</b>", "replay a sample of production query shapes and values", "skew problems (drill 4) that uniform test data hides"],
]) + mn("Test data with every customer having 5 orders hides every problem in this dive. Real customers have 3 or 30,000.") + code("order-history.test.ts", "two guards in one test", '''
test("order history: fixed query count, uses the index", async () => {
  const counter = db.countQueries();
  await request(app).get("/customers/42/orders").expect(200);
  expect(counter.total()).toBeLessThanOrEqual(3);            // orders, lines, products

  const plan = await db.explain(
    "SELECT id FROM orders WHERE customer_id = 42 ORDER BY placed_at DESC, id DESC LIMIT 20");
  expect(plan).toContain("Index Scan using orders_customer_placed");
  expect(plan).not.toContain("Seq Scan on orders");
});
''') + full('''<p>The plan check only means something on a table big enough that the planner would choose differently. A few hundred thousand rows with a realistic spread usually suffice; the seed script is worth more than any individual test, because every query test uses it.</p>
<h3>Seed data with the right shape</h3>
''' + tbl(["Real shape", "Seed it as"], [
    ["most customers have a few orders, a few have thousands", "order counts drawn from a long-tailed distribution, plus a handful of giant customers"],
    ["90 % of orders are DELIVERED, 0.1 % PENDING", "the same proportions, not one row of each"],
    ["five years of history, most reads on the last month", "dates spread over five years, with recent months fuller"],
    ["emails with mixed case, product names in many languages", "real-looking text, so expression indexes and collations are exercised"],
]) + '''
<h3>Review plans like code</h3>
<p>For the few queries that carry the product, keep their expected plan shape in the repository next to the query: which index, which join method, roughly how many pages. When a change makes the plan test fail, the pull request shows the old and new plans side by side, and a person decides whether the new one is better. That turns “the database got slow” from a mystery into a diff.</p>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>Tools</h3>
''' + tbl(["Need", "PostgreSQL", "Elsewhere"], [
    ["find expensive query shapes", "pg_stat_statements", "MySQL performance_schema; SQL Server Query Store"],
    ["see real plans of slow queries", "auto_explain", "MySQL slow log with EXPLAIN ANALYZE; Query Store"],
    ["read a plan visually", "explain.dalibo.com, PEV2, pgMustard", "MySQL Workbench visual explain"],
    ["try an index without building it", "HypoPG", "invisible indexes in MySQL and Oracle"],
    ["continuous advice", "pganalyze, Datadog and other database monitoring", "the cloud provider's performance insights"],
]) + mn("Tools find the slow query. Reading its plan is still the skill.") + '''
<h3>Lab</h3>
<p>Support gets a new screen: find orders by customer email, optionally by status, within a date range, newest first, 50 per page. Most searches cover the last 30 days. <code>PENDING</code> is 0.1 % of orders; <code>DELIVERED</code> is 90 %.</p>
<ol class="keep">
  <li>Emails are stored as typed by customers. How does the search find the customer?</li>
  <li>Which index serves “this customer's orders in a date range, newest first”? Can an existing one be reused?</li>
  <li>“All PENDING orders this week” with no customer: what serves it?</li>
  <li>How is paging done, and what index does it need?</li>
  <li>Support also wants “total orders found”. What do you show?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The email</summary><p>An expression index on <code>lower(email)</code> in customers, and the query compares <code>lower(email) = lower($1)</code> (drill 1). That gives the customer id in one index lookup.</p></details>
<details><summary>2 · Date range</summary><p>The existing <code>(customer_id, placed_at DESC)</code> already serves it: equality on the customer, then a range and sort on the date. Adding <code>id DESC</code> at the end makes it serve keyset paging too. No new index.</p></details>
<details><summary>3 · Pending this week</summary><p>The partial index <code>(placed_at) WHERE status = 'PENDING'</code> from chapter 5. It is tiny, and the query is a short range scan of it. A filter on <code>DELIVERED</code> without a customer would match most of the table and should be refused or sent to the warehouse.</p></details>
<details><summary>4 · Paging</summary><p>Keyset on <code>(placed_at, id)</code>, with the index ordered the same way, tie-breaker included. No OFFSET: support staff do page deep into busy customers.</p></details>
<details><summary>5 · The total</summary><p>An exact count can read millions of rows. Count up to 1,000 with a limited subquery and show “1,000 or more”, or show the planner's estimate labelled as approximate.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Finding the work", ["pg_stat_statements is on and reviewed by total time", "Slow plans are logged automatically with auto_explain", "Every index has a named query it serves"]),
    ("Designing indexes", ["Equality columns first, then sort, then range", "One index serves several queries where they share leading columns", "Rare values use partial indexes; computed comparisons use expression indexes", "Hot queries that need a few extra columns use covering indexes", "Frequently updated columns are indexed only when needed"]),
    ("Queries", ["No functions or casts on indexed columns in WHERE", "Parameter types match column types", "Pages make a fixed number of queries; related rows are batched", "Lists page by key with a unique tie-breaker, never deep OFFSET", "Big counts are capped or estimated"]),
    ("Statistics and plans", ["ANALYZE runs after every bulk load", "random_page_cost suits the storage", "Correlated columns have extended statistics", "Skewed values are checked against generic plans"]),
    ("Change and cleanup", ["Indexes are built concurrently, with a lock timeout", "Unused indexes are checked on every replica before dropping", "Index count on hot tables is reviewed in migration lint"]),
    ("Tests", ["Request tests assert a maximum query count", "Key queries are plan-checked on realistic, skewed data", "Expected plans for core queries are kept in the repository"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="indexes-query-plans", no=10, title="Indexes & Query Plans",
    sub="Why a query was fast yesterday and slow today: how the planner decides, how to read what it decided, and how to index a whole workload.",
    summary="A deep dive on indexes and query plans: how the planner estimates, reading EXPLAIN ANALYZE, six failure drills, indexing a workload, B-tree numbers and the cost of writes, batch loading and keyset paging, monitoring plans, and testing query performance.",
    builds_on="Vol. 3, notes 05, 06 and 07",
    builds_on_links=[("Indexing", "../../data/notes/indexing.html"), ("Batch Loading (Fixing N+1)", "../../data/notes/n-plus-one.html"),
                     ("Keyset Pagination", "../../data/notes/keyset-pagination.html")],
    notes=[("data", "indexing"), ("data", "n-plus-one"), ("data", "keyset-pagination")],
    facts=[("Example", "customer 42's “my orders” page on a 10-million-row table")],
    blurb="How the planner decides, reading EXPLAIN ANALYZE, six failure drills, indexing a workload, the cost of every index.",
    chapters=[
        dict(id="recap", nav="Recap", title="Three notes in sixty seconds",
             gist="An index lets a query jump to its rows, batch loading replaces one query per row with one query per set, and keyset pagination keeps deep pages fast. Behind all three sits the planner, which chooses how to run each query from statistics. This deep dive is about that planner and the workload it serves.",
             body=recap),
        dict(id="planner", nav="The planner", title="How the planner decides",
             gist="The planner estimates how many rows each step returns from sampled statistics, prices the page reads, and picks the cheapest plan. A full scan is right when a query wants a large share of the table. Plans go wrong when statistics are stale, columns are correlated, or costs are set for old disks.",
             body=planner,
             check=[("A query matches 40 % of the table and uses a full scan. Is the planner wrong?", "Probably not. Reading every page in order is cheaper than visiting most of them at random through an index."),
                    ("Why lower random_page_cost on SSDs?", "The default assumes random reads cost four times sequential ones, which is true for spinning disks. On SSDs it makes the planner avoid indexes it should use.")]),
        dict(id="plans", nav="Reading plans", title="Reading a real plan",
             gist="Read EXPLAIN ANALYZE from the most indented line up. Look at the scan type, rows removed by filter, estimated against actual rows, any Sort node and the pages read. In joins, figures on an inner line are per loop. Compare plans by pages read, not milliseconds.",
             body=plans,
             check=[("Estimated rows 200, actual 2,000,000, nested loop. What happened, and the first step?", "The planner expected few rows and chose a per-row lookup. Run ANALYZE and check the estimate again."),
                    ("An inner Index Scan shows rows=2 loops=20. How many rows did it return in total?", "40: the figures are per loop.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six queries that used to be fast: a function on an indexed column, a parameter of the wrong type, statistics that lag behind a bulk load, a generic plan for a skewed value, a page that makes sixty-one queries, and a table so heavily indexed that every write is slow.",
             body=drills,
             check=[("The plan shows Filter: ((customer_id)::numeric = 42). Why is the index unused?", "The column is being converted to numeric for every row, because the parameter arrived as a decimal. Make the types match."),
                    ("Only the warehouse's PENDING screen got slow, and only after a few calls. Likely cause?", "A prepared statement switched to a generic plan chosen for the common status. A partial index for PENDING fixes it.")]),
        dict(id="workload", nav="Workload", title="Indexing a workload: the hard problem",
             gist="Rank queries by total time, then find the smallest set of indexes that serves the important ones: shared leading columns let one index serve several queries, partial indexes serve rare subsets cheaply, and reports go elsewhere. Drop indexes nobody uses, after checking every replica.",
             body=workload,
             check=[("A 40-second monthly report and a 4 ms query run 900 times a second. Which matters more?", "The 4 ms query: about 3.6 seconds of database time every second, against 40 seconds a month."),
                    ("An index shows zero scans on the leader. Why not drop it at once?", "A replica may use it, it may enforce uniqueness, or a monthly job may need it since statistics were last reset.")]),
        dict(id="numbers", nav="Numbers", title="Indexes in numbers",
             gist="A B-tree on 10 million rows is three levels deep, so a lookup reads three index pages and then one page per row. Depth grows very slowly with size. Every index adds a write to every insert and competes for memory. Keyset pages read the same 20 rows however deep you go.",
             body=numbers,
             check=[("Roughly how many levels for 10 billion rows?", "About five, with around 250 entries per page."),
                    ("Why does an export with OFFSET get slower page by page?", "Each page re-reads every row before it, so the work grows with the page number; keyset reads only the page itself.")]),
        dict(id="access", nav="Access patterns", title="Batching, paging and asking less",
             gist="Load related rows in one query per set, page by the last key shown with a unique tie-breaker, select only the columns you show, and avoid exact counts on big lists. Put equality columns before the range in an index, because a range ends the useful part.",
             body=access,
             check=[("Why does SELECT * prevent an index-only scan?", "The index holds only some columns, so the database must visit the table for the rest."),
                    ("Index (customer_id, placed_at, status), query with a range on placed_at and status = 'PENDING'. What happens to status?", "It can only be filtered row by row; the range on placed_at ends the part of the index that can be searched.")]),
        dict(id="running", nav="Running it", title="Running it: watching plans change",
             gist="Keep pg_stat_statements on and review the top queries by total time. Log the plans of slow queries automatically. Watch rows read per row returned and calls per request. When a query slows overnight, compare plans, refresh statistics, then look for casts, functions and generic plans.",
             body=running,
             check=[("Rows read per row returned for a query climbs from 1 to 400 over a month. What does it suggest?", "The query increasingly filters instead of seeking: an index no longer fits the query, or the data shifted under it."),
                    ("Why build indexes CONCURRENTLY on live tables?", "An ordinary CREATE INDEX blocks writes to the table until it finishes.")]),
        dict(id="testing", nav="Testing", title="Testing query performance",
             gist="Assert a maximum number of queries per request to stop N+1. Check the plans of key queries on seeded data with realistic volume and skew. Lint migrations for unsafe or excessive indexes, try indexes hypothetically before building them, and keep expected plans for core queries in the repository.",
             body=testing,
             check=[("Why does a plan test on a 1,000-row table prove little?", "At that size the planner may scan everything whatever the indexes are; plans only match production on realistic volume and skew."),
                    ("What does a query-count test catch that a plan test does not?", "N+1: each query has a good plan, but the page makes one per row.")]),
        dict(id="tools", nav="Tools & lab", title="Tools, a lab and the checklist",
             gist="pg_stat_statements finds the expensive queries, auto_explain records their plans, visualisers help read them and HypoPG tries indexes for free; other databases have equivalents. The lab designs indexes for a support search screen, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="The PostgreSQL documentation: “Using EXPLAIN”, “Planner Statistics”, “Indexes” and “Planner Method Configuration”. Markus Winand, <i>SQL Performance Explained</i> and use-the-index-luke.com. Hironobu Suzuki, <i>The Internals of PostgreSQL</i>. Laurenz Albe and the Cybertec blog on generic plans and plan_cache_mode. The HypoPG and auto_explain documentation.",
)
