# Deep dive 03 · The Resilience Stack. Builds on Vol. 1 notes 01 (circuit breaker), 02 (retry with backoff),
# 03 (bulkhead) and 04 (rate limiter). Example, from the circuit breaker note: Checkout calls Payments, Payments
# calls the Bank API. Normal day: 100 requests a second, the bank answers in 200 ms, Payments has 200 threads.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
chain_svg = '''
  <rect class="bx" x="20" y="60" width="90" height="60" rx="8"/><text class="lbl" x="65" y="96" text-anchor="middle">shopper</text>
  <rect class="bx" x="180" y="50" width="130" height="80" rx="8"/><text class="lbl" x="245" y="86" text-anchor="middle">Checkout</text><text class="soft" x="245" y="108" text-anchor="middle">waits 3 s at most</text>
  <rect class="bx-y" x="380" y="50" width="140" height="80" rx="8"/><text class="lbl" x="450" y="86" text-anchor="middle">Payments</text><text class="soft" x="450" y="108" text-anchor="middle">200 threads</text>
  <rect class="bx-r" x="600" y="50" width="140" height="80" rx="8"/><text class="lbl" x="670" y="86" text-anchor="middle">Bank API</text><text class="soft" x="670" y="108" text-anchor="middle">not ours</text>
  <path class="ln" d="M110 90 H178" marker-end="url(#a)"/><path class="ln" d="M310 90 H378" marker-end="url(#a)"/><path class="ln" d="M520 90 H598" marker-end="url(#a)"/>
  <text class="soft" x="344" y="78" text-anchor="middle">100/s</text><text class="soft" x="560" y="78" text-anchor="middle">100/s</text>
  <text class="soft" x="560" y="150" text-anchor="middle">200 ms</text><text class="soft" x="560" y="170" text-anchor="middle">on a normal day</text>
  <text class="soft" x="450" y="24" text-anchor="middle">this deep dive stands here</text><path class="ln-d" d="M450 30 V46" marker-end="url(#a)"/>
'''
recap = '''
<p>The circuit breaker note told a story: Checkout calls Payments, Payments calls the Bank API, the bank has a slow day and the whole shop goes down. Four notes each offered a defence.</p>
''' + tbl(["Note", "In one line", "The question it asks before a call"], [
    ["Retry with Backoff", "try again, politely, a limited number of times", "is another attempt worth it?"],
    ["Circuit Breaker", "stop calling what keeps failing", "is the dependency healthy right now?"],
    ["Bulkhead", "a separate, limited pool per dependency", "is there room for one more call?"],
    ["Rate Limiter", "cap what each client may send", "has this client had its share?"],
]) + fig(760, 185, "The call chain used in this deep dive. A shopper calls Checkout, which waits three seconds at most. Checkout calls Payments at 100 requests a second. Payments has 200 threads and calls the Bank API, which is outside our control and answers in 200 milliseconds on a normal day. The deep dive looks at the system from inside Payments.",
          chain_svg, "We stand inside Payments: a caller of the bank, and a server for Checkout.") + mn("Every note said “pairs with” the other three. None said how.") + '''
<p class="full">Each pattern works alone in its note. In a real service they are all switched on at once, on the same call, and they affect each other. Retries feed the breaker. The bulkhead changes what the timeout means. A rate limiter's rejection looks like a failure to a retry. Configured without regard for each other, they can make an outage longer. This deep dive is about the combination: the order they sit in, the numbers that must agree, and a fifth piece that had no note of its own, the timeout.</p>
'''

# ------------------------------------------------------------------ 2 overload
overload = '''
<p>A dependency that is down answers at once: connection refused. A dependency that is slow holds on to you. To see why that is worse, one formula is enough.</p>
<p><mark>Calls in flight = arrival rate × time each call takes.</mark></p>
''' + tbl(["Bank answers in", "Calls in flight in Payments", "With 200 threads"], [
    ["200 ms (normal)", "100/s × 0.2 s = <b>20</b>", "180 threads idle"],
    ["1 s", "100/s × 1 s = <b>100</b>", "half used, nobody notices"],
    ["2 s", "100/s × 2 s = <b>200</b>", "exactly full"],
    ["10 s (bad day)", "100/s × 10 s = <b>1,000</b> wanted", "full after 2 seconds; the rest queue"],
], hot=(3,)) + mn("This is Little's law from the bulkhead note. It predicts the outage to the second.") + '''
<p>Nothing crashed and no error was logged. Latency went up by a factor of fifty, so the number of calls in flight tried to go up by a factor of fifty, and the pool was sized for a factor of ten.</p>
<h3>The outage, minute by minute, with no protection</h3>
''' + tbl(["Time", "What happens"], [
    ["12:00:00", "the bank slows from 200 ms to 10 s"],
    ["12:00:02", "all 200 Payments threads are waiting on the bank; new requests queue"],
    ["12:00:05", "Checkout's calls to Payments get no answer; Checkout's own threads fill"],
    ["12:00:15", "shoppers see spinners and press refresh; arrivals rise from 100/s to 180/s"],
    ["12:01", "browsing, the cart and search are down too: they share Checkout's threads"],
    ["12:05", "the bank recovers and answers in 200 ms again"],
    ["12:05 →", "the shop stays down"],
], hot=(6,), mono=(0,)) + full('''<h3>Why it stays down after the bank is back</h3>
<p>At 12:05 Payments holds a long queue of requests. Most belong to shoppers who gave up minutes ago. It works through them anyway, in the order they arrived, so the fresh requests wait at the back and time out too. Their callers retry, which adds more. If the backlog plus the retries arrive faster than the pool can clear them, the service is busy for ever and useful for no one.</p>
<p>That state has a name: a <b>metastable failure</b>. The trigger is gone, and the system keeps itself down with its own traffic. It usually ends when a person restarts things or blocks traffic at the door.</p>
<p>The four patterns, plus timeouts, each remove one link of this chain.</p>
''' + tbl(["Link in the chain", "Removed by"], [
    ["a call may wait 10 s", "timeout"],
    ["one slow dependency takes every thread", "bulkhead"],
    ["we keep sending calls to something that is failing", "circuit breaker"],
    ["a failed call is repeated at once, by every layer", "retry with backoff, limited by a budget"],
    ["more arrives than we can ever serve", "rate limiter and load shedding"],
    ["we do work nobody is waiting for", "deadlines"],
]))

# ------------------------------------------------------------------ 3 timeouts and deadlines
timeouts = '''
<p>The timeout never got its own note, and every other pattern depends on it. A breaker counts failures, and a call that never returns is never counted. A bulkhead frees a slot when a call ends, and a call with no timeout may not end. Start here.</p>
<h3>Choosing a timeout</h3>
''' + tbl(["If you set it", "Then"], [
    ["far above normal (30 s “to be safe”)", "it never fires in time to protect anything. This is the default in many HTTP clients"],
    ["at the average (200 ms)", "half of all healthy calls fail. You have built your own outage"],
    ["just above the slow-but-healthy case (1 s, with 99 % of calls under 800 ms)", "healthy calls pass, sick ones are cut early"],
], hot=(2,)) + mn("Two timeouts, really: one to connect (short, 100–300 ms) and one to get the answer.") + '''
<p>Use the measured slow case of the dependency, the time under which 99 in 100 calls finish, and add a margin. Review it when the dependency changes.</p>
<h3>A timeout is local. A deadline is shared</h3>
<p>The shopper will wait about 3 seconds. That is the only number that matters to them, and it has to be divided along the chain. A <b>deadline</b> is that budget, passed with the request so every service knows how much is left.</p>
''' + code("deadline.ts", "pass the time that is left", '''
// Checkout: the shopper waits 3 s at most
const res = await payments.charge(order, { timeLeftMs: 3_000 });

// Payments: read the budget, refuse work that cannot finish in time
const left = Number(req.headers["x-time-left-ms"]) - timeSpentHere();
if (left < 300) return res.status(504).end();     // too late to be useful

// give the bank what is left, minus time to send our own answer
const bankTimeout = Math.min(1_000, left - 200);
''') + full('''<p>Two things happen here that a plain timeout cannot do. Payments refuses work that is already too late, which costs almost nothing. And the bank call gets the smaller of its usual timeout and the time actually left, so a request that has already spent 2.5 seconds waiting does not start a fresh one-second attempt.</p>
<p>Send the time that is left, not a clock time. Two servers rarely agree on the time to the millisecond, and a duration does not need them to.</p>
<h3>The rule the numbers must obey</h3>
<p><mark>Every inner time limit is shorter than the limit of whoever is waiting for it.</mark> Checkout waits 3 s for Payments. Then everything Payments does, all attempts and all waits between them, must fit inside 3 s with room to answer. Chapter 7 does the sum. Drill 2 shows what happens when it is the other way round.</p>
<h3>Stop the work, too</h3>
<p>When a timeout fires, the caller stops waiting. The callee often keeps going: the query runs to the end, the bank call completes, and the result is thrown away. Where the platform allows it, cancel on timeout: close the connection, abort the request, cancel the query. Otherwise the timeout protects the caller and leaves the load exactly where it was.</p>''')

# ------------------------------------------------------------------ 4 the stack
stack_svg = '''
  <text class="soft" x="250" y="22" text-anchor="middle">inside Payments, around one call to the bank</text>
  <rect class="bx" x="10" y="40" width="86" height="60" rx="8"/><text class="lbl" x="53" y="76" text-anchor="middle">deadline</text>
  <rect class="bx" x="112" y="40" width="86" height="60" rx="8"/><text class="lbl" x="155" y="76" text-anchor="middle">retry</text>
  <rect class="bx-r" x="214" y="40" width="86" height="60" rx="8"/><text class="lbl" x="257" y="76" text-anchor="middle">breaker</text>
  <rect class="bx" x="316" y="40" width="86" height="60" rx="8"/><text class="lbl" x="359" y="76" text-anchor="middle">timeout</text>
  <rect class="bx-y" x="418" y="40" width="86" height="60" rx="8"/><text class="lbl" x="461" y="76" text-anchor="middle">bulkhead</text>
  <path class="ln" d="M96 70 H110" marker-end="url(#a)"/><path class="ln" d="M198 70 H212" marker-end="url(#a)"/><path class="ln" d="M300 70 H314" marker-end="url(#a)"/><path class="ln" d="M402 70 H416" marker-end="url(#a)"/>
  <path class="ln" d="M504 70 H568" marker-end="url(#a)"/><path class="ln-d" d="M536 30 V150"/><text class="soft" x="536" y="170" text-anchor="middle">network</text>
  <rect class="bx-g" x="570" y="40" width="86" height="60" rx="8"/><text class="lbl" x="613" y="68" text-anchor="middle">rate</text><text class="lbl" x="613" y="88" text-anchor="middle">limit</text>
  <path class="ln" d="M656 70 H672" marker-end="url(#a)"/>
  <rect class="bx" x="674" y="40" width="76" height="60" rx="8"/><text class="lbl" x="712" y="76" text-anchor="middle">Bank</text>
  <text class="soft" x="53" y="124" text-anchor="middle">any time</text><text class="soft" x="53" y="142" text-anchor="middle">left?</text>
  <text class="soft" x="155" y="124" text-anchor="middle">worth one</text><text class="soft" x="155" y="142" text-anchor="middle">more try?</text>
  <text class="soft" x="257" y="124" text-anchor="middle">is it</text><text class="soft" x="257" y="142" text-anchor="middle">healthy?</text>
  <text class="soft" x="359" y="124" text-anchor="middle">this try</text><text class="soft" x="359" y="142" text-anchor="middle">too slow?</text>
  <text class="soft" x="461" y="124" text-anchor="middle">room in</text><text class="soft" x="461" y="142" text-anchor="middle">the pool?</text>
  <text class="soft" x="613" y="124" text-anchor="middle">had your</text><text class="soft" x="613" y="142" text-anchor="middle">share?</text>
'''
stack = '''
<p>All five pieces wrap the same call, so they have to be nested, and the nesting order changes the behaviour.</p>
''' + fig(760, 180, "The order of the layers around one call from Payments to the bank. Inside Payments, from outside to inside: deadline, retry, circuit breaker, timeout, bulkhead. Then the network. On the bank's side: a rate limiter, then the bank itself. Each layer asks one question: any time left, worth one more try, is it healthy, is this try too slow, is there room in the pool, has this client had its share.",
          stack_svg, "Read left to right: each layer can say no before the next one is asked.") + code("call-bank.ts", "the same order, in code", '''
const callBank = (req, deadline) =>
  retry({ attempts: 2, budget, deadline }, () =>    // worth one more try?
    breaker.run(() =>                               // is the bank healthy?
      withTimeout(Math.min(1_000, deadline.left()), // this try too slow?
        () => bulkhead.run(() =>                    // room in the pool?
          bank.charge(req)))));
''') + '''
<h3>Why this order</h3>
''' + tbl(["Decision", "Reason"], [
    ["Retry <b>outside</b> the breaker", "each attempt asks the breaker first. When the breaker is open, the attempt fails at once and the retry stops: an open breaker is not a reason to try again"],
    ["Breaker <b>outside</b> the timeout", "a timed-out attempt is reported to the breaker as a failure. Slow counts as broken"],
    ["Timeout <b>outside</b> the bulkhead", "time spent waiting for a free slot counts against the attempt, so nothing waits unseen"],
    ["Deadline around everything", "attempts, waits and queueing together may not exceed what the caller gave us"],
]) + mn("Most libraries let you choose the order, and their default is not always this one. Check.") + full('''<h3>Who sees which error</h3>
<p>The layers pass errors outward, and each must decide what an error means. This table is where most misconfigurations live.</p>
''' + tbl(["What came back", "Retry it?", "Count it against the breaker?"], [
    ["timeout, connection reset, 502, 503, 504", "yes, if the call is safe to repeat and time is left", "yes"],
    ["429 from the bank", "yes, after the wait it names", "no: the bank is healthy, we are over our share"],
    ["400, 401, 404, 409", "no, it will fail the same way", "no: the bank answered correctly"],
    ["“circuit open” from our own breaker", "no. Go to the fallback", "not applicable"],
    ["“pool full” from our own bulkhead", "no", "no: it is our limit, not the bank's failure"],
], hot=(1, 4)) + '''<p>The two tinted rows are the common mistakes. Counting 429s as failures opens the breaker on a healthy dependency. Retrying a “pool full” error puts more pressure on a pool that has just said it has no room.</p>
<h3>Two sides of the wire</h3>
<p>Deadline, retry, breaker, timeout and bulkhead live in the <b>caller</b> and protect it from a bad dependency. The rate limiter lives in the <b>server</b> and protects it from its callers. Payments is both, so it needs both sets: the client stack toward the bank, and limits at its own front door for Checkout (chapter 8).</p>''')

# ------------------------------------------------------------------ 5 drills
drills = mn("As before: cover the lower half of each card and guess.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · retry storm</a></li><li><a href="#drill-2">2 · timeouts upside down</a></li><li><a href="#drill-3">3 · one big breaker</a></li>
  <li><a href="#drill-4">4 · the stampede back</a></li><li><a href="#drill-5">5 · the fallback falls</a></li><li><a href="#drill-6">6 · the long queue</a></li>
</ul>
''' + drill(1, "Three layers, three attempts each", [
    ("Timeline", "The bank drops requests for two seconds. Payments retries each bank call 3 times. Checkout retries each Payments call 3 times. The shop's web client retries each Checkout call 3 times."),
    ("What you see", "One click can become 3 × 3 × 3 = 27 calls to the bank. The bank, which was recovering from a two-second blip, now receives many times its normal traffic and stays down for ten minutes.", True),
    ("Why", "Each layer's retry policy looks reasonable alone. Multiplied, they turn every failure into more load, at the moment the dependency can least take it.", True),
    ("What saves you", "Retry in <b>one</b> layer, the one next to the failure, and have the others pass the error up. Cap retries with a budget: at most 10 % extra calls, however many fail (chapter 6). And let the breaker cut retries off entirely once the bank is clearly down."),
], "retries multiply through layers. Retry once, in one place, inside a budget.") + drill(2, "The inner timeout is longer than the outer one", [
    ("Timeline", "Checkout waits 2 s for Payments. Payments waits 10 s for the bank. The bank takes 5 s. At 2 s Checkout gives up and tries again. Payments is still working on the first request, and now on the second."),
    ("What you see", "Payments does every piece of work twice or more, and none of it reaches a shopper. Its threads fill with requests that nobody is waiting for. From Checkout's side, Payments “always times out”.", True),
    ("What saves you", "The rule from chapter 3: inner limits are shorter than outer ones, and they come from one shared budget. With a deadline in the request, Payments knows at second 2 that its caller has gone, and stops."),
], "a timeout longer than your caller's patience buys work that nobody will collect.") + drill(3, "One breaker for the whole bank", [
    ("Timeline", "The bank's <code>/refund</code> endpoint breaks. Refunds are 5 % of calls. Either the single breaker around “the Bank API” never trips, because 5 % failures is under its 50 % threshold, and refunds keep hanging. Or, on a quiet night when refunds dominate, it trips and blocks card charges that were working perfectly."),
    ("Why", "A breaker measures one thing. If that thing is a mixture, the measurement describes none of its parts.", True),
    ("What saves you", "One breaker per thing that fails on its own: per dependency <i>and</i> per operation where they differ, so <code>bank.charge</code> and <code>bank.refund</code> each get one. Add a minimum number of calls before the breaker may judge, so two failures at 3 a.m. are not “100 % failing”."),
], "a breaker should wrap one thing that fails as a unit. No more, no less.") + drill(4, "Everyone comes back at once", [
    ("Timeline", "The bank is down for five minutes. All 20 Payments instances have open breakers with the same 30-second cool-down, so they test at the same moments. The bank returns. Twenty breakers close in the same second and the full traffic, plus everything callers saved up to retry, lands on a bank that has just restarted."),
    ("What you see", "The bank falls over again. Breakers open. Thirty seconds later, the same thing. The graph looks like a saw.", True),
    ("What saves you", "Make recovery gradual. In the half-open state allow only a few trial calls. Add a random part to the cool-down so instances do not test together. And keep the bulkhead: even with the breaker closed, it caps how many calls are in flight, so the return is a slope and not a wall."),
], "plan the recovery as carefully as the failure. Closing is the dangerous moment.") + drill(5, "The fallback was never tested", [
    ("Timeline", "The breaker opens, as designed. The fallback for “bank unavailable” is to call a second payment provider. That path has not run in production for eight months. Its credentials expired in March."),
    ("What you see", "The primary fails cleanly and the fallback fails messily: slow, with errors nobody has seen before, and with no breaker or timeout of its own, because it was “only the fallback”.", True),
    ("What saves you", "Prefer fallbacks that cannot fail: a cached value, a default, “we'll confirm by email” with the request saved to a queue. If the fallback is another remote call, it needs its own full stack, and it must be exercised regularly, for example by sending 1 % of real traffic through it. Alert on the fallback rate, or a silent fallback will hide the outage from you."),
], "a fallback is code that runs only on your worst day. Keep it simple, and run it on ordinary days too.") + drill(6, "The queue that hides the problem", [
    ("Timeline", "To “avoid rejecting customers”, the Payments bulkhead gets a waiting queue of 10,000. The bank slows down. The queue fills. A request now waits 50 seconds in the queue before it is even attempted."),
    ("What you see", "No errors on the dashboard, which looks like success. Every shopper has left long before their request is served, and every answer is produced for nobody. When the bank recovers, Payments spends minutes working through dead requests.", True),
    ("Why", "A queue turns “no” into “later”. That helps for a burst of a few milliseconds. For anything longer it converts fast failures into slow ones and stores the overload for afterwards.", True),
    ("What saves you", "Keep queues short: a few tens of milliseconds of work. When full, reject at once. Check the deadline when a request leaves the queue and drop it if its time has passed. Under overload, serve the newest request first: its shopper is the one still waiting."),
], "a long queue is a slow way to say no. Say it fast instead.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Agreement between the parts", "Drill"], [
    ["retries happen in one layer and inside a budget", "1"],
    ["time limits shrink as you go inward, from one shared deadline", "2"],
    ["each breaker and each pool wraps one thing that fails as a unit", "3"],
    ["recovery is gradual and staggered", "4"],
    ["fallbacks are simple, protected and exercised", "5"],
    ["queues are short, and waiting requests can expire", "6"],
]))

# ------------------------------------------------------------------ 6 retries and load
retries = '''
<p>A retry is the only pattern in the stack that <b>adds</b> load. All the others remove it. That makes retries the part most likely to turn a small failure into a large one, and the part that most needs a limit that does not depend on luck.</p>
<h3>What “3 attempts” does on a bad day</h3>
''' + tbl(["Bank failure rate", "Calls sent with “up to 3 attempts”", "Load on the bank"], [
    ["1 % (a normal blip)", "100 + about 1 retry", "× 1.01"],
    ["50 %", "100 + 50 + 25", "× 1.75"],
    ["100 % (it is down)", "100 + 100 + 100", "× 3"],
], hot=(2,)) + mn("The more it fails, the more we send. Exactly backwards.") + '''
<p>A fixed attempt count behaves well when things are fine and badly when they are not. Through three layers the last row becomes × 27 (drill 1).</p>
<h3>The retry budget</h3>
<p>A budget ties retries to successes. Every successful call earns a small credit. Every retry spends a whole one. When the credit runs out, there are no more retries until successes return.</p>
''' + code("retry-budget.ts", "retries are at most 10 % of traffic", '''
class RetryBudget {
  private tokens = 10;
  onSuccess() { this.tokens = Math.min(10, this.tokens + 0.1); }  // 10 successes earn 1 retry
  tryToSpend() {
    if (this.tokens < 1) return false;   // budget empty: do not retry
    this.tokens -= 1;
    return true;
  }
}
''') + tbl(["Bank failure rate", "With a 10 % budget", "Load on the bank"], [
    ["1 %", "every failure gets its retry", "× 1.01"],
    ["50 %", "retries capped", "× 1.1 at most"],
    ["100 %", "no successes, so no credit, so no retries", "× 1.0"],
], hot=(2,)) + full('''<p>On a normal day nothing changes: the occasional blip is retried and the shopper never knows. On a bad day the retries fade out by themselves, which is the behaviour you would have chosen by hand.</p>
<h3>The rest of a safe retry</h3>
''' + tbl(["Rule", "From", "Why it matters in the stack"], [
    ["Only where a repeat is safe", "Reliable Messaging dive", "a charge needs an idempotency key, or the retry charges twice"],
    ["Growing waits with a random part", "Retry note", "spreads the retries so they do not arrive as one spike"],
    ["Honour <code>Retry-After</code>", "Rate Limiter note", "the server is telling you when it can take you"],
    ["Stay inside the deadline", "chapter 3", "do not start an attempt that cannot finish in the time left"],
    ["In one layer only", "drill 1", "the layer next to the failure knows best whether a repeat can help"],
]) + '''<h3>Which layer retries?</h3>
<p>In our chain, Payments retries the bank call, because it holds the idempotency key and knows which bank errors are temporary. Checkout does not retry Payments. If Payments answers 503, Checkout shows “please try again” and lets the shopper decide. The web client retries only when the request never reached the server at all.</p>
<p>A shopper pressing the button again is also a retry. The idempotency key from the checkout page makes it safe, and a clear, fast error makes it less likely to be pressed five times.</p>''')

# ------------------------------------------------------------------ 7 numbers
numbers = '''
<p>The patterns are easy to switch on and hard to configure. This chapter works the numbers for the call from Payments to the bank, starting from three measurements.</p>
''' + tbl(["Measured on a normal day", "Value"], [
    ["Calls to the bank", "100 a second"],
    ["Typical answer time", "200 ms"],
    ["Slow but healthy (99 in 100 calls are faster)", "800 ms"],
    ["What Checkout gives us", "3 s"],
]) + '''
<h3>The settings, each derived from the one before</h3>
''' + tbl(["Setting", "Reasoning", "Value"], [
    ["<b>Timeout</b> per attempt", "a little above slow-but-healthy", "1 s"],
    ["<b>Attempts</b>", "one retry covers a blip; more only helps if the bank is down, and then it hurts", "2"],
    ["<b>Wait</b> between them", "random, up to 200 ms", "0–200 ms"],
    ["<b>Worst case</b> in total", "1 s + 0.2 s + 1 s = 2.2 s. Must be under 3 s with room to answer", "fits, 0.8 s spare"],
    ["<b>Retry budget</b>", "at most 10 % extra", "10 %"],
    ["<b>Bulkhead</b>", "normal need is 100 × 0.2 = 20 in flight. Allow double for bursts; far below the 200 threads", "40"],
    ["<b>Breaker</b> window", "long enough to hold plenty of calls: 10 s is about 1,000", "10 s"],
    ["Breaker opens at", "half the calls failing or slower than the timeout, with at least 50 calls seen", "50 %, min 50"],
    ["Breaker cool-down", "long enough for a restart; random spread so instances differ", "30 s ± 5 s"],
    ["Half-open trial", "a handful of calls, all must pass", "5"],
]) + mn("If the worst case had not fitted in 3 s, the fix is fewer attempts or a shorter timeout. Never a longer deadline nobody agreed to.") + full('''<h3>Check it against the bad day</h3>
<p>Replay chapter 2 with these settings. The bank slows to 10 s at 12:00:00.</p>
''' + tbl(["Time", "What happens now"], [
    ["12:00:00", "bank slows to 10 s"],
    ["12:00:00.4", "the bulkhead's 40 slots are full; further bank calls are refused in microseconds. 160 threads stay free"],
    ["12:00:01", "the first calls hit the 1 s timeout and are reported to the breaker"],
    ["12:00:01.5", "50 calls seen, all failed: the breaker opens. Bank calls now fail instantly; the retry budget is empty"],
    ["12:00:02 →", "Payments answers every request within milliseconds: “payment is unavailable, your basket is saved”"],
    ["12:00:31", "half-open: 5 trial calls, all time out, breaker opens again"],
    ["12:05:35", "the bank is back: the trial passes, the breaker closes, traffic returns under the 40-slot cap"],
], mono=(0,)) + '''<p>Payments was degraded for five and a half minutes and never down. Checkout kept its threads, so browsing and the cart never noticed. Nothing had to be restarted.</p>
<h3>Numbers that drift</h3>
<p>Every value above came from a measurement, and measurements change. The bank adds a fraud check and its slow case moves from 800 ms to 1.4 s: the 1 s timeout now cuts healthy calls. Traffic doubles: the bulkhead of 40 is now the normal load. Put the three inputs on a dashboard next to the settings, and look again whenever one of them moves by a quarter.</p>''')

# ------------------------------------------------------------------ 8 server side
shedding = '''
<p>So far Payments has protected itself from the bank. It also has to protect itself from its own callers. The rate limiter note covered one tool. There are two, and they answer different questions.</p>
''' + tbl(["", "Rate limiter", "Load shedder"], [
    ["Question", "has <i>this client</i> had its share?", "can <i>we</i> take any more right now?"],
    ["Counts", "requests per client key, per period", "what is in flight in the whole service, or how long requests wait"],
    ["Protects against", "one client taking everything", "everyone together sending too much"],
    ["Answers", "<code>429</code> with <code>Retry-After</code>", "<code>503</code> with <code>Retry-After</code>"],
    ["Fires when", "a client misbehaves, even on a quiet day", "the service is overloaded, even if every client behaves"],
]) + mn("A rate limiter is about fairness. A load shedder is about survival. You want both.") + '''
<h3>Shed by priority</h3>
<p>When Payments cannot serve everything, it should choose what to drop. Decide the order on a calm day.</p>
''' + tbl(["Priority", "Work", "Under overload"], [
    ["1", "charge for a checkout in progress", "served to the last"],
    ["2", "refunds, payment status lookups", "served while there is room"],
    ["3", "the nightly settlement report, admin exports", "refused first"],
]) + '''
<p>A simple shedder uses the calls-in-flight number from chapter 2. With 200 threads, it might refuse priority 3 above 120 in flight, priority 2 above 160, and keep the last 40 for charges.</p>
''' + full('''<h3>Make “no” cheap</h3>
<p>A rejection only helps if it costs far less than the work it replaces. Reject as early as possible: at the gateway or in the first lines of the handler, before parsing the body, before opening a transaction, before calling anything. A service that spends half the cost of a request on refusing it has not shed much.</p>
<h3>Limits that set themselves</h3>
<p>A fixed “160 in flight” is right until the hardware, the code or the bank changes. An <b>adaptive limit</b> watches response time and adjusts. While answers stay fast it raises the limit a little. When they slow down it cuts the limit sharply. It finds the capacity the service has today, with no number to maintain. Several libraries and proxies offer it. Use it once the fixed limits are in place and understood.</p>
<h3>Degrade in steps</h3>
<p>Between “everything works” and “down” there is a ladder, and a good system steps down it one rung at a time.</p>
''' + tbl(["Rung", "The shopper sees"], [
    ["0 · normal", "everything"],
    ["1 · extras off", "no recommendations, no “recently viewed”"],
    ["2 · stale data", "prices and stock from the cache, marked “updated 5 minutes ago”"],
    ["3 · work deferred", "“order received, we'll confirm payment by email”"],
    ["4 · honest refusal", "“checkout is busy, your basket is saved, try again in a minute”"],
]) + '''<p>Each rung is a fallback from one of the breakers or a rule in the shedder. Written as a list, it is something product and engineering can agree on before the bad day.</p>''')

# ------------------------------------------------------------------ 9 testing and running
testing = '''
<p>Resilience code runs only when something is wrong, so on a normal day it is untested by definition. You have to make things go wrong on purpose.</p>
<h3>Inject slowness, not only errors</h3>
<p>Most tests fake a dependency that returns an error. Chapter 2 showed that the dangerous failure is the slow one. Put a small proxy between Payments and a fake bank and let the test turn dials on it.</p>
''' + tbl(["Dial", "Checks"], [
    ["add 5 s of delay", "timeout fires at 1 s; bulkhead refuses call 41; the caller gets an answer inside its deadline"],
    ["fail 100 % for 20 s", "breaker opens after 50 calls; retries stop; fallback answers"],
    ["fail 100 %, then heal", "breaker half-opens, passes 5 trials, closes; traffic returns under the cap"],
    ["fail 30 % at random", "retries hide the failures; extra load stays under 10 %"],
    ["answer <code>429</code> with <code>Retry-After: 2</code>", "the client waits 2 s; the breaker does not count it"],
    ["accept the connection, then send nothing", "the answer timeout fires, not only the connect timeout"],
]) + mn("The last one catches the most bugs. Many clients only time out on connecting.") + full(code("bank-slow.test.ts", "the bad day, as a test", '''
test("a slow bank does not take Payments down", async () => {
  bankProxy.addDelay(10_000);
  const results = await sendCharges({ perSecond: 100, forSeconds: 5 });

  expect(results.slowerThan(3_000)).toBe(0);          // every caller got an answer in time
  expect(pool.maxInFlight("bank")).toBeLessThanOrEqual(40);
  expect(breaker.state("bank.charge")).toBe("OPEN");
  expect(results.status(503)).toBeGreaterThan(400);   // fast, honest refusals
});
''') + '''<h3>What to graph, per dependency</h3>
''' + tbl(["Graph", "Tells you"], [
    ["answer time, typical and slow case", "whether the timeout still sits in the right place"],
    ["calls in flight against the bulkhead limit", "how close you are to refusing"],
    ["refusals, split by reason: timeout, breaker open, pool full, rate limited, shed", "which layer is doing the protecting. One number for “errors” hides this"],
    ["retries as a share of calls", "whether the budget is being hit"],
    ["breaker state changes", "each open is an event worth a line in the incident channel"],
    ["fallback rate", "how many shoppers are getting the degraded experience"],
]) + '''<h3>Runbook: “everything is slow”</h3>
<ol>
  <li><b>Find the pool that is full.</b> The calls-in-flight graph points at the dependency. Slow everywhere usually means one dependency without a bulkhead.</li>
  <li><b>Check that the protections fired.</b> Is its breaker open? Are refusals fast? If calls are still hanging, a timeout is missing or too long.</li>
  <li><b>Look at retries.</b> A retry share far above 10 % means some layer has no budget and is feeding the problem.</li>
  <li><b>Shed by hand if needed.</b> Force the breaker open or lower a limit with a switch. Having that switch ready is part of the design.</li>
  <li><b>Watch the return.</b> When the dependency heals, traffic should come back as a slope. A saw-tooth is drill 4.</li>
</ol>
<h3>Practise</h3>
<p>Once a quarter, on a quiet afternoon and with everyone told, slow the real bank connection in a test environment or for a small share of production traffic, and watch. The first run nearly always finds a client with a default timeout of 30 seconds or none at all.</p>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>Where the stack can live</h3>
''' + tbl(["", "In the service (a library)", "Beside it (proxy or service mesh)", "In front (API gateway)"], [
    ["Timeouts, retries", "yes", "yes", "yes"],
    ["Circuit breaker", "yes, with a fallback you write", "yes: it stops sending to failing instances", "sometimes"],
    ["Bulkhead", "yes, per dependency or operation", "connection and request caps", "no"],
    ["Rate limit, shedding", "possible", "yes", "yes: the usual place"],
    ["Knows if a call is safe to repeat", "yes", "no, unless you tell it", "no"],
    ["Can serve a fallback", "yes", "no", "only a static answer"],
    ["Same behaviour in every language", "one library per language", "yes", "yes"],
], hot=(4, 5)) + mn("The mesh can refuse and repeat. Only the service knows what to do instead.") + full('''<p>The two tinted rows decide the split. Anything that needs business knowledge, such as whether a charge may be repeated or what to show when recommendations are missing, belongs in the service. Uniform plumbing, such as a default timeout on every call or removing a bad instance from rotation, is a good job for a proxy.</p>
<p>The risk in using both is drill 1 by another route: the library retries twice and the proxy retries twice, and nobody planned for four. Decide which one owns retries and switch them off in the other.</p>''') + '''
<h3>Lab</h3>
<p>Checkout makes two calls while it builds the confirmation page. Design the stack for each.</p>
''' + tbl(["Call", "Normal", "Slow but healthy", "If it fails"], [
    ["<b>Recommendations</b>: “you may also like”", "50 ms", "150 ms", "the page is a little emptier"],
    ["<b>Payments</b>: charge the card", "300 ms", "1.2 s", "there is no order"],
]) + '''
<ol class="keep">
  <li>Checkout has 3 s in total and calls Payments first. What timeout does each call get?</li>
  <li>Which of the two calls gets retries, and how many?</li>
  <li>What is the fallback for each?</li>
  <li>Both calls currently share one HTTP connection pool of 100. What do you change, and to what sizes at 100 requests a second?</li>
  <li>Under overload, which call does Checkout drop first?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · Timeouts</summary><p>Payments: about 1.5 s per attempt, a little above its slow case. Recommendations: 200 ms. It is optional, so it gets a small, fixed slice and never more than the time left. If Payments used most of the budget, skip the Recommendations call entirely.</p></details>
<details><summary>2 · Retries</summary><p>Recommendations: none. A retry would cost more time than the feature is worth; go straight to the fallback. Payments: Checkout does not retry it either, because Payments already retries the bank (one layer only). Checkout passes the idempotency key so that a shopper's second click is safe.</p></details>
<details><summary>3 · Fallbacks</summary><p>Recommendations: an empty list or the cached bestsellers, which cannot fail. Payments: no silent fallback exists for taking money. Save the basket and answer quickly and clearly, or accept the order as “payment pending” if the business has agreed to that rung of the ladder.</p></details>
<details><summary>4 · Pools</summary><p>Split them, so slow recommendations can never take a connection that a payment needs. Payments: 100 × 0.3 s = 30 in flight normally, so about 60. Recommendations: 100 × 0.05 s = 5, so about 10. The small pool is the point: when Recommendations slows down, the eleventh call is refused at once and the page renders without it.</p></details>
<details><summary>5 · Shedding</summary><p>Recommendations first, at the first sign of pressure. It is rung 1 of the ladder. Its breaker should also be quick to open, because nobody is harmed when it does.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Time", ["Every remote call has a connect timeout and an answer timeout", "Timeouts sit just above the dependency's slow-but-healthy time", "A deadline travels with the request, as time left", "Inner limits are shorter than outer ones; the worst case is added up and fits", "Work is cancelled when its timeout fires"]),
    ("Retries", ["Exactly one layer retries each call", "A budget caps retries at about 10 % of traffic", "Only calls that are safe to repeat are retried", "Waits grow, are random, and respect Retry-After and the deadline"]),
    ("Breakers and pools", ["One breaker and one pool per thing that fails as a unit", "The breaker needs a minimum number of calls before it judges", "429s, 4xx answers and our own refusals do not count as failures", "Pool sizes come from rate × time, with headroom, and are far below the thread count", "Queues are short and waiting requests can expire"]),
    ("Recovery and fallbacks", ["Half-open lets a few calls through; cool-downs are staggered", "Every breaker has a fallback, or a decision that there is none", "Fallbacks are local where possible, protected where not, and run on ordinary days", "The steps of degradation are written down and agreed"]),
    ("At the front door", ["Per-client rate limits answer 429 with Retry-After", "A load shedder refuses by priority when the service is full", "Refusing is much cheaper than serving"]),
    ("Tests and operations", ["A test makes the dependency slow, not only failing", "Refusals are graphed by reason, per dependency", "Breaker openings and the fallback rate raise alerts", "There are switches to open a breaker or lower a limit by hand", "The settings are reviewed when traffic or latency moves by a quarter"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="resilience-stack", no=3, title="The Resilience Stack",
    sub="Timeouts, retries, circuit breakers, bulkheads and rate limits on the same call: the order they sit in, the numbers that must agree, and what happens when they don't.",
    summary="A deep dive on combining timeouts, retries, circuit breakers, bulkheads and rate limiters: overload and metastable failure, deadlines, layer order, six failure drills, retry budgets, tuning with numbers, load shedding, testing and operations.",
    builds_on="Vol. 1, notes 01–04",
    builds_on_links=[("Circuit Breaker", "../../distributed/notes/circuit-breaker.html"), ("Retry with Backoff", "../../distributed/notes/retry-backoff.html"),
                     ("Bulkhead", "../../distributed/notes/bulkhead.html"), ("Rate Limiter", "../../distributed/notes/rate-limiter.html")],
    notes=[("distributed", "circuit-breaker"), ("distributed", "retry-backoff"), ("distributed", "bulkhead"), ("distributed", "rate-limiter")],
    facts=[("Example", "Checkout → Payments → Bank API, 100 requests a second")],
    blurb="Five protections on one call: overload, deadlines, the order of the layers, six failure drills, retry budgets, worked numbers and load shedding.",
    chapters=[
        dict(id="recap", nav="Recap", title="Four notes in sixty seconds",
             gist="Retry repeats a failed call, the circuit breaker stops calling what is broken, the bulkhead gives each dependency its own limited pool, and the rate limiter caps each client. Each works alone in its note. In a real service they all wrap the same call and affect each other, and that combination is the subject here.",
             body=recap),
        dict(id="overload", nav="Overload", title="Why slow is worse than down",
             gist="Calls in flight equal arrival rate times the time each call takes. When a dependency gets fifty times slower, the calls in flight try to grow fifty times, and the thread pool fills in seconds. After the dependency recovers, the backlog and the retries can keep the service down by themselves.",
             body=overload,
             check=[("Payments handles 100 requests a second and the bank answers in 500 ms. How many calls are in flight?", "100 × 0.5 = 50."),
                    ("The bank recovered ten minutes ago and Payments is still unusable. What is keeping it down?", "Its own traffic: a backlog of requests whose callers have gone, plus retries arriving on top. The trigger has ended, and the overload is sustaining itself.")]),
        dict(id="deadlines", nav="Deadlines", title="Timeouts and deadlines: the foundation",
             gist="Every other pattern depends on calls ending, so every call needs a timeout, set just above the dependency's slow-but-healthy time. A deadline is the caller's total budget, passed along as time left, so that inner limits are always shorter than outer ones and no one works for a caller who has gone.",
             body=timeouts,
             check=[("Why does a circuit breaker need timeouts in order to work?", "It counts completed calls. A call that hangs for ever is never counted as a failure, so the breaker never sees the problem."),
                    ("A request reaches Payments with 250 ms left. What should Payments do?", "Refuse it at once. A bank call takes 200 ms on a good day, and there would be no time left to send the answer.")]),
        dict(id="stack", nav="The stack", title="The stack, in order",
             gist="From outside to inside: deadline, retry, circuit breaker, timeout, bulkhead, then the call. Each layer can say no before the next is asked. The layers must also agree on what each error means: a rate-limit answer or a full pool is not a failure of the dependency, and an open breaker is not a reason to retry.",
             body=stack,
             check=[("What happens if the breaker sits outside the retry?", "The breaker sees one result for the whole retried operation. It learns about failures later, and each of those operations has already sent every attempt to the failing dependency."),
                    ("The bank answers 429 to a third of calls and the breaker opens. What is misconfigured?", "429 is being counted as a failure. The bank is healthy and asking us to slow down; the right response is to wait as it says.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways the protections make things worse when they are set without regard for each other: retries that multiply, timeouts upside down, one breaker around too much, everyone returning at once, a fallback that was never run, and a long queue that hides the overload.",
             body=drills,
             check=[("Checkout waits 2 s for Payments; Payments allows the bank 2 attempts of 1.5 s. Which drill is this, and what is the fix?", "Drill 2: the inner worst case (over 3 s) exceeds the outer limit. Shorten the attempts or drop the retry so the total fits inside 2 s."),
                    ("Your dashboard shows no errors during an incident, and shoppers are complaining. What do you look for?", "A queue. Requests are waiting a long time and then being served to nobody (drill 6), or a silent fallback is hiding the failure (drill 5).")]),
        dict(id="retries", nav="Retry budgets", title="Retries and load: the hard problem",
             gist="A retry is the only pattern that adds load. A fixed number of attempts sends the most extra traffic exactly when the dependency is failing most. A retry budget ties retries to successes, so they help with small blips and fade out by themselves in a real outage.",
             body=retries,
             check=[("With a 10 % budget and the bank completely down, how many retries are sent?", "Almost none. No successes means no credit is earned, so once the starting credit is spent the retries stop."),
                    ("Why should Payments, not Checkout, retry a failed bank call?", "Payments is next to the failure: it knows which bank errors are temporary and it holds the idempotency key. If both retried, the attempts would multiply.")]),
        dict(id="numbers", nav="Numbers", title="Tuning with numbers",
             gist="Start from three measurements: call rate, typical answer time and slow-but-healthy answer time. The timeout follows from the slow case, the pool size from rate times time, the attempts from the deadline, and the breaker's window from how many calls it needs to judge. Then replay the bad day against the settings.",
             body=numbers,
             check=[("The bank's slow-but-healthy time rises from 800 ms to 1.4 s. Which settings must change?", "The timeout (1 s now cuts healthy calls), then the worst-case sum against the 3 s deadline, which may force a single attempt. The pool size too, since calls take longer."),
                    ("Why is the bulkhead 40 and not 200?", "200 is every thread Payments has. A limit of 40 covers twice the normal need and leaves 160 threads for everything else when the bank is slow.")]),
        dict(id="shedding", nav="Shedding", title="The front door: rate limits and load shedding",
             gist="A rate limiter asks whether one client has had its share. A load shedder asks whether the service can take any more at all. You need both. Shed by priority, make refusing far cheaper than serving, and agree in advance on the steps by which the product degrades.",
             body=shedding,
             check=[("Every client is within its rate limit and the service is still overloaded. Which tool acts?", "The load shedder. The limits were set per client, and together the clients exceed today's capacity."),
                    ("Why answer 503 with <code>Retry-After</code> and not just close the connection?", "A clear, fast answer tells well-behaved clients when to come back and costs little. A dropped connection looks like a network fault and invites an immediate retry.")]),
        dict(id="testing", nav="Testing", title="Testing it and running it",
             gist="Resilience code runs only on bad days, so cause bad days in tests: slow the dependency, fail it, heal it. Graph refusals by reason for each dependency, alert on breaker openings and fallback rate, and keep switches to open a breaker or lower a limit by hand.",
             body=testing,
             check=[("Your tests fake a bank that returns errors. What have they missed?", "The slow case: timeouts, the bulkhead and the breaker's slow-call rule are never exercised, and those are what prevent the cascade."),
                    ("Refusals rise sharply and all of them are “pool full” for Recommendations. Is this an incident?", "Not for the shop. The bulkhead is doing its job and the page renders without recommendations. It is a ticket for the Recommendations team.")]),
        dict(id="tools", nav="Tools & lab", title="Where it lives, a lab and the checklist",
             gist="A library inside the service knows whether a call is safe to repeat and can serve a fallback. A proxy or mesh gives every service the same timeouts and limits. Use both, and make sure only one of them retries. The lab designs the stack for an optional call and a critical one.",
             body=tools),
    ],
    sources="Michael Nygard, <i>Release It!</i> (2nd ed., 2018), the stability patterns. Google, <i>Site Reliability Engineering</i> (2016), “Handling Overload” and “Addressing Cascading Failures”. Marc Brooker, “Timeouts, retries, and backoff with jitter”, and David Yanacek, “Using load shedding to avoid overload”, Amazon Builders' Library. Bronson and others, “Metastable Failures in Distributed Systems” (2021). Ben Maurer, “Fail at Scale” (2015), for queues under overload.",
)
