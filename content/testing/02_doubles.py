# Vol. 4 · Doubles & boundaries: Test Doubles, Fakes, Throwaway Containers, Contract Testing.

# ------------------------------------------------------------------ 05 Test Doubles
td_problem = Doodle(760, 260, "Doodle of a unit test for a signup function that really calls the payment provider, sends a real email and waits for the weather API. It takes eight seconds, costs money, fails when the network is down, and once emailed a real customer.",
                    "A “unit” test that charges a card, emails a customer and waits on the network.")
td_problem.box(20, 100, 170, 60, "signup test", "blue")
for i, (t, n) in enumerate([("payments API", "charges €1 · 2 s"), ("email service", "emails a real person!"), ("weather API", "down today → red")]):
    y = 20 + i * 80
    td_problem.box(420, y, 190, 50, t, "pink", stroke="red", size=17)
    td_problem.arrow(196, 130, 414, y + 25, color="red")
    td_problem.note(620, y + 32, n, "red", anchor="start")

td_analogy = Doodle(760, 260, "Doodle of a film set. A stunt double does the dangerous fall instead of the star, a cardboard cut-out stands in for lighting checks, and a crash-test dummy records the impact. Each stand-in has a different job.",
                    "A film set has different stand-ins: a stunt double, a cut-out for lighting, a dummy with sensors.")
for i, (icon, t, sub) in enumerate([("dummy", "cut-out", "just stands there"), ("dummy", "stunt double", "acts the scene"), ("dummy", "crash dummy", "records the hits")]):
    x = 60 + i * 240
    td_analogy.icon(icon, x, 30, 1.8, fill=["paper", "y", "green"][i])
    td_analogy.note(x + 54, 180, t, "pen")
    td_analogy.note(x + 54, 206, sub)

td_how = Doodle(760, 300, "Kinds of test doubles. A dummy is passed but never used. A stub returns canned answers, for example the price service returns 20. A spy records how it was called so the test can check afterwards. A mock is pre-programmed with expectations and fails if they are not met. A fake is a lightweight working implementation, covered in the next note.",
                "Five kinds of stand-in, each with one job. Stub what you read, spy or mock what you must send.")
kinds = [("dummy", "fills a slot", "paper"), ("stub", "canned answers", "y"), ("spy", "records calls", "blue"), ("mock", "expects calls", "pink"), ("fake", "works, simply", "green")]
for i, (t, sub, f) in enumerate(kinds):
    td_how.box(10 + i * 150, 60, 136, 90, t, f, sub=sub, size=20, subsize=15)
td_how.note(160, 200, "queries (data in) → stub", "green")
td_how.note(530, 200, "commands (effects out) → spy / mock", "pen")
td_how.note(380, 250, "never mock what you don't own: wrap it first", "red")

DOUBLES = dict(
    slug="test-doubles",
    kicker="a.k.a. “stunt doubles”",
    tldr="Replace slow, costly or unpredictable dependencies with <b>test doubles</b>, and pick the right kind: a <b>stub</b> returns canned answers for things you <i>read</i>, a <b>spy</b> or <b>mock</b> checks things you <i>send</i> (emails, payments), a <b>fake</b> is a simple working version. Double only at <b>boundaries you own</b>, and don't mock the thing you're testing.",
    chips=[("Family", "isolation"), ("Names from", "Gerard Meszaros, <i>xUnit Test Patterns</i>"), ("Kinds", "dummy, stub, spy, mock, fake"), ("Pairs with", "fakes, contract testing")],
    problem="""  <p class="lead">Real code talks to payment providers, email services and third-party APIs. If tests call them for real, they're <span class="hl-pink">slow, costly, flaky and sometimes dangerous</span>.</p>
  <ul>
    <li>Every test run charges a card or sends an email.</li>
    <li>A third-party outage turns your build red.</li>
    <li>You can't easily test “the payment was declined” or “the API timed out”.</li>
  </ul>""",
    problem_figs=[td_problem],
    analogy_side="stand-ins on a film set",
    analogy="""  <p>A film set uses <b>different stand-ins for different jobs</b>: a <b>cardboard cut-out</b> while lights are set up, a <b>stunt double</b> for the dangerous fall, a <b>crash-test dummy</b> with sensors to record the impact. Using the wrong one wastes time or misses what you needed to know.</p>
  <ul>
    <li>Cut-out = <b>dummy</b> (fills a slot).</li>
    <li>Stunt double playing the scene = <b>stub/fake</b> (gives answers).</li>
    <li>Crash dummy with sensors = <b>spy/mock</b> (records what happened to it).</li>
  </ul>""",
    analogy_figs=[td_analogy],
    map=[("Cardboard cut-out", "Dummy: passed in, never used"),
         ("Stunt double", "Stub: returns the answers the scene needs"),
         ("Crash dummy with sensors", "Spy: records calls for later checks"),
         ("A dummy that complains if not hit", "Mock: fails if expected calls didn't happen"),
         ("A rehearsal set", "Fake: a simple working version")],
    how_side="pick the double by its job",
    how="""  <p>A good rule: <b>stub queries, verify commands</b>. If a dependency gives you data, stub it and assert on your result. If your code must cause an effect (send, charge, publish), check that the effect was requested.</p>""",
    how_figs=[td_how],
    steps=[("Find the boundary", "Payments, email, clock, HTTP clients: things that are slow, costly or random."),
           ("Wrap third-party APIs", "Put an interface you own (<code>PaymentGateway</code>) in front of the SDK; double your interface, not theirs."),
           ("Inject it", "Pass the dependency in (constructor or parameter) so tests can swap it."),
           ("Stub queries", "<code>prices.get</code> returns 20; assert on your own result."),
           ("Verify commands", "Check <code>email.send</code> was called with the right address, once."),
           ("Back it with integration tests", "One real-integration test per adapter proves the wrapper actually works.")],
    vocab=[("Test double", "Any stand-in for a real dependency in a test."),
           ("Stub", "Returns predetermined answers."),
           ("Spy", "Records how it was called."),
           ("Mock", "Has expectations that must be met."),
           ("Seam", "A place where you can swap behaviour without editing code."),
           ("Over-mocking", "Doubling so much the test only checks the mocks.")],
    code=dict(file="signup.test.ts", note="Vitest", src="""
it("sends a welcome email after a successful signup", async () => {
  const payments = { charge: vi.fn().mockResolvedValue({ ok: true }) };   // stub
  const email = { send: vi.fn() };                                         // spy
  const signup = makeSignup({ payments, email });

  await signup({ email: "ana@example.com", plan: "pro" });

  expect(email.send).toHaveBeenCalledOnce();
  expect(email.send).toHaveBeenCalledWith(
    expect.objectContaining({ to: "ana@example.com", template: "welcome" }));
});

it("does not email when the card is declined", async () => {
  const payments = { charge: vi.fn().mockResolvedValue({ ok: false }) };
  const email = { send: vi.fn() };

  await expect(makeSignup({ payments, email })({ email: "a@b.c", plan: "pro" }))
    .rejects.toThrow(/declined/);
  expect(email.send).not.toHaveBeenCalled();
});
"""),
    tools="tools: Vitest <code>vi.fn</code>, Jest mocks, Sinon (spies/stubs), MSW (stub HTTP at the network layer), unittest.mock (Python), Mockito (Java), NSubstitute (.NET).",
    gains=["<b>Fast, free, offline tests</b>.",
           "<b>Hard cases on demand</b>: declines, timeouts, errors.",
           "<b>No side effects</b> on real customers.",
           "<b>Precise failures</b> in your own code."],
    losses=["<b>Doubles can lie</b>: the real API behaves differently.",
            "<b>Over-mocking</b> ties tests to implementation details.",
            "<b>Setup noise</b> when many doubles are needed.",
            "<b>Needs integration tests</b> to cover the real wiring."],
    baseline="Each line compares tests that <b>call real third-party services</b> to tests using <b>stubs and spies at owned boundaries</b>.",
    ratings=[(3, 3, "Doubles add setup but remove network noise."),
             (1, 5, "Milliseconds instead of network round trips."),
             (4, 3, "Doubles can drift from the real API."),
             (1, 5, "No outages, rate limits or shared accounts."),
             (2, 5, "A red test points at your code, not theirs."),
             (3, 3, "Good with wrappers; brittle with over-mocking."),
             (5, 2, "Stand-ins aren't the real thing."),
             (2, 5, "No API bills or test accounts per run."),
             (2, 4, "Thousands of tests can run in parallel.")],
    pitfalls=[("Mocking the thing under test", "Half the class is mocked, so the test checks your mocks.", "double only collaborators at boundaries."),
              ("Mocking libraries you don't own", "A mocked SDK call passes; the real SDK needs a different argument.", "wrap it in your interface and integration-test the wrapper."),
              ("Verifying every call", "Tests assert exact call order of internal helpers and break on every refactor.", "verify only commands with real effects."),
              ("Mocks for everything", "Five mocks per test, 40 lines of setup.", "prefer a fake (note 06) or a real dependency in a container.")],
    use=["Payments, email, SMS, third-party APIs.",
         "Simulating failures that are hard to trigger for real.",
         "Fast unit tests of logic around side effects."],
    skip=["Your own database queries (use a real database in a container).",
          "Pure functions with no dependencies.",
          "When a simple fake would be clearer than many mocks."],
    related=["<b>Fakes</b>", "<b>Contract testing</b>", "<b>Controlled time &amp; randomness</b>", "<b>Circuit breaker</b> (Vol. 1)"],
    quiz=[("Stub or spy for a price lookup?", "A stub: it's a query, so return a canned price and assert on your own result."),
          ("Stub or spy for sending an email?", "A spy or mock: it's a command, so check the email was requested correctly."),
          ("Why wrap third-party SDKs before doubling them?", "So you double an interface you own and can prove the wrapper against the real SDK in an integration test."),
          ("What's the danger of over-mocking?", "Tests become coupled to implementation details and pass even when the real system is broken.")],
    remember="<span class=\"hl\">Stub</span> what you read, <span class=\"hl\">spy</span> on what you send, and only double what you <span class=\"hl\">own</span>.",
    sources=["Gerard Meszaros, <i>xUnit Test Patterns</i>, “Test Double”.",
             "Martin Fowler, “Mocks Aren't Stubs”.",
             "Steve Freeman et al., “Mock Roles, not Objects” (OOPSLA 2004).",
             "Vladimir Khorikov, <i>Unit Testing Principles, Practices, and Patterns</i>, ch. 5."],
)

# ------------------------------------------------------------------ 06 Fakes
fk_problem = Doodle(760, 260, "Doodle of a test with five mocks set up line by line: when find user with id 7 return Ana, when save is called return true, when find again return Ana with the new email. The mocks repeat the database's behaviour badly, and a refactor that calls find twice breaks every test.",
                    "Mocks that script every call: 30 lines of setup, broken by harmless refactors.")
fk_problem.box(20, 20, 400, 220, None, "paper", rx=4)
for i, t in enumerate(["repo.find.mockReturnValueOnce(ana)", "repo.save.mockResolvedValue(true)", "repo.find.mockReturnValueOnce(ana2)", "repo.list.mockReturnValue([ana])", "repo.exists.mockReturnValue(false)", "… 25 more lines …"]):
    fk_problem.text(34, 50 + i * 32, t, "t", anchor="start", size=15)
fk_problem.note(590, 80, "refactor: call find() twice", "red")
fk_problem.arrow(590, 96, 590, 140, color="red")
fk_problem.note(590, 166, "40 tests fail, code is fine", "red")

fk_analogy = Doodle(760, 250, "Doodle of a flight simulator. Pilots train in a simulator that really responds to the controls, with simplified physics, instead of a real plane or a script that says press button A, then the screen shows B.",
                    "A flight simulator: it really responds to the controls, with simpler insides than a plane.")
fk_analogy.icon("screen", 60, 50, 2.4, fill="y")
fk_analogy.note(140, 210, "responds like a plane", "green")
fk_analogy.note(470, 80, "✗ the real plane: costly, risky", "red", anchor="start")
fk_analogy.note(470, 130, "✗ a script: “press A, see B”", "red", anchor="start")
fk_analogy.note(470, 180, "✓ simulator: simple but real", "green", anchor="start")

fk_how = Doodle(760, 290, "Fake repository. Production code depends on a UserRepository interface. The real implementation talks to PostgreSQL. An InMemoryUserRepository keeps users in a Map and behaves the same way. The same contract test suite runs against both, so the fake can't drift from the real one.",
                "One interface, two implementations, one shared contract test that keeps the fake honest.")
fk_how.box(260, 20, 240, 60, "UserRepository", "y", size=19)
fk_how.arrow(330, 84, 170, 130)
fk_how.arrow(430, 84, 590, 130)
fk_how.box(40, 134, 260, 70, "PostgresUserRepo", "blue", sub="real database", size=17)
fk_how.box(460, 134, 260, 70, "InMemoryUserRepo", "green", sub="a Map, in memory", size=17)
fk_how.box(200, 230, 360, 50, "same contract tests run on both", "paper", stroke="green", size=17)
fk_how.arrow(300, 226, 200, 208, dash=True, color="green")
fk_how.arrow(460, 226, 560, 208, dash=True, color="green")

FAKES = dict(
    slug="fakes",
    kicker="a.k.a. “the flight simulator”",
    tldr="A fake is a <b>small, working implementation</b> of a dependency, like an <b>in-memory repository</b> backed by a Map, or a fake payment gateway that remembers charges. Tests use it like the real thing: <b>save, then find</b>. No scripting of every call. Run one <b>shared contract test</b> against both the fake and the real implementation so the fake can't quietly drift.",
    chips=[("Family", "isolation"), ("Examples", "in-memory repo, fake clock, fake mail outbox"), ("Kept honest by", "shared contract tests"), ("Pairs with", "test doubles, throwaway containers")],
    problem="""  <p class="lead">Mocks script a conversation call by call. For anything with state, like a repository or a cart service, the script grows long and <span class="hl-pink">re-implements the dependency badly</span>, and tests break when you refactor harmless details.</p>
  <ul>
    <li>Thirty lines of <code>mockReturnValueOnce</code> per test.</li>
    <li>Calling <code>find()</code> twice in the code breaks 40 tests.</li>
    <li>The mock says save succeeded, but nothing is actually stored for the next step.</li>
  </ul>""",
    problem_figs=[fk_problem],
    analogy_side="the flight simulator",
    analogy="""  <p>Pilots don't train in a real plane, and they don't train with a <b>script</b> (“press A, the screen shows B”). They use a <b>simulator</b>: simplified insides, but it <b>really responds</b> to whatever they do, in any order.</p>
  <ul>
    <li>The simulator is the <b>fake</b>: real behaviour, simple insides.</li>
    <li>The script is a <b>mock</b>: only works if you follow it exactly.</li>
    <li>Simulators are certified against real planes: the <b>contract test</b>.</li>
  </ul>""",
    analogy_figs=[fk_analogy],
    map=[("The simulator", "<code>InMemoryUserRepository</code>"),
         ("Responds to any input order", "Save, find, list in any order just works"),
         ("Simplified physics", "A Map instead of SQL"),
         ("Certified against the real plane", "Shared contract tests on fake and real"),
         ("A scripted training video", "A mock with call-by-call expectations")],
    how_side="one interface, two implementations",
    how="""  <p>Fakes shine for <b>stateful</b> dependencies. Write them once, share them across the suite, and prove them with the same tests the real implementation passes.</p>""",
    how_figs=[fk_how],
    steps=[("Define the port", "An interface your code depends on: <code>save</code>, <code>findById</code>, <code>findByEmail</code>."),
           ("Write the fake", "A Map or array; keep it small and obviously correct."),
           ("Write contract tests", "One suite, parameterised by implementation: “save then find returns it”, “email is unique”."),
           ("Run them on both", "The fake in unit runs; the real one against a database container."),
           ("Use the fake everywhere", "Services, handlers and use-case tests get fast, realistic behaviour.")],
    vocab=[("Fake", "A working, simplified implementation."),
           ("Port", "An interface the domain depends on."),
           ("Adapter", "A real implementation of a port (Postgres, Stripe)."),
           ("Contract test", "Tests every implementation of a port must pass."),
           ("Stateful dependency", "One whose answers depend on earlier calls."),
           ("Drift", "When the fake stops behaving like the real thing.")],
    code=dict(file="users.fake.ts + users.contract.ts", note="Vitest", src="""
export class InMemoryUserRepository implements UserRepository {
  private rows = new Map<string, User>();
  async save(u: User) {
    const clash = [...this.rows.values()].find((x) => x.email === u.email && x.id !== u.id);
    if (clash) throw new DuplicateEmail(u.email);          // same rule as the DB
    this.rows.set(u.id, structuredClone(u));
  }
  async findById(id: string) { return structuredClone(this.rows.get(id)) ?? null; }
}

// one suite, every implementation
export function userRepositoryContract(make: () => Promise<UserRepository>) {
  it("finds what it saved", async () => {
    const repo = await make();
    await repo.save(aUser({ id: "7" }));
    expect(await repo.findById("7")).toMatchObject({ id: "7" });
  });
  it("rejects duplicate emails", async () => { /* … */ });
}
describe("in-memory", () => userRepositoryContract(async () => new InMemoryUserRepository()));
describe("postgres", () => userRepositoryContract(() => pgRepoInContainer()));
"""),
    tools="tools: hand-written fakes, MSW handlers with in-memory state, <code>localstack</code> (AWS), fake SMTP servers like MailHog/Mailpit, Firebase and Azurite emulators, SQLite in-memory (careful: it isn't Postgres).",
    gains=["<b>Natural tests</b>: save, then find. No call scripts.",
           "<b>Refactor-friendly</b>: tests check behaviour, not calls.",
           "<b>Fast</b>: in-memory and in-process.",
           "<b>Reusable</b> across the whole suite."],
    losses=["<b>Code to write and maintain</b>.",
            "<b>Can drift</b> from the real thing without contract tests.",
            "<b>Not the real engine</b>: SQL quirks, transactions and locks aren't covered."],
    baseline="Each line compares tests using <b>call-by-call mocks</b> for a repository to tests using an <b>in-memory fake</b> kept honest by contract tests.",
    ratings=[(2, 4, "Tests read like normal usage."),
             (5, 5, "Both run in memory."),
             (3, 4, "State flows between steps like the real thing."),
             (4, 4, "Neutral to slightly better: less fragile setup."),
             (4, 4, "Failures still point at your code."),
             (1, 5, "Refactors don't break call scripts."),
             (2, 3, "Real behaviour, but not the real engine."),
             (3, 3, "Writing the fake costs up front, saves later."),
             (2, 4, "One fake serves hundreds of tests.")],
    pitfalls=[("Fakes without contract tests", "The fake allows duplicate emails; production doesn't.", "run the same contract suite on fake and real."),
              ("Over-smart fakes", "The fake re-implements half of PostgreSQL.", "keep it tiny; test SQL-specific behaviour against a real database."),
              ("Returning shared references", "A test mutates a found object and changes the fake's state.", "return copies (<code>structuredClone</code>)."),
              ("SQLite as a fake for Postgres", "Tests pass; real queries fail on JSONB or locking.", "use a real Postgres container for data-layer tests.")],
    use=["Repositories, caches, queues, file stores.",
         "Use-case and service tests with stateful collaborators.",
         "Replacing long mock setups."],
    skip=["Simple one-call queries (a stub is enough).",
          "Testing SQL itself (use the real database).",
          "Dependencies whose behaviour is too complex to fake honestly."],
    related=["<b>Test doubles</b>", "<b>Throwaway containers</b>", "<b>Contract testing</b>", "<b>Surrogate keys</b> (Vol. 3)"],
    quiz=[("How is a fake different from a stub?", "A stub returns canned answers; a fake actually works, keeping state so calls in any order behave sensibly."),
          ("How do you stop a fake drifting from the real implementation?", "Run one shared contract test suite against both."),
          ("Why return copies from an in-memory fake?", "So tests can't change stored state by mutating returned objects, just like a real database."),
          ("When is a real database better than a fake?", "When you're testing queries, constraints, transactions or engine-specific features.")],
    remember="Train in a <span class=\"hl\">simulator</span>, not from a <span class=\"hl\">script</span>, and certify it against the real thing.",
    sources=["Martin Fowler, “Mocks Aren't Stubs” and “InMemoryTestDatabase”.",
             "Google Testing Blog, “Know Your Test Doubles” and “Testing on the Toilet: Fake Your Way to Better Tests”.",
             "Alistair Cockburn, “Hexagonal Architecture” (ports and adapters).",
             "Software Engineering at Google, ch. 13 “Test Doubles”."],
)

# ------------------------------------------------------------------ 07 Throwaway Containers
tc_problem = Doodle(760, 260, "Doodle of a shared test database on a server called test-db-01. Two CI runs write to it at the same time and break each other's data, one developer has an old schema version, and a test passes locally on SQLite but the real Postgres query fails in production.",
                    "One shared test database: runs collide, schemas drift, and “works on SQLite” isn't “works on Postgres”.")
for i, t in enumerate(["CI run #1", "CI run #2", "Ana's laptop"]):
    tc_problem.box(20, 20 + i * 76, 170, 54, t, "blue", size=17)
    tc_problem.arrow(196, 47 + i * 76, 380, 120, color="red")
tc_problem.db(450, 90, "test-db-01 (shared)", w=110, h=60)
tc_problem.note(640, 60, "data collisions", "red")
tc_problem.note(640, 100, "old schema", "red")
tc_problem.note(640, 140, "SQLite ≠ Postgres", "red")

tc_analogy = Doodle(760, 250, "Doodle of a hotel room. Each guest gets a freshly made room with clean sheets, identical to every other room, and it's cleaned when they leave. Nobody inherits the last guest's mess, and nobody shares a room with a stranger.",
                    "A hotel room: fresh, identical, yours alone, and cleaned up when you leave.")
for i in range(3):
    tc_analogy.icon("door", 60 + i * 110, 40, 1.4, fill=["green", "y", "green"][i])
tc_analogy.note(220, 190, "a fresh room per guest", "green")
tc_analogy.note(560, 70, "clean sheets every time", "pen")
tc_analogy.note(560, 120, "no stranger's luggage", "pen")
tc_analogy.note(560, 170, "cleaned when you leave", "pen")

tc_how = Doodle(760, 290, "Throwaway containers in a test run. The test suite starts a Postgres 16 container with the same version as production, runs the migrations, and each test runs inside a transaction that is rolled back, or gets its own schema. When the suite ends the container is removed. Every run and every developer gets an identical fresh database.",
                "Start the real database in a container, migrate, test, throw it away. Every run is identical and isolated.")
tc_how.box(20, 100, 150, 70, "test suite", "blue")
tc_how.arrow(176, 135, 256, 135, label="start", lx=216, ly=121)
tc_how.icon("box", 262, 90, 1.5, fill="y")
tc_how.note(307, 200, "postgres:16 (= prod)", "pen")
tc_how.arrow(356, 135, 436, 135, label="migrate", lx=396, ly=121)
tc_how.box(442, 100, 160, 70, "tests", "green", sub="tx rolled back each")
tc_how.arrow(608, 135, 680, 135, label="stop", lx=644, ly=121)
tc_how.icon("bin", 684, 110, 1.0)
tc_how.note(380, 260, "same on every laptop and every CI run", "green")

CONTAINERS = dict(
    slug="testcontainers",
    kicker="a.k.a. “a fresh hotel room”",
    tldr="For integration tests, don't share a test database or swap in SQLite. <b>Start the real dependency</b> (the same Postgres, Redis or Kafka version as production) <b>in a container</b> for the test run, run the migrations, <b>isolate each test</b> (rollback or a fresh schema), and <b>throw it away</b> afterwards. Real behaviour, no collisions, identical everywhere.",
    chips=[("Family", "integration testing"), ("Library", "Testcontainers (Java, Go, .NET, Node, Python…)"), ("Needs", "Docker or a compatible runtime"), ("Pairs with", "test pyramid (middle layer), fakes")],
    problem="""  <p class="lead">Database code needs a real database to test. A <span class="hl-pink">shared test server</span> means runs trample each other; an <span class="hl-pink">in-memory substitute</span> means you're not testing what production runs.</p>
  <ul>
    <li>Two CI runs insert the same user and both fail.</li>
    <li>The shared database is on an old schema; tests fail for no reason.</li>
    <li>Queries using JSONB, upserts or row locks pass on SQLite and fail in production.</li>
  </ul>""",
    problem_figs=[tc_problem],
    analogy_side="the hotel room",
    analogy="""  <p>Every hotel guest gets a <b>freshly made room</b>, identical to the others, <b>theirs alone</b>, and it's <b>cleaned when they leave</b>. You never inherit the last guest's mess.</p>
  <ul>
    <li>The room is a <b>container</b> started for your run.</li>
    <li>Identical rooms are the <b>same image version</b> everywhere.</li>
    <li>Cleaning up is <b>removing the container</b>, automatically.</li>
  </ul>""",
    analogy_figs=[tc_analogy],
    map=[("A fresh room per guest", "A new database container per test run"),
         ("Identical rooms", "Pinned image: <code>postgres:16.4</code>, same as prod"),
         ("Making the bed", "Running migrations at start-up"),
         ("Not sharing with strangers", "Per-test isolation (rollback or schema)"),
         ("Cleaning after check-out", "Container removed when tests finish")],
    how_side="start, migrate, isolate, discard",
    how="""  <p>Containers start in a few seconds. Start <b>one per test run</b> (not per test) and isolate tests inside it, so you keep realism without paying start-up time a thousand times.</p>""",
    how_figs=[tc_how],
    steps=[("Pin the production version", "<code>postgres:16.4</code>, not <code>latest</code>."),
           ("Start once per run", "A global setup starts the container and exports its connection string."),
           ("Migrate", "Run the same migrations production runs."),
           ("Isolate each test", "Wrap each test in a transaction and roll back, or give each worker its own schema or database."),
           ("Clean up automatically", "Testcontainers' reaper removes containers even if the run crashes."),
           ("Keep it in the middle layer", "Use it for repositories and adapters, not every unit test.")],
    vocab=[("Container", "An isolated process with its own filesystem image."),
           ("Image tag", "The exact version of the software in the container."),
           ("Global setup", "Code that runs once before all tests."),
           ("Transaction rollback", "Undoing a test's writes at the end."),
           ("Ryuk / reaper", "Testcontainers' cleanup helper."),
           ("Environment parity", "Tests run against what production runs.")],
    code=dict(file="test/global-setup.ts + users.int.test.ts", note="Testcontainers + Vitest", src="""
import { PostgreSqlContainer } from "@testcontainers/postgresql";

export async function setup() {
  const pg = await new PostgreSqlContainer("postgres:16.4").start();   // ~3 s
  process.env.DATABASE_URL = pg.getConnectionUri();
  await runMigrations(process.env.DATABASE_URL);
  return () => pg.stop();                                              // teardown
}

// each test runs in a transaction that is always rolled back
beforeEach(async () => { tx = await db.begin(); });
afterEach(async () => { await tx.rollback(); });

it("upserts by email", async () => {
  const repo = new PostgresUserRepo(tx);

  await repo.upsert(aUser({ email: "ana@x.io", name: "Ana" }));
  await repo.upsert(aUser({ email: "ana@x.io", name: "Ana T." }));

  expect(await repo.countByEmail("ana@x.io")).toBe(1);
});
"""),
    tools="tools: Testcontainers (Node, Java, Go, .NET, Python, Rust), Docker Compose for local stacks, GitHub Actions service containers, pg_tmp, Neon/Supabase branching for preview databases.",
    gains=["<b>Real behaviour</b>: the same engine and version as production.",
           "<b>No collisions</b>: every run gets its own database.",
           "<b>Identical everywhere</b>: laptops and CI match.",
           "<b>Self-cleaning</b>: nothing left behind."],
    losses=["<b>Slower than in-memory</b>: seconds to start.",
            "<b>Needs Docker</b> on laptops and CI.",
            "<b>More CI resources</b> (memory, image pulls).",
            "<b>Still not production</b>: no real data volume or network."],
    baseline="Each line compares integration tests against a <b>shared test database or SQLite</b> to tests against a <b>throwaway container</b> of the production engine.",
    ratings=[(3, 4, "One setup file; tests look normal."),
             (4, 3, "A few seconds of start-up per run."),
             (2, 5, "Real SQL, constraints and locking are exercised."),
             (2, 5, "No shared state between runs or people."),
             (3, 4, "Each test starts from a known state."),
             (3, 4, "Schema changes come from the real migrations."),
             (2, 5, "Same engine and version as production."),
             (4, 3, "Docker and CI minutes cost a little."),
             (2, 4, "Parallel workers get their own schemas.")],
    pitfalls=[("A container per test", "1,000 tests × 3 s start-up.", "one container per run; isolate inside it."),
              ("Using <code>latest</code>", "A new major version breaks tests overnight.", "pin the exact production version."),
              ("Tests depending on each other's data", "Test B passes only after test A inserted a row.", "roll back or reset per test; build data in each test."),
              ("Everything becomes an integration test", "The suite slows to 20 minutes.", "keep logic in fast unit tests; containers for adapters.")],
    use=["Repositories, SQL queries and migrations.",
         "Message consumers (Kafka, RabbitMQ) and caches (Redis).",
         "Anything where an in-memory substitute behaves differently."],
    skip=["Pure business logic (unit tests with fakes).",
          "Managed cloud services with no faithful container image.",
          "Environments where Docker is unavailable (use a CI service container instead)."],
    related=["<b>Fakes</b>", "<b>Test pyramid</b>", "<b>Parallel &amp; selective runs</b>", "<b>Expand &amp; contract</b> (Vol. 3)"],
    quiz=[("Why not test Postgres code against SQLite?", "They differ in SQL features, types, locking and constraints, so passing tests don't prove production behaviour."),
          ("Why start one container per run rather than per test?", "Start-up takes seconds; isolating tests inside one container keeps the suite fast."),
          ("How do you isolate tests inside one database?", "Wrap each test in a transaction and roll back, or give each worker its own schema."),
          ("Why pin the image version?", "So tests match production and don't break when a new version is released.")],
    remember="Every run gets a <span class=\"hl\">fresh room</span>, the <span class=\"hl\">same</span> as production, cleaned on <span class=\"hl\">check-out</span>.",
    sources=["Testcontainers documentation (testcontainers.com).",
             "Martin Fowler / Ham Vocke, “The Practical Test Pyramid”, integration tests.",
             "AtomicJar, “Testcontainers best practices”.",
             "PostgreSQL docs, “Transactions”."],
)

# ------------------------------------------------------------------ 08 Contract Testing
ct_problem = Doodle(760, 260, "Doodle of two teams. The orders service renames the field price to amount and all its tests pass. The mobile app's tests also pass, because they use an old mock of the orders API. In production the app shows a price of undefined. The only way to catch it was a slow shared staging environment.",
                    "Both sides green, production broken: each team tested against its own idea of the API.")
ct_problem.box(20, 40, 200, 70, "orders API", "blue", sub="price → amount ✓")
ct_problem.box(540, 40, 200, 70, "mobile app", "green", sub="mocked old API ✓")
ct_problem.arrow(226, 75, 534, 75, color="red", both=True, label="nobody checks the gap", lx=380, ly=60)
ct_problem.box(260, 160, 240, 60, "“Price: undefined”", "pink", stroke="red", size=18)
ct_problem.note(380, 248, "found by customers, not tests", "red")

ct_analogy = Doodle(760, 250, "Doodle of a plug and a socket. The appliance maker and the electrician never meet, but both build to the same written standard. Each checks their own side against the standard, so the plug always fits.",
                    "Plug and socket makers never meet; both test against the same written standard.")
ct_analogy.icon("plug", 60, 50, 2.0, fill="y")
ct_analogy.note(110, 200, "appliance maker")
ct_analogy.icon("ledger", 340, 40, 1.6, fill="green")
ct_analogy.note(385, 160, "the standard", "green")
ct_analogy.box(560, 60, 120, 90, None, "paper", rx=8)
ct_analogy.raw('<path class="d" d="M600 90 v20 M640 90 v20"/>')
ct_analogy.note(620, 200, "socket maker")
ct_analogy.arrow(200, 100, 330, 100, dash=True)
ct_analogy.arrow(550, 100, 440, 100, dash=True)

ct_how = Doodle(760, 300, "Consumer-driven contract testing. The mobile app's tests run against a mock provider and record a contract file saying: GET orders 42 returns id, status and price as a number. The contract is published to a broker. The orders service's CI replays every consumer contract against the real service. Can-I-deploy checks the broker before release.",
                "Consumers record what they need; the provider replays those needs in its own CI. No shared staging needed.")
ct_how.box(20, 40, 180, 70, "mobile app tests", "green", size=17)
ct_how.arrow(206, 75, 290, 75, label="records", lx=248, ly=61)
ct_how.icon("ledger", 296, 30, 1.2, fill="y")
ct_how.note(332, 120, "contract.json", "pen")
ct_how.arrow(380, 75, 460, 75, label="publish", lx=420, ly=61)
ct_how.box(466, 40, 140, 70, "broker", "y", size=18)
ct_how.arrow(536, 114, 536, 170, label="replay", lx=550, ly=146, anchor="start")
ct_how.box(436, 176, 200, 70, "orders API CI", "blue", sub="verifies ✓ / ✗", size=17)
ct_how.note(200, 200, "GET /orders/42 → { id, status, price: number }", "pen")
ct_how.note(380, 280, "can-i-deploy? asks the broker before release", "green")

CONTRACT = dict(
    slug="contract-testing",
    kicker="a.k.a. “plug and socket”",
    tldr="When a service and its clients are built by different teams, each side's tests can pass against <b>its own idea of the API</b> while production breaks. With <b>consumer-driven contracts</b>, each client records <b>exactly what it needs</b> (request and response shape) into a contract, and the provider <b>replays every contract in its CI</b>. Breaking changes fail the provider's build, <b>before deploy</b>, without a shared staging environment.",
    chips=[("Family", "integration between teams"), ("Tools", "Pact, Spring Cloud Contract, schema checks"), ("Style", "consumer-driven (CDC)"), ("Pairs with", "API gateway (Vol. 1), micro-frontends (Vol. 2)")],
    problem="""  <p class="lead">Each team mocks the other side. The mocks are written once and <span class="hl-pink">never updated</span>, so both suites stay green while the real services drift apart.</p>
  <ul>
    <li>A field is renamed; every client breaks in production.</li>
    <li>The only real check is a slow, shared staging environment that's always half broken.</li>
    <li>Providers are afraid to change anything because they don't know who uses what.</li>
  </ul>""",
    problem_figs=[ct_problem],
    analogy_side="plug and socket",
    analogy="""  <p>The company that makes your kettle and the electrician who wired your kitchen <b>never meet</b>. Both build to the <b>same written standard</b>, and each checks their own side against it. So the plug fits, every time.</p>
  <ul>
    <li>The standard is the <b>contract</b>.</li>
    <li>Each side tests <b>alone</b>, against the contract, not against each other.</li>
    <li>With consumer-driven contracts, the plug makers write down what they need, and the socket maker checks every one.</li>
  </ul>""",
    analogy_figs=[ct_analogy],
    map=[("The written plug standard", "The contract file (requests + expected responses)"),
         ("Kettle maker", "The consumer (mobile app, frontend, other service)"),
         ("Socket maker", "The provider (orders API)"),
         ("Each checks their own side", "Consumer tests record; provider CI verifies"),
         ("“Is it safe to sell?”", "<code>can-i-deploy</code> against the broker")],
    how_side="record on one side, replay on the other",
    how="""  <p>A contract captures only what the consumer <b>actually uses</b>, so providers can freely change everything else and know immediately when they'd break someone.</p>""",
    how_figs=[ct_how],
    steps=[("Write consumer tests", "Against a mock provider generated by the tool; the interactions are saved as a contract."),
           ("Publish the contract", "To a broker (Pact Broker / PactFlow), tagged with the consumer's version and branch."),
           ("Verify on the provider", "The provider's CI starts the real service and replays every consumer's contract."),
           ("Use provider states", "“Given order 42 exists” sets up data for each interaction."),
           ("Gate deploys", "<code>can-i-deploy</code> checks that the versions about to meet in production have verified contracts.")],
    vocab=[("Consumer", "The side that calls an API."),
           ("Provider", "The side that serves the API."),
           ("Contract", "Recorded interactions the consumer relies on."),
           ("Broker", "Server that stores contracts and verification results."),
           ("Provider state", "Named setup data for an interaction."),
           ("Schema test", "Checking responses against OpenAPI/JSON Schema only.")],
    code=dict(file="orders.pact.test.ts", note="Pact JS (consumer side)", src="""
const provider = new PactV3({ consumer: "mobile-app", provider: "orders-api" });

it("shows an order's price", async () => {
  provider
    .given("order 42 exists")
    .uponReceiving("a request for order 42")
    .withRequest({ method: "GET", path: "/orders/42" })
    .willRespondWith({
      status: 200,
      body: { id: like(42), status: like("paid"), price: decimal(19.99) },
    });

  await provider.executeTest(async (mock) => {
    const order = await ordersClient(mock.url).get(42);
    expect(order.price).toBe(19.99);
  });
});
// provider CI:  pact verify --provider orders-api   →  fails if "price" disappears
"""),
    tools="tools: Pact and PactFlow (many languages), Spring Cloud Contract, Specmatic, OpenAPI diff tools (oasdiff) for breaking-change checks, GraphQL schema checks (Apollo GraphOS, graphql-inspector).",
    gains=["<b>Catches breaking API changes</b> before deploy.",
           "<b>No shared staging</b> needed to test integration.",
           "<b>Providers know who uses what</b>, so they can change safely.",
           "<b>Fast</b>: runs in each team's normal CI."],
    losses=["<b>Tooling and a broker</b> to set up and run.",
            "<b>Learning curve</b>: provider states, matchers, versions.",
            "<b>Checks shape, not meaning</b>: business behaviour still needs tests.",
            "<b>Needs buy-in</b> from both teams."],
    baseline="Each line compares <b>each team mocking the other plus a shared staging environment</b> to <b>consumer-driven contract tests</b> with a broker.",
    ratings=[(3, 2, "New tools and concepts to learn."),
             (1, 4, "Minutes in each team's CI instead of a staging cycle."),
             (2, 4, "Breaking changes to used fields are caught."),
             (1, 4, "No shared, half-broken environment."),
             (1, 5, "A failure names the consumer, interaction and field."),
             (2, 4, "Providers can change unused fields freely."),
             (3, 3, "Real provider, but only the recorded interactions."),
             (2, 3, "Broker and setup cost; staging costs drop."),
             (1, 5, "Works across many teams and services.")],
    pitfalls=[("Contracts that test business logic", "Every pricing rule is encoded in the contract.", "contracts check shape and key interactions; logic stays in provider tests."),
              ("Over-specified responses", "Exact values everywhere; any data change breaks it.", "use type matchers (<code>like</code>, <code>decimal</code>)."),
              ("Skipping can-i-deploy", "Contracts are verified but deploys don't check them.", "gate every deploy on the broker."),
              ("Only the provider writes contracts", "The “contract” is whatever the provider says.", "let consumers record what they actually use.")],
    use=["Services and clients owned by different teams.",
         "Many consumers of one API (web, mobile, partners).",
         "Replacing slow shared staging environments."],
    skip=["A frontend and backend in one repo, deployed together.",
          "Public APIs with unknown consumers (use schema diff + versioning).",
          "One team owning both sides with good integration tests."],
    related=["<b>Test doubles</b>", "<b>Fakes</b>", "<b>API gateway</b> (Vol. 1)", "<b>Micro-frontends</b> (Vol. 2)"],
    quiz=[("Why can both teams' tests pass while production breaks?", "Each tests against its own mock of the other side, and those mocks drift from reality."),
          ("Who writes the contract in consumer-driven contract testing?", "The consumer, by recording the interactions it actually relies on."),
          ("What does the provider do with contracts?", "Replays them against the real service in its CI and fails if any expectation is broken."),
          ("What does can-i-deploy answer?", "Whether the version you're about to deploy has verified contracts with the versions of its partners in that environment.")],
    remember="Build to the <span class=\"hl\">standard</span>, and let every <span class=\"hl\">plug</span> tell the socket what it needs.",
    sources=["Ian Robinson, “Consumer-Driven Contracts: A Service Evolution Pattern” (martinfowler.com).",
             "Pact documentation (docs.pact.io).",
             "Spring Cloud Contract reference.",
             "Sam Newman, <i>Building Microservices</i> (2nd ed.), ch. 9."],
)

NOTES = [DOUBLES, FAKES, CONTAINERS, CONTRACT]
