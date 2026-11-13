# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 2 · Strategy & roadmaps.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Product Strategy on a Page
sp_problem = Doodle(760, 280, "Doodle of three people on Grace's team answering the same question in January 2026, what are we trying to do this year? Ben says ship approvals. Dee says rebuild the app for Rotterdam. Sam says fewer tickets. Priya asks Grace for the ordering strategy for 2026; Grace has a backlog of sixty items and an opportunity tree, but no story that connects them.",
                    "“What are we trying to do this year?” Three people, three answers, and a backlog of sixty items.")
for i, (who, says) in enumerate([("Ben", "“ship approvals”"), ("Dee", "“the app for Rotterdam”"), ("Sam", "“fewer tickets”")]):
    sp_problem.box(20 + i * 250, 30, 220, 76, who, "paper", sub=says)
sp_problem.box(150, 150, 460, 70, "Priya: “the 2026 strategy?”", "y", size=17)
sp_problem.note(380, 262, "60 backlog items, no story connecting them", "red")

sp_analogy = Doodle(760, 270, "Doodle of a football coach's game plan on one whiteboard: where we are in the league, the opponent's weak flank, how we'll win (press high, fast wingers), what we won't do (no long balls), and how we'll know at half-time (shots on target).",
                    "A coach's game plan fits on one whiteboard: where we are, how we'll win, what we won't do, how we'll know.")
sp_analogy.icon("board", 30, 60, 1.8)
for i, (t, s, f) in enumerate([("where we are", "8th, two losses", "paper"), ("how we win", "press high, use the wings", "green"), ("not doing", "no long balls", "pink"), ("we'll know", "shots on target at half-time", "y")]):
    y = 14 + i * 60
    sp_analogy.box(190, y, 170, 48, t, f, size=16, rx=6)
    sp_analogy.text(380, y + 30, s, anchor="start", size=16)

sp_how = Doodle(760, 360, "Grace's ordering strategy for 2026 on one page, agreed with Priya on 26 January. Where we are: 6.2 percent of orders end in a refund ticket; 82 percent perfect orders. Who we serve: tonight-dinner parents and Sunday planners; offices later. How we win: honest substitutions and on-time delivery. Three bets for 2026: approvals in the app, the no-swaps flag, live order updates. Not this year: recipes, meal kits, non-food. We'll know by: perfect orders from 82 to 88 percent by December.",
                "Six boxes, one page. Every backlog item should point at one of them.")
cells = [("where we are", "6.2 % refund tickets · 82 % perfect", "paper"), ("who we serve", "dinner parents, planners · offices later", "blue"),
         ("how we win", "honest swaps · on time", "green"), ("3 bets for 2026", "approvals · flag · live updates", "y"),
         ("not this year", "recipes · meal kits · non-food", "pink"), ("we'll know by", "perfect orders 82 → 88 % (Dec)", "green")]
for i, (t, s, f) in enumerate(cells):
    r, c = divmod(i, 2)
    x, y = 14 + c * 372, 14 + r * 104
    sp_how.box(x, y, 360, 92, t, f, sub=s, size=18, subsize=15)
sp_how.note(380, 344, "agreed with Priya, 26 Jan · on the team wall", "pen", size=18)

STRATEGY = dict(
    slug="strategy-on-a-page",
    kicker="a.k.a. “the coach's whiteboard”",
    tldr="A backlog says what you'll build; a <b>strategy</b> says why those things and not others. Put it on <b>one page</b>: <b>where we are</b> (the honest numbers), <b>who we serve</b>, <b>how we win</b> (the few things that make customers choose you), the <b>bets</b> for the year, what we're <b>not doing</b>, and <b>how we'll know</b> it's working. One page is short enough to remember and to argue with, and every backlog item should point at one box.",
    chips=[("Family", "strategy &amp; roadmaps"), ("Origin", "Richard Rumelt, <i>Good Strategy Bad Strategy</i> (2011); Roman Pichler's product strategy canvas; Playing to Win (Lafley &amp; Martin)"), ("Lives in", "one page on the team wall and the wiki"), ("Pairs with", "north star metric, now / next / later roadmap, opportunity solution tree")],
    problem_side="Larder, 19 January 2026",
    problem="""  <p class="lead">Priya asks Grace for the <b>ordering strategy for 2026</b>. Grace has a lot: an opportunity tree, a north star, a baseline, 60 backlog items. But when she asks her team <i>what are we trying to do this year?</i>, <b>Ben</b> says “ship approvals”, <b>Dee</b> says “get the app ready for Rotterdam”, <b>Sam</b> says “fewer tickets”. All true; <span class="hl-pink">none of it adds up to a story</span>, and the next loud request could reshuffle everything.</p>
  <ul>
    <li>A backlog without a strategy is a list of things people asked for.</li>
    <li>Each person fills the gap with their own priority.</li>
    <li>Without a written “not doing”, every idea is still in play.</li>
  </ul>""",
    problem_figs=[sp_problem],
    analogy_side="the coach's whiteboard",
    analogy="""  <p>Before a match, a good coach puts the game plan on <b>one whiteboard</b>: where we are in the league, <b>how we'll win</b> (press high, use the wings), what we <b>won't do</b> (no long balls), and <b>how we'll know</b> at half-time (shots on target). Every player can repeat it. A forty-page plan would be better researched and completely useless at minute 60.</p>""",
    analogy_figs=[sp_analogy],
    map=[("Where we are in the league", "Where we are: 6.2 % refund tickets, 82 % perfect orders"),
         ("The opponent's weak flank", "Who we serve: dinner parents, Sunday planners"),
         ("Press high, use the wings", "How we win: honest substitutions, on time"),
         ("No long balls", "Not this year: recipes, meal kits, non-food"),
         ("Shots on target at half-time", "We'll know by: perfect orders 82 → 88 %")],
    how_side="six boxes, one page",
    how="""  <p>Grace drafted it in an afternoon from what she already had (the interviews, the tree, the north star) and spent a week arguing it with Priya, Ana and the team. The hardest box was <b>not this year</b>: three things people liked, written down as out. After that, every item in the Q2 plan pointed at one of the three bets, and the request triage had something to triage <i>against</i>.</p>""",
    how_figs=[sp_how],
    steps=[("Start with the honest numbers", "Where we are: the north star, the baseline, the problem in one line."),
           ("Name who you serve", "The two or three customer types you'll focus on, and who comes later."),
           ("Say how you'll win", "The few things that make customers choose you; keep it to two or three."),
           ("Pick the bets", "Three bets for the year, each linked to an opportunity on the tree."),
           ("Write what you won't do", "Three things people would like, out for this year, with a line why."),
           ("Say how you'll know", "One or two numbers with a date. Review the page every quarter.")],
    vocab=[("Strategy", "The choices about where to focus and how to win; what you won't do."),
           ("Bet", "A big piece of work you believe will move the numbers."),
           ("Not doing", "Explicit choices to leave things out."),
           ("Diagnosis", "Rumelt's “where we are”: the honest problem."),
           ("Guiding policy", "Rumelt's “how we win”: the approach."),
           ("Coherent actions", "The bets: work that follows from the policy.")],
    code=dict(file="product/strategy/2026-ordering.md", note="Grace's strategy on a page, agreed 26 January 2026", plain=True, src="""
# Ordering & customer apps · strategy 2026            owner: Grace · agreed with Priya

WHERE WE ARE   6.2 % of orders end in a substitution refund ticket (≈ €45k/month);
               customers with 2+ tickets order 30 % less. Perfect orders: 82 %.
               Rotterdam opens 27 Apr; six cities by end 2027.
WHO WE SERVE   Tonight-dinner parents (express, ~70 % of orders) and Sunday
               planners (slots). Offices: later, once Larder for Business is proven.
HOW WE WIN     Honest substitutions: customers decide, never surprised at the door.
               On time, every time, in every new city.
3 BETS         1. Approve or refuse substitutes in the app (2-minute window)
               2. "Never swap this" flag per item
               3. Live order updates with the substitute and its price
NOT THIS YEAR  Recipe ideas · meal kits · non-food ranges
WE'LL KNOW BY  Perfect orders 82 % → 88 % by December 2026 ·
               substitution refund tickets 6.2 % → 2 %
Review         every quarter with Priya; the next one in April.
"""),
    tools="tools: one page in the wiki, printed for the wall. Templates: Roman Pichler's Product Vision Board and Strategy Canvas, Rumelt's kernel (diagnosis, guiding policy, coherent actions), the Playing to Win cascade.",
    gains=["<b>One story</b> the whole team can repeat.",
           "<b>Every item points somewhere</b>, or it's questioned.",
           "<b>Not-doing list</b> stops ideas coming back each week.",
           "<b>Leadership alignment</b> on one page, not a deck.",
           "<b>Quarterly review</b> keeps it honest."],
    losses=["<b>Hard choices in writing</b>: some people will be unhappy.",
            "<b>Too short for detail</b>: link to the tree and the roadmap.",
            "<b>Can go stale</b> without the quarterly review.",
            "<b>Tempting to fill with slogans</b> instead of choices."],
    baseline="Each line compares <b>a long backlog with no written strategy</b> to <b>one page of strategy: where we are, who we serve, how we win, three bets, not doing, and how we'll know</b>.",
    ratings=[(3, 4, "Focus on the customers and problems that matter most."),
             (2, 5, "Every bet ties to the north star and the money."),
             (2, 4, "Built from interviews, the tree and the baseline."),
             (3, 3, "Doesn't speed up learning; directs it."),
             (2, 5, "Three bets and a not-doing list."),
             (2, 5, "Everyone can say what we're doing this year and why."),
             (2, 4, "Priya and Femke agreed it in writing."),
             (3, 3, "Doesn't change flow directly."),
             (3, 4, "An afternoon to draft, a week to agree.")],
    pitfalls=[("Slogans, not choices", "“Delight customers with world-class ordering.”", "each box must exclude something."),
              ("No not-doing list", "Every idea stays alive.", "write three things you won't do this year."),
              ("A deck, not a page", "Forty slides nobody rereads.", "one page; link details from it."),
              ("Written once", "January's strategy in September.", "review every quarter.")],
    use=["The start of a year or a new product area.",
         "When the team gives different answers to “what are we doing?”.",
         "Before building a roadmap.",
         "When requests keep reshuffling the backlog."],
    skip=["A single short project with one clear goal.",
          "When the company strategy already says it all for your area (rare)."],
    related=["<b>Now / next / later roadmap</b> (this volume)", "<b>Outcome-based roadmaps</b> (this volume)", "<b>North star metric</b> (Vol. 1)", "<b>Business drivers &amp; goals</b> (Ana, book 1 vol. 1)"],
    quiz=[("What six boxes make up the page?", "Where we are, who we serve, how we win, the bets, not doing, and how we'll know."),
          ("Why is the not-doing box the hardest and most useful?", "It's a real choice: written-down exclusions stop ideas coming back."),
          ("How do you test a backlog item against the strategy?", "It should point at one of the bets; if not, question it."),
          ("How often should it be reviewed?", "Every quarter.")],
    try_it="Write your product's strategy on one page with the six boxes, in under two hours. Ask three team members to read it and say back, in one sentence, what you're doing this year. Where their sentences differ, the page isn't clear yet.",
    remember="One <span class=\"hl\">whiteboard</span>. How we win, what we <span class=\"hl\">won't</span> do, how we'll know.",
    sources=["Richard Rumelt, <i>Good Strategy Bad Strategy</i> (2011).",
             "A. G. Lafley and Roger Martin, <i>Playing to Win</i> (2013).",
             "Roman Pichler, <i>Strategize</i>, 2nd ed. (2022), the Product Strategy Canvas.",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018)."],
)

# ------------------------------------------------------------------ 10 Now / Next / Later Roadmap
nnl_problem = Doodle(760, 290, "Doodle of the roadmap Grace inherited: a Gantt chart from 2025 with fourteen features and exact dates through December. It's February 2026 and nine of them are already late. Femke asks whether the roadmap is still true; nobody can say.",
                     "The inherited roadmap: fourteen dated bars to December, nine already late. “Is this still true?”")
for i in range(7):
    y = 24 + i * 30
    x = 40 + (i * 53) % 300
    late = i in (0, 1, 3, 4, 6)
    nnl_problem.box(x, y, 180 + (i % 3) * 40, 20, None, "pink" if late else "paper", stroke="red" if late else "", rx=3)
nnl_problem.line("M300 14 V240", dash=True, color="red")
nnl_problem.note(306, 254, "today, Feb 2026", "red", anchor="start", size=17)
nnl_problem.box(560, 40, 180, 80, "Femke", "y", sub="“still true?”")
nnl_problem.note(380, 280, "9 of 14 dates already missed", "red")

nnl_analogy = Doodle(760, 260, "Doodle of a house renovation plan in three columns. Now: fix the leaking roof, sure and detailed. Next: the kitchen, likely, roughly sketched. Later: the garden, an idea. The further away, the fuzzier, and that's honest.",
                      "A renovation: the roof now (detailed), the kitchen next (sketched), the garden later (an idea).")
for i, (h, t, d, f) in enumerate([("now", "fix the roof", "quotes in, starts Monday", "green"), ("next", "the kitchen", "rough sketch", "y"), ("later", "the garden", "an idea", "paper")]):
    x = 20 + i * 250
    nnl_analogy.head(x + 110, 34, h, size=22)
    nnl_analogy.box(x, 54, 220, 110, t, f, sub=d, dash=i == 2)
nnl_analogy.note(380, 224, "the further away, the fuzzier, on purpose", "pen")

nnl_how = Doodle(760, 360, "Grace's now, next, later roadmap, 6 February 2026, updated 31 March. Now, February to March, committed: the no-swaps flag, the approvals build, Rotterdam in the app. Next, April to June, likely: approvals in Amsterdam, then Rotterdam in June; live order updates. Later, second half of 2026 and beyond, possible: offices ordering for themselves, French and Dutch for Antwerp, a recipe test if the newsletter test shows interest. Each card names the bet it serves.",
                 "Three columns, cards that name their bet, no dates beyond “now”. Updated every month.")
cols = [("NOW · Feb–Mar", "green", ["“no swaps” flag", "approvals build", "Rotterdam in app"]),
        ("NEXT · Apr–Jun", "y", ["approvals rollout", "live order update", "flag remembered"]),
        ("LATER · H2+", "paper", ["offices self-serve", "French + Dutch", "recipe test, if…"])]
for i, (h, f, cards) in enumerate(cols):
    x = 14 + i * 248
    nnl_how.box(x, 14, 236, 40, h, f, size=16, rx=6)
    for k, t in enumerate(cards):
        nnl_how.box(x + 8, 70 + k * 72, 220, 58, t, "paper" if i else "blue", size=13, rx=4, dash=i == 2)
nnl_how.note(130, 300, "committed", "green", size=17)
nnl_how.note(380, 300, "likely", "pen", size=17)
nnl_how.note(626, 300, "possible", "pen", size=17)
nnl_how.note(380, 340, "updated monthly · 31 Mar: RTM approvals moved to June", "pen", size=17)

NNL = dict(
    slug="now-next-later",
    kicker="a.k.a. “the roof, then the kitchen, then the garden”",
    tldr="A Gantt chart of features with dates to December promises precision nobody has, and is wrong by February. A <b>now / next / later</b> roadmap has three columns: <b>now</b> (being built, committed), <b>next</b> (likely, being shaped) and <b>later</b> (possible, still fuzzy). No dates beyond “now”, every card names the <b>bet or outcome</b> it serves, and the board is <b>updated monthly</b>. Honest uncertainty earns more trust than precise bars that slip.",
    chips=[("Family", "strategy &amp; roadmaps"), ("Origin", "Janna Bastow, ProdPad (c. 2012); “theme-based roadmaps”"), ("Lives in", "one board, shared, updated monthly"), ("Pairs with", "strategy on a page, outcome-based roadmaps, roadmap vs release plan")],
    problem_side="Larder, 6 February 2026",
    problem="""  <p class="lead">Grace inherited a roadmap: a Gantt chart from 2025 with <b>14 features</b> and exact dates through December. By February, <span class="hl-pink">nine are already late</span>, two have nothing to do with the strategy she just agreed, and Femke asks a fair question: <i>is the roadmap still true?</i> Nobody can say, so nobody trusts it, so everyone keeps their own list.</p>
  <ul>
    <li>Dates far ahead are guesses presented as facts.</li>
    <li>Each slip erodes trust in the whole roadmap.</li>
    <li>Features without a why can't be questioned or swapped.</li>
  </ul>""",
    problem_figs=[nnl_problem],
    meanwhile=[("architect-1", "walking-skeleton", "the “Rotterdam in the app” card in Grace's Now column runs on this skeleton.", "Grace's roadmap puts “Rotterdam in the app” in its Now column, built on this skeleton.")],
    analogy_side="the renovation plan",
    analogy="""  <p>Renovating a house: the <b>leaking roof</b> is now (quotes in, starts Monday, detailed). The <b>kitchen</b> is next (a rough sketch, likely this year). The <b>garden</b> is later (an idea). Nobody books the gardener for next September on day one; the plan is honest about what's known, and gets sharper as each job comes closer.</p>""",
    analogy_figs=[nnl_analogy],
    map=[("The roof, starting Monday", "Now: committed work, being built"),
         ("The kitchen sketch", "Next: likely, being shaped"),
         ("The garden idea", "Later: possible, fuzzy on purpose"),
         ("Why each job matters", "Each card names its bet or outcome"),
         ("Updating the plan as you go", "A monthly update, changes noted")],
    how_side="three columns, a why on every card",
    how="""  <p>Grace replaced the Gantt chart with three columns on 6 February. Every card names the bet it serves; two old features with no bet disappeared. The board is updated on the first Monday of each month, with a one-line change log. On <b>31 March</b>, after the Rotterdam trade-off sliders, “approvals in Rotterdam” moved within Next to June, and because the roadmap had never promised a date, nobody felt lied to.</p>""",
    how_figs=[nnl_how],
    steps=[("Start from the strategy", "Every card should serve one of the bets or outcomes on the strategy page."),
           ("Fill Now honestly", "Only what's being built or about to be: committed, detailed."),
           ("Shape Next", "Likely in the coming months; problems more than solutions."),
           ("Keep Later fuzzy", "Possible directions, written as problems or themes."),
           ("No dates beyond Now", "Dates belong in the release plan, with confidence levels."),
           ("Update monthly, log changes", "One line per change: what moved and why.")],
    vocab=[("Now", "Being built; committed."),
           ("Next", "Likely soon; being shaped."),
           ("Later", "Possible; still uncertain."),
           ("Theme", "A group of work around one problem or bet."),
           ("Gantt chart", "Bars on a timeline: good for plans, bad for roadmaps."),
           ("Change log", "A dated line for each move on the roadmap.")],
    code=dict(file="product/roadmap/README.md", note="Grace's roadmap, as of 31 March 2026", plain=True, src="""
# Ordering & customer apps · roadmap          updated monthly · strategy: 2026-ordering.md

NOW (Feb–Mar, committed)
  - "No swaps" flag per item ............................ bet 2 · live 23 Feb
  - Substitution approvals, build ...................... bet 1
  - Rotterdam in the app (zones, prices, hours) ......... launch 27 Apr
NEXT (Apr–Jun, likely)
  - Approvals: Amsterdam (Apr), Rotterdam (June) ........ bet 1
  - Live order update with the substitute ............... bet 3
  - "No swaps" remembered across orders ................. bet 2
LATER (H2 2026 and beyond, possible)
  - Offices order for themselves (if the pilot works)
  - French and Dutch in the apps (Antwerp, 2027)
  - Recipe test, if the newsletter shows interest (it didn't; see 25 Feb)

Change log
  06 Feb  replaced the 2025 Gantt chart; dropped 2 items with no bet
  31 Mar  approvals in Rotterdam → June (trade-off sliders, Rotterdam launch)
"""),
    tools="tools: a board with three columns (Miro, FigJam, Trello, ProdPad, Productboard), or a Markdown page. ProdPad popularised the format and has a template.",
    gains=["<b>Honest about uncertainty</b>, so it stays true.",
           "<b>Every card has a why</b>, linked to the strategy.",
           "<b>Easy to update</b> as you learn.",
           "<b>Trust grows</b>: fewer broken promises.",
           "<b>Readable in a minute</b> by anyone."],
    losses=["<b>Some stakeholders want dates</b>: give them the release plan.",
            "<b>Can feel vague</b> to people used to Gantt charts.",
            "<b>Later can become a dumping ground</b>.",
            "<b>Needs the monthly update</b> to stay credible."],
    baseline="Each line compares <b>a Gantt-chart roadmap of features with dates to December</b> to <b>now / next / later columns with a why on every card, updated monthly</b>.",
    ratings=[(3, 4, "Customer problems shape Next and Later."),
             (2, 4, "Every card ties to a bet and its outcome."),
             (2, 4, "Later stays fuzzy until there's evidence."),
             (2, 4, "Easy to move cards as tests come in."),
             (2, 4, "Now is short; the rest waits."),
             (2, 5, "One board, readable by anyone."),
             (1, 4, "No more missed dates on the roadmap."),
             (3, 4, "Small, committed Now column."),
             (3, 4, "A monthly update and a change log.")],
    pitfalls=[("Dates sneak back", "“Next (by 15 May)”.", "dates go in the release plan, not the roadmap."),
              ("Later as a dump", "Fifty cards in Later.", "keep Later to a handful of themes."),
              ("Features without a why", "Cards that serve no bet.", "every card names its bet or outcome."),
              ("Never updated", "February's board in June.", "update monthly, with a change log.")],
    use=["Replacing a date-heavy roadmap that keeps slipping.",
         "Sharing direction with leadership and other teams.",
         "Products with a lot of uncertainty.",
         "After writing a strategy on a page."],
    skip=["Contractual delivery dates: those need a release plan.",
          "Very short projects: a release plan is enough."],
    related=["<b>Product strategy on a page</b> (this volume)", "<b>Outcome-based roadmaps</b> (this volume)", "<b>Roadmap vs release plan</b> (this volume)", "<b>Walking skeleton</b> (Ana, book 1 vol. 1)"],
    quiz=[("What goes in each column?", "Now: committed work being built. Next: likely, being shaped. Later: possible, fuzzy."),
          ("Where do dates go?", "In the release plan, with confidence levels, not on the roadmap."),
          ("What must every card say?", "Which bet or outcome it serves."),
          ("How often should it be updated?", "Monthly, with a change log.")],
    try_it="Redraw your current roadmap as three columns. For each card, write the bet or outcome it serves; anything without one goes on a separate list to question. Remove every date beyond Now and share the board with one stakeholder who used to ask for dates.",
    remember="The <span class=\"hl\">roof</span> now, the kitchen next, the garden later. Honest <span class=\"hl\">fuzz</span> beats precise slips.",
    sources=["Janna Bastow, “The Now-Next-Later Roadmap” (ProdPad, 2012–).",
             "C. Todd Lombardo et al., <i>Product Roadmaps Relaunched</i> (2017).",
             "Roman Pichler, <i>Strategize</i>, 2nd ed. (2022), on goal-oriented roadmaps.",
             "Marty Cagan, “The Alternative to Roadmaps” (SVPG, 2015)."],
)

# ------------------------------------------------------------------ 11 Outcome-Based Roadmaps
or_problem = Doodle(760, 280, "Doodle of Femke's board slide in March 2026: Q2 features: approvals, the no-swaps flag, live order updates. An investor asks: and what will that do? The slide lists outputs and says nothing about results.",
                    "A slide of features. The board's question: “and what will that do?”")
or_problem.box(20, 20, 380, 220, None, "paper")
or_problem.head(210, 54, "Q2 features", size=19)
for i, t in enumerate(["• approvals", "• “no swaps” flag", "• live order updates"]):
    or_problem.text(60, 100 + i * 40, t, anchor="start", size=17)
or_problem.box(450, 60, 290, 90, "an investor", "y", sub="“and what will that do?”")
or_problem.note(590, 210, "outputs, no outcomes", "red", size=20)

or_analogy = Doodle(760, 250, "Doodle comparing a list of train times with a travel goal. A list of trains: the 08:12, the 11:40, the 15:05. A goal: be in Lyon by Friday evening for the wedding. With the goal, a cancelled train is a detour; with only the list, it's a failure.",
                    "“Catch the 08:12” vs “be in Lyon by Friday for the wedding”. Only the second survives a cancelled train.")
or_analogy.box(20, 30, 320, 150, None, "paper")
or_analogy.head(180, 60, "the trains", size=18)
for i, t in enumerate(["08:12 → Paris", "11:40 → Lyon", "15:05 → hotel"]):
    or_analogy.text(180, 98 + i * 28, t, size=16)
or_analogy.box(420, 50, 320, 110, "be in Lyon by Friday", "green", sub="for the wedding", size=18)
or_analogy.note(380, 222, "with the goal, a cancelled train is a detour, not a failure", "pen", size=18)

or_how = Doodle(760, 340, "Grace's outcome-based roadmap for the board, 23 March 2026. Now: fewer refund tickets, substitution refunds from 6.2 to 4 percent by June; current bets: approvals and the no-swaps flag. Next: customers know before the door, where-is-my-order tickets down 30 percent; bet: live order updates. Later: offices order without phoning Mo, three offices self-serve; bet: business accounts. Outcomes are the commitments; features are today's bets and may change.",
                "Outcomes on top are the commitment; the features underneath are today's bets, and may change.")
for i, (when, outcome, target, bets, f) in enumerate([("NOW", "fewer refund tickets", "6.2 % → 4 % by June", "approvals · flag", "green"),
                                                      ("NEXT", "customers know first", "“where is it?” −30 %", "live order update", "y"),
                                                      ("LATER", "offices self-serve", "3 offices, no phone", "business accounts", "paper")]):
    x = 14 + i * 248
    or_how.head(x + 118, 34, when, size=18)
    or_how.box(x, 50, 236, 100, outcome, f, sub=target, size=17, subsize=15)
    or_how.arrow(x + 118, 156, x + 118, 196, dash=True)
    or_how.box(x + 20, 200, 196, 56, bets, "paper", dash=True, size=14, rx=4)
or_how.note(60, 290, "↑ commitment", "green", anchor="start", size=17)
or_how.note(60, 316, "↓ current bets, may change", "pen", anchor="start", size=17)

OUTCOME_RM = dict(
    slug="outcome-roadmaps",
    kicker="a.k.a. “be in Lyon by Friday”",
    tldr="A roadmap of features answers <i>what will we ship?</i>; leaders and investors want <i>what will change?</i>. Put the <b>outcome</b> on top of each column (a measurable change, with a target), and the <b>features underneath as current bets</b>. Commit to the outcomes; keep the features <b>swappable</b>. When a feature turns out not to move the number, you change the bet, not the promise, and the roadmap survives contact with reality.",
    chips=[("Family", "strategy &amp; roadmaps"), ("Origin", "outcome-based roadmapping (C. Todd Lombardo, Bruce McCarthy et al.); Josh Seiden, <i>Outcomes Over Output</i> (2019)"), ("Lives in", "the board deck and the roadmap board"), ("Pairs with", "outcomes over outputs, now / next / later, bets not promises")],
    problem_side="Larder, 23 March 2026",
    problem="""  <p class="lead">Femke's board deck has a slide titled <b>Q2 features</b>: approvals, the “no swaps” flag, live order updates. An investor asks the obvious question: <i>and what will that do?</i> Femke improvises an answer about refunds. The slide lists <b>outputs</b>; <span class="hl-pink">nothing on it says what success looks like</span>, so the board can only judge whether features ship, not whether they work.</p>
  <ul>
    <li>Feature lists invite “is it done?”, not “did it help?”.</li>
    <li>When a feature disappoints, the roadmap has failed, even if the team learned fast.</li>
    <li>Leaders can't see what the features are for.</li>
  </ul>""",
    problem_figs=[or_problem],
    analogy_side="the trip to Lyon",
    analogy="""  <p>A list of <b>train times</b> (08:12, 11:40, 15:05) is a plan of outputs. The <b>goal</b> is “be in Lyon by Friday evening for the wedding”. If the 11:40 is cancelled, the goal makes it a detour: take the bus, or the 12:30. With only the list, a cancelled train is a failure, and you might not even remember why you were going.</p>""",
    analogy_figs=[or_analogy],
    map=[("Be in Lyon by Friday", "The outcome: refund tickets 6.2 % → 4 % by June"),
         ("The trains", "The features: approvals, the flag"),
         ("A cancelled train", "A feature that doesn't move the number"),
         ("Taking the bus instead", "Changing the bet, keeping the outcome"),
         ("The wedding", "Why it matters: customers who trust their order")],
    how_side="outcomes on top, bets below",
    how="""  <p>Grace rewrote the slide for Femke in an hour: three columns, an <b>outcome with a target</b> on top, the <b>current bets</b> below in dashed boxes. At the next board meeting, the investor's question was already answered on the slide, and the conversation moved to the right question: <i>how will you know by June?</i></p>""",
    how_figs=[or_how],
    steps=[("Write each column's outcome", "A change in customer behaviour or a business number, with a target and a date."),
           ("List the bets below", "Features and experiments you believe will move it, marked as current bets."),
           ("Link to the strategy", "Each outcome should match a line in “we'll know by”."),
           ("Commit to outcomes, not bets", "Say so on the slide: features may change."),
           ("Report progress on the outcome", "The number first, then which bets helped."),
           ("Swap bets openly", "When a bet fails, show the new one under the same outcome.")],
    vocab=[("Outcome", "A measurable change in behaviour or results."),
           ("Output", "Something shipped: a feature, a screen."),
           ("Bet", "A feature or experiment expected to move the outcome."),
           ("Target", "The number and date that count as success."),
           ("Leading indicator", "An early signal the outcome is moving."),
           ("Impact", "The business result outcomes add up to.")],
    code=dict(file="product/roadmap/board-2026-03.md", note="the slide Grace wrote for Femke, 23 March 2026", plain=True, src="""
# Ordering · what will change in 2026            commitments are outcomes; bets may change

NOW (to June)       Fewer refund tickets
                    substitution refund tickets 6.2 % → 4 % of orders by end June
                    bets: approvals in the app (Amsterdam Apr, Rotterdam Jun) ·
                          "no swaps" flag (live since 23 Feb)
NEXT (Q3)           Customers know before the door
                    "where is my order?" tickets −30 % by end September
                    bet: live order updates with the substitute and its price
LATER (Q4 →)        Offices order for themselves
                    3 offices ordering without phoning Mo
                    bet: business accounts (only if the Korenwolf pilot works)

How we'll report    the number first, then which bets moved it, then what we changed.
"""),
    tools="tools: the same board as the now / next / later roadmap, with an outcome row on top; Productboard and Aha! support objectives linked to features. Pair with OKRs (Vol. 4).",
    gains=["<b>Leaders see what changes</b>, not just what ships.",
           "<b>Bets can change</b> without breaking a promise.",
           "<b>Progress reports focus on results</b>.",
           "<b>Teams own the outcome</b>, not a feature list.",
           "<b>Better questions</b> from the board: how will you know?"],
    losses=["<b>Harder to write</b>: good outcomes take thought.",
            "<b>Some stakeholders still want feature dates</b>.",
            "<b>Outcomes can lag</b>: results show up after the release.",
            "<b>Needs measurement</b> that actually works."],
    baseline="Each line compares <b>a roadmap of features to ship</b> to <b>a roadmap of outcomes with targets, with the features underneath as current bets</b>.",
    ratings=[(2, 4, "Outcomes are written from the customer's side."),
             (2, 5, "Targets tie straight to refunds and tickets."),
             (2, 4, "Bets are judged by the number they move."),
             (2, 4, "A failing bet is spotted and swapped early."),
             (2, 4, "Three outcomes, a few bets each."),
             (2, 5, "Everyone can see what each feature is for."),
             (2, 5, "The board sees results, not just deliveries."),
             (3, 3, "Doesn't change flow directly."),
             (3, 3, "More thought up front; easier updates later.")],
    pitfalls=[("Outputs disguised as outcomes", "“Outcome: launch approvals.”", "an outcome is a measured change, not a release."),
              ("No target", "“Fewer refund tickets.”", "add a number and a date: 6.2 % → 4 % by June."),
              ("Bets set in stone", "Approvals are “committed” even if they fail.", "commit to outcomes; mark features as current bets."),
              ("Outcomes nobody measures", "“Customers know first”, no data.", "pick outcomes you can measure today.")],
    use=["Roadmaps for leadership, boards and investors.",
         "When “is it done?” crowds out “did it work?”.",
         "Teams trusted to choose their own solutions.",
         "Alongside OKRs."],
    skip=["Contract deliverables with fixed scope.",
          "When you can't measure the outcome yet: fix measurement first."],
    related=["<b>Now / next / later roadmap</b> (this volume)", "<b>Bets, not promises</b> (this volume)", "<b>Outcomes over outputs</b> (Vol. 1)", "<b>Product strategy on a page</b> (this volume)"],
    quiz=[("What goes on top of each column?", "An outcome: a measurable change with a target and a date."),
          ("What's the status of the features underneath?", "Current bets: they may change if they don't move the outcome."),
          ("What do you report first?", "The outcome number, then which bets moved it."),
          ("Turn “launch live order updates” into an outcome.", "For example: “where is my order?” tickets down 30 % by end September.")],
    try_it="Take your current roadmap. Above each column or theme, write one outcome with a number and a date. Move the features underneath and label them “current bets”. Show it to a leader who usually asks for feature dates and note which question they ask first.",
    remember="Promise <span class=\"hl\">Lyon by Friday</span>, not the 11:40. Features are <span class=\"hl\">bets</span>.",
    sources=["Josh Seiden, <i>Outcomes Over Output</i> (2019).",
             "C. Todd Lombardo, Bruce McCarthy et al., <i>Product Roadmaps Relaunched</i> (2017).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018).",
             "Christina Wodtke, <i>Radical Focus</i> (2016)."],
)

# ------------------------------------------------------------------ 12 Roadmap vs Release Plan
rr_problem = Doodle(760, 220, "Doodle of a misunderstanding on 9 March 2026. Sanne reads Grace's roadmap as a release plan: Now means done by 31 March. She tells Joost that approvals will be live in Rotterdam at launch. Grace never said that; one document was being used for two jobs.",
                    "One document, two jobs. Sanne reads “Now” as “done by 31 March” and promises Joost a date.")
rr_problem.box(20, 30, 260, 90, "Grace's roadmap", "y", sub="why · what order")
rr_problem.arrow(286, 75, 360, 75)
rr_problem.box(366, 30, 180, 90, "Sanne reads", "paper", sub="“Now = by 31 Mar”")
rr_problem.arrow(552, 75, 600, 75)
rr_problem.box(606, 30, 140, 90, "Joost", "pink", sub="“RTM approvals!”", stroke="red", subsize=14)
rr_problem.note(380, 180, "a promise nobody made", "red", size=22)

rr_analogy = Doodle(760, 250, "Doodle of a restaurant's menu next to the kitchen's service plan for tonight. The menu says what the restaurant serves and why. The service plan says which table gets which course at what time, and changes every hour.",
                    "The menu says what we serve and why. Tonight's service plan says which table gets what, when.")
rr_analogy.icon("menu", 60, 30, 1.5)
rr_analogy.box(20, 140, 220, 70, "the menu", "y", sub="what and why")
rr_analogy.icon("clock", 530, 40, 1.2)
rr_analogy.box(420, 140, 320, 70, "tonight's service plan", "blue", sub="table 4, mains at 20:15", size=17)
rr_analogy.note(380, 240, "different jobs, different documents", "pen")

rr_how = Doodle(760, 340, "Grace's roadmap and Sanne's release plan side by side. The roadmap: outcomes and order, now, next, later, no dates beyond now, owned by Grace, updated monthly. The release plan: increments with dates and confidence, owned by Sanne with Grace, updated weekly. Approvals: R1, staff test at Noord, 30 March, 90 percent confidence; R2, all Amsterdam behind a flag, 13 April, 80 percent; R3, Rotterdam, first planned for 27 April, moved to June after the trade-off sliders on 31 March.",
                "Two documents, two owners, two rhythms. The release plan carries the dates, with how sure we are.")
rr_how.box(14, 14, 300, 200, None, "y")
rr_how.head(164, 46, "roadmap", size=19)
for i, t in enumerate(["outcomes, order", "now · next · later", "no dates beyond now", "Grace · monthly"]):
    rr_how.text(164, 86 + i * 32, t, size=16)
rr_how.box(340, 14, 406, 200, None, "blue")
rr_how.head(543, 46, "release plan: approvals", size=17)
for i, (r, d, c) in enumerate([("R1 staff test, Noord", "30 Mar", "90 %"), ("R2 all Amsterdam (flag)", "13 Apr", "80 %"), ("R3 Rotterdam", "Jun", "70 %")]):
    y = 92 + i * 40
    rr_how.text(354, y, r, anchor="start", size=15)
    rr_how.text(640, y, d, size=15)
    rr_how.text(712, y, c, "t-head", size=15)
rr_how.note(520, 236, "R3 was 27 Apr → June (sliders, 31 Mar)", "red", size=16)
rr_how.note(380, 290, "Sanne + Grace · weekly", "pen", size=18)
rr_how.note(380, 322, "dates live here, with how sure we are", "green", size=18)

ROADMAP_RELEASE = dict(
    slug="roadmap-vs-release-plan",
    kicker="a.k.a. “the menu and tonight's service”",
    tldr="A <b>roadmap</b> says <b>why and in what order</b>: outcomes and bets, with no firm dates beyond now. A <b>release plan</b> says <b>which increments ship when</b>, with dates and a <b>confidence level</b> for each. They have different owners (the product owner; the delivery manager with the PO), different rhythms (monthly; weekly) and different audiences. Keep them as <b>two documents</b>, link them, and when people ask “when?”, send them to the release plan.",
    chips=[("Family", "strategy &amp; roadmaps"), ("Origin", "agile release planning (Mike Cohn); roadmap practice (Roman Pichler, ProdPad)"), ("Lives in", "two linked pages: the roadmap and the release plan"), ("Pairs with", "now / next / later roadmap, MoSCoW, trade-off sliders")],
    problem_side="Larder, 9 March 2026",
    problem="""  <p class="lead">Sanne, the delivery manager for the Rotterdam launch, reads Grace's new roadmap. “Approvals” is in <b>Now</b>, so Sanne assumes it's <b>done by 31 March</b>, ready for Rotterdam on 27 April, and tells Joost so. Joost tells his store managers. Grace never said that: <span class="hl-pink">one document was doing two jobs</span>, and a promise appeared that nobody had made.</p>
  <ul>
    <li>A roadmap without dates gets dates read into it.</li>
    <li>A release plan without a why gets reshuffled by whoever asks loudest.</li>
    <li>Confidence levels are missing, so every date sounds certain.</li>
  </ul>""",
    problem_figs=[rr_problem],
    meanwhile=[("architect-2", "trade-off-sliders", "on 31 March these sliders moved approvals in Rotterdam (R3) from launch day to June in Grace and Sanne's release plan.", "Grace and Sanne's release plan moved approvals in Rotterdam (R3) from 27 April to June after this meeting.")],
    analogy_side="the menu and tonight's service",
    analogy="""  <p>A restaurant's <b>menu</b> says what it serves and why: seasonal, local, the chef's style. It changes a few times a year. The kitchen's <b>service plan</b> for tonight says table 4 gets mains at 20:15, table 7 is waiting on the fish. It changes every hour. Nobody hands the guests the service plan, or runs the kitchen from the menu.</p>""",
    analogy_figs=[rr_analogy],
    map=[("The menu", "The roadmap: outcomes, bets, order"),
         ("The chef", "Grace, who owns it, updated monthly"),
         ("Tonight's service plan", "The release plan: increments with dates"),
         ("The head waiter", "Sanne, who owns it with Grace, updated weekly"),
         ("“Mains in about 10 minutes”", "A date with a confidence level")],
    how_side="two documents, linked",
    how="""  <p>Grace and Sanne split it the same week. The roadmap stayed as it was. Sanne's <b>release plan</b> lists increments with dates and how sure they are: R1, a staff test at Noord on 30 March (90 %); R2, all of Amsterdam behind a flag on 13 April (80 %); R3, Rotterdam. Joost got a corrected message the same day. On <b>31 March</b>, the trade-off sliders moved R3 to June, a one-line change in one document, explained by the other.</p>""",
    how_figs=[rr_how],
    steps=[("Separate the documents", "Roadmap: outcomes, bets, order. Release plan: increments, dates, confidence."),
           ("Name the owners", "Roadmap: the product owner. Release plan: the delivery manager, with the PO."),
           ("Give every date a confidence", "90 % for this sprint, 70 % for next month; say what would change it."),
           ("Link them both ways", "Each release names its roadmap item; each roadmap item links its releases."),
           ("Set two rhythms", "Roadmap monthly; release plan weekly."),
           ("Send “when?” to the release plan", "And “why?” to the roadmap.")],
    vocab=[("Roadmap", "Why and in what order: outcomes and bets."),
           ("Release plan", "Which increments ship when, with confidence."),
           ("Increment", "A releasable slice of a feature."),
           ("Confidence level", "How sure we are of a date, in percent."),
           ("Release train", "A regular release rhythm (e.g. every two weeks)."),
           ("Delivery manager", "Owns the plan for getting work out: dates, risks, dependencies.")],
    code=dict(file="delivery/release-plan.md", note="Sanne's release plan for approvals, updated 31 March 2026", plain=True, src="""
# Release plan · substitution approvals        owner: Sanne (with Grace) · updated weekly
Roadmap item: "Approvals" (bet 1, outcome: refund tickets 6.2 % → 4 % by June)

| Release | What                                 | Date    | Confidence | Depends on              |
|---------|--------------------------------------|---------|------------|-------------------------|
| R1      | Staff test at Noord, 20 orders/day   | 30 Mar  | 90 %       | picker app 3.4          |
| R2      | All Amsterdam express, behind a flag | 13 Apr  | 80 %       | R1 answer rate ≥ 70 %   |
| R3      | Rotterdam                            | June    | 70 %       | RTM stable after launch |

Change log
  09 Mar  plan created; Joost told: approvals are NOT in Rotterdam on day one (was a misread)
  31 Mar  R3 moved 27 Apr → June: trade-off sliders put the launch date above feature scope
"""),
    tools="tools: the roadmap board plus a release-plan table or a delivery tool (Jira versions, Linear cycles, a spreadsheet). Confidence levels can be a simple column.",
    gains=["<b>No accidental promises</b> from a misread roadmap.",
           "<b>Dates with confidence</b>: honest and useful.",
           "<b>Clear owners</b> for why and for when.",
           "<b>Changes are explained</b>: the roadmap says why a date moved.",
           "<b>Each audience gets the right document</b>."],
    losses=["<b>Two documents</b> to keep in sync.",
            "<b>Confidence levels are judgement</b>, not science.",
            "<b>Some people read only one</b>.",
            "<b>Weekly updates</b> take Sanne's time."],
    baseline="Each line compares <b>one roadmap used as both strategy and schedule</b> to <b>a roadmap (why, order) and a separate release plan (increments, dates, confidence), linked</b>.",
    ratings=[(3, 3, "Customers get releases on dates that hold."),
             (3, 3, "Indirect: fewer slips on business dates."),
             (2, 3, "Confidence levels are judgement, made explicit."),
             (3, 4, "Small increments (R1, R2) teach early."),
             (3, 4, "The roadmap stays on outcomes."),
             (2, 5, "Everyone knows where to look for why and when."),
             (1, 4, "No more promises nobody made."),
             (2, 4, "Increments flow on a weekly plan."),
             (3, 3, "Two documents, two rhythms.")],
    pitfalls=[("Dates on the roadmap", "“Now = by 31 March.”", "dates live only in the release plan."),
              ("Dates without confidence", "“13 April” sounds certain.", "add a percentage and what it depends on."),
              ("Plans that don't link", "Releases with no outcome; roadmap items with no release.", "link both ways."),
              ("Big-bang releases", "One release, one date, all or nothing.", "plan small increments: staff test, one city, then more.")],
    use=["Any team with a delivery manager or a fixed launch date.",
         "When roadmap items are read as promises.",
         "Coordinating releases across teams or cities.",
         "Reporting to operations who need dates."],
    skip=["Tiny teams shipping continuously with no external dates.",
          "When there's one release and one date: a release plan alone is enough."],
    related=["<b>Now / next / later roadmap</b> (this volume)", "<b>MoSCoW and its traps</b> (this volume)", "<b>Bets, not promises</b> (this volume)", "<b>Trade-off sliders</b> (Ana, book 1 vol. 2)"],
    quiz=[("What does a roadmap answer, and a release plan?", "Roadmap: why and in what order. Release plan: what ships when, with confidence."),
          ("Who owns each?", "The roadmap: the product owner. The release plan: the delivery manager, with the PO."),
          ("Why add confidence levels to dates?", "So people know how sure the date is and what would change it."),
          ("Approvals in Rotterdam moved to June. Where is that recorded?", "In the release plan's change log, with the reason (the trade-off sliders).")],
    try_it="Find the dates people quote from your roadmap. Move them into a separate release plan, one line per increment, with a confidence percentage and what each depends on. Ask your delivery manager (or yourself) to own it weekly, and link the two documents both ways.",
    remember="The <span class=\"hl\">menu</span> says why. Tonight's <span class=\"hl\">service plan</span> says when, and how sure.",
    sources=["Mike Cohn, <i>Agile Estimating and Planning</i> (2005), on release planning.",
             "Roman Pichler, “Product Roadmap vs. Release Plan” (romanpichler.com, 2016).",
             "C. Todd Lombardo et al., <i>Product Roadmaps Relaunched</i> (2017).",
             "Troy Magennis, on forecasting with confidence levels (Focused Objective)."],
)

NOTES = [STRATEGY, NNL, OUTCOME_RM, ROADMAP_RELEASE]
