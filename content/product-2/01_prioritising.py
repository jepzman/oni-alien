# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 2 · Prioritising.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 RICE & ICE Scoring
rice_problem = Doodle(760, 290, "Doodle of Grace's planning wall on 2 February 2026: twenty-three idea cards for the second quarter, each defended by whoever suggested it. Priya asks why substitution approvals should go before Joost's faster picking screen. Grace's honest answer is a feeling.",
                      "Twenty-three ideas, each with a sponsor, and the honest answer to “why this one first?” is a feeling.")
for i in range(23):
    r, c = divmod(i, 6)
    rice_problem.box(20 + c * 62, 24 + r * 52, 52, 40, None, ["y", "paper", "blue", "pink"][i % 4], rx=4)
rice_problem.note(200, 250, "23 ideas for Q2", "pen")
rice_problem.box(430, 40, 310, 70, "Priya", "paper", sub="“why this one first?”")
rice_problem.box(430, 150, 310, 70, "Grace", "pink", sub="“…it feels right”", stroke="red")
rice_problem.note(585, 262, "a feeling loses to a sponsor", "red")

rice_analogy = Doodle(760, 270, "Doodle of a charity's grant committee scoring projects. For each project: how many people it reaches, how much it helps each one, how sure they are it works, and what it costs. Reach times impact times confidence, divided by cost, gives people helped per euro, a number to argue with.",
                      "A grant committee: reach × impact × confidence ÷ cost, a number to argue with, not to obey.")
for i, (t, s, f) in enumerate([("reach", "how many people", "blue"), ("impact", "how much each", "y"), ("confidence", "how sure", "paper"), ("effort", "what it costs", "pink")]):
    x = 20 + i * 190
    rice_analogy.box(x, 50, 160, 80, t, f, sub=s, size=18, subsize=15)
    if i < 3:
        rice_analogy.text(x + 175, 98, "÷" if i == 2 else "×", "t-head", size=24)
rice_analogy.note(380, 186, "= people helped per euro", "green", size=20)
rice_analogy.note(380, 236, "the wells project wins, the gala dinner doesn't", "pen", size=18)

rice_how = Doodle(760, 340, "Grace's RICE table for six of the ideas, per quarter. Substitution approvals: reach 76,000 orders, impact 2, confidence 80 percent, effort 8 person-weeks, score 15,200. Faster picking screen: reach 364,000, impact 0.5, confidence 30 percent, effort 6, score 9,100, and it serves another outcome, so it goes to Joost and Priya. No-swaps flag: 30,000, 1, 50 percent, 2, score 7,500. Live order update: 76,000, 0.5, 50 percent, 4, score 4,750. Auto-refund button: 23,000, 0.5, 80 percent, 3, score 3,000. Recipe ideas: 364,000, 0.25, 20 percent, 12, score 1,500.",
                 "Six ideas scored the same way. The ranking starts the conversation; the outlier is the interesting part.")
for x, t in [(300, "R"), (370, "I"), (440, "C"), (510, "E"), (590, "score")]:
    rice_how.head(x, 36, t, size=16)
rows = [("substitution approvals", "76k", "2", "80 %", "8", 15200, "green"), ("faster picking screen", "364k", "0.5", "30 %", "6", 9100, "paper"),
        ("“no swaps” flag", "30k", "1", "50 %", "2", 7500, "y"), ("live order update", "76k", "0.5", "50 %", "4", 4750, "y"),
        ("auto-refund button", "23k", "0.5", "80 %", "3", 3000, "y"), ("recipe ideas", "364k", "0.25", "20 %", "12", 1500, "pink")]
for i, (name, r, im, c, e, score, f) in enumerate(rows):
    y = 70 + i * 38
    rice_how.text(20, y, name, anchor="start", size=15)
    for x, v in [(300, r), (370, im), (440, c), (510, e)]:
        rice_how.text(x, y, v, size=15)
    rice_how.text(590, y, f"{score:,}", "t-head", size=15)
    rice_how.box(636, y - 16, max(6, round(score / 15200 * 110)), 18, None, f, rx=3)
rice_how.note(390, 300, "↑ picking screen: another outcome → Joost & Priya", "pen", size=17)
rice_how.note(380, 328, "a ranking to argue with, not a verdict", "green", size=18)

RICE = dict(
    slug="rice-ice-scoring",
    kicker="a.k.a. “the grant committee”",
    tldr="When every idea has a sponsor, score them the same way. <b>RICE</b> = <b>Reach</b> (how many customers or orders per quarter) × <b>Impact</b> (how much for each, on a fixed scale) × <b>Confidence</b> (how sure you are, from evidence) ÷ <b>Effort</b> (person-weeks). <b>ICE</b> drops reach for a quicker first pass. The number doesn't decide; it makes the <b>assumptions visible</b>, so people argue about reach and confidence instead of about whose idea it is. Score only ideas that serve the <b>same outcome</b>.",
    chips=[("Family", "prioritising"), ("Origin", "RICE: Sean McBride at Intercom (2016); ICE: Sean Ellis, growth teams"), ("Lives in", "a table next to the opportunity tree"), ("Pairs with", "opportunity solution tree, cost of delay, saying no")],
    problem_side="Larder, 2 February 2026",
    problem="""  <p class="lead">Q2 planning. Grace's wall has <b>23 idea cards</b>: her own branch of the opportunity tree, Sam's auto-refund button, Joost's faster picking screen, Femke's recipe ideas, and more. Each has a sponsor who can explain why it matters. Then Priya asks the simple question: <i>why substitution approvals before Joost's picking screen?</i> Grace believes she's right, but <span class="hl-pink">her honest answer is a feeling</span>, and a feeling loses to a sponsor.</p>
  <ul>
    <li>Ideas are compared by how persuasive their sponsors are.</li>
    <li>Big ideas with no evidence sit next to small ideas with lots, and look equal.</li>
    <li>Nobody can say what would change the order.</li>
  </ul>""",
    problem_figs=[rice_problem],
    analogy_side="the grant committee",
    analogy="""  <p>A charity with one budget and fifty proposals asks the same four questions of each: how many people does it <b>reach</b>, how much does it <b>help each</b>, how <b>sure</b> are we it works, and what does it <b>cost</b>? People helped per euro isn't the final word (a committee still talks), but the village wells don't lose to the gala dinner just because the gala has a better speaker.</p>""",
    analogy_figs=[rice_analogy],
    map=[("People reached", "Reach: orders or customers affected per quarter"),
         ("How much it helps each", "Impact: 3 massive · 2 high · 1 medium · 0.5 low · 0.25 minimal"),
         ("How sure we are", "Confidence: 100 % tested · 80 % strong evidence · 50 % some · 20 % a hunch"),
         ("What it costs", "Effort: person-weeks for the whole team"),
         ("People helped per euro", "The RICE score: a ranking to argue with")],
    how_side="same four questions for every idea",
    how="""  <p>Approvals came out top, with evidence behind every number (the concierge test, the prototype). The surprise was the <b>picking screen</b> in second place: huge reach, weak evidence. It serves a different outcome (picking speed, Joost's), so Grace didn't fight it: she took the score to Joost and Priya, and Joost ran his own interviews with pickers.</p>""",
    how_figs=[rice_how],
    steps=[("Fix the scales first", "Write down what impact 3, 2, 1, 0.5 and 0.25 mean, and what earns 80 % confidence, before scoring."),
           ("Use one outcome per table", "Score the ideas that compete for the same outcome; send others to their owners."),
           ("Reach from data", "Orders or customers per quarter: 21 % of orders have a swap → 76,000 a quarter."),
           ("Confidence from evidence", "A test or data → 80 %. Interviews → 50 %. Someone's hunch → 20 %. No exceptions for seniority."),
           ("Effort from the team", "Person-weeks from the engineers who'll build it, rough is fine."),
           ("Score, then discuss", "Look for surprises; change a number only with new evidence, and write down why.")],
    vocab=[("RICE", "Reach × Impact × Confidence ÷ Effort."),
           ("ICE", "Impact × Confidence × Ease: a quicker, rougher pass."),
           ("Reach", "How many customers or orders an idea touches in a period."),
           ("Impact scale", "A fixed scale (3 to 0.25) so “high” means the same for everyone."),
           ("Confidence", "How much evidence backs the other numbers."),
           ("Person-week", "One person working one week: the unit of effort.")],
    code=dict(file="product/q2-2026/rice.md", note="Grace's RICE table, 2 February 2026", plain=True, src="""
# Q2 2026 · RICE for the "refund tickets 6 % → 2 %" outcome    (per quarter)

Scales   Impact 3 massive · 2 high · 1 medium · 0.5 low · 0.25 minimal
         Confidence 100 % tested · 80 % strong evidence · 50 % interviews · 20 % hunch
         Effort = person-weeks, Ben's and Dee's teams together

| Idea                     | Reach  | Impact | Conf. | Effort | RICE   | Evidence                     |
|--------------------------|--------|--------|-------|--------|--------|------------------------------|
| Substitution approvals   | 76,000 | 2      | 80 %  | 8      | 15,200 | concierge, prototype         |
| "No swaps" flag per item | 30,000 | 1      | 50 %  | 2      |  7,500 | 5/12 interviews              |
| Live order update        | 76,000 | 0.5    | 50 %  | 4      |  4,750 | 7/12 interviews              |
| Auto-refund button (Sam) | 23,000 | 0.5    | 80 %  | 3      |  3,000 | faster, not fewer refunds    |
| Recipe ideas (Femke)     |364,000 | 0.25   | 20 %  | 12     |  1,500 | investor's hunch             |

Other outcome (picking speed → Joost): faster picking screen 364,000 · 0.5 · 30 % · 6 = 9,100
Reach: 28,000 orders/week × 13 weeks = 364,000; 21 % have a swap (concierge) = 76,000
"""),
    tools="tools: a spreadsheet or a table in the repo is enough. Productboard, Airfocus and Jira Product Discovery have RICE fields built in. Keep the scales written next to the table.",
    gains=["<b>Arguments about numbers</b>, not about sponsors.",
           "<b>Evidence counts</b>: confidence rewards tested ideas.",
           "<b>Small, sure ideas surface</b> next to big, vague ones.",
           "<b>Surprises show up</b>: the picking screen's reach.",
           "<b>Repeatable</b>: next quarter's table uses the same scales."],
    losses=["<b>False precision</b>: 15,200 looks exact; it's a guess.",
            "<b>Gameable</b>: impact 3 for your own idea.",
            "<b>Misses timing</b>: a deadline doesn't show (see cost of delay).",
            "<b>Mixes outcomes badly</b> if you score everything together."],
    baseline="Each line compares <b>ranking ideas by how persuasive their sponsors are</b> to <b>scoring every idea for one outcome with the same RICE scales, then discussing the surprises</b>.",
    ratings=[(3, 4, "Reach and impact are counted in customers and orders."),
             (2, 4, "Ideas are ranked by their effect on the outcome."),
             (2, 4, "Confidence rewards evidence over enthusiasm."),
             (3, 3, "Doesn't speed up learning; shows where evidence is missing."),
             (2, 4, "A clear top three instead of 23 equal cards."),
             (2, 4, "Everyone can read why approvals came first."),
             (2, 4, "Sponsors see their idea scored fairly, not dismissed."),
             (3, 3, "Doesn't change how work flows."),
             (3, 4, "An hour to score; minutes to update.")],
    pitfalls=[("Scales made up on the spot", "Impact 3 for every idea of your own.", "write the scales first; score others' ideas before your own."),
              ("Confidence by rank", "The CEO's idea gets 80 %.", "confidence comes only from evidence: tests, data, interviews."),
              ("One table for everything", "Picking speed and refunds compete on one list.", "score ideas per outcome; send others to their owners."),
              ("Obeying the number", "15,200 beats 15,100, so that's decided.", "close scores mean discuss; the table starts the conversation.")],
    use=["Quarterly planning with many competing ideas.",
         "When a sponsor's enthusiasm is winning the argument.",
         "Comparing ideas for the same outcome.",
         "Showing stakeholders why their idea is where it is."],
    skip=["Deadlines and legal must-dos: they're not optional (see cost of delay).",
          "Two or three ideas: just discuss them.",
          "Ideas for different outcomes: decide the outcome first."],
    related=["<b>Cost of delay</b> (this volume)", "<b>Saying no without burning bridges</b> (this volume)", "<b>Opportunity solution tree</b> (Vol. 1)", "<b>Options analysis</b> (Ana, book 1 vol. 2)"],
    quiz=[("What do the four letters of RICE stand for?", "Reach, Impact, Confidence, Effort: R × I × C ÷ E."),
          ("Where should confidence come from?", "Evidence: tests and data score high, interviews medium, hunches low, whoever had the idea."),
          ("Why score one outcome at a time?", "Ideas for different outcomes aren't really competing; the outcome choice comes first."),
          ("Two ideas score 15,200 and 15,100. What next?", "Discuss them: the scores are too rough to separate them.")],
    try_it="Take the top ten ideas on your backlog that serve one outcome. Write your impact and confidence scales on top of a sheet, then score all ten in 45 minutes with an engineer. Circle the biggest surprise and take it to whoever owns that idea.",
    remember="Same four questions for <span class=\"hl\">every</span> idea. The number starts the argument; <span class=\"hl\">evidence</span> ends it.",
    sources=["Sean McBride, “RICE: Simple prioritization for product managers” (Intercom blog, 2016).",
             "Sean Ellis and Morgan Brown, <i>Hacking Growth</i> (2017), on ICE scoring.",
             "Itamar Gilad, <i>Evidence-Guided</i> (2023), the Confidence Meter.",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021), on comparing solutions."],
)

# ------------------------------------------------------------------ 02 Cost of Delay
cod_problem = Doodle(760, 290, "Doodle of two orders of work in February 2026. Plan A: substitution approvals first, eight weeks, then the no-swaps flag, two weeks. Plan B: the flag first, then approvals. The team picked plan A because approvals are worth more, so the two-week flag waits eight weeks while allergy households keep getting unsafe swaps.",
                     "Biggest value first looks obvious, until the two-week job waits eight weeks behind it.")
cod_problem.head(20, 50, "plan A", anchor="start", size=17)
cod_problem.box(110, 26, 400, 40, "approvals · 8 weeks", "green", size=16, rx=4)
cod_problem.box(516, 26, 100, 40, "flag", "y", size=16, rx=4)
cod_problem.note(682, 52, "waits", "red", size=18)
cod_problem.head(20, 130, "plan B", anchor="start", size=17)
cod_problem.box(110, 106, 100, 40, "flag", "y", size=16, rx=4)
cod_problem.box(216, 106, 400, 40, "approvals · 8 weeks", "green", size=16, rx=4)
cod_problem.box(110, 186, 560, 60, "allergy households: unsafe swaps for 8 more weeks", "pink", stroke="red", size=15)
cod_problem.note(380, 276, "“approvals are worth more, so they go first”", "pen")

cod_analogy = Doodle(760, 260, "Doodle of a supermarket queue: a shopper with a full trolley lets the person behind with one carton of milk go first. The full trolley loses one minute; the milk saves fifteen. Value per minute of waiting decides the order, not the size of the shop.",
                      "At the checkout, the full trolley lets the one carton of milk go first: it costs a minute and saves fifteen.")
cod_analogy.icon("bucket", 70, 40, 1.6)
cod_analogy.box(30, 160, 200, 60, "full trolley", "paper", sub="15 minutes")
cod_analogy.arrow(260, 110, 480, 110, label="“go ahead”", lx=370, ly=96)
cod_analogy.icon("cup", 540, 60, 1.4)
cod_analogy.box(500, 160, 200, 60, "one carton", "y", sub="1 minute")
cod_analogy.note(380, 248, "short, valuable jobs jump the queue", "green")

cod_how = Doodle(760, 340, "Grace's cost of delay table, 9 February 2026. The no-swaps flag: about 12,000 euros a month lost while it waits, two weeks to build, CD3 of 24. Substitution approvals: about 30,000 euros a month, eight weeks, CD3 of 15. Live order update: about 6,000 euros a month, four weeks, CD3 of 6. Rotterdam in the app has a fixed date, 27 April: worthless after it if late, so it is scheduled to finish by 20 April. Order: Rotterdam work protected, then flag, then approvals, then live updates. Flag first costs about 15,000 euros of delayed approvals; approvals first would cost about 24,000 euros of delayed flag.",
                "Divide cost of delay by duration. The flag goes first; the fixed date gets protected, whatever its score.")
for x, t in [(330, "€ / month"), (450, "months"), (560, "CD3")]:
    cod_how.head(x, 36, t, size=15)
for i, (name, cd, dur, cd3, f) in enumerate([("“no swaps” flag", "12k", "0.5", "24", "green"), ("substitution approvals", "30k", "2", "15", "y"), ("live order update", "6k", "1", "6", "paper")]):
    y = 76 + i * 40
    cod_how.text(20, y, name, anchor="start", size=16)
    cod_how.text(330, y, cd, size=16)
    cod_how.text(450, y, dur, size=16)
    cod_how.box(530, y - 22, 60, 30, cd3, f, size=16, rx=6)
cod_how.box(14, 206, 600, 50, None, "pink", rx=8)
cod_how.text(24, 237, "Rotterdam in the app · fixed date 27 Apr → done by 20 Apr", "t-head", anchor="start", size=15)
cod_how.note(690, 238, "protected", "red", size=18)
cod_how.note(380, 296, "flag first: €15k of delay · approvals first: €24k", "pen", size=18)
cod_how.note(380, 326, "CD3 = cost of delay ÷ duration", "green", size=18)

COD = dict(
    slug="cost-of-delay",
    kicker="a.k.a. “let the carton of milk go first”",
    tldr="Every week an idea isn't live has a price: lost revenue, refunds, risk, a missed date. That's its <b>cost of delay</b>, per week or month. Divide it by how long the work takes and you get <b>CD3</b> (cost of delay divided by duration): do the <b>highest CD3 first</b>, so short, valuable jobs don't wait behind long ones. Also look at the <b>urgency profile</b>: some items lose value steadily, and some have a <b>fixed date</b> after which they're worth nothing; protect those first.",
    chips=[("Family", "prioritising"), ("Origin", "Don Reinertsen, <i>The Principles of Product Development Flow</i> (2009); Joshua Arnold, Black Swan Farming"), ("Lives in", "a column next to the RICE table"), ("Pairs with", "RICE scoring, now / next / later roadmap, business case")],
    problem_side="Larder, 9 February 2026",
    problem="""  <p class="lead">RICE put approvals first, so the team planned it first: <b>eight weeks</b>, then the <b>“no swaps” flag</b>, two weeks. It looks obvious: do the most valuable thing first. But the flag would then wait eight weeks, and in those weeks allergy households (4 of 12 interviews) keep getting <span class="hl-pink">swaps they can't eat</span>. Meanwhile Rotterdam's app work (zones, prices, opening hours) has to be ready for 27 April, whatever any score says.</p>
  <ul>
    <li>Big-value-first makes small, urgent items wait behind long ones.</li>
    <li>Value scores ignore time: when something ships matters as much as what.</li>
    <li>Fixed dates hide in the backlog until they're suddenly late.</li>
  </ul>""",
    problem_figs=[cod_problem],
    analogy_side="the supermarket queue",
    analogy="""  <p>At the checkout, the shopper with a <b>full trolley</b> lets the person with <b>one carton of milk</b> go first. The trolley loses a minute; the milk saves fifteen. Nobody thinks the milk is more important than the week's shop; it's just that <b>value per minute of waiting</b> decides the order. And the person whose train leaves in five minutes? Let them through too.</p>""",
    analogy_figs=[cod_analogy],
    map=[("The full trolley", "Approvals: high value, eight weeks"),
         ("One carton of milk", "The “no swaps” flag: decent value, two weeks"),
         ("Minutes saved per minute lost", "CD3: cost of delay ÷ duration"),
         ("The train leaving in five minutes", "A fixed date: Rotterdam on 27 April"),
         ("Letting someone through", "Reordering the backlog by CD3")],
    how_side="cost of delay ÷ duration",
    how="""  <p>Grace priced each item's delay roughly, from the refund numbers: approvals ≈ <b>€30,000 a month</b> of avoidable refunds, the flag ≈ <b>€12,000</b> (refunds plus allergy customers leaving). Flag first costs about €15,000 of delayed approvals; approvals first, about €24,000 of delayed flag. The flag went live on <b>23 February</b>. Rotterdam's app work was protected separately: a <b>fixed-date</b> item doesn't compete on CD3, it gets scheduled back from its date.</p>""",
    how_figs=[cod_how],
    steps=[("Price a week or month of waiting", "Refunds, revenue, churn, cost, risk. A rough euro figure beats “high”."),
           ("Name the urgency profile", "Standard (value lost steadily), fixed date (worthless if late), expedite (costs now), intangible (cheap now, costly later)."),
           ("Estimate the duration", "Weeks of the team's time, roughly."),
           ("Compute CD3", "Cost of delay ÷ duration. Highest first."),
           ("Protect fixed dates", "Schedule them back from the date with a buffer; they don't compete on CD3."),
           ("Revisit when numbers change", "New evidence, a new date, a shorter design: recompute.")],
    vocab=[("Cost of delay", "What it costs per week or month that something isn't live."),
           ("CD3", "Cost of delay divided by duration: the order to do things in."),
           ("Urgency profile", "How value changes with time: standard, fixed date, expedite, intangible."),
           ("Fixed date", "A deadline after which the work loses most of its value."),
           ("WSJF", "Weighted shortest job first: SAFe's version of CD3."),
           ("Queue cost", "The total value lost by everything waiting.")],
    code=dict(file="product/q2-2026/cost-of-delay.md", note="Grace's cost of delay sheet, 9 February 2026", plain=True, src="""
# Cost of delay · order of work, Feb–Apr 2026

| Item                     | Profile    | CoD / month          | Duration | CD3 | Order          |
|--------------------------|------------|----------------------|----------|-----|----------------|
| Rotterdam in the app     | fixed date | all value lost if    | 5 weeks  |  –  | protected:     |
|  (zones, prices, hours)  | 27 Apr     | late (lease signed)  |          |     | done by 20 Apr |
| "No swaps" flag          | standard   | ≈ €12k (refunds +    | 0.5 mo   | 24  | 1 → live 23 Feb|
|                          |            | allergy churn)       |          |     |                |
| Substitution approvals   | standard   | ≈ €30k (2/3 of swap  | 2 mo     | 15  | 2 → Amsterdam  |
|                          |            | refunds)             |          |     |    mid-April   |
| Live order update        | standard   | ≈ €6k ("where is my  | 1 mo     |  6  | 3 → Q2         |
|                          |            | order?" tickets)     |          |     |                |

Check: flag first delays approvals 0.5 mo → €15k. Approvals first delays flag 2 mo → €24k.
Rough numbers on purpose; recompute when the evidence changes.
"""),
    tools="tools: a column in the same sheet as RICE. SAFe calls it WSJF; Jira and Azure DevOps have WSJF fields. Black Swan Farming's cost of delay guides have worked examples.",
    gains=["<b>Short, valuable work ships sooner</b>.",
           "<b>Time has a price</b>, so waiting stops looking free.",
           "<b>Fixed dates are visible</b> and protected early.",
           "<b>Euro figures</b> make sense to finance and leadership.",
           "<b>Less total value lost</b> across the whole queue."],
    losses=["<b>Rough numbers</b>: cost of delay is an estimate.",
            "<b>Hard for intangible items</b> (tech debt, learning).",
            "<b>Can churn the order</b> if recomputed too often.",
            "<b>Needs finance-style thinking</b> some teams aren't used to."],
    baseline="Each line compares <b>doing the most valuable item first, regardless of how long it takes</b> to <b>ordering by cost of delay ÷ duration, with fixed dates protected</b>.",
    ratings=[(3, 4, "Customers waiting for a fix get it sooner."),
             (2, 5, "Value lost by waiting is counted in euros."),
             (2, 4, "Estimates come from refund and churn data."),
             (3, 4, "Small items ship and teach sooner."),
             (3, 4, "The order of work is explicit."),
             (2, 4, "Everyone sees why the flag jumped the queue."),
             (2, 4, "Finance understands euros per month."),
             (2, 4, "Small items flow instead of waiting."),
             (3, 3, "An extra column and an hour of estimating.")],
    pitfalls=[("Value first, time ignored", "The eight-week item goes first because it's worth more.", "divide by duration; short jobs often win."),
              ("Fake precision", "€29,412 a month.", "round numbers; the order matters, not the decimals."),
              ("Fixed dates scored like the rest", "Rotterdam's app work competes on CD3 and slips.", "schedule fixed-date items back from the date."),
              ("Reordering every day", "The plan changes with every new estimate.", "recompute at planning, or when evidence really changes.")],
    use=["Choosing the order of work, not just the top idea.",
         "When big items keep small, urgent ones waiting.",
         "Talking about priorities with finance and leadership.",
         "Anything with a deadline in the mix."],
    skip=["When every item is about the same size: RICE is enough.",
          "Legal must-dos: they're fixed dates, schedule them."],
    related=["<b>RICE &amp; ICE scoring</b> (this volume)", "<b>Now / next / later roadmap</b> (this volume)", "<b>Business case one-pager</b> (this volume)", "<b>Last responsible moment</b> (Ana, book 1 vol. 2)"],
    quiz=[("What is CD3?", "Cost of delay divided by duration; do the highest first."),
          ("Why did the flag go before approvals?", "Its CD3 was higher (24 vs 15): two weeks of work that stopped €12k a month of losses."),
          ("How do you handle a fixed-date item?", "Schedule it back from the date with a buffer; don't let it compete on CD3."),
          ("Name two urgency profiles.", "Standard (value lost steadily) and fixed date (worthless if late); also expedite and intangible.")],
    try_it="Take your next five backlog items. For each, write a rough euro cost per month of it not being live, and its duration in weeks. Compute CD3 and compare the order with your current plan. If anything has a fixed date, schedule it back from that date first.",
    remember="Let the <span class=\"hl\">carton of milk</span> go first. And let the person with the <span class=\"hl\">train</span> through.",
    sources=["Donald Reinertsen, <i>The Principles of Product Development Flow</i> (2009).",
             "Joshua Arnold, “Cost of Delay” (blackswanfarming.com).",
             "Scaled Agile Framework, “Weighted Shortest Job First”.",
             "Özlem Yüce and Joshua Arnold, “Introduction to Cost of Delay” (Agile 2013)."],
)

# ------------------------------------------------------------------ 03 Kano Model
kano_problem = Doodle(760, 280, "Doodle of a February 2026 discussion. Femke says recipe ideas will delight customers. Sam says the no-swaps flag is just basic. Grace realises nobody knows which features customers take for granted, which they want more of, and which would surprise them; everyone guesses from their own taste.",
                      "Everyone is sure which features delight customers. Everyone has a different list.")
kano_problem.box(20, 30, 330, 80, "Femke", "y", sub="“recipes will delight them”")
kano_problem.box(410, 30, 330, 80, "Sam", "paper", sub="“the flag is just basic”")
kano_problem.box(150, 160, 460, 70, "basic? more-is-better? surprise?", "pink", stroke="red", size=17)
kano_problem.note(380, 264, "four opinions, zero customers asked", "red")

kano_analogy = Doodle(760, 280, "Doodle of a hotel room. Clean sheets are a must-be: nobody thanks you, everyone complains if they're missing. Wi-fi speed is performance: the faster the better. A handwritten welcome note is an attractor: nobody expects it, everyone remembers it. A trouser press is indifferent: nobody cares either way.",
                      "Grace's old job, hotels: clean sheets, fast wi-fi, a handwritten note, and the trouser press nobody uses.")
for i, (t, s, f) in enumerate([("clean sheets", "must-be", "pink"), ("fast wi-fi", "performance", "y"), ("a note", "attractive", "green"), ("trouser press", "indifferent", "paper")]):
    x = 20 + i * 186
    kano_analogy.box(x, 40, 166, 90, t, f, sub=s, size=16)
for i, t in enumerate(["missing: angry", "more: happier", "there: delighted", "nobody cares"]):
    kano_analogy.note(103 + i * 186, 166, t, "pen", size=17)
kano_analogy.note(380, 240, "same room, four very different features", "green")

kano_how = Doodle(760, 340, "The Kano diagram and Larder's survey, 212 customers in February 2026. Three curves: must-be features only stop dissatisfaction, performance features rise in a straight line, attractive features delight even in small amounts. Results: substitution approvals, performance 48 percent; no-swaps flag, must-be 41 percent; live order updates, attractive 39 percent; recipe ideas, indifferent 62 percent.",
                 "Three curves, and what 212 customers said: the flag is basic, approvals are more-is-better, recipes leave them cold.")
kx, ky = 40, 170
kano_how.line(f"M{kx} {ky} H400")
kano_how.line(f"M220 30 V310")
kano_how.note(404, ky - 10, "done well →", "pen", anchor="end", size=15)
kano_how.note(226, 24, "satisfied", "pen", anchor="start", size=15)
kano_how.note(226, 322, "dissatisfied", "pen", anchor="start", size=15)
kano_how.line("M50 300 Q 220 280 380 180", color="red")
kano_how.line("M60 290 L380 50", color="pen")
kano_how.line("M60 160 Q 230 150 380 40", color="green")
kano_how.note(78, 278, "must-be", "red", anchor="start", size=16)
kano_how.note(300, 120, "performance", "pen", anchor="start", size=16)
kano_how.note(110, 130, "attractive", "green", anchor="start", size=16)
for i, (feat, cat, pct, f) in enumerate([("approvals", "performance", "48 %", "y"), ("“no swaps” flag", "must-be", "41 %", "pink"),
                                         ("live order update", "attractive", "39 %", "green"), ("recipe ideas", "indifferent", "62 %", "paper")]):
    y = 40 + i * 66
    kano_how.box(430, y, 316, 54, None, f, rx=8)
    kano_how.text(444, y + 24, feat, "t-head", anchor="start", size=15)
    kano_how.text(444, y + 46, cat, anchor="start", size=14)
    kano_how.text(732, y + 36, pct, "t-head", anchor="end", size=18)
kano_how.note(588, 322, "212 answers, in-app survey", "pen", size=16)

KANO = dict(
    slug="kano-model",
    kicker="a.k.a. “clean sheets, fast wi-fi, a handwritten note”",
    tldr="Not all features please customers the same way. <b>Must-be</b> features only prevent anger: nobody thanks you for them. <b>Performance</b> features please in proportion: more is better. <b>Attractive</b> features delight because nobody expects them. Some are <b>indifferent</b>: nobody cares. Find out which is which by <b>asking customers two questions per feature</b> (how would you feel if it were there? and if it weren't?), not by guessing. Then fix the must-bes first, compete on performance, and add a few attractors.",
    chips=[("Family", "prioritising"), ("Origin", "Noriaki Kano, “Attractive quality and must-be quality” (1984)"), ("Lives in", "a short in-app survey and a table"), ("Pairs with", "customer interviews, RICE scoring, MoSCoW")],
    problem_side="Larder, 16 February 2026",
    problem="""  <p class="lead">With the flag shipping next week, the discussion turns to what comes after. <b>Femke</b> is sure recipe ideas will <i>delight</i> customers. <b>Sam</b> calls the “no swaps” flag “just basic, they'll expect it”. <b>Dee</b> thinks live order updates are a nice extra. Everyone is confident; <span class="hl-pink">nobody has asked customers</span>. Grace realises they're arguing about three different kinds of value without a word for any of them.</p>
  <ul>
    <li>People guess what delights customers from their own taste.</li>
    <li>Basic needs get treated as features to celebrate, or ignored until customers leave.</li>
    <li>“Delighters” get built while basics are still broken.</li>
  </ul>""",
    problem_figs=[kano_problem],
    analogy_side="the hotel room",
    analogy="""  <p>Grace learned this in hotels. <b>Clean sheets</b> are a must-be: nobody writes a review praising them, everyone writes one when they're dirty. <b>Wi-fi speed</b> is performance: the faster, the happier. A <b>handwritten welcome note</b> is attractive: unexpected, remembered. And the <b>trouser press</b>? Indifferent: it costs money and nobody cares. Each needs a different decision.</p>""",
    analogy_figs=[kano_analogy],
    map=[("Clean sheets", "Must-be: the “no swaps” flag for allergy households"),
         ("Wi-fi speed", "Performance: approvals (more control, more satisfaction)"),
         ("The handwritten note", "Attractive: live order updates with the substitute's photo"),
         ("The trouser press", "Indifferent: recipe ideas, 62 %"),
         ("Guest reviews", "The two-question Kano survey")],
    how_side="two questions per feature, then the curves",
    how="""  <p>For each feature, the survey asks: <i>if Larder had this, how would you feel?</i> and <i>if it didn't, how would you feel?</i> (like it, expect it, don't mind, can live with it, dislike it). The pair of answers puts each response in a category. With <b>212 answers</b> in a week, the debate settled: the flag is basic (fix it, don't celebrate it), approvals are performance (worth investing in), and recipe ideas leave most customers cold.</p>""",
    how_figs=[kano_how],
    steps=[("Pick 4–8 features", "Ones people disagree about; describe each in one customer-facing sentence."),
           ("Ask the two questions", "Functional (if it's there) and dysfunctional (if it's not), five answers each."),
           ("Reach the right customers", "An in-app survey or email to a sample; 100+ answers per segment if you can."),
           ("Classify each answer", "Use the Kano table: e.g. “expect it” + “dislike it” = must-be."),
           ("Take the most common category", "Note the split; a close call means the segment matters."),
           ("Decide by category", "Fix must-bes quietly, invest in performance, add a few attractors, drop the indifferent.")],
    vocab=[("Must-be", "Expected; missing it angers, having it pleases nobody."),
           ("Performance", "More is better, in proportion."),
           ("Attractive", "Unexpected; delights even in a small form."),
           ("Indifferent", "Customers don't care either way."),
           ("Reverse", "Some customers actively don't want it."),
           ("Decay", "Attractors become performance, then must-be, over time.")],
    code=dict(file="product/research/2026-02-kano.md", note="Kano survey, 16–20 February 2026", plain=True, src="""
# Kano survey · in-app, express and slot customers · 212 answers

Q1  If you could approve or refuse each substitute in the app within
    2 minutes, how would you feel?        (like / expect / neutral / tolerate / dislike)
Q2  If you couldn't, how would you feel?  (same five answers)
    ... same pair for each feature

| Feature                         | Must-be | Perform. | Attract. | Indiff. | Result         |
|---------------------------------|---------|----------|----------|---------|----------------|
| Approve substitutes in the app  | 22 %    | 48 %     | 18 %     | 12 %    | performance    |
| "Never swap this" flag per item | 41 %    | 24 %     | 9 %      | 26 %    | must-be        |
| Live order update with photo    | 8 %     | 21 %     | 39 %     | 32 %    | attractive     |
| Recipe ideas from your basket   | 3 %     | 9 %      | 26 %     | 62 %    | indifferent    |

Note: households with an allergy (n = 38): flag must-be 74 %.
Decisions: flag = basic, keep it working; approvals = invest; live update = Q2 bet;
recipes = park (see "Saying no").
"""),
    tools="tools: any survey tool (Typeform, Google Forms, an in-app survey such as Sprig or Hotjar) and a spreadsheet to classify answers. Kano analysis templates exist for Excel and Miro.",
    gains=["<b>Customers settle the argument</b>, not taste.",
           "<b>Basics get fixed first</b>, before delighters.",
           "<b>A shared vocabulary</b>: must-be, performance, attractive.",
           "<b>Wasted work avoided</b>: indifferent features get dropped.",
           "<b>Segments show up</b>: allergy households differ."],
    losses=["<b>Survey effort</b>: questions, reach, analysis.",
            "<b>Hypothetical answers</b>: people describe, not behave.",
            "<b>Categories drift</b>: today's delighter is tomorrow's basic.",
            "<b>Hard to explain</b> the two-question method at first."],
    baseline="Each line compares <b>guessing which features delight customers</b> to <b>a two-question Kano survey sorting features into must-be, performance, attractive and indifferent</b>.",
    ratings=[(2, 4, "Features sorted by how customers actually value them."),
             (3, 3, "Indirect: guides where value lies."),
             (2, 4, "212 customer answers instead of four opinions."),
             (2, 4, "A one-week survey settles a month of debate."),
             (2, 4, "Indifferent features drop off the list."),
             (2, 5, "Everyone uses the same words for kinds of value."),
             (2, 4, "Stakeholders see customer data behind the order."),
             (3, 3, "Doesn't change delivery flow."),
             (3, 3, "A survey and an afternoon of analysis.")],
    pitfalls=[("One question only", "“Would you like this?” Everyone says yes.", "ask both: if it's there, and if it's not."),
              ("Celebrating basics", "A launch party for the flag.", "must-bes are fixed quietly; save the fanfare for performance and attractors."),
              ("Ignoring segments", "The average hides allergy households.", "split results by segment when it matters."),
              ("Surveying once forever", "2026's delighter is 2028's must-be.", "repeat yearly for the features that matter.")],
    use=["When people argue about what customers value.",
         "Planning a release with basics and extras.",
         "Before investing in a “delighter”.",
         "Checking if old delighters have become basics."],
    skip=["When you can test real behaviour cheaply (an A/B test or fake door is better).",
          "Features customers can't imagine yet."],
    related=["<b>RICE &amp; ICE scoring</b> (this volume)", "<b>MoSCoW and its traps</b> (this volume)", "<b>Customer interviews</b> (Vol. 1)", "<b>Saying no without burning bridges</b> (this volume)"],
    quiz=[("What are the two Kano questions?", "How would you feel if the feature were there? And if it weren't?"),
          ("What's a must-be feature?", "One customers expect: missing it causes dissatisfaction, having it pleases nobody."),
          ("What happened to recipe ideas?", "62 % indifferent: most customers don't care, so they were parked."),
          ("Why do categories change over time?", "Customers get used to delighters; they become performance, then must-be.")],
    try_it="Pick four features your team disagrees about. Write the two Kano questions for each and send them to 50 customers (or 10, if that's what you can get). Classify the answers and bring the table to the next planning meeting before anyone gives an opinion.",
    remember="Fix the <span class=\"hl\">clean sheets</span> first. Then the wi-fi. Then a <span class=\"hl\">note</span> or two.",
    sources=["Noriaki Kano et al., “Attractive quality and must-be quality” (Journal of the Japanese Society for Quality Control, 1984).",
             "Daniel Zacarias, “The Complete Guide to the Kano Model” (foldingburritos.com, 2015).",
             "Charles Berger et al., “Kano's Methods for Understanding Customer-Defined Quality” (Center for Quality Management Journal, 1993).",
             "Jared Spool, “Understanding the Kano Model” (UIE, 2011)."],
)

# ------------------------------------------------------------------ 04 MoSCoW and Its Traps
mo_problem = Doodle(760, 290, "Doodle of the Rotterdam app scope list on 3 March 2026: nineteen items, fourteen of them marked Must. With fourteen musts in eight weeks of capacity, must has stopped meaning anything, and nobody knows what to drop when time runs short.",
                    "Nineteen items, fourteen musts. When everything is a must, nothing is.")
for i in range(19):
    r, c = divmod(i, 10)
    x, y = 20 + c * 72, 30 + r * 74
    must = i < 14
    mo_problem.box(x, y, 60, 56, "M" if must else "S", "pink" if must else "paper", stroke="red" if must else "", size=20)
mo_problem.note(380, 210, "14 × M in 8 weeks of capacity", "red", size=20)
mo_problem.note(380, 262, "time runs short → what goes?  nobody knows", "pen")

mo_analogy = Doodle(760, 270, "Doodle of packing a 10-kilo cabin bag. Must: passport and medicine, without them you can't travel. Should: the phone charger, painful to miss. Could: a third pair of shoes. Won't this time: the hairdryer, the hotel has one. If everything is a must, the bag doesn't close.",
                    "A 10-kilo cabin bag: the passport is a must; the third pair of shoes isn't, however much you love them.")
mo_analogy.icon("parcel", 40, 70, 1.6)
mo_analogy.note(85, 200, "10 kg", "pen")
for i, (k, t, f) in enumerate([("Must", "passport, medicine", "pink"), ("Should", "charger", "y"), ("Could", "third pair of shoes", "blue"), ("Won't", "hairdryer: hotel has one", "paper")]):
    y = 20 + i * 56
    mo_analogy.box(170, y, 110, 44, k, f, size=17, rx=6)
    mo_analogy.text(300, y + 29, t, anchor="start", size=17)
mo_analogy.note(600, 250, "all “must” = the bag won't close", "red", size=18)

mo_how = Doodle(760, 340, "The Rotterdam app scope after Grace and Sanne's rework, 3 March 2026. Must, six items, only what makes the launch fail without it: Rotterdam zones and slots, prices and VAT, opening hours, iDEAL and card payments, order tracking, store shown in the app. Should, five: substitution approvals in Rotterdam, Rotterdam welcome offer and others. Could, four, such as promo banners. Won't this time, four, written down: recipe ideas, business ordering, French language, loyalty points. Rule: musts at most 60 percent of capacity.",
                "Musts only if the launch fails without them, at most 60 % of capacity. And the Won'ts are written down.")
cols = [("Must · 6", "pink", ["zones & slots", "prices & VAT", "opening hours", "iDEAL & cards", "order tracking", "store in app"]),
        ("Should · 5", "y", ["approvals in RTM", "welcome offer", "Dutch help pages", "push reminders", "slot waitlist"]),
        ("Could · 4", "blue", ["promo banners", "store photos", "referral link", "courier names"]),
        ("Won't · 4", "paper", ["recipe ideas", "business orders", "French", "loyalty points"])]
for i, (h, f, items) in enumerate(cols):
    x = 14 + i * 186
    mo_how.box(x, 14, 174, 40, h, f, size=16, rx=6)
    for k, t in enumerate(items):
        mo_how.text(x + 87, 84 + k * 32, t, size=15)
mo_how.line("M14 290 H746", thin=True)
mo_how.note(380, 318, "musts ≤ 60 % of capacity · won'ts written down", "green", size=18)

MOSCOW = dict(
    slug="moscow",
    kicker="a.k.a. “the 10-kilo cabin bag”",
    tldr="<b>MoSCoW</b> sorts scope into <b>Must</b>, <b>Should</b>, <b>Could</b> and <b>Won't (this time)</b>. It's useful for a fixed date, and it's easy to break. Make it work with three rules: a <b>Must</b> is only something without which the release <b>fails or is illegal</b>; <b>Musts take at most about 60 %</b> of the capacity, so there's room to absorb surprises; and the <b>Won'ts are written down</b>, so they stop coming back. Agree the categories with the people who'll later ask “where's my feature?”.",
    chips=[("Family", "prioritising"), ("Origin", "Dai Clegg, Oracle (1994); DSDM / Agile Business Consortium"), ("Lives in", "the release plan for a fixed date"), ("Pairs with", "cost of delay, roadmap vs release plan, trade-off sliders")],
    problem_side="Larder, 3 March 2026",
    problem="""  <p class="lead">Sanne asks Grace for the Rotterdam app scope. Grace collects requests from Joost, Femke, Priya, Sam and the team: <b>19 items</b>. Everyone marks their own as “Must”. Result: <span class="hl-pink">14 Musts</span>, about twice what eight weeks of the team's time can deliver. When things slip, nobody will know what to drop, so the team will drop whatever's last, which may be order tracking.</p>
  <ul>
    <li>Everyone's own item is a Must; “must” stops meaning anything.</li>
    <li>No slack: one surprise and the date is at risk.</li>
    <li>Won'ts aren't written down, so they come back every week.</li>
  </ul>""",
    problem_figs=[mo_problem],
    meanwhile=[("architect-2", "decision-log", "two weeks later Sanne asks Ana the same kind of question about the open decisions for Rotterdam.", "Two weeks earlier, Grace and Sanne cut the Rotterdam app scope from 14 Musts to 6.")],
    analogy_side="the 10-kilo cabin bag",
    analogy="""  <p>Packing a 10-kilo cabin bag: the <b>passport and medicine</b> are musts (you can't travel without them), the <b>charger</b> is a should, the <b>third pair of shoes</b> is a could, and the <b>hairdryer</b> is a won't, because the hotel has one. Pack the musts first, leave some space, and if the bag won't close, the shoes come out, not the passport.</p>""",
    analogy_figs=[mo_analogy],
    map=[("Passport and medicine", "Must: zones, prices, payments, tracking"),
         ("The charger", "Should: approvals in Rotterdam, welcome offer"),
         ("The third pair of shoes", "Could: promo banners, store photos"),
         ("The hairdryer", "Won't this time: recipes, business orders, French"),
         ("Space left in the bag", "Musts at most 60 % of capacity")],
    how_side="a strict Must, room to spare, Won'ts on paper",
    how="""  <p>Grace and Sanne asked one question per item: <i>does the Rotterdam launch fail, or break the law, without it?</i> That left <b>six Musts</b>, about 55 % of the capacity. Approvals in Rotterdam became a <b>Should</b>, which mattered later: when the trade-off sliders were agreed on 31 March, it moved to June without a fight. The four Won'ts went into the plan with one line each explaining why.</p>""",
    how_figs=[mo_how],
    steps=[("List everything", "Every request for the release, with who asked for it."),
           ("Apply the strict Must test", "Does the release fail, or break the law, without it? If not, it's not a Must."),
           ("Check capacity", "Musts ≤ ~60 % of what the team can do. Too many? Find a smaller version of each Must."),
           ("Sort the rest", "Should: painful to miss. Could: nice. Won't: not this time, with a reason."),
           ("Agree with the askers", "In one session, with the people who'd escalate later."),
           ("Use it when things slip", "Drop Coulds, then Shoulds; Musts are protected by the slack.")],
    vocab=[("Must", "Without it the release fails or is illegal."),
           ("Should", "Important and painful to leave out, but there's a workaround."),
           ("Could", "Nice to have; first to go."),
           ("Won't (this time)", "Agreed not to do now, written down with a reason."),
           ("Contingency", "The slack Musts leave for surprises."),
           ("Timebox", "A fixed date or period; scope flexes to fit it.")],
    code=dict(file="product/rotterdam/app-scope.md", note="Rotterdam app scope, agreed 3 March 2026 (excerpt)", plain=True, src="""
# Rotterdam launch · app scope · 27 April 2026            agreed: Grace, Sanne, Joost, Priya

Must test: "Does the launch fail, or break the law, without it?"
Capacity: ~8 team-weeks · Musts ≈ 4.5 (55 %) · Should + Could fill the rest

MUST     Rotterdam zones and slots · prices and VAT · opening hours ·
         iDEAL and card payments · order tracking · Rotterdam store in the app
SHOULD   Substitution approvals in Rotterdam (Amsterdam first) · welcome offer ·
         Dutch help pages for Rotterdam · push reminders · slot waitlist
COULD    Promo banners · store photos · referral link · courier first names
WON'T    Recipe ideas (parked, see "Saying no") · business ordering (Korenwolf
(this    pilot runs by hand) · French (Antwerp, 2027) · loyalty points (no
 time)   outcome on our tree)

If we slip: drop Coulds first, then Shoulds, in this order. Musts don't move.
"""),
    tools="tools: a table in the release plan; labels on tickets (must/should/could/wont). The Agile Business Consortium's DSDM handbook defines the 60 % rule.",
    gains=["<b>A protected core</b> for a fixed date.",
           "<b>Clear drop order</b> when things slip.",
           "<b>Won'ts stop recurring</b> once written down.",
           "<b>Simple language</b> stakeholders already know.",
           "<b>Slack for surprises</b> with the 60 % rule."],
    losses=["<b>Inflation</b>: everything drifts back to Must.",
            "<b>Coarse</b>: no order inside a category.",
            "<b>Political</b>: “your item is a Could” hurts.",
            "<b>Ignores value per effort</b>: pair with RICE or CD3."],
    baseline="Each line compares <b>a scope list where each asker marks their own item Must</b> to <b>a strict Must test, Musts under 60 % of capacity, and Won'ts written down</b>.",
    ratings=[(3, 4, "Customers get the core working on day one."),
             (3, 4, "Protects the launch the business depends on."),
             (2, 3, "The Must test is a judgement, not data."),
             (3, 3, "Doesn't change learning speed."),
             (1, 5, "Six Musts instead of fourteen."),
             (2, 5, "Everyone knows what's in, out and droppable."),
             (2, 4, "Askers agreed the categories; fewer surprises later."),
             (3, 4, "Slack keeps the release on its date."),
             (3, 4, "One session; a label per item.")],
    pitfalls=[("Must inflation", "14 of 19 items are Musts.", "the strict test: fails or illegal without it."),
              ("No slack", "Musts fill 100 % of the capacity.", "keep Musts at about 60 %."),
              ("Won't = never", "People fight Won'ts as if forever.", "say “won't, this time”, with a reason and a review date."),
              ("Sorted alone", "Grace labels everything; Joost escalates in April.", "agree the labels with the askers in one session.")],
    use=["A release with a fixed date.",
         "Many stakeholders, each sure their item is essential.",
         "Planning what to drop when things slip.",
         "Short timeboxes where scope must flex."],
    skip=["Ongoing prioritisation of a backlog: use RICE or cost of delay.",
          "When there's no fixed date: order by value instead."],
    related=["<b>Cost of delay</b> (this volume)", "<b>Roadmap vs release plan</b> (this volume)", "<b>Kano model</b> (this volume)", "<b>Trade-off sliders</b> (Ana, book 1 vol. 2)"],
    quiz=[("What's the strict test for a Must?", "The release fails, or breaks the law, without it."),
          ("Why keep Musts at about 60 % of capacity?", "To leave slack for surprises so the Musts are safe."),
          ("What does “Won't” mean?", "Won't this time: agreed and written down with a reason, not “never”."),
          ("When things slip, what goes first?", "Coulds, then Shoulds; Musts stay.")],
    try_it="Take your next fixed-date release. Apply the strict Must test to every item and count how many survive. Check the Musts against 60 % of your capacity, write four Won'ts with a one-line reason each, and agree the list with the two loudest askers.",
    remember="Passport first, <span class=\"hl\">space left</span>, hairdryer stays home. Write the <span class=\"hl\">Won'ts</span> down.",
    sources=["Agile Business Consortium, <i>DSDM Agile Project Framework</i>, “MoSCoW Prioritisation”.",
             "Dai Clegg and Richard Barker, <i>Case Method Fast-Track</i> (1994).",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005), on prioritising for a date.",
             "Roman Pichler, <i>Strategize</i>, 2nd ed. (2022)."],
)

NOTES = [RICE, COD, KANO, MOSCOW]
