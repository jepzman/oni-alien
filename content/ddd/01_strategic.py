# Vol. 7 · Domain-Driven Design · Finding the domain: Ubiquitous Language, Subdomains, Bounded Context, Event Storming.
# Running example: an online shop (catalogue, ordering, shipping, billing, support). Plan: docs/PLAN-code-design.md.

# ------------------------------------------------------------------ 01 Ubiquitous Language
ul_problem = Doodle(760, 270, "Doodle of three people using different words for the same thing. The shop manager says an order is a paid purchase. The code creates an Order the moment a basket gets its first item. The database stores the status as the number 3. The monthly report counts every Order row, so abandoned baskets are counted as sales and the numbers are wrong.",
                    "The manager, the code and the database use the same word for different things, and the report is wrong.")
ul_problem.box(20, 30, 220, 80, "manager", "y", sub="“order = paid”")
ul_problem.box(270, 30, 220, 80, "code", "blue", sub="Order on first item")
ul_problem.box(520, 30, 220, 80, "database", "paper", sub="status = 3")
ul_problem.arrow(244, 70, 266, 70, color="red", both=True)
ul_problem.arrow(494, 70, 516, 70, color="red", both=True)
ul_problem.box(150, 160, 460, 60, "report: 40% more “orders”", "pink", stroke="red")
ul_problem.note(380, 254, "abandoned baskets were counted as sales", "red")

ul_analogy = Doodle(760, 250, "Doodle of a restaurant kitchen. The chef calls out fire table four, eighty-six the salmon, and on the pass. Every cook knows exactly what each phrase means, so orders move fast and nobody cooks the wrong dish. A new cook learns the words in the first week.",
                     "A busy kitchen has its own words, and every cook knows exactly what each one means.")
ul_analogy.icon("kitchen", 40, 90, 1.6)
ul_analogy.note(470, 60, "“fire table 4” = start cooking now", "pen")
ul_analogy.note(470, 110, "“86 the salmon” = it's sold out", "pen")
ul_analogy.note(470, 160, "“on the pass” = ready to serve", "pen")
ul_analogy.note(470, 220, "one meaning each, used by everyone", "green")

ul_how = Doodle(760, 300, "The ubiquitous language at the centre. A glossary of terms agreed with the domain experts is used in four places: in conversations and workshops, in class and method names, in test names, and in the user interface and documentation. When a word changes in one place, it changes in all four.",
                 "One glossary, used in talk, code, tests and screens. Change a word in one place, change it everywhere.")
ul_how.box(250, 100, 260, 100, "the glossary", "y", sub="agreed with the experts")
ul_how.box(20, 20, 200, 64, "conversations", "paper", sub="workshops · tickets")
ul_how.box(540, 20, 200, 64, "code", "blue", sub="classes · methods")
ul_how.box(20, 216, 200, 64, "tests", "green", sub="test names")
ul_how.box(540, 216, 200, 64, "screens & docs", "paper", sub="labels · help")
for x1, y1, x2, y2 in [(224, 60, 250, 110), (536, 60, 510, 110), (224, 240, 250, 190), (536, 240, 510, 190)]:
    ul_how.arrow(x1, y1, x2, y2, both=True)

UBIQUITOUS = dict(
    slug="ubiquitous-language",
    kicker="a.k.a. “say what the business says, and code it that way”",
    tldr="Agree <b>one vocabulary</b> with the people who know the business, and use it <b>everywhere</b>: in meetings, in class and method names, in tests and on screens. Each word has <b>one meaning</b> inside one model. When the code and the experts use different words, a translation happens in someone's head, and <b>bugs live in translations</b>.",
    chips=[("Family", "strategic design"), ("From", "Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 2"), ("Lives in", "a glossary, the code, the tests"), ("Pairs with", "bounded context, event storming")],
    problem="""  <p class="lead">When the experts say one thing and the code says another, every conversation needs a <span class="hl-pink">translation</span>, and translations go wrong <span class="hl-pink">quietly</span>.</p>
  <ul>
    <li>The manager's “order” means a paid purchase; the code's <code>Order</code> exists from the first item in the basket.</li>
    <li>Developers say “status 3”; nobody in the business knows what that is.</li>
    <li>Rules get lost: a sentence in a meeting never becomes a method anyone can find.</li>
  </ul>""",
    problem_figs=[ul_problem],
    analogy_side="the kitchen's own words",
    analogy="""  <p>A busy <b>restaurant kitchen</b> has its own language: “fire table four”, “eighty-six the salmon”, “on the pass”. Each phrase means <b>one exact thing</b>, everyone uses it, and a new cook learns it in the first week. Orders move fast because nobody translates.</p>
  <ul>
    <li>The phrases are the <b>ubiquitous language</b>.</li>
    <li>They only work <b>inside this kitchen</b>: the bar next door has its own.</li>
    <li>When the menu changes, the words change for <b>everyone at once</b>.</li>
  </ul>""",
    analogy_figs=[ul_analogy],
    map=[("Kitchen phrases", "The glossary of domain terms"),
         ("The chef and the cooks", "Domain experts and developers"),
         ("“86 the salmon”", "A method like <code>product.markSoldOut()</code>"),
         ("Only in this kitchen", "Only inside one bounded context"),
         ("New cook learns the words", "Onboarding reads the glossary and the code")],
    how_side="one glossary, four places",
    how="""  <p>The language is <b>discovered</b>, not invented: listen to how experts describe the work, write the terms down with their meaning, and push back where a word is vague. Then make the code say the same thing.</p>""",
    how_figs=[ul_how],
    steps=[("Listen first", "Sit with the people who do the work. Note the nouns and verbs they use, and the words they argue about."),
           ("Write a glossary", "One line per term: the word, what it means here, and an example. Keep it next to the code."),
           ("Name the code after it", "Classes, methods, events and modules use the glossary words, not technical ones like Manager or Data."),
           ("Use it in tests", "Test names read like business examples: “a paid order can be refunded within 30 days”."),
           ("Challenge vague words", "When “customer” means three things, that's a sign of three models: split them or qualify the word."),
           ("Refactor when the language changes", "A new word in a workshop means a rename in the code. Do it while it's cheap.")],
    vocab=[("Ubiquitous language", "The shared vocabulary of a team and its experts, used everywhere within one context."),
           ("Domain expert", "Someone who knows how the business works: a buyer, a planner, a support lead."),
           ("Glossary", "The written list of terms and their meanings."),
           ("Knowledge crunching", "Evans's name for working through the domain with experts until the model is clear."),
           ("Model", "A simplified view of the business that the code is built on."),
           ("Translation cost", "The effort, and the bugs, of mapping one vocabulary to another.")],
    code=dict(file="order.ts", note="the code says what the business says", src="""
// Glossary: an Order is placed when it is paid. Before that it is a Basket.
class Basket {
  add(item: ProductId, qty: Quantity) { /* ... */ }
  checkOut(payment: PaymentConfirmed): Order {   // a Basket becomes an Order
    return Order.place(this.lines, payment);
  }
}

class Order {
  static place(lines: OrderLine[], payment: PaymentConfirmed): Order { /* ... */ }
  cancel(reason: CancellationReason) { /* ... */ }
  refund(within = days(30)) { /* ... */ }
}

// not: OrderManager.updateStatus(orderId, 3)
"""),
    tools="tools: a glossary file in the repository (<code>docs/glossary.md</code>), Context Mapper or a wiki page per context, event storming boards, and code review that asks “is that the word the business uses?”",
    gains=["<b>Fewer translation bugs</b>: one word, one meaning.",
           "<b>Experts can read</b> test names and even some code.",
           "<b>Rules are easy to find</b>: search for the business word.",
           "<b>Faster onboarding</b>: learn the glossary, then the code."],
    losses=["<b>Time with experts</b>, which is scarce.",
            "<b>Renames</b> when the language changes.",
            "<b>Arguments about words</b>, which feel slow (but find real gaps).",
            "<b>Only works inside one context</b>; it is not a company dictionary."],
    baseline="Each line compares <b>code named in technical terms, with translation in people's heads</b> to <b>code and tests named in the experts' own words</b>.",
    ratings=[(3, 4, "Fewer translations to keep in your head."),
             (2, 5, "The point of the pattern."),
             (3, 4, "Misunderstood rules surface in conversation, not in production."),
             (3, 4, "A new rule is easy to place when names match the business."),
             (3, 4, "Tests read as business examples."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (4, 3, "A glossary to keep up and renames to make."),
             (2, 4, "New people learn one vocabulary, not three.")],
    pitfalls=[("A company-wide dictionary", "One meaning of “customer” is forced on sales, billing and support, and fits none of them.", "keep one language per bounded context; let words differ between contexts."),
              ("Developers invent the words", "The code says <code>FulfilmentEntity</code>; the warehouse says “pick list”.", "use the words the experts already use, and ask when unsure."),
              ("Glossary nobody reads", "A wiki page from 2023 that disagrees with the code.", "keep it in the repository and update it in the same pull request as the rename."),
              ("Technical names win", "<code>Manager</code>, <code>Processor</code>, <code>Data</code> classes hide what really happens.", "name classes and methods after business things and actions.")],
    use=["The business rules are rich, and getting them wrong costs money.",
         "Developers and experts talk often, and misunderstandings keep showing up.",
         "New people take months to understand what the code does."],
    skip=["Simple CRUD or a technical tool where the “domain” is the technology itself.",
          "You have no access to domain experts at all (fix that first)."],
    related=["<b>Bounded Context</b>", "<b>Event Storming</b>", "<b>Core, Supporting &amp; Generic Subdomains</b>", "<b>Domain Discovery</b> (Ana, vol. 1)"],
    quiz=[("Where should the ubiquitous language be used?", "Everywhere inside one context: conversations, documents, class and method names, tests and the user interface."),
          ("Why is one meaning per word so important?", "Every place where a word means two things needs a translation in someone's head, and that's where bugs come from."),
          ("Is the ubiquitous language the same across the whole company?", "No. It holds inside one bounded context. Billing and shipping can use “customer” differently."),
          ("Who decides the words?", "They come from the domain experts, refined together with the developers. Developers shouldn't invent them alone.")],
    quiz_sit=[("In a refinement meeting the warehouse lead keeps saying “pick list”, but the code and tickets say <code>FulfilmentTask</code>. A new developer built the wrong screen because of it. What do you do?",
               "Adopt the experts' word: add “pick list” to the glossary with its meaning, rename the class, the table and the tickets in one change, and ask in review whether new names match the words people really use.")],
    try_it="Take one feature you work on and list the ten nouns and verbs in its code. Next to each, write the word a business person would use. Wherever they differ, ask an expert which is right, add it to a glossary file, and rename one class in the code.",
    then_now=dict(src="Evans, 2003", verdict="core",
                  then="Evans made the shared language the heart of the method: developers and experts “crunch knowledge” together until one model and one vocabulary emerge, used in speech, diagrams and code.",
                  now="Nothing has replaced it. The tools changed: event storming and domain storytelling find the language faster, glossaries live in the repository, and test names in BDD style carry it. The one refinement is that the language belongs to <b>one context</b>, not the company.",
                  take="Still the first thing to get right. It costs little and pays off in every other pattern in this volume."),
    remember="If the code needs a <span class=\"hl\">translation</span>, the bug is already <span class=\"hl\">in the translation</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 2 “Communication and the Use of Language”.",
             "Martin Fowler, “UbiquitousLanguage” (bliki, 2006).",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 2.",
             "Stefan Hofer &amp; Henning Schwentner, <i>Domain Storytelling</i> (2021)."],
)

# ------------------------------------------------------------------ 02 Subdomains
sd_problem = Doodle(760, 260, "Doodle of a team spending its effort in the wrong places. Six months went into building an in-house login system and an invoicing engine, both things every business needs and can buy. The pricing and recommendation logic, which is what makes this shop different, is a tangle of if-statements written in a hurry.",
                    "Months on login and invoicing, which anyone can buy; the pricing logic that makes the shop special was rushed.")
sd_problem.box(20, 40, 210, 80, "own login", "paper", sub="3 months")
sd_problem.box(260, 40, 210, 80, "own invoicing", "paper", sub="3 months")
sd_problem.box(520, 40, 220, 80, "pricing", "pink", stroke="red", sub="2 weeks, rushed")
sd_problem.note(245, 160, "polished, but everyone has these", "pen")
sd_problem.note(630, 160, "the reason customers come", "red")
sd_problem.note(380, 230, "effort went where it made no difference", "red")

sd_analogy = Doodle(760, 250, "Doodle of a famous bakery. It makes its own sourdough with a secret starter, which is why people queue. It buys flour and boxes from suppliers, and uses a standard card terminal and accounting package. It would never bake its own boxes or write its own card terminal.",
                    "A great bakery bakes its own bread, buys its flour, and never builds its own card terminal.")
sd_analogy.box(20, 40, 230, 90, "sourdough", "y", sub="secret starter: core")
sd_analogy.box(270, 40, 220, 90, "flour, boxes", "blue", sub="bought: supporting")
sd_analogy.box(510, 40, 230, 90, "card terminal", "paper", sub="standard: generic")
sd_analogy.note(380, 180, "the queue is for the bread, not the boxes", "green")
sd_analogy.note(380, 220, "care goes where customers notice", "pen")

sd_how = Doodle(760, 320, "A core domain chart for the online shop. The horizontal axis is how much it sets the business apart; the vertical is how complex it is. Pricing and recommendations sit top right: core. Catalogue management and returns sit in the middle: supporting. Login, payments, invoicing and email sit bottom left: generic. Core is built in-house with the best people; supporting is built simply or bought; generic is bought or used as a service.",
                 "Core: build it well. Supporting: build it simply. Generic: buy it.")
sd_how.line("M60 290 H740 M60 290 V20")
sd_how.note(400, 314, "sets us apart →", "pen")
sd_how.note(20, 150, "complex ↑", "pen", anchor="start")
sd_how.box(470, 30, 260, 90, "pricing · recs", "y", sub="CORE: build, best people")
sd_how.box(270, 130, 260, 80, "catalogue · returns", "blue", sub="SUPPORTING: keep simple")
sd_how.box(80, 210, 260, 70, "login · payments", "paper", sub="GENERIC: buy or rent")

SUBDOMAINS = dict(
    slug="subdomains",
    kicker="a.k.a. “bake your own bread, buy your flour”",
    tldr="Split the business into <b>subdomains</b> and sort them: <b>core</b> (what makes you different, so build it carefully with your best people), <b>supporting</b> (needed and specific to you, but not special, so keep it simple) and <b>generic</b> (every business has it, so <b>buy or rent</b> it). Then spend your modelling effort where it <b>makes a difference</b>.",
    chips=[("Family", "strategic design"), ("From", "Evans (2003), ch. 15 “Distillation”"), ("Modern tools", "core domain charts, Wardley maps"), ("Pairs with", "build vs buy, bounded context")],
    problem="""  <p class="lead">Teams naturally polish what is <span class="hl-pink">fun or familiar</span>, not what the business <span class="hl-pink">competes on</span>.</p>
  <ul>
    <li>Months go into a home-made login, invoicing or search engine.</li>
    <li>The rules that make customers choose you are rushed and tangled.</li>
    <li>Every part gets the same “full DDD” treatment, or none does.</li>
  </ul>""",
    problem_figs=[sd_problem],
    analogy_side="the bakery and its suppliers",
    analogy="""  <p>A <b>famous bakery</b> makes its own sourdough from a secret starter: that's why people queue. It <b>buys</b> flour and boxes, and uses a <b>standard</b> card terminal and accounting package. Baking boxes in-house would be effort with no customer benefit.</p>
  <ul>
    <li>The bread is the <b>core</b> domain.</li>
    <li>Flour and boxes are <b>supporting</b>: needed, bought or kept simple.</li>
    <li>The card terminal is <b>generic</b>: everybody has the same one.</li>
  </ul>""",
    analogy_figs=[sd_analogy],
    map=[("Sourdough with a secret starter", "Core subdomain: pricing, matching, scheduling, whatever you compete on"),
         ("Flour and boxes", "Supporting subdomain: catalogue admin, returns handling"),
         ("Card terminal, accounting", "Generic subdomain: login, payments, email, invoicing"),
         ("Best baker on the bread", "Best developers and most modelling effort on the core"),
         ("Bought from a supplier", "SaaS, open source or a simple off-the-shelf module")],
    how_side="sort, then spend effort accordingly",
    how="""  <p>A <b>subdomain</b> is a part of the business (the problem space). A <b>bounded context</b> is a part of the software (the solution space). They often line up one to one, but they don't have to.</p>""",
    how_figs=[sd_how],
    steps=[("List the business capabilities", "What does the company do, in verbs: sell, price, ship, bill, support, recommend."),
           ("Ask “does this set us apart?”", "Would a customer pick us because of it? If yes, it's a candidate for core."),
           ("Ask “could we buy this?”", "If a SaaS or library does it well enough, it's generic."),
           ("Place each on a chart", "Differentiation on one axis, complexity on the other. Talk it through with the business."),
           ("Match effort to the type", "Core: rich model, tests, senior people. Supporting: simple code, maybe CRUD. Generic: buy, integrate behind an adapter."),
           ("Revisit yearly", "Today's core can become generic (search, recommendations) as the market catches up.")],
    vocab=[("Domain", "The whole area of business the software serves."),
           ("Subdomain", "One part of it, such as pricing or shipping."),
           ("Core domain", "The subdomain that gives the business its edge."),
           ("Supporting subdomain", "Specific to the business, needed, but not a differentiator."),
           ("Generic subdomain", "A solved problem every business shares."),
           ("Distillation", "Evans's term for separating the core from everything else.")],
    code=dict(file="subdomains.md", note="a one-page classification, kept in the repo", plain=True, src="""
# Subdomains · online shop · reviewed 2026-11

| Subdomain        | Type        | Why                                     | Approach                   |
|------------------|-------------|-----------------------------------------|----------------------------|
| Pricing          | core        | dynamic bundles win customers           | rich model, senior team    |
| Recommendations  | core        | drives 30% of basket value              | in-house, experiments      |
| Catalogue admin  | supporting  | specific to us, not a differentiator    | simple CRUD app            |
| Returns          | supporting  | our rules, low complexity               | transaction scripts        |
| Payments         | generic     | everyone needs it, regulated            | Stripe behind an adapter   |
| Login            | generic     | solved problem                          | identity provider (OIDC)   |
| Invoicing, email | generic     | solved problems                         | SaaS                       |
"""),
    tools="tools: the core domain chart and bounded context canvas from the DDD Crew (GitHub, free), Wardley maps for how capabilities evolve, and a build-vs-buy decision record for each generic subdomain.",
    gains=["<b>Effort goes where it matters</b> to customers.",
           "<b>Less code to own</b>: generic parts are bought.",
           "<b>Clear reason</b> for where to use rich modelling and where not.",
           "<b>A shared picture</b> with the business of what really counts."],
    losses=["<b>Hard conversations</b>: someone's favourite system is “generic”.",
            "<b>Vendor dependence</b> for generic parts.",
            "<b>The sort changes</b> over time, and needs revisiting.",
            "<b>Not every company agrees</b> on what its core is."],
    baseline="Each line compares <b>one approach for every part of the system</b> to <b>effort matched to core, supporting and generic subdomains</b>.",
    ratings=[(3, 4, "Supporting and generic parts stay simple or are bought."),
             (3, 4, "The core gets the care that makes its language clear."),
             (3, 4, "The best people guard the rules that matter most."),
             (3, 4, "Less code overall; the core is easier to change."),
             (3, 3, "Neutral."),
             (3, 4, "Generic parts sit behind adapters, so they can be swapped."),
             (3, 3, "Neutral."),
             (2, 4, "No heavy modelling where CRUD will do."),
             (3, 4, "Teams can own subdomains with clear expectations.")],
    pitfalls=[("Everything is core", "Every team claims its area is strategic, so nothing is prioritised.", "ask “would a customer choose us for this?” and accept a short core list."),
              ("Building generic things", "A custom identity system or CMS eats a year.", "buy or use open source; build only the glue."),
              ("Full DDD everywhere", "Aggregates and events for a settings page.", "use rich models in the core; plain CRUD is fine elsewhere."),
              ("A one-time exercise", "The chart from three years ago still says search is core.", "revisit at least yearly, and when the strategy changes.")],
    use=["Planning where to put your strongest people and most care.",
         "Deciding build vs buy for a new capability.",
         "Before splitting a system into contexts or services."],
    skip=["A tiny product where everything is the core and the team is three people.",
          "Prototypes whose business model isn't known yet (learn first)."],
    related=["<b>Bounded Context</b>", "<b>Ubiquitous Language</b>", "<b>Anemic Domain Model</b>", "<b>Build vs Buy vs Open Source</b> (Ana, vol. 2)", "<b>Capability Map</b> (Ana, vol. 4)"],
    quiz=[("What are the three kinds of subdomain?", "Core (sets you apart), supporting (specific to you but not special) and generic (solved problems every business has)."),
          ("Where should a team use its richest modelling?", "In the core domain."),
          ("What's the usual approach for a generic subdomain?", "Buy it, rent it as a service or use open source, behind an adapter."),
          ("What's the difference between a subdomain and a bounded context?", "A subdomain is part of the business problem; a bounded context is part of the software solution. They often, but not always, line up.")],
    quiz_sit=[("Your team wants to build its own feature-flag service and search engine “to keep control”. Meanwhile the delivery-slot pricing, which the CEO says wins customers, has no tests. What do you propose?",
               "Classify the subdomains with the business. Search and feature flags are generic: use a product or open source behind an adapter. Delivery-slot pricing is core: move the strongest developers there and give it a proper model and tests.")],
    try_it="List eight to ten capabilities of a product you know. For each, answer two questions with someone from the business: “would a customer choose us for this?” and “could we buy it?”. Place them on a two-axis chart and write one line on how much effort each deserves.",
    then_now=dict(src="Evans, 2003", verdict="grown",
                  then="Evans put “distillation” near the end of the book, in part IV, so many readers never reached it. He described the core domain, generic subdomains and a “domain vision statement” to keep the team focused.",
                  now="Today it's usually the <b>first</b> thing taught. With SaaS and open source for almost every generic capability, “buy the generic, build the core” is a daily decision. Core domain charts, Wardley maps and team topologies use the same idea.",
                  take="More useful now than in 2003, because there is so much more you can buy instead of build."),
    remember="Bake your own <span class=\"hl\">bread</span>; buy your <span class=\"hl\">flour</span>; never build your own <span class=\"hl\">card terminal</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 15 “Distillation”.",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 1.",
             "DDD Crew, “Core Domain Charts” (github.com/ddd-crew).",
             "Simon Wardley, <i>Wardley Maps</i> (online book, 2016–)."],
)

# ------------------------------------------------------------------ 03 Bounded Context
bc_problem = Doodle(760, 300, "Doodle of one giant Product class that every team edits. Catalogue needs title, photos and description. Pricing needs cost and margin. Shipping needs weight and size. Billing needs tax code. The class has eighty fields; every change by one team risks breaking another's; meetings argue about what a product really is.",
                    "One Product for everyone: eighty fields, five teams, and every change breaks someone.")
bc_problem.box(250, 70, 260, 130, "Product", "pink", stroke="red", sub="80 fields")
for (x, y, t) in [(20, 30, "catalogue"), (560, 30, "pricing"), (20, 200, "shipping"), (560, 200, "billing")]:
    bc_problem.box(x, y, 180, 56, t, "paper", size=18)
for (x1, y1, x2, y2) in [(204, 58, 250, 100), (556, 58, 510, 100), (204, 228, 250, 180), (556, 228, 510, 180)]:
    bc_problem.arrow(x1, y1, x2, y2, color="red")
bc_problem.note(380, 286, "“what IS a product?” · every change breaks someone", "red")

bc_analogy = Doodle(760, 250, "Doodle of the word table in different rooms. In the dining room a table has four legs and seats six. In the spreadsheet office a table has rows and columns. In parliament, to table a motion means to propose it in Britain and to postpone it in America. The word is fine as long as you know which room you're in.",
                    "“Table” means different things in different rooms. Each room is fine on its own.")
bc_analogy.box(20, 40, 220, 100, "dining room", "y", sub="four legs, seats six")
bc_analogy.box(270, 40, 220, 100, "office", "blue", sub="rows and columns")
bc_analogy.box(520, 40, 220, 100, "parliament", "paper", sub="“table a motion”")
bc_analogy.note(380, 190, "same word, different meaning per room", "pen")
bc_analogy.note(380, 226, "trouble only starts when rooms are merged", "red")

bc_how = Doodle(760, 320, "Three bounded contexts for the online shop. In Catalogue, a Product has title, photos and description. In Pricing, a Product is a SKU with cost, price and margin rules. In Shipping, a Parcel item has weight and dimensions. They share only the product ID. Each context has its own model, code, database schema and team, and they communicate through events or APIs that translate between models.",
                 "Each context has its own small model. They share an ID and talk through translated messages.")
for i, (name, sub, fill) in enumerate([("Catalogue", "Product: title, photos", "y"), ("Pricing", "SKU: cost, price, margin", "blue"), ("Shipping", "Item: weight, size", "green")]):
    x = 20 + i * 250
    bc_how.box(x, 30, 220, 170, None, fill, dash=True)
    bc_how.head(x + 110, 64, name)
    bc_how.text(x + 110, 104, sub)
    bc_how.text(x + 110, 140, "own code & schema")
    bc_how.text(x + 110, 176, "own team")
bc_how.arrow(244, 115, 266, 115, both=True)
bc_how.arrow(494, 115, 516, 115, both=True)
bc_how.note(380, 244, "they share only the product ID", "pen")
bc_how.note(380, 284, "messages are translated at each border", "green")

BOUNDED_CONTEXT = dict(
    slug="bounded-context",
    kicker="a.k.a. “same word, different room”",
    tldr="Don't build one model for the whole company. Draw <b>borders</b>, and inside each border keep <b>one model with one language</b>, where every word means exactly one thing. <b>Catalogue's</b> product and <b>Shipping's</b> product can be different classes with different fields; they share an <b>ID</b> and talk through <b>translated messages</b>. A bounded context is also a natural unit for a <b>team, a module or a service</b>.",
    chips=[("Family", "strategic design"), ("From", "Evans (2003), ch. 14"), ("Becomes", "a module, a service, a team's area"), ("Pairs with", "context map, anti-corruption layer")],
    problem="""  <p class="lead">One model for everybody grows until it means <span class="hl-pink">nothing precise to anybody</span>.</p>
  <ul>
    <li>A <code>Product</code> class with eighty fields, half of them null for any given use.</li>
    <li>Every team edits it; every change risks breaking someone else.</li>
    <li>Meetings argue about what “product” or “customer” really means.</li>
  </ul>""",
    problem_figs=[bc_problem],
    analogy_side="the word “table” in different rooms",
    analogy="""  <p>“Table” means a piece of furniture in the <b>dining room</b>, a grid in the <b>office</b>, and a proposal in <b>parliament</b>. Nobody is confused, because everyone knows <b>which room</b> they're in. Trouble only starts if you insist the word must mean the same thing everywhere.</p>
  <ul>
    <li>Each room is a <b>bounded context</b>.</li>
    <li>The word is part of each room's <b>language</b>.</li>
    <li>Walking between rooms means <b>translating</b>.</li>
  </ul>""",
    analogy_figs=[bc_analogy],
    map=[("A room", "A bounded context"),
         ("“Table” in that room", "A term in that context's ubiquitous language"),
         ("The furniture vs the grid", "Catalogue's <code>Product</code> vs Pricing's <code>Sku</code>"),
         ("Walking to another room", "Sending a message across a context border, translated"),
         ("Who uses each room", "The team that owns the context")],
    how_side="borders around models",
    how="""  <p>Look for borders where <b>language changes</b>, where <b>different experts</b> are in charge, or where data changes for <b>different reasons</b>. A context is a <b>language border first</b>: it can be a module in a monolith long before it is a service.</p>""",
    how_figs=[bc_how],
    steps=[("Find where words change meaning", "“Customer” in sales has leads and deals; in billing it has invoices and a tax ID. That's a border."),
           ("Name each context", "Catalogue, Pricing, Ordering, Shipping, Billing. Write one sentence on what each is responsible for."),
           ("Give each its own model", "Its own classes, schema (or tables) and language. Duplication of a few fields across contexts is fine."),
           ("Share IDs, not objects", "Contexts refer to each other's things by ID and never reach into another's tables."),
           ("Connect through contracts", "Events or APIs at the border, translated into each side's language."),
           ("Align teams", "One team per context where you can, so the model and its owners change together.")],
    vocab=[("Bounded context", "A border inside which one model and one language apply consistently."),
           ("Model", "The classes and rules that represent the business inside the context."),
           ("Context border", "Where translation happens between two models."),
           ("Big ball of mud", "A system with no clear borders, where everything depends on everything."),
           ("Modular monolith", "One deployable app split into modules along context borders."),
           ("Conway's law", "Systems tend to mirror the communication structure of the teams that build them.")],
    code=dict(file="two-products.ts", note="same thing, two models, one shared ID", src="""
// catalogue/product.ts : what shoppers see
export class Product {
  constructor(readonly id: ProductId, public title: string,
              public photos: PhotoUrl[], public description: Markdown) {}
}

// shipping/item.ts : what the warehouse needs
export class ShippableItem {
  constructor(readonly productId: ProductId,     // the only shared thing
              readonly weight: Grams, readonly size: Dimensions,
              readonly fragile: boolean) {}
}

// shipping listens to catalogue events and keeps only what it needs
on("catalogue.ProductPublished", (e) =>
  shippingItems.upsert(e.productId, { weight: e.weightGrams, size: e.dimensions }));
"""),
    tools="tools: modules or packages per context with an architecture test that forbids reaching across (ArchUnit, dependency-cruiser, Nx module boundaries), the bounded context canvas from the DDD Crew, and Context Mapper for drawing them.",
    gains=["<b>Precise models</b>: each word means one thing.",
           "<b>Teams change their model alone</b>.",
           "<b>Natural seams</b> for modules, services and teams.",
           "<b>Smaller classes</b> with only the fields each use needs."],
    losses=["<b>Some duplication</b> of fields and data.",
            "<b>Translation work</b> at every border.",
            "<b>Eventual consistency</b> between contexts.",
            "<b>Wrong borders are expensive</b> to move later."],
    baseline="Each line compares <b>one shared model for the whole system</b> to <b>separate models inside bounded contexts</b>.",
    ratings=[(2, 4, "Each model is small and has one meaning."),
             (2, 5, "Words are precise inside each border."),
             (3, 4, "Rules live with the model they belong to."),
             (2, 4, "A change stays inside one context."),
             (3, 4, "A context can be tested on its own."),
             (1, 4, "The main gain: contexts depend on contracts, not internals."),
             (4, 3, "Some copying and messaging between contexts."),
             (4, 3, "Translations and contracts to maintain."),
             (2, 5, "One team per context, working in parallel.")],
    pitfalls=[("One context per entity", "Separate “contexts” for Customer, Order and Product, chatting constantly.", "split by language and business capability, not by noun."),
              ("Shared database tables", "Two contexts read and write the same table, so they're really one.", "each context owns its tables; others ask through an API or event."),
              ("Services before borders", "Microservices are cut first, and the models stay tangled across them.", "find contexts first; start as modules in one app and split later if needed."),
              ("Borders that never move", "The business changed, but the contexts from year one stay.", "revisit borders when language or teams change; moving a module is cheaper than moving a service.")],
    use=["A system larger than one team can keep in its head.",
         "The same word means different things to different departments.",
         "Before deciding on modules, services or team ownership."],
    skip=["A small app with one team and one consistent language (it's already one context).",
          "Very early, before you understand where the language changes."],
    related=["<b>Ubiquitous Language</b>", "<b>Context Map</b>", "<b>Anti-Corruption Layer</b>", "<b>Bounded Contexts</b> (Ana, vol. 1)", "<b>Modular Monolith First</b> (Ana, vol. 1)"],
    quiz=[("What is a bounded context?", "A border inside which one model and one language apply consistently, so every term has one meaning."),
          ("Can two contexts have different classes for the same real-world thing?", "Yes, and they usually should: each keeps only what it needs, and they share an ID."),
          ("Is a bounded context the same as a microservice?", "No. It's a language and model border. It can be a module in a monolith, one service, or occasionally several."),
          ("Name two signs of a border.", "A word changes meaning; different experts are in charge; data changes for different reasons; different teams own it.")],
    quiz_sit=[("Shipping and Catalogue both write to the <code>products</code> table. A Catalogue migration renames <code>weight</code> to <code>weight_kg</code> and the warehouse labels break overnight. What do you change?",
               "Give each context its own data. Shipping keeps its own item table with weight and size, filled from a catalogue event or API, and nobody outside Catalogue touches Catalogue's tables. Add an architecture test that forbids cross-context table access.")],
    try_it="Pick one overloaded word in your system (customer, product, account). Write down what it means to three different departments and which fields each uses. Sketch three small classes, one per context, and the one ID they share.",
    then_now=dict(src="Evans, 2003", verdict="grown",
                  then="Evans introduced the bounded context in part IV, as a way to keep large models consistent: an explicit border, a model inside it, and a context map between them. Many teams at the time read the book for its object patterns and skipped it.",
                  now="Since about 2014 it's the most quoted idea in DDD, because microservices needed a way to draw service borders, and team topologies a way to draw team borders. The modern advice: find contexts first, start them as modules, and only split into services when you need to.",
                  take="Matters more today than when it was written. If you take one thing from this volume, take this."),
    remember="Every word is fine <span class=\"hl\">in its own room</span>. Trouble starts when you <span class=\"hl\">knock down the walls</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 14 “Maintaining Model Integrity”.",
             "Martin Fowler, “BoundedContext” (bliki, 2014).",
             "Matthew Skelton &amp; Manuel Pais, <i>Team Topologies</i> (2019).",
             "DDD Crew, “Bounded Context Canvas” (github.com/ddd-crew)."],
)

# ------------------------------------------------------------------ 04 Event Storming
es_problem = Doodle(760, 260, "Doodle of requirements gathered one department at a time. Analysts interview sales, then the warehouse, then finance, separately, and write a ninety-page document. Nobody sees the whole process. Developers discover in testing that a refund needs the warehouse to confirm the return first, which nobody had mentioned.",
                    "Interviews one department at a time: nobody sees the whole flow, and the gaps show up in testing.")
es_problem.box(20, 40, 160, 60, "sales", "paper", size=18)
es_problem.box(20, 110, 160, 60, "warehouse", "paper", size=18)
es_problem.box(20, 180, 160, 60, "finance", "paper", size=18)
for y in (70, 140, 210):
    es_problem.arrow(184, y, 300, 140)
es_problem.box(310, 100, 180, 80, "90-page doc", "y", sub="nobody reads it")
es_problem.arrow(494, 140, 540, 140, color="red")
es_problem.box(550, 100, 190, 80, "found in test", "pink", stroke="red", sub="refund needs return!")

es_analogy = Doodle(760, 250, "Doodle of a family planning a wedding on a wall of sticky notes. Everyone writes what has to happen, in the order it happens: venue booked, invitations sent, replies received, seating plan drawn. Aunt Maria spots that the seating plan can't happen before replies come back. Disagreements appear on the wall, not on the day.",
                     "Planning a wedding on a wall of sticky notes: everyone at once, in time order, gaps visible.")
for i, t in enumerate(["venue booked", "invites sent", "replies in", "seating drawn"]):
    es_analogy.box(30 + i * 180, 50, 150, 70, t, "y", size=16)
for i in range(3):
    es_analogy.arrow(184 + i * 180, 85, 206 + i * 180, 85)
es_analogy.note(380, 170, "“seating can't be before replies!”", "red")
es_analogy.note(380, 214, "everyone in the room, one wall, in time order", "pen")

es_how = Doodle(760, 330, "An event storming wall. Orange notes are domain events in the past tense along a timeline: Basket Checked Out, Payment Taken, Order Placed, Order Packed, Parcel Shipped. Blue notes are commands that cause them, yellow notes are the actors, lilac notes are policies like when payment is taken then reserve stock, and pink notes mark hot spots, questions and disagreements. Vertical lines show where the language changes: candidate bounded contexts.",
                 "Orange events in time order, blue commands, yellow actors, lilac policies, pink hot spots, then borders.", exact=True)
evs = ["Checked Out", "Payment Taken", "Order Placed", "Packed", "Shipped"]
for i, t in enumerate(evs):
    es_how.box(14 + i * 150, 120, 130, 64, t, "y", size=15)
es_how.box(14, 30, 130, 56, "Check Out", "blue", size=15)
es_how.box(164, 30, 130, 56, "shopper", "paper", size=15)
es_how.box(314, 210, 130, 60, "policy", "green", sub="then reserve stock", subsize=13, size=15)
es_how.box(614, 210, 130, 60, "hot spot!", "pink", stroke="red", sub="split parcels?", subsize=13, size=15)
es_how.line("M447 20 V300", dash=True)
es_how.note(600, 28, "ordering | shipping", "pen")
es_how.note(240, 300, "dashed line: the language changes here", "pen")

EVENT_STORMING = dict(
    slug="event-storming",
    kicker="a.k.a. “the wall of orange sticky notes”",
    tldr="Put the people who <b>know the process</b> and the people who <b>build it</b> in one room with a very long wall. Everyone writes <b>domain events</b> on orange notes, in the past tense (“Order Placed”), and sticks them on a <b>timeline</b>. Then add the <b>commands</b>, <b>actors</b>, <b>policies</b> and <b>hot spots</b>. In a few hours you see the whole flow, the gaps, the arguments and the likely <b>context borders</b>.",
    chips=[("Family", "discovery workshop"), ("Invented by", "Alberto Brandolini (2013)"), ("Takes", "2–4 hours to a few days"), ("Finds", "events, language, borders, hot spots")],
    problem="""  <p class="lead">Interviews one department at a time produce long documents, and <span class="hl-pink">nobody sees the whole process</span> until it is built.</p>
  <ul>
    <li>Each department describes only its own step.</li>
    <li>The rules between steps (“refund only after the return is checked”) fall through the gaps.</li>
    <li>Disagreements between departments surface in testing or in production.</li>
  </ul>""",
    problem_figs=[es_problem],
    analogy_side="planning a wedding on the wall",
    analogy="""  <p>A family plans a <b>wedding</b> with sticky notes on a wall: “venue booked”, “invitations sent”, “replies received”, “seating plan drawn”, in the order they happen. Aunt Maria immediately sees the seating plan can't come before the replies. The argument happens <b>on the wall, months early</b>, not on the day.</p>
  <ul>
    <li>Each note is a <b>domain event</b>, in the past tense.</li>
    <li>The wall is the <b>timeline</b>.</li>
    <li>Aunt Maria's objection is a <b>hot spot</b>.</li>
  </ul>""",
    analogy_figs=[es_analogy],
    map=[("A note: “invitations sent”", "A domain event: <code>OrderPlaced</code>"),
         ("The wall in time order", "The end-to-end business timeline"),
         ("“Who sends them?”", "Actors (yellow) and commands (blue)"),
         ("“When replies are in, draw seats”", "A policy (lilac): when this happens, do that"),
         ("Aunt Maria's objection", "A hot spot (pink): a question or conflict to resolve")],
    how_side="a timeline of the business, in orange",
    how="""  <p>There are three common formats. <b>Big picture</b>: the whole business, many departments, to find borders and problems. <b>Process level</b>: one process in detail, with commands, policies and read models. <b>Design level</b>: down to aggregates and the code. Start big, then zoom in.</p>""",
    how_figs=[es_how],
    steps=[("Invite the right people", "Domain experts from each step, developers, a product owner, and one facilitator. Eight to fifteen people."),
           ("Chaotic exploration", "Everyone writes orange events in the past tense and sticks them roughly in time order. No discussion yet."),
           ("Enforce the timeline", "Sort the notes together, remove duplicates, and argue about order. The arguments are the gold."),
           ("Mark hot spots", "Every question, conflict or “it depends” becomes a pink note. Don't solve them yet."),
           ("Add commands, actors and policies", "What triggers each event, who does it, and which automatic rules connect events."),
           ("Draw the borders", "Where the language or the experts change, draw a line: candidate bounded contexts. Photograph everything.")],
    vocab=[("Domain event", "Something that happened that the business cares about, in the past tense (orange)."),
           ("Command", "A request to do something, which may cause an event (blue)."),
           ("Actor", "The person or role that issues a command (small yellow)."),
           ("Policy", "An automatic reaction: “whenever X, then Y” (lilac)."),
           ("Hot spot", "A question, risk or disagreement (pink, at an angle)."),
           ("Read model", "The information someone needs to decide (green).")],
    code=dict(file="storm-to-code.ts", note="the wall's names become the code's names", src="""
// From the wall: [shopper] -> Check Out -> Basket Checked Out
//                policy: when Payment Taken, then Reserve Stock -> Stock Reserved
type BasketCheckedOut = { type: "BasketCheckedOut"; basketId: BasketId; total: Money };
type PaymentTaken     = { type: "PaymentTaken";     orderId: OrderId; amount: Money };
type StockReserved    = { type: "StockReserved";    orderId: OrderId; lines: Line[] };

// the lilac note, as code
on<PaymentTaken>("PaymentTaken", async (e) => {
  await commands.send({ type: "ReserveStock", orderId: e.orderId });
});
"""),
    tools="tools: a long roll of paper, orange, blue, yellow, lilac and pink sticky notes, and markers in person; Miro, Mural or FigJam templates remotely; Brandolini's book and the DDD Crew's EventStorming glossary for the colours.",
    gains=["<b>The whole process</b> visible in one afternoon.",
           "<b>Gaps and conflicts</b> found before code exists.",
           "<b>Shared language</b> emerges from the notes.",
           "<b>Candidate borders</b> for contexts and teams."],
    losses=["<b>Getting the right people</b> in one room is hard.",
            "<b>Needs a good facilitator</b>, or it turns into a meeting.",
            "<b>The wall isn't documentation</b>; someone must write it up.",
            "<b>Remote sessions</b> are harder to keep lively."],
    baseline="Each line compares <b>requirements gathered by separate interviews and documents</b> to <b>a shared event storming session with experts and developers</b>.",
    ratings=[(3, 4, "One timeline everyone can read."),
             (2, 5, "The language comes straight from the experts."),
             (2, 4, "Missing rules and edge cases show up as hot spots early."),
             (3, 4, "The flow is understood, so changes are easier to place."),
             (3, 4, "Events and policies map straight to test cases."),
             (3, 4, "Borders come from the business, not guesses."),
             (3, 3, "Neutral."),
             (3, 2, "A workshop to prepare, run and write up."),
             (2, 4, "Teams can be aligned to the borders found.")],
    pitfalls=[("Only developers in the room", "The wall shows what developers think the business does.", "no domain experts, no session; reschedule rather than guess."),
              ("Events in the wrong tense", "Notes say “create order” or “order screen”.", "past tense, business words: “Order Placed”."),
              ("Solving hot spots on the spot", "Two hours lost on one pink note.", "mark it, move on, and pick the top hot spots at the end."),
              ("The wall dies", "Photos sit in a chat thread nobody opens.", "turn it into a glossary, a context map and the first event names in code within a week.")],
    use=["Starting a new product or a major rewrite.",
         "Before drawing bounded contexts or service borders.",
         "A process that crosses several departments and keeps breaking."],
    skip=["A small, well-understood feature inside one team.",
          "When the experts can't attend (use interviews and domain storytelling instead)."],
    related=["<b>Ubiquitous Language</b>", "<b>Bounded Context</b>", "<b>Domain Events</b>", "<b>Domain Discovery</b> (Ana, vol. 1)"],
    quiz=[("What colour and tense are domain events in event storming?", "Orange, in the past tense: “Payment Taken”."),
          ("What is a hot spot?", "A pink note marking a question, conflict or risk that needs an answer later."),
          ("What is a policy?", "An automatic rule connecting events to commands: “whenever payment is taken, reserve stock”."),
          ("How does event storming help find bounded contexts?", "Where the language or the experts change along the timeline, there is probably a border.")],
    quiz_sit=[("Your team wants to run event storming for a new returns process, but the warehouse and finance leads “don't have time”. Developers suggest doing it without them. What do you do?",
               "Don't storm without experts: the result would be developers' guesses. Shorten it to a focused two-hour process-level session, book it with the warehouse and finance leads' managers, and prepare the room so their time is used well.")],
    try_it="Run a one-hour mini event storm on a process you know (ordering food, onboarding a colleague). Write every event in the past tense on its own note, put them in time order, mark three hot spots, and draw one line where the language changes.",
    then_now=dict(src="Brandolini, 2013 (not in Evans)", verdict="grown",
                  then="The 2003 book had no workshop format. Evans described “knowledge crunching”: developers and experts talking, sketching and refining a model over weeks, often with UML diagrams.",
                  now="Event storming (2013) and domain storytelling (2021) are now the standard ways to start. They put events, not classes, at the centre, which also suits event-driven systems. Remote boards made them possible for distributed teams.",
                  take="A newer tool for an old goal. It made DDD's first step faster and much more inclusive."),
    remember="Orange notes, past tense, <span class=\"hl\">one long wall</span>: the arguments you have there are the bugs you <span class=\"hl\">won't ship</span>.",
    sources=["Alberto Brandolini, <i>Introducing EventStorming</i> (Leanpub, 2013–).",
             "DDD Crew, “EventStorming Glossary &amp; Cheat Sheet” (github.com/ddd-crew).",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 12.",
             "Stefan Hofer &amp; Henning Schwentner, <i>Domain Storytelling</i> (2021)."],
)

NOTES = [UBIQUITOUS, SUBDOMAINS, BOUNDED_CONTEXT, EVENT_STORMING]
