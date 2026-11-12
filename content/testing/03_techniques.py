# Vol. 4 · Smarter techniques: Property-Based, Snapshot, Mutation, Characterization tests.

# ------------------------------------------------------------------ 09 Property-Based Testing
pb_problem = Doodle(760, 250, "Doodle of a function that splits a bill, with three hand-picked example tests: one hundred split by two, ninety by three and zero by four. All pass. In production, ten euros split three ways loses a cent, and an empty name list crashes the function. Nobody thought of those inputs.",
                    "Three hand-picked examples pass. The bugs live in the inputs nobody thought to write.")
for i, (t, ok) in enumerate([("split(100, 2) ✓", True), ("split(90, 3) ✓", True), ("split(0, 4) ✓", True)]):
    pb_problem.box(20, 20 + i * 64, 220, 48, t, "green", size=17)
pb_problem.note(500, 50, "production:", "pen")
pb_problem.note(500, 90, "split(10, 3) → 3.33 × 3 = 9.99", "red")
pb_problem.note(500, 130, "a cent vanished", "red")
pb_problem.note(500, 180, "split(10, 0) → crash", "red")
pb_problem.note(500, 230, "nobody wrote those examples", "pen")

pb_analogy = Doodle(760, 250, "Doodle of a chair being tested in a furniture lab. Instead of a tester sitting on it three times, a machine drops thousands of random weights from random angles, and checks one rule each time: the chair must not break below a hundred and fifty kilograms.",
                    "A furniture lab: thousands of random loads, one rule — it must not break under 150 kg.")
pb_analogy.raw('<rect class="d f-y" x="300" y="112" width="120" height="16" rx="3"/><rect class="d f-y" x="404" y="30" width="16" height="82" rx="3"/>')
pb_analogy.line("M306 128 v92 M414 128 v92 M306 176 h108")
for i, (x, y) in enumerate([(240, 40), (330, 20), (450, 50), (260, 90), (470, 100)]):
    pb_analogy.arrow(x, y, 360 + (i - 2) * 12, 116, dash=True)
pb_analogy.icon("dice", 100, 60, 1.2, fill="y")
pb_analogy.note(130, 160, "random loads", "pen")
pb_analogy.note(600, 120, "rule: no break", "green")
pb_analogy.note(600, 146, "under 150 kg", "green")

pb_how = Doodle(760, 290, "Property-based test loop. A generator produces hundreds of random inputs, amounts and number of people. Each is run through split, and the property is checked: the parts add up to the total exactly, and no part differs from another by more than one cent. When a failure is found, the tool shrinks it to the smallest failing case, here ten cents split three ways.",
                "Generate many inputs, check a rule that must always hold, and shrink any failure to the smallest example.")
pb_how.box(20, 40, 180, 80, "generator", "y", sub="amount, people")
pb_how.arrow(206, 80, 286, 80, label="× 1,000", lx=246, ly=66)
pb_how.box(292, 40, 160, 80, "split()", "blue")
pb_how.arrow(458, 80, 538, 80)
pb_how.box(544, 30, 200, 100, "property", "green", sub="sum(parts) = total")
pb_how.arrow(644, 134, 644, 186, color="red", label="fails", lx=656, ly=166, anchor="start")
pb_how.box(470, 190, 274, 70, "shrunk: split(0.10, 3)", "pink", stroke="red", size=17)
pb_how.note(200, 220, "the tool hunts; you state the rule", "pen")

PROPERTY = dict(
    slug="property-based",
    kicker="a.k.a. “the furniture lab”",
    tldr="Instead of listing examples, state a <b>property</b>: a rule that must hold for <b>every</b> input (“the parts always add up to the total”). The tool <b>generates hundreds of random inputs</b>, including nasty edge cases, and when one fails it <b>shrinks</b> it to the smallest failing example. Great at finding the bugs nobody thought to write a test for.",
    chips=[("Family", "test technique"), ("Origin", "QuickCheck (Claessen &amp; Hughes, 2000)"), ("Libraries", "fast-check, Hypothesis, jqwik, FsCheck"), ("Pairs with", "test data builders, example tests")],
    problem="""  <p class="lead">Example tests only check the inputs you <span class="hl-pink">thought of</span>. Bugs hide in the ones you didn't: zero, negative numbers, empty lists, rounding, unicode, very large values.</p>
  <ul>
    <li>All three examples pass; a cent disappears for 10 ÷ 3.</li>
    <li>Edge cases depend on how imaginative the author was that day.</li>
    <li>Writing every combination by hand is impossible.</li>
  </ul>""",
    problem_figs=[pb_problem],
    analogy_side="the furniture lab",
    analogy="""  <p>A furniture lab doesn't test a chair by having someone sit on it three times. A <b>machine drops thousands of random loads</b> from random angles and checks <b>one rule</b> each time: “it must not break under 150 kg”. When it breaks, they find the <b>smallest load</b> that does it.</p>
  <ul>
    <li>Random loads are <b>generated inputs</b>.</li>
    <li>“Must not break under 150 kg” is the <b>property</b>.</li>
    <li>Finding the smallest breaking load is <b>shrinking</b>.</li>
  </ul>""",
    analogy_figs=[pb_analogy],
    map=[("Random loads and angles", "Generators (<code>fc.integer()</code>, <code>fc.array()</code>)"),
         ("“Must not break under 150 kg”", "A property that must always hold"),
         ("Thousands of drops", "Hundreds of generated runs per test"),
         ("Smallest breaking load", "The shrunk counter-example"),
         ("Lab report with the seed", "A seed to replay the failing run")],
    how_side="state the rule, let the tool hunt",
    how="""  <p>The hard part is finding good properties. Common shapes: <b>round-trips</b> (decode(encode(x)) = x), <b>invariants</b> (sorted output is ordered), <b>conservation</b> (nothing created or lost), and <b>comparing to a simple model</b>.</p>""",
    how_figs=[pb_how],
    steps=[("Pick a property", "Round-trip, invariant, conservation, idempotence (f(f(x)) = f(x)) or “same as a simple reference version”."),
           ("Describe the inputs", "Generators for amounts, people, strings, lists; constrain to valid domains."),
           ("Run many cases", "100–1,000 per test in CI; more in a nightly job."),
           ("Read the shrunk example", "It's usually the clearest possible bug report."),
           ("Keep the failure", "Add the shrunk case as a regular example test, and record the seed.")],
    vocab=[("Property", "A rule that holds for all valid inputs."),
           ("Generator / arbitrary", "Produces random inputs of a given shape."),
           ("Shrinking", "Simplifying a failing input to a minimal one."),
           ("Seed", "Number that makes a random run repeatable."),
           ("Round-trip property", "Encode then decode gives back the original."),
           ("Oracle", "A trusted way to know the right answer.")],
    code=dict(file="split.prop.test.ts", note="fast-check + Vitest", src="""
import fc from "fast-check";

it("never loses or creates a cent", () => {
  fc.assert(
    fc.property(
      fc.integer({ min: 0, max: 10_000_00 }),     // total in cents
      fc.integer({ min: 1, max: 50 }),            // people
      (total, people) => {
        const parts = splitBill(total, people);

        expect(parts).toHaveLength(people);
        expect(parts.reduce((a, b) => a + b, 0)).toBe(total);
        expect(Math.max(...parts) - Math.min(...parts)).toBeLessThanOrEqual(1);
      },
    ),
  );
});
// on failure: "Counterexample: [10, 3]  Shrunk 6 time(s)  seed: 1593201"
"""),
    tools="tools: fast-check (JS/TS), Hypothesis (Python), jqwik (Java), FsCheck (.NET), proptest (Rust), QuickCheck (Haskell, Erlang). Stateful/model-based testing modes can test whole APIs.",
    gains=["<b>Finds edge cases</b> nobody imagined.",
           "<b>Shrunk failures</b> are minimal, clear bug reports.",
           "<b>One property covers thousands of examples</b>.",
           "<b>Forces you to state the real rule</b>."],
    losses=["<b>Good properties are hard</b> to think of at first.",
            "<b>Slower</b> than one example.",
            "<b>Randomness</b> needs seeds for reproducibility.",
            "<b>Easy to restate the implementation</b> as the property."],
    baseline="Each line compares <b>only hand-written examples</b> to examples <b>plus property-based tests</b> for the core rules.",
    ratings=[(4, 3, "Properties take more thought to read."),
             (5, 4, "Hundreds of cases still run in well under a second."),
             (3, 5, "Explores inputs nobody would write by hand."),
             (4, 4, "Seeded runs are repeatable."),
             (3, 4, "Shrinking points straight at the minimal failing input."),
             (3, 4, "Rules change less often than examples."),
             (2, 4, "Messy, real-world-shaped inputs."),
             (3, 3, "More thinking per test, far fewer tests."),
             (3, 4, "Generators are reused across the suite.")],
    pitfalls=[("Re-implementing the code in the test", "The property computes the answer the same way the code does.", "check rules and relations, not the algorithm."),
              ("Generators that are too narrow", "Only positive integers under 10, so nothing interesting happens.", "include zero, empties, huge and odd values."),
              ("Losing the failing case", "A random failure in CI can't be reproduced.", "log seeds; add shrunk cases as example tests."),
              ("Replacing all examples", "Nobody can read what the code should do.", "keep a few examples as documentation.")],
    use=["Pure functions with clear rules: money, parsing, sorting, encoding.",
         "Serializers and parsers (round-trip properties).",
         "Data structures and state machines."],
    skip=["UI layout and copy.",
          "Logic with no general rule, only special cases.",
          "Slow, side-effectful operations (unless you can fake them)."],
    related=["<b>Test data builders</b>", "<b>Mutation testing</b>", "<b>Controlled time &amp; randomness</b>", "<b>State machines</b> (Vol. 2)"],
    quiz=[("What is a property?", "A rule that must hold for every valid input, such as “the parts add up to the total”."),
          ("What does shrinking do?", "Reduces a failing input to the smallest, simplest example that still fails."),
          ("Name three common property shapes.", "Round-trip, invariant, conservation (also idempotence and comparing to a reference model)."),
          ("How do you reproduce a failing random run?", "Re-run with the reported seed, then add the shrunk case as an example test.")],
    remember="Don't sit on the chair <span class=\"hl\">three times</span>. State the <span class=\"hl\">rule</span> and drop a thousand <span class=\"hl\">weights</span>.",
    sources=["Koen Claessen &amp; John Hughes, “QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs” (2000).",
             "fast-check documentation (fast-check.dev).",
             "Hypothesis docs, “What you can generate and how”.",
             "Scott Wlaschin, “Choosing properties for property-based testing”."],
)

# ------------------------------------------------------------------ 10 Snapshot (Approval) Testing
sn_problem = Doodle(760, 250, "Doodle of a test for an invoice PDF generator with forty assertions, each checking one line of the output. The invoice layout changes slightly and the developer spends an hour updating assertions one at a time, while other parts of the output are not checked at all.",
                    "40 hand-written assertions for one big output, and still most of it unchecked.")
sn_problem.icon("receipt", 40, 30, 2.6, fill="paper")
sn_problem.note(260, 50, "expect(line[1]).toBe(…)", "pen", anchor="start")
sn_problem.note(260, 80, "expect(line[2]).toBe(…)", "pen", anchor="start")
sn_problem.note(260, 110, "… × 40", "pen", anchor="start")
sn_problem.note(260, 170, "small layout change → 1 hour of edits", "red", anchor="start")
sn_problem.note(260, 210, "lines 41–120: never checked", "red", anchor="start")

sn_analogy = Doodle(760, 250, "Doodle of a museum conservator who photographs a painting when it's approved. Every month they take a new photo and compare it to the approved one. Any difference is highlighted; either it's damage to fix, or an intended restoration, which becomes the new approved photo.",
                    "Photograph it once when approved; compare each new photo; approve intended changes.")
sn_analogy.icon("camera", 40, 60, 1.6, fill="y")
sn_analogy.icon("frame", 200, 50, 1.6, fill="green")
sn_analogy.note(250, 160, "approved photo", "green")
sn_analogy.icon("frame", 420, 50, 1.6)
sn_analogy.raw('<circle class="d d-red" cx="480" cy="80" r="16"/>')
sn_analogy.note(470, 160, "this month", "pen")
sn_analogy.note(640, 70, "damage?", "red")
sn_analogy.note(640, 96, "fix it", "red")
sn_analogy.note(640, 140, "restored?", "green")
sn_analogy.note(640, 166, "approve it", "green")

sn_how = Doodle(760, 290, "Snapshot testing loop. The test renders the invoice to text. The first run writes the approved snapshot file. Later runs compare the new output to the snapshot. If they match the test passes; if not, the test fails with a diff. A human reviews the diff: a bug gets fixed, an intended change is approved by updating the snapshot, and the snapshot change is reviewed in the pull request.",
                "Render, compare to the approved file, show a diff. A human decides: bug or approve.")
sn_how.box(20, 40, 150, 70, "render()", "blue")
sn_how.arrow(176, 75, 256, 75)
sn_how.box(262, 30, 200, 90, "compare", "y", sub="with invoice.snap")
sn_how.arrow(468, 60, 560, 40, color="green", label="same", lx=514, ly=34)
sn_how.box(566, 14, 120, 48, "pass ✓", "green", size=17)
sn_how.arrow(468, 92, 560, 130, color="red", label="diff ✗", lx=514, ly=126)
sn_how.box(566, 100, 180, 64, "human reviews", "pink", stroke="red", size=17)
sn_how.box(420, 210, 150, 54, "bug → fix", "paper", stroke="red", size=17)
sn_how.box(590, 210, 160, 54, "approve: -u", "green", size=17)
sn_how.arrow(620, 168, 510, 206, dash=True)
sn_how.arrow(660, 168, 670, 206, dash=True)
sn_how.note(170, 230, "snapshot diffs are reviewed in the PR", "pen")

SNAPSHOT = dict(
    slug="snapshot-testing",
    kicker="a.k.a. “the approved photograph”",
    tldr="For big outputs (rendered HTML, invoices, API responses, generated SQL), save an <b>approved copy</b> once, and have the test <b>compare new output to it</b>. Any difference fails with a <b>diff</b>; a human decides whether it's a <b>bug</b> or an <b>intended change</b> to approve. Keep snapshots <b>small and readable</b>, and review snapshot changes in the PR like code.",
    chips=[("Family", "test technique"), ("a.k.a.", "approval testing, golden files"), ("Tools", "Vitest/Jest snapshots, ApprovalTests, Playwright visual"), ("Pairs with", "characterization tests")],
    problem="""  <p class="lead">Some outputs are <span class="hl-pink">large and detailed</span>: an invoice, an email, a JSON report, a rendered component. Asserting every line by hand is tedious, and most of the output ends up unchecked.</p>
  <ul>
    <li>Forty assertions for one invoice, and lines 41–120 never checked.</li>
    <li>A small intended layout change means an hour of editing asserts.</li>
    <li>Nobody notices a stray field leaking into an API response.</li>
  </ul>""",
    problem_figs=[sn_problem],
    analogy_side="the conservator's photograph",
    analogy="""  <p>A museum conservator <b>photographs a painting</b> when it's approved. Every month they take a new photo and <b>compare</b>. Any difference is circled: either <b>damage to fix</b>, or an <b>intended restoration</b>, whose photo becomes the new approved one.</p>
  <ul>
    <li>The approved photo is the <b>snapshot</b>.</li>
    <li>Circled differences are the <b>diff</b>.</li>
    <li>Signing off a restoration is <b>updating the snapshot</b>, consciously.</li>
  </ul>""",
    analogy_figs=[sn_analogy],
    map=[("The approved photograph", "The stored snapshot / golden file"),
         ("This month's photo", "The output of the current code"),
         ("Circled differences", "The diff in the failing test"),
         ("Damage", "A regression: fix the code"),
         ("Intended restoration", "Approve: update the snapshot (<code>-u</code>)")],
    how_side="compare to the approved copy",
    how="""  <p>Snapshots turn “is this output right?” into “is this <b>change</b> right?”, which is much easier for a human to judge, as long as the diff is small and readable.</p>""",
    how_figs=[sn_how],
    steps=[("Render to a readable form", "Pretty-printed JSON, normalised HTML or plain text, not binary blobs."),
           ("Scrub the noise", "Replace dates, ids and random values with placeholders so snapshots are stable."),
           ("Keep snapshots small", "Snapshot the invoice body, not the whole page; inline snapshots for short output."),
           ("Review diffs like code", "Snapshot file changes appear in the PR; reviewers read them."),
           ("Update deliberately", "Run with <code>-u</code> only after reading the diff, never to “make it green”.")],
    vocab=[("Snapshot / golden file", "A stored, approved copy of output."),
           ("Approval", "Accepting a new output as the reference."),
           ("Scrubber", "Replaces unstable values (dates, ids) before comparing."),
           ("Inline snapshot", "A small snapshot stored inside the test file."),
           ("Visual regression", "Comparing screenshots pixel by pixel."),
           ("Snapshot fatigue", "Blindly updating snapshots without reading diffs.")],
    code=dict(file="invoice.test.ts", note="Vitest", src="""
it("renders an invoice for a Dutch customer", () => {
  const invoice = anInvoice().for(aCustomer().inNetherlands()).withLines(3).build();

  const text = renderInvoiceText(invoice)
    .replace(/\\d{4}-\\d{2}-\\d{2}/g, "<date>")          // scrub unstable values
    .replace(/INV-\\d+/g, "INV-<n>");

  expect(text).toMatchSnapshot();                     // __snapshots__/invoice.test.ts.snap
});

it("formats a small amount", () => {
  expect(formatMoney(1234.5, "EUR", "nl-NL")).toMatchInlineSnapshot(`"€ 1.234,50"`);
});
// intended change? read the diff, then:  vitest -u
"""),
    tools="tools: Vitest/Jest <code>toMatchSnapshot</code> and inline snapshots, ApprovalTests (many languages), Verify (.NET), syrupy (pytest), insta (Rust), Playwright <code>toHaveScreenshot</code> and Chromatic/Percy for visual snapshots.",
    gains=["<b>Whole output checked</b> with one line.",
           "<b>Easy updates</b> for intended changes.",
           "<b>Readable diffs</b> show exactly what changed.",
           "<b>Catches surprises</b> like leaked fields."],
    losses=["<b>Snapshot fatigue</b>: people approve without reading.",
            "<b>Doesn't say what's right</b>, only what changed.",
            "<b>Huge snapshots</b> are unreviewable.",
            "<b>Unstable values</b> need scrubbing."],
    baseline="Each line compares <b>dozens of hand-written assertions</b> on a large output to <b>one small, scrubbed snapshot</b>.",
    ratings=[(3, 4, "One line instead of forty asserts."),
             (4, 4, "Comparing text is fast."),
             (3, 3, "Checks everything, but only against past output."),
             (3, 3, "Stable with scrubbing; flaky without."),
             (3, 4, "The diff shows exactly what changed."),
             (2, 4, "Intended changes are one reviewed update."),
             (3, 4, "Real, complete output is checked."),
             (2, 5, "Very cheap to write."),
             (3, 3, "Great until snapshots grow huge.")],
    pitfalls=[("Blind updates", "Tests fail, someone runs <code>-u</code>, the bug is now approved.", "read every diff; review snapshot changes in PRs."),
              ("Giant snapshots", "A 2,000-line snapshot of a whole page.", "snapshot the part that matters; prefer inline for small output."),
              ("Unscrubbed timestamps and ids", "Snapshots change on every run.", "freeze time, seed ids, or scrub them."),
              ("Snapshots instead of rules", "The snapshot of a total is “wrong” and nobody knows it.", "assert key rules explicitly too.")],
    use=["Rendered emails, invoices, reports and HTML.",
         "API response shapes and generated code or SQL.",
         "Pinning legacy behaviour (see characterization tests)."],
    skip=["Small values where a direct assertion is clearer.",
          "Output that changes on every run and can't be scrubbed.",
          "Core business rules (assert them explicitly)."],
    related=["<b>Characterization tests</b>", "<b>Controlled time &amp; randomness</b>", "<b>Test data builders</b>", "<b>Design tokens</b> (Vol. 2)"],
    quiz=[("What does a failing snapshot test tell you?", "That the output changed compared to the approved copy, not whether the new output is right."),
          ("Why scrub dates and ids?", "So snapshots don't change on every run for reasons that don't matter."),
          ("What's snapshot fatigue?", "Updating snapshots without reading the diffs, which approves bugs."),
          ("When is an inline snapshot better?", "For short outputs, so the expected value is visible right in the test.")],
    remember="Photograph it when it's <span class=\"hl\">right</span>; read every <span class=\"hl\">difference</span> before you <span class=\"hl\">approve</span>.",
    sources=["Llewellyn Falco, ApprovalTests (approvaltests.com).",
             "Jest docs, “Snapshot Testing” and “Best Practices”.",
             "Vitest docs, “Snapshot”.",
             "Kent C. Dodds, “Effective Snapshot Testing”."],
)

# ------------------------------------------------------------------ 11 Mutation Testing
mu_problem = Doodle(760, 250, "Doodle of a coverage report showing ninety-four percent in green. But the tests call the discount function without checking its result, so when the code has greater-than instead of greater-than-or-equal, nothing fails. High coverage, weak tests.",
                    "94% coverage, but the tests run the code without really checking it.")
mu_problem.box(20, 40, 220, 120, "coverage 94%", "green", size=24)
mu_problem.note(130, 200, "looks great…", "green")
mu_problem.note(470, 60, "if (total > 100)  ← should be >=", "red")
mu_problem.note(470, 100, "test: discount(100)", "pen")
mu_problem.note(470, 130, "expect(…) — nothing!", "red")
mu_problem.note(470, 190, "line covered ✓  bug caught ✗", "red")

mu_analogy = Doodle(760, 250, "Doodle of a fire drill. The safety officer deliberately sets off fake alarms in different rooms to check that the smoke detectors and staff react. A detector that stays silent during the drill is broken, even though it's installed.",
                    "A fire drill: set off fake fires on purpose and see which detectors stay silent.")
for i in range(4):
    x = 60 + i * 170
    mu_analogy.box(x, 50, 140, 100, None, "paper", rx=3)
    mu_analogy.icon("bell", x + 50, 60, 0.7, color="green" if i != 2 else "red")
    mu_analogy.note(x + 70, 140, "fake fire", "pen", size=16)
mu_analogy.note(410, 200, "room 3: silent detector = a gap in your safety", "red")

mu_how = Doodle(760, 290, "Mutation testing. The tool makes many small copies of the code, each with one planted bug, called a mutant: greater-than becomes greater-or-equal, plus becomes minus, true becomes false, a line is deleted. The test suite runs against each mutant. Killed mutants made a test fail. Surviving mutants show where tests are missing or too weak. The mutation score is killed divided by total.",
                "Plant one small bug at a time. Tests should fail (kill it). Survivors show where tests are blind.")
muts = [("> → >=", "killed"), ("+ → −", "killed"), ("true → false", "survived"), ("delete line", "killed")]
for i, (t, r) in enumerate(muts):
    y = 20 + i * 62
    mu_how.box(20, y, 200, 48, t, "y", size=17)
    mu_how.arrow(226, y + 24, 330, y + 24, label="run tests", lx=278, ly=y + 14)
    mu_how.box(336, y, 160, 48, r, "green" if r == "killed" else "pink", stroke="" if r == "killed" else "red", size=17)
mu_how.note(630, 90, "score = 3 / 4 = 75%", "pen")
mu_how.note(630, 140, "survivor → missing", "red")
mu_how.note(630, 166, "assertion", "red")

MUTATION = dict(
    slug="mutation-testing",
    kicker="a.k.a. “the fire drill”",
    tldr="Coverage tells you which lines <b>ran</b>, not whether any test would <b>notice a bug</b> in them. Mutation testing <b>plants small bugs</b> (mutants) in your code, like <code>&gt;</code> → <code>&gt;=</code> or deleting a line, and runs the tests. If a test fails, the mutant is <b>killed</b>; if all pass, it <b>survived</b> and shows you exactly where tests are blind.",
    chips=[("Family", "test quality"), ("Origin", "Richard Lipton, 1971; DeMillo et al., 1978"), ("Tools", "Stryker, PIT, mutmut, cargo-mutants"), ("Measures", "mutation score")],
    problem="""  <p class="lead">Coverage is easy to game, even by accident. A test that calls a function and <span class="hl-pink">asserts nothing</span> still “covers” every line it runs.</p>
  <ul>
    <li>94% coverage, yet an off-by-one in the discount rule goes unnoticed.</li>
    <li>Tests check that no exception was thrown, not that the answer is right.</li>
    <li>Teams chase a coverage number instead of real confidence.</li>
  </ul>""",
    problem_figs=[mu_problem],
    analogy_side="the fire drill",
    analogy="""  <p>Having smoke detectors installed doesn't prove they work. A safety officer runs a <b>drill</b>: <b>fake fires</b> in each room, one at a time. Any detector that <b>stays silent</b> is a gap, even though it's on the ceiling.</p>
  <ul>
    <li>Installed detectors are <b>coverage</b>.</li>
    <li>Each fake fire is a <b>mutant</b>.</li>
    <li>A silent detector is a <b>surviving mutant</b>.</li>
  </ul>""",
    analogy_figs=[mu_analogy],
    map=[("A detector on the ceiling", "A covered line"),
         ("A fake fire in one room", "One mutant: a small planted bug"),
         ("The alarm goes off", "A test fails: mutant killed"),
         ("Silence", "All tests pass: mutant survived"),
         ("Drill report", "Mutation score and survivor list")],
    how_side="plant bugs, see who notices",
    how="""  <p>Each survivor is a concrete to-do: “if this <code>&gt;</code> were <code>&gt;=</code>, no test would notice”. Add the assertion or case that kills it.</p>""",
    how_figs=[mu_how],
    steps=[("Run it on core code", "Start with business logic, not the whole repo: it's slow."),
           ("Read the survivors", "Each one shows the exact change no test noticed."),
           ("Kill them", "Add the missing assertion or boundary case (here: <code>discount(100)</code> must apply)."),
           ("Ignore equivalent mutants", "Some mutants behave identically to the original; mark and skip them."),
           ("Run incrementally", "On changed files in PRs, the full run nightly; set a threshold, not 100%.")],
    vocab=[("Mutant", "A copy of the code with one small change."),
           ("Mutation operator", "A rule for making mutants (<code>&gt;</code> → <code>&gt;=</code>)."),
           ("Killed", "At least one test failed against the mutant."),
           ("Survived", "All tests passed against the mutant."),
           ("Equivalent mutant", "A change that doesn't alter behaviour."),
           ("Mutation score", "Killed mutants ÷ all (non-equivalent) mutants.")],
    code=dict(file="stryker.config.json + report", note="StrykerJS", src="""
{
  "testRunner": "vitest",
  "mutate": ["src/pricing/**/*.ts", "!src/**/*.test.ts"],
  "incremental": true,
  "thresholds": { "high": 85, "low": 70, "break": 65 }
}

// report excerpt
// [Survived] EqualityOperator  src/pricing/discount.ts:12
// -   if (total > 100) return total * 0.9;
// +   if (total >= 100) return total * 0.9;
//
// fix: add the boundary case
it("applies the discount from exactly 100", () => {
  expect(discount(100)).toBe(90);
});
"""),
    tools="tools: StrykerJS / Stryker.NET / Stryker4s, PIT (Java), mutmut and cosmic-ray (Python), cargo-mutants (Rust), Infection (PHP). Incremental and diff-based modes keep CI time manageable.",
    gains=["<b>Measures test strength</b>, not just reach.",
           "<b>Concrete to-dos</b>: each survivor is a missing check.",
           "<b>Finds weak assertions</b> and untested boundaries.",
           "<b>Raises the bar</b> without chasing coverage."],
    losses=["<b>Slow</b>: the suite runs once per mutant.",
            "<b>Noise</b> from equivalent mutants.",
            "<b>Needs a decent suite</b> to be useful.",
            "<b>Another report</b> to read and act on."],
    baseline="Each line compares a suite judged by <b>line coverage only</b> to the same suite <b>checked with mutation testing</b> on core modules.",
    ratings=[(4, 3, "A new report and new concepts."),
             (4, 3, "Extra runs; incremental mode helps."),
             (3, 5, "Proves tests would catch real-looking bugs."),
             (4, 4, "Neutral; it can expose order-dependent tests."),
             (3, 4, "Pushes towards precise assertions."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (4, 2, "Many extra test runs in CI."),
             (3, 3, "Scope it to core code as the repo grows.")],
    pitfalls=[("Running it on everything", "Six hours for a full run; nobody looks.", "start with core logic; use incremental mode in PRs."),
              ("Chasing 100%", "Hours spent on equivalent or trivial mutants.", "set a sensible threshold; ignore equivalents."),
              ("Killing mutants with silly tests", "Tests assert implementation details just to kill mutants.", "add meaningful behaviour checks."),
              ("Using it on a weak suite", "Hundreds of survivors, overwhelming.", "fix the obvious gaps first, then mutate.")],
    use=["Core business logic: pricing, permissions, money.",
         "Libraries other teams depend on.",
         "When coverage is high but bugs still slip through."],
    skip=["Glue code and generated code.",
          "Very slow suites, until they're faster.",
          "Early prototypes."],
    related=["<b>Property-based testing</b>", "<b>Arrange–Act–Assert</b>", "<b>Characterization tests</b>", "<b>Parallel &amp; selective runs</b>"],
    quiz=[("Why isn't high coverage enough?", "Coverage shows code ran, not that any assertion would fail if the code were wrong."),
          ("What's a surviving mutant?", "A planted bug that no test noticed: every test still passed."),
          ("What's an equivalent mutant?", "A change that doesn't alter behaviour, so no test could ever kill it."),
          ("How do you keep mutation testing affordable?", "Limit it to core code and run it incrementally on changed files.")],
    remember="Detectors on the ceiling aren't <span class=\"hl\">safety</span>. Run the <span class=\"hl\">drill</span> and fix the <span class=\"hl\">silent</span> ones.",
    sources=["DeMillo, Lipton &amp; Sayward, “Hints on Test Data Selection: Help for the Practicing Programmer” (1978).",
             "Stryker Mutator documentation (stryker-mutator.io).",
             "PIT mutation testing docs (pitest.org).",
             "Google, “State of Mutation Testing at Google” (ICSE 2018)."],
)

# ------------------------------------------------------------------ 12 Characterization Tests
ch_problem = Doodle(760, 250, "Doodle of a 1,500-line legacy function called calculate shipping, written eight years ago, with no tests and no documentation. A ticket asks to add a new country. Every change might break a rule nobody remembers, so nobody wants to touch it.",
                    "1,500 lines, no tests, no docs, and a ticket that says “just add Portugal”.")
ch_problem.box(20, 20, 260, 210, None, "paper", rx=4)
for i in range(8):
    ch_problem.line(f"M40 {44 + i * 22} h{120 + (i * 37) % 100}", thin=True)
ch_problem.note(150, 222, "calculateShipping() · 2018", "pen")
ch_problem.note(500, 60, "no tests", "red")
ch_problem.note(500, 100, "author left in 2020", "red")
ch_problem.note(500, 140, "ticket: “just add Portugal”", "pen")
ch_problem.note(500, 190, "touch it → what breaks?", "red")

ch_analogy = Doodle(760, 250, "Doodle of a renovator photographing and labelling every wire in an old house before changing anything. They don't judge whether the old wiring is right; they record exactly what is connected to what, so after the change they can check nothing else moved.",
                    "Before rewiring an old house: photograph and label what's there, right or wrong.")
ch_analogy.icon("store", 40, 60, 1.8)
ch_analogy.icon("camera", 240, 60, 1.4, fill="y")
for i, t in enumerate(["red → kitchen light", "blue → ??? (keep it!)", "green → boiler"]):
    ch_analogy.icon("tag", 400, 30 + i * 62, 0.8, fill="y")
    ch_analogy.note(470, 52 + i * 62, t, "pen", anchor="start")
ch_analogy.note(380, 230, "record what is, not what should be", "green")

ch_how = Doodle(760, 290, "Characterization testing workflow. Feed many realistic inputs, such as recorded production orders, into the legacy function and capture its outputs into a golden master file, including the odd ones. Tests now fail if any output changes. Refactor or add the new country in small steps; for each difference, decide whether it was intended. Then gradually replace golden masters with clear rule-based tests.",
                "Record today's outputs for many inputs, then change the code in small steps and watch for any difference.")
ch_how.box(20, 40, 170, 80, "1,000 real inputs", "y", size=17)
ch_how.arrow(196, 80, 266, 80)
ch_how.box(272, 40, 170, 80, "legacy code", "paper")
ch_how.arrow(448, 80, 518, 80, label="record", lx=483, ly=66)
ch_how.icon("ledger", 526, 40, 1.0, fill="green")
ch_how.note(600, 70, "golden master", "green", anchor="start")
ch_how.note(600, 96, "(odd results too)", "pen", anchor="start")
ch_how.box(20, 190, 260, 64, "refactor in small steps", "green", size=17)
ch_how.arrow(286, 222, 370, 222)
ch_how.box(376, 190, 360, 64, "any diff? intended or regression", "pink", stroke="red", size=16)

CHARACTERIZE = dict(
    slug="characterization-tests",
    kicker="a.k.a. “label the old wiring”",
    tldr="Before changing legacy code with no tests, write tests that <b>record what it does today</b>, right or wrong. Feed it many realistic inputs, <b>capture the outputs</b> (a golden master), and assert they stay the same. Then <b>refactor in small steps</b>; any difference is either an intended change or a regression, and now you'll <b>know</b>.",
    chips=[("Family", "legacy code"), ("Coined by", "Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004)"), ("a.k.a.", "golden master, pinning tests"), ("Pairs with", "snapshot testing, expand &amp; contract")],
    problem="""  <p class="lead">Legacy code is <span class="hl-pink">code without tests</span>. Nobody knows all its rules, some of its “bugs” are features customers rely on, and every change is a gamble.</p>
  <ul>
    <li>The author left; the spec, if it ever existed, is out of date.</li>
    <li>You can't write “correct” tests because nobody knows what correct is.</li>
    <li>So the code never gets cleaned up, and gets worse with every patch.</li>
  </ul>""",
    problem_figs=[ch_problem],
    analogy_side="labelling the old wiring",
    analogy="""  <p>A renovator in an old house doesn't rip out wires first. They <b>photograph and label</b> every wire: “red goes to the kitchen light”, “blue goes… somewhere, keep it!”. They <b>don't judge</b> whether it's right. After the work, they check that <b>everything still connects</b> the way it did.</p>
  <ul>
    <li>The labels are <b>characterization tests</b>.</li>
    <li>“Keep it, we don't know why” is a <b>pinned odd behaviour</b>.</li>
    <li>Once the house is understood, the labels become a proper <b>wiring diagram</b>: real tests.</li>
  </ul>""",
    analogy_figs=[ch_analogy],
    map=[("Photographing every wire", "Capturing outputs for many inputs"),
         ("“Blue → ??? keep it”", "Pinning odd behaviour you don't understand yet"),
         ("Don't judge the wiring yet", "Assert what is, not what should be"),
         ("Check after rewiring", "Run the tests after each small refactor"),
         ("The final wiring diagram", "Clear behaviour tests replacing the golden master")],
    how_side="pin first, change second",
    how="""  <p>The goal isn't to prove the code right. It's to make any <b>change in behaviour visible</b>, so refactoring becomes safe.</p>""",
    how_figs=[ch_how],
    steps=[("Find a seam", "A place to call the code and observe output (a function, an HTTP endpoint, a file it writes)."),
           ("Collect realistic inputs", "Recorded production requests, combinations of options, plus a generator for coverage."),
           ("Record the outputs", "Store them as a golden master (snapshot); include weird results."),
           ("Assert “unchanged”", "One test compares current outputs to the master."),
           ("Change in small steps", "Refactor, run, inspect any diff; approve intended changes only."),
           ("Graduate", "As rules become clear, write named behaviour tests and retire golden cases.")],
    vocab=[("Legacy code", "Code without tests (Feathers' definition)."),
           ("Characterization test", "A test that records current behaviour."),
           ("Golden master", "Saved outputs for a large set of inputs."),
           ("Seam", "A place to observe or alter behaviour without editing it."),
           ("Pinning", "Locking current behaviour so changes become visible."),
           ("Sprout / wrap", "Adding new code beside old code instead of inside it.")],
    code=dict(file="shipping.characterization.test.ts", note="Vitest", src="""
import inputs from "./fixtures/shipping-requests-2026-10.json";   // 1,000 recorded orders

it("calculates shipping exactly as it did before the refactor", () => {
  const results = inputs.map((req) => ({
    id: req.id,
    out: calculateShipping(req.weight, req.country, req.express, req.items),
  }));

  expect(results).toMatchSnapshot();          // golden master, odd results included
});

// pinned odd behaviour, written down when discovered
it("charges zero for exactly 30 kg to Belgium (legacy rule, ask Sales)", () => {
  expect(calculateShipping(30, "BE", false, 1)).toBe(0);
});
"""),
    tools="tools: ApprovalTests (“golden master” helpers, combination approvals), Vitest/Jest snapshots, recorded traffic (GoReplay, VCR-style cassettes), fast-check for generating input combinations, coverage reports to find unexercised branches.",
    gains=["<b>Safe refactoring</b> of code nobody understands.",
           "<b>Quick to write</b>: no need to know the rules first.",
           "<b>Documents surprises</b> as you find them.",
           "<b>A path</b> from legacy to well-tested code."],
    losses=["<b>Pins bugs too</b>: wrong behaviour is locked in.",
            "<b>Opaque failures</b>: a diff, not a named rule.",
            "<b>Brittle</b> if outputs include noise.",
            "<b>Temporary</b>: needs replacing with real tests later."],
    baseline="Each line compares <b>changing untested legacy code directly</b> to <b>pinning it with characterization tests first</b>.",
    ratings=[(3, 3, "Easy to add; harder to read than named rules."),
             (3, 4, "Runs in seconds instead of a manual QA cycle."),
             (1, 4, "Any behaviour change is caught."),
             (3, 3, "Stable with scrubbed outputs."),
             (2, 3, "Shows which inputs changed, not which rule."),
             (1, 4, "Refactors become possible at all."),
             (3, 4, "Uses recorded real inputs."),
             (3, 4, "Much cheaper than reverse-engineering a spec."),
             (2, 3, "Golden masters grow; graduate them to rules.")],
    pitfalls=[("“Fixing” bugs while pinning", "You change behaviour before tests exist.", "pin first, change in a separate, deliberate step."),
              ("Unrepresentative inputs", "Ten hand-made inputs miss most branches.", "use recorded real inputs and check branch coverage."),
              ("Leaving golden masters forever", "Five years later nobody knows what they mean.", "graduate to named behaviour tests as you learn the rules."),
              ("Noise in outputs", "Timestamps make every run differ.", "scrub or control time and ids.")],
    use=["Legacy code with no tests that must change.",
         "Large refactors and rewrites (compare old and new).",
         "Migrating to a new library or language version."],
    skip=["New code (write behaviour tests from the start).",
          "Code that will be deleted rather than changed.",
          "Outputs that can't be made deterministic."],
    related=["<b>Snapshot testing</b>", "<b>Mutation testing</b>", "<b>Expand &amp; contract</b> (Vol. 3)", "<b>Strangler fig</b> (planned, Vol. 1)"],
    quiz=[("What does a characterization test assert?", "That the code behaves the way it does today, whether or not that's correct."),
          ("Why pin behaviour you think is a bug?", "Customers may rely on it; you want to change it deliberately and visibly, not by accident."),
          ("Where do good inputs come from?", "Recorded production requests, plus generated combinations to reach more branches."),
          ("What happens to characterization tests later?", "They're gradually replaced by clear, named behaviour tests as the rules are understood.")],
    remember="<span class=\"hl\">Label</span> the old wiring before you <span class=\"hl\">touch</span> it. Judge it <span class=\"hl\">later</span>.",
    sources=["Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004), ch. 13.",
             "Llewellyn Falco &amp; Emily Bache, “Approval Testing / Gilded Rose kata”.",
             "Emily Bache, “Golden Master and approval testing”.",
             "Martin Fowler, <i>Refactoring</i> (2nd ed.), ch. 4."],
)

NOTES = [PROPERTY, SNAPSHOT, MUTATION, CHARACTERIZE]
