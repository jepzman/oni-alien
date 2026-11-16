# Revisions to Vol. 4 (November 2026): one situational quiz question and a “try it” per note.
# Merged into the notes by scripts/build_notes.py (load_content).

REVISION_NOTE = ("Nov 2026", "every note gains a “what would you do?” question and a try it; related notes are links now")

REVISIONS = {
    "test-pyramid": dict(
        quiz_add=[("Your CI runs 400 end-to-end tests in 55 minutes and 120 unit tests in 20 seconds. A third of the e2e tests check discount rules through the browser. What do you change first?",
                   "Move the discount rules down to unit tests on the pricing code, keep one e2e test that a discount shows at checkout, and delete the rest. The suite gets faster and failures point at the rule instead of a screen.")],
        try_it="List your team's tests by layer (unit, integration, e2e) with their count and run time. Pick three e2e tests that check business rules and rewrite each as a unit test. Compare run times and how clearly a failure explains itself.",
    ),
    "arrange-act-assert": dict(
        quiz_add=[("A test called test_cart_3 fails. It is 60 lines long, calls addItem, applyCoupon and checkout, and asserts eleven things. What do you do before fixing the bug?",
                   "Split it into small tests named after one behaviour each (“applies a 20% coupon”, “rejects an expired coupon”), each with one Act and the assertions about that behaviour. Then the failing one tells you what broke.")],
        try_it="Pick the longest test in your project. Rewrite it as separate tests with blank lines between Arrange, Act and Assert, and names that describe behaviour. Break the code on purpose and compare the failure messages before and after.",
    ),
    "test-data-builders": dict(
        quiz_add=[("Order gains a required currency field, and 180 tests fail to compile because each builds an Order by hand. How do you make the next new field a one-line change?",
                   "Add an anOrder() builder with complete, valid defaults (including currency) and move the tests to it, overriding only what each test is about. The next new field gets a default in the builder and no test changes.")],
        try_it="Write a builder for one of your domain types with sensible defaults and three “with” methods. Rewrite five tests to use it, then add a new required field to the type and count how many files you have to touch.",
    ),
    "page-objects": dict(
        quiz_add=[("The login button's CSS class changes, and 40 Playwright tests fail on the same selector. What do you introduce, and which selector do you use in it?",
                   "A LoginPage object with a signInAs(user) method that is the only place the selectors live, using role-based locators such as getByRole('button', { name: 'Sign in' }). The next markup change is fixed once.")],
        try_it="Write a page object for your app's sign-in page with getByRole locators and a signInAs method, and move three tests to it. Change the button's class and its text, and see which change breaks the tests.",
    ),
    "test-doubles": dict(
        quiz_add=[("A signup test mocks the repository, the hasher, the clock, the email sender and the logger, and asserts the order of eight calls. A harmless refactor breaks it. What do you change?",
                   "Use a fake repository and the real hasher, fix the clock, and keep a spy only on the email sender (the thing you send). Assert outcomes: the user is saved and one welcome email is sent, not the order of internal calls.")],
        try_it="Find a test with three or more mocks. Replace the ones for things you read with stubs or fakes, keep one spy on an outgoing call, and assert results instead of calls. Then refactor the code under test and see whether the new test still passes.",
    ),
    "fakes": dict(
        quiz_add=[("Tests pass against an in-memory UserRepository, but production fails because the real one rejects duplicate emails and the fake doesn't. How do you stop the fake drifting again?",
                   "Write one contract test suite and run it against both the fake and the real repository (in a container). Add the duplicate-email case to the contract, and the fake must pass it too.")],
        try_it="Write an in-memory fake for a repository interface you have, then write five contract tests and run them against both the fake and the real implementation. Add a rule to the real one and watch the contract test catch the fake.",
    ),
    "testcontainers": dict(
        quiz_add=[("Integration tests run against SQLite and pass, but a query using Postgres's ILIKE and JSONB fails in production. Someone suggests a shared staging database for tests. What do you suggest instead?",
                   "Start a throwaway Postgres container of the production version for each test run, run the migrations, and isolate tests with transactions or a schema per worker. A shared database brings flaky tests from other people's data.")],
        try_it="Set up Testcontainers in your project to start the same Postgres version as production once per run. Move one integration test from a mock or SQLite to it, wrap each test in a rolled-back transaction, and time the suite.",
    ),
    "contract-testing": dict(
        quiz_add=[("The Orders team renames total to totalAmount. Their tests pass, the web app's tests pass, and checkout breaks in production. What would have stopped the deploy?",
                   "Consumer-driven contracts: the web app records that it reads total, the Orders build verifies every consumer contract, and a can-i-deploy check blocks the release while a consumer still needs the old field.")],
        try_it="Write a Pact consumer test for one call your frontend makes, publish the pact file, and verify it in the provider's test suite. Rename a field the consumer uses and watch the provider verification fail.",
    ),
    "property-based": dict(
        quiz_add=[("A bill-splitting function has 12 example tests and still produced a total one cent short for a customer splitting €100 three ways. Which property would have caught it?",
                   "“The parts always add up to the total”, checked for random amounts and numbers of people. The tool would have found and shrunk a failing case such as €100 / 3 quickly.")],
        try_it="Pick a pure function you own (sorting, splitting, formatting, encoding). Write one property for it with fast-check or Hypothesis, such as a round trip or an invariant. Introduce an off-by-one bug and read the shrunk counterexample.",
    ),
    "snapshot-testing": dict(
        quiz_add=[("A pull request updates 214 snapshot files, and the reviewer approves without reading them. A week later an invoice ships with the VAT line missing. What do you change?",
                   "Keep snapshots small and focused (one invoice section, not the whole page), scrub dates and ids so they only change for real reasons, and treat a large snapshot update as a code change to review, or replace it with explicit assertions.")],
        try_it="Snapshot one function that produces a large output (an email body, an invoice, generated SQL). Scrub the dates and ids, change one line of logic, and read the diff. Then make the snapshot smaller so the diff shows only what matters.",
    ),
    "mutation-testing": dict(
        quiz_add=[("A pricing module has 98% line coverage. Stryker reports 40% of mutants survived, including changing > to >= in the free-shipping rule. What does that tell you, and what do you write?",
                   "The tests run the code but don't check the boundaries. Write tests at the exact edges: an order of exactly €50 and one of €49.99, with the expected shipping fee for each.")],
        try_it="Run StrykerJS, mutmut or PIT on one small module with good coverage. Read three surviving mutants and add the tests that kill them. Note which ones were real gaps and which were equivalent mutants.",
    ),
    "characterization-tests": dict(
        quiz_add=[("You must change a 900-line shipping-cost function with no tests. It has a known bug for Belgian islands that a customer depends on. What do you do first?",
                   "Write characterization tests over many realistic inputs (from production logs) and record today's outputs, bug included. Refactor with them green. Fix the island bug later as a deliberate change, with the customer warned.")],
        try_it="Choose a legacy function without tests. Feed it 200 inputs taken from logs or generated, and save the outputs as a golden master file. Refactor one part and check the outputs stay identical.",
    ),
    "deterministic-tests": dict(
        quiz_add=[("A test about trial expiry passes all day and fails between 23:00 and midnight on the CI server, which runs in UTC. What is going on, and what is the fix?",
                   "The code reads the real clock and local time zone, so around midnight “today” differs between the test and the code. Inject a clock, set a fixed instant in the test, and run tests with TZ=UTC.")],
        try_it="Find code that calls new Date(), Date.now() or Math.random() directly. Pass in a clock and a random source instead. Write a test that moves the clock forward 14 days, and one that runs at 23:59 on 31 December.",
    ),
    "flaky-tests": dict(
        quiz_add=[("The team re-runs CI two or three times per pull request “because checkout.spec is flaky”. Nobody owns it. What do you do this week?",
                   "Quarantine it into a non-blocking job, open a ticket with an owner and a deadline, and look for the cause: a fixed sleep, shared data or an unawaited request. Replace sleeps with waiting for a visible result.")],
        try_it="Run your end-to-end suite 20 times in a row (with repeat-each or a loop) and record which tests fail at least once. Pick one, find the cause, and fix it without adding a retry.",
    ),
    "parallel-selective": dict(
        quiz_add=[("Pull requests wait 40 minutes for CI. Tests are spread over 4 shards by file count, and one shard always takes 25 minutes. What do you change?",
                   "Split shards by recorded test timing so they finish together, run only the tests affected by the change on pull requests, and keep the full suite on main. Check first that tests are isolated, or parallel runs will create flakes.")],
        try_it="Run your test suite with 1, 2 and 4 workers and note the times. Then use your tool's affected-tests or changed-files option on a one-file change and compare how many tests ran.",
    ),
}

for _rev in REVISIONS.values():
    _rev.setdefault("revised", ("Nov 2026", "a “what would you do?” question and a try it"))
