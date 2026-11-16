# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 3 · How big is it? (estimating, part of Develop Schedule)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 3").
# Spine: PMBOK Guide, Eighth Edition. Names are PMI's; every explanation is in our own words.

SCHED = ["schedule"]


def curve(d, a, m, b, x0=60, x1=700, base=200, top=60):
    """A PERT-shaped (beta) curve from a to b with its peak at m, drawn as one path."""
    al = 1 + 4 * (m - a) / (b - a)
    be = 1 + 4 * (b - m) / (b - a)
    pts = []
    for i in range(61):
        t = i / 60
        pts.append((t, (t ** (al - 1)) * ((1 - t) ** (be - 1))))
    peak = max(y for _, y in pts) or 1
    path = " ".join(f"{'M' if i == 0 else 'L'}{x0 + t * (x1 - x0):.1f} {base - (y / peak) * (base - top):.1f}" for i, (t, y) in enumerate(pts))
    d.raw(f'<path class="d f-hl" d="{path} Z"/>')
    d.line(f"M{x0 - 20} {base} H{x1 + 20}", thin=True)
    return lambda v: x0 + (v - a) / (b - a) * (x1 - x0)


# ------------------------------------------------------------------ 05 How Long, Roughly?
em_problem = Doodle(760, 250, "Doodle of 3 February 2026. Femke asks Sanne one question in the corridor: will it fit in fifteen weeks? Sanne has three kinds of information: a store Larder opened before, a few rates from Noord, and teams who could list their work if asked. She has a day.",
                    "“Will it fit in fifteen weeks?” One day to answer, and three kinds of information.")
em_problem.row([("a store done before", "Zuid, 2024", "paper"), ("rates from Noord", "minutes per product", "paper"), ("teams' own lists", "if asked", "paper")], y=30, h=84, size=17, subsize=14)
em_problem.note(380, 168, "Femke: “will it fit in fifteen weeks?”", "red", size=19)
em_problem.note(380, 206, "three kinds of facts call for three ways to estimate", "pen", size=17)

em_analogy = Doodle(760, 240, "Doodle of three ways to guess how long a drive will take. From memory: last time to the coast took two hours. From a rate: 180 kilometres at 90 an hour. From the parts: the ring road, the motorway, the coast road, each timed. Each is right for a different moment.",
                    "How long is the drive? From last time, from a rate, or by adding up the legs.")
em_analogy.row([("“last time: 2 h”", "from memory", "y"), ("180 km ÷ 90", "from a rate", "blue"), ("ring + road + coast", "from the parts", "green")], y=50, h=90, size=16, subsize=14)
em_analogy.note(132, 190, "analogous", "red", size=19)
em_analogy.note(380, 190, "parametric", "red", size=19)
em_analogy.note(628, 190, "bottom-up", "red", size=19)

em_how = Doodle(760, 400, "Three estimates Sanne made on 5 February 2026. Analogous, for the fit-out: Zuid's took six weeks for 520 square metres, including a week of floor re-work; Rotterdam is 600 square metres, so five to seven weeks. Parametric, for stocking: 2,500 products at two and a half minutes each is about 104 hours, fifteen person-days, four days for a team of four, but deliveries arrive over ten working days, so the duration is ten days. Bottom-up, for the platform set-up: Eli lists nine pieces of work from half a day to three days each; they add up to twelve days.",
                "Analogous for the fit-out, parametric for stocking, bottom-up for the platform. Each says how sure it is.")
em_how.box(14, 14, 236, 250, None, "y")
em_how.head(132, 42, "analogous", size=19)
for i, t in enumerate(["fit-out", "Zuid: 6 weeks, 520 m²", "(1 week re-work)", "Rotterdam: 600 m²", "→ 5 to 7 weeks"]):
    em_how.text(132, 78 + i * 30, t, size=15)
em_how.note(132, 246, "± 30 %", "pen", size=17)
em_how.box(262, 14, 236, 250, None, "blue")
em_how.head(380, 42, "parametric", size=19)
for i, t in enumerate(["stocking", "2,500 × 2½ min", "= 104 h ≈ 15 days", "4 people: 4 days", "deliveries: 10 days"]):
    em_how.text(380, 78 + i * 30, t, size=15)
em_how.note(380, 246, "± 15 %", "pen", size=17)
em_how.box(510, 14, 236, 250, None, "green")
em_how.head(628, 42, "bottom-up", size=19)
for i, t in enumerate(["platform set-up", "9 pieces of work", "½ to 3 days each", "added up", "→ 12 days"]):
    em_how.text(628, 78 + i * 30, t, size=15)
em_how.note(628, 246, "± 10 % if complete", "pen", size=17)
em_how.box(120, 290, 520, 80, "answer to Femke, 5 Feb", "paper", sub="it fits, with no spare week; the fit-out is the long pole", size=18, subsize=14)

METHODS = dict(
    slug="estimating-methods",
    kicker="a.k.a. analogous, parametric and bottom-up estimating",
    tldr="There are three basic ways to estimate. <b>Analogous</b>: from a similar past job, adjusted (quick, rough). <b>Parametric</b>: a quantity times a rate you trust (good when the work is repetitive). <b>Bottom-up</b>: list the pieces and add them up (slower, most accurate, if the list is complete). Pick the method that fits the facts you have, say <b>how sure</b> each estimate is, and remember the trap: a rate tells you the <b>effort</b>, not the <b>duration</b>.",
    chips=[("Family", "how big is it?"), ("Lives in", "an estimates table: what, method, number, how sure"), ("Pairs with", "the WBS, three-point estimates, opportunity sizing")],
    pmbok=dict(covers="estimating duration and effort: analogous, parametric and bottom-up; accuracy ranges; effort versus duration",
               domains=SCHED + ["resources"], processes=["Develop Schedule"], principles=["Focus on value"], focus=["planning"],
               older="6th: “Estimate Activity Durations” (6.4) and “Estimate Activity Resources” (9.2). In the 8th they sit inside Develop Schedule."),
    problem_side="Larder, 3–5 February 2026",
    problem="""  <p class="lead">Femke stops Sanne in the corridor on 3 February: <b>“Will it fit in fifteen weeks?”</b> There is no plan yet. Sanne has three kinds of information: a store Larder opened before (<b>Zuid</b>, in 2024), a few <b>rates</b> from Noord (how long it takes to shelve a product), and <b>teams</b> who could list their work if she asked. <span class="hl-pink">She has a day, and one wrong answer would follow the launch to April.</span></p>
  <ul>
    <li>Different parts of the work come with different facts.</li>
    <li>A single number hides how sure it is.</li>
    <li>Effort and elapsed time are easy to confuse.</li>
  </ul>""",
    problem_figs=[em_problem],
    analogy_side="three ways to time a drive",
    analogy="""  <p>How long to drive to the coast? <b>From memory</b>: “last time it took two hours.” <b>From a rate</b>: 180 kilometres at 90 an hour. <b>From the parts</b>: the ring road at rush hour, the motorway, the coast road, each timed. Memory is quick and rough. The rate is good if the road is uniform. The parts are slowest to work out and most accurate, if you didn't forget the ferry.</p>""",
    analogy_figs=[em_analogy],
    map=[("“Last time: two hours”", "Analogous: Zuid's fit-out, adjusted for size"),
         ("Kilometres ÷ speed", "Parametric: 2,500 products × 2½ minutes"),
         ("Timing each leg", "Bottom-up: Eli's nine pieces of platform work"),
         ("Forgetting the ferry", "A bottom-up list with a missing piece"),
         ("Speed isn't arrival time", "Effort (104 hours) isn't duration (10 days)")],
    how_side="match the method to the facts, and say how sure",
    how="""  <p>Sanne uses all three, one per kind of fact. <b>Fit-out, analogous</b>: Zuid's took six weeks for 520 m², one week of it re-doing the floor; Rotterdam is 600 m², so <b>five to seven weeks</b>. <b>Stocking, parametric</b>: Noord's rate is about 2½ minutes per product (receive, place, label, scan), so 2,500 products is about <b>104 hours</b>, fifteen person-days, four days for a team of four. But suppliers deliver in slots over <b>ten working days</b>, so stocking takes ten days: the rate gave the effort, the deliveries set the duration. <b>Platform set-up, bottom-up</b>: Eli lists nine pieces of work, half a day to three days each: <b>twelve days</b>. Her answer to Femke on 5 February: it fits, with no spare week, and the fit-out is the long pole.</p>""",
    how_figs=[em_how],
    steps=[("Look at what facts you have for each piece", "A past job, a rate, a list."),
           ("Analogous where you have a similar job", "Adjust for size and differences."),
           ("Parametric where the work repeats", "Quantity × a rate you trust."),
           ("Bottom-up where the team can list the work", "Add up the pieces."),
           ("Separate effort from duration", "Who, how many, and what else sets the pace."),
           ("Write how sure each estimate is", "A range, not a point.")],
    vocab=[("Analogous estimate", "An estimate based on a similar past piece of work."),
           ("Parametric estimate", "A quantity multiplied by a rate per unit."),
           ("Bottom-up estimate", "The sum of estimates for the smaller pieces."),
           ("Effort", "Work time: person-hours or person-days."),
           ("Duration", "Elapsed working time from start to finish."),
           ("Rough order of magnitude", "A very early estimate, perhaps −25 % to +75 %.")],
    code=dict(file="rotterdam/20-estimates.md", note="Sanne with the leads, 5 February 2026", plain=True, src="""
# ROTTERDAM · FIRST ESTIMATES

WORKSTREAM          METHOD       BASIS                                ESTIMATE      HOW SURE
Store fit-out       analogous    Zuid 2024: 6 weeks, 520 m² (incl.     5–7 weeks     ± 30 %
                                 1 week floor re-work); RTM 600 m²
                    bottom-up    builder's quote, 12 activities        25 days       (see 3-point)
Cold room           quote        supplier: "up to 8 weeks"; on order   delivered     confirmed
                                 (13 Feb) confirmed for 27 March       27 Mar
Stocking            parametric   2,500 products × 2.5 min = 104 h      effort 15     ± 15 %
                                 → 4 days for 4 people                 person-days
                                 deliveries in slots over 10 days      duration 10 d
Training            parametric   40 people × (1 induction day +        ≈ 50 person-  ± 20 %
                                 20 practice orders × 6 min = 2 h)     days
Platform set-up     bottom-up    Eli: 9 pieces, ½–3 days each          12 days       (see 3-point)
Apps                story points Ben, Dee: 14 Musts = 61 points        see 4 Feb
                                                                       session

ANSWER TO FEMKE (5 Feb)  it fits in 15 weeks with no spare week; the fit-out is the long pole
"""),
    tools="tools: one past job, two or three rates you trust, the WBS, and a column headed “how sure”.",
    dial=[("Light", "a small job", ["One method, the one with the best facts.", "A range in one sentence.", "No table."]),
          ("Standard", "Rotterdam", ["A method per workstream.", "Effort and duration separated.", "An estimates table with “how sure”."]),
          ("Heavy", "large or contracted work", ["Estimating databases and calibrated rates.", "Independent estimates to compare.", "Estimates reviewed and baselined formally."])],
    baseline="Each line compares <b>one guessed number for the whole launch</b> to <b>a method per workstream, chosen by the facts available, with effort, duration and confidence</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "Each estimate rests on a stated basis."),
             (2, 4, "The long pole (the fit-out) shows up in February."),
             (2, 4, "“How sure” is written next to each number."),
             (3, 4, "Femke gets an answer with its basis."),
             (3, 4, "Bottom-up numbers come from the teams."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (4, 4, "A day's work.")],
    pitfalls=[("Effort as duration", "“104 hours, so three days.”", "ask what else sets the pace."),
              ("The analogy that isn't", "Zuid had different floors.", "adjust for the differences, out loud."),
              ("Bottom-up with a missing piece", "The forgotten ferry.", "check the list against the WBS."),
              ("A number without a range", "Heard as a promise.", "always say how sure.")],
    use=["Every estimate, at every stage.", "Early: analogous for a quick answer.", "Repetitive work: parametric.", "Before a baseline: bottom-up."],
    skip=["Never skip saying how sure. Skip bottom-up when the work can't yet be listed."],
    related=["<b>How Do We Break It Down?</b> (previous note)", "<b>How Sure Are We?</b> (next note)", "<b>Opportunity sizing</b> (Grace, vol. 2)", "<b>Cost estimates</b> (vol. 4)"],
    quiz=[("Analogous, parametric or bottom-up: “Zuid took six weeks, so…”?", "Analogous."),
          ("Stocking needs 104 hours of effort. Why does it take ten days?", "Deliveries arrive in slots over ten working days; the deliveries, not the labour, set the pace."),
          ("Which method is most accurate, and when?", "Bottom-up, if the list of pieces is complete."),
          ("On 5 February Joost says “the builder said five weeks, so let's write five weeks”. What does Sanne add?", "The basis (the builder's list) and how sure it is; the analogy with Zuid says five to seven."),
          ("A parametric rate came from Noord's night shift. Is it safe for Rotterdam's first week?", "Probably optimistic: new staff in a new store. Adjust it, and say so.")],
    try_it="Take your project's three biggest pieces of work. For each, write the estimate, the method, the basis in one line, and how sure you are. Then check one: is it effort or duration?",
    remember="A rate gives the <span class=\"hl\">effort</span>. Something else sets the <span class=\"hl\">pace</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, developing the schedule.",
             "Project Management Institute, <i>Practice Standard for Project Estimating</i> (2nd ed., 2019).",
             "Steve McConnell, <i>Software Estimation: Demystifying the Black Art</i> (2006)."],
)

# ------------------------------------------------------------------ 06 How Sure Are We?
tp_problem = Doodle(760, 250, "Doodle of 6 February 2026. Two estimates, two people pretty sure of them. The builder's site manager, Kees: twenty-five working days for the fit-out. Eli: twelve days for the platform set-up. Sanne asks each how sure. Both say: pretty sure. Neither number says what could go wrong, or by how much.",
                    "Two estimates, two people “pretty sure”. Neither number says what could go wrong.")
tp_problem.box(20, 30, 330, 100, "Kees (builder)", "y", sub="fit-out: 25 working days", size=19, subsize=15)
tp_problem.box(410, 30, 330, 100, "Eli", "blue", sub="platform set-up: 12 days", size=19, subsize=15)
tp_problem.note(185, 166, "“pretty sure”", "red", size=20)
tp_problem.note(575, 166, "“pretty sure”", "red", size=20)
tp_problem.note(380, 216, "one number hides the odds", "pen", size=19)

tp_analogy = Doodle(760, 240, "Doodle of a weather forecast. The forecaster doesn't say it will rain at three o'clock. They say: seventy percent chance of rain this afternoon. Nobody calls that a weak forecast. People take an umbrella, or don't, knowing the odds.",
                    "A forecaster says “70 % chance of rain”, not “rain at three”. People decide knowing the odds.")
tp_analogy.icon("cloud", 60, 50, 1.6)
tp_analogy.box(220, 50, 300, 90, "70 % chance of rain", "blue", sub="this afternoon", size=20, subsize=15)
tp_analogy.icon("hourglass", 600, 60, 2.0)
tp_analogy.note(380, 196, "a range with odds is a better forecast, not a weaker one", "pen", size=18)

tp_how = Doodle(760, 400, "The builder's three numbers for the fit-out, 6 February 2026. Best case 22 working days. Most likely 25. Worst case 34, if the electrical inspection is re-booked, materials are late and the floor cures slowly in cold weather. The PERT average is 26 days, give or take two. The planned 25 days has about a one in three chance. There is about an 84 percent chance of finishing within 28 working days: 9 April, with the builder off on Easter Monday. The curve leans to the right: more can go wrong than right.",
                "Best 22, likely 25, worst 34. Expected 26 ± 2. The 25-day plan has about a 1 in 3 chance.")
X = curve(tp_how, 22, 25, 34, x0=60, x1=700, base=240, top=70)
for v, t, c in [(22, "best 22", "pen"), (25, "likely 25", "pen"), (26, "expected 26", "red"), (28, "84 %: 28", "green"), (34, "worst 34", "pen")]:
    tp_how.line(f"M{X(v):.0f} 50 V250", thin=True, dash=True, color=("red" if c == "red" else ""))
    tp_how.note(X(v), 278 if v not in (26,) else 300, t, c, size=15)
tp_how.box(14, 320, 732, 64, "plan 3 April = 25 days: ≈ 1 in 3 · expected 7 April · 84 % by 9 April", "y", size=16)

tp_deep1 = Doodle(760, 260, "Two formulas for three-point estimates. Triangular: best plus likely plus worst, divided by three; for the fit-out, 81 divided by 3 is 27. PERT, or beta: best plus four times likely plus worst, divided by six; 156 divided by 6 is 26. The spread, one standard deviation: worst minus best, divided by six; 12 divided by 6 is 2.",
                  "Triangular gives 27, PERT gives 26. The spread: (worst − best) ÷ 6 = 2 days.")
tp_deep1.row([("triangular", "(O + M + P) ÷ 3", "paper"), ("PERT", "(O + 4M + P) ÷ 6", "y"), ("spread σ", "(P − O) ÷ 6", "blue")], y=30, h=90, size=19, subsize=15)
tp_deep1.row([("(22+25+34) ÷ 3", "= 27", "paper"), ("(22+100+34) ÷ 6", "= 26", "y"), ("(34−22) ÷ 6", "= 2", "blue")], y=140, h=80, size=16, subsize=20)
tp_deep1.note(380, 248, "O = best (optimistic) · M = most likely · P = worst (pessimistic)", "pen", size=15)

tp_deep2 = Doodle(760, 230, "Turning the PERT numbers into odds, using the rough normal-curve rule. The expected value has about a fifty percent chance. Expected plus one spread, about 84 percent. Plus two spreads, about 98 percent. For the fit-out: 26 days, 50 percent; 28 days, 84 percent; 30 days, 98 percent. The planned 25 days is half a spread below the expected value: about 31 percent.",
                  "Expected = 50 %. +1σ ≈ 84 %. +2σ ≈ 98 %. The 25-day plan is −½σ: about 31 %.")
tp_deep2.row([("25 days", "≈ 31 %", "pink"), ("26 days", "≈ 50 %", "y"), ("28 days", "≈ 84 %", "green"), ("30 days", "≈ 98 %", "green")], y=40, h=90, size=19, subsize=17)
tp_deep2.note(380, 170, "a rule of thumb, not a law: real delays bunch together", "pen", size=17)
tp_deep2.note(380, 204, "useful for choosing which date to promise, and how much buffer", "pen", size=16)

THREE_POINT = dict(
    slug="three-point-estimates",
    kicker="a.k.a. three-point estimating and PERT",
    tldr="Instead of one number, ask for three: the <b>best case</b>, the <b>most likely</b> and the <b>worst case</b> (with what would cause it). Combine them into an <b>expected value</b> and a <b>spread</b>; a common formula is (best + 4 × likely + worst) ÷ 6. Then you can say how likely each date is. Most estimates lean one way: more can go wrong than right, so the expected value is <b>later than the most likely</b>. A plan built on the most likely number is usually a plan you'll miss.",
    chips=[("Family", "how big is it?"), ("Lives in", "three columns in the estimates table, and one sentence of odds"), ("Pairs with", "float and buffers, the risk register, status forecasts")],
    pmbok=dict(covers="three-point estimates; triangular and PERT averages; spread; confidence levels for dates",
               domains=SCHED + ["risk"], processes=["Develop Schedule"], principles=["Be an accountable leader"], focus=["planning"],
               older="6th: three-point estimating in 6.4 (Estimate Activity Durations), and Monte Carlo in 11.4. 7th: estimating under the Planning domain."),
    problem_side="Larder, 6 February 2026",
    problem="""  <p class="lead">Two estimates matter more than the rest. <b>Kees</b>, the builder's site manager: the fit-out takes <b>25 working days</b>. <b>Eli</b>: the platform set-up takes <b>12</b>. Sanne asks each how sure they are. Both say “pretty sure”. <span class="hl-pink">Neither number says what could go wrong, or by how much</span>, and the fit-out has no room: 25 days from 2 March is exactly 3 April.</p>
  <ul>
    <li>A single number is heard as a promise.</li>
    <li>“Pretty sure” can't be compared or added up.</li>
    <li>What could go wrong is in people's heads, not in the plan.</li>
  </ul>""",
    problem_figs=[tp_problem],
    analogy_side="the weather forecast",
    analogy="""  <p>A weather forecaster doesn't say “it will rain at three.” They say <b>“70 % chance of rain this afternoon.”</b> Nobody thinks that's a weak forecast. It's an honest one, and people decide with it: take an umbrella, move the barbecue. A forecast that pretended to know the minute would be wrong most days, and nobody would plan around it.</p>""",
    analogy_figs=[tp_analogy],
    map=[("“Rain at three”", "“25 working days”"),
         ("“70 % chance of rain”", "“About a 1 in 3 chance of 25 days; 84 % by 28”"),
         ("Taking an umbrella", "Pricing weekend work before it's needed"),
         ("The forecaster's evidence", "The worst case's causes: inspection, materials, cold floors"),
         ("A forecast that leans", "More can go wrong than right")],
    how_side="three numbers, the causes of the worst, and the odds",
    how="""  <p>Sanne asks Kees and Eli for <b>three numbers</b> and what would cause the worst. Kees: best <b>22</b>, likely <b>25</b>, worst <b>34</b> (the electrical inspection re-booked, materials late, the screed curing slowly in a cold March). Eli: <b>8, 12, 24</b> (deposits on bottles need their own VAT rate; zone edges are messy). The PERT sum gives the fit-out an expected <b>26 days, give or take 2</b>, and the platform <b>13⅓, give or take 2⅔</b>. Read as odds, the 25-day plan has about a <b>1 in 3 chance</b>; the expected date is <b>7 April</b>; <b>9 April</b> is 84 % likely (Easter Monday is a day off for the builder). Sanne keeps 3 April as the target, because stocking needs it, and does two things: the plan says <b>“no spare week”</b> as its weak point, and she asks the builder in February what <b>weekend work</b> would cost. On 23 March that price is already on her desk.</p>""",
    how_figs=[tp_how],
    steps=[("Ask for best, likely and worst", "From the person who does the work."),
           ("Ask what would cause the worst", "That's a risk list for free."),
           ("Compute the expected value and spread", "(O + 4M + P) ÷ 6; (P − O) ÷ 6."),
           ("Turn it into odds for the dates that matter", "Your target, your promise."),
           ("Decide what to promise and what to buffer", "Out loud."),
           ("Prepare the response to the worst case", "Before it happens.")],
    vocab=[("Three-point estimate", "An estimate given as best, most likely and worst case."),
           ("PERT", "A method that weights the most likely value four times: (O + 4M + P) ÷ 6."),
           ("Triangular average", "(O + M + P) ÷ 3: gives the extremes more weight."),
           ("Standard deviation (σ)", "A measure of spread; for PERT, roughly (P − O) ÷ 6."),
           ("Confidence level", "How likely an estimate is to be met: P50, P80, P90."),
           ("Skew", "A distribution that leans: more room to be late than early.")],
    code=dict(file="rotterdam/21-three-point.md", note="Kees (builder) and Eli, 6 February 2026", plain=True, src="""
# ROTTERDAM · THREE-POINT ESTIMATES (working days)

                      BEST  LIKELY  WORST   WORST CASE IF…                   EXPECTED  SPREAD
Fit-out (builder)      22     25     34     electrical inspection re-booked;   26.0    ± 2.0
                                            materials late; screed cures slow
                                            in a cold March
Platform set-up (Eli)   8     12     24     deposits need their own VAT rate;  13.3    ± 2.7
                                            zone edges messy

FIT-OUT ODDS (from Mon 2 March; builder off Easter Monday 6 April)
  25 days  Fri  3 April   ≈ 31 %   ← the plan
  26 days  Tue  7 April   ≈ 50 %
  28 days  Thu  9 April   ≈ 84 %
DECISION  keep 3 April as the target (stocking needs it) · write "no spare week" as the
          plan's weak point · get a price for weekend work now, not when it's late
          → builder's price (12 Feb): one weekend ≈ €5,000
"""),
    tools="tools: three columns, one question (“what would cause the worst?”) and the (O + 4M + P) ÷ 6 sum.",
    deep_dive=dict(
        side="the formulas, the odds, adding estimates up, and what it can't fix",
        intro="Three-point estimating takes five minutes to ask for and is often misused. This chapter shows the two common formulas side by side, how to turn the result into odds for a date, how to add several estimates together without fooling yourself, and what no formula can fix.",
        parts=[
            ("Two formulas", """  <p>The <b>triangular</b> average treats the three numbers equally: (O + M + P) ÷ 3. The <b>PERT</b> (beta) average gives the most likely value four times the weight: (O + 4M + P) ÷ 6. For the fit-out, triangular says <b>27</b>, PERT says <b>26</b>. Both are later than the most likely 25, because the worst case is further from it than the best case is.</p>
  <p>Use PERT when the person estimating has done the work before and their “most likely” deserves trust; triangular when the three numbers are all guesses. The <b>spread</b> (one standard deviation) for PERT is about (P − O) ÷ 6: here, <b>2 days</b>.</p>""", [tp_deep1]),
            ("From numbers to odds", """  <p>A rough rule, borrowed from the bell curve: the expected value has about a <b>50 %</b> chance; one spread later, about <b>84 %</b>; two spreads later, about <b>98 %</b>. For the fit-out, that's 26, 28 and 30 days.</p>
  <p>The plan of <b>25 days</b> sits half a spread <i>below</i> the expected value: about <b>31 %</b>. That one sentence changed the February conversation. Nobody argued that the builder was wrong. They argued about what to do with a 1-in-3 date: keep it as the target, say plainly that there's no spare week, and price the rescue in advance.</p>
  <p>The rule is approximate. Real delays bunch together (one wet week delays several activities at once), so the true odds are usually a little worse.</p>""", [tp_deep2]),
            ("Adding estimates up", """  <p>When activities follow each other, their <b>expected values add up</b>. Their spreads don't: the <b>squares</b> of the spreads add, and you take the square root. The fit-out (26 ± 2) followed by stocking (best 9, likely 10, worst 14: expected 10.5 ± 0.8) gives 36.5 days, give or take √(4 + 0.7) ≈ <b>2.2</b>, not 2.8.</p>
  <p>Two lessons follow. A chain is more predictable than its parts suggest, if the parts vary independently. And the <b>planned</b> chain, built from the most likely values (25 + 10 = 35), has only about a <b>1 in 4</b> chance. Plans built on “most likely” numbers get less likely with every activity added.</p>""", []),
            ("What no formula fixes", """  <ul>
    <li><b>Optimism.</b> If the worst case is “a bit late”, the worst case is wrong. Ask “what would make this take twice as long?”</li>
    <li><b>Hidden padding.</b> If people pad their “likely”, the numbers look safe and the time gets used anyway. Keep the estimate honest and put the slack in a visible buffer (two notes on).</li>
    <li><b>Risks shared by many activities.</b> A strike, a flu wave, a re-booked inspector. These move many estimates at once, which is what the risk register is for (vol. 5).</li>
  </ul>
  <p>For big projects the next step is a <b>Monte Carlo simulation</b>: thousands of random runs through the whole schedule. Vol. 5 shows it in plain words.</p>""", []),
        ]),
    dial=[("Light", "small work", ["Ask “best and worst?” after every estimate.", "Say the range.", "No sums."]),
          ("Standard", "Rotterdam", ["Three points for the activities that matter.", "PERT and a spread.", "Odds for the target date, and a prepared response."]),
          ("Heavy", "large, uncertain work", ["Three points for every activity.", "Monte Carlo on the whole schedule.", "Promised dates at a chosen confidence (P80)."])],
    baseline="Each line compares <b>a single “pretty sure” number</b> to <b>best, likely and worst with causes, turned into odds for the dates that matter</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "Dates are promised with their odds."),
             (2, 5, "The worst case's causes are a free risk list."),
             (2, 4, "“1 in 3” is clearer than “pretty sure”."),
             (2, 4, "The steering group knew in February."),
             (3, 4, "Kees and Eli give the numbers and the causes."),
             (2, 4, "The rescue was priced before it was needed."),
             (3, 3, "Neutral."),
             (4, 3, "Five minutes per estimate, and a sum.")],
    pitfalls=[("A worst case that isn't", "“Maybe a day late.”", "ask what would make it take twice as long."),
              ("Promising the most likely", "A plan you'll usually miss.", "say the odds; promise later or buffer."),
              ("Adding spreads up", "The chain looks worse than it is.", "add squares, take the root."),
              ("Formula over judgment", "Shared risks ignored.", "use the risk register as well.")],
    use=["Estimates that set a key date.", "Work with a known worst case.", "Before promising a date to a sponsor.", "When someone says “pretty sure”."],
    skip=["Small, familiar work where the range is narrow and nothing depends on it."],
    related=["<b>How Long, Roughly?</b> (previous note)", "<b>How Much Can This Slip?</b> (this volume)", "<b>Where Are We, Really?</b> (vol. 2)", "<b>Simulation in plain words</b> (vol. 5)"],
    quiz=[("Best 22, likely 25, worst 34. PERT average?", "(22 + 100 + 34) ÷ 6 = 26."),
          ("Why is the expected value later than the most likely?", "The worst case is further from the likely case than the best case is: the estimate leans late."),
          ("What chance did the 25-day plan have?", "About 1 in 3 (31 %)."),
          ("Two activities in a row: 26 ± 2 and 10.5 ± 0.8. What is the spread of the pair?", "√(2² + 0.8²) ≈ 2.2, not 2.8."),
          ("Joost says “just tell the steering group 3 April, the odds will confuse them”. What does Sanne do?", "Gives 3 April as the target and says, in one line, that it has about a 1 in 3 chance with no spare week, and what is ready if it slips.")],
    try_it="Take the estimate that sets your project's most important date. Ask its owner for best, likely and worst, and what would cause the worst. Work out the PERT average. What are the odds of the date you've promised?",
    remember="Say <span class=\"hl\">“70 % chance of rain”</span>, not <span class=\"hl\">“rain at three”</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, estimating.",
             "D. G. Malcolm et al., “Application of a Technique for Research and Development Program Evaluation”, <i>Operations Research</i> (1959): the origin of PERT.",
             "Douglas Hubbard, <i>How to Measure Anything</i> (3rd ed., 2014): calibrated estimates.",
             "Daniel Kahneman, <i>Thinking, Fast and Slow</i> (2011): the planning fallacy."],
)

# ------------------------------------------------------------------ 07 Who Should Guess?
et_problem = Doodle(760, 250, "Doodle of the planning session on 4 February 2026 and Sanne's mistake in it. Before the platform estimate she says to Eli, kindly: Zuid's set-up took about two weeks, didn't it? Every estimate that follows is ten days. She has anchored the room. Nobody says the number they had in mind.",
                    "Sanne says “Zuid took about two weeks, didn't it?” Every estimate that follows is ten days.")
et_problem.box(20, 30, 300, 90, "Sanne: “about two weeks?”", "pink", size=16)
et_problem.row([("10", None, "paper"), ("10", None, "paper"), ("10", None, "paper"), ("10", None, "paper")], x=380, y=40, h=70, w=80, gap=10, size=24)
et_problem.arrow(322, 75, 378, 75, color="red")
et_problem.note(380, 170, "the first number in the room wins", "red", size=20)
et_problem.note(380, 210, "nobody says the number they had in mind", "pen", size=17)

et_analogy = Doodle(760, 240, "Doodle of a wine tasting. The judges score each wine on a card, privately, before anyone speaks. Only then do they compare and discuss the widest differences. If the most famous judge spoke first, everyone else's score would drift towards theirs.",
                    "Judges at a wine tasting score privately first, then compare. The famous judge speaks last.")
et_analogy.row([("score alone", "on a card", "y"), ("reveal together", "all at once", "blue"), ("discuss gaps", "high and low explain", "green"), ("score again", None, "y")], y=50, h=90, gap=34, size=16, subsize=13, arrows=True)
et_analogy.note(380, 196, "independent first, together second", "pen", size=19)

et_how = Doodle(760, 400, "How the planning session of 4 February 2026 was fixed, the same afternoon. Platform set-up: estimates written privately, revealed together: 8, 10, 12 and 24 days. Eli's 24 comes with a reason: bottle deposits need their own VAT rate and the zone edges are messy. After discussion, a second round: 10, 12, 12, 14. The app work is estimated in story points with planning poker: fourteen Musts come to 61 points; Ben's and Dee's teams have 8 to 10 points a sprint for Rotterdam, which means about seven sprints. There are five before 20 April. That number goes to Grace and becomes the reason for her MoSCoW session on 3 March.",
                "Round one alone, round two after the reasons. And a story-point sum that sent the app scope to Grace.")
et_how.box(14, 14, 360, 230, None, "blue")
et_how.head(194, 42, "platform: wideband Delphi", size=17)
et_how.row([("8", None, "paper"), ("10", None, "paper"), ("12", None, "paper"), ("24", None, "pink")], x=34, y=60, h=48, w=72, gap=10, size=20)
et_how.note(194, 136, "Eli's 24: deposits' VAT · zone edges", "red", size=15)
et_how.row([("10", None, "green"), ("12", None, "green"), ("12", None, "green"), ("14", None, "green")], x=34, y=156, h=48, w=72, gap=10, size=20)
et_how.note(194, 230, "round 2 → likely 12 (best 8 · worst 24)", "pen", size=15)
et_how.box(386, 14, 360, 230, None, "y")
et_how.head(566, 42, "apps: planning poker", size=17)
for i, t in enumerate(["14 Musts = 61 points", "capacity for Rotterdam:", "8–10 points a sprint", "→ about 7 sprints", "5 sprints before 20 April"]):
    et_how.text(566, 78 + i * 30, t, size=15)
et_how.note(566, 232, "→ to Grace: cut the Musts", "red", size=16)
et_how.box(120, 270, 520, 90, "3 March: Grace's MoSCoW", "green", sub="14 Musts → 6 · 61 points → 26 · about 3 sprints", size=18, subsize=14)

TEAM = dict(
    slug="estimating-with-the-team",
    kicker="a.k.a. expert judgment, wideband Delphi and planning poker",
    tldr="The people who will do the work make the best estimates, if they estimate <b>independently first</b>. Whoever speaks first sets an <b>anchor</b> that pulls every other number towards it. So: everyone writes a number privately, all reveal together, the <b>highest and lowest explain</b> their reasons (that's where the hidden risks are), then estimate again. For product work, teams do the same with <b>story points</b> and compare the total with their real <b>velocity</b>. The project manager asks the questions and keeps their own number to themselves.",
    chips=[("Family", "how big is it?"), ("Lives in", "a planning session; a record of rounds and reasons"), ("Pairs with", "let the team decide, MoSCoW, three-point estimates")],
    pmbok=dict(covers="estimating with the people who do the work: expert judgment, group techniques, story points and velocity; avoiding anchoring",
               domains=SCHED + ["resources"], processes=["Develop Schedule"], principles=["Build an empowered culture"], focus=["planning"],
               older="6th: expert judgment and group decision-making in 6.4; agile estimating in the <i>Agile Practice Guide</i>. 7th: estimating under the Planning domain."),
    problem_side="Larder, 4 February 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. In the planning session of 4 February, before the platform estimate, she says to Eli, trying to help: <b>“Zuid's set-up took about two weeks, didn't it?”</b> Every estimate that follows is <b>ten days</b>. <span class="hl-pink">She has anchored the room.</span> Eli had a much higher number in mind and a reason for it. He doesn't say it, because the project manager has just told everyone what the answer is.</p>
  <ul>
    <li>The first number spoken pulls every other one towards it.</li>
    <li>Agreement in the room hides the risks people know about.</li>
    <li>A project manager's “just checking” is heard as a target.</li>
  </ul>""",
    problem_figs=[et_problem],
    analogy_side="the wine tasting",
    analogy="""  <p>At a serious <b>wine tasting</b>, judges score each wine <b>on a card, privately</b>, before anyone speaks. Then they compare, and the judges with the highest and lowest scores explain what they tasted. Then they score again. If the most famous judge spoke first, everyone else's score would drift towards theirs, and the panel would taste one wine through one mouth.</p>""",
    analogy_figs=[et_analogy],
    map=[("Scoring on a card", "Writing an estimate privately"),
         ("Revealing together", "Turning the cards over at the same moment"),
         ("Highest and lowest explain", "Eli's 24: deposits' VAT and messy zone edges"),
         ("The famous judge speaking first", "Sanne's “about two weeks?”"),
         ("Scoring again", "Round two: 10, 12, 12, 14")],
    how_side="independent first, reasons second, then the sum against capacity",
    how="""  <p>Sanne sees what happened and fixes it the same afternoon. <b>Platform set-up</b>, again, as a small <b>wideband Delphi</b>: each person writes a number on a card; all turn them over together: <b>8, 10, 12, 24</b>. Eli explains his 24: bottle deposits need their own VAT rate, and Rotterdam's zone edges cut through streets. Round two: <b>10, 12, 12, 14</b>, and the three-point estimate (8, 12, 24) is recorded with its causes. For the <b>apps</b>, Ben's and Dee's teams use <b>planning poker</b>: the fourteen app Musts come to <b>61 points</b>. With approvals running too, the teams have <b>8–10 points a sprint</b> for Rotterdam: about <b>seven sprints</b>, and there are five before 20 April. Sanne doesn't argue with the sum. She takes it to Grace, and it becomes the reason for Grace's MoSCoW session on 3 March: <b>14 Musts become 6</b>, 26 points, about three sprints.</p>""",
    how_figs=[et_how],
    steps=[("Invite the people who will do the work", "Not their managers instead."),
           ("Keep your own number to yourself", "Ask questions, don't suggest answers."),
           ("Estimate privately, reveal together", "Cards, fingers, an app."),
           ("Ask the highest and lowest to explain", "Write their reasons down: they're risks."),
           ("Estimate again", "Agreement after reasons, not before."),
           ("Compare the total with real capacity", "Then take the gap to whoever owns scope.")],
    vocab=[("Anchoring", "The pull of the first number heard on all later estimates."),
           ("Wideband Delphi", "Estimating in rounds: private estimates, discussion of the spread, again."),
           ("Planning poker", "A team estimates stories with cards, revealed together."),
           ("Story point", "A relative size for a piece of product work, not hours."),
           ("Velocity", "How many points a team actually finishes per sprint."),
           ("Expert judgment", "Estimates from people who have done similar work.")],
    code=dict(file="rotterdam/22-estimating-session.md", note="planning session, 4 February 2026 (rounds redone that afternoon)", plain=True, src="""
# ROTTERDAM · ESTIMATING SESSION · 4 Feb 2026 · Ben, Dee, Eli, Tomás, Joost's ops lead

RULE (from round 2 on)  write privately · reveal together · high and low explain · again
                        Sanne gives no numbers

PLATFORM SET-UP (days)   round 1 (anchored): 10 10 10 10   ← "Zuid took ~2 weeks?" (Sanne)
                         round 1 (redone):    8 10 12 24
                         reasons for 24 (Eli): deposits need their own VAT rate;
                                               zone edges cut through streets
                         round 2:            10 12 12 14   → best 8 · likely 12 · worst 24
STORE TRAINING (Tomás)   round 1: 2 3 3 5 days per group → round 2: 3 3 3 4  → 3 days

APPS (story points, planning poker, Ben's and Dee's teams)
  14 app Musts                       61 points
  capacity for Rotterdam             8–10 points a sprint (approvals runs alongside)
  sprints needed                     ≈ 7   ·   sprints before 20 April: 5
  → to Grace (5 Feb): the app scope does not fit; which Musts can wait?
  → Grace's MoSCoW, 3 March: 6 Musts = 26 points ≈ 3 sprints
"""),
    tools="tools: index cards or fingers, a timer, a notebook for the reasons behind the outliers.",
    dial=[("Light", "a small team", ["Everyone says a number at the same moment.", "Outliers explain.", "Agree."]),
          ("Standard", "Rotterdam", ["Two rounds, written privately.", "Reasons recorded as risks.", "Totals compared with capacity."]),
          ("Heavy", "large estimates, contracts", ["Formal Delphi with an independent facilitator.", "Estimates compared with a second, separate team.", "Calibration against past actuals."])],
    baseline="Each line compares <b>estimates said out loud after the project manager's hint</b> to <b>private estimates revealed together, outliers explained, then totals compared with capacity</b>.",
    ratings=[(3, 4, "The capacity gap went to the person who owns scope."),
             (2, 4, "Estimates include what the doers know."),
             (2, 5, "The outliers' reasons are risks found in February."),
             (3, 4, "The spread of opinion is visible."),
             (3, 4, "Grace got a sum, not a complaint."),
             (2, 5, "The team's numbers are the team's."),
             (3, 4, "Scope was cut in March, not April."),
             (3, 3, "Neutral."),
             (3, 3, "Two rounds take longer than one.")],
    pitfalls=[("Anchoring", "The first number wins.", "private first; the project manager last, or never."),
              ("Managers estimate for teams", "Wrong numbers, nobody committed.", "ask the people who'll do it."),
              ("Averaging the outliers away", "The risk goes with them.", "make the high and low explain."),
              ("Points as hours", "Velocity becomes a target.", "points compare sizes; velocity is measured, not set.")],
    use=["Any estimate a team will be held to.", "When the room agrees suspiciously fast.", "Product work: story points.", "When one senior voice dominates."],
    skip=["One person doing the work alone: ask them, privately, for three numbers."],
    related=["<b>Let the Team Decide</b> (vol. 1)", "<b>MoSCoW and its traps</b> (Grace, vol. 2)", "<b>How Sure Are We?</b> (previous note)", "<b>Refinement that isn't a meeting marathon</b> (Grace, vol. 3)"],
    quiz=[("What is anchoring?", "The pull of the first number heard on every later estimate."),
          ("Why do the highest and lowest estimates explain?", "Their reasons are risks or shortcuts the others haven't thought of."),
          ("61 points, 8–10 points a sprint. How many sprints?", "About six to eight: roughly seven."),
          ("Joost opens an estimating round with “the builder told me five weeks”. What does Sanne do?", "Stop the round, ask everyone to write their own number first, and treat Joost's as one card among the rest."),
          ("The app sum didn't fit. Who decided what to cut?", "Grace, who owns the app scope (MoSCoW, 3 March). Sanne brought the sum.")],
    try_it="At your next estimate, ask everyone to write their number privately and turn them over together. Ask the highest and lowest to explain. Write their reasons down as risks.",
    remember="Score on a <span class=\"hl\">card</span> first. The famous judge speaks <span class=\"hl\">last</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, estimating with the team.",
             "Barry Boehm, <i>Software Engineering Economics</i> (1981): wideband Delphi.",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005): planning poker and velocity.",
             "Amos Tversky and Daniel Kahneman, “Judgment under Uncertainty: Heuristics and Biases”, <i>Science</i> (1974): anchoring."],
)

NOTES = [METHODS, THREE_POINT, TEAM]
