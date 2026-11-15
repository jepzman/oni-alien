# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 1 · Ways of working.
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 1").
# Spine: PMBOK Guide, Eighth Edition. Names are PMI's; every explanation is in our own words.

# ------------------------------------------------------------------ 11 Plan It All, or Learn As We Go?
lc_problem = Doodle(760, 250, "Doodle of 9 February 2026. Two people want two opposite plans. The builder wants every detail fixed before work starts: drawings, permits, a contract. Ben wants to plan two weeks at a time and show something working every fortnight. Sanne has to run both inside one launch.",
                    "The builder needs everything fixed first. Ben wants to learn every two weeks. One launch.")
lc_problem.box(20, 40, 300, 110, "the builder", "y", sub="“fix it all, then build”", size=20, subsize=16)
lc_problem.box(440, 40, 300, 110, "Ben", "blue", sub="“two weeks at a time”", size=20, subsize=16)
lc_problem.circle(380, 95, 34, "paper", label="?")
lc_problem.note(380, 200, "both are right, for their own work", "pen", size=20)

lc_analogy = Doodle(760, 250, "Doodle of two ways to travel. A package tour: every flight and hotel booked months ahead, cheap and certain, hard to change. A road trip: the direction is known, each day is decided on the way. Most real holidays mix them: flights booked, the days in between left open.",
                    "A package tour, a road trip, and what most people do: book the flights, leave the days open.")
lc_analogy.row([("package tour", "all booked ahead", "y"), ("road trip", "decided on the way", "blue"), ("flights + open days", "a mix", "green")], y=40, h=96, size=18, subsize=14)
lc_analogy.note(132, 186, "predictive", "red", size=20)
lc_analogy.note(380, 186, "adaptive", "red", size=20)
lc_analogy.note(628, 186, "hybrid", "red", size=20)

lc_how = Doodle(760, 400, "Rotterdam's approach per workstream, 9 February 2026. Store fit-out: predictive, a contract with the builder and a fixed sequence. People: predictive, with hiring and training dates. Stock: predictive. Platform set-up and apps: adaptive, two-week sprints with a demo. Launch marketing: adaptive. Five shared milestones tie them together: fit-out complete 3 April, stock on shelves 17 April, app ready 20 April, go or no-go 24 April, opening 27 April.",
                "Predictive where change is expensive, adaptive where learning is cheap, tied together by five shared milestones.")
rows = [("store fit-out", "predictive", "y"), ("people", "predictive", "y"), ("stock + suppliers", "predictive", "y"),
        ("platform + apps", "adaptive", "blue"), ("marketing", "adaptive", "blue")]
for i, (t, a, f) in enumerate(rows):
    y = 14 + i * 50
    lc_how.text(14, y + 26, t, anchor="start", size=16)
    if a == "predictive":
        lc_how.box(190, y, 450, 38, a, f, size=15)
    else:
        for k in range(5):
            lc_how.box(190 + k * 90, y, 82, 38, None, f)
        lc_how.text(680, y + 26, a, size=15)
for i, (d, t) in enumerate([("3 Apr", "fit-out done"), ("17 Apr", "stock in"), ("20 Apr", "app ready"), ("24 Apr", "go / no-go"), ("27 Apr", "open")]):
    lc_how.box(14 + i * 148, 320, 138, 60, d, "pink", sub=t, size=16, subsize=13)
lc_how.note(380, 300, "five shared milestones, the same for every workstream", "red", size=17)

lc_deep1 = Doodle(760, 300, "A scoring table Sanne uses to choose an approach for each workstream. Five questions, each answered left or right. How clear is what we need: clear, or still unclear. How expensive is it to change later: expensive, or cheap. Can we deliver in small pieces: no, or yes. How often can the customer look: rarely, or often. How strict are the rules: strict, or light. Answers on the left point to predictive, answers on the right to adaptive.",
                  "Five questions. Answers on the left point to predictive, on the right to adaptive.")
qs = [("what we need", "clear", "still unclear"), ("changing later", "expensive", "cheap"), ("small pieces?", "no", "yes"),
      ("feedback", "rare", "often"), ("rules, contracts", "strict", "light")]
lc_deep1.head(250, 30, "→ predictive", size=18)
lc_deep1.head(630, 30, "→ adaptive", size=18)
for i, (q, l, r) in enumerate(qs):
    y = 46 + i * 48
    lc_deep1.text(14, y + 26, q, anchor="start", size=16)
    lc_deep1.box(160, y, 180, 38, l, "y", size=15)
    lc_deep1.box(540, y, 180, 38, r, "blue", size=15)
    lc_deep1.line(f"M344 {y + 19} h192", thin=True, dash=True)

lc_deep2 = Doodle(760, 250, "The same five questions scored for two Rotterdam workstreams. Store fit-out: clear needs, expensive to change, can't be delivered in pieces, feedback is rare, rules are strict: five answers on the left, so predictive. Apps: needs still unclear, cheap to change, small pieces possible, feedback every fortnight, light rules: five answers on the right, so adaptive.",
                  "The fit-out scores five on the left. The apps score five on the right. Neither is a matter of taste.")
lc_deep2.box(14, 30, 350, 150, None, "y")
lc_deep2.head(189, 58, "store fit-out", size=19)
lc_deep2.text(189, 92, "drawings fixed · cold room can't move", size=14)
lc_deep2.text(189, 116, "one handover · permits · contract", size=14)
lc_deep2.note(189, 156, "5 left → predictive", "red", size=18)
lc_deep2.box(396, 30, 350, 150, None, "blue")
lc_deep2.head(571, 58, "apps", size=19)
lc_deep2.text(571, 92, "details still open · cheap to change", size=14)
lc_deep2.text(571, 116, "ships in pieces · demo every 2 weeks", size=14)
lc_deep2.note(571, 156, "5 right → adaptive", "red", size=18)
lc_deep2.note(380, 224, "most workstreams land in between: that is where hybrid lives", "pen", size=17)

LIFE_CYCLES = dict(
    slug="life-cycles",
    kicker="a.k.a. “development approach and life cycle: predictive, adaptive, hybrid”",
    tldr="There are two basic ways to run work. <b>Predictive</b>: plan it all, then do it; best when you know what you want and change is expensive. <b>Adaptive</b> (agile): do a little, look, adjust; best when you'll learn as you go and change is cheap. Most projects are <b>hybrid</b>: each part uses the way that fits it. The choice is not about fashion. It follows from <b>how certain the work is and what a change costs</b>.",
    chips=[("Family", "ways of working"), ("Lives in", "one table per project, redone when the work changes"), ("Pairs with", "tailoring, the focus areas, the now / next / later roadmap")],
    pmbok=dict(covers="development approaches (predictive, adaptive, hybrid); the project life cycle and phases; delivery cadence",
               principles=["Adopt a holistic view"], focus=["initiating", "planning"],
               older="6th: “project life cycles” in chapter 1, plus the separate <i>Agile Practice Guide</i>. 7th: the Development Approach and Life Cycle domain."),
    problem_side="Larder, 9 February 2026",
    problem="""  <p class="lead">Two conversations on one Monday. The <b>builder</b> won't start the Rotterdam fit-out until the drawings, the permit and the price are fixed: every later change costs money and days. <b>Ben</b> won't promise a list of app features for April: his team works in two-week sprints and shows what works at the end of each. Sanne's old job was all builder. Larder's habit is all Ben. <span class="hl-pink">The launch needs both, and one plan.</span></p>
  <ul>
    <li>One method for everything fits half the work badly.</li>
    <li>A fixed plan for uncertain work is fiction, like the 2025 Gantt chart.</li>
    <li>“We're agile” doesn't order a cold room on time.</li>
  </ul>""",
    problem_figs=[lc_problem],
    meanwhile=[("product-2", "now-next-later", "on 6 February Grace replaces the 2025 Gantt chart (14 features, 9 late) with a now / next / later roadmap.",
                "three days later Sanne keeps a fixed plan only where change is expensive: the store. The apps stay adaptive.")],
    analogy_side="a package tour or a road trip",
    analogy="""  <p>A <b>package tour</b> is booked months ahead: cheap, certain, and hard to change. A <b>road trip</b> has a direction; each day is decided on the way. Most holidays are a mix: <b>book the flights</b>, because they sell out and changes are expensive, and <b>leave the days open</b>, because you'll know more when you're there.</p>""",
    analogy_figs=[lc_analogy],
    map=[("Booking flights months ahead", "The fit-out contract; ordering the cold room"),
         ("Deciding each day on the way", "Two-week sprints for the apps"),
         ("Flights + open days", "Rotterdam: a hybrid"),
         ("The flight home", "27 April: fixed for everyone"),
         ("Meeting points on the route", "Five shared milestones")],
    how_side="choose per workstream, tie together with milestones",
    how="""  <p>Sanne stops asking “are we agile or waterfall?” and asks it <b>per workstream</b>. The <b>store fit-out</b>, <b>people</b> and <b>stock</b> are predictive: a known sequence, long lead times, contracts. The <b>platform set-up and apps</b> and <b>marketing</b> are adaptive: two-week sprints, a demo, the list re-ordered each time. Five <b>shared milestones</b> tie them together, so the adaptive teams know which dates are not theirs to move: fit-out complete 3 April, stock on shelves 17 April, app ready 20 April, go / no-go 24 April, opening 27 April.</p>""",
    how_figs=[lc_how],
    steps=[("Split the project into workstreams", "Use your whole-project map."),
           ("Ask how certain each one is", "Do we know what we need?"),
           ("Ask what a change costs", "Days and money."),
           ("Choose predictive, adaptive or a mix for each", "Say why."),
           ("Set shared milestones", "The few dates all workstreams meet."),
           ("Review the choice when the work changes", "It isn't forever.")],
    vocab=[("Predictive (waterfall)", "Plan the whole, then carry it out; change is controlled."),
           ("Adaptive (agile)", "Work in short cycles, learn from each, adjust the plan."),
           ("Hybrid", "Predictive for some parts, adaptive for others."),
           ("Iterative", "Repeating the work to improve it."),
           ("Incremental", "Delivering in pieces that each add something usable."),
           ("Life cycle", "The phases a project passes through from start to end."),
           ("Milestone", "A point in time that marks something important finished.")],
    code=dict(file="rotterdam/approach.md", note="Sanne with the leads, 9 February 2026", plain=True, src="""
# Rotterdam · how each workstream is run

WORKSTREAM          APPROACH     WHY                                    RHYTHM
Store fit-out       predictive   contract, permits, 8-week cold room    weekly site check
People              predictive   notice periods, training on site       hiring + training dates
Stock + suppliers   predictive   delivery slots booked ahead            weekly
Platform set-up     adaptive     details emerge; cheap to change        2-week sprints, demo
Apps                adaptive     details emerge; cheap to change        2-week sprints, demo
Payments + legal    predictive   contracts and rules                    checklist
Launch marketing    adaptive     test messages on the waitlist          weekly

SHARED MILESTONES (not movable by one workstream)
  3 Apr   fit-out complete, store handed over
  17 Apr  stock on shelves
  20 Apr  app ready for Rotterdam
  24 Apr  go / no-go
  27 Apr  opening
"""),
    tools="tools: the whole-project map, five questions per workstream (see the deep dive), and a milestone list.",
    deep_dive=dict(
        side="choosing an approach, and making a hybrid hold together",
        intro="The note says “choose per workstream”. This deep dive shows how to choose without arguing about taste, what a hybrid needs in order not to fall apart, and the four classic life cycles you will meet in other books and exam questions.",
        parts=[
            ("Five questions that choose for you", """  <p>For each workstream, answer five questions. <b>How clear is what we need?</b> <b>How expensive is a change later?</b> <b>Can it be delivered in small pieces?</b> <b>How often can the customer look and react?</b> <b>How strict are the rules and contracts?</b></p>
  <p>Answers on the left (clear, expensive, no, rarely, strict) point to <b>predictive</b>. Answers on the right point to <b>adaptive</b>. A split result is a hybrid inside the workstream: plan the fixed parts, iterate the rest.</p>""", [lc_deep1]),
            ("Two workstreams, scored", """  <p>The <b>fit-out</b>: the drawings are agreed; moving a cold room after it is built costs weeks; a store can't open half-fitted; the “customer” sees it once, at handover; permits and a contract apply. Five on the left.</p>
  <p>The <b>apps</b>: nobody yet knows exactly how Saturday slots should behave in Rotterdam; a screen costs hours to change; each sprint can ship something; Joost and Tomás can react every fortnight; the rules are light. Five on the right. Sanne didn't have to persuade the builder to be agile or Ben to draw a Gantt chart.</p>""", [lc_deep2]),
            ("What a hybrid needs to hold together", """  <p>A hybrid fails at the joins. Three things hold it together:</p>
  <ul>
    <li><b>Shared milestones.</b> A few dates where workstreams meet. Adaptive teams choose what is in each sprint, but “app ready on 20 April” is fixed, so they manage scope to hit it.</li>
    <li><b>One status, two measures.</b> Predictive work reports against its plan (is the fit-out on its dates?). Adaptive work reports what is working (which must-haves are demonstrated?). Sanne's weekly page shows both, side by side.</li>
    <li><b>A rule for change at the boundary.</b> A change inside a sprint is the team's business. A change that moves a shared milestone goes to Sanne, and over three days to Joost.</li>
  </ul>""", []),
            ("The four life cycles, in one paragraph each", """  <ul>
    <li><b>Predictive:</b> one pass through requirements, design, build, test, deliver. One delivery at the end.</li>
    <li><b>Iterative:</b> the same thing built several times, better each time, from rough to finished. One delivery, well tested. Good when the idea needs refining (a prototype).</li>
    <li><b>Incremental:</b> the thing delivered in pieces, each usable. Several deliveries. Good when early pieces bring early value.</li>
    <li><b>Adaptive (agile):</b> iterative and incremental together, in short fixed cycles, with the customer looking at every one.</li>
  </ul>
  <p>A <b>phase</b> is a stretch of the project that ends with something agreed (design approved, store handed over). Any of the four can be used inside a phase. Vol. 2 covers the gates between phases.</p>""", []),
        ]),
    dial=[("Light", "one team, one kind of work", ["Pick one approach.", "Say why in a sentence.", "Move on."]),
          ("Standard", "Rotterdam: seven workstreams", ["An approach per workstream.", "Five shared milestones.", "One status with two measures."]),
          ("Heavy", "many teams and vendors", ["A written delivery model.", "Phase gates.", "Contracts that match each approach."])],
    baseline="Each line compares <b>one method for the whole launch</b> to <b>an approach chosen per workstream, tied together with shared milestones</b>.",
    ratings=[(3, 4, "Learning where it's cheap brings value earlier."),
             (2, 4, "Fixed where it must be; honest where it can't be."),
             (2, 4, "Long lead times are planned, not discovered."),
             (3, 4, "Each workstream reports in a way that means something."),
             (3, 4, "The builder and Ben both recognise their plan."),
             (3, 4, "Teams keep the way of working that fits them."),
             (2, 4, "Change is easy where it should be."),
             (3, 3, "Neutral."),
             (3, 3, "Two rhythms to keep in step.")],
    pitfalls=[("One true method", "“We're agile”, so nobody orders the cold room.", "choose per workstream."),
              ("Hybrid as an excuse", "No plan and no demos.", "each workstream names its approach and rhythm."),
              ("No shared milestones", "Workstreams drift apart.", "a few fixed meeting points."),
              ("Choosing by taste", "The loudest person's favourite.", "the five questions.")],
    use=["At the start, before the plan.", "When teams argue about method.", "When a project mixes building things and writing software.", "When the work changes character."],
    skip=["The organisation has one approach that clearly fits all the work."],
    related=["<b>How Much Process Do We Need?</b> (this volume)", "<b>What Do I Do When?</b> (next note)", "<b>Now / next / later roadmap</b> (Grace, vol. 2)", "<b>Last responsible moment</b> (Ana, vol. 2)"],
    quiz=[("When does predictive fit?", "When needs are clear and change is expensive."),
          ("When does adaptive fit?", "When you'll learn as you go and change is cheap."),
          ("What ties a hybrid together?", "Shared milestones, one status, and a rule for changes at the boundary."),
          ("Ben's team wants to move “app ready” from 20 to 23 April to finish a nicer slot picker. Who decides?", "Not the team alone: it's a shared milestone. It goes to Sanne; she looks at what it does to go / no-go on the 24th, and the nicer picker most likely waits."),
          ("Iterative or incremental: “deliver slots first, tracking second”?", "Incremental: usable pieces, one after another.")],
    try_it="List your project's workstreams. For each, answer the five questions and write P, A or a mix. Then write the three to five dates where they must meet.",
    remember="Book the <span class=\"hl\">flights</span>. Leave the <span class=\"hl\">days</span> open.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): development approaches and life cycles.",
             "Project Management Institute and Agile Alliance, <i>Agile Practice Guide</i> (2017).",
             "Ralph Stacey's certainty and agreement matrix, as used in the <i>Agile Practice Guide</i>.",
             "Barry Boehm and Richard Turner, <i>Balancing Agility and Discipline</i> (2003)."],
)

# ------------------------------------------------------------------ 12 What Do I Do When?
fa_problem = Doodle(760, 250, "Doodle of 11 February 2026. Joost looks at Sanne's week and is puzzled. On Monday she was planning. On Tuesday she closed the helpdesk-tool decision. On Wednesday she was starting something new, the courier hiring drive. He asks: I thought planning was the first phase and closing the last. Which phase are we in?",
                    "“Which phase are we in?” Planning on Monday, closing on Tuesday, starting on Wednesday.")
fa_problem.row([("Mon", "planning", "y"), ("Tue", "closing", "pink"), ("Wed", "starting", "green"), ("Thu", "checking", "blue"), ("Fri", "doing", "paper")], y=40, h=80, size=18, subsize=15)
fa_problem.note(380, 176, "“I thought planning came first and closing last?”", "red", size=19)
fa_problem.note(380, 212, "they are not phases", "pen", size=19)

fa_analogy = Doodle(760, 250, "Doodle of cooking a dinner with several dishes. For each dish the cook decides to make it, plans it, cooks it, tastes and adjusts, and plates it. The cook does not plan all the dishes for an hour and then cook for an hour: while one dish is cooking, another is being tasted and a third is being planned.",
                    "A cook decides, plans, cooks, tastes and plates, for each dish, and several dishes at once.")
fa_analogy.row([("decide", None, "y"), ("plan", None, "y"), ("cook", None, "y"), ("taste", None, "y"), ("plate", None, "y")], y=30, h=56, size=16, gap=34, arrows=True)
fa_analogy.note(380, 124, "…for the soup, while…", "pen", size=18)
fa_analogy.row([("decide", None, "blue"), ("plan", None, "blue"), ("cook", None, "blue"), ("taste", None, "blue"), ("plate", None, "blue")], x=60, y=148, h=56, size=16, gap=34, arrows=True)
fa_analogy.note(380, 236, "…the roast is two steps behind", "pen", size=18)

fa_how = Doodle(760, 380, "The five focus areas drawn as a loop for Rotterdam, 11 February 2026. Initiating: agree it should exist, why, and who is behind it. Planning: work out what, when, how much, who, and what could stop us. Executing: do the work and lead the people. Monitoring and controlling sits in the middle and watches all the others: compare with the plan and decide what to change. Closing: hand over, settle up, keep the lessons. Arrows loop from executing back to planning. The whole loop runs again for each phase and each sprint.",
                "Five kinds of attention. Monitoring and controlling watches all the others; the loop repeats for every phase.")
fa_how.box(14, 20, 170, 96, "initiating", "y", sub="should it exist?", size=18, subsize=13)
fa_how.box(214, 20, 170, 96, "planning", "blue", sub="what, when, who?", size=18, subsize=13)
fa_how.box(414, 20, 170, 96, "executing", "green", sub="do it, lead it", size=18, subsize=13)
fa_how.box(614, 20, 132, 96, "closing", "pink", sub="hand over", size=18, subsize=13)
fa_how.arrow(184, 68, 212, 68)
fa_how.arrow(384, 68, 412, 68)
fa_how.arrow(584, 68, 612, 68)
fa_how.arrow(499, 118, 299, 118, curve=(399, 168), label="re-plan", lx=399, ly=166)
fa_how.box(14, 200, 732, 80, "monitoring and controlling", "paper", sub="compare with the plan · decide what to change", size=19, subsize=14)
for x in (99, 240, 560, 680):
    fa_how.line(f"M{x} 118 V198", thin=True, dash=True)
fa_how.note(380, 326, "the loop runs once for the project, and again for each phase and sprint", "pen", size=17)
fa_how.note(380, 356, "this week: Rotterdam is planning; the helpdesk decision is closing", size=16)

fa_deep1 = Doodle(760, 356, "A grid of the seven performance domains against the five focus areas. Rows: governance, scope, schedule, finance, stakeholders, resources, risk. Columns: initiating, planning, executing, monitoring and controlling, closing. Dots show where each domain has work. Governance has work in every column. The others mostly start in planning and continue through monitoring and controlling. The forty processes of the guide are the dots in this grid.",
                  "Seven domains down, five focus areas across. The forty processes are the cells of this grid.")
cols = ["initiating", "planning", "executing", "monitoring", "closing"]
for k, c in enumerate(cols):
    fa_deep1.head(250 + k * 108, 28, c, size=15)
grid = [("governance", [1, 1, 1, 1, 1]), ("scope", [0, 1, 0, 1, 0]), ("schedule", [0, 1, 0, 1, 0]), ("finance", [0, 1, 0, 1, 0]),
        ("stakeholders", [1, 1, 1, 1, 0]), ("resources", [0, 1, 1, 1, 0]), ("risk", [0, 1, 1, 1, 0])]
for i, (d, cells) in enumerate(grid):
    y = 46 + i * 38
    fa_deep1.text(14, y + 22, d, anchor="start", size=16)
    for k, on in enumerate(cells):
        fa_deep1.box(200 + k * 108, y, 100, 30, None, "blue" if on else "paper", rx=4)
fa_deep1.note(380, 344, "an illustration of the pattern, not the official table: each volume fills in its rows", "pen", size=15)

fa_deep2 = Doodle(760, 230, "One week in February at Rotterdam, seen through the five focus areas. Initiating: the courier hiring drive gets a sponsor and a one-line reason. Planning: the Rotterdam plan is being made with the team for 20 February. Executing: the builder starts stripping the unit, Eli sets up zones. Monitoring and controlling: the weekly status compares must-haves done with the plan. Closing: the helpdesk tool decision is closed, with a lesson written down.",
                  "One week, five kinds of attention, across four pieces of work.")
fa_deep2.row([("initiating", "courier drive", "y"), ("planning", "Rotterdam plan", "blue"), ("executing", "builder, zones", "green"),
              ("monitoring", "weekly status", "paper"), ("closing", "helpdesk tool", "pink")], y=40, h=110, gap=10, size=15, subsize=14)
fa_deep2.note(380, 200, "9–13 February 2026", "pen", size=18)

FOCUS = dict(
    slug="focus-areas",
    kicker="a.k.a. “the five focus areas” (older editions: the process groups)",
    tldr="Project work needs five kinds of attention. <b>Initiating</b>: agree it should exist. <b>Planning</b>: work out how. <b>Executing</b>: do it. <b>Monitoring and controlling</b>: compare with the plan and adjust. <b>Closing</b>: hand over and learn. They are <b>not phases in a row</b>: they overlap, they repeat for every phase and sprint, and monitoring runs all the time. Use them as a checklist: <b>which kind of attention is this work missing?</b>",
    chips=[("Family", "ways of working"), ("Lives in", "your head, every Monday"), ("Pairs with", "the seven domains, life cycles, phase gates (vol. 2)")],
    pmbok=dict(covers="the five focus areas: initiating, planning, executing, monitoring and controlling, closing",
               focus=["initiating", "planning", "executing", "monitoring", "closing"],
               older="6th: the five “process groups”, same names. 7th: not used (they moved to a separate process-groups guide). Back in the 8th as focus areas."),
    problem_side="Larder, 11 February 2026",
    problem="""  <p class="lead">Joost has read a little about project management, and Sanne's week confuses him. Monday she was <b>planning</b> Rotterdam. Tuesday she <b>closed</b> the helpdesk-tool decision. Wednesday she <b>started</b> something: the courier hiring drive got a sponsor. <span class="hl-pink">“I thought planning was the first phase and closing the last. Which phase are we in?”</span></p>
  <ul>
    <li>The five words are read as five phases in a row.</li>
    <li>So “planning” is declared finished, and never revisited.</li>
    <li>And closing is left for the very end, when everyone has gone.</li>
  </ul>""",
    problem_figs=[fa_problem],
    analogy_side="cooking a dinner of several dishes",
    analogy="""  <p>A cook making dinner <b>decides</b> on a dish, <b>plans</b> it, <b>cooks</b> it, <b>tastes and adjusts</b>, and <b>plates</b> it. But not for all dishes at once, one step at a time. While the soup simmers, the roast is being tasted and the dessert is still being planned. And the cook tastes all the way through, not once at the end.</p>""",
    analogy_figs=[fa_analogy],
    map=[("Deciding to make a dish", "Initiating: the courier hiring drive gets a sponsor"),
         ("Planning the dish", "Planning: the Rotterdam plan, made with the team"),
         ("Cooking", "Executing: the builder starts; Eli sets up zones"),
         ("Tasting and adjusting, all the time", "Monitoring and controlling: the weekly status"),
         ("Plating", "Closing: the helpdesk decision, with its lesson written down")],
    how_side="five kinds of attention, in a loop",
    how="""  <p>Sanne draws it for Joost as a <b>loop</b>, not a line. Initiating, planning and executing follow each other, and executing feeds back into planning whenever something is learned. <b>Monitoring and controlling</b> sits under all of them. Closing happens every time something ends: a decision, a phase, a sprint, the project. The loop runs once for Rotterdam as a whole and again inside each phase. So the answer to “which phase are we in?” is: <b>Rotterdam is mostly planning this week, and something is always being checked</b>.</p>""",
    how_figs=[fa_how],
    steps=[("Initiating", "Agree it should exist, why, and who backs it."),
           ("Planning", "What, when, how much, who, what could stop us."),
           ("Executing", "Do the work; lead the people."),
           ("Monitoring and controlling", "Compare with the plan; decide what to change."),
           ("Closing", "Hand over, settle up, keep the lessons."),
           ("Repeat for every phase, and ask which one is missing", "Usually initiating or closing.")],
    vocab=[("Focus area", "A kind of attention project work needs. Five in the eighth edition."),
           ("Process group", "The same idea, as older editions named it."),
           ("Phase", "A stretch of the project that ends with something agreed."),
           ("Initiating", "Getting agreement to start a project or a phase."),
           ("Monitoring and controlling", "Measuring against the plan and correcting."),
           ("Closing", "Finishing properly: handover, records, lessons.")],
    code=dict(file="sanne/monday-check.md", note="the five-question check Sanne runs each Monday", plain=True, src="""
# Monday check · five kinds of attention · 9 February 2026

                      INITIATING   PLANNING    EXECUTING   MONITORING   CLOSING
Rotterdam launch      done 16 Jan  ← THIS WEEK builder on  weekly       -
                                   plan 20 Feb site        status
Zuid cold room        done         done        fitted      test run     ← due: handover
                                                                          to Tomás
New helpdesk tool     done         options     -           -            decision closed,
                                   compared                               lesson logged
Courier hiring drive  ← THIS WEEK  -           -           -            -
                      sponsor: Joost

Missing attention this week:  Zuid cold room has no closing (who signs it off?) → ask Tomás
"""),
    tools="tools: five words and a weekly look across all your projects.",
    deep_dive=dict(
        side="how the focus areas, the domains and the 40 processes fit together",
        intro="The eighth edition arranges its forty processes in a grid: seven domains down, five focus areas across. Once you can see that grid, the guide stops being a list of forty things to memorise. This deep dive draws it, walks one real week through it, and shows why “closing” deserves more attention than it gets.",
        parts=[
            ("The grid behind the guide", """  <p>Every process in the guide answers two questions: <b>which domain</b> is it about (scope, schedule, risk…), and <b>which kind of attention</b> is it (planning it, doing it, checking it…)? So each process sits in one cell of a grid.</p>
  <p>The pattern is regular, which is what makes it learnable. Almost every domain has a process for <b>planning</b> how it will be managed and one for <b>monitoring and controlling</b> it. Some add <b>executing</b> processes (leading the team, carrying out risk responses). Only <b>Governance</b> stretches across all five columns, because starting and closing a project are governance questions.</p>
  <p>Read a row and you get a domain from start to finish: that is how Vols. 2 to 5 are organised. Read a column and you get everything that needs your attention at one moment: that is how a project manager's week is organised.</p>""", [fa_deep1]),
            ("One week, read across the grid", """  <p>In the week of 9 February Sanne touches all five columns, on four different pieces of work. That is normal. What the grid adds is a check: for each piece of work, <b>is any column empty that shouldn't be?</b></p>
  <p>Her Monday check finds one. The Zuid cold room is fitted and tested, and everyone has moved on. Nobody has <b>closed</b> it: no sign-off from Tomás, no warranty papers filed, no note that the supplier delivered a week late (useful for Rotterdam's order). Ten minutes on Monday saves an argument in June.</p>""", [fa_deep2]),
            ("Why initiating and closing get skipped", """  <p>Planning, executing and monitoring feel like work, so they happen. The two ends don't.</p>
  <ul>
    <li><b>Initiating</b> is skipped when work “just starts”: no sponsor, no stated reason, no agreed finish. Rotterdam itself had run for months this way. The cost appears later, as arguments about what the project was for.</li>
    <li><b>Closing</b> is skipped because the team is already needed elsewhere. The cost: results nobody formally accepted, bills and contracts left open, and lessons that are learned again, at full price, in the next city.</li>
  </ul>
  <p>Each <b>phase</b> has both ends too. Before the fit-out started, someone had to say “yes, go” (initiating the phase). On 3 April someone has to accept the finished store (closing it). Vol. 2 turns those two moments into phase gates.</p>""", []),
        ]),
    dial=[("Light", "small work", ["Ask: who wants it? what's the plan? is it done and handed over?", "No documents.", "A lesson in one line."]),
          ("Standard", "Rotterdam", ["A Monday check across projects.", "Each phase started and closed on purpose.", "Weekly monitoring."]),
          ("Heavy", "large, regulated or contracted work", ["Formal gates with sign-off.", "A documented process for each cell that applies.", "Closure reports and audits."])],
    baseline="Each line compares <b>treating the five as phases done once, in order</b> to <b>five kinds of attention, repeated, checked every Monday</b>.",
    ratings=[(3, 4, "Initiating asks “why” before work starts."),
             (2, 4, "Plans are revisited, not declared finished."),
             (3, 4, "Monitoring runs all the way through."),
             (3, 4, "It's clear what state each piece of work is in."),
             (3, 4, "Joost understands the week."),
             (3, 3, "Neutral."),
             (2, 4, "Re-planning is expected."),
             (3, 4, "Work is accepted and closed properly."),
             (4, 4, "Ten minutes on Monday.")],
    pitfalls=[("Five phases in a row", "“We're past planning.”", "they overlap and repeat."),
              ("No initiating", "Work starts with no sponsor or reason.", "a sponsor and one line of why."),
              ("No closing", "Things drift to an end.", "close every phase: accept, file, learn."),
              ("Monitoring as a report", "Numbers collected, nothing decided.", "it ends in a decision, or it isn't controlling.")],
    use=["Explaining project work to someone new.", "A weekly look across projects.", "When something feels unfinished.", "At the start and end of every phase."],
    skip=["Don't turn it into forty forms: tailor (two notes on)."],
    related=["<b>What Must I Keep an Eye On?</b> (next note)", "<b>Plan It All, or Learn As We Go?</b> (previous note)", "<b>Phase gates and go / no-go</b> (vol. 2)", "<b>Closing a project or phase</b> (vol. 2)"],
    quiz=[("Name the five focus areas.", "Initiating, planning, executing, monitoring and controlling, closing."),
          ("Are they phases?", "No. They overlap and repeat in every phase."),
          ("Which one runs all the time?", "Monitoring and controlling."),
          ("The fit-out phase ends on 3 April. Which two focus areas apply on that day?", "Closing (the store is accepted from the builder) and initiating (the stocking phase is given the go-ahead)."),
          ("In March the plan is clearly wrong. Joost says “planning is over, just execute”. What does Sanne answer?", "Planning is a kind of attention, not a finished phase. Executing has taught us something; we re-plan, and take it to the sponsor if a trigger is hit.")],
    try_it="List the pieces of work you look after. For each, mark which of the five kinds of attention it has had. Find one with no proper start or no proper close, and fix that this week.",
    remember="Five kinds of <span class=\"hl\">attention</span>, not five <span class=\"hl\">phases</span>. Taste all the way through.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): focus areas and processes.",
             "Project Management Institute, <i>Process Groups: A Practice Guide</i> (2022).",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): the five process groups."],
)

# ------------------------------------------------------------------ 13 What Must I Keep an Eye On?
pd_problem = Doodle(760, 250, "Doodle of 13 February 2026. Sanne's notes are full of schedule: dates, lead times, milestones. Marco asks a simple question: what has Rotterdam spent so far? She doesn't know. She has been watching one thing very carefully and six things hardly at all.",
                    "Watching the dates very carefully, and the money not at all.")
pd_problem.box(20, 30, 320, 120, "schedule", "y", sub="dates · lead times · milestones", size=24, subsize=15)
for i, t in enumerate(["money?", "scope?", "people?", "risks?"]):
    pd_problem.box(420 + (i % 2) * 165, 30 + (i // 2) * 66, 150, 54, t, "paper", size=16, dash=True)
pd_problem.note(380, 200, "Marco: “what has Rotterdam spent so far?”", "red", size=19)

pd_analogy = Doodle(760, 250, "Doodle of a pilot's instrument panel. Seven dials: heading, altitude, speed, fuel, engine, weather and the other aircraft. A good pilot scans all of them in a steady pattern. Staring at one dial, however important, is how pilots get into trouble.",
                    "A pilot scans seven dials in a steady pattern. Staring at one is how trouble starts.")
for i, t in enumerate(["heading", "altitude", "speed", "fuel", "engine", "weather", "traffic"]):
    pd_analogy.circle(64 + i * 105, 90, 42, "paper")
    pd_analogy.line(f"M{64 + i * 105} 90 l{[18, -14, 20, -22, 10, -18, 16][i]} -22", color="red")
    pd_analogy.note(64 + i * 105, 164, t, size=16)
pd_analogy.note(380, 216, "scan them all, every time", "pen", size=20)

pd_how = Doodle(760, 400, "Sanne's seven-tab binder for Rotterdam, 13 February 2026, one line per performance domain. Governance: sponsor Joost, steering every two weeks. Scope: launch scope not yet agreed, session on 3 March. Schedule: ten weeks left, five milestones. Finance: budget 380 thousand euros, 61 thousand spent or committed. Stakeholders: neighbours and the landlord not yet contacted. Resources: forty staff to hire, the first training group starts in March. Risk: top three are the cold-room delivery, hiring, and StockPilot's rate limit. Three tabs are amber.",
                "Seven tabs, one line each, every week. Three are amber, and only one of them is the schedule.")
tabs = [("governance", "sponsor Joost · steering fortnightly", "green"),
        ("scope", "launch scope not agreed → 3 March", "y"),
        ("schedule", "10 weeks left · 5 milestones", "green"),
        ("finance", "€380k budget · €61k committed", "green"),
        ("stakeholders", "neighbours, landlord: not contacted", "y"),
        ("resources", "40 to hire · training from March", "green"),
        ("risk", "cold room · hiring · StockPilot limit", "y")]
for i, (t, s, f) in enumerate(tabs):
    y = 12 + i * 52
    pd_how.box(14, y, 180, 42, t, f, size=17, rx=6)
    pd_how.box(204, y, 542, 42, s, "paper", size=15, rx=4)
pd_how.note(380, 388, "green = fine · yellow = needs attention this week", "pen", size=15)

DOMAINS = dict(
    slug="performance-domains",
    kicker="a.k.a. “the seven performance domains”",
    tldr="A <b>performance domain</b> is an area of a project that needs looking after from start to finish. The eighth edition names seven: <b>Governance</b> (who decides), <b>Scope</b> (what), <b>Schedule</b> (when), <b>Finance</b> (how much), <b>Stakeholders</b> (for and with whom), <b>Resources</b> (people and things), <b>Risk</b> (what might happen). They affect each other, and none can be ignored for long. <b>Scan all seven, every week.</b>",
    chips=[("Family", "ways of working"), ("Lives in", "seven tabs in the project binder; seven lines in the weekly status"), ("Pairs with", "the focus areas, see the whole, the PMBOK map")],
    pmbok=dict(covers="the seven performance domains, and how they interact",
               domains=["governance", "scope", "schedule", "finance", "stakeholders", "resources", "risk"],
               focus=["initiating", "planning", "executing", "monitoring", "closing"], principles=["Adopt a holistic view"],
               older="6th: ten “knowledge areas” (integration, scope, schedule, cost, quality, resource, communications, risk, procurement, stakeholder). 7th: eight performance domains."),
    problem_side="Larder, 13 February 2026",
    problem="""  <p class="lead">Sanne's notebook is full of dates. The fridge order went out today, on time. Then Marco asks: <b>“what has Rotterdam spent so far?”</b> She doesn't know. Nor can she say whether the neighbours have been told about the building work, or who decides if the launch scope changes. <span class="hl-pink">She has been watching one dial very carefully.</span></p>
  <ul>
    <li>What feels urgent gets all the attention.</li>
    <li>Problems grow quietly in the areas nobody is watching.</li>
    <li>A fix in one area (speed up) breaks another (cost).</li>
  </ul>""",
    problem_figs=[pd_problem],
    analogy_side="the pilot's scan",
    analogy="""  <p>A pilot is taught to <b>scan</b>: heading, altitude, speed, fuel, engine, weather, other aircraft, and round again. Each dial alone says little. Together they say whether the flight is safe. Pilots who stare at one dial, even the most important, are the ones who fly into the hill.</p>""",
    analogy_figs=[pd_analogy],
    map=[("Heading", "Scope: are we still going to the right place?"),
         ("Speed and time", "Schedule"),
         ("Fuel", "Finance"),
         ("Engine and crew", "Resources"),
         ("Weather", "Risk"),
         ("Air traffic control, other aircraft", "Stakeholders, Governance")],
    how_side="seven tabs, one line each, every week",
    how="""  <p>Sanne sets up a binder with <b>seven tabs</b> and writes one line under each for Rotterdam. It takes an afternoon to fill the gaps: Marco's team gives her the spend (<b>€61k of €380k</b> spent or committed). Three tabs come out amber, and only one of them is the one she'd been watching. <b>Scope</b>: nobody has agreed what customers get at launch, so she books a session for 3 March. <b>Stakeholders</b>: the neighbours and the landlord haven't heard from Larder. <b>Risk</b>: three big ones, written down for the first time. From now on the weekly status has seven lines.</p>""",
    how_figs=[pd_how],
    steps=[("Governance", "Who decides, how do we start, steer, change and close?"),
           ("Scope", "What will we deliver, and what not?"),
           ("Schedule", "By when?"),
           ("Finance", "For how much, and is the money there when needed?"),
           ("Stakeholders", "Who is affected, and what do they need from us?"),
           ("Resources", "Which people and things, and how is the team led?"),
           ("Risk", "What could go wrong, or better than planned?")],
    vocab=[("Performance domain", "A group of related activities that matter for delivering the project's results."),
           ("Governance", "The way decisions are made, checked and escalated."),
           ("Scope", "The work and results the project will deliver."),
           ("Stakeholder", "Anyone who affects the project or is affected by it."),
           ("Resources", "The people, equipment, materials and places a project needs."),
           ("Risk", "An uncertain event that would matter if it happened, for better or worse."),
           ("Knowledge area", "The sixth edition's grouping; ten of them.")],
    code=dict(file="rotterdam/seven-tabs.md", note="Sanne, 13 February 2026 · 10 weeks to opening", plain=True, src="""
# Rotterdam · the seven tabs · week of 9 February 2026

GOVERNANCE    ok     sponsor Joost · steering (Femke, Marco, Priya, Joost) fortnightly · 3 triggers
SCOPE         AMBER  what customers get at launch is not agreed → session 3 March
SCHEDULE      ok     10 weeks left · milestones 3, 17, 20, 24, 27 April · fridge order placed today
FINANCE       ok     budget €380k · spent or committed €61k · reserve €6k after the fridge choice
STAKEHOLDERS  AMBER  neighbours and landlord not told about building work → Joost, this week
RESOURCES     ok     ~40 pickers and couriers to hire · first training group in March at Noord
RISK          AMBER  top 3 written down: cold-room delivery · hiring on time · StockPilot rate limit

Where one tab pulls another:  speeding up the fit-out (schedule) costs overtime (finance)
                              cutting launch scope (scope) frees Ben's team (resources)
"""),
    tools="tools: a binder with seven tabs, or seven lines in a document. The discipline is the weekly scan.",
    dial=[("Light", "a small, short project", ["Seven questions in your head.", "A line each when something changes.", "Five minutes a week."]),
          ("Standard", "Rotterdam", ["Seven lines in the weekly status.", "A colour and a next step for each.", "The pulls between them noted."]),
          ("Heavy", "large or contracted work", ["A management plan per domain.", "Measures and thresholds for each.", "Domain leads reporting to the project manager."])],
    baseline="Each line compares <b>watching the schedule closely and the rest by accident</b> to <b>a weekly scan of all seven domains</b>.",
    ratings=[(3, 4, "Scope is checked against the benefit."),
             (3, 4, "Money and people are forecast, not only dates."),
             (2, 4, "Quiet problems are found early."),
             (2, 5, "Seven lines anyone can read."),
             (3, 4, "Marco gets his answer."),
             (3, 3, "Neutral."),
             (3, 4, "Trade-offs between domains are visible."),
             (3, 3, "Neutral."),
             (4, 3, "An afternoon to set up; minutes a week after.")],
    pitfalls=[("Staring at one dial", "Usually the schedule.", "scan all seven."),
              ("Seven silos", "Each domain managed alone.", "note where one pulls another."),
              ("Seven heavy plans", "For a fifteen-week project.", "one line each; tailor."),
              ("Green by default", "Nobody looked.", "a line of evidence, or it's unknown.")],
    use=["Every week, on every project.", "When you inherit a project: where are the blanks?", "Building a status report.", "Finding your way around the PMBOK Guide."],
    skip=["Never; shrink it to seven questions."],
    related=["<b>What Do I Do When?</b> (previous note)", "<b>See the Whole</b> (this volume)", "<b>The PMBOK map</b>", "<b>Trade-off sliders</b> (Ana, vol. 2)"],
    quiz=[("Name the seven domains.", "Governance, scope, schedule, finance, stakeholders, resources, risk."),
          ("Which domains answer “what”, “when” and “how much”?", "Scope, schedule and finance."),
          ("How many knowledge areas did the sixth edition have?", "Ten."),
          ("The builder offers to finish a week early for €9,000 of overtime. Which tabs does Sanne look at?", "Schedule (a week gained), finance (reserve is €6k: not enough), risk (does a week of float reduce the top risks?), governance (over €5,000: Joost decides)."),
          ("A tab is green because nobody has checked it. What is its real status?", "Unknown. Sanne writes “not checked” and checks it.")],
    try_it="Write the seven domain names down the side of a page. Next to each, write one true line about your project today. Which line was hardest to write? Start there.",
    remember="Seven <span class=\"hl\">dials</span>. Scan them <span class=\"hl\">all</span>, every week.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the seven performance domains.",
             "Project Management Institute, <i>PMBOK Guide</i>, Seventh Edition (2021): the eight performance domains.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): the ten knowledge areas."],
)

# ------------------------------------------------------------------ 14 How Much Process Do We Need?
ta_problem = Doodle(760, 250, "Doodle of 18 February 2026. Two piles on Sanne's desk. On the left, what her old company used on every project: forty templates, a 60-page plan, a weekly two-hour meeting. On the right, what Larder uses: a chat channel and Joost's spreadsheet. One is too heavy for fifteen weeks. The other already failed at Zuid.",
                    "Forty templates, or a chat channel and a spreadsheet. Neither fits Rotterdam.")
ta_problem.box(20, 40, 300, 110, "her old company", "paper", sub="40 templates · 60-page plan", size=19, subsize=15)
ta_problem.box(440, 40, 300, 110, "Larder today", "paper", sub="a chat channel · a spreadsheet", size=19, subsize=15)
ta_problem.note(170, 186, "too heavy", "red", size=20)
ta_problem.note(590, 186, "too light (see Zuid)", "red", size=20)
ta_problem.note(380, 226, "how much is enough?", "pen", size=20)

ta_analogy = Doodle(760, 250, "Doodle of a tailor. A suit off the rack fits nobody well. A tailor starts from a standard pattern, measures the person, and takes it in or lets it out. The tailor doesn't invent a new garment, and doesn't hand over the pattern uncut.",
                    "A tailor starts from a standard pattern and fits it to the person. Not off the rack, not from nothing.")
ta_analogy.row([("the pattern", "the standard", "paper"), ("measure", "this person", "y"), ("cut to fit", "take in, let out", "blue"), ("try it on", "adjust again", "green")], y=50, h=90, size=17, subsize=14, gap=34, arrows=True)
ta_analogy.note(380, 200, "start from the standard, cut to fit, check the fit", "pen", size=19)

ta_how = Doodle(760, 400, "Sanne's tailoring table for Rotterdam, 18 February 2026. For each practice, what she keeps and how big. Charter: one page. Plan: one page plus a milestone chart. Risk register: the top fifteen, reviewed weekly. Status: one page, seven lines, every Friday. Change control: three triggers, no form. Meetings: one thirty-minute weekly, Thursdays 09:30. Lessons: a line a week. Left out on purpose: a separate communications plan, a procurement plan, earned value. To be reviewed on 20 March.",
                "For each practice: keep it, shrink it, or leave it out on purpose. Then review the fit.")
rowsT = [("charter", "1 page", "keep, small"), ("plan", "1 page + milestone chart", "keep, small"), ("risk register", "top 15 · weekly", "keep, small"),
         ("status", "1 page · 7 lines · Fridays", "keep"), ("change control", "3 triggers · no form", "shrink"), ("meetings", "30 min · Thu 09:30", "shrink"),
         ("comms + procurement plans · earned value", "", "leave out")]
for i, (p, how, v) in enumerate(rowsT):
    y = 12 + i * 48
    f = "green" if v.startswith("keep") else ("y" if v == "shrink" else "paper")
    if i < 6:
        ta_how.box(14, y, 200, 40, p, "blue", size=16, rx=5)
        ta_how.box(224, y, 340, 40, how, "paper", size=15, rx=4)
    else:
        ta_how.box(14, y, 550, 40, p, "paper", size=15, rx=5, dash=True)
    ta_how.box(574, y, 172, 40, v, f, size=15, rx=5)
ta_how.note(380, 380, "review the fit on 20 March: what was missing, what was waste?", "pen", size=16)

ta_deep1 = Doodle(760, 240, "The four steps of tailoring. One: choose the development approach. Two: fit to the organisation, what it requires and what it's used to. Three: fit to the project, its size, risk and people. Four: keep improving, review the fit and adjust. An arrow loops from step four back to step three.",
                  "Four steps: choose the approach, fit to the organisation, fit to the project, keep improving.")
ta_deep1.row([("1 approach", "predictive / adaptive", "y"), ("2 organisation", "rules, habits", "blue"), ("3 project", "size, risk, people", "green"), ("4 improve", "review the fit", "pink")], y=40, h=90, gap=34, size=17, subsize=13, arrows=True)
ta_deep1.arrow(652, 132, 466, 132, curve=(560, 190), label="adjust", lx=560, ly=188)

ta_deep2 = Doodle(760, 300, "Five dials that set how much process a project needs, each from low to high, with Rotterdam marked. Size and length: low to medium, fifteen weeks and about 380 thousand euros. What a mistake costs: medium to high, food safety and a signed lease. How new it is: medium, the second store but the first new city. How many parties: medium, seven workstreams and two vendors. How strict the rules: medium. More towards high means more process; the dials don't all move together.",
                  "Five dials set the weight. Rotterdam is light on size, heavier on what a mistake costs.")
dials = [("size and length", 0.3, "15 weeks · €380k"), ("cost of a mistake", 0.75, "food safety · the lease"), ("how new it is", 0.5, "first new city"),
         ("number of parties", 0.5, "7 workstreams · 2 vendors"), ("rules and contracts", 0.5, "lease · permits · labour law")]
for i, (t, v, s) in enumerate(dials):
    y = 30 + i * 50
    ta_deep2.text(14, y + 6, t, anchor="start", size=16)
    ta_deep2.line(f"M210 {y} h300", thin=True)
    ta_deep2.circle(210 + int(300 * v), y, 9, "y")
    ta_deep2.text(530, y + 6, s, anchor="start", size=14, cls="t t-soft")
ta_deep2.note(210, 284, "lighter", size=15)
ta_deep2.note(510, 284, "heavier", size=15)

TAILORING = dict(
    slug="tailoring",
    kicker="a.k.a. “tailoring”",
    tldr="<b>Tailoring</b> means fitting the way of working to the project: choosing which practices, documents and meetings to use, and how big to make each. The guide's forty processes are a <b>menu, not a checklist</b>. Too little process and things are forgotten (Zuid). Too much and the team serves the paperwork. Decide on purpose, <b>write down what you left out and why</b>, and review the fit once the project is moving.",
    chips=[("Family", "ways of working"), ("Lives in", "a one-page tailoring table, reviewed monthly"), ("Pairs with", "life cycles, the project environment, the dial in every note")],
    pmbok=dict(covers="tailoring: fitting the approach, processes, artefacts and governance to the project",
               principles=["Adopt a holistic view", "Focus on value"], focus=["initiating", "planning", "monitoring"],
               domains=["governance"],
               older="6th: a short “tailoring considerations” list in each knowledge area. 7th: a chapter of its own. In the 8th it is part of every domain."),
    problem_side="Larder, 18 February 2026",
    problem="""  <p class="lead">Sanne's old company had <b>forty templates</b> and a 60-page plan for every project, large or small. Larder has <b>a chat channel and Joost's spreadsheet</b>. For five weeks she has been improvising between the two. The team has started asking: is there a risk list? do we need to fill in something for changes? which meeting is the real one? <span class="hl-pink">Nobody decided how Rotterdam would be run. It just accumulated.</span></p>
  <ul>
    <li>Heavy process on a fifteen-week launch eats the fifteen weeks.</li>
    <li>No process is how Zuid opened with 340 unpriced products.</li>
    <li>Process that grows by accident fits nobody.</li>
  </ul>""",
    problem_figs=[ta_problem],
    analogy_side="the tailor",
    analogy="""  <p>A suit <b>off the rack</b> fits nobody well. A suit from nothing takes months. A <b>tailor</b> starts from a standard pattern, measures the person, takes it in here, lets it out there, and then asks them to walk around in it and adjusts again. The standard does most of the work. The fit makes it wearable.</p>""",
    analogy_figs=[ta_analogy],
    map=[("The standard pattern", "The PMBOK Guide's processes and artefacts"),
         ("Measuring the person", "Rotterdam: 15 weeks, €380k, seven workstreams, a fixed date"),
         ("Taking in and letting out", "A one-page charter; a top-15 risk list; three change triggers"),
         ("Leaving off the waistcoat", "No earned value, no separate communications plan"),
         ("Walking around in it", "Reviewing the fit on 20 March")],
    how_side="keep, shrink or leave out, on purpose",
    how="""  <p>Sanne lists the usual practices and decides each one with the leads: <b>keep</b>, <b>shrink</b>, or <b>leave out</b>. A <b>charter</b>: yes, one page. A <b>plan</b>: one page and a milestone chart. A <b>risk register</b>: the top fifteen, looked at weekly. <b>Status</b>: one page, seven lines, every Friday. <b>Change control</b>: the three triggers, no form. <b>Meetings</b>: one, thirty minutes, Thursdays at 09:30. Left out, with reasons written down: a communications plan, a procurement plan, earned value. A date goes in the diary to <b>review the fit</b>: 20 March.</p>""",
    how_figs=[ta_how],
    steps=[("List the practices you might use", "From the standard, and from your organisation."),
           ("Measure the project", "Size, risk, novelty, parties, rules."),
           ("For each practice: keep, shrink or leave out", "With the team."),
           ("Write down what you left out, and why", "So it's a decision, not a gap."),
           ("Check with the sponsor and any required rules", "Some things aren't optional."),
           ("Review the fit after a month", "What was missing? What was waste?")],
    vocab=[("Tailoring", "Deliberately adapting the approach, governance and processes to suit the project."),
           ("Artefact", "A document or other output of project management: a plan, a register, a report."),
           ("Process", "A set of activities that turns inputs into outputs."),
           ("Ceremony", "A regular meeting with a fixed purpose."),
           ("Just enough", "The least process that still controls the risk."),
           ("Retrospective", "A look back at how the work is going, to improve the way of working.")],
    code=dict(file="rotterdam/how-we-run-this.md", note="tailoring table · Sanne with the leads, 18 February 2026", plain=True, src="""
# Rotterdam · how we run this (15 weeks · €380k · 7 workstreams · date fixed)

PRACTICE             FOR ROTTERDAM                              DECISION
Charter              1 page: why, benefit, sponsor, limits      keep, small
Plan                 1 page + milestone chart (5 milestones)    keep, small
Risk register        top 15, owner each, reviewed Thursdays     keep, small
Status report        1 page, 7 lines, Fridays to the steering   keep
Change control       3 triggers → Joost; a line in the log      shrink
Decision log         shared with Ana (reviewed Mondays)         reuse
Meetings             one: Thursdays 09:30, 30 min, the leads    shrink
Lessons              one line a week, sorted in May             keep, small

LEFT OUT, ON PURPOSE
  communications plan   7 lines in the status cover it
  procurement plan      two vendors; contracts handled by Joost and Lena
  earned value          too heavy for 15 weeks; must-haves done / 71 is our measure

Review the fit: 20 March (what was missing? what was waste?)
"""),
    tools="tools: the list of practices, five measures of the project (see the deep dive), and a review date.",
    deep_dive=dict(
        side="how to tailor, step by step",
        intro="“Use judgment” is true and not much help. This deep dive gives the judgment something to hold: the four steps of tailoring, five dials that tell you how heavy to go, the things you may not tailor away, and what a review of the fit looks like.",
        parts=[
            ("The four steps", """  <ol class="steps">
    <li><b>Choose the approach.</b><p>Predictive, adaptive or hybrid, per workstream (the note before last). This sets the shape of everything else.</p></li>
    <li><b>Fit to the organisation.</b><p>What does your organisation require (finance approvals, security review, a PMO's templates)? What is it used to? Start from there; don't fight habits you don't need to.</p></li>
    <li><b>Fit to the project.</b><p>Now size each practice for this project: its length, risk, people and rules. This is the tailoring table.</p></li>
    <li><b>Keep improving.</b><p>Review the fit while the project runs. Add what was missed, drop what nobody used.</p></li>
  </ol>""", [ta_deep1]),
            ("Five dials that set the weight", """  <p>Five things decide how much process a project needs. Mark your project on each:</p>
  <ul>
    <li><b>Size and length.</b> Fifteen weeks needs less than three years.</li>
    <li><b>What a mistake costs.</b> Food safety and a signed lease cost more than a slow web page.</li>
    <li><b>How new it is.</b> The tenth store needs less than the first city.</li>
    <li><b>How many parties.</b> Each extra team or vendor adds joins to manage.</li>
    <li><b>How strict the rules are.</b> Contracts, regulators and auditors require evidence.</li>
  </ul>
  <p>The dials don't move together, and that is the useful part. Rotterdam is <b>light on size</b> but <b>heavier on the cost of a mistake</b>. So Sanne keeps documents short and spends her process on the places where a mistake is expensive: the quality checks, the long-lead orders, the go / no-go.</p>""", [ta_deep2]),
            ("What you may not tailor away", """  <p>Tailoring changes <b>how</b>, never <b>whether</b>, for a few things:</p>
  <ul>
    <li><b>The principles.</b> You can drop a template. You can't drop telling the truth about status, or thinking about value.</li>
    <li><b>The law and contracts.</b> Food-safety registration, the lease, labour rules.</li>
    <li><b>Your organisation's hard rules.</b> At Larder: Marco approves spending; Lena reviews contracts.</li>
    <li><b>The seven questions.</b> Every domain still needs an answer, even if the answer is one line.</li>
  </ul>
  <p>A useful test: if you leave a practice out, can you say <b>which risk it would have covered</b> and <b>what covers it now</b>? “No communications plan, because the weekly status reaches everyone who needs it” passes. “No risk list, because we're agile” doesn't.</p>""", []),
            ("Reviewing the fit", """  <p>On <b>20 March</b>, a month in, Sanne asks the leads two questions: <b>what did we miss that a bit more process would have caught?</b> and <b>what did we do that nobody used?</b></p>
  <p>The answers go straight into the table. A way of working that has never been changed is a sign that nobody has looked at it. Later notes show what that review found. One thing to know now: the table had no line for <b>store IT and internet</b>, because it sat between the fit-out and the platform. Tailoring can't see what the whole-project map misses.</p>""", []),
        ]),
    dial=[("Light", "a small, familiar project", ["A conversation: “how do we want to run this?”", "Three or four practices.", "Adjust as you go."]),
          ("Standard", "Rotterdam", ["A one-page tailoring table.", "Left-outs written down with reasons.", "A review after a month."]),
          ("Heavy", "large, regulated, many parties", ["Tailoring agreed with a PMO.", "Formal approval of deviations.", "Reviewed at each phase gate."])],
    baseline="Each line compares <b>process that accumulated by accident</b> to <b>a one-page tailoring table, decided with the team and reviewed</b>.",
    ratings=[(3, 4, "Effort goes where the risk is."),
             (3, 4, "The practices that protect the date are kept."),
             (2, 4, "Process sized to what a mistake costs."),
             (2, 4, "Everyone knows how the project is run."),
             (3, 4, "The sponsor agreed the way of working."),
             (2, 4, "The team helped choose it."),
             (3, 4, "A review date is built in."),
             (3, 4, "Checks are kept where they matter."),
             (2, 4, "One meeting, one page each.")],
    pitfalls=[("Tailoring as “skip it”", "Leaving things out to save effort now.", "name the risk and what covers it."),
              ("Tailoring alone", "The team gets a process handed down.", "decide with the leads."),
              ("Never reviewed", "The fit drifts.", "a date in the diary."),
              ("Every template, shrunk", "Forty one-page documents.", "leave some out completely.")],
    use=["At the start of every project.", "When the team asks “do we have to?”", "When process feels heavy or things keep being missed.", "At each new phase."],
    skip=["Never skip the decision. The table itself can be five lines."],
    related=["<b>Plan It All, or Learn As We Go?</b> (this volume)", "<b>What Was Here Before Me?</b> (this volume)", "<b>Who Helps the Project Managers?</b> (next note)", "<b>Tailoring a whole project</b> (vol. 6)"],
    quiz=[("What is tailoring?", "Deliberately fitting the approach, processes and documents to the project."),
          ("Are the forty processes compulsory?", "No. They are a menu."),
          ("Name the four steps.", "Choose the approach, fit to the organisation, fit to the project, keep improving."),
          ("Ben says “we're only fifteen weeks, let's drop the risk list”. What does Sanne ask?", "Which risks it covers and what would cover them instead. Nothing would, so it stays, at fifteen lines."),
          ("What can't be tailored away?", "The principles, the law and contracts, the organisation's hard rules, and an answer for each of the seven domains.")],
    try_it="List every document and meeting your project uses. Mark each keep, shrink or drop, and for each drop write what covers that risk now. Put a date in your diary one month from today: “review the fit”.",
    remember="Start from the <span class=\"hl\">pattern</span>. Cut it to <span class=\"hl\">fit</span>. Then walk around in it.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): tailoring.",
             "Project Management Institute, <i>PMBOK Guide</i>, Seventh Edition (2021): the tailoring chapter.",
             "Alistair Cockburn, <i>Crystal Clear</i> (2004): methodology weight and criticality.",
             "Barry Boehm and Richard Turner, <i>Balancing Agility and Discipline</i> (2003)."],
)

# ------------------------------------------------------------------ 15 Who Helps the Project Managers?
po_problem = Doodle(760, 250, "Doodle of 25 February 2026. Femke counts on her fingers: Rotterdam, then Utrecht, The Hague, Eindhoven and Antwerp, plus Korenwolf for Larder for Business. Six projects in two years and one project manager who started six weeks ago. She asks: do we need a project management office?",
                    "Five more launches and a business client, and one project manager. “Do we need a PMO?”")
for i, t in enumerate(["Rotterdam", "Utrecht", "The Hague", "Eindhoven", "Antwerp", "Korenwolf"]):
    po_problem.box(14 + i * 124, 30, 112, 60, t, "y" if i == 0 else "paper", size=14, dash=i > 0)
po_problem.circle(380, 160, 34, "blue", label="Sanne")
po_problem.note(380, 226, "Femke: “do we need a PMO?”", "red", size=20)

po_analogy = Doodle(760, 250, "Doodle of a hospital. Each surgeon runs their own operations. Behind them is a small team that keeps the checklists up to date, schedules the theatres, collects what went wrong and teaches it to new surgeons. That team never operates. If it started telling surgeons where to cut, it would be in the way.",
                    "The team that keeps the checklists and schedules the theatres doesn't hold the knife.")
po_analogy.row([("checklists", "kept up to date", "y"), ("theatre schedule", "who needs what, when", "blue"), ("lessons", "collected and taught", "green")], y=50, h=90, size=18, subsize=14)
po_analogy.note(380, 200, "helps every surgeon · never operates", "pen", size=20)

po_how = Doodle(760, 390, "Three kinds of project management office, and the one Sanne proposes on 25 February 2026. Supportive: offers templates, lessons and advice; low control. Controlling: requires a method and checks it is followed; medium control. Directive: runs the projects itself; high control. For Larder she proposes a launch desk, a supportive office: one plan template, one status format, one risk and lessons page across cities, and a quarterly look across all projects for Femke. It costs two hours a week.",
                "Supportive, controlling or directive. Larder gets the lightest: a “launch desk”.")
po_how.row([("supportive", "templates · lessons · advice", "green"), ("controlling", "a required method · checks", "y"), ("directive", "runs the projects itself", "pink")], y=14, h=90, size=19, subsize=13)
po_how.note(132, 132, "low control", size=15)
po_how.note(380, 132, "medium", size=15)
po_how.note(628, 132, "high control", size=15)
po_how.arrow(132, 144, 240, 178, color="green")
po_how.box(14, 180, 732, 180, None, "blue")
po_how.head(380, 210, "Larder's launch desk (supportive) · 2 hours a week", size=19)
for i, t in enumerate(["one plan template · one status format", "one risk + lessons page across all cities",
                       "the launch playbook, updated after each city", "a quarterly look across projects, for Femke"]):
    po_how.text(380, 244 + i * 28, t, size=16)

PMO = dict(
    slug="pmo",
    kicker="a.k.a. “the project management office (PMO)”",
    tldr="A <b>project management office</b> (PMO) is whatever helps an organisation run its projects in a consistent way: shared templates and lessons, a view across all projects, sometimes rules, sometimes the project managers themselves. It can be <b>supportive</b> (helps), <b>controlling</b> (requires and checks) or <b>directive</b> (runs the projects). The right size is <b>the lightest one that stops each project from starting at zero</b>.",
    chips=[("Family", "ways of working"), ("Lives in", "a shared folder and two hours a week, at first"), ("Pairs with", "tailoring, lessons learned, the portfolio")],
    pmbok=dict(covers="the project management office: what it is for, and its forms", domains=["governance"],
               focus=["initiating", "monitoring", "closing"],
               older="6th: section 2.4, three types (supportive, controlling, directive). 7th: “project management offices” under the system for value delivery. The 8th adds an appendix on PMOs."),
    problem_side="Larder, 25 February 2026",
    problem="""  <p class="lead">Femke counts on her fingers: Rotterdam, then <b>Utrecht, The Hague, Eindhoven and Antwerp</b>, and Mo arrives next week for Larder for Business. Six projects in two years, and one project manager, six weeks in. A board member has told her that serious companies have a PMO. <span class="hl-pink">“Do we need one?”</span> Ben, overhearing: “please, no.”</p>
  <ul>
    <li>Every launch so far started from a blank page.</li>
    <li>Nobody sees all the projects on one sheet.</li>
    <li>A heavy PMO would cost more than the problem.</li>
  </ul>""",
    problem_figs=[po_problem],
    analogy_side="the team behind the surgeons",
    analogy="""  <p>In a hospital each <b>surgeon</b> runs their own operations. Behind them, a small team <b>keeps the checklists</b> current, <b>schedules the theatres</b>, and <b>collects what went wrong</b> so the next surgeon doesn't repeat it. That team never holds the knife. When it starts telling surgeons where to cut, the surgeons stop listening, and they are right to.</p>""",
    analogy_figs=[po_analogy],
    map=[("The surgeons", "Whoever leads each launch: Sanne now, others later"),
         ("The checklists", "A plan template, a status format, the launch playbook"),
         ("The theatre schedule", "One sheet of all projects, for Femke"),
         ("What went wrong, collected", "A lessons page across cities"),
         ("Never holding the knife", "The desk doesn't run the projects")],
    how_side="the lightest office that stops each project starting from zero",
    how="""  <p>Sanne explains the three kinds. A <b>supportive</b> PMO offers templates, lessons and advice. A <b>controlling</b> one requires a method and checks it. A <b>directive</b> one runs the projects. For a company of Larder's size, with six similar launches ahead, she proposes the lightest: a <b>“launch desk”</b>. One plan template and one status format (Rotterdam's). One risk and lessons page across all cities. The launch playbook, updated after each city. And once a quarter, <b>one sheet of all projects</b> for Femke. Cost: two hours of her week. Femke agrees to try it until Utrecht, and to look again then.</p>""",
    how_figs=[po_how],
    steps=[("List the projects coming", "And who will lead them."),
           ("Ask what each one would otherwise reinvent", "Templates, lessons, decisions."),
           ("Choose the lightest form that covers it", "Supportive first."),
           ("Start with what one project already made", "Rotterdam's pages become the templates."),
           ("Give leadership one view across projects", "Quarterly is enough to begin."),
           ("Review when the number of projects changes", "Grow it only when it's missed.")],
    vocab=[("PMO", "Project management office: a function that supports or standardises how projects are run."),
           ("Supportive PMO", "Offers templates, training and lessons. Low control."),
           ("Controlling PMO", "Requires certain methods and checks compliance. Medium control."),
           ("Directive PMO", "Manages the projects directly. High control."),
           ("Portfolio view", "All projects on one sheet, for those who choose between them."),
           ("Centre of excellence", "A group that keeps and spreads good practice.")],
    code=dict(file="larder/launch-desk.md", note="Sanne's proposal to Femke, 25 February 2026 · agreed until Utrecht", plain=True, src="""
# The launch desk · a supportive PMO, as small as possible

WHY     six projects in two years; each one so far started from a blank page
WHO     Sanne, 2 hours a week (no new people)

WHAT IT KEEPS
  templates   plan on a page · weekly status (7 lines) · role card · tailoring table
  lessons     one page across all cities, one line a week, sorted after each launch
  playbook    "how to open a city", updated after Rotterdam, used for Utrecht
  one sheet   every project: sponsor, benefit, next milestone, colour → Femke, quarterly

WHAT IT DOESN'T DO
  run other people's projects · approve their plans · add meetings

REVIEW  at the start of Utrecht: was anything reinvented? was anything unused?
"""),
    tools="tools: a shared folder, the documents one project already made, and one sheet for leadership.",
    dial=[("Light", "a few projects, one or two project managers", ["A shared folder of templates and lessons.", "One sheet across projects.", "A couple of hours a week."]),
          ("Standard", "a dozen projects a year", ["A small supportive team.", "Common status and risk formats.", "Coaching for new project managers."]),
          ("Heavy", "many large or regulated projects", ["A controlling or directive PMO.", "A required method and tools.", "Portfolio reporting and assurance."])],
    baseline="Each line compares <b>every launch starting from a blank page</b> to <b>a small supportive launch desk: shared templates, lessons, a playbook and one sheet across projects</b>.",
    ratings=[(3, 4, "The next city in eight weeks needs a playbook."),
             (2, 4, "Plans start from what really happened last time."),
             (2, 4, "Lessons travel to the next launch."),
             (2, 4, "Femke sees all projects on one sheet."),
             (3, 4, "The board's question has an answer."),
             (3, 3, "Neutral: it must not take decisions away."),
             (3, 3, "Neutral."),
             (3, 4, "Good practice is reused."),
             (4, 3, "Two hours a week.")],
    pitfalls=[("A PMO because “serious companies have one”", "Size before need.", "start from what gets reinvented."),
              ("The template police", "Checking forms, not helping projects.", "supportive first; measure by what teams reuse."),
              ("A PMO that owns the projects by accident", "Leads stop feeling responsible.", "say what it doesn't do."),
              ("Lessons nobody reads", "A graveyard folder.", "one page, sorted, used at every kick-off.")],
    use=["Several similar projects are coming.", "Leadership can't see all projects together.", "Each project reinvents the basics.", "New project managers are joining."],
    skip=["One project at a time and no repeats in sight."],
    related=["<b>How Much Process Do We Need?</b> (previous note)", "<b>What Is It All For?</b> (this volume)", "<b>Lessons learned that get used</b> (vol. 2)", "<b>The city launch playbook</b> (vol. 6)"],
    quiz=[("Name the three kinds of PMO.", "Supportive, controlling, directive."),
          ("Which did Sanne propose, and why?", "Supportive: the lightest that stops each launch starting from zero."),
          ("What does the launch desk not do?", "Run other people's projects, approve their plans, or add meetings."),
          ("At Utrecht's kick-off the new lead ignores the templates and writes her own. What does Sanne do?", "Ask why. If hers is better, the template changes. A supportive desk is judged by what teams choose to reuse."),
          ("When would Larder need a heavier PMO?", "When there are many more projects, new project managers, or rules that require proof of how projects are run.")],
    try_it="Count the projects your organisation will run in the next year. Name three things each one will reinvent. What is the smallest thing (a folder, a page, an hour a month) that would stop that?",
    remember="Keep the <span class=\"hl\">checklists</span>. Don't hold the <span class=\"hl\">knife</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): project management offices.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): section 2.4, PMO types.",
             "Brian Hobbs and Monique Aubry, <i>The Project Management Office (PMO): A Quest for Understanding</i> (2010)."],
)

NOTES = [LIFE_CYCLES, FOCUS, DOMAINS, TAILORING, PMO]
