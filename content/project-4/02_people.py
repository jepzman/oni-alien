# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 4 · People (the Resources domain)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 4").
# People facts reused: ~40 pickers and couriers (15 + 25); first 15 start 30 Mar, trained at Noord; Yara starts 2 Mar;
# King's Day 27 Apr (Amsterdam's busiest day; Rotterdam's opening day); Eli's RFC-003 week (18–27 Mar); hypercare 27 Apr–11 May.

RES = ["resources"]

# ------------------------------------------------------------------ 09 Who Does What?
ra_problem = Doodle(760, 250, "Doodle of 2 February 2026. Kees, the builder's site manager, needs the shelving layout signed off before he can place the electrical points. Tomás thinks Joost signs it. Joost thinks Tomás does. Meanwhile Priya and Grace both believe they have the last word on the launch messages.",
                    "“Who signs off the shelving layout?” Tomás says Joost; Joost says Tomás. The builder waits.")
ra_problem.box(20, 30, 220, 80, "Kees", "paper", sub="waiting for a layout", size=19, subsize=14)
ra_problem.box(270, 30, 220, 80, "Tomás", "y", sub="“Joost signs it”", size=19, subsize=14)
ra_problem.box(520, 30, 220, 80, "Joost", "y", sub="“Tomás signs it”", size=19, subsize=14)
ra_problem.note(380, 160, "and two people think they own the launch messages", "red", size=17)
ra_problem.note(380, 200, "nobody wrote down who decides", "pen", size=18)

ra_analogy = Doodle(760, 240, "Doodle of a wedding. The couple decides. A planner books the venue and the band. The parents are asked for their opinion on the guest list. The guests are told the date. Four roles, and trouble starts when two people think they're the one who decides.",
                    "A wedding: the couple decides, the planner does, the parents are asked, the guests are told.")
ra_analogy.row([("the planner", "does it", "blue"), ("the couple", "decides", "pink"), ("the parents", "are asked", "y"), ("the guests", "are told", "paper")], y=50, h=90, size=17, subsize=15)
ra_analogy.note(98, 190, "R", "red", size=22)
ra_analogy.note(282, 190, "A", "red", size=22)
ra_analogy.note(466, 190, "C", "red", size=22)
ra_analogy.note(650, 190, "I", "red", size=22)

ra_how = Doodle(760, 420, "Rotterdam's RACI table, agreed on 2 February 2026. Rows: the deliverables. Columns: Joost, Sanne, Tomás, Eli, Ben and Dee, Grace, Lena, Priya, and Kees the builder. Each row has exactly one A, the person who answers for it, and at least one R, who does the work. Store fitted: Kees responsible, Joost accountable. Stocked and laid out: Tomás both. City set up: Eli. Apps: Ben and Dee responsible, Grace accountable. Payments and legal: Lena. Marketing: Priya accountable, Grace consulted. Hypercare: Joost accountable. The plan and status: Sanne responsible, Joost accountable.",
                "One A per row, at least one R. The shelving layout is Tomás's; the launch messages are Priya's.", exact=True)
cols = ["Joost", "Sanne", "Tomás", "Eli", "Ben, Dee", "Grace", "Lena", "Priya", "Kees"]
rows_ = [("store fitted", ["A", "C", "C", "C", "", "", "", "", "R"]),
         ("stocked + laid out", ["C", "I", "A R", "", "", "", "", "", "C"]),
         ("staff trained", ["A", "I", "R", "", "", "", "", "", ""]),
         ("city set up", ["", "I", "C", "A R", "", "C", "", "", ""]),
         ("Rotterdam in apps", ["", "C", "", "C", "R", "A", "", "", ""]),
         ("payments + legal", ["", "I", "", "", "", "", "A R", "", ""]),
         ("launch marketing", ["", "I", "", "", "", "C", "", "A R", ""]),
         ("hypercare", ["A", "C", "R", "", "R", "C", "", "", ""]),
         ("plan + status", ["A", "R", "C", "C", "C", "C", "", "", ""])]
x0, cw, rh = 170, 64, 38
for k, c in enumerate(cols):
    ra_how.head(x0 + k * cw + cw / 2, 30, c, size=14)
fills = {"A": "pink", "R": "blue", "A R": "pink", "C": "y", "I": "paper"}
for i, (name, cells) in enumerate(rows_):
    y = 44 + i * rh
    ra_how.text(14, y + 24, name, anchor="start", size=15)
    for k, v in enumerate(cells):
        if v:
            ra_how.box(x0 + k * cw + 4, y + 3, cw - 8, rh - 8, v, fills[v], size=14, rx=4)
ra_how.note(380, 404, "R does it · A answers for it (one per row) · C is asked · I is told", "pen", size=15)

RACI = dict(
    slug="raci",
    kicker="a.k.a. planning resource management: the responsibility matrix (RACI)",
    tldr="A <b>RACI</b> table answers “who does what?” for each deliverable or decision. <b>R</b>esponsible: does the work. <b>A</b>ccountable: answers for it and signs it off; <b>exactly one per row</b>. <b>C</b>onsulted: asked before. <b>I</b>nformed: told after. Most confusion on a project is two people who each think they're the A, or none. Draw the table early, with the people in it, and fix every row with no A or two.",
    chips=[("Family", "getting the people and things"), ("Lives in", "one table in the plan, rows = deliverables, columns = people"), ("Pairs with", "the role card, who decides what, decision rights")],
    pmbok=dict(covers="planning resource management: roles and responsibilities, the responsibility assignment matrix, how people will be found, trained and released",
               domains=RES + ["governance"], processes=["Plan Resource Management"], principles=["Build an empowered culture"], focus=["planning"],
               older="6th: “Plan Resource Management” (9.1): the RACI chart, resource management plan, team charter. 7th: the Team domain."),
    problem_side="Larder, 2 February 2026",
    problem="""  <p class="lead">Kees needs the <b>shelving layout</b> signed off before he can place the electrical points. Tomás thinks Joost signs it: it's a store. Joost thinks Tomás does: he'll run it. <span class="hl-pink">Each is waiting for the other, and the builder is waiting for both.</span> In the same week Priya and Grace each believe they have the last word on the launch messages to customers.</p>
  <ul>
    <li>Some decisions have no owner; some have two.</li>
    <li>People wait politely for each other.</li>
    <li>The role card covered Sanne and Joost, not everyone else.</li>
  </ul>""",
    problem_figs=[ra_problem],
    analogy_side="the wedding",
    analogy="""  <p>At a wedding, the <b>couple decides</b>. A <b>planner</b> books the venue and the band. The <b>parents are asked</b> about the guest list. The <b>guests are told</b> the date. Four roles, all clear. Trouble starts when the planner thinks they decide the menu, or two parents each think the guest list is theirs.</p>""",
    analogy_figs=[ra_analogy],
    map=[("The planner (R)", "Kees fits the store; Ben and Dee build the app items"),
         ("The couple (A)", "Joost for the store; Grace for the app; Tomás for the layout"),
         ("The parents (C)", "Tomás on the fit-out; Grace on the marketing messages"),
         ("The guests (I)", "Sanne on most rows; the steering group"),
         ("Two people who think they decide", "Priya and Grace on the launch messages")],
    how_side="one table, one A per row, agreed in the room",
    how="""  <p>Sanne draws the table with the leads on <b>2 February</b>: rows are the deliverables, columns the people. The rule: <b>exactly one A per row</b>, at least one R. Two rows change in the room. The <b>shelving layout</b> moves into “stocked and laid out”, where <b>Tomás is A</b> (he'll run the store; Joost is consulted), and Kees gets his signature that afternoon. The <b>launch messages</b>: <b>Priya is A</b>, Grace is consulted on anything about the app. Sanne is A for nothing except the plan's integrity under Joost; on most rows she's I or C, which is the point. The table goes into the plan with three more lines: how people will be found (hire, borrow), trained (at Noord), and released (borrowed staff home by 8 May).</p>""",
    how_figs=[ra_how],
    steps=[("List the deliverables or decisions as rows", "Not tasks."),
           ("List the people as columns", "Including suppliers."),
           ("Fill in R, A, C, I with the people in the room", "Not alone."),
           ("Exactly one A per row", "Fix every row with none or two."),
           ("Check no one is A for everything", "Including you."),
           ("Add how people are found, trained, released", "The rest of the resource plan.")],
    vocab=[("RACI", "Responsible, Accountable, Consulted, Informed."),
           ("Responsible", "Does the work."),
           ("Accountable", "Answers for the result and signs it off. One person."),
           ("Consulted", "Asked for input before; two-way."),
           ("Informed", "Told after; one-way."),
           ("Resource management plan", "How people and things will be found, used, looked after and released.")],
    code=dict(file="rotterdam/39-raci.md", note="agreed with the leads, 2 February 2026", plain=True, src="""
# ROTTERDAM · WHO DOES WHAT (R does · A answers · C asked · I told)

DELIVERABLE            Joost  Sanne  Tomás  Eli   Ben/Dee  Grace  Lena  Priya  Kees
Store fitted             A      C      C     C                                   R
Stocked + laid out       C      I     A R                                        C
Staff trained            A      I      R
City set up                     I      C    A R             C
Rotterdam in the apps           C            C      R       A
Payments + legal                I                                  A R
Launch marketing                I                                  C      A R
Hypercare                A      C      R            R       C
Plan + status            A      R      C     C      C       C

FIXED IN THE ROOM  shelving layout → Tomás (A) · launch messages → Priya (A), Grace (C)
PEOPLE PLAN        found: hire 40 hourly staff, borrow experienced pickers (agreed with
                   their store managers) · trained: at Noord, 20 practice orders each ·
                   released: borrowed staff home by 8 May · thanked: at closing
"""),
    tools="tools: a grid on a whiteboard, the leads in the room, and the rule “one A per row”.",
    dial=[("Light", "one small team", ["Say who decides each big thing.", "One sentence each.", "No table."]),
          ("Standard", "Rotterdam", ["A RACI by deliverable.", "One A per row.", "Three lines on finding, training and releasing people."]),
          ("Heavy", "many teams and suppliers", ["RACI per work package.", "A full resource management plan.", "Team charters per team."])],
    baseline="Each line compares <b>assuming everyone knows who decides</b> to <b>a RACI table with one A per row, drawn with the people in it</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "Decisions stop waiting for the wrong person."),
             (2, 4, "Rows with no owner are found in February."),
             (2, 5, "Who does what is one table."),
             (3, 4, "Leads see their role written down."),
             (2, 4, "Owners own their deliverables."),
             (3, 4, "A new person can find their role at once."),
             (3, 3, "Neutral."),
             (4, 4, "An hour, once.")],
    pitfalls=[("Two A's", "Two people decide; neither does.", "one A per row."),
              ("No A", "Everyone waits.", "fill every row."),
              ("Project manager as A for everything", "A bottleneck, and wrong.", "A where you answer; C or I elsewhere."),
              ("Drawn alone", "Nobody agrees with it.", "draw it with the people in it.")],
    use=["Early, after the deliverables are known.", "When decisions wait for each other.", "When suppliers or new people join.", "When two people claim the same decision."],
    skip=["A two-person job where who does what is obvious."],
    related=["<b>What Is My Job Here?</b> (vol. 1)", "<b>Who Decides What?</b> (vol. 2)", "<b>Decision rights</b> (Ana, vol. 2)", "<b>How Many People, and What Else?</b> (next note)"],
    quiz=[("What's the rule for A?", "Exactly one per row."),
          ("Who signs off the shelving layout?", "Tomás: A for “stocked and laid out”."),
          ("R or A: Kees fitting the store?", "R. Joost is A."),
          ("Why is Sanne A on only one row?", "She answers for the plan, not for the deliverables; owners answer for those."),
          ("On 10 March the cold-room supplier asks who approves the door position. Whose call?", "Joost (A for the store fitted), with Tomás consulted.")],
    try_it="Draw a RACI for your project's five most important deliverables. Count the A's in each row. Fix every row with none or more than one, with the people involved.",
    remember="The couple <span class=\"hl\">decides</span>; the planner <span class=\"hl\">does</span>. One couple per wedding.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, planning resource management.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 9.1 Plan Resource Management.",
             "Michael L. Smith and James Erwin, “Role & Responsibility Charting (RACI)” (2005)."],
)

# ------------------------------------------------------------------ 10 How Many People, and What Else?
er_problem = Doodle(760, 250, "Doodle of 10 February 2026. Joost's first answer to how many people Rotterdam needs: sixty, like Zuid. At 1,500 euros each to recruit and train, that's ninety thousand euros, thirty more than the people line. Sanne asks a different question: how many orders will the store handle, and how many people does that take?",
                    "“Sixty, like Zuid.” At €1,500 each that's €30k over the people line. How many does Rotterdam's demand take?")
er_problem.box(20, 40, 330, 100, "Joost: 60 people", "y", sub="“like Zuid”", size=20, subsize=15)
er_problem.box(410, 40, 330, 100, "60 × €1,500", "pink", sub="€90k vs a €60k line", size=20, subsize=15)
er_problem.note(380, 186, "people from habit, not from demand", "red", size=20)
er_problem.note(380, 222, "Zuid serves a different number of orders", "pen", size=17)

er_analogy = Doodle(760, 240, "Doodle of a caterer quoting for a wedding. Not as many waiters as last time: so many guests, so many courses, one waiter per twelve guests for a sit-down dinner, plus two at the bar. Plates and glasses follow from the same sum, with a few spares.",
                    "A caterer counts waiters from guests and courses: one per twelve, plus the bar, plus spares.")
er_analogy.row([("120 guests", "sit-down", "paper"), ("÷ 12 per waiter", "+ 2 at the bar", "y"), ("12 waiters", "+ plates, spares", "green")], y=50, h=90, gap=34, size=18, subsize=15, arrows=True)
er_analogy.note(380, 196, "people and things follow from demand", "pen", size=19)

er_how = Doodle(760, 400, "Sanne's resource estimate from demand, 10 February 2026. Joost's plan for the first month: about 350 orders a day, open 08:00 to 22:00. Pickers: about 9 orders an hour each at Noord's pace, so 39 picker-hours a day plus 10 for receiving and stocking: about 7 shifts a day, 49 a week, 15 pickers at three or four shifts each. Couriers: about 2.5 deliveries an hour, so 140 courier-hours a day, 20 shifts, 140 a week, 25 couriers at five or six shifts. Forty people in all. Equipment from the same sums: 40 e-bikes, 30 handhelds.",
                "350 orders a day → 15 pickers + 25 couriers = 40. Bikes and handhelds follow from the same sum.", exact=True)
er_how.box(250, 14, 260, 56, "≈ 350 orders a day", "y", sub="first month · 08:00–22:00", size=18, subsize=13)
er_how.box(14, 100, 360, 170, None, "blue")
er_how.head(194, 128, "pickers", size=19)
for i, t in enumerate(["350 ÷ 9 an hour ≈ 39 h", "+ 10 h receiving, stocking", "≈ 7 shifts a day, 49 a week", "→ 15 pickers"]):
    er_how.text(194, 160 + i * 28, t, size=15)
er_how.box(386, 100, 360, 170, None, "green")
er_how.head(566, 128, "couriers", size=19)
for i, t in enumerate(["350 ÷ 2.5 an hour = 140 h", "= 20 shifts a day", "140 a week at 5–6 each", "→ 25 couriers"]):
    er_how.text(566, 160 + i * 28, t, size=15)
er_how.arrow(380, 70, 194, 98)
er_how.arrow(380, 70, 566, 98)
er_how.row([("40 people", "€60k line holds", "pink"), ("40 e-bikes", "24 at peak + spares + growth", "paper"), ("30 handhelds", "10 at peak + spares + growth", "paper")], y=296, h=84, size=17, subsize=13)

ESTIMATE_RES = dict(
    slug="estimating-resources",
    kicker="a.k.a. estimating resources: people, skills, equipment and materials",
    tldr="Work out the <b>people</b> and <b>things</b> a project needs from the <b>demand they must serve</b>: the volume of work, a productivity rate you trust, the hours, the shifts, a margin for absence and growth. Equipment follows from the same sum. “As many as last time” copies last time's demand and last time's mistakes. Write the rates down, so the estimate can be checked when real demand arrives.",
    chips=[("Family", "getting the people and things"), ("Lives in", "a short sum from demand to headcount and equipment"), ("Pairs with", "estimating methods, the budget's people line, monitoring resources")],
    pmbok=dict(covers="estimating the kind and number of people, skills, equipment and materials the work needs",
               domains=RES, processes=["Estimate Resources"], principles=["Focus on value"], focus=["planning"],
               older="6th: “Estimate Activity Resources” (9.2), resource requirements and breakdown structure. 7th: the Team and Planning domains."),
    problem_side="Larder, 10 February 2026",
    problem="""  <p class="lead">Joost's first answer to “how many people does Rotterdam need?” is <b>sixty, like Zuid</b>. At €1,500 each to recruit and train, that's <b>€90k</b> against a people line of €60k. But Zuid serves a different number of orders from a different-sized store. <span class="hl-pink">Sixty is a habit, not an estimate.</span> Sanne asks the question underneath: how many orders will Rotterdam handle in its first month, and how many people does that take?</p>
  <ul>
    <li>Headcount copied from another store copies its demand too.</li>
    <li>The budget line and the headcount were never compared.</li>
    <li>Equipment was being ordered from a separate guess.</li>
  </ul>""",
    problem_figs=[er_problem],
    analogy_side="the caterer's sum",
    analogy="""  <p>A good caterer doesn't send “as many waiters as last time.” They ask: how many <b>guests</b>, how many <b>courses</b>, sit-down or standing? One waiter per <b>twelve guests</b> for a sit-down dinner, two at the bar. The plates and glasses come from the same sum, with a few spares. Last time's party had different guests.</p>""",
    analogy_figs=[er_analogy],
    map=[("Guests and courses", "≈ 350 orders a day, 08:00–22:00"),
         ("One waiter per twelve", "9 orders an hour per picker; 2.5 deliveries an hour per courier"),
         ("The bar", "Receiving and stocking: 10 hours a day"),
         ("Plates and glasses", "40 e-bikes, 30 handhelds"),
         ("“As many as last time”", "“Sixty, like Zuid”")],
    how_side="from demand to people to equipment",
    how="""  <p>Joost's plan for the first month is about <b>350 orders a day</b>, open 08:00–22:00, rising to 500 by the end of May. <b>Pickers</b>: Noord picks about <b>9 orders an hour</b> per picker (6 minutes 40 an order), so 350 orders is about 39 picker-hours a day; add 10 for receiving and stocking: about 7 shifts a day, 49 a week, so <b>15 pickers</b> at three or four shifts each. <b>Couriers</b>: about <b>2.5 deliveries an hour</b>, so 140 courier-hours a day, 20 shifts, 140 a week, so <b>25 couriers</b> at five or six shifts. <b>Forty people</b>, and the €60k line holds. Equipment from the same sums: <b>40 e-bikes</b> (24 on the road at the Friday peak, plus charging spares and growth) and <b>30 handhelds</b>. The growth to 500 a day becomes a <b>second hiring wave</b> in May, paid by operations.</p>""",
    how_figs=[er_how],
    steps=[("Start from demand", "Volume, hours, peaks."),
           ("Use a productivity rate you trust", "From a running operation."),
           ("Turn hours into shifts, shifts into people", "With realistic shifts per person."),
           ("Add margins for absence and growth", "And say how big."),
           ("Derive equipment from the same sums", "Peak use plus spares."),
           ("Compare with the budget line", "Before hiring anyone.")],
    vocab=[("Resource requirements", "The kinds and numbers of people and things the work needs."),
           ("Productivity rate", "Output per person per hour: orders, deliveries."),
           ("Shift", "A block of working hours for one person."),
           ("Full-time equivalent (FTE)", "Total hours expressed as full-time people."),
           ("Resource breakdown structure", "People and things grouped by kind."),
           ("Peak load", "The busiest period the resources must cover.")],
    code=dict(file="rotterdam/40-resource-estimate.md", note="Sanne with Joost and Tomás, 10 February 2026", plain=True, src="""
# ROTTERDAM · PEOPLE AND THINGS FROM DEMAND (first month)

DEMAND        ≈ 350 orders a day (first month) → 500 a day by end May · open 08:00–22:00
PICKERS       9 orders an hour each (Noord: 6:40 an order)
              350 ÷ 9 ≈ 39 h + 10 h receiving/stocking = 49 h a day ≈ 7 shifts of 7 h
              49 shifts a week ÷ 3–4 each                              → 15 pickers
COURIERS      2.5 deliveries an hour each
              350 ÷ 2.5 = 140 h a day = 20 shifts · 140 a week ÷ 5–6 each → 25 couriers
TOTAL         40 people × €1,500 = €60k (the people line holds)
EQUIPMENT     e-bikes   40  (24 on the road at Friday peak + 6 charging/spare + 10 growth)
              handhelds 30  (10 at peak + 4 receiving + 6 spare/charging + 10 growth)
              label printers 4 · payment terminals 2 · chargers 40 (R-31)
GROWTH        to 500 a day: second wave (+5 pickers, +12 couriers) in May, operations budget
JOOST'S FIRST GUESS  60 "like Zuid" → €90k, €30k over the line
"""),
    tools="tools: the demand plan, two productivity rates from a running store, and a calculator.",
    dial=[("Light", "a small team", ["Ask: how much work, how fast does one person do it?", "One sum.", "A little margin."]),
          ("Standard", "Rotterdam", ["Demand → hours → shifts → people.", "Equipment from the same sums.", "Checked against the budget line."]),
          ("Heavy", "large operations", ["Workforce models with absence rates and peaks.", "Resource breakdown structures.", "Capacity planning tools."])],
    baseline="Each line compares <b>“as many as Zuid”</b> to <b>people and equipment worked out from Rotterdam's demand and trusted rates</b>.",
    ratings=[(3, 4, "People sized for the orders that matter."),
             (2, 4, "Hiring and spending follow one sum."),
             (2, 4, "€30k of over-hiring avoided."),
             (2, 4, "The rates are written down."),
             (3, 4, "Joost sees the sum, not just a number."),
             (3, 4, "Tomás's rates are the basis."),
             (2, 4, "A second wave is planned for growth."),
             (3, 3, "Neutral."),
             (4, 4, "An hour's sum.")],
    pitfalls=[("“As many as last time”", "Last time's demand.", "start from this demand."),
              ("No margin", "One sick day and the shift fails.", "add absence and peaks."),
              ("Equipment from another guess", "Bikes don't match couriers.", "same sums for both."),
              ("Never checked", "Real demand differs.", "re-check in week one (note 15).")],
    use=["Before hiring or ordering equipment.", "When a headcount is quoted without a reason.", "When demand changes.", "For every new site."],
    skip=["A project done entirely by an existing team."],
    related=["<b>How Long, Roughly?</b> (vol. 3)", "<b>What Will It Cost?</b> (this volume)", "<b>Capacity planning</b> (Ana, vol. 5)", "<b>Are the People and Things Still There?</b> (this volume)"],
    quiz=[("Pickers needed for 350 orders a day at 9 an hour?", "About 39 hours of picking, plus receiving: about 15 pickers on part-time shifts."),
          ("Why not sixty like Zuid?", "Zuid's demand is different; and sixty would cost €30k over the people line."),
          ("Where did 40 e-bikes come from?", "24 on the road at the Friday peak, plus charging spares, plus growth."),
          ("Who pays for the second wave in May?", "Operations: it's running the store, not launching it."),
          ("In week one orders are 540 a day, not 350. What does Sanne do with the estimate?", "Re-run the sum with the real demand and pull the second wave forward (it went from mid-May to 4 May).")],
    try_it="Write your project's demand in one line, find one productivity rate you trust, and work out the people it needs. Compare with the number you were planning to hire.",
    remember="Count the <span class=\"hl\">guests</span> before you book the <span class=\"hl\">waiters</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, estimating resources.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 9.2 Estimate Activity Resources.",
             "Eliyahu Goldratt, <i>The Goal</i> (1984): capacity follows the constraint."],
)

# ------------------------------------------------------------------ 11 Where Do They Come From?
aq_problem = Doodle(760, 250, "Doodle of 2 April 2026 and Sanne's mistake for this collection. On 30 March she agreed with Tomás to borrow four experienced pickers from Noord for Rotterdam's opening fortnight, starting on opening day. Joost reads the plan and stops her: 27 April is King's Day. Noord's busiest day of the year, five times a normal peak. Nobody had asked the person who plans Noord's King's Day.",
                    "Four of Noord's best pickers, lent for Rotterdam's opening day. Which is King's Day, Noord's busiest day of the year.")
aq_problem.box(20, 40, 330, 100, "4 pickers from Noord", "y", sub="agreed with Tomás, 30 Mar", size=19, subsize=14)
aq_problem.box(410, 40, 330, 100, "27 April", "pink", sub="King's Day: Noord at 5× peak", size=20, subsize=15)
aq_problem.note(380, 186, "the loan was agreed with one owner, not the one who plans the peak", "red", size=16)
aq_problem.note(380, 222, "Joost caught it on 2 April", "pen", size=18)

aq_analogy = Doodle(760, 240, "Doodle of a family borrowing a neighbour's car. The neighbour said yes. But the car belongs to the household, and the teenager needs it on Saturday for a driving test. Asking the person who said yes isn't the same as asking everyone who depends on it.",
                    "The neighbour said yes. The teenager has a driving test on Saturday. Ask everyone who depends on it.")
aq_analogy.row([("borrow the car", "for the weekend", "y"), ("neighbour: yes", None, "green"), ("Saturday", "the driving test", "pink")], y=50, h=90, gap=34, size=18, subsize=15, arrows=True)
aq_analogy.note(380, 196, "a loan is agreed with everyone who needs it", "pen", size=19)

aq_how = Doodle(760, 400, "Where Rotterdam's people and things came from, February to April 2026. Hired: 40 hourly pickers and couriers, through an agency (22), local job boards (10), referrals (4) and internal moves (4); first 15 started on 30 March, the last on 17 April. Central hires under Marco's cap of four for 2026: Rotterdam used one, Sanne herself. Borrowed: four experienced pickers, two from Noord and two from Zuid, from 28 April to 8 May, never on King's Day. Leased: 40 e-bikes, by operations. Bought: the equipment and cold room. Negotiated: 8 to 10 story points a sprint from Ben's and Dee's teams.",
                "Hire, borrow, lease, buy, negotiate. Each from whoever owns it, with every person who depends on it.", exact=True)
src = [("hire", "40 hourly staff", "agency 22 · job boards 10 · referrals 4 · moves 4", "blue"),
       ("central cap", "4 for 2026", "Rotterdam used one: Sanne", "paper"),
       ("borrow", "4 experienced pickers", "2 Noord + 2 Zuid · 28 Apr–8 May · not King's Day", "y"),
       ("lease", "40 e-bikes", "operations, 24 h repair promised", "paper"),
       ("buy", "equipment, cold room", "see sourcing (vol. 2)", "paper"),
       ("negotiate", "team time", "8–10 points a sprint (Ben, Dee)", "green")]
for i, (k, a, b, f) in enumerate(src):
    y = 14 + i * 60
    aq_how.box(14, y, 140, 50, k, f, size=18, rx=5)
    aq_how.box(164, y, 220, 50, a, "paper", size=15, rx=5)
    aq_how.text(400, y + 31, b, anchor="start", size=14)
aq_how.note(380, 388, "first 15 start 30 Mar (training at Noord) · last hire 17 Apr", "pen", size=15)

ACQUIRE = dict(
    slug="acquiring-resources",
    kicker="a.k.a. acquiring resources: hiring, borrowing, leasing and negotiating",
    tldr="People and things reach a project in five ways: <b>hire</b> them, <b>borrow</b> them from another part of the organisation, <b>lease</b> or <b>buy</b> them, or <b>negotiate</b> a share of a team's time. Every one of them belongs to someone first. Agree each one with <b>the owner and everyone who depends on it</b>, put the dates on paper, and plan when it goes back. Most resource trouble starts with a yes from the wrong person.",
    chips=[("Family", "getting the people and things"), ("Lives in", "a sources table: what, how, from whom, when it goes back"), ("Pairs with", "sourcing, estimating resources, RACI")],
    pmbok=dict(covers="obtaining people, equipment and materials: hiring, internal assignment, borrowing, leasing, negotiation with resource owners",
               domains=RES, processes=["Acquire Resources"], principles=["Adopt a holistic view"], focus=["executing"],
               older="6th: “Acquire Resources” (9.3): pre-assignment, negotiation, virtual teams. 7th: the Team domain."),
    problem_side="Larder, 30 March → 2 April 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. Rotterdam's forty are new, and opening day needs a few people who've picked a thousand orders. On <b>30 March</b> she agrees with Tomás to borrow <b>four of Noord's most experienced pickers</b> for the opening fortnight, from 27 April. On 2 April Joost reads the plan and stops her: <b>27 April is King's Day</b>, Noord's busiest day of the year, five times a normal peak. <span class="hl-pink">She asked the store manager, not the person who plans Noord's King's Day.</span></p>
  <ul>
    <li>A yes from one owner isn't a yes from everyone who depends on the resource.</li>
    <li>The calendar knew it was King's Day; the loan didn't look.</li>
    <li>Borrowing the best people weakens the place they come from.</li>
  </ul>""",
    problem_figs=[aq_problem],
    analogy_side="borrowing the neighbour's car",
    analogy="""  <p>You ask to borrow the neighbour's car for the weekend, and the neighbour says yes. On Saturday morning their teenager comes out for a <b>driving test</b>. The car belonged to the household, not to the person who said yes. Borrowing well means asking everyone who depends on the thing, and writing down when it comes back.</p>""",
    analogy_figs=[aq_analogy],
    map=[("The neighbour's yes", "Tomás's agreement on 30 March"),
         ("The household", "Noord's operations, planned by Joost"),
         ("The driving test", "King's Day, 27 April"),
         ("Asking everyone", "Joost and Zuid's manager as well"),
         ("When it comes back", "8 May, written in the plan")],
    how_side="five ways in, each agreed with everyone who depends on it",
    how="""  <p>Sanne fixes the loan the same day: <b>two pickers from Noord and two from Zuid</b>, from <b>28 April to 8 May</b>, agreed with Joost and both store managers in writing. On opening day Rotterdam runs on its own fifteen, with Yara and Grace on the floor and Tomás where he's needed most: at Noord, for King's Day. Then she writes every source down. <b>Hired</b>: forty hourly staff through an agency (22), job boards (10), referrals (4) and internal moves (4); the first fifteen start on 30 March and train at Noord; the last joins on 17 April. <b>Central hires</b>: Marco's cap of four for 2026 is for salaried central roles, and Rotterdam used one: Sanne. <b>Leased</b>: forty e-bikes, by operations. <b>Bought</b>: the equipment and cold room (Vol. 2). <b>Negotiated</b>: 8–10 story points a sprint from Ben's and Dee's teams, agreed with Grace.</p>""",
    how_figs=[aq_how],
    steps=[("For each resource, choose: hire, borrow, lease, buy, negotiate", "From the estimate."),
           ("Find its owner", "And everyone who depends on it."),
           ("Check the calendar on both sides", "Their peaks, not just yours."),
           ("Agree dates in writing", "Start, end, return."),
           ("Check limits", "Hiring caps, budgets, contracts."),
           ("Plan the return", "When, and who checks it happened.")],
    vocab=[("Acquisition", "Getting the people and things the project needs."),
           ("Pre-assignment", "People named before the project starts."),
           ("Internal loan", "People borrowed from another part of the organisation."),
           ("Resource owner", "Whoever the person or thing belongs to day to day."),
           ("Headcount cap", "A limit on permanent hires."),
           ("Release", "Returning people and things when they're no longer needed.")],
    code=dict(file="rotterdam/41-resource-sources.md", note="February → April 2026 · loan corrected 2 April", plain=True, src="""
# ROTTERDAM · WHERE THE PEOPLE AND THINGS COME FROM

HIRED        40 hourly pickers and couriers (store staff, people line)
             agency 22 · local job boards 10 · referrals 4 · internal moves 4
             first 15 start Mon 30 Mar (training at Noord) · last starts 17 Apr
CENTRAL CAP  4 salaried central hires for 2026 (Marco) · Rotterdam used 1: Sanne
BORROWED     4 experienced pickers: 2 from Noord, 2 from Zuid · 28 Apr → 8 May
             agreed with Joost, Tomás and Zuid's manager, 2 Apr
             (was: 4 from Noord from 27 Apr, agreed with Tomás only → King's Day clash)
OPENING DAY  Rotterdam's own 15 · Yara and Grace on the floor · Tomás at Noord
LEASED       40 e-bikes (operations) · repair within 24 h (contract)
BOUGHT       equipment + store IT, cold room (see sourcing, vol. 2)
NEGOTIATED   8–10 story points a sprint from Ben's and Dee's teams (with Grace)
RETURNS      borrowed pickers home 8 May (Joost checks) · spare handhelds stay
"""),
    tools="tools: the resource estimate, a calendar with everyone's peaks on it, and written agreements with each owner.",
    dial=[("Light", "one borrowed person", ["Ask their manager and them.", "Dates in a message.", "Return on time."]),
          ("Standard", "Rotterdam", ["A sources table.", "Each loan agreed with every owner, in writing.", "Returns planned."]),
          ("Heavy", "large programmes", ["Resource requests through a PMO.", "Formal secondment agreements.", "Hiring plans approved by HR and finance."])],
    baseline="Each line compares <b>a yes from whoever was asked</b> to <b>each resource agreed with its owner and everyone who depends on it, with dates and a return</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "Loans arrive and leave on agreed dates."),
             (2, 4, "The King's Day clash was caught three weeks ahead."),
             (2, 4, "Every source is on one table."),
             (2, 4, "Joost and two store managers agreed in writing."),
             (3, 4, "Rotterdam's own team ran opening day."),
             (3, 4, "A loan was reshaped in a day."),
             (3, 3, "Neutral."),
             (3, 3, "A table and a few conversations.")],
    pitfalls=[("A yes from one owner", "The others find out later.", "everyone who depends on it."),
              ("Only your calendar", "Their peak clashes with yours.", "check both."),
              ("No return date", "Loans become permanent, or vanish.", "write when it comes back."),
              ("Borrowing the best everywhere", "The home team suffers.", "spread loans; plan the gap.")],
    use=["Before hiring, borrowing or leasing.", "When a resource is shared.", "Around anyone's peak days.", "When a cap or budget applies."],
    skip=["The team is fixed and nothing is borrowed."],
    related=["<b>Make It, Buy It, or Hire It?</b> (vol. 2)", "<b>How Many People, and What Else?</b> (previous note)", "<b>Who Does What?</b> (this volume)", "<b>Are the People and Things Still There?</b> (this volume)"],
    quiz=[("Name the five ways resources reach a project.", "Hire, borrow, lease, buy, negotiate."),
          ("Why was the first loan wrong?", "It took four of Noord's best pickers on King's Day; it was agreed with Tomás, not with Joost, who plans Noord's peak."),
          ("Did Rotterdam's forty pickers and couriers count against Marco's cap of four?", "No: the cap is for salaried central roles. Rotterdam used one: Sanne."),
          ("When did the borrowed pickers go home?", "8 May."),
          ("On 20 April Ben offers to lend two of his engineers to Eli for a week. What does Sanne check?", "With Grace, who negotiated the team's time, and with Ben's sprint plan; then dates and the return in writing.")],
    try_it="List every person and thing your project borrows. For each, write the owner, everyone else who depends on it, the return date, and whether their busiest day falls in your loan.",
    remember="The neighbour said yes. Ask about the <span class=\"hl\">driving test</span> before you take the <span class=\"hl\">car</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, acquiring resources.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 9.3 Acquire Resources.",
             "J. Rodney Turner, <i>The Handbook of Project-Based Management</i> (4th ed., 2014): the matrix organisation."],
)

# ------------------------------------------------------------------ 12 Who Is Overloaded?
rl_problem = Doodle(760, 250, "Doodle of Monday 23 March 2026 and Sanne's mistake for this collection. Her plan has Eli at a hundred percent on Rotterdam. But Eli is also Larder's platform engineer: the Dispatch RFC with Ben this week, the on-call week, the internet line, two extras he said yes to. Added up, his week is eight days long. He hasn't complained. He's just slower.",
                    "Eli on the plan: 100 % Rotterdam. Eli in reality: an eight-day week. He hasn't complained; he's just slower.")
rl_problem.row([("platform", "2½ d", "blue"), ("RFC-003", "1½ d", "paper"), ("on call", "1 d", "paper"), ("internet", "1 d", "pink"), ("extras", "1½ d", "paper"), ("alert fix", "½ d", "paper")], y=30, h=76, gap=8, size=15, subsize=15)
rl_problem.note(380, 160, "8 days of work in a 5-day week = 160 %", "red", size=20)
rl_problem.note(380, 200, "the plan assumed he worked only on Rotterdam", "pen", size=17)

rl_analogy = Doodle(760, 240, "Doodle of a wedding photographer booked for two weddings on the same Saturday afternoon. Each couple's plan is fine. Together they need one person in two places. Nobody notices until both plans are laid on one calendar.",
                    "Each couple's plan is fine. Laid on one calendar, the photographer is in two places at once.")
rl_analogy.box(20, 40, 330, 100, "wedding 1", "y", sub="Sat 14:00–18:00", size=20, subsize=15)
rl_analogy.box(410, 40, 330, 100, "wedding 2", "blue", sub="Sat 15:00–19:00", size=20, subsize=15)
rl_analogy.note(380, 186, "one photographer, two places", "red", size=20)
rl_analogy.note(380, 222, "only one calendar shows it", "pen", size=18)

rl_how = Doodle(760, 400, "Eli's load by week, March and April 2026, as a percentage of a five-day week, before and after levelling on 24 March. Before: 80, 100, 160, 120, 70 and 60. After: 80, 100, 100, 100, 95, 75. Actions: the on-call week swapped with another engineer, Ben takes the Dispatch code changes and Eli only reviews, the alert fix moved a week within its float, the store dashboard stopped until after opening, and the zone checks moved to the week of 6 April. No milestone moved.",
                "Eli's weeks before (outline) and after levelling (filled). Same work, same milestones, no 160 % week.", exact=True)
weeks = ["9 Mar", "16 Mar", "23 Mar", "30 Mar", "6 Apr", "13 Apr"]
before = [80, 100, 160, 120, 70, 60]
after = [80, 100, 100, 100, 95, 75]
base, sc = 270, 1.4
rl_how.line(f"M50 {base - 100 * sc} H730", color="red", dash=True)
rl_how.note(726, base - 100 * sc - 8, "100 %", "red", size=14, anchor="end")
for i, w in enumerate(weeks):
    x = 70 + i * 110
    rl_how.box(x, round(base - before[i] * sc), 40, round(before[i] * sc), None, "pink" if before[i] > 100 else "paper", dash=True, rx=2)
    rl_how.box(x + 46, round(base - after[i] * sc), 40, round(after[i] * sc), None, "blue", rx=2)
    rl_how.text(x + 43, base + 22, w, "t t-soft", size=14)
    rl_how.note(x + 20, round(base - before[i] * sc) - 6, f"{before[i]}", size=13)
rl_how.line(f"M50 {base} H730", thin=True)
rl_how.text(380, 322, "on-call swapped · Ben does the Dispatch code, Eli reviews · alert fix moved", size=14)
rl_how.text(380, 346, "a week (float) · dashboard after opening · zone checks to 6 April", size=14)
rl_how.note(380, 378, "no milestone moved: smoothing, not levelling", "green", size=16)

rl_deep1 = Doodle(760, 260, "Smoothing and levelling compared. Smoothing moves work only within its float, so no end date moves: Rotterdam's choice. Levelling moves work until nobody is over a hundred percent, even if the end date moves: needed when there isn't enough float. A third option, adding or switching people, changes who does the work.",
                  "Smoothing: within float, dates hold. Levelling: whatever it takes, dates may move. Or change who does it.")
rl_deep1.row([("smoothing", "within float · dates hold", "green"), ("levelling", "dates may move", "y"), ("re-assigning", "someone else does it", "blue")], y=40, h=96, size=19, subsize=14)
rl_deep1.note(132, 180, "Rotterdam: alert fix, zone checks", "green", size=14)
rl_deep1.note(380, 180, "not needed", size=14)
rl_deep1.note(628, 180, "Ben: Dispatch code · on-call swap", "pen", size=14)
rl_deep1.note(380, 228, "and stop work that shouldn't be there (the dashboard)", "red", size=16)

LEVEL = dict(
    slug="resource-levelling",
    kicker="a.k.a. resource levelling and smoothing",
    tldr="A plan can be fine activity by activity and still ask one person to work an eight-day week. Draw each key person's <b>load by week</b> (a resource histogram) across <b>all</b> their work, not just your project. Where it passes 100 %, <b>smooth</b> (move work within its float, so no date moves), <b>re-assign</b> (someone else does it), <b>stop</b> what shouldn't be there, or, if nothing else works, <b>level</b> (move work even if a date moves). Plan people at about 80 %: meetings, support and surprises take the rest.",
    chips=[("Family", "leading and balancing"), ("Lives in", "a load chart for each key person, checked weekly"), ("Pairs with", "float, scope creep, acquiring resources")],
    pmbok=dict(covers="spotting over-allocation across all of a person's work; resource smoothing, levelling and re-assignment; realistic allocation",
               domains=RES + ["schedule"], processes=["Monitor and Control Resourcing"], principles=["Adopt a holistic view", "Build an empowered culture"], focus=["planning", "monitoring"],
               older="6th: resource optimisation (levelling and smoothing) in 6.5 Develop Schedule; Control Resources (9.6). 7th: the Planning and Team domains."),
    problem_side="Larder, 23–24 March 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. Her plan has <b>Eli at 100 % on Rotterdam</b>. But Eli is also Larder's platform engineer, and the week of 23 March holds: the Rotterdam platform set-up (2½ days), the Dispatch RFC with Ben (1½), his turn on call (1), the store's internet line (1), two extras he said yes to (1½) and the alert fix from the quality review (½). <span class="hl-pink">Eight days of work in a five-day week.</span> He hasn't complained. He's just slower, and every lead waiting on him is slower too.</p>
  <ul>
    <li>Each plan was fine; together they weren't.</li>
    <li>The project manager saw only her project's slice of Eli.</li>
    <li>Overload shows up as delay, not as a complaint.</li>
  </ul>""",
    problem_figs=[rl_problem],
    meanwhile=[("architect-2", "rfcs-design-docs", "RFC-003, Dispatch as a service (Eli and Ben, comments 18–25 March), is accepted on 27 March.",
                "the same week, that RFC was one of six things that put Eli at 160 %; Ben took over its code changes.")],
    analogy_side="the photographer with two weddings",
    analogy="""  <p>A wedding photographer is booked for <b>two weddings on the same Saturday afternoon</b>. Each couple's plan is perfectly sensible. Laid on one calendar, they need one person in two places. Nobody notices until someone looks at the photographer's calendar instead of the couples' plans.</p>""",
    analogy_figs=[rl_analogy],
    map=[("Each couple's plan", "Rotterdam's plan; Ana's RFC; the on-call rota"),
         ("The photographer's calendar", "Eli's load by week, across all his work"),
         ("Two places at once", "160 % in the week of 23 March"),
         ("Moving the second shoot an hour", "Smoothing: the alert fix moves a week within float"),
         ("A second photographer", "Re-assigning: Ben does the Dispatch code")],
    how_side="one chart per key person, across all their work",
    how="""  <p>Sanne sits down with Eli on <b>24 March</b> and draws his load for six weeks, <b>everything</b> he does, not just Rotterdam: 80, 100, <b>160</b>, 120, 70, 60 %. Then they move things. The <b>on-call</b> week is swapped with another engineer (Ana arranges it). <b>Ben</b> takes the Dispatch code changes; Eli only reviews. The <b>alert fix</b> moves a week, inside its float. The <b>store dashboard</b>, one of the extras, is paused (three days later the extras list makes it “after opening”). The <b>zone checks</b> move to the week of 6 April, when Eli has room. After: 80, 100, 100, 100, 95, 75 %. <b>No milestone moved</b>: that's smoothing, not levelling. Sanne also changes her plan's assumption: key people are planned at <b>80 %</b>, because meetings, support and surprises take the rest.</p>""",
    how_figs=[rl_how],
    steps=[("Pick the people everyone waits for", "The bottlenecks."),
           ("Draw their load by week, across all their work", "Ask them; don't guess."),
           ("Find the weeks over 100 %", "Or over 80 % for key people."),
           ("Stop what shouldn't be there", "Extras, nice-to-haves."),
           ("Re-assign or smooth within float", "Dates hold."),
           ("Level only if you must", "And say which date moves.")],
    vocab=[("Resource histogram", "A chart of a person's or team's load over time."),
           ("Over-allocation", "More work assigned than a person can do in the time."),
           ("Resource smoothing", "Moving work within its float so no dates change."),
           ("Resource levelling", "Moving work to remove over-allocation, even if dates change."),
           ("Utilisation", "The share of time spent on planned work."),
           ("Multitasking cost", "Time lost switching between pieces of work.")],
    code=dict(file="rotterdam/42-eli-load.md", note="Sanne and Eli, 24 March 2026", plain=True, src="""
# ELI'S LOAD BY WEEK (% of a 5-day week, ALL his work)

WEEK OF            9 Mar  16 Mar  23 Mar  30 Mar  6 Apr  13 Apr
before               80     100     160     120     70     60
after                80     100     100     100     95     75

WEEK OF 23 MARCH, BEFORE (8 days)
  Rotterdam platform set-up 2½ · RFC-003 Dispatch with Ben 1½ · on call 1 ·
  store internet line (I-07) 1 · extras (dashboard E6, test data E7) 1½ · alert fix ½
ACTIONS (24 Mar)                                              DATE MOVES?
  on-call swapped with another engineer (Ana)                  no
  Ben does the Dispatch code changes; Eli reviews only         no
  alert fix moved one week (float)                             no   (smoothing)
  store dashboard (E6) paused (extras list, 27 Mar: after opening) no
  zone checks moved to week of 6 Apr (float to 20 Apr)          no   (smoothing)
RULE FROM NOW   key people planned at 80 %, across all their work
"""),
    tools="tools: a sheet of weeks for each key person, an honest conversation with them, and the float column from the schedule.",
    deep_dive=dict(
        side="histograms, smoothing vs levelling, 80 % plans, and the cost of switching",
        intro="Overload is the most common hidden cause of slow projects, because it shows up as delay rather than as a complaint. This chapter shows how to see it, the three ways to fix it, why 100 % is already too much, and what switching between projects costs.",
        parts=[
            ("See it: the histogram, across everything", """  <p>A <b>resource histogram</b> is a bar per week of how much work one person has. The trap is drawing it for <b>your project only</b>. Eli was at about 50 % on Rotterdam in the week of 23 March, and at 160 % overall. Only he knew the whole picture, and he didn't think it was his place to say so.</p>
  <p>Draw it for the few people everyone waits for (here: Eli, Ben, Tomás), and draw it <b>with</b> them. It takes ten minutes each and is usually the first time anyone has added it up.</p>""", []),
            ("Fix it: smooth, level, re-assign, stop", """  <ul>
    <li><b>Stop</b> work that shouldn't be there. The store dashboard was an extra; stopping it cost nothing.</li>
    <li><b>Re-assign</b>: someone else does it. Ben took the Dispatch code; another engineer took on-call.</li>
    <li><b>Smooth</b>: move work within its float. The alert fix and the zone checks had float before their milestones.</li>
    <li><b>Level</b>: move work until nobody is overloaded, even if a date moves. Rotterdam didn't need to; if it had, the date that moved would have gone to Joost as a change.</li>
  </ul>""", [rl_deep1]),
            ("Why 100 % is already too much", """  <p>A person planned at 100 % on project work has no time for the things that always happen: meetings, questions from colleagues, support, illness, the unplanned. In practice their plan slips by exactly that amount, every week. Planning key people at about <b>80 %</b> isn't generosity; it's accuracy.</p>
  <p>The same logic applies to machines and teams: queues grow sharply as utilisation approaches 100 %. The last 20 % of a person's week is where the waiting time of everyone downstream comes from.</p>""", []),
            ("The cost of switching", """  <p>Six pieces of work in one week don't just add up to six pieces of work. Each switch costs time to pick up where you left off. Eli's 160 % week would probably have been nearer 180 % in practice.</p>
  <p>The cure is fewer things at once, not more hours: finish one, then start the next. That's why “stop” comes first in the list above, and why the extras list (Vol. 3) was also a resource tool.</p>""", []),
        ]),
    dial=[("Light", "a small team", ["Ask at the weekly meeting: anyone over 100 %?", "Move one thing.", "No charts."]),
          ("Standard", "Rotterdam", ["A load chart for each bottleneck person, across all work.", "Smooth, re-assign, stop.", "Plan key people at 80 %."]),
          ("Heavy", "large programmes", ["Resource management tools across projects.", "Portfolio-level capacity planning.", "Formal levelling in the schedule."])],
    baseline="Each line compares <b>assuming people work only on your project</b> to <b>a load chart for each key person across all their work, with overloads fixed</b>.",
    ratings=[(3, 4, "Eli's time goes to what matters most."),
             (2, 4, "The pace stops leaking into a hidden queue."),
             (2, 4, "A 160 % week was found before it hurt."),
             (2, 4, "Everyone sees the real load."),
             (3, 4, "Ana and Ben helped re-balance."),
             (2, 4, "Eli was asked, not told."),
             (3, 4, "Float was used on purpose."),
             (3, 4, "Less switching, fewer mistakes."),
             (3, 3, "Ten minutes per person per week.")],
    pitfalls=[("Your project only", "Others' work is invisible.", "draw everything the person does."),
              ("Planning at 100 %", "The plan slips every week.", "about 80 % for key people."),
              ("More hours as the fix", "Burn-out, mistakes.", "stop, re-assign, smooth."),
              ("Waiting for a complaint", "Overload shows as delay.", "ask the bottleneck people weekly.")],
    use=["When one person is on everyone's critical path.", "When work slows for no visible reason.", "Before a busy week.", "When people work on several projects."],
    skip=["A dedicated team with nothing else to do (rare)."],
    related=["<b>How Much Can This Slip?</b> (vol. 3)", "<b>Where Did That Come From?</b> (vol. 3)", "<b>RFCs and design docs</b> (Ana, vol. 2)", "<b>Let the Team Decide</b> (vol. 1)"],
    quiz=[("Smoothing or levelling: the alert fix moves a week inside its float?", "Smoothing."),
          ("Why was Eli at 160 %?", "Rotterdam plus the Dispatch RFC, on-call, the internet line, extras and the alert fix."),
          ("Why plan key people at about 80 %?", "Meetings, support and surprises take the rest; at 100 % the plan slips every week."),
          ("Name four ways to fix an overload.", "Stop, re-assign, smooth, level."),
          ("Tomás is at 140 % in the rehearsal week. What does Sanne do first?", "Draw his week with him, across Noord and Rotterdam, and look for something to stop or hand to Yara before moving anything.")],
    try_it="Pick the person your project waits for most. Draw their next four weeks with them, including everything that isn't your project. Any week over 100 %? Stop, re-assign or move one thing.",
    remember="Each <span class=\"hl\">couple's</span> plan was fine. Look at the <span class=\"hl\">photographer's</span> calendar.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, monitoring and controlling resourcing.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): resource optimisation (6.5).",
             "Eliyahu Goldratt, <i>Critical Chain</i> (1997): multitasking and resource contention.",
             "Gerald Weinberg, <i>Quality Software Management</i> (1992): the cost of switching between tasks."],
)

# ------------------------------------------------------------------ 13 How Do I Lead People Who Don't Report to Me?
la_problem = Doodle(760, 250, "Doodle of 16 March 2026. Two Rotterdam app items are slipping: zones and slots in the app, and the store page. Dee's team gave its sprint to approvals and an Android fix, both Grace's priorities. Sanne isn't Dee's manager. She can't move the work, and asking Joost to order it would make an enemy of the team she needs for five more weeks.",
                    "Two Rotterdam items slipping in a team Sanne doesn't manage. She can't order it, and shouldn't.")
la_problem.box(20, 40, 330, 100, "Dee's sprint", "blue", sub="approvals · Android fix", size=19, subsize=15)
la_problem.box(410, 40, 330, 100, "Rotterdam items", "pink", sub="zones + slots · store page", size=19, subsize=15)
la_problem.note(380, 186, "no authority, and five more weeks together", "red", size=19)
la_problem.note(380, 222, "ordering it through Joost would win once", "pen", size=18)

la_analogy = Doodle(760, 240, "Doodle of a choir conductor at a village festival. None of the singers are paid or employed by her. She has no power to make anyone come. They come because the music is worth singing, because she's prepared, because she makes their evening easier, and because she thanks them by name.",
                    "A village choir conductor employs nobody. They come for the music, the preparation, and being thanked by name.")
la_analogy.row([("worth singing", "a shared goal", "y"), ("well prepared", "the facts", "blue"), ("easy to join", "remove blocks", "green"), ("thanked by name", "credit", "pink")], y=50, h=90, size=17, subsize=14)
la_analogy.note(380, 196, "no authority, plenty of influence", "pen", size=19)

la_how = Doodle(760, 400, "How Sanne led Dee's team without authority, 16 to 20 March 2026. First she asked Dee what was blocking the Rotterdam items: the Dutch store-page texts from Priya's team, waiting nine days. She got them in one day. She showed the milestone and the burn-up: app ready on 20 April, two items at risk. She offered something back: Yara's new pickers would test approvals on real handhelds, which Grace needed. And she named Dee's team in the Friday status. Dee put both items in the sprint of 23 March; both were done by 3 April. Joost was never asked.",
                "Ask, unblock, show the facts, offer something back, give credit. The sponsor stayed in reserve.", exact=True)
la_how.row([("ask", "what's blocking you?", "paper"), ("unblock", "texts in 1 day, not 9", "green"), ("show facts", "20 Apr · 2 items at risk", "blue"), ("offer back", "pickers test approvals", "y"), ("credit", "named in the status", "pink")],
           y=20, h=96, gap=34, size=17, subsize=12, arrows=True)
la_how.box(120, 150, 520, 80, "Dee: both items into the sprint of 23 March", "green", sub="done by 3 April", size=18, subsize=14)
la_how.box(120, 260, 520, 80, "the sponsor, Joost", "paper", sub="kept in reserve: never asked", size=18, subsize=14, dash=True)
la_how.note(380, 372, "influence: goal, facts, help, exchange, credit", "pen", size=17)

la_deep1 = Doodle(760, 260, "Five sources of influence a project manager has without authority over people. Information: the plan, the milestones, who waits for whom. Expertise: knowing how launches work. Relationships: people who trust you. Reciprocity: favours given and returned. Sponsorship: the sponsor's authority, borrowed rarely. Positional power over the team: none.",
                  "No positional power. Five other sources, in rough order of how often to use them.", exact=True)
la_deep1.row([("information", "plan, dates, who waits", "blue"), ("expertise", "how launches work", "blue"), ("relationships", "trust built early", "green"), ("reciprocity", "favours both ways", "y"), ("sponsor", "borrowed rarely", "paper")], y=40, h=110, size=16, subsize=12)
la_deep1.note(380, 196, "use from left to right; the sponsor last", "pen", size=17)
la_deep1.note(380, 232, "positional power over the team: none, and not needed", "red", size=15)

LEAD = dict(
    slug="leading-without-authority",
    kicker="a.k.a. leading the team: influence without authority",
    tldr="Most of the people a project needs don't report to the project manager. You lead them with what you have: a <b>shared goal</b> they care about, <b>facts</b> nobody else has assembled, <b>help</b> that removes what's blocking them, <b>exchange</b> (something back for them or their manager), and <b>credit</b> given in public. The sponsor's authority is real, but every time you borrow it, you spend trust you'll need later. Use it last.",
    chips=[("Family", "leading and balancing"), ("Lives in", "conversations, not documents"), ("Pairs with", "the role card, let the team decide, escalation")],
    pmbok=dict(covers="leading the team: influence without positional authority, motivation, recognition, servant leadership",
               domains=RES + ["stakeholders"], processes=["Lead the Team"], principles=["Build an empowered culture", "Be an accountable leader"], focus=["executing"],
               older="6th: “Develop Team” and “Manage Team” (9.4, 9.5), interpersonal skills, influencing. 7th: the Team domain and leadership principles."),
    problem_side="Larder, 16 March 2026",
    problem="""  <p class="lead">Two Rotterdam app items are slipping: <b>zones and slots in the app</b>, and <b>the store page</b>. Dee's team has given its sprint to approvals and an Android fix, both Grace's priorities, both sensible. Sanne isn't Dee's manager. She could ask Joost to tell Priya to tell Dee. <span class="hl-pink">It would work once, and she needs Dee's team for five more weeks.</span></p>
  <ul>
    <li>The people doing the work don't report to the project manager.</li>
    <li>Their own priorities are reasonable.</li>
    <li>Orders through the sponsor cost trust.</li>
  </ul>""",
    problem_figs=[la_problem],
    meanwhile=[("architect-6", "influencing-without-authority", "Ana's influencing without authority: architects persuade teams they don't manage, with evidence, timing and allies.",
                "Sanne does the same with Dee's team: ask, unblock, show the facts, offer something back, give credit, and keep the sponsor in reserve.")],
    analogy_side="the village choir",
    analogy="""  <p>A conductor of a <b>village choir</b> employs nobody. She can't make anyone come on a Thursday night. They come because the <b>music is worth singing</b>, because she's <b>prepared</b>, because she makes their evening <b>easy</b> (parts printed, car-sharing sorted), and because at the concert she <b>thanks them by name</b>. A conductor who had to threaten people would soon have no choir.</p>""",
    analogy_figs=[la_analogy],
    map=[("Music worth singing", "Opening a city on 27 April"),
         ("Being prepared", "The milestone, the burn-up, who waits for what"),
         ("Parts printed, cars sorted", "The store-page texts, in a day instead of nine"),
         ("A favour returned", "Yara's pickers testing approvals for Grace"),
         ("Thanks by name", "Dee's team named in the Friday status")],
    how_side="ask, unblock, show the facts, offer back, give credit",
    how="""  <p>Sanne starts with a question to Dee: <b>“what's blocking the Rotterdam items?”</b> The answer: the Dutch store-page texts from Priya's team, waiting nine days. Sanne gets them <b>the next day</b>. Then she shows Dee the <b>facts</b> nobody had put together: app ready is 20 April, the burn-up says two items are at risk, and Tomás's training plan depends on them. She <b>offers something back</b>: Yara's new pickers can test approvals on real handhelds in their training week, which Grace has been asking for. And in Friday's status, Dee's team is <b>named</b> for the Android fix. Dee puts both items into the sprint of 23 March; both are done by <b>3 April</b>. Joost is never asked. That reserve of trust is still there when Sanne needs it on 23 March, for the builder.</p>""",
    how_figs=[la_how],
    steps=[("Ask what's in their way", "Before asking for anything."),
           ("Remove a block yourself", "Fast, visibly."),
           ("Show facts they don't have", "Dates, dependencies, consequences."),
           ("Offer something back", "To them or their manager."),
           ("Give credit in public", "By name."),
           ("Borrow the sponsor's authority last", "And rarely.")],
    vocab=[("Influence", "Changing what others do without ordering them."),
           ("Positional power", "Authority from a job title over people who report to you."),
           ("Reciprocity", "People tend to return help they've received."),
           ("Servant leadership", "Leading by removing what stops people doing their work."),
           ("Recognition", "Visible appreciation of someone's contribution."),
           ("Matrix organisation", "People report to one manager but work on another's project.")],
    code=dict(file="rotterdam/43-dee-notes.md", note="Sanne's notes, 16–20 March 2026", plain=True, src="""
# LEADING WITHOUT AUTHORITY · Dee's team and two Rotterdam items

THE PROBLEM   zones + slots in the app, the store page: slipping (sprint went to approvals,
              Android fix: Grace's priorities). Sanne doesn't manage Dee.
1 ASK         Dee: what's blocking? → Dutch store-page texts from Priya's team, waiting 9 days
2 UNBLOCK     texts delivered Tue 17 Mar (Sanne with Priya)
3 FACTS       app ready 20 Apr · burn-up: 2 items at risk · Tomás's training needs them
4 EXCHANGE    Yara's new pickers test approvals on real handhelds, training week of 30 Mar
              (Grace had asked for this)
5 CREDIT      Friday status, 20 Mar: "Dee's team fixed the Android crash for all of Amsterdam"
RESULT        both items in the sprint of 23 Mar · done Fri 3 Apr
NOT USED      Joost (sponsor) · kept for when it's needed (23 Mar: the builder)
"""),
    tools="tools: a question, a block you can remove, a fact sheet, something to offer, and the Friday status.",
    deep_dive=dict(
        side="sources of influence, tactics that work, the favour bank, when to use the sponsor",
        intro="Every project manager in a matrix organisation leads people they don't manage. The skill can be learned. This chapter lists the sources of influence you actually have, the tactics that work and those that backfire, how the favour bank works, and when the sponsor's authority is the right tool.",
        parts=[
            ("What you have instead of authority", """  <p>A project manager rarely has <b>positional power</b> over the team. What they have, often more than anyone:</p>
  <ul>
    <li><b>Information</b>: the whole plan, the dates, who waits for whom. Nobody else has assembled it.</li>
    <li><b>Expertise</b>: how launches go, where they go wrong.</li>
    <li><b>Relationships</b>: built before they're needed, in the first weeks, over small things.</li>
    <li><b>Reciprocity</b>: help given earlier.</li>
    <li><b>The sponsor's authority</b>: real, borrowed, and expensive to use.</li>
  </ul>""", [la_deep1]),
            ("Tactics that work, and two that backfire", """  <p>Research on influence finds that the tactics that work best with peers are <b>rational persuasion</b> (facts and consequences), <b>consultation</b> (asking for their idea), <b>inspiration</b> (the goal), and <b>collaboration</b> (removing a block for them). Sanne used all four with Dee.</p>
  <p>Two backfire with peers: <b>pressure</b> (deadlines repeated more loudly) and <b>going over their head</b> without telling them. Both can get compliance once and cost commitment afterwards.</p>""", []),
            ("The favour bank", """  <p>Every favour is a deposit: texts fetched in a day, a tester found, a name in the status. When you need something, you make a withdrawal. A project manager who only ever asks runs an overdraft, and people start being busy when they see them coming.</p>
  <p>The deposits that count are the ones that cost you something and help them with <b>their</b> goals, not the project's. Yara's pickers testing approvals helped Grace, not Rotterdam.</p>""", []),
            ("When to use the sponsor", """  <p>Use the sponsor's authority when <b>a decision is above everyone in the room</b> (a threshold is crossed, two priorities conflict at the top), not to make a peer do what you want. Then do it openly: tell the person first that you're taking it up, and why. On 23 March Sanne went to Joost about the builder because €5,000 and a milestone were at stake. With Dee, two items in a sprint weren't, so the sponsor stayed out of it.</p>""", []),
        ]),
    dial=[("Light", "a small team you know", ["Ask, help, thank.", "No plan needed.", "Every day."]),
          ("Standard", "Rotterdam", ["Know what each team needs and what blocks it.", "Unblock fast, show facts, exchange, credit.", "The sponsor kept in reserve."]),
          ("Heavy", "large matrix organisations", ["Stakeholder and team engagement plans.", "Formal agreements with resource managers.", "Coaching in influence for project managers."])],
    baseline="Each line compares <b>pushing through the sponsor</b> to <b>asking, unblocking, showing facts, exchanging and giving credit</b>.",
    ratings=[(3, 4, "The team sees why Rotterdam matters."),
             (2, 4, "Commitments made by the team are kept."),
             (3, 4, "Blocks are found by asking."),
             (3, 4, "Facts are shared, not held."),
             (3, 5, "Joost wasn't spent on a sprint."),
             (2, 5, "Dee's team chose to commit."),
             (3, 4, "Exchanges create room for both sides."),
             (3, 3, "Neutral."),
             (3, 3, "It takes conversations, not documents.")],
    pitfalls=[("Ordering through the sponsor", "Works once.", "influence first; sponsor last."),
              ("Asking before helping", "An overdraft at the favour bank.", "remove a block first."),
              ("Pressure", "Compliance, not commitment.", "facts and consequences instead."),
              ("Credit kept for yourself", "People stop helping.", "name them in public.")],
    use=["With every team you don't manage.", "When a team's priorities clash with yours.", "Before escalating.", "From day one: build relationships before you need them."],
    skip=["Never; even with your own reports these work better than orders."],
    related=["<b>Let the Team Decide</b> (vol. 1)", "<b>When Do I Take It Upstairs?</b> (vol. 2)", "<b>Influencing without authority</b> (Ana, vol. 6)", "<b>Why Is the Team Arguing?</b> (next note)"],
    quiz=[("What was blocking Dee's team?", "The Dutch store-page texts from Priya's team, waiting nine days."),
          ("What did Sanne offer back?", "Yara's new pickers testing approvals on real handhelds, for Grace."),
          ("Why not ask Joost to order it?", "It would cost trust Sanne needed for five more weeks, and it wasn't above the room."),
          ("Name two influence tactics that backfire with peers.", "Pressure, and going over their head without telling them."),
          ("In April Ben's team refuses a late Rotterdam request that crosses no threshold. What does Sanne try first?", "Ask what's in their way, offer help or an exchange, show the facts; if it's still a no and nothing crosses a threshold, it stays a no.")],
    try_it="Pick one team you need but don't manage. Ask them this week what's blocking them, and remove one block yourself. Then thank them by name in your next status.",
    remember="The choir comes for the <span class=\"hl\">music</span>, the preparation, and being thanked <span class=\"hl\">by name</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, leading the team.",
             "Allan Cohen and David Bradford, <i>Influence Without Authority</i> (3rd ed., 2017).",
             "Gary Yukl, <i>Leadership in Organizations</i> (9th ed., 2019): influence tactics.",
             "Robert Cialdini, <i>Influence</i> (new and expanded ed., 2021): reciprocity."],
)

# ------------------------------------------------------------------ 14 Why Is the Team Arguing?
tc_problem = Doodle(760, 250, "Doodle of the rehearsal week, 20 to 24 April 2026. Tomás's new pickers say the handheld app is broken. Ben's team says the pickers are using it wrong. By Wednesday they talk about each other, not to each other. Three days before go or no-go.",
                    "“The app is broken.” “They're using it wrong.” By Wednesday they talk about each other, not to each other.")
tc_problem.box(20, 40, 330, 100, "Tomás's pickers", "y", sub="“the app is broken”", size=19, subsize=15)
tc_problem.box(410, 40, 330, 100, "Ben's team", "blue", sub="“they're using it wrong”", size=19, subsize=15)
tc_problem.note(380, 186, "three days before go / no-go", "red", size=20)
tc_problem.note(380, 222, "two positions; nobody has said what they need", "pen", size=17)

tc_analogy = Doodle(760, 240, "Doodle of two siblings arguing over one orange. Both want it. The parent cuts it in half and both are unhappy. Asked why, one wants the juice and the other the peel for a cake. They could each have had all of what they needed.",
                    "Two children, one orange. Cut in half, both lose. One wanted the juice, the other the peel.")
tc_analogy.row([("“I want the orange”", "position", "y"), ("“why?”", None, "paper"), ("juice · peel", "interests", "green")], y=50, h=90, gap=34, size=18, subsize=15, arrows=True)
tc_analogy.note(380, 196, "work on interests, not positions", "pen", size=19)

tc_how = Doodle(760, 400, "How the rehearsal-week conflict was worked through. The team stages: forming in the March training, storming in rehearsal week, norming after the daily triage, performing by the second week of hypercare. On Wednesday 22 April Sanne asked each side what it needed. Tomás: no wrong items on opening day. Ben: no risky code changes three days before release. A rule both could accept: every problem logged with the time and a photo; a fifteen-minute triage at 16:00 with both; fix it in code if it causes wrong items, otherwise a training note. Fourteen problems: four fixed in code, two of which caused wrong items, seven training notes, three parked.",
                "Positions → interests → a shared rule. 14 problems: 4 code fixes, 7 training notes, 3 parked.", exact=True)
tc_how.row([("forming", "March training", "paper"), ("storming", "rehearsal week", "pink"), ("norming", "16:00 triage", "y"), ("performing", "hypercare week 2", "green")], y=14, h=80, gap=34, size=17, subsize=13, arrows=True)
tc_how.box(14, 120, 360, 120, None, "y")
tc_how.head(194, 146, "Tomás needs", size=17)
tc_how.text(194, 180, "no wrong items on opening day", size=15)
tc_how.box(386, 120, 360, 120, None, "blue")
tc_how.head(566, 146, "Ben needs", size=17)
tc_how.text(566, 180, "no risky changes before release", size=15)
tc_how.box(14, 262, 732, 70, "rule: log it · triage at 16:00 · code if it causes wrong items, else training", "green", size=15)
tc_how.note(380, 370, "14 problems → 4 code fixes (2 caused wrong items) · 7 training notes · 3 parked", "pen", size=15)

CONFLICT = dict(
    slug="team-conflict",
    kicker="a.k.a. developing the team: team stages and managing conflict",
    tldr="New teams go through <b>stages</b>: polite at first (<b>forming</b>), then friction (<b>storming</b>), then shared ways of working (<b>norming</b>), then real flow (<b>performing</b>). Conflict is part of the second stage, not a sign of failure. Work it through by separating <b>positions</b> (“the app is broken”) from <b>interests</b> (“no wrong items on opening day”), agreeing the <b>facts</b>, and finding a <b>rule</b> both sides can live with. Collaborate when both needs matter; compromise when time is short; don't avoid.",
    chips=[("Family", "leading and balancing"), ("Lives in", "a short, regular meeting with both sides and a shared log"), ("Pairs with", "leading without authority, disagree and commit, issue log")],
    pmbok=dict(covers="developing the team: stages of team development, conflict and its handling, agreements on how to work",
               domains=RES + ["stakeholders"], processes=["Lead the Team"], principles=["Build an empowered culture"], focus=["executing"],
               older="6th: “Develop Team” and “Manage Team” (9.4, 9.5): Tuckman's stages, conflict management. 7th: the Team domain."),
    problem_side="Larder, rehearsal week, 20–24 April 2026",
    problem="""  <p class="lead">Rehearsal week. Rotterdam's new pickers run real orders on real handhelds. By Tuesday, Tomás's pickers say the app is <b>broken</b>; Ben's team says the pickers are <b>using it wrong</b>. By Wednesday the two groups talk <b>about</b> each other, not <b>to</b> each other. <span class="hl-pink">Go / no-go is on Friday.</span> Both sides are partly right, and neither has said what it actually needs.</p>
  <ul>
    <li>Each side defends a position.</li>
    <li>Nobody has agreed what the facts are.</li>
    <li>The clock makes everyone less patient.</li>
  </ul>""",
    problem_figs=[tc_problem],
    meanwhile=[("product-5", "disagree-and-commit", "Grace's disagree and commit: once a decision is made, people who argued against it commit to making it work.",
                "in rehearsal week Tomás and Ben don't need to agree on whose fault it is; they commit to one rule for every problem.")],
    analogy_side="the orange",
    analogy="""  <p>Two children argue over <b>one orange</b>. A parent cuts it in half; both are unhappy. If the parent had asked why, they'd have found that one wanted the <b>juice</b> and the other the <b>peel</b> for a cake. Each could have had all of what they needed. The argument was about positions; the solution was in the interests.</p>""",
    analogy_figs=[tc_analogy],
    map=[("“I want the orange”", "“The app is broken” · “they're using it wrong”"),
         ("Asking why", "Wednesday's question: what do you each need?"),
         ("The juice", "Tomás: no wrong items on opening day"),
         ("The peel", "Ben: no risky code changes before release"),
         ("Both get what they need", "Fix in code if it causes wrong items; otherwise train")],
    how_side="interests, facts, a rule, a short daily meeting",
    how="""  <p>Sanne sees the stage for what it is: the team formed politely in the March training; this is <b>storming</b>. On Wednesday she gets Tomás and Ben in a room and asks one question each: <b>what do you need from this week?</b> Tomás: <b>no wrong items on opening day</b>. Ben: <b>no risky code changes three days before release</b>. Neither need contradicts the other. They agree the <b>facts</b> first: every problem goes in a log with the time and a photo of the screen. Then a <b>rule</b>: a fifteen-minute triage at <b>16:00</b> with both; if a problem can cause a wrong item, Ben's team fixes it in code; otherwise it becomes a training note for Yara's team. By Friday: <b>14 problems</b>, <b>4 fixed in code</b> (2 of which really did cause wrong items), <b>7 training notes</b>, <b>3 parked</b>. Norming, just in time. By the second week of hypercare the store is performing.</p>""",
    how_figs=[tc_how],
    steps=[("Recognise the stage", "Storming is normal."),
           ("Get both sides in one room", "Not about each other."),
           ("Ask each what they need", "Interests, not positions."),
           ("Agree the facts", "A shared log, with evidence."),
           ("Agree a rule both can live with", "Who decides what, by when."),
           ("Meet briefly and often until it settles", "Then stop.")],
    vocab=[("Forming", "A new team, polite and unsure."),
           ("Storming", "Friction as people find out how to work together."),
           ("Norming", "Shared ways of working emerge."),
           ("Performing", "The team works smoothly towards the goal."),
           ("Position", "What someone says they want."),
           ("Interest", "Why they want it: the need underneath."),
           ("Collaborating", "Finding a solution that meets both sides' needs.")],
    code=dict(file="rotterdam/44-rehearsal-triage.md", note="rehearsal week, 20–24 April 2026", plain=True, src="""
# REHEARSAL WEEK · HANDHELD PROBLEMS · triage daily at 16:00 (Tomás, Ben, 15 min)

NEEDS        Tomás  no wrong items on opening day
             Ben    no risky code changes in the last three days before release
RULE         every problem logged: time, order, photo of the screen
             can it cause a wrong item? → code fix (Ben) · else → training note (Yara)

LOG (extract)                                                     DECISION
 1 Tue  swap screen hides the second item on small fonts           code (wrong item)
 4 Tue  "packed" pressed twice → order skips the cold bag          code (wrong item)
 6 Wed  scanner beeps but item not ticked (glove on the trigger)   training note
 9 Wed  label prints in the Noord format after a restart           code
12 Thu  battery icon unreadable in sunlight                        parked
TOTAL   14 problems: 4 code fixes (2 caused wrong items) · 7 training notes · 3 parked
STAGES  forming (March training) → storming (rehearsal) → norming (16:00 triage) →
        performing (hypercare week 2)
"""),
    tools="tools: a room, two questions, a shared log, and a fifteen-minute meeting at the same time every day.",
    dial=[("Light", "a small team", ["Ask each side what they need.", "Agree one rule.", "Done in an hour."]),
          ("Standard", "Rotterdam", ["Interests, facts, a rule.", "A short daily triage until it settles.", "Results logged."]),
          ("Heavy", "large or long conflicts", ["A facilitator or mediator.", "Team agreements in writing.", "Escalation paths for unresolved conflict."])],
    baseline="Each line compares <b>two groups defending positions</b> to <b>interests stated, facts agreed, and one rule with a daily triage</b>.",
    ratings=[(3, 4, "Effort goes to what affects customers."),
             (2, 4, "Problems are sorted daily, not argued about."),
             (2, 5, "Two real wrong-item bugs found before opening."),
             (2, 4, "A shared log replaces blame."),
             (3, 4, "Tomás and Ben both kept their need."),
             (2, 4, "The team made its own rule."),
             (3, 4, "Training absorbed what code didn't need to."),
             (2, 4, "Fixes target wrong items first."),
             (3, 3, "Fifteen minutes a day for a week.")],
    pitfalls=[("Treating storming as failure", "Panic, blame.", "it's a stage; work through it."),
              ("Splitting the orange", "A compromise nobody wanted.", "find the interests first."),
              ("Arguing without facts", "Opinions harden.", "a shared log with evidence."),
              ("Avoiding it", "It surfaces on opening day.", "one room, this week.")],
    use=["New teams, especially before a deadline.", "When groups talk about each other, not to each other.", "When a disagreement repeats.", "During rehearsals and hand-offs."],
    skip=["Healthy debate that's moving towards a decision: let it run."],
    related=["<b>How Do I Lead People Who Don't Report to Me?</b> (previous note)", "<b>Disagree and commit</b> (Grace, vol. 5)", "<b>What's in the Way Right Now?</b> (vol. 2)", "<b>Is This What We Asked For?</b> (vol. 3)"],
    quiz=[("Which stage was rehearsal week?", "Storming."),
          ("Position or interest: “no wrong items on opening day”?", "Interest."),
          ("What was the rule?", "Log every problem; if it can cause a wrong item, fix it in code; otherwise, a training note."),
          ("How many of the 14 problems were fixed in code?", "Four (two of which caused wrong items)."),
          ("After opening, Yara and the couriers' lead clash over the loading bay. What does Sanne do first?", "Ask each what they need from the bay, agree the facts (when, who, how long), and help them find a rule; Yara, as store manager, owns it from there.")],
    try_it="Think of a disagreement on your project. Write each side's position, then what each actually needs. Is there a rule that meets both needs?",
    remember="Ask <span class=\"hl\">why</span> before you cut the <span class=\"hl\">orange</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, leading and developing the team.",
             "Bruce Tuckman, “Developmental Sequence in Small Groups”, <i>Psychological Bulletin</i> (1965).",
             "Roger Fisher and William Ury, <i>Getting to Yes</i> (1981): positions and interests.",
             "Kenneth Thomas and Ralph Kilmann, <i>Thomas-Kilmann Conflict Mode Instrument</i> (1974)."],
)

# ------------------------------------------------------------------ 15 Are the People and Things Still There?
mr_problem = Doodle(760, 250, "Doodle of Wednesday 29 April 2026, day three. Orders are at 470 a day, well above the 350 planned. Three couriers are sick. Four e-bikes have flat tyres; the lease supplier promised repair in 24 hours. Two handhelds are broken. Everything in the plan was available on paper. Today, at 08:30, a lot of it isn't.",
                    "Day three: orders above plan, three couriers sick, four bikes down, two handhelds broken.")
mr_problem.row([("orders", "470 vs 350", "pink"), ("couriers", "3 sick", "pink"), ("e-bikes", "4 flat tyres", "pink"), ("handhelds", "2 broken", "y")], y=30, h=84, size=18, subsize=15)
mr_problem.note(380, 168, "available on paper; not at 08:30", "red", size=20)
mr_problem.note(380, 206, "the evening peak is in nine hours", "pen", size=18)

mr_analogy = Doodle(760, 240, "Doodle of a pilot's pre-flight walk-round. Every flight, the pilot walks round the aircraft: tyres, fuel, lights, the crew present and fit. The aircraft was certified months ago. The walk-round checks it's still true today.",
                    "A pilot walks round the aircraft before every flight. Certified months ago; checked again today.")
mr_analogy.row([("crew", "present, fit", "blue"), ("tyres", "pressure", "y"), ("fuel", "enough", "green"), ("lights", "working", "paper")], y=50, h=90, size=19, subsize=15)
mr_analogy.note(380, 196, "every flight, not once a month", "pen", size=19)

mr_how = Doodle(760, 400, "Rotterdam's daily availability check at 08:30 during hypercare, and what it caused on 29 April 2026. People on the rota against the orders forecast: three couriers short. Bikes ready: 36 of 40. Handhelds working: 28 of 30, spares 4 left. Deliveries due from suppliers: on time. Actions that day: Zuid lends three couriers for four days, agreed with Joost and Zuid's manager; the bike lease supplier held to its 24-hour repair, with a credit for the delay; the second hiring wave pulled forward from mid-May to 4 May. On 8 May the borrowed pickers go home as planned.",
                "08:30 every day: people, bikes, handhelds, deliveries. Short somewhere? Act before the evening peak.", exact=True)
board = [("couriers on rota", "22 of 25 needed", "pink"), ("pickers on rota", "13 of 13", "green"), ("e-bikes ready", "36 of 40", "y"), ("handhelds working", "28 of 30 · 4 spares", "y"), ("supplier deliveries", "on time", "green")]
for i, (a, b, f) in enumerate(board):
    y = 14 + i * 50
    mr_how.box(14, y, 260, 42, a, "paper", size=16, rx=5)
    mr_how.box(284, y, 220, 42, b, f, size=15, rx=5)
mr_how.box(520, 14, 226, 242, None, "blue")
mr_how.head(633, 40, "actions, 29 Apr", size=16)
for i, t in enumerate(["Zuid lends 3 couriers,", "4 days (Joost + Zuid)", "lease: 24 h repair held,", "credit for the delay", "2nd hiring wave:", "mid-May → 4 May"]):
    mr_how.text(633, 74 + i * 28, t, size=14)
mr_how.box(14, 290, 732, 70, "8 May: borrowed pickers go home, as planned · 11 May: hypercare exit", "green", size=15)
mr_how.note(380, 388, "checked every day at 08:30 by Yara and Sanne during hypercare", "pen", size=14)

MONITOR = dict(
    slug="monitoring-resources",
    kicker="a.k.a. monitoring and controlling resourcing: availability, suppliers and release",
    tldr="A plan assumes people and things are there when needed. <b>Check that it's still true</b>, as often as the work demands: daily during a launch, weekly otherwise. Compare what's <b>available</b> (people on the rota, equipment working, deliveries due) with what the <b>work needs today</b>. When something's short, act before the peak: borrow (with every owner's agreement), hold suppliers to their terms, pull plans forward. And <b>release</b> people and things on the date you promised.",
    chips=[("Family", "leading and balancing"), ("Lives in", "a short daily check during busy phases, weekly otherwise"), ("Pairs with", "estimating resources, acquiring resources, hypercare")],
    pmbok=dict(covers="checking that planned people, equipment and supplies are available; acting on shortfalls; supplier performance; releasing resources",
               domains=RES, processes=["Monitor and Control Resourcing"], principles=["Adopt a holistic view", "Be an accountable leader"], focus=["monitoring", "closing"],
               older="6th: “Control Resources” (9.6). 7th: the Team and Measurement domains."),
    problem_side="Larder, 29 April 2026",
    problem="""  <p class="lead">Day three. Orders are at <b>470 a day</b>, well above the 350 planned for the first month. <b>Three couriers</b> are sick. <b>Four e-bikes</b> have flat tyres, and the lease supplier, who promised repairs within 24 hours, hasn't come. <b>Two handhelds</b> are broken. <span class="hl-pink">Everything in the plan was available on paper. At 08:30 today, a lot of it isn't</span>, and the evening peak is nine hours away.</p>
  <ul>
    <li>Plans assume availability; reality removes some every day.</li>
    <li>Demand above plan uses up the margins faster.</li>
    <li>Suppliers' promises need checking too.</li>
  </ul>""",
    problem_figs=[mr_problem],
    analogy_side="the pilot's walk-round",
    analogy="""  <p>Before every flight, a pilot <b>walks round the aircraft</b>: tyres, fuel, lights, and checks the crew are present and fit. The aircraft was certified months ago. The walk-round isn't about whether it was ever airworthy; it's whether it is <b>today</b>. Nobody thinks that's a waste of the pilot's time.</p>""",
    analogy_figs=[mr_analogy],
    map=[("The walk-round", "The 08:30 check, every day of hypercare"),
         ("Crew present and fit", "Couriers and pickers on the rota"),
         ("Tyres", "E-bikes ready: 36 of 40"),
         ("Instruments working", "Handhelds: 28 of 30, 4 spares left"),
         ("Fuel for this flight", "Today's orders forecast: 470, not 350")],
    how_side="a daily check, action before the peak, release on time",
    how="""  <p>During hypercare Yara and Sanne do a <b>five-line check at 08:30</b>: couriers on the rota against today's forecast, pickers, e-bikes ready, handhelds working, supplier deliveries due. On 29 April three lines are short. By 10:00: <b>Zuid lends three couriers for four days</b>, agreed with Joost and Zuid's manager this time; the <b>lease supplier</b> is held to its 24-hour repair clause (bikes back by evening, a credit for the delay); two spare handhelds go into use, leaving four. And because orders are running at 470, not 350, Joost <b>pulls the second hiring wave forward</b> from mid-May to <b>4 May</b>. The other end of resourcing matters too: on <b>8 May</b> the borrowed pickers go home to Noord and Zuid, on the day promised, and Joost checks it happened.</p>""",
    how_figs=[mr_how],
    steps=[("List what the work needs today", "People, equipment, deliveries."),
           ("Check what's actually available", "At a fixed time, early."),
           ("Compare with today's demand", "Not last month's plan."),
           ("Act on shortfalls before the peak", "Borrow, chase suppliers, re-plan."),
           ("Hold suppliers to their terms", "And record when they miss."),
           ("Release on the promised date", "And confirm it happened.")],
    vocab=[("Availability", "Whether a person or thing can actually be used when needed."),
           ("Shortfall", "Less available than the work needs."),
           ("Service level (SLA)", "A supplier's promised response, like repair in 24 hours."),
           ("Absence rate", "The share of planned staff not available on a given day."),
           ("Release", "Returning people and things when the project no longer needs them."),
           ("Contingency staffing", "A plan for covering absence: on-call lists, loans.")],
    code=dict(file="rotterdam/45-availability.md", note="hypercare, Wednesday 29 April 2026, 08:30", plain=True, src="""
# ROTTERDAM · AVAILABILITY CHECK · Wed 29 Apr · 08:30 (Yara, Sanne)

TODAY'S ORDERS FORECAST   470 (plan for the first month: 350)
                          NEEDED   AVAILABLE   STATUS
couriers on the rota        25         22      SHORT 3 (sick)
pickers on the rota         13         13      ok (incl. 4 borrowed)
e-bikes ready               40         36      4 flat tyres; lease: repair in 24 h
handhelds working           30         28      2 broken → spares in use (4 left)
supplier deliveries          6          6      ok

ACTIONS BY 10:00
  Zuid lends 3 couriers, 29 Apr → 2 May (agreed: Joost, Zuid's manager)
  lease supplier held to 24 h repair → bikes back 18:00 · credit for the delay
  second hiring wave pulled forward: mid-May → Mon 4 May (Joost, operations)
RELEASE   borrowed pickers home Fri 8 May, as agreed (Joost confirmed)
"""),
    tools="tools: a five-line check, a fixed time, the forecast for today, and the phone numbers of whoever can lend or repair.",
    dial=[("Light", "a small team", ["“Who's here, what's working?” at the start of the day.", "Fix the gaps.", "No board."]),
          ("Standard", "Rotterdam", ["A five-line availability check at 08:30 in busy phases.", "Act before the peak.", "Release on the promised date."]),
          ("Heavy", "large operations", ["Workforce management systems.", "Supplier performance reports and penalties.", "Formal resource release procedures."])],
    baseline="Each line compares <b>assuming the plan's people and things are there</b> to <b>a daily check against today's demand, action before the peak, and release on time</b>.",
    ratings=[(3, 4, "Customers get their orders despite shortfalls."),
             (2, 4, "Gaps are closed before the evening peak."),
             (2, 4, "Shortfalls found at 08:30, not 17:30."),
             (2, 4, "Five lines anyone can read."),
             (3, 4, "Loans agreed with every owner, this time."),
             (3, 4, "Yara owns the check from week two."),
             (2, 4, "Hiring moved forward on real demand."),
             (3, 3, "Neutral."),
             (3, 3, "Ten minutes a day.")],
    pitfalls=[("Trusting the plan", "Availability changes daily.", "check at a fixed time."),
              ("Checking after the peak", "Too late to act.", "first thing in the morning."),
              ("Supplier promises unchecked", "Repairs drift.", "hold them to the terms."),
              ("Forgetting the release", "Borrowed people never go home.", "release on the date, and confirm.")],
    use=["Busy phases: launches, hypercare, peaks.", "When demand runs above plan.", "With borrowed people or leased equipment.", "At the end: releasing resources."],
    skip=["Quiet steady phases: weekly is enough."],
    related=["<b>How Many People, and What Else?</b> (this volume)", "<b>Where Do They Come From?</b> (this volume)", "<b>Hypercare after launch</b> (Grace, vol. 3)", "<b>Who Looks After It Now?</b> (vol. 2)"],
    quiz=[("What does the 08:30 check compare?", "What's available (people, bikes, handhelds, deliveries) with what today's demand needs."),
          ("Why did the second hiring wave move to 4 May?", "Orders ran at 470 a day, not 350."),
          ("What did the lease supplier owe?", "Repair within 24 hours; held to it, with a credit for the delay."),
          ("When did the borrowed pickers go home?", "8 May, as agreed, and Joost confirmed it."),
          ("After hypercare, who runs the check?", "Yara, as store manager, as part of running the store.")],
    try_it="Write the five things your project's work needs most each day or week. Check them at a fixed time for a week. What did you find that the plan assumed?",
    remember="Certified months ago. <span class=\"hl\">Walk round</span> it again <span class=\"hl\">today</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, monitoring and controlling resourcing.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 9.6 Control Resources.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

NOTES = [RACI, ESTIMATE_RES, ACQUIRE, LEVEL, LEAD, CONFLICT, MONITOR]
