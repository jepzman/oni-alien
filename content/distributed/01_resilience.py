# Resilience collection: Retry with Backoff, Bulkhead, Rate Limiter.
# `Doodle` is injected by scripts/build_notes.py.

# ------------------------------------------------------------------ 02 Retry with Backoff
retry_problem = Doodle(760, 300, "Doodle of a retry storm: four clients all retry instantly at the same moment after a short blip, flooding the Orders service, which answers 503 and stays overloaded.",
                       "The blip lasted 200 ms. The instant, synchronised retries turned it into an outage.")
for i, y in enumerate([30, 95, 160, 225]):
    retry_problem.box(30, y, 110, 46, f"client {i + 1}", "paper", size=18)
    retry_problem.arrow(146, y + 23, 470, 150, color="red", label="retry NOW" if i in (0, 3) else None,
                        lx=300, ly=(y + 23 + 150) / 2 - 8 + (-6 if i == 0 else 10))
retry_problem.box(480, 100, 170, 100, "Orders", "pink", sub="503 · 503 · 503", stroke="red")
retry_problem.icon("hourglass", 690, 120, 1.2)
retry_problem.note(560, 236, "every client retries on the same beat", "red")
retry_problem.note(560, 262, "→ 4× the traffic exactly when it's weakest", "red")

retry_analogy = Doodle(760, 250, "Doodle of calling a busy pizza place: the first call is busy, then you wait 1 minute, then about 2, then about 4 before calling again, and the fourth call gets through. Neighbours wait slightly different times.",
                       "Wait longer each time, and not at exactly the same moment as everyone else.")
retry_analogy.icon("phone", 10, 70, 1.2)
retry_analogy.line("M90 130 H740")
for x, lab, ok in [(120, "call 1", False), (250, "call 2", False), (420, "call 3", False), (650, "call 4", True)]:
    retry_analogy.circle(x, 130, 30, "green" if ok else "pink", stroke="green" if ok else "red")
    retry_analogy.note(x, 190, lab)
    retry_analogy.head(x, 137, "✓" if ok else "busy", color="green" if ok else "red", size=17)
for x1, x2, lab in [(146, 224, "wait ~1 min"), (276, 394, "wait ~2 min"), (446, 624, "wait ~4 min")]:
    retry_analogy.arrow(x1, 98, x2, 98, curve=((x1 + x2) / 2, 50), label=lab, lx=(x1 + x2) / 2, ly=48)
retry_analogy.note(400, 232, "…and the neighbours wait 50 s, 70 s, 3 min — not all at once", "pen")

retry_how = Doodle(760, 230, "Timeline of four attempts. Each attempt has a 2 second timeout. Between attempts the caller sleeps a random time inside a window that doubles: up to 200 ms, 400 ms, then 800 ms. After the fourth failure it gives up and reports the error.",
                   "Each try has its own timeout; each wait is random inside a window that doubles.")
retry_how.line("M20 120 H740", color="soft")
for x, lab in [(30, "try 1"), (200, "try 2"), (390, "try 3"), (600, "try 4")]:
    retry_how.box(x, 92, 110, 56, lab, "blue")
    if x < 600:
        retry_how.note(x + 55, 176, "timeout 2 s")
for x1, x2, lab in [(140, 200, "rand(0–200 ms)"), (310, 390, "rand(0–400 ms)"), (500, 600, "rand(0–800 ms)")]:
    retry_how.arrow(x1, 84, x2, 84, curve=((x1 + x2) / 2, 40), dash=True, label=lab, lx=(x1 + x2) / 2, ly=34)
retry_how.box(500, 184, 250, 36, "give up → error + alert", "pink", stroke="red", size=17, rx=6)

RETRY = dict(
    slug="retry-backoff",
    kicker="a.k.a. “try again, but politely”",
    tldr="Most network failures are <b>short</b>. So try the call again, but only for errors that can succeed later, with a <b>timeout on every attempt</b>, a <b>growing, random wait</b> between attempts (exponential backoff + jitter), and a <b class=\"red\">hard limit</b> before giving up.",
    chips=[("Family", "resilience"), ("Lives in", "the caller (client, SDK or proxy)"), ("Also called", "exponential backoff, jitter"), ("Pairs with", "timeouts, idempotency keys, circuit breaker")],
    problem='''  <p class="lead">Networks are noisy. A packet gets dropped, a pod restarts during a deploy, a database pauses for a few hundred milliseconds. These <span class="hl-pink">transient failures</span> fix themselves a moment later.</p>
  <ul>
    <li>If the caller gives up on the first error, users see an error for something that would have worked half a second later.</li>
    <li>If the caller retries <b>instantly and forever</b>, every client hits the struggling service at the same moment. That's a <b>retry storm</b> (or “thundering herd”), and it keeps the service down.</li>
    <li>If a call has <b>no timeout</b>, it can hang forever, holding a thread, a connection and a user.</li>
    <li>If the call wasn't safe to repeat, a retry can <b>charge a card twice</b>.</li>
  </ul>''',
    problem_figs=[retry_problem],
    problem_after='  <p class="aside">numbers from class: 3 layers (app → gateway → SDK) each retrying 3 times = 3 × 3 × 3 = 27 calls for one click.</p>',
    analogy_side="calling the pizza place on a Friday",
    analogy='''  <p>You call to order a pizza and the line is busy. You don't redial every second, because you'd never get through and you'd be annoying. You wait a minute, try again, then wait a bit longer.</p>
  <ul>
    <li>You hang up after 30 seconds of ringing instead of holding forever. That's a <b>timeout</b>.</li>
    <li>Each wait gets longer: 1 minute, 2, then 4. That's <b>exponential backoff</b>.</li>
    <li>Your neighbours, who also want pizza, don't all redial at 7:01:00 exactly. That's <b>jitter</b>.</li>
    <li>After three tries you order from the app instead. That's the <b>retry limit</b> and a <b>fallback</b>.</li>
    <li>If the call dropped mid-order, you say “this is order 42 again” so they don't bake two. That's an <b>idempotency key</b>.</li>
  </ul>''',
    analogy_figs=[retry_analogy],
    map=[("Hang up after 30 s of ringing", "Timeout on each attempt"),
         ("Wait 1, then 2, then 4 minutes", "Exponential backoff"),
         ("Neighbours redial at slightly different times", "Jitter (random wait)"),
         ("Give up after three tries", "Max attempts / overall deadline"),
         ("“This is order 42 again”", "Idempotency key on the request"),
         ("Order from the app instead", "Fallback after giving up")],
    how_side="retry the right errors, the right way",
    how='  <p>A retry policy answers four questions: <b>what</b> to retry, <b>how long</b> each try may take, <b>how long</b> to wait between tries, and <b>when</b> to stop.</p>',
    how_figs=[retry_how],
    steps=[("Set two clocks", "A timeout for each attempt (say 2 s) and an overall deadline for the whole operation (say 8 s). The deadline is what the user is willing to wait."),
           ("Classify the error", "Retry timeouts, connection resets, <code>429</code>, <code>502</code>, <code>503</code>, <code>504</code>. Never retry <code>400</code>, <code>401</code>, <code>403</code>, <code>404</code> or <code>409</code>: they'll fail the same way again."),
           ("Wait with full jitter", "Sleep a random time between 0 and min(cap, base × 2<sup>attempt</sup>). If the server sends <code>Retry-After</code>, honour it."),
           ("Make writes repeatable", "Send an <code>Idempotency-Key</code> header so a repeated POST returns the first result instead of doing the work again."),
           ("Give up loudly", "After N attempts or at the deadline, return the error, count it in a metric, and alert when the give-up rate climbs.")],
    how_after='''  <h3>Why jitter matters</h3>
  <div class="grid2">
    <div class="sticky"><h3>No jitter</h3><p>1,000 clients fail at 12:00:00.000. They all retry at 12:00:00.200, then all at 12:00:00.600… Every retry is a synchronised spike.</p></div>
    <div class="sticky sticky--green"><h3>Full jitter</h3><p>Each client picks a random wait inside the window. The same 1,000 retries spread over the whole window, so the service sees a gentle slope.</p></div>
  </div>''',
    vocab=[("Transient failure", "A failure that goes away on its own after a short time."),
           ("Exponential backoff", "Wait base × 2<sup>n</sup> before attempt n+1, up to a cap."),
           ("Jitter", "Randomness added to the wait so clients don't retry in sync."),
           ("Retry budget", "A cap on retries as a % of normal traffic (e.g. 10%)."),
           ("Deadline propagation", "Passing the remaining time to downstream calls."),
           ("Idempotency key", "A unique ID that lets the server recognise a repeated request.")],
    code=dict(file="with-retry.ts", note="full jitter + per-try timeout", src='''
export async function withRetry<T>(
  fn: (signal: AbortSignal) => Promise<T>,
  { attempts = 4, baseMs = 200, capMs = 5_000, timeoutMs = 2_000 } = {},
): Promise<T> {
  for (let i = 0; ; i++) {
    try {
      return await fn(AbortSignal.timeout(timeoutMs));   // every try gets a timeout
    } catch (err) {
      if (i + 1 >= attempts || !isRetryable(err)) throw err;
      const windowMs = Math.min(capMs, baseMs * 2 ** i);
      await sleep(Math.random() * windowMs);           // full jitter
    }
  }
}

const isRetryable = (e: any) =>
  e.name === "TimeoutError" || [429, 502, 503, 504].includes(e.status);

// a POST is only safe to retry with an idempotency key
await withRetry((signal) =>
  fetch("/payments", {
    method: "POST", signal,
    headers: { "Idempotency-Key": order.id },
    body: JSON.stringify(order),
  }));
'''),
    tools="built-in options: AWS SDK retry modes (“standard”, “adaptive”), Polly (.NET), Resilience4j Retry (Java), tenacity (Python), gRPC retry policy, Envoy / Istio retries.",
    gains=["<b>Transient blips never reach the user.</b> Most single failures succeed on the next try.",
           "<b>Bounded waiting.</b> Timeouts and a deadline give every call a known worst case.",
           "<b>Gentle on a struggling service.</b> Backoff and jitter spread the load out.",
           "<b>Cheap to add.</b> A few lines or a library setting.",
           "<b>Safe writes</b> when combined with idempotency keys."],
    losses=["<b>Higher latency on failure.</b> Retries add waiting time to the slow path (p99).",
            "<b>Extra load.</b> Every retry is another request; layered retries multiply.",
            "<b>Duplicates.</b> Without idempotency, a retried write can run twice.",
            "<b>Hides problems.</b> Calls that “succeed on the third try” look green on dashboards.",
            "<b>Tuning.</b> Attempts, base, cap and timeout all need sensible values."],
    baseline="Each line compares a typical service that calls others with <b>no retries</b> (fail on first error) to the same service with <b>timeouts + capped, jittered retries</b>.",
    ratings=[(4, 4, "A small, well-known policy. Easy to read and reason about."),
             (4, 4, "Free libraries; a little extra traffic during incidents."),
             (4, 4, "No change. Policies are usually config."),
             (4, 3, "You need to test timeouts, retryable vs fatal errors and duplicates."),
             (3, 3, "Doesn't add capacity. Badly tuned, it eats capacity."),
             (3, 3, "Jitter smooths spikes, but retries also add load during one."),
             (2, 4, "Short outages and deploy blips become invisible to users."),
             (3, 3, "Happy path unchanged; failed calls get slower before they succeed."),
             (4, 4, "Policies are easy to retune or remove later.")],
    pitfalls=[("Retrying at every layer", "Client, gateway and SDK each retry 3 times: one click becomes 27 calls to the bottom service, exactly when it's weakest.", "retry in ONE layer, usually the one closest to the failing call."),
              ("Retrying without idempotency", "A payment times out after it succeeded. The retry charges the card again.", "idempotency keys on writes, or don't retry the write."),
              ("No jitter", "Every client backs off by exactly 200, 400, 800 ms, so the retries still arrive in synchronised waves.", "full jitter: a random wait inside the window."),
              ("Timeouts longer than the caller's patience", "The backend works for 30 s after the frontend gave up at 5 s. The work is wasted and queues grow.", "pass the remaining deadline down with each call."),
              ("Retrying errors that can't succeed", "Retrying a <code>400 Bad Request</code> three times just triples the noise.", "only retry timeouts, connection errors, 429 and 5xx (except 501)."),
              ("Silent retries", "Everything “works” on the third try while the dependency quietly falls over.", "a metric for every retry, not just for final failures.")],
    use=["Calling anything over a network: HTTP, gRPC, databases, queues, cloud APIs.",
         "Failures are usually short (deploys, failovers, network blips).",
         "The operation is idempotent, or you can make it so with a key.",
         "A user or job can afford a little extra latency for a better success rate."],
    skip=["The error can never succeed on retry (validation, auth, not found).",
          "The operation isn't safe to repeat and can't be made idempotent.",
          "Another layer already retries the same call.",
          "The user can't wait (a hard real-time budget). Fail fast instead."],
    related=["<b>Circuit breaker</b> · stops retries when it's clearly down", "<b>Idempotent consumer</b>", "<b>Rate limiter</b> · and its Retry-After", "<b>Bulkhead</b>", "<b>Timeouts &amp; deadlines</b>"],
    quiz=[("Why add jitter to exponential backoff?", "Without randomness, clients that failed together retry together, creating synchronised spikes. Jitter spreads their retries across the window."),
          ("Which of these should you retry: 400, 404, 429, 503, timeout?", "429, 503 and timeouts. 400 and 404 will fail the same way every time."),
          ("A gateway and the app both retry 3 times. How many calls can one request create?", "Up to 3 × 3 = 9 calls to the service behind them (plus whatever the SDK does). Retry in one layer only."),
          ("How do you make retrying a POST safe?", "Send an idempotency key so the server can recognise the repeat and return the original result instead of doing the work twice.")],
    remember="Every call gets a <span class=\"hl\">timeout</span>. Every retry gets a random wait. Every retry loop gets a limit, and every limit gets an alarm.",
    sources=["Marc Brooker, “Exponential Backoff And Jitter”, AWS Architecture Blog.",
             "AWS Builders' Library, “Timeouts, retries, and backoff with jitter”.",
             "Google SRE Book, chapter “Handling Overload” (retry budgets).",
             "Microsoft Azure Architecture Center, “Retry pattern”."],
)

# ------------------------------------------------------------------ 03 Bulkhead
bh_problem = Doodle(760, 300, "Doodle of one shared pool of 50 threads in the Shop service. All 50 threads are stuck waiting on a slow Reviews service, so calls for Cart and Checkout, which are healthy, can't get a thread either.",
                    "One slow dependency used up the shared pool, so healthy features failed too.")
bh_problem.box(20, 40, 300, 200, None, "paper")
bh_problem.head(170, 30, "Shop service · 1 shared pool of 50 threads", size=18)
for r in range(4):
    for c in range(8):
        bh_problem.raw(f'<rect class="d d-thin d-red f-pink" x="{40 + c * 34}" y="{60 + r * 40}" width="24" height="28" rx="4"/>')
bh_problem.note(170, 226, "all 50 busy waiting on Reviews", "red", size=19)
bh_problem.box(470, 30, 150, 60, "Reviews", "pink", sub="slow: 20 s", stroke="red")
bh_problem.box(470, 120, 150, 60, "Cart", "green", sub="healthy")
bh_problem.box(470, 210, 150, 60, "Checkout", "green", sub="healthy")
bh_problem.arrow(325, 80, 465, 60, color="red", label="50 calls stuck", lx=395, ly=58)
bh_problem.arrow(325, 150, 465, 150, dash=True, label="no thread left ✗", lx=395, ly=142, color="red")
bh_problem.arrow(325, 220, 465, 240, dash=True, label="no thread left ✗", lx=395, ly=258, color="red")

bh_analogy = Doodle(760, 260, "Doodle of a ship's hull divided into watertight compartments by walls. One compartment is flooded with water, the others are dry, so the ship stays afloat.",
                    "The hull is split into watertight compartments. A leak floods one, not the whole ship.")
bh_analogy.raw('<path class="d f-paper" d="M40 90 H720 L660 210 H100 Z"/>')
for x in [180, 320, 460, 600]:
    bh_analogy.line(f"M{x} 90 V210")
bh_analogy.raw('<path class="d d-pen f-blue" d="M188 150 q20 -8 40 0 t40 0 t40 0 t4 0 V208 H188 Z"/>')
bh_analogy.line("M40 230 q30 -10 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0", color="pen", thin=True)
bh_analogy.raw('<path class="d" d="M380 90 V40 H460 V90"/><path class="d" d="M420 40 V20"/>')
bh_analogy.note(250, 130, "leak!", "red")
bh_analogy.arrow(250, 70, 250, 140, color="red", curve=(210, 100))
bh_analogy.note(110, 130, "dry")
bh_analogy.note(390, 130, "dry")
bh_analogy.note(530, 130, "dry")
bh_analogy.note(640, 130, "dry")
bh_analogy.note(380, 256, "watertight walls = bulkheads", "pen")

bh_how = Doodle(760, 310, "The Shop service now has three separate pools: 20 threads for Reviews, 15 for Cart and 15 for Checkout. The Reviews pool is full and rejecting, but the Cart and Checkout pools still have free threads, so those features keep working.",
                "Separate pools: when Reviews fills its own pool, Cart and Checkout still have threads.")
for i, (name, n, full, fill) in enumerate([("Reviews pool · 20", 20, True, "pink"), ("Cart pool · 15", 15, False, "green"), ("Checkout pool · 15", 15, False, "green")]):
    y = 34 + i * 94
    bh_how.box(20, y, 330, 62, None, "paper", stroke="red" if full else "")
    bh_how.note(185, y - 8, name, size=18)
    for k in range(10):
        busy = full or k < 3
        cls = "d d-thin d-red f-pink" if (busy and full) else ("d d-thin f-blue" if busy else "d d-thin f-paper")
        bh_how.raw(f'<rect class="{cls}" x="{36 + k * 31}" y="{y + 14}" width="22" height="34" rx="4"/>')
for i, (name, fill, sub, st) in enumerate([("Reviews", "pink", "slow", "red"), ("Cart", "green", "fine", ""), ("Checkout", "green", "fine", "")]):
    y = 35 + i * 94
    bh_how.box(560, y, 160, 60, name, fill, sub=sub, stroke=st)
    bh_how.arrow(356, y + 30, 554, y + 30, color="red" if i == 0 else "green",
                 label="full → reject fast" if i == 0 else "✓ still works", lx=455, ly=y + 22)

BULKHEAD = dict(
    slug="bulkhead",
    kicker="a.k.a. “don't share one bucket of threads”",
    tldr="Split a service's resources (threads, connections, memory, even whole instances) into <b>separate pools per dependency or per kind of work</b>. When one dependency gets slow and fills its own pool, the others <b>keep their pools and keep working</b>.",
    chips=[("Family", "resilience / isolation"), ("Lives in", "the caller, or the deployment layout"), ("Named after", "ship hull compartments"), ("Pairs with", "timeouts, circuit breaker, load shedding")],
    problem='''  <p class="lead">Most services share <b>one</b> pool of something: one thread pool, one HTTP connection pool, one database connection pool. That's efficient, until one dependency gets <span class="hl-pink">slow</span>.</p>
  <ol>
    <li>The Reviews service starts taking 20 s per call.</li>
    <li>Requests that need reviews grab threads from the shared pool and sit there waiting.</li>
    <li>Within seconds every thread is waiting on Reviews.</li>
    <li>A request for the cart or checkout arrives. Those dependencies are healthy, but there's <b>no thread left</b> to run them.</li>
    <li>The whole shop is down because the least important feature got slow.</li>
  </ol>''',
    problem_figs=[bh_problem],
    problem_after='  <p><b>Key insight:</b> shared resources couple failures. Anything that shares a pool can be starved by its noisiest neighbour.</p>',
    analogy_side="the watertight walls in a ship",
    analogy='''  <p>Ships aren't one big open hull. They're divided into watertight compartments by walls called <b>bulkheads</b>. If the hull is breached, water floods one compartment and the walls stop it there. The ship stays afloat.</p>
  <ul>
    <li>A ship with no walls sinks from a single hole. A ship with walls survives with one compartment flooded.</li>
    <li>The walls cost something: less open space and more structure. You accept that for survival.</li>
    <li>You decide where the walls go based on what must keep working (the engine room gets its own).</li>
  </ul>
  <p class="aside">another everyday one: a supermarket with a separate “10 items or fewer” lane. A trolley full of shopping can't block the quick shoppers.</p>''',
    analogy_figs=[bh_analogy],
    map=[("The ship's hull", "Your service's total resources"),
         ("A watertight compartment", "A separate pool (threads, connections, instances)"),
         ("A hole in the hull", "A slow or failing dependency"),
         ("Water fills one compartment", "Only that dependency's pool fills up"),
         ("The ship stays afloat", "Other features keep working"),
         ("The engine room gets its own compartment", "Critical paths (checkout) get dedicated capacity")],
    how_side="separate pools, sized on purpose",
    how='  <p>Give each dependency, or each class of work, its <b>own limited pool</b>. When a pool is full, new work for it is <b>rejected immediately</b> (or queued briefly) instead of stealing from the others.</p>',
    how_figs=[bh_how],
    steps=[("Find what you share", "List the pools a service uses: worker threads, HTTP client connections, DB connections, queues, memory, CPU."),
           ("Split by dependency or by priority", "One pool per downstream service, or separate pools for “checkout” vs “browse” vs “admin reports”."),
           ("Size each pool", "Use Little's law: concurrent calls ≈ requests/s × latency (s). 50 req/s × 0.2 s = 10 in flight, so a pool of ~15 leaves headroom."),
           ("Decide what happens when it's full", "Reject at once with a clear error or a fallback. A short bounded queue is fine; an unbounded one just moves the problem."),
           ("Watch the pools", "Graph pool usage and rejections per pool. A pool that's always full is either undersized or protecting you from a real problem.")],
    how_after='''  <h3>Bulkheads at different sizes</h3>
  <div class="grid2">
    <div class="sticky"><h3>Inside one process</h3><p>Separate thread pools or semaphores per dependency (e.g. max 20 concurrent calls to Reviews).</p></div>
    <div class="sticky sticky--blue"><h3>Connection pools</h3><p>Separate HTTP / DB connection pools so a slow query can't take every connection.</p></div>
    <div class="sticky sticky--green"><h3>Separate deployments</h3><p>Run the admin/reporting API on different instances from the customer API.</p></div>
    <div class="sticky sticky--pink"><h3>Cells / per-tenant</h3><p>Split customers into “cells”, each a full copy of the stack, so one tenant's spike hits only its cell.</p></div>
  </div>''',
    vocab=[("Bulkhead", "An isolation boundary that limits how much one part can consume."),
           ("Semaphore isolation", "A counter limiting concurrent calls, using the caller's own thread."),
           ("Thread-pool isolation", "Each dependency runs on its own dedicated threads."),
           ("Little's law", "In-flight work = arrival rate × time in system (L = λW)."),
           ("Noisy neighbour", "A workload that hogs shared resources and slows others."),
           ("Cell-based architecture", "Whole copies of the stack, each serving a subset of users.")],
    code=dict(file="bulkhead.ts", note="semaphore per dependency", src='''
class Bulkhead {
  private inFlight = 0;
  constructor(private name: string, private max: number) {}

  async run<T>(fn: () => Promise<T>, fallback: () => T): Promise<T> {
    if (this.inFlight >= this.max) {        // pool full: don't wait, don't steal
      metrics.inc(`bulkhead.rejected.${this.name}`);
      return fallback();
    }
    this.inFlight++;
    try {
      return await fn();                    // fn still needs its own timeout!
    } finally {
      this.inFlight--;
    }
  }
}

// one pool per dependency, sized from traffic × latency
const reviews  = new Bulkhead("reviews", 20);
const checkout = new Bulkhead("checkout", 40);   // critical path gets more

const stars = await reviews.run(() => reviewsApi.get(id, { timeoutMs: 800 }), () => []);
'''),
    tools="in practice: Resilience4j Bulkhead / ThreadPoolBulkhead (Java), Polly Bulkhead (.NET), separate connection pools per client, Kubernetes resource limits, Envoy max-connections / max-pending-requests per cluster.",
    gains=["<b>Failures stay contained.</b> One slow dependency can't starve the rest.",
           "<b>Critical paths are protected.</b> Checkout keeps its capacity even when browsing is overloaded.",
           "<b>Fast, honest rejections</b> instead of everything slowly timing out.",
           "<b>Clear signals.</b> A full pool points straight at the guilty dependency.",
           "<b>Fairness.</b> One tenant or feature can't hog everything."],
    losses=["<b>Less efficient use of resources.</b> Idle threads in one pool can't help a busy one.",
            "<b>Sizing is hard.</b> Too small rejects good traffic; too big doesn't isolate.",
            "<b>More config and more metrics</b> to look after.",
            "<b>More rejected requests</b> under load, which need fallbacks.",
            "<b>Cost</b> when the bulkheads are whole deployments or cells."],
    baseline="Each line compares a service where all calls share <b>one pool</b> to the same service with <b>separate, bounded pools</b> per dependency.",
    ratings=[(4, 3, "A few more pools and limits to understand and size."),
             (4, 3, "Some capacity sits idle; separate deployments or cells cost more."),
             (4, 4, "Neutral. Pool sizes are config."),
             (4, 3, "You need load and fault tests to prove each pool isolates."),
             (3, 4, "Hot spots stay local, so the rest scales predictably."),
             (2, 3, "Spikes in one area are capped instead of spreading."),
             (2, 5, "The whole point: a leak floods one compartment only."),
             (3, 3, "No change on the happy path; faster failures when a pool is full."),
             (4, 4, "Pools are easy to add, resize or merge.")],
    pitfalls=[("No timeouts inside the pool", "The pool is isolated, but each call waits 60 s, so it fills up with stuck calls and rejects everything.", "always pair bulkheads with tight timeouts."),
              ("Unbounded queues in front of the pool", "Requests pile up in a queue forever, using memory and blowing response times.", "a small queue (or none) and fast rejection."),
              ("Pools sized by guesswork", "A pool of 5 for a dependency that normally needs 30 in flight rejects healthy traffic all day.", "size from Little's law and real traffic, then load-test."),
              ("Isolating the wrong thing", "Separate thread pools, but every pool shares one DB connection pool, which is the real bottleneck.", "find the real shared resource and split that."),
              ("Too many tiny pools", "Twenty pools of 3 threads waste memory and make tuning impossible.", "group dependencies by criticality, not one pool each by reflex.")],
    use=["One service calls several dependencies with very different reliability.",
         "Some features are critical (checkout, login) and others are nice-to-have.",
         "You host many tenants and one can overload the others.",
         "You've seen one slow dependency take the whole service down."],
    skip=["The service has one dependency and nothing to protect from it.",
          "Resources are so tight that splitting them leaves every pool too small.",
          "Work is async through queues, where separate queues/consumers already isolate it.",
          "You haven't added timeouts yet. Do that first."],
    related=["<b>Circuit breaker</b>", "<b>Retry with backoff</b>", "<b>Rate limiter</b>", "<b>Competing consumers</b> · separate queues", "<b>Cell-based architecture</b>"],
    quiz=[("Where does the name come from?", "From ships: watertight walls (bulkheads) split the hull so one breach floods only one compartment."),
          ("A pool for Reviews is full. What should happen to a new Reviews call?", "Reject it at once (or after a very short bounded wait) and use a fallback, such as showing the page without reviews."),
          ("50 requests/s, each call takes 0.3 s. Roughly how many concurrent calls does the pool need?", "About 50 × 0.3 = 15 in flight (Little's law), so size it a bit above that, e.g. 20."),
          ("What's the main cost of bulkheads?", "Less efficient resource use: capacity reserved for one pool can't be borrowed by another, plus sizing and config effort.")],
    remember="Don't let the <span class=\"hl\">least important</span> dependency use up the resources the most important one needs. Walls first, then the ship survives a leak.",
    sources=["Michael T. Nygard, <i>Release It!</i>, 2nd ed., “Bulkheads”.",
             "Microsoft Azure Architecture Center, “Bulkhead pattern”.",
             "AWS Well-Architected, “Use bulkhead architectures to limit scope of impact” (cells).",
             "Resilience4j docs, “Bulkhead”."],
)

# ------------------------------------------------------------------ 04 Rate Limiter
rl_problem = Doodle(760, 280, "Doodle of a public API. Normal clients send a few requests each, but one buggy script sends 5,000 requests per second, and the API and its database fall over for everyone.",
                    "One client, buggy or hostile, can use up the capacity meant for everyone.")
rl_problem.box(20, 30, 150, 50, "app A · 5/s", "paper", size=18)
rl_problem.box(20, 110, 150, 50, "app B · 8/s", "paper", size=18)
rl_problem.box(20, 190, 150, 70, "buggy script", "pink", sub="5,000 req/s", stroke="red")
rl_problem.arrow(176, 55, 400, 130)
rl_problem.arrow(176, 135, 400, 140)
for dy in (-14, 0, 14):
    rl_problem.arrow(176, 225 + dy, 400, 160 + dy / 2, color="red")
rl_problem.box(410, 100, 150, 80, "Public API", "pink", sub="CPU 100%", stroke="red")
rl_problem.arrow(566, 140, 630, 140, color="red")
rl_problem.db(680, 110, "DB maxed out", fill="pink", stroke="red")
rl_problem.note(300, 24, "everyone gets 503s now", "red")

rl_analogy = Doodle(760, 260, "Doodle of a theme park ride with a turnstile that lets one guest through every few seconds, and a bucket of ride tokens that refills at a steady rate. Guests without a token wait or come back later.",
                    "The turnstile lets people through at a steady rate. Tokens refill over time; no token, no entry right now.")
rl_analogy.icon("turnstile", 280, 90, 1.6)
rl_analogy.icon("bucket", 60, 70, 2.0, fill="y")
rl_analogy.note(120, 220, "token bucket: +1 token every 2 s")
rl_analogy.note(120, 246, "holds at most 10")
rl_analogy.msgs(470, 140, 6, fill="blue", size=26, gap=8)
rl_analogy.note(570, 120, "the queue of guests")
rl_analogy.arrow(460, 150, 380, 150)
rl_analogy.note(340, 70, "one through per token", "pen")
rl_analogy.note(600, 220, "no token? “come back in 4 s”", "red")

rl_how = Doodle(760, 260, "Token bucket algorithm. Tokens drip into a bucket at a fixed rate, up to a maximum. Each request takes one token and is allowed. If the bucket is empty, the request is rejected with HTTP 429 and a Retry-After header.",
                "Token bucket: a steady refill rate allows the average; the bucket size allows short bursts.")
rl_how.icon("bucket", 300, 40, 2.4, fill="y")
rl_how.arrow(330, 20, 360, 70, label="refill 10 tokens/s", lx=420, ly=26, anchor="start")
rl_how.box(20, 100, 150, 56, "request", "blue")
rl_how.arrow(176, 128, 300, 128)
rl_how.arrow(460, 110, 590, 70, color="green", label="token taken ✓", lx=520, ly=72)
rl_how.box(596, 40, 150, 56, "200 OK", "green")
rl_how.arrow(460, 160, 590, 200, color="red", label="bucket empty ✗", lx=520, ly=210)
rl_how.box(596, 176, 150, 70, "429", "pink", sub="Retry-After: 2", stroke="red")
rl_how.note(380, 252, "capacity 20 = burst size", "pen")

RATE = dict(
    slug="rate-limiter",
    kicker="a.k.a. “take a number, please”",
    tldr="Decide how many requests each client (user, API key, IP, tenant) may make in a period, for example <b>100 per minute</b>. Count them, and when a client goes over, <b class=\"red\">reject the extra requests quickly</b> with <code>429 Too Many Requests</code> and a hint about when to retry.",
    chips=[("Family", "resilience / protection"), ("Lives in", "API gateway, load balancer, or the service"), ("Also called", "throttling"), ("Pairs with", "retries with Retry-After, quotas, API keys")],
    problem='''  <p class="lead">A service has <b>limited capacity</b>: CPU, memory, database connections, a paid third-party quota. Without limits, <span class="hl-pink">any single client can use all of it</span>.</p>
  <ul>
    <li>A buggy script calls your API in a tight loop: 5,000 requests a second.</li>
    <li>A big customer runs a bulk import at 9 a.m. on Monday.</li>
    <li>A bot scrapes every product page, or someone tries passwords by brute force.</li>
    <li>Your own retry storm after an outage (see note 02).</li>
  </ul>
  <p>In every case, well-behaved clients get slow responses or errors because of someone else.</p>''',
    problem_figs=[rl_problem],
    analogy_side="the turnstile at a theme park ride",
    analogy='''  <p>A popular ride can only take so many people a minute. A turnstile lets guests through at a <b>steady rate</b>. If you arrive when it's at its limit, you wait or come back later. The ride never gets overloaded, and everyone gets a fair turn.</p>
  <ul>
    <li>Think of it as a bucket of ride tokens that refills slowly. Each guest takes a token. A group can go in together if enough tokens have saved up (a <b>burst</b>).</li>
    <li>Annual-pass holders get a bigger bucket: <b>different limits per plan</b>.</li>
    <li>The sign says “next entry in 4 s”, so guests know when to try again (<code>Retry-After</code>).</li>
  </ul>''',
    analogy_figs=[rl_analogy],
    map=[("Guests arriving at the ride", "Requests from clients"),
         ("The turnstile", "The rate limiter"),
         ("Ride tokens refilling over time", "Token bucket: refill rate"),
         ("Tokens saved up for a group", "Bucket size = allowed burst"),
         ("Annual pass = bigger allowance", "Per-plan / per-key limits"),
         ("“Next entry in 4 s” sign", "429 + Retry-After header")],
    how_side="count, compare, allow or reject",
    how='''  <p>Every request is mapped to a <b>key</b> (API key, user ID, IP, tenant). The limiter keeps a counter per key and decides in microseconds whether the request fits. Common algorithms:</p>
  <ul>
    <li><b>Token bucket:</b> tokens refill at rate r up to size b; each request spends one. Allows short bursts, enforces the average. The most common choice.</li>
    <li><b>Leaky bucket:</b> requests drain from a queue at a fixed rate. Smooths output completely.</li>
    <li><b>Fixed window:</b> count per calendar minute. Simple, but allows 2× the limit around the minute boundary.</li>
    <li><b>Sliding window:</b> counts over the last 60 s. Fairer, a bit more work.</li>
  </ul>''',
    how_figs=[rl_how],
    steps=[("Choose the key", "Per API key for partners, per user for logged-in traffic, per IP for anonymous traffic, per tenant for SaaS."),
           ("Choose the limits", "Base them on capacity and fairness, e.g. 100 req/min with bursts of 20; higher for paid plans; stricter on expensive endpoints like login or search."),
           ("Count somewhere shared", "With many instances, keep counters in a shared store (Redis, the gateway) or give each instance limit ÷ N."),
           ("Reject clearly", "Return <code>429 Too Many Requests</code> with <code>Retry-After</code> and <code>RateLimit-*</code> headers so clients can back off."),
           ("Monitor and tune", "Track rejections per key. A key that's always limited may be a bug, an attacker, or a customer who needs a bigger plan.")],
    vocab=[("Rate limit", "Max requests per key per period (e.g. 100/min)."),
           ("Quota", "A larger allowance over a long period (e.g. 1M calls/month)."),
           ("Burst", "Short spike above the average that the limiter tolerates."),
           ("429 Too Many Requests", "The HTTP status for “you're over your limit”."),
           ("Retry-After", "Header saying how many seconds to wait before retrying."),
           ("Load shedding", "Dropping low-priority work when the whole system is overloaded.")],
    code=dict(file="token-bucket.ts", note="one bucket per key, in Redis in real life", src='''
type Bucket = { tokens: number; updated: number };
const buckets = new Map<string, Bucket>();

export function allow(key: string, ratePerSec = 10, capacity = 20): number {
  const now = Date.now() / 1000;
  const b = buckets.get(key) ?? { tokens: capacity, updated: now };
  // refill for the time that passed, but never above capacity
  b.tokens = Math.min(capacity, b.tokens + (now - b.updated) * ratePerSec);
  b.updated = now;
  buckets.set(key, b);
  if (b.tokens >= 1) { b.tokens -= 1; return 0; }        // allowed
  return Math.ceil((1 - b.tokens) / ratePerSec);         // seconds to wait
}

app.use((req, res, next) => {
  const wait = allow(req.apiKey ?? req.ip);
  if (wait === 0) return next();
  res.set("Retry-After", String(wait)).status(429).send("Too Many Requests");
});
'''),
    tools="ready-made: API gateways (Kong, AWS API Gateway usage plans, Azure APIM), NGINX limit_req, Envoy local / global rate limit, Cloudflare rate limiting, Redis + a Lua script for a shared token bucket.",
    gains=["<b>Protects capacity</b> from floods, bugs and abuse.",
           "<b>Fairness.</b> One client can't starve the others.",
           "<b>Predictable cost</b> for expensive or paid downstream calls.",
           "<b>Security</b> against brute force and scraping.",
           "<b>Product tiers.</b> Limits become part of free vs paid plans."],
    losses=["<b>Legit traffic gets rejected</b> when limits are too tight.",
            "<b>Shared counters</b> add a dependency (Redis) and a little latency.",
            "<b>Hard to choose the key.</b> Many users behind one office IP look like one client.",
            "<b>Clients must handle 429</b> properly, or they'll just retry harder.",
            "<b>More config</b> per plan, endpoint and key."],
    baseline="Each line compares a public or shared API with <b>no limits</b> to the same API with <b>per-client rate limits</b> at the edge.",
    ratings=[(4, 3, "One more component and a set of limits to explain to clients."),
             (4, 4, "Gateways include it; it also saves money on runaway usage."),
             (4, 4, "Neutral. Limits are config, often changeable live."),
             (4, 3, "Needs tests for limits, bursts and distributed counters."),
             (3, 4, "Capacity is shared fairly, so growth is predictable."),
             (2, 4, "Floods are capped before they reach the backend."),
             (2, 4, "One bad client can't take the service down for everyone."),
             (3, 3, "A tiny check per request; much better under attack."),
             (4, 4, "Limits per plan or endpoint are easy to change.")],
    pitfalls=[("Limiting by IP only", "A whole university or company shares one IP and hits the limit together.", "limit by API key or user where you can; use IP only for anonymous traffic."),
              ("Per-instance counters", "10 instances each allow 100/min, so the real limit is 1,000/min and changes as you scale.", "a shared store, or divide the limit by the instance count."),
              ("No Retry-After", "Clients get 429 with no hint and retry instantly in a loop.", "send Retry-After and RateLimit headers; document them."),
              ("Fixed windows at the boundary", "A client sends 100 at 12:00:59 and 100 at 12:01:00: 200 in two seconds.", "token bucket or sliding window."),
              ("Same limit for every endpoint", "Cheap GETs and an expensive report endpoint share one number.", "weight expensive endpoints or give them their own limits."),
              ("Limiter fails closed", "Redis goes down and the limiter rejects every request.", "decide on purpose: usually fail open with a local fallback limit.")],
    use=["Public or partner APIs.",
         "Expensive endpoints: login, search, exports, AI calls.",
         "Multi-tenant SaaS where tenants share capacity.",
         "Calls to a paid third party with its own quota."],
    skip=["Internal calls between your own services, where backpressure, bulkheads or queues fit better.",
          "Traffic is tiny and trusted.",
          "You actually need to smooth bursts of work. Use a queue (note 12).",
          "Clients can't handle rejection at all (e.g. hardware devices that never retry)."],
    related=["<b>Retry with backoff</b> · honour Retry-After", "<b>API gateway</b> · the usual home", "<b>Bulkhead</b>", "<b>Competing consumers</b> · queue-based levelling", "<b>Circuit breaker</b>"],
    quiz=[("What's the difference between the bucket's refill rate and its size?", "The refill rate is the long-run average allowed; the size is the largest burst a client can send at once after being idle."),
          ("Why can fixed-window counting let through 2× the limit?", "A client can send the full limit at the end of one window and again at the start of the next, so two windows' worth arrive within seconds."),
          ("Which HTTP status and header should a limiter return?", "429 Too Many Requests, with Retry-After (and ideally RateLimit-Limit / RateLimit-Remaining / RateLimit-Reset)."),
          ("Should the limiter fail open or closed if its counter store is down?", "Usually open, with a conservative local limit, so an outage of the limiter doesn't become an outage of the API. Security-critical endpoints like login may fail closed.")],
    remember="Everyone gets a <span class=\"hl\">fair share</span>. Over your share? Get a fast 429 and a time to come back, never a slow death for everyone.",
    sources=["Stripe Engineering, “Scaling your API with rate limiters”.",
             "IETF draft, “RateLimit header fields for HTTP”.",
             "Google Cloud Architecture, “Rate-limiting strategies and techniques”.",
             "Microsoft Azure Architecture Center, “Rate Limiting pattern” and “Throttling pattern”."],
)

NOTES = [RETRY, BULKHEAD, RATE]
