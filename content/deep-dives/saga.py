# Deep dive 01 · Saga. Builds on Vol. 1, note 05 and keeps its example: order 42, two mugs, $49.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
recap = '''
<p>Our shop sells mugs. Placing order 42 touches four services, each with its own database. The note ended with this plan:</p>
''' + tbl(["#", "Step", "If we must undo", "Type"], [
    ["1", "Order: create as <code>PENDING</code>", "mark <code>CANCELLED</code>", "compensatable"],
    ["2", "Inventory: reserve 2 mugs", "release the reservation", "compensatable"],
    ["3", "Payment: charge $49", "none: this is the pivot", "pivot"],
    ["4", "Shipping: book the courier", "keep retrying", "retriable"],
    ["5", "Order: mark <code>APPROVED</code>", "keep retrying", "retriable"],
]) + mn("compensatable → pivot → retriable. If you remember one thing from the note, this.") + '''
<p class="full">That plan reads well on a whiteboard. It also hides the questions the note only touched. Where does the saga remember how far it got? What happens when a machine dies between two lines of code? What do other requests see while the saga is half done? How long may it take, how do you test it, and who fixes it at night? The chapters take them in that order.</p>
'''

# ------------------------------------------------------------------ 2 state machine
machine_svg = '''
  <rect class="bx" x="10" y="40" width="100" height="50" rx="8"/><text class="lbl" x="60" y="71" text-anchor="middle">PENDING</text>
  <rect class="bx" x="140" y="40" width="150" height="50" rx="8"/><text class="lbl" x="215" y="71" text-anchor="middle">STOCK_RESERVED</text>
  <rect class="bx-y" x="320" y="40" width="80" height="50" rx="8"/><text class="lbl" x="360" y="71" text-anchor="middle">PAID</text>
  <rect class="bx" x="430" y="40" width="160" height="50" rx="8"/><text class="lbl" x="510" y="71" text-anchor="middle">SHIPPING_BOOKED</text>
  <rect class="bx-g" x="620" y="40" width="110" height="50" rx="8"/><text class="lbl" x="675" y="71" text-anchor="middle">APPROVED</text>
  <path class="ln" d="M110 65 H138" marker-end="url(#a)"/><path class="ln" d="M290 65 H318" marker-end="url(#a)"/>
  <path class="ln" d="M400 65 H428" marker-end="url(#a)"/><path class="ln" d="M590 65 H618" marker-end="url(#a)"/>
  <text class="soft" x="360" y="26" text-anchor="middle">pivot: no way back from here</text>
  <path class="ln-r" d="M60 90 V187 H128" marker-end="url(#ar)"/><path class="ln-r" d="M215 90 V160" marker-end="url(#ar)"/>
  <rect class="bx-r" x="130" y="162" width="170" height="50" rx="8"/><text class="lbl" x="215" y="193" text-anchor="middle">COMPENSATING</text>
  <path class="ln-r" d="M215 212 V246" marker-end="url(#ar)"/>
  <rect class="bx-r" x="150" y="248" width="130" height="44" rx="8"/><text class="lbl" x="215" y="276" text-anchor="middle">CANCELLED</text>
  <text class="soft bad" x="72" y="140">a step fails</text>
  <path class="ln-d" d="M510 90 V160" marker-end="url(#a)"/>
  <rect class="bx" x="420" y="162" width="180" height="50" rx="8" stroke-dasharray="6 5"/><text class="lbl" x="510" y="193" text-anchor="middle">NEEDS_ATTENTION</text>
  <text class="soft" x="522" y="130">retries used up:</text><text class="soft" x="522" y="148">a human looks</text>
'''
machine = '''
<p>The code in the note was a <code>for</code> loop over steps. A loop keeps its position in memory, and memory is gone after a crash. The real design has two parts.</p>
<ol>
  <li><b>States.</b> Every place the saga can rest gets a name. Order 42 is always in exactly one of them.</li>
  <li><b>A saga log.</b> Before each command goes out, the orchestrator writes a row. When the reply comes back, it updates the row. The log lives in the orchestrator's own database.</li>
</ol>
''' + fig(760, 300, "State machine for the order saga. Forward path: Pending, Stock reserved, Paid, Shipping booked, Approved. A failure in Pending or Stock reserved leads to Compensating and then Cancelled. After Paid there is no path back; failures there are retried, and after too many retries the saga moves to Needs attention.",
          machine_svg, "Left of the pivot, failures go down to CANCELLED. Right of the pivot, the only exits are APPROVED or a human.") + '''
<h3>The saga log for order 42</h3>
<p>This is the whole memory of the saga. One row per step, written by the orchestrator.</p>
''' + tbl(["saga", "step", "command key", "status", "updated"], [
    ["42", "create-order", "42:1", "DONE", "10:00:00.120"],
    ["42", "reserve-stock", "42:2", "DONE", "10:00:00.310"],
    ["42", "charge-card", "42:3", "STARTED", "10:00:00.315"],
], hot=(2,), mono=(0, 2, 4)) + mn("STARTED = “I may or may not have sent this.” That honesty is what makes recovery possible.") + '''
<p>The pink row is the interesting one. <code>STARTED</code> with no <code>DONE</code> means the orchestrator does not know whether the card was charged. It may have crashed before sending, after sending, or after the charge succeeded but before the reply arrived.</p>
''' + full('''<h3>The recovery rule</h3>
<p>When an orchestrator starts, it reads every saga that is not in a final state and applies one rule:</p>
<p><mark>For a step that is STARTED, send the same command again with the same command key.</mark></p>
<p>That rule only works if every service treats a repeated key as “you already asked me this, here is the answer I gave before”. So the state machine forces a requirement onto every participant: commands are idempotent, keyed by saga id plus step number. This is the Idempotent Consumer note, now mandatory.</p>
<h3>Two writes that must not drift</h3>
<p>Writing the log row and sending the command are two actions. If the orchestrator writes <code>STARTED</code> and crashes before sending, recovery re-sends: fine. If it sent first and wrote second, a crash in between would leave a charge that the log knows nothing about. So the order is fixed: <b>write, then send</b>. In practice the command goes into an outbox table in the same local transaction as the log row, and a relay publishes it. That is the Transactional Outbox note, also now mandatory.</p>''')

# ------------------------------------------------------------------ 3 drills
drills = mn("Try to answer “what happens next?” before reading each drill. That is the exercise.") + '''
<ul class="drill-index" aria-label="The five drills">
  <li><a href="#drill-1">1 · crash between steps</a></li><li><a href="#drill-2">2 · timeout</a></li>
  <li><a href="#drill-3">3 · undo arrives first</a></li><li><a href="#drill-4">4 · undo fails</a></li><li><a href="#drill-5">5 · double click</a></li>
</ul>
''' + drill(1, "The orchestrator dies between two steps", [
    ("Timeline", "Inventory reserves two mugs and replies OK. The orchestrator crashes before it writes <code>DONE</code> for step 2."),
    ("What you see", "Two mugs are held. Order 42 shows PENDING. Nothing moves. Without recovery it stays that way, and the mugs are unsellable.", True),
    ("What saves you", "On restart the log shows step 2 as STARTED. The orchestrator re-sends <code>ReserveStock</code> with key 42:2. Inventory finds the key, returns the earlier OK and reserves nothing new. The saga continues to step 3."),
], "every step is safe to send twice, and the orchestrator resumes from its log, never from memory.") + drill(2, "The payment call times out", [
    ("Timeline", "The orchestrator sends <code>ChargeCard $49</code>. Two seconds pass. No reply."),
    ("The tempting mistake", "Treat the timeout as a failure and compensate: release the mugs, cancel the order. Then the payment provider finishes the charge it was working on. The customer has paid $49 for a cancelled order."),
    ("Why", "A timeout carries no information about the outcome. It means “I stopped waiting”. The request may never have arrived, may be running now, or may have finished with the reply lost on the way back.", True),
    ("What saves you", "Retry the same command with the same key until you get a definite answer: charged or declined. Only a definite “declined” starts the compensations. If you run out of patience, the saga moves to NEEDS_ATTENTION. It does not guess. Chapter 5 shows a way to get a definite answer on demand."),
], "a timeout is a question, not an answer. Never compensate on “I don't know”, least of all at the pivot.") + drill(3, "The undo arrives before the thing it undoes", [
    ("Timeline", "<code>ReserveStock</code> is stuck in a slow queue. The saga's overall deadline passes, so the orchestrator sends <code>ReleaseStock</code>. Inventory has nothing to release and replies OK. A minute later the delayed <code>ReserveStock</code> finally arrives and reserves two mugs for an order that is already cancelled."),
    ("What you see", "Stock that slowly leaks away. Each leaked reservation belongs to a cancelled order, so no process will ever release it. Someone notices weeks later when the warehouse count and the system disagree.", True),
    ("What saves you", "Two behaviours in the participant. First, a compensation for a step that never ran must succeed and do nothing. Second, it must leave a tombstone: “42:2 was cancelled”. When the late command arrives, Inventory sees the tombstone and refuses it."),
], "compensations work even when there is nothing to undo, and they block the late original.") + drill(4, "The compensation itself fails", [
    ("Timeline", "Payment declines the card. The orchestrator sends <code>ReleaseStock</code>. Inventory is down for a deploy."),
    ("The tempting mistake", "Catch the error, log it and mark the order CANCELLED anyway. The order looks finished, the mugs stay reserved, and nobody is told.", True),
    ("What saves you", "A compensation is a retriable step: it has no “undo of the undo”, so it must eventually succeed. Retry with backoff for as long as it is reasonable. The saga stays in COMPENSATING, which is visible on a dashboard. After a limit it moves to NEEDS_ATTENTION with the failed step named."),
], "compensations may be slow but they may not be optional. Design them so the only possible failures are temporary.") + drill(5, "The customer double-clicks “Place order”", [
    ("Timeline", "Two identical requests arrive 80 ms apart. Two sagas start. Both reserve mugs, both charge $49."),
    ("Why the earlier rules don't help", "Idempotent steps protect one saga from repeating itself. Here there are two sagas with two ids, and each is behaving correctly.", True),
    ("What saves you", "The saga id must come from the client's intent, not from the server's clock. The checkout page generates one idempotency key when it loads. The orchestrator has a unique constraint on that key, so the second request finds saga 42 already running and returns its status."),
], "starting a saga must be idempotent too. One customer intent, one saga id.") + full('''<h3 id="participant-rules">What the five drills add up to</h3>
''' + tbl(["Every participant must…", "Because of"], [
    ["recognise a repeated command key and return the first result", "drills 1, 2"],
    ["accept a compensation for a step it never saw", "drill 3"],
    ["reject a step whose compensation already ran", "drill 3"],
    ["offer compensations that only fail temporarily", "drill 4"],
]) + '''<p>This is the real cost of a saga. The orchestrator is the small part. The contract that every service has to honour is the large part, and it is the part teams skip.</p>''')

# ------------------------------------------------------------------ 4 isolation
isolation = '''
<p>ACID has four letters. A saga keeps atomicity in a weaker form (all steps finish, or all are compensated), keeps consistency and durability inside each service, and drops isolation completely. Three things follow.</p>
<h3>Three anomalies, with mugs</h3>
''' + tbl(["Anomaly", "What happens in the shop"], [
    ["<b>Dirty read</b>", "Order 42 reserves the last two mugs. Order 43 sees zero stock and tells its customer “sold out”. Then 42's card is declined and the mugs come back. Order 43 lost a sale because of data that was never final."],
    ["<b>Lost update</b>", "While order 42 waits for payment, the customer changes the delivery address. Step 5 then saves the order using the copy it read at step 1. The new address is gone."],
    ["<b>Fuzzy read</b>", "Step 1 reads the mug price as $24.50. Marketing changes it to $27 before step 3. The order confirmation says $49 and the card is charged $54."],
]) + mn("None of these is a bug in one service. Each service did its job. The bug is in the gaps.") + '''
<h3>Six countermeasures</h3>
''' + tbl(["Countermeasure", "Idea", "In the shop"], [
    ["<b>Semantic lock</b>", "Mark the record as mid-saga so others can react", "Order is <code>PENDING</code>; address edits are refused or queued until it is final"],
    ["<b>Commutative updates</b>", "Design changes so their order doesn't matter", "Stock moves by <code>+2</code> and <code>-2</code>, never “set stock to 8”"],
    ["<b>Pessimistic view</b>", "Reorder steps so risky data shows up late", "Loyalty points are added after the pivot, so nobody spends points from an order that gets cancelled"],
    ["<b>Reread value</b>", "Check the data hasn't changed before writing", "Step 5 rereads the order's version number and restarts if it moved"],
    ["<b>By value</b>", "Carry the facts inside the saga", "The $49 total travels in the saga's context; no step looks the price up again"],
    ["<b>Version file</b>", "Record operations so they can be reordered", "Payment logs “authorise” and “cancel” per order, so a cancel that arrives first still wins"],
]) + full('''<p>Semantic lock is the one you will use most, and it comes with a decision. When another request meets a locked record, it can <b>fail fast</b> (“this order is being processed, try again”) or <b>wait</b> until the saga ends. Failing fast is simple and pushes the retry to the caller. Waiting is friendlier and brings back a problem sagas were meant to avoid: two sagas waiting on each other's locks is a deadlock, and now you need a timeout to break it.</p>
<p>For the dirty read on stock there is a product answer as well as a technical one. Many shops show “2 left, reserved in another basket” for a few minutes. The half-finished state becomes something the customer can see and understand. That is often cheaper than hiding it.</p>''')

# ------------------------------------------------------------------ 5 time
time_ = '''
<p>A saga that never fails and never finishes is the most common production problem. The cause is nearly always a state with no clock on it. Give the saga three clocks.</p>
''' + tbl(["Clock", "What it limits", "Order saga", "When it rings"], [
    ["<b>Attempt timeout</b>", "one call to one service", "5 s for the charge, 2 s elsewhere", "retry the same command, same key"],
    ["<b>Step budget</b>", "all attempts of one step", "4 attempts, about 30 s", "treat the step as failed, if the outcome is known"],
    ["<b>Saga deadline</b>", "the time before the pivot", "5 minutes", "stop going forward and compensate"],
]) + mn("Set the attempt timeout a little above the service's slow-day response time. Too short and you create your own timeouts.") + '''
<p>After the pivot there is no deadline that cancels anything. Retriable steps get a long budget (booking a courier may retry for a day) and then the saga goes to NEEDS_ATTENTION.</p>
<h3>Getting a definite answer from payment</h3>
<p>Drill 2 left a gap. The saga deadline rings while the charge is still <code>STARTED</code>, and we are not allowed to guess. The usual fix is to split the payment in two, the way card payments already work.</p>
''' + tbl(["#", "Step", "If we must undo", "Type"], [
    ["3a", "Payment: <b>authorise</b> $49 (hold the money, take nothing)", "<b>void</b> the authorisation", "compensatable"],
    ["3b", "Payment: <b>capture</b> the $49", "none", "pivot"],
], hot=(0,)) + '''
<p><code>Void 42:3a</code> follows the rules from drill 3: it works when the authorisation exists, it works when the authorisation never arrived, and it blocks a late one. So sending it always ends in a definite state, “no money held”. The dangerous step is now compensatable, and the pivot is a capture on money that is already reserved, which rarely fails.</p>
''' + full('''<h3>Timers must survive a crash too</h3>
<p>A timer in memory dies with the process, exactly like the <code>for</code> loop in chapter 2. So a deadline is stored as data: each saga row has a <code>wake_at</code> column. A small job, the <b>sweeper</b>, runs every few seconds and picks up sagas whose time has come.</p>
''' + code("sweeper.sql", "runs every 5 s", '''
SELECT saga_id, state
FROM saga
WHERE state NOT IN ('APPROVED', 'CANCELLED')
  AND wake_at < now()
ORDER BY wake_at
LIMIT 100
FOR UPDATE SKIP LOCKED;   -- several sweepers can run side by side
''') + '''
<p>For each row the sweeper feeds a <code>TimerFired</code> event into the state machine, the same way a reply would arrive. The machine decides what it means in that state: retry, compensate or ask for a human. The sweeper also acts as the recovery job from chapter 2, because a saga whose orchestrator crashed is simply a saga that slept past its <code>wake_at</code>.</p>
<h3>What the customer sees meanwhile</h3>
<p>Internal states are too many and too technical to show. Map them to three.</p>
''' + tbl(["Customer sees", "Internal states", "Note"], [
    ["Processing your order…", "PENDING, STOCK_RESERVED, COMPENSATING", "a spinner for seconds; after 10 s, “we'll email you”"],
    ["Order confirmed", "PAID and everything after it", "confirm at the pivot, not at the end"],
    ["Order cancelled, you were not charged", "CANCELLED", "say what happens to the money in the same sentence"],
]) + '''<p>Confirming at the pivot is safe because every later step is retriable. A saga in NEEDS_ATTENTION after the pivot still shows “confirmed” to the customer. Support sees the flag; the customer should not have to.</p>''')

# ------------------------------------------------------------------ 6 styles
styles_svg = '''
  <text class="lbl" x="190" y="24" text-anchor="middle">orchestration</text>
  <rect class="bx-y" x="130" y="100" width="120" height="50" rx="8"/><text class="lbl" x="190" y="131" text-anchor="middle">orchestrator</text>
  <rect class="bx" x="20" y="40" width="90" height="40" rx="8"/><text x="65" y="66" text-anchor="middle">Order</text>
  <rect class="bx" x="270" y="40" width="90" height="40" rx="8"/><text x="315" y="66" text-anchor="middle">Inventory</text>
  <rect class="bx" x="20" y="170" width="90" height="40" rx="8"/><text x="65" y="196" text-anchor="middle">Payment</text>
  <rect class="bx" x="270" y="170" width="90" height="40" rx="8"/><text x="315" y="196" text-anchor="middle">Shipping</text>
  <path class="ln" d="M140 100 L104 82" marker-end="url(#a)"/><path class="ln" d="M240 100 L276 82" marker-end="url(#a)"/>
  <path class="ln" d="M140 150 L104 168" marker-end="url(#a)"/><path class="ln" d="M240 150 L276 168" marker-end="url(#a)"/>
  <text class="soft" x="190" y="236" text-anchor="middle">commands out, replies back;</text><text class="soft" x="190" y="256" text-anchor="middle">state lives in the middle</text>
  <path class="ln-d" d="M390 10 V262"/>
  <text class="lbl" x="580" y="24" text-anchor="middle">choreography</text>
  <rect class="bx" x="420" y="60" width="90" height="40" rx="8"/><text x="465" y="86" text-anchor="middle">Order</text>
  <rect class="bx" x="650" y="60" width="90" height="40" rx="8"/><text x="695" y="86" text-anchor="middle">Inventory</text>
  <rect class="bx" x="650" y="160" width="90" height="40" rx="8"/><text x="695" y="186" text-anchor="middle">Payment</text>
  <rect class="bx" x="420" y="160" width="90" height="40" rx="8"/><text x="465" y="186" text-anchor="middle">Shipping</text>
  <path class="ln" d="M510 80 H648" marker-end="url(#a)"/><text class="soft" x="580" y="72" text-anchor="middle">OrderCreated</text>
  <path class="ln" d="M695 100 V158" marker-end="url(#a)"/><text class="soft" x="686" y="134" text-anchor="end">StockReserved</text>
  <path class="ln" d="M650 180 H512" marker-end="url(#a)"/><text class="soft" x="580" y="172" text-anchor="middle">PaymentTaken</text>
  <path class="ln" d="M465 160 V102" marker-end="url(#a)"/><text class="soft" x="474" y="134">CourierBooked</text>
  <text class="soft" x="580" y="236" text-anchor="middle">events passed along;</text><text class="soft" x="580" y="256" text-anchor="middle">state is spread over four services</text>
'''
styles = fig(760, 270, "Two ways to run the order saga. Orchestration: an orchestrator in the middle sends commands to Order, Inventory, Payment and Shipping and gets replies. Choreography: Order publishes OrderCreated, Inventory reacts and publishes StockReserved, Payment reacts and publishes PaymentTaken, Shipping reacts and publishes CourierBooked, which Order hears.",
             styles_svg, "Same four services, same five steps. The difference is where the knowledge of the flow lives.") + '''
<p>The note gave a rule of thumb for choosing. Here is the detail behind it.</p>
''' + tbl(["Question", "Orchestration", "Choreography"], [
    ["Where is the flow written down?", "one state machine", "nowhere; it is the sum of who listens to what"],
    ["Where is order 42 right now?", "one row in the saga log", "ask four services, or build a tracking view"],
    ["Who owns the deadline?", "the orchestrator", "nobody, unless you appoint someone"],
    ["Who starts compensation?", "the orchestrator sends undo commands", "each service reacts to a failure event"],
    ["Adding a step", "change the orchestrator", "change who subscribes to what, in several teams"],
    ["Coupling", "orchestrator knows every service", "services know each other's events"],
]) + '''
<h3>The five drills, run against choreography</h3>
''' + tbl(["Drill", "What changes"], [
    ["1 · crash between steps", "Each service must save its change and publish its event atomically (outbox). If one forgets, the chain stops silently and no component notices, because no component expects the next event."],
    ["2 · timeout", "Nobody is waiting for a reply, so nobody times out. A stuck saga looks like silence. In practice the Order service sets a timer on PENDING, which makes it a small orchestrator."],
    ["3 · undo arrives first", "More likely than before. <code>PaymentDeclined</code> can reach Inventory before <code>OrderCreated</code> does, because the two events travel on different topics. The tombstone rule is unchanged."],
    ["4 · undo fails", "The broker redelivers until the consumer succeeds. The dead-letter queue plays the part of NEEDS_ATTENTION, so someone has to watch it."],
    ["5 · double click", "Unchanged: the first service needs the unique key."],
]) + mn("Choreography doesn't remove the orchestrator's work. It hands a piece of it to every team.") + full('''<h3>Two problems only choreography has</h3>
<p><b>Cycles.</b> Order listens to Payment's events to mark itself paid. Payment listens to Order's events to know what to charge. Each service now depends on the other's event format, and a change on either side breaks both. In orchestration the dependencies all point one way, toward the orchestrator.</p>
<p><b>An invisible flow.</b> A new engineer cannot open one file and read what happens to an order. The remedy is discipline: every event carries the saga id, and a tracking service or a trace view rebuilds the story from the events (chapter 8).</p>
<h3>Choosing</h3>
''' + tbl(["Choose", "When"], [
    ["Choreography", "two to four steps, in a line, no deadline to enforce, and the teams want to stay independent"],
    ["Orchestration", "branches, deadlines or human steps; or the business asks “where is my order?”"],
    ["Both", "events between business areas, an orchestrator inside one area. Common and sensible"],
]))

# ------------------------------------------------------------------ 7 testing
testing = '''
<p>The happy path of a saga is easy to test and tells you almost nothing. The bugs live in the moments between steps. Three kinds of test reach them.</p>
<h3>1 · The state machine as a plain function</h3>
<p>Write the saga's logic as a function with no database and no network: given a state and an event, return the new state and the commands to send. Then test it with a table.</p>
''' + code("order-saga.test.ts", "one row per (state, event) pair", '''
const cases = [
  // state            event               new state         commands
  ["STOCK_RESERVED", "PaymentCaptured",  "PAID",           ["BookCourier"]],
  ["STOCK_RESERVED", "PaymentDeclined",  "COMPENSATING",   ["ReleaseStock"]],
  ["STOCK_RESERVED", "TimerFired",       "COMPENSATING",   ["VoidPayment", "ReleaseStock"]],
  ["PAID",           "TimerFired",       "PAID",           ["BookCourier"]],   // retry, never undo
  ["PAID",           "PaymentCaptured",  "PAID",           []],                // duplicate reply
  ["CANCELLED",      "StockReserved",    "CANCELLED",      ["ReleaseStock"]],  // late reply
];

for (const [state, event, next, commands] of cases) {
  test(`${state} + ${event}`, () => {
    expect(step(state, event)).toEqual({ state: next, commands });
  });
}
''') + '''
<p>The last three rows are the valuable ones. Every state must have an answer for every event, including the ones that “cannot happen”. In production they happen.</p>
''' + full('''<h3>2 · Kill the orchestrator at every write</h3>
<p>Chapter 2 claimed that the saga survives a crash at any point. This test proves it. Run the saga against in-memory fakes of the four services. Count the writes to the saga log in a normal run, say 12. Then run the saga 12 more times, and on run <i>k</i> stop the orchestrator right after write <i>k</i>, start a fresh one, and let it finish.</p>
''' + code("crash-recovery.test.ts", "every crash point, one assertion", '''
for (let k = 1; k <= totalWrites; k++) {
  test(`crash after log write ${k}`, async () => {
    const world = new FakeWorld();                 // fake Order, Inventory, Payment, Shipping
    await runUntilWrite(k, world).catch(() => {});  // the orchestrator "dies" here
    await new Orchestrator(world).recover();        // a fresh process reads the log

    expect(world.order(42).status).toBe("APPROVED");
    expect(world.effects("capture")).toBe(1);       // charged exactly once
    expect(world.effects("reserve")).toBe(1);
    expect(world.effects("bookCourier")).toBe(1);
  });
}
''') + '''
<p>Repeat it with a card that declines, and assert the opposite: order CANCELLED, nothing reserved, nothing captured. If a write-then-send is in the wrong order anywhere, one of these runs fails.</p>
<h3>3 · A contract test for every participant</h3>
<p>The four rules from chapter 3 turn directly into four tests. Each service team runs them against its own command handler.</p>
''' + tbl(["Test", "Send", "Expect"], [
    ["repeat", "<code>Reserve 42:2</code> twice", "one reservation, the same reply both times"],
    ["empty undo", "<code>Release 42:2</code> with no earlier reserve", "OK, nothing changes"],
    ["late original", "<code>Release 42:2</code>, then <code>Reserve 42:2</code>", "the reserve is refused"],
    ["repeat undo", "<code>Release 42:2</code> twice", "OK both times, stock released once"],
]) + '''<p>These are small and dull, and they are what stands between you and drill 3 in production. Put them in a shared test kit so a new participant gets them for free.</p>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>A saga's promise is “eventually”. Running one means being able to see how long eventually is taking, and being able to help when it stalls.</p>
<h3>Three numbers</h3>
''' + tbl(["Metric", "Healthy", "Alert when"], [
    ["Sagas in flight, per state", "a few, changing constantly", "one state keeps growing: its next step is stuck"],
    ["Age of the oldest unfinished saga", "seconds", "older than the saga deadline plus a margin: the sweeper is not doing its job"],
    ["Sagas in NEEDS_ATTENTION", "zero", "above zero: each one is a customer waiting"],
]) + mn("Also worth a graph: the share of sagas that end CANCELLED. A jump means a participant is failing, not that customers changed their minds.") + '''
<h3>One id everywhere</h3>
<p>Every command, event, log line and trace carries the saga id. Then one search tells the story of order 42 across four services:</p>
''' + tbl(["time", "service", "message"], [
    ["10:00:00.120", "order", "saga=42 order created PENDING"],
    ["10:00:00.310", "inventory", "saga=42 key=42:2 reserved 2 × mug"],
    ["10:00:05.320", "orchestrator", "saga=42 step=charge attempt=1 timeout"],
    ["10:00:06.900", "payment", "saga=42 key=42:3 duplicate key, returning earlier result: captured"],
    ["10:00:06.940", "orchestrator", "saga=42 PAID"],
], hot=(2,), mono=(0,)) + '''
<p>That is drill 2 as it looks from the outside: a timeout, a retry with the same key, and a payment service that had already done the work.</p>
''' + full('''<h3>Runbook: a saga is stuck</h3>
<ol>
  <li><b>Read the saga log.</b> Which step is STARTED, and since when?</li>
  <li><b>Ask the participant.</b> Every service offers “status of command 42:3”. That endpoint is a requirement, and this is the moment you need it. Now you know more than the orchestrator does.</li>
  <li><b>Look at the pivot.</b> Before it, the safe direction is backward: compensate. After it, the only direction is forward: fix what blocks the step and retry.</li>
  <li><b>Use the admin actions</b>: “retry step”, “compensate now” or “mark step done, with a reason”. They go through the same state machine and the same idempotent commands as normal traffic.</li>
  <li><b>Write down what you did</b> on the saga itself, so the next person sees it.</li>
</ol>
<p>What you never do is edit rows by hand in four databases. A manual fix skips the tombstones and idempotency records, and the next late message undoes it.</p>
<h3>Reconciliation: proof that “eventually” arrived</h3>
<p>Once a night a job compares the services with each other and reports anything that breaks these three sentences.</p>
<ul>
  <li>No order is CANCELLED while stock is still reserved for it.</li>
  <li>No order is CANCELLED while money is held or captured for it.</li>
  <li>No order is APPROVED without a captured payment and a courier booking.</li>
</ul>
<p>The job should find nothing. When it finds something, you have discovered a broken participant rule before the customer or the warehouse did.</p>
<h3>Changing the saga while sagas are running</h3>
<p>You deploy a new version with an extra step, “check fraud score”, between 2 and 3. At that moment hundreds of sagas are in STOCK_RESERVED under the old definition. Store a <b>definition version</b> on each saga row. A saga finishes under the version it started with; new sagas use the new one. Remove the old code only when the count of old-version sagas reaches zero.</p>''')

# ------------------------------------------------------------------ 9 tools
tools = '''
<p>Everything in chapters 2 and 5 is plumbing: a durable log, recovery, retries, timers. Workflow engines sell exactly that plumbing. It helps to be precise about what they cover.</p>
''' + tbl(["You need", "Chapter", "An engine gives you"], [
    ["Durable state and crash recovery", "2", "yes"],
    ["Retries with backoff, durable timers", "5", "yes"],
    ["A view of every running saga", "8", "yes, usually a good one"],
    ["Running compensations in order", "2", "yes; you still write each compensation"],
    ["Idempotent participants, tombstones", "3", "no. This is in your services"],
    ["Isolation countermeasures", "4", "no. This is in your data model"],
    ["Versioning running sagas", "8", "partly; each engine has rules you must follow"],
], hot=(4, 5)) + mn("An engine replaces the orchestrator you would have written. It does not replace the contract with the participants.") + '''
<h3>Four families</h3>
''' + tbl(["Family", "Examples", "The flow is written as"], [
    ["Durable execution", "Temporal, Azure Durable Functions", "ordinary code that the engine can replay after a crash"],
    ["State machine service", "AWS Step Functions", "a JSON definition of states and transitions"],
    ["Process engine", "Camunda", "a BPMN diagram that business people can read"],
    ["Saga support in a messaging library", "MassTransit, NServiceBus, Axon", "a state machine class next to your message handlers"],
]) + full('''<p>Each has a cost that is easy to miss. Durable execution replays your workflow code to rebuild its state, so that code has to be deterministic: no random numbers, clock reads or direct network calls outside the engine's own functions. A state machine service keeps logic in a definition file that needs its own tests. A process engine adds a modelling tool and people who can use it. All of them are one more system to run, upgrade and understand at 3 a.m.</p>
<h3>Build or adopt?</h3>
''' + tbl(["Write your own (a table, an outbox, a sweeper)", "Adopt an engine"], [
    ["one or two sagas", "many workflows, or new ones every quarter"],
    ["a handful of steps, minutes long", "long waits: days, human approvals, reminders"],
    ["the team already runs a database and a broker well", "the team wants the dashboard and history without building them"],
]) + '''<p>Either way, chapters 3 and 4 remain your work. Teams that adopt an engine and skip those chapters get the same incidents, with better dashboards.</p>''')

# ------------------------------------------------------------------ 10 lab
lab = '''
<p>Order 42 was delivered. A week later the customer wants to send the mugs back and get the $49 refunded. Design the <b>return saga</b>. You have five services: Order, Shipping (books a pickup), Warehouse (a person inspects the parcel), Payment and Inventory.</p>
<ol class="keep">
  <li>List the steps in order. Mark each as compensatable, pivot or retriable.</li>
  <li>Where does the refund go, and why there?</li>
  <li>One step waits for a human. How long may it wait, and what happens then?</li>
  <li>What stops the customer from starting two returns for the same order?</li>
  <li>Which of the five drills would cost real money here?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>Show the steps</summary>
''' + tbl(["#", "Step", "If we must undo", "Type"], [
    ["1", "Order: create return, order becomes <code>RETURN_IN_PROGRESS</code>", "cancel the return, order back to <code>DELIVERED</code>", "compensatable"],
    ["2", "Shipping: book a pickup", "cancel the pickup", "compensatable"],
    ["3", "Warehouse: parcel received and accepted", "none", "pivot"],
    ["4", "Payment: refund $49", "keep retrying", "retriable"],
    ["5", "Inventory: stock <code>+2</code>", "keep retrying", "retriable"],
    ["6", "Order: mark <code>RETURNED</code>", "keep retrying", "retriable"],
]) + '''</details>
<details><summary>Why the refund comes after the pivot</summary><p>A refund is the step you cannot take back: charging the customer again needs their consent. So it goes after everything that can still fail, including the inspection. The note's rule, hard-to-undo last, decides the order.</p></details>
<details><summary>The human step</summary><p>The saga rests in <code>AWAITING_PARCEL</code> with a <code>wake_at</code> 14 days ahead. If the parcel never arrives, the timer fires and the saga compensates: cancel the pickup, cancel the return. If the inspector rejects the parcel, that is a definite “no” and it compensates the same way. Two weeks in one state is normal for a saga, and it is the reason timers are stored as data.</p></details>
<details><summary>Two returns for one order</summary><p>A semantic lock. Step 1 moves the order to <code>RETURN_IN_PROGRESS</code>, and a second return request for an order in that state is refused. The saga id is derived from the return request, so a double click is also covered.</p></details>
<details><summary>The expensive drill</summary><p>Drill 2 on the refund step. A timeout followed by a retry with a new key refunds $98. The refund command must carry a stable key such as <code>return-42:4</code>, and the payment service must recognise it.</p></details>
</div>
<h3>The review checklist</h3>
<p>Take this to the design review of any saga. Each line is a question from one of the chapters.</p>
''' + checklist([
    ("Steps", ["Every step is typed: compensatable, pivot or retriable", "The pivot is named, and nothing hard to undo comes before it", "Every compensation can only fail temporarily"]),
    ("State", ["Every resting state has a name and a maximum age", "The log is written before the command is sent, through an outbox", "The saga id comes from the customer's intent"]),
    ("Participants", ["A repeated key returns the first result", "An undo for an unknown step succeeds and leaves a tombstone", "A step after its undo is refused", "Each participant can report the status of a command key"]),
    ("Isolation", ["Every record another request can touch mid-saga has a countermeasure", "Money and stock change by amounts, not by overwriting", "Values the customer saw travel inside the saga"]),
    ("Time", ["Attempt timeout, step budget and saga deadline are set", "Timers are rows, picked up by a sweeper", "The customer is told at the pivot"]),
    ("Tests and operations", ["A test crashes the orchestrator after every log write", "The three numbers are on a dashboard with alerts", "There is a runbook and admin actions, and nobody edits rows by hand", "A nightly reconciliation checks the services against each other"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="saga", no=1, title="Saga",
    sub="What actually happens when a multi-service transaction crashes halfway, and how to design one that survives it.",
    summary="A deep dive on the Saga pattern: the saga log and state machine, five failure drills, isolation anomalies, timeouts, orchestration vs choreography, testing, operations and tools.",
    builds_on="Vol. 1, note 05",
    builds_on_links=[("Saga", "../../distributed/notes/saga.html"), ("Transactional Outbox", "../../distributed/notes/transactional-outbox.html"),
                     ("Idempotent Consumer", "../../distributed/notes/idempotent-consumer.html")],
    notes=[("distributed", "saga")],
    facts=[("Example", "order 42: two mugs, $49")],
    blurb="The saga log, five failure drills, the missing isolation, timeouts, both styles side by side, testing, operations and tools.",
    chapters=[
        dict(id="recap", nav="Recap", title="The note in sixty seconds",
             gist="A saga replaces one big transaction with a chain of small local ones. Each step commits on its own. If a later step fails, you run compensations for the earlier ones. The note taught the shape. This deep dive is about everything that goes wrong inside that shape.",
             body=recap),
        dict(id="machine", nav="State machine", title="A saga is a state machine with a diary",
             gist="Stop thinking of a saga as a function that runs top to bottom. Think of it as a row in a table that moves between named states. The orchestrator can die at any moment, so it writes down what it is about to do, then does it, then writes down that it is done.",
             body=machine,
             check=[("The log says step 3 is STARTED and the orchestrator has just restarted. Should it compensate steps 1 and 2?", "No. It does not know that step 3 failed. It re-sends the charge command with key 42:3 and acts on the reply."),
                    ("Why is the command key 42:3 and not a fresh random id on each attempt?", "A fresh id makes each retry look like a new request, so the customer could be charged twice. A stable key lets Payment recognise the repeat.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Five things that will happen to your saga in production. Each drill shows the timeline, what you would see, why, and the design rule that prevents it. If you only skim, read the green rule at the bottom of each card.",
             body=drills,
             check=[("Inventory receives <code>Release 42:2</code> but has no reservation for 42. What are the two things it must do?", "Reply OK without changing stock, and record that 42:2 was cancelled so a late <code>Reserve 42:2</code> is refused."),
                    ("A colleague proposes: “on timeout, compensate; if the charge turns out to have succeeded, refund it later.” What is wrong with that?", "It turns an uncertain moment into a certain bad experience: the customer is charged for a cancelled order and waits days for a refund. It also needs a process that notices the late charge, which is the same work as waiting for a definite answer.")]),
        dict(id="isolation", nav="Isolation", title="The missing letter: no isolation",
             gist="A database transaction hides its half-finished work from everyone else. A saga cannot: each step commits and is visible at once. Other requests can read, and change, data that the saga may still undo. There are six standard countermeasures, and you choose them per step.",
             body=isolation,
             check=[("Which countermeasure fixes the fuzzy read on price, and why is it the cheapest?", "By value: put the price in the saga's context at step 1. No lock, no reread, no extra call. The customer pays what the confirmation page showed."),
                    ("Your refund step sets <code>balance = 120</code>. What breaks, and how do you rewrite it?", "If another saga changed the balance in between, its change is overwritten. Rewrite it as a commutative update: <code>balance = balance + 49</code>.")]),
        dict(id="time", nav="Time", title="Timeouts, deadlines and the stuck saga",
             gist="Every resting state gets a maximum age. Three clocks do the work: a timeout per attempt, a budget per step and a deadline for the whole saga before its pivot. Timers are stored as rows, and a sweeper job wakes the sagas that have slept too long.",
             body=time_,
             check=[("The saga deadline fires while the saga is in PAID. What should the state machine do?", "Not compensate. After the pivot a timer only means “retry the current step”, and after the step's budget, NEEDS_ATTENTION."),
                    ("Why does splitting payment into authorise and capture solve drill 2?", "Because a void is a compensation that always ends in a known state, whether or not the authorisation arrived. The saga can stop waiting without guessing.")]),
        dict(id="styles", nav="Two styles", title="Orchestration and choreography, side by side",
             gist="The same saga can be run by one coordinator or by services reacting to each other's events. The drills apply to both. What changes is who is responsible for each rule: in orchestration one component, in choreography every team.",
             body=styles,
             check=[("In a choreographed saga, which service notices that order 42 has been PENDING for an hour?", "None, unless one was given that job. Usually Order owns a timer on its PENDING state."),
                    ("Why is drill 3 more likely with choreography?", "The step and its undo are triggered by different events on different topics, so nothing guarantees their order of arrival.")]),
        dict(id="testing", nav="Testing", title="Testing a saga",
             gist="Test the state machine as a plain function with a table of cases. Then crash the orchestrator after every single log write and check that the saga still ends correctly. Then give every participant the same four contract tests.",
             body=testing,
             check=[("Your crash test passes for all 12 crash points on the happy path. What have you not tested yet?", "Crashes during compensation. Run the same loop with a declining card, so the crash points fall inside COMPENSATING."),
                    ("Why does the table include <code>CANCELLED + StockReserved</code>?", "It is the orchestrator's side of drill 3: a late reply for a saga that already gave up. The machine must answer with a release, not ignore it.")]),
        dict(id="running", nav="Running it", title="Running it: dashboards and repair",
             gist="Watch three numbers: sagas in flight per state, the age of the oldest one, and how many need a human. Put the saga id on every message and log line. Repair stuck sagas through admin actions that use the normal commands, and let a nightly job check that the services agree.",
             body=running,
             check=[("A saga is stuck in STOCK_RESERVED and Payment's status endpoint says “no such command 42:3”. Forward or backward?", "Either is safe, because the charge never arrived. Retrying is the normal choice; if you compensate, the void still has to be sent so that a late charge is blocked."),
                    ("Reconciliation finds a CANCELLED order with stock reserved. Which rule was broken, and where?", "Most likely Inventory accepted a reserve after its release (drill 3, no tombstone), or a compensation was skipped (drill 4).")]),
        dict(id="tools", nav="Tools", title="Tools, and when to stop writing your own",
             gist="A workflow engine gives you the durable log, recovery, retries, timers and a dashboard. It gives you nothing for idempotent participants or isolation. Adopt one when you have many workflows or long waits; a table, an outbox and a sweeper are enough for one or two short sagas.",
             body=tools),
        dict(id="lab", nav="Lab", title="Lab and review checklist",
             gist="Design a return-and-refund saga for order 42, then compare with the model answer. The checklist at the end is the whole deep dive as questions to ask in a design review.",
             body=lab),
    ],
    sources="Garcia-Molina and Salem, “Sagas” (1987). Frank and Zahorjan, “Semantic ACID properties in multidatabases using remote procedure calls and update propagations” (1998), for the countermeasures. Chris Richardson, <i>Microservices Patterns</i>, chapter 4. Caitie McCaffrey, “Distributed Sagas: A Protocol for Coordinating Microservices” (talk). Pat Helland, “Life beyond Distributed Transactions” (2007).",
)
