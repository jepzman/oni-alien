# Vol. 6 · Running & observing: Health Checks, Autoscaling, Logs/Metrics/Traces, SLOs & Error Budgets.

# ------------------------------------------------------------------ 09 Health Checks & Probes
hc_problem = Doodle(760, 250, "Doodle of a load balancer sending traffic to three instances. One instance has a stuck database connection pool and returns errors to every request, but its process is still running, so the platform thinks it's fine and keeps sending it a third of all traffic.",
                    "One instance is broken but still “running”, so it keeps getting a third of the traffic.")
hc_problem.box(20, 90, 150, 60, "load balancer", "y", size=16)
for i, (t, ok) in enumerate([("web-1 ✓", True), ("web-2 ✗ stuck pool", False), ("web-3 ✓", True)]):
    hc_problem.arrow(176, 120, 330, 40 + i * 70, color="" if ok else "red")
    hc_problem.box(336, 18 + i * 70, 220, 46, t, "green" if ok else "pink", stroke="" if ok else "red", size=16)
hc_problem.note(660, 110, "process up,", "red")
hc_problem.note(660, 136, "33% errors", "red")

hc_analogy = Doodle(760, 250, "Doodle of a hospital nurse doing rounds. For each patient she asks two different questions: are you alive and breathing, and are you well enough to have visitors today? A patient can be alive but not ready for visitors.",
                    "Two questions on the ward round: “alive?” and “ready for visitors?”. Different answers, different actions.")
hc_analogy.icon("dummy", 60, 50, 1.6, fill="y")
hc_analogy.note(250, 70, "“are you alive?”", "pen", anchor="start")
hc_analogy.note(470, 70, "no → call the doctor (restart)", "red", anchor="start")
hc_analogy.note(250, 130, "“ready for visitors?”", "pen", anchor="start")
hc_analogy.note(470, 130, "no → no visitors yet", "pen", anchor="start")
hc_analogy.note(470, 156, "(no traffic)", "pen", anchor="start")
hc_analogy.note(380, 220, "alive ≠ ready", "green")

hc_how = Doodle(760, 290, "Kubernetes probes. A startup probe gives a slow app time to boot. A liveness probe checks that the process isn't stuck, and if it fails several times the container is restarted. A readiness probe checks the instance can serve now, including critical dependencies, and if it fails the instance is removed from the load balancer until it recovers, without restarting.",
                "Startup: give it time to boot. Liveness: restart if stuck. Readiness: stop sending traffic until it can serve.")
for i, (t, sub, act, f) in enumerate([("startup", "booted yet?", "wait", "blue"), ("liveness", "stuck?", "restart", "pink"), ("readiness", "can serve now?", "remove from LB", "green")]):
    hc_how.box(20 + i * 250, 50, 220, 90, t, f, sub=sub, size=20)
    hc_how.note(130 + i * 250, 180, f"fail → {act}", "red" if i == 1 else "pen")
hc_how.note(380, 250, "liveness: cheap, local · readiness: may check critical deps", "pen")

HEALTH = dict(
    slug="health-checks",
    kicker="a.k.a. “the ward round”",
    tldr="Let the platform ask every instance <b>two different questions</b>: <b>“are you alive?”</b> (liveness: if not, restart it) and <b>“can you serve traffic right now?”</b> (readiness: if not, stop sending requests until it recovers). Add a <b>startup</b> check for slow boots. Keep liveness <b>cheap and local</b>, so a slow database doesn't trigger a restart storm.",
    chips=[("Family", "runtime operations"), ("Probes", "startup, liveness, readiness"), ("Used by", "Kubernetes, load balancers, ECS, Cloud Run"), ("Pairs with", "autoscaling, blue–green, circuit breaker (Vol. 1)")],
    problem="""  <p class="lead">“The process is running” isn't the same as “it works”. Without real health checks, a <span class="hl-pink">stuck or half-started</span> instance keeps receiving traffic, and every request it gets fails.</p>
  <ul>
    <li>A deadlocked instance serves errors for hours.</li>
    <li>New instances get traffic before they've warmed up.</li>
    <li>A bad health check restarts every pod when the database is slow.</li>
  </ul>""",
    problem_figs=[hc_problem],
    analogy_side="the ward round",
    analogy="""  <p>On her round, a nurse asks each patient <b>two different questions</b>: “are you <b>alive</b> and breathing?” and “are you <b>ready for visitors</b> today?”. A patient can be alive but not ready for visitors, and that needs a very different response.</p>
  <ul>
    <li>“Alive?” is the <b>liveness</b> probe; “no” means call the doctor (<b>restart</b>).</li>
    <li>“Visitors?” is <b>readiness</b>; “no” means <b>no traffic</b> for now.</li>
  </ul>""",
    analogy_figs=[hc_analogy],
    map=[("“Are you alive?”", "Liveness probe"),
         ("Call the doctor", "Restart the container"),
         ("“Ready for visitors?”", "Readiness probe"),
         ("No visitors for now", "Removed from the load balancer"),
         ("Just admitted, still settling", "Startup probe / grace period")],
    how_side="three probes, three actions",
    how="""  <p>The classic mistake is making liveness check dependencies. If the database is slow, every instance fails liveness and restarts, turning a slowdown into an outage.</p>""",
    how_figs=[hc_how],
    steps=[("Add endpoints", "<code>/livez</code> (process responsive) and <code>/readyz</code> (can serve: warmed up, critical deps reachable)."),
           ("Keep liveness local", "No database or downstream calls; just “is my event loop alive?”."),
           ("Make readiness honest", "Fail while starting, while draining on shutdown, or when a critical dependency is down."),
           ("Tune timings", "Startup probe for slow boots; failure thresholds that avoid flapping."),
           ("Drain on shutdown", "On SIGTERM: fail readiness, finish in-flight requests, then exit."),
           ("Wire them everywhere", "Kubernetes probes, load balancer health checks, deploy gates.")],
    vocab=[("Liveness", "Is the process alive and not stuck?"),
           ("Readiness", "Can this instance serve traffic right now?"),
           ("Startup probe", "Gives slow apps time before liveness starts."),
           ("Graceful shutdown", "Stop taking traffic, finish work, then exit."),
           ("Flapping", "Rapidly switching between healthy and unhealthy."),
           ("Restart storm", "Many instances restarting at once.")],
    code=dict(file="deployment.yaml + health.ts", note="Kubernetes + Express", src="""
startupProbe:   { httpGet: { path: /livez,  port: 8080 }, failureThreshold: 30, periodSeconds: 2 }
livenessProbe:  { httpGet: { path: /livez,  port: 8080 }, periodSeconds: 10, failureThreshold: 3 }
readinessProbe: { httpGet: { path: /readyz, port: 8080 }, periodSeconds: 5,  failureThreshold: 2 }

// health.ts
let draining = false;
app.get("/livez", (_req, res) => res.sendStatus(200));          // local only
app.get("/readyz", async (_req, res) => {
  if (draining || !cache.warm) return res.sendStatus(503);
  const dbOk = await db.ping({ timeoutMs: 300 }).catch(() => false);
  res.sendStatus(dbOk ? 200 : 503);                              // stop traffic, don't restart
});
process.on("SIGTERM", () => { draining = true; setTimeout(() => server.close(), 10_000); });
"""),
    tools="tools: Kubernetes probes, AWS ALB/NLB target health checks, ECS health checks, Cloud Run startup/liveness probes, gRPC health checking protocol, Spring Boot Actuator, terminus / lightship for Node.",
    gains=["<b>Broken instances stop getting traffic</b>.",
           "<b>Stuck processes heal</b> by restart.",
           "<b>Safe rollouts</b>: new pods only get traffic when ready.",
           "<b>Graceful shutdowns</b> without dropped requests."],
    losses=["<b>Badly designed checks</b> can cause outages.",
            "<b>Tuning</b> timings takes care.",
            "<b>Readiness can hide</b> a problem if nobody alerts on it."],
    baseline="Each line compares <b>“process is running” as the only health signal</b> to <b>separate startup, liveness and readiness probes with graceful shutdown</b>.",
    ratings=[(4, 3, "Three probes to understand and tune."),
             (3, 4, "Rollouts can rely on readiness gates."),
             (2, 4, "New versions only get traffic when ready."),
             (2, 4, "Bad instances drop out automatically."),
             (3, 4, "Autoscaling can trust instance health."),
             (2, 4, "Stuck processes restart themselves."),
             (2, 3, "Probe status is a useful signal."),
             (4, 4, "Almost free."),
             (3, 4, "Standard endpoints in every service.")],
    pitfalls=[("Dependencies in liveness", "DB slows down; every pod restarts; full outage.", "liveness local only; deps in readiness."),
              ("No startup probe", "Slow-booting apps get killed in a restart loop.", "startup probe or initial delay."),
              ("Health endpoint does heavy work", "Probes cause load themselves.", "make checks cheap; cache dependency status briefly."),
              ("Ignoring SIGTERM", "In-flight requests fail on every deploy.", "fail readiness, drain, then exit.")],
    use=["Every service behind a load balancer or orchestrator.",
         "Rolling, blue–green and canary deployments.",
         "Workers that can get stuck."],
    skip=["Short-lived batch jobs (use timeouts and exit codes)."],
    related=["<b>Autoscaling</b>", "<b>Blue–green deployment</b>", "<b>Circuit breaker</b> (Vol. 1)", "<b>Logs, metrics &amp; traces</b>"],
    quiz=[("What's the difference between liveness and readiness?", "Liveness asks if the process is stuck (restart it); readiness asks if it can serve now (stop sending traffic)."),
          ("Why shouldn't liveness check the database?", "A slow database would make all instances fail liveness and restart at once."),
          ("What does a startup probe protect against?", "Slow-booting apps being killed by liveness before they finish starting."),
          ("What should an app do on SIGTERM?", "Fail readiness, finish in-flight requests, then exit.")],
    remember="Ask <span class=\"hl\">“alive?”</span> and <span class=\"hl\">“ready?”</span> separately. Alive isn't ready.",
    sources=["Kubernetes docs, “Configure Liveness, Readiness and Startup Probes”.",
             "Google Cloud blog, “Kubernetes best practices: Setting up health checks with readiness and liveness probes”.",
             "AWS Builders' Library, “Implementing health checks”.",
             "gRPC, “Health Checking Protocol”."],
)

# ------------------------------------------------------------------ 10 Autoscaling
as_problem = Doodle(760, 250, "Doodle of a fixed fleet of four servers. During a lunchtime traffic spike they max out and requests time out. At night the same four servers sit at five percent CPU, costing money for nothing.",
                    "Four servers, always: overwhelmed at lunch, idle at night.")
as_problem.raw('<path class="d d-pen" d="M20 200 C 120 200 160 60 260 50 C 360 40 380 200 480 200 C 560 200 600 190 740 190"/>')
as_problem.line("M20 120 h720", color="red", dash=True)
as_problem.note(620, 110, "capacity: 4 servers", "red")
as_problem.note(260, 34, "lunch spike: timeouts", "red")
as_problem.note(620, 230, "night: 5% CPU, still paying", "red")

as_analogy = Doodle(760, 250, "Doodle of a supermarket opening more checkout lanes when queues get long and closing them when it's quiet. A manager watches the queue length, not how tired the cashiers look, and new lanes take a minute to open.",
                    "Open lanes when queues grow, close them when it's quiet. Watch the queue, not the cashiers.")
as_analogy.icon("lanes", 40, 60, 2.0)
as_analogy.note(130, 200, "queue long → open a lane", "green")
as_analogy.icon("lanes", 360, 100, 1.0)
as_analogy.note(410, 200, "quiet → close lanes", "pen")
as_analogy.note(620, 100, "new lane: ~1 min", "pen")
as_analogy.note(620, 126, "to open", "pen")

as_how = Doodle(760, 290, "Horizontal autoscaling loop. A metric such as requests per second per instance or queue depth is compared to a target. The autoscaler adds instances when above the target and removes them when below, within a minimum of three and a maximum of thirty. Scale-up is fast, scale-down is slow with a cooldown, so it doesn't flap.",
                "Measure a load signal, compare with a target, add or remove instances within min/max. Up fast, down slow.")
as_how.box(20, 50, 180, 80, "metric", "y", sub="RPS/pod or queue")
as_how.arrow(206, 90, 286, 90)
as_how.box(292, 40, 200, 100, "autoscaler", "blue", sub="target: 50 RPS / pod")
as_how.arrow(498, 70, 580, 50, color="green", label="+ pods, fast", lx=590, ly=40, anchor="start")
as_how.arrow(498, 110, 580, 130, label="− pods, slowly", lx=590, ly=150, anchor="start")
as_how.box(160, 190, 440, 54, "min 3 · max 30 · keep headroom", "green", size=17)

AUTOSCALE = dict(
    slug="autoscaling",
    kicker="a.k.a. “open more checkout lanes”",
    tldr="Let the platform <b>add instances when load rises</b> and <b>remove them when it falls</b>, based on a signal that tracks real demand (requests per instance, queue depth, CPU), within <b>min and max limits</b>. Scale <b>up fast and down slowly</b>. You get capacity for spikes without paying for idle servers at night, as long as instances are <b>stateless</b> and <b>start quickly</b>.",
    chips=[("Family", "capacity"), ("Kinds", "horizontal, vertical, scheduled, event-driven, scale-to-zero"), ("Tools", "Kubernetes HPA, KEDA, cloud autoscaling groups, Cloud Run"), ("Pairs with", "health checks, immutable infrastructure, competing consumers (Vol. 1)")],
    problem="""  <p class="lead">Fixed capacity is <span class="hl-pink">always wrong</span>: too little at peak (timeouts, lost sales), too much off-peak (wasted money). Manual scaling is slow and happens after the outage starts.</p>
  <ul>
    <li>The lunchtime spike overloads the fleet.</li>
    <li>At night 95% of the capacity sits idle.</li>
    <li>Someone has to remember to scale up before the big launch.</li>
  </ul>""",
    problem_figs=[as_problem],
    analogy_side="supermarket checkout lanes",
    analogy="""  <p>A good supermarket <b>opens more lanes</b> when queues grow and <b>closes them</b> when it's quiet. The manager watches the <b>queue length</b>, not how tired the cashiers look, and knows a new lane takes a minute to open, so they open one <b>a little early</b>.</p>
  <ul>
    <li>Lanes are <b>instances</b>.</li>
    <li>Queue length is the <b>scaling metric</b>.</li>
    <li>Opening early is <b>headroom</b>.</li>
  </ul>""",
    analogy_figs=[as_analogy],
    map=[("Checkout lanes", "Instances / pods"),
         ("Watching queue length", "Scaling on requests per pod or queue depth"),
         ("Open a lane when it's busy", "Scale out above the target"),
         ("Close lanes slowly when quiet", "Scale in with a cooldown"),
         ("Store has only 30 tills", "Max replicas (and a minimum for safety)")],
    how_side="target tracking within limits",
    how="""  <p>Pick a metric that <b>leads</b> load (requests, queue depth) rather than one that lags (memory). And make sure new instances are <b>ready fast</b>: autoscaling can't help if boot takes ten minutes.</p>""",
    how_figs=[as_how],
    steps=[("Make instances stateless", "Sessions and data outside the instance; any instance can serve any request."),
           ("Pick the right signal", "Web: requests/instance or CPU; workers: queue depth or lag."),
           ("Set min, max and target", "Min for redundancy (≥ 2–3), max for cost and downstream safety."),
           ("Up fast, down slow", "Short scale-up window; longer scale-down stabilisation."),
           ("Make boot fast", "Small images, readiness probes, pre-warmed caches."),
           ("Schedule known peaks", "Scale ahead of launches and daily patterns.")],
    vocab=[("Horizontal scaling", "More or fewer instances."),
           ("Vertical scaling", "Bigger or smaller instances."),
           ("Target tracking", "Adjust capacity to keep a metric near a target."),
           ("Cooldown / stabilisation", "Waiting before scaling again, to avoid flapping."),
           ("Scale to zero", "No instances when idle; start on demand."),
           ("Headroom", "Spare capacity kept for sudden spikes.")],
    code=dict(file="hpa.yaml + keda.yaml", note="Kubernetes HPA and KEDA", src="""
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata: { name: web }
spec:
  scaleTargetRef: { apiVersion: apps/v1, kind: Deployment, name: web }
  minReplicas: 3
  maxReplicas: 30
  metrics:
    - type: Resource
      resource: { name: cpu, target: { type: Utilization, averageUtilization: 60 } }
  behavior:
    scaleUp:   { stabilizationWindowSeconds: 0 }
    scaleDown: { stabilizationWindowSeconds: 300 }    # down slowly
---
# workers: scale on queue length with KEDA
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata: { name: invoice-worker }
spec:
  scaleTargetRef: { name: invoice-worker }
  minReplicaCount: 0
  maxReplicaCount: 50
  triggers: [{ type: aws-sqs-queue, metadata: { queueURL: "…", queueLength: "20" } }]
"""),
    tools="tools: Kubernetes HPA / VPA, KEDA, Karpenter and Cluster Autoscaler (nodes), AWS Auto Scaling groups and ECS service autoscaling, GCP managed instance groups, Cloud Run / Lambda (automatic, scale to zero).",
    gains=["<b>Capacity for spikes</b>.",
           "<b>Lower cost</b> off-peak.",
           "<b>No manual scaling</b> under pressure.",
           "<b>Scale to zero</b> for idle workloads."],
    losses=["<b>Cold starts and lag</b> during sudden spikes.",
            "<b>Downstream overload</b>: more instances, more DB connections.",
            "<b>Tuning</b> metrics and windows.",
            "<b>Runaway cost</b> without a max."],
    baseline="Each line compares a <b>fixed-size fleet scaled by hand</b> to <b>autoscaling on a demand signal with min/max limits</b>.",
    ratings=[(4, 3, "Targets, limits and windows to tune."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Spikes get capacity automatically."),
             (2, 5, "Grows to demand within limits."),
             (3, 4, "Replaces failed capacity automatically."),
             (3, 3, "Scaling events are visible signals."),
             (2, 4, "Pay for what you use; watch the max."),
             (3, 4, "No midnight manual scaling.")],
    pitfalls=[("Scaling on a lagging metric", "Memory rises after the overload; scaling comes too late.", "scale on requests or queue depth."),
              ("No max", "A bug or attack scales you to 500 instances.", "set max and budget alerts."),
              ("Forgetting downstream limits", "30 pods × 20 connections overwhelm the database.", "connection pooling and limits (Vol. 3)."),
              ("Slow boot", "New pods take 5 minutes; the spike is over.", "smaller images, startup tuning, headroom.")],
    use=["Variable or spiky traffic.",
         "Queue-based workers.",
         "Stateless services."],
    skip=["Steady, predictable load (right-size and reserve instead).",
          "Stateful systems that can't add nodes quickly."],
    related=["<b>Health checks &amp; probes</b>", "<b>Immutable infrastructure</b>", "<b>Cost visibility (FinOps)</b>", "<b>Connection pooling</b> (Vol. 3)"],
    quiz=[("Why scale up fast and down slowly?", "To catch spikes quickly while avoiding flapping when load dips briefly."),
          ("What makes a good scaling metric?", "One that tracks demand early, like requests per instance or queue depth."),
          ("Why set a maximum?", "To cap cost and protect downstream systems from too many instances."),
          ("What must be true of instances?", "They must be stateless and start quickly.")],
    remember="Watch the <span class=\"hl\">queue</span>, open <span class=\"hl\">lanes</span> early, close them <span class=\"hl\">slowly</span>.",
    sources=["Kubernetes docs, “Horizontal Pod Autoscaling”.",
             "KEDA documentation.",
             "AWS docs, “Target tracking scaling policies”.",
             "Google SRE Book, ch. 21 “Handling Overload”."],
)

# ------------------------------------------------------------------ 11 Logs, Metrics & Traces
ob_problem = Doodle(760, 250, "Doodle of an engineer at 3 a.m. with a ticket that says checkout is slow for some users. There are gigabytes of unstructured log lines across twelve services, a CPU graph that looks normal, and no way to follow one request from the browser through the services to the database.",
                    "“Checkout is slow for some users.” Twelve services, gigabytes of text logs, no way to follow one request.")
ob_problem.icon("magnifier", 40, 60, 1.6)
ob_problem.box(220, 30, 300, 130, None, "paper", rx=3)
for i, t in enumerate(["INFO done", "ERROR something failed", "INFO ok", "WARN retry"]):
    ob_problem.text(234, 60 + i * 26, t, "t", anchor="start", size=15)
ob_problem.note(640, 60, "which request?", "red")
ob_problem.note(640, 100, "which service?", "red")
ob_problem.note(640, 140, "which users?", "red")
ob_problem.note(370, 210, "12 services, 0 connected clues", "red")

ob_analogy = Doodle(760, 250, "Doodle of a parcel delivery tracking page. The parcel has one tracking number. Every depot it passes scans it with a timestamp, so you can see the whole journey and exactly where it got stuck. Separately, the company's dashboard counts parcels per hour, and each depot keeps a detailed diary.",
                    "A parcel tracking number: every depot scans it, so you can see where it got stuck.")
ob_analogy.icon("parcel", 30, 80, 1.2, fill="y")
ob_analogy.note(70, 180, "#TRK-42", "pen")
for i, (t, ms) in enumerate([("depot A", "09:00"), ("hub", "09:40"), ("depot B", "17:55 ← stuck"), ("door", "18:10")]):
    ob_analogy.box(160 + i * 145, 70, 130, 60, t, "pink" if i == 2 else "green", sub=ms, size=16, subsize=14)
    if i:
        ob_analogy.arrow(160 + i * 145 - 14, 100, 160 + i * 145 - 2, 100)
ob_analogy.note(450, 210, "one id, every scan, the whole journey", "green")

ob_how = Doodle(760, 300, "The three signals. Metrics are cheap numbers over time, like request rate, errors and duration per service, used for dashboards and alerts. Traces follow a single request across services as spans with timings, sharing one trace id. Logs are structured JSON events with details, also carrying the trace id. OpenTelemetry collects all three and sends them to a backend, where you jump from an alert to a trace to the logs.",
                "Metrics say something's wrong, traces say where, logs say why. One trace id links them.")
ob_how.box(20, 40, 220, 90, "metrics", "y", sub="rate · errors · duration")
ob_how.box(270, 40, 220, 90, "traces", "green", sub="spans across services")
ob_how.box(520, 40, 220, 90, "logs", "blue", sub="structured JSON + trace_id")
ob_how.arrow(240, 85, 266, 85)
ob_how.arrow(490, 85, 516, 85)
ob_how.note(130, 160, "something's wrong", "pen")
ob_how.note(380, 160, "where", "pen")
ob_how.note(630, 160, "why", "pen")
ob_how.box(160, 200, 440, 54, "OpenTelemetry → one backend", "paper", stroke="green", size=17)

OBSERVE = dict(
    slug="observability",
    kicker="a.k.a. “the parcel tracking number”",
    tldr="Emit three kinds of signals from every service: <b>metrics</b> (cheap numbers over time: rate, errors, duration) to <b>notice</b> problems, <b>traces</b> (one request's journey across services) to find <b>where</b>, and <b>structured logs</b> (events with context) to see <b>why</b>. Link them with a shared <b>trace id</b>, collect them with <b>OpenTelemetry</b>, and you can answer questions you didn't plan for.",
    chips=[("Family", "operations"), ("Standard", "OpenTelemetry (CNCF)"), ("Starter metrics", "RED: rate, errors, duration · USE for resources"), ("Pairs with", "SLOs, audit logging (Vol. 5), canary releases")],
    problem="""  <p class="lead">With many services, “it's slow for some users” is a <span class="hl-pink">needle in a haystack</span>: text logs on many machines, dashboards that show averages, and no way to follow one request end to end.</p>
  <ul>
    <li>Averages hide the 1% of users with 10-second checkouts.</li>
    <li>Log lines can't be joined across services.</li>
    <li>Every incident starts with “add more logging and redeploy”.</li>
  </ul>""",
    problem_figs=[ob_problem],
    analogy_side="the parcel tracking number",
    analogy="""  <p>A parcel has <b>one tracking number</b>. Every depot <b>scans it</b> with a timestamp, so you can see its whole journey and exactly <b>where it got stuck</b>. The company also <b>counts parcels per hour</b> on a dashboard, and each depot keeps a <b>detailed diary</b>.</p>
  <ul>
    <li>The tracking number is the <b>trace id</b>; each scan is a <b>span</b>.</li>
    <li>Parcels per hour is a <b>metric</b>.</li>
    <li>The depot diary is <b>logs</b>, mentioning the tracking number.</li>
  </ul>""",
    analogy_figs=[ob_analogy],
    map=[("Tracking number", "Trace id (W3C traceparent)"),
         ("A scan at each depot", "A span with start time and duration"),
         ("Parcels per hour dashboard", "Metrics: rate, errors, duration"),
         ("Depot diary entries", "Structured logs with the trace id"),
         ("“Stuck at depot B”", "The slow span in a trace")],
    how_side="three signals, one id",
    how="""  <p>Observability isn't more dashboards. It's being able to ask a <b>new question</b> (“which tenant on which version is slow?”) <b>without shipping new code</b>.</p>""",
    how_figs=[ob_how],
    steps=[("Instrument with OpenTelemetry", "Auto-instrumentation for HTTP, databases and queues; vendor-neutral."),
           ("Propagate context", "Pass the trace context (traceparent) across HTTP and message headers."),
           ("RED metrics per service", "Request rate, error rate, duration histograms (p50/p95/p99), by route."),
           ("Structured logs", "JSON with trace_id, user/tenant id, version; no secrets."),
           ("Add business attributes", "tenant, plan, feature flag state on spans: that's what answers “for some users”."),
           ("Sample wisely", "Keep all errors and slow traces; sample the boring ones.")],
    vocab=[("Metric", "A number measured over time."),
           ("Trace", "The full journey of one request across services."),
           ("Span", "One step in a trace, with timing."),
           ("Structured log", "A log event as key–value data (JSON)."),
           ("Cardinality", "How many distinct values a label has."),
           ("Percentile (p95)", "95% of requests are faster than this.")],
    code=dict(file="checkout.ts", note="OpenTelemetry JS", src="""
import { trace, metrics } from "@opentelemetry/api";
const tracer = trace.getTracer("checkout");
const duration = metrics.getMeter("checkout").createHistogram("checkout.duration", { unit: "ms" });

export async function checkout(req: Req) {
  return tracer.startActiveSpan("checkout", async (span) => {
    span.setAttributes({ "tenant.id": req.tenantId, "cart.items": req.items.length,
                         "flag.new_checkout": req.flags.newCheckout });
    const t0 = performance.now();
    try {
      const order = await placeOrder(req);              // child spans: db, payments
      logger.info({ msg: "order placed", orderId: order.id, traceId: span.spanContext().traceId });
      return order;
    } catch (e) {
      span.recordException(e as Error); span.setStatus({ code: 2 });
      throw e;
    } finally {
      duration.record(performance.now() - t0, { route: "/checkout" });
      span.end();
    }
  });
}
"""),
    tools="tools: OpenTelemetry SDKs and Collector, Prometheus + Grafana, Grafana Tempo/Loki, Jaeger, Honeycomb, Datadog, New Relic, Elastic, cloud-native (CloudWatch, Cloud Trace, Azure Monitor).",
    gains=["<b>Find where and why</b> quickly.",
           "<b>Answer new questions</b> without redeploying.",
           "<b>See tail latency</b>, not just averages.",
           "<b>Vendor-neutral</b> instrumentation with OpenTelemetry."],
    losses=["<b>Data volume and cost</b>.",
            "<b>High-cardinality traps</b> in metrics.",
            "<b>Instrumentation effort</b> and consistency.",
            "<b>Privacy risk</b> if personal data leaks into telemetry."],
    baseline="Each line compares <b>unstructured text logs and host CPU graphs</b> to <b>OpenTelemetry metrics, traces and structured logs linked by trace id</b>.",
    ratings=[(3, 3, "More concepts, but one standard."),
             (3, 4, "Confident, faster releases."),
             (3, 4, "Canary analysis and alerts get real signals."),
             (3, 4, "Problems are found and fixed sooner."),
             (3, 3, "Neutral."),
             (2, 4, "Faster diagnosis means faster recovery."),
             (1, 5, "From an alert to the slow span to the log line."),
             (4, 2, "Telemetry storage isn't cheap; sample and tier."),
             (2, 4, "Debug production without guesswork.")],
    pitfalls=[("Averages only", "Mean latency 120 ms; p99 is 9 s.", "histograms and percentiles."),
              ("User ids as metric labels", "Millions of time series; the bill explodes.", "high-cardinality data on spans and logs, not metric labels."),
              ("Broken context propagation", "Traces stop at the queue.", "propagate traceparent through messages too."),
              ("Logging personal data", "Emails and tokens in logs.", "redact; log ids, not secrets.")],
    use=["Any production service, especially distributed ones.",
         "Canary analysis and SLO alerting.",
         "Debugging “only some users” problems."],
    skip=["Don't skip; for a tiny app, start with RED metrics and structured logs."],
    related=["<b>SLOs &amp; error budgets</b>", "<b>Canary releases</b>", "<b>Audit logging</b> (Vol. 5)", "<b>Sidecar &amp; service mesh</b> (Vol. 1)"],
    quiz=[("What does each signal answer?", "Metrics: is something wrong? Traces: where? Logs: why?"),
          ("What links the three?", "A shared trace id, propagated across services."),
          ("Why use percentiles instead of averages?", "Averages hide slow outliers that real users experience."),
          ("Where should high-cardinality data (user id) go?", "On spans and logs, not on metric labels.")],
    remember="Give every request a <span class=\"hl\">tracking number</span>, and <span class=\"hl\">scan</span> it at every depot.",
    sources=["OpenTelemetry documentation (opentelemetry.io).",
             "Charity Majors, Liz Fong-Jones &amp; George Miranda, <i>Observability Engineering</i> (O'Reilly).",
             "Tom Wilkie, “The RED Method”; Brendan Gregg, “The USE Method”.",
             "W3C Trace Context recommendation."],
)

# ------------------------------------------------------------------ 12 SLOs & Error Budgets
sl_problem = Doodle(760, 250, "Doodle of a tug of war between a product team pulling for more features and faster releases, and an operations team pulling for more stability and fewer changes. Without a shared measure of how reliable is reliable enough, every release becomes an argument.",
                    "Features vs stability: without a shared number, every release is a tug of war.")
sl_problem.line("M170 130 h400")
sl_problem.box(20, 100, 150, 60, "“ship more!”", "y", size=17)
sl_problem.box(570, 100, 180, 60, "“change less!”", "blue", size=17)
sl_problem.note(380, 110, "?", "red", size=40)
sl_problem.note(380, 210, "“how reliable is reliable enough?” nobody knows", "red")

sl_analogy = Doodle(760, 250, "Doodle of a monthly data allowance on a phone plan. You get ten gigabytes. You can stream as much as you like until you've used it up; when you're close to the limit, you slow down. The allowance is agreed in advance, so nobody argues about each video.",
                    "A monthly data allowance: use it freely; near the limit, slow down. No arguing over each video.")
sl_analogy.icon("phone", 60, 50, 1.6, fill="y")
sl_analogy.box(260, 60, 400, 40, None, "paper", rx=6)
sl_analogy.raw('<rect class="d f-green" x="260" y="60" width="280" height="40" rx="6"/>')
sl_analogy.note(460, 130, "7 of 10 GB used", "pen")
sl_analogy.note(460, 170, "plenty left → stream away", "green")
sl_analogy.note(460, 210, "almost gone → slow down", "red")

sl_how = Doodle(760, 300, "SLO and error budget. The service level indicator is the share of checkout requests that succeed in under 400 milliseconds. The objective is 99.9 percent over 28 days, which leaves an error budget of 0.1 percent, about 40 minutes. Burn-rate alerts page someone when the budget is burning fast. When budget remains, teams ship freely; when it's spent, they focus on reliability.",
                "SLI → SLO → error budget. Alert on burn rate. Budget left: ship. Budget gone: fix reliability first.")
sl_how.box(20, 30, 220, 80, "SLI", "y", sub="% good checkouts (<400 ms)")
sl_how.arrow(246, 70, 286, 70)
sl_how.box(292, 30, 200, 80, "SLO 99.9%", "green", sub="over 28 days")
sl_how.arrow(498, 70, 538, 70)
sl_how.box(544, 30, 200, 80, "budget 0.1%", "pink", sub="≈ 40 min / 28 days")
sl_how.box(20, 160, 340, 60, "budget left → ship features", "green", size=17)
sl_how.box(400, 160, 340, 60, "budget spent → reliability work", "pink", stroke="red", size=16)
sl_how.note(380, 270, "page on fast burn (e.g. 2% of budget in 1 hour)", "pen")

SLO = dict(
    slug="slo-error-budgets",
    kicker="a.k.a. “the monthly data allowance”",
    tldr="Agree, in numbers, <b>how reliable is reliable enough</b>. Pick an <b>SLI</b> that reflects what users feel (share of fast, successful checkouts), set an <b>SLO</b> (99.9% over 28 days), and treat the remainder as an <b>error budget</b> to spend on change. <b>Alert on burn rate</b>, not on every blip. Budget left: ship. Budget spent: <b>prioritise reliability</b>.",
    chips=[("Family", "reliability engineering"), ("Origin", "Google SRE (2016)"), ("Terms", "SLI, SLO, SLA, error budget, burn rate"), ("Pairs with", "observability, canary releases, postmortems")],
    problem="""  <p class="lead">Product wants speed; operations wants stability. Without a shared definition of <span class="hl-pink">“reliable enough”</span>, every release is a negotiation, and teams either freeze or break things.</p>
  <ul>
    <li>Aiming for 100% makes every change look dangerous.</li>
    <li>Alerts fire on every CPU spike; real user pain goes unnoticed.</li>
    <li>Reliability work never gets prioritised until there's an outage.</li>
  </ul>""",
    problem_figs=[sl_problem],
    analogy_side="the monthly data allowance",
    analogy="""  <p>A phone plan gives you <b>10 GB a month</b>. You stream freely while there's plenty left, and <b>slow down</b> when you're near the limit. The allowance was <b>agreed up front</b>, so nobody argues about each video.</p>
  <ul>
    <li>The allowance is the <b>error budget</b>.</li>
    <li>Data used is <b>bad events</b> (failed or slow requests).</li>
    <li>Your usage alert is a <b>burn-rate alert</b>.</li>
  </ul>""",
    analogy_figs=[sl_analogy],
    map=[("What you measure: data used", "SLI: good events ÷ valid events"),
         ("The plan: 10 GB/month", "SLO: 99.9% over 28 days"),
         ("What's left to use", "Error budget: 0.1% bad events"),
         ("“80% used, 10 days left”", "Burn-rate alert"),
         ("Slowing down near the limit", "Pausing risky releases, fixing reliability")],
    how_side="measure what users feel, then budget",
    how="""  <p>100% is the wrong target: users can't tell 99.99% from 100% through their own Wi-Fi, and chasing it stops all change. The budget makes the trade-off explicit.</p>""",
    how_figs=[sl_how],
    steps=[("Pick user journeys", "Sign-in, search, checkout: what users actually care about."),
           ("Define SLIs", "Good events ÷ valid events, measured as close to the user as possible."),
           ("Set SLOs", "Realistic, based on history and user needs; a 28-day rolling window."),
           ("Agree the policy", "What happens when the budget is spent (freeze risky launches, fix top causes)."),
           ("Alert on burn rate", "Multi-window alerts: page on fast burn, ticket on slow burn."),
           ("Review regularly", "Adjust SLOs as users and systems change.")],
    vocab=[("SLI", "Service level indicator: a measure of good service."),
           ("SLO", "Service level objective: the target for an SLI."),
           ("SLA", "A contract with consequences, usually looser than the SLO."),
           ("Error budget", "Allowed unreliability: 100% − SLO."),
           ("Burn rate", "How fast the budget is being used."),
           ("Toil", "Repetitive manual operational work.")],
    code=dict(file="slo.yaml", note="OpenSLO-style + Prometheus burn alert", src="""
apiVersion: openslo/v1
kind: SLO
metadata: { name: checkout-availability }
spec:
  service: checkout
  indicator:
    ratioMetric:
      good:  { metricSource: { spec: { query: 'sum(rate(http_requests_total{route="/checkout",code!~"5..",le_400ms="true"}[5m]))' } } }
      total: { metricSource: { spec: { query: 'sum(rate(http_requests_total{route="/checkout"}[5m]))' } } }
  timeWindow: [{ duration: 28d, isRolling: true }]
  objectives: [{ target: 0.999 }]

# page: burning 14.4× budget over 1h AND 5m (≈2% of the 28-day budget in an hour)
# ticket: burning 1× over 3 days
"""),
    tools="tools: Prometheus + Sloth / Pyrra, Grafana SLO, Datadog / New Relic / Honeycomb SLOs, Google Cloud Service Monitoring, Nobl9, OpenSLO specification.",
    gains=["<b>A shared, numeric definition</b> of reliable enough.",
           "<b>Fewer, better alerts</b> tied to user pain.",
           "<b>Explicit trade-off</b> between speed and stability.",
           "<b>Reliability work gets prioritised</b> by data."],
    losses=["<b>Hard to choose good SLIs</b> at first.",
            "<b>Needs organisational buy-in</b> for the budget policy.",
            "<b>Measurement work</b> to get accurate SLIs.",
            "<b>Can be gamed</b> if SLIs don't reflect users."],
    baseline="Each line compares <b>implicit “keep it up” goals and CPU alerts</b> to <b>user-centred SLOs with error budgets and burn-rate alerts</b>.",
    ratings=[(3, 3, "New terms; one clear number per journey."),
             (2, 4, "Ship freely while the budget lasts."),
             (3, 4, "Risky changes pause when the budget is low."),
             (3, 4, "Reliability work happens before outages."),
             (3, 3, "Neutral."),
             (3, 4, "Burn alerts catch real incidents early."),
             (2, 5, "User-centred signals, not just CPU."),
             (3, 3, "Some tooling; fewer wasted pages."),
             (2, 4, "Fewer arguments; fewer noisy alerts.")],
    pitfalls=[("100% targets", "Every change becomes too risky.", "realistic SLOs below 100%."),
              ("SLIs users don't feel", "CPU usage as an SLI.", "measure success and latency of user journeys."),
              ("No budget policy", "Budget is spent and nothing changes.", "agree consequences up front."),
              ("Too many SLOs", "Forty SLOs nobody reads.", "a few per critical journey.")],
    use=["Services with real users and frequent changes.",
         "Teams arguing about speed vs stability.",
         "Replacing noisy alerting."],
    skip=["Internal prototypes with no users yet.",
          "Batch jobs (use freshness and completion SLOs instead of availability)."],
    related=["<b>Logs, metrics &amp; traces</b>", "<b>Canary releases</b>", "<b>Incident response &amp; postmortems</b>", "<b>Circuit breaker</b> (Vol. 1)"],
    quiz=[("What's the difference between an SLO and an SLA?", "An SLO is an internal target; an SLA is a contract with consequences, usually set looser than the SLO."),
          ("How do you calculate the error budget?", "100% minus the SLO, e.g. 0.1% of requests for a 99.9% SLO."),
          ("Why alert on burn rate?", "It pages when user-facing reliability is actually at risk, not on every blip."),
          ("Why not aim for 100%?", "It's unreachable and stops all change; users can't tell the difference beyond a point.")],
    remember="Agree the <span class=\"hl\">allowance</span>, watch the <span class=\"hl\">burn</span>, and slow down near the <span class=\"hl\">limit</span>.",
    sources=["Beyer et al., <i>Site Reliability Engineering</i> (Google, 2016), ch. 3–4.",
             "<i>The Site Reliability Workbook</i>, ch. 2 “Implementing SLOs” and ch. 5 “Alerting on SLOs”.",
             "Alex Hidalgo, <i>Implementing Service Level Objectives</i> (O'Reilly).",
             "OpenSLO specification (openslo.com)."],
)

NOTES = [HEALTH, AUTOSCALE, OBSERVE, SLO]
