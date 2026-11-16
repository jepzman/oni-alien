# Vol. 4 · going deeper (November 2026): a longer chapter inside three key notes.
# Merged into the notes by scripts/build_notes.py (load_content).

# ------------------------------------------------------------------ Test doubles
td_d1 = Doodle(760, 280, "Where doubles plug in. The signup code depends on a Mailer interface the team owns. In production an adapter implements it with the email provider's SDK; that adapter has one integration test against a sandbox. In unit tests a spy implements the same interface. The SDK itself is never mocked.",
               "Double your own interface. Test the adapter once against the real thing.")
td_d1.box(20, 90, 150, 80, "signup", "y", sub="your code", size=19, subsize=14)
td_d1.arrow(174, 130, 236, 130)
td_d1.box(240, 90, 150, 80, "Mailer", "green", sub="interface you own", size=19, subsize=14)
td_d1.arrow(394, 115, 466, 60)
td_d1.arrow(394, 145, 466, 200, dash=True)
td_d1.box(470, 20, 270, 70, "SDK adapter", "blue", sub="1 integration test (sandbox)", size=17, subsize=14)
td_d1.box(470, 170, 270, 70, "spy in unit tests", "paper", sub="records what was sent", size=17, subsize=14)
td_d1.note(20, 266, "never mock the provider's SDK directly", "red", anchor="start", size=16)

td_d2 = Doodle(760, 230, "A double drifting from reality. The stubbed payment client returns status approved. The real provider changed its response to status authorised months ago. Every unit test passes; production treats every payment as failed. A contract or recorded-response test against the real sandbox would have failed when the provider changed.",
               "A double is a claim about the real thing. Check the claim somewhere.")
td_d2.box(20, 40, 280, 80, "stub says", "green", sub="{ status: \"approved\" }", size=18, subsize=15)
td_d2.box(460, 40, 280, 80, "provider says", "pink", stroke="red", sub="{ status: \"authorised\" }", size=18, subsize=15)
td_d2.arrow(304, 80, 456, 80, both=True, color="red", label="drift", lx=380, ly=70)
td_d2.note(160, 156, "unit tests: all green", "green", size=17)
td_d2.note(600, 156, "production: every payment “fails”", "red", size=17)
td_d2.note(380, 206, "catch it: adapter test against the sandbox, run nightly", "pen", size=17)

TEST_DOUBLES_DEEP = dict(
    side="seams you own, checking commands, doubles that lie",
    intro="The note says: stub queries, verify commands, double only at boundaries you own. This chapter shows how to build those boundaries, how to check a command without tying the test to the code's insides, and how to notice when a double has stopped telling the truth about the real thing.",
    parts=[
        ("Seams you own", """  <p>A double is only as good as the place it plugs in. The cleanest place is an <b>interface your code owns</b>, shaped by what your code needs: <code>Mailer.sendWelcome(user)</code>, not the email provider's 40-method SDK. This is the ports-and-adapters idea: your logic talks to a port; an adapter connects the port to the real world.</p>
  <ul>
    <li>Unit tests plug a <b>stub, spy or fake</b> into the port. They are fast and say what the code is for.</li>
    <li>The adapter gets <b>one or two integration tests</b> against the real thing (a sandbox account, a container), proving the translation works.</li>
    <li>Nothing mocks the SDK directly. When the SDK's API changes, only the adapter and its tests change.</li>
  </ul>
  <p>A useful check: if a test needs more than two doubles to run, the code under test probably has too many collaborators, or the seam is in the wrong place.</p>""", [td_d1]),
        ("Checking a command without freezing the code", """  <p>“Verify commands” is easy to overdo. A test that asserts the exact order of eight calls breaks on every refactor, even when the behaviour is the same. Check the <b>effect that matters</b>, at the level a person would describe it:</p>
  <ul>
    <li><b>Was it sent, to whom, with what?</b> One welcome email to ana@example.com containing her name. Not which internal helper built it.</li>
    <li><b>How many times?</b> Exactly once matters for emails and payments. “At least once” usually doesn't need checking.</li>
    <li><b>Was it not sent?</b> A failed signup sends nothing. This is often the more valuable assertion.</li>
  </ul>
  <p>Prefer a <b>spy that records</b> (and assert on the record afterwards) to a mock that is told in advance what to expect: the test then reads Arrange, Act, Assert in order. And keep to <b>one verified command per test</b>; if a step sends an email and charges a card, that's two tests.</p>""", []),
        ("When a double lies", """  <p>Every stub states something about the real dependency: “the price service returns 20”, “the payment provider says approved”. When the real thing changes, the stub doesn't, and the tests keep passing on a story that is no longer true.</p>
  <ul>
    <li><b>Contract tests</b> for services you run (the previous note in this collection), so the double and the real provider are checked against the same contract.</li>
    <li><b>Adapter tests against a sandbox</b> for third parties, run nightly, so a change on their side fails a test, not a customer's payment.</li>
    <li><b>Recorded responses</b> (VCR-style cassettes) made from the real API, with an expiry date, so they are re-recorded instead of trusted for ever.</li>
    <li><b>A fake with its own contract tests</b> for things you call often (repositories), as in the Fakes note.</li>
  </ul>
  <p>Signs a double is lying: production errors in code with full test coverage, and stubs that return fields the real API doesn't have.</p>""", [td_d2]),
    ],
)

# ------------------------------------------------------------------ Contract testing
ct_d1 = Doodle(760, 280, "The release flow with a contract broker. The web app's CI runs its consumer tests and publishes the contract to the broker. The Orders service's CI fetches every consumer's contracts and verifies them against the real service, publishing the results. Before either side deploys to production, it asks the broker can-i-deploy: have the versions now in production been verified against mine? If yes, deploy and record the deployment.",
               "Both pipelines meet at the broker. can-i-deploy is the gate before production.")
ct_d1.box(20, 30, 200, 80, "web app CI", "y", sub="consumer tests → contract", size=17, subsize=13)
ct_d1.box(20, 170, 200, 80, "Orders CI", "blue", sub="verify all contracts", size=17, subsize=13)
ct_d1.box(290, 100, 180, 80, "broker", "green", sub="contracts + results", size=19, subsize=14)
ct_d1.arrow(224, 70, 286, 120, label="publish", lx=262, ly=82)
ct_d1.arrow(286, 160, 224, 200, both=True, label="fetch · report", lx=258, ly=196, anchor="start")
ct_d1.box(540, 100, 200, 80, "can-i-deploy?", "paper", sub="before prod", size=18, subsize=14)
ct_d1.arrow(474, 140, 536, 140, both=True)
ct_d1.note(640, 214, "yes → deploy, record it", "green", size=16)
ct_d1.note(640, 238, "no → which pair is unverified", "red", size=16)

CONTRACT_DEEP = dict(
    side="writing good contracts, the release flow, events and schemas",
    intro="The note explains the loop: consumers record what they need, providers replay it, a gate stops incompatible deploys. This chapter covers how to write contracts that don't break for no reason, how the broker flow works with branches and environments, and when a schema-based approach is the better choice.",
    parts=[
        ("Writing contracts that last", """  <p>A contract should hold <b>only what the consumer uses</b>, matched <b>by shape, not by value</b>. If the web app shows an order's total and status, its contract says: a response with <code>total</code> (a number) and <code>status</code> (one of placed, paid, shipped). It does not list the twelve other fields, and it doesn't require the total to be exactly 49.95.</p>
  <ul>
    <li><b>Use type matchers</b> (<code>like(49.95)</code>, <code>eachLike(...)</code>, a regex for ids). Exact values make the provider's test data a contract too.</li>
    <li><b>Leave business rules out.</b> “A cancelled order returns 409” is a contract; “the discount is 10% over €50” is the provider's own unit test.</li>
    <li><b>Name provider states in plain words</b> (“order 42 exists and is paid”), so the provider team can set them up without reading consumer code.</li>
  </ul>
  <p>Over-specified contracts are the main reason teams give up on contract testing: every harmless provider change fails a build. Minimal contracts fail only when a consumer would really break.</p>""", []),
        ("The release flow", """  <p>The broker connects two pipelines that never call each other. The consumer's CI publishes its contract, tagged with its version and branch. The provider's CI verifies <b>every contract that matters</b>: the consumers' main branches and the versions now deployed in each environment. Results go back to the broker.</p>
  <p>Before any deploy, either side asks <code>can-i-deploy</code>: “has my version been verified against the versions currently in production?” If yes, deploy, then <code>record-deployment</code> so the broker knows what is live. If no, the answer names the pair that isn't verified.</p>
  <p>Two settings keep it workable. <b>Pending contracts</b>: a new consumer expectation doesn't fail the provider's main build until the provider has passed it once, so consumers can't block providers by publishing. <b>Work-in-progress contracts</b>: the provider also verifies consumers' feature branches, so a consumer learns early whether its new need is already met.</p>""", [ct_d1]),
        ("Events, and when schemas are enough", """  <p>Contracts work for messages too. A consumer of <code>OrderPlaced</code> records the message shape it needs; the provider's test calls the code that builds the message and checks it against every consumer's contract. No broker connection or running queue is needed.</p>
  <p>Consumer-driven contracts aren't always the right tool:</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Situation</th><th scope="col">Better fit</th></tr></thead><tbody>
    <tr><td>A few internal consumers you can talk to</td><td>Consumer-driven contracts (Pact).</td></tr>
    <tr><td>A public API with unknown consumers</td><td>A published OpenAPI or AsyncAPI schema, and a breaking-change check in CI (oasdiff, a schema registry's compatibility rules).</td></tr>
    <tr><td>Events with many subscribers</td><td>A schema registry with backward compatibility enforced, plus contracts for the few critical consumers.</td></tr>
    <tr><td>A provider team that already keeps a precise OpenAPI file</td><td>Bi-directional contracts: compare consumer contracts with the provider's schema, no provider replay.</td></tr>
  </tbody></table></div>""", []),
    ],
)

# ------------------------------------------------------------------ Flaky tests
fl_d1 = Doodle(760, 280, "Why a little flakiness ruins a suite. If each of 200 tests fails by chance one time in 200, a whole run passes only about 37 percent of the time. With 20 tests at that rate it passes about 90 percent of the time. With 200 tests at one in 2,000 it passes about 90 percent of the time. Teams stop trusting red long before any single test looks bad.",
               "Small per-test flake rates multiply into a suite nobody trusts.")
for i, (label, pct, fill, stroke) in enumerate([("20 tests · 0.5% each", 90, "green", ""), ("200 tests · 0.5% each", 37, "pink", "red"), ("200 tests · 0.05% each", 90, "green", "")]):
    y = 30 + i * 70
    fl_d1.text(20, y + 30, label, "t-head", anchor="start", size=16)
    fl_d1.box(250, y + 6, round(3.5 * pct), 40, None, fill, stroke=stroke)
    fl_d1.text(262 + round(3.5 * pct), y + 32, f"{pct}% of runs green", "t", anchor="start", size=15)
fl_d1.note(380, 256, "suite pass rate = (1 − flake rate) ^ number of tests", "pen", size=17)

fl_d2 = Doodle(760, 250, "Waiting by time versus waiting by state. With a fixed sleep of two seconds, the test fails when the server takes 2.3 seconds and wastes time when it takes 0.4 seconds. Waiting for the result to appear, with a ten second limit, passes in both cases and continues as soon as the result is there.",
               "Wait for what you need to see, not for a number of seconds.")
fl_d2.head(20, 34, "sleep(2000)", anchor="start", size=17, color="red")
fl_d2.box(200, 14, 200, 34, "waits 2.0 s", "pink", size=15)
fl_d2.note(200, 74, "server took 2.3 s → fails · took 0.4 s → 1.6 s wasted", "red", anchor="start", size=16)
fl_d2.head(20, 130, "expect(total).toHaveText(…)", anchor="start", size=17, color="green")
fl_d2.box(340, 108, 70, 34, "0.4 s", "green", size=15)
fl_d2.note(340, 168, "continues the moment it appears · gives up at 10 s", "green", anchor="start", size=16)
fl_d2.note(380, 226, "same idea in back-end tests: poll for the state, with a deadline", "pen", size=17)

FLAKY_DEEP = dict(
    side="the maths of distrust, finding causes, fixing async waits",
    intro="The note sets up detection and quarantine. This chapter explains why a few flaky tests do so much damage, how to find the cause of a specific flake quickly, and how to fix the most common kind, the test that waits by the clock instead of by what it needs to see.",
    parts=[
        ("Why a little flakiness ruins a suite", """  <p>Flakiness multiplies. If each test fails by chance one time in 200 (0.5%), a single test looks fine. But a run of 200 such tests passes only when all 200 pass: 0.995<sup>200</sup> ≈ <b>37%</b>. Two runs in three are red for no reason, and people learn to press re-run.</p>
  <p>That gives a useful target. To keep a 2,000-test suite green 95% of the time, the average flake rate per test must be below about 1 in 40,000. You can't reach that by fixing tests one at a time after complaints; you need the numbers:</p>
  <ul>
    <li>Record every test result with the commit, and mark a test <b>flaky</b> when it failed and passed on the same commit.</li>
    <li>Track <b>flake rate per test</b> (flaky runs ÷ runs) and the suite's <b>green-on-first-try rate</b> each week.</li>
    <li>Work from the top of the list: a handful of tests usually cause most re-runs.</li>
  </ul>""", [fl_d1]),
        ("Finding the cause", """  <p>Most flakes fall into a few families. Each has a tell-tale sign and a way to reproduce it on purpose.</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Cause</th><th scope="col">Sign · how to reproduce</th></tr></thead><tbody>
    <tr><td><b>Timing</b> (async UI, background jobs)</td><td>Fails more on slow CI machines. Slow the CPU or network; run with a fixed sleep removed.</td></tr>
    <tr><td><b>Shared state, test order</b></td><td>Fails only with other tests. Run in random order with a fixed seed; run the test alone and with its neighbour.</td></tr>
    <tr><td><b>Parallel runs</b> (shared rows, ports, files)</td><td>Fails with more workers. Run with 1 worker, then 8.</td></tr>
    <tr><td><b>Clock and environment</b></td><td>Fails at certain times or on some machines. Set TZ, locale and the date to edge values.</td></tr>
    <tr><td><b>Real external services</b></td><td>Fails when the network or a sandbox is slow. Replace with a double or a container.</td></tr>
    <tr><td><b>Randomness</b></td><td>Fails for some generated data. Log the seed and replay it.</td></tr>
  </tbody></table></div>
  <p>Start by running the test 100 times in a loop locally (Playwright's <code>--repeat-each</code>, a shell loop elsewhere). If it never fails alone, the cause is in its neighbours or the environment, not in the test itself.</p>""", []),
        ("Fixing async waits", """  <p>The most common flaky test waits by the clock: click, sleep two seconds, check. It fails when the server takes 2.3 seconds and wastes time when it takes 0.4. The fix is always the same: <b>wait for the state you need</b>, with a deadline.</p>
  <ul>
    <li><b>In UI tests</b>, use assertions that retry until they pass or time out: <code>await expect(page.getByText("Total €49.95")).toBeVisible()</code>. Wait for something the user would see, not for “network idle”, which modern pages rarely reach.</li>
    <li><b>Control the network</b> where the test isn't about it: serve fixed responses with route mocking so timing doesn't vary.</li>
    <li><b>Turn off animations</b> and transitions in test runs, so clicks don't land on moving elements.</li>
    <li><b>In back-end tests</b> for queues and background jobs, poll for the result (the row exists, the message was published) with a short interval and a deadline, instead of sleeping.</li>
  </ul>
  <p>A retry hides the symptom; a wait on the right condition removes the cause.</p>""", [fl_d2]),
    ],
)

REVISIONS = {
    "test-doubles": dict(deep_dive=TEST_DOUBLES_DEEP),
    "contract-testing": dict(deep_dive=CONTRACT_DEEP),
    "flaky-tests": dict(deep_dive=FLAKY_DEEP),
}
