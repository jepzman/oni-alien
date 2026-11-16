# Revisions to Vol. 1 (November 2026): one situational quiz question and a “try it” per note.
# Merged into the notes by scripts/build_notes.py (load_content); the two hand-made notes get them injected.

REVISION_NOTE = ("Nov 2026", "every note gains a “what would you do?” question and a try it; related notes are links now")

REVISIONS = {
    "circuit-breaker": dict(
        quiz_add=[("Checkout calls Recommendations and Payments. Recommendations starts timing out after a deploy. Which one gets a breaker with a fallback, and what is the fallback?",
                   "Both calls get a breaker, but only Recommendations gets a quiet fallback: an empty list or yesterday's bestsellers, so checkout still loads. Payments must not pretend to succeed; when its breaker is open, fail fast and tell the user to try again.")],
        try_it="Put a toy service behind a 2-second sleep and call it in a loop from a tiny client with a 500 ms timeout. Watch the calls queue up. Add a breaker (opossum, resilience4j or Polly) with a 50% failure threshold and a 10-second cool-down, and log every state change. Remove the sleep and watch it go half-open, then closed.",
    ),
    "retry-backoff": dict(
        quiz_add=[("Your mobile app retries a failed checkout three times with no wait. The payment service had a 20-second blip, and its load graph shows a spike four times the normal size right after. What changed it, and what do you change?",
                   "Every client retried at once, so the blip turned into a retry storm. Add exponential backoff with full jitter, cap the attempts, retry only errors that can pass (timeouts, 503, 429), and send an idempotency key so a retried payment can't charge twice.")],
        try_it="Start a fake service that fails the first two calls of each minute with 503. Call it from 50 parallel clients, first with immediate retries and then with exponential backoff and full jitter. Plot requests per second at the service for both runs and compare the peak.",
    ),
    "bulkhead": dict(
        quiz_add=[("One product page calls Prices, Stock and Reviews from a shared pool of 200 connections. Reviews gets slow and the whole page starts failing. You can change one thing today. What is it?",
                   "Give Reviews its own small pool (for example 20 connections) with a short timeout, and leave the rest to Prices and Stock. When the Reviews pool is full, skip the reviews section instead of waiting.")],
        try_it="Write a small server that calls two fake dependencies through one shared pool of 10 workers. Make one dependency sleep for 5 seconds and measure how many fast calls still succeed. Split the pool 7 / 3 and run it again.",
    ),
    "rate-limiter": dict(
        quiz_add=[("A partner's batch job sends 3,000 requests in the first second of every minute, then nothing. Your limit is 1,000 per minute in a fixed window, and other customers see errors at the top of each minute. What do you change?",
                   "Use a token bucket (or a sliding window) per API key: a small burst size and a steady refill, so the partner is spread over the minute instead of filling it in one second. Return 429 with Retry-After, and tell the partner to pace the job.")],
        try_it="Implement a token bucket in about 20 lines (capacity 10, refill 5 per second) and hit it with a burst of 30 calls and then a steady 6 per second. Print allowed and rejected counts per second. Change capacity and refill and predict the numbers before you run it.",
    ),
    "saga": dict(
        quiz_add=[("A trip booking reserves a flight, then a hotel, then charges the card. The charge fails after the hotel was booked. The hotel's cancel call is down for an hour. What does the saga do?",
                   "It keeps the saga in a “compensating” state and retries the hotel cancellation with backoff until it succeeds, then cancels the flight. Every compensation must be retryable and idempotent. Nothing is rolled back by magic, and someone gets an alert if it stays stuck.")],
        try_it="Write a three-step saga (reserve stock, charge, ship) as a table of states in a SQLite file, with a compensation for each step. Kill the process after step 2, restart it, and check that it picks up where it stopped and compensates correctly.",
    ),
    "transactional-outbox": dict(
        quiz_add=[("A service saves an order, then publishes OrderPlaced to Kafka. Once a week support finds a paid order that the warehouse never heard about. Logs show a pod restart between the two calls. What do you change?",
                   "Write the event to an outbox table in the same transaction as the order, and let a relay (polling or CDC) publish it, retrying until the broker acknowledges. The warehouse must then handle the occasional duplicate.")],
        try_it="Write an order and publish an event in two separate steps, and kill the process between them with a breakpoint. Count the lost events. Then add an outbox table, a 20-line polling relay and an id on each event, repeat the kill, and confirm every event arrives (some twice).",
    ),
    "idempotent-consumer": dict(
        quiz_add=[("A payment-captured message is delivered twice, two minutes apart, and the customer receives two loyalty bonuses. The handler already checks a Redis set of processed ids. Why didn't that help?",
                   "The Redis check and the database write aren't one transaction: the first run added the bonus, crashed before writing the id (or the key expired), and the redelivery passed the check. Store the processed id in the same database transaction as the bonus, with a unique constraint.")],
        try_it="Build a consumer that adds 10 points per message, then send the same message three times. Watch the balance grow by 30. Add a processed_messages table with a unique id, written in the same transaction, and run it again.",
    ),
    "event-sourcing": dict(
        quiz_add=[("A team wants event sourcing for a CRUD admin screen that edits product descriptions, because “we might want history”. What do you suggest?",
                   "A history (audit) table or temporal table is enough: it keeps every version without the cost of events, projections and versioning. Use event sourcing where the events themselves matter to the business (money, stock, bookings) and the history is replayed and reasoned about.")],
        try_it="Model a bank account as a list of events in a JSON file (Opened, Deposited, Withdrew). Write a replay function, then a rule that rejects a withdrawal larger than the balance. Add a new read model, “largest deposit per month”, from the same events without changing them.",
    ),
    "cqrs": dict(
        quiz_add=[("An order screen joins six tables and takes 4 seconds; the write path is simple and fine. The team proposes full CQRS with event sourcing and Kafka. What is the smaller step?",
                   "Build one read model for that screen (a materialized view or a denormalised table updated in the same transaction or by a projection) and leave the write model alone. CQRS can be one table, not a new architecture.")],
        try_it="Take a slow list query in your own app (or a sample database) and create a denormalised read table for it. Keep it updated from the write path and measure the query before and after. Then break the update on purpose and see what users would notice.",
    ),
    "api-gateway": dict(
        quiz_add=[("Three teams keep adding special cases to the gateway: response reshaping for mobile, a discount rule, a feature flag. Releases of the gateway now need all three teams. What has gone wrong, and what do you do?",
                   "Business logic crept into the gateway. Keep it to shared plumbing (routing, TLS, authentication, rate limits), move the discount rule back into its service, and give the mobile app its own backend for frontend owned by the mobile team.")],
        try_it="Run two toy services and put a local gateway (Nginx, Envoy or Kong) in front of them. Route /orders and /users, add one API-key check and one rate limit in gateway config only, and confirm the services didn't change.",
    ),
    "publish-subscribe": dict(
        quiz_add=[("Billing publishes InvoiceIssued. A new reporting service subscribes late and needs the last 90 days of invoices. With your current broker, events are deleted once delivered. What are your options?",
                   "Use a broker that keeps a log (Kafka, or a stream with retention) so the new subscriber can replay, or backfill it once from Billing's database or an export. The producer still doesn't change; that's the point of pub/sub.")],
        try_it="With a local Redis or NATS, publish OrderPlaced events from one script and start two subscribers that do different things (an email log, a running total). Add a third subscriber while it runs, and confirm the publisher needed no change. Then stop a subscriber and see what it misses.",
    ),
    "competing-consumers": dict(
        quiz_add=[("Image resizing runs on 4 workers. On Monday mornings the queue reaches 50,000 jobs and users wait an hour. CPU on the workers is at 30%. What do you check before adding workers?",
                   "Low CPU with a long queue means the workers are waiting on something: the storage, a lock, a prefetch of one, or a downstream limit. Find the bottleneck first. Then scale on queue age, not CPU, and set a ceiling the downstream can take.")],
        try_it="Put 1,000 fake jobs on a queue (RabbitMQ, SQS-local or Redis lists) and process them with one worker, then four. Time both. Kill a worker in the middle of a job and confirm the job is redelivered and not lost.",
    ),
    "sidecar": dict(
        quiz_add=[("A team of six runs four services and wants a service mesh “for mTLS and retries”. What would you ask before installing one?",
                   "Is there a simpler way: TLS in the load balancer, a shared client library with retries, the platform's network policies? A mesh adds a control plane, sidecar resources and a new failure mode to debug. It pays off with many services and teams, not four.")],
        try_it="Run a small app in a pod (kind or minikube) with a second container that adds a header or collects logs, sharing localhost. Then remove the sidecar and add the same feature to the app. Compare what changed in each version.",
    ),
    "service-discovery": dict(
        quiz_add=[("After a deploy, 5% of calls to Orders fail for about 30 seconds. The new pods show as healthy in the registry before they finish loading their cache. What do you fix?",
                   "The readiness check: make it pass only when the pod can serve (cache loaded, connections open), so traffic waits. Add a short drain on shutdown so old pods leave the registry before they stop.")],
        try_it="In a local Kubernetes cluster, run two replicas behind a Service and curl it by name in a loop. Delete one pod and watch requests keep working. Then add a readiness probe that fails for the first 20 seconds and see how a new pod joins.",
    ),
    "sharding": dict(
        quiz_add=[("You shard an online shop by country. One country is 60% of all orders, and its shard is at 95% CPU while the rest are idle. What went wrong, and what is a better key?",
                   "The key has low cardinality and an uneven spread, so one shard got most of the load. Use a key with many values that spreads evenly and matches the main queries, such as customer id, hashed into many logical shards that you can move between machines.")],
        try_it="Take 100,000 fake customer ids and assign them to 4 shards with hash % 4. Count rows per shard. Change to 5 shards and count how many ids moved. Then do the same with 64 logical shards mapped onto 4 machines and compare how much data a fifth machine would move.",
    ),
    "replication": dict(
        quiz_add=[("Users update their address, reload the page, and see the old address for a few seconds. Reads go to followers. What are two fixes?",
                   "Read your own writes from the leader for a short time after a change (or for that user's own profile), or wait until the follower has caught up past the write's position before reading. Other users can keep reading from followers.")],
        try_it="Start a Postgres primary and one replica with Docker. Write a row and read it from the replica in a loop, timing the lag. Pause the replica, write more, and resume it; watch it catch up. Then promote it and notice what the old primary's clients now see.",
    ),
    "cache-aside": dict(
        quiz_add=[("The price of a product is cached for 10 minutes. Marketing changes it and complains the old price shows for up to 10 minutes. What do you change?",
                   "Delete the key when the price is written (in the same code path, or via change data capture so every writer is covered), and keep the TTL as a safety net. Don't lower the TTL to seconds; that removes most of the cache's benefit.")],
        try_it="Put Redis in front of a slow (300 ms) product lookup with cache-aside and a 60-second TTL. Measure hit rate and average latency over 1,000 random reads. Then expire a hot key while 50 clients read it at once and count how many hit the database: that is a stampede.",
    ),
    "leader-election": dict(
        quiz_add=[("A nightly billing job runs on three instances so it survives a crash. One night every customer is billed twice. The job uses a lock row with a 30-second timeout and the run takes 2 minutes. What happened?",
                   "The leader's lock expired during a long run (or a GC pause), a second instance took over, and both ran. Renew the lease while working, check a fencing token on every write, and make the billing step idempotent per customer and month.")],
        try_it="Run three copies of a script that compete for a lease in etcd or Redis (SET NX with expiry) and print when each becomes leader. Kill the leader and time the handover. Then pause the leader with SIGSTOP past its lease and resume it; see what it does if it doesn't check its lease.",
    ),
}

for _rev in REVISIONS.values():
    _rev.setdefault("revised", ("Nov 2026", "a “what would you do?” question and a try it"))
