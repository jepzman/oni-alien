# Vol. 4 · Reliability & speed: Controlled Time & Randomness, Flaky Test Quarantine, Parallel & Selective Runs.

# ------------------------------------------------------------------ 13 Controlled Time & Randomness
dt_problem = Doodle(760, 250, "Doodle of a calendar showing the 31st of the month and a clock at 23:59. A test that checks a subscription renews next month passes all month, then fails on the 31st, at midnight, in a different time zone on the CI server, and when the random coupon code happens to start with a zero.",
                    "Tests that read the real clock and real randomness pass most days, and fail on the 31st at 23:59.")
dt_problem.icon("calendar", 30, 40, 1.8, fill="y")
dt_problem.head(80, 186, "31", size=30)
dt_problem.icon("clock", 190, 50, 1.6, color="red")
dt_problem.note(240, 170, "23:59 UTC", "red")
dt_problem.note(560, 50, "passes on the 12th ✓", "green")
dt_problem.note(560, 90, "fails on the 31st ✗", "red")
dt_problem.note(560, 130, "fails on CI (other time zone) ✗", "red")
dt_problem.note(560, 170, "fails if Math.random() < 0.01 ✗", "red")
dt_problem.note(560, 220, "“works on my machine”", "pen")

dt_analogy = Doodle(760, 250, "Doodle of a cinema projector playing a film. Unlike a live sports broadcast, the film is identical every time: the same frames in the same order, whatever the weather or the time of day. You can pause it, rewind it, and jump to any minute.",
                    "A film, not a live broadcast: identical every showing, and you can jump to any minute.")
dt_analogy.icon("tv", 40, 50, 1.8)
dt_analogy.note(105, 200, "live: never the same", "red")
dt_analogy.icon("camera", 360, 60, 1.6, fill="y")
dt_analogy.line("M470 110 h240", dash=True)
for i in range(5):
    dt_analogy.box(480 + i * 46, 90, 36, 40, None, "paper", rx=2)
dt_analogy.note(590, 200, "film: same frames, any minute", "green")

dt_how = Doodle(760, 290, "Controlled time and randomness. Production code receives a clock, a random generator and an id generator as dependencies. Production uses the system clock and crypto random. Tests pass a fixed clock set to 31 January at 23:59 UTC, a seeded random generator and sequential ids, and can advance the clock by one minute to test the renewal.",
                "Inject the clock, randomness and ids. Production gets real ones; tests get fixed, seeded, steppable ones.")
dt_how.box(260, 20, 240, 70, "renewSubscription()", "blue", size=17)
for i, (t, sub) in enumerate([("clock", "now()"), ("random", "next()"), ("ids", "newId()")]):
    dt_how.box(20 + i * 250, 140, 220, 56, t, "y", sub=sub, size=17)
    dt_how.arrow(130 + i * 250, 136, 380, 94)
dt_how.note(130, 230, "test: fixed 2027-01-31 23:59Z", "green")
dt_how.note(380, 230, "test: seed 42", "green")
dt_how.note(630, 230, "test: id-1, id-2…", "green")
dt_how.note(380, 270, "clock.advance(1 min) → test the boundary on purpose", "pen")

DETERMINISTIC = dict(
    slug="deterministic-tests",
    kicker="a.k.a. “a film, not a live broadcast”",
    tldr="Anything that changes between runs (<b>the clock</b>, <b>time zones</b>, <b>random numbers</b>, <b>generated ids</b>) makes tests pass today and fail tomorrow. <b>Inject</b> them as dependencies: production gets the real ones, tests get a <b>fixed clock</b>, a <b>seeded random</b> and <b>predictable ids</b>. Then test the scary moments (month end, midnight, leap day) <b>on purpose</b>.",
    chips=[("Family", "test reliability"), ("Sources of chaos", "now(), time zones, Math.random(), UUIDs, ordering"), ("Tools", "fake timers, seeded RNGs, TZ pinning"), ("Pairs with", "flaky test quarantine, property-based testing")],
    problem="""  <p class="lead">Code that calls <code>new Date()</code> or <code>Math.random()</code> directly behaves <span class="hl-pink">differently every run</span>. Its tests pass on most days and fail on a few, which is the worst kind of test.</p>
  <ul>
    <li>“Renews next month” fails on 31 January.</li>
    <li>Passes on laptops in Amsterdam, fails on CI in UTC.</li>
    <li>One random value in a hundred triggers an untested path.</li>
    <li>Tests <code>sleep(2000)</code> waiting for time to pass, and are slow and still flaky.</li>
  </ul>""",
    problem_figs=[dt_problem],
    analogy_side="a film, not a live broadcast",
    analogy="""  <p>A <b>live broadcast</b> is never the same twice. A <b>film</b> plays the same frames in the same order every showing, and you can <b>pause</b>, <b>rewind</b> and <b>jump to minute 87</b>. Good tests are films.</p>
  <ul>
    <li>The projector's frame counter is an injected <b>clock</b>.</li>
    <li>Jumping to a scene is <b>setting or advancing time</b>.</li>
    <li>The same print every showing is a <b>seeded</b> random generator.</li>
  </ul>""",
    analogy_figs=[dt_analogy],
    map=[("Live broadcast", "Code reading the real clock and randomness"),
         ("A film print", "Injected clock, seeded random, predictable ids"),
         ("Jump to minute 87", "Set the clock to 2027-01-31 23:59Z"),
         ("Fast-forward", "<code>clock.advance(minutes(1))</code> instead of sleep"),
         ("Same print every showing", "Same seed, same results")],
    how_side="make time and chance inputs",
    how="""  <p>Treat time, randomness and ids as <b>inputs</b>, like any other argument. Then the edge cases become ordinary test cases you choose deliberately.</p>""",
    how_figs=[dt_how],
    steps=[("Find the hidden inputs", "Search for <code>Date.now</code>, <code>new Date()</code>, <code>Math.random</code>, <code>randomUUID</code>, <code>setTimeout</code>."),
           ("Inject them", "A <code>Clock</code>, <code>Random</code> and <code>IdGenerator</code> passed in, with real defaults in production."),
           ("Pin the environment", "Run tests with <code>TZ=UTC</code> and a fixed locale."),
           ("Use fake timers", "Advance time instead of sleeping (<code>vi.useFakeTimers()</code>, <code>vi.setSystemTime</code>)."),
           ("Test the edges on purpose", "Month ends, leap days, DST switches, midnight, year boundaries."),
           ("Log seeds", "When randomness is part of the test, print the seed so failures can be replayed.")],
    vocab=[("Deterministic", "Same inputs, same result, every time."),
           ("Injected clock", "A time source passed in rather than read globally."),
           ("Fake timers", "Test helpers that control timers and the date."),
           ("Seed", "Starting value that makes random output repeatable."),
           ("DST", "Daylight saving time: days with 23 or 25 hours."),
           ("Hidden input", "Something code reads that the test doesn't control.")],
    code=dict(file="renewal.ts + renewal.test.ts", note="Vitest", src="""
export const systemClock = { now: () => new Date() };

export function nextRenewal(sub: Subscription, clock = systemClock) {
  return addMonthsClamped(sub.renewsOn ?? clock.now(), 1);    // 31 Jan → 28 Feb
}

// test: choose the scary moment on purpose
const fixed = (iso: string) => ({ now: () => new Date(iso) });

it("renews on the last day of February from 31 January", () => {
  const clock = fixed("2027-01-31T23:59:00Z");

  const next = nextRenewal(aSubscription().build(), clock);

  expect(next.toISOString()).toBe("2027-02-28T23:59:00.000Z");
});

it("expires a trial exactly 14 days later", () => {
  vi.useFakeTimers({ now: new Date("2027-03-01T00:00:00Z") });
  const trial = startTrial();
  vi.advanceTimersByTime(days(14));            // no sleeping
  expect(trial.isExpired()).toBe(true);
});
"""),
    tools="tools: Vitest/Jest fake timers and <code>setSystemTime</code>, Sinon fake timers, freezegun and time-machine (Python), <code>java.time.Clock</code>, seedable RNGs (seedrandom, pure-rand), <code>TZ=UTC</code> in the test script.",
    gains=["<b>Same result every run</b>, on every machine.",
           "<b>Edge cases on demand</b>: month end, DST, leap years.",
           "<b>No sleeping</b>: time-based tests run instantly.",
           "<b>Replayable</b> failures with seeds."],
    losses=["<b>Extra parameters</b> (clock, random, ids) to pass around.",
            "<b>Fake timers can surprise</b> async code and libraries.",
            "<b>Real-time bugs</b> can hide if you never test real clocks."],
    baseline="Each line compares tests of code that <b>reads the real clock and randomness</b> to the same tests with <b>injected, controlled</b> time, randomness and ids.",
    ratings=[(3, 3, "A few extra parameters; clearer intent."),
             (2, 5, "No sleeps: advance time instantly."),
             (2, 4, "Time edge cases are tested deliberately."),
             (1, 5, "No more “fails on the 31st”."),
             (3, 4, "A failing date test names the exact moment."),
             (3, 4, "Tests don't break as the calendar moves on."),
             (3, 3, "Controlled, not real, time."),
             (3, 4, "Cheap once the seams exist."),
             (3, 4, "Safe to run anywhere, in parallel.")],
    pitfalls=[("Fixing one test, not the code", "Mocking <code>Date</code> globally in one test file.", "inject a clock into the code itself."),
              ("Forgetting time zones", "Green locally, red on UTC CI.", "set <code>TZ=UTC</code> for tests; test other zones deliberately."),
              ("sleep() in tests", "Slow and still racy.", "fake timers or polling with a deadline."),
              ("Unseeded randomness", "A random failure nobody can reproduce.", "seed it and log the seed.")],
    use=["Anything involving dates: billing, trials, expiry, scheduling.",
         "Code that generates ids, tokens or random choices.",
         "Timers, retries and debouncing."],
    skip=["Truly time-independent pure logic.",
          "A small set of real-clock smoke tests that verify the wiring."],
    related=["<b>Flaky test quarantine</b>", "<b>Property-based testing</b>", "<b>Test doubles</b>", "<b>Retry with backoff</b> (Vol. 1)"],
    quiz=[("Why is calling new Date() inside business logic a testing problem?", "It's a hidden input that changes every run, so results depend on when and where tests run."),
          ("How do you test that a trial expires after 14 days without waiting?", "Use fake timers or an injected clock and advance it by 14 days."),
          ("Why set TZ=UTC for tests?", "So date results don't depend on the machine's time zone."),
          ("Name three date edge cases worth testing deliberately.", "Month end (31st), leap day, daylight-saving switches (also midnight and year boundaries).")],
    remember="Show a <span class=\"hl\">film</span>, not a <span class=\"hl\">live broadcast</span>, and jump to the <span class=\"hl\">31st</span> on purpose.",
    sources=["Vitest docs, “Mocking: Dates and Timers”.",
             "Martin Fowler, “Eradicating Non-Determinism in Tests”.",
             "Oracle docs, <code>java.time.Clock</code>.",
             "Zach Holman, “UTC is enough for everyone… right?”."],
)

# ------------------------------------------------------------------ 14 Flaky Test Quarantine
fl_problem = Doodle(760, 250, "Doodle of a CI history for one test showing green, green, red, green, red, green with no code changes. Developers' reaction is to press re-run. Over time everyone ignores red builds, and a real failure gets merged because people assumed it was just flaky again.",
                    "Same code, random results. Everyone learns to press “re-run”, then a real failure slips through.")
for i, ok in enumerate([1, 1, 0, 1, 0, 1, 1, 0]):
    dt = 40 + i * 60
    fl_problem.circle(dt, 70, 20, "green" if ok else "pink", stroke="" if ok else "red")
fl_problem.note(250, 130, "same commit, 8 runs", "pen")
fl_problem.box(560, 40, 170, 60, "↻ re-run", "y", size=20)
fl_problem.note(380, 190, "“it's just flaky” → a real bug gets merged", "red")
fl_problem.note(380, 230, "trust in the suite: gone", "red")

fl_analogy = Doodle(760, 250, "Doodle of a smoke alarm that goes off randomly, even with no smoke. People start taking out the battery. The right move is to move the faulty alarm to a workbench, put a temporary replacement up, and repair it, rather than ignoring every alarm in the house.",
                    "A smoke alarm that beeps at random: take it to the workbench and fix it, don't pull every battery.")
fl_analogy.icon("bell", 60, 50, 1.8, color="red")
fl_analogy.note(115, 180, "beeps for no reason", "red")
fl_analogy.arrow(200, 100, 330, 100, color="red", label="✗ pull the battery", lx=265, ly=86)
fl_analogy.note(390, 106, "all alarms ignored", "red", anchor="start")
fl_analogy.arrow(200, 160, 330, 200, color="green", label="✓ to the workbench", lx=250, ly=236)
fl_analogy.icon("kitchen", 340, 170, 1.0)
fl_analogy.note(440, 210, "repair, test, put back", "green", anchor="start")

fl_how = Doodle(760, 290, "Flaky test quarantine workflow. CI detects a flaky test when it fails and then passes on retry with the same commit. The test is automatically tagged as quarantined and moved to a separate non-blocking job, and a ticket is opened with an owner and a deadline. The owner finds the root cause, such as shared state, timing or order dependence, fixes it, and the test returns to the blocking suite.",
                "Detect, quarantine (non-blocking), assign an owner, fix the root cause, bring it back. The main suite stays trusted.")
steps = [("detect", "fail → pass on retry", "y"), ("quarantine", "non-blocking job", "pink"), ("ticket", "owner + deadline", "blue"), ("fix cause", "state · timing · order", "green")]
for i, (t, sub, f) in enumerate(steps):
    fl_how.box(10 + i * 188, 60, 172, 84, t, f, sub=sub, size=19, subsize=15)
    if i:
        fl_how.arrow(10 + i * 188 - 14, 102, 10 + i * 188 - 2, 102)
fl_how.arrow(660, 150, 100, 150, dash=True, color="green", curve=(380, 260), label="back in the main suite", lx=380, ly=232)
fl_how.note(380, 30, "the blocking suite only holds tests you trust", "pen")

FLAKY = dict(
    slug="flaky-tests",
    kicker="a.k.a. “the alarm that beeps at random”",
    tldr="A <b>flaky test</b> passes and fails on the <b>same code</b>. Left alone, flakes teach everyone to press “re-run” and ignore red. <b>Detect</b> them automatically (fail then pass on retry), <b>quarantine</b> them into a non-blocking job so the main suite stays trusted, give each an <b>owner and a deadline</b>, and <b>fix the root cause</b>: shared state, timing, order or the outside world.",
    chips=[("Family", "test reliability"), ("Usual causes", "async timing, shared state, order, time, network"), ("Tools", "retries with reporting, flaky dashboards"), ("Pairs with", "controlled time &amp; randomness, throwaway containers")],
    problem="""  <p class="lead">One flaky test costs a re-run. A hundred flaky tests cost the team's <span class="hl-pink">trust in red builds</span>, and then real failures get merged.</p>
  <ul>
    <li>“Just re-run it” becomes the team's reflex.</li>
    <li>Merges wait for green by luck; CI time doubles.</li>
    <li>A genuine regression is dismissed as “probably flaky”.</li>
  </ul>""",
    problem_figs=[fl_problem],
    analogy_side="the smoke alarm that beeps at random",
    analogy="""  <p>If one smoke alarm beeps for no reason, people start <b>pulling batteries</b>, and soon nobody reacts to <i>any</i> alarm. The right move: <b>take that alarm to the workbench</b>, keep the others working, repair it, test it and <b>put it back</b>.</p>
  <ul>
    <li>Pulling batteries is <b>“just re-run it”</b>.</li>
    <li>The workbench is <b>quarantine</b>.</li>
    <li>Putting it back is <b>returning the test to the blocking suite</b> once fixed.</li>
  </ul>""",
    analogy_figs=[fl_analogy],
    map=[("An alarm beeping for no reason", "A test failing on unchanged code"),
         ("Pulling every battery", "Ignoring red builds / blind re-runs"),
         ("The workbench", "A quarantined, non-blocking test job"),
         ("A repair ticket", "An owner and a deadline for the flaky test"),
         ("Back on the ceiling", "The fixed test rejoins the blocking suite")],
    how_side="detect, isolate, own, fix",
    how="""  <p>Quarantine is a <b>hospital, not a graveyard</b>: tests go in with an owner and come back out fixed, or get deleted on purpose.</p>""",
    how_figs=[fl_how],
    steps=[("Detect automatically", "Retry failed tests once; if a retry passes on the same commit, record it as flaky (don't hide it)."),
           ("Quarantine", "Tag it (<code>@flaky</code>) and run it in a separate, non-blocking job that still reports."),
           ("Assign an owner and deadline", "A ticket per flaky test; a cap on how many can be quarantined."),
           ("Find the cause", "Run it 100× locally, in random order, in parallel; check timing, shared data, test order, real clock, network."),
           ("Fix and return", "Fix the cause (not with a sleep), then move it back. Delete tests nobody will fix.")],
    vocab=[("Flaky test", "Passes and fails on the same code."),
           ("Quarantine", "Running a test without letting it block merges."),
           ("Retry-on-failure", "Re-running a failed test to detect flakiness."),
           ("Order dependence", "A test that only passes after (or before) another."),
           ("Race condition", "Result depends on which async step finishes first."),
           ("Auto-waiting", "Assertions that retry until a condition holds or time runs out.")],
    code=dict(file="playwright.config.ts + checkout.spec.ts", note="Playwright", src="""
export default defineConfig({
  retries: process.env.CI ? 1 : 0,        // a pass on retry is reported as "flaky"
  reporter: [["html"], ["json", { outputFile: "results.json" }]],
  projects: [
    { name: "blocking",    grepInvert: /@quarantine/ },
    { name: "quarantine",  grep: /@quarantine/ },     // CI: continue-on-error
  ],
});

// ✗ the usual cause: a fixed sleep racing the app
await page.waitForTimeout(2000);
expect(await page.locator(".total").textContent()).toBe("€16");

// ✓ auto-waiting assertion: retries until true or timeout
await expect(page.getByTestId("total")).toHaveText("€16");

test("applies coupon @quarantine  JIRA-482 owner:ana due:2026-11-30", async () => { /* … */ });
"""),
    tools="tools: Playwright retries + flaky reporting, Jest/Vitest <code>--retry</code>, BuildPulse, Trunk Flaky Tests, Datadog Test Visibility, Gradle Develocity flaky detection, <code>--sequence.shuffle</code> to expose order dependence.",
    gains=["<b>A trusted main suite</b>: red means broken.",
           "<b>No blind re-runs</b>; faster merges.",
           "<b>Visible flakiness</b> with owners and trends.",
           "<b>Root causes fixed</b>, not hidden."],
    losses=["<b>Quarantined tests don't protect you</b> while quarantined.",
            "<b>Process overhead</b>: tickets, owners, dashboards.",
            "<b>Retries can hide flakiness</b> if not reported.",
            "<b>Risk of a quarantine graveyard</b>."],
    baseline="Each line compares a suite where <b>flaky tests block and people re-run</b> to one with <b>detection, quarantine and owned fixes</b>.",
    ratings=[(3, 3, "Tags and a second job to understand."),
             (2, 4, "No more re-run loops."),
             (2, 3, "Main suite trusted; quarantined tests temporarily don't protect."),
             (1, 5, "Red builds mean something again."),
             (3, 4, "Real failures stand out from noise."),
             (2, 4, "Root causes fixed instead of sleeps added."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer wasted CI minutes; some process cost."),
             (2, 4, "Works as the suite and team grow.")],
    pitfalls=[("Retries without reporting", "Retries quietly turn flaky tests green forever.", "report every pass-on-retry as flaky."),
              ("A quarantine graveyard", "200 quarantined tests, none being fixed.", "owner, deadline and a cap; delete tests nobody will fix."),
              ("Fixing with sleep", "<code>waitForTimeout(5000)</code> makes it slower and still racy.", "wait for a condition (auto-waiting assertions)."),
              ("Blaming the test runner", "“CI is just slow.”", "reproduce: run 100×, shuffle order, run in parallel.")],
    use=["Any suite with UI, async or integration tests.",
         "Teams where “re-run” has become a habit.",
         "Large monorepos with shared CI."],
    skip=["Tiny suites where you can fix a flake on the spot.",
          "As an excuse not to fix: quarantine is temporary."],
    related=["<b>Controlled time &amp; randomness</b>", "<b>Throwaway containers</b>", "<b>Page objects</b>", "<b>Parallel &amp; selective runs</b>"],
    quiz=[("What makes a test flaky?", "It passes and fails on the same code, because of timing, shared state, order, time or external systems."),
          ("Why are flaky tests worse than no tests?", "They teach people to ignore red builds, so real failures get dismissed and merged."),
          ("What does quarantine mean?", "The test still runs and reports, but in a non-blocking job, with an owner and deadline to fix it."),
          ("What's the right fix for a test that sleeps 2 seconds?", "Wait for the actual condition with an auto-waiting assertion or polling, not a fixed delay.")],
    remember="Don't pull every <span class=\"hl\">battery</span>. Take the beeping alarm to the <span class=\"hl\">workbench</span>, and bring it <span class=\"hl\">back</span>.",
    sources=["Martin Fowler, “Eradicating Non-Determinism in Tests”.",
             "Google Testing Blog, “Flaky Tests at Google and How We Mitigate Them”.",
             "Luo et al., “An Empirical Analysis of Flaky Tests” (FSE 2014).",
             "Playwright docs, “Retries” and “Auto-waiting”."],
)

# ------------------------------------------------------------------ 15 Parallel & Selective Runs
ps_problem = Doodle(760, 250, "Doodle of a single CI job running six thousand tests one after another for forty-two minutes, for a pull request that only changed a README typo in the billing package. Developers context-switch while they wait, and batch changes into huge pull requests to avoid the wait.",
                    "One worker, 6,000 tests, 42 minutes, for a typo fix in one package.")
ps_problem.box(20, 80, 160, 60, "1 CI job", "blue")
ps_problem.raw('<rect class="d d-thin f-pink" x="200" y="90" width="520" height="40" rx="3"/>')
ps_problem.note(460, 80, "6,000 tests in a row · 42 min", "red")
ps_problem.note(200, 200, "PR: fix a typo in billing/README.md", "pen", anchor="start")
ps_problem.note(200, 230, "still runs every test in the repo", "red", anchor="start")

ps_analogy = Doodle(760, 250, "Doodle of a supermarket with eight open checkout lanes instead of one, so the queue moves eight times faster. Customers with only a few items use the express lane, and nobody scans items that aren't in their basket.",
                    "Open more checkout lanes, and only scan what's in the basket.")
ps_analogy.icon("lanes", 60, 50, 2.4)
ps_analogy.note(170, 220, "8 lanes in parallel", "green")
ps_analogy.icon("bucket", 470, 60, 1.6, fill="y")
ps_analogy.note(520, 200, "scan only this basket", "green")

ps_how = Doodle(760, 290, "Parallel and selective runs. First, the build graph works out which packages a change affects: a change in billing affects billing and checkout, but not search or admin. Only those tests are selected. Then the selected tests are split across four shards by previous timing so each finishes in about the same time. The pull request gets feedback in six minutes; the full suite still runs on main and nightly.",
                "Select only the affected tests, then split them across workers by past timing. Full suite still runs on main.")
pkgs = [("billing ✎", "pink"), ("checkout", "y"), ("search", "paper"), ("admin", "paper")]
for i, (t, f) in enumerate(pkgs):
    ps_how.box(20, 20 + i * 58, 150, 44, t, f, size=16)
ps_how.arrow(170, 42, 170, 92, color="red", curve=(200, 66))
ps_how.arrow(176, 66, 280, 110, label="affected", lx=228, ly=74)
ps_how.box(286, 80, 150, 70, "selected", "y", sub="billing + checkout")
ps_how.arrow(442, 115, 554, 115, label="split by timing", lx=498, ly=100)
for i in range(4):
    ps_how.box(560, 30 + i * 46, 180, 36, f"shard {i + 1} · ~90 s", "green", size=15)
ps_how.note(380, 270, "PR feedback: 6 min · full suite on main + nightly", "green")

PARALLEL = dict(
    slug="parallel-selective",
    kicker="a.k.a. “more lanes, smaller baskets”",
    tldr="Two levers for fast feedback: <b>run tests in parallel</b> (workers and CI shards, balanced by past timing) and <b>run only the tests a change can affect</b> (using the dependency graph). Pull requests get answers in minutes, and the <b>full suite still runs</b> on main and nightly as a safety net. Tests must be <b>isolated</b> for either lever to work.",
    chips=[("Family", "test speed"), ("Levers", "parallel workers, CI sharding, test impact analysis"), ("Tools", "Vitest/Playwright shards, Nx, Turborepo, Bazel"), ("Needs", "isolated, order-independent tests")],
    problem="""  <p class="lead">Suites grow linearly with the code, and so does the wait. A <span class="hl-pink">42-minute</span> CI run changes how people work: they context-switch, batch huge PRs and stop running tests locally.</p>
  <ul>
    <li>A typo fix in one package runs 6,000 unrelated tests.</li>
    <li>One CI job uses one core while the machine has eight.</li>
    <li>Slow suites get skipped: “I'll let CI tell me.”</li>
  </ul>""",
    problem_figs=[ps_problem],
    analogy_side="the supermarket checkout",
    analogy="""  <p>A supermarket with one open lane has a long queue. <b>Open eight lanes</b> and it moves eight times faster. And nobody scans items that <b>aren't in their basket</b>.</p>
  <ul>
    <li>More lanes = <b>parallel workers and shards</b>.</li>
    <li>Balancing queues = <b>splitting by past timing</b>.</li>
    <li>Scanning only your basket = <b>selecting affected tests</b>.</li>
  </ul>""",
    analogy_figs=[ps_analogy],
    map=[("One open lane", "One CI job running every test in sequence"),
         ("Eight lanes", "Workers on each machine + several CI shards"),
         ("Balanced queues", "Shards split by previous run times"),
         ("Only your basket", "Tests for packages the change affects"),
         ("Stock-take at night", "The full suite on main and nightly")],
    how_side="select, then split",
    how="""  <p>Selection shrinks the work; parallelism shares what's left. Both need tests that don't depend on <b>order or shared state</b>, so isolation comes first.</p>""",
    how_figs=[ps_how],
    steps=[("Make tests isolated", "No shared mutable data, no order dependence; each worker gets its own database schema or container."),
           ("Use all cores", "Parallel workers in the runner (Vitest threads, Playwright workers)."),
           ("Shard in CI", "<code>--shard=1/4</code> across machines; balance by timing data."),
           ("Select affected tests", "Use the dependency graph (Nx/Turborepo/Bazel affected) or the runner's <code>--changed</code>."),
           ("Keep a full run", "On main, before release and nightly, to catch anything selection missed."),
           ("Watch the numbers", "Track p50/p95 CI time and the slowest tests; fix the outliers.")],
    vocab=[("Worker", "A process running a subset of tests in parallel."),
           ("Shard", "One slice of the suite run on its own CI machine."),
           ("Timing-based split", "Balancing shards using past test durations."),
           ("Test impact analysis", "Choosing tests based on what a change touches."),
           ("Affected graph", "Packages that depend, directly or not, on a change."),
           ("Remote cache", "Reusing results of unchanged tasks across machines.")],
    code=dict(file=".github/workflows/test.yml", note="GitHub Actions + Nx + Vitest", src="""
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix: { shard: [1, 2, 3, 4] }            # 4 machines in parallel
    steps:
      - uses: actions/checkout@v5
        with: { fetch-depth: 0 }
      - run: npm ci
      # only projects affected by this PR, split across the 4 shards
      - run: npx nx affected -t test --base=origin/main --
             --shard=${{ matrix.shard }}/4
      # on main and nightly a separate job runs:  npx nx run-many -t test
"""),
    tools="tools: Vitest/Jest workers and <code>--shard</code>, Playwright <code>--shard</code> and <code>fullyParallel</code>, Nx and Turborepo affected + remote cache, Bazel, Gradle test distribution, Knapsack Pro and CircleCI timing-based splitting, Launchable for predictive test selection.",
    gains=["<b>Minutes, not an hour</b> for PR feedback.",
           "<b>Uses the hardware</b> you already pay for.",
           "<b>Smaller, more frequent PRs</b> become practical.",
           "<b>Scales with the repo</b> instead of slowing down."],
    losses=["<b>Needs isolated tests</b>; hidden shared state surfaces as flakes.",
            "<b>Selection can miss</b> indirect effects (config, data files).",
            "<b>More CI machines</b> at once.",
            "<b>More moving parts</b>: graphs, caches, timing data."],
    baseline="Each line compares <b>one CI job running every test in sequence</b> to <b>affected-only selection plus parallel shards</b>, with a full run on main.",
    ratings=[(4, 3, "Sharding and affected graphs add CI concepts."),
             (1, 5, "42 minutes becomes about 6."),
             (4, 4, "The full suite still runs on main and nightly."),
             (3, 4, "Exposes and forces out shared-state flakes."),
             (3, 4, "Isolated tests point at one cause."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Fewer total test minutes per PR; more machines briefly."),
             (1, 5, "CI time stays flat as the repo grows.")],
    pitfalls=[("Parallelising non-isolated tests", "Shared rows and global state turn into random failures.", "isolate first: per-worker schemas, unique data."),
              ("Trusting selection blindly", "A config change affects everything, but no tests are selected.", "mark global inputs; always run the full suite on main."),
              ("Unbalanced shards", "Three shards finish in 2 minutes, one takes 20.", "split by timing data, not by file count."),
              ("Ignoring the slowest tests", "Five tests take half the time.", "track and fix the slow tail.")],
    use=["Suites slower than about 10 minutes.",
         "Monorepos with many packages.",
         "Teams that want small, frequent PRs."],
    skip=["Small suites that already finish in a minute or two.",
          "Tests that can't be isolated yet (fix that first)."],
    related=["<b>Test pyramid</b>", "<b>Flaky test quarantine</b>", "<b>Throwaway containers</b>", "<b>Competing consumers</b> (Vol. 1)"],
    quiz=[("What are the two main levers for faster CI?", "Run tests in parallel (workers and shards) and run only the tests a change can affect."),
          ("Why must tests be isolated before parallelising?", "Shared state and order dependence cause random failures when tests run at the same time or in different orders."),
          ("Why split shards by timing rather than file count?", "Files have very different run times; timing data balances shards so they finish together."),
          ("Why still run the full suite on main?", "Selection can miss indirect effects; the full run is the safety net.")],
    remember="Open more <span class=\"hl\">lanes</span>, scan only your <span class=\"hl\">basket</span>, and do a full <span class=\"hl\">stock-take</span> at night.",
    sources=["Vitest docs, “Improving Performance” and <code>--shard</code>.",
             "Playwright docs, “Parallelism” and “Sharding”.",
             "Nx docs, “Run only tasks affected by a PR”.",
             "Google, “Taming Google-Scale Continuous Testing” (ICSE SEIP 2017)."],
)

NOTES = [DETERMINISTIC, FLAKY, PARALLEL]
