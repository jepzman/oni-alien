# Vol. 6 · Resilience & cost: Backups & DR, Incident Response & Postmortems, Cost Visibility (FinOps).

# ------------------------------------------------------------------ 13 Backups & Disaster Recovery
dr_problem = Doodle(760, 250, "Doodle of a ransomware or deleted-account incident. The team discovers that backups exist but were stored in the same account, so they were deleted too. An older backup in another place has never been restored, and the restore takes three days instead of the hour everyone assumed.",
                    "Backups in the same account (gone too), and the other one never tested: 3 days to restore, not 1 hour.")
dr_problem.raw('<rect class="d d-dash d-red" x="20" y="30" width="330" height="150" rx="8" style="fill:none"/>')
dr_problem.db(110, 70, "prod DB", w=90)
dr_problem.db(260, 70, "backups", w=90)
dr_problem.raw('<path class="d d-red" d="M60 60 L320 160 M320 60 L60 160"/>')
dr_problem.note(185, 210, "same account → both deleted", "red")
dr_problem.note(570, 70, "other backup:", "pen")
dr_problem.note(570, 100, "never restored", "red")
dr_problem.note(570, 150, "assumed: 1 hour", "pen")
dr_problem.note(570, 180, "actual: 3 days", "red")

dr_analogy = Doodle(760, 250, "Doodle of a fire drill and a spare house key. Families keep a spare key with a trusted neighbour, not under the mat, and practise the fire drill twice a year so everyone knows the meeting point. The plan only counts if it has been practised.",
                    "A spare key at a neighbour's, and a fire drill you've actually practised.")
dr_analogy.icon("key", 40, 60, 1.4, fill="y")
dr_analogy.note(90, 150, "spare key next door", "green")
dr_analogy.note(90, 176, "(not under the mat)", "pen")
dr_analogy.icon("bell", 360, 50, 1.4, fill="pink")
dr_analogy.note(400, 160, "fire drill twice a year", "green")
dr_analogy.note(640, 100, "meeting point:", "pen")
dr_analogy.note(640, 126, "the oak tree", "pen")

dr_how = Doodle(760, 300, "Disaster recovery plan. Set targets: recovery point objective, how much data you can lose, for example five minutes, and recovery time objective, how long to restore, for example one hour. Follow 3-2-1: three copies, two kinds of storage, one off-site in a separate account and region, immutable so it can't be deleted. Infrastructure as code rebuilds the platform. Restore drills every quarter prove the times.",
                "Set RPO and RTO; keep 3-2-1 immutable backups in another account and region; rebuild with IaC; drill restores.")
dr_how.box(20, 30, 200, 70, "RPO: 5 min", "y", sub="data you may lose")
dr_how.box(20, 120, 200, 70, "RTO: 1 hour", "y", sub="time to recover")
dr_how.box(260, 30, 260, 160, None, "green")
dr_how.head(390, 60, "3-2-1 backups", size=18)
for i, t in enumerate(["3 copies", "2 storage types", "1 other account + region", "immutable (locked)"]):
    dr_how.text(276, 92 + i * 24, t, "t", anchor="start", size=15)
dr_how.box(560, 30, 180, 70, "IaC rebuild", "blue", size=17)
dr_how.box(560, 120, 180, 70, "restore drill", "pink", sub="every quarter")
dr_how.note(380, 250, "a backup you haven't restored is a hope, not a backup", "red")

DISASTER = dict(
    slug="disaster-recovery",
    kicker="a.k.a. “the spare key and the fire drill”",
    tldr="Decide how much data you can afford to lose (<b>RPO</b>) and how fast you must be back (<b>RTO</b>), then design for it: <b>3-2-1 backups</b> with at least one <b>immutable copy in a separate account and region</b>, <b>infrastructure as code</b> to rebuild the platform, and <b>regular restore drills</b> that prove you can hit the targets. An untested backup is a hope, not a plan.",
    chips=[("Family", "resilience"), ("Targets", "RPO (data loss), RTO (downtime)"), ("Strategies", "backup/restore, pilot light, warm standby, active–active"), ("Pairs with", "IaC, replication (Vol. 1), postmortems")],
    problem="""  <p class="lead">Most teams have backups. Far fewer have backups that <span class="hl-pink">survive the disaster</span> and that they have <span class="hl-pink">actually restored</span>. Ransomware, a deleted account or a bad migration reveals the difference.</p>
  <ul>
    <li>Backups in the same account are deleted along with production.</li>
    <li>Nobody knows how long a full restore takes.</li>
    <li>The database is restored, but the infrastructure around it isn't.</li>
  </ul>""",
    problem_figs=[dr_problem],
    analogy_side="the spare key and the fire drill",
    analogy="""  <p>Sensible families keep a <b>spare key with a trusted neighbour</b>, not under the doormat, and practise a <b>fire drill</b> so everyone knows the way out and the meeting point. A plan that's never been practised fails at the worst moment.</p>
  <ul>
    <li>The spare key next door is an <b>off-site, separate-account backup</b>.</li>
    <li>The drill is a <b>restore test</b>.</li>
    <li>The meeting point is your <b>runbook</b>.</li>
  </ul>""",
    analogy_figs=[dr_analogy],
    map=[("Spare key at the neighbour's", "Backup in another account and region"),
         ("Not under the doormat", "Not in the same account as production"),
         ("The fire drill", "Scheduled restore tests"),
         ("The meeting point", "A written, rehearsed DR runbook"),
         ("“Out in 2 minutes”", "RTO measured in drills, not assumed")],
    how_side="targets, copies, rebuild, rehearse",
    how="""  <p>Choose a strategy per system based on RPO/RTO and cost: <b>backup &amp; restore</b> (hours), <b>pilot light</b> or <b>warm standby</b> (minutes), <b>active–active</b> (seconds, expensive).</p>""",
    how_figs=[dr_how],
    steps=[("Set RPO and RTO per system", "With the business: what does an hour of downtime or data loss cost?"),
           ("Follow 3-2-1", "Three copies, two media, one off-site; plus immutability (object lock)."),
           ("Separate the blast radius", "Backups in a different account with separate credentials and region."),
           ("Back up the platform too", "Infrastructure as code, secrets, DNS and configuration."),
           ("Drill restores", "Quarterly: restore to a clean environment, time it, fix what's slow."),
           ("Write the runbook", "Who decides, who does what, in which order, how to communicate.")],
    vocab=[("RPO", "Recovery point objective: maximum acceptable data loss."),
           ("RTO", "Recovery time objective: maximum acceptable downtime."),
           ("3-2-1 rule", "3 copies, 2 media, 1 off-site."),
           ("Immutable backup", "Can't be modified or deleted for a set period."),
           ("Pilot light / warm standby", "Minimal or scaled-down copy of production ready elsewhere."),
           ("Point-in-time recovery", "Restoring a database to a specific moment.")],
    code=dict(file="backups.tf", note="AWS Backup, cross-account vault lock", src="""
resource "aws_backup_plan" "prod" {
  name = "prod-daily"
  rule {
    rule_name         = "daily-35d"
    target_vault_name = aws_backup_vault.local.name
    schedule          = "cron(0 3 * * ? *)"
    lifecycle { delete_after = 35 }
    copy_action {                                   # copy to the isolated DR account/region
      destination_vault_arn = "arn:aws:backup:eu-central-1:999999999999:backup-vault:dr"
      lifecycle { delete_after = 90 }
    }
  }
}

# in the DR account: vault lock = nobody (not even admins) can delete early
resource "aws_backup_vault_lock_configuration" "dr" {
  backup_vault_name  = "dr"
  min_retention_days = 30
}
# + continuous PITR on the database (RPO ≈ 5 min) + quarterly restore drill
"""),
    tools="tools: AWS Backup (vault lock, cross-account copy), Azure Backup immutable vaults, GCP Backup and DR, database point-in-time recovery, Velero for Kubernetes, restic / Kopia, object lock / WORM storage, IaC for the platform.",
    gains=["<b>Survive the worst day</b>: deletion, ransomware, region loss.",
           "<b>Known recovery times</b>, proven by drills.",
           "<b>Clear expectations</b> with the business.",
           "<b>Calmer incidents</b>: there's a plan."],
    losses=["<b>Storage and standby costs</b>.",
            "<b>Drills take time</b> and planning.",
            "<b>Complexity</b> for warm standby and active–active.",
            "<b>Immutability</b> makes deleting data on request harder."],
    baseline="Each line compares <b>untested backups in the production account</b> to <b>RPO/RTO targets, immutable cross-account backups, IaC rebuilds and quarterly restore drills</b>.",
    ratings=[(3, 3, "More pieces, but one written plan."),
             (3, 3, "Neutral."),
             (3, 4, "Bad migrations can be undone with PITR."),
             (3, 4, "Disasters become recoverable incidents."),
             (3, 3, "Neutral."),
             (1, 5, "Recovery is designed, measured and rehearsed."),
             (2, 4, "Backup jobs and drills are monitored."),
             (4, 2, "Extra storage, copies and drill time."),
             (3, 3, "Runbooks and drills take effort.")],
    pitfalls=[("Backups in the same account", "Ransomware or a deleted account takes them too.", "separate account, credentials and region; vault lock."),
              ("Never testing restores", "The backup is corrupt or takes days.", "quarterly restore drills with timing."),
              ("Only backing up data", "Data restored, but no infrastructure to run it.", "IaC for the platform; back up config and secrets."),
              ("No owner for the decision", "During the disaster nobody knows who calls failover.", "runbook with roles and decision points.")],
    use=["Every production data store.",
         "Systems with business or legal recovery requirements.",
         "Anything ransomware could reach."],
    skip=["Truly disposable data (caches, rebuildable indexes): document that instead."],
    related=["<b>Infrastructure as code</b>", "<b>Incident response &amp; postmortems</b>", "<b>Leader–follower replication</b> (Vol. 1)", "<b>Envelope encryption</b> (Vol. 5)"],
    quiz=[("What's the difference between RPO and RTO?", "RPO is how much data you can lose; RTO is how long you can be down."),
          ("What is the 3-2-1 rule?", "Three copies of data, on two kinds of storage, with one off-site."),
          ("Why keep backups in a separate account?", "So an attacker or mistake in production can't delete them too."),
          ("Why run restore drills?", "To prove backups work and to measure real recovery time.")],
    remember="Spare key at the <span class=\"hl\">neighbour's</span>, and practise the <span class=\"hl\">fire drill</span>.",
    sources=["AWS whitepaper, “Disaster Recovery of Workloads on AWS”.",
             "Google Cloud, “Disaster recovery planning guide”.",
             "NIST SP 800-34, “Contingency Planning Guide for Federal Information Systems”.",
             "CISA, “Ransomware Guide” (backups section)."],
)

# ------------------------------------------------------------------ 14 Incident Response & Postmortems
ir_problem = Doodle(760, 250, "Doodle of a chaotic incident channel. Twenty people are posting theories at once, two engineers restart the same service at the same time, nobody is talking to customers, and afterwards the review is about finding who pushed the bad change, so people hide details next time.",
                    "Twenty people, no roles, nobody updating customers, and a blame hunt afterwards.")
for i in range(8):
    ir_problem.circle(40 + (i % 4) * 50, 60 + (i // 4) * 60, 16, "paper")
ir_problem.note(110, 200, "20 people, 20 theories", "red")
ir_problem.note(470, 60, "two restarts at once", "red")
ir_problem.note(470, 100, "customers: silence", "red")
ir_problem.note(470, 150, "afterwards: “who did it?”", "red")
ir_problem.note(470, 180, "→ details hidden next time", "red")

ir_analogy = Doodle(760, 250, "Doodle of an air crash investigation and a cockpit. In the cockpit, the captain flies and the first officer handles the radio and checklists, with clear roles. Afterwards, investigators look for how the system allowed the error, not who to punish, and publish lessons so every airline improves.",
                    "In the cockpit: clear roles and checklists. Afterwards: find how the system allowed it, not who to blame.")
ir_analogy.box(40, 50, 200, 120, None, "blue", rx=10)
ir_analogy.note(140, 90, "captain: flies", "pen")
ir_analogy.note(140, 120, "first officer: radio,", "pen")
ir_analogy.note(140, 146, "checklists", "pen")
ir_analogy.arrow(250, 110, 370, 110, label="afterwards", lx=310, ly=96)
ir_analogy.icon("magnifier", 380, 70, 1.2)
ir_analogy.note(600, 90, "how did the system", "green")
ir_analogy.note(600, 116, "allow it?", "green")
ir_analogy.note(600, 170, "lessons shared with all", "green")

ir_how = Doodle(760, 300, "Incident lifecycle. Detect through an SLO burn alert. Declare an incident with a severity. Assign roles: an incident commander who coordinates, operations people who investigate and fix, and a communications lead who updates the status page. Mitigate first, for example roll back, then fix. Afterwards, hold a blameless postmortem with a timeline, contributing factors and action items with owners, and share it.",
                "Detect → declare → roles → mitigate first → resolve → blameless postmortem with owned actions.")
steps_ir = [("detect", "SLO burn alert", "y"), ("declare", "SEV-2", "pink"), ("mitigate", "roll back first", "green"), ("resolve", "root fix", "blue"), ("learn", "postmortem", "y")]
for i, (t, sub, f) in enumerate(steps_ir):
    ir_how.box(10 + i * 150, 30, 136, 76, t, f, sub=sub, size=18, subsize=14)
    if i:
        ir_how.arrow(10 + i * 150 - 12, 68, 10 + i * 150 - 2, 68)
for i, (t, sub) in enumerate([("commander", "coordinates"), ("ops", "investigates, fixes"), ("comms", "status page, customers")]):
    ir_how.box(40 + i * 240, 160, 210, 70, t, "paper", sub=sub, size=18)
ir_how.note(380, 270, "roles, not rank · blameless · actions have owners", "pen")

INCIDENTS = dict(
    slug="postmortems",
    kicker="a.k.a. “the cockpit and the crash investigation”",
    tldr="Treat incidents as a practised routine: <b>declare</b> them early with a <b>severity</b>, assign <b>clear roles</b> (incident commander, operations, communications), <b>mitigate first</b> (roll back, fail over) and diagnose after. Then run a <b>blameless postmortem</b>: a timeline, the <b>contributing factors in the system</b>, and <b>action items with owners</b>, shared widely so everyone learns.",
    chips=[("Family", "operations culture"), ("Roles", "incident commander, ops, comms, scribe"), ("Influences", "aviation, fire services (ICS), Google SRE"), ("Pairs with", "SLOs, observability, disaster recovery")],
    problem="""  <p class="lead">Without a routine, incidents become <span class="hl-pink">chaos</span>: everyone debugging at once, nobody coordinating or updating customers. And if the review hunts for <span class="hl-pink">who to blame</span>, people hide details and the same failure returns.</p>
  <ul>
    <li>Two engineers make conflicting fixes at the same time.</li>
    <li>Customers learn about the outage from social media.</li>
    <li>The “root cause” is “human error”, and nothing changes.</li>
  </ul>""",
    problem_figs=[ir_problem],
    analogy_side="the cockpit and the crash investigation",
    analogy="""  <p>In a cockpit, the <b>captain flies</b> and the <b>first officer handles the radio and checklists</b>: clear roles, especially in an emergency. Afterwards, air-crash investigators ask <b>how the system allowed</b> the error, not who to punish, and <b>publish lessons</b> so every airline gets safer.</p>
  <ul>
    <li>Captain = <b>incident commander</b>; radio = <b>comms lead</b>.</li>
    <li>Checklists = <b>runbooks</b>.</li>
    <li>The investigation = a <b>blameless postmortem</b>.</li>
  </ul>""",
    analogy_figs=[ir_analogy],
    map=[("Captain flies the plane", "Incident commander coordinates (doesn't debug)"),
         ("First officer on the radio", "Comms lead updates status page and stakeholders"),
         ("Emergency checklists", "Runbooks and rollback procedures"),
         ("Land first, investigate later", "Mitigate first, then root-cause"),
         ("Investigators publish lessons", "Blameless postmortem, shared widely")],
    how_side="practised roles, then learning",
    how="""  <p>“Human error” is where an investigation <b>starts</b>, not where it ends: what made the mistake easy, and the damage large?</p>""",
    how_figs=[ir_how],
    steps=[("Define severities", "SEV-1 to SEV-4 with examples and who to page."),
           ("Declare early", "Anyone can declare; downgrading is cheap, late declaring is expensive."),
           ("Assign roles", "Commander (coordinates, decides), ops (hands on keyboard), comms (updates every 30 min), scribe."),
           ("Mitigate before diagnosing", "Roll back, fail over, turn off the flag; find root causes afterwards."),
           ("Write a blameless postmortem", "Timeline, impact, contributing factors, what went well, action items with owners and dates."),
           ("Close the loop", "Track action items; share postmortems; practise with game days.")],
    vocab=[("Incident commander", "Coordinates the response and makes decisions."),
           ("Severity (SEV)", "How bad an incident is, which sets the response."),
           ("Mitigation", "Stopping the impact, even before fixing the cause."),
           ("Blameless postmortem", "Review focused on systems, not individuals."),
           ("Contributing factors", "The conditions that together allowed the incident."),
           ("Game day", "A planned exercise simulating an incident.")],
    code=dict(file="postmortems/2026-11-12-checkout-errors.md", note="template", src="""
# Checkout 5xx spike · SEV-2 · 2026-11-12 · 41 min
Commander: ana · Ops: ben, cho · Comms: dee · Status: resolved

## Impact
6% of checkouts failed (≈ 1,900 orders retried, 140 lost). Error budget: 38% used.

## Timeline (UTC)
09:02 deploy web@9c1e (new payment client)   09:07 burn-rate page
09:09 SEV-2 declared                          09:14 rolled back to web@4a7b
09:43 error rate normal, monitoring           09:50 resolved

## Contributing factors
- Payment client default timeout changed from 10 s to 2 s
- Canary step was skipped for “small” changes
- No alert on payment-provider latency

## Action items
- [ ] Pin client timeouts in config (ben, 11-19)
- [ ] Canary required for every prod deploy (cho, 11-26)
- [ ] Latency SLI for payment provider (dee, 12-03)
"""),
    tools="tools: PagerDuty / Opsgenie / incident.io / Rootly / FireHydrant, Statuspage / Instatus, Slack incident channels, Jeli for incident analysis, runbooks in the repo, game days and chaos tools.",
    gains=["<b>Faster mitigation</b> with clear roles.",
           "<b>Customers kept informed</b>.",
           "<b>Real learning</b>: systemic fixes, not blame.",
           "<b>Less fear</b>, so people share what really happened."],
    losses=["<b>Process overhead</b> for small incidents.",
            "<b>Time for postmortems</b> and follow-ups.",
            "<b>Action items pile up</b> if not prioritised.",
            "<b>Blameless is hard</b> to keep under pressure."],
    baseline="Each line compares <b>ad-hoc firefighting and blame-focused reviews</b> to <b>declared incidents with roles and blameless postmortems</b>.",
    ratings=[(3, 3, "A routine to learn, then it's automatic."),
             (3, 3, "Neutral."),
             (3, 4, "Lessons (like “canary always”) make deploys safer."),
             (2, 4, "Repeat incidents become rarer."),
             (3, 3, "Neutral."),
             (2, 5, "Mitigate-first and roles cut downtime."),
             (2, 4, "Timelines expose missing signals."),
             (3, 3, "Meeting time vs repeated outages."),
             (2, 4, "Calmer on-call; less blame.")],
    pitfalls=[("Commander also debugging", "Nobody coordinates; work overlaps.", "the commander coordinates; others fix."),
              ("Diagnosing before mitigating", "An hour of root-causing while users suffer.", "roll back or fail over first."),
              ("“Root cause: human error”", "Nothing changes; it happens again.", "ask what made the error possible and costly."),
              ("Action items never done", "The same postmortem every quarter.", "owners, dates and tracking; review them.")],
    use=["Every team that runs production services.",
         "Customer-facing outages and security incidents.",
         "Near-misses worth learning from."],
    skip=["Use a lighter version for tiny blips; keep the habit, not the paperwork."],
    related=["<b>SLOs &amp; error budgets</b>", "<b>Backups &amp; disaster recovery</b>", "<b>Feature flags</b>", "<b>Audit logging</b> (Vol. 5)"],
    quiz=[("What does the incident commander do?", "Coordinates the response, assigns work and makes decisions, rather than debugging."),
          ("Why mitigate before finding the root cause?", "Users are affected now; rollback or failover stops the impact quickly."),
          ("What makes a postmortem blameless?", "It examines how the system allowed the failure, not who to punish, so people share details honestly."),
          ("What turns a postmortem into improvement?", "Action items with owners and dates that are tracked to completion.")],
    remember="<span class=\"hl\">Fly the plane</span> first, keep the <span class=\"hl\">radio</span> going, and investigate the <span class=\"hl\">system</span>, not the pilot.",
    sources=["Google SRE Book, ch. 14 “Managing Incidents” and ch. 15 “Postmortem Culture”.",
             "PagerDuty, “Incident Response Documentation” (response.pagerduty.com).",
             "John Allspaw, “Blameless PostMortems and a Just Culture” (Etsy, 2012).",
             "Sidney Dekker, <i>The Field Guide to Understanding Human Error</i>."],
)

# ------------------------------------------------------------------ 15 Cost Visibility (FinOps)
fo_problem = Doodle(760, 250, "Doodle of a monthly cloud bill that jumped from forty thousand to ninety thousand euros. Finance asks why. Nobody knows which team, service or environment caused it, because resources aren't tagged. Later they find forgotten GPU instances from a demo and preview environments that never shut down.",
                    "The bill doubled. Which team? Which service? Nobody knows: nothing is tagged.")
fo_problem.raw('<path class="d d-pen" d="M40 200 L140 190 L240 185 L340 170 L440 60"/>')
fo_problem.note(140, 220, "€40k", "pen")
fo_problem.note(440, 46, "€90k ?!", "red")
fo_problem.note(620, 100, "untagged: 70%", "red")
fo_problem.note(620, 140, "demo GPUs still on", "red")
fo_problem.note(620, 180, "previews never deleted", "red")

fo_analogy = Doodle(760, 250, "Doodle of a shared flat's electricity bill. Before smart plugs, flatmates argued about one big bill. With a meter per room, everyone sees their own usage, the person with the space heater turns it down, and the flat agrees a monthly budget.",
                    "A meter per room: everyone sees their own usage, and the space heater gets turned down.")
fo_analogy.icon("store", 40, 60, 1.6)
for i, (t, v, f) in enumerate([("Ana", "€18", "green"), ("Ben", "€22", "green"), ("Cho", "€71 · heater!", "pink")]):
    fo_analogy.box(260 + i * 160, 70, 140, 70, t, f, sub=v, size=16)
fo_analogy.note(500, 200, "seen → owned → reduced", "green")

fo_how = Doodle(760, 290, "FinOps loop. Inform: every resource is tagged with team, service and environment, enforced by policy; costs are shown per team in a dashboard with unit costs like cost per thousand orders. Optimise: rightsize, schedule non-production off at night, use savings plans and spot for flexible work, delete idle resources. Operate: budgets and anomaly alerts per team, and cost reviewed in design decisions.",
                "Inform (tags, dashboards, unit cost) → optimise (rightsize, schedule, commit) → operate (budgets, alerts, design reviews).")
for i, (t, sub, f) in enumerate([("inform", "tags · €/team · €/order", "y"), ("optimise", "rightsize · nights off · spot", "green"), ("operate", "budgets · anomaly alerts", "blue")]):
    fo_how.box(20 + i * 250, 50, 220, 100, t, f, sub=sub, size=20, subsize=14)
fo_how.arrow(240, 100, 266, 100)
fo_how.arrow(490, 100, 516, 100)
fo_how.arrow(620, 156, 140, 156, dash=True, curve=(380, 250), label="repeat monthly", lx=380, ly=230)

FINOPS = dict(
    slug="finops",
    kicker="a.k.a. “a meter per room”",
    tldr="Make cloud cost <b>visible, owned and part of design</b>. <b>Tag</b> every resource with team, service and environment (and enforce it), show <b>cost per team</b> and <b>per unit</b> (€ per 1,000 orders), then <b>optimise</b>: rightsize, switch non-production off at night, commit to discounts for steady load, delete idle things. <b>Budgets and anomaly alerts</b> catch surprises in days, not at month end.",
    chips=[("Family", "cost management"), ("Phases", "inform → optimise → operate (FinOps Foundation)"), ("Tools", "cloud cost explorers, Kubecost/OpenCost, Infracost"), ("Pairs with", "IaC, autoscaling, preview environments")],
    problem="""  <p class="lead">Cloud makes it easy to spend and hard to see. Without tags and owners, the bill is <span class="hl-pink">one big number</span> that only finance looks at, and only after the month ends.</p>
  <ul>
    <li>The bill doubles and nobody knows which service caused it.</li>
    <li>Forgotten demo GPUs and preview environments run for months.</li>
    <li>Engineers never see the cost of their design choices.</li>
  </ul>""",
    problem_figs=[fo_problem],
    analogy_side="a meter per room",
    analogy="""  <p>In a shared flat, one big electricity bill leads to arguments. Put a <b>meter in each room</b> and everyone sees their own usage: the person running a <b>space heater all day</b> turns it down, and the flat agrees a <b>monthly budget</b>.</p>
  <ul>
    <li>Meters per room are <b>tags and per-team dashboards</b>.</li>
    <li>Turning down the heater is <b>optimisation</b>.</li>
    <li>The agreed budget is <b>budgets and alerts</b>.</li>
  </ul>""",
    analogy_figs=[fo_analogy],
    map=[("A meter in each room", "Tags: team, service, environment"),
         ("Everyone sees their own usage", "Cost dashboards per team and service"),
         ("Cost per hot shower", "Unit cost: € per 1,000 orders / per tenant"),
         ("Heater off when you're out", "Non-production scheduled off at night"),
         ("Agreed monthly budget", "Budgets and anomaly alerts")],
    how_side="inform, optimise, operate",
    how="""  <p>FinOps is a <b>culture</b> as much as a tool: engineers see the cost of their choices, finance understands the trade-offs, and both decide together.</p>""",
    how_figs=[fo_how],
    steps=[("Tag everything", "team, service, env, cost_center; enforced in IaC and with policies."),
           ("Show cost to owners", "Per-team dashboards and weekly reports; Kubecost/OpenCost for clusters."),
           ("Track unit cost", "€ per 1,000 requests, per order, per tenant: does cost grow with value?"),
           ("Optimise the big items", "Rightsize, delete idle resources, schedule non-prod off, storage lifecycle rules."),
           ("Commit where steady", "Savings plans / reservations for base load; spot for interruptible work."),
           ("Alert and review", "Budgets, anomaly detection, and a cost estimate (Infracost) in infrastructure PRs.")],
    vocab=[("FinOps", "Practice of managing cloud cost collaboratively."),
           ("Cost allocation", "Assigning costs to teams and services."),
           ("Unit economics", "Cost per unit of business value."),
           ("Rightsizing", "Matching resource size to actual use."),
           ("Savings plan / reservation", "Discount for committing to steady usage."),
           ("Spot / preemptible", "Cheap, interruptible capacity.")],
    code=dict(file="tags.tf + infracost comment", note="enforce tags, see cost in PRs", src="""
provider "aws" {
  region = "eu-west-1"
  default_tags {
    tags = { team = "storefront", service = "web", env = "prod", cost_center = "cc-114" }
  }
}

# non-prod: off outside working hours
resource "aws_autoscaling_schedule" "staging_night" {
  autoscaling_group_name = module.web_staging.asg_name
  scheduled_action_name  = "night-off"
  recurrence             = "0 20 * * MON-FRI"
  min_size               = 0
  max_size               = 0
  desired_capacity       = 0
}

# PR comment from Infracost:
#   Monthly cost will increase by €1,240 (+9%)
#   + aws_db_instance.search   db.r6g.2xlarge   €1,240
"""),
    tools="tools: AWS Cost Explorer / CUR, Azure Cost Management, GCP Billing export + Looker Studio, Kubecost / OpenCost, Infracost, Vantage, CloudZero, tag policies (AWS Organizations, Azure Policy), budgets and anomaly detection.",
    gains=["<b>Know who spends what</b>, and why.",
           "<b>Surprises caught in days</b>, not at month end.",
           "<b>Real savings</b> from rightsizing and scheduling.",
           "<b>Cost-aware design</b> decisions."],
    losses=["<b>Tagging discipline</b> and enforcement effort.",
            "<b>Commitments</b> can lock you in.",
            "<b>Over-optimising</b> can hurt reliability.",
            "<b>Shared costs</b> are hard to split fairly."],
    baseline="Each line compares <b>one untagged monthly bill reviewed by finance</b> to <b>tagged, team-owned costs with unit metrics, budgets and PR cost estimates</b>.",
    ratings=[(3, 3, "Tags and dashboards to maintain."),
             (3, 3, "Neutral; cost shows up in PRs."),
             (3, 3, "Neutral."),
             (3, 3, "Careful: don't cut redundancy to save money."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Cost becomes another observable signal."),
             (1, 5, "Typically 20–30% saved on the first pass."),
             (3, 4, "Engineers see the impact of their choices.")],
    pitfalls=[("Tags as a suggestion", "Half the resources untagged after a month.", "enforce tags in IaC and with policies."),
              ("Cutting redundancy to save money", "Single-AZ database; the next outage costs more.", "optimise waste first, not resilience."),
              ("Big commitments too early", "Three-year reservation for a service you're about to retire.", "commit only to steady, long-lived base load."),
              ("Only finance looks at cost", "Engineers never see it.", "per-team dashboards and PR estimates.")],
    use=["Any organisation with a meaningful cloud bill.",
         "Multi-team platforms and Kubernetes clusters.",
         "SaaS products that need healthy unit economics."],
    skip=["Tiny fixed-price hosting where there's nothing to optimise."],
    related=["<b>Autoscaling</b>", "<b>Preview environments</b>", "<b>Infrastructure as code</b>", "<b>Multitenancy</b> (Vol. 3)"],
    quiz=[("What are the three FinOps phases?", "Inform (visibility and allocation), optimise (reduce waste and rates), operate (continuous governance)."),
          ("Why track unit cost?", "To see whether spending grows in line with business value, not just whether the bill goes up."),
          ("What should you optimise first?", "Waste: idle and oversized resources and non-production running 24/7, not redundancy."),
          ("How do tags help?", "They let costs be allocated to teams, services and environments, so owners can see and act on them.")],
    remember="Put a <span class=\"hl\">meter</span> in every room, and turn off the <span class=\"hl\">heater</span> when nobody's home.",
    sources=["FinOps Foundation, “FinOps Framework” (finops.org).",
             "J.R. Storment &amp; Mike Fuller, <i>Cloud FinOps</i> (2nd ed., O'Reilly).",
             "AWS Well-Architected, “Cost Optimization Pillar”.",
             "OpenCost documentation (CNCF)."],
)

NOTES = [DISASTER, INCIDENTS, FINOPS]
