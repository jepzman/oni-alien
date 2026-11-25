# Series 2 · Book 5 · The IT Operations Notebook · Vol. 3 · Safety nets.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 3".

# ------------------------------------------------------------------ 06 How Do We Undo It?
rb_problem = Doodle(760, 260, "Doodle of 14 to 16 April 2027. A deploy renamed the field 'store' to 'store_id' in the order.placed event. Billing, one of nine consumers, quietly stopped creating invoice lines. Two days later, on 16 April, someone noticed. Rolling back the deploy would stop new damage, but two days of events had already gone out in the new shape; undoing the code couldn't undo them.",
                    "Rolling back the code stops new damage. It can't undo two days of events already sent.")
rb_problem.box(14, 30, 230, 100, "14 Apr deploy", "blue", sub="store → store_id", size=19, subsize=14)
rb_problem.arrow(250, 80, 290, 80)
rb_problem.box(296, 30, 220, 100, "billing silent", "pink", sub="2 days, 9 consumers", size=19, subsize=14)
rb_problem.arrow(522, 80, 562, 80)
rb_problem.box(568, 30, 178, 100, "roll back?", "y", sub="only the code", size=19, subsize=14)
rb_problem.note(380, 180, "events, data and messages don't roll back with the deploy", "red", size=17)

rb_analogy = Doodle(760, 220, "Doodle of a tailor shortening trousers. Before cutting, he pins and tacks: easy to undo. Once he cuts, there's no going back, so before he cuts he measures twice and keeps the offcut, and he knows how he'd let the hem down with a false hem if he had to. Some steps undo; some only go forward, and he plans both.",
                    "Pins and tacking undo easily. Cutting doesn't, so the tailor plans the way forward before he cuts.")
rb_analogy.row([("pins + tacking", "undo in a minute", "green"), ("the cut", "no way back", "pink"), ("a false hem", "the way forward", "y")], y=40, h=96, gap=20, size=18, subsize=14)
rb_analogy.note(380, 190, "know which steps undo, and plan forward for the ones that don't", "pen", size=17)

rb_how = Doodle(760, 380, "Larder's rule for normal changes from 26 April 2027: every change states its way back, how long it takes and where it was tested. Three kinds. Undo: flag off, or redeploy the previous version; tested in staging. Way forward: when the change touches data, events or a vendor, a written plan to repair instead of undo, such as expand and contract for schema changes, a backup taken just before, or replaying events. No way back: rare, and only with a restore that has been practised, a planned time and a watcher. For the 14 April rename: forward fix, replay of two days of events to billing, 312 invoice lines restored by 20 April.",
                "Every change states its way back: undo, a way forward, or a practised restore.")
rb_how.row([("undo", "flag off · redeploy previous", "green"), ("way forward", "expand → contract · backup · replay", "y"), ("no way back", "practised restore · watcher", "pink")], y=14, h=110, gap=16, size=20, subsize=13)
rb_how.box(14, 150, 732, 110, None, "paper")
rb_how.text(380, 182, "14 April rename, fixed forward:", size=16)
rb_how.text(380, 212, "publish both fields → replay 2 days of events to billing → 312 lines restored (20 Apr)", size=14)
rb_how.text(380, 240, "→ events change by expand and contract only (ADR 0020)", size=14)
rb_how.note(380, 300, "“we can always roll back” is checked, not assumed", "red", size=17)
rb_how.note(380, 340, "the way back is tested where the change was tested", "pen", size=16)

ROLLBACK = dict(
    slug="rollback-plans",
    kicker="a.k.a. “back-out plans and roll-forward”",
    tldr="Every change needs a <b>way back</b>, written down before it's made: how, how long, and tested where. For code, that's usually a flag or a redeploy. But <b>data, events, messages and vendor changes don't roll back with the code</b>, so those need a <b>way forward</b>: expand and contract, a backup taken just before, a replay. The few changes with no way back need a <b>practised restore</b>, a planned time and someone watching.",
    chips=[("Family", "safety nets"), ("Lives in", "“way back” in every normal change's pull request"), ("Pairs with", "release vs deploy, risk scoring, zero-downtime change")],
    itil=dict(groups=["service", "technical"], chain=["design", "deliver"], practices=["change enablement", "deployment management"],
              sre="“rollbacks should be fast and safe; roll forward when they can't be”", principles=["Think and work holistically"],
              older="ITIL v3: remediation (back-out) plans"),
    problem_side="Larder, 14–16 April 2027",
    problem="""  <p class="lead">On <b>Wednesday 14 April</b>, two days after Utrecht opens, a deploy renames the field <code>store</code> to <code>store_id</code> in the <b>order.placed</b> event. It looks harmless: the team's own consumers are updated. <b>Billing</b>, one of <b>nine</b> consumers, quietly stops creating invoice lines. On <b>Friday the 16th</b> someone notices. Rolling back the deploy stops new damage, but <span class="hl-pink">two days of events have already gone out in the new shape, and undoing the code can't undo them</span>.</p>
  <ul>
    <li>“We can always roll back” was assumed, not checked.</li>
    <li>Data and events outlive the deploy that made them.</li>
    <li>Nobody had written down what the way back was.</li>
  </ul>""",
    problem_figs=[rb_problem],
    analogy_side="the tailor's pins and the cut",
    analogy="""  <p>A tailor shortening trousers <b>pins and tacks</b> first, and that undoes in a minute. <b>The cut</b> doesn't undo. So before cutting he measures twice, keeps the offcut, and knows how he'd let the hem down with <b>a false hem</b> if he had to. Some steps undo and some only go forward, and he plans for both kinds before he starts.</p>""",
    analogy_figs=[rb_analogy],
    map=[("Pins and tacking", "Flags and redeploys: true undo"),
         ("The cut", "Data written, events published, a vendor setting changed"),
         ("Measuring twice", "Testing the change and its way back"),
         ("The false hem", "A way forward: expand and contract, a replay, a backup"),
         ("Knowing which is which", "“Way back” written in every normal change")],
    how_side="undo, way forward, or a practised restore, written before the change",
    how="""  <p>The fix for 14 April is forward, not back. Ben publishes <b>both fields</b> for a while (expand), the two days of events are <b>replayed</b> to billing, and <b>312 invoice lines</b> are restored by <b>20 April</b>. Ana's ADR 0020 (19 April) then makes events change only compatibly, through expand and contract.</p>
  <p>From <b>26 April</b> every normal change states its way back, how long it takes, and where it was tested:</p>
  <ul>
    <li><b>Undo</b>: flag off, or redeploy the previous version. Fine for most code.</li>
    <li><b>Way forward</b>: when the change touches <b>data, events, messages or a vendor</b>. Expand and contract for schemas, a backup taken just before, a replay, a script to repair.</li>
    <li><b>No way back</b>: rare. It needs a <b>practised restore</b>, a planned time and a watcher. The Postgres upgrade in May is the first (this volume).</li>
  </ul>
  <p>The reviewer's job includes one question: <b>has the way back been tried, or only imagined?</b></p>""",
    how_figs=[rb_how],
    steps=[("Write the way back before the change", "How, how long, tested where."),
           ("Ask what doesn't roll back", "Data, events, messages, vendors, emails sent."),
           ("Plan forward for those", "Expand and contract, backup, replay, repair script."),
           ("Test the way back too", "Where the change was tested."),
           ("For no-way-back changes, practise the restore", "Planned time, watcher."),
           ("Review what happened when it was used", "Did it work as written?")],
    vocab=[("Rollback", "Returning to the previous version of code or configuration."),
           ("Roll forward", "Fixing a problem with a new change instead of undoing the old one."),
           ("Back-out plan", "The written steps to undo a change."),
           ("Expand and contract", "Add the new shape alongside the old, move everyone, then remove the old."),
           ("Replay", "Re-sending events or messages to rebuild what a consumer missed."),
           ("One-way door", "A change that can't easily be undone (Ana's term).")],
    code=dict(file="ops/changes/way-back.md", note="from 26 April 2027 · one line in every normal change", plain=True, src="""
Way back    [ ] undo          flag off / redeploy v(n-1)          ≈ 2 min    tested: staging
            [ ] way forward   expand → move → contract / backup   ≈ ____     tested: ______
                              taken at __:__ / replay from ____
            [ ] no way back   practised restore on ____ took ____  watcher: ______

Doesn't roll back with the code:
  data written · events published (9 consumers of order.placed!) · emails/SMS sent
  vendor settings · payments made · device updates already installed

14 Apr 2027  order.placed store → store_id   way back assumed, not checked
             → both fields published · 2 days replayed to billing · 312 lines (20 Apr)
"""),
    tools="tools: a line in the pull request template, expand and contract for schemas and events, a replay tool for events, and backups you've restored at least once.",
    ladder=[("“we can always roll back”", ["Assumed.", "Data and events forgotten."]),
            ("the way back written and tested", ["Undo, way forward or practised restore.", "Checked by the reviewer."]),
            ("undo built in", ["Expand and contract by default.", "Replays and backups one command."]),
            ("automatic undo", ["Canary signals trigger rollback by themselves.", "One-way doors rare and known."])],
    ladder_now=1,
    baseline="Each line compares <b>assuming every change can be rolled back</b> to <b>a written, tested way back (or forward) for every normal change</b>.",
    ratings=[(2, 4, "Damage like 14 April is repaired, not just stopped."),
             (3, 3, "Neutral on its own."),
             (2, 4, "The way back is ready before it's needed."),
             (2, 4, "Changes that can't undo get extra care."),
             (2, 3, "What doesn't roll back is named."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "On-call knows how to undo someone else's change."),
             (3, 3, "One line per change.")],
    pitfalls=[("Assuming rollback works", "It was never tried.", "test the way back where the change was tested."),
              ("Forgetting data and events", "The code rolls back; the data doesn't.", "ask what doesn't roll back."),
              ("Renaming in one step", "Every consumer breaks at once.", "expand and contract."),
              ("Backups nobody restored", "The way back fails when it's needed.", "practise the restore (vol. 5).")],
    use=["Every normal change.", "Changes to schemas, events or vendor settings.", "Upgrades of databases or platforms.", "After a rollback that didn't fix things."],
    skip=["Standard changes whose recipe already includes the undo."],
    related=["<b>Release or Deploy?</b> (this volume)", "<b>How Risky Is This Change?</b> (this volume)", "<b>Event-Driven Integration</b> (Ana, vol. 4)", "<b>The Database Runs Out of Support</b> (this volume)"],
    quiz=[("Why couldn't the 14 April deploy simply be rolled back?", "Two days of events had already gone out in the new shape; undoing the code couldn't undo them."),
          ("What are the three kinds of way back?", "Undo (flag, redeploy), way forward (expand and contract, backup, replay), and a practised restore for no-way-back changes."),
          ("What usually doesn't roll back with code?", "Data, published events, messages and emails sent, vendor settings, payments, installed device updates."),
          ("What is expand and contract?", "Add the new shape alongside the old, move every consumer, then remove the old."),
          ("What does the reviewer ask about the way back?", "Has it been tried, or only imagined?")],
    quiz_sit=[("A change adds a required column to the orders table. The author writes “way back: redeploy previous version”. What do you ask?", "Will the old version still work with the new column, and what about rows written in between? Probably add it as optional first (expand), then make it required later (contract), with a backup before.")],
    try_it="Take your next three changes and write their way back: how, how long, tested where. For each, list anything that won't roll back with the code. Which one needs a way forward instead?",
    remember="The code rolls back; <span class=\"hl\">data and events don't</span>. Write the way back before the change, and <span class=\"hl\">try it</span>, don't imagine it.",
    sources=["AXELOS, <i>ITIL 4: Change enablement</i> practice guide (2020): remediation.",
             "Martin Fowler, “ParallelChange” (martinfowler.com, 2014): expand and contract.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 16, canarying releases."],
)

# ------------------------------------------------------------------ 07 Is It Really Ready?
vl_problem = Doodle(760, 260, "Doodle of the ADR 0017 failover fix, February 2027. The target: failover in under 2 minutes. On 15 February it is tested in staging and passes in 50 seconds. But staging's database has no replica; the 'failover' there is a restart. On Tuesday 23 February at 10:00 the first production test takes 6 minutes 10 seconds: the Dispatch containers cache the database address for 5 minutes. Staging couldn't have found it, because staging isn't built the same way.",
                    "50 seconds in staging, 6 minutes 10 in production. Staging had no replica.")
vl_problem.box(14, 30, 350, 100, "staging · 15 Feb", "green", sub="50 s ✓ (no replica)", size=20, subsize=15)
vl_problem.box(396, 30, 350, 100, "production · 23 Feb", "pink", sub="6 min 10 s ✗", size=20, subsize=15)
vl_problem.note(380, 180, "Dispatch caches the database address for 5 minutes", "red", size=17)
vl_problem.note(380, 216, "staging can't find what it isn't built to have", "pen", size=17)

vl_analogy = Doodle(760, 220, "Doodle of a fire drill. Practising the evacuation in an empty car park says nothing about the real building: the stairwell door that sticks, the lift people try to use. The useful drill is in the real building, at a quiet time, with people told in advance.",
                    "An evacuation practised in a car park finds nothing. Practise in the real building, at a quiet time.")
vl_analogy.box(14, 40, 340, 100, "drill in a car park", "pink", sub="finds nothing", size=19, subsize=15)
vl_analogy.box(406, 40, 340, 100, "drill in the building", "green", sub="quiet time · announced", size=19, subsize=15)
vl_analogy.note(380, 190, "test where the real problems live", "pen", size=18)

vl_how = Doodle(760, 380, "Larder's testing rules from March 2027. Staging is built from the same infrastructure code as production at smaller size: same replica, same pooler, same network rules, masked data. Some things can only be tested in production: failover, real vendor behaviour, real load. Those are tested in production, at a quiet hour (Tuesday 10:00), announced, with a watcher and a way back. After the Dispatch fix (address refreshed every 10 seconds), the monthly production failover test from 9 March: 1 minute 40, 1 minute 35, 1 minute 38. Changes record where they were tested; the risk score counts 'staging only' as 2.",
                "Staging built like production; the rest tested in production, carefully. Monthly failover: about 1 minute 40.")
vl_how.box(14, 14, 360, 120, "staging = production, smaller", "blue", sub="same code · replica · pooler · rules · masked data", size=17, subsize=12)
vl_how.box(386, 14, 360, 120, "in production, carefully", "y", sub="failover · vendors · real load · Tue 10:00 · watcher", size=17, subsize=12)
vl_how.row([("9 Mar", "1:40", "green"), ("13 Apr", "1:35", "green"), ("11 May", "1:38", "green"), ("8 Jun", "1:36", "green")], x=14, y=170, h=80, gap=14, size=19, subsize=17)
vl_how.note(380, 290, "monthly production failover test, second Tuesday, 10:00", "pen", size=17)
vl_how.note(380, 330, "fix: Dispatch refreshes the database address every 10 s", "green", size=16)

VALIDATION = dict(
    slug="validation",
    kicker="a.k.a. “service validation and testing”",
    tldr="A test is only as good as the place it runs in. Build <b>staging from the same infrastructure code as production</b>, smaller but with the same parts (replicas, poolers, network rules, masked real data). Accept that some things can <b>only be tested in production</b>: failover, real vendors, real load. Test those there, <b>carefully</b>: at a quiet hour, announced, with a watcher and a way back. Record where each change was tested.",
    chips=[("Family", "safety nets"), ("Lives in", "staging built from the same code; ops/tests/production-tests.md"), ("Pairs with", "risk scoring, rollback plans, game days (vol. 5)")],
    itil=dict(groups=["service"], chain=["design", "build"], practices=["service validation and testing"],
              sre="“testing in production”, carefully; disaster role-playing", principles=["Progress iteratively with feedback", "Think and work holistically"],
              older="ITIL v3: service validation and testing"),
    problem_side="Larder, February 2027",
    problem="""  <p class="lead">ADR 0017 promises <b>failover in under 2 minutes</b>. On <b>15 February</b> the fix is tested in staging and passes in <b>50 seconds</b>. But staging's database <b>has no replica</b>, so the “failover” there is just a restart. On Tuesday <b>23 February at 10:00</b>, the first production test takes <b>6 minutes 10 seconds</b>: the Dispatch containers cache the database's address for five minutes. <span class="hl-pink">Staging couldn't find it, because staging isn't built the same way.</span></p>
  <ul>
    <li>A passed test in the wrong place is false comfort.</li>
    <li>Staging was built by hand and drifted from production.</li>
    <li>Nobody had planned to test the real failover, in the real place.</li>
  </ul>""",
    problem_figs=[vl_problem],
    analogy_side="the fire drill in the real building",
    analogy="""  <p>Practising an evacuation in an <b>empty car park</b> tells you nothing about the real building: the stairwell door that sticks, the lift people try to use. The useful drill happens <b>in the real building</b>, at a quiet time, with people told in advance and someone timing it.</p>""",
    analogy_figs=[vl_analogy],
    map=[("A drill in a car park", "A failover test in staging without a replica"),
         ("The sticking stairwell door", "Dispatch caching the database address"),
         ("The real building", "Production"),
         ("A quiet time, people told", "Tuesday 10:00, announced, with a watcher"),
         ("Timing it", "1 minute 40 seconds, written down monthly")],
    how_side="a staging that's honest, and careful tests in production",
    how="""  <p>Two changes, from <b>March</b>:</p>
  <ul>
    <li><b>Staging is built from the same infrastructure code</b> as production, just smaller: the same replica, the same connection pooler, the same network rules, and masked copies of real data. Bram rebuilds it on <b>2 March</b>. The differences that remain are listed on one page.</li>
    <li><b>Some things are tested in production</b>, because nothing else is real enough: failover, real vendor behaviour, real load. Each test has a <b>quiet hour</b> (Tuesday 10:00), an <b>announcement</b> in the incident channel and to Sam, a <b>watcher</b>, and a <b>way back</b>.</li>
  </ul>
  <p>After Dispatch is changed to refresh the database address every 10 seconds, the <b>monthly production failover test</b> (second Tuesday, 10:00) gives <b>1:40 on 9 March, 1:35 in April, 1:38 in May</b>. Every change now records where it was tested, and the risk score counts “staging only” as 2, not 1.</p>""",
    how_figs=[vl_how],
    steps=[("List how staging differs from production", "Every difference is a blind spot."),
           ("Build staging from the same code", "Smaller, not different."),
           ("Use masked real data", "Edge cases live in real data."),
           ("Name what only production can test", "Failover, vendors, real load."),
           ("Test those carefully in production", "Quiet hour, announced, watcher, way back."),
           ("Record where each change was tested", "And let the risk score use it.")],
    vocab=[("Validation", "Checking that a change does what the service needs, not just what was built."),
           ("Staging", "A pre-production environment for testing."),
           ("Environment parity", "How closely staging matches production."),
           ("Testing in production", "Deliberate, controlled tests on the live system."),
           ("Masked data", "Real data with personal details replaced."),
           ("Drift", "Differences that creep in between environments over time.")],
    code=dict(file="ops/tests/production-tests.md", note="from March 2027", plain=True, src="""
# Tests only production can do

test                  when                    watcher   way back            results
DB failover           2nd Tue 10:00 monthly   Eli/Bram  promote back        9 Mar 1:40 · 13 Apr 1:35
                                                                            11 May 1:38 · 8 Jun 1:36
store line failover   1st Tue 15:00 monthly   store lead plug back in       (vol. 1)
PSP backup route      quarterly, Tue 10:00    Cho       switch back         Apr ✓
load test             before peaks, 05:00     Ben       stop the test       (vol. 4)

announce   #incident + Sam, 30 min before · "test, not an incident"
staging differences (2 Mar rebuild): smaller sizes · masked data · no real PSP
"""),
    tools="tools: infrastructure as code for both environments, a data-masking script, and a calendar of production tests.",
    ladder=[("staging built by hand", ["Tests pass in the wrong place.", "Production surprises."]),
            ("staging from the same code; careful production tests", ["Differences listed.", "Monthly failover test."]),
            ("production tests automated", ["Failover and load tests scheduled and scripted.", "Results tracked."]),
            ("continuous verification", ["Canaries and synthetic checks test every change in production.", "Chaos experiments (vol. 5)."])],
    ladder_now=1,
    baseline="Each line compares <b>tests in a staging that differs from production</b> to <b>an honest staging plus careful production tests</b>.",
    ratings=[(2, 3, "A failover that really takes under 2 minutes."),
             (2, 4, "Problems found by tests, not incidents."),
             (2, 4, "6 min 10 → about 1 min 40."),
             (2, 4, "Where a change was tested is known."),
             (2, 3, "Staging's differences on one page."),
             (3, 3, "Neutral."),
             (3, 3, "A second environment costs money; smaller sizes help."),
             (2, 3, "Fewer surprises at night."),
             (3, 3, "A monthly hour of tests.")],
    pitfalls=[("Trusting a pass in a different place", "Staging lacks the part that fails.", "list the differences; test those in production."),
              ("Staging by hand", "It drifts within weeks.", "build it from the same code."),
              ("Production tests without care", "A test becomes an incident.", "quiet hour, announced, watcher, way back."),
              ("Fake data only", "Edge cases never appear.", "masked real data.")],
    use=["A test passed and production still failed.", "Staging was built by hand.", "You promise a recovery time (failover, restore).", "Vendors behave differently from their sandboxes."],
    skip=["Simple, flagged code changes: a canary tests them in production anyway."],
    related=["<b>How Risky Is This Change?</b> (this volume)", "<b>Preview Environments</b> (cloud, vol. 6)", "<b>Infrastructure as Code</b> (cloud, vol. 6)", "<b>When Is It a Major Incident?</b> (vol. 2)"],
    quiz=[("Why did the failover pass in staging and fail in production?", "Staging had no replica, so its “failover” was a restart; it couldn't show Dispatch caching the address."),
          ("How should staging be built?", "From the same infrastructure code as production, smaller, with masked real data."),
          ("What can only be tested in production?", "Things like failover, real vendor behaviour and real load."),
          ("What makes a production test careful?", "A quiet hour, an announcement, a watcher and a way back."),
          ("What were the monthly failover times after the fix?", "About 1 minute 40, under the 2-minute target.")],
    quiz_sit=[("A vendor's sandbox accepts every test payment, but production payments sometimes fail. How do you test the change?", "In production, carefully: a small real payment at a quiet hour, announced, with a watcher, or a canary to a small share of customers. The sandbox can't show real behaviour.")],
    try_it="Write down every way your staging differs from production. For the top three, decide: make staging match, or test that part in production with a quiet hour, an announcement, a watcher and a way back.",
    remember="A test is only as honest as <span class=\"hl\">the place it runs</span>. Build staging like production, and test the rest <span class=\"hl\">in production, carefully</span>.",
    sources=["AXELOS, <i>ITIL 4: Service validation and testing</i> practice guide (2020).",
             "Cindy Sridharan, “Testing in Production, the safe way” (2018).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 17, testing for reliability."],
)

# ------------------------------------------------------------------ 08 The Urgent Fix at 17:00 on a Friday
em_problem = Doodle(760, 260, "Doodle of Friday 12 March 2027, 16:52. Thursday's deploy let the promo code WELCOME10, ten euros off a first order, be used on every order. About 40 euros of discount a minute, eight minutes before the Friday window. Ben has a code fix ready in ten minutes. The pipeline refuses deploys from 17:00. Two people argue whether to break the rule or wait three hours.",
                    "A promo bug costing €40 a minute, a fix ready, and the Friday window starting in eight minutes.")
em_problem.box(14, 30, 230, 100, "WELCOME10", "pink", sub="every order, not the first", size=19, subsize=14)
em_problem.box(264, 30, 230, 100, "≈ €40 a minute", "pink", size=20)
em_problem.box(514, 30, 232, 100, "window at 17:00", "y", sub="pipeline says no", size=19, subsize=14)
em_problem.note(380, 180, "break the rule, or wait three hours?", "red", size=19)

em_analogy = Doodle(760, 220, "Doodle of an ambulance crossing a red light: lights and siren on, slowing at the junction, a second paramedic watching the road, and the driver logs it afterwards. It's allowed, and it isn't careless: fewer rules, never none.",
                    "An ambulance may cross a red light: siren on, slow at the junction, logged afterwards.")
em_analogy.icon("traffic", 70, 30, 1.3)
em_analogy.row([("siren on", "declared", "pink"), ("slow at junction", "two people", "y"), ("logged after", "written up", "green")], x=160, y=40, h=96, w=180, gap=18, size=17, subsize=14)
em_analogy.note(450, 190, "fewer checks, never zero", "pen", size=18)

em_how = Doodle(760, 380, "Larder's emergency change path, used on 12 March. First: the smallest undo that stops the harm, ideally a flag or a config, not new code. At 17:01 Dee, as incident lead, turned off the promo-code flag: losses stopped; new customers couldn't use codes for the evening. The code fix wasn't urgent any more, so it waited until Monday, as a normal change. If code had been needed: the incident lead approves, two people (one writes, one reviews in the same call), deploy marked 'emergency' with the lead's name, a watcher for 30 minutes, and a write-up within a working day. February to June: 3 emergency changes, all written up.",
                "First the smallest undo (a flag). The code fix then waits for Monday as a normal change.")
em_how.box(14, 14, 360, 110, "1 · smallest undo", "green", sub="flag off at 17:01 · losses stop", size=19, subsize=14)
em_how.box(386, 14, 360, 110, "2 · fix waits", "y", sub="Monday, as a normal change", size=19, subsize=14)
em_how.box(14, 150, 732, 120, None, "paper")
em_how.head(380, 178, "if code must ship now:", size=17)
em_how.text(380, 210, "lead approves · two people (write + review) · “emergency” + lead's name", size=15)
em_how.text(380, 240, "watcher 30 min · written up within a working day", size=15)
em_how.note(380, 310, "Feb–Jun: 3 emergency changes, 3 written up", "pen", size=17)
em_how.note(380, 346, "≈ €320 lost, not ≈ €7,000", "green", size=17)

EMERGENCY = dict(
    slug="emergency-changes",
    kicker="a.k.a. “emergency change”",
    tldr="An <b>emergency change</b> is one that can't wait, usually to stop harm during an incident. It gets <b>fewer checks, never none</b>. First look for the <b>smallest undo</b> that stops the harm (a flag, a config, a rollback), because that often makes the real fix non-urgent. If new code must ship now: the incident lead approves, <b>two people</b> do it, it's marked in the feed, someone watches it, and it's <b>written up within a day</b>.",
    chips=[("Family", "safety nets"), ("Lives in", "ops/changes/emergency.md, the pipeline's “emergency” label"), ("Pairs with", "change calendar, incident roles, rollback plans")],
    itil=dict(groups=["service"], chain=["deliver"], practices=["change enablement", "incident management"],
              sre="(mitigate first, fix later)", principles=["Focus on value", "Keep it simple and practical"],
              older="ITIL v3: emergency change, the emergency CAB (ECAB)"),
    pager=dict(when="Fri 12 Mar 2027 · Dee on call", lines=[
        ("16:52", "<b>ALERT</b> discount_per_order 4× normal · promo WELCOME10"),
        ("16:54", "Dee declares SEV2 · Ben: Thursday's deploy, fix ready in 10 min"),
        ("16:58", "pipeline: window opens 17:00 · deploy would need “emergency”"),
        ("17:00", "Dee: smallest undo first? promo flag off → codes off for everyone"),
        ("17:01", "flag off (standard change) · discounts back to zero"),
        ("17:10", "SEV2 closed · code fix → normal change, Mon 15 Mar"),
        ("Sat", "write-up: ≈ €320 lost · ≈ 8 min of exposure")]),
    problem_side="Larder, Friday 12 March 2027",
    problem="""  <p class="lead">At <b>16:52 on a Friday</b> an alert fires: discounts per order are four times normal. Thursday's deploy has let the promo code <b>WELCOME10</b>, €10 off a <i>first</i> order, work on <b>every</b> order: about <b>€40 a minute</b>. Ben has a fix ready in ten minutes, but at 17:00 the Friday window starts and the pipeline will refuse it. <span class="hl-pink">Two people start arguing whether to break the rule or wait three hours.</span></p>
  <ul>
    <li>A window rule with no emergency path forces a choice between harm and bypassing.</li>
    <li>Under pressure, “ship the fix” feels like the only option.</li>
    <li>Rushed code in the peak window is how one incident becomes two.</li>
  </ul>""",
    problem_figs=[em_problem],
    analogy_side="the ambulance at a red light",
    analogy="""  <p>An <b>ambulance may cross a red light</b>. Its lights and siren go on, it slows at the junction, a second paramedic watches the road, and the crossing is logged afterwards. That's allowed, and it isn't careless. Emergency means <b>fewer rules, never none</b>.</p>""",
    analogy_figs=[em_analogy],
    map=[("Lights and siren", "Declared as an emergency change, with the lead's name"),
         ("Slowing at the junction", "Two people: one writes, one reviews"),
         ("Second paramedic watching", "A watcher for 30 minutes"),
         ("Logged afterwards", "Written up within a working day"),
         ("Taking the side road if it's clear", "The smallest undo: a flag instead of new code")],
    how_side="smallest undo first; if code must ship, a light path with two people",
    how="""  <p>Dee, the incident lead, stops the argument with one question: <b>what's the smallest undo that stops the harm?</b> The answer is the <b>promo-code flag</b>. Turning it off is a standard change and allowed in the window. At <b>17:01</b> it's off, and the losses stop. New customers can't use codes for the evening, which costs far less. With the harm stopped, the code fix <b>isn't urgent any more</b>. It waits until Monday as a normal change. Total loss: about <b>€320</b> instead of the roughly €7,000 three hours of waiting would have cost.</p>
  <p>Eli writes the path down that weekend:</p>
  <ol>
    <li><b>Smallest undo first</b>: a flag, a config, a rollback of the last change.</li>
    <li>If <b>new code must ship now</b>: the incident lead approves, <b>two people</b> do it (one writes, one reviews in the same call), the deploy is labelled <b>“emergency”</b> with the lead's name (which the pipeline accepts in a window and posts to the feed), and someone watches for 30 minutes.</li>
    <li><b>Written up within a working day</b>, like a normal change after the fact.</li>
  </ol>
  <p>From February to June there are <b>3 emergency changes</b>, and all 3 are written up.</p>""",
    how_figs=[em_how],
    steps=[("Ask for the smallest undo first", "Flag, config, or roll back the last change."),
           ("Stop the harm, then decide about the fix", "Often it can wait for a normal change."),
           ("If code must ship: the lead approves", "One named person decides."),
           ("Two people do it", "Write and review in the same call."),
           ("Label it and watch it", "“Emergency” + name; a watcher for 30 minutes."),
           ("Write it up within a day", "And review whether the path worked.")],
    vocab=[("Emergency change", "A change that must be made as soon as possible, often to restore service."),
           ("Mitigation", "Reducing harm now, without fixing the cause."),
           ("Smallest undo", "The quickest, least risky action that stops the harm."),
           ("Emergency CAB", "ITIL v3's small group for approving emergencies; at Larder, the incident lead."),
           ("Retroactive record", "The write-up of a change after it's been made."),
           ("Kill switch", "A flag that turns a feature off instantly.")],
    code=dict(file="ops/changes/emergency.md", note="written Sat 13 March 2027", plain=True, src="""
# Emergency changes

1 smallest undo first     flag off · config back · roll back the last change
                          (12 Mar: promo flag off at 17:01 → harm stopped)
2 code must ship now?     incident lead approves (name)
                          two people: one writes, one reviews, same call
                          pipeline label: emergency + lead's name (allowed in windows,
                          posted to the change feed)
                          watcher: 30 min after, named
3 within a working day    write-up as a normal change: why, what, risk, way back, result

Feb–Jun 2027: 3 emergency changes · 3 written up · 0 caused a second incident
"""),
    tools="tools: kill-switch flags for risky features, an “emergency” label the pipeline understands, and a write-up template.",
    ladder=[("break the rules or wait", ["Arguments under pressure.", "Rushed code in the peak."]),
            ("a written emergency path", ["Smallest undo first.", "Two people, a label, a write-up."]),
            ("kill switches everywhere", ["Every risky feature has a flag.", "Most emergencies need no code."]),
            ("automatic mitigation", ["Signals turn off a misbehaving feature by themselves.", "People decide the fix calmly."])],
    ladder_now=1,
    baseline="Each line compares <b>arguing whether to break the window rule</b> to <b>smallest undo first, then a light, named emergency path</b>.",
    ratings=[(2, 4, "Harm stopped in minutes, not hours."),
             (3, 3, "Neutral."),
             (2, 4, "One minute from decision to stop."),
             (2, 4, "No rushed code in the Friday window."),
             (2, 4, "Every emergency change is in the feed and written up."),
             (3, 3, "Neutral."),
             (2, 4, "≈ €320 instead of ≈ €7,000."),
             (2, 3, "The lead has a clear rule instead of an argument."),
             (3, 3, "A page and a habit.")],
    pitfalls=[("Jumping to new code", "A rushed fix in the peak causes a second incident.", "smallest undo first."),
              ("No emergency path", "People bypass the pipeline entirely.", "a light, named path that the pipeline accepts."),
              ("Emergency as a shortcut", "“Emergency” used to skip review on a normal day.", "only during an incident, with the lead's name."),
              ("No write-up", "Nobody learns how often this happens.", "written up within a working day.")],
    use=["An incident needs a change during a window or freeze.", "Harm is growing every minute.", "A fix is ready and people want to ship it now.", "Designing risky features (add a kill switch)."],
    skip=["Anything that can wait until the window closes: it's a normal change."],
    related=["<b>When Must We Not Change Anything?</b> (this volume)", "<b>Who Is in Charge?</b> (vol. 2)", "<b>Feature Flags</b> (cloud, vol. 6)", "<b>How Do We Undo It?</b> (this volume)"],
    quiz=[("What's the first question in an emergency change?", "What's the smallest undo that stops the harm?"),
          ("How did Dee stop the WELCOME10 losses?", "She turned off the promo-code flag at 17:01, a standard change allowed in the window."),
          ("Why did the code fix wait until Monday?", "Once the harm had stopped it wasn't urgent, so it went through as a normal change."),
          ("If code must ship in an emergency, what's needed?", "The lead's approval, two people, the emergency label with the lead's name, a watcher, and a write-up within a day."),
          ("What's the risk of “emergency” as a label?", "That it becomes a shortcut to skip review on normal days.")],
    quiz_sit=[("At 07:20 on a Tuesday, business orders fail because of a bug in this morning's 06:50 deploy. There's no flag. What do you do?", "Smallest undo: roll back the 06:50 deploy (emergency label, lead's name), watch the business orders, and fix the bug as a normal change after 09:00.")],
    try_it="List your three riskiest features. Does each have a kill switch you could turn off in a minute? For the one that doesn't, write down what the smallest undo would be in an emergency.",
    remember="In an emergency, <span class=\"hl\">stop the harm with the smallest undo</span> first. The fix can usually wait, and when it can't: <span class=\"hl\">two people, a name, a write-up</span>.",
    sources=["AXELOS, <i>ITIL 4: Change enablement</i> practice guide (2020): emergency changes.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 14, managing incidents (mitigate first).",
             "Pete Hodgson, “Feature Toggles” (martinfowler.com, 2017): ops toggles and kill switches."],
)

# ------------------------------------------------------------------ 09 Which Changes Fail?
dm_problem = Doodle(760, 250, "Doodle of a question from Marco in February 2027, after the change board trial: 'Are we getting safer or not?' Eli has a change feed with every change, and an incident list, but no numbers that connect them. He can tell stories about 29 October and 19 April. He can't say how many changes fail, or whether that's going up or down.",
                    "“Are we getting safer?” Lots of stories, no numbers that connect changes to failures.")
dm_problem.box(14, 30, 340, 110, "change feed", "blue", sub="every change, Oct → Feb", size=20, subsize=14)
dm_problem.box(406, 30, 340, 110, "incident list", "pink", sub="every incident", size=20, subsize=14)
dm_problem.note(380, 186, "nothing joins them · “safer?” → stories", "red", size=18)

dm_analogy = Doodle(760, 220, "Doodle of a bakery's four numbers on the wall: how many batches a day, how long from mixing to shelf, how many batches had to be thrown away, how long to bake a replacement. Faster and fewer thrown away go together in a good bakery; they're not a trade-off.",
                    "Four numbers on the bakery wall: batches a day, time to shelf, batches binned, time to replace.")
dm_analogy.row([("batches / day", None, "y"), ("mix → shelf", None, "y"), ("binned %", None, "pink"), ("time to replace", None, "green")], y=50, h=80, gap=14, size=17)
dm_analogy.note(380, 180, "in a good bakery, faster and fewer binned go together", "pen", size=18)

dm_how = Doodle(760, 380, "Larder's four delivery numbers, computed from the pipeline and the incident list from March 2027 and shown to Marco monthly. Deployment frequency: about 8 a day. Lead time for changes, commit to production: median 2 hours 10 minutes. Change failure rate, changes that needed a fix, rollback or caused an incident: 6 percent in the fourth quarter of 2026, 4 percent in the first quarter of 2027, 3 percent in the second. Time to restore after a failed change: median 14 minutes. Network and database changes failed most often, which fed back into the risk score.",
                "Four numbers from the pipeline and the incident list. Change failure rate 6 % → 3 %; deploys didn't slow down.")
for i, (t, v, f) in enumerate([("deploy frequency", "≈ 8 a day", "blue"), ("lead time", "median 2 h 10", "blue"), ("change failure rate", "6 % → 4 % → 3 %", "pink"), ("time to restore", "median 14 min", "green")]):
    dm_how.box(14 + i * 186, 14, 172, 120, t, f, sub=v, size=17, subsize=14)
dm_how.box(14, 160, 732, 90, None, "paper")
dm_how.text(380, 192, "failure rate by kind (Q2 2027): deploys 2 % · flags 1 %", size=15)
dm_how.text(380, 222, "infrastructure 8 % · network 11 % · database 9 %", size=15)
dm_how.note(380, 290, "faster and safer went together, as the research says", "pen", size=17)
dm_how.note(380, 330, "the numbers are for learning, never for ranking people", "red", size=16)

DORA = dict(
    slug="dora-metrics",
    kicker="a.k.a. “the four key metrics”",
    tldr="Four numbers show whether change is getting faster <b>and</b> safer: <b>deployment frequency</b>, <b>lead time for changes</b> (commit to production), <b>change failure rate</b> (share of changes that need a fix, a rollback or cause an incident), and <b>time to restore</b> after a failed change. Research (DORA) shows the best teams are good at all four: speed and stability go together. Compute them from your pipeline and incident list, look at them by <b>kind of change</b>, and use them for learning, never for ranking people.",
    chips=[("Family", "safety nets"), ("Lives in", "a monthly page from the pipeline and incident data, for Marco and tech leads"), ("Pairs with", "change board, incident metrics (vol. 2), risk scoring")],
    itil=dict(groups=["general"], chain=["improve"], practices=["measurement and reporting", "change enablement"],
              sre="(release engineering metrics); DORA's four keys", principles=["Progress iteratively with feedback", "Focus on value"],
              older="ITIL v3: change management KPIs (failed changes, backlog)"),
    problem_side="Larder, February 2027",
    problem="""  <p class="lead">After the change board trial, Marco asks: <b>“Are we getting safer or not?”</b> Eli has a change feed listing every change since October, and an incident list. <span class="hl-pink">Nothing connects them.</span> He can tell the stories of 29 October and of the change board, but he can't say how many changes fail, which kinds fail most, or whether things are getting better.</p>
  <ul>
    <li>Without numbers, every debate about process is opinions.</li>
    <li>“Slow down to be safe” and “speed up” both sound reasonable.</li>
    <li>Nobody can see which kind of change is actually risky.</li>
  </ul>""",
    problem_figs=[dm_problem],
    analogy_side="the bakery's four numbers",
    analogy="""  <p>A good bakery keeps <b>four numbers on the wall</b>: batches baked a day, time from mixing to shelf, batches thrown away, and time to bake a replacement. The surprising thing is that <b>faster and fewer thrown away go together</b>: small, frequent batches are easier to get right and quicker to replace. A bakery that slows down to avoid mistakes usually makes bigger batches, and bigger mistakes.</p>""",
    analogy_figs=[dm_analogy],
    map=[("Batches a day", "Deployment frequency"),
         ("Mixing to shelf", "Lead time: commit to production"),
         ("Batches thrown away", "Change failure rate"),
         ("Time to bake a replacement", "Time to restore after a failed change"),
         ("Small, frequent batches", "Small, frequent changes")],
    how_side="four numbers, by kind of change, monthly",
    how="""  <p>Bram joins the change feed and the incident list in <b>March</b>. A change counts as <b>failed</b> if it needed a fix, a rollback, or caused an incident within 24 hours. Each month Marco and tech leads get four numbers:</p>
  <ul>
    <li><b>Deployment frequency</b>: about <b>8 a day</b>.</li>
    <li><b>Lead time for changes</b>: median <b>2 h 10</b> from commit to production.</li>
    <li><b>Change failure rate</b>: <b>6 %</b> in Q4 2026, <b>4 %</b> in Q1 2027, <b>3 %</b> in Q2.</li>
    <li><b>Time to restore</b> after a failed change: median <b>14 minutes</b>.</li>
  </ul>
  <p>The most useful view is <b>by kind of change</b>. In Q2, deploys fail 2 % of the time and flags 1 %, but infrastructure 8 %, network <b>11 %</b> and database 9 %. That feeds straight back into the risk score and the reviewer list. Deploys didn't slow down while failures fell, which is exactly what the research predicts. Eli adds one rule: the numbers are <b>for learning, never for ranking people or teams</b>.</p>""",
    how_figs=[dm_how],
    steps=[("Define a failed change", "Needed a fix, a rollback, or caused an incident within 24 h."),
           ("Join the change feed and incident list", "Each incident links to its change, if any."),
           ("Compute the four numbers monthly", "From data, not memory."),
           ("Split by kind of change", "That's where the lessons are."),
           ("Show the trend with one sentence", "What changed, and why."),
           ("Never rank people by them", "People game numbers that judge them.")],
    vocab=[("Deployment frequency", "How often changes reach production."),
           ("Lead time for changes", "Time from a commit to that commit running in production."),
           ("Change failure rate", "The share of changes that cause a failure needing a fix or rollback."),
           ("Time to restore", "How long it takes to recover from a failed change."),
           ("DORA", "DevOps Research and Assessment: the research programme behind these four numbers."),
           ("Goodhart's law", "A number that becomes a target stops being a good measure.")],
    code=dict(file="ops/reports/delivery-2027-q2.md", note="for Marco and tech leads · Q2 2027", plain=True, src="""
# Delivery · Q2 2027                                       Q4 '26   Q1 '27   Q2 '27

deployment frequency    per day                            7        8        8
lead time               commit → production (median)       3 h 40   2 h 30   2 h 10
change failure rate     fix / rollback / incident ≤ 24 h   6 %      4 %      3 %
time to restore         after a failed change (median)     22 min   16 min   14 min

failure rate by kind (Q2)   deploys 2 % · flags 1 % · infrastructure 8 %
                            network 11 % · database 9 % · devices 3 %
what changed    risk score + knowing reviewers (Feb) · staging rebuilt (Mar)
                · ways back written (Apr)
rule            for learning, never for ranking people or teams
"""),
    tools="tools: the pipeline's deploy log, the change feed, the incident list with a “caused by change” link, and a small script.",
    ladder=[("stories, no numbers", ["“Safer?” answered by anecdotes.", "Process debates by opinion."]),
            ("four numbers monthly, by kind", ["Failed changes defined.", "Trends with a sentence."]),
            ("collected automatically", ["Incidents linked to changes by the tool.", "Dashboards per team."]),
            ("used to choose improvements", ["Each quarter, one number to improve, one experiment.", "Never a target for people."])],
    ladder_now=1,
    baseline="Each line compares <b>stories about changes</b> to <b>four delivery numbers, monthly, split by kind of change</b>.",
    ratings=[(3, 3, "Neutral on its own."),
             (2, 3, "Risky kinds of change are found and handled."),
             (2, 3, "Time to restore is watched, and falls."),
             (2, 4, "Failure rate 6 % → 3 %, and visible."),
             (2, 4, "Marco gets an answer in numbers."),
             (3, 3, "Neutral."),
             (2, 3, "Process debates end with data."),
             (3, 3, "Neutral."),
             (3, 3, "A script and an hour a month.")],
    pitfalls=[("Numbers as targets", "Teams split changes to raise frequency.", "use them to learn, not to judge."),
              ("No definition of failure", "Everyone counts differently.", "write it down: fix, rollback or incident within 24 h."),
              ("One number alone", "Fast but failing, or safe but stuck.", "all four together."),
              ("Only the total", "The risky kinds hide in the average.", "split by kind of change.")],
    use=["Someone asks whether you're getting safer or faster.", "Process changes are argued by opinion.", "After introducing a new change practice.", "Before deciding to slow down “for safety”."],
    skip=["Very few changes a month: describe each one instead."],
    related=["<b>Do We Need a Change Board?</b> (this volume)", "<b>Which Incident Numbers Mean Anything?</b> (vol. 2)", "<b>How Risky Is This Change?</b> (this volume)", "<b>Build Once, Deploy Many</b> (cloud, vol. 6)"],
    quiz=[("What are the four key metrics?", "Deployment frequency, lead time for changes, change failure rate, time to restore."),
          ("How does Larder define a failed change?", "One that needed a fix or rollback, or caused an incident within 24 hours."),
          ("What did splitting by kind show?", "Network (11 %), database (9 %) and infrastructure (8 %) changes fail far more than deploys (2 %)."),
          ("Do speed and stability trade off?", "The research says no: the best teams are good at both, because small, frequent changes are safer."),
          ("Why never rank people with these numbers?", "Numbers that judge people get gamed (Goodhart's law) and stop telling the truth.")],
    quiz_sit=[("A manager suggests a bonus for the team with the lowest change failure rate. What do you say?", "That it will be gamed: teams will avoid risky but necessary changes or stop recording failures. Use the numbers to choose improvements together, not to reward or rank.")],
    try_it="Take last month's changes and incidents. Mark which incidents followed a change within 24 hours. Compute your change failure rate overall and by kind of change. Which kind surprised you?",
    remember="Fast and safe <span class=\"hl\">go together</span>. Count four numbers, split them <span class=\"hl\">by kind of change</span>, and never use them to rank people.",
    sources=["Nicole Forsgren, Jez Humble and Gene Kim, <i>Accelerate</i> (2018).",
             "DORA, <i>Accelerate State of DevOps</i> reports (2014 onwards).",
             "AXELOS, <i>ITIL 4: Measurement and reporting</i> practice guide (2020)."],
)

NOTES = [ROLLBACK, VALIDATION, EMERGENCY, DORA]
