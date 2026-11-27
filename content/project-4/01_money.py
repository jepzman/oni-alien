# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 4 · Money (the Finance domain)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 4").
# The money, reconciled with vols. 1–3 (k€, excluding VAT):
#   budget 30 Jan: builder 148 · cold room + fridges 64 · equipment + store IT 48 · people 60 (40 × 1.5) · marketing 40
#                  = 360 + reserve 20 = 380.  Reserve draws: C-01 fridges 14 · C-02 weekend 5 · C-04 router 0.6 → 0.4 left.
#   committed: 61 (13 Feb: recruiting 30 + marketing 31) · 335 (27 Feb: + cold room 78, equipment 48, builder 148) · 355.5 (27 Mar).
#   earned value, Fri 20 Mar (BAC 374 = 360 + 14): PV 178 · EV 175 · AC 178 → SPI 0.98 · CPI 0.98 · EAC ≈ 380.
#   final, 22 May: fit-out 231 · equipment + IT 49.1 · people 62.5 · marketing 37 = 379.6.
#   cash paid by month: Jan 4 · Feb 58 · Mar 141 · Apr 129 · May 47.6 = 379.6.

FIN = ["finance"]

# ------------------------------------------------------------------ 01 Whose Money Is It?
fm_problem = Doodle(760, 250, "Doodle of 27 January 2026. Sanne has been told the Rotterdam budget is 380 thousand euros. She asks Marco three questions and gets three surprises. Does it include our own engineers' time? No. Can I sign a purchase order? Not without a rule. Is it with or without VAT? Without. Nobody had written any of it down.",
                    "“The budget is €380k.” Three questions, three surprises: what's in it, who may spend it, with or without VAT.")
fm_problem.row([("our engineers' time?", "not in it", "pink"), ("may I sign orders?", "no rule yet", "pink"), ("with VAT?", "without", "y")], y=30, h=84, size=17, subsize=15)
fm_problem.note(380, 168, "a number with no rules attached", "red", size=20)
fm_problem.note(380, 206, "“€380k” meant different things to three people", "pen", size=17)

fm_analogy = Doodle(760, 240, "Doodle of a household holiday fund. Before anyone spends from it, the family agrees: what it covers (flights and hotel, not shopping), who can pay from it (either parent, up to a limit), how they keep track (every receipt in one envelope), and what the spare money is for.",
                    "A family holiday fund: what it covers, who may pay from it, and how receipts are kept.")
fm_analogy.row([("what it covers", "travel, not shopping", "y"), ("who may pay", "up to a limit", "blue"), ("how it's tracked", "one envelope", "green")], y=50, h=90, size=18, subsize=15)
fm_analogy.note(380, 196, "agreed before the first euro is spent", "pen", size=19)

fm_how = Doodle(760, 400, "The money rules Sanne agrees with Marco on 27 January 2026. What the budget covers: external spend and new store staff until opening, in euros excluding VAT. What it doesn't: Larder's own people's time, about 170 person-days, tracked separately; the e-bike lease and rent from opening, which are operations. Who may spend: Sanne up to five thousand euros within a budget line; Joost above that; Marco's veto on anything outside the budget. How it's counted: committed, spent and forecast, by line, every Friday. The reserve is drawn only through a logged change.",
                "Four boxes of rules, one page, signed by Marco before the first order.", exact=True)
for i, (t, items, f) in enumerate([("covers", ["external spend", "new store staff until opening", "€ excluding VAT"], "green"),
                                   ("doesn't cover", ["our own people's time (~170 days)", "e-bike lease, rent: operations"], "pink"),
                                   ("who may spend", ["Sanne: ≤ €5,000 within a line", "Joost: above that", "Marco: veto outside budget"], "y"),
                                   ("how it's counted", ["committed · spent · forecast", "by line, every Friday", "reserve: only by a change"], "blue")]):
    r, c = divmod(i, 2)
    x, y = 14 + c * 372, 14 + r * 176
    fm_how.box(x, y, 360, 160, None, f)
    fm_how.head(x + 180, y + 34, t, size=20)
    for k, it in enumerate(items):
        fm_how.text(x + 180, y + 72 + k * 30, it, size=16)
fm_how.note(380, 384, "signed: Marco, 27 January", "pen", size=17)

FIN_MGMT = dict(
    slug="financial-management",
    kicker="a.k.a. planning financial management",
    tldr="Before spending a euro, agree the <b>rules for the money</b>: what the budget <b>covers</b> (and what it doesn't), the <b>units</b> (with or without VAT, which currency), <b>who may spend</b> how much, how spending is <b>counted</b> (committed, spent, forecast) and <b>reported</b>, and how the <b>reserve</b> may be used. It fits on a page and takes an hour with the finance lead. Without it, one number, “the budget”, means something different to everyone who hears it.",
    chips=[("Family", "planning the money"), ("Lives in", "one page with the finance lead's signature"), ("Pairs with", "the charter, who decides what, the budget")],
    pmbok=dict(covers="how money will be estimated, budgeted, authorised, spent, counted and reported on the project",
               domains=FIN + ["governance"], processes=["Plan Financial Management"], principles=["Be an accountable leader"], focus=["planning"],
               older="6th: “Plan Cost Management” (7.1), the cost management plan. 7th: the Planning and Measurement domains. The 8th gives finance its own domain."),
    problem_side="Larder, 27 January 2026",
    problem="""  <p class="lead">Sanne has been told, more than once, that Rotterdam's budget is <b>€380k</b>. She asks Marco three questions. Does it include our own engineers' time? <b>No.</b> May I sign a purchase order? <b>There's no rule yet.</b> Is it with or without VAT? <b>Without</b>, which Joost had assumed the other way. <span class="hl-pink">The number was real. Nothing around it had been written down.</span></p>
  <ul>
    <li>“The budget” means different things to different people.</li>
    <li>Nobody knows who may commit money, or how much.</li>
    <li>Some real costs aren't in it at all, and nobody has said so.</li>
  </ul>""",
    problem_figs=[fm_problem],
    analogy_side="the holiday fund",
    analogy="""  <p>A family saving for a holiday agrees a few things before anyone spends from the fund: <b>what it covers</b> (travel and the hotel, not shopping), <b>who may pay</b> from it (either parent, up to a limit without asking the other), and <b>how they keep track</b> (every receipt in one envelope). Families that skip this don't argue about the holiday. They argue about the shoes.</p>""",
    analogy_figs=[fm_analogy],
    map=[("What the fund covers", "External spend and new store staff until opening"),
         ("Not the shopping", "Our engineers' time; the bike lease; rent"),
         ("Either parent, up to a limit", "Sanne up to €5,000 within a line; Joost above"),
         ("Receipts in one envelope", "Committed, spent and forecast, by line, every Friday"),
         ("The emergency twenty", "The reserve: only through a logged change")],
    how_side="one page of money rules, signed by the finance lead",
    how="""  <p>Sanne and Marco spend an hour and write one page. <b>Covers</b>: external spend and new store staff until opening, in <b>euros excluding VAT</b>. <b>Doesn't cover</b>: Larder's own people's time (about 170 person-days of engineers, Tomás's team and Sanne, which Marco tracks separately), the e-bike lease and rent from opening day (operations). <b>Who may spend</b>: Sanne up to €5,000 within a budget line, Joost above that, Marco with a veto on anything outside the budget. These are the same limits as the change triggers. <b>Counted</b> three ways, committed, spent and forecast, by line, every Friday. The <b>reserve</b> moves only through a logged change. Marco signs it. Joost, reading it, finally understands why his VAT-inclusive sums never matched.</p>""",
    how_figs=[fm_how],
    steps=[("Ask the finance lead what the number covers", "And what it doesn't."),
           ("Fix the units", "Currency; with or without VAT."),
           ("Write who may commit how much", "Match the change triggers."),
           ("Decide how money is counted", "Committed, spent, forecast."),
           ("Decide how and when it's reported", "By line, on a fixed day."),
           ("Write how the reserve may be used", "And get it signed.")],
    vocab=[("Budget", "The approved amount for the project, with its breakdown."),
           ("Commitment", "Money promised by an order or contract, even if not yet paid."),
           ("Actual cost", "Money for work done or goods received."),
           ("Internal cost", "The cost of the organisation's own people's time."),
           ("Delegated authority", "How much a person may commit without asking."),
           ("Excluding VAT", "Amounts without value-added tax, which a business usually reclaims.")],
    code=dict(file="rotterdam/31-money-rules.md", note="Sanne with Marco, 27 January 2026", plain=True, src="""
# ROTTERDAM · HOW WE HANDLE THE MONEY                           signed: Marco (CFO)

BUDGET        €380k, euros EXCLUDING VAT
COVERS        all external spend for the launch · recruiting and paid training of new
              store staff until opening day
NOT COVERED   Larder's own people's time (≈ 170 person-days; Marco tracks it separately)
              · e-bike lease and store rent from 27 April (operations budget)
WHO MAY SPEND Sanne      up to €5,000 per commitment, within a budget line
              Joost      above €5,000 (sponsor)
              Marco      veto on anything outside the budget · approves moves between lines
ORDERS        through Marco's team: a purchase order number before any supplier starts
COUNTED       committed (orders, contracts) · spent (work done, goods received) ·
              forecast (where each line will end), BY LINE, every Friday
RESERVE       €20k, drawn only through a logged change, never by moving lines quietly
REPORTS       Friday status (one line) · monthly to Marco (the table)
"""),
    tools="tools: an hour with the finance lead, one page, and the change triggers you already have.",
    dial=[("Light", "a small internal job", ["Ask: what does it cover, with or without VAT?", "Who may spend: you, up to a limit.", "A note in chat."]),
          ("Standard", "Rotterdam", ["One page of money rules.", "Spending limits matching the triggers.", "Three numbers, by line, weekly."]),
          ("Heavy", "large or public money", ["A cost management plan.", "Formal delegated financial authority.", "Audit trail and cost accounting codes."])],
    baseline="Each line compares <b>a budget number with nothing around it</b> to <b>one page of money rules, signed by the finance lead</b>.",
    ratings=[(3, 4, "Money is tied to what the launch needs."),
             (2, 4, "Everyone counts the same number the same way."),
             (2, 4, "Spending outside the rules is caught at the order."),
             (2, 5, "What's in and out of the budget is written."),
             (2, 5, "Marco signed the rules he'll judge by."),
             (3, 4, "Leads know their spending limit."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (4, 4, "One page, an hour.")],
    pitfalls=[("A number with no rules", "Everyone reads it differently.", "write what it covers."),
              ("Hidden costs", "Your own people's time isn't free.", "say what's excluded and who tracks it."),
              ("VAT confusion", "Sums that never match.", "fix the units."),
              ("No spending limits", "Every purchase becomes a meeting.", "delegate up to a threshold.")],
    use=["Before the first commitment.", "When you inherit a budget number.", "When finance and the sponsor read the budget differently.", "At the start of each phase with new money."],
    skip=["Never; for tiny jobs it's two sentences."],
    related=["<b>Who Decides What?</b> (vol. 2)", "<b>Should This Project Exist?</b> (vol. 2)", "<b>What Will It Cost?</b> (next note)", "<b>Cost-aware architecture</b> (Ana, vol. 5)"],
    quiz=[("Does Rotterdam's budget include Larder's own engineers' time?", "No. Marco tracks it separately (about 170 person-days)."),
          ("Up to how much may Sanne commit alone?", "€5,000 per commitment, within a budget line."),
          ("Name the three numbers counted every Friday.", "Committed, spent and forecast."),
          ("Joost wants to order €7,000 of signage. Who decides?", "Joost himself as sponsor (above €5,000), within the budget; Marco only if it's outside a line."),
          ("Priya asks to move €3k from marketing to people. What does Sanne do?", "Moves between lines need Marco's approval: she takes it to him with the reason.")],
    try_it="Ask your finance contact four questions about your project's budget: what does it cover, what doesn't it, with or without VAT, and who may commit how much? Write the answers on one page and ask them to sign it.",
    remember="Agree what the <span class=\"hl\">fund</span> covers before anyone buys <span class=\"hl\">shoes</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, planning financial management.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 7.1 Plan Cost Management.",
             "Project Management Institute, <i>Practice Standard for Project Estimating</i> (2nd ed., 2019)."],
)

# ------------------------------------------------------------------ 02 What Will It Cost?
ce_problem = Doodle(760, 250, "Doodle of 28 January 2026. The 380 thousand euros came from the top: Femke and Marco set it per city when the Series B closed. Nobody has checked it from the bottom, against what Rotterdam actually needs. Sanne asks: if we add up the pieces, do we land under 380 or over it?",
                    "€380k came from the top, per city. Nobody had added up the pieces from the bottom.")
ce_problem.box(230, 20, 300, 70, "top-down: €380k", "y", sub="per city, set in September", size=19, subsize=14)
ce_problem.row([("builder", "?", "paper"), ("cold room", "?", "paper"), ("equipment", "?", "paper"), ("people", "?", "paper"), ("marketing", "?", "paper")], y=120, h=70, size=16, subsize=18)
ce_problem.note(380, 226, "do the pieces add up to less, or more?", "red", size=19)

ce_analogy = Doodle(760, 240, "Doodle of planning a kitchen renovation. One number comes from a friend: kitchens cost about twenty thousand. Another comes from adding up the quotes: units, worktop, appliances, fitter. The friend's number tells you whether to start. The quotes tell you whether you can afford it.",
                    "“Kitchens cost about €20k” tells you whether to start. The quotes, added up, tell you whether you can afford it.")
ce_analogy.box(20, 40, 330, 100, "“about €20k”", "y", sub="a friend, from memory", size=20, subsize=15)
ce_analogy.box(410, 40, 330, 100, "quotes, added up", "blue", sub="units · worktop · fitter", size=20, subsize=15)
ce_analogy.note(185, 180, "top-down", "red", size=19)
ce_analogy.note(575, 180, "bottom-up", "red", size=19)

ce_how = Doodle(760, 400, "Sanne's bottom-up cost estimate for Rotterdam, 28 January 2026, by line, with where each number came from and how sure it is. Builder 148 thousand, from an indicative quote, plus or minus ten percent. Cold room and fridges 64 thousand, a firm quote. Equipment and store IT 48 thousand, catalogue prices. People 60 thousand: 40 hires at 1,500 euros each, 500 to recruit and 1,000 for paid induction and training, plus or minus twenty percent. Marketing 40 thousand, Priya's plan. Total 360 thousand: twenty under the top-down 380, which becomes the reserve.",
                "Five lines, each with its source and how sure. €360k from the bottom; €380k from the top. The gap becomes the reserve.", exact=True)
rows_ = [("builder", "indicative quote", "€148k", "± 10 %"), ("cold room + fridges", "firm quote", "€64k", "firm"), ("equipment + store IT", "catalogue", "€48k", "± 2 %"),
         ("people: 40 × €1,500", "€500 recruit + €1,000 training", "€60k", "± 20 %"), ("launch marketing", "Priya's plan", "€40k", "± 10 %")]
for i, (a, b, c, d) in enumerate(rows_):
    y = 14 + i * 56
    ce_how.box(14, y, 230, 46, a, "paper", size=16, rx=5)
    ce_how.text(260, y + 29, b, anchor="start", size=15)
    ce_how.box(520, y, 110, 46, c, "y", size=17, rx=5)
    ce_how.box(640, y, 106, 46, d, "blue", size=15, rx=5)
ce_how.box(14, 300, 340, 70, "bottom-up: €360k", "green", sub="sum of the five lines", size=19, subsize=14)
ce_how.box(406, 300, 340, 70, "top-down: €380k", "y", sub="gap €20k → the reserve", size=19, subsize=14)

COST = dict(
    slug="cost-estimates",
    kicker="a.k.a. estimating costs",
    tldr="A <b>cost estimate</b> puts a money figure on each piece of work. Build it <b>bottom-up</b> from the work breakdown (quotes, rates, catalogue prices) and check it against any <b>top-down</b> number you were given. Write, for every line, <b>where the number came from</b> and <b>how sure</b> it is. A quote you hold is firmer than a quote you expect; a rate times a guess is softer still. The gap between bottom-up and top-down is your first real piece of information about the budget.",
    chips=[("Family", "planning the money"), ("Lives in", "an estimate table: line, source, number, how sure"), ("Pairs with", "estimating methods, the WBS, the business case")],
    pmbok=dict(covers="estimating costs: top-down and bottom-up, quotes, rates, accuracy ranges, basis of estimate",
               domains=FIN, processes=["Estimate Costs"], principles=["Focus on value"], focus=["planning"],
               older="6th: “Estimate Costs” (7.2), the basis of estimates. 7th: estimating in the Planning domain."),
    problem_side="Larder, 28 January 2026",
    problem="""  <p class="lead">The €380k didn't come from Rotterdam. Femke and Marco set it <b>per city</b> when the Series B closed in September, from what Zuid had cost and a bit for being a new city. <span class="hl-pink">Nobody has added up what Rotterdam actually needs.</span> If the pieces come to €420k, the launch is underfunded from the start; if they come to €300k, there's money nobody has decided about.</p>
  <ul>
    <li>A top-down number says what someone hopes, not what the work costs.</li>
    <li>Without a breakdown, nobody can say which line is at risk.</li>
    <li>Estimates without sources can't be defended or improved.</li>
  </ul>""",
    problem_figs=[ce_problem],
    meanwhile=[("product-2", "business-case", "Grace's business case for approvals (12 Feb) counts engineers' time in money: 8 person-weeks × €6k ≈ €48k.",
                "Sanne's Rotterdam budget, by Marco's rule, leaves Larder's own people's time out and counts only external spend; both are right for their purpose.")],
    analogy_side="the kitchen renovation",
    analogy="""  <p>Planning a new kitchen, you get one number from a friend: <b>“kitchens cost about €20k.”</b> You get another by <b>adding up the quotes</b>: units, worktop, appliances, the fitter. The friend's number tells you whether to start. The quotes tell you whether you can afford it, and which line to argue about. If they differ a lot, the difference is the first thing to understand.</p>""",
    analogy_figs=[ce_analogy],
    map=[("“About €20k”", "€380k per city, set top-down in September"),
         ("Adding up the quotes", "Five lines, built from the work"),
         ("A quote in hand", "The cold room: €64k, firm"),
         ("A quote you expect", "The builder: €148k indicative, ± 10 %"),
         ("The difference", "€20k: the reserve")],
    how_side="five lines, each with its source and how sure",
    how="""  <p>Sanne builds the estimate <b>bottom-up</b> from the workstreams, writing the source next to every number. <b>Builder</b>: €148k from Kees's indicative quote, ± 10 %. <b>Cold room and fridges</b>: €64k, a firm quote. <b>Equipment and store IT</b>: €48k at catalogue prices. <b>People</b>: 40 hires at €1,500 each (€500 to recruit, €1,000 for paid induction and training), ± 20 %. <b>Marketing</b>: €40k, Priya's plan. Total: <b>€360k</b>, €20k under the top-down €380k. Sanne doesn't spend the gap. She proposes it as the <b>reserve</b>, and on 30 January the budget is €380k with €20k set aside. Marco confirms it on 6 February, now that he can see what's under it.</p>""",
    how_figs=[ce_how],
    steps=[("Start from the work breakdown", "A line per workstream or work package."),
           ("Price each line from the best source you have", "Quote, catalogue, rate × quantity."),
           ("Write the source and how sure", "Firm, ± 10 %, ± 20 %."),
           ("Add it up", "Bottom-up total."),
           ("Compare with any top-down number", "Understand the gap."),
           ("Decide what the gap is for", "Usually: the reserve.")],
    vocab=[("Cost estimate", "A money figure for a piece of work, with its basis."),
           ("Top-down estimate", "A total set from above or from a similar past project."),
           ("Bottom-up estimate", "The sum of estimates for the pieces."),
           ("Basis of estimate", "Where a number came from and what it assumes."),
           ("Indicative quote", "A supplier's price that isn't yet binding."),
           ("Accuracy range", "How far the real cost might be from the estimate.")],
    code=dict(file="rotterdam/32-cost-estimate.md", note="Sanne, 28 January 2026 · confirmed by Marco 6 February", plain=True, src="""
# ROTTERDAM · COST ESTIMATE (bottom-up, € excl. VAT)

LINE                    SOURCE                                   ESTIMATE   HOW SURE
Builder (fit-out)       Kees's indicative quote, 12 activities    148,000   ± 10 %
                        (fixed price signed 26 Feb: 148,000)
Cold room + fridges     supplier's firm quote                      64,000   firm
Equipment + store IT    catalogue: shelving, 30 handhelds,         48,000   ± 2 %
                        4 label printers, 2 terminals, chargers
People                  40 hires × €1,500 (€500 recruiting +       60,000   ± 20 %
                        €1,000 paid induction and training)
Launch marketing        Priya's plan (waitlist, local ads)         40,000   ± 10 %
                                                      BOTTOM-UP   360,000
TOP-DOWN (per city, Sept 2025)                                    380,000
GAP                                                                20,000   → proposed as the reserve
"""),
    tools="tools: the work breakdown, every quote you hold, a few rates you trust, and a column headed “source”.",
    dial=[("Light", "a small purchase", ["One quote, one number.", "Say how sure.", "No table."]),
          ("Standard", "Rotterdam", ["Bottom-up by line, with sources.", "Compared with the top-down figure.", "Accuracy per line."]),
          ("Heavy", "large or public projects", ["Estimates per work package with a basis-of-estimate document.", "Independent cost review.", "Estimate classes (from rough to definitive)."])],
    baseline="Each line compares <b>accepting a top-down number</b> to <b>a bottom-up estimate by line, with sources, compared with the top-down figure</b>.",
    ratings=[(3, 4, "Money follows the work it pays for."),
             (2, 4, "Each line has a source and a range."),
             (2, 4, "The softest line (people, ± 20 %) is known."),
             (2, 5, "Anyone can see what's under €380k."),
             (2, 4, "Marco confirmed the budget with the detail in front of him."),
             (3, 4, "Leads' quotes and plans are the basis."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "A day's work.")],
    pitfalls=[("Trusting the top-down number", "Underfunded, or slack nobody owns.", "add up the pieces."),
              ("No sources", "Can't be defended.", "a source next to every number."),
              ("Indicative treated as firm", "The quote moves.", "mark how sure each is."),
              ("Spending the gap", "The reserve disappears into lines.", "name it and set it aside.")],
    use=["When you're handed a budget number.", "Before asking for money.", "Before signing big contracts.", "At each phase, with better information."],
    skip=["Never; for tiny work, one quote and a range."],
    related=["<b>How Long, Roughly?</b> (vol. 3)", "<b>How Do We Break It Down?</b> (vol. 3)", "<b>Business case one-pager</b> (Grace, vol. 2)", "<b>How Much Do We Set Aside?</b> (next note)"],
    quiz=[("Top-down or bottom-up: €380k per city?", "Top-down."),
          ("Which line was softest, and why?", "People, ± 20 %: hiring costs and training time depend on who is hired."),
          ("What did Sanne do with the €20k gap?", "Proposed it as the reserve, set aside, not spread into lines."),
          ("On 24 Feb the builder offers a fixed price of €148k. What changes in the estimate?", "The builder line goes from indicative (± 10 %) to firm at the same €148k."),
          ("The bottom-up had come to €410k. What would Sanne do?", "Take the €30k gap to Joost and Marco before starting: more money, less scope, or a different plan.")],
    try_it="Build a bottom-up estimate of your project in five to ten lines, with a source and an accuracy for each. Compare it with the budget you were given. What is the gap, and who should decide what it's for?",
    remember="The friend's number tells you whether to <span class=\"hl\">start</span>. The quotes tell you whether you can <span class=\"hl\">afford</span> it.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, estimating costs.",
             "Project Management Institute, <i>Practice Standard for Project Estimating</i> (2nd ed., 2019).",
             "AACE International, Recommended Practice 18R-97: cost estimate classification."],
)

# ------------------------------------------------------------------ 03 How Much Do We Set Aside?
br_problem = Doodle(760, 250, "Doodle of 30 January 2026. Joost looks at the twenty thousand euro gap and has ideas: a nicer shop sign, a launch event, better uniforms. Marco looks at the same twenty thousand and asks what happens if the builder is late, if hiring costs more, if the cold room needs a part. Same money, two uses.",
                    "Joost sees €20k for a sign and an event. Marco sees €20k for when something goes wrong.")
br_problem.box(20, 40, 330, 100, "Joost", "y", sub="sign · event · uniforms", size=20, subsize=15)
br_problem.box(410, 40, 330, 100, "Marco", "blue", sub="late builder · hiring · parts", size=20, subsize=15)
br_problem.note(380, 186, "one €20k, two plans for it", "red", size=20)
br_problem.note(380, 222, "money with no name gets spent", "pen", size=18)

br_analogy = Doodle(760, 240, "Doodle of packing for a long car journey. The fuel tank is filled for the planned distance, plus a quarter of a tank for detours and traffic. The spare quarter isn't for a longer route chosen on a whim; it's for the things that might happen. And it has a gauge, so everyone sees how much is left.",
                    "Fuel for the route, plus a quarter tank for detours. The spare has a gauge, and isn't for a longer route on a whim.")
br_analogy.box(20, 50, 470, 80, "fuel for the planned route", "blue", size=19)
br_analogy.box(500, 50, 240, 80, "¼ for detours", "y", size=19)
br_analogy.note(380, 186, "the spare has a gauge, and a rule for using it", "pen", size=19)

br_how = Doodle(760, 400, "Rotterdam's cost baseline, spread over time, as approved on 30 January 2026 and confirmed on 6 February. A rising S-curve of planned spend by month: 4 thousand by the end of January, 64 by the end of February, 238 by the end of March, 352 by the end of April, 360 by the end of May. Above it a band of twenty thousand: the reserve, taking the total to 380.",
                "The planned spend as an S-curve: slow, steep through March and April, flat in May. The reserve sits on top.", exact=True)
x0, x1, y0, y1 = 80, 720, 30, 330
pts = [(0, 0), (1, 4), (2, 64), (3, 238), (4, 352), (5, 360)]
X = lambda m: x0 + m * (x1 - x0) / 5
Y = lambda v: y1 - v / 400 * (y1 - y0)
br_how.line(f"M{x0} {y0} V{y1} H{x1 + 10}", thin=True)
br_how.raw(f'<rect class="d f-y d-dash" x="{x0}" y="{Y(380):.0f}" width="{x1 - x0}" height="{Y(360) - Y(380):.0f}"/>')
br_how.note(x0 + 10, Y(380) - 8, "reserve €20k → €380k", "red", size=15, anchor="start")
br_how.line("M" + " L".join(f"{X(m):.0f} {Y(v):.0f}" for m, v in pts), color="pen")
for m, v in pts[1:]:
    br_how.circle(round(X(m)), round(Y(v)), 5, "blue")
    br_how.note(X(m) + 12, Y(v) + 18, f"{v}", size=15, anchor="start")
for m, t in enumerate(["", "end Jan", "end Feb", "end Mar", "end Apr", "end May"]):
    br_how.text(X(m), y1 + 22, t, "t t-soft", size=14)
for v in (100, 200, 300):
    br_how.text(x0 - 8, Y(v) + 5, f"{v}", "t t-soft", anchor="end", size=13)
br_how.note(x0 + 20, Y(300), "cumulative planned spend (€k)", "pen", size=15, anchor="start")

br_deep1 = Doodle(760, 330, "How a budget is stacked, from the bottom up. The work package estimates add up to the cost of each line; the lines add up to the cost baseline, 360 thousand euros for Rotterdam. Contingency for known risks sits on top, here the 20 thousand reserve, controlled by the project. A management reserve for unknown surprises would sit above that, controlled by the sponsor; Larder chose not to keep one for Rotterdam. Together they make the budget, 380 thousand.",
                  "Work packages → lines → cost baseline → contingency → (management reserve) → budget.", exact=True)
layers = [("work package estimates", "e.g. cold room €64k", "paper", 0), ("five lines", "builder · cold room · …", "blue", 1), ("cost baseline: €360k", "what the plan should cost", "blue", 2),
          ("contingency: €20k", "known risks · project controls it", "y", 3), ("management reserve: none", "unknowns · sponsor controls it", "paper", 4)]
for t, s, f, i in layers:
    w = 340 + i * 80
    x = 380 - w // 2
    y = 244 - i * 58
    br_deep1.box(x, y, w, 52, t, f, sub=s, size=16, subsize=12, dash=(i == 4))
br_deep1.note(380, 318, "budget = cost baseline + reserves = €380k", "pen", size=16)

BUDGET = dict(
    slug="budget-and-reserves",
    kicker="a.k.a. developing the budget: cost baseline, reserves and the S-curve",
    tldr="A <b>budget</b> is the cost estimates added up, plus <b>reserves</b>, spread over <b>time</b>. The estimates make the <b>cost baseline</b>: what the plan should cost if things go as planned. On top sits a <b>contingency reserve</b> for risks you know about, visible, with a rule for drawing on it, and sometimes a <b>management reserve</b> for surprises nobody can name, held by the sponsor. Spread over time, the baseline becomes an <b>S-curve</b>: slow start, steep middle, flat end. Money with no name gets spent; reserves need a name, a size and a gauge.",
    chips=[("Family", "planning the money"), ("Lives in", "the budget table, the S-curve, and the reserve line in every status"), ("Pairs with", "cost estimates, float and buffers, change control")],
    pmbok=dict(covers="aggregating estimates into a cost baseline; contingency and management reserves; time-phasing the budget; funding limits",
               domains=FIN + ["risk"], processes=["Develop Budget"], principles=["Be an accountable leader", "Focus on value"], focus=["planning"],
               older="6th: “Determine Budget” (7.3): cost baseline, contingency and management reserves, funding limit reconciliation. 7th: the Planning domain."),
    problem_side="Larder, 30 January 2026",
    problem="""  <p class="lead">The bottom-up estimate leaves <b>€20k</b> under the €380k. Joost sees it at once: a nicer shop sign, a launch event, better uniforms. Marco sees the same €20k and asks what happens if the builder is late, if hiring costs more, if the cold room needs a part nobody quoted. <span class="hl-pink">Same money, two plans for it.</span> If it isn't named and fenced today, it will be spent on the first good idea, and there'll be nothing left for the first bad day.</p>
  <ul>
    <li>Unnamed money gets spent.</li>
    <li>A total says nothing about when cash is needed.</li>
    <li>Nobody has said what the spare is for, or who may use it.</li>
  </ul>""",
    problem_figs=[br_problem],
    analogy_side="the spare quarter tank",
    analogy="""  <p>For a long car journey you fill the tank for the <b>planned route</b>, plus about a <b>quarter tank</b> for detours and traffic. The spare isn't for a longer route chosen on a whim; it's for the things that might happen. And it has a <b>gauge</b>: everyone in the car can see how much is left, and the driver says out loud when they start using it.</p>""",
    analogy_figs=[br_analogy],
    map=[("Fuel for the planned route", "The cost baseline: €360k"),
         ("The spare quarter", "The reserve: €20k (≈ 5.5 %)"),
         ("Not for a longer route on a whim", "Not for a sign, an event or uniforms"),
         ("The gauge", "“Reserve: €x left” in every Friday status"),
         ("Saying it out loud", "Drawn only through a logged change")],
    how_side="name the reserve, spread the baseline over time",
    how="""  <p>Sanne writes the budget in three layers. The <b>cost baseline</b>: the five lines, €360k. The <b>reserve</b>: €20k, for known risks. She lists the five things that could cost money (late builder, hiring above rate, a cold-room part, equipment prices, a lost week of training) and their likely total, about €10k; Marco doubles it for a first city. The rule: drawn <b>only through a logged change</b>, and reported every Friday. Then she spreads the baseline over the months from the plan: <b>€4k</b> by the end of January, <b>€64k</b> by February, <b>€238k</b> by March, <b>€352k</b> by April, <b>€360k</b> by May. That <b>S-curve</b> is what Marco needs for cash, and what earned value will measure against. Joost's sign, event and uniforms go on a list for the operations budget.</p>""",
    how_figs=[br_how],
    steps=[("Add the estimates into lines, and lines into a baseline", "What the plan should cost."),
           ("List the risks that would cost money", "And what each might cost."),
           ("Size a contingency reserve from them", "Visible, with a rule."),
           ("Decide whether the sponsor holds a management reserve", "For the unnamed."),
           ("Spread the baseline over time", "The S-curve."),
           ("Report the reserve every week", "A gauge everyone can read.")],
    vocab=[("Cost baseline", "The approved, time-phased budget excluding management reserve."),
           ("Contingency reserve", "Money for identified risks, controlled within the project."),
           ("Management reserve", "Money for unforeseen work, held by the sponsor or organisation."),
           ("Budget at completion (BAC)", "The total of the cost baseline."),
           ("S-curve", "Cumulative planned spend over time; usually slow, steep, then flat."),
           ("Funding limit", "How much money is available in a given period.")],
    code=dict(file="rotterdam/33-budget.md", note="30 January 2026 · confirmed by Marco 6 February", plain=True, src="""
# ROTTERDAM · BUDGET (€ excl. VAT)

COST BASELINE (BAC)                                                    360,000
  builder 148,000 · cold room + fridges 64,000 · equipment + IT 48,000 ·
  people 60,000 · marketing 40,000
RESERVE (contingency, project-controlled)                               20,000
  sized from: late builder ~5k · hiring above rate ~2.5k · cold-room part ~1k ·
  equipment prices ~0.5k · a lost week of training ~1k = ~10k likely; doubled
  for a first city (Marco)
  RULE  drawn only through a logged change · "reserve left" in every Friday status
MANAGEMENT RESERVE                                                        none
  (Larder's runway is the reserve for the unforeseen; Femke decides)
BUDGET                                                                 380,000

TIME-PHASED (cumulative planned spend, the S-curve)
  end Jan 4k · end Feb 64k · end Mar 238k · end Apr 352k · end May 360k
NOT FOR THE RESERVE   shop sign upgrade, launch event, uniforms → operations list
"""),
    tools="tools: the estimate table, the risk list, a spreadsheet for the S-curve, and a line in the status called “reserve left”.",
    deep_dive=dict(
        side="how a budget is stacked, sizing the reserve, and using it",
        intro="“Add a bit for contingency” is how most reserves are made, and why most disappear. This chapter shows the layers of a budget, a simple way to size a reserve from the risks you know, the S-curve and why finance cares about its shape, and Rotterdam's reserve from €20k to €0.4k.",
        parts=[
            ("The layers", """  <p>A budget stacks up in layers, each controlled by someone:</p>
  <ul>
    <li><b>Work package estimates</b> add up to <b>lines</b> (here, five).</li>
    <li>The lines add up to the <b>cost baseline</b>: what the plan should cost. Progress and earned value are measured against it.</li>
    <li>A <b>contingency reserve</b> covers risks you have named. The project manager manages it, by a rule.</li>
    <li>A <b>management reserve</b> covers surprises nobody can name. The sponsor holds it, outside the baseline.</li>
  </ul>
  <p>Larder chose not to keep a separate management reserve for Rotterdam: Femke treats the company's cash runway as that. It's a legitimate choice, and writing “none” makes it a decision rather than an oversight.</p>""", [br_deep1]),
            ("Sizing a reserve from the risks", """  <p>A percentage (“add 10 %”) is better than nothing. Better still is to list the risks that would <b>cost money</b> and put a rough likely cost on each: Rotterdam's five came to about <b>€10k</b>. Vol. 5 shows the proper sum (expected monetary value); the idea is already here: the reserve should be about the size of what's likely to go wrong, plus a margin for how new the work is.</p>
  <p>Marco doubled it because Rotterdam was the first new city. That judgment is the kind a finance lead is for. Writing both numbers down (€10k from the list, €20k chosen) means the next city can start from Rotterdam's real draws instead of a guess.</p>""", []),
            ("The S-curve, and why finance cares", """  <p>Spread over time, the baseline makes an <b>S</b>: a slow start (planning, deposits), a <b>steep middle</b> (March and April: the builder, the cold room, equipment, training) and a flat end (retention, final invoices). The steep part is what a CFO watches: <b>€174k in March alone</b> in Rotterdam's plan. If the company's cash is tight, the shape matters as much as the total.</p>
  <p>The S-curve is also the <b>planned value</b> line that earned value measures against (three notes on).</p>""", []),
            ("Using the reserve: the gauge", """  <p>Rotterdam's reserve went <b>€20k → €6k</b> (fridges with doors, 2 Feb), <b>→ €1k</b> (weekend work, 23 Mar), <b>→ €0.4k</b> (the 4G router, 1 Apr). Every draw was a logged change with a decider. None was a sign, an event or uniforms.</p>
  <p>Two habits made that work. The reserve had its own line in every Friday status, so the steering group watched it shrink in real time. And when it reached €1k, Sanne said in writing that it could no longer absorb a surprise, which turned the next problem into a decision for Joost instead of a quiet overspend.</p>""", []),
        ]),
    dial=[("Light", "small work", ["A total and a small spare.", "Say what the spare is for.", "No S-curve."]),
          ("Standard", "Rotterdam", ["Baseline by line, reserve sized from known risks.", "Monthly S-curve.", "Reserve reported weekly; drawn by change."]),
          ("Heavy", "large or public projects", ["Contingency per risk; management reserve held separately.", "Time-phased baselines by control account.", "Funding released in tranches against the curve."])],
    baseline="Each line compares <b>a total with €20k of unnamed slack</b> to <b>a baseline, a named reserve with a rule, and an S-curve</b>.",
    ratings=[(3, 4, "The reserve protects the launch, not extras."),
             (2, 4, "Monthly cash needs are known."),
             (2, 5, "The reserve covered three real draws."),
             (2, 5, "“Reserve left” is in every status."),
             (2, 5, "Marco sized it and watched it."),
             (3, 3, "Neutral."),
             (3, 4, "Surprises had money waiting."),
             (3, 3, "Neutral."),
             (3, 3, "A table and a curve.")],
    pitfalls=[("Unnamed slack", "Spent on the first idea.", "name it: reserve, with a rule."),
              ("Hidden padding in lines", "Nobody knows the real reserve.", "honest lines, one visible reserve."),
              ("Only a total", "Cash runs out in March.", "spread it over time."),
              ("No gauge", "The reserve vanishes quietly.", "report it every week.")],
    use=["After the cost estimate, before spending.", "When a gap appears between estimate and budget.", "When the sponsor asks for a cash forecast.", "At each new phase."],
    skip=["Tiny work with no real risk of overrun."],
    related=["<b>What Will It Cost?</b> (previous note)", "<b>How Much Can This Slip?</b> (vol. 3)", "<b>Can We Change That?</b> (vol. 2)", "<b>Contingency vs management reserve</b> (vol. 5)"],
    quiz=[("What is the cost baseline?", "The approved, time-phased budget without the management reserve: here €360k."),
          ("Contingency or management reserve: money for a late builder?", "Contingency: a known risk."),
          ("Why does Marco care about the S-curve's shape?", "Cash: €174k of planned spend in March alone."),
          ("Joost asks to pay for a nicer shop sign from the reserve. What does Sanne say?", "The reserve is for known risks, drawn by change; a sign is a wish for the operations budget list."),
          ("Trace Rotterdam's reserve from €20k.", "€20k → €6k (fridges) → €1k (weekend work) → €0.4k (router).")],
    try_it="Write your project's budget in three lines: baseline, reserve, total. List three risks that would cost money and roughly how much. Is your reserve about that size? Add a “reserve left” line to your next status.",
    remember="Fuel for the <span class=\"hl\">route</span>, a quarter tank for <span class=\"hl\">detours</span>, and a gauge everyone can read.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, developing the budget.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 7.3 Determine Budget.",
             "Project Management Institute, <i>Practice Standard for Earned Value Management</i> (2nd ed., 2011): the cost baseline."],
)

# ------------------------------------------------------------------ 04 When Does the Money Leave?
cf_problem = Doodle(760, 250, "Doodle of Friday 27 February 2026 and Sanne's mistake for this collection. The builder's contract, signed the day before, says twenty percent on signing. Kees expects the money within days to buy materials. Larder pays suppliers once a month, thirty days after the invoice. Kees phones: no money, no materials, no start on Monday 2 March.",
                    "“20 % on signing.” Kees expects it in days; Larder pays in thirty. “No money, no start on Monday.”")
cf_problem.box(20, 40, 330, 100, "contract: 20 % on signing", "y", sub="€29,600 · signed 26 Feb", size=17, subsize=14)
cf_problem.box(410, 40, 330, 100, "Larder pays", "paper", sub="once a month, 30 days after invoice", size=19, subsize=14)
cf_problem.note(380, 186, "Kees: “no money, no materials, no start on Monday”", "red", size=17)
cf_problem.note(380, 222, "the total was right; the timing wasn't", "pen", size=18)

cf_analogy = Doodle(760, 240, "Doodle of a household with a fixed monthly salary and a big holiday booked. The holiday is affordable over the year. But the deposit is due in March and the salary arrives at the end of the month. Being able to afford something and having the cash on the day are different questions.",
                    "Affordable over the year isn't the same as having the cash on the day the deposit is due.")
cf_analogy.box(20, 40, 330, 100, "affordable this year?", "green", sub="yes", size=19, subsize=17)
cf_analogy.box(410, 40, 330, 100, "cash on 3 March?", "pink", sub="salary comes on the 25th", size=19, subsize=15)
cf_analogy.note(380, 186, "two different questions", "pen", size=19)

cf_how = Doodle(760, 400, "Rotterdam's cash by month, planned on 27 February 2026 and paid in the end. January 4 thousand planned, 4 paid. February 58 and 58. March 138 planned, 141 paid. April 132 planned, 129 paid. May 48 planned, 47.6 paid. March and April together are about 270 thousand euros in nine weeks. Payment terms underneath: builder 20 percent on signing, 40 at first fix, 35 at handover, 5 percent retention; cold room 30 percent with the order, 70 on delivery; equipment on delivery, net 30.",
                "Cash by month: planned (outline) and paid (filled). Seventy percent of it leaves in March and April.", exact=True)
plan = [4, 58, 138, 132, 48]
paid = [4, 58, 141, 129, 47.6]
base, top = 290, 30
Yv = lambda v: (base - top) * v / 150
for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May"]):
    x = 70 + i * 135
    cf_how.box(x, round(base - Yv(plan[i])), 48, max(2, round(Yv(plan[i]))), None, "paper", dash=True, rx=2)
    cf_how.box(x + 54, round(base - Yv(paid[i])), 48, max(2, round(Yv(paid[i]))), None, "blue", rx=2)
    cf_how.text(x + 51, base + 22, m, "t t-soft", size=15)
    cf_how.note(x + 51, round(base - Yv(max(plan[i], paid[i]))) - 8, f"{plan[i]:g} / {paid[i]:g}", size=14)
cf_how.line(f"M50 {base} H730", thin=True)
cf_how.text(380, 344, "builder: 20 % signing · 40 % first fix · 35 % handover · 5 % retention", size=14)
cf_how.text(380, 368, "cold room: 30 % with order · 70 % on delivery · equipment: on delivery, net 30", size=14)
cf_how.note(380, 392, "€k planned / paid", "pen", size=14)

CASH = dict(
    slug="cash-flow",
    kicker="a.k.a. funding and cash flow",
    tldr="A budget answers <b>how much</b>; cash flow answers <b>when</b>. Money is <b>committed</b> when an order is signed, but it <b>leaves the bank</b> when invoices fall due, and suppliers' payment terms decide that: deposits, stage payments, retention, 30 days. Plan the cash by month with the finance lead, make sure the <b>funding</b> is there when the steep part comes, and never sign payment terms your organisation can't actually meet.",
    chips=[("Family", "planning the money"), ("Lives in", "a monthly cash table, agreed with finance"), ("Pairs with", "the budget's S-curve, sourcing, the contract")],
    pmbok=dict(covers="funding requirements, payment terms and cash flow over time; matching spending to available funds",
               domains=FIN, processes=["Develop Budget"], principles=["Adopt a holistic view"], focus=["planning", "executing"],
               older="6th: project funding requirements and funding limit reconciliation in 7.3. 7th: the Planning domain."),
    problem_side="Larder, 26 February → 2 March 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. The builder's contract, signed on <b>26 February</b>, says <b>20 % on signing</b>: €29,600. Sanne agreed it; it's normal. What she didn't check: Larder pays suppliers <b>once a month, 30 days after the invoice</b>. On Friday Kees phones: he needs the money to buy materials. <span class="hl-pink">No money, no materials, no start on Monday 2 March</span>, the first day on the critical path.</p>
  <ul>
    <li>The total was in the budget; the timing wasn't.</li>
    <li>Contract terms were agreed without the finance lead.</li>
    <li>A cash problem became a schedule problem in a day.</li>
  </ul>""",
    problem_figs=[cf_problem],
    analogy_side="the holiday deposit",
    analogy="""  <p>A family can afford a holiday over the year. But the <b>deposit is due on 3 March</b>, and the salary arrives on the 25th. “Can we afford it?” and “do we have the cash on the day?” are <b>different questions</b>. Households learn to ask the second one before they book.</p>""",
    analogy_figs=[cf_analogy],
    map=[("Affordable over the year", "€148k is in the budget"),
         ("Deposit due on 3 March", "20 % on signing, needed for materials"),
         ("Salary on the 25th", "Larder's monthly payment run, 30 days"),
         ("Asking before booking", "Checking payment terms with Marco before signing"),
         ("A planned cash calendar", "The monthly cash table")],
    how_side="plan cash by month, and check terms before signing",
    how="""  <p>Sanne phones Marco that afternoon and says it was her mistake. Marco makes an <b>exception payment</b> on Monday morning, and Kees starts on time. Then they fix the cause. Every contract's <b>payment terms</b> go into one table: the builder (20 % signing, 40 % at first fix, 35 % at handover, 5 % retention after the snags), the cold room (30 % with the order, 70 % on delivery), equipment (on delivery, net 30), recruiting per hire, marketing monthly. From that, a <b>cash plan by month</b>: €4k, €58k, €138k, €132k, €48k. About <b>€270k leaves in March and April</b>, which Marco needs to know for Larder's runway. And a rule: <b>no payment terms signed without Marco</b>. In the end the cash came within €3k of the plan every month.</p>""",
    how_figs=[cf_how],
    steps=[("Collect every contract's payment terms", "Deposits, stages, retention, days."),
           ("Turn them into cash by month", "With the finance lead."),
           ("Find the steep months", "And check the funding covers them."),
           ("Check your organisation's payment habits", "Monthly runs, approval steps."),
           ("Never sign terms finance can't meet", "Ask before, not after."),
           ("Compare plan and paid each month", "And explain the gaps.")],
    vocab=[("Cash flow", "Money actually coming in and going out, by date."),
           ("Payment terms", "When a supplier must be paid: on signing, on delivery, in 30 days."),
           ("Stage payment", "A payment due when a stage of work is complete."),
           ("Retention", "Part of the price held back until defects are fixed."),
           ("Funding", "The money made available, and when."),
           ("Runway", "How long the organisation's cash lasts at its current spending.")],
    code=dict(file="rotterdam/34-cash-plan.md", note="Sanne with Marco, 27 February 2026 · actuals added in May", plain=True, src="""
# ROTTERDAM · CASH BY MONTH (€k excl. VAT)

PAYMENT TERMS
  builder €148k        20 % on signing (26 Feb) · 40 % first fix done · 35 % handover ·
                       5 % retention, after the snags (paid 15 May)
  cold room €78k       30 % with order (13 Feb) · 70 % on delivery (27 Mar)
  equipment €48k       on delivery (16 Mar), net 30
  recruiting           per hire, on start · training wages: monthly
  marketing            agency, monthly
                        JAN    FEB    MAR    APR    MAY    TOTAL
  planned (27 Feb)        4     58    138    132     48     380
  paid                    4     58    141    129   47.6   379.6
  March + April ≈ €270k in nine weeks → Marco's runway forecast

MISTAKE   20 % on signing agreed without checking Larder's monthly payment run →
          exception payment Mon 2 Mar (Marco); builder started on time
RULE      no payment terms signed without Marco
"""),
    tools="tools: every contract's payment clause, a monthly table, and the finance lead before signing.",
    dial=[("Light", "a few small invoices", ["Ask finance when they'll be paid.", "Avoid deposits if you can.", "No table."]),
          ("Standard", "Rotterdam", ["A table of payment terms.", "Cash by month, planned and paid.", "No terms signed without finance."]),
          ("Heavy", "large contracts", ["Cash-flow forecasts by week.", "Funding released in tranches.", "Payment certificates and retention schedules."])],
    baseline="Each line compares <b>a total budget with no view of timing</b> to <b>a monthly cash plan from every contract's terms, agreed with finance</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "Cash timing no longer threatens dates."),
             (2, 4, "The steep months are known in February."),
             (2, 4, "Planned and paid, side by side."),
             (2, 5, "Marco can plan the runway."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "A table, kept monthly.")],
    pitfalls=[("Terms signed without finance", "No cash on the day.", "finance sees the terms first."),
              ("Total only", "The steep months surprise everyone.", "cash by month."),
              ("Commitment = payment", "They happen weeks apart.", "track both."),
              ("Forgetting retention", "A payment months later.", "put it in the table.")],
    use=["Before signing any contract with deposits or stages.", "When finance asks for a forecast.", "When the organisation's cash is tight.", "Monthly, until the last invoice."],
    skip=["Internal work with no external payments."],
    related=["<b>Make It, Buy It, or Hire It?</b> (vol. 2)", "<b>How Much Do We Set Aside?</b> (previous note)", "<b>Total cost of ownership</b> (Ana, vol. 5)", "<b>How Much Have We Spent?</b> (next note)"],
    quiz=[("Budget or cash flow: “can we afford it?”", "Budget. Cash flow asks: is the money there on the day?"),
          ("What caused the builder's problem on 27 Feb?", "20 % on signing was agreed, but Larder pays monthly, 30 days after invoice."),
          ("How much cash left in March and April?", "About €270k (141 + 129)."),
          ("When was the builder's retention paid?", "15 May, after the last snag was fixed."),
          ("The shelving supplier asks for 50 % up front. What does Sanne do?", "Check with Marco before agreeing; offer payment on delivery if the payment run can't meet it.")],
    try_it="List every supplier on your project with its payment terms. Turn them into a table of cash by month. Which month is steepest? Show it to your finance contact this week.",
    remember="Can we <span class=\"hl\">afford</span> it, and do we have the cash on the <span class=\"hl\">day</span>?",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, funding.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 7.3, funding requirements.",
             "Richard Brealey, Stewart Myers and Franklin Allen, <i>Principles of Corporate Finance</i> (14th ed., 2023): working capital."],
)

# ------------------------------------------------------------------ 05 How Much Have We Spent?
cs_problem = Doodle(760, 250, "Doodle of the steering group of 27 February 2026 and Sanne's mistake for this collection. Asked what Rotterdam has spent, she says 61 thousand euros, the figure Marco's team gave her two weeks earlier. Marco corrects her: 335 thousand is committed. The cold room was ordered on 13 February, the equipment on 23 February and the builder's contract was signed yesterday. Nearly nine tenths of the budget is promised.",
                    "“€61k spent.” Marco: “€335k committed.” Nearly nine tenths of the budget was already promised.")
cs_problem.box(20, 40, 330, 100, "Sanne: €61k", "y", sub="invoices received (13 Feb)", size=20, subsize=14)
cs_problem.box(410, 40, 330, 100, "Marco: €335k", "pink", sub="+ cold room · equipment · builder", size=20, subsize=14)
cs_problem.note(380, 186, "a sixth, or nine tenths?", "red", size=20)
cs_problem.note(380, 222, "one word, “spent”, two very different numbers", "pen", size=17)

cs_analogy = Doodle(760, 240, "Doodle of a credit card and a bank account. The bank balance shows money that has left. The card shows purchases not yet taken. The holiday booked for next month shows nowhere yet. To know what's really left, you need all three.",
                    "Bank balance, card purchases not yet taken, and the holiday already booked. You need all three.")
cs_analogy.row([("bank balance", "money gone", "blue"), ("card pending", "bought, not taken", "y"), ("booked holiday", "promised, not billed", "pink")], y=50, h=90, size=18, subsize=14)
cs_analogy.note(380, 196, "what's left = budget − all three", "pen", size=19)

cs_how = Doodle(760, 400, "Rotterdam's money table on Friday 27 March 2026, by line. Columns: budget, committed, spent, forecast. Builder: budget 148 plus 5 weekend work, committed 153, spent 96, forecast 153. Cold room: 78, 78, 78, 78. Equipment and store IT: 48, 48.5, 48.5, 48.5. People: 60, 45, 21, 62.5. Marketing: 40, 31, 22, 37. Totals: budget 378 plus reserve 1, committed 355.5, spent 265.5, forecast 379. Reserve 1 thousand.",
                "Four columns by line. Committed is far ahead of spent; the forecast is what matters.", exact=True)
hdr = ["line", "budget", "committed", "spent", "forecast"]
data = [("builder", "153", "153", "96", "153"), ("cold room", "78", "78", "78", "78"), ("equipment + IT", "48", "48.5", "48.5", "48.5"),
        ("people", "60", "45", "21", "62.5"), ("marketing", "40", "31", "22", "37"), ("total (+ reserve 1)", "379", "355.5", "265.5", "379")]
xs = [14, 270, 390, 510, 630]
for k, h in enumerate(hdr):
    cs_how.head(xs[k] + (0 if k == 0 else 55), 34, h, anchor="start" if k == 0 else "middle", size=16)
for i, row in enumerate(data):
    y = 50 + i * 48
    for k, v in enumerate(row):
        if k == 0:
            cs_how.box(14, y, 240, 40, v, "paper" if i < 5 else "y", size=15, rx=5)
        else:
            cs_how.box(xs[k], y, 110, 40, v, ["", "paper", "blue", "green", "y"][k] if i < 5 else "y", size=16, rx=5)
cs_how.note(380, 362, "people: committed 45 but forecast 62.5 (agency costs more than planned)", "red", size=15)
cs_how.note(380, 388, "€k excl. VAT · builder includes €5k weekend work (C-02)", "pen", size=14)

SPENT = dict(
    slug="committed-and-spent",
    kicker="a.k.a. monitoring finances: committed, actual and forecast",
    tldr="“How much have we spent?” has <b>three</b> honest answers. <b>Committed</b>: everything promised by an order or contract. <b>Spent</b> (actual cost): work done and goods received. <b>Forecast</b>: where each line will end. Report all three, <b>line by line</b>, against the budget, every week. Committed tells you how much freedom is left; spent tells you about progress; the forecast tells you whether you'll fit. One number labelled “spent” misleads everyone, usually in the comfortable direction.",
    chips=[("Family", "watching the money"), ("Lives in", "a four-column table by line, every Friday"), ("Pairs with", "money rules, earned value, status reports")],
    pmbok=dict(covers="tracking commitments, actual costs and forecasts against the budget; variance by line; reporting",
               domains=FIN, processes=["Monitor and Control Finances"], principles=["Be an accountable leader"], focus=["monitoring"],
               older="6th: “Control Costs” (7.4). 7th: the Measurement domain."),
    problem_side="Larder, 27 February 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. At the steering group of 27 February, Femke asks what Rotterdam has spent. Sanne says <b>€61k</b>, the figure Marco's team gave her on 13 February. Marco corrects her, gently: <b>€335k is committed</b>. The cold room (€78k) was ordered on 13 February, the equipment (€48k) on 23 February, and the builder's €148k contract was signed yesterday. <span class="hl-pink">Nearly nine tenths of the budget is already promised</span>; the €61k was only the recruiting and marketing contracts of mid-February.</p>
  <ul>
    <li>“Spent” was used for three different things.</li>
    <li>The comfortable number was the wrong one.</li>
    <li>A total hides which line is going wrong.</li>
  </ul>""",
    problem_figs=[cs_problem],
    analogy_side="the bank, the card and the booking",
    analogy="""  <p>To know how much you really have left this month, the <b>bank balance</b> isn't enough. There are <b>card purchases</b> not yet taken, and a <b>holiday already booked</b> that isn't billed yet. Each is real money. Someone who only looks at the bank balance always thinks they have more than they do.</p>""",
    analogy_figs=[cs_analogy],
    map=[("Bank balance", "Paid: cash out of the bank"),
         ("Card purchases pending", "Spent: work done, goods received, not yet paid"),
         ("The booked holiday", "Committed: orders and contracts signed"),
         ("What's left", "Budget minus committed"),
         ("Where the month will end", "Forecast, line by line")],
    how_side="four columns, by line, every Friday",
    how="""  <p>From the next Friday the money goes in a table of <b>four columns by line</b>: <b>budget</b>, <b>committed</b>, <b>spent</b> (work done or goods received) and <b>forecast</b>. Marco's team fills the first three from the orders and invoices; each line's lead gives the forecast. On <b>27 March</b>: committed €355.5k, spent €265.5k, forecast <b>€379k</b> against €379k (after the weekend work). The table shows what the total hid: <b>people</b> has €45k committed but a forecast of <b>€62.5k</b>, because the agency charges more per hire than planned; <b>marketing</b> will land at €37k, because Priya is holding €3k back. One line over, one under, and a reserve of €1k between them and trouble.</p>""",
    how_figs=[cs_how],
    steps=[("Separate committed, spent and paid", "Name each, every time."),
           ("Get committed and spent from finance", "Orders, contracts, invoices."),
           ("Get the forecast from each line's owner", "Where will it end?"),
           ("Show them by line against the budget", "Totals hide the problem line."),
           ("Explain every forecast variance", "Over or under, and why."),
           ("Report the reserve beside it", "What's left to absorb surprises.")],
    vocab=[("Committed cost", "Money promised by signed orders and contracts."),
           ("Actual cost (AC)", "Cost of work done and goods received so far."),
           ("Paid", "Cash that has left the bank."),
           ("Forecast (estimate at completion)", "Where a line, or the project, will end."),
           ("Cost variance (by line)", "Budget minus forecast."),
           ("Accrual", "Recording a cost when the work is done, not when it's paid.")],
    code=dict(file="rotterdam/35-money-table.md", note="Friday 27 March 2026 (from Marco's team and the line owners)", plain=True, src="""
# ROTTERDAM · MONEY BY LINE · 27 March 2026 (€k excl. VAT)

LINE                   BUDGET  COMMITTED  SPENT  FORECAST  VARIANCE  WHY
Builder (+C-02)          153      153       96      153        0     fixed price + weekend work
Cold room + fridges       78       78       78       78        0     delivered today
Equipment + store IT      48       48.5     48.5     48.5    -0.5    handhelds €500 dearer
People                    60       45       21       62.5    -2.5    agency charges €575 a
                                                                     hire, not €500
Marketing                 40       31       22       37      +3      Priya holds €3k back
TOTAL                    379      355.5    265.5    379        0
RESERVE                    1                                          (20 → 6 → 1)
PAID (cash out)                            219                        (see cash plan)

27 Feb CORRECTION   "€61k spent" (recruiting + marketing contracts, 13 Feb) → €335k committed
                    (+ cold room 78, 13 Feb · equipment 48, 23 Feb · builder 148, 26 Feb)
"""),
    tools="tools: a four-column table, Marco's team for the facts, each line's owner for the forecast.",
    dial=[("Light", "a small budget", ["Keep a list of what's ordered and what's arrived.", "One forecast number.", "Monthly."]),
          ("Standard", "Rotterdam", ["Budget, committed, spent, forecast, by line.", "Weekly.", "Variances explained."]),
          ("Heavy", "large projects", ["Cost accounts per work package.", "Accruals and commitments from the finance system.", "Monthly cost reports with variance analysis."])],
    baseline="Each line compares <b>one “spent” number</b> to <b>budget, committed, spent and forecast, line by line, every week</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "The forecast shows where the total will land."),
             (2, 4, "The people line's drift is caught in March."),
             (1, 5, "No more comfortable wrong numbers."),
             (2, 5, "Marco and Sanne report the same figures."),
             (3, 4, "Line owners give their own forecasts."),
             (3, 4, "Lines can be balanced before they overrun."),
             (3, 3, "Neutral."),
             (3, 3, "A table each Friday.")],
    pitfalls=[("One word, three meanings", "“Spent”.", "committed, spent, paid: name them."),
              ("Totals only", "The bad line hides.", "by line."),
              ("Forecast = budget", "Nobody really forecasts.", "the line owner gives a number and a reason."),
              ("Using finance's figure without the date", "Two weeks stale.", "date every number.")],
    use=["Every week once money is being committed.", "Before every steering group.", "When finance and project numbers differ.", "After any big contract is signed."],
    skip=["Never, once there's a budget."],
    related=["<b>Whose Money Is It?</b> (this volume)", "<b>Where Are We, Really?</b> (vol. 2)", "<b>Is the Money Buying Progress?</b> (next note)", "<b>Where Will the Money End Up?</b> (this volume)"],
    quiz=[("Committed, spent or paid: the builder's contract on the day it's signed?", "Committed (all €148k)."),
          ("Why was “€61k” misleading on 27 Feb?", "It was two weeks old and counted only the recruiting and marketing contracts; €335k was committed."),
          ("Which line was forecast over, and why?", "People, by €2.5k: the agency charges €575 a hire, not €500."),
          ("The total forecast equals the budget. Is everything fine?", "Not necessarily: people is over and marketing under. Look by line."),
          ("On 3 April Joost asks for €4k of extra training. What does Sanne check first?", "The people line's forecast (already €2.5k over) and the reserve (€1k): it needs a change for Joost to decide, with marketing's €3k as a possible source via Marco.")],
    try_it="For your project, write four numbers per budget line: budget, committed, spent, forecast. Which line's forecast differs most from its budget? Can its owner explain why in one sentence?",
    remember="Bank, card and <span class=\"hl\">booking</span>: what's left is the budget minus <span class=\"hl\">all three</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, monitoring and controlling finances.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 7.4 Control Costs.",
             "Harold Kerzner, <i>Project Management: A Systems Approach</i> (13th ed., 2022): cost control."],
)

# ------------------------------------------------------------------ 06 Is the Money Buying Progress?
ev_problem = Doodle(760, 250, "Doodle of Friday 20 March 2026. Marco has two pieces of good news that don't fit together. Spending is close to plan: 178 thousand against 178 planned. Progress, by the must-have count, is a little behind. He asks: if we're behind but spending on plan, are we paying more for less? Neither number alone can say.",
                    "Spending on plan, progress a little behind. “Are we paying more for less?” Neither number alone can say.")
ev_problem.box(20, 40, 330, 100, "spent: €178k", "green", sub="plan: €178k", size=20, subsize=15)
ev_problem.box(410, 40, 330, 100, "progress: behind", "y", sub="45 must-haves, plan ≈ 47", size=20, subsize=15)
ev_problem.note(380, 186, "Marco: “are we paying more for less?”", "red", size=19)
ev_problem.note(380, 222, "money and progress, in different units", "pen", size=18)

ev_analogy = Doodle(760, 240, "Doodle of a road trip with a fuel budget. Halfway through the planned time you've used half the fuel money. Good? Only if you've also covered half the distance. If you've driven only forty percent of the way, the money is going faster than the trip.",
                    "Half the fuel money gone at half time is only good news if you've covered half the distance.")
ev_analogy.row([("time used", "50 %", "paper"), ("fuel money used", "50 %", "y"), ("distance covered", "40 %?", "pink")], y=50, h=90, size=19, subsize=20)
ev_analogy.note(380, 196, "money only means something next to progress", "pen", size=19)

ev_how = Doodle(760, 400, "Earned value for Rotterdam on Friday 20 March 2026, against a budget of 374 thousand euros. Planned value: 178 thousand of work should have been done by now. Earned value: the work actually done is worth 175 thousand at budget prices. Actual cost: that work cost 178 thousand. Schedule variance minus 3 thousand, schedule performance index 0.98. Cost variance minus 3 thousand, cost performance index 0.98. Most of the gap is the people line: 34 of 40 hires done, at a higher price per hire.",
                "PV 178 · EV 175 · AC 178 (€k). A little behind, a little over, both by €3k: the people line.", exact=True)
x0, sc = 180, 540 / 374
for i, (t, v, f) in enumerate([("planned value (PV)", 178, "paper"), ("earned value (EV)", 175, "green"), ("actual cost (AC)", 178, "pink")]):
    y = 30 + i * 70
    ev_how.text(14, y + 30, t, anchor="start", size=16)
    ev_how.box(x0, y, round(v * sc), 46, f"€{v}k", f, size=17, rx=4)
ev_how.line(f"M{x0 + round(374 * sc)} 20 V240", color="red", dash=True)
ev_how.note(x0 + round(374 * sc) - 6, 254, "budget (BAC) €374k", "red", size=14, anchor="end")
ev_how.row([("SV = EV − PV", "−€3k · SPI 0.98", "y"), ("CV = EV − AC", "−€3k · CPI 0.98", "y")], x=60, y=280, h=80, w=300, gap=40, size=18, subsize=15)
ev_how.note(380, 388, "both gaps: people (34 of 40 hired, €575 a hire, not €500)", "red", size=14)

ev_deep1 = Doodle(760, 300, "The three earned value curves over time, drawn for Rotterdam up to 20 March 2026. Planned value follows the S-curve of the cost baseline. Earned value runs just below it. Actual cost runs just above earned value and close to planned value. The vertical gap between earned and planned is the schedule variance; between earned and actual, the cost variance. At the far right, the budget at completion: 374 thousand.",
                  "Three lines: what was planned, what was earned, what it cost. The gaps between them are the variances.", exact=True)
x0, x1, y0, y1 = 70, 700, 30, 260
mon = [(0, 0, 0, 0), (1, 4, 4, 4), (2, 64, 63, 64), (2.65, 178, 175, 178)]
X = lambda m: x0 + m * (x1 - x0) / 5
Y = lambda v: y1 - v / 400 * (y1 - y0)
ev_deep1.line(f"M{x0} {y0} V{y1} H{x1 + 10}", thin=True)
ev_deep1.line("M" + " L".join(f"{X(m):.0f} {Y(v):.0f}" for m, v in [(0, 0), (1, 4), (2, 64), (3, 238), (4, 352), (5, 360)]), dash=True)
ev_deep1.line("M" + " L".join(f"{X(m):.0f} {Y(e):.0f}" for m, p, e, a in mon), color="green")
ev_deep1.line("M" + " L".join(f"{X(m):.0f} {Y(a):.0f}" for m, p, e, a in mon), color="red")
ev_deep1.line(f"M{x0} {Y(374):.0f} H{x1}", thin=True, dash=True)
ev_deep1.note(x1, Y(374) - 8, "BAC 374", "red", size=14, anchor="end")
ev_deep1.note(X(2.65) + 10, Y(178) - 6, "PV 178 · AC 178", "red", size=14, anchor="start")
ev_deep1.note(X(2.65) + 10, Y(175) + 16, "EV 175", "green", size=14, anchor="start")
ev_deep1.note(X(3) + 20, Y(238) - 6, "planned (the S-curve)", size=14, anchor="start")
ev_deep1.text(X(2.65), y1 + 22, "20 Mar", "t t-soft", size=13)
for m, t in [(1, "end Jan"), (2, "end Feb"), (4, "end Apr"), (5, "end May")]:
    ev_deep1.text(X(m), y1 + 22, t, "t t-soft", size=13)

EV = dict(
    slug="earned-value",
    kicker="a.k.a. earned value management (EVM)",
    tldr="<b>Earned value</b> puts progress and money in the same unit. Three numbers: <b>planned value</b> (PV), the budget for the work that should be done by now; <b>earned value</b> (EV), the budget for the work actually done; and <b>actual cost</b> (AC), what that work really cost. EV − PV says if you're <b>ahead or behind</b>; EV − AC says if you're <b>over or under</b> on cost. Divide instead of subtract and you get two indices, <b>SPI</b> and <b>CPI</b>: 1.0 is on plan. Spending on plan means nothing until you know what was earned.",
    chips=[("Family", "watching the money"), ("Lives in", "three numbers and two ratios, once a month (or on a key date)"), ("Pairs with", "the budget's S-curve, status reports, forecasting")],
    pmbok=dict(covers="earned value: planned value, earned value, actual cost; schedule and cost variances and indices",
               domains=FIN + ["schedule"], processes=["Monitor and Control Finances"], principles=["Focus on value", "Be an accountable leader"], focus=["monitoring"],
               older="6th: earned value analysis in 7.4 (Control Costs). 7th: the Measurement domain."),
    problem_side="Larder, 20 March 2026",
    problem="""  <p class="lead">Marco has two pieces of news that don't fit. <b>Spending</b> is close to plan: about €178k of work paid for or received, against €178k planned by now. <b>Progress</b>, on Sanne's must-have count, is a little behind: 45 done, the plan line is about 47. He asks: <b>“if we're behind but spending on plan, are we paying more for less?”</b> <span class="hl-pink">Neither number alone can say</span>: one is in euros, the other in must-haves.</p>
  <ul>
    <li>Spending on plan can mean on plan, or overpaying for less.</li>
    <li>Progress and money are counted in different units.</li>
    <li>The comfortable answer (“on budget”) may be wrong.</li>
  </ul>""",
    problem_figs=[ev_problem],
    analogy_side="fuel money on a road trip",
    analogy="""  <p>Halfway through the planned time of a road trip, you've used <b>half the fuel money</b>. Good news? Only if you've also covered <b>half the distance</b>. If you've driven only 40 % of the way, the money is going faster than the trip, and at this rate you'll run short before you arrive. Money spent only means something next to progress made.</p>""",
    analogy_figs=[ev_analogy],
    map=[("The fuel money planned by halfway", "Planned value: €178k"),
         ("The distance covered, in fuel money", "Earned value: €175k"),
         ("The fuel money actually used", "Actual cost: €178k"),
         ("Behind on distance", "SV −€3k, SPI 0.98"),
         ("Paying more per kilometre", "CV −€3k, CPI 0.98")],
    how_side="three numbers on 20 March, line by line",
    how="""  <p>Sanne and Marco work it out by line, at budget prices, against the <b>€374k</b> cost baseline (€360k plus the fridge upgrade). <b>Planned value</b>: by 20 March the builder should have done €90k of work, equipment €48k, recruiting €20k, marketing €20k: <b>€178k</b>. <b>Earned value</b>: the builder is exactly on its activities (€90k; the inspector's re-booking is three days away), equipment delivered (€48k), <b>34 of 40</b> hires made (€17k), marketing on plan (€20k): <b>€175k</b>. <b>Actual cost</b>: builder €90k (fixed price), equipment €48.5k, recruiting €19.5k, marketing €20k: <b>€178k</b>. So: a little behind (SV −€3k, SPI 0.98) and a little over (CV −€3k, CPI 0.98), <b>both in the people line</b>. Marco's answer: yes, slightly more for slightly less, and only in hiring. Sanne asks the agency for a fixed fee for the last six hires.</p>""",
    how_figs=[ev_how],
    steps=[("Use the time-phased budget as planned value", "The S-curve."),
           ("Measure work done in budget money: earned value", "By work package or line."),
           ("Get actual cost for that work", "Not commitments, not cash."),
           ("Subtract: SV = EV − PV, CV = EV − AC", "Negative is bad."),
           ("Divide: SPI = EV ÷ PV, CPI = EV ÷ AC", "Below 1 is bad."),
           ("Find the line causing it", "Then act there.")],
    vocab=[("Planned value (PV)", "The budget for work scheduled to be done by now."),
           ("Earned value (EV)", "The budget for work actually done by now."),
           ("Actual cost (AC)", "What the work done actually cost."),
           ("Schedule variance (SV)", "EV − PV. Negative: behind."),
           ("Cost variance (CV)", "EV − AC. Negative: over cost."),
           ("SPI and CPI", "EV ÷ PV and EV ÷ AC. Below 1.0: behind, or over cost."),
           ("Budget at completion (BAC)", "The total cost baseline: €374k here.")],
    code=dict(file="rotterdam/36-earned-value.md", note="Sanne and Marco, Friday 20 March 2026 (BAC = €374k)", plain=True, src="""
# ROTTERDAM · EARNED VALUE · 20 March 2026 (€k, budget prices)

LINE                  BUDGET    PV     EV     AC    HOW EV WAS MEASURED
Builder                 148     90     90     90    activities A–F done or in progress
                                                    (fixed price: AC = EV by contract)
Cold room + fridges      78      0      0      0    earned on delivery (27 Mar)
Equipment + store IT     48     48     48    48.5   delivered 16 Mar
People (recruiting part) 60     20     17    19.5   34 of 40 hired × €500 budget each
Marketing                40     20     20     20    waitlist open 16 Mar, creative done
TOTAL                   374    178    175    178

SV  = EV − PV = −3      SPI = EV ÷ PV = 0.98   a little behind (people)
CV  = EV − AC = −3      CPI = EV ÷ AC = 0.98   a little over   (people, equipment)
ACTION  agency asked for a fixed fee for the last 6 hires (agreed: €500 each)
NEXT    forecast where this ends (see: where will the money end up?)
"""),
    tools="tools: the S-curve, a way to measure work done in budget money, and actual costs from finance.",
    deep_dive=dict(
        side="the three curves, measuring “earned”, fixed prices, and the limits",
        intro="Earned value has a reputation for being heavy. Its core is three numbers you can work out on one page, as Rotterdam's shows. This chapter draws the curves, explains how to measure “earned” honestly, shows what happens with a fixed-price contract, and says what earned value can't see.",
        parts=[
            ("Three curves", """  <p>Plot the three numbers over time. <b>Planned value</b> follows the budget's S-curve. <b>Earned value</b> rises as work is done. <b>Actual cost</b> rises as money is spent on that work.</p>
  <ul>
    <li>EV <b>below</b> PV: behind schedule (in money terms).</li>
    <li>AC <b>above</b> EV: over cost for what's been done.</li>
    <li>On 20 March Rotterdam's three lines are almost on top of each other: a small, explainable gap.</li>
  </ul>""", [ev_deep1]),
            ("Measuring “earned” honestly", """  <p>Earned value is only as good as the way “done” is counted. Three rules that kept Rotterdam's honest:</p>
  <ul>
    <li><b>0 / 100 for small items</b>: equipment is earned when it arrives, not when it's ordered.</li>
    <li><b>Units completed</b> where work is countable: 34 of 40 hires = 34 × €500.</li>
    <li><b>Activity progress</b> for the builder, from the network: an activity half done earns half its value, judged with Kees on site, not from his invoice.</li>
  </ul>
  <p>Never earn from money spent (“we've spent 60 %, so we're 60 % done”). That makes CPI 1.0 by definition and hides exactly what earned value is for.</p>""", []),
            ("Fixed-price contracts", """  <p>With a fixed price, Larder pays the builder for work done at contract prices, so for that line <b>AC equals EV</b> and the cost variance is zero by construction. The builder's own costs can overrun; that's the builder's risk, which is why the contract is fixed. What earned value still shows for that line is <b>schedule</b>: EV against PV. That was the one to watch, and three days later the inspector proved it.</p>""", []),
            ("What earned value can't see", """  <ul>
    <li><b>Which work</b> was done. Earning €3k on the wrong activities while the critical path waits looks fine in money. Use the critical path alongside it.</li>
    <li><b>Quality</b>. Rushed, wrong work earns as much as good work until someone rejects it.</li>
    <li><b>Value to the customer</b>. EV measures progress against the plan, not whether the plan is still worth doing.</li>
  </ul>
  <p>Used once a month (or on a key date), with these limits said out loud, three numbers answer Marco's question better than any amount of colour.</p>""", []),
        ]),
    dial=[("Light", "small work", ["Ask: what fraction is done, what fraction is spent?", "Compare.", "No indices."]),
          ("Standard", "Rotterdam", ["PV, EV and AC by line on a key date.", "SV, CV, SPI, CPI.", "Find the line behind the gap."]),
          ("Heavy", "large contracts", ["Earned value system by control account.", "Monthly EV reports to the client.", "Formal thresholds for SPI and CPI."])],
    baseline="Each line compares <b>“spending on plan” with progress counted separately</b> to <b>planned value, earned value and actual cost in one unit, by line</b>.",
    ratings=[(3, 4, "Money is judged by the work it bought."),
             (2, 4, "SPI and CPI feed a forecast."),
             (2, 4, "The people line's drift is caught at 0.98, not 0.80."),
             (2, 5, "Progress and money in one unit."),
             (2, 5, "Marco's question gets a one-line answer."),
             (3, 3, "Neutral."),
             (3, 4, "Action goes to the line that causes the gap."),
             (3, 3, "Neutral: EV can't see quality."),
             (3, 3, "An hour with finance on a key date.")],
    pitfalls=[("Earning from spending", "CPI always 1.0.", "measure work done, not money spent."),
              ("Commitments as actual cost", "Everything looks over.", "AC is work done or goods received."),
              ("Indices without lines", "0.98 of what?", "find the line behind the gap."),
              ("EV instead of the critical path", "Right money, wrong work.", "use both.")],
    use=["When someone asks “are we paying more for less?”", "On key dates and monthly on larger projects.", "Before forecasting the final cost.", "With mixed predictive and countable work."],
    skip=["Purely adaptive work: use the burn-up and velocity instead."],
    related=["<b>How Much Do We Set Aside?</b> (this volume: the S-curve)", "<b>Are We Still on Time?</b> (vol. 3)", "<b>Where Will the Money End Up?</b> (next note)", "<b>Where Are We, Really?</b> (vol. 2)"],
    quiz=[("PV 178, EV 175, AC 178. What are SV and CV?", "SV = −3, CV = −3 (€k)."),
          ("And SPI and CPI?", "175 ÷ 178 ≈ 0.98 for both."),
          ("Why is the builder's CV zero?", "Fixed price: Larder pays contract value for work done, so AC = EV for that line."),
          ("A team says “we've spent 60 %, so we're 60 % done”. What's wrong?", "That's earning from spending: CPI becomes 1.0 by definition and hides overruns."),
          ("Earned value shows SPI 1.0, but the critical path is late. Is the project on schedule?", "No: non-critical work is ahead and hides it. Check the critical path alongside EV.")],
    try_it="For your project on today's date, estimate three numbers: the budget for the work that should be done by now (PV), the budget for the work actually done (EV), and what it cost (AC). Work out SPI and CPI. Which line explains most of the gap?",
    remember="Half the <span class=\"hl\">fuel money</span> is only good news at half the <span class=\"hl\">distance</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, monitoring and controlling finances.",
             "Project Management Institute, <i>Practice Standard for Earned Value Management</i> (2nd ed., 2011).",
             "Quentin Fleming and Joel Koppelman, <i>Earned Value Project Management</i> (4th ed., 2010)."],
)

# ------------------------------------------------------------------ 07 Where Will the Money End Up?
fc_problem = Doodle(760, 250, "Doodle of 27 March 2026. Two people forecast the final cost two ways. Marco, from the earned value index: 374 divided by 0.98 is about 380 thousand: the whole reserve gone. Sanne, line by line with each owner: 379 thousand. They agree on the total and disagree completely on why.",
                    "Marco's formula: ≈ €380k. Sanne's lines: €379k. Same total, different reasons.")
fc_problem.box(20, 40, 330, 100, "formula: BAC ÷ CPI", "y", sub="374 ÷ 0.98 ≈ €380k", size=19, subsize=15)
fc_problem.box(410, 40, 330, 100, "line by line", "blue", sub="owners' forecasts: €379k", size=19, subsize=15)
fc_problem.note(380, 186, "close totals, different stories", "red", size=20)
fc_problem.note(380, 222, "which one should the steering group believe?", "pen", size=17)

fc_analogy = Doodle(760, 240, "Doodle of two ways to forecast a phone bill at the end of the month. One: halfway through, you've used half the allowance faster than usual, so multiply. Two: look at what you'll actually do in the rest of the month: the trip abroad next week, the quiet weekend. The first is quick; the second knows things the formula doesn't.",
                    "Forecasting a phone bill: multiply the pace so far, or think about what's coming. Use both.")
fc_analogy.box(20, 40, 330, 100, "multiply the pace", "y", sub="quick · knows only the past", size=19, subsize=14)
fc_analogy.box(410, 40, 330, 100, "think ahead", "blue", sub="the trip next week · the quiet weekend", size=19, subsize=13)
fc_analogy.note(380, 186, "compare them; explain the difference", "pen", size=19)

fc_how = Doodle(760, 400, "The two forecasts side by side. By formula, from 20 March: budget 374 divided by CPI 0.98 is about 380 thousand, using the whole 6 thousand reserve, driven by hiring costs. Line by line on 27 March: builder 153 including weekend work, cold room 78, equipment 48.5, people 62.5, marketing 37, total 379 after the weekend work. The actual final cost on 22 May: 379.6 thousand. The formula was right about the total and wrong about the reasons: the reserve went on the weekend work and the router, not on hiring.",
                "Formula ≈ €380k, lines €379k, actual €379.6k. The formula saw the total; the lines saw the reasons.", exact=True)
fc_how.row([("formula, 20 Mar", "374 ÷ 0.98 ≈ 380", "y"), ("lines, 27 Mar", "153+78+48.5+62.5+37 = 379", "blue"), ("actual, 22 May", "379.6", "green")], y=20, h=96, size=18, subsize=14)
fc_how.box(14, 150, 732, 110, None, "paper")
fc_how.head(380, 178, "why the reserve went", size=18)
fc_how.text(380, 210, "formula's guess: hiring keeps overrunning (CPI 0.98)", size=15)
fc_how.text(380, 238, "real draws: weekend work €5k (23 Mar) · router €0.6k (1 Apr)", size=15)
fc_how.row([("ETC", "EAC − AC", "paper"), ("VAC", "BAC − EAC", "paper"), ("TCPI", "(BAC−EV) ÷ (BAC−AC)", "paper")], y=290, h=76, size=18, subsize=13)

FORECAST = dict(
    slug="cost-forecasting",
    kicker="a.k.a. forecasting final cost: EAC, ETC, VAC and TCPI",
    tldr="Two ways to forecast where the money will end up. <b>By formula</b>: assume the cost performance so far continues, so the estimate at completion (EAC) ≈ budget ÷ CPI. Quick, objective, blind to what's coming. <b>Bottom-up</b>: each line's owner forecasts from what they know (the trip next week, the quiet weekend). Do <b>both</b> and explain the difference. Then say what's left to spend (ETC), how far over or under you'll land (VAC) and how efficiently the rest must go to fit (TCPI).",
    chips=[("Family", "watching the money"), ("Lives in", "one line in the status: forecast, and against what"), ("Pairs with", "earned value, committed and spent, status reports")],
    pmbok=dict(covers="forecasting final cost: estimate at completion by formula and bottom-up; estimate to complete; variance at completion; to-complete performance index",
               domains=FIN, processes=["Monitor and Control Finances"], principles=["Be an accountable leader"], focus=["monitoring"],
               older="6th: forecasting (EAC, ETC, VAC, TCPI) in 7.4. 7th: the Measurement domain."),
    problem_side="Larder, 20–27 March 2026",
    problem="""  <p class="lead">Two forecasts reach the steering group of 27 March. <b>Marco</b>, from earned value: €374k ÷ 0.98 ≈ <b>€380k</b>, the whole reserve gone, because hiring keeps costing more. <b>Sanne</b>, line by line with each owner: <b>€379k</b> after the weekend work. <span class="hl-pink">The totals are close. The stories behind them are completely different</span>, and the steering group will act on the story, not the number.</p>
  <ul>
    <li>A formula only knows the past.</li>
    <li>Owners know what's coming, and can be optimistic.</li>
    <li>A forecast without its reasons can't be acted on.</li>
  </ul>""",
    problem_figs=[fc_problem],
    analogy_side="the phone bill",
    analogy="""  <p>Halfway through the month you've used your phone allowance faster than usual. One forecast: <b>multiply the pace</b>; you'll be over. Another: <b>think about what's coming</b>: a trip abroad next week (worse), a quiet weekend (better). The first is quick and knows only the past. The second knows things the formula can't. Sensible people do both and look at why they differ.</p>""",
    analogy_figs=[fc_analogy],
    map=[("Multiplying the pace", "EAC = BAC ÷ CPI ≈ €380k"),
         ("Thinking about what's coming", "Owners' line forecasts: €379k"),
         ("The trip abroad", "The weekend work: €5k from the reserve"),
         ("The quiet weekend", "Marketing holding €3k back"),
         ("The final bill", "€379.6k on 22 May")],
    how_side="two forecasts, one explanation",
    how="""  <p>Sanne puts both forecasts on one page. <b>Formula</b> (20 March): EAC ≈ €374k ÷ 0.98 ≈ <b>€380k</b>; variance at completion ≈ −€6k, the whole reserve as it then stood. <b>Line by line</b> (27 March): builder €153k (including the €5k weekend work), cold room €78k, equipment €48.5k, people €62.5k, marketing €37k: <b>€379k</b>. Then she explains the gap: the formula assumes hiring keeps overrunning; the owners know the agency has agreed a fixed fee for the last hires and marketing is holding €3k back. The steering group gets one sentence: <b>“we'll land at about €379k–€380k; the reserve is nearly gone; any new cost needs a decision.”</b> On 22 May the actual was <b>€379.6k</b>. The formula had the total right and the reasons wrong: the reserve went on the weekend work and the router, not on hiring.</p>""",
    how_figs=[fc_how],
    steps=[("Forecast by formula: EAC = BAC ÷ CPI", "Quick, objective."),
           ("Forecast bottom-up with each line's owner", "What's coming."),
           ("Put them side by side", "Explain the difference."),
           ("Work out ETC and VAC", "What's left to spend; over or under."),
           ("Check TCPI", "How efficient the rest must be to fit."),
           ("Report one range and the reason", "And what it means for decisions.")],
    vocab=[("Estimate at completion (EAC)", "The expected final cost."),
           ("EAC by CPI", "BAC ÷ CPI: assumes cost performance stays as it is."),
           ("Bottom-up EAC", "Actual cost so far + a fresh estimate of what's left."),
           ("Estimate to complete (ETC)", "EAC − AC: what's still to spend."),
           ("Variance at completion (VAC)", "BAC − EAC: the expected over- or underspend."),
           ("To-complete performance index (TCPI)", "(BAC − EV) ÷ (BAC − AC): the efficiency needed on the rest to finish on budget.")],
    code=dict(file="rotterdam/37-cost-forecast.md", note="Sanne and Marco, 27 March 2026 · actual added 22 May", plain=True, src="""
# ROTTERDAM · WHERE WILL THE MONEY END UP? (€k)

BY FORMULA (from 20 Mar: BAC 374, EV 175, AC 178, CPI 0.98)
  EAC  = BAC ÷ CPI = 374 ÷ 0.983      ≈ 380      VAC = BAC − EAC ≈ −6  (the whole reserve)
  ETC  = EAC − AC                     ≈ 202
  TCPI = (374 − 175) ÷ (374 − 178)    = 1.015    the rest must be 1.5 % more efficient

BY LINE (27 Mar, owners' forecasts, after the weekend work C-02)
  builder 153 · cold room 78 · equipment + IT 48.5 · people 62.5 · marketing 37  = 379

WHY THEY DIFFER   formula assumes hiring keeps overrunning; owners know the agency fee is
                  now fixed for the last 6 hires and marketing holds €3k back
TO THE STEERING   "about €379k–€380k; the reserve is nearly gone; any new cost needs a
                  decision"
ACTUAL (22 May)   379.6 — the reserve went on weekend work (5) and the router (0.6)
"""),
    tools="tools: the earned value numbers, each line owner's forecast, and one sentence for the steering group.",
    dial=[("Light", "small budgets", ["Ask the owner where it will end.", "One number with a reason.", "Monthly."]),
          ("Standard", "Rotterdam", ["Formula and line-by-line, side by side.", "ETC, VAC, TCPI.", "One sentence for the steering group."]),
          ("Heavy", "large contracts", ["Several EAC formulas (CPI, CPI × SPI).", "Independent EAC review.", "Formal re-baselining when VAC passes a threshold."])],
    baseline="Each line compares <b>one forecast number with no reasons</b> to <b>a formula forecast and an owners' forecast, side by side, with the difference explained</b>.",
    ratings=[(3, 4, "Decisions are made on where the money will end."),
             (2, 5, "Two methods catch each other's blind spots."),
             (2, 4, "The empty reserve was forecast in March."),
             (2, 4, "The reasons travel with the number."),
             (2, 5, "The steering group gets one honest sentence."),
             (3, 4, "Line owners own their forecasts."),
             (3, 4, "New costs became decisions, not overruns."),
             (3, 3, "Neutral."),
             (3, 3, "An hour a month.")],
    pitfalls=[("Formula only", "Blind to what's coming.", "ask the owners too."),
              ("Owners only", "Optimism.", "check against the formula."),
              ("A number without reasons", "Nobody knows what to do.", "explain the difference."),
              ("Forecast = budget", "Every month.", "a real number, even if uncomfortable.")],
    use=["Monthly, and after any big change.", "When the reserve is getting small.", "Before a steering group decision about money.", "Once earned value is available."],
    skip=["Tiny budgets with nothing left to buy."],
    related=["<b>Is the Money Buying Progress?</b> (previous note)", "<b>How Much Have We Spent?</b> (this volume)", "<b>Where Are We, Really?</b> (vol. 2)", "<b>Can We Change That?</b> (vol. 2)"],
    quiz=[("BAC 374, EV 175, AC 178. EAC by formula?", "CPI = 175 ÷ 178 ≈ 0.983, so EAC = 374 ÷ 0.983 ≈ €380k."),
          ("What does a TCPI above 1 mean?", "The rest of the work must be done more efficiently than planned to finish on budget."),
          ("Why did the two forecasts differ?", "The formula assumed hiring would keep overrunning; the owners knew the agency fee was now fixed and marketing was holding €3k back."),
          ("What was the actual final cost?", "€379.6k."),
          ("In April the formula says €385k and the owners say €378k. What does Sanne do?", "Ask which owner forecast is hopeful and which risk the formula is seeing; report a range with the reason, and treat €385k as possible until explained.")],
    try_it="Forecast your project's final cost two ways: budget ÷ CPI, and each owner's estimate for their line. Put them side by side. Write one sentence explaining the difference.",
    remember="Multiply the <span class=\"hl\">pace</span>, then think about what's <span class=\"hl\">coming</span>. Explain the gap.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, forecasting.",
             "Project Management Institute, <i>Practice Standard for Earned Value Management</i> (2nd ed., 2011): EAC, ETC, TCPI.",
             "David Christensen, “Using the Earned Value Cost Management Report to Evaluate the Contractor's Estimate at Completion” (1999)."],
)

# ------------------------------------------------------------------ 08 Was It Worth It?
pb_problem = Doodle(760, 250, "Doodle of 22 May 2026, the day the project closes. The closing report says 379.6 thousand euros against a budget of 380. Femke reads it and asks the question the report doesn't answer: and what do we get back for it, and when?",
                    "“€379.6k of €380k.” Femke: “And what do we get back for it, and when?”")
pb_problem.box(20, 40, 330, 100, "closing report", "green", sub="€379.6k of €380k", size=20, subsize=15)
pb_problem.box(410, 40, 330, 100, "Femke", "y", sub="“what do we get back, and when?”", size=20, subsize=14)
pb_problem.note(380, 186, "on budget says nothing about worth", "red", size=20)
pb_problem.note(380, 222, "the investment, next to what it brings back", "pen", size=18)

pb_analogy = Doodle(760, 240, "Doodle of buying solar panels for a house. They cost six thousand euros. They save about a hundred euros a month on electricity. They pay for themselves in five years, and keep saving for twenty. Whether the installer was on budget is a small part of the story.",
                    "Solar panels: €6,000, saving €100 a month. They pay for themselves in five years.")
pb_analogy.row([("cost", "€6,000", "pink"), ("saving", "€100 a month", "green"), ("payback", "5 years", "y")], y=50, h=90, gap=34, size=19, subsize=18, arrows=True)
pb_analogy.note(380, 196, "worth = what comes back, and how soon", "pen", size=19)

pb_how = Doodle(760, 400, "Marco's payback sum for Rotterdam, 22 May 2026. Investment 379.6 thousand euros. Each order contributes about four euros after picking, delivery and store costs. In week four Rotterdam did 590 orders a day; Marco assumes 550 a day from June. That is about 66 thousand euros a month. Payback about six months: around December 2026. And the value of speed: each week earlier a city opens is worth about 15 thousand euros, so the playbook's eight-week target for Utrecht is worth about 100 thousand compared with Rotterdam's fifteen weeks.",
                "€379.6k back at about €66k a month: paid back by about December 2026. Speed is worth €15k a week.", exact=True)
pb_how.row([("investment", "€379.6k", "pink"), ("per order", "≈ €4 contribution", "blue"), ("orders a day", "550 (590 in week 4)", "blue"), ("per month", "≈ €66k", "green")], y=20, h=90, gap=34, size=17, subsize=14, arrows=True)
pb_how.box(14, 140, 732, 90, "payback ≈ 6 months of steady trade → about December 2026", "y", size=18)
pb_how.box(14, 256, 732, 100, None, "green")
pb_how.head(380, 284, "the value of speed", size=18)
pb_how.text(380, 316, "a week earlier ≈ 7 × 550 × €4 ≈ €15k · Utrecht in 8 weeks, not 15 ≈ €100k", size=15)
pb_how.note(380, 384, "assumptions: Marco's, written down, checked again at Utrecht", "pen", size=15)

PAYBACK = dict(
    slug="payback",
    kicker="a.k.a. measuring financial value: payback, ROI and NPV",
    tldr="Being on budget says how well money was <b>controlled</b>, not whether it was <b>worth spending</b>. Put the investment next to what the result brings back. <b>Payback</b>: how long until the money returns. <b>Return on investment</b>: how much comes back per euro. <b>Net present value</b>: what future money is worth today. Use the simplest one your sponsor trusts, write the assumptions down, and check them later. Often the most useful number is the value of <b>time</b>: what each week earlier is worth.",
    chips=[("Family", "watching the money"), ("Lives in", "the business case before; the closing report and benefit reviews after"), ("Pairs with", "what is it all for?, the business case, benefits")],
    pmbok=dict(covers="financial value of the project: payback, return on investment, net present value; the value of time; checking value after delivery",
               domains=FIN, processes=["Monitor and Control Finances"], principles=["Focus on value"], focus=["closing", "monitoring"],
               older="6th: payback, ROI, NPV and IRR in the business documents (1.2.6). 7th: the principle “focus on value” and the Measurement domain."),
    problem_side="Larder, 22 May 2026",
    problem="""  <p class="lead">The closing report says <b>€379.6k of €380k</b>. The steering group is pleased. Femke reads it twice and asks the question it doesn't answer: <b>“and what do we get back for it, and when?”</b> <span class="hl-pink">On budget says nothing about worth.</span> A launch that cost exactly what was planned could still never pay for itself.</p>
  <ul>
    <li>Budget control and value are different questions.</li>
    <li>The value arrives after the project closes.</li>
    <li>Nobody has written down the sum the investors will ask about.</li>
  </ul>""",
    problem_figs=[pb_problem],
    meanwhile=[("architect-5", "total-cost-of-ownership", "Ana's total cost of ownership weighs a system's costs over three years, not just to build it.",
                "Sanne's payback weighs Rotterdam's €379.6k against what it brings back each month: the same long view, for money coming in.")],
    analogy_side="solar panels",
    analogy="""  <p>Solar panels for a house cost <b>€6,000</b> and save about <b>€100 a month</b>. They pay for themselves in <b>five years</b> and keep saving for twenty. Whether the installer finished on budget matters, but it's a small part of the story. The question that decided the purchase was how long until they pay back, and how sure you are about the saving.</p>""",
    analogy_figs=[pb_analogy],
    map=[("€6,000 for the panels", "€379.6k for the launch"),
         ("€100 a month saved", "≈ €4 per order × 550 a day ≈ €66k a month"),
         ("Five years to pay back", "About six months: December 2026"),
         ("How sure is the saving?", "Marco's assumptions, written down"),
         ("Installing them sooner", "Each week earlier a city opens ≈ €15k")],
    how_side="the investment, what comes back, and the value of speed",
    how="""  <p>Sanne asks Marco for the sum and writes it into the closing report. <b>Investment</b>: €379.6k. Each Rotterdam order contributes about <b>€4</b> after picking, delivery and store costs (Marco's figure). In week four Rotterdam did <b>590 orders a day</b>; Marco assumes <b>550</b> from June. That's about <b>€66k a month</b>, so the launch pays back in about <b>six months of steady trade: around December 2026</b>. Then the number that matters most for the next city: <b>each week earlier a city opens is worth about €15k</b> (7 × 550 × €4). Opening Utrecht in eight weeks instead of Rotterdam's fifteen is worth about <b>€100k</b>, which is what the playbook is for. The assumptions are written down, with a date to check them: the start of Utrecht.</p>""",
    how_figs=[pb_how],
    steps=[("Write down the investment", "All of it, including reserve draws."),
           ("Estimate what comes back per period", "From the business's own numbers."),
           ("Work out payback", "Investment ÷ return per period."),
           ("Work out the value of a week", "What speed is worth."),
           ("Write the assumptions", "And who owns each."),
           ("Check them later", "At a named date.")],
    vocab=[("Payback period", "How long until the money returned equals the investment."),
           ("Return on investment (ROI)", "Gain from the investment, compared with its cost."),
           ("Net present value (NPV)", "Future cash flows discounted to today's money, minus the investment."),
           ("Contribution", "What each sale leaves after its variable costs."),
           ("Cost of delay", "What waiting costs per week."),
           ("Benefit review", "A later check of whether the value arrived.")],
    code=dict(file="rotterdam/38-payback.md", note="Marco and Sanne, 22 May 2026 · check again at the start of Utrecht", plain=True, src="""
# ROTTERDAM · WAS IT WORTH IT?

INVESTMENT              €379,600 (incl. €19,600 of reserve draws)
RETURN                  contribution ≈ €4 per order (after picking, delivery, store costs)
                        orders: 590 a day in week 4 · assume 550 a day from June
                        ≈ 550 × €4 × 30 ≈ €66,000 a month
PAYBACK                 €379.6k ÷ €66k ≈ 5.8 months → about DECEMBER 2026
VALUE OF SPEED          a week earlier ≈ 7 × 550 × €4 ≈ €15,400
                        Utrecht in 8 weeks instead of Rotterdam's 15 ≈ €100k
NOT COUNTED             our own people's time (≈ 170 person-days) · rent and lease
                        (operations) · the brand value of a second city
ASSUMPTIONS             €4 contribution (Marco) · 550 a day holds (Joost) ·
                        no price war with the Rotterdam rival (Priya)
CHECK AGAIN             start of Utrecht (with the Rotterdam benefits review)
"""),
    tools="tools: the closing cost, the business's own contribution figure, a calculator, and a date to check.",
    dial=[("Light", "small changes", ["One sentence: what it saves or earns, and when.", "No discounting.", "Checked once."]),
          ("Standard", "Rotterdam", ["Payback from the business's own figures.", "The value of a week.", "Assumptions with owners and a check date."]),
          ("Heavy", "large investments", ["NPV and IRR over several years.", "Sensitivity analysis.", "Formal benefits realisation reviews."])],
    baseline="Each line compares <b>“on budget” as the last word</b> to <b>the investment next to what it brings back, with payback, the value of speed and written assumptions</b>.",
    ratings=[(2, 5, "Worth, not just control, is reported."),
             (3, 4, "A payback date to check."),
             (2, 4, "Assumptions are written and owned."),
             (2, 4, "Investors' question answered in the report."),
             (2, 5, "Femke got her answer."),
             (3, 3, "Neutral."),
             (3, 4, "The value of speed shapes the next city."),
             (3, 3, "Neutral."),
             (4, 4, "One sum with finance.")],
    pitfalls=[("On budget = success", "Worth is never asked.", "put the return next to the cost."),
              ("Invented returns", "Nobody believes them.", "use the business's own figures."),
              ("No assumptions", "Can't be checked.", "write them, with owners."),
              ("Never checked again", "The sum stays a hope.", "a named date to check.")],
    use=["In the business case before.", "In the closing report after.", "When choosing between projects.", "When arguing for speed."],
    skip=["Mandatory work (law, safety) where the choice isn't financial."],
    related=["<b>What Is It All For?</b> (vol. 1)", "<b>Business case one-pager</b> (Grace, vol. 2)", "<b>Cost of delay</b> (Grace, vol. 2)", "<b>Total cost of ownership</b> (Ana, vol. 5)"],
    quiz=[("€379.6k back at €66k a month. Payback?", "About 5.8 months."),
          ("What is a week earlier worth for a new city?", "About €15k (7 days × 550 orders × €4)."),
          ("What isn't counted in the investment?", "Larder's own people's time, rent and lease, brand value."),
          ("Why write the assumptions down?", "So they can be checked later: the €4, the 550 a day, the rival's prices."),
          ("At Utrecht's start Rotterdam is doing 420 a day, not 550. What changes?", "Payback stretches to about 7½ months; the benefits review says why, and Joost owns the order assumption.")],
    try_it="For your project, write three numbers: what it cost, what it brings back per month, and what a week earlier would be worth. Write the assumptions and who owns each. When will you check them?",
    remember="On budget is the <span class=\"hl\">installer's</span> story. Payback is the <span class=\"hl\">house's</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Finance domain, value.",
             "Project Management Institute, <i>Benefits Realization Management: A Practice Guide</i> (2019).",
             "Donald Reinertsen, <i>The Principles of Product Development Flow</i> (2009): cost of delay."],
)

NOTES = [FIN_MGMT, COST, BUDGET, CASH, SPENT, EV, FORECAST, PAYBACK]
