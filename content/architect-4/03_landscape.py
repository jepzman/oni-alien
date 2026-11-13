# Series 2 · The Solution Architect's Notebook · Vol. 4 · The landscape.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Capability Map
cm_problem = Doodle(760, 280, "Doodle of the March 2027 board meeting. The board asks: are we ready for four more cities, a new country and more business clients this year? Ana has a list of systems and a list of projects. Neither answers the question, because the question is about what Larder must be able to do, not which software it runs.",
                    "“Are we ready for 2027?” A list of systems and a list of projects can't answer it.")
cm_problem.box(20, 30, 220, 160, None, "paper")
cm_problem.head(130, 60, "systems", size=17)
for i, t in enumerate(["Larder Core", "Dispatch", "WMS B", "billing"]):
    cm_problem.text(130, 94 + i * 24, t, size=14)
cm_problem.box(270, 30, 220, 160, None, "paper")
cm_problem.head(380, 60, "projects", size=17)
for i, t in enumerate(["warehouse move", "Business API", "Utrecht", "Antwerp"]):
    cm_problem.text(380, 94 + i * 24, t, size=14)
cm_problem.box(520, 50, 220, 120, "the board", "y", sub="“ready for 2027?”")
cm_problem.note(380, 250, "the question is about abilities, not software", "red")

cm_analogy = Doodle(760, 250, "Doodle of a hospital's list of services: emergency care, maternity, cardiology, imaging, pharmacy. It doesn't say which building, team or machine provides each; it says what the hospital must be able to do. Planning a new wing starts from that list, coloured by how ready each service is.",
                     "A hospital plans from its services (emergency, maternity, imaging), not from its buildings.")
cm_analogy.icon("badge", 40, 50, 1.4)
for i, (t, f) in enumerate([("emergency", "green"), ("maternity", "green"), ("cardiology", "y"), ("imaging", "pink"), ("pharmacy", "green")]):
    cm_analogy.box(150 + i * 120, 70, 110, 60, t, f, size=13)
cm_analogy.note(450, 200, "what it must do, coloured by readiness", "pen")

cm_how = Doodle(760, 380, "Larder's capability map, 1 March 2027, coloured for 2027's needs. Seven areas: sell, fulfil, deliver, serve, business clients, expand, run. Green, ready; yellow, needs work; red, not ready. Red: localisation for French and Dutch, Belgian compliance (VAT and e-invoicing), city setup without code (three hard-coded settings left). Yellow: stock management (mid-migration), van routing, business ordering self-service. The rest green. The board saw five boxes to fund, not sixty projects.",
                 "What Larder must be able to do, independent of systems, coloured by how ready it is for 2027.")
areas = [("sell", [("catalogue", "green"), ("pricing", "green"), ("ordering", "green")]),
         ("fulfil", [("stock", "y"), ("picking", "green"), ("swaps", "green")]),
         ("deliver", [("couriers", "green"), ("vans", "y"), ("tracking", "green")]),
         ("serve", [("support", "green"), ("refunds", "green"), ("comms", "green")]),
         ("business", [("accounts", "green"), ("self-service", "y"), ("invoicing", "green")]),
         ("expand", [("city setup", "pink"), ("languages", "pink"), ("BE rules", "pink")]),
         ("run", [("finance", "green"), ("people", "green"), ("data", "y")])]
for i, (area, caps) in enumerate(areas):
    x = 8 + i * 107
    cm_how.box(x, 14, 100, 40, area, "paper", size=14, rx=4)
    for k, (c, f) in enumerate(caps):
        cm_how.box(x, 66 + k * 64, 100, 54, None, f, rx=4)
        cm_how.text(x + 50, 98 + k * 64, c, size=13)
for i, (f, t) in enumerate([("green", "ready"), ("y", "needs work"), ("pink", "not ready for 2027")]):
    cm_how.box(120 + i * 200, 280, 22, 16, None, f, rx=3)
    cm_how.text(150 + i * 200, 294, t, anchor="start", size=14)
cm_how.note(380, 340, "5 boxes to fund, not 60 projects", "green", size=17)

CAPABILITY = dict(
    slug="capability-map",
    kicker="a.k.a. “the hospital's list of services”",
    tldr="A <b>capability map</b> lists what the business must be <b>able to do</b> (sell, fulfil, deliver, serve, expand), in a few levels, <b>independent of systems, teams and projects</b>. It changes slowly, so it's a stable frame for big questions. <b>Colour it</b> for the question at hand (readiness for next year, cost, risk), and the conversation moves from “which projects?” to “which abilities are weak?”. Then map systems and projects onto it.",
    chips=[("Family", "the landscape"), ("Origin", "business capability modelling (enterprise architecture; BIZBOK, TOGAF)"), ("Lives in", "one page, coloured per question, reviewed yearly"), ("Pairs with", "application portfolio, architecture roadmap, business drivers")],
    problem_side="Larder, 1 March 2027",
    problem="""  <p class="lead">At the March board meeting an investor asks Ana: <i>is Larder ready for four more cities, a new country and more business clients this year?</i> Ana has a <b>list of systems</b> and a <b>list of projects</b>. Neither answers the question, because <span class="hl-pink">the question is about what Larder must be able to do</span>, not which software it runs or which projects are underway.</p>
  <ul>
    <li>Systems lists answer “what do we run?”, not “what can we do?”.</li>
    <li>Project lists mix the important with the merely active.</li>
    <li>Executives can't see where the weak spots are.</li>
  </ul>""",
    problem_figs=[cm_problem],
    analogy_side="the hospital's services",
    analogy="""  <p>A hospital plans from its <b>services</b>: emergency care, maternity, cardiology, imaging, pharmacy. The list doesn't say which building, team or machine provides each; it says what the hospital must be <b>able to do</b>. When it plans a new wing, it colours the list: which services are ready, which need investment. Buildings come after.</p>""",
    analogy_figs=[cm_analogy],
    map=[("The list of services", "Larder's capabilities: sell, fulfil, deliver, serve, expand…"),
         ("Not the buildings", "Independent of systems, teams and projects"),
         ("Colouring for a new wing", "Readiness for 2027's cities and country"),
         ("A red service", "Localisation, Belgian rules, city setup"),
         ("Buildings come after", "Systems and projects mapped onto the weak capabilities")],
    how_side="what we must do, coloured by readiness",
    how="""  <p>Ana drew <b>seven areas</b> with three capabilities each and coloured them for 2027 with Femke, Joost and Grace in an hour. <b>Red</b>: languages (French and Dutch), Belgian rules (VAT, e-invoicing), city setup without code. <b>Yellow</b>: stock (mid-migration), vans, business self-service, data. The board saw <b>five boxes to fund</b>, not sixty projects, and asked better questions: why is city setup still red after ADR 0003?</p>""",
    how_figs=[cm_how],
    steps=[("List level-1 capabilities", "Five to eight areas of what the business does, as nouns or verbs."),
           ("Break into level 2", "Three to six capabilities each; stop there for most uses."),
           ("Keep systems out", "No product names; a capability outlives any system."),
           ("Colour for one question", "Readiness, cost, risk, strategic importance: one at a time."),
           ("Agree colours with the business", "Not the architect alone; an hour with the people who know."),
           ("Map systems and projects onto it", "Which systems serve which capability; where projects land.")],
    vocab=[("Capability", "Something the business must be able to do."),
           ("Capability map", "The structured list of capabilities, in levels."),
           ("Heat map", "A capability map coloured for one question."),
           ("Level 1 / level 2", "Broad areas / the capabilities inside them."),
           ("Capability gap", "A capability that isn't good enough for what's needed."),
           ("Business architecture", "Describing the business itself: capabilities, value streams.")],
    code=dict(file="docs/landscape/capability-map-2027.md", note="Larder's capability map, coloured for 2027 (excerpt)", plain=True, src="""
# Capability map · coloured for 2027 readiness (Femke, Joost, Grace, Ana · 1 Mar 2027)
●ready  ◐needs work  ○not ready

SELL      catalogue ●  pricing ●  ordering ●
FULFIL    stock ◐ (WMS B migration)  picking ●  substitutions ●
DELIVER   couriers ●  vans ◐ (ADR 0015 in progress)  tracking ●
SERVE     support ●  refunds ●  customer comms ●
BUSINESS  accounts ●  self-service ◐ (Business API v1 in May)  invoicing ●
EXPAND    city setup ○ (3 hard-coded settings, TD-1)  languages ○ (FR, NL)
          Belgian rules ○ (VAT, e-invoicing, Bancontact refunds)
RUN       finance ●  people ●  data ◐

To fund in 2027: city setup · languages · Belgian rules · stock · vans
"""),
    tools="tools: a table or a grid of boxes; enterprise architecture tools (LeanIX, Ardoq, Archi with ArchiMate) for larger maps; industry reference models as a starting point.",
    gains=["<b>A stable frame</b> for big questions.",
           "<b>Executives see weak spots</b> at a glance.",
           "<b>Investment by ability</b>, not by loudest project.",
           "<b>Systems and projects get context</b>.",
           "<b>Shared language</b> between business and IT."],
    losses=["<b>Abstract</b> for some audiences.",
            "<b>Easy to over-model</b> (level 4, 300 boxes).",
            "<b>Colours are judgement</b>.",
            "<b>Needs refreshing</b> when the business changes."],
    baseline="Each line compares <b>answering “are we ready?” with lists of systems and projects</b> to <b>a capability map of what the business must do, coloured for the question</b>.",
    ratings=[(1, 5, "One page shows what Larder must be able to do."),
             (2, 5, "Femke, Joost and Grace coloured it with Ana."),
             (2, 4, "The board picked five boxes to fund."),
             (2, 4, "Red capabilities surfaced months before Antwerp."),
             (3, 4, "Capabilities stay stable as systems change."),
             (3, 3, "Neutral."),
             (2, 4, "Investment follows weak capabilities."),
             (3, 4, "An hour to colour; yearly review."),
             (3, 3, "Neutral.")],
    pitfalls=[("Systems as capabilities", "“WMS B” on the map.", "write what the business does, not what it runs."),
              ("Too many levels", "300 boxes nobody reads.", "level 2 is enough for most questions."),
              ("Colouring alone", "The architect's opinion in colour.", "colour with the business."),
              ("One map, all questions", "Colours mean five things.", "one colouring per question.")],
    use=["Annual planning and board questions about readiness.",
         "New markets, mergers, big programmes.",
         "Deciding where to invest or cut.",
         "Mapping applications and projects to purpose."],
    skip=["Small teams with one product.",
          "Detailed design: too coarse."],
    related=["<b>Application portfolio (TIME)</b> (this volume)", "<b>Architecture roadmap</b> (Vol. 3)", "<b>Business drivers &amp; goals</b> (Vol. 1)", "<b>Product strategy on a page</b> (Grace, book 2 vol. 2)"],
    quiz=[("What does a capability map describe?", "What the business must be able to do, independent of systems and projects."),
          ("Why keep systems off it?", "Capabilities outlive systems; the map stays stable."),
          ("What does colouring add?", "An answer to one question, e.g. readiness for 2027."),
          ("Which Larder capabilities were red?", "City setup, languages and Belgian rules.")],
    try_it="List your organisation's five to eight main capabilities and three to five under each. Colour them with two business people for one question (readiness for next year). Compare the red boxes with your current project list.",
    remember="Plan from the <span class=\"hl\">services</span>, not the buildings. Colour for <span class=\"hl\">one question</span>.",
    sources=["Business Architecture Guild, <i>BIZBOK Guide</i>, capability mapping.",
             "Ulrich Homann, “A Business-Oriented Foundation for Service Orientation” (Microsoft, 2006).",
             "The Open Group, <i>TOGAF Standard</i>, business capabilities.",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020)."],
)

# ------------------------------------------------------------------ 10 Application Portfolio (TIME)
ap_problem = Doodle(760, 280, "Doodle of July 2027. Marco asks how many applications Larder pays for. Nobody knows: the answer turns out to be twenty-three, about 61,000 euros a month, including two tools nobody uses, a second chat tool, and StockPilot still running.",
                    "“How many applications do we pay for?” Twenty-three, and nobody knew; two of them unused.")
for i in range(23):
    r, c = divmod(i, 8)
    ap_problem.box(20 + c * 54, 30 + r * 54, 44, 44, None, "pink" if i in (5, 17) else ["blue", "paper", "y"][i % 3], rx=4, stroke="red" if i in (5, 17) else "")
ap_problem.box(480, 50, 260, 90, "Marco", "y", sub="“how many? what for?”")
ap_problem.note(380, 250, "23 apps · ≈ €61k a month · 2 unused", "red")

ap_analogy = Doodle(760, 250, "Doodle of clearing out a garage with four labelled piles: keep and use, keep but don't spend on, replace soon, and throw away. Every item goes on one pile; nothing stays unsorted.",
                     "Clearing a garage: four piles (keep, tolerate, replace, bin), and every item goes on one.")
for i, (t, f) in enumerate([("keep, use more", "green"), ("tolerate", "blue"), ("replace soon", "y"), ("bin", "pink")]):
    ap_analogy.box(20 + i * 186, 70, 166, 70, t, f, size=15)
ap_analogy.note(380, 200, "every item on exactly one pile", "pen")

ap_how = Doodle(760, 380, "Larder's application portfolio, 19 July 2027, on two axes: business value and technical fit. Invest, high value and good fit: Larder Core, Dispatch, WMS B, the billing service, the customer apps. Tolerate, lower value but fine: the helpdesk, the HR tool, the BI tool. Migrate, high value but poor fit: StockPilot, moving to WMS B by September; Mo's spreadsheet CRM, moving to a CRM. Eliminate, low value: a survey tool and a second chat tool nobody uses, the old courier cron and a legacy reporting database. Savings: about 2,300 euros a month.",
                 "Two axes, four boxes, every application in one. Eliminate pays for some of Invest.")
ap_how.line("M60 330 H720")
ap_how.line("M60 330 V20")
ap_how.line("M390 20 V330", dash=True, thin=True)
ap_how.line("M60 175 H720", dash=True, thin=True)
ap_how.text(390, 360, "technical fit →", "t t-soft", size=14)
ap_how.rawtext('<text class="t t-soft" transform="translate(40 175) rotate(-90)" text-anchor="middle" font-size="14">business value →</text>')
for x, y, t, items, f in [(70, 28, "MIGRATE", ["StockPilot → WMS B", "spreadsheet CRM"], "y"), (400, 28, "INVEST", ["Core · Dispatch · WMS B", "billing · apps"], "green"),
                          (70, 183, "ELIMINATE", ["survey tool · 2nd chat", "old cron · legacy DB"], "pink"), (400, 183, "TOLERATE", ["helpdesk · HR tool", "BI tool"], "blue")]:
    ap_how.box(x, y, 310, 138, None, f, rx=8)
    ap_how.head(x + 155, y + 34, t, size=17)
    for k, it in enumerate(items):
        ap_how.text(x + 155, y + 72 + k * 28, it, size=14)

PORTFOLIO = dict(
    slug="application-portfolio",
    kicker="a.k.a. “four piles in the garage”",
    tldr="Applications pile up: SaaS trials that stuck, tools for one team, systems you're half-way off. Keep an <b>application portfolio</b>: one list of every application, with its owner, cost, the capabilities it serves, and a <b>TIME</b> verdict: <b>Tolerate</b> (keep, don't invest), <b>Invest</b> (keep and improve), <b>Migrate</b> (replace with something better) or <b>Eliminate</b> (switch off). Sort by <b>business value</b> and <b>technical fit</b>, review yearly, and let Eliminate pay for Invest.",
    chips=[("Family", "the landscape"), ("Origin", "Gartner's TIME model (2009); application portfolio management"), ("Lives in", "one table in the landscape docs, reviewed yearly with finance"), ("Pairs with", "capability map, exit plans, data ownership")],
    problem_side="Larder, 19 July 2027",
    problem="""  <p class="lead">Marco asks a simple question: <i>how many applications do we pay for, and what for?</i> Nobody knows. Ana and Eli count <b>twenty-three</b>, about <b>€61,000 a month</b>, including a survey tool and a <b>second chat tool nobody uses</b>, a legacy reporting database, and StockPilot, still running during the migration. <span class="hl-pink">Nobody owned the whole list</span>, so nothing ever left it.</p>
  <ul>
    <li>Tools accumulate; nobody's job is to remove them.</li>
    <li>Spend, ownership and purpose are scattered.</li>
    <li>Every tool looks equally permanent.</li>
  </ul>""",
    problem_figs=[ap_problem],
    analogy_side="clearing the garage",
    analogy="""  <p>Clearing out a garage works with <b>four labelled piles</b>: keep and use more, keep but don't spend on, replace soon, and throw away. <b>Every item goes on exactly one pile</b>; nothing stays unsorted in the corner. Once a year is enough, if you actually carry the bin bags out.</p>""",
    analogy_figs=[ap_analogy],
    map=[("Keep and use more", "Invest: Larder Core, Dispatch, WMS B, billing, apps"),
         ("Keep, don't spend on", "Tolerate: helpdesk, HR tool, BI tool"),
         ("Replace soon", "Migrate: StockPilot, the spreadsheet CRM"),
         ("Throw away", "Eliminate: survey tool, second chat tool, old cron, legacy DB"),
         ("Once a year", "The yearly review with finance")],
    how_side="every application in one of four boxes",
    how="""  <p>Ana, Eli and Marco listed all 23 with owner, monthly cost and the capabilities each serves, then placed each on <b>business value</b> and <b>technical fit</b>. Four were <b>eliminated</b> (≈ €2,300 a month), two put on <b>migrate</b> with dates, and the <b>invest</b> box matched the capability map's weak spots. Each application now has a named owner, and new SaaS needs a line in the table before a contract.</p>""",
    how_figs=[ap_how],
    steps=[("List every application", "Including SaaS on company cards; ask finance for the bank lines."),
           ("Add owner, cost, users, capabilities", "One line each; a name, not a team."),
           ("Score value and fit", "Business value (from the capability map) and technical fit (from engineers)."),
           ("Give each a TIME verdict", "Tolerate, Invest, Migrate or Eliminate."),
           ("Act on Eliminate and Migrate", "Dates and owners; use exit plans."),
           ("Review yearly, gate new tools", "A line in the table before any new contract.")],
    vocab=[("Application portfolio", "The managed list of all applications."),
           ("TIME", "Tolerate, Invest, Migrate, Eliminate."),
           ("Business value", "How much an application matters to capabilities."),
           ("Technical fit", "How healthy, secure and maintainable it is."),
           ("Shadow IT", "Tools bought outside any central list."),
           ("Rationalisation", "Reducing the number of applications.")],
    code=dict(file="docs/landscape/portfolio-2027.md", note="Larder's application portfolio, 19 July 2027 (excerpt)", plain=True, src="""
# Application portfolio · reviewed with Marco · next review: July 2028

| Application        | Owner | €/month | Capabilities          | Value | Fit  | TIME      | Action          |
|--------------------|-------|---------|-----------------------|-------|------|-----------|-----------------|
| Larder Core        | Ana   | 4,800   | sell, fulfil, serve   | high  | good | Invest    | TD register     |
| Dispatch + Engine A| Eli   | 1,900   | deliver               | high  | good | Invest    |                 |
| WMS B              | Ben   | 9,800   | fulfil (stock)        | high  | good | Invest    |                 |
| StockPilot         | Ben   | 7,000   | fulfil (stock)        | high  | poor | Migrate   | off 15 Sep 2027 |
| Spreadsheet CRM    | Mo    | 0       | business accounts     | med   | poor | Migrate   | CRM by Dec      |
| Helpdesk           | Sam   | 2,100   | serve                 | med   | ok   | Tolerate  |                 |
| Survey tool        | —     | 900     | —                     | low   | ok   | Eliminate | cancelled 1 Aug |
| Second chat tool   | —     | 1,100   | —                     | low   | ok   | Eliminate | cancelled 1 Aug |
Total ≈ €61k/month · Eliminate ≈ €2.3k/month · new tools: a line here before any contract
"""),
    tools="tools: a spreadsheet joined with finance's SaaS spend; SaaS management tools (Zylo, Productiv, Vendr) for bigger organisations; LeanIX or Ardoq for enterprise portfolios.",
    gains=["<b>Spend visible</b>, with owners.",
           "<b>Unused tools removed</b>: ≈ €2,300 a month.",
           "<b>Migrations dated</b> instead of drifting.",
           "<b>Investment matches capabilities</b>.",
           "<b>A gate for new tools</b>."],
    losses=["<b>Collecting the list</b> takes a few days the first time.",
            "<b>Scores are judgement</b>.",
            "<b>Teams defend their tools</b>.",
            "<b>Needs the yearly habit</b>."],
    baseline="Each line compares <b>applications accumulating without a list or owners</b> to <b>a portfolio with owner, cost, capabilities and a TIME verdict per application, reviewed yearly</b>.",
    ratings=[(2, 5, "One table shows every application and why it exists."),
             (2, 4, "Finance and engineering agree the verdicts."),
             (3, 4, "Decisions to cut or keep take one session."),
             (2, 4, "Poor-fit applications get migration dates."),
             (2, 4, "The landscape gets simpler each year."),
             (2, 4, "Owners and verdicts on record."),
             (1, 5, "€61k a month, line by line; €2.3k cut."),
             (3, 3, "A few days the first time, then yearly."),
             (3, 3, "Neutral.")],
    pitfalls=[("Missing the card spend", "Half the SaaS is on credit cards.", "ask finance for bank lines, not just contracts."),
              ("Teams as owners", "“Engineering” owns the BI tool.", "one name per application."),
              ("Verdicts without action", "Eliminate, but still paid.", "dates and owners for every Eliminate and Migrate."),
              ("No gate", "New tools appear the next month.", "a line in the table before any contract.")],
    use=["Yearly budget and planning.",
         "After growth, mergers or a hiring spree.",
         "Before big migrations.",
         "When finance asks what you pay for."],
    skip=["Tiny companies with a handful of tools.",
          "As a substitute for exit plans on the critical ones."],
    related=["<b>Capability map</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)", "<b>Data ownership &amp; master data</b> (this volume)", "<b>Total cost of ownership</b> (Vol. 5)"],
    quiz=[("What does TIME stand for?", "Tolerate, Invest, Migrate, Eliminate."),
          ("Which two axes decide the verdict?", "Business value and technical fit."),
          ("Where did the hidden tools come from?", "SaaS bought by teams, often on company cards."),
          ("How do you stop new sprawl?", "A line in the portfolio before any new contract.")],
    try_it="Ask finance for last quarter's software and SaaS spend. Build a one-line-per-application table with owner, cost and the capability it serves. Give each a TIME verdict with one colleague, and cancel the first Eliminate this week.",
    remember="Four <span class=\"hl\">piles</span>, every item on one, and carry the <span class=\"hl\">bin bags</span> out.",
    sources=["Gartner, “Use TIME to Engage Business Stakeholders for Application Rationalization” (2009, updated).",
             "The Open Group, <i>TOGAF Standard</i>, application portfolio.",
             "Gregor Hohpe, <i>Cloud Strategy</i> (2020), on SaaS sprawl.",
             "LeanIX, “Application Portfolio Management” guides."],
)

# ------------------------------------------------------------------ 11 Data Ownership & Master Data
dm_problem = Doodle(760, 280, "Doodle of a pre-launch test for Antwerp in August 2027. The same product has three names and two VAT categories in three systems: the Catalogue, WMS B and the billing service. 212 products disagree. Each system was edited directly by a different team.",
                    "One product, three names, two VAT categories, three systems. 212 products disagree.")
for i, (sys, name, vat, f) in enumerate([("Catalogue", "Pommes Elstar 1 kg", "VAT: food", "blue"), ("WMS B", "APPLE ELSTAR 1KG", "—", "y"), ("billing", "Elstar apples", "VAT: standard ✗", "pink")]):
    dm_problem.box(20 + i * 250, 40, 220, 110, sys, f, sub=name, subsize=14)
    dm_problem.text(130 + i * 250, 140, vat, "t t-red" if "✗" in vat else "t", size=13)
dm_problem.note(380, 210, "212 products disagree across systems", "red", size=19)
dm_problem.note(380, 250, "each edited directly by a different team", "pen")

dm_analogy = Doodle(760, 250, "Doodle of a family's shared address book. One person keeps the master copy; everyone's phone syncs from it. When cousin Lisa moves, the master is changed once, and every phone updates. Nobody edits their own phone's copy.",
                     "A family address book: one master, every phone syncs from it, nobody edits their own copy.")
dm_analogy.icon("book", 40, 50, 1.5)
dm_analogy.box(160, 60, 220, 90, "the master", "green", sub="changed once")
dm_analogy.arrow(384, 105, 440, 105, dash=True, label="sync", lx=412, ly=92)
for i in range(3):
    dm_analogy.icon("phone", 450 + i * 90, 66, 1.4)
dm_analogy.note(450, 210, "edit the master, never the copies", "pen")

dm_how = Doodle(760, 360, "Larder's data ownership, ADR 0024, 2 August 2027. One master per kind of data, with a named owner. Product, including French and Dutch names and the VAT category: the Catalogue, owned by Grace's team. Price: Pricing. Stock: the Stock module, fed by WMS B. Customer: Ordering. Business account: Ordering, with Mo's CRM subscribing. Courier: Dispatch. Every other system subscribes to changes by events and never edits its copy. The 212 differences were fixed in the master and pushed out.",
                 "One master per kind of data, one owner, and everyone else subscribes. Fix the master, never the copies.")
rows = [("product (+ FR/NL, VAT)", "Catalogue", "Grace's team"), ("price", "Pricing", "Grace's team"), ("stock", "Stock (← WMS B)", "Ben"),
        ("customer", "Ordering", "Ben"), ("business account", "Ordering (→ CRM)", "Mo + Ben"), ("courier", "Dispatch", "Eli")]
dm_how.head(20, 30, "data", anchor="start", size=15)
dm_how.head(300, 30, "master", anchor="start", size=15)
dm_how.head(560, 30, "owner", anchor="start", size=15)
for i, (d, m, o) in enumerate(rows):
    y = 48 + i * 40
    dm_how.box(12, y, 736, 34, None, ["blue", "paper"][i % 2], rx=4)
    dm_how.text(20, y + 23, d, anchor="start", size=14)
    dm_how.text(300, y + 23, m, "t-head", anchor="start", size=14)
    dm_how.text(560, y + 23, o, anchor="start", size=14)
dm_how.note(380, 310, "everyone else subscribes to events; no edits to copies", "pen", size=16)
dm_how.note(380, 338, "ADR 0024 · 212 differences fixed in the master", "green", size=16)

DATA_OWNERSHIP = dict(
    slug="data-ownership",
    kicker="a.k.a. “the family address book”",
    tldr="When the same data lives in several systems and each is edited directly, the copies drift apart. Decide, for each important <b>kind of data</b> (product, price, customer, stock), <b>one master system</b> and <b>one owner</b>. Everyone else holds a <b>read-only copy</b> that <b>subscribes to changes</b>; fixes happen in the master, never in the copies. Write it down as a short table, and enforce it in the integrations.",
    chips=[("Family", "the landscape"), ("Origin", "master data management (MDM); data ownership and stewardship practice"), ("Lives in", "an ADR and a data ownership table in the landscape docs"), ("Pairs with", "event-driven integration, canonical data model, bounded contexts")],
    problem_side="Larder, 2 August 2027",
    problem="""  <p class="lead">A pre-launch test for <b>Antwerp</b> compares product data across systems. The same apples are <i>“Pommes Elstar 1 kg”</i> in the Catalogue, <i>“APPLE ELSTAR 1KG”</i> in WMS B and <i>“Elstar apples”</i> in billing, which also has the <b>wrong VAT category</b>. <span class="hl-pink">212 products disagree.</span> Each system was edited directly by a different team, each sure their copy was the real one.</p>
  <ul>
    <li>Several systems, each editable, each “the truth” to someone.</li>
    <li>Fixes in one copy don't reach the others.</li>
    <li>A new country multiplies the fields (languages, VAT) that can drift.</li>
  </ul>""",
    problem_figs=[dm_problem],
    analogy_side="the family address book",
    analogy="""  <p>A family keeps one <b>master address book</b>; everyone's phone syncs from it. When cousin Lisa moves, the master is <b>changed once</b> and every phone updates. If people edited their own phone's copy instead, within a year nobody would know where Lisa lives.</p>""",
    analogy_figs=[dm_analogy],
    map=[("The master address book", "The master system for a kind of data"),
         ("Whoever keeps it", "The data owner"),
         ("Phones syncing", "Other systems subscribing to change events"),
         ("Lisa moves", "A product's VAT category changes"),
         ("Never editing the phone", "No edits to copies; fix the master")],
    how_side="one master, one owner, everyone subscribes",
    how="""  <p>ADR 0024 named a <b>master and an owner</b> for six kinds of data. <b>Product</b> (including French and Dutch names and the VAT category) lives in the <b>Catalogue</b>, owned by Grace's team; WMS B and billing receive it by events and their edit screens for product fields were switched off. The 212 differences were fixed <b>in the Catalogue</b> and pushed out in a day; a nightly check now compares the copies and reports drift.</p>""",
    how_figs=[dm_how],
    steps=[("List the important kinds of data", "Product, price, customer, account, stock, courier…"),
           ("Name one master each", "The system where it's created and changed."),
           ("Name one owner each", "A person or team accountable for its quality."),
           ("Make copies read-only", "Others subscribe to change events; turn off edit screens."),
           ("Fix in the master", "Drift is corrected at the source and pushed out."),
           ("Check for drift", "A periodic comparison of copies with the master.")],
    vocab=[("Master data", "Core business data used by many systems: products, customers."),
           ("Master system", "The one system where that data is created and changed."),
           ("Data owner", "Accountable for a kind of data's quality and meaning."),
           ("Golden record", "The single trusted version of an entity."),
           ("Drift", "Copies diverging from the master."),
           ("Data steward", "Someone who looks after data quality day to day.")],
    code=dict(file="docs/adr/0024-data-ownership.md", note="ADR 0024, the ownership table", plain=True, src="""
# 24. One master and one owner per kind of data
Status: Accepted · 2027-08-02 · Driver: Ana · with Grace, Ben, Mo, Eli, Marco

| Data               | Master            | Owner         | Copies (read-only, by events)        |
|--------------------|-------------------|---------------|--------------------------------------|
| Product (+FR, NL,  | Catalogue         | Grace's team  | WMS B, billing, apps, analytics      |
|  VAT category)     |                   |               |                                      |
| Price              | Pricing           | Grace's team  | apps, billing                        |
| Stock              | Stock (← WMS B)   | Ben           | apps, analytics                      |
| Customer           | Ordering          | Ben           | Customer Care, helpdesk, billing     |
| Business account   | Ordering          | Mo + Ben      | CRM, billing                         |
| Courier            | Dispatch          | Eli           | analytics                            |

Rules  copies are read-only (edit screens off) · fixes in the master · nightly drift report
Antwerp test, Aug 2027: 212 product differences → fixed in Catalogue, pushed in one day
"""),
    tools="tools: the event-driven integration you already have; a drift-check job; MDM products (Akeneo or Salsify for product data, enterprise MDM suites) once the volume justifies them.",
    gains=["<b>One truth per kind of data</b>.",
           "<b>Fixes happen once</b> and spread.",
           "<b>Clear accountability</b> for data quality.",
           "<b>New fields</b> (languages, VAT) added in one place.",
           "<b>Drift detected</b>, not discovered."],
    losses=["<b>Edit screens removed</b> from some teams' tools.",
            "<b>Owners need time</b> for data quality.",
            "<b>Events to build</b> for every copy.",
            "<b>Edge cases</b>: data with two natural homes."],
    baseline="Each line compares <b>the same data edited directly in several systems</b> to <b>one master and owner per kind of data, with read-only copies that subscribe to changes</b>.",
    ratings=[(2, 5, "One table says where each kind of data lives."),
             (2, 4, "Grace, Ben, Mo and Eli each own a kind of data."),
             (3, 4, "Data questions go to one owner."),
             (1, 5, "Wrong VAT caught before Antwerp, not after."),
             (3, 4, "New fields added once."),
             (2, 4, "ADR 0024 and the drift report on record."),
             (3, 3, "Neutral."),
             (3, 3, "Events and a drift job to run."),
             (2, 4, "Owners fix their own data.")],
    pitfalls=[("Several masters", "Product names editable in three tools.", "one master; switch off edit screens elsewhere."),
              ("No owner", "Data owned by “the business”.", "a named team per kind of data."),
              ("Fixing copies", "Support corrects the helpdesk's copy.", "fix in the master; let it flow."),
              ("No drift check", "Divergence found at launch.", "compare copies with the master regularly.")],
    use=["Data shared by several systems: products, customers, prices.",
         "Before a new market, language or legal entity.",
         "When reports disagree about basic facts.",
         "Integrating new SaaS that wants its own copy."],
    skip=["Data used by one system only.",
          "Temporary copies in caches (keep them short-lived)."],
    related=["<b>Event-driven integration</b> (this volume)", "<b>Canonical data model (and its traps)</b> (this volume)", "<b>Glossary &amp; ubiquitous language</b> (Vol. 3)", "<b>Data classification &amp; residency</b> (Vol. 5)"],
    quiz=[("What's master data?", "Core business data used by many systems, such as products and customers."),
          ("What's the rule for copies?", "Read-only; they subscribe to changes, and fixes happen in the master."),
          ("Where does Larder's product data live?", "In the Catalogue, owned by Grace's team, including FR/NL names and VAT category."),
          ("How is drift caught?", "A nightly comparison of copies with the master.")],
    try_it="Pick one important kind of data (product or customer). List every system that stores it and whether each can edit it. Name the master and an owner, then find out how many records differ between two of the copies today.",
    remember="Edit the <span class=\"hl\">master</span>, never the copies. One <span class=\"hl\">owner</span> each.",
    sources=["DAMA International, <i>DAMA-DMBOK</i>, 2nd ed. (2017), master data management.",
             "David Loshin, <i>Master Data Management</i> (2008).",
             "Zhamak Dehghani, <i>Data Mesh</i> (2022), on domain data ownership.",
             "Eric Evans, <i>Domain-Driven Design</i> (2003), on bounded contexts."],
)

# ------------------------------------------------------------------ 12 Identity Federation & SSO
id_problem = Doodle(760, 280, "Doodle of a May 2027 access review by Lena. Larder staff use fourteen tools, each with its own password. A support agent who left in April still had access to the helpdesk and the billing service three weeks later. Business clients want their office managers to log in with their own company accounts, not another Larder password.",
                    "Fourteen tools, fourteen passwords, and a leaver with access three weeks later.")
for i in range(14):
    r, c = divmod(i, 7)
    id_problem.icon("key", 20 + c * 62, 30 + r * 60, 0.8, color="red" if i in (3, 9) else "")
id_problem.box(470, 30, 270, 90, "a leaver", "pink", sub="access 3 weeks later", stroke="red")
id_problem.box(470, 140, 270, 70, "clients", "y", sub="“our own accounts”")
id_problem.note(380, 262, "found in Lena's access review", "red")

id_analogy = Doodle(760, 250, "Doodle of a company badge that opens every door in the building. When someone leaves, security deactivates one badge and every door closes to them. Visitors from a partner company are let in on their own company's badge, agreed in advance, without a new key for each door.",
                     "One badge opens every door; one deactivation closes them all. Partners come in on their own badges.")
id_analogy.icon("badge", 40, 50, 1.5)
id_analogy.box(160, 50, 260, 100, "one badge", "green", sub="every door, off in one place")
id_analogy.box(450, 50, 290, 100, "partner badges", "blue", sub="trusted, agreed in advance")
id_analogy.note(450, 210, "no key per door", "pen")

id_how = Doodle(760, 360, "Larder's identity setup, ADR 0021, 24 May 2027. Staff: one identity provider; single sign-on to all fourteen tools; automatic provisioning and removal where tools support it; leavers switched off in one place, on their last day. Business clients: federation with each client's own identity provider, so office managers use their company accounts; when they leave their company, they lose access to Larder too. Pickers: personal badges on store handhelds instead of shared store logins.",
                 "Staff: one identity, SSO everywhere, off in one place. Clients: their own accounts, federated. Pickers: personal badges.")
id_how.box(280, 20, 200, 80, "identity provider", "green", sub="one per person", subsize=14)
for i, t in enumerate(["helpdesk", "billing", "WMS B", "… 14 tools"]):
    id_how.box(20 + i * 186, 150, 166, 50, t, "paper", size=14)
    id_how.arrow(380, 104, 103 + i * 186, 146, dash=True)
id_how.box(20, 230, 350, 70, "clients: their own IdP", "blue", sub="federated (OIDC / SAML)")
id_how.box(390, 230, 350, 70, "leaver: off in one place", "y", sub="last day, every tool")
id_how.note(380, 336, "pickers: personal badges on handhelds · ADR 0021", "pen", size=16)

IDENTITY = dict(
    slug="identity-federation",
    kicker="a.k.a. “one badge for every door”",
    tldr="When every tool has its own password, people reuse weak ones, and <b>leavers keep access</b> because nobody removes fourteen accounts. Use <b>one identity provider</b> for staff, with <b>single sign-on</b> to every tool and <b>automatic provisioning and removal</b> where tools support it. For partners and business clients, <b>federate</b>: trust <b>their</b> identity provider, so their people use their own company accounts and lose access when they leave. One identity per person; switched off in one place.",
    chips=[("Family", "the landscape"), ("Origin", "SAML 2.0 (2005), OpenID Connect (2014), SCIM (2015); identity federation practice"), ("Lives in", "the identity provider's config and an ADR"), ("Pairs with", "solution design document, data ownership, security architecture review")],
    problem_side="Larder, 24 May 2027",
    problem="""  <p class="lead">Lena's access review finds that Larder staff use <b>fourteen tools</b>, each with its own password. A support agent who left in April still had access to the <b>helpdesk and the billing service three weeks later</b>. Meanwhile two new business clients, like Korenwolf before them, want their office managers to log in <b>with their own company accounts</b>, not another Larder password. <span class="hl-pink">Identity is scattered across every tool.</span></p>
  <ul>
    <li>Leavers keep access because removal is manual, tool by tool.</li>
    <li>Password reuse and resets cost time and security.</li>
    <li>Business clients can't control who at their company has access.</li>
  </ul>""",
    problem_figs=[id_problem],
    analogy_side="the building badge",
    analogy="""  <p>A company <b>badge</b> opens every door in the building. When someone leaves, security <b>deactivates one badge</b> and every door closes to them. Visitors from a partner company come in on <b>their own company's badge</b>, trusted by agreement, without a new key for each door. Nobody keeps a drawer of keys.</p>""",
    analogy_figs=[id_analogy],
    map=[("The badge", "One identity per person, in the identity provider"),
         ("Every door", "Single sign-on to all fourteen tools"),
         ("Deactivating the badge", "Leaver switched off in one place, on their last day"),
         ("A partner's own badge", "Federation with the client's identity provider"),
         ("A drawer of keys", "Fourteen separate passwords")],
    how_side="one identity, federated outward",
    how="""  <p>ADR 0021 put all staff on <b>one identity provider</b>, with <b>SSO</b> to every tool and <b>automatic provisioning and removal</b> (SCIM) for the eleven that support it; the other three are removed by a checklist on the leaver's last day. Business clients <b>federate</b> their own identity providers, as Korenwolf did in December: when an office manager leaves Korenwolf, they lose Larder access automatically. Pickers got personal badges on the handhelds instead of shared store logins.</p>""",
    how_figs=[id_how],
    steps=[("Pick one identity provider", "Usually the one staff already log in to every day."),
           ("Connect every tool by SSO", "SAML or OpenID Connect; list tools that can't, and plan for them."),
           ("Automate joiners and leavers", "SCIM provisioning; a checklist for the rest."),
           ("Federate with partners and clients", "Trust their identity provider; no Larder passwords for them."),
           ("Remove shared accounts", "Personal identities, even on store devices."),
           ("Review access regularly", "Quarterly, with the data protection officer.")],
    vocab=[("Identity provider (IdP)", "The system that holds identities and logs people in."),
           ("Single sign-on (SSO)", "One login for many tools."),
           ("Federation", "Trusting another organisation's identity provider."),
           ("SAML / OIDC", "Standard protocols for SSO and federation."),
           ("SCIM", "A standard for creating and removing accounts automatically."),
           ("Joiner-mover-leaver", "The lifecycle of a person's access.")],
    code=dict(file="docs/adr/0021-identity.md", note="ADR 0021, decision (shortened)", plain=True, src="""
# 21. One identity per person; federate with clients
Status: Accepted · 2027-05-24 · Driver: Ana · Approver: Lena (DPO) · with Eli, Sam, Mo

Staff     one identity provider · SSO to all 14 tools (SAML/OIDC)
          SCIM provisioning for 11 tools; 3 without SCIM → leaver checklist
          leavers switched off on their last day by People ops
Clients   federation with each client's IdP (OIDC or SAML) for the business portal
          and API keys per client system; no Larder passwords for client staff
          Korenwolf (Dec 2026), + 2 clients (June 2027)
Stores    personal badges on handhelds; shared store logins removed by July
Review    quarterly access review with Lena
Finding that triggered this: a leaver kept helpdesk and billing access for 3 weeks.
"""),
    tools="tools: your workspace identity provider or a dedicated one (Okta, Microsoft Entra ID, Google, Keycloak); SCIM support in each SaaS; access review tooling.",
    gains=["<b>Leavers lose access</b> in one step.",
           "<b>Fewer passwords</b>, fewer resets.",
           "<b>Clients control their own users</b>.",
           "<b>Audit-ready</b>: one place to see who has access.",
           "<b>Personal accountability</b>: no shared logins."],
    losses=["<b>SSO costs extra</b> on some SaaS plans.",
            "<b>One provider is critical</b>: its outage locks everyone out.",
            "<b>Federation setup per client</b>.",
            "<b>Some tools can't</b> do SSO or SCIM."],
    baseline="Each line compares <b>a separate account per tool, removed by hand</b> to <b>one identity per person with SSO, automated provisioning, and federation with clients</b>.",
    ratings=[(2, 4, "One place shows who can access what."),
             (2, 4, "Lena, Sam and clients agree on the model."),
             (3, 3, "Neutral."),
             (1, 5, "Leavers lose access the day they leave."),
             (3, 4, "New tools plug into the same identity."),
             (2, 5, "Every access change is logged in one place."),
             (2, 3, "SSO tiers cost extra on some plans."),
             (2, 4, "Fewer accounts to manage by hand."),
             (3, 4, "Clients manage their own users.")],
    pitfalls=[("Tools left out", "Three tools still on passwords, forgotten.", "list them; a leaver checklist until they support SSO."),
              ("Shared accounts", "“noord-picker-1” used by six people.", "personal identities, even on store devices."),
              ("Client passwords", "Larder accounts for client staff who leave their job.", "federate with the client's IdP."),
              ("No break-glass", "The IdP is down; nobody can get in.", "emergency accounts, stored safely, tested.")],
    use=["Any company with more than a handful of SaaS tools.",
         "B2B products with client users.",
         "Before an audit or security review.",
         "When joiners and leavers are frequent."],
    skip=["Very small teams with two or three tools (still use strong passwords and MFA).",
          "Public consumer logins: a different problem (customer identity)."],
    related=["<b>Solution design document done right</b> (Vol. 3)", "<b>Security architecture review</b> (Vol. 5)", "<b>Data ownership &amp; master data</b> (this volume)", "<b>OAuth 2.0 &amp; OpenID Connect</b> (patterns, Vol. 5)"],
    quiz=[("What's the difference between SSO and federation?", "SSO: one login for your own tools. Federation: trusting another organisation's identity provider."),
          ("What does SCIM do?", "Creates and removes accounts in tools automatically."),
          ("Why federate with business clients?", "Their staff use their own accounts and lose access when they leave their company."),
          ("What triggered Larder's change?", "A leaver kept helpdesk and billing access for three weeks.")],
    try_it="List every tool your team logs in to, and mark which support SSO and automatic removal. Pick someone who left in the last six months and check which tools still have their account. Fix those today, and plan SSO for the rest.",
    remember="One <span class=\"hl\">badge</span> for every door, switched off in <span class=\"hl\">one place</span>.",
    sources=["OASIS, SAML 2.0 (2005); OpenID Foundation, OpenID Connect Core 1.0 (2014).",
             "IETF RFC 7643/7644, SCIM 2.0 (2015).",
             "NIST SP 800-63, “Digital Identity Guidelines”.",
             "Justin Richer and Antonio Sanso, <i>OAuth 2 in Action</i> (2017)."],
)

NOTES = [CAPABILITY, PORTFOLIO, DATA_OWNERSHIP, IDENTITY]
