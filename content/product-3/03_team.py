# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 3 · Working with the team.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 08 The Product Trio
pt_problem = Doodle(760, 280, "Doodle of how work flowed before February 2026. Grace interviews customers alone, writes a spec, and hands it to Dee for screens; Dee hands them to Ben's engineers. Each hand-off loses something. The engineers have never met a customer or a picker.",
                    "Grace interviews, writes, hands over; design hands over; engineers build. Each hand-off loses something.")
for i, (t, s, f) in enumerate([("Grace", "interviews alone", "y"), ("spec", "12 pages", "paper"), ("screens", "Dee, evenings", "blue"), ("engineers", "never met users", "pink")]):
    x = 14 + i * 188
    pt_problem.box(x, 50, 170, 90, t, f, sub=s, size=17, subsize=13)
    if i < 3:
        pt_problem.arrow(x + 172, 95, x + 186, 95)
pt_problem.note(380, 200, "each arrow loses something", "red", size=20)

pt_analogy = Doodle(760, 260, "Doodle of a film crew scouting a location together: the director (does it serve the story?), the cinematographer (can we shoot it well?) and the producer (can we afford it?). They decide on the spot instead of passing memos for a month.",
                     "The director, cinematographer and producer scout the location together, and decide on the spot.")
pt_analogy.icon("camera", 40, 60, 1.3)
for i, (t, s, f) in enumerate([("director", "serves the story?", "y"), ("cinematographer", "can we shoot it?", "blue"), ("producer", "can we afford it?", "green")]):
    x = 160 + i * 196
    pt_analogy.box(x, 60, 184, 84, t, f, sub=s, size=15, subsize=13)
pt_analogy.note(450, 210, "together, on the spot", "pen")

pt_how = Doodle(760, 360, "Larder's ordering trio from 9 February 2026: Grace for value and viability, Noor for usability, Ben for feasibility. The overlap in the middle is where good solutions live. Their weekly rhythm: Thursday 16:00, one customer interview together; one store visit a fortnight with Tomás's pickers; the opportunity tree updated together on Fridays.",
                 "Three views, one decision. Value, usable, feasible, and a weekly rhythm that keeps the trio close to customers.")
pt_how.circle(200, 150, 110, fill="y")
pt_how.circle(330, 150, 110, fill="blue")
pt_how.circle(265, 245, 110, fill="green")
for x, y, t, s in [(150, 110, "Grace", "valuable?"), (380, 110, "Noor", "usable?"), (265, 300, "Ben", "feasible?")]:
    pt_how.text(x, y, t, "t-head", size=17)
    pt_how.text(x, y + 24, s, size=14)
pt_how.box(500, 30, 246, 300, None, "paper")
pt_how.head(623, 62, "every week", size=17)
for i, t in enumerate(["Thu 16:00 · 1 interview", "together, all three", "fortnightly: Noord", "with Tomás's pickers", "Fri: tree, together"]):
    pt_how.text(623, 104 + i * 40, t, size=15)

TRIO = dict(
    slug="product-trio",
    kicker="a.k.a. “scouting the location together”",
    tldr="Hand-offs (PO to designer to engineers) lose what each person learned. A <b>product trio</b> (the product owner, a designer and a tech lead) does <b>discovery together</b>: they interview customers <b>together, every week</b>, visit the people who use the product, and decide on solutions as one group. The PO brings <b>value and viability</b>, the designer <b>usability</b>, the tech lead <b>feasibility</b>. Good solutions live where all three overlap.",
    chips=[("Family", "working with the team"), ("Origin", "Teresa Torres, <i>Continuous Discovery Habits</i> (2021); Marty Cagan's product team (<i>Inspired</i>)"), ("Lives in", "a weekly calendar slot and a shared opportunity tree"), ("Pairs with", "customer interviews, opportunity solution tree, refinement")],
    problem_side="Larder, 9 February 2026",
    problem="""  <p class="lead">Until February, Grace interviewed customers <b>alone</b>, wrote a twelve-page spec, and handed it to Dee, who drew screens in the evenings between mobile work; Dee handed them to Ben's engineers. <span class="hl-pink">The engineers had never met a customer or a picker.</span> Each hand-off lost something: why a feature mattered, what the customer actually said, what the pickers' gloves are like.</p>
  <ul>
    <li>Knowledge stays with whoever did the research.</li>
    <li>Feasibility arrives late, after the design is “done”.</li>
    <li>Engineers build what's written, not what's needed.</li>
  </ul>""",
    problem_figs=[pt_problem],
    analogy_side="the location scout",
    analogy="""  <p>A film crew scouts locations with three people: the <b>director</b> (does it serve the story?), the <b>cinematographer</b> (can we shoot it well here?) and the <b>producer</b> (can we afford it, and get permits?). They stand in the same street and decide <b>together, on the spot</b>, instead of passing memos for a month.</p>""",
    analogy_figs=[pt_analogy],
    map=[("The director", "Grace: valuable and viable?"),
         ("The cinematographer", "Noor: usable?"),
         ("The producer", "Ben: feasible, and at what cost?"),
         ("Standing in the street", "Interviewing customers and visiting Noord together"),
         ("Deciding on the spot", "Choosing solutions on the tree, together")],
    how_side="three views, one weekly rhythm",
    how="""  <p>When Noor joined as product designer on 9 February, Grace, Noor and Ben became a trio. Every Thursday at 16:00 they interview <b>one customer together</b>; every other week they visit <b>Noord</b> to watch Tomás's pickers. It paid off fast: during slice 1, Ben watched a picker stand waiting for an answer and suggested applying answers <b>at packing</b>, the fix that made slice 2 work.</p>""",
    how_figs=[pt_how],
    steps=[("Name the trio", "Product owner, designer, tech lead: the same three people for an area."),
           ("Book a weekly interview", "One customer, 30 minutes, all three present; take turns asking."),
           ("Visit the real users", "Stores, warehouses, offices: watch the work, not a demo."),
           ("Share one opportunity tree", "Update it together, every week."),
           ("Decide solutions together", "Value, usability and feasibility in one conversation."),
           ("Bring the team along", "Rotate an engineer into the interview now and then.")],
    vocab=[("Product trio", "PO, designer and tech lead doing discovery together."),
           ("Discovery", "Finding out what to build: interviews, tests, research."),
           ("Delivery", "Building and shipping it."),
           ("Viability", "Does it work for the business: cost, law, operations?"),
           ("Feasibility", "Can we build and run it, with our people and systems?"),
           ("Usability", "Can people use it, easily and without errors?")],
    code=dict(file="team/ordering/trio.md", note="the trio's working agreement, February 2026", plain=True, src="""
# Ordering trio · Grace (product) · Noor (design) · Ben (tech lead)        from 9 Feb 2026

Every week
  Thu 16:00–16:45   one customer interview, all three (recruited by Sam's team)
  Fri 09:30–10:00   update the opportunity tree together
Every other week
  Tue 17:00–18:30   Noord: watch picking at peak with Tomás
Decisions
  Solutions are chosen by the three of us; if we disagree, Grace decides on value,
  Ben on feasibility, Noor on usability, and we write down why.
Bringing others in
  One engineer joins an interview each month (rotating).
"""),
    tools="tools: a calendar slot, an interview guide (Vol. 1), the shared opportunity tree; interview scheduling tools (Calendly, Great Question, Ethnio) once it's a habit.",
    gains=["<b>No lossy hand-offs</b>: all three heard the customer.",
           "<b>Feasibility early</b>: Ben's packing idea came from a store visit.",
           "<b>Better solutions</b> in the overlap.",
           "<b>Engineers see why</b>, through the tech lead.",
           "<b>Faster decisions</b>: no memos between three desks."],
    losses=["<b>Two to three hours a week</b> from a tech lead and a designer.",
            "<b>Needs a designer</b> (Larder hired one).",
            "<b>Can exclude the rest of the team</b> if not rotated.",
            "<b>Disagreements need a rule</b>."],
    baseline="Each line compares <b>a PO who researches alone and hands over a spec</b> to <b>a product trio that interviews, visits and decides together every week</b>.",
    ratings=[(2, 5, "All three hear customers and pickers directly."),
             (3, 4, "Viability stays in the room with usability and feasibility."),
             (2, 4, "Decisions rest on what all three saw."),
             (2, 4, "Ideas are tested together within a week."),
             (3, 4, "One shared tree, one priority."),
             (1, 5, "Design and engineering know the why first-hand."),
             (3, 3, "Neutral."),
             (2, 4, "No spec waiting for screens waiting for engineers."),
             (3, 3, "A few hours a week for three people.")],
    pitfalls=[("A trio in name only", "Grace still interviews alone; Noor and Ben read notes.", "all three in the interview, every week."),
              ("A closed club", "The rest of the team feels shut out.", "rotate engineers into interviews."),
              ("No disagreement rule", "Stalemates between the three.", "agree who decides what, and write down why."),
              ("Discovery only", "The trio stops at the idea.", "stay together through delivery and the launch.")],
    use=["Any product area with a PO, a designer and engineers.",
         "When specs keep getting misread.",
         "When engineers never meet users.",
         "Continuous discovery alongside delivery."],
    skip=["Very small teams where everyone already interviews.",
          "Pure platform work with no end users."],
    related=["<b>Refinement that isn't a meeting marathon</b> (this volume)", "<b>Customer interviews</b> (Vol. 1)", "<b>Opportunity solution tree</b> (Vol. 1)", "<b>Working with the architect</b> (Vol. 5)"],
    quiz=[("Who's in a product trio?", "The product owner, a designer and a tech lead."),
          ("What does each bring?", "PO: value and viability. Designer: usability. Tech lead: feasibility."),
          ("What's the weekly habit?", "Interviewing one customer together."),
          ("What came from Ben's store visit?", "Applying answers at packing, so pickers never wait.")],
    try_it="Book a 45-minute customer interview next week with your designer and tech lead in the room. Take turns asking. Afterwards, spend 15 minutes on what each of you heard that the others didn't, and put one change on the opportunity tree.",
    remember="Scout the location <span class=\"hl\">together</span>. Value, usable, feasible: decide <span class=\"hl\">on the spot</span>.",
    sources=["Teresa Torres, <i>Continuous Discovery Habits</i> (2021).",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017) and <i>Empowered</i> (2020).",
             "Jeff Gothelf and Josh Seiden, <i>Lean UX</i>, 3rd ed. (2021).",
             "Christian Idiodi et al., <i>Transformed</i> (2024)."],
)

# ------------------------------------------------------------------ 09 Sprint Goals
sg_problem = Doodle(760, 280, "Doodle of sprint 6 in March 2026: fourteen tickets and no goal. Midway, an urgent request from Sam takes three days. Nobody can say whether it mattered more than the sprint's work, because the sprint was a list, not a purpose.",
                    "Fourteen tickets, no goal. Sam's urgent request takes three days; was it worth it? Nobody can say.")
for i in range(7):
    sg_problem.box(20, 20 + i * 30, 280, 24, None, ["paper", "blue", "y"][i % 3], rx=3)
sg_problem.note(160, 250, "sprint 6: 14 tickets", "pen")
sg_problem.box(380, 40, 360, 80, "Sam: “urgent!”", "pink", sub="3 days", stroke="red")
sg_problem.box(380, 150, 360, 70, "worth it? nobody knows", "y", size=17)

sg_analogy = Doodle(760, 250, "Doodle of a sailing race leg. The goal is to round the next buoy. The crew decides every tack and sail change against that, without asking the skipper. A list of manoeuvres without the buoy would be useless when the wind changes.",
                     "A sailing leg: “round the next buoy”. The crew picks every tack against it, without asking.")
sg_analogy.icon("ship", 40, 70, 1.3)
sg_analogy.circle(620, 100, 30, fill="y", label="buoy")
sg_analogy.arrow(200, 120, 560, 100, dash=True, curve=(380, 30))
sg_analogy.note(380, 200, "the goal stays; the tacks change with the wind", "pen")

sg_how = Doodle(760, 340, "Sprint 7's goal, 16 to 27 March 2026: a Noord picker can send a swap and see the customer's answer at packing. Items on the board are tagged as serving the goal or not. Midway, a picker-history screen was dropped to fix the packing view, a trade the team made without asking Grace, because the goal said what mattered. The goal was met; R1 went to the Noord staff test on 30 March.",
                "One sentence of value. The team trades items against it on its own; the sprint review checks the sentence.")
sg_how.box(14, 14, 732, 80, None, "green")
sg_how.text(380, 46, "Sprint 7 goal: a Noord picker can send a swap", "t-head", size=17)
sg_how.text(380, 76, "and see the customer's answer at packing.", "t-head", size=17)
for i, (t, f) in enumerate([("swap screen ✓", "blue"), ("answer at packing ✓", "blue"), ("customer card ✓", "blue")]):
    sg_how.box(14 + i * 248, 116, 236, 56, t, f, size=14, rx=4)
sg_how.box(14, 190, 360, 60, "picker history ✗ (dropped)", "paper", dash=True, size=14, rx=4)
sg_how.box(386, 190, 360, 60, "packing view fix (added)", "y", size=14, rx=4)
sg_how.note(380, 288, "a trade the team made without asking", "green", size=17)
sg_how.note(380, 320, "goal met → R1 at Noord, 30 Mar", "pen", size=17)

SPRINT_GOALS = dict(
    slug="sprint-goals",
    kicker="a.k.a. “round the next buoy”",
    tldr="A sprint without a goal is a to-do list, and every interruption looks equally important. A <b>sprint goal</b> is <b>one sentence of value</b> the sprint should deliver, written with the team. It lets the team make <b>trade-offs on its own</b> (drop this, add that) as long as the goal is met; it gives interruptions a test (does this matter more than the goal?); and the review checks <b>the sentence</b>, not the ticket count.",
    chips=[("Family", "working with the team"), ("Origin", "<i>The Scrum Guide</i> (sprint goal; made a commitment in the 2020 edition)"), ("Lives in", "the top of the sprint board"), ("Pairs with", "thin slices, definition of done, story mapping")],
    problem_side="Larder, 16 March 2026",
    problem="""  <p class="lead">Sprint 6 was <b>fourteen tickets</b>. Halfway through, Sam asked for an urgent change to the support view; it took <b>three days</b>. Was that right? Nobody could say, because the sprint had <b>no goal</b>, only a list. At the review the team showed eleven finished tickets, and Grace couldn't tell whether the sprint had moved approvals any closer to Noord. <span class="hl-pink">The sprint was a list, not a purpose.</span></p>
  <ul>
    <li>Without a goal, every interruption looks as important as the plan.</li>
    <li>The team can't trade items without asking the PO.</li>
    <li>Reviews count tickets, not value.</li>
  </ul>""",
    problem_figs=[sg_problem],
    analogy_side="the sailing leg",
    analogy="""  <p>On a sailing race, each leg has one goal: <b>round the next buoy</b>. The crew decides every tack and sail change against that, without asking the skipper each time. A list of planned manoeuvres would be useless the moment the wind shifts; the buoy stays where it is.</p>""",
    analogy_figs=[sg_analogy],
    map=[("The next buoy", "The sprint goal: one sentence of value"),
         ("Tacks and sail changes", "The tickets, which can change"),
         ("The crew deciding", "The team trading items without asking"),
         ("A wind shift", "Sam's urgent request: does it beat the goal?"),
         ("Rounding the buoy", "The review: was the sentence achieved?")],
    how_side="one sentence, trades against it",
    how="""  <p>Sprint 7's goal was one sentence: <b>a Noord picker can send a swap and see the customer's answer at packing</b>. Midway, the packing view needed more work than planned; the team <b>dropped a picker-history screen</b> to fix it, without asking Grace, because the goal said what mattered. When Sam asked for another urgent change, the question was simple: does it beat the goal? It waited a week. R1 reached the Noord staff test on 30 March.</p>""",
    how_figs=[sg_how],
    steps=[("Start planning with the goal", "From the slice: what should be possible at the end of the sprint?"),
           ("One sentence, from a user's view", "“A Noord picker can…”, not “finish tickets 41–55”."),
           ("Pick items that serve it", "Mark the ones that do; some others are fine, but fewer."),
           ("Let the team trade", "Drop or add items as long as the goal is met."),
           ("Test interruptions against it", "“Does this matter more than the goal?” If not, it waits."),
           ("Review the sentence", "Demo the goal working; count tickets only if you must.")],
    vocab=[("Sprint goal", "One sentence of value the sprint should achieve."),
           ("Sprint backlog", "The items chosen to reach the goal, which can change."),
           ("Commitment", "The team commits to the goal, not to every ticket."),
           ("Interruption", "Unplanned work during the sprint."),
           ("Sprint review", "Showing what was achieved and adapting the plan."),
           ("Focus", "Working on one thing that matters most.")],
    code=dict(file="team/ordering/sprints/07.md", note="sprint 7, 16–27 March 2026", plain=True, src="""
# Sprint 7 · 16–27 Mar 2026

GOAL   A Noord picker can send a swap and see the customer's answer at packing.

Serves the goal                     Status
  S-02 picker picks a substitute    done
  S-03 customer decides             done
  S-05 answer applied at packing    done (needed 2 extra days)
  S-07 customer sees the swap       done
Other
  S-11 picker history screen        DROPPED to fix S-05 (team decision, Thu)
  R-44 support view tweak (Sam)     moved to sprint 8: didn't beat the goal

Review   Goal met: demo on a Noord handheld with Tomás. R1 staff test on 30 Mar.
"""),
    tools="tools: the top line of the sprint board; any tracker lets you pin it. The Scrum Guide's short section on the sprint goal is enough reading.",
    gains=["<b>The team trades on its own</b>, as long as the goal holds.",
           "<b>Interruptions get a test</b>: do they beat the goal?",
           "<b>Reviews show value</b>, not ticket counts.",
           "<b>Focus</b>: most items serve one purpose.",
           "<b>Easier to say no</b> mid-sprint."],
    losses=["<b>Writing a good goal</b> takes practice.",
            "<b>Mixed sprints</b> (bugs, chores) fit awkwardly.",
            "<b>Missed goals feel worse</b> than missed tickets.",
            "<b>Can be ignored</b> after planning if not on the board."],
    baseline="Each line compares <b>sprints as lists of tickets with no stated purpose</b> to <b>a one-sentence sprint goal the team trades against and the review checks</b>.",
    ratings=[(2, 4, "Each sprint delivers something a picker or customer can use."),
             (3, 4, "The goal ties to the slice and its outcome."),
             (3, 3, "Neutral."),
             (2, 4, "A working increment to show every two weeks."),
             (1, 5, "One sentence decides what matters."),
             (2, 5, "Everyone can say what the sprint is for."),
             (2, 4, "Stakeholders see value at reviews."),
             (2, 4, "Interruptions are tested, not absorbed."),
             (3, 4, "One sentence at planning.")],
    pitfalls=[("A list in disguise", "“Goal: finish S-02, S-03, S-05.”", "say what becomes possible, from a user's view."),
              ("Two goals", "“Approvals and the Rotterdam config.”", "one goal; other work can still happen."),
              ("Forgotten after planning", "The goal lives in the planning notes.", "pin it on top of the board."),
              ("PO decides every trade", "The team still asks Grace about each item.", "let the team trade, as long as the goal is met.")],
    use=["Every sprint, in teams that work in sprints.",
         "When interruptions keep derailing plans.",
         "When reviews feel like ticket counting.",
         "Thin-slice delivery, one slice per goal."],
    skip=["Kanban teams without sprints: use a weekly focus instead.",
          "Pure support rotations."],
    related=["<b>Thin slices of value</b> (this volume)", "<b>Definition of ready &amp; done</b> (this volume)", "<b>Refinement that isn't a meeting marathon</b> (this volume)", "<b>Outcomes over outputs</b> (Vol. 1)"],
    quiz=[("What is a sprint goal?", "One sentence of value the sprint should achieve."),
          ("What does it let the team do?", "Trade items on its own, as long as the goal is met."),
          ("How do you test an interruption?", "Does it matter more than the goal? If not, it waits."),
          ("What does the review check?", "Whether the goal was achieved, shown working.")],
    try_it="At your next planning, write the sprint goal first: one sentence about what a user can do at the end. Pin it on top of the board. At the review, start with a demo of that sentence, then count anything else.",
    remember="Round the <span class=\"hl\">buoy</span>. The crew picks the <span class=\"hl\">tacks</span>.",
    sources=["Ken Schwaber and Jeff Sutherland, <i>The Scrum Guide</i> (2020), sprint goal.",
             "Roman Pichler, “Effective Sprint Goals” (romanpichler.com, 2015).",
             "Maarten Dalmijn, on sprint goals and focus (2020–).",
             "Mike Cohn, <i>Succeeding with Agile</i> (2009)."],
)

# ------------------------------------------------------------------ 10 Refinement that Isn't a Meeting Marathon
rf_problem = Doodle(760, 280, "Doodle of Thursday refinement in March 2026: two hours, nine people, six stories discussed, two ready. Half the room on laptops. Most people listened to discussions about stories they'd never work on.",
                    "Two hours, nine people, six stories discussed, two ready. Eighteen person-hours for two stories.")
for i in range(9):
    rf_problem.circle(60 + (i % 5) * 70, 70 + (i // 5) * 80, 24, fill="paper")
rf_problem.icon("clock", 420, 40, 1.1)
rf_problem.box(500, 30, 240, 80, "2 hours", "pink", sub="9 people", stroke="red")
rf_problem.box(500, 130, 240, 80, "2 stories ready", "y", sub="of 6 discussed")
rf_problem.note(380, 262, "18 person-hours for 2 stories", "red")

rf_analogy = Doodle(760, 250, "Doodle of a band preparing a concert. The whole band doesn't sit through the drummer learning a new fill. Sections rehearse separately in short sessions; then the full band runs the songs together once.",
                     "A band rehearses in sections, briefly, then runs the songs together, not everyone through every part.")
rf_analogy.icon("bell", 40, 60, 1.2)
for i, (t, s, f) in enumerate([("drums", "20 min", "blue"), ("strings", "20 min", "blue"), ("full band", "one run-through", "green")]):
    rf_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, size=17)
rf_analogy.note(450, 210, "sections first, together briefly", "pen")

rf_how = Doodle(760, 360, "Larder's refinement from 23 March 2026. Monday: Grace posts the next stories as a pre-read, with questions. Tuesday and Wednesday: 25-minute example-mapping sessions, three people per story. Thursday: 45 minutes with the whole team, only for open questions and rough sizing. Before: 18 person-hours a week, two stories ready. After: about 8 person-hours, six to eight stories ready.",
                 "Pre-read, small groups per story, one short whole-team session. Fewer hours, more stories ready.")
for i, (d, t, s, f) in enumerate([("Mon", "pre-read", "Grace posts stories + questions", "paper"), ("Tue–Wed", "3 amigos", "25 min per story", "blue"), ("Thu", "whole team", "45 min: questions, sizing", "green")]):
    x = 14 + i * 248
    rf_how.head(x + 118, 30, d, size=18)
    rf_how.box(x, 46, 236, 100, t, f, sub=s, subsize=14)
rf_how.box(14, 180, 360, 90, "before", "pink", sub="18 person-hours · 2 ready")
rf_how.box(386, 180, 360, 90, "after", "green", sub="≈ 8 person-hours · 6–8 ready")
rf_how.note(380, 316, "refine just enough, just in time", "pen", size=18)

REFINEMENT = dict(
    slug="refinement",
    kicker="a.k.a. “rehearse in sections”",
    tldr="Refinement (getting stories ready to build) often becomes a <b>two-hour meeting</b> where nine people listen to discussions about stories most of them won't touch. Break it up: a <b>pre-read</b> early in the week, <b>small-group sessions per story</b> (the three amigos, 25 minutes, example mapping), and one <b>short whole-team session</b> only for open questions and rough sizing. Refine <b>just enough, just in time</b>: about the next sprint or two.",
    chips=[("Family", "working with the team"), ("Origin", "backlog grooming in Scrum (renamed refinement, 2013); three amigos (George Dinwiddie)"), ("Lives in", "a weekly rhythm in the team calendar"), ("Pairs with", "example mapping, definition of ready, sprint goals")],
    problem_side="Larder, 23 March 2026",
    problem="""  <p class="lead">Every Thursday, the whole team of <b>nine</b> sits in refinement for <b>two hours</b>. They discuss six stories; two end up ready. Half the room is on laptops; Dee hears twenty minutes about a support table he'll never touch. That's <span class="hl-pink">eighteen person-hours a week for two stories</span>, and everyone dreads Thursdays.</p>
  <ul>
    <li>Everyone attends everything, so most people are bored most of the time.</li>
    <li>Discussion starts from zero because nobody read anything first.</li>
    <li>Deep detail gets debated by people who don't need it.</li>
  </ul>""",
    problem_figs=[rf_problem],
    analogy_side="the band rehearsal",
    analogy="""  <p>A band preparing a concert doesn't make everyone sit through the drummer learning a new fill. <b>Sections rehearse separately</b>, briefly and focused; then the <b>full band</b> runs the songs together once, fixing what only shows up when everyone plays. Everyone rehearses more, and waits less.</p>""",
    analogy_figs=[rf_analogy],
    map=[("Sheet music sent ahead", "The Monday pre-read"),
         ("Section rehearsals", "25-minute three-amigos sessions per story"),
         ("The full run-through", "A 45-minute whole-team session"),
         ("Not sitting through the drum fill", "Only the people a story needs, in its details"),
         ("Ready for the concert", "Stories ready for the next sprint")],
    how_side="pre-read, small groups, short together",
    how="""  <p>From 23 March: on <b>Monday</b> Grace posts the next stories with her open questions; on <b>Tuesday and Wednesday</b> three people per story map examples in 25 minutes; on <b>Thursday</b> the whole team meets for <b>45 minutes</b>, only for remaining questions and rough sizing. The team spends about <b>8 person-hours</b> a week instead of 18, and six to eight stories are ready instead of two.</p>""",
    how_figs=[rf_how],
    steps=[("Post a pre-read", "Monday: the next stories, their links and your open questions."),
           ("Refine in small groups", "The three amigos per story, 25 minutes, example mapping."),
           ("Meet briefly as a team", "45 minutes: remaining questions, rough sizes, dependencies."),
           ("Refine just enough", "Only the next sprint or two; later items stay rough."),
           ("Check against ready", "Use the definition of ready, not the clock."),
           ("Review the rhythm", "Ask at the retro: too much, too little, wrong people?")],
    vocab=[("Refinement", "Getting backlog items ready to build."),
           ("Three amigos", "Product, engineering and testing or design on one story."),
           ("Pre-read", "Material shared before a meeting so time isn't spent reading."),
           ("Just in time", "Refining only what's coming up soon."),
           ("Sizing", "A rough estimate of effort, for planning."),
           ("Meeting load", "Total person-hours spent in a meeting.")],
    code=dict(file="team/ordering/refinement.md", note="the refinement rhythm, from 23 March 2026", plain=True, src="""
# Refinement rhythm · ordering & apps team

Mon (async)    Grace posts the next 6–8 stories: link to story map + open questions.
               Everyone comments where they know something.
Tue–Wed        Three amigos per story, 25 min, example mapping.
               Who: Grace or Noor + one engineer who'll build it + Dee (testing).
Thu 10:00–10:45  Whole team: remaining red cards, rough sizes, dependencies.
               No new stories presented here.

Rule: refine only for the next two sprints.
Before (to 20 Mar): 2 h × 9 people = 18 person-hours → 2 stories ready.
After  (from 23 Mar): ≈ 8 person-hours → 6–8 stories ready.
"""),
    tools="tools: the backlog tool's comments for the pre-read; example-mapping templates (Miro, FigJam) or sticky notes; a shared calendar rhythm.",
    gains=["<b>Fewer person-hours</b>: 18 → about 8.",
           "<b>More stories ready</b>: two → six to eight.",
           "<b>The right people</b> on each story.",
           "<b>Better questions</b>, because people read first.",
           "<b>Less dread</b> on Thursdays."],
    losses=["<b>More scheduling</b>: several small sessions.",
            "<b>Not everyone sees everything</b>.",
            "<b>Pre-reads get skipped</b> sometimes.",
            "<b>Needs a PO who prepares</b> each Monday."],
    baseline="Each line compares <b>a two-hour whole-team refinement meeting</b> to <b>a pre-read, small three-amigos sessions per story and a 45-minute whole-team session</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Example maps make stories concrete."),
             (3, 4, "Stories are ready sooner."),
             (2, 4, "People spend time only on their stories."),
             (2, 4, "Pre-reads and maps are shared with everyone."),
             (3, 3, "Neutral."),
             (2, 4, "Six to eight ready stories keep work flowing."),
             (1, 4, "18 person-hours a week down to about 8.")],
    pitfalls=[("Everyone, everything", "Nine people on every story.", "small groups per story; whole team briefly."),
              ("No pre-read", "The meeting starts by reading the stories aloud.", "post them Monday, with questions."),
              ("Refining months ahead", "Detail for stories that will change.", "only the next sprint or two."),
              ("Presenting in Thursday's session", "New stories shown for the first time.", "Thursday is for questions and sizing only.")],
    use=["Teams whose refinement meetings run long.",
         "When most attendees have nothing to say about most stories.",
         "Alongside example mapping.",
         "Teams of six or more."],
    skip=["Teams of three or four: one short session is fine.",
          "Kanban teams pulling just in time: refine at the top of the queue."],
    related=["<b>Example mapping</b> (this volume)", "<b>Definition of ready &amp; done</b> (this volume)", "<b>The product trio</b> (this volume)", "<b>Sprint goals</b> (this volume)"],
    quiz=[("What are the three parts of Larder's rhythm?", "A Monday pre-read, three-amigos sessions per story, a 45-minute whole-team session."),
          ("What's the whole-team session for?", "Remaining questions, rough sizing and dependencies, not presenting stories."),
          ("How far ahead should you refine?", "Just the next sprint or two."),
          ("What changed in numbers?", "From 18 person-hours for 2 ready stories to about 8 for 6–8.")],
    try_it="Count your refinement's person-hours last week and how many stories ended up ready. Next week, post a pre-read on Monday, run 25-minute sessions with three people per story, and cut the team meeting to 45 minutes. Compare the two numbers.",
    remember="Rehearse in <span class=\"hl\">sections</span>. Play <span class=\"hl\">together</span> briefly.",
    sources=["Ken Schwaber and Jeff Sutherland, <i>The Scrum Guide</i> (2020), on refinement.",
             "George Dinwiddie, “The Three Amigos” (Better Software, 2011).",
             "Roman Pichler, “Refining the Product Backlog” (romanpichler.com).",
             "Matt Wynne, “Introducing Example Mapping” (2015)."],
)

# ------------------------------------------------------------------ 11 Talking Tech Debt with Engineers
td_problem = Doodle(760, 280, "Doodle of a planning conversation on 8 June 2026. Ben asks for twenty percent of each sprint for technical debt and explains sync conflict resolution and idempotency keys. Grace hears a hobby that competes with approvals in Rotterdam, and says: after the launch. Ben hears: never.",
                    "Ben talks idempotency; Grace hears a hobby. She says “after the launch”; he hears “never”.")
td_problem.box(20, 30, 330, 100, "Ben", "blue", sub="“sync conflicts, idempotency…”")
td_problem.box(410, 30, 330, 100, "Grace", "y", sub="“after the launch”")
td_problem.note(185, 170, "Grace hears: a hobby", "red", size=19)
td_problem.note(575, 170, "Ben hears: never", "red", size=19)
td_problem.note(380, 250, "same table, two languages", "pen")

td_analogy = Doodle(760, 250, "Doodle of a restaurant owner and the head chef. The chef says the walk-in fridge needs servicing: the owner hears a cost. The chef says if the fridge fails on a Saturday we bin 3,000 euros of fish and close: the owner says book it this week.",
                     "“The fridge needs servicing” sounds like a cost. “If it fails on Saturday we bin €3,000 of fish” gets booked.")
td_analogy.icon("fridge", 40, 50, 1.6)
td_analogy.box(160, 40, 280, 90, "“needs servicing”", "paper", sub="owner hears: a cost")
td_analogy.box(470, 40, 270, 90, "“€3,000 of fish”", "green", sub="owner: book it now")
td_analogy.note(450, 200, "same fridge, different sentence", "pen")

td_how = Doodle(760, 360, "How Grace and Ben translated the debt, 8 June 2026. Picker sync conflicts fixed by hand, twelve a week at Noord, cause wrong swaps packed and refund tickets: the outcome Grace owns. Rotterdam's three hard-coded settings make Utrecht slower to launch. The Dispatch loop keeps Rotterdam's on-time rate at 84 percent. Agreed: twenty percent of every sprint, ordered by product impact, each item reported at the sprint review with a product number.",
                 "Translate each debt into the outcomes the PO owns. Then 20 % stops being a hobby and becomes a bet.")
for i, (debt, effect, f) in enumerate([("picker sync conflicts (12/wk)", "wrong swaps → refund tickets", "pink"),
                                      ("3 hard-coded RTM settings", "Utrecht launch slower", "y"),
                                      ("Dispatch 30-s loop", "RTM on time stuck at 84 %", "y")]):
    y = 16 + i * 74
    td_how.box(14, y, 330, 60, debt, "blue", size=14, rx=6)
    td_how.arrow(348, y + 30, 404, y + 30)
    td_how.box(408, y, 338, 60, effect, f, size=14, rx=6)
td_how.box(14, 250, 732, 70, None, "green")
td_how.text(380, 280, "20 % of every sprint · ordered by product impact", "t-head", size=16)
td_how.text(380, 306, "reported at the review with a product number", size=15)

DEBT_TALKS = dict(
    slug="tech-debt-talks",
    kicker="a.k.a. “€3,000 of fish”",
    tldr="Engineers talk about technical debt in technical terms; product owners hear a hobby competing with features. Fix the <b>language</b>, not the relationship. Ask engineers to <b>translate each debt item into an effect you own</b> (refund tickets, launch dates, on-time rate, team speed), agree a <b>fixed share of capacity</b>, order debt by <b>product impact</b>, and report each paid item with a <b>product number</b>. Then debt work is a bet you both understand.",
    chips=[("Family", "working with the team"), ("Origin", "Ward Cunningham's debt metaphor (1992); product practice on capacity allocation"), ("Lives in", "the planning conversation and the debt register"), ("Pairs with", "technical debt register, cost of delay, sprint goals")],
    problem_side="Larder, 8 June 2026",
    problem="""  <p class="lead">At Q3 planning Ben asks for <b>20 % of every sprint</b> for technical debt. He explains sync conflict resolution and idempotency keys. Grace hears something interesting that competes with approvals in Rotterdam, and says <b>“after the launch”</b>. Ben hears <span class="hl-pink">“never”</span>, again. Neither is wrong; they're speaking two languages at the same table.</p>
  <ul>
    <li>Debt described in technical terms sounds optional to product.</li>
    <li>“After the launch” repeated becomes “never”, and trust erodes.</li>
    <li>Debt work, when it happens, isn't connected to anything product can see.</li>
  </ul>""",
    problem_figs=[td_problem],
    meanwhile=[("architect-2", "tech-debt-register", "Grace and Ben's 20 % deal, agreed a week earlier, is the budget this register spends.", "A week earlier Grace and Ben agreed 20 % of each sprint for debt, after translating it into refund tickets and launch dates.")],
    analogy_side="the chef and the fridge",
    analogy="""  <p>A head chef tells the owner: <b>“the walk-in fridge needs servicing”</b>. The owner hears a cost and says next month. The chef tries again: <b>“if it fails on a Saturday we bin €3,000 of fish and close the kitchen”</b>. The owner says: book it this week. Same fridge; a sentence in the owner's terms.</p>""",
    analogy_figs=[td_analogy],
    map=[("“The fridge needs servicing”", "“Sync conflict resolution”"),
         ("“€3,000 of fish on a Saturday”", "“12 wrong swaps a week at Noord → refund tickets”"),
         ("The owner's terms", "Refund tickets, launch dates, on-time rate"),
         ("Booking it this week", "20 % of every sprint, agreed"),
         ("The service report", "A product number at each review")],
    how_side="translate, agree a share, report",
    how="""  <p>Grace asked Ben to try again, in her terms. <b>Picker sync conflicts</b> (12 a week at Noord) meant wrong swaps packed, which meant <b>refund tickets</b>, her outcome. Rotterdam's <b>three hard-coded settings</b> meant Utrecht would launch slower. The <b>Dispatch loop</b> kept Rotterdam at 84 % on time. They agreed <b>20 % of every sprint</b>, ordered by product impact, with each paid item reported at the review with a number. A week later Ana's debt register adopted the same 20 %.</p>""",
    how_figs=[td_how],
    steps=[("Ask for the translation", "“What does this cost customers, launches or the team, per month?”"),
           ("Map debt to outcomes you own", "Refund tickets, on-time, launch dates, team speed."),
           ("Agree a fixed share", "A percentage of every sprint (20 % here), not a fight per item."),
           ("Order by product impact", "Within the share, the item with the biggest product effect goes first."),
           ("Report with a product number", "“Sync conflicts: 12 → 1 a week; swap refunds from wrong packing: −40 %.”"),
           ("Revisit the share quarterly", "Up after a big launch; down when the register is healthy.")],
    vocab=[("Technical debt", "Shortcuts that make change slower or riskier later."),
           ("Capacity allocation", "A fixed share of team time for a kind of work."),
           ("Product impact", "The effect on outcomes the PO owns."),
           ("Interest", "What debt costs every month (see Ana's register)."),
           ("Translation", "Saying a technical issue in the listener's terms."),
           ("Trust", "Believing “later” means later, not never.")],
    code=dict(file="team/ordering/debt-agreement.md", note="Grace and Ben's agreement, 8 June 2026", plain=True, src="""
# Debt agreement · ordering & apps                    Grace + Ben · reviewed quarterly

Share       20 % of every sprint (≈ 2 days per engineer per sprint)
Order       by product impact, from Ana's debt register (from 15 Jun)

Translated  debt                               → what it costs us
            Picker sync conflicts (12/wk Noord) → wrong swaps packed → refund tickets
            3 hard-coded Rotterdam settings     → Utrecht launch slower (TD-1)
            Dispatch 30-s assignment loop       → Rotterdam on time stuck at 84 %
            (Dispatch is Eli's team; we support)

Report      each paid item at the sprint review, with a product number
            e.g. "sync conflicts 12 → 1 a week; refund tickets from wrong packing −40 %"
"""),
    tools="tools: Ana's technical debt register for the list; the sprint board for the 20 % (a label or swimlane); the review for the product numbers.",
    gains=["<b>Debt gets paid</b>, steadily.",
           "<b>Shared language</b> between product and engineering.",
           "<b>Trust</b>: “later” has a schedule.",
           "<b>Better order</b>: product impact decides.",
           "<b>Visible results</b> in product numbers."],
    losses=["<b>20 % less feature work</b>, visibly.",
            "<b>Translation is hard</b> for some debt.",
            "<b>Some debt has no product number</b> yet.",
            "<b>The share needs defending</b> in busy quarters."],
    baseline="Each line compares <b>debt requests in technical terms, answered with “after the launch”</b> to <b>debt translated into product effects, a fixed 20 % share, and product numbers at each review</b>.",
    ratings=[(3, 4, "Fewer wrong swaps from sync conflicts."),
             (2, 4, "Debt tied to refund tickets and launch dates."),
             (2, 4, "Each item has a measured effect."),
             (3, 3, "Neutral."),
             (3, 4, "A fixed share, not a fight per item."),
             (1, 5, "Product and engineering share one language."),
             (2, 4, "Reviews show what debt work bought."),
             (2, 4, "Fewer slowdowns from old shortcuts."),
             (3, 3, "One conversation, then a label on the board.")],
    pitfalls=[("Technical pitch", "“We need to refactor the sync layer.”", "say what it costs customers or launches."),
              ("Negotiating every item", "A fight in every planning.", "agree a share; order within it."),
              ("“After the launch”, again", "Later becomes never.", "a fixed share from now, reviewed quarterly."),
              ("No result shown", "Debt work disappears into the sprint.", "report each item with a product number.")],
    use=["Every product team with a codebase older than a year.",
         "When “tech debt” keeps losing planning debates.",
         "After a launch that took shortcuts.",
         "When engineers start to distrust “later”."],
    skip=["Brand-new products with almost no debt (yet).",
          "Incidents: fix first, then translate."],
    related=["<b>Technical debt register</b> (Ana, book 1 vol. 2)", "<b>Cost of delay</b> (Vol. 2)", "<b>Sprint goals</b> (this volume)", "<b>Explaining trade-offs to non-engineers</b> (Ana, book 1 vol. 3)"],
    quiz=[("What does Grace ask Ben for?", "A translation of each debt item into effects she owns: refunds, launch dates, on-time rate."),
          ("Why a fixed share instead of per-item decisions?", "It stops the fight in every planning and makes “later” a schedule."),
          ("What share did they agree?", "20 % of every sprint, ordered by product impact."),
          ("How is the result shown?", "Each paid item at the review, with a product number.")],
    try_it="Ask your tech lead for the three debt items that bother them most. For each, write together what it costs customers, launches or the team, with a number if you can. Propose a fixed share of capacity and one product number you'll report at the next review.",
    remember="Not “the fridge needs servicing”: <span class=\"hl\">€3,000 of fish</span>. Then book a <span class=\"hl\">fixed share</span>.",
    sources=["Ward Cunningham, “The WyCash Portfolio Management System” (OOPSLA, 1992).",
             "Philippe Kruchten, Robert Nord, Ipek Ozkaya, <i>Managing Technical Debt</i> (2019).",
             "Marty Cagan, “Tech Debt” (SVPG), on the 20 % rule of thumb.",
             "Adam Tornhill, <i>Software Design X-Rays</i> (2018)."],
)

NOTES = [TRIO, SPRINT_GOALS, REFINEMENT, DEBT_TALKS]
