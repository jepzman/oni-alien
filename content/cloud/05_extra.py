# Vol. 6 · extra notes (November 2026): Progressive Delivery, Service Catalogue, Chaos Engineering.
# Numbered 16–18 so earlier note URLs and PDF names stay the same. Fault injection inside test suites is in Vol. 4.

# ------------------------------------------------------------------ 16 Progressive delivery
pd_problem = Doodle(760, 250, "Doodle of a change rolled out everywhere after a successful canary. The canary ran in one region for 15 minutes at 5 percent and looked fine. The release then went to all six regions at once. A bug that only showed with one region's payment provider took down checkout in that region, and a config error took down another, at the same time.",
                    "One good canary, then everywhere at once: the problems the canary couldn't see arrive together.")
pd_problem.box(10, 70, 200, 80, "canary", "green", sub="1 region · 5% · 15 min ✓", size=17, subsize=12)
pd_problem.arrow(214, 110, 266, 110)
for i in range(6):
    bad = i in (2, 4)
    pd_problem.box(270 + (i % 3) * 160, 40 + (i // 3) * 80, 150, 64, f"region {i + 1}", "pink" if bad else "blue", stroke="red" if bad else "", sub="down" if bad else "100%", size=15, subsize=13)
pd_problem.note(500, 220, "all regions at once: two different failures, one evening", "red", size=16)

pd_analogy = Doodle(760, 250, "Doodle of opening a new metro line. First staff ride it, then a few off-peak trains with passengers, then rush hour on one branch, then the whole line. At each step an inspector checks a list before the next one. If something is off, they stop and go back one step.",
                    "Staff first, then off-peak, then one branch at rush hour, then the whole line, with an inspector at each step.")
pd_analogy.row([("staff only", "", "paper"), ("off-peak", "few passengers", "y"), ("one branch", "rush hour", "blue"), ("whole line", "", "green")], x=20, y=50, h=76, gap=40, size=17, subsize=13, arrows=True)
pd_analogy.note(380, 176, "an inspector checks before each step", "pen", size=16)
pd_analogy.note(380, 206, "something off → stop, go back one step", "red", size=16)

pd_how = Doodle(760, 300, "A progressive delivery pipeline. The same build moves through rings: internal users, a 1 percent canary in one region, 25 percent of that region, then region by region. Between rings it waits a bake time and an automated check compares error rate, latency and a business metric with the previous version and the SLO burn rate. A failed check rolls back automatically and stops the rollout.",
                "Rings, bake times and automatic gates between them; a failed gate rolls back on its own.")
pd_how.row([("internal", "staff · 1 h", "paper"), ("canary", "1% · region A", "y"), ("region A", "25% → 100%", "blue"), ("region B…F", "one at a time", "green")], x=20, y=40, h=80, gap=40, size=17, subsize=13, arrows=True)
for x in (186, 372, 558):
    pd_how.circle(x, 160, 14, fill="paper", label="✓")
pd_how.note(380, 204, "gate: errors · p99 · checkout success · SLO burn, vs the old version", "pen", size=15)
pd_how.box(200, 228, 360, 50, "failed gate → automatic rollback", "pink", stroke="red", size=15)

PROGRESSIVE_DELIVERY = dict(
    slug="progressive-delivery",
    kicker="a.k.a. “ring by ring, with a robot at every gate”",
    tldr="A canary tests a change on a small slice. <b>Progressive delivery</b> extends that to the whole rollout: the same build moves through <b>rings</b> (staff, a small canary, one region, then the rest, one at a time), with a <b>bake time</b> and an <b>automated gate</b> between rings that compares errors, latency, a business metric and the SLO burn rate with the old version. A failing gate <b>rolls back on its own</b>. Feature flags do the same for features inside a deploy.",
    chips=[("Family", "shipping safely"), ("Builds on", "canary releases, feature flags"), ("Tools", "Argo Rollouts, Flagger, Spinnaker, cloud deployment services"), ("Pairs with", "SLOs &amp; error budgets, logs, metrics &amp; traces")],
    problem="""  <p class="lead">A release passed its canary: 5% of one region for 15 minutes. Then it went to <b>all six regions at once</b>. A bug that only showed with one region's payment provider took down checkout there, and a config value missing in another region took that one down too, <span class="hl-pink">at the same time, on the same evening</span>.</p>
  <ul>
    <li>A single canary can't see problems that depend on <b>region, tenant, time of day or scale</b>.</li>
    <li>After the canary, the next step is usually <b>everything</b>: the largest possible blast radius.</li>
    <li>Humans watching dashboards decide “looks fine” differently at 6 p.m. on a Friday.</li>
  </ul>""",
    problem_figs=[pd_problem],
    analogy_side="opening a new metro line",
    analogy="""  <p>A new metro line doesn't open to rush hour on day one. <b>Staff ride it</b> first, then a few <b>off-peak trains</b> with passengers, then <b>one branch at rush hour</b>, then the whole line. An <b>inspector checks a list</b> before each step, and if anything is off, they stop and go back one step.</p>""",
    analogy_figs=[pd_analogy],
    map=[("Staff riding first", "An internal ring: employees and test accounts"),
         ("Off-peak trains", "A small canary in one region"),
         ("One branch at rush hour", "A whole region at full traffic"),
         ("The inspector's checklist", "An automated gate: metrics against thresholds and the old version"),
         ("Back one step", "Automatic rollback when a gate fails")],
    how_side="rings, bake times, automatic gates",
    how="""  <p>Define the rings once, as part of the pipeline. Each ring has a size, a <b>bake time</b> long enough to see real traffic (including a peak if possible), and a <b>gate</b>: queries that compare the new version with the old on errors, latency, a business signal, and the SLO burn rate. Passing gates promote the build; failing gates roll back and stop the rollout, without anyone needing to be awake.</p>""",
    how_figs=[pd_how],
    steps=[("Define the rings", "Internal → 1% canary in one region → that region → other regions one by one (or by cell or tenant group)."),
           ("Set bake times", "Long enough to see normal traffic: 30–60 minutes per ring, longer for changes that touch nightly jobs."),
           ("Write the gates as queries", "Error rate, p99 latency and a business metric (checkout success), each compared with the stable version, plus SLO burn."),
           ("Roll back automatically", "A failed gate shifts traffic back and pages the owner; promotion past it needs a fix, not a click."),
           ("Use flags for features", "Deploy dark, then enable the feature ring by ring with flags, using the same gates.")],
    vocab=[("Progressive delivery", "Rolling out in stages with automated checks between them."),
           ("Ring", "A group of users, hosts or regions that gets a release together."),
           ("Bake time", "How long a release runs in a ring before the next step."),
           ("Gate", "An automated check that decides promote or roll back."),
           ("Blast radius", "How many users a bad change can reach."),
           ("Cell", "An independent copy of the stack serving a slice of users.")],
    code=dict(file="rollout.yaml", note="Argo Rollouts, one region (generic)", src="""
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata: { name: checkout }
spec:
  strategy:
    canary:
      steps:
        - setWeight: 1
        - pause: { duration: 30m }          # bake
        - analysis: { templates: [{ templateName: checkout-gate }] }
        - setWeight: 25
        - pause: { duration: 60m }          # includes the evening peak when possible
        - analysis: { templates: [{ templateName: checkout-gate }] }
        - setWeight: 100
---
kind: AnalysisTemplate
metadata: { name: checkout-gate }
spec:
  metrics:
    - name: checkout-success-vs-stable       # business signal, canary minus stable
      successCondition: result[0] >= -0.5      # at most 0.5 points worse
      failureLimit: 1
      provider: { prometheus: { query: "{{ checkout_success_canary - checkout_success_stable }}" } }
# the pipeline runs this per region, one region at a time, and stops on the first failure
"""),
    tools="tools: Argo Rollouts, Flagger, Spinnaker / Kayenta, AWS CodeDeploy and AppConfig, Google Cloud Deploy, Azure Deployment Environments, LaunchDarkly / Unleash / OpenFeature for flag rollouts.",
    gains=["<b>Small blast radius</b> at every step.",
           "<b>Problems that need scale or a region</b> show up early and in one place.",
           "<b>No one has to watch dashboards</b>: gates decide, consistently.",
           "<b>Faster, calmer releases</b> overall: more deploys, fewer incidents."],
    losses=["<b>Slower full rollout</b>: hours instead of minutes.",
            "<b>Good metrics are required</b>: gates are only as smart as the queries.",
            "<b>Mixed versions</b> run side by side for longer.",
            "<b>Pipeline complexity</b>: rings, analysis templates, region ordering."],
    baseline="Each line compares <b>one canary, then everywhere</b> to <b>ring-by-ring rollout with automated gates and rollback</b>.",
    ratings=[(3, 2, "Rings, gates and analysis to set up."),
             (3, 3, "Each release takes longer; teams release more often."),
             (3, 5, "A bad change reaches a ring, not everyone."),
             (3, 4, "Fewer region-wide incidents."),
             (3, 3, "Neutral."),
             (3, 4, "Automatic rollback within minutes."),
             (3, 4, "Gates force good per-version metrics."),
             (3, 3, "Neutral: some tooling, fewer incidents."),
             (3, 4, "Ship and walk away; the gates watch.")],
    pitfalls=[("Gates on averages only", "Overall error rate looks fine while one tenant or region is broken.", "compare canary with stable, and split by region or tenant where it matters."),
              ("Bake times too short", "15 minutes at 3 a.m. sees almost no traffic.", "bake long enough to see real load, or until enough requests have passed."),
              ("Manual promotion", "A person clicks “promote” after a glance, and the gates are ignored.", "let passing gates promote; overriding a failure needs a recorded reason."),
              ("Database changes in the rollout", "The schema change can't be rolled back with the code.", "change schemas separately with expand and contract, before the code rollout.")],
    use=["Services with many users, several regions or tenants.",
         "Teams that release often and want to stop watching dashboards.",
         "Changes whose failures depend on scale or region."],
    skip=["A small internal tool with one instance.",
          "No reliable per-version metrics yet: build those first.",
          "Urgent security fixes, where speed beats staging (still watch closely)."],
    related=["<b>Canary releases</b>", "<b>Feature flags</b>", "<b>SLOs &amp; error budgets</b>", "<b>Expand &amp; contract</b> (Vol. 3)"],
    quiz=[("How is progressive delivery different from a single canary?", "The whole rollout is staged in rings, each with a bake time and an automated gate, instead of canary then everywhere."),
          ("What should a gate compare?", "The new version with the stable one on errors, latency and a business metric, plus the SLO burn rate."),
          ("What happens when a gate fails?", "Traffic shifts back to the old version automatically and the rollout stops."),
          ("Why roll out region by region?", "Some problems depend on a region's data, providers or config; one region at a time limits the damage.")],
    quiz_sit=[("A release passes the canary and region A, then breaks checkout in region C because of a missing config value only C needs. The rollout had moved to B, C and D together. What do you change?",
               "Roll out one region at a time after the first, with a gate per region that includes checkout success, so C's failure stops the rollout with only C affected. Also check required config per region in the pipeline before deploying.")],
    try_it="In a local cluster, install Argo Rollouts and convert one Deployment to a Rollout with steps at 10%, 50% and 100% and a short pause between. Add an analysis step that queries an error rate (even a fake Prometheus metric), make the new version fail it, and watch the rollout abort and return to the stable version.",
    remember="<span class=\"hl\">Ring by ring</span>, with a <span class=\"hl\">robot at every gate</span>.",
    sources=["James Governor, “Towards Progressive Delivery” (RedMonk, 2018).",
             "Argo Rollouts documentation, “Analysis &amp; Progressive Delivery”.",
             "Clare Liguori, “Automating safe, hands-off deployments”, Amazon Builders' Library.",
             "Google SRE Workbook, chapter 16, “Canarying Releases”."],
)

# ------------------------------------------------------------------ 17 Service catalogue
sc_problem = Doodle(760, 250, "Doodle of an incident with no owner. At 2 a.m. an alert fires for a service called ledger-sync. Nobody on call knows what it does, who owns it, where its dashboards are, or which services depend on it. It takes 50 minutes and four people to find the team that wrote it two years ago.",
                    "2 a.m.: “what is ledger-sync, and whose is it?” Fifty minutes to find out.")
sc_problem.box(20, 70, 190, 80, "alert", "pink", stroke="red", sub="ledger-sync · errors", size=18, subsize=13)
sc_problem.arrow(214, 110, 286, 110, color="red")
for i, q in enumerate(["what does it do?", "who owns it?", "where's the runbook?", "who depends on it?"]):
    sc_problem.box(290 + (i % 2) * 230, 40 + (i // 2) * 76, 210, 56, q, "paper", size=15)
sc_problem.note(500, 220, "50 minutes and 4 people before anyone can act", "red", size=16)

sc_analogy = Doodle(760, 250, "Doodle of a building's directory board in the lobby. Each office is listed with the company, the floor, a contact and the emergency number. When a pipe bursts on floor 6, the caretaker reads the board and calls the right person, instead of knocking on every door.",
                    "The lobby directory: who's in each office, and who to call when something leaks.")
sc_analogy.table(40, 30, "directory", ["fl. 3 · Acme · Joost", "fl. 6 · Ledger team · Mira", "fl. 7 · Search · Ben"], w=280, fill="y", hl=(1,), size=16)
sc_analogy.arrow(330, 90, 446, 90, label="pipe burst on 6", lx=388, ly=78)
sc_analogy.box(450, 50, 260, 80, "call Mira", "green", sub="on call for floor 6", size=18, subsize=13)
sc_analogy.note(380, 200, "no knocking on every door", "pen", size=16)

sc_how = Doodle(760, 280, "A service catalogue entry. Each service has a small file in its own repository: name, what it does, owning team, on-call rotation, tier, links to dashboards, runbook and docs, and the services and data it depends on. The catalogue collects these files into one searchable portal, draws the dependency graph, and checks that every service has an owner and a runbook.",
                "A small file in each repo; one portal that collects, links and checks them.")
sc_how.box(20, 40, 280, 200, None, "y")
sc_how.head(160, 70, "catalog-info.yaml", size=17)
for k, line in enumerate(["owner: team-ledger", "on-call: ledger-primary", "tier: 1 (customer-facing)", "runbook · dashboards · docs", "depends on: payments, postgres"]):
    sc_how.text(40, 104 + k * 26, line, "t", anchor="start", size=15)
sc_how.arrow(304, 140, 396, 140, label="collected", lx=350, ly=128)
sc_how.box(400, 60, 340, 160, "catalogue portal", "green", sub="search · owners · dependency graph · checks", size=18, subsize=13)

SERVICE_CATALOGUE = dict(
    slug="service-catalogue",
    kicker="a.k.a. “what is this, and whose is it?”",
    tldr="With dozens or hundreds of services, the questions that matter at 2 a.m. are simple and hard to answer: <b>what does it do, who owns it, how do I run it, what depends on it?</b> A <b>service catalogue</b> answers them in one place. Each service keeps a small <b>metadata file in its own repository</b> (owner, on-call, tier, links, dependencies); a portal collects them, draws the graph, and <b>checks</b> that every service meets the basics.",
    chips=[("Family", "running it"), ("Common tool", "Backstage (CNCF), or Port, Cortex, OpsLevel"), ("Lives in", "a catalog-info.yaml next to each service's code"), ("Pairs with", "golden paths, incident response, cost visibility")],
    problem="""  <p class="lead">At 2 a.m. an alert fires for <code>ledger-sync</code>. Nobody on call knows what it does, who owns it, where its dashboards are, or what breaks if it stays down. <span class="hl-pink">Fifty minutes and four people later</span>, someone finds the team that wrote it two years ago.</p>
  <ul>
    <li>Knowledge of who owns what lives in people's heads and old chat threads.</li>
    <li>Wikis listing services go <b>out of date</b> within months.</li>
    <li>Nobody can answer “which services handle personal data?” or “who still runs the old Java version?”</li>
  </ul>""",
    problem_figs=[sc_problem],
    analogy_side="the lobby directory",
    analogy="""  <p>A building's <b>directory board</b> lists every office: company, floor, contact and emergency number. When a pipe bursts on floor 6, the caretaker reads the board and <b>calls the right person</b>, instead of knocking on every door. Tenants update their own line when they move.</p>""",
    analogy_figs=[sc_analogy],
    map=[("A line on the directory board", "A service's catalogue entry"),
         ("The tenant updating their own line", "The metadata file lives in the service's repo, owned by its team"),
         ("Floor and contact", "Owner team and on-call rotation"),
         ("“Who's below floor 6?”", "The dependency graph"),
         ("The building manager's checks", "Scorecards: owner, runbook, alerts, supported versions")],
    how_side="a file per service, one portal for all",
    how="""  <p>Each team describes its services in a small YAML file next to the code, so it's reviewed and changed with the code. The catalogue collects every file, links each service to its team, dashboards, runbook and docs, and draws who depends on whom. <b>Scorecards</b> check the basics automatically (an owner, an on-call, a runbook, alerts, a supported runtime) and show what's missing.</p>""",
    how_figs=[sc_how],
    steps=[("Start with ownership", "One required field first: every service has an owning team. Import the list from your repos and deploy tooling."),
           ("Put the file in the repo", "<code>catalog-info.yaml</code> next to the code, so changes are reviewed and it moves with the service."),
           ("Add the 2 a.m. links", "On-call rotation, dashboards, runbook, logs, docs, tier."),
           ("Record dependencies", "APIs it provides and consumes, data stores, queues; draw the graph."),
           ("Add scorecards slowly", "A few checks that matter (owner, runbook, alerts), visible per team; avoid a wall of red on day one.")],
    vocab=[("Service catalogue", "A searchable list of every service with its metadata."),
           ("Owner", "The team accountable for a service, day and night."),
           ("Tier", "How critical a service is, which sets its expectations."),
           ("Scorecard", "Automated checks of a service against agreed standards."),
           ("Dependency graph", "Which services call or rely on which."),
           ("Developer portal", "A site combining the catalogue, docs and self-service templates.")],
    code=dict(file="catalog-info.yaml", note="Backstage format", src="""
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: ledger-sync
  description: Copies settled payments into the finance ledger every 5 minutes.
  annotations:
    pagerduty.com/service-id: P4LEDGR
    grafana/dashboard-selector: "service=ledger-sync"
    backstage.io/techdocs-ref: dir:.
  links:
    - { url: https://runbooks.internal/ledger-sync, title: Runbook }
  tags: [payments, personal-data]
spec:
  type: service
  lifecycle: production
  owner: team-ledger
  system: payments
  tier: 1                                  # customer-facing: money is late without it
  dependsOn: [component:payments-api, resource:ledger-db]
  providesApis: [ledger-events]
"""),
    tools="tools: Backstage (CNCF) with its catalogue, TechDocs and scorecard plugins, Port, Cortex, OpsLevel, Compass (Atlassian), GitHub CODEOWNERS and custom properties as a starting point.",
    gains=["<b>Faster incidents</b>: the owner and runbook are one search away.",
           "<b>Answers to fleet questions</b>: who handles personal data, who runs an old version.",
           "<b>Clear ownership</b>: no orphan services.",
           "<b>A home for golden paths</b>: new services start from templates that fill in the entry."],
    losses=["<b>Upkeep</b>: entries rot if nothing checks them.",
            "<b>A portal to run</b> (Backstage is real work) or to pay for.",
            "<b>Adoption</b>: teams must see value, not paperwork.",
            "<b>Dependency data</b> written by hand drifts; better generated from traces."],
    baseline="Each line compares <b>ownership knowledge in heads and wikis</b> to <b>a catalogue fed by files in each repo, with scorecards</b>.",
    ratings=[(3, 3, "Neutral: a file per service and a portal."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Faster to the right person during incidents."),
             (2, 4, "Works for 50 or 500 services."),
             (2, 4, "Runbooks and owners found in seconds."),
             (2, 4, "Links to every service's dashboards."),
             (3, 3, "Hosting and some people time; ties cost to owners."),
             (2, 4, "One place to find anything about a service.")],
    pitfalls=[("A spreadsheet catalogue", "A central list that one person updates, out of date within weeks.", "keep each entry in its service's repo and check it in CI."),
              ("Twenty required fields on day one", "Teams see paperwork and fill in junk.", "start with owner and on-call; add fields when someone needs them."),
              ("Owners that are people", "The owner left the company a year ago.", "own by team, linked to the org chart and the on-call tool."),
              ("Hand-written dependencies", "The graph says A calls B; traces say A calls B, C and D.", "generate dependencies from tracing or the mesh where you can.")],
    use=["More services than one person can keep in their head (often around 20+).",
         "Several teams sharing on-call or platforms.",
         "Audits asking which systems hold which data."],
    skip=["A handful of services owned by one team: a README is enough.",
          "No one will maintain it or check it.",
          "You need a CMDB for hardware assets: a different job."],
    related=["<b>Incident response &amp; postmortems</b>", "<b>Cost visibility (FinOps)</b>", "<b>Golden paths</b> (Ana, vol. 6)", "<b>Logs, metrics &amp; traces</b>"],
    quiz=[("What four questions should a catalogue answer at 2 a.m.?", "What does it do, who owns it, how do I run or fix it (runbook, dashboards), and what depends on it."),
          ("Why keep the entry in the service's own repository?", "It's reviewed and updated with the code by the owning team, so it doesn't rot in a central list."),
          ("What is a scorecard?", "Automated checks of each service against agreed basics, such as having an owner, a runbook and alerts."),
          ("Why should owners be teams, not people?", "People move on; a team with an on-call rotation stays accountable.")],
    quiz_sit=[("An auditor asks which services store customer addresses, and who owns each. It takes three weeks of emails to answer, and two services turn out to have no owner. What do you set up so the next answer takes minutes?",
               "A catalogue with an entry per service in its repo: owning team, on-call, and data tags such as personal-data, with a CI check that every service has an owner. Then the audit is a search, and orphan services show up on a scorecard instead of in an audit.")],
    try_it="Write a <code>catalog-info.yaml</code> for three services you know, with owner, on-call, links and dependencies. Run Backstage locally (<code>npx @backstage/create-app</code>) and register them, or simply list them in a table. Then try answering “who do I call if this one is down?” and “what breaks if that one stops?” in under a minute.",
    remember="Every service has a <span class=\"hl\">name, an owner and a runbook</span>, and they live <span class=\"hl\">next to the code</span>.",
    sources=["Backstage documentation, “Software Catalog” and “Descriptor Format”.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019), on ownership and platform teams.",
             "Google SRE Book, chapter 32, “The Evolving SRE Engagement Model”.",
             "CNCF Platforms White Paper (2023)."],
)

# ------------------------------------------------------------------ 18 Chaos engineering
ce_problem = Doodle(760, 250, "Doodle of an untested failover. The database has a standby in a second zone, and the architecture diagram says failover is automatic. In the first real zone outage, the standby takes over, but the application's connection strings still point at the old address and its DNS cache holds it for an hour. The failover that existed on paper fails in practice.",
                    "The diagram said “automatic failover”. Nobody had ever pulled the plug.")
ce_problem.box(20, 60, 200, 80, "primary DB", "pink", stroke="red", sub="zone A: down", size=17, subsize=13)
ce_problem.box(280, 60, 200, 80, "standby", "green", sub="zone B: promoted ✓", size=17, subsize=13)
ce_problem.box(540, 60, 200, 80, "app", "pink", stroke="red", sub="still calls zone A", size=17, subsize=13)
ce_problem.arrow(536, 100, 224, 100, color="red", dash=True, curve=(380, -24))
ce_problem.note(380, 186, "DNS cached for 1 hour · connection pool never reconnects", "red", size=16)
ce_problem.note(380, 216, "first test of failover: a real outage", "red", size=16)

ce_analogy = Doodle(760, 250, "Doodle of a vaccine. A small, controlled dose of something harmful, given on purpose, when the body is healthy, so it learns to cope. The dose is measured, the patient is watched, and it's stopped if the reaction is too strong.",
                    "A small, measured dose on purpose, so the body learns before the real thing arrives.")
ce_analogy.box(40, 60, 200, 100, "small dose", "y", sub="measured · on purpose", size=18, subsize=13)
ce_analogy.arrow(244, 110, 316, 110)
ce_analogy.box(320, 60, 200, 100, "watched", "blue", sub="stop if too strong", size=18, subsize=13)
ce_analogy.arrow(524, 110, 576, 110)
ce_analogy.box(580, 60, 166, 100, "immune", "green", sub="before the real one", size=18, subsize=13)

ce_how = Doodle(760, 290, "The chaos experiment loop. Define steady state with a user-facing metric, for example checkout success above 99.5 percent. Form a hypothesis: if one database zone fails, checkout success stays above 99 percent and recovers in under two minutes. Inject the fault in a limited blast radius with an abort condition. Observe, then fix what you learned and run it again, eventually automatically.",
                "Steady state → hypothesis → small, abortable fault → observe → fix → repeat.")
ce_how.row([("steady state", "checkout ≥ 99.5%", "green"), ("hypothesis", "zone fails → ≥ 99%", "y"), ("inject", "small · abortable", "pink"), ("observe", "vs. hypothesis", "blue")], x=20, y=40, h=84, gap=40, size=17, subsize=13, arrows=True)
ce_how.arrow(650, 128, 110, 128, curve=(380, 230), dash=True)
ce_how.note(380, 206, "fix what you learned · run again · then automate it", "pen", size=16)
ce_how.note(380, 266, "abort if the steady-state metric drops below the limit", "red", size=15)

CHAOS_ENGINEERING = dict(
    slug="chaos-engineering",
    kicker="a.k.a. “break it on purpose, before it breaks on its own”",
    tldr="Failover, retries, autoscaling and runbooks are claims until something fails. <b>Chaos engineering</b> tests them with planned <b>experiments on a running system</b>: define a <b>steady state</b> (a user-facing metric), write a <b>hypothesis</b> (“if a zone fails, checkout stays above 99%”), inject the fault in a <b>small, abortable</b> way, and observe. Start in staging and with game days; move to production carefully. Every surprise becomes a fix.",
    chips=[("Family", "resilience"), ("Started at", "Netflix (Chaos Monkey, 2011)"), ("Faults", "kill instances · zone loss · latency · dependency outage · clock skew"), ("Vol. 4 cousin", "fault injection tests inside the test suite")],
    problem="""  <p class="lead">The diagram says the database fails over automatically. In the first real zone outage, the standby is promoted on time, but the application's connection pool never reconnects and its DNS cache holds the old address for an hour. <span class="hl-pink">The failover worked on paper and failed in practice</span>, and its first test was a real outage.</p>
  <ul>
    <li>Resilience mechanisms are <b>rarely exercised</b>, so they rot: configs change, assumptions break.</li>
    <li>Distributed systems fail in <b>combinations</b> no design review imagines.</li>
    <li>On-call people meet each failure for the first time <b>during</b> the incident.</li>
  </ul>""",
    problem_figs=[ce_problem],
    analogy_side="a vaccine",
    analogy="""  <p>A vaccine is a <b>small, measured dose</b> of something harmful, given <b>on purpose</b> while the body is healthy, so it learns to cope before the real thing arrives. The patient is watched, and it's stopped if the reaction is too strong.</p>""",
    analogy_figs=[ce_analogy],
    map=[("The small, measured dose", "A limited fault: one instance, one zone, 1% of traffic"),
         ("Given while healthy", "Run when the system is in steady state, with people ready"),
         ("Watching the patient", "Observing the steady-state metric during the experiment"),
         ("Stopping if the reaction is strong", "Abort conditions that end the experiment automatically"),
         ("Immunity", "Fixes made before a real failure tests them")],
    how_side="the experiment loop",
    how="""  <p>Each experiment is a small scientific test. The <b>steady state</b> is a metric users feel; the <b>hypothesis</b> says it stays within limits during a specific fault; the <b>blast radius</b> is kept small; an <b>abort condition</b> stops the fault automatically if the metric drops too far. A disproved hypothesis is the point: it's a weakness found on your schedule, not the incident's.</p>""",
    how_figs=[ce_how],
    steps=[("Pick a weakness you suspect", "Failover, a slow dependency, losing a zone, a full disk, an expired certificate."),
           ("Define steady state", "A user-facing metric with a normal range: checkout success, search latency."),
           ("Write the hypothesis and limits", "What should happen, how much traffic is in scope, and when to abort."),
           ("Run it, small and watched", "Staging first, then production in a small slice, during working hours, with the owners present (a game day)."),
           ("Fix and repeat", "Turn findings into fixes, re-run to confirm, then schedule it to run automatically.")],
    vocab=[("Chaos engineering", "Experimenting on a system to build confidence it can withstand turbulent conditions."),
           ("Steady state", "The normal range of a metric users care about."),
           ("Hypothesis", "What you expect to stay true during the fault."),
           ("Blast radius", "How much of the system and its users the experiment can affect."),
           ("Abort condition", "The rule that stops the experiment automatically."),
           ("Game day", "A planned session where a team runs failure experiments together.")],
    code=dict(file="zone-failure.yaml", note="Chaos Mesh (Kubernetes)", src="""
# hypothesis: if orders loses its pods in zone b, checkout success stays >= 99% and recovers within 2 min
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata: { name: orders-zone-b-loss, namespace: chaos }
spec:
  action: pod-kill
  mode: all
  selector:
    namespaces: [shop]
    labelSelectors: { app: orders }
    nodeSelectors: { topology.kubernetes.io/zone: eu-west-1b }
  duration: "10m"
---
# abort: stop the experiment if checkout success drops below 98.5% (alert wired to delete the PodChaos)
# run in staging first; in production, during a game day, with the orders team watching
"""),
    tools="tools: Chaos Mesh and LitmusChaos (Kubernetes), AWS Fault Injection Service, Azure Chaos Studio, Gremlin, Chaos Toolkit, Toxiproxy for network faults, Steadybit.",
    gains=["<b>Failover and recovery are proven</b>, not assumed.",
           "<b>Weaknesses found on your schedule</b>, during working hours.",
           "<b>Practised on-call</b>: the team has seen the failure before.",
           "<b>Better runbooks and alerts</b> from every experiment."],
    losses=["<b>Real risk</b> if the blast radius or abort is wrong.",
            "<b>Needs good observability</b> first, or you can't see the result.",
            "<b>Time</b>: planning, game days, follow-up work.",
            "<b>Trust to earn</b> with the business before production experiments."],
    baseline="Each line compares <b>resilience that exists only on diagrams</b> to <b>regular, controlled experiments against it</b>.",
    ratings=[(3, 3, "Neutral: experiments are planned, small and documented."),
             (3, 3, "Neutral."),
             (3, 4, "Rollback and recovery paths are known to work."),
             (2, 4, "Weaknesses are fixed before real failures find them."),
             (3, 3, "Neutral."),
             (2, 5, "Failover and restore are practised."),
             (2, 4, "Experiments expose missing alerts and dashboards."),
             (3, 3, "Tool and people time, fewer long outages."),
             (3, 3, "Neutral.")],
    pitfalls=[("Chaos without a hypothesis", "Killing random things and watching what happens teaches little and scares everyone.", "one suspected weakness, a written hypothesis and a steady-state metric per experiment."),
              ("No abort condition", "An experiment keeps running while customers suffer.", "an automatic stop tied to the steady-state metric, and a person ready to stop it."),
              ("Starting in production", "The first experiment ever takes down checkout.", "staging and game days first; production with a tiny blast radius once trust is earned."),
              ("Findings without fixes", "The same weakness shows up in every game day.", "track findings as tickets with owners, and re-run the experiment to confirm the fix.")],
    use=["Systems with failover, redundancy or autoscaling you rely on.",
         "Before peak events (sales, launches) to test the plan.",
         "Teams with good monitoring and an on-call rotation."],
    skip=["No observability yet: you won't be able to tell what happened.",
          "Known weaknesses already waiting to be fixed: fix them first.",
          "A system that can't take any risk and has no staging copy (build one first)."],
    related=["<b>Fault injection tests</b> (Vol. 4)", "<b>Backups &amp; disaster recovery</b>", "<b>Incident response &amp; postmortems</b>", "<b>Circuit breaker</b> (Vol. 1)"],
    quiz=[("What are the parts of a chaos experiment?", "A steady-state metric, a hypothesis, a fault with a limited blast radius, an abort condition, and observation of the result."),
          ("Why define steady state with a user-facing metric?", "It measures what matters (users succeeding), not whether a single server is up."),
          ("Why start in staging and with game days?", "To learn safely and build trust before running small, controlled experiments in production."),
          ("How is chaos engineering different from fault injection tests?", "Chaos experiments run against a whole running system and its operations; fault injection tests run inside the test suite against code.")],
    quiz_sit=[("Leadership wants to “turn on Chaos Monkey in production” next week. There's no steady-state metric for checkout, and alerts are mostly on CPU. What do you propose instead?",
               "First define steady-state SLIs (checkout success, latency) with alerts on them. Then run a game day in staging with one hypothesis (an instance or zone loss), fix what it finds, and only then run small, abortable experiments in production during working hours.")],
    try_it="Pick one resilience claim in your system (“if one instance dies, users don't notice”). Write it as a hypothesis with a steady-state metric, then test it in staging: delete one pod or stop one instance while a load generator runs, and watch the metric. Write down what happened, what surprised you, and one fix.",
    remember="A <span class=\"hl\">small dose, on purpose</span>, with a <span class=\"hl\">hand on the stop button</span>.",
    sources=["Principles of Chaos Engineering (principlesofchaos.org).",
             "Casey Rosenthal and Nora Jones, <i>Chaos Engineering</i> (O'Reilly, 2020).",
             "Ali Basiri et al., “Chaos Engineering”, <i>IEEE Software</i> (2016).",
             "AWS Well-Architected Reliability Pillar, “Test reliability using fault injection”."],
)

NOTES = [PROGRESSIVE_DELIVERY, SERVICE_CATALOGUE, CHAOS_ENGINEERING]
