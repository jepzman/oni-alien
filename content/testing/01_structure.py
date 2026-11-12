# Vol. 4 · Structure: Test Pyramid, Arrange–Act–Assert, Test Data Builders, Page Objects.

# ------------------------------------------------------------------ 01 Test Pyramid
tp_problem = Doodle(760, 260, "Doodle of an upside-down pyramid, an ice-cream cone. A huge scoop of slow end-to-end browser tests sits on top of a few integration tests and almost no unit tests. The suite takes 55 minutes and fails randomly, so developers merge without waiting.",
                    "The ice-cream cone: mostly slow browser tests, few fast ones. 55 minutes and flaky.")
tp_problem.raw('<path class="d f-pink" d="M60 40 h360 l-180 200 z"/>')
tp_problem.raw('<path class="d d-thin" d="M105 90 h270 M150 140 h180 M195 190 h90"/>')
tp_problem.head(240, 72, "end-to-end: 600", size=19)
tp_problem.text(240, 122, "integration: 80", size=17)
tp_problem.text(240, 172, "unit: 30", size=17)
tp_problem.icon("stopwatch", 500, 40, 1.1, color="red")
tp_problem.note(600, 70, "55 min per run", "red", anchor="start")
tp_problem.note(480, 150, "random failures → “re-run it”", "red", anchor="start")
tp_problem.note(480, 190, "red = “something, somewhere”", "red", anchor="start")

tp_analogy = Doodle(760, 260, "Doodle of a car factory. Every bolt and part is checked on a bench in seconds, assembled sections are checked on a rig, and only a few finished cars go on a full test drive. Nobody test-drives a car to find a faulty bolt.",
                    "A car factory: check every bolt on the bench, sections on a rig, and test-drive only a few finished cars.")
tp_analogy.icon("pyramid", 40, 40, 2.6, fill="y")
tp_analogy.note(330, 70, "1 · a few test drives (slow, real)", "pen", anchor="start")
tp_analogy.note(330, 130, "2 · sections on a test rig", "pen", anchor="start")
tp_analogy.note(330, 190, "3 · every bolt on the bench (seconds)", "green", anchor="start")
tp_analogy.note(330, 240, "nobody test-drives to find a bad bolt", "pen", anchor="start")

tp_how = Doodle(760, 300, "The test pyramid. A wide base of unit tests, about seventy percent, running in seconds. A middle band of integration tests that touch a real database or HTTP layer. A small top of end-to-end tests covering only the critical user journeys. Arrows show that higher layers are slower, costlier and more realistic, lower layers are faster and pinpoint failures.",
                "Lots of fast tests at the bottom, a few slow realistic ones at the top. Each layer catches what the one below can't.")
tp_how.raw('<path class="d f-green" d="M60 270 h420 l-60 -80 h-300 z"/>')
tp_how.raw('<path class="d f-y" d="M120 190 h300 l-60 -80 h-180 z"/>')
tp_how.raw('<path class="d f-pink" d="M180 110 h180 l-90 -100 z"/>')
tp_how.head(270, 240, "unit · ~70% · ms each", size=18)
tp_how.head(270, 158, "integration · ~20%", size=17)
tp_how.head(270, 92, "e2e · few", size=16)
tp_how.arrow(530, 260, 530, 30)
tp_how.note(548, 60, "slower, costlier,", "red", anchor="start")
tp_how.note(548, 86, "more realistic", "red", anchor="start")
tp_how.note(548, 230, "faster, pinpoints", "green", anchor="start")
tp_how.note(548, 256, "the fault", "green", anchor="start")

PYRAMID = dict(
    slug="test-pyramid",
    kicker="a.k.a. “bench, rig, test drive”",
    tldr="Write <b>lots of small, fast unit tests</b>, <b>fewer integration tests</b> that touch real boundaries (database, HTTP), and <b>only a handful of end-to-end tests</b> for the critical journeys. Push each check to the <b>lowest layer that can catch it</b>. You get a suite that runs in minutes, fails precisely, and still proves the whole thing works.",
    chips=[("Family", "test strategy"), ("Origin", "Mike Cohn, <i>Succeeding with Agile</i> (2009)"), ("Variants", "testing trophy, honeycomb"), ("Anti-pattern", "the ice-cream cone")],
    problem="""  <p class="lead">Browser tests feel like the most honest tests: they click what users click. So teams write <span class="hl-pink">hundreds of them</span>, and the suite turns into an <b>ice-cream cone</b>: slow, flaky, and vague about what broke.</p>
  <ul>
    <li>CI takes an hour, so people batch changes and merge without waiting.</li>
    <li>A failing end-to-end test could mean any of fifty causes.</li>
    <li>Random timeouts teach everyone to press “re-run”.</li>
  </ul>""",
    problem_figs=[tp_problem],
    analogy_side="the car factory",
    analogy="""  <p>A car factory checks <b>every bolt on a bench</b> in seconds, checks <b>assembled sections on a rig</b>, and sends only <b>a few finished cars</b> on a full test drive. If a test drive finds a problem, they add a bench check so it's caught earlier next time.</p>
  <ul>
    <li>Bench checks are <b>unit tests</b>: cheap, fast, precise.</li>
    <li>The rig is <b>integration tests</b>: real joints, fewer of them.</li>
    <li>The test drive is <b>end-to-end</b>: proof it all works together.</li>
  </ul>""",
    analogy_figs=[tp_analogy],
    map=[("A bolt on the bench", "A unit test of one function or class"),
         ("A section on a rig", "An integration test with a real database or HTTP layer"),
         ("A full test drive", "An end-to-end browser test of a user journey"),
         ("Finding a bad bolt on a drive", "Pushing that check down to a unit test"),
         ("Most checks on the bench", "Most tests at the bottom of the pyramid")],
    how_side="the right test at the right layer",
    how="""  <p>The shape matters more than exact percentages. Each layer exists to catch what the cheaper layer below <b>can't</b>, never to repeat it.</p>""",
    how_figs=[tp_how],
    steps=[("List the risks", "Business rules, data access, wiring, the critical user journeys."),
           ("Rules → unit tests", "Pricing, validation, state changes: pure functions and small classes, tested in milliseconds."),
           ("Boundaries → integration tests", "Queries against a real database, HTTP handlers, message consumers."),
           ("Journeys → a few end-to-end tests", "Sign up, checkout, payment: the paths that must never break."),
           ("Push bugs down", "When an e2e test catches a bug, add a lower-level test that would have caught it."),
           ("Watch the shape", "Track counts and run time per layer; a growing top is a smell.")],
    vocab=[("Unit test", "Tests one small piece in isolation, in milliseconds."),
           ("Integration test", "Tests a piece together with a real boundary."),
           ("End-to-end (e2e)", "Drives the whole running system like a user."),
           ("Ice-cream cone", "Inverted pyramid: mostly slow e2e tests."),
           ("Testing trophy", "A variant that favours integration tests."),
           ("Feedback loop", "Time from a change to knowing if it broke something.")],
    code=dict(file="package.json", note="one script per layer", src="""
{
  "scripts": {
    "test:unit":  "vitest run src --project unit",              // ~2,000 tests · 20 s
    "test:int":   "vitest run src --project integration",       // ~300 tests · 2 min
    "test:e2e":   "playwright test e2e/critical",               // ~25 tests · 6 min
    "test":       "npm run test:unit && npm run test:int"       // every push
  }
}
// CI: unit + integration on every push, e2e on merge to main and nightly
"""),
    tools="tools: Vitest and Jest (unit), Testcontainers and Supertest (integration), Playwright and Cypress (e2e). Kent C. Dodds's “testing trophy” and Spotify's “honeycomb” are variants for UI-heavy and microservice code.",
    gains=["<b>Fast feedback</b>: most failures show up in seconds.",
           "<b>Precise failures</b>: a red unit test points at one function.",
           "<b>Cheap to run</b> on every push.",
           "<b>Still realistic</b>: the top layer proves the journeys work."],
    losses=["<b>Unit tests can miss wiring bugs</b>: things pass alone, fail together.",
            "<b>Over-mocking temptation</b> to keep things “unit”.",
            "<b>Needs judgement</b> about which layer each test belongs to.",
            "<b>Several tools</b> and test setups to maintain."],
    baseline="Each line compares an <b>ice-cream cone</b> (mostly e2e tests) to a <b>pyramid-shaped suite</b> covering the same features.",
    ratings=[(3, 4, "Small tests are easy to read; e2e tests are long."),
             (1, 5, "Most checks run in milliseconds."),
             (4, 4, "The few e2e tests still prove the journeys."),
             (1, 4, "Far fewer timing-sensitive browser tests."),
             (1, 5, "A red unit test points at one place."),
             (2, 4, "Fewer brittle UI selectors to fix."),
             (5, 3, "Most tests no longer touch a real browser."),
             (2, 4, "CI minutes drop dramatically."),
             (1, 4, "Unit tests scale with the codebase; e2e count stays small.")],
    pitfalls=[("Mocking everything to stay “unit”", "Every collaborator is mocked; tests pass while the real wiring is broken.", "test boundaries with real integrations at the middle layer."),
              ("Duplicating checks at every layer", "The same validation is tested in unit, API and e2e tests.", "test each rule once, at the lowest layer that can see it."),
              ("Chasing percentages", "“We need exactly 70% unit tests.”", "aim for the shape, judge by speed and confidence."),
              ("No e2e at all", "Everything passes, but the login page is blank.", "keep a small set of critical-path journeys.")],
    use=["Almost any product with a growing codebase.",
         "Teams whose CI is slow or flaky.",
         "Business logic that can be tested without the UI."],
    skip=["Thin UI glue with no logic (prefer integration tests, the “trophy”).",
          "Tiny scripts where a couple of end-to-end checks are enough.",
          "Exploratory prototypes you'll throw away."],
    related=["<b>Arrange–Act–Assert</b>", "<b>Test doubles</b>", "<b>Throwaway containers</b>", "<b>Parallel &amp; selective runs</b>"],
    quiz=[("What's the ice-cream cone anti-pattern?", "A suite with mostly slow end-to-end tests and few unit tests: the pyramid upside down."),
          ("Where should a pricing rule be tested?", "In fast unit tests; the e2e layer only needs to show checkout works overall."),
          ("What should you do when an e2e test catches a bug?", "Add a lower-level test that would have caught it, so the next one fails faster and more precisely."),
          ("Why keep any e2e tests?", "They're the only layer that proves the whole system works together for real users.")],
    remember="Check every <span class=\"hl\">bolt</span> on the bench, and take only a <span class=\"hl\">few test drives</span>.",
    sources=["Mike Cohn, <i>Succeeding with Agile</i>, ch. 16 (2009).",
             "Ham Vocke, “The Practical Test Pyramid” (martinfowler.com).",
             "Kent C. Dodds, “The Testing Trophy and Testing Classifications”.",
             "Google Testing Blog, “Just Say No to More End-to-End Tests”."],
)

# ------------------------------------------------------------------ 02 Arrange–Act–Assert
aaa_problem = Doodle(760, 260, "Doodle of a messy 60-line test called test2. Setup, several actions and assertions are interleaved, with a comment saying do not touch. When it fails, nobody can tell what behaviour it was checking.",
                    "test2(): setup, actions and checks all tangled together. When it fails, what was it testing?")
aaa_problem.box(30, 20, 320, 220, None, "paper", rx=4)
for i, (t, c) in enumerate([("const u = makeUser()", ""), ("expect(u.id).toBeDefined()", "red"), ("cart.add(u, lamp)", ""), ("db.save(cart)", ""), ("expect(cart.total).toBe(20)", "red"), ("cart.applyCoupon('X')", ""), ("// do not touch!!", "red"), ("expect(…).toBe(16)", "red")]):
    aaa_problem.text(46, 46 + i * 25, t, "t" + (f" t-{c}" if c else ""), anchor="start", size=16)
aaa_problem.note(560, 60, "test2()", "red")
aaa_problem.note(560, 110, "act, check, act, check…", "red")
aaa_problem.note(560, 160, "fails: which part broke?", "red")
aaa_problem.note(560, 210, "what is it even testing?", "red")

aaa_analogy = Doodle(760, 250, "Doodle of a school science experiment write-up with three headed sections: Method, where you set up the equipment; Experiment, the one thing you change; Result, what you measured. A reader can follow any experiment at a glance.",
                    "A lab write-up: set up, do one thing, record the result. Same three headings every time.")
aaa_analogy.icon("flask", 40, 50, 2.0, fill="y")
for i, (t, sub, f) in enumerate([("Method", "set up the kit", "blue"), ("Experiment", "heat to 80 °C", "y"), ("Result", "turned blue ✓", "green")]):
    aaa_analogy.box(230 + i * 175, 70, 160, 90, t, f, sub=sub, size=19)
    if i:
        aaa_analogy.arrow(225 + i * 175 - 14, 115, 225 + i * 175, 115)
aaa_analogy.note(490, 210, "anyone can read it at a glance", "pen")

aaa_how = Doodle(760, 280, "A test in three labelled blocks. Arrange: build a cart with one twenty euro lamp. Act: apply the coupon SAVE20, a single call. Assert: the total is sixteen euros. The test name states the behaviour: applies a twenty percent coupon to the total.",
                 "One behaviour per test, in three blocks: arrange, act (one call), assert.")
for i, (t, sub, f) in enumerate([("Arrange", "cart with a €20 lamp", "blue"), ("Act", "applyCoupon('SAVE20')", "y"), ("Assert", "total = €16", "green")]):
    aaa_how.box(20 + i * 250, 80, 220, 100, t, f, sub=sub, size=22)
    if i:
        aaa_how.arrow(20 + i * 250 - 26, 130, 20 + i * 250 - 4, 130)
aaa_how.note(380, 40, "it(“applies a 20% coupon to the total”)", "pen")
aaa_how.note(380, 230, "exactly one Act line per test", "green")
aaa_how.note(380, 262, "name = the behaviour, not the method", "green")

AAA = dict(
    slug="arrange-act-assert",
    kicker="a.k.a. “method, experiment, result”",
    tldr="Write every test as three visible blocks: <b>Arrange</b> the world, <b>Act</b> with <b>one</b> call, <b>Assert</b> the outcome. Name the test after the <b>behaviour</b> (“applies a 20% coupon”), not the method. One behaviour per test means a failure tells you <b>exactly what broke</b>.",
    chips=[("Family", "test structure"), ("a.k.a.", "Given–When–Then (BDD)"), ("Origin", "Bill Wake, 2001"), ("Pairs with", "test data builders, test doubles")],
    problem="""  <p class="lead">Tests grow by accretion. Someone adds “one more check” to an existing test, then another action, then another check. Soon you have <span class="hl-pink">test2()</span>: sixty lines that test six things, and nobody dares touch it.</p>
  <ul>
    <li>When it fails, you have to debug the test before the code.</li>
    <li>An early assertion fails and hides five other problems.</li>
    <li>The test name says nothing about the behaviour it protects.</li>
  </ul>""",
    problem_figs=[aaa_problem],
    analogy_side="the lab write-up",
    analogy="""  <p>A school science report always has the same headings: <b>Method</b> (how you set up), <b>Experiment</b> (the one thing you changed), <b>Result</b> (what you saw). Any teacher can read any report in seconds, because the shape never changes.</p>
  <ul>
    <li>Method is <b>Arrange</b>; Experiment is <b>Act</b>; Result is <b>Assert</b>.</li>
    <li>Change one variable per experiment: <b>one Act per test</b>.</li>
  </ul>""",
    analogy_figs=[aaa_analogy],
    map=[("Method: set up the kit", "Arrange: create objects, stub dependencies"),
         ("Experiment: heat to 80 °C", "Act: call the one thing under test"),
         ("Result: it turned blue", "Assert: check the outcome"),
         ("The report's title", "A test name that states the behaviour"),
         ("One variable per experiment", "One behaviour per test")],
    how_side="three blocks, one behaviour",
    how="""  <p>The blank lines between the blocks are the point: a reader sees the setup, the trigger and the expectation without reading every line.</p>""",
    how_figs=[aaa_how],
    steps=[("Name the behaviour", "<code>it(\"applies a 20% coupon to the total\")</code>, not <code>it(\"applyCoupon works\")</code>."),
           ("Arrange only what matters", "Hide the boring defaults in builders or helpers (note 03)."),
           ("Act once", "One call. If you need two, you probably have two tests."),
           ("Assert the outcome", "Check results and visible effects, not private internals."),
           ("Separate the blocks", "Blank lines or <code>// arrange / act / assert</code> comments.")],
    vocab=[("Arrange", "Set up inputs, objects and doubles."),
           ("Act", "Run the single behaviour under test."),
           ("Assert", "Check the outcome."),
           ("Given–When–Then", "The same shape in BDD language."),
           ("Assertion roulette", "Many unlabelled asserts; you can't tell which failed."),
           ("Behaviour name", "Describes what should happen, not which method runs.")],
    code=dict(file="cart.test.ts", note="Vitest", src="""
describe("Cart", () => {
  it("applies a 20% coupon to the total", () => {
    // arrange
    const cart = aCart().with(aProduct().priced(20)).build();

    // act
    cart.applyCoupon("SAVE20");

    // assert
    expect(cart.total).toBe(16);
  });

  it("rejects an expired coupon", () => {
    const cart = aCart().build();

    const result = () => cart.applyCoupon("SUMMER2019");

    expect(result).toThrow(/expired/);
  });
});
"""),
    tools="tools: any test runner (Vitest, Jest, pytest, JUnit, xUnit). Cucumber and Gherkin use Given–When–Then explicitly. Linters like <code>eslint-plugin-jest</code> can flag tests with no assertions.",
    gains=["<b>Readable tests</b>: setup, trigger and expectation at a glance.",
           "<b>Precise failures</b>: one behaviour per test.",
           "<b>Tests as documentation</b>: names describe the rules.",
           "<b>Easier reviews</b>: reviewers check the shape quickly."],
    losses=["<b>More, smaller tests</b> (a bit more setup repetition).",
            "<b>Shared setup temptation</b> moves Arrange far away.",
            "<b>Awkward for long flows</b> like e2e journeys."],
    baseline="Each line compares <b>long tests mixing setup, actions and checks</b> to <b>one-behaviour Arrange–Act–Assert tests</b>.",
    ratings=[(2, 5, "Same shape every time; names say what's checked."),
             (3, 3, "Neutral."),
             (3, 4, "Each behaviour is checked on its own, nothing hidden."),
             (3, 4, "Less hidden state carried between steps."),
             (2, 5, "A red test names exactly one behaviour."),
             (2, 4, "Small tests are easy to update or delete."),
             (3, 3, "Neutral."),
             (3, 3, "More tests, but each is quick to write."),
             (2, 4, "New teammates follow one obvious convention.")],
    pitfalls=[("Several Acts in one test", "Add item, apply coupon, check out, refund: four behaviours.", "split into one test per behaviour."),
              ("Arrange in a distant beforeEach", "The setup that matters lives 200 lines away.", "keep the relevant setup inside the test."),
              ("Asserting internals", "Checking private fields or call order instead of the result.", "assert outcomes the caller can observe."),
              ("Vague names", "<code>it(\"works\")</code>, <code>test2</code>.", "name the behaviour and the condition.")],
    use=["Every unit and integration test.",
         "Reviewing tests: check for the three blocks.",
         "Teaching testing to new teammates."],
    skip=["Long end-to-end journeys (use clear steps instead).",
          "Exploratory scripts and quick spikes."],
    related=["<b>Test data builders</b>", "<b>Test doubles</b>", "<b>Test pyramid</b>", "<b>Custom hooks</b> (Vol. 2)"],
    quiz=[("What goes in each of the three blocks?", "Arrange sets up inputs and doubles, Act runs one behaviour, Assert checks the outcome."),
          ("Why only one Act per test?", "So a failure points to exactly one behaviour."),
          ("What's a good test name?", "One that states the behaviour and condition, like “rejects an expired coupon”."),
          ("What's the BDD version of AAA?", "Given–When–Then.")],
    remember="<span class=\"hl\">Set up</span>, <span class=\"hl\">poke once</span>, <span class=\"hl\">check</span>. One experiment per write-up.",
    sources=["Bill Wake, “3A: Arrange, Act, Assert” (xp123.com).",
             "Gerard Meszaros, <i>xUnit Test Patterns</i> (2007), “Four-Phase Test”.",
             "Dan North, “Introducing BDD” (Given–When–Then).",
             "Vladimir Khorikov, <i>Unit Testing Principles, Practices, and Patterns</i>, ch. 3."],
)

# ------------------------------------------------------------------ 03 Test Data Builders
tb_problem = Doodle(760, 260, "Doodle of a test that only cares whether an order is overdue, but has to build a user, an address, a payment method, three line items and a shipping option with fifteen fields. When the Order type gets a new required field, two hundred tests stop compiling.",
                    "To test one rule, every test spells out 15 fields. Add a field, fix 200 tests.")
tb_problem.box(20, 20, 330, 220, None, "paper", rx=4)
for i, t in enumerate(["new Order({", "  id: 1, user: { id: 7, name, email,", "    address: { street, city, zip } },", "  items: [ … 3 items … ],", "  payment: { card, expiry },", "  shipping: 'express',", "  dueDate: '2026-01-01', // ← the only", "})                     //  thing we test"]):
    tb_problem.text(32, 46 + i * 25, t, "t" + (" t-red" if i == 6 else ""), anchor="start", size=15)
tb_problem.note(560, 80, "+1 required field", "red")
tb_problem.arrow(560, 96, 560, 140, color="red")
tb_problem.note(560, 166, "200 tests break", "red")

tb_analogy = Doodle(760, 250, "Doodle of a sandwich shop order. The regular sandwich comes with sensible defaults: bread, butter, cheese, tomato. You only say what's different: no tomato, extra pickles. Nobody lists all twelve ingredients every time.",
                    "“The usual, but no tomato.” You only say what's different.")
tb_analogy.icon("plate", 40, 60, 2.2, fill="y")
tb_analogy.note(115, 225, "the usual (defaults)")
tb_analogy.box(300, 60, 420, 70, "“the usual, but no tomato”", "y", size=20)
tb_analogy.note(510, 170, "only the difference is spoken", "green")
tb_analogy.note(510, 210, "✗ listing all 12 ingredients", "red")

tb_how = Doodle(760, 280, "Test data builder. A function anOrder returns a builder holding a complete, valid default order. The test calls anOrder, then dueOn yesterday, then build. Only the relevant detail appears in the test; when Order gets a new field, only the builder's defaults change.",
                "A builder holds a valid default; each test names only the detail it cares about.")
tb_how.box(20, 40, 230, 150, "anOrder()", "y", sub="valid defaults: 15 fields", size=20)
tb_how.arrow(256, 115, 296, 115)
tb_how.box(302, 80, 200, 70, ".dueOn(yesterday)", "green", sub="only this detail", size=16, subsize=14)
tb_how.arrow(508, 115, 600, 115, label=".build()", lx=554, ly=100)
tb_how.box(606, 80, 140, 70, "Order", "blue", size=18)
tb_how.note(140, 240, "new field → change 1 default", "green")
tb_how.note(500, 240, "test reads: an order due yesterday", "pen")

BUILDERS = dict(
    slug="test-data-builders",
    kicker="a.k.a. “the usual, but no tomato”",
    tldr="Create test objects through <b>builders</b> that start from a <b>complete, valid default</b> and let each test override <b>only the detail it cares about</b>: <code>anOrder()</code> <code>.dueOn(yesterday)</code> <code>.build()</code>. Tests get shorter and say what matters, and when a type gains a field you change <b>one default</b>, not 200 tests.",
    chips=[("Family", "test setup"), ("Origin", "Nat Pryce; <i>Growing Object-Oriented Software</i> (2009)"), ("Cousins", "object mother, factories (factory_bot, Fishery)"), ("Pairs with", "arrange–act–assert, property-based testing")],
    problem="""  <p class="lead">Real objects have many required fields. If every test builds them by hand, the <span class="hl-pink">noise drowns the signal</span>: you can't see which of 15 fields the test is actually about.</p>
  <ul>
    <li>A test about overdue orders spells out addresses and card numbers.</li>
    <li>A new required field breaks hundreds of tests that don't care about it.</li>
    <li>People copy-paste setup and slightly different “valid” objects spread everywhere.</li>
  </ul>""",
    problem_figs=[tb_problem],
    analogy_side="the regular sandwich",
    analogy="""  <p>At your usual sandwich shop you don't list twelve ingredients. You say <b>“the usual, but no tomato”</b>. The shop knows the sensible defaults; you speak only the <b>difference</b>.</p>
  <ul>
    <li>“The usual” is the builder's <b>default</b>.</li>
    <li>“No tomato” is the <b>override</b> the test cares about.</li>
    <li>When the shop adds a new sauce to the usual, nobody re-orders: <b>one place changes</b>.</li>
  </ul>""",
    analogy_figs=[tb_analogy],
    map=[("“The usual”", "A builder with valid defaults: <code>anOrder()</code>"),
         ("“…but no tomato”", "An override: <code>.dueOn(yesterday)</code>"),
         ("Handing over the sandwich", "<code>.build()</code>"),
         ("Shop adds a sauce", "Type gains a field; only the default changes"),
         ("Listing all 12 ingredients", "Hand-built objects in every test")],
    how_side="valid defaults + named overrides",
    how="""  <p>A builder is a tiny fluent API for your tests. Its method names become the <b>domain vocabulary</b> of your test suite.</p>""",
    how_figs=[tb_how],
    steps=[("Start from a valid default", "Every field filled with a believable value that passes validation."),
           ("Add intention-revealing methods", "<code>.overdue()</code>, <code>.paidBy(card)</code>, <code>.withItems(3)</code>, not just raw setters."),
           ("Make defaults unique", "Generate ids and emails so tests don't collide."),
           ("Compose builders", "Pass one builder into another: <code>anOrder().for(</code> <code>aUser().inSpain())</code>."),
           ("Keep builders in one place", "<code>test/builders/</code>, shared by all tests.")],
    vocab=[("Test data builder", "Fluent helper that builds valid test objects."),
           ("Object mother", "Named ready-made objects (<code>Orders.overdue()</code>)."),
           ("Default", "The value used when a test doesn't care."),
           ("Override", "The detail a test deliberately sets."),
           ("Fixture", "Any data or state a test needs before it runs."),
           ("Irrelevant detail", "Setup noise that hides the test's intent.")],
    code=dict(file="test/builders/order.ts", note="TypeScript", src="""
let seq = 0;

export function anOrder(overrides: Partial<Order> = {}) {
  const order: Order = {
    id: ++seq,
    user: aUser().build(),
    items: [anItem().build()],
    shipping: "standard",
    dueDate: daysFromNow(14),
    ...overrides,
  };
  return {
    dueOn: (d: Date) => anOrder({ ...order, dueDate: d }),
    overdue: () => anOrder({ ...order, dueDate: daysFromNow(-1) }),
    build: () => order,
  };
}

// the test says only what matters
it("flags orders past their due date", () => {
  const order = anOrder().overdue().build();

  expect(isOverdue(order, today())).toBe(true);
});
"""),
    tools="tools: hand-written builders, Fishery and @faker-js/faker (TypeScript), factory_bot (Ruby), factory_boy (Python), Instancio and Lombok @Builder (Java), AutoFixture (.NET).",
    gains=["<b>Short tests</b> that show only what matters.",
           "<b>One place to change</b> when types grow.",
           "<b>Valid by default</b>: fewer accidental validation failures.",
           "<b>A shared domain vocabulary</b> for tests."],
    losses=["<b>Builder code to maintain</b>.",
            "<b>Hidden defaults</b> can matter without anyone noticing.",
            "<b>Over-clever builders</b> become their own little framework."],
    baseline="Each line compares <b>hand-built objects in every test</b> to the same tests using <b>shared test data builders</b>.",
    ratings=[(2, 5, "Tests show the one detail that matters."),
             (3, 3, "Neutral."),
             (3, 4, "Defaults are always valid, so tests check real cases."),
             (3, 4, "Unique ids avoid collisions between tests."),
             (3, 4, "Less setup noise between cause and effect."),
             (1, 5, "A new field changes one default, not 200 tests."),
             (3, 3, "Neutral."),
             (2, 4, "New tests are a line or two of setup."),
             (2, 5, "The whole team reuses the same builders.")],
    pitfalls=[("A test relies on a hidden default", "It passes only because the default country happens to be “NL”.", "if a value matters to the assertion, set it explicitly."),
              ("Builders with logic", "The builder computes totals the same way the code does, so bugs hide in both.", "keep builders dumb; set values, don't compute them."),
              ("A builder per test file", "Five slightly different <code>makeOrder</code> helpers.", "one shared builder per type."),
              ("Shared mutable objects", "Tests reuse one built object and change it.", "build a fresh object per test.")],
    use=["Domain objects with many required fields.",
         "Any type built in more than a handful of tests.",
         "Integration tests that insert rows (pair with a persist helper)."],
    skip=["Tiny value types (<code>new Money(5, \"EUR\")</code> is fine).",
          "One-off tests of trivial functions."],
    related=["<b>Arrange–Act–Assert</b>", "<b>Property-based testing</b>", "<b>Fakes</b>", "<b>Normalization</b> (Vol. 3)"],
    quiz=[("What does a builder's default have to be?", "A complete, valid object, so tests only override what they care about."),
          ("Why do builders make type changes cheaper?", "Only the builder's default has to change when a field is added."),
          ("When should a test set a value explicitly?", "Whenever the assertion depends on that value."),
          ("Builder vs object mother?", "An object mother offers fixed named objects; a builder offers defaults plus flexible overrides.")],
    remember="Order <span class=\"hl\">“the usual”</span> and name only the <span class=\"hl\">difference</span>.",
    sources=["Nat Pryce, “Test Data Builders: an alternative to the Object Mother pattern”.",
             "Steve Freeman &amp; Nat Pryce, <i>Growing Object-Oriented Software, Guided by Tests</i>, ch. 22.",
             "Martin Fowler, “ObjectMother” (bliki).",
             "Fishery documentation (thoughtbot)."],
)

# ------------------------------------------------------------------ 04 Page Objects
po_problem = Doodle(760, 260, "Doodle of forty browser tests all containing the CSS selector div.form > button.btn-primary nth child two. A designer renames one class and all forty tests fail, each needing the same edit.",
                    "The same fragile selector copy-pasted into 40 tests. One CSS change, 40 broken tests.")
for i in range(5):
    po_problem.box(20 + i * 30, 30 + i * 22, 230, 60, None, "paper", rx=3)
po_problem.text(150, 208, "click('div.form > .btn-primary')", "t t-red", size=15)
po_problem.note(150, 238, "× 40 test files", "red")
po_problem.arrow(420, 100, 520, 100, color="red", label="designer renames .btn-primary", lx=470, ly=80)
po_problem.note(620, 140, "40 red tests", "red")
po_problem.note(620, 170, "40 identical fixes", "red")

po_analogy = Doodle(760, 250, "Doodle of a TV remote. You press Play and Volume up without knowing anything about the circuits inside the TV. If the manufacturer changes the circuits, the buttons on the remote stay the same.",
                    "A remote control: press “Play”; the wiring behind it can change.")
po_analogy.icon("tv", 380, 40, 2.4)
po_analogy.box(60, 40, 120, 180, None, "y", rx=16)
for i, t in enumerate(["▶ play", "+ vol", "– vol"]):
    po_analogy.box(76, 60 + i * 50, 88, 36, t, "paper", size=15)
po_analogy.arrow(186, 120, 370, 120, dash=True)
po_analogy.note(560, 220, "the circuits can change; the buttons don't", "pen")

po_how = Doodle(760, 290, "Page object pattern. Tests call methods like loginPage.signInAs Ana and checkoutPage.payWith card. The page object classes hold the locators, preferably by role and label, and the browser interactions. When the markup changes, only the page object changes.",
                "Tests speak user language; page objects own the locators. Markup changes stay in one file.")
tests = ["signInAs('ana')", "addToCart('lamp')", "payWith(card)"]
for i, t in enumerate(tests):
    po_how.box(20, 30 + i * 74, 210, 54, t, "green", size=16)
    po_how.arrow(236, 57 + i * 74, 320, 140)
po_how.note(125, 270, "tests: user language", "green")
po_how.box(326, 90, 210, 110, "Page objects", "y", sub="getByRole · getByLabel")
po_how.arrow(542, 145, 620, 145)
po_how.icon("window", 626, 110, 1.0)
po_how.note(430, 240, "markup changes → edit one file", "pen")

PAGES = dict(
    slug="page-objects",
    kicker="a.k.a. “the remote control”",
    tldr="Give each page or component of your UI a <b>page object</b>: a class with methods in <b>user language</b> (<code>signInAs</code>, <code>addToCart</code>) that hides the selectors and clicks. Tests read like stories, and when the markup changes you fix <b>one page object</b>, not forty tests. Prefer <b>role and label locators</b> so even the page object rarely changes.",
    chips=[("Family", "UI test structure"), ("Popularised by", "Selenium community, Martin Fowler (2013)"), ("Variants", "component objects, screenplay pattern"), ("Pairs with", "test pyramid (top layer), headless components")],
    problem="""  <p class="lead">Browser tests click on things found by selectors. Copy those selectors into every test and the suite becomes <span class="hl-pink">as fragile as your CSS</span>.</p>
  <ul>
    <li>A designer renames a class and 40 tests fail with the same error.</li>
    <li>Tests are full of <code>nth-child(2)</code> and nobody knows what they click.</li>
    <li>Login steps are repeated, slightly differently, in every file.</li>
  </ul>""",
    problem_figs=[po_problem],
    analogy_side="the TV remote",
    analogy="""  <p>You press <b>Play</b> on a remote without knowing how the TV is wired. The manufacturer can redesign every circuit, and the <b>buttons stay the same</b>.</p>
  <ul>
    <li>The buttons are page-object <b>methods</b>.</li>
    <li>The circuits are <b>selectors and clicks</b>, hidden inside.</li>
    <li>You read the remote, not the circuit diagram: tests read like <b>user stories</b>.</li>
  </ul>""",
    analogy_figs=[po_analogy],
    map=[("The ▶ Play button", "<code>checkout.payWith(card)</code>"),
         ("Wiring inside the TV", "Locators and clicks inside the page object"),
         ("New circuits, same buttons", "Markup changes, tests don't"),
         ("One remote per device", "One page object per page or component"),
         ("Pressing buttons in order", "A test reading like a user story")],
    how_side="tests talk to pages, pages talk to the DOM",
    how="""  <p>Page objects are a <b>thin translation layer</b>: user intent above, DOM details below. Keep assertions in the tests and the “how to click” in the page objects.</p>""",
    how_figs=[po_how],
    steps=[("One object per page or component", "<code>LoginPage</code>, <code>CartDrawer</code>, <code>CheckoutPage</code>."),
           ("Expose user actions", "<code>signInAs(user)</code>, <code>addToCart(name)</code>, returning the next page where useful."),
           ("Use resilient locators", "<code>getByRole(\"button\", { name: \"Pay\" })</code> or test ids, not CSS paths."),
           ("Keep assertions in tests", "Page objects may expose state (<code>cart.count()</code>), tests decide what's right."),
           ("Share via fixtures", "Inject page objects with your runner's fixtures so tests stay short.")],
    vocab=[("Page object", "Class wrapping one page's locators and actions."),
           ("Locator", "How the test finds an element."),
           ("Role locator", "Finds elements the way assistive tech sees them."),
           ("Test id", "A <code>data-testid</code> attribute just for tests."),
           ("Component object", "A page object for a reusable widget."),
           ("Screenplay pattern", "Actors performing tasks: a more composable variant.")],
    code=dict(file="e2e/pages/login.ts + checkout.spec.ts", note="Playwright", src="""
export class LoginPage {
  constructor(private page: Page) {}
  async goto() { await this.page.goto("/login"); }
  async signInAs(user: { email: string; password: string }) {
    await this.page.getByLabel("Email").fill(user.email);
    await this.page.getByLabel("Password").fill(user.password);
    await this.page.getByRole("button", { name: "Sign in" }).click();
  }
}

// the test reads like a story
test("a signed-in user can pay for a lamp", async ({ page }) => {
  const login = new LoginPage(page), shop = new ShopPage(page);

  await login.goto();
  await login.signInAs(users.ana);
  await shop.addToCart("Lamp");
  await shop.checkout().payWith(cards.valid);

  await expect(page.getByText("Thanks for your order")).toBeVisible();
});
"""),
    tools="tools: Playwright (fixtures + <code>getByRole</code>), Cypress (custom commands or page objects), WebdriverIO, Selenium, Testing Library queries (<code>getByRole</code>, <code>getByLabelText</code>) for component tests.",
    gains=["<b>One place to fix</b> when the markup changes.",
           "<b>Readable tests</b> in user language.",
           "<b>Reusable steps</b> like sign-in.",
           "<b>Accessible locators</b> double as an a11y check."],
    losses=["<b>An extra layer</b> of classes.",
            "<b>Bloated page objects</b> if they grow every helper.",
            "<b>Assertions can leak in</b> and hide what the test checks."],
    baseline="Each line compares <b>browser tests with selectors inline</b> to the same tests using <b>page objects with role locators</b>.",
    ratings=[(2, 4, "Tests read like user stories."),
             (3, 3, "Neutral."),
             (3, 4, "Role locators check what users actually see."),
             (2, 4, "Stable locators, one tested wait strategy."),
             (2, 3, "Failures point to a named step."),
             (1, 5, "A markup change is one edit."),
             (4, 4, "Still a real browser."),
             (2, 4, "New tests reuse existing steps."),
             (2, 4, "Teams share one library of page objects.")],
    pitfalls=[("Assertions inside page objects", "<code>signInAs</code> secretly expects a welcome banner.", "keep checks in tests; expose state instead."),
              ("God page objects", "One <code>AppPage</code> with 120 methods.", "one object per page or component."),
              ("CSS paths as locators", "Page objects still break on every redesign.", "use roles, labels and test ids."),
              ("Wrapping every tiny thing", "<code>clickButton(name)</code> adds nothing over Playwright.", "wrap user intents, not single API calls.")],
    use=["Any suite with more than a handful of UI tests.",
         "Steps repeated across tests (sign-in, checkout).",
         "UIs that change often."],
    skip=["Two or three smoke tests.",
          "Component tests with Testing Library, which already query by role."],
    related=["<b>Test pyramid</b>", "<b>Arrange–Act–Assert</b>", "<b>Headless components</b> (Vol. 2)", "<b>Flaky test quarantine</b>"],
    quiz=[("Where do selectors live in the page object pattern?", "Inside the page objects, never in the tests."),
          ("Why prefer getByRole over CSS selectors?", "Roles and accessible names change far less than classes, and they check what users and assistive tech see."),
          ("Should page objects contain assertions?", "Generally no: they expose actions and state, tests decide what's expected."),
          ("What does a page object method usually represent?", "One user intent, like signing in or paying.")],
    remember="Press the <span class=\"hl\">buttons</span>; let the remote hide the <span class=\"hl\">wiring</span>.",
    sources=["Martin Fowler, “PageObject” (bliki, 2013).",
             "Playwright docs, “Page object models” and “Locators”.",
             "Selenium docs, “Page object models”.",
             "Testing Library docs, “Which query should I use?”."],
)

NOTES = [PYRAMID, AAA, BUILDERS, PAGES]
