# Revisions to Vol. 3 (November 2026): one situational quiz question and a “try it” per note.
# The “going deeper” chapters for four key notes are in deeper.py. Merged by scripts/build_notes.py (load_content).

REVISION_NOTE = ("Nov 2026", "every note gains a “what would you do?” question and a try it; four notes go deeper; related notes are links now")

REVISIONS = {
    "normalization": dict(
        quiz_add=[("A customer changes their email address, and support still sees the old one on 40% of their orders. The orders table has a customer_email column. What happened, and what do you change?",
                   "The email was copied into each order, so an update anomaly left old copies behind. Keep the email only in customers and join through customer_id. If an order must show the email used at the time, keep it deliberately as a snapshot and name it that way (email_at_order).")],
        try_it="Take a spreadsheet you know (a sign-up list, an expense sheet) and split it into tables until each fact is stored once. Write the CREATE TABLE statements with foreign keys, then write the query that rebuilds the original sheet with joins.",
    ),
    "surrogate-keys": dict(
        quiz_add=[("Your products table uses the SKU as its primary key, and eight tables reference it. The supplier renames 2,000 SKUs. What does that cost, and what would have made it a one-table change?",
                   "Every referencing row in eight tables must change, ideally in one transaction with cascades and locks. With a surrogate id as the key and SKU as a UNIQUE column, the rename is a 2,000-row update in products only.")],
        try_it="Create two versions of a users and orders schema: one keyed by email, one by a generated id with email UNIQUE. Insert some orders, then change one user's email in each version and count the rows you had to touch.",
    ),
    "soft-delete": dict(
        quiz_add=[("A user deletes a project called “launch”, then tries to create a new one with the same name and gets a duplicate-name error. Soft delete is in place. What do you fix?",
                   "The unique constraint still sees the deleted row. Make it a partial unique index that only covers live rows (UNIQUE (owner_id, name) WHERE deleted_at IS NULL).")],
        try_it="Add deleted_at to a table, create a view that hides deleted rows, and point your reads at it. Delete and restore a row. Then add a unique column, delete a row and insert its twin, and fix the error with a partial unique index.",
    ),
    "history-tables": dict(
        quiz_add=[("A customer disputes a price: “it was €9 when I added it to the cart last Tuesday”. Your products table only holds the current €12. What would have let you answer, and what do you add now?",
                   "A history table (or system-versioned table) with valid_from and valid_to and who made each change. Add it now with a trigger, so the next dispute can be answered with a query “as of” that date.")],
        try_it="Add a history table and an update trigger to one table in a local Postgres. Change a row three times, then write the query that shows its value at a time between the second and third change.",
    ),
    "indexing": dict(
        quiz_add=[("A query filters orders by customer_id and sorts by created_at descending. There is an index on created_at only, and the query takes 2 seconds. Which index do you add, and how do you check it helped?",
                   "A composite index on (customer_id, created_at DESC): the equality column first, then the sort column. Run EXPLAIN ANALYZE before and after, and look for an index scan with no separate sort step.")],
        try_it="Fill a table with a million rows (generate_series), run a filtered and sorted query with EXPLAIN ANALYZE, then add a single-column index and a composite one in both column orders. Write down the plan and time for each.",
    ),
    "n-plus-one": dict(
        quiz_add=[("The blog's front page makes 101 queries: one for 50 posts and two for each post's author and comment count. The ORM hides it. How do you find it, and what does the fixed page do?",
                   "Turn on query logging (or an APM trace) and count queries per request. The fixed page runs three queries: the posts, the authors WHERE id = ANY(…), and the comment counts grouped by post_id, or uses the ORM's eager loading.")],
        try_it="Write a page that lists 50 posts with their authors using a loop of queries, and log the query count. Rewrite it with one batched query (or your ORM's include or preload option) and compare query count and time.",
    ),
    "keyset-pagination": dict(
        quiz_add=[("An admin list is fast on page 1 and takes 9 seconds on page 4,000. Users also complain that items appear twice when new rows arrive while they scroll. What do you change?",
                   "Replace OFFSET with keyset pagination on (created_at, id) with a matching index, and pass a cursor of the last row's values. Deep pages become as fast as the first, and new rows no longer shift the pages.")],
        try_it="With a million-row table, time LIMIT 20 OFFSET 0, 100,000 and 900,000. Then implement the same pages with WHERE (created_at, id) < (…) and an index on both columns, and time them again.",
    ),
    "materialized-views": dict(
        quiz_add=[("A sales dashboard runs a 40-second aggregate on every page view, and 30 people open it each morning. Numbers from five minutes ago are fine. What do you build?",
                   "A materialized view of the aggregate with a unique index, refreshed CONCURRENTLY every five minutes by a scheduled job. The dashboard reads it in milliseconds, and refreshes don't block readers.")],
        try_it="Create a materialized view over an expensive GROUP BY on a large table, time a read before and after, and refresh it while a loop reads from it, with and without CONCURRENTLY. Note which refresh blocked the readers.",
    ),
    "optimistic-locking": dict(
        quiz_add=[("Two support agents edit the same customer at the same time. The second save silently removes the phone number the first one added. What do you add, and what does the second agent see?",
                   "A version column checked in the UPDATE's WHERE clause. The second save matches 0 rows, so the API returns 409 Conflict, and the agent sees “this customer changed since you opened it” with the new values to merge.")],
        try_it="Open the same row in two terminals, update it from both with a plain UPDATE, and see the lost update. Add a version column and WHERE version = :v, repeat, and handle the 0-rows case with a clear error.",
    ),
    "expand-contract": dict(
        quiz_add=[("You need to split full_name into first_name and last_name on a 50-million-row table, with no downtime and three app instances deployed one by one. Outline the deploys.",
                   "1. Add the two nullable columns. 2. Deploy code that writes all three. 3. Backfill old rows in batches. 4. Switch reads to the new columns. 5. Stop writing full_name. 6. Drop it in a later release. Each step works with the code before and after it.")],
        try_it="Rename a column in a local app the expand-and-contract way, in five commits: add, dual-write, backfill, switch reads, drop. Run the old and new app versions against the database after each step to check they both still work.",
    ),
    "change-data-capture": dict(
        quiz_add=[("The search index is out of date for about 1 product in 500. The app writes to Postgres and then to Elasticsearch, and the second call sometimes times out. What do you change?",
                   "Stop writing to the index from the app. Let a CDC connector (such as Debezium) read Postgres's log and update the index from committed changes, with retries. Every committed change reaches the index, including changes made by scripts.")],
        try_it="Run Postgres with logical replication and Debezium (or a small wal2json client) with Docker Compose. Insert, update and delete rows, and watch the events. Roll back a transaction and confirm no event appears.",
    ),
    "partitioning": dict(
        quiz_add=[("An events table has 2 billion rows. The nightly “delete older than 90 days” job runs for 6 hours and slows everything down. What do you change?",
                   "Partition the table by day or month on created_at, and drop whole partitions that are older than 90 days instead of deleting rows. Dropping is almost instant, and queries for recent events only touch recent partitions.")],
        try_it="Create a table partitioned by month, insert a year of fake events, and run EXPLAIN on a query for one week to see partition pruning. Then remove the oldest month with DROP TABLE and compare with a DELETE on an unpartitioned copy.",
    ),
    "multitenancy": dict(
        quiz_add=[("In a shared-table SaaS app, a developer forgot WHERE tenant_id = … in one new report, and customer A saw customer B's invoices. How do you make the next forgotten filter harmless?",
                   "Turn on row-level security with a policy on tenant_id = current_setting('app.tenant_id'), set that value per transaction (SET LOCAL), and make sure the app's database role doesn't bypass RLS. A missing WHERE then returns only the tenant's own rows.")],
        try_it="Create an invoices table with tenant_id, enable row-level security with a policy, and query it as two tenants using SET LOCAL in a transaction. Then run a query with no WHERE clause and confirm it only returns the current tenant's rows.",
    ),
    "connection-pooling": dict(
        quiz_add=[("After you scale an API from 10 to 60 pods, the database starts refusing connections. Each pod has a pool of 20. What do you change?",
                   "60 × 20 = 1,200 connections is far beyond what Postgres handles well. Lower the pool per pod, and put a transaction-mode pooler (PgBouncer) in front of the database so many app connections share a few hundred real ones.")],
        try_it="Run a small load test against an endpoint that queries Postgres, first opening a new connection per request and then with a pool of 10. Compare latency and the number of server processes (pg_stat_activity). Then try a pool of 200 and see if it gets faster.",
    ),
    "star-schema": dict(
        quiz_add=[("Analysts write reports against the production order tables and join nine tables each time. Numbers differ between reports, and the database slows down at month end. What do you propose?",
                   "A star schema in a warehouse: a sales fact table at order-line grain with date, product, customer and store dimensions, loaded nightly or by CDC. Reports become simple GROUP BYs, everyone uses the same definitions, and production is left alone.")],
        try_it="Take a small sales data set and design one fact table and three dimensions. State the grain in one sentence. Load it into DuckDB or SQLite and answer “revenue by month and category” with one join per dimension.",
    ),
}

for _slug, _rev in REVISIONS.items():
    _deeper = _slug in ("indexing", "optimistic-locking", "change-data-capture", "multitenancy")
    _rev.setdefault("revised", ("Nov 2026", "a “what would you do?” question, a try it" + (" and a going-deeper chapter" if _deeper else "")))
