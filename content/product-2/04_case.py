# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 2 · Making the case.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 13 Opportunity Sizing
os_problem = Doodle(760, 280, "Doodle of February 2026, after the trade fair where Femke met Korenwolf. Femke quotes a report: office catering in the Netherlands is a 50-million-euro market, so Larder for Business deserves its own team. Priya asks Grace how big it really is for Larder. Grace's question: how many offices could actually order from us?",
                    "“A €50 million market!” But how many offices could actually order from Larder?")
os_problem.box(20, 30, 330, 90, "Femke", "y", sub="“a €50 million market”")
os_problem.icon("newspaper", 380, 40, 1.2)
os_problem.box(440, 30, 300, 90, "Priya", "paper", sub="“how big, for us?”")
os_problem.box(150, 160, 460, 64, "how many offices could order from us?", "pink", size=16)
os_problem.note(380, 262, "a big number from a report, about everyone", "red")

os_analogy = Doodle(760, 270, "Doodle of someone planning a bakery. Top-down: the Dutch bread market is two billion euros. Bottom-up: two thousand homes within a ten-minute walk, sixty percent buy fresh bread, three times a week, three euros each: about 560,000 euros a year. Only the second number helps decide whether to open.",
                     "Opening a bakery: “bread is a €2 billion market” vs counting the homes within a ten-minute walk.")
os_analogy.box(20, 30, 300, 90, "top-down", "paper", sub="“bread: €2 billion”")
os_analogy.icon("store", 380, 40, 1.3)
os_analogy.box(470, 20, 270, 170, None, "green")
os_analogy.head(605, 50, "bottom-up", size=18)
for i, t in enumerate(["2,000 homes, 10 min walk", "× 60 % buy fresh bread", "× 3 a week × €3", "≈ €560k a year"]):
    os_analogy.text(605, 84 + i * 26, t, "t-head" if i == 3 else "t", size=15)
os_analogy.note(170, 170, "true, and useless", "red")
os_analogy.note(380, 244, "count the customers you could actually serve", "pen")

os_how = Doodle(760, 350, "Grace's bottom-up sizing of Larder for Business, 9 February 2026. Offices with fifty or more staff inside Larder's delivery zones in Amsterdam and Rotterdam: about 1,500. Times 120 staff on average, times 5 euros of pantry per person per week, times 48 weeks: a market of about 43 million euros a year. Reachable by end 2027, two percent of offices, 30 offices: about 0.9 million euros a year. Checks: the fake door found 9 offices in two weeks; Korenwolf alone would be about 0.6 million euros a year. Consumer orders bring about 55 million euros a year. Decision: worth a pilot, not yet a team.",
                "Count what you can serve, then what you can win. Check it against real signals. Then compare with what you already have.")
for i, (t, s, w, f) in enumerate([("1,500 offices", "50+ staff, in our zones", 560, "paper"), ("× 120 staff × €5/wk × 48", "≈ €43M a year", 460, "y"), ("2 % by end 2027", "30 offices ≈ €0.9M a year", 360, "green")]):
    os_how.box(290 - w / 2, 16 + i * 74, w, 62, t, f, sub=s, size=16, subsize=15)
os_how.box(14, 250, 230, 76, "fake door", "blue", sub="9 offices in 2 weeks", size=16)
os_how.box(264, 250, 230, 76, "Korenwolf", "blue", sub="≈ €0.6M a year alone", size=16)
os_how.box(600, 30, 146, 170, None, "paper", dash=True)
os_how.text(673, 70, "consumers", "t-head", size=15)
os_how.text(673, 100, "≈ €55M", "t-head", size=18)
os_how.text(673, 126, "a year", size=14)
os_how.note(620, 280, "→ a pilot,", "green", anchor="start", size=19)
os_how.note(620, 308, "not a team (yet)", "green", anchor="start", size=19)

SIZING = dict(
    slug="opportunity-sizing",
    kicker="a.k.a. “count the homes within a ten-minute walk”",
    tldr="A <b>top-down</b> number (“a €50 million market”) is true and almost useless: it's about everyone, not your customers. Size <b>bottom-up</b> instead: count the customers you could <b>actually serve</b> (where you deliver, the size you fit), multiply by what each would spend, then estimate what share you could <b>realistically win</b> by a date. <b>Check</b> it against real signals (a fake door, a first client), <b>compare</b> it with what you already have, and let the size decide the <b>next step</b>: an experiment, a pilot or a team.",
    chips=[("Family", "making the case"), ("Origin", "TAM / SAM / SOM in venture practice; Fermi estimation"), ("Lives in", "one page with the sums, linked from the business case"), ("Pairs with", "fake door test, business case one-pager, bets not promises")],
    problem_side="Larder, 9 February 2026",
    problem="""  <p class="lead">At the January trade fair Femke met <b>Korenwolf</b>, and came back with a report: office catering in the Netherlands is a <b>€50 million market</b>. Larder for Business, she says, deserves its own team. Priya asks Grace a sharper question: <i>how big is it for us?</i> The €50 million counts every office in the country, including ones Larder can't reach and ones that would never buy pantry restocks. <span class="hl-pink">It can't tell anyone what to do next</span>.</p>
  <ul>
    <li>Top-down numbers are big, true and not about your customers.</li>
    <li>Without a realistic share and a date, every market looks worth a team.</li>
    <li>Real signals (the fake door, one client) sit unused next to the report.</li>
  </ul>""",
    problem_figs=[os_problem],
    analogy_side="opening a bakery",
    analogy="""  <p>Someone opening a bakery could quote the <b>€2 billion Dutch bread market</b>. A good baker counts instead: <b>2,000 homes</b> within a ten-minute walk, 60 % buy fresh bread, three times a week, €3 a time: about <b>€560,000 a year</b> if they won every one. Then: how many could we really win, from the bakery on the corner? That number decides whether to sign the lease.</p>""",
    analogy_figs=[os_analogy],
    map=[("The €2 billion bread market", "The €50 million office-catering report"),
         ("Homes within a ten-minute walk", "Offices with 50+ staff in Larder's delivery zones"),
         ("Bread per home per week", "€5 of pantry per person per week"),
         ("Winning some from the corner bakery", "2 % of offices by end 2027"),
         ("Signing the lease, or not", "A pilot now; a team only if it works")],
    how_side="count, multiply, check, compare",
    how="""  <p>Grace built the sum with Joost's zone maps and a public company register: <b>1,500 offices</b> of 50+ staff in Amsterdam and Rotterdam zones, roughly <b>€43M a year</b> if Larder won them all, and about <b>€0.9M</b> at a realistic 2 % by end 2027. The checks agreed: the fake door found 9 offices in two weeks, and Korenwolf alone would be €0.6M. Against <b>€55M</b> of consumer orders, the answer was clear: <b>a pilot, not a team</b>, and a pilot with Korenwolf was agreed for May.</p>""",
    how_figs=[os_how],
    steps=[("Define who you could serve", "The segment you can reach and fit: here, offices of 50+ staff inside delivery zones."),
           ("Count them", "From registers, maps, your own data. A range is fine."),
           ("Multiply by spend", "Per customer per period, from interviews, a first client or comparable products."),
           ("Estimate a realistic share by a date", "What you could win, given your team and channels: 1–5 % is often honest."),
           ("Check against real signals", "Fake door responses, a first client, inbound requests."),
           ("Compare and decide the step", "Against what you already earn: experiment, pilot or team?")],
    vocab=[("Top-down", "Starting from a whole-market number and slicing it."),
           ("Bottom-up", "Counting reachable customers and multiplying by spend."),
           ("TAM / SAM / SOM", "Total, serviceable and obtainable market."),
           ("Segment", "A group of customers you could serve the same way."),
           ("Realistic share", "What you could win by a date, honestly."),
           ("Fermi estimate", "A rough calculation from a few reasonable guesses.")],
    code=dict(file="product/sizing/2026-02-larder-for-business.md", note="Grace's sizing, 9 February 2026", plain=True, src="""
# Larder for Business: how big is it for us?            Grace · 9 Feb 2026

Who we could serve   offices with 50+ staff inside our delivery zones
                     Amsterdam ~900 · Rotterdam ~600 (from April) = ~1,500
Spend                ~120 staff per office (median from the register)
                     × €5 of pantry per person per week (Korenwolf's estimate)
                     × 48 weeks
Serviceable market   1,500 × 120 × €5 × 48 ≈ €43M a year
Realistic by 2027    2 % of offices = 30 offices ≈ €0.9M a year

Checks               Fake door (Dec): 9 offices of 40+ staff in 2 weeks
                     Korenwolf alone, 2,400 staff: ≈ €0.6M a year
Compare              Consumer orders ≈ €55M a year (4,000/day × €38)

Next step            A 12-week pilot with Korenwolf HQ (May). A team only if the
                     pilot renews and 5+ more offices ask.  Review: September.
Top-down, for the record: "office catering NL ≈ €50M" (report Femke brought).
"""),
    tools="tools: a spreadsheet; public company registers (the Dutch KvK), your delivery-zone maps, a fake door or landing page for signals. Fermi-style estimation with ranges beats false precision.",
    gains=["<b>A number about your customers</b>, not everyone's.",
           "<b>The next step falls out</b>: experiment, pilot or team.",
           "<b>Assumptions are visible</b> and can be checked.",
           "<b>Real signals get used</b>: the fake door, a first client.",
           "<b>Calm conversations</b> with enthusiastic founders."],
    losses=["<b>Rough</b>: each number is a guess.",
            "<b>Can undersell</b> a market that grows fast.",
            "<b>Takes a day</b> of digging.",
            "<b>Disappointing</b> to people who loved the big number."],
    baseline="Each line compares <b>quoting a top-down market report</b> to <b>a bottom-up count of reachable customers × spend × a realistic share, checked against real signals</b>.",
    ratings=[(3, 4, "Starts from customers Larder could really serve."),
             (2, 5, "≈ €0.9M by 2027, compared with €55M today."),
             (2, 4, "Fake door and Korenwolf check the sum."),
             (3, 4, "The pilot tests the biggest assumption (spend)."),
             (2, 4, "A pilot, not a team: effort stays on refunds."),
             (2, 4, "Everyone can follow the sum."),
             (2, 4, "Femke gets a real answer, and a pilot."),
             (3, 3, "Doesn't change flow."),
             (3, 3, "A day of digging and a page.")],
    pitfalls=[("Top-down only", "“1 % of a €50M market.”", "count reachable customers bottom-up."),
              ("Unrealistic share", "“We'll win 20 % by next year.”", "use an honest share for your team and channels."),
              ("No checks", "The sum is never compared with any signal.", "check against a fake door, a first client, inbound asks."),
              ("Size decides everything", "Big number, so build a team.", "let the size pick the next step: test, pilot or team.")],
    use=["New segments or markets someone is excited about.",
         "Before staffing a new team or product line.",
         "When a top-down report is driving the conversation.",
         "Business cases that need a revenue line."],
    skip=["Small improvements to an existing product: use cost of delay.",
          "When a cheap test would answer faster than a sizing."],
    related=["<b>Business case one-pager</b> (this volume)", "<b>Bets, not promises</b> (this volume)", "<b>Fake door test</b> (Vol. 1)", "<b>Opportunity cost</b> (this volume)"],
    quiz=[("Why is a top-down number “true and useless”?", "It's about the whole market, not the customers you could actually serve."),
          ("What are the bottom-up steps?", "Count reachable customers, multiply by spend, estimate a realistic share by a date."),
          ("How did Grace check her sum?", "Against the fake door (9 offices in 2 weeks) and Korenwolf alone (≈ €0.6M)."),
          ("What did the size decide?", "A pilot with Korenwolf, not a new team, yet.")],
    try_it="Pick a segment someone in your company is excited about. Count the customers you could actually reach, multiply by a spend you can defend, and take an honest share by a date. Check it against one real signal, then write one line: experiment, pilot or team?",
    remember="Don't quote the <span class=\"hl\">bread market</span>. Count the homes within a <span class=\"hl\">ten-minute walk</span>.",
    sources=["Steve Blank and Bob Dorf, <i>The Startup Owner's Manual</i> (2012), on TAM / SAM / SOM.",
             "Douglas Hubbard, <i>How to Measure Anything</i> (2007), on Fermi estimates.",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on opportunity assessment.",
             "Rob Fitzpatrick, <i>The Mom Test</i> (2013), on signals from real customers."],
)

# ------------------------------------------------------------------ 14 Business Case One-Pager
bc_problem = Doodle(760, 270, "Doodle of Grace's first business case for substitution approvals, February 2026: nine pages. Marco, the CFO, reads page one and asks two questions: what do we get, and what does it cost?",
                    "Nine pages. Marco reads page one and asks: what do we get, and what does it cost?")
for i in range(9):
    bc_problem.box(30 + i * 22, 24 + i * 10, 160, 140, None, "paper", rx=4)
bc_problem.text(286, 190, "p. 1 of 9", "t-head", size=16)
bc_problem.box(420, 60, 320, 100, "Marco", "y", sub="“what do we get? what does it cost?”", subsize=15)
bc_problem.note(580, 210, "pages 2–9: unread", "red", size=20)

bc_analogy = Doodle(760, 250, "Doodle of a solar panel quote on one sheet: cost 6,000 euros, saves 900 euros a year, pays back in about seven years, risk: the neighbour's tree shades the roof in winter. One sheet, and you can decide.",
                    "A solar-panel quote: cost, savings, payback, the one big risk. One sheet, and you can decide.")
bc_analogy.icon("lamp", 40, 40, 1.4)
for i, (t, s, f) in enumerate([("cost", "€6,000", "pink"), ("saves", "€900 a year", "green"), ("payback", "≈ 7 years", "y"), ("risk", "the tree's shade", "paper")]):
    x = 150 + i * 152
    bc_analogy.box(x, 50, 140, 90, t, f, sub=s, size=18, subsize=15)
bc_analogy.note(450, 210, "one sheet, and you can decide", "pen")

bc_how = Doodle(760, 360, "Grace's one-page business case for substitution approvals, approved on 12 February 2026. The problem: substitution refunds cost about 45,000 euros a month. Benefit: about 30,000 euros a month, plus customers keeping their order frequency. Cost: about 48,000 euros to build, plus about 1,800 euros a month of picker time. Payback: about two months. Evidence and risks: concierge test, 1.1 percent swap refund tickets against 6.8 percent; risk, customers not answering in time. The ask: eight person-weeks of Ben's and Dee's teams, February and March.",
                "Problem, benefit, cost, payback, evidence and risks, the ask: one page Marco read to the end.")
bc_how.box(14, 14, 732, 56, "problem: substitution refunds ≈ €45k a month", "paper", size=17)
bc_how.box(14, 86, 350, 110, "benefit", "green", sub="≈ €30k/month + retention", size=19)
bc_how.box(396, 86, 350, 110, "cost", "pink", sub="€48k build + €1.8k/month", size=19)
bc_how.box(230, 214, 300, 56, "payback ≈ 2 months", "y", size=18)
bc_how.box(14, 286, 350, 60, "evidence: 1.1 % vs 6.8 %", "blue", size=15)
bc_how.box(396, 286, 350, 60, "ask: 8 person-weeks", "blue", size=15)

BIZ_CASE = dict(
    slug="business-case",
    kicker="a.k.a. “the solar-panel quote”",
    tldr="People who approve money read <b>one page</b>. Put it all there: the <b>problem</b> in euros, the <b>benefit</b> (with how you estimated it), the <b>cost</b> to build and to run, the <b>payback</b>, the <b>evidence</b> behind the numbers, the <b>biggest risks</b>, and the <b>ask</b>: how much, from whom, until when. Round the numbers, show the sums, and link the details. If it doesn't fit on one page, you don't understand it well enough yet.",
    chips=[("Family", "making the case"), ("Origin", "business case practice; Amazon's narrative memos; the one-page proposal"), ("Lives in", "one page, linked from the roadmap item"), ("Pairs with", "cost of delay, opportunity sizing, bets not promises")],
    problem_side="Larder, 12 February 2026",
    problem="""  <p class="lead">Approvals need <b>eight person-weeks</b> of Ben's and Dee's teams, which Priya can approve, but Marco, the CFO, wants to see the case. Grace writes a thorough one: <b>nine pages</b> of interviews, opportunity trees, concierge results and screen designs. Marco reads page one and asks two questions: <span class="hl-pink">what do we get, and what does it cost?</span> Both answers were on page seven.</p>
  <ul>
    <li>Long cases hide the numbers decision-makers need.</li>
    <li>Benefits without sums look like hope; costs without running costs look like tricks.</li>
    <li>The ask (how much, from whom, until when) is often missing entirely.</li>
  </ul>""",
    problem_figs=[bc_problem],
    analogy_side="the solar-panel quote",
    analogy="""  <p>A good solar-panel quote fits on <b>one sheet</b>: it costs <b>€6,000</b>, saves about <b>€900 a year</b>, pays back in about <b>seven years</b>, and the one big risk is the neighbour's tree shading the roof in winter. The installer has forty pages of specifications, but you can decide from the sheet, and ask for page 23 if you care.</p>""",
    analogy_figs=[bc_analogy],
    map=[("€6,000 to install", "Cost: €48k to build, €1.8k a month in picker time"),
         ("€900 a year saved", "Benefit: ≈ €30k a month of refunds avoided"),
         ("Pays back in seven years", "Payback: about two months"),
         ("The tree's shade", "Risk: customers not answering within two minutes"),
         ("Forty pages of specs", "Interviews, tests and designs, linked, not attached")],
    how_side="seven parts, one page",
    how="""  <p>Grace rewrote it in an hour. The benefit came from the baseline: <b>€45k a month</b> of substitution refunds, and approvals targeting the two-thirds where customers weren't asked. The cost included the <b>running cost</b> pickers would feel (about 10 seconds per swap order, after the prototype fix). Marco read it to the end, asked one question about the risk, and it was approved the same afternoon.</p>""",
    how_figs=[bc_how],
    steps=[("State the problem in euros", "From the baseline: what it costs today, per month."),
           ("Estimate the benefit with its sum", "Which part of the problem this removes, and why you think so."),
           ("Cost it fully", "Build cost (person-weeks × rate) and running cost (people's time, fees)."),
           ("Compute payback", "Cost ÷ monthly net benefit. Round it."),
           ("Name evidence and the top risks", "What the numbers rest on; the two or three things that could break them."),
           ("End with the ask", "How much, from whom, until when, and who decides.")],
    vocab=[("Business case", "The argument for spending money or time, with numbers."),
           ("Benefit", "Money saved or earned, or risk avoided, per period."),
           ("Running cost", "What it costs every month once it's live."),
           ("Payback period", "How long until the benefit covers the cost."),
           ("Loaded rate", "The full cost of a person-week, including overheads."),
           ("The ask", "The specific resources and decision you need.")],
    code=dict(file="product/cases/2026-02-approvals.md", note="the one-pager Marco approved, 12 February 2026", plain=True, src="""
# Business case: substitution approvals in the app        Grace · 12 Feb 2026

Problem    Substitution refunds cost ≈ €45k a month (refunds + support time).
           Customers with 2+ refund tickets order 30 % less the next month.
Benefit    Approvals target the ~2/3 of swap refunds where nobody asked:
           ≈ €30k a month, plus customers keeping their order frequency (not counted).
Cost       Build: 8 person-weeks × €6k ≈ €48k.
           Running: ~10 s extra picking per swap order × ~25k a month ≈ €1.8k a month.
Payback    €48k ÷ (€30k − €1.8k) ≈ 2 months.
Evidence   Concierge test at Noord (Dec): swap refund tickets 1.1 % vs 6.8 % at Zuid;
           81 % answered within 2 minutes. Prototype: 6 customers, 3 pickers.
Risks      Answer rate below 70 % at scale · picker slowdown at peak ·
           web orders (~20 %) can't approve until the web shop follows.
Ask        8 person-weeks of Ben's and Dee's teams, Feb–Mar. Decision: Priya,
           Marco consulted. Release plan: Noord staff test → Amsterdam → Rotterdam.
"""),
    tools="tools: a page in the wiki or a document; a spreadsheet behind it for the sums. Amazon-style six-page memos are for bigger decisions; for a team-sized ask, one page is right.",
    gains=["<b>Decisions in an afternoon</b>, not after three meetings.",
           "<b>The numbers are visible</b> and can be challenged.",
           "<b>Running costs included</b>, so no surprises later.",
           "<b>Finance trusts product</b> when cases are honest.",
           "<b>Forces clear thinking</b>: one page needs understanding."],
    losses=["<b>Rounding hides detail</b> some people want.",
            "<b>Estimates can be wrong</b>; the page makes them look firm.",
            "<b>Hard to fit uncertain benefits</b> (retention).",
            "<b>Writing short takes longer</b> than writing long."],
    baseline="Each line compares <b>a long case document with the numbers buried inside</b> to <b>one page: problem, benefit, cost, payback, evidence and risks, and the ask</b>.",
    ratings=[(3, 3, "Mostly about the money; customers are in the evidence."),
             (2, 5, "Benefit and payback in euros."),
             (2, 4, "Every number names where it came from."),
             (3, 4, "Approved in an afternoon; building starts sooner."),
             (2, 4, "One ask, clearly bounded."),
             (2, 5, "Anyone can read why approvals were funded."),
             (2, 5, "Marco read it to the end and said yes."),
             (3, 3, "Doesn't change flow directly."),
             (3, 4, "An hour to write.")],
    pitfalls=[("Burying the numbers", "The benefit is on page seven.", "problem, benefit, cost, payback first."),
              ("Build cost only", "No running cost.", "add what it costs every month once live."),
              ("Benefits without sums", "“Customers will be happier.”", "show the sum, or mark it as not counted."),
              ("No ask", "A case that never says what it needs.", "end with how much, from whom, until when.")],
    use=["Any ask for money, people or weeks that needs approval.",
         "When finance or leadership must say yes.",
         "Comparing two investments.",
         "Before a big bet on the roadmap."],
    skip=["Small work inside the team's agreed capacity.",
          "Experiments costing days: a hypothesis card is enough."],
    related=["<b>Opportunity sizing</b> (this volume)", "<b>Cost of delay</b> (this volume)", "<b>Bets, not promises</b> (this volume)", "<b>Build vs buy vs open source</b> (Ana, book 1 vol. 2)"],
    quiz=[("What are the seven parts of the one-pager?", "Problem, benefit, cost, payback, evidence, risks and the ask."),
          ("Why include running cost?", "It's paid every month once live; leaving it out makes the case look better than it is."),
          ("How is payback calculated?", "Cost divided by monthly net benefit (benefit minus running cost)."),
          ("What must the ask say?", "How much, from whom, until when, and who decides.")],
    try_it="Take the next thing you need approval for. Write it on one page with the seven parts, rounding every number and showing each sum. Give it to someone from finance and ask them to tell you, in one sentence, what you're asking for and why.",
    remember="A <span class=\"hl\">quote</span>, not a brochure: cost, savings, <span class=\"hl\">payback</span>, the one big risk, the ask.",
    sources=["Jeff Bezos, Amazon shareholder letter (2017), on narrative memos.",
             "Roman Pichler, <i>Strategize</i>, 2nd ed. (2022), on business cases for products.",
             "Douglas Hubbard, <i>How to Measure Anything</i> (2007), on estimating benefits.",
             "Barbara Minto, <i>The Pyramid Principle</i> (1987), answer first."],
)

# ------------------------------------------------------------------ 15 Bets, Not Promises
bn_problem = Doodle(760, 270, "Doodle of Femke's draft board slide in April 2026: refund tickets at 2 percent by June. Grace's worry: Larder doesn't control how fast customers answer or how often items run out. A promise on a number nobody controls, missed, costs trust.",
                    "“Refunds: 2 % by June.” A promise on a number nobody controls.")
bn_problem.box(20, 30, 360, 160, None, "paper")
bn_problem.head(200, 70, "board, 16 April", size=17)
bn_problem.text(200, 120, "refunds: 2 % by June", "t-head", size=20)
bn_problem.text(200, 156, "(a promise)", size=16)
bn_problem.box(430, 40, 310, 140, None, "pink", stroke="red")
bn_problem.head(585, 74, "what we don't control", size=16, color="red")
for i, t in enumerate(["how fast customers answer", "how often items run out"]):
    bn_problem.text(585, 112 + i * 30, t, size=16)
bn_problem.note(380, 246, "missed promise = lost trust", "red")

bn_analogy = Doodle(760, 250, "Doodle of a weather forecast. One forecaster says it will rain tomorrow. A better one says seventy percent chance of rain, and updates it every six hours. When it stays dry, the second is still trusted.",
                     "“It will rain” vs “70 % chance of rain, updated every six hours”. Only one is still trusted after a dry day.")
bn_analogy.box(20, 40, 320, 100, "“it will rain”", "pink", sub="a promise")
bn_analogy.box(420, 40, 320, 100, "“70 % chance”", "green", sub="a bet, updated every 6 h")
bn_analogy.note(180, 190, "dry day: wrong", "red", size=20)
bn_analogy.note(580, 190, "dry day: still trusted", "green", size=20)

bn_how = Doodle(760, 360, "Grace's three bets for the board, 16 April 2026. Bet 1, approvals: confidence high; expected swap refund tickets from 6.2 to about 3.5 percent by end of June; double down if at least 70 percent answer within two minutes; rethink if under 50 percent; first signal, 79 percent in the first three days in Amsterdam. Bet 2, the no-swaps flag: confidence medium; about half a point; signal, flag used on at least 8 percent of orders. Bet 3, live order updates: confidence low, Q3. Message: 3 to 4 percent by June, 2 percent by December if bets 2 and 3 work; reported monthly.",
                "Three bets with confidence, expected effect and signals. The board gets a range and a monthly number, not a promise.")
for i, (name, conf, w, eff, sig, f) in enumerate([("1 · approvals", "high", 0.8, "6.2 % → ~3.5 % by June", "≥ 70 % answer in 2 min (now 79 %)", "green"),
                                                  ("2 · “no swaps” flag", "medium", 0.5, "≈ −0.5 point", "used on ≥ 8 % of orders", "y"),
                                                  ("3 · live order update", "low", 0.25, "Q3: fewer “where is it?”", "a test first", "paper")]):
    y = 14 + i * 96
    bn_how.box(14, y, 732, 84, None, f, rx=8)
    bn_how.text(28, y + 32, name, "t-head", anchor="start", size=16)
    bn_how.text(28, y + 62, eff, anchor="start", size=15)
    bn_how.text(300, y + 32, "confidence", "t t-soft", anchor="start", size=14)
    bn_how.box(300, y + 44, 110, 14, None, "paper", rx=3)
    bn_how.box(300, y + 44, round(110 * w), 14, None, "blue", rx=3)
    bn_how.text(420, y + 56, conf, anchor="start", size=14)
    bn_how.text(730, y + 32, "signal", "t t-soft", anchor="end", size=14)
    bn_how.text(730, y + 62, sig, anchor="end", size=14)
bn_how.note(380, 322, "to the board: 3–4 % by June · 2 % by December · reported monthly", "green", size=17)

BETS = dict(
    slug="bets-not-promises",
    kicker="a.k.a. “70 % chance of rain”",
    tldr="A product team controls what it builds, not how customers respond. So present plans as <b>bets</b>, not <b>promises</b>: what you're doing, the <b>expected effect</b> as a range, your <b>confidence</b> and why, the <b>signal</b> that says double down, and the one that says stop or rethink. Report the <b>number every month</b>. A missed promise costs trust; a bet that's updated honestly earns it, even when it loses.",
    chips=[("Family", "making the case"), ("Origin", "Annie Duke, <i>Thinking in Bets</i> (2018); John Cutler and Itamar Gilad on product bets"), ("Lives in", "the board deck and the outcome roadmap"), ("Pairs with", "outcome-based roadmaps, business case, testable hypotheses")],
    problem_side="Larder, 14 April 2026",
    problem="""  <p class="lead">Approvals went live in Amsterdam on <b>13 April</b>. Femke's draft slide for Thursday's board says <b>“Refunds: 2 % by June”</b>, the goal Grace wrote in November. Grace is worried: Larder controls the app, but <span class="hl-pink">not how fast customers answer, or how often items run out</span>, and Rotterdam won't have approvals until June. If June shows 3.5 %, the board will remember a missed promise, not a halving of refunds.</p>
  <ul>
    <li>Promises on outcomes you don't control are likely to be missed.</li>
    <li>A missed promise damages trust more than an honest range ever would.</li>
    <li>Without signals, nobody knows early whether the plan is working.</li>
  </ul>""",
    problem_figs=[bn_problem],
    analogy_side="the weather forecast",
    analogy="""  <p>One forecaster says <b>“it will rain tomorrow”</b>. Another says <b>“70 % chance of rain”</b>, and updates it every six hours. When tomorrow stays dry, the first is simply wrong. The second was right to say 70 %, and people keep trusting her, because she told them how sure she was and kept them posted.</p>""",
    analogy_figs=[bn_analogy],
    map=[("“It will rain”", "“Refunds: 2 % by June”"),
         ("“70 % chance of rain”", "“3–4 % by June, high confidence”"),
         ("Why she thinks so", "The concierge test, the prototype"),
         ("Updated every six hours", "Reported every month"),
         ("The forecast that changes", "Doubling down, or rethinking, on a signal")],
    how_side="expected effect, confidence, signals",
    how="""  <p>Grace and Femke rewrote the slide together: <b>three bets</b>, each with an expected effect, a confidence level, and a signal. The first signal was already in: <b>79 %</b> of Amsterdam customers answered within two minutes in the first three days. The board heard “3–4 % by June, 2 % by December if bets 2 and 3 work, and you'll get the number every month”, and an investor said it was the first product slide he'd believed.</p>""",
    how_figs=[bn_how],
    steps=[("Separate what you control", "What you'll build and ship (control) from what customers do (influence)."),
           ("Write each bet", "The work, the outcome it targets, the expected effect as a range."),
           ("State confidence and why", "High, medium, low, with the evidence behind it."),
           ("Set two signals per bet", "Double down if…; stop or rethink if… Both measurable, both early."),
           ("Give leadership a range and a date", "Not a point promise: “3–4 % by June”."),
           ("Report monthly", "The number, the signals, and what you changed.")],
    vocab=[("Bet", "Work you believe will move an outcome, with stated confidence."),
           ("Promise", "A commitment to a result, as if you controlled it."),
           ("Confidence", "How sure you are, and on what evidence."),
           ("Signal", "An early, measurable sign a bet is working or not."),
           ("Range", "An honest spread for the expected effect."),
           ("Double down", "Invest more because the signal says it works.")],
    code=dict(file="product/board/2026-04-bets.md", note="the slide Grace and Femke took to the board, 16 April 2026", plain=True, src="""
# Substitution refunds: our bets for 2026          reported monthly to the board

Today: 6.2 % of orders end in a swap refund ticket (≈ €45k a month).
We control what we ship; we influence how customers respond.

BET 1  Approvals in the app (Amsterdam 13 Apr, Rotterdam June)    confidence HIGH
       Expect   6.2 % → ~3.5 % by end June
       Why      concierge 1.1 % vs 6.8 %; prototype with 6 customers
       Double down if ≥ 70 % answer within 2 min   (first 3 days: 79 %)
       Rethink if     < 50 %, or picking slows > 15 s per swap order
BET 2  "No swaps" flag per item (live 23 Feb)                       confidence MEDIUM
       Expect   ≈ −0.5 point · signal: used on ≥ 8 % of orders
BET 3  Live order updates (Q3)                                       confidence LOW
       Expect   fewer "where is my order?" tickets · a test first

Our message: 3–4 % by June; 2 % by December if bets 2 and 3 work.
"""),
    tools="tools: the outcome roadmap plus a monthly one-page update. Itamar Gilad's Confidence Meter for confidence levels; Annie Duke's <i>Thinking in Bets</i> for the mindset.",
    gains=["<b>Trust survives a miss</b>, because the range was honest.",
           "<b>Early signals</b> show if the plan is working.",
           "<b>Leaders understand uncertainty</b> instead of being surprised by it.",
           "<b>Bets can change</b> without anyone being wrong.",
           "<b>Better decisions</b> about where to double down."],
    losses=["<b>Feels less decisive</b> to some leaders.",
            "<b>Ranges can be gamed</b> (always low, always beat it).",
            "<b>Monthly reporting</b> takes time.",
            "<b>Investors sometimes want a single number</b>."],
    baseline="Each line compares <b>promising a single result by a date</b> to <b>bets with an expected range, stated confidence and early signals, reported monthly</b>.",
    ratings=[(3, 3, "Customers aren't directly affected."),
             (2, 4, "Expected effects in the business's numbers."),
             (2, 5, "Confidence is tied to named evidence."),
             (2, 5, "Signals show within days whether a bet works."),
             (2, 4, "Three bets, ranked by confidence."),
             (2, 5, "Everyone knows what's expected and how sure we are."),
             (2, 5, "The board heard a range, and believed it."),
             (3, 3, "Doesn't change flow."),
             (3, 3, "A monthly update to write.")],
    pitfalls=[("Promising an outcome", "“2 % by June.”", "a range, a confidence level and a monthly number."),
              ("Sandbagging", "Always promise low and beat it.", "state your real best estimate; show the evidence."),
              ("No signals", "Wait until June to find out.", "two early signals per bet: double down, or rethink."),
              ("Silent updates", "The range changes and nobody is told.", "report every month, including bad news.")],
    use=["Reporting outcome goals to leadership, boards or investors.",
         "When a past target now looks unlikely.",
         "Any plan where customers' behaviour decides the result.",
         "Portfolios of several initiatives."],
    skip=["Pure delivery commitments you fully control (a contract date).",
          "Legal or safety obligations: those are promises."],
    related=["<b>Outcome-based roadmaps</b> (this volume)", "<b>Business case one-pager</b> (this volume)", "<b>Testable hypotheses</b> (Vol. 1)", "<b>Revisiting decisions</b> (Ana, book 1 vol. 2)"],
    quiz=[("Why not promise “2 % by June”?", "Larder doesn't control how customers respond; a missed promise costs trust."),
          ("What does each bet need?", "The work, the expected effect as a range, confidence and why, and signals to double down or rethink."),
          ("What was the first signal for approvals?", "79 % answered within two minutes in the first three days."),
          ("How often should bets be reported?", "Monthly: the number, the signals, what changed.")],
    try_it="Find one target your team has promised that depends on customers' behaviour. Rewrite it as a bet: expected range, confidence with evidence, and two signals. Share it with the person who'll be asked about it, and offer a monthly one-paragraph update.",
    remember="Say “<span class=\"hl\">70 % chance</span>”, not “it will rain”. And update the <span class=\"hl\">forecast</span>.",
    sources=["Annie Duke, <i>Thinking in Bets</i> (2018).",
             "Itamar Gilad, <i>Evidence-Guided</i> (2023), the Confidence Meter.",
             "John Cutler, “Bets, not projects” (The Beautiful Mess, 2020–).",
             "Philip Tetlock and Dan Gardner, <i>Superforecasting</i> (2015)."],
)

NOTES = [SIZING, BIZ_CASE, BETS]
