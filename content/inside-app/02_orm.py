# Vol. 8 · Inside the Application · Inside your ORM: Active Record vs Data Mapper, Unit of Work & Identity Map,
# Lazy Loading, Offline Locks & ETags, DTOs & Remote Facade. Source: Fowler, Patterns of Enterprise Application
# Architecture (2002).

# ------------------------------------------------------------------ 06 Active Record vs Data Mapper
ar_problem = Doodle(760, 260, "Doodle of the wrong persistence style for each area. In the pricing engine, an Active Record class mixes forty business rules with save and find methods, and every rule's test needs a database. Meanwhile the admin screen for store opening hours has a domain class, a mapper, a repository and a DTO for four fields.",
                    "Rules tangled with save() where logic is rich; four layers of mapping for a four-field admin form.")
ar_problem.box(20, 40, 340, 130, None, "pink", stroke="red")
ar_problem.head(190, 74, "Price (Active Record)")
ar_problem.text(190, 110, "40 rules + save() + find()")
ar_problem.text(190, 142, "tests need a database")
ar_problem.box(400, 40, 340, 130, None, "pink", stroke="red")
ar_problem.head(570, 74, "OpeningHours")
ar_problem.text(570, 110, "entity + mapper + repo + DTO")
ar_problem.text(570, 142, "for four fields")
ar_problem.note(380, 220, "the right tool, each in the wrong place", "red")

ar_analogy = Doodle(760, 250, "Doodle of two ways to file letters. In a small office, each letter carries a sticky note saying which drawer it goes in, and anyone files it themselves. In a big legal firm, a records clerk files everything, and the letters know nothing about drawers, so the filing system can change without rewriting any letter.",
                     "Small office: each letter files itself. Big firm: a clerk does the filing; letters know nothing about drawers.")
ar_analogy.box(20, 40, 340, 120, None, "y")
ar_analogy.head(190, 74, "letter files itself")
ar_analogy.text(190, 112, "quick, fine for a few")
ar_analogy.box(400, 40, 340, 120, None, "blue")
ar_analogy.head(570, 74, "records clerk files")
ar_analogy.text(570, 112, "letters know no drawers")
ar_analogy.note(190, 200, "Active Record", "pen")
ar_analogy.note(570, 200, "Data Mapper", "pen")

ar_how = Doodle(760, 320, "The two styles side by side. Active Record: one class per table row that holds data, a few rules, and save, find and delete; used by Rails, Laravel Eloquent and Django. Data Mapper: plain domain objects with no persistence code, and a separate mapper or ORM session that loads and saves them; used by Hibernate, EF Core, Doctrine and MikroORM. Choose Active Record for simple CRUD and Data Mapper for rich domains.",
                 "Active Record: the object saves itself. Data Mapper: a mapper saves plain objects. Pick per area.")
ar_how.box(20, 20, 340, 150, None, "y")
ar_how.head(190, 52, "Active Record")
ar_how.text(190, 90, "order.total = …")
ar_how.text(190, 124, "await order.save()")
ar_how.text(190, 156, "Rails · Eloquent · Django")
ar_how.box(400, 20, 340, 150, None, "blue")
ar_how.head(570, 52, "Data Mapper")
ar_how.text(570, 90, "order.addLine(…)")
ar_how.text(570, 124, "await em.persist(order)")
ar_how.text(570, 156, "Hibernate · EF Core · Doctrine")
ar_how.note(190, 220, "simple CRUD, few rules", "green")
ar_how.note(570, 220, "rich domain, many rules", "green")
ar_how.note(380, 290, "both can live in one app, per area", "pen")

ACTIVE_RECORD = dict(
    slug="active-record-data-mapper",
    kicker="a.k.a. “the letter that files itself, or the records clerk”",
    tldr="Two ways to save objects. <b>Active Record</b>: one object per row that holds data and knows how to <code>save()</code> and <code>find()</code> itself (Rails, Laravel, Django). Quick and clear when rules are few. <b>Data Mapper</b>: plain domain objects that know nothing about the database, and a separate mapper or ORM session that loads and saves them (Hibernate, EF Core, Doctrine). More setup, but rules stay testable and the schema can differ from the model. <b>Pick per area</b>, by how complex the rules are.",
    chips=[("Family", "data source pattern"), ("From", "Fowler, PoEAA (2002)"), ("Active Record in", "Rails, Laravel, Django"), ("Data Mapper in", "Hibernate, EF Core, Doctrine, MikroORM")],
    problem="""  <p class="lead">Teams pick a persistence style by habit, then find it <span class="hl-pink">fighting the code</span> in the areas it doesn't suit.</p>
  <ul>
    <li>Business rules tangled with <code>save()</code>; every test needs a database.</li>
    <li>Or four layers of mapping for a four-field admin form.</li>
    <li>Arguments about which ORM is “right” for the whole company.</li>
  </ul>""",
    problem_figs=[ar_problem],
    analogy_side="filing letters",
    analogy="""  <p>In a <b>small office</b>, each letter carries a note saying which drawer it goes in, and anyone files it. Fast and simple. In a <b>big legal firm</b>, a <b>records clerk</b> does all the filing; letters know nothing about drawers, so the filing system can change without rewriting a single letter.</p>
  <ul>
    <li>Self-filing letters are <b>Active Record</b>.</li>
    <li>The clerk is a <b>Data Mapper</b>.</li>
  </ul>""",
    analogy_figs=[ar_analogy],
    map=[("A letter with its drawer note", "An Active Record object with <code>save()</code>"),
         ("Anyone can file it", "Any code can load and save rows directly"),
         ("The records clerk", "The ORM session or mapper (<code>DbContext</code>, <code>EntityManager</code>)"),
         ("Letters know no drawers", "Domain objects with no persistence code"),
         ("Changing the filing system", "Changing the schema without changing the model")],
    how_side="two styles, pick per area",
    how="""  <p>Active Record maps <b>one class to one table</b>, so the model follows the schema. Data Mapper lets the model and schema <b>differ</b> (value objects in columns, aggregates over several tables). That freedom is what rich domains need, and what CRUD doesn't.</p>""",
    how_figs=[ar_how],
    steps=[("Look at the rules", "Few rules and forms? Active Record. Many rules, invariants, aggregates? Data Mapper."),
           ("Use your framework's default where it fits", "Rails and Laravel shine at Active Record; don't fight them for CRUD."),
           ("Keep rules out of callbacks", "In Active Record, avoid business logic in before-save hooks."),
           ("Keep persistence out of the model", "In Data Mapper, entities don't import the ORM's session."),
           ("Mix by area", "Active Record for admin and reporting, Data Mapper for the core."),
           ("Revisit when an area grows", "Rules multiplying in an Active Record class? Extract a domain object.")],
    vocab=[("Active Record", "An object wrapping a database row, with data, some logic and its own persistence."),
           ("Data Mapper", "A layer that moves data between objects and the database, keeping them independent."),
           ("Persistence ignorance", "Domain objects that don't know how they're stored."),
           ("Callback / hook", "Code run before or after save in Active Record frameworks."),
           ("Object-relational mismatch", "The differences between objects and tables that mappers bridge."),
           ("ORM", "Object-relational mapper: a library implementing one or both styles.")],
    code=dict(file="two-styles.ts", note="the same change in each style", src="""
// Active Record (e.g. TypeORM BaseEntity, Rails, Eloquent): the row saves itself
const hours = await OpeningHours.findOneByOrFail({ storeId, day: "mon" });
hours.closes = "21:00";
await hours.save();

// Data Mapper (e.g. MikroORM, Hibernate, EF Core): a plain object, a session saves it
const order = await em.findOneOrFail(Order, orderId);   // Order has no persistence code
order.addLine(productId, Quantity.of(2), price);        // rules on the object
await em.flush();                                       // the mapper writes the changes
"""),
    tools="tools: Rails ActiveRecord, Laravel Eloquent, Django ORM and TypeORM's BaseEntity for Active Record; Hibernate/JPA, EF Core, Doctrine, MikroORM and SQLAlchemy's ORM for Data Mapper; query builders (Kysely, jOOQ) when you want neither.",
    gains=["<b>Active Record</b>: very little code for CRUD.",
           "<b>Data Mapper</b>: rules testable without a database.",
           "<b>Data Mapper</b>: model and schema can differ.",
           "<b>Choosing per area</b> gives the best of both."],
    losses=["<b>Active Record</b>: rules and persistence tangle as logic grows.",
            "<b>Data Mapper</b>: more mapping and configuration.",
            "<b>Two styles</b> in one codebase to explain.",
            "<b>Switching later</b> takes refactoring."],
    baseline="Each line compares <b>one persistence style used everywhere by habit</b> to <b>Active Record for simple areas and Data Mapper for the rich core</b>.",
    ratings=[(3, 4, "Each area uses the lighter fitting style."),
             (3, 4, "The core's model isn't bent to the table layout."),
             (3, 4, "Core rules tested without persistence in the way."),
             (3, 4, "Schema and model change more independently in the core."),
             (2, 4, "Core tests run in memory."),
             (3, 4, "The core doesn't import the ORM."),
             (3, 3, "Neutral; both can be fast or slow."),
             (3, 4, "No mapping ceremony where CRUD will do."),
             (3, 3, "Neutral.")],
    pitfalls=[("Rules in callbacks", "Before-save hooks send emails and change other rows.", "explicit service or domain methods; keep hooks for timestamps."),
              ("Active Record in a rich core", "A 2,000-line model class with rules and queries mixed.", "extract a domain object, or move that area to Data Mapper."),
              ("Data Mapper for forms", "Entity, mapper, repository and DTO for a settings page.", "plain Active Record or a direct query."),
              ("Leaking the session", "Entities call the ORM session to load more data.", "load what's needed in the application service.")],
    use=["Choosing an ORM or persistence approach for an area.",
         "An Active Record class whose rules are growing.",
         "Tests that need a database only because of persistence style."],
    skip=["Read-only reporting: plain SQL or a query builder is simpler than either.",
          "Rewriting a working CRUD app just to be “clean”."],
    related=["<b>Transaction Script vs Domain Model</b>", "<b>Unit of Work &amp; Identity Map</b>", "<b>Repository</b> (Vol. 7)", "<b>Anemic Domain Model</b> (Vol. 7)"],
    quiz=[("What is Active Record?", "An object that wraps a database row and contains both data, some logic and its own save/find methods."),
          ("What is Data Mapper?", "A separate layer that loads and saves plain domain objects, so they don't know about the database."),
          ("When does Active Record fit best?", "Simple CRUD areas with few rules, where model and table match closely."),
          ("Can one app use both?", "Yes: Active Record for simple areas and Data Mapper for the rich core is a common mix.")],
    quiz_sit=[("Your Rails app's <code>Subscription</code> model has 1,800 lines: billing rules, callbacks that call Stripe, and scopes. Every test needs the database and stubs Stripe. What's a first step?",
               "Extract the billing rules into a plain Ruby domain object (or service) that takes values and returns decisions, move the Stripe calls out of callbacks into an explicit application step, and keep the Active Record model for persistence and simple scopes.")],
    try_it="Pick one model class in your app and count its business rules and its persistence methods. If rules dominate, extract the three most important into a plain object with no ORM imports and test it without a database.",
    then_now=dict(src="Fowler, PoEAA 2002", verdict="built-in",
                  then="Fowler described both, plus Table Data Gateway and Row Data Gateway, as patterns you might implement by hand, with advice on when each fits.",
                  now="Every major ORM is one or the other: Rails, Laravel and Django are Active Record; Hibernate, EF Core, Doctrine and MikroORM are Data Mappers. You choose a style by choosing a framework, and Fowler's advice on when each fits is still exactly right.",
                  take="Built in now: you don't write them, but knowing which one you're using tells you where your rules should live."),
    remember="Let a few letters <span class=\"hl\">file themselves</span>; give the big firm <span class=\"hl\">a records clerk</span>.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Active Record”, “Data Mapper”.",
             "Rails Guides, “Active Record Basics”.",
             "Microsoft, “EF Core: persistence ignorance” (.NET architecture guides).",
             "MikroORM documentation, “Unit of Work and Identity Map”."],
)

# ------------------------------------------------------------------ 07 Unit of Work & Identity Map
uw_problem = Doodle(760, 270, "Doodle of saving changes by hand. A request changes an order, two order lines and the customer's credit. The code calls save four times. The third save fails, so the order is changed but the credit isn't. Elsewhere in the same request, the customer was loaded twice into two different objects; one change overwrote the other.",
                    "Four separate saves, the third fails: half-saved. And two copies of one customer overwrite each other.")
for i, t in enumerate(["save(order)", "save(line 1)", "save(line 2)", "save(credit)"]):
    x = 20 + i * 185
    bad = i == 2
    uw_problem.box(x, 40, 165, 56, t, "pink" if bad else "paper", stroke="red" if bad else "", size=15)
uw_problem.note(380, 140, "fails at the third: half the change is saved", "red")
uw_problem.box(130, 180, 220, 56, "customer (copy 1)", "y", size=15)
uw_problem.box(410, 180, 220, 56, "customer (copy 2)", "y", size=15)
uw_problem.note(380, 262, "last write wins, silently", "red")

uw_analogy = Doodle(760, 250, "Doodle of a waiter's order pad. The waiter writes every change the table asks for: one more drink, swap the side, cancel a starter. At the end, the whole page goes to the kitchen at once. Each dish appears on the pad only once, however many times the table mentions it.",
                     "The waiter notes every change, then sends the whole page to the kitchen at once, one line per dish.")
uw_analogy.icon("menu", 60, 60, 1.8)
uw_analogy.note(450, 60, "+1 lemonade · swap fries → salad", "pen")
uw_analogy.note(450, 110, "cancel the soup", "pen")
uw_analogy.note(450, 170, "whole page to the kitchen, once", "green")
uw_analogy.note(450, 220, "each dish written once", "green")

uw_how = Doodle(760, 320, "A unit of work inside an ORM session. The identity map holds one object per row loaded in this request, so loading customer 42 twice returns the same object. The unit of work tracks new, changed and deleted objects. Calling save changes writes all of them in one transaction, in the right order, or none of them.",
                 "One object per row (identity map), all changes tracked, one transaction at the end (unit of work).")
uw_how.box(20, 30, 330, 200, None, "y", dash=True)
uw_how.head(185, 62, "identity map")
uw_how.text(185, 104, "Customer#42 → one object")
uw_how.text(185, 140, "Order#7 → one object")
uw_how.text(185, 186, "load twice = same object")
uw_how.box(410, 30, 330, 200, None, "blue", dash=True)
uw_how.head(575, 62, "unit of work")
uw_how.text(575, 104, "new: line 3")
uw_how.text(575, 140, "changed: order 7, credit")
uw_how.text(575, 176, "deleted: line 1")
uw_how.box(250, 260, 260, 50, "saveChanges(): one tx", "green", size=17)

UNIT_OF_WORK = dict(
    slug="unit-of-work",
    kicker="a.k.a. “the waiter's order pad”",
    tldr="A <b>unit of work</b> keeps a list of every object <b>created, changed or deleted</b> during one business operation, and writes them all in <b>one transaction</b> at the end. An <b>identity map</b> makes sure each row is loaded <b>once</b> per operation, so two parts of the code never hold two diverging copies of the same customer. Your ORM session (<code>DbContext</code>, <code>EntityManager</code>, <code>Session</code>) is both. Keep it <b>short-lived</b>: one per request.",
    chips=[("Family", "object-relational behaviour"), ("From", "Fowler, PoEAA (2002)"), ("In your ORM as", "DbContext, EntityManager, Session"), ("Lifetime", "one per request or command")],
    problem="""  <p class="lead">Saving each object by hand leads to <span class="hl-pink">half-saved changes</span> and <span class="hl-pink">duplicate copies</span> of the same row.</p>
  <ul>
    <li>Four saves in a row; the third fails, the first two stay.</li>
    <li>The same customer loaded twice; one change overwrites the other.</li>
    <li>Forgotten saves: an object changed but never written.</li>
  </ul>""",
    problem_figs=[uw_problem],
    analogy_side="the waiter's order pad",
    analogy="""  <p>A good <b>waiter</b> writes every change on the pad (another drink, swap the side, cancel the soup) and sends the <b>whole page</b> to the kitchen at once. Each dish appears <b>once</b> on the pad, however many times the table mentions it.</p>
  <ul>
    <li>The pad's change list is the <b>unit of work</b>.</li>
    <li>One line per dish is the <b>identity map</b>.</li>
    <li>Sending the page is the <b>commit</b>.</li>
  </ul>""",
    analogy_figs=[uw_analogy],
    map=[("Writing each change on the pad", "Change tracking of loaded objects"),
         ("Each dish once on the pad", "Identity map: one object per row"),
         ("Sending the page at once", "<code>saveChanges()</code> / <code>flush()</code> in one transaction"),
         ("A new pad for each table", "A new session per request"),
         ("A pad kept all night", "A long-lived session: stale and bloated")],
    how_side="track, de-duplicate, commit once",
    how="""  <p>Most of the time you <b>use</b> these patterns rather than write them. What matters is the <b>lifetime</b>: a session per request or per command, never shared between threads or kept for hours.</p>""",
    how_figs=[uw_how],
    steps=[("One session per operation", "Open a DbContext or EntityManager per request, command or job."),
           ("Load through it", "So the identity map can return the same object for the same row."),
           ("Change objects, don't call save on each", "The unit of work tracks what changed."),
           ("Commit once at the end", "<code>SaveChanges()</code> or <code>flush()</code> in one transaction."),
           ("Dispose it", "Don't reuse a session across requests or threads."),
           ("Write events in the same commit", "Outbox rows go into the same unit of work.")],
    vocab=[("Unit of work", "Tracks changes during a business transaction and writes them together."),
           ("Identity map", "Ensures each row is loaded into one object per unit of work."),
           ("Change tracking", "Detecting which loaded objects were modified."),
           ("Flush", "Writing pending changes to the database."),
           ("Scoped lifetime", "A dependency created per request in a DI container."),
           ("Detached entity", "An object that's no longer tracked by a session.")],
    code=dict(file="place-order.ts", note="one unit of work per command", src="""
// MikroORM shown; EF Core's DbContext and JPA's EntityManager work the same way
export async function handlePlaceOrder(cmd: PlaceOrderCommand, orm: MikroORM) {
  const em = orm.em.fork();                       // new unit of work + identity map
  const order    = await em.findOneOrFail(Order, cmd.orderId);
  const customer = await em.findOneOrFail(Customer, order.customerId);
  const again    = await em.findOneOrFail(Customer, order.customerId);
  console.assert(customer === again);             // identity map: same object

  customer.reserveCredit(order.total());          // tracked
  order.place(new Date());                        // tracked
  em.persist(new OutboxMessage(order.events));    // new
  await em.flush();                               // one transaction, all or nothing
}
"""),
    tools="tools: EF Core <code>DbContext</code>, JPA/Hibernate <code>EntityManager</code> and <code>Session</code>, SQLAlchemy <code>Session</code>, MikroORM <code>EntityManager</code>; request-scoped lifetimes in DI containers.",
    gains=["<b>All or nothing</b>: no half-saved operations.",
           "<b>One copy per row</b>: no diverging duplicates.",
           "<b>No forgotten saves</b>: changes are tracked.",
           "<b>Fewer round trips</b>: batched writes."],
    losses=["<b>Hidden writes</b>: it's not obvious what flush will do.",
            "<b>Memory</b> grows with tracked objects.",
            "<b>Stale data</b> in long-lived sessions.",
            "<b>Not thread-safe</b>."],
    baseline="Each line compares <b>saving each object by hand with separate loads</b> to <b>an ORM session used as a short-lived unit of work and identity map</b>.",
    ratings=[(3, 4, "Change objects, commit once."),
             (3, 3, "Neutral."),
             (2, 5, "All or nothing, one copy per row."),
             (3, 4, "New objects join the same commit without new save calls."),
             (3, 3, "Neutral; tests often use a real or in-memory session."),
             (3, 3, "Neutral."),
             (3, 4, "Batched writes and cached reads within a request."),
             (3, 4, "No manual save bookkeeping."),
             (3, 3, "Neutral.")],
    pitfalls=[("Long-lived sessions", "One DbContext for a whole desktop app or a batch of a million rows.", "one session per request or per batch chunk."),
              ("Sharing across threads", "A singleton DbContext in a web server.", "scoped lifetime per request."),
              ("Surprising flushes", "Loading a query triggers an automatic flush of half-made changes.", "make changes, then flush once, explicitly."),
              ("Saving per entity anyway", "<code>SaveChanges()</code> after every line.", "one commit at the end of the operation.")],
    use=["Any operation that changes several rows together.",
         "Code that loads the same entity from several places in one request.",
         "Choosing session lifetimes in a web app or job."],
    skip=["Bulk data loads (use the database's bulk tools, not tracked objects).",
          "Read-only queries (turn tracking off for speed)."],
    related=["<b>Active Record vs Data Mapper</b>", "<b>Lazy Loading</b>", "<b>Aggregate</b> (Vol. 7)", "<b>Transactional Outbox</b> (Vol. 1)"],
    quiz=[("What does a unit of work do?", "Tracks changes made during an operation and writes them all in one transaction."),
          ("What does an identity map guarantee?", "Each row is loaded into a single object per unit of work, so there are no diverging copies."),
          ("What's the right lifetime for an ORM session in a web app?", "One per request (scoped), never shared between requests or threads."),
          ("Why turn off tracking for read-only queries?", "Tracking costs memory and time and isn't needed when nothing will be saved.")],
    quiz_sit=[("A nightly import of 2 million products slows to a crawl and runs out of memory after an hour. It uses one DbContext for the whole run. What do you change?",
               "Process in chunks with a fresh context per chunk (say 1,000 rows), turn off tracking for reads, and for pure inserts use the database's bulk copy instead of tracked entities.")],
    try_it="In your app, find where the ORM session is created and how long it lives. Log the number of tracked entities at the end of one request and of one background job. If either is in the thousands, shorten the lifetime or turn off tracking for its reads.",
    then_now=dict(src="Fowler, PoEAA 2002", verdict="built-in",
                  then="Fowler described both patterns in detail, because in 2002 many teams wrote their own data layer and had to implement change tracking, commit ordering and identity maps themselves.",
                  now="Every Data Mapper ORM has them built in (Hibernate's Session, EF Core's DbContext, SQLAlchemy's Session). Nobody writes them now; the skill is choosing the session's lifetime and knowing when it flushes.",
                  take="Built in now: know they exist, and keep the session short."),
    remember="Write every change on <span class=\"hl\">one pad</span>, and send <span class=\"hl\">the whole page</span> at once.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Unit of Work”, “Identity Map”.",
             "Microsoft, “DbContext Lifetime, Configuration, and Initialization” (EF Core docs).",
             "SQLAlchemy documentation, “Session Basics”.",
             "Vlad Mihalcea, <i>High-Performance Java Persistence</i> (2016)."],
)

# ------------------------------------------------------------------ 08 Lazy Loading
ll_problem = Doodle(760, 270, "Doodle of the N plus one problem caused by lazy loading. A page lists fifty orders and shows each customer's name. The ORM loads the fifty orders in one query, then, as the template touches order.customer.name, runs one more query per order: fifty-one queries. In another place, the customer is touched after the session closed and the app throws a lazy-initialisation error.",
                    "50 orders, then one hidden query per order for its customer: 51 queries. Or an error after the session closes.")
ll_problem.box(20, 40, 200, 70, "1 query", "green", sub="50 orders")
for i in range(5):
    ll_problem.box(270 + i * 92, 40, 80, 70, "+1", "pink", stroke="red", sub="customer")
ll_problem.note(500, 140, "… × 50", "red")
ll_problem.box(160, 180, 440, 56, "LazyInitializationException", "pink", stroke="red", size=17)
ll_problem.note(380, 262, "touched after the session closed", "red")

ll_analogy = Doodle(760, 250, "Doodle of a hotel minibar versus a room-service menu. The minibar is lazy: items are there, and you pay when you take one, which is great for a snack but terrible if you need fifty sandwiches for a meeting. For a meeting you order everything at once from catering.",
                     "Fine to grab one snack from the minibar; for fifty sandwiches, order catering in one go.")
ll_analogy.box(20, 40, 340, 120, None, "y")
ll_analogy.head(190, 74, "minibar")
ll_analogy.text(190, 112, "one item when you want it")
ll_analogy.box(400, 40, 340, 120, None, "green")
ll_analogy.head(570, 74, "catering order")
ll_analogy.text(570, 112, "fifty sandwiches, one trip")
ll_analogy.note(190, 200, "lazy loading", "pen")
ll_analogy.note(570, 200, "eager loading / projection", "pen")

ll_how = Doodle(760, 320, "Loading data deliberately per use case. Lazy loading is turned off by default. The order list page uses a projection query that joins customer names and returns exactly the fields the page shows, in one query. The order detail use case explicitly includes the lines and the customer. Lazy proxies remain only where an association is rarely needed. A test counts queries.",
                 "Decide per use case: a projection for lists, explicit includes for details, lazy only for the rare path.")
ll_how.row([("list page", "projection: 1 query", "green"), ("detail page", "include lines", "blue"), ("rare path", "lazy is fine", "y")], x=20, y=40, h=90, gap=30, size=17, subsize=13)
ll_how.note(380, 180, "lazy loading off by default", "pen")
ll_how.box(180, 220, 400, 60, "test: “list page runs ≤ 2 queries”", "paper", size=16)

LAZY = dict(
    slug="lazy-loading",
    kicker="a.k.a. “the minibar, and why not to feed a meeting from it”",
    tldr="<b>Lazy loading</b> fetches related data only when code first touches it (<code>order.customer</code>), through a proxy. It feels free, which is the problem: in a list it causes the <b>N+1 query</b> problem, and after the session closes it <b>throws</b>. Today the advice is to <b>decide per use case</b>: projections for lists, explicit <b>eager includes</b> for details, and lazy only on rare paths. Many teams turn it <b>off by default</b>.",
    chips=[("Family", "object-relational behaviour"), ("From", "Fowler, PoEAA (2002)"), ("Famous failure", "the N+1 query problem"), ("Pairs with", "batch loading (Vol. 3), DTOs")],
    problem="""  <p class="lead">Lazy loading hides database calls behind property access, so the code <span class="hl-pink">looks cheap and isn't</span>.</p>
  <ul>
    <li>A list of 50 orders runs 51 queries.</li>
    <li>A template touches a relation after the session closed, and crashes.</li>
    <li>Performance depends on which fields a view happens to read.</li>
  </ul>""",
    problem_figs=[ll_problem],
    analogy_side="the minibar and the catering order",
    analogy="""  <p>A hotel <b>minibar</b> is lazy: everything is there, and you take one item when you want it. Great for a midnight snack; terrible for feeding a <b>meeting of fifty</b>, one trip each. For the meeting, you <b>order catering</b>: everything at once.</p>
  <ul>
    <li>The minibar is <b>lazy loading</b>.</li>
    <li>Fifty trips is <b>N+1</b>.</li>
    <li>Catering is <b>eager loading</b> or a <b>projection</b>.</li>
  </ul>""",
    analogy_figs=[ll_analogy],
    map=[("One snack from the minibar", "Touching <code>order.customer</code> once: one extra query"),
         ("Fifty trips to the minibar", "N+1 queries in a list"),
         ("Minibar locked after checkout", "Lazy loading after the session closed: an exception"),
         ("Catering for the meeting", "Eager loading or a projection query"),
         ("Deciding before the meeting", "Choosing the loading strategy per use case")],
    how_side="decide per use case",
    how="""  <p>A <b>projection</b> (selecting just the fields the screen needs into a DTO) is often better than loading entities at all for read screens. Keep entity loading for use cases that <b>change</b> things.</p>""",
    how_figs=[ll_how],
    steps=[("Turn lazy loading off by default", "Or at least know where it's on."),
           ("List pages: project", "Select only the needed fields with joins into a DTO, in one query."),
           ("Detail and write use cases: include", "Eager-load the aggregate's parts explicitly."),
           ("Lazy only on rare paths", "Associations needed in one case out of a hundred."),
           ("Keep the session open only inside the use case", "Not during view rendering (avoid open-session-in-view)."),
           ("Count queries in tests", "Fail a test when a page exceeds its query budget.")],
    vocab=[("Lazy loading", "Loading related data on first access, through a proxy."),
           ("Eager loading", "Loading related data up front with the main query (<code>Include</code>, <code>JOIN FETCH</code>)."),
           ("N+1 problem", "One query for a list plus one per item."),
           ("Proxy", "A stand-in object that loads the real data when touched."),
           ("Projection", "A query that selects specific fields into a shape for one screen."),
           ("Open session in view", "Keeping the ORM session open while rendering, which hides lazy queries.")],
    code=dict(file="orders-list.ts", note="a projection instead of lazy entities", src="""
// lazy: looks innocent, runs 1 + 50 queries
const orders = await em.find(Order, { status: "placed" }, { limit: 50 });
orders.map((o) => ({ id: o.id, customer: o.customer.name }));   // each .customer = a query

// projection: exactly what the page shows, one query
const rows = await db.selectFrom("orders as o")
  .innerJoin("customers as c", "c.id", "o.customer_id")
  .select(["o.id", "o.placed_at", "c.name as customer", "o.total_cents"])
  .where("o.status", "=", "placed").orderBy("o.placed_at", "desc").limit(50)
  .execute();

// detail use case: load the aggregate explicitly
const order = await em.findOneOrFail(Order, id, { populate: ["lines", "customer"] });
"""),
    tools="tools: ORM include/populate options (<code>Include</code> in EF Core, <code>JOIN FETCH</code> and entity graphs in JPA, <code>populate</code> in MikroORM), query builders for projections, DataLoader for GraphQL, query counters in tests (e.g. Hibernate statistics, Bullet for Rails).",
    gains=["<b>Predictable queries</b> per use case.",
           "<b>No N+1</b> surprises.",
           "<b>No closed-session errors</b>.",
           "<b>Faster list pages</b> with projections."],
    losses=["<b>More explicit code</b> for loading.",
            "<b>Over-fetching</b> if includes are too broad.",
            "<b>Several shapes</b> of the same data.",
            "<b>Lazy convenience lost</b> for prototypes."],
    baseline="Each line compares <b>lazy loading by default everywhere</b> to <b>explicit loading per use case, with projections for lists</b>.",
    ratings=[(4, 3, "Lazy is simpler to write; explicit is clearer to read."),
             (3, 3, "Neutral."),
             (3, 4, "No crashes from closed sessions."),
             (3, 3, "Neutral."),
             (3, 4, "Query budgets can be tested."),
             (3, 3, "Neutral."),
             (2, 5, "The point: one query instead of fifty-one."),
             (4, 3, "Includes and projections to write."),
             (3, 3, "Neutral.")],
    pitfalls=[("Lazy loading in loops", "A template or mapper touching a relation per row.", "projection or eager include for lists."),
              ("Open session in view", "Lazy loads keep working during rendering, invisibly.", "close the session at the end of the use case."),
              ("Include everything", "Every query eager-loads ten relations “to be safe”.", "include what the use case needs, no more."),
              ("No measurement", "N+1 found by customers, not tests.", "count queries in tests and log slow pages.")],
    use=["Deciding loading strategies in an ORM-based app.",
         "Slow list pages or GraphQL resolvers.",
         "Lazy-initialisation errors in production."],
    skip=["Prototypes where speed of writing beats speed of running.",
          "Rarely-used associations on single objects (lazy is fine there)."],
    related=["<b>Unit of Work &amp; Identity Map</b>", "<b>DTOs &amp; Remote Facade</b>", "<b>Batch Loading</b> (Vol. 3)", "<b>CQRS</b> (Vol. 1)"],
    quiz=[("What is lazy loading?", "Loading related data only when it is first accessed, through a proxy."),
          ("What's the N+1 problem?", "One query loads N items, then one more query runs per item for a related object."),
          ("What's usually best for list pages?", "A projection query that selects just the shown fields, with joins, into a DTO."),
          ("Why avoid open-session-in-view?", "It lets lazy queries run invisibly during rendering, hiding N+1 problems.")],
    quiz_sit=[("A GraphQL query for 100 orders with their customers and products takes 4 seconds; logs show 301 SQL queries. What do you do?",
               "Batch the related loads per request with DataLoader (or the ORM's batch fetching), so customers and products load in one query each, and add a test that fails if the query count for this request exceeds a small budget.")],
    try_it="Turn on SQL logging, open your app's busiest list page, and count the queries. If it's more than three, rewrite it as one projection query and compare the timings.",
    then_now=dict(src="Fowler, PoEAA 2002", verdict="built-in",
                  then="Fowler described four ways to implement lazy load (lazy initialisation, virtual proxy, value holder, ghost) for teams writing their own data layers, with a warning about “ripple loading”, his name for N+1.",
                  now="ORMs build lazy proxies in. Experience turned the warning into the main lesson: many teams disable lazy loading by default (EF Core has it off unless enabled), and projections, DataLoader and query budgets are standard.",
                  take="Built in now, and best used sparingly: load deliberately per use case."),
    remember="Grab <span class=\"hl\">one snack</span> from the minibar; order <span class=\"hl\">catering</span> for the meeting.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Lazy Load”.",
             "Microsoft, “Loading Related Data” (EF Core docs).",
             "Vlad Mihalcea, “The Open Session In View Anti-Pattern” (2016).",
             "GraphQL DataLoader (github.com/graphql/dataloader)."],
)

# ------------------------------------------------------------------ 09 Offline Locks & ETags
ol_problem = Doodle(760, 260, "Doodle of a lost update across two browser tabs. Support agent Sam opens order 7 at 10:00 and changes the address. Agent Priya opens the same order at 10:02 and adds a discount. Sam saves at 10:05; Priya saves at 10:08 with the old address still in her form. Sam's address change is silently lost and the parcel goes to the old address.",
                    "Sam and Priya edit the same order; Priya's later save silently overwrites Sam's new address.")
ol_problem.box(20, 30, 220, 70, "Sam 10:00", "blue", sub="changes address")
ol_problem.box(20, 140, 220, 70, "Priya 10:02", "y", sub="adds discount")
ol_problem.box(300, 30, 200, 70, "save 10:05", "green", sub="new address")
ol_problem.box(300, 140, 200, 70, "save 10:08", "pink", stroke="red", sub="old address!")
ol_problem.arrow(244, 65, 296, 65)
ol_problem.arrow(244, 175, 296, 175)
ol_problem.note(630, 120, "Sam's change: gone", "red")
ol_problem.note(380, 246, "no error, no warning", "red")

ol_analogy = Doodle(760, 250, "Doodle of a shared online document. When you try to save after someone else changed the same paragraph, the editor says: this was changed since you opened it, review the changes. For a booked meeting room, a different approach: you take the key for an hour, and others wait or come back later.",
                    "A shared doc warns “changed since you opened it”. A meeting room key lets one person in at a time.")
ol_analogy.box(20, 40, 340, 120, None, "green")
ol_analogy.head(190, 74, "shared document")
ol_analogy.text(190, 112, "“changed since you opened it”")
ol_analogy.box(400, 40, 340, 120, None, "y")
ol_analogy.head(570, 74, "meeting-room key")
ol_analogy.text(570, 112, "one person, for an hour")
ol_analogy.note(190, 200, "optimistic", "pen")
ol_analogy.note(570, 200, "pessimistic", "pen")

ol_how = Doodle(760, 320, "Optimistic offline lock over HTTP. GET order 7 returns the order with an ETag header containing version 12. The browser sends the edit with If-Match version 12. The server updates only if the version is still 12, and returns the new ETag 13. If someone saved in between, the version is 13 and the server answers 412 Precondition Failed; the client shows the changes and lets the user merge.",
                 "GET returns an ETag; PUT sends If-Match; a changed version means 412, never a silent overwrite.")
ol_how.box(20, 30, 200, 70, "browser", "paper", size=18)
ol_how.box(540, 30, 200, 70, "server", "blue", size=18)
ol_how.arrow(224, 50, 536, 50, label="GET → ETag: \"v12\"", lx=380, ly=40)
ol_how.arrow(224, 130, 536, 130, label="PUT, If-Match: \"v12\"", lx=380, ly=120)
ol_how.box(540, 170, 200, 60, "200 · ETag v13", "green", size=16)
ol_how.box(540, 246, 200, 60, "412 if now v13", "pink", stroke="red", size=16)
ol_how.note(250, 230, "UPDATE … WHERE version = 12", "pen")
ol_how.note(250, 270, "0 rows → someone saved first", "pen")

OFFLINE_LOCKS = dict(
    slug="offline-locks",
    kicker="a.k.a. “changed since you opened it”",
    tldr="A database transaction can't stay open while a person edits a form for ten minutes, so two people can <b>overwrite each other</b> without knowing. An <b>optimistic offline lock</b> saves a <b>version</b> with the data; a save succeeds only if the version is unchanged, otherwise the user sees a <b>conflict</b> instead of silently losing work. Over HTTP this is <b>ETag + If-Match → 412</b>. Use a <b>pessimistic</b> lock (a lease with an expiry) only where conflicts are costly and frequent.",
    chips=[("Family", "offline concurrency"), ("From", "Fowler, PoEAA (2002)"), ("Over HTTP", "ETag, If-Match, 412 Precondition Failed"), ("Pairs with", "optimistic locking (Vol. 3)")],
    problem="""  <p class="lead">When two people edit the same record over minutes, the second save <span class="hl-pink">silently erases</span> the first.</p>
  <ul>
    <li>Two agents edit one order; one agent's address change vanishes.</li>
    <li>A mobile app syncs an old copy over a newer one.</li>
    <li>No error, so nobody knows until the parcel goes astray.</li>
  </ul>""",
    problem_figs=[ol_problem],
    analogy_side="the shared document and the room key",
    analogy="""  <p>A shared online <b>document</b> warns you: “this paragraph was changed since you opened it”, and lets you review. A <b>meeting room</b> works differently: one person takes the key for an hour; others wait.</p>
  <ul>
    <li>The warning is an <b>optimistic</b> lock: check at save time.</li>
    <li>The key is a <b>pessimistic</b> lock: block others up front.</li>
  </ul>""",
    analogy_figs=[ol_analogy],
    map=[("“Changed since you opened it”", "Version mismatch → 409 / 412 conflict"),
         ("The version you opened", "An ETag or version number sent back on save"),
         ("Review the changes", "Showing the user the newer data to merge"),
         ("Taking the room key", "A pessimistic lease: “Sam is editing until 10:15”"),
         ("Key with a return time", "A lock that expires if Sam walks away")],
    how_side="versions, ETags and conflicts",
    how="""  <p>This is the same idea as optimistic locking in the database (Vol. 3), stretched over a whole <b>user session</b>: the version travels to the browser and back. Conflicts are rare in most apps, so optimistic is the default.</p>""",
    how_figs=[ol_how],
    steps=[("Add a version", "A column incremented on every update (or a timestamp, or a hash)."),
           ("Send it to the client", "As an ETag header or a field in the response."),
           ("Require it on save", "If-Match header or a version field; reject saves without one."),
           ("Update conditionally", "<code>UPDATE … WHERE id = ? AND version = ?</code>; zero rows means conflict."),
           ("Show the conflict", "412 or 409 with the current data; let the user merge or retry."),
           ("Pessimistic only where needed", "A lease with an owner and an expiry, released on save or timeout.")],
    vocab=[("Lost update", "A later save overwriting an earlier one without noticing."),
           ("Optimistic offline lock", "Check a version at save time; fail on conflict."),
           ("Pessimistic offline lock", "Mark the record as being edited so others can't."),
           ("ETag", "An HTTP header identifying a version of a resource."),
           ("If-Match", "A request header: only apply if the ETag still matches."),
           ("412 Precondition Failed", "The response when If-Match doesn't match.")],
    code=dict(file="orders.route.ts", note="ETag and If-Match on an edit endpoint", src="""
app.get("/orders/:id", async (req, res) => {
  const o = await orders.find(req.params.id);
  res.set("ETag", `"${o.version}"`).json(toDto(o));
});

app.put("/orders/:id", async (req, res) => {
  const ifMatch = req.get("If-Match");
  if (!ifMatch) return res.status(428).send("If-Match required");
  const expected = Number(ifMatch.replaceAll('"', ""));
  const updated = await db.updateTable("orders")
    .set({ ...fromDto(req.body), version: expected + 1 })
    .where("id", "=", req.params.id).where("version", "=", expected)
    .executeTakeFirst();
  if (Number(updated.numUpdatedRows) === 0) return res.status(412).json(await currentDto(req.params.id));
  res.set("ETag", `"${expected + 1}"`).sendStatus(204);
});
"""),
    tools="tools: ORM version columns (<code>@Version</code> in JPA, concurrency tokens in EF Core, Rails <code>lock_version</code>), HTTP ETag/If-Match support in frameworks and API gateways, merge UIs for conflicts.",
    gains=["<b>No silent lost updates</b>.",
           "<b>No long database locks</b>.",
           "<b>Standard HTTP</b> mechanism for clients.",
           "<b>Users see conflicts</b> and can fix them."],
    losses=["<b>Conflict handling UI</b> to build.",
            "<b>Version field</b> on every editable resource.",
            "<b>Retries</b> under heavy contention.",
            "<b>Pessimistic leases</b> need expiry and cleanup."],
    baseline="Each line compares <b>last-write-wins saves of long edits</b> to <b>versioned saves with ETags and conflict responses</b>.",
    ratings=[(3, 3, "A version to carry, but a clear rule."),
             (3, 3, "Neutral."),
             (2, 5, "The point: no silent overwrites."),
             (3, 3, "Neutral."),
             (3, 4, "Conflicts are a testable response, not a race."),
             (3, 3, "Neutral."),
             (3, 4, "No database locks held while people think."),
             (4, 3, "Version columns, headers and a conflict view."),
             (3, 4, "Many people can edit safely at once.")],
    pitfalls=[("Version not sent back", "The client never sends If-Match, so nothing is checked.", "require it: 428 Precondition Required without it."),
              ("Database transactions across user think time", "A transaction open while the form is on screen.", "short transactions; carry a version instead."),
              ("Pessimistic locks without expiry", "Sam goes home; the order stays locked all weekend.", "leases with an owner, an expiry and an admin override."),
              ("Unhelpful conflicts", "“Error 412” with no detail.", "return the current data and show what changed.")],
    use=["Records edited by several people or devices.",
         "APIs where clients read, edit and write back.",
         "Offline-capable or mobile apps that sync."],
    skip=["Append-only data (new rows, no edits).",
          "Single-user data where nobody else can edit it."],
    related=["<b>Optimistic Locking</b> (Vol. 3)", "<b>Unit of Work &amp; Identity Map</b>", "<b>Aggregate</b> (Vol. 7)", "<b>Offline-First Sync</b> (Vol. 2)"],
    quiz=[("What is a lost update?", "A later save overwriting an earlier one without noticing."),
          ("How does an optimistic offline lock work?", "A version travels with the data; a save succeeds only if the stored version is unchanged."),
          ("What do ETag and If-Match do in HTTP?", "ETag identifies the version; If-Match makes the server apply the change only if that version is still current, else 412."),
          ("When is a pessimistic lock worth it?", "When conflicts are frequent and costly to merge, with a lease that expires.")],
    quiz_sit=[("Warehouse staff on tablets keep complaining that stock counts “jump back”. Two tablets edit the same bin and the last sync wins. What do you change?",
               "Add a version per bin, send it with each sync, and reject stale updates with a conflict the tablet must resolve. Better still for counts, send deltas (“−3”) instead of absolute values so concurrent changes add up.")],
    try_it="Pick one edit screen in your app. Open it in two tabs, change different fields in each, and save both. If the first change disappears, add a version column, return it as an ETag, and reject mismatched saves with 412.",
    then_now=dict(src="Fowler, PoEAA 2002", verdict="core",
                  then="Fowler described optimistic, pessimistic, coarse-grained and implicit offline locks for web and rich-client apps where a business transaction spans several requests.",
                  now="Exactly the same problem, with more clients (tabs, phones, offline apps). HTTP's ETag and If-Match made the optimistic version a web standard, and ORMs add version columns with one annotation.",
                  take="Still core: every app where two people can edit the same thing needs it."),
    remember="If it <span class=\"hl\">changed since you opened it</span>, say so; never <span class=\"hl\">overwrite silently</span>.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Optimistic Offline Lock”, “Pessimistic Offline Lock”.",
             "RFC 9110, “HTTP Semantics” (2022), sections on ETag, If-Match and 412.",
             "Microsoft, “Handling Concurrency Conflicts” (EF Core docs).",
             "Zalando RESTful API Guidelines, “Optimistic locking”."],
)

# ------------------------------------------------------------------ 10 DTOs & Remote Facade
dt_problem = Doodle(760, 270, "Doodle of two API mistakes. Left: a chatty API where the mobile app calls get order, get customer, get address, then get each of twelve lines, fifteen round trips on a slow network. Right: the API returns the Customer entity directly as JSON, including the password hash and internal flags, and renaming a database column breaks the app.",
                    "Left: 15 small calls on a phone network. Right: entities as JSON, leaking a password hash.")
dt_problem.box(20, 30, 340, 160, None, "pink", stroke="red")
dt_problem.head(190, 62, "chatty API")
dt_problem.msgs(50, 90, 10, size=24)
dt_problem.text(190, 150, "15 round trips")
dt_problem.box(400, 30, 340, 160, None, "pink", stroke="red")
dt_problem.head(570, 62, "entity as JSON")
dt_problem.text(570, 104, "passwordHash: “…”")
dt_problem.text(570, 140, "column rename → app breaks")
dt_problem.note(380, 240, "too many calls, or the wrong shape", "red")

dt_analogy = Doodle(760, 250, "Doodle of a mail-order form. Instead of phoning the shop once per item to ask its price, size and stock, you fill in one order form with everything on it, and get back one confirmation with exactly what you need. The form is designed for customers, not a copy of the warehouse ledger.",
                     "One order form with everything, not one phone call per item, and not the warehouse ledger.")
dt_analogy.icon("phone", 40, 60, 1.6)
dt_analogy.note(170, 70, "× 12 calls", "red")
dt_analogy.arrow(240, 100, 330, 100)
dt_analogy.icon("receipt", 360, 50, 1.6)
dt_analogy.note(560, 70, "one form, one reply", "green")
dt_analogy.note(560, 120, "shaped for the customer", "green")
dt_analogy.note(560, 170, "not the warehouse ledger", "pen")

dt_how = Doodle(760, 320, "A remote facade with DTOs. The mobile app calls one coarse endpoint, GET order summary 7, and receives one DTO: order number, status, delivery address, line names and quantities, and totals. Inside, a facade calls the domain and repositories, then maps to the DTO. The DTO is versioned and documented separately from the domain classes.",
                 "One coarse call per screen or use case; a DTO shaped for it; mapping happens inside, behind the facade.")
dt_how.box(20, 100, 180, 80, "mobile app", "paper", size=17)
dt_how.arrow(204, 140, 266, 140, label="1 call", lx=235, ly=128)
dt_how.box(270, 70, 220, 140, None, "y")
dt_how.head(380, 104, "remote facade")
dt_how.text(380, 144, "GET /order-summary/7")
dt_how.text(380, 180, "maps → DTO")
dt_how.arrow(494, 140, 556, 140, both=True)
dt_how.box(560, 70, 180, 140, "domain", "blue", sub="entities, rules")
dt_how.box(170, 240, 420, 60, "OrderSummaryDto (versioned)", "green", size=16)

DTO = dict(
    slug="dto-remote-facade",
    kicker="a.k.a. “one order form, not twelve phone calls”",
    tldr="Across a network, every call costs. A <b>remote facade</b> offers <b>coarse-grained</b> operations (one call per screen or use case) on top of a fine-grained domain. A <b>DTO</b> (data transfer object) is the <b>shape</b> sent over the wire: just the fields the client needs, separate from your entities. You get fewer round trips, no leaked internals, and an API contract that can <b>stay stable</b> while the domain changes.",
    chips=[("Family", "distribution pattern"), ("From", "Fowler, PoEAA (2002)"), ("Today also", "BFF, GraphQL, OpenAPI-typed DTOs"), ("Pairs with", "open host service (Vol. 7), BFF")],
    problem="""  <p class="lead">Exposing fine-grained objects over a network leads to <span class="hl-pink">chatty APIs</span> or <span class="hl-pink">leaked internals</span>.</p>
  <ul>
    <li>A screen needs fifteen calls on a slow mobile network.</li>
    <li>Entities serialised straight to JSON leak hashes and internal flags.</li>
    <li>A database rename breaks the mobile app.</li>
  </ul>""",
    problem_figs=[dt_problem],
    analogy_side="the mail-order form",
    analogy="""  <p>You don't <b>phone the shop</b> once per item to ask its size, price and stock. You fill in <b>one order form</b> and get <b>one confirmation</b> with what you need. The form is designed for customers, not a photocopy of the <b>warehouse ledger</b>.</p>
  <ul>
    <li>The shop counter is the <b>remote facade</b>.</li>
    <li>The form and the confirmation are <b>DTOs</b>.</li>
  </ul>""",
    analogy_figs=[dt_analogy],
    map=[("A phone call per item", "A chatty, fine-grained remote API"),
         ("One order form", "One coarse call per use case"),
         ("The confirmation slip", "A response DTO shaped for the screen"),
         ("The warehouse ledger", "Your entities and tables, which stay inside"),
         ("A new form layout, same ledger", "A new API version, same domain")],
    how_side="coarse calls, shaped data",
    how="""  <p>Fowler designed these to cut <b>round trips</b> in the EJB era. Today the bigger reason is the <b>contract</b>: a DTO is your published language (Vol. 7), and keeping it separate from entities lets both change at their own pace. For many differently-shaped clients, a <b>BFF</b> or <b>GraphQL</b> lets each client shape its own DTOs.</p>""",
    how_figs=[dt_how],
    steps=[("Start from the screen or use case", "What does the client need in one go?"),
           ("Design the DTO for that", "Only those fields, named for the client, with no internal IDs or flags."),
           ("Offer one coarse operation", "<code>GET /order-summary/7</code>, <code>POST /checkout</code>."),
           ("Map inside the facade", "Domain → DTO in one place, tested."),
           ("Document and version it", "OpenAPI schema; additive changes, new versions for breaking ones."),
           ("Consider a BFF or GraphQL", "When several clients need very different shapes.")],
    vocab=[("DTO", "A plain object carrying data across a boundary, with no behaviour."),
           ("Remote facade", "A coarse-grained interface over fine-grained objects, for remote callers."),
           ("Chatty interface", "One that needs many small calls to do one job."),
           ("Over-posting / mass assignment", "Accepting fields in a request that clients shouldn't set."),
           ("BFF", "Backend for frontend: a server-side facade per client type."),
           ("Mapper", "Code that converts between domain objects and DTOs.")],
    code=dict(file="order-summary.ts", note="a DTO for one screen, mapped inside", src="""
// the contract: what the app needs, nothing more
export type OrderSummaryDto = {
  number: string; status: "placed" | "shipped" | "delivered";
  deliverTo: { name: string; street: string; city: string };
  lines: { name: string; qty: number; price: string }[];
  total: string;
};

app.get("/order-summary/:id", async (req, res) => {
  const order = await orders.get(orderId(req.params.id));
  const customer = await customers.get(order.customerId);
  res.json(toSummary(order, customer));   // never res.json(order)
});

const toSummary = (o: Order, c: Customer): OrderSummaryDto => ({
  number: o.number, status: o.status, deliverTo: c.deliveryAddress.toDto(c.name),
  lines: o.lines.map((l) => ({ name: l.productName, qty: l.qty.value, price: l.subtotal().format() })),
  total: o.total().format(),
});
"""),
    tools="tools: OpenAPI with generated client types, Zod or class-validator schemas for request DTOs, mapping helpers (or plain functions), BFF services, GraphQL with DataLoader, gRPC/Protobuf messages for service-to-service DTOs.",
    gains=["<b>Fewer round trips</b>.",
           "<b>No leaked internals</b> or over-posting.",
           "<b>Stable API</b> while the domain changes.",
           "<b>Clear contracts</b> for clients and docs."],
    losses=["<b>Mapping code</b> to write and test.",
            "<b>More types</b>: DTOs per use case.",
            "<b>Coarse calls</b> may over-fetch for some clients.",
            "<b>Duplication</b> between DTO and entity fields."],
    baseline="Each line compares <b>fine-grained APIs or entities serialised directly</b> to <b>a coarse remote facade returning use-case DTOs</b>.",
    ratings=[(3, 4, "One call and one shape per screen."),
             (3, 4, "DTOs named for what clients see."),
             (2, 4, "No mass assignment or leaked fields."),
             (2, 4, "Domain changes don't break clients."),
             (3, 4, "Mappers and contracts tested separately."),
             (2, 5, "Clients depend on DTOs, not entities."),
             (2, 4, "Far fewer round trips."),
             (4, 3, "DTOs and mappers to write."),
             (3, 4, "Client and server teams agree on a contract.")],
    pitfalls=[("Returning entities", "<code>res.json(customer)</code> leaks the password hash.", "always map to a DTO; never serialise entities."),
              ("Binding requests to entities", "Clients set <code>isAdmin</code> by adding a field.", "request DTOs with an allow-list of fields."),
              ("One DTO for everything", "A 60-field OrderDto used by every screen.", "DTOs per use case or per client (BFF)."),
              ("Generic CRUD over HTTP", "Every table exposed as fine-grained endpoints.", "design operations around use cases.")],
    use=["Any API crossing a network, especially to mobile or third parties.",
         "Screens that need data from several objects.",
         "Keeping an API stable while the domain changes."],
    skip=["In-process calls between modules (pass domain objects or plain values).",
          "Prototypes where the API and the model are deliberately the same."],
    related=["<b>Lazy Loading</b>", "<b>Adapter &amp; Facade</b>", "<b>Open Host Service &amp; Published Language</b> (Vol. 7)", "<b>Backend for Frontend</b> (Ana, vol. 4)", "<b>API Gateway</b> (Vol. 1)"],
    quiz=[("What's a remote facade?", "A coarse-grained interface over fine-grained objects, so remote clients need few calls."),
          ("What's a DTO?", "A plain data object shaped for transfer across a boundary, with no behaviour."),
          ("Why not return entities as JSON?", "They leak internals, invite mass assignment, and tie clients to the database shape."),
          ("When do a BFF or GraphQL help?", "When different clients need very different shapes of the same data.")],
    quiz_sit=[("A security review finds that <code>PATCH /users/:id</code> accepts any JSON and saves it into the User entity; a tester made themselves an admin. What do you change?",
               "Accept a request DTO with an explicit allow-list of editable fields (name, phone), validate it, map it onto the entity through domain methods, and never bind request bodies to entities directly. Add a test that sending <code>isAdmin</code> has no effect.")],
    try_it="Find one endpoint that returns an ORM entity directly. Write a DTO type with only what the client uses, a mapper function with a test, and compare the JSON size before and after.",
    then_now=dict(src="Fowler, PoEAA 2002", verdict="rethought",
                  then="Fowler introduced DTOs and remote facades mainly for performance: remote calls in EJB and CORBA were expensive, so you batched data into serialisable objects and offered coarse operations.",
                  now="The performance reason still applies on mobile networks, but the main reason now is the <b>contract</b>: DTOs as OpenAPI or Protobuf schemas, separate from entities, safe against over-posting. BFFs and GraphQL let each client shape its own DTOs.",
                  take="Rethought: same patterns, now mostly for stable, safe contracts rather than raw speed."),
    remember="Send <span class=\"hl\">one order form</span>, never the <span class=\"hl\">warehouse ledger</span>.",
    sources=["Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Data Transfer Object”, “Remote Facade”.",
             "Martin Fowler, “LocalDTO” (bliki, 2004).",
             "OWASP API Security Top 10 (2023), “Broken Object Property Level Authorization”.",
             "Sam Newman, “Backends For Frontends” (2015)."],
)

NOTES = [ACTIVE_RECORD, UNIT_OF_WORK, LAZY, OFFLINE_LOCKS, DTO]
