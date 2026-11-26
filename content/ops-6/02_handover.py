# Series 2 · Book 5 · The IT Operations Notebook · Vol. 6 · Handing over.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 6".

# ------------------------------------------------------------------ 04 Is This Service Ready for Production?
pr_problem = Doodle(760, 260, "Doodle of August 2028. The reliability team is to take Ordering's pager on 1 October. Ben's team says Ordering is ready: it's been in production for four years. Lotte, five weeks into the job, asks simple questions: which alerts page, and does each have a runbook? What's the restore time? What breaks if the address lookup vendor fails? Some answers are 'Ben knows'.",
                    "“It's been in production for four years.” Lotte's simple questions get “Ben knows” for an answer.")
pr_problem.box(14, 30, 300, 100, "“ready: 4 years in prod”", "y", sub="Ben's team", size=17, subsize=14)
pr_problem.box(346, 30, 400, 100, "Lotte's questions", "paper", sub="runbooks? restore time? vendor failure?", size=18, subsize=13)
pr_problem.note(380, 180, "answer: “Ben knows”", "red", size=20)

pr_analogy = Doodle(760, 220, "Doodle of a building handed over from the builder to the facilities team. Before the keys change hands, they walk every floor with a checklist: fire alarms tested, plans of the pipes and wires, manuals for the lift, spare parts, a list of known snags with dates. 'It's been standing for years' isn't on the list.",
                    "Before the keys change hands: alarms tested, plans, manuals, spares, a snag list with dates.")
pr_analogy.icon("cabinet", 60, 40, 1.4)
pr_analogy.box(170, 30, 576, 120, None, "paper")
for i, t in enumerate(["fire alarms tested ✓ · plans of pipes and wires ✓", "lift manual ✓ · spare parts ✓", "snags: 6, each with a date"]):
    pr_analogy.text(190, 64 + i * 32, t, anchor="start", size=16)
pr_analogy.note(450, 190, "a walk-through with a checklist, not a feeling", "pen", size=18)

pr_how = Doodle(760, 400, "Larder's production readiness review for Ordering, held on Monday 28 August 2028 by Bram, Lotte and Ben's team. 31 checks in seven areas: SLOs set and met for three months; alerts symptom-based, each with a tested runbook; dashboards per the standard; capacity headroom and the last load test; failover and restore tested within a month; dependencies mapped with vendor plans; rollback for every deploy type; known errors written down; on-call training done. Result: 25 met, 6 gaps: two alerts without runbooks, the address lookup vendor's failure untested, one dashboard missing, a slow-query runbook in Ben's head, the restore test older than a month. All six fixed by Monday 11 September. The template is reused for Dispatch in 2029.",
                "31 checks in seven areas, walked through together. 25 met, 6 gaps, fixed by 11 September.")
for i, t in enumerate(["SLOs met 3 months", "alerts + tested runbooks", "dashboards", "capacity + load test", "failover + restore ≤ 1 month", "dependencies + vendor plans", "rollbacks · known errors · training"]):
    r, c = divmod(i, 4)
    pr_how.box(14 + c * 186, 14 + r * 76, 172, 64, t, "blue", size=13)
pr_how.row([("28 Aug", "31 checks", "paper"), ("25 met", "6 gaps", "y"), ("11 Sep", "all 6 fixed", "green")], x=14, y=180, h=86, gap=40, size=19, subsize=14, arrows=True)
pr_how.note(380, 300, "gaps: 2 runbooks · vendor failure untested · a dashboard", "pen", size=15)
pr_how.note(380, 330, "a runbook in Ben's head · restore test > 1 month old", "pen", size=15)
pr_how.note(380, 366, "reused for Dispatch (2029)", "green", size=15)

READINESS = dict(
    slug="production-readiness",
    kicker="a.k.a. “production readiness review (PRR)”",
    tldr="Before a team takes on a service, <b>walk through it together with a checklist</b>: SLOs set and met, alerts with tested runbooks, dashboards, capacity, tested failover and restore, mapped dependencies, rollbacks, known errors, training. “It's been in production for years” isn't readiness. Turn every gap into an action with a date, and <b>don't take the pager until they're closed</b>. Reuse the checklist for every service after.",
    chips=[("Family", "handing over"), ("Lives in", "ops/readiness/checklist.md; one review file per service"), ("Pairs with", "who runs what, handing over the pager, Ana's go-live readiness")],
    itil=dict(groups=["service"], chain=["design", "build"], practices=["service design", "service validation and testing", "deployment management"],
              sre="“production readiness review (PRR)”", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: service transition: acceptance criteria and service acceptance"),
    problem_side="Larder, August 2028",
    problem="""  <p class="lead">The reliability team is to take Ordering's pager on <b>1 October</b>. Ben's team says Ordering is ready: <b>“it's been in production for four years”</b>. Lotte, five weeks into the job, asks simple questions. Which alerts page, and does each have a runbook? What's the restore time? What breaks if the address lookup vendor fails? <span class="hl-pink">Some of the answers are “Ben knows”.</span></p>
  <ul>
    <li>Age in production isn't readiness; it often hides tacit knowledge.</li>
    <li>A team taking over inherits every gap at 3 a.m.</li>
    <li>Without a checklist, “ready” is an argument.</li>
  </ul>""",
    problem_figs=[pr_problem],
    meanwhile=[("architect-6", "handover-to-operations", "Ana's handover of Ordering to the reliability team: runbooks, alerts, practice and a warranty period; game days 14 and 21 Sep, pager 1 Oct.",
                "Eli's side of the same handover: the readiness review the reliability team ran first, 31 checks, 6 gaps closed by 11 September.")],
    analogy_side="the building handover",
    analogy="""  <p>When a builder hands a building to the facilities team, they <b>walk every floor with a checklist</b> before the keys change hands: fire alarms tested, plans of the pipes and wires, manuals for the lift, spare parts, a list of known snags with dates. “It's been standing for years” isn't on the list.</p>""",
    analogy_figs=[pr_analogy],
    map=[("Walking every floor", "Walking through the service together"),
         ("Fire alarms tested", "Alerts with tested runbooks"),
         ("Plans of pipes and wires", "Dependency map with vendor plans"),
         ("Spare parts and manuals", "Rollbacks, restore tests, known errors"),
         ("Snag list with dates", "Six gaps, each fixed by 11 September")],
    how_side="31 checks, walked through together, gaps closed before the pager moves",
    how="""  <p>On <b>Monday 28 August</b>, Bram and Lotte hold the readiness review with Ben's team. It covers <b>31 checks in seven areas</b>:</p>
  <ul>
    <li><b>SLOs</b> set and met for three months.</li>
    <li><b>Alerts</b> symptom-based, each with a <b>tested runbook</b>.</li>
    <li><b>Dashboards</b> per the standard.</li>
    <li><b>Capacity</b> headroom and the last load test.</li>
    <li><b>Failover and restore</b> tested within a month.</li>
    <li><b>Dependencies</b> mapped, with vendor plans.</li>
    <li><b>Rollback</b> for every kind of deploy, <b>known errors</b> written down, <b>on-call training</b> done.</li>
  </ul>
  <p>The result is <b>25 met, 6 gaps</b>: two alerts without runbooks, the address lookup vendor's failure never tested, one dashboard missing, a slow-query fix that lived only in Ben's head, and a restore test older than a month. All six are fixed by <b>Monday 11 September</b>. The pager doesn't move until they are. The checklist becomes the template for Dispatch in 2029, and for any team that wants a review of its own service.</p>""",
    how_figs=[pr_how],
    steps=[("Write a checklist of what “ready” means", "SLOs, alerts, runbooks, capacity, recovery, dependencies."),
           ("Walk through it together", "Both teams, the real service."),
           ("Answer with evidence, not memory", "“Ben knows” is a gap."),
           ("Turn gaps into dated actions", "Owned by the building team."),
           ("Don't move the pager until they're closed", "Or agree the exceptions in writing."),
           ("Reuse the checklist", "For every service after.")],
    vocab=[("Production readiness review (PRR)", "A structured check that a service can be run reliably by its future operators."),
           ("Acceptance criteria", "Conditions a service must meet before it's taken over."),
           ("Tacit knowledge", "What someone knows but hasn't written down."),
           ("Gap", "A check not met, with an owner and a date."),
           ("Warranty period", "A time after handover when the building team still helps (next notes)."),
           ("Template", "The reusable checklist for the next service.")],
    code=dict(file="ops/readiness/ordering-2028-08.md", note="review Mon 28 Aug 2028 · Bram, Lotte, Ben's team", plain=True, src="""
area           checks   met   gaps (owner · date)
SLOs           3        3
alerts         6        4     2 alerts without runbooks (Ben · 4 Sep ✓)
dashboards     3        2     business ordering dashboard (Ben · 4 Sep ✓)
capacity       4        4
recovery       5        4     restore test > 1 month old (Bram · 5 Sep ✓)
dependencies   5        4     address lookup failure untested (Lotte · 7 Sep ✓, game day)
rollback etc.  5        4     slow-query fix only in Ben's head → RB-31 (Ben · 11 Sep ✓)
total          31       25    6 gaps, all closed by Mon 11 Sep
next           game days 14 + 21 Sep · pager 1 Oct
"""),
    tools="tools: a checklist in the repo, two afternoons together, and the catalogue, runbooks and test logs as evidence.",
    ladder=[("“it's been in production for years”", ["Ready by assumption.", "Gaps found at 3 a.m."]),
            ("a readiness review before any handover", ["31 checks, gaps closed first.", "Reused."]),
            ("readiness continuously checked", ["The review's checks run automatically.", "Readiness visible on each service page."]),
            ("ready by default", ["New services are born meeting the checklist (golden path).", "Reviews confirm, not discover."])],
    ladder_now=1,
    baseline="Each line compares <b>taking over a service because it's old</b> to <b>a 31-check readiness review with gaps closed first</b>.",
    ratings=[(2, 3, "Fewer surprises after the handover."),
             (2, 4, "Untested failures tested before taking over."),
             (2, 4, "Every alert has a runbook."),
             (3, 3, "Neutral."),
             (2, 4, "Ready means something written."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "The new team isn't paged into unknowns."),
             (3, 3, "Two afternoons and two weeks of fixes.")],
    pitfalls=[("Age as readiness", "Old services hide the most tacit knowledge.", "walk the checklist."),
              ("Answers from memory", "“Ben knows” at 3 a.m. is no answer.", "evidence for every check."),
              ("Taking the pager with open gaps", "The new team inherits them.", "close them first, or agree in writing."),
              ("A checklist used once", "Each review starts from scratch.", "reuse and improve it.")],
    use=["A team is taking over a service.", "A service goes live for the first time.", "Before a major launch.", "When a team asks “are we ready?”"],
    skip=["Tiny internal tools with no on-call."],
    related=["<b>Handover to Operations</b> (Ana, vol. 6)", "<b>Go-Live Readiness</b> (Ana, vol. 6)", "<b>Handing Over the Pager</b> (next note)", "<b>Who Runs What?</b> (this volume)"],
    quiz=[("What does a readiness review check?", "SLOs met, alerts with tested runbooks, dashboards, capacity, failover and restore, dependencies, rollbacks, known errors, training."),
          ("Why isn't “four years in production” readiness?", "Old services often hide tacit knowledge and untested failures."),
          ("What did Ordering's review find?", "25 of 31 met; 6 gaps, including a fix only in Ben's head and an untested vendor failure."),
          ("When does the pager move?", "Only after the gaps are closed (by 11 September), then game days, then 1 October."),
          ("What happens to the checklist?", "It's reused for Dispatch in 2029 and any team that wants it.")],
    quiz_sit=[("Two days before the pager handover, one runbook is still missing for a rare alert. Ben says “it never fires”. What do you do?", "Either Ben writes it now (an hour), or both sides agree in writing that it's an accepted gap with a date and Ben's team stays first line for that alert until it's done. “Never fires” is what people say about the alert that fires on the first weekend.")],
    try_it="Pick a service someone else might one day run. Walk through it with the seven areas and count the checks you could answer with evidence, not memory. What's in one person's head?",
    remember="Ready is a <span class=\"hl\">checklist walked together</span>, not years in production. Close the gaps <span class=\"hl\">before</span> the pager moves.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 32, the evolving SRE engagement model (PRR).",
             "Susan Fowler, <i>Production-Ready Microservices</i> (2016).",
             "AXELOS, <i>ITIL 4: Service validation and testing</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 05 Handing Over the Pager
ph_problem = Doodle(760, 260, "Doodle of the simplest plan for moving Ordering's on-call: on Sunday 1 October, swap the schedule in the paging tool. Ben's team stops being paged; the reliability team starts. Lotte joined in July, Yusuf in August. Neither has ever handled a real Ordering incident. Ben worries; so does Femke, remembering Christmas 2026.",
                    "The simplest plan: swap the schedule on 1 October. Two of the four new people have never seen an Ordering incident.")
ph_problem.box(14, 30, 300, 100, "1 Oct: swap schedule", "pink", sub="all at once", size=19, subsize=14)
ph_problem.box(346, 30, 400, 100, "Lotte (Jul) · Yusuf (Aug)", "y", sub="never handled an Ordering incident", size=18, subsize=13)
ph_problem.note(380, 180, "a big bang for the most critical service", "red", size=19)

ph_analogy = Doodle(760, 220, "Doodle of a new driving instructor taking over a school bus route. First they ride along and watch the old driver. Then they drive while the old driver sits beside them. Then they practise the hard bits (a breakdown, a missing child) in the depot. Only then do they drive alone, with the old driver's phone number in their pocket.",
                    "Ride along, then drive with the old driver beside you, practise the hard bits, then drive alone.")
ph_analogy.row([("ride along", None, "blue"), ("drive, watched", None, "y"), ("practise the hard bits", None, "pink"), ("drive alone", "old driver on the phone", "green")], y=50, h=86, gap=14, size=16, subsize=12)
ph_analogy.note(380, 186, "responsibility moves in steps", "pen", size=18)

ph_how = Doodle(760, 400, "How Ordering's pager moved, September 2028. Shadow, 4 to 17 September: the reliability team gets every Ordering page alongside Ben's team, and watches and asks. Reverse shadow, 18 to 30 September: the reliability team is primary, Ben's team is secondary and steps in only if asked. Game days on Thursdays 14 and 21 September: a failed deploy, the database failover, the address lookup vendor down, a major-incident drill; Lotte and Yusuf lead. Handover on 1 October: the reliability team is primary, Ben's team second line. Way back: if two SEV1s or the error budget spent in October, Ben's team returns as primary while gaps are fixed.",
                "Shadow, reverse shadow, two game days, then a date, with a way back written in advance.")
ph_how.row([("4–17 Sep", "shadow", "blue"), ("18–30 Sep", "reverse shadow", "y"), ("14 + 21 Sep", "game days", "pink"), ("1 Oct", "reliability primary", "green")], y=14, h=96, gap=36, size=17, subsize=13, arrows=True)
ph_how.box(14, 136, 732, 110, None, "paper")
ph_how.text(380, 166, "game days: a failed deploy · DB failover · address lookup down", size=14)
ph_how.text(380, 194, "· a major-incident drill · led by Lotte and Yusuf", size=14)
ph_how.text(380, 226, "Ben's team: second line from 1 Oct", size=14)
ph_how.box(14, 268, 732, 64, "way back: 2 SEV1s or budget spent in October → Ben's team primary again", "pink", size=14)
ph_how.note(380, 366, "nobody on the new rota takes their first real page alone", "pen", size=15)

PAGER_HANDOVER = dict(
    slug="pager-handover",
    kicker="a.k.a. “transitioning operational responsibility”",
    tldr="Don't move on-call for a critical service in one swap. Move it in steps. <b>Shadow</b>: the new team gets every page and watches. <b>Reverse shadow</b>: the new team is primary, the old team backs them up. <b>Game days</b> practise the hard incidents. Then <b>a date</b>, with the old team as second line and a <b>way back written in advance</b>. Nobody should take their first real page for a critical service alone.",
    chips=[("Family", "handing over"), ("Lives in", "ops/readiness/ordering-handover.md; the paging tool's schedules"), ("Pairs with", "production readiness, early life support, game days (vol. 5)")],
    itil=dict(groups=["service", "general"], chain=["design", "deliver"], practices=["deployment management (of responsibility)", "workforce and talent management", "service continuity management"],
              sre="(shadow / reverse shadow on-call onboarding)", principles=["Progress iteratively with feedback"],
              older="ITIL v3: service transition, early life support"),
    problem_side="Larder, August 2028",
    problem="""  <p class="lead">The simplest plan for moving Ordering's on-call: on <b>1 October</b>, swap the schedule in the paging tool. Ben's team stops being paged, and the reliability team starts. But <b>Lotte</b> joined in July and <b>Yusuf</b> in August, and <span class="hl-pink">neither has ever handled a real Ordering incident</span>. Ben is worried. So is Femke, who remembers Christmas 2026.</p>
  <ul>
    <li>A big-bang swap puts the least experienced people on the most critical service.</li>
    <li>Knowledge moves by doing, not by reading.</li>
    <li>If it goes wrong, nobody has agreed how to step back.</li>
  </ul>""",
    problem_figs=[ph_problem],
    analogy_side="taking over a school bus route",
    analogy="""  <p>A new driver taking over a school bus route first <b>rides along</b> and watches. Then they <b>drive while the old driver sits beside them</b>. Then they <b>practise the hard bits</b> in the depot: a breakdown, a missing child. Only then do they <b>drive alone</b>, with the old driver's phone number in their pocket.</p>""",
    analogy_figs=[ph_analogy],
    map=[("Riding along", "Shadow: every page, watching"),
         ("Driving with the old driver beside you", "Reverse shadow: primary, with Ben's team as backup"),
         ("Practising breakdowns in the depot", "Game days on 14 and 21 September"),
         ("Driving alone", "Primary from 1 October"),
         ("The old driver's number", "Ben's team as second line, and a way back")],
    how_side="shadow, reverse shadow, game days, a date, a way back",
    how="""  <p>Eli and Ben plan the handover in steps through <b>September</b>:</p>
  <ul>
    <li><b>Shadow</b>, 4–17 September: the reliability team gets <b>every Ordering page</b> alongside Ben's team. They watch, ask and update runbooks.</li>
    <li><b>Reverse shadow</b>, 18–30 September: the reliability team is <b>primary</b>. Ben's team is secondary and steps in only if asked.</li>
    <li><b>Game days</b>, Thursdays <b>14 and 21 September</b>: a failed deploy, the database failover, the address lookup vendor down, and a major-incident drill. <b>Lotte and Yusuf lead</b>, and Eli only watches.</li>
    <li><b>1 October</b>: the reliability team is primary for Ordering, and Ben's team is <b>second line</b>.</li>
    <li><b>Way back</b>, written in advance: if there are two SEV1s, or the error budget is spent in October, Ben's team returns as primary while gaps are fixed.</li>
  </ul>
  <p>By 1 October everyone on the reliability rota has handled at least three real Ordering pages with someone beside them. Nobody takes their first real page alone.</p>""",
    how_figs=[ph_how],
    steps=[("Close the readiness gaps first", "Previous note."),
           ("Shadow for two weeks", "Every page, both teams."),
           ("Reverse shadow for two weeks", "New team primary, old team backing up."),
           ("Practise the hard incidents", "Game days led by the newest people."),
           ("Hand over on a date", "Old team as second line."),
           ("Write the way back first", "Conditions both sides agree.")],
    vocab=[("Shadowing", "Receiving pages and watching, without being responsible."),
           ("Reverse shadowing", "Being responsible, with an experienced person backing you up."),
           ("Transition", "Moving a service, or responsibility for it, from one state or team to another."),
           ("Second line", "The team called for deeper knowledge after the first responder."),
           ("Way back", "The agreed conditions for returning responsibility."),
           ("Game day", "A planned exercise of failures and responses (vol. 5).")],
    code=dict(file="ops/readiness/ordering-handover.md", note="September 2028 · Eli and Ben", plain=True, src="""
# Ordering on-call: reliability team takes over

4–17 Sep    SHADOW          every Ordering page → both rotas · reliability watches, asks
18–30 Sep   REVERSE SHADOW  reliability primary · Ordering secondary (asked, not assumed)
Thu 14 Sep  game day 1      failed deploy · DB failover · leads: Lotte, Yusuf
Thu 21 Sep  game day 2      address lookup down · major-incident drill · leads: Yusuf, Lotte
1 Oct       HANDOVER        reliability team primary · Ordering second line
way back    2 × SEV1 or error budget spent in Oct → Ordering primary again while fixed
check       every reliability rota member: ≥ 3 real Ordering pages with someone beside them ✓
"""),
    tools="tools: the paging tool's schedules (both rotas paged in shadow), game day plans, and one page agreed by both teams.",
    ladder=[("swap the schedule", ["Big bang.", "First page alone."]),
            ("shadow, reverse shadow, game days, a date", ["Way back written.", "Old team second line."]),
            ("the steps as a template", ["Every handover uses them.", "Readiness and transition one process."]),
            ("handovers boring", ["Teams move services calmly.", "Ways back rarely used."])],
    ladder_now=1,
    baseline="Each line compares <b>swapping the schedule on a date</b> to <b>shadow, reverse shadow, game days, a date and a way back</b>.",
    ratings=[(2, 4, "Customers don't notice the handover."),
             (3, 3, "Neutral."),
             (2, 4, "The new team has practised the hard incidents."),
             (3, 3, "Neutral."),
             (2, 4, "Both teams know who's primary when."),
             (3, 3, "Neutral."),
             (3, 3, "Four weeks of double paging."),
             (2, 4, "Nobody's first page is alone."),
             (3, 3, "A month of steps.")],
    pitfalls=[("A big-bang swap", "First page alone, on the most critical service.", "steps."),
              ("Shadowing without asking", "Watching without learning.", "ask and update runbooks during shadow."),
              ("Game days led by the experts", "The new people only watch.", "the newest lead."),
              ("No way back", "A bad October becomes a crisis.", "write the conditions first.")],
    use=["Moving on-call for a service between teams.", "New people joining a critical rota.", "Before taking over a vendor's or another team's service.", "After a readiness review."],
    skip=["Low-tier services: a handover meeting and a runbook review may do."],
    related=["<b>Is This Service Ready for Production?</b> (this volume)", "<b>Did the Handover Work?</b> (next note)", "<b>Breaking Things on Purpose</b> (vol. 5)", "<b>Can Someone Else Run This?</b> (Sanne, vol. 6)"],
    quiz=[("What are the steps of Larder's pager handover?", "Shadow, reverse shadow, game days, a handover date, and a way back."),
          ("What's the difference between shadow and reverse shadow?", "In shadow, the new team watches; in reverse shadow, it's primary with the old team backing up."),
          ("Who led the game days?", "Lotte and Yusuf, the newest people; Eli only watched."),
          ("What's Ben's team's role after 1 October?", "Second line."),
          ("What's the way back?", "Two SEV1s or the error budget spent in October → Ben's team primary again while gaps are fixed.")],
    quiz_sit=[("During reverse shadow Yusuf is paged at 02:00 and doesn't call Ben's secondary, though he's unsure. It goes fine. What do you say in the morning?", "Well done for handling it; and next time, call: that's what reverse shadow is for. Unsure at 02:00 is exactly when to use the backup, and it costs nothing.")],
    try_it="Pick a service whose on-call you'd like to move. Write the four steps with dates: shadow, reverse shadow, game days, handover, plus the way back. Who would lead the game days?",
    remember="Move a pager <span class=\"hl\">in steps</span>: watch, drive with help, practise, then alone, with <span class=\"hl\">a way back</span> written first.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 28, accelerating SREs to on-call.",
             "AXELOS, <i>ITIL 4: Deployment management</i> and <i>Workforce and talent management</i> practice guides (2020).",
             "PagerDuty, <i>On-Call Onboarding</i> (open documentation): shadowing."],
)

# ------------------------------------------------------------------ 06 Did the Handover Work?
el_problem = Doodle(760, 260, "Doodle of 2 October 2028, the day after the handover. The plan ended at 'pager moves'. Nobody has said how anyone would know it worked: when Ben's team stops being second line by default, when the extra checks end, or what would count as success. Femke asks Eli at the Monday meeting: 'So, is it done?'",
                    "The plan ended at “pager moves”. On day two, Femke asks: “so, is it done?”")
el_problem.box(14, 30, 340, 100, "1 Oct: pager moved", "green", size=20)
el_problem.box(396, 30, 350, 100, "“is it done?”", "pink", sub="how would anyone know?", size=20, subsize=14)
el_problem.note(380, 180, "no exit test · no end date · no measure of success", "red", size=18)

el_analogy = Doodle(760, 220, "Doodle of a patient going home after an operation. The hospital doesn't just discharge them: a nurse calls daily for the first week, there's a check-up after two weeks, and a clear sign that recovery is complete: walking unaided, wound healed. Then the follow-up ends.",
                    "After the operation: daily calls the first week, a check-up at two weeks, and a clear sign it's healed.")
el_analogy.row([("daily calls", "week 1", "blue"), ("check-up", "week 2", "y"), ("healed?", "clear signs", "green"), ("follow-up ends", None, "paper")], y=40, h=96, gap=14, size=17, subsize=13)
el_analogy.note(380, 186, "care continues until the signs say it's done", "pen", size=18)

el_how = Doodle(760, 400, "Larder's early life support for Ordering, 1 to 31 October 2028. Ben's team stays second line and joins a 10-minute check-in every day in the first week, then twice a week. Every page is reviewed the next morning and its runbook updated if needed. Exit test: four weeks without a SEV1; the reliability team handles at least two incidents without calling Ben's team; every page in October has a runbook; SLOs met. The first incident: Monday 9 October, checkout slow after a deploy; Lotte leads, Yusuf fixes, the deploy is rolled back, 18 minutes from page to normal; Eli is in a meeting and reads about it afterwards. Exit on 31 October: all four met. Ben's team goes back to being second line only when asked.",
                "A month of extra care with an exit test. 9 October: the first incident without Eli, 18 minutes. Exit met on 31 October.")
el_how.box(14, 14, 360, 120, "October", "blue", sub="daily 10-min check-in wk 1 · then twice a week · every page reviewed", size=19, subsize=12)
el_how.box(386, 14, 360, 120, "exit test", "y", sub="4 weeks no SEV1 · 2 incidents alone · runbooks · SLOs", size=19, subsize=12)
el_how.box(14, 160, 732, 100, None, "green")
el_how.head(380, 190, "Mon 9 Oct · first incident without Eli", size=17)
el_how.text(380, 220, "checkout slow after a deploy · Lotte leads · Yusuf rolls back", size=14)
el_how.text(380, 246, "18 minutes · Eli reads about it afterwards", size=14)
el_how.note(380, 300, "31 Oct: exit test met (4 of 4)", "green", size=17)
el_how.note(380, 336, "Ben's team: second line when asked", "pen", size=16)

EARLY_LIFE = dict(
    slug="early-life-support",
    kicker="a.k.a. “early life support and hypercare”",
    tldr="A handover isn't finished when the pager moves. Plan a period of <b>early life support</b>: the old team stays close as second line, there are <b>short, frequent check-ins</b>, and every page is reviewed. Write an <b>exit test</b> in advance (weeks without a major incident, incidents handled alone, runbooks complete, SLOs met), so “is it done?” has an answer. The best sign of success is an incident handled well <b>without the people who used to be essential</b>.",
    chips=[("Family", "handing over"), ("Lives in", "ops/readiness/ordering-els.md; the check-in calendar"), ("Pairs with", "handing over the pager, production readiness, Grace's hypercare")],
    itil=dict(groups=["service"], chain=["deliver", "improve"], practices=["deployment management", "incident management", "service level management"],
              sre="(a stabilisation period after a transition)", principles=["Progress iteratively with feedback"],
              older="ITIL v3: early life support (ELS)"),
    pager=dict(when="Mon 9 Oct 2028 · Lotte primary, Yusuf secondary", lines=[
        ("17:42", "<b>PAGE</b> checkout p95 2.4 s (SLO burn: fast) · ordering"),
        ("17:43", "Lotte ack · declares SEV2 · leads; Yusuf fixes"),
        ("17:45", "change feed: deploy core v1207 at 17:31 (Ordering team)"),
        ("17:49", "Yusuf: rollback to v1206 (way back in the deploy line)"),
        ("17:56", "p95 back to 610 ms · error budget burn stops"),
        ("18:00", "SEV2 closed · 18 min · Ben's team told; not called"),
        ("18:20", "Eli, out of a meeting, reads the channel")]),
    problem_side="Larder, Monday 2 October 2028",
    problem="""  <p class="lead">The day after the handover, Femke asks Eli at the Monday meeting: <b>“So, is it done?”</b> The plan ended at “pager moves”. <span class="hl-pink">Nobody has said how anyone would know it worked</span>: when Ben's team stops being on standby by default, when the extra checks end, or what success would even look like.</p>
  <ul>
    <li>Without an end, the old team never really lets go.</li>
    <li>Without checks, small gaps grow quietly.</li>
    <li>Without a test, “done” is a feeling.</li>
  </ul>""",
    problem_figs=[el_problem],
    meanwhile=[("product-3", "hypercare", "Grace's hypercare after launch: two weeks of daily watching and fast fixes, with clear exit criteria (Rotterdam: tickets under 3 per 100 for two days, no P1 for five days).",
                "Eli's version for a team handover: a month of check-ins, every page reviewed, and an exit test met on 31 October.")],
    analogy_side="going home after an operation",
    analogy="""  <p>A hospital doesn't just discharge a patient after an operation. A nurse <b>calls daily for the first week</b>, there's a <b>check-up at two weeks</b>, and a <b>clear sign</b> that recovery is complete: walking unaided, the wound healed. Then the follow-up ends, on purpose, not because everyone forgot.</p>""",
    analogy_figs=[el_analogy],
    map=[("Daily calls the first week", "A 10-minute check-in every day in week 1"),
         ("The two-week check-up", "Twice-weekly check-ins, then the exit review"),
         ("Clear signs of recovery", "The exit test: no SEV1, incidents alone, runbooks, SLOs"),
         ("Walking unaided", "9 October, handled without Eli or Ben's team"),
         ("Follow-up ends", "31 October: Ben's team second line only when asked")],
    how_side="a month of close care, and an exit test written first",
    how="""  <p>Eli writes early life support for <b>October</b>, agreed with Ben:</p>
  <ul>
    <li>Ben's team stays <b>second line</b>, and joins a <b>10-minute check-in</b> every day in the first week, then twice a week.</li>
    <li><b>Every page is reviewed</b> the next morning, and its runbook is updated if anything was missing.</li>
    <li><b>Exit test</b>, written on 2 October: four weeks without a SEV1; the reliability team handles <b>at least two incidents without calling Ben's team</b>; every page in October has a runbook; SLOs met.</li>
  </ul>
  <p>The first incident comes on <b>Monday 9 October</b>: checkout slows after a deploy at 17:31. <b>Lotte</b> leads and <b>Yusuf</b> rolls the deploy back using the way back in its deploy line. It's <b>18 minutes</b> from page to normal. <b>Eli is in a meeting</b> and reads about it afterwards. It's the moment the whole book has been working towards. On <b>31 October</b> the exit test is met, all four parts, and Ben's team goes back to being second line only when asked.</p>""",
    how_figs=[el_how],
    steps=[("Plan the weeks after the handover", "Not just the day."),
           ("Keep the old team close, as second line", "With a clear role."),
           ("Check in briefly and often, then less", "Daily, then twice a week."),
           ("Review every page", "And fix the runbook the next morning."),
           ("Write the exit test on day one", "Measurable, agreed by both teams."),
           ("End it on purpose", "Say so, and celebrate the first incident handled alone.")],
    vocab=[("Early life support", "Extra support and monitoring just after a service or responsibility is handed over."),
           ("Hypercare", "Another name for a period of intensive support after a launch."),
           ("Exit test", "Agreed conditions that end early life support."),
           ("Stabilisation", "Getting to steady, predictable operation."),
           ("Check-in", "A short, regular meeting during the support period."),
           ("Letting go", "The old team stepping back on purpose.")],
    code=dict(file="ops/readiness/ordering-els.md", note="1–31 October 2028 · exit test written 2 October", plain=True, src="""
# Early life support · Ordering (reliability team primary)

check-ins     daily 09:30, 10 min (2–6 Oct) · then Tue + Thu (to 31 Oct)
page review   every page, next morning · runbook updated if anything was missing
exit test     [✓] 4 weeks without a SEV1
              [✓] ≥ 2 incidents handled without calling Ordering (9 Oct, 23 Oct)
              [✓] every October page had a runbook (17 of 17)
              [✓] SLOs met (checkout 99.94 %, speed 96.2 %)
9 Oct         SEV2 · checkout slow after deploy v1207 · Lotte leads, Yusuf rolls back
              18 min · Ordering told, not called · Eli not involved
31 Oct        exit met → Ordering second line when asked
"""),
    tools="tools: a calendar of check-ins, the page review, the incident list and one agreed exit test.",
    ladder=[("handover = pager moves", ["No end, no test.", "The old team never lets go."]),
            ("early life support with an exit test", ["Close care, then an end on purpose.", "Every page reviewed."]),
            ("the same for every transition", ["Launches, handovers and migrations share it.", "Exit tests reused."]),
            ("transitions are routine", ["Short support periods.", "Exit tests almost always met."])],
    ladder_now=1,
    baseline="Each line compares <b>a handover that ends when the pager moves</b> to <b>a month of early life support with an exit test written first</b>.",
    ratings=[(2, 4, "No SEV1 in the first month."),
             (2, 3, "Gaps found by page reviews, not outages."),
             (2, 4, "18 minutes, handled alone."),
             (3, 3, "Neutral."),
             (2, 4, "“Is it done?” has an answer."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Ben's team lets go on purpose."),
             (3, 3, "A month of short check-ins.")],
    pitfalls=[("No exit test", "Support never ends, or ends by neglect.", "write it on day one."),
              ("The old team as first line in disguise", "They're called for everything.", "second line, asked not assumed."),
              ("Skipping page reviews", "Small gaps grow.", "every page, next morning."),
              ("Not marking the end", "Nobody knows it's over.", "say so, and celebrate.")],
    use=["After any handover of responsibility.", "After a launch or migration.", "When a new team takes on-call.", "When leadership asks “is it done?”"],
    skip=["Tiny changes with no new people or responsibilities."],
    related=["<b>Handing Over the Pager</b> (this volume)", "<b>Hypercare after Launch</b> (Grace, vol. 3)", "<b>Who Looks After It Now?</b> (Sanne, vol. 2)", "<b>Was It a Change?</b> (vol. 2)"],
    quiz=[("What is early life support?", "A period of extra support and checking just after a handover, ending with an exit test."),
          ("What was Larder's exit test?", "Four weeks without a SEV1, two incidents handled alone, every page with a runbook, SLOs met."),
          ("What happened on 9 October?", "Checkout slowed after a deploy; Lotte led, Yusuf rolled back; 18 minutes; Eli wasn't involved."),
          ("Why write the exit test on day one?", "So “done” is measurable and agreed, not a feeling."),
          ("What's Ben's team's role after 31 October?", "Second line, only when asked.")],
    quiz_sit=[("In week three the reliability team calls Ben's team for every database question, even easy ones. The exit test says “two incidents without calling them”. What do you do?", "Look at why: missing runbooks or confidence? Write the runbooks, pair on the next questions, and keep early life support going past 31 October if needed. Ending on time matters less than ending for the right reasons.")],
    try_it="Think of a recent handover or launch. When did the extra support end, and how did anyone know it had worked? Write an exit test you could have used.",
    remember="A handover ends when <span class=\"hl\">the exit test is met</span>, not when the pager moves. The real sign: an incident <span class=\"hl\">handled well without you</span>.",
    sources=["AXELOS, <i>ITIL 4: Deployment management</i> practice guide (2020): early life support.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 18, SRE engagement.",
             "Michael Watkins, <i>The First 90 Days</i> (2013): on transitions."],
)

NOTES = [READINESS, PAGER_HANDOVER, EARLY_LIFE]
