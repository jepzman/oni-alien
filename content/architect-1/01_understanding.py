# Series 2 · The Solution Architect's Notebook · Vol. 1 · Understanding the problem.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Stakeholder Map
sh_problem = Doodle(760, 280, "Doodle of Ana's first design review at Larder. Product and engineering approve the multi-city design. Then three people who were never asked raise late surprises: Lena the data protection officer says customer data can't go to the new analytics tool without a contract, Tomás the store manager says pickers wear gloves so the new scanning flow won't work, and Marco the CFO asks why the cloud estimate doubled. The result is three weeks of rework.",
                    "Approved by everyone in the room, then blocked by the people who weren't in it.")
sh_problem.box(20, 40, 210, 90, "multi-city design v1", "blue", sub="✓ product  ✓ engineering", size=17, subsize=15)
sh_problem.arrow(236, 85, 286, 85, dash=True, label="week 3", lx=261, ly=71)
for i, (who, said) in enumerate([("Lena · DPO", "“no contract for that data”"), ("Tomás · store", "“pickers wear gloves”"), ("Marco · CFO", "“why is the bill ×2?”")]):
    y = 20 + i * 62
    sh_problem.box(292, y, 290, 50, None, "pink", stroke="red")
    sh_problem.head(306, y + 22, who, anchor="start", size=16, color="red")
    sh_problem.text(306, y + 42, said, anchor="start", size=16)
sh_problem.arrow(588, 106, 632, 106, color="red")
sh_problem.box(638, 66, 110, 80, "3 weeks", "pink", sub="of rework", stroke="red", size=19, subsize=15)
sh_problem.note(380, 240, "nobody had asked them: they weren't “stakeholders” in anyone's head", "red")

sh_analogy = Doodle(760, 300, "Doodle of planning a street party on a power and interest grid. The council can cancel it but cares little, so keep them satisfied with the permit. The organising committee has both power and interest, so manage them closely. The neighbours care a lot but can't stop it, so keep them informed. The bus company whose route passes by only needs monitoring and a notice.",
                     "A street party: the council can cancel it, the neighbours have to live with it. Treat them differently.")
sh_analogy.line("M90 20 V270 H740", thin=True)
sh_analogy.arrow(90, 270, 90, 16)
sh_analogy.arrow(90, 270, 744, 270)
sh_analogy.text(46, 145, "power", "t-s", size=18)
sh_analogy.note(415, 296, "interest →", size=18)
sh_analogy.line("M415 24 V266 M94 145 H736", dash=True, thin=True)
for (x, y, title, who, fill, ic) in [(100, 30, "keep satisfied", "the council (permit)", "blue", "stamp"),
                                    (425, 30, "manage closely", "organising committee", "green", "board"),
                                    (100, 155, "monitor", "the bus company", "paper", "truck"),
                                    (425, 155, "keep informed", "the neighbours", "y", "store")]:
    sh_analogy.box(x, y, 305, 104, None, fill)
    sh_analogy.head(x + 92, y + 40, title, anchor="start", size=19)
    sh_analogy.text(x + 92, y + 70, who, anchor="start", size=16)
    sh_analogy.icon(ic, x + 14, y + 26, 1.0)

sh_how = Doodle(760, 330, "Larder's stakeholder map on the same grid. Manage closely: Femke the CEO, Joost in operations, Priya in product and Marco the CFO. Keep satisfied: Lena the data protection officer and the investors. Keep informed: Tomás and the pickers, Sam in support, the couriers and the engineering teams. Monitor: the StockPilot vendor and the payment provider. Each name gets a way of working: a weekly review, a monthly note, a demo or a ticket.",
                 "Larder's map in week one, with how Ana works with each group.")
sh_how.line("M70 20 V300 H740", thin=True)
sh_how.text(36, 160, "power", "t-s", size=18)
sh_how.note(405, 326, "interest →", size=18)
sh_how.line("M405 24 V296 M74 160 H736", dash=True, thin=True)
quads = [(84, 28, "keep satisfied", "blue", ["Lena · DPO", "investors (board)"], "monthly 1:1 · early review"),
         (415, 28, "manage closely", "green", ["Femke · CEO", "Joost · ops", "Priya · product", "Marco · CFO"], "weekly 30-min review"),
         (84, 172, "monitor", "paper", ["StockPilot (vendor)", "payment provider"], "ticket · quarterly call"),
         (415, 172, "keep informed", "y", ["Tomás + pickers", "Sam · support", "couriers · engineers"], "demo every 2 weeks · notes")]
for x, y, title, fill, names, how in quads:
    sh_how.box(x, y, 316, 120, None, fill)
    sh_how.head(x + 12, y + 26, title, anchor="start", size=18)
    for i, nm in enumerate(names):
        col = i % 2
        row = i // 2
        sh_how.text(x + 14 + col * 150, y + 54 + row * 24, "• " + nm, anchor="start", size=15)
    sh_how.note(x + 12, y + 110, "→ " + how, "pen", anchor="start", size=17)

STAKEHOLDER_MAP = dict(
    slug="stakeholder-map",
    kicker="a.k.a. “who could say no, and who has to live with it?”",
    tldr="Before you design anything, list <b>everyone who can affect the system or is affected by it</b>: not just product and engineering, but legal, finance, operations, support, the people on the shop floor and outside vendors. Place each on a <b>power × interest grid</b>, decide <b>how you'll work with each group</b> (manage closely, keep satisfied, keep informed, monitor), and revisit it monthly. Late surprises come from people nobody thought to ask.",
    chips=[("Family", "understanding the problem"), ("Origin", "Mendelow's power/interest grid (1991); stakeholder theory"), ("Lives in", "a one-page register next to the architecture docs"), ("Pairs with", "business drivers, decision rights (RACI), discovery workshops")],
    problem_side="Larder, week three",
    problem="""  <p class="lead">Ana's first design for the six-city platform is reviewed by Priya (product) and the tech leads. Everyone approves. Then, one by one, the people who weren't in the room find out. <b>Lena</b>, the data protection officer, says customer addresses can't go to the new analytics tool without a contract. <b>Tomás</b>, who runs the Noord dark store, says pickers wear gloves, so the new tap-to-confirm scanning flow won't work. <b>Marco</b>, the CFO, asks why the cloud estimate doubled. <span class="hl-pink">Three weeks of rework</span>, all avoidable.</p>
  <ul>
    <li>The architect talks to the people who are easy to reach: product and engineering.</li>
    <li>Legal, finance and operations hear about it late, and late is when “no” is most expensive.</li>
    <li>The people who use the system every day (pickers, couriers, support agents) are rarely asked at all.</li>
  </ul>""",
    problem_figs=[sh_problem],
    analogy_side="planning a street party",
    analogy="""  <p>To hold a street party you need a <b>permit from the council</b>: they hardly care, but they can cancel it. The <b>organising committee</b> cares and decides. The <b>neighbours</b> can't stop it, but they'll live with the noise, so you tell them early. The <b>bus company</b> only needs a notice that the route is closed. Same party, four very different conversations.</p>""",
    analogy_figs=[sh_analogy],
    map=[("The council that issues the permit", "Legal, compliance, security, the board: high power, low day-to-day interest"),
         ("The organising committee", "Sponsors and leaders who own the outcome: manage closely"),
         ("The neighbours", "Users and operators who live with the result: keep informed, ask them"),
         ("The bus company", "Vendors and adjacent teams: monitor, notify when it touches them"),
         ("Who to tell, and when", "An engagement plan per group, revisited as the project moves")],
    how_side="list them, place them, plan the conversation",
    how="""  <p>The map is <b>cheap</b>: one afternoon in week one. Brainstorm names (people, not departments), ask each person you meet “who else should I talk to?”, then place everyone by <b>power</b> (can they block, fund or change it?) and <b>interest</b> (how much does it change their day?).</p>""",
    how_figs=[sh_how],
    steps=[("Brainstorm wide", "Users, buyers, operators, support, legal, security, finance, vendors, regulators, other teams. Write <i>names</i>, not job titles."),
           ("Snowball", "End every early conversation with “who else should I talk to?” Add the answers."),
           ("Place on the grid", "Power: can they block, fund or overrule? Interest: how much does this change their work?"),
           ("Plan the engagement", "For each group: what they need to hear, how often, in what format, and from whom."),
           ("Find what each one fears", "One line each: “Lena fears a GDPR breach”, “Joost fears a slower picking line”."),
           ("Revisit monthly", "People move quadrants: Lena's interest jumps the day personal data is involved.")],
    vocab=[("Stakeholder", "Anyone who can affect, or is affected by, the system."),
           ("Power / interest grid", "A 2×2 that places stakeholders by influence and concern."),
           ("Manage closely", "High power, high interest: involve in decisions."),
           ("Keep satisfied", "High power, low interest: short, early, targeted updates."),
           ("Keep informed", "Low power, high interest: demos, notes, ask for feedback."),
           ("Engagement plan", "How and how often you work with each stakeholder.")],
    code=dict(file="docs/stakeholders.md", note="stakeholder register, Larder, week one", plain=True, src="""
# Stakeholders: six-city platform                  last reviewed: 2025-10-27

| Who        | Role        | Power | Interest | How we engage              |
|------------|-------------|-------|----------|----------------------------|
| Femke      | CEO         | high  | high     | weekly 30-min review       |
| Marco      | CFO         | high  | high     | weekly review + cost sheet |
| Joost      | Head of Ops | high  | high     | weekly review, store visits|
| Lena       | DPO / legal | high  | low→high | monthly 1:1, early drafts  |
| Tomás      | Store Noord | low   | high     | demo every 2 weeks         |
| Sam        | Support     | low   | high     | demo, ticket review        |
| StockPilot | WMS vendor  | med   | low      | ticket, quarterly call     |

Cares about / fears
  Femke   six cities by 2027 / losing the investors' trust
  Marco   cost per order, the cloud bill / a surprise invoice
  Joost   on-time %, picking speed / a slower picking line
  Lena    GDPR, Belgian rules / a data breach or an unsigned contract
  Tomás   picker app, gloves, Wi-Fi / pickers standing idle

Open: who signs off Antwerp VAT? (ask Lena)
"""),
    tools="tools: a whiteboard or a Miro / FigJam 2×2 is enough. Keep the register as Markdown in the repo or a shared doc; some teams add a column for each stakeholder's preferred channel (Slack, email, a meeting).",
    gains=["<b>Fewer late vetoes</b>: legal, finance and operations are in from week one.",
           "<b>Better requirements</b>: the people who use the system tell you what really hurts.",
           "<b>The right message for each person</b>: the CFO gets cost, the store gets workflow.",
           "<b>A shared list</b> the whole team can use, not just the architect.",
           "<b>Trust</b>: people who were asked are far more likely to support the result."],
    losses=["<b>Time</b>: a day to build, an hour a month to maintain, plus the conversations.",
            "<b>Politics on paper</b>: a written power ranking can offend if shared carelessly.",
            "<b>More voices</b> mean more opinions to reconcile.",
            "<b>Easy to go stale</b>: a map from month one misleads in month six."],
    baseline="Each line compares <b>designing with whoever is in the room (product and engineering)</b> to <b>a stakeholder map built in week one, with an engagement plan, revisited monthly</b>.",
    ratings=[(3, 4, "Everyone knows who decides, who's consulted and who to ask."),
             (2, 5, "Legal, finance and operations shape the design instead of vetoing it."),
             (2, 4, "Fewer late surprises; a day of mapping saves weeks of rework."),
             (2, 4, "Blockers (GDPR, gloves, the bill) surface while they're cheap to fix."),
             (3, 3, "Doesn't change how flexible the system is."),
             (2, 3, "The register shows who was consulted on what."),
             (2, 4, "Finance is managed closely, so cost is a first-class question."),
             (4, 3, "A day to build, an hour a month, plus the conversations."),
             (3, 4, "Teams know who to ask directly, without going through the architect.")],
    pitfalls=[("Departments, not people", "“Legal” is on the map, but nobody knows which lawyer.", "write names; a department can't answer a question."),
              ("Only the loud and the senior", "The map has the C-suite and nobody who uses the system.", "add the operators: pickers, couriers, support agents. Visit them."),
              ("Sharing the grid as-is", "Someone sees themselves in “monitor” and is offended.", "share the engagement plan; keep the power ranking as a working note."),
              ("Draw once, never update", "A new regulation makes Lena critical; the map still says low interest.", "review monthly and at every big change of scope.")],
    use=["The start of any project that crosses teams or departments.",
         "Anything touching personal data, money, contracts or regulated work.",
         "When you're new to an organisation and don't yet know who matters.",
         "Before a big decision that will need sponsors to back it."],
    skip=["A small change inside one team that owns everything it touches.",
          "A short spike or prototype with no users yet.",
          "When the full map exists already: update it instead of starting again."],
    related=["<b>Business drivers &amp; goals</b> (this volume)", "<b>Decision rights (RACI/DACI)</b> (Vol. 2)", "<b>Discovery workshops</b> (Vol. 6)", "<b>Influencing without authority</b> (Vol. 6)"],
    quiz=[("What do the two axes of the grid measure?", "Power: can they block, fund or change it. Interest: how much it affects their work."),
          ("Lena (DPO) has high power and low interest. How do you work with her?", "Keep her satisfied: short, early, targeted updates, especially before anything touches personal data."),
          ("Why write names instead of departments?", "A department can't answer questions or sign off; a named person can."),
          ("Why revisit the map monthly?", "People change quadrants as the project changes: interest jumps when it touches their area.")],
    try_it="For your current project, list 15 stakeholders by name in ten minutes, including at least three people who use or operate the system every day. Place them on the grid. Pick the one person in “keep satisfied” you've never spoken to, and book 20 minutes with them this week.",
    remember="The people who can say <span class=\"hl\">no</span> and the people who have to <span class=\"hl\">live with it</span> are rarely the people in the room.",
    sources=["Aubrey Mendelow, “Stakeholder Mapping” (Proceedings of the 2nd International Conference on Information Systems, 1991).",
             "Nick Rozanski &amp; Eoin Woods, <i>Software Systems Architecture</i>, 2nd ed. (2011), chapter on stakeholders.",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "PMI, <i>A Guide to the Project Management Body of Knowledge</i>, stakeholder management."],
)

# ------------------------------------------------------------------ 02 Business Drivers & Goals
bd_problem = Doodle(760, 280, "Doodle of a vague brief turning into the wrong project. Femke the CEO asks to make the platform scalable for six cities. The engineers hear Kubernetes, microservices and a million users. The real numbers are small: forty thousand orders a day is about five orders a second at peak. The real bottleneck was that opening the second Amsterdam store took five months of code changes.",
                    "“Make it scalable” sends the team after the wrong problem.")
bd_problem.box(20, 30, 220, 70, "“make it scalable", "y", sub="for six cities”", size=18)
bd_problem.note(130, 128, "Femke, CEO", "pen")
bd_problem.arrow(246, 65, 300, 65)
for i, t in enumerate(["Kubernetes!", "microservices!", "1 million users!"]):
    bd_problem.box(306, 18 + i * 44, 190, 36, t, "blue", size=16)
bd_problem.note(400, 166, "what the team heard", "pen")
bd_problem.box(530, 20, 220, 64, "40k orders/day", "green", sub="≈ 5 orders/s at peak", size=17, subsize=15)
bd_problem.box(530, 100, 220, 64, "new store: 5 months", "pink", sub="of code changes", stroke="red", size=17, subsize=15)
bd_problem.note(640, 186, "what actually hurt", "red")
bd_problem.box(160, 206, 440, 52, "6 months on the wrong problem", "pink", stroke="red", size=18)

bd_analogy = Doodle(760, 250, "Doodle of a satnav. Typing 'somewhere nice' gives no route. Typing 'Antwerp by 18:00, avoid tolls, under 40 euros of fuel' gives one clear route, and every turn can be checked against it.",
                     "A satnav can't route “somewhere nice”. Give it a destination, a deadline and what to avoid.")
bd_analogy.icon("screen", 30, 50, 1.6)
bd_analogy.note(80, 170, "satnav", "pen")
bd_analogy.box(170, 30, 220, 50, "“somewhere nice”", "pink", stroke="red", size=17)
bd_analogy.note(280, 104, "✗ no route", "red")
bd_analogy.box(170, 130, 220, 90, None, "green")
bd_analogy.head(184, 160, "Antwerp by 18:00", anchor="start", size=17)
bd_analogy.text(184, 184, "avoid tolls", anchor="start", size=15)
bd_analogy.text(184, 206, "fuel under €40", anchor="start", size=15)
bd_analogy.arrow(396, 175, 470, 175, color="green", label="one route", lx=433, ly=161)
bd_analogy.line("M476 175 C 530 120, 560 210, 610 150 S 680 120, 720 90", color="green")
bd_analogy.icon("pin", 708, 46, 0.8, fill="green")
bd_analogy.note(600, 214, "every turn can be checked", "green")

bd_how = Doodle(760, 360, "From goal to architecture at Larder. The business goal is six cities by the end of 2027. Four drivers support it, each with a measure: a new city in eight weeks or less; ninety-five percent of express orders on time; cost per order down to 2.80 euros; and trust: no lost orders, no double charges, GDPR-clean. Each driver points to an architecture consequence: a city is configuration not code; real-time dispatch; keep it simple and use managed services; reliable order handling.",
                 "One goal, four measurable drivers, and what each one means for the design.")
bd_how.box(230, 14, 300, 54, "six cities by end 2027", "y", size=19)
bd_how.note(645, 46, "business goal", "pen")
drivers = [("city ≤ 8 weeks", "today: 5 months"), ("95 % on time", "today: 88 %"), ("€2.80 / order", "today: €4.10"), ("trust", "no lost orders")]
cons = [("city = config", "not code"), ("real-time", "dispatch"), ("simple", "managed services"), ("reliable", "order flow")]
for i, ((d, s), c) in enumerate(zip(drivers, cons)):
    x = 14 + i * 186
    bd_how.line(f"M380 70 L{x + 85} 112", thin=True)
    bd_how.box(x, 116, 172, 74, d, "green", sub=s, size=16, subsize=14)
    bd_how.arrow(x + 86, 196, x + 86, 246)
    bd_how.box(x, 250, 172, 64, c[0], "blue", sub=c[1], size=16, subsize=14)
bd_how.note(14, 100, "drivers (measurable)", "pen", anchor="start", size=17)
bd_how.note(380, 340, "architecture consequences: what each driver asks of the design", "pen")

BUSINESS_DRIVERS = dict(
    slug="business-drivers",
    kicker="a.k.a. “what does winning look like, in numbers?”",
    tldr="A business brief like “make it scalable” can't guide a design. Turn it into <b>three to five business drivers</b>: the outcomes the business needs, each with a <b>measure, today's value and a target date</b>. Agree them with the sponsors, write them on one page, and check every big design choice against them. Drivers tell you <b>what to optimise</b>, and just as usefully, <b>what not to bother with</b>.",
    chips=[("Family", "understanding the problem"), ("Origin", "business architecture; goal-question-metric (Basili); OKRs"), ("Lives in", "the first page of the architecture overview"), ("Pairs with", "stakeholder map, quality attribute scenarios, ASRs")],
    problem_side="Larder, the brief",
    problem="""  <p class="lead">Femke's brief to Ana is one sentence: <i>“Make the platform scalable for six cities.”</i> In the first meeting the engineers are already discussing Kubernetes, microservices and a million users. But six cities at Amsterdam's rate is about <b>40,000 orders a day</b>, roughly <b>five orders a second</b> at peak: one Postgres database handles that easily. What really hurt was that opening Amsterdam's second dark store took <span class="hl-pink">five months of code changes</span>. “Scalable” meant <i>opening cities fast</i>, not handling traffic.</p>
  <ul>
    <li>Vague words (“scalable”, “modern”, “robust”) mean something different to everyone.</li>
    <li>Engineers fill the gap with the interesting technical problem, not the business one.</li>
    <li>With no measure, nobody can tell if the architecture worked.</li>
  </ul>""",
    problem_figs=[bd_problem],
    analogy_side="the satnav",
    analogy="""  <p>A satnav can't plan a route to “somewhere nice”. Type <b>“Antwerp by 18:00, avoid tolls, fuel under €40”</b> and it gives you one route, and every turn can be checked against it. The destination and the limits decide the road, not the other way round.</p>""",
    analogy_figs=[bd_analogy],
    map=[("The destination", "The business goal: six cities by end 2027"),
         ("Arrive by 18:00", "A target with a date: new city in ≤ 8 weeks"),
         ("Avoid tolls, fuel under €40", "Cost and constraint drivers: €2.80 per order"),
         ("The route", "The architecture"),
         ("“Recalculating…”", "Re-checking the design when a driver changes")],
    how_side="from one-line brief to measurable drivers",
    how="""  <p>Ask “<b>why?</b>” until you reach something the business measures. “Scalable” → why? → “to open cities” → why does that hurt today? → “five months per store”. That's a driver: <i>new city in eight weeks</i>. Then ask what each driver asks of the design.</p>""",
    how_figs=[bd_how],
    steps=[("Collect the goals", "Read the business plan, the investor deck and the OKRs. Ask the sponsor: “what must be true in two years?”"),
           ("Ask “why?” until it's measurable", "Keep asking until the answer has a number someone already tracks."),
           ("Write each driver as a measure", "Name, today's value, target, date, owner: “express on time: 88 % → 95 % by Q4 2026, Joost”."),
           ("Keep it to three to five", "More than five and they stop deciding anything. Rank them."),
           ("Note the consequence", "For each driver, one line on what it means for the architecture."),
           ("Get them signed off", "Sponsors agree the list and the order. Re-check at every big decision.")],
    vocab=[("Business goal", "What the organisation wants to achieve (six cities)."),
           ("Business driver", "An outcome that must happen for the goal, with a measure."),
           ("Measure / KPI", "The number that tells you if a driver is met."),
           ("Baseline", "Today's value of the measure."),
           ("Target", "The value to reach, by a date."),
           ("Five whys", "Asking “why?” repeatedly to get from a vague wish to a real need.")],
    code=dict(file="docs/architecture/01-drivers.md", note="business drivers, agreed 2025-10-24", plain=True, src="""
# Business drivers: six-city platform
Goal: six cities by end 2027 (Series B condition). Sponsors: Femke, Marco, Joost.

| # | Driver            | Measure                   | Today    | Target | By      |
|---|-------------------|---------------------------|----------|--------|---------|
| 1 | Open cities fast  | weeks, lease to launch    | 20       | ≤ 8    | Q3 2026 |
| 2 | Keep the promise  | express orders on time    | 88 %     | 95 %   | Q4 2026 |
| 3 | Unit economics    | cost per order            | €4.10    | €2.80  | Q4 2027 |
| 4 | Stay trusted      | lost / double-charged     | ~3/month | 0      | always  |

Owners: 1–2 Joost · 3 Marco · 4 Priya

What each means for the architecture
1 → a new city is configuration, not code (stores, zones, hours, prices, VAT)
2 → courier dispatch must react in seconds, not a 30-second cron job
3 → prefer simple, managed services; no platform team we can't afford
4 → order + payment must survive crashes without loss or duplicates

Not a driver (yet): handling more than ~10 orders/s. Don't design for it.
"""),
    tools="tools: one page in the repo or the wiki. Some teams use an OKR tool or a business model canvas as input; the drivers page links to them rather than copying.",
    gains=["<b>A shared definition of success</b> that business and engineering both understand.",
           "<b>A tie-breaker</b> for every design debate: which option serves driver 1?",
           "<b>Less over-engineering</b>: “not a driver” is permission to keep things simple.",
           "<b>Measurable</b>: you can tell, later, whether the architecture worked.",
           "<b>Sponsors stay engaged</b> because the design speaks their language."],
    losses=["<b>Hard conversations</b>: sponsors may disagree on the order.",
            "<b>Numbers can be guesses</b> at first, and need correcting.",
            "<b>Risk of tunnel vision</b>: what isn't on the list may still matter (security, accessibility).",
            "<b>Goals change</b>: the page has to be maintained."],
    baseline="Each line compares <b>designing from a one-line brief (“make it scalable”)</b> to <b>four ranked, measurable drivers agreed with the sponsors and checked at each big decision</b>.",
    ratings=[(2, 5, "Everyone can say, in numbers, what the architecture is for."),
             (2, 5, "Business and engineering agree on the same few outcomes."),
             (2, 4, "Debates end sooner: “which option serves driver 1?”"),
             (2, 4, "You build for the real problem, not the imagined one."),
             (3, 3, "Neutral; drivers can change, and the page is updated."),
             (2, 4, "Every design choice can point to the driver it serves."),
             (2, 5, "Cost per order is a driver, so cost is part of every choice."),
             (4, 4, "One page and one meeting; it saves meetings later."),
             (2, 4, "Teams can make local choices that serve the same drivers.")],
    pitfalls=[("Drivers without numbers", "“Be fast”, “be reliable”, “be modern”.", "ask “why?” until there's a measure, a baseline and a target."),
              ("Twelve drivers", "Everything is a priority, so nothing decides anything.", "three to five, ranked. The rest are context."),
              ("Technical drivers in disguise", "“Use microservices” is listed as a business driver.", "that's a solution; ask what outcome it was meant to achieve."),
              ("Set once, forgotten", "The drivers page is from the kick-off and nobody reads it.", "open it at every big decision and every quarterly review.")],
    use=["Any new system, platform rebuild or major change of direction.",
         "When the brief is one sentence or a buzzword.",
         "When engineering and business seem to be solving different problems.",
         "Before a big build vs buy, cloud or vendor decision."],
    skip=["A small feature where the product goal is already measured.",
          "When the drivers already exist in a product strategy: link them, don't duplicate.",
          "Throwaway experiments with a one-week life."],
    related=["<b>Stakeholder map</b> (this volume)", "<b>Architecturally significant requirements</b> (this volume)", "<b>Quality attribute scenarios</b> (this volume)", "<b>Trade-off sliders</b> (Vol. 2)"],
    quiz=[("Why is “make it scalable” not a business driver?", "It has no measure and means different things to different people; it's a wish, not an outcome."),
          ("What five things make a driver usable?", "A name, a measure, today's value (baseline), a target with a date, and an owner."),
          ("Why keep only three to five drivers?", "With more, they stop deciding anything; ranking a few gives a real tie-breaker."),
          ("What's the value of writing “not a driver” lines?", "They give permission to keep things simple and stop over-engineering for needs nobody has.")],
    try_it="Take your project's brief and ask “why?” five times about its vaguest word. Write the result as one driver with a measure, today's value, a target and a date. Show it to the sponsor and ask: “if we hit this number, did we win?”",
    remember="Ask <span class=\"hl\">why</span> until you hit a <span class=\"hl\">number</span>. Then design for the number, not the word.",
    sources=["Victor Basili et al., “The Goal Question Metric Approach” (1994).",
             "Len Bass, Paul Clements &amp; Rick Kazman, <i>Software Architecture in Practice</i>, 4th ed. (2021), business goals.",
             "John Doerr, <i>Measure What Matters</i> (2018), on OKRs.",
             "The Open Group, TOGAF Standard, “Business Architecture: drivers, goals and objectives”."],
)

# ------------------------------------------------------------------ 03 System Context Diagram
sc_problem = Doodle(760, 280, "Doodle of three engineers each drawing 'the system' differently. Ben's boundary includes StockPilot, the warehouse system, as if Larder owned it. Dee's leaves out the support tool. Joost's includes the couriers' phones. Their estimates for the Rotterdam work differ by two months because one includes rebuilding the warehouse system.",
                    "Three people, three boundaries, three estimates.")
for i, (who, inside, est) in enumerate([("Ben", ["Larder Core", "StockPilot"], "7 months"), ("Dee", ["apps", "Larder Core"], "4 months"), ("Joost", ["Larder Core", "courier phones"], "5 months")]):
    x = 20 + i * 250
    sc_problem.box(x, 20, 220, 150, None, "paper", dash=True)
    sc_problem.head(x + 110, 46, f"{who}'s “system”", size=17)
    for k, t in enumerate(inside):
        sc_problem.box(x + 20, 62 + k * 50, 180, 40, t, "blue" if k == 0 else "y", size=15)
    sc_problem.note(x + 110, 200, "estimate: " + est, "red")
sc_problem.box(150, 220, 460, 46, "an hour arguing what's “in scope”", "pink", stroke="red", size=17)

sc_analogy = Doodle(760, 280, "Doodle of a site plan for a house. The house is one block inside the plot boundary. Around it are the road access, the water, power and sewer connections, and the neighbours' houses. Nobody draws the neighbours' kitchens; the site plan only shows what crosses the boundary.",
                     "A site plan: your house as one block, the plot line, and everything that crosses it.")
sc_analogy.box(250, 70, 260, 140, None, "paper", dash=True)
sc_analogy.note(520, 204, "plot boundary", "pen", anchor="start")
sc_analogy.box(310, 100, 140, 80, "the house", "y", size=18)
sc_analogy.box(20, 100, 140, 80, "neighbours", "paper", size=16)
sc_analogy.box(600, 100, 140, 80, "neighbours", "paper", size=16)
sc_analogy.box(250, 236, 260, 34, "the road", "blue", size=16)
sc_analogy.arrow(380, 184, 380, 232, both=True)
for (x1, y1, x2, y2, lab, lx, ly) in [(310, 120, 164, 120, "", 0, 0), (450, 120, 596, 120, "", 0, 0)]:
    sc_analogy.line(f"M{x1} {y1} L{x2} {y2}", dash=True, thin=True)
for i, t in enumerate(["water", "power", "sewer"]):
    x = 300 + i * 80
    sc_analogy.line(f"M{x + 20} 100 L{x + 20} 30", thin=True, color="pen")
    sc_analogy.note(x + 20, 22, t, "pen", size=17)
sc_analogy.note(90, 220, "not their kitchens", "pen")

sc_how = Doodle(760, 400, "Larder's system context diagram. In the middle, one box: the Larder platform. Above it, the people: customers order groceries, pickers pick and pack orders, couriers deliver them, support agents handle refunds. Below it, the external systems: the payment provider takes card and iDEAL payments, StockPilot holds the warehouse stock, the helpdesk tool holds support tickets, and an SMS and email service sends updates. Each line is labelled with what crosses it.",
                 "Larder's context diagram: one box for us, everything else around it, every line labelled.")
sc_how.box(270, 160, 220, 80, "Larder platform", "y", sub="what we build & run", size=20, subsize=15)
people = [("customer", 10, "orders, tracks"), ("picker", 200, "picks, packs"), ("courier", 390, "delivers"), ("support agent", 580, "refunds, answers")]
for name, x, what in people:
    sc_how.box(x, 14, 170, 66, name, "green", sub=what, size=17, subsize=15)
    sc_how.arrow(x + 85, 84, 380 + (x - 295) * 0.35, 156)
systems = [("payment provider", 10, "charges, refunds"), ("StockPilot", 200, "stock levels"), ("helpdesk tool", 390, "tickets"), ("SMS & email", 580, "order updates")]
for name, x, what in systems:
    sc_how.box(x, 314, 170, 66, name, "blue", sub=what, size=16, subsize=15)
    sc_how.arrow(380 + (x - 295) * 0.35, 244, x + 85, 310)
sc_how.note(504, 190, "↑ people", "green", anchor="start", size=17)
sc_how.note(504, 220, "↓ systems we don't own", "pen", anchor="start", size=17)

SYSTEM_CONTEXT = dict(
    slug="system-context",
    kicker="a.k.a. “the site plan”",
    tldr="Draw your system as <b>one box</b> in the middle. Around it, draw the <b>people</b> who use it and the <b>external systems</b> it talks to, and <b>label every line</b> with what crosses it. Nothing inside the box, nothing about technology. It takes an hour, fits on one slide, and settles the most expensive early question: <b>where does our system end, and what do we depend on?</b>",
    chips=[("Family", "understanding the problem"), ("Origin", "context diagrams in structured analysis (1970s); level 1 of Simon Brown's C4 model"), ("Lives in", "the architecture overview, as diagram-as-code"), ("Pairs with", "stakeholder map, C4 model, integration styles")],
    problem_side="Larder, scoping Rotterdam",
    problem="""  <p class="lead">Ana asks three people to estimate the Rotterdam work. Ben says seven months, Dee four, Joost five. It turns out they're estimating <span class="hl-pink">three different systems</span>: Ben's includes changing StockPilot, the warehouse system Larder only rents; Dee's leaves out the support tool; Joost's includes the couriers' phones. An hour of the meeting goes on “is that in scope?”</p>
  <ul>
    <li>Everyone has a picture of “the system” in their head, and the pictures don't match.</li>
    <li>External dependencies (vendors, providers) are forgotten until they break or block.</li>
    <li>Estimates, contracts and security reviews all need a clear boundary.</li>
  </ul>""",
    problem_figs=[sc_problem],
    analogy_side="the site plan",
    analogy="""  <p>Before an architect designs the rooms, they draw a <b>site plan</b>: the house as one block, the <b>plot boundary</b>, the road access, and the <b>water, power and sewer connections</b>. The neighbours appear as blocks too; nobody draws their kitchens. It answers one question: <i>what's ours, and what crosses the line?</i></p>""",
    analogy_figs=[sc_analogy],
    map=[("The house as one block", "Your system as one box, no internals"),
         ("The plot boundary", "The scope: what you build, run and are responsible for"),
         ("Water, power, sewer connections", "External systems you depend on: payments, StockPilot, SMS"),
         ("The road and the visitors", "The people who use the system: customers, pickers, couriers"),
         ("Not drawing the neighbours' kitchens", "Not modelling other systems' insides")],
    how_side="one box, everything around it, every line labelled",
    how="""  <p>The trick is what you <b>leave out</b>: no databases, no services, no technologies. Only the people, the outside systems and <b>what flows</b> between them. That's what makes it readable by Femke, Lena and the vendor alike.</p>""",
    how_figs=[sc_how],
    steps=[("Draw one box for your system", "Name it the way the business does: “Larder platform”, not “k8s cluster”."),
           ("Add the people", "Every role that uses it: customers, pickers, couriers, support agents, store managers."),
           ("Add the external systems", "Everything it talks to that you don't own: providers, SaaS tools, partner APIs, other teams."),
           ("Label every line", "With what crosses it, in plain words: “charges, refunds”, “stock levels every 5 min”."),
           ("Walk it with stakeholders", "Ask each one: who's missing? What else do we send or receive?"),
           ("Keep it as code", "Write it in a diagram-as-code tool and keep it in the repo, so it gets updated.")],
    vocab=[("System context", "The system as a black box among its users and neighbours."),
           ("System boundary", "The line between what you own and what you depend on."),
           ("Actor / person", "A role that uses the system."),
           ("External system", "A system you integrate with but don't build or run."),
           ("Relationship", "A labelled line: what flows, and which way."),
           ("Diagram as code", "A diagram described in text, versioned with the code.")],
    code=dict(file="docs/architecture/context.dsl", note="Structurizr DSL, C4 level 1", plain=True, src="""
workspace "Larder" {
  model {
    customer = person "Customer"      "Orders groceries in the app or web shop"
    picker   = person "Picker"        "Picks and packs orders in a dark store"
    courier  = person "Courier"       "Delivers orders by e-bike"
    agent    = person "Support agent" "Answers questions, issues refunds"

    larder   = softwareSystem "Larder platform" "Shop, orders, picking, dispatch"

    psp        = softwareSystem "Payment provider" "Cards, iDEAL, Bancontact"
    stockpilot = softwareSystem "StockPilot"       "Warehouse stock (SaaS)"
    helpdesk   = softwareSystem "Helpdesk tool"    "Support tickets (SaaS)"
    messaging  = softwareSystem "SMS & email"      "Order updates"

    customer -> larder     "Orders, tracks delivery"
    picker   -> larder     "Picks, packs, reports out-of-stock"
    courier  -> larder     "Collects, delivers, shares location"
    agent    -> larder     "Looks up orders, refunds"
    larder   -> psp        "Charges, refunds"
    larder   -> stockpilot "Reads stock levels, every 5 min"
    larder   -> helpdesk   "Creates tickets"
    larder   -> messaging  "Sends order updates"
  }
  views { systemContext larder { include * ; autolayout lr } }
}
"""),
    tools="tools: Structurizr (DSL above), PlantUML with the C4 library, Mermaid's C4 diagrams, or draw.io / Excalidraw for a first sketch. A whiteboard photo is fine in week one; move it to code once it settles.",
    gains=["<b>One agreed scope</b>: estimates and contracts talk about the same thing.",
           "<b>Dependencies are visible</b>: every vendor and provider is on the page.",
           "<b>Readable by anyone</b>: no technology, so executives and lawyers can review it.",
           "<b>A starting point</b> for security reviews, data flows and integration plans.",
           "<b>Cheap</b>: an hour to draw, minutes to update."],
    losses=["<b>Too high-level for builders</b>: they need container and component views too.",
            "<b>Boundary arguments</b> surface early, and can be uncomfortable.",
            "<b>Goes stale</b> unless it's kept as code and reviewed.",
            "<b>Hides the hard parts</b>: one line can hide a very messy integration."],
    baseline="Each line compares <b>everyone holding their own mental picture of the system</b> to <b>one agreed context diagram, labelled and kept as code</b>.",
    ratings=[(2, 5, "One page anyone can read in two minutes."),
             (2, 4, "Business, vendors and engineering agree what's in scope."),
             (2, 4, "“Is that in scope?” is answered by pointing at the page."),
             (2, 4, "Forgotten dependencies (helpdesk, SMS) show up on day one."),
             (3, 3, "Neutral; it describes the boundary, it doesn't fix it."),
             (2, 4, "Versioned with the code, so changes in scope have history."),
             (2, 3, "Each external system is a cost line you can now see."),
             (4, 4, "An hour to draw, minutes to update."),
             (2, 3, "Teams can see which neighbours they talk to, without asking.")],
    pitfalls=[("Drawing the insides", "The context diagram shows services, queues and databases.", "one box only; inside detail belongs in the container view."),
              ("Unlabelled lines", "Arrows connect boxes but say nothing about what flows.", "label every line with what crosses it, in plain words."),
              ("Forgetting the humans", "Only systems are drawn; pickers and support agents are missing.", "add every role that uses it, especially internal staff."),
              ("A picture in a slide deck", "Drawn once in a deck, never updated, wrong by month three.", "keep it as diagram-as-code in the repo and review it with changes.")],
    use=["The start of every new system or major change.",
         "When estimates or scope discussions don't match.",
         "Before a security review, a data protection review or a vendor contract.",
         "Onboarding: the first diagram a new joiner should see."],
    skip=["Inside a single component where the boundary is obvious.",
          "As the only diagram for builders: add container and component views.",
          "When an up-to-date one exists: update it instead."],
    related=["<b>Stakeholder map</b> (this volume)", "<b>C4 model</b> (Vol. 3)", "<b>Choosing an integration style</b> (Vol. 4)", "<b>Threat modelling</b> (patterns, Vol. 5)"],
    quiz=[("What goes inside the system box on a context diagram?", "Nothing: the system is one black box. Internals belong in other views."),
          ("What are the two kinds of things around the box?", "People (roles that use it) and external systems it talks to."),
          ("Why label every line?", "So readers know what flows and which way: the label is where most misunderstandings surface."),
          ("Why keep it as code?", "It's versioned and reviewed with the code, so it stays current.")],
    try_it="Draw your system's context diagram from memory in 15 minutes, with every line labelled. Then show it to someone in operations or support and ask “who or what is missing?” Count how many boxes they add.",
    remember="Draw the <span class=\"hl\">plot line</span> before the rooms. One box for you, and <span class=\"hl\">label everything that crosses it</span>.",
    sources=["Simon Brown, <i>The C4 Model for Visualising Software Architecture</i> (c4model.com; Leanpub).",
             "Tom DeMarco, <i>Structured Analysis and System Specification</i> (1978), context diagrams.",
             "Nick Rozanski &amp; Eoin Woods, <i>Software Systems Architecture</i>, 2nd ed. (2011), the context viewpoint.",
             "Structurizr DSL documentation (docs.structurizr.com)."],
)

# ------------------------------------------------------------------ 04 Domain Discovery (Event Storming)
es_problem = Doodle(760, 290, "Doodle of four people explaining how an order works, each from their own corner. Ben talks about database tables. Joost talks about the store floor. Sam talks about refunds. Tomás talks about the picker app. Nobody owns what happens when an item is out of stock: pickers choose substitutes, customers complain, and support refunds by hand, six percent of orders.",
                    "Everyone knows their part of “an order”. Nobody knows the whole, and the gap costs 6 % of orders.")
for i, (who, says) in enumerate([("Ben · orders", "“orders, order_lines…”"), ("Joost · ops", "“release to store…”"), ("Tomás · store", "“scan, pack, shelf”"), ("Sam · support", "“then we refund”")]):
    x = 18 + i * 186
    es_problem.box(x, 20, 172, 70, None, "blue")
    es_problem.head(x + 86, 46, who, size=16)
    es_problem.text(x + 86, 74, says, size=15)
es_problem.box(250, 140, 260, 64, "item out of stock?", "pink", sub="who decides the substitute?", stroke="red", size=17, subsize=14)
for x in (104, 290, 476, 662):
    es_problem.line(f"M{x} 94 L{380 + (x - 383) * 0.45} 136", dash=True, thin=True, color="red")
es_problem.note(380, 236, "pickers guess · customers complain · support refunds by hand", "red")
es_problem.note(380, 266, "6 % of orders get a refund ticket", "red", size=19)

es_analogy = Doodle(760, 260, "Doodle of a film storyboard pinned on a wall. Each scene is a card in order from left to right. The director, the actors and the crew stand in front of it together and see the whole film before anything is shot. Question marks are stuck where the script is unclear.",
                     "A storyboard: the whole film on one wall, in order, before anyone shoots a scene.")
for i, t in enumerate(["scene 1", "scene 2", "scene 3", "scene 4", "scene 5"]):
    x = 30 + i * 144
    es_analogy.box(x, 40, 120, 90, None, "paper")
    es_analogy.icon("frame", x + 28, 52, 1.0)
    es_analogy.note(x + 60, 152, t, "pen", size=17)
es_analogy.arrow(30, 176, 730, 176, label="time →", lx=380, ly=200)
es_analogy.box(445, 4, 54, 40, "?", "pink", stroke="red", size=22)
es_analogy.note(560, 24, "unclear script", "red", anchor="start")
es_analogy.note(380, 240, "director, actors and crew see the same film", "pen")

es_how = Doodle(760, 380, "Part of Larder's event storming timeline. Orange events, left to right: order placed, payment authorised, order released to store, item picked, item out of stock, substitution offered, substitution accepted, order packed, courier assigned, order delivered. Blue commands above some events, such as place order and offer substitution. Yellow actors: customer, picker, courier. A pink hot spot on substitution: who decides, and how long does the customer get to answer? A green policy: when an item is out of stock, offer a substitute within two minutes.",
                 "Orange events in time order; the pink hot spot shows where nobody owns the process.")
events = ["order placed", "payment authorised", "released to store", "item picked", "item out of stock", "substitute offered", "substitute accepted", "order packed", "courier assigned", "delivered"]
for i, e in enumerate(events):
    col, row = i % 5, i // 5
    x, y = 14 + col * 150, 110 + row * 150
    es_how.box(x, y, 130, 64, None, "y", rx=3)
    words = e.split(" ", 1)
    es_how.text(x + 65, y + 28, words[0], size=16)
    es_how.text(x + 65, y + 50, words[1] if len(words) > 1 else "", size=16)
    if col < 4:
        es_how.line(f"M{x + 132} {y + 32} h14", thin=True)
for (x, y, t) in [(14, 60, "place order"), (614, 60, "report OOS")]:
    es_how.box(x, y, 130, 36, t, "blue", rx=3, size=15)
for (x, y, t) in [(154, 66, "customer"), (508, 66, "picker"), (468, 336, "courier")]:
    es_how.box(x, y, 100, 28, t, "paper", size=14, rx=3)
es_how.box(304, 196, 150, 52, "who decides?", "pink", sub="how long to wait?", stroke="red", size=15, subsize=13)
es_how.line("M304 238 L262 258", dash=True, color="red")
es_how.box(14, 196, 270, 52, "policy: offer a substitute", "green", sub="within 2 minutes of OOS", size=15, subsize=13)
es_how.note(380, 26, "colour key: orange = event · blue = command · white = actor · pink = hot spot · green = policy", "pen", size=16)

EVENT_STORMING = dict(
    slug="event-storming",
    kicker="a.k.a. “the storyboard on the wall”",
    tldr="Get the people who <b>do the work</b> and the people who <b>build the software</b> in one room with a long paper roll and orange sticky notes. Everyone writes the <b>events</b> that happen in the business, in the past tense (“order placed”, “item out of stock”), and puts them on the wall <b>in time order</b>. Gaps, arguments and question marks become <b>hot spots</b>. In a few hours you get a shared picture of the domain, the problems nobody owns, and the first hints of where the <b>boundaries</b> are.",
    chips=[("Family", "understanding the problem"), ("Origin", "Alberto Brandolini, “Introducing Event Storming” (2013)"), ("Lives in", "a paper roll, then photos and a digital board"), ("Pairs with", "bounded contexts, stakeholder map, discovery workshops")],
    problem_side="Larder, “how does an order work?”",
    problem="""  <p class="lead">Ana asks four people how an order works. Ben talks in tables, Joost in store releases, Tomás in scans and shelves, Sam in refunds. Each story is right, and none of them covers the whole. The hole in the middle is <b>substitutions</b>: when an item is out of stock, pickers guess a replacement, customers complain, and support refunds by hand. <span class="hl-pink">6 % of orders</span> end in a refund ticket, and nobody owns the problem.</p>
  <ul>
    <li>Interviews one by one give you pieces, never the whole flow.</li>
    <li>The worst problems sit <i>between</i> departments, where nobody looks.</li>
    <li>Engineers learn the domain from the database, which is the least reliable source.</li>
  </ul>""",
    problem_figs=[es_problem],
    analogy_side="the storyboard",
    analogy="""  <p>Before shooting a film, the crew pins a <b>storyboard</b> on the wall: every scene on a card, <b>in order</b>. The director, actors, camera crew and editor stand in front of the same wall. Missing scenes and scenes that don't make sense jump out, and someone sticks a <b>question mark</b> on them. Fixing a storyboard costs a pen; fixing a shot film costs a reshoot.</p>""",
    analogy_figs=[es_analogy],
    map=[("A scene card", "A domain event: “item out of stock”, written in the past tense"),
         ("Cards in order on the wall", "The timeline of the business process"),
         ("Director, actors and crew together", "Domain experts and engineers in one room"),
         ("A question mark on a scene", "A hot spot: a conflict, a gap, a pain point"),
         ("Chapters of the film", "Groups of events that hint at bounded contexts")],
    how_side="events first, everything else after",
    how="""  <p>Start with <b>chaotic exploration</b>: everyone writes events at once, no discussion. Then <b>enforce the timeline</b>: sort them left to right, remove duplicates, argue. Then add <b>hot spots</b>, the <b>commands</b> that trigger events, the <b>actors</b> who issue them, and <b>policies</b> (“whenever X, then Y”).</p>""",
    how_figs=[es_how],
    steps=[("Invite the right mix", "6–12 people: the ones who do the work (store, support, ops) and the ones who build it. A facilitator who isn't the architect helps."),
           ("Prepare the wall", "6+ metres of paper, plenty of orange stickies and markers. No chairs: people should stand and move."),
           ("Chaotic exploration (30 min)", "Everyone writes events in the past tense and sticks them roughly in time order. No debate yet."),
           ("Enforce the timeline (45 min)", "Walk left to right, merge duplicates, order them, and mark disagreements with a pink hot spot."),
           ("Add commands, actors, policies", "Blue: what triggered it. Small yellow: who. Lilac or green: the rule that reacts to it."),
           ("Harvest", "Photograph everything. Pick the top three hot spots, name owners, and sketch the first boundaries.")],
    vocab=[("Domain event", "Something that happened that the business cares about, in the past tense."),
           ("Command", "A request or decision that causes an event (“offer substitute”)."),
           ("Actor", "The person or role who issues a command."),
           ("Policy", "A reaction rule: “whenever X happens, do Y”."),
           ("Hot spot", "A pink note marking a conflict, question or pain."),
           ("Big-picture storming", "The wide, whole-business version; design-level storming goes deeper on one area.")],
    code=dict(file="docs/workshops/2025-10-21-event-storming.md", note="workshop plan and harvest", plain=True, src="""
# Big-picture event storming: “an order, end to end”
When: Tue 21 Oct 2025, 13:00–17:00, Noord dark store canteen
Who:  Joost, Tomás + 2 pickers, a courier, Sam, Priya, Ben, Cho, Dee, Ana
Facilitator: Eli (not the architect, so Ana can listen)
Kit:  8 m paper roll · orange, blue, yellow, pink, green stickies · markers

13:00  Why we're here, the rules (past tense, one event per note)
13:10  Chaotic exploration: everyone writes events, silently
13:40  Enforce the timeline: sort, merge, argue, mark hot spots
14:30  Break
14:45  Commands, actors, policies on the busiest part
15:45  Vote: top 3 hot spots (3 dots each)
16:15  Owners and next steps

Harvest
- 61 events, 14 hot spots
- Top hot spot: substitutions (no owner; 6 % of orders → refund ticket)
- Policy agreed: offer a substitute within 2 minutes of “item out of stock”
- Owner: Joost (process) + Priya (app flow) · next: design-level session, 4 Nov
- Boundary hints: catalogue · ordering · payments · fulfilment · dispatch · care
"""),
    tools="tools: a paper roll and stickies in a room beats any tool. For remote teams: Miro or FigJam event storming templates. Photograph the wall before anyone takes it down.",
    gains=["<b>A shared picture</b> of the whole process in hours, not weeks of interviews.",
           "<b>Problems between departments</b> (like substitutions) become visible and get owners.",
           "<b>Engineers learn the domain</b> from the people who live it.",
           "<b>Boundary hints</b>: clusters of events suggest bounded contexts.",
           "<b>Energy and trust</b>: operations staff are heard, often for the first time."],
    losses=["<b>Expensive room</b>: a half day of 10 busy people.",
            "<b>Needs facilitation</b>: without it, the loudest voice wins.",
            "<b>Messy output</b>: a wall of stickies needs harvesting into decisions.",
            "<b>Remote is harder</b>: digital boards lose some of the energy."],
    baseline="Each line compares <b>learning the domain through one-to-one interviews and the database</b> to <b>a half-day big-picture event storming with domain experts and engineers, harvested into owners and next steps</b>.",
    ratings=[(2, 5, "The whole process on one wall, in the business's own words."),
             (2, 5, "Ops, support and engineering build the picture together."),
             (3, 4, "Half a day replaces weeks of interviews and back-and-forth."),
             (2, 5, "Hot spots expose the problems nobody owned."),
             (3, 4, "Boundaries drawn from the domain are easier to change later."),
             (2, 3, "Photos and the harvest note keep the reasoning, roughly."),
             (2, 3, "Pain points often have a cost attached (6 % refunds)."),
             (3, 2, "A half day of 10 people, plus preparation and harvesting."),
             (2, 4, "Teams form around clear parts of the domain.")],
    pitfalls=[("Only engineers in the room", "The wall shows tables and APIs, not the business.", "half the room must be people who do the work."),
              ("Starting with the solution", "People write “call payment API” instead of “payment authorised”.", "events only, in the past tense, in business words."),
              ("No harvest", "A great afternoon, then the stickies go in the bin.", "photograph, list the top hot spots, name owners and dates before leaving."),
              ("The architect facilitates and talks", "Ana runs the session and steers it to her design.", "use a neutral facilitator so the architect can listen.")],
    use=["A new domain you don't know, or a team that doesn't share one picture.",
         "Before drawing service or module boundaries.",
         "When the worst problems sit between departments.",
         "Onboarding a team onto a complex business process."],
    skip=["A simple CRUD tool with obvious behaviour.",
          "When the domain experts can't attend: you'll only storm your assumptions.",
          "When you need detailed requirements for one screen: use a design-level session or a story map."],
    related=["<b>Bounded contexts</b> (this volume)", "<b>Stakeholder map</b> (this volume)", "<b>Event sourcing</b> (patterns, Vol. 1)", "<b>Discovery workshops</b> (Vol. 6)"],
    quiz=[("Why write events in the past tense?", "They describe facts the business cares about (“order placed”), not solutions or wishes."),
          ("What is a hot spot?", "A pink note marking a conflict, gap, question or pain point on the timeline."),
          ("Who must be in the room?", "People who do the work (operations, support, store) as well as the people who build the software."),
          ("What should you leave the room with?", "Photos, the top hot spots with owners and dates, and first hints of boundaries.")],
    try_it="Run a 45-minute mini event storming on one process you know (for example, “a customer gets a refund”) with two colleagues from outside engineering. Silent writing for 10 minutes, sorting for 25, then mark the hot spots. Did you find a step nobody owns?",
    remember="Put the <span class=\"hl\">whole film on the wall</span> before you shoot. The <span class=\"hl\">pink notes</span> are where the money is.",
    sources=["Alberto Brandolini, <i>Introducing EventStorming</i> (Leanpub).",
             "Vaughn Vernon, <i>Domain-Driven Design Distilled</i> (2016), chapter on event storming.",
             "Eric Evans, <i>Domain-Driven Design</i> (2003).",
             "eventstorming.com, the official site with guides and photos."],
)

NOTES = [STAKEHOLDER_MAP, BUSINESS_DRIVERS, SYSTEM_CONTEXT, EVENT_STORMING]
