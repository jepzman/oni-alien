# Vol. 4 · extra notes (November 2026): Fuzzing, Visual Regression Tests, Fault Injection Tests.
# Numbered 16–18 so earlier note URLs and PDF names stay the same. Chaos engineering on running systems is in Vol. 6;
# fault injection here is about failures you cause inside the test suite.

# ------------------------------------------------------------------ 16 Fuzzing
fz_problem = Doodle(760, 250, "Doodle of a parser tested only with sensible examples. Twelve example tests with well-formed invoices pass. In production, an invoice file with a truncated line and an unexpected byte makes the parser loop forever, and the import worker hangs.",
                    "Twelve tidy examples pass. The thirteenth file from the real world hangs the worker.")
fz_problem.box(20, 40, 240, 70, "12 example tests", "green", sub="tidy, well-formed files", size=17, subsize=13)
fz_problem.box(20, 150, 240, 70, "real file #4,812", "pink", stroke="red", sub="cut-off line + odd byte", size=17, subsize=13)
fz_problem.arrow(264, 75, 376, 110, color="green")
fz_problem.arrow(264, 185, 376, 140, color="red")
fz_problem.box(380, 90, 150, 70, "parser", "y", size=19)
fz_problem.note(640, 110, "infinite loop", "red", size=17)
fz_problem.note(640, 138, "import worker hangs", "red", size=17)

fz_analogy = Doodle(760, 250, "Doodle of a toddler testing a toy. Instead of pressing buttons the way the manual says, the toddler bangs, twists, drops and chews it, thousands of times. Toy makers do this on purpose with machines, because it finds the weak spots no careful adult would think of.",
                    "Test the toy the way a toddler would: thousands of times, in every wrong way.")
fz_analogy.icon("box", 40, 60, 1.6, fill="y")
for i, w in enumerate(["bang", "twist", "drop", "chew", "stomp"]):
    fz_analogy.box(200 + i * 110, 70 + (i % 2) * 40, 96, 44, w, "paper", size=15)
fz_analogy.note(470, 214, "the crack nobody planned for shows up by try 3,000", "pen", size=16)

fz_how = Doodle(760, 280, "A coverage-guided fuzzer loop. It starts from a few seed inputs, mutates them (flipping bytes, cutting, repeating), runs the target, and watches which code paths each input reaches. Inputs that reach new code are kept in the corpus and mutated further. Any crash, hang or failed assertion is saved as a minimal reproducing input.",
                "Mutate, run, keep what reaches new code, repeat millions of times.")
fz_how.row([("seeds", "a few real files", "paper"), ("mutate", "flip, cut, repeat", "y"), ("run target", "with sanitizers", "blue"), ("new path?", "keep in corpus", "green")], x=20, y=40, h=80, gap=40, size=17, subsize=13, arrows=True)
fz_how.arrow(650, 124, 280, 124, curve=(465, 200), dash=True)
fz_how.note(465, 194, "loop · millions of runs", "pen", size=15)
fz_how.box(500, 206, 240, 62, "crash or hang", "pink", stroke="red", sub="input saved, shrunk", size=16, subsize=13)
fz_how.arrow(560, 124, 600, 206, color="red")

FUZZING = dict(
    slug="fuzzing",
    kicker="a.k.a. “throw garbage at it, very fast”",
    tldr="Code that reads <b>untrusted input</b> (parsers, file importers, decoders, protocol handlers) breaks on inputs nobody thought to write a test for. A <b>fuzzer</b> generates millions of mutated inputs, runs your code on each, and watches for <b>crashes, hangs, sanitizer errors and failed assertions</b>. Coverage-guided fuzzers keep inputs that reach new code, so they dig deeper over time. Run it continuously; turn every finding into a regular test.",
    chips=[("Family", "test techniques"), ("Best for", "parsers, decoders, file formats, protocols"), ("Kinds", "coverage-guided · grammar-based · API fuzzing"), ("Pairs with", "property-based testing, validate at the boundary")],
    problem="""  <p class="lead">An invoice importer has twelve example tests with tidy files, all green. In production, file #4,812 has a cut-off line and a stray byte, and <span class="hl-pink">the parser loops for ever</span>, hanging the import worker for every customer behind it.</p>
  <ul>
    <li>Example tests check the inputs <b>you imagined</b>; real-world and hostile inputs are stranger.</li>
    <li>Parser bugs are often <b>security bugs</b>: crashes, hangs and memory errors on attacker-chosen input.</li>
    <li>Writing enough strange examples by hand is impossible.</li>
  </ul>""",
    problem_figs=[fz_problem],
    analogy_side="the toddler test",
    analogy="""  <p>Toy makers don't only press the buttons the way the manual says. They let machines <b>bang, twist, drop and chew</b> the toy thousands of times, because that's how a toddler will use it, and the crack nobody planned for shows up by try 3,000.</p>""",
    analogy_figs=[fz_analogy],
    map=[("The toy", "The code that reads input: a parser, a decoder"),
         ("Banging, twisting, dropping", "Mutating inputs: flipping bytes, cutting, repeating"),
         ("Thousands of tries by machine", "Millions of runs per hour, automatically"),
         ("Noticing a crack", "A crash, hang, sanitizer report or failed assertion"),
         ("Remembering what broke it", "The saved crashing input, added as a regular test")],
    how_side="mutate, run, keep what's new",
    how="""  <p>A coverage-guided fuzzer starts from a few real inputs (the <b>seed corpus</b>), changes them in small random ways, and runs your code on each, instrumented so it can see which branches ran. Inputs that reach <b>new code</b> are kept and mutated further. Sanitizers turn silent memory errors into crashes the fuzzer can see. Findings are shrunk to a small input that reproduces them.</p>""",
    how_figs=[fz_how],
    steps=[("Pick a target", "A function that takes bytes or a string from outside: a parser, a decoder, an upload handler."),
           ("Write a fuzz harness", "A few lines that pass the fuzzer's input to the target and assert anything that must always hold."),
           ("Give it seeds", "A handful of real files, including odd ones; a dictionary of keywords helps text formats."),
           ("Run it continuously", "Minutes per pull request, hours nightly (or a service like OSS-Fuzz for open source)."),
           ("Keep the findings", "Each crash becomes a regular test case and a fix; keep the corpus between runs.")],
    vocab=[("Fuzzing", "Running code on huge numbers of generated inputs to find failures."),
           ("Harness", "The small function that hands fuzzer input to your code."),
           ("Corpus", "The set of interesting inputs the fuzzer keeps and mutates."),
           ("Coverage-guided", "The fuzzer favours inputs that reach new code."),
           ("Sanitizer", "Instrumentation that turns memory and undefined-behaviour bugs into crashes."),
           ("Minimisation", "Shrinking a crashing input to the smallest that still fails.")],
    code=dict(file="invoice_fuzz_test.go", note="Go 1.18+ native fuzzing", src="""
func FuzzParseInvoice(f *testing.F) {
    // seeds: real files, including odd ones we've seen
    f.Add([]byte("INV;2026-03-01;812;4.10\\n"))
    f.Add([]byte("INV;;;\\n"))

    f.Fuzz(func(t *testing.T, data []byte) {
        inv, err := ParseInvoice(bytes.NewReader(data))  // must never panic or hang
        if err != nil {
            return                                       // rejecting bad input is fine
        }
        // properties that must hold for anything we accept
        if inv.TotalCents < 0 {
            t.Fatalf("negative total from %q", data)
        }
        again, _ := ParseInvoice(strings.NewReader(inv.String()))
        if !reflect.DeepEqual(inv, again) {
            t.Fatalf("round trip changed the invoice")
        }
    })
}
// go test -fuzz=FuzzParseInvoice -fuzztime=10m ; crashes land in testdata/fuzz/
"""),
    tools="tools: Go native fuzzing, libFuzzer and AFL++ (C, C++, Rust via cargo-fuzz), Jazzer (Java), Atheris (Python), Jazzer.js (JavaScript), OSS-Fuzz and ClusterFuzzLite, RESTler and Schemathesis (API fuzzing).",
    gains=["<b>Finds bugs no one would write a test for</b>.",
           "<b>Finds security bugs</b> in input handling early.",
           "<b>Cheap per bug</b>: machines do the searching.",
           "<b>Reproducible</b>: every finding comes with its input."],
    losses=["<b>Needs a harness</b> per target, and CPU time.",
            "<b>Mostly finds crashes</b>: logic bugs need assertions or properties.",
            "<b>Slow to start</b> on complex formats without good seeds or grammars.",
            "<b>Triage</b>: findings need someone to look at them."],
    baseline="Each line compares <b>example tests only</b> to <b>example tests plus continuous fuzzing of input-handling code</b>.",
    ratings=[(4, 3, "A harness and a corpus to keep."),
             (4, 3, "Short runs in PRs, long ones nightly."),
             (3, 5, "Finds the inputs nobody imagined."),
             (4, 4, "Findings are saved inputs: deterministic."),
             (3, 4, "A minimised input points at the bug."),
             (4, 4, "Harnesses rarely change."),
             (2, 4, "Real-world strangeness, generated."),
             (4, 3, "CPU hours, but little human time."),
             (3, 4, "Add a harness per new parser.")],
    pitfalls=[("Fuzzing once", "A ten-minute run before release, never again.", "run it continuously; coverage keeps growing for days."),
              ("No assertions", "The fuzzer only finds crashes, while wrong results pass.", "assert properties: round trips, invariants, no negative totals."),
              ("Throwing away the corpus", "Each run starts from scratch and finds the same shallow bugs.", "store the corpus and reuse it between runs."),
              ("Fixing without a test", "A crash is fixed, and comes back a year later.", "add the crashing input as a regular test before the fix.")],
    use=["Parsers, decoders, file importers and protocol handlers.",
         "Anything that reads untrusted input from users or the network.",
         "Code in memory-unsafe languages (C, C++, unsafe Rust)."],
    skip=["Code that doesn't take external input (most business logic: use property tests).",
          "UI flows (use other tests).",
          "No one will look at the findings."],
    related=["<b>Property-based testing</b> · the same idea for logic", "<b>Validate at the boundary</b> (Vol. 5)", "<b>Characterization tests</b>", "<b>Mutation testing</b>"],
    quiz=[("What kind of code benefits most from fuzzing?", "Code that reads untrusted or complex input: parsers, decoders, file formats and protocol handlers."),
          ("What does “coverage-guided” mean?", "The fuzzer keeps inputs that reach new code paths and mutates those further."),
          ("Why add assertions to a fuzz harness?", "Without them the fuzzer only sees crashes and hangs; assertions turn wrong results into failures too."),
          ("What do you do with a crashing input?", "Minimise it, add it as a regular test, then fix the bug.")],
    quiz_sit=[("Your team wrote a new parser for a partner's file format. It has 30 example tests and ships next week. Security asks how you know a malformed file can't crash the import service. What do you add before release?",
               "A fuzz harness for the parser with real partner files as seeds and a few properties (round trip, no negative amounts), run for several hours before release and then in CI and nightly. Add every finding as a regular test, and set a time and size limit on parsing as a second line of defence.")],
    try_it="Pick one function in your codebase that parses text or bytes. Write a fuzz harness for it (Go's <code>testing.F</code>, Jazzer.js, Atheris or cargo-fuzz), seed it with three real inputs, and run it for 15 minutes. Add any crashing input as a regular test, fix it, and run again.",
    remember="Your tests try what you <span class=\"hl\">imagined</span>. A fuzzer tries what you <span class=\"hl\">didn't</span>.",
    sources=["Barton Miller, Lars Fredriksen and Bryan So, “An Empirical Study of the Reliability of UNIX Utilities” (1990).",
             "Go documentation, “Go Fuzzing” tutorial.",
             "Google, OSS-Fuzz documentation.",
             "Andreas Zeller et al., <i>The Fuzzing Book</i> (fuzzingbook.org)."],
)

# ------------------------------------------------------------------ 17 Visual regression tests
vr_problem = Doodle(760, 250, "Doodle of a style change that breaks another page. A developer changes the padding of a shared button. All unit and end-to-end tests pass, because they check text and clicks. On the checkout page the pay button now overlaps the total and is cut off on small phones. Nobody notices until customers complain.",
                    "Every test passes: they check text and clicks, not what the page looks like.")
vr_problem.box(20, 40, 220, 70, "button padding", "y", sub="+8 px, shared component", size=17, subsize=13)
vr_problem.box(20, 150, 220, 70, "all tests green", "green", sub="text and clicks are fine", size=17, subsize=13)
vr_problem.box(420, 40, 300, 180, None, "paper")
vr_problem.text(450, 80, "Total  €49.95", "t-head", anchor="start", size=17)
vr_problem.box(440, 74, 200, 48, "Pay now", "pink", stroke="red", size=17)
vr_problem.note(570, 160, "button covers the total", "red", size=16)
vr_problem.note(570, 188, "cut off on small phones", "red", size=16)
vr_problem.arrow(244, 75, 416, 95, dash=True)

vr_analogy = Doodle(760, 250, "Doodle of spot-the-difference. Two pictures side by side, one approved and one new. Differences are circled in red. A person looks at each circle and decides: a mistake to fix, or an intended change to accept as the new approved picture.",
                    "Spot the difference, with the differences circled for you.")
vr_analogy.box(40, 40, 260, 150, "approved", "paper", size=18)
vr_analogy.box(460, 40, 260, 150, "new", "paper", size=18)
vr_analogy.circle(640, 150, 22, fill="pink", stroke="red")
vr_analogy.circle(520, 80, 18, fill="pink", stroke="red")
vr_analogy.note(380, 220, "a person decides: bug, or new approved picture?", "pen", size=16)

vr_how = Doodle(760, 270, "The visual test loop. A test opens a page or component in a fixed browser, at fixed sizes, with fixed data and fonts, and takes a screenshot. It compares the screenshot pixel by pixel with the approved baseline. Differences above a small threshold fail the test and show a diff image. A reviewer either fixes the bug or approves the new screenshot as the baseline.",
                "Same browser, same data, same size: screenshot, compare, review.")
vr_how.row([("render", "fixed data + fonts", "y"), ("screenshot", "3 widths", "blue"), ("compare", "with baseline", "paper"), ("diff?", "fail + show it", "pink")], x=20, y=40, h=80, gap=40, size=17, subsize=13, arrows=True)
vr_how.box(200, 170, 180, 60, "fix the bug", "green", size=16)
vr_how.box(420, 170, 240, 60, "approve new baseline", "green", size=16)
vr_how.arrow(650, 124, 300, 166, dash=True)
vr_how.arrow(650, 124, 540, 166, dash=True)

VISUAL_REGRESSION = dict(
    slug="visual-regression",
    kicker="a.k.a. “did the page change how it looks?”",
    tldr="Unit and end-to-end tests check text, state and clicks; they don't notice a button covering the total or a broken layout on phones. <b>Visual regression tests</b> render pages or components in a fixed browser, at fixed sizes, with fixed data, take <b>screenshots</b>, and compare them with approved <b>baselines</b>. A difference fails the build and shows a diff; a person decides whether it's a bug or the new look.",
    chips=[("Family", "test techniques"), ("Unit of test", "a component state or a page at a viewport size"), ("Cousin", "snapshot testing (text instead of pixels)"), ("Pairs with", "design tokens, page objects, Storybook")],
    problem="""  <p class="lead">A developer adds 8 px of padding to a shared button. Every unit and end-to-end test passes. On the checkout page, <span class="hl-pink">the Pay button now covers the order total</span> and is cut off on small phones. Customers notice first.</p>
  <ul>
    <li>CSS changes travel: one shared style can break many pages.</li>
    <li>Functional tests check <b>what</b> is on the page, not <b>where</b> or <b>how it looks</b>.</li>
    <li>Manual checks of every page, at every screen size, after every change don't happen.</li>
  </ul>""",
    problem_figs=[vr_problem],
    analogy_side="spot the difference",
    analogy="""  <p>Two pictures side by side, the <b>approved</b> one and the <b>new</b> one, with every difference <b>circled in red</b>. You don't search the whole picture; you look at the circles and decide: a mistake to fix, or an intended change that becomes the new approved picture.</p>""",
    analogy_figs=[vr_analogy],
    map=[("The approved picture", "The baseline screenshot, stored with the tests"),
         ("The new picture", "The screenshot from this build"),
         ("Circles around differences", "The diff image, pixels above a threshold"),
         ("“Mistake or intended?”", "Review: fix the bug, or approve the new baseline"),
         ("Same light, same angle", "Same browser, fonts, data and viewport every run")],
    how_side="render the same way, compare, review",
    how="""  <p>The hard part is making screenshots <b>repeatable</b>: the same browser build, fonts loaded, animations off, fixed data and dates, no ads or live content. Then any pixel difference means something changed. Test at the component level (Storybook stories) for breadth, and a few full pages for layout.</p>""",
    how_figs=[vr_how],
    steps=[("Choose what to capture", "Each component state (from stories) and a few key pages, at 2–3 widths (phone, tablet, desktop)."),
           ("Make rendering repeatable", "Pinned browser in a container, fonts loaded, animations and carets off, fixed data and clock, masks for live content."),
           ("Store baselines", "In the repo (small sets) or a service; one baseline per browser and size."),
           ("Compare with a small threshold", "Ignore tiny anti-aliasing noise; fail above it and attach the diff image."),
           ("Review changes like code", "An intended change updates the baseline in the same pull request; a reviewer looks at the diffs.")],
    vocab=[("Baseline", "The approved screenshot a new one is compared with."),
           ("Diff image", "An image highlighting the pixels that changed."),
           ("Threshold", "How much difference is tolerated as noise."),
           ("Mask", "An area left out of the comparison (a clock, an ad, an avatar)."),
           ("Viewport", "The screen size the page is rendered at."),
           ("Flaky screenshot", "One that differs between runs with no code change.")],
    code=dict(file="checkout.visual.spec.ts", note="Playwright", src="""
import { test, expect } from "@playwright/test";

for (const width of [375, 768, 1280]) {
  test(`checkout summary looks right at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.clock.setFixedTime(new Date("2026-03-01T10:00:00Z"));   // fixed dates
    await page.route("**/api/cart", (r) => r.fulfill({ path: "fixtures/cart.json" }));
    await page.goto("/checkout");
    await page.evaluate(() => document.fonts.ready);

    await expect(page.getByTestId("order-summary")).toHaveScreenshot(`summary-${width}.png`, {
      animations: "disabled",
      mask: [page.getByTestId("live-chat")],      // live content left out
      maxDiffPixelRatio: 0.002,                     // ignore anti-aliasing noise
    });
  });
}
// npx playwright test --update-snapshots   ← only for an intended change, reviewed in the PR
"""),
    tools="tools: Playwright <code>toHaveScreenshot</code>, Storybook test runner, Chromatic, Percy, Applitools, BackstopJS, Loki, Lost Pixel; run in a pinned Docker image so fonts and rendering match.",
    gains=["<b>Catches layout and style bugs</b> that other tests miss.",
           "<b>Covers many screen sizes</b> automatically.",
           "<b>Safer shared CSS</b>: changes show every affected page.",
           "<b>Review by looking</b>: diffs are quick to judge."],
    losses=["<b>Flaky without care</b>: fonts, animations and live data.",
            "<b>Baselines to maintain</b> for every intended change.",
            "<b>Storage and CI time</b> for screenshots.",
            "<b>Tells you what changed, not why</b>."],
    baseline="Each line compares <b>functional tests only</b> to <b>functional tests plus visual regression tests on components and key pages</b>.",
    ratings=[(4, 3, "Screenshots and a review step."),
             (4, 3, "Rendering and comparing take time."),
             (3, 5, "Layout bugs fail the build."),
             (4, 3, "Rendering must be pinned to avoid noise."),
             (3, 4, "The diff points at the changed spot."),
             (3, 3, "Intended changes need new baselines."),
             (3, 4, "Real browser, real CSS."),
             (4, 3, "CI minutes and storage, or a paid service."),
             (3, 3, "Grows with components and sizes.")],
    pitfalls=[("Screenshots that differ every run", "Fonts load late, a carousel moves, today's date changes.", "wait for fonts, disable animations, fix the clock and data, mask live areas."),
              ("Different machines, different pixels", "Baselines made on a Mac fail on Linux CI.", "make and compare screenshots in the same pinned container."),
              ("Approving without looking", "A big change updates 200 baselines and nobody checks them.", "keep shots small (components), and review diffs like code."),
              ("Only full pages", "One full-page shot changes for every tiny thing.", "mostly component states; a few pages for layout.")],
    use=["Design systems and shared components.",
         "Responsive layouts that must work at several sizes.",
         "Refactors of CSS, themes or design tokens."],
    skip=["Pages full of live, changing content you can't fix.",
          "Very early prototypes whose look changes daily.",
          "No one will review the diffs."],
    related=["<b>Snapshot testing</b>", "<b>Page objects</b>", "<b>Design tokens</b> (Vol. 2)", "<b>Controlled time &amp; randomness</b>"],
    quiz=[("What do visual regression tests catch that end-to-end tests usually don't?", "How the page looks: overlaps, broken layouts, wrong colours or spacing, at different screen sizes."),
          ("Name three things that make screenshots flaky.", "Fonts loading late, animations, and live data such as dates, ads or avatars."),
          ("Why compare screenshots in a container?", "Different operating systems render fonts slightly differently; the same container makes runs comparable."),
          ("What happens when a change is intended?", "The new screenshot is approved as the baseline in the same pull request, after review.")],
    quiz_sit=[("Visual tests fail on about one run in five with tiny differences in text edges, and the team has started approving every diff without looking. What do you change?",
               "Remove the noise: render in one pinned container, wait for fonts, disable animations, and set a small difference threshold. Once diffs only appear for real changes, require a reviewer to look at them, and keep screenshots small so diffs stay readable.")],
    try_it="Add one visual test with Playwright's <code>toHaveScreenshot</code> for a component or page at two widths, with fonts loaded and animations off. Run it twice to check it's stable, then change one CSS value (padding, colour) and look at the diff image it produces.",
    remember="Tests check <span class=\"hl\">what</span> is there. Screenshots check <span class=\"hl\">how it looks</span>.",
    sources=["Playwright documentation, “Visual comparisons”.",
             "Storybook documentation, “Visual tests”.",
             "Kent C. Dodds, “Write tests. Not too many. Mostly integration.” (2017), on test balance.",
             "BackstopJS documentation."],
)

# ------------------------------------------------------------------ 18 Fault injection tests
fi_problem = Doodle(760, 250, "Doodle of code that has only been tested against healthy dependencies. In tests the payment provider always answers in 50 milliseconds. In production it once took 30 seconds; the checkout had no timeout, all its threads waited, and the whole shop stopped. The retry and fallback code that was supposed to handle this had never run.",
                    "Tested only against a perfect world, the error handling had never run once.")
fi_problem.box(20, 40, 260, 70, "in tests", "green", sub="provider answers in 50 ms, always", size=17, subsize=13)
fi_problem.box(20, 150, 260, 70, "in production", "pink", stroke="red", sub="provider takes 30 s", size=17, subsize=13)
fi_problem.note(520, 90, "timeout: missing", "red", size=17)
fi_problem.note(520, 120, "retry code: never ran", "red", size=17)
fi_problem.note(520, 150, "whole shop stops", "red", size=17)

fi_analogy = Doodle(760, 250, "Doodle of a fire drill. Instead of waiting for a real fire, the school sets off the alarm on purpose, on a calm day, with someone watching the clock. Blocked exits and missing people are found while nothing is burning.",
                    "A fire drill: set off the alarm on purpose, on a calm day.")
fi_analogy.icon("bell", 60, 60, 1.6, fill="y")
fi_analogy.box(240, 50, 220, 120, "drill", "blue", sub="planned · timed · watched", size=19, subsize=14)
fi_analogy.note(620, 90, "blocked exit: found", "green", size=16)
fi_analogy.note(620, 120, "missing class: found", "green", size=16)
fi_analogy.note(620, 150, "nothing on fire", "green", size=16)

fi_how = Doodle(760, 280, "Fault injection in an integration test. The service under test calls the payment provider through a fault proxy such as Toxiproxy. The test tells the proxy to add 5 seconds of latency, or to cut the connection, or to return errors, then checks the service's behaviour: it times out after 2 seconds, shows a friendly message, does not charge twice, and recovers when the fault is removed.",
                "Put a switchable fault between the service and its dependency, then assert the behaviour.")
fi_how.box(20, 90, 170, 80, "service", "y", sub="under test", size=18, subsize=13)
fi_how.arrow(194, 130, 286, 130)
fi_how.box(290, 70, 180, 120, "fault proxy", "pink", stroke="red", sub="latency · reset · errors", size=17, subsize=13)
fi_how.arrow(474, 130, 566, 130)
fi_how.box(570, 90, 170, 80, "payment fake", "blue", sub="or a container", size=17, subsize=13)
fi_how.note(380, 230, "assert: times out in 2 s · friendly message · no double charge · recovers", "green", size=15)
fi_how.note(380, 258, "the test turns each fault on and off", "pen", size=15)

FAULT_INJECTION = dict(
    slug="fault-injection",
    kicker="a.k.a. “make it fail on purpose, in the test”",
    tldr="Timeouts, retries, fallbacks and error messages are code too, but in most test suites they <b>never run</b>, because the fakes and containers always answer quickly and correctly. <b>Fault injection tests</b> put a switchable fault between your code and a dependency (latency, dropped connections, errors, garbage responses) and assert that the code behaves well: it times out, retries safely, shows a useful message and recovers.",
    chips=[("Family", "reliability"), ("Faults", "latency · connection reset · 5xx · timeouts · bad payloads"), ("Tools", "Toxiproxy, WireMock faults, test doubles that fail"), ("Vol. 6 cousin", "chaos engineering on running systems")],
    problem="""  <p class="lead">In every test the payment provider answers in 50 ms. In production it once took 30 seconds; checkout had no timeout, every thread waited, and <span class="hl-pink">the whole shop stopped</span>. The retry and fallback code written for exactly this had never run once.</p>
  <ul>
    <li>Fakes and test containers are <b>always healthy</b>, so error paths go untested.</li>
    <li>Timeout and retry settings are configured and <b>never checked</b> until an incident.</li>
    <li>Error handling that's never run is often wrong: double charges, swallowed errors, blank screens.</li>
  </ul>""",
    problem_figs=[fi_problem],
    analogy_side="the fire drill",
    analogy="""  <p>A school doesn't wait for a fire to learn whether the exits work. It sets off the <b>alarm on purpose</b>, on a calm day, with someone timing it. Blocked exits and missing classes are found <b>while nothing is burning</b>.</p>""",
    analogy_figs=[fi_analogy],
    map=[("Setting off the alarm on purpose", "Turning on a fault in the test"),
         ("A calm day", "A test environment, not production"),
         ("Timing the evacuation", "Asserting timeouts and recovery times"),
         ("Blocked exit found", "A missing timeout or a retry that double-charges"),
         ("The next drill", "The test runs on every build")],
    how_side="a switchable fault between you and the dependency",
    how="""  <p>Route calls to a dependency through something you control in the test: a fault proxy (Toxiproxy) in front of a real container, or a fake that can be told to fail. Each test switches one fault on, exercises the feature, asserts the behaviour, and switches it off. Test the <b>recovery</b> too: once the fault is gone, the feature must work again.</p>""",
    how_figs=[fi_how],
    steps=[("List the dependencies", "Database, cache, payment provider, email, other services: everything the feature calls."),
           ("List the faults that matter", "Slow (above your timeout), down (connection refused), flaky (some 503s), wrong (malformed or partial answers)."),
           ("Add a switch", "A fault proxy in front of the container, or a test double with failure modes."),
           ("Assert the behaviour", "Timeout in the expected time, safe retries (no double charge), a clear message, metrics and logs written."),
           ("Assert recovery", "Remove the fault; the next request succeeds, and the circuit breaker closes.")],
    vocab=[("Fault injection", "Causing failures on purpose to test how code handles them."),
           ("Fault proxy", "A proxy that can add latency, drop or corrupt traffic on command."),
           ("Toxic", "Toxiproxy's name for a fault (latency, timeout, reset)."),
           ("Error path", "The code that runs only when something fails."),
           ("Graceful degradation", "Doing less, but still working, when a dependency fails."),
           ("Recovery test", "Checking the system works again once the fault is removed.")],
    code=dict(file="checkout.faults.test.ts", note="Vitest + Testcontainers + Toxiproxy", src="""
// the service talks to the payment fake through Toxiproxy (set up once per run)
test("checkout times out quickly when payments hang, and doesn't charge twice", async () => {
  await paymentsProxy.addToxic({ type: "latency", attributes: { latency: 5_000 } });

  const started = Date.now();
  const res = await api.post("/checkout", { cartId: "c-42", idempotencyKey: "k-1" });

  expect(res.status).toBe(503);
  expect(res.body.message).toMatch(/try again/i);
  expect(Date.now() - started).toBeLessThan(2_500);        // our 2 s timeout, not 5 s

  await paymentsProxy.removeAllToxics();                    // recovery
  const retry = await api.post("/checkout", { cartId: "c-42", idempotencyKey: "k-1" });
  expect(retry.status).toBe(200);
  expect(await paymentsFake.chargesFor("c-42")).toHaveLength(1);
});
"""),
    tools="tools: Toxiproxy (with Testcontainers modules), WireMock fault responses and delays, MockServer, Polly's simmy (.NET), Chaos Mesh / Litmus for cluster-level tests (see Vol. 6), tc netem for network faults.",
    gains=["<b>Error paths actually run</b> in CI.",
           "<b>Timeouts and retries are checked</b>, not assumed.",
           "<b>Fewer incident surprises</b>: the first slow dependency isn't in production.",
           "<b>Safe refactors</b> of resilience code."],
    losses=["<b>Slower tests</b>: waiting for timeouts takes real time.",
            "<b>More setup</b>: proxies, fakes with failure modes.",
            "<b>Many combinations</b>: you can't test every fault everywhere.",
            "<b>Not production</b>: real failures can be stranger."],
    baseline="Each line compares <b>tests against always-healthy dependencies</b> to <b>the same tests plus injected faults on key dependencies</b>.",
    ratings=[(4, 3, "A proxy or failing fakes to set up."),
             (4, 3, "Timeouts make some tests take seconds."),
             (3, 5, "The code paths incidents use are tested."),
             (3, 3, "Timing assertions need generous margins."),
             (3, 4, "Each test has one named fault."),
             (3, 3, "Neutral."),
             (2, 4, "Real network faults against real containers."),
             (4, 3, "More CI time and setup."),
             (3, 3, "Pick the dependencies that matter, not all.")],
    pitfalls=[("Faults only in fakes", "A fake that throws an exception tests nothing about real timeouts and sockets.", "inject faults on the network path (a proxy) for the critical dependencies."),
              ("Tight timing assertions", "“Within 2,000 ms” fails on a slow CI machine.", "assert with margin (under 2.5 s), or use fake timers where possible."),
              ("Forgetting recovery", "The service handles the outage but never recovers when the dependency comes back.", "always remove the fault and assert the next request succeeds."),
              ("Every fault, everywhere", "Hundreds of slow tests nobody can maintain.", "cover the critical paths (payment, login, checkout) with the faults that matter.")],
    use=["Code that calls payment, identity, storage or other critical services.",
         "Timeouts, retries, circuit breakers and fallbacks you rely on.",
         "Before and after changing resilience settings."],
    skip=["Pure logic with no external calls.",
          "Dependencies whose failure is already handled by a platform you trust and tested there.",
          "Running systems in staging or production: that's chaos engineering (Vol. 6)."],
    related=["<b>Circuit breaker</b> (Vol. 1)", "<b>Retry with backoff</b> (Vol. 1)", "<b>Throwaway containers</b>", "<b>Chaos engineering</b> (Vol. 6)"],
    quiz=[("Why do error paths often go untested?", "Fakes and containers in tests always answer quickly and correctly, so timeout, retry and fallback code never runs."),
          ("Name four kinds of fault worth injecting.", "Latency above the timeout, connection refused or reset, intermittent 5xx errors, and malformed or partial responses."),
          ("Why inject faults with a proxy rather than a fake that throws?", "A proxy exercises the real network path: socket timeouts, connection pools and retries behave as in production."),
          ("Why test recovery?", "Code can handle an outage but stay broken after it ends, for example a breaker that never closes.")],
    quiz_sit=[("A service sets a 3-second timeout on its calls to the inventory service, with 2 retries. In an incident, requests took 12 seconds before failing. Your tests never showed this. What test do you add, and what did it probably reveal?",
               "An integration test with a fault proxy adding 10 s of latency to inventory, asserting the request fails within about 3–4 s. It would show the timeout applies per attempt, so 3 attempts × 3 s plus backoff ≈ 12 s; fix it with an overall deadline or fewer retries.")],
    try_it="Pick one feature that calls another service in an integration test. Put Toxiproxy (or WireMock with a fixed delay) between them and add 10 seconds of latency. Check how long the feature takes to fail and what the user sees. Then add a connection reset, and finally remove the fault and check that the next request succeeds.",
    remember="Your error handling is <span class=\"hl\">code</span>. If no test makes it run, it <span class=\"hl\">doesn't work</span>.",
    sources=["Shopify, Toxiproxy (github.com/Shopify/toxiproxy).",
             "Testcontainers documentation, “Toxiproxy module”.",
             "Michael Nygard, <i>Release It!</i> (2nd ed., 2018), chapters on stability patterns.",
             "WireMock documentation, “Simulating faults”."],
)

NOTES = [FUZZING, VISUAL_REGRESSION, FAULT_INJECTION]
