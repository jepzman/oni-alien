# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 4 · Instrumenting.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Event Tracking Plan
tp_problem = Doodle(760, 280, "Doodle of May 2026's first look at approvals data. iOS sends swap_answered, Android sends SwapAnswer with different properties, the web shop sends nothing. Three dashboards give three different answer rates: 71, 79 and 84 percent. Nobody can say which is right.",
                    "Three platforms, three event names, three answer rates: 71 %, 79 %, 84 %. Which is right?")
for i, (plat, ev, f) in enumerate([("iOS", "swap_answered", "blue"), ("Android", "SwapAnswer", "y"), ("web", "(nothing)", "pink")]):
    tp_problem.box(20 + i * 250, 30, 220, 80, plat, f, sub=ev)
for i, r in enumerate(["71 %", "79 %", "84 %"]):
    tp_problem.box(80 + i * 250, 150, 100, 50, r, "paper", size=18)
tp_problem.note(380, 254, "three dashboards, three truths", "red")

tp_analogy = Doodle(760, 250, "Doodle of a football club's match statistics sheet. Before the season, the analysts agree exactly what counts as a shot, a pass and a tackle, and who records each. Without that, two analysts watching the same match produce different numbers.",
                     "Match statistics only agree if everyone counts a “shot” the same way, decided before the season.")
tp_analogy.icon("ledger", 40, 50, 1.5)
for i, (t, s, f) in enumerate([("shot", "on or off target", "y"), ("pass", "completed or not", "blue"), ("tackle", "won or lost", "green")]):
    tp_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, subsize=14)
tp_analogy.note(450, 210, "agreed before the season, not after", "pen")

tp_how = Doodle(760, 360, "Grace's tracking plan for approvals, 4 May 2026. One row per event: name in object_action form, when it fires, its properties, and who owns it. swap_offered when a picker sends a substitute; swap_seen when the card or banner is shown; swap_answered with answer and seconds; swap_applied at packing. Same names and properties on iOS, Android and web. Reviewed in every story's definition of done.",
                 "One table: event name, when it fires, properties, owner. Same names on every platform, checked in the definition of done.")
tp_how.head(20, 32, "event", anchor="start", size=15)
tp_how.head(220, 32, "fires when", anchor="start", size=15)
tp_how.head(470, 32, "properties", anchor="start", size=15)
for i, (e, w, p) in enumerate([("swap_offered", "picker sends a swap", "order, item, substitute, price diff"), ("swap_seen", "card or banner shown", "channel: push / banner / in-app"),
                               ("swap_answered", "customer taps", "answer, seconds, platform"), ("swap_applied", "at packing", "answer or default, picker")]):
    y = 50 + i * 54
    tp_how.box(12, y, 736, 44, None, ["blue", "paper"][i % 2], rx=4)
    tp_how.text(20, y + 28, e, "t-head", anchor="start", size=14)
    tp_how.text(220, y + 28, w, anchor="start", size=14)
    tp_how.text(470, y + 28, p, anchor="start", size=13)
tp_how.note(380, 296, "same names and properties on iOS, Android and web", "green", size=16)
tp_how.note(380, 324, "owner: Dee · checked in the definition of done", "pen", size=16)

TRACKING = dict(
    slug="event-tracking-plan",
    kicker="a.k.a. “what counts as a shot”",
    tldr="Product numbers are only as good as the events behind them. Before (or as) you build, write a <b>tracking plan</b>: one row per event, with a <b>consistent name</b> (object_action), <b>exactly when it fires</b>, its <b>properties</b>, and an <b>owner</b>. Use the <b>same names on every platform</b>, check the events in the <b>definition of done</b>, and change the plan through review. Three dashboards with three answers usually means no plan.",
    chips=[("Family", "instrumenting"), ("Origin", "product analytics practice (Segment, Amplitude and Mixpanel tracking plans)"), ("Lives in", "a table in the repo, next to the code that fires the events"), ("Pairs with", "funnels, definition of done, dashboards")],
    problem_side="Larder, 4 May 2026",
    problem="""  <p class="lead">Approvals has been live in Amsterdam for three weeks. Grace asks a simple question: <i>what share of customers answer within two minutes?</i> <b>iOS</b> sends <code>swap_answered</code>, <b>Android</b> sends <code>SwapAnswer</code> with different properties, the <b>web shop</b> sends nothing. Three dashboards give <span class="hl-pink">three answer rates: 71, 79 and 84 %</span>. Nobody can say which is right.</p>
  <ul>
    <li>Each platform names and shapes events its own way.</li>
    <li>“When does it fire?” is decided by whoever writes the code.</li>
    <li>Numbers disagree, so nobody trusts any of them.</li>
  </ul>""",
    problem_figs=[tp_problem],
    analogy_side="match statistics",
    analogy="""  <p>A football club's analysts agree, <b>before the season</b>, exactly what counts as a <b>shot</b> (on or off target), a <b>pass</b> (completed or not), a <b>tackle</b> (won or lost), and who records each. Without that, two analysts watching the same match produce different numbers, and the coach stops reading the sheet.</p>""",
    analogy_figs=[tp_analogy],
    map=[("What counts as a shot", "Exactly when swap_answered fires"),
         ("The statistics sheet", "The tracking plan"),
         ("The same definitions for every analyst", "Same names and properties on iOS, Android, web"),
         ("Agreed before the season", "Written before the story is built"),
         ("Who records what", "An owner per event")],
    how_side="one table, the same everywhere",
    how="""  <p>Grace and Dee wrote the tracking plan for approvals in an afternoon: <b>four events</b> following the swap from offered to applied, each with <b>when it fires</b> and its <b>properties</b>. All three platforms were fixed to the same names in a week; the definition of done now includes “tracking events firing as in the plan”. The real answer rate in May: <b>77 %</b>.</p>""",
    how_figs=[tp_how],
    steps=[("Start from the questions", "What do you need to know? Work back to the events that answer it."),
           ("Name events consistently", "object_action, lower case: <code>swap_answered</code>."),
           ("Say exactly when each fires", "“When the customer taps yes or no”, not “on answer”."),
           ("List the properties", "With types and allowed values: answer = yes / no."),
           ("Give each event an owner", "Usually the team that builds the feature."),
           ("Check it in the definition of done", "And change the plan by review, like code.")],
    vocab=[("Tracking plan", "The agreed list of events, when they fire, and their properties."),
           ("Event", "A record that a user or system did something."),
           ("Property", "A detail attached to an event (answer, seconds)."),
           ("object_action", "A naming style: thing, then what happened to it."),
           ("Instrumentation", "The code that sends events."),
           ("Data quality", "How complete and correct the events are.")],
    code=dict(file="product/tracking/approvals.md", note="the approvals tracking plan, 4 May 2026", plain=True, src="""
# Tracking plan · approvals                     owner: Dee · reviewed in the definition of done

| Event          | Fires when                                  | Properties                                  |
|----------------|---------------------------------------------|---------------------------------------------|
| swap_offered   | the picker sends a substitute (handheld)    | order_id, item_id, substitute_id,           |
|                |                                             | price_diff_cents, store_id                  |
| swap_seen      | the swap card or banner is shown            | order_id, channel: push | banner | in_app   |
| swap_answered  | the customer taps yes or no                 | order_id, answer: yes | no, seconds,        |
|                |                                             | platform: ios | android | web               |
| swap_applied   | the picker packs with the answer            | order_id, outcome: yes | no | default       |

Rules  same names and properties on every platform · snake_case · no PII in properties
Fixed  Android SwapAnswer → swap_answered (11 May) · web added (14 May) · May answer rate: 77 %
"""),
    tools="tools: a table in the repo or a tracking-plan tool (Avo, Segment Protocols, Amplitude Data); schema validation on incoming events; product analytics (Amplitude, Mixpanel, PostHog) or your warehouse.",
    gains=["<b>One answer</b> instead of three.",
           "<b>Trust</b> in product numbers.",
           "<b>Faster questions</b>: events already exist.",
           "<b>Same events everywhere</b>, so platforms compare.",
           "<b>No personal data</b> leaking into analytics."],
    losses=["<b>Upfront work</b> per feature.",
            "<b>Discipline</b>: plans drift without review.",
            "<b>Old events</b> need fixing or retiring.",
            "<b>Can over-track</b> if every click gets an event."],
    baseline="Each line compares <b>events named and fired however each platform's engineer chose</b> to <b>a tracking plan with consistent names, firing rules, properties and owners, checked in the definition of done</b>.",
    ratings=[(3, 3, "Indirect: better decisions about customers."),
             (2, 4, "Numbers the business can trust."),
             (1, 5, "One answer rate, with a definition."),
             (2, 4, "Questions answered from existing events."),
             (3, 4, "Only the events that answer real questions."),
             (2, 5, "Everyone knows what each number means."),
             (2, 4, "Leaders stop questioning the numbers."),
             (3, 3, "Neutral."),
             (3, 3, "An afternoon per feature, plus reviews.")],
    pitfalls=[("Tracking everything", "An event per click, nobody reads them.", "start from the questions; track what answers them."),
              ("Vague firing rules", "“On answer.”", "say exactly when: “when the customer taps yes or no”."),
              ("Platform drift", "iOS and Android diverge again.", "check events in the definition of done."),
              ("Personal data in properties", "Names and addresses in analytics.", "IDs only; check with your DPO.")],
    use=["Every feature you want to measure.",
         "When dashboards disagree.",
         "Multi-platform products.",
         "Before an A/B test."],
    skip=["Prototypes and fake doors: count simply and throw away."],
    related=["<b>Funnels</b> (this volume)", "<b>Dashboards that get used</b> (this volume)", "<b>Definition of ready &amp; done</b> (Vol. 3)", "<b>Baseline before you build</b> (Vol. 1)"],
    quiz=[("What's in each row of a tracking plan?", "Event name, exactly when it fires, its properties, and an owner."),
          ("Why the same names on every platform?", "So numbers can be combined and compared."),
          ("Where are events checked?", "In the definition of done."),
          ("What was Larder's real answer rate in May?", "77 %, once all platforms sent the same events.")],
    try_it="Pick one feature and one question about it. Write the events that answer it as a four-column table (name, fires when, properties, owner). Check what your three platforms actually send today and list the differences.",
    remember="Agree what counts as a <span class=\"hl\">shot</span> before the season. Same <span class=\"hl\">names</span> everywhere.",
    sources=["Segment, “The Data Tracking Plan” guide (segment.com/academy).",
             "Amplitude, “Data Taxonomy Playbook”.",
             "Alistair Croll and Benjamin Yoskovitz, <i>Lean Analytics</i> (2013).",
             "Avo, “Tracking plan best practices”."],
)

# ------------------------------------------------------------------ 02 Funnels
fn_problem = Doodle(760, 280, "Doodle of May 2026: 77 percent of swaps are answered within two minutes. Grace wants more, and the team has three guesses why the rest don't answer: the countdown is too short, people don't trust the price, the screen is confusing. Nobody knows where customers actually drop out.",
                    "77 % answer. Three guesses about the other 23 %, and no idea where they drop out.")
fn_problem.box(20, 40, 260, 90, "answered ≤ 2 min", "green", sub="77 %")
for i, t in enumerate(["“timer too short”", "“price scares them”", "“confusing screen”"]):
    fn_problem.box(330, 20 + i * 66, 410, 52, t, "paper", size=15)
fn_problem.note(380, 250, "where do they actually drop out?", "red")

fn_analogy = Doodle(760, 250, "Doodle of a theme park queue for a ride: people join the queue, some leave at the first turn, some at the height check, some at the ticket scanner. Counting at each step shows the height check loses the most, so that's where to put a sign.",
                     "A ride queue: count people at every step, and the biggest drop shows where to put the sign.")
for i, (t, n, w) in enumerate([("join the queue", "100", 560), ("first turn", "92", 500), ("height check", "70", 380), ("on the ride", "68", 360)]):
    fn_analogy.box(380 - w / 2, 20 + i * 52, w, 42, f"{t} · {n}", "pink" if i == 2 else "y", size=15)
fn_analogy.note(380, 234, "the biggest drop: put the sign there", "pen")

fn_how = Doodle(760, 360, "The approvals funnel, Amsterdam, May 2026. Swap offered: 100. Seen, by push, banner or in-app: 88. Card opened: 82. Answered within two minutes: 77. Applied at packing as answered: 76. The biggest drop is between seen and opened on Android: 71 percent there against 96 percent on iOS. Cause: Android grouped Larder's notifications so the swap was hidden. Fixed on 1 June; answers rose to 82 percent.",
                 "Count every step. The biggest drop (Android, seen → opened) was a notification bug, not the timer.")
steps = [("offered", 100), ("seen", 88), ("opened", 82), ("answered ≤ 2 min", 77), ("applied", 76)]
for i, (t, n) in enumerate(steps):
    w = n * 5
    fn_how.box(14, 20 + i * 50, w, 40, None, "pink" if i == 2 else "green", rx=4)
    fn_how.text(24, 46 + i * 50, f"{t} · {n}", "t-head", anchor="start", size=14)
fn_how.box(560, 20, 186, 100, "seen → opened", "paper", size=14, sub=" ")
fn_how.text(653, 84, "iOS 96 %", size=14)
fn_how.text(653, 106, "Android 71 %", "t t-red", size=14)
fn_how.note(380, 296, "Android grouped our notifications: the swap was hidden", "red", size=16)
fn_how.note(380, 326, "fixed 1 June → answered ≤ 2 min: 77 % → 82 %", "green", size=17)

FUNNELS = dict(
    slug="funnels",
    kicker="a.k.a. “the ride queue”",
    tldr="A single rate (“77 % answer”) tells you how much, not <b>where</b> people drop out. A <b>funnel</b> counts users at <b>every step</b> of a journey, in order, so the <b>biggest drop</b> shows itself. Split each step by segment (platform, city, new vs returning) to find the cause. Fix the biggest drop first, with the same funnel as your measure. Guesses about “why” come after you know “where”.",
    chips=[("Family", "instrumenting"), ("Origin", "conversion funnels in marketing and web analytics; AARRR (Dave McClure, 2007)"), ("Lives in", "the analytics tool, built on the tracking plan's events"), ("Pairs with", "event tracking plan, customer journey map, A/B tests")],
    problem_side="Larder, 18 May 2026",
    problem="""  <p class="lead">With consistent events, approvals' answer rate is <b>77 %</b>. Grace wants more, and the team has three theories about the other 23 %: the <b>countdown is too short</b>, people <b>don't trust the price</b>, the screen is <b>confusing</b>. Each theory has a fan. <span class="hl-pink">Nobody knows where customers actually drop out</span>, so any fix is a guess.</p>
  <ul>
    <li>One rate hides which step loses people.</li>
    <li>Teams fix the step they have a theory about, not the one that's broken.</li>
    <li>Averages hide segments where it's much worse.</li>
  </ul>""",
    problem_figs=[fn_problem],
    analogy_side="the ride queue",
    analogy="""  <p>A theme park counts people at each step of a ride's queue: <b>join</b>, <b>first turn</b>, <b>height check</b>, <b>on the ride</b>. Most leave at the height check: so that's where to put a sign at the entrance (“120 cm minimum”), not a faster ride. The count shows <b>where</b>; then you ask why.</p>""",
    analogy_figs=[fn_analogy],
    map=[("Joining the queue", "swap_offered"),
         ("The first turn", "swap_seen"),
         ("The height check", "Card opened: the biggest drop"),
         ("On the ride", "Answered within 2 minutes"),
         ("A sign at the entrance", "The Android notification fix")],
    how_side="count every step, split by segment",
    how="""  <p>Grace built the funnel from the four tracking-plan events: <b>offered 100 → seen 88 → opened 82 → answered 77 → applied 76</b>. The biggest drop was <b>seen → opened</b>, and split by platform it was almost all <b>Android</b> (71 % against iOS's 96 %). Dee found Android was <b>grouping Larder's notifications</b>, hiding the swap under an order update. Fixed on 1 June: answers rose to <b>82 %</b>. None of the three theories had been the problem.</p>""",
    how_figs=[fn_how],
    steps=[("Write the journey's steps", "In order, each matching an event from the tracking plan."),
           ("Count users at each step", "For a fixed period and population."),
           ("Find the biggest drop", "In absolute numbers, not just percentages."),
           ("Split that step by segment", "Platform, city, new vs returning, time of day."),
           ("Then ask why", "Interviews, recordings, logs, for that step and segment."),
           ("Fix and re-measure", "Same funnel, same period length.")],
    vocab=[("Funnel", "Users counted at each step of a journey, in order."),
           ("Conversion rate", "The share moving from one step to the next."),
           ("Drop-off", "Users lost between two steps."),
           ("Segment", "A subgroup: platform, city, customer type."),
           ("Step", "One event in the journey."),
           ("AARRR", "Acquisition, Activation, Retention, Referral, Revenue: a growth funnel.")],
    code=dict(file="product/analytics/approvals-funnel.md", note="the approvals funnel, Amsterdam, May 2026", plain=True, src="""
# Approvals funnel · Amsterdam express · 1–31 May 2026            from the tracking plan

Step                    all     iOS     Android   web
swap_offered            100 %   100 %   100 %     100 %
swap_seen                88 %    94 %    86 %      79 %   (web: banner only)
card opened              82 %    90 %    61 %  ←   74 %   biggest drop: Android
answered ≤ 2 min         77 %    86 %    56 %      70 %
swap_applied as answered 76 %    85 %    55 %      69 %

Cause (Dee, 27 May): Android grouped Larder notifications; the swap sat under an
order update. Fix: separate notification channel for swaps, high priority (1 Jun).
June: answered ≤ 2 min 82 % (Android 78 %).
"""),
    tools="tools: product analytics funnels (Amplitude, Mixpanel, PostHog) or SQL on the event warehouse; session recordings (with consent) to understand a drop.",
    gains=["<b>Where, before why</b>: no more guessing.",
           "<b>Segments reveal causes</b> (Android).",
           "<b>The right fix first</b>.",
           "<b>Measurable improvement</b>, same funnel.",
           "<b>Theories tested cheaply</b> against data."],
    losses=["<b>Needs good events</b> first.",
            "<b>Funnels miss loops</b> and non-linear journeys.",
            "<b>Segment fishing</b> can find noise.",
            "<b>“Why” still needs</b> research."],
    baseline="Each line compares <b>one overall rate and competing theories</b> to <b>a step-by-step funnel, split by segment, fixing the biggest drop first</b>.",
    ratings=[(2, 4, "Android customers stopped missing swaps."),
             (2, 4, "Answers 77 % → 82 %, fewer refunds."),
             (2, 5, "The drop was found in data, not argued."),
             (2, 4, "Cause found in days."),
             (2, 4, "One step, one fix."),
             (2, 4, "Everyone sees where customers drop out."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Built once from existing events.")],
    pitfalls=[("Percentages only", "A 50 % drop of 10 users.", "look at absolute numbers too."),
              ("Fixing the favourite theory", "A longer timer, without data.", "find the biggest drop first."),
              ("No segments", "The average hides Android.", "split the worst step by platform, city, type."),
              ("Segment fishing", "Ten splits until one looks interesting.", "split the worst step; confirm with a second period.")],
    use=["Any multi-step journey: checkout, onboarding, approvals.",
         "When a rate is lower than expected.",
         "Before choosing which step to improve.",
         "After a launch."],
    skip=["Single-step actions.",
          "Journeys with no events yet: write the tracking plan first."],
    related=["<b>Event tracking plan</b> (this volume)", "<b>Customer journey map</b> (Vol. 1)", "<b>A/B tests</b> (this volume)", "<b>Cohorts &amp; retention curves</b> (this volume)"],
    quiz=[("What does a funnel show that a single rate doesn't?", "Where people drop out, step by step."),
          ("What should you do with the biggest drop?", "Split it by segment, then investigate why."),
          ("What was Larder's biggest drop?", "Seen → opened on Android: notifications were grouped and the swap hidden."),
          ("What did the fix achieve?", "Answers within two minutes rose from 77 % to 82 %.")],
    try_it="Pick a journey with a disappointing rate. List its steps, count users at each for last month, and split the biggest drop by platform. Before discussing any fix, write down which step and which segment lose the most people.",
    remember="Count at every <span class=\"hl\">turn</span> of the queue. Fix the biggest <span class=\"hl\">drop</span> first.",
    sources=["Alistair Croll and Benjamin Yoskovitz, <i>Lean Analytics</i> (2013).",
             "Dave McClure, “Startup Metrics for Pirates: AARRR!” (2007).",
             "Amplitude, “Funnel Analysis” documentation.",
             "Avinash Kaushik, <i>Web Analytics 2.0</i> (2009)."],
)

# ------------------------------------------------------------------ 03 Cohorts & Retention Curves
co_problem = Doodle(760, 280, "Doodle of June 2026. Femke asks: do approvals actually keep customers? The monthly active customers line is going up, but it mixes new customers from Rotterdam with old ones. One total line can't say whether people who had a good swap come back more.",
                    "“Do approvals keep customers?” One growing total line can't answer it.")
co_problem.line("M40 220 L120 200 L200 190 L280 160 L360 150 L440 120 L520 100 L600 80 L700 60", color="green")
co_problem.line("M40 230 H720")
co_problem.note(560, 140, "monthly active customers ↑", "green", size=17)
co_problem.box(30, 30, 330, 70, "Femke", "y", sub="“do approvals keep customers?”", subsize=15)
co_problem.note(380, 264, "new Rotterdam customers hide everything", "red")

co_analogy = Doodle(760, 250, "Doodle of a gym tracking members by the month they joined: of January's joiners, how many still come in February, March, April? Of March's joiners after the new induction class, how many? Comparing those lines shows whether the induction helps, which total visitor numbers never could.",
                     "A gym compares members by the month they joined: did the new induction class keep more of them?")
co_analogy.icon("stopwatch", 40, 60, 1.3)
co_analogy.line("M180 60 L300 110 L420 140 L540 155 L700 165", color="red")
co_analogy.line("M180 60 L300 90 L420 110 L540 118 L700 122", color="green")
co_analogy.note(600, 100, "after induction", "green", size=16)
co_analogy.note(600, 190, "before", "red", size=16)

co_how = Doodle(760, 360, "Grace's retention curves, July 2026: share of customers ordering again, by weeks since their first swap of the spring. Three cohorts: customers whose swap ended in a refund ticket, customers with an approved swap, and customers with no swap. After eight weeks: refund ticket 58 percent, approved swap 71 percent, no swap 69 percent. A good swap doesn't just avoid harm; customers come back like those who never had one.",
                 "Retention by cohort: after a refund ticket 58 % come back; after an approved swap, 71 %, like customers with no swap.")
co_how.line("M60 300 H720")
co_how.line("M60 300 V30")
co_how.text(390, 346, "weeks since first swap →", "t t-soft", size=14)
for i in range(5):
    co_how.text(60 + i * 160, 320, str(i * 2), "t t-soft", size=13)
co_how.line("M60 50 L220 160 L380 190 L540 200 L700 206", color="red")
co_how.line("M60 50 L220 110 L380 130 L540 136 L700 138", color="green")
co_how.line("M60 50 L220 114 L380 136 L540 142 L700 144", color="pen", dash=True)
co_how.note(712, 232, "refund ticket 58 %", "red", anchor="end", size=15)
co_how.note(712, 124, "approved swap 71 %", "green", anchor="end", size=15)
co_how.note(712, 166, "no swap 69 %", "pen", anchor="end", size=15)

COHORTS = dict(
    slug="cohorts-retention",
    kicker="a.k.a. “members by the month they joined”",
    tldr="Totals mix everyone together: new customers can hide lost ones. A <b>cohort</b> is a group that shares a starting point (joined in March, had a refund ticket, had an approved swap). A <b>retention curve</b> shows what share of a cohort is still active over time. Compare cohorts to see whether something <b>changes behaviour</b>: does a good experience bring customers back? Use them for questions about keeping customers, which totals can't answer.",
    chips=[("Family", "instrumenting"), ("Origin", "cohort analysis in epidemiology and marketing; SaaS retention practice"), ("Lives in", "the analytics tool or a warehouse query, reviewed monthly"), ("Pairs with", "funnels, north star metric, post-launch review")],
    problem_side="Larder, 6 July 2026",
    problem="""  <p class="lead">Femke asks the question behind the business case: <i>do approvals actually keep customers?</i> The <b>monthly active customers</b> line is going up, but it mixes in thousands of new <b>Rotterdam</b> customers. Vol. 1 found that customers with two refund tickets order 30 % less; nobody knows yet whether a good swap undoes the damage. <span class="hl-pink">One total line can't say.</span></p>
  <ul>
    <li>Growth from new customers hides whether existing ones stay.</li>
    <li>Averages over time blur the effect of a change.</li>
    <li>“Keeps customers” needs comparing similar groups over time.</li>
  </ul>""",
    problem_figs=[co_problem],
    analogy_side="the gym's members",
    analogy="""  <p>A gym tracks members <b>by the month they joined</b>: of January's joiners, how many still come in February, March, April? Then it compares with March's joiners, who had the new <b>induction class</b>. If March's line stays higher, the induction works. The total number of visitors could never show that; new joiners would hide it.</p>""",
    analogy_figs=[co_analogy],
    map=[("Members by joining month", "Customers grouped by what happened in their first swap"),
         ("Still coming in week by week", "Ordering again, week by week"),
         ("The induction class", "An approved swap"),
         ("January's joiners", "Customers whose swap ended in a refund ticket"),
         ("Total visitors", "Monthly active customers: misleading here")],
    how_side="compare similar groups over time",
    how="""  <p>Grace grouped spring's customers by their <b>first swap</b>: ended in a <b>refund ticket</b>, an <b>approved swap</b>, or <b>no swap</b> at all. After eight weeks, <b>58 %</b> of the refund-ticket cohort were still ordering, against <b>71 %</b> for approved swaps and <b>69 %</b> for no swap. A good swap doesn't just avoid harm: customers come back like those who never needed one. Femke took the chart to the board.</p>""",
    how_figs=[co_how],
    steps=[("Define the starting event", "What puts someone in the cohort: first order, first swap, joined month."),
           ("Define “still active”", "Ordered again in the week? In the month?"),
           ("Build the curve", "Share active at each period since the start."),
           ("Compare cohorts", "Before and after a change; with and without an experience."),
           ("Check they're comparable", "Similar customers? Same season? Watch for selection effects."),
           ("Review monthly", "New cohorts show whether a change is working.")],
    vocab=[("Cohort", "A group sharing a starting event or period."),
           ("Retention", "The share of a cohort still active after some time."),
           ("Retention curve", "Retention plotted over time since the start."),
           ("Churn", "Customers who stop being active."),
           ("Selection effect", "Cohorts differing for reasons other than the thing studied."),
           ("Monthly active customers", "A total that mixes all cohorts.")],
    code=dict(file="product/analytics/retention-by-first-swap.md", note="retention by first swap, spring 2026", plain=True, src="""
# Retention by first swap · customers with a first swap 13 Apr – 31 May 2026
"Active" = ordered at least once in the week

Cohort (by first swap)          size     wk 2    wk 4    wk 6    wk 8
Swap ended in a refund ticket    1,940   74 %    65 %    61 %    58 %
Approved swap (yes or no)       11,820   86 %    78 %    73 %    71 %
No swap in the period           (sample) 85 %    76 %    71 %    69 %

Check: refund-ticket cohort skews to Zuid's evening slots; same gap within Zuid evenings (−12 pts).
Read: a good swap brings customers back like no swap at all; a bad one costs ~11 points.
"""),
    tools="tools: cohort charts in product analytics (Amplitude, Mixpanel, PostHog) or SQL in the warehouse; a monthly review.",
    gains=["<b>Answers “do they come back?”</b> honestly.",
           "<b>Growth can't hide losses</b>.",
           "<b>Effects of changes show</b> in new cohorts.",
           "<b>Strong evidence</b> for leadership.",
           "<b>Links product to revenue</b> over time."],
    losses=["<b>Takes weeks</b> to see a curve.",
            "<b>Cohorts can differ</b> for other reasons.",
            "<b>Easy to over-read</b> small cohorts.",
            "<b>Not causal</b> on its own (A/B tests are)."],
    baseline="Each line compares <b>reading total active customers over time</b> to <b>retention curves comparing cohorts that share a starting point</b>.",
    ratings=[(2, 4, "Shows what a good or bad swap does to a customer's habits."),
             (2, 5, "Links approvals to repeat orders and revenue."),
             (2, 4, "Comparable groups, checked for differences."),
             (3, 3, "Takes eight weeks to read."),
             (3, 3, "Neutral."),
             (2, 4, "One chart explains why approvals matter."),
             (2, 5, "Femke took it to the board."),
             (3, 3, "Neutral."),
             (3, 3, "A query and a monthly look.")],
    pitfalls=[("Reading totals", "Monthly actives up, all is well.", "compare cohorts."),
              ("Unfair comparisons", "Cohorts from different seasons or stores.", "check composition; compare within segments."),
              ("Small cohorts", "Conclusions from 40 customers.", "wait for size, or show the uncertainty."),
              ("Treating it as proof", "Correlation read as cause.", "use A/B tests for causal claims.")],
    use=["Questions about keeping customers.",
         "Judging whether a change improved habits.",
         "Subscription and repeat-purchase products.",
         "Explaining long-term value to leadership."],
    skip=["Questions about one session or one step: use funnels.",
          "Causal claims: run an experiment."],
    related=["<b>Funnels</b> (this volume)", "<b>North star metric</b> (Vol. 1)", "<b>Post-launch review</b> (this volume)", "<b>Reading results honestly</b> (this volume)"],
    quiz=[("What's a cohort?", "A group sharing a starting event or period."),
          ("Why can't total active customers answer “do they come back?”", "New customers hide whether existing ones stay."),
          ("What did Larder's curves show?", "After eight weeks: refund ticket 58 %, approved swap 71 %, no swap 69 %."),
          ("What's a selection effect?", "Cohorts differing for reasons other than the thing you're studying.")],
    try_it="Pick a good and a bad experience in your product. Group customers by which they had first, define “active”, and plot eight weeks of retention for both groups. Check one way they might differ besides the experience.",
    remember="Count members by the <span class=\"hl\">month they joined</span>. Totals hide who <span class=\"hl\">left</span>.",
    sources=["Alistair Croll and Benjamin Yoskovitz, <i>Lean Analytics</i> (2013), on cohorts.",
             "Amplitude, “Retention Analysis” guide.",
             "Brian Balfour, “Retention is King” (Reforge, 2018–).",
             "Sean Ellis and Morgan Brown, <i>Hacking Growth</i> (2017)."],
)

# ------------------------------------------------------------------ 04 Dashboards That Get Used
db_problem = Doodle(760, 280, "Doodle of July 2026: fourteen product dashboards in the analytics tool, built by different people for different questions. Most haven't been opened in a month. When Priya asks how ordering is doing, Grace still builds a slide by hand.",
                    "Fourteen dashboards, most unopened for a month, and Grace still builds a slide by hand.")
for i in range(14):
    r, c = divmod(i, 7)
    db_problem.box(20 + c * 66, 30 + r * 80, 56, 64, None, "paper", dash=i not in (2, 9), rx=4)
db_problem.box(500, 50, 240, 90, "Priya", "y", sub="“how is ordering doing?”", subsize=15)
db_problem.note(380, 254, "a slide by hand, every Monday", "red")

db_analogy = Doodle(760, 250, "Doodle of a car dashboard: speed, fuel and a few warning lights, in fixed places, read at a glance while driving. Not forty gauges. The detailed diagnostics live in the garage's computer.",
                     "A car dashboard: a few numbers in fixed places, read at a glance. Diagnostics live in the garage.")
db_analogy.icon("stopwatch", 40, 60, 1.3)
for i, (t, s, f) in enumerate([("speed", "one big number", "y"), ("fuel", "will we make it?", "blue"), ("warning lights", "only when needed", "pink")]):
    db_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, subsize=14)
db_analogy.note(450, 210, "a glance, not a study", "pen")

db_how = Doodle(760, 360, "Grace's ordering health page, from 13 July 2026. Top: the north star, perfect orders per week, with its target. Below: four input metrics: share complete, on time, no refund ticket, swaps answered within two minutes. Then three guardrails: order conversion, picking time per swap order, crash-free sessions. Each with this week, last week and the target. Reviewed every Monday for fifteen minutes with Priya and the trio. Twelve old dashboards archived.",
                 "One page: the north star, four inputs, three guardrails. This week, last week, target. Fifteen minutes on Mondays.")
db_how.box(14, 14, 732, 70, "perfect orders / week: 84 % · target 86 % (Sep)", "green", size=16)
for i, (t, v) in enumerate([("complete", "92 %"), ("on time", "90 %"), ("no refund", "96.3 %"), ("answered ≤ 2 min", "82 %")]):
    db_how.box(14 + i * 186, 100, 172, 80, t, "y", sub=v, size=13)
for i, (t, v) in enumerate([("conversion", "9.5 %"), ("picking / swap", "+7 s"), ("crash-free", "99.7 %")]):
    db_how.box(14 + i * 248, 196, 236, 64, t, "blue", sub=v, size=14)
db_how.note(380, 296, "this week · last week · target, for each", "pen", size=16)
db_how.note(380, 326, "Mondays, 15 minutes · 12 old dashboards archived", "green", size=16)

DASHBOARDS = dict(
    slug="dashboards",
    kicker="a.k.a. “the car dashboard”",
    tldr="Dashboards multiply and stop being read. Build <b>one page</b> people actually use: the <b>north star</b> at the top, the few <b>input metrics</b> that drive it, the <b>guardrails</b> that mustn't get worse, each with <b>this period, last period and the target</b>. Give it a <b>fixed review</b> (fifteen minutes, weekly, with the people who act on it), and <b>archive</b> the rest. Detail belongs in analyses, not on the health page.",
    chips=[("Family", "instrumenting"), ("Origin", "metric trees and north star frameworks; Stephen Few, <i>Information Dashboard Design</i> (2006)"), ("Lives in", "one page in the analytics tool, reviewed weekly"), ("Pairs with", "north star metric, guardrail metrics, OKRs")],
    problem_side="Larder, 13 July 2026",
    problem="""  <p class="lead">The analytics tool now holds <b>fourteen product dashboards</b>, built by different people for different questions. Most <b>haven't been opened in a month</b>. When Priya asks “how is ordering doing?”, Grace still <span class="hl-pink">builds a slide by hand</span> every Monday, copying numbers from four of them.</p>
  <ul>
    <li>Every question gets a dashboard; nobody removes old ones.</li>
    <li>No page shows the few numbers that matter together.</li>
    <li>Without a review rhythm, nobody looks until something breaks.</li>
  </ul>""",
    problem_figs=[db_problem],
    analogy_side="the car dashboard",
    analogy="""  <p>A car's dashboard shows <b>speed</b>, <b>fuel</b> and a few <b>warning lights</b>, always in the same places, read at a glance while driving. Not forty gauges. The detailed diagnostics live in the <b>garage's computer</b>, used when something needs investigating. Nobody studies the dashboard; they glance and drive.</p>""",
    analogy_figs=[db_analogy],
    map=[("Speed", "The north star: perfect orders per week"),
         ("Fuel", "Input metrics: complete, on time, no refund, answered"),
         ("Warning lights", "Guardrails: conversion, picking time, crashes"),
         ("Fixed places", "The same layout every week"),
         ("The garage's computer", "Detailed analyses, separate from the health page")],
    how_side="one page, a weekly glance",
    how="""  <p>Grace replaced the slide with an <b>ordering health page</b>: the <b>north star</b> on top, <b>four inputs</b> underneath, <b>three guardrails</b> below, each with this week, last week and the target. Every Monday, fifteen minutes with Priya and the trio. Twelve dashboards were archived (two kept for deep dives). The first review caught on-time slipping in Rotterdam a week before anyone complained.</p>""",
    how_figs=[db_how],
    steps=[("Start from the north star", "One number at the top, with its target."),
           ("Add the inputs that drive it", "Three to five; the levers the team can pull."),
           ("Add guardrails", "Two or three things that mustn't get worse."),
           ("Show now, before, target", "For each number; colour only against the target."),
           ("Set a review rhythm", "Weekly, fifteen minutes, with the people who act."),
           ("Archive the rest", "Keep analyses for deep dives; remove unused dashboards.")],
    vocab=[("Health page", "One page with the few numbers that show whether the product is OK."),
           ("North star", "The one number for the value customers get."),
           ("Input metric", "A number that drives the north star and the team can move."),
           ("Guardrail", "A number that must not get worse."),
           ("Vanity metric", "A number that looks good but doesn't guide action."),
           ("Review rhythm", "A fixed time when the page is read and acted on.")],
    code=dict(file="product/analytics/ordering-health.md", note="the health page's layout, 13 July 2026", plain=True, src="""
# Ordering health · reviewed Mondays 09:30, 15 min · Priya, Grace, Noor, Ben

NORTH STAR   perfect orders / week        this wk 84.1 %   last wk 83.6 %   target 86 % (30 Sep)
INPUTS       complete                     92.0 %           91.8 %           93 %
             on time                      90.2 %           89.5 %           92 %
             no refund ticket             96.3 %           96.1 %           97 %
             swaps answered ≤ 2 min       82 %             81 %             85 %
GUARDRAILS   order conversion             9.5 %            9.4 %            ≥ 9.3 %
             picking time per swap order  +7 s             +7 s             ≤ +15 s
             crash-free sessions          99.7 %           99.6 %           ≥ 99.5 %

By city on click · deep dives: approvals funnel, retention by first swap
Archived 13 Jul: 12 dashboards (kept: funnel, retention)
"""),
    tools="tools: your analytics tool's dashboards (Amplitude, Looker, Metabase, Grafana); one page per product area; a recurring calendar slot.",
    gains=["<b>One page everyone reads</b>.",
           "<b>Problems caught weekly</b>, not monthly.",
           "<b>No manual slides</b>.",
           "<b>Shared numbers</b> for product and leadership.",
           "<b>Fewer dashboards</b> to maintain."],
    losses=["<b>Choosing what's off</b> the page is hard.",
            "<b>Metrics need to be right</b> first.",
            "<b>A weekly habit</b> to keep.",
            "<b>Deep questions</b> still need analyses."],
    baseline="Each line compares <b>many dashboards built per question and rarely opened</b> to <b>one health page (north star, inputs, guardrails) reviewed weekly, the rest archived</b>.",
    ratings=[(3, 4, "Problems customers feel show up weekly."),
             (2, 4, "The north star and its drivers on one page."),
             (2, 4, "Decisions start from the same numbers."),
             (2, 4, "Rotterdam's slip caught a week early."),
             (2, 4, "Three to five inputs, not fifty charts."),
             (1, 5, "Everyone reads the same page."),
             (2, 4, "Priya stops asking for slides."),
             (3, 3, "Neutral."),
             (2, 4, "Fifteen minutes a week; 12 dashboards fewer.")],
    pitfalls=[("Fifty numbers", "A health page nobody can read at a glance.", "north star, a few inputs, a few guardrails."),
              ("No targets", "Numbers without a sense of good or bad.", "show the target next to each."),
              ("No rhythm", "Opened only when something breaks.", "a fixed weekly review."),
              ("Keeping everything", "Old dashboards linger.", "archive what nobody opened in a month.")],
    use=["Any product with a north star and a team that acts on numbers.",
         "When leadership keeps asking for slides.",
         "When dashboards have multiplied.",
         "After a launch, to watch steady state."],
    skip=["One-off analyses: keep them as analyses.",
          "Incident monitoring: that's operations dashboards and alerts."],
    related=["<b>North star metric</b> (Vol. 1)", "<b>Leading vs lagging indicators</b> (Vol. 1)", "<b>Guardrail metrics</b> (this volume)", "<b>OKRs</b> (this volume)"],
    quiz=[("What goes at the top of the health page?", "The north star, with its target."),
          ("What are input metrics?", "The few numbers that drive the north star and the team can move."),
          ("What makes a dashboard get used?", "Few numbers, targets beside them, and a fixed weekly review."),
          ("What happened to the other dashboards?", "Twelve archived; two kept for deep dives.")],
    try_it="Count your product's dashboards and when each was last opened. Design one health page on paper: your north star, up to five inputs and three guardrails, each with now, before and target. Book fifteen minutes a week to review it, and archive anything unopened for a month.",
    remember="A car <span class=\"hl\">dashboard</span>, not a cockpit. Glance <span class=\"hl\">weekly</span>.",
    sources=["Stephen Few, <i>Information Dashboard Design</i>, 2nd ed. (2013).",
             "Amplitude, <i>The North Star Playbook</i> (2019).",
             "Abhi Sivasailam, “Metric Trees” (Reforge / talks, 2022–).",
             "Edward Tufte, <i>The Visual Display of Quantitative Information</i> (1983)."],
)

NOTES = [TRACKING, FUNNELS, COHORTS, DASHBOARDS]
