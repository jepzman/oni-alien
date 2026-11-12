# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 1 · Testing ideas cheaply.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 Testable Hypotheses
hy_problem = Doodle(760, 260, "Doodle of last year's experiments list at Larder: 'try SMS', 'try calling', 'try a banner'. None says what result would count as success. After each one, people looked at the numbers and found a reason it had worked. Nothing was ever stopped.",
                    "Experiments with no pass mark always “sort of work”. Nothing ever gets stopped.")
hy_problem.box(20, 20, 260, 160, None, "paper")
hy_problem.head(150, 48, "experiments 2025", size=17)
for i, t in enumerate(["try SMS", "try calling", "try a banner"]):
    hy_problem.text(40, 84 + i * 28, "• " + t, anchor="start", size=16)
hy_problem.arrow(286, 100, 340, 100)
for i, t in enumerate(["“it kind of worked”", "“promising!”", "“needs more time”"]):
    hy_problem.box(346, 20 + i * 54, 240, 44, t, "y", size=15)
hy_problem.box(610, 50, 136, 80, "stopped:", "pink", sub="none", stroke="red", size=17, subsize=15)
hy_problem.note(380, 230, "no pass mark → every result looks like success", "red")

hy_analogy = Doodle(760, 240, "Doodle of a bet written on a napkin before the match: 'Ajax win by two or more goals, loser buys dinner'. Written before kick-off, the terms can't be changed afterwards. Compare a friend who says after the match, 'I knew they'd win'.",
                    "A bet on a napkin before kick-off. After the final whistle, nobody can move the goalposts.")
hy_analogy.box(40, 40, 320, 130, None, "y")
hy_analogy.head(200, 74, "before kick-off:", size=17)
hy_analogy.text(200, 106, "“Ajax win by 2+ goals,", size=15)
hy_analogy.text(200, 130, "loser buys dinner”", size=15)
hy_analogy.note(200, 200, "✓ terms fixed in advance", "green")
hy_analogy.box(420, 60, 300, 80, "“I knew they'd win”", "pink", sub="said after the match", stroke="red", size=16, subsize=14)
hy_analogy.note(570, 170, "✗ can't be wrong, so it says nothing", "red")

hy_how = Doodle(760, 330, "The parts of Grace's hypothesis card. We believe asking express customers to approve swaps will reduce swap refund tickets for the tonight-dinner parent. We'll know we're right when at least 70 percent answer within two minutes and swap refund tickets on tested orders fall below two percent. Test: concierge at Noord, ten evenings. Decision rule: pass, go to prototype and build; fail on answer rate, try the no-swap flag branch instead.",
                 "Belief, who, expected change, a pass mark, a test and a decision rule, all written before the test.")
rows = [("we believe", "asking before a swap", "y"), ("for", "the tonight-dinner parent", "blue"), ("will result in", "fewer swap refund tickets", "y"),
        ("we'll know when", "≥ 70 % answer < 2 min · tickets < 2 %", "green"), ("test", "concierge, Noord, 10 evenings", "paper"), ("then", "pass → build · fail → “no swap” flag", "paper")]
for i, (k, v, f) in enumerate(rows):
    y = 12 + i * 50
    hy_how.text(166, y + 28, k, "t-head", anchor="end", size=15)
    hy_how.box(180, y, 566, 40, None, f)
    hy_how.text(196, y + 27, v, anchor="start", size=16)

HYPOTHESES = dict(
    slug="hypotheses",
    kicker="a.k.a. “the bet on the napkin”",
    tldr="Write every idea you test as a <b>bet with terms set in advance</b>: <b>we believe</b> [this change] <b>for</b> [these customers] <b>will result in</b> [this outcome]; <b>we'll know we're right when</b> [a measurable signal passes a threshold]. Add the <b>test</b> and the <b>decision rule</b> (pass, then what; fail, then what). Without a pass mark set beforehand, every result looks like success and nothing ever gets stopped.",
    chips=[("Family", "testing ideas cheaply"), ("Origin", "the scientific method; Lean Startup (Eric Ries, 2011); Strategyzer test cards"), ("Lives in", "a hypothesis card per experiment, next to the assumption map"), ("Pairs with", "assumption mapping, concierge MVP, fake door test")],
    problem_side="Larder, last year's experiments",
    problem="""  <p class="lead">Larder ran experiments in 2025: “try SMS”, “try calling”, “try a banner”. None said what result would count as success. Afterwards, people looked at the numbers and found a reason each one had <i>sort of</i> worked: “promising”, “needs more time”. <span class="hl-pink">Nothing was ever stopped</span>, and nothing was ever decided.</p>
  <ul>
    <li>Without a pass mark, any result can be read as success.</li>
    <li>Experiments drift on because stopping feels like failing.</li>
    <li>The team learns nothing it can act on.</li>
  </ul>""",
    problem_figs=[hy_problem],
    meanwhile=[("architect-1", "spike-prototype-poc", "Ana writes success criteria before her spikes; Grace writes the pass mark before her product tests.", "Grace writes product hypotheses the same way: the pass mark is set before the test starts.")],
    analogy_side="the bet on the napkin",
    analogy="""  <p>Two friends write a bet on a napkin <b>before kick-off</b>: “Ajax win by two or more goals; the loser buys dinner.” After the final whistle there's nothing to argue about. Compare the friend who says <b>after</b> the match, “I knew they'd win”: they can never be wrong, so what they say tells you nothing.</p>""",
    analogy_figs=[hy_analogy],
    map=[("The bet on the napkin", "The hypothesis card"),
         ("“Ajax win by 2+ goals”", "“≥ 70 % answer within 2 minutes”"),
         ("Written before kick-off", "Written before the test starts"),
         ("The loser buys dinner", "The decision rule: build, or try another branch"),
         ("“I knew they'd win”", "Reading success into results afterwards")],
    how_side="belief, signal, pass mark, decision",
    how="""  <p>A hypothesis tests <b>one</b> assumption, the riskiest from the map. The <b>signal</b> must be something the test can actually measure, and the <b>pass mark</b> must be agreed with whoever will act on the result (Priya, Joost). Then the decision is already made; the test only tells you which branch to take.</p>""",
    how_figs=[hy_how],
    steps=[("Pick the riskiest assumption", "From the assumption map's top-left: “customers answer within 2 minutes”."),
           ("Write the belief", "We believe [change] for [who] will result in [outcome]."),
           ("Choose a measurable signal", "Something the test can measure directly: answer rate, time to answer."),
           ("Set the pass mark", "A threshold agreed in advance with the decision-maker: ≥ 70 %."),
           ("Write the decision rule", "Pass → next step. Fail → which branch of the tree next."),
           ("Run, record, decide", "Report the result against the card; don't move the pass mark afterwards.")],
    vocab=[("Hypothesis", "A testable statement of what you believe will happen."),
           ("Signal", "What you'll measure in the test."),
           ("Pass mark", "The threshold that counts as success, set in advance."),
           ("Decision rule", "What you'll do if the test passes or fails."),
           ("Falsifiable", "Could be shown wrong by evidence."),
           ("Moving the goalposts", "Changing success criteria after seeing results.")],
    code=dict(file="product/substitutions/hypothesis-H1.md", note="hypothesis card, 1 Dec 2025", plain=True, src="""
# H1 · Asking before a swap                         owner: Grace · agreed with Priya, Joost

We believe     asking express customers to approve or reject a substitute
for            the tonight-dinner parent (express orders)
will result in fewer substitution refund tickets.

We'll know we're right when, on tested orders:
  - ≥ 70 % of customers answer within 2 minutes          (assumption A1)
  - swap refund tickets < 2 % of orders                  (baseline 6.8 % at Noord)
  - picking time per affected order rises ≤ 60 seconds    (assumption A2, Joost)

Test           Concierge at Noord: support phones customers, 8–19 Dec, 17:00–20:00
Decision rule  all pass  → prototype test in January, then build (Q1 roadmap)
               A1 fails  → test the “never swap this” flag branch instead
               A2 fails  → picker continues; answer applied at packing (redesign)
Not allowed    changing the pass marks after 8 Dec.
"""),
    tools="tools: a card in the repo or on the wall. Strategyzer's Test Card and Learning Card are good templates; Jira Product Discovery and similar tools can hold hypotheses next to ideas.",
    gains=["<b>Clear decisions</b>: the result picks the next step.",
           "<b>Honest learning</b>: no reading success into noise.",
           "<b>Experiments stop</b> when they fail, freeing the team.",
           "<b>Stakeholders agree in advance</b>, so results aren't re-argued.",
           "<b>One assumption per test</b>, so you know what you learned."],
    losses=["<b>Picking thresholds is hard</b> before you have data.",
            "<b>Feels rigid</b> to people used to “let's see”.",
            "<b>Small tests</b> give noisy results near the pass mark.",
            "<b>Can be over-formalised</b> for tiny tweaks."],
    baseline="Each line compares <b>experiments without success criteria (“try SMS”)</b> to <b>hypothesis cards with a signal, a pass mark and a decision rule agreed before the test</b>.",
    ratings=[(3, 4, "Tests focus on what customers will really do."),
             (3, 4, "Pass marks link to the outcome the business tracks."),
             (1, 5, "Results are judged against criteria set in advance."),
             (2, 5, "Each test ends with a clear answer and a next step."),
             (2, 4, "Failed ideas stop; the team moves to the next branch."),
             (2, 4, "Everyone knows what the test is for and what counts."),
             (2, 4, "Priya and Joost agreed the terms before the result."),
             (3, 3, "Neutral."),
             (3, 4, "A card takes 20 minutes.")],
    pitfalls=[("No pass mark", "“Let's see what happens.”", "write the threshold before starting, with the decision-maker."),
              ("Moving the goalposts", "65 % answered, so the bar is lowered to 60 %.", "keep the original mark; decide by the rule; re-test if needed."),
              ("Testing several things at once", "New flow, new copy and a discount in one test.", "one assumption per hypothesis."),
              ("Signals the test can't measure", "“Customers love it.”", "choose something countable in the test.")],
    use=["Any experiment, interview round or pilot meant to inform a decision.",
         "When stakeholders tend to re-argue results.",
         "When experiments keep running without ending.",
         "Before spending money on a test."],
    skip=["Pure exploration where you don't know what to look for yet: interview first.",
          "Tiny copy tweaks: ship and watch.",
          "Decisions already made: don't stage a test for show."],
    related=["<b>Assumption mapping</b> (this volume)", "<b>Concierge &amp; Wizard-of-Oz MVP</b> (this volume)", "<b>Fake door test</b> (this volume)", "<b>Spike vs prototype vs PoC</b> (Ana, vol. 1)"],
    quiz=[("What are the parts of a hypothesis card?", "Belief (change, who, expected result), signal, pass mark, test, decision rule."),
          ("Why set the pass mark in advance?", "Otherwise any result can be read as success and nothing is decided."),
          ("What was H1's pass mark for answering?", "At least 70 % answer within 2 minutes."),
          ("What happens if H1 fails on the answer rate?", "The team tests the “never swap this” flag branch instead.")],
    try_it="Take one experiment your team is running or planning. Write its hypothesis card with a pass mark and a decision rule. Show it to the person who'll act on the result and ask: “if it lands at exactly the pass mark, what will you do?”",
    remember="Write the <span class=\"hl\">bet</span> before kick-off. Don't move the <span class=\"hl\">goalposts</span>.",
    sources=["Eric Ries, <i>The Lean Startup</i> (2011).",
             "David J. Bland &amp; Alexander Osterwalder, <i>Testing Business Ideas</i> (2019), test cards.",
             "Jeff Gothelf &amp; Josh Seiden, <i>Lean UX</i>, 3rd ed. (2021), hypothesis statements.",
             "Ron Kohavi et al., <i>Trustworthy Online Controlled Experiments</i> (2020)."],
)

# ------------------------------------------------------------------ 13 Fake Door Test
fd_problem = Doodle(760, 260, "Doodle of Femke's plan for Larder for Business: hire a business salesperson for seventy thousand euros a year and build an office ordering portal, because she believes offices want weekly pantry deliveries. The only evidence is two interviews and a feeling.",
                    "€70,000 a year and a new portal, on two interviews and a feeling.")
fd_problem.box(20, 30, 260, 90, "Larder for Business", "y", sub="Femke's idea", size=18, subsize=15)
fd_problem.arrow(286, 75, 340, 75)
fd_problem.box(346, 20, 200, 60, "hire sales", "pink", sub="€70k / year", stroke="red", size=16, subsize=14)
fd_problem.box(346, 96, 200, 60, "build a portal", "pink", sub="3 months", stroke="red", size=16, subsize=14)
fd_problem.box(580, 50, 160, 80, "evidence?", "paper", dash=True, sub="2 interviews", size=17, subsize=14)
fd_problem.note(380, 216, "do offices want this? nobody has asked many", "red")

fd_analogy = Doodle(760, 240, "Doodle of a restaurant testing a new dish. The chef adds 'mushroom risotto' to the menu before buying any equipment or ingredients. When someone orders it, the waiter honestly says it's not available yet and offers a free dessert, and the chef counts the orders. Many orders: develop it. Few: drop it.",
                    "Put the dish on the menu first. Count who orders it. Be honest, and say sorry with a free dessert.")
fd_analogy.icon("menu", 40, 40, 2.0)
fd_analogy.note(90, 200, "+ mushroom risotto", "pen")
fd_analogy.arrow(160, 110, 240, 110)
fd_analogy.box(246, 50, 230, 120, None, "y")
fd_analogy.head(361, 80, "“not ready yet,", size=16)
fd_analogy.text(361, 110, "here's a free dessert”", size=15)
fd_analogy.text(361, 140, "+ count the orders", size=15)
fd_analogy.arrow(482, 110, 540, 110)
fd_analogy.box(546, 50, 190, 120, "23 orders", "green", sub="in a week → develop", size=19, subsize=14)

fd_how = Doodle(760, 350, "The fake door funnel, 3 to 17 December. Twenty-one thousand app sessions see a 'Larder for your office?' link in the account menu and the order email. One hundred and forty click it. They land on an honest page: not ready yet, leave your email and team size. Thirty-eight leave an email. Nine are offices with more than forty staff. Femke takes these numbers to the facilities trade fair in January, where she meets Korenwolf.",
                 "One honest link, two weeks, four numbers. Enough to decide the next step, not to build the portal.")
funnel = [("saw the link", "21,000 sessions", 720, "paper"), ("clicked", "140", 580, "blue"), ("left an email", "38", 460, "y"), ("offices with 40+ staff", "9", 360, "green")]
for i, (lbl, n, w, f) in enumerate(funnel):
    x = (760 - w) / 2
    fd_how.box(x, 14 + i * 64, w, 52, None, f)
    fd_how.text(380, 46 + i * 64, f"{n} · {lbl}", "t-head", size=16)
fd_how.box(150, 280, 460, 56, "landing page: “not ready yet,", "paper", sub="tell us about your office” · honest, no fake checkout", size=15, subsize=13)

FAKE_DOOR = dict(
    slug="fake-door",
    kicker="a.k.a. “put the dish on the menu first”",
    tldr="Before building something, add the <b>entry point</b> to it (a link, a button, a menu item) and <b>count who uses it</b>. Behind the door, be honest: “not ready yet, tell us more”, and ask for an email or a detail you can follow up. It measures <b>real interest</b> with real behaviour in days, for almost nothing. Keep it short, small and honest, and never fake a payment.",
    chips=[("Family", "testing ideas cheaply"), ("Origin", "Lean Startup “smoke tests” (2000s); painted-door tests at large web companies"), ("Lives in", "a small link in the product for one or two weeks"), ("Pairs with", "testable hypotheses, concierge MVP, jobs to be done")],
    problem_side="Larder, Femke's business idea",
    problem="""  <p class="lead">Femke wants to start <b>Larder for Business</b>: weekly pantry deliveries to offices. Her plan is to hire a business salesperson (<b>€70,000 a year</b>) and build an office ordering portal (<b>three months</b>). The evidence: two of Grace's interviews mentioned an office pantry, and <span class="hl-pink">a feeling</span>. Grace suggests finding out who knocks before building the door.</p>
  <ul>
    <li>Big bets get made on enthusiasm and a few anecdotes.</li>
    <li>Asking people “would you use it?” gets polite yeses.</li>
    <li>Building first is the most expensive way to find out nobody wants it.</li>
  </ul>""",
    problem_figs=[fd_problem],
    meanwhile=[("architect-1", "risk-storming", "while Ana's team storms the delivery risks, Grace's fake door tests a business risk: do offices want this at all?", "In the same weeks, Grace's fake door tests a business risk this wall didn't cover: do offices want Larder for Business?")],
    analogy_side="the dish on the menu",
    analogy="""  <p>A restaurant can add <b>“mushroom risotto”</b> to the menu before buying a single mushroom. When a guest orders it, the waiter is honest (“it's not ready yet, here's a free dessert”) and the chef <b>counts the orders</b>. Twenty-three in a week: develop it. Two: drop it, having spent almost nothing.</p>""",
    analogy_figs=[fd_analogy],
    map=[("The dish on the menu", "A “Larder for your office?” link in the app"),
         ("Guests ordering it", "Customers clicking the link"),
         ("“Not ready yet, free dessert”", "An honest page: not ready, tell us about your office"),
         ("Counting orders for a week", "Counting clicks and emails for two weeks"),
         ("Develop or drop the dish", "Next step for Larder for Business, or stop")],
    how_side="a small link, an honest page, a pass mark",
    how="""  <p>Show the door to a <b>small share</b> of users for a <b>short time</b>, with a hypothesis and pass mark written first. The landing page must be honest and give something back: a promise to get in touch, a way to leave details. The follow-up conversations are often worth more than the click count.</p>""",
    how_figs=[fd_how],
    steps=[("Write the hypothesis", "“At least 0.5 % of sessions click, and at least 5 offices with 40+ staff leave details.”"),
           ("Place the door where it fits", "Account menu and the order confirmation email: where office managers would look."),
           ("Build an honest landing page", "Not ready yet; tell us about your office; we'll be in touch. No fake checkout."),
           ("Limit it", "Two weeks, a share of users; check with legal and privacy (Lena) for the form."),
           ("Count and follow up", "Clicks, emails, team sizes. Call the most promising ones within a week."),
           ("Decide and remove the door", "Pass → next step (a pilot). Fail → park the idea. Take the link down either way.")],
    vocab=[("Fake door test", "An entry point to something that doesn't exist yet, to measure interest."),
           ("Smoke test", "A landing page or ad that measures demand before building."),
           ("Painted door", "Another name for a fake door."),
           ("Click-through rate", "Share of people who saw the door and clicked."),
           ("Qualified lead", "Someone who matches the target (offices with 40+ staff)."),
           ("Honest disclosure", "Telling people right away that it's not ready.")],
    code=dict(file="product/experiments/2025-12-fake-door-business.md", note="test card and result", plain=True, src="""
# Fake door: “Larder for your office?”                  owner: Grace · for: Femke

Hypothesis   Offices want weekly pantry deliveries from Larder.
Pass mark    ≥ 0.5 % of sessions click · ≥ 5 offices with 40+ staff leave details
Door         Account menu link + a line in the order confirmation email
Behind it    “We're not doing this yet. Tell us about your office and we'll call you.”
             (email, company, team size, how you restock today) · Lena approved the form
When / who   3–17 Dec 2025, all app users in Amsterdam

Result       21,000 sessions saw it · 140 clicked (0.67 %) ✓
             38 left details · 9 offices with 40+ staff ✓
             Today they restock via: a caterer (4), staff go shopping (3), a wholesaler (2)
Follow-up    Grace + Femke called 6 of the 9 (“the person who buys milk”)
Decision     PASS → Femke takes the numbers to the facilities trade fair (Jan 2026);
             a pilot before any portal. Door removed 18 Dec.
"""),
    tools="tools: a feature flag to show the door to a share of users (LaunchDarkly, Unleash, or your own), a simple form, and your analytics tool. Check the landing page wording with legal and keep it honest.",
    gains=["<b>Real behaviour</b>, not polite opinions.",
           "<b>Days, not months</b>, for almost nothing.",
           "<b>Leads to talk to</b>: the follow-up calls.",
           "<b>Evidence for big bets</b>: Femke's trade-fair numbers.",
           "<b>Easy to stop</b>: remove one link."],
    losses=["<b>Can annoy users</b> who expected a real feature.",
            "<b>Trust risk</b> if overused or dishonest.",
            "<b>Interest isn't purchase</b>: clicks overstate demand.",
            "<b>Only tests the entry</b>, not whether the product works."],
    baseline="Each line compares <b>deciding a new business line on two interviews and a feeling</b> to <b>a two-week honest fake door with a pass mark and follow-up calls</b>.",
    ratings=[(3, 3, "Neutral; it measures interest, not value delivered."),
             (2, 4, "A €70k decision rests on numbers."),
             (1, 4, "Clicks and details are behaviour, not opinions."),
             (2, 5, "Two weeks to an answer."),
             (3, 4, "A clear pass or fail stops idea drift."),
             (2, 4, "Everyone sees the same funnel."),
             (2, 5, "Femke gets evidence, not a lecture."),
             (3, 3, "Neutral."),
             (3, 4, "A link, a page and a few calls.")],
    pitfalls=[("Dishonest door", "A fake checkout takes card details.", "say “not ready yet” immediately; never fake payment."),
              ("Running it forever", "The link stays for months; users get annoyed.", "set an end date and remove it."),
              ("Clicks as demand", "140 clicks = 140 customers.", "follow up; qualify; treat clicks as interest only."),
              ("No pass mark", "Any number looks interesting.", "write the hypothesis and pass mark first.")],
    use=["A new feature or business line with unknown demand.",
         "Before a big hire or build.",
         "Choosing between several possible features.",
         "When surveys keep giving polite yeses."],
    skip=["Anything involving payment, health or safety promises.",
          "Very small user bases where a few clicks mean nothing.",
          "When you'd build it anyway: don't stage a test."],
    related=["<b>Testable hypotheses</b> (this volume)", "<b>Concierge &amp; Wizard-of-Oz MVP</b> (this volume)", "<b>Jobs to be done</b> (this volume)", "<b>Risk-storming</b> (Ana, vol. 1)"],
    quiz=[("What does a fake door test measure?", "Real interest, through behaviour (clicks, details left), before anything is built."),
          ("What must the page behind the door do?", "Tell people honestly it's not ready, and give them a way to leave details."),
          ("Why follow up with the people who clicked?", "Clicks overstate demand; conversations show who's really a customer."),
          ("What did Larder's fake door lead to?", "Numbers Femke took to the trade fair where she met Korenwolf, and a pilot before any portal.")],
    try_it="Pick one feature idea your team is debating. Write a fake-door hypothesis with a pass mark, an honest landing-page text and an end date. Ask your legal or privacy contact to read the text before anything goes live.",
    remember="Put the dish on the <span class=\"hl\">menu</span>, count the <span class=\"hl\">orders</span>, and always be honest at the table.",
    sources=["Eric Ries, <i>The Lean Startup</i> (2011), smoke tests.",
             "David J. Bland &amp; Alexander Osterwalder, <i>Testing Business Ideas</i> (2019), fake door and smoke tests.",
             "Alberto Savoia, <i>The Right It</i> (2019), pretotyping.",
             "Nielsen Norman Group, “Fake-Door Testing” (nngroup.com)."],
)

# ------------------------------------------------------------------ 14 Concierge & Wizard-of-Oz MVP
cm_problem = Doodle(760, 260, "Doodle of the team ready to build approve-in-app: new app screens, push notifications, a picker app change, a timer, a backend for answers. About eight weeks of work. But the riskiest assumption, that customers answer within two minutes, could be tested next week with a phone.",
                    "Eight weeks of build to learn something a phone could tell you next week.")
for i, t in enumerate(["app screens", "push + SMS", "picker app", "timer", "answer API"]):
    cm_problem.box(20 + i * 146, 30, 132, 54, t, "blue", size=15)
cm_problem.note(380, 116, "≈ 8 weeks of build", "red", size=19)
cm_problem.icon("phone", 340, 140, 1.0)
cm_problem.note(500, 186, "← or: a phone, next week", "green", size=19)

cm_analogy = Doodle(760, 240, "Doodle of someone starting a laundry pick-up service. Before building an app or renting a laundry, the founder collects bags from neighbours by bike, washes them at home and brings them back folded. If neighbours keep using it and paying, then build the business.",
                    "Start a laundry service by hand: collect the bags by bike, wash at home. Build the business once neighbours keep coming back.")
cm_analogy.icon("bucket", 40, 70, 1.6)
cm_analogy.arrow(150, 120, 220, 120)
cm_analogy.box(226, 60, 250, 120, None, "y")
cm_analogy.head(351, 92, "by hand, for 2 weeks", size=16)
cm_analogy.text(351, 124, "bike, home washer,", size=15)
cm_analogy.text(351, 148, "a notebook of orders", size=15)
cm_analogy.arrow(482, 120, 540, 120)
cm_analogy.box(546, 60, 190, 120, "they come back?", "green", sub="→ build the business", size=16, subsize=14)

cm_how = Doodle(760, 380, "How the concierge test ran at the Noord store, 8 to 19 December, 17:00 to 20:00, express orders only. A picker taps item missing in the existing picker app. Sam's support agent sees an alert, picks a substitute with the picker, and phones the customer. The customer says yes or no. The agent tells the picker, who packs. Results over 412 swaps: 81 percent answered within two minutes, 74 percent accepted the substitute, 15 percent chose no substitute, 11 percent didn't answer. Swap refund tickets on those orders: 1.1 percent, against 6.8 percent at Zuid in the same weeks. Picking time rose by 40 seconds per affected order.",
                 "No new code: a picker, a support agent with a phone, and a spreadsheet. Two weeks, 412 swaps.")
flow = [("picker", "taps “missing”", "blue"), ("agent", "sees an alert", "y"), ("phone call", "“swap OK?”", "y"), ("customer", "yes / no", "green"), ("picker", "packs", "blue")]
for i, (who, act, f) in enumerate(flow):
    x = 14 + i * 150
    cm_how.box(x, 20, 136, 66, who, f, sub=act, size=15, subsize=13)
    if i < 4:
        cm_how.arrow(x + 138, 53, x + 148, 53)
res = [("answered < 2 min", 81, "green"), ("accepted swap", 74, "green"), ("chose “no swap”", 15, "y"), ("no answer", 11, "pink")]
for i, (lbl, pct, f) in enumerate(res):
    y = 120 + i * 42
    cm_how.text(220, y + 22, lbl, anchor="end", size=15)
    cm_how.box(234, y, pct * 4.6, 30, None, f, rx=4)
    cm_how.text(244 + pct * 4.6, y + 22, f"{pct} %", "t-head", anchor="start", size=14)
cm_how.box(14, 300, 360, 60, "swap refund tickets: 1.1 %", "green", sub="vs 6.8 % at Zuid, same weeks", size=16, subsize=13)
cm_how.box(392, 300, 354, 60, "picking time +40 s", "y", sub="per affected order · Joost: OK", size=16, subsize=13)

CONCIERGE = dict(
    slug="concierge-mvp",
    kicker="a.k.a. “do the laundry by hand first”",
    tldr="Before building software, <b>deliver the value by hand</b> to a small group of real customers: people do what the product would do. A <b>concierge</b> test is open about it (a person calls you); a <b>Wizard of Oz</b> test shows a product front end while people work the levers behind the curtain. You learn whether customers want the result, what they really need, and what the process should be, in days, with no code. Build only once it's proven.",
    chips=[("Family", "testing ideas cheaply"), ("Origin", "Eric Ries, <i>The Lean Startup</i> (2011); early Food on the Table and Zappos stories"), ("Lives in", "a two-week pilot with a few staff and a spreadsheet"), ("Pairs with", "testable hypotheses, assumption mapping, prototype testing")],
    problem_side="Larder, eight weeks or a phone",
    problem="""  <p class="lead">The team is ready to build <b>approve-in-app</b>: new app screens, push notifications and SMS, a picker app change, a two-minute timer, a backend for answers. About <b>eight weeks</b> of work. But the riskiest assumption on the map, that customers <b>answer within two minutes</b>, could be tested <span class="hl-pink">next week, with a phone</span>.</p>
  <ul>
    <li>Building to learn is the slowest, most expensive way to learn.</li>
    <li>Once code exists, the team is reluctant to throw it away, even if the idea fails.</li>
    <li>The real process (who calls, what's said, what pickers do meanwhile) is unknown until someone does it.</li>
  </ul>""",
    problem_figs=[cm_problem],
    meanwhile=[("architect-1", "spike-prototype-poc", "Ana's spike answers a technical question; Grace's concierge test answers the customer question, by hand.", "Grace's concierge test is the product's version: two weeks of phone calls answer the customer question before any code.")],
    analogy_side="the laundry service by hand",
    analogy="""  <p>To start a laundry pick-up service you could build an app and rent a laundry. Or you could <b>collect bags from neighbours by bike</b>, wash them at home and bring them back folded, for two weeks. If neighbours keep coming back and paying, you know the service is wanted, and you know exactly what the app needs to do.</p>""",
    analogy_figs=[cm_analogy],
    map=[("Collecting bags by bike", "A support agent phoning customers about swaps"),
         ("Washing at home", "The picker and agent choosing the substitute together"),
         ("A notebook of orders", "A spreadsheet of answers and times"),
         ("Neighbours coming back", "Customers answering, accepting, fewer refund tickets"),
         ("Then build the app", "Then build approve-in-app, knowing the process")],
    how_side="people do what the software would",
    how="""  <p>Keep it <b>small</b> (one store, express only, three hours an evening), <b>time-boxed</b> (two weeks) and tied to a <b>hypothesis card</b>. Use what already exists: the picker app's “item missing” button, a phone, a spreadsheet. Watch the process as closely as the numbers.</p>""",
    how_figs=[cm_how],
    steps=[("Start from the hypothesis", "H1: ≥ 70 % answer within 2 minutes; refund tickets < 2 %; picking time ≤ +60 s."),
           ("Design the manual process", "Who notices, who calls, what they say, where it's written down, what the picker does meanwhile."),
           ("Keep it small and safe", "One store, express orders, 17:00–20:00, two weeks. Brief the staff; tell Lena about the calls."),
           ("Run it, watch it", "Grace spends evenings at Noord. Note surprises, not just numbers."),
           ("Compare to a baseline", "Same weeks at Zuid without calls; same ticket rule."),
           ("Decide by the card", "Pass → prototype the in-app version. Fail → the next branch of the tree.")],
    vocab=[("MVP", "Minimum viable product: the smallest thing that tests whether something is worth building."),
           ("Concierge MVP", "Delivering the value by hand, openly, to a few customers."),
           ("Wizard of Oz", "A product-looking front end, with people doing the work behind it."),
           ("Manual-first", "Doing a process by hand before automating it."),
           ("Comparison group", "Similar orders without the change (Zuid), for a fair comparison."),
           ("Operational load", "The extra work a test puts on staff.")],
    code=dict(file="product/experiments/2025-12-concierge-noord.md", note="learning card", plain=True, src="""
# Concierge test · asking before a swap (H1)          Noord · 8–19 Dec 2025, 17:00–20:00

Setup     Picker taps “item missing” (existing button) → alert to a support agent
          → agent + picker pick a substitute → agent phones the customer → answer
          to picker → pack. Logged in a spreadsheet. 2 agents (Sam's team).

Result    412 swaps on 1,960 express orders
          answered < 2 min       81 %   ✓ (≥ 70 %)
          accepted the swap      74 %
          chose “no swap”        15 %
          no answer               11 %  → picker's choice (as today)
          swap refund tickets    1.1 %  ✓ (< 2 %)   Zuid same weeks: 6.8 %
          picking time           +40 s per affected order ✓ (≤ 60 s)

Surprises - customers asked the price difference in 1 of 3 calls → show it
          - 9 calls mentioned an allergy → “never swap this” matters (O3)
          - pickers waited idle for the answer → let them continue (redesign)
Decision  PASS. Next: clickable prototype test (Jan), then build. Calls stop 19 Dec.
          Cost: ≈ 60 agent-hours.
"""),
    tools="tools: a phone, a spreadsheet and the systems you already have. For a Wizard of Oz version, a feature flag shows a real-looking screen while a person sends the answers by hand from an admin tool.",
    gains=["<b>Answers in two weeks</b> without code.",
           "<b>The real process is discovered</b>: price questions, allergies, idle pickers.",
           "<b>Strong evidence</b>: 1.1 % vs 6.8 % in the same weeks.",
           "<b>Better design</b>: the build starts from what actually happened.",
           "<b>Easy to stop</b> if it fails."],
    losses=["<b>Staff time</b>: about 60 agent-hours.",
            "<b>Doesn't scale</b>: the manual version can't run everywhere.",
            "<b>Differs from the product</b>: a phone call isn't a push notification.",
            "<b>Disruption</b> to the store during the test."],
    baseline="Each line compares <b>building approve-in-app first (about eight weeks)</b> to <b>a two-week manual concierge test at one store, judged against a hypothesis card and a comparison store</b>.",
    ratings=[(2, 5, "Real customers got the real value, and their reactions shaped the design."),
             (2, 4, "Refund tickets fell to 1.1 % on tested orders."),
             (2, 5, "Behaviour on 412 real swaps, against a comparison store."),
             (2, 5, "Two weeks instead of eight."),
             (3, 4, "The test answered the one question that mattered."),
             (2, 5, "Pickers, support and engineers all saw the process."),
             (3, 5, "Joost and Femke saw evidence from their own store."),
             (3, 3, "Neutral; it delays the build but improves it."),
             (3, 2, "Sixty agent-hours and store disruption.")],
    pitfalls=[("Too big", "All stores, all evenings, from day one.", "one store, one segment, a short window."),
              ("No comparison", "1.1 % sounds great, but compared to what?", "run a comparison group in the same weeks."),
              ("Never stopping", "The manual process becomes permanent.", "set an end date; decide by the card."),
              ("Only counting", "Numbers recorded, surprises missed.", "be there; note what people say and do.")],
    use=["When the riskiest assumption is about customer behaviour.",
         "Before building a new service or workflow.",
         "When the process itself is unclear.",
         "When a manual version is possible for a small group."],
    skip=["When the value only exists at scale or speed (real-time pricing).",
          "Where manual handling is unsafe or illegal.",
          "When the assumption is purely technical: spike it."],
    related=["<b>Testable hypotheses</b> (this volume)", "<b>Assumption mapping</b> (this volume)", "<b>Prototype testing with users</b> (this volume)", "<b>Spike vs prototype vs PoC</b> (Ana, vol. 1)"],
    quiz=[("What's the difference between a concierge and a Wizard-of-Oz MVP?", "Concierge is openly manual; Wizard of Oz shows a product front end with people working behind it."),
          ("Why compare with Zuid in the same weeks?", "So the result isn't explained by season, weather or anything else that changed."),
          ("Name two surprises from the Noord test.", "Customers asked about the price difference; allergies came up often; pickers waited idle."),
          ("What decided the next step?", "The hypothesis card: all three pass marks were met, so the next step was a prototype test.")],
    try_it="Pick the idea your team plans to build next. Describe how a person could deliver its value by hand to ten customers next week, using only tools you already have. What's the one number you'd check at the end?",
    remember="Do the <span class=\"hl\">laundry by hand</span> first. Build the machine once they <span class=\"hl\">come back</span>.",
    sources=["Eric Ries, <i>The Lean Startup</i> (2011), concierge MVP.",
             "David J. Bland &amp; Alexander Osterwalder, <i>Testing Business Ideas</i> (2019), concierge and Wizard of Oz.",
             "Ash Maurya, <i>Running Lean</i>, 3rd ed. (2022).",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), prototype types."],
)

# ------------------------------------------------------------------ 15 Prototype Testing with Users
pt_problem = Doodle(760, 260, "Doodle of the design review for approve-in-app. Grace, Dee and Priya all look at the screens and agree they're clear. But all three already know how the feature works. Nobody has watched a hungry parent at 17:40 with a toddler, or a picker wearing gloves, try to use it.",
                    "Three people who know how it works agree it's clear. Nobody has watched a real user try it.")
for i, who in enumerate(["Grace", "Dee", "Priya"]):
    pt_problem.box(20 + i * 160, 40, 140, 70, who, "blue", sub="“clear!”", size=17, subsize=15)
pt_problem.arrow(500, 75, 560, 75, dash=True)
pt_problem.box(566, 20, 180, 110, None, "pink", stroke="red")
pt_problem.head(656, 50, "not asked:", size=16, color="red")
pt_problem.text(656, 80, "a parent at 17:40", size=14)
pt_problem.text(656, 104, "a picker in gloves", size=14)
pt_problem.note(380, 200, "the people who built it can't see what's confusing", "red")

pt_analogy = Doodle(760, 240, "Doodle of a family planning a new kitchen by taping the floor plan onto the garage floor at full size and walking through cooking a meal. They discover the dishwasher door blocks the fridge when open. Fixing tape costs nothing; moving a fitted kitchen costs thousands.",
                    "Tape the new kitchen on the garage floor and cook an imaginary dinner. The dishwasher blocks the fridge.")
pt_analogy.raw('<rect class="d d-dash f-paper" x="40" y="30" width="420" height="180"/>')
for (x, y, w, h, t) in [(60, 50, 120, 60, "fridge"), (200, 50, 120, 60, "sink"), (340, 50, 100, 60, "oven"), (200, 130, 120, 60, "dishwasher")]:
    pt_analogy.box(x, y, w, h, t, "y" if t != "dishwasher" else "pink", stroke="red" if t == "dishwasher" else "", size=15)
pt_analogy.arrow(200, 160, 130, 112, color="red")
pt_analogy.note(600, 90, "door blocks the fridge", "red", size=18)
pt_analogy.note(600, 140, "tape: €5 · kitchen: €8,000", "pen", size=17)

pt_how = Doodle(760, 360, "How Grace ran the prototype test in January 2026. A clickable prototype of approve-in-app, with real products and prices. Six express customers, each given a scenario on their own phone: it's 17:40, you ordered dinner, now you get this. Three pickers at Noord, wearing gloves, using the picker side. Observers note where people hesitate or fail. Findings: five of six didn't notice the two-minute timer; four asked about the price difference; all three pickers couldn't tap the small buttons with gloves; pickers wanted to continue picking while waiting. Version two fixes all four.",
                 "Six customers, three pickers, real scenarios. Four problems found, all fixed before a line of code.")
pt_how.box(14, 20, 230, 90, "clickable prototype", "blue", sub="real items, real prices", size=16, subsize=14)
pt_how.box(264, 20, 230, 90, "6 customers", "y", sub="“it's 17:40, you get this”", size=16, subsize=13)
pt_how.box(514, 20, 232, 90, "3 pickers", "y", sub="at Noord, wearing gloves", size=16, subsize=13)
finds = [("5 / 6 missed the 2-min timer", "big countdown on top"), ("4 / 6 asked “how much more?”", "show the price difference"),
         ("3 / 3 pickers: buttons too small", "large buttons, gloves-friendly"), ("pickers stood waiting", "continue; answer at packing")]
for i, (f, fix) in enumerate(finds):
    y = 136 + i * 50
    pt_how.box(14, y, 400, 40, None, "pink")
    pt_how.text(28, y + 27, f, anchor="start", size=15)
    pt_how.arrow(420, y + 20, 456, y + 20, color="green")
    pt_how.box(462, y, 284, 40, None, "green")
    pt_how.text(476, y + 27, fix, anchor="start", size=15)
pt_how.note(380, 350, "v1 → v2 in a week, before any code", "pen", size=17)

PROTOTYPE_TESTING = dict(
    slug="prototype-testing",
    kicker="a.k.a. “tape the kitchen on the garage floor”",
    tldr="Put a <b>clickable prototype</b> (screens that look real, no code behind them) in front of <b>about five real users</b> per kind of user, give each a <b>realistic scenario</b>, and <b>watch</b> what they do without helping. Where they hesitate, misread or fail is where the design is wrong. Fix it and test again. It costs days, finds most usability problems before engineering starts, and the people who designed it can't do it for themselves.",
    chips=[("Family", "testing ideas cheaply"), ("Origin", "usability testing (Jakob Nielsen, “five users”, 2000); Google Ventures design sprints"), ("Lives in", "a test plan, session notes and a findings list per round"), ("Pairs with", "concierge MVP, proto-personas, journey map")],
    problem_side="Larder, the design review",
    problem="""  <p class="lead">With the concierge test passed, Dee designs the screens for <b>approve-in-app</b>. In the review, Grace, Dee and Priya agree they're clear. But all three know exactly how the feature works. Nobody has watched <b>a parent at 17:40</b> with a toddler on one arm, or <b>a picker wearing gloves</b>, try to use it. <span class="hl-pink">The people who built it can't see what's confusing.</span></p>
  <ul>
    <li>Designers and product owners know too much to judge clarity.</li>
    <li>Usability problems found after release cost a sprint each to fix.</li>
    <li>Staff-facing screens (pickers) are rarely tested at all.</li>
  </ul>""",
    problem_figs=[pt_problem],
    meanwhile=[("architect-1", "walking-skeleton", "while Ana's team builds the Rotterdam walking skeleton, Grace tests what will hang on it next.", "In the same weeks, Grace tests the substitution flow as a clickable prototype, so the next slice on this skeleton is ready.")],
    analogy_side="the kitchen taped on the garage floor",
    analogy="""  <p>Before ordering a new kitchen, a family <b>tapes the floor plan onto the garage floor</b> at full size and walks through cooking a dinner. They find that the <b>dishwasher door blocks the fridge</b> when it's open. Moving tape costs nothing. Moving a fitted kitchen costs thousands.</p>""",
    analogy_figs=[pt_analogy],
    map=[("Tape on the garage floor", "A clickable prototype, no code"),
         ("Cooking an imaginary dinner", "A realistic scenario: “it's 17:40, you get this”"),
         ("The family walking it", "Six real customers and three pickers"),
         ("Dishwasher blocks the fridge", "Pickers can't tap small buttons with gloves"),
         ("Moving the tape", "Version two of the prototype, a week later")],
    how_side="scenario, watch, fix, repeat",
    how="""  <p>Test each <b>kind of user</b> separately (customers and pickers here), in their real setting where possible: their own phone, the store floor, gloves on. Observers say nothing and note where people hesitate. Five people per group finds most problems; then fix and test again rather than testing more people.</p>""",
    how_figs=[pt_how],
    steps=[("Build a realistic prototype", "Figma or similar; real products, prices and wording, not lorem ipsum."),
           ("Write scenarios, not instructions", "“It's 17:40, you ordered dinner, your phone buzzes.” Never “tap the approve button”."),
           ("Recruit 5–6 per user type", "Customers matching the persona; pickers from Noord. Test in context."),
           ("Watch, don't help", "Ask them to think aloud; note hesitations, errors and quotes. One facilitator, one note-taker."),
           ("List findings by severity", "What, how many hit it, how bad, proposed fix."),
           ("Fix and re-test", "A second round on version two, before engineering starts.")],
    vocab=[("Prototype", "A model of the product that looks real enough to react to."),
           ("Usability test", "Watching real users try to complete tasks with a design."),
           ("Think-aloud", "Asking participants to say what they're thinking as they go."),
           ("Task scenario", "A realistic situation that gives the participant a goal."),
           ("Severity", "How badly a problem blocks users, and how many it affects."),
           ("Fidelity", "How close the prototype is to the real thing (paper → clickable).")],
    code=dict(file="product/research/2026-01-prototype-test.md", note="test plan and findings", plain=True, src="""
# Prototype test · approve-in-app v1          13–16 Jan 2026 · Grace (facilitator), Dee (notes)

Prototype   Figma, clickable; customer side + picker side; real Noord products and prices
Customers   6 express customers (tonight-dinner parents), on their own phone, at home
            Scenario: “It's 17:40. You ordered dinner at 17:30. Your phone buzzes.”
Pickers     3 Noord pickers, on the store handheld, wearing gloves
            Scenario: “Lactose-free milk is out of stock. Carry on with the order.”

Findings                                          who        severity   fix (v2)
F1 Didn't notice the 2-minute timer               5/6 cust   high       big countdown on top
F2 Asked “how much more is it?”                   4/6 cust   medium     show price difference
F3 Couldn't tap the buttons with gloves           3/3 pick   high       large buttons, full width
F4 Stood waiting for the answer                   3/3 pick   high       continue; apply at packing
F5 Wanted “never swap this item” right there      3/6 cust   medium     inline toggle (O3)

Next        v2 re-tested 22 Jan with 5 new customers + 2 pickers: F1–F4 resolved.
            → Ready for the backlog (vol. 2: story map and thin slices).
"""),
    tools="tools: Figma, Framer or ProtoPie for clickable prototypes; Lookback, Maze or a simple video call to watch remote sessions; paper sketches for very early tests. Get consent to record.",
    gains=["<b>Most usability problems found</b> before engineering starts.",
           "<b>Real context</b>: gloves, toddlers, 17:40 stress.",
           "<b>Cheap fixes</b>: a design change, not a sprint.",
           "<b>Persuasive</b>: watching users struggle convinces faster than arguments.",
           "<b>Staff screens tested too</b>: pickers are users."],
    losses=["<b>Not real behaviour at scale</b>: a test, not live use.",
            "<b>Recruiting and scheduling</b> take effort.",
            "<b>Prototype fidelity limits</b>: some issues only show with real data and speed.",
            "<b>Small samples</b> can't measure rates, only find problems."],
    baseline="Each line compares <b>a design review by the people who made it</b> to <b>two rounds of scenario-based tests with five or six real users per user type, in context</b>.",
    ratings=[(2, 5, "Real customers and pickers shape the design."),
             (3, 4, "Avoids shipping a flow that misses its outcome."),
             (2, 5, "Observed behaviour, not opinions in a review."),
             (2, 5, "Problems found in days, fixed in a week."),
             (3, 4, "Findings ranked by severity decide what to fix."),
             (2, 5, "Engineers who watch sessions understand the why."),
             (3, 4, "Joost sees his pickers' needs taken seriously."),
             (3, 4, "Fewer post-release fixes keep delivery flowing."),
             (3, 3, "A few days per round.")],
    pitfalls=[("Instructions instead of scenarios", "“Tap the approve button.”", "give a goal in a realistic situation; don't name the UI."),
              ("Helping participants", "“It's up there, on the top.”", "stay quiet; note where they got stuck."),
              ("Only testing customers", "Pickers get the screens on launch day.", "test every kind of user, in their real setting."),
              ("One round only", "Fixes are never checked.", "re-test version two before engineering starts.")],
    use=["Any new flow or significant screen change.",
         "Staff-facing tools used under pressure or with gloves.",
         "After a concierge test, before building.",
         "When the team disagrees about a design."],
    skip=["Measuring rates or preferences: use data or A/B tests.",
          "Tiny copy changes.",
          "When you don't yet know if the problem is worth solving: interview and test the value first."],
    related=["<b>Concierge &amp; Wizard-of-Oz MVP</b> (this volume)", "<b>Proto-personas</b> (this volume)", "<b>Customer journey map</b> (this volume)", "<b>Walking skeleton</b> (Ana, vol. 1)"],
    quiz=[("Why can't the designers judge the design themselves?", "They know how it works, so they can't see what's confusing."),
          ("How many users per group find most problems?", "About five; then fix and test again."),
          ("What's the difference between a scenario and an instruction?", "A scenario gives a goal in a realistic situation; an instruction names the UI to use."),
          ("What did the pickers' test reveal?", "Buttons too small for gloves, and pickers waiting idle for the answer.")],
    try_it="Take one screen your team will build next. Write a one-sentence scenario for it without naming any button. Show the design to three people outside the team and watch silently. Write down every place they hesitated.",
    remember="Tape the kitchen on the <span class=\"hl\">garage floor</span>. Watch five people <span class=\"hl\">cook</span> before you order it.",
    sources=["Jakob Nielsen, “Why You Only Need to Test with 5 Users” (nngroup.com, 2000).",
             "Steve Krug, <i>Don't Make Me Think, Revisited</i> (2014) and <i>Rocket Surgery Made Easy</i> (2010).",
             "Jake Knapp et al., <i>Sprint</i> (2016).",
             "Nielsen Norman Group, “Thinking Aloud: The #1 Usability Tool” (nngroup.com)."],
)

NOTES = [HYPOTHESES, FAKE_DOOR, CONCIERGE, PROTOTYPE_TESTING]
