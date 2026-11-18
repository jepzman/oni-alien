# Vol. 8 · Inside the Application · SOLID, read today: Single Responsibility, Open–Closed, Liskov Substitution,
# Interface Segregation, Dependency Inversion. Running example: the Ordering service of the online shop (Vol. 7).

# ------------------------------------------------------------------ 01 Single Responsibility
sr_problem = Doodle(760, 270, "Doodle of one Invoice class changed by three departments. Finance asks for a new VAT rule; the developer edits Invoice. Design asks for a new PDF layout; the developer edits Invoice. Operations asks to archive invoices to a new store; the developer edits Invoice. A VAT change accidentally moves the total on the PDF, and the archive job breaks after a layout change.",
                    "Finance, design and operations all change the same Invoice class, and break each other's work.")
sr_problem.box(250, 90, 260, 110, "Invoice", "pink", stroke="red", sub="tax · PDF · archive")
for x, t in [(20, "finance"), (290, "design"), (560, "operations")]:
    sr_problem.box(x, 10, 180, 50, t, "paper", size=17)
sr_problem.arrow(110, 64, 290, 104, color="red")
sr_problem.arrow(380, 64, 380, 86, color="red")
sr_problem.arrow(650, 64, 470, 104, color="red")
sr_problem.note(380, 250, "a VAT change moved the total on the PDF", "red")

sr_analogy = Doodle(760, 250, "Doodle of one employee with three bosses. The sales manager, the accountant and the warehouse lead each give the same person instructions. Every new instruction from one boss risks undoing what another asked for. Three people, each with one boss, would not have this problem.",
                    "One employee, three bosses: every instruction risks undoing another boss's.")
sr_analogy.box(290, 140, 180, 80, "one employee", "pink", stroke="red", size=18)
for x, t in [(20, "sales"), (290, "accounts"), (560, "warehouse")]:
    sr_analogy.box(x, 20, 180, 56, t, "paper", size=17)
    sr_analogy.arrow(x + 90, 80, 380, 136, dash=True)
sr_analogy.note(620, 200, "one boss each = calm", "green")

sr_how = Doodle(760, 300, "The invoice split by who asks for changes. A TaxCalculator owned by finance rules, an InvoicePdf owned by design, and an InvoiceArchive owned by operations. Invoice itself is a small object holding the lines and calling them. A change requested by one department now touches one module.",
                 "Split by who asks for the change: one module per actor, a small Invoice in the middle.")
sr_how.box(270, 110, 220, 80, "Invoice", "y", sub="lines, totals")
sr_how.box(20, 20, 220, 70, "TaxCalculator", "green", sub="finance")
sr_how.box(520, 20, 220, 70, "InvoicePdf", "blue", sub="design")
sr_how.box(270, 220, 220, 70, "InvoiceArchive", "paper", sub="operations")
sr_how.arrow(266, 130, 244, 80)
sr_how.arrow(494, 130, 516, 80)
sr_how.arrow(380, 194, 380, 216)
sr_how.note(130, 240, "one reason to change", "green")
sr_how.note(130, 270, "= one group asking", "green")

SRP = dict(
    slug="single-responsibility",
    kicker="a.k.a. “one boss per module”",
    tldr="A module should have <b>one reason to change</b>, which Robert Martin later clarified as <b>one actor</b>: one group of people who ask for changes. Keep together code that changes for the <b>same people</b>, and separate code that changes for <b>different</b> ones (finance's tax rules, design's PDF layout, operations' archiving). It does <b>not</b> mean “a class should do one tiny thing”.",
    chips=[("Family", "SOLID principle"), ("From", "Robert C. Martin, 2000–2003; clarified 2014"), ("Really about", "who asks for changes"), ("Pairs with", "vertical slices, bounded context")],
    problem="""  <p class="lead">When code that serves <span class="hl-pink">different people</span> lives in one class, a change for one of them <span class="hl-pink">breaks the others</span>.</p>
  <ul>
    <li>Finance, design and operations all edit the same Invoice class.</li>
    <li>A tax change shifts a number on the printed PDF.</li>
    <li>Merge conflicts between unrelated work, every sprint.</li>
  </ul>""",
    problem_figs=[sr_problem],
    analogy_side="one employee, three bosses",
    analogy="""  <p>An employee who takes instructions from <b>sales</b>, <b>accounts</b> and the <b>warehouse</b> is always undoing one boss's request for another. Give each job to someone with <b>one boss</b>, and each boss can change their instructions without upsetting the others.</p>
  <ul>
    <li>Each boss is an <b>actor</b>.</li>
    <li>Each job with one boss is a <b>module</b> with one reason to change.</li>
  </ul>""",
    analogy_figs=[sr_analogy],
    map=[("A boss", "An actor: finance, design, operations"),
         ("The overloaded employee", "An Invoice class with tax, PDF and archive code"),
         ("Conflicting instructions", "A change for one actor breaking another's feature"),
         ("One boss per job", "TaxCalculator, InvoicePdf, InvoiceArchive"),
         ("“Do one tiny thing”", "The misreading: splitting by method count, not by actor")],
    how_side="split by who asks",
    how="""  <p>The test is not “does it do one thing?” but <b>“who would ask me to change this?”</b>. If the answer is two different groups, split it. If it's one group, keep it together, even if it's long.</p>""",
    how_figs=[sr_how],
    steps=[("List who asks for changes", "For a big class, write the people or teams whose requests have changed it."),
           ("Group code by actor", "Mark each method with the actor it serves."),
           ("Split along actors", "One module per actor; a small coordinating object if needed."),
           ("Don't split further", "A long module that serves one actor is fine. Tiny classes with one method each are a different problem."),
           ("Check with history", "Files that always change together belong together; files changed for unrelated reasons may not."),
           ("Apply at every level", "Functions, classes, modules and services: the same question.")],
    vocab=[("Single responsibility principle", "A module should be responsible to one, and only one, actor."),
           ("Actor", "A group of people who want the same kind of change."),
           ("Cohesion", "How strongly the parts of a module belong together."),
           ("Change coupling", "Files that change together in version history."),
           ("God class", "A class that does everything for everyone."),
           ("Over-splitting", "Breaking code into so many tiny pieces that nothing is readable.")],
    code=dict(file="invoice.ts", note="split by actor, not by size", src="""
// before: one class, three actors
class Invoice {
  calculateVat() { /* finance's rules */ }
  renderPdf()    { /* design's layout */ }
  archive()      { /* operations' storage */ }
}

// after: each actor's code changes on its own
export class TaxCalculator  { vatFor(lines: Line[], country: Country): Money { /* finance */ } }
export class InvoicePdf     { render(inv: InvoiceView): Buffer { /* design */ } }
export class InvoiceArchive { store(inv: InvoiceView, pdf: Buffer): Promise<void> { /* operations */ } }

export class Invoice {
  constructor(readonly lines: Line[], private tax: TaxCalculator) {}
  total(country: Country) { return sum(this.lines).add(this.tax.vatFor(this.lines, country)); }
}
"""),
    tools="tools: <code>git log --format= --name-only</code> or CodeScene to find files that change together, CODEOWNERS to make actors visible, and review questions like “who asked for this change?”",
    gains=["<b>Changes stay local</b> to one actor's module.",
           "<b>Fewer merge conflicts</b> between unrelated work.",
           "<b>Clear ownership</b>: which team owns which module.",
           "<b>Easier testing</b> of each concern."],
    losses=["<b>More modules</b> to navigate.",
            "<b>Judgement</b>: actors aren't always obvious.",
            "<b>Over-splitting</b> when misread as “one thing”.",
            "<b>Coordination code</b> between the pieces."],
    baseline="Each line compares <b>a class serving several actors</b> to <b>modules split so each serves one actor</b>.",
    ratings=[(3, 4, "Each module has one audience."),
             (3, 4, "Modules named after what each actor cares about."),
             (3, 3, "Neutral."),
             (2, 4, "One actor's change touches one module."),
             (3, 4, "Each concern tested alone."),
             (2, 4, "Unrelated concerns no longer share code."),
             (3, 3, "Neutral."),
             (4, 3, "A few more modules."),
             (2, 4, "Teams stop colliding in one file.")],
    pitfalls=[("Reading it as “do one thing”", "Forty one-method classes nobody can follow.", "split by actor, not by size."),
              ("Splitting by technical layer only", "A Validator, Mapper and Helper per entity, all changed together.", "keep together what changes together."),
              ("Shared “utils” for everyone", "A helpers file every team edits.", "move helpers to the module whose actor needs them."),
              ("Ignoring history", "Splitting on a guess.", "look at which files really change together.")],
    use=["A class or module changed by several teams or for unrelated reasons.",
         "Frequent merge conflicts between unrelated work.",
         "One actor's change keeps breaking another's feature."],
    skip=["A long module that serves one actor: length alone isn't a reason.",
          "Tiny scripts and prototypes."],
    related=["<b>Vertical Slices</b>", "<b>Interface Segregation</b>", "<b>Bounded Context</b> (Vol. 7)", "<b>Transaction Script vs Domain Model</b>"],
    quiz=[("What does “one reason to change” mean, in Martin's later wording?", "A module should be responsible to one actor: one group of people who request changes."),
          ("Does SRP mean every class should do one small thing?", "No. That's a common misreading; a long module serving one actor is fine."),
          ("How can version history help?", "Files that always change together probably belong together; files changed for unrelated reasons may need splitting."),
          ("What's the cost of over-applying it?", "Many tiny pieces and coordination code, making the system harder to read.")],
    quiz_sit=[("A reviewer asks you to split a 300-line <code>ShippingRates</code> class into twelve one-method classes “for SRP”. Every change to it comes from the logistics team. What do you answer?",
               "That it already has one reason to change: logistics. Splitting it into twelve classes would scatter one actor's rules. Split only if another group (say finance) starts changing parts of it.")],
    try_it="Take the most-changed class in your codebase. Read its last 20 commits and write who asked for each change. If two or more groups appear, sketch the split along those lines.",
    then_now=dict(src="Martin, 2000–2003", verdict="rethought",
                  then="“A class should have only one reason to change.” Widely read as “a class should do one thing”, which led to codebases full of tiny Manager, Helper and Validator classes.",
                  now="Martin himself clarified it in 2014 (“The Single Responsibility Principle”) and in <i>Clean Architecture</i> (2017): one <b>actor</b>, not one task. Today it's applied to modules and services too, and backed by change-coupling data from version history.",
                  take="Rethought: still useful once you read “responsibility” as “who asks for changes”."),
    remember="Give every module <span class=\"hl\">one boss</span>, and let it be as long as that boss needs.",
    sources=["Robert C. Martin, <i>Agile Software Development: Principles, Patterns, and Practices</i> (2002), ch. 8.",
             "Robert C. Martin, “The Single Responsibility Principle” (Clean Coder blog, 2014).",
             "Robert C. Martin, <i>Clean Architecture</i> (2017), ch. 7.",
             "Adam Tornhill, <i>Your Code as a Crime Scene</i>, 2nd ed. (2024)."],
)

# ------------------------------------------------------------------ 02 Open–Closed
oc_problem = Doodle(760, 260, "Doodle of a growing switch statement for shipping cost. Each new carrier, DHL, PostNL, DPD, then a bike courier, means editing the same function, adding another case, and retesting all the others. Last month adding the bike courier broke the PostNL case by a misplaced break.",
                    "Every new carrier means editing the same switch, and last month one edit broke another carrier.")
oc_problem.box(220, 20, 320, 180, None, "pink", stroke="red")
oc_problem.head(380, 52, "shippingCost(order)")
for i, t in enumerate(["case 'dhl': …", "case 'postnl': …", "case 'dpd': …", "case 'bike': … (new)"]):
    oc_problem.text(380, 90 + i * 28, t)
oc_problem.note(380, 240, "adding “bike” broke “postnl”", "red")

oc_analogy = Doodle(760, 250, "Doodle of wall sockets. To use a new kettle, toaster or laptop you plug it into a standard socket; you don't open the wall and rewire the house. The wiring is closed for change but open for any new appliance that fits the plug.",
                    "New appliances plug into the socket. Nobody rewires the house for a new kettle.")
oc_analogy.box(300, 60, 160, 120, "socket", "y", sub="standard shape")
for i, t in enumerate(["kettle", "toaster", "laptop"]):
    y = 30 + i * 70
    oc_analogy.box(560, y, 180, 50, t, "paper", size=17)
    oc_analogy.arrow(556, y + 25, 464, 120)
oc_analogy.note(150, 120, "wiring: closed", "pen")
oc_analogy.note(150, 160, "appliances: open", "green")

oc_how = Doodle(760, 300, "Shipping cost made open for extension. A map from carrier name to a pricing function. Each carrier is a small module that registers its function. Adding the bike courier means adding one new file and one line in the registry; the existing carriers' code is not touched.",
                 "A registry of small pricing functions: a new carrier is a new file, not an edit.")
oc_how.box(270, 100, 220, 100, "carrier rates", "y", sub="name → function")
for i, t in enumerate(["dhl.ts", "postnl.ts", "dpd.ts"]):
    oc_how.box(20, 20 + i * 90, 180, 60, t, "paper", size=17)
    oc_how.arrow(204, 50 + i * 90, 266, 150)
oc_how.box(560, 110, 180, 70, "bike.ts", "green", sub="new file")
oc_how.arrow(556, 145, 494, 150)
oc_how.note(380, 260, "nothing existing was edited", "green")

OCP = dict(
    slug="open-closed",
    kicker="a.k.a. “plug it in, don't rewire the house”",
    tldr="Code should be <b>open for extension</b> but <b>closed for modification</b>: adding a new case (a carrier, a payment method, a report format) should mean <b>adding code</b>, not editing a growing <code>switch</code> that every case shares. Today you get there with <b>functions, maps and small interfaces</b>, not inheritance trees, and only where new cases <b>really keep coming</b>.",
    chips=[("Family", "SOLID principle"), ("From", "Bertrand Meyer (1988); Robert C. Martin (1996)"), ("Today", "registries, functions, plug-in points"), ("Pairs with", "strategy, YAGNI")],
    problem="""  <p class="lead">When every new case means <span class="hl-pink">editing shared code</span>, each addition risks <span class="hl-pink">breaking the cases</span> that already work.</p>
  <ul>
    <li>A shipping switch statement grows with each carrier.</li>
    <li>Adding one carrier needs a retest of all the others.</li>
    <li>Several developers edit the same function in parallel.</li>
  </ul>""",
    problem_figs=[oc_problem],
    analogy_side="the wall socket",
    analogy="""  <p>A house's wiring ends in <b>standard sockets</b>. A new kettle just plugs in; nobody opens the wall. The wiring is <b>closed</b> for change and <b>open</b> for any appliance with the right plug.</p>
  <ul>
    <li>The socket is the <b>extension point</b>.</li>
    <li>Each appliance is a <b>new case</b>, added without touching the wiring.</li>
  </ul>""",
    analogy_figs=[oc_analogy],
    map=[("The wiring in the wall", "The core code that uses carriers"),
         ("The socket shape", "A function type or interface: <code>(order) =&gt; Money</code>"),
         ("A new kettle", "A new carrier module"),
         ("Not rewiring the house", "Not editing the switch or the other carriers"),
         ("A house with no sockets", "A growing switch statement")],
    how_side="extension points where change really happens",
    how="""  <p>Don't make everything pluggable “just in case”: that's speculative generality. Add an extension point the <b>second or third time</b> the same kind of change arrives.</p>""",
    how_figs=[oc_how],
    steps=[("Spot the repeating change", "The same switch or if-chain edited for each new kind of thing."),
           ("Name the shape", "What does each case need to provide? <code>(order: Order) =&gt; Money</code>."),
           ("Move each case out", "One small module per case, all with the same shape."),
           ("Register them", "A map or registry the core looks up by key."),
           ("Add by adding", "A new case is a new file and one registration line."),
           ("Stop there", "Leave other code concrete until it shows the same pattern.")],
    vocab=[("Open–closed principle", "Open for extension, closed for modification."),
           ("Extension point", "A place designed for new cases to plug in."),
           ("Registry", "A lookup from a key to an implementation."),
           ("Polymorphism", "Calling one interface that many implementations satisfy."),
           ("Speculative generality", "Flexibility added for changes that never come."),
           ("Rule of three", "Abstract when the same change appears the third time.")],
    code=dict(file="shipping.ts", note="a registry instead of a switch", src="""
type RateFn = (order: Order) => Money;

const carriers = new Map<CarrierId, RateFn>();
export const registerCarrier = (id: CarrierId, fn: RateFn) => carriers.set(id, fn);

export function shippingCost(order: Order): Money {
  const rate = carriers.get(order.carrier);
  if (!rate) throw new Error(`Unknown carrier ${order.carrier}`);
  return rate(order);
}

// carriers/bike.ts  — added without touching anything above
registerCarrier("bike", (o) => o.distanceKm <= 5 ? Money.eur(4) : Money.eur(9));
"""),
    tools="tools: plain maps and functions, dependency-injection containers with multi-bindings, plug-in systems (webpack and ESLint plug-ins are the same idea), and feature flags for switching implementations.",
    gains=["<b>New cases without editing</b> old ones.",
           "<b>Smaller, safer changes</b> and reviews.",
           "<b>Parallel work</b> on different cases.",
           "<b>Each case tested alone</b>."],
    losses=["<b>Indirection</b>: harder to see all cases at once.",
            "<b>Wrong guesses</b> about where change happens.",
            "<b>More files</b>.",
            "<b>Registration</b> can be forgotten."],
    baseline="Each line compares <b>a switch statement edited for every new case</b> to <b>a registry of small modules with one shape</b>.",
    ratings=[(4, 3, "One switch is easier to scan than a registry."),
             (3, 4, "Each carrier's rules sit in its own named module."),
             (3, 4, "Adding a case can't break others by accident."),
             (2, 5, "New cases are new files."),
             (3, 4, "Each case tested alone."),
             (2, 4, "The core doesn't know any carrier."),
             (3, 3, "Neutral."),
             (4, 3, "A type, a registry and a file per case."),
             (2, 4, "Teams add cases without editing shared code.")],
    pitfalls=[("Everything pluggable", "Interfaces for code that has one implementation forever.", "wait for the second or third real case."),
              ("Inheritance trees", "A deep class hierarchy to add one rule.", "functions or small interfaces and composition."),
              ("Silent missing registration", "A new carrier isn't registered and orders fail at runtime.", "fail loudly on unknown keys, and test the registry."),
              ("A switch in disguise", "The registry is fine, but callers still branch on carrier.", "push carrier-specific logic into the carrier module.")],
    use=["The same kind of change keeps arriving (carriers, payment methods, formats).",
         "Several teams add cases to the same feature.",
         "A growing switch keeps breaking."],
    skip=["Code with one case and no sign of more.",
          "A small, stable switch that's clearer than a registry."],
    related=["<b>Strategy &amp; Command as Functions</b>", "<b>Liskov Substitution</b>", "<b>Dependency Inversion</b>", "<b>Feature Flags</b> (Vol. 6)"],
    quiz=[("What does open–closed mean?", "Add behaviour by adding code, without modifying code that already works."),
          ("How was it usually done in 1988–1996, and how today?", "Then through inheritance and abstract classes; today mostly through functions, maps and small interfaces."),
          ("When should you add an extension point?", "When the same kind of change has come two or three times, not in advance."),
          ("What's speculative generality?", "Flexibility built for changes that never arrive, which adds cost without benefit.")],
    quiz_sit=[("A new developer proposes an abstract <code>ReportGenerator</code> with a factory and three subclasses, for the one CSV export the product has. What do you say?",
               "Keep the single concrete export. Add an extension point when a second or third format is actually requested; until then the abstraction is speculative.")],
    try_it="Find a switch or if-chain in your code that has been edited for each new case. Replace it with a map from key to function, move two cases into their own modules, and add a test that fails on an unknown key.",
    then_now=dict(src="Meyer, 1988; Martin, 1996", verdict="rethought",
                  then="Meyer meant extension through inheritance: subclass a module instead of editing it. Martin reframed it around abstract interfaces and polymorphism, which in C++ and Java meant class hierarchies.",
                  now="The goal holds, the means changed: functions, maps, composition and plug-in registries. Experience also added a warning: predicting where change will come often fails, so extension points are added when change actually repeats.",
                  take="Rethought: aim for “add, don't edit” where change repeats, with functions instead of inheritance."),
    remember="Plug in a <span class=\"hl\">new kettle</span>; don't <span class=\"hl\">rewire the house</span>.",
    sources=["Bertrand Meyer, <i>Object-Oriented Software Construction</i> (1988).",
             "Robert C. Martin, “The Open-Closed Principle” (C++ Report, 1996).",
             "Martin Fowler, <i>Refactoring</i>, 2nd ed. (2018), “Speculative Generality” and “Replace Conditional with Polymorphism”.",
             "Kent Beck, <i>Tidy First?</i> (2023)."],
)

# ------------------------------------------------------------------ 03 Liskov Substitution
ls_problem = Doodle(760, 260, "Doodle of a subtype that breaks its promise. Checkout accepts any Cart and calls add on it. A ReadOnlyCart extends Cart for saved wish lists, but its add method throws an error. When a wish list reaches checkout, the app crashes. The code compiled fine.",
                    "ReadOnlyCart “is a” Cart, but its add() throws; checkout crashes on a wish list.")
ls_problem.box(20, 40, 220, 80, "checkout(cart)", "blue", sub="calls cart.add()")
ls_problem.box(300, 20, 200, 60, "Cart", "paper", sub="add() works", size=18)
ls_problem.box(300, 120, 200, 60, "ReadOnlyCart", "pink", stroke="red", sub="add() throws!", size=17)
ls_problem.arrow(400, 116, 400, 84, dash=True)
ls_problem.arrow(244, 80, 296, 140, color="red")
ls_problem.note(620, 110, "compiles fine", "pen")
ls_problem.note(620, 140, "crashes at runtime", "red")
ls_problem.note(380, 230, "the subtype broke a promise the parent made", "red")

ls_analogy = Doodle(760, 250, "Doodle of a substitute teacher. When the regular teacher is ill, the substitute must be able to teach from the same lesson plan, take the register, and follow the school rules. A substitute who only takes questions in French, or refuses to mark homework, isn't a substitute: the class plan breaks.",
                    "A substitute teacher must keep the class plan working. One who refuses half of it isn't a substitute.")
ls_analogy.box(20, 50, 220, 90, "teacher", "green", sub="the lesson plan")
ls_analogy.box(270, 50, 220, 90, "good substitute", "green", sub="same plan works")
ls_analogy.box(520, 50, 220, 90, "bad substitute", "pink", stroke="red", sub="“no marking”")
ls_analogy.note(380, 200, "the class shouldn't notice the swap", "pen")

ls_how = Doodle(760, 300, "Fixing the hierarchy. Instead of ReadOnlyCart extending Cart, split the abilities: a CartView interface with lines and total that both a cart and a wish list satisfy, and an EditableCart with add and remove that only real carts implement. Checkout asks for EditableCart; the wish list page asks for CartView. A shared contract test runs against every implementation.",
                 "Split by ability: everything can be viewed, only real carts can be edited. One contract test for all.")
ls_how.box(270, 20, 220, 70, "CartView", "y", sub="lines · total")
ls_how.box(40, 160, 220, 70, "EditableCart", "green", sub="+ add · remove")
ls_how.box(500, 160, 220, 70, "WishList", "blue", sub="view only")
ls_how.arrow(150, 156, 330, 94, dash=True)
ls_how.arrow(610, 156, 430, 94, dash=True)
ls_how.note(150, 270, "checkout asks for this", "green")
ls_how.note(610, 270, "wish-list page uses this", "pen")

LSP = dict(
    slug="liskov-substitution",
    kicker="a.k.a. “the substitute teacher must follow the plan”",
    tldr="If code works with a type, it must keep working with <b>any subtype or implementation</b> of it. A subtype may not <b>demand more</b> (stricter inputs) or <b>promise less</b> (weaker results, new exceptions) than its parent. When an implementation can't keep a promise, it isn't really that type: <b>split the interface</b> by ability instead of throwing “not supported”.",
    chips=[("Family", "SOLID principle"), ("From", "Barbara Liskov (1987); Liskov &amp; Wing (1994)"), ("Applies to", "subclasses, interfaces, API versions"), ("Check with", "contract tests")],
    problem="""  <p class="lead">A subtype that quietly <span class="hl-pink">breaks a promise</span> of its parent compiles fine and <span class="hl-pink">fails at runtime</span>, far from where it was written.</p>
  <ul>
    <li><code>ReadOnlyCart extends Cart</code>, but <code>add()</code> throws.</li>
    <li>A cached repository returns stale data where callers expect fresh.</li>
    <li>Callers fill up with <code>if (x instanceof …)</code> checks.</li>
  </ul>""",
    problem_figs=[ls_problem],
    analogy_side="the substitute teacher",
    analogy="""  <p>When a teacher is ill, the <b>substitute</b> must teach from the same plan, take the register and mark homework. One who only answers in French or refuses to mark isn't really a substitute: the class plan breaks.</p>
  <ul>
    <li>The lesson plan is the <b>contract</b>.</li>
    <li>A good substitute is a <b>proper subtype</b>.</li>
    <li>The class shouldn't notice the swap.</li>
  </ul>""",
    analogy_figs=[ls_analogy],
    map=[("The lesson plan", "The parent type's contract"),
         ("The substitute", "A subclass or another implementation"),
         ("“I don't mark homework”", "<code>throw new Error('not supported')</code>"),
         ("Class notices the swap", "Callers need <code>instanceof</code> checks"),
         ("Hire a different role", "Split the interface by ability")],
    how_side="keep the promises, or split the type",
    how="""  <p>The rules: <b>preconditions</b> can't be stronger, <b>postconditions</b> can't be weaker, <b>invariants</b> must hold, and no <b>new exceptions</b> callers don't expect. It applies to interface implementations and to API versions too.</p>""",
    how_figs=[ls_how],
    steps=[("Write the contract down", "What does the type accept, return and promise? Comments, types and tests."),
           ("Check each implementation", "Does it accept everything the parent accepts and return what the parent promises?"),
           ("Watch for “not supported”", "An implementation that throws for part of the interface is a sign of a wrong type."),
           ("Split by ability", "Separate interfaces for what different implementations really can do."),
           ("Prefer composition", "Reuse code by holding an object, not by inheriting one you can't fully honour."),
           ("Run one contract test for all", "The same test suite against every implementation.")],
    vocab=[("Liskov substitution principle", "Subtypes must be usable wherever their base type is expected."),
           ("Precondition", "What must be true before calling: a subtype can't demand more."),
           ("Postcondition", "What's true after: a subtype can't promise less."),
           ("Invariant", "What's always true about the object."),
           ("Contract test", "A test suite every implementation of an interface must pass."),
           ("Refused bequest", "A subclass that doesn't want what it inherits: a hint of the wrong hierarchy.")],
    code=dict(file="cart.contract.test.ts", note="one contract, every implementation", src="""
export interface CartView     { lines(): readonly Line[]; total(): Money }
export interface EditableCart extends CartView { add(p: ProductId, q: Quantity): void }

// every EditableCart must pass this, whatever its storage
export function editableCartContract(make: () => EditableCart) {
  test("adding a product increases the total", () => {
    const cart = make();
    const before = cart.total();
    cart.add(productId("BIKE-42"), Quantity.of(1));
    expect(cart.total().cents).toBeGreaterThan(before.cents);
  });
}

describe("InMemoryCart", () => editableCartContract(() => new InMemoryCart()));
describe("RedisCart",    () => editableCartContract(() => new RedisCart(testRedis)));
"""),
    tools="tools: shared contract test suites, TypeScript and Kotlin type checkers (they check signatures, not behaviour), property-based tests that run the same properties against each implementation, and consumer contract tests for API versions.",
    gains=["<b>Safe substitution</b>: swap implementations without surprises.",
           "<b>No type checks</b> scattered through callers.",
           "<b>Honest types</b>: they say what things can do.",
           "<b>Reusable tests</b> across implementations."],
    losses=["<b>More, smaller interfaces</b>.",
            "<b>Contracts take thought</b> to write down.",
            "<b>Reworking hierarchies</b> that already exist.",
            "<b>Behaviour isn't checked</b> by compilers alone."],
    baseline="Each line compares <b>subtypes that sometimes refuse or change their parent's promises</b> to <b>types split by ability, checked by contract tests</b>.",
    ratings=[(3, 4, "No surprises when swapping."),
             (3, 4, "Types say what things can really do."),
             (2, 5, "The point: substitutes keep every promise."),
             (3, 4, "New implementations slot in safely."),
             (3, 5, "One contract suite for all implementations."),
             (3, 4, "Callers depend on the contract, not the concrete class."),
             (3, 3, "Neutral."),
             (3, 3, "More interfaces, fewer type checks."),
             (3, 4, "Teams can add implementations without breaking callers.")],
    pitfalls=[("“Not supported” methods", "An implementation throws for half the interface.", "split the interface by ability."),
              ("Inheriting for reuse", "A class extends another only to reuse a few methods.", "compose: hold the other object instead."),
              ("Stricter inputs in a subtype", "The subclass rejects values the parent accepts.", "accept at least what the parent accepts."),
              ("Trusting the compiler", "Signatures match, so it “must” be fine.", "contract tests check behaviour, not just types.")],
    use=["Designing interfaces with several implementations (storage, payment, carriers).",
         "Class hierarchies where callers check concrete types.",
         "Versioning an API that old clients still call."],
    skip=["There's only one implementation and no hierarchy.",
          "Internal test doubles that deliberately do less (keep them in tests)."],
    related=["<b>Interface Segregation</b>", "<b>Open–Closed</b>", "<b>Contract Testing</b> (Vol. 4)", "<b>Fakes</b> (Vol. 4)"],
    quiz=[("State the Liskov substitution principle simply.", "Code that works with a type must keep working with any of its subtypes or implementations."),
          ("Can a subtype require stricter inputs than its parent?", "No: preconditions may not be strengthened."),
          ("What does a method that throws “not supported” suggest?", "The type is wrong: the implementation can't honour the contract, so split the interface."),
          ("How do you check behaviour across implementations?", "A shared contract test suite run against each one.")],
    quiz_sit=[("Your <code>FileStorage</code> interface has <code>delete()</code>, and the new archive storage throws “archives are immutable” on delete. A cleanup job crashed overnight. What do you change?",
               "Split the interface: a readable/writable storage for everything, and a deletable one only for storages that support it. The cleanup job asks for the deletable kind, so the archive can't be passed to it. Add a contract test for each interface.")],
    try_it="Pick an interface with two or more implementations in your code. Write three contract tests describing what every implementation must do, run them against each, and fix or split whatever fails.",
    then_now=dict(src="Liskov, 1987; Liskov &amp; Wing, 1994", verdict="core",
                  then="Liskov's 1987 keynote defined behavioural subtyping; with Wing (1994) it became precise rules about preconditions, postconditions and invariants. Martin made it the “L” in SOLID, mostly about class hierarchies.",
                  now="Deep inheritance is rarer, but the principle applies equally to interface implementations, plug-ins, mocks and API versions. Contract tests and consumer-driven contracts are the practical tools.",
                  take="Still core. It's the most precise of the five, and the least fashion-dependent."),
    remember="A good <span class=\"hl\">substitute</span> follows the <span class=\"hl\">whole lesson plan</span>.",
    sources=["Barbara Liskov, “Data Abstraction and Hierarchy” (OOPSLA keynote, 1987).",
             "Barbara Liskov &amp; Jeannette Wing, “A Behavioral Notion of Subtyping” (1994).",
             "Robert C. Martin, “The Liskov Substitution Principle” (C++ Report, 1996).",
             "Bertrand Meyer, <i>Object-Oriented Software Construction</i>, 2nd ed. (1997), Design by Contract."],
)

# ------------------------------------------------------------------ 04 Interface Segregation
is_problem = Doodle(760, 260, "Doodle of a fat PaymentGateway interface with fourteen methods: charge, refund, payout, dispute, report and more. Checkout only uses charge, but depends on all fourteen. Every test fake must implement fourteen methods. When payouts change signature, checkout must be rebuilt and redeployed.",
                    "Checkout uses one method of a 14-method interface, and is rebuilt every time payouts change.")
is_problem.table(270, 20, "PaymentGateway", ["charge()", "refund()", "payout()", "dispute()", "… 10 more"], w=220, fill="pink", stroke="red")
is_problem.box(20, 60, 200, 70, "checkout", "blue", sub="uses 1 of 14")
is_problem.arrow(224, 95, 266, 95, color="red")
is_problem.note(630, 80, "fakes: 14 methods each", "red")
is_problem.note(630, 120, "payouts change →", "red")
is_problem.note(630, 150, "checkout redeploys", "red")

is_analogy = Doodle(760, 250, "Doodle of two remote controls. A universal remote has sixty buttons for TV, DVD, satellite and lights; a guest can't find the volume. A simple remote has power, volume and channel, exactly what most people need. The TV supports both, but each person gets the remote for their job.",
                    "A 60-button universal remote vs a simple one with power, volume and channel.")
is_analogy.box(60, 30, 200, 170, None, "pink", stroke="red")
is_analogy.head(160, 64, "60 buttons")
for r in range(3):
    for c in range(5):
        is_analogy.circle(92 + c * 34, 100 + r * 32, 9)
is_analogy.box(480, 50, 200, 130, None, "green")
is_analogy.head(580, 84, "3 buttons")
is_analogy.text(580, 124, "power · volume")
is_analogy.text(580, 156, "channel")
is_analogy.note(380, 230, "give each user the remote for their job", "pen")

is_how = Doodle(760, 300, "The gateway split into role interfaces: ChargePayments with charge, Refunds with refund, and Payouts with payout. The Stripe adapter implements all three. Checkout depends only on ChargePayments, the returns flow on Refunds, the finance job on Payouts. Each test fake implements one small interface.",
                 "Small role interfaces; one adapter implements them all; each client depends on just its role.")
is_how.box(270, 210, 220, 70, "StripeAdapter", "y", sub="implements all three")
for i, (role, client) in enumerate([("ChargePayments", "checkout"), ("Refunds", "returns"), ("Payouts", "finance job")]):
    x = 20 + i * 250
    is_how.box(x, 100, 220, 60, role, "green", size=17)
    is_how.box(x, 20, 220, 50, client, "paper", size=16)
    is_how.arrow(x + 110, 74, x + 110, 96)
    is_how.arrow(380, 206, x + 110, 164, dash=True)

ISP = dict(
    slug="interface-segregation",
    kicker="a.k.a. “give each user the remote for their job”",
    tldr="Clients shouldn't depend on methods they <b>don't use</b>. Instead of one fat interface (a 14-method <code>PaymentGateway</code>), define small <b>role interfaces</b> shaped by each client's needs (<code>ChargePayments</code>, <code>Refunds</code>, <code>Payouts</code>). One class can implement several. Clients get <b>simpler fakes</b>, and changes to one role <b>don't ripple</b> to the others.",
    chips=[("Family", "SOLID principle"), ("From", "Robert C. Martin (1996, at Xerox)"), ("Today", "role interfaces, structural types"), ("Pairs with", "dependency inversion, test doubles")],
    problem="""  <p class="lead">A <span class="hl-pink">fat interface</span> couples every client to every method, even the ones it never calls.</p>
  <ul>
    <li>Checkout depends on a 14-method gateway but uses one method.</li>
    <li>Every fake in every test implements all 14.</li>
    <li>A change to payouts forces checkout to rebuild and redeploy.</li>
  </ul>""",
    problem_figs=[is_problem],
    analogy_side="the remote control",
    analogy="""  <p>A <b>universal remote</b> with sixty buttons controls everything, and a guest can't find the volume. A <b>simple remote</b> with power, volume and channel does what most people need. The TV supports both; each person gets the remote for their job.</p>
  <ul>
    <li>The TV is the <b>implementation</b>.</li>
    <li>Each remote is a <b>role interface</b>.</li>
  </ul>""",
    analogy_figs=[is_analogy],
    map=[("The TV", "The Stripe adapter that can do everything"),
         ("Universal remote", "A fat <code>PaymentGateway</code> interface"),
         ("Simple remote", "<code>ChargePayments</code> with one method"),
         ("Guest can't find volume", "Clients and tests burdened by unused methods"),
         ("One TV, several remotes", "One class implementing several role interfaces")],
    how_side="interfaces shaped by their clients",
    how="""  <p>Let the <b>client</b> define the interface it needs, in its own words: that's also what dependency inversion asks. In TypeScript and Go, structural typing makes this almost free: any object with the right methods fits.</p>""",
    how_figs=[is_how],
    steps=[("List each client's calls", "Which methods does each user of the interface actually call?"),
           ("Group by role", "Methods used together by the same kind of client form a role."),
           ("Define small interfaces", "Named after the role, owned near the client."),
           ("Implement several in one class", "The adapter can implement all roles."),
           ("Narrow dependencies", "Each client asks for the smallest role it needs."),
           ("Simplify fakes", "Tests fake one small role, not the whole gateway.")],
    vocab=[("Interface segregation principle", "No client should be forced to depend on methods it doesn't use."),
           ("Role interface", "An interface describing one role a client needs."),
           ("Header interface", "An interface that mirrors every public method of one class: usually too fat."),
           ("Structural typing", "Type compatibility by shape, as in TypeScript and Go."),
           ("<code>Pick&lt;T, K&gt;</code>", "TypeScript helper to take just some members of a type."),
           ("Fat interface", "One interface serving many unrelated clients.")],
    code=dict(file="payments.ts", note="role interfaces, owned by their clients", src="""
// checkout/ports.ts
export interface ChargePayments { charge(amount: Money, card: CardToken): Promise<ChargeId> }

// returns/ports.ts
export interface Refunds { refund(charge: ChargeId, amount: Money): Promise<void> }

// infrastructure/stripe.ts : one adapter, several roles
export class StripeAdapter implements ChargePayments, Refunds, Payouts { /* ... */ }

// a test fake now needs one method, not fourteen
const fakeCharge: ChargePayments = { charge: async () => chargeId("ch_test_1") };
"""),
    tools="tools: TypeScript and Go structural typing, <code>Pick</code> and <code>Omit</code> types, Kotlin and C# interfaces, mocking libraries (which become simpler with small interfaces).",
    gains=["<b>Smaller dependencies</b> per client.",
           "<b>Simpler fakes</b> in tests.",
           "<b>Changes don't ripple</b> across unrelated clients.",
           "<b>Clear roles</b> named in client terms."],
    losses=["<b>More interfaces</b> to name and find.",
            "<b>Too fine-grained</b> if split per method everywhere.",
            "<b>Implementations</b> list several interfaces.",
            "<b>Navigation</b>: where's the full picture?"],
    baseline="Each line compares <b>one fat interface shared by every client</b> to <b>small role interfaces shaped by each client</b>.",
    ratings=[(3, 4, "Each client sees only what it uses."),
             (3, 4, "Roles named after what clients do."),
             (3, 3, "Neutral."),
             (2, 4, "A change to one role leaves others alone."),
             (2, 5, "Fakes implement one small interface."),
             (2, 5, "Clients depend on a sliver, not the whole."),
             (3, 3, "Neutral."),
             (3, 3, "More interfaces, simpler fakes."),
             (3, 4, "Teams own their own role interfaces.")],
    pitfalls=[("One interface per method", "Fifty single-method interfaces nobody can navigate.", "group methods used together by the same client."),
              ("Header interfaces", "<code>IOrderService</code> mirroring every public method of OrderService.", "define interfaces from the client's side."),
              ("Splitting but still passing the whole", "Small interfaces exist, but functions still take the concrete class.", "ask for the smallest role in each signature."),
              ("Ignoring language features", "Writing adapter classes to narrow interfaces in TypeScript.", "structural types and <code>Pick</code> do it for free.")],
    use=["An interface with many methods and many different clients.",
         "Tests that need large fakes for small uses.",
         "Changes in one area forcing rebuilds elsewhere."],
    skip=["An interface with one client that uses all of it.",
          "Small interfaces already (3–5 methods used together)."],
    related=["<b>Dependency Inversion</b>", "<b>Liskov Substitution</b>", "<b>Single Responsibility</b>", "<b>Test Doubles</b> (Vol. 4)"],
    quiz=[("What does interface segregation say?", "No client should depend on methods it doesn't use."),
          ("What's a role interface?", "A small interface describing one role a client needs, often owned by that client."),
          ("Can one class implement several role interfaces?", "Yes, and that's typical: one adapter, several roles."),
          ("How does this help tests?", "Fakes implement only the small role the code under test uses.")],
    quiz_sit=[("Every unit test in your service creates a mock of <code>ICustomerService</code>, which has 22 methods; most tests stub one. Mocks break whenever a method is added. What do you change?",
               "Introduce role interfaces from the callers' side (for example <code>CustomerLookup</code>, <code>CustomerCredit</code>), make each caller depend on its role, and let the existing service implement them. Tests then fake one or two methods.")],
    try_it="Pick the largest interface in your code and list which methods each caller uses. Define one role interface for the most common caller, switch that caller to it, and rewrite one of its tests with a hand-written fake.",
    then_now=dict(src="Martin, 1996", verdict="core",
                  then="Martin found it at Xerox, where a single Job class used by every printer task made every change recompile everything. In C++ and Java, splitting interfaces was the way to cut compile and deploy coupling.",
                  now="Compile times matter less, but the coupling, the fakes and the deploy ripple are the same. Structural typing in TypeScript and Go made role interfaces nearly free, and the idea reappears in API design (small, focused endpoints) and micro-frontends.",
                  take="Still core, and cheaper to apply than ever."),
    remember="Give each user the <span class=\"hl\">remote for their job</span>, not the <span class=\"hl\">sixty-button</span> one.",
    sources=["Robert C. Martin, “The Interface Segregation Principle” (C++ Report, 1996).",
             "Robert C. Martin, <i>Agile Software Development</i> (2002), ch. 12.",
             "Martin Fowler, “RoleInterface” (bliki, 2006).",
             "TypeScript Handbook, “Type Compatibility”."],
)

# ------------------------------------------------------------------ 05 Dependency Inversion
di_problem = Doodle(760, 260, "Doodle of business code that builds its own infrastructure. PlaceOrder creates a new Postgres client and a new Stripe client inside its method. Tests can't run without a database and a Stripe sandbox. Switching to another payment provider means editing the business rule itself.",
                    "PlaceOrder creates its own Postgres and Stripe clients: no tests without both, no switching without rewriting.")
di_problem.box(250, 40, 260, 110, None, "pink", stroke="red")
di_problem.head(380, 74, "PlaceOrder")
di_problem.text(380, 108, "new PostgresClient()")
di_problem.text(380, 136, "new StripeClient()")
di_problem.box(20, 60, 180, 60, "Postgres", "paper", size=17)
di_problem.box(560, 60, 180, 60, "Stripe", "paper", size=17)
di_problem.arrow(246, 90, 204, 90, color="red")
di_problem.arrow(514, 90, 556, 90, color="red")
di_problem.note(380, 210, "the business rule depends on the plumbing", "red")

di_analogy = Doodle(760, 250, "Doodle of a lamp and the power grid. The lamp doesn't depend on a particular power station; both the lamp and the grid depend on the standard plug and socket. The country can switch from coal to wind without changing a single lamp.",
                     "The lamp and the grid both depend on the plug standard, so the grid can change without touching lamps.")
di_analogy.box(20, 60, 180, 90, "lamp", "y", sub="needs power")
di_analogy.box(290, 60, 180, 90, "plug standard", "green", sub="the agreement")
di_analogy.box(560, 60, 180, 90, "power grid", "blue", sub="coal → wind")
di_analogy.arrow(204, 105, 286, 105)
di_analogy.arrow(556, 105, 474, 105)
di_analogy.note(380, 210, "both point at the standard, not at each other", "pen")

di_how = Doodle(760, 320, "Inverted dependencies. The ordering core defines two ports in its own words: OrderRepository and PaymentPort. A Postgres adapter and a Stripe adapter in the infrastructure layer implement them, so the arrows point inward from infrastructure to the core. A composition root at start-up creates the adapters and passes them in. Tests pass in-memory fakes instead.",
                 "The core owns the interfaces; adapters implement them; arrows point inward; start-up wires it.")
di_how.box(250, 30, 260, 160, None, "y", dash=True)
di_how.head(380, 62, "ordering core")
di_how.box(270, 82, 220, 40, "PaymentPort", "green", size=16)
di_how.box(270, 134, 220, 40, "OrderRepository", "green", size=16)
di_how.box(20, 80, 190, 60, "StripeAdapter", "blue", size=16)
di_how.box(550, 80, 190, 60, "PostgresOrders", "blue", size=16)
di_how.arrow(214, 105, 266, 102)
di_how.arrow(546, 112, 494, 152)
di_how.box(250, 240, 260, 56, "composition root", "paper", sub="wires it at start-up", size=16, subsize=13)
di_how.note(115, 200, "tests: in-memory fakes", "green")

DIP = dict(
    slug="dependency-inversion",
    kicker="a.k.a. “both depend on the plug, not on each other”",
    tldr="High-level business code shouldn't depend on low-level details like databases, HTTP clients or SDKs. <b>Both</b> should depend on an <b>abstraction</b>, and the abstraction belongs to the <b>business side</b>: the core defines <code>PaymentPort</code> in its own words, and a Stripe adapter implements it. Dependencies point <b>inward</b>; a <b>composition root</b> wires real adapters at start-up, tests wire fakes.",
    chips=[("Family", "SOLID principle"), ("From", "Robert C. Martin (1996)"), ("Not the same as", "a DI container"), ("Pairs with", "ports &amp; adapters, interface segregation")],
    problem="""  <p class="lead">When business rules <span class="hl-pink">create and call infrastructure directly</span>, they can't be tested or changed without it.</p>
  <ul>
    <li><code>PlaceOrder</code> news up a database client and a payment SDK.</li>
    <li>Unit tests need a database and a sandbox account.</li>
    <li>Changing payment provider means editing business code.</li>
  </ul>""",
    problem_figs=[di_problem],
    analogy_side="the lamp and the grid",
    analogy="""  <p>A <b>lamp</b> doesn't depend on a particular power station. The lamp and the grid both depend on the <b>plug standard</b>. The country can move from coal to wind without changing a single lamp, and you can test a lamp with a battery.</p>
  <ul>
    <li>The lamp is the <b>business core</b>.</li>
    <li>The plug standard is the <b>port</b> (interface).</li>
    <li>The grid is an <b>adapter</b>; the battery is a <b>fake</b>.</li>
  </ul>""",
    analogy_figs=[di_analogy],
    map=[("The lamp", "PlaceOrder: the business use case"),
         ("The plug standard", "<code>PaymentPort</code>, defined by the core"),
         ("The power grid", "<code>StripeAdapter</code>"),
         ("Testing with a battery", "An in-memory fake in tests"),
         ("Switching coal to wind", "Swapping Stripe for another provider in one adapter")],
    how_side="the core owns the interfaces",
    how="""  <p>“Inversion” means the interface <b>moves</b>: not <code>StripeClient</code>'s own interface, but one the core writes in its language. A DI <b>container</b> is optional; a plain function that wires objects at start-up does the same job.</p>""",
    how_figs=[di_how],
    steps=[("Find direct infrastructure calls", "<code>new</code> of clients, SDK imports and SQL inside business code."),
           ("Write a port in the core's words", "<code>PaymentPort.charge(amount, card)</code>, not Stripe's API shape."),
           ("Implement it in an adapter", "The Stripe code lives in infrastructure and implements the port."),
           ("Inject through the constructor", "The use case receives the port; it never creates it."),
           ("Wire at the composition root", "One place at start-up builds real adapters; tests build fakes."),
           ("Guard the direction", "An architecture test forbids core imports of infrastructure.")],
    vocab=[("Dependency inversion principle", "High-level modules don't depend on low-level ones; both depend on abstractions owned by the high level."),
           ("Port", "An interface the core defines for what it needs."),
           ("Adapter", "An implementation of a port using a real technology."),
           ("Dependency injection", "Passing dependencies in instead of creating them."),
           ("Composition root", "The one place where the object graph is assembled."),
           ("DI container", "A library that automates the composition root; optional.")],
    code=dict(file="place-order.ts", note="the core owns the port; start-up wires it", src="""
// core/ports.ts : in the core's words
export interface PaymentPort { charge(amount: Money, card: CardToken): Promise<ChargeId> }

// core/place-order.ts
export class PlaceOrder {
  constructor(private orders: OrderRepository, private payments: PaymentPort) {}
  async handle(cmd: PlaceOrderCommand) {
    const order = await this.orders.get(cmd.orderId);
    await this.payments.charge(order.total(), cmd.card);
    order.place(new Date());
    await this.orders.save(order);
  }
}

// main.ts : composition root
const placeOrder = new PlaceOrder(new PostgresOrders(db), new StripeAdapter(stripeKey));
// test: new PlaceOrder(new InMemoryOrders(), { charge: async () => chargeId("ch_1") })
"""),
    tools="tools: plain constructor injection and a hand-written composition root, or containers like NestJS DI, InversifyJS, .NET's built-in container, Spring; ArchUnit or dependency-cruiser to keep imports pointing inward.",
    gains=["<b>Business rules testable</b> without infrastructure.",
           "<b>Infrastructure swappable</b> in one adapter.",
           "<b>Ports in the business's words</b>.",
           "<b>Clear direction</b> of dependencies."],
    losses=["<b>More interfaces</b> and wiring code.",
            "<b>Indirection</b> when reading.",
            "<b>Over-abstraction</b> of things that never change.",
            "<b>Container magic</b> if a framework is overused."],
    baseline="Each line compares <b>business code that creates and calls infrastructure directly</b> to <b>a core that owns its ports, with adapters injected</b>.",
    ratings=[(3, 3, "Clearer core, plus wiring to follow."),
             (3, 4, "Ports speak the core's language."),
             (3, 3, "Neutral."),
             (2, 4, "Infrastructure changes stay in adapters."),
             (2, 5, "Core tests use fakes, in milliseconds."),
             (1, 5, "The point: the core knows no infrastructure."),
             (3, 3, "Neutral."),
             (4, 3, "Interfaces and a composition root."),
             (2, 4, "Core and adapter work can happen in parallel.")],
    pitfalls=[("Ports shaped like the vendor", "<code>PaymentPort</code> copies Stripe's API, so switching still hurts.", "write the port from the core's needs."),
              ("Interfaces for everything", "An interface for a pure helper with one implementation.", "invert only dependencies on infrastructure or volatile code."),
              ("Service locator", "Code calls <code>container.get(PaymentPort)</code> deep inside.", "constructor injection, wired at the composition root."),
              ("Wrong direction creeping back", "A core file imports an ORM type “just once”.", "an architecture test fails the build.")],
    use=["Business rules that call databases, APIs or SDKs.",
         "You want fast tests of the core.",
         "Infrastructure that may change (providers, storage)."],
    skip=["Small scripts and CRUD apps where the framework is the app.",
          "Pure, stable libraries (no need to hide <code>Math</code>)."],
    related=["<b>Ports &amp; Adapters</b>", "<b>Interface Segregation</b>", "<b>Adapter &amp; Facade</b>", "<b>Repository</b> (Vol. 7)", "<b>Anti-Corruption Layer</b> (Vol. 7)"],
    quiz=[("What is “inverted” in dependency inversion?", "Ownership of the interface: the high-level core defines it, and low-level code depends on it."),
          ("Is a DI container required?", "No. A composition root that wires objects by hand applies the principle just as well."),
          ("What's a composition root?", "The single place at start-up where real implementations are created and passed in."),
          ("Why shouldn't a port copy the vendor's API?", "Then the core still depends on that vendor's shape, and switching still means changing the core.")],
    quiz_sit=[("Your use cases import <code>@prisma/client</code> types directly, and unit tests spin up a real database, taking 9 minutes. What do you change first?",
               "Define repository ports in the core's own types, implement them with Prisma in an adapter, inject them into the use cases, and give tests in-memory implementations. Add an import rule so the core can't import Prisma again.")],
    try_it="Find one place where business code creates an infrastructure client with <code>new</code>. Define a port in business terms, move the client into an adapter, inject it, and write a test with a fake. Measure the test time before and after.",
    then_now=dict(src="Martin, 1996", verdict="grown",
                  then="Martin described it for C++ and Java layered systems: high-level policy shouldn't depend on low-level detail. It became the basis of DI frameworks like Spring (2003), which often hid it behind heavy configuration.",
                  now="It's the heart of hexagonal, onion and clean architecture, and of fast test suites. Lighter DI (constructor injection, hand-written composition roots) replaced XML-heavy containers, and architecture tests keep the direction honest.",
                  take="More important now: it's the principle under most modern application architectures."),
    remember="The lamp and the grid both depend on <span class=\"hl\">the plug</span>, and <span class=\"hl\">the lamp</span> wrote the standard.",
    sources=["Robert C. Martin, “The Dependency Inversion Principle” (C++ Report, 1996).",
             "Mark Seemann &amp; Steven van Deursen, <i>Dependency Injection Principles, Practices, and Patterns</i> (2019).",
             "Martin Fowler, “Inversion of Control Containers and the Dependency Injection pattern” (2004).",
             "Robert C. Martin, <i>Clean Architecture</i> (2017), ch. 11."],
)

NOTES = [SRP, OCP, LSP, ISP, DIP]
