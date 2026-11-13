# Series 2 · The Solution Architect's Notebook · Vol. 5 · Cost & balance.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 Total Cost of Ownership
tc_problem = Doodle(760, 280, "Doodle of February 2028. ADR 0012's routing engine, open source and self-hosted, has been on watch since 2026. Joost is tired of upgrade weekends and a vendor offers a managed routing service. The debate is about price per month: the open-source engine is free, the service costs about 4,000 euros a month. Nobody has counted people, upgrades or growth.",
                    "“Engine A is free; the service costs €4,000 a month.” Nobody has counted people, upgrades or growth.")
tc_problem.box(20, 40, 320, 100, "Engine A", "green", sub="“free”")
tc_problem.box(400, 40, 340, 100, "routing service", "pink", sub="€4,000 / month")
tc_problem.note(380, 200, "comparing licence prices, not costs", "red", size=19)

tc_analogy = Doodle(760, 250, "Doodle of choosing between a cheap printer and an expensive one: the cheap printer's ink costs a fortune and it jams weekly; over three years it costs more. The price on the box is the smallest part.",
                     "The cheap printer's ink costs a fortune and it jams weekly. Over three years, the price on the box is the smallest part.")
tc_analogy.icon("copier", 30, 60, 1.2)
tc_analogy.box(150, 50, 280, 100, "price on the box", "y", sub="€60")
tc_analogy.box(460, 50, 280, 100, "three years of ink", "pink", sub="€540 + jams")
tc_analogy.note(450, 210, "count everything, for years", "pen")

tc_how = Doodle(760, 400, "Ana's three-year total cost of ownership, 7 February 2028, at the forecast volume. Engine A, self-hosted: hosting about 72,000 euros, half an engineer about 135,000, map data and upgrades about 36,000, total about 243,000; people are more than half. Managed routing service: usage fees growing with orders about 230,000, integration 40,000, a tenth of an engineer 27,000, total about 297,000, plus an exit cost if prices rise. Decision: keep Engine A, fund the half engineer explicitly, review the service again if order volume or Engine A's incidents change.",
                 "Three years, every cost, at forecast volume: €243k vs €297k. People are the biggest line.")
tc_how.head(20, 30, "3 years", anchor="start", size=15)
tc_how.head(360, 30, "Engine A", anchor="start", size=15)
tc_how.head(560, 30, "service", anchor="start", size=15)
for i, (k, a, b, f) in enumerate([("hosting / usage", "€72k", "€230k", "paper"), ("people", "€135k", "€27k", "y"),
                                  ("upgrades, map data", "€36k", "—", "paper"), ("integration", "—", "€40k", "paper"), ("total", "≈ €243k", "≈ €297k", "green")]):
    y = 44 + i * 46
    tc_how.box(12, y, 736, 38, None, f, rx=4)
    tc_how.text(20, y + 25, k, "t-head", anchor="start", size=14)
    tc_how.text(360, y + 25, a, "t-head" if k == "total" else "t", anchor="start", size=14)
    tc_how.text(560, y + 25, b, "t-head" if k == "total" else "t", anchor="start", size=14)
tc_how.box(12, 284, 736, 46, "keep Engine A · fund the half engineer · review at volume", "blue", size=15)
tc_how.note(380, 366, "“free” software: people are the biggest line", "pen", size=16)

TCO = dict(
    slug="total-cost-of-ownership",
    kicker="a.k.a. “the cheap printer”",
    tldr="<b>Total cost of ownership</b> (TCO) adds up <b>every cost</b> of an option over <b>several years</b>: licences or usage, hosting, <b>people</b> to run and upgrade it, integration, training, support, and the cost of leaving. It's the only fair way to compare build, buy, open source and managed services, because the visible price is rarely the biggest line. Use the <b>forecast volume</b>, not today's.",
    chips=[("Family", "cost &amp; balance"), ("Origin", "Gartner (1980s), IT procurement practice"), ("Lives in", "a TCO sheet attached to the ADR"), ("Pairs with", "build vs buy vs open source, exit plans, cost-aware architecture")],
    problem_side="Larder, 7 February 2028",
    problem="""  <p class="lead">Routing <b>Engine A</b> (open source, self-hosted, ADR 0012) has been on watch since 2026. Joost is tired of <b>upgrade weekends</b>, and a vendor offers a <b>managed routing service</b>. The debate is about monthly prices: Engine A is <b>“free”</b>, the service is about <b>€4,000 a month</b>. <span class="hl-pink">Nobody has counted the people</span>, the upgrades, or how the service's fee grows with orders.</p>
  <ul>
    <li>Licence prices hide the biggest costs.</li>
    <li>Usage-based fees grow with the business.</li>
    <li>People's time is real money, even if salaried.</li>
  </ul>""",
    problem_figs=[tc_problem],
    analogy_side="the cheap printer",
    analogy="""  <p>A <b>cheap printer</b> costs €60; its <b>ink</b> costs €15 a month and it jams every week. An expensive one costs €300 with cheap ink. Over <b>three years</b>, the price on the box is the smallest part, and the jams cost an evening each.</p>""",
    analogy_figs=[tc_analogy],
    map=[("The price on the box", "Licence: Engine A free, the service €4,000 a month today"),
         ("The ink", "Hosting and usage fees at forecast volume"),
         ("Weekly jams", "Upgrade weekends and incidents"),
         ("Three years", "The comparison period"),
         ("Your evenings", "Half an engineer's time")],
    how_side="every cost, three years, forecast volume",
    how="""  <p>Ana and Marco built a three-year sheet at <b>forecast volume</b>. <b>Engine A</b>: hosting ≈ €72k, <b>half an engineer ≈ €135k</b>, map data and upgrades ≈ €36k: <b>≈ €243k</b>. <b>The service</b>: usage fees rising with orders ≈ €230k, integration ≈ €40k, a tenth of an engineer ≈ €27k: <b>≈ €297k</b>, plus an exit cost if prices rise. Decision: <b>keep Engine A</b>, but fund the half engineer explicitly (Joost's weekends were the hidden cost), and review if volume or incidents change.</p>""",
    how_figs=[tc_how],
    steps=[("Pick the period", "Usually three to five years."),
           ("List every cost", "Licences, usage, hosting, people, integration, training, support, exit."),
           ("Use forecast volume", "Not today's; usage fees grow."),
           ("Price people honestly", "Fraction of an engineer × loaded cost."),
           ("Add risk and exit", "Price changes, lock-in, migration cost."),
           ("Compare totals, then qualities", "Cost isn't the only criterion.")],
    vocab=[("TCO", "Total cost of ownership over a period."),
           ("Loaded cost", "Salary plus taxes, benefits, equipment and overhead."),
           ("Usage-based pricing", "Fees that grow with volume."),
           ("Exit cost", "What it costs to leave an option later."),
           ("Opex vs capex", "Running costs vs one-off investment."),
           ("Hidden cost", "A real cost not on any invoice (people's time).")],
    code=dict(file="docs/costs/routing-tco.md", note="the routing TCO, 7 February 2028", plain=True, src="""
# TCO · routing · 3 years (2028–2030) · forecast: 27k → 55k orders/day · Ana with Marco, Eli

|                          | Engine A (self-hosted, ADR 0012) | Managed routing service      |
|--------------------------|----------------------------------|------------------------------|
| Licence / usage          | 0                                | ≈ €230k (per stop, grows)    |
| Hosting                  | ≈ €72k                           | included                     |
| People                   | 0.5 engineer ≈ €135k             | 0.1 engineer ≈ €27k          |
| Upgrades, map data       | ≈ €36k                           | included                     |
| Integration / migration  | 0                                | ≈ €40k                       |
| Total                    | ≈ €243k                          | ≈ €297k (+ exit risk)        |

Decision: keep Engine A; the 0.5 engineer becomes an explicit role on Eli's team.
Review: if volume > 70k orders/day, or Engine A causes > 2 P1 incidents in a quarter.
"""),
    tools="tools: a spreadsheet; vendor pricing calculators; the cloud bill by tag; loaded people costs from finance.",
    gains=["<b>Fair comparisons</b> across build, buy and open source.",
           "<b>Hidden costs visible</b>: people, upgrades.",
           "<b>Growth priced in</b>.",
           "<b>Finance trusts</b> the numbers.",
           "<b>Decisions with review points</b>."],
    losses=["<b>Estimates of the future</b>.",
            "<b>People costs</b> are sensitive to discuss.",
            "<b>Takes a day or two</b>.",
            "<b>Cost can crowd out</b> other qualities."],
    baseline="Each line compares <b>comparing licence or monthly prices</b> to <b>a multi-year total of every cost, at forecast volume, people included</b>.",
    ratings=[(2, 5, "One sheet, every cost, two totals."),
             (2, 5, "Marco, Joost and Eli agree on the numbers."),
             (3, 4, "The debate ends at the totals."),
             (2, 4, "Usage growth and exit risk priced in."),
             (3, 4, "Review triggers in the decision."),
             (2, 4, "The sheet sits with the ADR."),
             (1, 5, "Every cost counted for three years."),
             (3, 3, "A day or two of work."),
             (3, 3, "Neutral.")],
    pitfalls=[("Licence only", "“Open source is free.”", "count people and hosting."),
              ("Today's volume", "Usage fees at current orders.", "forecast volume."),
              ("Forgetting exit", "No cost to leave assumed.", "price migration and lock-in."),
              ("Cost only", "Cheapest wins, whatever it does.", "compare qualities too.")],
    use=["Build vs buy vs open source decisions.",
         "Renewals and vendor changes.",
         "Comparing hosting models.",
         "When “free” software takes a lot of time."],
    skip=["Small, cheap tools with no lock-in."],
    related=["<b>Build vs buy vs open source</b> (vol. 2)", "<b>Exit plans &amp; reversibility</b> (vol. 2)", "<b>Cost-aware architecture</b> (this volume)", "<b>Cost visibility (FinOps)</b> (patterns, Vol. 6)"],
    quiz=[("What does TCO include?", "Every cost over several years: licences, hosting, people, integration, upgrades, exit."),
          ("Why use forecast volume?", "Usage-based fees grow with the business."),
          ("What was the biggest cost of “free” Engine A?", "Half an engineer's time, about €135k over three years."),
          ("What did Larder decide?", "Keep Engine A and fund the half engineer explicitly, with review triggers.")],
    try_it="Pick a tool or service your team runs. Add up three years of every cost, including people's time at a loaded rate. Compare it with one alternative at forecast volume.",
    remember="Don't buy the <span class=\"hl\">printer</span>; buy three years of <span class=\"hl\">ink</span>.",
    sources=["Gartner, Total Cost of Ownership model (1987 onwards).",
             "Bill Kirwin, “TCO: the hidden cost of IT” (Gartner research, 1990s).",
             "J.R. Storment and Mike Fuller, <i>Cloud FinOps</i>, 2nd ed. (2023).",
             "Martin Fowler, “Utility vs Strategic Dichotomy” (martinfowler.com, 2010)."],
)

# ------------------------------------------------------------------ 13 Cost-Aware Architecture
ca_problem = Doodle(760, 280, "Doodle of February 2028. Cost per order was meant to reach 2.80 euros by the end of 2027; it ended at 3.05. Marco looks at the cloud bill: 78,000 euros a month and rising, as one number. Nobody can say which part of the platform costs what, or what an order costs in cloud.",
                    "The cloud bill: €78,000 a month, one number. Nobody can say what each part costs, or what an order costs.")
ca_problem.box(20, 40, 320, 100, "€78k / month", "pink", sub="one number", stroke="red")
ca_problem.box(400, 40, 340, 100, "cost per order", "y", sub="€3.05 (target €2.80)")
ca_problem.note(380, 200, "a bill nobody can read", "red", size=20)

ca_analogy = Doodle(760, 250, "Doodle of a restaurant that prices each dish: ingredients, chef's minutes, energy for the oven. Once the kitchen knows the risotto costs four euros and the steak eleven, it can redesign the menu, not just ask everyone to use less butter.",
                     "A restaurant that costs each dish can redesign the menu, not just ask everyone to use less butter.")
ca_analogy.icon("menu", 30, 60, 1.3)
ca_analogy.box(150, 50, 280, 100, "risotto", "green", sub="€4 a plate")
ca_analogy.box(460, 50, 280, 100, "steak", "pink", sub="€11 a plate")
ca_analogy.note(450, 210, "cost per dish, not per month", "pen")

ca_how = Doodle(760, 400, "Larder's cost work from 21 February 2028. Every resource tagged with its capability and team. Cost per thousand orders for each part on the platform dashboard. Findings: logs 11,000 euros a month, mostly Dispatch's debug logging; six idle test environments, 7,000; an oversized replica, 3,000; images served uncompressed from the origin, 4,000. Fixes: log sampling, test environments that switch off at night, right-sizing, image compression. Bill: 78,000 to 58,000 euros a month; cloud cost per order from about 9.6 to 7.1 cents. Every design review now has a cost line.",
                 "Tag everything, show cost per order per part, fix the big lines. €78k → €58k a month.")
for i, (t, v, f) in enumerate([("logs (Dispatch debug)", "€11k", "pink"), ("idle test environments", "€7k", "pink"), ("images, uncompressed", "€4k", "y"), ("oversized replica", "€3k", "y")]):
    y = 14 + i * 50
    ca_how.box(14, y, 732, 42, None, f, rx=4)
    ca_how.text(30, y + 28, t, "t-head", anchor="start", size=15)
    ca_how.text(730, y + 28, v + " / month", anchor="end", size=15)
ca_how.box(14, 222, 732, 50, "sampling · night switch-off · compression · right-size", "blue", size=15)
ca_how.box(14, 290, 360, 60, "€78k → €58k", "green", sub="per month", size=17)
ca_how.box(386, 290, 360, 60, "9.6 → 7.1 cents", "green", sub="cloud cost per order", size=17)
ca_how.note(380, 382, "every design review now has a cost line", "pen", size=15)

COSTAWARE = dict(
    slug="cost-aware-architecture",
    kicker="a.k.a. “the price of each dish”",
    tldr="<b>Cost-aware architecture</b> treats cost as a quality like speed or availability. <b>Tag</b> every resource with its capability and owner, show <b>cost per unit of business</b> (per order, per customer) for each part, and give teams that number. Then fix the big lines (logging, idle environments, oversizing, data transfer) and add a <b>cost line to every design review</b>. A bill nobody can read can't be designed down.",
    chips=[("Family", "cost &amp; balance"), ("Origin", "FinOps practice; AWS Well-Architected cost pillar"), ("Lives in", "tags, the cost dashboard and every design review"), ("Pairs with", "total cost of ownership, capacity planning, green software")],
    problem_side="Larder, 21 February 2028",
    problem="""  <p class="lead">Cost per order was meant to reach <b>€2.80</b> by the end of 2027; it ended at <b>€3.05</b>. Marco looks at the cloud bill: <b>€78,000 a month</b> and rising, as one number. <span class="hl-pink">Nobody can say which part costs what</span>, or what an order costs in cloud, so every cost conversation ends with “let's be careful”.</p>
  <ul>
    <li>One total can't be acted on.</li>
    <li>Teams don't see the cost of their design choices.</li>
    <li>Waste hides in logs, idle environments and oversizing.</li>
  </ul>""",
    problem_figs=[ca_problem],
    analogy_side="the price of each dish",
    analogy="""  <p>A restaurant that only knows its monthly food bill can only ask everyone to <b>use less butter</b>. One that knows the <b>risotto costs €4 a plate</b> and the <b>steak €11</b> can redesign the menu, change suppliers, or price differently. Cost per dish turns a worry into decisions.</p>""",
    analogy_figs=[ca_analogy],
    map=[("The monthly food bill", "€78k a month, as one number"),
         ("Cost per dish", "Cloud cost per order, per part of the platform"),
         ("Using less butter", "“Let's be careful”"),
         ("Redesigning the menu", "Log sampling, night switch-off, compression, right-sizing"),
         ("The chef sees the cost", "Teams see their part's cost per order")],
    how_side="tag, unit cost, fix the big lines, review",
    how="""  <p>Eli tagged every resource with its <b>capability and team</b>, and the platform dashboard now shows <b>cost per 1,000 orders</b> for each part. The big lines: <b>logs €11k a month</b> (mostly Dispatch's debug logging), <b>six idle test environments €7k</b>, uncompressed images €4k, an oversized replica €3k. Fixes: log sampling, test environments that switch off at night, compression, right-sizing. The bill fell to <b>€58k</b>; cloud cost per order from about <b>9.6 to 7.1 cents</b>. Every design review now has a <b>cost line</b>.</p>""",
    how_figs=[ca_how],
    steps=[("Tag everything", "Capability, team, environment; untagged = alert."),
           ("Pick a business unit", "Cost per order, per customer, per city."),
           ("Show it per part", "On the dashboard teams already use."),
           ("Fix the big lines", "Logs, idle resources, oversizing, data transfer."),
           ("Add a cost line to reviews", "Expected cost per order for each design."),
           ("Set budget alerts", "Per team, so surprises are days old, not months.")],
    vocab=[("Unit cost", "Cost per unit of business (order, customer)."),
           ("Cost allocation tags", "Labels that assign cloud costs to owners."),
           ("Right-sizing", "Matching resource size to real use."),
           ("FinOps", "Engineering, finance and product managing cloud cost together."),
           ("Showback", "Showing teams the cost of what they run."),
           ("Egress", "Data transferred out, often charged.")],
    code=dict(file="docs/costs/2028-02-cost-review.md", note="the cost review, 21 February 2028", plain=True, src="""
# Cloud cost review · Feb 2028 · Ana, Eli, Marco · bill €78k/month · ≈ 810k orders/month

Cost per 1,000 orders by part (before)     Core €31 · Dispatch €24 · data & analytics €18 ·
                                           logs/monitoring €14 · test envs €9 · CDN/images €5

| Line                                   | €/month | Fix                                | Owner | After  |
|----------------------------------------|---------|------------------------------------|-------|--------|
| Logs, mostly Dispatch debug level      | 11,000  | sampling, debug off in production  | Eli   | 3,500  |
| 6 test environments, idle 70 % of time | 7,000   | off at night and weekends          | Eli   | 2,400  |
| Product images uncompressed at origin  | 4,000   | compress + modern formats          | Dee   | 1,300  |
| Read replica 2 sizes too big           | 3,000   | right-size after load test         | Eli   | 1,500  |

Bill: €78k → €58k/month · cloud cost per order ≈ 9.6 → 7.1 cents
Design reviews: new "expected cost per 1,000 orders" line (template updated)
"""),
    tools="tools: cloud cost tags and reports, a FinOps or cost dashboard (the provider's own, or tools like Kubecost or Vantage), budget alerts, the design review template.",
    gains=["<b>A readable bill</b>: cost per order, per part.",
           "<b>€20k a month</b> saved in weeks.",
           "<b>Teams see</b> their choices' cost.",
           "<b>Designs priced</b> before they're built.",
           "<b>Marco and engineering</b> speak one language."],
    losses=["<b>Tagging discipline</b> needed.",
            "<b>Shared costs</b> are hard to split.",
            "<b>Cost can dominate</b> other qualities.",
            "<b>Ongoing attention</b>."],
    baseline="Each line compares <b>one monthly cloud bill</b> to <b>tagged costs, cost per order per part, fixed big lines and a cost line in every design review</b>.",
    ratings=[(2, 5, "Cost per order per part, on one dashboard."),
             (2, 5, "Marco and the teams read the same numbers."),
             (3, 4, "Cost questions answered with data."),
             (3, 4, "Budget alerts catch surprises."),
             (3, 4, "Designs compared on cost early."),
             (2, 4, "Fixes and savings recorded."),
             (1, 5, "€78k → €58k a month."),
             (3, 3, "Tagging and reviews take time."),
             (2, 4, "Teams own their part's cost.")],
    pitfalls=[("One big number", "The bill as a total.", "cost per order, per part."),
              ("Untagged resources", "30 % “unallocated”.", "alert on untagged."),
              ("Cutting blindly", "Reliability cut with cost.", "check against budgets and SLOs."),
              ("Once a year", "Annual cost panic.", "monthly review, budget alerts.")],
    use=["Growing cloud bills.",
         "When cost per order is a business target.",
         "Design reviews for new services.",
         "After big launches or migrations."],
    skip=["Tiny bills where the effort costs more than the savings."],
    related=["<b>Total cost of ownership</b> (this volume)", "<b>Capacity planning</b> (this volume)", "<b>Green software</b> (this volume)", "<b>Cost visibility (FinOps)</b> (patterns, Vol. 6)"],
    quiz=[("What makes cost actionable?", "Cost per unit of business (per order) for each part, with owners."),
          ("What were Larder's biggest waste lines?", "Dispatch's debug logs, idle test environments, uncompressed images, an oversized replica."),
          ("What changed in design reviews?", "A cost line: expected cost per 1,000 orders."),
          ("What was the result?", "The bill fell from €78k to €58k; cost per order from about 9.6 to 7.1 cents.")],
    try_it="Tag your cloud resources by team or capability for one month. Divide each part's cost by your main business unit (orders, customers), and pick the biggest line to cut without hurting a quality you've promised.",
    remember="Price each <span class=\"hl\">dish</span>; then redesign the <span class=\"hl\">menu</span>.",
    sources=["J.R. Storment and Mike Fuller, <i>Cloud FinOps</i>, 2nd ed. (2023).",
             "FinOps Foundation, FinOps Framework (finops.org).",
             "AWS Well-Architected Framework, Cost Optimization Pillar.",
             "Erik Peterson, “Cloud Unit Economics” (CloudZero writing, 2020s)."],
)

# ------------------------------------------------------------------ 14 Green Software
gs_problem = Doodle(760, 280, "Doodle of March 2028. Korenwolf reports its own emissions and sends suppliers a questionnaire: what are the emissions of the services you provide us? Mo forwards it to Ana with one question: what do we answer for the platform? Nobody at Larder has ever measured it.",
                    "Korenwolf's supplier questionnaire: what are your platform's emissions? Nobody has ever measured.")
gs_problem.box(20, 40, 340, 100, "Korenwolf", "y", sub="supplier emissions questionnaire")
gs_problem.box(400, 40, 340, 100, "Mo → Ana", "paper", sub="“what do we answer?”")
gs_problem.note(380, 200, "never measured, so nothing to say", "red", size=19)

gs_analogy = Doodle(760, 250, "Doodle of running a home more greenly: first read the meter, then use less (switch off what's idle), run the washing machine when the electricity is cleanest, and choose a greener supplier. Measure, reduce, shift, choose.",
                     "A greener home: read the meter, use less, run the washing when power is cleanest, pick a cleaner supplier.")
gs_analogy.icon("gauge", 30, 60, 1.2)
for i, (t, f) in enumerate([("measure", "paper"), ("use less", "green"), ("shift", "blue"), ("choose", "y")]):
    gs_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=16)
gs_analogy.note(450, 200, "meter first, then the rest", "pen")

gs_how = Doodle(760, 400, "Larder's green software work from 6 March 2028. Measure: the cloud provider's carbon report plus estimates for data transfer, about 9 tonnes of CO2-equivalent a year for the platform, about 0.9 grams per order; the delivery e-bikes and vans are far larger. Use less: the cost cuts already removed idle resources; old event archives cut from 40 to 12 terabytes; image compression cut app data by 38 percent. Shift: nightly reporting and backup copies moved to hours with cleaner electricity. Choose: the second region for backups picked partly on carbon intensity. Result: about 0.6 grams per order, reported honestly to Korenwolf, with the method.",
                 "Measure, use less, shift, choose. About 0.9 → 0.6 g CO₂e per order, reported with the method.")
gs_how.box(14, 14, 732, 60, "measure: ≈ 9 t CO₂e / year · ≈ 0.9 g per order", "paper", size=15)
for i, (t, s, f) in enumerate([("use less", "idle off · archives · images", "green"), ("shift", "nightly jobs, cleaner hours", "blue"), ("choose", "backup region by carbon", "y")]):
    gs_how.box(14 + i * 248, 92, 236, 100, t, f, sub=s, size=16, subsize=14)
gs_how.box(14, 212, 732, 56, "≈ 0.6 g CO₂e per order", "green", size=17)
gs_how.note(380, 304, "e-bikes and vans dominate; said so honestly", "pen", size=16)
gs_how.note(380, 336, "answer to Korenwolf: number + method + plan", "green", size=15)

GREEN = dict(
    slug="green-software",
    kicker="a.k.a. “reading the meter”",
    tldr="<b>Green software</b> reduces the carbon emissions of running software. Start by <b>measuring</b> (the cloud provider's carbon report, plus estimates), express it <b>per unit of business</b> (per order), then <b>use less</b> (idle resources, data you don't need, heavy transfers), <b>shift</b> flexible work to times and places with cleaner electricity, and <b>choose</b> cleaner regions. Report the number <b>with its method</b>, and be honest about where the bigger emissions are.",
    chips=[("Family", "cost &amp; balance"), ("Origin", "Green Software Foundation (2021), Software Carbon Intensity (SCI) specification"), ("Lives in", "a yearly carbon page and the cost dashboard"), ("Pairs with", "cost-aware architecture, data classification (retention), capacity planning")],
    problem_side="Larder, 6 March 2028",
    problem="""  <p class="lead">Korenwolf reports its own emissions and sends suppliers a <b>questionnaire</b>: what are the emissions of the services you provide us? Mo forwards it to Ana: <b>what do we answer for the platform?</b> <span class="hl-pink">Nobody at Larder has ever measured it.</span></p>
  <ul>
    <li>Clients increasingly ask suppliers for emissions data.</li>
    <li>Without a number, there's nothing to improve or report.</li>
    <li>Guesses either overclaim or undersell.</li>
  </ul>""",
    problem_figs=[gs_problem],
    analogy_side="a greener home",
    analogy="""  <p>To run a home more greenly you first <b>read the meter</b>. Then you <b>use less</b> (switch off what's idle), run the <b>washing machine when electricity is cleanest</b>, and <b>choose a greener supplier</b>. Without the meter, every step is a guess.</p>""",
    analogy_figs=[gs_analogy],
    map=[("Reading the meter", "The provider's carbon report, per order"),
         ("Switching off what's idle", "Idle environments, old archives"),
         ("Washing at the cleanest hour", "Nightly jobs moved to cleaner hours"),
         ("A greener supplier", "A backup region with cleaner electricity"),
         ("The car in the drive", "E-bikes and vans: far larger emissions")],
    how_side="measure, use less, shift, choose",
    how="""  <p>Ana and Eli <b>measured</b>: the provider's carbon report plus estimates for data transfer, about <b>9 tonnes CO₂e a year</b>, about <b>0.9 g per order</b>. They <b>used less</b> (the cost cuts had removed idle resources; event archives cut from 40 to 12 TB; image compression cut app data by 38 %), <b>shifted</b> nightly reporting and backup copies to cleaner hours, and <b>chose</b> the backup region partly on carbon intensity. Result: about <b>0.6 g per order</b>. The answer to Korenwolf gave the number, the method, the plan, and said plainly that the <b>e-bikes and vans</b> matter far more.</p>""",
    how_figs=[gs_how],
    steps=[("Measure", "Provider carbon tools; estimate what they miss."),
           ("Express per unit", "Grams of CO₂e per order (like SCI)."),
           ("Use less", "Idle resources, unneeded data, heavy transfers."),
           ("Shift flexible work", "To cleaner hours or regions."),
           ("Choose cleaner places", "When picking regions and vendors."),
           ("Report with the method", "And name the bigger sources honestly.")],
    vocab=[("CO₂e", "Carbon dioxide equivalent: all greenhouse gases in one unit."),
           ("Carbon intensity", "Grams of CO₂e per kilowatt-hour of electricity."),
           ("SCI", "Software Carbon Intensity: emissions per functional unit."),
           ("Carbon-aware", "Running flexible work when or where electricity is cleaner."),
           ("Embodied carbon", "Emissions from making the hardware."),
           ("Scope 3", "Emissions in a company's supply chain, e.g. its suppliers' services.")],
    code=dict(file="docs/sustainability/platform-carbon-2027.md", note="the answer for Korenwolf, March 2028", plain=True, src="""
# Platform carbon · 2027 · method and plan                    Ana, Eli · for Mo (Korenwolf questionnaire)

Measured     cloud provider carbon report (location-based) ≈ 8.1 t CO₂e
Estimated    data transfer + CDN ≈ 0.9 t · total ≈ 9 t CO₂e/year · ≈ 0.9 g per order
Not included staff laptops, handhelds, office (company report) · deliveries (e-bikes, vans: far larger)

Done (Feb–Mar 2028)
  idle test environments off nights/weekends · event archives 40 TB → 12 TB (retention per class)
  images compressed: app data −38 % · nightly reporting + backup copies moved to 01:00–05:00
  backup region chosen partly on grid carbon intensity
Now          ≈ 0.6 g CO₂e per order (SCI-style: per order, per year) · next review March 2029
"""),
    tools="tools: the cloud provider's carbon footprint tool, the Green Software Foundation's SCI specification, carbon intensity data (e.g. Electricity Maps), the cost dashboard.",
    gains=["<b>An honest answer</b> for clients.",
           "<b>Overlaps with cost cuts</b>: less waste.",
           "<b>Per-order number</b> to improve.",
           "<b>Method in the open</b>.",
           "<b>Bigger sources named</b>, not hidden."],
    losses=["<b>Measurements are estimates</b>.",
            "<b>Provider tools</b> differ and lag.",
            "<b>Small next to deliveries</b>.",
            "<b>Shifting work</b> adds scheduling complexity."],
    baseline="Each line compares <b>not measuring the platform's emissions</b> to <b>measuring per order, reducing, shifting, choosing cleaner places and reporting with the method</b>.",
    ratings=[(2, 4, "One number per order, with a method."),
             (2, 4, "Mo can answer Korenwolf honestly."),
             (3, 3, "Neutral."),
             (2, 4, "No overclaiming in a client report."),
             (3, 4, "The plan updates yearly."),
             (2, 4, "Method and numbers written down."),
             (2, 4, "Most actions also cut the bill."),
             (3, 3, "A day a year to report."),
             (3, 3, "Neutral.")],
    pitfalls=[("Overclaiming", "“Carbon-neutral platform.”", "the number, the method, the limits."),
              ("Ignoring the big sources", "Platform optimised; vans ignored.", "say where the real emissions are."),
              ("No unit", "Tonnes rise as you grow.", "grams per order."),
              ("Green at any cost", "Reliability cut to save grams.", "balance with other qualities.")],
    use=["Client or investor questionnaires.",
         "Choosing regions and vendors.",
         "Alongside cost reviews.",
         "Retention and archiving decisions."],
    skip=["Never entirely, but keep it proportionate to the platform's share."],
    related=["<b>Cost-aware architecture</b> (this volume)", "<b>Data classification &amp; residency</b> (this volume)", "<b>Quality attribute utility tree</b> (this volume)", "<b>Cost visibility (FinOps)</b> (patterns, Vol. 6)"],
    quiz=[("What are the four steps?", "Measure, use less, shift flexible work, choose cleaner places."),
          ("Why express emissions per order?", "Totals rise with growth; per order shows real improvement."),
          ("What was Larder's platform figure?", "About 0.9 g CO₂e per order, cut to about 0.6 g."),
          ("What did Ana say honestly?", "That deliveries by e-bike and van matter far more than the platform.")],
    try_it="Find your cloud provider's carbon report for last year. Divide by your main business unit, list two things you could switch off or delete, and one flexible job you could move to a cleaner hour.",
    remember="Read the <span class=\"hl\">meter</span> first; then use less, shift and <span class=\"hl\">choose</span>.",
    sources=["Green Software Foundation, Software Carbon Intensity (SCI) Specification (ISO/IEC 21031:2024).",
             "Anne Currie, Sarah Hsu and Sara Bergman, <i>Building Green Software</i> (2024).",
             "Green Software Foundation, “Principles of Green Software Engineering”.",
             "GHG Protocol, Corporate Value Chain (Scope 3) Standard (2011)."],
)

# ------------------------------------------------------------------ 15 Quality Attribute Utility Tree
ut_problem = Doodle(760, 280, "Doodle of March 2028. The board has approved eight cities and 60,000 orders a day by the end of 2028. In the planning meeting every leader names the quality that matters most: Femke resilience, Marco cost, Joost speed for pickers, Lena compliance, Priya app speed. Everything is top priority, so nothing is.",
                    "Eight cities, 60,000 orders a day. Every leader's quality is top priority, so nothing is.")
for i, (who, q, f) in enumerate([("Femke", "resilience", "pink"), ("Marco", "cost", "y"), ("Joost", "pickers' speed", "blue"), ("Lena", "compliance", "green"), ("Priya", "app speed", "paper")]):
    ut_problem.box(14 + i * 148, 40, 138, 90, who, f, sub=q, size=16, subsize=14)
ut_problem.note(380, 200, "everything is top priority", "red", size=20)

ut_analogy = Doodle(760, 250, "Doodle of a family choosing a house: they list what matters (space, schools, commute, garden, price), turn each into something concrete (three bedrooms, under thirty minutes to work), and mark each must-have or nice-to-have and easy or hard to find. The hard must-haves decide where they look.",
                     "Choosing a house: concrete wishes, each marked must-have or nice, easy or hard. The hard must-haves decide the search.")
ut_analogy.icon("castle", 30, 60, 1.2)
for i, (t, s, f) in enumerate([("3 bedrooms", "must · easy", "green"), ("short commute", "must · hard", "pink"), ("garden", "nice · hard", "paper")]):
    ut_analogy.box(150 + i * 200, 50, 186, 90, t, f, sub=s, size=15)
ut_analogy.note(450, 205, "hard must-haves decide the search", "pen")

ut_how = Doodle(760, 420, "Larder's utility tree from the workshop on 20 March 2028 with Femke, Marco, Joost, Lena, Priya and Grace. Each quality refined into concrete scenarios, each rated for business importance and difficulty, high, medium or low. High and high: checkout at 5 times peak with 60,000 orders a day, p95 under 800 milliseconds; a new city live in six weeks by configuration. High and medium: a new country's rules live in a month; cloud cost per order under 6 cents. Medium and high: survive a region outage within an hour, stays parked under ADR 0026's triggers. Low and medium: real-time recommendations, dropped. The high-high scenarios become the 2028 architecture priorities, in that order.",
                 "Qualities → concrete scenarios → rated (importance, difficulty). The (H, H) scenarios lead 2028.")
ut_how.box(14, 14, 160, 380, "utility", "paper", size=18)
for i, (sc, r, f) in enumerate([("checkout 5× at 60k/day, p95 < 800 ms", "H, H", "pink"), ("new city live in 6 weeks (config)", "H, H", "pink"),
                                ("new country's rules in a month", "H, M", "y"), ("cloud cost < 6 cents / order", "H, M", "y"),
                                ("region outage: back within 1 h", "M, H", "blue"), ("real-time recommendations", "L, M", "paper")]):
    y = 14 + i * 64
    ut_how.arrow(176, 200, 206, y + 26)
    ut_how.box(210, y, 536, 52, None, f, rx=6)
    ut_how.text(226, y + 32, sc, anchor="start", size=14)
    ut_how.text(730, y + 32, r, "t-head", anchor="end", size=15)
ut_how.note(470, 412, "(H, H) first · (M, H) parked · (L, M) dropped", "pen", size=15)

UTILITY = dict(
    slug="utility-tree",
    kicker="a.k.a. “choosing a house”",
    tldr="A <b>quality attribute utility tree</b> turns “everything matters” into a ranked list. Start with the qualities (performance, availability, security, cost…), refine each into <b>concrete scenarios</b> with numbers, and rate each scenario for <b>business importance</b> and <b>technical difficulty</b> (high, medium, low). The <b>high-importance, high-difficulty</b> scenarios drive the architecture; the rest are handled routinely, parked or dropped. Built with the people who own the priorities.",
    chips=[("Family", "cost &amp; balance"), ("Origin", "ATAM, Software Engineering Institute (Kazman, Klein, Clements, 2000)"), ("Lives in", "the year's architecture plan, next to the roadmap"), ("Pairs with", "quality attribute scenarios, architecture roadmap, trade-off sliders")],
    problem_side="Larder, 20 March 2028",
    problem="""  <p class="lead">The board has approved <b>eight cities and 60,000 orders a day</b> by the end of 2028. In the planning meeting each leader names the quality that matters most: Femke <b>resilience</b>, Marco <b>cost</b>, Joost <b>speed for pickers</b>, Lena <b>compliance</b>, Priya <b>app speed</b>. <span class="hl-pink">Everything is top priority, so nothing is</span>, and Ana can't plan a year of architecture work around five equal wishes.</p>
  <ul>
    <li>Qualities in the abstract can't be ranked.</li>
    <li>Leaders each see their own part.</li>
    <li>Without a ranking, the loudest wish wins.</li>
  </ul>""",
    problem_figs=[ut_problem],
    analogy_side="choosing a house",
    analogy="""  <p>A family choosing a house lists what matters (<b>space, schools, commute, garden, price</b>), turns each into something concrete (<b>three bedrooms</b>, <b>under thirty minutes to work</b>), and marks each <b>must-have or nice</b>, <b>easy or hard</b> to find. The hard must-haves decide where they look; the easy ones take care of themselves.</p>""",
    analogy_figs=[ut_analogy],
    map=[("Space, schools, commute", "Performance, availability, cost, compliance"),
         ("Three bedrooms, ≤ 30 min", "Scenarios with numbers"),
         ("Must-have or nice", "Business importance: H, M, L"),
         ("Easy or hard to find", "Technical difficulty: H, M, L"),
         ("Hard must-haves decide the search", "(H, H) scenarios lead the 2028 plan")],
    how_side="qualities → scenarios → (importance, difficulty)",
    how="""  <p>Ana ran a half-day workshop with Femke, Marco, Joost, Lena, Priya and Grace. Each quality became concrete scenarios, rated together. <b>(H, H)</b>: checkout at 5× peak with <b>60,000 orders a day</b>, p95 under 800 ms; a <b>new city live in six weeks</b> by configuration. <b>(H, M)</b>: a new country's rules in a month; cloud cost under 6 cents an order. <b>(M, H)</b>: back within an hour after a region outage, <b>parked</b> under ADR 0026's triggers. <b>(L, M)</b>: real-time recommendations, <b>dropped</b>. The (H, H) scenarios became the 2028 architecture priorities, in that order.</p>""",
    how_figs=[ut_how],
    steps=[("Invite the owners of the priorities", "Leaders and product, not just engineers."),
           ("List the qualities", "Performance, availability, security, cost, modifiability…"),
           ("Refine into scenarios", "Concrete, with numbers: stimulus, environment, response."),
           ("Rate importance and difficulty", "H, M, L each, together."),
           ("Act on (H, H) first", "These drive the architecture work."),
           ("Park or drop the rest", "With the reason written down.")],
    vocab=[("Utility tree", "A tree from “utility” to qualities to rated scenarios."),
           ("Quality attribute", "A property like performance, availability or cost."),
           ("Scenario", "A concrete, testable statement of a quality."),
           ("ATAM", "Architecture Tradeoff Analysis Method, where utility trees come from."),
           ("Business importance", "How much the scenario matters to the business."),
           ("Technical difficulty", "How hard it is to achieve with the architecture.")],
    code=dict(file="docs/architecture/utility-tree-2028.md", note="the utility tree, 20 March 2028", plain=True, src="""
# Utility tree · 2028 · workshop 20 Mar · Femke, Marco, Joost, Lena, Priya, Grace, Ana
Ratings: (business importance, technical difficulty)

Performance   checkout at 5× Friday peak with 60k orders/day, p95 < 800 ms           (H, H) → priority 1
              picker: scan → next item ≤ 1 s on store Wi-Fi                          (H, L)
Modifiability new city live in 6 weeks, by configuration only                         (H, H) → priority 2
              new country's legal rules live within a month                          (H, M) → priority 3
Cost          cloud cost per order < 6 cents at 60k orders/day                       (H, M) → priority 4
Availability  ordering 99.8 %/month (Korenwolf SLA)                                  (H, M)
              region outage: ordering back within 1 h                                (M, H) → parked (ADR 0026)
Security      every new trust boundary reviewed before go-live                       (H, L)
Features      real-time recommendations on the home screen                           (L, M) → dropped
"""),
    tools="tools: a whiteboard or a shared doc; the scenario format from vol. 1; dot-voting or consensus for ratings; the architecture roadmap for the outcome.",
    gains=["<b>A ranked list</b> instead of five equal wishes.",
           "<b>Leaders rate together</b>, so they own it.",
           "<b>Concrete scenarios</b> become tests.",
           "<b>Parked and dropped</b> items explained.",
           "<b>The year's plan</b> follows directly."],
    losses=["<b>Half a day</b> of leaders' time.",
            "<b>Ratings are judgments</b>.",
            "<b>Needs good facilitation</b>.",
            "<b>Must be redone</b> when strategy changes."],
    baseline="Each line compares <b>every leader naming their own top quality</b> to <b>a utility tree of concrete scenarios rated for importance and difficulty, built together</b>.",
    ratings=[(2, 5, "One tree: qualities, scenarios, ratings."),
             (1, 5, "Six leaders rated it together."),
             (2, 4, "The 2028 priorities fell out of the tree."),
             (2, 4, "Hard, important scenarios get the effort."),
             (3, 4, "Redone when the strategy changes."),
             (2, 5, "Each priority traces to a scenario."),
             (2, 4, "Cost is one rated quality among others."),
             (3, 3, "Half a day once a year."),
             (3, 4, "Teams pick up scenarios as their own goals.")],
    pitfalls=[("Abstract qualities", "“Scalable”, “secure”.", "concrete scenarios with numbers."),
              ("Engineers only", "Leaders not in the room.", "the owners of the priorities rate."),
              ("Everything (H, H)", "No ranking after all.", "force a spread; compare pairs."),
              ("A poster, not a plan", "The tree never used again.", "turn (H, H) into the roadmap.")],
    use=["Yearly architecture planning.",
         "Big new goals (cities, volume, markets).",
         "When stakeholders disagree on priorities.",
         "Evaluating a major design (ATAM-style)."],
    skip=["Small systems with one obvious quality."],
    related=["<b>Quality attribute scenarios</b> (vol. 1)", "<b>Trade-off sliders</b> (vol. 2)", "<b>Architecture roadmap</b> (vol. 3)", "<b>Back-of-the-envelope estimation</b> (this volume)"],
    quiz=[("What are the two ratings in a utility tree?", "Business importance and technical difficulty."),
          ("Which scenarios drive the architecture?", "High importance and high difficulty: (H, H)."),
          ("What happened to region failover within an hour?", "Rated (M, H) and parked under ADR 0026's triggers."),
          ("Why include leaders?", "They own the priorities, so they must rate them.")],
    try_it="List your system's four most important qualities. Write two concrete scenarios with numbers for each, rate them (importance, difficulty) with your product lead, and circle the (H, H) ones as next quarter's architecture priorities.",
    remember="Mark the <span class=\"hl\">must-haves</span> and the <span class=\"hl\">hard</span> ones; they decide the search.",
    sources=["Rick Kazman, Mark Klein and Paul Clements, “ATAM: Method for Architecture Evaluation” (SEI, CMU/SEI-2000-TR-004).",
             "Paul Clements, Rick Kazman and Mark Klein, <i>Evaluating Software Architectures</i> (2001).",
             "Len Bass, Paul Clements and Rick Kazman, <i>Software Architecture in Practice</i>, 4th ed. (2021).",
             "Neal Ford and Mark Richards, <i>Fundamentals of Software Architecture</i> (2020), architecture characteristics."],
)

NOTES = [TCO, COSTAWARE, GREEN, UTILITY]
