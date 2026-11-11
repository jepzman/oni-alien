# Data consistency collection: Transactional Outbox, Idempotent Consumer, Event Sourcing, CQRS.
# (Saga is hand-made in public/notes/saga.html.)

# ------------------------------------------------------------------ 06 Transactional Outbox
ob_problem = Doodle(760, 290, "Doodle of the dual-write problem. The Order service saves the order in its database, then crashes before publishing the OrderPlaced event to the broker. The database has the order, but Shipping and Email never hear about it.",
                    "Two separate writes, no shared transaction: a crash in between leaves them disagreeing forever.")
ob_problem.box(20, 100, 170, 80, "Order service", "blue")
ob_problem.arrow(196, 120, 330, 70, color="green", label="① INSERT order ✓", lx=250, ly=72)
ob_problem.db(380, 50, "orders db")
ob_problem.arrow(196, 160, 330, 210, dash=True, color="red", label="② publish event", lx=250, ly=226)
ob_problem.box(340, 180, 140, 60, "broker", "y")
ob_problem.icon("cross", 250, 150, .6, color="red")
ob_problem.note(150, 270, "crash between ① and ② !", "red")
ob_problem.box(580, 150, 150, 50, "Shipping", "paper", size=18)
ob_problem.box(580, 220, 150, 50, "Email", "paper", size=18)
ob_problem.arrow(486, 205, 574, 175, dash=True, color="red")
ob_problem.arrow(486, 215, 574, 240, dash=True, color="red")
ob_problem.note(655, 130, "never hear about it", "red")

ob_analogy = Doodle(760, 260, "Doodle of an office out-tray. You write the letter and drop it in your own out-tray in one go. A mail clerk walks by on a schedule, collects everything in the out-tray, posts it, and ticks it off. If the clerk is off sick, the letters wait safely in the tray.",
                    "You only ever drop letters into your own out-tray. The mail clerk delivers them later, even after a sick day.")
ob_analogy.box(30, 80, 170, 120, None, "paper")
ob_analogy.icon("envelope", 60, 100, .9, fill="y")
ob_analogy.icon("envelope", 110, 120, .9, fill="y")
ob_analogy.note(115, 230, "my out-tray")
ob_analogy.arrow(210, 140, 390, 140, label="clerk collects every 5 min", lx=300, ly=128)
ob_analogy.icon("parcel", 400, 105, 1.1)
ob_analogy.arrow(470, 140, 600, 140, label="posts it", lx=535, ly=128)
ob_analogy.icon("truck", 610, 110, 1.6)
ob_analogy.note(300, 190, "…and ticks it off in the log ✓", "pen")
ob_analogy.note(560, 236, "clerk off sick? letters just wait", "pen")

ob_how = Doodle(760, 300, "Outbox flow. The Order service writes the order row and an outbox row in the same database transaction. A separate relay process reads new outbox rows, publishes each to the broker, and marks it sent. Consumers receive the event, possibly more than once.",
                "One local transaction writes both rows. The relay turns outbox rows into messages, at least once.")
ob_how.box(20, 120, 160, 70, "Order service", "blue")
ob_how.box(240, 40, 250, 230, None, "paper", dash=True)
ob_how.head(365, 30, "ONE transaction", size=18)
ob_how.db(300, 90, None, w=90)
ob_how.note(300, 175, "orders")
ob_how.db(430, 90, None, w=90, fill="y")
ob_how.note(430, 175, "outbox")
ob_how.text(365, 230, "BEGIN · insert both · COMMIT", size=16)
ob_how.arrow(186, 155, 250, 155)
ob_how.box(540, 50, 200, 60, "relay / CDC", "y")
ob_how.arrow(480, 96, 536, 84, label="poll new rows", lx=500, ly=134, anchor="start")
ob_how.box(560, 170, 170, 56, "broker", "green")
ob_how.arrow(640, 114, 640, 166, label="publish", lx=650, ly=146, anchor="start")
ob_how.arrow(640, 230, 640, 280, label="consumers (dedupe!)", lx=630, ly=272, anchor="end")

OUTBOX = dict(
    slug="transactional-outbox",
    kicker="a.k.a. “don't write to two places at once”",
    tldr="When a service must <b>update its database and publish an event</b>, don't do two separate writes. Write the change <b>and the event</b> (into an <code>outbox</code> table) in <b>one local transaction</b>. A separate relay reads the outbox and publishes the events to the broker, retrying until each one is sent.",
    chips=[("Family", "data consistency / messaging"), ("Lives in", "the service + its own database"), ("Solves", "the dual-write problem"), ("Pairs with", "saga, idempotent consumer, CDC")],
    problem='''  <p class="lead">In event-driven systems a service often has to do two things together: <b>save a change</b> and <b>tell others about it</b>. Those are writes to two different systems (database + message broker), and there's <span class="hl-pink">no transaction that covers both</span>.</p>
  <ul>
    <li><b>DB first, then publish:</b> crash in between and the order exists but nobody hears about it. Shipping never ships.</li>
    <li><b>Publish first, then DB:</b> crash in between and everyone hears about an order that was never saved.</li>
    <li>Wrapping the publish in a DB transaction doesn't help: the broker isn't part of it, and the publish can't be rolled back.</li>
  </ul>
  <p>This is the <b>dual-write problem</b>, and it's one of the most common sources of “ghost” and “missing” data in microservices.</p>''',
    problem_figs=[ob_problem],
    analogy_side="the office out-tray",
    analogy='''  <p>In an old-style office you don't walk every letter to the post office yourself. You write it, and in the same moment you drop it in <b>your own out-tray</b>. A mail clerk comes round on a schedule, collects everything in the tray, posts it, and ticks it off in a log.</p>
  <ul>
    <li>Writing the letter and putting it in the tray is <b>one action at your own desk</b>. It can't half-happen.</li>
    <li>If the clerk is off sick, the letters wait safely and go out tomorrow. Nothing is lost.</li>
    <li>If the clerk posts a letter but forgets to tick it off, it might be posted twice. The receiver should notice a duplicate.</li>
  </ul>''',
    analogy_figs=[ob_analogy],
    map=[("Writing the letter + dropping it in the tray", "One DB transaction: business row + outbox row"),
         ("Your own out-tray", "The <code>outbox</code> table in the service's own database"),
         ("The mail clerk's rounds", "The relay: a poller or change-data-capture (CDC)"),
         ("Posting the letter", "Publishing the event to the broker"),
         ("Ticking it off in the log", "Marking the outbox row as sent"),
         ("Same letter posted twice", "At-least-once delivery → consumers must dedupe")],
    how_side="one transaction, then a relay",
    how='  <p>The trick is to turn two writes into <b>one local write</b> plus a reliable background job.</p>',
    how_figs=[ob_how],
    steps=[("Add an outbox table", "Columns like <code>id</code>, <code>aggregate_id</code>, <code>type</code>, <code>payload</code>, <code>created_at</code>, <code>sent_at</code>. It lives in the same database as the business data."),
           ("Write both in one transaction", "<code>BEGIN</code>; insert the order; insert an <code>OrderPlaced</code> row into the outbox; <code>COMMIT</code>. Both happen or neither does."),
           ("Relay the rows", "A poller selects unsent rows in order (or a CDC tool like Debezium tails the DB log) and publishes each one to the broker."),
           ("Mark as sent (or delete)", "After the broker confirms, set <code>sent_at</code>. If the relay crashes first, it publishes again on restart: delivery is <b>at least once</b>."),
           ("Make consumers idempotent", "Each event carries its outbox <code>id</code>; consumers skip ids they've already processed (see note 07). Clean up old outbox rows regularly.")],
    vocab=[("Dual write", "Writing to two systems without a shared transaction."),
           ("Outbox table", "A table of events waiting to be published, in the service's DB."),
           ("Message relay", "The process that moves outbox rows to the broker."),
           ("Change data capture (CDC)", "Reading the DB's transaction log to stream changes."),
           ("At-least-once delivery", "Every message arrives, maybe more than once."),
           ("Inbox table", "The consumer-side twin: records processed message ids.")],
    code=dict(file="place-order.sql + relay.ts", note="Postgres, polling relay", src='''
-- ① the service: both rows in ONE transaction
BEGIN;
INSERT INTO orders (id, customer_id, total) VALUES ('o-42', 'c-7', 49.00);
INSERT INTO outbox (id, type, aggregate_id, payload)
VALUES (gen_random_uuid(), 'OrderPlaced', 'o-42', '{"total":49.00}');
COMMIT;

// ② the relay: runs every second, safe with several copies running
const rows = await db.query(`
  SELECT * FROM outbox WHERE sent_at IS NULL
  ORDER BY created_at LIMIT 100
  FOR UPDATE SKIP LOCKED`);              // two relays never grab the same row
for (const row of rows) {
  await broker.publish(row.type, { id: row.id, ...row.payload });
  await db.query("UPDATE outbox SET sent_at = now() WHERE id = $1", [row.id]);
}
'''),
    tools="tools: Debezium (CDC from Postgres / MySQL logs to Kafka), MassTransit and NServiceBus outbox (.NET), Spring Modulith / Eventuate Tram (Java), AWS DynamoDB Streams.",
    gains=["<b>No lost or ghost events.</b> The change and the event commit together.",
           "<b>Works with any broker</b>; no distributed transactions needed.",
           "<b>Survives outages.</b> If the broker is down, events wait in the outbox.",
           "<b>Keeps event order per aggregate</b> when the relay reads in order.",
           "<b>An audit trail</b> of what was published and when."],
    losses=["<b>At-least-once, not exactly-once.</b> Consumers must handle duplicates.",
            "<b>A little delay</b> between commit and publish (polling interval).",
            "<b>Another moving part</b>: the relay or CDC pipeline to run and monitor.",
            "<b>Extra DB load</b> and a table that needs cleaning up.",
            "<b>Ordering across instances</b> needs care if several relays run."],
    baseline="Each line compares a service that does a <b>dual write</b> (save, then publish) to the same service using a <b>transactional outbox</b>.",
    ratings=[(4, 3, "An extra table, a relay and duplicate handling to understand."),
             (4, 3, "Some extra DB writes and a relay or CDC service to run."),
             (4, 4, "Neutral. The relay deploys independently."),
             (3, 4, "Easy to test: assert the outbox row exists after the transaction."),
             (4, 4, "Neutral to slightly positive; CDC scales well."),
             (3, 4, "Events queue up in the outbox during spikes or broker outages."),
             (2, 5, "Crashes and broker outages no longer lose or invent events."),
             (4, 3, "One extra insert per transaction; events arrive a bit later."),
             (3, 4, "Adding new event types or consumers is straightforward.")],
    pitfalls=[("Publishing inside the transaction anyway", "Code calls <code>broker.publish()</code> before <code>COMMIT</code> “to be safe”, bringing the dual write back.", "only the relay publishes; the service only writes rows."),
              ("Consumers that can't handle duplicates", "The relay crashes after publishing but before marking the row, so the event goes out twice and an email is sent twice.", "idempotent consumers keyed by the event id."),
              ("Several relays stepping on each other", "Two relay instances read the same rows and publish everything twice, out of order.", "<code>FOR UPDATE SKIP LOCKED</code>, partitioning, or a single active relay."),
              ("Never cleaning the outbox", "The table grows to 500 million rows and the polling query slows the whole DB.", "delete or archive sent rows; index <code>sent_at IS NULL</code>."),
              ("Huge payloads in the outbox", "Whole documents are copied into every event, bloating the DB and the broker.", "send ids plus the fields consumers actually need.")],
    use=["A service changes its own data <b>and</b> must notify others reliably.",
         "You use sagas or event-driven integration between services.",
         "The broker doesn't share a transaction with your database (almost always).",
         "Losing or inventing an event would cost money or trust."],
    skip=["Nobody else needs to know about the change.",
          "The database and queue really are the same system with one transaction.",
          "A short delay before others hear about the change is unacceptable.",
          "A lost notification is harmless (e.g. a best-effort cache refresh)."],
    related=["<b>Saga</b>", "<b>Idempotent consumer</b>", "<b>Publish–subscribe</b>", "<b>Event sourcing</b> · the event log is the outbox", "<b>Change data capture</b>"],
    quiz=[("What is the dual-write problem?", "Writing to two systems (e.g. a database and a broker) without one transaction covering both, so a crash in between leaves them inconsistent."),
          ("Why does the outbox give at-least-once delivery, not exactly-once?", "The relay can publish a message and crash before marking it sent; on restart it publishes it again."),
          ("Polling relay or CDC: what's the difference?", "A poller queries the outbox table on a schedule; CDC reads the database's transaction log and streams new rows, with lower latency and no polling load."),
          ("Where must the outbox table live?", "In the same database as the business data, so both inserts are in one local transaction.")],
    remember="Never write to two places at once. Write <span class=\"hl\">once, locally</span>, and let a relay carry the news, and expect the news to arrive twice.",
    sources=["Chris Richardson, <i>Microservices Patterns</i>, “Transactional outbox”, and microservices.io.",
             "Debezium docs, “Outbox Event Router”.",
             "Gunnar Morling, “Reliable Microservices Data Exchange With the Outbox Pattern”.",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, chapter 11."],
)

# ------------------------------------------------------------------ 07 Idempotent Consumer
ic_problem = Doodle(760, 260, "Doodle of a duplicate message. The broker delivers PaymentCaptured for order 42, the Email consumer sends a receipt but crashes before acknowledging, so the broker delivers the same message again and the customer gets two receipts and two loyalty points awards.",
                    "The consumer did the work, then crashed before saying “got it”. The broker, doing its job, delivers again.")
ic_problem.box(20, 90, 140, 70, "broker", "y")
ic_problem.msgs(40, 60, 2, fill="y", size=26)
ic_problem.arrow(166, 110, 330, 80, label="PaymentCaptured #42", lx=248, ly=74)
ic_problem.arrow(166, 140, 330, 170, color="red", label="…again (no ack)", lx=248, ly=180)
ic_problem.box(340, 90, 150, 80, "Loyalty", "blue", sub="crash before ack")
ic_problem.arrow(496, 110, 600, 70, color="red")
ic_problem.arrow(496, 150, 600, 190, color="red")
ic_problem.box(606, 40, 140, 56, "+100 pts", "pink", stroke="red", size=18)
ic_problem.box(606, 160, 140, 56, "+100 pts", "pink", stroke="red", size=18)
ic_problem.note(670, 245, "customer gets 200 ✗", "red")

ic_analogy = Doodle(760, 240, "Doodle of an elevator call button and a door bell. Pressing the elevator button five times calls one elevator, not five. A ticket with a number is stamped once; showing it again does nothing new.",
                    "Pressing the lift button five times still calls one lift. Same request, same result.")
ic_analogy.box(60, 40, 110, 160, None, "paper")
ic_analogy.circle(115, 95, 22, "y")
ic_analogy.head(115, 102, "▲", size=20)
ic_analogy.circle(115, 150, 22, "paper")
ic_analogy.head(115, 157, "▼", size=20)
ic_analogy.note(115, 226, "press ×5 = 1 lift")
ic_analogy.icon("ticket", 330, 70, 1.6, fill="y")
ic_analogy.head(375, 115, "#42", size=22)
ic_analogy.note(380, 180, "ticket #42 stamped ✓")
ic_analogy.note(380, 206, "show it again → “already used”", "pen")
ic_analogy.icon("calendar", 600, 60, 1.6)
ic_analogy.note(645, 196, "“already booked for you”")

ic_how = Doodle(760, 330, "Idempotent consumer flow. A message with id m-42 arrives. In one transaction the consumer tries to insert m-42 into a processed_messages table. If the insert succeeds it applies the effect and commits; if the id already exists, it skips the work and just acknowledges.",
                "Remember every message id you've handled, in the same transaction as the work.")
ic_how.box(20, 110, 130, 60, "msg m-42", "y")
ic_how.arrow(156, 140, 250, 140)
ic_how.raw('<path class="d f-y" d="M330 70 L410 140 L330 210 L250 140 Z"/>')
ic_how.text(330, 135, "seen", size=17)
ic_how.text(330, 155, "m-42?", size=17)
ic_how.arrow(410, 140, 520, 80, color="green", label="new", lx=452, ly=96, anchor="end")
ic_how.box(526, 40, 220, 76, "apply effect", "green", sub="+ insert m-42, one tx")
ic_how.arrow(410, 140, 520, 210, color="red", label="seen before", lx=440, ly=208, anchor="end")
ic_how.box(526, 180, 220, 60, "just ack", "pink", stroke="red")
ic_how.db(330, 236, "processed_messages", w=90)

IDEMP = dict(
    slug="idempotent-consumer",
    kicker="a.k.a. “twice is the same as once”",
    tldr="Messages and retried requests can arrive <b>more than once</b>. Make the receiver <b>idempotent</b>: give every message or request a unique id, <b>record the ids you've already handled</b> (in the same transaction as the work), and when a duplicate shows up, <b class=\"green\">skip the work</b> and return the original result.",
    chips=[("Family", "data consistency / messaging"), ("Lives in", "every message consumer & write API"), ("Also called", "deduplication, idempotency keys"), ("Pairs with", "outbox, retries, saga")],
    problem='''  <p class="lead">Almost every real messaging system gives you <b>at-least-once</b> delivery. “Exactly once” over a network is, in practice, <span class="hl-pink">at-least-once plus deduplication</span>.</p>
  <ul>
    <li>A consumer processes a message, then crashes before acknowledging it. The broker redelivers it.</li>
    <li>The outbox relay publishes, then crashes before marking the row sent. The event goes out again.</li>
    <li>A client times out waiting for <code>POST /payments</code> and retries, but the first one actually worked.</li>
    <li>A rebalance moves a partition to another consumer, which re-reads the last few messages.</li>
  </ul>
  <p>If the handler isn't idempotent, duplicates become <b>double charges, double emails, double stock reservations</b>.</p>''',
    problem_figs=[ic_problem],
    analogy_side="the lift button",
    analogy='''  <p>Pressing the lift button five times doesn't call five lifts. The first press registers the request; the others change nothing. That's <b>idempotent</b>: doing it again has the same effect as doing it once.</p>
  <ul>
    <li>A cinema ticket with a number gets stamped once. Show it again and the usher says “already used”.</li>
    <li>“Set the thermostat to 21 °C” is naturally idempotent. “Turn it up by 1 °C” is not: say it twice and it's 2 degrees warmer.</li>
  </ul>''',
    analogy_figs=[ic_analogy],
    map=[("Pressing the lift button again", "The same message delivered again"),
         ("The ticket number", "Message id / idempotency key"),
         ("The usher's list of stamped tickets", "A processed-messages (inbox) table"),
         ("“Already used”", "Skip the work, return the stored result"),
         ("“Set to 21 °C” vs “turn up 1 °C”", "Naturally idempotent vs non-idempotent operations")],
    how_side="remember what you've done",
    how='''  <p>There are two ways to get there, and good systems use both:</p>
  <ul>
    <li><b>Make the operation naturally idempotent:</b> “set status = PAID”, upserts, “reserve item X for order 42” (a unique constraint stops a second row).</li>
    <li><b>Deduplicate by id:</b> record each processed id and skip repeats. Needed for things like “add 100 points” or “send an email”.</li>
  </ul>''',
    how_figs=[ic_how],
    steps=[("Give every message an id", "The producer sets a unique id (UUID or outbox row id). For HTTP, the client sends an <code>Idempotency-Key</code> header."),
           ("Check and record in one transaction", "Insert the id into <code>processed_messages</code> with a unique constraint, in the same DB transaction as the business change."),
           ("Duplicate? Skip", "If the insert hits the unique constraint, the work was already done: acknowledge the message (or return the stored response) and stop."),
           ("Store the result for APIs", "For idempotent HTTP endpoints, save the response with the key so a retry gets exactly the same answer."),
           ("Expire old ids", "Keep ids for longer than the longest possible redelivery or retry window (e.g. 7 days), then delete them.")],
    vocab=[("Idempotent", "Doing it twice has the same effect as doing it once."),
           ("At-least-once", "Delivery guarantee where duplicates are possible."),
           ("Exactly-once processing", "At-least-once delivery + idempotent handling."),
           ("Idempotency key", "Client-chosen id that marks a request as a repeat."),
           ("Inbox / processed table", "Where a consumer records ids it has handled."),
           ("Natural key", "A business id (order 42) that makes duplicates detectable.")],
    code=dict(file="handle-payment-captured.ts", note="dedupe in the same transaction", src='''
export async function onPaymentCaptured(msg: { id: string; orderId: string; points: number }) {
  await db.transaction(async (tx) => {
    // the unique constraint on message_id does the dedupe
    const inserted = await tx.query(
      `INSERT INTO processed_messages (message_id) VALUES ($1)
       ON CONFLICT DO NOTHING RETURNING message_id`, [msg.id]);

    if (inserted.rowCount === 0) return;          // seen it: skip, just ack

    await tx.query(
      "UPDATE loyalty SET points = points + $1 WHERE order_id = $2",
      [msg.points, msg.orderId]);
  });                                             // both commit together
  // ack AFTER commit; a crash before this only causes a harmless redelivery
}
'''),
    tools="built-ins: Stripe-style Idempotency-Key headers, Kafka idempotent producer + transactions (inside Kafka), AWS SQS FIFO deduplication id (5-minute window), MassTransit / NServiceBus inbox, AWS Lambda Powertools Idempotency.",
    gains=["<b>Duplicates become harmless.</b> Retries and redeliveries are safe.",
           "<b>Enables at-least-once everywhere</b>, which is simple and reliable.",
           "<b>Safe client retries</b> on payments and other writes.",
           "<b>Easier recovery.</b> You can replay messages after an incident.",
           "<b>Clear, testable rule</b>: send it twice, assert one effect."],
    losses=["<b>An extra table and write</b> per message.",
            "<b>Must be in the same transaction</b>, which is hard if the effect is an external call (e.g. sending email).",
            "<b>Id retention</b> needs a policy and cleanup job.",
            "<b>Producers must send stable ids</b>; a new id per retry defeats it.",
            "<b>Slightly more complex handlers</b> everywhere."],
    baseline="Each line compares consumers that <b>assume each message arrives once</b> to the same consumers with <b>id-based deduplication</b>.",
    ratings=[(4, 3, "Every handler gains a dedupe step and a rule to remember."),
             (4, 4, "A small table and an extra insert; little real cost."),
             (4, 4, "Neutral."),
             (3, 4, "Simple property to test: deliver twice, assert one effect."),
             (4, 4, "Neutral; the dedupe table is keyed and cheap."),
             (3, 4, "Safe redelivery means you can scale consumers and rebalance freely."),
             (2, 5, "Crashes, retries and replays stop causing double effects."),
             (4, 4, "One indexed insert per message."),
             (3, 4, "New consumers can replay history safely.")],
    pitfalls=[("Check, then act, outside a transaction", "“Have I seen m-42? No.” Then two consumer instances both process it at once.", "a unique constraint and the work in one transaction."),
              ("New id on every retry", "The client generates a fresh UUID each time it retries, so every retry looks new.", "create the key once per logical operation and reuse it on retries."),
              ("Side effects outside the transaction", "The email is sent, then the DB commit fails; the retry sends it again.", "record the intent in the DB (outbox) and send from there, or use the provider's idempotency key."),
              ("Forgetting ids too soon", "Ids expire after 1 hour, but the broker can redeliver after a 6-hour outage.", "keep ids longer than the maximum redelivery / retry window."),
              ("Relying on the broker's “exactly once”", "Kafka transactions cover Kafka-to-Kafka; your DB write is outside it.", "dedupe at your own system boundary anyway.")],
    use=["Any message consumer on an at-least-once broker (that's nearly all).",
         "Write APIs that clients may retry: payments, orders, bookings.",
         "Saga steps and compensations.",
         "Jobs you may want to replay after a bug fix."],
    skip=["The operation is already naturally idempotent (set, upsert, delete by id).",
          "Duplicates are truly harmless (refreshing a cache).",
          "Read-only requests (GET) with no side effects.",
          "You can't get a stable id from the producer. Fix that first."],
    related=["<b>Transactional outbox</b>", "<b>Retry with backoff</b>", "<b>Saga</b>", "<b>Competing consumers</b>", "<b>Event sourcing</b>"],
    quiz=[("Is “UPDATE balance = balance + 10” idempotent? And “UPDATE status = 'PAID'”?", "The first is not (twice adds 20). The second is (twice still PAID)."),
          ("Why must the dedupe record and the work be in the same transaction?", "Otherwise a crash between them either loses the record (work done twice) or loses the work (marked done but never happened)."),
          ("A client retries POST /payments with a new UUID each time. What goes wrong?", "The server sees every retry as a new request and may charge again. The key must stay the same across retries of one operation."),
          ("What does “exactly-once processing” usually mean in practice?", "At-least-once delivery combined with idempotent (deduplicating) handling.")],
    remember="Assume <span class=\"hl\">everything arrives twice</span>. Give it an id, write the id with the work, and the second copy becomes a no-op.",
    sources=["Chris Richardson, microservices.io, “Pattern: Idempotent Consumer”.",
             "Stripe API docs, “Idempotent requests”.",
             "Gregor Hohpe &amp; Bobby Woolf, <i>Enterprise Integration Patterns</i>, “Idempotent Receiver”.",
             "AWS Builders' Library, “Making retries safe with idempotent APIs”."],
)

# ------------------------------------------------------------------ 08 Event Sourcing
es_problem = Doodle(760, 240, "Doodle of a normal accounts table storing only the current balance of 70 dollars. Someone asks how it got to 70, whether it was 120 last Tuesday, and who changed it. The table can't answer: each update overwrote the previous value.",
                    "UPDATE overwrites history. The current value survives; the story of how we got there doesn't.")
es_problem.box(30, 60, 260, 120, None, "paper")
es_problem.head(160, 52, "accounts", size=18)
es_problem.line("M30 100 H290 M150 60 V180", thin=True)
es_problem.text(90, 88, "id", size=17)
es_problem.text(220, 88, "balance", size=17)
es_problem.text(90, 140, "acc-1", size=19)
es_problem.head(220, 142, "$70", size=24)
es_problem.note(160, 214, "UPDATE … SET balance = 70", "red")
es_problem.note(420, 70, "how did it get to $70?", "pen", anchor="start")
es_problem.note(420, 110, "was it $120 last Tuesday?", "pen", anchor="start")
es_problem.note(420, 150, "who changed it, and why?", "pen", anchor="start")
es_problem.note(420, 196, "…no idea, it was overwritten ✗", "red", anchor="start")
es_problem.arrow(300, 120, 410, 100, dash=True)

es_analogy = Doodle(760, 250, "Doodle of a bank passbook with lines: deposit 100, deposit 50, withdraw 30, withdraw 50. The balance of 70 is just the sum of the lines. Mistakes are never erased; a correcting line is added instead.",
                    "The passbook never erases a line. The balance is just the lines added up.")
es_analogy.box(30, 30, 380, 200, None, "paper")
rows = [("+ deposit", "+100"), ("+ deposit", "+50"), ("− cash out", "−30"), ("− card", "−50")]
for i, (a, b) in enumerate(rows):
    y = 70 + i * 34
    es_analogy.text(60, y, a, anchor="start", size=19)
    es_analogy.text(380, y, b, anchor="end", size=19)
    es_analogy.line(f"M45 {y + 10} H395", thin=True, color="soft")
es_analogy.head(60, 214, "balance", anchor="start", size=19)
es_analogy.head(380, 214, "= $70", anchor="end", size=22)
es_analogy.icon("book", 500, 60, 1.8)
es_analogy.note(560, 200, "never erase, only add", "pen")
es_analogy.note(560, 226, "a mistake? add a correcting line", "pen")

es_how = Doodle(760, 300, "Event sourcing flow. A command Withdraw 50 dollars arrives. The service loads the account's past events, replays them to get the current state, checks the rule, then appends a new MoneyWithdrawn event to the append-only event store. Projections read the events to build query views like the current balance and a monthly statement.",
                "Commands are checked against state rebuilt from events; new facts are appended, never updated.")
es_how.box(20, 40, 170, 60, "Withdraw $50", "blue", size=19)
es_how.arrow(196, 70, 290, 70)
es_how.box(296, 30, 190, 80, "Account", "y", sub="replay → check → decide")
es_how.arrow(492, 70, 560, 130, label="append", lx=540, ly=88, anchor="start")
es_how.box(20, 150, 700, 56, None, "paper")
for i, ev in enumerate(["Opened", "Deposited 100", "Deposited 50", "Withdrew 30", "Withdrew 50"]):
    es_how.box(28 + i * 138, 158, 132, 40, ev, "green" if i == 4 else "y", size=13, rx=4)
es_how.note(370, 230, "event store: append-only log for acc-1", "pen")
es_how.arrow(390, 104, 300, 150, dash=True, label="load + replay", lx=270, ly=132, anchor="end")
es_how.arrow(200, 210, 140, 260, label="project", lx=120, ly=240, anchor="end")
es_how.box(150, 250, 160, 44, "balance = $70", "green", size=17)
es_how.arrow(520, 210, 580, 250)
es_how.box(500, 250, 220, 44, "monthly statement", "green", size=17)

ES = dict(
    slug="event-sourcing",
    kicker="a.k.a. “keep the receipts, all of them”",
    tldr="Instead of storing only the <b>current state</b> and overwriting it, store <b>every change as an immutable event</b> in an append-only log (<code>Deposited 100</code>, <code>Withdrew 30</code>…). The current state is <b>derived by replaying the events</b>. You never lose history, and you can build new views of the past at any time.",
    chips=[("Family", "data management"), ("Lives in", "the service that owns the data"), ("Popular with", "finance, logistics, audit-heavy domains"), ("Pairs with", "CQRS, outbox, snapshots")],
    problem='''  <p class="lead">Most systems store state with <code>UPDATE</code>: each change <span class="hl-pink">overwrites the previous value</span>. That's simple, but it throws away the story.</p>
  <ul>
    <li><b>Audit:</b> “Who changed this order's address, and when?” Not recorded, or scattered across logs.</li>
    <li><b>Debugging:</b> “How did this account end up negative?” You only see the end result.</li>
    <li><b>New questions:</b> “How many people added an item and then removed it?” The removes were overwritten.</li>
    <li><b>Integration:</b> other services want to know <i>what happened</i>, not just the latest snapshot.</li>
  </ul>''',
    problem_figs=[es_problem],
    analogy_side="the bank passbook",
    analogy='''  <p>An old bank passbook (or any accountant's ledger) doesn't have a single “balance” box that gets rubbed out and rewritten. It has <b>lines</b>: every deposit and withdrawal, in order. The balance is just those lines added up.</p>
  <ul>
    <li>Accountants never erase. A mistake is fixed by adding a <b>correcting entry</b>.</li>
    <li>You can answer “what was the balance on 1 March?” by adding up the lines until that date.</li>
    <li>Adding up thousands of lines every time is slow, so the book prints a <b>carried-forward balance</b> at the top of each page (a snapshot).</li>
  </ul>''',
    analogy_figs=[es_analogy],
    map=[("Each line in the passbook", "An immutable event (MoneyDeposited, MoneyWithdrawn)"),
         ("The passbook itself", "The event store (append-only log per aggregate)"),
         ("Adding up the lines", "Replaying events to rebuild state"),
         ("Correcting entry, never an eraser", "Compensating event, never UPDATE/DELETE"),
         ("Carried-forward balance on each page", "Snapshot to speed up replay"),
         ("A monthly statement printed from the lines", "A projection / read model")],
    how_side="append facts, derive state",
    how="""  <p>Events are <b>facts in the past tense</b>. They're appended to a stream per entity (an “aggregate”), and everything else is calculated from them.</p>""",
    how_figs=[es_how],
    steps=[("Model events as past-tense facts", "<code>OrderPlaced</code>, <code>ItemAdded</code>, <code>AddressChanged</code>, each with the data needed to apply it and a timestamp."),
           ("Handle a command", "Load the aggregate's events (or the latest snapshot + newer events), replay them to get current state, and check business rules."),
           ("Append new events", "Write the resulting events to the stream with an expected version number, so two concurrent writers can't both succeed (optimistic concurrency)."),
           ("Project for reading", "Subscribers turn events into read models: a balance table, a search index, a statement. These can be rebuilt from scratch at any time."),
           ("Snapshot and version", "Save a snapshot every N events to keep loading fast, and version event schemas so old events still replay after the code changes.")],
    vocab=[("Event", "An immutable record of something that happened."),
           ("Event store", "Append-only database of events, grouped into streams."),
           ("Aggregate / stream", "One entity's events, e.g. all events for acc-1."),
           ("Projection", "Code that turns events into a read model."),
           ("Snapshot", "Saved state at event N, to avoid replaying from zero."),
           ("Upcasting", "Converting old event versions to the current shape on read.")],
    code=dict(file="account.ts", note="replay, decide, append", src='''
type Event =
  | { type: "Deposited"; amount: number }
  | { type: "Withdrew"; amount: number };

const apply = (balance: number, e: Event) =>
  e.type === "Deposited" ? balance + e.amount : balance - e.amount;

export async function withdraw(accountId: string, amount: number) {
  const { events, version } = await store.load(`account-${accountId}`);
  const balance = events.reduce(apply, 0);            // replay
  if (amount > balance) throw new Error("Insufficient funds");   // decide
  await store.append(`account-${accountId}`,          // append, never update
    [{ type: "Withdrew", amount }],
    { expectedVersion: version });                     // optimistic concurrency
}
'''),
    tools="tools: EventStoreDB (Kurrent), Marten (Postgres, .NET), Axon (Java), Eventuous, or a plain append-only table with a (stream_id, version) unique key. Kafka is a log, but not a per-aggregate event store by itself.",
    gains=["<b>Complete audit trail</b> for free: every change, who, when.",
           "<b>Time travel.</b> Rebuild state at any point in the past.",
           "<b>New read models any time</b> by replaying history.",
           "<b>Natural integration.</b> Events are already there for other services.",
           "<b>Append-only writes</b> are fast and conflict-friendly."],
    losses=["<b>Steep learning curve</b> and an unusual way of thinking.",
            "<b>Event schema changes are forever.</b> Old events must still replay.",
            "<b>Querying current state needs projections</b> (usually CQRS).",
            "<b>Eventual consistency</b> between the log and the read models.",
            "<b>Deleting data</b> (e.g. GDPR) needs special techniques."],
    baseline="Each line compares a service that stores <b>current state with UPDATE</b> to the same service using <b>event sourcing</b> (with projections for reads).",
    ratings=[(4, 2, "Events, streams, projections, snapshots and versioning to master."),
             (4, 3, "More storage and more components (projections, event store)."),
             (4, 3, "Event schema changes need careful, backward-compatible releases."),
             (3, 4, "Given these events, when this command, then these events: very testable."),
             (3, 4, "Append-only writes and independent read models scale well."),
             (3, 3, "Neutral; projections can lag during spikes."),
             (3, 4, "Read models can be rebuilt; history is never lost."),
             (4, 3, "Writes are fast; reads depend on projections; long streams need snapshots."),
             (3, 4, "New questions about the past can be answered later.")],
    pitfalls=[("Using it everywhere", "Every CRUD table becomes event-sourced, and simple screens need projections and replays.", "use it only where history and audit really matter."),
              ("Events that are really commands or CRUD", "Events like <code>OrderUpdated</code> with the whole object say nothing about intent.", "small, past-tense, meaningful events (AddressChanged)."),
              ("Changing old events", "Someone edits stored events to fix a bug, and replays now disagree with what happened.", "never edit; add correcting events and use upcasters."),
              ("Querying the event store directly", "Screens scan millions of events to show a list.", "build projections (CQRS) for every query."),
              ("No snapshots on long streams", "An account with 2 million events takes seconds to load.", "snapshot every N events, or close and reopen streams per period.")],
    use=["Audit and history are core requirements (finance, healthcare, logistics).",
         "The business thinks in events (“booked”, “shipped”, “refunded”).",
         "You need to answer new questions about the past later.",
         "You already need events for integration and want one source of truth."],
    skip=["Simple CRUD with no history requirements.",
          "The team is new to it and the deadline is tight.",
          "Strong, immediate read-after-write consistency on every screen is a must.",
          "You'd need to delete data often and can't encrypt-and-forget."],
    related=["<b>CQRS</b> · its usual partner", "<b>Transactional outbox</b>", "<b>Saga</b>", "<b>Idempotent consumer</b> · projections must be", "<b>Snapshots</b>"],
    quiz=[("How do you fix a wrong event in an event-sourced system?", "You don't edit it. You append a new, correcting event, just as an accountant adds a correcting entry."),
          ("Why do event-sourced systems usually need CQRS?", "Replaying events is great for one aggregate but bad for queries across many, so separate read models (projections) are built for querying."),
          ("What problem do snapshots solve?", "Long streams are slow to replay; a snapshot stores the state at version N so you only replay events after it."),
          ("What does “expected version” protect against?", "Two writers changing the same aggregate at once; the second append fails because the stream version moved, so it reloads and retries.")],
    remember="State is just the <span class=\"hl\">sum of the story</span>. Keep the story, and you can always rebuild the state, or any new view of it.",
    sources=["Martin Fowler, “Event Sourcing” (martinfowler.com).",
             "Greg Young, “CQRS Documents” and talks on event sourcing.",
             "Microsoft Azure Architecture Center, “Event Sourcing pattern”.",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, “Event Sourcing”."],
)

# ------------------------------------------------------------------ 09 CQRS
cq_problem = Doodle(760, 260, "Doodle of one shared data model serving both writes and reads. Order writes need strict validation and normalised tables; the dashboard read needs a six-table join with sums and is slow, and the heavy reads lock rows that the writes need.",
                    "One model trying to be good at writing and at every kind of reading ends up good at neither.")
cq_problem.box(20, 40, 170, 60, "place order", "blue", size=19)
cq_problem.box(20, 160, 170, 60, "dashboard", "blue", size=19)
cq_problem.arrow(196, 70, 330, 110)
cq_problem.arrow(196, 190, 330, 150, color="red")
cq_problem.box(340, 60, 230, 140, "ONE model", "pink", sub="6 tables, many rules", stroke="red")
cq_problem.note(660, 70, "6-table JOIN", "red")
cq_problem.note(660, 100, "+ SUM + GROUP BY", "red")
cq_problem.note(660, 140, "3.2 s ✗", "red")
cq_problem.note(455, 240, "and heavy reads lock rows that writes need", "red")

cq_analogy = Doodle(760, 260, "Doodle of a restaurant. Orders are written on tickets and go to the kitchen, which has strict rules. Separately, the menu board on the wall is what customers read. The kitchen updates the menu board when a dish sells out, a little later.",
                    "The kitchen takes orders (writes); the menu board answers questions (reads). Different tools for different jobs.")
cq_analogy.icon("ticket", 30, 60, 1.4, fill="y")
cq_analogy.note(75, 170, "order tickets")
cq_analogy.arrow(120, 100, 230, 100, label="write", lx=175, ly=88)
cq_analogy.icon("kitchen", 240, 60, 2.0)
cq_analogy.note(310, 200, "kitchen: rules, stock")
cq_analogy.arrow(390, 100, 520, 100, dash=True, label="“fish sold out” (later)", lx=455, ly=86)
cq_analogy.icon("menu", 540, 30, 2.4)
cq_analogy.note(600, 220, "menu board: read by everyone")

cq_how = Doodle(760, 320, "CQRS flow. Commands go to a write model with business rules and a normalised write database. Changes are published as events. Projections update one or more read models, such as a denormalised dashboard table and a search index. Queries go straight to the read models.",
                "Writes and reads take different paths, joined by events. Read models are shaped for each screen.")
cq_how.box(20, 40, 150, 56, "commands", "blue")
cq_how.arrow(176, 68, 250, 68)
cq_how.box(256, 30, 190, 80, "write model", "y", sub="rules + validation")
cq_how.db(350, 140, "write DB (normalised)", w=90)
cq_how.arrow(452, 70, 560, 70, label="events", lx=506, ly=58)
cq_how.box(566, 40, 170, 60, "projections", "green")
cq_how.arrow(650, 104, 600, 190)
cq_how.arrow(680, 104, 700, 190)
cq_how.db(560, 200, "dashboard table", w=80, fill="green")
cq_how.db(700, 200, "search index", w=70, fill="green")
cq_how.box(20, 230, 150, 56, "queries", "blue")
cq_how.arrow(176, 258, 510, 225, label="read only, fast", lx=330, ly=268)

CQRS = dict(
    slug="cqrs",
    kicker="a.k.a. “writing and reading are different jobs”",
    tldr="<b>C</b>ommand <b>Q</b>uery <b>R</b>esponsibility <b>S</b>egregation: use <b>one model to change data</b> (commands, with all the business rules) and <b>separate models to read it</b> (queries), each shaped for the screens that use it. Read models are kept up to date from the write side, usually through events.",
    chips=[("Family", "data management"), ("Lives in", "inside one service (not across services)"), ("Coined by", "Greg Young, from Bertrand Meyer's CQS"), ("Pairs with", "event sourcing, outbox, materialised views")],
    problem='''  <p class="lead">One data model usually serves both writes and reads. As the system grows, those two jobs <span class="hl-pink">pull the model in opposite directions</span>.</p>
  <ul>
    <li><b>Writes</b> want normalised tables, strict validation, transactions and invariants (“stock can't go negative”).</li>
    <li><b>Reads</b> want data pre-joined, pre-summed and shaped for each screen: dashboards, search, mobile lists.</li>
    <li>Reads usually outnumber writes 10:1 or 100:1, but both are scaled together.</li>
    <li>Heavy report queries lock rows and slow down checkout.</li>
  </ul>''',
    problem_figs=[cq_problem],
    analogy_side="the restaurant kitchen and the menu board",
    analogy='''  <p>In a restaurant, <b>taking an order</b> and <b>answering “what's on today?”</b> are handled very differently.</p>
  <ul>
    <li>Orders go on tickets to the kitchen, where there are rules: check stock, cook in order, one chef per station. That's the <b>write side</b>.</li>
    <li>Customers read the <b>menu board</b>, which is written for reading: big, simple, no kitchen details. That's a <b>read model</b>.</li>
    <li>When the fish sells out, the kitchen updates the board a moment later. For a short while the board can be slightly out of date: <b>eventual consistency</b>.</li>
    <li>You can have several boards: one outside, one at the bar, one on the website. Several read models from the same kitchen.</li>
  </ul>''',
    analogy_figs=[cq_analogy],
    map=[("Order tickets to the kitchen", "Commands to the write model"),
         ("Kitchen rules and stock", "Business invariants, validation, transactions"),
         ("“Fish sold out” sent to the front", "Events from the write side"),
         ("The menu board", "A read model / materialised view"),
         ("Board updated a moment later", "Eventual consistency of read models"),
         ("Boards outside, at the bar, online", "Several read models for different screens")],
    how_side="two models, joined by events",
    how='  <p>Commands change state and return little or nothing. Queries return data and change nothing. In CQRS each side gets its <b>own model</b>, and often its own store.</p>',
    how_figs=[cq_how],
    steps=[("Split commands from queries", "<code>PlaceOrder</code>, <code>CancelOrder</code> go to the write model; <code>GetOrderSummary</code>, <code>SearchOrders</code> go to read models."),
           ("Keep the write model strict", "Normalised schema, invariants, transactions. It only needs what's required to make decisions."),
           ("Publish changes", "Every successful command emits events (via an outbox, or as the events themselves with event sourcing)."),
           ("Build read models per need", "Projections listen to events and update denormalised tables, caches or a search index, shaped exactly like the screen."),
           ("Handle the lag", "Tell users their action was accepted, show the optimistic result, or read your own write from the write side for that one screen.")],
    how_after='''  <div class="grid2">
    <div class="sticky sticky--green"><h3>Light CQRS</h3><p>Same database, separate code paths and maybe a few SQL views or materialised views for reads. Cheap and often enough.</p></div>
    <div class="sticky sticky--blue"><h3>Full CQRS</h3><p>Separate read stores (Elasticsearch, Redis, a reporting DB), updated from events. More power, more moving parts.</p></div>
  </div>''',
    vocab=[("Command", "A request to change state (“PlaceOrder”). May be rejected."),
           ("Query", "A request for data that changes nothing."),
           ("Write model", "The model that enforces business rules."),
           ("Read model", "A denormalised view optimised for one kind of query."),
           ("Projection", "Code that updates a read model from events."),
           ("Read-your-writes", "Seeing your own change straight after making it.")],
    code=dict(file="orders-cqrs.ts", note="write side + projection + query", src='''
// WRITE side: rules, then events
export async function placeOrder(cmd: { orderId: string; items: Item[] }) {
  if (cmd.items.length === 0) throw new Error("Empty order");
  await db.transaction(async (tx) => {
    await tx.insert("orders", { id: cmd.orderId, status: "PLACED" });
    await tx.insert("outbox", { type: "OrderPlaced", payload: cmd });
  });
}

// PROJECTION: keeps a read model shaped for the dashboard
bus.on("OrderPlaced", async (e) => {
  await readDb.upsert("dashboard_orders", {
    id: e.orderId, item_count: e.items.length,
    total: sum(e.items.map((i) => i.price)), placed_at: e.at,
  });
});

// READ side: no joins, no rules, just fast
export const recentOrders = () =>
  readDb.query("SELECT * FROM dashboard_orders ORDER BY placed_at DESC LIMIT 20");
'''),
    tools="building blocks: MediatR (.NET) for command/query handlers, Axon (Java), Marten projections, Postgres materialised views, Debezium → Elasticsearch, Redis as a read cache.",
    gains=["<b>Fast reads</b> shaped for each screen, no expensive joins.",
           "<b>Scale reads and writes separately</b>; reads are usually the bigger side.",
           "<b>Simpler write model</b> focused only on rules.",
           "<b>Many views from one source</b>: dashboards, search, reports.",
           "<b>Less contention</b>: reports no longer lock rows checkout needs."],
    losses=["<b>Eventual consistency.</b> Read models lag behind writes.",
            "<b>More code and infrastructure</b>: projections, read stores, events.",
            "<b>Duplicated data</b> in several shapes.",
            "<b>Rebuilding read models</b> needs tooling and time.",
            "<b>Overkill</b> for simple CRUD screens."],
    baseline="Each line compares a service with <b>one shared model for reads and writes</b> to the same service with <b>separate write and read models</b> kept in sync by events.",
    ratings=[(4, 2, "Two models, events and projections to understand."),
             (4, 3, "Extra stores and projection workers to run."),
             (4, 3, "Read models and event contracts must be released carefully."),
             (3, 4, "Write rules and projections can each be tested in isolation."),
             (2, 5, "Read stores scale out independently of writes."),
             (3, 4, "Read replicas and caches absorb traffic spikes."),
             (3, 4, "Read side can serve while the write side is degraded (and vice versa)."),
             (2, 4, "Queries hit pre-shaped data; writes stay lean."),
             (3, 4, "New screens get new read models without touching the write side.")],
    pitfalls=[("CQRS for every service", "A settings page with 3 fields gets commands, events, projections and two databases.", "use it where reads and writes truly differ; plain CRUD elsewhere."),
              ("Ignoring the lag in the UI", "User saves, the list reloads from the read model and the item “isn't there”. They click save again.", "optimistic UI, read-your-writes for that view, or show “processing”."),
              ("Projections that aren't idempotent", "A replay or duplicate event doubles the totals on the dashboard.", "idempotent projections (upsert by id, track last event position)."),
              ("Querying the write model for screens", "Shortcuts creep in and the write DB serves reports again.", "keep queries on read models; guard the boundary in code review."),
              ("No way to rebuild", "A projection bug corrupts the read model and there's no replay.", "keep the events (or outbox history) and a rebuild command.")],
    use=["Reads and writes have very different shapes or volumes.",
         "Complex domains with rich rules on the write side.",
         "Many different views of the same data (dashboards, search, mobile).",
         "You already use event sourcing."],
    skip=["Simple CRUD where the form and the table look the same.",
          "Users must always see their changes instantly everywhere.",
          "A small team that can't run the extra infrastructure.",
          "A read replica or a cache would solve the performance problem."],
    related=["<b>Event sourcing</b>", "<b>Transactional outbox</b>", "<b>Cache-aside</b>", "<b>Leader–follower replication</b> · read replicas", "<b>Materialised view</b>"],
    quiz=[("What's the difference between a command and a query?", "A command asks to change state and can be rejected; a query only returns data and never changes anything."),
          ("Why are read models eventually consistent?", "They're updated asynchronously from events after the write commits, so there's a short delay."),
          ("Does CQRS require event sourcing?", "No. They're often combined, but CQRS works with a normal database plus an outbox or even SQL views."),
          ("A user saves a change but the list doesn't show it yet. Two ways to fix the experience?", "Optimistically show the change in the UI, or read that one item from the write side (read-your-writes), or show a “processing” state.")],
    remember="Write with <span class=\"hl\">rules</span>, read with <span class=\"hl\">speed</span>. Two models, one source of truth, a short delay in between.",
    sources=["Martin Fowler, “CQRS” (martinfowler.com/bliki/CQRS.html).",
             "Greg Young, “CQRS Documents”.",
             "Microsoft Azure Architecture Center, “CQRS pattern” and “Materialized View pattern”.",
             "Microsoft, <i>.NET Microservices: Architecture for Containerized .NET Applications</i>, CQRS chapter."],
)

NOTES = [OUTBOX, IDEMP, ES, CQRS]
