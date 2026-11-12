# Vol. 6 · Shipping safely: Blue–Green, Canary, Feature Flags, Build Once Deploy Many.

# ------------------------------------------------------------------ 01 Blue–Green Deployment
bg_problem = Doodle(760, 250, "Doodle of an in-place deployment on a Friday evening. The servers are stopped, updated one by one and restarted. For ten minutes users see errors and a maintenance page. The new version has a bug, and rolling back means doing the whole slow process again in reverse.",
                    "Update in place: downtime during the deploy, and a slow, scary rollback.")
for i in range(3):
    bg_problem.icon("server", 30 + i * 90, 60, 1.2)
bg_problem.note(160, 160, "stop → update → start", "pen")
bg_problem.box(360, 40, 220, 70, "503 · maintenance", "pink", stroke="red", size=18)
bg_problem.note(470, 140, "10 minutes of errors", "red")
bg_problem.note(470, 190, "bug found → redo it all in reverse", "red")
bg_problem.icon("clock", 640, 60, 1.0, color="red")

bg_analogy = Doodle(760, 250, "Doodle of a theatre with two identical stages on a turntable. While the audience watches the show on the front stage, the crew builds the next scene on the back stage. When it's ready, the turntable rotates and the new scene appears instantly. If something's wrong, they rotate back.",
                    "A theatre turntable: build the next scene out of sight, then rotate. Rotate back if needed.")
bg_analogy.raw('<circle class="d f-y" cx="230" cy="130" r="100"/><path class="d" d="M130 130 h200"/>')
bg_analogy.note(230, 90, "front stage: live show", "green")
bg_analogy.note(230, 180, "back stage: next scene", "pen")
bg_analogy.arrow(350, 60, 350, 200, curve=(420, 130), label="rotate", lx=392, ly=134, anchor="start")
bg_analogy.note(600, 90, "instant switch", "green")
bg_analogy.note(600, 130, "rotate back = rollback", "green")

bg_how = Doodle(760, 300, "Blue-green deployment. Two identical environments sit behind a router or load balancer. Blue runs version one and takes all traffic. Green gets version two deployed and smoke-tested with no user traffic. The router switches all traffic to green in one step. Blue stays running, so rollback is switching back. Database changes must work with both versions.",
                "Two identical environments; deploy to the idle one, test it, then flip the router. Flip back to roll back.")
bg_how.box(300, 20, 160, 60, "router", "y")
bg_how.box(60, 140, 220, 90, "blue · v1", "blue", sub="idle after switch, kept warm")
bg_how.box(480, 140, 220, 90, "green · v2", "green", sub="smoke-tested, then live")
bg_how.arrow(340, 84, 200, 136, dash=True, label="before", lx=230, ly=104)
bg_how.arrow(420, 84, 580, 136, color="green", label="after: 100%", lx=560, ly=104)
bg_how.note(380, 270, "shared database: schema must suit v1 AND v2 (expand & contract)", "pen")

BLUEGREEN = dict(
    slug="blue-green",
    kicker="a.k.a. “the theatre turntable”",
    tldr="Keep <b>two identical environments</b>. One (blue) serves users; deploy the new version to the other (green), <b>test it with no user traffic</b>, then <b>switch the router</b> in one step. Rollback is <b>switching back</b>, in seconds. The catch: both versions share data, so <b>database changes must be backward compatible</b>.",
    chips=[("Family", "deployment strategy"), ("Popularised by", "Dan North &amp; Jez Humble; Martin Fowler (2010)"), ("Switch with", "load balancer, DNS, service mesh, ingress"), ("Pairs with", "build once, expand &amp; contract (Vol. 3)")],
    problem="""  <p class="lead">Updating servers <span class="hl-pink">in place</span> means a window where some are down or half-updated, and if the new version is broken, rolling back is the <span class="hl-pink">same slow process in reverse</span>.</p>
  <ul>
    <li>Users see errors or a maintenance page during each deploy.</li>
    <li>Deploys are scheduled for nights and weekends, so they're rare and big.</li>
    <li>Rollback takes as long as the deploy, while things are on fire.</li>
  </ul>""",
    problem_figs=[bg_problem],
    analogy_side="the theatre turntable",
    analogy="""  <p>Some theatres have a <b>turntable stage</b>. While the audience watches the front, the crew builds the <b>next scene on the back</b>. When it's ready, the stage <b>rotates</b>, and the new scene is there instantly. If a prop is missing, they rotate back.</p>
  <ul>
    <li>The front stage is <b>blue</b> (live); the back is <b>green</b> (next).</li>
    <li>Rotating is the <b>router switch</b>.</li>
    <li>Rotating back is <b>rollback in seconds</b>.</li>
  </ul>""",
    analogy_figs=[bg_analogy],
    map=[("Front stage (live show)", "Blue environment serving users"),
         ("Back stage (next scene)", "Green environment with the new version"),
         ("Dress rehearsal", "Smoke tests on green with no user traffic"),
         ("Turntable rotates", "Load balancer / DNS switches 100% of traffic"),
         ("Rotate back", "Instant rollback to blue")],
    how_side="two environments, one switch",
    how="""  <p>The switch is <b>all-or-nothing</b>: simple and instant, but every user moves at once. For gradual exposure, see canary releases (note 02).</p>""",
    how_figs=[bg_how],
    steps=[("Two identical stacks", "Same infrastructure code for blue and green; only the version differs."),
           ("Deploy to the idle one", "Install the new build on green while blue serves traffic."),
           ("Test green privately", "Smoke tests and health checks via an internal URL."),
           ("Switch", "Point the load balancer or ingress at green; drain blue's in-flight requests."),
           ("Watch, then keep blue warm", "Monitor errors and latency; keep blue ready for a quick switch back."),
           ("Handle data carefully", "Use expand-and-contract migrations so both versions work with the same schema.")],
    vocab=[("Blue / green", "The two identical environments."),
           ("Cutover", "The moment traffic switches."),
           ("Connection draining", "Letting in-flight requests finish before shutdown."),
           ("Smoke test", "A quick check that the basics work."),
           ("Rollback", "Returning to the previous version."),
           ("Backward-compatible migration", "A schema change both versions can run against.")],
    code=dict(file="switch.sh", note="Kubernetes Service selector", src="""
# both Deployments run: app-blue (v1) and app-green (v2)
kubectl rollout status deploy/app-green              # wait until ready
./smoke-test.sh https://green.internal.example.com   # test without users

# cutover: point the Service at green
kubectl patch service app -p '{"spec":{"selector":{"app":"app","color":"green"}}}'

# watch for 15 minutes; if error rate rises, switch back in one command:
# kubectl patch service app -p '{"spec":{"selector":{"app":"app","color":"blue"}}}'
"""),
    tools="tools: load balancer target groups (AWS ALB/CodeDeploy blue/green), Kubernetes Service selectors or Argo Rollouts blueGreen strategy, Azure App Service deployment slots, Cloud Run traffic splitting, DNS weighted records.",
    gains=["<b>Zero-downtime deploys</b>.",
           "<b>Instant rollback</b>: switch back.",
           "<b>Test the real environment</b> before users see it.",
           "<b>Simple model</b> to explain."],
    losses=["<b>Double infrastructure</b> during deploys.",
            "<b>All users switch at once</b>: no gradual exposure.",
            "<b>Shared data</b> needs compatible migrations.",
            "<b>Long-lived sessions and queues</b> need draining."],
    baseline="Each line compares <b>in-place deploys with a maintenance window</b> to <b>blue–green deploys behind a switchable router</b>.",
    ratings=[(4, 4, "Two copies, one switch: easy to explain."),
             (2, 4, "Deploy any time; no maintenance windows."),
             (2, 4, "Tested before users; rollback in seconds."),
             (2, 4, "No downtime during releases."),
             (3, 3, "Neutral."),
             (2, 5, "Rollback is flipping the switch back."),
             (3, 3, "Neutral; compare blue and green metrics."),
             (4, 2, "Double capacity while both run."),
             (2, 4, "Releases stop being scary events.")],
    pitfalls=[("Breaking schema changes", "Green migrates the database; blue starts failing.", "expand-and-contract migrations."),
              ("Tearing blue down immediately", "Rollback now means a full redeploy.", "keep blue warm until green has proven itself."),
              ("Drifting environments", "Blue and green were configured by hand and differ.", "build both from the same infrastructure code."),
              ("Forgetting background work", "Old workers keep consuming jobs with old logic.", "switch workers and queues deliberately too.")],
    use=["Services where downtime is unacceptable.",
         "Releases that need a fast, reliable rollback.",
         "Teams moving away from maintenance windows."],
    skip=["Huge stateful systems where doubling is impractical (use rolling or canary).",
          "When you need gradual exposure (canary)."],
    related=["<b>Canary releases</b>", "<b>Build once, deploy many</b>", "<b>Health checks &amp; probes</b>", "<b>Expand &amp; contract</b> (Vol. 3)"],
    quiz=[("How does rollback work in blue–green?", "Switch the router back to the previous environment, which is still running."),
          ("What's the main data risk?", "Both versions share the database, so schema changes must be backward compatible."),
          ("What's the cost trade-off?", "You run two full environments during the switch."),
          ("How is blue–green different from canary?", "Blue–green switches all traffic at once; canary shifts a small share first and widens gradually.")],
    remember="Build the next scene <span class=\"hl\">backstage</span>, <span class=\"hl\">rotate</span>, and rotate <span class=\"hl\">back</span> if a prop is missing.",
    sources=["Martin Fowler, “BlueGreenDeployment” (bliki).",
             "Jez Humble &amp; David Farley, <i>Continuous Delivery</i> (2010), ch. 10.",
             "AWS whitepaper, “Blue/Green Deployments on AWS”.",
             "Argo Rollouts docs, “BlueGreen Deployment Strategy”."],
)

# ------------------------------------------------------------------ 02 Canary Releases
cn_problem = Doodle(760, 250, "Doodle of a release going to one hundred percent of users at once. A bug that only affects users on old Android phones, five percent of traffic, crashes their app. By the time alerts fire, every one of those users has been hit, and support is flooded.",
                    "Everyone gets the new version at once, so every affected user hits the bug before anyone notices.")
cn_problem.box(20, 80, 160, 70, "v2", "y", size=22)
cn_problem.arrow(186, 115, 300, 115, color="red", label="100% at once", lx=243, ly=100)
for i in range(12):
    x, y = 320 + (i % 6) * 60, 60 + (i // 6) * 70
    cn_problem.circle(x, y, 16, "pink" if i % 4 == 0 else "paper", stroke="red" if i % 4 == 0 else "")
cn_problem.note(470, 220, "every affected user hit before the alert", "red")

cn_analogy = Doodle(760, 250, "Doodle of coal miners carrying a canary into a mine. The small bird reacts to bad air long before the miners would, giving them time to get out. Only the canary is exposed first.",
                    "The canary in the coal mine: a small early warning, before everyone is exposed.")
cn_analogy.raw('<path class="d f-y" d="M120 120 q30 -40 60 -10 q20 -20 30 0 l-10 10 q10 30 -30 40 q-40 0 -50 -40 z"/><circle cx="180" cy="104" r="3"/>')
cn_analogy.note(170, 200, "small, sensitive, first", "pen")
cn_analogy.arrow(260, 130, 400, 130, dash=True)
cn_analogy.note(560, 90, "bird uneasy → everyone out", "red")
cn_analogy.note(560, 140, "bird happy → keep digging", "green")

cn_how = Doodle(760, 300, "Canary release. Traffic is split: five percent to version two, ninety-five percent to version one. An analysis step compares error rate and latency of the canary against the stable version for ten minutes. If healthy, the share grows to twenty-five, fifty, then one hundred percent. If any check fails, traffic goes back to version one automatically.",
                "Shift a little traffic, compare metrics with the stable version, widen in steps, or roll back automatically.")
steps_c = [("5%", "y"), ("25%", "y"), ("50%", "y"), ("100%", "green")]
for i, (t, f) in enumerate(steps_c):
    cn_how.box(20 + i * 160, 50, 130, 64, t, f, size=22)
    if i:
        cn_how.arrow(20 + i * 160 - 26, 82, 20 + i * 160 - 4, 82)
    cn_how.note(85 + i * 160, 140, "10 min ✓" if i < 3 else "done", "green")
cn_how.box(140, 180, 480, 60, "analysis: errors, p95 latency vs stable", "blue", size=16)
cn_how.arrow(380, 244, 380, 280, color="red")
cn_how.note(560, 278, "any check fails → back to 0%", "red")

CANARY = dict(
    slug="canary",
    kicker="a.k.a. “the canary in the coal mine”",
    tldr="Release a new version to a <b>small slice of traffic</b> first (1–5%), <b>compare its metrics</b> (errors, latency, business signals) with the stable version, and <b>widen in steps</b> only while it stays healthy. If any check fails, <b>shift traffic back automatically</b>. A bad release hurts a few users for a few minutes, not everyone.",
    chips=[("Family", "progressive delivery"), ("Tools", "Argo Rollouts, Flagger, AWS CodeDeploy, Cloud Run, Spinnaker/Kayenta"), ("Signals", "error rate, p95 latency, saturation, business KPIs"), ("Pairs with", "SLOs, observability, feature flags")],
    problem="""  <p class="lead">Some bugs only show up with <span class="hl-pink">real traffic</span>: a device type, a data shape, a load pattern. If every user gets the new version at once, every affected user hits the bug <span class="hl-pink">before anyone notices</span>.</p>
  <ul>
    <li>Staging passed, production broke for 5% of users, all at once.</li>
    <li>Alerts fire after the damage is done.</li>
    <li>Rollback decisions are made by a tired human under pressure.</li>
  </ul>""",
    problem_figs=[cn_problem],
    analogy_side="the canary in the coal mine",
    analogy="""  <p>Miners once carried a <b>canary</b> underground. The bird reacted to bad air <b>long before</b> people would, so the miners got out in time. Only the canary was exposed first.</p>
  <ul>
    <li>The canary is the <b>small slice of traffic</b> on the new version.</li>
    <li>Watching the bird is <b>automated analysis</b>.</li>
    <li>Getting out is <b>automatic rollback</b>.</li>
  </ul>""",
    analogy_figs=[cn_analogy],
    map=[("The canary", "The new version receiving 1–5% of traffic"),
         ("The miners", "The other 95–99% of users on stable"),
         ("Watching the bird", "Comparing canary vs stable metrics"),
         ("Going deeper while it's happy", "Widening to 25%, 50%, 100%"),
         ("Running out when it's uneasy", "Automatic rollback")],
    how_side="small slice, compare, widen",
    how="""  <p>The key is <b>comparison</b>: canary vs stable at the same time, so normal daily ups and downs don't fool the analysis.</p>""",
    how_figs=[cn_how],
    steps=[("Split traffic", "Weighted routing in the load balancer, ingress or service mesh."),
           ("Define health", "Error rate, p95 latency, saturation and a business signal (checkouts per minute)."),
           ("Compare against stable", "Same window, same metrics; thresholds or statistical analysis."),
           ("Step up", "1% → 5% → 25% → 50% → 100%, pausing at each step."),
           ("Automate rollback", "Any failed check sends all traffic back to stable without a human."),
           ("Keep it sticky when needed", "Route the same user consistently so they don't flip between versions.")],
    vocab=[("Canary", "The new version on a small share of traffic."),
           ("Baseline / stable", "The current version for comparison."),
           ("Traffic weight", "The percentage routed to each version."),
           ("Canary analysis", "Automated health comparison."),
           ("Progressive delivery", "Gradually exposing changes with checks."),
           ("Sticky sessions", "Keeping a user on the same version.")],
    code=dict(file="rollout.yaml", note="Argo Rollouts", src="""
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata: { name: checkout }
spec:
  strategy:
    canary:
      steps:
        - setWeight: 5
        - pause: { duration: 10m }
        - analysis: { templates: [{ templateName: error-rate-vs-stable }] }
        - setWeight: 25
        - pause: { duration: 10m }
        - setWeight: 50
        - pause: { duration: 10m }
# AnalysisTemplate: fail if canary 5xx rate > stable + 0.5% or p95 > 400 ms
# a failed analysis aborts the rollout and returns traffic to stable
"""),
    tools="tools: Argo Rollouts, Flagger (with Istio, Linkerd, NGINX, Gateway API), AWS CodeDeploy / Lambda aliases, Google Cloud Run and Cloud Deploy, Spinnaker with Kayenta, mobile staged rollouts (Play Console, App Store phased release).",
    gains=["<b>Small blast radius</b> for bad releases.",
           "<b>Real-traffic validation</b>, not just staging.",
           "<b>Automatic rollback</b>.",
           "<b>Confidence to deploy often</b>."],
    losses=["<b>Needs good metrics</b> and enough traffic.",
            "<b>Slower full rollout</b>.",
            "<b>Two versions live</b>: data and API compatibility.",
            "<b>More tooling</b> (mesh, rollout controller)."],
    baseline="Each line compares <b>releasing to 100% of traffic at once</b> to <b>canary steps with automated analysis and rollback</b>.",
    ratings=[(4, 3, "Rollout steps and analysis rules to understand."),
             (3, 3, "A release takes ~30–60 min to fully roll out."),
             (2, 5, "A bad release reaches a few percent, briefly."),
             (3, 4, "Problems are caught before most users see them."),
             (3, 3, "Neutral."),
             (2, 4, "Automatic rollback in minutes."),
             (3, 4, "Forces clear health metrics per release."),
             (4, 3, "Extra tooling; little extra capacity."),
             (3, 4, "Ship often without fear.")],
    pitfalls=[("Too little traffic", "1% of 50 requests/min tells you nothing.", "longer steps or a bigger first slice."),
              ("Only technical metrics", "No errors, but checkouts dropped 30%.", "include a business signal."),
              ("Manual watching", "Someone has to stare at dashboards.", "automate analysis and rollback."),
              ("Incompatible versions", "v1 and v2 write data the other can't read.", "backward-compatible APIs and schemas.")],
    use=["Services with steady traffic and good metrics.",
         "High-risk changes and frequent releases.",
         "Mobile and desktop apps (staged rollouts)."],
    skip=["Very low traffic (use flags for internal users instead).",
          "Changes that can't run side by side with the old version."],
    related=["<b>Blue–green deployment</b>", "<b>Feature flags</b>", "<b>SLOs &amp; error budgets</b>", "<b>Logs, metrics &amp; traces</b>"],
    quiz=[("Why compare the canary with the stable version rather than a fixed threshold?", "Traffic and error rates vary over the day; comparing at the same time removes that noise."),
          ("What should happen when canary analysis fails?", "Traffic is automatically shifted back to the stable version."),
          ("Why add a business metric?", "A release can be technically healthy while breaking something users care about, like checkout."),
          ("When is canary a poor fit?", "Very low traffic, or changes that can't run alongside the old version.")],
    remember="Send the <span class=\"hl\">canary</span> first, watch it <span class=\"hl\">closely</span>, and leave the mine if it <span class=\"hl\">struggles</span>.",
    sources=["Danilo Sato, “CanaryRelease” (martinfowler.com).",
             "Google SRE Workbook, ch. 16 “Canarying Releases”.",
             "Argo Rollouts docs, “Canary” and “Analysis &amp; Progressive Delivery”.",
             "Netflix/Google, “Automated Canary Analysis at Netflix with Kayenta”."],
)

# ------------------------------------------------------------------ 03 Feature Flags
ff_problem = Doodle(760, 250, "Doodle of a long-lived feature branch called new checkout, open for six weeks. Main has moved on, the merge has two hundred conflicts, and marketing wants the launch on a specific day at nine a.m., which means a risky deploy at exactly that moment.",
                    "A six-week branch, 200 merge conflicts, and a launch that has to be a deploy at 9:00 sharp.")
ff_problem.line("M20 80 h700", color="green")
ff_problem.note(60, 70, "main", "green")
ff_problem.line("M80 80 q40 60 120 60 h420", color="red", dash=True)
ff_problem.note(300, 166, "feature/new-checkout · 6 weeks", "red")
ff_problem.arrow(620, 140, 690, 86, color="red", label="200 conflicts", lx=640, ly=176)
ff_problem.note(380, 230, "launch = deploy at 09:00 sharp", "red")

ff_analogy = Doodle(760, 250, "Doodle of a house wired with all its lights already installed, each on its own switch. The electrician finishes the wiring weeks before the party; on the night, you just flick the switches for the rooms you want, and flick them off again if a bulb flickers.",
                    "Wire the lights early; on the night, flick the switches. Flick off if a bulb flickers.")
ff_analogy.icon("lamp", 60, 50, 1.6, fill="y")
ff_analogy.icon("lamp", 200, 50, 1.6)
ff_analogy.note(160, 200, "wired weeks ago", "pen")
for i, (t, on) in enumerate([("living room", True), ("garden", False), ("kitchen", True)]):
    ff_analogy.icon("switch", 400, 30 + i * 64, 0.8, fill="green" if on else "paper")
    ff_analogy.note(470, 58 + i * 64, t + (" · on" if on else " · off"), "green" if on else "pen", anchor="start")

ff_how = Doodle(760, 290, "Feature flags in practice. New checkout code is merged to main behind a flag that's off. The flag service decides per request: on for staff, then ten percent of users in the Netherlands, then everyone. A kill switch turns it off instantly without a deploy. After full launch the flag and old code are deleted.",
                "Merge code switched off; turn it on for staff, then a slice, then everyone. Kill switch included. Then delete the flag.")
ff_how.box(20, 40, 200, 70, "code on main", "blue", sub="behind flag: off")
ff_how.arrow(226, 75, 300, 75)
ff_how.box(306, 30, 180, 90, "flag service", "y", sub="rules per user")
for i, (t, f) in enumerate([("staff", "green"), ("10% NL", "green"), ("everyone", "green")]):
    ff_how.box(540, 20 + i * 52, 200, 40, t, f, size=16)
    ff_how.arrow(492, 75, 536, 40 + i * 52)
ff_how.box(306, 170, 180, 50, "kill switch: off", "pink", stroke="red", size=16)
ff_how.box(20, 200, 220, 54, "then delete the flag", "paper", stroke="green", size=16)

FLAGS = dict(
    slug="feature-flags",
    kicker="a.k.a. “wire the lights early”",
    tldr="<b>Separate deploying from releasing.</b> Merge unfinished or risky code to main <b>behind a flag that's off</b>, deploy it any time, then turn it on <b>for staff, a percentage, a country or a customer</b> without a deploy. A <b>kill switch</b> turns it off in seconds. Flags are temporary: <b>delete them</b> once a feature is fully launched.",
    chips=[("Family", "progressive delivery"), ("Kinds", "release, experiment, ops (kill switch), permission"), ("Tools", "LaunchDarkly, Unleash, Flagsmith, OpenFeature"), ("Pairs with", "canary releases, trunk-based development")],
    problem="""  <p class="lead">Without flags, “not ready yet” means a <span class="hl-pink">long-lived branch</span>, and “launch” means a <span class="hl-pink">deploy at a precise moment</span>. Both are risky and slow.</p>
  <ul>
    <li>Feature branches drift for weeks and end in painful merges.</li>
    <li>The launch time is set by marketing, so the deploy is too.</li>
    <li>Turning a broken feature off means another deploy, under pressure.</li>
  </ul>""",
    problem_figs=[ff_problem],
    analogy_side="the lights on switches",
    analogy="""  <p>An electrician wires every light in the house <b>weeks before the party</b>, each on its <b>own switch</b>. On the night you just flick on the rooms you want, and if a bulb flickers you <b>flick it off</b>. Nobody rewires the house during the party.</p>
  <ul>
    <li>Wiring is <b>deploying the code</b>.</li>
    <li>Flicking switches is <b>releasing</b>.</li>
    <li>Turning a flickering bulb off is the <b>kill switch</b>.</li>
  </ul>""",
    analogy_figs=[ff_analogy],
    map=[("Wiring done weeks early", "Code merged and deployed, flag off"),
         ("A switch per room", "A flag per feature"),
         ("Lights on for family first", "Targeting rules: staff, beta users, 10%"),
         ("Flick off a flickering bulb", "Kill switch, no deploy needed"),
         ("Removing old switches", "Deleting the flag and dead code after launch")],
    how_side="deploy dark, release by rule",
    how="""  <p>Flags make deploys boring and releases a <b>product decision</b>, but each flag is technical debt with an expiry date.</p>""",
    how_figs=[ff_how],
    steps=[("Wrap the change", "One check at the entry point: <code>if (flags.isOn(\"new-checkout\", user))</code>."),
           ("Default to off (safe)", "If the flag service is unreachable, fall back to the old behaviour."),
           ("Roll out by rule", "Staff → beta customers → 10% → 100%, watching metrics."),
           ("Keep a kill switch", "Ops flags for risky dependencies and expensive features."),
           ("Set an expiry", "Each release flag gets an owner and a removal ticket."),
           ("Delete it", "Remove the flag and the old code path once fully launched.")],
    vocab=[("Feature flag / toggle", "A runtime switch for a code path."),
           ("Release flag", "Temporary flag to roll out a feature."),
           ("Kill switch", "Ops flag to disable something instantly."),
           ("Targeting", "Rules deciding who sees a flag (user, %, region)."),
           ("Dark launch", "Deploying code that's off for users."),
           ("Flag debt", "Old flags and dead code left behind.")],
    code=dict(file="checkout.ts", note="OpenFeature SDK", src="""
import { OpenFeature } from "@openfeature/server-sdk";
const flags = OpenFeature.getClient();

export async function checkoutPage(req: Request) {
  const useNew = await flags.getBooleanValue(
    "new-checkout",                    // owner: payments · remove by 2027-01-31
    false,                             // safe default if the flag service is down
    { targetingKey: req.user.id, country: req.user.country, plan: req.user.plan },
  );
  return useNew ? renderNewCheckout(req) : renderLegacyCheckout(req);
}
// rules live in the flag service: staff → NL 10% → all
// after 100% for two weeks: delete the flag and renderLegacyCheckout
"""),
    tools="tools: LaunchDarkly, Unleash, Flagsmith, GrowthBook, ConfigCat, Split, AWS AppConfig, Firebase Remote Config, OpenFeature (vendor-neutral SDK standard).",
    gains=["<b>Deploy any time</b>; release when ready.",
           "<b>Kill switch</b> without a deploy.",
           "<b>Gradual rollouts</b> and targeted betas.",
           "<b>Short-lived branches</b>: merge daily."],
    losses=["<b>Flag debt</b> and dead code.",
            "<b>More code paths</b> to test.",
            "<b>A runtime dependency</b> on the flag service.",
            "<b>Confusing</b> when many flags interact."],
    baseline="Each line compares <b>long-lived feature branches and launch-day deploys</b> to <b>trunk-based development with release flags and kill switches</b>.",
    ratings=[(4, 3, "Extra branches in code while flags live."),
             (2, 5, "Merge daily; release without deploying."),
             (2, 5, "Turn things off in seconds."),
             (3, 4, "Kill switches limit incidents."),
             (3, 3, "Neutral."),
             (2, 4, "Disabling is faster than rolling back."),
             (3, 4, "Flag state is part of every event."),
             (4, 3, "Flag service fees or self-hosting."),
             (2, 4, "No merge hell; product controls launches.")],
    pitfalls=[("Never deleting flags", "300 flags, half forgotten, some contradicting.", "owner + expiry per flag; delete after launch."),
              ("Unsafe defaults", "Flag service down → new, half-finished feature shown.", "default to the safe (old) path."),
              ("Flags inside flags", "Combinations nobody has tested.", "keep flags independent; test both paths of each."),
              ("Using flags for permissions forever", "Paid features live in a release-flag tool.", "use real entitlements for long-term access rules.")],
    use=["Trunk-based development.",
         "Launches timed by product or marketing.",
         "Risky changes needing a kill switch.",
         "Betas and experiments."],
    skip=["Tiny, low-risk changes (just ship them).",
          "Permanent configuration (use config, not flags)."],
    related=["<b>Canary releases</b>", "<b>Build once, deploy many</b>", "<b>Optimistic UI</b> (Vol. 2)", "<b>Circuit breaker</b> (Vol. 1)"],
    quiz=[("What does “separate deploy from release” mean?", "Code can be in production but switched off; turning it on for users is a separate, runtime decision."),
          ("What should a flag default to if the service is down?", "The safe, existing behaviour."),
          ("What's a kill switch?", "An operational flag that disables a feature or dependency instantly without a deploy."),
          ("Why delete flags after launch?", "Old flags leave dead code and untested combinations: flag debt.")],
    remember="<span class=\"hl\">Wire</span> early, <span class=\"hl\">switch</span> on the night, and take the old switches <span class=\"hl\">off the wall</span>.",
    sources=["Pete Hodgson, “Feature Toggles (aka Feature Flags)” (martinfowler.com).",
             "OpenFeature specification (openfeature.dev).",
             "Paul Hammant, trunkbaseddevelopment.com.",
             "Accelerate (Forsgren, Humble, Kim), trunk-based development findings."],
)

# ------------------------------------------------------------------ 04 Build Once, Deploy Many
bo_problem = Doodle(760, 250, "Doodle of three separate builds: one for staging, one for production, each running npm install at a different time. Production pulls a newer dependency version than staging did, so the code that passed testing is not the code that ships. A bug appears only in production.",
                    "Rebuilding per environment: what you tested isn't what you shipped.")
for i, (t, v) in enumerate([("build for test", "lib 2.3.1"), ("build for staging", "lib 2.3.1"), ("build for prod", "lib 2.4.0 !")]):
    bo_problem.box(20 + i * 250, 60, 220, 80, t, "pink" if i == 2 else "paper", sub=v, stroke="red" if i == 2 else "", size=17)
bo_problem.note(380, 190, "tested ≠ shipped", "red")
bo_problem.note(380, 220, "“works in staging” bugs", "red")

bo_analogy = Doodle(760, 250, "Doodle of a sealed, numbered shipping container. It's packed and sealed once at the factory, then moves from truck to train to ship to warehouse without ever being opened or repacked. Only the delivery address changes at each stage.",
                    "A sealed shipping container: packed once, same seal number at every stop. Only the address label changes.")
bo_analogy.icon("container", 30, 70, 1.6, fill="y")
bo_analogy.note(90, 190, "sealed #A7F3", "pen")
for i, t in enumerate(["truck", "train", "ship"]):
    bo_analogy.arrow(160 + i * 170, 110, 290 + i * 170, 110, label="same seal", lx=225 + i * 170, ly=96)
    bo_analogy.note(330 + i * 170, 150, t, "pen")
bo_analogy.note(450, 220, "only the address label changes", "green")

bo_how = Doodle(760, 290, "Build once, deploy many. CI builds one container image from a commit, tags it with the commit hash and its digest, and runs tests against it. The same digest is promoted to test, staging and production. Each environment injects its own configuration and secrets at runtime. Nothing is rebuilt.",
                "One build, one digest. Promote the identical artefact; inject config per environment at runtime.")
bo_how.box(20, 40, 160, 70, "commit 3f2a", "blue")
bo_how.arrow(186, 75, 256, 75, label="build", lx=221, ly=61)
bo_how.icon("container", 262, 50, 1.0, fill="y")
bo_how.note(300, 130, "image@sha256:9c1e…", "pen")
for i, t in enumerate(["test", "staging", "prod"]):
    bo_how.arrow(340, 80, 470, 40 + i * 70)
    bo_how.box(476, 20 + i * 70, 140, 44, t, "green", size=17)
    bo_how.note(630, 48 + i * 70, f"+ {t} config", "pen", anchor="start")
bo_how.note(240, 250, "same digest everywhere; nothing rebuilt", "green")

BUILDONCE = dict(
    slug="build-once",
    kicker="a.k.a. “the sealed container”",
    tldr="Build your app <b>exactly once</b> per commit into an <b>immutable artefact</b> (a container image, a bundle), identify it by <b>digest</b>, test it, and <b>promote that same artefact</b> through test, staging and production. Each environment supplies its own <b>configuration and secrets at runtime</b>. What you tested is, byte for byte, what you ship.",
    chips=[("Family", "delivery pipeline"), ("Artefacts", "container images, JARs, bundles, AMIs"), ("Identify by", "content digest + commit SHA"), ("Pairs with", "blue–green, GitOps, supply-chain hygiene (Vol. 5)")],
    problem="""  <p class="lead">When each environment gets its <span class="hl-pink">own build</span>, dependencies, compilers and base images can differ between them. The code that passed testing is <span class="hl-pink">not the code that ships</span>.</p>
  <ul>
    <li>Production pulled a newer library than staging tested.</li>
    <li>Environment-specific values are baked in at build time.</li>
    <li>Nobody can say exactly what's running in production.</li>
  </ul>""",
    problem_figs=[bo_problem],
    analogy_side="the sealed shipping container",
    analogy="""  <p>A shipping container is <b>packed and sealed once</b> at the factory. It moves from truck to train to ship <b>without being opened</b>, and the <b>seal number</b> proves it. Only the <b>address label</b> changes along the way.</p>
  <ul>
    <li>The sealed container is the <b>artefact</b>.</li>
    <li>The seal number is the <b>digest</b>.</li>
    <li>The address label is <b>runtime config</b>.</li>
  </ul>""",
    analogy_figs=[bo_analogy],
    map=[("Packing once at the factory", "One CI build per commit"),
         ("The seal number", "Image digest (<code>sha256:…</code>)"),
         ("Never repacked on the way", "Promoted unchanged between environments"),
         ("Address label per stop", "Environment config and secrets at runtime"),
         ("Customs checks the seal", "Deploys verify digest and signature")],
    how_side="one artefact, many environments",
    how="""  <p>Promotion becomes a <b>pointer change</b> (“prod now runs digest 9c1e…”), which also makes rollback a pointer change.</p>""",
    how_figs=[bo_how],
    steps=[("Build in CI only", "No laptop builds for deploys; reproducible inputs (lockfiles, pinned base images)."),
           ("Tag by commit and digest", "Human-readable tag + immutable digest; deploy by digest."),
           ("Keep config out of the build", "Environment variables, config maps and secrets injected at runtime (12-factor)."),
           ("Promote, don't rebuild", "The pipeline moves the same digest from test → staging → prod."),
           ("Record what's where", "A deploy log or GitOps repo states which digest runs in each environment."),
           ("Roll back by pointer", "Redeploy the previous digest.")],
    vocab=[("Artefact", "The built, deployable output of a commit."),
           ("Immutable", "Never changed after it's built."),
           ("Digest", "A content hash that uniquely identifies an artefact."),
           ("Promotion", "Moving an artefact to the next environment."),
           ("12-factor config", "Config from the environment, not the build."),
           ("Reproducible build", "Same inputs always produce the same output.")],
    code=dict(file=".github/workflows/release.yml", note="build once, promote by digest", src="""
jobs:
  build:
    outputs: { digest: ${{ steps.push.outputs.digest }} }
    steps:
      - uses: actions/checkout@v5
      - id: push
        uses: docker/build-push-action@v6
        with: { push: true, tags: "ghcr.io/acme/web:${{ github.sha }}" }

  deploy-staging:
    needs: build
    steps:
      - run: ./deploy.sh staging ghcr.io/acme/web@${{ needs.build.outputs.digest }}

  deploy-prod:
    needs: [build, deploy-staging]
    environment: production              # approval gate
    steps:
      - run: ./deploy.sh prod ghcr.io/acme/web@${{ needs.build.outputs.digest }}
"""),
    tools="tools: container registries (GHCR, ECR, Artifact Registry), artefact repositories (Artifactory, Nexus), Docker Buildx / Bazel for reproducible builds, deploy-by-digest in Kubernetes and Cloud Run, Kustomize/Helm for per-environment config.",
    gains=["<b>Tested = shipped</b>, byte for byte.",
           "<b>Faster pipelines</b>: no rebuilds.",
           "<b>Clear inventory</b> of what runs where.",
           "<b>Simple rollback</b> to a previous digest."],
    losses=["<b>Config discipline</b>: nothing environment-specific at build time.",
            "<b>Registry storage</b> for many artefacts.",
            "<b>Frontend builds</b> that inline env vars need rework."],
    baseline="Each line compares <b>rebuilding separately for each environment</b> to <b>one immutable artefact promoted by digest</b>.",
    ratings=[(3, 4, "One build, one pointer per environment."),
             (3, 4, "Promotion skips rebuilds."),
             (2, 5, "Exactly what was tested goes live."),
             (3, 4, "No environment-only build surprises."),
             (3, 3, "Neutral."),
             (3, 4, "Roll back by redeploying the previous digest."),
             (2, 4, "Every environment reports its digest."),
             (3, 4, "Fewer CI minutes; some registry storage."),
             (3, 4, "Clear, predictable pipeline.")],
    pitfalls=[("Baking config into the build", "<code>API_URL</code> inlined at build time per environment.", "load config at runtime (or a config.json served per environment)."),
              ("Deploying by mutable tag", "<code>:latest</code> or <code>:staging</code> changes underneath you.", "deploy by digest."),
              ("Laptop builds", "“Quick fix” built and pushed from a laptop.", "only CI builds deployable artefacts."),
              ("Rebuilding for a hotfix", "The emergency fix skips the pipeline.", "same pipeline, just faster gates.")],
    use=["Any service deployed to more than one environment.",
         "Container-based and serverless deployments.",
         "Regulated environments that need traceability."],
    skip=["Truly single-environment scripts.",
          "Static sites whose content is the build (still: build once per content change)."],
    related=["<b>Blue–green deployment</b>", "<b>GitOps</b>", "<b>Immutable infrastructure</b>", "<b>Supply-chain hygiene</b> (Vol. 5)"],
    quiz=[("Why not rebuild for each environment?", "Dependencies and tools can differ between builds, so the shipped code isn't what was tested."),
          ("Why deploy by digest rather than tag?", "Tags can be moved; a digest always identifies the exact same artefact."),
          ("Where should environment-specific values come from?", "Runtime configuration and secrets, not the build."),
          ("How does rollback work?", "Redeploy the previous known-good digest.")],
    remember="Pack it <span class=\"hl\">once</span>, check the <span class=\"hl\">seal</span>, change only the <span class=\"hl\">label</span>.",
    sources=["Jez Humble &amp; David Farley, <i>Continuous Delivery</i>, ch. 5 “Anatomy of the Deployment Pipeline”.",
             "The Twelve-Factor App, “III. Config” and “V. Build, release, run”.",
             "Docker docs, “Image digests”.",
             "reproducible-builds.org."],
)

NOTES = [BLUEGREEN, CANARY, FLAGS, BUILDONCE]
