# Series 2 · The Solution Architect's Notebook · Vol. 2 · Living with decisions.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 13 Technical Debt Register
td_problem = Doodle(760, 290, "Doodle of six shortcuts taken for the Rotterdam launch, scattered on sticky notes and TODO comments around one sentence: 'we'll fix it after launch'. Rotterdam hard-coding, Korenwolf orders by hand, Dispatch's 30-second loop, picker sync conflicts fixed by hand, outbox polling and cross-module reads. Three weeks after launch nobody remembers which ones matter, or how much each one costs.",
                    "“We'll fix it after launch.” Three weeks later: which ones, and how bad?")
td_problem.box(230, 112, 300, 64, "“we'll fix it after launch”", "y", size=16)
for x, y, t in [(20, 24, "TODO: RTM hack"), (270, 24, "Korenwolf by hand"), (520, 24, "30-s dispatch loop"),
                (20, 200, "picker sync by hand"), (270, 200, "outbox polls 2 s"), (520, 200, "cross-module reads")]:
    td_problem.box(x, y, 220, 44, t, "paper", size=15, rx=4)
td_problem.note(380, 278, "written nowhere · owned by nobody · cost unknown", "red")

td_analogy = Doodle(760, 270, "Doodle of a household's three kinds of debt. A mortgage: planned, low interest, worth it. A credit card: convenient, high interest, pay it off first. Money owed to a friend: forgotten, and it costs trust. The rule: write every debt down and pay the highest interest first.",
                    "Every household has debt. The trouble is debt you didn't write down, or the card at 20 % you keep ignoring.")
for i, (ic, t, s, f) in enumerate([("key", "the mortgage", "planned, low interest", "green"), ("receipt", "the credit card", "convenient, high interest", "pink"), ("handshake", "owed to a friend", "forgotten, costs trust", "paper")]):
    x = 20 + i * 250
    td_analogy.icon(ic, x + 80, 20, 1.1)
    td_analogy.box(x, 106, 220, 84, t, f, sub=s, size=17)
td_analogy.note(380, 240, "write it all down; pay the highest interest first", "green")

td_how = Doodle(760, 340, "Larder's technical debt register plotted by principal (effort to fix) and interest (cost per month). Pay now: TD-1 Rotterdam hard-coding and TD-5 picker sync by hand, high interest and small effort. Plan it: TD-3 Dispatch's 30-second loop and TD-6 cross-module reads, high interest and bigger effort. TD-2 Korenwolf orders by hand waits for its trigger. Leave it: TD-4 outbox polling, low interest. Policy: 20 percent of each sprint, highest interest first.",
                "Plot interest against principal. Pay the top-left first; leave the bottom-right on purpose.")
tdx, tdy = 80, 290
td_how.line(f"M{tdx} {tdy} H470")
td_how.line(f"M{tdx} {tdy} V30")
td_how.line("M275 30 V290", dash=True, thin=True)
td_how.line("M80 160 H470", dash=True, thin=True)
td_how.note(90, 54, "pay now", "green", anchor="start", size=18)
td_how.note(462, 54, "plan it", "pen", anchor="end", size=18)
td_how.note(90, 280, "when handy", "pen", anchor="start", size=18)
td_how.note(462, 280, "leave it", "pen", anchor="end", size=18)
td_how.text(275, 320, "principal: effort to fix →", "t t-soft", size=15)
td_how.rawtext('<text class="t t-soft" transform="translate(56 160) rotate(-90)" text-anchor="middle" font-size="15">interest per month →</text>')
for num, x, y, f in [(1, 140, 96, "pink"), (5, 210, 116, "pink"), (3, 380, 76, "y"), (6, 400, 136, "y"), (2, 330, 196, "paper"), (4, 380, 250, "green")]:
    td_how.circle(x, y, 13, fill=f)
    td_how.text(x, y + 6, str(num), "t-head", size=15)
for i, t in enumerate(["1 Rotterdam hard-coding", "2 Korenwolf by hand", "3 Dispatch 30-s loop", "4 outbox polling", "5 picker sync by hand", "6 cross-module reads"]):
    td_how.text(500, 60 + i * 30, t, anchor="start", size=15)
td_how.note(615, 280, "20 % of each sprint", "green", size=18)
td_how.note(615, 306, "highest interest first", "green", size=18)

TD_REGISTER = dict(
    slug="tech-debt-register",
    kicker="a.k.a. “the household's list of loans”",
    tldr="Shortcuts are often the right call: Rotterdam's date beat “configuration, not code”, on purpose. What turns a shortcut into trouble is forgetting it. Keep a <b>technical debt register</b>: one line per known shortcut, with <b>why</b> it was taken, its <b>interest</b> (what it costs every month), its <b>principal</b> (the effort to fix), an <b>owner</b> and a <b>payback trigger</b>. Review it monthly, reserve a fixed share of each sprint, and pay the <b>highest interest first</b>; some debt you leave on purpose.",
    chips=[("Family", "living with decisions"), ("Origin", "Ward Cunningham's debt metaphor (1992); Martin Fowler's technical debt quadrant (2009)"), ("Lives in", "docs/debt/register.md, linked from the decision log"), ("Pairs with", "trade-off sliders, ADRs, fitness functions")],
    problem_side="Larder, 15 June 2026",
    problem="""  <p class="lead">Rotterdam opened on time. To make the date, the team took <b>six shortcuts</b>, each agreed with a shrug and “we'll fix it after launch”: three Rotterdam values hard-coded, Korenwolf's orders entered by hand, Dispatch's 30-second loop, picker sync conflicts fixed by hand, and more. Three weeks later, preparing the next quarter, Ana asks which shortcuts matter most. Nobody knows. They're in <span class="hl-pink">TODO comments, sticky notes and memories</span>, with no cost attached.</p>
  <ul>
    <li>Debt you don't write down compounds silently.</li>
    <li>Without interest figures, debt loses every priority fight against features.</li>
    <li>Engineers fix what annoys them, not what costs most.</li>
  </ul>""",
    problem_figs=[td_problem],
    analogy_side="the household's loans",
    analogy="""  <p>Most households carry debt, and that's fine. A <b>mortgage</b> is planned and worth it. A <b>credit card</b> is convenient and expensive: pay it first. The <b>money you owe a friend</b> is the dangerous one, because nobody wrote it down and it costs trust. A sensible household keeps one list, knows each interest rate, and pays the most expensive first.</p>""",
    analogy_figs=[td_analogy],
    map=[("The mortgage", "Deliberate, prudent debt: TD-4, outbox polling, accepted in ADR 0007"),
         ("The credit card", "High-interest debt: TD-1, Rotterdam hard-coding, before Utrecht"),
         ("Owed to a friend, forgotten", "Debt in TODO comments and memories"),
         ("The interest rate", "Cost per month: hours, incidents, slower delivery"),
         ("The monthly budget", "20 % of each sprint for paying debt")],
    how_side="interest, principal, a trigger",
    how="""  <p>Plotting the six items made the order obvious. <b>TD-1</b> (Rotterdam hard-coding) and <b>TD-5</b> (picker sync) were cheap to fix and costly to keep: paid in July. <b>TD-3</b> (the dispatch loop) was already planned with Engine A. <b>TD-4</b> stays: the interest is tiny and ADR 0007 accepted it. <b>TD-2</b> waits for its trigger.</p>""",
    how_figs=[td_how],
    steps=[("Collect the shortcuts", "Ask the teams, search TODOs, read the sliders and ADRs: “what did we accept to make a date?”"),
           ("One line each", "What, why it was taken (deliberate or accidental), where, linked ADR or ticket."),
           ("Put a price on it", "Interest: hours, incidents or delay per month. Principal: effort to fix, in days."),
           ("Give it an owner and a trigger", "“Before Utrecht prep starts”, “if a second office signs”, “if incidents > 2/month”."),
           ("Budget for it", "A fixed share of each sprint (Larder: 20 %), highest interest first."),
           ("Review monthly", "Update interest, close paid items, add new ones; decide to leave some on purpose.")],
    vocab=[("Technical debt", "A shortcut that makes later change slower or riskier."),
           ("Interest", "The ongoing cost of keeping the debt, per month."),
           ("Principal", "The effort to remove it."),
           ("Deliberate debt", "Taken knowingly, for a reason, with a plan."),
           ("Payback trigger", "The event or date when it must be paid."),
           ("Debt quadrant", "Fowler: deliberate or inadvertent, prudent or reckless.")],
    code=dict(file="docs/debt/register.md", note="Larder's technical debt register, 15 June 2026", plain=True, src="""
# Technical debt register                  reviewed monthly · 20 % of each sprint

| ID   | Debt                                   | Why taken                  | Interest / month         | Principal | Owner | Pay by / trigger          |
|------|----------------------------------------|----------------------------|--------------------------|-----------|-------|---------------------------|
| TD-1 | 3 Rotterdam settings hard-coded        | date > config (sliders)    | Utrecht needs code edits | 5 days    | Ben   | before Utrecht prep (Oct) |
| TD-2 | Korenwolf orders entered by hand       | ADR 0011, pilot            | ~12 h support            | 4 weeks   | Mo/Ben| more offices sign         |
| TD-3 | Dispatch: 30-s assignment loop         | RFC-003, launch first      | on time 84 % in RTM      | 4 weeks   | Eli   | July (Engine A, ADR 0012) |
| TD-4 | Outbox relay polls every 2 s           | ADR 0007, accepted         | ~2 s delay, no complaints| 1 week    | Ben   | orders > 200/s            |
| TD-5 | Picker sync conflicts fixed by hand    | offline-first, v1          | ~12/week at Noord        | 2 weeks   | Dee   | July                      |
| TD-6 | 4 cross-module table reads (allowed)   | Jan fitness-function list  | blocks Payments split    | 3 weeks   | Cho   | before any Payments split |

Left on purpose: TD-4 (low interest; revisit on its trigger).
"""),
    tools="tools: a Markdown table in the repo, or tickets with a “debt” label and fields for interest and principal. Code-level signals help find debt (static analysis, change-frequency hotspots with CodeScene), but the register is about decisions, not lint warnings.",
    gains=["<b>Shortcuts stay visible</b> after the launch rush.",
           "<b>Priced debt</b> can win priority fights against features.",
           "<b>Highest interest first</b>, not loudest annoyance.",
           "<b>Deliberate shortcuts become safe</b>: they're tracked.",
           "<b>Some debt is left on purpose</b>, with a reason."],
    losses=["<b>Interest is a guess</b> for many items.",
            "<b>Monthly upkeep</b> or it goes stale.",
            "<b>Can become a wish list</b> of every refactor.",
            "<b>20 % is a negotiation</b> with product, every quarter."],
    baseline="Each line compares <b>shortcuts remembered as TODOs and “after launch”</b> to <b>a register with interest, principal, owner and trigger, paid from a fixed sprint budget</b>.",
    ratings=[(2, 4, "Anyone can see what was cut and why."),
             (2, 4, "Product sees the cost of debt in its own terms."),
             (3, 4, "Shortcuts can be taken fast, because they're tracked."),
             (2, 4, "High-interest debt is paid before it causes incidents."),
             (2, 4, "Triggers say when debt must be paid."),
             (2, 4, "Each item links to the decision that created it."),
             (2, 5, "Interest makes the ongoing cost visible."),
             (3, 3, "An hour a month to keep it current."),
             (3, 4, "Teams pay their own debt from the sprint budget.")],
    pitfalls=[("No price", "A list of complaints with no interest figures.", "estimate interest per month, even roughly."),
              ("Everything is debt", "Every wished-for refactor goes on the list.", "only shortcuts that cost something now or block something soon."),
              ("No budget", "Debt waits for a quiet quarter that never comes.", "a fixed share of every sprint."),
              ("Paying the wrong debt", "The fun refactor beats the expensive one.", "pay highest interest first; leave low-interest debt on purpose.")],
    use=["After any launch where shortcuts were taken.",
         "When “we'll fix it later” is heard in planning.",
         "When product and engineering argue about refactoring time.",
         "Before choosing what to fix in a quarter."],
    skip=["Prototypes and spikes: their code is thrown away.",
          "Code style issues: that's what linters are for."],
    related=["<b>Trade-off sliders</b> (this volume)", "<b>Revisiting decisions</b> (this volume)", "<b>Fitness functions</b> (Vol. 1)", "<b>The architecture backlog</b> (Vol. 6)"],
    quiz=[("What's the difference between interest and principal?", "Interest is what keeping the debt costs each month; principal is the effort to remove it."),
          ("Which debt should be paid first?", "The highest interest relative to its principal."),
          ("Is all technical debt bad?", "No: deliberate, prudent debt with a plan can be the right call; some low-interest debt is left on purpose."),
          ("What does every line need besides a description?", "Why it was taken, interest, principal, an owner and a payback trigger.")],
    try_it="Ask your team for every shortcut taken in the last three months. Write each as a line with interest per month, principal in days, an owner and a trigger. Plot them on interest vs principal, and bring the top-left two to your next planning meeting with their monthly cost.",
    remember="Debt is fine; <span class=\"hl\">unwritten</span> debt isn't. Pay the <span class=\"hl\">highest interest</span> first.",
    sources=["Ward Cunningham, “The WyCash Portfolio Management System” (OOPSLA, 1992).",
             "Martin Fowler, “Technical Debt Quadrant” (martinfowler.com, 2009).",
             "Philippe Kruchten, Robert Nord, Ipek Ozkaya, <i>Managing Technical Debt</i> (2019).",
             "Adam Tornhill, <i>Your Code as a Crime Scene</i> (2015), on hotspots."],
)

# ------------------------------------------------------------------ 14 Exit Plans & Reversibility
ex_problem = Doodle(760, 290, "Doodle of a letter from StockPilot in July 2026: from the July 2027 renewal, prices are per store, which for Larder's twelve planned stores means about three times today's cost. Marco asks: can we leave? Nobody can answer what depends on StockPilot, how long leaving would take, or what data Larder gets back. No answers means no negotiating position.",
                    "“Can we leave?” Three questions nobody can answer, and a renewal with no leverage.")
ex_problem.icon("envelope", 40, 40, 1.6)
ex_problem.box(150, 30, 300, 90, "StockPilot, from Jul 2027", "y", sub="per store: ≈ 3× today", size=17)
ex_problem.box(520, 40, 220, 70, "Marco", "paper", sub="“can we leave?”")
for i, t in enumerate(["what depends on it?", "how long would leaving take?", "what data do we get back?"]):
    ex_problem.note(400, 162 + i * 32, "? " + t, "red", size=19)
ex_problem.note(380, 272, "no answers = no negotiating position", "red")

ex_analogy = Doodle(760, 270, "Doodle of a theatre's emergency exits. Nobody plans to use them, but they are marked, kept unlocked, and tested in a drill. If the exits are blocked, nobody notices until the night they're needed.",
                    "A theatre's exits: you hope never to use them, so they're marked, unlocked and drilled.")
for i, (ic, t, s, f) in enumerate([("door", "marked", "everyone knows where", "green"), ("key", "unlocked", "nothing blocks the way", "y"), ("bell", "drilled", "tested, on purpose", "blue")]):
    x = 20 + i * 250
    ex_analogy.icon(ic, x + 80, 14, 1.1)
    ex_analogy.box(x, 106, 220, 84, t, f, sub=s, size=18)
ex_analogy.note(380, 240, "hope never to use it; be able to", "green")

ex_how = Doodle(760, 320, "How Larder's exit from StockPilot looks, thanks to ADR 0005. Ordering, Fulfilment and Dispatch never call StockPilot; they use Larder's Stock module, which caches stock and holds the only adapter. Only that adapter talks to StockPilot. The alternatives, another warehouse system or Larder's own stock service, would replace the adapter, not the modules. One adapter in one module made the exit cheap.",
                "Every module asks Larder's Stock module; only its adapter talks to StockPilot. Leaving means replacing one adapter.")
ex_how.box(20, 26, 340, 250, None, "paper")
ex_how.head(190, 56, "Larder Core", size=17)
for i, t in enumerate(["Ordering", "Fulfilment", "Dispatch"]):
    ex_how.box(34 + i * 108, 76, 98, 44, t, "blue", size=14)
    ex_how.arrow(83 + i * 108, 124, 150 + i * 40, 176)
ex_how.box(60, 180, 260, 76, "Stock module", "green", sub="cache + the only adapter", subsize=15)
ex_how.arrow(326, 218, 466, 74)
ex_how.box(470, 30, 270, 70, "StockPilot", "y", sub="contract to Jun 2027")
ex_how.arrow(326, 228, 466, 170, dash=True)
ex_how.box(470, 146, 270, 50, "WMS B", "paper", dash=True, size=16)
ex_how.arrow(326, 238, 466, 240, dash=True)
ex_how.box(470, 216, 270, 50, "our own stock service", "paper", dash=True, size=15)
ex_how.note(380, 306, "one adapter in one module: ADR 0005 made the exit cheap", "green", size=18)

EXIT = dict(
    slug="exit-plans",
    kicker="a.k.a. “the theatre's emergency exits”",
    tldr="Every vendor, platform and big dependency is a door that's easier to walk through than to leave. Before signing, and at least once a year after, write an <b>exit plan</b>: what you depend on, the <b>data</b> you'd need back and in what format, the <b>alternatives</b>, the <b>effort and lead time</b> to leave, the <b>early warning signs</b>, and what you do <b>now</b> to keep leaving cheap (an adapter in one place, regular exports, contract clauses). You hope never to use it; having it is what gives you <b>choices and leverage</b>.",
    chips=[("Family", "living with decisions"), ("Origin", "exit strategies in outsourcing and regulated sectors (e.g. EBA outsourcing guidelines, 2019); Gregor Hohpe on lock-in"), ("Lives in", "one page per vendor, next to its ADR and contract"), ("Pairs with", "build vs buy, one-way doors, anti-corruption layer")],
    problem_side="Larder, 6 July 2026",
    problem="""  <p class="lead">A letter from <b>StockPilot</b>: from the renewal in July 2027, prices are <b>per store</b>. For the twelve stores Larder plans by the end of 2027 that's <b>about three times</b> today's bill. The contract ends in June 2027 with six months' notice, so the decision is due in <b>December</b>. Marco asks Ana: <i>can we leave?</i> Nobody can say what depends on StockPilot, how long leaving would take, or what data Larder would get back. <span class="hl-pink">Without an exit, there's no negotiation</span>, only a price.</p>
  <ul>
    <li>Lock-in is invisible until the price goes up or the vendor goes down.</li>
    <li>Leaving often takes longer than the notice period.</li>
    <li>The cheapest time to plan an exit is before you need one.</li>
  </ul>""",
    problem_figs=[ex_problem],
    analogy_side="the theatre's emergency exits",
    analogy="""  <p>No theatre plans for the audience to leave by the emergency exits. But the exits are <b>marked</b>, kept <b>unlocked</b>, and <b>drilled</b>. A blocked exit costs nothing on a normal night, and everything on the night it's needed. Checking them is part of running a theatre, not a sign you expect a fire.</p>""",
    analogy_figs=[ex_analogy],
    map=[("Marked exits", "An exit plan per vendor: alternatives, effort, lead time"),
         ("Kept unlocked", "Keeping exits cheap: one adapter, regular exports, contract clauses"),
         ("Fire drills", "Testing the export once a year, pricing the alternative"),
         ("A blocked exit", "Lock-in found at renewal time"),
         ("The night it's needed", "A price rise, an outage, a vendor closing down")],
    how_side="keep the way out short",
    how="""  <p>The good news was in an old decision: <b>ADR 0005</b> put a stock cache and the only StockPilot adapter inside Larder's <b>Stock module</b>. No other module talks to StockPilot. Leaving means replacing <b>one adapter</b>, not rewriting Ordering, Fulfilment and Dispatch. Ana costed two alternatives; Marco goes into the autumn renewal talks with a real one.</p>""",
    how_figs=[ex_how],
    steps=[("List your exits", "Every vendor, SaaS, platform and open-source dependency you couldn't remove in a week."),
           ("Map the dependency", "Which parts of your system touch it, directly? Ideally: one adapter in one place."),
           ("Secure your data", "What you'd need back, in what format, how often you export it today."),
           ("Price the alternatives", "Two options with effort, lead time and cost; compare with the notice period."),
           ("Watch for warnings", "Price changes, outages, acquisitions, end-of-life notices, slow support."),
           ("Keep it cheap, now", "Adapters, regular exports, notice and data clauses in the contract; review yearly.")],
    vocab=[("Exit plan", "How you'd leave a vendor or platform, and what it would take."),
           ("Lock-in", "The cost and time of leaving."),
           ("Adapter", "One place in your code that talks to the vendor."),
           ("Notice period", "How early you must say you're leaving."),
           ("Data portability", "Getting your data back in a usable format."),
           ("Leverage", "The negotiating power a credible alternative gives you.")],
    code=dict(file="docs/exits/stockpilot.md", note="exit plan, written 6 July 2026", plain=True, src="""
# Exit plan: StockPilot (warehouse management)       owner: Ana · review: yearly

We depend on   stock levels and locations per store; goods-in; stock counts
Touch points   Stock module only (adapter + cache, ADR 0005). No other module calls it.
Contract       ends 30 Jun 2027 · 6 months' notice → decide by 31 Dec 2026
Our data       daily export (products, locations, levels) since 2025: tested ✓
               movement history: API only, 10 req/s → bulk export requested

Alternatives                     effort        lead time   cost / year (12 stores)
1. Renew at new pricing          none          –           ≈ 3× today
2. WMS B (2 shortlisted)         adapter + migration, ~3 months   5 months   ≈ 1.4× today
3. Own stock service             grow the Stock module, ~6 months 7 months   people, not licences

Warning signs  price change (Jul 2026 ✓) · API limits · outages > 2/quarter · acquisition
Keep it cheap  no new module talks to StockPilot · daily export kept · ask for a
               12-month exit-assistance clause at renewal
Next step      price option 2 properly by 30 Sep (needs 5 months' lead time).
"""),
    tools="tools: one page per vendor in the repo. Contract registers in finance tools; data export jobs with alerts; anti-corruption layers (Vol. 4) to keep vendors behind one adapter. Regulated firms follow formal exit-plan rules (e.g. EBA outsourcing guidelines, DORA).",
    gains=["<b>Leverage</b>: a costed alternative changes the renewal talk.",
           "<b>No surprises</b>: lead times known before notice periods run out.",
           "<b>Cheaper exits</b> from design choices made now.",
           "<b>Data you own</b>, tested regularly.",
           "<b>Calmer decisions</b> when a vendor changes course."],
    losses=["<b>Upfront effort</b>: a day per important vendor.",
            "<b>Adapters and exports cost</b> a little, every month.",
            "<b>Can look like distrust</b> to the vendor.",
            "<b>Plans go stale</b> without a yearly review."],
    baseline="Each line compares <b>finding out how locked in you are at renewal time</b> to <b>a reviewed exit plan per vendor, with data exports and one adapter keeping the way out short</b>.",
    ratings=[(2, 4, "Everyone can see what depends on which vendor."),
             (2, 4, "Finance and engineering prepare the renewal together."),
             (2, 4, "When the letter comes, the options are already costed."),
             (1, 5, "Lock-in and lead times are known before they bite."),
             (2, 5, "Adapters and exports keep doors two-way."),
             (3, 4, "Each plan links to the ADR and contract."),
             (2, 5, "Alternatives priced; renewal cost is a choice."),
             (3, 3, "A day per vendor, plus a yearly review."),
             (3, 3, "Owned by the architect and finance, mostly.")],
    pitfalls=[("Planning at renewal", "The exit is costed after the notice deadline.", "write it before signing; review a year ahead."),
              ("Vendor everywhere", "Five modules call StockPilot directly.", "one adapter in one place; fitness function to keep it there."),
              ("Untested exports", "The export exists but nobody has opened it.", "restore it into something once a year."),
              ("Lead time > notice", "Leaving takes 7 months; notice is 6.", "start pricing alternatives before the notice window.")],
    use=["Every vendor or platform you couldn't remove in a week.",
         "Before signing or renewing a contract.",
         "When a vendor changes prices, terms or owners.",
         "Regulated environments that require exit plans."],
    skip=["Commodity tools with drop-in alternatives (a CI service, a font).",
          "Short trials you'd simply stop."],
    related=["<b>Build vs buy vs open source</b> (this volume)", "<b>One-way vs two-way doors</b> (this volume)", "<b>Anti-corruption layer</b> (Vol. 4)", "<b>SaaS &amp; vendor integration</b> (Vol. 4)"],
    quiz=[("What makes an exit cheap?", "Few touch points (one adapter), your data regularly exported, and contract clauses for notice and help."),
          ("When should you write an exit plan?", "Before signing, and review it at least yearly, well before the notice period."),
          ("Why compare lead time with the notice period?", "If leaving takes longer than the notice, you have to start before you give notice."),
          ("What does an exit plan give you if you never leave?", "Leverage in negotiations and calm, informed decisions.")],
    try_it="Pick the vendor your system would struggle most to lose. In one page, write what depends on it, where your code touches it, how you'd get your data back, two alternatives with rough effort, and the notice period. Then test the data export by loading it somewhere.",
    remember="Hope never to use the <span class=\"hl\">exit</span>. Keep it marked, <span class=\"hl\">unlocked</span> and drilled.",
    sources=["Gregor Hohpe, “Don't Get Locked Up Into Avoiding Lock-In” (martinfowler.com, 2019).",
             "European Banking Authority, “Guidelines on Outsourcing Arrangements” (2019), on exit strategies.",
             "Eric Evans, <i>Domain-Driven Design</i> (2003), on anti-corruption layers.",
             "Mark Richards and Neal Ford, <i>Fundamentals of Software Architecture</i> (2020)."],
)

# ------------------------------------------------------------------ 15 Revisiting Decisions
rv_problem = Doodle(760, 290, "Doodle of one week in September 2026. Three decisions are reopened with no new facts: the outbox is slow so switch to change data capture; should we still be a monolith; Kafka is overkill. Meanwhile the one real change goes unnoticed: Korenwolf has signed for three offices, and orders are still entered by hand under the pilot decision.",
                    "Three decisions re-argued on a hunch; the one real trigger, unnoticed.")
for i, t in enumerate(["“outbox is slow: CDC?”", "“still a monolith?”", "“Kafka is overkill”"]):
    rv_problem.box(20, 24 + i * 64, 320, 50, t, "paper", size=16)
rv_problem.note(180, 236, "no new facts, just a hunch", "red", size=18)
rv_problem.box(400, 50, 340, 140, None, "pink", stroke="red")
rv_problem.head(570, 84, "Korenwolf: 3 offices", size=18, color="red")
rv_problem.text(570, 122, "orders still entered by hand", size=16)
rv_problem.text(570, 150, "(ADR 0011: the pilot)", size=16)
rv_problem.note(570, 236, "the real trigger: unnoticed", "red", size=18)

rv_analogy = Doodle(760, 270, "Doodle of a doctor's prescription with a review date: take this for three months, then come back. At the review the doctor checks the results and decides to continue, change or stop. Nobody stops the medicine on a hunch, and nobody takes it forever without a check.",
                    "A prescription with a review date: check the results, then continue, change or stop, on purpose.")
rv_analogy.icon("recipe", 40, 50, 1.6)
rv_analogy.note(80, 180, "3 months, then", "pen", size=18)
rv_analogy.note(80, 204, "come back", "pen", size=18)
rv_analogy.arrow(150, 120, 240, 120)
rv_analogy.box(246, 80, 180, 80, "the review", "y", sub="check the results")
for i, (t, f) in enumerate([("continue", "green"), ("change", "y"), ("stop", "pink")]):
    y = 30 + i * 70
    rv_analogy.arrow(432, 120, 536, y + 25)
    rv_analogy.box(540, y, 180, 50, t, f, size=18)
rv_analogy.note(380, 250, "on the date, with the results, not on a hunch", "green")

rv_how = Doodle(760, 340, "Larder's quarterly decision review, 21 September 2026. Each ADR's revisit trigger against today's facts. ADR 0002: a module needs its own scaling; only Dispatch, done: keep. ADR 0005: stock mismatch over 1 percent; it's 0.4 percent: keep. ADR 0007: orders over 200 per second; peak is 2.6: keep. ADR 0010: more than five services; there are three: keep. ADR 0011: more offices sign; Korenwolf signed three: superseded by ADR 0014. ADR 0012: on time under 93 percent after eight weeks; Amsterdam 93, Rotterdam 91: watch. Forty-five minutes: four keep, one watch, one superseded.",
                "Each decision's trigger against today's facts. 45 minutes: 4 keep, 1 watch, 1 superseded.")
rv_how.head(20, 34, "ADR", anchor="start", size=15)
rv_how.head(90, 34, "revisit when…", anchor="start", size=15)
rv_how.head(420, 34, "today", anchor="start", size=15)
rv_how.head(670, 34, "verdict", size=15)
for i, (adr, trig, now, verdict, f) in enumerate([("0002", "a module needs its own scaling", "only Dispatch (done)", "keep", "green"), ("0005", "stock mismatch > 1 %", "0.4 %", "keep", "green"),
                                                  ("0007", "orders > 200/s", "peak 2.6/s", "keep", "green"), ("0010", "more than 5 services", "3", "keep", "green"),
                                                  ("0011", "more offices sign", "Korenwolf: 3 offices", "→ ADR 0014", "pink"), ("0012", "on time < 93 % after 8 weeks", "AMS 93 · RTM 91 %", "watch", "y")]):
    y = 56 + i * 40
    if f != "green":
        rv_how.box(12, y + 2, 736, 34, None, f, rx=6)
    rv_how.text(20, y + 25, adr, "t-head", anchor="start", size=14)
    rv_how.text(90, y + 25, trig, anchor="start", size=14)
    rv_how.text(420, y + 25, now, anchor="start", size=14)
    rv_how.text(670, y + 25, verdict, "t-head" + (" t-green" if f == "green" else ""), size=14)
rv_how.line("M14 306 H746", thin=True)
rv_how.note(380, 330, "a hunch reopens nothing; a trigger reopens anything", "green", size=18)

REVISIT = dict(
    slug="revisiting-decisions",
    kicker="a.k.a. “the prescription with a review date”",
    tldr="Decisions age. Some should change when the world does; most shouldn't change just because someone new dislikes them. Give every ADR a <b>revisit trigger</b>: a measurable condition or a date (“if orders pass 200/s”, “if a second office signs”). Then hold a short <b>decision review</b> every quarter: check each trigger against <b>today's facts</b>, and decide <b>keep, watch or supersede</b>. Re-open decisions <b>on purpose</b>, with evidence, not on a hunch, and never keep one alive just because it was expensive.",
    chips=[("Family", "living with decisions"), ("Origin", "“revisit” conditions in ADR templates (MADR); after-action reviews; Annie Duke on decision quality"), ("Lives in", "a “Revisit when” line in each ADR; a quarterly review note"), ("Pairs with", "ADRs, decision log, technical debt register")],
    problem_side="Larder, 21 September 2026",
    problem="""  <p class="lead">One week in September, three decisions get re-opened in three different chats: a new on-call engineer says “the outbox is slow, let's switch to change data capture”; Femke asks whether Larder should “still be a monolith”; someone calls Kafka overkill. <b>No new facts</b>, just hunches. Meanwhile the one real change slips by: <span class="hl-pink">Korenwolf has signed for three offices</span>, and their orders are still entered by hand under ADR 0011, a decision written for a twelve-week pilot.</p>
  <ul>
    <li>Without triggers, decisions are reopened by whoever feels strongest this week.</li>
    <li>The decisions that really should change are missed, because nobody is checking.</li>
    <li>Sunk cost keeps bad decisions alive; fashion kills good ones.</li>
  </ul>""",
    problem_figs=[rv_problem],
    analogy_side="the prescription with a review date",
    analogy="""  <p>A good doctor prescribes medicine <b>with a review date</b>: take this for three months, then come back. At the review, the doctor <b>checks the results</b> and decides to <b>continue, change or stop</b>. Patients don't stop on a hunch halfway through, and they don't take it forever without a check.</p>""",
    analogy_figs=[rv_analogy],
    map=[("The prescription", "The ADR"),
         ("“Come back in three months, or if…”", "The revisit trigger"),
         ("The blood test", "Today's facts: volumes, error rates, contracts"),
         ("Continue, change or stop", "Keep, watch, or supersede with a new ADR"),
         ("Not stopping on a hunch", "No re-arguing without new evidence")],
    how_side="triggers, checked every quarter",
    how="""  <p>The review took <b>45 minutes</b>. Four decisions stayed: their triggers weren't close. Dispatch's routing (ADR 0012) went on <b>watch</b>: Rotterdam is at 91 % on time, below the 93 % trigger. And ADR 0011 was <b>superseded</b>: Ana proposed <b>ADR 0014</b>, scheduled orders on business accounts in Ordering, option B from April's analysis. The hunches got a polite answer: “show me the trigger”.</p>""",
    how_figs=[rv_how],
    steps=[("Write a trigger in every ADR", "A measurable condition or a date: “orders > 200/s”, “a second office signs”, “review in 12 months”."),
           ("Collect the facts", "Before the review: the numbers each trigger needs, from dashboards and the business."),
           ("Review quarterly, briefly", "Architect and tech leads, 45 minutes: each trigger against the facts."),
           ("Decide: keep, watch or supersede", "Watch = check again next month. Supersede = a new ADR that links the old one."),
           ("Answer hunches with triggers", "“What fact would change it?” If it's new, check it; if not, the decision stands."),
           ("Ignore sunk cost", "What it cost to build doesn't matter; only what's best from here.")],
    vocab=[("Revisit trigger", "The condition or date that re-opens a decision."),
           ("Decision review", "A regular check of triggers against facts."),
           ("Keep / watch / supersede", "The three outcomes of a review."),
           ("Sunk cost", "Money or effort already spent; irrelevant to what's best now."),
           ("Decision quality", "Judging a decision by what was known then, not by the outcome alone."),
           ("Hunch", "A feeling without new facts: not a reason to re-open.")],
    code=dict(file="docs/decisions/reviews/2026-Q3.md", note="decision review, 21 September 2026", plain=True, src="""
# Decision review · 2026 Q3                21 Sep · Ana, Ben, Cho, Dee, Eli · 45 min

| ADR  | Revisit when                    | Today                        | Verdict                 |
|------|---------------------------------|------------------------------|-------------------------|
| 0002 | a module needs its own scaling  | only Dispatch (extracted)    | keep                    |
| 0005 | stock mismatch > 1 %            | 0.4 %                        | keep (see exit plan)    |
| 0007 | orders > 200/s at peak          | peak 2.6/s                   | keep                    |
| 0010 | more than 5 services            | 3                            | keep                    |
| 0011 | a client signs for more offices | Korenwolf: 3 offices (Sep)   | supersede → ADR 0014    |
| 0012 | on time < 93 % after 8 weeks    | Amsterdam 93 %, Rotterdam 91 % | watch: re-check 19 Oct |

Hunches raised this quarter, and the fact that would re-open them:
- "Outbox is slow" → measured delay 1.8 s; trigger is volume, not taste. Keep.
- "Still a monolith?" → which module needs its own scaling or team? None yet. Keep.
New: ADR 0014 "Scheduled orders on business accounts, in Ordering" (proposed).
"""),
    tools="tools: a “Revisit when” line in the ADR template (MADR has “more information”; add your own field), a quarterly calendar slot, and dashboards for each trigger's number. Log4brains and Backstage can list ADRs by status for the review.",
    gains=["<b>Real changes get caught</b>: Korenwolf's contract re-opened ADR 0011.",
           "<b>Fewer hunch debates</b>: “show me the trigger”.",
           "<b>Decisions stay current</b> without a rewrite.",
           "<b>Sunk cost loses</b>: supersede when the facts say so.",
           "<b>Trust in decisions</b>: people know they'll be checked."],
    losses=["<b>Triggers can be wrong</b>, or the wrong metric.",
            "<b>A quarterly slot</b> with five people.",
            "<b>Facts take effort</b> to gather.",
            "<b>“Watch” can become forever</b> without a re-check date."],
    baseline="Each line compares <b>decisions re-opened on hunches, or never</b> to <b>revisit triggers in every ADR, checked against facts in a short quarterly review</b>.",
    ratings=[(3, 4, "Each decision says when it should be looked at again."),
             (2, 4, "Re-opening is a shared process, not a chat war."),
             (2, 4, "Hunch debates end with “what's the trigger?”."),
             (2, 4, "Triggers catch changes before they hurt."),
             (3, 5, "Decisions change on purpose when the facts do."),
             (3, 5, "Superseded ADRs link to their successors."),
             (3, 3, "Cost can be a trigger; not the focus."),
             (3, 3, "45 minutes a quarter, plus gathering facts."),
             (3, 4, "Teams can propose triggers and bring facts.")],
    pitfalls=[("No triggers", "ADRs end at “Consequences”.", "add a measurable “revisit when” to every ADR."),
              ("Hunches win", "The loudest voice re-opens a decision weekly.", "ask what new fact would change it; check it at the review."),
              ("Watch forever", "ADR 0012 on watch for a year.", "every “watch” gets a re-check date."),
              ("Sunk-cost loyalty", "“We spent four months on it.”", "judge from here on; supersede if the facts say so.")],
    use=["Every ADR, at the time it's written.",
         "When a decision keeps being re-argued.",
         "After big changes: a new city, a new client, a new team.",
         "Quarterly, as a standing slot."],
    skip=["Two-way doors: just change them.",
          "Decisions about to be retired anyway."],
    related=["<b>Architecture decision records</b> (this volume)", "<b>Technical debt register</b> (this volume)", "<b>Options analysis</b> (this volume)", "<b>Evolutionary architecture</b> (Vol. 6)"],
    quiz=[("What makes a good revisit trigger?", "A measurable condition or a date that would change the decision, e.g. “orders > 200/s”."),
          ("What are the three outcomes of a review?", "Keep, watch (with a re-check date), or supersede with a new ADR."),
          ("Someone says “the outbox is slow”. What do you ask?", "What new fact would change the decision? Then check it against the trigger."),
          ("Why ignore sunk cost?", "What's been spent can't be recovered; only the best path from here matters.")],
    try_it="Take your five most important past decisions. For each, write one measurable “revisit when” trigger. Book 45 minutes with two colleagues, gather the current number for each trigger, and decide keep, watch or supersede. Note how many hunch debates you can now answer with a trigger.",
    remember="Every decision gets a <span class=\"hl\">review date</span>. A hunch reopens nothing; a <span class=\"hl\">trigger</span> reopens anything.",
    sources=["MADR, “Markdown Any Decision Records” (adr.github.io/madr), on decision follow-up.",
             "Annie Duke, <i>Thinking in Bets</i> (2018), on judging decisions, not outcomes.",
             "Neal Ford et al., <i>Building Evolutionary Architectures</i>, 2nd ed. (2022).",
             "U.S. Army, “A Leader's Guide to After-Action Reviews” (1993)."],
)

NOTES = [TD_REGISTER, EXIT, REVISIT]
