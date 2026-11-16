# Vol. 1 · going deeper (November 2026): a longer chapter inside three key notes.
# Saga, the resilience patterns, the outbox and event sourcing already have full deep dives (Series 3), so they get none here.
# Merged into the notes by scripts/build_notes.py (load_content).

# ------------------------------------------------------------------ API gateway
gw_d1 = Doodle(760, 300, "A product page request fans out from the gateway to three services, with a 1.5 second budget. Product and Prices answer in 80 and 120 milliseconds. Reviews is slow and hits its 300 millisecond timeout. The gateway returns the page with product and price and an empty reviews section marked as unavailable, in 310 milliseconds, instead of waiting or failing the whole page.",
               "One slow backend costs one section of the page, not the page.")
gw_d1.box(20, 110, 130, 70, "client", "paper", sub="budget 1.5 s", size=18, subsize=14)
gw_d1.arrow(154, 145, 226, 145)
gw_d1.box(230, 100, 150, 90, "gateway", "y", sub="per-call timeouts", size=19, subsize=14)
for i, (name, t, ok) in enumerate([("Product", "80 ms ✓", True), ("Prices", "120 ms ✓", True), ("Reviews", "timeout at 300 ms", False)]):
    y = 20 + i * 92
    gw_d1.arrow(384, 145, 496, y + 32, color="" if ok else "red", dash=not ok)
    gw_d1.box(500, y, 240, 64, name, "green" if ok else "pink", stroke="" if ok else "red", sub=t, size=17, subsize=14)
gw_d1.note(300, 236, "answer in 310 ms:", anchor="middle", size=17)
gw_d1.note(300, 262, "product + price + “reviews unavailable”", "green", size=17)

gw_d2 = Doodle(760, 280, "Ownership of a shared gateway. A platform team runs the gateway itself: instances, TLS, authentication and default limits. Each product team owns the route file for its own paths in its own repository, reviewed by that team, for example orders routes and search routes. The mobile team owns its own backend for frontend behind the gateway.",
               "The platform team runs the gateway; each team owns its own routes.")
gw_d2.box(240, 20, 280, 80, "gateway (platform team)", "y", sub="instances · TLS · auth · default limits", size=17, subsize=14)
for i, (name, sub) in enumerate([("orders routes", "Orders team repo"), ("search routes", "Search team repo"), ("mobile BFF", "Mobile team")]):
    x = 20 + i * 250
    gw_d2.box(x, 170, 220, 70, name, "blue" if i < 2 else "green", sub=sub, size=17, subsize=14)
    gw_d2.arrow(x + 110, 166, 380, 104, dash=True)
gw_d2.note(380, 268, "a change to orders routes needs only the Orders team", "pen", size=17)

API_GATEWAY_DEEP = dict(
    side="budgets and partial answers, staying up, who owns it",
    intro="The note lists the gateway's jobs. This chapter is about running one: how timeouts work when one request fans out to several services, how to keep the front door from becoming the single thing that takes everything down, and how to share it between teams without it becoming one team's bottleneck.",
    parts=[
        ("Timeout budgets and partial answers", """  <p>A request that enters the gateway has a <b>budget</b>: how long the client will wait. Every call the gateway makes on its behalf spends from it. If the mobile app gives up after 1.5 seconds, a backend timeout of 5 seconds is pointless: the gateway would still be waiting long after nobody is listening.</p>
  <p>So set timeouts from the outside in. Client budget 1.5 s; the gateway's own limit a little below that; each backend call a fraction of it, based on that backend's normal p99 (Reviews normally answers in 120 ms, so 300 ms is generous). Pass the remaining budget along in a header so services deeper down can give up early too.</p>
  <p>When the gateway combines several calls into one response, decide in advance which parts are <b>required</b> and which are <b>optional</b>. Product and price are required: without them the page is useless, so fail the request. Reviews and recommendations are optional: return the page without them, with a field that says so (<code>"reviews": {"status": "unavailable"}</code>), and let the client show a placeholder.</p>""", [gw_d1]),
        ("The front door must not fall over", """  <p>Every request passes through the gateway, so its availability caps everyone else's. A few rules keep it boring:</p>
  <ul>
    <li><b>Keep it stateless.</b> No sessions, no local caches that matter. Then any instance can serve any request and you can add or replace instances freely.</li>
    <li><b>At least two instances in at least two zones,</b> behind the cloud load balancer, with health checks. Three if a deploy takes one out.</li>
    <li><b>Shared counters for shared limits.</b> A limit of 100 requests a minute per client, counted locally on 4 instances, really allows 400. Keep the counters in Redis, or divide the limit by the instance count and accept the rough edge.</li>
    <li><b>Config is code.</b> Routes and policies live in git, are tested in CI, and roll out like a deploy: to one instance first. A bad route rule is the most common way a gateway takes everything down.</li>
    <li><b>Protect the backends from the gateway.</b> A breaker per backend route, so one failing service doesn't tie up the gateway's connections for the rest.</li>
  </ul>""", []),
        ("Sharing it between teams", """  <p>A gateway owned and edited by one team turns every new endpoint into a ticket in that team's queue. A gateway everyone edits freely turns into a pile of special cases. The usual answer splits ownership:</p>
  <ul>
    <li>The <b>platform team</b> runs the gateway itself: instances, TLS certificates, authentication, default limits, logging.</li>
    <li>Each <b>product team</b> owns the routes for its own paths, in its own repository, reviewed by its own people. Kubernetes' Gateway API is built this way: one Gateway, many HTTPRoute objects owned by different teams.</li>
    <li>Clients with very different needs (the mobile app) get their own <b>backend for frontend</b>, owned by the client team, behind the shared gateway.</li>
  </ul>
  <p>Add guardrails the platform team checks automatically: no team may claim another team's path prefix, every route must have a timeout, and anything beyond routing (reshaping responses, business rules) goes in a service, not in gateway config.</p>""", [gw_d2]),
    ],
)

# ------------------------------------------------------------------ Service discovery
sd_d1 = Doodle(760, 280, "Long-lived connections and new instances. A client opened three HTTP/2 connections when Payments had two pods, and keeps reusing them. Payments scales out to four pods, but the two new pods receive no traffic, because no new connections are opened. With a maximum connection age, connections are closed every few minutes and reopened across all four pods.",
               "Discovery answers once per connection. Long-lived connections keep using the old answer.")
sd_d1.box(20, 100, 130, 80, "client", "paper", sub="3 HTTP/2 conns", size=18, subsize=14)
for i, (name, busy) in enumerate([("pod 1", True), ("pod 2", True), ("pod 3 (new)", False), ("pod 4 (new)", False)]):
    y = 14 + i * 64
    sd_d1.box(500, y, 200, 50, name, "green" if busy else "paper", stroke="" if busy else "red", size=16)
for y in (28, 50, 103):
    sd_d1.arrow(154, 140, 496, y)
sd_d1.note(20, 222, "pods 3 and 4: idle", "red", anchor="start", size=17)
sd_d1.note(20, 252, "fix: max connection age,", "pen", anchor="start", size=17)
sd_d1.note(20, 274, "or a client that rebalances", "pen", anchor="start", size=17)

sd_d2 = Doodle(760, 260, "Shutting down a pod without errors. At time zero the pod receives SIGTERM and the platform starts removing it from discovery, which takes a few seconds to reach every caller. During a preStop wait of 10 seconds the pod keeps serving. Then the app stops taking new requests, finishes in-flight ones, and exits well before the 30 second grace period ends.",
               "Wait until the callers have heard, then drain, then exit.")
sd_d2.arrow(20, 170, 744, 170)
for x, w, top, sub, fill in [(20, 140, "SIGTERM", "0 s", "pink"), (180, 190, "preStop wait", "0–10 s · still serving", "y"), (390, 200, "drain", "10–20 s · finish requests", "blue"), (610, 130, "exit", "~20 s", "green")]:
    sd_d2.box(x, 40, w, 80, top, fill, sub=sub, size=17, subsize=13)
    sd_d2.line(f"M{x + 10} 124 V166", thin=True)
sd_d2.note(250, 214, "meanwhile: removal spreads to every caller (seconds)", "pen", size=17)
sd_d2.note(250, 244, "grace period 30 s: the hard deadline", size=16)

SERVICE_DISCOVERY_DEEP = dict(
    side="cached answers, clean shutdowns, staying in the zone",
    intro="The note covers registering, health and lookup. In production, most discovery bugs aren't in the registry. They come from answers that are cached too long, from instances that disappear before callers know, and from traffic that crosses zones without anyone noticing. This chapter covers all three.",
    parts=[
        ("Answers that stick", """  <p>A lookup is only as fresh as the place it is cached. Three caches catch people out:</p>
  <ul>
    <li><b>DNS caches.</b> Records have a time to live, but some runtimes ignore it (older JVM settings cached DNS for ever). Check what your runtime does, and keep TTLs short, around 5–30 seconds, for service names.</li>
    <li><b>Connection pools.</b> A pool opens connections once and reuses them. The lookup happens at connect time, so a pool full of connections to old instances keeps using them until they break.</li>
    <li><b>Long-lived HTTP/2 and gRPC connections.</b> One connection carries thousands of requests. When Payments scales from two pods to four, existing clients keep sending everything to the first two. The fix is a <b>maximum connection age</b> on the server (gRPC has a setting for this), or client-side load balancing that watches the registry and spreads requests across all instances.</li>
  </ul>
  <p>A good test: scale a service from 2 to 6 instances under load and check that the new instances get their share within a minute.</p>""", [sd_d1]),
        ("Leaving without errors", """  <p>Most errors during deploys come from instances that stop before every caller knows they're gone. In Kubernetes, the pod gets SIGTERM and its removal from the endpoints list happen <b>at the same time</b>, and the removal takes a few seconds to reach every caller and proxy. If the app exits at once, those callers send requests to a closed port.</p>
  <p>The usual order:</p>
  <ol>
    <li><b>Keep serving for a few seconds</b> after SIGTERM (a preStop hook that sleeps 5–10 s), so the removal spreads.</li>
    <li><b>Stop accepting new connections,</b> finish in-flight requests, close keep-alive connections politely.</li>
    <li><b>Exit</b> well before the grace period (30 s by default) runs out, or the platform kills the process mid-request.</li>
  </ol>
  <p>Do the same on the way in: a new instance should only become ready once it can really serve (connections open, caches warm), so readiness, not liveness, decides when traffic starts.</p>""", [sd_d2]),
        ("Staying in your zone", """  <p>Spread across three zones, a service with round-robin load balancing sends two thirds of its calls to another zone. That adds a millisecond or two each way and, in most clouds, a charge for every gigabyte that crosses zones. For chatty services it becomes a visible line on the bill.</p>
  <ul>
    <li><b>Prefer the same zone</b> when it has healthy instances, and fall back to others when it doesn't (Kubernetes topology-aware routing, or zone-aware load balancing in a mesh).</li>
    <li><b>Keep enough instances per zone.</b> Zone preference with one instance per zone means one slow pod gets a third of all traffic.</li>
    <li><b>Eject outliers.</b> An instance that passes its health check but returns errors or slow answers should be taken out of rotation for a while (outlier detection). Health checks see the instance from the outside; outlier detection sees what callers actually get.</li>
  </ul>""", []),
    ],
)

# ------------------------------------------------------------------ Sharding
sh_d1 = Doodle(760, 300, "Logical shards on physical machines. Customers are hashed into 1,024 logical shards. A small map assigns ranges of logical shards to four database machines. To add a fifth machine, some logical shards are copied to it, kept in sync, and then their lines in the map are changed. No customer's shard number ever changes.",
               "Hash into many logical shards once; move whole shards between machines later.")
sh_d1.box(20, 30, 170, 70, "customer 81723", "paper", sub="hash % 1024 = 517", size=16, subsize=14)
sh_d1.arrow(194, 65, 246, 65)
sh_d1.table(250, 20, "shard map", ["0–255 → db-1", "256–511 → db-2", "512–767 → db-3", "768–1023 → db-4"], w=210, fill="y", hl=(2,), size=16)
sh_d1.arrow(464, 116, 520, 150)
for i, name in enumerate(["db-1", "db-2", "db-3", "db-4"]):
    sh_d1.db(560 + (i % 2) * 110, 30 + (i // 2) * 100, name, w=70, fill="green" if name == "db-3" else "paper")
sh_d1.note(380, 238, "adding db-5: copy shards 640–767 · catch up · change one line", "pen", size=17)
sh_d1.note(380, 270, "the customer's shard (517) never changes", size=16)

sh_d2 = Doodle(760, 250, "Scatter-gather across eight shards. A query that needs all shards waits for the slowest. Seven shards answer in 20 milliseconds and one in 400, so the whole query takes 400 milliseconds. The more shards a query touches, the more likely one of them is slow.",
               "A query to every shard is as slow as the slowest shard.")
sh_d2.box(20, 90, 130, 70, "query", "paper", sub="needs all 8", size=18, subsize=14)
for i in range(8):
    slow = i == 5
    x = 210 + i * 66
    sh_d2.box(x, 70, 56, 110, None, "pink" if slow else "green", stroke="red" if slow else "")
    sh_d2.text(x + 28, 118, f"s{i + 1}", "t-head", size=16)
    sh_d2.text(x + 28, 148, "400" if slow else "20", size=14)
sh_d2.arrow(154, 125, 204, 125)
sh_d2.note(480, 216, "result in 400 ms, not 20: the slowest one decides", "red", size=17)

SHARDING_DEEP = dict(
    side="moving shards, hot keys, queries across shards",
    intro="The note explains how to choose a shard key and why to plan for resharding. This chapter shows what that plan looks like when you carry it out, what to do about a single key that is hotter than a whole shard, and how to deal with the queries and transactions that don't fit inside one shard.",
    parts=[
        ("Moving shards, not keys", """  <p>Hash each key into a large, fixed number of <b>logical shards</b> (say 1,024) and keep a small <b>shard map</b> that says which physical database holds which logical shards. The key-to-shard step never changes; only the map does.</p>
  <p>Adding a machine then means moving some logical shards to it:</p>
  <ol>
    <li><b>Copy</b> the rows of the moving shards to the new machine (a snapshot), then <b>stream</b> later changes to it (logical replication or CDC) until it is a few seconds behind.</li>
    <li><b>Pause writes</b> for those shards for a moment, let the copy catch up completely, and <b>change their lines in the map</b>.</li>
    <li>Callers pick up the new map (watch it, or check its version on each request) and go to the new machine. <b>Delete</b> the old copies a few days later.</li>
  </ol>
  <p>Each move touches a fraction of the data and pauses only those shards. This is what Vitess, Citus and MongoDB's balancer do for you; with your own router you build it once and run it many times.</p>""", [sh_d1]),
        ("When one key is hotter than a shard", """  <p>A good key spreads load evenly on average, but averages hide single keys. One celebrity account with 50 million followers, one product in a flash sale, one tenant who imports a year of data on a Monday: all of that lands on one shard, and moving shards doesn't help, because a key can't be split across them.</p>
  <ul>
    <li><b>Reads:</b> cache the hot item in front of the database; a hot key is usually a few rows read many times.</li>
    <li><b>Writes:</b> split the key. Store counters as <code>post:42#0</code> to <code>post:42#7</code> on different shards, add to a random one, and sum the eight on read.</li>
    <li><b>Known giants:</b> give a very large tenant its own shard or its own database, and route to it from the map.</li>
  </ul>
  <p>Measure per key, not just per shard: the top 20 keys by requests and by writes, every day. Hot keys show up there weeks before they cause an incident.</p>""", []),
        ("Queries and transactions across shards", """  <p>A query without the shard key has to ask every shard and merge the answers (scatter-gather). Two problems grow with the number of shards. Load: every such query costs every shard something. And latency: the query waits for the slowest shard, so its p99 is roughly the worst of eight (or sixty-four) p99s.</p>
  <ul>
    <li><b>Keep a second copy shaped for the question.</b> Search, reports and “all orders for this product” go to a store built for them (a search index, a warehouse) fed by CDC, not to the shards.</li>
    <li><b>Global lookups</b> (email to customer id) get their own small table, itself sharded by email, or a cache.</li>
    <li><b>Small reference tables</b> (countries, currencies) are copied to every shard so joins stay local.</li>
  </ul>
  <p>Avoid transactions across shards. Choose the key so a business operation stays on one shard (a customer and their orders together). When an operation really spans shards, such as moving money between two customers on different shards, use a saga or the outbox, not a distributed transaction.</p>""", [sh_d2]),
    ],
)

REVISIONS = {
    "api-gateway": dict(deep_dive=API_GATEWAY_DEEP),
    "service-discovery": dict(deep_dive=SERVICE_DISCOVERY_DEEP),
    "sharding": dict(deep_dive=SHARDING_DEEP),
}
