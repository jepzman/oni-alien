# Vol. 7 · Domain-Driven Design · Building blocks: Value Object, Entity, Aggregate, Domain Events, Repository,
# Domain & Application Services.

# ------------------------------------------------------------------ 10 Value Object
vo_problem = Doodle(760, 270, "Doodle of primitive obsession. A price is a plain number and a currency is a separate string. Somewhere the code adds 10 euros to 10 pounds and gets 20. An email address is a string, and an invalid one gets stored. A discount of minus 50 percent is accepted. The same checks are copied into twelve places, and some are missing.",
                    "Plain numbers and strings: euros plus pounds, invalid emails, negative discounts, checks copied twelve times.")
vo_problem.box(20, 40, 220, 70, "10 + 10 = 20", "pink", stroke="red", sub="€ + £ ?!", size=18)
vo_problem.box(270, 40, 220, 70, "“bob@”", "pink", stroke="red", sub="stored as an email", size=18)
vo_problem.box(520, 40, 220, 70, "discount −50%", "pink", stroke="red", sub="accepted", size=18)
vo_problem.note(380, 170, "if (price < 0) … copied into 12 places", "pen")
vo_problem.note(380, 220, "…and missing from the 13th", "red")

vo_analogy = Doodle(760, 250, "Doodle of banknotes. A ten-euro note is defined by its value, not by which note it is: you don't care which ten-euro note you get back as change, and you can't change a note into a twenty by writing on it. To get a different amount, you swap it for another note. Notes also check themselves: a fake is rejected.",
                     "Any ten-euro note will do; you can't edit one into a twenty; fakes are rejected at the till.")
vo_analogy.box(40, 60, 200, 100, "€10", "green", sub="any one will do")
vo_analogy.box(280, 60, 200, 100, "€10", "green", sub="equal to the first")
vo_analogy.box(520, 60, 200, 100, "fake €10", "pink", stroke="red", sub="rejected")
vo_analogy.note(380, 210, "defined by value · can't be edited · checked on entry", "pen")

vo_how = Doodle(760, 300, "A value object called Money. It is created through a factory that checks the amount and currency, so an invalid Money can't exist. It is immutable: add returns a new Money. Two Moneys with the same amount and currency are equal. Adding different currencies throws an error. The same idea works for EmailAddress, Quantity, DateRange and Percentage.",
                 "Checked when created, never changed, equal by value, with its rules inside.")
vo_how.box(250, 30, 260, 120, "Money", "y", sub="cents · currency")
vo_how.note(130, 60, "valid or not created", "green")
vo_how.note(130, 100, "immutable", "green")
vo_how.note(630, 60, "equal by value", "green")
vo_how.note(630, 100, "rules inside: add()", "green")
vo_how.row([("EmailAddress", "", "paper"), ("Quantity", "", "paper"), ("DateRange", "", "paper"), ("Percentage", "", "paper")], x=20, y=200, h=60, gap=16, size=16)

VALUE_OBJECT = dict(
    slug="value-object",
    kicker="a.k.a. “any ten-euro note will do”",
    tldr="Replace plain numbers and strings with small types like <b>Money</b>, <b>EmailAddress</b> or <b>DateRange</b>. A value object is <b>defined by its value</b> (two €10 are equal), is <b>immutable</b> (to change it, make a new one), and <b>checks itself</b> when created, so an invalid one can't exist. Its rules (adding money, overlapping ranges) live <b>inside</b> it, written once.",
    chips=[("Family", "tactical building block"), ("From", "Evans (2003), ch. 5"), ("Language support", "records, data classes, branded types"), ("Pairs with", "entity, make illegal states unrepresentable")],
    problem="""  <p class="lead">Using raw numbers and strings for business concepts (<span class="hl-pink">primitive obsession</span>) scatters the rules and lets invalid data in.</p>
  <ul>
    <li>Euros get added to pounds because both are just numbers.</li>
    <li>“bob@” is stored as an email address.</li>
    <li>The same validation is copied into many places, and missing from some.</li>
  </ul>""",
    problem_figs=[vo_problem],
    analogy_side="banknotes",
    analogy="""  <p>A <b>ten-euro note</b> is defined by its value: you don't care which one you get as change. You can't turn it into a twenty by writing on it; you swap it for another note. And the till <b>rejects fakes</b> at the door.</p>
  <ul>
    <li>Equal if the <b>value</b> is equal.</li>
    <li><b>Immutable</b>: replace, don't edit.</li>
    <li><b>Validated</b> on the way in.</li>
  </ul>""",
    analogy_figs=[vo_analogy],
    map=[("Any €10 note will do", "Equality by value, not identity"),
         ("Can't write a 2 in front", "Immutable: operations return a new object"),
         ("Swap it for a twenty", "<code>price.add(tax)</code> returns new Money"),
         ("Till rejects fakes", "Constructor or factory validates; invalid values can't exist"),
         ("Notes have one currency", "<code>add()</code> refuses different currencies")],
    how_side="small, immutable, self-checking types",
    how="""  <p>Most of a domain model is value objects; entities are fewer than people think. A good test: <b>“if two of these have the same data, are they the same?”</b> If yes, it's a value object.</p>""",
    how_figs=[vo_how],
    steps=[("Spot the primitives", "Prices as numbers, emails as strings, date pairs, percentages, quantities with units."),
           ("Make a type for each", "Money, EmailAddress, DateRange, Percentage. Use the business's words."),
           ("Validate on creation", "A private constructor and a factory that returns the value or an error."),
           ("Make it immutable", "Readonly fields; operations return new instances."),
           ("Compare by value", "Implement equals, or use the language's records or data classes."),
           ("Move rules inside", "Adding money, checking overlaps, formatting: methods on the type, written once.")],
    vocab=[("Value object", "An immutable object defined only by its attributes."),
           ("Primitive obsession", "Using raw strings and numbers for domain concepts."),
           ("Immutable", "Can't change after it's created."),
           ("Structural equality", "Equal when all fields are equal."),
           ("Self-validating", "Checks its own invariants when created."),
           ("Branded type", "A TypeScript trick to make a string type distinct, like <code>OrderId</code>.")],
    code=dict(file="money.ts", note="a value object", src="""
export class Money {
  private constructor(readonly cents: bigint, readonly currency: Currency) {}

  static of(cents: bigint, currency: Currency): Money {
    if (cents < 0n) throw new Error("Money can't be negative");
    return new Money(cents, currency);
  }
  add(other: Money): Money {
    if (other.currency !== this.currency) throw new Error("Different currencies");
    return Money.of(this.cents + other.cents, this.currency);   // a new object
  }
  times(qty: Quantity): Money { return Money.of(this.cents * BigInt(qty.value), this.currency); }
  equals(o: Money) { return o.cents === this.cents && o.currency === this.currency; }
}

const total = Money.of(1999n, "EUR").times(Quantity.of(3));   // EUR 59.97
"""),
    tools="tools: records in Java and C#, data classes in Kotlin and Python (<code>frozen=True</code>), branded types or Zod schemas in TypeScript, ORM support for embedded values (JPA <code>@Embeddable</code>, EF Core owned types).",
    gains=["<b>Rules in one place</b>, not copied.",
           "<b>Invalid values can't exist</b>.",
           "<b>Immutability</b> removes a class of bugs.",
           "<b>Code reads like the business</b>: <code>price.add(tax)</code>."],
    losses=["<b>More small types</b> to write.",
            "<b>Mapping</b> to and from the database and JSON.",
            "<b>Some allocation</b> for immutable copies.",
            "<b>Team habits</b>: people reach for strings by default."],
    baseline="Each line compares <b>business values stored as plain numbers and strings</b> to <b>small immutable value objects</b>.",
    ratings=[(3, 4, "Each type is tiny and obvious."),
             (2, 5, "Money, Quantity, EmailAddress: the business's words."),
             (2, 5, "Invalid values are rejected at creation."),
             (2, 4, "A rule changes in one class."),
             (3, 5, "Pure, small, no dependencies: trivial to test."),
             (3, 4, "Callers depend on a type, not on a format."),
             (4, 3, "A few extra allocations; rarely matters."),
             (4, 3, "More types and mapping code."),
             (3, 4, "Shared types make intent clear across the team.")],
    pitfalls=[("Mutable value objects", "Two orders share one Address object; changing one changes both.", "make it immutable; operations return new instances."),
              ("Validation outside", "Money can be built negative, and a service checks later (sometimes).", "private constructor plus factory; no invalid instance can exist."),
              ("Everything is an entity", "Address gets an ID and its own table and lifecycle.", "ask “if the data is the same, is it the same thing?”"),
              ("Floats for money", "0.1 + 0.2 ≠ 0.3 on an invoice.", "integer minor units (cents) or a decimal type, inside Money.")],
    use=["Any concept with rules: money, quantities, emails, ranges, percentages, codes.",
         "The same validation appears in more than one place.",
         "Mixing units or currencies would be a real bug."],
    skip=["A field with no rules at all (a free-text note).",
          "Hot loops where allocation really is measured as a problem."],
    related=["<b>Entity</b>", "<b>Aggregate</b>", "<b>Make Illegal States Unrepresentable</b>", "<b>Shared Kernel &amp; Partnership</b>"],
    quiz=[("What makes something a value object?", "It's defined by its value (equal when its fields are equal), immutable, and usually validates itself."),
          ("How do you change a value object?", "You don't: you create a new one, often with a method that returns a new instance."),
          ("Why store money in cents (or a decimal), not floats?", "Floating point can't represent many decimal amounts exactly, so totals drift."),
          ("What's primitive obsession?", "Using raw strings and numbers for domain concepts, which scatters their rules.")],
    quiz_sit=[("A bug report: an order total showed €59.969999. Prices are <code>number</code> and every service rounds “its own way”. What do you change?",
               "Introduce a Money value object with integer cents (or a decimal type) and a currency, put rounding and arithmetic inside it, and replace raw numbers at the boundaries, starting with order totals.")],
    try_it="Find one concept in your code that is a plain string or number but has rules (an email, a price, a percentage). Write a value object with a factory that validates, one operation, and equality, then replace it in one function and its tests.",
    then_now=dict(src="Evans, 2003", verdict="grown",
                  then="Evans described value objects as immutable, attribute-defined objects, and encouraged making as many things values as possible. In Java in 2003 that meant writing equals, hashCode and constructors by hand.",
                  now="Languages caught up: Java and C# records, Kotlin data classes, Python frozen dataclasses, TypeScript branded types. Immutability became mainstream through functional programming. Making a value object is now a one-liner.",
                  take="More useful now: the idea was always right, and today it's nearly free to apply."),
    remember="Any <span class=\"hl\">€10 note</span> will do, nobody can edit it, and the till <span class=\"hl\">rejects fakes</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 5 “Value Objects”.",
             "Martin Fowler, “ValueObject” (bliki, 2016).",
             "Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), ch. 6.",
             "Scott Wlaschin, <i>Domain Modeling Made Functional</i> (2018), ch. 5."],
)

# ------------------------------------------------------------------ 11 Entity
en_problem = Doodle(760, 260, "Doodle of identity going wrong. A customer changes their email address, and because the system used the email as the key, their order history disappears and a duplicate customer appears. Another customer moved house and the system treats them as a new person. Two records are merged by name and two different John Smiths become one.",
                    "Using an email or a name as identity: changes split one person in two, and two people become one.")
en_problem.box(20, 40, 220, 80, "anna@old", "paper", sub="12 orders")
en_problem.arrow(244, 80, 296, 80)
en_problem.note(270, 26, "email change", "pen")
en_problem.box(300, 40, 200, 80, "anna@new", "pink", stroke="red", sub="0 orders?!")
en_problem.box(540, 40, 200, 80, "John Smith", "pink", stroke="red", sub="two people, merged")
en_problem.note(380, 190, "identity tied to data that changes", "red")

en_analogy = Doodle(760, 250, "Doodle of a person through life. Name, address, hair colour and job change over the years, but it's still the same person, tracked by a passport or national ID number that never changes. Two people with the same name and birthday are still two people.",
                     "Name, address and hair change; the person and their passport number stay the same.")
en_analogy.box(20, 60, 200, 90, "age 8", "y", sub="Annie, Leeds")
en_analogy.box(280, 60, 200, 90, "age 30", "y", sub="Anna, Utrecht")
en_analogy.box(540, 60, 200, 90, "age 70", "y", sub="Anna B., Porto")
en_analogy.arrow(224, 105, 276, 105)
en_analogy.arrow(484, 105, 536, 105)
en_analogy.note(380, 200, "same person: ID NL-48213 all along", "green")

en_how = Doodle(760, 300, "An entity called Customer. It has an ID generated when it is created, like a UUID, that never changes. Its other attributes, like name, email and address, can change through methods with business names, such as changeEmail and moveTo, which check the rules. Two customers are equal only if their IDs are equal. Its address is a value object inside it.",
                 "An ID that never changes; attributes that change through named methods; equal by ID only.")
en_how.box(240, 30, 280, 180, None, "blue")
en_how.head(380, 62, "Customer")
en_how.text(380, 100, "id: 018f…c2 (never changes)")
en_how.text(380, 136, "email · name · address")
en_how.text(380, 176, "changeEmail() · moveTo()")
en_how.note(120, 80, "equal by ID", "green")
en_how.note(640, 80, "rules in methods", "green")
en_how.box(540, 230, 200, 50, "Address", "y", sub="a value object", size=16, subsize=13)
en_how.arrow(520, 200, 560, 228, dash=True)

ENTITY = dict(
    slug="entity",
    kicker="a.k.a. “same person, new haircut”",
    tldr="An entity is something the business tracks <b>through time</b>: a customer, an order, a parcel. It has an <b>identity</b> that never changes (an ID you generate, not an email or a name), while its other details <b>do</b> change, through methods with <b>business names</b> that check the rules. Two entities are equal only if their <b>IDs</b> are equal.",
    chips=[("Family", "tactical building block"), ("From", "Evans (2003), ch. 5"), ("Identity", "UUID or ULID, created by the app"), ("Pairs with", "value object, aggregate")],
    problem="""  <p class="lead">When identity is tied to data that changes, <span class="hl-pink">one thing splits in two</span>, or <span class="hl-pink">two things merge into one</span>.</p>
  <ul>
    <li>A customer changes email and loses their order history.</li>
    <li>Two John Smiths become one record.</li>
    <li>Setters let any code change anything, so rules are skipped.</li>
  </ul>""",
    problem_figs=[en_problem],
    analogy_side="a person through life",
    analogy="""  <p>Over a lifetime a person changes <b>name, address, hair and job</b>, yet they are the same person, tracked by a <b>passport number</b> that never changes. Two people with the same name and birthday are still two people.</p>
  <ul>
    <li>The person is an <b>entity</b>.</li>
    <li>The passport number is its <b>identity</b>.</li>
    <li>The address is a <b>value</b> that gets replaced when they move.</li>
  </ul>""",
    analogy_figs=[en_analogy],
    map=[("A person", "An entity: Customer, Order, Parcel"),
         ("Passport number", "A generated ID that never changes"),
         ("Changing name or address", "<code>customer.changeEmail()</code>, <code>moveTo()</code>"),
         ("Same name, different people", "Equality by ID, not by attributes"),
         ("The address on file", "A value object inside the entity")],
    how_side="identity plus behaviour",
    how="""  <p>Keep entities <b>small</b>: identity, a few attributes, and the behaviour that changes them. Push details into value objects. And prefer methods named after business actions over public setters.</p>""",
    how_figs=[en_how],
    steps=[("Ask “is it tracked over time?”", "If the business cares which one it is, not just what it contains, it's an entity."),
           ("Generate the ID early", "A UUID v7 or ULID created in the code when the entity is born, not by the database later."),
           ("Never use changing data as the ID", "Not email, name or address. Those are attributes."),
           ("Replace setters with actions", "<code>order.ship()</code>, <code>customer.moveTo(address)</code>, each checking its rules."),
           ("Equality by ID", "Two Customer objects with the same ID are the same customer."),
           ("Extract value objects", "Address, Money, EmailAddress live inside the entity as values.")],
    vocab=[("Entity", "An object with a lasting identity whose attributes can change."),
           ("Identity", "What makes it the same thing over time: usually a generated ID."),
           ("Natural key", "An ID taken from the data (email, tax number); risky if it can change."),
           ("Surrogate key", "An ID with no meaning, generated for the purpose."),
           ("Lifecycle", "The states an entity goes through, from creation to archive."),
           ("UUID v7 / ULID", "Unique IDs that also sort by creation time.")],
    code=dict(file="customer.ts", note="an entity: ID plus behaviour", src="""
export class Customer {
  private constructor(
    readonly id: CustomerId,                 // never changes
    private email: EmailAddress,             // value objects inside
    private address: Address,
  ) {}

  static register(email: EmailAddress, address: Address): Customer {
    return new Customer(CustomerId.new(), email, address);   // uuidv7, created here
  }

  changeEmail(newEmail: EmailAddress, verified: boolean) {
    if (!verified) throw new Error("Verify the new address first");
    this.email = newEmail;
  }
  moveTo(newAddress: Address) { this.address = newAddress; }

  equals(other: Customer) { return other.id === this.id; }
}
"""),
    tools="tools: UUID v7 or ULID generators, ORM entity mappings (JPA, EF Core, Prisma, TypeORM) that allow private fields, and lint rules that flag public setters on domain classes.",
    gains=["<b>Stable identity</b> while details change.",
           "<b>Rules in named methods</b>, not scattered setters.",
           "<b>IDs before saving</b>: easier events and tests.",
           "<b>Clear equality</b>: same ID, same thing."],
    losses=["<b>Mapping private fields</b> can fight the ORM.",
            "<b>Generated IDs</b> are long and not human-friendly.",
            "<b>More thought</b> than a public-fields data class.",
            "<b>Easy to over-use</b> for things that are really values."],
    baseline="Each line compares <b>data classes with public setters and natural keys</b> to <b>entities with generated IDs and named behaviour</b>.",
    ratings=[(3, 4, "One place to see how a customer can change."),
             (3, 5, "Methods named after business actions."),
             (2, 4, "Rules are checked in each action; identity can't drift."),
             (3, 4, "A new rule goes into one method."),
             (3, 4, "Construct in memory with an ID; no database needed."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral; UUID v7 keeps indexes ordered."),
             (4, 3, "Methods instead of setters; some ORM configuration."),
             (3, 3, "Neutral.")],
    pitfalls=[("Email or name as the key", "A change of email splits the history.", "generated ID; the email is an attribute with a unique index."),
              ("Public setters everywhere", "Any code can set <code>status = 'shipped'</code> without a parcel.", "business-named methods that check rules."),
              ("Database-generated IDs only", "No ID until saved, so events and links can't be made earlier.", "create the ID in code (UUID v7, ULID)."),
              ("Equality by fields", "Two different customers with the same name compare as equal.", "compare entities by ID only.")],
    use=["Things the business tracks over time and refers to: customers, orders, accounts, parcels.",
         "Objects whose details change but whose history matters."],
    skip=["Things defined only by their values (money, address, date range): use value objects.",
          "Read-only reporting rows with no behaviour."],
    related=["<b>Value Object</b>", "<b>Aggregate</b>", "<b>Repository</b>", "<b>Surrogate Keys</b> (Vol. 3)"],
    quiz=[("What makes something an entity?", "A lasting identity: the business cares which one it is, and it changes over time."),
          ("Why not use an email address as the ID?", "Emails change; the identity must not, or one customer becomes two."),
          ("How are two entities compared?", "By ID only."),
          ("Why generate the ID in code rather than in the database?", "The entity has an identity from birth, so events, links and tests can use it before it's saved.")],
    quiz_sit=[("Support merges duplicate customer accounts every week, because sign-up creates a new customer whenever someone uses a different email at checkout. How do you fix the model?",
               "Give Customer a generated ID independent of email, let a customer have a verified email that can change, and match guest checkouts to existing customers by a deliberate process rather than creating one per email.")],
    try_it="Pick one class in your code with public setters. Replace two setters with methods named after business actions, each with one rule, and write a test for each rule. Check what the class uses as its identity.",
    then_now=dict(src="Evans, 2003", verdict="core",
                  then="Evans defined entities by continuity and identity, and warned against letting them become bags of attributes. IDs were often database sequences, assigned on insert.",
                  now="Same idea. The details changed: IDs are now usually generated in code (UUID v7 and ULID sort well in indexes), ORMs can map private fields, and the advice to keep entities small and push detail into value objects is stronger.",
                  take="Still core. Fewer entities than you think, and each with behaviour, not setters."),
    remember="New haircut, new address, <span class=\"hl\">same passport number</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 5 “Entities”.",
             "Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), ch. 5.",
             "RFC 9562, “Universally Unique IDentifiers (UUIDs)” (2024): UUID v7.",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 6."],
)

# ------------------------------------------------------------------ 12 Aggregate
ag_problem = Doodle(760, 270, "Doodle of an invariant being broken. The rule is: an order may have at most ten lines and its total must not exceed the customer's credit limit. Two pieces of code add lines to the same order directly through the line repository, at the same time. Neither sees the other's line. The order ends up with twelve lines and over the limit. The rule was checked, but in the wrong place.",
                    "Lines are added directly by two pieces of code at once; the order ends up with 12 lines and over its limit.")
ag_problem.box(250, 30, 260, 90, "Order", "paper", sub="max 10 lines · ≤ limit")
ag_problem.box(20, 170, 220, 60, "code A: add line", "blue", size=16)
ag_problem.box(520, 170, 220, 60, "code B: add line", "blue", size=16)
ag_problem.arrow(130, 166, 300, 124, color="red")
ag_problem.note(380, 160, "both go straight to the lines", "red")
ag_problem.arrow(630, 166, 460, 124, color="red")
ag_problem.note(380, 258, "result: 12 lines, €200 over the limit", "red")

ag_analogy = Doodle(760, 250, "Doodle of a restaurant table and its waiter. Customers don't walk into the kitchen and add dishes to their own ticket. They ask the table's waiter, who checks the rules: the kitchen is closing, the table has a set menu, the dish is sold out. The ticket and its items change only through the waiter, one request at a time.",
                     "You don't add dishes to your own ticket in the kitchen: you ask the table's waiter, who checks the rules.")
ag_analogy.box(30, 60, 200, 90, "guests", "paper", sub="“add a dessert”")
ag_analogy.arrow(234, 105, 296, 105)
ag_analogy.box(300, 50, 160, 110, "waiter", "y", sub="checks rules")
ag_analogy.arrow(464, 105, 526, 105)
ag_analogy.box(530, 60, 200, 90, "ticket", "green", sub="items, total")
ag_analogy.note(380, 220, "the ticket only changes through the waiter", "pen")

ag_how = Doodle(760, 330, "An Order aggregate. The Order is the aggregate root; it contains order lines and a shipping address. Outside code can only hold a reference to the Order, by ID, and must call its methods, like addLine, which check the rules: at most ten lines and total within the credit limit. The whole aggregate is loaded and saved in one transaction with a version number for optimistic locking. Other aggregates, like Customer and Product, are referenced by ID only.",
                 "One root guards the rules; the whole cluster is saved in one transaction; others are referenced by ID.")
ag_how.box(200, 30, 360, 230, None, "y", dash=True)
ag_how.box(260, 50, 240, 70, "Order (root)", "green", sub="addLine() · version 7")
ag_how.box(230, 150, 140, 50, "OrderLine", "paper", size=15)
ag_how.box(390, 150, 140, 50, "OrderLine", "paper", size=15)
ag_how.box(310, 210, 140, 40, "Address", "paper", size=15)
ag_how.box(20, 60, 150, 50, "customerId", "blue", size=15)
ag_how.box(590, 60, 150, 50, "productId", "blue", size=15)
ag_how.arrow(256, 85, 174, 85, dash=True)
ag_how.arrow(504, 85, 586, 85, dash=True)
ag_how.note(380, 296, "outside code calls the root · one transaction per aggregate", "pen")
ag_how.note(380, 322, "other aggregates by ID only", "pen")

AGGREGATE = dict(
    slug="aggregate",
    kicker="a.k.a. “ask the waiter, don't walk into the kitchen”",
    tldr="Group objects that must stay consistent together (an order and its lines) into an <b>aggregate</b> with one <b>root</b>. Outside code can only talk to the <b>root</b>, which checks every rule before changing anything inside. One aggregate is loaded and saved in <b>one transaction</b>; other aggregates are referenced <b>by ID</b> and updated <b>separately</b>, often by events. Keep aggregates <b>small</b>.",
    chips=[("Family", "tactical building block"), ("From", "Evans (2003), ch. 6; Vernon (2011)"), ("Rule of thumb", "one aggregate per transaction"), ("Pairs with", "repository, domain events, optimistic locking")],
    problem="""  <p class="lead">When any code can change any object, business rules that span several objects (<span class="hl-pink">invariants</span>) get broken, especially under concurrency.</p>
  <ul>
    <li>Lines are added straight to the line table, bypassing the order's limits.</li>
    <li>Two requests change the same order at once and both “pass” the check.</li>
    <li>One transaction locks orders, customers and stock at the same time.</li>
  </ul>""",
    problem_figs=[ag_problem],
    analogy_side="the table's waiter",
    analogy="""  <p>In a restaurant you don't walk into the kitchen and add dishes to your own ticket. You ask <b>your table's waiter</b>, who checks the rules (kitchen closing, set menu, sold out) and updates the ticket. One waiter per table means two guests can't put conflicting orders on it at the same time.</p>
  <ul>
    <li>The ticket and its items are the <b>aggregate</b>.</li>
    <li>The waiter is the <b>aggregate root</b>.</li>
    <li>Other tables are <b>other aggregates</b>, served separately.</li>
  </ul>""",
    analogy_figs=[ag_analogy],
    map=[("The table's ticket and items", "The Order aggregate with its lines"),
         ("The waiter", "The aggregate root: <code>Order</code>"),
         ("“Add a dessert”", "<code>order.addLine(productId, qty)</code>"),
         ("Kitchen's closing, no more", "Invariants checked inside the root"),
         ("Other tables", "Other aggregates (Customer, Product) referenced by ID")],
    how_side="a consistency boundary with one door",
    how="""  <p>Vaughn Vernon's four rules (2011): <b>protect true invariants</b> inside the border; <b>design small</b> aggregates; <b>reference others by ID</b>; and use <b>eventual consistency</b> between aggregates. Ask “does this rule really have to be true at every instant, or within a few seconds?”</p>""",
    how_figs=[ag_how],
    steps=[("Find the invariants", "Rules that must be true at every moment: “at most ten lines”, “total within credit limit”."),
           ("Draw the smallest border around them", "Only objects that take part in such a rule go inside."),
           ("Pick the root", "The one entity outside code may hold and call. Everything else is reached through it."),
           ("Refer to others by ID", "Order stores <code>customerId</code>, not a Customer object."),
           ("One aggregate per transaction", "Load, call a method, save, with a version number for optimistic locking."),
           ("Between aggregates, use events", "“Order placed” → reserve stock in another transaction, eventually consistent.")],
    vocab=[("Aggregate", "A cluster of objects treated as one unit for changes."),
           ("Aggregate root", "The single entry point that enforces the aggregate's rules."),
           ("Invariant", "A rule that must always hold within the aggregate."),
           ("Consistency boundary", "The border inside which changes are immediately consistent."),
           ("Optimistic concurrency", "Save only if the version hasn't changed since loading."),
           ("Eventual consistency", "Other aggregates catch up shortly after, through events.")],
    code=dict(file="order.ts", note="the root guards the rules", src="""
export class Order {
  private lines: OrderLine[] = [];
  private status: "draft" | "placed" = "draft";
  private constructor(readonly id: OrderId, readonly customerId: CustomerId,  // by ID
                      private creditLimit: Money, public version = 0) {}

  addLine(productId: ProductId, qty: Quantity, unitPrice: Money) {
    if (this.status !== "draft") throw new Error("Order is already placed");
    if (this.lines.length >= 10) throw new Error("At most 10 lines");
    const next = this.total().add(unitPrice.times(qty));
    if (next.cents > this.creditLimit.cents) throw new Error("Over credit limit");
    this.lines.push(new OrderLine(productId, qty, unitPrice));
  }
  total(): Money { return this.lines.reduce((t, l) => t.add(l.subtotal()), Money.zero("EUR")); }
}

// application code: one aggregate, one transaction, optimistic lock
const order = await orders.get(id);
order.addLine(productId, qty, price);
await orders.save(order);   // UPDATE ... WHERE id = ? AND version = ?   -> retry on conflict
"""),
    tools="tools: ORMs with optimistic locking (<code>@Version</code> in JPA, concurrency tokens in EF Core), document databases that store one aggregate per document, and event stores (EventStoreDB, Marten) for event-sourced aggregates.",
    gains=["<b>Invariants always hold</b>, even under concurrency.",
           "<b>One door</b>: easy to see how state can change.",
           "<b>Small transactions</b>, fewer lock conflicts.",
           "<b>Natural unit</b> for storage, caching and events."],
    losses=["<b>Hard to size right</b>: too big locks too much, too small can't protect rules.",
            "<b>Eventual consistency</b> between aggregates must be designed.",
            "<b>Loading the whole aggregate</b> for a small change.",
            "<b>Queries across aggregates</b> need separate read models."],
    baseline="Each line compares <b>objects any code can change, with rules checked here and there</b> to <b>small aggregates whose roots enforce the rules</b>.",
    ratings=[(2, 3, "One door per cluster, but sizing takes skill."),
             (3, 4, "Rules live in methods on the root."),
             (2, 5, "The main gain: invariants are enforced in one place, safely."),
             (2, 4, "A rule change happens inside one aggregate."),
             (3, 5, "Pure in-memory objects; test rules without a database."),
             (2, 4, "Aggregates point at each other only by ID."),
             (3, 3, "Small transactions vs loading whole clusters: depends on size."),
             (4, 3, "Roots, versioning and events between aggregates."),
             (2, 4, "Small aggregates rarely collide between teams or requests.")],
    pitfalls=[("Giant aggregates", "Customer contains all orders, all addresses and all payments; every change locks it.", "small aggregates around true invariants; reference by ID."),
              ("Changing two aggregates in one transaction", "Placing an order also updates stock and loyalty points atomically.", "one aggregate per transaction; the rest via events."),
              ("Bypassing the root", "A repository for OrderLine lets code add lines directly.", "repositories only for roots; children reached through the root."),
              ("No concurrency control", "Two requests load version 7 and both save.", "optimistic locking with a version column; retry on conflict.")],
    use=["Rules that span several objects and must always hold.",
         "Concurrent changes to the same business object.",
         "A rich core domain with real behaviour."],
    skip=["CRUD screens with no rules across objects.",
          "Reporting and queries (use read models)."],
    related=["<b>Entity</b>", "<b>Repository</b>", "<b>Domain Events</b>", "<b>Optimistic Locking</b> (Vol. 3)", "<b>Event Sourcing</b> (Vol. 1)"],
    quiz=[("What is an aggregate root?", "The one entity outside code may reference and call; it enforces the aggregate's rules."),
          ("Why reference other aggregates by ID?", "So each aggregate stays small, is loaded and saved alone, and isn't accidentally changed through another."),
          ("How many aggregates should one transaction change?", "One, as a rule. Others are updated afterwards, usually through domain events."),
          ("How do you stop two concurrent changes from breaking an invariant?", "Optimistic locking: save only if the version is unchanged, otherwise retry.")],
    quiz_sit=[("Your <code>Customer</code> aggregate holds every order, address and payment method. Saving it takes 800 ms and checkout fails with lock timeouts during sales. What do you change?",
               "Split it: make Order its own aggregate referencing the customer by ID, keep in Customer only what its own invariants need, and update anything else (loyalty, stats) through events after the order is placed. Add optimistic locking per aggregate.")],
    try_it="Pick one business rule that involves several objects (an order's maximum, a booking's capacity). Write the root class with one method that enforces it and a test that fails when the rule is broken. Then decide which other objects it should reference only by ID.",
    then_now=dict(src="Evans, 2003; Vernon, 2011", verdict="grown",
                  then="Evans described aggregates as clusters with a root and a boundary, but gave little guidance on size, and early implementations were often large object graphs loaded through ORM lazy loading.",
                  now="Vernon's “Effective Aggregate Design” (2011) rethought the sizing: small aggregates, references by ID, eventual consistency between them. Aggregates then became the unit of event sourcing, of documents in NoSQL stores, and of consistency in microservices.",
                  take="More important today than in 2003: it's the tactical pattern that matters most, as long as you keep it small."),
    remember="Ask <span class=\"hl\">the waiter</span>; never add to the ticket <span class=\"hl\">in the kitchen</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 6 “Aggregates”.",
             "Vaughn Vernon, “Effective Aggregate Design”, parts I–III (2011).",
             "Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), ch. 10.",
             "Martin Fowler, “DDD_Aggregate” (bliki, 2013)."],
)

# ------------------------------------------------------------------ 13 Domain Events
de_problem = Doodle(760, 270, "Doodle of a place-order method that does everything. It saves the order, then reserves stock, sends a confirmation email, adds loyalty points, notifies analytics and updates the recommendation model, all in one method and one transaction. When the email service is slow, checkout is slow. When analytics is down, orders fail. Each new reaction means editing the method again.",
                    "placeOrder() calls six things in a row: a slow email server slows checkout, and analytics down means no orders.")
de_problem.box(20, 90, 200, 80, "placeOrder()", "y", sub="does everything")
for i, t in enumerate(["reserve stock", "send email", "loyalty points", "analytics", "recommendations"]):
    y = 14 + i * 50
    de_problem.box(310, y, 220, 40, t, "paper", size=15)
    de_problem.arrow(224, 130, 306, y + 20)
de_problem.note(650, 90, "email slow →", "red")
de_problem.note(650, 120, "checkout slow", "red")
de_problem.note(650, 170, "analytics down →", "red")
de_problem.note(650, 200, "no orders", "red")

de_analogy = Doodle(760, 250, "Doodle of a birth announcement. When a baby is born, the parents send one card: Mia was born on the fourth of March. They don't phone the registry, grandparents, the employer and the nursery one by one and wait for each. Each recipient decides what to do: register the birth, knit a hat, arrange leave.",
                     "One announcement, “Mia was born”, and everyone who cares decides what to do about it.")
de_analogy.box(260, 30, 240, 80, "“Mia was born”", "y", sub="4 March")
for i, t in enumerate(["registry", "grandparents", "employer"]):
    x = 20 + i * 250
    de_analogy.box(x, 160, 220, 56, t, "paper", size=17)
    de_analogy.arrow(380, 114, x + 110, 156, dash=True)
de_analogy.note(380, 240, "the parents don't wait for any of them", "pen")

de_how = Doodle(760, 320, "Domain events in the online shop. The Order aggregate records an OrderPlaced event when placeOrder succeeds. The event is saved in the same transaction as the order, in an outbox table. A relay publishes it to a message broker. Stock, email, loyalty and analytics each subscribe and react in their own time and transaction. If email is down, its handler retries later; orders keep working.",
                 "The aggregate records “OrderPlaced”; it's saved with the order and published; each reaction runs separately.")
de_how.box(20, 40, 200, 90, "Order", "green", sub="records event")
de_how.box(20, 170, 200, 70, "outbox", "paper", sub="same transaction")
de_how.arrow(120, 134, 120, 166)
de_how.box(280, 120, 180, 70, "broker", "y", sub="OrderPlaced")
de_how.arrow(224, 205, 276, 160)
for i, t in enumerate(["stock", "email", "loyalty", "analytics"]):
    y = 20 + i * 70
    de_how.box(540, y, 200, 54, t, "blue", size=17)
    de_how.arrow(464, 155, 536, y + 27)
de_how.note(380, 300, "email down? it retries later; orders keep flowing", "green")

DOMAIN_EVENTS = dict(
    slug="domain-events",
    kicker="a.k.a. “the birth announcement”",
    tldr="When something happens that the business cares about, <b>record it as an event</b> in the past tense: <code>OrderPlaced</code>, <code>PaymentFailed</code>, <code>ParcelDelivered</code>. The aggregate <b>records</b> the event; it's <b>saved with</b> the change and then <b>published</b>. Other parts of the system <b>react</b> in their own time: reserve stock, send an email, add points. The order code doesn't need to know who's listening.",
    chips=[("Family", "tactical building block"), ("Not in", "the 2003 book (added by Evans in 2004+)"), ("Delivered by", "outbox + message broker"), ("Pairs with", "aggregate, transactional outbox, event storming")],
    problem="""  <p class="lead">One method that does the change <span class="hl-pink">and every reaction to it</span> becomes slow, fragile and impossible to extend safely.</p>
  <ul>
    <li><code>placeOrder()</code> calls stock, email, loyalty and analytics in a row.</li>
    <li>A slow or broken side service breaks the main action.</li>
    <li>Every new reaction means editing the core method again.</li>
  </ul>""",
    problem_figs=[de_problem],
    analogy_side="the birth announcement",
    analogy="""  <p>When a baby is born, the parents send <b>one announcement</b>: “Mia was born on 4 March.” They don't ring the registry, the grandparents, the employer and the nursery one by one and wait for each. <b>Each recipient decides</b> what to do: register, knit a hat, arrange leave.</p>
  <ul>
    <li>The announcement is a <b>domain event</b>: a fact, in the past tense.</li>
    <li>The recipients are <b>subscribers</b>.</li>
    <li>The parents don't depend on them.</li>
  </ul>""",
    analogy_figs=[de_analogy],
    map=[("“Mia was born on 4 March”", "<code>OrderPlaced { orderId, total, placedAt }</code>"),
         ("Sent once by the parents", "Recorded by the aggregate, published once"),
         ("Registry, grandparents, employer", "Stock, email, loyalty, analytics handlers"),
         ("Each decides what to do", "Each handler reacts in its own transaction"),
         ("Parents don't wait", "Checkout returns before the email is sent")],
    how_side="record the fact, publish it, react separately",
    how="""  <p><b>Domain events</b> stay inside a context and use its language. When you share them with other contexts, publish a stable <b>integration event</b> (part of a published language) and keep the internal one free to change.</p>""",
    how_figs=[de_how],
    steps=[("Name events in the past tense", "From the business's words: <code>OrderPlaced</code>, not <code>OrderCreatedEvent</code> or <code>SendEmail</code>."),
           ("Record them in the aggregate", "The method that changes state also appends the event to a list."),
           ("Save with the change", "Write events to an outbox table in the same transaction as the aggregate."),
           ("Publish reliably", "A relay or change-data-capture moves outbox rows to the broker."),
           ("Handle idempotently", "Each handler can receive an event twice; make that harmless."),
           ("Separate internal and integration events", "Translate to a versioned public event before other contexts see it.")],
    vocab=[("Domain event", "A record of something that happened in the domain, in the past tense."),
           ("Integration event", "A published, versioned event meant for other contexts."),
           ("Event handler", "Code that reacts to an event."),
           ("Transactional outbox", "Saving events in the same transaction as the change, then publishing."),
           ("Idempotent handler", "Processing the same event twice has the same effect as once."),
           ("Eventual consistency", "Other parts catch up shortly after the event.")],
    code=dict(file="order.ts", note="record, save with the change, react elsewhere", src="""
type OrderPlaced = { type: "OrderPlaced"; orderId: OrderId; total: Money; placedAt: Date };

export class Order {
  readonly events: OrderPlaced[] = [];
  place(now: Date) {
    if (this.lines.length === 0) throw new Error("Empty order");
    this.status = "placed";
    this.events.push({ type: "OrderPlaced", orderId: this.id, total: this.total(), placedAt: now });
  }
}

// repository: save state and events in one transaction (outbox)
await db.tx(async (t) => {
  await t.orders.update(order);
  await t.outbox.insertMany(order.events);
});

// elsewhere, in its own transaction, idempotent
on("OrderPlaced", async (e) => { await email.sendConfirmation(e.orderId); });
"""),
    tools="tools: an outbox table plus a relay or Debezium, brokers like Kafka, RabbitMQ, SNS/SQS or Azure Service Bus, in-process dispatchers (MediatR notifications, Spring application events) for reactions inside one service.",
    gains=["<b>Decoupled reactions</b>: add a subscriber without touching the order.",
           "<b>Resilience</b>: a broken side service doesn't break the main action.",
           "<b>Audit trail</b> of what happened in business terms.",
           "<b>Matches the language</b> from event storming."],
    losses=["<b>Eventual consistency</b>: reactions happen a bit later.",
            "<b>Harder to follow</b> the flow by reading code.",
            "<b>Infrastructure</b>: outbox, broker, retries.",
            "<b>Duplicates and ordering</b> must be handled."],
    baseline="Each line compares <b>one method that performs the change and every reaction</b> to <b>an aggregate that records domain events handled separately</b>.",
    ratings=[(3, 2, "The flow is spread across handlers."),
             (3, 5, "Events are named in the business's past tense."),
             (3, 4, "The core change is atomic; reactions retry until done."),
             (2, 5, "New reactions are new handlers, not edits."),
             (3, 4, "Test that an event is recorded; test handlers alone."),
             (2, 5, "The order code doesn't know who listens."),
             (3, 4, "Checkout doesn't wait for email or analytics."),
             (4, 2, "Outbox, broker, handlers, idempotency."),
             (2, 4, "Teams subscribe without coordinating with the publisher.")],
    pitfalls=[("Publishing before committing", "The event goes out, then the transaction rolls back: a ghost order.", "transactional outbox: save events with the change, publish after commit."),
              ("Commands dressed as events", "<code>SendWelcomeEmail</code> published as an “event”.", "events state facts in the past tense; the subscriber decides what to do."),
              ("Leaking internal events", "Other teams subscribe to internal events, so you can't change them.", "translate to versioned integration events at the border."),
              ("Non-idempotent handlers", "A redelivered event sends two emails or adds points twice.", "store processed event IDs, or make the effect naturally idempotent.")],
    use=["Several reactions to one business fact.",
         "Side effects that shouldn't slow down or break the main action.",
         "Integrating contexts loosely, or building read models."],
    skip=["A single reaction that must happen in the same transaction (just do it).",
          "Tiny apps where a direct call is simpler and failure is fine."],
    related=["<b>Aggregate</b>", "<b>Event Storming</b>", "<b>Transactional Outbox</b> (Vol. 1)", "<b>Idempotent Consumer</b> (Vol. 1)", "<b>Publish–Subscribe</b> (Vol. 1)"],
    quiz=[("How should domain events be named?", "In the past tense, using the business's words: OrderPlaced, PaymentFailed."),
          ("Why save events in the same transaction as the change?", "So an event is published if and only if the change was committed (transactional outbox)."),
          ("What's the difference between a domain event and an integration event?", "A domain event is internal to a context; an integration event is a published, versioned contract for other contexts."),
          ("Why must handlers be idempotent?", "Brokers deliver at least once, so a handler may see the same event twice.")],
    quiz_sit=[("Customers sometimes get an order confirmation email for an order that doesn't exist. Logs show the email handler ran, but the order transaction rolled back. What's wrong?",
               "The event was published before the transaction committed. Save the event in an outbox table in the same transaction, and publish it only after commit through a relay, so a rolled-back order never produces an event.")],
    try_it="Find a method in your code that changes something and then calls two or more side effects. Make it record an event instead, write the event to a table in the same transaction, and move one side effect into a handler that reads it.",
    then_now=dict(src="Evans, 2004+ (not in the 2003 book)", verdict="grown",
                  then="Domain events are missing from the 2003 book. Evans added them afterwards (talks from 2004, the DDD Reference in 2015), after teams found that “something happened” was a key part of the model.",
                  now="They are now central: event storming starts from them, event-driven architecture and microservices run on them, and the outbox pattern and brokers like Kafka made publishing them reliable.",
                  take="Grew from an afterthought into one of the most used DDD ideas."),
    remember="Send <span class=\"hl\">one announcement</span>, in the past tense, and let everyone who cares <span class=\"hl\">decide for themselves</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design Reference</i> (2015), “Domain Events”.",
             "Martin Fowler, “DomainEvent” (bliki, 2005).",
             "Udi Dahan, “Domain Events – Salvation” (2009).",
             "Chris Richardson, <i>Microservices Patterns</i> (2018), ch. 3 and 5 (transactional outbox, domain events)."],
)

# ------------------------------------------------------------------ 14 Repository
re_problem = Doodle(760, 260, "Doodle of SQL scattered through business code. The pricing rule loads order lines with a hand-written query in the middle of a discount calculation. Another service loads orders with a slightly different join and forgets the lines. Tests for the discount rule need a real database. Changing a column name means searching forty files.",
                    "SQL inside business rules: different queries for the same thing, and every rule's test needs a database.")
re_problem.box(20, 40, 340, 140, None, "pink", stroke="red")
re_problem.head(190, 74, "applyDiscount()")
re_problem.text(190, 112, "SELECT … JOIN order_lines")
re_problem.text(190, 146, "if (total > 100) …")
re_problem.box(400, 40, 340, 140, None, "pink", stroke="red")
re_problem.head(570, 74, "shipOrder()")
re_problem.text(570, 112, "SELECT * FROM orders")
re_problem.text(570, 146, "(forgets the lines)")
re_problem.note(380, 230, "rename a column → search 40 files", "red")

re_analogy = Doodle(760, 250, "Doodle of a library desk. You ask the librarian for the book with a given number, and you get the whole book, cover and pages together. You don't go into the stacks, and you don't get loose chapters. When you're done you hand the whole book back. How the stacks are organised is the librarian's business.",
                     "Ask the librarian for a book by number, get the whole book, hand the whole book back.")
re_analogy.box(30, 60, 200, 90, "you", "paper", sub="“book 823.9”")
re_analogy.arrow(234, 105, 296, 105, both=True)
re_analogy.box(300, 50, 180, 110, "librarian", "y", sub="get / put back")
re_analogy.arrow(484, 105, 546, 105, dash=True)
re_analogy.box(550, 60, 190, 90, "stacks", "blue", sub="their business")
re_analogy.note(380, 220, "whole books only, never loose chapters", "pen")

re_how = Doodle(760, 320, "A repository for Order aggregates. The domain defines an interface, OrderRepository, with get by ID, save, and a few business queries like ordersAwaitingShipment. Application code uses the interface. In production, a Postgres implementation maps tables to aggregates; in tests, an in-memory implementation is used. There is one repository per aggregate root, never per table.",
                 "The domain owns the interface; the database implementation is a detail; tests use an in-memory one.")
re_how.box(250, 20, 260, 90, "OrderRepository", "y", sub="get · save · awaiting…")
re_how.note(130, 60, "interface in the domain", "pen")
re_how.box(60, 190, 280, 80, "PostgresOrders", "blue", sub="maps tables ↔ aggregate")
re_how.box(420, 190, 280, 80, "InMemoryOrders", "green", sub="for tests")
re_how.arrow(200, 186, 330, 114, dash=True, label="implements", lx=220, ly=150, anchor="end")
re_how.arrow(560, 186, 430, 114, dash=True)
re_how.note(380, 304, "one repository per aggregate root, not per table", "pen")

REPOSITORY = dict(
    slug="repository",
    kicker="a.k.a. “ask the librarian for the whole book”",
    tldr="Give each <b>aggregate root</b> a repository: an interface that looks like a <b>collection</b> (<code>get(id)</code>, <code>save(order)</code>, a few named queries) and hides how the aggregate is stored. Business code asks for <b>whole aggregates</b>, never rows, and never writes SQL. The interface lives in the domain; the database code implements it, and tests use an <b>in-memory</b> version.",
    chips=[("Family", "tactical building block"), ("From", "Evans (2003), ch. 6; Fowler, PoEAA (2002)"), ("One per", "aggregate root"), ("Pairs with", "aggregate, unit of work, ORM")],
    problem="""  <p class="lead">When business rules fetch their own data, <span class="hl-pink">SQL spreads through the domain</span> and every rule's test needs a database.</p>
  <ul>
    <li>Different queries load “the same” order differently, some without its lines.</li>
    <li>Rules can't be tested without a database.</li>
    <li>A schema change means hunting through dozens of files.</li>
  </ul>""",
    problem_figs=[re_problem],
    analogy_side="the library desk",
    analogy="""  <p>At a library you ask the <b>librarian</b> for book 823.9 and get the <b>whole book</b>, cover and pages together. You don't wander the stacks or get loose chapters, and you hand the whole book back when you're done. How the stacks are arranged is the librarian's business.</p>
  <ul>
    <li>The librarian is the <b>repository</b>.</li>
    <li>The book is the <b>aggregate</b>.</li>
    <li>The stacks are the <b>database</b>.</li>
  </ul>""",
    analogy_figs=[re_analogy],
    map=[("The librarian", "<code>OrderRepository</code>"),
         ("Ask by number", "<code>orders.get(orderId)</code>"),
         ("Whole book, never loose chapters", "Whole aggregate, never separate lines"),
         ("Hand it back", "<code>orders.save(order)</code>"),
         ("How the stacks are arranged", "Tables, joins and ORM mapping, hidden behind the interface")],
    how_side="a collection-like door to storage",
    how="""  <p>Keep the interface <b>small and named in the domain's language</b>. For reports and screens that need lists, joins and paging, don't stretch the repository: use a separate <b>query service</b> or read model (CQRS-style).</p>""",
    how_figs=[re_how],
    steps=[("One per aggregate root", "OrderRepository, CustomerRepository. Never OrderLineRepository."),
           ("Define the interface in the domain", "In the domain's terms: <code>get</code>, <code>save</code>, <code>awaitingShipment()</code>."),
           ("Implement it in infrastructure", "With your ORM or SQL, mapping rows to the aggregate and back."),
           ("Load and save whole aggregates", "With a version for optimistic locking."),
           ("Keep queries few and named", "A handful of business queries; everything else goes to a read model."),
           ("Use an in-memory version in tests", "So domain and application tests run in milliseconds.")],
    vocab=[("Repository", "A collection-like interface for loading and saving aggregates."),
           ("Aggregate root", "The only thing a repository returns and saves."),
           ("Data mapper", "Code that moves data between objects and tables (often the ORM)."),
           ("Unit of work", "Tracks changes and commits them together; most ORMs include one."),
           ("Generic repository", "A one-size <code>Repository&lt;T&gt;</code> for every table; usually adds nothing over the ORM."),
           ("Read model", "A separate model optimised for queries and screens.")],
    code=dict(file="order-repository.ts", note="interface in the domain, implementation outside", src="""
// domain/ordering/order-repository.ts
export interface OrderRepository {
  get(id: OrderId): Promise<Order>;                 // whole aggregate, or throws
  save(order: Order): Promise<void>;                // optimistic lock on version
  awaitingShipment(limit: number): Promise<Order[]>;
}

// infrastructure/postgres-orders.ts
export class PostgresOrders implements OrderRepository {
  constructor(private db: Kysely<DB>) {}
  async get(id: OrderId) {
    const row = await this.db.selectFrom("orders").where("id", "=", id).selectAll().executeTakeFirstOrThrow();
    const lines = await this.db.selectFrom("order_lines").where("order_id", "=", id).selectAll().execute();
    return OrderMapper.toDomain(row, lines);
  }
  // save(): update orders WHERE version = ?, replace lines, insert outbox events
}

// tests: new InMemoryOrders()  — same interface, a Map inside
"""),
    tools="tools: ORMs that already act as repositories and units of work (EF Core DbSet, Spring Data, Hibernate, Prisma), query builders like Kysely or jOOQ for the implementation, and a simple in-memory fake for tests.",
    gains=["<b>No SQL in business rules</b>.",
           "<b>Fast domain tests</b> with an in-memory repository.",
           "<b>Whole aggregates</b> loaded the same way every time.",
           "<b>Storage can change</b> without touching the domain."],
    losses=["<b>An extra layer</b> over an ORM that already does this.",
            "<b>Mapping code</b> between rows and aggregates.",
            "<b>Tempting to bloat</b> with query methods.",
            "<b>Loading whole aggregates</b> can be wasteful for small reads."],
    baseline="Each line compares <b>business code that queries the database directly</b> to <b>aggregates loaded and saved through a repository per root</b>.",
    ratings=[(3, 4, "Business code reads without SQL."),
             (3, 4, "Queries named in domain terms."),
             (3, 4, "Aggregates always loaded whole, with version checks."),
             (2, 4, "Schema changes stay in the implementation."),
             (2, 5, "Domain tests use an in-memory repository."),
             (2, 4, "The domain doesn't depend on the database."),
             (3, 3, "Whole aggregates can over-fetch; reads go to read models."),
             (4, 3, "An interface, an implementation and a mapper per root."),
             (3, 3, "Neutral.")],
    pitfalls=[("A repository per table", "OrderLineRepository lets code change lines without the root.", "one repository per aggregate root."),
              ("Generic repository over the ORM", "<code>Repository&lt;T&gt;</code> with <code>getAll()</code> just wraps DbSet and leaks IQueryable.", "use the ORM directly, or write specific repositories with named methods."),
              ("Query explosion", "<code>findByStatusAndCityAndDateBetween…</code> for every screen.", "send screen queries to a read model or query service."),
              ("Saving inside the domain", "Entities call repositories to save themselves.", "application services load, call and save; the domain stays storage-free.")],
    use=["A rich domain model with aggregates.",
         "You want business rules tested without a database.",
         "Storage details are complex or may change."],
    skip=["CRUD apps where the ORM already gives you all you need.",
          "Reporting and list screens (use queries or read models)."],
    related=["<b>Aggregate</b>", "<b>Domain &amp; Application Services</b>", "<b>CQRS</b> (Vol. 1)", "<b>Fakes</b> (Vol. 4)", "<b>Batch Loading</b> (Vol. 3)"],
    quiz=[("How many repositories should an aggregate have?", "One, for its root. Children are loaded and saved through the root."),
          ("Where does the repository interface live?", "In the domain layer, in domain terms. The implementation lives in infrastructure."),
          ("Why is a generic Repository&lt;T&gt; over an ORM often pointless?", "The ORM already is a repository and unit of work; the wrapper adds a layer without adding meaning."),
          ("What do you use for complex list and report queries?", "A separate query service or read model, not more repository methods.")],
    quiz_sit=[("Your <code>OrderRepository</code> has 46 methods, most of them for admin screens with filters and paging, and it returns half-loaded orders. What do you change?",
               "Cut it back to the aggregate's needs: get, save and a few business queries that return whole orders. Move screen queries to a query service that returns flat DTOs straight from SQL, without loading aggregates.")],
    try_it="Pick one aggregate in your code. Write a repository interface with only <code>get</code>, <code>save</code> and one business query, an in-memory implementation, and rewrite one domain test to use it instead of the database. Time the test before and after.",
    then_now=dict(src="Evans, 2003; Fowler, PoEAA 2002", verdict="built-in",
                  then="Evans and Fowler described repositories as collection-like interfaces over a data mapper, hiding query construction. In 2003 you wrote them yourself, often with hand-written SQL.",
                  now="Modern ORMs (EF Core, Spring Data, Hibernate, Prisma) already provide repositories and units of work. Wrapping them in a generic repository is now seen as an anti-pattern. A thin, specific repository per aggregate root is still valuable for a rich domain and fast tests.",
                  take="Built in now: use your ORM's version, and add your own interface only for aggregate roots in a rich domain."),
    remember="Ask the <span class=\"hl\">librarian</span> for the <span class=\"hl\">whole book</span>, and hand the whole book back.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 6 “Repositories”.",
             "Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Repository”.",
             "Microsoft, “Design the infrastructure persistence layer” (.NET microservices guide).",
             "Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), ch. 12."],
)

# ------------------------------------------------------------------ 15 Domain & Application Services
ds_problem = Doodle(760, 270, "Doodle of logic in the wrong places. A transfer of loyalty points between two customers is written as a method on Customer that reaches into another Customer. A 900-line OrderService mixes HTTP parsing, transactions, email sending and pricing rules. Nobody can find where the discount rule lives, and it is tested only through HTTP.",
                    "A 900-line OrderService mixing HTTP, transactions, email and pricing rules; nobody can find the discount rule.")
ds_problem.box(160, 30, 440, 170, None, "pink", stroke="red")
ds_problem.head(380, 64, "OrderService · 900 lines")
ds_problem.text(380, 104, "parse request · open transaction")
ds_problem.text(380, 136, "if (vip && total > 100) … · send email")
ds_problem.text(380, 170, "save · log · map to JSON")
ds_problem.note(380, 246, "“where is the discount rule?”", "red")

ds_analogy = Doodle(760, 250, "Doodle of a hospital. The surgeon performs the operation using medical knowledge: that's the domain. The ward coordinator books the theatre, gets consent forms signed, calls the surgeon and the anaesthetist, and arranges the bed afterwards, but makes no medical decisions: that's the application service. A transfer between two wards is decided by a bed manager, not by either ward alone: a domain service.",
                     "The coordinator organises (application); the surgeon decides (domain); the bed manager handles what no single ward owns.")
ds_analogy.box(20, 50, 220, 100, "coordinator", "paper", sub="books, calls, arranges")
ds_analogy.box(270, 50, 220, 100, "surgeon", "green", sub="medical decisions")
ds_analogy.box(520, 50, 220, 100, "bed manager", "y", sub="between two wards")
ds_analogy.note(130, 190, "application service", "pen")
ds_analogy.note(380, 190, "entities / aggregates", "pen")
ds_analogy.note(630, 190, "domain service", "pen")

ds_how = Doodle(760, 330, "Layers for one use case, transferring loyalty points. A controller receives the HTTP request and calls the TransferPoints application service. The application service opens a transaction, loads both customers from the repository, calls the PointsTransfer domain service, which applies the rules across both customers, then saves both and publishes events. The domain service has no database or HTTP code; the application service has no business rules.",
                  "Application service: load, call, save. Domain service: a rule across several objects. Neither does the other's job.")
ds_how.row([("controller", "HTTP → command", "paper"), ("application svc", "load · call · save", "blue"), ("domain svc", "the rule", "y"), ("aggregates", "Customer A, B", "green")], x=14, y=40, h=90, gap=40, size=16, subsize=13, arrows=True)
ds_how.note(380, 180, "application service: no business rules, no HTTP", "pen")
ds_how.note(380, 216, "domain service: no database, no HTTP, just rules", "pen")
ds_how.box(160, 250, 440, 56, "transfer(from, to, points, policy)", "y", size=16)

DOMAIN_SERVICE = dict(
    slug="domain-service",
    kicker="a.k.a. “the coordinator books the theatre; the surgeon operates”",
    tldr="Put a business rule that <b>belongs to no single object</b> (a transfer between two accounts, a price that depends on customer, basket and promotions) in a <b>domain service</b>: stateless, named in the domain's language, with no database or HTTP code. Put the <b>use case</b> (load, call the domain, save, publish) in an <b>application service</b>, which has no business rules of its own. Both stay <b>thin</b>; most logic belongs on entities and value objects.",
    chips=[("Family", "tactical building block"), ("From", "Evans (2003), ch. 5; Fowler's service layer (2002)"), ("Today often", "command handlers, use-case classes"), ("Pairs with", "repository, aggregate")],
    problem="""  <p class="lead">Without a clear home for rules that span objects, and for use-case plumbing, both end up in a <span class="hl-pink">giant “service” class</span> that does everything.</p>
  <ul>
    <li>One OrderService mixes HTTP, transactions, email and pricing rules.</li>
    <li>Or one entity reaches into another to apply a shared rule.</li>
    <li>Business rules are tested only through HTTP.</li>
  </ul>""",
    problem_figs=[ds_problem],
    analogy_side="the hospital",
    analogy="""  <p>In a hospital the <b>coordinator</b> books the theatre, gets forms signed and calls the team, but makes <b>no medical decisions</b>. The <b>surgeon</b> makes them. A move between two wards is decided by the <b>bed manager</b>, because neither ward can decide it alone.</p>
  <ul>
    <li>The coordinator is the <b>application service</b>.</li>
    <li>The surgeon's knowledge lives in <b>entities and aggregates</b>.</li>
    <li>The bed manager is a <b>domain service</b>.</li>
  </ul>""",
    analogy_figs=[ds_analogy],
    map=[("Coordinator: books, calls, arranges", "Application service: transaction, load, save, publish"),
         ("Makes no medical decisions", "Contains no business rules"),
         ("The surgeon decides", "Entities and aggregates hold most rules"),
         ("Bed manager between wards", "Domain service: a rule across several aggregates"),
         ("Consent forms", "Authorisation and input checks before the use case")],
    how_side="two kinds of service, both thin",
    how="""  <p>Try the entity first. Only when a rule truly needs <b>several aggregates</b> or an outside policy (exchange rates, tax tables) does it become a domain service. If a domain service grows large, the model is probably missing a concept.</p>""",
    how_figs=[ds_how],
    steps=[("Put rules on objects first", "If a rule is about one order, it's a method on Order."),
           ("Spot cross-object rules", "Transfers, pricing across basket and customer, matching. Those become domain services."),
           ("Name them as domain actions", "<code>PointsTransfer</code>, <code>PricingPolicy</code>, not <code>CustomerHelper</code>."),
           ("Keep domain services pure", "Stateless, no repositories, no HTTP: values in, decisions out."),
           ("One application service per use case", "<code>TransferPoints</code>: authorise, load, call the domain, save, publish."),
           ("Keep controllers dumb", "Parse input into a command, call the use case, map the result.")],
    vocab=[("Domain service", "A stateless operation expressing a domain rule that doesn't belong to one entity."),
           ("Application service", "Coordinates a use case: transaction, loading, calling the domain, saving."),
           ("Service layer", "Fowler's term for the application layer's boundary of use cases."),
           ("Command handler", "A modern shape of an application service: one class per command."),
           ("Use case", "One thing a user or system wants to do, end to end."),
           ("God service", "A huge service class that holds everything.")],
    code=dict(file="transfer-points.ts", note="application service + domain service", src="""
// domain: pure rule across two aggregates
export class PointsTransfer {
  transfer(from: Customer, to: Customer, points: Points, policy: LoyaltyPolicy) {
    if (from.tier === "basic" && points.value > policy.basicTransferLimit)
      throw new Error("Basic members can transfer at most " + policy.basicTransferLimit);
    from.spendPoints(points);
    to.receivePoints(points);
  }
}

// application: one use case, no business rules
export class TransferPoints {
  constructor(private customers: CustomerRepository, private tx: UnitOfWork,
              private rule = new PointsTransfer(), private policy: LoyaltyPolicy) {}
  async handle(cmd: { from: CustomerId; to: CustomerId; points: number }) {
    await this.tx.run(async () => {
      const [a, b] = await Promise.all([this.customers.get(cmd.from), this.customers.get(cmd.to)]);
      this.rule.transfer(a, b, Points.of(cmd.points), this.policy);
      await this.customers.saveAll([a, b]);
    });
  }
}
"""),
    tools="tools: command and handler libraries (MediatR, Axon, NestJS CQRS module), use-case or “interactor” classes in clean architecture, and architecture tests that keep HTTP and database imports out of the domain layer.",
    gains=["<b>Business rules have a clear home</b>.",
           "<b>Use cases are easy to find</b>: one class each.",
           "<b>Domain tests without infrastructure</b>.",
           "<b>Thin controllers</b> and thin services."],
    losses=["<b>More classes</b> than one big service.",
            "<b>Judgement needed</b>: entity or domain service?",
            "<b>Domain services can become dumping grounds</b>.",
            "<b>Overkill</b> for CRUD."],
    baseline="Each line compares <b>a large service class mixing plumbing and rules</b> to <b>thin application services and focused domain services</b>.",
    ratings=[(2, 4, "Plumbing and rules are no longer mixed."),
             (2, 4, "Services named after domain actions and use cases."),
             (3, 4, "Cross-object rules are checked in one place."),
             (2, 4, "A rule changes in the domain; a flow in the use case."),
             (2, 5, "Domain services are pure functions of their inputs."),
             (2, 4, "The domain doesn't know about HTTP or databases."),
             (3, 3, "Neutral."),
             (4, 3, "More, smaller classes."),
             (3, 4, "Use cases can be owned and changed separately.")],
    pitfalls=[("Everything is a service", "Entities are data bags; all logic sits in services.", "put rules on entities first; services only for what spans objects."),
              ("Rules in the application service", "<code>if (vip && total &gt; 100)</code> inside the use case.", "move the decision into the domain; the use case just calls it."),
              ("Domain services with repositories", "The pricing rule loads customers from the database itself.", "pass in what it needs; loading is the application's job."),
              ("Helper and Manager names", "<code>OrderHelper</code>, <code>CustomerManager</code> hide what they do.", "name after the domain action.")],
    use=["Rules that involve several aggregates or an outside policy.",
         "A codebase where use cases are hard to find.",
         "You want business rules tested without infrastructure."],
    skip=["Simple CRUD: one handler that saves a form is enough.",
          "A rule that clearly belongs on one entity."],
    related=["<b>Aggregate</b>", "<b>Repository</b>", "<b>Anemic Domain Model</b>", "<b>Entity</b>"],
    quiz=[("What's the difference between a domain service and an application service?", "A domain service holds a business rule that spans objects; an application service coordinates a use case (load, call, save) with no business rules."),
          ("Should a domain service use repositories?", "Preferably not: the application service loads what's needed and passes it in."),
          ("When should a rule be a domain service rather than an entity method?", "When it involves several aggregates or an outside policy, and doesn't naturally belong to one."),
          ("What's a common modern shape for application services?", "One command handler or use-case class per operation.")],
    quiz_sit=[("A code review shows a new <code>DiscountService</code> that loads the customer and basket from the database, checks VIP status, calls the payment API and writes an audit log. What do you suggest?",
               "Split it: a pure domain service (or a method on the basket) that decides the discount from values passed in; an application service that loads the customer and basket, calls it, saves and publishes; and the payment call and audit log in infrastructure behind ports.")],
    try_it="Take the biggest service class in your code. Highlight the lines that are business rules in one colour and plumbing (HTTP, transactions, mapping, logging) in another. Move one rule into an entity or a pure domain service and test it without a database.",
    then_now=dict(src="Evans, 2003; Fowler, PoEAA 2002", verdict="rethought",
                  then="Evans separated domain services (stateless domain operations) from application services; Fowler's service layer defined the application's boundary. Both warned that services can drain the model of its behaviour.",
                  now="The split held, but the shape changed: one big service per entity gave way to one handler per command or use case, vertical slices and clean architecture “interactors”. Functional styles make domain services simply pure functions.",
                  take="Rethought: the two roles are still right; write them as small use-case handlers and pure functions, not big service classes."),
    remember="The coordinator <span class=\"hl\">books the theatre</span>; the surgeon <span class=\"hl\">operates</span>. Never the other way round.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 5 “Services”.",
             "Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), “Service Layer”.",
             "Jimmy Bogard, “Vertical Slice Architecture” (2018).",
             "Robert C. Martin, <i>Clean Architecture</i> (2017), ch. 20–22 (use cases)."],
)

NOTES = [VALUE_OBJECT, ENTITY, AGGREGATE, DOMAIN_EVENTS, REPOSITORY, DOMAIN_SERVICE]
