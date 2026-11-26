# Series 5 · On the Client's Floor · Vol. 4 · Delivery Under Fire · Holding the line (notes 8–12).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 08 How Do We Re-plan Without Lying?
rp_problem = Doodle(760, 240, "Doodle of the plan on 3 July 2028, the day the pilot is accepted. Velocity has been 38 points per sprint against 45 planned. Remaining work to wave 1 at that pace finishes 21 October, not 23 September. Callum's first instinct: plan at 45 again and use the buffer quietly.",
                    "38 points a sprint, not 45. At that pace, wave 1 is 21 October.", exact=True)
rp_problem.line("M40 200 L700 40", dash=True)
rp_problem.line("M40 200 L700 90", color="red")
rp_problem.note(600, 40, "plan: 45/sprint → 23 Sep", "pen", size=17)
rp_problem.note(600, 120, "real: 38/sprint → 21 Oct", "red", size=17)
rp_problem.note(260, 230, "Callum: “plan at 45, use the buffer”", "red", size=18)

rp_how = Doodle(760, 330, "The honest re-plan. Start from real velocity, 38, and the critical path: reconciliation tooling, then rehearsal 3, then cutover. Three options shown to Elaine: A, keep 23 September by moving two low-value features to wave 2; B, move wave 1 to 21 October; C, add two engineers, which costs margin. Chosen: A plus one engineer. The buffer, nine working days, shown openly on the plan as buffer, not hidden in the tasks.",
                "Real velocity, the critical path, three options, and the buffer in plain sight.", exact=True)
for i, (h, sub, fill) in enumerate([("A · keep 23 Sep", "2 features → wave 2", "green"), ("B · move to 21 Oct", "same scope", "y"), ("C · add 2 people", "costs margin", "pink")]):
    rp_how.box(14 + i * 250, 20, 232, 90, h, fill, sub=sub, size=19, subsize=15)
rp_how.box(14, 136, 732, 60, "chosen: A + 1 engineer (from Leeds)", "green", size=18)
rp_how.box(14, 216, 540, 60, "critical path: reconciliation → rehearsal 3 → cutover", "paper", size=16)
rp_how.box(570, 216, 176, 60, "buffer", "y", sub="9 days, visible", size=18, subsize=14)
rp_how.note(380, 310, "planned at 38, not at the number we wished for", "red", size=18)

REPLAN = dict(
    slug="re-planning", date=date(2028, 7, 3), meta=on_site(date(2028, 7, 3)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. re-planning a slipping programme",
    tldr="Re-planning goes wrong when the new plan is built from the old hopes. Start from <b>real velocity</b> and the <b>critical path</b>, show the client <b>options</b> (scope, date, people) with their costs, and make the <b>buffer visible</b> as buffer, not hidden inside tasks. A re-plan you'll have to re-plan again in six weeks costs more trust than the first slip.",
    chips=[("Family", "holding the line"), ("Lives in", "delivery/lodestar/plan-v2.3.md"), ("Pairs with", "the watermelon report, protecting margin")],
    problem_side="The Grid, 3 July 2028",
    problem="""  <p class="lead">On <b>Monday 3 July</b> the pilot's milestone (M3) is accepted after its fix: exceptions down to 0.3 %. The same day, Callum shows Ines the numbers for wave 1.</p>
  <ul>
    <li>The plan assumed <b>45</b> points a sprint. The last eight sprints averaged <b>38</b>.</li>
    <li>At 38, the remaining work finishes on <b>21 October</b>. Wave 1 night is <b>23 September</b>.</li>
    <li>Callum's proposal: re-plan at 45 (“the side-door work has stopped, we'll speed up”) and absorb any gap in the <b>nine days of buffer</b>. <span class="hl-pink">Nobody outside Wrenfield would need to know.</span></li>
  </ul>""",
    problem_figs=[rp_problem],
    sides=dict(client=("Elaine", "<p>Elaine has just survived a steering ambush and a rejected milestone. She wants to know whether 23 September is real. If the plan changes again in August, she'll stop believing any date, and so will Priya.</p>", "Is 23 September real? Tell me now, not in August."),
                vendor=("Ines and Callum", "<p>Callum's plan might work. If it doesn't, Wrenfield will be re-planning in August with no buffer and no options, after promising it was fine. Ines would rather show the slip now, while there are still choices.</p>", "Plan at the speed we are, not the speed we wish we were.")),
    sides_after="A buffer hidden inside tasks gets spent without anyone noticing. A buffer on the plan can be watched, and protected.",
    analogy_side="the long-distance runner",
    analogy="""  <p>A marathon runner at mile 15, slower than planned, doesn't decide to run the last eleven miles at her original pace “because she'll feel better”. She <b>works out her real pace</b>, decides what matters (a finish, or a time), and tells her coach. If she lies to herself at mile 15, she finds out at mile 22, when nothing can be done.</p>""",
    map=[("Real pace at mile 15", "38 points a sprint"),
         ("The original pace", "45 points, the plan"),
         ("A finish or a time", "Keep the date and cut scope, or keep the scope and move the date"),
         ("Telling the coach", "Showing Elaine the options"),
         ("Finding out at mile 22", "Re-planning in August with no buffer")],
    how_side="real velocity, critical path, options, visible buffer",
    how="""  <p><b>Real velocity.</b> The re-plan uses <b>38</b>, the average of the last eight sprints. Not 45, not a hoped-for 42.</p>
  <p><b>Critical path.</b> Hana and Oskar trace what must happen in order before wave 1 night: reconciliation tooling (the longest chain), then rehearsal 3 on 26 August, then the cutover runbook. Work not on that path can move without moving the date.</p>
  <p><b>Options, with costs.</b> Ines takes three to Elaine. <b>A</b>: keep 23 September by moving two low-value features (bulk address edit, a reporting screen) to wave 2. <b>B</b>: keep the scope, move wave 1 to 21 October (a re-baseline, and Rupert's board). <b>C</b>: add two engineers from Leeds (it shortens the build by about three weeks and costs margin).</p>
  <p><b>Elaine chooses A plus one engineer.</b> The plan becomes v2.3. The <b>nine days of buffer</b> sit on it as a separate bar, labelled buffer, with a rule: any day used is reported in that week's status. By wave 1 night, four of the nine have been used, all reported.</p>""",
    how_figs=[rp_how],
    steps=[("Measure real velocity", "Recent average, not the plan."),
           ("Find the critical path", "What must happen in order before the date."),
           ("Build options", "Scope, date, people, each with its cost."),
           ("Let the client choose", "With a recommendation."),
           ("Make the buffer visible", "A separate bar, reported when used."),
           ("Re-plan once, properly", "Not every two weeks.")],
    vocab=[("Velocity", "How much work a team completes per sprint, on average."),
           ("Critical path", "The longest chain of dependent tasks; it sets the earliest finish."),
           ("Buffer", "Time held in reserve for the unexpected."),
           ("Scope trade", "Moving or removing features to protect a date."),
           ("Brooks's law", "Adding people to a late project often makes it later; it depends when and who."),
           ("Re-plan", "A revised plan from current facts, agreed with the client.")],
    code=dict(file="delivery/lodestar/plan-v2.3.md", note="agreed with Elaine · Mon 3 Jul 2028", src="""
PLAN v2.3 · WAVE 1 (night: Sat 23 Sep 2028)

velocity        last 8 sprints: 36 41 35 39 37 40 38 38 → 38 (plan was 45)
remaining       at 38/sprint: done 21 Oct (too late)
critical path   reconciliation tooling (S24–S27) → rehearsal 3 (26 Aug) → runbook
options         A keep 23 Sep: bulk address edit + MI screen → wave 2   (−58 points)
                B move to 21 Oct: same scope; re-baseline via Horizon board
                C +2 engineers: ≈ −3 weeks; cost ≈ £96k
chosen          A + 1 engineer (Leeds, from S24) · DL-047
buffer          9 working days, shown as its own bar; any use reported that week
"""),
    contract=dict(side="what can move without a re-baseline", doc="Lodestar SOW · §4.3 and Schedule 4", date="baseline v2.0", stamp="replanned",
                  clauses=[("4.3", "The Supplier may re-plan work within a Milestone without approval, provided Milestone dates and the scope in Schedule 2 are unaffected.", "moving two features to wave 2 changes Schedule 2. so: Elaine's decision, DL-047."),
                           ("Sch. 2, 7.1", "<ins>Bulk address edit and the operational MI screen are delivered in Wave 2.</ins>", "two features out, in writing. not quietly dropped.")],
                  plain="you can re-plan inside your own work freely, but moving scope between waves changes the contract's description of the work. Make that a decision, recorded, not a quiet omission."),
    health=dict(now="a",
                g=("trust is high", ["Show the real velocity early.", "Options in a conversation.", "Decide in a day."]),
                a=("burned by slips", ["Real numbers, three options.", "Buffer visible.", "One re-plan, properly."]),
                r=("every slip a dispute", ["Re-plan in writing with evidence.", "Scope changes through change control.", "Buffer use reported weekly."])),
    pressure=dict(level=4, title="the slip nobody would notice", cost="a tempting shortcut · one more hard conversation",
                  items=["Callum's plan was tempting because it might have worked. “Might” isn't a plan with 380,000 customers.", "After the ambush, admitting another slip felt dangerous. Admitting it with options felt like leadership."]),
    baseline="Each line compares <b>re-planning at the hoped-for 45 and spending the buffer quietly</b> with <b>real velocity, the critical path, options and a visible buffer</b>.",
    ratings=[(2, 4, "Elaine chose, with the facts, in July."),
             (2, 4, "No impossible sprints ahead."),
             (3, 3, "One engineer added; features deferred, not given away."),
             (3, 4, "Two features moved to wave 2, in writing."),
             (3, 4, "The critical path drives the plan."),
             (2, 5, "Slip seen in July, not August."),
             (2, 4, "DL-047 and the Schedule 2 change recorded."),
             (3, 4, "Decided in a day."),
             (3, 3, "A buffer to report weekly.")],
    pitfalls=[("Re-planning at the hoped-for speed", "Another re-plan in six weeks.", "real velocity."),
              ("Hiding buffer in tasks", "It's spent unseen.", "a separate, reported buffer."),
              ("Only one option", "The client can't choose.", "scope, date, people."),
              ("Adding people late", "They slow the team down.", "add early, and only experienced people."),
              ("Dropping scope quietly", "Discovered at acceptance.", "move it in writing.")],
    use=["Velocity is below plan for several sprints.", "A milestone is at risk.", "After any major surprise."],
    skip=["A one-sprint dip with a known, fixed cause."],
    related=["<b>Why Is Everything Green Except the Truth?</b> (this volume)", "<b>How Do We Protect the Margin?</b> (this volume)", "<b>How Long Will It Really Take?</b> (vol. 1)", "<b>What If We Ran It a Thousand Times?</b> (Sanne, vol. 5)"],
    quiz=[("What velocity did the re-plan use?", "38, the average of the last eight sprints."),
          ("What were options A, B and C?", "A: keep the date, move two features to wave 2; B: move the date; C: add two engineers."),
          ("What did Elaine choose?", "A plus one engineer."),
          ("Why make the buffer a separate bar?", "So its use is visible and reported, not spent unseen."),
          ("Why record the moved features in Schedule 2?", "Moving scope between waves changes the contract's description of the work.")],
    quiz_sit=[("Graham suggests option C with four engineers to finish early and impress Priya. What do you say?", "Four new people in the last ten weeks would slow the team while they learn. One experienced engineer on the critical path helps; more would hurt, and cost margin.")],
    try_it="Take your current plan. Recalculate it with your real average speed. Where's the critical path? Write three options and put your buffer on the plan as its own line.",
    remember="Re-plan at <span class=\"hl\">the speed you are</span>, not the speed you hoped. Options for the client, and the buffer <span class=\"hl\">in plain sight</span>.",
    late=dict(when="Mon 3 July 2028 · 21:15 · hotel near The Grid",
              lines=["Pilot accepted this morning. Re-plan this afternoon. Some days have two moods.",
                     "Callum's plan might have worked. I couldn't bet 380,000 customers on “might”.",
                     "Elaine chose A in ten minutes. Two features to wave 2. The buffer is a grey bar with “9” on it. Every day we use, we say so."]),
    sources=["Frederick Brooks, <i>The Mythical Man-Month</i> (1975, anniversary ed. 1995).",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005): velocity and re-planning.",
             "Eliyahu Goldratt, <i>Critical Chain</i> (1997): visible project buffers."],
)

# ------------------------------------------------------------------ 09 Why Do the Test Environments Never Work?
te_problem = Doodle(760, 240, "Doodle of Oskar's environment log for March and April 2028: 31 per cent of planned test days lost. Three shared test environments, used by four other MetroVolt projects. The MAVIS test copy dates from 2019. Nobody books anything; whoever arrives first on Monday wins.",
                    "31 % of test days lost. Three environments, five projects, a MAVIS copy from 2019.", exact=True)
for i, (h, sub) in enumerate([("SIT", "shared by 5 projects"), ("UAT", "shared by 4"), ("PERF", "not built")]):
    te_problem.box(14 + i * 250, 30, 232, 90, h, "pink" if i == 2 else "y", sub=sub, size=22, subsize=15)
te_problem.box(14, 140, 360, 60, "MAVIS test copy: 2019", "paper", size=17)
te_problem.box(386, 140, 360, 60, "31 % of test days lost", "pink", size=18)
te_problem.note(380, 226, "first to arrive on Monday wins", "red", size=18)

te_how = Doodle(760, 330, "What Oskar did. Count the loss: a daily environment log, test days planned versus usable, by cause. Book environments like a meeting room: a shared calendar agreed with the other projects, in half-days. Refresh the MAVIS test copy, masked, from 2028 data. Test without environments where possible: contract tests, the golden master, synthetic data. And report the loss in the weekly status as a measure. By July, lost days fell to 9 per cent.",
                "Count the loss, book environments, refresh the data, test without them where you can.", exact=True)
for i, (h, sub, fill) in enumerate([("count", "daily log, by cause", "y"), ("book", "shared calendar", "blue"), ("refresh", "masked 2028 copy", "green"), ("test without", "contracts, golden master", "paper")]):
    te_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=14)
te_how.box(14, 150, 360, 80, "Mar–Apr", "pink", sub="31 % of test days lost", size=22, subsize=15)
te_how.box(386, 150, 360, 80, "July", "green", sub="9 % lost", size=22, subsize=15)
te_how.note(380, 286, "the loss is a status measure, every week", "pen", size=18)

TEST_ENVS = dict(
    slug="test-environments", date=date(2028, 5, 9), meta=on_site(date(2028, 5, 9)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. shared test environments you don't control",
    tldr="On a client's estate, test environments are shared, old and owned by someone else, and they quietly eat your schedule. <b>Count the loss</b> every day, by cause. <b>Book</b> shared environments like meeting rooms, agreed with the other projects. Get <b>realistic, masked test data</b>. Test <b>without</b> the environment wherever you can (contract tests, recorded behaviour, synthetic data). And report the lost days as a <b>measure</b>, so the owner can fix the cause.",
    chips=[("Family", "holding the line"), ("Lives in", "test/environment-log.md · the booking calendar"), ("Pairs with", "escalation, the watermelon report, reading legacy code (vol. 3)")],
    problem_side="The Grid, 9 May 2028",
    problem="""  <p class="lead">Oskar has kept a quiet log since March. On <b>9 May</b> he shows Ines the total: <b>31 %</b> of planned test days in March and April were lost.</p>
  <ul>
    <li>Lodestar shares MetroVolt's <b>three test environments</b> with four other projects. Whoever arrives first on Monday wins.</li>
    <li>The <b>MAVIS test copy dates from 2019</b>: thousands of today's customers don't exist in it.</li>
    <li>The performance environment hasn't been built yet. <span class="hl-pink">Hollis's team owns all of it, and is three people short.</span></li>
  </ul>""",
    problem_figs=[te_problem],
    sides=dict(client=("Hollis's team", "<p>MetroVolt's environments were sized for one project at a time. Horizon cut the team that runs them. Five projects now compete for three environments, and each one thinks it's the priority. Nobody has counted what that costs.</p>", "Everyone needs the environment this week."),
                vendor=("Oskar", "<p>For Oskar, a lost test day is a day the team can't prove anything, on a fixed price. Complaining hasn't worked; the other projects complain too. He needs the loss <b>measured</b>, the time <b>shared fairly</b>, and as much testing as possible that <b>doesn't need</b> the environments at all.</p>", "If we can't control them, we can measure them, share them and need them less.")),
    sides_after="Environment problems are rarely anyone's fault. They're a shared resource nobody manages as one.",
    analogy_side="the shared kitchen",
    analogy="""  <p>Five flatmates share one kitchen and everyone wants it at seven. Shouting doesn't help. A <b>rota on the fridge</b> does, along with a note of how often dinner was late and why, fresh food instead of last year's tins, and doing the chopping at your own desk so you need the cooker for less time.</p>""",
    map=[("Five flatmates, one kitchen", "Five projects, three environments"),
         ("A rota on the fridge", "The shared booking calendar"),
         ("A note of late dinners and why", "The daily environment log"),
         ("Fresh food, not last year's tins", "A masked 2028 copy of MAVIS"),
         ("Chopping at your own desk", "Contract tests and the golden master, run without the environment")],
    how_side="count, book, refresh, test without",
    how="""  <p><b>Count it.</b> Oskar's log becomes a daily record: test days planned, test days usable, and the <b>cause</b> of every loss (environment down, taken by another project, data missing, deployment failed). March–April: <b>31 %</b> lost, half of it from collisions with other projects.</p>
  <p><b>Book it.</b> Oskar proposes, and Hollis's team adopts, a <b>shared booking calendar</b> for all five projects, in half-days, agreed at a fifteen-minute meeting every Friday. Collisions drop to almost nothing in two weeks.</p>
  <p><b>Refresh the data.</b> A new MAVIS test copy from <b>2028 data</b>, with personal fields masked (the DPIA allows it). Thousands of “missing customer” failures disappear.</p>
  <p><b>Test without it.</b> The 58 Halvorsen contract tests, the golden master for CUSTBL07 and synthetic data for the migration tooling all run on Wrenfield's own build servers, no shared environment needed. About 40 % of the test suite moves there.</p>
  <p>The loss goes into the weekly status as a measure. By July it's <b>9 %</b>.</p>""",
    how_figs=[te_how],
    steps=[("Log every lost test day, by cause", "Daily, in a shared sheet."),
           ("Share the numbers with the environment owner", "As data, not blame."),
           ("Book shared environments", "A calendar, half-days, agreed weekly."),
           ("Refresh test data, masked", "Recent enough to be realistic."),
           ("Move tests off shared environments", "Contract tests, recorded behaviour, synthetic data."),
           ("Report the loss as a measure", "Weekly, with the trend.")],
    vocab=[("Test environment", "A copy of the systems used for testing, not for customers."),
           ("Environment booking", "Reserving a shared environment for a period."),
           ("Data masking", "Replacing personal data with realistic but fake values."),
           ("Synthetic data", "Generated data with the right shape and oddities."),
           ("Environment drift", "Test and production configurations diverging."),
           ("Shift left", "Testing earlier, often without full environments.")],
    code=dict(file="test/environment-log.md", note="summary · Tue 9 May 2028", src="""
ENVIRONMENT LOG · LODESTAR (planned vs usable test days)

period      planned  usable  lost   cause of loss
Mar 2028    62       43      31 %   collisions 11 · env down 4 · data missing 3 · deploy 1
Apr 2028    58       40      31 %   collisions 8 · env down 5 · data missing 4 · deploy 1
actions     shared booking calendar (5 projects, half-days, Fridays 15 min)  from 12 May
            MAVIS test copy refreshed from 2028 data, masked (DPIA ok)        from 22 May
            40 % of suite moved off shared envs (contract tests, golden master,
            synthetic migration data)                                         from 15 May
Jul 2028    60       55       9 %   env down 3 · deploy 2
"""),
    contract=dict(side="whose environments they are", doc="Lodestar SOW · Appendix C, D-12", date="signed 30 June 2027", stamp="dependency",
                  clauses=[("D-12", "MetroVolt provides integration and user-acceptance test environments, with MAVIS test data no older than 12 months, as set out in Schedule 9.", "“no older than 12 months”. the 2019 copy was a dependency miss, and nobody had counted it."),
                           ("3.4", "Where a Dependency is late, the Supplier is entitled to relief day for day on affected Milestones.", "we didn't claim. we fixed. the log meant we could have.")],
                  plain="test environments and test data are usually the client's dependencies. Counting the lost days gives you the evidence for relief, and, better, the evidence the owner needs to fix the cause."),
    health=dict(now="g",
                g=("the owner wants help", ["Share the log and the calendar idea.", "Fix data together.", "Thank them as it improves."]),
                a=("a stretched owner, many projects", ["Count by cause.", "Propose the booking calendar.", "Test without where you can."]),
                r=("environments as a battleground", ["Log formally.", "Relief notices if needed.", "Your own test infrastructure for what you control."])),
    pressure=dict(level=3, title="the invisible thief", cost="a third of the test days, for two months",
                  items=["Lost test days feel like nobody's fault and everyone's problem. A number gives them an owner.", "Oskar kept the log quietly for six weeks. Ask your test lead what they're quietly counting."]),
    baseline="Each line compares <b>first-come-first-served environments and complaints</b> with <b>a daily log, a booking calendar, fresh masked data and tests that don't need the environments</b>.",
    ratings=[(3, 4, "Hollis's team gets a tool, not a complaint."),
             (2, 4, "Fewer wasted days for testers."),
             (2, 4, "31 % → 9 % lost test time."),
             (3, 3, "Neutral."),
             (3, 4, "Tests run on realistic data."),
             (2, 4, "Loss measured weekly."),
             (2, 4, "Evidence for relief if ever needed."),
             (3, 4, "Two weeks to see improvement."),
             (3, 3, "A calendar and a log to keep.")],
    pitfalls=[("Complaining without numbers", "Everyone complains; nothing changes.", "a daily log, by cause."),
              ("Grabbing environments", "A war between projects.", "a shared calendar."),
              ("Old test data", "Failures that aren't real.", "refresh, masked."),
              ("Everything needs the environment", "Testing stops when it's down.", "contract tests and synthetic data."),
              ("Silent loss", "The slip appears as “testing behind”.", "report lost days as a measure.")],
    use=["Shared test environments on a client site.", "Testing is behind and nobody knows why.", "Old or unrealistic test data."],
    skip=["You own your environments end to end: still count the loss."],
    related=["<b>When Do We Go Over Their Heads?</b> (this volume)", "<b>How Do We Read Code Nobody Owns?</b> (vol. 3)", "<b>Contract Testing</b> (patterns, Vol. 4)", "<b>Why Is Everything Green Except the Truth?</b> (this volume)"],
    quiz=[("What share of test days was lost in March and April?", "31 %."),
          ("What was the biggest cause?", "Collisions with other projects using the same environments."),
          ("What fixed collisions?", "A shared booking calendar in half-days, agreed weekly."),
          ("How did the team test without environments?", "Contract tests, the golden master and synthetic data on their own build servers."),
          ("What did the contract say about test data?", "MetroVolt's MAVIS test data should be no older than twelve months (D-12).")],
    quiz_sit=[("Another project books the UAT environment for the whole of rehearsal week. What do you do?", "Raise it at the Friday booking meeting with the numbers: rehearsal 3 is on the wave 1 critical path. Offer to swap half-days. If it can't be settled, escalate via the ladder with a proposal.")],
    try_it="For two weeks, log every test day you planned and whether you could use it, with the cause. What share was lost? Which tests could run without the shared environment?",
    remember="You can't control shared environments. You can <span class=\"hl\">count the loss</span>, book them fairly and <span class=\"hl\">need them less</span>.",
    late=dict(when="Tue 9 May 2028 · 20:45 · hotel near The Grid",
              lines=["Oskar's quiet log: 31 % of test days lost. Six weeks he kept it before showing anyone. Testers are like that.",
                     "Hollis's team loved the booking calendar. They'd wanted one for years.",
                     "A MAVIS test copy from 2019. Half our “defects” were customers who didn't exist yet."]),
    sources=["Lisa Crispin and Janet Gregory, <i>More Agile Testing</i> (2014): test environments.",
             "Jez Humble and David Farley, <i>Continuous Delivery</i> (2010).",
             "UK Information Commissioner's Office, guidance on anonymisation and pseudonymisation."],
)

# ------------------------------------------------------------------ 10 Is It a Defect or a Change?
dt_problem = Doodle(760, 240, "Doodle of the user-acceptance testing defect list on 27 July 2028: 412 items logged by MetroVolt's testers as defects. A closer look: some are real defects, many are wishes, some are duplicates. Every one is labelled defect, which means Wrenfield must fix it for free under the fixed price.",
                    "412 “defects”. Some are bugs. Many are wishes. All say “fix for free”.", exact=True)
dt_problem.box(24, 30, 300, 170, "UAT list", "pink", sub="412 · all labelled “defect”", size=24, subsize=16)
for i, t in enumerate(["“button should be blue”", "“add a field for…”", "balance off by 1p", "same as #217"]):
    dt_problem.box(380, 20 + i * 48, 366, 40, t, "paper", size=16)

dt_how = Doodle(760, 340, "The triage board, three times a week, with Rosa, MetroVolt's test lead, and Oskar. Agreed definitions: a defect fails an acceptance criterion or Schedule 2; a change is new or different behaviour; plus duplicate and not reproducible. Severity definitions from 1 to 4. Result for the 412: 188 defects, 161 changes, 63 duplicates or not reproducible. Changes go to the change register; defects are fixed by severity.",
                "Agreed definitions, a joint board, and every item in one of four boxes.", exact=True)
for i, (h, n, sub, fill) in enumerate([("defect", "188", "fails a criterion", "pink"), ("change", "161", "new behaviour", "y"), ("duplicate", "41", "same as another", "paper"), ("not reproducible", "22", "can't repeat", "paper")]):
    dt_how.box(14 + i * 186, 20, 174, 140, h, fill, sub=sub, size=19, subsize=14)
    dt_how.text(101 + i * 186, 58, n, cls="t-head", size=28)
dt_how.box(14, 180, 732, 60, "severity: 1 stops wave 1 · 2 serious, no workaround · 3 workaround · 4 cosmetic", "blue", size=16)
dt_how.box(14, 256, 732, 50, "Mon / Wed / Fri 11:00 · Rosa + Oskar decide together", "green", size=17)

DEFECT_TRIAGE = dict(
    slug="defect-triage", date=date(2028, 7, 27), meta=on_site(date(2028, 7, 27)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. defect triage in user-acceptance testing",
    tldr="In acceptance testing on a fixed price, the word “defect” means “fix for free”, so it's used for everything. Agree <b>definitions</b> in advance: a <b>defect</b> fails an acceptance criterion or the agreed design; a <b>change</b> is new or different behaviour; plus <b>duplicate</b> and <b>not reproducible</b>. Triage <b>together</b>, client and vendor, several times a week, with agreed <b>severities</b>. Then fix defects by severity and send changes to the change register.",
    chips=[("Family", "holding the line"), ("Lives in", "test/triage-board (Jira LODE, triage view)"), ("Pairs with", "acceptance criteria (vol. 2), side-door scope")],
    problem_side="The Grid, July 2028",
    problem="""  <p class="lead">User-acceptance testing starts on <b>3 July</b>, with MetroVolt's testers led by <b>Rosa</b>. By <b>27 July</b> they've logged <b>412 defects</b>.</p>
  <ul>
    <li>Some are real: a balance off by a penny for a tariff Bert forgot; a screen that crashes on Welsh characters.</li>
    <li>Many aren't: “the button should be blue like MAVIS”, “add a field for the meter reader's name”, “sort by street, not postcode”.</li>
    <li>Every one is labelled <b>defect</b>, which under the fixed price means <span class="hl-pink">fix for free, before wave 1</span>.</li>
  </ul>""",
    problem_figs=[dt_problem],
    sides=dict(client=("Rosa and the testers", "<p>MetroVolt's testers are Customer Ops staff who'll use Lodestar every day. To them, anything that makes the job harder is a defect. They aren't trying to get free work; they're trying to make the system usable, and “defect” is the only label the tool gives them.</p>", "It doesn't work the way we need. That's a defect."),
                vendor=("Oskar and Ines", "<p>Fixing 412 items before 23 September is impossible, and many of them aren't Wrenfield's to fix for free. But arguing item by item with the people who'll use the system is the fastest way to lose them. Wrenfield needs shared definitions and a shared board.</p>", "Same words, same board, decided together.")),
    sides_after="Most “defect versus change” fights are really about missing definitions. Agree the words, and most items sort themselves.",
    analogy_side="the new-build snagging list",
    analogy="""  <p>When you move into a new-build house, you walk round with the builder making a <b>snagging list</b>. A cracked tile is a snag: the builder fixes it free. “I'd like a socket here” isn't a snag: it's an extra, priced. Good builders and buyers agree the difference <b>before</b> the walk-round, and do it <b>together</b>, so nobody argues about each item.</p>""",
    map=[("The snagging list", "The UAT defect list"),
         ("A cracked tile", "A balance off by a penny: a defect"),
         ("“A socket here”", "“Add a field for the meter reader”: a change"),
         ("Agreeing the difference first", "Definitions agreed with Rosa"),
         ("Walking round together", "The triage board, three times a week")],
    how_side="definitions, a joint board, severities, two routes",
    how="""  <p><b>Definitions</b>, agreed between Oskar and Rosa and approved by Elaine: a <b>defect</b> is behaviour that fails an acceptance criterion (Schedule 4) or contradicts the agreed design (Schedule 2); a <b>change</b> is new or different behaviour; a <b>duplicate</b> is the same as another item; <b>not reproducible</b> can't be repeated with the steps given.</p>
  <p><b>Severities</b>: <b>1</b> stops wave 1; <b>2</b> serious, no workaround; <b>3</b> has a workaround; <b>4</b> cosmetic. Wave 1 needs zero severity 1 and 2 defects (a go / no-go criterion).</p>
  <p><b>A joint triage board</b>, Monday, Wednesday and Friday at 11:00, thirty minutes: Rosa and Oskar decide each new item together, with the tester who raised it if needed. The first sessions clear the backlog: of 412, <b>188 defects</b>, <b>161 changes</b>, <b>41 duplicates</b>, <b>22 not reproducible</b>.</p>
  <p><b>Two routes.</b> Defects are fixed by severity: all 23 severity 1–2 fixed by 25 August. Changes go to the change register; Elaine takes 19 into the change pool (they matter for go-live), the rest to wave 2. Rosa says the definitions helped her testers too: “Now they know what to write.”</p>""",
    how_figs=[dt_how],
    steps=[("Agree definitions before testing starts", "Defect, change, duplicate, not reproducible."),
           ("Agree severities", "And which block go-live."),
           ("Triage jointly, often", "Client and vendor leads, short sessions."),
           ("Decide every item into one box", "No “TBD” category."),
           ("Fix defects by severity", "Severity 1–2 first."),
           ("Route changes through the register", "Pool now, or a later wave.")],
    vocab=[("Defect", "Behaviour that fails an agreed criterion or design."),
           ("Change", "New or different behaviour from what was agreed."),
           ("Severity", "How badly a defect affects use; set by agreed definitions."),
           ("Triage", "Quickly sorting items into categories and priorities."),
           ("UAT", "User-acceptance testing, by the people who'll use the system."),
           ("Snagging", "Listing small faults to be fixed before handover.")],
    code=dict(file="test/triage-definitions.md", note="agreed Oskar + Rosa, approved by Elaine · 24 Jul 2028", src="""
UAT TRIAGE · DEFINITIONS AND RESULTS

defect           fails a Schedule 4 criterion or contradicts Schedule 2
change           new or different behaviour from Schedule 2 → change register
duplicate        same as an existing item (link it)
not reproducible can't be repeated with the steps given (ask the tester, then close)
severity         1 stops wave 1 · 2 serious, no workaround · 3 workaround · 4 cosmetic
board            Mon / Wed / Fri 11:00, 30 min · Rosa + Oskar · decide every item
first 412        defects 188 (sev 1: 4 · sev 2: 19 · sev 3: 102 · sev 4: 63)
                 changes 161 (→ pool 19, £41k · → wave 2 142)
                 duplicates 41 · not reproducible 22
by 25 Aug        all sev 1–2 fixed (go / no-go criterion C6)
"""),
    contract=dict(side="what the contract calls a defect", doc="Lodestar SOW · §10 (warranty) and Schedule 4", date="signed 30 June 2027", stamp="defined",
                  clauses=[("10.1", "A Defect is a failure of the Solution to conform to Schedule 2 or to meet the Acceptance Criteria in Schedule 4.", "the contract already had the definition. the testers had never seen it."),
                           ("7.6", "No Change is binding unless recorded in the Change Register and approved under this clause.", "161 changes, now recorded.")],
                  plain="the contract usually defines “defect” already. Showing that definition to the client's testers, and triaging with them, turns 412 arguments into one agreement."),
    health=dict(now="g",
                g=("testers trust you", ["Definitions shared on day one.", "Light triage.", "Changes priced quickly."]),
                a=("everything is a defect", ["Definitions from the contract.", "Joint board, decided together.", "Pool for changes that matter now."]),
                r=("defects as leverage", ["Every item decided and recorded.", "Severity by definition only.", "Escalate disagreements by the ladder."])),
    pressure=dict(level=4, title="412 items", cost="seven weeks to wave 1 · testers who'll use the system daily",
                  items=["Arguing with users about their own system is a losing game. Agree the words; then the words do the arguing.", "Rosa is on your side. She wants a working system on 23 September as much as you do."]),
    baseline="Each line compares <b>412 “defects” argued one by one</b> with <b>agreed definitions, severities and a joint triage board</b>.",
    ratings=[(3, 4, "Testers feel heard; their wishes are recorded."),
             (2, 4, "The team fixes what matters first."),
             (1, 4, "161 changes aren't fixed for free."),
             (2, 5, "Every item has a category."),
             (3, 4, "Real defects get attention."),
             (2, 4, "Severity 1–2 tracked to zero."),
             (2, 4, "Definitions from §10.1; decisions logged."),
             (3, 4, "Three sessions a week, thirty minutes."),
             (3, 3, "A board to run.")],
    pitfalls=[("No definitions", "Every item is an argument.", "agree them before testing."),
              ("Vendor-only triage", "The client feels overruled.", "decide together."),
              ("A “to be decided” pile", "It grows forever.", "every item, one box."),
              ("Changes fixed for free", "The fixed price leaks.", "change register."),
              ("Changes refused outright", "Users hate the system.", "pool what matters now, schedule the rest.")],
    use=["User-acceptance testing on a fixed price.", "Testers who aren't professional testers.", "A large defect backlog."],
    skip=["Time and materials, where changes are simply prioritised work: still agree severities."],
    related=["<b>How Will We Know It's Done?</b> (vol. 2)", "<b>Where Did This Extra Work Come From?</b> (this volume)", "<b>When Do We Quote the Contract?</b> (next note)", "<b>Definition of Ready and Done</b> (Grace, vol. 3)"],
    quiz=[("What is a defect, by the contract?", "A failure to conform to Schedule 2 or to meet the acceptance criteria."),
          ("What is a change?", "New or different behaviour from what was agreed."),
          ("How were the 412 sorted?", "188 defects, 161 changes, 41 duplicates, 22 not reproducible."),
          ("Who decides each item?", "Rosa and Oskar together, at the triage board."),
          ("What happened to the changes?", "19 into the change pool for go-live, the rest to wave 2.")],
    quiz_sit=[("A tester insists “sort by street” is a defect because MAVIS did it. What do you decide?", "Check Schedule 2: if it specifies sorting, it's a defect; if not, it's a change. If it's a change that matters for go-live, propose it for the pool. Either way, decide it at the board with Rosa.")],
    try_it="Take your project's bug list. Write definitions for defect and change from your contract or agreement, and sort twenty items. How many “defects” were changes?",
    remember="Agree <span class=\"hl\">the words</span> before the testing, then triage <span class=\"hl\">together</span>. Defects get fixed; changes get decided.",
    late=dict(when="Thu 27 July 2028 · 21:10 · hotel near The Grid",
              lines=["412. Rosa looked as tired as Oskar. They're both right about different items.",
                     "The contract already defined “defect” in clause 10.1. Nobody had shown it to the testers.",
                     "188 real ones. 23 serious. All before the night, or there's no night."]),
    sources=["Cem Kaner, James Bach and Bret Pettichord, <i>Lessons Learned in Software Testing</i> (2002).",
             "ISTQB, <i>Foundation Level Syllabus</i>: defect management.",
             "UK Government, <i>Model Services Contract</i>: testing and defects."],
)

# ------------------------------------------------------------------ 11 When Do We Quote the Contract?
qc_problem = Doodle(760, 240, "Doodle of a demand from Gareth Pound's Network Assets, through Kofi, on 8 August 2028: migrate ten years of meter-reading history for wave 1 customers. The contract excludes history beyond 24 months, exclusion X-07. Gareth has already emailed Rupert: Lodestar is refusing to migrate essential data.",
                    "“Migrate ten years of meter readings.” The contract says 24 months. Gareth has emailed Rupert.", exact=True)
qc_problem.box(24, 40, 300, 120, "Gareth's ask", "pink", sub="10 years of readings", size=21, subsize=16)
qc_problem.box(436, 40, 300, 120, "X-07", "y", sub="history beyond 24 months excluded", size=21, subsize=15)
qc_problem.note(380, 200, "cc: Rupert · “Lodestar refuses essential data”", "red", size=18)

qc_how = Doodle(760, 320, "Quoting the contract, rarely and well. At the working group on 8 August, with Kofi and Gareth's deputy: acknowledge the need; read the clause aloud, calmly, exclusion X-07 and Schedule 2; offer a way to get it: an impact assessment within ten days, about 140,000 pounds, best done in wave 2; offer an interim: the ten years stay readable in MAVIS for all migrated customers. Gareth accepts the interim. The second time in fourteen months Ines has read a clause aloud.",
                "Acknowledge the need, read the clause calmly, offer a way to get it, and an interim.", exact=True)
for i, (h, sub, fill) in enumerate([("acknowledge", "the need is real", "green"), ("read it aloud", "X-07, calmly", "y"), ("offer a way", "CR ≈ £140k, wave 2", "blue"), ("interim", "readable in MAVIS", "paper")]):
    qc_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=14)
qc_how.box(14, 170, 732, 60, "second time in fourteen months", "pink", size=19)
qc_how.note(380, 280, "quote the contract to solve a problem, never to win one", "pen", size=18)

QUOTING = dict(
    slug="quoting-the-contract", date=date(2028, 8, 8), meta=on_site(date(2028, 8, 8)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. using the contract in a disagreement",
    tldr="The contract is your safety net, not your argument. Read it aloud <b>rarely</b>: only when the relationship can't settle something on its own. When you do, <b>acknowledge the need</b> first, read the clause <b>calmly</b>, and immediately <b>offer a way</b> to get what they want (a change, a later wave) and, if possible, an <b>interim</b>. A clause read to win an argument loses the relationship; a clause read to solve a problem keeps both.",
    chips=[("Family", "holding the line"), ("Lives in", "Appendix C, X-07 · change register"), ("Pairs with", "change control (vol. 2), mapping the client (vol. 2)")],
    problem_side="The Grid, 8 August 2028",
    problem="""  <p class="lead">Six weeks before wave 1, Kofi brings a request from <b>Gareth Pound</b>: migrate <b>ten years of meter-reading history</b> for every wave 1 customer. Network Assets' analysts use it for load forecasting.</p>
  <ul>
    <li>The contract excludes history older than <b>24 months</b>: exclusion <b>X-07</b>, listed in the bid in March 2027.</li>
    <li>Gareth has already emailed Rupert: <i>“Lodestar is refusing to migrate essential data.”</i></li>
    <li>Ten years of readings for 380,000 customers is about <b>40 million rows</b>. <span class="hl-pink">Six weeks before the night.</span></li>
  </ul>""",
    problem_figs=[qc_problem],
    sides=dict(client=("Gareth and Kofi", "<p>For Network Assets, meter history is how they plan the grid: which streets will overload in a cold January. Losing easy access to it feels like Lodestar breaking their work. Gareth wanted Lodestar in his own programme in 2027; this is also about that.</p>", "You're taking away data we need."),
                vendor=("Ines", "<p>Gareth's need is real. The exclusion is also real, and was in the bid. Doing it now would put wave 1 at risk; refusing it bluntly hands Gareth the story he's already telling Rupert. Ines needs to use the contract without using it as a weapon.</p>", "Read the clause, then solve the problem.")),
    sides_after="Quoting the contract is like pulling a handbrake: useful when you need it, and noticed by everyone in the car.",
    analogy_side="the landlord and the lease",
    analogy="""  <p>A tenant asks the landlord to repaint the whole flat. The lease says the landlord repaints every five years; it's been three. A good landlord doesn't wave the lease. He says: <b>“I understand, it's looking tired. The lease says five years, so it's due in 2030. I could do the living room now at cost, and the rest then. Meanwhile, here are the paint codes if you want to touch up.”</b></p>""",
    map=[("Repaint the whole flat", "Migrate ten years of meter history"),
         ("Every five years", "Exclusion X-07: 24 months"),
         ("“I understand, it's looking tired”", "Acknowledging the need"),
         ("The living room now, at cost", "A change request, best in wave 2"),
         ("Here are the paint codes", "The interim: history readable in MAVIS")],
    how_side="acknowledge, read calmly, offer a way, an interim",
    how="""  <p>Ines asks for the request to come to the <b>data working group</b> the same day, with Kofi and Gareth's deputy, rather than answering Gareth's email.</p>
  <ul>
    <li><b>Acknowledge the need.</b> “Load forecasting depends on this history. That's a real need, and Lodestar shouldn't make it harder.”</li>
    <li><b>Read the clause, calmly.</b> “When we bid, we listed X-07: meter history older than 24 months isn't migrated. It's in Appendix C. Wave 1 migrates the last 24 months.”</li>
    <li><b>Offer a way.</b> “We can assess migrating the full history as a change, within ten days. Our rough figure is about <b>£140k</b>, and it's safer in wave 2 than six weeks before wave 1.”</li>
    <li><b>Offer an interim.</b> “Until then, all ten years stay <b>readable in MAVIS</b> for migrated customers: Network Assets' reports keep working.”</li>
  </ul>
  <p>Gareth's deputy takes the interim back. Gareth accepts it by email, and replies to his own message to Rupert: “Resolved with Lodestar.” The change request is assessed and scheduled for wave 2. It's the <b>second time in fourteen months</b> Ines has read a clause aloud; the first was “absorb”, in June 2027.</p>""",
    how_figs=[qc_how],
    steps=[("Try everything else first", "Most issues settle without a clause."),
           ("Move it to the right room", "A working group, not an email thread."),
           ("Acknowledge the need", "Before any clause."),
           ("Read the clause calmly, once", "Where it is, what it says."),
           ("Offer a way to get it", "A change, a later phase, a price."),
           ("Offer an interim if you can", "Something that helps now.")],
    vocab=[("Exclusion", "Work explicitly outside the contract's scope."),
           ("Scope boundary", "The line between what's in and out."),
           ("Interim measure", "A temporary solution until the proper one is delivered."),
           ("Contractual leverage", "Using the contract's terms to influence an outcome."),
           ("Relationship capital", "Goodwill built up and spent in disagreements."),
           ("Escalation by email", "Copying senior people to put pressure on a decision.")],
    code=dict(file="delivery/lodestar/working-groups/data-2028-08-08.md", note="data working group · Tue 8 Aug 2028", src="""
DATA WORKING GROUP · 8 Aug 2028 · Kofi, Network Assets (deputy), Bilal, Ines

request     migrate 10 years of meter readings for wave 1 (≈ 40m rows) · Gareth
need        load forecasting by Network Assets (acknowledged)
contract    Appendix C, X-07: meter history older than 24 months not migrated
            (in the bid, Mar 2027; Schedule 2 §5.6)
offered     CR-019: full history migration, impact assessment by 22 Aug,
            rough ≈ £140k, recommended for wave 2
interim     all MAVIS meter history stays readable for migrated customers
            (read-only, via the back-feed reports Network Assets already use)
outcome     interim accepted (Gareth, email 16:40); CR-019 → wave 2 planning
"""),
    contract=dict(side="the exclusion, quoted", doc="Lodestar SOW · Appendix C, X-07", date="signed 30 June 2027", stamp="quoted (2nd time)",
                  clauses=[("X-07", "Meter-reading history older than 24 months is not migrated. MAVIS history remains available read-only.", "the second sentence was the interim, written in 2027. we just had to read it out."),
                           ("3.5", "Exclusions are outside the Services and may be added only by Change Request.", "and we offered one.")],
                  plain="a good exclusion often contains its own interim (“remains available read-only”). Read the whole clause, and lead with what it allows, not just what it excludes."),
    health=dict(now="a",
                g=("trust is high", ["Rarely needed.", "A conversation settles it.", "Offer the change."]),
                a=("a powerful stakeholder escalating", ["Right room, calm clause, a way and an interim.", "Reply to the escalation with the outcome.", "Credit their need."]),
                r=("repeated demands outside scope", ["Quote, offer, record each time.", "Escalate patterns via the ladder.", "Never refuse without offering a route."])),
    pressure=dict(level=3, title="the clause", cost="an email to Rupert · six weeks to the night",
                  items=["Being accused to Rupert stings. Answering the substance in the right room makes the accusation disappear on its own.", "Reading a clause aloud feels confrontational. Saying the need first takes most of that away."]),
    baseline="Each line compares <b>refusing by email, or agreeing to 40 million rows six weeks before go-live</b> with <b>acknowledging the need, quoting X-07 calmly, offering a change and an interim</b>.",
    ratings=[(3, 4, "Network Assets keeps its reports and gets a route."),
             (3, 4, "No last-minute data migration."),
             (2, 4, "£140k of work priced, not given away."),
             (3, 5, "X-07 confirmed in front of the client."),
             (3, 4, "Wave 1's design isn't stretched at the last minute."),
             (2, 4, "40 million extra rows kept off the critical path."),
             (3, 4, "Working group minutes, CR-019."),
             (3, 4, "Settled in a day."),
             (4, 4, "Nothing new to run.")],
    pitfalls=[("Quoting first", "The need is ignored; they escalate.", "acknowledge the need first."),
              ("Quoting often", "Every conversation becomes legal.", "rarely: twice in fourteen months."),
              ("Quoting without an offer", "A wall, not a door.", "a change, a later phase, a price."),
              ("Answering the escalation email", "The thread grows.", "solve it in the right room, then reply with the outcome."),
              ("Giving in to pressure", "Wave 1 at risk.", "protect the critical path.")],
    grimoire=[(1, "empire-builder", "The Empire Builder", "is Gareth, from inside: the colleague who collects headcount, and data, like dragon gold.")],
    use=["A request is clearly outside the agreed scope.", "Pressure is applied through senior people.", "Doing it would put a milestone at risk."],
    skip=["A small request the change pool can handle: use the pool, not the clause."],
    related=["<b>How Do We Change the Deal Without a War?</b> (vol. 2)", "<b>What Are We Assuming?</b> (vol. 1)", "<b>Is It a Defect or a Change?</b> (previous note)", "<b>How Do We Protect the Margin?</b> (next note)"],
    quiz=[("When should you read the contract aloud?", "Rarely, when the relationship can't settle it on its own."),
          ("What comes before the clause?", "Acknowledging the other side's need."),
          ("What did X-07 say, in full?", "History older than 24 months isn't migrated; MAVIS history remains available read-only."),
          ("What was offered?", "A change request (about £140k, best in wave 2) and an interim: history readable in MAVIS."),
          ("Why move the conversation to the working group?", "Email threads with senior people copied grow; a working group solves.")],
    quiz_sit=[("Rupert replies to Gareth's email asking Ines “to explain the refusal”. What does Ines send?", "A short reply: it's resolved; Network Assets keeps full access in MAVIS; a change request for full migration is being assessed for wave 2; minutes attached. No defence, no clause quotes.")],
    try_it="Think of a request outside your agreed scope. Write four sentences: the need, the clause, the way to get it, and an interim. How does it sound read aloud?",
    remember="The contract is <span class=\"hl\">a safety net, not an argument</span>. Need first, clause second, <span class=\"hl\">a way and an interim</span> third.",
    late=dict(when="Tue 8 August 2028 · 20:30 · hotel near The Grid",
              lines=["Gareth emailed Rupert that we were “refusing essential data”. By 16:40 he'd emailed Rupert again: resolved.",
                     "X-07 had the interim in it all along: “remains available read-only”. Past me, writing in March 2027, was kind to present me.",
                     "Second clause read aloud in fourteen months. I hope it's the last for a while."]),
    sources=["Roger Fisher and William Ury, <i>Getting to Yes</i> (1981).",
             "Ian Macneil, <i>The New Social Contract</i> (1980): relational contracting.",
             "World Commerce &amp; Contracting, research on relational contracts."],
)

# ------------------------------------------------------------------ 12 How Do We Protect the Margin?
mg_problem = Doodle(760, 240, "Doodle of the margin forecast on 18 August 2028. Bid at P80: 19 per cent. After CR-007 and the re-plan: 11 per cent. Latest forecast: 9 per cent, below Wrenfield's 15 per cent floor. Graham's suggestion from Leeds: drop rehearsal 3 and half the performance testing; saves about 60,000 pounds.",
                    "19 % at bid, 9 % now, floor 15 %. Graham: “drop rehearsal 3”.", exact=True)
mg_problem.line("M40 200 L240 80 L440 130 L640 150", color="red")
for x, y, t in [(40, 200, ""), (240, 80, "19 % bid"), (440, 130, "11 % after CR"), (640, 150, "9 % now")]:
    if t:
        mg_problem.note(x, y - 16 if x == 240 else y + 28, t, "pen", size=17)
mg_problem.line("M30 100 H730", dash=True)
mg_problem.note(700, 90, "floor 15 %", "red", size=16)
mg_problem.note(380, 230, "“drop rehearsal 3, halve the perf test: −£60k”", "red", size=18)

mg_how = Doodle(760, 330, "Protecting margin without cutting corners. A line drawn first: never cut testing, rehearsals, security or honesty. Then the levers that are fair: bill the side-door work through the change pool, as agreed; roll two senior people off earlier after cutover, planned with Elaine; reuse wave 1 tooling for the phase 2 bid estimate; renegotiate invoice timing, not price. Forecast up to 10 per cent. Below the floor, and said so to Graham in writing.",
                "Draw the line first, then pull the fair levers. Below the floor is a fact, not a reason to cut quality.", exact=True)
mg_how.box(14, 14, 732, 50, "never cut: testing · rehearsals · security · honesty", "pink", size=18)
for i, (h, sub) in enumerate([("change pool", "side-door work billed"), ("roll-off plan", "2 seniors earlier"), ("reuse", "tooling for phase 2"), ("invoice timing", "not price")]):
    mg_how.box(14 + i * 186, 84, 174, 100, h, "green", sub=sub, size=18, subsize=13)
mg_how.box(14, 210, 360, 70, "forecast 9 % → 10 %", "y", size=19)
mg_how.box(386, 210, 360, 70, "below floor: told Graham", "paper", sub="in writing, with why", size=18, subsize=14)
mg_how.note(380, 312, "a cheaper night that fails costs more than any margin", "red", size=18)

MARGIN = dict(
    slug="protecting-margin", date=date(2028, 8, 18), meta=on_site(date(2028, 8, 18)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. protecting margin on a fixed-price project",
    tldr="On a fixed price, margin pressure arrives late and pushes towards the cheapest cut: testing. Draw the line <b>before</b> the pressure: <b>never cut testing, rehearsals, security or honesty</b>. Then protect the margin with fair levers: <b>bill agreed changes</b>, plan <b>roll-offs</b> with the client, <b>reuse</b> what you've built, adjust <b>timing</b> rather than price. If you're still below the floor, say so to your own firm, in writing. That's a business fact, not a reason to make the night riskier.",
    chips=[("Family", "holding the line"), ("Lives in", "internal/lodestar-margin-forecast.xlsx (Wrenfield only)"), ("Pairs with", "re-planning, the honest change request (vol. 3)")],
    problem_side="Wrenfield, Leeds, 18 August 2028",
    problem="""  <p class="lead">Callum's monthly margin forecast, presented at Wrenfield's board in Leeds on <b>Friday 18 August</b>: the bid's P80 margin was <b>19 %</b>; after CR-007 and the re-plan, <b>11 %</b>; latest forecast, <b>9 %</b>. Wrenfield's floor is <b>15 %</b>.</p>
  <ul>
    <li>Graham proposes two savings: <b>drop rehearsal 3</b> (26 August) and <b>halve the performance testing</b>. About <b>£60k</b>.</li>
    <li>Rehearsal 3 is the last full run before the night, and a go / no-go criterion.</li>
    <li><span class="hl-pink">Nobody at MetroVolt would know until 23 September.</span></li>
  </ul>""",
    problem_figs=[mg_problem],
    sides=dict(client=("MetroVolt (who isn't in the room)", "<p>MetroVolt is paying a fixed price for a tested, rehearsed migration. Elaine has never asked about Wrenfield's margin, and shouldn't need to. What she'd care about is that the risk she's carrying on 23 September doesn't quietly go up to fix it.</p>", "(not asked, and shouldn't have to be)"),
                vendor=("Graham and Ines", "<p>Graham's worry is real: 9 % on Wrenfield's biggest contract is a bad year, and a 15 % floor exists for a reason. But the cut he proposes moves Wrenfield's financial risk onto 380,000 customers' accounts. Ines needs to protect the margin without touching the night.</p>", "Protect the margin. Not by making the night more dangerous.")),
    sides_after="The cheapest corner to cut is always the one that only shows up later. That's exactly why it has to be ruled out in advance.",
    analogy_side="the airline's fuel",
    analogy="""  <p>An airline under cost pressure can sell more seats, renegotiate airport fees, fly older planes longer, schedule crews better. It doesn't carry less <b>reserve fuel</b> than the rules require. The fuel isn't where margin comes from; it's what lets the plane land when the weather turns.</p>""",
    map=[("Reserve fuel", "Rehearsal 3 and the performance test"),
         ("Selling more seats", "Billing agreed changes through the pool"),
         ("Better crew scheduling", "Planned roll-offs after cutover"),
         ("Renegotiating airport fees", "Invoice timing, not price"),
         ("When the weather turns", "Wave 1 night, if something unforeseen happens")],
    how_side="the line first, then fair levers, then the truth to your own firm",
    how="""  <p><b>The line, first.</b> Ines writes it at the top of her response to Graham: <b>“We won't cut testing, rehearsals, security, or anything we've told MetroVolt we're doing.”</b> She points to Schedule 4: rehearsal 3 is a condition of wave 1 (clause 2.2); dropping it would be a contract breach as well as a risk.</p>
  <p><b>Fair levers.</b> Four: <b>bill the agreed side-door work</b> properly through the change pool (it had been under-invoiced: <b>+£31k</b>); <b>roll two senior people off</b> two weeks after cutover instead of six, agreed with Elaine as part of hypercare planning (<b>+£38k</b>); <b>reuse</b> wave 1's estimating model and tooling for the phase 2 bid instead of building new (saves bid cost later); and ask MetroVolt to pay M4 in two parts (cash flow, not margin). Forecast: <b>10 %</b> (the two levers add about £69k on £5.7m of revenue).</p>
  <p><b>The truth to your own firm.</b> 10 % is still below the floor. Ines says so in writing, with why (CR-007's agreed price was £400k less than the work it covered, by choice, to keep MetroVolt's trust) and what it buys (a strong position for phase 2). Graham reads it twice and approves. Rehearsal 3 happens on 26 August.</p>""",
    how_figs=[mg_how],
    steps=[("Write the line before the pressure", "What you will never cut."),
           ("Check the contract", "Some cuts are breaches too."),
           ("Bill what's agreed", "Change pool work, invoiced properly."),
           ("Plan roll-offs with the client", "Fewer people after cutover, openly."),
           ("Reuse what you've built", "For the next phase or bid."),
           ("Tell your firm the truth", "Below the floor, why, and what it buys.")],
    vocab=[("Margin", "Price minus cost, as a share of price."),
           ("Margin floor", "The lowest margin a firm will accept."),
           ("Roll-off", "Moving people off a project as their work ends."),
           ("Revenue leakage", "Work done but not billed."),
           ("Quality cut", "Saving cost by doing less testing or checking; risk moves to the client."),
           ("Forecast at completion", "The expected final cost and margin, updated regularly.")],
    code=dict(file="internal/lodestar-margin-response.md", note="Ines to Graham · Fri 18 Aug 2028 (Wrenfield only)", src="""
LODESTAR MARGIN · response to the 18 Aug forecast (9 %)

the line   we won't cut testing, rehearsals, security, or anything MetroVolt has
           been told we're doing. (Rehearsal 3 = Sch. 4 §2.2 condition for wave 1.)
levers     1 change-pool work invoiced properly (CN-010..018, 4 more)   +£31,000
           2 two seniors roll off 2 weeks after cutover, not 6 (agreed with
             Elaine in the hypercare plan)                               +£38,000
           3 reuse estimate model + tooling for the phase 2 bid          (bid cost)
           4 M4 paid in two parts (cash flow, not margin)
forecast   9 % → 10 % (floor 15 %)
why below  CR-007 agreed at £700k for ≈ £1.1m of work, by choice, to keep trust
what for   phase 2 (waves 2–4, ≈ £9m) bid in 2029 from a position of credibility
"""),
    contract=dict(side="why the cut wasn't even allowed", doc="Lodestar SOW · Schedule 4, §2.2 and §5.3 (Sch. 2)", date="baseline v2.0", stamp="not negotiable",
                  clauses=[("Sch. 4, 2.2", "Wave 1 shall not proceed unless the final dress rehearsal meets the M4 criteria.", "no rehearsal 3, no wave 1. Graham hadn't read it."),
                           ("Sch. 2, 5.3", "Migrated customers' bills shall be calculated identically to MAVIS, except where MetroVolt instructs a change.", "halving the performance test risks the 02:10 file. same problem.")],
                  plain="many cost cuts that look internal are actually commitments to the client. Check the contract before discussing them; it often settles the argument for you."),
    health=dict(now="g",
                g=("good margin, trusted", ["Keep the line written anyway.", "Bill what's agreed.", "Plan roll-offs early."]),
                a=("margin squeezed, client happy", ["Fair levers only.", "Tell your firm the truth.", "Protect what makes the client happy."]),
                r=("below floor, pressure to cut", ["The line, in writing, signed.", "Escalate inside your firm, not to the client.", "If it can't be fixed fairly, renegotiate openly."])),
    pressure=dict(level=4, title="your own firm", cost="a 9 % forecast · a managing director's worry",
                  items=["Arguing with your own managing director is harder than arguing with a client. Bring the contract clause; it isn't your opinion.", "Graham isn't a villain. He has a payroll. Give him levers, not just a refusal."]),
    baseline="Each line compares <b>dropping rehearsal 3 and halving performance tests</b> with <b>a written line, fair levers and the truth to the board</b>.",
    ratings=[(3, 4, "MetroVolt's risk doesn't quietly rise."),
             (2, 3, "Senior people roll off sooner; planned."),
             (1, 3, "9 % → 10 %: better, not yet at the floor."),
             (3, 4, "Change-pool work properly invoiced."),
             (3, 5, "Rehearsal and testing intact."),
             (2, 5, "The night keeps its safety margin."),
             (3, 4, "Decision and reasons in writing."),
             (3, 3, "A week of rework on the plan."),
             (3, 3, "A forecast to keep.")],
    pitfalls=[("Cutting testing", "Risk moves to the client, unseen.", "a written line, before the pressure."),
              ("Hiding the margin problem", "Your firm finds out at year end.", "tell it, with why."),
              ("Leaking revenue", "Agreed work never invoiced.", "bill the pool properly."),
              ("Surprise roll-offs", "The client feels abandoned.", "plan them with the client."),
              ("Making it the client's problem", "Asking them to pay for your miss.", "fix it inside, or renegotiate openly.")],
    grimoire=[(5, "more-with-less", "The Curse of “More with Less”", "is the inside version: re-scoping when resources vanish, without pretending nothing changed.")],
    use=["Fixed-price work under cost pressure.", "Late in delivery, when testing is the last big cost.", "When someone proposes a cut the client wouldn't see."],
    skip=["Never skip the line; skip the levers if the margin is healthy."],
    related=["<b>How Do We Re-plan Without Lying?</b> (this volume)", "<b>How Do We Ask for More Money Honestly?</b> (vol. 3)", "<b>Fixed Price, or Time and Materials?</b> (vol. 1)", "<b>Is the Money Buying Progress?</b> (Sanne, vol. 4)"],
    quiz=[("What's on the line Ines wrote first?", "Never cut testing, rehearsals, security, or anything MetroVolt has been told."),
          ("Why couldn't rehearsal 3 be dropped anyway?", "Schedule 4 §2.2 makes it a condition of wave 1."),
          ("What were the four fair levers?", "Bill change-pool work, plan earlier roll-offs, reuse tooling, adjust invoice timing."),
          ("What did the forecast become?", "10 %, still below the 15 % floor."),
          ("Why tell Graham it was still below the floor?", "It's a business fact; hiding it would surprise the firm later.")],
    quiz_sit=[("Graham says: “Fine, keep rehearsal 3, but don't run the Welsh-language tests, nobody will notice.” What do you say?", "No: the Welsh-language behaviour is part of Schedule 2 and the golden master; skipping it is the same kind of cut. Offer to look for another lever instead.")],
    try_it="Write your own line: three things you'd never cut on your current project, whatever the cost pressure. Then list three fair levers you could pull instead.",
    remember="Draw <span class=\"hl\">the line before the pressure</span>. Margin comes from fair levers, never from <span class=\"hl\">the reserve fuel</span>.",
    late=dict(when="Fri 18 August 2028 · 23:30 · the train home from Leeds",
              lines=["Graham wanted to drop rehearsal 3. It's in Schedule 4. He hadn't read it. Neither had I, for months.",
                     "10 %. Still below the floor. I wrote down why: we chose to keep Elaine's trust in February. I'd choose it again.",
                     "Rehearsal 3 is next Saturday. Thank goodness."]),
    sources=["David Maister, <i>Managing the Professional Service Firm</i> (1993): profitability.",
             "Project Management Institute, <i>PMBOK Guide</i>: cost forecasting.",
             "Diane Vaughan, <i>The Challenger Launch Decision</i> (1996): the normalisation of deviance."],
)

NOTES = [REPLAN, TEST_ENVS, DEFECT_TRIAGE, QUOTING, MARGIN]
