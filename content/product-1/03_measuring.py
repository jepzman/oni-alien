# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 1 · Measuring what matters.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 North Star Metric
ns_problem = Doodle(760, 280, "Doodle of four Larder teams each chasing their own number. Marketing celebrates sign-ups up twenty percent after a promotion. Operations watches picks per hour. Support counts tickets closed per day. Product watches conversion. The promotion floods the stores with one-time customers, picks per hour drop, tickets rise, and fewer orders arrive complete and on time. Every team hit its own target; customers got a worse service.",
                    "Every team hit its own number. Customers got a worse Friday.")
for i, (team, num, ok) in enumerate([("marketing", "sign-ups +20 %", True), ("operations", "picks / hour ↓", False), ("support", "tickets / day ↑", False), ("product", "conversion +2 %", True)]):
    x = 14 + i * 186
    ns_problem.box(x, 20, 172, 74, team, "green" if ok else "pink", sub=num, stroke="" if ok else "red", size=16, subsize=14)
    ns_problem.arrow(x + 86, 100, x + 86 + (i - 1.5) * 40, 150, dash=True)
ns_problem.note(380, 190, "four teams, four directions", "red", size=19)
ns_problem.box(200, 206, 360, 54, "orders complete & on time ↓", "pink", stroke="red", size=16)

ns_analogy = Doodle(760, 240, "Doodle of a rowing eight. When each rower pulls at their own pace, the boat zigzags. When the cox calls one rhythm, everyone pulls together and the boat goes straight and fast. The cox's call is the north star; each rower's stroke is an input.",
                    "A rowing eight: one rhythm from the cox, eight people pulling the same way.")
ns_analogy.raw('<path class="d f-blue" d="M60 140 Q380 190 700 140 Q380 160 60 140 Z"/>')
for i in range(8):
    x = 130 + i * 64
    ns_analogy.raw(f'<circle class="d f-y" cx="{x}" cy="146" r="9"/><path class="d d-thin" d="M{x} 155 L{x - 30} 200"/>')
ns_analogy.raw('<circle class="d f-green" cx="660" cy="146" r="10"/>')
ns_analogy.note(660, 110, "cox: “stroke!”", "green", size=18)
ns_analogy.note(300, 60, "one rhythm, everyone pulls the same way", "pen", size=18)

ns_how = Doodle(760, 360, "Larder's north star and its inputs. North star: perfect orders per week, meaning delivered complete or with an accepted substitute, on time, and with no refund ticket. October 2025 baseline: about 23,000 a week, 82 percent of orders. Four input metrics, each owned by a team: orders per week, owned by marketing and product; percent complete or accepted swap, owned by Grace with the stores; percent on time, owned by Joost and Dispatch; percent with no refund ticket, owned by Grace with support.",
                 "One number for value delivered, four inputs underneath, each with an owner.")
ns_how.box(190, 14, 380, 80, "perfect orders / week", "green", sub="complete · on time · no refund ticket", size=20, subsize=14)
ns_how.note(660, 44, "≈ 23,000", "green", size=19)
ns_how.note(660, 70, "82 % of orders", "green", size=16)
inputs = [("orders / week", "marketing, product"), ("% complete", "Grace + stores"), ("% on time", "Joost + Dispatch"), ("% no refund", "Grace + support")]
for i, (m, owner) in enumerate(inputs):
    x = 14 + i * 186
    ns_how.line(f"M380 98 L{x + 86} 150", thin=True)
    ns_how.box(x, 150, 172, 70, m, "y" if "Grace" in owner else "blue", sub=owner, size=16, subsize=13)
ns_how.note(380, 310, "a perfect order needs all four; each team owns one input", "pen", size=17)

NORTH_STAR = dict(
    slug="north-star-metric",
    kicker="a.k.a. “one rhythm for the whole boat”",
    tldr="Pick <b>one metric</b> that captures the value customers get from the product and that leads to the business's success. Break it into a few <b>input metrics</b> that teams can actually move, and give each input an <b>owner</b>. The north star doesn't replace other numbers; it settles arguments about which number wins, and stops teams from hitting their own targets while customers get a worse service.",
    chips=[("Family", "measuring what matters"), ("Origin", "Sean Ellis and growth teams (2010s); Amplitude's North Star Playbook"), ("Lives in", "the top of every team dashboard and the quarterly review"), ("Pairs with", "outcomes over outputs, leading vs lagging, baseline")],
    problem_side="Larder, four dashboards",
    problem="""  <p class="lead">Every team at Larder has its own number. Marketing celebrates <b>sign-ups up 20 %</b> after a promotion. Operations watches picks per hour, support counts tickets closed per day, product watches conversion. The promotion floods Friday with one-time customers: picks per hour drop, tickets rise, and <span class="hl-pink">fewer orders arrive complete and on time</span>. Every team can show its target was met.</p>
  <ul>
    <li>Local metrics pull teams in different directions.</li>
    <li>Nobody owns the number that describes what customers actually get.</li>
    <li>Arguments about priorities become arguments about whose metric matters.</li>
  </ul>""",
    problem_figs=[ns_problem],
    meanwhile=[("architect-1", "business-drivers", "Ana's drivers say what the business needs; Grace's north star says what customers get, and feeds drivers 2 and 4.", "Grace's north star, perfect orders per week, sits between drivers 2 (on time) and 4 (trust).")],
    analogy_side="the rowing eight",
    analogy="""  <p>In a rowing eight, if each rower pulls at their own pace the boat zigzags, however strong they are. The <b>cox</b> calls one rhythm, and everyone pulls to it. Each rower still has a job (their stroke), but there's one shared measure of whether the boat is going well: <b>speed, in a straight line</b>.</p>""",
    analogy_figs=[ns_analogy],
    map=[("The boat's speed in a straight line", "Perfect orders per week"),
         ("The cox's rhythm", "The north star everyone checks first"),
         ("Each rower's stroke", "Input metrics: % complete, % on time…"),
         ("A rower sprinting alone", "Marketing's promotion flooding Friday"),
         ("The coach reviewing the race", "The quarterly review of the north star and inputs")],
    how_side="one value number, a few inputs",
    how="""  <p>A good north star <b>measures value delivered</b> (not revenue alone), can be counted every week, and leads to the business result. Grace, Priya and Joost choose <b>perfect orders per week</b>: delivered complete or with an accepted substitute, on time, and with no refund ticket afterwards.</p>""",
    how_figs=[ns_how],
    steps=[("Start from the customer's value", "What does a great experience look like, in one countable event? (A perfect order.)"),
           ("Check it leads to the business result", "Does it predict drivers 2 and 4, and repeat orders? Check with data."),
           ("Define it precisely", "Complete or accepted swap, within the promised window, no ticket within 7 days."),
           ("Break it into inputs", "Three to five factors teams can move: volume, completeness, on time, no refund."),
           ("Give each input an owner", "One team per input; shared review weekly."),
           ("Guard against gaming", "Watch counter-metrics: cost per order, picker workload, complaints.")],
    vocab=[("North star metric", "One number that captures the value customers get."),
           ("Input metric", "A factor teams can move that drives the north star."),
           ("Counter-metric", "A number watched to catch harm from chasing the north star."),
           ("Vanity metric", "A number that looks good but doesn't guide decisions (downloads)."),
           ("Metric tree", "The north star broken down into its inputs."),
           ("Perfect order", "Larder: complete or accepted swap, on time, no refund ticket.")],
    code=dict(file="product/metrics/north-star.md", note="definition, agreed 19 Nov 2025", plain=True, src="""
# North star: perfect orders per week            agreed: Grace, Priya, Joost, Femke

Definition   An order is PERFECT when all three hold:
             1. delivered complete, or every swap was accepted by the customer
             2. delivered inside the promised window (express 30 min / the slot)
             3. no refund or complaint ticket within 7 days
Baseline     Oct 2025: ≈ 23,000 / week = 82 % of orders (express 79 %, slots 88 %)
Why          predicts repeat orders: customers with 3 perfect orders in a row order
             1.6 × more next month (order data, Jan–Sep 2025)

Inputs                        owner                 now
  orders / week               marketing + product   28,000
  % complete or swap accepted Grace + stores        91 %
  % on time                   Joost + Dispatch      88 %
  % no refund ticket          Grace + support       94 %

Counter-metrics  cost per order (Marco) · picks per hour (Joost) · support hours (Sam)
Review           every Monday, 15 min, all four owners
"""),
    tools="tools: one shared dashboard (Metabase, Looker, Amplitude, Mixpanel) with the north star at the top and the inputs below. Amplitude's North Star Playbook is a good free guide.",
    gains=["<b>One direction</b> for every team.",
           "<b>Customer value</b> at the centre, not only revenue.",
           "<b>Settles priority arguments</b>: which input moves the star most?",
           "<b>Owners for each input</b>, so it isn't nobody's job.",
           "<b>Cross-team reviews</b> that talk about the same thing."],
    losses=["<b>Takes debate</b> to define precisely.",
            "<b>Can be gamed</b> without counter-metrics.",
            "<b>One number hides detail</b>: inputs and segments still matter.",
            "<b>Needs good data</b>, joined across systems."],
    baseline="Each line compares <b>each team chasing its own local metric</b> to <b>one north star (perfect orders per week) with four owned inputs and counter-metrics, reviewed weekly</b>.",
    ratings=[(2, 5, "It counts what customers actually get."),
             (2, 4, "It predicts repeat orders and links to drivers 2 and 4."),
             (2, 4, "Defined precisely, with a baseline from data."),
             (3, 4, "Weekly reviews show whether changes help."),
             (2, 5, "One number settles which work matters most."),
             (2, 5, "Every team can say what a perfect order is."),
             (3, 4, "Leaders see one honest number every Monday."),
             (3, 3, "Neutral."),
             (3, 3, "A definition, a dashboard, a 15-minute weekly review.")],
    pitfalls=[("Revenue as the north star", "Revenue grows while customers get worse service.", "measure value delivered; revenue follows."),
              ("Vague definition", "“Happy orders.”", "define it precisely enough to count automatically."),
              ("No counter-metrics", "Perfect orders up because pickers work unpaid overtime.", "watch cost, workload and complaints alongside."),
              ("Inputs nobody owns", "Everyone looks at the star; nobody moves it.", "one owner per input, reviewed weekly.")],
    use=["Several teams pulling in different directions.",
         "Setting the product strategy or quarterly goals.",
         "When revenue metrics hide customer problems.",
         "Explaining product priorities to leadership."],
    skip=["A single small team with one obvious goal.",
          "Before you understand customer value: interview first.",
          "As the only number: keep inputs and counter-metrics."],
    related=["<b>Leading vs lagging indicators</b> (this volume)", "<b>Outcomes over outputs</b> (this volume)", "<b>Baseline before you build</b> (this volume)", "<b>Business drivers &amp; goals</b> (Ana, vol. 1)"],
    quiz=[("What makes a good north star?", "It measures value customers get, can be counted often, and leads to business success."),
          ("What is Larder's north star?", "Perfect orders per week: complete or accepted swap, on time, no refund ticket within 7 days."),
          ("Why add counter-metrics?", "To catch harm from chasing the north star, such as higher cost or picker overwork."),
          ("What are input metrics for?", "They break the north star into factors teams can move, each with an owner.")],
    try_it="Write one sentence describing a perfect experience with your product, then turn it into a countable event. Check last month's data: what share of customers got it? Name three inputs and who could own each.",
    remember="One <span class=\"hl\">rhythm</span> for the boat. Each team pulls one <span class=\"hl\">input</span>.",
    sources=["Amplitude, <i>The North Star Playbook</i> (amplitude.com, 2019).",
             "Sean Ellis &amp; Morgan Brown, <i>Hacking Growth</i> (2017).",
             "John Cutler, “North Star Framework” talks and posts (2019–2021).",
             "Alistair Croll &amp; Benjamin Yoskovitz, <i>Lean Analytics</i> (2013)."],
)

# ------------------------------------------------------------------ 10 Leading vs Lagging Indicators
ll_problem = Doodle(760, 250, "Doodle of a timeline. Grace's outcome, refund tickets, arrives days after an order, and its effect on repeat orders shows a month later. By the time the number moves, weeks of work have passed with no signal. Meanwhile marketing watches app downloads, which move fast but predict nothing.",
                    "The number she cares about arrives weeks late. The fast number marketing watches predicts nothing.")
ll_problem.arrow(20, 120, 740, 120, label="time →", lx=700, ly=106)
for x, t, s, f in [(40, "order", "day 0", "paper"), (250, "refund ticket", "day 1–7", "pink"), (520, "repeat orders", "+30 days", "pink")]:
    ll_problem.box(x, 140, 190, 60, t, f, sub=s, size=16, subsize=13)
ll_problem.box(40, 20, 260, 60, "app downloads ↑", "y", sub="fast, but predicts nothing", size=16, subsize=13)
ll_problem.note(560, 60, "weeks with no signal", "red", size=19)

ll_analogy = Doodle(760, 240, "Doodle of someone getting fitter. The weight on the scale and the race time are lagging: they move slowly, weeks later. Calories eaten today and steps walked today are leading: you can see and change them every day, and they predict where the scale will go.",
                    "The scale lags. Today's steps and meals lead, and you can change them today.")
ll_analogy.box(30, 30, 300, 90, None, "green")
ll_analogy.head(180, 60, "leading: today", size=18)
ll_analogy.text(180, 92, "10,000 steps · no snacks", size=15)
ll_analogy.arrow(336, 75, 420, 75, label="predicts", lx=378, ly=61)
ll_analogy.box(426, 30, 300, 90, None, "blue")
ll_analogy.head(576, 60, "lagging: in 6 weeks", size=18)
ll_analogy.text(576, 92, "−3 kg · 5 km in 30 min", size=15)
ll_analogy.note(380, 180, "steer with the leading, judge with the lagging", "pen", size=18)

ll_how = Doodle(760, 330, "Grace's indicator chain for substitutions, from fast to slow. Daily leading indicators: percent of out-of-stock items where the customer was asked, and percent who answered within two minutes. Weekly: refund tickets from substitutions as a percent of orders, the outcome. Monthly lagging: repeat orders and the north star, perfect orders per week. Each leading indicator was checked against the lagging one with past data before being trusted.",
                 "Fast signals she can move every day, chained to the slow results that matter.")
chain = [("daily", "% asked", "leading", "green"), ("daily", "answer < 2 min", "leading", "green"),
         ("weekly", "swap refunds", "outcome", "y"), ("monthly", "repeat orders", "lagging", "blue")]
for i, (when, m, kind, f) in enumerate(chain):
    x = 14 + i * 186
    ll_how.note(x + 86, 30, when, "pen", size=17)
    ll_how.box(x, 44, 172, 80, m, f, sub=kind, size=15, subsize=13)
    if i < 3:
        ll_how.arrow(x + 174, 84, x + 184, 84)
ll_how.arrow(20, 170, 740, 170, label="fast → slow", lx=380, ly=160)
ll_how.box(120, 200, 520, 60, "checked first: do weeks with more “asked”", "paper", sub="have fewer refund tickets? (concierge data: yes)", size=15, subsize=13)
ll_how.note(380, 300, "steer weekly with green, judge quarterly with blue", "pen", size=17)

LEADING_LAGGING = dict(
    slug="leading-lagging",
    kicker="a.k.a. “today's steps, next month's scale”",
    tldr="<b>Lagging indicators</b> tell you whether you succeeded (refund tickets, repeat orders, revenue), but they arrive late and are hard to move directly. <b>Leading indicators</b> move quickly, are under the team's control, and <b>predict</b> the lagging ones (customers asked about a swap, answers within two minutes). Track both: <b>steer with the leading</b>, <b>judge with the lagging</b>, and check with data that the leading one really predicts the lagging one.",
    chips=[("Family", "measuring what matters"), ("Origin", "economics (leading economic indicators); Kaplan &amp; Norton's balanced scorecard (1992)"), ("Lives in", "the team dashboard: leading on top, lagging below"), ("Pairs with", "north star metric, baseline, OKRs (vol. 4)")],
    problem_side="Larder, waiting for the number",
    problem="""  <p class="lead">Grace's outcome is refund tickets from substitutions. But a ticket arrives one to seven days after the order, and the effect on repeat orders shows a <b>month later</b>. If she waits for those, weeks of work pass with <span class="hl-pink">no signal</span>. Meanwhile marketing reports app downloads every morning: they move fast, but they don't predict a single perfect order.</p>
  <ul>
    <li>Results arrive too late to steer by.</li>
    <li>Fast numbers are tempting even when they predict nothing.</li>
    <li>Teams can't tell this week whether their change is working.</li>
  </ul>""",
    problem_figs=[ll_problem],
    meanwhile=[("architect-1", "fitness-functions", "Ana checks the architecture on every merge; Grace checks the product every day with leading indicators.", "Grace's leading indicators do for the product what these checks do for the architecture: catch drift daily, not quarterly.")],
    analogy_side="getting fitter",
    analogy="""  <p>When you're getting fitter, the <b>scale</b> and your <b>race time</b> are lagging: they move slowly and tell you, weeks later, whether it worked. <b>Steps today</b> and <b>what you ate today</b> are leading: you can see them and change them every day, and they predict where the scale is going. You steer with the first and judge with the second.</p>""",
    analogy_figs=[ll_analogy],
    map=[("Weight on the scale in six weeks", "Repeat orders next month (lagging)"),
         ("Steps and meals today", "% of customers asked, % answered in 2 min (leading)"),
         ("A step counter that counts arm swings", "A leading indicator that doesn't predict: app downloads"),
         ("Checking steps really drop the weight", "Validating the leading indicator with past data"),
         ("Weekly weigh-in", "Weekly outcome review")],
    how_side="a chain from fast to slow",
    how="""  <p>Work backwards from the lagging result: what customer behaviour comes just before it? What does the team do that causes that behaviour? Each step is a candidate leading indicator. Keep only the ones that past data shows <b>actually predict</b> the next step in the chain.</p>""",
    how_figs=[ll_how],
    steps=[("Start from the lagging result", "The outcome or north star: refund tickets, repeat orders, perfect orders."),
           ("Work backwards", "What happens just before? (A customer is asked and answers in time.)"),
           ("Pick leading candidates", "Fast, frequent, and something the team's work can change."),
           ("Check they predict", "Past data or a test: do days with more “asked” have fewer tickets?"),
           ("Set targets for both", "Leading: weekly targets. Lagging: quarterly targets."),
           ("Review on two rhythms", "Leading in the weekly team review; lagging in the monthly or quarterly review.")],
    vocab=[("Lagging indicator", "Shows the result after the fact; slow to move."),
           ("Leading indicator", "Moves early and predicts the lagging one."),
           ("Predictive validity", "Evidence that the leading indicator really predicts the result."),
           ("Proxy metric", "A measurable stand-in for something harder to measure."),
           ("Signal delay", "Time between a change and its effect showing in the data."),
           ("Balanced scorecard", "A management framework mixing leading and lagging measures.")],
    code=dict(file="product/metrics/indicators.md", note="Grace's indicator pairs", plain=True, src="""
# Indicators · substitutions                              reviewed: weekly (Mon)

LEADING (daily, the team moves these)           now     target   source
  % out-of-stock items where customer was asked  0 %     ≥ 90 %   picker app events
  % of asked who answer within 2 min             –       ≥ 70 %   app / call log
  % swaps decided before packing                 –       ≥ 95 %   picker app

OUTCOME (weekly)
  swap refund tickets, % of orders               6.2 %   < 2 %    helpdesk (re-tagged)

LAGGING (monthly / quarterly)
  repeat orders within 30 days                   61 %    65 %     order data
  perfect orders / week (north star)             82 %    88 %     metrics/north-star.md

Predicts? Concierge test (Dec): orders where the customer was asked had 1.1 %
swap refund tickets vs 6.8 % at Zuid in the same weeks → keep “% asked”.
Dropped: app downloads (no relation to repeat orders, Jan–Sep 2025 data).
"""),
    tools="tools: the same dashboard as the north star, with leading indicators updated daily. Event data from the apps (Amplitude, Mixpanel, Snowplow) gives fast signals; tickets and orders give slower ones.",
    gains=["<b>Feedback in days</b>, not months.",
           "<b>Steerable</b>: the team can move leading indicators directly.",
           "<b>Honest judgement</b>: lagging results still decide success.",
           "<b>Vanity metrics exposed</b> when they don't predict.",
           "<b>Calmer reviews</b>: no panic over slow numbers that haven't caught up."],
    losses=["<b>Checking predictions takes data work.</b>",
            "<b>Leading indicators can be gamed</b> (ask customers about everything).",
            "<b>More numbers</b> to track and explain.",
            "<b>Predictions can break</b> when the product changes."],
    baseline="Each line compares <b>waiting for slow results (or watching fast vanity numbers)</b> to <b>a validated chain of leading indicators tied to lagging results, reviewed on two rhythms</b>.",
    ratings=[(3, 4, "Daily signals keep the team close to what customers experience."),
             (3, 4, "Leading indicators are chosen because they predict the result."),
             (2, 4, "Each indicator's predictive power is checked with data."),
             (2, 5, "Signals in days instead of a month."),
             (3, 4, "Vanity metrics drop off the dashboard."),
             (2, 4, "The team knows which daily number to push."),
             (3, 4, "Leaders see early progress before the slow numbers move."),
             (3, 4, "Fast feedback supports small, frequent changes."),
             (3, 3, "Some data work to set up and check.")],
    pitfalls=[("Leading but not predictive", "App downloads go up; nothing else does.", "check with data that it predicts the lagging result."),
              ("Gaming the leading number", "Pickers ask customers about every item to hit 90 %.", "pair it with a counter-metric: picking time, customer annoyance."),
              ("Only lagging", "The team waits a month to know anything.", "add at least one daily or weekly leading indicator."),
              ("Only leading", "Leading targets met; repeat orders flat.", "judge success on the lagging result.")],
    use=["Outcomes that arrive slowly (retention, revenue, refunds).",
         "Weekly team reviews that need something to steer by.",
         "Setting OKRs with key results the team can move.",
         "Exposing vanity metrics."],
    skip=["Results that are already fast and direct.",
          "When you haven't got a baseline: measure first.",
          "Tiny experiments with a single, immediate measure."],
    related=["<b>North star metric</b> (this volume)", "<b>Baseline before you build</b> (this volume)", "<b>Testable hypotheses</b> (this volume)", "<b>Fitness functions</b> (Ana, vol. 1)"],
    quiz=[("What's the difference between a leading and a lagging indicator?", "Lagging shows the result after the fact; leading moves early, is controllable, and predicts the result."),
          ("Name one of Grace's leading indicators.", "% of out-of-stock items where the customer was asked; % who answer within 2 minutes."),
          ("Why were app downloads dropped?", "Data showed they didn't predict repeat orders."),
          ("How do you check a leading indicator is useful?", "Use past data or a test to show it predicts the lagging result.")],
    try_it="Write your team's main outcome. List three things that happen before it, and pick one you can measure daily. Pull last quarter's data: do weeks with more of it have a better outcome? If not, keep looking.",
    remember="<span class=\"hl\">Steer</span> with today's steps. <span class=\"hl\">Judge</span> with next month's scale.",
    sources=["Robert Kaplan &amp; David Norton, “The Balanced Scorecard” (Harvard Business Review, 1992).",
             "Alistair Croll &amp; Benjamin Yoskovitz, <i>Lean Analytics</i> (2013).",
             "John Doerr, <i>Measure What Matters</i> (2018).",
             "Amplitude, <i>The North Star Playbook</i> (2019), inputs and leading indicators."],
)

# ------------------------------------------------------------------ 11 Baseline Before You Build
bl_problem = Doodle(760, 270, "Doodle of the famous six percent. It comes from support's 'substitution' tag, but agents pick the first tag in a dropdown. In a sample, many tickets tagged 'substitution' were about late orders, and many substitution problems were tagged 'missing item'. If Larder builds the fix now, it can't tell whether a change in the number is the fix or the tagging.",
                    "“6 %” came from a dropdown that agents fill in a hurry. Measure it wrong today and you can't prove anything tomorrow.")
bl_problem.box(20, 30, 220, 150, None, "paper")
bl_problem.head(130, 58, "ticket tag ▾", size=17)
for i, t in enumerate(["substitution", "missing item", "late", "other"]):
    bl_problem.text(40, 90 + i * 24, ("▸ " if i == 0 else "  ") + t, anchor="start", size=15)
bl_problem.note(130, 206, "first option wins", "red")
bl_problem.box(290, 30, 210, 70, "tagged “swap”", "pink", sub="but was late: 21 %", stroke="red", size=16, subsize=14)
bl_problem.box(290, 120, 210, 70, "tagged “missing”", "pink", sub="but was a swap: 17 %", stroke="red", size=16, subsize=14)
bl_problem.box(540, 60, 200, 100, "is it 6 %?", "y", sub="nobody knows", size=19, subsize=15)
bl_problem.note(380, 246, "build first, and the fix and the tagging get mixed up", "red")

bl_analogy = Doodle(760, 240, "Doodle of a bathroom scale before a diet. The old scale reads three kilograms light. If you start the diet without checking it, then buy a new scale halfway through, you can't tell whether you lost weight or changed scales. Check the scale and write down the starting weight first.",
                    "Weigh yourself on a scale you trust before the diet, not halfway through.")
bl_analogy.box(40, 50, 160, 140, None, "paper")
bl_analogy.raw('<path class="d d-thin" d="M80 100 a40 40 0 0 1 80 0"/><path class="d d-red" d="M120 100 L100 76"/>')
bl_analogy.note(120, 170, "reads 3 kg light", "red")
bl_analogy.arrow(210, 120, 290, 120)
bl_analogy.box(296, 70, 200, 100, "check it", "green", sub="against a known weight", size=17, subsize=14)
bl_analogy.arrow(502, 120, 560, 120)
bl_analogy.box(566, 70, 170, 100, "start: 84 kg", "blue", sub="written down", size=17, subsize=14)

bl_how = Doodle(760, 340, "How Grace and Sam set the baseline. They take a random sample of four hundred refund tickets from October and re-tag each by reading it, with a written rule for what counts as a substitution problem. Result: 6.2 percent of orders end in a substitution refund ticket: 7.4 percent of express orders and 3.5 percent of slots. The support tag was wrong in 38 percent of cases. The new tag rule goes into the helpdesk so future numbers are comparable.",
                 "A random sample, a written rule, read by hand: the baseline everyone can trust.")
bl_how.box(14, 20, 200, 90, "400 tickets", "paper", sub="random, October", size=18, subsize=14)
bl_how.arrow(220, 65, 270, 65)
bl_how.box(276, 20, 220, 90, "re-tag by reading", "y", sub="one written rule", size=16, subsize=14)
bl_how.arrow(502, 65, 552, 65)
bl_how.box(558, 20, 188, 90, "6.2 %", "green", sub="of orders", size=24, subsize=14)
for i, (lbl, v, w) in enumerate([("express", "7.4 %", 296), ("slots", "3.5 %", 140), ("tag was wrong", "38 %", 228)]):
    y = 150 + i * 48
    bl_how.text(14, y + 24, lbl, "t-head", anchor="start", size=15)
    bl_how.box(170, y, w, 34, None, "pink" if i == 2 else "blue", rx=4)
    bl_how.text(180 + w, y + 24, v, anchor="start", size=15)
bl_how.note(380, 318, "the rule goes into the helpdesk, so next month compares fairly", "pen", size=17)

BASELINE = dict(
    slug="baseline",
    kicker="a.k.a. “check the scale before the diet”",
    tldr="Before you change anything, <b>measure today properly</b>: how the number is defined, where it comes from, how reliable that source is, and what it is for each important segment. Fix the measurement first if you have to. Without a trustworthy <b>baseline</b> you can't tell whether a change worked, and every later argument becomes a fight about the data instead of the result.",
    chips=[("Family", "measuring what matters"), ("Origin", "experiment design and evaluation practice; “measure before you manage”"), ("Lives in", "a baseline card per outcome, next to the problem statement"), ("Pairs with", "north star metric, leading vs lagging, A/B tests (vol. 4)")],
    problem_side="Larder, the famous 6 %",
    problem="""  <p class="lead">Everyone at Larder quotes <b>“6 % of orders end in a refund ticket”</b>. Grace asks where it comes from: support's “substitution” tag. But agents pick tags from a dropdown, in a hurry, and the first option wins. In a quick look, some “substitution” tickets are about late orders, and some swap problems are tagged “missing item”. If the team builds the fix now, it <span class="hl-pink">can't tell</span> whether a change in the number comes from the fix or from the tagging.</p>
  <ul>
    <li>Numbers everyone quotes are often the least checked.</li>
    <li>A measurement that changes mid-project ruins the comparison.</li>
    <li>Averages hide differences between segments (express vs slots).</li>
  </ul>""",
    problem_figs=[bl_problem],
    meanwhile=[("architect-1", "nfr-checklist", "Ana's NFR checklist asks what's measured before go-live; Grace measures the product baseline before building.", "Grace does the product version before building anything: 400 tickets re-tagged by hand for a baseline she can trust.")],
    analogy_side="the bathroom scale",
    analogy="""  <p>Starting a diet on an old scale that reads <b>three kilos light</b>, then buying a new one halfway through, you'll never know whether you lost weight or changed scales. Check the scale against a known weight, <b>write the starting number down</b>, and keep the same scale until the end.</p>""",
    analogy_figs=[bl_analogy],
    map=[("The old scale", "The support tag dropdown"),
         ("Checking it against a known weight", "Re-tagging 400 tickets by reading them"),
         ("Writing down the starting weight", "The baseline card: 6.2 %, by segment"),
         ("Keeping the same scale", "The tag rule fixed in the helpdesk"),
         ("Weight per body part (sort of)", "Segments: express 7.4 %, slots 3.5 %")],
    how_side="define, check, sample, fix the source",
    how="""  <p>Write the <b>definition</b> first, then check the <b>source</b> against reality with a sample you read by hand. If the source is unreliable, fix it <b>before</b> the change, so before and after use the same ruler. Split by the segments the change might affect differently.</p>""",
    how_figs=[bl_how],
    steps=[("Define the number", "What counts, what doesn't, over which period: “a refund ticket within 7 days caused by a substitution”."),
           ("Find the source", "Where it comes from today, and how it's produced (a dropdown chosen in a hurry)."),
           ("Check a random sample by hand", "Read 200–400 cases with a written rule; measure how often the source is wrong."),
           ("Split by segment", "Express vs slots, stores, new vs returning: the fix may affect them differently."),
           ("Fix the measurement first", "Change the tag rule or tracking before the product change, then wait a few weeks."),
           ("Write the baseline card", "Number, definition, method, date, error margin, owner. Everyone quotes the card.")],
    vocab=[("Baseline", "The measured value before a change, used for comparison."),
           ("Operational definition", "An exact, repeatable rule for what counts."),
           ("Random sample", "Cases picked by chance, so they represent the whole."),
           ("Measurement error", "How far the source differs from reality."),
           ("Segment", "A group that may behave differently (express vs slots)."),
           ("Before/after comparison", "Comparing the baseline to the number after a change.")],
    code=dict(file="product/metrics/baseline-swap-refunds.md", note="baseline card, 26 Nov 2025", plain=True, src="""
# Baseline: substitution refund tickets                     owner: Grace · checked: Sam

Definition  A refund or complaint ticket within 7 days of delivery whose main
            cause is a substituted item (wrong swap, unsafe swap, swap not wanted).
Period      1–31 Oct 2025 · 124,000 orders
Method      Random sample of 400 refund tickets, re-tagged by reading each one
            (rule above; Grace and Sam, disagreements resolved together)

Result      6.2 % of orders  (± 0.5 pt)
  express   7.4 %
  slots     3.5 %
  Noord     6.5 %   Zuid 5.9 %
Source      Helpdesk tag was wrong in 38 % of sampled tickets
            (21 % tagged “substitution” were late orders; 17 % of swaps were “missing item”)

Fix         New tag rule + “substitution” split into three tags, live 1 Dec.
            Compare from 15 Dec onward; re-check 100 tickets monthly.
"""),
    tools="tools: a spreadsheet and two people reading tickets for a day. Your helpdesk's export, a random-number column, and a written rule are enough. Later, the product analytics tool keeps the number current.",
    gains=["<b>Results you can prove</b>: before and after use the same ruler.",
           "<b>Better targets</b>: express needs more help than slots.",
           "<b>Fewer data fights</b>: everyone quotes the same card.",
           "<b>A cleaner source</b> for every future measurement.",
           "<b>Surprises early</b>: the tag was wrong 38 % of the time."],
    losses=["<b>Delay</b>: weeks before the product change starts.",
            "<b>Tedious work</b>: reading tickets by hand.",
            "<b>Error margins</b> remain, even after sampling.",
            "<b>Awkward</b> when the “famous number” turns out wrong."],
    baseline="Each line compares <b>quoting an unchecked number and building straight away</b> to <b>a defined, sampled, segmented baseline with the measurement fixed before the change</b>.",
    ratings=[(3, 3, "Neutral by itself; it makes later fixes provable."),
             (2, 4, "Shows where the cost really is (express)."),
             (1, 5, "The number is checked by hand against reality."),
             (2, 3, "Slows the start, speeds every later conclusion."),
             (2, 4, "Segments show where to focus first."),
             (2, 4, "Everyone quotes the same card and definition."),
             (2, 5, "Leaders can trust before/after claims."),
             (3, 3, "Neutral."),
             (3, 2, "A day or two of careful, manual work.")],
    pitfalls=[("Trusting the famous number", "Everyone quotes 6 %; nobody knows how it's made.", "trace the source and check a sample by hand."),
              ("Changing the ruler mid-way", "New tags arrive in the same week as the fix.", "fix the measurement first, wait, then change the product."),
              ("Averages only", "One number for all orders.", "split by the segments the change will affect."),
              ("No definition", "Two analysts get two different baselines.", "write an exact rule anyone can apply.")],
    use=["Before any change you'll want to claim credit for.",
         "When a number comes from manual tagging or surveys.",
         "When segments might react differently.",
         "Setting targets for a new outcome."],
    skip=["Tiny reversible tweaks where a quick A/B test is enough.",
          "When the source is already audited and stable.",
          "Emergencies: fix first, measure the next one properly."],
    related=["<b>North star metric</b> (this volume)", "<b>Leading vs lagging indicators</b> (this volume)", "<b>Testable hypotheses</b> (this volume)", "<b>NFR checklist</b> (Ana, vol. 1)"],
    quiz=[("Why fix the measurement before the product change?", "So before and after use the same ruler; otherwise you can't tell the fix from the tagging."),
          ("How did Grace check the 6 %?", "A random sample of 400 tickets re-tagged by hand with a written rule."),
          ("What did the baseline show by segment?", "Express 7.4 %, slots 3.5 %: express needs the fix most."),
          ("What goes on a baseline card?", "Definition, period, method, result with error margin, segments, source quality, owner.")],
    try_it="Pick the number your team quotes most. Write its exact definition, then check 50 random cases by hand. How often does the source agree with what you read? Write a baseline card and share it.",
    remember="Check the <span class=\"hl\">scale</span>, write down the <span class=\"hl\">start</span>, then begin the diet.",
    sources=["Ron Kohavi, Diane Tang &amp; Ya Xu, <i>Trustworthy Online Controlled Experiments</i> (2020).",
             "Douglas Hubbard, <i>How to Measure Anything</i>, 3rd ed. (2014).",
             "Alistair Croll &amp; Benjamin Yoskovitz, <i>Lean Analytics</i> (2013).",
             "Caroline Criado Perez, <i>Invisible Women</i> (2019), on what averages hide."],
)

NOTES = [NORTH_STAR, LEADING_LAGGING, BASELINE]
