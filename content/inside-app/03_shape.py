# Vol. 8 · Inside the Application · Shaping the app: Transaction Script vs Domain Model, Ports & Adapters,
# Vertical Slices, Functional Core / Imperative Shell.

# ------------------------------------------------------------------ 11 Transaction Script vs Domain Model
ts_problem = Doodle(760, 260, "Doodle of two mismatches. On the left, a returns process started as a twenty-line script and grew over three years into a two-thousand-line procedure with nested if-statements for every special case. On the right, a newsletter sign-up form was built with aggregates, domain events and a repository for two fields.",
                    "A script that grew to 2,000 lines of ifs, and a two-field form built with aggregates and events.")
ts_problem.box(20, 30, 340, 160, None, "pink", stroke="red")
ts_problem.head(190, 62, "processReturn()")
ts_problem.text(190, 100, "if … if … else if …")
ts_problem.text(190, 134, "2,000 lines, 3 years")
ts_problem.box(400, 30, 340, 160, None, "pink", stroke="red")
ts_problem.head(570, 62, "newsletter sign-up")
ts_problem.text(570, 100, "aggregate · events · repo")
ts_problem.text(570, 134, "for two fields")
ts_problem.note(380, 236, "the wrong shape for the job, both ways", "red")

ts_analogy = Doodle(760, 250, "Doodle of a recipe card and a trained chef. For a simple dish, a recipe card with numbered steps is perfect: anyone can follow it. For a restaurant with a changing menu, allergies and substitutions, you need a chef who understands ingredients and rules, not a card with a thousand exceptions written in the margin.",
                     "A recipe card for a simple dish; a trained chef for a kitchen full of rules and exceptions.")
ts_analogy.box(20, 40, 340, 120, None, "y")
ts_analogy.head(190, 74, "recipe card")
ts_analogy.text(190, 112, "steps 1, 2, 3: done")
ts_analogy.box(400, 40, 340, 120, None, "green")
ts_analogy.head(570, 74, "trained chef")
ts_analogy.text(570, 112, "knows the rules, adapts")
ts_analogy.note(190, 200, "transaction script", "pen")
ts_analogy.note(570, 200, "domain model", "pen")

ts_how = Doodle(760, 320, "The two styles and when to move. A transaction script is one procedure per use case: validate, load, compute, save, in order. A domain model puts rules on objects that collaborate. The signals to move from script to model: the same rules repeated across scripts, long conditionals about state, and bugs from rules forgotten in one script. Different areas of one app can use different styles.",
                 "Script: one procedure per use case. Model: rules on objects. Move when rules repeat and branch.")
ts_how.box(20, 20, 300, 150, None, "y")
ts_how.head(170, 52, "transaction script")
ts_how.text(170, 90, "validate → load")
ts_how.text(170, 124, "→ compute → save")
ts_how.box(440, 20, 300, 150, None, "green")
ts_how.head(590, 52, "domain model")
ts_how.text(590, 90, "order.cancel()")
ts_how.text(590, 124, "rules on objects")
ts_how.arrow(324, 95, 436, 95, label="move when…", lx=380, ly=84)
ts_how.note(380, 210, "the same rule appears in 3 scripts", "pen")
ts_how.note(380, 245, "long if/else about state", "pen")
ts_how.note(380, 280, "bugs from a rule forgotten in one place", "pen")

TRANSACTION_SCRIPT = dict(
    slug="transaction-script",
    kicker="a.k.a. “recipe card or trained chef?”",
    tldr="Two ways to organise business logic. A <b>transaction script</b> is one procedure per use case: validate, load, compute, save, top to bottom. Simple, obvious, ideal when rules are <b>few</b>. A <b>domain model</b> puts rules on <b>objects</b> that collaborate (entities, value objects, aggregates). More setup, but it stays sane when rules are <b>many and shared</b>. Choose <b>per area</b>, and move from script to model when rules start <b>repeating and branching</b>.",
    chips=[("Family", "domain logic pattern"), ("From", "Fowler, PoEAA (2002)"), ("Also there", "Table Module (now retired)"), ("Pairs with", "subdomains and anemic model (Vol. 7)")],
    problem="""  <p class="lead">Picking one style for the whole app means it's <span class="hl-pink">too heavy</span> in some places and <span class="hl-pink">too weak</span> in others.</p>
  <ul>
    <li>A returns script grew to 2,000 lines of nested ifs.</li>
    <li>A two-field sign-up form got aggregates and domain events.</li>
    <li>Rules copied between scripts drift apart.</li>
  </ul>""",
    problem_figs=[ts_problem],
    analogy_side="the recipe card and the chef",
    analogy="""  <p>For a simple dish, a <b>recipe card</b> with numbered steps is perfect: anyone can follow it. For a restaurant with a changing menu, allergies and substitutions, a card with a thousand margin notes fails; you need a <b>trained chef</b> who understands the ingredients and the rules.</p>
  <ul>
    <li>The card is a <b>transaction script</b>.</li>
    <li>The chef is a <b>domain model</b>.</li>
  </ul>""",
    analogy_figs=[ts_analogy],
    map=[("Recipe card, numbered steps", "One procedure per use case"),
         ("Anyone can follow it", "Easy to read, no abstractions"),
         ("Margin notes for every exception", "Nested ifs as rules grow"),
         ("A chef who knows the rules", "Objects that hold and enforce the rules"),
         ("Cards for snacks, chef for dinner", "Scripts for simple areas, a model for the core")],
    how_side="choose per area, move when it hurts",
    how="""  <p>Fowler's third option, <b>Table Module</b> (one class per table working on record sets), suited .NET DataSets in 2002 and is rarely used now. The real choice today is script or model, often both in one app, decided by the <b>subdomain</b> (Vol. 7).</p>""",
    how_figs=[ts_how],
    steps=[("Start simple", "A new area with few rules: a script per use case is fine."),
           ("Watch for repetition", "The same rule copied into several scripts is the first signal."),
           ("Watch for state branching", "<code>if (status === …)</code> chains about what's allowed when."),
           ("Extract rules onto objects", "Move the repeated rule to an entity or value object method."),
           ("Grow the model gradually", "One rule at a time, with tests, not a big rewrite."),
           ("Keep scripts where they fit", "Reports, admin screens and imports can stay as scripts.")],
    vocab=[("Transaction script", "A procedure that handles one request from start to finish."),
           ("Domain model", "Objects that hold both data and the business rules."),
           ("Table module", "One class per table handling all its rows; mostly retired."),
           ("Use case", "One thing a user or system wants to do."),
           ("Shotgun surgery", "One change requiring edits in many places: a sign of copied rules."),
           ("Refactor to a model", "Gradually moving rules from scripts onto objects.")],
    code=dict(file="returns.ts", note="a script, and the rule that outgrew it", src="""
// transaction script: clear and fine while rules are few
export async function requestReturn(orderId: OrderId, lineId: LineId) {
  const order = await db.orders.find(orderId);
  if (!order) throw new NotFound();
  if (daysSince(order.deliveredAt) > 30) throw new Error("Return window closed");
  await db.returns.insert({ orderId, lineId, status: "requested" });
}

// the 30-day rule now appears in returns, refunds and exchanges -> move it onto the model
export class Order {
  canBeReturned(now: Date) { return this.deliveredAt && daysBetween(this.deliveredAt, now) <= 30; }
}
"""),
    tools="tools: none special: plain functions for scripts; for models, the building blocks in Vol. 7. Refactoring tools and characterization tests help when moving a script to a model.",
    gains=["<b>Scripts</b>: fastest to write and read for simple logic.",
           "<b>Models</b>: rules in one place as complexity grows.",
           "<b>Choosing per area</b> avoids both failure modes.",
           "<b>Gradual move</b> from one to the other."],
    losses=["<b>Scripts</b> rot into duplication when rules grow.",
            "<b>Models</b> cost design time and more code.",
            "<b>Two styles</b> in one app to explain.",
            "<b>Knowing when</b> to switch takes judgement."],
    baseline="Each line compares <b>one logic style for the whole app</b> to <b>scripts for simple areas and a domain model where rules are rich</b>.",
    ratings=[(3, 4, "Each area uses the lightest style that works."),
             (3, 4, "The rich areas speak the business's language on objects."),
             (2, 4, "Shared rules live in one place."),
             (2, 4, "Rules change once, not in every script."),
             (3, 4, "Model rules tested alone; scripts tested end to end."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "No ceremony where it isn't needed."),
             (3, 3, "Neutral.")],
    pitfalls=[("One style everywhere", "A rich model for CSV exports, or scripts for the pricing engine.", "decide per area by how complex the rules are."),
              ("Scripts that never move", "Rules copied into the fifth script.", "extract on the second or third copy."),
              ("Big-bang rewrite", "“Let's rebuild returns as a domain model” for six months.", "move one rule at a time behind tests."),
              ("Scripts calling scripts", "Procedures chained into a hidden workflow.", "name the workflow, or move rules onto objects.")],
    use=["Deciding how to structure logic for a new area.",
         "A procedure that keeps growing branches.",
         "Reviewing whether an area is over- or under-engineered."],
    skip=["Pure data pipelines and reports (scripts or SQL).",
          "Debating style for an area that hasn't caused problems."],
    related=["<b>Active Record vs Data Mapper</b>", "<b>Functional Core, Imperative Shell</b>", "<b>Anemic Domain Model</b> (Vol. 7)", "<b>Core, Supporting &amp; Generic Subdomains</b> (Vol. 7)"],
    quiz=[("What is a transaction script?", "A single procedure that handles one request or use case from start to finish."),
          ("When does a domain model pay off?", "When rules are many, shared between use cases, and depend on state."),
          ("What's a signal to move from script to model?", "The same rule copied into several scripts, or long conditionals about state."),
          ("Can one app use both?", "Yes, and it usually should: scripts for simple areas, a model for the core.")],
    quiz_sit=[("A colleague wants to rewrite the 2,000-line returns script as a full domain model before adding a new “exchange” feature. The deadline is in six weeks. What do you suggest?",
               "Don't rewrite first. Write characterization tests around the script, extract the rules the exchange feature also needs (return window, condition checks) onto Order and a small value object, and build exchange on those. Move more rules later, one at a time.")],
    try_it="Find your longest procedure-style function. Mark each business rule in it, then search the codebase for the same rule elsewhere. Move the most-copied one onto an object and replace the copies.",
    then_now=dict(src="Fowler, PoEAA 2002", verdict="core",
                  then="Fowler offered three ways to organise domain logic (transaction script, table module, domain model) with a famous chart: scripts are cheapest for simple logic, models win as complexity grows.",
                  now="The chart still holds. Table module faded with .NET DataSets. The choice is now usually made per subdomain, and functional programming adds a third way: pure functions over precise types, which behaves like a model without classes.",
                  take="Still core: it's the real choice behind most “anemic or rich?” debates."),
    remember="A <span class=\"hl\">recipe card</span> for a snack; a <span class=\"hl\">chef</span> for a kitchen full of rules.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), ch. 2 “Organizing Domain Logic”.",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 5 “Implementing Simple Business Logic”.",
             "Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004).",
             "Martin Fowler, <i>Refactoring</i>, 2nd ed. (2018)."],
)

# ------------------------------------------------------------------ 12 Ports & Adapters
pa_problem = Doodle(760, 270, "Doodle of business logic welded to its framework. The order rules live inside Express route handlers and use Prisma calls directly. To test a discount rule you start an HTTP server and a database. Adding a CLI or a queue consumer for the same use case means copying the logic. Upgrading the framework means touching every rule.",
                    "Rules welded into route handlers: tests need HTTP and a database; a queue consumer copies the logic.")
pa_problem.box(160, 30, 440, 150, None, "pink", stroke="red")
pa_problem.head(380, 62, "app.post('/orders', …)")
pa_problem.text(380, 100, "req.body → prisma.order.update")
pa_problem.text(380, 134, "if (vip) discount… → res.json")
pa_problem.note(380, 216, "queue consumer? copy it · tests? start a server", "red")
pa_problem.note(380, 252, "framework upgrade? touch every rule", "red")

pa_analogy = Doodle(760, 250, "Doodle of a laptop with standard ports. The laptop doesn't care whether the screen is from one brand or another, or whether power comes from a wall socket or a power bank; it has USB-C ports, and adapters connect whatever you have. In a hotel abroad, you change the plug adapter, not the laptop.",
                     "The laptop has standard ports; adapters connect whatever screen or power you have.")
pa_analogy.box(260, 60, 240, 120, "laptop", "y", sub="USB-C ports")
pa_analogy.box(20, 40, 180, 60, "monitor", "paper", size=17)
pa_analogy.box(20, 140, 180, 60, "keyboard", "paper", size=17)
pa_analogy.box(560, 40, 180, 60, "UK plug", "paper", size=17)
pa_analogy.box(560, 140, 180, 60, "power bank", "paper", size=17)
for y in (70, 170):
    pa_analogy.arrow(204, y, 256, 120)
    pa_analogy.arrow(556, y, 504, 120)
pa_analogy.note(380, 230, "change the adapter, not the laptop", "green")

pa_how = Doodle(760, 340, "A hexagonal application. In the middle, the application core: use cases and the domain model, with no framework imports. On the left, driving adapters call the core through driving ports: an HTTP controller, a queue consumer, a CLI and the tests. On the right, the core calls driven ports, such as OrderRepository and PaymentPort, implemented by driven adapters: Postgres, Stripe, and an email service. All dependencies point inward.",
                 "Driving adapters call the core's use cases; the core calls driven ports that adapters implement. Arrows point inward.")
pa_how.raw('<path class="d f-y" d="M380 40 L520 110 V230 L380 300 L240 230 V110 Z"/>')
pa_how.head(380, 150, "core")
pa_how.text(380, 186, "use cases + domain")
pa_how.text(380, 214, "no framework")
for i, t in enumerate(["HTTP", "queue", "CLI", "tests"]):
    y = 40 + i * 66
    pa_how.box(20, y, 150, 50, t, "blue", size=16)
    pa_how.arrow(174, y + 25, 236, 170)
for i, t in enumerate(["Postgres", "Stripe", "email"]):
    y = 60 + i * 80
    pa_how.box(590, y, 150, 50, t, "green", size=16)
    pa_how.arrow(586, y + 25, 524, 170)
pa_how.note(95, 320, "driving side", "pen")
pa_how.note(665, 320, "driven side", "pen")

PORTS_ADAPTERS = dict(
    slug="ports-adapters",
    kicker="a.k.a. “hexagonal architecture, or the laptop with USB-C ports”",
    tldr="Put the <b>business core</b> (use cases and domain) in the middle, with <b>no framework, database or SDK imports</b>. The core declares <b>ports</b>: what it offers (use cases) and what it needs (repositories, payments). <b>Adapters</b> connect the outside world: HTTP, queues, CLIs and tests <b>drive</b> the core; Postgres, Stripe and email are <b>driven</b> by it. All dependencies point <b>inward</b>, so the core runs, and is tested, without the outside.",
    chips=[("Family", "application architecture"), ("From", "Alistair Cockburn (2005)"), ("Cousins", "onion (2008), clean architecture (2012)"), ("Built on", "dependency inversion")],
    problem="""  <p class="lead">When business rules live <span class="hl-pink">inside the framework's handlers</span>, they can't be tested, reused or kept through a framework change.</p>
  <ul>
    <li>Rules sit in route handlers calling the ORM directly.</li>
    <li>A queue consumer for the same use case copies the logic.</li>
    <li>Tests need a running server and a database.</li>
  </ul>""",
    problem_figs=[pa_problem],
    analogy_side="the laptop and its ports",
    analogy="""  <p>A <b>laptop</b> has standard ports. It doesn't care which brand the monitor is, or whether power comes from a wall or a power bank: <b>adapters</b> connect whatever you have. In a hotel abroad, you change the plug adapter, not the laptop.</p>
  <ul>
    <li>The laptop is the <b>core</b>.</li>
    <li>USB-C is a <b>port</b>.</li>
    <li>Cables and plugs are <b>adapters</b>.</li>
  </ul>""",
    analogy_figs=[pa_analogy],
    map=[("The laptop", "Use cases and domain model"),
         ("A USB-C port", "An interface the core defines"),
         ("Keyboard and monitor", "Driving adapters: HTTP, queue, CLI, tests"),
         ("Power from wall or power bank", "Driven adapters: Postgres, Stripe, email"),
         ("Swap the plug abroad", "Swap a provider in one adapter")],
    how_side="a core with ports, adapters around it",
    how="""  <p>Onion and clean architecture draw the same thing as rings with more layers. The essential rule in all three is one: <b>source dependencies point toward the core</b>. Don't add rings you don't need; two sides and a core is usually enough.</p>""",
    how_figs=[pa_how],
    steps=[("Pull rules out of handlers", "Each use case becomes a function or class in the core."),
           ("Define driving ports", "The use cases' input and output types, independent of HTTP."),
           ("Define driven ports", "Interfaces for what the core needs, in its own words."),
           ("Write adapters", "HTTP handler → use case; Postgres and Stripe implement driven ports."),
           ("Wire at start-up", "A composition root builds adapters and injects them."),
           ("Enforce the direction", "Architecture tests: the core imports nothing from adapters or frameworks.")],
    vocab=[("Hexagonal architecture", "Cockburn's name for ports and adapters; the hexagon has no meaning beyond “many sides”."),
           ("Port", "An interface at the core's border."),
           ("Driving (primary) adapter", "Calls the core: HTTP, CLI, queue, tests."),
           ("Driven (secondary) adapter", "Called by the core: database, payment, email."),
           ("Onion / clean architecture", "Ring-shaped variants with the same inward rule."),
           ("Composition root", "Where adapters are created and plugged in.")],
    code=dict(file="layout.txt", note="one service, ports and adapters", plain=True, src="""
src/
  core/                      # no imports from express, prisma, stripe
    orders/
      place-order.ts         # use case (driving port: handle(cmd))
      order.ts               # domain model
      ports.ts               # OrderRepository, PaymentPort (driven ports)
  adapters/
    http/orders.routes.ts    # express → placeOrder.handle()
    queue/orders.consumer.ts # same use case, from a queue
    postgres/orders.repo.ts  # implements OrderRepository
    stripe/payments.ts       # implements PaymentPort
  main.ts                    # composition root: wires adapters into the core
test/
  place-order.test.ts        # core + in-memory fakes, no server, no database
"""),
    tools="tools: plain modules and constructor injection; dependency-cruiser, ArchUnit, NetArchTest or Nx module boundaries to enforce inward dependencies; framework templates (NestJS, Spring) that can be bent to this layout.",
    gains=["<b>Core tested in milliseconds</b>, no server or database.",
           "<b>Many entry points</b>, one use case.",
           "<b>Frameworks and providers swappable</b>.",
           "<b>Clear place</b> for every kind of code."],
    losses=["<b>More files and interfaces</b>.",
            "<b>Mapping</b> between adapters and core types.",
            "<b>Overkill</b> for thin CRUD services.",
            "<b>Ring obsession</b>: too many layers in clean-architecture variants."],
    baseline="Each line compares <b>business rules inside framework handlers</b> to <b>a framework-free core with ports and adapters</b>.",
    ratings=[(3, 3, "Clearer core, more files to navigate."),
             (3, 4, "The core reads in business terms."),
             (3, 4, "Rules in one place, not copied per entry point."),
             (2, 4, "Framework and provider changes stay in adapters."),
             (2, 5, "Core tests without HTTP or databases."),
             (1, 5, "The core depends on nothing outside."),
             (3, 3, "Neutral; a little mapping."),
             (4, 2, "Ports, adapters, mapping and wiring."),
             (3, 4, "Adapter and core work in parallel.")],
    pitfalls=[("Hexagon for CRUD", "Ports and adapters around a service that just saves forms.", "use it where the core has real rules."),
              ("Too many rings", "Entities, use cases, interface adapters, frameworks, each with its own models and mappers.", "core and adapters; add layers only for a reason."),
              ("Leaky ports", "A port method takes an Express <code>Request</code> or returns a Prisma type.", "ports use the core's own types."),
              ("No enforcement", "One shortcut import and the direction is gone.", "architecture tests in CI.")],
    use=["Services with real business rules that must be tested well.",
         "One use case reached from several entry points (HTTP, queue, CLI).",
         "Infrastructure likely to change."],
    skip=["Thin CRUD services and prototypes.",
          "Scripts and small tools."],
    related=["<b>Dependency Inversion</b>", "<b>Vertical Slices</b>", "<b>Functional Core, Imperative Shell</b>", "<b>Anti-Corruption Layer</b> (Vol. 7)", "<b>Fakes</b> (Vol. 4)"],
    quiz=[("What's the one essential rule of ports and adapters?", "Source dependencies point inward: the core imports nothing from adapters or frameworks."),
          ("What's the difference between driving and driven adapters?", "Driving adapters call the core (HTTP, CLI, tests); driven adapters are called by it (database, payments)."),
          ("How do onion and clean architecture relate?", "They are ring-shaped variants of the same idea, with more named layers."),
          ("When is it overkill?", "In thin CRUD services and prototypes with few rules.")],
    quiz_sit=[("Your team must add a Kafka consumer that places orders, but all the order logic lives in an Express handler. Copying it is the fastest option. What do you do?",
               "Extract the logic into a PlaceOrder use case in a core module with ports for its repository and payments, make the Express handler call it, then write the Kafka consumer as a second driving adapter calling the same use case. Add tests on the use case with fakes.")],
    try_it="Take one route handler with business rules in it. Move the rules into a function in a core folder that takes plain inputs and ports, make the handler call it, and write a test of the function without HTTP or a database.",
    then_now=dict(src="Cockburn, 2005", verdict="grown",
                  then="Cockburn described the hexagonal architecture in 2005 so applications could be driven equally by users, programs and tests, and run without their databases. Onion (Palermo, 2008) and clean architecture (Martin, 2012) followed with rings.",
                  now="It's now the default shape for services with real logic, and the reason fast core tests are possible. The lesson learned since: keep it to a core and adapters; the many-ringed versions often add mapping without benefit.",
                  take="Matters more now, in its simple form: a core, ports, adapters, and dependencies pointing in."),
    remember="Change the <span class=\"hl\">plug</span>, never the <span class=\"hl\">laptop</span>.",
    sources=["Alistair Cockburn, “Hexagonal Architecture” (2005).",
             "Alistair Cockburn &amp; Juan Manuel Garrido de Paz, <i>Hexagonal Architecture Explained</i> (2024).",
             "Jeffrey Palermo, “The Onion Architecture” (2008).",
             "Robert C. Martin, <i>Clean Architecture</i> (2017)."],
)

# ------------------------------------------------------------------ 13 Vertical Slices
vs_problem = Doodle(760, 260, "Doodle of a feature spread across technical layers. Adding a cancel order feature means editing files in five folders: controllers, services, repositories, DTOs and mappers. The shared OrderService grows to forty methods used by twenty features, and every change to it risks breaking features nobody is looking at.",
                    "One small feature touches five folders, and the shared OrderService has forty methods.")
for i, t in enumerate(["controllers/", "services/", "repositories/", "dtos/", "mappers/"]):
    y = 20 + i * 44
    vs_problem.box(20, y, 220, 36, t, "paper", size=15)
    vs_problem.arrow(244, y + 18, 300, 120, color="red", dash=True)
vs_problem.box(310, 80, 180, 80, "“cancel order”", "y", sub="5 folders", size=17)
vs_problem.box(540, 80, 200, 80, "OrderService", "pink", stroke="red", sub="40 methods")
vs_problem.note(640, 200, "used by 20 features", "red")

vs_analogy = Doodle(760, 250, "Doodle of a layered cake. You don't serve a guest the whole sponge layer, then the whole cream layer, then the whole fruit layer. You cut a slice that has a bit of every layer. Each guest's slice is complete on its own, and cutting one doesn't disturb the others.",
                     "Serve a slice with every layer in it, not the whole cream layer to one guest.")
vs_analogy.box(200, 40, 360, 50, "fruit", "pink", size=17)
vs_analogy.box(200, 90, 360, 50, "cream", "paper", size=17)
vs_analogy.box(200, 140, 360, 50, "sponge", "y", size=17)
vs_analogy.line("M216 30 V200 M268 30 V200", dash=True)
vs_analogy.note(242, 226, "one slice = all layers", "green")
vs_analogy.note(650, 120, "a feature is a slice", "pen")

vs_how = Doodle(760, 320, "Vertical slice layout. Each feature folder, such as place-order, cancel-order and order-history, holds its own endpoint, handler, request and response types, data access and tests. Slices share only the domain model and infrastructure basics. A new feature is a new folder; changing one rarely touches another. Each slice can use the style it needs: a simple query or a rich domain call.",
                 "One folder per feature, end to end. Share the domain, not a giant service.")
for i, (name, sub) in enumerate([("place-order", "rich: domain"), ("cancel-order", "rich: domain"), ("order-history", "simple: one query")]):
    x = 20 + i * 250
    vs_how.box(x, 20, 220, 190, None, "blue" if i < 2 else "y", dash=True)
    vs_how.head(x + 110, 52, name)
    vs_how.text(x + 110, 90, "endpoint · handler")
    vs_how.text(x + 110, 122, "types · data · tests")
    vs_how.text(x + 110, 166, sub)
vs_how.box(140, 240, 480, 56, "shared: domain model · infrastructure", "green", size=16)

VERTICAL_SLICES = dict(
    slug="vertical-slices",
    kicker="a.k.a. “serve a slice, not a layer”",
    tldr="Organise code by <b>feature</b> instead of by technical layer. Each slice (<code>place-order/</code>, <code>cancel-order/</code>) holds its own endpoint, handler, request and response types, data access and tests. Slices share the <b>domain model</b> and basic infrastructure, not a giant <code>OrderService</code>. A new feature is a <b>new folder</b>; changing one rarely <b>touches another</b>; each slice can be as simple or rich as it needs.",
    chips=[("Family", "application architecture"), ("Named by", "Jimmy Bogard (2018)"), ("Instead of", "controllers/ services/ repositories/ folders"), ("Pairs with", "CQRS, single responsibility")],
    problem="""  <p class="lead">Layered folders spread every feature <span class="hl-pink">across the codebase</span> and grow <span class="hl-pink">shared services</span> that every feature depends on.</p>
  <ul>
    <li>A small feature edits five folders.</li>
    <li>OrderService has forty methods used by twenty features.</li>
    <li>A change for one feature breaks another nobody was looking at.</li>
  </ul>""",
    problem_figs=[vs_problem],
    analogy_side="the layered cake",
    analogy="""  <p>You don't serve one guest the whole <b>sponge layer</b> and another the whole <b>cream layer</b>. You cut a <b>slice</b> with some of every layer. Each slice is complete on its own, and cutting one doesn't disturb the others.</p>
  <ul>
    <li>The layers are <b>technical layers</b>: endpoint, logic, data.</li>
    <li>A slice is a <b>feature</b>, end to end.</li>
  </ul>""",
    analogy_figs=[vs_analogy],
    map=[("The cake's layers", "HTTP, application logic, data access"),
         ("A slice", "One feature folder with all its layers"),
         ("A guest's plate", "A pull request that touches one folder"),
         ("Cutting doesn't disturb the rest", "Changes stay inside one slice"),
         ("The cake stand everyone shares", "Domain model and infrastructure")],
    how_side="one folder per feature",
    how="""  <p>Slices pair naturally with <b>CQRS</b>: each command and query is a slice. They also combine with ports and adapters: the slices live in the core, and adapters stay outside. Watch for <b>duplication</b> between slices; when real rules repeat, push them into the domain model.</p>""",
    how_figs=[vs_how],
    steps=[("Pick one feature", "New features are the easiest start; don't move everything at once."),
           ("Create its folder", "Endpoint, handler, request and response types, tests, all together."),
           ("Choose the slice's style", "A simple query for reads; domain model calls for rich writes."),
           ("Share the domain, not services", "Rules go on entities and value objects that slices call."),
           ("Retire the giant service", "Move its methods into the slices that use them, one at a time."),
           ("Keep cross-cutting concerns in middleware", "Logging, auth and validation as pipeline behaviours.")],
    vocab=[("Vertical slice", "All the code for one feature or use case, kept together."),
           ("Layered architecture", "Code organised by technical layer: presentation, logic, data."),
           ("Feature folder", "A directory per feature."),
           ("Pipeline behaviour", "Middleware around every handler (logging, validation, transactions)."),
           ("Coupling between features", "Features depending on each other through shared services."),
           ("Screaming architecture", "A folder structure that tells you what the app does, not which framework it uses.")],
    code=dict(file="layout.txt", note="features, not layers", plain=True, src="""
src/features/
  place-order/
    place-order.endpoint.ts   # POST /orders
    place-order.handler.ts    # loads Order, calls domain, saves
    place-order.types.ts      # request / response DTOs
    place-order.test.ts
  cancel-order/
    ...
  order-history/
    order-history.endpoint.ts # GET /customers/:id/orders
    order-history.query.ts    # one SQL projection, no domain objects
    order-history.test.ts
src/domain/                   # Order, Money, ... shared by slices
src/infrastructure/           # db, broker, http server, middleware
"""),
    tools="tools: MediatR or similar handler libraries, NestJS or Fastify modules per feature, Next.js and Remix route folders (slices by default), architecture tests to stop slices importing each other.",
    gains=["<b>Feature changes stay local</b>: one folder.",
           "<b>No giant shared services</b>.",
           "<b>Each slice picks its style</b>: simple or rich.",
           "<b>Easy to find</b>, delete or own a feature."],
    losses=["<b>Some duplication</b> between slices.",
            "<b>Rules can scatter</b> if not pushed into the domain.",
            "<b>Unfamiliar</b> to teams used to layers.",
            "<b>Cross-cutting changes</b> touch many folders."],
    baseline="Each line compares <b>code organised by technical layer with shared services</b> to <b>code organised in vertical feature slices</b>.",
    ratings=[(3, 4, "Everything for a feature in one place."),
             (3, 4, "Folders named after what the app does."),
             (3, 3, "Neutral; shared rules must still live in the domain."),
             (2, 4, "A feature changes in one folder."),
             (3, 4, "Tests sit next to the feature they test."),
             (2, 4, "Features don't share giant services."),
             (3, 4, "Read slices can use lean queries."),
             (3, 4, "No service/repository/mapper per entity by default."),
             (2, 5, "Teams own features without colliding.")],
    pitfalls=[("Copying rules between slices", "The same discount check in three handlers.", "move shared rules onto the domain model."),
              ("Slices importing slices", "cancel-order calls place-order's handler.", "share the domain; communicate through it or events."),
              ("Big-bang reorganisation", "A month-long PR moving every file.", "new features as slices; migrate old ones when touched."),
              ("No shared conventions", "Every slice structured differently.", "a template for slice layout and naming.")],
    use=["Feature-heavy apps where most changes are “add or change a feature”.",
         "Shared services that keep growing and breaking.",
         "Teams that own features end to end."],
    skip=["Libraries and frameworks (layers by concept make sense there).",
          "Tiny apps with a handful of endpoints."],
    related=["<b>Single Responsibility</b>", "<b>Ports &amp; Adapters</b>", "<b>Transaction Script vs Domain Model</b>", "<b>CQRS</b> (Vol. 1)", "<b>Domain &amp; Application Services</b> (Vol. 7)"],
    quiz=[("What is a vertical slice?", "All the code for one feature or use case, from endpoint to data access and tests, kept together."),
          ("What do slices share?", "The domain model and infrastructure basics, not large services."),
          ("How do slices pair with CQRS?", "Each command and each query becomes its own slice."),
          ("What's the main risk?", "Business rules duplicated across slices instead of living in the domain model.")],
    quiz_sit=[("Two teams keep breaking each other's features through a shared <code>CustomerService</code> with 55 methods. Reorganising the whole codebase isn't possible this quarter. What do you do?",
               "Build every new feature as a slice, and when a team changes an existing feature, move the methods it uses out of CustomerService into that feature's slice (rules onto the domain). The service shrinks over time; add a rule that no new methods go into it.")],
    try_it="Take the next feature you build and put everything for it in one folder: endpoint, handler, types and tests. After it's merged, count how many files outside that folder the pull request touched.",
    then_now=dict(src="Fowler, PoEAA 2002 (layering); Bogard, 2018", verdict="grown",
                  then="PoEAA opened with layering: presentation, domain and data source as separate layers, which most frameworks turned into folders of controllers, services and repositories.",
                  now="Layers still describe dependencies well, but as a folder structure they scatter features. Vertical slices (Bogard, 2018), feature folders and route-based frameworks like Next.js organise by feature instead, often combined with CQRS and a shared domain.",
                  take="Matters more now: layers for dependency direction, slices for folders."),
    remember="Serve a <span class=\"hl\">slice</span>, not a <span class=\"hl\">layer</span>.",
    sources=["Jimmy Bogard, “Vertical Slice Architecture” (2018).",
             "Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), ch. 1 “Layering”.",
             "Robert C. Martin, “Screaming Architecture” (2011).",
             "Derek Comartin, “Vertical Slice Architecture” talks and articles (CodeOpinion)."],
)

# ------------------------------------------------------------------ 14 Functional Core, Imperative Shell
fc_problem = Doodle(760, 260, "Doodle of logic tangled with input and output. A function loads the basket from the database, computes discounts, calls the tax API, computes totals, checks stock with another API, decides on a delivery slot and writes to the database, all interleaved. Its test needs five mocks set up in the right order, and it breaks whenever the call order changes.",
                    "Load, decide, call an API, decide, call another, decide, save, all mixed: five mocks per test.")
steps = [("load", "paper"), ("decide", "y"), ("tax API", "paper"), ("decide", "y"), ("stock API", "paper"), ("decide", "y"), ("save", "paper")]
for i, (t, f) in enumerate(steps):
    fc_problem.box(14 + i * 106, 60, 96, 56, t, f, size=15)
fc_problem.note(380, 170, "decisions sandwiched between side effects", "red")
fc_problem.note(380, 214, "test = 5 mocks in the right order", "red")

fc_analogy = Doodle(760, 250, "Doodle of an architect and a builder. The architect draws plans at a desk using measurements: no concrete, no cranes, and the plans can be checked, copied and changed for free. The builder takes the plans and does the heavy, risky work on site. Mistakes are cheap to fix on paper, expensive in concrete.",
                     "The architect decides on paper (cheap to check); the builder pours concrete (the risky part).")
fc_analogy.box(20, 50, 340, 110, None, "green")
fc_analogy.head(190, 84, "architect: plans")
fc_analogy.text(190, 122, "pure: checkable on paper")
fc_analogy.box(400, 50, 340, 110, None, "y")
fc_analogy.head(570, 84, "builder: concrete")
fc_analogy.text(570, 122, "effects: the risky part")
fc_analogy.arrow(364, 105, 396, 105)
fc_analogy.note(380, 210, "decide on paper, then build", "pen")

fc_how = Doodle(760, 320, "Functional core, imperative shell for checkout. The shell gathers everything first: basket, customer, tax rates and stock levels. It passes plain data to a pure function, priceCheckout, which returns a decision: totals, chosen slot and a list of effects to perform. The shell then performs the effects: save, reserve stock, publish an event. The pure core is tested with plain values and no mocks.",
                 "Shell: gather → pure core decides → shell performs. The core gets values in and returns a decision.")
fc_how.row([("gather", "basket · rates · stock", "paper"), ("decide (pure)", "priceCheckout()", "green"), ("perform", "save · reserve · publish", "paper")], x=20, y=60, h=100, gap=50, size=17, subsize=13, arrows=True)
fc_how.note(380, 210, "core: values in, decision out, no I/O", "green")
fc_how.note(380, 250, "tests: plain data, no mocks", "green")
fc_how.note(380, 290, "shell: thin, few branches, tested end to end", "pen")

FUNCTIONAL_CORE = dict(
    slug="functional-core",
    kicker="a.k.a. “decide on paper, then pour the concrete”",
    tldr="Split code into a <b>pure core</b> that makes <b>decisions</b> from plain values (no database, network, clock or randomness) and a thin <b>imperative shell</b> that <b>gathers</b> inputs, calls the core, and <b>performs</b> the effects it returns. The core gets values in and returns a decision; it's <b>trivial to test</b> without mocks. The shell has few branches and is covered by a handful of integration tests.",
    chips=[("Family", "application structure"), ("Named by", "Gary Bernhardt (2012)"), ("Related", "impureim sandwich, ports and adapters"), ("Pairs with", "make illegal states unrepresentable (Vol. 7)")],
    problem="""  <p class="lead">When decisions are <span class="hl-pink">interleaved with input and output</span>, every test needs a pile of mocks in the right order.</p>
  <ul>
    <li>Load, decide, call an API, decide, call another, decide, save.</li>
    <li>Tests need five mocks and break when the call order changes.</li>
    <li>Nobody can see the business decision for the plumbing.</li>
  </ul>""",
    problem_figs=[fc_problem],
    analogy_side="the architect and the builder",
    analogy="""  <p>An <b>architect</b> draws plans from measurements: no concrete, no cranes. Plans can be checked, copied and changed <b>for free</b>. The <b>builder</b> takes the plans and does the heavy, risky work on site. Mistakes are cheap on paper and expensive in concrete.</p>
  <ul>
    <li>The architect is the <b>functional core</b>.</li>
    <li>The builder is the <b>imperative shell</b>.</li>
  </ul>""",
    analogy_figs=[fc_analogy],
    map=[("Measurements handed to the architect", "Values gathered by the shell"),
         ("Drawing the plans", "A pure function computing a decision"),
         ("Checking plans on paper", "Unit tests with plain values, no mocks"),
         ("The builder on site", "The shell performing effects: save, call, publish"),
         ("Few decisions on site", "A thin shell with few branches")],
    how_side="gather, decide, perform",
    how="""  <p>Mark Seemann calls the shape an <b>impureim sandwich</b>: impure, pure, impure. It's ports and adapters at the scale of a single function. When the core needs more data midway, return a decision that says “need X” and let the shell loop, or gather more up front.</p>""",
    how_figs=[fc_how],
    steps=[("Find the decision", "In a tangled function, what's the business decision being made?"),
           ("Gather inputs first", "Load everything the decision needs, including the current time."),
           ("Write the pure function", "Plain values in, a decision or list of effects out; no I/O, no <code>Date.now()</code>."),
           ("Perform effects after", "Save, call APIs and publish based on the returned decision."),
           ("Test the core with examples", "Tables of inputs and expected decisions; property-based tests fit well."),
           ("Keep the shell dumb", "If the shell grows branches, move decisions into the core.")],
    vocab=[("Pure function", "Same inputs, same output, no side effects."),
           ("Side effect", "Anything observable outside the function: I/O, mutation, time, randomness."),
           ("Functional core", "The pure part that makes decisions."),
           ("Imperative shell", "The thin part that does I/O around the core."),
           ("Impureim sandwich", "Impure gather, pure decide, impure perform."),
           ("Decision object", "A returned value describing what should happen.")],
    code=dict(file="checkout.ts", note="pure decision, effects in the shell", src="""
// core: pure, no I/O, no clock
export type CheckoutDecision =
  | { ok: true; total: Money; slot: Slot; reserve: Line[] }
  | { ok: false; reason: "out-of-stock" | "no-slot"; missing?: ProductId[] };

export function decideCheckout(basket: Basket, rates: TaxRates, stock: StockLevels,
                               slots: Slot[], now: Date): CheckoutDecision {
  const missing = basket.lines.filter((l) => (stock.get(l.productId) ?? 0) < l.qty).map((l) => l.productId);
  if (missing.length) return { ok: false, reason: "out-of-stock", missing };
  const slot = slots.find((s) => s.start > addHours(now, 2));
  if (!slot) return { ok: false, reason: "no-slot" };
  return { ok: true, total: priceWithTax(basket, rates), slot, reserve: basket.lines };
}

// shell: gather -> decide -> perform
const d = decideCheckout(await baskets.get(id), await tax.rates(), await stock.levels(ids), await slots.free(), new Date());
if (d.ok) { await stockApi.reserve(d.reserve); await orders.save(Order.place(id, d.total, d.slot)); }
"""),
    tools="tools: plain functions and types; property-based testing (fast-check, Hypothesis) for the core; functional libraries (Effect, fp-ts, Arrow) if your team wants effects modelled explicitly, though they aren't needed.",
    gains=["<b>Decisions tested without mocks</b>.",
           "<b>Clear business logic</b>, separate from plumbing.",
           "<b>Deterministic</b>: time and randomness passed in.",
           "<b>Easy to reuse</b> the core elsewhere."],
    losses=["<b>Gathering up front</b> may load more than needed.",
            "<b>Awkward</b> when decisions need data in several rounds.",
            "<b>Decision types</b> to define.",
            "<b>Unfamiliar</b> to object-oriented habits."],
    baseline="Each line compares <b>decisions interleaved with I/O</b> to <b>a pure core between a gathering and a performing shell</b>.",
    ratings=[(2, 4, "Decision and plumbing are separate and short."),
             (3, 4, "The core reads as the business decision."),
             (3, 4, "Pure decisions are easy to test exhaustively."),
             (3, 4, "Rules change in the core; plumbing in the shell."),
             (2, 5, "Values in, values out, no mocks."),
             (2, 4, "The core depends on nothing."),
             (3, 3, "May over-fetch inputs; usually negligible."),
             (3, 3, "Decision types vs mock setup: roughly even."),
             (3, 3, "Neutral.")],
    pitfalls=[("Hidden effects in the core", "The “pure” function calls <code>Date.now()</code> or a logger.", "pass time in; return log entries if needed."),
              ("A fat shell", "The shell grows if-statements about business cases.", "move decisions into the core; the shell just follows them."),
              ("Mocking the core", "Tests of the shell mock the pure function.", "test the core with values; test the shell end to end, lightly."),
              ("Forcing it everywhere", "Contortions for a simple CRUD save.", "use it where decisions are rich enough to deserve tests.")],
    use=["Functions that make business decisions and also do I/O.",
         "Tests full of mocks and call-order assertions.",
         "Logic that depends on time or randomness."],
    skip=["Pure plumbing with no decisions (just a save).",
          "Decisions that truly need many rounds of I/O (use a state machine or workflow)."],
    related=["<b>Ports &amp; Adapters</b>", "<b>Transaction Script vs Domain Model</b>", "<b>Make Illegal States Unrepresentable</b> (Vol. 7)", "<b>Controlled Time &amp; Randomness</b> (Vol. 4)", "<b>Property-Based Testing</b> (Vol. 4)"],
    quiz=[("What goes in the functional core?", "Pure decision-making: plain values in, a decision out, no I/O, clock or randomness."),
          ("What does the shell do?", "Gathers inputs, calls the core, and performs the effects it decides."),
          ("How do you handle the current time?", "The shell reads it and passes it in as a value."),
          ("Why does this reduce mocking?", "The core has no dependencies, so tests pass values and check results.")],
    quiz_sit=[("A test for the delivery-fee rule needs mocks for the database, the clock, the maps API and the feature-flag client, and fails whenever someone reorders calls. How do you restructure it?",
               "Gather the basket, address distance, current time and flag value in the shell, pass them as values to a pure <code>deliveryFee(…)</code> function, and test that function with a table of examples. Keep one integration test for the shell.")],
    try_it="Pick a function in your code that both reads from somewhere and decides something. Split it into gather, a pure decide function, and perform. Write five example tests for the pure part with no mocks.",
    then_now=dict(src="Bernhardt, 2012 (not in the 2002–2005 books)", verdict="grown",
                  then="The enterprise books of 2002–2005 had no such split: logic lived in objects or scripts that called repositories and services freely, tested with mocks.",
                  now="Gary Bernhardt's “Boundaries” talk (2012) named it, functional programming made it mainstream, and Mark Seemann's “impureim sandwich” gave it a recipe. It's the small-scale version of ports and adapters, and the easiest way to cut mock-heavy tests.",
                  take="A newer idea that matters more and more; use it wherever decisions hide among I/O."),
    remember="Decide <span class=\"hl\">on paper</span>; pour <span class=\"hl\">concrete</span> only after.",
    sources=["Gary Bernhardt, “Boundaries” (talk, 2012) and “Functional Core, Imperative Shell” (Destroy All Software).",
             "Mark Seemann, “Impureim sandwich” (blog, 2020).",
             "Scott Wlaschin, <i>Domain Modeling Made Functional</i> (2018), ch. 12.",
             "Eric Normand, <i>Grokking Simplicity</i> (2021)."],
)

NOTES = [TRANSACTION_SCRIPT, PORTS_ADAPTERS, VERTICAL_SLICES, FUNCTIONAL_CORE]
