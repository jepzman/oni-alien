# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 4 · Listening.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Support Tickets as Data
st_problem = Doodle(760, 280, "Doodle of June 2026. Sam's team handles about 900 tickets a week. Grace hears about them as anecdotes: an angry email forwarded, a story at lunch. The loudest complaint gets attention; the most common one doesn't. Sam's auto-refund button is up for review on 1 June, and nobody has the numbers to decide.",
                    "900 tickets a week, heard as anecdotes: the loudest one gets attention, the most common one doesn't.")
st_problem.icon("envelope", 40, 40, 1.4)
st_problem.box(150, 40, 270, 80, "900 tickets / week", "paper", sub="heard as stories")
st_problem.box(460, 30, 280, 100, "auto-refund button", "y", sub="review due 1 June · no numbers", subsize=14)
st_problem.note(380, 200, "the loudest complaint isn't the most common one", "red", size=18)

st_analogy = Doodle(760, 250, "Doodle of a family doctor's appointment book. Each visit gets a short, consistent reason. Read weekly, the book shows a pattern no single visit could: a rise in ear infections after the swimming pool reopened.",
                     "A doctor's appointment book, read weekly, shows what no single visit can: a pattern.")
st_analogy.icon("ledger", 40, 50, 1.5)
for i, (t, n, f) in enumerate([("colds", "31", "paper"), ("ear infections", "18 ↑", "pink"), ("back pain", "12", "paper")]):
    st_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=n)
st_analogy.note(450, 210, "the pool reopened: a pattern, not a story", "pen")

st_how = Doodle(760, 360, "Grace and Sam's weekly ticket review from 15 June 2026: top reasons per 1,000 orders, with the trend. Where is my order: 11.2, flat. Missing item: 6.4. Late delivery: 4.1. Swap refund: 3.4, down from 6.2 before approvals. Damaged item: 2.0. Consistent tags, checked by Sam's team; fifteen minutes on Mondays. Decisions it drove: the auto-refund button was closed, swap refunds having nearly halved; live order updates got a target from the top reason.",
                 "Top reasons per 1,000 orders, weekly, with the trend. Fifteen minutes, and two decisions in the first month.")
st_how.head(20, 32, "reason", anchor="start", size=15)
st_how.head(420, 32, "per 1,000 orders", anchor="start", size=15)
st_how.head(640, 32, "trend", anchor="start", size=15)
for i, (r, n, t, f) in enumerate([("where is my order?", "11.2", "flat", "pink"), ("missing item", "6.4", "↓", "paper"), ("late delivery", "4.1", "↑", "y"),
                                  ("swap refund", "3.4", "↓↓ (6.2)", "green"), ("damaged item", "2.0", "flat", "paper")]):
    y = 46 + i * 46
    st_how.box(12, y, 736, 38, None, f, rx=4)
    st_how.text(20, y + 25, r, "t-head", anchor="start", size=14)
    st_how.text(420, y + 25, n, anchor="start", size=15)
    st_how.text(640, y + 25, t, anchor="start", size=14)
st_how.note(380, 300, "→ auto-refund button closed · live updates targeted at #1", "green", size=15)
st_how.note(380, 330, "Mondays, 15 minutes, Grace + Sam", "pen", size=15)

TICKETS = dict(
    slug="support-tickets-data",
    kicker="a.k.a. “the doctor's appointment book”",
    tldr="Support tickets are the largest, cheapest stream of customer pain you have, if you read them as <b>data</b>, not anecdotes. Agree <b>consistent reason tags</b> with support, check them, and review the <b>top reasons per 1,000 orders</b> (normalised, so growth doesn't fool you) <b>every week</b>, with the trend. Use it to pick problems, set targets and close requests, and keep reading a few actual tickets for the “why”.",
    chips=[("Family", "listening"), ("Origin", "customer support analytics; voice-of-the-customer practice"), ("Lives in", "the helpdesk's tags and a weekly review with the support lead"), ("Pairs with", "baseline before you build, funnels, feedback loops with operations")],
    problem_side="Larder, 15 June 2026",
    problem="""  <p class="lead">Sam's team handles about <b>900 tickets a week</b>. Grace hears about them as <b>anecdotes</b>: an angry email forwarded by Femke, a story over lunch. The loudest complaint gets attention; <span class="hl-pink">the most common one doesn't</span>. Sam's auto-refund button (parked in March) is up for review, and nobody has the numbers to decide it.</p>
  <ul>
    <li>Anecdotes favour vivid stories over frequent ones.</li>
    <li>Raw counts rise with orders, hiding whether things improve.</li>
    <li>Support's knowledge stays in support.</li>
  </ul>""",
    problem_figs=[st_problem],
    analogy_side="the doctor's appointment book",
    analogy="""  <p>A family doctor writes a short, <b>consistent reason</b> next to each appointment. Read <b>weekly</b>, the book shows what no single visit can: a rise in <b>ear infections</b> after the swimming pool reopened. The doctor still listens to every patient; the book shows where to look.</p>""",
    analogy_figs=[st_analogy],
    map=[("The reason next to each visit", "A consistent tag on each ticket"),
         ("Reading the book weekly", "The Monday review with Sam"),
         ("Visits per thousand patients", "Tickets per 1,000 orders"),
         ("The pool reopened", "“Where is my order?” as the top reason"),
         ("Still listening to each patient", "Reading a sample of real tickets")],
    how_side="tags, per 1,000, weekly, with the trend",
    how="""  <p>Sam's team already used the tag rule from the baseline work in Vol. 1. Grace and Sam added a <b>weekly review</b>: the top five reasons <b>per 1,000 orders</b>, with the trend, fifteen minutes on Mondays. It paid off at once: <b>swap refunds</b> had nearly halved (6.2 → 3.4), so the <b>auto-refund button was closed</b> with Sam's agreement; and <b>“where is my order?”</b> at 11.2 per 1,000 became the target for live updates.</p>""",
    how_figs=[st_how],
    steps=[("Agree reason tags", "Ten to fifteen, mutually exclusive, with examples; one per ticket."),
           ("Check the tagging", "Sam's team re-checks a sample monthly (the baseline found 38 % wrong once)."),
           ("Normalise", "Per 1,000 orders, so growth doesn't hide improvement."),
           ("Review weekly", "Top five reasons, trend, fifteen minutes, with the support lead."),
           ("Read real tickets too", "Ten a week from the top reason, for the why."),
           ("Act and close the loop", "Decisions go back to support: “you said, we did”.")],
    vocab=[("Ticket reason", "The tag saying why the customer contacted support."),
           ("Normalised rate", "Tickets per 1,000 orders, comparable over time."),
           ("Voice of the customer", "Customer feedback gathered and used systematically."),
           ("Contact rate", "Tickets per order: how often customers need help."),
           ("Tag drift", "Tags used inconsistently over time."),
           ("Closing the loop", "Telling support what changed because of their data.")],
    code=dict(file="product/support/weekly-review.md", note="the weekly ticket review, week of 15 June 2026", plain=True, src="""
# Ticket review · week 24 · Grace + Sam · per 1,000 orders (all cities)

| Reason              | This week | 4-wk trend | Note                                   |
|---------------------|-----------|------------|----------------------------------------|
| Where is my order?  | 11.2      | flat       | → live order updates (bet 3), target −30 % |
| Missing item        | 6.4       | ↓          | partly swaps defaulted; see funnel      |
| Late delivery       | 4.1       | ↑          | Rotterdam (on time 84 %) → Ana, routing |
| Swap refund         | 3.4       | ↓↓         | was 6.2 before approvals                |
| Damaged item        | 2.0       | flat       |                                        |
Contact rate 31 per 1,000 orders (was 38 in April)

Decisions  R-22 auto-refund button: CLOSED (swap refunds −45 %); Sam agrees
           live updates: KR "where is my order?" −30 % in Q3
"""),
    tools="tools: helpdesk tags and reporting (Zendesk, Intercom, Freshdesk), exported to the warehouse; a weekly report; optional text classification once tags are stable.",
    gains=["<b>Frequent pain over loud pain</b>.",
           "<b>Cheap, large, continuous</b> customer signal.",
           "<b>Targets set</b> from real numbers.",
           "<b>Requests closed</b> with evidence.",
           "<b>Support's knowledge</b> reaches the product."],
    losses=["<b>Tags need discipline</b>.",
            "<b>Only customers who complain</b> are counted.",
            "<b>Numbers lack the why</b> without reading tickets.",
            "<b>A weekly habit</b> to keep."],
    baseline="Each line compares <b>hearing about tickets as forwarded anecdotes</b> to <b>a weekly review of tagged reasons per 1,000 orders, with trends, plus a sample of real tickets</b>.",
    ratings=[(2, 5, "The most common pains get fixed first."),
             (2, 4, "Ticket costs fall where it matters."),
             (2, 5, "Normalised, checked, weekly numbers."),
             (2, 4, "Changes show up within a week or two."),
             (2, 4, "One top reason becomes one target."),
             (2, 4, "Support and product read the same table."),
             (2, 5, "Sam sees his team's data drive decisions."),
             (3, 3, "Neutral."),
             (3, 4, "Fifteen minutes a week.")],
    pitfalls=[("Raw counts", "Tickets up 20 %: panic.", "per 1,000 orders."),
              ("Messy tags", "Twenty overlapping reasons.", "few, exclusive, with examples; check a sample monthly."),
              ("Numbers only", "Nobody reads a ticket.", "ten real tickets a week from the top reason."),
              ("One-way flow", "Support never hears what changed.", "“you said, we did” back to support.")],
    use=["Any product with a support team.",
         "Choosing which problem to tackle next.",
         "Checking whether a launch reduced contacts.",
         "Closing or confirming feature requests from support."],
    skip=["Very low ticket volumes: read them all instead."],
    related=["<b>Baseline before you build</b> (Vol. 1)", "<b>Feedback loops with operations</b> (this volume)", "<b>Feature request triage</b> (Vol. 2)", "<b>OKRs</b> (this volume)"],
    quiz=[("Why normalise tickets per 1,000 orders?", "So growth in orders doesn't hide whether things are improving."),
          ("What decision did the first review drive?", "Closing the auto-refund button: swap refunds had nearly halved."),
          ("What's still needed beyond the numbers?", "Reading a sample of real tickets for the why."),
          ("What was the top reason?", "“Where is my order?”, 11.2 per 1,000 orders.")],
    try_it="Ask your support lead for last month's tickets by reason. Turn them into rates per 1,000 orders and a four-week trend. Read ten tickets from the top reason, then decide one thing to do about it and tell support.",
    remember="Read the <span class=\"hl\">appointment book</span> weekly, and still listen to each <span class=\"hl\">patient</span>.",
    sources=["Bill Price and David Jaffe, <i>The Best Service is No Service</i> (2008).",
             "Zendesk, “Customer service metrics” guides.",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021), on mining existing data.",
             "Gerry McGovern, <i>Top Tasks</i> (2018)."],
)

# ------------------------------------------------------------------ 10 Feedback Loops with Operations
op_problem = Doodle(760, 280, "Doodle of July 2026. Customers accept only 71 percent of substitutes. Pickers at Noord know why: the handheld lists suggestions by price, so the first one is often a strange choice. They've grumbled about it for weeks, but only to each other. Nobody asked them, and there was no easy way to tell the team.",
                    "Pickers knew why customers refuse swaps. They grumbled to each other; nobody asked them.")
op_problem.box(20, 40, 320, 100, "handheld suggestions", "y", sub="sorted by price")
op_problem.box(420, 40, 320, 100, "pickers", "paper", sub="“the first one is daft”")
op_problem.box(160, 170, 440, 60, "customers accept 71 %", "pink", stroke="red", size=16)
op_problem.note(380, 262, "the knowledge was in the store, not in the team", "red")

op_analogy = Doodle(760, 250, "Doodle of a theatre's stage crew noticebook backstage: crew write down anything that slows the show, a sticking door, a dim light. The stage manager reads it daily and writes back what's fixed. Crew keep writing because things get fixed.",
                     "A backstage noticebook: the crew write what slows the show; the stage manager writes back what's fixed.")
op_analogy.icon("ledger", 40, 50, 1.4)
op_analogy.box(160, 50, 280, 100, "crew write", "y", sub="“door sticks, scene 3”")
op_analogy.box(470, 50, 270, 100, "manager writes back", "green", sub="“fixed Tuesday”")
op_analogy.note(450, 210, "people keep writing when things get fixed", "pen")

op_how = Doodle(760, 360, "Larder's loop with operations from 20 July 2026. An idea button on the handhelds: one tap, a photo or a sentence. Every other week, twenty minutes at Noord and Rotterdam with the store manager and two pickers, in the store. A you said, we did note on the store notice board. In three weeks: 14 items; the top one, sort suggestions by similarity not price, shipped on 3 August: customers accepting substitutes rose from 71 to 78 percent.",
                 "An easy way in, a regular visit, and answers going back. Fourteen items in three weeks; one of them moved acceptance 71 → 78 %.")
for i, (t, s, f) in enumerate([("idea button", "on the handheld", "y"), ("20 min, fortnightly", "in the store", "blue"), ("“you said, we did”", "store notice board", "green")]):
    op_how.box(14 + i * 248, 20, 236, 90, t, f, sub=s, size=16)
op_how.box(14, 140, 732, 110, None, "paper")
op_how.head(380, 172, "top item: sort suggestions by similarity, not price", size=15)
op_how.text(380, 206, "shipped 3 Aug · Noord + Rotterdam", size=15)
op_how.text(380, 234, "swaps accepted: 71 % → 78 %", "t-head", size=16)
op_how.note(380, 290, "14 items in 3 weeks · 9 done or answered", "pen", size=16)
op_how.note(380, 320, "Tomás: “first time anyone wrote back”", "green", size=16)

OPS = dict(
    slug="operations-feedback",
    kicker="a.k.a. “the backstage noticebook”",
    tldr="The people who operate your product every day (pickers, couriers, store staff) see problems long before dashboards do. Build a <b>feedback loop</b>: an <b>easy way in</b> (a button on the device they already use), a <b>regular visit</b> where they work, and <b>answers going back</b> (“you said, we did”). Without the way back, people stop telling you; with it, they become your best early-warning system.",
    chips=[("Family", "listening"), ("Origin", "lean “go and see” (genchi genbutsu); service design practice"), ("Lives in", "the handheld app, a fortnightly store visit and a notice board"), ("Pairs with", "the product trio, support tickets as data, operations as a customer")],
    problem_side="Larder, 20 July 2026",
    problem="""  <p class="lead">With answers at 88 %, the next question is why customers accept only <b>71 %</b> of substitutes. Pickers at Noord know: the handheld lists suggestions <b>by price</b>, so the first one is often a strange choice (oat milk for whole milk, the cheapest bread for sourdough). They've grumbled about it for weeks, <span class="hl-pink">but only to each other</span>. Nobody asked, and there was no easy way to tell the team.</p>
  <ul>
    <li>Operations staff see problems first and have the least time to report them.</li>
    <li>Feedback without answers dries up.</li>
    <li>Occasional visits catch what's visible that day, not patterns.</li>
  </ul>""",
    problem_figs=[op_problem],
    analogy_side="the backstage noticebook",
    analogy="""  <p>Backstage, a theatre keeps a <b>noticebook</b>: crew write anything that slows the show (a sticking door, a dim light). The stage manager reads it daily and <b>writes back</b> what's fixed and when. The crew keep writing <b>because things get fixed</b>; a noticebook nobody answers is empty within a month.</p>""",
    analogy_figs=[op_analogy],
    map=[("The noticebook", "The idea button on the handheld"),
         ("The crew", "Pickers and store staff"),
         ("The stage manager reading it", "Grace and the trio, fortnightly in the store"),
         ("Writing back", "“You said, we did” on the store notice board"),
         ("The sticking door", "Suggestions sorted by price")],
    how_side="easy in, regular visits, answers back",
    how="""  <p>Dee added an <b>idea button</b> to the handheld: one tap, a sentence or a photo. Every other week the trio spends <b>twenty minutes in the store</b> with the manager and two pickers. Answers go on the <b>notice board</b>: “you said, we did”. In three weeks: <b>14 items</b>. The top one, <b>sort suggestions by similarity</b>, shipped on 3 August, and customers accepting substitutes rose from <b>71 % to 78 %</b>. Tomás: “first time anyone wrote back.”</p>""",
    how_figs=[op_how],
    steps=[("Make it easy", "A button on the device they use; one tap, a sentence or photo."),
           ("Go to where the work is", "Fortnightly, short, in the store, at a busy time."),
           ("Triage like any request", "Joins an opportunity, quick fix, parked, declined."),
           ("Write back, visibly", "“You said, we did” where they'll see it."),
           ("Measure the effect", "Pick the metric the fix should move."),
           ("Thank by name", "Credit the picker whose idea shipped.")],
    vocab=[("Feedback loop", "A regular way in, and a way back."),
           ("Go and see", "Visiting the place where the work happens."),
           ("Front line", "The people doing the operational work."),
           ("You said, we did", "Visible answers to feedback."),
           ("Acceptance rate", "The share of substitutes customers accept."),
           ("Operations as a customer", "Treating internal users as customers of the product.")],
    code=dict(file="product/operations/feedback-loop.md", note="the loop with operations, from 20 July 2026", plain=True, src="""
# Feedback loop with operations · Noord + Rotterdam            owner: Grace (with the trio)

Way in      idea button on the handheld (text or photo) → triage list
Visits      every other Tuesday 17:00–17:20, in the store, manager + 2 pickers
Way back    "You said, we did" sheet on the store notice board, updated after each visit

First 3 weeks (20 Jul – 7 Aug): 14 items
  #1  Sort swap suggestions by similarity, not price   shipped 3 Aug
      → swaps accepted 71 % → 78 % (Noord + Rotterdam, 4 weeks after)
  #2  Bigger font for allergen warning                 shipped 10 Aug
  #3  Scanner beeps twice on substitutes               declined: confuses packing (answered)
  ... 9 of 14 done or answered by 7 Aug
"""),
    tools="tools: an in-app feedback button (or a shared form), the request triage list, a printed sheet for the store board; a fortnightly calendar slot.",
    gains=["<b>Problems found early</b>, by those who see them.",
           "<b>Real fixes</b>: 71 → 78 % accepted.",
           "<b>Trust with operations</b>.",
           "<b>Cheap</b>: a button and twenty minutes.",
           "<b>Better designs</b> from people doing the work."],
    losses=["<b>A habit to keep</b>.",
            "<b>Raised expectations</b> if answers stop.",
            "<b>Noise</b> mixed with gold.",
            "<b>Store time</b> during busy hours."],
    baseline="Each line compares <b>operations feedback heard occasionally, if at all</b> to <b>an easy way in, fortnightly visits, and visible answers going back</b>.",
    ratings=[(2, 4, "Customers get better substitutes."),
             (2, 4, "Acceptance up seven points."),
             (2, 4, "Front-line knowledge, measured after the fix."),
             (2, 4, "Problems reported the day pickers see them."),
             (3, 3, "Neutral."),
             (2, 4, "The team sees the store's view."),
             (1, 5, "Pickers see their ideas shipped."),
             (3, 3, "Neutral."),
             (3, 3, "A button and twenty minutes a fortnight.")],
    pitfalls=[("No way back", "Ideas vanish; people stop sending them.", "“you said, we did”, visibly, every time."),
              ("Hard way in", "A form on a laptop pickers never use.", "a button on the device they hold."),
              ("Visits at quiet times", "Nothing to see at 11:00.", "go at peak."),
              ("Only the manager", "Pickers' view filtered.", "talk to pickers directly.")],
    use=["Products used by operations staff.",
         "When metrics drop and nobody knows why.",
         "Any feature that changes someone's daily work.",
         "Building trust with operations."],
    skip=["Products with no operational users."],
    related=["<b>Support tickets as data</b> (this volume)", "<b>The product trio</b> (Vol. 3)", "<b>Operations as a customer</b> (Vol. 5)", "<b>Feature request triage</b> (Vol. 2)"],
    quiz=[("What are the three parts of the loop?", "An easy way in, regular visits where the work is, answers going back."),
          ("Why does the way back matter?", "Without answers, people stop giving feedback."),
          ("What did the top item change?", "Suggestions sorted by similarity; acceptance rose from 71 % to 78 %."),
          ("When should you visit?", "At busy times, when the work is happening.")],
    try_it="Add the simplest possible feedback route for the people who operate your product, and visit them for twenty minutes at their busiest time. Answer every item within two weeks in a place they'll see, and track one metric for the first fix.",
    remember="Keep a <span class=\"hl\">noticebook</span> backstage, and always <span class=\"hl\">write back</span>.",
    sources=["Taiichi Ohno, <i>Toyota Production System</i> (1988), go and see.",
             "Marc Stickdorn et al., <i>This Is Service Design Doing</i> (2018).",
             "Jeffrey Liker, <i>The Toyota Way</i> (2004).",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021)."],
)

# ------------------------------------------------------------------ 11 Customer Advisory Panel
cp_problem = Doodle(760, 280, "Doodle of September 2026. The team wants early reactions to ideas like slot reminders and the live order timeline, but recruiting new interviewees each time takes a week, and surveys are too shallow. The Thursday interviews give depth but always with someone new, who doesn't know what came before.",
                    "Every interview starts from zero; surveys are shallow; recruiting takes a week each time.")
cp_problem.box(20, 40, 220, 80, "surveys", "paper", sub="shallow")
cp_problem.box(270, 40, 220, 80, "new interviewees", "paper", sub="a week to recruit")
cp_problem.box(520, 40, 220, 80, "no history", "paper", sub="start from zero")
cp_problem.note(380, 200, "we want depth, early, from people who know us", "red", size=18)

cp_analogy = Doodle(760, 250, "Doodle of a restaurant's regulars invited to try the new menu before it launches. A dozen people who know the place well, from different tables: families, couples, the Friday business lunch. Their reactions shape the menu; their votes don't decide it.",
                     "Regulars trying the new menu early: a dozen people who know the place, from different tables.")
cp_analogy.icon("menu", 40, 50, 1.4)
for i, (t, f) in enumerate([("families", "y"), ("couples", "blue"), ("business lunch", "green")]):
    cp_analogy.box(170 + i * 196, 60, 180, 70, t, f, size=16)
cp_analogy.note(450, 200, "reactions shape it; votes don't decide it", "pen")

cp_how = Doodle(760, 360, "Larder's customer advisory panel from 21 September 2026: twelve customers. Four tonight-dinner parents, three Sunday planners, two allergy households, two office managers, one lapsed customer. A ninety-minute session each quarter, short questions by message each month, a thank-you voucher. Rules: depth not votes; a third rotate out each year; never the only evidence for a decision. First session: the live order timeline and slot reminders.",
                 "Twelve customers, varied on purpose. Quarterly sessions, monthly questions, a third rotating out yearly. Depth, not votes.")
for i, (t, n, f) in enumerate([("parents", "4", "y"), ("planners", "3", "blue"), ("allergy", "2", "pink"), ("offices", "2", "green"), ("lapsed", "1", "paper")]):
    cp_how.box(10 + i * 150, 20, 140, 80, t, f, sub=n, size=13)
for i, (t, s) in enumerate([("quarterly", "90-min session"), ("monthly", "short questions"), ("yearly", "a third rotate")]):
    cp_how.box(14 + i * 248, 130, 236, 70, t, "paper", sub=s)
cp_how.box(14, 226, 732, 60, "rules: depth, not votes · never the only evidence", "green", size=15)
cp_how.note(380, 326, "first session, 21 Sep: live timeline, slot reminders", "pen", size=16)

PANEL = dict(
    slug="advisory-panel",
    kicker="a.k.a. “the regulars try the new menu”",
    tldr="A <b>customer advisory panel</b> is a small group (around a dozen) of real customers, <b>varied on purpose</b>, who agree to give feedback regularly: a <b>session each quarter</b>, <b>short questions</b> in between. Because they know your product and each other's context, you get <b>depth and early reactions</b> fast. Use it for <b>understanding, not voting</b>; rotate members so it doesn't become a fan club; and never let it be the <b>only evidence</b> for a decision.",
    chips=[("Family", "listening"), ("Origin", "customer advisory boards in B2B; community research panels"), ("Lives in", "a roster, a quarterly calendar and a notes folder"), ("Pairs with", "customer interviews, proto-personas, prototype testing")],
    problem_side="Larder, 21 September 2026",
    problem="""  <p class="lead">The trio wants early reactions to ideas like <b>slot reminders</b> and the <b>live order timeline</b>. The Thursday interviews give depth, but always with <b>someone new</b> who doesn't know what came before; recruiting each one takes a week; surveys are too shallow to explain anything. <span class="hl-pink">Every conversation starts from zero.</span></p>
  <ul>
    <li>New interviewees need context every time.</li>
    <li>Surveys say what, rarely why.</li>
    <li>Early ideas need quick, informed reactions.</li>
  </ul>""",
    problem_figs=[cp_problem],
    analogy_side="the regulars and the new menu",
    analogy="""  <p>Before a new menu launches, a good restaurant invites a dozen <b>regulars</b> to try it, chosen from different tables: <b>families</b>, <b>couples</b>, the <b>Friday business lunch</b>. They know the place, so their reactions are quick and specific. Their reactions <b>shape</b> the menu; their votes don't <b>decide</b> it, because twelve regulars aren't all the guests.</p>""",
    analogy_figs=[cp_analogy],
    map=[("A dozen regulars", "Twelve customers on the panel"),
         ("From different tables", "Personas, allergies, offices, one lapsed customer"),
         ("Trying the menu early", "Quarterly sessions on early ideas"),
         ("Shaping, not deciding", "Depth, not votes"),
         ("New regulars each year", "A third rotate out yearly")],
    how_side="small, varied, regular, not a vote",
    how="""  <p>Grace and Noor recruited <b>twelve</b> customers, varied on purpose: four dinner parents, three Sunday planners, two allergy households, two office managers and <b>one lapsed customer</b>. A <b>90-minute session</b> each quarter, short questions by message monthly, a thank-you voucher. The first session (21 September) reshaped the live timeline (“show the courier's name, not a map”) and cooled slot reminders (“I'd switch them off”). Both went to a test, not straight to the backlog.</p>""",
    how_figs=[cp_how],
    steps=[("Recruit for variety", "Personas, segments, at least one lapsed or unhappy customer."),
           ("Keep it small", "Ten to fifteen people; enough variety, few enough to know."),
           ("Set a rhythm", "A quarterly session, short monthly questions."),
           ("Thank them properly", "A voucher or credit, and tell them what changed."),
           ("Use for depth", "Reactions and reasons; test anything important with more customers."),
           ("Rotate yearly", "A third out each year so it doesn't become a fan club.")],
    vocab=[("Advisory panel", "A standing group of customers giving regular feedback."),
           ("Recruitment", "Choosing who joins, deliberately varied."),
           ("Rotation", "Replacing some members each year."),
           ("Fan club effect", "A panel growing too loyal to be critical."),
           ("Depth vs breadth", "Why and how (panel) vs how many (surveys, data)."),
           ("Incentive", "A thank-you for members' time.")],
    code=dict(file="product/research/advisory-panel.md", note="the panel charter, September 2026", plain=True, src="""
# Customer advisory panel · charter                 owners: Grace, Noor · started 21 Sep 2026

Members     12: dinner parents (4), Sunday planners (3), allergy households (2),
            office managers (2), lapsed customer (1) · Amsterdam 8, Rotterdam 4
Rhythm      90-min session each quarter (in person or video) · 2–3 questions by message monthly
Thanks      €25 voucher per session; a short "what changed because of you" note
Rules       depth, not votes · never the only evidence for a decision ·
            a third rotate out each year · no employees' friends or family
Session 1   21 Sep: live order timeline (→ show courier's first name, not a map),
            slot reminders (→ cooled: "I'd switch them off"; test before building)
"""),
    tools="tools: a roster and consent forms (with Lena for privacy), a video-call tool, a messaging channel or short surveys between sessions, a notes folder linked to the opportunity tree.",
    gains=["<b>Depth fast</b>: people who know the product.",
           "<b>Early reactions</b> before building.",
           "<b>Continuity</b>: they remember what came before.",
           "<b>Varied voices</b> on purpose, including critics.",
           "<b>Customers feel heard</b>."],
    losses=["<b>Small and not representative</b>.",
            "<b>Members grow loyal</b> over time.",
            "<b>Running costs</b>: time and vouchers.",
            "<b>Tempting to treat as a vote</b>."],
    baseline="Each line compares <b>recruiting new interviewees for every question, or only surveys</b> to <b>a small, varied panel with quarterly sessions, used for depth and rotated yearly</b>.",
    ratings=[(2, 4, "Ideas shaped by people who'll use them."),
             (3, 3, "Indirect."),
             (2, 3, "Deep, but small: confirmed by tests."),
             (2, 4, "Reactions in days, not weeks."),
             (3, 4, "Weak ideas cooled early."),
             (2, 4, "The team hears the same customers over time."),
             (2, 4, "Leaders hear real voices, not just numbers."),
             (3, 3, "Neutral."),
             (2, 3, "A quarterly session and a few messages.")],
    pitfalls=[("A vote", "“8 of 12 want it, build it.”", "depth, not votes; test with more customers."),
              ("A fan club", "Only happy, loyal customers.", "include lapsed and critical members; rotate yearly."),
              ("The only evidence", "Panel opinion beats data.", "combine with data, tests and interviews."),
              ("No thank-you", "Members drift away.", "a voucher and a “what changed” note.")],
    use=["Products with a steady base of repeat customers.",
         "Early reactions to ideas before tests.",
         "Following how needs change over a year.",
         "B2B: a few key clients' office managers."],
    skip=["Questions needing numbers: use data or experiments.",
          "One-off research on a new segment: recruit fresh."],
    related=["<b>Customer interviews</b> (Vol. 1)", "<b>Proto-personas</b> (Vol. 1)", "<b>Prototype testing with users</b> (Vol. 1)", "<b>Kano model</b> (Vol. 2)"],
    quiz=[("What is a panel good for?", "Depth and early reactions from people who know the product."),
          ("What's it not for?", "Voting, or being the only evidence for a decision."),
          ("How do you avoid a fan club?", "Recruit for variety, include critics and lapsed customers, rotate a third yearly."),
          ("Who's on Larder's panel?", "Twelve customers across personas, allergy households, office managers and one lapsed customer.")],
    try_it="Sketch a panel of ten for your product: which segments, at least one critic, and a thank-you. Invite three this month for a 60-minute session on one early idea, and note what they told you that data couldn't.",
    remember="Invite the <span class=\"hl\">regulars</span> early. Their reactions shape it; they don't <span class=\"hl\">vote</span> on it.",
    sources=["Steve Portigal, <i>Interviewing Users</i>, 2nd ed. (2023).",
             "Erika Hall, <i>Just Enough Research</i>, 2nd ed. (2019).",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021).",
             "Indi Young, <i>Practical Empathy</i> (2015)."],
)

NOTES = [TICKETS, OPS, PANEL]
