# SQL · a laminated reference card in four pages.
# Rendered by scripts/build_notes.py (render_cheatsheet); Graph, Diagram, cmd, code and box come from scripts/cheatsheet.py.
# Examples are PostgreSQL; MySQL and SQL Server differences are called out where they bite.
# Boxes flow into a 3-column grid (dense packing), so order them to fill rows: wide (2) + narrow (1).

SLUG = "sql"
TITLE = "SQL"
SUBTITLE = "queries, joins, window functions, indexes and transactions"
DESC = ("A four-page SQL cheat sheet: the order a query really runs in, NULL rules, joins as Venn diagrams, set operations, "
        "CTEs, window functions, upserts, indexes, reading EXPLAIN, transactions and isolation levels.")
VERSION = "v1 · Nov 2026"
BLURB = ("Four laminated pages: query order and NULLs, joins as pictures, window functions and everyday patterns, "
         "indexes, EXPLAIN and transactions. PostgreSQL first, MySQL and SQL Server where they differ.")
LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
        '<ellipse cx="17" cy="9" rx="9" ry="3.5" fill="none" stroke="var(--b-dev)" stroke-width="2.4"/>'
        '<path d="M8 9v16c0 2 4 3.5 9 3.5s9-1.5 9-3.5V9" fill="none" stroke="var(--b-dev)" stroke-width="2.4"/>'
        '<path d="M8 17c0 2 4 3.5 9 3.5s9-1.5 9-3.5" fill="none" stroke="var(--b-bug)" stroke-width="2.4"/></svg>')

# ---------------------------------------------------------------- page 1 · queries
def order():
    d = Diagram("The logical order a SELECT runs in: FROM and JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY, "
                "LIMIT. It is written starting with SELECT, but SELECT runs fifth.", 880, 140)
    steps = [("FROM · JOIN", "pick + join tables", "dev"), ("WHERE", "filter rows", "bug"), ("GROUP BY", "make groups", "feat"),
             ("HAVING", "filter groups", "feat"), ("SELECT", "compute columns", "main"), ("DISTINCT", "drop duplicates", "main"),
             ("ORDER BY", "sort", "rel"), ("LIMIT", "cut", "rel")]
    x = 14
    for i, (label, sub, tone) in enumerate(steps):
        d.node(f"s{i}", x, 34, 96, 50, label, sub, tone)
        if i:
            d.arrow(f"s{i - 1}", f"s{i}", None, tone="ink")
        d.text(x + 48, 24, f"{i + 1}", "dt strong", "middle")
        x += 108
    d.text(14, 110, "Written: SELECT · FROM · JOIN · WHERE · GROUP BY · HAVING · ORDER BY · LIMIT.")
    d.text(14, 128, "So a SELECT alias can't be used in WHERE, but works in ORDER BY; and WHERE can't use aggregates: that's HAVING's job.")
    return d.svg()


PAGE_QUERY = dict(
    title="Queries",
    kicker="the order it really runs in, filters, NULLs, grouping",
    figure=order(),
    boxes=[
        box("Anatomy of a query", code('''
SELECT c.country,
       COUNT(*)            AS orders,
       SUM(o.total)        AS revenue,
       AVG(o.total)::numeric(10,2) AS avg_order
FROM   orders o
JOIN   customers c ON c.id = o.customer_id
WHERE  o.created_at >= DATE '2026-01-01'
  AND  o.status <> 'cancelled'
GROUP  BY c.country
HAVING COUNT(*) >= 10  -- groups, after grouping
ORDER  BY revenue DESC
LIMIT  5;
'''), "dev", "wide", "top 5 countries"),
        box("NULL rules", '''
<ul class="checks nul">
<li><code>NULL = NULL</code> is <b>unknown</b>, not true: use <code>IS NULL</code></li>
<li>WHERE keeps only <b>true</b> rows; unknown is dropped</li>
<li><code>COUNT(*)</code> counts rows, <code>COUNT(col)</code> skips NULLs</li>
<li><code>SUM</code>, <code>AVG</code> ignore NULLs; all-NULL → NULL</li>
<li><code>COALESCE(a, b, 0)</code> first non-NULL</li>
<li><code>NULLIF(x, 0)</code> avoids divide-by-zero</li>
<li><b>!</b> <code>NOT IN (subquery)</code> with a NULL inside returns <b>nothing</b>: use <code>NOT EXISTS</code></li>
<li>Postgres: <code>a IS DISTINCT FROM b</code> = NULL-safe <code>&lt;&gt;</code></li>
</ul>''', "warn"),
        box("Filters", '''
<dl class="kv">
<dt><code>IN (1, 2, 3)</code></dt><dd>any of a list</dd>
<dt><code>BETWEEN a AND b</code></dt><dd>inclusive at <b>both</b> ends</dd>
<dt><code>LIKE 'ab%'</code></dt><dd><code>%</code> any text, <code>_</code> one char</dd>
<dt><code>ILIKE</code></dt><dd>case-insensitive (Postgres)</dd>
<dt><code>EXISTS (…)</code></dt><dd>at least one row matches</dd>
<dt><code>= ANY(array)</code></dt><dd>Postgres array match</dd>
</dl>
<p class="fine">Dates: prefer <code>&gt;= '2026-01-01' AND &lt; '2026-02-01'</code> over BETWEEN: no 23:59:59 bugs.</p>''', "bug"),
        box("CASE &amp; conditional counts", code('''
SELECT customer_id,
  CASE WHEN total >= 100 THEN 'big'
       WHEN total >= 20  THEN 'medium'
       ELSE 'small' END            AS size,
  COUNT(*) FILTER (WHERE status = 'paid')  AS paid,
  SUM(CASE WHEN status = 'refunded'
           THEN 1 ELSE 0 END)     AS refunds
FROM orders GROUP BY 1, 2;
''') + '<p class="fine"><code>FILTER</code> is Postgres / SQLite; <code>SUM(CASE …)</code> works everywhere.</p>', "feat", "wide"),
        box("Same thing, three dialects", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th></th><th>Postgres</th><th>MySQL</th><th>SQL Server</th></tr></thead>
<tbody>
<tr><th>first n rows</th><td><code>LIMIT 10</code></td><td><code>LIMIT 10</code></td><td><code>TOP 10</code> / <code>FETCH</code></td></tr>
<tr><th>concat</th><td><code>a || b</code></td><td><code>CONCAT(a,b)</code></td><td><code>a + b</code> / <code>CONCAT</code></td></tr>
<tr><th>now</th><td><code>now()</code></td><td><code>NOW()</code></td><td><code>SYSDATETIME()</code></td></tr>
<tr><th>auto id</th><td><code>GENERATED … AS IDENTITY</code></td><td><code>AUTO_INCREMENT</code></td><td><code>IDENTITY(1,1)</code></td></tr>
<tr><th>cast</th><td><code>x::int</code></td><td colspan="2"><code>CAST(x AS INT)</code> (works in all three)</td></tr>
<tr><th>truncate date</th><td><code>date_trunc('month', d)</code></td><td><code>DATE_FORMAT(d,'%Y-%m-01')</code></td><td><code>DATETRUNC(month, d)</code></td></tr>
</tbody></table></div>''', "ink", "full"),
    ],
)

# ---------------------------------------------------------------- page 2 · joins
def venn(d, i, cx, kind, label, sub):
    cy, r = 46, 27
    ax, bx = cx - 17, cx + 17
    circ = lambda x, cls="", clip="": f'<circle {cls}{clip}cx="{x}" cy="{cy}" r="{r}"/>'
    defs = (f'<clipPath id="vA{i}">{circ(ax)}</clipPath><clipPath id="vB{i}">{circ(bx)}</clipPath>')
    fill = {
        "inner": circ(bx, 'class="vf" ', f'clip-path="url(#vA{i})" '),
        "left": circ(ax, 'class="vf" '),
        "right": circ(bx, 'class="vf" '),
        "full": circ(ax, 'class="vf" ') + circ(bx, 'class="vf" '),
        "anti": circ(ax, 'class="vf" ') + circ(bx, 'class="vm" ', f'clip-path="url(#vA{i})" '),
    }[kind]
    vo = 'class="vo" '
    d.raw(f'<defs>{defs}</defs><g class="vg">{fill}</g>{circ(ax, vo)}{circ(bx, vo)}'
          f'<text class="vt" x="{ax - 11}" y="{cy + 4}">A</text><text class="vt" x="{bx + 11}" y="{cy + 4}">B</text>'
          f'<text class="vl" x="{cx}" y="{cy + r + 20}">{label}</text><text class="vs" x="{cx}" y="{cy + r + 35}">{sub}</text>')


def joins():
    d = Diagram("Joins as Venn diagrams: INNER keeps matches only; LEFT keeps all of A; RIGHT keeps all of B; FULL keeps "
                "everything; LEFT anti-join keeps A rows with no match in B; CROSS pairs every row of A with every row of B.",
                880, 124)
    slots = [("inner", "INNER JOIN", "matches only"), ("left", "LEFT JOIN", "all A + matches"),
             ("right", "RIGHT JOIN", "all B + matches"), ("full", "FULL JOIN", "everything"),
             ("anti", "A without B", "LEFT JOIN … IS NULL")]
    for i, (kind, label, sub) in enumerate(slots):
        venn(d, i, 73 + i * 146, kind, label, sub)
    # CROSS JOIN: every row with every row
    cx = 803
    lines = "".join(f'<path class="ar t-dev" d="M{cx - 22} {28 + a * 18} L{cx + 22} {28 + b * 18}"/>' for a in range(3) for b in range(3))
    dots = "".join(f'<circle class="vo" cx="{cx - 22}" cy="{28 + a * 18}" r="4"/><circle class="vo" cx="{cx + 22}" cy="{28 + a * 18}" r="4"/>'
                   for a in range(3))
    d.raw(lines + dots + f'<text class="vl" x="{cx}" y="{93}">CROSS JOIN</text><text class="vs" x="{cx}" y="{108}">every A × every B</text>')
    return d.svg()


PAGE_JOIN = dict(
    title="Joins &amp; combining",
    kicker="which rows survive, and how to stack results",
    figure=joins(),
    boxes=[
        box("Join syntax", code('''
-- INNER: orders that have a customer
SELECT o.id, c.name
FROM orders o JOIN customers c ON c.id = o.customer_id;

-- LEFT: every customer, with or without orders
SELECT c.name, COUNT(o.id) AS orders  -- COUNT(o.id), not COUNT(*)
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.name;

-- anti-join: customers who never ordered
SELECT c.* FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);

-- self-join: employee and manager
SELECT e.name, m.name AS manager
FROM employees e LEFT JOIN employees m ON m.id = e.manager_id;
'''), "dev", "wide", "postgres"),
        box("Join traps", '''
<ol class="cs-steps">
<li><b>Fan-out:</b> joining two one-to-many tables multiplies rows, so sums double. Aggregate each side first, then join.</li>
<li><b>ON vs WHERE in a LEFT JOIN:</b> a condition on B in <code>WHERE</code> turns it into an inner join. Put it in <code>ON</code>.</li>
<li><b>Missing ON</b> (or a wrong one) = an accidental cross join.</li>
<li><b>NOT IN + NULL</b> returns no rows. Use <code>NOT EXISTS</code>.</li>
<li>Join on columns with the <b>same type</b>; casts kill indexes.</li>
</ol>''', "main"),
        box("Set operations", '''
<dl class="kv">
<dt>UNION</dt><dd>stack + remove duplicates (sorts: slower)</dd>
<dt>UNION ALL</dt><dd>stack, keep all: the default choice</dd>
<dt>INTERSECT</dt><dd>rows in both</dd>
<dt>EXCEPT</dt><dd>rows in the first, not the second (<code>MINUS</code> in Oracle)</dd>
</dl>
<p class="fine">Same number of columns, compatible types, names from the first query.</p>''', "feat"),
        box("Subquery or CTE?", code('''
WITH monthly AS (           -- name a step
  SELECT date_trunc('month', created_at) AS m,
         SUM(total) AS revenue
  FROM orders GROUP BY 1
)
SELECT m, revenue,
       revenue - LAG(revenue) OVER (ORDER BY m) AS growth
FROM monthly ORDER BY m;
''') + '<p class="fine">CTEs read top to bottom; use them for steps. A correlated subquery runs per row: fine with an index, slow without.</p>', "bug", "wide"),
        box("Semi-join: EXISTS vs IN vs JOIN", '''
<dl class="kv">
<dt>EXISTS</dt><dd>“has at least one”; stops at the first match; NULL-safe</dd>
<dt>IN</dt><dd>fine for small lists and non-NULL subqueries</dd>
<dt>JOIN</dt><dd>only when you need B's columns; watch for duplicates</dd>
</dl>''', "ink", "full"),
    ],
)

# ---------------------------------------------------------------- page 3 · window functions & patterns
def window():
    d = Diagram("GROUP BY collapses each group to one row; a window function keeps every row and adds a value computed "
                "over its partition.", 880, 238)
    rows = [("A", "10"), ("A", "20"), ("B", "5"), ("B", "15"), ("B", "30")]
    d.group("gl", 14, 10, 410, 222, "GROUP BY customer", "feat")
    d.group("gr", 446, 10, 420, 222, "SUM(amount) OVER (PARTITION BY customer)", "dev")
    for i, (c, a) in enumerate(rows):
        tone = "feat" if c == "A" else "bug"
        d.node(f"l{i}", 30, 34 + i * 33, 110, 27, f"{c} · {a}", None, tone, "soft chip")
        d.node(f"r{i}", 462, 34 + i * 33, 110, 27, f"{c} · {a}", None, tone, "soft chip")
        tot = "30" if c == "A" else "50"
        rn = [1, 2, 1, 2, 3][i]
        d.node(f"w{i}", 640, 34 + i * 33, 210, 27, f"{c} · {a} · sum {tot} · rn {rn}", None, tone, "chip")
        d.arrow(f"r{i}", f"w{i}", None, tone="ink")
    d.node("ga", 250, 60, 150, 30, "A · 30", None, "feat", "chip")
    d.node("gb", 250, 122, 150, 30, "B · 50", None, "bug", "chip")
    for i in range(2):
        d.arrow(f"l{i}", "ga", None, tone="feat")
    for i in range(2, 5):
        d.arrow(f"l{i}", "gb", None, tone="bug")
    d.text(30, 222, "5 rows in → 2 rows out", "dt")
    d.text(462, 222, "5 rows in → 5 rows out, each with its group's total · rn = ROW_NUMBER()", "dt")
    return d.svg()


PAGE_WIN = dict(
    title="Window functions &amp; patterns",
    kicker="rankings, running totals, top-N, upserts, paging",
    figure=window(),
    boxes=[
        box("Window functions", code('''
SELECT customer_id, created_at, total,
  ROW_NUMBER() OVER w            AS rn,       -- 1,2,3,4
  RANK()       OVER w            AS rnk,      -- 1,2,2,4
  DENSE_RANK() OVER w            AS drnk,     -- 1,2,2,3
  LAG(total)   OVER w            AS prev_total,
  LEAD(total)  OVER w            AS next_total,
  SUM(total)   OVER w            AS running_total,
  AVG(total)   OVER (w ROWS BETWEEN 6 PRECEDING
                       AND CURRENT ROW)       AS avg_last_7,
  SUM(total)   OVER (PARTITION BY customer_id) AS customer_total
FROM orders
WINDOW w AS (PARTITION BY customer_id ORDER BY created_at);
'''), "dev", "wide", "over (partition … order …)"),
        box("Top-N per group", code('''
SELECT * FROM (
  SELECT o.*, ROW_NUMBER() OVER (
           PARTITION BY customer_id
           ORDER BY total DESC) AS rn
  FROM orders o
) t
WHERE rn <= 3;  -- top 3 per customer
''') + '<p class="fine">Windows run after WHERE, so filter them in an outer query. Postgres shortcut for top-1: <code>DISTINCT ON (customer_id)</code>.</p>', "feat"),
        box("Upsert", code('''
-- Postgres / SQLite
INSERT INTO stock (sku, qty) VALUES ('A1', 5)
ON CONFLICT (sku) DO UPDATE SET qty = stock.qty + EXCLUDED.qty;

-- MySQL
INSERT INTO stock (sku, qty) VALUES ('A1', 5)
ON DUPLICATE KEY UPDATE qty = qty + VALUES(qty);

-- SQL Server / standard (Postgres 15+ too)
MERGE INTO stock s USING (VALUES ('A1', 5)) v(sku, qty) ON s.sku = v.sku
WHEN MATCHED THEN UPDATE SET qty = s.qty + v.qty
WHEN NOT MATCHED THEN INSERT (sku, qty) VALUES (v.sku, v.qty);
'''), "main", "wide", "insert or update"),
        box("Delete duplicates", code('''
DELETE FROM users u
USING (
  SELECT id, ROW_NUMBER() OVER (
    PARTITION BY lower(email)
    ORDER BY created_at) AS rn
  FROM users
) d
WHERE u.id = d.id AND d.rn > 1;
''') + '<p class="fine">Keeps the oldest per email. Run it as a SELECT first, then add a unique index so it can\'t happen again.</p>', "hot"),
        box("Paging: OFFSET vs keyset", code('''
-- OFFSET: page 500 still reads 10,000 rows
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 10000;

-- keyset: fast at any depth; pass the last id seen
SELECT * FROM orders WHERE id > :last_id
ORDER BY id LIMIT 20;
''') + '<p class="fine">Keyset needs a unique, indexed sort key; for (date, id) compare tuples: <code>WHERE (created_at, id) &gt; (:d, :id)</code>.</p>', "rel", "wide"),
        box("Recursive CTE", code('''
WITH RECURSIVE tree AS (
  SELECT id, name, parent_id, 1 AS depth
  FROM categories WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, c.parent_id, t.depth + 1
  FROM categories c JOIN tree t ON c.parent_id = t.id
)
SELECT * FROM tree ORDER BY depth;
''') + '<p class="fine">SQL Server: drop the word <code>RECURSIVE</code>.</p>', "bug"),
    ],
)

# ---------------------------------------------------------------- page 4 · performance & safety
def index():
    d = Diagram("A composite index on orders (customer_id, status, created_at) helps queries that filter on a leftmost "
                "prefix of its columns; it does not help a filter on status or created_at alone, or a function on a column.",
                880, 286)
    d.node("ix", 14, 110, 230, 66, "INDEX (customer_id,", "status, created_at)", "dev")
    qs = [
        ("✓ WHERE customer_id = 7", "feat"),
        ("✓ WHERE customer_id = 7 AND status = 'paid'", "feat"),
        ("✓ … AND status = 'paid' AND created_at > '2026-01-01'", "feat"),
        ("✓ WHERE customer_id = 7 ORDER BY status  (no sort step)", "feat"),
        ("~ WHERE customer_id = 7 AND created_at > …  (1st column only)", "warn"),
        ("✗ WHERE status = 'paid'  (skips the first column)", "main"),
        ("✗ WHERE created_at > '2026-01-01'", "main"),
        ("✗ WHERE date(created_at) = '2026-01-01'  (function on column)", "main"),
    ]
    for i, (q, tone) in enumerate(qs):
        d.node(f"q{i}", 300, 10 + i * 34, 566, 27, q, None, tone, "soft chip")
        d.arrow("ix", f"q{i}", None, tone=tone)
    return d.svg()


PAGE_PERF = dict(
    title="Indexes, EXPLAIN &amp; transactions",
    kicker="fast queries, safe changes",
    figure=index(),
    boxes=[
        box("Index rules", '''
<ol class="rules">
<li><b>Leftmost prefix:</b> <code>(a, b, c)</code> serves <code>a</code>, <code>a,b</code>, <code>a,b,c</code>, not <code>b</code> alone.</li>
<li><b>Equality first,</b> range column last: <code>(customer_id, created_at)</code>.</li>
<li><b>Keep columns bare:</b> <code>created_at &gt;= '2026-01-01'</code>, not <code>date(created_at) = …</code>; or index the expression.</li>
<li><code>LIKE 'abc%'</code> can use an index; <code>'%abc'</code> can't (use trigram / full-text).</li>
<li>Index <b>foreign keys</b> you join on.</li>
<li><b>Covering:</b> <code>INCLUDE (total)</code> lets the index answer alone.</li>
<li>Every index slows writes and costs disk: drop unused ones.</li>
</ol>''', "dev"),
        box("Read EXPLAIN", code('''
EXPLAIN (ANALYZE, BUFFERS) SELECT …;  -- Postgres: runs it!
EXPLAIN ANALYZE SELECT …;  -- MySQL 8
''') + '''
<dl class="kv">
<dt>Seq Scan</dt><dd>reads the whole table: fine if small, else index?</dd>
<dt>Index Scan</dt><dd>index, then table rows</dd>
<dt>Index Only</dt><dd>answered from the index alone</dd>
<dt>Bitmap</dt><dd>many matches gathered, then fetched</dd>
<dt>Nested Loop</dt><dd>good for few rows with an index</dd>
<dt>Hash Join</dt><dd>big unsorted sets, needs memory</dd>
<dt>Merge Join</dt><dd>both sides already sorted</dd>
</dl>
<p class="fine"><b>Look for:</b> estimated vs actual rows far apart (run <code>ANALYZE</code>), sorts spilling to disk, the slowest node.</p>''', "rel"),
        box("Isolation levels", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th></th><th>dirty</th><th>non-rep.</th><th>phantom</th></tr></thead>
<tbody>
<tr><th>Read uncommitted</th><td>yes</td><td>yes</td><td>yes</td></tr>
<tr><th>Read committed</th><td>—</td><td>yes</td><td>yes</td></tr>
<tr><th>Repeatable read</th><td>—</td><td>—</td><td>yes*</td></tr>
<tr><th>Serializable</th><td>—</td><td>—</td><td>—</td></tr>
</tbody></table></div>
<p class="fine"><b>yes</b> = can happen. Defaults: Postgres, SQL Server = read committed; MySQL InnoDB = repeatable read. *Postgres and InnoDB prevent most phantoms here too. Serializable can fail with retry errors: retry the transaction.</p>''', "hot"),
        box("Change data safely", code('''
BEGIN;
UPDATE orders SET status = 'cancelled' WHERE id = 42;
-- check the count: "UPDATE 1", not "UPDATE 40000"
SELECT status FROM orders WHERE id = 42;
COMMIT;  -- or ROLLBACK;

SELECT * FROM jobs WHERE id = 7 FOR UPDATE;  -- lock the row
SELECT * FROM jobs WHERE state = 'new'
LIMIT 10 FOR UPDATE SKIP LOCKED;  -- work queue
''') + '<p class="fine">Write the <code>WHERE</code> first. Run it as a <code>SELECT</code> before the <code>UPDATE</code> / <code>DELETE</code>. Keep transactions short; lock rows in the same order to avoid deadlocks.</p>', "main", "wide"),
        box("Schema changes in production", '''
<ul class="checks">
<li>Add columns <b>nullable</b> (or with a constant default)</li>
<li><code>CREATE INDEX CONCURRENTLY</code> (Postgres) · <code>ALGORITHM=INPLACE</code> (MySQL)</li>
<li>Rename = add new, copy, switch reads, drop old later</li>
<li>Backfill big tables in batches</li>
<li>Set a <code>lock_timeout</code> on migrations</li>
<li>Migrations in git, reviewed, reversible</li>
<li>Backup tested <b>by restoring it</b></li>
</ul>''', "warn"),
    ],
)

PAGES = [PAGE_QUERY, PAGE_JOIN, PAGE_WIN, PAGE_PERF]
