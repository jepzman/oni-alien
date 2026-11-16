# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 3 · By when? (the Schedule domain)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 3").
# The fit-out network below is the one worked example for notes 08–12; its numbers were checked by hand and by script:
# critical path A-B-E-F-G-H-K-L = 25 working days (Mon 2 Mar → Fri 3 Apr 2026); C and D have 4 days of float;
# I-J (cold room) has none because of the delivery date (Fri 27 Mar). Builder's calendar: Mon–Fri, not Easter Monday 6 Apr.

SCHED = ["schedule"]

ACT = {  # key: (short name, full name, working days, waits for)
    "A": ("strip-out", "strip-out", 3, ""),
    "B": ("1st fix", "electrical first fix", 4, "A"),
    "C": ("plumbing", "plumbing and drains", 3, "A"),
    "D": ("screed", "floor screed and curing", 7, "C"),
    "E": ("walls", "walls, ceiling, cold-room base", 5, "B"),
    "F": ("2nd fix", "electrical second fix", 4, "E"),
    "G": ("inspect", "electrical inspection", 1, "F"),
    "H": ("paint", "paint and finishes", 3, "G, D"),
    "I": ("cold room", "cold-room build (delivery 27 Mar)", 3, "D"),
    "J": ("test 48 h", "cold room energised, 48 h test", 2, "I, G"),
    "K": ("shelving", "shelving, fridges, chargers", 3, "H"),
    "L": ("snags", "snagging and clean", 2, "K"),
}
ES = {"A": 1, "B": 4, "C": 4, "D": 7, "E": 8, "F": 13, "G": 17, "H": 18, "I": 21, "J": 24, "K": 21, "L": 24}
EF = {"A": 3, "B": 7, "C": 6, "D": 13, "E": 12, "F": 16, "G": 17, "H": 20, "I": 23, "J": 25, "K": 23, "L": 25}
TF = {"C": 4, "D": 4}
CRIT = set("ABEFGHKL")
POS = {"A": (0, 1), "B": (1, 0), "C": (1, 2), "E": (2, 0), "D": (2, 2), "F": (3, 0), "G": (4, 0), "H": (5, 0), "I": (5, 2),
       "K": (6, 0), "J": (6, 2), "L": (7, 0), "M": (8, 1)}


def network(d, crit=False, times=False, floats=False, y0=30):
    """The Rotterdam fit-out as an activity-on-node network. 9 columns, 3 rows."""
    W, H, step = 64, 60, 83
    ys = [y0, y0 + 88, y0 + 176]

    def xy(k):
        c, r = POS[k]
        return 8 + c * step, ys[r]

    def red(a, b):
        return "red" if crit and a in CRIT | {"M"} and b in CRIT | {"M"} else ""

    def right(k):
        x, y = xy(k)
        return x + W, y + H // 2

    def left(k):
        x, y = xy(k)
        return x, y + H // 2

    for a, b in [("A", "B"), ("A", "C"), ("B", "E"), ("C", "D"), ("E", "F"), ("F", "G"), ("G", "H"), ("D", "I"), ("I", "J"),
                 ("H", "K"), ("K", "L"), ("L", "M"), ("J", "M")]:
        (x1, y1), (x2, y2) = right(a), left(b)
        d.arrow(x1, y1, x2, y2, color=red(a, b))
    hx, hy = xy("H")
    d.arrow(right("D")[0], right("D")[1], hx + W // 2, hy + H)                     # D → H, into H from below
    gx, gy = xy("G")
    jx, jy = xy("J")
    d.arrow(gx + W // 2, gy + H, jx + W // 2, jy, curve=(515, y0 + 112))           # G → J, round the H box
    for k in POS:
        x, y = xy(k)
        on = crit and (k in CRIT or k == "M")
        if k == "M":
            d.box(x, y, W, H, "hand-", "y", sub="over", size=15, subsize=15, stroke="red" if on else "")
            continue
        short, _, dur, _ = ACT[k]
        d.box(x, y, W, H, f"{k} · {dur}", "pink" if on else "blue", sub=short, size=16, subsize=12, stroke="red" if on else "")
        if times:
            d.note(x + W / 2, y - 6 if y == ys[0] else y + H + 15, f"{ES[k]}–{EF[k]}", size=13)
        if floats and k in TF:
            d.note(x + W / 2, y + H + 15, f"float {TF[k]}", "green", size=13)
    ix, iy = xy("I")
    d.note(ix + W / 2, iy - 10, "delivery 27 Mar", "red", size=12)


# ------------------------------------------------------------------ 08 What Waits for What?
nd_problem = Doodle(760, 250, "Doodle of 12 February 2026 and Sanne's mistake for this collection. She has turned the builder's quote into a bar chart: twelve bars with dates, no links between them. Joost asks: if the electrical inspection is a week late, what happens to the handover? Sanne looks at the bars and cannot say. Bars don't know what waits for what.",
                    "Twelve bars, no links. “If the inspection is a week late, when do we get the store?” The bars can't say.")
for i in range(6):
    nd_problem.box(30 + i * 52, 30 + i * 24, 120, 18, None, "blue", rx=3)
nd_problem.box(30 + 4 * 52, 30 + 4 * 24, 120, 18, None, "pink", rx=3)
nd_problem.box(430, 40, 310, 90, "Joost asks:", "paper", sub="“inspection a week late: then what?”", size=18, subsize=15)
nd_problem.note(585, 172, "the bars don't know", "red", size=20)
nd_problem.note(380, 226, "a bar chart without links can't answer “what if?”", "pen", size=17)

nd_analogy = Doodle(760, 240, "Doodle of getting ready for a dinner party. The oven must be hot before the roast goes in. The table can be laid any time. The guests' arrival is fixed by the invitation, not by the cook. Some waits are physics, some are choices, some are outside your kitchen.",
                    "The oven before the roast (must), the table whenever (choice), the guests at eight (outside).")
nd_analogy.row([("oven, then roast", "must: physics", "pink"), ("lay the table", "any time: a choice", "blue"), ("guests at 8", "outside your kitchen", "y")], y=50, h=90, size=17, subsize=14)
nd_analogy.note(132, 186, "mandatory", "red", size=18)
nd_analogy.note(380, 186, "discretionary", "red", size=18)
nd_analogy.note(628, 186, "external", "red", size=18)

nd_how = Doodle(760, 330, "The Rotterdam fit-out network, drawn with Kees, the builder's site manager, on 19 February 2026. Twelve activities and the handover, with arrows for what waits for what. Strip-out first; then electrical first fix and plumbing; walls and ceiling after first fix; floor screed and curing after plumbing; electrical second fix, then the inspection; paint and finishes after the inspection and the cured floor; the cold room is built on the cured floor once it is delivered on 27 March and energised after the inspection; shelving after paint; snagging after shelving; handover when both the snagging and the cold-room test are done.",
                "Twelve activities, the arrows between them, and one wait from outside: the cold room's delivery.", exact=True)
network(nd_how)


NETWORK = dict(
    slug="network-diagram",
    kicker="a.k.a. sequencing activities: dependencies and the network diagram",
    tldr="Before a schedule has dates it needs <b>order</b>: which activities wait for which. Draw each activity as a box and each wait as an arrow: a <b>network diagram</b>. Most waits are <b>finish-to-start</b> (B can't start until A finishes). Some are <b>mandatory</b> (physics, law), some <b>discretionary</b> (a preference you could change), some <b>external</b> (a delivery, an inspector). A bar chart without these links looks like a plan, but can't answer the only question that matters when something slips: <b>what moves with it?</b>",
    chips=[("Family", "by when?"), ("Lives in", "a sheet of sticky notes and arrows, then the scheduling tool"), ("Pairs with", "the WBS, critical path, last responsible moment")],
    pmbok=dict(covers="sequencing activities; finish-to-start and other dependencies; mandatory, discretionary and external dependencies; leads and lags",
               domains=SCHED, processes=["Develop Schedule"], principles=["Adopt a holistic view"], focus=["planning"],
               older="6th: “Define Activities” (6.2) and “Sequence Activities” (6.3), the precedence diagramming method. In the 8th both sit inside Develop Schedule."),
    problem_side="Larder, 12–19 February 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. On 12 February she turns the builder's quote into a tidy <b>bar chart</b>: twelve bars, each with a start and an end, from 2 March to 3 April. Joost looks at it and asks the obvious question: <b>“if the electrical inspection is a week late, when do we get the store?”</b> <span class="hl-pink">Sanne looks at the bars and can't say.</span> Nothing on the chart says which bars wait for the inspection and which don't.</p>
  <ul>
    <li>Bars show when, not why then.</li>
    <li>Without links, every slip has to be worked out by hand, and usually isn't.</li>
    <li>Waits on things outside the project don't appear at all.</li>
  </ul>""",
    problem_figs=[nd_problem],
    analogy_side="getting dinner ready",
    analogy="""  <p>For a dinner party, the <b>oven must be hot before the roast goes in</b>: that's physics. The <b>table can be laid any time</b>: you usually do it before cooking, but that's a choice. And the <b>guests arrive at eight</b> because the invitation says so: that's outside your kitchen. A cook who knows which waits are which can rearrange the evening when the oven is slow. A cook with a list of times can't.</p>""",
    analogy_figs=[nd_analogy],
    map=[("Oven before roast", "Inspection before the cold room is energised (law)"),
         ("Laying the table", "Paint before shelving: a preference that could change"),
         ("Guests at eight", "The cold room's delivery on 27 March"),
         ("Curing time", "A lag: the screed must cure before anything stands on it"),
         ("A list of times", "Sanne's first bar chart")],
    how_side="boxes, arrows, and the kind of each wait",
    how="""  <p>On <b>19 February</b> Sanne and <b>Kees</b>, the builder's site manager, spend two hours at the empty unit with sticky notes. Twelve activities go on the wall, A to L, and arrows between them. Most are <b>finish-to-start</b>. Each wait gets a kind. <b>Mandatory</b>: walls after first fix; the cold room energised only after the electrical inspection; nothing stands on the floor until the screed has cured (Kees counts the curing inside D's seven days). <b>Discretionary</b>: paint before shelving, so shelves don't get splashed; it could be changed if needed. <b>External</b>: the cold room can't be built before it arrives on <b>27 March</b>. Now Joost's question has an answer: the inspection sits on a chain that runs straight to the handover. A week's slip there is a week's slip at the end.</p>""",
    how_figs=[nd_how],
    steps=[("List the activities from the work packages", "Verbs now: build, test, paint."),
           ("For each, ask: what must be finished first?", "Arrows, not dates."),
           ("Mark each wait: mandatory, discretionary, external", "Only discretionary ones can be changed cheaply."),
           ("Add lags where something must wait in between", "Curing, drying, notice periods."),
           ("Check every activity has a way in and a way out", "No loose ends."),
           ("Only then put durations and dates on it", "The next note.")],
    vocab=[("Dependency", "A relationship where one activity waits for another."),
           ("Finish-to-start (FS)", "B can't start until A finishes. The most common."),
           ("Start-to-start (SS)", "B can't start until A starts."),
           ("Mandatory dependency", "Required by physics, law or contract."),
           ("Discretionary dependency", "Chosen because it's usually best; could be changed."),
           ("External dependency", "A wait on something outside the project."),
           ("Lag", "A required wait between two activities, such as curing time.")],
    code=dict(file="rotterdam/23-fit-out-network.md", note="Sanne and Kees (builder), on site, 19 February 2026", plain=True, src="""
# ROTTERDAM FIT-OUT · ACTIVITIES AND WHAT EACH WAITS FOR (working days)

ID  ACTIVITY                              DAYS  WAITS FOR   KIND OF WAIT
A   strip-out                               3   -
B   electrical first fix                    4   A           mandatory
C   plumbing and drains                     3   A           mandatory
D   floor screed and curing                 7   C           mandatory (incl. 5 days' curing)
E   walls, ceiling, cold-room base          5   B           mandatory
F   electrical second fix                   4   E           mandatory
G   electrical inspection (inspector)       1   F           mandatory + external (booked
                                                            for Tue 24 Mar)
H   paint and finishes                      3   G, D        mandatory (G), mandatory (D)
I   cold-room build (supplier)              3   D           mandatory + external (delivery
                                                            Fri 27 Mar)
J   cold room energised, 48-hour test       2   I, G        mandatory (law: G before power)
K   shelving, fridges, chargers             3   H           discretionary (paint first)
L   snagging and clean                      2   K           mandatory
--  handover (Gate 1)                       0   J, L

JOOST'S QUESTION  inspection a week late? → it is on the chain to the handover:
                  the handover moves by the same week (see: critical path)
"""),
    tools="tools: sticky notes, a wall, the person who'll do the work, and three colours of pen for the kinds of wait.",
    dial=[("Light", "a few activities", ["Say what waits for what.", "A sketch with arrows.", "No tool."]),
          ("Standard", "Rotterdam's fit-out", ["A network of the predictive work, drawn with the supplier.", "Kinds of wait marked.", "External dates shown."]),
          ("Heavy", "large construction or engineering", ["A full precedence network in a scheduling tool.", "All four dependency types, leads and lags.", "Network checked for loose ends by a scheduler."])],
    baseline="Each line compares <b>a bar chart with dates and no links</b> to <b>a network of activities with each wait drawn and its kind marked</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "A slip's effect can be worked out at once."),
             (2, 5, "External waits (the delivery, the inspector) are visible."),
             (2, 4, "Anyone can follow the arrows."),
             (2, 4, "Joost gets an answer to “what if?”"),
             (3, 4, "The builder drew it with Sanne."),
             (2, 4, "Discretionary waits are options when time is short."),
             (3, 4, "Curing and testing waits can't be skipped by accident."),
             (3, 3, "Two hours on site.")],
    pitfalls=[("Bars without links", "Looks like a plan; can't answer “what if?”.", "draw the arrows first."),
              ("Loose ends", "An activity that leads nowhere.", "every box has a way in and out."),
              ("Treating a preference as a law", "No room to re-order when late.", "mark which waits are discretionary."),
              ("Forgetting outside waits", "Deliveries, inspectors, permits.", "draw them, with their dates.")],
    use=["Any predictive work with more than a handful of steps.", "Work with outside dates (deliveries, inspections).", "Before promising a date.", "When someone asks “what if X is late?”"],
    skip=["Adaptive work planned sprint by sprint: order the backlog instead."],
    related=["<b>How Do We Break It Down?</b> (this volume)", "<b>What Decides the Finish Date?</b> (next note)", "<b>Last responsible moment</b> (Ana, vol. 2)", "<b>Dependencies across teams</b> (Grace, vol. 5)"],
    quiz=[("What kind of wait is “paint before shelving”?", "Discretionary: usually best, but it could be changed."),
          ("And “cold room energised only after the inspection”?", "Mandatory (by law)."),
          ("What is a lag?", "A required wait between activities, like the screed's curing time."),
          ("Why couldn't Sanne answer Joost from the bar chart?", "It had no links, so it couldn't show which bars wait for the inspection."),
          ("The shelving supplier offers to deliver a week early. Does that help the handover?", "No: shelving waits for paint, not for its delivery. The arrow, not the delivery, sets its start.")],
    try_it="Take the predictive part of your project. Write each activity on a sticky note and draw what waits for what. Mark each arrow M (mandatory), D (discretionary) or E (external). Which E arrows have no date on them yet?",
    remember="The <span class=\"hl\">oven</span> before the roast; the <span class=\"hl\">guests</span> at eight. Know which wait is which.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, developing the schedule.",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019): the precedence diagramming method.",
             "James Kelley and Morgan Walker, “Critical-Path Planning and Scheduling” (1959)."],
)

# ------------------------------------------------------------------ 09 What Decides the Finish Date?
cp_problem = Doodle(760, 250, "Doodle of 20 February 2026. Twelve activities, and everyone has a favourite worry. Joost worries about the plumber. Tomás about the shelving. Marco about the cold room. Sanne asks a different question: of all these, which ones actually decide the handover date?",
                    "Everyone worries about a different activity. Which ones actually decide the date?")
cp_problem.row([("Joost", "the plumber", "paper"), ("Tomás", "the shelving", "paper"), ("Marco", "the cold room", "paper")], y=30, h=84, size=18, subsize=15)
cp_problem.note(380, 168, "twelve activities, twelve worries", "red", size=20)
cp_problem.note(380, 206, "which ones set the date?", "pen", size=19)

cp_analogy = Doodle(760, 240, "Doodle of a group walking to a picnic along different paths that meet at the same spot. The picnic starts when the slowest group arrives. Making a fast group walk faster changes nothing. Only the slowest path decides when lunch begins.",
                    "The picnic starts when the slowest group arrives. Hurrying the fast ones changes nothing.")
cp_analogy.box(560, 80, 180, 80, "the picnic", "green", sub="starts when all arrive", size=18, subsize=13)
for i, (t, f) in enumerate([("fast path", "paper"), ("slow path", "pink"), ("fast path", "paper")]):
    cp_analogy.box(20, 20 + i * 70, 200, 50, t, f, size=16)
    cp_analogy.arrow(222, 45 + i * 70, 558, 120, color=("red" if f == "pink" else ""))
cp_analogy.note(380, 226, "only the slowest path decides when lunch starts", "pen", size=17)

cp_how = Doodle(760, 340, "The critical path through the Rotterdam fit-out, worked out on 20 February 2026. Each activity shows its earliest start and finish in working days. The longest chain runs from strip-out through electrical first fix, walls, second fix, the inspection, paint, shelving and snagging: twenty-five working days, ending on Friday 3 April. Plumbing and the floor screed have four days to spare. The cold-room chain also ends on day twenty-five, held there by its delivery date.",
                "A-B-E-F-G-H-K-L: 25 working days, Mon 2 March → Fri 3 April. The inspection sits on it.", exact=True)
network(cp_how, crit=True, times=True, y0=40)

cp_deep1 = Doodle(760, 260, "How one activity box is read after the two passes. Top line: earliest start and earliest finish, from the forward pass. Bottom line: latest start and latest finish, from the backward pass. The difference is the float. For the inspection, G: earliest 17 to 17, latest 17 to 17, float zero: critical. For plumbing, C: earliest 4 to 6, latest 8 to 10, float four.",
                  "Forward pass gives the earliest dates, backward pass the latest. Latest minus earliest is the float.")
for i, (k, es, ef, ls, lf, f) in enumerate([("G · inspection", 17, 17, 17, 17, "pink"), ("C · plumbing", 4, 6, 8, 10, "blue")]):
    x = 60 + i * 360
    d = cp_deep1
    d.box(x, 30, 280, 150, None, f)
    d.head(x + 140, 60, k, size=18)
    d.text(x + 70, 100, f"ES {es}", size=17)
    d.text(x + 210, 100, f"EF {ef}", size=17)
    d.text(x + 70, 150, f"LS {ls}", size=17)
    d.text(x + 210, 150, f"LF {lf}", size=17)
    d.line(f"M{x + 10} 118 h260", thin=True)
    d.note(x + 140, 210, "float 0: critical" if ls == es else f"float {ls - es}", "red" if ls == es else "green", size=18)
cp_deep1.note(380, 246, "earliest from the forward pass · latest from the backward pass", "pen", size=15)

cp_deep2 = Doodle(760, 300, "What happened on 23 March 2026, on the builder's calendar. Planned: inspection Tuesday 24 March, paint 25 to 27, shelving 30 March to 1 April, snagging 2 and 3 April, handover Friday 3 April. The inspector re-books to Thursday 26 March: paint 27, 30, 31; shelving 1, 2, 3 April; Easter Monday 6 April is a day off; snagging 7 and 8; handover Wednesday 8 April. Two working days late, five calendar days. With the builder working Saturday 28 and Sunday 29 March, paint finishes on the 29th and handover is back on 3 April.",
                  "Two working days on the critical path, plus Easter Monday, made “five days late”. One weekend bought them back.")
days = [("24", 0), ("25", 0), ("26", 0), ("27", 0), ("28", 1), ("29", 1), ("30", 0), ("31", 0), ("1", 0), ("2", 0), ("3", 0), ("4", 1), ("5", 1), ("6", 2), ("7", 0), ("8", 0)]
for i, (t, kind) in enumerate(days):
    x = 150 + i * 37
    cp_deep2.text(x + 16, 30, t, "t t-soft", size=13)
    if kind:
        cp_deep2.box(x, 40, 33, 210, None, "paper" if kind == 1 else "pink", dash=True, rx=2)
cp_deep2.note(150 + 13 * 37 + 16, 268, "Easter Mon", "red", size=12)
rows_ = [("planned", {0: "G", 1: "H", 2: "H", 3: "H", 6: "K", 7: "K", 8: "K", 9: "L", 10: "L"}),
         ("inspector re-books", {2: "G", 3: "H", 6: "H", 7: "H", 8: "K", 9: "K", 10: "K", 14: "L", 15: "L"}),
         ("+ weekend 28–29", {2: "G", 3: "H", 4: "H", 5: "H", 6: "K", 7: "K", 8: "K", 9: "L", 10: "L"})]
for r, (label, cells) in enumerate(rows_):
    y = 54 + r * 64
    cp_deep2.text(14, y + 24, label, anchor="start", size=14)
    for i, a in cells.items():
        x = 150 + i * 37
        cp_deep2.box(x + 2, y, 29, 34, a, "pink" if a == "G" else ("green" if r == 2 and i in (4, 5) else "blue"), size=14, rx=4)
    cp_deep2.note(14, y + 50, "→ handover " + ["3 Apr", "8 Apr", "3 Apr"][r], "red" if r == 1 else "green", size=14, anchor="start")

CRITICAL = dict(
    slug="critical-path",
    kicker="a.k.a. the critical path method (CPM)",
    tldr="The <b>critical path</b> is the longest chain of dependent activities through a network. It decides the finish date: if any activity on it is late, the end is late by the same amount. Activities off it have <b>float</b> and can slip a little without harm. Find it with two passes, <b>forward</b> (earliest start and finish) and <b>backward</b> (latest), and watch it every week. Speeding up an activity that isn't on it buys <b>nothing</b>.",
    chips=[("Family", "by when?"), ("Lives in", "the network, with the critical chain marked in red"), ("Pairs with", "float and buffers, crashing, escalation")],
    pmbok=dict(covers="the critical path method: forward and backward passes, earliest and latest dates, the critical path and near-critical paths",
               domains=SCHED, processes=["Develop Schedule"], principles=["Adopt a holistic view", "Focus on value"], focus=["planning", "monitoring"],
               older="6th: the critical path method in 6.5 (Develop Schedule). 7th: the same, under the Planning domain."),
    problem_side="Larder, 20 February and 23 March 2026",
    problem="""  <p class="lead">With the network on the wall, everyone has a favourite worry. <b>Joost</b>: the plumber, who is slow. <b>Tomás</b>: the shelving, because Zuid's was late. <b>Marco</b>: the cold room, because it's the most expensive thing. <span class="hl-pink">Twelve activities, twelve worries, and only so much attention.</span> Sanne asks a different question: of all of these, which ones actually decide the handover date?</p>
  <ul>
    <li>Worry goes to what is slow, dear or familiar.</li>
    <li>The date is decided by something else: the longest chain.</li>
    <li>Effort spent on the wrong activity buys nothing.</li>
  </ul>""",
    problem_figs=[cp_problem],
    meanwhile=[("architect-2", "last-responsible-moment", "Ana's last responsible moment asks how late a decision can be taken without costing anything.",
                "Sanne asks the same of activities: the backward pass gives each one its latest start, and the critical ones have none to spare.")],
    analogy_side="the picnic",
    analogy="""  <p>Three groups walk to a picnic by different paths that meet at the same spot. The picnic starts when the <b>slowest group arrives</b>. Making a fast group walk faster changes nothing; they just wait longer at the blanket. If you want lunch earlier, there's only one path worth hurrying, and you'd better know which one it is.</p>""",
    analogy_figs=[cp_analogy],
    map=[("The slowest path", "A-B-E-F-G-H-K-L: 25 working days"),
         ("The picnic starts", "Handover, Friday 3 April"),
         ("A fast group", "Plumbing and the screed: 4 days to spare"),
         ("Hurrying the fast group", "Paying the plumber to rush"),
         ("A group that must leave at a set time", "The cold room: delivered 27 March")],
    how_side="two passes, then watch the red chain",
    how="""  <p>Sanne does the two passes by hand with Kees on <b>20 February</b> (the chapter below shows them). The <b>forward pass</b> gives every activity its earliest start and finish; the last finish is day <b>25</b>: Friday 3 April. The <b>backward pass</b>, from day 25, gives the latest each activity can start without moving it. Where earliest and latest are equal, there's no float: that's the <b>critical path</b>, <b>A-B-E-F-G-H-K-L</b>. The <b>electrical inspection</b> is on it. Joost's plumber isn't: plumbing and the screed have four days to spare. Marco's cold room is a special case: its chain also ends on day 25, held there by the delivery date, so it has no float either. Sanne marks the chain in red and from then on asks Kees one question every Thursday: is anything on the red chain moving? On <b>23 March</b> the answer is yes.</p>""",
    how_figs=[cp_how],
    steps=[("Put durations on the network", "From the three-point estimates."),
           ("Forward pass: earliest start and finish", "Left to right; take the latest of the predecessors."),
           ("Backward pass: latest start and finish", "Right to left; take the earliest of the successors."),
           ("Float = latest − earliest", "Zero float: critical."),
           ("Mark the critical path, and the near-critical ones", "A few days of float is near."),
           ("Watch it every week", "A slip on it is a slip at the end.")],
    vocab=[("Critical path", "The longest chain of dependent activities; it sets the end date."),
           ("Forward pass", "Calculating earliest start and finish from the beginning."),
           ("Backward pass", "Calculating latest start and finish from the end."),
           ("Float (slack)", "How much an activity can slip without moving the end date."),
           ("Near-critical path", "A chain with only a little float, which becomes critical easily."),
           ("Date constraint", "A fixed date (a delivery) that holds an activity in place.")],
    code=dict(file="rotterdam/24-critical-path.md", note="Sanne and Kees, 20 February 2026 · revisited 23 March", plain=True, src="""
# ROTTERDAM FIT-OUT · CRITICAL PATH (working days; day 1 = Mon 2 Mar)

ID  ACTIVITY              DAYS   EARLIEST   LATEST    FLOAT
A   strip-out               3     1 –  3     1 –  3     0   critical
B   first fix               4     4 –  7     4 –  7     0   critical
C   plumbing                3     4 –  6     8 – 10     4
D   screed + curing         7     7 – 13    11 – 17     4
E   walls, ceiling          5     8 – 12     8 – 12     0   critical
F   second fix              4    13 – 16    13 – 16     0   critical
G   inspection              1    17 – 17    17 – 17     0   critical   (Tue 24 Mar)
H   paint, finishes         3    18 – 20    18 – 20     0   critical
I   cold-room build         3    21 – 23    21 – 23     0   held by delivery (Fri 27 Mar)
J   energise + 48 h test    2    24 – 25    24 – 25     0
K   shelving, chargers      3    21 – 23    21 – 23     0   critical
L   snags, clean            2    24 – 25    24 – 25     0   critical
    HANDOVER                     day 25 = Fri 3 April

23 MARCH  inspector re-books G: Tue 24 → Thu 26 Mar (+2 working days, on the red chain)
          → H 27, 30, 31 Mar · K 1–3 Apr · Easter Monday 6 Apr off · L 7–8 Apr
          → HANDOVER Wed 8 Apr: 2 working days = 5 calendar days late → escalated
          → weekend work 28–29 Mar on H (change C-02): HANDOVER back to Fri 3 Apr
"""),
    tools="tools: the network, a pencil for the two passes (or a scheduling tool), and a red pen.",
    deep_dive=dict(
        side="the two passes by hand, what moves the path, and what the method ignores",
        intro="Scheduling tools do the critical path in a millisecond, which is why few people can check it. This chapter does Rotterdam's by hand, then looks at three things the textbook version leaves out: calendars, paths that change, and the limits of the method.",
        parts=[
            ("The forward pass", """  <p>Start at day 1. For each activity, the <b>earliest start</b> is the day after the latest of its predecessors finishes; the <b>earliest finish</b> is start + duration − 1.</p>
  <ul>
    <li>A starts day 1, finishes 3. B and C both wait for A: start 4. B finishes 7, C finishes 6.</li>
    <li>E waits for B: 8–12. D waits for C: 7–13. F waits for E: 13–16. G: 17.</li>
    <li>H waits for G (17) <b>and</b> D (13): take the later, so H starts 18 and finishes 20.</li>
    <li>I waits for D (13), but the cold room arrives on Friday 27 March, day 20: start 21, finish 23. J waits for I (23) and G (17): 24–25.</li>
    <li>K: 21–23. L: 24–25. Handover waits for J and L: day <b>25</b>.</li>
  </ul>""", []),
            ("The backward pass, and reading the result", """  <p>Start at the end, day 25, and walk backwards. For each activity, the <b>latest finish</b> is the day before the earliest of its successors' latest starts; the <b>latest start</b> is latest finish − duration + 1.</p>
  <ul>
    <li>L must finish by 25: start 24. K: 21–23. H: 18–20. G: 17. F: 13–16. E: 8–12. B: 4–7. A: 1–3.</li>
    <li>D has two successors: H (latest start 18) and I (21). Take the earlier: D must finish by 17, so it may start as late as 11. Its earliest start was 7: <b>4 days of float</b>. C, before it: latest 8–10, earliest 4–6: also 4.</li>
  </ul>
  <p>Wherever latest equals earliest, the float is zero and the activity is <b>critical</b>.</p>""", [cp_deep1]),
            ("Calendars: how two days became five", """  <p>The passes count <b>working days</b>. Dates come from laying those days on a <b>calendar</b>, and that's where 23 March got its sting. The inspector re-booked from Tuesday 24 to Thursday 26 March: two working days on the red chain. Laid on the builder's calendar, which has <b>Easter Monday, 6 April</b> off, the handover moved from Friday 3 April to <b>Wednesday 8 April</b>: two working days, <b>five calendar days</b>, over the three-day trigger.</p>
  <p>The same calendar showed the cure: the builder working <b>Saturday 28 and Sunday 29 March</b> adds two days to the red chain exactly where they're needed (crashing, three notes on).</p>""", [cp_deep2]),
            ("Paths that change, and what the method ignores", """  <ul>
    <li><b>Near-critical paths.</b> C-D has 4 days of float. If the screed cures five days late, D becomes critical and pushes H. Watch chains with little float, not just the red one.</li>
    <li><b>Paths become critical when you speed others up.</b> After the weekend work, the builder's chain and the cold-room chain <b>both</b> end on day 25. No money could now bring the handover before 3 April: the delivery date holds it.</li>
    <li><b>Resources.</b> The method assumes people are there when the arrows allow. Rotterdam's first and second fix use the same electrician crew, which is fine because they're in sequence; two activities needing one crew at the same time would need re-planning (resource levelling, vol. 4).</li>
    <li><b>Adaptive work</b> has no critical path. The app's milestone (20 April) is fixed; the team manages scope inside it.</li>
  </ul>""", []),
        ]),
    dial=[("Light", "a short chain", ["Find the longest chain by eye.", "Watch that chain.", "No passes."]),
          ("Standard", "Rotterdam's fit-out", ["Two passes, by hand, with the supplier.", "Critical and near-critical marked.", "A weekly question: is anything red moving?"]),
          ("Heavy", "large schedules", ["A scheduling tool with calendars and constraints.", "Critical path and float reports weekly.", "Schedule health checks by a scheduler."])],
    baseline="Each line compares <b>worrying about whichever activity feels risky</b> to <b>finding and watching the chain that decides the end date</b>.",
    ratings=[(3, 4, "Attention goes where the date is decided."),
             (2, 5, "A slip's effect on the end is known at once."),
             (2, 5, "The inspection was watched, and the slip caught the same day."),
             (2, 4, "The red chain is on the wall."),
             (3, 4, "Joost's plumber worry was answered with a number."),
             (3, 4, "Kees worked out the passes with Sanne."),
             (3, 4, "Float shows where there's room to re-order."),
             (3, 3, "Neutral."),
             (3, 3, "An afternoon, then one question a week.")],
    pitfalls=[("Hurrying the wrong activity", "Paying the plumber to rush.", "only the critical path moves the end."),
              ("Forgetting the calendar", "Two days became five.", "lay working days on the real calendar."),
              ("Watching only the red chain", "A near-critical one overtakes it.", "watch anything with little float."),
              ("Trusting the tool blindly", "Missing links make a short, wrong path.", "check one pass by hand.")],
    use=["Predictive work with a fixed end date.", "Before deciding where to spend effort or money.", "Every week while the work runs.", "When a slip is reported."],
    skip=["Adaptive work: manage scope against a fixed date instead."],
    related=["<b>What Waits for What?</b> (previous note)", "<b>How Much Can This Slip?</b> (next note)", "<b>Can We Go Faster?</b> (this volume)", "<b>When Do I Take It Upstairs?</b> (vol. 2)"],
    quiz=[("What is the critical path?", "The longest chain of dependent activities: it sets the end date."),
          ("Is the plumbing critical?", "No: it has 4 days of float."),
          ("Why did a two-day slip make the handover five days late?", "Two working days on the critical path, and Easter Monday was a day off for the builder: 3 April became 8 April."),
          ("Joost offers the plumber a bonus to finish two days early. What does it buy?", "Nothing for the handover: plumbing isn't on the critical path."),
          ("After the weekend work, could more money bring the handover before 3 April?", "No: the cold-room chain also ends on day 25, held by its delivery date.")],
    try_it="Take your project's predictive work. Do a forward and a backward pass, by hand, on the eight to twelve biggest activities. Which chain is critical? Is the thing everyone worries about on it?",
    remember="The picnic starts when the <span class=\"hl\">slowest group</span> arrives. Hurry <span class=\"hl\">that</span> one.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, developing the schedule.",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019).",
             "James Kelley and Morgan Walker, “Critical-Path Planning and Scheduling” (1959).",
             "Eliyahu Goldratt, <i>Critical Chain</i> (1997): resources and buffers."],
)

# ------------------------------------------------------------------ 10 How Much Can This Slip?
fb_problem = Doodle(760, 250, "Doodle of 24 February 2026. The plumber phones: can he start a week later? He has another job. Joost says no, everything is tight. Kees says yes, plumbing has float. Both are partly right, and nobody knows how much of the float the plumber may take before the screed has none left.",
                    "“Can the plumber start a week late?” Joost says no, Kees says yes. Whose float is it?")
fb_problem.box(20, 40, 210, 80, "plumber", "paper", sub="“a week later?”", size=19, subsize=15)
fb_problem.box(275, 40, 210, 80, "Joost: no", "pink", sub="“everything is tight”", size=19, subsize=14)
fb_problem.box(530, 40, 210, 80, "Kees: yes", "green", sub="“plumbing has float”", size=19, subsize=14)
fb_problem.note(380, 176, "a week is five days; the float is four, and the screed shares it", "red", size=17)
fb_problem.note(380, 214, "whose float is it?", "pen", size=19)

fb_analogy = Doodle(760, 240, "Doodle of a family sharing a bathroom in the morning before school. There are thirty spare minutes between waking and leaving. If the first person takes all thirty, the last person is late, even though everyone used only spare time. Spare time on a shared path belongs to the whole path.",
                    "Thirty spare minutes in the morning. If the first person uses all of them, the last one is late.")
fb_analogy.row([("first: +30 min", "“I had spare time”", "pink"), ("second: on time", None, "paper"), ("third: late", "no spare left", "pink")], y=50, h=90, gap=34, size=17, subsize=13, arrows=True)
fb_analogy.note(380, 196, "spare time on a shared chain belongs to the chain", "pen", size=18)

fb_how = Doodle(760, 330, "The float in the Rotterdam fit-out, 24 February 2026. Plumbing, C, and the screed, D, share four days of total float. D also has four days of free float: it can slip four days without delaying anything else. C has no free float: any slip in plumbing eats the screed's float. The cold-room chain has no float, held by the delivery. The project as a whole has no buffer between the handover and stocking.",
                "C and D share four days. C has no free float of its own: any slip there uses the screed's.", exact=True)
network(fb_how, floats=True)

FLOAT = dict(
    slug="float-and-buffers",
    kicker="a.k.a. total float, free float and schedule buffers",
    tldr="<b>Float</b> is how late an activity can be without moving something else. <b>Total float</b>: without moving the end date. <b>Free float</b>: without moving the next activity. Float on a chain is <b>shared</b>: whoever uses it first takes it from everyone after. A <b>buffer</b> is different: slack you add <b>on purpose</b>, visible, owned by the project manager, instead of hiding it inside estimates. Know where your float is, decide who may use it, and say plainly when there's none.",
    chips=[("Family", "by when?"), ("Lives in", "a float column next to the critical path; a buffer line in the plan"), ("Pairs with", "critical path, three-point estimates, last responsible moment")],
    pmbok=dict(covers="total and free float; using float; schedule buffers (project and feeding buffers); contingency in the schedule",
               domains=SCHED + ["risk"], processes=["Develop Schedule"], principles=["Be an accountable leader"], focus=["planning", "monitoring"],
               older="6th: total and free float in 6.5; contingency reserves for duration in 6.4; critical chain buffers in 6.5. 7th: the same ideas under Planning."),
    problem_side="Larder, 24 February 2026",
    problem="""  <p class="lead">The plumber phones: could he start <b>a week later</b>? He has another job finishing. <b>Joost</b>: no, everything is tight. <b>Kees</b>: yes, plumbing has float. <span class="hl-pink">Both are partly right.</span> Plumbing does have float, four days of it. But a week is five working days, and the four days aren't the plumber's alone: the floor screed comes after him, and it needs them too.</p>
  <ul>
    <li>“There's float” is heard as “there's time”.</li>
    <li>Float on a chain is shared, and the first to use it takes it.</li>
    <li>Nobody knows how much slack the whole project has. (None.)</li>
  </ul>""",
    problem_figs=[fb_problem],
    analogy_side="the morning bathroom",
    analogy="""  <p>A family has <b>thirty spare minutes</b> between waking up and leaving for school. If the first person spends all thirty in the bathroom, the last person is late, even though nobody used anything but “spare” time. Spare time on a shared path belongs to <b>the whole path</b>. A sensible family says who gets how much, and keeps ten minutes nobody may touch.</p>""",
    analogy_figs=[fb_analogy],
    map=[("Thirty spare minutes", "Four days of total float on plumbing and the screed"),
         ("The first person", "The plumber, who comes first in the chain"),
         ("The last person, late", "The screed, if the plumber takes all four"),
         ("Ten minutes nobody may touch", "A buffer, owned by the project manager"),
         ("A family with no spare time", "Rotterdam's project: no buffer before stocking")],
    how_side="total and free float, who may use it, and an honest “no buffer”",
    how="""  <p>Sanne reads the float column with Kees. <b>Total float</b>: plumbing (C) and the screed (D) can each slip <b>four days</b> without moving the handover. <b>Free float</b> is the catch: the screed has four of its own, but plumbing has <b>none</b>. Any day the plumber slips is taken from the screed. So the answer is <b>two days, not five</b>: the plumber may start two days later, leaving two for the screed, which is the activity that can go wrong in a cold March. Kees agrees; the plumber agrees. And Sanne writes down the bigger fact the float column shows: the cold-room chain has none, the builder's chain has none, and there is <b>no buffer</b> between the handover and stocking. She asks the cold-room supplier to deliver two days early to create one; they can't (the panels leave the factory on the 26th). So she books a <b>confirmation call for 20 March</b> instead: an early warning where she couldn't buy a buffer.</p>""",
    how_figs=[fb_how],
    steps=[("Read total float for every activity", "From the two passes."),
           ("Read free float too", "That's what an owner can use alone."),
           ("Decide who may use shared float", "Usually the riskier activity later in the chain."),
           ("Look for chains with none", "Critical, or held by a fixed date."),
           ("Add buffers on purpose, where you can", "Visible, owned by you."),
           ("Where you can't buy a buffer, buy an early warning", "A check before the date.")],
    vocab=[("Total float", "How long an activity can slip without moving the end date."),
           ("Free float", "How long it can slip without moving the next activity."),
           ("Shared float", "Float that belongs to a chain, not to one activity."),
           ("Buffer", "Slack added on purpose and managed openly."),
           ("Project buffer", "A buffer before the final date."),
           ("Feeding buffer", "A buffer where a side chain joins the critical path.")],
    code=dict(file="rotterdam/25-float.md", note="Sanne and Kees, 24 February 2026", plain=True, src="""
# ROTTERDAM FIT-OUT · FLOAT AND BUFFERS (working days)

ACTIVITY              TOTAL FLOAT  FREE FLOAT  NOTE
C  plumbing                4           0       any slip takes the screed's float
D  screed + curing         4           4       the riskier one (cold March)
I  cold-room build         0           0       held by delivery, Fri 27 Mar
J  energise + test         0           0
all others                 0           0       the critical path

PLUMBER'S REQUEST (start a week = 5 days later)  → may start 2 days later (Mon 9 Mar)
                                                   2 days left for the screed
BUFFERS
  project buffer     none: handover 3 Apr, stocking from 6 Apr (the plan's weak point)
  feeding buffer     asked supplier for delivery Wed 25 Mar (2 days) → not possible
                     → instead: confirmation call Fri 20 Mar (early warning)
  weekend work       priced in advance: one weekend ≈ €5,000 (builder, 12 Feb)
"""),
    tools="tools: the float column from the two passes, and the discipline to say who owns each day of it.",
    dial=[("Light", "small work", ["Ask “how much can this slip?” before saying yes.", "Keep a little slack before the deadline.", "Said, not written."]),
          ("Standard", "Rotterdam", ["Total and free float read with the supplier.", "Shared float allocated.", "Buffers or early warnings where float is zero."]),
          ("Heavy", "large schedules", ["Float reports and float erosion trends.", "Formal schedule contingency.", "Critical-chain project and feeding buffers."])],
    baseline="Each line compares <b>“there's float, so there's time”</b> to <b>total and free float read, shared float allocated, and buffers or early warnings where there's none</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "Shared float is no longer used up by whoever asks first."),
             (2, 4, "The riskier activity keeps its slack."),
             (2, 4, "“No buffer” is written, not discovered."),
             (3, 4, "The plumber and the builder both agreed the answer."),
             (3, 4, "Kees helped decide how float is used."),
             (3, 4, "Float is used on purpose, for real requests."),
             (3, 3, "Neutral."),
             (4, 4, "A column and a conversation.")],
    pitfalls=[("Float as free time", "“There's float, so yes.”", "check free float, and who comes after."),
              ("Padding estimates instead of buffers", "Hidden slack gets used anyway.", "honest estimates, visible buffers."),
              ("No buffer, not said", "Discovered in April.", "write “no buffer” as a weak point."),
              ("Nothing where you can't buy slack", "A surprise on the day.", "an early-warning check instead.")],
    use=["When someone asks to start late or finish late.", "When a chain has a fixed date in it.", "Before promising a date.", "When float is getting used up week by week."],
    skip=["Adaptive work: protect the sprint goal and the milestone instead."],
    related=["<b>What Decides the Finish Date?</b> (previous note)", "<b>How Sure Are We?</b> (this volume)", "<b>Last responsible moment</b> (Ana, vol. 2)", "<b>Contingency vs management reserve</b> (vol. 5)"],
    quiz=[("Total float or free float: how long can the screed slip without moving the next activity?", "Free float: four days."),
          ("Why may the plumber only start two days late, not five?", "Plumbing has no free float; its four days of total float are shared with the screed, which is riskier and needs some."),
          ("What's a buffer?", "Slack added on purpose, visible and owned by the project manager."),
          ("The supplier couldn't deliver early. What did Sanne do instead?", "A confirmation call on 20 March: an early warning where she couldn't buy a buffer."),
          ("On 10 March the screed contractor says the floor will cure two days slower in the cold. Does the handover move?", "No: the plumber started two days late, which left two days of float, and the screed has just used them. Now that chain has none left either.")],
    try_it="For your project's critical deadline, write the float of the five activities nearest it. Which ones share float? Who should get it? Is there any buffer you could add on purpose, or an early warning you could book?",
    remember="Spare time on a <span class=\"hl\">shared path</span> belongs to the <span class=\"hl\">whole path</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain.",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019): total and free float.",
             "Eliyahu Goldratt, <i>Critical Chain</i> (1997): project and feeding buffers."],
)

# ------------------------------------------------------------------ 11 How Do We Show the Dates?
gm_problem = Doodle(760, 250, "Doodle of the steering group of 27 February 2026, where Sanne's detailed chart goes up on the screen: twelve bars for the builder, five workstreams, sprints and deliveries, nearly two hundred lines. Femke squints and asks one thing: are we opening on 27 April? The chart has the answer somewhere. Nobody can find it.",
                    "Two hundred lines on the screen. Femke asks one thing: are we opening on 27 April?")
for i in range(9):
    gm_problem.box(30 + (i % 4) * 40, 26 + i * 16, 140, 10, None, "blue", rx=2)
gm_problem.box(400, 40, 340, 90, "Femke", "y", sub="“are we opening on 27 April?”", size=19, subsize=15)
gm_problem.note(200, 200, "the answer is in there somewhere", "red", size=17)
gm_problem.note(570, 176, "one question, one level", "pen", size=18)

gm_analogy = Doodle(760, 240, "Doodle of three maps of the same journey. A country map with the cities on it, for deciding where to go. A road map with the route, for the driver. A street plan of the last kilometre, for finding the door. Nobody hands the passenger the street plan to ask whether they'll arrive tonight.",
                    "A country map, a road map and a street plan of the same journey. Each for a different person.")
gm_analogy.row([("country map", "where, roughly when", "y"), ("road map", "the route", "blue"), ("street plan", "the last kilometre", "green")], y=50, h=90, size=18, subsize=14)
gm_analogy.note(132, 186, "steering group", "red", size=17)
gm_analogy.note(380, 186, "the leads", "red", size=17)
gm_analogy.note(628, 186, "the builder", "red", size=17)

gm_how = Doodle(760, 400, "The fit-out as a Gantt chart drawn from the network, February 2026. Twelve bars over twenty-five working days, from 2 March to 3 April. The critical activities in red, plumbing and the screed with their four days of float shown dotted, the cold room starting when it is delivered on 27 March, and a diamond for the handover on 3 April. Above it, for the steering group, the same project as five milestones.",
                "The builder's Gantt, generated from the network, critical bars in red and float dotted. The steering group sees five diamonds.")
x0, px = 190, 22
for w, t in enumerate(["2 Mar", "9 Mar", "16 Mar", "23 Mar", "30 Mar"]):
    gm_how.text(x0 + w * 5 * px + 4, 22, t, "t t-soft", anchor="start", size=13)
    gm_how.line(f"M{x0 + w * 5 * px} 30 V336", thin=True, dash=True)
for i, k in enumerate("ABCDEFGHIJKL"):
    y = 36 + i * 24
    gm_how.text(14, y + 15, f"{k} {ACT[k][0]}", anchor="start", size=13)
    s, e = ES[k], EF[k]
    on = k in CRIT
    gm_how.box(x0 + (s - 1) * px, y, (e - s + 1) * px - 2, 16, None, "pink" if on else "blue", stroke="red" if on else "", rx=3)
    if k in TF:
        gm_how.box(x0 + e * px, y, TF[k] * px - 2, 16, None, "paper", dash=True, rx=3)
gm_how.raw(f'<path class="d f-red" d="M{x0 + 25 * px} 326 l9 9 l-9 9 l-9 -9 z"/>')
gm_how.note(x0 + 25 * px - 14, 340, "hand-over", "red", size=13, anchor="end")
gm_how.note(380, 376, "red = critical · dotted = float · the bars come from the network, not drawn by hand", "pen", size=14)

GANTT = dict(
    slug="gantt-and-milestones",
    kicker="a.k.a. presenting the schedule: Gantt charts, milestone charts, levels of detail",
    tldr="A schedule has different readers who need different <b>levels</b>. The people who decide need a <b>milestone chart</b>: a few dates that matter, and whether they're holding. The people who co-ordinate need a <b>summary</b> by workstream. The people who do the work need the <b>detailed Gantt chart</b>: bars on a calendar. Draw every level <b>from the same network</b>, so they can never disagree, and show each audience only the level it needs.",
    chips=[("Family", "by when?"), ("Lives in", "three views of one schedule: milestones, summary, detail"), ("Pairs with", "the network, roadmap vs release plan, status reports")],
    pmbok=dict(covers="presenting the schedule: Gantt (bar) charts, milestone charts, summary and detailed schedules, the schedule baseline",
               domains=SCHED + ["stakeholders"], processes=["Develop Schedule"], principles=["Adopt a holistic view"], focus=["planning", "monitoring"],
               older="6th: bar charts, milestone charts and project schedule network diagrams as outputs of 6.5. 7th: schedules as artefacts in the Planning domain."),
    problem_side="Larder, 20–27 February 2026",
    problem="""  <p class="lead">At the steering group of 27 February, Sanne's full schedule goes up on the screen: the builder's twelve bars, five other workstreams, sprints, deliveries, training groups. Nearly <b>two hundred lines</b>. Femke squints and asks one question: <b>“are we opening on 27 April?”</b> <span class="hl-pink">The answer is on the chart, somewhere.</span> Nobody in the room can find it, and the next ten minutes are spent on a bar for chargers.</p>
  <ul>
    <li>One chart for every audience serves none of them.</li>
    <li>Detail drags the meeting down to the wrong level.</li>
    <li>Charts drawn by hand drift away from the plan.</li>
  </ul>""",
    problem_figs=[gm_problem],
    meanwhile=[("product-2", "roadmap-vs-release-plan", "on 9 March Grace and Sanne separate the roadmap (outcomes, for Priya) from the release plan (R1, R2, R3, for the teams).",
                "Sanne had made the same split for the schedule two weeks earlier: milestones for the steering group, Gantt charts for the people doing the work.")],
    analogy_side="three maps of one journey",
    analogy="""  <p>For one journey you might carry three maps. A <b>country map</b> with the cities on it, for deciding where to go and roughly when. A <b>road map</b> with the route, for the driver. A <b>street plan</b> of the last kilometre, for finding the door. All three show the same journey. Nobody hands the passenger the street plan to ask whether they'll arrive tonight.</p>""",
    analogy_figs=[gm_analogy],
    map=[("The country map", "The milestone chart: five dates, for the steering group"),
         ("The road map", "The summary schedule: seven workstreams, for Thursday's leads"),
         ("The street plan", "The builder's Gantt: twelve activities, for the site"),
         ("Same journey", "All three generated from one network"),
         ("“Will we arrive tonight?”", "“Are we opening on 27 April?”")],
    how_side="one network, three views, each for its reader",
    how="""  <p>From the steering group of 13 March on, Femke sees <b>five diamonds</b>: fit-out done 3 April, stock in 17 April, app ready 20 April, go / no-go 24 April, opening 27 April, each with its baseline date, its forecast and a colour. The Thursday leads see a <b>summary</b>: one bar per workstream, the shared milestones, and the links between workstreams. Kees and his crew get the <b>detailed Gantt</b> for the fit-out: twelve bars over 25 working days, critical ones in red, float dotted, the cold room's bar starting on its delivery date. All three are <b>generated from the same network</b> in a scheduling tool, so a change on site moves the diamonds too. The adaptive teams don't get a Gantt at all: their view is the sprint board and the must-have burn-up.</p>""",
    how_figs=[gm_how],
    steps=[("Build one network; generate every view from it", "Never redraw dates by hand."),
           ("Give decision-makers milestones", "Five to ten, with baseline, forecast and colour."),
           ("Give co-ordinators a summary", "A bar per workstream, the shared milestones."),
           ("Give doers the detail", "Activities, the critical path, float."),
           ("Mark today on every view", "And what has moved."),
           ("Show adaptive work in its own form", "Boards and burn-ups, not bars.")],
    vocab=[("Gantt chart", "A bar chart of activities against a calendar."),
           ("Milestone", "A point in time when something important is finished; zero duration."),
           ("Milestone chart", "A schedule showing only milestones."),
           ("Summary schedule", "A higher-level schedule, a bar per workstream or phase."),
           ("Schedule baseline", "The approved version of the schedule."),
           ("Today line", "A vertical line marking the current date.")],
    code=dict(file="rotterdam/26-milestone-chart.md", note="for the steering group, from 13 March 2026 (shown here: 13 March)", plain=True, src="""
# ROTTERDAM · MILESTONES (generated from the schedule; three views, one network)

MILESTONE                 BASELINE      FORECAST     STATUS   OWNER
G1 fit-out done           Fri  3 Apr    Fri  3 Apr   green    Joost (builder)
G2 stock on shelves       Fri 17 Apr    Fri 17 Apr   green    Tomás
G3 app ready              Mon 20 Apr    Mon 20 Apr   green    Grace
G4 go / no-go             Fri 24 Apr    Fri 24 Apr   green    steering group
OPENING                   Mon 27 Apr    Mon 27 Apr   green    Joost
G5 hypercare exit         Mon 11 May    Mon 11 May   green    Joost

THE THREE VIEWS
  steering group  this table (6 lines), every 2nd Friday
  the leads       summary: a bar per workstream + shared milestones, Thursdays 09:30
  the builder     detailed Gantt: activities A–L, critical path red, float dotted
  adaptive teams  sprint boards + must-haves burn-up (no Gantt)
"""),
    tools="tools: a scheduling tool (or a spreadsheet) fed from the network, and the discipline to show each reader one view.",
    dial=[("Light", "a small project", ["A list of three to five dates.", "A simple bar chart if it helps.", "Updated by hand."]),
          ("Standard", "Rotterdam", ["Milestones, summary and detail.", "All from one network.", "A view per audience."]),
          ("Heavy", "large programmes", ["Integrated master schedule in a tool.", "Standard levels (1 to 4) of schedule.", "Automatic reports per stakeholder group."])],
    baseline="Each line compares <b>one detailed chart for every audience</b> to <b>three views of one network: milestones, summary and detail</b>.",
    ratings=[(3, 4, "The steering group talks about the dates that matter."),
             (3, 4, "One network means the views never disagree."),
             (3, 3, "Neutral."),
             (2, 5, "Each reader finds their answer quickly."),
             (2, 4, "Femke gets her answer in five lines."),
             (3, 4, "Kees's crew has the detail they use."),
             (3, 4, "A site change moves the diamonds automatically."),
             (3, 3, "Neutral."),
             (3, 4, "Generated, not redrawn.")],
    pitfalls=[("The 200-line slide", "Nobody finds the answer.", "milestones for those who decide."),
              ("Hand-drawn Gantts", "They drift from the plan.", "generate every view from the network."),
              ("Milestones without forecasts", "Only the baseline, forever green.", "baseline and forecast side by side."),
              ("A Gantt for sprints", "Fake precision.", "boards and burn-ups for adaptive work.")],
    use=["Every project with more than one audience.", "Steering groups and sponsors: milestones.", "Site and suppliers: detailed Gantt.", "Whenever someone asks “when?”"],
    skip=["A single-team project: one simple view is enough."],
    related=["<b>Roadmap vs release plan</b> (Grace, vol. 2)", "<b>Where Are We, Really?</b> (vol. 2)", "<b>What Waits for What?</b> (this volume)", "<b>Are We Still on Time?</b> (this volume)"],
    quiz=[("Which view does the steering group get?", "The milestone chart."),
          ("Why generate every view from one network?", "So they can never disagree, and a change moves all of them."),
          ("What is a milestone's duration?", "Zero: it's a point in time."),
          ("Kees asks for the milestone chart instead of the Gantt. What's wrong with that?", "He'd lose the activities, the critical path and the float he needs to run the site."),
          ("Ben asks for a Gantt of his sprints. What does Sanne offer instead?", "The sprint board and the burn-up of must-haves; bars would pretend to know the order of work that's decided each sprint.")],
    try_it="Write down who reads your schedule. For each reader, sketch the one view they need, at the right level. Are all of them generated from the same plan?",
    remember="A <span class=\"hl\">country map</span> for those who decide, a <span class=\"hl\">street plan</span> for those who drive.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain.",
             "Henry Gantt, <i>Work, Wages, and Profits</i> (1910).",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019): schedule levels and presentation."],
)

# ------------------------------------------------------------------ 12 Can We Go Faster?
cf_problem = Doodle(760, 250, "Doodle of the afternoon of 23 March 2026. The handover is forecast for 8 April, five days late. Everyone has an idea for going faster: Joost wants to pay the plumber, Marco wants the cold-room fitters on Saturday, Tomás wants to start stocking in the finished half of the store. Some ideas cost money and buy nothing.",
                    "Five days late, and everyone has an idea for going faster. Some cost money and buy nothing.")
cf_problem.row([("pay the plumber", "Joost", "paper"), ("cold room on Sat", "Marco", "paper"), ("stock half the store", "Tomás", "paper")], y=30, h=84, size=16, subsize=14)
cf_problem.note(380, 168, "which of these moves 8 April?", "red", size=20)
cf_problem.note(380, 206, "only work on the critical path can", "pen", size=18)

cf_analogy = Doodle(760, 240, "Doodle of a family late for a train. They can pay for a taxi instead of the bus: faster, and it costs money. Or they can pack in the car on the way instead of before leaving: faster, free, and something might get left behind. Paying to speed up is crashing; overlapping steps is fast-tracking.",
                    "Late for a train: pay for a taxi (crashing), or pack in the car on the way (fast-tracking).")
cf_analogy.box(20, 40, 330, 100, "take a taxi", "y", sub="faster · costs money", size=20, subsize=15)
cf_analogy.box(410, 40, 330, 100, "pack in the car", "blue", sub="faster · free · something left behind?", size=20, subsize=14)
cf_analogy.note(185, 180, "crashing", "red", size=20)
cf_analogy.note(575, 180, "fast-tracking", "red", size=20)

cf_how = Doodle(760, 400, "The options Sanne lays out on 23 March 2026, each tested against the critical path. Pay the plumber: not critical, already done; buys nothing. Cold-room fitters on Saturday: the cold-room chain is not late; buys nothing. Electrician faster: the inspector's date can't be moved; impossible. Builder works the weekend of 28 and 29 March on paint and finishes: two days, five thousand euros, two and a half thousand a day; handover back on 3 April. Start stocking in the dry half while the chilled half is finished: two days, no cost, but pickers and builders share the store, as at Zuid. Crashing is chosen.",
                "Only work after the inspection, on the critical path, can be shortened. Crashing it costs €2,500 a day.")
opts = [("pay the plumber", "not critical, already done", "buys 0", "paper"),
        ("cold-room fitters, Sat", "chain not late", "buys 0", "paper"),
        ("faster electrician", "inspector's date is fixed", "impossible", "paper"),
        ("crash: weekend 28–29", "paint on Sat + Sun · €5,000", "2 days · €2.5k/day", "green"),
        ("fast-track: stock dry half", "pickers among builders", "2 days · €0 · risky", "y")]
for i, (t, s, r, f) in enumerate(opts):
    y = 14 + i * 64
    cf_how.box(14, y, 260, 54, t, f, size=16)
    cf_how.text(290, y + 33, s, anchor="start", size=15)
    cf_how.box(560, y, 186, 54, r, "pink" if r in ("buys 0", "impossible") else f, size=13)
cf_how.note(380, 370, "chosen: crash (change C-02). Fast-track kept as a fallback.", "green", size=17)

CRASH = dict(
    slug="crashing-and-fast-tracking",
    kicker="a.k.a. schedule compression: crashing and fast-tracking",
    tldr="Two ways to shorten a schedule without cutting scope. <b>Crashing</b>: add money or people to activities <b>on the critical path</b> (overtime, weekend work, extra crews), cheapest days first. <b>Fast-tracking</b>: overlap activities that were planned in sequence, which is usually free but adds risk and rework. Both only help on the critical path, and both stop helping when another path becomes critical. Spend nothing on activities that aren't.",
    chips=[("Family", "by when?"), ("Lives in", "a short table of options: days gained, cost per day, risk"), ("Pairs with", "critical path, escalation, change control")],
    pmbok=dict(covers="schedule compression: crashing (time-cost trade-offs) and fast-tracking (overlapping activities), and their limits",
               domains=SCHED + ["finance", "risk"], processes=["Develop Schedule"], principles=["Focus on value"], focus=["planning", "monitoring"],
               older="6th: crashing and fast-tracking as schedule compression in 6.5. 7th: the same, in the Planning domain."),
    problem_side="Larder, 23 March 2026",
    problem="""  <p class="lead">The inspector has re-booked, and the handover is forecast for <b>8 April</b>. Within the hour, everyone has an idea. <b>Joost</b>: pay the plumber a bonus. <b>Marco</b>: have the cold-room fitters work Saturday. <b>Tomás</b>: start stocking in the finished half of the store. <b>Ben</b>, half joking: get a faster electrician. <span class="hl-pink">Some of these cost money and buy nothing.</span> Sanne has two hours before her message to Joost.</p>
  <ul>
    <li>Ideas for speed rarely start from the critical path.</li>
    <li>Money spent off the path disappears.</li>
    <li>Overlapping steps is free until it isn't.</li>
  </ul>""",
    problem_figs=[cf_problem],
    analogy_side="late for a train",
    analogy="""  <p>A family is late for a train. They can <b>pay for a taxi</b> instead of the bus: faster, and it costs money. Or they can <b>pack in the car on the way</b> instead of before leaving: faster and free, but something might get left behind. Either works only on the part of the journey that's actually making them late. A taxi doesn't help if the problem is the queue at the ticket office.</p>""",
    analogy_figs=[cf_analogy],
    map=[("The taxi", "Crashing: the builder works the weekend of 28–29 March"),
         ("Packing in the car", "Fast-tracking: stocking the dry half while the rest is finished"),
         ("Something left behind", "Pickers and builders sharing the floor, as at Zuid"),
         ("The ticket-office queue", "The inspector's date: no money moves it"),
         ("A taxi on the wrong leg", "A bonus for the plumber")],
    how_side="test each idea against the critical path, then price the days",
    how="""  <p>Sanne tests each idea against the <b>red chain</b>. The plumber: <b>not critical</b>, and finished two weeks ago. The cold-room fitters: their chain isn't late; working Saturday moves nothing. A faster electrician: the delay is the <b>inspector's date</b>, which no money moves. What can be shortened is the work <b>after</b> the inspection: paint, shelving and snagging, on the critical path. Two options. <b>Crash</b>: the builder works <b>Saturday 28 and Sunday 29 March</b> on paint and finishes: two days for <b>€5,000</b>, €2,500 a day, priced in February. <b>Fast-track</b>: start stocking the dry half while the chilled half is finished: two days, no cost, but pickers working among builders, which is how Zuid went wrong. She recommends crashing, keeps fast-tracking as a fallback, and notes the limit: after the weekend, the cold-room chain is critical too, so <b>3 April is as early as money can make it</b>. Joost decides at 16:00 (change C-02).</p>""",
    how_figs=[cf_how],
    steps=[("List every idea for going faster", "From everyone."),
           ("Strike out anything off the critical path", "It buys nothing."),
           ("Strike out anything outside your control", "The inspector's date."),
           ("Price each remaining day", "Cost per day gained."),
           ("Weigh fast-tracking's risk honestly", "Free isn't free if it causes rework."),
           ("Check the new critical path after each step", "Stop when another path takes over.")],
    vocab=[("Schedule compression", "Shortening the schedule without reducing scope."),
           ("Crashing", "Adding resources (money, people, overtime) to critical activities."),
           ("Fast-tracking", "Doing activities in parallel that were planned in sequence."),
           ("Cost per day", "The price of each day gained by crashing."),
           ("Crash limit", "The point where an activity can't be shortened further."),
           ("Rework", "Work done again because something was done too early or wrong.")],
    code=dict(file="rotterdam/27-going-faster.md", note="Sanne's options, 23 March 2026 (sent to Joost at 11:40)", plain=True, src="""
# ROTTERDAM FIT-OUT · CAN WE GO FASTER? (handover forecast Wed 8 Apr; need Fri 3 Apr)

IDEA                               ON CRITICAL PATH?        DAYS GAINED  COST     RISK
pay the plumber a bonus            no (C, done 11 Mar)       0            -        -
cold-room fitters on Saturday      no (chain not late)      0            -        -
faster electrician                 the delay is G's date    0            -        -
                                   (inspector): fixed
CRASH: builder works 28–29 Mar     yes (H, paint)           2            €5,000   low
       on paint and finishes                                             (€2,500
                                                                          a day)
FAST-TRACK: stock the dry half     yes (overlaps K, L       2            €0       medium:
       from 3 Apr, chilled from 8  with stocking)                                 Zuid 2024

LIMIT    after crashing, the cold-room chain (delivery 27 Mar) also ends on 3 Apr:
         no money brings the handover earlier than that
RESULT   Joost, 16:00: crash (change C-02, reserve €6k → €1k); fast-track kept as fallback
"""),
    tools="tools: the critical path, the price of weekend work (asked for in February), and a column headed “on the critical path?”",
    dial=[("Light", "a small team behind schedule", ["Ask what's on the critical path.", "Overtime or re-ordering, agreed with the team.", "No table."]),
          ("Standard", "Rotterdam", ["Every idea tested against the critical path.", "Days gained, cost per day, risk.", "Decided by the sponsor over the threshold."]),
          ("Heavy", "large contracts", ["Formal time-cost analysis.", "Acceleration clauses and claims.", "Re-baselining after major compression."])],
    baseline="Each line compares <b>trying every idea for speed</b> to <b>testing each against the critical path and pricing the days that are left</b>.",
    ratings=[(3, 4, "Money goes only where it moves the date."),
             (2, 5, "The handover returns to its baseline date."),
             (2, 4, "Fast-tracking's risk is named, not assumed away."),
             (3, 4, "Each idea's effect is shown, including “nothing”."),
             (3, 4, "Joost decides in hours, with prices."),
             (3, 3, "Neutral."),
             (2, 4, "A fallback is kept ready."),
             (3, 4, "The Zuid-style overlap is avoided."),
             (3, 3, "Two hours of work.")],
    pitfalls=[("Crashing off the path", "The plumber's bonus.", "critical path only."),
              ("Fast-tracking as free", "Rework and accidents.", "price the risk."),
              ("Crashing past the limit", "Another path is now critical.", "re-check after each step."),
              ("Pricing it on the day", "No crew available.", "ask for prices before you need them.")],
    use=["A forecast date is later than the promise.", "When someone proposes paying to go faster.", "Before cutting scope.", "When a phase must finish before a fixed date."],
    skip=["When scope can move instead and the sponsor prefers that: then it's a change, not compression."],
    related=["<b>What Decides the Finish Date?</b> (this volume)", "<b>When Do I Take It Upstairs?</b> (vol. 2)", "<b>Can We Change That?</b> (vol. 2)", "<b>One-way and two-way doors</b> (Ana, vol. 2)"],
    quiz=[("Crashing or fast-tracking: weekend work by the builder?", "Crashing."),
          ("Crashing or fast-tracking: stocking while the store is being finished?", "Fast-tracking."),
          ("Why did paying the plumber buy nothing?", "Plumbing wasn't on the critical path (and was already finished)."),
          ("€5,000 for two days. What's the cost per day?", "€2,500."),
          ("After the weekend work, Femke asks if more money could open the store on 2 April. What does Sanne answer?", "No: the cold-room chain, held by its delivery on 27 March, also ends on 3 April. It's now critical too.")],
    try_it="Take a deadline your project is at risk of missing. List every idea for going faster. Strike out those not on the critical path. Price each remaining day, and write the risk of each overlap.",
    remember="A <span class=\"hl\">taxi</span> on the wrong leg of the journey doesn't catch the <span class=\"hl\">train</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, schedule compression.",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019).",
             "Harold Kerzner, <i>Project Management: A Systems Approach</i> (13th ed., 2022): time-cost trade-offs."],
)

NOTES = [NETWORK, CRITICAL, FLOAT, GANTT, CRASH]
