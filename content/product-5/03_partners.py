# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 5 · Partners inside.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 08 Operations as a Customer
oc_problem = Doodle(760, 280, "Doodle of January 2027. The picker app gets whatever time is left after customer features. Joost's list of picker problems is two years old; sync conflicts at Noord still cause about twelve wrong swaps packed a week. Joost says ops is everyone's second customer and nobody's first.",
                    "The picker app gets leftover time. Joost: “ops is everyone's second customer and nobody's first.”")
oc_problem.box(20, 40, 320, 90, "picker app", "paper", sub="leftover time")
oc_problem.box(400, 40, 340, 90, "12 wrong swaps / week", "pink", sub="sync conflicts, Noord", stroke="red")
oc_problem.note(380, 200, "nobody's first customer", "red", size=20)

oc_analogy = Doodle(760, 250, "Doodle of a restaurant's kitchen tools: the owner who only buys for the dining room, new chairs, new menus, while the kitchen's oven runs cold on one side. The food that reaches the customer is made in the kitchen.",
                     "A restaurant that only buys for the dining room, while the oven runs cold on one side.")
oc_analogy.icon("kitchen", 30, 60, 1.3)
oc_analogy.box(150, 50, 280, 100, "dining room", "y", sub="new chairs, new menus")
oc_analogy.box(460, 50, 280, 100, "kitchen", "pink", sub="the oven runs cold")
oc_analogy.note(450, 210, "the food is made in the kitchen", "pen")

oc_how = Doodle(760, 400, "How Grace and Joost treat operations as a customer from 18 January 2027. The picker app gets its own outcomes: picking time per order and wrong items packed per thousand orders. A fixed share of capacity, 20 percent of Dee's team. A quarterly operations roadmap reviewed with Joost. Tomás as the customer representative, at refinement every other week. By March: sync conflicts fixed, wrong swaps packed from twelve a week to one; picking time per order from 6 minutes 40 to 6 minutes 5.",
                 "Its own outcomes, a fixed share of capacity, a roadmap with Joost, and Tomás in refinement.")
for i, (t, s, f) in enumerate([("outcomes", "picking time · wrong items / 1,000", "green"), ("capacity", "20 % of Dee's team", "y"), ("roadmap", "quarterly, with Joost", "blue"), ("customer rep", "Tomás, every other week", "paper")]):
    r, c = divmod(i, 2)
    oc_how.box(14 + c * 372, 14 + r * 96, 360, 84, t, f, sub=s, size=17)
oc_how.box(14, 214, 360, 70, "wrong swaps packed", "green", sub="12 → 1 a week", size=16)
oc_how.box(386, 214, 360, 70, "picking per order", "green", sub="6:40 → 6:05", size=16)
oc_how.note(380, 326, "by March 2027", "pen", size=17)

OPSCUST = dict(
    slug="operations-as-customer",
    kicker="a.k.a. “the kitchen, not just the dining room”",
    tldr="The tools your operations staff use (pickers' handhelds, couriers' app, support's tools) are <b>products with customers</b> too, and they shape what end customers get. Treat them that way: give them their <b>own outcomes</b>, a <b>fixed share of capacity</b>, a <b>roadmap</b> reviewed with the operations lead, and a <b>customer representative</b> from the floor. Otherwise they get leftover time, and customer features fail in the kitchen.",
    chips=[("Family", "partners inside"), ("Origin", "service design; internal product management"), ("Lives in", "the roadmap, as its own lane with its own outcomes"), ("Pairs with", "feedback loops with operations, OKRs, the product trio")],
    problem_side="Larder, 18 January 2027",
    problem="""  <p class="lead">The picker app gets <b>whatever time is left</b> after customer features. Joost's list of picker problems is two years old; <b>sync conflicts</b> at Noord still cause about <b>twelve wrong swaps packed a week</b>, undoing the approvals work at the last step. Joost puts it plainly: <span class="hl-pink">“ops is everyone's second customer and nobody's first.”</span></p>
  <ul>
    <li>Internal tools get leftover time.</li>
    <li>Operations problems reach customers anyway.</li>
    <li>Without outcomes, internal work can't compete for priority.</li>
  </ul>""",
    problem_figs=[oc_problem],
    analogy_side="the kitchen and the dining room",
    analogy="""  <p>A restaurant owner who only buys for the <b>dining room</b> (new chairs, new menus) while the <b>kitchen's oven runs cold on one side</b> will get complaints about the food, however nice the chairs. The food that reaches the customer is made in the kitchen.</p>""",
    analogy_figs=[oc_analogy],
    map=[("The dining room", "The customer apps"),
         ("The kitchen", "The picker app, handhelds and store tools"),
         ("The cold oven", "Sync conflicts packing the wrong swaps"),
         ("Buying for the kitchen", "20 % of Dee's team for operations"),
         ("The head chef", "Joost, with Tomás as the voice of the floor")],
    how_side="outcomes, capacity, roadmap, a rep",
    how="""  <p>Grace and Joost gave the picker app its <b>own outcomes</b>: <b>picking time per order</b> and <b>wrong items packed per 1,000 orders</b>. It gets <b>20 % of Dee's team</b>, a <b>quarterly roadmap</b> reviewed with Joost, and <b>Tomás</b> joins refinement every other week as the customer rep. First item: sync conflicts. By March, wrong swaps packed fell from <b>12 to 1 a week</b>, and picking time per order from <b>6:40 to 6:05</b>.</p>""",
    how_figs=[oc_how],
    steps=[("Name the internal customers", "Pickers, couriers, support, finance."),
           ("Give their tools outcomes", "Time per task, errors, satisfaction."),
           ("Reserve capacity", "A fixed share, not leftovers."),
           ("Run a roadmap with their lead", "Quarterly, like any product."),
           ("Bring a rep from the floor", "In refinement and demos."),
           ("Report their outcomes too", "In the update and the review.")],
    vocab=[("Internal customer", "A colleague who uses a tool you own."),
           ("Operational tool", "Software staff use to run the service."),
           ("Capacity allocation", "A fixed share of team time for a kind of work."),
           ("Customer rep", "Someone who speaks for the users in the team."),
           ("Picking time", "How long it takes to pick an order."),
           ("Sync conflict", "Two devices disagreeing about the same data.")],
    code=dict(file="product/ops/picker-roadmap-2027-q1.md", note="the operations lane, Q1 2027", plain=True, src="""
# Picker & store tools · Q1 2027 · owners: Grace with Joost · rep: Tomás · 20 % of Dee's team

Outcomes   picking time per order 6:40 → ≤ 6:15 · wrong items packed per 1,000 orders 4.2 → ≤ 2.0
Now        sync conflicts (12 wrong swaps/week at Noord) → fixed 15 Feb
           bigger allergen warning on substitutes (from the idea button)
Next       crate labels for business orders · offline mode for Rotterdam's back room
Later      picker training mode for new stores (Utrecht, April)
Review     with Joost, first Monday of each quarter · Tomás at refinement every other Thursday
Result (31 Mar)   wrong swaps packed 12 → 1 a week · picking per order 6:05 · wrong items 1.8 per 1,000
"""),
    tools="tools: the roadmap with an operations lane, the health page with operations outcomes, the idea button, refinement with a floor representative.",
    gains=["<b>Operations problems fixed</b>, not listed.",
           "<b>Customers benefit</b>: fewer wrong items.",
           "<b>Trust with Joost</b> and the stores.",
           "<b>Internal work competes</b> on outcomes.",
           "<b>Faster stores</b>: 35 seconds per order."],
    losses=["<b>Less capacity</b> for customer features.",
            "<b>Another roadmap</b> to run.",
            "<b>Store visits</b> and reps take time.",
            "<b>Operations asks</b> can grow."],
    baseline="Each line compares <b>internal tools getting leftover time</b> to <b>operations tools with their own outcomes, capacity, roadmap and a floor representative</b>.",
    ratings=[(2, 4, "Fewer wrong items reach customers."),
             (2, 4, "35 seconds less per order."),
             (2, 4, "Measured outcomes for the picker app."),
             (3, 4, "Tomás's feedback every other week."),
             (2, 4, "A fixed 20 %: no arguing each sprint."),
             (2, 4, "Store and product teams share the outcomes."),
             (1, 5, "Joost: “first time we're someone's first customer.”"),
             (3, 4, "Small store fixes ship weekly."),
             (3, 3, "A quarterly review and a rep.")],
    pitfalls=[("Leftovers", "“When we have time.”", "a fixed share of capacity."),
              ("No outcomes", "A wish list from ops.", "time per task, errors."),
              ("Managers only", "Joost speaks for pickers.", "a rep from the floor."),
              ("Separate world", "Ops tools never in reviews.", "report their outcomes too.")],
    use=["Products with operations staff.",
         "When customer problems start in operations.",
         "Internal tools nobody owns.",
         "Before scaling to new stores or cities."],
    skip=["Products without operational users."],
    related=["<b>Feedback loops with operations</b> (Vol. 4)", "<b>The product trio</b> (Vol. 3)", "<b>Working with account managers</b> (this volume)", "<b>OKRs</b> (Vol. 4)"],
    quiz=[("Why treat operations as a customer?", "Their tools shape what end customers get, and leftover time leaves problems unfixed."),
          ("What outcomes did the picker app get?", "Picking time per order and wrong items packed per 1,000 orders."),
          ("How much capacity?", "20 % of Dee's team."),
          ("What changed by March?", "Wrong swaps packed 12 → 1 a week; picking time 6:40 → 6:05.")],
    try_it="Pick one internal tool your team owns. Write two outcomes for it, agree a fixed share of capacity with its users' lead, and invite one front-line user to your next refinement.",
    remember="Buy for the <span class=\"hl\">kitchen</span>, not only the <span class=\"hl\">dining room</span>.",
    sources=["Marc Stickdorn et al., <i>This Is Service Design Doing</i> (2018).",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), platform and internal products.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019).",
             "Jeffrey Liker, <i>The Toyota Way</i> (2004)."],
)

# ------------------------------------------------------------------ 09 Working with Legal & Privacy
lp_problem = Doodle(760, 280, "Doodle of November 2026. The live order timeline for the web shop shows the courier's first name and, Noor proposes, their position on a map. Last time a privacy question came up, Lena saw the feature two days before launch and it was delayed three weeks. Grace expects the same again.",
                    "Last time Lena saw a feature two days before launch, and it slipped three weeks. The timeline shows couriers' names.")
lp_problem.box(20, 40, 320, 90, "live timeline", "y", sub="courier's name + map")
lp_problem.box(400, 40, 340, 90, "last time", "pink", sub="Lena: 2 days before → 3 weeks late")
lp_problem.note(380, 200, "legal as a gate at the end", "red", size=20)

lp_analogy = Doodle(760, 250, "Doodle of building a house with a structural engineer: you invite them when you sketch the plan, not after the walls are up. A question on paper costs a conversation; the same question after building costs a wall.",
                     "Invite the structural engineer when you sketch, not after the walls are up.")
lp_analogy.icon("frame", 40, 60, 1.3)
lp_analogy.box(170, 50, 270, 90, "at the sketch", "green", sub="a conversation")
lp_analogy.box(470, 50, 270, 90, "after the walls", "pink", sub="a wall")
lp_analogy.note(450, 205, "early is cheap", "pen")

lp_how = Doodle(760, 400, "How Grace worked with Lena on the live timeline, 9 November 2026. One page sent at design time: what data, whose, why, who sees it, how long it's kept. A thirty-minute conversation, not a review at the end. Agreed: the courier's first name only, and couriers may choose a nickname; the map position shown only for the last ten minutes, on approach; nothing kept after delivery; couriers told before launch. Done in a week, launched on time. From then on: a monthly privacy office hour with Lena.",
                 "A one-page question at design time, a short conversation, privacy designed in. Launched on time.")
lp_how.box(14, 14, 732, 56, "one page: what data · whose · why · who sees it · how long", "paper", size=15)
for i, (t, sub) in enumerate([("name", "first or nickname"), ("map", "last 10 min only"), ("history", "none after delivery"), ("couriers", "told first")]):
    lp_how.box(14 + i * 184, 92, 174, 80, t, "green", sub=sub, size=17, subsize=14)
lp_how.box(14, 196, 732, 56, "a week, not three · launched on time", "y", size=16)
lp_how.note(380, 292, "monthly privacy office hour with Lena", "pen", size=16)
lp_how.note(380, 326, "Lena: “a question I can answer, early”", "green", size=16)

LEGAL = dict(
    slug="legal-privacy",
    kicker="a.k.a. “the structural engineer at the sketch”",
    tldr="Legal and privacy colleagues become a gate at the end only when they're invited at the end. Bring them in <b>at design time</b> with a <b>clear, one-page question</b>: what data, whose, why, who sees it, how long it's kept. Have a short conversation, design privacy in (collect less, show less, keep less), and set up a <b>regular office hour</b>. Early questions cost a conversation; late ones cost weeks.",
    chips=[("Family", "partners inside"), ("Origin", "privacy by design (GDPR Art. 25); data protection impact assessments"), ("Lives in", "a one-page privacy question per feature, and a monthly office hour"), ("Pairs with", "one-page PRD, data classification, compliance by design")],
    problem_side="Larder, 9 November 2026",
    problem="""  <p class="lead">The <b>live order timeline</b> on the web shop will show the courier's first name, and Noor proposes their <b>position on a map</b>. Last time a privacy question came up, Lena saw the feature <b>two days before launch</b> and it slipped <b>three weeks</b>. <span class="hl-pink">Grace expects the same again</span>, and is tempted not to ask.</p>
  <ul>
    <li>Late legal reviews delay launches.</li>
    <li>Not asking is worse: problems reach customers and couriers.</li>
    <li>Vague questions get cautious answers.</li>
  </ul>""",
    problem_figs=[lp_problem],
    analogy_side="the structural engineer",
    analogy="""  <p>When you build a house you invite the <b>structural engineer</b> while you're <b>sketching</b>, not after the walls are up. A question on paper costs a conversation; the same question after building costs <b>a wall</b>.</p>""",
    analogy_figs=[lp_analogy],
    map=[("The structural engineer", "Lena, legal and data protection officer"),
         ("The sketch", "Noor's first designs of the timeline"),
         ("A question on paper", "One page: data, whose, why, who sees it, how long"),
         ("Taking down a wall", "A three-week delay before launch"),
         ("A load-bearing wall", "The courier's live position")],
    how_side="a one-page question, early, and privacy designed in",
    how="""  <p>Grace sent Lena <b>one page at design time</b>: what data, whose, why, who sees it, how long it's kept. They talked for <b>thirty minutes</b>. Agreed: the courier's <b>first name only</b> (couriers may choose a nickname); the map shown only for the <b>last ten minutes</b>, on approach; <b>nothing kept</b> after delivery; couriers told before launch. Done in a week; the timeline launched on time. Since then: a <b>monthly privacy office hour</b>.</p>""",
    how_figs=[lp_how],
    steps=[("Ask at design time", "When designs are sketches, not code."),
           ("Write a one-page question", "What data, whose, why, who sees it, how long."),
           ("Talk, briefly", "Thirty minutes beats a long email thread."),
           ("Design privacy in", "Collect less, show less, keep less."),
           ("Tell the people affected", "Customers, couriers, staff."),
           ("Hold a regular office hour", "Small questions answered early.")],
    vocab=[("DPO", "Data protection officer."),
           ("Personal data", "Information about an identifiable person."),
           ("DPIA", "Data protection impact assessment, for risky processing."),
           ("Data minimisation", "Collecting only what's needed."),
           ("Retention", "How long data is kept."),
           ("Privacy by design", "Building data protection in from the start.")],
    code=dict(file="product/privacy/live-timeline.md", note="the one-page question for Lena, 9 November 2026", plain=True, src="""
# Privacy question · live order timeline (web) · Grace → Lena · 9 Nov 2026

What data      courier first name; courier position (map); order status times
Whose          couriers (employees and contractors); customers (address, order)
Why            customers asked "where is my order?" (11.2 per 1,000 orders); panel: name, not map
Who sees it    the customer of that order only, while the order is on its way
How long       live only; nothing stored for the timeline after delivery
Agreed 16 Nov  first name or a chosen nickname · map only in the last 10 minutes, on approach ·
               no history after delivery · couriers told by Joost's team 1 week before launch
Launched       web, on time · no DPIA needed (Lena), noted in the processing register
"""),
    tools="tools: a one-page privacy question template, the processing register, a monthly office-hour slot, the data classes.",
    gains=["<b>No late surprises</b> before launch.",
           "<b>Better designs</b>: less data, shown less.",
           "<b>Trust with couriers</b>.",
           "<b>Lena's time</b> used well.",
           "<b>Launches on time</b>."],
    losses=["<b>Writing the question</b> takes an hour.",
            "<b>Some ideas</b> get smaller.",
            "<b>Legal capacity</b> is limited.",
            "<b>Not every answer</b> is quick."],
    baseline="Each line compares <b>showing legal a finished feature before launch</b> to <b>a one-page question at design time, a short conversation and privacy designed in</b>.",
    ratings=[(2, 4, "Customers get the timeline; couriers keep their privacy."),
             (3, 4, "Launched on time."),
             (3, 4, "A clear question gets a clear answer."),
             (2, 4, "Answered in a week, not three."),
             (3, 3, "Neutral."),
             (2, 4, "Grace, Noor, Lena and Joost agree the rules."),
             (2, 5, "Lena trusts the product team to ask early."),
             (2, 4, "No last-minute delays."),
             (2, 4, "One page and thirty minutes.")],
    pitfalls=[("Asking at the end", "Two days before launch.", "at design time."),
              ("Vague questions", "“Is this GDPR-OK?”", "what, whose, why, who, how long."),
              ("Not asking", "Hoping nobody notices.", "ask early; it's cheaper."),
              ("Forgetting staff", "Couriers learn from customers.", "tell the people affected first.")],
    use=["Any feature using or showing personal data.",
         "New markets, new data, new partners.",
         "Contracts and terms changes.",
         "Anything shown to people outside the company."],
    skip=["Changes with no personal data and no legal effect."],
    related=["<b>The one-page PRD</b> (this volume)", "<b>Customer advisory panel</b> (Vol. 4)", "<b>Data classification &amp; residency</b> (Ana, book 1 vol. 5)", "<b>Compliance by design</b> (Ana, book 1 vol. 5)"],
    quiz=[("When should legal be involved?", "At design time, while designs are still sketches."),
          ("What goes on the one-page question?", "What data, whose, why, who sees it, how long it's kept."),
          ("What did Lena and Grace agree?", "First name or nickname, map only in the last ten minutes, nothing kept, couriers told first."),
          ("What's privacy by design here?", "Collect less, show less, keep less.")],
    try_it="Pick a feature in design that touches personal data. Write the one-page question (what, whose, why, who sees it, how long) and book thirty minutes with your legal or privacy colleague this week.",
    remember="Invite the <span class=\"hl\">engineer</span> at the <span class=\"hl\">sketch</span>.",
    sources=["Regulation (EU) 2016/679 (GDPR), Articles 5, 25 and 35.",
             "Ann Cavoukian, “Privacy by Design: The 7 Foundational Principles” (2009).",
             "Dutch Data Protection Authority (Autoriteit Persoonsgegevens), guidance on DPIAs.",
             "Michelle Finneran Dennedy et al., <i>The Privacy Engineer's Manifesto</i> (2014)."],
)

# ------------------------------------------------------------------ 10 Working with the Architect
wa_problem = Doodle(760, 280, "Doodle of January 2027. After the Christmas outage, Ana's new rule protects the critical windows: no changes on Fridays 17:00 to 20:00 or on weekday mornings 07:00 to 09:00. Grace hears about it after it's decided, and her order-editing test, planned for Friday evenings, no longer fits. Ana didn't know about the test.",
                    "Ana's new rule meets Grace's test plan for the first time after both are decided.")
wa_problem.box(20, 40, 320, 90, "ADR 0017", "blue", sub="no changes in critical windows")
wa_problem.box(400, 40, 340, 90, "order-editing test", "y", sub="planned for Friday evenings")
wa_problem.note(380, 200, "two good plans, found out about each other late", "red", size=18)

wa_analogy = Doodle(760, 250, "Doodle of a client and an architect designing a house: the client brings how the family lives and what matters; the architect brings what the ground, the budget and the rules allow, with options and their costs. Neither designs alone.",
                     "The family brings how they live; the architect brings what the ground allows. Neither designs alone.")
wa_analogy.icon("castle", 30, 60, 1.2)
wa_analogy.box(150, 50, 280, 100, "the family", "y", sub="how we live, what matters")
wa_analogy.box(460, 50, 280, 100, "the architect", "blue", sub="what's possible, at what cost")
wa_analogy.note(450, 210, "neither designs alone", "pen")

wa_how = Doodle(760, 400, "How Grace and Ana work together from 12 January 2027. Thirty minutes every week. Grace brings the why: next quarter's outcomes and bets, early. Ana brings the how: constraints, options and their costs. Decisions are recorded on both sides: the PRD links the ADR, the ADR names the product outcome. Example: the order-editing test; Ana proposed closing the edit window before the order is released to the store, so picking never changes and the critical windows aren't touched. The test moved to weekday afternoons.",
                 "Weekly: Grace brings the why early, Ana brings constraints and options. Both sides record the decision.")
wa_how.box(14, 14, 360, 110, None, "y")
wa_how.head(194, 46, "Grace: why", size=17)
wa_how.text(194, 78, "outcomes, bets, next quarter", size=14)
wa_how.text(194, 104, "early, before designs", size=14)
wa_how.box(386, 14, 360, 110, None, "blue")
wa_how.head(566, 46, "Ana: how", size=17)
wa_how.text(566, 78, "constraints, options, costs", size=14)
wa_how.text(566, 104, "before decisions", size=14)
wa_how.box(14, 144, 732, 56, "PRD links the ADR · ADR names the outcome", "green", size=16)
wa_how.box(14, 220, 732, 70, None, "paper")
wa_how.head(380, 248, "edit window closes before release to the store", size=15)
wa_how.text(380, 276, "picking never changes · test on weekday afternoons", size=14)
wa_how.note(380, 330, "thirty minutes a week, Tuesdays", "pen", size=16)

ARCHITECT = dict(
    slug="working-with-architect",
    kicker="a.k.a. “the family and the architect”",
    tldr="A product owner and an architect answer different questions about the same product: <b>why and for whom</b>, and <b>how, within which limits</b>. Work as partners: meet <b>regularly</b>, bring your <b>outcomes and bets early</b> (before designs), ask for <b>constraints and options with costs</b> (before decisions), and record decisions on <b>both sides</b> (the PRD links the ADR; the ADR names the product outcome). Most clashes are just two good plans meeting too late.",
    chips=[("Family", "partners inside"), ("Origin", "product–engineering partnership; architecture decision records"), ("Lives in", "a weekly 30 minutes, and links between PRDs and ADRs"), ("Pairs with", "the product trio, one-page PRD, dependencies across teams")],
    problem_side="Larder, 12 January 2027",
    problem="""  <p class="lead">After the Christmas outage, Ana's new rule (ADR 0017) protects the <b>critical windows</b>: no changes on Fridays 17:00–20:00 or weekday mornings 07:00–09:00. Grace hears about it <b>after it's decided</b>, and her <b>order-editing test</b>, planned for Friday evenings, no longer fits. <span class="hl-pink">Ana didn't know about the test.</span> Two good plans met each other too late.</p>
  <ul>
    <li>Architecture decisions change what product can do, and when.</li>
    <li>Product bets change what architecture must support.</li>
    <li>Meeting only when there's a clash makes every meeting a clash.</li>
  </ul>""",
    problem_figs=[wa_problem],
    meanwhile=[("architect-3", "explaining-trade-offs", "the same day, Ana explains to Femke why 99.99 % would cost a second region, and Grace learns what the new rule means for her test.",
                "The same day, Grace and Ana start their weekly thirty minutes, after ADR 0017 and the order-editing test collided.")],
    analogy_side="the family and the architect",
    analogy="""  <p>When a family builds a house, they bring <b>how they live</b> and what matters (a big kitchen, a quiet study); the <b>architect</b> brings what the ground, the budget and the building rules allow, with <b>options and their costs</b>. Neither designs the house alone, and both sign the plans.</p>""",
    analogy_figs=[wa_analogy],
    map=[("How the family lives", "Outcomes and bets: order editing, Korenwolf"),
         ("What the ground allows", "Constraints: critical windows, picking flow"),
         ("Options with costs", "Close the edit window before release to the store"),
         ("Both sign the plans", "The PRD links the ADR; the ADR names the outcome"),
         ("Designing alone", "ADR 0017 and the test, each decided separately")],
    how_side="the why early, the how before decisions",
    how="""  <p>Grace and Ana now meet for <b>thirty minutes every Tuesday</b>. Grace brings next quarter's <b>outcomes and bets</b> before designs start; Ana brings <b>constraints, options and costs</b> before decisions are made. Decisions are recorded on <b>both sides</b>. For the order-editing test, Ana proposed closing the edit window <b>before the order is released to the store</b>, so picking never changes and the critical windows aren't touched. The test moved to weekday afternoons and ran in February.</p>""",
    how_figs=[wa_how],
    steps=[("Meet regularly", "Weekly or fortnightly, not only when there's a clash."),
           ("Bring the why early", "Outcomes and bets for next quarter."),
           ("Ask for constraints and options", "With costs, before deciding."),
           ("Share the roadmap and the ADR log", "Each reads the other's."),
           ("Record on both sides", "PRD links ADR; ADR names the outcome."),
           ("Disagree in private, decide together", "Then present one plan.")],
    vocab=[("Solution architect", "Owns how the system is built to meet business needs."),
           ("ADR", "Architecture decision record."),
           ("Constraint", "A limit that must be respected."),
           ("Option", "One possible way to do something, with its costs."),
           ("Critical window", "Hours when no risky changes are allowed (ADR 0017)."),
           ("Trade-off", "Gaining one quality by giving up some of another.")],
    code=dict(file="product/partners/grace-ana.md", note="the weekly agenda, 19 January 2027", plain=True, src="""
# Grace ↔ Ana · Tuesdays 14:00, 30 min

FROM GRACE (why, early)
  Q1 bets: order editing (test, Feb) · Rotterdam slot swaps · Korenwolf "skip a week" in the portal
  Q2 thinking: Larder Plus (Femke) · Antwerp in French (Sep)
FROM ANA (how, before decisions)
  ADR 0017: no changes Fri 17–20, weekdays 07–09 → order-editing test on weekday afternoons
  Option for editing: close the window before release to store (no change to picking) ✓ chosen
  Coming: WMS B (ADR 0016) store by store from April: freeze dates per store
DECISIONS (recorded both sides)
  PRD "order editing" links ADR 0017 · ADR 0017 names "Korenwolf 98 % by 09:00" as the outcome
"""),
    tools="tools: a shared agenda doc, the roadmap and the ADR log read by both, links between PRDs and ADRs.",
    gains=["<b>No late clashes</b> between plans.",
           "<b>Cheaper options</b> found early.",
           "<b>Decisions traceable</b> both ways.",
           "<b>One plan</b> presented to leadership.",
           "<b>Better designs</b> from both views."],
    losses=["<b>Thirty minutes a week</b>.",
            "<b>Plans shared</b> before they're polished.",
            "<b>Disagreements</b> surface earlier.",
            "<b>Two documents</b> to keep linked."],
    baseline="Each line compares <b>product and architecture meeting only when plans clash</b> to <b>a weekly partnership: why early, constraints and options before decisions, recorded both sides</b>.",
    ratings=[(3, 4, "Order editing reached customers without touching picking."),
             (3, 4, "Korenwolf's mornings protected."),
             (2, 4, "Options compared with costs."),
             (2, 4, "Clashes found weeks earlier."),
             (2, 4, "One test, in the right hours."),
             (1, 5, "Grace and Ana each know the other's plan."),
             (2, 4, "Leaders see one plan, not two."),
             (2, 4, "No last-minute replanning."),
             (3, 3, "Thirty minutes a week.")],
    pitfalls=[("Meeting only to fight", "Every meeting a clash.", "a regular slot."),
              ("Solutions, not problems", "“Ana, build an edit button.”", "bring the outcome; ask for options."),
              ("Decisions on one side", "An ADR without the why.", "record and link both sides."),
              ("Public disagreements", "Two plans in front of Femke.", "settle it together first.")],
    use=["Any product with an architect or tech lead.",
         "Quarterly planning.",
         "Bets that touch platform rules.",
         "After a clash, to prevent the next one."],
    skip=["Never; only the rhythm changes."],
    related=["<b>The product trio</b> (Vol. 3)", "<b>The one-page PRD</b> (this volume)", "<b>Explaining trade-offs to non-engineers</b> (Ana, book 1 vol. 3)", "<b>Architecture decision records</b> (Ana, book 1 vol. 2)"],
    quiz=[("What does each bring?", "Grace: the why (outcomes, bets) early; Ana: the how (constraints, options, costs)."),
          ("How are decisions recorded?", "On both sides: the PRD links the ADR, the ADR names the outcome."),
          ("What option did Ana propose for order editing?", "Close the edit window before the order is released to the store."),
          ("Why meet regularly?", "So plans meet early, not as clashes.")],
    try_it="Book thirty minutes with your architect or tech lead. Bring next quarter's outcomes and bets, ask what constraints and options they see with costs, and agree to link each other's documents.",
    remember="The <span class=\"hl\">family</span> brings how it lives; the <span class=\"hl\">architect</span> brings what the ground allows.",
    sources=["Marty Cagan, <i>Empowered</i> (2020), product and engineering partnership.",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Michael Nygard, “Documenting Architecture Decisions” (2011).",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021), the product trio."],
)

# ------------------------------------------------------------------ 11 Working with Account Managers
am_problem = Doodle(760, 280, "Doodle of February 2027. In two months Mo has brought seventeen requests from Korenwolf: a custom invoice layout, an approval step for orders over 500 euros, delivery photos, a Korenwolf logo in the portal and more. Each arrives as urgent; Mo fears losing the renewal. Ben's team fears building a Korenwolf-only product.",
                    "Seventeen Korenwolf requests in two months, each urgent. Mo fears the renewal; Ben fears a Korenwolf-only product.")
am_problem.box(20, 40, 320, 90, "17 requests", "pink", sub="each “urgent”")
am_problem.box(400, 40, 340, 90, "Ben's team", "y", sub="“a Korenwolf fork?”")
am_problem.note(380, 200, "the biggest client designing the product", "red", size=19)

am_analogy = Doodle(760, 250, "Doodle of a tailor and an off-the-peg shop: the shop listens to a regular customer's request for longer sleeves, and if many customers want it, adds a longer size for everyone. It doesn't sew one coat for one customer in its factory.",
                     "If many customers want longer sleeves, add a size for everyone. Don't sew one coat in the factory.")
am_analogy.icon("tag", 40, 60, 1.3)
am_analogy.box(170, 50, 270, 90, "one coat, one client", "pink", sub="a custom fork")
am_analogy.box(470, 50, 270, 90, "a new size", "green", sub="for everyone")
am_analogy.note(450, 205, "solve for the many, hear the one", "pen")

am_how = Doodle(760, 400, "Grace and Mo's monthly request review from 22 February 2027. For each request: what problem is behind it, how many business clients have it, and how to solve it for all business accounts. Results for the seventeen: five built as settings for every business account, such as cost-centre splits, an approval threshold and delivery photos; four solved by operations or process; eight declined with a reason Mo can explain, including the custom invoice layout and the logo. Mo takes the answers to Ruben; two more office clients use the same settings by June.",
                 "What problem, how many clients have it, solve for all. 5 built as settings, 4 by process, 8 declined with reasons.")
am_how.box(14, 14, 732, 56, "each request: what problem? how many clients? solve for all?", "paper", size=15)
for i, (t, s, f) in enumerate([("5 built", "settings for all accounts", "green"), ("4 by process", "operations or Mo", "blue"), ("8 declined", "with reasons Mo can explain", "pink")]):
    am_how.box(14 + i * 248, 92, 236, 100, t, f, sub=s, size=18, subsize=13)
am_how.box(14, 212, 732, 56, "no Korenwolf-only code", "y", size=17)
am_how.note(380, 306, "monthly, 45 minutes, Grace + Mo", "pen", size=16)
am_how.note(380, 340, "two more office clients use the same settings by June", "green", size=15)

ACCOUNTS = dict(
    slug="account-managers",
    kicker="a.k.a. “a new size, not one coat”",
    tldr="Account managers bring the voice of your biggest clients, and with it the risk that one client designs the product. Work with them as partners: review requests <b>together, regularly</b>; for each, find the <b>problem behind it</b> and <b>how many clients share it</b>; solve shared problems <b>for everyone</b> (often as settings), solve others by <b>process</b>, and <b>decline</b> the rest with reasons the account manager can explain. No client-only code.",
    chips=[("Family", "partners inside"), ("Origin", "B2B product management; key account management"), ("Lives in", "a monthly request review and a decisions log Mo can share"), ("Pairs with", "feature request triage, saying no without burning bridges, negotiating scope")],
    problem_side="Larder, 22 February 2027",
    problem="""  <p class="lead">In two months Mo has brought <b>seventeen requests</b> from Korenwolf: a custom invoice layout, an approval step for orders over €500, delivery photos, Korenwolf's logo in the portal, and more. Each arrives as <b>urgent</b>; Mo fears losing the renewal. Ben's team fears building <span class="hl-pink">a Korenwolf-only product</span> that every future client will want copied.</p>
  <ul>
    <li>Big clients' requests feel more urgent than they are.</li>
    <li>Client-only features multiply upkeep.</li>
    <li>Account managers need answers they can explain.</li>
  </ul>""",
    problem_figs=[am_problem],
    analogy_side="a new size, not one coat",
    analogy="""  <p>An off-the-peg clothes shop listens when a regular asks for <b>longer sleeves</b>. If many customers want it, it adds a <b>longer size for everyone</b>. It doesn't sew <b>one coat for one customer</b> in its factory, because the factory would soon make nothing but exceptions.</p>""",
    analogy_figs=[am_analogy],
    map=[("A regular customer", "Korenwolf, via Mo"),
         ("Longer sleeves", "An approval step for big orders"),
         ("A size for everyone", "An approval threshold setting for all business accounts"),
         ("One coat in the factory", "A Korenwolf-only invoice layout"),
         ("The shop assistant", "Mo, explaining the answers")],
    how_side="the problem, how many, solve for all",
    how="""  <p>Grace and Mo now hold a <b>monthly request review</b>, 45 minutes. For each request: <b>what problem</b> is behind it, <b>how many business clients</b> have it, and how to solve it <b>for all</b>. Of the seventeen: <b>5 built</b> as settings for every business account (cost-centre splits, an approval threshold, delivery photos); <b>4 solved by process</b> (operations or Mo); <b>8 declined</b> with reasons Mo can explain (the custom invoice layout, the logo). Ruben accepted; by June two more office clients use the same settings.</p>""",
    how_figs=[am_how],
    steps=[("Review together, regularly", "Monthly with the account manager."),
           ("Find the problem behind it", "Ask the client why, through the account manager."),
           ("Count who shares it", "Other clients, other segments."),
           ("Solve for all", "Settings and features for every account."),
           ("Use process where it's enough", "Operations or the account manager."),
           ("Decline with reasons", "Words the account manager can repeat.")],
    vocab=[("Account manager", "Owns the relationship with key clients."),
           ("Key account", "A client important enough for special attention."),
           ("Custom fork", "A version of the product for one client."),
           ("Configuration", "Behaviour changed by settings, not code."),
           ("Renewal", "A client extending its contract."),
           ("Request log", "Decisions on requests, shareable with clients.")],
    code=dict(file="product/business/request-review-2027-02.md", note="the February request review, 22 February 2027", plain=True, src="""
# Business request review · Feb 2027 · Grace + Mo · 17 requests from Korenwolf

| Request                         | Problem behind it                      | Who else? | Decision                         |
|---------------------------------|----------------------------------------|-----------|----------------------------------|
| Split invoice by cost centre    | finance books costs per department     | 3 leads   | BUILD: setting for all accounts  |
| Approve orders > €500           | office manager's budget limit          | 2 leads   | BUILD: approval threshold setting|
| Delivery photos                 | proving delivery to reception          | all vans  | BUILD: photo at drop, for all    |
| Change order by phone at 07:30  | something forgotten                    | —         | PROCESS: Mo's number until 08:00 |
| Korenwolf invoice layout        | "our template"                         | none      | DECLINE: standard e-invoice fields |
| Korenwolf logo in the portal    | branding                               | none      | DECLINE: not worth the upkeep    |
… 11 more · summary sent to Ruben by Mo, 1 Mar
"""),
    tools="tools: a request log shared with the account manager, the feature request triage, settings for business accounts, a monthly slot.",
    gains=["<b>One product</b> for every business client.",
           "<b>Mo has answers</b> to give.",
           "<b>Real problems solved</b>, not demands copied.",
           "<b>New clients benefit</b> from the same settings.",
           "<b>Less upkeep</b> than client forks."],
    losses=["<b>Some requests declined</b>, and clients may push.",
            "<b>Settings add complexity</b>.",
            "<b>A monthly meeting</b>.",
            "<b>Account managers</b> must carry hard answers."],
    baseline="Each line compares <b>building big clients' requests as they arrive</b> to <b>a monthly review: the problem, who shares it, solve for all, process, or decline with reasons</b>.",
    ratings=[(2, 4, "Every business client gets the useful settings."),
             (2, 5, "Korenwolf renews; two more offices onboard faster."),
             (2, 4, "Requests sized by how many clients share them."),
             (3, 3, "Neutral."),
             (1, 5, "8 of 17 declined, 4 solved without code."),
             (2, 4, "Mo and Ben's team share the reasons."),
             (2, 5, "Mo can explain every answer to Ruben."),
             (3, 4, "Small settings ship monthly."),
             (2, 4, "45 minutes a month instead of daily escalations.")],
    pitfalls=[("Client-only code", "“Just for Korenwolf.”", "settings for every account, or no."),
              ("Taking requests literally", "Building the stated solution.", "ask for the problem."),
              ("No reasons", "“Product said no.”", "words Mo can repeat."),
              ("Bypassing the account manager", "Engineers called directly.", "one channel, the review.")],
    use=["B2B products with key accounts.",
         "When one client's requests dominate the backlog.",
         "Before renewals.",
         "Onboarding new business clients."],
    skip=["Products without account managers or key clients."],
    related=["<b>Feature request triage</b> (Vol. 2)", "<b>Saying no without burning bridges</b> (Vol. 2)", "<b>Negotiating scope</b> (this volume)", "<b>API-first design</b> (Ana, book 1 vol. 4)"],
    quiz=[("What three questions does each request get?", "What's the problem, how many clients have it, how to solve it for all."),
          ("What happened to the seventeen requests?", "5 built as settings, 4 solved by process, 8 declined with reasons."),
          ("Why no client-only code?", "Forks multiply upkeep and every client wants their own."),
          ("What does the account manager need?", "Answers and reasons they can explain to the client.")],
    try_it="Take your biggest client's last ten requests. For each, write the problem behind it and how many other clients share it, and sort them into build for all, process, or decline with a reason.",
    remember="Add a <span class=\"hl\">size</span> for everyone; don't sew one <span class=\"hl\">coat</span> in the factory.",
    sources=["Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on customer-driven vs sales-driven products.",
             "Blair Reeves and Benjamin Gaines, <i>Building Products for the Enterprise</i> (2018).",
             "Des Traynor, <i>Intercom on Product Management</i> (2016).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018)."],
)

NOTES = [OPSCUST, LEGAL, ARCHITECT, ACCOUNTS]
