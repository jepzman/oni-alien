# Vol. 1 · extra notes (November 2026): Strangler Fig, Backpressure, Consistent Hashing.
# Numbered 19–21 so earlier note URLs and PDF names stay the same.

# ------------------------------------------------------------------ 19 Strangler Fig
sf_problem = Doodle(760, 260, "Doodle of a big-bang rewrite. An eight-year-old monolith keeps running while a team rewrites everything from scratch. After 14 months the rewrite still can't do what the old system does, because the old system kept changing, and nothing new has reached users.",
                    "The rewrite chases a moving target, and nothing ships until all of it does.")
sf_problem.box(20, 40, 220, 80, "old monolith", "blue", sub="still changing every week", size=18, subsize=14)
sf_problem.box(20, 160, 220, 70, "the rewrite", "pink", stroke="red", sub="month 14 · 60% done", size=18, subsize=14)
sf_problem.arrow(244, 80, 360, 120, dash=True, label="new features", lx=300, ly=84)
sf_problem.arrow(244, 195, 360, 150, color="red", dash=True)
sf_problem.box(364, 100, 160, 70, "users", "y", sub="get nothing new", size=18, subsize=14)
sf_problem.note(640, 110, "switch-over day:", "red", size=16)
sf_problem.note(640, 136, "everything at once", "red", size=16)

sf_analogy = Doodle(760, 250, "Doodle of a strangler fig. A seed lands in the branches of an old tree. Its roots grow down around the trunk, a little at a time. Over the years the fig carries more and more of the weight, until the old tree inside can be gone and the fig stands on its own.",
                    "The fig grows around the old tree, a root at a time, until it stands on its own.")
for i, (label, share) in enumerate([("year 1", 0.15), ("year 4", 0.5), ("year 8", 0.9)]):
    x = 60 + i * 240
    sf_analogy.box(x + 40, 40, 60, 160, None, "paper")
    sf_analogy.box(x + 40, 200 - round(160 * share), 60, round(160 * share), None, "green")
    sf_analogy.note(x + 70, 228, label, size=16)
sf_analogy.note(620, 30, "green = the fig", "green", size=15)

sf_how = Doodle(760, 290, "Strangler fig in software. A routing facade sits in front of the old system. At first every path goes to the monolith. Then the orders paths are routed to a new orders service, later the search paths to a new search service. Each move is small and can be switched back. When no path goes to the monolith, it is switched off.",
                "A router in front; move one route at a time; switch back if needed.")
sf_how.box(20, 110, 130, 70, "clients", "paper", size=18)
sf_how.arrow(154, 145, 226, 145)
sf_how.box(230, 90, 160, 110, "routing facade", "y", sub="proxy or gateway", size=17, subsize=14)
sf_how.arrow(394, 115, 516, 50, label="/orders/*", lx=430, ly=62, color="green")
sf_how.arrow(394, 145, 516, 145, label="/search/*", lx=455, ly=136, color="green")
sf_how.arrow(394, 175, 516, 240, label="everything else", lx=430, ly=236, dash=True)
sf_how.box(520, 20, 220, 60, "new orders service", "green", size=16)
sf_how.box(520, 115, 220, 60, "new search service", "green", size=16)
sf_how.box(520, 210, 220, 60, "old monolith", "blue", sub="shrinking", size=16, subsize=13)

STRANGLER_FIG = dict(
    slug="strangler-fig",
    kicker="a.k.a. “replace it a route at a time”",
    tldr="Don't rewrite a big old system in one go. Put a <b>routing facade</b> (a proxy or gateway) in front of it, then move <b>one route or capability at a time</b> to new code, behind the same URLs. Each move is small, ships on its own, and can be <b>switched back</b> by changing a route. The old system shrinks until nothing routes to it, and then you turn it off.",
    chips=[("Family", "communication · migration"), ("Named by", "Martin Fowler (2004), after the strangler fig tree"), ("Needs", "a place to route traffic: proxy, gateway, or the app's own router"), ("Pairs with", "anti-corruption layer, change data capture, feature flags")],
    problem="""  <p class="lead">A team decides to rewrite an eight-year-old monolith from scratch. Fourteen months later the rewrite is “60% done”, the old system has gained features the rewrite doesn't have, and <span class="hl-pink">users have received nothing new</span>. The plan ends in one risky switch-over day.</p>
  <ul>
    <li>Big-bang rewrites chase a <b>moving target</b>: the old system keeps changing.</li>
    <li>Nothing reaches users until <b>everything</b> works, so the risk piles up at the end.</li>
    <li>There's no small step back: switching over is all or nothing.</li>
  </ul>""",
    problem_figs=[sf_problem],
    analogy_side="the strangler fig tree",
    analogy="""  <p>A strangler fig starts as a seed in the branches of an old tree. Its roots grow down around the trunk, <b>a little each year</b>, carrying more of the weight, until the fig <b>stands on its own</b> and the old tree is no longer needed. At no point does anything fall down.</p>""",
    analogy_figs=[sf_analogy],
    map=[("The old tree", "The legacy system, still serving users"),
         ("Each new root", "One route or capability moved to new code"),
         ("Growing around the trunk", "A facade in front that decides where each request goes"),
         ("The fig carrying more weight", "More routes pointing at new services"),
         ("The old tree gone", "No traffic to the monolith: switch it off")],
    how_side="a facade and many small moves",
    how="""  <p>Clients only ever talk to the <b>facade</b>. Routing rules decide which requests still go to the old system and which go to new services. Moving a capability means building it, testing it against real traffic, and changing a route; moving it back means changing the route back.</p>""",
    how_figs=[sf_how],
    steps=[("Put a facade in front", "A reverse proxy or gateway that passes everything to the old system at first. Nothing changes for users."),
           ("Pick a thin slice", "A capability with clear edges and real value: product search, invoices, one report. Not the hardest part first."),
           ("Build it new, with its own data", "Sync the data it needs from the old database (change data capture), or call the old system through an anti-corruption layer."),
           ("Shift traffic gradually", "Shadow requests to compare answers, then 1%, 10%, 100%. Keep the route switch as the rollback."),
           ("Remove the old code", "Delete the old feature once nothing routes to it. Repeat until the monolith is empty.")],
    vocab=[("Facade", "The single entry point that routes requests to old or new code."),
           ("Slice", "One capability moved at a time, end to end."),
           ("Shadow traffic", "Copying real requests to the new code without using its answers."),
           ("Anti-corruption layer", "A translator that keeps the old model out of the new code."),
           ("Event interception", "Capturing the old system's changes (CDC) to feed new services."),
           ("Big-bang rewrite", "Replacing everything at once on one switch-over day.")],
    code=dict(file="facade.yaml", note="Envoy-style routes (generic)", src="""
# one facade, many small moves: each route is a separate, reversible change
routes:
  - match: { prefix: /search }          # moved in March: fully on the new service
    route: { cluster: search-v2 }

  - match: { prefix: /orders }          # moving now: 10% new, 90% old
    route:
      weighted_clusters:
        - { name: orders-v2,  weight: 10 }
        - { name: monolith,   weight: 90 }
    request_mirror_policies:            # also copy the old system's traffic to v2 to compare
      - { cluster: orders-v2-shadow, runtime_fraction: { default_value: { numerator: 100 } } }

  - match: { prefix: / }                # everything else: still the monolith
    route: { cluster: monolith }
"""),
    tools="tools: Envoy, NGINX, Traefik or a cloud API gateway as the facade; Kubernetes Gateway API HTTPRoutes; Debezium for change data capture; feature flags for slices inside one app; Diffy-style response comparison for shadow traffic.",
    gains=["<b>Value early</b>: each slice ships on its own.",
           "<b>Small, reversible steps</b>: a route change undoes a move.",
           "<b>Old and new run side by side</b>, so real traffic tests the new code.",
           "<b>Can stop any time</b> with a working system."],
    losses=["<b>Two systems to run</b> for a long time.",
            "<b>Data sync</b> between old and new databases is the hard part.",
            "<b>The facade</b> is one more critical component.",
            "<b>Easy to stall</b> at 80%, with the last hard parts never moved."],
    baseline="Each line compares <b>a big-bang rewrite</b> to <b>moving one route at a time behind a facade</b>.",
    ratings=[(3, 3, "Neutral: simpler steps, but two systems for a while."),
             (3, 2, "Running old and new together costs more."),
             (1, 4, "Each slice deploys on its own."),
             (2, 4, "Shadow traffic compares old and new on real requests."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "A failed slice is rolled back by a route change."),
             (3, 3, "One extra hop through the facade."),
             (2, 5, "The system changes shape a slice at a time.")],
    pitfalls=[("Facade with business logic", "The router starts translating, merging and fixing data.", "keep the facade to routing; put translation in an anti-corruption layer next to the new service."),
              ("Sharing the old database", "New services read and write the monolith's tables directly, so neither can change.", "give each new service its own data, synced by CDC or events."),
              ("Starting with the hardest part", "The first slice takes a year and the effort loses support.", "start with a thin, valuable, well-bounded slice."),
              ("Never finishing", "The last 20% stays in the monolith for ever, and you pay for both.", "plan and budget the removal of the old system, not only the new code.")],
    use=["A large legacy system that must keep running while it's replaced.",
         "Requests can be routed by path, host, tenant or message type.",
         "You want value and learning before the whole migration ends."],
    skip=["The system is small enough to rewrite in a few weeks.",
          "Nothing can be routed separately (one huge batch job, a desktop app without seams).",
          "The old system is being retired, not replaced."],
    related=["<b>Strangler fig migration</b> (Ana, vol. 4) · the strategy and the plan", "<b>API gateway</b> · a natural facade", "<b>Change data capture</b> (Vol. 3)", "<b>Feature flags</b> (Vol. 6)", "<b>Expand &amp; contract</b> (Vol. 3)"],
    quiz=[("Why do big-bang rewrites so often fail?", "The old system keeps changing, nothing ships until everything works, and the switch-over is one large, risky step."),
          ("What does the facade do?", "It is the single entry point that routes each request to the old system or a new service."),
          ("How do you roll back a slice?", "Change its route back to the old system."),
          ("What is usually the hardest part?", "The data: keeping the old and new databases in step while both are in use.")],
    quiz_sit=[("Six months into a strangler migration, three slices are live, but the new services all read the monolith's database directly, and a schema change in the monolith just broke two of them. What do you change?",
               "Give each new service its own data, fed by change data capture or events from the old system, with an anti-corruption layer translating the old model. Then the monolith's schema can change without breaking the new services, and the old tables can be retired slice by slice.")],
    try_it="Put a local reverse proxy (NGINX, Caddy or Envoy) in front of any small app. Route one path to a second, new app, and send 10% of that path's traffic to it with a weight. Then move it to 100% and back to 0% by editing only the proxy config, and check the clients never noticed.",
    remember="Grow around it <span class=\"hl\">one root at a time</span>. A <span class=\"hl\">route change</span> is your undo button.",
    sources=["Martin Fowler, “StranglerFigApplication” (2004, updated 2024).",
             "Sam Newman, <i>Monolith to Microservices</i> (2019), chapter 3.",
             "Microsoft Azure Architecture Center, “Strangler Fig pattern”.",
             "Paul Hammant, “Legacy Application Strangulation: Case Studies” (2013)."],
)

# ------------------------------------------------------------------ 20 Backpressure
bp_problem = Doodle(760, 260, "Doodle of an unbounded queue. An API accepts 2,000 requests a second and puts each one on an in-memory queue. The worker behind it handles 1,200 a second. The queue grows by 800 every second; after a few minutes memory runs out, the process crashes, and every queued request is lost.",
                    "Accept faster than you can finish, and the queue grows until the process dies.")
bp_problem.box(20, 90, 150, 70, "API in", "y", sub="2,000 / s", size=18, subsize=14)
bp_problem.arrow(174, 125, 226, 125)
bp_problem.box(230, 70, 300, 110, None, "pink", stroke="red")
bp_problem.msgs(244, 100, 11, fill="y", size=22, gap=4)
bp_problem.msgs(244, 136, 11, fill="y", size=22, gap=4)
bp_problem.note(380, 62, "queue: +800 every second", "red", size=15)
bp_problem.arrow(534, 125, 586, 125)
bp_problem.box(590, 90, 150, 70, "worker", "blue", sub="1,200 / s", size=18, subsize=14)
bp_problem.note(380, 226, "minute 4: out of memory · crash · all queued work lost", "red", size=16)

bp_analogy = Doodle(760, 250, "Doodle of a restaurant host. The kitchen can cook 40 meals an hour. When the order rail in the kitchen is full, the host stops seating new tables and gives waiting guests a time instead. Guests wait outside for a bit, but the kitchen never drowns and nobody waits two hours for food at the table.",
                    "When the kitchen's rail is full, the host stops seating people.")
bp_analogy.box(20, 70, 170, 90, "guests", "paper", sub="arriving", size=18, subsize=14)
bp_analogy.arrow(194, 115, 266, 115)
bp_analogy.box(270, 60, 190, 110, "host", "y", sub="seats only if rail has room", size=18, subsize=13)
bp_analogy.arrow(464, 115, 536, 115)
bp_analogy.box(540, 60, 200, 110, "kitchen rail", "green", sub="room for 12 tickets", size=18, subsize=14)
bp_analogy.arrow(560, 56, 360, 56, curve=(460, 10), dash=True, color="pen")
bp_analogy.note(460, 30, "“full”", "pen", size=16)
bp_analogy.note(270, 210, "“about 20 minutes”: waiting outside, not at the table", "pen", anchor="start", size=15)

bp_how = Doodle(760, 280, "Four ways to push back. Block: the producer waits until there is room. Drop or sample: extra items are discarded, like old metrics. Reject: the API answers 429 or 503 with a retry hint. Pull: the consumer asks for the next items only when it has capacity, as Kafka consumers and reactive streams do.",
                "A bounded buffer, and a decision about what happens when it's full.")
bp_how.box(20, 20, 200, 60, "bounded buffer", "y", sub="e.g. 1,000 items", size=17, subsize=13)
for i, (name, sub, fill) in enumerate([("block", "producer waits", "blue"), ("drop / sample", "lose the extras", "paper"),
                                       ("reject", "429 / 503 + retry-after", "pink"), ("pull", "ask for N when ready", "green")]):
    x = 20 + i * 184
    bp_how.box(x, 130, 170, 80, name, fill, sub=sub, size=17, subsize=13)
    bp_how.arrow(x + 85, 104, x + 85, 126)
bp_how.line("M120 84 V104 M105 104 H657")
bp_how.note(244, 97, "when full:", anchor="start", size=15)
bp_how.note(380, 252, "every buffer between two steps needs a limit and a “when full” rule", "pen", size=16)

BACKPRESSURE = dict(
    slug="backpressure",
    kicker="a.k.a. “slow down, I'm full”",
    tldr="When work arrives faster than it can be finished, an unlimited queue only <b>hides the problem until memory runs out</b>. Give every buffer a <b>limit</b>, and decide what happens when it's full: <b>block</b> the producer, <b>drop or sample</b> the extras, <b>reject</b> with 429/503 and a retry hint, or let consumers <b>pull</b> only what they can handle. The slowness then travels back to the source, where it can be seen and dealt with.",
    chips=[("Family", "resilience"), ("Built into", "TCP flow control, Kafka consumers, reactive streams"), ("Opposite", "unbounded queues and buffers"), ("Pairs with", "rate limiter, competing consumers, autoscaling")],
    problem="""  <p class="lead">An API accepts 2,000 requests a second and hands each one to an in-memory queue. The worker behind it manages 1,200. The queue grows by 800 every second, latency grows with it, and after four minutes <span class="hl-pink">the process runs out of memory and everything queued is lost</span>.</p>
  <ul>
    <li>Unbounded buffers <b>hide overload</b>: no errors, just slower and slower answers.</li>
    <li>By the time the queue is noticed, the requests at the front are <b>too old to matter</b>; the user gave up minutes ago.</li>
    <li>The crash loses <b>all</b> queued work, not just the excess.</li>
  </ul>""",
    problem_figs=[bp_problem],
    analogy_side="the restaurant host",
    analogy="""  <p>A kitchen can cook 40 meals an hour. When the <b>ticket rail</b> is full, the host <b>stops seating tables</b> and tells new guests “about 20 minutes”. Guests wait outside for a while, but nobody sits at a table for two hours, and the kitchen never drowns.</p>""",
    analogy_figs=[bp_analogy],
    map=[("The ticket rail with room for 12", "A bounded buffer or queue"),
         ("The host stops seating", "The producer is slowed, blocked or turned away"),
         ("“About 20 minutes”", "429 / 503 with a Retry-After header"),
         ("Cooks taking the next ticket when ready", "Pull-based consumers"),
         ("The kitchen never drowns", "The service stays fast for the work it accepts")],
    how_side="a limit, and a rule for when it's full",
    how="""  <p>Every place work waits (a queue, a channel, a thread pool, a socket buffer) gets a maximum size. When it's full, one of four things happens, chosen on purpose for that kind of work. The signal then flows back upstream, step by step, until it reaches something that can slow down, retry later or show a message.</p>""",
    how_figs=[bp_how],
    steps=[("Find every buffer", "In-memory queues, worker pools, connection pools, message brokers, HTTP clients' request queues."),
           ("Give each a limit", "Size it from throughput × acceptable wait: 1,200/s and 2 s of waiting is about 2,400 items, not “unlimited”."),
           ("Choose the full-buffer rule", "Block (internal pipelines), drop or sample (metrics, telemetry), reject (public APIs), pull (consumers of a broker)."),
           ("Propagate it", "A rejected downstream call becomes a 503 upstream; a full consumer stops pulling. Don't swallow the signal halfway."),
           ("Watch queue age", "Alert on how old the oldest waiting item is, and scale or shed load before it matters to users.")],
    vocab=[("Backpressure", "A signal from a slow consumer that makes the producer slow down."),
           ("Bounded buffer", "A queue with a maximum size."),
           ("Load shedding", "Rejecting some work on purpose to keep the rest fast."),
           ("Pull-based", "The consumer asks for more work when it has capacity."),
           ("Flow control", "The protocol-level version (TCP windows, HTTP/2 streams)."),
           ("Queue age", "How long the oldest item has waited: the number that matters.")],
    code=dict(file="ingest.ts", note="Node.js + Express", src="""
// a bounded queue in front of a slower worker: reject early instead of growing for ever
const MAX = 2_400;                        // ≈ 1,200 jobs/s × 2 s of acceptable waiting
const queue: Job[] = [];

app.post("/events", (req, res) => {
  if (queue.length >= MAX) {
    res.set("Retry-After", "2");          // tell the client when to come back
    return res.status(503).json({ error: "busy, try again shortly" });
  }
  queue.push(toJob(req.body));
  res.status(202).end();                  // accepted, not done
});

// the worker pulls at its own pace
async function work() {
  for (;;) {
    const job = queue.shift();
    if (!job) { await sleep(10); continue; }
    metrics.queueAgeMs.set(Date.now() - job.receivedAt);
    await handle(job);
  }
}
"""),
    tools="tools: Node.js streams (<code>highWaterMark</code>, <code>pipeline</code>), Go buffered channels, Reactive Streams / Project Reactor / RxJS, Kafka and SQS (pull consumers), Envoy and NGINX connection and request limits, Akka Streams.",
    gains=["<b>No out-of-memory crashes</b> from runaway queues.",
           "<b>Fast answers for accepted work</b>, instead of slow answers for all.",
           "<b>Overload is visible</b>: rejections and queue age, not mystery latency.",
           "<b>Clients can react</b>: retry later, show a message, slow down."],
    losses=["<b>Some work is refused</b> or dropped during peaks.",
            "<b>Every producer must handle “full”</b>: retries, messages, waiting.",
            "<b>Limits need tuning</b>, and wrong ones reject too early or too late.",
            "<b>Blocking</b> can spread a slowdown upstream if used everywhere."],
    baseline="Each line compares <b>unbounded queues between steps</b> to <b>bounded buffers with an explicit full-buffer rule</b>.",
    ratings=[(4, 3, "A limit and a rule at each buffer."),
             (3, 3, "Neutral."),
             (4, 4, "Neutral: limits are config."),
             (3, 4, "Overload behaviour becomes testable."),
             (3, 3, "Doesn't add capacity, protects it."),
             (2, 4, "Spikes are shed or absorbed, not stored until a crash."),
             (1, 5, "The service stays up under overload."),
             (2, 4, "Accepted work stays fast; latency doesn't creep."),
             (4, 4, "Neutral.")],
    pitfalls=[("A limit in one place only", "The API rejects, but an unbounded in-memory retry queue in the client brings the problem back.", "check every buffer along the path, clients included."),
              ("Swallowing the signal", "A middle service catches 503s from below and queues them internally.", "pass the pushback upstream as a 503 or 429."),
              ("Queue length, not age", "10,000 items looks scary, but they may be 50 ms old; 200 items can be 10 minutes old.", "alert on the age of the oldest item."),
              ("Blocking a request thread", "The producer blocks inside a web request, and the server runs out of threads.", "reject quickly at the edge; block only inside internal pipelines.")],
    use=["Producers can outrun consumers, even briefly.",
         "Ingest endpoints, event pipelines, streaming and batch imports.",
         "Anywhere an in-memory queue sits between two steps."],
    skip=["Work must never be refused and there is no peak (rare: use a durable queue and capacity instead).",
          "Single synchronous calls with timeouts already bound the work.",
          "The producer is a person typing; ordinary rate limits are enough."],
    related=["<b>Rate limiter</b>", "<b>Bulkhead</b>", "<b>Competing consumers</b>", "<b>Autoscaling</b> (Vol. 6)", "<b>Connection pooling</b> (Vol. 3)"],
    quiz=[("Why is an unbounded queue dangerous?", "It hides overload as growing latency until memory runs out; then the crash loses every queued item."),
          ("Name the four things that can happen when a buffer is full.", "Block the producer, drop or sample the extras, reject with an error, or let consumers pull only what they can handle."),
          ("Which HTTP status codes signal pushback?", "429 Too Many Requests and 503 Service Unavailable, ideally with a Retry-After header."),
          ("Why alert on queue age rather than queue length?", "Age is what users feel: how long work waits. Length says little without the processing rate.")],
    quiz_sit=[("A metrics agent buffers data points in memory when the metrics backend is slow. During a backend outage, the agent on every host grows to 4 GB and the hosts start swapping. Which full-buffer rule fits metrics, and what do you set?",
               "Drop or sample: losing some metric points during an outage is acceptable, slowing the hosts isn't. Cap the agent's buffer (by size or age), drop the oldest points when full, and count what was dropped so the gap is visible.")],
    try_it="Write a tiny producer that sends 2,000 jobs a second to a worker that handles 1,000, through an in-memory array. Watch memory grow. Then cap the queue at 2,000 items and return 503 when full, and graph accepted jobs, rejected jobs and the age of the oldest queued job.",
    remember="Every queue needs a <span class=\"hl\">limit</span> and a <span class=\"hl\">“when full”</span> rule. Push back; don't pile up.",
    sources=["Reactive Streams specification (reactive-streams.org).",
             "Fred Hébert, “Queues Don't Fix Overload” (2014).",
             "Marc Brooker, “Load shedding to avoid overload”, Amazon Builders' Library.",
             "Node.js documentation, “Backpressuring in Streams”."],
)

# ------------------------------------------------------------------ 21 Consistent hashing
ch_problem = Doodle(760, 250, "Doodle of hash modulo N when a cache node is added. With four nodes, each key goes to hash modulo 4. Adding a fifth node changes the rule to hash modulo 5, and about 80 percent of keys now map to a different node. Almost every lookup misses at once, and the database behind the cache is flooded.",
                    "hash % 4 → hash % 5: four keys in five move, and the cache is suddenly empty.")
ch_problem.row([("node 1", "", "blue"), ("node 2", "", "blue"), ("node 3", "", "blue"), ("node 4", "", "blue"), ("node 5", "new", "green")], x=20, y=30, h=60, gap=16, size=16, subsize=13)
ch_problem.note(380, 130, "hash % 4 → hash % 5", size=17)
ch_problem.note(380, 162, "≈ 80% of keys now live on a different node", "red", size=17)
ch_problem.note(380, 200, "cache misses everywhere → the database takes it all", "red", size=16)

ch_analogy = Doodle(760, 260, "Doodle of seats around a round table. Each guest sits at the first free host chair clockwise from their name card's spot. When a new host sits down, only the guests between the new host and the previous host move to the new host; everyone else stays put.",
                    "Around a round table, a new host only takes the guests just before their chair.")
import math as _m
cx, cy, r = 220, 130, 95
ch_analogy.circle(cx, cy, r, fill="paper")
for k, (ang, lab, fill) in enumerate([(-90, "A", "blue"), (30, "B", "blue"), (150, "C", "blue"), (-30, "D", "green")]):
    a = _m.radians(ang)
    ch_analogy.circle(round(cx + r * _m.cos(a)), round(cy + r * _m.sin(a)), 16, fill=fill, label=lab)
ch_analogy.note(500, 90, "D sits down between A and B", "green", anchor="start", size=16)
ch_analogy.note(500, 120, "only guests from A to D move", "green", anchor="start", size=16)
ch_analogy.note(500, 150, "everyone else stays put", anchor="start", size=16)

ch_how = Doodle(760, 280, "A hash ring with virtual nodes. Keys and nodes are hashed onto the same circle. Each key belongs to the first node clockwise. Each physical node appears at many points on the ring (virtual nodes), so the load is even and a new node takes small slices from every other node, about one fifth of the keys when going from four nodes to five.",
                "Keys and nodes share one ring; each key goes to the next node clockwise.")
cx, cy, r = 190, 140, 105
ch_how.circle(cx, cy, r, fill="paper")
cols = ["blue", "green", "y", "pink"]
for k in range(12):
    a = _m.radians(-90 + k * 30)
    ch_how.circle(round(cx + r * _m.cos(a)), round(cy + r * _m.sin(a)), 9, fill=cols[k % 4])
ch_how.arrow(round(cx + 60), round(cy - 30), round(cx + r * _m.cos(_m.radians(-60)) - 10), round(cy + r * _m.sin(_m.radians(-60)) + 6), color="pen", curve=(cx + 95, cy - 50))
ch_how.text(cx + 52, cy - 22, "key", "t-s", size=14)
ch_how.note(370, 70, "4 nodes × 3 virtual points each (colours)", anchor="start", size=15)
ch_how.note(370, 104, "a key → the next point clockwise", anchor="start", size=15)
ch_how.note(370, 150, "add a 5th node: ≈ 1/5 of keys move,", "green", anchor="start", size=15)
ch_how.note(370, 174, "a little from every other node", "green", anchor="start", size=15)
ch_how.note(370, 220, "replicas: the next 2 distinct nodes clockwise", "pen", anchor="start", size=15)

CONSISTENT_HASHING = dict(
    slug="consistent-hashing",
    kicker="a.k.a. “add a node, move only a few keys”",
    tldr="Spreading keys with <code>hash(key) % N</code> works until N changes: then almost every key moves. <b>Consistent hashing</b> places nodes and keys on the same <b>ring</b>; each key belongs to the next node clockwise. Adding or removing a node moves only the keys next to it, about <b>1/N</b> of them. <b>Virtual nodes</b> (many points per server) keep the load even. Used by caches, sharded databases and load balancers that need stickiness.",
    chips=[("Family", "scaling data"), ("Introduced", "Karger et al. (1997), for web caches"), ("Variants", "virtual nodes · jump hash · rendezvous (HRW) hashing"), ("Used by", "Cassandra, DynamoDB, Memcached clients, Envoy ring-hash")],
    problem="""  <p class="lead">A cache cluster spreads keys with <code>hash(key) % 4</code>. Traffic grows and a fifth node is added: now it's <code>% 5</code>, and <span class="hl-pink">about 80% of keys map to a different node</span>. Almost every lookup misses at once, and the database behind the cache takes the full load.</p>
  <ul>
    <li>Adding capacity <b>causes</b> an incident instead of preventing one.</li>
    <li>Losing a node is just as bad: every key's home shifts.</li>
    <li>For sharded data, “moving” means copying most of the data between machines.</li>
  </ul>""",
    problem_figs=[ch_problem],
    analogy_side="a round table",
    analogy="""  <p>Guests have name cards placed around a <b>round table</b>, and each is served by the first host clockwise from their card. When a <b>new host sits down</b>, only the guests between the new chair and the previous host move to the new host. Everyone else keeps their host.</p>""",
    analogy_figs=[ch_analogy],
    map=[("The round table", "The hash ring (0 to 2³² − 1, wrapping around)"),
         ("A guest's card position", "hash(key)"),
         ("A host's chair", "hash(node), placed on the same ring"),
         ("Served by the next host clockwise", "Key → first node at or after its position"),
         ("One host in several chairs", "Virtual nodes, for an even spread")],
    how_side="a ring, virtual nodes, the next node clockwise",
    how="""  <p>Hash every node many times (say 100–200 <b>virtual nodes</b> each) onto a ring, and keep the points sorted. For a key, hash it and find the first point at or after it (a binary search). To store copies, walk on to the next distinct nodes. A new node's points land all around the ring, so it takes a small slice from every other node.</p>""",
    how_figs=[ch_how],
    steps=[("Hash nodes onto a ring", "Each node at many points: hash(\"node-3#0\") … hash(\"node-3#149\"). Keep the points sorted."),
           ("Look up by the next point", "Hash the key, binary-search for the first point ≥ it, wrap to the start if needed."),
           ("Use virtual nodes", "100–200 points per node keep the spread within a few percent; give bigger machines more points."),
           ("Replicate along the ring", "Store copies on the next 2 distinct physical nodes clockwise."),
           ("Move only what changed", "When a node joins or leaves, only the keys between it and its neighbour points move; copy those, nothing else.")],
    vocab=[("Hash ring", "The hash space treated as a circle."),
           ("Virtual node", "One of many ring positions belonging to the same physical node."),
           ("Key movement", "The share of keys that change node when membership changes."),
           ("Jump hash", "A fast, memory-free variant for numbered buckets (Lamping & Veach)."),
           ("Rendezvous hashing", "Each key picks the node with the highest hash(key, node)."),
           ("Hot spot", "A node that gets more than its share of keys or traffic.")],
    code=dict(file="ring.ts", note="TypeScript, no library", src="""
import { createHash } from "node:crypto";
const h = (s: string) => createHash("md5").update(s).digest().readUInt32BE(0);

export class Ring {
  private points: { at: number; node: string }[] = [];

  constructor(nodes: string[], private vnodes = 150) { nodes.forEach((n) => this.add(n)); }

  add(node: string) {                       // many points per node keep the spread even
    for (let i = 0; i < this.vnodes; i++) this.points.push({ at: h(`${node}#${i}`), node });
    this.points.sort((a, b) => a.at - b.at);
  }

  remove(node: string) { this.points = this.points.filter((p) => p.node !== node); }

  nodeFor(key: string): string {            // first point at or after hash(key), wrapping around
    const k = h(key);
    let lo = 0, hi = this.points.length;
    while (lo < hi) { const mid = (lo + hi) >> 1; if (this.points[mid].at < k) lo = mid + 1; else hi = mid; }
    return this.points[lo % this.points.length].node;
  }
}
// 4 → 5 nodes: about 20% of keys move. With hash % N it would be about 80%.
"""),
    tools="tools: Envoy and NGINX ring-hash / Maglev load balancing, Memcached clients (ketama), Cassandra and ScyllaDB token rings, DynamoDB partitioning, Redis Cluster (16,384 fixed slots: the same goal by another route), Go <code>hashring</code> and Java Guava <code>Hashing.consistentHash</code>.",
    gains=["<b>Adding or removing a node moves ~1/N of keys</b>, not almost all.",
           "<b>Smooth scaling</b> of caches and shards.",
           "<b>Even load</b> with virtual nodes, weighted by machine size.",
           "<b>Natural replica placement</b>: the next nodes on the ring."],
    losses=["<b>More complex</b> than a modulo.",
            "<b>Uneven without virtual nodes</b>: a few points per node gives lumpy load.",
            "<b>Hot keys</b> still land on one node; the ring doesn't split a key.",
            "<b>Every client must agree</b> on the ring, or keys are looked up in the wrong place."],
    baseline="Each line compares <b><code>hash(key) % N</code></b> to <b>a consistent-hash ring with virtual nodes</b>.",
    ratings=[(5, 4, "A small, well-known algorithm or a library."),
             (4, 4, "Neutral."),
             (3, 4, "Nodes can be added during the day without a miss storm."),
             (4, 4, "Deterministic; easy to unit-test the movement share."),
             (2, 5, "Grow the cluster a node at a time."),
             (2, 4, "Add and remove nodes for peaks without flushing the cache."),
             (2, 4, "A lost node only affects its own keys."),
             (4, 4, "A binary search per lookup: microseconds."),
             (3, 4, "Membership changes become routine.")],
    pitfalls=[("Too few virtual nodes", "Each server at one point on the ring: one server owns 40% of the keys.", "use 100–200 virtual nodes per server and check the spread."),
              ("Clients with different rings", "Two app versions hash with different functions or node lists, and look in different places.", "share one membership source and one hash function; roll changes out everywhere together."),
              ("Expecting it to fix hot keys", "One popular key still lands on one node.", "cache hot keys locally, or split them (key#0…key#7)."),
              ("Forgetting the data move", "For stored data, the ring says where keys belong now, but the bytes are still on the old node.", "copy the moved ranges before switching, or read from both during the move.")],
    use=["Caches and shards whose node count changes.",
         "Sticky routing: the same user or session to the same backend.",
         "Placing replicas in a peer-to-peer or leaderless store."],
    skip=["The node count never changes; a modulo is simpler.",
          "A fixed number of logical shards with a map already solves movement (see Sharding).",
          "One managed service already does the placement for you (DynamoDB, Redis Cluster)."],
    related=["<b>Sharding</b> · logical shards are the other answer", "<b>Cache-aside</b>", "<b>Leader–follower replication</b>", "<b>Service discovery</b>"],
    quiz=[("Why does hash % N move most keys when N changes?", "The result depends on N, so for most keys the remainder changes: going from 4 to 5 nodes moves about 80% of keys."),
          ("On a ring, which node owns a key?", "The first node position at or after the key's hash, going clockwise and wrapping around."),
          ("What problem do virtual nodes solve?", "Uneven load: many points per node spread each node's share evenly around the ring."),
          ("Roughly what share of keys moves when going from 4 to 5 nodes?", "About one fifth: the new node takes small slices from each of the others.")],
    quiz_sit=[("A Memcached cluster of 6 nodes uses consistent hashing, but one node handles 35% of the traffic. Its key share is normal (about 17%). What's going on, and what do you do?",
               "The keys are spread evenly, but a few hot keys on that node get far more requests. Consistent hashing can't split a single key: add a small local cache in the app for the hottest keys, or split them into several sub-keys, and track requests per key to find them.")],
    try_it="Hash 100,000 random keys onto 4 nodes with <code>hash % 4</code>, then with <code>% 5</code>, and count how many keys changed node. Do the same with the ring above (150 virtual nodes), then with only 1 virtual node per server, and compare both the share of keys that moved and the largest node's share.",
    remember="Nodes and keys on <span class=\"hl\">one ring</span>. A new node takes <span class=\"hl\">a little from everyone</span>, not everything from everyone.",
    sources=["David Karger et al., “Consistent Hashing and Random Trees” (STOC 1997).",
             "Giuseppe DeCandia et al., “Dynamo: Amazon's Highly Available Key-value Store” (SOSP 2007).",
             "John Lamping and Eric Veach, “A Fast, Minimal Memory, Consistent Hash Algorithm” (2014).",
             "David Thaler and Chinya Ravishankar, “Using Name-Based Mappings to Increase Hit Rates” (rendezvous hashing, 1998)."],
)

NOTES = [STRANGLER_FIG, BACKPRESSURE, CONSISTENT_HASHING]
