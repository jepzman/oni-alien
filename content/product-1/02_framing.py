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


# ------------------------------------------------------------------ 05 Problem Statements
ps_problem = Doodle(760, 260, "Doodle of the brief Grace inherits: 'Build a substitution approval feature', a solution with no problem. In the first meeting the team debates button colours and whether to use a modal. Nobody can say who it's for, what it fixes or how they'll know it worked.",
                    "The brief is a solution. Within ten minutes the team is debating button colours.")
ps_problem.box(20, 30, 300, 80, "“build a substitution", "y", sub="approval feature”", size=17, subsize=17)
ps_problem.note(170, 136, "the brief, from the Q4 roadmap", "pen")
ps_problem.arrow(326, 70, 380, 70)
for i, t in enumerate(["button colour?", "a modal or a banner?", "how many seconds?"]):
    ps_problem.box(386, 16 + i * 46, 240, 38, t, "blue", size=14)
for i, q in enumerate(["for whom?", "fixes what?", "worked how?"]):
    ps_problem.note(690, 40 + i * 46, q, "red", size=18)
ps_problem.note(380, 226, "solutions argued, problem never written down", "red")

ps_analogy = Doodle(760, 240, "Doodle of calling a plumber. One caller says 'install a new pipe under the sink'. Another says 'the kitchen floor is wet every morning, near the dishwasher, since Tuesday'. A good plumber wants the second: it says who, where, when and how bad, and leaves the fix to the expert.",
                    "“Install a new pipe” vs “the floor is wet every morning near the dishwasher”. A good plumber wants the second.")
ps_analogy.icon("phone", 30, 60, 1.6)
ps_analogy.box(140, 30, 260, 70, "“install a new pipe”", "pink", sub="a solution", stroke="red", size=16, subsize=14)
ps_analogy.box(430, 30, 310, 110, None, "green")
ps_analogy.text(585, 62, "“the floor is wet every", size=15)
ps_analogy.text(585, 86, "morning near the dishwasher,", size=15)
ps_analogy.text(585, 110, "since Tuesday”", size=15)
ps_analogy.note(585, 166, "who · where · when · how bad", "green")
ps_analogy.note(270, 130, "✗ the fix is guessed", "red")

ps_how = Doodle(760, 340, "The parts of Grace's problem statement for substitutions. Who: the tonight-dinner parent ordering express. Struggle: finds out about substitutions at the door, too late to act. Why it matters to them: no dinner ingredient, sometimes an allergy risk, a trip to the corner shop. Impact on Larder: six percent of orders end in a refund ticket, about 45,000 euros a month in refunds and support time, and customers with two refund tickets in a month order 30 percent less. How we'll know it's solved: refund tickets from substitutions below two percent of orders.",
                 "Five parts, one paragraph, no solution in it.")
parts = [("who", "the tonight-dinner parent, express", "blue"), ("struggles with", "finding out about swaps at the door", "y"),
         ("which means", "no ingredient, allergy risk, a trip out", "y"), ("costing us", "6 % refund tickets · ~€45k/month", "pink"),
         ("solved when", "swap refund tickets < 2 % of orders", "green")]
for i, (k, v, f) in enumerate(parts):
    y = 14 + i * 60
    ps_how.box(14, y, 170, 50, k, "paper", size=16)
    ps_how.arrow(188, y + 25, 220, y + 25)
    ps_how.box(226, y, 520, 50, None, f)
    ps_how.text(242, y + 32, v, anchor="start", size=16)
ps_how.note(380, 328, "no buttons, no screens: the team designs the fix", "pen")

PROBLEM_STATEMENTS = dict(
    slug="problem-statements",
    kicker="a.k.a. “the floor is wet near the dishwasher”",
    tldr="Before anyone proposes a fix, write the problem down in <b>one short paragraph</b>: <b>who</b> struggles, <b>with what</b>, <b>why it matters</b> to them, what it <b>costs</b> the business, and how you'll <b>know it's solved</b>. No solution words. A good problem statement ends solution debates that start too early, lets the team find better fixes, and gives everyone the same target.",
    chips=[("Family", "framing the problem"), ("Origin", "design thinking (“point of view” statements); Lean UX problem statements"), ("Lives in", "the top of every brief, ticket epic and roadmap item"), ("Pairs with", "opportunity solution tree, outcomes over outputs, customer interviews")],
    problem_side="Larder, the inherited brief",
    problem="""  <p class="lead">The Q4 roadmap Grace inherits says: <i>“Build a substitution approval feature.”</i> In the first meeting about it, the team spends twenty minutes on <b>button colours</b>, modals and timeouts. Nobody can say who it's for, what exactly it fixes, or how they'll know it worked. The brief is a <span class="hl-pink">solution with no problem attached</span>.</p>
  <ul>
    <li>Briefs written as solutions lock in the first idea.</li>
    <li>Teams argue about details because they don't share the goal.</li>
    <li>Without a “solved when”, nobody can tell if the work succeeded.</li>
  </ul>""",
    problem_figs=[ps_problem],
    meanwhile=[("architect-1", "quality-attribute-scenarios", "Ana rewrites “fast” as a testable scenario; Grace rewrites “build approval” as a testable problem.", "Grace does the same for the product: “build an approval feature” becomes a problem with a measure.")],
    analogy_side="calling the plumber",
    analogy="""  <p>One caller tells the plumber <b>“install a new pipe under the sink”</b>. Another says <b>“the kitchen floor is wet every morning near the dishwasher, since Tuesday”</b>. A good plumber much prefers the second: it says where, when and how bad, and leaves the fix to the expert. The first might get a new pipe and a floor that's still wet.</p>""",
    analogy_figs=[ps_analogy],
    map=[("“The floor is wet near the dishwasher”", "Who struggles, with what, when"),
         ("“Every morning, since Tuesday”", "Evidence: 6 % of orders, ticket data, interviews"),
         ("“The parquet is starting to warp”", "The cost: refunds, support time, lost orders"),
         ("“Install a new pipe”", "A solution disguised as a request"),
         ("The plumber finds the leak", "The team designs the fix")],
    how_side="five parts, no solution",
    how="""  <p>Write it with the team, from interview and data evidence. Read it back and delete every word that describes a solution (button, screen, notification). If the team can't agree on the paragraph, they wouldn't have agreed on the feature either, and it's far cheaper to find that out now.</p>""",
    how_figs=[ps_how],
    steps=[("Name who", "A persona or job, not “users”: “the tonight-dinner parent, ordering express”."),
           ("Describe the struggle", "What goes wrong, when, in the customer's terms."),
           ("Say why it matters to them", "The consequence for the customer: no dinner ingredient, a trip out, allergy risk."),
           ("Add the cost to the business", "Numbers: refund rate, support hours, lost orders."),
           ("Write “solved when”", "The measure that shows it's fixed: swap refunds below 2 % of orders."),
           ("Strip out solutions", "Delete product words; agree the paragraph before any design starts.")],
    vocab=[("Problem statement", "A short description of a problem, without a solution."),
           ("Point of view", "Design-thinking name for a user + need + insight statement."),
           ("Success criterion", "The measurable sign that the problem is solved."),
           ("Solution bias", "Jumping to a fix before the problem is understood."),
           ("Problem space / solution space", "Understanding the need / designing the answer."),
           ("Brief", "The document that starts a piece of work.")],
    code=dict(file="product/substitutions/problem.md", note="problem statement, agreed 7 Nov 2025", plain=True, src="""
# Problem: substitution surprises                      agreed: Grace, Priya, Ben, Dee, Sam

Who        Express customers, mostly the tonight-dinner parent (product/personas/)
Struggle   When an item is out of stock, the picker swaps it without asking.
           The customer finds out at the door, too late to do anything.
Matters    No ingredient for tonight's dinner; sometimes an allergy risk;
           a second trip to the corner shop.
Costs us   6 % of orders end in a refund ticket (re-tagged baseline, 400 tickets)
           ≈ €45,000 / month in refunds and support time
           Customers with 2+ refund tickets in a month order 30 % less next month
Solved     Refund tickets from substitutions < 2 % of orders, by end Q2 2026,
when       with no drop in express on-time rate (88 % today)

Not in this statement: any button, screen or notification. That's the team's job.
"""),
    tools="tools: a paragraph at the top of the brief. Lean UX and IDEO's design-thinking guides have problem-statement templates; some teams use a “how might we…?” question to open ideation once the statement is agreed.",
    gains=["<b>Earlier agreement</b> on what matters, before design starts.",
           "<b>Better fixes</b>: the team can find options you didn't think of.",
           "<b>A finish line</b>: “solved when” says when to stop.",
           "<b>Faster reviews</b>: every design is checked against one paragraph.",
           "<b>Stakeholders see the cost</b>, so priority is easier to argue."],
    losses=["<b>Feels slow</b> to people who already “know” the solution.",
            "<b>Needs evidence</b>: numbers and interviews take time.",
            "<b>Can be gamed</b>: a solution disguised as a problem.",
            "<b>Uncomfortable</b> when the inherited brief gets rewritten."],
    baseline="Each line compares <b>briefs written as solutions (“build approval”)</b> to <b>a five-part problem statement agreed with the team before design starts</b>.",
    ratings=[(2, 4, "The fix starts from the customer's real struggle."),
             (2, 4, "The cost to the business is in the statement."),
             (2, 4, "Numbers and interviews back every part."),
             (3, 3, "Neutral; it sets up the learning that follows."),
             (2, 5, "One paragraph replaces twenty minutes of button debates."),
             (2, 5, "The whole team can say what problem they're solving."),
             (3, 4, "Priya and Femke see the cost, not just the feature."),
             (3, 3, "Neutral."),
             (3, 4, "An hour with the team.")],
    pitfalls=[("A solution in disguise", "“Customers lack an approval button.”", "delete product words; describe the struggle."),
              ("No “solved when”", "Nobody knows when to stop or if it worked.", "add a measurable success criterion."),
              ("“Users” as the who", "Everyone, so no one.", "name the persona or job."),
              ("Written alone", "Grace writes it; the team never reads it.", "agree it with the team before design starts.")],
    use=["At the start of any epic, project or roadmap item.",
         "When a brief arrives as a solution.",
         "When design debates go round in circles.",
         "Before asking for budget or priority."],
    skip=["Tiny fixes where the problem is obvious (a typo, a broken link).",
          "Pure tech maintenance with its own clear goal.",
          "When the problem isn't understood yet: interview first."],
    related=["<b>Opportunity solution tree</b> (this volume)", "<b>Outcomes over outputs</b> (this volume)", "<b>Customer interviews</b> (this volume)", "<b>Quality attribute scenarios</b> (Ana, vol. 1)"],
    quiz=[("What are the five parts of Grace's problem statement?", "Who, the struggle, why it matters to them, the cost to the business, and “solved when”."),
          ("What's wrong with “build a substitution approval feature” as a brief?", "It's a solution: it says nothing about who, what problem, or how to know it worked."),
          ("Why remove all product words?", "So the team can find the best fix instead of the first one."),
          ("What was Larder's “solved when”?", "Refund tickets from substitutions below 2 % of orders by end Q2 2026, with no drop in on-time rate.")],
    try_it="Take the top item on your roadmap. Write its problem statement in five parts without any product words. Read it to the team and ask each person to name one solution. If they all name the same one, ask for two more each.",
    remember="Describe the <span class=\"hl\">wet floor</span>, not the pipe. Then let the team find the leak.",
    sources=["Jeff Gothelf &amp; Josh Seiden, <i>Lean UX</i>, 3rd ed. (2021), problem statements.",
             "IDEO, <i>The Field Guide to Human-Centered Design</i> (2015).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018).",
             "Thomas Wedell-Wedellsborg, <i>What's Your Problem?</i> (2020)."],
)

# ------------------------------------------------------------------ 07 Assumption Mapping
am_problem = Doodle(760, 270, "Doodle of the team falling in love with the approve-in-app idea. Everyone is ready to build. But the idea rests on things nobody has checked: that customers answer within two minutes, that pickers can wait two minutes without slowing down, that push notifications reach customers, and that the price difference of a substitute can be charged. If the first is false, the whole feature is wasted.",
                    "Everyone loves the idea. It stands on four legs nobody has checked.")
am_problem.box(230, 20, 300, 70, "approve in the app!", "y", sub="team vote: 9 of 9", size=18, subsize=14)
legs = ["customers answer in 2 min?", "pickers can wait 2 min?", "push reaches them?", "price change allowed?"]
for i, t in enumerate(legs):
    x = 14 + i * 186
    am_problem.line(f"M380 94 L{x + 86} 150", dash=True, thin=True, color="red")
    am_problem.box(x, 150, 172, 60, None, "pink", stroke="red")
    am_problem.text(x + 86, 176, " ".join(t.split(" ")[:2]), size=14)
    am_problem.text(x + 86, 198, " ".join(t.split(" ")[2:]), size=14)
am_problem.note(380, 248, "unchecked: if leg one breaks, the feature is wasted", "red")

am_analogy = Doodle(760, 260, "Doodle of planning an outdoor wedding on a two by two grid: how important an assumption is, and how much evidence there is for it. Good weather is very important and has no evidence, so it gets a plan B tent. The caterer can serve 120 is important but proven. Guests like fish matters less.",
                    "An outdoor wedding: “it won't rain” is important and unproven, so book the tent.")
am_analogy.line("M100 230 V20 M100 230 H740", thin=True)
am_analogy.text(92, 120, "important", "t-s", anchor="end", size=15)
am_analogy.note(420, 254, "evidence →", size=16)
am_analogy.line("M420 24 V226 M104 125 H736", dash=True, thin=True)
am_analogy.box(116, 34, 290, 80, "“it won't rain”", "pink", sub="→ book a tent", stroke="red", size=16, subsize=14)
am_analogy.box(436, 34, 290, 80, "caterer serves 120", "green", sub="did it last month", size=16, subsize=14)
am_analogy.box(436, 140, 290, 70, "guests like fish", "paper", sub="low stakes", size=15, subsize=13)
am_analogy.note(260, 170, "test or plan B here", "red")

am_how = Doodle(760, 380, "Grace's assumption map for approve-in-app. Assumptions are grouped as desirable, viable, feasible and usable, and placed on a grid of importance against evidence. Top left, important with little evidence, test first: customers answer within two minutes, and pickers can wait two minutes without slowing the line. Important with evidence: customers want to be asked, from twelve interviews. Less important: the substitute's price difference, which Lena says is fine with consent. Push reaching customers has some evidence: sixty percent have notifications on.",
                 "Important and unproven goes top left: test those first, with the cheapest experiment you can.")
am_how.line("M90 330 V20 M90 330 H740", thin=True)
am_how.text(84, 175, "important", "t-s", anchor="end", size=15)
am_how.note(415, 360, "evidence →", size=16)
am_how.line("M415 24 V326 M94 175 H736", dash=True, thin=True)
am_how.note(252, 44, "TEST FIRST → concierge test", "red", size=17)
for (x, y, t, s, f, st) in [(104, 60, "answer in 2 min", "desirable · usable", "pink", "red"), (104, 120, "pickers can wait", "viable · Joost", "pink", "red"),
                            (430, 60, "they want to be asked", "12 of 12 interviews", "green", ""), (430, 120, "push reaches them", "60 % have it on", "y", ""),
                            (430, 220, "price change OK", "Lena: with consent", "paper", ""), (104, 220, "offline picker app", "Ana: ASR-2", "blue", "")]:
    am_how.box(x, y, 296, 50, None, f, stroke=st)
    am_how.head(x + 14, y + 22, t, anchor="start", size=15)
    am_how.text(x + 14, y + 42, s, "t t-soft", anchor="start", size=13)

ASSUMPTIONS = dict(
    slug="assumption-mapping",
    kicker="a.k.a. “book the tent”",
    tldr="Every idea rests on things that must be true: customers want it (<b>desirable</b>), they can use it (<b>usable</b>), we can build it (<b>feasible</b>), and it works for the business (<b>viable</b>). List them, then place each on a grid of <b>importance</b> (does the idea fail if it's false?) against <b>evidence</b> (how sure are we?). Test the <b>important, unproven</b> ones first, as cheaply as you can, before building anything.",
    chips=[("Family", "framing the problem"), ("Origin", "David J. Bland, <i>Testing Business Ideas</i> (2019); Marty Cagan's four risks"), ("Lives in", "a 2×2 on the wall next to the opportunity tree"), ("Pairs with", "opportunity solution tree, testable hypotheses, concierge MVP")],
    problem_side="Larder, a team in love",
    problem="""  <p class="lead">The team picks <b>approve in the app</b> from the opportunity tree, and everyone loves it: nine votes out of nine. Ben is already sketching the API. But the idea stands on legs nobody has checked: that customers <b>answer within two minutes</b>, that pickers can <b>wait two minutes</b> without slowing the line, that push notifications <b>reach</b> customers, that charging a substitute's <b>price difference</b> is allowed. If the first one is false, <span class="hl-pink">the whole feature is wasted</span>.</p>
  <ul>
    <li>Excitement hides assumptions; the more a team likes an idea, the fewer it questions.</li>
    <li>Teams test what's easy (can we build it?) instead of what's risky (will they use it?).</li>
    <li>The riskiest assumption is usually found after launch, the most expensive moment.</li>
  </ul>""",
    problem_figs=[am_problem],
    meanwhile=[("architect-1", "constraints-assumptions", "Ana sorts the technical plan into constraints and assumptions; Grace does the same for the product idea.", "Grace maps the product's assumptions the same way, and tests the riskiest with a concierge test.")],
    analogy_side="the outdoor wedding",
    analogy="""  <p>Planning an outdoor wedding, some beliefs matter more than others. <b>“It won't rain”</b> is very important and you have no evidence, so you <b>book a tent</b>. “The caterer can serve 120” is important, but they did it last month. “Guests like fish” barely matters. You spend your worry, and your money, on the top-left corner.</p>""",
    analogy_figs=[am_analogy],
    map=[("“It won't rain”", "“Customers answer within 2 minutes”"),
         ("Booking a tent", "A cheap test, or a plan B"),
         ("“The caterer did 120 last month”", "“They want to be asked”: 12 of 12 interviews"),
         ("“Guests like fish”", "Low-stakes details you can fix later"),
         ("The grid on the planner's desk", "The assumption map on the team wall")],
    how_side="list, place, test the top-left",
    how="""  <p>Brainstorm assumptions with the whole team using the four risk types as prompts, so you don't only list technical ones. Place each sticky on the grid <b>together</b>, arguing about evidence. The top-left quadrant is the test plan.</p>""",
    how_figs=[am_how],
    steps=[("Pick one idea", "One solution from the tree: “approve or reject a substitute in the app, within 2 minutes”."),
           ("List assumptions by risk type", "Desirable, usable, feasible, viable. Ask “what must be true?” for each."),
           ("Write them as statements", "“Customers answer within 2 minutes”, not “speed?”."),
           ("Place them on the grid", "Importance (fails if false?) × evidence (how sure, and from what?)."),
           ("Test the top-left first", "The cheapest test that could prove it wrong: a concierge test, a prototype, a data query."),
           ("Re-map after each test", "Evidence moves stickies right; failed ones change the idea.")],
    vocab=[("Assumption", "Something that must be true for an idea to work."),
           ("Desirability", "Customers want it."),
           ("Usability", "Customers can figure out how to use it."),
           ("Feasibility", "We can build and run it."),
           ("Viability", "It works for the business: cost, legal, operations."),
           ("Leap of faith", "An important assumption with no evidence yet.")],
    code=dict(file="product/substitutions/assumptions.md", note="assumption map, 12 Nov 2025", plain=True, src="""
# Assumption map · idea S1: approve or reject a substitute in the app (2-min window)

TEST FIRST (important, little evidence)
 A1 desirable/usable  Customers answer within 2 minutes            evidence: none
 A2 viable (Joost)    Pickers can wait 2 min without slowing picks  evidence: none
    → test both: concierge test at Noord, 2 weeks (Sam's team phones customers)

KNOWN (important, evidence)
 A3 desirable  Customers want to be asked                12/12 interviews
 A4 feasible   Push notifications reach them             60 % have push on → SMS fallback?

LATER (less important)
 A5 viable     Charging the substitute's price difference is allowed   Lena: yes, with consent
 A6 feasible   Picker app shows the answer when offline                Ana: ASR-2, offline-first

Re-map after the concierge test (due 19 Dec).
"""),
    tools="tools: stickies on a 2×2, or the assumption-mapping templates from Strategyzer (Testing Business Ideas) in Miro or FigJam. Keep the evidence source next to each sticky.",
    gains=["<b>Risk made visible</b>: the leaps of faith are named.",
           "<b>Right test first</b>: desirability and viability, not just feasibility.",
           "<b>Cheaper failures</b>: a two-week test instead of a two-month build.",
           "<b>Healthy doubt</b> without killing the team's enthusiasm.",
           "<b>Shared risk picture</b> with operations and legal."],
    losses=["<b>Slows the start</b> of a popular idea.",
            "<b>Evidence ratings are judgement calls.</b>",
            "<b>Tests cost time</b>, and some can't be done cheaply.",
            "<b>Can become a ritual</b> if tests never change the idea."],
    baseline="Each line compares <b>building a popular idea straight away</b> to <b>mapping its assumptions by importance and evidence, and testing the riskiest before building</b>.",
    ratings=[(3, 4, "The idea is checked against what customers will really do."),
             (2, 4, "Viability (picking speed, legal) is tested early."),
             (2, 5, "Each assumption shows its evidence source."),
             (2, 5, "The riskiest question gets answered first."),
             (2, 4, "Tests target the two assumptions that matter most."),
             (2, 4, "Ops, legal and engineering see the same risks."),
             (3, 4, "Joost and Lena see their concerns on the map."),
             (3, 2, "Testing first delays the start of building."),
             (3, 3, "An hour to map; tests cost more.")],
    pitfalls=[("Only feasibility", "The map lists APIs and databases.", "use all four risk types as prompts."),
              ("Vague stickies", "“Speed?” “Adoption?”", "write testable statements with a number."),
              ("Map, no tests", "A lovely grid; the build starts anyway.", "the top-left quadrant is the test plan, with dates."),
              ("Evidence inflation", "“We all feel strongly” counts as evidence.", "evidence means data, interviews or tests, with a source.")],
    use=["Before building any idea that takes more than a sprint.",
         "When the team is very sure of an idea.",
         "When operations, legal or finance are affected.",
         "To choose between experiments."],
    skip=["Small, reversible changes: ship and watch the data.",
          "When the assumptions were already tested.",
          "Pure maintenance with no customer or business risk."],
    related=["<b>Opportunity solution tree</b> (this volume)", "<b>Testable hypotheses</b> (this volume)", "<b>Concierge &amp; Wizard-of-Oz MVP</b> (this volume)", "<b>Constraints vs assumptions</b> (Ana, vol. 1)"],
    quiz=[("Name the four risk types.", "Desirable, usable, feasible, viable."),
          ("What are the grid's two axes?", "Importance (does the idea fail if it's false?) and evidence (how sure are we?)."),
          ("Which assumptions do you test first?", "Important ones with little evidence: the top-left quadrant."),
          ("What were Larder's two test-first assumptions?", "Customers answer within 2 minutes; pickers can wait 2 minutes without slowing down.")],
    try_it="Take the idea your team is most excited about. In 15 minutes, write ten assumptions, at least two per risk type. Place them on the grid together. What's in the top-left corner, and what's the cheapest way to test it this week?",
    remember="Love the idea, then <span class=\"hl\">book the tent</span>: test the important, unproven leg first.",
    sources=["David J. Bland &amp; Alexander Osterwalder, <i>Testing Business Ideas</i> (2019).",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), the four big risks.",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021), assumption testing.",
             "Jeff Gothelf &amp; Josh Seiden, <i>Lean UX</i>, 3rd ed. (2021)."],
)

# ------------------------------------------------------------------ 08 Outcomes over Outputs
oo_problem = Doodle(760, 270, "Doodle of last year's roadmap: fourteen features with dates. Eleven shipped on time and the team celebrated. In the same year the refund rate didn't move and express on-time stayed at 88 percent. Now Femke adds ML recipe ideas, an investor's suggestion, as feature fifteen.",
                    "Eleven of fourteen features shipped on time. Not one number that mattered moved.")
oo_problem.box(20, 20, 260, 220, None, "paper")
oo_problem.head(150, 46, "roadmap 2025", size=17)
for i in range(7):
    oo_problem.text(40, 76 + i * 22, ("✓ feature " if i < 6 else "✗ feature ") + str(i + 1), "t t-red" if i == 6 else "t", anchor="start", size=14)
oo_problem.note(150, 262, "11 of 14 shipped on time", "green", size=17)
oo_problem.box(320, 30, 200, 70, "refund rate", "pink", sub="still 6 %", stroke="red", size=17, subsize=14)
oo_problem.box(540, 30, 200, 70, "express on time", "pink", sub="still 88 %", stroke="red", size=16, subsize=14)
oo_problem.box(400, 150, 260, 64, "+ ML recipe ideas", "y", sub="feature 15 (an investor's idea)", size=16, subsize=13)

oo_analogy = Doodle(760, 240, "Doodle of a gym card with twelve visits stamped, next to the real goal: run 5 kilometres in 30 minutes by June. Twelve visits is the output. Running faster is the outcome. You can collect every stamp and still not get fitter.",
                    "Twelve stamps on the gym card is an output. Running 5 km in 30 minutes is the outcome.")
oo_analogy.box(30, 40, 300, 150, None, "paper")
oo_analogy.head(180, 70, "gym card", size=17)
for i in range(12):
    oo_analogy.raw(f'<circle class="d d-thin f-y" cx="{60 + (i % 6) * 48}" cy="{110 + (i // 6) * 44}" r="14"/>')
oo_analogy.note(180, 214, "output: 12 visits ✓", "pen")
oo_analogy.box(420, 60, 310, 100, "5 km in 30 min", "green", sub="by June · today 36 min", size=19, subsize=15)
oo_analogy.note(575, 190, "outcome: did I get fitter?", "green")

oo_how = Doodle(760, 330, "The chain from work to results, with Larder's example. Activities and outputs: the team builds and ships approve-in-app. Outcome: customers change behaviour, answering swap requests, so refund tickets fall from six to two percent. Impact: business drivers move: stay trusted, and cost per order falls because refunds and support time drop. The roadmap is written at the outcome level; features are bets under each outcome.",
                 "Write the roadmap at the outcome level. Features are bets underneath, not promises on top.")
chain = [("output", "approve-in-app", "what we ship", "paper"), ("outcome", "refund tickets", "6 % → 2 %", "green"), ("impact", "drivers 3 & 4", "trust · €/order", "blue")]
for i, (k, v, s, f) in enumerate(chain):
    x = 14 + i * 256
    oo_how.note(x + 112, 30, k, "pen", size=18)
    oo_how.box(x, 44, 224, 90, v, f, sub=s, size=18, subsize=15)
    if i < 2:
        oo_how.arrow(x + 228, 89, x + 252, 89)
oo_how.raw('<rect class="f-hl" x="262" y="150" width="236" height="12" rx="4" style="stroke:none"/>')
oo_how.note(380, 190, "the roadmap lives here", "green", size=19)
oo_how.box(14, 230, 360, 80, "recipe ideas (ML)?", "pink", sub="which outcome? none → parked", stroke="red", size=16, subsize=14)
oo_how.box(400, 230, 346, 80, "feature as a bet", "y", sub="kept only if the outcome moves", size=16, subsize=14)

OUTCOMES = dict(
    slug="outcomes-over-outputs",
    kicker="a.k.a. “twelve gym visits isn't fitness”",
    tldr="An <b>output</b> is what you ship: a feature, a screen. An <b>outcome</b> is a change in what customers do that you can measure: fewer refund tickets, more repeat orders. An <b>impact</b> is the business result that follows. Judge work, and write the roadmap, by <b>outcomes</b>. Features become <b>bets</b> under an outcome, kept if the number moves and dropped if it doesn't. It's also the kindest way to say no: “which outcome does this serve?”",
    chips=[("Family", "framing the problem"), ("Origin", "Joshua Seiden, <i>Outcomes Over Output</i> (2019); logic models in programme evaluation"), ("Lives in", "the roadmap's rows and the team's goals"), ("Pairs with", "north star metric, opportunity solution tree, OKRs (vol. 4)")],
    problem_side="Larder, last year's roadmap",
    problem="""  <p class="lead">Larder's 2025 roadmap was a list of <b>fourteen features with dates</b>. Eleven shipped on time, and the team celebrated. In the same year the refund rate stayed at <b>6 %</b> and express on-time stayed at <b>88 %</b>. Now Femke adds feature fifteen: <b>ML recipe ideas</b>, suggested by an investor. Nobody can say what number it's meant to move, only that it would be <span class="hl-pink">delivered on time</span>.</p>
  <ul>
    <li>Success measured as “shipped” rewards busyness, not results.</li>
    <li>Feature lists make every request look equally worth doing.</li>
    <li>Saying no to a senior idea is personal when there's no outcome to point to.</li>
  </ul>""",
    problem_figs=[oo_problem],
    meanwhile=[("architect-1", "business-drivers", "Ana's four drivers are the impact level of Grace's chain; refund tickets are an outcome that moves drivers 3 and 4.", "Grace ties her outcomes to these drivers: fewer refund tickets move “stay trusted” and cost per order.")],
    analogy_side="the gym card",
    analogy="""  <p>A gym card with <b>twelve stamps</b> looks like progress. But the goal was to <b>run 5 km in 30 minutes by June</b>, and you can collect every stamp without getting any fitter. The stamps are outputs. The time on the stopwatch is the outcome. Only one of them is why you joined.</p>""",
    analogy_figs=[oo_analogy],
    map=[("A stamp on the gym card", "A shipped feature (output)"),
         ("Running 5 km in 30 minutes", "Refund tickets 6 % → 2 % (outcome)"),
         ("Feeling healthier, sleeping better", "Drivers move: trust, cost per order (impact)"),
         ("Changing the workout when times don't improve", "Dropping a bet when the outcome doesn't move"),
         ("A personal trainer asking “why this exercise?”", "Asking “which outcome does this serve?”")],
    how_side="outputs serve outcomes serve impact",
    how="""  <p>Pick a few outcomes the team can influence directly (customer behaviour), each linked to an impact the business already tracks. Put <b>outcomes on the roadmap</b>, features underneath as <b>bets</b>, and review the numbers after each release. Requests that don't serve an outcome go to a parking list, with the reason.</p>""",
    how_figs=[oo_how],
    steps=[("Name the impact", "The business result you're after: Ana's driver 4 (trust) and driver 3 (cost per order)."),
           ("Find the behaviour that drives it", "What customers do differently: answer swap requests; fewer refund tickets."),
           ("Make it measurable", "Baseline, target, date: 6 % → 2 % by end Q2 2026."),
           ("Hang features under it as bets", "Each with what you expect it to move, and by how much."),
           ("Review after every release", "Did the outcome move? Keep, change or drop the bet."),
           ("Park what serves no outcome", "With the reason: “recipes: no outcome on this quarter's roadmap”.")],
    vocab=[("Output", "What the team makes and ships."),
           ("Outcome", "A measurable change in customer behaviour."),
           ("Impact", "The business result: revenue, cost, retention, trust."),
           ("Bet", "A feature you expect to move an outcome, and will check."),
           ("Feature factory", "A team judged only by how much it ships."),
           ("Parking lot", "Ideas kept for later, with the reason they wait.")],
    code=dict(file="product/roadmap/q1-2026.md", note="outcome-based roadmap, draft", plain=True, src="""
# Ordering & apps · Q1 2026                                  owner: Grace

OUTCOME 1  Refund tickets from substitutions 6 % → 2 % of orders (by end Q2)
           impact: driver 4 (trust), driver 3 (€/order: ~€45k/month)
  bets     approve-or-reject in the app (2-min window)     expect −3 pts
           “never swap this” flag per item                 expect −0.5 pt
           live order update before the courier arrives    expect −0.5 pt

OUTCOME 2  Express orders delivered complete and on time: 82 % → 90 %
           impact: driver 2 (keep the promise)          shared with Joost
  bets     substitute decided before packing (with outcome 1)
           ETA shown from Dispatch (Ana: Dispatch service)

PARKED     ML recipe ideas (Femke): no outcome this quarter; revisit with
           retention data in Q3 · faster picking screen → Joost's roadmap
"""),
    tools="tools: a roadmap doc or board grouped by outcome (Now / Next / Later works well, see vol. 2). Productboard, Jira Product Discovery and Aha! all support outcome-based roadmaps; a Markdown file is enough.",
    gains=["<b>Results, not busyness</b>: success is a number that matters.",
           "<b>A kind way to say no</b>: “which outcome does this serve?”",
           "<b>Freedom to find better fixes</b> than the first feature.",
           "<b>Honest reviews</b>: bets that don't work get dropped.",
           "<b>Leadership speaks the same language</b> as the team."],
    losses=["<b>Less certainty</b>: no feature list with dates to promise.",
            "<b>Measurement work</b>: you need baselines and tracking.",
            "<b>Slower signals</b>: outcomes can take weeks to move.",
            "<b>Uncomfortable</b> for stakeholders used to feature promises."],
    baseline="Each line compares <b>a roadmap of features with dates, judged by delivery</b> to <b>a roadmap of measurable outcomes with features as bets underneath, reviewed after each release</b>.",
    ratings=[(2, 4, "Work is chosen by the change it makes for customers."),
             (2, 5, "Every outcome links to a business driver."),
             (2, 4, "Bets are judged on measured results."),
             (2, 4, "Reviews after each release show what worked."),
             (2, 5, "Requests without an outcome get parked."),
             (2, 4, "The team knows what number it's trying to move."),
             (3, 3, "Leaders gain clarity but lose dated feature promises."),
             (3, 3, "Neutral."),
             (3, 3, "Measuring and reviewing take regular time.")],
    pitfalls=[("Outputs dressed as outcomes", "“Outcome: launch approve-in-app.”", "an outcome is a change in behaviour with a number."),
              ("Outcomes the team can't move", "“Grow revenue 30 %” for one team.", "pick behaviour the team can influence, linked to the impact."),
              ("Never reviewing bets", "Features ship; nobody checks the number.", "review the outcome after each release; drop bets that don't work."),
              ("Using it as a weapon", "“No outcome, no discussion.”", "park with a reason and a date to revisit.")],
    use=["Writing or reshaping a roadmap.",
         "When the team ships a lot and nothing moves.",
         "When senior requests pile up.",
         "Setting team goals for a quarter."],
    skip=["Contractual or legal deadlines: those are fixed outputs.",
          "Tiny fixes and maintenance.",
          "When nothing can be measured yet: build the measurement first."],
    related=["<b>North star metric</b> (this volume)", "<b>Opportunity solution tree</b> (this volume)", "<b>Problem statements</b> (this volume)", "<b>Business drivers &amp; goals</b> (Ana, vol. 1)"],
    quiz=[("What's the difference between an output and an outcome?", "An output is what you ship; an outcome is a measurable change in what customers do."),
          ("How does impact relate to outcome?", "Outcomes (behaviour) drive impact (business results like trust or cost per order)."),
          ("Why were the ML recipe ideas parked?", "They served no outcome on the quarter's roadmap; they'll be revisited with retention data."),
          ("What happens to a bet that doesn't move its outcome?", "It's changed or dropped after the review.")],
    try_it="Take your last three shipped features. For each, write the outcome it was supposed to move, and check whether it did. If you can't name the outcome, write down what you'd measure next time before building.",
    remember="Count the <span class=\"hl\">running time</span>, not the gym stamps. Features are <span class=\"hl\">bets</span>.",
    sources=["Joshua Seiden, <i>Outcomes Over Output</i> (2019).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018).",
             "John Cutler, “12 Signs You're Working in a Feature Factory” (2016).",
             "Bruce McCarthy et al., <i>Product Roadmaps Relaunched</i> (2017)."],
)

NOTES = [PROBLEM_STATEMENTS, OST, ASSUMPTIONS, OUTCOMES]
