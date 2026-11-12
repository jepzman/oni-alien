# Vol. 3 · Reading fast: Indexing, Batch Loading (N+1), Keyset Pagination, Materialized Views.

# ------------------------------------------------------------------ 05 Indexing
ix_problem = Doodle(760, 250, "Doodle of a query looking for the orders of customer 42 in a table of ten million rows. Without an index the database reads every row from top to bottom, a sequential scan, and the request takes four seconds.",
                    "No index: to find 12 rows, the database reads all 10,000,000.")
ix_problem.table(20, 20, "orders · 10M rows", ["#1 · cust 913", "#2 · cust 7", "#3 · cust 42", "#4 · cust 518", "…9,999,996 more…"], w=230, hl=(2,), soft=(4,))
ix_problem.arrow(280, 30, 280, 180, color="red", label="read every row", lx=296, ly=110, anchor="start")
ix_problem.note(560, 60, "WHERE customer_id = 42", "pen")
ix_problem.icon("clock", 520, 90, 1.1, color="red")
ix_problem.note(600, 130, "4.1 s", "red", anchor="start")
ix_problem.note(560, 200, "Seq Scan · rows read: 10,000,000", "red")

ix_analogy = Doodle(760, 250, "Doodle of a thick textbook. To find every page about photosynthesis you don't read the whole book: you open the index at the back, find the word in alphabetical order, and jump straight to pages 14, 88 and 203.",
                    "The index at the back of the book: sorted words, each with page numbers.")
ix_analogy.icon("book", 40, 50, 2.4, fill="y")
ix_analogy.note(110, 230, "600 pages")
ix_analogy.box(260, 30, 230, 160, None, "paper", rx=3)
for i, t in enumerate(["osmosis … 51", "photosynthesis … 14, 88, 203", "pigment … 90", "pollen … 112"]):
    ix_analogy.text(272, 64 + i * 34, t, "t", anchor="start", size=16)
ix_analogy.raw('<rect class="f-hl" x="266" y="80" width="220" height="26" style="stroke:none"/>')
ix_analogy.note(375, 220, "sorted, so you jump in", "pen")
ix_analogy.arrow(500, 92, 620, 92, label="jump to p. 14", lx=560, ly=78)
ix_analogy.icon("frame", 630, 60, 1.2)

ix_how = Doodle(760, 300, "B-tree index on customer_id. A root node splits key ranges, branch nodes narrow them, and the leaf for 42 holds pointers to the three matching rows in the table. The lookup touches four pages instead of millions, and finishes in under a millisecond.",
                "A B-tree index: a few hops down sorted pages, then straight to the matching rows.")
ix_how.box(300, 10, 160, 50, "root: 1 … 1M", "y", size=16)
ix_how.arrow(330, 64, 180, 100)
ix_how.arrow(430, 64, 580, 100)
ix_how.box(90, 104, 180, 50, "1 … 500", "y", size=16)
ix_how.box(500, 104, 180, 50, "500 … 1M", "paper", size=16)
ix_how.arrow(180, 158, 180, 188)
ix_how.box(70, 192, 220, 50, "leaf: 42 → rows", "green", size=16)
ix_how.arrow(296, 216, 440, 230, color="green")
ix_how.table(446, 186, "orders", ["#3 · cust 42", "#81k · cust 42"], w=200, hl=(0, 1))
ix_how.note(700, 30, "Index Scan", "green")
ix_how.note(700, 56, "0.4 ms", "green")

INDEXING = dict(
    slug="indexing",
    kicker="a.k.a. “the index at the back of the book”",
    tldr="An index is a <b>sorted copy of one or more columns</b> with pointers back to the rows, usually a <b>B-tree</b>. Queries that filter, join or sort on those columns <b>jump straight to the rows</b> instead of scanning the whole table. Every index makes <b>writes a little slower</b> and takes space, so index the queries you actually run, and check with <code>EXPLAIN</code>.",
    chips=[("Family", "query performance"), ("Default type", "B-tree"), ("Others", "hash, GIN, GiST, BRIN, partial, covering"), ("Check with", "EXPLAIN ANALYZE")],
    problem="""  <p class="lead">A table without the right index is a book without an index: to answer “which orders belong to customer 42?”, the database must <span class="hl-pink">read every row</span>. Fine at 1,000 rows. A disaster at 10 million.</p>
  <ul>
    <li>Pages get slower every month as data grows, with no code change.</li>
    <li>One slow query holds locks and connections, so everything else queues up.</li>
    <li>Throwing a bigger server at it buys weeks, not years.</li>
  </ul>""",
    problem_figs=[ix_problem],
    analogy_side="the index at the back of the book",
    analogy="""  <p>To find every page about photosynthesis you don't read the whole textbook. You flip to the <b>index</b>: words in <b>alphabetical order</b>, each with page numbers. Because it's sorted, you find the word in seconds and jump to the pages.</p>
  <ul>
    <li>Every new edition must update the index too: <b>indexes slow down writes</b>.</li>
    <li>An index of every word would be as big as the book: <b>don't index everything</b>.</li>
    <li>“Words starting with ph” is easy; “words ending in -sis” isn't: <b>column order and leading wildcards matter</b>.</li>
  </ul>""",
    analogy_figs=[ix_analogy],
    map=[("The index pages at the back", "A B-tree index on <code>customer_id</code>"),
         ("Alphabetical order", "Sorted keys, so lookups take a few hops"),
         ("Page numbers next to each word", "Row pointers (or the row itself, if covering)"),
         ("Updating the index for a new edition", "Extra work on every INSERT / UPDATE"),
         ("Reading the whole book", "A sequential scan")],
    how_side="sorted keys, a few hops down a tree",
    how="""  <p>A B-tree keeps keys <b>sorted in pages</b>. Finding one key among millions takes only 3–4 page reads, and once you're there, ranges and ORDER BY come for free.</p>""",
    how_figs=[ix_how],
    steps=[("Find the slow queries", "Use <code>pg_stat_statements</code> or your APM; sort by total time, not just the slowest single call."),
           ("Read the plan", "<code>EXPLAIN (ANALYZE, BUFFERS)</code>: a Seq Scan reading millions of rows for a few results is the signal."),
           ("Index what you filter, join and sort on", "Equality columns first, then range or sort columns: <code>(customer_id, placed_at)</code>."),
           ("Use special shapes when they fit", "Partial (<code>WHERE status = 'open'</code>), covering (<code>INCLUDE (total)</code>), expression (<code>lower(email)</code>), GIN for JSON and full text."),
           ("Build it without blocking", "<code>CREATE INDEX CONCURRENTLY</code> on busy tables."),
           ("Prune", "Drop indexes nobody uses (<code>pg_stat_user_indexes.idx_scan = 0</code>); they only slow writes.")],
    vocab=[("B-tree", "Balanced sorted tree; the default index type."),
           ("Sequential scan", "Reading the whole table, row by row."),
           ("Selectivity", "How few rows a condition matches; high = good for an index."),
           ("Composite index", "An index on several columns, in a set order."),
           ("Covering index", "Holds every column the query needs: no table visit."),
           ("Query plan", "The database's step-by-step recipe; see it with EXPLAIN.")],
    code=dict(file="indexes.sql", note="PostgreSQL", src="""
-- the query we run all day
SELECT id, total FROM orders
WHERE customer_id = 42 ORDER BY placed_at DESC LIMIT 20;

-- equality first, then the sort column; INCLUDE makes it covering
CREATE INDEX CONCURRENTLY orders_customer_recent
  ON orders (customer_id, placed_at DESC) INCLUDE (total);

-- only open tickets are ever searched: index just those
CREATE INDEX tickets_open ON tickets (assignee_id) WHERE status = 'open';

-- case-insensitive email lookups need an expression index
CREATE UNIQUE INDEX users_email_ci ON users (lower(email));

EXPLAIN (ANALYZE, BUFFERS) SELECT …;   -- Seq Scan → Index Only Scan
"""),
    tools="tools: <code>EXPLAIN ANALYZE</code>, pg_stat_statements, explain.depesz.com, pgMustard, MySQL <code>EXPLAIN FORMAT=TREE</code>, SQL Server execution plans, the “use-the-index-luke.com” guide.",
    gains=["<b>Huge read speedups</b>: seconds to milliseconds.",
           "<b>Cheap ORDER BY and ranges</b> on indexed columns.",
           "<b>Uniqueness enforced</b> by unique indexes.",
           "<b>Less load</b>: fewer pages read, fewer locks held."],
    losses=["<b>Slower writes</b>: every index is updated on insert/update.",
            "<b>Disk and memory</b> for each index.",
            "<b>Easy to get wrong</b>: wrong column order, unused indexes.",
            "<b>Bloat</b> on heavily updated tables needs maintenance."],
    baseline="Each line compares a table with <b>only a primary key</b> to the same table with <b>a few indexes chosen from real slow queries</b>.",
    ratings=[(4, 3, "Plans and column order take some learning."),
             (1, 5, "From full scans to a few page reads."),
             (5, 4, "Each index adds work to every write."),
             (3, 4, "Unique indexes enforce rules the app might miss."),
             (2, 4, "Lookups stay fast as tables grow."),
             (5, 3, "Indexes can rival the table in size."),
             (3, 3, "Fast for indexed questions, not for any question."),
             (2, 4, "Fewer slow-query fires and lock pile-ups."),
             (3, 3, "New queries may need new indexes.")],
    pitfalls=[("Indexing every column", "Twelve single-column indexes, and writes crawl.", "index real queries; prefer one good composite."),
              ("Wrong column order", "An index on (placed_at, customer_id) for <code>WHERE customer_id = ?</code>.", "equality columns first, then range/sort."),
              ("Functions on the column", "<code>WHERE lower(email) = ?</code> ignores an index on email.", "use an expression index or store it normalized."),
              ("Guessing instead of measuring", "An index is added and the plan doesn't use it.", "always confirm with EXPLAIN ANALYZE on real data.")],
    use=["Columns in frequent WHERE, JOIN and ORDER BY clauses.",
         "Foreign key columns (joins and cascading deletes).",
         "Uniqueness rules (unique indexes).",
         "Large tables where a query returns a small share of rows."],
    skip=["Tiny tables, where a scan is already instant.",
          "Columns with few distinct values (a boolean), unless partial.",
          "Write-heavy tables where the query is rare (log tables)."],
    related=["<b>Keyset pagination</b>", "<b>Materialized views</b>", "<b>Table partitioning</b>", "<b>Cache-aside</b> (Vol. 1)"],
    quiz=[("Why does column order matter in a composite index?", "The index is sorted by the first column, then the second; it helps queries that filter on a leading prefix of the columns."),
          ("What's a covering index?", "One that contains every column the query needs, so the database never has to visit the table (an index-only scan)."),
          ("Why can too many indexes hurt?", "Each one must be updated on every write and takes disk and memory."),
          ("How do you know an index is used?", "EXPLAIN ANALYZE shows an Index Scan or Index Only Scan, and index usage stats show scans over time.")],
    remember="Don't read the <span class=\"hl\">whole book</span>. Check the <span class=\"hl\">index</span>, but don't index every word.",
    sources=["Markus Winand, <i>SQL Performance Explained</i> and use-the-index-luke.com.",
             "PostgreSQL docs, “Indexes” and “Using EXPLAIN”.",
             "Bayer &amp; McCreight, “Organization and Maintenance of Large Ordered Indexes” (1972).",
             "Haki Benita, “Things I Wish I Knew About PostgreSQL Indexes”."],
)

# ------------------------------------------------------------------ 06 Batch Loading (N+1)
np_problem = Doodle(760, 260, "Doodle of a blog page listing 50 posts. The code loads the posts with one query, then inside a loop loads each post's author with another query, so 51 queries go to the database. Each is fast, but together they take 400 milliseconds.",
                    "1 query for the list + 1 per row = N+1 round trips.")
np_problem.box(20, 30, 160, 60, "app loop", "blue", sub="for post in posts")
np_problem.box(560, 70, 170, 110, "database", "y")
np_problem.arrow(186, 50, 554, 90, label="1 · SELECT posts", lx=370, ly=56)
for i in range(5):
    np_problem.arrow(186, 100 + i * 22, 554, 124 + i * 10, color="red")
np_problem.note(370, 210, "+ 50 × SELECT author WHERE id = ?", "red")
np_problem.note(370, 240, "51 round trips · 400 ms", "red")

np_analogy = Doodle(760, 250, "Doodle of a shopper with a list of 20 items who drives to the shop, buys one item, drives home, and repeats twenty times. The smart shopper takes the whole list in one trip.",
                    "Twenty trips for twenty items, or one trip with the list.")
np_analogy.icon("store", 320, 30, 1.6)
np_analogy.icon("door", 20, 40, 1.4)
np_analogy.note(55, 150, "home", "pen")
for i in range(4):
    np_analogy.arrow(100, 50 + i * 26, 310, 60 + i * 10, color="red")
np_analogy.note(160, 190, "20 trips, 1 item each", "red")
np_analogy.icon("menu", 560, 60, 1.2, fill="y")
np_analogy.arrow(550, 100, 436, 80, color="green")
np_analogy.note(600, 190, "1 trip, whole list", "green")

np_how = Doodle(760, 260, "Batch loading. Query one loads 50 posts. The app collects the 50 author ids and sends a second query with WHERE id = ANY of the list. The authors are matched to posts in memory. Two round trips instead of fifty-one.",
                "Collect the ids, fetch them all at once, match in memory: 2 queries, whatever N is.")
np_how.box(20, 40, 160, 60, "app", "blue")
np_how.box(560, 60, 170, 110, "database", "y")
np_how.arrow(186, 60, 554, 80, color="green", label="1 · SELECT posts LIMIT 50", lx=370, ly=52)
np_how.arrow(186, 90, 554, 140, color="green", label="2 · authors WHERE id = ANY(…)", lx=370, ly=150)
np_how.box(20, 170, 300, 60, "match author_id → author", "green", size=17)
np_how.note(560, 230, "2 round trips · 9 ms", "green")

N1 = dict(
    slug="n-plus-one",
    kicker="a.k.a. “take the shopping list”",
    tldr="The <b>N+1 problem</b>: load a list with one query, then run <b>one more query per row</b> to load something related. Fix it by <b>batch loading</b>: collect the ids and fetch the related rows in <b>one query</b> (a JOIN, <code>WHERE id = ANY(…)</code>, an ORM's eager loading, or a DataLoader). The number of queries stays <b>constant</b> however long the list gets.",
    chips=[("Family", "query performance"), ("Usual cause", "ORM lazy loading in a loop"), ("Fixes", "JOIN, eager loading, IN / ANY, DataLoader"), ("Pairs with", "indexing, keyset pagination")],
    problem="""  <p class="lead">Each query is fast, so nobody notices. But a page that loads 50 posts and then each post's author makes <span class="hl-pink">51 round trips</span>. With comments and likes it's 151. Latency adds up, and the database drowns in tiny queries.</p>
  <ul>
    <li>ORMs make it invisible: <code>post.author.name</code> looks like a field, but it's a query.</li>
    <li>Fine in development with 5 rows; slow in production with 500.</li>
    <li>GraphQL resolvers make it worse: every field can trigger its own query.</li>
  </ul>""",
    problem_figs=[np_problem],
    analogy_side="the shopping list",
    analogy="""  <p>You need 20 things from the shop. You could drive there, buy one, drive home, and repeat twenty times. Or you could take the <b>whole list</b> in one trip. The driving, not the shopping, is what takes time.</p>
  <ul>
    <li>Each drive is a <b>round trip</b> to the database.</li>
    <li>Writing the list first is <b>collecting the ids</b>.</li>
    <li>Fetching everything at once is <b>batch loading</b>.</li>
  </ul>""",
    analogy_figs=[np_analogy],
    map=[("One item per trip", "One query per row in a loop"),
         ("The drive", "Network round trip + query overhead"),
         ("Writing the shopping list", "Collecting <code>author_id</code>s from the posts"),
         ("One trip with the list", "<code>WHERE id = ANY($1)</code> or a JOIN"),
         ("Unpacking at home", "Matching authors to posts in memory")],
    how_side="collect, fetch once, match",
    how="""  <p>The fix is always the same shape: <b>don't query inside a loop</b>. Either join in SQL, or gather the keys and make one batched query per relationship.</p>""",
    how_figs=[np_how],
    steps=[("Spot it", "Count queries per request (ORM logs, APM traces). A count that grows with the list size is the tell."),
           ("Join when it's one-to-one", "<code>JOIN authors</code> brings the author along on each post row."),
           ("Batch when it's one-to-many", "Comments per post: a second query with <code>WHERE post_id = ANY(…)</code>, avoiding a giant row-multiplying join."),
           ("Use the ORM's eager loading", "<code>includes</code> (Rails), <code>select_related</code> / <code>prefetch_related</code> (Django), <code>include</code> (Prisma), <code>JOIN FETCH</code> (JPA)."),
           ("In GraphQL, use DataLoader", "It collects every key requested in one tick and makes one batched call."),
           ("Guard it in tests", "Assert the query count for key pages so a regression fails CI.")],
    vocab=[("N+1 query", "1 query for a list + 1 per item."),
           ("Lazy loading", "Related data is fetched when first accessed."),
           ("Eager loading", "Related data is fetched up front, in batches."),
           ("Round trip", "Send a query, wait for the answer."),
           ("DataLoader", "A helper that batches and caches lookups per request."),
           ("Row explosion", "A join that multiplies rows (posts × comments).")],
    code=dict(file="posts.ts", note="node-postgres", src="""
// ✗ N+1: one query per post
for (const p of posts) {
  p.author = (await db.query("SELECT * FROM authors WHERE id = $1", [p.author_id])).rows[0];
}

// ✓ batch: two queries, however many posts
const posts = (await db.query("SELECT * FROM posts ORDER BY id DESC LIMIT 50")).rows;
const ids = [...new Set(posts.map((p) => p.author_id))];
const authors = (await db.query("SELECT * FROM authors WHERE id = ANY($1)", [ids])).rows;
const byId = new Map(authors.map((a) => [a.id, a]));
for (const p of posts) p.author = byId.get(p.author_id);

// the same with an ORM (Prisma): include = eager loading
await prisma.post.findMany({ take: 50, include: { author: true } });
"""),
    tools="tools: ORM eager loading, GraphQL DataLoader, Bullet (Rails) and nplusone (Django) detectors, Sentry/Datadog “N+1 query” detection, query-count assertions in tests.",
    gains=["<b>Constant query count</b>: 2 queries for 10 or 10,000 rows.",
           "<b>Much lower latency</b>: round trips dominate small queries.",
           "<b>Less database load</b>: fewer parses, fewer connections held.",
           "<b>Predictable pages</b> as data grows."],
    losses=["<b>A little more code</b> (or ORM hints) per relationship.",
            "<b>Over-fetching</b> if you eager-load things you don't show.",
            "<b>Big joins can multiply rows</b> if used for one-to-many.",
            "<b>Huge id lists</b> need chunking."],
    baseline="Each line compares <b>lazy loading in a loop</b> to the same page with <b>batched / eager loading</b>.",
    ratings=[(4, 4, "One more line of ORM hints; same idea everywhere."),
             (1, 5, "Dozens of round trips become two."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 5, "Query count no longer grows with the page size."),
             (3, 3, "Neutral."),
             (3, 4, "Batched loaders compose for nested data."),
             (2, 4, "Far fewer tiny queries flooding the database."),
             (3, 3, "New relations need their own batch rule.")],
    pitfalls=[("Eager-loading everything", "Every request loads comments, likes and tags it never shows.", "load only what the view renders."),
              ("A JOIN for one-to-many", "Posts × comments returns 50,000 rows for 50 posts.", "use a second batched query for collections."),
              ("Batching without an index", "<code>WHERE post_id = ANY(…)</code> still scans the table.", "index the foreign key column."),
              ("Fixing it once", "A new field in a template brings the N+1 back.", "assert query counts in tests or use a detector.")],
    use=["Any list page that shows related data.",
         "GraphQL APIs (use DataLoader by default).",
         "Background jobs that loop over many rows."],
    skip=["Detail pages that load a single row and its relations.",
          "Relations that are rarely accessed and expensive to load.",
          "When a denormalized read model already holds what you need."],
    related=["<b>Indexing</b>", "<b>Keyset pagination</b>", "<b>Materialized views</b>", "<b>Server-state cache</b> (Vol. 2)"],
    quiz=[("How do you recognize an N+1 problem?", "The number of queries per request grows with the number of rows shown."),
          ("JOIN or second query for comments per post?", "A second batched query: a JOIN multiplies post rows by comment rows."),
          ("What does DataLoader do?", "Collects all the keys requested during one tick and loads them in one batched call, caching per request."),
          ("Why are 50 fast queries slower than 1 medium one?", "Each has a network round trip and per-query overhead; latency adds up even if each query is quick.")],
    remember="Never <span class=\"hl\">query in a loop</span>. Write the <span class=\"hl\">list</span>, make <span class=\"hl\">one trip</span>.",
    sources=["Rails Guides, “Active Record Query Interface: Eager Loading Associations”.",
             "Django docs, <code>select_related</code> and <code>prefetch_related</code>.",
             "GraphQL DataLoader README (github.com/graphql/dataloader).",
             "Sentry docs, “N+1 Queries” performance issue."],
)

# ------------------------------------------------------------------ 07 Keyset Pagination
kp_problem = Doodle(760, 250, "Doodle of OFFSET pagination. To show page 5,000 with 20 rows per page, the database reads and throws away 100,000 rows before returning 20. Meanwhile a new row was inserted, so one item appears on two pages.",
                    "OFFSET 100000: read 100,020 rows, keep 20, and new inserts shift every page.")
kp_problem.raw('<rect class="d d-thin f-pink" x="20" y="60" width="520" height="40" rx="3"/>')
kp_problem.raw('<rect class="d d-thin f-green" x="540" y="60" width="40" height="40" rx="3"/>')
kp_problem.note(280, 50, "skipped: 100,000 rows read and thrown away", "red")
kp_problem.note(600, 130, "20 kept", "green")
kp_problem.note(280, 150, "page 1 → 3 ms · page 5,000 → 900 ms", "red")
kp_problem.note(280, 190, "a new row arrives → items repeat or vanish", "red")
kp_problem.note(280, 230, "SELECT … ORDER BY id LIMIT 20 OFFSET 100000", "pen")

kp_analogy = Doodle(760, 250, "Doodle of reading a long novel with a bookmark. To continue tomorrow you open at the bookmark. You don't count 4,000 lines from the start. If the author adds a preface, your bookmark still points at the right place.",
                    "A bookmark: continue from where you stopped, without counting from the start.")
kp_analogy.icon("book", 60, 50, 2.4, fill="y")
kp_analogy.raw('<path class="d d-red f-pink" d="M140 30 v70 l8 -8 l8 8 v-70 z"/>')
kp_analogy.note(140, 230, "open at the bookmark", "green")
kp_analogy.note(480, 80, "✗ “start at line 1, count 4,000”", "red")
kp_analogy.note(480, 130, "✓ “continue after this line”", "green")
kp_analogy.note(480, 180, "new preface? bookmark still right", "pen")

kp_how = Doodle(760, 260, "Keyset pagination. Page one returns rows ordered by created_at and id and ends at the cursor 12 Nov, 9041. The next request asks for rows after that pair. The index on created_at and id jumps straight to the cursor, so every page costs the same.",
                "Remember the last row's sort key; ask for rows after it. The index jumps there directly.")
kp_how.table(20, 20, "page 1", ["12 Nov · 9044", "12 Nov · 9043", "12 Nov · 9041"], w=200, fill="green", hl=(2,))
kp_how.arrow(226, 112, 330, 112, label="cursor", lx=278, ly=98)
kp_how.box(336, 82, 260, 60, "next: after (12 Nov, 9041)", "y", size=16)
kp_how.arrow(466, 146, 466, 190, color="green")
kp_how.box(336, 194, 260, 50, "index jumps there", "green", size=17)
kp_how.note(680, 60, "page 1: 3 ms", "green")
kp_how.note(680, 90, "page 5,000: 3 ms", "green")

KEYSET = dict(
    slug="keyset-pagination",
    kicker="a.k.a. “the bookmark”",
    tldr="Instead of <code>LIMIT 20 OFFSET 100000</code>, remember the <b>sort key of the last row</b> you showed and ask for <b>rows after it</b>: <code>WHERE (created_at, id) &lt; (:last_at, :last_id)</code>. With an index on those columns, <b>every page is as fast as page 1</b>, and new inserts don't make items repeat or vanish.",
    chips=[("Family", "query performance"), ("a.k.a.", "seek method, cursor pagination"), ("Needs", "a unique, indexed sort order"), ("Pairs with", "indexing, infinite scroll")],
    problem="""  <p class="lead"><code>OFFSET</code> pagination is easy, but the database still has to <span class="hl-pink">read every skipped row</span>. Deep pages get slower and slower, and the results shift under your feet.</p>
  <ul>
    <li>Page 5,000 reads 100,020 rows to return 20.</li>
    <li>Someone inserts a row while you page, and an item appears twice.</li>
    <li>Crawlers and exports that walk every page hammer the database.</li>
  </ul>""",
    problem_figs=[kp_problem],
    analogy_side="the bookmark",
    analogy="""  <p>When you stop reading a novel you leave a <b>bookmark</b>. Tomorrow you open the book there. You don't count 4,000 lines from the first page. And if the publisher adds a preface, your bookmark is still in the right place.</p>
  <ul>
    <li>The bookmark is the <b>cursor</b>: the last row's sort key.</li>
    <li>Opening at it is an <b>index seek</b>.</li>
    <li>Counting lines from the start is <b>OFFSET</b>.</li>
  </ul>""",
    analogy_figs=[kp_analogy],
    map=[("The bookmark", "The cursor: <code>(created_at, id)</code> of the last row"),
         ("Open at the bookmark", "<code>WHERE (created_at, id) &lt; (…)</code> + index seek"),
         ("Counting lines from page 1", "<code>OFFSET n</code>"),
         ("A new preface", "Rows inserted while you page"),
         ("Ribbon instead of page number", "An opaque cursor token in the API")],
    how_side="seek, don't skip",
    how="""  <p>The trick is a <b>unique, stable sort order</b> (add the id as a tie-breaker) and an index that matches it. Then “rows after X” is a single index seek.</p>""",
    how_figs=[kp_how],
    steps=[("Pick a stable order", "Sort by something meaningful plus a unique tie-breaker: <code>ORDER BY created_at DESC, id DESC</code>."),
           ("Index it", "<code>CREATE INDEX ON posts (created_at DESC, id DESC)</code>."),
           ("Return a cursor", "Send the last row's <code>(created_at, id)</code>, encoded as an opaque token."),
           ("Seek on the next request", "Row-value comparison: <code>WHERE (created_at, id) &lt; ($1, $2)</code>."),
           ("Design the UI for it", "Next/previous and infinite scroll work well; “jump to page 731” doesn't.")],
    vocab=[("OFFSET pagination", "Skip n rows, then take a page."),
           ("Keyset / seek", "Continue after the last row's key."),
           ("Cursor", "Token holding the last row's sort key."),
           ("Tie-breaker", "A unique column that makes the order total."),
           ("Row-value comparison", "<code>(a, b) &lt; (x, y)</code> compares pairs in order."),
           ("Page drift", "Items repeating or vanishing as data changes.")],
    code=dict(file="feed.sql", note="PostgreSQL", src="""
CREATE INDEX posts_feed ON posts (created_at DESC, id DESC);

-- first page
SELECT id, title, created_at FROM posts
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- next page: continue after the last row we sent
SELECT id, title, created_at FROM posts
WHERE (created_at, id) < ($1, $2)     -- $1, $2 = last row's values
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- API: { items: [...], next: base64('2026-11-12T09:41Z|9041') }
"""),
    tools="tools: most APIs with a <code>next_cursor</code> (Stripe, Slack, GitHub GraphQL) use it. GraphQL Relay connections, Django REST <code>CursorPagination</code>, Prisma <code>cursor</code>, jOOQ <code>seek()</code>.",
    gains=["<b>Constant speed</b>: page 5,000 = page 1.",
           "<b>No duplicates or gaps</b> when rows are inserted.",
           "<b>Cheap full walks</b> for exports and syncs.",
           "<b>Natural fit</b> for infinite scroll and APIs."],
    losses=["<b>No “jump to page 731”</b>.",
            "<b>Total counts are separate</b> (and still expensive).",
            "<b>Needs a matching index</b> and unique order.",
            "<b>Cursor logic</b> is fiddlier with many sort options."],
    baseline="Each line compares <b>LIMIT/OFFSET pages</b> to <b>keyset pagination</b> with a matching index.",
    ratings=[(5, 4, "A cursor and row comparison instead of a page number."),
             (2, 5, "Every page is a single index seek."),
             (3, 3, "Neutral."),
             (2, 4, "No repeated or skipped items while data changes."),
             (1, 5, "Cost doesn't grow with page depth."),
             (3, 3, "One index you likely needed anyway."),
             (4, 3, "Random page jumps and odd sort orders are harder."),
             (3, 4, "Crawlers and exports stop hammering the database."),
             (3, 3, "Each new sort order needs its own index and cursor.")],
    pitfalls=[("A non-unique sort", "Ordering by <code>created_at</code> alone skips rows with the same timestamp.", "always add a unique tie-breaker (id)."),
              ("Index doesn't match the order", "The seek turns into a scan plus sort.", "index the exact columns and directions."),
              ("Exposing raw values", "Clients build their own cursors and break when you change the sort.", "encode the cursor as an opaque token."),
              ("COUNT(*) on every page", "The pagination is fast, the total count isn't.", "show “more” instead, or cache an estimate.")],
    use=["Feeds, timelines, infinite scroll and activity logs.",
         "Public APIs that return lists.",
         "Exports, syncs and batch jobs that walk a whole table."],
    skip=["Small result sets where OFFSET is instant.",
          "UIs that really need numbered pages you can jump between.",
          "Ad-hoc admin screens with many sortable columns."],
    related=["<b>Indexing</b>", "<b>Batch loading</b>", "<b>Table partitioning</b>", "<b>List virtualization</b> (Vol. 2)"],
    quiz=[("Why does OFFSET get slower on deep pages?", "The database still reads every skipped row before discarding it."),
          ("Why add the id to the sort?", "To make the order unique, so rows sharing the same timestamp aren't skipped or repeated."),
          ("What index supports ORDER BY created_at DESC, id DESC?", "A composite index on (created_at DESC, id DESC)."),
          ("What can't keyset pagination do easily?", "Jump straight to an arbitrary page number.")],
    remember="Use a <span class=\"hl\">bookmark</span>, not a <span class=\"hl\">line count</span>.",
    sources=["Markus Winand, “We need tool support for keyset pagination” and use-the-index-luke.com/no-offset.",
             "PostgreSQL docs, “Row Constructor Comparison”.",
             "Slack engineering, “Evolving API Pagination at Slack”.",
             "Relay docs, “GraphQL Cursor Connections Specification”."],
)

# ------------------------------------------------------------------ 08 Materialized Views
mv_problem = Doodle(760, 250, "Doodle of a sales dashboard. Every time anyone opens it, the database joins orders, items and products across fifty million rows and groups by day and region. The query takes twelve seconds, and twenty people open it every morning.",
                    "The same expensive question, recomputed from scratch for every viewer.")
for i, t in enumerate(["orders · 50M", "items · 180M", "products"]):
    mv_problem.db(70 + i * 140, 40, t, w=90)
mv_problem.arrow(420, 70, 540, 70, color="red", label="JOIN + GROUP BY", lx=480, ly=56)
mv_problem.icon("screen", 560, 40, 1.4)
mv_problem.note(605, 140, "12 s per view", "red")
mv_problem.note(380, 200, "20 people × every morning = 20 × the same work", "red")

mv_analogy = Doodle(760, 250, "Doodle of a train station departure board. Nobody phones every train driver to ask when they'll leave. The station computes the board and refreshes it every minute; travellers just read it.",
                    "The departure board: computed once, refreshed every minute, read by everyone.")
mv_analogy.icon("board", 300, 30, 2.0, fill="y")
mv_analogy.note(370, 186, "refreshed every minute", "green")
for i in range(3):
    mv_analogy.arrow(140, 60 + i * 40, 290, 70 + i * 10, dash=True)
mv_analogy.icon("phone", 40, 40, 1.2, color="red")
mv_analogy.note(90, 170, "✗ call every driver", "red")
mv_analogy.note(620, 120, "everyone just reads", "pen")
mv_analogy.arrow(560, 100, 460, 80)

mv_how = Doodle(760, 280, "Materialized view flow. A materialized view called daily_sales stores the result of the heavy join and group by as real rows with an index. A scheduled job refreshes it concurrently every fifteen minutes. The dashboard reads the small precomputed table in five milliseconds.",
                "Store the answer as a table, index it, and refresh it on a schedule.")
for i, t in enumerate(["orders", "items", "products"]):
    mv_how.db(50, 20 + i * 80, None, w=70, h=30)
    mv_how.note(130, 44 + i * 80, t, anchor="start")
mv_how.arrow(220, 120, 320, 120, label="heavy query", lx=270, ly=106)
mv_how.table(326, 60, "daily_sales (stored)", ["day · region · total", "11 Nov · EU · €82k", "11 Nov · US · €91k"], w=250, fill="green")
mv_how.arrow(582, 120, 650, 120, color="green", label="5 ms", lx=616, ly=106)
mv_how.icon("screen", 656, 96, 1.0)
mv_how.box(326, 210, 250, 50, "REFRESH every 15 min", "y", size=17)
mv_how.arrow(450, 206, 450, 178, dash=True)

MATVIEW = dict(
    slug="materialized-views",
    kicker="a.k.a. “the departure board”",
    tldr="A materialized view <b>stores the result of an expensive query as real rows</b>, which you can index and read in milliseconds. You <b>refresh</b> it on a schedule or after changes, accepting that readers see data that's <b>a few minutes old</b>. Perfect for dashboards, leaderboards and reports that many people read and nobody needs to the second.",
    chips=[("Family", "read optimisation"), ("Built in", "PostgreSQL, Oracle, SQL Server (indexed views), Snowflake"), ("Trade", "freshness for speed"), ("Pairs with", "star schema, CQRS")],
    problem="""  <p class="lead">Some questions are expensive: sales per region per day across 50 million orders. A normal view just <span class="hl-pink">re-runs the query</span> every time, so every viewer pays the full cost.</p>
  <ul>
    <li>Dashboards take 12 seconds to load, every time.</li>
    <li>Twenty people opening it at 9 a.m. means twenty heavy queries at once.</li>
    <li>The reporting load slows down checkout on the same database.</li>
  </ul>""",
    problem_figs=[mv_problem],
    analogy_side="the departure board",
    analogy="""  <p>A station doesn't make every traveller phone the drivers. It computes a <b>departure board</b> and <b>refreshes it every minute</b>. Thousands of people read it instantly. It might be a minute out of date, and nobody minds.</p>
  <ul>
    <li>The board is the <b>materialized view</b>.</li>
    <li>“Updated every minute” is the <b>refresh schedule</b>.</li>
    <li>For the exact second a train leaves, you ask the platform staff: <b>query the source</b>.</li>
  </ul>""",
    analogy_figs=[mv_analogy],
    map=[("The departure board", "<code>CREATE MATERIALIZED VIEW daily_sales</code>"),
         ("Phoning every driver", "Re-running the heavy join for every request"),
         ("Board refreshed every minute", "<code>REFRESH MATERIALIZED VIEW</code> on a schedule"),
         ("“Last updated 09:41”", "A <code>refreshed_at</code> shown in the UI"),
         ("Asking the platform staff", "Querying the source tables for exact numbers")],
    how_side="compute once, read many times",
    how="""  <p>A materialized view is a <b>cache that lives in the database</b>. It's queried with plain SQL, can have indexes, and its freshness is set by how often you refresh it.</p>""",
    how_figs=[mv_how],
    steps=[("Find the heavy, popular query", "Read many times, changes slowly, and slightly stale is fine."),
           ("Create the view", "<code>CREATE MATERIALIZED VIEW daily_sales AS SELECT …</code>."),
           ("Index it", "A unique index is needed for concurrent refresh, plus indexes for the dashboard's filters."),
           ("Refresh without blocking", "<code>REFRESH MATERIALIZED VIEW CONCURRENTLY</code> keeps readers working during the refresh."),
           ("Schedule it", "pg_cron, a job runner, or after a batch load; show “last updated” to users."),
           ("Go incremental when it's too slow", "Summary tables updated by triggers or CDC, or a database with incremental views.")],
    vocab=[("View", "A saved query; re-runs every time."),
           ("Materialized view", "A saved query whose result is stored."),
           ("Refresh", "Recomputing the stored result."),
           ("Staleness", "How old the stored result can be."),
           ("Incremental maintenance", "Updating only what changed, not everything."),
           ("Summary table", "A hand-maintained table of precomputed totals.")],
    code=dict(file="daily_sales.sql", note="PostgreSQL + pg_cron", src="""
CREATE MATERIALIZED VIEW daily_sales AS
SELECT date_trunc('day', o.placed_at) AS day, o.region,
       sum(i.qty * i.price) AS total, count(DISTINCT o.id) AS orders
FROM orders o JOIN order_items i ON i.order_id = o.id
GROUP BY 1, 2;

CREATE UNIQUE INDEX ON daily_sales (day, region);  -- needed for CONCURRENTLY

-- every 15 minutes, without blocking readers
SELECT cron.schedule('*/15 * * * *',
  'REFRESH MATERIALIZED VIEW CONCURRENTLY daily_sales');

-- the dashboard: milliseconds
SELECT * FROM daily_sales WHERE day >= now() - interval '30 days';
"""),
    tools="tools: PostgreSQL materialized views + pg_cron, Oracle fast refresh, SQL Server indexed views, Snowflake/BigQuery materialized views, dbt incremental models, Materialize and RisingWave for always-fresh incremental views.",
    gains=["<b>Fast reads</b> for expensive questions.",
           "<b>Less load</b>: the heavy query runs once per refresh.",
           "<b>Plain SQL</b>: readers don't know it's precomputed.",
           "<b>Indexable</b>, unlike a normal view."],
    losses=["<b>Stale data</b> between refreshes.",
            "<b>Refresh cost</b>: full recompute by default.",
            "<b>Extra storage</b> for the stored result.",
            "<b>One more thing to schedule</b> and monitor."],
    baseline="Each line compares running the <b>heavy report query on every request</b> to reading a <b>materialized view refreshed every 15 minutes</b>.",
    ratings=[(4, 4, "It's just a table you query; refresh is one command."),
             (1, 5, "Seconds become milliseconds."),
             (3, 3, "Source writes are untouched; refreshes cost separately."),
             (5, 4, "Correct as of the last refresh; slightly stale."),
             (2, 4, "Read cost no longer grows with viewers."),
             (4, 3, "Stores a copy of the result."),
             (4, 3, "Fast for the questions it answers; new ones need new views."),
             (3, 3, "Refresh jobs need monitoring and alerting."),
             (3, 3, "Changing the query means recreating the view.")],
    pitfalls=[("Blocking refresh", "A plain REFRESH locks the view, so the dashboard hangs for a minute.", "use CONCURRENTLY with a unique index."),
              ("Refreshing too often", "A 3-minute refresh every minute: refreshes pile up.", "refresh no faster than it can finish; consider incremental tables."),
              ("Hidden staleness", "Users think the numbers are live and make decisions on old data.", "show “last updated” in the UI."),
              ("Using it for live data", "Stock levels from a 15-minute-old view.", "keep exact, fast-changing reads on the source tables.")],
    use=["Dashboards, leaderboards and reports read by many people.",
         "Heavy aggregations over data that changes slowly.",
         "Offloading reporting queries from transactional work."],
    skip=["Data that must be exact right now (balances, stock).",
          "Queries that are already fast with the right index.",
          "Source data that changes faster than you can refresh."],
    related=["<b>Star schema</b>", "<b>Normalization</b> (denormalizing on purpose)", "<b>CQRS</b> (Vol. 1)", "<b>Cache-aside</b> (Vol. 1)"],
    quiz=[("Difference between a view and a materialized view?", "A view re-runs its query every time; a materialized view stores the result and is refreshed explicitly."),
          ("What does REFRESH … CONCURRENTLY need, and why use it?", "A unique index on the view; it lets readers keep querying during the refresh."),
          ("What's the main trade-off?", "Freshness for speed: reads are fast but can be as old as the last refresh."),
          ("When would you use incremental maintenance instead?", "When full refreshes are too slow or you need near-real-time results.")],
    remember="Compute it <span class=\"hl\">once</span>, show it to <span class=\"hl\">everyone</span>, and print <span class=\"hl\">“last updated”</span>.",
    sources=["PostgreSQL docs, “Materialized Views” and “REFRESH MATERIALIZED VIEW”.",
             "Gupta &amp; Mumick, “Maintenance of Materialized Views: Problems, Techniques, and Applications” (1995).",
             "Microsoft docs, “Create Indexed Views”.",
             "Materialize docs, “Incremental view maintenance”."],
)

NOTES = [INDEXING, N1, KEYSET, MATVIEW]
