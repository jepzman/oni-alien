# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 3 · What, exactly? (the Scope domain)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 3").
# Spine: PMBOK Guide, Eighth Edition. Names are PMI's; every explanation is in our own words.

# ------------------------------------------------------------------ 01 How Will We Pin It Down?
ap_problem = Doodle(760, 250, "Doodle of 10 February 2026. Four kinds of plan sit on Sanne's desk and none of them can be compared with another. Joost's spreadsheet: 140 rows, no row says when it counts as done. The builder's quote: five weeks, one line. Ben's team: two-week sprints, no dates. Grace's app scope: not decided until 3 March.",
                    "Four kinds of plan, four different units, and no way to lay one beside another.")
ap_problem.row([("Joost's rows", "140 · no “done”", "paper"), ("builder's quote", "“5 weeks”", "paper"), ("Ben's sprints", "no dates", "paper"), ("app scope", "decided 3 March", "pink")], y=30, h=84, size=16, subsize=13)
ap_problem.note(380, 168, "rows, weeks, sprints, “later”", "red", size=20)
ap_problem.note(380, 206, "how will any of this be measured?", "pen", size=18)

ap_analogy = Doodle(760, 250, "Doodle of a map-maker before drawing. Three decisions come first: the scale, the legend and the grid. The town centre is drawn street by street; the far hills only as outlines, to be filled in when someone walks there. The map is redrawn on a fixed cycle.",
                    "Before drawing, a map-maker picks a scale, a legend and a grid. The near part is detailed; the far part is sketched.")
ap_analogy.icon("map", 40, 60, 1.6)
ap_analogy.row([("scale", "how much detail", "y"), ("legend", "what each mark means", "blue"), ("grid", "the units", "green")], x=180, y=60, h=84, w=178, gap=10, size=17, subsize=13)
ap_analogy.note(460, 196, "near: street by street · far: outlines", "pen", size=19)

ap_how = Doodle(760, 400, "Sanne's one page of rules for scope and schedule on the Rotterdam launch, 10 February 2026. Scope: the unit is a must-have with an owner and a done-means line; the must-haves are broken down by workstream; each is accepted by its owner at a gate; changes follow the three triggers. Schedule: the predictive workstreams are scheduled in working days, Monday to Friday, with the builder off on Easter Monday 6 April; the adaptive ones in two-week sprints. Detail for the next four weeks, milestones beyond. Tracked every Thursday, baselined on 13 March.",
                "One page of rules before any plan: the unit, the detail, the calendar, how it is tracked, how it changes.")
ap_how.box(14, 14, 360, 210, None, "blue")
ap_how.head(194, 42, "scope", size=20)
for i, t in enumerate(["unit: a must-have + owner + “done means”", "broken down by workstream", "accepted by its owner at a gate", "changed only by the three triggers"]):
    ap_how.text(194, 78 + i * 36, t, size=14)
ap_how.box(386, 14, 360, 210, None, "y")
ap_how.head(566, 42, "schedule", size=20)
for i, t in enumerate(["predictive: working days, Mon–Fri", "adaptive: two-week sprints", "detail 4 weeks ahead, milestones beyond", "tracked Thursdays · baseline 13 Mar"]):
    ap_how.text(566, 78 + i * 36, t, size=14)
ap_how.box(14, 246, 732, 92, None, "paper", dash=True)
ap_how.head(380, 274, "the calendar", size=18)
ap_how.text(380, 306, "Easter Monday 6 Apr: builders off  ·  King's Day 27 Apr: opening day, stores and couriers work", size=14)
ap_how.note(380, 372, "decided once, before the first estimate", "pen", size=17)

APPROACH = dict(
    slug="scope-schedule-approach",
    kicker="a.k.a. “planning scope management” and “planning schedule management”",
    tldr="Before you write down scope or dates, decide <b>how</b> you will: what the unit of scope is and who accepts it, how far it will be broken down, which <b>units and calendar</b> the schedule uses, how much detail to plan now and how much later (<b>rolling wave</b>), how progress will be tracked and how changes are made. It fits on a page. Without it, every workstream plans in its own units, and no two plans can be added up.",
    chips=[("Family", "what, exactly?"), ("Lives in", "one page at the front of the plan"), ("Pairs with", "tailoring, the plan on a page, life cycles")],
    pmbok=dict(covers="how scope will be defined, broken down, accepted and controlled; how the schedule will be built, in what units and detail, and tracked",
               domains=["scope", "schedule"], processes=["Plan Scope Management", "Plan Schedule Management"],
               principles=["Adopt a holistic view"], focus=["planning"],
               older="6th: “Plan Scope Management” (5.1) and “Plan Schedule Management” (6.1), each producing a management plan. 7th: the Planning domain."),
    problem_side="Larder, 10 February 2026",
    problem="""  <p class="lead">Ten days before the plan is due, Sanne has four kinds of plan on her desk. <b>Joost's spreadsheet</b>: 140 rows, and no row says when it counts as done. <b>The builder's quote</b>: “about five weeks”, in one line. <b>Ben's team</b>: two-week sprints and no dates at all. <b>The app scope</b>: Grace won't settle it until 3 March. <span class="hl-pink">Each is a reasonable way to plan. None can be laid beside another</span>, so nobody can say whether they add up to 27 April.</p>
  <ul>
    <li>Rows, weeks, sprints and “later” are four different units.</li>
    <li>Nobody has said what “done” means, or who says so.</li>
    <li>Nobody has said how far ahead to plan in detail.</li>
  </ul>""",
    problem_figs=[ap_problem],
    analogy_side="the map-maker's first decisions",
    analogy="""  <p>Before drawing a line, a map-maker decides three things: the <b>scale</b> (how much detail), the <b>legend</b> (what each mark means) and the <b>grid</b> (the units). The town centre is drawn street by street; the hills beyond are outlines, filled in when someone walks there. Two maps with different scales can't be pinned edge to edge. Two plans with different units can't either.</p>""",
    analogy_figs=[ap_analogy],
    map=[("The legend", "A must-have: owner, “done means”, accepted at a gate"),
         ("The scale", "Detail for the next four weeks; milestones beyond"),
         ("The grid", "Working days for the predictive work; two-week sprints for the adaptive"),
         ("Filling in the hills later", "Rolling-wave planning"),
         ("Redrawing on a cycle", "Updated on Thursdays; baselined on 13 March")],
    how_side="one page of rules, before the first estimate",
    how="""  <p>Sanne writes the rules before the plan. For <b>scope</b>: the unit is a <b>must-have</b>, each with an owner and a “done means” line; the must-haves are broken down by workstream; each is <b>accepted by its owner</b> at a gate; changes follow the three triggers. For the <b>schedule</b>: the predictive workstreams are planned in <b>working days, Monday to Friday</b>; the adaptive ones in <b>two-week sprints</b>. Detail is planned four weeks ahead and milestones beyond (<b>rolling wave</b>). And a calendar: the builder doesn't work on <b>Easter Monday, 6 April</b>; opening day, <b>27 April</b>, is King's Day, when the store and couriers work and offices don't. That calendar line turns out to matter on 23 March.</p>""",
    how_figs=[ap_how],
    steps=[("Choose the unit of scope", "And who accepts it."),
           ("Decide how far to break it down", "Until each piece has an owner and a check."),
           ("Choose the units of time", "Working days, sprints, or both."),
           ("Write the calendar", "Holidays, shutdowns, who works when."),
           ("Decide the planning horizon", "Detail near, outline far; when to fill in."),
           ("Say how progress and change are handled", "Then start planning.")],
    vocab=[("Scope management plan", "How scope will be defined, broken down, accepted and controlled."),
           ("Schedule management plan", "How the schedule will be built, in what units and detail, and tracked."),
           ("Rolling-wave planning", "Detailed planning for near work; outline planning for later work, filled in as it approaches."),
           ("Project calendar", "The working days and hours the schedule counts in."),
           ("Unit of measure", "What the plan counts in: days, story points, must-haves."),
           ("Planning horizon", "How far ahead the detailed plan reaches.")],
    code=dict(file="rotterdam/16-scope-and-schedule-rules.md", note="Sanne, 10 February 2026 · agreed with the leads", plain=True, src="""
# ROTTERDAM · HOW WE HANDLE SCOPE AND SCHEDULE

SCOPE
  unit          a must-have: one line, an owner, a "done means" (71 of them)
  breakdown     by workstream (the WBS, by 17 Feb); the app branch = Grace's story map
  requirements  from the people who will live with it (workshop 12 Feb)
  acceptance    each must-have accepted by its owner; groups accepted at the gates
  change        the three triggers; anything else is the team's or Sanne's call

SCHEDULE
  predictive    fit-out, people, stock, payments + legal: activities in WORKING DAYS
  adaptive      platform, apps, marketing: TWO-WEEK SPRINTS, a demo each
  horizon       activities for the next 4 weeks; milestones beyond (rolling wave)
  calendar      Mon–Fri · Easter Monday 6 Apr: builder off · King's Day 27 Apr:
                opening day (store and couriers work; offices and builders don't)
  estimates     a range from whoever does the work (best · likely · worst)
  tracking      Thursdays: milestones, must-haves done, float on the critical path
  baseline      steering group, 13 March
"""),
    tools="tools: one page, written before the plan, with the leads in the room.",
    dial=[("Light", "a short job for one team", ["Agree the unit and the definition of done.", "One calendar.", "Said, not written."]),
          ("Standard", "Rotterdam", ["One page of rules for scope and schedule.", "Working days and sprints side by side.", "Rolling wave, four weeks ahead."]),
          ("Heavy", "large or contracted work", ["Separate scope and schedule management plans.", "Scheduling standards and tools.", "Formal calendars per contractor."])],
    baseline="Each line compares <b>every workstream planning in its own units</b> to <b>one page of rules for scope and schedule, agreed before planning</b>.",
    ratings=[(3, 4, "Must-haves, not activity, are the unit."),
             (2, 4, "Plans in the same units can be added up."),
             (2, 4, "The calendar catches holidays in February."),
             (2, 4, "Everyone knows how progress is counted."),
             (3, 4, "The steering group knows when the baseline comes."),
             (3, 4, "Each kind of team keeps its own rhythm."),
             (3, 4, "Rolling wave leaves later detail open."),
             (3, 4, "“Done means” is required from the start."),
             (4, 4, "One page.")],
    pitfalls=[("Planning first, rules later", "Four units, no sum.", "a page of rules before the first estimate."),
              ("Detail to the horizon", "Week 14 planned by the hour, then wrong.", "rolling wave: detail near, outline far."),
              ("No calendar", "Holidays found by accident.", "write the working days and holidays down."),
              ("One method forced on all", "Sprints for the builder, Gantt for the app.", "both, in the same rules.")],
    use=["At the start of planning.", "When teams plan in different units.", "When a hybrid project needs one view.", "Before asking anyone for an estimate."],
    skip=["A one-team job that already has a working rhythm: write the calendar only."],
    related=["<b>How Much Process Do We Need?</b> (vol. 1)", "<b>Plan It All, or Learn As We Go?</b> (vol. 1)", "<b>What's the Plan?</b> (vol. 2)", "<b>How Do We Break It Down?</b> (this volume)"],
    quiz=[("What is Rotterdam's unit of scope?", "A must-have with an owner and a “done means” line."),
          ("What is rolling-wave planning?", "Detail for near work, outline for later work, filled in as it gets closer."),
          ("Why write a calendar?", "So holidays and non-working days are in the plan, not discovered."),
          ("The builder says “five weeks”; Ben says “three sprints”. How does Sanne compare them?", "In the same calendar: five weeks is 25 working days from 2 March; three sprints is six weeks from the sprint start. Then both are dates."),
          ("On 10 February Joost wants every activity to 27 April planned by the day. What does Sanne answer?", "Detail for the next four weeks, milestones beyond. The far detail would be guesses, and it would be wrong by March.")],
    try_it="Write your project's rules on half a page: the unit of scope and who accepts it, the units of time, the calendar (with holidays), how far ahead you plan in detail, and how progress is counted. Which line did nobody agree before?",
    remember="Pick the <span class=\"hl\">scale</span>, the <span class=\"hl\">legend</span> and the <span class=\"hl\">grid</span> before you draw.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Scope and Schedule domains, planning.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 5.1 Plan Scope Management, 6.1 Plan Schedule Management.",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019)."],
)

# ------------------------------------------------------------------ 02 What Do They Actually Need?
rq_problem = Doodle(760, 250, "Doodle of Joost's spreadsheet on 11 February 2026. Many rows are solutions, not needs: a second cold-room door, forty chargers, the same shelving as Zuid. One row says only: same as Zuid. Tomás points out that Zuid is where 340 products opened without a price.",
                    "Rows written as solutions: “a second door”, “40 chargers”, “same as Zuid”. What is each one for?")
rq_problem.row([("“2nd cold-room door”", None, "paper"), ("“40 chargers”", None, "paper"), ("“same as Zuid”", None, "pink")], y=30, h=64, size=17)
rq_problem.note(380, 140, "each row is an answer. What was the question?", "red", size=19)
rq_problem.note(380, 182, "Tomás: “Zuid is where 340 products had no price”", "pen", size=17)
rq_problem.note(380, 222, "solutions hide the need, and the cheaper way to meet it", "pen", size=16)

rq_analogy = Doodle(760, 240, "Doodle of a doctor. A patient comes in asking for a particular medicine. The doctor asks about the symptoms first: what hurts, since when, what makes it worse. The medicine the patient named may be right; often a different one is better. The prescription follows the diagnosis, never the request.",
                    "A patient asks for a pill. The doctor asks about the symptoms first.")
rq_analogy.row([("“I need pill X”", "the request", "paper"), ("what hurts?", "the symptoms", "y"), ("the diagnosis", "the real need", "blue"), ("the prescription", "maybe not X", "green")], y=50, h=90, gap=34, size=16, subsize=13, arrows=True)
rq_analogy.note(380, 200, "the prescription follows the diagnosis", "pen", size=19)

rq_how = Doodle(760, 400, "How Rotterdam's requirements were drawn out and traced, February 2026. Four sources: Sanne walks the Friday evening peak at Noord, a ninety-minute workshop with Tomás, Joost's operations lead, Sam and Lena, Grace's prototype test with three pickers, and Zuid's opening. 96 requirements come out. Each is traced: need, requirement, must-have, how it is checked, who accepts it. Example: forty e-bikes fully charged by 07:30 from overnight charging leads to a three-phase supply and must-have F-09, checked by charging ten bikes overnight, accepted by Joost.",
                "Four ways of asking, 96 requirements, and every must-have traced back to a need and forward to a check.")
rq_how.row([("walk the peak", "Noord, Fri 17:30", "y"), ("workshop", "90 min, 12 Feb", "y"), ("prototype test", "Grace, 3 pickers", "y"), ("Zuid's opening", "what went wrong", "y")], y=14, h=76, size=16, subsize=13)
rq_how.box(220, 110, 320, 56, "96 requirements", "blue", size=20)
rq_how.row([("need", "bikes at 07:30", "paper"), ("requirement", "40 charged", "paper"), ("must-have", "F-09 chargers", "green"), ("check", "10-bike test", "paper"), ("accepts", "Joost", "paper")],
           y=200, h=90, gap=34, size=15, subsize=12, arrows=True)
rq_how.note(380, 330, "71 must-haves, each traced to at least one requirement", "pen", size=17)
rq_how.note(380, 362, "18 kept as “helps” · 7 rejected or duplicates", size=15)

REQUIREMENTS = dict(
    slug="requirements",
    kicker="a.k.a. “eliciting and analysing requirements”",
    tldr="A <b>requirement</b> is a condition the result must meet: what it must do, how well, under which rules. People rarely state requirements; they state <b>solutions</b> (“a second door”) or comparisons (“same as Zuid”). <b>Eliciting</b> means drawing out the need behind each: watch the work, ask about real moments, test prototypes, read what went wrong last time. <b>Analysing</b> means sorting, removing duplicates and conflicts, and <b>tracing</b> each one to something you'll deliver and a check that proves it.",
    chips=[("Family", "what, exactly?"), ("Lives in", "a requirements list with a trace to each must-have"), ("Pairs with", "customer interviews, prototype testing, the scope statement")],
    pmbok=dict(covers="drawing out, sorting and tracing requirements; business, stakeholder, solution and transition requirements",
               domains=["scope", "stakeholders"], processes=["Elicit and Analyze Requirements"],
               principles=["Focus on value", "Embed quality into processes and deliverables"], focus=["planning"],
               older="6th: “Collect Requirements” (5.2), the requirements traceability matrix. 7th: requirements under the Planning domain."),
    problem_side="Larder, 11–12 February 2026",
    problem="""  <p class="lead">Joost's spreadsheet is full of <b>answers</b>. “A second cold-room door.” “Forty chargers.” “Shelving the same as Zuid.” One row reads, in full, <b>“same as Zuid”</b>. Tomás laughs: Zuid is where 340 products opened without a price. <span class="hl-pink">Each row is a solution somebody already chose. Nobody wrote down what it was for</span>, so nobody can tell whether it's the right one, or whether a cheaper one would do.</p>
  <ul>
    <li>Solutions hide the need behind them.</li>
    <li>“Same as last time” copies the mistakes too.</li>
    <li>Without a need, there's no way to check the result.</li>
  </ul>""",
    problem_figs=[rq_problem],
    meanwhile=[("product-1", "prototype-testing", "Grace's prototype test with 6 customers and 3 pickers (13–22 January) found the picker-side needs: glove-friendly buttons, answers applied at packing.",
                "Sanne's requirements workshop of 12 February took the picker-side needs from Grace's test instead of asking the same pickers again.")],
    analogy_side="the doctor's first questions",
    analogy="""  <p>A patient walks in and asks for a <b>particular medicine</b>. A good doctor doesn't write the prescription. They ask about the <b>symptoms</b>: what hurts, since when, what makes it worse. Sometimes the medicine the patient named is right. Often a different one is better, or cheaper, or safer. The prescription follows the <b>diagnosis</b>, never the request.</p>""",
    analogy_figs=[rq_analogy],
    map=[("“I need pill X”", "“We need a second cold-room door”"),
         ("Asking about symptoms", "Walking the Friday peak; asking what goes wrong"),
         ("The diagnosis", "“No more than two pickers waiting at the cold room at peak”"),
         ("A different prescription", "A wider door and a layout change, now; a second door deferred"),
         ("The patient's file", "Zuid's opening: what went wrong last time")],
    how_side="four ways of asking, then trace every need",
    how="""  <p>Sanne uses four sources. She <b>walks the Friday peak</b> at Noord (17:30–19:00) with Tomás and watches where pickers wait. She runs a <b>90-minute workshop</b> on 12 February with Tomás, Joost's operations lead, Sam and Lena, asking about real moments: “tell me about the last time a shift went wrong.” She takes the picker-side findings from <b>Grace's prototype test</b>. And she reads <b>Zuid's opening</b> as a list of requirements nobody wrote. Out come <b>96 requirements</b>. Each “solution” row is turned back into its need: “a second door” becomes <i>no more than two pickers waiting at the cold room at peak</i>, met for launch by a wider door and a layout change. Then each must-have is <b>traced</b>: need, requirement, must-have, check, who accepts.</p>""",
    how_figs=[rq_how],
    steps=[("Find everyone who will live with the result", "Not only those who asked."),
           ("Watch the work at its worst moment", "A peak, a busy shift."),
           ("Ask about real past moments", "“Tell me about the last time…”"),
           ("Turn each solution back into its need", "“What is it for?”"),
           ("Sort: must-have, helps, out", "Remove duplicates and conflicts."),
           ("Trace each need to a deliverable and a check", "And name who accepts it.")],
    vocab=[("Requirement", "A condition or capability the result must meet."),
           ("Elicitation", "Drawing requirements out of people and evidence."),
           ("Business requirement", "Why the organisation wants it: 500 orders a day."),
           ("Stakeholder requirement", "What a group of people needs: pickers reach chilled goods fast."),
           ("Non-functional requirement", "How well: speed, capacity, safety, temperature."),
           ("Transition requirement", "What's needed to switch over: training, data."),
           ("Traceability matrix", "A table linking each requirement to its deliverable, check and owner.")],
    code=dict(file="rotterdam/17-requirements.md", note="extract · 96 requirements, workshop of 12 February 2026", plain=True, src="""
# ROTTERDAM · REQUIREMENTS (extract) → traced to must-haves

ID    NEED (from)                    REQUIREMENT                          MUST-HAVE  CHECK                ACCEPTS
R-08  pickers don't queue for        ≤ 2 pickers waiting at the cold      F-07       timed at rehearsal   Tomás
      chilled goods (Noord peak)     room at the Friday peak                         peak
R-12  chilled stays chilled (law)    cold room 2–4 °C; alarm to Tomás     F-06       48 h test at G1      Joost
                                     if > 5 °C for 15 min
R-23  every product has a price      100 % of products have price + VAT   P-03       nightly script = 0   Eli
      (Zuid: 340 had none)           before stocking starts
R-31  couriers start at 07:30        40 e-bikes fully charged by 07:30    F-09       10 bikes charged     Joost
                                     → three-phase supply                            overnight
R-44  pickers wear gloves            buttons ≥ 12 mm on handhelds         A-04       picker test          Grace
      (Grace's prototype test)
R-57  food is safe to sell (law)     store registered with the food-      L-02       letter on file       Lena
                                     safety authority before 1st delivery

"a second cold-room door" (Joost) → is a solution for R-08 → met by a wider door + layout;
                                   second door deferred (see change C-06)
TOTAL  96 requirements → 71 must-haves (each traced) · 18 "helps" · 7 rejected / duplicates
"""),
    tools="tools: a peak shift, a 90-minute workshop, last time's mistakes, and a five-column table.",
    dial=[("Light", "a small, familiar change", ["Ask “what is it for?” of every request.", "A short list of needs.", "A check for each."]),
          ("Standard", "Rotterdam", ["Observation, a workshop, existing findings.", "Solutions turned back into needs.", "A trace from need to check and owner."]),
          ("Heavy", "regulated or contracted work", ["A business analyst and formal elicitation.", "A full traceability matrix under change control.", "Requirements reviewed and signed per group."])],
    baseline="Each line compares <b>a list of requested solutions</b> to <b>needs drawn out from the people affected, each traced to a must-have, a check and an owner</b>.",
    ratings=[(2, 5, "Every must-have answers a need."),
             (3, 4, "Fewer late discoveries of missing things."),
             (2, 4, "Last time's mistakes become requirements."),
             (2, 4, "Anyone can see why each must-have exists."),
             (3, 4, "Tomás and Lena see their needs in the plan."),
             (3, 4, "The people doing the work were asked."),
             (3, 4, "A need can be met in a cheaper way."),
             (2, 5, "Each requirement has its check."),
             (4, 3, "A workshop, a shift and a table.")],
    pitfalls=[("Collecting solutions", "“A second door.”", "ask what it's for."),
              ("“Same as last time”", "Copies the mistakes.", "read last time as a list of requirements."),
              ("Asking only the sponsor", "The people who work there are missed.", "watch the work; ask them."),
              ("No check", "Nobody can prove it's met.", "write the check next to each requirement.")],
    use=["Before the scope statement.", "When requests arrive as solutions.", "When a similar project went wrong.", "When many groups will live with the result."],
    skip=["The needs are already known and written, and nothing has changed."],
    related=["<b>Customer interviews</b> (Grace, vol. 1)", "<b>Prototype testing with users</b> (Grace, vol. 1)", "<b>What's In, and What's Out?</b> (next note)", "<b>Quality attribute scenarios</b> (Ana, vol. 1)"],
    quiz=[("Need or solution: “a second cold-room door”?", "A solution. The need: no more than two pickers waiting at the cold room at peak."),
          ("Name two ways Sanne drew requirements out.", "Watching the Friday peak at Noord; a workshop about real past moments (also: Grace's prototype test, Zuid's opening)."),
          ("What does a trace link?", "Need, requirement, must-have, check and who accepts it."),
          ("Priya asks for “a Rotterdam landing page like Amsterdam's”. What does Sanne ask?", "What it is for. If the need is “people in Rotterdam can join the waitlist”, the existing page with a city field may meet it."),
          ("A requirement has no check. What's wrong?", "Nobody can prove it's met, so it can't be accepted. Write the check, or it isn't a requirement yet.")],
    try_it="Take five items from your project's list. For each, ask “what is it for?” and write the need in one sentence. Then write how you'd check it's met. Did any item turn out to be a solution with a cheaper alternative?",
    remember="Ask about the <span class=\"hl\">symptoms</span> before you write the <span class=\"hl\">prescription</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Scope domain, eliciting and analysing requirements.",
             "Project Management Institute, <i>Business Analysis for Practitioners: A Practice Guide</i> (2015).",
             "Karl Wiegers and Joy Beatty, <i>Software Requirements</i> (3rd ed., 2013).",
             "Ellen Gottesdiener, <i>Requirements by Collaboration</i> (2002)."],
)

# ------------------------------------------------------------------ 03 What's In, and What's Out?
ss_problem = Doodle(760, 250, "Doodle of 16 February 2026. Priya and Joost discover they have been planning two different launches. Priya assumed a Rotterdam landing page and a promo code were part of it. Joost assumed hypercare after opening was his store team's job, not the project's. Each was sure, and neither had said it.",
                    "Two people, two launches: each sure of what was in, neither had said so.")
ss_problem.box(20, 30, 330, 100, "Priya's launch", "blue", sub="+ landing page + promo code", size=19, subsize=14)
ss_problem.box(410, 30, 330, 100, "Joost's launch", "y", sub="ends at opening; hypercare is ops", size=19, subsize=14)
ss_problem.note(380, 176, "both sure · neither written", "red", size=20)
ss_problem.note(380, 214, "the charter is due in three days", "pen", size=18)

ss_analogy = Doodle(760, 240, "Doodle of a quote from a decorator. It lists the rooms to be painted, the colour and the number of coats, how the client will check it, and a line at the bottom: not included, the ceilings and the window frames. That last line prevents most arguments.",
                    "A decorator's quote: the rooms, how you'll check them, and the line that says “not included”.")
ss_analogy.row([("rooms", "what is delivered", "blue"), ("two coats, no drips", "how it's checked", "y"), ("not included", "ceilings, frames", "pink")], y=50, h=90, size=17, subsize=14)
ss_analogy.note(380, 196, "the last line prevents most arguments", "pen", size=19)

ss_how = Doodle(760, 400, "Rotterdam's scope statement, 16 February 2026, in six parts. What the result is: a dark store serving three delivery zones, live in the platform and apps. Eight deliverable groups. For each, how it will be accepted and by whom. What is out: new app features, Larder for Business in Rotterdam, changes to Amsterdam, a launch event, Sunday opening as an open question. Constraints: 27 April, 380 thousand euros, four hires, no deliveries before 07:30. Assumptions, each with an owner who checks it: StockPilot copes with a second city, forty staff can be hired by 30 March, suppliers deliver as in Amsterdam.",
                "Six parts on one page. The “out” and “assumptions” boxes do the most work.")
parts = [("the result", "a dark store, 3 zones, live", "blue"), ("8 deliverables", "fit-out → hypercare", "blue"), ("acceptance", "a check + an owner each", "green"),
         ("out", "features · B2B · Amsterdam", "pink"), ("constraints", "27 Apr · €380k · 4 hires", "y"), ("assumptions", "each with a checker", "y")]
for i, (t, s, f) in enumerate(parts):
    r, c = divmod(i, 3)
    ss_how.box(14 + c * 248, 14 + r * 130, 236, 112, t, f, sub=s, size=20, subsize=13)
ss_how.box(120, 290, 520, 70, "→ the charter's IN / OUT, 19 Feb", "paper", sub="hypercare IN · landing page OUT (the existing page has a city field)", size=17, subsize=13)

SCOPE_STATEMENT = dict(
    slug="scope-statement",
    kicker="a.k.a. “defining scope”: the scope statement",
    tldr="A <b>scope statement</b> says, on one page, what the project will deliver: the <b>result</b> in a few lines, the <b>deliverables</b>, how each will be <b>accepted</b> and by whom, what is deliberately <b>out</b>, the <b>constraints</b>, and the <b>assumptions</b> it rests on (each with someone who checks it). It turns requirements into a promise. Its most useful lines are the ones that say what <b>won't</b> be done.",
    chips=[("Family", "what, exactly?"), ("Lives in", "one page; its in / out lines go into the charter"), ("Pairs with", "requirements, the charter, the WBS")],
    pmbok=dict(covers="product scope and project scope; deliverables, acceptance criteria, exclusions, constraints and assumptions",
               domains=["scope"], processes=["Define Scope"], principles=["Focus on value"], focus=["planning"],
               older="6th: “Define Scope” (5.3), the project scope statement. 7th: scope under the Planning and Delivery domains."),
    problem_side="Larder, 16 February 2026",
    problem="""  <p class="lead">Three days before the charter, a short meeting about the waitlist goes wrong. <b>Priya</b> has been planning a Rotterdam landing page and a promo code: “it's a launch.” <b>Joost</b> has been planning for the project to end on opening day: hypercare is his store team's job. <span class="hl-pink">Each is sure. Neither had said it.</span> Between them, the launch is either two features bigger or two weeks shorter than Sanne's plan.</p>
  <ul>
    <li>Everyone carries a picture of the scope in their head.</li>
    <li>The edges (what's out, when it ends) are where pictures differ.</li>
    <li>Assumptions nobody checks become surprises.</li>
  </ul>""",
    problem_figs=[ss_problem],
    analogy_side="the decorator's quote",
    analogy="""  <p>A good <b>decorator's quote</b> lists the rooms, the colour and the number of coats, and how you'll check the work: “two coats, no drips, edges clean.” At the bottom is one more line: <b>“not included: ceilings, window frames.”</b> That last line costs nothing to write, and prevents most of the arguments decorators and clients have.</p>""",
    analogy_figs=[ss_analogy],
    map=[("The rooms", "Eight deliverable groups, from fit-out to hypercare"),
         ("“Two coats, no drips”", "Acceptance criteria and who accepts"),
         ("“Not included”", "New features, Larder for Business, Amsterdam, a launch event"),
         ("The client's assumption: “ceilings too”", "Priya's landing page; Joost's “ends at opening”"),
         ("The signed quote", "The charter's IN and OUT, 19 February")],
    how_side="one page, six parts; settle the edges",
    how="""  <p>Sanne writes the <b>scope statement</b> in six parts: the result (a dark store serving three delivery zones, live in the platform and apps), <b>eight deliverable groups</b>, <b>acceptance</b> for each, what is <b>out</b>, the <b>constraints</b>, and the <b>assumptions</b>, each with someone who checks it. The edges get settled in the room. <b>Hypercare is in</b>: two weeks, then a handover, because Joost's team can't absorb a new store's first days alone. The <b>landing page is out</b>: the existing waitlist page gets a city field, which meets the need (Priya's promo code stays open and comes back later). Sunday opening is written as an <b>open question</b> with an owner. Three days later the in and out lines go into the charter word for word.</p>""",
    how_figs=[ss_how],
    steps=[("Describe the result in a few lines", "What exists when you're done."),
           ("List the deliverables", "Groups, not tasks."),
           ("Write how each is accepted, and by whom", "From the requirements' checks."),
           ("Write what is out", "Especially what people might assume is in."),
           ("List constraints and assumptions", "Each assumption gets a checker."),
           ("Settle the edges with the people who disagree", "Then copy in / out into the charter.")],
    vocab=[("Scope statement", "A description of the project's deliverables, acceptance, exclusions, constraints and assumptions."),
           ("Product scope", "The features and qualities of the result."),
           ("Project scope", "The work needed to deliver it, including training and hypercare."),
           ("Acceptance criteria", "Conditions a deliverable must meet before it is accepted."),
           ("Exclusion", "Something explicitly not part of the project."),
           ("Assumption", "Something treated as true for planning, to be checked.")],
    code=dict(file="rotterdam/18-scope-statement.md", note="16 February 2026 · in / out copied into the charter of 19 February", plain=True, src="""
# ROTTERDAM · SCOPE STATEMENT

RESULT       a dark store in Rotterdam serving three delivery zones (RTM-1 to RTM-3),
             express and slots, live in the platform and the apps, from 27 April 2026
DELIVERABLES 1 store fitted out   2 staff hired and trained   3 store stocked
             4 city set up in the platform   5 Rotterdam in the apps
             6 payments and legal in place   7 launch marketing   8 two weeks of hypercare
ACCEPTANCE   1 Joost, at Gate 1 (snag list)   2 Tomás: 20 practice orders each
             3 Tomás, at Gate 2   4 Eli: nightly check = 0 errors   5 Grace, at Gate 3
             6 Lena: registrations on file   7 Priya   8 exit criteria, Gate 5
OUT          new app features for Rotterdam · Larder for Business in Rotterdam ·
             changes to Amsterdam · a launch event · a separate Rotterdam landing page
             (the waitlist page gets a city field)
OPEN         Sunday opening at launch → Joost, by 27 Feb
CONSTRAINTS  opens 27 April (lease) · €380k · max 4 new hires · no deliveries before 07:30
ASSUMPTIONS                                                         CHECKED BY
             StockPilot syncs a second city within its limits       Ana, by 1 Mar
             ~40 pickers and couriers can be hired by 30 March      Joost, weekly
             suppliers deliver to Rotterdam on Amsterdam's terms    Tomás, by 13 Mar
"""),
    tools="tools: one page, the requirements list, and the two people who disagree about the edges.",
    dial=[("Light", "a small job", ["Three lines: what, how it's checked, what's out.", "Agreed in a message.", "Nothing more."]),
          ("Standard", "Rotterdam", ["One page, six parts.", "Assumptions with checkers.", "In / out copied into the charter."]),
          ("Heavy", "contracts, tenders", ["A detailed statement of work.", "Acceptance criteria per deliverable in the contract.", "Exclusions reviewed by legal."])],
    baseline="Each line compares <b>scope carried in people's heads</b> to <b>a one-page scope statement with acceptance, exclusions and checked assumptions</b>.",
    ratings=[(3, 4, "What's in is tied to the benefit."),
             (2, 4, "The edges stop moving."),
             (2, 4, "Assumptions have someone checking them."),
             (2, 5, "One page everyone can read."),
             (2, 4, "Priya and Joost agree the same launch."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral: the edges are now harder to move."),
             (3, 4, "Every deliverable has its acceptance."),
             (4, 4, "One page.")],
    pitfalls=[("No “out”", "People assume the ceilings too.", "write what is excluded."),
              ("Assumptions with no owner", "Nobody checks; they turn into issues.", "a checker and a date each."),
              ("Tasks instead of deliverables", "A to-do list, not a result.", "name what exists at the end."),
              ("Written alone", "The disagreements surface in April.", "settle the edges with those who differ.")],
    use=["Before the charter or the contract.", "When two people describe the project differently.", "Before breaking the work down.", "When suppliers quote against it."],
    skip=["Tiny work whose edges nobody could disagree about."],
    related=["<b>What Do They Actually Need?</b> (previous note)", "<b>Should This Project Exist?</b> (vol. 2)", "<b>How Do We Break It Down?</b> (next note)", "<b>Constraints vs assumptions</b> (Ana, vol. 1)"],
    quiz=[("Name the six parts.", "Result, deliverables, acceptance, out, constraints, assumptions."),
          ("Product scope or project scope: two weeks of hypercare?", "Project scope: it's work the project does, not a feature of the store."),
          ("Why give each assumption a checker?", "Unchecked assumptions become issues. StockPilot's limit is one Ana already found."),
          ("On 2 March Ana reports that StockPilot can sync a second city, but not a third. What does Sanne do with the assumption?", "Mark it checked and true for Rotterdam, and pass the limit to the programme for Utrecht."),
          ("Priya asks again for a Rotterdam landing page on 5 March. What does Sanne point to?", "The OUT line, and the need it was meant for (the waitlist page's city field). A real change would go through the triggers.")],
    try_it="Write your project's scope on one page in six parts. Spend most of the time on two boxes: what is out, and what you are assuming. Give each assumption a name and a date.",
    remember="The line that says <span class=\"hl\">“not included”</span> prevents most of the <span class=\"hl\">arguments</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Scope domain, defining scope.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 5.3 Define Scope.",
             "Project Management Institute, <i>Practice Standard for Work Breakdown Structures</i> (3rd ed., 2019): the scope statement as input."],
)

# ------------------------------------------------------------------ 04 How Do We Break It Down?
wb_problem = Doodle(760, 250, "Doodle of 20 March 2026, a month after the breakdown was made. Eli asks who is ordering the store's internet line. It was in nobody's piece of the plan. Going back, Sanne finds the builder's quote said: data cabling to the comms cabinet; connectivity by client. By client meant Larder. Nobody turned it into a piece of work.",
                    "“Connectivity by client”: one line in the builder's quote that never became anybody's work.")
wb_problem.box(20, 30, 330, 100, "builder's quote", "paper", sub="“…connectivity by client”", size=19, subsize=15)
wb_problem.box(410, 30, 330, 100, "Larder's breakdown", "blue", sub="cabling ✓ · Wi-Fi ✓ · line ✗", size=19, subsize=15)
wb_problem.arrow(352, 80, 408, 80, color="red")
wb_problem.note(380, 176, "“by client” = Larder = nobody", "red", size=20)
wb_problem.note(380, 214, "the 100 % rule, broken one level down", "pen", size=18)

wb_analogy = Doodle(760, 250, "Doodle of a recipe for a three-course dinner broken down: the dinner into starter, main and dessert; the main into the roast, the potatoes and the gravy; each of those into something one cook can make and taste. If the parts add up to less than the dinner, someone discovers at eight o'clock that nobody made the gravy.",
                    "A dinner, broken down until each dish is one cook's job. The parts must add up to the whole dinner.")
wb_analogy.box(280, 14, 200, 50, "the dinner", "y", size=18)
wb_analogy.row([("starter", None, "blue"), ("main", None, "blue"), ("dessert", None, "blue")], x=100, y=96, h=50, w=170, gap=25, size=17)
wb_analogy.row([("roast", None, "paper"), ("potatoes", None, "paper"), ("gravy", None, "pink")], x=220, y=178, h=50, w=100, gap=10, size=15)
for x in (185, 380, 575):
    wb_analogy.line(f"M380 64 L{x} 96", thin=True)
for x in (270, 380, 490):
    wb_analogy.line(f"M380 146 L{x} 178", thin=True)
wb_analogy.note(640, 216, "who made the gravy?", "red", size=17)

wb_how = Doodle(760, 420, "Rotterdam's work breakdown structure, first drawn on 17 February 2026 and baselined on 13 March. Level 1: the Rotterdam launch. Level 2: nine branches with their must-haves: project management (none, about six percent of the effort), store fit-out 16, people 9, stock and suppliers 10, platform set-up 12, apps 6, payments and legal 9, launch marketing 5, opening and hypercare 4. That is 71. Level 3 under fit-out: building works, cold room and fridges, shelving, e-bike charging, store systems online. The last one was missing a work package: the internet line.",
                "Nine branches, 71 must-haves. One branch opened up: the gap was one level further down.", exact=True)
wb_how.box(260, 10, 240, 48, "1 Rotterdam launch", "y", size=18)
br = [("PM", "0"), ("fit-out", "16"), ("people", "9"), ("stock", "10"), ("platform", "12"), ("apps", "6"), ("pay+legal", "9"), ("marketing", "5"), ("hypercare", "4")]
for i, (t, n) in enumerate(br):
    x = 8 + i * 83
    wb_how.box(x, 92, 78, 66, t, "pink" if t == "fit-out" else "blue", sub=n, size=12, subsize=17)
    wb_how.line(f"M380 58 L{x + 39} 92", thin=True)
l3 = [("building works", "builder"), ("cold room", "supplier"), ("shelving", "catalogue"), ("e-bike charging", "builder"), ("systems online", "Eli")]
for i, (t, s) in enumerate(l3):
    x = 14 + i * 148
    wb_how.box(x, 206, 140, 60, t, "pink" if t == "systems online" else "paper", sub=s, size=12, subsize=12)
    wb_how.line(f"M90 158 L{x + 70} 206", thin=True)
for i, (t, f) in enumerate([("cabling", "green"), ("Wi-Fi", "green"), ("devices", "green"), ("internet line", "pink")]):
    wb_how.box(330 + i * 106, 306, 100, 48, t, f, size=11, dash=(t == "internet line"))
    wb_how.line(f"M676 266 L{380 + i * 106} 306", thin=True)
wb_how.note(200, 330, "71 must-haves in total", "pen", size=17)
wb_how.note(560, 386, "the missing work package (found 20 March)", "red", size=16)

wb_deep1 = Doodle(760, 260, "Two ways to break down the same thing. On the left, by activity: plan, buy, build, test. Every activity touches every deliverable, so nobody owns a result. On the right, by deliverable: cold room, shelving, chargers, systems online. Each has one owner and can be checked. Nouns, not verbs.",
                  "Break down by what is delivered (nouns), not by what is done (verbs). Each noun can have an owner and a check.")
wb_deep1.box(14, 14, 350, 52, "by activity (verbs)", "paper", size=18)
wb_deep1.row([("plan", None, "paper"), ("buy", None, "paper"), ("build", None, "paper"), ("test", None, "paper")], x=14, y=86, h=50, w=80, gap=10, size=15)
wb_deep1.note(189, 172, "touches everything; owns nothing", "red", size=16)
wb_deep1.box(396, 14, 350, 52, "by deliverable (nouns)", "green", size=18)
wb_deep1.row([("cold room", None, "green"), ("shelving", None, "green"), ("chargers", None, "green"), ("online", None, "green")], x=396, y=86, h=50, w=82, gap=7, size=12)
wb_deep1.note(571, 172, "one owner and one check each", "green", size=16)
wb_deep1.note(380, 228, "stop breaking down when a piece has an owner, an estimate and a check", "pen", size=16)

wb_deep2 = Doodle(760, 250, "The 100 percent rule and three checks for it. The children of every element must add up to all of the parent, no more and no less. Check one: against the charter's in-list, top down. Check two: walk the result as if it were finished, a day in the life of the store. Check three: read every supplier quote for the words by client, by others, excluded. Rotterdam's breakdown passed the first two and skipped the third.",
                  "Children must add up to 100 % of the parent. Three checks, and Rotterdam skipped the third.")
wb_deep2.row([("1 the charter", "every IN line has a branch", "green"), ("2 walk it", "a day in the finished store", "green"), ("3 the small print", "“by client”, “by others”", "pink")], y=40, h=100, size=18, subsize=13)
wb_deep2.note(132, 176, "done 17 Feb", "green", size=17)
wb_deep2.note(380, 176, "done 17 Feb", "green", size=17)
wb_deep2.note(628, 176, "skipped", "red", size=17)
wb_deep2.note(380, 224, "a walk-through would only catch it if someone tried to place an order", "pen", size=16)

WBS = dict(
    slug="work-breakdown-structure",
    kicker="a.k.a. “developing the scope structure”: the work breakdown structure (WBS)",
    tldr="A <b>work breakdown structure</b> splits the whole result into smaller <b>deliverables</b>, level by level, until each piece (a <b>work package</b>) can be owned, estimated and checked. It is a tree of <b>nouns</b>, not a list of tasks. Its one hard rule: the children of every element must add up to <b>100 % of the parent</b>, nothing more and nothing less. Most forgotten work is a hole in that rule, often one level further down than anyone looked.",
    chips=[("Family", "what, exactly?"), ("Lives in", "a tree on one page, plus a short dictionary entry per work package"), ("Pairs with", "story mapping, the scope statement, estimates")],
    pmbok=dict(covers="breaking the scope into deliverables and work packages; the WBS, the 100 % rule, the WBS dictionary; the scope baseline",
               domains=["scope"], processes=["Develop Scope Structure"], principles=["Adopt a holistic view"], focus=["planning"],
               older="6th: “Create WBS” (5.4); the scope baseline = scope statement + WBS + WBS dictionary. 7th: the WBS as an artefact in the Planning domain."),
    problem_side="Larder, 17 February and 20 March 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. On 17 February she breaks the launch down by workstream: nine branches, 71 must-haves, each with an owner. It is checked against the charter and against Joost's rows. On <b>20 March</b> Eli asks who is ordering the store's internet line. Sanne goes back to the builder's quote and finds the sentence: <b>“data cabling to the comms cabinet; connectivity by client.”</b> <span class="hl-pink">“By client” meant Larder. Nobody turned it into a piece of work.</span></p>
  <ul>
    <li>The must-have “store systems online” existed; one of its parts didn't.</li>
    <li>The gap sat between the builder's work and Eli's.</li>
    <li>The checks looked down one level, not two.</li>
  </ul>""",
    problem_figs=[wb_problem],
    meanwhile=[("product-3", "story-mapping", "Grace's story map of 16 February broke the approvals work into a backbone and 17 stories; it is the app branch's breakdown.",
                "the next day Sanne used Grace's story map as the app branch (1.5) of the Rotterdam WBS, instead of breaking the app down a second time.")],
    analogy_side="a dinner broken into dishes",
    analogy="""  <p>A <b>three-course dinner</b> breaks down into a starter, a main and a dessert; the main into the roast, the potatoes and the <b>gravy</b>; each of those into something one cook can make and taste. The rule is simple: the parts must add up to the <b>whole dinner</b>. If they add up to slightly less, someone finds out at eight o'clock that nobody made the gravy, and everyone assumed somebody had.</p>""",
    analogy_figs=[wb_analogy],
    map=[("The dinner", "The Rotterdam launch"),
         ("Starter, main, dessert", "Nine branches: fit-out, people, stock, platform…"),
         ("One cook's dish", "A work package: one owner, an estimate, a check"),
         ("The gravy", "The internet line, inside “store systems online”"),
         ("“I thought you were making it”", "“Connectivity by client”")],
    how_side="nouns, level by level, until each piece can be owned and checked",
    how="""  <p>On <b>17 February</b> Sanne and the leads draw the tree. Level 1: the launch. Level 2: <b>nine branches</b>, one per workstream, plus <b>project management</b> (no must-haves, about 6 % of the effort, but real work). Level 3: the deliverables in each branch. The leaves are the <b>71 must-haves</b>: fit-out 16, people 9, stock 10, platform 12, apps 6, payments and legal 9, marketing 5, opening and hypercare 4. The app branch is Grace's story map. Each work package gets a <b>dictionary</b> entry: what it is, owner, “done means”, estimate, what it waits for. The app branch is cut to 6 must-haves after Grace's session of 3 March, and the tree is baselined on 13 March. After 20 March, “store systems online” gets its missing child: <b>the internet line</b>, owner Eli.</p>""",
    how_figs=[wb_how],
    steps=[("Start from the scope statement's deliverables", "Level 2."),
           ("Break each into smaller deliverables", "Nouns, not verbs."),
           ("Stop when a piece has an owner, an estimate and a check", "That is a work package."),
           ("Check the 100 % rule at every level", "Charter, walk-through, suppliers' small print."),
           ("Write a dictionary entry per work package", "Five lines each."),
           ("Baseline it with the scope statement", "Then change it only on purpose.")],
    vocab=[("Work breakdown structure (WBS)", "A tree that splits the whole scope into smaller deliverables."),
           ("Work package", "The lowest level: owned, estimated, checkable."),
           ("100 % rule", "The children of each element add up to all of it: nothing more, nothing less."),
           ("WBS dictionary", "A short description of each work package: content, owner, done means, estimate."),
           ("Decomposition", "Breaking something into smaller parts."),
           ("Scope baseline", "The approved scope statement, WBS and dictionary.")],
    code=dict(file="rotterdam/19-wbs.md", note="first drawn 17 February · baselined 13 March · 1.1.5 corrected 23 March 2026", plain=True, src="""
# ROTTERDAM · WORK BREAKDOWN STRUCTURE (level 2, with must-haves)

1 ROTTERDAM LAUNCH                                                   71
  1.0 Project management (charter, plan, status, gates, closing)     -   ~6 % of effort
  1.1 Store fit-out                                                  16
      1.1.1 building works · 1.1.2 cold room + fridges · 1.1.3 shelving
      1.1.4 e-bike charging · 1.1.5 store systems online
  1.2 People (hired, trained, rostered)                               9
  1.3 Stock and suppliers                                            10
  1.4 Platform set-up (zones, prices, VAT, hours, slots)             12
  1.5 Apps (= Grace's story map; 6 Musts after 3 Mar)                 6
  1.6 Payments and legal                                              9
  1.7 Launch marketing                                                5
  1.8 Opening and hypercare                                           4

DICTIONARY · 1.1.5 Store systems online                              owner: Eli
  content     data cabling to the comms cabinet (builder) · Wi-Fi · 30 handhelds,
              4 label printers, 2 payment terminals set up
              + INTERNET LINE from the street (added 23 Mar; "connectivity by client")
  done means  an order picked, labelled and paid in the store, on the store's own line
  estimate    4 days (Eli) + 6 weeks' lead time for the line
  waits for   electrical second fix (1.1.1), handheld delivery (ordered 23 Feb)
"""),
    tools="tools: the scope statement, a wall, sticky notes in two colours (deliverables, work packages), and every supplier quote.",
    deep_dive=dict(
        side="decomposition, the 100 % rule, and the dictionary",
        intro="A WBS looks like the easiest thing in this book: draw a tree. The mistakes are in three places: breaking down by activity instead of by deliverable, stopping at the wrong depth, and trusting that the children add up to the parent. This chapter takes them in turn, with Rotterdam's missed line as the example.",
        parts=[
            ("Nouns, not verbs", """  <p>The commonest bad WBS is a list of phases: plan, buy, build, test. Every phase touches every deliverable, so nobody owns a <b>result</b>, and “build is 80 % done” means nothing. A WBS breaks down <b>what is delivered</b>: cold room, shelving, chargers, systems online. Each of those can have one owner and one check.</p>
  <p>How deep? Stop when a piece is a <b>work package</b>: one owner, an estimate someone believes, and a check that says it's done. A common rule of thumb is that a work package takes between a day and two weeks of effort. Larger, and it hides too much; smaller, and the tree becomes a task list. In an adaptive branch, the work packages are features or stories, and the lower levels are filled in sprint by sprint (rolling wave).</p>""", [wb_deep1]),
            ("The 100 % rule, and three ways to test it", """  <p>The rule: the children of every element must add up to <b>all</b> of the parent, including work nobody likes (project management, training, clean-up). A WBS that passes it at level 2 can still fail at level 4. Three checks catch most holes:</p>
  <ol class="steps">
    <li><b>Top down, against the charter.</b><p>Every IN line has a branch; no branch is OUT. Rotterdam passed.</p></li>
    <li><b>Walk the finished result.</b><p>A day in the life of the open store: a delivery arrives, a picker logs in, an order is paid. Rotterdam did this on paper; nobody imagined the handheld actually connecting.</p></li>
    <li><b>Read every supplier's small print.</b><p>“By client”, “by others”, “excluded”, “not in scope”: each phrase is work that someone must own. Rotterdam skipped this one. The builder had written it down; Larder had not read it as a work package.</p></li>
  </ol>""", [wb_deep2]),
            ("The dictionary: five lines per work package", """  <p>A tree shows the shape; the <b>dictionary</b> says what each leaf means. Five lines are enough: <b>content</b> (what's included, including from suppliers), <b>owner</b>, <b>done means</b>, <b>estimate</b>, <b>waits for</b>. Writing the content line is where small print gets read: 1.1.5's entry, written properly, would have had to say “internet line: …?” and someone would have asked.</p>
  <p>Together, the scope statement, the WBS and the dictionary are the <b>scope baseline</b>. Rotterdam's was approved on 13 March. The internet line was added on 23 March as a correction inside an existing must-have: the count stayed 71, the promise didn't change, only the plan for keeping it did.</p>""", []),
            ("WBS, story map, task list", """  <p>Three tools break work down, at different levels:</p>
  <ul>
    <li>The <b>WBS</b> breaks down the <b>whole project's result</b>. One per project.</li>
    <li>A <b>story map</b> breaks down <b>one product's</b> journey into features and stories: here, Grace's map is the app branch.</li>
    <li>A <b>task list</b> or sprint board breaks one work package into <b>activities</b> for this week. These are verbs, and they belong to the people doing the work.</li>
  </ul>
  <p>The WBS is the one that stops at the work package. Below that, the team decides how; the schedule (next collection) turns work packages into activities with durations and links.</p>""", []),
        ]),
    dial=[("Light", "a short job", ["A list of deliverables with owners.", "One question: “what's missing?”", "No dictionary."]),
          ("Standard", "Rotterdam", ["A tree of nine branches and 71 must-haves.", "Five-line dictionary entries.", "Three checks of the 100 % rule."]),
          ("Heavy", "large or contracted work", ["A coded WBS used for cost and schedule.", "A full dictionary under change control.", "WBS reviews with every supplier."])],
    baseline="Each line compares <b>a list of workstream tasks</b> to <b>a deliverable tree with work packages, a dictionary and the 100 % rule checked</b>.",
    ratings=[(3, 4, "Every leaf is a deliverable that serves the result."),
             (2, 4, "Estimates are made per work package."),
             (2, 4, "Holes are found by the three checks (when they're all done)."),
             (2, 5, "Who owns what is on one page."),
             (3, 4, "The steering group sees the whole result."),
             (3, 4, "Owners define their own work packages."),
             (3, 3, "Neutral: lower levels stay open in adaptive branches."),
             (3, 4, "Each work package has its check."),
             (3, 3, "A tree and five lines per leaf.")],
    pitfalls=[("Phases as branches", "Plan, build, test: nobody owns a result.", "break down by deliverable."),
              ("Too deep", "A task list in disguise.", "stop at owner + estimate + check."),
              ("The 100 % rule at level 2 only", "Holes hide lower down.", "three checks, at every level."),
              ("Supplier small print unread", "“By client” becomes nobody.", "turn every “by client” into a work package.")],
    use=["After the scope statement, before estimating.", "When work keeps falling between teams.", "With every supplier's quote in hand.", "When you need one view of the whole result."],
    skip=["A single deliverable with one owner."],
    related=["<b>Story mapping</b> (Grace, vol. 3)", "<b>What's In, and What's Out?</b> (previous note)", "<b>What's in the Way Right Now?</b> (vol. 2: the internet line as an issue)", "<b>How Long, Roughly?</b> (next note)"],
    quiz=[("What is a work package?", "The lowest level of the WBS: one owner, an estimate, a check."),
          ("State the 100 % rule.", "The children of each element add up to all of the parent: nothing more, nothing less."),
          ("Why nouns and not verbs?", "Deliverables can have one owner and a check; activities touch everything and own nothing."),
          ("A new supplier quote for the store's alarm says “monitoring contract by client”. What does Sanne do?", "Add a work package under the right branch, with an owner and a date, the day she reads it."),
          ("Adding the internet line on 23 March didn't change the 71. Why not?", "It was a missing part of an existing must-have (store systems online), not a new promise.")],
    try_it="Draw your project's WBS to level 3. Then run the third check: read every supplier quote and contract for “by client”, “by others” and “excluded”. Is each of those a work package with an owner?",
    remember="The parts must add up to the whole <span class=\"hl\">dinner</span>. Somebody has to make the <span class=\"hl\">gravy</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Scope domain, developing the scope structure.",
             "Project Management Institute, <i>Practice Standard for Work Breakdown Structures</i> (3rd ed., 2019).",
             "Gregory Haugan, <i>Effective Work Breakdown Structures</i> (2002).",
             "Jeff Patton, <i>User Story Mapping</i> (2014)."],
)

NOTES = [APPROACH, REQUIREMENTS, SCOPE_STATEMENT, WBS]
