# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 1 · The six principles.
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 1").
# The six principle names are from the PMBOK Guide, Eighth Edition. Every explanation is in our own words.

# ------------------------------------------------------------------ 05 See the Whole
hv_problem = Doodle(760, 260, "Doodle of 23 January 2026. Tomás suggests that the Rotterdam store opens from seven in the morning to eleven at night, not eight to ten like Amsterdam. It sounds like one small setting. Arrows show it touching five other things: delivery slots in the app, courier contracts, picker shifts, the lease's noise clause, and the launch adverts.",
                    "“Open an hour earlier and an hour later.” One small change, five other things moved.")
hv_problem.box(270, 90, 220, 76, "open 07:00–23:00", "y", sub="Tomás's idea", size=18, subsize=14)
for x, y, t in [(20, 14, "slots in the app"), (540, 14, "courier contracts"), (20, 196, "picker shifts"), (540, 196, "launch adverts"), (280, 204, "lease: noise clause")]:
    hv_problem.box(x, y, 200, 48, t, "paper", size=15)
hv_problem.arrow(272, 96, 222, 54)
hv_problem.arrow(488, 96, 538, 54)
hv_problem.arrow(272, 160, 222, 204)
hv_problem.arrow(488, 160, 538, 204)
hv_problem.arrow(380, 166, 380, 202, color="red")

hv_analogy = Doodle(760, 240, "Doodle of a mobile hanging over a child's bed: several shapes on strings, balanced on rods. Pull one shape and all the others move. You can't adjust one piece without watching the rest.",
                    "A mobile: touch one piece and every other piece moves.")
hv_analogy.line("M380 10 v30 M180 40 h400 M180 40 v40 M580 40 v40 M100 80 h160 M500 80 h160 M100 80 v50 M260 80 v70 M500 80 v60 M660 80 v80")
hv_analogy.circle(100, 152, 22, "y")
hv_analogy.box(236, 150, 48, 48, None, "blue")
hv_analogy.circle(500, 162, 22, "green")
hv_analogy.box(636, 160, 48, 48, None, "pink")
hv_analogy.note(380, 226, "pull one, watch them all", "pen", size=20)

hv_how = Doodle(760, 400, "Sanne's map of the whole Rotterdam launch, 23 January 2026. Seven workstreams in a ring: store fit-out, people, stock and suppliers, platform set-up, apps, payments and legal, launch marketing. Lines connect the ones that depend on each other. In the middle: the store opens on 27 April. Two items sit outside any workstream, marked in red: the food-safety registration and charging for the couriers' e-bikes.",
                "Seven workstreams, the links between them, and two things nobody owned.")
hv_how.circle(380, 190, 62, "y", label="27 April", sub="store opens")
ws = [(380, 40, "store fit-out"), (610, 100, "people"), (640, 250, "stock + suppliers"), (500, 350, "platform set-up"), (260, 350, "apps"), (120, 250, "payments + legal"), (150, 100, "marketing")]
for x, y, t in ws:
    hv_how.box(x - 90, y - 24, 180, 48, t, "blue", size=15)
for (x, y, _) in ws:
    hv_how.line(f"M{x} {y + (24 if y < 190 else -24)} L{380 + (x - 380) * 0.3:.0f} {190 + (y - 190) * 0.42:.0f}", thin=True)
hv_how.line("M470 40 Q560 50 600 76 M700 124 Q720 180 690 226 M410 350 h-60 M150 124 Q110 180 120 226", dash=True, thin=True)
hv_how.box(14, 14, 190, 44, "food-safety reg.", "pink", size=14, stroke="red")
hv_how.box(556, 14, 190, 44, "e-bike charging", "pink", size=14, stroke="red")

HOLISTIC = dict(
    slug="holistic-view",
    kicker="principle 1 of 6 · a.k.a. “adopt a holistic view”",
    tldr="A project is not a list of separate tasks. It is <b>one connected system</b>, sitting inside a bigger one (the company, the city, the market). Change one part and others move. A project manager's first habit is to <b>look at the whole</b> before fixing a part: draw the pieces, draw the links, and ask of every change, <b>“what else does this touch?”</b>",
    chips=[("Family", "the six principles"), ("Lives in", "one map on the wall, and a question at every change"), ("Pairs with", "the project environment, dependencies, the system context")],
    pmbok=dict(covers="principle: adopt a holistic view; systems thinking", principles=["Adopt a holistic view"],
               focus=["initiating", "planning", "executing", "monitoring", "closing"],
               older="6th: “project integration management”. 7th: the principle “recognize, evaluate and respond to system interactions”."),
    problem_side="Larder, 23 January 2026",
    problem="""  <p class="lead">Tomás has an idea for Rotterdam: open from <b>07:00 to 23:00</b>, not 08:00 to 22:00 like Amsterdam. Joost likes it. It looks like one setting. Sanne asks who else it touches, and the list grows: <span class="hl-pink">delivery slots in the app, courier contracts, picker shifts, a noise clause in the lease, and the adverts already at the printer.</span></p>
  <ul>
    <li>Each team sees its own tasks, not the links between them.</li>
    <li>A good local decision can cost another team two weeks.</li>
    <li>Some things sit between teams, so nobody owns them.</li>
  </ul>""",
    problem_figs=[hv_problem],
    analogy_side="a mobile over a child's bed",
    analogy="""  <p>A <b>mobile</b> is shapes on strings, balanced on rods. Pull one shape and the whole thing tilts. Someone who repairs mobiles never looks at one shape alone: they hold it up, <b>watch all of it</b>, and then touch one piece. A project behaves the same way, only the strings are harder to see.</p>""",
    analogy_figs=[hv_analogy],
    map=[("The shapes", "Seven workstreams: fit-out, people, stock, platform, apps, payments and legal, marketing"),
         ("The strings and rods", "Dependencies between them"),
         ("Pulling one shape", "Changing the opening hours"),
         ("The ceiling it hangs from", "Larder: its money, its promise of six cities"),
         ("Holding it up to look", "Sanne's map of the whole launch")],
    how_side="draw the whole, then ask “what else does this touch?”",
    how="""  <p>Sanne draws the launch as <b>seven workstreams</b> around one date, with a line wherever one depends on another. Then she walks Tomás's idea around the ring. Slots: a day's work for Ben. Courier contracts: Lena must check. The lease: no deliveries before 07:30. Adverts: already say 08:00. Decision, the same afternoon: <b>open 08:00 to 22:00 at launch, review after hypercare</b>. The drawing also shows two things <b>outside every workstream</b>: the food-safety registration and charging for forty e-bikes. Both get an owner that day.</p>""",
    how_figs=[hv_how],
    steps=[("List the workstreams", "Five to nine, not fifty."),
           ("Draw a line for every dependency", "Who waits for whom?"),
           ("Look for orphans", "Work that belongs to no workstream."),
           ("Draw what the project sits inside", "Company, customers, rules."),
           ("For every change, walk it round the map", "“What else does this touch?”"),
           ("Keep the map where people can see it", "Update it when links change.")],
    vocab=[("Holistic view", "Looking at the project as a whole and at how its parts affect each other."),
           ("System", "Parts that work together to produce a result none could produce alone."),
           ("Systems thinking", "Understanding causes and effects across the whole, including delays."),
           ("Dependency", "One piece of work that needs another to start or finish."),
           ("Workstream", "A group of related work, usually with one lead."),
           ("Integration", "Making the parts of a project work as one.")],
    code=dict(file="rotterdam/whole-map.md", note="Sanne, 23 January 2026", plain=True, src="""
# Rotterdam · the whole on a page                    lead      waits for

1 Store fit-out      builder, cold room, fridges     Joost     lease, permits
2 People             ~40 pickers and couriers        Joost     fit-out (training on site)
3 Stock + suppliers  2,500 products on shelves       Tomás     fit-out, StockPilot set-up
4 Platform set-up    zones, hours, prices, VAT       Eli, Ana  decisions from 1, 3
5 Apps               Rotterdam in the customer app   Ben, Dee  4
6 Payments + legal   provider, contracts, rules      Cho, Lena -
7 Launch marketing   waitlist, adverts               Priya     5 (dates, hours)

ORPHANS FOUND → OWNER
  food-safety registration      → Tomás, with Lena
  charging for 40 e-bikes       → Joost (part of fit-out)

A CHANGE WALKED ROUND THE MAP · opening hours 07:00–23:00
  touches 2, 4, 5, 6, 7 and the lease → not at launch; review after hypercare
"""),
    tools="tools: a whiteboard, sticky notes, and the question “what else does this touch?”.",
    dial=[("Light", "one team, one deliverable", ["Ask “what else does this touch?”", "A quick sketch.", "No upkeep."]),
          ("Standard", "Rotterdam: seven workstreams", ["A one-page map with leads.", "Every change walked round it.", "Updated monthly."]),
          ("Heavy", "many teams, vendors, countries", ["A dependency register.", "Interface agreements between teams.", "An integration lead."])],
    baseline="Each line compares <b>seven teams each managing their own task list</b> to <b>one map of the whole, and every change walked round it</b>.",
    ratings=[(3, 4, "Decisions serve the launch, not one team."),
             (2, 4, "Fewer knock-on delays."),
             (2, 5, "Two orphans found in January."),
             (2, 4, "Everyone sees the same picture."),
             (3, 4, "Joost sees why “small” changes aren't."),
             (3, 4, "Teams see who waits for them."),
             (3, 4, "A change is tested before it is made."),
             (3, 4, "Gaps between teams close."),
             (4, 3, "A map to keep up to date.")],
    pitfalls=[("Optimising one part", "A team's best choice hurts the whole.", "walk the change round the map."),
              ("A map with fifty boxes", "Nobody reads it.", "five to nine workstreams."),
              ("Drawn once", "Links change.", "update it monthly."),
              ("Only the inside", "Forgetting the lease, the neighbours, the market.", "draw what the project sits in.")],
    use=["More than one team is involved.", "A “small” change is proposed.", "Things fall between teams.", "At the start of every project."],
    skip=["Never. Scale it down to one question."],
    related=["<b>What Was Here Before Me?</b> (this volume)", "<b>System context</b> (Ana, vol. 1)", "<b>Dependencies across teams</b> (Grace, vol. 5)", "<b>What Must I Keep an Eye On?</b> (this volume)"],
    quiz=[("What question does a holistic view add to every change?", "“What else does this touch?”"),
          ("What is an orphan?", "Work that belongs to no workstream, so nobody owns it."),
          ("Priya wants to move the launch adverts a week earlier. What does Sanne do first?", "Walk it round the map: adverts depend on the app showing Rotterdam and on the final hours and zones. Then decide."),
          ("How many workstreams on the map?", "Five to nine. Seven for Rotterdam."),
          ("What did older editions call making the parts work as one?", "Integration management.")],
    try_it="Draw your project as five to nine workstreams around its goal. Add a line for each dependency. Circle anything that belongs to nobody. Then take the last change someone proposed and walk it round the map.",
    remember="Hold up the whole <span class=\"hl\">mobile</span> before you touch one piece.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the principle “adopt a holistic view”.",
             "Donella Meadows, <i>Thinking in Systems</i> (2008).",
             "Peter Senge, <i>The Fifth Discipline</i> (1990)."],
)

# ------------------------------------------------------------------ 06 Focus on Value
fv_problem = Doodle(760, 250, "Doodle of 26 January 2026. Femke asks Sanne in the corridor: are we on track for 27 April? Sanne answers with a question: on track for what? The spreadsheet shows 38 of 140 rows done, which is 27 percent. Nobody can say whether those 38 were the ones that matter.",
                    "“Are we on track?” “On track for what?” 38 of 140 rows done says nothing about the launch.")
fv_problem.box(20, 40, 300, 90, "38 of 140 done", "paper", sub="27 % “complete”", size=20, subsize=16)
fv_problem.box(440, 40, 300, 90, "on track for what?", "pink", size=20)
fv_problem.arrow(322, 85, 438, 85, color="red")
fv_problem.note(380, 190, "counting tasks is not measuring value", "red", size=20)

fv_analogy = Doodle(760, 240, "Doodle of packing for a hike. One hiker packs everything on a long list and can barely lift the bag. Another asks of each item: does this get me to the hut safely by dark? Water and a map go in; the third pair of shoes stays home.",
                    "Packing for a hike: every item answers one question, “does this get us to the hut by dark?”")
fv_analogy.box(20, 40, 320, 110, "pack the whole list", "paper", sub="heavy, slow, late", size=18, subsize=15)
fv_analogy.box(420, 40, 320, 110, "pack for the hut", "green", sub="water, map, coat", size=18, subsize=15)
fv_analogy.note(380, 200, "“does this get us to the hut by dark?”", "pen", size=20)

fv_how = Doodle(760, 360, "Sanne's value test on Joost's 140 rows, 26 January 2026. One question for every row: what happens to the benefit if we drop this? 71 rows are needed to open safely on 27 April. 47 rows help the benefit and are planned in order. 22 rows have no link to any benefit and are parked, such as tote bags and an app animation. The benefit on top: 500 orders a day by the end of May, 90 percent on time by the end of the summer, the next city in 8 weeks or less.",
                "One question per row: “what happens to the benefit if we drop this?”")
fv_how.box(14, 14, 732, 76, "500 orders/day · 90 % on time · next city ≤ 8 weeks", "green", sub="the benefit every row is tested against", size=17, subsize=14)
fv_how.box(110, 112, 540, 50, "“what happens to the benefit if we drop this?”", "y", size=16)
fv_how.row([("71 rows", "must have to open safely", "blue"), ("47 rows", "help the benefit: in order", "y"), ("22 rows", "no link: parked", "paper")], y=196, h=96, size=24, subsize=14)
fv_how.arrow(300, 162, 140, 194)
fv_how.arrow(380, 162, 380, 194)
fv_how.arrow(460, 162, 620, 194)
fv_how.note(628, 326, "tote bags · app animation", "red", size=16)

VALUE = dict(
    slug="focus-on-value",
    kicker="principle 2 of 6 · a.k.a. “focus on value”",
    tldr="A project exists to produce a <b>benefit</b>. Tasks, documents and even the deadline are only means. So steer by value: say what the benefit is, <b>test every piece of work against it</b>, and keep asking through the project whether it is still worth doing. “Done” means the benefit is on its way, not that the list is ticked.",
    chips=[("Family", "the six principles"), ("Lives in", "a benefit line on every plan and status"), ("Pairs with", "the value delivery system, outcomes over outputs, the business case")],
    pmbok=dict(covers="principle: focus on value", principles=["Focus on value"], focus=["initiating", "planning", "executing", "monitoring", "closing"],
               older="6th: the business case and benefits management plan. 7th: the principle “focus on value”."),
    problem_side="Larder, 26 January 2026",
    problem="""  <p class="lead">Femke stops Sanne in the corridor: “Are we on track for 27 April?” Sanne has Joost's spreadsheet: <b>38 of 140 rows</b> done. Is 27 % good? <span class="hl-pink">Nobody knows whether those 38 were the ones that matter.</span> And “on track” for what: a store with its doors open, or a city that orders?</p>
  <ul>
    <li>Progress is counted in tasks, not in value.</li>
    <li>Every row looks equally important.</li>
    <li>The date has become the goal.</li>
  </ul>""",
    problem_figs=[fv_problem],
    meanwhile=[("product-2", "strategy-on-a-page", "the same week, Grace writes the product strategy on one page: who Larder serves and what it won't do.",
                "the same week, Sanne tests every row of the Rotterdam plan against the benefit and parks 22 of them.")],
    analogy_side="packing for a hike",
    analogy="""  <p>Two people pack for a mountain hut. One works down a long list and can hardly lift the bag. The other asks of every item: <b>“does this get us to the hut safely by dark?”</b> Water, a map, a coat: yes. A third pair of shoes: no. The second hiker isn't lazy. They know what the walk is for.</p>""",
    analogy_figs=[fv_analogy],
    map=[("The hut by dark", "500 orders a day by the end of May; a city in 8 weeks or less"),
         ("The long packing list", "Joost's 140 rows"),
         ("“Does this get us there?”", "“What happens to the benefit if we drop this?”"),
         ("The third pair of shoes", "Branded tote bags, a launch-day animation"),
         ("Checking the sky on the way", "Asking “still worth it?” at every review")],
    how_side="one question, asked of every row",
    how="""  <p>Sanne and Joost go through all 140 rows in ninety minutes with one question: <b>what happens to the benefit if we drop this?</b> <b>71</b> rows are needed to open safely on 27 April. <b>47</b> help the benefit and are put in order. <b>22</b> have no link to it and are parked: tote bags, an animation in the app, a second coffee machine. From now on her status report opens with the benefit, and progress is counted against the 71.</p>""",
    how_figs=[fv_how],
    steps=[("Write the benefit where everyone sees it", "A number and a date."),
           ("Test each piece of work against it", "“What if we drop this?”"),
           ("Sort: must have, helps, no link", "Park the last group."),
           ("Count progress against what matters", "Not against the whole list."),
           ("Start every status with the benefit", "Then the date."),
           ("Ask “still worth it?” at every review", "And act on the answer.")],
    vocab=[("Value", "The worth of what the project brings, compared with what it costs."),
           ("Benefit", "A measurable gain for the business or its customers."),
           ("Business case", "The reasoning for doing the project: benefit, cost, risk."),
           ("Scope", "The work the project will do. Less is often worth more."),
           ("Gold plating", "Adding extras nobody asked for."),
           ("Value-based progress", "Measuring how much of the benefit is secured, not how many tasks are done.")],
    code=dict(file="rotterdam/value-test.md", note="Sanne and Joost, 26 January 2026", plain=True, src="""
# Rotterdam · the 140 rows, tested against the benefit

Benefit   500 orders a day by end May · 90 % on time by end of summer · next city ≤ 8 weeks
Question  "what happens to the benefit if we drop this?"

MUST HAVE to open safely on 27 Apr     71 rows   e.g. cold room, food-safety registration,
                                                 zones + prices in the platform, 40 staff trained
HELPS the benefit, in this order       47 rows   e.g. waitlist push, Saturday slot capacity,
                                                 help pages for Rotterdam
NO LINK → parked                       22 rows   e.g. branded tote bags, app animation,
                                                 second coffee machine

Progress from now on: must-haves done / 71   (today: 24 of 71)
"""),
    tools="tools: the benefit on a card, the task list, and ninety minutes with the sponsor.",
    dial=[("Light", "a short piece of work", ["One sentence of benefit.", "Ask the question when adding work.", "No sorting session."]),
          ("Standard", "Rotterdam", ["The benefit on every plan and status.", "Each row sorted once.", "Progress against must-haves."]),
          ("Heavy", "a large investment", ["A business case kept up to date.", "Value reviewed at each gate.", "Benefits tracked after closing."])],
    baseline="Each line compares <b>counting ticked rows</b> to <b>testing every row against the benefit and counting what matters</b>.",
    ratings=[(2, 5, "Every row has to earn its place."),
             (2, 4, "71 must-haves are easier to forecast than 140 mixed rows."),
             (3, 4, "Must-haves get attention first."),
             (2, 4, "24 of 71 means something."),
             (2, 4, "Femke gets a real answer."),
             (3, 4, "The team can judge its own work."),
             (3, 4, "Parking a row is easy to explain."),
             (3, 3, "Neutral."),
             (3, 4, "22 rows less to do.")],
    pitfalls=[("The date becomes the goal", "Opening on time with nothing on the shelves.", "state the benefit before the date."),
              ("Everything is a must", "The question is answered “disaster” for every row.", "ask for the evidence."),
              ("Gold plating", "Extras creep back in.", "parked means parked until the benefit owner asks."),
              ("Value checked once", "The world changes.", "ask at every review.")],
    use=["Always.", "When the list is longer than the time.", "When progress is reported as a percentage of tasks.", "Before cutting or adding scope."],
    skip=["Never."],
    related=["<b>What Is It All For?</b> (this volume)", "<b>Outcomes over outputs</b> (Grace, vol. 1)", "<b>MoSCoW and its traps</b> (Grace, vol. 2)", "<b>Business case one-pager</b> (Grace, vol. 2)"],
    quiz=[("What is the one question?", "“What happens to the benefit if we drop this?”"),
          ("Is 38 of 140 rows useful progress information?", "No: it doesn't say whether the important rows are done."),
          ("What is gold plating?", "Adding extras nobody asked for."),
          ("Marketing asks to bring the tote bags back, at no cost to the date. What does Sanne ask?", "What they do for the benefit, and who owns that claim. If nobody can say, they stay parked."),
          ("The store can open on 27 April with half the shelves empty. On track?", "On time, but not on value. Sanne reports it that way.")],
    try_it="Write your project's benefit on a card. Take the ten biggest items on your list and ask of each: what happens to the benefit if we drop this? Park one.",
    remember="Pack for the <span class=\"hl\">hut</span>, not for the <span class=\"hl\">list</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the principle “focus on value”.",
             "Project Management Institute, <i>The Standard for Project Management</i> (2021): focus on value.",
             "Joshua Seiden, <i>Outcomes Over Output</i> (2019)."],
)

# ------------------------------------------------------------------ 07 Build Quality In
eq_problem = Doodle(760, 250, "Doodle of the story Tomás tells on 28 January 2026 about Zuid's opening day in November 2024. 340 products had no price. Support heard about it from customers. A push message went to the wrong area. Everything had been checked: the evening before, in one long inspection, when it was too late to fix.",
                    "Zuid, November 2024: one big check the night before, and 340 products with no price in the morning.")
eq_problem.row([("build", None, "paper"), ("build", None, "paper"), ("build", None, "paper"), ("one big check", "the night before", "pink")], y=30, h=70, size=17, subsize=13, gap=34, arrows=True)
eq_problem.note(380, 150, "340 products without a price", "red", size=20)
eq_problem.note(380, 182, "customers told support · push to the wrong area", "red", size=17)
eq_problem.note(380, 224, "found late = expensive to fix", "pen", size=18)

eq_analogy = Doodle(760, 240, "Doodle of a baker. One baker tastes the cake only when it comes out of the oven; if it's wrong, the whole cake is lost. Another weighs the flour, checks the oven temperature and tastes the batter at each step. The second baker rarely throws a cake away.",
                    "Taste the batter, don't judge the cake. Quality is in the steps.")
eq_analogy.box(20, 40, 320, 110, "taste at the end", "paper", sub="wrong? bin the cake", size=18, subsize=15)
eq_analogy.box(420, 40, 320, 110, "check at every step", "green", sub="weigh · oven · batter", size=18, subsize=15)
eq_analogy.note(380, 200, "the cheapest mistake is the one caught at its own step", "pen", size=18)

eq_how = Doodle(760, 380, "Quality built into the Rotterdam launch, agreed on 28 January 2026. Four steps, each with its own check and its own definition of done. Platform set-up: every product has a price and VAT rate, checked by a script each night. Stocking: the shelf label is scanned when the product is placed. People: every picker does twenty practice orders at Noord. End to end: orders run through the RTM-0 test store every week from January. The final rehearsal in April becomes a confirmation, not a hunt.",
                "A check inside every step, with a clear “done”, and a test store running since January.")
steps4 = [("platform set-up", "price + VAT set", "nightly script"),
          ("stocking", "label scanned", "by the stocker"),
          ("people", "20 practice orders each", "at Noord"),
          ("end to end", "weekly order in RTM-0", "since 15 Jan")]
for i, (t, s, who) in enumerate(steps4):
    x = 14 + i * 186
    eq_how.box(x, 20, 172, 70, t, "blue", size=16)
    eq_how.box(x, 110, 172, 90, "check", "green", sub=s, size=16, subsize=12)
    eq_how.note(x + 86, 226, who, "pen", size=15)
    eq_how.arrow(x + 86, 90, x + 86, 108)
eq_how.box(120, 270, 520, 80, "rehearsal week in April", "y", sub="a confirmation, not a hunt for faults", size=19, subsize=15)

QUALITY = dict(
    slug="embed-quality",
    kicker="principle 3 of 6 · a.k.a. “embed quality into processes and deliverables”",
    tldr="Quality is not a check at the end. It is <b>built into each step</b>: a clear definition of “done”, a check made by the person doing the work, and a way to see problems while they are small. Inspection at the end still has a place, as a confirmation. The earlier a fault is found, the cheaper it is, so <b>design the work so faults can't travel far</b>.",
    chips=[("Family", "the six principles"), ("Lives in", "a “done means” line on every step"), ("Pairs with", "definition of done, the walking skeleton, the launch checklist")],
    pmbok=dict(covers="principle: embed quality into processes and deliverables", principles=["Embed quality into processes and deliverables"],
               focus=["planning", "executing", "monitoring"], domains=["governance"],
               older="6th: “project quality management” (plan, manage, control quality). 7th: the principle “build quality into processes and deliverables”."),
    problem_side="Larder, 28 January 2026",
    problem="""  <p class="lead">Sanne asks Tomás how Zuid's opening went in November 2024. He laughs, not happily. <span class="hl-pink">340 products had no price.</span> Support heard it from customers. A push message went to the wrong part of town. Everything <i>had</i> been checked: in one long inspection the evening before, when nobody had the hours to fix what it found.</p>
  <ul>
    <li>Checks came at the end, after the faults had piled up.</li>
    <li>“Done” meant “I've finished my part”, not “it works”.</li>
    <li>The people who made a fault never saw it.</li>
  </ul>""",
    problem_figs=[eq_problem],
    meanwhile=[("architect-1", "walking-skeleton", "Ana's walking skeleton: one test order through the test store RTM-0, end to end, by 15 January.",
                "Sanne turns RTM-0 into a weekly quality check for the whole Rotterdam launch.")],
    analogy_side="the baker",
    analogy="""  <p>One baker tastes the cake when it comes out of the oven. If the salt and sugar were swapped, the cake goes in the bin. Another <b>weighs the flour, checks the oven, tastes the batter</b>. A mistake is caught at its own step, when fixing it costs a spoonful. Both bakers care about quality. Only one of them has built it in.</p>""",
    analogy_figs=[eq_analogy],
    map=[("Tasting the finished cake", "One inspection the night before opening"),
         ("Weighing the flour", "A nightly script: every product has a price and VAT rate"),
         ("Tasting the batter", "A weekly test order through RTM-0"),
         ("The recipe says “golden, springs back”", "A “done means” line for every step"),
         ("The baker tastes their own batter", "The stocker scans the label at the shelf")],
    how_side="a “done means” and a check, inside every step",
    how="""  <p>Sanne, Tomás, Eli and Ben agree four habits. <b>Platform set-up</b>: a script runs every night and lists any product without a price or VAT rate. <b>Stocking</b>: the label is scanned as the product goes on the shelf. <b>People</b>: every new picker does twenty practice orders at Noord before their first shift. <b>End to end</b>: one order a week runs through the test store RTM-0, which Ana's team has had working since 15 January. The rehearsal week in April stays, as a confirmation.</p>""",
    how_figs=[eq_how],
    steps=[("Write “done means…” for each step", "Something you can check."),
           ("Put the check inside the step", "Done by the person doing the work."),
           ("Automate the checks you can", "A nightly script beats a monthly audit."),
           ("Run the whole thing early and often", "Small, end to end."),
           ("Count faults by where they were made", "Fix the step, not only the fault."),
           ("Keep the final inspection", "As a confirmation.")],
    vocab=[("Quality", "How well the result meets what was needed."),
           ("Quality assurance", "Making sure the way of working will produce good results."),
           ("Quality control", "Checking the results themselves."),
           ("Definition of done", "What must be true before a piece of work counts as finished."),
           ("Prevention over inspection", "Stopping faults from being made, not finding them later."),
           ("Cost of quality", "What you spend preventing and checking, plus what faults cost when they escape.")],
    code=dict(file="rotterdam/quality-built-in.md", note="Sanne, Tomás, Eli, Ben · 28 January 2026", plain=True, src="""
# Rotterdam · quality built in

STEP                DONE MEANS                                   CHECK (who, when)
Platform set-up     every product has a price and a VAT rate     script, every night (Eli)
                    every street belongs to a delivery zone      script, every night (Eli)
Stocking            product on the shelf its label names         scan at the shelf (stocker)
People              20 practice orders, under 3 % wrong items    at Noord (Tomás)
App                 Rotterdam order placed, paid, tracked        weekly, RTM-0 (Ben)
End to end          a real basket, picked and delivered          weekly from Feb, RTM-0

Final check         rehearsal week before go / no-go             confirmation only
Lesson from Zuid    340 products with no price, found by customers → the nightly script
"""),
    tools="tools: a “done means” column, a nightly script, a scanner, and the RTM-0 test store.",
    dial=[("Light", "a small change, low stakes", ["A “done means” sentence.", "A second pair of eyes.", "Fix as you go."]),
          ("Standard", "Rotterdam", ["A check inside each step.", "A weekly end-to-end run.", "A final rehearsal to confirm."]),
          ("Heavy", "safety, money or law at stake", ["A quality plan with standards.", "Independent audits.", "Measured fault rates and formal sign-off."])],
    baseline="Each line compares <b>one inspection the night before opening</b> to <b>a check inside every step, plus a weekly end-to-end run</b>.",
    ratings=[(3, 4, "Customers get a store that works on day one."),
             (2, 4, "Fewer late surprises to push the date."),
             (2, 4, "Faults found the day they're made."),
             (2, 4, "The nightly list shows the true state."),
             (2, 4, "Joost sees the checks pass each week."),
             (3, 4, "People check their own work."),
             (3, 3, "Neutral."),
             (1, 5, "That is the whole point."),
             (4, 3, "Checks take a little time every day.")],
    pitfalls=[("Quality as a phase", "“Testing” in the last week.", "a check in every step."),
              ("Checker ≠ maker", "The maker never learns.", "the maker checks first."),
              ("Vague “done”", "“Mostly set up.”", "a “done means” you can check."),
              ("Dropping the final check", "Over-trusting the steps.", "keep it, as a confirmation.")],
    use=["Always.", "After a launch that went wrong.", "When faults are found by customers.", "When “done” starts arguments."],
    skip=["Never. For throwaway experiments, keep only “done means”."],
    related=["<b>Walking skeleton</b> (Ana, vol. 1)", "<b>Definition of ready and done</b> (Grace, vol. 3)", "<b>Launch checklist</b> (Grace, vol. 3)", "<b>Quality assurance vs control</b> (vol. 2)"],
    quiz=[("What went wrong at Zuid?", "One inspection at the end: 340 products had no price on opening day."),
          ("Assurance or control: “the nightly script exists and runs”?", "Assurance: it is about the way of working. The list it produces is control."),
          ("Who checks first?", "The person doing the work."),
          ("Three weeks before launch the nightly script lists 60 products without VAT rates. Good news or bad?", "Good: found with three weeks to spare, at the step that made them. Fix them and ask why that step let them through."),
          ("Is the rehearsal week still needed?", "Yes, as a confirmation, not as the first test.")],
    try_it="Pick one step in your project. Write “done means…” for it in one line that someone else could check. Who makes that check today, and when? Move it one step earlier.",
    remember="Taste the <span class=\"hl\">batter</span>. Don't wait for the <span class=\"hl\">cake</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the principle “embed quality into processes and deliverables”.",
             "W. Edwards Deming, <i>Out of the Crisis</i> (1986): build quality in, stop depending on inspection.",
             "Philip Crosby, <i>Quality Is Free</i> (1979): the cost of quality."],
)

# ------------------------------------------------------------------ 08 Own the Outcome
al_problem = Doodle(760, 250, "Doodle of 30 January 2026, the first Rotterdam status meeting. Twelve and a half weeks to go. Joost would like the status to be green: the team is working hard. Sanne has no agreed plan yet, three open questions, and a fridge order that must go out in two weeks. Green would be comfortable. It would not be true.",
                    "The first status. Green would be comfortable. It would not be true.")
al_problem.icon("traffic", 60, 30, 1.6)
al_problem.box(200, 30, 250, 70, "Joost hopes: green", "green", size=18)
al_problem.box(200, 120, 250, 70, "Sanne sees: amber", "y", size=18)
al_problem.text(600, 60, "no agreed plan yet", size=17)
al_problem.text(600, 92, "3 open questions", size=17)
al_problem.text(600, 124, "fridges: order in 2 weeks", size=17)
al_problem.note(600, 170, "12½ weeks to go", "red", size=20)

al_analogy = Doodle(760, 240, "Doodle of a ship's captain. The captain doesn't row or cook, but answers for the ship, the crew and the cargo. When the weather turns, the captain tells the owner at once and says what they will do. When something goes wrong, the captain says “my ship”, not “the cook's fault”.",
                    "A captain answers for the ship: tells the owner the weather as it is, and says “my ship”.")
al_analogy.icon("ship", 40, 60, 1.6)
al_analogy.row([("answers for it", "ship, crew, cargo", "y"), ("tells the truth", "the weather as it is", "blue"), ("minds the crew", "they sail it", "green")], x=200, y=50, h=90, w=172, gap=12, size=15, subsize=13)
al_analogy.note(470, 196, "“my ship”", "pen", size=22)

al_how = Doodle(760, 360, "Sanne's first status report, 30 January 2026. Overall: amber. Why, in three lines: no agreed plan yet, three open questions, one early order. What she commits to: a first plan by 20 February; the fridge order placed by 13 February; the three questions answered by named people with dates. What she needs from the sponsor: one decision on opening hours and thirty minutes a week. Signed with her name.",
                "An honest amber: why, what I commit to, what I need from you. Signed.")
al_how.box(14, 14, 200, 90, "AMBER", "y", sub="30 January 2026", size=26, subsize=14)
al_how.box(230, 14, 516, 90, None, "paper")
al_how.head(488, 40, "why", size=18)
al_how.text(488, 68, "no agreed plan yet · 3 open questions", size=15)
al_how.text(488, 90, "fridges must be ordered by 13 Feb", size=15)
al_how.box(14, 124, 360, 150, None, "green")
al_how.head(194, 152, "I commit to", size=18)
for i, t in enumerate(["a first plan by 20 Feb", "fridge order placed by 13 Feb", "3 questions: owner + date"]):
    al_how.text(194, 184 + i * 28, t, size=15)
al_how.box(386, 124, 360, 150, None, "blue")
al_how.head(566, 152, "I need from Joost", size=18)
for i, t in enumerate(["opening hours: decide by 2 Feb", "30 minutes every week"]):
    al_how.text(566, 184 + i * 28, t, size=15)
al_how.note(380, 318, "signed: Sanne", "pen", size=22)

LEADER = dict(
    slug="accountable-leader",
    kicker="principle 4 of 6 · a.k.a. “be an accountable leader”",
    tldr="A project manager <b>answers for the outcome</b>, without doing all the work and without owning all the decisions. That means three habits: <b>tell the truth</b> about where the project is, early and plainly; <b>make commitments and keep them</b>, or say first when you can't; and <b>look after the people</b> and the organisation's trust. When it goes well, it was the team. When it goes badly, say “mine”.",
    chips=[("Family", "the six principles"), ("Lives in", "every status, every promise, every bad-news talk"), ("Pairs with", "the project manager's role, status reports, delivering bad news")],
    pmbok=dict(covers="principle: be an accountable leader; stewardship, integrity, leadership", principles=["Be an accountable leader"],
               focus=["initiating", "planning", "executing", "monitoring", "closing"], domains=["governance"],
               older="6th: leadership skills in chapter 3, and the PMI Code of Ethics. 7th: the principles “be a diligent, respectful and caring steward” and “demonstrate leadership behaviors”."),
    problem_side="Larder, 30 January 2026",
    problem="""  <p class="lead">The first Rotterdam status meeting, with Femke, Marco, Priya and Joost. <b>Twelve and a half weeks</b> to go. Before the meeting Joost says, kindly, “let's show green: the team is working flat out.” Sanne has no agreed plan, three open questions and a fridge order that must go out by mid-February. <span class="hl-pink">Green would be comfortable. It would not be true</span>, and in April it would be her green.</p>
  <ul>
    <li>Status is treated as a mood, not a measurement.</li>
    <li>Bad news travels late, when choices are gone.</li>
    <li>Nobody has yet said “this is mine”.</li>
  </ul>""",
    problem_figs=[al_problem],
    analogy_side="the ship's captain",
    analogy="""  <p>A <b>captain</b> doesn't row, cook or load the cargo. But the captain <b>answers for the ship</b>. When the weather turns, the owner hears it from the captain, at once, with what they'll do about it. When the cook burns dinner, the captain doesn't say “the cook's fault” to the owner. And a captain who wears out the crew to make one port on time has no crew for the next.</p>""",
    analogy_figs=[al_analogy],
    map=[("The ship, crew and cargo", "The launch, the team, Larder's money and name"),
         ("The owner", "Joost and the steering group"),
         ("Reporting the weather as it is", "Amber, with reasons"),
         ("“My ship”", "Signing the status with her own name"),
         ("Not wearing out the crew", "No plan that depends on weekends")],
    how_side="an honest status, a commitment, a request",
    how="""  <p>Sanne reports <b>amber</b> and gives three reasons. Then two lists. <b>I commit to</b>: a first plan by 20 February, the fridge order by 13 February, each open question with a named owner and a date. <b>I need from you</b>: a decision on opening hours by Monday, and thirty minutes a week with Joost. She signs it. Femke's only question: “when will we know if it turns red?” Marco, afterwards: “first status report here I've believed.”</p>""",
    how_figs=[al_how],
    steps=[("Report what is true", "With reasons, not adjectives."),
           ("Say what you commit to", "Few things, with dates."),
           ("Say what you need", "From named people."),
           ("Put your name on it", "And keep the promise."),
           ("If you'll miss a promise, say so first", "Before the date, not after."),
           ("Share credit, keep blame", "And protect the team's time.")],
    vocab=[("Accountability", "Answering for the result, whoever did the work."),
           ("Stewardship", "Looking after what you've been trusted with: money, people, reputation."),
           ("Integrity", "Doing what you said, and saying what is true."),
           ("Commitment", "A promise with a date and a name."),
           ("Transparency", "Letting people see the real state of things."),
           ("Servant leadership", "Leading by removing what stops the team.")],
    code=dict(file="rotterdam/status-2026-01-30.md", note="the first status report · to Femke, Marco, Priya, Joost", plain=True, src="""
# Rotterdam · status · Friday 30 January 2026 · 12½ weeks to opening

OVERALL   AMBER
WHY       1 no agreed plan yet (first plan: 20 Feb)
          2 three open questions: opening hours · who trains couriers · Saturday slots
          3 cold room and fridges take 8 weeks: order must go out by 13 Feb

I COMMIT TO                                   BY
  a first plan, made with the team            20 Feb
  fridge order placed (with Joost)            13 Feb
  an owner and a date for each open question   6 Feb

I NEED FROM YOU
  Joost    decide opening hours                2 Feb
  Joost    30 minutes with me, every week      from now
  Marco    confirm the budget of €380k stands  6 Feb

Turns RED if: the fridge order slips past 13 Feb, or there is no plan on 20 Feb.
                                                              Sanne
"""),
    tools="tools: one page a week, a short list of promises, and your own name at the bottom.",
    dial=[("Light", "a small team that talks daily", ["Say the true status out loud.", "One promise at a time.", "Own misses the same day."]),
          ("Standard", "Rotterdam", ["A weekly one-page status.", "Commitments and needs listed.", "“Turns red if…” written down."]),
          ("Heavy", "public money, contracts, regulators", ["Formal reporting and audit trail.", "A code of conduct.", "Independent assurance."])],
    baseline="Each line compares <b>a green status because the team is working hard</b> to <b>an honest amber with commitments, requests and a name</b>.",
    ratings=[(3, 4, "Attention goes to what threatens the benefit."),
             (2, 4, "Promises with dates can be checked."),
             (2, 4, "“Turns red if” names the danger early."),
             (1, 5, "The status is true."),
             (2, 5, "Marco believes the report."),
             (3, 4, "The team isn't blamed or hidden behind."),
             (3, 4, "Early bad news leaves choices open."),
             (3, 3, "Neutral."),
             (4, 4, "One page a week.")],
    pitfalls=[("Watermelon status", "Green outside, red inside.", "reasons, not colours, come first."),
              ("Blame", "“The builder let us down.”", "say “mine”, then fix it."),
              ("Hero mode", "The project manager does everything.", "answer for it; let the team do it."),
              ("Promises without dates", "“Soon.”", "a date and a name, or it isn't a promise.")],
    use=["Every status, every week.", "When the news is bad.", "When someone asks you to soften a report.", "When you inherit a project."],
    skip=["Never."],
    related=["<b>What Is My Job Here?</b> (this volume)", "<b>Delivering bad news</b> (Grace, vol. 5)", "<b>Status reports that tell the truth</b> (vol. 2)", "<b>Let the Team Decide</b> (this volume)"],
    quiz=[("Why not report green?", "It wasn't true: no plan, three open questions, a long-lead order not placed."),
          ("What three things did the status contain besides the colour?", "Why, what Sanne commits to, what she needs."),
          ("What is a watermelon status?", "Green on the outside, red inside."),
          ("On 12 February Sanne sees the plan won't be ready on the 20th. What does she do?", "Tell Joost that day, with the new date and the reason. A missed promise is announced before its date."),
          ("The builder is a week late. What does Sanne say to the steering group?", "“We are a week late on the fit-out; here is what I'm doing.” Not “the builder's fault”.")],
    try_it="Write this week's status for your project in the same shape: colour, why (three lines), I commit to, I need from you, and “turns red if…”. Would you sign it?",
    remember="Report the <span class=\"hl\">weather as it is</span>, and say <span class=\"hl\">“my ship”</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the principle “be an accountable leader”.",
             "Project Management Institute, <i>Code of Ethics and Professional Conduct</i>.",
             "L. David Marquet, <i>Turn the Ship Around!</i> (2012).",
             "Kim Scott, <i>Radical Candor</i> (2017)."],
)

# ------------------------------------------------------------------ 09 Think Past the Finish
su_problem = Doodle(760, 250, "Doodle of 2 February 2026. The fit-out quote offers two kinds of fridge. Open fridges cost fourteen thousand euros less to buy. Fridges with doors use less electricity, about six thousand euros a year less. The project budget only sees the purchase price. The store will pay the electricity bill for ten years.",
                    "The project pays for the fridges once. The store pays for the electricity for ten years.")
su_problem.box(20, 30, 330, 110, "open fridges", "paper", sub="€14k cheaper to buy", size=20, subsize=16)
su_problem.box(410, 30, 330, 110, "fridges with doors", "green", sub="≈ €6k a year less power", size=20, subsize=16)
su_problem.note(380, 186, "the project budget sees only the left number", "red", size=19)
su_problem.note(380, 222, "who answers for the next ten years?", "pen", size=18)

su_analogy = Doodle(760, 240, "Doodle of a family planting a tree in their garden. They think about the shade in twenty years, the roots near the neighbour's wall, the leaves in the gutter, and the fruit. A tree planted only for this summer's photo is in the wrong place by the time it's grown.",
                    "Planting a tree: think about the shade, the roots and the neighbour, twenty years on.")
su_analogy.row([("people", "the neighbour's wall", "pink"), ("planet", "shade, birds, soil", "green"), ("money", "fruit, upkeep", "y")], y=50, h=90, size=19, subsize=14)
su_analogy.note(380, 200, "plant for the tree it will become", "pen", size=20)

su_how = Doodle(760, 380, "Sanne's long-view check, used on three Rotterdam decisions on 2 February 2026. Three questions for each: people, planet, money over five years. Fridges: doors chosen, fourteen thousand euros more, pays back in about two and a half years. Early deliveries: start at half past seven, not seven, for the neighbours. Unsold food: a daily pick-up by a Rotterdam food bank, agreed before opening. Each decision records what it costs the project now.",
                "Three questions on every big decision: people, planet, and money over five years.")
su_how.row([("people?", "staff, neighbours, customers", "pink"), ("planet?", "energy, waste, transport", "green"), ("money, 5 years?", "not just the project", "y")], y=14, h=76, size=18, subsize=13)
for i, (t, d, c) in enumerate([("fridges", "with doors", "+€14k · back in 2½ yrs"),
                               ("deliveries", "from 07:30, not 07:00", "30 minutes of slots"),
                               ("unsold food", "food bank, daily", "one shelf, one contact")]):
    y = 116 + i * 84
    su_how.box(14, y, 200, 68, t, "blue", size=18)
    su_how.box(228, y, 250, 68, d, "paper", size=16)
    su_how.box(492, y, 254, 68, c, "paper", size=14, dash=True)
su_how.note(114, 372, "decision", size=15)
su_how.note(353, 372, "chosen", size=15)
su_how.note(619, 372, "cost to the project", size=15)

SUSTAIN = dict(
    slug="sustainability",
    kicker="principle 5 of 6 · a.k.a. “integrate sustainability within all project areas”",
    tldr="A project is short. What it leaves behind lasts. <b>Sustainability</b> means weighing the long-term effect of project decisions on <b>people</b> (staff, neighbours, customers), the <b>planet</b> (energy, waste, transport) and <b>money</b> (running costs, not just the project budget). It is not a separate workstream or a report at the end. It is <b>three questions asked inside ordinary decisions</b>.",
    chips=[("Family", "the six principles"), ("Lives in", "three questions on every big decision"), ("Pairs with", "focus on value, total cost of ownership, the decision log")],
    pmbok=dict(covers="principle: integrate sustainability within all project areas", principles=["Integrate sustainability within all project areas"],
               focus=["planning", "executing", "closing"], domains=["finance", "resources", "stakeholders"],
               older="6th: not a topic of its own (a line under trends). 7th: part of stewardship. New as a principle in the 8th."),
    problem_side="Larder, 2 February 2026",
    problem="""  <p class="lead">The fit-out quote arrives with a choice. <b>Open fridges</b> are €14,000 cheaper. <b>Fridges with doors</b> use about €6,000 a year less electricity. Sanne's budget only feels the first number, and it is tight. <span class="hl-pink">The store will pay the second number every year for ten years</span>, long after the project has closed and Sanne has moved on to Utrecht.</p>
  <ul>
    <li>A project is judged on its own budget and date.</li>
    <li>Running costs, staff and neighbours aren't in the plan.</li>
    <li>“We'll fix it after launch” rarely happens.</li>
  </ul>""",
    problem_figs=[su_problem],
    analogy_side="planting a tree",
    analogy="""  <p>When a family <b>plants a tree</b>, the planting takes an afternoon. The tree stays for fifty years. So they think about where the <b>shade</b> will fall, whether the <b>roots</b> will reach the neighbour's wall, who will clear the <b>leaves</b>, and what the <b>fruit</b> is worth. A tree planted for this summer's photo is in the wrong place by the time it has grown.</p>""",
    analogy_figs=[su_analogy],
    map=[("The afternoon of planting", "The fifteen-week project"),
         ("Fifty years of tree", "A store that runs for ten years or more"),
         ("The neighbour's wall", "Noise from 07:00 deliveries; staff contracts"),
         ("Shade and soil", "Energy for cooling; unsold food"),
         ("Fruit and upkeep", "Running costs after the project closes")],
    how_side="three questions, inside the decision",
    how="""  <p>Sanne adds three questions to any decision over €5,000 or with a life longer than the project: <b>people?</b> <b>planet?</b> <b>money over five years?</b> That Monday three decisions get them. <b>Fridges</b>: doors, €14k more, paid back in about two and a half years; Marco agrees to move the money. <b>First deliveries</b>: 07:30, not 07:00, for the street. <b>Unsold food</b>: a daily pick-up by a Rotterdam food bank, arranged before opening instead of “later”. Each choice is written in the decision log with what it costs the project now.</p>""",
    how_figs=[su_how],
    steps=[("Pick the decisions that outlive the project", "Buildings, equipment, contracts, data."),
           ("Ask: who is affected, and how?", "Staff, neighbours, customers."),
           ("Ask: what does it use and waste?", "Energy, materials, transport."),
           ("Ask: what does it cost over five years?", "Not just to buy."),
           ("Decide with the person who'll live with it", "The store manager, the finance lead."),
           ("Write down the trade-off", "What it costs the project now, and why.")],
    vocab=[("Sustainability", "Meeting today's needs without harming the ability to meet tomorrow's."),
           ("Triple bottom line", "Judging results on people, planet and profit together."),
           ("Total cost of ownership", "What something costs to buy, run, maintain and remove."),
           ("Payback period", "How long until the savings cover the extra cost."),
           ("Social impact", "The effect on staff, neighbours and communities."),
           ("Life-cycle thinking", "Looking at a thing from making to disposal.")],
    code=dict(file="rotterdam/long-view.md", note="Sanne · three decisions, 2 February 2026", plain=True, src="""
# Rotterdam · the long view (decisions > €5k or that outlive the project)

DECISION        PEOPLE              PLANET             MONEY, 5 YEARS          CHOSEN
Fridges         warmer aisles for   ≈ a third less     +€14k to buy            doors
                pickers             electricity        ≈ −€6k a year           (Marco: OK)
                                                       pays back ≈ 2½ years
First           street wakes at     -                  30 min fewer slots      07:30
deliveries      07:00 (lease:                          a day
                none before 07:30)
Unsold food     staff dislike       less in the bin    one shelf, one contact  food bank,
                binning food                           ≈ €0                    daily, from
                                                                               week 1
Cost to the project now: €14k from the reserve (€20k → €6k). Flagged to Joost.
"""),
    tools="tools: three questions, a five-year sum, and the person who will live with the result in the room.",
    dial=[("Light", "a small internal change", ["Ask “who lives with this afterwards?”", "A sentence in the decision.", "No sums."]),
          ("Standard", "Rotterdam", ["Three questions on decisions over €5k.", "A five-year cost line.", "Recorded in the decision log."]),
          ("Heavy", "construction, public works, big supply chains", ["An impact assessment.", "Sustainability targets and reporting.", "Supplier standards in contracts."])],
    baseline="Each line compares <b>choosing by purchase price and launch date</b> to <b>asking people, planet and five-year money on decisions that outlive the project</b>.",
    ratings=[(3, 4, "Value over ten years, not fifteen weeks."),
             (3, 3, "Neutral."),
             (3, 4, "Fewer complaints and fines later."),
             (3, 4, "Trade-offs are written down."),
             (3, 4, "Marco and the neighbours see they were considered."),
             (3, 4, "Staff see their concerns in decisions."),
             (3, 3, "Neutral."),
             (3, 4, "A store built to run well."),
             (4, 3, "A few extra questions and sums.")],
    pitfalls=[("A sustainability section at the end", "Written after everything is decided.", "ask inside each decision."),
              ("Only “planet”", "Forgetting staff and running costs.", "three questions."),
              ("The project's budget wins every time", "Cheap now, dear for ten years.", "show the five-year number to the sponsor."),
              ("Good intentions, no owner", "“We'll donate unsold food.”", "a name and a start date.")],
    use=["Buildings, equipment, long contracts.", "Decisions that affect staff or neighbours.", "When “cheapest” is the only argument.", "Before closing: what are we leaving behind?"],
    skip=["Short-lived choices that end with the project."],
    related=["<b>Focus on Value</b> (this volume)", "<b>Total cost of ownership</b> (Ana, vol. 5)", "<b>Decision log</b> (Ana, vol. 2)", "<b>Working with legal and privacy</b> (Grace, vol. 5)"],
    quiz=[("What are the three questions?", "People, planet, and money over five years."),
          ("Why did doors win on the fridges?", "€14k more to buy, about €6k a year less to run: paid back in about two and a half years."),
          ("Is sustainability a separate workstream?", "No. It is asked inside ordinary decisions."),
          ("The reserve is now €6k and the builder offers cheaper lighting that uses twice the power. What does Sanne do?", "Run the same three questions with the five-year cost, and take both numbers to Joost. The project budget alone doesn't decide."),
          ("Who should be in the room?", "The person who will live with the result: here, the store manager and finance.")],
    try_it="Find one decision in your project that will outlive it. Ask the three questions. Write the five-year cost next to the purchase price. Does the choice still look right?",
    remember="The planting takes an <span class=\"hl\">afternoon</span>. The tree stays <span class=\"hl\">fifty years</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the principle “integrate sustainability within all project areas”.",
             "John Elkington, <i>Cannibals with Forks</i> (1997): the triple bottom line.",
             "GPM Global, <i>The GPM P5 Standard for Sustainability in Project Management</i>.",
             "United Nations, <i>Sustainable Development Goals</i> (2015)."],
)

# ------------------------------------------------------------------ 10 Let the Team Decide
ec_problem = Doodle(760, 250, "Doodle of 3 February 2026. Sanne has written a plan alone: 96 tasks, each with a date and a name. She shows it to Ben. He reads three lines and says the app estimate is half what it needs, two tasks are in the wrong order, and nobody asked him. The plan is neat, complete, and wrong.",
                    "96 tasks, planned alone at a desk. Neat, complete, and wrong in three lines.")
ec_problem.box(20, 40, 280, 110, "Sanne's plan", "y", sub="96 tasks · dates · names", size=20, subsize=15)
ec_problem.box(460, 20, 280, 50, "“app estimate: half”", "pink", size=15)
ec_problem.box(460, 80, 280, 50, "“wrong order”", "pink", size=15)
ec_problem.box(460, 140, 280, 50, "“nobody asked me”", "pink", size=15)
ec_problem.arrow(302, 95, 458, 45, color="red")
ec_problem.arrow(302, 95, 458, 105, color="red")
ec_problem.arrow(302, 95, 458, 165, color="red")
ec_problem.note(160, 210, "a plan the team doesn't own", "red", size=18)

ec_analogy = Doodle(760, 240, "Doodle of a jazz band. The leader names the tune, the key and the tempo, then lets each player decide what to play. Nobody hands the drummer every note. If the leader wrote out every note, it would be a worse band and a tired leader.",
                    "A band leader gives the tune, the key and the tempo. The players choose the notes.")
ec_analogy.row([("the tune", "what and why", "y"), ("the key + tempo", "limits and dates", "blue"), ("the notes", "the players decide", "green")], y=50, h=90, size=18, subsize=14)
ec_analogy.note(380, 200, "clear frame, free hands", "pen", size=20)

ec_how = Doodle(760, 380, "The planning session of 4 February 2026. Sanne brings the frame: the benefit, the fixed date of 27 April, the budget of 380 thousand euros, and the known limits. The team, Ben, Dee, Eli, Tomás and Joost's operations lead, bring the work: they break it down, estimate it and order it themselves. Below: who decides what. The team decides how and in what order. Sanne decides how the plan fits together. The sponsor decides when the date, the money or what customers get would change.",
                "Sanne brings the frame. The team makes the plan. Three levels of decision, written down.")
ec_how.box(14, 14, 340, 150, None, "y")
ec_how.head(184, 42, "Sanne brings the frame", size=18)
for i, t in enumerate(["the benefit", "27 April, fixed", "€380k · the known limits"]):
    ec_how.text(184, 76 + i * 28, t, size=16)
ec_how.box(406, 14, 340, 150, None, "green")
ec_how.head(576, 42, "the team makes the plan", size=18)
for i, t in enumerate(["break the work down", "estimate their own work", "put it in order"]):
    ec_how.text(576, 76 + i * 28, t, size=16)
ec_how.arrow(356, 89, 404, 89)
ec_how.row([("the team decides", "how, and in what order", "green"), ("Sanne decides", "how the plan fits together", "y"), ("the sponsor decides", "date · money · launch scope", "pink")], y=200, h=96, size=17, subsize=13)
ec_how.note(380, 340, "decide at the lowest level that has the facts", "pen", size=19)

EMPOWER = dict(
    slug="empowered-culture",
    kicker="principle 6 of 6 · a.k.a. “build an empowered culture”",
    tldr="The people doing the work know most about it. An <b>empowered culture</b> gives them a <b>clear frame</b> (the goal, the limits, the date), the <b>facts</b>, and the <b>authority to decide</b> inside that frame, and makes it safe to say “this won't work”. The project manager's part is the frame and the fit between pieces, not every decision. Plans made by the team are <b>better plans, and they get kept</b>.",
    chips=[("Family", "the six principles"), ("Lives in", "planning sessions, decision rules, how bad news is received"), ("Pairs with", "the product trio, decision rights, own the outcome")],
    pmbok=dict(covers="principle: build an empowered culture; teams, trust, psychological safety", principles=["Build an empowered culture"],
               focus=["planning", "executing"], domains=["resources"],
               older="6th: “project resource management” (develop team, manage team). 7th: the Team domain and the principle “create a collaborative project team environment”."),
    problem_side="Larder, 3–4 February 2026",
    problem="""  <p class="lead">Sanne has promised a plan by 20 February. She does what worked at her old job: writes it herself. <b>96 tasks</b>, each with a date and a name. On 3 February she shows Ben. He reads three lines: the app estimate is half what it needs, two tasks are the wrong way round, <span class="hl-pink">and nobody asked him.</span> He isn't angry. He just won't be working to that plan.</p>
  <ul>
    <li>The person planning doesn't have the facts.</li>
    <li>People don't commit to dates they didn't give.</li>
    <li>Every question now comes back to Sanne's desk.</li>
  </ul>""",
    problem_figs=[ec_problem],
    meanwhile=[("product-3", "product-trio", "from 9 February Grace, Noor and Ben decide together what to build: a trio, not a queue of approvals.",
                "the week before, Sanne stops planning for the team and has the team make the Rotterdam plan.")],
    analogy_side="the jazz band",
    analogy="""  <p>A <b>band leader</b> names the tune, the key and the tempo, and counts the band in. Then each player decides what to play, listening to the others. Nobody hands the drummer every note. A leader who tried would get a worse band, and would be too busy writing notes to hear that the song was going wrong.</p>""",
    analogy_figs=[ec_analogy],
    map=[("The tune", "The benefit: a city that orders, opened fast"),
         ("Key and tempo", "27 April, €380k, the known limits"),
         ("The players choose the notes", "Ben, Dee, Eli and Tomás plan and estimate their own work"),
         ("Listening to each other", "Planning in one room, dependencies out loud"),
         ("The leader hears the whole song", "Sanne watches how the pieces fit")],
    how_side="bring the frame, let the team plan, write who decides what",
    how="""  <p>Sanne throws away the 96 tasks and books two hours on <b>4 February</b> with Ben, Dee, Eli, Tomás and Joost's operations lead. She brings the <b>frame</b>: the benefit, the date, the budget, the limits from her scan. They bring the work: they break it down, estimate it and order it. She asks questions and writes down what waits for what. Then they agree <b>who decides what</b>: the team decides how and in what order; Sanne decides how the plan fits together; three things go to the sponsor. The plan has fewer lines than hers, and everyone in the room has put their name to a date.</p>""",
    how_figs=[ec_how],
    steps=[("Give the frame", "Goal, date, money, limits. Short."),
           ("Share the facts", "Everything you know, including bad news."),
           ("Let the people who do the work plan it", "Their breakdown, their estimates."),
           ("Write who decides what", "Three levels is enough."),
           ("Make it safe to say “this won't work”", "Thank the first person who does."),
           ("Stay out of the how", "Watch the fit between pieces.")],
    vocab=[("Empowerment", "Giving people the authority, facts and trust to decide in their own area."),
           ("Self-organising team", "A team that plans and divides its own work."),
           ("Psychological safety", "Feeling safe to speak up, disagree and admit mistakes."),
           ("Decision level", "Who decides: the team, the project manager or the sponsor."),
           ("Guardrails", "The limits inside which a team is free to choose."),
           ("Commitment", "A date someone gave themselves, not one they were given.")],
    code=dict(file="rotterdam/who-decides.md", note="agreed in the planning session, 4 February 2026", plain=True, src="""
# Rotterdam · who decides what

THE FRAME (from Sanne)
  benefit   500 orders a day by end May · 90 % on time by end of summer · next city ≤ 8 weeks
  fixed     opening 27 April (lease) · budget €380k · max 4 new hires · StockPilot stays

THE TEAM DECIDES            how the work is done, how big it is, in what order
  apps Ben, Dee · platform Eli · stores Tomás · fit-out and people Joost's ops lead

SANNE DECIDES               how the pieces fit: dependencies, shared milestones, the weekly status

THE SPONSOR (JOOST) DECIDES when the date is at risk by more than 3 days
                            when a change costs more than €5,000
                            when what customers get at launch would change

RULES   say "this won't work" as soon as you think it · estimates belong to those who do the work
"""),
    tools="tools: a room, two hours, sticky notes, and the discipline not to pick up the pen.",
    dial=[("Light", "a small experienced team", ["State the goal and the limit.", "The team plans.", "Decision levels by word of mouth."]),
          ("Standard", "Rotterdam: five leads", ["A planning session with the leads.", "A written “who decides what”.", "Weekly check on the fit."]),
          ("Heavy", "many teams, new people, vendors", ["Team charters and working agreements.", "A responsibility matrix.", "Coaching for leads; escalation paths in writing."])],
    baseline="Each line compares <b>a plan written by the project manager alone</b> to <b>a frame from the project manager and a plan made by the team</b>.",
    ratings=[(3, 4, "People who know the work aim it at the benefit."),
             (2, 4, "Estimates come from those who do the work."),
             (2, 4, "“This won't work” is said in February."),
             (3, 4, "Dependencies are said out loud."),
             (3, 4, "Leads stand behind their dates."),
             (1, 5, "That is the whole point."),
             (2, 4, "Decisions are made where the facts are."),
             (3, 4, "Makers care about what they committed to."),
             (3, 4, "Fewer questions queue at one desk.")],
    pitfalls=[("Freedom without a frame", "“Just plan it.”", "goal, date, money and limits first."),
              ("A frame that is really a plan", "Every step prescribed.", "say what and why, not how."),
              ("Punishing bad news", "People stop bringing it.", "thank them, then act."),
              ("Taking the decision back", "At the first wobble.", "ask a question; don't take the pen.")],
    use=["Always, with the frame sized to the team.", "When estimates keep being wrong.", "When every question lands on one desk.", "When a new plan is needed."],
    skip=["A real emergency: decide, then explain. Go back to the frame afterwards."],
    related=["<b>The product trio</b> (Grace, vol. 3)", "<b>Decision rights</b> (Ana, vol. 2)", "<b>Own the Outcome</b> (this volume)", "<b>Leading without authority</b> (vol. 4)"],
    quiz=[("What does the project manager bring to planning?", "The frame: goal, date, money, limits, and the facts."),
          ("Who estimates the app work?", "Ben's and Dee's teams: the people who do it."),
          ("Name the three decision levels.", "The team, the project manager, the sponsor."),
          ("In week six Eli says the platform set-up will be four days late. What does Sanne do first?", "Thank him for saying it early. Four days is over the three-day trigger, so she takes options to Joost; she doesn't redo Eli's plan for him."),
          ("Why was the team's plan better than Sanne's 96 tasks?", "It used their facts, and they committed to dates they gave themselves.")],
    try_it="Before your next planning meeting, write the frame on half a page: goal, date, money, limits. In the meeting, don't write a single task yourself. Afterwards, write down who decides what, in three levels.",
    remember="Give the <span class=\"hl\">tune</span>, the <span class=\"hl\">key</span> and the <span class=\"hl\">tempo</span>. Let them play.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the principle “build an empowered culture”.",
             "Amy Edmondson, <i>The Fearless Organization</i> (2018): psychological safety.",
             "L. David Marquet, <i>Turn the Ship Around!</i> (2012).",
             "Daniel Pink, <i>Drive</i> (2009)."],
)

NOTES = [HOLISTIC, VALUE, QUALITY, LEADER, SUSTAIN, EMPOWER]
