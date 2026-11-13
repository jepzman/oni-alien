# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 5 · Managing up and across.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Managing Up
mu_problem = Doodle(760, 280, "Doodle of October 2026. Priya has been surprised twice in a month: she heard about the live-updates guardrail trip from Femke, and about the slot waitlist being switched off from Sam. Grace thought both were too small to bother her with. Priya felt blindsided in front of her own boss.",
                    "Priya heard about two of Grace's decisions from other people. Grace thought they were too small to mention.")
mu_problem.box(20, 40, 320, 90, "guardrail trip", "pink", sub="Priya heard it from Femke")
mu_problem.box(400, 40, 340, 90, "waitlist switched off", "pink", sub="Priya heard it from Sam")
mu_problem.note(380, 200, "too small to mention, big enough to surprise", "red", size=18)

mu_analogy = Doodle(760, 250, "Doodle of a co-pilot: they don't fly the plane for the captain, and they don't stay silent either. They call out what the captain needs to know, early, in the agreed words: fuel, weather, a warning light. No surprises in the cockpit.",
                     "A co-pilot calls out what the captain needs, early, in agreed words. No surprises in the cockpit.")
mu_analogy.icon("phone", 40, 60, 1.3)
for i, (t, f) in enumerate([("fuel", "y"), ("weather", "blue"), ("warning light", "pink")]):
    mu_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
mu_analogy.note(450, 200, "call it out early, in agreed words", "pen")

mu_how = Doodle(760, 380, "Grace's way of working with Priya from 19 October 2026. A shared one-to-one document, updated before each weekly thirty minutes: decisions I need from you; risks, with what I'm doing; decisions I made, so you hear it from me; wins worth passing up. One rule: no surprises; bad news within a day, in person or a call. And learning Priya's style: numbers before stories, a written pre-read for anything she must defend to Femke.",
                 "A shared 1:1 doc: decisions needed, risks, decisions made, wins. One rule: no surprises.")
for i, (t, s, f) in enumerate([("decisions I need", "from you, by when", "y"), ("risks", "and what I'm doing", "pink"), ("decisions I made", "so you hear it from me", "blue"), ("wins", "worth passing up", "green")]):
    r, c = divmod(i, 2)
    mu_how.box(14 + c * 372, 14 + r * 96, 360, 84, t, f, sub=s, size=17)
mu_how.box(14, 214, 732, 56, "rule: no surprises · bad news within a day, in person", "pink", size=15)
mu_how.note(380, 310, "Priya's style: numbers before stories, written pre-reads", "pen", size=15)
mu_how.note(380, 344, "weekly, 30 minutes, the doc updated the day before", "green", size=15)

UP = dict(
    slug="managing-up",
    kicker="a.k.a. “the co-pilot's call-outs”",
    tldr="<b>Managing up</b> means making it easy for your manager to back you: <b>no surprises</b>, a <b>regular, short channel</b> where they see the decisions you need, the risks and what you're doing about them, the decisions you've made, and the wins worth passing on. Learn how they like information (numbers or stories, written or spoken) and what they must defend to their own boss. It isn't flattery; it's keeping the person who carries your work upstairs well informed.",
    chips=[("Family", "managing up and across"), ("Origin", "John Gabarro and John Kotter, “Managing Your Boss” (HBR, 1980)"), ("Lives in", "a shared one-to-one document and a weekly slot"), ("Pairs with", "product update that gets read, delivering bad news, pitching to the CEO")],
    problem_side="Larder, 19 October 2026",
    problem="""  <p class="lead">Priya has been surprised twice in a month: she heard about the <b>live-updates guardrail trip</b> from Femke, and about the <b>slot waitlist</b> being switched off from Sam. Grace thought both were too small to bother her with. <span class="hl-pink">Priya felt blindsided in front of her own boss</span>, and started asking for daily status messages.</p>
  <ul>
    <li>What's small to you can be big for your manager.</li>
    <li>Surprises cost trust, and trust costs autonomy.</li>
    <li>Without a channel, information arrives by accident.</li>
  </ul>""",
    problem_figs=[mu_problem],
    analogy_side="the co-pilot",
    analogy="""  <p>A <b>co-pilot</b> doesn't fly the plane for the captain, and doesn't stay silent either. They <b>call out</b> what the captain needs to know (fuel, weather, a warning light) <b>early</b>, in <b>agreed words</b>. The captain never learns about the warning light from air traffic control.</p>""",
    analogy_figs=[mu_analogy],
    map=[("The captain", "Priya, who answers to Femke"),
         ("Call-outs", "The shared 1:1 document"),
         ("A warning light", "A guardrail tripping, a feature removed"),
         ("Agreed words", "Decisions needed, risks, decisions made, wins"),
         ("Air traffic control", "Hearing it from Femke or Sam first")],
    how_side="a shared doc, one rule, her style",
    how="""  <p>Grace set up a <b>shared one-to-one document</b>, updated the day before their weekly 30 minutes: <b>decisions I need</b> (by when), <b>risks</b> (and what I'm doing), <b>decisions I made</b> (so you hear it from me), <b>wins</b> worth passing up. One rule: <b>no surprises</b>, bad news within a day, in person. She learned Priya's style: <b>numbers before stories</b>, and a written pre-read for anything Priya must defend to Femke. After a month Priya dropped the daily status request.</p>""",
    how_figs=[mu_how],
    steps=[("Ask what they need", "What they must answer for, to whom."),
           ("Set a regular channel", "A weekly slot and a shared document."),
           ("Use four headings", "Decisions needed, risks, decisions made, wins."),
           ("Agree “no surprises”", "Bad news within a day, in person."),
           ("Learn their style", "Numbers or stories; written or spoken."),
           ("Make them look good", "Give them what they need to defend your work.")],
    vocab=[("Managing up", "Working well with your manager so they can support you."),
           ("No surprises", "Your manager hears important news from you first."),
           ("One-to-one", "A regular meeting between a manager and a report."),
           ("Escalation", "Bringing a problem to someone with more authority."),
           ("Working style", "How a person prefers to get and use information."),
           ("Air cover", "A manager's support when work is challenged.")],
    code=dict(file="product/1on1/priya-grace.md", note="the shared 1:1 doc, week of 26 October 2026", plain=True, src="""
# Priya ↔ Grace · weekly 1:1 · Tue 10:00, 30 min · updated Mon

DECISIONS I NEED FROM YOU
  - OK to spend 2 sprints of Dee's team on Korenwolf's office-manager screens? (by 30 Oct)
RISKS (and what I'm doing)
  - Korenwolf 4 Jan depends on billing (Cho) and vans (Eli): dependency board from 16 Nov
  - Swap refunds at 2.6 %, December goal 2.0 %: forecast in early Dec; I'll tell you first
DECISIONS I MADE (so you hear it from me)
  - Live timeline on web ships 9 Nov, courier first name only (agreed with Lena)
WINS (to pass up)
  - Ops feedback loop: 14 items in 3 weeks; swaps accepted 71 % → 78 %
"""),
    tools="tools: a shared document, a weekly calendar slot, and the product update for the wider picture.",
    gains=["<b>No more surprises</b> for your manager.",
           "<b>Decisions faster</b>: asked clearly.",
           "<b>More autonomy</b>, earned by trust.",
           "<b>Better air cover</b> when work is challenged.",
           "<b>Your wins</b> reach leadership."],
    losses=["<b>A weekly habit</b>.",
            "<b>Judgment</b> about what's worth mentioning.",
            "<b>Bad news</b> said out loud, early.",
            "<b>Different managers</b> need different styles."],
    baseline="Each line compares <b>telling your manager only big things, irregularly</b> to <b>a weekly shared doc with decisions, risks, decisions made and wins, and a no-surprises rule</b>.",
    ratings=[(3, 3, "Indirect."),
             (3, 4, "Priya can defend the roadmap upstairs."),
             (3, 4, "Risks come with numbers."),
             (3, 4, "Problems surface within a day."),
             (2, 4, "Decisions needed are listed and dated."),
             (2, 4, "Priya and Grace share one picture."),
             (1, 5, "No surprises; daily status dropped."),
             (3, 3, "Neutral."),
             (2, 4, "Thirty minutes a week replaces daily messages.")],
    pitfalls=[("Only big news", "Small decisions surprise her later.", "list decisions made, every week."),
              ("Problems without plans", "“We have an issue.”", "the risk and what you're doing."),
              ("Bad news by email", "Discovered at night.", "in person or a call, within a day."),
              ("Your style, not theirs", "Stories for a numbers person.", "learn how they like it.")],
    use=["With any manager, from the first week.",
         "When your manager seems surprised or anxious.",
         "Before asking for more autonomy.",
         "When your work is politically exposed."],
    skip=["Never; only the format changes."],
    related=["<b>Product update that gets read</b> (this volume)", "<b>Delivering bad news</b> (this volume)", "<b>Pitching to the CEO</b> (this volume)", "<b>Decision rights</b> (Ana, book 1 vol. 2)"],
    quiz=[("What does “no surprises” mean?", "Your manager hears important news from you first."),
          ("What are the four headings?", "Decisions I need, risks, decisions I made, wins."),
          ("Why list decisions you made?", "So your manager hears them from you, not from others."),
          ("What changed after a month?", "Priya dropped the request for daily status messages.")],
    try_it="Ask your manager what they have to answer for to their boss. Then start a shared doc with the four headings, update it before your next one-to-one, and agree a “no surprises” rule.",
    remember="Be the <span class=\"hl\">co-pilot</span>: call out the warning light before <span class=\"hl\">air traffic control</span> does.",
    sources=["John Gabarro and John Kotter, “Managing Your Boss”, <i>Harvard Business Review</i> (1980).",
             "Kim Scott, <i>Radical Candor</i> (2017).",
             "Mary Abbajay, <i>Managing Up</i> (2018).",
             "Marty Cagan, <i>Empowered</i> (2020), on product leaders and teams."],
)

# ------------------------------------------------------------------ 06 Pitching to the CEO
pc_problem = Doodle(760, 280, "Doodle of November 2026. Grace wants to let customers add items for a few minutes after ordering: eight percent of express customers place a second order within thirty minutes, and each costs another courier trip. Her first draft for Femke is twelve slides, starting with the research method. Femke has ten minutes between board calls.",
                    "A strong idea, a twelve-slide deck starting with the research method, and a CEO with ten minutes.")
pc_problem.box(20, 40, 320, 90, "12 slides", "paper", sub="slide 1: “our method”")
pc_problem.box(400, 40, 340, 90, "Femke", "y", sub="10 minutes between calls")
pc_problem.note(380, 200, "the answer is on slide 11", "red", size=20)

pc_analogy = Doodle(760, 250, "Doodle of a lift pitch: the investor gets in on the ground floor and gets out on the sixth. You say what you want, why it matters to them in their terms, and the small next step, before the doors open.",
                     "A lift pitch: what you want, why it matters to them, the small next step, before the doors open.")
pc_analogy.icon("turnstile", 40, 60, 1.3)
for i, (t, f) in enumerate([("the answer", "y"), ("their terms", "blue"), ("small ask", "green")]):
    pc_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
pc_analogy.note(450, 200, "before the doors open", "pen")

pc_how = Doodle(760, 400, "Grace's pitch to Femke on 30 November 2026, one page, ten minutes. The answer first: let customers add items for ten minutes after ordering. In Femke's terms: 8 percent of express customers place a second order within 30 minutes; each costs a courier trip of about 4.50 euros; about 22,000 euros a month, and bigger baskets. The risk: picking may already have started; the ten-minute window ends before release to the store. The small ask: four weeks of Dee's team and a test in Amsterdam in January, with a stop rule. Femke said yes to the test in the room.",
                 "Answer first, in her terms, the risk named, a small ask with a stop rule. Yes in the room.")
for i, (t, s, f) in enumerate([("answer", "add items for 10 min after ordering", "y"), ("her terms", "≈ €22k a month in second trips · bigger baskets", "blue"),
                               ("the risk", "picking started → window ends before release", "pink"), ("small ask", "4 weeks, Amsterdam test, a stop rule", "green")]):
    y = 14 + i * 62
    pc_how.box(14, y, 732, 52, None, f, rx=6)
    pc_how.text(30, y + 33, t, "t-head", anchor="start", size=16)
    pc_how.text(730, y + 33, s, anchor="end", size=14)
pc_how.note(380, 290, "one page · ten minutes · questions after", "pen", size=16)
pc_how.note(380, 326, "Femke: “yes to the test; show me in February”", "green", size=16)

PITCH = dict(
    slug="pitching-to-ceo",
    kicker="a.k.a. “the lift pitch”",
    tldr="A CEO has little time and many asks. Pitch with the <b>answer first</b> (what you want to do), then <b>why it matters in their terms</b> (money, customers, the strategy they've promised), the <b>main risk</b> and how you'll handle it, and a <b>small ask</b>: a test, a few weeks, a stop rule. Put it on one page, keep it to ten minutes, and leave the method for questions. A small yes now beats a big maybe later.",
    chips=[("Family", "managing up and across"), ("Origin", "the pyramid principle (Minto); lean experimentation"), ("Lives in", "a one-page pitch and a ten-minute slot"), ("Pairs with", "business case one-pager, bets not promises, managing up")],
    problem_side="Larder, 30 November 2026",
    problem="""  <p class="lead">Grace wants to let customers <b>add items for a few minutes after ordering</b>: <b>8 %</b> of express customers place a <b>second order</b> within 30 minutes, and each costs another courier trip. Her first draft for Femke is <b>twelve slides</b> that start with the research method. <span class="hl-pink">The answer is on slide 11</span>, and Femke has ten minutes between board calls.</p>
  <ul>
    <li>Leaders decide in minutes; decks are built for hours.</li>
    <li>The method impresses the presenter, not the listener.</li>
    <li>Big asks get “let's discuss later”.</li>
  </ul>""",
    problem_figs=[pc_problem],
    analogy_side="the lift pitch",
    analogy="""  <p>An investor steps into the <b>lift</b> on the ground floor and gets out on the sixth. In that time you say <b>what you want</b>, <b>why it matters to them</b> in their terms, and the <b>small next step</b>. The details come later, if the doors open on a yes.</p>""",
    analogy_figs=[pc_analogy],
    map=[("Six floors", "Ten minutes between board calls"),
         ("What you want", "Add items for ten minutes after ordering"),
         ("Their terms", "≈ €22k a month in courier trips, bigger baskets"),
         ("The small next step", "Four weeks, a test in Amsterdam, a stop rule"),
         ("Details if the doors open", "Research method kept for questions")],
    how_side="answer, their terms, the risk, a small ask",
    how="""  <p>Grace rewrote it as <b>one page</b>. <b>Answer</b>: let customers add items for ten minutes after ordering. <b>Femke's terms</b>: second orders cost about <b>€4.50</b> each in courier time, about <b>€22,000 a month</b>, and baskets grow. <b>Risk</b>: picking may have started, so the window ends <b>before release to the store</b> (Ana's suggestion). <b>Ask</b>: four weeks of Dee's team and a <b>test in Amsterdam</b> in January, stopping if picking delays rise. Femke said <b>yes to the test</b> in the room: “show me in February.”</p>""",
    how_figs=[pc_how],
    meanwhile=[("architect-3", "presenting-to-executives", "two days later, Ana pitches the warehouse decision to Femke, and it fails the first time.",
                "Two days earlier, Grace pitched order editing to Femke with the answer first, and got a yes to a test.")],
    steps=[("Lead with the answer", "One sentence: what you want to do."),
           ("Say why in their terms", "Money, customers, the promises they've made."),
           ("Name the main risk", "And how you'll handle it."),
           ("Make the ask small", "A test, a few weeks, a stop rule."),
           ("Fit it on one page", "The method in the appendix."),
           ("Leave with a decision", "Yes, no, or what would make it yes.")],
    vocab=[("Pitch", "A short case for a decision."),
           ("Answer first", "Starting with the conclusion, not the background."),
           ("Stop rule", "A condition agreed in advance for ending a test."),
           ("Second order", "A customer ordering again soon after, for forgotten items."),
           ("Courier trip cost", "The cost of one extra delivery."),
           ("Ask", "The specific decision you want.")],
    code=dict(file="product/pitches/order-editing.md", note="the one-page pitch, 30 November 2026", plain=True, src="""
# Pitch: add items after ordering · Grace → Femke · 30 Nov 2026 · 10 min

ANSWER    Let express customers add items for 10 minutes after they order.
WHY       8 % of express customers place a 2nd order within 30 min (≈ 4,900 a month)
          each costs a courier trip ≈ €4.50 → ≈ €22k a month · basket +€6 when added in-order
RISK      Picking may have started → window closes before release to store (Ana: no change
          to picking) · watch: picking delays, payment re-authorisations
ASK       4 weeks of Dee's team · test in Amsterdam, January, 50 % of customers
STOP IF   orders released to store later than today by > 1 min on average
DECISION  Yes to the test (Femke, 30 Nov) · results review in February
"""),
    tools="tools: one page; the numbers from the health page and support data; a stop rule on the test card.",
    gains=["<b>A decision</b> in ten minutes.",
           "<b>Speaks the CEO's language</b>.",
           "<b>Small asks</b> get a yes.",
           "<b>Risk named</b> up front builds trust.",
           "<b>Learning fast</b> through a test."],
    losses=["<b>Hard to compress</b> to a page.",
            "<b>Nuance</b> waits for questions.",
            "<b>Small asks</b> may need a second pitch.",
            "<b>Needs good numbers</b> ready."],
    baseline="Each line compares <b>a long deck building up to the answer</b> to <b>a one-page pitch: answer first, in the CEO's terms, the risk, a small ask</b>.",
    ratings=[(2, 4, "Customers who forgot an item get it in the same delivery."),
             (2, 5, "≈ €22k a month in Femke's terms."),
             (2, 4, "Numbers from orders and support."),
             (2, 5, "A test in January, results in February."),
             (2, 4, "One ask, one test."),
             (3, 4, "Femke, Priya and Dee know the plan."),
             (2, 5, "A clear page and a stop rule build trust."),
             (3, 3, "Neutral."),
             (2, 4, "One page instead of twelve slides.")],
    pitfalls=[("Building up to it", "Method, data, then the idea.", "the answer first."),
              ("Your terms", "Story points and NPS.", "money and customers."),
              ("A big ask", "“A team for a year.”", "a test with a stop rule."),
              ("Hiding the risk", "Found by the CEO's first question.", "name it first.")],
    use=["Asking leaders for money, people or a change of plan.",
         "Short slots with busy executives.",
         "Ideas that need a test before a commitment.",
         "Any pitch that's grown past one page."],
    skip=["Decisions inside your own authority: just decide and tell them."],
    related=["<b>Business case one-pager</b> (Vol. 2)", "<b>Managing up</b> (this volume)", "<b>A/B tests</b> (Vol. 4)", "<b>Presenting to executives</b> (Ana, book 1 vol. 3)"],
    quiz=[("What comes first in a pitch?", "The answer: what you want to do."),
          ("Why make the ask small?", "A small, testable ask gets a yes; a big one gets “later”."),
          ("What did Grace ask Femke for?", "Four weeks of Dee's team and a test in Amsterdam, with a stop rule."),
          ("How did she handle the main risk?", "The edit window closes before the order is released to the store.")],
    try_it="Take an idea you want leadership to back. Write it on one page: the answer, why in their terms, the main risk, a small ask with a stop rule. Read it aloud in under three minutes.",
    remember="Pitch it in the <span class=\"hl\">lift</span>: the answer, their terms, and a small <span class=\"hl\">next step</span>.",
    sources=["Barbara Minto, <i>The Pyramid Principle</i> (1987).",
             "Chip and Dan Heath, <i>Made to Stick</i> (2007).",
             "Oren Klaff, <i>Pitch Anything</i> (2011).",
             "Eric Ries, <i>The Lean Startup</i> (2011)."],
)

# ------------------------------------------------------------------ 07 Dependencies across Teams
dp_problem = Doodle(760, 280, "Doodle of November 2026. Korenwolf goes live on 4 January, and Grace's work depends on three other teams: billing must create invoice lines per cost centre (Cho), Dispatch must plan van routes (Eli), and operations must staff picking from 06:00 (Joost). Each team has its own priorities, and each dependency lives in a different chat thread.",
                    "4 January depends on billing, vans and early picking: three teams, three priorities, three chat threads.")
dp_problem.box(270, 20, 220, 70, "4 Jan go-live", "pink", size=16, stroke="red")
for i, (t, who, f) in enumerate([("billing lines", "Cho", "y"), ("van routes", "Eli", "blue"), ("06:00 picking", "Joost", "green")]):
    x = 20 + i * 250
    dp_problem.box(x, 140, 220, 70, t, f, sub=who, size=16)
    dp_problem.arrow(x + 110, 136, 380, 94)
dp_problem.note(380, 250, "each in a different chat thread", "red", size=18)

dp_analogy = Doodle(760, 250, "Doodle of a wedding planner's board: the venue, the caterer, the band, the flowers, each with what's needed, by when, the agreed date and a colour. The planner calls each supplier weekly, and where she can, removes the dependency: the cake from the caterer, not a separate baker.",
                     "A wedding planner's board: each supplier, what's needed, by when. Where possible, one fewer supplier.")
dp_analogy.icon("calendar", 30, 60, 1.2)
for i, (t, f) in enumerate([("venue", "green"), ("caterer", "y"), ("band", "pink"), ("flowers", "green")]):
    dp_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=16)
dp_analogy.note(450, 200, "call weekly; remove one when you can", "pen")

dp_how = Doodle(760, 400, "Grace's dependency board from 16 November 2026. Each line: what we need, from whom, needed by, the date they agreed, status. Billing invoice lines per cost centre, Cho, needed 11 December, agreed 4 December, green. Van routes the evening before, Eli, needed 14 December, agreed 7 December, then amber when it slipped a week. Picking from 06:00, Joost, needed 4 January, agreed, green. Asked in person, tracked in a weekly fifteen-minute sync. Removed one dependency: the cost centre field built in Ordering by Grace's team instead of waiting for billing's form. The van slip was seen three weeks early.",
                 "What, who, needed by, agreed date, status. Asked in person, synced weekly, one removed. The slip seen three weeks early.")
dp_how.head(20, 30, "need", anchor="start", size=15)
dp_how.head(300, 30, "who", anchor="start", size=15)
dp_how.head(400, 30, "needed", anchor="start", size=15)
dp_how.head(530, 30, "agreed", anchor="start", size=15)
dp_how.head(660, 30, "status", anchor="start", size=15)
for i, (n, w, nb, ag, st, f) in enumerate([("cost-centre invoice lines", "Cho", "11 Dec", "4 Dec", "green", "green"), ("van routes, evening before", "Eli", "14 Dec", "7 → 14 Dec", "amber", "y"),
                                           ("picking from 06:00", "Joost", "4 Jan", "4 Jan", "green", "green"), ("cost centre form", "billing", "—", "removed", "ours", "paper")]):
    y = 44 + i * 50
    dp_how.box(12, y, 736, 42, None, f, rx=4)
    dp_how.text(20, y + 27, n, "t-head", anchor="start", size=13)
    dp_how.text(300, y + 27, w, anchor="start", size=13)
    dp_how.text(400, y + 27, nb, anchor="start", size=13)
    dp_how.text(530, y + 27, ag, anchor="start", size=13)
    dp_how.text(660, y + 27, st, anchor="start", size=13)
dp_how.note(380, 280, "asked in person · weekly 15-min sync", "pen", size=16)
dp_how.note(380, 316, "the van slip seen three weeks early", "green", size=16)

DEPS = dict(
    slug="dependencies",
    kicker="a.k.a. “the wedding planner's board”",
    tldr="When your outcome depends on other teams, make each dependency <b>visible</b>: what you need, from whom, needed by when, the date <b>they agreed</b>, and its status. <b>Ask in person</b> and early, explain the why, and track them together in a short <b>weekly sync</b>. Best of all, <b>remove</b> dependencies you can (build it yourself, change the design, cut the scope). Dependencies managed in scattered chat threads become surprises.",
    chips=[("Family", "managing up and across"), ("Origin", "programme management; SAFe's programme board; team topologies"), ("Lives in", "a dependency board, reviewed weekly"), ("Pairs with", "when the date is fixed, working with the architect, release plans")],
    problem_side="Larder, 16 November 2026",
    problem="""  <p class="lead">Korenwolf goes live on <b>4 January</b>. Grace's work depends on three other teams: <b>billing</b> must create invoice lines per cost centre (Cho), <b>Dispatch</b> must plan van routes the evening before (Eli), <b>operations</b> must staff picking from 06:00 (Joost). Each has its own priorities, and <span class="hl-pink">each dependency lives in a different chat thread</span>.</p>
  <ul>
    <li>Other teams' priorities aren't yours.</li>
    <li>“Should be fine” in a chat isn't a date.</li>
    <li>Slips are found when they hit, not when they start.</li>
  </ul>""",
    problem_figs=[dp_problem],
    analogy_side="the wedding planner's board",
    analogy="""  <p>A wedding planner keeps a <b>board</b>: venue, caterer, band, flowers, each with what's needed, by when, and the date the supplier agreed. She <b>calls each one weekly</b>. And where she can, she <b>removes a supplier</b>: the cake comes from the caterer, not a separate baker.</p>""",
    analogy_figs=[dp_analogy],
    map=[("The suppliers", "Billing, Dispatch, operations"),
         ("What's needed, by when", "Invoice lines by 11 Dec, van routes by 14 Dec"),
         ("The date they agreed", "Cho: 4 Dec; Eli: 7 Dec (slipped to 14)"),
         ("The weekly call", "Fifteen minutes on Thursdays"),
         ("The cake from the caterer", "The cost-centre field built in Ordering")],
    how_side="visible, agreed, synced, removed",
    how="""  <p>Grace listed each dependency on one board: <b>what</b>, <b>who</b>, <b>needed by</b>, <b>agreed date</b>, <b>status</b>. She asked each lead <b>in person</b>, with the why (Korenwolf's contract), and set a <b>15-minute weekly sync</b>. One dependency she <b>removed</b>: the cost-centre field went into Ordering, built by her team, instead of waiting for billing's form. The van routes slipped a week; the board showed it <b>three weeks early</b>, and Eli's fix landed on 14 December.</p>""",
    how_figs=[dp_how],
    steps=[("List every dependency", "What you need from whom, for which outcome."),
           ("Ask in person, with the why", "Agree a date they own."),
           ("Put them on one board", "Needed by, agreed, status."),
           ("Sync weekly, briefly", "Fifteen minutes with the other leads."),
           ("Remove what you can", "Build it, redesign, or cut the scope."),
           ("Escalate early", "When an agreed date is at risk.")],
    vocab=[("Dependency", "Something you need from another team to deliver."),
           ("Critical path", "The chain of work that sets the end date."),
           ("Agreed date", "A date the providing team committed to."),
           ("Programme board", "A shared view of teams' dependencies and dates."),
           ("Decoupling", "Removing a dependency by changing the design or ownership."),
           ("Escalation", "Bringing a blocked dependency to a manager.")],
    code=dict(file="product/korenwolf/dependencies.md", note="the dependency board, 7 December 2026", plain=True, src="""
# Korenwolf go-live (4 Jan 2027) · dependencies · sync Thursdays 11:00, 15 min

| Need                                 | From        | Needed by | Agreed     | Status |
|--------------------------------------|-------------|-----------|------------|--------|
| Invoice lines per cost centre        | Cho (billing) | 11 Dec  | 4 Dec      | done   |
| Van routes planned the evening before | Eli (Dispatch) | 14 Dec | 7 → 14 Dec | amber → done 14 Dec |
| Picking from 06:00, Mon–Fri          | Joost (ops) | 4 Jan     | 4 Jan      | green  |
| Cost-centre form                     | (billing)   | —         | removed: built in Ordering by us |
| SSO for office managers              | Eli (platform) | 18 Dec | 18 Dec     | green  |
"""),
    tools="tools: a shared board (a wiki table, a spreadsheet or the planning tool), a weekly calendar slot, the release plan.",
    gains=["<b>Slips seen early</b>.",
           "<b>Dates owned</b> by the teams that deliver.",
           "<b>One place</b> instead of five threads.",
           "<b>Fewer dependencies</b> after removing some.",
           "<b>Better relationships</b> through asking in person."],
    losses=["<b>A weekly meeting</b> more.",
            "<b>Other teams' time</b>.",
            "<b>Removing dependencies</b> costs your team effort.",
            "<b>A board can become</b> a blame list."],
    baseline="Each line compares <b>dependencies managed in scattered chat threads</b> to <b>one board with agreed dates, a weekly sync, early escalation and dependencies removed where possible</b>.",
    ratings=[(3, 4, "Korenwolf's go-live held."),
             (2, 4, "The contract date protected."),
             (2, 4, "Dates agreed, not assumed."),
             (2, 4, "The slip seen in time to act."),
             (2, 4, "One less dependency to wait on."),
             (2, 5, "Cho, Eli, Joost and Grace see one board."),
             (2, 4, "Mo hears a believable plan."),
             (2, 4, "Work isn't blocked waiting."),
             (3, 3, "Fifteen minutes a week.")],
    pitfalls=[("Assuming dates", "“Should be fine.”", "a date they agree to."),
              ("Asking by ticket", "A ticket in their backlog.", "ask in person, with the why."),
              ("Tracking without removing", "Ten dependencies forever.", "remove what you can."),
              ("Blame boards", "Red names in a slide.", "a shared plan, not a scorecard.")],
    use=["Any work that needs other teams.",
         "Fixed dates and client go-lives.",
         "Platform changes your feature relies on.",
         "When work keeps getting blocked."],
    skip=["Work fully inside your team."],
    related=["<b>When the date is fixed</b> (this volume)", "<b>Working with the architect</b> (this volume)", "<b>Roadmap vs release plan</b> (Vol. 2)", "<b>Decision rights</b> (Ana, book 1 vol. 2)"],
    quiz=[("What does each line on the board need?", "What, from whom, needed by, the agreed date, status."),
          ("Why ask in person?", "To explain the why and get a date the other team owns."),
          ("Which dependency did Grace remove?", "The cost-centre form, built in Ordering by her own team."),
          ("What did the board catch?", "The van routes slipping a week, three weeks early.")],
    try_it="List every dependency your next release has on other teams. For each, get a date the other team agrees to, put them on one board, and find one you could remove.",
    remember="Keep the <span class=\"hl\">wedding planner's board</span>, and get the cake from the <span class=\"hl\">caterer</span>.",
    sources=["Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019).",
             "Dean Leffingwell, <i>SAFe</i> documentation, programme board.",
             "Donald Reinertsen, <i>The Principles of Product Development Flow</i> (2009).",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005), dependencies."],
)

NOTES = [UP, PITCH, DEPS]
