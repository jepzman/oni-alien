# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 3 · Holding the line (monitoring scope and schedule)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 3").
# Must-haves done (of 71), from the casebook: 26 Feb 33 · 5 Mar 34 · 12 Mar 41 · 19 Mar 45 · 27 Mar 49 · 3 Apr 55 ·
# 10 Apr 60 · 17 Apr 69 · 24 Apr 69 · 26 Apr 71. Plan line: 33 on 26 Feb → 71 on 24 Apr.

# ------------------------------------------------------------------ 13 Are We Still on Time?
DONE = [("26 Feb", 33), ("5 Mar", 34), ("12 Mar", 41), ("19 Mar", 45), ("27 Mar", 49), ("3 Apr", 55), ("10 Apr", 60), ("17 Apr", 69), ("24 Apr", 69)]


def burnup(d, upto=9, x0=70, x1=730, y0=40, y1=260, forecast=False):
    """Must-haves done per week against the plan line and the scope line (71)."""
    n = len(DONE) - 1
    X = lambda i: x0 + i * (x1 - x0) / n
    Y = lambda v: y1 - (v - 30) / (75 - 30) * (y1 - y0)
    d.line(f"M{x0} {y0 - 10} V{y1} H{x1 + 10}", thin=True)
    for v in (40, 50, 60, 70):
        d.text(x0 - 8, Y(v) + 5, str(v), "t t-soft", anchor="end", size=12)
    d.line(f"M{x0} {Y(71):.0f} H{x1}", color="red", dash=True)
    d.note(x1 - 4, Y(71) - 8, "scope: 71", "red", size=14, anchor="end")
    d.line(f"M{X(0):.0f} {Y(33):.0f} L{X(8):.0f} {Y(71):.0f}", dash=True, thin=True)
    d.note(X(5) - 10, Y(33 + 38 * 5 / 8) - 14, "plan", size=14, anchor="end")
    pts = " L".join(f"{X(i):.0f} {Y(v):.0f}" for i, (_, v) in enumerate(DONE[:upto]))
    d.line("M" + pts, color="green")
    for i, (t, v) in enumerate(DONE[:upto]):
        d.circle(round(X(i)), round(Y(v)), 4, "green")
    for i, (t, _) in enumerate(DONE):
        if i % 2 == 0:
            d.text(X(i), y1 + 20, t, "t t-soft", size=12)
    if forecast:
        i = 4
        d.line(f"M{X(i):.0f} {Y(49):.0f} L{X(i + 3.1):.0f} {Y(71):.0f}", color="pen", dash=True)
        d.line(f"M{X(i):.0f} {Y(49):.0f} L{X(8):.0f} {Y(65):.0f}", color="pen", dash=True)
        d.note(X(8) - 4, Y(65) + 40, "slow: 3 May →", "pen", size=13, anchor="end")
        d.note(X(7.1) - 10, Y(71) - 8, "fast: 17 Apr", "pen", size=13, anchor="end")
        d.note(X(i) + 30, Y(49) + 26, "from 27 Mar: 4–7 a week", "pen", size=13, anchor="start")
    return X, Y


st_problem = Doodle(760, 250, "Doodle of 13 March 2026, the day the baseline is approved. Femke asks how she will know, each week, whether the dates are holding. Sanne has two kinds of work and no single measure that fits both: the builder's activities run to a network and dates, the app teams' work runs in sprints and points.",
                    "“How will I know each week if the dates are holding?” Two kinds of work, no single measure.")
st_problem.box(20, 30, 330, 100, "the builder", "y", sub="activities, dates, a critical path", size=19, subsize=14)
st_problem.box(410, 30, 330, 100, "the app teams", "blue", sub="sprints, points, no dates", size=19, subsize=14)
st_problem.note(380, 170, "Femke: “are the dates holding?”", "red", size=19)
st_problem.note(380, 208, "one question, two kinds of evidence", "pen", size=18)

st_analogy = Doodle(760, 240, "Doodle of a long-distance runner checking a watch at each kilometre marker. At every marker: what time did I expect to pass here, what time is it, and at this pace when will I finish? The finish time is re-forecast at every marker, not at the end.",
                    "A runner re-forecasts the finish at every kilometre marker, not at the end.")
st_analogy.row([("km 10", "expected 50:00", "paper"), ("actual 51:30", "1½ min behind", "y"), ("at this pace", "finish 3:34", "blue")], y=50, h=90, gap=34, size=18, subsize=14, arrows=True)
st_analogy.note(380, 196, "every marker: expected, actual, new forecast", "pen", size=18)

st_how = Doodle(760, 330, "The burn-up of must-haves done, Thursday by Thursday, from 26 February to 24 April 2026, against the plan line from 33 to 71 and the scope line at 71. The actual line falls below the plan in March, to 49 against 52 on 27 March, then climbs faster after approvals in Rotterdam were moved to June: 55, 60, 69. It stays at 69 in the last week; the final two must-haves are done on 26 April.",
                "Must-haves done against the plan line. Behind in March, back on the line in April, two left at go / no-go.")
burnup(st_how)
st_how.note(380, 318, "green = done · dashed = plan · red = scope (71)", "pen", size=14)

st_deep1 = Doodle(760, 300, "A milestone trend chart, February to April 2026. Across: the Fridays the forecast was made. Up: the date forecast for two milestones. Fit-out done stays flat on 3 April, except one point on 23 March at 8 April, back to 3 April after the weekend work. App ready is above the chart before Grace's MoSCoW session, because 14 Musts didn't fit; from 6 March it reads 20 April, rises to 22 April in the last two weeks of March, and falls back to 20 April after approvals moved to June.",
                  "Flat lines are good news. A jump is news. A line that creeps up is a slip nobody has said out loud.")
rep = ["20 Feb", "27 Feb", "6 Mar", "13 Mar", "20 Mar", "23 Mar", "27 Mar", "3 Apr", "10 Apr"]
x0, x1, y0, y1 = 90, 730, 30, 230
X = lambda i: x0 + i * (x1 - x0) / (len(rep) - 1)
Y = lambda day: y1 - (day - 1) / (24 - 1) * (y1 - y0)
st_deep1.line(f"M{x0} {y0 - 10} V{y1} H{x1 + 10}", thin=True)
for dday, lab in [(3, "3 Apr"), (8, "8 Apr"), (20, "20 Apr"), (22, "22 Apr")]:
    st_deep1.text(x0 - 8, Y(dday) + 5, lab, "t t-soft", anchor="end", size=12)
    st_deep1.line(f"M{x0} {Y(dday):.0f} H{x1}", thin=True, dash=True)
g1 = [3, 3, 3, 3, 3, 8, 3, 3]
st_deep1.line("M" + " L".join(f"{X(i):.0f} {Y(v):.0f}" for i, v in enumerate(g1)), color="red")
for i, v in enumerate(g1):
    st_deep1.circle(round(X(i)), round(Y(v)), 4, "pink")
g3 = [(2, 20), (3, 20), (4, 22), (6, 22), (7, 20), (8, 20)]
st_deep1.line("M" + " L".join(f"{X(i):.0f} {Y(v):.0f}" for i, v in g3), color="pen")
for i, v in g3:
    st_deep1.circle(round(X(i)), round(Y(v)), 4, "blue")
for i in (0, 1):
    st_deep1.arrow(round(X(i)), round(Y(21)), round(X(i)), round(Y(24)) - 6, color="pen")
st_deep1.note(X(1) + 14, Y(24) + 8, "14 Musts: mid-May", "pen", size=12, anchor="start")
st_deep1.note(X(7), Y(3) - 12, "fit-out done", "red", size=14)
st_deep1.note(X(8), Y(20) + 22, "app ready", "pen", size=14, anchor="end")
for i, t in enumerate(rep):
    st_deep1.text(X(i), y1 + 22, t, "t t-soft", size=12)
st_deep1.note(380, 290, "forecast made on (across) · date forecast (up)", "pen", size=14)

st_deep2 = Doodle(760, 330, "The same burn-up as on 27 March 2026, with a forecast as a range. Twenty-two must-haves left. The last three weeks finished seven, four and four. At seven a week the line reaches 71 in about three weeks, 17 April. At four a week, in five and a half weeks, 3 May. Go or no-go is on 24 April, inside the range. That is why the status was amber, and why approvals in Rotterdam were moved.",
                  "On 27 March: 22 left at 4 to 7 a week → somewhere between 17 April and 3 May. Go / no-go (24 April) is inside the range.")
burnup(st_deep2, upto=5, forecast=True)
st_deep2.note(380, 318, "a forecast as a range, from the slowest and fastest recent weeks", "pen", size=14)

TRACKING = dict(
    slug="schedule-tracking",
    kicker="a.k.a. monitoring and controlling the schedule",
    tldr="Track a schedule with the measure that fits each kind of work. <b>Predictive</b> work: are the milestones' <b>forecast dates</b> moving, and how much <b>float</b> is left on the critical path? <b>Adaptive</b> work: a <b>burn-up</b> of finished items against the plan line, and a forecast <b>as a range</b> from the real pace. Plot the forecasts week by week, because a line that creeps is a slip nobody has said out loud. And every slip ends in a decision: recover, re-plan, or accept.",
    chips=[("Family", "holding the line"), ("Lives in", "two charts on Thursday: the milestone trend and the burn-up"), ("Pairs with", "status reports, critical path, release plans")],
    pmbok=dict(covers="measuring schedule progress against the baseline; milestone trends, float, burn-up and burn-down charts, forecasting; corrective action",
               domains=["schedule"], processes=["Monitor and Control Schedule"], principles=["Be an accountable leader", "Focus on value"], focus=["monitoring"],
               older="6th: “Control Schedule” (6.6), with schedule variance and earned schedule. 7th: the Measurement domain."),
    problem_side="Larder, 13 March → 24 April 2026",
    problem="""  <p class="lead">On <b>13 March</b> the steering group approves the baseline, and Femke asks: <b>“how will I know, each week, whether the dates are holding?”</b> It's a fair question with an awkward answer. Half of Rotterdam runs on a <b>network of dated activities</b> (the builder, stocking, hiring). The other half runs in <b>sprints and story points</b> with no dates inside them at all. <span class="hl-pink">One measure won't fit both</span>, and two unrelated charts would leave Femke to do the sum herself.</p>
  <ul>
    <li>A percentage of tasks says nothing about dates.</li>
    <li>Sprints don't produce dates; activities don't produce velocity.</li>
    <li>A single weekly snapshot can't show a slow creep.</li>
  </ul>""",
    problem_figs=[st_problem],
    analogy_side="the runner's kilometre markers",
    analogy="""  <p>A marathon runner checks the watch at every <b>kilometre marker</b>: when did I expect to pass here, when did I actually, and <b>at this pace, when will I finish?</b> The finish is re-forecast forty-two times, not once at the end. Nobody waits for kilometre forty to discover they've been slowing down since twenty.</p>""",
    analogy_figs=[st_analogy],
    map=[("Kilometre markers", "Thursdays at 09:30"),
         ("Expected time at the marker", "The plan line; the baseline milestone dates"),
         ("Pace", "Must-haves finished per week"),
         ("Re-forecast finish", "Forecast dates for each milestone, as a range"),
         ("Slowing since kilometre twenty", "A milestone line that creeps up week by week")],
    how_side="two charts, both forecasting, every Thursday",
    how="""  <p>Sanne tracks the two halves on their own terms and puts both on one page. <b>Predictive</b>: each Thursday the leads give a <b>forecast date</b> for every milestone, and Kees says how much <b>float</b> is left on the red chain. The forecasts go on a <b>milestone trend chart</b> (in the chapter below): flat is good, a jump is news. <b>Adaptive</b>: a <b>burn-up</b> of must-haves done against the plan line, 33 on 26 February rising to 71 on 24 April. In March the line sags: 49 against 52 on 27 March. The forecast, from the real pace, is a <b>range</b>: 17 April to 3 May, with go / no-go on 24 April inside it. That range is what sends approvals in Rotterdam to June (change C-03). In April the pace rises: 55, 60, 69. The last two must-haves are done on 26 April, after go / no-go with conditions. At the steering group Femke sees one line per milestone: baseline, forecast, trend.</p>""",
    how_figs=[st_how],
    steps=[("Pick a measure for each kind of work", "Milestone dates and float; a burn-up."),
           ("Collect forecasts on a fixed day", "From the people doing the work."),
           ("Plot them over time, not just this week", "Trends show creep."),
           ("Forecast as a range from the real pace", "Slowest and fastest recent weeks."),
           ("For every slip: recover, re-plan or accept", "And say which."),
           ("Report one line per milestone", "Baseline, forecast, trend.")],
    vocab=[("Schedule variance (in days)", "How far a forecast date is from its baseline."),
           ("Milestone trend chart", "Forecast dates of milestones plotted week by week."),
           ("Burn-up chart", "Work done rising towards a scope line; shows scope changes too."),
           ("Burn-down chart", "Work remaining falling towards zero."),
           ("Velocity", "Work finished per period, measured, not set."),
           ("Float erosion", "Float on a chain being used up week by week.")],
    code=dict(file="rotterdam/28-schedule-tracking.md", note="Thursday by Thursday, 13 March → 24 April 2026", plain=True, src="""
# ROTTERDAM · ARE WE STILL ON TIME?

MILESTONE FORECASTS (made on…)   13 Mar  20 Mar  23 Mar  27 Mar  3 Apr   10 Apr  17 Apr
  G1 fit-out done  (bl 3 Apr)    3 Apr   3 Apr   8 Apr   3 Apr   3 Apr ✓
  G2 stock in      (bl 17 Apr)   17 Apr  17 Apr  20 Apr  17 Apr  17 Apr  17 Apr  17 Apr ✓*
  G3 app ready     (bl 20 Apr)   20 Apr  22 Apr  22 Apr  22 Apr  20 Apr  20 Apr  20 Apr
  float on the fit-out's red chain: 0 · 0 · −2 (inspector) · 0 after weekend work (C-02)

MUST-HAVES DONE (of 71)  plan line 33 (26 Feb) → 71 (24 Apr), about 4¾ a week
  26 Feb 33 · 5 Mar 34 · 12 Mar 41 · 19 Mar 45 · 27 Mar 49 (plan 52) · 3 Apr 55 ·
  10 Apr 60 · 17 Apr 69 · 24 Apr 69 · 26 Apr 71
FORECAST ON 27 MAR  22 left · recent weeks 7, 4, 4 → 17 Apr (fast) to 3 May (slow)
                    go / no-go 24 Apr is inside the range → AMBER → approvals to June (C-03)
ACTIONS  23 Mar recover (weekend work) · 31 Mar re-plan (C-03) · 24 Apr accept 2 open,
         as conditions of go / no-go (fixed 26 Apr)
* G2 accepted 20 Apr after two aisles were relabelled (see: acceptance)
"""),
    tools="tools: a forecast date from each lead every Thursday, a burn-up drawn from the must-have board, and a chart that keeps last week's forecasts.",
    deep_dive=dict(
        side="milestone trends, burn-ups, forecasting with a range, and float",
        intro="The status page in Vol. 2 asked where the project would land. This chapter shows the instruments behind that answer for a hybrid schedule: a chart that catches creeping dates, a burn-up that can't hide scope changes, a forecast given as a range, and the one number to watch on a critical path.",
        parts=[
            ("The milestone trend chart", """  <p>Each Thursday, each milestone's owner gives a <b>forecast date</b>. Plot them: across, the day the forecast was made; up, the date forecast. Read the shape:</p>
  <ul>
    <li><b>Flat</b>: the date is holding. Fit-out done was flat on 3 April, except one point.</li>
    <li><b>A jump</b>: news, usually a single event. 23 March: the inspector. It came back down after the weekend work.</li>
    <li><b>A slow climb</b>: a slip nobody has announced. App ready crept from 20 to 22 April in late March. That creep, not a crisis, is what the chart is for.</li>
  </ul>
  <p>Before 6 March, app ready was off the top of the chart: fourteen Musts didn't fit before 20 April. That's the estimating session's sum, seen as a trend.</p>""", [st_deep1]),
            ("Burn-up, not burn-down", """  <p>A <b>burn-down</b> shows work remaining falling to zero. A <b>burn-up</b> shows work done rising towards a separate <b>scope line</b>. The difference matters when scope changes: on a burn-down, adding scope looks like going backwards, and cutting scope looks like progress. On a burn-up, the scope line moves and everyone can see it.</p>
  <p>Rotterdam's scope line stayed at 71 throughout: C-03 moved approvals out of the launch, but approvals was a Should, not one of the 71. What C-03 changed was the <b>pace</b>: Ben's team had a week back, and the next three weeks finished 6, 5 and 9.</p>""", []),
            ("Forecast as a range", """  <p>A single forecast from an average pace hides how unsure it is. Use the <b>fastest and slowest recent weeks</b> instead. On 27 March: 22 must-haves left; the last three weeks finished 7, 4 and 4. At 7 a week, done in about three weeks: <b>17 April</b>. At 4 a week, in five and a half: <b>3 May</b>. Go / no-go, 24 April, is inside the range.</p>
  <p>That sentence is worth more than any colour. It says the date is possible but not safe, and it says how much faster the team must go (5½ a week) for it to be safe. The steering group's response, four days later, was to remove work rather than hope for speed.</p>""", [st_deep2]),
            ("Float: the number to watch on a critical path", """  <p>For predictive work, the single most useful weekly number is the <b>float left on the critical path</b>. It starts at zero on a tight plan like Rotterdam's (no buffer). Any negative number is a slip at the end of the same size: on 23 March, −2 working days. Recovery means getting back to zero (crashing, fast-tracking) or moving the baseline (a change).</p>
  <p>Larger projects also measure schedule performance in money terms (earned value) and in time terms (earned schedule). Vol. 4 does those sums with Rotterdam's budget.</p>""", []),
        ]),
    dial=[("Light", "one team", ["A burn-up on the wall.", "A forecast range each week.", "Said at the stand-up."]),
          ("Standard", "Rotterdam", ["Milestone forecasts and float, every Thursday.", "A must-have burn-up with a range forecast.", "One line per milestone for the steering group."]),
          ("Heavy", "large programmes", ["Schedule variance and earned schedule.", "Float erosion and critical path reports.", "Monte Carlo forecasts of key milestones."])],
    baseline="Each line compares <b>a weekly percentage complete</b> to <b>milestone forecasts plotted over time, float on the red chain, and a burn-up with a range forecast</b>.",
    ratings=[(3, 4, "Forecasts are about the milestones that matter."),
             (2, 5, "Creep is seen weeks before the date."),
             (2, 4, "The forecast range triggered C-03 in March."),
             (2, 5, "Two charts anyone can read."),
             (3, 5, "Femke sees baseline, forecast and trend."),
             (3, 4, "Forecasts come from the people doing the work."),
             (3, 4, "Every slip ends in recover, re-plan or accept."),
             (3, 3, "Neutral."),
             (3, 3, "Ten minutes on Thursdays to update.")],
    pitfalls=[("One measure for all work", "Percentages of mixed things.", "milestones and float for predictive, burn-up for adaptive."),
              ("Only this week's snapshot", "Creep is invisible.", "plot the forecasts over time."),
              ("A point forecast", "False certainty.", "a range from the slowest and fastest weeks."),
              ("Burn-down hiding scope changes", "Cuts look like progress.", "burn-up with a scope line.")],
    use=["Every week once there is a schedule baseline.", "Hybrid projects with dates and sprints.", "When a sponsor asks “are the dates holding?”", "When forecasts have been flat for suspiciously long."],
    skip=["Never; shrink it to one forecast per milestone."],
    related=["<b>Where Are We, Really?</b> (vol. 2)", "<b>What Decides the Finish Date?</b> (this volume)", "<b>Roadmap vs release plan</b> (Grace, vol. 2)", "<b>Earned value</b> (vol. 4)"],
    quiz=[("What does a slow upward line on a milestone trend chart mean?", "A slip that hasn't been announced: the forecast is creeping."),
          ("Why a burn-up rather than a burn-down?", "The scope line is separate, so scope changes are visible and can't look like progress."),
          ("22 left; recent weeks 7, 4 and 4. The forecast range?", "About 3 weeks at 7 a week, 5½ at 4 a week."),
          ("What does −2 float on the critical path mean?", "The end date will slip two working days unless something recovers it."),
          ("On 17 April the burn-up stands at 69, with go / no-go a week away and the last two must-haves hard. What does Sanne prepare?", "A go / no-go recommendation with conditions: the two must-haves as named conditions with owners and a date (they were fixed on 26 April).")],
    try_it="Start a milestone trend chart today: for each of your project's milestones, write this week's forecast date in a column. Do it again next week, without changing last week's. In a month, read the shapes.",
    remember="Check the watch at every <span class=\"hl\">marker</span>, and re-forecast the <span class=\"hl\">finish</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Schedule domain, monitoring and controlling the schedule.",
             "Project Management Institute, <i>Practice Standard for Scheduling</i> (3rd ed., 2019).",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005): burn charts and velocity ranges.",
             "Walt Lipke, “Schedule Is Different”, <i>The Measurable News</i> (2003): earned schedule."],
)

# ------------------------------------------------------------------ 14 Is This What We Asked For?
vs_problem = Doodle(760, 250, "Doodle of Gate 2 on Friday 17 April 2026. The stocking team reports done: 2,500 products on the shelves, every label scanned against its product, a hundred percent. Tomás walks the aisles with a picker's handheld and stops at aisle 14: the labels carry Noord's aisle codes. The handheld sends pickers by Rotterdam's codes. Every label was correct, and two aisles were wrong.",
                    "Every label matched its product: 100 %. Two aisles still sent pickers to the wrong place.")
vs_problem.box(20, 30, 330, 100, "stocking team: done", "green", sub="2,500 products · scan check 100 %", size=18, subsize=14)
vs_problem.box(410, 30, 330, 100, "Tomás at aisle 14", "pink", sub="labels say N-14; handheld says R-14", size=18, subsize=14)
vs_problem.note(380, 176, "correct, and not what was asked for", "red", size=20)
vs_problem.note(380, 214, "the check measured the wrong thing", "pen", size=18)

vs_analogy = Doodle(760, 240, "Doodle of a tailor and a client. Before handing over a suit, the tailor checks the seams, the buttons and the measurements against the order: that is the tailor's own check. Then the client puts it on, walks, sits down, and says whether it is what they asked for. Both are needed, and only the client can do the second.",
                    "The tailor checks the seams. Only the client, wearing it, can say it's what they asked for.")
vs_analogy.box(20, 40, 330, 100, "the tailor checks", "y", sub="seams · buttons · measurements", size=19, subsize=14)
vs_analogy.box(410, 40, 330, 100, "the client tries it on", "blue", sub="walks · sits · “yes, this”", size=19, subsize=14)
vs_analogy.note(185, 180, "quality control", "red", size=19)
vs_analogy.note(575, 180, "validating scope", "red", size=19)

vs_how = Doodle(760, 400, "How Rotterdam's eight deliverable groups were accepted, April and May 2026. Each by the person named in the scope statement, against criteria written in February, after the team's own check. Store fitted: Joost, 3 April, with two conditions. Payments and legal: Lena, 13 April. Store stocked: Tomás rejects two aisles on 17 April, accepts on 20 April after relabelling. City set up: Eli, 17 April. Rotterdam in the apps: Grace, 20 April. Staff trained: Tomás, 17 April. Marketing: Priya, 24 April. Hypercare: exit criteria met, 11 May.",
                "Eight groups, eight owners, criteria from February. The team checks first; the owner accepts.", exact=True)
rows_ = [("store fitted", "Joost", "3 Apr + 2 fixes", "y"), ("pay + legal", "Lena", "13 Apr", "green"), ("store stocked", "Tomás", "17 Apr no · 20 Apr yes", "pink"),
         ("city set up", "Eli", "17 Apr", "green"), ("staff trained", "Tomás", "17 Apr", "green"), ("Rotterdam in apps", "Grace", "20 Apr", "green"),
         ("marketing", "Priya", "24 Apr", "green"), ("hypercare", "exit criteria", "11 May", "green")]
for i, (t, who, when, f) in enumerate(rows_):
    r, c = divmod(i, 2)
    x, y = 14 + c * 372, 14 + r * 82
    vs_how.box(x, y, 170, 66, t, "paper", sub=who, size=15, subsize=13)
    vs_how.box(x + 178, y, 180, 66, when, f, size=13)
vs_how.note(380, 362, "the team's own check first (quality control) · then the owner accepts (validation)", "pen", size=15)

VALIDATE = dict(
    slug="validate-scope",
    kicker="a.k.a. validating scope: formal acceptance of deliverables",
    tldr="<b>Validating scope</b> means the people who asked for each deliverable <b>formally accept</b> it, against criteria agreed <b>in advance</b>. It isn't the same as quality control. <b>Quality control</b> is the team checking that the work is correct; <b>validation</b> is the customer checking that it's <b>what they asked for</b>. Do control first, then validation, then record the acceptance. Something can pass every internal check and still be the wrong thing.",
    chips=[("Family", "holding the line"), ("Lives in", "an acceptance log: deliverable, owner, criteria, date, conditions"), ("Pairs with", "phase gates, definition of done, the scope statement")],
    pmbok=dict(covers="formal acceptance of deliverables by the customer or sponsor; acceptance criteria; the difference from quality control",
               domains=["scope", "stakeholders"], processes=["Validate Scope"], principles=["Embed quality into processes and deliverables", "Focus on value"], focus=["monitoring", "closing"],
               older="6th: “Validate Scope” (5.5), after Control Quality (8.3). 7th: acceptance under the Delivery domain."),
    problem_side="Larder, 17–20 April 2026",
    problem="""  <p class="lead">Gate 2, Friday <b>17 April</b>. The stocking team reports done: <b>2,500 products</b> on the shelves, every label scanned against its product, <b>100 %</b>. Tomás walks the aisles with a picker's handheld and stops at aisle 14. The labels carry <b>Noord's aisle codes</b>, from the template the label printer was set up with. The handheld sends pickers by <b>Rotterdam's</b>. <span class="hl-pink">Every label was correct, and two aisles would send pickers to the wrong place.</span></p>
  <ul>
    <li>The team's check asked “is the label right for the product?”</li>
    <li>Tomás's need was “can a picker find it?”</li>
    <li>Only the person who will use it can check the second.</li>
  </ul>""",
    problem_figs=[vs_problem],
    meanwhile=[("product-3", "definition-ready-done", "Grace's definition of done (February) is the team's own check on each story; her acceptance at Gate 3 is a separate step.",
                "at Gate 2 Tomás learns the same difference on the shop floor: the team's scan check passed, and his acceptance didn't.")],
    analogy_side="the tailor and the client",
    analogy="""  <p>Before handing over a suit, a good <b>tailor checks</b> the seams, the buttons and the measurements against the order. Then the <b>client puts it on</b>, walks across the room, sits down, and says whether it's what they asked for. Both checks are needed. Only the client can do the second, and a suit with perfect seams can still pull at the shoulders.</p>""",
    analogy_figs=[vs_analogy],
    map=[("The tailor's check", "The scan check: every label matches its product"),
         ("The client tries it on", "Tomás walking the aisles with a picker's handheld"),
         ("Perfect seams, pulls at the shoulders", "Correct labels with Noord's aisle codes"),
         ("The order", "Acceptance criteria written in February (R-08, R-23…)"),
         ("“Yes, this”", "Acceptance recorded, with any conditions")],
    how_side="control first, then the owner accepts against criteria from February",
    how="""  <p>Tomás rejects <b>two aisles</b>, not the gate. The stocking team reprints and relabels them over the weekend; Tomás walks them again on <b>Monday 20 April</b> and accepts. Sanne records it and uses it to fix the process for the other groups: <b>every deliverable is accepted by the person named in the scope statement</b>, against the criteria written in February, <b>after</b> the team's own check. Sanne arranges each acceptance; she never accepts anything herself. The <b>acceptance log</b> fills up: Joost accepts the store from the builder on 3 April (two conditions), Lena accepts payments and legal on 13 April, Grace accepts the app at Gate 3 on 20 April by placing real orders in each zone, Priya accepts the marketing on 24 April, and the hypercare exit criteria close the last group on 11 May.</p>""",
    how_figs=[vs_how],
    steps=[("Write acceptance criteria early", "In the scope statement, from the requirements."),
           ("Name who accepts each deliverable", "The person who asked for it, or will use it."),
           ("Let the team check first", "Quality control: is it right?"),
           ("Then the owner tries it the way it will be used", "Validation: is it what we asked for?"),
           ("Accept, accept with conditions, or reject the part", "Not the whole, if only a part fails."),
           ("Record it", "Who, when, against what, with which conditions.")],
    vocab=[("Validate scope", "Formal acceptance of completed deliverables by the customer or sponsor."),
           ("Control quality", "The team checking that work meets its requirements."),
           ("Acceptance criteria", "Conditions agreed in advance that a deliverable must meet."),
           ("Accepted deliverable", "One the owner has formally signed off."),
           ("Conditional acceptance", "Accepted, with named fixes, owners and dates."),
           ("User acceptance test", "The users trying the result the way they'll use it.")],
    code=dict(file="rotterdam/29-acceptance-log.md", note="April and May 2026", plain=True, src="""
# ROTTERDAM · ACCEPTANCE LOG (criteria from the scope statement, 16 Feb)

DELIVERABLE          ACCEPTED BY  TEAM CHECK FIRST              DATE     RESULT
1 store fitted       Joost        builder's snag list            3 Apr   accepted, 2 conditions
                                                                         (fixed 7 Apr)
6 payments + legal   Lena         registrations on file         13 Apr   accepted
3 store stocked      Tomás        scan check: 100 % match       17 Apr   REJECTED: aisles 14
                                                                         and 15 carry Noord codes
                                  relabelled 18–19 Apr          20 Apr   accepted
4 city set up        Eli          nightly check: 0 errors       17 Apr   accepted
2 staff trained      Tomás        20 practice orders each       17 Apr   accepted
5 Rotterdam in apps  Grace        Ben's definition of done      20 Apr   accepted (real orders
                                                                         in RTM-1, -2, -3)
7 launch marketing   Priya        waitlist push tested          24 Apr   accepted
8 hypercare          exit         tickets < 3 per 100, no P1    11 May   met (Gate 5)
                     criteria     for five days

RULE (from 17 Apr)  the team checks first · the named owner accepts, the way it will be
                    used · reject the part, not the whole · Sanne arranges, never accepts
"""),
    tools="tools: the acceptance criteria from the scope statement, the person who asked, and the deliverable used the way it will be used.",
    dial=[("Light", "a small deliverable", ["Show it to the person who asked.", "“Is this what you wanted?”", "A message saying yes."]),
          ("Standard", "Rotterdam", ["Criteria written in February.", "Team check, then the owner tries it for real.", "An acceptance log with conditions."]),
          ("Heavy", "contracts", ["Formal acceptance tests and certificates.", "Acceptance tied to payment.", "Disputes handled under the contract."])],
    baseline="Each line compares <b>“the team says it's done”</b> to <b>the named owner accepting each deliverable against criteria from February, after the team's own check</b>.",
    ratings=[(3, 5, "Deliverables are checked against the need, not just the spec."),
             (3, 4, "Rejections happen at the gate, not on opening day."),
             (2, 4, "Two wrong aisles found before customers ordered."),
             (3, 4, "The log shows who accepted what, and when."),
             (3, 5, "Owners signed for their own deliverables."),
             (3, 4, "Teams know who will judge their work, and how."),
             (3, 3, "Neutral."),
             (2, 5, "Control and validation both happen."),
             (3, 3, "An hour per group.")],
    pitfalls=[("The team accepts its own work", "Correct, not right.", "the person who asked accepts."),
              ("Criteria written at the gate", "They bend to fit.", "write them in the scope statement."),
              ("Rejecting everything for one part", "Days lost.", "reject the part; accept the rest."),
              ("The project manager signs", "Nobody who will use it checked.", "arrange, never accept.")],
    use=["At every gate.", "Before a supplier is paid.", "Before handing anything to operations.", "Whenever the team says “done”."],
    skip=["Work in progress inside a team: that's for their definition of done."],
    related=["<b>Definition of ready and done</b> (Grace, vol. 3)", "<b>Is Our Way of Working Working?</b> (vol. 2)", "<b>May We Take the Next Step?</b> (vol. 2)", "<b>What's In, and What's Out?</b> (this volume)"],
    quiz=[("Quality control or validation: the scan check of every label?", "Quality control."),
          ("And Tomás walking the aisles with a handheld?", "Validation."),
          ("Who accepts the app?", "Grace, who owns its scope."),
          ("Why did Tomás reject two aisles, not the whole gate?", "Only they failed; the rest met the criteria. Rejecting the part kept the schedule."),
          ("On 22 April Joost offers to sign the acceptance for marketing to save Priya time. What does Sanne say?", "Priya asked for it and owns it; she accepts. Sanne will find twenty minutes in Priya's diary.")],
    try_it="Pick a deliverable your team calls done. Ask the person who asked for it to use it, the way they will really use it, against the criteria you agreed. Record what they say.",
    remember="The tailor checks the <span class=\"hl\">seams</span>. The client says if it <span class=\"hl\">fits</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Scope domain, validating scope.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 5.5 Validate Scope and 8.3 Control Quality.",
             "Gojko Adzic, <i>Specification by Example</i> (2011): acceptance criteria as examples."],
)

# ------------------------------------------------------------------ 15 Where Did That Come From?
sc_problem = Doodle(760, 250, "Doodle of 27 March 2026. The must-have count has risen only four a week for a fortnight. Sanne asks Ben, Dee and Eli where their time went. Small things, they say: a promo code for Priya, neighbourhood names in the zone picker, a dashboard for Yara. Nine of them since the baseline, none of them must-haves, none logged, about seven team-days.",
                    "Nine small yeses since the baseline. None logged. About seven team-days, mostly from the people on the blocked must-haves.")
for i, t in enumerate(["promo code", "late slot", "zone names", "labels EN", "tour video", "dashboard", "test data", "route cards", "email copy"]):
    r, c = divmod(i, 5)
    sc_problem.box(14 + c * 148, 20 + r * 62, 138, 48, t, "paper", size=14)
sc_problem.note(380, 176, "each one “only half a day”", "red", size=19)
sc_problem.note(380, 214, "together: about 7 team-days, 5 from Ben, Dee and Eli", "pen", size=17)

sc_analogy = Doodle(760, 240, "Doodle of a household budget. Nobody decides to overspend. A coffee here, a magazine there, a small subscription. Each one is too small to think about. At the end of the month the money is gone, and the big things go unpaid.",
                    "Nobody decides to overspend. A coffee, a magazine, a subscription. Then the rent is short.")
sc_analogy.row([("coffee", "€3", "paper"), ("magazine", "€6", "paper"), ("subscription", "€9", "paper"), ("rent", "short", "pink")], y=50, h=90, gap=34, size=18, subsize=16, arrows=True)
sc_analogy.note(380, 196, "each too small to decide; together, too big to ignore", "pen", size=18)

sc_how = Doodle(760, 400, "The extras list Sanne starts on 27 March 2026. All nine additions written down with who asked, who did it, the time it took and a decision. Five kept, because they were done or cost almost nothing: the promo code, English shelf labels, the training tour video, Rotterdam test data, courier route cards. Four stopped until after opening: the late Friday slot, neighbourhood names in the zone picker, the store dashboard, extra email copy. The rule from now on: any addition, however small, goes on the list, and Sanne decides it at the Thursday meeting.",
                "Every addition on one list, decided on Thursday. Five kept, four moved to after opening.")
items = [("promo code", "Ben 1½ d", "kept"), ("late Friday slot", "Ben 1 d", "after"), ("zone names", "Dee 1 d", "after"),
         ("English labels", "stockers ½ d", "kept"), ("tour video", "Tomás ½ d", "kept"), ("store dashboard", "Eli 1 d", "after"),
         ("test data", "Eli ½ d", "kept"), ("route cards", "ops lead ½ d", "kept"), ("email copy", "marketing ½ d", "after")]
for i, (t, who, res) in enumerate(items):
    r, c = divmod(i, 3)
    x, y = 14 + c * 248, 14 + r * 84
    sc_how.box(x, y, 160, 70, t, "paper", sub=who, size=15, subsize=12)
    sc_how.box(x + 166, y, 70, 70, "kept" if res == "kept" else "after", "green" if res == "kept" else "y", size=14)
sc_how.box(14, 280, 732, 80, "from now on: any addition goes on the list; decided on Thursdays", "blue", sub="inside Sanne's authority if no milestone, money or must-have moves; otherwise a change (C-…)", size=16, subsize=12)

CREEP = dict(
    slug="scope-creep",
    kicker="a.k.a. monitoring and controlling scope: scope creep and gold plating",
    tldr="<b>Scope creep</b> is scope growing through small additions that nobody decided. Each one is too small to bother anyone; together they eat the schedule. Its cousin, <b>gold plating</b>, is the team adding extras nobody asked for. The fix isn't to say no to everything: it's to make <b>every addition a decision</b>. Put each on a list, with who asked and what it costs, and decide it at a fixed time, at the right level. Watch the pace: creep usually shows up first as work slowing down for no visible reason.",
    chips=[("Family", "holding the line"), ("Lives in", "an extras list beside the must-have board, decided on Thursdays"), ("Pairs with", "change control, request triage, saying no")],
    pmbok=dict(covers="monitoring scope against the baseline; scope creep and gold plating; deciding additions; variance in scope",
               domains=["scope"], processes=["Monitor and Control Scope"], principles=["Focus on value", "Be an accountable leader"], focus=["monitoring"],
               older="6th: “Control Scope” (5.6). 7th: scope under the Delivery and Measurement domains."),
    problem_side="Larder, 27 March 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. For two weeks the must-have count has risen only <b>four a week</b>, and the blocked column doesn't explain it all. On 27 March she asks Ben, Dee and Eli where their time went. Small things, they say. A promo code for Priya. Neighbourhood names in the zone picker. A dashboard for Yara's office. <span class="hl-pink">Nine additions since the baseline, none of them must-haves, none written down: about seven team-days</span>, five of them from the three people the blocked must-haves were waiting for. Sanne had told everyone only the 71 counted. She had never said who could say yes to anything else.</p>
  <ul>
    <li>Each addition was too small to ask about.</li>
    <li>“Helps” rows looked free because nobody owned them.</li>
    <li>The cost showed up only as a slower pace.</li>
  </ul>""",
    problem_figs=[sc_problem],
    meanwhile=[("product-2", "request-triage", "since 2 March Grace has triaged every product request on Monday mornings: joined to an opportunity, a quick fix, parked or declined.",
                "on 27 March Sanne copies the idea for the launch: every addition goes on one list and is decided on Thursdays.")],
    analogy_side="the household budget",
    analogy="""  <p>Nobody decides to overspend. A <b>coffee</b> here, a <b>magazine</b> there, a small <b>subscription</b>. Each is too small to think about, so nobody does. At the end of the month the money is gone and the <b>rent is short</b>. Households that stay solvent don't ban coffee. They write everything down and look at the list once a week.</p>""",
    analogy_figs=[sc_analogy],
    map=[("A coffee, a magazine", "A promo code, neighbourhood names, a dashboard"),
         ("Too small to think about", "“Only half a day”"),
         ("The rent is short", "The blocked must-haves waited on the same people"),
         ("Writing everything down", "The extras list"),
         ("Looking at it once a week", "Decided at the Thursday meeting")],
    how_side="one list, a decision for every addition, at a fixed time",
    how="""  <p>Sanne says it plainly at the Thursday meeting: the rule was hers, and it had a hole. Then she starts an <b>extras list</b> beside the must-have board and writes down all nine: who asked, who did it, the time it took. Five are <b>kept</b>, because they're done or nearly free (the promo code, English shelf labels, a tour video for training, Rotterdam test data, courier route cards). Four are <b>stopped until after opening</b> (a late Friday slot, neighbourhood names, the dashboard, extra email copy). The new rule: <b>any addition goes on the list, however small</b>, and is decided on Thursday. Sanne decides those inside her authority (no milestone, money or must-have moves); anything bigger is a change for Joost or the steering group. The rule catches its first one the same week: an in-store launch event, which becomes change C-05 and is rejected. The pace rises again in April, helped by C-03.</p>""",
    how_figs=[sc_how],
    steps=[("Watch the pace", "Slowing for no visible reason is the first sign."),
           ("Ask where the time went", "Without blame."),
           ("Put every addition on one list", "Who asked, who did it, what it cost."),
           ("Decide them at a fixed time, at the right level", "Small ones yourself; big ones as changes."),
           ("Keep, stop, or move to later", "Out loud, to the person who asked."),
           ("Tell teams who may say yes", "And that “no, but on the list” is always allowed.")],
    vocab=[("Scope creep", "Uncontrolled growth of scope through small, undecided additions."),
           ("Gold plating", "The team adding extras nobody asked for."),
           ("Scope baseline", "The approved scope against which additions are measured."),
           ("Variance (scope)", "The difference between what is being delivered and what was agreed."),
           ("Extras list", "A visible list of every addition and its decision."),
           ("Opportunity cost", "What the time spent on an extra could have done instead.")],
    code=dict(file="rotterdam/30-extras-list.md", note="started 27 March 2026 · decided on Thursdays", plain=True, src="""
# ROTTERDAM · EXTRAS LIST (anything not one of the 71 must-haves)

#   ADDITION                         ASKED BY         DONE BY        TIME    DECISION (27 Mar)
E1  Rotterdam promo code in the app  Priya            Ben            1½ d    kept (done)
E2  extra Friday slot 21:00–22:00    Joost's ops lead Ben            1 d     after opening
E3  neighbourhood names, zone picker Priya            Dee            1 d     after opening
E4  English shelf labels beside Dutch a picker        stockers       ½ d     kept
E5  store tour video for training    Tomás            Tomás          ½ d     kept
E6  live dashboard, store office     Yara             Eli            1 d     after opening
E7  Rotterdam street test data       Eli              Eli            ½ d     kept (helps RTM-0)
E8  courier route cards              Joost's ops lead ops lead       ½ d     kept
E9  three waitlist email variants    Priya            marketing      ½ d     after opening
                                                       TOTAL ≈ 7 team-days (5 from Ben, Dee, Eli)
RULE from 27 Mar  every addition on this list, however small · decided Thursdays ·
                  Sanne decides if no milestone, money or must-have moves; else a change
FIRST CATCH       26 Mar in-store launch event → change C-05 → rejected (Joost)
"""),
    tools="tools: the must-have board, a second list beside it, and Thursday's meeting.",
    dial=[("Light", "one team", ["A product owner orders every request.", "Nothing starts without a yes.", "A short list."]),
          ("Standard", "Rotterdam", ["An extras list beside the must-haves.", "Decided weekly at the right level.", "Pace watched for creep."]),
          ("Heavy", "contracts", ["Every addition a formal change request.", "Scope verified against the contract.", "Claims for unapproved work rejected."])],
    baseline="Each line compares <b>small additions agreed in passing</b> to <b>every addition on one list, decided weekly at the right level</b>.",
    ratings=[(3, 5, "Time goes to the must-haves first."),
             (2, 4, "The pace stops leaking."),
             (2, 4, "Creep is found by watching the pace."),
             (2, 5, "Every addition is visible."),
             (3, 4, "Priya and Yara get a clear answer and a date."),
             (3, 4, "Teams are allowed to say “on the list”."),
             (3, 4, "Good extras are kept; others wait, not vanish."),
             (3, 3, "Neutral."),
             (3, 3, "A list and five minutes a week.")],
    pitfalls=[("“Only half a day”", "Nine of them is a week.", "every addition on the list."),
              ("Nobody owns the yes", "Teams say yes to whoever asks.", "say who decides, and when."),
              ("Banning extras", "People go round the rule.", "keep, stop or later, decided fast."),
              ("Gold plating", "The team adds polish nobody asked for.", "extras from the team go on the list too.")],
    use=["From the day there is a scope baseline.", "When the pace drops without a visible cause.", "When many people can ask the same team for things.", "Near a deadline."],
    skip=["Purely exploratory work where scope is meant to grow."],
    related=["<b>Can We Change That?</b> (vol. 2)", "<b>Feature request triage</b> (Grace, vol. 2)", "<b>Saying no without burning bridges</b> (Grace, vol. 2)", "<b>Are We Still on Time?</b> (this volume)"],
    quiz=[("Scope creep or gold plating: Eli adds Rotterdam test data nobody asked for?", "Gold plating (useful here, which is why it was kept)."),
          ("What was the first sign of creep?", "The pace dropped to four a week without enough blocked items to explain it."),
          ("Who decides a half-day addition that moves no milestone, money or must-have?", "Sanne, at the Thursday meeting."),
          ("Why did Sanne call it her mistake?", "She said only the 71 counted, but never said who could say yes to anything else."),
          ("On 2 April Priya asks Dee for “just a banner” in the app for Rotterdam. What does Dee say?", "“Yes, on the list”: it's decided on Thursday. If it moves nothing, Sanne can approve it there.")],
    try_it="Ask your team where their time went last week. List every piece of work that wasn't in the plan, with who asked. For each, decide: keep, stop, or later. Then tell them who decides additions from now on.",
    remember="Nobody decides to <span class=\"hl\">overspend</span>. Write every <span class=\"hl\">coffee</span> down.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Scope domain, monitoring and controlling scope.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 5.6 Control Scope.",
             "Capers Jones, <i>Assessment and Control of Software Project Risks</i> (1994): creeping requirements."],
)

NOTES = [TRACKING, VALIDATE, CREEP]
