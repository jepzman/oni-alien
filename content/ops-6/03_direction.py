# Series 2 · Book 5 · The IT Operations Notebook · Vol. 6 · Setting direction.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 6".

# ------------------------------------------------------------------ 07 What to Automate Next
au_problem = Doodle(760, 260, "Doodle of the reliability team's automation wish list in June 2028: 27 ideas, from a fully scripted city set-up to a bot that answers 'is it down?'. Everyone has a favourite. Half the scripts written so far automate part of a job: the city script sets up zones but someone still clicks through monitoring; the restore check runs, but someone still starts the restore by hand. The team's toil is 28 percent of its time.",
                    "27 automation ideas, everyone's favourite first, and half the existing scripts do half a job.")
au_problem.box(14, 30, 230, 100, "27 ideas", "y", sub="everyone's favourite", size=20, subsize=14)
au_problem.box(264, 30, 230, 100, "half-automated", "pink", sub="script + clicks", size=19, subsize=14)
au_problem.box(514, 30, 232, 100, "toil 28 %", "y", sub="reliability team, June", size=20, subsize=14)
au_problem.note(380, 180, "which first? and why do half-scripts still need a person?", "red", size=17)

au_analogy = Doodle(760, 220, "Doodle of a farmer choosing between machines. She counts which job takes the most hours across the year and is the riskiest to get wrong, and buys the machine for that first. She doesn't buy half a machine: a milking robot that still needs someone to carry the milk saves nothing at 5 a.m.",
                    "Automate the job with the most hours and risk first, and the whole job, or nobody sleeps longer.")
au_analogy.icon("gear", 60, 50, 1.3)
au_analogy.box(170, 40, 270, 100, "hours × risk", "y", sub="choose by numbers", size=19, subsize=14)
au_analogy.box(470, 40, 276, 100, "the whole job", "green", sub="not half a machine", size=19, subsize=14)
au_analogy.note(450, 190, "half-automation still needs someone at 5 a.m.", "pen", size=18)

au_how = Doodle(760, 400, "The reliability team's automation rules from June 2028. Score each idea by hours of toil saved per month, times how often the manual way goes wrong, plus risk removed; the top three go into the quarter. Automate end to end: a job counts only when no person has to start, click or check it in the normal case. A toil budget: the team keeps toil under 30 percent of its time, and above that, automation beats features. Q3 2028: new-city set-up end to end ('larder new-city' creates zones, router, monitoring, on-call, status page in 20 minutes); restore tests start, check and report themselves; access review lists generated from the identity provider. Ops side of Ana's golden path: every new service is born with SLO file, alerts, dashboard, runbook skeleton and catalogue entry. Team toil: 28 percent in June, 19 percent in October.",
                "Score by hours × errors + risk; automate end to end; keep a toil budget. Q3: three whole jobs automated; toil 28 % → 19 %.")
au_how.box(14, 14, 236, 110, "score", "blue", sub="hours saved × error rate + risk", size=19, subsize=12)
au_how.box(262, 14, 236, 110, "end to end", "green", sub="no person to start, click or check", size=19, subsize=12)
au_how.box(510, 14, 236, 110, "toil budget", "y", sub="< 30 %; above it, automation first", size=19, subsize=12)
for i, (t, s) in enumerate([("larder new-city", "zones · router · monitoring · on-call · status page · 20 min"), ("restore tests", "start, check, report themselves"), ("access review lists", "generated from the identity provider"), ("golden path (ops side)", "SLOs · alerts · dashboard · runbook · catalogue")]):
    au_how.box(14, 146 + i * 50, 240, 42, t, "green", size=14)
    au_how.box(264, 146 + i * 50, 482, 42, s, "paper", size=13)
au_how.note(380, 366, "team toil: 28 % (Jun) → 19 % (Oct)", "green", size=17)

AUTOMATION = dict(
    slug="automation-strategy",
    kicker="a.k.a. “optimise and automate, on purpose”",
    tldr="Automation ideas are endless; time isn't. Choose by <b>numbers</b>: hours of toil saved, how often the manual way goes wrong, and risk removed. Automate <b>the whole job</b>, so that in the normal case no person has to start, click or check it, because half-automation still needs someone at 5 a.m. Keep a <b>toil budget</b>: when toil goes over it, automation beats features. And make new things <b>born automated</b>.",
    chips=[("Family", "setting direction"), ("Lives in", "the improvement register (scored), ops/toil-log.md for the team"), ("Pairs with", "toil (vol. 1), the golden path, the improvement register")],
    itil=dict(groups=["general", "technical"], chain=["improve", "build"], practices=["continual improvement", "infrastructure and platform management"],
              sre="“eliminating toil”; the 50 % cap; automate the whole process", principles=["Optimise and automate", "Focus on value"],
              older="ITIL v3: continual service improvement"),
    problem_side="Larder, June 2028",
    problem="""  <p class="lead">The reliability team's automation wish list in June has <b>27 ideas</b>, from a fully scripted city set-up to a chat bot that answers “is it down?”. Everyone has a favourite. Half the scripts written so far automate <b>part</b> of a job: the city script sets up zones, but someone still clicks through monitoring and on-call; the restore check runs, but someone still starts the restore by hand. <span class="hl-pink">The team's toil is 28 % of its time</span>, and Lotte and Yusuf are about to add a lot of new hours.</p>
  <ul>
    <li>Favourites win over the jobs that cost the most.</li>
    <li>Half-automation keeps a person in the loop at the worst moments.</li>
    <li>New services keep arriving with handwork built in.</li>
  </ul>""",
    problem_figs=[au_problem],
    meanwhile=[("architect-6", "golden-paths", "Ana's golden path of 8 May 2028: `larder new-service`, from new service to first deploy in 1 day instead of 3 weeks.",
                "Eli's side of the same path: every new service born with an SLO file, alerts, a dashboard, a runbook skeleton and a catalogue entry.")],
    analogy_side="the farmer's next machine",
    analogy="""  <p>A farmer choosing her next machine counts <b>which job takes the most hours across the year</b>, and which goes wrong most dangerously, and buys for that first. She doesn't buy <b>half a machine</b>: a milking robot that still needs someone to carry the milk to the tank saves nothing at 5 a.m.</p>""",
    analogy_figs=[au_analogy],
    map=[("Hours across the year", "Toil hours saved per month"),
         ("Goes wrong dangerously", "Error rate of the manual way, risk removed"),
         ("Half a machine", "A script that still needs clicks"),
         ("The whole job", "No person to start, click or check, normally"),
         ("Buying for the biggest job first", "Top three ideas into the quarter")],
    how_side="score by numbers, automate end to end, keep a toil budget",
    how="""  <p>From <b>June</b> the team uses three rules:</p>
  <ul>
    <li><b>Score every idea</b>: hours of toil saved per month × how often the manual way goes wrong, plus risk removed. The <b>top three</b> go into the quarter.</li>
    <li><b>Automate end to end</b>: a job counts as automated only when, in the normal case, <b>no person has to start, click or check it</b>.</li>
    <li><b>A toil budget</b>: the team keeps toil under <b>30 %</b> of its time. Above that, automation comes before feature requests from other teams.</li>
  </ul>
  <p>Q3 2028's three: <b>new-city set-up end to end</b> (<code>larder new-city</code> creates zones, the WMS route, monitoring, on-call and the status page in <b>20 minutes</b>, used for Haarlem in August); <b>restore tests</b> that start, check and report themselves; and <b>access review lists</b> generated from the identity provider. With Ana's golden path, every new service is <b>born automated</b>: an SLO file, alerts, a dashboard, a runbook skeleton and a catalogue entry. Team toil falls from <b>28 % in June to 19 % in October</b>, with two new people on the team.</p>""",
    how_figs=[au_how],
    steps=[("Log toil as a team", "Hours per kind, monthly."),
           ("Score ideas by numbers", "Hours × errors + risk."),
           ("Take the top three per quarter", "Not the favourites."),
           ("Automate the whole job", "No start, click or check in the normal case."),
           ("Keep a toil budget", "Above it, automation first."),
           ("Make new things born automated", "Through the golden path.")],
    vocab=[("Automation", "Doing a job without a person, from start to finish."),
           ("Half-automation", "A script that still needs a person to start, click or check."),
           ("Toil budget", "The share of time toil may take before automation comes first."),
           ("Scoring", "Ranking ideas by numbers instead of preference."),
           ("Born automated", "New services created with their operations work already automated."),
           ("Self-service", "Others can do the job themselves, safely.")],
    code=dict(file="ops/automation/q3-2028.md", note="scored June 2028", plain=True, src="""
idea                                   toil h/month  errors  risk  score   status
new-city set-up end to end             22            often   high  1st     ✓ larder new-city, 20 min
                                                                            (used for Haarlem, Aug)
restore tests self-starting + report   9             some    high  2nd     ✓
access review lists from IdP           7             some    med   3rd     ✓
"is it down?" chat bot                 2             rare    low   19th    later
… 27 ideas

rules     whole job: no person to start, click or check (normal case)
          toil budget < 30 % of team time · above → automation first
          golden path: new services born with SLOs, alerts, dashboard, runbook, catalogue
toil      Jun 28 % → Oct 19 % (team of 4)
"""),
    tools="tools: the team's toil log, a scored list in the improvement register, and the golden path templates.",
    ladder=[("favourite scripts", ["Half-automated jobs.", "Toil unmeasured."]),
            ("scored, end to end, budgeted", ["Top three a quarter.", "New services born automated."]),
            ("self-service for other teams", ["Teams run the automations themselves.", "Toil per team visible."]),
            ("little left to automate", ["Toil rarely over budget.", "Engineers mostly build."])],
    ladder_now=1,
    baseline="Each line compares <b>everyone's favourite half-scripts</b> to <b>scored, end-to-end automation within a toil budget</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 3, "Manual errors removed from risky jobs."),
             (2, 3, "Restores and city set-ups faster."),
             (2, 3, "Fewer hand-made changes."),
             (3, 3, "Neutral."),
             (1, 4, "28 % → 19 % toil."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer jobs needing a person at night."),
             (3, 3, "A quarterly scoring hour.")],
    pitfalls=[("Automating favourites", "Fun scripts, little saved.", "score by numbers."),
              ("Half-automation", "Still needs someone at 5 a.m.", "the whole job, or it doesn't count."),
              ("Automating a broken process", "Faster mistakes.", "fix the process first."),
              ("No budget", "Toil creeps back as the business grows.", "a toil budget, checked monthly.")],
    use=["The automation list is long and argued about.", "Scripts still need someone to click.", "Toil is rising.", "New services keep arriving with handwork."],
    skip=["One-off jobs: automation costs more than it saves."],
    related=["<b>Why Am I Always Busy?</b> (vol. 1)", "<b>Golden Paths</b> (Ana, vol. 6)", "<b>Continual Improvement That Continues</b> (this volume)", "<b>A New City by Checklist</b> (vol. 3)"],
    quiz=[("How does the team choose what to automate?", "By score: toil hours saved × how often the manual way goes wrong, plus risk removed; top three per quarter."),
          ("When does a job count as automated?", "When, normally, no person has to start, click or check it."),
          ("What's the toil budget?", "Under 30 % of team time; above it, automation comes first."),
          ("What did Q3 automate?", "New-city set-up end to end, self-running restore tests, and access review lists from the identity provider."),
          ("What does “born automated” mean?", "New services come with SLOs, alerts, dashboard, runbook skeleton and catalogue entry from the golden path.")],
    quiz_sit=[("Yusuf wants to spend two weeks on the “is it down?” chat bot because stores ask him that often. It scored 19th. What do you say?", "Look at why stores ask: the self-service page's “just us?” may need fixing (an hour). If the asking is real toil, log it and it'll score higher next quarter. Two weeks go to the top three.")],
    try_it="List five things you'd like to automate. For each, estimate hours saved per month and how often the manual way goes wrong. Which is first by numbers, not by preference? Does your current script do the whole job?",
    remember="Choose automation <span class=\"hl\">by numbers</span>, automate <span class=\"hl\">the whole job</span>, and keep toil under a budget.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 7, the evolution of automation at Google.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 6, eliminating toil.",
             "AXELOS, <i>ITIL 4: Continual improvement</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 08 Which Tools Do We Really Need?
tl_problem = Doodle(760, 260, "Doodle of Larder's operations tools counted in July 2028: 17. Two paging tools (one from 2026, one a team bought in 2027), three tools for metrics and logs, two status pages, tickets in both the helpdesk and the engineering tracker, a wiki nobody updates, two uptime checkers. 11,200 euros a month. On-call needs to look in four places during an incident.",
                    "17 operations tools, €11,200 a month, two of most things, and four places to look in an incident.")
for i, (t, n) in enumerate([("paging", "2"), ("metrics + logs", "3"), ("status pages", "2"), ("tickets", "2"), ("uptime", "2"), ("wiki", "1 (stale)")]):
    tl_problem.box(14 + i * 124, 30, 112, 100, t, "y", sub=n, size=14, subsize=16)
tl_problem.note(380, 180, "€11,200 a month · four places to look in an incident", "red", size=17)

tl_analogy = Doodle(760, 220, "Doodle of a kitchen drawer with three tin openers, two broken peelers and a gadget nobody remembers buying. A good cook keeps one of each tool she uses, sharp, in the same place, and gives the rest away. In a hurry she finds what she needs without thinking.",
                    "Three tin openers and a mystery gadget. Keep one good tool per job, in the same place.")
tl_analogy.icon("cabinet", 60, 40, 1.4)
tl_analogy.box(170, 40, 270, 100, "the drawer", "pink", sub="3 openers · 2 broken peelers", size=18, subsize=13)
tl_analogy.box(470, 40, 276, 100, "one per job", "green", sub="sharp, same place", size=18, subsize=14)
tl_analogy.note(450, 190, "in a hurry, you find it without thinking", "pen", size=18)

tl_how = Doodle(760, 400, "Larder's operations toolset after the review in July and August 2028. Each tool has a job written in one sentence, an owner, a cost and a user count. Overlaps chosen by a short trial and the people who use them. Paging: one tool. Metrics, logs and traces: one platform plus the security log store. Status page: one, for customers and clients. Tickets: the helpdesk for requests and incidents from people, the tracker for engineering work, with a link between them. Knowledge: the repository, and the old wiki archived. Uptime: the outside checks in the metrics platform. 17 tools became 9; cost from 11,200 to 6,900 euros a month; on-call looks in two places. Any new tool needs a job no current tool does.",
                "Each tool: one job, an owner, a cost. 17 → 9 tools, €11,200 → €6,900 a month, two places to look.")
rows = [("paging", "one tool"), ("metrics · logs · traces", "one platform + security log store"), ("status page", "one, customers + clients"),
        ("tickets", "helpdesk (people) + tracker (engineering), linked"), ("knowledge", "the repository · wiki archived")]
for i, (k, v) in enumerate(rows):
    y = 14 + i * 50
    tl_how.box(14, y, 240, 42, k, "blue", size=14)
    tl_how.box(264, y, 482, 42, v, "paper", size=13)
tl_how.row([("17 tools", "€11,200 / month", "pink"), ("9 tools", "€6,900 / month", "green")], x=110, y=274, h=80, w=250, gap=40, size=19, subsize=14, arrows=True)
tl_how.note(380, 382, "a new tool needs a job no current tool does", "pen", size=15)

TOOLSET = dict(
    slug="ops-toolset",
    kicker="a.k.a. “rationalising the operations toolset”",
    tldr="Operations tools multiply: every team buys the one it needs, and nobody switches anything off. Keep <b>one tool per job</b>, each with a <b>one-sentence job, an owner, a cost and its users</b>. Choose between overlaps with the people who use them, consolidate, and archive the rest. Fewer tools means fewer places to look in an incident, fewer logins, less cost, and one way of doing things.",
    chips=[("Family", "setting direction"), ("Lives in", "ops/tools.md; the asset register (vol. 1)"), ("Pairs with", "dashboards (vol. 4), decommissioning (vol. 4), cloud costs (vol. 5)")],
    itil=dict(groups=["general", "technical"], chain=["plan", "improve"], practices=["infrastructure and platform management", "IT asset management", "service financial management"],
              sre="(fewer, well-understood tools for responders)", principles=["Keep it simple and practical", "Think and work holistically"],
              older="ITIL v3: technical management (tool selection)"),
    problem_side="Larder, July 2028",
    problem="""  <p class="lead">Eli counts the operations tools in July: <b>17</b>. There are two paging tools (one from 2026, and one a team bought in 2027), three tools for metrics and logs, two status pages, tickets in both the helpdesk and the engineering tracker, a wiki nobody updates, and two uptime checkers. Together they cost <b>€11,200 a month</b>. <span class="hl-pink">During an incident, on-call has to look in four places.</span></p>
  <ul>
    <li>Each tool made sense to someone when it was bought.</li>
    <li>Overlaps mean two truths, and two places to forget.</li>
    <li>New people learn 17 logins before their first page.</li>
  </ul>""",
    problem_figs=[tl_problem],
    analogy_side="the kitchen drawer",
    analogy="""  <p>A kitchen drawer fills up with <b>three tin openers, two broken peelers</b> and a gadget nobody remembers buying. A good cook keeps <b>one of each tool she uses</b>, sharp, in the same place, and gives the rest away. In a hurry she finds what she needs <b>without thinking</b>.</p>""",
    analogy_figs=[tl_analogy],
    map=[("Three tin openers", "Two paging tools, two status pages"),
         ("The broken peelers", "The wiki nobody updates"),
         ("One sharp tool per job", "One tool per job, with an owner"),
         ("Same place every time", "Two places to look in an incident"),
         ("Giving the rest away", "8 tools archived and cancelled")],
    how_side="one tool per job, each with a sentence, an owner and a cost",
    how="""  <p>In <b>July and August</b>, Eli and the reliability team give each tool a <b>one-sentence job</b>, an owner, a cost and a user count. Where two tools do the same job, the people who use them run a <b>short trial</b> and choose. The result:</p>
  <ul>
    <li><b>Paging</b>: one tool.</li>
    <li><b>Metrics, logs and traces</b>: one platform, plus the separate security log store.</li>
    <li><b>Status page</b>: one, for customers and business clients.</li>
    <li><b>Tickets</b>: the helpdesk for requests and incidents from people, the tracker for engineering work, linked to each other.</li>
    <li><b>Knowledge</b>: the repository; the old wiki is archived.</li>
    <li><b>Uptime</b>: the outside checks inside the metrics platform.</li>
  </ul>
  <p><b>17 tools become 9.</b> The cost falls from <b>€11,200 to €6,900 a month</b>. On-call looks in <b>two places</b>. Retiring the eight uses the decommissioning checklist. The rule from now on: <b>a new tool needs a job no current tool does</b>.</p>""",
    how_figs=[tl_how],
    steps=[("List every operations tool", "Card statements included."),
           ("Write each one's job in a sentence", "If you can't, that's a clue."),
           ("Add owner, cost and users", "From the asset register."),
           ("Choose between overlaps with users", "A short trial, not a vote by managers."),
           ("Retire the rest properly", "Decommissioning checklist."),
           ("Guard the door", "New tools need a new job.")],
    vocab=[("Toolset", "The set of tools a team uses to do its work."),
           ("Tool sprawl", "Many overlapping tools, bought separately."),
           ("Consolidation", "Reducing overlapping tools to one per job."),
           ("Total cost", "Licences plus the time to learn, maintain and switch between tools."),
           ("Tool owner", "The person who keeps a tool configured, current and paid for."),
           ("Context switching", "Moving between tools, costly during incidents.")],
    code=dict(file="ops/tools.md", note="after the review · August 2028", plain=True, src="""
job                                   tool                 owner   users   €/month
page the right person                 paging tool A        Eli     34      620
metrics, logs, traces, outside checks observability platf. Bram    30      3,900
security logs (1 year)                security log store   Eli     4       780
status for customers and clients      status page          Sam     —       90
requests + incidents from people      helpdesk             Sam     22      (shared)
engineering work                      tracker              Ben     30      (shared)
knowledge                             the repository       Eli     30      0
device management                     MDM                  Dee     8       ≈ 380
secrets                               vault                Bram    12      ≈ 130
                                      9 tools · €6,900 (was 17 · €11,200)
retired  paging tool B · 2 metrics tools · status page 2 · uptime checkers × 2 · wiki
rule     a new tool needs a job no current tool does
"""),
    tools="tools: the asset register, card statements, the people who use each tool, and the decommissioning checklist.",
    ladder=[("a drawer of tools", ["Overlaps, logins, costs.", "Four places to look."]),
            ("one tool per job, owned", ["Consolidated, archived.", "A door policy."]),
            ("integrated", ["Tools linked: alert → incident → ticket → review.", "One place to start."]),
            ("tools fade into the background", ["People think about the work, not the tools.", "Reviewed yearly."])],
    ladder_now=1,
    baseline="Each line compares <b>17 overlapping operations tools</b> to <b>9 tools, one per job, each with an owner and a cost</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "Two places to look instead of four."),
             (3, 3, "Neutral."),
             (2, 4, "One truth per job."),
             (2, 3, "Fewer tools to maintain."),
             (1, 4, "€11,200 → €6,900 a month."),
             (2, 3, "New people learn 9 tools, not 17."),
             (3, 3, "A month of trials and retirements.")],
    pitfalls=[("Choosing by managers' preference", "The people using it hate it.", "trial with users."),
              ("Keeping both just in case", "Sprawl returns.", "retire properly."),
              ("Ignoring time costs", "A free tool that costs hours.", "count learning and switching."),
              ("No door policy", "Back to 17 in two years.", "a new tool needs a new job.")],
    use=["Several tools do the same job.", "On-call looks in many places during incidents.", "Tool costs are unknown or growing.", "A new team is forming and needs a standard set."],
    skip=["When each tool truly has a separate job and everyone knows it."],
    related=["<b>Dashboards People Actually Open</b> (vol. 4)", "<b>Switching a System Off</b> (vol. 4)", "<b>What Does It Cost to Run?</b> (vol. 5)", "<b>What Do We Own, and Where Is It?</b> (vol. 1)"],
    quiz=[("What does every tool need?", "A one-sentence job, an owner, a cost and its users."),
          ("How were overlaps resolved?", "By a short trial with the people who use them."),
          ("What was the result?", "17 tools → 9; €11,200 → €6,900 a month; two places to look in an incident."),
          ("What's the rule for new tools?", "A new tool needs a job no current tool does."),
          ("Why count time, not just licences?", "Learning, maintaining and switching between tools costs hours, especially in incidents.")],
    quiz_sit=[("Dee's team wants a new error-tracking tool for the apps. The observability platform has a basic version. What happens?", "Ask what job the new tool does that the platform can't. If it's real (mobile crash grouping, say), it gets a sentence, an owner and a cost, and joins the list; if not, improve how the platform is used.")],
    try_it="List every tool your team uses for operations, with its cost. Write each one's job in a sentence. Where do two tools share a sentence? Which one would your on-call person keep?",
    remember="<span class=\"hl\">One tool per job</span>, each with an owner and a cost, and a door policy: a new tool needs <span class=\"hl\">a new job</span>.",
    sources=["AXELOS, <i>ITIL 4: Infrastructure and platform management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): on tooling for incident response.",
             "Gene Kim et al., <i>The DevOps Handbook</i> (2016): on shared tools and telemetry."],
)

# ------------------------------------------------------------------ 09 Where Are We Weak?
mc_problem = Doodle(760, 260, "Doodle of June 2028. Femke asks Eli for 'the state of operations' before the board. Eli could list everything that's been built since 2026, and it would sound good. But he doesn't know what's still weak, and his own view is the least objective in the building. Every practice in this notebook ended with a ladder from 'by hand' to 'automatic'; nobody has ever looked at all the ladders together.",
                    "“The state of operations?” Eli could list everything built. He can't say what's still weak.")
mc_problem.box(14, 30, 350, 100, "what's been built", "green", sub="sounds good", size=20, subsize=15)
mc_problem.box(396, 30, 350, 100, "what's still weak?", "pink", sub="unknown", size=20, subsize=15)
mc_problem.note(380, 180, "and Eli's own view is the least objective in the building", "red", size=17)

mc_analogy = Doodle(760, 220, "Doodle of a football team's end-of-season review: each part of the game (defending set pieces, fitness, passing under pressure) rated together by the coaches and the players, against what a good team does. The coach picks three things for pre-season, not twenty.",
                    "Rate each part of the game together, against what good looks like, and pick three for pre-season.")
mc_analogy.row([("set pieces", "2 / 4", "pink"), ("fitness", "3 / 4", "y"), ("passing", "3 / 4", "y"), ("pick three", None, "green")], y=40, h=96, gap=14, size=17, subsize=15)
mc_analogy.note(380, 186, "honest, together, and only three to work on", "pen", size=18)

mc_how = Doodle(760, 400, "Larder's operations maturity check, Monday 19 June 2028: a half-day with the reliability team, Ben, Cho, Dee, Sam, Joost's operations lead and Mo. Every practice in the notebook, scored on its own ladder from 1, by hand, to 4, automatic, with evidence, together. Strongest: incidents and reviews 3, change 3, on-call 3, monitoring 3. Weakest: capacity forecasting 2, knowledge 2, store self-service 2, vendor management 2, cost 2, and the people risk: two people still hold too much. Chosen for the next six months: knowledge (rewrite the last 6 undocumented systems), capacity forecasting from Ana's plans, and the reliability team itself. Re-check in December.",
                "Every practice scored on its own ladder, together, with evidence. Three weak spots chosen; re-check in six months.")
strong = [("incidents", 3), ("change", 3), ("on-call", 3), ("monitoring", 3)]
weak = [("capacity forecast", 2), ("knowledge", 2), ("store self-service", 2), ("vendors", 2), ("cost", 2)]
for i, (t, s) in enumerate(strong):
    mc_how.box(14 + i * 186, 14, 172, 70, t, "green", sub=f"{s} / 4", size=16, subsize=15)
for i, (t, s) in enumerate(weak):
    mc_how.box(14 + i * 148, 104, 136, 70, t, "pink", sub=f"{s} / 4", size=13, subsize=15)
mc_how.box(14, 196, 732, 64, "chosen: knowledge · capacity forecasting · the reliability team", "y", size=15)
mc_how.note(380, 296, "Mon 19 Jun · half a day · reliability team + Ben, Cho, Dee, Sam, Joost's lead, Mo", "pen", size=14)
mc_how.note(380, 332, "scored with evidence, never by one person", "red", size=15)
mc_how.note(380, 366, "re-check in December", "pen", size=15)

MATURITY = dict(
    slug="maturity-check",
    kicker="a.k.a. “assessing practice maturity”",
    tldr="A <b>maturity check</b> asks, practice by practice, how well each one is done today. Score each on a simple ladder (by hand → written → scripted → automatic), <b>together</b> with the people who depend on operations, and <b>with evidence</b>, not from one person's view. Then choose <b>three weak spots</b> to work on, not twenty, and check again in six months. It turns “how are we doing?” into a short, honest list.",
    chips=[("Family", "setting direction"), ("Lives in", "ops/maturity/2028-06.md; every half year"), ("Pairs with", "every ladder in this notebook, strategy and roadmap, the improvement register")],
    itil=dict(groups=["general"], chain=["improve", "plan"], practices=["continual improvement", "measurement and reporting"],
              sre="(SRE maturity and team health checks)", principles=["Start where you are", "Progress iteratively with feedback"],
              older="ITIL v3: process maturity frameworks; the ITIL 4 maturity model"),
    problem_side="Larder, June 2028",
    problem="""  <p class="lead">Before the board in June, Femke asks Eli for <b>“the state of operations”</b>. He could list everything built since 2026, and it would sound good. <span class="hl-pink">But he doesn't know what's still weak</span>, and his own view is the least objective in the building. Every practice in this notebook ends with a ladder from “by hand” to “automatic”, and nobody has ever looked at all the ladders together.</p>
  <ul>
    <li>Lists of achievements hide the gaps.</li>
    <li>The builder's view of their own work is always kind.</li>
    <li>Without a picture, priorities are whatever's loudest.</li>
  </ul>""",
    problem_figs=[mc_problem],
    analogy_side="the team's end-of-season review",
    analogy="""  <p>At the end of a season a football team rates <b>each part of its game</b> (defending set pieces, fitness, passing under pressure) <b>together</b>, coaches and players, against what a good team does. Then the coach picks <b>three things for pre-season</b>, not twenty. The honest 2 out of 4 on set pieces is worth more than any highlight reel.</p>""",
    analogy_figs=[mc_analogy],
    map=[("Each part of the game", "Each practice in the notebook"),
         ("What a good team does", "The ladder: by hand → written → scripted → automatic"),
         ("Coaches and players together", "The reliability team with Ben, Cho, Dee, Sam, Joost's lead, Mo"),
         ("Three things for pre-season", "Knowledge, capacity forecasting, the reliability team"),
         ("Next season's review", "Re-check in December")],
    how_side="every practice on its ladder, together, with evidence; pick three",
    how="""  <p>On <b>Monday 19 June</b>, Eli runs a half-day maturity check with the reliability team, Ben, Cho, Dee, Sam, Joost's operations lead and Mo. Every practice in the notebook is scored <b>on its own ladder</b>, from 1 (by hand) to 4 (automatic), <b>together and with evidence</b>: a link, a number, or a recent incident.</p>
  <ul>
    <li><b>Strongest</b>: incidents and reviews (3), change (3), on-call (3), monitoring (3).</li>
    <li><b>Weakest</b>: capacity <b>forecasting</b> (2), knowledge (2), store self-service (2), vendor management (2), cost (2). The people risk is named again: two people still hold too much.</li>
  </ul>
  <p>Three are chosen for the next six months: <b>knowledge</b> (write up the last six undocumented systems), <b>capacity forecasting</b> from Ana's growth plans, and <b>the reliability team itself</b>. Femke gets a one-page picture: the strong, the weak, the three, and the date of the next check in December.</p>""",
    how_figs=[mc_how],
    steps=[("List your practices", "This notebook's 90 notes are a start; pick the ones you do."),
           ("Use a simple ladder for each", "By hand, written, scripted, automatic."),
           ("Score together, with evidence", "People who depend on operations included."),
           ("Name the people risks too", "Not just processes."),
           ("Choose three", "Not twenty."),
           ("Re-check in six months", "Same people, same ladders.")],
    vocab=[("Maturity", "How well and how consistently a practice is done."),
           ("Maturity ladder", "Levels from ad hoc to automatic, with what each looks like."),
           ("Assessment", "Scoring current maturity, with evidence."),
           ("Evidence", "A link, number or recent example showing the level."),
           ("Baseline", "The first score, to compare later ones with."),
           ("Focus areas", "The few practices chosen for improvement.")],
    code=dict(file="ops/maturity/2028-06.md", note="Mon 19 June 2028 · half a day", plain=True, src="""
practice                     level  evidence
incidents + reviews          3      reviews ≤ 1 week (18 of 18), actions 88 % done
change enablement            3      failure rate 3 %, pipeline enforces windows
on-call                      3      load measured, 31 → 12 night pages (in progress)
monitoring + alerting        3      SLO burn alerts, 4 security alerts/week
capacity forecasting         2      plan per peak, no rolling forecast   ← chosen
knowledge                    2      6 systems still "ask Bram"           ← chosen
store self-service           2      31 % solved in store
vendor management            2      scorecards, exit plans just started
cost                         2      tags + waste hunt, no budgets per service
people                       —      two people hold too much             ← chosen (team)
next check: December 2028, same people, same ladders
"""),
    tools="tools: the ladders from each note, a half-day, the people who depend on operations, and evidence links.",
    ladder=[("“it's going well”", ["One person's view.", "Gaps hidden."]),
            ("a half-yearly check together", ["Every practice on its ladder, with evidence.", "Three chosen."]),
            ("tracked over time", ["Scores compared each half-year.", "Linked to the roadmap."]),
            ("self-assessed by every team", ["Teams check their own practices.", "Shared picture across the company."])],
    ladder_now=1,
    baseline="Each line compares <b>a list of achievements</b> to <b>every practice scored on its ladder, together, with evidence, and three chosen</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Strong and weak spots on one page."),
             (3, 3, "Neutral."),
             (2, 3, "Effort goes to the real gaps."),
             (2, 3, "The people risk named and acted on."),
             (3, 3, "Half a day, twice a year.")],
    pitfalls=[("Scoring alone", "Kind to your own work.", "together, with those who depend on it."),
              ("No evidence", "Scores are opinions.", "a link, number or example for each."),
              ("Twenty focus areas", "Nothing improves.", "three."),
              ("Chasing level 4 everywhere", "Automation where it isn't worth it.", "the level a practice needs, not the top.")],
    use=["Someone asks “how are we doing?”", "Planning the next half-year.", "After a period of building.", "Before a board or a big change."],
    skip=["In the middle of a crisis: fix it first."],
    related=["<b>Where Are We Going?</b> (next note)", "<b>Continual Improvement That Continues</b> (this volume)", "<b>What Is IT Operations For?</b> (vol. 1)", "<b>Is Our Way of Working Working?</b> (Sanne, vol. 2)"],
    quiz=[("How was each practice scored?", "On its own ladder, 1 (by hand) to 4 (automatic), together, with evidence."),
          ("Who took part?", "The reliability team with Ben, Cho, Dee, Sam, Joost's operations lead and Mo."),
          ("What were the weakest practices?", "Capacity forecasting, knowledge, store self-service, vendor management and cost (all 2), plus the people risk."),
          ("Which three were chosen?", "Knowledge, capacity forecasting, and the reliability team itself."),
          ("Should every practice aim for 4?", "No: each needs the level that's worth it.")],
    quiz_sit=[("In the check, Eli wants to score knowledge 3; Sam says support still asks Bram about six systems. What score goes down?", "2, with Sam's six systems as the evidence. That's why the check is done together: the people who depend on operations see what the builders don't.")],
    try_it="Pick ten practices from this notebook that you do. Score each 1–4 on its ladder with one piece of evidence, together with two people who depend on your work. Which three would you choose?",
    remember="Ask <span class=\"hl\">where you're weak</span>, together, with evidence, and work on <span class=\"hl\">three things</span>, not twenty.",
    sources=["AXELOS, <i>ITIL Maturity Model</i> (2021) and <i>ITIL 4: Continual improvement</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): on assessing SRE practices.",
             "DORA, <i>State of DevOps</i> reports: capabilities as a maturity lens."],
)

# ------------------------------------------------------------------ 10 Where Are We Going?
os_problem = Doodle(760, 260, "Doodle of the board's plan of 20 March 2028: eight cities and 60,000 orders a day by the end of 2028, more after. Operations has a register of improvements, a risk register, a maturity check and a new team. What it doesn't have is a page saying where operations is going and why, so every request (another tool, another city, another on-call) arrives as a separate fight.",
                    "The board's plan: eight cities, 60,000 orders a day. Operations: lots of lists, no page saying where it's going.")
os_problem.box(14, 30, 350, 100, "board plan, 20 Mar", "green", sub="8 cities · 60,000 orders / day", size=19, subsize=14)
os_problem.box(396, 30, 350, 100, "operations", "pink", sub="registers, checks, a team · no direction", size=19, subsize=13)
os_problem.note(380, 180, "every request arrives as a separate fight", "red", size=18)

os_analogy = Doodle(760, 220, "Doodle of a sailing club's plan for a long voyage: one page with the destination, the three things that must be true to get there (a sound boat, a trained crew, a safe route), and the legs of the journey with dates. Every decision on board is checked against that page.",
                    "One page: the destination, three things that must be true, and the legs with dates.")
os_analogy.icon("ship", 40, 50, 1.0)
os_analogy.row([("destination", None, "green"), ("3 must-be-trues", None, "y"), ("legs + dates", None, "blue")], x=170, y=50, h=80, w=180, gap=18, size=17)
os_analogy.note(450, 180, "every decision checked against one page", "pen", size=18)

os_how = Doodle(760, 400, "Larder's operations strategy on a page, signed by Femke on Monday 24 July 2028. Purpose: Larder keeps its promises at 60,000 orders a day, without heroics. Three goals for 18 months: tier 1 meets its SLOs at twice today's volume; a new city's IT in 5 days, self-service; no single person critical to operations. Principles: build it and run it, with help; automate the whole job; measure what users feel; practise failure. Roadmap: Q3 2028 the reliability team and Ordering's handover; Q4 Dispatch's readiness review and capacity forecasting; Q1 2029 Dispatch handover and payments review; Q2 2029 a second region decision against ADR 0026's triggers. Reviewed every quarter with the maturity check and the risk register.",
                "Purpose, three goals, four principles, a quarterly roadmap. Signed by Femke on 24 July 2028.")
os_how.box(14, 14, 732, 50, "purpose: Larder keeps its promises at 60,000 orders a day, without heroics", "green", size=15)
for i, t in enumerate(["tier 1 SLOs at 2× volume", "new city IT in 5 days, self-service", "no single person critical"]):
    os_how.box(14 + i * 248, 80, 236, 64, t, "y", size=14)
os_how.box(14, 160, 732, 50, "principles: build + run with help · automate the whole job · measure what users feel · practise failure", "blue", size=13)
os_how.row([("Q3 '28", "team + Ordering", "paper"), ("Q4 '28", "Dispatch review · forecasting", "paper"), ("Q1 '29", "Dispatch handover · payments", "paper"), ("Q2 '29", "second region?", "paper")], x=14, y=230, h=86, gap=20, size=15, subsize=11, arrows=True)
os_how.note(380, 352, "signed by Femke, Mon 24 July · reviewed quarterly", "pen", size=16)
os_how.note(380, 386, "requests are checked against the page, not fought one by one", "red", size=15)

OPS_STRATEGY = dict(
    slug="ops-strategy",
    kicker="a.k.a. “strategy management for operations”",
    tldr="An operations strategy is <b>one page</b>: a <b>purpose</b> tied to the business plan, <b>three goals</b> for the next year or two, a few <b>principles</b> that guide everyday choices, and a <b>quarterly roadmap</b>. It turns a pile of registers and requests into a direction, so decisions are checked against the page instead of fought one at a time. Get it <b>signed by leadership</b> and review it every quarter.",
    chips=[("Family", "setting direction"), ("Lives in", "ops/strategy.md, signed by Femke; reviewed quarterly"), ("Pairs with", "the maturity check, the risk register, Grace's strategy on a page")],
    itil=dict(groups=["general"], chain=["plan", "engage"], practices=["strategy management", "portfolio management"],
              sre="(SRE team charters and roadmaps)", principles=["Focus on value", "Think and work holistically"],
              older="ITIL v3: service strategy"),
    problem_side="Larder, July 2028",
    problem="""  <p class="lead">The board's plan of <b>20 March 2028</b> says <b>eight cities and 60,000 orders a day</b> by the end of 2028, and more after. Operations has an improvement register, a risk register, a maturity check and a new team. <span class="hl-pink">What it doesn't have is a page saying where operations is going, and why.</span> So every request (another tool, another city, another team wanting help with on-call) arrives as a separate negotiation.</p>
  <ul>
    <li>Lists of work aren't a direction.</li>
    <li>Leadership can't support what it hasn't seen on a page.</li>
    <li>The team can't say no without a reason everyone shares.</li>
  </ul>""",
    problem_figs=[os_problem],
    meanwhile=[("project-6", "programmes-and-portfolios", "Sanne's programme “Cities 2028” (from 10 January): Ghent, Haarlem, the launch office and the courier renewal; benefit: eight cities and 60,000 orders a day by the end of 2028.",
                "Eli's operations strategy for the same target: Larder keeps its promises at 60,000 orders a day, without heroics.")],
    analogy_side="the voyage plan",
    analogy="""  <p>A sailing club planning a long voyage writes <b>one page</b>: the <b>destination</b>, the <b>three things that must be true</b> to get there (a sound boat, a trained crew, a safe route), and the <b>legs of the journey with dates</b>. Every decision on board, from what to stow to which harbour to skip, is checked against that page.</p>""",
    analogy_figs=[os_analogy],
    map=[("The destination", "Purpose: promises kept at 60,000 orders a day, without heroics"),
         ("Three must-be-trues", "Three goals: SLOs at 2×, a city in 5 days, no single person critical"),
         ("How the crew works", "Four principles"),
         ("Legs with dates", "The quarterly roadmap"),
         ("Checked against the page", "Requests decided by the strategy")],
    how_side="purpose, three goals, principles, a quarterly roadmap, signed",
    how="""  <p>Eli writes the <b>operations strategy</b> on one page in July, and Femke signs it on <b>Monday 24 July</b>:</p>
  <ul>
    <li><b>Purpose</b>: Larder keeps its promises at 60,000 orders a day, <b>without heroics</b>.</li>
    <li><b>Three goals for 18 months</b>: tier 1 meets its SLOs at <b>twice today's volume</b>; a new city's IT in <b>5 days, self-service</b>; <b>no single person critical</b> to operations.</li>
    <li><b>Principles</b>: build it and run it, with help; automate the whole job; measure what users feel; practise failure.</li>
    <li><b>Roadmap</b>: Q3 2028, the reliability team and Ordering's handover; Q4, Dispatch's readiness review and capacity forecasting; Q1 2029, Dispatch's handover and a payments review; Q2 2029, a decision on a second region against ADR 0026's triggers.</li>
  </ul>
  <p>It's reviewed every quarter with the maturity check and the risk register. When Dee's team asks the reliability team to run the apps' on-call, the answer comes from the page: not tier 1, so build it and run it, <b>with help</b>. And the help comes the next week.</p>""",
    how_figs=[os_how],
    steps=[("Start from the business plan", "What must operations make possible?"),
           ("Write a purpose in one sentence", "In business words."),
           ("Choose three goals", "Measurable, 12–18 months."),
           ("Write a few principles", "For everyday choices."),
           ("Lay out a quarterly roadmap", "Tied to the goals and the top risks."),
           ("Get it signed and review quarterly", "And use it to answer requests.")],
    vocab=[("Strategy", "Where you're going, why, and how you'll choose what to do."),
           ("Purpose", "Why the team exists, in the business's words."),
           ("Goal", "A measurable result to reach in a set time."),
           ("Principle", "A rule of thumb for everyday choices."),
           ("Roadmap", "The order of big pieces of work over time."),
           ("Charter", "A team's agreed purpose and scope, signed by leadership.")],
    code=dict(file="ops/strategy.md", note="signed by Femke · Mon 24 July 2028", plain=True, src="""
# Operations strategy · 2028–2029

purpose     Larder keeps its promises at 60,000 orders a day, without heroics.
goals       1 tier 1 meets its SLOs at 2× today's volume          (by end 2029)
(18 months) 2 a new city's IT in 5 days, self-service              (Haarlem: 20 min set-up)
            3 no single person critical to operations              (risk R1 ≤ 2 × 4)
principles  build it and run it, with help · automate the whole job
            · measure what users feel · practise failure
roadmap     Q3 '28 reliability team · Ordering handover (1 Oct)
            Q4 '28 Dispatch readiness review · capacity forecasting
            Q1 '29 Dispatch handover · payments readiness review
            Q2 '29 second region? (ADR 0026 triggers: 60k/day, region > 1 h, a contract)
review      quarterly, with the maturity check and the risk register
"""),
    tools="tools: the board's plan, the maturity check, the risk register, one page and an hour with leadership.",
    ladder=[("lists, no direction", ["Every request a fight.", "Priorities by volume."]),
            ("a signed one-page strategy", ["Purpose, goals, principles, roadmap.", "Requests checked against it."]),
            ("strategy drives the portfolio", ["Budgets and hiring follow it.", "Teams' plans linked."]),
            ("strategy shared across teams", ["Product and operations goals aligned.", "Reviewed together."])],
    ladder_now=1,
    baseline="Each line compares <b>registers and requests without a direction</b> to <b>a signed one-page operations strategy with a quarterly roadmap</b>.",
    ratings=[(2, 3, "Work aimed at the promises customers feel."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone sees where operations is going."),
             (3, 3, "Neutral."),
             (2, 3, "Spending tied to goals."),
             (2, 3, "“No single person critical” is a goal, not a wish."),
             (3, 3, "One page, an hour a quarter.")],
    pitfalls=[("A long document", "Nobody reads it.", "one page."),
              ("Goals in IT words", "Leadership can't connect.", "business words and numbers."),
              ("Unsigned", "Ignored at the first conflict.", "signed by leadership."),
              ("Never used", "Requests still fought one by one.", "check every request against the page.")],
    use=["Operations has lots of work and no stated direction.", "A business plan changes the scale.", "A new team is forming.", "Requests keep turning into negotiations."],
    skip=["A tiny team with one obvious job."],
    related=["<b>Where Are We Weak?</b> (this volume)", "<b>Strategy on a Page</b> (Grace, vol. 2)", "<b>Which Risks Keep Us Up at Night?</b> (vol. 5)", "<b>Architecture Principles</b> (Ana, vol. 6)"],
    quiz=[("What's on Larder's operations strategy page?", "A purpose, three goals, four principles and a quarterly roadmap."),
          ("What's the purpose?", "Larder keeps its promises at 60,000 orders a day, without heroics."),
          ("Name the three goals.", "Tier 1 SLOs at 2× volume; a new city's IT in 5 days, self-service; no single person critical."),
          ("How did the strategy answer Dee's request?", "Not tier 1, so build it and run it, with help, and the help came."),
          ("How often is it reviewed?", "Every quarter, with the maturity check and the risk register.")],
    quiz_sit=[("Marketing asks the reliability team to run the new campaign microsite's on-call for Black Friday. What does the page say?", "It's not tier 1, so marketing's builders run it, with the reliability team's help (alerts, a runbook, a game day). The principles answer, not a negotiation.")],
    try_it="Write your team's purpose in one sentence of business words, three goals for the next year, and four principles. Which current request would the page answer differently from how you'd have answered it last week?",
    remember="One page: <span class=\"hl\">why, three goals, a few principles, the next legs</span>. Signed, reviewed quarterly, and used to answer every request.",
    sources=["Richard Rumelt, <i>Good Strategy / Bad Strategy</i> (2011).",
             "AXELOS, <i>ITIL 4: Strategy management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): SRE team charters."],
)

NOTES = [AUTOMATION, TOOLSET, MATURITY, OPS_STRATEGY]
