# Series 2 · The Solution Architect's Notebook · Vol. 2 · Big choices.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Build vs Buy vs Open Source
bb_problem = Doodle(760, 300, "Doodle of Korenwolf's first monthly invoice in June 2026: Mo and Marco built it in a spreadsheet in six hours, with two VAT errors. Ben offers to build an invoicing module in two sprints. Beside it, an iceberg: the visible tip is 'invoices'; under the water are VAT rules, invoice numbering, credit notes, payment reminders and Belgian e-invoicing.",
                    "“Two sprints” sees the tip. Invoicing is an iceberg.")
bb_problem.box(20, 30, 300, 90, "May invoice", "pink", sub="spreadsheet: 6 h, 2 VAT errors", stroke="red")
bb_problem.box(20, 160, 300, 60, "Ben: “two sprints”", "blue", size=17)
bb_problem.line("M360 110 H740", dash=True, thin=True)
bb_problem.raw('<path class="d f-paper" d="M550 40 L600 110 L500 110 z"/>')
bb_problem.raw('<path class="d f-blue" d="M500 110 L400 262 L720 262 L600 110 z"/>')
bb_problem.text(550, 100, "invoices", size=14)
for i, t in enumerate(["VAT rules · numbering", "credit notes · reminders", "Belgian e-invoicing (Peppol)"]):
    bb_problem.text(560, 160 + i * 30, t, size=15)
bb_problem.note(560, 290, "what “two sprints” doesn't see", "red")

bb_analogy = Doodle(760, 270, "Doodle of a restaurant's three choices. It bakes its own bread, because that's what guests come for. It buys napkins, because nobody comes for the napkins. It uses a classic recipe from a book: the recipe is free, but the kitchen still has to cook it.",
                    "A restaurant bakes the bread guests come for, buys the napkins, and knows a free recipe still has to be cooked.")
for i, (ic, t, s, f) in enumerate([("kitchen", "bake the bread", "what guests come for", "green"), ("box", "buy the napkins", "nobody comes for them", "paper"), ("recipe", "a classic recipe", "free, but you still cook", "y")]):
    x = 20 + i * 250
    bb_analogy.icon(ic, x + 80, 20, 1.1)
    bb_analogy.box(x, 106, 220, 84, t, f, sub=s, size=17)
bb_analogy.note(380, 240, "build what makes you different", "green")

bb_how = Doodle(760, 340, "How Larder sorts build, buy and open source. First question: does it make customers choose us? If yes, build it: it's core. If not, is there a good product for it? If yes, buy it; if not, use open source or build something small. Larder in June 2026: core, so built, are substitution approvals, courier assignment rules and a city as configuration. Context, so bought, are invoicing (ADR 0013), the helpdesk, warehouse management (StockPilot) and card payments.",
                "Core gets built. Context gets bought. Open source is a third option with its own running costs.")
bb_how.box(20, 20, 340, 70, "makes customers choose us?", "y", size=16)
bb_how.arrow(95, 94, 95, 136, color="green", label="yes", lx=108, ly=122, anchor="start")
bb_how.box(20, 140, 150, 64, "build", "green", sub="it's core")
bb_how.arrow(285, 94, 285, 136, color="red", label="no", lx=298, ly=122, anchor="start")
bb_how.box(200, 140, 170, 64, "good product?", "y", size=15)
bb_how.arrow(245, 208, 235, 246, label="yes", lx=226, ly=232, anchor="end")
bb_how.box(180, 250, 90, 56, "buy", "blue", size=18)
bb_how.arrow(325, 208, 335, 246, label="no", lx=342, ly=232, anchor="start")
bb_how.box(280, 250, 100, 56, "OSS", "paper", sub="or small", size=16, subsize=13)
bb_how.head(580, 40, "Larder, June 2026", size=17)
bb_how.head(420, 80, "core → build", anchor="start", size=16, color="green")
for i, t in enumerate(["substitution approvals", "courier assignment rules", "a city as configuration"]):
    bb_how.text(436, 108 + i * 26, t, anchor="start", size=15)
bb_how.head(420, 200, "context → buy", anchor="start", size=16)
for i, t in enumerate(["invoicing (ADR 0013)", "helpdesk", "warehouse (StockPilot)", "card payments (PSP)"]):
    bb_how.text(436, 228 + i * 26, t, anchor="start", size=15)

BUILD_BUY = dict(
    slug="build-vs-buy",
    kicker="a.k.a. “bake the bread, buy the napkins”",
    tldr="For every capability, ask first: <b>does this make customers choose us?</b> If yes, it's <b>core</b>: build it and own it. If not, it's <b>context</b>: <b>buy</b> a good product if one exists. <b>Open source</b> is a third option: no licence fee, but you run, upgrade and secure it yourself. Compare the options on <b>total cost over three years</b> (not the first sprint), on fit with your constraints, and on how you'd <b>leave</b>. Most of the iceberg is under the water.",
    chips=[("Family", "big choices"), ("Origin", "Geoffrey Moore, “core vs context” (<i>Dealing with Darwin</i>, 2005); Wardley mapping"), ("Lives in", "an ADR with a three-year cost table"), ("Pairs with", "options analysis, technology evaluation, exit plans")],
    problem_side="Larder, 8 June 2026",
    problem="""  <p class="lead">Korenwolf's pilot is going well, and Mo hopes for a three-office contract in September. But the <b>May invoice</b> took Mo and Marco <b>six hours</b> in a spreadsheet and had <b>two VAT errors</b> (the pantry goods at 9 %, the coffee-machine rental at 21 %). Ruben, Korenwolf's procurement lead, already wants invoices <b>per office and per cost centre</b>. Ben offers to build an invoicing module “in two sprints”. Ana has seen this before: <span class="hl-pink">invoicing is an iceberg</span>.</p>
  <ul>
    <li>Building looks cheap because only the first version is estimated.</li>
    <li>Credit notes, numbering rules, reminders and Belgian e-invoicing (needed for Antwerp) are under the water.</li>
    <li>Every engineer-week on invoicing is a week not spent on what makes Larder win.</li>
  </ul>""",
    problem_figs=[bb_problem],
    analogy_side="the restaurant",
    analogy="""  <p>A good restaurant <b>bakes its own bread</b>: it's what guests remember. It <b>buys the napkins</b>: nobody comes for the napkins, and a supplier makes them better and cheaper. And it might use a <b>classic recipe from a book</b>: the recipe is free, but the kitchen still has to cook it, every night.</p>""",
    analogy_figs=[bb_analogy],
    map=[("The bread guests come for", "Core: substitution approvals, courier assignment, city configuration"),
         ("The napkins", "Context: invoicing, helpdesk, warehouse management"),
         ("Buying from a supplier", "A SaaS product with a contract and an exit plan"),
         ("A free recipe you still cook", "Open source: no licence, but hosting, upgrades and security are yours"),
         ("The cost of the whole year's cooking", "Three-year total cost, not the first sprint")],
    how_side="core or context, then cost over three years",
    how="""  <p>Invoicing doesn't make anyone choose Larder; on-time express and honest substitutions do. Good billing products exist, EU-hosted, with Dutch and Belgian VAT and e-invoicing built in. So <b>buy</b> (ADR 0013): Larder keeps the data about <b>what was delivered</b> and sends it to the billing service; the service owns invoices, VAT and reminders.</p>""",
    how_figs=[bb_how],
    steps=[("Ask the core question", "Would customers notice, and choose us for it? If yes, it's core: lean towards building."),
           ("Look for a good product", "For context: is there a product that fits the constraints (EU data, Belgian VAT, an API)?"),
           ("Cost three years, all options", "Build: first version + upkeep + the people. Buy: fees + integration. Open source: hosting + upgrades + security."),
           ("Check fit and lock-in", "Constraints, data ownership, the API, the contract term, and how you'd leave."),
           ("Decide the seam", "What you keep (the facts of the business) and what the product owns (invoices, VAT)."),
           ("Record it, with an exit", "ADR with the cost table; an exit plan before signing.")],
    vocab=[("Core", "What makes customers choose you: worth building and owning."),
           ("Context", "Necessary, but not why customers choose you: buy it."),
           ("Total cost of ownership", "All the costs over the life of a choice, not just the start."),
           ("Open source", "Free to use and change; you still run, upgrade and secure it."),
           ("Seam", "The boundary between what you own and what the product owns."),
           ("Lock-in", "How costly it is to leave a product later.")],
    code=dict(file="docs/adr/0013-buy-business-billing.md", note="build/buy/open-source table from ADR 0013", plain=True, src="""
# 13. Buy a billing service for Larder for Business invoices
Status: Accepted · 2026-06-08 · Approver: Marco · Driver: Ana · with Mo, Ben, Lena

Core or context?  Context. No customer chooses Larder for its invoices.
Must-haves       EU-hosted data · NL and BE VAT · Peppol e-invoicing (BE) ·
                 invoices per office / cost centre · API · monthly data export

                          Build (Core module)   Buy (billing SaaS)   Open source (self-hosted)
First version             12 wks × 2 eng ≈ €70k  setup + API ≈ €12k   4 wks × 2 eng ≈ €23k
Running, per year         upkeep ≈ €14k         €7.2k fees           hosting + upgrades ≈ €12k
VAT / Peppol changes      ours                  vendor's             ours (community helps)
3-year total              ≈ €112k               ≈ €34k               ≈ €59k
Ready for Korenwolf (Sep) tight                 yes                  yes, if no surprises

Decision   Buy. Larder Core keeps "what was delivered" and sends it monthly;
           the billing service owns invoices, VAT, numbering and reminders.
Exit       Monthly export of invoices and customers; 3-month notice. See exit plan.
Revisit    If invoicing ever becomes part of what we sell (e.g. budgets for clients).
"""),
    tools="tools: a cost table in the ADR. For seeing what's core: Wardley maps, capability maps (Vol. 4). For vendors: reference calls, trial accounts, the security questionnaire, and Lena reading the data-processing agreement.",
    gains=["<b>Engineers on what matters</b>: the core, not invoices.",
           "<b>Honest costs</b>: three years, not two sprints.",
           "<b>Expertise bought in</b>: the vendor tracks VAT and e-invoicing rules.",
           "<b>Faster</b>: ready for Korenwolf's contract in September.",
           "<b>A clear seam</b>: Larder owns its business facts."],
    losses=["<b>Fees forever</b>, rising with volume.",
            "<b>Lock-in</b>: the vendor's roadmap and prices.",
            "<b>Less control</b> over features and outages.",
            "<b>Integration work</b> still lands on the team."],
    baseline="Each line compares <b>building by default because the first version looks quick</b> to <b>sorting core from context and comparing build, buy and open source over three years</b>.",
    ratings=[(3, 4, "Core vs context explains why each part is built or bought."),
             (2, 4, "Finance, product and engineering see the same cost table."),
             (3, 4, "A clear question settles most cases quickly."),
             (2, 4, "Hidden work and lock-in are on the table before signing."),
             (3, 3, "Buying adds lock-in; the exit plan limits it."),
             (2, 4, "The ADR keeps the cost table and the reasoning."),
             (2, 5, "Three-year costs for every option."),
             (3, 4, "A day of work for a decision worth tens of thousands."),
             (3, 3, "Bought tools need a team to own the integration.")],
    pitfalls=[("Estimating the tip", "“Two sprints” for invoicing.", "estimate upkeep and the rules under the water; cost three years."),
              ("Buying the core", "Outsourcing what makes customers choose you.", "build the differentiator, even if a product exists."),
              ("“Open source is free”", "No licence, but nobody budgeted for upgrades.", "cost hosting, upgrades and security like any other option."),
              ("No seam", "The vendor becomes the source of truth for your business facts.", "keep your own data; send the vendor what it needs.")],
    use=["Any new capability that a product might cover.",
         "When an engineer says “we can build that in two sprints”.",
         "Before signing a multi-year vendor contract.",
         "Reviewing whether old in-house tools are still core."],
    skip=["Tiny utilities: a library choice, not a build-vs-buy.",
          "When a constraint rules out all but one option."],
    related=["<b>Options analysis</b> (this volume)", "<b>Technology evaluation</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (this volume)", "<b>Total cost of ownership</b> (Vol. 5)"],
    quiz=[("What's the first question to ask?", "Does this make customers choose us? If yes it's core: build. If not, it's context: buy if a good product exists."),
          ("Why compare over three years?", "Building looks cheap at the start; upkeep and changing rules dominate later."),
          ("What does open source cost?", "No licence fee, but hosting, upgrades, security and expertise are yours."),
          ("When buying, what should you keep?", "Your own business facts (here: what was delivered), sent to the product, plus an exit plan.")],
    try_it="List five capabilities your system has or needs. Mark each core or context with your product owner. For one context capability you currently build, make a three-year cost table for build, buy and open source, and show it to whoever owns the budget.",
    remember="Bake the <span class=\"hl\">bread</span>; buy the <span class=\"hl\">napkins</span>. And cost the whole iceberg.",
    sources=["Geoffrey Moore, <i>Dealing with Darwin</i> (2005), core vs context.",
             "Simon Wardley, <i>Wardley Maps</i> (2016–), on build, buy and outsource by evolution stage.",
             "Gregor Hohpe, <i>Cloud Strategy</i> (2020), on buying and lock-in.",
             "Martin Fowler, “Utility vs Strategic Dichotomy” (martinfowler.com, 2010)."],
)

# ------------------------------------------------------------------ 10 Technology Evaluation
te_problem = Doodle(760, 290, "Doodle of the routing engine choice in May 2026. Eli wants the engine from a conference talk, Ben wants to write their own, Marco wants whatever's cheapest. Ana remembers 2025, when a search-engine 'look' ran for three weeks without a decision.",
                    "Three favourites from a talk, a hunch and a budget, and the memory of a look that never ended.")
for i, (who, says, f) in enumerate([("Eli", "“the one from that talk”", "blue"), ("Ben", "“let's write our own”", "y"), ("Marco", "“whatever's cheapest”", "paper")]):
    te_problem.box(20, 20 + i * 76, 330, 62, who, f, sub=says, size=17)
te_problem.box(400, 40, 340, 180, None, "pink", stroke="red")
te_problem.head(570, 76, "2025: the search-engine “look”", size=15, color="red")
te_problem.text(570, 120, "no question, no criteria", size=16)
te_problem.text(570, 150, "3 weeks, no decision", size=16)
te_problem.icon("hourglass", 558, 168, 1.2)
te_problem.note(380, 276, "Dispatch needs a routing engine by July", "pen")

te_analogy = Doodle(760, 290, "Doodle of buying a used car as a funnel: twenty ads, three cars worth viewing, one test drive on your own commute rather than the dealer's route, a mechanic's check, then one car.",
                    "Buying a used car: from twenty ads to one, and the test drive is on your own commute.")
for i, (t, w, f) in enumerate([("20 ads", 560, "paper"), ("3 worth viewing", 440, "y"), ("test drive: your own commute", 340, "blue"), ("1 car", 180, "green")]):
    te_analogy.box(380 - w / 2, 24 + i * 60, w, 48, t, f, size=16)
te_analogy.note(120, 160, "not the dealer's", "red", size=18)
te_analogy.note(120, 184, "route", "red", size=18)
te_analogy.note(650, 280, "+ a mechanic's check", "pen", size=18)

te_how = Doodle(760, 340, "Larder's routing engine evaluation, 11 to 22 May 2026. Seven candidates on the long list; must-haves (EU hosting, e-bike profiles, under 2 seconds for 300 couriers) leave four; documentation and a demo leave three; a bake-off replays Friday 8 May's Amsterdam peak; Engine A wins. Scorecard: p95 for 300 couriers: A 1.4 s, B 0.9 s, C 1.1 s. On time in simulation: 93, 94 and 93 percent. Team can run it: A yes, B weak, C yes. Cost per month at six cities: 300, 300 and 4,800 euros. Criteria were set before the bake-off; decided 26 May in ADR 0012.",
                "Funnel down with must-haves, then a bake-off on your own data, scored on criteria set before anyone ran it.")
for i, (t, w, f) in enumerate([("7 on the long list", 310, "paper"), ("must-haves → 4", 280, "y"), ("docs + demo → 3", 250, "y"), ("bake-off, our data", 220, "blue"), ("Engine A", 180, "green")]):
    te_how.box(175 - w / 2, 16 + i * 62, w, 50, t, f, size=15)
for name, x in [("A", 560), ("B", 635), ("C", 710)]:
    te_how.head(x, 40, name, size=19)
for i, (crit, vals) in enumerate([("p95, 300 couriers", ("1.4 s", "0.9 s", "1.1 s")), ("on time (sim.)", ("93 %", "94 %", "93 %")),
                                  ("team can run it", ("yes", "weak", "yes")), ("€/month, 6 cities", ("300", "300", "4,800"))]):
    y = 84 + i * 46
    te_how.text(360, y, crit, anchor="start", size=14)
    for (x, v) in zip((560, 635, 710), vals):
        te_how.text(x, y, v, "t t-red" if v in ("weak", "4,800") else "t", size=14)
te_how.box(530, 56, 60, 180, None, "green", dash=True, rx=6)
te_how.note(548, 300, "criteria set before the bake-off", "pen", size=17)
te_how.note(548, 326, "decided 26 May · ADR 0012", "green", size=17)

TECH_EVAL = dict(
    slug="technology-evaluation",
    kicker="a.k.a. “test-drive it on your own commute”",
    tldr="Choosing a technology from blog posts, conference talks or vendor demos picks the best-<i>marketed</i> option. Instead, <b>funnel</b>: a <b>long list</b>, cut by <b>must-haves</b> to a <b>shortlist</b> of two or three, then a <b>bake-off on your own data and load</b>. Write the <b>criteria and their weights before</b> anyone runs anything, <b>timebox</b> it (two weeks is plenty), include the people who'll <b>run it</b>, and end with an ADR.",
    chips=[("Family", "big choices"), ("Origin", "vendor selection practice; ThoughtWorks' radar process; benchmarking discipline"), ("Lives in", "an evaluation card and the ADR it ends with"), ("Pairs with", "build vs buy, spike vs prototype vs PoC, technology radar")],
    problem_side="Larder, 11 May 2026",
    problem="""  <p class="lead">Rotterdam opened on 27 April with the new Dispatch service, still running the old assignment loop every 30 seconds. Express on time is <b>89 % in Amsterdam</b> and <b>84 % in Rotterdam</b>; the target is 95 %. Dispatch needs a real <b>routing engine</b> by July. <b>Eli</b> wants the one from a conference talk; <b>Ben</b> wants to write their own; <b>Marco</b> wants whatever's cheapest. And Ana remembers the 2025 search-engine “look” that ran for <span class="hl-pink">three weeks without a decision</span>.</p>
  <ul>
    <li>Talks and demos show the best case, on someone else's data.</li>
    <li>Without criteria set in advance, the evaluation ends in a debate, or never ends.</li>
    <li>The people who'll run it at 3 a.m. are often not asked.</li>
  </ul>""",
    problem_figs=[te_problem],
    analogy_side="buying a used car",
    analogy="""  <p>You start with <b>twenty ads</b>, drop the ones that fail your must-haves (too small, too old), view <b>three</b>, and <b>test-drive</b> the best on <b>your own commute</b>, not the dealer's smooth route. A mechanic checks what you can't see. Then you buy one, and you decided what mattered before you fell for the colour.</p>""",
    analogy_figs=[te_analogy],
    map=[("Twenty ads", "The long list: seven engines and services"),
         ("Too small, too old", "Must-haves: EU hosting, e-bike profiles, under 2 s for 300 couriers"),
         ("Three worth viewing", "The shortlist: Engine A, B and Service C"),
         ("Test drive on your commute", "A bake-off replaying Larder's own Friday peak"),
         ("The mechanic", "Eli and the on-call engineers judging what it takes to run")],
    how_side="funnel, then a bake-off on your data",
    how="""  <p>The evaluation took <b>two weeks</b>: two days for the long list and must-haves, three for docs and demos, and a week-long <b>bake-off</b> replaying Friday 8 May's Amsterdam peak at 300 couriers. Engine B was fastest, but nobody in the team could maintain its solver model. Service C was good and costly at six-city volume. <b>Engine A</b> won (ADR 0012).</p>""",
    how_figs=[te_how],
    steps=[("Write the question and criteria first", "Must-haves (pass/fail) and weighted criteria, agreed with the approver, before looking at products."),
           ("Long list, fast", "Five to ten candidates from colleagues, the radar, analysts, open source. An afternoon."),
           ("Cut with must-haves", "Anything failing a must-have is out, however good its demo."),
           ("Shortlist two or three", "Read the docs, see a demo, ask a reference customer."),
           ("Bake-off on your data", "Same data, same load, same hardware for each; involve the people who'll run it. Timebox a week."),
           ("Score, decide, record", "Fill the scorecard, decide, write the ADR; add the winner to the radar as “trial”.")],
    vocab=[("Long list", "Every plausible candidate, before filtering."),
           ("Must-have", "A pass/fail criterion; failing it rules a candidate out."),
           ("Shortlist", "Two or three candidates worth testing properly."),
           ("Bake-off", "Testing the shortlist side by side on your own data and load."),
           ("Scorecard", "The weighted criteria with each candidate's results."),
           ("Reference call", "Talking to another customer who runs it.")],
    code=dict(file="docs/evaluations/2026-05-routing-engine.md", note="evaluation card, filled in", plain=True, src="""
# Evaluation: routing engine for Dispatch                    11–22 May 2026
Question   Which engine assigns orders to couriers best for six cities?
Owner      Eli (+ Ben, Dee for the courier app)     Approver: Ana · timebox 2 weeks

Must-haves  EU hosting or self-hosted · e-bike and walking profiles ·
            p95 < 2 s for 300 couriers (QAS from Vol. 1 PoC) · licence OK for SaaS use
Long list   7 → must-haves → 4 → docs, demo, reference call → 3

Bake-off    Replay of Fri 8 May, Amsterdam, 17:00–19:30, scaled to 300 couriers
                                    weight   Engine A   Engine B   Service C
p95 assignment time                   3      1.4 s      0.9 s      1.1 s
on time in simulation                 5      93 %       94 %       93 %
team can run and change it            4      yes        weak       yes
cost / month at 6 cities              3      €300       €300       €4,800
exit: how hard to leave               2      easy       easy       medium
Weighted (1–5 scores)                        58         55         49

Decision   Engine A, self-hosted on the container service. → ADR 0012 (26 May)
Radar      Engine A → "trial".  Service C kept as plan B if A misses 93 % on time.
"""),
    tools="tools: an evaluation card in the repo; load-test tools for the bake-off (k6, Locust); recorded production data for replays. Analyst reports and vendor comparisons are fine for the long list, never for the decision.",
    gains=["<b>Decisions on your data</b>, not on demos.",
           "<b>Ends on time</b>: a timebox and criteria set in advance.",
           "<b>Operators have a say</b> before they inherit it.",
           "<b>A plan B</b>: the runner-up is already tested.",
           "<b>Defensible</b>: the scorecard explains the choice."],
    losses=["<b>Two weeks</b> of several people's time.",
            "<b>Replays aren't production</b>: surprises remain.",
            "<b>Vendors push back</b> on bake-offs, or tune for them.",
            "<b>Over-engineering</b> for small choices."],
    baseline="Each line compares <b>choosing from talks, demos and favourites</b> to <b>a timeboxed funnel ending in a bake-off on your own data, scored against criteria set in advance</b>.",
    ratings=[(2, 4, "The card shows what was tested and why A won."),
             (2, 4, "Criteria agreed before testing; no favourite wins by default."),
             (2, 4, "Two weeks, then a decision; not three weeks of “looking”."),
             (2, 5, "Real data exposes problems demos hide."),
             (3, 4, "The runner-up is a tested plan B."),
             (2, 5, "Scorecard and ADR record the evidence."),
             (2, 4, "Cost at six-city volume is a scored criterion."),
             (4, 2, "Real effort: worth it only for big choices."),
             (2, 4, "The team that runs it does the evaluation.")],
    pitfalls=[("Criteria after results", "The weights shift once the favourite is behind.", "write and agree criteria before the bake-off."),
              ("The vendor's data", "Benchmarks on the vendor's demo dataset.", "replay your own peak, at your target scale."),
              ("No timebox", "One more candidate, one more week.", "two weeks, then decide with what you have."),
              ("Operators left out", "The winner is fast and nobody can run it.", "the on-call team scores “can we run it”.")],
    use=["Platforms, engines and services you'll live with for years.",
         "When people already have favourites from talks.",
         "When cost or performance at scale is uncertain.",
         "Before a multi-year contract."],
    skip=["Small libraries inside one module: pick one, it's a two-way door.",
          "When one option is the obvious standard and nobody objects."],
    related=["<b>Build vs buy vs open source</b> (this volume)", "<b>Technology radar</b> (this volume)", "<b>Spike vs prototype vs PoC</b> (Vol. 1)", "<b>Load profiles</b> (Vol. 5)"],
    quiz=[("What must be written before the bake-off?", "The question, must-haves and weighted criteria, agreed with the approver."),
          ("Why test on your own data?", "Demos and vendor benchmarks show the best case on someone else's data."),
          ("What happens to the runner-up?", "It's a tested plan B, noted in the ADR."),
          ("Who should score “can we run it”?", "The people who'll operate it, e.g. the on-call engineers.")],
    try_it="Pick a technology your team is about to choose. Write the must-haves and four weighted criteria before looking at any product, and get your lead to agree them. Then design a one-week bake-off on a copy of your own data. Compare it with how the choice would have been made otherwise.",
    remember="Decide what matters <span class=\"hl\">before</span> the viewing; test-drive on <span class=\"hl\">your own commute</span>.",
    sources=["ThoughtWorks, “Build your own Technology Radar” (2016–), on evaluation rings.",
             "Brendan Gregg, <i>Systems Performance</i>, 2nd ed. (2020), on benchmarking pitfalls.",
             "Gartner and Forrester vendor-selection guides (for long lists only).",
             "Michael Nygard, <i>Release It!</i>, 2nd ed. (2018), on what operating a system really takes."],
)

# ------------------------------------------------------------------ 11 Choosing a Cloud Service Model
cs_problem = Doodle(760, 290, "Doodle of the April 2026 debate about where the new Dispatch service runs. Eli proposes Kubernetes: we'll need it eventually. Ben proposes functions: serverless, pay per use. Underneath, the real question: who runs it at 3 a.m.? Larder has one platform engineer, Eli.",
                    "Two fashionable answers, and the question nobody asked: who runs it at 3 a.m.?")
cs_problem.box(20, 30, 340, 80, "Eli: Kubernetes", "blue", sub="“we'll need it eventually”")
cs_problem.box(400, 30, 340, 80, "Ben: functions", "y", sub="“serverless, pay per use”")
cs_problem.arrow(190, 116, 330, 166, dash=True)
cs_problem.arrow(570, 116, 430, 166, dash=True)
cs_problem.box(170, 170, 420, 70, "who runs it at 3 a.m.?", "pink", sub="one platform engineer: Eli", stroke="red")
cs_problem.icon("clock", 640, 176, 0.9)
cs_problem.note(380, 274, "Dispatch: 300 phones, a location every 5 s, always on", "pen", size=18)

cs_analogy = Doodle(760, 280, "Doodle of 'pizza as a service' in four columns. Home-made: you make the dough and sauce, bake it and set the table. Take and bake: the shop makes dough and sauce, you bake and set the table. Delivery: the shop does everything except your table. Dine out: they do everything.",
                    "Pizza as a service: the more they do, the less you control, and the less you have to do.")
layers = ["dough", "sauce", "oven", "table"]
for i, (name, mine) in enumerate([("home-made", 4), ("take & bake", 2), ("delivery", 1), ("dine out", 0)]):
    x = 30 + i * 182
    cs_analogy.head(x + 75, 34, name, size=16)
    for r, layer in enumerate(layers):
        you = r >= 4 - mine
        cs_analogy.box(x, 52 + r * 42, 150, 34, layer, "y" if you else "blue", size=14, rx=6)
cs_analogy.box(190, 240, 22, 16, None, "y", rx=3)
cs_analogy.text(220, 254, "you", anchor="start", size=15)
cs_analogy.box(420, 240, 22, 16, None, "blue", rx=3)
cs_analogy.text(450, 254, "the shop", anchor="start", size=15)

cs_how = Doodle(760, 320, "The same stack for running Dispatch. Virtual machines: Larder runs code, scaling and the operating system; patching by hand. Managed Kubernetes: Larder runs code, scaling and much of the cluster; too much for one engineer. Managed containers, serverless: Larder runs only the code and a few scaling settings; this fits Dispatch. Functions: Larder runs only small pieces of code, but they can't hold the courier phones' always-on location streams. Decision 8 April 2026, ADR 0010: managed containers.",
                "How much do we run ourselves? For Dispatch, with one platform engineer: only the code. ADR 0010.")
rows = ["code", "scaling", "OS / cluster", "hardware"]
for i, (name, sub, mine, fit, ok) in enumerate([("VMs", "IaaS", 3, "patch by hand", False), ("Kubernetes", "managed K8s", 2.5, "too much for one", False),
                                                ("containers", "serverless", 1, "✓ fits Dispatch", True), ("functions", "FaaS", 1, "✗ 5 s streams", False)]):
    x = 20 + i * 185
    if ok:
        cs_how.box(x - 6, 14, 182, 254, None, "paper", stroke="green", dash=True, rx=12)
    cs_how.head(x + 85, 30, name, size=17, color="green" if ok else "")
    cs_how.text(x + 85, 52, sub, "t t-soft", size=13)
    for r, layer in enumerate(rows):
        fill = "y" if r < int(mine) else ("pink" if r < mine else "blue")
        cs_how.box(x, 66 + r * 40, 170, 34, layer, fill, size=14, rx=6)
    cs_how.note(x + 85, 254, fit, "green" if ok else "red", size=17)
for x, f, t in [(150, "y", "we run it"), (330, "pink", "shared"), (490, "blue", "the provider runs it")]:
    cs_how.box(x, 284, 22, 16, None, f, rx=3)
    cs_how.text(x + 30, 298, t, anchor="start", size=15)

CLOUD = dict(
    slug="cloud-service-model",
    kicker="a.k.a. “pizza as a service”",
    tldr="The cloud offers the same thing at different levels: <b>virtual machines</b> (IaaS), <b>Kubernetes</b>, <b>managed or serverless containers</b>, <b>functions</b> (FaaS), <b>platforms</b> (PaaS) and finished <b>SaaS</b>. Each step up, the provider runs more and you control less. Choose by <b>the workload's shape</b> (always on? long connections? spiky?) and, above all, by <b>who will run it at 3 a.m.</b>: pick the <b>highest level that fits</b>, and step down only for a reason you can name.",
    chips=[("Family", "big choices"), ("Origin", "NIST definition of cloud computing (2011); “pizza as a service” (Albert Barron, 2014)"), ("Lives in", "an ADR per workload"), ("Pairs with", "build vs buy, team topologies, total cost of ownership")],
    problem_side="Larder, 6 April 2026",
    problem="""  <p class="lead">RFC-003 is accepted: Dispatch becomes its own service. Where does it run? <b>Eli</b> proposes managed <b>Kubernetes</b>: “we'll need it eventually”. <b>Ben</b> proposes <b>functions</b>: “serverless, pay per use”. Both are in fashion. But Larder has <span class="hl-pink">one platform engineer</span>, Eli, who already patches Larder Core's virtual machines by hand. Dispatch must hold connections from <b>300 courier phones</b>, each sending a location <b>every 5 seconds</b>, all evening.</p>
  <ul>
    <li>Platforms chosen for the future team leave today's team on call for them.</li>
    <li>Fashion picks the level, not the workload.</li>
    <li>The running cost that matters most is people's time, and it's rarely in the comparison.</li>
  </ul>""",
    problem_figs=[cs_problem],
    analogy_side="pizza as a service",
    analogy="""  <p>Pizza for dinner: <b>home-made</b> (you do it all), <b>take and bake</b> (they make it, you bake it), <b>delivery</b> (you set the table), or <b>dine out</b> (they do everything). Each step up you control less, pay more per pizza, and do far less. On a busy Tuesday, nobody kneads dough to prove they could.</p>""",
    analogy_figs=[cs_analogy],
    map=[("Home-made", "Virtual machines: you run the OS, patches, scaling"),
         ("Take and bake", "Managed Kubernetes: you run workloads and much of the cluster"),
         ("Delivery", "Managed or serverless containers: you run your code"),
         ("Dine out", "SaaS: someone else runs the whole thing"),
         ("A busy Tuesday", "A team of 14 with one platform engineer")],
    how_side="the highest level that fits the workload",
    how="""  <p>Functions are cheap for spiky, short work, but can't hold long-lived connections well. Kubernetes can do everything, and needs people to run it. <b>Managed containers</b> run Dispatch's always-on service, scale with cities, and leave Eli only the code and a few settings (ADR 0010, 8 April). Revisit when Larder runs more than five services or needs something the container service can't do.</p>""",
    how_figs=[cs_how],
    steps=[("Describe the workload", "Always on or spiky? Long connections? State? Start-up time? Peak vs average."),
           ("Count who runs it", "Who's on call, what they know, how many hours a week they have for it."),
           ("Start at the top", "SaaS if it's context. Then PaaS or serverless containers. Then functions for spiky, short jobs."),
           ("Step down only for a reason", "A named need (long connections, GPUs, special networking) justifies more control."),
           ("Compare total cost", "Provider bill + people's time + the cost of moving later."),
           ("Write the ADR with a trigger", "“Revisit when we run more than five services” or “if we need X”.")],
    vocab=[("IaaS", "Infrastructure as a service: virtual machines; you run the rest."),
           ("Kubernetes", "A container platform; powerful, and needs running."),
           ("Serverless containers", "Run a container image; the provider runs servers and scaling."),
           ("FaaS", "Functions as a service: small pieces of code run per event."),
           ("PaaS", "Platform as a service: push code, the platform runs it."),
           ("Operational load", "The people-time a platform needs to stay healthy.")],
    code=dict(file="docs/adr/0010-dispatch-on-managed-containers.md", note="ADR 0010, the decision table", plain=True, src="""
# 10. Run Dispatch on the managed container service
Status: Accepted · 2026-04-08 · Driver: Eli · Approver: Ana · with Ben, Marco

Workload   always on 07:00–23:00 · 300 courier phones send a location every 5 s
           (≈ 60 msgs/s, long-lived connections) · grows with each city
People     one platform engineer (Eli); on-call rota of 5 from June

                     VMs          Managed K8s     Managed containers   Functions
Long connections     yes          yes             yes                  poor (timeouts)
We run               OS, patches  cluster, nodes  code + settings      code
Ops hours / week     ~6           ~8              ~1                   ~1
Bill / month (est.)  €450         €700            €520                 €300
Moving later         hard         medium          easy (it's a         hard (code
                                                  container)           shaped to it)

Decision   Managed containers, in the EU region (Frankfurt), same as Core.
Revisit    More than 5 services, or a need the service can't meet → consider K8s.
"""),
    tools="tools: whatever your cloud calls these levels: virtual machines, managed Kubernetes, serverless containers (e.g. Cloud Run, Fargate, Container Apps), functions, app platforms. Infrastructure as code (patterns Vol. 6) for each.",
    gains=["<b>Less to run</b>: the team's hours go to the product.",
           "<b>Fit for the workload</b>: long connections, spikes, state.",
           "<b>Honest cost</b>: people's time counted with the bill.",
           "<b>Easier to move</b> when the unit is a standard container.",
           "<b>A trigger</b> says when to step down a level."],
    losses=["<b>Less control</b>: limits and features are the provider's.",
            "<b>Higher unit price</b> at large scale.",
            "<b>Provider-specific settings</b> creep in.",
            "<b>Mixed levels</b> across services can confuse newcomers."],
    baseline="Each line compares <b>picking the fashionable platform, or the one for the future team</b> to <b>the highest service level that fits the workload and the people who'll run it</b>.",
    ratings=[(3, 4, "The ADR explains the level per workload."),
             (3, 3, "Mostly an engineering choice; finance sees the cost table."),
             (3, 4, "A clear rule: highest level that fits."),
             (2, 4, "Fewer moving parts to fail at 3 a.m."),
             (3, 4, "Containers move between levels more easily."),
             (3, 4, "Trigger and reasons recorded."),
             (2, 5, "Bill and people-time compared side by side."),
             (2, 4, "Less platform to run."),
             (3, 4, "Teams deploy without a platform specialist.")],
    pitfalls=[("Building for the future team", "Kubernetes for 14 engineers “because we'll grow”.", "choose for the team you have; set a trigger for the one you'll have."),
              ("Ignoring the workload", "Functions for long-lived connections.", "describe the workload's shape first."),
              ("Bill only", "The cheapest bill, with eight hours a week of care.", "count people's time in the cost."),
              ("Deep lock-in", "Code shaped around one provider's functions.", "prefer standard units (containers) when moving matters.")],
    use=["Every new service or workload.",
         "When a team proposes a new platform.",
         "When ops load is crowding out product work.",
         "Reviewing costs at a new scale."],
    skip=["When the organisation already has a mature platform team and golden path: use it.",
          "SaaS decisions: that's build vs buy."],
    related=["<b>Build vs buy vs open source</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (this volume)", "<b>Golden paths</b> (Vol. 6)", "<b>Infrastructure as code</b> (patterns, Vol. 6)"],
    quiz=[("What changes as you move from VMs to SaaS?", "The provider runs more; you control less and run less."),
          ("Why were functions a poor fit for Dispatch?", "Dispatch holds long-lived connections from 300 phones; functions handle short, event-driven work."),
          ("What cost is often left out of the comparison?", "People's time to run the platform."),
          ("What's the rule of thumb?", "Pick the highest level that fits the workload; step down only for a named reason.")],
    try_it="For one service you run, list the layers you operate yourselves (OS, cluster, scaling, runtime) and estimate the hours each takes per month. Then ask: which level would remove the most hours without breaking the workload's needs? Write it as a one-page ADR draft with a revisit trigger.",
    remember="On a busy Tuesday, order <span class=\"hl\">delivery</span>. Knead the dough only for a <span class=\"hl\">reason</span>.",
    sources=["NIST SP 800-145, “The NIST Definition of Cloud Computing” (2011).",
             "Albert Barron, “Pizza as a Service” (LinkedIn, 2014).",
             "Gregor Hohpe, <i>Cloud Strategy</i> (2020).",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019), on cognitive load."],
)

# ------------------------------------------------------------------ 12 Technology Radar
tr_problem = Doodle(760, 290, "Doodle of Ana's inbox in May 2026, after four new engineers joined. Eleven separate questions of the form 'can I use X?': Go for a small tool, a second message queue library, MongoDB for business orders, a new date library. Each gets a different answer depending on the day.",
                    "Eleven “can I use X?” messages in one month, each answered differently, depending on the day.")
for i, t in enumerate(["“can I use Go for a small tool?”", "“a second queue library?”", "“MongoDB for business orders?”", "“this new date library?”"]):
    tr_problem.box(20 + (i % 2) * 14, 24 + i * 52, 340, 42, t, "paper", size=14, rx=6)
    tr_problem.arrow(366 + (i % 2) * 14, 45 + i * 52, 486, 130, dash=True)
tr_problem.box(490, 80, 250, 100, "Ana's inbox", "y", sub="11 in May")
tr_problem.note(380, 272, "4 new engineers · no shared answer", "red")

tr_analogy = Doodle(760, 290, "Doodle of a household pantry list on the fridge with four shelves: always stocked (rice, olive oil); trying this month (oat milk); heard about it (that new hot sauce); we don't buy any more (the cheap coffee). Anyone doing the shopping knows what to buy without asking.",
                    "The pantry list on the fridge: whoever shops knows what to buy, what to try and what to skip.")
for i, (shelf, items, f) in enumerate([("always stocked", "rice · olive oil · pasta", "green"), ("trying this month", "oat milk", "y"), ("heard about it", "that new hot sauce", "paper"), ("don't buy any more", "the cheap coffee", "pink")]):
    y = 30 + i * 60
    tr_analogy.box(20, y, 260, 46, shelf, f, size=16)
    tr_analogy.line(f"M300 {y + 40} H740", thin=True)
    tr_analogy.text(320, y + 30, items, anchor="start", size=17)

tr_how = Doodle(760, 350, "Larder's first technology radar, June 2026. Four rings from the centre: adopt, trial, assess, hold. Four quadrants: techniques, tools, platforms, and languages and frameworks. Adopt: ADRs, the transactional outbox, Postgres, Python and Django, React Native. Trial: RFCs, managed Kafka, routing Engine A, managed containers. Assess: a feature-flag service, change data capture, Go for small tools. Hold: Kafka writes inside request handlers, and a second database type without an ADR.",
                "Four rings, four quadrants, fourteen blips, one page. Refreshed every six months.")
cx, cy = 240, 178
for r, f in [(150, "pink"), (125, "paper"), (95, "y"), (60, "green")]:
    tr_how.circle(cx, cy, r, fill=f)
tr_how.line(f"M{cx - 156} {cy} H{cx + 156}", thin=True)
tr_how.line(f"M{cx} {cy - 156} V{cy + 156}", thin=True)
for name, rr in [("adopt", 48), ("trial", 80), ("assess", 110), ("hold", 140)]:
    tr_how.text(cx - 4, cy - rr + 5, name, "t t-soft", anchor="end", size=12)
tr_how.note(20, 24, "techniques", "pen", anchor="start", size=17)
tr_how.note(460, 24, "tools", "pen", anchor="end", size=17)
tr_how.note(20, 344, "platforms", "pen", anchor="start", size=17)
tr_how.note(460, 344, "languages, frameworks", "pen", anchor="end", size=17)
for num, bx, by in [(1, 212, 150), (2, 190, 170), (3, 180, 118), (4, 140, 80), (5, 295, 120), (6, 318, 158), (7, 320, 90),
                    (8, 205, 205), (9, 175, 235), (10, 140, 240), (11, 150, 290), (12, 262, 215), (13, 290, 198), (14, 320, 265)]:
    tr_how.circle(bx, by, 10, fill="paper")
    tr_how.text(bx, by + 5, str(num), "t-head", size=12)
legend = ["1 ADRs", "2 transactional outbox", "3 RFCs", "4 Kafka writes in requests", "5 managed Kafka", "6 routing Engine A", "7 feature-flag service",
          "8 Postgres", "9 managed containers", "10 change data capture", "11 a 2nd database type", "12 Python, Django", "13 React Native", "14 Go for small tools"]
for i, t in enumerate(legend):
    tr_how.text(486, 34 + i * 22, t, anchor="start", size=13)

RADAR = dict(
    slug="technology-radar",
    kicker="a.k.a. “the pantry list on the fridge”",
    tldr="As a team grows, “can I use X?” arrives faster than an architect can answer it. A <b>technology radar</b> answers in advance: every technology the teams care about, placed in one of four rings: <b>adopt</b> (our default), <b>trial</b> (use it on real work, carefully), <b>assess</b> (explore, not in production) and <b>hold</b> (don't start anything new with it). Build it <b>with the tech leads</b>, give each blip a sentence and a link to its ADR, and <b>refresh it every six months</b>.",
    chips=[("Family", "big choices"), ("Origin", "ThoughtWorks Technology Radar (2010–); Zalando and others publish their own"), ("Lives in", "a page in the repo or wiki, refreshed twice a year"), ("Pairs with", "technology evaluation, ADRs, golden paths")],
    problem_side="Larder, 22 June 2026",
    problem="""  <p class="lead">Four engineers joined in the spring (14 → 18). In May alone Ana got <span class="hl-pink">eleven “can I use X?” messages</span>: Go for a small tool, a second message-queue library, MongoDB for business orders, a new date library. Each got an answer, but a different one depending on the day and who asked. One new hire had already written a tool in Go before asking.</p>
  <ul>
    <li>Every new engineer brings favourites; without a shared default, the stack sprawls.</li>
    <li>The architect becomes a help desk for technology choices.</li>
    <li>Old decisions (ADRs) exist, but nobody new knows which technologies they settled.</li>
  </ul>""",
    problem_figs=[tr_problem],
    analogy_side="the pantry list on the fridge",
    analogy="""  <p>A busy household keeps a <b>pantry list</b> on the fridge: what's <b>always stocked</b>, what they're <b>trying this month</b>, what they've <b>heard about</b>, and what they <b>don't buy any more</b> (and why). Whoever does the shopping buys the right things without phoning home. Twice a year someone updates the list.</p>""",
    analogy_figs=[tr_analogy],
    map=[("Always stocked", "Adopt: the default; no question needed"),
         ("Trying this month", "Trial: on real work, with a named owner"),
         ("Heard about it", "Assess: explore, spike, but not in production"),
         ("Don't buy any more", "Hold: nothing new with it"),
         ("Updating the list twice a year", "The radar refresh with the tech leads")],
    how_side="one page, four rings, twice a year",
    how="""  <p>Ana and the four tech leads built the first radar in one afternoon: fourteen blips, each with <b>one sentence</b> and a link to its ADR or evaluation card. The rule that made it work: <b>adopt and trial need no permission</b>; assess means a spike first; hold needs an ADR to break.</p>""",
    how_figs=[tr_how],
    steps=[("Collect the candidates", "Ask each team what they use, want to use, and wish they didn't. Twenty to forty items."),
           ("Place them together", "An afternoon with the tech leads: ring and quadrant per blip. Disagreement is useful."),
           ("Write one sentence each", "Why it's in that ring, and a link to the ADR, evaluation card or spike."),
           ("Say what each ring allows", "Adopt and trial: go ahead. Assess: spike first. Hold: needs an ADR."),
           ("Publish it where people look", "In the repo or wiki, linked from onboarding and the PR template."),
           ("Refresh every six months", "Move blips, add new ones, explain each move in a sentence.")],
    vocab=[("Blip", "One technology or technique on the radar."),
           ("Adopt", "Our default; use it."),
           ("Trial", "Use on real work, with care and a named owner."),
           ("Assess", "Worth exploring; not in production yet."),
           ("Hold", "Don't start anything new with it."),
           ("Quadrant", "A grouping: techniques, tools, platforms, languages and frameworks.")],
    code=dict(file="docs/radar/2026-06.md", note="Larder Tech Radar, June 2026 (excerpt)", plain=True, src="""
# Larder Tech Radar · June 2026            next refresh: December 2026
Adopt, trial: go ahead · Assess: spike first · Hold: needs an ADR to break

| Blip                      | Quadrant   | Ring   | Why (one sentence)                         | Link     |
|---------------------------|------------|--------|--------------------------------------------|----------|
| Transactional outbox      | technique  | adopt  | How events leave a transaction safely.     | ADR 0007 |
| Postgres                  | platform   | adopt  | Our one database; ask before adding one.   | ADR 0002 |
| Python, Django            | language   | adopt  | The team's skills; Core and new services.  |          |
| Managed Kafka             | tool       | trial  | Live since Feb; topics need an owner.      | ADR 0006 |
| Routing Engine A          | tool       | trial  | Dispatch only, until on-time ≥ 93 %.       | ADR 0012 |
| Managed containers        | platform   | trial  | Default for new services.                  | ADR 0010 |
| Go for small tools        | language   | assess | Fast CLIs, but a 2nd language to maintain. | spike    |
| Kafka writes in requests  | technique  | hold   | Loses events on crash; use the outbox.     | ADR 0007 |
| A 2nd database type       | platform   | hold   | Ops cost for one engineer; ADR first.      |          |
"""),
    tools="tools: a Markdown table is enough. ThoughtWorks' “Build your own Radar” tool and Zalando's open-source radar generator draw the circles from a spreadsheet; Backstage has a radar plugin.",
    gains=["<b>Fast answers</b>: most “can I use X?” questions answer themselves.",
           "<b>Less sprawl</b>: shared defaults, deliberate exceptions.",
           "<b>Onboarding</b>: newcomers see the stack and the reasons.",
           "<b>Safe experimentation</b>: assess and trial are allowed, on purpose.",
           "<b>Links old decisions</b> to everyday choices."],
    losses=["<b>Goes stale</b> without the six-monthly refresh.",
            "<b>Can feel like a ban list</b> if hold dominates.",
            "<b>An afternoon of tech leads</b> twice a year.",
            "<b>Arguments about rings</b> can drag on."],
    baseline="Each line compares <b>answering “can I use X?” one message at a time</b> to <b>a published radar with four rings, one sentence per blip, refreshed twice a year</b>.",
    ratings=[(2, 4, "One page shows the stack and why."),
             (2, 4, "Tech leads place blips together."),
             (2, 5, "Most questions are answered before they're asked."),
             (2, 4, "Hold stops known traps; assess keeps new things away from production."),
             (3, 4, "Trial lets new tools in, carefully."),
             (2, 4, "Each blip links to its ADR or evaluation."),
             (3, 3, "Running cost shows up in the one-line reasons."),
             (3, 4, "An afternoon twice a year."),
             (2, 5, "Teams choose within the rings without asking.")],
    pitfalls=[("Never refreshed", "The December radar is still June's in March.", "put the refresh date on the page and in the calendar."),
              ("The architect's radar", "Ana fills it alone; teams ignore it.", "place blips with the tech leads."),
              ("No reasons", "A ring without a sentence invites arguments.", "one sentence and a link per blip."),
              ("Hold as a ban", "Hold blocks fixing old code that uses it.", "hold means nothing new; existing use is fine.")],
    use=["Teams growing past ten engineers.",
         "When “can I use X?” reaches the architect weekly.",
         "Onboarding new hires.",
         "After a technology evaluation, to record where the winner sits."],
    skip=["A single small team that already shares one stack.",
          "As a substitute for ADRs: the radar points to them."],
    related=["<b>Technology evaluation</b> (this volume)", "<b>Architecture decision records</b> (this volume)", "<b>Golden paths</b> (Vol. 6)", "<b>Architecture principles</b> (Vol. 6)"],
    quiz=[("What are the four rings?", "Adopt, trial, assess and hold."),
          ("What does “hold” mean?", "Don't start anything new with it; existing use can stay."),
          ("Who should place the blips?", "The architect with the tech leads, together."),
          ("How often should it be refreshed?", "About every six months, with a sentence explaining each move.")],
    try_it="List the ten technologies your team argues about most. Put each in a ring (adopt, trial, assess, hold) with one sentence of reasoning. Show it to two other engineers and move anything they can convince you about. Publish it with a refresh date six months out.",
    remember="Write the <span class=\"hl\">pantry list</span>, and update it <span class=\"hl\">twice a year</span>.",
    sources=["ThoughtWorks, Technology Radar (thoughtworks.com/radar), and “Build your own Radar”.",
             "Neal Ford, “Build Your Own Technology Radar” (2013).",
             "Zalando Tech Radar (opensource.zalando.com/tech-radar).",
             "Backstage Tech Radar plugin documentation."],
)

NOTES = [BUILD_BUY, TECH_EVAL, CLOUD, RADAR]
