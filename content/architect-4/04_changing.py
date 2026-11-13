# Series 2 · The Solution Architect's Notebook · Vol. 4 · Changing the landscape.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 13 Strangler Fig Migration
sf_problem = Doodle(760, 280, "Doodle of the first warehouse migration plan in March 2027: a big-bang weekend. All five stores switch from StockPilot to WMS B on one Saturday night in July. If anything goes wrong, every store opens on Sunday without trustworthy stock, and there's no way back without losing a day's movements.",
                    "Five stores, one Saturday night, no way back: the big-bang plan.")
for i, t in enumerate(["Noord", "Zuid", "Rotterdam", "Utrecht", "The Hague"]):
    sf_problem.box(20 + i * 148, 40, 132, 50, t, "paper", size=15)
    sf_problem.arrow(86 + i * 148, 94, 380, 150, color="red", dash=True)
sf_problem.box(220, 154, 320, 64, "one Saturday night", "pink", sub="all at once, no way back", stroke="red", subsize=14)
sf_problem.note(380, 262, "if it fails, every store opens blind", "red")

sf_analogy = Doodle(760, 250, "Doodle of a road bridge being replaced lane by lane. Traffic keeps flowing on the old lanes while one new lane is built and opened; then the next. Each step is small, traffic never stops, and if a new lane has a problem, cars go back to an old one.",
                     "Replacing a bridge lane by lane: traffic keeps flowing, and any lane can go back to the old one.")
for i, (t, f) in enumerate([("new lane", "green"), ("new lane", "green"), ("old lane", "paper"), ("old lane", "paper")]):
    sf_analogy.box(60, 30 + i * 44, 400, 36, t, f, size=15, rx=4)
sf_analogy.arrow(480, 70, 560, 70)
sf_analogy.note(640, 74, "traffic flows", "pen", size=18)
sf_analogy.note(380, 230, "one lane at a time, never closed", "pen")

sf_how = Doodle(760, 380, "How Larder moved its warehouses, store by store, from April to September 2027. A router in the Stock module sends each store's calls to StockPilot or WMS B, by a setting per store. Each move: a week in shadow mode comparing both systems, then the switch, then two weeks with StockPilot read-only as a way back. Zuid moved 19 April, Noord 24 May, The Hague opened on WMS B 14 June, Rotterdam 21 June, Utrecht 26 July. StockPilot switched off 15 September.",
                 "A router per store, shadow mode, switch, a way back. Five moves, then the old system switched off.")
sf_how.box(250, 14, 260, 70, "Stock module router", "y", sub="setting per store", subsize=14)
sf_how.box(30, 120, 260, 60, "StockPilot", "paper", sub="shrinking", subsize=14)
sf_how.box(470, 120, 260, 60, "WMS B", "green", sub="growing", subsize=14)
sf_how.arrow(330, 88, 200, 116, dash=True)
sf_how.arrow(430, 88, 560, 116)
for i, (store, date, f) in enumerate([("Zuid", "19 Apr", "green"), ("Noord", "24 May", "green"), ("The Hague", "14 Jun (new)", "green"), ("Rotterdam", "21 Jun", "green"), ("Utrecht", "26 Jul", "green")]):
    x = 14 + i * 148
    sf_how.box(x, 210, 136, 64, store, f, sub=date, size=15, subsize=13)
sf_how.note(380, 310, "each move: 1 week shadow → switch → 2 weeks read-only way back", "pen", size=15)
sf_how.note(380, 340, "StockPilot off: 15 September 2027", "green", size=17)

STRANGLER = dict(
    slug="strangler-fig",
    kicker="a.k.a. “a bridge, lane by lane”",
    tldr="Replacing a system in one big weekend bets everything on one night with no way back. A <b>strangler fig migration</b> replaces it <b>piece by piece</b> while it keeps running: put a <b>router</b> in front that sends each piece (a store, a feature, a customer group) to the old or the new system; move one piece at a time, with a <b>shadow period</b> and a <b>way back</b>; and when nothing is left on the old system, <b>switch it off</b>.",
    chips=[("Family", "changing the landscape"), ("Origin", "Martin Fowler, “StranglerFigApplication” (2004)"), ("Lives in", "a router in the owning module, a migration plan with dates"), ("Pairs with", "anti-corruption layer, transition architectures, exit plans")],
    problem_side="Larder, 29 March 2027",
    problem="""  <p class="lead">The first plan for the warehouse move (ADR 0016) is a <b>big bang</b>: all five stores switch from StockPilot to WMS B on <b>one Saturday night in July</b>. It looks efficient. But if anything goes wrong, every store opens on Sunday <span class="hl-pink">without trustworthy stock</span>, and going back means losing a day of movements. Joost says what everyone is thinking: “not on my Sundays”.</p>
  <ul>
    <li>Big-bang migrations concentrate all the risk in one moment.</li>
    <li>Problems show up everywhere at once, at the worst time.</li>
    <li>There's no small step to learn from, and no easy way back.</li>
  </ul>""",
    problem_figs=[sf_problem],
    analogy_side="the bridge, lane by lane",
    analogy="""  <p>Road engineers replace a busy bridge <b>lane by lane</b>. Traffic keeps flowing on the old lanes while one new lane is built and opened; then the next. Each step is small, the bridge never closes, and if a new lane has a problem, cars <b>go back to an old one</b> for a while. One day the last old lane is closed for good.</p>""",
    analogy_figs=[sf_analogy],
    map=[("The bridge", "Stock management for all stores"),
         ("A lane", "One store"),
         ("Traffic switching lanes", "The router sending a store to WMS B"),
         ("Going back to an old lane", "StockPilot read-only for two weeks after each move"),
         ("Closing the last old lane", "StockPilot off on 15 September")],
    how_side="router, one piece at a time, a way back",
    how="""  <p>Because the Stock module already held the only adapter (ADR 0005, 0018), adding a <b>router</b> was small: a setting per store chooses StockPilot or WMS B. Each move had a week of <b>shadow mode</b> (both systems updated, stock compared), then the switch, then two weeks with StockPilot <b>read-only</b> as a way back. <b>Zuid</b> went first in April (smallest), <b>The Hague</b> opened directly on WMS B in June, <b>Utrecht</b> moved last in July. StockPilot was switched off on <b>15 September</b>.</p>""",
    how_figs=[sf_how],
    steps=[("Find the seam", "Where calls to the old system pass through one place (an adapter)."),
           ("Put a router there", "Per store, feature or customer group: old or new."),
           ("Pick the first piece", "Small and low-risk, but real."),
           ("Shadow, compare, switch", "Run both, compare results, then switch the piece."),
           ("Keep a way back", "The old system read-only for a set period."),
           ("Repeat, then switch off", "When nothing routes to the old system, turn it off and delete the router branch.")],
    vocab=[("Strangler fig", "Replacing a system gradually until the old one can be removed."),
           ("Router", "The switch deciding old or new per piece."),
           ("Shadow mode", "Running the new system alongside, comparing, without relying on it."),
           ("Seam", "A place where you can redirect calls."),
           ("Way back", "A tested route to return to the old system."),
           ("Big bang", "Switching everything at once.")],
    code=dict(file="docs/migrations/stockpilot-to-wms-b.md", note="migration plan and log, 2027", plain=True, src="""
# StockPilot → WMS B · strangler migration (ADR 0016, 0018)      owner: Ben

Router    core/stock/router.py · setting stores.<id>.wms = stockpilot | wms_b
Per store 1 week shadow (both updated, nightly stock comparison, ≤ 0.5 % diff)
          → switch → 2 weeks StockPilot read-only (way back) → done

| Store      | Shadow from | Switched   | Diff in shadow | Notes                         |
|------------|-------------|------------|----------------|-------------------------------|
| Zuid       | 12 Apr      | 19 Apr     | 0.3 %          | first; units of measure fixed |
| Noord      | 17 May      | 24 May     | 0.2 %          |                               |
| The Hague  | —           | 14 Jun     | —              | opened on WMS B               |
| Rotterdam  | 14 Jun      | 21 Jun     | 0.4 %          |                               |
| Utrecht    | 19 Jul      | 26 Jul     | 0.2 %          | opened on StockPilot in April |
StockPilot switched off 15 Sep 2027 (bridge contract ended 30 Sep). Router branch deleted.
"""),
    tools="tools: a router or feature flag in the owning module; comparison jobs for shadow mode; the anti-corruption layer as the seam; dashboards per migrated piece.",
    gains=["<b>Small risk per step</b>: one store at a time.",
           "<b>Learning early</b>: Zuid found the units problem.",
           "<b>A way back</b> after every move.",
           "<b>The business keeps running</b>, every Sunday.",
           "<b>Progress is visible</b>, store by store."],
    losses=["<b>Longer overall</b>: months instead of a weekend.",
            "<b>Two systems at once</b>, with two bills for a while.",
            "<b>Router and shadow code</b> to build and delete.",
            "<b>Easy to stall</b> with the last pieces."],
    baseline="Each line compares <b>a big-bang weekend switching every store at once</b> to <b>a router per store, shadow mode, one store at a time with a way back, then switching the old system off</b>.",
    ratings=[(2, 4, "The plan and progress are clear per store."),
             (2, 5, "Joost agreed each store's date."),
             (3, 3, "Each move is a small, quick decision."),
             (1, 5, "One store at risk at a time, with a way back."),
             (2, 5, "Any store could go back for two weeks."),
             (3, 4, "A log of every move and its comparison."),
             (2, 3, "Two systems paid for during the move."),
             (3, 3, "Shadow jobs and a router to run."),
             (3, 4, "Ben's team ran each move without Ana.")],
    pitfalls=[("No seam", "Calls to the old system everywhere.", "build the single adapter first (ACL)."),
              ("No way back", "Switch and hope.", "keep the old system read-only for a set time."),
              ("The last 10 % stalls", "One store left on StockPilot for a year.", "a date for switching off, in the contract too."),
              ("Router left behind", "Dead branches for years.", "delete the router branch when done.")],
    use=["Replacing a vendor, platform or legacy system.",
         "Migrations where downtime is unacceptable.",
         "When the work can be split by store, feature or customer.",
         "Extracting services from a monolith."],
    skip=["Tiny systems that can be swapped in an hour with a rollback.",
          "When the old and new can't run side by side at all."],
    related=["<b>Anti-corruption layer</b> (this volume)", "<b>Transition architectures</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)", "<b>Strangler fig</b> (patterns, Vol. 1)"],
    quiz=[("What does the router do?", "Sends each piece (here, each store) to the old or the new system."),
          ("What's shadow mode for?", "Running both systems and comparing results before relying on the new one."),
          ("What's the way back?", "The old system kept read-only for a set period after each move."),
          ("When is the migration done?", "When nothing routes to the old system and it's switched off.")],
    try_it="For a system you'd like to replace, find the seam: the one place calls pass through. If there isn't one, that's the first job. Then list the pieces you could move one at a time, and pick the smallest real one to go first.",
    remember="Replace the bridge <span class=\"hl\">lane by lane</span>. Keep a <span class=\"hl\">way back</span>.",
    sources=["Martin Fowler, “StranglerFigApplication” (martinfowler.com, 2004, updated 2024).",
             "Sam Newman, <i>Monolith to Microservices</i> (2019).",
             "Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004), on seams.",
             "Microsoft Azure Architecture Center, “Strangler Fig pattern”."],
)

# ------------------------------------------------------------------ 14 Transition Architectures
ta_problem = Doodle(760, 280, "Doodle of an August 2027 clean-up. While planning the end of the warehouse move, Ana finds three temporary bridges from the 2026 Dispatch extraction still running: the old courier cron as a fallback, a database view Dispatch was meant to stop reading, and a nightly copy job. Nobody remembered they were temporary.",
                    "Three “temporary” bridges from the 2026 Dispatch move, still running a year later.")
for i, (t, s) in enumerate([("old courier cron", "the fallback"), ("database view", "meant to go"), ("nightly copy job", "for a report")]):
    ta_problem.box(20 + i * 250, 50, 220, 90, t, "pink", sub=s, stroke="red")
ta_problem.note(380, 200, "temporary, with no end date, is permanent", "red", size=19)

ta_analogy = Doodle(760, 250, "Doodle of a building renovation with scaffolding. The scaffolding is needed in between, so it's on the plan with a date to come down and a person responsible. Without that, it stays up for years, rusting.",
                     "Scaffolding belongs on the plan, with a date to come down, or it stays up for years.")
ta_analogy.icon("bricks", 40, 60, 1.4)
ta_analogy.box(170, 50, 260, 100, "scaffolding", "y", sub="needed in between")
ta_analogy.box(460, 50, 280, 100, "on the plan", "green", sub="down by 30 Sep · Jan's job")
ta_analogy.note(450, 210, "temporary parts need end dates", "pen")

ta_how = Doodle(760, 360, "The warehouse move's transition states, 16 August 2027. State A, March: StockPilot only. State B, April to September: both systems, the router per store, and three temporary bridges: shadow comparison jobs, finance's nightly files from both systems, and StockPilot kept read-only as a way back. State C, from 15 September: WMS B only. Each temporary bridge has an owner and an end date; state C isn't reached until they're all removed.",
                 "Name each in-between state, list its temporary bridges with owners and end dates, and don't call it done until they're gone.")
for i, (t, s, f) in enumerate([("A · March", "StockPilot only", "paper"), ("B · Apr–Sep", "both + router", "y"), ("C · 15 Sep", "WMS B only", "green")]):
    x = 14 + i * 248
    ta_how.box(x, 20, 236, 80, t, f, sub=s)
    if i < 2:
        ta_how.arrow(x + 238, 60, x + 246, 60)
ta_how.box(14, 130, 732, 140, None, "paper", dash=True)
ta_how.head(380, 160, "temporary bridges in B (owner · end)", size=16)
for i, t in enumerate(["shadow comparison jobs · Ben · 30 Sep", "finance files from both systems · Cho · 30 Sep", "StockPilot read-only way back · Ben · 15 Sep"]):
    ta_how.text(380, 196 + i * 26, t, size=14)
ta_how.note(380, 310, "C is reached when every bridge is gone", "green", size=17)
ta_how.note(380, 338, "+ the 3 old Dispatch bridges: removed by 30 Sep", "pen", size=15)

TRANSITIONS = dict(
    slug="transition-architectures",
    kicker="a.k.a. “scaffolding with a date”",
    tldr="Big changes pass through <b>in-between states</b> where old and new run side by side, held together by <b>temporary bridges</b>: comparison jobs, dual feeds, fallbacks, copies. Design those states on purpose. For each, write <b>what runs</b>, <b>which parts are temporary</b>, who <b>owns</b> each one and the <b>date it goes</b>. Don't call the change finished until every bridge is removed: temporary with no end date is permanent.",
    chips=[("Family", "changing the landscape"), ("Origin", "TOGAF transition architectures; migration planning practice"), ("Lives in", "the migration plan, one section per state"), ("Pairs with", "strangler fig, architecture roadmap, technical debt register")],
    problem_side="Larder, 16 August 2027",
    problem="""  <p class="lead">Planning the end of the warehouse move, Ana goes looking for anything else still connected to old paths, and finds <b>three temporary bridges from the 2026 Dispatch extraction</b> still running: the old courier <b>cron as a fallback</b>, a <b>database view</b> Dispatch was meant to stop reading, and a <b>nightly copy job</b> for one report. <span class="hl-pink">Nobody remembered they were temporary.</span> Each one still costs money, attention and risk.</p>
  <ul>
    <li>Migrations are planned as start and end; the middle is improvised.</li>
    <li>Temporary parts have no owner and no end date.</li>
    <li>“Done” is declared when the new system works, not when the old bits are gone.</li>
  </ul>""",
    problem_figs=[ta_problem],
    analogy_side="scaffolding with a date",
    analogy="""  <p>A renovation needs <b>scaffolding</b> in between: nobody can paint the top floor without it. On a good project, the scaffolding is <b>on the plan</b>, with a <b>date to come down</b> and a person responsible. On a bad one, it stays up for years, rusting, because the building “works” and nobody's job is to remove it.</p>""",
    analogy_figs=[ta_analogy],
    map=[("The building before", "State A: StockPilot only"),
         ("Scaffolding up", "State B: both systems, router, temporary bridges"),
         ("Scaffolding on the plan", "Each bridge with an owner and an end date"),
         ("Scaffolding down", "State C: WMS B only, bridges removed"),
         ("Rusting scaffolding", "The old Dispatch cron, a year later")],
    how_side="name the states, date the bridges",
    how="""  <p>Ana wrote the warehouse move as three <b>states</b>: A (StockPilot only), B (both, with the router) and C (WMS B only). For B she listed every <b>temporary bridge</b> (shadow comparison jobs, finance files from both systems, StockPilot read-only as a way back), each with an <b>owner and an end date</b>, and added them to the debt register. State C was declared only on <b>30 September</b>, when all were gone. The three old Dispatch bridges were removed in the same sweep.</p>""",
    how_figs=[ta_how],
    steps=[("Name the states", "Before, each in-between state, after: what runs in each."),
           ("List the temporary parts", "Comparison jobs, dual feeds, fallbacks, copies, flags, routers."),
           ("Give each an owner and an end date", "And put them in the technical debt register."),
           ("Define exit criteria per state", "What must be true to move to the next one."),
           ("Declare done only at the end", "When every temporary part is removed."),
           ("Sweep for old bridges", "Look for leftovers from earlier migrations.")],
    vocab=[("Transition architecture", "A planned in-between state of a change."),
           ("Temporary bridge", "Something that exists only to get through a transition."),
           ("Exit criteria", "What must be true to move to the next state."),
           ("Target state", "Where the change ends."),
           ("Baseline", "Where it starts."),
           ("Decommissioning", "Removing the old system and its bridges.")],
    code=dict(file="docs/migrations/stockpilot-to-wms-b.md", note="the transition states section", plain=True, src="""
## Transition states

A  (until Apr)      StockPilot only. Stock adapter → StockPilot.
B  (Apr → Sep)      Both. Router per store. Temporary bridges:
                      T1 shadow comparison jobs          Ben   end 30 Sep   (TD-14)
                      T2 finance files from both systems Cho   end 30 Sep   (TD-15)
                      T3 StockPilot read-only way back   Ben   end 15 Sep   (TD-16)
                    Exit: all stores on WMS B for 2 weeks, diff ≤ 0.5 %, finance signed off
C  (from 30 Sep)    WMS B only. Router branch deleted. StockPilot contract ended.
                    Declared on 30 Sep 2027, when T1–T3 were removed.

Sweep (Aug): leftovers from the 2026 Dispatch extraction, removed by 30 Sep:
  old courier cron fallback · Core DB view read by Dispatch · nightly copy for a report
"""),
    tools="tools: the migration plan in the repo; the technical debt register for temporary parts; architecture modelling tools (ArchiMate's plateau and gap concepts) for big programmes.",
    gains=["<b>The middle is designed</b>, not improvised.",
           "<b>Temporary parts get removed</b>, on dates.",
           "<b>Honest “done”</b>: the old bits are gone.",
           "<b>Lower running cost</b> after the change.",
           "<b>Old leftovers found</b> in the sweep."],
    losses=["<b>More planning</b> up front.",
            "<b>Removing bridges</b> takes real work at the end.",
            "<b>States can multiply</b> if over-planned.",
            "<b>The finish takes longer</b> than “it works”."],
    baseline="Each line compares <b>planning only the start and end of a change</b> to <b>named in-between states with dated, owned temporary bridges, and done only when they're gone</b>.",
    ratings=[(2, 4, "Everyone sees what runs in each state."),
             (3, 4, "Finance and operations know when their temporary flows end."),
             (3, 3, "Neutral."),
             (2, 4, "Temporary parts can't silently become permanent."),
             (2, 4, "Each state is a stable place to pause."),
             (2, 5, "Every bridge has an owner and an end date on record."),
             (2, 4, "Old bridges' running costs end."),
             (3, 3, "More planning, then clean-up work."),
             (3, 3, "Neutral.")],
    pitfalls=[("Undated scaffolding", "“Temporary” fallback, no end date.", "every temporary part gets an owner and a date."),
              ("Done too early", "Declared done when the new system works.", "done when the bridges are removed."),
              ("No exit criteria", "State B lasts forever.", "what must be true to move on."),
              ("Not looking back", "Leftovers from the last migration.", "sweep for old bridges at each new one.")],
    use=["Migrations that run old and new side by side.",
         "Extractions from a monolith.",
         "Programmes with several releases before the target.",
         "Any change with temporary workarounds."],
    skip=["Changes with no in-between state.",
          "Small swaps finished in a day."],
    related=["<b>Strangler fig migration</b> (this volume)", "<b>Architecture roadmap</b> (Vol. 3)", "<b>Technical debt register</b> (Vol. 2)", "<b>Migration planning</b> (Vol. 6)"],
    quiz=[("What's a temporary bridge?", "Something that exists only to get through a transition: comparison jobs, dual feeds, fallbacks."),
          ("What must every temporary bridge have?", "An owner and an end date (and a line in the debt register)."),
          ("When is a migration done?", "When the target state is reached and every temporary bridge is removed."),
          ("What did Ana's sweep find?", "Three bridges from the 2026 Dispatch extraction still running.")],
    try_it="Pick your last finished migration. List every temporary part it needed and check whether each is really gone. For the next one, write the states and the temporary bridges, with owners and end dates, before you start.",
    remember="Put the <span class=\"hl\">scaffolding</span> on the plan, with a <span class=\"hl\">date</span> to come down.",
    sources=["The Open Group, <i>TOGAF Standard</i>, “Transition Architecture”.",
             "The Open Group, <i>ArchiMate 3</i>, plateaus and gaps.",
             "Sam Newman, <i>Monolith to Microservices</i> (2019).",
             "Martin Fowler, “StranglerFigApplication” (2004)."],
)

# ------------------------------------------------------------------ 15 SaaS & Vendor Integration
sa_problem = Doodle(760, 280, "Doodle of 31 August 2027, month end. The billing service's webhooks stop for nine hours; invoice-paid updates never arrive, and Korenwolf's account shows unpaid invoices that were paid. The same month, WMS B's rate limit of 20 requests a second was hit during the Utrecht move, and its sandbox behaved differently from production.",
                    "Month end: nine hours without billing webhooks. The same month, a rate limit and a sandbox that lied.")
sa_problem.box(20, 30, 330, 100, "billing webhooks", "pink", sub="silent for 9 hours, 31 Aug", stroke="red")
sa_problem.box(410, 30, 330, 100, "Korenwolf's account", "y", sub="paid invoices shown unpaid")
sa_problem.box(20, 160, 330, 64, "WMS B: 20 req/s limit hit", "paper", size=15)
sa_problem.box(410, 160, 330, 64, "sandbox ≠ production", "paper", size=15)
sa_problem.note(380, 262, "systems we don't control, integrated as if we did", "red")

sa_analogy = Doodle(760, 250, "Doodle of hiring a catering company for a wedding. You don't control their kitchen. So you agree arrival times, check deliveries against the order, know their emergency number, have a backup for the cake, and don't let them rearrange your venue.",
                     "Hiring caterers: you don't control their kitchen, so you check deliveries, know their number and keep a backup.")
sa_analogy.icon("tray", 40, 60, 1.4)
for i, (t, s, f) in enumerate([("check deliveries", "against the order", "y"), ("their number", "status, escalation", "blue"), ("a backup", "for the cake", "green")]):
    sa_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, subsize=13)
sa_analogy.note(450, 210, "trust, but check and plan", "pen")

sa_how = Doodle(760, 380, "Larder's SaaS integration checklist, 6 September 2027. Webhooks: verify signatures, handle duplicates, and poll as a fallback when they go quiet. Limits: queue and back off below the vendor's rate limit. Testing: sandbox for development, plus contract tests against production read-only endpoints. Operations: subscribe to the vendor's status page, alert when an expected webhook doesn't arrive, know the support contact and the service levels. Boundaries: everything behind an anti-corruption layer, with an exit plan.",
                 "Webhooks that can go quiet, limits, sandboxes that differ, outages: plan for each, behind one adapter.")
items = [("webhooks", "verify · dedupe · poll if quiet", "y"), ("limits", "queue + back off below the limit", "blue"),
         ("testing", "sandbox + prod contract checks", "paper"), ("operations", "status page · silence alert · contacts", "green"),
         ("boundaries", "ACL adapter · exit plan", "green"), ("contract", "service levels · notice · data export", "paper")]
for i, (t, s, f) in enumerate(items):
    r, c = divmod(i, 2)
    sa_how.box(14 + c * 372, 14 + r * 104, 360, 90, t, f, sub=s, subsize=14)
sa_how.note(380, 350, "31 Aug again? the poll catches it within 15 minutes", "pen", size=16)

SAAS = dict(
    slug="saas-integration",
    kicker="a.k.a. “hiring the caterers”",
    tldr="SaaS and vendor systems run on someone else's schedule: webhooks go quiet, rate limits bite, sandboxes differ from production, and outages land at month end. Integrate as if you <b>don't control them</b>, because you don't: <b>verify and de-duplicate</b> webhooks and <b>poll as a fallback</b>; stay <b>below rate limits</b> with a queue; test against the <b>sandbox and production</b>; watch the <b>status page</b> and alert on <b>silence</b>; keep it all behind an <b>anti-corruption layer</b> with an <b>exit plan</b>.",
    chips=[("Family", "changing the landscape"), ("Origin", "integration practice with third-party services; Michael Nygard on integration points (<i>Release It!</i>)"), ("Lives in", "a checklist used for every new vendor integration"), ("Pairs with", "anti-corruption layer, exit plans, batch &amp; file transfer")],
    problem_side="Larder, 6 September 2027",
    problem="""  <p class="lead">On <b>31 August</b>, month end, the billing service's <b>webhooks stop for nine hours</b>. “Invoice paid” updates never arrive, and Korenwolf's account shows paid invoices as <b>unpaid</b>; Mo gets the call. The same month, WMS B's <b>rate limit</b> (20 requests a second) was hit during the Utrecht move, and its <b>sandbox</b> behaved differently from production. <span class="hl-pink">Larder had integrated systems it doesn't control as if it did.</span></p>
  <ul>
    <li>Webhooks can stop silently; nothing tells you.</li>
    <li>Vendor limits and sandboxes differ from what you tested.</li>
    <li>Outages hit at the worst moments: peaks, month ends.</li>
  </ul>""",
    problem_figs=[sa_problem],
    analogy_side="hiring the caterers",
    analogy="""  <p>For a wedding you hire <b>caterers</b>; you don't control their kitchen. So you agree arrival times, <b>check deliveries</b> against the order, keep <b>their emergency number</b>, have a <b>backup</b> for the cake, and don't let them rearrange your venue. You trust them, and you plan as if one thing will go wrong, because one usually does.</p>""",
    analogy_figs=[sa_analogy],
    map=[("Checking deliveries", "Verifying and de-duplicating webhooks"),
         ("Their emergency number", "Status page, support contacts, service levels"),
         ("A backup for the cake", "Polling when webhooks go quiet"),
         ("Not rearranging your venue", "The anti-corruption layer"),
         ("Agreeing arrival times", "Rate limits and expected timings, watched")],
    how_side="plan for the vendor's bad day",
    how="""  <p>Ana and Cho turned the lessons into a <b>checklist</b> for every vendor integration. Webhooks are <b>verified</b>, <b>de-duplicated</b>, and backed by a <b>poll every 15 minutes</b> when they go quiet; an <b>alert fires on silence</b>. Calls go through a <b>queue below the rate limit</b>. Tests run against the sandbox and <b>read-only production checks</b>. The vendor's <b>status page</b> feeds Larder's alerts. Applied to billing in September: a repeat of 31 August would now be caught within fifteen minutes.</p>""",
    how_figs=[sa_how],
    steps=[("Assume webhooks fail", "Verify signatures, de-duplicate, poll as a fallback, alert on silence."),
           ("Respect the limits", "Queue and back off below the vendor's rate limit; know the bulk options."),
           ("Test beyond the sandbox", "Contract checks against production's read-only endpoints."),
           ("Watch the vendor", "Status page subscriptions, support contacts, escalation path."),
           ("Keep it behind an adapter", "Anti-corruption layer; your own model inside."),
           ("Have an exit", "Data exports, notice periods, an exit plan.")],
    vocab=[("Webhook", "A vendor's HTTP call to you when something happens."),
           ("Rate limit", "The maximum calls a vendor accepts per period."),
           ("Polling fallback", "Asking the vendor periodically in case webhooks are missed."),
           ("Silence alert", "An alert when expected events stop arriving."),
           ("Sandbox", "A vendor's test environment; often not identical to production."),
           ("Status page", "The vendor's public page of incidents and uptime.")],
    code=dict(file="docs/integrations/vendor-checklist.md", note="Larder's vendor integration checklist, September 2027", plain=True, src="""
# Vendor / SaaS integration checklist              owner: Ana · used for every new vendor

WEBHOOKS    [ ] verify signatures  [ ] store event ids, ignore duplicates
            [ ] poll every 15 min for changes since the last event (fallback)
            [ ] alert if no event for N minutes when some are expected (billing: 60)
LIMITS      [ ] client-side queue below the rate limit (WMS B: 15 of 20 req/s)
            [ ] backoff + retry on 429/5xx  [ ] bulk endpoints for migrations
TESTING     [ ] sandbox for development  [ ] read-only contract checks on production
OPERATIONS  [ ] status page → our alerts  [ ] support contacts + escalation path
            [ ] service levels written down (and what we do when they're missed)
BOUNDARIES  [ ] one adapter, anti-corruption layer (no vendor words outside)
            [ ] exit plan: data export tested, notice period, alternatives
Applied     billing (Sep 2027) · WMS B (Sep 2027) · payment providers (Oct 2027)
"""),
    tools="tools: webhook signature libraries, an inbox table for de-duplication, a queue with rate limiting, status page subscriptions (Statuspage feeds), contract tests; vendor sandboxes as a start, not the finish.",
    gains=["<b>Silent failures caught</b> within minutes.",
           "<b>No duplicate effects</b> from repeated webhooks.",
           "<b>Rate limits respected</b>, even during migrations.",
           "<b>Outages are someone's alert</b>, not a client's call.",
           "<b>Exits stay possible</b>."],
    losses=["<b>Extra code</b>: polling, queues, checks.",
            "<b>More monitoring</b> to tune.",
            "<b>Production checks</b> need care and permission.",
            "<b>Not every vendor</b> offers what you need."],
    baseline="Each line compares <b>integrating vendors as if they were always up and as documented</b> to <b>a checklist for webhooks, limits, testing, operations, boundaries and exit</b>.",
    ratings=[(2, 4, "One checklist for every vendor."),
             (2, 4, "Mo hears about outages before clients do."),
             (3, 3, "Neutral."),
             (1, 5, "Silent webhooks caught in fifteen minutes."),
             (3, 4, "Behind an adapter, vendors can change."),
             (2, 4, "Each integration's checklist on record."),
             (3, 3, "A little extra code and monitoring."),
             (3, 3, "A checklist per integration."),
             (2, 4, "Teams integrate vendors safely without Ana.")],
    pitfalls=[("Webhooks only", "No fallback when they stop.", "poll for changes and alert on silence."),
              ("Trusting the sandbox", "It works in test; production differs.", "add read-only production contract checks."),
              ("Ignoring limits", "A migration hits 429s at peak.", "queue below the limit; use bulk endpoints."),
              ("Vendor words inside", "The vendor's model spreads through the code.", "an anti-corruption layer at the border.")],
    use=["Every SaaS or vendor integration.",
         "Payments, billing, warehouses, identity: anything critical.",
         "Before a migration that hammers a vendor's API.",
         "After a vendor outage surprised you."],
    skip=["Non-critical tools where a day's delay doesn't matter (still keep an exit)."],
    related=["<b>Anti-corruption layer</b> (this volume)", "<b>Batch &amp; file transfer</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)", "<b>Retries with backoff</b> (patterns, Vol. 1)"],
    quiz=[("Why poll if you have webhooks?", "Webhooks can stop silently; polling catches what was missed."),
          ("How do you handle a rate limit?", "A client-side queue below the limit, with backoff on 429s."),
          ("Why isn't the sandbox enough?", "It often behaves differently from production; add read-only production checks."),
          ("What's a silence alert?", "An alert when expected events stop arriving.")],
    try_it="Pick your most critical vendor integration. Ask: if its webhooks stopped for nine hours, when would we know? If its rate limit halved, what would break? Fix the worse answer this sprint, using the checklist.",
    remember="You don't control the <span class=\"hl\">caterers'</span> kitchen: check deliveries, know their number, keep a <span class=\"hl\">backup</span>.",
    sources=["Michael Nygard, <i>Release It!</i>, 2nd ed. (2018), on integration points.",
             "Stripe documentation, “Best practices for using webhooks”.",
             "Gregor Hohpe, <i>Cloud Strategy</i> (2020), on SaaS dependencies.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018), on dependencies."],
)

NOTES = [STRANGLER, TRANSITIONS, SAAS]
