# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 4 · Experimenting.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 A/B Tests
ab_problem = Doodle(760, 280, "Doodle of a June 2026 argument: should customers get two or three minutes to answer a swap? Sam says three, customers complain the timer is stressful. Tomás says two, pickers can't wait longer. Both have anecdotes; neither has numbers. Changing it for everyone and comparing June with July would mix in the weather, the holidays and Rotterdam.",
                    "Two minutes or three? Two sets of anecdotes, and a before/after comparison would mix in the holidays.")
ab_problem.box(20, 40, 320, 90, "Sam: 3 minutes", "blue", sub="“the timer stresses people”")
ab_problem.box(420, 40, 320, 90, "Tomás: 2 minutes", "y", sub="“pickers can't wait longer”")
ab_problem.box(160, 170, 440, 60, "June vs July? holidays, weather, Rotterdam", "pink", size=15, stroke="red")
ab_problem.note(380, 262, "anecdotes, and a comparison that can't separate causes", "red")

ab_analogy = Doodle(760, 250, "Doodle of a fair taste test of two recipes: tasters are assigned at random to recipe A or B, they don't know which they got, and everything else (plate, temperature, time of day) is the same. The only difference is the recipe.",
                     "A fair taste test: tasters assigned at random, everything else the same, only the recipe differs.")
ab_analogy.icon("dice", 40, 60, 1.2)
ab_analogy.box(160, 50, 260, 100, "recipe A", "y", sub="random half of tasters")
ab_analogy.box(450, 50, 290, 100, "recipe B", "green", sub="the other half, same plate")
ab_analogy.note(450, 210, "only one thing differs", "pen")

ab_how = Doodle(760, 360, "The window test, 22 June to 6 July 2026. Amsterdam express customers split at random, half get two minutes and half three. Primary metric, chosen in advance: share of swaps answered by the customer rather than defaulted. Result: 82 percent with two minutes, 88 percent with three, a difference of 6 points, 95 percent interval 3.8 to 8.2. Guardrail, picking time per swap order: plus 7 seconds versus plus 11, within the 15-second limit. Decision: three minutes from 13 July.",
                 "Random split, one change, a primary metric and guardrails chosen first. Three minutes won, within the picking guardrail.")
ab_how.box(14, 20, 240, 100, "customers", "paper", sub="Amsterdam express", subsize=14)
ab_how.arrow(258, 50, 330, 40)
ab_how.arrow(258, 90, 330, 110)
ab_how.box(334, 14, 200, 70, "A · 2 min", "y", sub="answered 82 %", subsize=14)
ab_how.box(334, 94, 200, 70, "B · 3 min", "green", sub="answered 88 %", subsize=14)
ab_how.box(560, 14, 186, 150, None, "paper")
ab_how.head(653, 44, "difference", size=15)
ab_how.text(653, 78, "+6 points", "t-head", size=18)
ab_how.text(653, 108, "95 %: +3.8 to +8.2", size=13)
ab_how.text(653, 138, "picking: +7 s vs +11 s", size=13)
ab_how.box(14, 190, 732, 70, "decision: 3 minutes from 13 July", "green", sub="guardrail (≤ +15 s picking) held", subsize=14)
ab_how.note(380, 300, "metric, guardrails, duration and decision rule: written before day one", "pen", size=15)
ab_how.note(380, 330, "22 Jun → 6 Jul · two full weeks · ≈ 5,200 swaps per arm", "pen", size=15)

AB = dict(
    slug="ab-tests",
    kicker="a.k.a. “the fair taste test”",
    tldr="To know whether a change <b>caused</b> a difference, compare two groups that differ <b>only</b> in that change: split users <b>at random</b> into A (as now) and B (the change), run both <b>at the same time</b>, and compare on a <b>primary metric</b> chosen in advance, with <b>guardrails</b> that mustn't get worse. Write the metric, guardrails, duration and decision rule <b>before</b> the test starts. Before/after comparisons mix in everything else that changed.",
    chips=[("Family", "experimenting"), ("Origin", "randomised controlled trials; online experiments (Ronny Kohavi et al.)"), ("Lives in", "a test card, a feature flag and the analytics tool"), ("Pairs with", "sample size &amp; duration, guardrail metrics, reading results honestly")],
    problem_side="Larder, 22 June 2026",
    problem="""  <p class="lead">Should customers get <b>two or three minutes</b> to answer a swap? <b>Sam</b> says three: customers complain the timer is stressful. <b>Tomás</b> says two: pickers can't wait longer. Both have anecdotes. Changing it for everyone and comparing June with July would mix in <span class="hl-pink">the summer holidays, the weather and Rotterdam's growth</span>; whatever happened, nobody could say why.</p>
  <ul>
    <li>Anecdotes favour whoever has the most vivid story.</li>
    <li>Before/after comparisons can't separate the change from everything else.</li>
    <li>Without a metric chosen first, both sides will claim the result.</li>
  </ul>""",
    problem_figs=[ab_problem],
    analogy_side="the fair taste test",
    analogy="""  <p>A fair taste test of two recipes assigns tasters <b>at random</b> to A or B; they don't know which they got; the <b>plate, temperature and time of day are the same</b>. The only difference is the recipe, so any difference in scores is the recipe's. Serving A on Monday and B on Friday would also be testing Mondays and Fridays.</p>""",
    analogy_figs=[ab_analogy],
    map=[("Tasters", "Amsterdam express customers"),
         ("Random assignment", "A random 50/50 split by customer"),
         ("Recipe A / B", "Two minutes / three minutes"),
         ("The score sheet, agreed first", "Primary metric: answered by the customer"),
         ("Same plate and time", "Both groups at the same time, same stores")],
    how_side="random split, one change, decided in advance",
    how="""  <p>Grace wrote the test card first: primary metric <b>share of swaps answered by the customer</b>, guardrail <b>picking time per swap order ≤ +15 s</b>, two full weeks, and the rule “ship B if it wins on the primary metric and the guardrail holds”. Result: <b>82 % vs 88 %</b>, a difference of <b>+6 points</b> (95 % interval +3.8 to +8.2); picking <b>+7 s vs +11 s</b>. Three minutes from 13 July. Sam and Tomás both read the same card.</p>""",
    how_figs=[ab_how],
    steps=[("Write the hypothesis", "“Three minutes will raise the share of swaps customers answer.”"),
           ("Choose one primary metric", "And two or three guardrails, with limits."),
           ("Work out sample size and duration", "Before starting; whole weeks (see the next note)."),
           ("Split at random", "By customer, not by session; stable for the test."),
           ("Don't change anything else", "No other releases to the same flow during the test."),
           ("Decide by the rule you wrote", "Ship, don't ship, or re-test: as the card says.")],
    vocab=[("A/B test", "A randomised comparison of a control (A) and a variant (B)."),
           ("Control", "The current version."),
           ("Variant", "The changed version."),
           ("Primary metric", "The one number the test is designed to move."),
           ("Randomisation", "Assigning users to groups by chance."),
           ("Confidence interval", "The range the true difference likely lies in.")],
    code=dict(file="product/tests/2026-06-window.md", note="the test card, written 15 June 2026", plain=True, src="""
# Test: approval window, 2 vs 3 minutes                      owner: Grace · flag: approvals.window

Hypothesis   3 minutes raises the share of swaps answered by the customer.
Population   Amsterdam express customers with a swap; 50/50 by customer id
Primary      swaps answered by the customer (not defaulted)        baseline 82 %
Guardrails   picking time per swap order ≤ +15 s · refund tickets per 100 swaps not up
Size         ≈ 1,300 swaps per arm to detect +4 pts (see sample-size note)
Duration     22 Jun → 6 Jul (two full weeks, two Friday peaks)
Rule         Ship B if primary up and both guardrails hold; else keep A.

Result       A 82 %  B 88 %  · +6 pts (95 % CI +3.8 to +8.2) · picking +7 s vs +11 s
             refund tickets per 100 swaps: 2.9 vs 2.8 · ≈ 5,200 swaps per arm
Decision     B: three minutes for all Amsterdam express customers, 13 Jul. Rotterdam: 20 Jul.
"""),
    tools="tools: a feature flag with percentage and sticky assignment (Statsig, GrowthBook, LaunchDarkly, Optimizely); analytics for results; a test-card template.",
    gains=["<b>Cause, not correlation</b>.",
           "<b>Debates settled</b> by agreed numbers.",
           "<b>Guardrails protect</b> operations.",
           "<b>Decisions written in advance</b>, so nobody moves the goalposts.",
           "<b>Confidence intervals</b> show how sure we are."],
    losses=["<b>Needs traffic</b>: small products wait long.",
            "<b>Two versions to run</b> for weeks.",
            "<b>Only measures</b> what you chose to measure.",
            "<b>Easy to misread</b> without discipline."],
    baseline="Each line compares <b>changing for everyone and comparing before with after</b> to <b>a randomised A/B test with a primary metric, guardrails and a decision rule set in advance</b>.",
    ratings=[(2, 4, "Customers got the window that helps them answer."),
             (3, 4, "More answers, fewer defaulted swaps."),
             (1, 5, "A causal answer with a confidence interval."),
             (3, 4, "Two weeks to a clear decision."),
             (2, 4, "One change, one metric."),
             (2, 5, "Sam and Tomás read the same card."),
             (2, 4, "Leadership sees the result and the guardrail."),
             (3, 3, "Neutral."),
             (3, 3, "A card, a flag and two weeks.")],
    pitfalls=[("Before/after", "June vs July, holidays and all.", "run both at the same time, randomised."),
              ("Metric chosen afterwards", "Whichever number looks best.", "write the primary metric on the card first."),
              ("Splitting by session", "Customers see both versions.", "assign by customer, sticky."),
              ("Other changes mid-test", "A new release to the same flow.", "freeze the flow during the test.")],
    use=["Changes where the effect is uncertain and traffic is enough.",
         "Debates that anecdotes can't settle.",
         "Changes that might hurt something else (with guardrails).",
         "Tuning settings like timers, wording, ordering."],
    skip=["Low traffic: use qualitative tests or a longer, simpler comparison.",
          "Obvious fixes (a bug) and legal changes."],
    related=["<b>Sample size &amp; test duration</b> (this volume)", "<b>Guardrail metrics</b> (this volume)", "<b>Reading results honestly</b> (this volume)", "<b>Testable hypotheses</b> (Vol. 1)"],
    quiz=[("Why randomise?", "So the groups differ only in the change, not in who they are or when."),
          ("What must be written before the test?", "Hypothesis, primary metric, guardrails, duration and decision rule."),
          ("Why split by customer, not session?", "So each customer sees one version consistently."),
          ("What was the window test's result?", "82 % vs 88 % answered (+6 points), guardrail held; three minutes shipped.")],
    try_it="Pick a setting your team argues about. Write a test card: hypothesis, one primary metric, two guardrails with limits, duration in whole weeks, and the decision rule. Get both sides of the argument to sign it before the test starts.",
    remember="A fair <span class=\"hl\">taste test</span>: random tasters, one difference, the <span class=\"hl\">score sheet</span> agreed first.",
    sources=["Ronny Kohavi, Diane Tang, Ya Xu, <i>Trustworthy Online Controlled Experiments</i> (2020).",
             "Stefan Thomke, <i>Experimentation Works</i> (2020).",
             "Georgi Georgiev, <i>Statistical Methods in Online A/B Testing</i> (2019).",
             "Evan Miller, “How Not To Run an A/B Test” (2010)."],
)

# ------------------------------------------------------------------ 06 Sample Size & Test Duration
ss_problem = Doodle(760, 280, "Doodle of 15 June 2026. Femke asks for the window test's answer by Friday: three days. Grace isn't sure three days is enough, or whether one week is, and can't say why. Run too short and noise looks like a result; run too long and the team waits for nothing.",
                    "“Can we know by Friday?” Three days, one week, a month? Nobody can say why.")
ss_problem.box(20, 40, 320, 90, "Femke", "y", sub="“by Friday?”")
ss_problem.box(420, 30, 320, 110, None, "paper")
for i, t in enumerate(["3 days?", "1 week?", "a month?"]):
    ss_problem.text(580, 64 + i * 30, t, size=17)
ss_problem.note(380, 200, "too short: noise looks like a result", "red", size=18)
ss_problem.note(380, 240, "too long: everyone waits for nothing", "red", size=18)

ss_analogy = Doodle(760, 250, "Doodle of a pollster before an election. To tell 48 percent from 52 percent with confidence, they need about a thousand people, chosen fairly, polled across a whole week, not just on Monday. Asking ten friends in a café tells you nothing.",
                     "A pollster needs about a thousand people across a whole week, not ten friends in a café.")
ss_analogy.icon("megaphone", 40, 60, 1.3)
ss_analogy.box(160, 50, 260, 100, "10 friends", "pink", sub="noise")
ss_analogy.box(450, 50, 290, 100, "≈ 1,000 people", "green", sub="a whole week, fairly chosen")
ss_analogy.note(450, 210, "enough people, and the whole cycle", "pen")

ss_how = Doodle(760, 360, "Grace's sample size, 15 June 2026. Baseline: 82 percent of swaps answered. Smallest difference worth acting on: 4 points. Usual settings: 5 percent false-alarm rate, 80 percent power. Result: about 1,300 swaps per group. Amsterdam has about 750 swap orders a day, so 375 per group per day: enough in four days. But weekdays and Fridays behave differently, so the test runs two full weeks, covering two Friday peaks.",
                 "Baseline, smallest useful difference, the usual settings: about 1,300 per group. Then round up to whole weeks.")
for i, (t, v, f) in enumerate([("baseline", "82 %", "paper"), ("smallest useful", "+4 points", "y"), ("settings", "5 % · 80 % power", "blue")]):
    ss_how.box(14 + i * 248, 20, 236, 80, t, f, sub=v)
ss_how.arrow(380, 104, 380, 136)
ss_how.box(200, 140, 360, 70, "≈ 1,300 swaps per group", "green", size=17)
ss_how.box(14, 236, 360, 80, "750 swaps a day", "paper", sub="→ enough in 4 days")
ss_how.box(386, 236, 360, 80, "but: weekly cycle", "y", sub="→ run 2 full weeks")
ss_how.note(380, 344, "decided before day one; no stopping early", "pen", size=16)

SAMPLE = dict(
    slug="sample-size",
    kicker="a.k.a. “a thousand voters, not ten friends”",
    tldr="An A/B test's length isn't a matter of patience; it's arithmetic. Before you start, set the <b>baseline</b> (today's rate), the <b>smallest difference worth acting on</b>, and the usual settings (<b>5 % false-alarm rate, 80 % power</b>). That gives the <b>sample size per group</b>. Divide by your traffic for the days needed, then <b>round up to whole weeks</b> so every weekday (and peak) is covered. Then don't stop early.",
    chips=[("Family", "experimenting"), ("Origin", "statistical power analysis (Jacob Cohen, 1960s–); online experimentation practice"), ("Lives in", "the test card, before day one"), ("Pairs with", "A/B tests, reading results honestly, guardrail metrics")],
    problem_side="Larder, 15 June 2026",
    problem="""  <p class="lead">Femke likes the idea of the window test and asks for the answer <b>by Friday</b>: three days. Grace isn't sure three days is enough, or whether a week is, and <span class="hl-pink">can't say why</span>. She knows the two failure modes: run too short, and noise looks like a result; run too long, and the team waits for nothing.</p>
  <ul>
    <li>Test length is set by impatience or habit, not by need.</li>
    <li>Small differences need far more data than people expect.</li>
    <li>Weekday patterns (Friday peaks) skew short tests.</li>
  </ul>""",
    problem_figs=[ss_problem],
    analogy_side="the pollster",
    analogy="""  <p>To tell <b>48 % from 52 %</b> with confidence, a pollster needs about <b>a thousand people</b>, fairly chosen, across a <b>whole week</b>, not only Monday mornings. Asking <b>ten friends in a café</b> tells you nothing, however strongly they feel. The closer the race, the more people you need.</p>""",
    analogy_figs=[ss_analogy],
    map=[("48 % vs 52 %", "82 % vs 86 %: the smallest difference worth acting on"),
         ("A thousand people", "About 1,300 swaps per group"),
         ("A whole week, not Monday", "Two full weeks, two Friday peaks"),
         ("Ten friends", "Three days of data, mostly weekdays"),
         ("A closer race", "A smaller difference needs more data")],
    how_side="baseline, smallest difference, settings, weeks",
    how="""  <p>Grace used a standard calculator: <b>baseline 82 %</b>, smallest useful difference <b>+4 points</b>, <b>5 %</b> false-alarm rate, <b>80 %</b> power: about <b>1,300 swaps per group</b>. Amsterdam has about 750 swap orders a day, so <b>four days</b> would be enough on paper; but Fridays behave differently, so the card said <b>two full weeks</b>. Femke got a date (6 July) and a reason instead of a Friday.</p>""",
    how_figs=[ss_how],
    steps=[("Find the baseline", "Today's rate on the primary metric, from recent data."),
           ("Pick the smallest useful difference", "The smallest change you'd act on; not what you hope for."),
           ("Use standard settings", "5 % significance, 80 % power, two-sided."),
           ("Calculate per group", "With a sample size calculator; note the number on the card."),
           ("Convert to days, round to weeks", "Traffic per group per day; cover full weekly cycles."),
           ("Commit to it", "No stopping early because a result looks good.")],
    vocab=[("Sample size", "How many units (swaps, customers) each group needs."),
           ("Minimum detectable effect", "The smallest difference the test is designed to find."),
           ("Significance level", "The accepted false-alarm rate, usually 5 %."),
           ("Power", "The chance of detecting a real effect, usually 80 %."),
           ("Weekly cycle", "Patterns that repeat by day of week."),
           ("Underpowered", "Too small a test to detect the effect you care about.")],
    code=dict(file="product/tests/2026-06-window.md", note="the sample size section of the test card", plain=True, src="""
## Sample size and duration                               (calculated 15 Jun 2026)

Primary metric      swaps answered by the customer
Baseline            82 % (Amsterdam express, May–June)
Smallest useful     +4 points (86 %)   — smaller wouldn't change our decision
Settings            two-sided, α = 5 %, power = 80 %
Per group           n ≈ (1.96 + 0.84)² × (0.82·0.18 + 0.86·0.14) / 0.04² ≈ 1,300 swaps
Traffic             ≈ 750 swap orders/day in Amsterdam → ≈ 375 per group per day
Days needed         ≈ 4 days on paper
Duration            two full weeks (22 Jun → 6 Jul): two Friday peaks, all weekdays
Stopping            no early stop; result read on 7 Jul
"""),
    tools="tools: sample size calculators (Evan Miller's, Statsig's, GrowthBook's), or a few lines of Python; your traffic data per day.",
    gains=["<b>A date with a reason</b>, not impatience.",
           "<b>No false wins</b> from tiny samples.",
           "<b>No endless tests</b> either.",
           "<b>Weekly patterns covered</b>.",
           "<b>Honest about what can be detected</b>."],
    losses=["<b>Small products wait long</b> for small effects.",
            "<b>Needs a baseline</b> you trust.",
            "<b>The maths can intimidate</b>.",
            "<b>“Smallest useful” is a judgement</b>."],
    baseline="Each line compares <b>running tests for as long as patience allows</b> to <b>a sample size and duration calculated before day one and rounded to whole weeks</b>.",
    ratings=[(3, 3, "Indirect: better decisions."),
             (3, 3, "Indirect."),
             (1, 5, "The result means what it says."),
             (2, 4, "As short as possible, no shorter."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone knows when the answer comes, and why."),
             (2, 4, "Femke got a date and a reason."),
             (3, 3, "Neutral."),
             (3, 4, "A calculator and five minutes.")],
    pitfalls=[("“Run it till it's significant”", "Stopping on the first good day.", "fix the size and duration first."),
              ("Hoped-for effect", "Designing for +15 points.", "design for the smallest change worth acting on."),
              ("Partial weeks", "Monday to Thursday only.", "whole weekly cycles, including peaks."),
              ("Ignoring traffic", "A test that needs 40 weeks.", "check feasibility; test something bolder or use qualitative methods.")],
    use=["Every A/B test, before it starts.",
         "When someone asks “can we know by Friday?”.",
         "Deciding whether a test is feasible at all.",
         "Planning a roadmap of experiments."],
    skip=["Qualitative tests (interviews, prototypes).",
          "Changes too obvious to test."],
    related=["<b>A/B tests</b> (this volume)", "<b>Reading results honestly</b> (this volume)", "<b>Baseline before you build</b> (Vol. 1)", "<b>Guardrail metrics</b> (this volume)"],
    quiz=[("What three inputs decide sample size?", "The baseline, the smallest useful difference, and the settings (significance and power)."),
          ("Why round up to whole weeks?", "Weekday patterns and peaks would otherwise skew the result."),
          ("What did Larder need per group?", "About 1,300 swaps."),
          ("Why not stop early when it looks good?", "Early looks are noisy; stopping on a good day inflates false wins.")],
    try_it="For your next test, write the baseline and the smallest difference you'd act on. Put them into a sample size calculator, divide by your daily traffic per group, round up to whole weeks, and write the end date on the test card before day one.",
    remember="A thousand <span class=\"hl\">voters</span>, a whole <span class=\"hl\">week</span>, not ten friends on a Monday.",
    sources=["Ronny Kohavi et al., <i>Trustworthy Online Controlled Experiments</i> (2020), on power.",
             "Evan Miller, “Sample Size Calculator” and “How Not To Run an A/B Test” (evanmiller.org).",
             "Jacob Cohen, <i>Statistical Power Analysis for the Behavioral Sciences</i>, 2nd ed. (1988).",
             "Georgi Georgiev, <i>Statistical Methods in Online A/B Testing</i> (2019)."],
)

# ------------------------------------------------------------------ 07 Guardrail Metrics
gm_problem = Doodle(760, 280, "Doodle of the live order updates test in August 2026. The team sends a push at every step: picked, packed, courier assigned, ten minutes away. Where-is-my-order tickets fall by a third, a clear win. Then Dee notices push opt-outs are up almost a point: customers are switching off notifications, including the ones that ask them to approve swaps.",
                    "“Where is my order?” tickets −34 %: a win. But customers are switching off notifications, including swap ones.")
gm_problem.box(20, 40, 320, 90, "“where is it?” tickets", "green", sub="−34 %")
gm_problem.box(420, 40, 320, 90, "push opt-outs", "pink", sub="+0.9 points", stroke="red")
gm_problem.note(380, 190, "the win was eating the thing approvals depends on", "red", size=18)

gm_analogy = Doodle(760, 250, "Doodle of a diet that works: the scale shows four kilos lost in a month. But the doctor also checks blood pressure and energy, and both are worse. The weight was the goal; the other two are guardrails, and a diet that breaks them isn't a good diet.",
                     "A diet loses four kilos, but blood pressure and energy got worse. The scale wasn't the only number that mattered.")
gm_analogy.icon("stopwatch", 40, 60, 1.3)
gm_analogy.box(160, 50, 180, 100, "weight", "green", sub="−4 kg")
gm_analogy.box(360, 50, 180, 100, "blood pressure", "pink", sub="worse")
gm_analogy.box(560, 50, 180, 100, "energy", "pink", sub="worse")
gm_analogy.note(450, 210, "the goal, and what mustn't break", "pen")

gm_how = Doodle(760, 360, "The live updates test with guardrails, August and September 2026. Primary: where-is-my-order tickets per 1,000 orders, target minus 30 percent. Guardrails, with limits: push opt-out rate at most plus 0.5 points, order conversion not down, approvals answered within the window not down. Round one, push at every step: tickets minus 34 percent, opt-outs plus 0.9 points: guardrail tripped, not shipped. Round two, two pushes only (swap, ten minutes away) plus an in-app timeline: tickets minus 31 percent, opt-outs plus 0.2: shipped 21 September.",
                 "A primary metric and guardrails with limits. Round one won and broke a guardrail; round two won and held.")
gm_how.box(14, 14, 732, 60, "primary: “where is my order?” tickets per 1,000 orders, −30 %", "y", size=15)
gm_how.box(14, 88, 732, 60, "guardrails: opt-outs ≤ +0.5 pts · conversion · approvals answered", "blue", size=14)
gm_how.box(14, 166, 360, 110, None, "pink", stroke="red")
gm_how.head(194, 196, "round 1 · push every step", size=15)
gm_how.text(194, 226, "tickets −34 % ✓", size=15)
gm_how.text(194, 254, "opt-outs +0.9 ✗ → not shipped", "t t-red", size=14)
gm_how.box(386, 166, 360, 110, None, "green", stroke="green")
gm_how.head(566, 196, "round 2 · 2 pushes + timeline", size=15)
gm_how.text(566, 226, "tickets −31 % ✓", size=15)
gm_how.text(566, 254, "opt-outs +0.2 ✓ → shipped 21 Sep", size=14)
gm_how.note(380, 318, "a win that breaks a guardrail isn't a win", "red", size=17)

GUARDRAILS = dict(
    slug="guardrail-metrics",
    kicker="a.k.a. “blood pressure on a diet”",
    tldr="Every test is designed to move one number; most changes can also hurt others. <b>Guardrail metrics</b> are the few numbers that <b>must not get worse</b> while you chase the primary one: conversion, crashes, opt-outs, operational load, things another feature depends on. Pick them <b>before</b> the test, give each a <b>limit</b>, and treat a tripped guardrail as a <b>no</b>, even when the primary metric wins.",
    chips=[("Family", "experimenting"), ("Origin", "online experimentation practice (Microsoft, Airbnb, Spotify); OEC and guardrails (Kohavi et al.)"), ("Lives in", "the test card, and on the health page"), ("Pairs with", "A/B tests, dashboards that get used, handling the HiPPO")],
    problem_side="Larder, 24 August 2026",
    problem="""  <p class="lead">Live order updates are bet 3. The first version sends a push at <b>every step</b>: picked, packed, courier assigned, ten minutes away. In the test, <b>“where is my order?” tickets fall 34 %</b>, better than the 30 % target. Then Dee notices <b>push opt-outs are up 0.9 points</b>: customers are switching off notifications altogether, <span class="hl-pink">including the ones that ask them to approve swaps</span>.</p>
  <ul>
    <li>Tests are judged on the number they were built to move.</li>
    <li>Side effects show up in other teams' numbers, later.</li>
    <li>A win on one metric can quietly undo another feature.</li>
  </ul>""",
    problem_figs=[gm_problem],
    analogy_side="the diet",
    analogy="""  <p>A diet works: the scale shows <b>four kilos lost</b> in a month. But the doctor also checks <b>blood pressure</b> and <b>energy</b>, and both are worse. Weight was the goal; the others are guardrails. A diet that breaks them isn't a good diet, however good the scale looks.</p>""",
    analogy_figs=[gm_analogy],
    map=[("Weight lost", "“Where is my order?” tickets down 34 %"),
         ("Blood pressure", "Push opt-outs up 0.9 points"),
         ("Energy", "Approvals answered (depends on notifications)"),
         ("The doctor's check-up", "Guardrails on the test card, with limits"),
         ("A gentler diet", "Round two: two pushes and an in-app timeline")],
    how_side="a primary metric and limits that mean no",
    how="""  <p>The test card had three guardrails with limits: <b>opt-outs ≤ +0.5 points</b>, conversion not down, approvals answered not down. Round one tripped the first, so it <b>wasn't shipped</b>, despite the win. Noor redesigned it: <b>two pushes</b> only (a swap, and ten minutes away) plus an <b>in-app timeline</b>. Round two: tickets <b>−31 %</b>, opt-outs <b>+0.2</b>. Shipped on 21 September.</p>""",
    how_figs=[gm_how],
    steps=[("List what could get worse", "Other features, operations, revenue, trust, performance."),
           ("Pick two or three guardrails", "The ones that matter most and can be measured in the test."),
           ("Set a limit for each", "“Opt-outs ≤ +0.5 points”: a number, before the test."),
           ("Write the rule", "Any guardrail tripped → don't ship as is."),
           ("Watch them during the test", "Alert if one crosses its limit early."),
           ("Redesign, not override", "Find a version that wins without breaking the guardrail.")],
    vocab=[("Guardrail metric", "A number that must not get worse during a change."),
           ("Primary metric", "The number the change is meant to improve."),
           ("Limit", "The worst acceptable value for a guardrail."),
           ("Opt-out rate", "The share of users switching off notifications."),
           ("Side effect", "An unintended change in another number."),
           ("OEC", "Overall evaluation criterion: the combined measure of success.")],
    code=dict(file="product/tests/2026-08-live-updates.md", note="test card and results, August–September 2026", plain=True, src="""
# Test: live order updates (bet 3)                     owner: Grace · design: Noor

Primary      "where is my order?" tickets per 1,000 orders      target −30 %
Guardrails   push opt-out rate                 limit ≤ +0.5 points
             order conversion                  limit: not down (CI excludes −0.2)
             swaps answered by the customer    limit: not down
Rule         ship only if primary wins and every guardrail holds

Round 1  3–17 Aug   push at every step (4 per order)
         tickets −34 % ✓  · opt-outs +0.9 pts ✗ · conversion = · answered −1 pt
         → NOT shipped (guardrail tripped)
Round 2  31 Aug–14 Sep  2 pushes (swap, 10 min away) + in-app timeline
         tickets −31 % ✓  · opt-outs +0.2 pts ✓ · conversion = · answered =
         → shipped 21 Sep
"""),
    tools="tools: the experimentation platform's guardrail settings (Statsig, Eppo, GrowthBook support them); alerts on guardrails during tests; the health page's guardrail row.",
    gains=["<b>Side effects caught</b> before shipping.",
           "<b>Other features protected</b> (approvals).",
           "<b>Better designs</b>: a win that doesn't break things.",
           "<b>Trust from other teams</b>.",
           "<b>Clear “no” rules</b>, set in advance."],
    losses=["<b>More metrics to watch</b>.",
            "<b>Some wins are blocked</b>.",
            "<b>Picking guardrails</b> takes judgement.",
            "<b>Bigger samples</b> to detect small guardrail moves."],
    baseline="Each line compares <b>judging a test only on the metric it was built to move</b> to <b>a primary metric plus two or three guardrails with limits that mean no</b>.",
    ratings=[(2, 5, "Customers keep the notifications that protect their orders."),
             (2, 4, "One win doesn't undo another."),
             (2, 5, "Limits set before the test."),
             (3, 4, "Two rounds, five weeks, a better design."),
             (3, 4, "Few, chosen guardrails."),
             (2, 4, "Everyone sees what a win must not break."),
             (2, 4, "Dee's team trusts product tests."),
             (3, 3, "Neutral."),
             (3, 3, "A few extra metrics per test.")],
    pitfalls=[("No guardrails", "A win on one number, damage elsewhere.", "two or three guardrails on every test card."),
              ("Limits after the fact", "“+0.9 isn't that bad.”", "write the limit before the test."),
              ("Overriding a trip", "Shipped anyway, it won.", "redesign until it wins without tripping."),
              ("Too many guardrails", "Fifteen numbers; something always moves.", "the two or three that matter most.")],
    use=["Every A/B test.",
         "Changes to notifications, pricing, checkout, operations.",
         "Features that other features depend on.",
         "Rollouts (as in dark launches)."],
    skip=["Purely cosmetic changes with no plausible side effects (rare)."],
    related=["<b>A/B tests</b> (this volume)", "<b>Dark launches &amp; rollouts</b> (Vol. 3)", "<b>Dashboards that get used</b> (this volume)", "<b>Handling the HiPPO</b> (Vol. 2)"],
    quiz=[("What's a guardrail metric?", "A number that must not get worse while you improve the primary one."),
          ("When should limits be set?", "Before the test starts, on the test card."),
          ("What happened in round one?", "Tickets fell 34 %, but opt-outs rose 0.9 points (limit 0.5), so it wasn't shipped."),
          ("How did round two pass?", "Two pushes plus an in-app timeline: tickets −31 %, opt-outs +0.2.")],
    try_it="For your next test, list everything the change could make worse. Pick the two that matter most, write a limit for each, and add the rule “any guardrail tripped means we don't ship as is”.",
    remember="Weigh yourself, and check the <span class=\"hl\">blood pressure</span>. A win that breaks a <span class=\"hl\">guardrail</span> isn't a win.",
    sources=["Ronny Kohavi et al., <i>Trustworthy Online Controlled Experiments</i> (2020), guardrail metrics.",
             "Airbnb Engineering, “Designing Experimentation Guardrails” (2021).",
             "Spotify Engineering, “Risk-aware product decisions in A/B tests” (2023).",
             "Statsig documentation, “Guardrail metrics”."],
)

# ------------------------------------------------------------------ 08 Reading Results Honestly
rr_problem = Doodle(760, 280, "Doodle of the window test's early days in June 2026. On day three, three minutes is ahead by 9 points and 'significant'; Femke wants to stop and ship. On day five, an analyst finds that Android users gained 11 points and suggests a special Android rule. Both are tempting; both are traps.",
                    "Day 3: +9 points, “significant”, stop! Day 5: “Android +11”, a special rule! Both are traps.")
rr_problem.box(20, 40, 320, 100, "day 3: +9 pts", "pink", sub="“stop and ship!”", stroke="red")
rr_problem.box(420, 40, 320, 100, "day 5: Android +11", "pink", sub="“an Android rule!”", stroke="red")
rr_problem.note(380, 200, "peeking and fishing", "red", size=20)

rr_analogy = Doodle(760, 250, "Doodle of a football bet settled at half-time because your team is winning, and a friend who, after losing, notes that his team won the second half. Neither is the result of the match. The bet was on the full ninety minutes.",
                     "Settling a bet at half-time, or claiming the second half after losing: neither is the match result.")
rr_analogy.icon("stopwatch", 40, 60, 1.2)
rr_analogy.box(160, 50, 270, 100, "half-time lead", "pink", sub="“pay up now”")
rr_analogy.box(460, 50, 280, 100, "“we won the 2nd half”", "pink", sub="after losing")
rr_analogy.note(450, 210, "the bet was on ninety minutes", "pen")

rr_how = Doodle(760, 360, "How Grace read the window test on 7 July 2026. One: no peeking; the result was read once, at the planned end, two weeks. The day-three lead of 9 points had shrunk to 6. Two: the primary metric first, as a range: plus 6 points, 95 percent interval 3.8 to 8.2. Three: guardrails next: picking plus 11 seconds, within the limit. Four: segments are hypotheses, not results: the Android gain was noted for a future test. Five: decide by the rule written in advance.",
                 "Read once, at the end. Primary as a range, guardrails, then segments as ideas, then the rule you wrote first.")
for i, (t, s, f) in enumerate([("1 · no peeking", "read once, day 14", "y"), ("2 · primary, as a range", "+6 pts (+3.8 … +8.2)", "green"), ("3 · guardrails", "picking +11 s ✓", "blue"),
                               ("4 · segments = ideas", "Android +11 → a new test", "paper"), ("5 · the rule", "written on 15 Jun", "green")]):
    y = 14 + i * 64
    rr_how.box(14, y, 732, 54, None, f, rx=6)
    rr_how.text(30, y + 34, t, "t-head", anchor="start", size=15)
    rr_how.text(730, y + 34, s, anchor="end", size=14)
rr_how.note(380, 346, "day 3 said +9 · day 14 said +6: the early lead shrank", "red", size=15)

READING = dict(
    slug="reading-results",
    kicker="a.k.a. “the bet is on ninety minutes”",
    tldr="Most bad experiment decisions come from reading results, not running tests. <b>Don't peek and stop</b> when it looks good; read <b>once</b>, at the planned end. Report the primary metric as a <b>range</b> (a confidence interval), not a single point. Check <b>guardrails</b>. Treat <b>segment</b> findings as <b>new hypotheses</b>, not results. And decide by the <b>rule you wrote before the test</b>, not by how you feel about the numbers.",
    chips=[("Family", "experimenting"), ("Origin", "pre-registration in science; experimentation practice on peeking and multiple comparisons"), ("Lives in", "the test card's results section, read once"), ("Pairs with", "A/B tests, sample size &amp; duration, bets not promises")],
    problem_side="Larder, 7 July 2026",
    problem="""  <p class="lead">On <b>day three</b> of the window test, three minutes is ahead by <b>9 points</b> and the dashboard says “significant”; Femke wants to stop and ship. On <b>day five</b>, an analyst finds that <b>Android users gained 11 points</b> and suggests a special rule for Android. Both are tempting. <span class="hl-pink">Both are traps</span>: early leads shrink, and if you look at enough segments, one always looks exciting.</p>
  <ul>
    <li>Checking daily and stopping on a good day inflates false wins.</li>
    <li>Slicing results many ways finds patterns that are just noise.</li>
    <li>Single numbers hide how uncertain the result is.</li>
  </ul>""",
    problem_figs=[rr_problem],
    analogy_side="the bet on the match",
    analogy="""  <p>You bet on the <b>full ninety minutes</b>. Settling at <b>half-time</b> because your team is ahead isn't the result; neither is a friend who, after losing, points out his team <b>won the second half</b>. Both are true statements about part of the match, and both are wrong about the bet.</p>""",
    analogy_figs=[rr_analogy],
    map=[("Settling at half-time", "Stopping on day three because it's ahead"),
         ("“We won the second half”", "“Android users gained 11 points”"),
         ("The full ninety minutes", "The planned two weeks"),
         ("The final score, with the margin", "+6 points, 95 % interval +3.8 to +8.2"),
         ("The terms of the bet", "The decision rule written on 15 June")],
    how_side="read once, as a range, by the rule",
    how="""  <p>Grace held the line: the test ran its <b>two weeks</b>. The day-three lead of 9 points ended at <b>+6</b> (interval <b>+3.8 to +8.2</b>), still a clear win, but smaller. Guardrails held. The <b>Android</b> gain went on the opportunity tree as a hypothesis for its own test, not a rule. The decision followed the card: ship three minutes. Femke later said the shrinking lead was what convinced her to wait next time.</p>""",
    how_figs=[rr_how],
    steps=[("Pre-register", "Metric, guardrails, duration, rule: written before day one."),
           ("Don't peek and stop", "Look only for safety (guardrails); read the result once, at the end."),
           ("Report a range", "The difference with its confidence interval."),
           ("Check guardrails", "Any tripped guardrail overrides the win."),
           ("Treat segments as hypotheses", "Interesting splits become new tests."),
           ("Decide by the rule", "And write down any disagreement with it.")],
    vocab=[("Peeking", "Checking results repeatedly and stopping when they look good."),
           ("Pre-registration", "Writing the plan and rules before the test."),
           ("Confidence interval", "A range likely to contain the true effect."),
           ("Multiple comparisons", "Testing many slices; some look significant by chance."),
           ("False positive", "A “win” that isn't real."),
           ("Regression to the mean", "Extreme early results drifting back toward normal.")],
    code=dict(file="product/tests/2026-06-window.md", note="the results section, read once on 7 July 2026", plain=True, src="""
## Results (read 7 Jul 2026, as planned)

Primary     answered by the customer: A 82.1 %  B 88.0 %
            difference +5.9 pts · 95 % CI +3.8 to +8.2 · ≈ 5,200 swaps per arm
Guardrails  picking time per swap order: +7 s vs +11 s (limit +15 s) ✓
            refund tickets per 100 swaps: 2.9 vs 2.8 ✓
Rule        ship B if primary up and guardrails hold → SHIP B

Not used for the decision
  day-3 interim look: +9 pts (shrank to +5.9 by day 14)
  Android-only: +11 pts → hypothesis H-14 for its own test (not a rule)
"""),
    tools="tools: experimentation platforms with sequential testing or fixed-horizon reads (Statsig, Eppo, GrowthBook); confidence intervals by default; a results template on the test card.",
    gains=["<b>Fewer false wins</b> shipped.",
           "<b>Honest uncertainty</b> in every result.",
           "<b>Segments become a test backlog</b>, not rules.",
           "<b>Decisions match the plan</b>, so nobody moves goalposts.",
           "<b>Leaders learn</b> to wait."],
    losses=["<b>Patience</b>: no early celebrations.",
            "<b>Ranges disappoint</b> people who want one number.",
            "<b>Some real segment effects</b> wait for their own test.",
            "<b>Discipline</b> under pressure."],
    baseline="Each line compares <b>reading results daily, stopping on a good day and slicing for wins</b> to <b>reading once at the planned end, as a range, with guardrails and the pre-written rule</b>.",
    ratings=[(3, 3, "Indirect: fewer bad changes."),
             (3, 4, "Real effects, honestly sized."),
             (1, 5, "No peeking, no fishing."),
             (3, 3, "Slightly slower, much surer."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone reads the same results section."),
             (2, 5, "Femke trusts the next result."),
             (3, 3, "Neutral."),
             (3, 4, "A results template, read once.")],
    pitfalls=[("Stopping on a good day", "Day three looked great.", "read once, at the planned end."),
              ("A single number", "“+6 points.”", "the range: +3.8 to +8.2."),
              ("Segment rules", "A special Android rule from one slice.", "segments become new hypotheses."),
              ("Rewriting the rule", "“+6 is basically +4, let's also…”", "decide by the rule; record any disagreement.")],
    use=["Every experiment's results.",
         "When leaders want early answers.",
         "When someone finds an exciting segment.",
         "Reviews of past experiments."],
    skip=["Safety stops: if a guardrail is badly broken, stop early (that's what guardrails are for)."],
    related=["<b>A/B tests</b> (this volume)", "<b>Sample size &amp; test duration</b> (this volume)", "<b>Bets, not promises</b> (Vol. 2)", "<b>Testable hypotheses</b> (Vol. 1)"],
    quiz=[("Why not stop on day three?", "Early results are noisy; stopping on a good day inflates false wins."),
          ("How should the primary result be reported?", "As a difference with a confidence interval."),
          ("What do you do with an exciting segment?", "Turn it into a hypothesis for its own test."),
          ("When is it fine to stop early?", "When a guardrail is badly broken: a safety stop.")],
    try_it="Take your last experiment. Rewrite its result as a difference with a confidence interval, list every segment someone highlighted, and check whether the decision matched a rule written in advance. Write the rule for the next one now.",
    remember="The bet is on the full <span class=\"hl\">ninety minutes</span>. Report the score with its <span class=\"hl\">margin</span>.",
    sources=["Ronny Kohavi et al., <i>Trustworthy Online Controlled Experiments</i> (2020), on peeking and pitfalls.",
             "Evan Miller, “How Not To Run an A/B Test” (2010).",
             "Andrew Gelman and Eric Loken, “The garden of forking paths” (2013).",
             "Center for Open Science, on pre-registration (cos.io)."],
)

NOTES = [AB, SAMPLE, GUARDRAILS, READING]
