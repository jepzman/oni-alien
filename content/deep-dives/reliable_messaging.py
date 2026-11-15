# Deep dive 02 · Reliable Messaging. Builds on Vol. 1 notes 06 (outbox), 07 (idempotent consumer), 11 (pub-sub),
# 12 (competing consumers) and Vol. 3 change data capture. Example: order 42 (two mugs, $49) and its OrderPlaced event,
# consumed by Shipping (creates a shipment), Email (sends a confirmation) and Loyalty (adds 49 points).
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
path_svg = '''
  <rect class="bx" x="10" y="50" width="170" height="110" rx="8"/><text class="lbl" x="95" y="74" text-anchor="middle">Order service</text>
  <rect class="bx-y" x="24" y="88" width="66" height="56" rx="6"/><text x="57" y="121" text-anchor="middle">orders</text>
  <rect class="bx-y" x="100" y="88" width="66" height="56" rx="6"/><text x="133" y="121" text-anchor="middle">outbox</text>
  <rect class="bx" x="220" y="80" width="80" height="50" rx="8"/><text class="lbl" x="260" y="111" text-anchor="middle">relay</text>
  <rect class="bx" x="340" y="70" width="110" height="70" rx="8"/><text class="lbl" x="395" y="100" text-anchor="middle">broker</text><text class="soft" x="395" y="122" text-anchor="middle">topic: orders</text>
  <rect class="bx" x="500" y="50" width="250" height="110" rx="8"/><text class="lbl" x="625" y="74" text-anchor="middle">Shipping service</text>
  <rect class="bx-y" x="514" y="88" width="100" height="56" rx="6"/><text x="564" y="121" text-anchor="middle">processed ids</text>
  <rect class="bx-y" x="624" y="88" width="112" height="56" rx="6"/><text x="680" y="121" text-anchor="middle">shipments</text>
  <path class="ln" d="M180 105 H218" marker-end="url(#a)"/><path class="ln" d="M300 105 H338" marker-end="url(#a)"/><path class="ln" d="M450 105 H498" marker-end="url(#a)"/>
  <path class="ln-d" d="M498 150 Q474 190 430 142" marker-end="url(#a)"/><text class="soft" x="470" y="200" text-anchor="middle">ack</text>
  <circle class="bx-r" cx="95" cy="30" r="13"/><text class="lbl bad" x="95" y="36" text-anchor="middle">1</text>
  <circle class="bx-r" cx="260" cy="56" r="13"/><text class="lbl bad" x="260" y="62" text-anchor="middle">2</text>
  <circle class="bx-r" cx="395" cy="46" r="13"/><text class="lbl bad" x="395" y="52" text-anchor="middle">3</text>
  <circle class="bx-r" cx="625" cy="30" r="13"/><text class="lbl bad" x="625" y="36" text-anchor="middle">4</text>
  <circle class="bx-r" cx="440" cy="186" r="13"/><text class="lbl bad" x="440" y="192" text-anchor="middle">5</text>
  <text class="soft" x="95" y="186" text-anchor="middle">one transaction</text><text class="soft" x="625" y="186" text-anchor="middle">one transaction</text>
'''
recap = '''
<p>Order 42 is placed: two mugs, $49. The Order service saves it and announces <code>OrderPlaced</code>. Three services care. Shipping creates a shipment, Email sends a confirmation, Loyalty adds 49 points. Three notes described the parts.</p>
''' + tbl(["Note", "In one line"], [
    ["Transactional Outbox", "save the order and the event in one transaction; a relay publishes the event later"],
    ["Publish–Subscribe, Competing Consumers", "one event, a copy for every subscriber; several workers share each subscriber's load"],
    ["Idempotent Consumer", "remember the ids you have handled, so a repeat does nothing"],
]) + fig(760, 215, "The path of one event. Inside the Order service, the orders table and the outbox table are written in one transaction. A relay reads the outbox and publishes to the broker's orders topic. The Shipping service receives the event, writes its processed-ids table and its shipments table in one transaction, then sends an ack back to the broker. Five numbered points mark where things go wrong: the order transaction, the relay, the broker, the consumer and the ack.",
          path_svg, "One event, five hops. Each numbered point can lose a message, repeat it or reorder it.") + mn("Each note fixed one hop. Nobody showed me the whole trip.") + '''
<p class="full">The notes are each correct. The trouble is in the joins. The relay can publish twice. The broker can deliver twice, or in a different order. The consumer can crash after the work and before the ack. This deep dive follows the event across all five points and makes the whole path reliable, which is a different job from making each part reliable.</p>
'''

# ------------------------------------------------------------------ 2 guarantees
guarantees = '''
<p>Vendors and documentation use three phrases. Two of them describe what a hop can do. The third describes a result that you build.</p>
''' + tbl(["Phrase", "Meaning", "What you see when things fail"], [
    ["<b>At most once</b>", "send it and don't check", "lost messages, never duplicates"],
    ["<b>At least once</b>", "resend until someone confirms", "duplicates, never losses"],
    ["<b>Exactly once</b>", "the <i>effect</i> happens once", "nothing, if you did the work in this deep dive"],
]) + '''
<h3>Why delivery can't be exactly once</h3>
<p>The relay sends <code>OrderPlaced</code> to the broker and waits for a confirmation. None arrives. There are two possible worlds: the message was lost on the way there, or the confirmation was lost on the way back. From the relay's chair they look identical. It has two choices.</p>
<ul>
  <li><b>Don't resend.</b> In the first world the event is gone. That is at most once.</li>
  <li><b>Resend.</b> In the second world the broker now has two copies. That is at least once.</li>
</ul>
<p>There is no third choice, and adding confirmations of confirmations only moves the doubt one step along. Every hop in the figure faces the same fork.</p>
''' + mn("So “exactly once” on a product page always means: at least once, plus someone throwing away the repeats.") + '''
<h3>The ack decides which one you get</h3>
<p>For a consumer, the choice is made by one line of code: where the ack goes.</p>
''' + tbl(["Order of events", "Crash in the middle means", "Guarantee"], [
    ["ack, then do the work", "the broker thinks it's done; the work never happened", "at most once"],
    ["do the work, then ack", "the work happened; the broker sends the message again", "at least once"],
], hot=(1,)) + full('''<p>Losing an order event is almost always worse than seeing it twice, so nearly every business system picks the second row. That choice has a price: <mark>duplicates are now a normal event, and every consumer must make them harmless</mark>. The rest of this deep dive is about paying that price properly.</p>
<p>A useful way to say it: delivery is at least once, <b>processing</b> is effectively once. The first is the transport's job. The second is yours.</p>''')

# ------------------------------------------------------------------ 3 outbox for real
outbox = '''
<p>The note said “write the event to an outbox table, and a relay publishes it”. Here is what that table and that relay look like when you have to build them.</p>
''' + code("place-order.sql", "one transaction, two inserts", '''
BEGIN;
INSERT INTO orders (id, customer_id, total, status)
VALUES (42, 7, 49.00, 'PLACED');

INSERT INTO outbox (event_id, key, type, payload)
VALUES ('e-9f31', 'order-42', 'OrderPlaced',
        '{"orderId": 42, "total": 49.00, "version": 1}');
COMMIT;
''') + tbl(["Column", "Why it is there"], [
    ["<code>id</code>", "an increasing number, so the relay can read in order"],
    ["<code>event_id</code>", "the event's identity for its whole life; consumers dedupe on it (chapter 6)"],
    ["<code>key</code>", "what must stay in order together: here, everything about order 42 (chapter 5)"],
    ["<code>type</code>, <code>payload</code>", "what happened, as the consumers will read it"],
    ["<code>sent_at</code>", "empty until the relay has published the row"],
]) + mn("The event id is created here, once, by the producer. Not by the relay, not by the broker.") + '''
<h3>The relay, as a poller</h3>
''' + code("relay.sql", "every 200 ms", '''
BEGIN;
SELECT id, event_id, key, type, payload
FROM outbox
WHERE sent_at IS NULL
ORDER BY id
LIMIT 100
FOR UPDATE SKIP LOCKED;

-- publish each row to the broker and wait for its confirmation

UPDATE outbox SET sent_at = now() WHERE id IN (101, 102, 103);
COMMIT;
''') + '''
<p>Publish first, mark second. If the relay crashes between the two, the rows are still unsent and go out again. So the relay is an at-least-once sender, by design.</p>
''' + full('''<h3>The trap: “give me everything after id 102”</h3>
<p>A tempting optimisation is to remember the highest id published and ask only for newer rows. It is faster than scanning for empty <code>sent_at</code>. It also loses events, because ids are handed out when a row is inserted and rows become visible when their transaction commits. Those are different moments.</p>
''' + tbl(["Time", "What happens", "Relay's high-water mark"], [
    ["10:00:00.000", "transaction A inserts outbox row <b>101</b>, keeps working", "100"],
    ["10:00:00.010", "transaction B inserts row <b>102</b> and commits", "100"],
    ["10:00:00.200", "relay asks for id &gt; 100, sees only 102, publishes it", "102"],
    ["10:00:00.300", "transaction A commits; row 101 becomes visible", "102"],
    ["10:00:00.400", "relay asks for id &gt; 102. Row 101 is never read", "102"],
], hot=(4,), mono=(0,)) + '''<p>An event silently missing is the exact failure the outbox was meant to prevent. Selecting on <code>sent_at IS NULL</code> does not have this hole: row 101 is picked up on the next round, a little late and after 102. Late is acceptable here because the two rows belong to different orders.</p>
<h3>Polling or reading the log</h3>
<p>The other way to build the relay is change data capture: a connector reads the database's own transaction log and publishes each committed outbox insert.</p>
''' + tbl(["", "Poller", "Log reader (CDC)"], [
    ["Order of events", "by id, with late commits arriving late", "exact commit order"],
    ["Delay", "the polling interval", "milliseconds"],
    ["Load on the database", "a query every interval, even when idle", "almost none"],
    ["What you run", "a small loop in your service", "a connector, its offsets and its monitoring"],
    ["Still at least once?", "yes", "yes: the connector can re-read after a restart"],
]) + '''<p>Start with the poller. Move to the log reader when the polling delay or the query load starts to hurt, or when you already run CDC for other reasons.</p>
<h3>Two housekeeping rules</h3>
<ul>
  <li><b>One relay per key at a time.</b> Two relays running side by side each take a batch and publish at their own speed, so events for the same order can overtake each other. Run one active relay, or split the outbox by key so each relay owns its slice.</li>
  <li><b>Delete what you sent.</b> An outbox that only grows makes every poll slower. A nightly job removes rows sent more than a few days ago. Keep those few days: they are your evidence when someone asks “did we publish it?”</li>
</ul>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Same exercise as in the Saga dive: guess what happens next before you read on.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · relay crash</a></li><li><a href="#drill-2">2 · consumer crash</a></li><li><a href="#drill-3">3 · poison message</a></li>
  <li><a href="#drill-4">4 · wrong order</a></li><li><a href="#drill-5">5 · slow worker</a></li><li><a href="#drill-6">6 · forgotten id</a></li>
</ul>
''' + drill(1, "The relay publishes, then dies", [
    ("Timeline", "The relay publishes <code>OrderPlaced e-9f31</code>. The broker confirms. The relay crashes before it sets <code>sent_at</code>."),
    ("What you see", "After the restart the row still looks unsent, so it is published again. Shipping, Email and Loyalty each receive the event twice, a few seconds apart.", True),
    ("What saves you", "Nothing at the relay: this is the fork from chapter 2, and resending is the right branch. The second copy carries the same <code>event_id</code>, and each consumer recognises it."),
], "the relay will repeat itself. Give every event one id at birth, and never change it on a resend.") + drill(2, "The consumer does the work, then dies", [
    ("Timeline", "Loyalty receives the event and adds 49 points. It crashes before the ack. The broker delivers the event to another Loyalty worker, which adds 49 more."),
    ("The tempting mistake", "Keep a list of handled ids in a cache: check the list, do the work, add the id. A crash between “do the work” and “add the id” leaves the same hole. Adding the id first moves the hole: now a crash loses the points."),
    ("Why", "The work and the memory of the work are two writes. If they can be separated by a crash, one of them will be missing sooner or later. It is the outbox problem again, on the receiving side.", True),
    ("What saves you", "Put the id and the work in <b>one transaction</b> in the consumer's own database: insert the id into a <code>processed_events</code> table, add the points, commit, then ack. A repeat fails on the insert and skips the work."),
], "the record that you handled a message lives in the same transaction as the handling.") + drill(3, "A message that can never succeed", [
    ("Timeline", "An <code>OrderPlaced</code> arrives with a postcode that Shipping's parser rejects. Shipping throws, the broker redelivers, Shipping throws again."),
    ("What you see", "One of two pictures. On a queue, the bad message cycles for ever and burns CPU. On an ordered log, it is worse: the worker cannot move past it, so every later order on that partition waits. One bad postcode has stopped shipping.", True),
    ("What saves you", "Count the attempts. Errors that might pass later (a timeout, a lock) get a few retries with growing waits. Errors that will never pass (a parse failure, a broken rule), and anything still failing after the limit, go to a <b>dead-letter queue</b> with the reason attached. The worker acks and moves on. Chapter 7 covers what happens to the letter after that."),
], "every message leaves the main flow in bounded time: done, or set aside where a person will see it.") + drill(4, "The cancel arrives before the order", [
    ("Timeline", "The customer places order 42 and cancels it two seconds later. Shipping sees <code>OrderCancelled</code> first. It finds no shipment to cancel and ignores the event. Then <code>OrderPlaced</code> arrives and a shipment is created for a cancelled order."),
    ("Why", "Several things reorder messages: two relays, two workers on one queue, or a retry that sends the first event to the back of the line. Any one is enough.", True),
    ("What saves you", "Two layers. First, keep related events in line: publish with <code>key = order-42</code> so they share a partition and a single worker. Second, make the consumer able to tell: each event carries the order's <b>version</b> (1, 2, 3…), and the consumer stores the last version it applied. An event with an older version is ignored. An event that skips a version is parked until the gap is filled."),
], "ask for order by key, and carry a version anyway, because order is the first thing a failure takes away.") + drill(5, "The worker is slow, so the broker gives up on it", [
    ("Timeline", "Email takes 40 seconds to send during a provider slowdown. The broker waits 30 seconds for an ack, decides the worker is dead and hands the event to a second worker. Both send the confirmation."),
    ("What you see", "Duplicates that appear only on slow days, which makes them hard to reproduce. The usual “check the id, then work” does not help: both workers checked while neither had finished.", True),
    ("What saves you", "Three things together. Set the broker's wait well above the slowest normal processing time. Have long jobs tell the broker they are still alive. And <b>claim before working</b>: insert the id first, under a unique constraint, so the second worker's insert fails at once."),
], "two workers can hold the same message at the same moment. Only a unique constraint settles who owns it.") + drill(6, "The duplicate that arrives after you forgot", [
    ("Timeline", "Loyalty deletes processed ids after 7 days to keep the table small. On day 9 an operator replays last week's events to repair a different service. Loyalty no longer knows the ids and adds every customer's points again."),
    ("Why", "Deduplication has a memory, and the memory has a length. A duplicate older than that length is treated as new.", True),
    ("What saves you", "Keep ids for longer than a message can possibly come back: the broker's retention period plus your replay window. Better still, where the operation allows it, do not rely on memory at all. “Points for order 42 = 49”, stored once per order, stays correct however late the repeat arrives."),
], "know how long your dedupe memory is, and make sure nothing can be redelivered from further back.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Part", "Its duty", "Drill"], [
    ["Producer", "one id per event, a key, a version", "1, 4"],
    ["Relay", "publish then mark; one active relay per key", "1, 4"],
    ["Consumer", "claim the id and do the work in one transaction, then ack", "2, 5"],
    ["Consumer", "bounded retries, then the dead-letter queue", "3"],
    ["Consumer", "ignore old versions, park early ones", "4"],
    ["Operations", "dedupe memory longer than any redelivery", "6"],
]))

# ------------------------------------------------------------------ 5 ordering
order_svg = '''
  <text class="lbl" x="20" y="28">topic: orders</text>
  <text class="soft" x="20" y="72">partition 0</text><text class="soft" x="20" y="132">partition 1</text><text class="soft" x="20" y="192">partition 2</text>
  <rect class="bx" x="110" y="48" width="400" height="40" rx="6"/><rect class="bx" x="110" y="108" width="400" height="40" rx="6"/><rect class="bx" x="110" y="168" width="400" height="40" rx="6"/>
  <rect class="bx-y" x="120" y="54" width="110" height="28" rx="4"/><text x="175" y="74" text-anchor="middle">42 · placed</text>
  <rect class="bx-y" x="240" y="54" width="110" height="28" rx="4"/><text x="295" y="74" text-anchor="middle">42 · paid</text>
  <rect class="bx-y" x="360" y="54" width="130" height="28" rx="4"/><text x="425" y="74" text-anchor="middle">42 · cancelled</text>
  <rect class="bx-g" x="120" y="114" width="110" height="28" rx="4"/><text x="175" y="134" text-anchor="middle">43 · placed</text>
  <rect class="bx-g" x="240" y="114" width="110" height="28" rx="4"/><text x="295" y="134" text-anchor="middle">43 · paid</text>
  <rect class="bx-r" x="120" y="174" width="110" height="28" rx="4"/><text x="175" y="194" text-anchor="middle">44 · placed</text>
  <path class="ln" d="M510 68 H588" marker-end="url(#a)"/><path class="ln" d="M510 128 H588" marker-end="url(#a)"/><path class="ln" d="M510 188 H588" marker-end="url(#a)"/>
  <rect class="bx" x="590" y="48" width="150" height="40" rx="8"/><text x="665" y="74" text-anchor="middle">shipping worker A</text>
  <rect class="bx" x="590" y="108" width="150" height="40" rx="8"/><text x="665" y="134" text-anchor="middle">shipping worker B</text>
  <rect class="bx" x="590" y="168" width="150" height="40" rx="8"/><text x="665" y="194" text-anchor="middle">shipping worker C</text>
  <text class="soft" x="310" y="236" text-anchor="middle">key = order id → same order, same partition, same worker</text>
'''
ordering = '''
<p>“Events arrive in order” can mean two things, and only one of them is affordable.</p>
''' + tbl(["Kind of order", "Meaning", "Cost"], [
    ["<b>Total order</b>", "every event in the system, one after another", "one line, one worker: no parallel work at all"],
    ["<b>Order per key</b>", "events about the same thing stay in sequence; different things are independent", "parallel across keys"],
], hot=(1,)) + '''
<p>Nobody needs order 43's payment to wait for order 42's cancellation. What matters is that order 42's own events are seen as placed, paid, cancelled. So choose a key, and ask for order within it.</p>
''' + fig(760, 250, "A topic with three partitions. Partition 0 holds three events for order 42: placed, paid, cancelled. Partition 1 holds two events for order 43. Partition 2 holds one event for order 44. Each partition is read by exactly one shipping worker, A, B and C.",
          order_svg, "The broker hashes the key to pick a partition. Within a partition there is one reader, so there is one order.") + mn("Choosing the key is a design decision. Order id? Customer id? It decides what can run in parallel.") + '''
<h3>How order gets lost anyway</h3>
''' + tbl(["Cause", "What happens"], [
    ["Several workers on one plain queue", "the note's competing consumers: fast, and no order at all"],
    ["A retry", "event 2 fails and is retried later; event 3 has already gone through"],
    ["The number of partitions changes", "the same key now hashes to a different partition; old and new events are read by different workers"],
    ["Two relays", "from chapter 3: each publishes its batch at its own pace"],
]) + full('''<h3>The retry dilemma</h3>
<p>The second row deserves a decision, because you cannot have everything. When event 2 for order 42 fails:</p>
''' + tbl(["Choice", "You keep", "You pay"], [
    ["<b>Block</b>: retry in place until it passes", "order", "everything behind it on that partition waits. One bad event stalls many orders (drill 3)"],
    ["<b>Step aside</b>: move it to a retry queue, carry on", "flow", "event 3 is processed before event 2"],
    ["<b>Step aside per key</b>: park event 2 <i>and</i> later events for order 42 only", "both, for every other order", "the consumer must remember which keys are parked"],
]) + '''<p>Most teams start with “step aside” and make the consumer safe against the reordering. The third option is the best behaviour and the most code.</p>
<h3>Design events so that order matters less</h3>
<p>The cheapest defence is in the event itself.</p>
''' + tbl(["Event style", "Example", "If it arrives late or twice"], [
    ["<b>Delta</b>", "“add 49 points”", "wrong total. Needs dedupe and order"],
    ["<b>Fact with identity</b>", "“order 42 earned 49 points”", "safe to repeat: one row per order"],
    ["<b>State with version</b>", "“order 42 is CANCELLED, version 3”", "safe to repeat and to reorder: keep the highest version"],
], hot=(2,)) + '''<p>An event that carries the current state and a version lets the consumer apply a simple rule: <i>if this version is higher than mine, take it; otherwise ignore it</i>. Late and duplicate events both fall out for free. The cost is a larger event, and consumers that only learn the latest state, not each step in between.</p>''')

# ------------------------------------------------------------------ 6 idempotent consumer
consumer = '''
<p>The note gave the idea: remember ids. In practice there are three techniques, and a consumer usually needs to pick one per kind of work.</p>
''' + tbl(["Technique", "How", "Fits"], [
    ["<b>Natural</b>", "the operation gives the same result when repeated: set a status, upsert a row keyed by order", "state changes, “one row per order” facts"],
    ["<b>Dedupe table</b>", "insert the event id under a unique constraint, in the same transaction as the work", "anything that changes your own database"],
    ["<b>Version check</b>", "apply only if the event's version is newer than the stored one", "keeping a copy of someone else's state"],
]) + code("handle-order-placed.sql", "Loyalty: claim, work, commit, then ack", '''
BEGIN;
INSERT INTO processed_events (consumer, event_id)
VALUES ('loyalty', 'e-9f31')
ON CONFLICT DO NOTHING;
-- 0 rows inserted? It is a repeat: COMMIT, ack, stop.

UPDATE loyalty_accounts
SET points = points + 49
WHERE customer_id = 7;
COMMIT;
-- only now: ack the message
''') + mn("Three consumers, three dedupe tables. Shipping having seen e-9f31 says nothing about Loyalty.") + '''
<h3>Which id?</h3>
''' + tbl(["Candidate", "Verdict"], [
    ["The <code>event_id</code> the producer wrote into the outbox", "yes. It is the same on every resend, from every hop"],
    ["The broker's message id or offset", "no. A resend by the relay is a new broker message with a new id"],
    ["A hash of the payload", "no. Two real orders for the same mugs at the same price look like one"],
]) + full('''<h3>When the work is outside your database</h3>
<p>Email cannot put “send the confirmation” inside a database transaction. The claim and the work are separated again, and a crash can fall between them. There are three ways out, in order of preference.</p>
<ol>
  <li><b>Pass the id on.</b> If the email provider or payment API accepts an idempotency key, send the <code>event_id</code> with the call. Now a repeat is the provider's duplicate to drop.</li>
  <li><b>Use your own outbox.</b> In one transaction, claim the event id and write “email to send” to an outbox of your own. A relay performs the send. You have turned an external side effect into the problem already solved in chapter 3.</li>
  <li><b>Accept the rare repeat, on purpose.</b> For a confirmation email, two copies once in a great while may be an acceptable cost. For a payment it is not. Write the decision down so it is a choice and not an accident.</li>
</ol>
<h3>Keeping a copy of someone else's state</h3>
<p>Shipping keeps a small table of orders so it does not have to call the Order service. The version check keeps that copy correct whatever the arrival order.</p>
''' + code("apply-order-event.sql", "duplicates and stale events change nothing", '''
INSERT INTO order_copy (order_id, status, version)
VALUES (42, 'CANCELLED', 3)
ON CONFLICT (order_id) DO UPDATE
SET status = EXCLUDED.status, version = EXCLUDED.version
WHERE order_copy.version < EXCLUDED.version;
''') + '''<p>No dedupe table is needed for this handler. A repeat has an equal version and a late event has a lower one, and both leave the row alone.</p>''')

# ------------------------------------------------------------------ 7 dead letters and replay
dead = '''
<p>Drill 3 ended with the bad message in a dead-letter queue. That is where many teams stop, and where the message stays until someone finds four thousand of them a year later.</p>
<h3>Retry in tiers</h3>
''' + tbl(["Tier", "Wait", "For"], [
    ["1 · at once", "none, up to 3 times", "a lock, a dropped connection"],
    ["2 · delayed", "10 s, 1 min, 10 min", "a dependency that is down or slow"],
    ["3 · dead letter", "until a person acts", "errors that will not pass, and anything that used up tiers 1 and 2"],
]) + '''
<p>The delayed tier matters most. A consumer that retries at once, for ever, against a database that is restarting turns one problem into two. The waits use the same growing, randomised delays as the Retry note.</p>
<p>Classify the error before choosing a tier. A timeout may pass later. “Unknown postcode format” will not, so it skips straight to tier 3.</p>
<h3>A dead-letter queue is a process</h3>
''' + tbl(["Step", "What it needs"], [
    ["Notice", "an alert when the queue is not empty; the count on a dashboard"],
    ["Understand", "each letter keeps the original event, the error text, the attempt count and the time"],
    ["Fix", "deploy the handler fix, or correct the data at its source"],
    ["Redrive", "a button or script that sends the letters back to the main queue"],
    ["Close", "the queue returns to zero; someone writes down the cause"],
]) + mn("If nobody owns the dead-letter queue, it is a slower way of losing messages.") + full('''<p>Redriving is safe only because consumers are idempotent. Some of those letters may have been partly handled before they failed, and some may be sent back twice by an impatient operator.</p>
<h3>Replay</h3>
<p>A broker that keeps its events lets you read them again from an earlier point. That is useful in three situations.</p>
''' + tbl(["Situation", "Replay"], [
    ["A new service needs history", "Loyalty launches in March and reads every order since January to compute starting balances"],
    ["A bug damaged data", "Shipping mis-read weights for two days; fix the code, replay those two days"],
    ["A copy was lost", "rebuild a search index or a read model from the first event"],
]) + '''<p>Replay is powerful and it is where drills 4 and 6 meet. Before you allow it, check three things.</p>
<ul>
  <li><b>Handlers are idempotent beyond the dedupe window.</b> Replayed events are old. Natural idempotency and version checks survive that; a seven-day id table does not (drill 6).</li>
  <li><b>Side effects are guarded.</b> Replaying January must not email ten thousand customers “your order is confirmed”. Handlers that talk to the outside world either check a replay flag on the consumer or skip events older than a cut-off time.</li>
  <li><b>The events still exist.</b> Retention is a decision. Seven days of history supports bug repair. Rebuilding from the first event needs the topic kept for good, or a snapshot plus recent events.</li>
</ul>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>A messaging path fails quietly. Nothing throws; events just arrive later and later. Four numbers make that visible.</p>
''' + tbl(["Metric", "Where", "Healthy", "It means trouble when"], [
    ["<b>Outbox age</b>: age of the oldest unsent row", "producer", "under a second", "it climbs: the relay is down or the broker refuses"],
    ["<b>Consumer lag</b>: events published but not yet handled, and the age of the oldest", "each consumer", "seconds", "it climbs steadily: the consumer is too slow or stuck on one message"],
    ["<b>Redelivery rate</b>: share of deliveries that are repeats", "each consumer", "well under 1 %", "it jumps: timeouts are too short, or a worker keeps crashing"],
    ["<b>Dead letters</b>: count waiting", "each consumer", "zero", "above zero"],
]) + mn("Measure lag in time, not only in messages. “4,000 behind” means little. “Shipping is 6 minutes behind” means a lot.") + '''
<h3>Follow one event</h3>
<p>Every log line carries the <code>event_id</code>, and the event carries the id of whatever caused it. One search then shows the whole trip:</p>
''' + tbl(["time", "service", "message"], [
    ["10:00:00.120", "order", "event=e-9f31 OrderPlaced written to outbox, order=42 v1"],
    ["10:00:00.310", "relay", "event=e-9f31 published to orders, partition 0"],
    ["10:00:00.340", "shipping", "event=e-9f31 handled, shipment created"],
    ["10:00:00.900", "relay", "event=e-9f31 published to orders, partition 0"],
    ["10:00:00.930", "shipping", "event=e-9f31 duplicate, skipped"],
], hot=(3, 4), mono=(0,)) + '''
<p>That is drill 1 seen from outside: the relay restarted and published again, and the consumer shrugged.</p>
''' + full('''<h3>Numbers worth working out once</h3>
<p>The shop takes 50 orders a second at peak, and each order produces about 3 events.</p>
''' + tbl(["Setting", "Reasoning", "Value"], [
    ["Relay capacity", "a batch of 100 every 200 ms is 500 events a second; the peak is 150", "about 3× headroom"],
    ["Broker's wait for an ack", "Shipping's slowest normal handling is 4 s; allow several times that", "30 s"],
    ["Worker count for Shipping", "one event takes 40 ms, so one worker does 25 a second; the peak needs 50 a second", "3 workers, 6 partitions so there is room to grow"],
    ["Dedupe memory", "the broker keeps events 7 days; replays are allowed for the last 7", "keep ids 14 days, plus a margin"],
    ["Outbox clean-up", "long enough to answer “was it published?”", "3 days"],
]) + '''<h3>When the consumer cannot keep up</h3>
<p>Lag that grows during a peak and shrinks afterwards is the queue doing its job. Lag that only grows needs action, in this order: find out whether one message is blocking the line (drill 3); add workers, up to the number of partitions; make the handler cheaper, often by batching its database writes; and only then add partitions, remembering from chapter 5 that this reshuffles keys.</p>
<h3>Runbook: “the customer never got a shipment”</h3>
<ol>
  <li>Find the order's row in the outbox. Missing? The bug is in the producer's transaction. Unsent? Look at the relay.</li>
  <li>Sent? Search the logs for the <code>event_id</code> on the consumer side.</li>
  <li>No trace there? Check the consumer's lag: the event may simply not have been reached yet.</li>
  <li>A trace ending in an error? Look in the dead-letter queue, fix, redrive.</li>
  <li>Marked handled but no shipment? The handler claimed the id and then lost the work, which means the two were not in one transaction (drill 2).</li>
</ol>''')

# ------------------------------------------------------------------ 9 testing and contracts
testing = '''
<p>Most messaging bugs need a crash or a repeat at an exact moment, which never happens on a developer's laptop. So the tests have to cause those moments on purpose.</p>
''' + tbl(["Test", "How", "Catches"], [
    ["<b>Deliver everything twice</b>", "a test broker hands each message to the handler two times", "any handler that is not idempotent (drills 1, 2)"],
    ["<b>Shuffle within a key</b>", "deliver order 42's events in every possible sequence", "handlers that assume order (drill 4)"],
    ["<b>Crash the relay</b>", "stop it after publish, before the mark; restart", "events lost or stuck (chapter 3)"],
    ["<b>Crash the consumer</b>", "stop it after commit, before the ack; redeliver", "work done twice (drill 2)"],
    ["<b>Two workers, one message</b>", "start the same message on two workers at once", "check-then-work races (drill 5)"],
    ["<b>Poison</b>", "send a message that always fails", "missing retry limit or dead-letter route (drill 3)"],
]) + code("loyalty.test.ts", "the cheapest, most valuable test", '''
test("every event twice gives the same balance as once", async () => {
  const events = [orderPlaced(42, 49), orderPlaced(43, 20), orderCancelled(43)];

  const once = await run(events);
  const twice = await run(events.flatMap((e) => [e, e]));

  expect(twice.balanceOf(7)).toBe(once.balanceOf(7));
});
''') + mn("Run the whole consumer test suite in “everything twice” mode. If it still passes, the consumer is idempotent.") + full('''<h3>Events are contracts</h3>
<p>The producer cannot see its consumers, which was the point of publish–subscribe. It also means the producer cannot see whom it breaks. Rename <code>total</code> to <code>amount</code> and Loyalty starts awarding zero points, with no error anywhere. An event's shape is a public interface and needs the same care as an API.</p>
''' + tbl(["Change", "Safe?", "Why"], [
    ["Add an optional field", "yes", "old consumers ignore it"],
    ["Add a new event type", "yes", "consumers that don't know the type must skip it, not crash"],
    ["Remove or rename a field", "no", "consumers reading it get nothing"],
    ["Change a field's meaning or unit", "no", "the worst kind: nothing fails, the numbers are just wrong"],
    ["Make an optional field required", "no", "old events in the topic, and replays, do not have it"],
], hot=(2, 3, 4)) + '''<p>Two habits keep this manageable. Consumers are <b>tolerant readers</b>: they take the fields they need and ignore the rest. And a breaking change is made as a new version beside the old one: publish <code>OrderPlaced.v2</code> as well as v1, move consumers across one by one, then stop publishing v1. It is the expand-and-contract move from the data volume, applied to events.</p>
<p>A schema registry or a contract test in the producer's build makes the rule automatic: the build fails if a change would break a registered consumer. Remember that replay makes old events live for ever, so “every consumer has upgraded” does not mean old shapes are gone.</p>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>Two kinds of broker</h3>
''' + tbl(["", "Queue", "Log"], [
    ["Examples", "RabbitMQ, Amazon SQS, Azure Service Bus", "Apache Kafka, Amazon Kinesis, Apache Pulsar"],
    ["A message is", "handed to one worker, then removed when acked", "appended and kept; each consumer group remembers its own position"],
    ["Order", "none by default; some offer ordered groups", "per partition"],
    ["Replay", "no, once acked it is gone", "yes, within the retention period"],
    ["Scaling a consumer", "add workers freely", "add workers up to the number of partitions"],
    ["Good at", "jobs and tasks: do this once", "events and history: this happened"],
]) + mn("Rule of thumb from class: commands and jobs like queues, facts like logs.") + full('''<p>Three product claims are worth reading carefully.</p>
<ul>
  <li><b>“Exactly-once” in a log broker</b> usually means: reading from one topic and writing to another can be made atomic inside the broker. Your own database, an email or a payment call are outside that boundary, and chapters 4 and 6 still apply.</li>
  <li><b>Built-in deduplication</b> in a queue service works on an id you supply and remembers it for a limited window, often minutes. It removes quick repeats from a producer. It is not a replacement for an idempotent consumer.</li>
  <li><b>Outbox support</b> exists in CDC connectors and in several messaging libraries. It saves you writing the relay. The table, the key and the event id are still your design.</li>
</ul>''') + '''
<h3>Lab</h3>
<p>The shop adds a <b>Stock</b> service. It must lower the stock count when an order is placed and raise it again when an order is cancelled. The warehouse also sends a nightly <code>StockCounted</code> event with the true number on the shelf.</p>
<ol class="keep">
  <li>What is the key for these events, and why?</li>
  <li><code>OrderPlaced</code> for two mugs arrives twice. Which technique from chapter 6 do you use?</li>
  <li><code>OrderCancelled</code> arrives before <code>OrderPlaced</code>. What does Stock do?</li>
  <li><code>StockCounted</code> says 80. How do you apply it safely next to the order events?</li>
  <li>Someone replays last week. What must not happen, and what guarantees it?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The key</summary><p>The product, not the order. Stock for mugs is the thing that must change in sequence, and one order can touch several products. So the Order service publishes one stock-relevant event per order line, keyed by product id. Orders for different products run in parallel.</p></details>
<details><summary>2 · The duplicate</summary><p>“Lower by 2” is a delta, so it is not naturally idempotent. Store a reservation row per order line, <code>(order 42, mug) = 2</code>, under a unique constraint, and compute stock as the count minus the reservations. A repeat hits the constraint and changes nothing. That is the “fact with identity” style, and it needs no id memory that could expire.</p></details>
<details><summary>3 · Cancel first</summary><p>Record the cancellation for <code>(order 42, mug)</code> even though no reservation exists. When <code>OrderPlaced</code> arrives later, Stock sees the cancellation and creates nothing. It is the tombstone from the Saga deep dive, and the order's version number makes the check simple.</p></details>
<details><summary>4 · The nightly count</summary><p><code>StockCounted</code> is state with a version: “80 on the shelf as of 02:00”. Store the count and its time. Reservations made before 02:00 for orders already picked are inside that number; later ones are subtracted from it. Applying the same count twice changes nothing, and an older count than the stored one is ignored.</p></details>
<details><summary>5 · Replay</summary><p>Stock must not be lowered a second time for last week's orders. Reservation rows per order line guarantee it, because they do not depend on a dedupe window. A seven-day <code>processed_events</code> table on its own would not.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Producer", ["The state change and the event are written in one transaction", "Every event has an id created once, a key and a version", "The relay publishes, then marks, and selects by “unsent”, not by highest id", "One active relay per key; sent rows are cleaned up"]),
    ("Consumer", ["The ack comes after the commit", "The id claim and the work are in one transaction, under a unique constraint", "Dedupe uses the producer's event id", "Outside side effects pass the id on, or go through the consumer's own outbox"]),
    ("Order", ["The key is chosen on purpose and written down", "Handlers ignore older versions and cope with a gap", "It is decided what a failing event does: block, step aside, or park its key"]),
    ("Failure", ["Retries are bounded and delayed; permanent errors skip them", "The dead-letter queue has an alert, an owner and a redrive tool", "Dedupe memory is longer than retention plus the replay window", "Replay cannot repeat outside side effects"]),
    ("Contracts", ["Consumers ignore fields and event types they don't know", "Breaking changes ship as a new version beside the old", "A build check protects registered consumers"]),
    ("Tests and operations", ["The consumer suite passes with every message delivered twice", "Events for one key are tested in shuffled order", "Outbox age, lag in time, redelivery rate and dead letters are on a dashboard", "One search by event id shows the whole trip"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="reliable-messaging", no=2, title="Reliable Messaging",
    sub="Exactly-once delivery does not exist. Here is how to get the same result anyway, with crashes, duplicates and events out of order.",
    summary="A deep dive on reliable messaging: delivery guarantees, the outbox and its relay, six failure drills, ordering, idempotent consumers, dead letters and replay, operations, testing and event contracts.",
    builds_on="Vol. 1, notes 06, 07, 11, 12",
    builds_on_links=[("Transactional Outbox", "../../distributed/notes/transactional-outbox.html"), ("Idempotent Consumer", "../../distributed/notes/idempotent-consumer.html"),
                     ("Publish–Subscribe", "../../distributed/notes/publish-subscribe.html"), ("Competing Consumers", "../../distributed/notes/competing-consumers.html")],
    notes=[("distributed", "transactional-outbox"), ("distributed", "idempotent-consumer"), ("distributed", "publish-subscribe"), ("distributed", "competing-consumers")],
    facts=[("Example", "order 42 and its <code>OrderPlaced</code> event")],
    blurb="Delivery guarantees, the outbox relay, six failure drills, ordering, idempotent consumers, dead letters, replay and event contracts.",
    chapters=[
        dict(id="recap", nav="Recap", title="Three notes in sixty seconds",
             gist="The outbox gets an event out of the producer safely. The broker copies it to every subscriber. The idempotent consumer survives a repeat. Each note fixed one hop. This deep dive follows one event across all of them, because the failures live between the hops.",
             body=recap),
        dict(id="guarantees", nav="Guarantees", title="What the guarantees really promise",
             gist="A sender that gets no confirmation must either resend, and risk a duplicate, or not resend, and risk a loss. There is no third option, so exactly-once delivery does not exist. What you can build is exactly-once effect: deliver at least once, and make repeats harmless.",
             body=guarantees,
             check=[("A consumer acks the message as soon as it arrives, then starts the work. Which guarantee is that, and what is lost in a crash?", "At most once. The broker believes the message is handled, so the work that was in progress never happens."),
                    ("A product says “exactly-once delivery”. What question do you ask?", "Exactly once between which two points? It usually covers the broker's own storage, not the effect in your database or an email.")]),
        dict(id="outbox", nav="Outbox", title="The outbox, for real",
             gist="The outbox is a table with an id, an event id, a key and a sent mark. The relay publishes first and marks second, so it sometimes sends twice and never loses. Select rows by “unsent”, never by “higher than the last id I saw”, or late commits will be skipped.",
             body=outbox,
             check=[("Why does the relay publish before it marks the row as sent, and not the other way round?", "Marking first and crashing before the publish would lose the event for good. Publishing first can only cause a repeat, which consumers handle."),
                    ("You run three relay instances to go faster. What breaks?", "Order within a key: two instances can publish events for the same order in the wrong sequence. Use one active relay, or give each a separate slice of keys.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six things that will happen to your events in production: a relay crash, a consumer crash, a message that can never succeed, the wrong order, a slow worker and a duplicate that arrives after you forgot its id. Each card ends with the rule that prevents it.",
             body=drills,
             check=[("Loyalty checks a cache for the event id, adds the points, then writes the id to the cache. Name two drills this fails.", "Drill 2: a crash after the points and before the cache write repeats the points. Drill 5: two workers both check before either writes."),
                    ("Why is a poison message worse on an ordered log than on a plain queue?", "On a log the worker reads in sequence and cannot pass the failing message, so every later event on that partition waits behind it.")]),
        dict(id="ordering", nav="Ordering", title="Ordering: the hard problem",
             gist="Order across everything is unaffordable. Order per key is cheap: pick a key, and the broker keeps that key's events in one line with one reader. Retries, extra workers and resizing still break it sometimes, so carry a version in every event and let the consumer keep the newest.",
             body=ordering,
             check=[("You key order events by customer id, not order id. What do you gain and lose?", "All of a customer's orders stay in sequence, which helps anything computed per customer. You lose parallelism: one busy customer's events all queue behind each other."),
                    ("Why does “state with version” survive both a duplicate and a late arrival?", "A duplicate has the same version as the stored one and a late event has a lower one. The rule “apply only if higher” ignores both.")]),
        dict(id="consumer", nav="Consumer", title="The idempotent consumer, in depth",
             gist="Three techniques: operations that are naturally repeatable, a dedupe table written in the same transaction as the work, and a version check. Dedupe on the producer's event id. When the work happens outside your database, pass the id on or route the work through an outbox of your own.",
             body=consumer,
             check=[("Why is the broker's message id a poor dedupe key?", "The relay's resend creates a new broker message with a new id, so the two copies look different."),
                    ("Email's provider has no idempotency key. How do you avoid a double send after a crash?", "Claim the event id and write “email to send” to Email's own outbox in one transaction; a relay does the send. A repeat of the event then finds the id already claimed.")]),
        dict(id="dead-letters", nav="Dead letters", title="Dead letters, retries and replay",
             gist="Retry in tiers: a few times at once, then with growing delays, then the dead-letter queue. That queue needs an alert, an owner and a way to send letters back. Replay re-reads old events to repair or rebuild, and it is safe only if handlers are idempotent beyond any time window and outside side effects are guarded.",
             body=dead,
             check=[("An event fails with “connection refused” to the database. Which tier, and why not the dead-letter queue?", "Tier 2, delayed retries. The error will pass when the database is back; sending it to a person would be noise."),
                    ("What makes redriving a dead-letter queue safe?", "Idempotent consumers. A redriven letter may have been partly handled before, or may be sent twice.")]),
        dict(id="running", nav="Running it", title="Running it: lag, numbers and a runbook",
             gist="Watch four numbers: the age of the oldest unsent outbox row, each consumer's lag measured in time, the share of redeliveries and the dead-letter count. Put the event id in every log line. When a customer says “it never arrived”, walk the path from the outbox forward.",
             body=running,
             check=[("Outbox age is flat at zero but Shipping's lag keeps growing. Where is the problem?", "On the consumer side: Shipping is too slow or stuck on one message. The producer and relay are fine."),
                    ("The redelivery rate jumps from 0.2 % to 15 % during a slow afternoon. Likely cause?", "Handling time has grown past the broker's wait for an ack, so messages are handed to a second worker while the first is still busy (drill 5).")]),
        dict(id="testing", nav="Testing", title="Testing, and events as contracts",
             gist="Cause the bad moments on purpose: deliver everything twice, shuffle events within a key, crash the relay and the consumer at the worst point. Treat an event's shape as a public interface: add optional fields freely, and never remove, rename or change the meaning of one without a new version.",
             body=testing,
             check=[("You change <code>total</code> from dollars to cents. No test fails. Why is this the most dangerous kind of change?", "Every consumer still parses the event, so nothing errors. Loyalty simply awards a hundred times the points until someone notices."),
                    ("All consumers have moved to <code>OrderPlaced.v2</code>. Can handlers drop support for v1?", "Only if no v1 events can come back. A replay of an older period still contains them.")]),
        dict(id="tools", nav="Tools & lab", title="Brokers, a lab and the checklist",
             gist="Queues hand a job to one worker and forget it; logs keep events in order per partition and let you read them again. Neither makes your consumer idempotent. The lab applies the whole deep dive to a stock counter, and the checklist turns it into review questions.",
             body=tools),
    ],
    sources="Pat Helland, “Idempotence Is Not a Medical Condition” (2012) and “Life beyond Distributed Transactions” (2007). Chris Richardson, <i>Microservices Patterns</i>, chapter 3. Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, chapter 11. Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (Dead Letter Channel, Idempotent Receiver, Guaranteed Delivery). Gunnar Morling, “Reliable Microservices Data Exchange With the Outbox Pattern” (2019).",
)
