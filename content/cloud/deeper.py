# Vol. 6 · going deeper (November 2026): a longer chapter inside four key notes.
# Blue–green, canary and feature flags already have a full deep dive (Zero-Downtime Change), so they get none here.
# Merged into the notes by scripts/build_notes.py (load_content).

# ------------------------------------------------------------------ Infrastructure as code
iac_d1 = Doodle(760, 310, "Infrastructure split into layers with separate state files. The foundation layer holds the network and DNS and changes a few times a year. The data layer holds databases and buckets and changes monthly. The apps layer holds services and queues and changes daily. Each layer reads the outputs of the layer below it. A mistake in an app change can only touch the apps layer.",
                "Separate state per layer: a daily change can't delete a yearly one.")
for i, (name, sub, fill, often) in enumerate([("apps", "services · queues · alarms", "green", "daily"),
                                               ("data", "databases · buckets · backups", "y", "monthly"),
                                               ("foundation", "network · DNS · IAM baseline", "blue", "yearly")]):
    y = 20 + i * 92
    iac_d1.box(140, y, 380, 62, name, fill, sub=sub, size=18, subsize=14)
    iac_d1.note(580, y + 38, f"changes {often}", anchor="start", size=16)
    iac_d1.note(100, y + 38, "state", anchor="end", size=15)
    if i < 2:
        iac_d1.arrow(330, y + 90, 330, y + 66)
        iac_d1.note(342, y + 84, "outputs", anchor="start", size=14)
iac_d1.note(380, 300, "one state file per layer and per environment", "pen", size=17)

iac_d2 = Doodle(760, 230, "Renaming a resource safely. Moving a database resource into a module changes its address from aws_db_instance.main to module.db.aws_db_instance.this. Without a moved block, the plan says destroy the old database and create a new, empty one. With a moved block from the old address to the new one, the plan says the resource moved and nothing is destroyed.",
                "Same database, new address: tell the tool it moved, or it will rebuild it empty.")
iac_d2.box(20, 30, 330, 70, "without “moved”", "pink", stroke="red", sub="- destroy main · + create this (empty!)", size=17, subsize=14)
iac_d2.box(410, 30, 330, 70, "with “moved”", "green", sub="~ main has moved to module.db…this", size=17, subsize=14)
iac_d2.note(380, 150, "moved { from = aws_db_instance.main", "pen", size=17)
iac_d2.note(380, 176, "to = module.db.aws_db_instance.this }", "pen", size=17)
iac_d2.note(380, 214, "and set prevent_destroy on anything stateful", size=16)

IAC_DEEP = dict(
    side="splitting state, reading plans, refactoring safely",
    intro="The note covers plans, remote state and applying from CI. As the code grows, three questions decide whether it stays safe: how much infrastructure one apply can touch, how to read a plan so the dangerous lines stand out, and how to restructure the code without the tool deciding to rebuild your database.",
    parts=[
        ("How much can one apply touch?", """  <p>With one big state file, every change is planned against everything: a typo in an alarm can show up next to a change to the network, and one bad apply can damage both. Split the state so a change can only reach what it should.</p>
  <ul>
    <li><b>By layer</b>, ordered by how often things change: a foundation layer (network, DNS, base permissions), a data layer (databases, buckets), and an apps layer (services, queues, alarms).</li>
    <li><b>By environment:</b> separate state for staging and production, ideally in separate accounts.</li>
    <li><b>Lower layers publish outputs</b> (subnet ids, database endpoints) that upper layers read. Never the other way round.</li>
  </ul>
  <p>Smaller states also plan faster and lock less: two teams can apply their own app layers at the same time. Don't split so far that one change needs five applies in the right order; layers that always change together belong together.</p>""", [iac_d1]),
        ("Reading a plan for the dangerous lines", """  <p>Most plans are routine. The skill is spotting the few lines that aren't:</p>
  <ul>
    <li><b>Replacements</b> (<code>-/+</code>, “must be replaced”): some attribute changes can't be made in place, so the tool destroys and recreates. Harmless for a stateless instance; a disaster for a database or a bucket.</li>
    <li><b>Deletes</b> you didn't expect, often from a renamed resource or a changed <code>count</code>.</li>
    <li><b>Permission changes:</b> new IAM policies, wider security groups, public access settings.</li>
    <li><b>The size of the plan:</b> a one-line code change that plans 40 changes needs explaining.</li>
  </ul>
  <p>Don't rely on reviewers alone. Set <code>prevent_destroy</code> on stateful resources, and run <b>policy checks</b> on the plan in CI (Conftest/OPA, Sentinel, Checkov): “no deletes of databases”, “no public buckets”, “every resource is tagged”. A failing policy stops the apply before a person has to notice.</p>""", []),
        ("Refactoring without rebuilding", """  <p>The tool tracks each resource by its <b>address</b> in the code. Rename a resource, move it into a module, or change a <code>count</code> to a <code>for_each</code>, and the address changes. To the tool that looks like one resource removed and another added: destroy and create.</p>
  <ul>
    <li><b>moved blocks</b> (Terraform 1.1+, OpenTofu) record that an address changed. The plan then shows a move, not a rebuild, and the block documents the refactor in code review.</li>
    <li><b>import blocks</b> bring resources created by hand under management without touching them. Write the code, plan until it shows no changes, then apply the import.</li>
    <li><b>removed blocks</b> (or <code>state rm</code>) stop managing a resource without destroying it, for handing it to another state.</li>
  </ul>
  <p>Always refactor in a change of its own, with no other edits, so the plan should show moves and nothing else. If it shows a destroy, stop.</p>""", [iac_d2]),
    ],
)

# ------------------------------------------------------------------ SLOs & error budgets
slo_d1 = Doodle(760, 290, "Budget burn over a 28-day window for a 99.9 percent SLO. At burn rate 1 the budget runs out exactly at day 28. A slow leak at burn rate 2 runs out on day 14 and should open a ticket. An outage at burn rate 13 uses 2 percent of the budget in an hour and should page someone.",
                "Burn rate = how many times faster than “exactly on budget” you are spending it.")
slo_d1.line("M70 30 V240 H730", thin=True)
slo_d1.text(60, 40, "100%", "t-s", anchor="end", size=14)
slo_d1.text(60, 244, "0%", "t-s", anchor="end", size=14)
slo_d1.text(90, 20, "budget left ↓", "t-s", anchor="start", size=14)
slo_d1.text(730, 264, "day 28", "t-s", anchor="end", size=14)
slo_d1.text(400, 264, "day 14", "t-s", anchor="middle", size=14)
slo_d1.line("M70 34 L730 236", color="green")
slo_d1.note(560, 150, "rate 1: on budget", "green", anchor="start", size=15)
slo_d1.line("M70 34 L400 236", color="pen", dash=True)
slo_d1.note(232, 116, "rate 2: ticket", "pen", anchor="start", size=15)
slo_d1.line("M70 34 L100 236", color="red")
slo_d1.note(112, 214, "rate 13+: page now", "red", anchor="start", size=15)
slo_d1.note(380, 284, "SLO 99.9% on 10 million requests: 10,000 may fail in the window", size=15)

SLO_DEEP = dict(
    side="the numbers, choosing SLIs, a policy that bites",
    intro="The note defines SLIs, SLOs and the error budget. This chapter does the arithmetic (how big the budget is, how burn-rate alerts are set), shows how to pick an SLI that matches what users feel, and how to write the budget policy so it changes decisions instead of decorating a dashboard.",
    parts=[
        ("Doing the numbers", """  <p>An SLO of 99.9% over 28 days allows 0.1% bad: <b>about 40 minutes</b> of full outage, or for a service with 10 million requests in the window, <b>10,000 failed or slow requests</b>. Request-based budgets are usually fairer: a slow hour at night costs less than a slow hour at lunch.</p>
  <p>The <b>burn rate</b> says how fast you are spending: rate 1 uses the budget exactly over the window; rate 2 uses it in half the window. Alerts look at the burn rate over two windows (a long one to be sure, a short one to know it's still happening). Common settings for a 28-day window:</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Spends</th><th scope="col">Alert</th></tr></thead><tbody>
    <tr><td>2% of the budget in 1 hour (rate ≈ 13)</td><td>Page now. Check the last 5 minutes too.</td></tr>
    <tr><td>5% in 6 hours (rate ≈ 5.6)</td><td>Page. Check the last 30 minutes too.</td></tr>
    <tr><td>10% in 3 days (rate ≈ 1)</td><td>Ticket for working hours.</td></tr>
  </tbody></table></div>
  <p>This replaces a dozen threshold alerts (“error rate above 1% for 5 minutes”) with a few that fire only when users are really losing out.</p>""", [slo_d1]),
        ("Choosing an SLI users would agree with", """  <p>An SLI is good events divided by valid events. Each word needs a decision:</p>
  <ul>
    <li><b>Where you measure.</b> The closer to the user, the truer: the load balancer sees failures your service never logs; real-user monitoring sees slow networks too. Server metrics alone miss requests that never arrived.</li>
    <li><b>What “good” means.</b> Success <i>and</i> fast enough: “checkout requests that return 2xx in under 800 ms”. Use a threshold from what users notice, not the current p99.</li>
    <li><b>What's valid.</b> Leave out traffic that says nothing about your service: health checks, synthetic probes, and client errors such as 400 and 404. Count 429 (you refused them) and 5xx.</li>
    <li><b>A journey, not a server.</b> “Search returns results” across three services is one SLI; three per-service SLIs at 99.9% each give the user about 99.7%.</li>
  </ul>
  <p>Start with three to five SLIs for the journeys that matter. A dashboard of forty SLOs gets the same attention as none.</p>""", []),
        ("A budget policy that changes decisions", """  <p>The budget only matters if everyone agreed in advance what happens when it runs low. Write it down, have product and engineering leads sign it, and keep it short:</p>
  <ul>
    <li><b>Budget left:</b> ship as normal; planned risky work (migrations, experiments) is fine.</li>
    <li><b>Under 25% left:</b> risky changes need a second reviewer and a rollback plan; the team looks at what is burning.</li>
    <li><b>Budget spent:</b> freeze non-urgent releases for that service; the top two causes of burn become the team's next work until the burn rate is below 1.</li>
    <li><b>Exceptions</b> (security fixes, legal deadlines) are decided by a named person, and written down.</li>
  </ul>
  <p>Review SLOs every quarter. If the budget is never touched, the SLO may be too loose to guide anything, or the team is spending effort on reliability users don't need. If it's always spent, the target or the system has to change.</p>""", []),
    ],
)

# ------------------------------------------------------------------ Incident response & postmortems
pm_d1 = Doodle(760, 280, "An incident timeline. A deploy goes out at 01:40. Errors start at 01:42. The alert fires at 01:49, seven minutes to detect. The on-call engineer declares a SEV-2 at 01:55 and becomes incident commander. The deploy is rolled back at 02:03, mitigated 21 minutes after errors began. The cause is found the next morning. The postmortem measures detection and mitigation time, not time to find the root cause.",
               "Measure the time users were hurt: start to detect, detect to mitigate.")
pm_d1.arrow(20, 140, 744, 140)
for x, t, lab, col in [(50, "01:40", "deploy", ""), (110, "01:42", "errors start", "red"), (260, "01:49", "alert", ""), (380, "01:55", "SEV-2 declared", ""),
                       (540, "02:03", "rolled back", "green"), (700, "09:30", "cause found", "")]:
    pm_d1.line(f"M{x} 128 V152")
    pm_d1.text(x, 118, t, "t-head", size=15)
    pm_d1.note(x, 176 if x not in (110, 380, 700) else 198, lab, col, size=15)
pm_d1.box(110, 30, 150, 50, "7 min", "pink", sub="to detect", size=16, subsize=13)
pm_d1.box(262, 30, 278, 50, "14 min", "y", sub="detect to mitigate", size=16, subsize=13)
pm_d1.note(380, 250, "users hurt for 21 minutes · the 7 hours after that didn't hurt anyone", "pen", size=16)

POSTMORTEM_DEEP = dict(
    side="running it, finding contributing factors, actions that happen",
    intro="The note sets out severities, roles and the blameless postmortem. This chapter follows one incident from the first alert to the last action item: what the first fifteen minutes look like, how to find the factors that made the incident possible and large, and how to write action items that actually get done.",
    parts=[
        ("The first fifteen minutes", """  <p>Under pressure, people do what they have practised. A short routine for the start of every incident:</p>
  <ol>
    <li><b>Declare.</b> Open the incident channel, set a severity, say who is commander. A wrong severity can be changed; a late declaration can't.</li>
    <li><b>Look for recent change.</b> Deploys, flag changes, config, a provider's status page. Most incidents follow a change.</li>
    <li><b>Mitigate first.</b> Roll back, turn off the flag, fail over, shed load. Ask “what makes users whole fastest?”, not “why did this happen?”.</li>
    <li><b>Communicate on a clock.</b> A status update every 30 minutes for SEV-1 and SEV-2, even if it says “no change”. Silence is what makes stakeholders join the call.</li>
    <li><b>Keep notes as you go</b> in the channel, with times. They become the postmortem's timeline.</li>
  </ol>
  <p>The commander's job is coordination: deciding, assigning, keeping the channel tidy. If they start debugging, nobody is doing their job.</p>""", [pm_d1]),
        ("Contributing factors, not a root cause", """  <p>“The root cause was a bad config value” ends the conversation too early. Incidents happen when several things line up, and each one is a place to improve. For the 01:40 incident:</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Question</th><th scope="col">Answer · possible action</th></tr></thead><tbody>
    <tr><td>What triggered it?</td><td>A config change set the payment timeout to 500 ms instead of 5,000 ms → validate config ranges in CI.</td></tr>
    <tr><td>What made it possible?</td><td>Config deploys skipped the canary stage → config goes through the same canary as code.</td></tr>
    <tr><td>What made it worse?</td><td>The deploy ran at night with one person on call → risky changes in working hours.</td></tr>
    <tr><td>What made it slow to see?</td><td>The alert waited 5 minutes on the error rate → a burn-rate alert on the checkout SLO.</td></tr>
    <tr><td>What limited the damage?</td><td>Rollback took one command → keep it that way; practise it.</td></tr>
  </tbody></table></div>
  <p>Notice that no answer is “the engineer should be more careful”. If one person's slip can cause a SEV-2, the system made that slip easy and expensive. Fix the system.</p>""", []),
        ("Action items that get done", """  <p>Postmortems fail at the end: twelve vague action items, no owners, closed by nobody. Fewer and sharper works better:</p>
  <ul>
    <li><b>Three to five items</b>, each with an owner, a date and a ticket in the team's normal backlog (not a separate postmortem list nobody looks at).</li>
    <li><b>A mix of kinds:</b> prevent (validate config), detect (better alert), mitigate (faster rollback). Don't only prevent; the next incident will be a different one.</li>
    <li><b>Specific enough to finish:</b> “add range checks for timeout settings in the config schema”, not “improve config safety”.</li>
    <li><b>Reviewed:</b> open postmortem actions are checked in the weekly operations review until they are closed or deliberately dropped.</li>
  </ul>
  <p>Then share the postmortem beyond the team, and once a quarter replay a past incident as a <b>game day</b>, to check that the fixes, the alerts and the routine still work.</p>""", []),
    ],
)

# ------------------------------------------------------------------ Autoscaling
as_d1 = Doodle(760, 290, "Load rising faster than capacity can follow. Traffic climbs steadily from 9:00. The autoscaler notices after a minute, asks for more pods, which need new machines first; machines take two minutes and pods one more. During those three to four minutes, the existing instances must carry the extra load, which is what headroom is for.",
               "Capacity arrives in steps, minutes after demand. Headroom carries the gap.")
as_d1.line("M60 30 V240 H740", thin=True)
as_d1.note(740, 266, "time →", anchor="end", size=15)
as_d1.text(50, 40, "load", "t-s", anchor="end", size=14)
as_d1.line("M60 220 L740 50", color="red")
as_d1.note(700, 46, "demand", "red", anchor="end", size=15)
as_d1.line("M60 190 H250 V150 H430 V110 H610 V70 H740", color="green")
as_d1.note(740, 92, "capacity", "green", anchor="end", size=15)
for x0, x1, cap in [(180, 250, 190), (340, 430, 150), (500, 610, 110), (660, 740, 70)]:   # demand above capacity
    as_d1.raw(f'<path class="d d-red f-pink" d="M{x0} {cap} L{x1} {220 - 0.25 * (x1 - 60):g} L{x1} {cap} Z"/>')
as_d1.note(190, 214, "the gaps: headroom must carry these", "red", anchor="start", size=15)
as_d1.note(400, 284, "notice ~1 min · new machine ~2 min · pod ready ~1 min", "pen", size=16)

AUTOSCALING_DEEP = dict(
    side="headroom and lag, two layers of scaling, protecting what's behind you",
    intro="The note covers signals, limits and “up fast, down slow”. This chapter is about the numbers behind those settings: how much spare capacity you need given how slowly new capacity arrives, why scaling pods also means scaling machines, and how to stop a scale-up from overwhelming the database behind it.",
    parts=[
        ("Headroom: carrying the gap", """  <p>New capacity always arrives late. The autoscaler needs a minute or so of data to notice a rise, a new machine may take two minutes, and a new pod another minute to become ready. For three to four minutes, the instances you already have must carry the extra load.</p>
  <p>That sets the <b>target utilisation</b>. If traffic can grow 30% in four minutes at the start of a sale, instances must be able to absorb 30% more than they carry now: a target around 70% CPU, not 90%. Add the loss of one zone: with three zones, the remaining two must carry everything until replacements arrive. Work it out from your own numbers:</p>
  <ul>
    <li><b>Lag:</b> time from load rising to a new instance serving. Measure it in a load test, don't guess.</li>
    <li><b>Ramp:</b> how fast load grows on a bad day (from your metrics, launch days included).</li>
    <li><b>Headroom</b> = ramp × lag, as a fraction of current capacity. Target utilisation = 100% minus that, minus a margin.</li>
  </ul>
  <p>Cutting lag is often cheaper than buying headroom: smaller images, faster start-up, and capacity scheduled ahead of known peaks.</p>""", [as_d1]),
        ("Two layers: pods and machines", """  <p>In Kubernetes, the pod autoscaler (HPA, or KEDA for queues) only asks for more pods. If the cluster has no room, the new pods wait as <i>Pending</i> until the cluster autoscaler (or Karpenter) adds machines. Two autoscalers, two delays, and the second is usually the slower.</p>
  <ul>
    <li><b>Keep a little spare room</b> in the cluster: a few low-priority placeholder pods that reserve space and are evicted the moment real pods need it. Real pods start in seconds; the placeholders wait for the new machine instead.</li>
    <li><b>Make requests honest.</b> The cluster autoscaler sizes machines from pod <i>requests</i>, not actual use. Requests set too low pack too many pods onto a machine; too high waste money and slow scaling.</li>
    <li><b>Watch scale-down.</b> Removing a machine evicts its pods. Set pod disruption budgets so a scale-down never takes out too many copies of one service at once.</li>
  </ul>""", []),
        ("Protecting what's behind you", """  <p>Autoscaling the web tier moves the bottleneck to whatever it calls. Twenty pods with a database pool of 20 connections each need 400 connections; scale to 60 pods and you need 1,200, far beyond what the database can take (see Connection Pooling, Vol. 3). The scale-up that was supposed to help takes the database down.</p>
  <ul>
    <li><b>Set the maximum from the dependency,</b> not just the budget: max pods × pool size must stay below the database's limit, or put a pooler in between.</li>
    <li><b>Scale workers on the queue, within the downstream limit.</b> More workers than the payment provider's rate limit allows only produce 429s.</li>
    <li><b>Shed load before the limit.</b> When the maximum is reached, reject excess requests quickly with 429 or 503 rather than queueing them until everything times out.</li>
    <li><b>Scale to zero only where cold starts are acceptable:</b> background jobs and internal tools, not checkout. Keep a minimum of two or three for anything users wait on.</li>
  </ul>""", []),
    ],
)

REVISIONS = {
    "infrastructure-as-code": dict(deep_dive=IAC_DEEP),
    "slo-error-budgets": dict(deep_dive=SLO_DEEP),
    "postmortems": dict(deep_dive=POSTMORTEM_DEEP),
    "autoscaling": dict(deep_dive=AUTOSCALING_DEEP),
}
