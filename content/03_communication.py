# Communication collection: API Gateway, Publish-Subscribe, Competing Consumers, Sidecar & Service Mesh, Service Discovery.

# ------------------------------------------------------------------ 10 API Gateway
gw_problem = Doodle(760, 280, "Doodle of a mobile app calling six different microservices directly, each with its own address, auth check and data format. The app makes many slow round trips and every service re-implements authentication, rate limits and logging.",
                    "Clients talking to every service directly: many round trips, many addresses, the same chores done six times.")
gw_problem.icon("phone", 20, 100, 1.6)
for i, name in enumerate(["Users", "Catalog", "Cart", "Orders", "Reviews", "Shipping"]):
    y = 20 + i * 42
    gw_problem.box(500, y, 140, 34, name, "blue", size=17, rx=6)
    gw_problem.arrow(80, 140, 494, y + 17, color="red" if i in (1, 4) else "")
gw_problem.note(280, 270, "6 round trips per screen · 6 auth checks · 6 URLs in the app", "red")
gw_problem.note(700, 140, "each does", "pen")
gw_problem.note(700, 164, "auth, limits,", "pen")
gw_problem.note(700, 188, "logging…", "pen")

gw_analogy = Doodle(760, 260, "Doodle of a hotel front desk with a bell. Guests only ever go to the front desk. The desk checks their key card, then sends requests to housekeeping, the kitchen or the spa behind the scenes.",
                    "Guests deal with one front desk. It checks who you are and passes your request to the right team.")
gw_analogy.icon("key", 20, 90, 1.2)
gw_analogy.note(55, 170, "guest key card")
gw_analogy.arrow(100, 126, 230, 126)
gw_analogy.box(240, 70, 180, 110, "front desk", "y")
gw_analogy.icon("bell", 300, 30, .8)
gw_analogy.arrow(426, 100, 560, 50)
gw_analogy.arrow(426, 126, 560, 126)
gw_analogy.arrow(426, 150, 560, 200)
gw_analogy.box(566, 26, 170, 46, "housekeeping", "green", size=18)
gw_analogy.box(566, 104, 170, 46, "kitchen", "green", size=18)
gw_analogy.box(566, 182, 170, 46, "spa", "green", size=18)
gw_analogy.note(330, 230, "checks the card once", "pen")

gw_how = Doodle(760, 320, "API gateway in the middle. Web, mobile and partner clients call one public endpoint. The gateway terminates TLS, authenticates, rate limits, routes by path, aggregates several backend calls into one response, and logs and traces every request before forwarding to internal services.",
                "One public front door. Cross-cutting chores happen once, then requests are routed to the right service.")
for i, c in enumerate(["web", "mobile", "partner"]):
    gw_how.box(20, 40 + i * 90, 110, 50, c, "paper", size=18)
    gw_how.arrow(136, 65 + i * 90, 236, 150)
gw_how.box(246, 30, 230, 260, None, "y")
gw_how.head(361, 62, "API gateway", size=22)
for i, t in enumerate(["TLS + auth (JWT)", "rate limit", "route /orders → Orders", "aggregate calls", "logs · metrics · traces"]):
    gw_how.text(266, 102 + i * 38, "✓ " + t, anchor="start", size=17)
for i, s in enumerate(["Users", "Orders", "Catalog", "Reviews"]):
    y = 40 + i * 66
    gw_how.box(590, y, 140, 46, s, "blue", size=18)
    gw_how.arrow(482, 160, 584, y + 23)
gw_how.note(536, 312, "internal network", "pen")

GATEWAY = dict(
    slug="api-gateway",
    kicker="a.k.a. “one front door”",
    tldr="Put a single entry point in front of your services. Clients call <b>the gateway</b>; it handles the shared chores (<b>TLS, authentication, rate limiting, logging</b>), <b>routes</b> each request to the right internal service, and can <b>combine several calls</b> into one response.",
    chips=[("Family", "communication / edge"), ("Lives in", "the edge of your system"), ("Variant", "Backends for Frontends (BFF)"), ("Pairs with", "rate limiter, service discovery, circuit breaker")],
    problem="""  <p class="lead">With microservices, one screen might need data from five or six services. If clients call them <span class="hl-pink">directly</span>, problems pile up.</p>
  <ul>
    <li><b>Chatty clients:</b> a mobile app on a slow network makes six round trips to draw one screen.</li>
    <li><b>Leaky internals:</b> clients know every service's address and API, so you can't split, merge or move services without breaking apps.</li>
    <li><b>Duplicated chores:</b> each service re-implements authentication, rate limits, CORS, logging and TLS, all slightly differently.</li>
    <li><b>Security surface:</b> every service is exposed to the internet.</li>
  </ul>""",
    problem_figs=[gw_problem],
    analogy_side="the hotel front desk",
    analogy="""  <p>In a hotel you don't wander into the kitchen to order food or find housekeeping's office for towels. You go to <b>the front desk</b>. They check your key card once, take the request, and pass it to the right team behind the scenes.</p>
  <ul>
    <li>Guests only need to know <b>one place</b>. The hotel can reorganise its teams without telling anyone.</li>
    <li>The desk can <b>combine</b> requests: “late checkout and a taxi” in one conversation.</li>
    <li>If the desk is closed, nobody gets anything. It must be <b>well staffed and always open</b>.</li>
  </ul>""",
    analogy_figs=[gw_analogy],
    map=[("Guests", "Clients: web, mobile, partners"),
         ("The front desk", "The API gateway"),
         ("Checking the key card", "Authentication (e.g. validating a JWT)"),
         ("Passing requests to the right team", "Routing to internal services"),
         ("“Late checkout and a taxi” in one go", "Request aggregation"),
         ("Teams behind the scenes", "Internal services, not exposed publicly")],
    how_side="handle chores once, then route",
    how="""  <p>The gateway is a reverse proxy with extra powers. Typical jobs, roughly in order for each request:</p>""",
    how_figs=[gw_how],
    steps=[("Terminate TLS", "HTTPS ends at the gateway; inside, services can use mTLS via the mesh."),
           ("Authenticate and authorise", "Validate the token once, then pass the user's identity to services in a header."),
           ("Protect", "Rate limits per client, request size limits, IP allow/deny lists, WAF rules."),
           ("Route and transform", "Map public paths to internal services (<code>/api/orders/*</code> → Orders), translate protocols (REST → gRPC), version APIs."),
           ("Aggregate and observe", "Optionally fan out to several services and merge the results; log, measure and trace every request.")],
    how_after="""  <h3>One gateway or one per client type?</h3>
  <div class="grid2">
    <div class="sticky"><h3>Single gateway</h3><p>One edge for everyone. Simple to run, but can grow into a shared “god” layer every team has to change.</p></div>
    <div class="sticky sticky--blue"><h3>Backends for Frontends (BFF)</h3><p>A small gateway per client type (web BFF, mobile BFF), owned by that frontend team and shaped for its screens.</p></div>
  </div>""",
    vocab=[("Reverse proxy", "A server that forwards client requests to backend servers."),
           ("Edge", "The boundary where outside traffic enters your system."),
           ("Request aggregation", "One client call fanned out to several services, merged."),
           ("BFF", "Backend for Frontend: a gateway tailored to one client type."),
           ("TLS termination", "Decrypting HTTPS at the gateway."),
           ("North–south traffic", "Traffic between clients and your system (vs east–west inside).")],
    code=dict(file="gateway.yaml", note="declarative routes (generic example)", src="""
routes:
  - path: /api/orders/*
    service: http://orders.internal:8080
    plugins:
      - jwt-auth: { issuer: "https://login.example.com" }
      - rate-limit: { per_key: 100/min }
      - timeout: 2s
  - path: /api/catalog/*
    service: http://catalog.internal:8080
    plugins:
      - cache: { ttl: 60s }
  - path: /api/home          # one call, three services
    aggregate:
      - GET http://users.internal/me
      - GET http://catalog.internal/featured
      - GET http://orders.internal/recent?limit=3
"""),
    tools="products: Kong, NGINX, Envoy Gateway, Traefik, AWS API Gateway, Azure API Management, Google Apigee, Spring Cloud Gateway, YARP (.NET). GraphQL federation is a popular aggregation flavour.",
    gains=["<b>One stable public API</b>; internals can change freely behind it.",
           "<b>Cross-cutting concerns in one place</b>: auth, limits, TLS, logging.",
           "<b>Fewer round trips</b> for clients through aggregation.",
           "<b>Smaller attack surface</b>: services stay on the private network.",
           "<b>Easier API versioning</b> and gradual migrations (e.g. strangler fig)."],
    losses=["<b>An extra network hop</b> on every request.",
            "<b>A critical component</b>: if it's down, everything is down.",
            "<b>Can become a bottleneck</b> for teams if all changes go through it.",
            "<b>Business logic creep</b>: it slowly turns into a monolith.",
            "<b>Another thing to scale, secure and monitor.</b>"],
    baseline="Each line compares clients calling <b>services directly</b> to the same system with an <b>API gateway</b> at the edge.",
    ratings=[(3, 3, "One more component, but clients and services both get simpler."),
             (4, 3, "Gateway infrastructure or a managed service to pay for."),
             (2, 4, "Services can move, split and version behind a stable public API."),
             (3, 3, "Routing and auth rules need their own tests."),
             (3, 4, "Gateways scale horizontally; caching at the edge helps."),
             (3, 4, "Limits and caching absorb spikes before they hit services."),
             (3, 3, "Contains abuse, but adds a critical shared component."),
             (3, 3, "One extra hop, often offset by aggregation and caching."),
             (2, 4, "Internals can be reshaped without breaking clients.")],
    pitfalls=[("Business logic in the gateway", "Discount rules and order validation creep into gateway scripts until it's a hidden monolith.", "keep it to routing and cross-cutting concerns; logic stays in services."),
              ("One gateway owned by one team", "Every feature needs a ticket to the platform team to add a route.", "self-service config, or BFFs owned by the client teams."),
              ("Single instance, single zone", "The gateway pod restarts and the whole product is down.", "run several instances across zones behind a load balancer."),
              ("No timeouts or breakers on backends", "One slow service fills the gateway's connections and everything stalls.", "per-route timeouts, circuit breakers and bulkheads."),
              ("Aggregation without partial results", "Reviews is down, so the whole home page fails.", "return what you have, mark missing parts, use fallbacks.")],
    use=["Several services are used by external or mobile clients.",
         "You need consistent auth, rate limiting and logging at the edge.",
         "Clients would otherwise need many round trips per screen.",
         "You want to hide or evolve the internal structure."],
    skip=["One service and one client: a plain load balancer is enough.",
          "Service-to-service traffic inside the cluster (that's the mesh's job).",
          "You'd put business rules in it.",
          "Latency budgets so tight that one hop matters (rare)."],
    related=["<b>Backends for Frontends</b>", "<b>Rate limiter</b>", "<b>Service discovery</b>", "<b>Sidecar &amp; service mesh</b>", "<b>Strangler fig</b> · migrate behind it"],
    quiz=[("Name three cross-cutting concerns a gateway typically handles.", "Any three of: TLS termination, authentication, rate limiting, logging/metrics/tracing, CORS, caching, request size limits."),
          ("What's a BFF and why use one?", "A Backend for Frontend: a gateway per client type, owned by that frontend team and shaped for its screens, so one shared gateway doesn't become a bottleneck."),
          ("How do you stop the gateway being a single point of failure?", "Run multiple instances across zones behind a load balancer, keep it stateless, and add timeouts and breakers to backend calls."),
          ("Gateway vs service mesh: which handles north–south traffic?", "The gateway handles north–south (clients ↔ system); the mesh handles east–west (service ↔ service).")],
    remember="One <span class=\"hl\">front door</span> for clients, many rooms behind it. Keep the door smart about security, and dumb about business.",
    sources=["Chris Richardson, microservices.io, “Pattern: API Gateway / Backends for Frontends”.",
             "Sam Newman, “Backends For Frontends” (samnewman.io).",
             "Microsoft Azure Architecture Center, “Gateway Routing / Aggregation / Offloading patterns”.",
             "Sam Newman, <i>Building Microservices</i>, 2nd ed., chapter on the edge."],
)

# ------------------------------------------------------------------ 11 Publish-Subscribe
ps_problem = Doodle(760, 270, "Doodle of point-to-point coupling. When an order is placed, the Order service has to call Email, Shipping, Analytics and Loyalty directly, one after another. Adding a new interested service means changing and redeploying Order, and if Analytics is slow, placing an order is slow.",
                    "The sender has to know, call and wait for every interested service. Adding one more means changing the sender.")
ps_problem.box(20, 100, 160, 70, "Order", "blue")
for i, name in enumerate(["Email", "Shipping", "Analytics", "Loyalty"]):
    y = 20 + i * 60
    ps_problem.box(470, y, 150, 44, name, "pink" if name == "Analytics" else "paper", size=18, stroke="red" if name == "Analytics" else "")
    ps_problem.arrow(186, 135, 464, y + 22, color="red" if name == "Analytics" else "")
ps_problem.note(680, 150, "slow", "red")
ps_problem.note(330, 262, "new team wants order events? → edit + redeploy Order ✗", "red")

ps_analogy = Doodle(760, 280, "Doodle of a radio station tower broadcasting a show. Many radios tune in to the station's channel. The station doesn't know or care how many radios are listening, and new listeners can tune in any time.",
                    "The station broadcasts once. Anyone who's tuned in hears it; the station never calls listeners.")
ps_analogy.icon("tower", 60, 60, 2.2)
ps_analogy.note(125, 230, "station: “Order placed!”")
for i, (x, y) in enumerate([(430, 10), (430, 70), (430, 130), (430, 190)]):
    ps_analogy.box(x, y, 110, 50, ["kitchen", "driver", "billing", "new!"][i], "green" if i < 3 else "y", size=17)
    ps_analogy.arrow(200, 100, x - 6, y + 25, dash=True)
ps_analogy.note(600, 274, "tune in any time, no one tells the station", "pen")

ps_how = Doodle(760, 290, "Publish-subscribe flow. The Order service publishes one OrderPlaced event to the orders topic on a broker. Email, Shipping, Analytics and a new Fraud service each have their own subscription and receive a copy independently, at their own pace.",
                "Publish once to a topic. Every subscription gets its own copy and reads at its own pace.")
ps_how.box(20, 110, 140, 64, "Order", "blue")
ps_how.arrow(166, 142, 256, 142, label="OrderPlaced", lx=212, ly=128)
ps_how.box(262, 80, 200, 124, None, "y")
ps_how.head(362, 110, "topic: orders", size=19)
ps_how.msgs(292, 140, 5, fill="paper", size=22)
for i, name in enumerate(["Email", "Shipping", "Analytics", "Fraud (new)"]):
    y = 20 + i * 66
    ps_how.box(590, y, 150, 46, name, "green" if i < 3 else "y", size=18)
    ps_how.arrow(468, 142, 584, y + 23)
ps_how.note(540, 286, "each subscriber: own copy, own speed", "pen")

PUBSUB = dict(
    slug="publish-subscribe",
    kicker="a.k.a. “announce it, don't call around”",
    tldr="When something happens, the producer <b>publishes one event to a topic</b> and moves on. Any number of services <b>subscribe</b> to that topic and each receives its own copy. The producer <b>doesn't know who's listening</b>, so you can add new consumers without touching it.",
    chips=[("Family", "communication / messaging"), ("Lives in", "a message broker (topics)"), ("Also called", "event-driven, fan-out"), ("Pairs with", "outbox, idempotent consumer, saga (choreography)")],
    problem="""  <p class="lead">With direct calls, the service where something happens must <span class="hl-pink">know about, call and wait for</span> every service that cares.</p>
  <ul>
    <li><b>Tight coupling:</b> Order has hard-coded calls to Email, Shipping, Analytics and Loyalty.</li>
    <li><b>Slow and fragile:</b> if Analytics is slow or down, placing an order is slow or fails.</li>
    <li><b>Hard to extend:</b> a new Fraud service wants order events, so the Order team must change and redeploy.</li>
    <li><b>Wrong ownership:</b> Order's code ends up full of other teams' concerns.</li>
  </ul>""",
    problem_figs=[ps_problem],
    analogy_side="the radio station",
    analogy="""  <p>A radio station <b>broadcasts</b> a show on its frequency. It doesn't phone each listener. Anyone who has <b>tuned in</b> hears it; anyone who hasn't, doesn't.</p>
  <ul>
    <li>The station doesn't know or care how many radios are on. A new listener can tune in without the station changing anything.</li>
    <li>A radio that's switched off simply misses it. (Brokers improve on radio: <b>durable subscriptions</b> keep messages until the subscriber comes back.)</li>
    <li>Different stations for different topics: news, sport, traffic.</li>
  </ul>""",
    analogy_figs=[ps_analogy],
    map=[("The radio station", "The publisher (producer)"),
         ("A frequency / channel", "A topic"),
         ("Tuning in", "Creating a subscription"),
         ("Each radio plays its own copy", "Each subscription gets every message"),
         ("Station doesn't know who's listening", "Producer is decoupled from consumers"),
         ("Recording the show to listen later", "Durable subscription / retained log")],
    how_side="topics and subscriptions",
    how="""  <p>A broker sits in the middle. Producers write to <b>topics</b>; consumers read through <b>subscriptions</b>. Each subscription receives every message, independently of the others.</p>""",
    how_figs=[ps_how],
    steps=[("Name events as facts", "<code>OrderPlaced</code>, <code>PaymentFailed</code>: past tense, about the producer's domain, not instructions to a consumer."),
           ("Publish reliably", "Use the transactional outbox so the event is published if and only if the change committed."),
           ("Subscribe per consumer", "Each consuming service gets its own subscription (or Kafka consumer group), so it reads at its own pace."),
           ("Handle duplicates and order", "Expect at-least-once delivery; make handlers idempotent. Order is usually only guaranteed per key/partition."),
           ("Version the contract", "Add fields, don't rename or remove them. Publish a schema (Avro, JSON Schema, Protobuf) and check compatibility.")],
    how_after="""  <div class="grid2">
    <div class="sticky"><h3>Thin event</h3><p><code>OrderPlaced { id: 42 }</code>. Small and safe, but consumers may call back for details.</p></div>
    <div class="sticky sticky--green"><h3>Fat event (event-carried state)</h3><p><code>OrderPlaced { id, items, total, address }</code>. Consumers have what they need; bigger and harder to change.</p></div>
  </div>""",
    vocab=[("Topic", "A named channel events are published to."),
           ("Subscription", "A consumer's registration to receive a topic's messages."),
           ("Fan-out", "One published message delivered to many consumers."),
           ("Durable subscription", "Messages are kept while the subscriber is offline."),
           ("Consumer group", "Kafka's version of a subscription shared by a service's instances."),
           ("Schema registry", "A store of event schemas with compatibility checks.")],
    code=dict(file="order-events.ts", note="publish once; subscribers are independent", src="""
// producer: knows the topic, not the consumers
await outbox.add({ topic: "orders", type: "OrderPlaced",
                   key: order.id, data: { id: order.id, total: order.total } });

// consumer 1 (Email service, its own subscription)
broker.subscribe("orders", { group: "email" }, async (e) => {
  if (e.type === "OrderPlaced") await sendReceipt(e.data.id);   // idempotent!
});

// consumer 2, added months later; Order never changed
broker.subscribe("orders", { group: "fraud-check" }, async (e) => {
  if (e.type === "OrderPlaced") await scoreRisk(e.data);
});
"""),
    tools="brokers: Apache Kafka, RabbitMQ (fanout / topic exchanges), Google Pub/Sub, AWS SNS + SQS, Azure Service Bus topics, NATS, Redis Streams.",
    gains=["<b>Loose coupling.</b> Producers don't know or call consumers.",
           "<b>Easy to extend.</b> New consumers subscribe without changes to the producer.",
           "<b>Faster, more resilient producers</b>; slow consumers don't slow them down.",
           "<b>Each consumer scales and fails independently.</b>",
           "<b>A record of business events</b> others can build on."],
    losses=["<b>Eventual consistency</b> between producer and consumers.",
            "<b>Harder to follow the flow.</b> “Who reacts to OrderPlaced?” needs tooling.",
            "<b>Duplicates and ordering</b> must be handled by consumers.",
            "<b>Event contracts are public APIs</b>; changing them is hard.",
            "<b>A broker to run</b>, secure and monitor."],
    baseline="Each line compares a producer that <b>calls each interested service directly</b> to the same system using <b>publish–subscribe through a broker</b>.",
    ratings=[(4, 3, "Flows are less visible; you need tracing and an event catalogue."),
             (4, 3, "A broker to run (or pay for)."),
             (2, 4, "Producers and consumers deploy independently."),
             (3, 3, "Unit tests are easy; end-to-end flows need async test tooling."),
             (2, 5, "Consumers scale out independently; brokers handle huge volumes."),
             (2, 4, "Brokers buffer spikes; consumers catch up later."),
             (2, 4, "A down consumer doesn't affect the producer or other consumers."),
             (3, 4, "Producer returns quickly; total processing is async."),
             (2, 5, "New features subscribe without touching existing services.")],
    pitfalls=[("Events that are commands in disguise", "<code>SendWelcomeEmail</code> on a shared topic: the producer is still telling a specific consumer what to do.", "publish facts (<code>UserRegistered</code>); consumers decide what to do."),
              ("Breaking the event schema", "A field is renamed and three teams' consumers crash on deploy.", "additive changes only, schema registry, versioned events."),
              ("Assuming global order", "Consumers assume <code>OrderCancelled</code> always arrives after <code>OrderPlaced</code>, but they're on different partitions.", "partition by entity key; handle out-of-order events."),
              ("Event spaghetti", "50 services reacting to each other's events; nobody can explain a checkout end to end.", "an event catalogue, tracing, and orchestration for long flows."),
              ("Publishing without an outbox", "The DB commit succeeds but the publish fails, so consumers never hear.", "transactional outbox.")],
    use=["Several services need to react to the same business event.",
         "You want to add consumers over time without changing producers.",
         "The producer shouldn't wait for consumers to finish.",
         "Integrating bounded contexts owned by different teams."],
    skip=["The caller needs an answer now (use a request/response call).",
          "Exactly one known receiver should do a specific task (use a queue / command).",
          "Strict, immediate consistency between producer and consumers is required.",
          "A tiny system where a direct call is clearer."],
    related=["<b>Transactional outbox</b>", "<b>Idempotent consumer</b>", "<b>Competing consumers</b>", "<b>Saga</b> · choreography", "<b>Event sourcing</b>"],
    quiz=[("What's the difference between a topic subscription and a work queue?", "In pub/sub every subscription gets a copy of every message; in a work queue each message goes to just one of the competing consumers."),
          ("Why name events in the past tense?", "They describe facts that already happened in the producer's domain, so consumers decide how to react, which keeps the producer decoupled."),
          ("How do you guarantee events for one order arrive in order?", "Use the order id as the partition/message key, so all its events go to one partition and are read in sequence."),
          ("A new Fraud service wants order events. What changes in the Order service?", "Nothing. Fraud creates its own subscription to the existing topic.")],
    remember="Say it <span class=\"hl\">once</span>, to the topic. Whoever cares will hear, now or later, and you never have to know their names.",
    sources=["Gregor Hohpe &amp; Bobby Woolf, <i>Enterprise Integration Patterns</i>, “Publish-Subscribe Channel”.",
             "Martin Fowler, “What do you mean by Event-Driven?”.",
             "Microsoft Azure Architecture Center, “Publisher-Subscriber pattern”.",
             "Confluent / Apache Kafka docs, “Consumer groups and partitions”."],
)

# ------------------------------------------------------------------ 12 Competing Consumers
cc_problem = Doodle(760, 260, "Doodle of a single worker processing image resizes from a backlog. At 9 a.m. 10,000 uploads arrive, the single worker handles 20 per second, so users wait over eight minutes, and if that worker crashes everything stops.",
                    "One worker can't keep up with the spike, and if it dies, all processing stops.")
cc_problem.box(20, 100, 140, 64, "uploads", "blue")
cc_problem.arrow(166, 132, 236, 132, color="red", label="10,000 at 9:00", lx=200, ly=196)
cc_problem.box(242, 92, 270, 80, None, "pink", stroke="red")
cc_problem.msgs(256, 120, 10, fill="y", size=20, gap=5)
cc_problem.note(377, 82, "backlog keeps growing", "red")
cc_problem.arrow(518, 132, 588, 132)
cc_problem.box(594, 100, 150, 64, "1 worker", "paper", sub="20 / s")
cc_problem.note(380, 230, "10,000 ÷ 20/s = 500 s ≈ 8 min wait · worker dies → everything stops", "red")

cc_analogy = Doodle(760, 260, "Doodle of a supermarket with one shared queue feeding several checkout lanes. The next customer goes to whichever cashier is free. When it gets busy, the manager opens more lanes.",
                    "One queue, many cashiers. The next person goes to whoever is free; busy day → open more lanes.")
cc_analogy.msgs(30, 120, 6, fill="blue", size=26, gap=8)
cc_analogy.note(110, 100, "one shared queue")
cc_analogy.arrow(240, 128, 360, 60)
cc_analogy.arrow(240, 128, 360, 128)
cc_analogy.arrow(240, 128, 360, 196, dash=True)
cc_analogy.box(366, 36, 160, 50, "till 1 · busy", "y", size=17)
cc_analogy.box(366, 104, 160, 50, "till 2 · free", "green", size=17)
cc_analogy.box(366, 172, 160, 50, "till 3 · opened", "paper", size=17, dash=True)
cc_analogy.icon("store", 600, 70, 1.6)
cc_analogy.note(660, 200, "busy? open more tills", "pen")

cc_how = Doodle(760, 300, "Competing consumers. Producers put jobs on one queue. Several identical worker instances pull from it; each message is locked by one worker and deleted only when it's acknowledged. If a worker crashes, its message becomes visible again for another worker. Failed messages go to a dead-letter queue after N tries. An autoscaler adds workers based on queue length.",
                "Each message is handled by exactly one worker. Crashes hand it to another; poison messages go to the DLQ.")
cc_how.box(20, 110, 130, 60, "producers", "blue")
cc_how.arrow(156, 140, 226, 140)
cc_how.box(232, 100, 230, 80, None, "y")
cc_how.msgs(248, 128, 8, fill="paper", size=20, gap=6)
cc_how.head(347, 94, "work queue", size=18)
for i in range(3):
    y = 30 + i * 80
    cc_how.box(590, y, 150, 56, f"worker {i + 1}", "green", size=18)
    cc_how.arrow(468, 140, 584, y + 28, label="pull · lock · ack" if i == 0 else None, lx=520, ly=56)
cc_how.box(232, 230, 230, 50, "dead-letter queue", "pink", stroke="red", size=18)
cc_how.arrow(347, 184, 347, 226, color="red", label="after 5 failures", lx=357, ly=212, anchor="start")
cc_how.note(665, 290, "autoscale on queue length", "pen")

COMPETING = dict(
    slug="competing-consumers",
    kicker="a.k.a. “one queue, many hands”",
    tldr="Put work items on <b>one queue</b> and run <b>several identical workers</b> that pull from it. Each message is processed by <b>exactly one</b> worker. Add workers when the queue grows, remove them when it shrinks. The queue also <b>absorbs spikes</b>, so producers never wait for the work to finish.",
    chips=[("Family", "communication / messaging"), ("Lives in", "a message queue + a worker pool"), ("Also called", "work queue, queue-based load levelling"), ("Pairs with", "idempotent consumer, autoscaling, dead-letter queue")],
    problem="""  <p class="lead">Some work is slow or bursty: resizing images, sending emails, generating PDFs, importing files. Doing it <b>inside the request</b> makes users wait, and doing it with <b>one worker</b> <span class="hl-pink">can't keep up</span>.</p>
  <ul>
    <li>At 9 a.m., 10,000 uploads arrive. One worker at 20 per second needs over 8 minutes.</li>
    <li>If that worker crashes, nothing is processed at all.</li>
    <li>Sizing for the peak wastes money the rest of the day; sizing for the average melts at the peak.</li>
  </ul>""",
    problem_figs=[cc_problem],
    analogy_side="the supermarket checkout",
    analogy="""  <p>A well-run supermarket has <b>one queue feeding several tills</b>. The next customer goes to whichever cashier is free. Nobody gets stuck behind a slow lane, and when the queue gets long the manager <b>opens more tills</b>.</p>
  <ul>
    <li>Each customer is served by exactly one cashier.</li>
    <li>If a cashier has to leave mid-scan, the customer goes back to the front of the queue for the next one.</li>
    <li>A customer whose card fails five times is sent to customer service instead of blocking the line (the <b>dead-letter queue</b>).</li>
  </ul>""",
    analogy_figs=[cc_analogy],
    map=[("The shared queue of shoppers", "The message queue"),
         ("Cashiers", "Identical worker instances (consumers)"),
         ("Next shopper to the next free till", "Each message delivered to one worker"),
         ("Opening more tills when busy", "Autoscaling workers on queue length"),
         ("Cashier leaves mid-scan → back to the queue", "No ack → message becomes visible again"),
         ("Sent to customer service after 5 failed cards", "Dead-letter queue after N attempts")],
    how_side="pull, lock, process, acknowledge",
    how="""  <p>The queue hands each message to one consumer and <b>hides it</b> from the others while it's being worked on. Only an <b>acknowledgement</b> removes it for good.</p>""",
    how_figs=[cc_how],
    steps=[("Producers enqueue and return", "The web request just adds <code>ResizeImage {id: 42}</code> to the queue and responds “processing”."),
           ("Workers pull", "Each worker takes a message (or a small batch). The broker locks it for a visibility timeout, e.g. 60 s."),
           ("Process, then ack", "Do the work, then acknowledge. If the worker crashes or the timeout passes, the message reappears for another worker."),
           ("Handle poison messages", "After N failed attempts, move the message to a dead-letter queue and alert, so it doesn't block or loop forever."),
           ("Scale on the backlog", "Autoscale workers on queue depth or age of the oldest message (KEDA, SQS + ASG). Make handlers idempotent: redelivery happens.")],
    vocab=[("Work queue", "A queue where each message goes to one consumer."),
           ("Visibility timeout / lock", "How long a taken message stays hidden from others."),
           ("Ack / nack", "Tell the broker the message is done / failed."),
           ("Dead-letter queue (DLQ)", "Where messages go after too many failures."),
           ("Queue-based load levelling", "Using a queue to smooth bursts into a steady rate."),
           ("Prefetch", "How many messages a consumer takes at once.")],
    code=dict(file="resize-worker.ts", note="run N copies of this", src="""
// producer (web request): enqueue and return immediately
await queue.send("image-resize", { imageId: "img-42" });
res.status(202).json({ status: "processing" });

// worker: run as many copies as you need
for await (const msg of queue.receive("image-resize", { visibilityTimeout: 60 })) {
  try {
    await resize(msg.body.imageId);          // idempotent: same output if repeated
    await msg.ack();                         // only now is it removed
  } catch (err) {
    if (msg.attempts >= 5) await msg.deadLetter(String(err));
    else await msg.nack({ delaySeconds: 2 ** msg.attempts });   // retry later
  }
}
"""),
    tools="queues: AWS SQS, RabbitMQ, Azure Service Bus queues, Google Cloud Tasks, Kafka consumer groups (one partition per consumer), Celery / Sidekiq / BullMQ job queues; autoscale with KEDA.",
    gains=["<b>Throughput scales</b> by adding workers.",
           "<b>Spikes are absorbed</b> by the queue (load levelling).",
           "<b>Workers fail independently</b>; messages move to a healthy one.",
           "<b>Producers respond fast</b>; slow work happens in the background.",
           "<b>Cost-efficient</b>: scale workers with the backlog, even to zero."],
    losses=["<b>No ordering guarantee</b> across workers.",
            "<b>Duplicates</b> when a worker crashes after doing the work.",
            "<b>Work is asynchronous</b>; users need status updates.",
            "<b>Poison messages and DLQs</b> need monitoring and tooling.",
            "<b>Shared downstream limits</b>: 50 workers can overload one database."],
    baseline="Each line compares doing background work in <b>one worker (or inside the request)</b> to <b>a queue with a pool of competing workers</b>.",
    ratings=[(4, 3, "Queues, acks, retries and DLQs to understand."),
             (3, 4, "Scale workers with demand instead of sizing for the peak."),
             (3, 4, "Workers deploy and roll independently of producers."),
             (3, 3, "Handlers are easy to test; async flows and redelivery need more."),
             (2, 5, "Add workers for more throughput, nearly linearly."),
             (2, 5, "The queue absorbs bursts; autoscaling follows the backlog."),
             (2, 4, "A crashed worker's message goes to another one."),
             (3, 4, "Requests return immediately; total time depends on backlog."),
             (3, 4, "New job types are new queues and workers.")],
    pitfalls=[("Handlers that aren't idempotent", "A worker resizes and uploads, then crashes before ack; another worker does it again and charges the CDN twice.", "idempotent handlers keyed by message id."),
              ("Visibility timeout shorter than the work", "Jobs take 90 s, the lock lasts 60 s, so a second worker starts the same job.", "timeout above the p99 job time, or extend the lock while working."),
              ("No dead-letter queue", "One malformed message fails forever and keeps being retried, wasting workers.", "max attempts → DLQ, plus an alert and a replay tool."),
              ("Assuming order", "“Account created” and “account updated” are processed by different workers in the wrong order.", "partition by key (FIFO groups / Kafka keys) when order matters."),
              ("Scaling workers past the bottleneck", "100 workers all hit one database with 50 connections.", "cap workers to what downstream can take; use bulkheads.")],
    use=["Work is slow, bursty or can happen in the background.",
         "Throughput must scale with demand.",
         "Each job is independent of the others.",
         "Users can accept “we're processing it”."],
    skip=["The caller needs the result in the same request.",
          "Strict global ordering is required.",
          "Volume is tiny and steady.",
          "Every consumer should see every message (that's pub/sub)."],
    related=["<b>Publish–subscribe</b>", "<b>Idempotent consumer</b>", "<b>Retry with backoff</b>", "<b>Bulkhead</b>", "<b>Rate limiter</b>"],
    quiz=[("Pub/sub vs competing consumers: who gets a message?", "In pub/sub every subscription gets a copy; with competing consumers exactly one worker in the pool gets each message."),
          ("A worker crashes halfway through a job. What happens to the message?", "It was never acknowledged, so after the visibility timeout it becomes visible again and another worker picks it up."),
          ("What is a dead-letter queue for?", "Messages that keep failing are moved there after N attempts, so they stop blocking or wasting workers and can be inspected and replayed."),
          ("What metric should drive autoscaling?", "Queue depth or the age of the oldest message, not CPU alone.")],
    remember="One queue, many hands. <span class=\"hl\">Ack only when done</span>, expect redelivery, and send the troublemakers to the dead-letter queue.",
    sources=["Gregor Hohpe &amp; Bobby Woolf, <i>Enterprise Integration Patterns</i>, “Competing Consumers”.",
             "Microsoft Azure Architecture Center, “Competing Consumers” and “Queue-Based Load Leveling”.",
             "AWS SQS docs, “Visibility timeout” and “Dead-letter queues”.",
             "RabbitMQ tutorial 2, “Work Queues”."],
)

# ------------------------------------------------------------------ 13 Sidecar & Service Mesh
sc_problem = Doodle(760, 270, "Doodle of four services written in Java, Go, Node and Python. Each team has re-implemented retries, timeouts, mutual TLS, metrics and tracing in its own language, with different bugs and versions.",
                    "Every service, in every language, re-implements the same networking chores, each slightly differently.")
for i, (lang, fill) in enumerate([("Java", "blue"), ("Go", "green"), ("Node", "y"), ("Python", "pink")]):
    x = 20 + i * 186
    sc_problem.box(x, 40, 170, 180, None, fill)
    sc_problem.head(x + 85, 70, lang + " svc", size=19)
    for k, t in enumerate(["retries v1.2", "timeouts?", "mTLS (own)", "metrics", "tracing v0.9"]):
        sc_problem.text(x + 85, 104 + k * 24, t, size=15)
sc_problem.note(380, 254, "4 languages × 5 chores = 20 slightly different implementations", "red")

sc_analogy = Doodle(760, 300, "Doodle of a motorcycle with a sidecar attached. The rider drives; the passenger in the sidecar handles the map, the radio and the luggage. The sidecar goes everywhere the motorcycle goes.",
                    "The rider focuses on riding. The sidecar handles navigation and radio, and goes wherever the bike goes.")
sc_analogy.icon("sidecar", 200, 40, 2.6)
sc_analogy.note(200, 284, "rider = your service: business logic", "pen")
sc_analogy.note(560, 284, "sidecar = proxy: map, radio, luggage", "pen")
sc_analogy.arrow(600, 60, 470, 110, label="handles the chores", lx=640, ly=50)

sc_how = Doodle(760, 320, "Service mesh with sidecars. Each pod contains the application container and a sidecar proxy. All traffic in and out goes through the sidecars, which add mTLS, retries, timeouts, load balancing and telemetry. A control plane pushes configuration and certificates to every sidecar.",
                "Apps talk to localhost; the sidecars talk to each other securely. The control plane configures them all.")
for i, (x, name) in enumerate([(30, "Orders"), (430, "Payments")]):
    sc_how.box(x, 120, 300, 130, None, "paper", dash=True)
    sc_how.note(x + 12, 270, "pod", size=18, anchor="start")
    app_x, proxy_x = (x + 16, x + 160) if i == 0 else (x + 160, x + 16)
    sc_how.box(app_x, 140, 124 if i else 130, 90, name, "blue", sub="app")
    sc_how.box(proxy_x, 140, 124 if i == 0 else 130, 90, "proxy", "y", sub="sidecar")
    if i == 0:
        sc_how.arrow(x + 146, 185, x + 160, 185)
    else:
        sc_how.arrow(x + 160, 185, x + 146, 185)
sc_how.arrow(314, 200, 446, 200, color="green", label="mTLS · retries · timeouts · metrics", lx=380, ly=300)
sc_how.box(250, 20, 260, 56, "control plane", "green")
sc_how.arrow(330, 82, 252, 136, dash=True, label="config + certs", lx=40, ly=100, anchor="start")
sc_how.arrow(430, 82, 510, 136, dash=True)

SIDECAR = dict(
    slug="sidecar",
    kicker="a.k.a. “a helper that rides along”",
    tldr="Run a <b>helper process next to each service instance</b> (in the same pod or host) that handles the networking chores: <b>mTLS, retries, timeouts, load balancing, metrics and tracing</b>. The app just talks to <code>localhost</code>. A <b>service mesh</b> is a fleet of these sidecars managed by one control plane.",
    chips=[("Family", "communication / infrastructure"), ("Lives in", "the same pod/host as each service"), ("Examples", "Envoy, Linkerd, Istio, Dapr"), ("Pairs with", "service discovery, circuit breaker, retries")],
    problem="""  <p class="lead">Every service needs the same plumbing to talk safely over a network. When each team builds it <span class="hl-pink">into the app</span>, you get a mess.</p>
  <ul>
    <li>Retries, timeouts and circuit breakers are re-implemented in Java, Go, Node and Python, each with different defaults and bugs.</li>
    <li>Rolling out mutual TLS means changing and redeploying every service.</li>
    <li>Metrics and traces look different in every service, so dashboards don't line up.</li>
    <li>Changing a retry policy needs a code change and a release.</li>
  </ul>""",
    problem_figs=[sc_problem],
    analogy_side="the motorcycle sidecar",
    analogy="""  <p>A motorcycle with a <b>sidecar</b>: the rider concentrates on riding, while the passenger in the sidecar reads the map, works the radio and minds the luggage. The sidecar is <b>attached</b>, so it goes wherever the bike goes, and can be swapped without rebuilding the bike.</p>
  <ul>
    <li>The rider doesn't need to learn navigation; the sidecar does it for every bike the same way.</li>
    <li>A fleet of bikes, each with a sidecar, all following directions from one dispatcher: that's a <b>mesh with a control plane</b>.</li>
  </ul>""",
    analogy_figs=[sc_analogy],
    map=[("The rider", "Your service's business logic"),
         ("The sidecar passenger", "A proxy process next to the service"),
         ("Map, radio, luggage", "mTLS, retries, timeouts, telemetry"),
         ("Attached, goes everywhere the bike goes", "Deployed and scaled with each instance"),
         ("Dispatcher radioing all sidecars", "The mesh control plane"),
         ("Swap the sidecar, keep the bike", "Upgrade networking without changing app code")],
    how_side="move plumbing out of the app",
    how="""  <p>The sidecar intercepts the app's inbound and outbound traffic (often transparently, via iptables or eBPF). The app makes a plain call to <code>http://payments</code>; the sidecar does the rest.</p>""",
    how_figs=[sc_how],
    steps=[("Deploy a proxy next to every instance", "In Kubernetes, a second container in each pod, usually injected automatically."),
           ("Route traffic through it", "Outbound calls go to the local proxy; inbound traffic arrives through it too."),
           ("Let it handle the chores", "mTLS between services, retries and timeouts, load balancing, circuit breaking / outlier detection, metrics and traces."),
           ("Configure centrally", "A control plane (Istio, Linkerd) pushes policies and certificates to every sidecar, without app redeploys."),
           ("Keep app-level concerns in the app", "Business retries (e.g. “retry payment with another provider”) and idempotency still belong in code.")],
    how_after="""  <p class="aside">the sidecar idea isn't only for networking: log shippers, config reloaders, Dapr (state, pub/sub, secrets) and cloud SQL proxies are sidecars too. Some meshes now also run “sidecar-less” (Istio ambient, Cilium) with per-node proxies.</p>""",
    vocab=[("Sidecar", "A helper container deployed alongside the main one."),
           ("Service mesh", "A layer of proxies handling service-to-service traffic."),
           ("Data plane", "The proxies that carry the traffic."),
           ("Control plane", "The brain that configures the proxies."),
           ("mTLS", "Mutual TLS: both sides prove their identity with certificates."),
           ("East–west traffic", "Traffic between services inside the system.")],
    code=dict(file="payments-policy.yaml", note="Istio-style config, no app change", src="""
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata: { name: payments }
spec:
  hosts: [payments]
  http:
    - timeout: 2s
      retries: { attempts: 3, perTryTimeout: 600ms, retryOn: "5xx,reset,connect-failure" }
      route: [{ destination: { host: payments } }]
---
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata: { name: payments }
spec:
  host: payments
  trafficPolicy:
    tls: { mode: ISTIO_MUTUAL }                       # mTLS everywhere
    outlierDetection: { consecutive5xxErrors: 5, baseEjectionTime: 30s }
"""),
    tools="meshes and sidecars: Istio (Envoy), Linkerd, Consul Connect, Cilium service mesh, AWS App Mesh (retiring), Dapr sidecar; plain Envoy works as a standalone sidecar.",
    gains=["<b>Consistent networking</b> for every service, in every language.",
           "<b>Zero-trust security</b> (mTLS) without app changes.",
           "<b>Uniform metrics and traces</b> across the fleet.",
           "<b>Change policies live</b> without redeploying apps.",
           "<b>Simpler app code</b>, focused on business logic."],
    losses=["<b>Extra latency</b> (two proxy hops per call, usually around a millisecond).",
            "<b>More CPU and memory</b> per pod.",
            "<b>Operational complexity</b>: the mesh itself must be run and upgraded.",
            "<b>Harder debugging</b> when the proxy is doing something surprising.",
            "<b>Overkill</b> for a handful of services."],
    baseline="Each line compares services that <b>build networking into each app</b> to the same services using <b>sidecars / a service mesh</b>.",
    ratings=[(3, 2, "Apps get simpler, but the mesh is a big system to learn."),
             (4, 3, "Extra CPU/memory per pod and people to run the mesh."),
             (3, 4, "Traffic shifting and canaries become config."),
             (3, 3, "Fault injection gets easier; the mesh adds another layer to test."),
             (4, 4, "Neutral; load balancing gets smarter."),
             (3, 3, "Neutral."),
             (3, 4, "Consistent timeouts, retries and outlier detection everywhere."),
             (4, 3, "A little added latency on every hop."),
             (3, 4, "Network policies change without touching app code.")],
    pitfalls=[("Double retries", "The app retries 3 times and the sidecar retries 3 times: 9 calls per failure.", "retry in one layer; turn off library retries or mesh retries."),
              ("Mesh for three services", "A team adopts Istio for a tiny system and spends more time on the mesh than on features.", "start with a library or a gateway; adopt a mesh when the fleet is big."),
              ("Ignoring resource limits", "Sidecars without limits eat node memory and get pods evicted.", "set sidecar CPU/memory requests and limits."),
              ("Startup race", "The app starts before its sidecar is ready and its first calls fail.", "native sidecar containers / hold-app-until-proxy-starts settings."),
              ("Thinking the mesh solves idempotency", "Mesh retries a POST that wasn't safe to repeat.", "only retry idempotent routes; keep idempotency keys in the app.")],
    use=["Many services in several languages need consistent networking.",
         "You need mTLS / zero-trust between services.",
         "You want uniform telemetry and traffic control (canaries, shifting).",
         "A platform team can own and run the mesh."],
    skip=["A handful of services in one language: a shared library is simpler.",
          "Ultra-low-latency paths where every millisecond counts.",
          "No one can own the mesh's upgrades and incidents.",
          "Serverless or managed platforms that already handle this."],
    related=["<b>API gateway</b> · north–south", "<b>Service discovery</b>", "<b>Circuit breaker</b>", "<b>Retry with backoff</b>", "<b>Ambassador / adapter</b> (sidecar variants)"],
    quiz=[("What's the difference between the data plane and the control plane?", "The data plane is the proxies that carry traffic; the control plane configures them and hands out certificates."),
          ("Why can a mesh roll out mTLS without changing services?", "The sidecars encrypt and authenticate the traffic between them; apps keep talking plain HTTP to localhost."),
          ("App retries 3× and mesh retries 3×. Worst case calls per request?", "3 × 3 = 9. Retry in one layer only."),
          ("Name one cost of the sidecar pattern.", "Extra latency per hop, extra CPU/memory per pod, or operational complexity of running the mesh.")],
    remember="Let the app <span class=\"hl\">ride</span>; let the sidecar <span class=\"hl\">navigate</span>. Same plumbing everywhere, changed in one place.",
    sources=["Brendan Burns, <i>Designing Distributed Systems</i>, “The Sidecar Pattern”.",
             "Microsoft Azure Architecture Center, “Sidecar pattern” and “Ambassador pattern”.",
             "Istio docs, “Architecture” and “Traffic Management”.",
             "William Morgan, “The Service Mesh: What Every Software Engineer Needs to Know” (Buoyant)."],
)

# ------------------------------------------------------------------ 14 Service Discovery
sd_problem = Doodle(760, 260, "Doodle of a config file with hard-coded IP addresses for the Payments service. Kubernetes and autoscaling keep creating and destroying instances with new addresses, so the caller keeps calling dead addresses and missing new ones.",
                    "Instances come and go with new addresses. A hard-coded list is out of date within minutes.")
sd_problem.box(20, 50, 220, 150, None, "paper")
sd_problem.head(130, 40, "config.yaml", size=18)
for i, ip in enumerate(["10.0.1.12", "10.0.1.15", "10.0.1.19"]):
    sd_problem.text(40, 90 + i * 34, "payments: " + ip, anchor="start", size=17)
sd_problem.arrow(246, 100, 430, 60, color="red", label="dead ✗", lx=340, ly=64)
sd_problem.arrow(246, 130, 430, 130, color="red", label="dead ✗", lx=340, ly=122)
sd_problem.arrow(246, 160, 430, 200, dash=True)
sd_problem.box(436, 30, 130, 50, "10.0.1.12", "pink", stroke="red", size=16, dash=True)
sd_problem.box(436, 106, 130, 50, "10.0.1.15", "pink", stroke="red", size=16, dash=True)
sd_problem.box(436, 182, 130, 50, "10.0.1.19", "green", size=16)
sd_problem.box(610, 70, 130, 50, "10.0.3.7", "green", size=16)
sd_problem.box(610, 150, 130, 50, "10.0.3.9", "green", size=16)
sd_problem.note(675, 50, "new, unknown", "pen")

sd_analogy = Doodle(760, 240, "Doodle of a phone directory and a phone. You look up a business by name in the directory and get its current number, instead of memorising numbers that change. Businesses update their own entry when they move.",
                    "You look up a name and get the current number. Businesses update their own entry when they move.")
sd_analogy.icon("phone", 40, 80, 1.6)
sd_analogy.arrow(110, 120, 260, 120, label="“Payments?”", lx=185, ly=108)
sd_analogy.icon("directory", 270, 70, 1.8)
sd_analogy.arrow(400, 120, 540, 120, label="10.0.3.7, 10.0.3.9", lx=470, ly=108)
sd_analogy.icon("store", 560, 70, 1.4)
sd_analogy.note(600, 190, "moved? updates its listing", "pen")
sd_analogy.arrow(600, 200, 340, 210, dash=True, curve=(470, 240))

sd_how = Doodle(760, 340, "Service discovery flow. Payments instances register themselves with a service registry and send heartbeats. The registry removes instances that miss heartbeats or fail health checks. The Orders service, or its sidecar or a load balancer, asks the registry for healthy Payments instances and load-balances across them. In Kubernetes, DNS and endpoints do this for you.",
                "Instances register and heartbeat; callers look up healthy instances by name.")
sd_how.box(270, 20, 220, 90, "service registry", "y", sub="name → healthy instances")
for i, ip in enumerate(["10.0.3.7", "10.0.3.9", "10.0.4.2"]):
    y = 150 + i * 52
    sd_how.box(550, y, 200, 42, "payments " + ip, "green", size=15)
    sd_how.arrow(546, y + 21, 470, 112, dash=True)
sd_how.note(610, 140, "register + heartbeat", "pen")
sd_how.box(20, 180, 180, 70, "Orders", "blue")
sd_how.arrow(110, 176, 280, 100, label="① lookup “payments”", lx=20, ly=140, anchor="start")
sd_how.arrow(206, 230, 542, 216, color="green", label="② call a healthy one", lx=370, ly=250)
sd_how.note(380, 330, "Kubernetes: Service DNS + EndpointSlices do this for you", "pen")

DISCOVERY = dict(
    slug="service-discovery",
    kicker="a.k.a. “look it up, don't hard-code it”",
    tldr="In the cloud, service instances <b>come and go with new addresses</b>. Instead of hard-coding IPs, each instance <b>registers</b> in a <b>service registry</b> (and keeps sending heartbeats); callers <b>look up a name</b> and get the current list of <b>healthy instances</b> to load-balance across.",
    chips=[("Family", "communication / infrastructure"), ("Lives in", "registry + client, proxy or DNS"), ("Examples", "Kubernetes DNS, Consul, Eureka"), ("Pairs with", "health checks, load balancing, sidecars")],
    problem="""  <p class="lead">In a data centre of the past, servers had fixed addresses for years. Today, <span class="hl-pink">instances are cattle, not pets</span>: autoscaling, deploys, spot instances and crashes create and destroy them all day.</p>
  <ul>
    <li>A hard-coded list of IPs is wrong within minutes: callers hit dead instances and miss new ones.</li>
    <li>Scaling Payments from 3 to 10 instances doesn't help if callers only know about the old 3.</li>
    <li>A crashed instance keeps receiving traffic until someone edits the config.</li>
    <li>Different environments (dev, staging, prod) need different addresses everywhere.</li>
  </ul>""",
    problem_figs=[sd_problem],
    analogy_side="the phone directory",
    analogy="""  <p>You don't memorise the phone number of every shop. You look it up by <b>name</b> in the directory (or a maps app) and get the <b>current</b> number. When a shop moves, <b>it</b> updates its listing; you don't have to do anything.</p>
  <ul>
    <li>Shops that close are removed, so you don't call dead numbers (health checks + heartbeats).</li>
    <li>A chain lists several branches; you pick the nearest or least busy one (load balancing).</li>
    <li>You might keep a recent lookup on a sticky note for a while (client-side caching with a TTL).</li>
  </ul>""",
    analogy_figs=[sd_analogy],
    map=[("A shop's name", "A logical service name (“payments”)"),
         ("Its current phone number(s)", "The current instance addresses"),
         ("The directory", "The service registry"),
         ("Shop updates its own listing", "Self-registration on startup"),
         ("Closed shops removed", "Heartbeats and health checks"),
         ("Several branches of a chain", "Multiple instances → load balancing")],
    how_side="register, check, look up",
    how="""  <p>There are two flavours:</p>
  <ul>
    <li><b>Client-side discovery:</b> the caller (or its library/sidecar) queries the registry and picks an instance itself.</li>
    <li><b>Server-side discovery:</b> the caller sends to a load balancer or DNS name, which looks up the registry for it.</li>
  </ul>""",
    how_figs=[sd_how],
    steps=[("Register", "On startup an instance registers its name, address, port and metadata (version, zone), or the platform (Kubernetes) does it automatically."),
           ("Stay healthy", "The instance sends heartbeats or the registry runs health checks. Missing ones get removed after a short TTL."),
           ("Look up by name", "Callers ask for “payments” and get the list of healthy instances (via an API, DNS, or the sidecar)."),
           ("Load-balance", "Pick an instance (round robin, least requests, same zone first) and keep the list cached briefly."),
           ("Deregister on shutdown", "On a graceful stop, remove the instance first and drain in-flight requests.")],
    vocab=[("Service registry", "A database of available service instances."),
           ("Self-registration", "The instance registers itself."),
           ("Third-party registration", "The platform registers instances for them."),
           ("Heartbeat / TTL", "Regular “I'm alive” signals; missing ones expire."),
           ("Client-side discovery", "The caller looks up and chooses an instance."),
           ("Server-side discovery", "A load balancer / DNS looks up for the caller.")],
    code=dict(file="orders-service.ts", note="Kubernetes: the name IS the discovery", src="""
// In Kubernetes a Service named "payments" gets a stable DNS name.
// kube-proxy / the mesh spreads calls over the healthy pods behind it.
const res = await fetch("http://payments.shop.svc.cluster.local/charge", {
  method: "POST", body: JSON.stringify(order), signal: AbortSignal.timeout(2000),
});

// Outside Kubernetes, e.g. with Consul's HTTP API (client-side discovery):
const instances = await (await fetch(
  "http://consul:8500/v1/health/service/payments?passing=true")).json();
const pick = instances[Math.floor(Math.random() * instances.length)].Service;
await fetch(`http://${pick.Address}:${pick.Port}/charge`, { method: "POST" });
"""),
    tools="registries: Kubernetes Services + DNS (CoreDNS) + EndpointSlices, HashiCorp Consul, Netflix Eureka, etcd / ZooKeeper, AWS Cloud Map, Spring Cloud LoadBalancer; meshes do client-side discovery in the sidecar.",
    gains=["<b>No hard-coded addresses</b>; instances can move freely.",
           "<b>Autoscaling just works</b>; new instances get traffic right away.",
           "<b>Dead instances are removed</b> automatically.",
           "<b>Same code in every environment</b>; only the registry differs.",
           "<b>Smarter routing</b> by zone, version or health."],
    losses=["<b>The registry is critical</b>; it must be highly available.",
            "<b>Stale data windows</b>: a crashed instance may get traffic until its TTL expires.",
            "<b>More moving parts</b> outside a platform like Kubernetes.",
            "<b>DNS caching surprises</b> (clients ignoring TTLs).",
            "<b>Debugging “why did it call that instance?”</b> gets harder."],
    baseline="Each line compares callers with <b>hard-coded addresses in config</b> to the same system using <b>a service registry with health checks</b>.",
    ratings=[(3, 3, "One more concept; on Kubernetes it's nearly invisible."),
             (4, 4, "Built into most platforms; a registry cluster otherwise."),
             (2, 5, "Instances can be replaced, moved and scaled without config edits."),
             (3, 3, "Neutral; local dev needs a registry or DNS stub."),
             (2, 5, "New instances join the pool automatically."),
             (2, 5, "Autoscaling depends on it."),
             (2, 4, "Unhealthy instances are dropped from rotation."),
             (4, 4, "A cached lookup costs almost nothing."),
             (2, 4, "Services can be split, moved or renamed behind names.")],
    pitfalls=[("Caching lookups forever", "A client resolves DNS once at startup and keeps calling an instance that died an hour ago.", "respect TTLs; re-resolve; use a client that refreshes."),
              ("Health checks that check nothing", "<code>/health</code> always returns 200, even when the DB is unreachable, so broken instances stay in rotation.", "readiness checks that test what the instance needs to serve."),
              ("Health checks that check too much", "Every instance's health depends on a shared DB, so a DB blip marks all of them unhealthy at once.", "liveness = “am I stuck?”; readiness = “can I serve?”; avoid deep cascading checks."),
              ("No graceful deregistration", "Pods are killed mid-request because they were still in the registry.", "deregister first, drain, then stop (preStop hooks)."),
              ("A single registry node", "The registry dies and nothing can find anything.", "a replicated registry cluster and client-side caches.")],
    use=["Instances are dynamic: containers, autoscaling, spot instances.",
         "Many services call each other.",
         "You deploy to several environments or regions.",
         "You want health-aware load balancing."],
    skip=["A few long-lived servers with stable addresses.",
          "A single service behind one load balancer.",
          "Your platform already does it (Kubernetes Services, serverless). Use that, don't add another registry."],
    related=["<b>Sidecar &amp; service mesh</b>", "<b>API gateway</b>", "<b>Leader election</b> · often uses the same store", "<b>Health checks</b>", "<b>Circuit breaker</b>"],
    quiz=[("Client-side vs server-side discovery?", "Client-side: the caller queries the registry and picks an instance. Server-side: the caller hits a load balancer or DNS name that does the lookup."),
          ("How does a registry learn an instance has died?", "Missed heartbeats (TTL expiry) or failed health checks remove it from the list."),
          ("What's the difference between liveness and readiness checks?", "Liveness asks “is the process stuck and in need of a restart?”; readiness asks “can it serve traffic right now?”, which decides whether it stays in rotation."),
          ("What does Kubernetes use for service discovery?", "Service objects with stable DNS names, backed by EndpointSlices that list the ready pods.")],
    remember="Call services by <span class=\"hl\">name</span>, never by address. The registry knows who's alive; your config shouldn't have to.",
    sources=["Chris Richardson, microservices.io, “Client-side / Server-side discovery” and “Service registry”.",
             "Kubernetes docs, “Service” and “DNS for Services and Pods”.",
             "HashiCorp Consul docs, “Service discovery”.",
             "Sam Newman, <i>Building Microservices</i>, 2nd ed., “Service Discovery”."],
)

NOTES = [GATEWAY, PUBSUB, COMPETING, SIDECAR, DISCOVERY]
