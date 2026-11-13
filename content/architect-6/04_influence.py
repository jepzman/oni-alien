# Series 2 · The Solution Architect's Notebook · Vol. 6 · Influence.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 Influencing Without Authority
iw_problem = Doodle(760, 280, "Doodle of August 2028. Two teams still read Larder Core's order tables every night through the old export: the data team for reporting and finance for the monthly close. Neither reports to Ana. A fitness function now flags it, and Ana could escalate to Femke, but forcing them would make enemies of two teams she needs.",
                    "Two teams read Core's tables nightly. Neither reports to Ana. Escalating would make enemies she needs.")
iw_problem.box(20, 40, 320, 90, "data team", "paper", sub="reports to Marco")
iw_problem.box(400, 40, 340, 90, "finance", "paper", sub="the monthly close")
iw_problem.note(380, 200, "no authority, and a deadline", "red", size=20)

iw_analogy = Doodle(760, 250, "Doodle of a town planner who wants people to stop parking on the square: instead of fines, she asks the shopkeepers what they need, builds a car park two minutes away with free first hour, and lets the shopkeepers announce it. The square empties by itself.",
                     "A planner empties the square without fines: ask what shopkeepers need, build an easier car park, let them announce it.")
iw_analogy.icon("map", 30, 60, 1.2)
for i, (t, f) in enumerate([("ask", "y"), ("build easier", "green"), ("they announce", "blue")]):
    iw_analogy.box(150 + i * 200, 60, 186, 70, t, f, size=15)
iw_analogy.note(450, 200, "the square empties by itself", "pen")

iw_how = Doodle(760, 400, "How Ana moved the two teams off the old export, from 7 August 2028. First she asked what they needed: finance needs every order by 06:00 on the first working day, the data team needs history. Then she made the new way easier: order events loaded into the warehouse with a ready-made order model, faster and with history. She found an ally, Cho, who had built the payment events finance already trusted. She let the data team lead present it at the monthly engineering meeting, and gave them the credit. The old export was retired on 2 October, without an escalation.",
                 "Their needs first, an easier way, an ally, and their name on the result. Retired without an escalation.")
for i, (t, s, f) in enumerate([("their needs", "06:00 close · history", "y"), ("easier way", "events + ready model", "green"), ("an ally", "Cho, finance trusts", "blue"), ("their credit", "they present it", "paper")]):
    iw_how.box(14 + i * 184, 14, 174, 100, t, f, sub=s, size=16, subsize=13)
iw_how.box(14, 138, 732, 56, "no escalation · no fines · no deadline from above", "pink", size=15)
iw_how.box(14, 214, 732, 56, "old export retired 2 October", "green", size=17)
iw_how.note(380, 306, "influence = their idea, their win, the easy path", "pen", size=16)

INFLUENCE = dict(
    slug="influencing-without-authority",
    kicker="a.k.a. “empty the square without fines”",
    tldr="Architects rarely have authority over the teams whose behaviour they need to change. <b>Influence</b> works through <b>their interests</b> (what do they need?), an <b>easier path</b> (make the right way less work than the old one), <b>allies</b> they already trust, and <b>credit</b> (their name on the result). Escalation is a last resort: it may win once and cost the relationship for years.",
    chips=[("Family", "influence"), ("Origin", "Allan Cohen and David Bradford, <i>Influence Without Authority</i> (1990); Robert Cialdini"), ("Lives in", "conversations, and the paths you build"), ("Pairs with", "golden paths, negotiating with stakeholders, architecture principles")],
    problem_side="Larder, 7 August 2028",
    problem="""  <p class="lead">Two teams still read <b>Larder Core's order tables</b> every night through the old export: the <b>data team</b> for reporting and <b>finance</b> for the monthly close. Neither reports to Ana. FF-11 now flags it, and Ana could <b>escalate to Femke</b>, but <span class="hl-pink">forcing them would make enemies of two teams she needs</span> for years.</p>
  <ul>
    <li>Architects advise; teams decide.</li>
    <li>Rules imposed from above get followed minimally.</li>
    <li>Escalation wins once and costs trust.</li>
  </ul>""",
    problem_figs=[iw_problem],
    analogy_side="the planner and the square",
    analogy="""  <p>A town planner wants people to stop parking on the square. Instead of fines, she <b>asks the shopkeepers what they need</b>, builds a <b>car park two minutes away</b> with a free first hour, and lets the <b>shopkeepers announce it</b>. The square empties by itself, and the shopkeepers thank her.</p>""",
    analogy_figs=[iw_analogy],
    map=[("Parking on the square", "Reading Core's tables through the old export"),
         ("Asking the shopkeepers", "Finance's 06:00 close, the data team's history"),
         ("A car park two minutes away", "Order events in the warehouse, with a ready-made model"),
         ("Shopkeepers announcing it", "The data team lead presenting it"),
         ("Fines", "Escalating to Femke")],
    how_side="needs, an easier path, allies, credit",
    how="""  <p>Ana first <b>asked what they needed</b>: finance needs every order by <b>06:00</b> on the first working day; the data team needs history. She made the new way <b>easier</b>: order events loaded into the warehouse with a <b>ready-made order model</b>, faster than the export and with history. She found an <b>ally</b>, Cho, whose payment events finance already trusted. She let the <b>data team lead present it</b> at the engineering meeting and gave them the credit. The old export was retired on <b>2 October</b>, without an escalation.</p>""",
    how_figs=[iw_how],
    steps=[("Ask what they need", "Their goals and fears, not your rule."),
           ("Make the new way easier", "Less work, faster, better than the old."),
           ("Find allies they trust", "Peers, not managers."),
           ("Let them own it", "Their team builds or presents it."),
           ("Give credit away", "Their name on the win."),
           ("Escalate last", "Only after the easy path exists and is refused.")],
    vocab=[("Influence", "Changing what others do without authority over them."),
           ("Currencies", "What each side values and can trade (Cohen and Bradford)."),
           ("Ally", "Someone the other side trusts who supports the change."),
           ("Easy path", "Making the desired behaviour the simplest one."),
           ("Escalation", "Asking someone with authority to decide."),
           ("Credit", "Public recognition for the result.")],
    code=dict(file="docs/architecture/notes/old-export.md", note="Ana's plan, August 2028", plain=True, src="""
# Retiring the old order export (TD-21) · Ana · no authority over either team

Who        data team (reports to Marco) · finance (monthly close)
Their needs   finance: every order of the month by 06:00, first working day, reconciled
              data team: full history, stable column names, fewer night failures
Easier path   order events → warehouse (CDC from the new Ordering DB) → model "orders_v2"
              ready 06:00 daily (export: 07:30, failed 3× this year) · history from 2024
Ally          Cho: his payment events already feed finance's reconciliation
Ownership     data team builds the orders_v2 model; their lead presents it (4 Sep)
Result        finance's September close on orders_v2 · export retired 2 Oct · no escalation
"""),
    tools="tools: conversations, a working alternative, allies' credibility, public credit; fitness functions to show the problem, not to punish.",
    gains=["<b>Change that sticks</b>.",
           "<b>Relationships kept</b>.",
           "<b>Better solutions</b> from their needs.",
           "<b>Allies for next time</b>.",
           "<b>No escalation</b> needed."],
    losses=["<b>Slower</b> than an order.",
            "<b>Building the easy path</b> takes work.",
            "<b>Credit given away</b>.",
            "<b>Doesn't always work</b>."],
    baseline="Each line compares <b>escalating or imposing a rule</b> to <b>influencing through their needs, an easier path, allies and credit</b>.",
    ratings=[(2, 4, "The reason is explained in their terms."),
             (1, 5, "Both teams wanted the change."),
             (3, 3, "Two months, not a decree."),
             (2, 4, "The export's night failures ended too."),
             (2, 4, "The new path serves future needs."),
             (3, 4, "TD-21 closed with the story."),
             (3, 3, "Neutral."),
             (3, 3, "Conversations and a model."),
             (1, 5, "The teams decided and owned it.")],
    pitfalls=[("Leading with the rule", "“FF-11 says you must.”", "start with their needs."),
              ("No easier path", "Asking them to do more work.", "make the new way easier."),
              ("Keeping the credit", "“Architecture fixed it.”", "their name on it."),
              ("Escalating early", "Femke decides on day one.", "escalate last.")],
    use=["Changes across teams you don't manage.",
         "Retiring old integrations others depend on.",
         "Adopting principles, templates or platforms.",
         "Any time you're tempted to escalate."],
    skip=["Safety, legal or security emergencies: act, then explain."],
    related=["<b>Golden paths</b> (this volume)", "<b>Negotiating with stakeholders</b> (this volume)", "<b>Explaining trade-offs to non-engineers</b> (vol. 3)", "<b>Data ownership &amp; master data</b> (vol. 4)"],
    quiz=[("What are the four levers?", "Their needs, an easier path, allies, and credit."),
          ("What did finance need?", "Every order by 06:00 on the first working day."),
          ("Who was Ana's ally?", "Cho, whose payment events finance already trusted."),
          ("When should you escalate?", "Last, after an easier path exists and is refused.")],
    try_it="Pick a change you need from a team you don't manage. Write down what they need, how you could make the new way easier than the old, who they trust, and how they could take the credit. Then go and ask.",
    remember="Build the <span class=\"hl\">car park</span>; let the shopkeepers <span class=\"hl\">announce</span> it.",
    sources=["Allan Cohen and David Bradford, <i>Influence Without Authority</i>, 3rd ed. (2017).",
             "Robert Cialdini, <i>Influence</i>, new and expanded ed. (2021).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Richard Thaler and Cass Sunstein, <i>Nudge</i> (2008)."],
)

# ------------------------------------------------------------------ 13 Negotiating with Stakeholders
nw_problem = Doodle(760, 280, "Doodle of July 2028. Femke wants Haarlem open on 4 September to hit the board's eight cities. Marco wants the cloud bill flat. Ana needs Ordering's switch finished before a new city starts on the old database. Three reasonable positions, and they collide on one week in September.",
                    "Femke: Haarlem on 4 Sep. Marco: no extra cost. Ana: the switch first. Three positions, one week.")
nw_problem.box(20, 40, 220, 90, "Femke", "y", sub="Haarlem 4 Sep")
nw_problem.box(270, 40, 220, 90, "Marco", "blue", sub="bill flat")
nw_problem.box(520, 40, 220, 90, "Ana", "green", sub="switch first")
nw_problem.note(380, 200, "three positions, one week", "red", size=20)

nw_analogy = Doodle(760, 250, "Doodle of three neighbours sharing a driveway that needs repaving: one wants it before her daughter's wedding, one wants to spend as little as possible, one wants the drain fixed first. Talking about why, they find a plan: drain this week, paving the week after, the cheapest contractor who can do both.",
                     "Three neighbours, one driveway: the wedding, the cost, the drain. Talking about why finds a plan for all three.")
nw_analogy.icon("truck", 30, 60, 1.2)
for i, (t, f) in enumerate([("the wedding", "y"), ("the cost", "blue"), ("the drain", "green")]):
    nw_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
nw_analogy.note(450, 200, "a plan for all three", "pen")

nw_how = Doodle(760, 400, "Ana's negotiation, 17 July 2028. Interests behind the positions: Femke needs eight cities live by the board meeting on 28 September, not 4 September specifically. Marco needs cost per order not to rise. Ana needs Haarlem born on the new database. Options on the table: Haarlem on 11 September, a week later, born on the new database; no extra cloud spend, because the old database's last replica is turned off the same week; and Ana commits to cost per order. Agreed in one meeting; Haarlem opened on 11 September.",
                 "Interests, not positions: the board date, cost per order, the new database. Haarlem a week later, nobody loses.")
nw_how.box(14, 14, 236, 100, "Femke", "y", sub="8 cities by the 28 Sep board", size=16, subsize=12)
nw_how.box(262, 14, 236, 100, "Marco", "blue", sub="cost per order not up", size=16, subsize=13)
nw_how.box(510, 14, 236, 100, "Ana", "green", sub="Haarlem on the new DB", size=16, subsize=13)
nw_how.box(14, 136, 732, 56, "Haarlem 11 Sep (a week later), born on the new database", "paper", size=15)
nw_how.box(14, 208, 732, 56, "old replica off the same week: no extra cloud spend", "paper", size=15)
nw_how.note(380, 300, "agreed in one meeting, written the same day", "pen", size=16)
nw_how.note(380, 334, "Haarlem opened 11 September · 8 cities by the board", "green", size=16)

NEGOTIATE = dict(
    slug="negotiating-with-stakeholders",
    kicker="a.k.a. “three neighbours, one driveway”",
    tldr="When architecture needs time, money or a change of plan, it's a <b>negotiation</b>, not a lecture. Look for the <b>interests</b> behind each stakeholder's position (why that date? why that budget?), put several <b>options</b> on the table that serve all of them, use <b>fair criteria</b> (numbers everyone accepts), and write the agreement down the same day. Most deadlocks between leaders are positions colliding while their interests don't.",
    chips=[("Family", "influence"), ("Origin", "Roger Fisher and William Ury, <i>Getting to Yes</i> (1981)"), ("Lives in", "one meeting with options prepared, and a written agreement"), ("Pairs with", "influencing without authority, trade-off sliders, negotiating scope (Grace)")],
    problem_side="Larder, 17 July 2028",
    problem="""  <p class="lead">Femke wants <b>Haarlem open on 4 September</b> for the board's eight cities. Marco wants the <b>cloud bill flat</b>. Ana needs <b>Ordering's switch</b> finished before a new city starts on the old database. <span class="hl-pink">Three reasonable positions, colliding on one week in September.</span></p>
  <ul>
    <li>Positions sound fixed; interests rarely are.</li>
    <li>Architects arguing “technical reasons” lose to dates.</li>
    <li>Unwritten agreements get remembered differently.</li>
  </ul>""",
    problem_figs=[nw_problem],
    analogy_side="three neighbours and a driveway",
    analogy="""  <p>Three neighbours share a driveway that needs repaving: one wants it done <b>before her daughter's wedding</b>, one wants to <b>spend as little as possible</b>, one wants the <b>drain fixed first</b>. Talking about why, they find a plan: drain this week, paving the next, the cheapest contractor who can do both. Nobody gives anything up.</p>""",
    analogy_figs=[nw_analogy],
    map=[("The wedding", "Eight cities by the 28 September board"),
         ("Spending as little as possible", "Cost per order not rising"),
         ("The drain first", "Haarlem born on the new database"),
         ("Drain this week, paving next", "Haarlem a week later, on 11 September"),
         ("The cheapest contractor", "The old replica switched off the same week")],
    how_side="interests, options, fair criteria, in writing",
    how="""  <p>Ana asked <b>why</b> before the meeting. Femke needed <b>eight cities by the board on 28 September</b>, not the 4th specifically. Marco needed <b>cost per order</b> not to rise. Ana needed Haarlem <b>born on the new database</b>. She brought <b>options</b>: Haarlem on <b>11 September</b>, born on the new database; the old database's last replica switched off the same week, so <b>no extra cloud spend</b>; her commitment on cost per order. Agreed in <b>one meeting</b>, written the same day. Haarlem opened on 11 September.</p>""",
    how_figs=[nw_how],
    steps=[("Ask why, before the meeting", "Each position's real interest."),
           ("Find fair criteria", "Board dates, cost per order: numbers all accept."),
           ("Prepare several options", "Each serving every interest somewhat."),
           ("Talk interests in the room", "Not technical reasons."),
           ("Agree and write it down", "The same day, to everyone."),
           ("Keep your side", "And report when you have.")],
    vocab=[("Position", "What someone says they want."),
           ("Interest", "Why they want it."),
           ("Option", "A possible agreement."),
           ("Fair criteria", "Standards both sides accept to judge options."),
           ("BATNA", "Best alternative to a negotiated agreement."),
           ("Stakeholder", "Someone with a stake in the outcome.")],
    code=dict(file="planning/2028-07-17-haarlem.md", note="the written agreement, 17 July 2028", plain=True, src="""
# Haarlem opening and the Ordering switch · agreed 17 Jul 2028 · Femke, Marco, Ana (Joost, Sanne cc)

Interests   Femke: 8 cities live before the board, 28 Sep
            Marco: cost per order does not rise in Q3
            Ana:   Haarlem born on the new Ordering database (no second migration)
Agreed      Haarlem opens Mon 11 Sep (was 4 Sep), on the new database
            Old Core order replica switched off week of 11 Sep (≈ €1,900/month saved)
            → no extra cloud spend; Ana reports cost per order at the board
Not agreed  (none)
Result      Haarlem opened 11 Sep · 8 cities at the 28 Sep board · cost per order flat
"""),
    tools="tools: one-to-one conversations before the meeting, options on one page, numbers everyone trusts, a written agreement.",
    gains=["<b>Agreements</b> instead of deadlocks.",
           "<b>Everyone's real need met</b>.",
           "<b>Architecture needs</b> heard in business terms.",
           "<b>One meeting</b>, prepared.",
           "<b>Trust</b> for the next negotiation."],
    losses=["<b>Preparation</b> before the meeting.",
            "<b>Some positions</b> really are fixed.",
            "<b>Compromises</b> cost something.",
            "<b>Needs credibility</b> with leaders."],
    baseline="Each line compares <b>arguing positions with technical reasons</b> to <b>finding interests, preparing options and agreeing in writing</b>.",
    ratings=[(2, 4, "The agreement fits on one page."),
             (1, 5, "Femke, Marco and Ana each got their need."),
             (2, 5, "One meeting."),
             (2, 4, "No city on the old database."),
             (3, 4, "Options, not ultimatums."),
             (2, 4, "Written the same day."),
             (2, 4, "Cost per order kept flat."),
             (3, 3, "Preparation conversations."),
             (3, 3, "Neutral.")],
    pitfalls=[("Technical arguments", "“The database isn't ready.”", "their interests, in their terms."),
              ("One option", "Take it or leave it.", "several prepared."),
              ("Meeting cold", "Interests discovered in the room.", "ask why beforehand."),
              ("Nothing written", "Remembered differently.", "write it the same day.")],
    use=["When architecture needs time or money.",
         "Conflicting dates between business and platform work.",
         "Budget and capacity discussions.",
         "Vendor and partner agreements."],
    skip=["Decisions inside your own authority."],
    related=["<b>Influencing without authority</b> (this volume)", "<b>Trade-off sliders</b> (vol. 2)", "<b>Negotiating scope</b> (Grace, book 2 vol. 5)", "<b>Presenting to executives</b> (vol. 3)"],
    quiz=[("What's behind each position?", "An interest: why they want it."),
          ("What did Femke really need?", "Eight cities live before the 28 September board."),
          ("What kept the bill flat?", "Switching off the old replica the same week."),
          ("When was it written down?", "The same day.")],
    try_it="Think of a conflict between your architecture needs and someone's date or budget. Write each side's position and the interest behind it, then three options that serve every interest. Take them to one meeting.",
    remember="Ask about the <span class=\"hl\">wedding</span> and the <span class=\"hl\">drain</span> before you argue about the driveway.",
    sources=["Roger Fisher, William Ury and Bruce Patton, <i>Getting to Yes</i>, 3rd ed. (2011).",
             "William Ury, <i>Getting Past No</i> (1991).",
             "Deepak Malhotra and Max Bazerman, <i>Negotiation Genius</i> (2007).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020)."],
)

# ------------------------------------------------------------------ 14 Discovery Workshops
dw_problem = Doodle(760, 280, "Doodle of June 2028. Femke has met a rail company and wants Larder lockers at train stations: order on the train, collect on the way home. She asks Ana for a technical design by Friday. Nobody has asked customers, Joost, Lena or Marco, and nobody knows which assumptions matter.",
                    "Femke wants station lockers and asks for a technical design by Friday. Nobody knows which assumptions matter.")
dw_problem.box(20, 40, 320, 90, "station lockers", "y", sub="Femke's idea")
dw_problem.box(400, 40, 340, 90, "design by Friday", "pink", sub="before anyone asked why", stroke="red")
dw_problem.note(380, 200, "the solution before the questions", "red", size=19)

dw_analogy = Doodle(760, 250, "Doodle of an expedition team planning around a map on a table: the guide, the doctor, the cook and the sponsor each mark what they know and what worries them, before anyone chooses a route.",
                     "An expedition around the map: guide, doctor, cook and sponsor mark what they know and fear, before choosing a route.")
dw_analogy.icon("map", 30, 60, 1.2)
for i, (t, f) in enumerate([("guide", "y"), ("doctor", "pink"), ("cook", "green"), ("sponsor", "blue")]):
    dw_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=16)
dw_analogy.note(450, 200, "everyone at the map before the route", "pen")

dw_how = Doodle(760, 400, "Ana's discovery workshop on station lockers, 3 and 4 July 2028, with Femke, Joost, Grace, Lena, Marco, Eli and a rail company manager. Day one: the customer journey and an event storm of a locker order; the riskiest assumptions mapped: do commuters want it, can a locker keep chilled food safe for two hours, who pays for the lockers. Day two: three options from manual to fully integrated, and a test for the riskiest assumptions. Outcome: a six-week pilot with two chilled lockers at Utrecht Centraal, orders routed by hand, no new systems.",
                 "Two days, the right people: journey, event storm, riskiest assumptions, options, a test. A pilot, not a design.")
for i, (t, s, f) in enumerate([("day 1", "journey · event storm", "y"), ("assumptions", "want it? chilled 2 h? who pays?", "pink"), ("day 2", "3 options · a test", "blue")]):
    dw_how.box(14 + i * 248, 14, 236, 100, t, f, sub=s, size=17, subsize=13)
dw_how.box(14, 136, 732, 56, "Femke · Joost · Grace · Lena · Marco · Eli · rail company", "paper", size=14)
dw_how.box(14, 212, 732, 70, None, "green")
dw_how.head(380, 240, "6-week pilot: 2 chilled lockers, Utrecht Centraal", size=16)
dw_how.text(380, 268, "orders routed by hand · no new systems", size=14)
dw_how.note(380, 322, "a test of the riskiest assumptions, not a design", "pen", size=16)

DISCOVERY = dict(
    slug="discovery-workshops",
    kicker="a.k.a. “everyone at the map”",
    tldr="A <b>discovery workshop</b> brings the people who know the business, the customers, operations, the law and the systems into one room to explore a new idea <b>before</b> anyone designs it. Map the journey and the events, surface the <b>riskiest assumptions</b>, sketch a few <b>options</b> (from manual to fully built), and leave with a <b>cheap test</b> rather than a design. The architect's job is to facilitate and to make the technical options and costs visible.",
    chips=[("Family", "influence"), ("Origin", "event storming (Alberto Brandolini), design sprints, lean discovery"), ("Lives in", "a one- or two-day workshop and a short write-up"), ("Pairs with", "domain discovery (event storming), assumption mapping, spike vs prototype vs PoC")],
    problem_side="Larder, 3 July 2028",
    problem="""  <p class="lead">Femke has met a rail company and wants <b>Larder lockers at train stations</b>: order on the train, collect on the way home. She asks Ana for a <b>technical design by Friday</b>. <span class="hl-pink">Nobody has asked customers, Joost, Lena or Marco</span>, and nobody knows which assumptions matter.</p>
  <ul>
    <li>Designs made too early solve the wrong problem.</li>
    <li>Each function knows a different risk.</li>
    <li>Big ideas need a cheap test before a build.</li>
  </ul>""",
    problem_figs=[dw_problem],
    analogy_side="everyone at the map",
    analogy="""  <p>Before an expedition chooses a route, the <b>guide</b>, the <b>doctor</b>, the <b>cook</b> and the <b>sponsor</b> stand around the map. Each marks what they know and what worries them: a river crossing, altitude sickness, how much food fits, how much it costs. Only then do they choose, and they choose a short trial walk first.</p>""",
    analogy_figs=[dw_analogy],
    map=[("The map on the table", "The customer journey and the event storm"),
         ("The guide, doctor, cook, sponsor", "Joost, Lena, Grace, Marco, the rail company"),
         ("Marking what worries them", "The riskiest assumptions"),
         ("Possible routes", "Three options, manual to integrated"),
         ("A trial walk", "Six weeks, two lockers, orders by hand")],
    how_side="the right people, assumptions, options, a test",
    how="""  <p>Instead of a design, Ana ran a <b>two-day workshop</b> with Femke, Joost, Grace, Lena, Marco, Eli and a rail company manager. Day one: the <b>customer journey</b> and an <b>event storm</b> of a locker order; the <b>riskiest assumptions</b>: do commuters want it, can a locker keep chilled food safe for two hours, who pays for the lockers. Day two: <b>three options</b> from manual to fully integrated, and a <b>test</b>. Outcome: a <b>six-week pilot</b> with two chilled lockers at <b>Utrecht Centraal</b>, orders routed by hand, no new systems.</p>""",
    how_figs=[dw_how],
    steps=[("Invite every kind of knowledge", "Business, customers, operations, legal, engineering, partners."),
           ("Start from the customer journey", "And the events in the domain."),
           ("Surface the riskiest assumptions", "What must be true; how sure are we?"),
           ("Sketch options", "From manual to fully built, with rough costs."),
           ("Choose a cheap test", "For the riskiest assumptions."),
           ("Write it up in a page", "Assumptions, options, the test, the decision date.")],
    vocab=[("Discovery", "Learning what to build before building it."),
           ("Event storming", "Mapping a domain's events with sticky notes."),
           ("Assumption", "Something believed but not yet shown."),
           ("Pilot", "A small, real trial."),
           ("Facilitator", "The person who runs the session and keeps it moving."),
           ("Wizard of Oz", "Doing by hand what software would do, behind the scenes.")],
    code=dict(file="discovery/2028-07-station-lockers.md", note="the write-up, 4 July 2028", plain=True, src="""
# Discovery: station lockers · 3–4 Jul 2028 · facilitated by Ana
With: Femke, Joost, Grace, Lena, Marco, Eli, a rail company manager

Riskiest assumptions                               confidence   test
  A1 commuters will order for station pick-up       low          pilot demand
  A2 a locker keeps chilled food safe for 2 h       medium       temperature logging
  A3 the rail company pays for lockers, we pay rent  low          contract talk (Femke)
  A4 lockers fit our dispatch (vans before 15:00)   high         —
Options   1 manual: lockers, orders flagged, couriers by hand (≈ €8k)
          2 semi: locker codes by SMS from Ordering (≈ 4 weeks)
          3 integrated: locker partner API, slots, live status (≈ 3 months)
Decision  option 1 as a 6-week pilot, 2 chilled lockers, Utrecht Centraal, from 4 Sep
          review 16 Oct: A1 and A2 results → option 2 or stop
"""),
    tools="tools: a room, sticky notes or a whiteboard tool, a journey map, event storming, an assumption map; a one-page write-up.",
    gains=["<b>The right questions</b> before designs.",
           "<b>Every function's risks</b> on one wall.",
           "<b>A cheap test</b> instead of a big build.",
           "<b>Shared ownership</b> of the idea.",
           "<b>Faster</b> than design-review cycles."],
    losses=["<b>Two days</b> of busy people.",
            "<b>Needs good facilitation</b>.",
            "<b>Leaders may want</b> an answer, not a test.",
            "<b>Partners</b> in the room need care."],
    baseline="Each line compares <b>an architect designing a new idea alone by Friday</b> to <b>a discovery workshop with every kind of knowledge, ending in a cheap test</b>.",
    ratings=[(2, 4, "One page of assumptions and options."),
             (1, 5, "Femke, Joost, Lena and Marco shaped it."),
             (2, 4, "A decision in two days."),
             (1, 5, "No three-month build on untested assumptions."),
             (2, 4, "Three options kept open."),
             (2, 4, "Write-up with a review date."),
             (2, 4, "€8k pilot instead of a project."),
             (3, 3, "Two days of leaders' time."),
             (3, 3, "Neutral.")],
    pitfalls=[("Designing first", "A solution by Friday.", "explore before designing."),
              ("Only engineers", "Operations and legal missing.", "every kind of knowledge."),
              ("No assumptions", "Everything taken as true.", "map the riskiest."),
              ("A design as the output", "Months of work agreed.", "a cheap test.")],
    use=["New business ideas and partnerships.",
         "When leaders bring a solution, not a problem.",
         "Before big investments.",
         "Cross-functional changes."],
    skip=["Small, well-understood changes."],
    related=["<b>Domain discovery (event storming)</b> (vol. 1)", "<b>Assumption mapping</b> (Grace, book 2 vol. 1)", "<b>Spike vs prototype vs PoC</b> (vol. 1)", "<b>Concierge &amp; Wizard-of-Oz MVP</b> (Grace, book 2 vol. 1)"],
    quiz=[("What should a discovery workshop end with?", "A cheap test of the riskiest assumptions, not a design."),
          ("Who should be in the room?", "Every kind of knowledge: business, operations, legal, engineering, partners."),
          ("What were the riskiest assumptions?", "Commuter demand, chilled food safe for two hours, who pays."),
          ("What did Larder decide?", "A six-week manual pilot with two lockers at Utrecht Centraal.")],
    try_it="Take the next big idea a leader brings you. Instead of designing it, plan a one-day workshop: who must be there, the journey to map, and three assumptions you suspect are riskiest.",
    remember="Put everyone at the <span class=\"hl\">map</span> before choosing the <span class=\"hl\">route</span>.",
    sources=["Alberto Brandolini, <i>Introducing EventStorming</i> (Leanpub, 2021).",
             "Jake Knapp et al., <i>Sprint</i> (2016).",
             "David Bland and Alexander Osterwalder, <i>Testing Business Ideas</i> (2019).",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021)."],
)

# ------------------------------------------------------------------ 15 Growing Other Architects
ga_problem = Doodle(760, 280, "Doodle of September 2028. The top risk on the register since April: architecture depends on one person, Ana. With eight cities and five teams, every one-way door still finds its way to her. If she's ill, on holiday or leaves, decisions stop, or get made without anyone thinking about the whole.",
                    "Risk #1 since April: architecture depends on one person. If Ana is away, decisions stop.")
ga_problem.box(200, 40, 360, 90, "Ana", "pink", sub="every one-way door", stroke="red")
ga_problem.note(380, 200, "a single point of failure, with a name", "red", size=19)

ga_analogy = Doodle(760, 250, "Doodle of a head chef growing sous-chefs: they cook beside her first, then run a station, then design a dish with her tasting, then run the kitchen on her day off. She stops cooking every plate and starts teaching.",
                     "A head chef grows sous-chefs: beside her, then a station, then a dish, then the kitchen on her day off.")
ga_analogy.icon("kitchen", 30, 60, 1.2)
for i, (t, f) in enumerate([("beside her", "paper"), ("a station", "y"), ("a dish", "blue"), ("her day off", "green")]):
    ga_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=15)
ga_analogy.note(450, 200, "from cooking every plate to teaching", "pen")

ga_how = Doodle(760, 400, "How Ana grew two architects from May to September 2028. Cho for payments and data, Dee for mobile and the customer apps. Step by step: pairing on ADRs; leading lightweight reviews with Ana as second reviewer; running the monthly architecture kata; then owning one-way doors in their domains alone. Also: a fortnightly architecture guild open to any engineer, and an architecture path in the engineering career ladder. By September Cho led ADR 0029 on a third payment method without Ana; risk number 1 dropped from 4 by 4 to 2 by 4.",
                 "Pair, then lead with Ana second, then own a domain alone. Risk #1: 4 × 4 → 2 × 4.")
for i, (t, s, f) in enumerate([("pair", "on ADRs", "paper"), ("lead", "reviews, Ana second", "y"), ("run", "the monthly kata", "blue"), ("own", "one-way doors alone", "green")]):
    ga_how.box(14 + i * 184, 14, 174, 90, t, f, sub=s, size=18, subsize=13)
    if i:
        ga_how.arrow(14 + i * 184 - 8, 59, 14 + i * 184 - 2, 59)
ga_how.box(14, 126, 360, 70, "Cho", "y", sub="payments + data", size=17)
ga_how.box(386, 126, 360, 70, "Dee", "blue", sub="mobile + customer apps", size=17)
ga_how.box(14, 216, 732, 56, "guild fortnightly · architecture path on the career ladder", "paper", size=15)
ga_how.note(380, 310, "Sep: Cho leads ADR 0029 alone · risk #1: 4 × 4 → 2 × 4", "green", size=15)

GROWING = dict(
    slug="growing-architects",
    kicker="a.k.a. “growing sous-chefs”",
    tldr="An architect who makes every important decision becomes the organisation's single point of failure. <b>Growing other architects</b> spreads the thinking: <b>pair</b> with engineers on decisions, let them <b>lead</b> reviews with you as second, give them <b>domains</b> where they own the one-way doors, run a <b>guild</b> and katas open to all, and make architecture a <b>path on the career ladder</b>. Your job shifts from deciding to teaching, and the organisation keeps thinking about the whole when you're not there.",
    chips=[("Family", "influence"), ("Origin", "apprenticeship; Andrew Harmel-Law's “advice process”; staff-engineer practice"), ("Lives in", "pairing, the review rotation, a guild and the career ladder"), ("Pairs with", "architecture katas, lightweight review, risk register")],
    problem_side="Larder, 18 September 2028",
    problem="""  <p class="lead">Since April the top risk on the register has been: <b>architecture depends on one person</b>, Ana. With eight cities and five teams, every one-way door still finds its way to her. <span class="hl-pink">If she's ill, on holiday or leaves, decisions stop</span>, or get made without anyone thinking about the whole.</p>
  <ul>
    <li>One architect doesn't scale with the organisation.</li>
    <li>Engineers who never decide never learn to.</li>
    <li>Knowledge in one head leaves with that person.</li>
  </ul>""",
    problem_figs=[ga_problem],
    analogy_side="growing sous-chefs",
    analogy="""  <p>A head chef grows her <b>sous-chefs</b>: first they cook <b>beside her</b>, then they run a <b>station</b>, then they design a <b>dish</b> while she tastes, then they run the kitchen on <b>her day off</b>. She stops cooking every plate and starts teaching, and the kitchen gets better, not worse.</p>""",
    analogy_figs=[ga_analogy],
    map=[("Cooking beside her", "Pairing on ADRs"),
         ("Running a station", "Leading reviews with Ana as second reviewer"),
         ("Designing a dish", "Owning one-way doors in a domain"),
         ("Her day off", "Cho leading ADR 0029 without Ana"),
         ("The kitchen staff", "The architecture guild, open to all")],
    how_side="pair, lead, own; a guild and a path",
    how="""  <p>From May, Ana grew <b>Cho</b> (payments and data) and <b>Dee</b> (mobile and customer apps): <b>pairing</b> on ADRs; <b>leading reviews</b> with Ana second; <b>running the monthly kata</b>; then <b>owning one-way doors</b> in their domains alone. A fortnightly <b>architecture guild</b> is open to any engineer, and the career ladder now has an <b>architecture path</b>. In September Cho led <b>ADR 0029</b> (a third payment method) without Ana. Risk #1 dropped from <b>4 × 4 to 2 × 4</b>.</p>""",
    how_figs=[ga_how],
    steps=[("Pick people with the interest", "Engineers who already think about the whole."),
           ("Pair on real decisions", "ADRs, reviews, workshops."),
           ("Let them lead, with you second", "And give feedback afterwards."),
           ("Give them domains", "Where they own the one-way doors."),
           ("Open the practice to all", "A guild, katas, shared reviews."),
           ("Make it a career path", "Recognised in the ladder and pay.")],
    vocab=[("Apprenticeship", "Learning by doing beside someone experienced."),
           ("Architecture guild", "A regular, open meeting for architecture practice."),
           ("Advice process", "Anyone may decide, after seeking advice from those affected."),
           ("Career ladder", "Defined levels and paths for engineers."),
           ("Domain", "A part of the system a person or team owns."),
           ("Staff engineer", "A senior engineer who works across teams.")],
    code=dict(file="docs/architecture/practice.md", note="how architecture is practised, September 2028", plain=True, src="""
# Architecture practice at Larder · Sep 2028

Architects      Ana (lead, whole platform) · Cho (payments + data) · Dee (mobile + customer apps)
How they grew   May: pairing on ADRs · Jun: leading reviews, Ana second · Jul: running the kata ·
                Sep: owning one-way doors in their domains (Cho: ADR 0029, third payment method)
Guild           every other Thursday, 45 min, open to all engineers (avg. 11 attend)
Reviews         rotation: Ana, Cho, Dee + one tech lead per review
Career ladder   engineering → staff engineer → architect path (levels and examples, from Oct)
Risk #1         "architecture depends on one person": 4 × 4 (Apr) → 2 × 4 (Sep)
"""),
    tools="tools: pairing time, the review rotation, the monthly kata, a guild slot, the career ladder; patience.",
    gains=["<b>No single point of failure</b>.",
           "<b>Decisions closer to teams</b>.",
           "<b>Engineers grow</b> and stay.",
           "<b>Ana thinks</b> about the whole again.",
           "<b>Better decisions</b>, from more viewpoints."],
    losses=["<b>Slower decisions</b> while people learn.",
            "<b>Some decisions</b> differ from Ana's.",
            "<b>Teaching takes time</b>.",
            "<b>Pay and titles</b> must follow."],
    baseline="Each line compares <b>one architect making every important decision</b> to <b>growing architects through pairing, leading, domain ownership, a guild and a career path</b>.",
    ratings=[(3, 4, "Three people explain the architecture, not one."),
             (2, 4, "Teams talk to an architect in their domain."),
             (2, 4, "Decisions don't wait for Ana."),
             (1, 5, "Risk #1 halved."),
             (2, 4, "More viewpoints, more options."),
             (3, 4, "Every decision still recorded."),
             (3, 3, "Neutral."),
             (3, 3, "Teaching time each week."),
             (1, 5, "Domains own their decisions.")],
    pitfalls=[("Delegating without teaching", "“You decide now.”", "pair first, then lead with you second."),
              ("Only titles", "Architects in name, Ana decides.", "real one-way doors to own."),
              ("A closed club", "Architecture for the chosen few.", "a guild open to all."),
              ("No career path", "They grow, then leave.", "a recognised path and pay.")],
    use=["When the architect is a bottleneck or a single point of failure.",
         "Growing organisations.",
         "Engineers asking how to grow beyond their team.",
         "Before the architect moves on."],
    skip=["Never; even a team of one benefits from a second opinion."],
    related=["<b>Architecture katas</b> (vol. 3)", "<b>Lightweight architecture review</b> (this volume)", "<b>Risk register</b> (this volume)", "<b>Hiring a product owner</b> (Grace, book 2 vol. 6)"],
    quiz=[("What's the sequence for growing an architect?", "Pair, lead with you as second, then own a domain's one-way doors."),
          ("Who did Ana grow?", "Cho (payments and data) and Dee (mobile and customer apps)."),
          ("What showed it worked?", "Cho led ADR 0029 alone; risk #1 dropped to 2 × 4."),
          ("Why a career path?", "So people who grow are recognised and stay.")],
    try_it="Pick one engineer who thinks about the whole system. Pair with them on your next decision, let them lead the one after with you as second, and agree a domain they'll own within six months.",
    remember="Stop cooking every <span class=\"hl\">plate</span>; grow the <span class=\"hl\">sous-chefs</span>.",
    sources=["Andrew Harmel-Law, <i>Facilitating Software Architecture</i> (2024).",
             "Tanya Reilly, <i>The Staff Engineer's Path</i> (2022).",
             "Will Larson, <i>Staff Engineer</i> (2021).",
             "Ted Neward, architecture katas (architecturalkatas.com)."],
)

NOTES = [INFLUENCE, NEGOTIATE, DISCOVERY, GROWING]
