# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 1 · Framing the problem.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 06 Opportunity Solution Tree
ost_problem = Doodle(760, 290, "Doodle of Grace's desk in November 2025, three weeks in. Four solution requests arrive from four people: Femke wants machine-learning recipe ideas, Joost wants a faster picking screen, Sam wants an automatic refund button for substitutions, Priya wants a smarter substitute algorithm. None of them says which outcome it serves. The team is about to build Sam's auto-refund, which would make refunds faster but not fewer: six percent of orders would still end in a refund.",
                     "Four good ideas, no outcome. The one about to be built makes refunds faster, not fewer.")
for i, (who, idea) in enumerate([("Femke", "recipe ideas"), ("Joost", "picking screen"), ("Sam", "auto-refund"), ("Priya", "smarter swaps")]):
    x = 18 + i * 186
    ost_problem.box(x, 20, 172, 72, idea, "y" if who != "Sam" else "pink", sub=f"— {who}", size=15, subsize=14,
                    stroke="red" if who == "Sam" else "")
    ost_problem.line(f"M{x + 86} 96 L380 150", dash=True, thin=True)
ost_problem.box(290, 150, 180, 50, "outcome?", "paper", dash=True, size=19)
ost_problem.arrow(475, 175, 540, 210, color="red")
ost_problem.box(546, 196, 200, 70, "refunds faster", "pink", sub="still 6 % of orders", stroke="red", size=17, subsize=14)
ost_problem.note(200, 246, "next sprint: Sam's button", "red")

ost_analogy = Doodle(760, 270, "Doodle of a doctor's notes. The goal is at the top: blood pressure down to 130 by spring. Below it, the possible causes the doctor found by listening: salt, stress, poor sleep. Under each cause, a few treatments. Under the chosen treatment, a small test: two weeks of less salt, then measure. The doctor doesn't start with the prescription.",
                     "A good doctor starts from the goal and the causes, not the prescription, and tests one treatment at a time.")
ost_analogy.box(260, 14, 240, 50, "BP down to 130", "green", size=18)
for i, (c, tr) in enumerate([("salt", "less salt"), ("stress", "walks"), ("sleep", "earlier nights")]):
    x = 40 + i * 240
    ost_analogy.line(f"M380 68 L{x + 90} 100", thin=True)
    ost_analogy.box(x, 100, 180, 48, c, "blue", size=17)
    ost_analogy.line(f"M{x + 90} 152 L{x + 90} 176", thin=True)
    ost_analogy.box(x, 176, 180, 40, tr, "y", size=15)
ost_analogy.box(40, 226, 180, 38, "test: 2 weeks", "paper", dash=True, size=14)
ost_analogy.note(580, 250, "goal → causes → treatments → tests", "pen", size=17)

ost_how = Doodle(760, 420, "Grace's opportunity solution tree for substitutions. The outcome at the top: refund tickets down from six percent to two percent of orders by the end of the second quarter of 2026. Four opportunities from customer interviews: I want a say before you swap; I want to know before the courier arrives; never swap this item for me; and the item should really be in stock. Under them, solutions: approve or reject the substitute in the app within two minutes, a phone call, a no-substitutes flag per item, a live order update, and better stock data from the StockPilot cache. Under the chosen solution, two experiments: a concierge test by phone at the Noord store and a clickable prototype with six customers.",
                 "Grace's tree: one outcome, four customer needs, a few ideas each, and the cheapest tests for the chosen branch.")
ost_how.box(230, 10, 300, 56, "refund tickets 6 % → 2 %", "green", sub="of orders, by end Q2 2026", size=18, subsize=14)
ost_how.note(640, 36, "outcome", "green", size=18)
opps = [("“let me say yes", "or no to a swap”"), ("“tell me before", "the courier comes”"), ("“never swap", "this for me”"), ("“it should be", "in stock at all”")]
for i, (a, b) in enumerate(opps):
    x = 12 + i * 186
    ost_how.line(f"M380 70 L{x + 86} 98", thin=True)
    ost_how.box(x, 98, 172, 66, None, "blue")
    ost_how.text(x + 86, 126, a, size=15)
    ost_how.text(x + 86, 150, b, size=15)
ost_how.note(12, 40, "↓ opportunities", "pen", anchor="start", size=16)
ost_how.note(12, 62, "(from interviews)", "pen", anchor="start", size=16)
for x, w, l1, l2, chosen, top in [(12, 82, "approve", "in app", True, 98), (102, 82, "a phone", "call", False, 98),
                                   (198, 172, "live order", "update", False, 284), (384, 172, "“no swaps”", "flag per item", False, 470),
                                   (570, 172, "better", "stock data", False, 656)]:
    ost_how.line(f"M{top} 168 L{x + w / 2} 200", thin=True)
    ost_how.box(x, 200, w, 56, None, "y" if chosen else "paper", stroke="green" if chosen else "")
    ost_how.text(x + w / 2, 224, l1, size=14)
    ost_how.text(x + w / 2, 244, l2, size=14)
ost_how.note(570, 280, "→ Ana's stock cache", "pen", anchor="start", size=15)
ost_how.note(200, 284, "↑ solutions (★ chosen)", "pen", anchor="start", size=16)
ost_how.text(16, 196, "★", "t-head t-green", anchor="start", size=18)
ost_how.line("M53 260 L53 300 M53 300 L120 328 M53 300 L340 328", thin=True, color="green")
ost_how.box(20, 330, 200, 60, "concierge test", "green", sub="phone calls at Noord", size=15, subsize=13)
ost_how.box(240, 330, 200, 60, "prototype test", "green", sub="6 customers, 3 pickers", size=15, subsize=13)
ost_how.note(600, 360, "experiments for", "pen", size=16)
ost_how.note(600, 384, "the chosen idea", "pen", size=16)

OST = dict(
    slug="opportunity-solution-tree",
    kicker="a.k.a. “the doctor doesn't start with the prescription”",
    tldr="Put <b>one outcome</b> at the top: a change in customer behaviour or a business number you can measure. Under it, the <b>opportunities</b>: customer needs and pains you found by listening, in the customer's words. Under each opportunity, several <b>solutions</b>. Under the solution you pick, the <b>experiments</b> that test it cheaply. The tree shows everyone <b>why</b> an idea is on the board, makes you compare ideas instead of falling for the first one, and turns stakeholder requests into branches you can weigh.",
    chips=[("Family", "framing the problem"), ("Origin", "Teresa Torres, <i>Continuous Discovery Habits</i> (2021); producttalk.org"), ("Lives in", "a wall or whiteboard, then a one-page tree the team updates weekly"), ("Pairs with", "customer interviews, assumption mapping, concierge MVP")],
    problem_side="Larder, Grace's third week",
    problem="""  <p class="lead">Three weeks in, Grace has four requests on her desk. Femke wants <b>ML recipe ideas</b> (an investor suggested it), Joost wants a <b>faster picking screen</b>, Sam wants an <b>automatic refund button</b> for substitutions so support can stop doing it by hand, and Priya wants a <b>smarter substitute algorithm</b>. All four are reasonable. None says which outcome it serves. Sam's button is already planned for the next sprint, and it would make refunds <i>faster</i>, not <i>fewer</i>: <span class="hl-pink">6 % of orders</span> would still end in a refund.</p>
  <ul>
    <li>Backlogs fill up with solutions; the problem behind each one is never written down.</li>
    <li>The idea with the loudest or most senior sponsor wins, not the one that moves the number.</li>
    <li>Nobody compares options, so the first idea for a need is the one that gets built.</li>
  </ul>""",
    problem_figs=[ost_problem],
    meanwhile=[("architect-1", "event-storming", "the substitutions hot spot on Ana's wall is where Grace's tree starts.", "Grace turned this hot spot into the outcome of her opportunity tree: refund tickets 6 % → 2 %."),
               ("architect-1", "asr", "Ana marks recipe ideas “not significant” for the architecture; Grace's tree parks them for the product.", "Grace's opportunity tree parks the recipe idea for the product too: it serves no outcome she's chasing."),
               ("architect-1", "spike-prototype-poc", "Ana's StockPilot spike decides what the “it should be in stock” branch can do.", "The result feeds Grace's “it should be in stock at all” branch: better stock data means fewer substitutions.")],
    analogy_side="the doctor's notes",
    analogy="""  <p>A good doctor doesn't start with the prescription. They agree a <b>goal</b> (blood pressure down to 130 by spring), find the likely <b>causes</b> by listening and examining (salt, stress, sleep), list a few <b>treatments</b> for each cause, and try one with a small <b>test</b>: two weeks, then measure. If it doesn't work, the notes show what to try next.</p>""",
    analogy_figs=[ost_analogy],
    map=[("The goal (BP down to 130)", "The outcome: refund tickets 6 % → 2 % of orders"),
         ("Causes found by listening", "Opportunities: customer needs and pains, in their words"),
         ("Treatments for each cause", "Solutions: several ideas per opportunity"),
         ("Two weeks of less salt, then measure", "Experiments: cheap tests of the chosen idea"),
         ("“Try something else” on the notes", "Going back up the tree when a test fails")],
    how_side="outcome → opportunities → solutions → experiments",
    how="""  <p>The order matters. Pick the <b>outcome</b> first, with your manager. Fill <b>opportunities</b> only from what customers actually said or did; if it came from a stakeholder, it's a solution and goes lower down. Compare at least <b>three solutions</b> for the opportunity you pick. Then test the riskiest assumption of the chosen one before building anything.</p>""",
    how_figs=[ost_how],
    steps=[("Agree one outcome", "A measurable change, owned by the team: “refund tickets 6 % → 2 % of orders by end Q2 2026”. Not a feature."),
           ("Map opportunities from evidence", "From interviews, tickets and data. Write them as the customer would say them: “let me say yes or no to a swap”."),
           ("Structure them", "Group similar needs; break big ones into smaller ones you could solve in weeks."),
           ("Pick one opportunity", "The one that most affects the outcome and that the team can do something about now."),
           ("Generate and compare solutions", "At least three. Stakeholder requests go here, next to the team's own ideas."),
           ("Test before building", "List the chosen idea's assumptions, test the riskiest cheaply, and update the tree every week.")],
    vocab=[("Outcome", "A measurable change in customer behaviour or a business result."),
           ("Output", "Something the team ships: a feature, a screen, a button."),
           ("Opportunity", "A customer need, pain or desire that, if met, moves the outcome."),
           ("Solution", "One idea for meeting an opportunity."),
           ("Experiment", "A cheap test of a solution's riskiest assumption."),
           ("Continuous discovery", "Talking to customers every week while building, not only at the start.")],
    code=dict(file="product/substitutions/opportunity-tree.md", note="Grace's tree, week of 10 Nov 2025", plain=True, src="""
OUTCOME   Refund tickets from substitutions: 6 % → 2 % of orders by end Q2 2026
          owner: Grace · agreed with Priya · baseline: re-tagged 400 tickets

├─ O1 “Let me say yes or no to a swap”        12/12 interviews · 71 % of tickets
│   ├─ S1 Approve or reject in the app, 2-minute window          ★ chosen
│   │    ├─ E1 Concierge: support phones Noord customers, 2 weeks
│   │    └─ E2 Clickable prototype: 6 customers, 3 pickers
│   ├─ S2 Picker phones the customer
│   └─ S3 Auto-refund button for support (Sam)       → faster, not fewer
├─ O2 “Tell me before the courier arrives”      7/12 interviews
│   └─ S4 Live order update with the substitute and its price
├─ O3 “Never swap this for me”                  5/12 interviews
│   └─ S5 A “no substitutes” flag per item, remembered
└─ O4 “It should just be in stock”             19 % of tickets
    ├─ S6 Better stock data (Ana: StockPilot cache, ADR 0005)
    └─ S7 Hide items below 3 in stock

Parked (no outcome on this tree): ML recipe ideas (Femke), faster picking screen
(Joost: belongs to the picking-speed tree).
"""),
    tools="tools: a whiteboard or sticky notes first. Miro, FigJam or Mural have opportunity-solution-tree templates; Vistaly and Productboard can keep the tree linked to the backlog. A Markdown tree in the repo, as above, is enough to share.",
    gains=["<b>Every idea has a why</b>: you can trace it up to an outcome.",
           "<b>Options get compared</b>: at least three solutions per opportunity.",
           "<b>Requests become branches</b>, not orders: Sam's button is weighed, not just built.",
           "<b>Shared picture</b>: the team, Priya and Femke see the same tree.",
           "<b>Faster learning</b>: experiments sit right under the idea they test."],
    losses=["<b>Discovery work</b>: interviews and data take time each week.",
            "<b>Hard conversations</b>: parking a CEO's idea needs care.",
            "<b>Can grow wild</b>: 40 opportunities and nothing chosen.",
            "<b>Needs a real outcome</b>: a vague goal makes a useless tree."],
    baseline="Each line compares <b>a backlog of solution requests from stakeholders</b> to <b>one outcome with a tree of evidence-based opportunities, compared solutions and cheap experiments, updated weekly</b>.",
    ratings=[(2, 5, "Opportunities come from customers, in their own words."),
             (2, 4, "Everything hangs under an outcome the business tracks."),
             (1, 4, "Opportunities need interview or ticket evidence to go on the tree."),
             (2, 4, "Experiments test ideas before any code is written."),
             (1, 5, "One outcome, one opportunity at a time."),
             (2, 5, "Anyone can point at the tree and say why we're building this."),
             (3, 4, "Stakeholders see their idea weighed, not ignored."),
             (3, 3, "Neutral; the tree picks what flows, not how fast."),
             (3, 3, "An hour a week to keep the tree current.")],
    pitfalls=[("Solutions disguised as opportunities", "“Customers need an approve button” sits on the opportunity row.", "write opportunities as the customer would say them; buttons are solutions."),
              ("An output as the outcome", "“Ship substitution approval by March” at the top.", "the top is a measured change: refund tickets, retention, time saved."),
              ("One solution per opportunity", "The first idea goes straight to the backlog.", "compare at least three, including “do nothing”."),
              ("Drawn once, never updated", "The tree from November still hangs on the wall in March.", "update it weekly as interviews and experiments come in.")],
    use=["A team owns an outcome and has more requests than capacity.",
         "Stakeholders keep sending solutions instead of problems.",
         "Before a big build: to check the idea is the best one for the need.",
         "Running continuous discovery alongside delivery."],
    skip=["Pure maintenance or compliance work with no choice to make.",
          "When there's no outcome yet: agree one with your manager first.",
          "Tiny fixes with an obvious cause and cure."],
    related=["<b>Customer interviews</b> (this volume)", "<b>Assumption mapping</b> (this volume)", "<b>Concierge &amp; Wizard-of-Oz MVP</b> (this volume)", "<b>Outcomes over outputs</b> (this volume)"],
    quiz=[("What are the four levels of the tree?", "Outcome, opportunities, solutions, experiments."),
          ("Where does a stakeholder's feature request go?", "At the solution level, under the opportunity it serves, next to other ideas."),
          ("Why was Sam's auto-refund button not chosen?", "It makes refunds faster, not fewer: it doesn't move the outcome of 6 % → 2 %."),
          ("How should opportunities be worded?", "As the customer would say them, based on interviews and data, not as features.")],
    try_it="Write your team's current outcome on a sticky note. Under it, put the last five requests you received. For each one, ask “which customer need does this serve?” and write that need as a separate sticky above it. How many requests share a need, and how many serve none?",
    remember="Start from the <span class=\"hl\">outcome</span>, not the prescription. Every idea hangs from a <span class=\"hl\">customer need</span>.",
    sources=["Teresa Torres, <i>Continuous Discovery Habits</i> (2021).",
             "Teresa Torres, “Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes” (producttalk.org).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018).",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017)."],
)

NOTES = [OST]
