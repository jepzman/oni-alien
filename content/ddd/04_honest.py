# Vol. 7 · Domain-Driven Design · Keeping it honest: Specification, Make Illegal States Unrepresentable,
# Anemic Domain Model.

# ------------------------------------------------------------------ 16 Specification
sp_problem = Doodle(760, 260, "Doodle of one business rule copied in three forms. The rule for a customer who qualifies for free delivery, a VIP or a basket over fifty euros outside the remote zones, is written once as an if-statement in checkout, once as a SQL WHERE clause in the marketing export, and once in the front end. Marketing changes the threshold to sixty euros; only one of the three is updated.",
                    "One rule (free delivery) written three times: checkout, a SQL export and the front end. Only one gets updated.")
sp_problem.box(20, 40, 220, 90, "checkout", "paper", sub="if (vip || total>50)…")
sp_problem.box(270, 40, 220, 90, "export SQL", "paper", sub="WHERE total > 50…")
sp_problem.box(520, 40, 220, 90, "front end", "paper", sub="total > 50 && …")
sp_problem.note(380, 180, "threshold changed to €60…", "pen")
sp_problem.note(380, 220, "…in one of the three places", "red")

sp_analogy = Doodle(760, 250, "Doodle of a recipe's dietary labels. Vegan, gluten-free and nut-free are each defined once by the kitchen. The same labels are used to check a dish, to filter the menu, and to plan what to cook, and they can be combined: vegan and gluten-free. Change what gluten-free means and every use follows.",
                    "Menu labels like vegan or gluten-free: defined once, used to check, filter and plan, and combinable.")
sp_analogy.box(20, 50, 200, 70, "vegan", "green", size=18)
sp_analogy.box(280, 50, 200, 70, "gluten-free", "y", size=18)
sp_analogy.box(540, 50, 200, 70, "nut-free", "blue", size=18)
sp_analogy.note(380, 160, "check a dish · filter the menu · plan a meal", "pen")
sp_analogy.note(380, 210, "vegan AND gluten-free: combine labels", "green")

sp_how = Doodle(760, 320, "A specification for free delivery. It is built from smaller named rules: IsVip, BasketOver of sixty euros and NotInRemoteZone, combined with or and and. The same specification can check one basket in memory with isSatisfiedBy, and can produce a database filter for the marketing export. Each small rule is tested alone.",
                 "Small named rules, combined with and / or; one definition used to check in memory and to filter queries.")
sp_how.box(20, 30, 200, 60, "IsVip", "y", size=17)
sp_how.box(20, 110, 200, 60, "BasketOver(€60)", "y", size=17)
sp_how.box(20, 190, 200, 60, "NotRemoteZone", "y", size=17)
sp_how.box(290, 90, 200, 110, "FreeDelivery", "green", sub="(vip OR over) AND zone")
for y in (60, 140, 220):
    sp_how.arrow(224, y, 286, 145)
sp_how.box(560, 50, 180, 60, "isSatisfiedBy()", "paper", size=16)
sp_how.box(560, 170, 180, 60, "toQuery()", "paper", size=16)
sp_how.arrow(494, 130, 556, 80)
sp_how.arrow(494, 160, 556, 200)
sp_how.note(380, 296, "one rule: check a basket, or filter a table", "pen")

SPECIFICATION = dict(
    slug="specification",
    kicker="a.k.a. “the dietary label on the menu”",
    tldr="Turn an important <b>yes/no business rule</b> (“qualifies for free delivery”, “overdue invoice”) into a <b>named object or function</b> you can <b>test</b>, <b>combine</b> with and/or/not, and <b>reuse</b>: to check one object, to filter a query, or to describe what to build. The rule is written <b>once</b>. Today a plain, well-named <b>predicate function</b> is often enough.",
    chips=[("Family", "supple design"), ("From", "Evans &amp; Fowler (1997); Evans (2003), ch. 9"), ("Today", "named predicates, expression trees"), ("Pairs with", "value object, repository")],
    problem="""  <p class="lead">An important rule written as scattered conditions gets <span class="hl-pink">copied and drifts</span>: each copy slightly different.</p>
  <ul>
    <li>The same rule lives in checkout, a SQL export and the front end.</li>
    <li>A change of threshold is applied in one place only.</li>
    <li>Nobody can say exactly what “qualifies” means.</li>
  </ul>""",
    problem_figs=[sp_problem],
    analogy_side="the menu labels",
    analogy="""  <p>A kitchen defines <b>“vegan”</b>, <b>“gluten-free”</b> and <b>“nut-free”</b> once. The same labels are used to <b>check</b> a dish, to <b>filter</b> the menu for a guest and to <b>plan</b> a meal, and they <b>combine</b>: “vegan and gluten-free”. If gluten-free changes meaning, every use follows.</p>
  <ul>
    <li>Each label is a <b>specification</b>.</li>
    <li>Combining labels is <b>and / or / not</b>.</li>
    <li>Check, filter and plan are the three <b>uses</b>.</li>
  </ul>""",
    analogy_figs=[sp_analogy],
    map=[("A label: “gluten-free”", "A specification: <code>NotInRemoteZone</code>"),
         ("Check one dish", "<code>spec.isSatisfiedBy(basket)</code>"),
         ("Filter the menu", "<code>spec.toQuery()</code> → a WHERE clause"),
         ("“Vegan and gluten-free”", "<code>isVip.or(over60).and(notRemote)</code>"),
         ("Defined once by the kitchen", "One definition, many uses")],
    how_side="named rules you can combine",
    how="""  <p>Use it for <b>important</b> rules that appear in more than one place or need combining. For a one-off condition, a well-named function is the specification, and that's fine. Avoid deep class hierarchies of specifications: they were the 2003 way, and they're hard to read.</p>""",
    how_figs=[sp_how],
    steps=[("Find a rule that repeats", "The same condition in code, SQL or the front end, or a rule people argue about."),
           ("Name it in the domain's words", "<code>QualifiesForFreeDelivery</code>, <code>IsOverdue</code>."),
           ("Write it once", "As a predicate function or a small object with <code>isSatisfiedBy</code>."),
           ("Compose from smaller rules", "and / or / not, each part named and tested."),
           ("Reuse for queries if needed", "Translate to a query filter (expression tree, query builder) instead of duplicating it in SQL."),
           ("Test with examples", "A table of baskets and expected yes/no, written with the business.")],
    vocab=[("Specification", "An object or function that says whether something satisfies a business rule."),
           ("Predicate", "A function that returns true or false."),
           ("Composite specification", "Specifications combined with and, or and not."),
           ("isSatisfiedBy", "The classic method name for checking one candidate."),
           ("Expression tree", "Code as data, which an ORM can translate into SQL (C# LINQ)."),
           ("Selection / validation / construction", "Evans's three uses: filter, check, and describe what to create.")],
    code=dict(file="free-delivery.ts", note="specification as small composable predicates", src="""
type Spec<T> = { isSatisfiedBy(c: T): boolean };
const spec = <T>(f: (c: T) => boolean): Spec<T> => ({ isSatisfiedBy: f });
const and = <T>(...s: Spec<T>[]) => spec<T>((c) => s.every((x) => x.isSatisfiedBy(c)));
const or  = <T>(...s: Spec<T>[]) => spec<T>((c) => s.some((x) => x.isSatisfiedBy(c)));

const isVip          = spec<Basket>((b) => b.customer.tier === "vip");
const over           = (m: Money) => spec<Basket>((b) => b.total().cents >= m.cents);
const notRemoteZone  = spec<Basket>((b) => !REMOTE_POSTCODES.has(b.address.postcode));

export const qualifiesForFreeDelivery = and(or(isVip, over(Money.eur(60))), notRemoteZone);

qualifiesForFreeDelivery.isSatisfiedBy(basket);   // true / false, tested with a table of examples
"""),
    tools="tools: plain predicate functions, Ardalis.Specification and LINQ expression trees in .NET, Spring Data JPA <code>Specification</code>, query builders (Kysely, jOOQ) to turn a rule into a WHERE clause.",
    gains=["<b>A rule written once</b>, used everywhere.",
           "<b>Readable</b>: named in business terms.",
           "<b>Composable</b> from small tested parts.",
           "<b>Testable</b> with a table of examples."],
    losses=["<b>Extra abstraction</b> for simple conditions.",
            "<b>Query translation</b> is hard outside .NET and JPA.",
            "<b>Class hierarchies</b> of specs get unreadable.",
            "<b>Performance</b>: in-memory checks can't replace indexed queries."],
    baseline="Each line compares <b>a business rule written as scattered conditions</b> to <b>one named, composable specification</b>.",
    ratings=[(3, 3, "Clearer rule, one more concept."),
             (2, 5, "The rule has a business name."),
             (2, 4, "One definition: no drifting copies."),
             (2, 4, "Change the threshold in one place."),
             (3, 5, "Test the rule with an example table."),
             (3, 4, "Callers depend on the rule's name, not its details."),
             (3, 3, "Fine in memory; queries need translation."),
             (4, 3, "Small helpers or a library."),
             (3, 3, "Neutral.")],
    pitfalls=[("Specs for everything", "<code>IsNotNull</code> and <code>IsPositive</code> specifications.", "only for important, repeated or combined business rules."),
              ("Deep class hierarchies", "<code>AndSpecification&lt;OrSpecification&lt;…&gt;&gt;</code> nobody can read.", "small functions and a couple of combinators."),
              ("Duplicating it in SQL anyway", "The spec is used in code, the export still has its own WHERE.", "translate the spec to a query, or generate the export from it."),
              ("Filtering in memory", "Load 2 million customers to apply a spec.", "use the query form for selection; in-memory only for single checks.")],
    use=["An important yes/no rule appears in several places.",
         "Rules that combine (eligible AND not blocked OR override).",
         "Business people argue about what a rule means: name it and test it."],
    skip=["A condition used once: a well-named function or variable is enough.",
          "Performance-critical selection where a hand-tuned query is needed."],
    related=["<b>Value Object</b>", "<b>Repository</b>", "<b>Make Illegal States Unrepresentable</b>", "<b>Property-Based Testing</b> (Vol. 4)"],
    quiz=[("What is a specification?", "A named, testable business rule that says whether a candidate satisfies it, and can be combined with others."),
          ("Name Evans's three uses of a specification.", "Validation (check one object), selection (filter a collection or query) and construction (describe what to build)."),
          ("What's the simplest modern form?", "A well-named predicate function, with small and/or helpers when needed."),
          ("Why not apply a specification to every row in memory?", "Selection over large data needs an indexed database query; translate the spec to a filter instead.")],
    quiz_sit=[("Marketing's “eligible for the loyalty bonus” count never matches what checkout gives. The rule lives in a Java method and a 40-line SQL view written separately. What do you do?",
               "Make the rule one specification with a business name and an example table agreed with marketing, then generate the query from it (or have the export call the same code), and add a test that runs both forms on the same sample data.")],
    try_it="Find one business condition written in two places (code and SQL, or back end and front end). Write it once as a named predicate built from two or three smaller ones, write a table of six examples, and replace one of the copies.",
    then_now=dict(src="Evans &amp; Fowler, 1997; Evans, 2003", verdict="rethought",
                  then="Specifications were objects with <code>isSatisfiedBy</code>, combined through composite classes, and used for validation, selection and construction. In Java in 2003 this meant a fair amount of class machinery.",
                  now="First-class functions made a specification just a named predicate. In .NET, LINQ expression trees let one spec run in memory and as SQL. The heavy class-hierarchy version is mostly gone; the idea of naming and composing important rules is alive.",
                  take="Rethought: keep the idea, write it as small named predicates."),
    remember="Define <span class=\"hl\">“gluten-free”</span> once; then check, filter and plan with the <span class=\"hl\">same label</span>.",
    sources=["Eric Evans &amp; Martin Fowler, “Specifications” (1997).",
             "Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 9.",
             "Ardalis.Specification documentation (specification.ardalis.com).",
             "Spring Data JPA reference, “Specifications”."],
)

# ------------------------------------------------------------------ 17 Make Illegal States Unrepresentable
is_problem = Doodle(760, 270, "Doodle of a parcel class where impossible combinations are allowed. It has status, trackingNumber, deliveredAt and failureReason, all optional. The code creates a parcel that is delivered but has no delivery date, one that is pending but has a tracking number, and one that failed with no reason. Every function checks for nulls defensively, and some checks are missing.",
                    "Everything optional: “delivered” with no date, “pending” with a tracking number, “failed” with no reason.")
is_problem.table(20, 30, "Parcel", ["status: string", "trackingNo?: string", "deliveredAt?: Date", "failureReason?: string"], w=280, fill="pink", stroke="red")
is_problem.note(530, 60, "delivered, deliveredAt = null", "red")
is_problem.note(530, 110, "pending, but has a tracking no.", "red")
is_problem.note(530, 160, "failed, no reason", "red")
is_problem.note(380, 248, "if (p.deliveredAt != null && …) everywhere", "pen")

is_analogy = Doodle(760, 250, "Doodle of a well-designed form. A paper form with tick boxes lets you tick both married and single. A good form has one question with exactly one choice, and only asks for the spouse's name if you chose married. Wrong combinations can't even be filled in.",
                     "A good form can't be filled in wrongly: pick one status, and the spouse field only appears for “married”.")
is_analogy.box(20, 40, 320, 140, None, "pink", stroke="red")
is_analogy.head(180, 72, "bad form")
is_analogy.text(180, 112, "☑ married  ☑ single")
is_analogy.text(180, 150, "spouse: ______ (always)")
is_analogy.box(420, 40, 320, 140, None, "green")
is_analogy.head(580, 72, "good form")
is_analogy.text(580, 112, "◉ married  ○ single")
is_analogy.text(580, 150, "spouse: only if married")
is_analogy.note(380, 222, "wrong combinations can't be written down", "green")

is_how = Doodle(760, 320, "The parcel modelled as a union of states. Pending has no tracking number. InTransit has a tracking number. Delivered has a tracking number and a delivery date. Failed has a tracking number and a reason. Each state carries exactly the fields that make sense. Transition functions take one state and return the next: ship takes a Pending and returns InTransit. The compiler stops code from reading a delivery date from a parcel that isn't Delivered.",
                 "One type per state, each with exactly its own fields; functions move from one state to the next.")
is_how.row([("Pending", "id", "paper"), ("InTransit", "+ trackingNo", "blue"), ("Delivered", "+ deliveredAt", "green"), ("Failed", "+ reason", "pink")], x=14, y=40, h=90, gap=40, size=17, subsize=13)
is_how.arrow(178, 85, 210, 85, label="ship()", lx=194, ly=150)
is_how.arrow(372, 85, 404, 85, label="deliver()", lx=388, ly=150)
is_how.arrow(372, 110, 598, 110, dash=True, curve=(486, 200), label="fail()", lx=486, ly=176)
is_how.note(380, 240, "parcel.deliveredAt only exists on Delivered", "green")
is_how.note(380, 280, "the compiler rejects impossible combinations", "pen")

ILLEGAL_STATES = dict(
    slug="illegal-states",
    kicker="a.k.a. “a form that can't be filled in wrongly”",
    tldr="Design your types so that <b>invalid combinations can't be built</b>. Instead of one class with many optional fields and a status string, use <b>one type per state</b> (a union), each with <b>exactly</b> the fields that make sense: a <code>Delivered</code> parcel always has a delivery date; a <code>Pending</code> one never has a tracking number. Parse input into these types <b>once at the edge</b>, and the compiler <b>enforces the rules</b> everywhere else.",
    chips=[("Family", "modelling with types"), ("Coined by", "Yaron Minsky (2011)"), ("Popular from", "Wlaschin (2018), “Parse, don't validate” (2019)"), ("Pairs with", "value object, aggregate")],
    problem="""  <p class="lead">One class with many <span class="hl-pink">optional fields and a status string</span> allows combinations the business says are impossible, so every function must check for them.</p>
  <ul>
    <li>A parcel is “delivered” but has no delivery date.</li>
    <li>A “pending” parcel already has a tracking number.</li>
    <li>Null checks everywhere, and the one that's missing causes the bug.</li>
  </ul>""",
    problem_figs=[is_problem],
    analogy_side="the well-designed form",
    analogy="""  <p>A badly designed paper form lets you tick both <b>“married”</b> and <b>“single”</b>, and always asks for a spouse's name. A good one has <b>one</b> choice, and only shows the spouse field if you picked “married”. Wrong answers <b>can't be written down</b>, so nobody has to check for them later.</p>
  <ul>
    <li>One choice: a <b>union</b> of states.</li>
    <li>The spouse field only with “married”: <b>state-specific fields</b>.</li>
    <li>No checking later: the <b>type system</b> did it.</li>
  </ul>""",
    analogy_figs=[is_analogy],
    map=[("Exactly one tick box", "A union type: <code>Pending | InTransit | Delivered | Failed</code>"),
         ("Spouse field only if married", "<code>deliveredAt</code> exists only on <code>Delivered</code>"),
         ("Can't tick both", "The compiler rejects impossible combinations"),
         ("Checked when the form is handed in", "Parse input into types once, at the edge"),
         ("No re-checking later", "Functions receive types that are already valid")],
    how_side="types that match the business's states",
    how="""  <p>This is the type-level version of value objects and aggregates: the same goal, <b>impossible to break the rules</b>, enforced by the compiler instead of runtime checks. It works best in languages with union types and pattern matching: TypeScript, Kotlin, Swift, Rust, F#, Scala, and Java 21 sealed types.</p>""",
    how_figs=[is_how],
    steps=[("List the states", "With the experts: what states can this thing be in, and what's always true in each?"),
           ("One type per state", "Each with exactly the fields that exist in that state, none optional by accident."),
           ("A union of them", "<code>type Parcel = Pending | InTransit | Delivered | Failed</code>."),
           ("Transitions as functions", "<code>ship(p: Pending): InTransit</code>. You can't ship a delivered parcel."),
           ("Parse at the edge", "Turn JSON or rows into these types once, rejecting what doesn't fit."),
           ("Match exhaustively", "Handle every state with a switch the compiler checks is complete.")],
    vocab=[("Union type", "A type that is exactly one of several alternatives (sum type, sealed class)."),
           ("Discriminator", "A field like <code>kind</code> that tells which alternative it is."),
           ("Exhaustive matching", "The compiler checks every alternative is handled."),
           ("Parse, don't validate", "Turn raw input into a precise type once, instead of re-checking it everywhere."),
           ("Smart constructor", "A function that only builds a value if it's valid."),
           ("State machine", "The allowed states and transitions between them.")],
    code=dict(file="parcel.ts", note="one type per state", src="""
type Pending   = { kind: "pending";    id: ParcelId };
type InTransit = { kind: "in-transit"; id: ParcelId; trackingNo: TrackingNo };
type Delivered = { kind: "delivered";  id: ParcelId; trackingNo: TrackingNo; deliveredAt: Date };
type Failed    = { kind: "failed";     id: ParcelId; trackingNo: TrackingNo; reason: FailureReason };
export type Parcel = Pending | InTransit | Delivered | Failed;

export const ship    = (p: Pending, t: TrackingNo): InTransit => ({ kind: "in-transit", id: p.id, trackingNo: t });
export const deliver = (p: InTransit, at: Date): Delivered => ({ ...p, kind: "delivered", deliveredAt: at });

export function label(p: Parcel): string {
  switch (p.kind) {                                   // the compiler checks all four are handled
    case "pending":    return "Waiting for pickup";
    case "in-transit": return `On its way (${p.trackingNo})`;
    case "delivered":  return `Delivered ${p.deliveredAt.toDateString()}`;  // always there
    case "failed":     return `Failed: ${p.reason}`;
  }
}
"""),
    tools="tools: TypeScript discriminated unions with Zod or Valibot to parse at the edge, Kotlin and Java sealed classes, Rust and Swift enums with data, F# and Scala ADTs, XState for state machines.",
    gains=["<b>Bugs become compile errors</b>.",
           "<b>Fewer null checks</b> and defensive code.",
           "<b>Types document the rules</b>: read the type, know the states.",
           "<b>Safe refactoring</b>: add a state, the compiler lists every place to update."],
    losses=["<b>Mapping to tables</b> and JSON takes work.",
            "<b>Unfamiliar</b> to teams used to classes with setters.",
            "<b>Weaker in languages</b> without union types.",
            "<b>Can over-engineer</b> simple data."],
    baseline="Each line compares <b>one class with optional fields and a status string</b> to <b>a union of state types that rules out impossible combinations</b>.",
    ratings=[(3, 4, "Read the type to know the states."),
             (3, 5, "States named exactly as the business names them."),
             (2, 5, "The point: invalid combinations can't be built."),
             (3, 4, "Add a state; the compiler finds every place to update."),
             (3, 4, "Fewer cases to test: impossible ones can't happen."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "More types, fewer checks."),
             (3, 4, "Rules enforced by the compiler, not by memory.")],
    pitfalls=[("Optional fields “just in case”", "<code>deliveredAt?</code> on every parcel.", "put each field only on the states where it exists."),
              ("Validating instead of parsing", "Check JSON, then keep passing the raw object around.", "parse into the precise type once; pass that type inward."),
              ("Non-exhaustive switches", "A new state is added and silently falls into <code>default</code>.", "no default case; let the compiler require every state."),
              ("Types for trivial data", "A union for a field that has no rules.", "use it where wrong combinations are real bugs.")],
    use=["Things with clear states and different data in each (orders, parcels, payments).",
         "Bugs caused by impossible combinations or missing null checks.",
         "Languages with union types or sealed classes."],
    skip=["Simple data with no states or rules.",
          "Teams and languages where it would fight every tool you use."],
    related=["<b>Value Object</b>", "<b>Aggregate</b>", "<b>State Machines</b> (Vol. 2)", "<b>Validate at the Boundary</b> (Vol. 5)"],
    quiz=[("What does “make illegal states unrepresentable” mean?", "Design types so invalid combinations of data can't be constructed at all."),
          ("What's a union (sum) type?", "A type that is exactly one of several alternatives, each with its own fields."),
          ("What does “parse, don't validate” mean?", "Turn raw input into a precise type once at the edge, instead of checking it and passing raw data around."),
          ("Why avoid a default case in a switch over states?", "So the compiler forces you to handle any new state you add.")],
    quiz_sit=[("A payment class has <code>status</code>, <code>refundedAt?</code>, <code>failureCode?</code> and <code>capturedAmount?</code>. Last month a refund was issued on a payment that had failed. How would you redesign it?",
               "Model a union: Authorised, Captured (with amount), Failed (with code), Refunded (with date and amount). Make <code>refund</code> accept only a Captured payment, so refunding a failed one doesn't compile, and parse stored rows into these types at the repository.")],
    try_it="Find a class in your code with a status field and several optional fields. Write its states as a union of types, each with only its own fields, and one transition function. Count how many null checks disappear.",
    then_now=dict(src="Minsky, 2011; Wlaschin, 2018 (after Evans)", verdict="grown",
                  then="In 2003 the DDD way to protect rules was runtime checks: constructors that validate, methods that throw, invariants asserted in aggregates. Languages like Java had no practical union types.",
                  now="Mainstream languages gained union types and pattern matching (TypeScript, Kotlin, Swift, Rust, Java 21). Wlaschin's <i>Domain Modeling Made Functional</i> showed DDD done with types, and “parse, don't validate” spread widely. The compiler now does part of the aggregate's job.",
                  take="A modern addition that makes the old goals cheaper to reach. Use it wherever your language allows."),
    remember="Design the form so it <span class=\"hl\">can't be filled in wrongly</span>, and nobody has to <span class=\"hl\">check it later</span>.",
    sources=["Yaron Minsky, “Effective ML” (talk, 2010) and “Effective ML Revisited” (Jane Street blog, 2011).",
             "Scott Wlaschin, <i>Domain Modeling Made Functional</i> (2018).",
             "Alexis King, “Parse, don't validate” (2019).",
             "TypeScript Handbook, “Narrowing: discriminated unions”."],
)

# ------------------------------------------------------------------ 18 Anemic Domain Model
an_problem = Doodle(760, 260, "Doodle of an anemic model in a complex domain. The Order class has only getters and setters. Its rules are spread across OrderService, PricingHelper, CheckoutManager and a validator. Each sets fields on the order directly. A new rule about cancelling must be added in four places, and one forgets, so a shipped order gets cancelled.",
                    "Order is just getters and setters; its rules live in four services, and one of them forgets a rule.")
an_problem.table(270, 20, "Order", ["getStatus / setStatus", "getTotal / setTotal", "getLines / setLines"], w=220, fill="paper")
for i, t in enumerate(["OrderService", "PricingHelper", "CheckoutManager", "Validator"]):
    x = 20 + i * 185
    an_problem.box(x, 170, 165, 50, t, "paper", size=14)
    an_problem.arrow(x + 82, 166, 380, 128, dash=True)
an_problem.note(380, 248, "shipped order cancelled: one service skipped the rule", "red")

an_analogy = Doodle(760, 250, "Doodle of two kinds of car. A complex car has its safety rules built in: it won't shift into reverse at speed, and the airbag decides when to fire. A simple garden wheelbarrow has no rules and needs none; the person pushing it decides everything. Building a wheelbarrow with a computer would be silly; so would a car without one.",
                     "A car has its rules built in; a wheelbarrow needs none. Match the build to the job.")
an_analogy.box(20, 40, 340, 110, None, "green")
an_analogy.head(190, 74, "car")
an_analogy.text(190, 110, "rules built in: no reverse at speed")
an_analogy.box(400, 40, 340, 110, None, "y")
an_analogy.head(570, 74, "wheelbarrow")
an_analogy.text(570, 110, "no rules, none needed")
an_analogy.note(190, 190, "complex domain → rich model", "pen")
an_analogy.note(570, 190, "simple CRUD → plain data is fine", "pen")

an_how = Doodle(760, 320, "Two healthy options. In the core domain, the Order has behaviour: methods like cancel, which checks the rule that shipped orders can't be cancelled, and the application service just calls it. In a simple supporting area, like an admin screen for store opening hours, plain data records with validation at the edge and a transaction script are fine. The smell is plain data in a complex domain, with rules scattered across services.",
                 "Core domain: behaviour on the objects. Simple areas: plain data and scripts are fine. The smell is the mix.")
an_how.box(20, 30, 340, 150, None, "green")
an_how.head(190, 64, "core: rich model")
an_how.text(190, 104, "order.cancel()")
an_how.text(190, 140, "rule lives on Order")
an_how.box(400, 30, 340, 150, None, "y")
an_how.head(570, 64, "CRUD: plain data")
an_how.text(570, 104, "OpeningHours record")
an_how.text(570, 140, "validate at the edge")
an_how.box(160, 220, 440, 64, "smell: complex rules + plain data", "pink", stroke="red", size=17)

ANEMIC = dict(
    slug="anemic-domain-model",
    kicker="a.k.a. “a car with no brakes, or a wheelbarrow with a computer”",
    tldr="An <b>anemic domain model</b> has objects with data and getters/setters, and <b>all the rules in services</b> around them. Fowler called it an <b>anti-pattern</b> in 2003, and in a <b>complex core domain</b> it still is: rules scatter, get copied and get skipped. But in <b>simple CRUD</b> and supporting areas, plain data with a transaction script is <b>fine</b>, and functional code separates data and functions on purpose. The smell is <b>complex rules on plain data</b>.",
    chips=[("Family", "anti-pattern (in the right place)"), ("Named by", "Martin Fowler (2003)"), ("Fine for", "CRUD, supporting subdomains"), ("Fix with", "behaviour on entities, value objects")],
    problem="""  <p class="lead">In a complex domain, objects that only hold data leave the rules <span class="hl-pink">nowhere in particular</span>, so they spread, get copied and get skipped.</p>
  <ul>
    <li>Order has setters for everything; any code can set any status.</li>
    <li>The cancel rule exists in some services, not in others.</li>
    <li>Nobody can list the rules of an order by reading the Order.</li>
  </ul>""",
    problem_figs=[an_problem],
    analogy_side="a car and a wheelbarrow",
    analogy="""  <p>A <b>car</b> has its safety rules built in: it won't shift into reverse at speed. Leaving those to the driver would be dangerous. A <b>wheelbarrow</b> has no rules and needs none: adding a computer would be silly. The question isn't “rich or plain?” but <b>“how complex is the job?”</b></p>
  <ul>
    <li>The car is a <b>rich model</b> for a complex domain.</li>
    <li>The wheelbarrow is <b>plain data</b> for CRUD.</li>
    <li>The problem is a car built like a wheelbarrow.</li>
  </ul>""",
    analogy_figs=[an_analogy],
    map=[("A car with rules built in", "Entities with behaviour: <code>order.cancel()</code> checks the rule"),
         ("A wheelbarrow", "Plain records and a transaction script for simple screens"),
         ("A car without brakes", "Anemic model in a complex domain: rules in services"),
         ("A wheelbarrow with a computer", "Aggregates and events for a settings page"),
         ("Matching build to job", "Rich model in the core; simple code elsewhere")],
    how_side="put behaviour where the complexity is",
    how="""  <p>Use the subdomain sort (note 02): <b>core</b> domains with real rules get rich models; <b>supporting</b> and <b>generic</b> ones can be plain data and scripts. In functional code, plain data plus pure functions in the same module, with precise types, is <b>not</b> anemic: the rules still have one clear home.</p>""",
    how_figs=[an_how],
    steps=[("Ask how complex the rules are", "Many rules and states? Core-like. Mostly forms and lists? CRUD."),
           ("In a complex area, find the setters", "Each setter called from several services is a missing method."),
           ("Move rules onto the object", "<code>order.cancel()</code> instead of <code>order.setStatus('cancelled')</code> plus checks elsewhere."),
           ("Hide the setters", "Private fields; changes only through business methods."),
           ("Keep services thin", "Application services load, call, save, nothing more."),
           ("In simple areas, don't bother", "Plain records, validation at the edge, a transaction script. That's a choice, not a smell.")],
    vocab=[("Anemic domain model", "Domain objects with data but no behaviour; logic lives in services."),
           ("Rich domain model", "Objects that hold both data and the rules that change it."),
           ("Transaction script", "A procedure per use case that does all the work (Fowler, PoEAA)."),
           ("Tell, don't ask", "Tell an object what to do rather than asking for data and deciding outside."),
           ("Feature envy", "Code that uses another object's data more than its own: a hint the logic is misplaced."),
           ("Functional core", "Pure functions over immutable data, kept together by module.")],
    code=dict(file="order.ts", note="from anemic to rich, only where it matters", src="""
// anemic: the rule lives (or doesn't) in whichever service remembers it
order.setStatus("cancelled");

// rich: the rule lives on Order, so every caller gets it
export class Order {
  cancel(reason: CancellationReason, now: Date) {
    if (this.status === "shipped") throw new Error("Shipped orders are returned, not cancelled");
    if (this.status === "cancelled") return;                       // idempotent
    this.status = "cancelled";
    this.events.push({ type: "OrderCancelled", orderId: this.id, reason, at: now });
  }
}

// a supporting CRUD area: plain data is fine
type OpeningHours = Readonly<{ storeId: StoreId; day: Weekday; opens: Time; closes: Time }>;
"""),
    tools="tools: code review (“where does this rule live?”), static analysis that flags public setters and feature envy, architecture tests that keep business rules out of controllers, and the subdomain chart to decide where rich models are worth it.",
    gains=["<b>Rich model in the core</b>: rules in one place, can't be skipped.",
           "<b>Plain data elsewhere</b>: less code where rules are few.",
           "<b>A clear test</b> for code review: where does this rule live?",
           "<b>Effort matches complexity</b>."],
    losses=["<b>Judgement</b>: the line between core and CRUD moves.",
            "<b>Two styles</b> in one codebase to explain.",
            "<b>Refactoring cost</b> when a CRUD area grows rules.",
            "<b>ORMs</b> sometimes push toward public setters."],
    baseline="Each line compares <b>an anemic model used everywhere, including the complex core</b> to <b>rich models in the core and plain data only where rules are few</b>.",
    ratings=[(3, 4, "Each area is as simple as its rules allow."),
             (2, 4, "Core objects say what they do."),
             (2, 5, "Core rules can't be bypassed by setters."),
             (2, 4, "A rule changes in one method."),
             (3, 4, "Core rules tested on objects; CRUD tested end to end."),
             (3, 4, "Services stop reaching into every object."),
             (3, 3, "Neutral."),
             (3, 3, "More thought in the core, less code elsewhere."),
             (3, 3, "Neutral.")],
    pitfalls=[("Calling all plain data “anemic”", "A team rewrites a simple admin screen with aggregates and events.", "rich models only where the rules are complex."),
              ("Setters left public", "Methods are added, but code still calls <code>setStatus</code>.", "make fields private once the methods exist."),
              ("Logic in controllers", "Rules move out of services and into HTTP handlers instead.", "into the domain object, not one layer up."),
              ("Ignoring growth", "A “simple” returns screen grows 30 rules over two years, still as scripts.", "revisit when a supporting area's rules multiply.")],
    use=["Reviewing a complex domain whose rules are hard to find.",
         "Deciding how much modelling an area deserves.",
         "Bugs caused by setters bypassing business rules."],
    skip=["Simple CRUD and admin screens: plain data is the right choice.",
          "Pure functional code with precise types, where data and functions are kept together by module."],
    related=["<b>Core, Supporting &amp; Generic Subdomains</b>", "<b>Entity</b>", "<b>Domain &amp; Application Services</b>", "<b>Make Illegal States Unrepresentable</b>"],
    quiz=[("What is an anemic domain model?", "Domain objects with data and getters/setters but no behaviour; the rules live in services around them."),
          ("When is plain data with services perfectly fine?", "In simple CRUD and supporting areas where there are few rules."),
          ("What's the usual fix in a complex domain?", "Move rules onto the objects as business-named methods and hide the setters."),
          ("Is functional code with data types and separate functions anemic?", "Not necessarily: with precise types and functions grouped by module, the rules still have one clear home.")],
    quiz_sit=[("A reviewer rejects a pull request for a store-opening-hours admin screen because “the model is anemic, add aggregates and domain events”. The screen has two rules. What do you answer?",
               "That opening hours are a simple supporting area: plain records, validation at the edge and a transaction script are the right size. Rich models are for the core, where rules are many and costly to get wrong. Agree to revisit if the rules grow.")],
    try_it="Pick one class in your core domain and search for every call to its setters. For the most-called one, write a method named after the business action, move the checks into it from the callers, and make the setter private.",
    then_now=dict(src="Fowler, 2003", verdict="rethought",
                  then="Fowler named the anemic domain model an anti-pattern in 2003: objects that look like a domain model but have no behaviour, “procedural design in object clothing”, paying the cost of a domain model without the benefit.",
                  now="Still true for complex domains. But the industry learned two nuances: most of a system is CRUD, where plain data is the right choice (see subdomains), and functional programming separates data and functions deliberately, with types doing much of the protecting.",
                  take="Rethought: an anti-pattern in the core, a sensible choice elsewhere. Judge it by where the rules are."),
    remember="Don't build a <span class=\"hl\">car without brakes</span>, and don't put a <span class=\"hl\">computer on a wheelbarrow</span>.",
    sources=["Martin Fowler, “AnemicDomainModel” (bliki, 2003).",
             "Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Transaction Script” and “Domain Model”.",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 5–6.",
             "Scott Wlaschin, <i>Domain Modeling Made Functional</i> (2018), ch. 1."],
)

NOTES = [SPECIFICATION, ILLEGAL_STATES, ANEMIC]
