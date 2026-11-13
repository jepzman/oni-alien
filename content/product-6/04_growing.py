# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 6 · Growing yourself.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 Product Sense
ps_problem = Doodle(760, 280, "Doodle of October 2027, a week after Antwerp opened. The dashboards say Antwerp is fine. Grace orders from Antwerp herself on Friday, as she does in every city, and notices what no number shows: the French swap message arrives as a cold one-liner, and the courier's first-name card says Ana in Dutch spelling. Noor asks: how do you notice these things?",
                    "The dashboards say Antwerp is fine. Grace orders herself and notices what no number shows.")
ps_problem.box(20, 40, 320, 90, "dashboards", "green", sub="“all fine”")
ps_problem.box(400, 40, 340, 90, "Grace's own order", "y", sub="a cold French message")
ps_problem.note(380, 200, "“how do you notice these things?”", "red", size=19)

ps_analogy = Doodle(760, 250, "Doodle of a chef's palate: trained by tasting everything, every day, including the competitors' food and their own dishes as a guest would eat them. Taste is a skill, practised, not a gift.",
                     "A chef's palate is trained: tasting everything, every day, as a guest would.")
ps_analogy.icon("plate", 40, 60, 1.3)
for i, (t, f) in enumerate([("taste daily", "y"), ("as a guest", "blue"), ("others' food", "green")]):
    ps_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
ps_analogy.note(450, 200, "a skill, practised", "pen")

ps_how = Doodle(760, 400, "Grace's product sense habits, written down for Noor and the new product owner, 25 October 2027. Use the product as a customer: an order every week, in a different city. Work a shift: picking at a store every month, an hour on support every month. Look at others: one competitor's app teardown a month with the trio. Read raw signals: ten support tickets and two interview notes a week. Ask why behind every number. And write down predictions before tests, then check them: her hit rate is about 60 percent.",
                 "Use it, work a shift, study others, read raw signals, ask why, predict and check. A skill, practised.")
for i, (t, s, f) in enumerate([("use it", "an order a week", "y"), ("work a shift", "store + support monthly", "blue"), ("study others", "a teardown a month", "green"),
                               ("raw signals", "10 tickets a week", "paper"), ("ask why", "behind every number", "y"), ("predict", "then check: ≈ 60 %", "pink")]):
    r, c = divmod(i, 3)
    ps_how.box(14 + c * 248, 14 + r * 104, 236, 92, t, f, sub=s, size=17, subsize=13)
ps_how.note(380, 256, "Antwerp message rewritten by Monday", "green", size=16)
ps_how.note(380, 290, "Noor and Jonas start the same habits", "pen", size=16)

SENSE = dict(
    slug="product-sense",
    kicker="a.k.a. “the chef's palate”",
    tldr="<b>Product sense</b> is the judgment that notices what matters before the data does: what feels wrong to a customer, what's missing, what would delight. It isn't a gift; it's <b>trained</b>: use your product as a customer, work shifts beside the people who run it, study other products, read raw signals (tickets, interviews), ask why behind numbers, and <b>write predictions</b> before tests so you learn where your judgment is good.",
    chips=[("Family", "growing yourself"), ("Origin", "product practice (e.g. Shreyas Doshi, Julie Zhuo)"), ("Lives in", "weekly habits, written down"), ("Pairs with", "customer interviews, support tickets as data, feedback loops with operations")],
    problem_side="Larder, 25 October 2027",
    problem="""  <p class="lead">A week after <b>Antwerp</b> opened, the dashboards say all is fine. Grace orders from Antwerp herself on Friday, as she does in every city, and notices what no number shows: the French swap message arrives as a <b>cold one-liner</b>, and the courier card uses a Dutch spelling. Noor asks: <span class="hl-pink">how do you notice these things?</span></p>
  <ul>
    <li>Dashboards show what was measured, not what feels wrong.</li>
    <li>Product people can drift away from the product.</li>
    <li>Judgment that isn't trained or checked stays vague.</li>
  </ul>""",
    problem_figs=[ps_problem],
    analogy_side="the chef's palate",
    analogy="""  <p>A chef's <b>palate</b> isn't a gift. It's trained by <b>tasting everything, every day</b>: their own dishes <b>as a guest would</b> eat them, the competitors' food, ingredients on their own. Over years they taste the missing salt before anyone complains.</p>""",
    analogy_figs=[ps_analogy],
    map=[("Tasting daily", "An order a week, in a different city"),
         ("As a guest would", "Using the app as a customer, not a tester"),
         ("Competitors' food", "A monthly app teardown"),
         ("The missing salt", "The cold French swap message"),
         ("Years of tasting", "Habits kept since 2025")],
    how_side="habits, written down and checked",
    how="""  <p>Grace wrote down her habits for Noor and the new product owner. <b>Use it</b>: an order every week, in a different city. <b>Work a shift</b>: picking at a store and an hour on support, monthly. <b>Study others</b>: a competitor teardown a month with the trio. <b>Raw signals</b>: ten tickets and two interview notes a week. <b>Ask why</b> behind every number. <b>Predict</b> before tests, then check: her hit rate is about <b>60 %</b>, which is why she still tests. The Antwerp message was rewritten by Monday.</p>""",
    how_figs=[ps_how],
    steps=[("Use the product as a customer", "Every week, the real way."),
           ("Work beside operations", "A shift a month."),
           ("Study other products", "A teardown with the team."),
           ("Read raw signals", "Tickets, interviews, store feedback."),
           ("Ask why behind numbers", "Then go and look."),
           ("Predict, then check", "Write it down before every test.")],
    vocab=[("Product sense", "Trained judgment about what makes a product good."),
           ("Dogfooding", "Using your own product for real."),
           ("Teardown", "Studying another product in detail."),
           ("Prediction log", "Written guesses before tests, checked after."),
           ("Calibration", "Knowing how often your judgment is right."),
           ("Taste", "A sense of quality, shared by a team.")],
    code=dict(file="product/habits.md", note="Grace's habits, October 2027", plain=True, src="""
# Product sense habits · Grace · shared with Noor and Jonas

Weekly    order as a customer (rotate cities: AMS, RTM, UTR, DH, ANT) · 10 support tickets ·
          2 interview notes · one "why?" behind a number, followed up in person
Monthly   picking shift at a store (2 h) · 1 h on support with Sam's team ·
          competitor app teardown with the trio (what, why, would we?)
Every test   prediction written first (result, size, confidence) → checked after
             2026–27: 31 predictions, 19 right on direction (≈ 60 %)
Antwerp, 22 Oct   French swap message rewritten (native writer) by Mon 25 Oct
"""),
    tools="tools: the product itself, store shifts, the support queue, a teardown template, a prediction log.",
    gains=["<b>Problems seen</b> before the data.",
           "<b>Better ideas</b> from first-hand experience.",
           "<b>Calibrated judgment</b>: know when to trust it.",
           "<b>Teachable</b> to others.",
           "<b>Closer to customers</b> and operations."],
    losses=["<b>Hours every week</b>.",
            "<b>One person's experience</b> isn't data.",
            "<b>Overconfidence</b> without checking.",
            "<b>Hard to measure</b>."],
    baseline="Each line compares <b>relying on dashboards and instinct</b> to <b>trained habits: using the product, working shifts, studying others, reading raw signals and checking predictions</b>.",
    ratings=[(2, 5, "Antwerp customers got a warmer message within days."),
             (3, 4, "Small fixes that numbers missed."),
             (2, 4, "Predictions checked against tests."),
             (2, 4, "Problems noticed on day four, not month two."),
             (3, 4, "Better instincts about what to try."),
             (2, 4, "Noor and Jonas learn the same habits."),
             (3, 3, "Neutral."),
             (3, 4, "Small fixes, fast."),
             (3, 3, "A few hours a week.")],
    pitfalls=[("Only dashboards", "Never using the product.", "order every week."),
              ("Anecdote as data", "“I saw it once.”", "check with data before big changes."),
              ("Never checking", "Always “right”.", "a prediction log."),
              ("Only your own product", "No outside view.", "teardowns of others.")],
    use=["Every product person, always.",
         "After launches in new places.",
         "Training new product people.",
         "When the team seems far from customers."],
    skip=["Never."],
    related=["<b>Customer interviews</b> (Vol. 1)", "<b>Support tickets as data</b> (Vol. 4)", "<b>Feedback loops with operations</b> (Vol. 4)", "<b>Localisation for a new country</b> (this volume)"],
    quiz=[("Is product sense a gift?", "No: it's trained by habits."),
          ("What did Grace's own order find?", "A cold French swap message in Antwerp."),
          ("Why write predictions down?", "To learn how often your judgment is right (about 60 % for Grace)."),
          ("Name three habits.", "Order weekly, work a shift monthly, read ten tickets a week.")],
    try_it="This week, order (or use) your product as a real customer, read ten support tickets, and write one prediction before your next test. Note one thing you noticed that no dashboard shows.",
    remember="Train the <span class=\"hl\">palate</span>: taste every day, as a <span class=\"hl\">guest</span> would.",
    sources=["Julie Zhuo, “The Making of a Product Sense” and <i>The Making of a Manager</i> (2019).",
             "Shreyas Doshi, writing on product sense (2020s).",
             "Philip Tetlock and Dan Gardner, <i>Superforecasting</i> (2015).",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021)."],
)

# ------------------------------------------------------------------ 13 Growing as a Product Owner
gp_problem = Doodle(760, 280, "Doodle of November 2027. Grace has been at Larder for two years. Her area has grown from one problem to three teams, a platform, business customers and Larder Plus. She's busy every day, but she can't say what she has got better at, what she hasn't, or what she wants next. Priya asks where she wants to be in a year.",
                    "Two years, an area that grew fivefold, and no clear answer to “where do you want to be in a year?”")
gp_problem.box(20, 40, 320, 90, "Oct 2025", "paper", sub="one problem: swaps")
gp_problem.box(400, 40, 340, 90, "Nov 2027", "y", sub="3 teams · platform · B2B · Plus")
gp_problem.note(380, 200, "busy every day, growing how?", "red", size=20)

gp_analogy = Doodle(760, 250, "Doodle of a climber reviewing a season: the routes climbed, what went well, where she fell, what her partners noticed, and the two skills to train next season. Not more climbing; better climbing.",
                     "A climber's season review: routes, falls, what partners noticed, two skills for next season.")
gp_analogy.icon("pyramid", 40, 60, 1.3)
for i, (t, f) in enumerate([("routes", "y"), ("falls", "pink"), ("partners", "blue"), ("two skills", "green")]):
    gp_analogy.box(150 + i * 150, 70, 138, 60, t, f, size=15)
gp_analogy.note(450, 200, "not more climbing; better climbing", "pen")

gp_how = Doodle(760, 400, "Grace's two-year review, 8 November 2027. Look back: the decisions she's proud of and the ones she'd redo, from her notebooks. Ask for feedback: six questions to Priya, Ben, Noor, Mo, Joost and Ana. Strengths they named: discovery, numbers, keeping promises honest. Growth areas: delegating, saying no to Femke sooner, writing strategy beyond a quarter. Choose two for the next year: hire and grow a product owner; write the 2028 strategy for ordering. Agree them with Priya, with a check-in every quarter.",
                 "Look back, ask six people, choose two things to grow, agree them with your manager.")
gp_how.box(14, 14, 236, 100, "look back", "paper", sub="proud of · would redo", size=17, subsize=13)
gp_how.box(262, 14, 236, 100, "ask 6 people", "blue", sub="Priya, Ben, Noor, Mo, Joost, Ana", size=17, subsize=12)
gp_how.box(510, 14, 236, 100, "choose 2", "green", sub="for the next year", size=17, subsize=13)
gp_how.box(14, 136, 360, 100, None, "y")
gp_how.head(194, 166, "strengths", size=16)
gp_how.text(194, 196, "discovery · numbers", size=14)
gp_how.text(194, 222, "honest promises", size=14)
gp_how.box(386, 136, 360, 100, None, "pink")
gp_how.head(566, 166, "to grow", size=16)
gp_how.text(566, 196, "delegating · saying no sooner", size=14)
gp_how.text(566, 222, "strategy beyond a quarter", size=14)
gp_how.box(14, 256, 732, 56, "next year: hire + grow a PO · write the 2028 strategy", "green", size=15)
gp_how.note(380, 350, "agreed with Priya · checked every quarter", "pen", size=16)

GROWING = dict(
    slug="growing-as-po",
    kicker="a.k.a. “the climber's season review”",
    tldr="Product owners are busy enough to stop growing without noticing. Once a year, <b>look back</b> at decisions you're proud of and ones you'd redo, <b>ask the people around you</b> a few specific questions, name your <b>strengths and growth areas</b>, and <b>choose two things</b> to get better at, with your manager's support and a quarterly check-in. Growth comes from choosing, not from being busy.",
    chips=[("Family", "growing yourself"), ("Origin", "career development practice; after-action reviews applied to yourself"), ("Lives in", "a yearly review, your notebooks and quarterly check-ins"), ("Pairs with", "managing up, product sense, hiring a product owner")],
    problem_side="Larder, 8 November 2027",
    problem="""  <p class="lead">Grace has been at Larder for <b>two years</b>. Her area has grown from <b>one problem</b> (swaps) to three teams, a platform, business customers and Larder Plus. She's busy every day, but she can't say what she's got better at, what she hasn't, or what she wants next. Priya asks: <span class="hl-pink">where do you want to be in a year?</span></p>
  <ul>
    <li>Busy isn't the same as growing.</li>
    <li>Blind spots need other people's eyes.</li>
    <li>Without a choice, growth is accidental.</li>
  </ul>""",
    problem_figs=[gp_problem],
    analogy_side="the climber's season review",
    analogy="""  <p>At the end of a season a climber reviews it: the <b>routes</b> climbed, what went well, where she <b>fell</b>, what her <b>partners</b> noticed, and <b>two skills</b> to train next season. Not more climbing; better climbing.</p>""",
    analogy_figs=[gp_analogy],
    map=[("The routes climbed", "Two years of decisions in Grace's notebooks"),
         ("Where she fell", "Decisions she'd redo"),
         ("What partners noticed", "Feedback from six colleagues"),
         ("Two skills to train", "Hiring a PO; writing the 2028 strategy"),
         ("The coach", "Priya, with a quarterly check-in")],
    how_side="look back, ask, choose two",
    how="""  <p>Grace <b>looked back</b> through her notebooks: decisions she's proud of, ones she'd redo. She <b>asked six people</b> (Priya, Ben, Noor, Mo, Joost, Ana) three questions each. <b>Strengths</b> they named: discovery, numbers, keeping promises honest. <b>Growth areas</b>: delegating, saying no to Femke sooner, strategy beyond a quarter. She <b>chose two</b> for the next year: <b>hire and grow a product owner</b>, and <b>write the 2028 strategy</b> for ordering. Agreed with Priya, checked every quarter.</p>""",
    how_figs=[gp_how],
    steps=[("Look back with evidence", "Notebooks, decisions, results."),
           ("Ask specific questions", "What should I keep, start, stop?"),
           ("Name strengths and gaps", "In the words people used."),
           ("Choose two", "Not ten; two you'll really work on."),
           ("Make them concrete", "A project, a habit, a mentor."),
           ("Agree with your manager", "And check in quarterly.")],
    vocab=[("Retrospective", "Looking back to learn, here on yourself."),
           ("360 feedback", "Feedback from people around you, not just your manager."),
           ("Growth area", "A skill to get better at."),
           ("Development plan", "What you'll learn, how, by when."),
           ("Mentor", "Someone experienced who advises you."),
           ("Stretch assignment", "Work slightly beyond your current skill.")],
    code=dict(file="personal/2027-review.md", note="Grace's two-year review, November 2027", plain=True, src="""
# Two years at Larder · Grace · 8 Nov 2027

Proud of      concierge test before building (2025) · bets not promises (2026) ·
              telling Femke early about 2.4 % (2026) · city playbook (2027)
Would redo    slot waitlist (built for one city's launch) · waiting a week to tell Priya about the guardrail
Asked         Priya, Ben, Noor, Mo, Joost, Ana: keep / start / stop?
Strengths     discovery · numbers · honest promises · calm in launches
Growth        delegating (Ben: "you still review every story") · saying no to Femke sooner ·
              strategy beyond the next quarter
Next year     1 hire and grow a product owner for Larder for Business (by Jan)
              2 write the 2028 ordering strategy (by Feb) · mentor: Priya, monthly
Check-ins     with Priya, first week of each quarter
"""),
    tools="tools: your notebooks, a few feedback questions, a one-page development plan, quarterly check-ins.",
    gains=["<b>Growth on purpose</b>.",
           "<b>Blind spots</b> found by others.",
           "<b>Clear asks</b> for your manager.",
           "<b>Better product work</b>, too.",
           "<b>A story</b> of your progress."],
    losses=["<b>Uncomfortable feedback</b>.",
            "<b>Time</b> for reflection.",
            "<b>Two things</b> means not ten.",
            "<b>Needs follow-through</b>."],
    baseline="Each line compares <b>being busy and hoping to grow</b> to <b>a yearly look back, feedback from six people, and two chosen growth areas agreed with your manager</b>.",
    ratings=[(3, 3, "Indirect."),
             (3, 4, "A hire and a strategy the business needs."),
             (2, 4, "Feedback from six people, not a feeling."),
             (3, 4, "Quarterly check-ins."),
             (2, 5, "Two growth areas, not ten."),
             (2, 4, "Priya knows exactly what Grace is working on."),
             (2, 4, "Colleagues see feedback taken seriously."),
             (3, 3, "Neutral."),
             (3, 4, "A day a year, an hour a quarter.")],
    pitfalls=[("Only your view", "Self-assessment alone.", "ask six people."),
              ("Vague questions", "“Any feedback?”", "keep, start, stop."),
              ("Ten goals", "Nothing changes.", "two."),
              ("No follow-up", "A plan in a drawer.", "quarterly check-ins.")],
    use=["Once a year, at least.",
         "When your role has grown.",
         "Before asking for a promotion or change.",
         "When you feel busy but stuck."],
    skip=["Never."],
    related=["<b>Managing up</b> (Vol. 5)", "<b>Product sense</b> (this volume)", "<b>Hiring a product owner</b> (this volume)", "<b>Post-launch review</b> (Vol. 4)"],
    quiz=[("What are the three steps?", "Look back, ask others, choose two things to grow."),
          ("What questions did Grace ask?", "Keep, start, stop."),
          ("What growth areas came up?", "Delegating, saying no to Femke sooner, longer-term strategy."),
          ("What did she choose?", "Hire and grow a product owner; write the 2028 strategy.")],
    try_it="Ask five people you work with: what should I keep doing, start doing, stop doing? Read your notes from the last year, then choose two things to get better at and tell your manager.",
    remember="Review the <span class=\"hl\">season</span>; train <span class=\"hl\">two skills</span>.",
    sources=["Marty Cagan, <i>Empowered</i> (2020), on coaching product people.",
             "Kim Scott, <i>Radical Candor</i> (2017).",
             "Sheila Heen and Douglas Stone, <i>Thanks for the Feedback</i> (2014).",
             "Herminia Ibarra, <i>Act Like a Leader, Think Like a Leader</i> (2015)."],
)

# ------------------------------------------------------------------ 14 Hiring a Product Owner
hp_problem = Doodle(760, 280, "Doodle of November 2027. Larder for Business needs its own product owner. Grace's first instinct is to copy a job ad and run the usual interviews: CV, a chat about frameworks, a case study about a famous app. Last year, a hire made that way talked well about frameworks and struggled with real customers.",
                    "The usual process: a copied ad, a framework chat, a famous-app case. Last time it hired a good talker.")
hp_problem.box(20, 40, 320, 90, "usual interviews", "paper", sub="frameworks · famous-app case")
hp_problem.box(400, 40, 340, 90, "last time", "pink", sub="talked well, struggled with customers")
hp_problem.note(380, 200, "testing talk, not the job", "red", size=20)

hp_analogy = Doodle(760, 250, "Doodle of a restaurant hiring a chef: not a chat about cooking theory but a trial shift, cooking two dishes from the real menu in the real kitchen, then tasting together and talking about what they'd change.",
                     "Hiring a chef: a trial shift in the real kitchen with the real menu, then tasting together.")
hp_analogy.icon("kitchen", 30, 60, 1.2)
hp_analogy.box(150, 50, 280, 100, "cooking theory", "pink", sub="a chat")
hp_analogy.box(460, 50, 280, 100, "a trial shift", "green", sub="the real menu")
hp_analogy.note(450, 210, "test the job, not the talk", "pen")

hp_how = Doodle(760, 400, "Grace's hiring process for the business product owner, from 22 November 2027. A scorecard first: judgment with customers, clear writing, comfort with numbers, working with sales without becoming sales. A work sample like the real job: ten anonymised Korenwolf-style requests to sort in two hours, with a one-page note. Interviews with the people they'll work with: Mo, Ben, Noor. One conversation with a real office manager, observed. Decision against the scorecard. Hired: Jonas, from a business-software company, starting 3 January 2028.",
                 "A scorecard, a work sample from the real job, the real colleagues, a real customer. Jonas starts 3 January.")
for i, (t, s, f) in enumerate([("scorecard", "4 qualities", "y"), ("work sample", "10 requests, 2 h", "blue"), ("colleagues", "Mo · Ben · Noor", "paper"), ("a real customer", "observed call", "green")]):
    hp_how.box(14 + i * 184, 14, 174, 100, t, f, sub=s, size=16, subsize=13)
hp_how.box(14, 136, 732, 56, "judgment · clear writing · numbers · sales without becoming sales", "paper", size=14)
hp_how.box(14, 212, 732, 60, "hired: Jonas · starts 3 January 2028", "green", size=17)
hp_how.note(380, 312, "decided against the scorecard, not the chat", "pen", size=16)

HIRING = dict(
    slug="hiring-a-po",
    kicker="a.k.a. “the trial shift”",
    tldr="Hiring a product owner by CV and conversation tests how well people <b>talk</b> about product work. Instead: write a <b>scorecard</b> of the few qualities the role needs, give a <b>work sample</b> that looks like the real job, let the <b>people they'll work with</b> interview, include a <b>real customer conversation</b> if you can, and decide against the scorecard. Treat candidates well: their time is real, too.",
    chips=[("Family", "growing yourself"), ("Origin", "structured hiring and work-sample tests (Schmidt and Hunter, 1998)"), ("Lives in", "a scorecard, a work sample and an interview plan"), ("Pairs with", "working with account managers, growing as a product owner, handing over")],
    problem_side="Larder, 22 November 2027",
    problem="""  <p class="lead">Larder for Business needs <b>its own product owner</b>. Grace's first instinct is the usual process: a copied job ad, a chat about frameworks, a case study about a famous app. <span class="hl-pink">Last year, a hire made that way talked well and struggled with real customers.</span></p>
  <ul>
    <li>Conversations test talking, not doing.</li>
    <li>Generic cases miss the role's real difficulties.</li>
    <li>Without a scorecard, the most likeable candidate wins.</li>
  </ul>""",
    problem_figs=[hp_problem],
    analogy_side="the trial shift",
    analogy="""  <p>A good restaurant doesn't hire a chef after a chat about cooking theory. It offers a <b>trial shift</b>: two dishes from the <b>real menu</b>, in the <b>real kitchen</b>, with the real team, then <b>tasting together</b> and talking about what they'd change. The kitchen learns more in two hours than in a week of interviews.</p>""",
    analogy_figs=[hp_analogy],
    map=[("Cooking theory", "A chat about product frameworks"),
         ("Two dishes from the real menu", "Ten Korenwolf-style requests in two hours"),
         ("The real kitchen team", "Interviews with Mo, Ben and Noor"),
         ("Tasting together", "Discussing the one-page note"),
         ("A real guest", "An observed call with an office manager")],
    how_side="scorecard, work sample, colleagues, a customer",
    how="""  <p>Grace wrote a <b>scorecard</b>: judgment with customers, clear writing, comfort with numbers, working with sales <b>without becoming sales</b>. The <b>work sample</b>: ten anonymised requests like Korenwolf's to sort in two hours, with a one-page note. <b>Interviews</b> with Mo, Ben and Noor. One <b>observed conversation</b> with a real office manager. The decision followed the scorecard. Hired: <b>Jonas</b>, from a business-software company, starting <b>3 January 2028</b>.</p>""",
    how_figs=[hp_how],
    steps=[("Write the scorecard", "Three to five qualities the role really needs."),
           ("Design a work sample", "A slice of the real job, two hours, paid if longer."),
           ("Involve future colleagues", "Each tests different qualities."),
           ("Add a real customer moment", "Observed, if possible."),
           ("Decide against the scorecard", "Together, with evidence."),
           ("Treat candidates well", "Clear steps, quick answers, feedback.")],
    vocab=[("Scorecard", "The qualities a role needs, written before interviewing."),
           ("Work sample", "A task like the real job."),
           ("Structured interview", "Same questions, scored the same way."),
           ("Bias", "Judging on things that don't predict the job."),
           ("Candidate experience", "How the process feels to applicants."),
           ("Onboarding", "Helping a new hire start well.")],
    code=dict(file="product/hiring/business-po.md", note="the hiring plan, November 2027", plain=True, src="""
# Hiring: product owner, Larder for Business · Grace · from 22 Nov 2027

Scorecard   1 judgment with business customers (needs vs requests)
            2 clear writing (one page, decisions with reasons)
            3 comfort with numbers (SLA %, cost per order, renewal health)
            4 works with sales without becoming sales
Steps       30-min call (Grace) → work sample (2 h, 10 anonymised requests + 1-page note)
            → interviews: Mo (4), Ben (1, 3), Noor (1, 2) → observed call with an office manager
Decision    scored per quality by each interviewer, discussed together · answer within 3 days
Hired       Jonas (from a business-software company) · starts 3 Jan 2028 · handover plan ready
"""),
    tools="tools: a scorecard, a realistic work sample, a structured interview plan, a debrief meeting.",
    gains=["<b>Hiring for the job</b>, not the talk.",
           "<b>Colleagues invested</b> in the hire.",
           "<b>Fairer decisions</b>.",
           "<b>Candidates see the real job</b>.",
           "<b>A better start</b>: the work sample shows gaps early."],
    losses=["<b>More preparation</b>.",
            "<b>Candidates' time</b>: keep it short.",
            "<b>Some good people</b> decline work samples.",
            "<b>Longer process</b>."],
    baseline="Each line compares <b>CV, framework chat and a generic case</b> to <b>a scorecard, a real work sample, future colleagues and a customer moment</b>.",
    ratings=[(3, 4, "Business customers get a PO tested with a customer."),
             (3, 4, "The right hire for Larder for Business."),
             (1, 5, "Decided on a work sample and a scorecard."),
             (3, 3, "Neutral."),
             (2, 4, "Four qualities, not twenty."),
             (2, 4, "Mo, Ben and Noor helped choose."),
             (2, 4, "Priya trusts the process."),
             (3, 3, "Neutral."),
             (3, 3, "More preparation than the usual way.")],
    pitfalls=[("Framework quizzes", "“Explain RICE.”", "a real slice of the job."),
              ("No scorecard", "The likeable one wins.", "qualities written first."),
              ("Only the manager", "Colleagues meet them on day one.", "future colleagues interview."),
              ("Long unpaid tasks", "A weekend of work.", "two hours, or paid.")],
    use=["Hiring any product role.",
         "When past hires talked well and struggled.",
         "Splitting a product area.",
         "Building a team's hiring habits."],
    skip=["Never; only the size of the process changes."],
    related=["<b>Growing as a product owner</b> (this volume)", "<b>Handing over a product area</b> (this volume)", "<b>Working with account managers</b> (Vol. 5)", "<b>Growing other architects</b> (Ana, book 1 vol. 6)"],
    quiz=[("What comes before interviews?", "A scorecard of the qualities the role needs."),
          ("What was the work sample?", "Ten anonymised business requests to sort in two hours, with a one-page note."),
          ("Who interviewed?", "Future colleagues: Mo, Ben and Noor."),
          ("Who was hired?", "Jonas, starting 3 January 2028.")],
    try_it="For the next role you hire for, write four qualities before reading a CV, and design a two-hour task taken from the real job. Ask two future colleagues to interview for one quality each.",
    remember="Offer a <span class=\"hl\">trial shift</span> with the <span class=\"hl\">real menu</span>.",
    sources=["Frank Schmidt and John Hunter, “The validity and utility of selection methods”, <i>Psychological Bulletin</i> (1998).",
             "Laszlo Bock, <i>Work Rules!</i> (2015).",
             "Geoff Smart and Randy Street, <i>Who</i> (2008), scorecards.",
             "Marty Cagan, <i>Empowered</i> (2020), hiring product people."],
)

# ------------------------------------------------------------------ 15 Handing Over a Product Area
hv_problem = Doodle(760, 280, "Doodle of December 2027. Jonas starts on 3 January to take over Larder for Business. Everything he needs lives in Grace's head and notebooks: why decisions were made, which promises Korenwolf heard, which bets are half-done, who to call. Grace is tempted to do a one-hour walkthrough and stay on every thread just in case.",
                    "Everything Jonas needs is in Grace's head. Tempting: a one-hour walkthrough, then stay on every thread.")
hv_problem.box(20, 40, 320, 90, "Grace's head", "y", sub="whys · promises · bets · people")
hv_problem.box(400, 40, 340, 90, "the temptation", "pink", sub="1-hour walkthrough · never let go")
hv_problem.note(380, 200, "too little, or never letting go", "red", size=19)

hv_analogy = Doodle(760, 250, "Doodle of a relay race's changeover: both runners in the zone at full speed for a few metres, the baton passed hand to hand, and then the first runner steps aside. Dropping it or running alongside both lose the race.",
                     "A relay changeover: run together for a few metres, pass the baton, then step aside.")
hv_analogy.icon("baton", 40, 60, 1.3)
for i, (t, f) in enumerate([("run together", "y"), ("pass the baton", "blue"), ("step aside", "green")]):
    hv_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
hv_analogy.note(450, 200, "neither drop it nor run alongside", "pen")

hv_how = Doodle(760, 400, "Grace's handover plan for Larder for Business, 13 December 2027. A state-of-the-product document: why the area exists, outcomes and numbers, open bets, decisions with reasons, promises made to clients, people. Introductions, in person, to Hanna and Ruben with Mo, and to Joost's morning crew. Two weeks of Jonas shadowing Grace; four weeks of Jonas leading with Grace as backup; then Grace steps out on 28 February 2028 and says so publicly. Jonas's first decision alone: the February request review with Mo.",
                 "A state-of-the-product doc, introductions, shadow, lead with backup, then step out, publicly.")
hv_how.box(14, 14, 732, 56, "state of the product: why · outcomes · bets · decisions · promises · people", "paper", size=13)
for i, (t, s, f) in enumerate([("introductions", "clients, ops", "y"), ("2 weeks", "Jonas shadows", "blue"), ("4 weeks", "Jonas leads", "blue"), ("28 Feb", "Grace steps out", "green")]):
    x = 14 + i * 184
    hv_how.box(x, 90, 174, 100, t, f, sub=s, size=16, subsize=12)
hv_how.box(14, 214, 732, 56, "announced publicly: Jonas owns Larder for Business", "green", size=15)
hv_how.note(380, 310, "Jonas's first decision alone: February request review", "pen", size=16)
hv_how.note(380, 344, "Grace: ordering, the apps, Plus, and the 2028 strategy", "green", size=15)

HANDOVER = dict(
    slug="handing-over",
    kicker="a.k.a. “the relay changeover”",
    tldr="Handing over a product area well means passing on the <b>why</b>, not just the backlog: a <b>state-of-the-product</b> document (purpose, outcomes, open bets, decisions with reasons, promises made, people), <b>introductions in person</b>, a period of <b>shadowing</b>, then the new owner <b>leading with you as backup</b>, and finally a clear, public <b>step out</b>. Hand over too little and they stumble; never let go and they never own it.",
    chips=[("Family", "growing yourself"), ("Origin", "transition planning; leadership hand-off practice"), ("Lives in", "a state-of-the-product document and a dated handover plan"), ("Pairs with", "hiring a product owner, handover to operations (Ana), writing product principles")],
    problem_side="Larder, 13 December 2027",
    problem="""  <p class="lead"><b>Jonas</b> starts on 3 January to take over <b>Larder for Business</b>. Everything he needs lives in Grace's head and notebooks: <b>why</b> decisions were made, which <b>promises</b> Korenwolf heard, which <b>bets</b> are half-done, <b>who to call</b>. Grace is tempted to do a one-hour walkthrough, and <span class="hl-pink">stay on every thread just in case</span>.</p>
  <ul>
    <li>Backlogs pass on what, not why.</li>
    <li>Promises made to clients get lost.</li>
    <li>A previous owner who never leaves keeps the new one from owning it.</li>
  </ul>""",
    problem_figs=[hv_problem],
    analogy_side="the relay changeover",
    analogy="""  <p>In a relay, both runners are in the changeover zone <b>at full speed</b> for a few metres, the <b>baton is passed hand to hand</b>, and then the first runner <b>steps aside</b>. Dropping the baton loses the race; so does the first runner trying to run alongside to the finish.</p>""",
    analogy_figs=[hv_analogy],
    map=[("The baton", "The why, the promises, the open bets"),
         ("Running together", "Two weeks of shadowing"),
         ("Hand to hand", "Introductions to Hanna, Ruben and Joost's crew"),
         ("Still in the zone", "Four weeks leading with Grace as backup"),
         ("Stepping aside", "28 February, announced publicly")],
    how_side="the why on paper, people in person, then step out",
    how="""  <p>Grace wrote a <b>state-of-the-product</b> document: why Larder for Business exists, outcomes and numbers, <b>open bets</b>, <b>decisions with reasons</b>, <b>promises made</b> to clients, people. She <b>introduced Jonas in person</b> to Hanna and Ruben (with Mo) and to Joost's morning crew. Two weeks of <b>shadowing</b>; four weeks of Jonas <b>leading with Grace as backup</b>; then Grace <b>stepped out on 28 February 2028</b> and said so publicly. Jonas's first decision alone: the February request review with Mo. Grace kept ordering, the apps, Plus, and the 2028 strategy.</p>""",
    how_figs=[hv_how],
    steps=[("Write the state of the product", "Why, outcomes, bets, decisions, promises, people."),
           ("Introduce people in person", "Clients, partners, operations."),
           ("Let them shadow", "A couple of weeks, in real meetings."),
           ("Let them lead, with you as backup", "Weeks, not months."),
           ("Step out, publicly", "A date, announced."),
           ("Stay available, not involved", "Questions welcome; decisions theirs.")],
    vocab=[("Handover", "Passing ownership to someone else."),
           ("State of the product", "A document of the product's why, numbers, bets and decisions."),
           ("Shadowing", "Joining someone's work to learn it."),
           ("Backup", "Available for help, not making the decisions."),
           ("Decision log", "Decisions with their reasons."),
           ("Stepping out", "Visibly giving up ownership.")],
    code=dict(file="product/business/handover.md", note="the handover plan, December 2027", plain=True, src="""
# Handover: Larder for Business · Grace → Jonas · plan 13 Dec 2027

State of the product (written, 12 pages max)
  why it exists · outcomes (SLA 99.0 %, 4 offices, renewal Dec 2027) · open bets
  (invite colleagues, budgets per cost centre) · decision log with reasons · promises made
  to Korenwolf (Monday reservations, portal changes until 16:00) · people and who to call
Introductions   Hanna + Ruben (with Mo), 10 Jan · Joost's 06:00 crew at Noord, 12 Jan · Cho, Eli
3–14 Jan        Jonas shadows Grace (request review, standups, Korenwolf monthly)
17 Jan–25 Feb   Jonas leads; Grace backup (weekly 30 min)
28 Feb 2028     Grace steps out; announced in the product update
Grace keeps     ordering, customer apps, Larder Plus, substitution platform, 2028 strategy
"""),
    tools="tools: a state-of-the-product document, the decision log, introductions, a dated plan, the product update for the announcement.",
    gains=["<b>The why survives</b> the handover.",
           "<b>Promises kept</b> to clients.",
           "<b>A confident new owner</b>.",
           "<b>Grace freed</b> for strategy.",
           "<b>Clear ownership</b> for everyone."],
    losses=["<b>Writing the document</b> takes days.",
            "<b>Letting go</b> is hard.",
            "<b>Some decisions</b> will differ from yours.",
            "<b>Weeks of overlap</b>."],
    baseline="Each line compares <b>a one-hour walkthrough, or never letting go</b> to <b>a written state of the product, introductions, shadowing, leading with backup and a public step-out</b>.",
    ratings=[(3, 4, "Office managers notice no gap."),
             (2, 4, "Korenwolf's promises carried over."),
             (2, 4, "Decisions passed on with their reasons."),
             (3, 3, "Neutral."),
             (2, 4, "Grace focuses on ordering and strategy."),
             (1, 5, "Jonas knows the why, not just the backlog."),
             (2, 5, "Hanna and Ruben met Jonas in person."),
             (3, 4, "No pause in delivery."),
             (3, 3, "Days of writing; weeks of overlap.")],
    pitfalls=[("Backlog only", "Tickets, no reasons.", "the why and the promises."),
              ("Email introductions", "Clients meet a name.", "in person."),
              ("Never letting go", "Grace on every thread.", "a public step-out date."),
              ("Disappearing", "Gone on day one.", "shadow, then backup.")],
    use=["Handing a product area to a new owner.",
         "Leaving a role or a company.",
         "Splitting a growing area.",
         "Parental leave and long absences (a temporary version)."],
    skip=["Never; only the length changes."],
    related=["<b>Hiring a product owner</b> (this volume)", "<b>Writing product principles</b> (this volume)", "<b>Handover to operations</b> (Ana, book 1 vol. 6)", "<b>Decision log</b> (Ana, book 1 vol. 2)"],
    quiz=[("What goes into the state-of-the-product document?", "Why, outcomes, open bets, decisions with reasons, promises made, people."),
          ("What are the phases?", "Shadowing, leading with backup, then a public step-out."),
          ("When did Grace step out?", "28 February 2028, announced in the product update."),
          ("What did Grace keep?", "Ordering, the customer apps, Plus, the substitution platform and the 2028 strategy.")],
    try_it="Write a one-page state of the product for your area: why it exists, the numbers, open bets, the three most important decisions with reasons, promises made, and who to call. Would someone else be able to own it next month?",
    remember="Pass the <span class=\"hl\">baton</span> hand to hand, then <span class=\"hl\">step aside</span>.",
    sources=["Michael Watkins, <i>The First 90 Days</i>, updated ed. (2013).",
             "Marty Cagan, <i>Empowered</i> (2020).",
             "Camille Fournier, <i>The Manager's Path</i> (2017).",
             "Will Larson, <i>An Elegant Puzzle</i> (2019)."],
)

NOTES = [SENSE, GROWING, HIRING, HANDOVER]
