# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 4 · Goals.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 OKRs
ok_problem = Doodle(760, 280, "Doodle of the Q3 2026 goals Priya receives from three teams: ship the three-minute window, ship live updates, launch slot reminders, migrate the payment screen. A list of outputs. None says what should change for customers, or how anyone will know if the quarter went well.",
                    "Q3 “goals”: four things to ship. None says what should change, or how we'll know.")
for i, t in enumerate(["ship 3-min window", "ship live updates", "launch slot reminders", "migrate payment screen"]):
    ok_problem.box(20 + (i % 2) * 370, 30 + (i // 2) * 76, 350, 60, t, "paper", size=16)
ok_problem.note(380, 220, "outputs, not outcomes", "red", size=20)
ok_problem.note(380, 256, "how will we know the quarter went well?", "pen")

ok_analogy = Doodle(760, 250, "Doodle of a mountain expedition: the objective is to reach the summit hut by Friday, safely. Key results: 1,200 metres climbed by Wednesday, everyone fit at the morning check, no more than one rest day used. The route can change; the objective and the checks stay.",
                     "An expedition: the objective in words, a few checks in numbers. The route can change; the checks stay.")
ok_analogy.icon("pyramid", 30, 60, 1.4)
ok_analogy.box(140, 40, 600, 50, "objective: the summit hut by Friday, safely", "green", size=15)
for i, t in enumerate(["1,200 m by Wed", "everyone fit daily", "≤ 1 rest day"]):
    ok_analogy.box(140 + i * 205, 110, 190, 50, t, "y", size=14)
ok_analogy.note(450, 210, "the route can change; the checks stay", "pen")

ok_how = Doodle(760, 380, "Grace's Q3 2026 OKRs, set 29 June, graded 30 September. Objective: every customer trusts their order. Key result 1: swap refund tickets from 3.4 to 2.5 percent of orders; graded 0.8 at 2.7 percent. Key result 2: where-is-my-order tickets down 30 percent; graded 1.0 at minus 31 percent. Key result 3: perfect orders from 84 to 86 percent; graded 0.75 at 85.5 percent. Initiatives underneath, not key results: the three-minute window test, live order updates, similarity-sorted suggestions.",
                 "One objective in words, three key results in numbers, graded honestly. The things to ship sit underneath, as bets.")
ok_how.box(14, 14, 732, 60, "O: every customer trusts their order", "green", size=17)
for i, (kr, start, end, got, grade, f) in enumerate([("swap refund tickets", "3.4 %", "2.5 %", "2.7 %", "0.8", "y"),
                                                    ("“where is it?” tickets", "", "−30 %", "−31 %", "1.0", "green"),
                                                    ("perfect orders", "84 %", "86 %", "85.5 %", "0.75", "y")]):
    y = 92 + i * 62
    ok_how.box(14, y, 732, 52, None, f, rx=6)
    ok_how.text(30, y + 33, f"KR{i + 1}  {kr}", "t-head", anchor="start", size=15)
    ok_how.text(470, y + 33, (f"{start} → " if start else "") + end, anchor="start", size=14)
    ok_how.text(730, y + 33, f"{got} · {grade}", "t-head", anchor="end", size=14)
ok_how.box(14, 290, 732, 50, "bets: 3-min window · live updates · similarity sort", "paper", dash=True, size=14)
ok_how.note(380, 366, "set 29 Jun · reviewed monthly · graded 30 Sep", "pen", size=15)

OKRS = dict(
    slug="okrs",
    kicker="a.k.a. “the summit hut by Friday”",
    tldr="<b>OKRs</b> pair an <b>objective</b> (where we want to be, in words people remember) with <b>two to four key results</b> (how we'll know, in numbers) for a quarter. Key results are <b>outcomes</b>, not things to ship; the features are <b>bets</b> underneath, free to change. Set them with the team, review them <b>monthly</b>, and <b>grade honestly</b> at the end: a 0.7 on an ambitious key result is a good quarter.",
    chips=[("Family", "goals"), ("Origin", "Andy Grove at Intel (1970s), John Doerr, <i>Measure What Matters</i> (2018)"), ("Lives in", "one page per team per quarter, next to the health page"), ("Pairs with", "outcome-based roadmaps, dashboards that get used, bets not promises")],
    problem_side="Larder, 29 June 2026",
    problem="""  <p class="lead">For Q3, Priya asks each team for goals. Grace's first draft looks like everyone else's: <b>ship the three-minute window</b>, <b>ship live updates</b>, <b>launch slot reminders</b>, <b>migrate the payment screen</b>. A list of outputs. <span class="hl-pink">None says what should change for customers</span>, so at the end of September the team could ship all four and still not know whether the quarter went well.</p>
  <ul>
    <li>Goals as features measure activity, not progress.</li>
    <li>If a feature turns out not to help, the goal still says “ship it”.</li>
    <li>Nobody can tell a good quarter from a busy one.</li>
  </ul>""",
    problem_figs=[ok_problem],
    analogy_side="the expedition",
    analogy="""  <p>A mountain expedition's <b>objective</b> is in words: <b>reach the summit hut by Friday, safely</b>. Its <b>checks</b> are numbers: 1,200 metres climbed by Wednesday, everyone fit at the morning check, no more than one rest day. If a path is blocked, the <b>route</b> changes; the objective and the checks don't.</p>""",
    analogy_figs=[ok_analogy],
    map=[("The summit hut by Friday, safely", "Objective: every customer trusts their order"),
         ("1,200 m by Wednesday", "KR: swap refund tickets 3.4 % → 2.5 %"),
         ("Everyone fit each morning", "KR: perfect orders 84 % → 86 %"),
         ("The route", "The bets: window test, live updates, similarity sort"),
         ("A blocked path", "Live updates round 1 tripping a guardrail")],
    how_side="an objective, a few numbers, bets underneath",
    how="""  <p>Grace rewrote it with the trio: <b>one objective</b>, “every customer trusts their order”, and <b>three key results</b>: swap refund tickets <b>3.4 % → 2.5 %</b>, “where is my order?” tickets <b>−30 %</b>, perfect orders <b>84 % → 86 %</b>. The features became <b>bets</b> underneath; slot reminders and the payment screen dropped off, serving neither. Graded on 30 September: <b>0.8, 1.0, 0.75</b>, a good quarter, and an honest one.</p>""",
    how_figs=[ok_how],
    steps=[("Start from the strategy", "Which bet or outcome matters most this quarter?"),
           ("Write one objective", "In words people remember; ambitious, qualitative."),
           ("Add two to four key results", "Outcomes with a start, a target and a date; no features."),
           ("Put bets underneath", "The features and tests you'll try; free to change."),
           ("Review monthly", "On the health page: on track, at risk, off track."),
           ("Grade honestly", "0 to 1 per key result; 0.7 on a stretch is good.")],
    vocab=[("OKR", "Objectives and key results."),
           ("Objective", "Where we want to be, in words."),
           ("Key result", "A measurable outcome that shows progress toward it."),
           ("Initiative / bet", "Work we think will move a key result."),
           ("Grading", "Scoring each key result 0 to 1 at the end."),
           ("Stretch goal", "Ambitious enough that 0.7 counts as success.")],
    code=dict(file="product/okrs/2026-q3.md", note="Grace's Q3 2026 OKRs, set 29 June, graded 30 September", plain=True, src="""
# Ordering & apps · Q3 2026 OKRs                          set 29 Jun · graded 30 Sep

OBJECTIVE   Every customer trusts their order.

KR1  Swap refund tickets 3.4 % → 2.5 % of orders            result 2.7 %   grade 0.8
KR2  "Where is my order?" tickets per 1,000 orders −30 %     result −31 %   grade 1.0
KR3  Perfect orders per week 84 % → 86 %                     result 85.5 %  grade 0.75

Bets (not key results)
  3-minute window test (→ shipped 13 Jul) · live order updates (→ shipped 21 Sep after
  a guardrail redesign) · similarity-sorted suggestions (→ shipped 3 Aug)
Dropped from the first draft: slot reminders, payment screen migration (no KR served)
Reviewed monthly on the health page.
"""),
    tools="tools: one page per team per quarter (a doc, the wiki, or an OKR tool such as Perdoo, Weekdone or Lattice); the health page for monthly check-ins.",
    gains=["<b>Outcomes over outputs</b>, every quarter.",
           "<b>Freedom to change bets</b> without changing goals.",
           "<b>Focus</b>: work that serves no KR drops off.",
           "<b>Honest grading</b> shows real progress.",
           "<b>Alignment</b> with leadership in a page."],
    losses=["<b>Can become bureaucracy</b> at scale.",
            "<b>Bad KRs</b> (features, vanity) undo the point.",
            "<b>Gaming</b> if grades affect pay.",
            "<b>Quarterly rhythm</b> may not fit every team."],
    baseline="Each line compares <b>quarterly goals written as features to ship</b> to <b>one objective, a few outcome key results, bets underneath, and honest grading</b>.",
    ratings=[(2, 4, "Every KR is something customers feel."),
             (2, 5, "Tied to refunds, tickets and the north star."),
             (2, 4, "Graded on measured results."),
             (3, 4, "Monthly reviews catch drift."),
             (2, 5, "Two features dropped: they served no KR."),
             (2, 5, "One page everyone can repeat."),
             (2, 4, "Priya sees outcomes, not activity."),
             (3, 3, "Neutral."),
             (3, 3, "An afternoon to set, an hour a month.")],
    pitfalls=[("Features as KRs", "“Ship live updates.”", "the outcome it should move."),
              ("Too many", "Five objectives, fifteen KRs.", "one objective, two to four KRs."),
              ("Set and forget", "Opened again on 30 September.", "review monthly."),
              ("Grades as pay", "Sandbagged targets.", "keep grading separate from performance reviews.")],
    use=["Quarterly planning for product teams.",
         "Aligning a team's work with a strategy.",
         "When goals keep turning into feature lists.",
         "Alongside outcome-based roadmaps."],
    skip=["Very small teams with one clear goal (just track it).",
          "Operational targets that don't change quarterly (use SLAs)."],
    related=["<b>Outcome-based roadmaps</b> (Vol. 2)", "<b>Dashboards that get used</b> (this volume)", "<b>Vanity vs actionable metrics</b> (this volume)", "<b>Bets, not promises</b> (Vol. 2)"],
    quiz=[("What's the difference between an objective and a key result?", "The objective says where, in words; key results say how we'll know, in numbers."),
          ("Where do features go?", "Underneath, as bets; not as key results."),
          ("What happened to slot reminders?", "Dropped: they served no key result."),
          ("Is 0.75 a bad grade?", "No: on an ambitious key result, around 0.7 is a good quarter.")],
    try_it="Take your team's goals for next quarter. Rewrite them as one objective and three key results with a start, target and date; move every feature underneath as a bet. Drop anything that serves no key result, and book a monthly fifteen-minute review.",
    remember="The <span class=\"hl\">summit hut</span> by Friday; a few numbers to check; the <span class=\"hl\">route</span> may change.",
    sources=["John Doerr, <i>Measure What Matters</i> (2018).",
             "Andy Grove, <i>High Output Management</i> (1983).",
             "Christina Wodtke, <i>Radical Focus</i>, 2nd ed. (2021).",
             "Marty Cagan, <i>Empowered</i> (2020), on team objectives."],
)

# ------------------------------------------------------------------ 13 Vanity vs Actionable Metrics
vm_problem = Doodle(760, 280, "Doodle of Femke's draft board slide in June 2026: 120,000 swaps approved since April! 180,000 app downloads! Both numbers only go up. Neither would make anyone do anything differently, and neither shows whether customers trust their orders more.",
                    "“120,000 swaps approved! 180,000 downloads!” Numbers that only go up, and change nothing.")
vm_problem.box(20, 40, 340, 100, "120,000", "y", sub="swaps approved since April")
vm_problem.box(400, 40, 340, 100, "180,000", "y", sub="app downloads")
vm_problem.note(380, 200, "big, rising, and useless for decisions", "red", size=19)

vm_analogy = Doodle(760, 250, "Doodle of a gym's two numbers: total sign-ups ever, which only rises, and the share of new members still training after three months, which can fall. Only the second tells the manager whether the new induction is working.",
                     "A gym's total sign-ups only rise. The share still training after three months tells the manager something.")
vm_analogy.icon("stopwatch", 40, 60, 1.3)
vm_analogy.box(160, 50, 270, 100, "total sign-ups", "pink", sub="only goes up")
vm_analogy.box(460, 50, 280, 100, "still training at 3 mo", "green", sub="can go down: useful")
vm_analogy.note(450, 210, "would we act differently if it changed?", "pen")

vm_how = Doodle(760, 360, "Grace's test for every metric on a slide, June 2026: if this number changed, would we do something different? Swaps approved since April: always rises, no. App downloads: no. Replaced by: swap refund tickets per 100 orders, 6.2 then, 3.4 now; share of swaps answered by the customer, 82 percent; customers still ordering eight weeks after a swap, 71 percent. Femke's board slide used the three actionable numbers.",
                 "The test: would a change in this number change what we do? Three actionable numbers replaced two vanity ones.")
vm_how.box(14, 14, 360, 160, None, "pink")
vm_how.head(194, 46, "vanity", size=17)
for i, t in enumerate(["swaps approved (total)", "app downloads", "only go up"]):
    vm_how.text(194, 86 + i * 30, t, "t t-red" if i == 2 else "t", size=15)
vm_how.box(386, 14, 360, 160, None, "green")
vm_how.head(566, 46, "actionable", size=17)
for i, t in enumerate(["swap refunds: 6.2 → 3.4 per 100", "answered by customer: 82 %", "ordering 8 wks after swap: 71 %"]):
    vm_how.text(566, 86 + i * 30, t, size=14)
vm_how.box(14, 200, 732, 70, "would we act differently if it changed?", "y", size=17)
vm_how.note(380, 310, "rates, per customer or order, with a direction that can go both ways", "pen", size=15)

VANITY = dict(
    slug="vanity-metrics",
    kicker="a.k.a. “total sign-ups ever”",
    tldr="<b>Vanity metrics</b> look impressive and change nothing: totals that only go up (downloads, sign-ups, “swaps approved since April”). <b>Actionable metrics</b> can go <b>both ways</b> and would <b>change a decision</b> if they moved: rates per customer or per order, shares, retention. Test every number on a slide with one question: <b>if this changed, would we do something different?</b> If not, replace it.",
    chips=[("Family", "goals"), ("Origin", "Eric Ries, <i>The Lean Startup</i> (2011); Alistair Croll and Benjamin Yoskovitz, <i>Lean Analytics</i> (2013)"), ("Lives in", "every slide, report and health page"), ("Pairs with", "OKRs, dashboards that get used, north star metric")],
    problem_side="Larder, 22 June 2026",
    problem="""  <p class="lead">Femke's draft board slide for June leads with two big numbers: <b>120,000 swaps approved since April!</b> and <b>180,000 app downloads!</b> Both are true and both are growing. <span class="hl-pink">Neither would make anyone do anything differently</span>, and neither says whether customers trust their orders more, which is what the business case was about.</p>
  <ul>
    <li>Cumulative totals only rise, so they always look good.</li>
    <li>Big numbers impress without informing.</li>
    <li>The numbers that would show a problem aren't on the slide.</li>
  </ul>""",
    problem_figs=[vm_problem],
    analogy_side="the gym's two numbers",
    analogy="""  <p>A gym can report <b>total sign-ups ever</b>, which only rises, or the <b>share of new members still training after three months</b>, which can fall. Only the second tells the manager whether the new induction is working, and what to change if it isn't. The first looks great on a poster.</p>""",
    analogy_figs=[vm_analogy],
    map=[("Total sign-ups ever", "Swaps approved since April; app downloads"),
         ("Still training after three months", "Customers still ordering eight weeks after a swap"),
         ("Can fall", "A rate or share, not a running total"),
         ("Changes what the manager does", "Changes what Grace's team does"),
         ("The poster", "The board slide")],
    how_side="one question per number",
    how="""  <p>Grace asked the same question of each number: <i>if this changed, would we do something different?</i> The totals failed. She offered three that pass: <b>swap refund tickets per 100 orders</b> (6.2 → 3.4), the <b>share of swaps answered by the customer</b> (82 %), and <b>customers still ordering eight weeks after a swap</b> (71 %). Femke used them; the board's questions were sharper (“what would take refunds to 2?”).</p>""",
    how_figs=[vm_how],
    steps=[("List every number on the slide", "Or the report, or the dashboard."),
           ("Ask the question", "If this changed, would we do something different?"),
           ("Prefer rates and shares", "Per order, per customer, per week: comparable over time."),
           ("Check it can go both ways", "Totals that only rise are almost always vanity."),
           ("Pair with a target", "So the reader knows good from bad."),
           ("Keep vanity numbers out of decisions", "Fine for a celebration; not for steering.")],
    vocab=[("Vanity metric", "A number that looks good but doesn't guide action."),
           ("Actionable metric", "A number whose change would change a decision."),
           ("Cumulative total", "A running sum: only goes up."),
           ("Rate", "A number per order, customer or time unit."),
           ("Ratio", "One number divided by another, comparable over time."),
           ("Leading indicator", "An early, actionable signal (see Vol. 1).")],
    code=dict(file="product/board/2026-06-slide.md", note="the slide before and after, 22 June 2026", plain=True, src="""
# Board slide · substitutions

BEFORE (draft)
  120,000 swaps approved since April!          → only rises; changes nothing
  180,000 app downloads!                        → only rises; not about trust

AFTER
  Swap refund tickets per 100 orders    6.2 (Oct) → 3.4 (Jun)     target 2.0 (Dec)
  Swaps answered by the customer        82 %                       test: 3-min window
  Ordering 8 weeks after a swap         71 % (refund ticket: 58 %) → why swaps matter

Test for every number: "If this changed, would we do something different?"
"""),
    tools="tools: any reporting tool; the habit of asking the question in reviews; rates and ratios instead of totals.",
    gains=["<b>Numbers that steer</b>, not decorate.",
           "<b>Problems stay visible</b>.",
           "<b>Sharper questions</b> from leaders.",
           "<b>Comparable over time</b> as rates.",
           "<b>Honest reporting</b> builds trust."],
    losses=["<b>Less impressive</b> slides.",
            "<b>Rates can be harder</b> to compute.",
            "<b>Some vanity numbers motivate</b> teams (keep them separate).",
            "<b>Needs targets</b> to read well."],
    baseline="Each line compares <b>reporting big cumulative totals</b> to <b>rates and shares that can go both ways and would change a decision</b>.",
    ratings=[(3, 4, "Numbers track what customers experience."),
             (2, 4, "Tied to refunds and repeat orders."),
             (2, 5, "Every number passes the question."),
             (3, 3, "Neutral."),
             (2, 4, "Three numbers instead of a pile."),
             (2, 4, "Everyone reads the same honest numbers."),
             (2, 5, "The board asked sharper questions."),
             (3, 3, "Neutral."),
             (3, 4, "One question per number.")],
    pitfalls=[("Running totals", "“1 million orders!”", "rates per order or customer."),
              ("No target", "82 %: good or bad?", "show the target or the comparison."),
              ("Dropping the bad numbers", "Only rising metrics on the slide.", "include the ones that could show trouble."),
              ("Banning celebration", "No totals ever.", "fine for celebrating; not for steering.")],
    use=["Board slides, reports, health pages.",
         "Choosing key results.",
         "Reviewing any dashboard.",
         "When numbers look great but nothing feels better."],
    skip=["Team celebrations (just don't steer by them)."],
    related=["<b>OKRs</b> (this volume)", "<b>Dashboards that get used</b> (this volume)", "<b>North star metric</b> (Vol. 1)", "<b>Leading vs lagging indicators</b> (Vol. 1)"],
    quiz=[("What's the test for a vanity metric?", "If it changed, would we do something different? If not, it's vanity."),
          ("Why are cumulative totals usually vanity?", "They only go up, so they always look good and never signal a problem."),
          ("What replaced “swaps approved since April”?", "Swap refund tickets per 100 orders, swaps answered, and repeat orders after a swap."),
          ("Are vanity metrics ever fine?", "For celebrating, yes; not for steering.")],
    try_it="Take your last report or slide. Ask the question of every number, and replace each one that fails with a rate or share that could go down, with a target next to it.",
    remember="Not <span class=\"hl\">total sign-ups</span>: who's still training after <span class=\"hl\">three months</span>?",
    sources=["Eric Ries, <i>The Lean Startup</i> (2011), vanity metrics.",
             "Alistair Croll and Benjamin Yoskovitz, <i>Lean Analytics</i> (2013).",
             "Josh Seiden, <i>Outcomes Over Output</i> (2019).",
             "Avinash Kaushik, <i>Web Analytics 2.0</i> (2009)."],
)

# ------------------------------------------------------------------ 14 Post-Launch Review
pl_problem = Doodle(760, 280, "Doodle of the weeks after approvals launched. The team celebrated, then moved straight to the next thing. Nobody compared what happened with what the business case and the bets had expected, so nobody could say whether the estimates had been good, or what to do differently next time.",
                    "Launched, celebrated, moved on. Nobody compared what happened with what we expected.")
pl_problem.box(20, 40, 220, 80, "launch", "green", sub="13 April")
pl_problem.arrow(244, 80, 300, 80)
pl_problem.box(304, 40, 220, 80, "next thing", "paper", sub="already")
pl_problem.box(560, 30, 180, 100, "expected?", "pink", sub="nobody checked", stroke="red")
pl_problem.note(380, 200, "no learning, just the next launch", "red", size=19)

pl_analogy = Doodle(760, 250, "Doodle of a sailing crew's debrief after a race: what we planned, what happened, why, and what we'll change next race. Fifteen minutes on the dock, no blame, written in the logbook.",
                     "A crew debrief on the dock: planned, happened, why, next time. Fifteen minutes, no blame, in the logbook.")
pl_analogy.icon("ship", 30, 70, 1.1)
for i, (t, f) in enumerate([("planned", "paper"), ("happened", "y"), ("why", "blue"), ("next time", "green")]):
    pl_analogy.box(150 + i * 150, 70, 138, 60, t, f, size=16)
pl_analogy.note(450, 200, "on the dock, no blame, in the log", "pen")

pl_how = Doodle(760, 360, "Grace's approvals post-launch review, 6 July 2026, twelve weeks after Amsterdam. Expected versus actual. Swap refund tickets: expected about 3.5 percent by end of June, actual 3.4. Answered within the window: expected 70 percent or more, actual 82 after the Android fix. Build effort: 8 person-weeks planned, 11 actual. Benefit: about 28,000 euros a month, as the business case said. Surprises: 37 percent with notifications off, the Android grouping bug. Next: the three-minute test, live updates, and estimating integrations with a buffer.",
                 "Expected vs actual, surprises, and what changes next time. Blameless, written down, in an hour.")
pl_how.head(20, 32, "measure", anchor="start", size=15)
pl_how.head(330, 32, "expected", anchor="start", size=15)
pl_how.head(520, 32, "actual", anchor="start", size=15)
for i, (m, e, a, f) in enumerate([("swap refund tickets", "≈ 3.5 %", "3.4 % ✓", "green"), ("answered in window", "≥ 70 %", "82 % ✓", "green"),
                                  ("build effort", "8 person-weeks", "11 ✗", "pink"), ("benefit", "≈ €28k / month", "≈ €28k ✓", "green")]):
    y = 46 + i * 46
    pl_how.box(12, y, 736, 38, None, f, rx=4)
    pl_how.text(20, y + 25, m, "t-head", anchor="start", size=14)
    pl_how.text(330, y + 25, e, anchor="start", size=14)
    pl_how.text(520, y + 25, a, anchor="start", size=14)
pl_how.box(12, 240, 736, 50, "surprises: 37 % notifications off · Android grouping", "y", size=14)
pl_how.note(380, 322, "next time: a buffer for platform integrations", "pen", size=16)

POST_LAUNCH = dict(
    slug="post-launch-review",
    kicker="a.k.a. “the debrief on the dock”",
    tldr="Most teams launch, celebrate and move on, so they never learn whether their estimates were any good. A <b>post-launch review</b>, a few weeks after launch, compares <b>what you expected</b> (the business case, the bets) with <b>what happened</b>: outcomes, effort, costs, side effects. Note the <b>surprises</b> and <b>why</b>, decide <b>what's next</b> for the feature, and what you'll do <b>differently</b> next time. Blameless, written, an hour.",
    chips=[("Family", "goals"), ("Origin", "after-action reviews (US Army); post-implementation reviews; blameless postmortems"), ("Lives in", "a page linked from the business case and the roadmap item"), ("Pairs with", "business case one-pager, bets not promises, killing a feature")],
    problem_side="Larder, 6 July 2026",
    problem="""  <p class="lead">Approvals launched in Amsterdam on 13 April. The team celebrated, then moved straight to Rotterdam and live updates. Twelve weeks later, nobody has compared what happened with what the <b>business case</b> and the <b>bets</b> expected. <span class="hl-pink">Were the estimates good? What surprised us?</span> Nobody knows, so the next business case will be written with the same blind spots.</p>
  <ul>
    <li>Launches are treated as the finish line.</li>
    <li>Estimates are never checked, so they never improve.</li>
    <li>Lessons stay in people's heads, and leave with them.</li>
  </ul>""",
    problem_figs=[pl_problem],
    analogy_side="the debrief on the dock",
    analogy="""  <p>After a race, a good sailing crew spends <b>fifteen minutes on the dock</b>: what we <b>planned</b>, what <b>happened</b>, <b>why</b>, and what we'll <b>change next race</b>. No blame; it goes in the <b>logbook</b>. Crews that skip it make the same mistake at the same mark every season.</p>""",
    analogy_figs=[pl_analogy],
    map=[("What we planned", "The business case and the bets"),
         ("What happened", "Measured outcomes, effort and cost"),
         ("Why", "Surprises: notifications off, the Android bug"),
         ("Next race", "What changes in the next business case"),
         ("The logbook", "A page linked from the business case")],
    how_side="expected vs actual, then next time",
    how="""  <p>Grace ran the review with the trio and Sam on <b>6 July</b>, in an hour. Outcomes matched the bets: swap refund tickets <b>3.4 %</b> (expected about 3.5 %), answers <b>82 %</b>, benefit about <b>€28k a month</b>. Effort didn't: <b>11 person-weeks</b>, not 8, mostly the platform integrations. The surprises (notifications off, Android grouping) were written down; next time's business cases get a <b>buffer for platform work</b>.</p>""",
    how_figs=[pl_how],
    steps=[("Schedule it at launch", "Six to twelve weeks after, when outcomes can be read."),
           ("Bring the expectations", "The business case, the bets, the test cards."),
           ("Compare, line by line", "Outcomes, effort, costs, guardrails: expected vs actual."),
           ("Name the surprises and why", "Without blame; facts and causes."),
           ("Decide what's next for the feature", "Invest more, keep as is, or stop."),
           ("Change how you estimate", "One or two concrete changes for the next case.")],
    vocab=[("Post-launch review", "Comparing expected and actual results after a launch."),
           ("After-action review", "Planned, happened, why, next time."),
           ("Blameless", "Looking at causes and systems, not culprits."),
           ("Estimate accuracy", "How close expectations were to reality."),
           ("Surprise", "Something nobody expected, worth learning from."),
           ("Benefit realisation", "Checking a business case's benefits actually arrived.")],
    code=dict(file="product/reviews/2026-07-approvals.md", note="the approvals post-launch review, 6 July 2026", plain=True, src="""
# Post-launch review · approvals (Amsterdam 13 Apr, Rotterdam 8 Jun)    6 Jul 2026
With: Grace, Noor, Ben, Sam · blameless · 60 minutes

| Measure                     | Expected (case, bets)  | Actual            |
|-----------------------------|------------------------|-------------------|
| Swap refund tickets         | ≈ 3.5 % by end June    | 3.4 % ✓           |
| Answered within window      | ≥ 70 %                 | 82 % (after fix) ✓|
| Picking time per swap order | ≤ +15 s                | +7 s ✓            |
| Build effort                | 8 person-weeks         | 11 ✗ (platforms)  |
| Benefit                     | ≈ €28k / month         | ≈ €28k ✓          |

Surprises   37 % of app users have notifications off · Android grouped our notifications
Next        3-minute window test (22 Jun–6 Jul) · live updates (Q3) · Rotterdam catch-up
Next time   +30 % buffer for work touching iOS, Android and web together
"""),
    tools="tools: a review template linked from the business case; the health page and test cards as sources; a calendar reminder set on launch day.",
    gains=["<b>Estimates improve</b> over time.",
           "<b>Benefits checked</b>, not assumed.",
           "<b>Surprises recorded</b>, not repeated.",
           "<b>Clear next step</b> for the feature.",
           "<b>Trust with finance</b>: cases get checked."],
    losses=["<b>An hour</b> for several people.",
            "<b>Uncomfortable</b> when estimates were off.",
            "<b>Easy to skip</b> when busy.",
            "<b>Blame creeps in</b> without care."],
    baseline="Each line compares <b>launching and moving on</b> to <b>a blameless review comparing expected and actual, with next steps and estimating changes</b>.",
    ratings=[(3, 4, "The next steps follow what customers did."),
             (2, 5, "Benefits checked against the business case."),
             (2, 5, "Expected vs actual, line by line."),
             (2, 4, "Lessons captured twelve weeks in."),
             (3, 4, "A clear next step for the feature."),
             (2, 4, "The team shares one story of what happened."),
             (2, 5, "Marco sees cases checked."),
             (3, 3, "Neutral."),
             (3, 3, "An hour per launch.")],
    pitfalls=[("Never scheduled", "Always next month.", "book it on launch day."),
              ("Only outcomes", "Effort and cost never compared.", "compare everything the case promised."),
              ("Blame", "“Who estimated 8 weeks?”", "causes, not culprits."),
              ("No change", "Lessons noted, nothing different.", "one or two concrete changes for next time.")],
    use=["Every launch with a business case or bets.",
         "Big migrations and city launches.",
         "Before writing the next business case.",
         "When a feature's value is being questioned."],
    skip=["Tiny changes; a note in the release log is enough."],
    related=["<b>Business case one-pager</b> (Vol. 2)", "<b>Bets, not promises</b> (Vol. 2)", "<b>Killing a feature</b> (this volume)", "<b>Revisiting decisions</b> (Ana, book 1 vol. 2)"],
    quiz=[("When should a post-launch review happen?", "Six to twelve weeks after launch, when outcomes can be read; booked on launch day."),
          ("What's compared?", "Expected vs actual: outcomes, effort, costs, guardrails."),
          ("What did Larder's review find?", "Outcomes matched the bets; effort was 11 person-weeks, not 8."),
          ("What changed for next time?", "A buffer for work touching several platforms.")],
    try_it="Pick a feature you launched two or three months ago. Find its business case or the expectations you set, and fill a two-column table: expected, actual. Write one surprise and one change you'll make in the next estimate.",
    remember="Fifteen minutes on the <span class=\"hl\">dock</span>: planned, happened, why, <span class=\"hl\">next time</span>.",
    sources=["U.S. Army, “A Leader's Guide to After-Action Reviews” (1993).",
             "Norman Kerth, <i>Project Retrospectives</i> (2001).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), blameless postmortems.",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018)."],
)

# ------------------------------------------------------------------ 15 Killing a Feature
kf_problem = Doodle(760, 280, "Doodle of the slot waitlist, built for Rotterdam in June 2026. By September, 1.1 percent of slot customers have joined a waitlist, and 9 percent of those ever ordered from it. It has caused two bugs and a steady trickle of confused tickets. Nobody wants to be the one to remove it.",
                    "The slot waitlist: 1.1 % use it, 9 % of those order, two bugs, confused tickets, and nobody wants to remove it.")
kf_problem.box(20, 40, 300, 100, "slot waitlist", "paper", sub="built June 2026")
for i, t in enumerate(["1.1 % of slot customers join", "9 % of those ever order", "2 bugs · confused tickets"]):
    kf_problem.text(540, 70 + i * 32, t, "t t-red" if i == 2 else "t", size=16)
kf_problem.note(380, 220, "easy to add, nobody's job to remove", "red", size=19)

kf_analogy = Doodle(760, 250, "Doodle of a restaurant taking a dish off the menu: few people order it, it slows the kitchen, and it takes space in the fridge. The chef tells regulars who liked it, suggests an alternative, and frees the kitchen for the dishes people love.",
                     "Taking a dish off the menu: tell the few who liked it, suggest another, free the kitchen.")
kf_analogy.icon("menu", 40, 50, 1.4)
kf_analogy.box(160, 50, 270, 100, "the dish", "pink", sub="few orders, slows the kitchen")
kf_analogy.box(460, 50, 280, 100, "taken off", "green", sub="regulars told, alternative offered")
kf_analogy.note(450, 210, "less on the menu, better food", "pen")

kf_how = Doodle(760, 360, "How Grace removed the slot waitlist, September to October 2026. The case: usage 1.1 percent, conversion 9 percent, two bugs, about two engineer-days a month of upkeep, confused tickets. Talk to the users: the twelve customers who used it most were offered slot alerts by email instead. Announce in the app two weeks before. Switch it off on 5 October; delete the code and the data the same week. Tell the team what it freed up.",
                 "Make the case with data, talk to the users, announce, switch off, delete the code, say what it freed.")
for i, (t, s, f) in enumerate([("the case", "1.1 % use · 2 bugs · 2 days/mo", "y"), ("talk to users", "top 12: an alternative", "blue"), ("announce", "in-app, 2 weeks", "paper"),
                               ("switch off", "5 Oct", "pink"), ("delete", "code + data, same week", "green"), ("tell the team", "2 days a month freed", "green")]):
    r, c = divmod(i, 3)
    kf_how.box(14 + c * 248, 20 + r * 120, 236, 100, t, f, sub=s, subsize=13)
kf_how.note(380, 296, "agreed with Priya and Sam; Rotterdam's store manager told first", "pen", size=15)
kf_how.note(380, 326, "tickets about the waitlist after 5 Oct: 0", "green", size=16)

KILL = dict(
    slug="killing-a-feature",
    kicker="a.k.a. “taking a dish off the menu”",
    tldr="Features are easy to add and nobody's job to remove, so products fill up with things few people use and everyone maintains. <b>Killing a feature</b> on purpose: make the <b>case with data</b> (usage, outcomes, upkeep, confusion), <b>talk to the people who use it</b> and offer an alternative, <b>announce</b> it in advance, <b>switch it off</b>, then <b>delete the code and data</b>, and tell the team what it freed up.",
    chips=[("Family", "goals"), ("Origin", "product practice (Intercom's “feature audits”, Basecamp, Google's product sunsets)"), ("Lives in", "the roadmap's “stopping” column and the post-launch review"), ("Pairs with", "post-launch review, saying no, technical debt register")],
    problem_side="Larder, 21 September 2026",
    problem="""  <p class="lead">The <b>slot waitlist</b> was a Should for Rotterdam's launch and shipped in June. By September, <b>1.1 %</b> of slot customers have joined a waitlist, and <b>9 %</b> of those ever ordered from one. It has caused <b>two bugs</b>, costs about <b>two engineer-days a month</b>, and produces a trickle of confused tickets. <span class="hl-pink">Nobody wants to be the one to remove it</span>: someone asked for it, and someone built it.</p>
  <ul>
    <li>Features accumulate; removal has no owner.</li>
    <li>Every feature costs upkeep, support and attention.</li>
    <li>Removing feels like admitting a mistake.</li>
  </ul>""",
    problem_figs=[kf_problem],
    meanwhile=[("architect-2", "revisiting-decisions", "the same week, Grace stops the slot waitlist using the same kind of evidence.", "The same week Ana reviews decision triggers, Grace removes the slot waitlist: its usage triggered the stop.")],
    analogy_side="taking a dish off the menu",
    analogy="""  <p>A restaurant takes a <b>dish off the menu</b> when few people order it, it slows the kitchen and takes fridge space. A good chef tells the <b>regulars who liked it</b>, suggests an <b>alternative</b>, and frees the kitchen for the dishes people love. A menu that only grows gets worse, not better.</p>""",
    analogy_figs=[kf_analogy],
    map=[("The rarely-ordered dish", "The slot waitlist: 1.1 % use"),
         ("Slowing the kitchen", "Two bugs, two engineer-days a month"),
         ("Telling the regulars", "Talking to the twelve heaviest users"),
         ("Suggesting another dish", "Slot alerts by email instead"),
         ("A freed kitchen", "Two days a month back for the roadmap")],
    how_side="case, users, announce, off, delete",
    how="""  <p>Grace put the <b>case</b> to Priya and Sam with numbers, then called the <b>twelve customers</b> who used the waitlist most and offered <b>slot alerts by email</b>; most were happy. An in-app notice ran <b>two weeks</b>; Rotterdam's store manager heard first. The waitlist was switched off on <b>5 October</b>, and the <b>code and data were deleted</b> the same week. Tickets about it since: <b>zero</b>; two engineer-days a month went back to the roadmap.</p>""",
    how_figs=[kf_how],
    steps=[("Review usage regularly", "Every feature's usage, outcomes and upkeep, once or twice a year."),
           ("Make the case with data", "Usage, effect on outcomes, bugs, upkeep, support load."),
           ("Talk to the users", "The heaviest users first; offer an alternative."),
           ("Announce in advance", "In the product, two weeks or more; staff told first."),
           ("Switch off, then delete", "Remove the code and data, not just the button."),
           ("Say what it freed", "Time, attention and simplicity, out loud.")],
    vocab=[("Feature sunset", "Planned removal of a feature."),
           ("Feature audit", "Reviewing features by usage and value."),
           ("Upkeep", "The ongoing cost of keeping a feature working."),
           ("Long tail", "Many features used by few customers."),
           ("Deprecation notice", "Telling users a feature will go."),
           ("Sunk cost", "The effort already spent; not a reason to keep it.")],
    code=dict(file="product/sunsets/slot-waitlist.md", note="the case and plan, 21 September 2026", plain=True, src="""
# Sunset: slot waitlist (Rotterdam, June 2026)       owner: Grace · agreed: Priya, Sam

Case      used by 1.1 % of slot customers · 9 % of those ever ordered from it
          2 bugs (Jul, Aug) · ≈ 2 engineer-days/month upkeep · ≈ 6 confused tickets/week
          no key result served; slot reminders were cooled by the panel too
Users     top 12 users called (21–23 Sep): offered slot alerts by email; 10 happy, 2 neutral
Notice    in-app on the slot page from 21 Sep; Rotterdam store manager told 20 Sep
Off       5 Oct 2026 · code and stored waitlists deleted by 9 Oct
Freed     ≈ 2 engineer-days a month → live updates polish
After     waitlist tickets since 5 Oct: 0
"""),
    tools="tools: usage data per feature (analytics events), the support ticket review, feature flags to switch off before deleting, the roadmap's “stopping” list.",
    gains=["<b>A simpler product</b> for everyone.",
           "<b>Time freed</b> for what matters.",
           "<b>Fewer bugs and tickets</b>.",
           "<b>Honest about bets</b> that didn't work.",
           "<b>Users treated well</b> on the way out."],
    losses=["<b>A few users lose something</b>.",
            "<b>Uncomfortable</b> for whoever asked for it.",
            "<b>Effort to remove</b> code and data.",
            "<b>Occasional backlash</b>."],
    baseline="Each line compares <b>keeping every feature forever because removal is nobody's job</b> to <b>removing low-value features on purpose: case, users, notice, switch off, delete</b>.",
    ratings=[(3, 4, "Heavy users got an alternative; everyone gets a simpler app."),
             (2, 4, "Two engineer-days a month back."),
             (2, 4, "Usage and upkeep decided it."),
             (3, 3, "Neutral."),
             (1, 5, "One less thing to maintain and explain."),
             (2, 4, "Everyone knows why it went."),
             (2, 4, "Priya and Sam agreed the case."),
             (2, 4, "Fewer bugs interrupting work."),
             (2, 4, "Less code, less upkeep.")],
    pitfalls=[("Switching off but not deleting", "Dead code and data linger.", "delete code and data the same week."),
              ("Surprising users", "It vanishes one morning.", "announce in advance; talk to heavy users."),
              ("Sunk-cost loyalty", "“We spent six weeks on it.”", "decide on value from here."),
              ("Never reviewing", "Features only accumulate.", "a usage review once or twice a year.")],
    use=["Features with low usage and real upkeep.",
         "After a post-launch review shows a bet didn't pay.",
         "Before a big redesign: fewer things to carry.",
         "When support keeps explaining a confusing feature."],
    skip=["Features with low usage but high importance (legal, safety, accessibility).",
          "Too early: give a new feature time and a fair test."],
    related=["<b>Post-launch review</b> (this volume)", "<b>Saying no without burning bridges</b> (Vol. 2)", "<b>Revisiting decisions</b> (Ana, book 1 vol. 2)", "<b>Technical debt register</b> (Ana, book 1 vol. 2)"],
    quiz=[("Why do features rarely get removed?", "Removal is nobody's job, and it feels like admitting a mistake."),
          ("What goes into the case?", "Usage, effect on outcomes, bugs, upkeep and support load."),
          ("How should users be treated?", "Talked to first, offered an alternative, warned in advance."),
          ("What's the last step?", "Delete the code and data, and say what it freed.")],
    try_it="List the five least-used features in your product with their upkeep and ticket load. Pick one, write the case in five lines, call three of its heaviest users, and propose a sunset date to your manager.",
    remember="Take the <span class=\"hl\">dish</span> off the menu: tell the regulars, then free the <span class=\"hl\">kitchen</span>.",
    sources=["Des Traynor, “Product strategy means saying no” and feature audits (Intercom blog, 2013–).",
             "Jason Fried and David Heinemeier Hansson, <i>Rework</i> (2010).",
             "Hunter Walk, on sunsetting features (2014).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018)."],
)

NOTES = [OKRS, VANITY, POST_LAUNCH, KILL]
