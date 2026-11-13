# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 5 · Communicating.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Product Update that Gets Read
pu_problem = Doodle(760, 280, "Doodle of October 2026. Grace's weekly update is a two-page email listing every ticket shipped. It goes to 31 people; 6 open it, nobody clicks a link, and Priya still asks in meetings what's going on with live updates.",
                    "A two-page list of tickets, sent to 31 people. Six open it. Priya still asks what's going on.")
pu_problem.icon("envelope", 40, 40, 1.4)
pu_problem.box(150, 40, 270, 90, "2 pages", "paper", sub="every ticket shipped")
pu_problem.box(460, 40, 280, 90, "6 of 31 open it", "pink", sub="0 link clicks", stroke="red")
pu_problem.note(380, 210, "written, sent, unread", "red", size=20)

pu_analogy = Doodle(760, 250, "Doodle of a ship's captain's daily log entry: position, weather, what happened, what's next, what's needed from the owners. Short, the same order every day, the important line first. Anyone can read it in a minute.",
                     "A captain's log: position, weather, events, next, needs. The same order, every day, in a minute.")
pu_analogy.icon("ship", 30, 70, 1.1)
for i, (t, f) in enumerate([("position", "y"), ("events", "paper"), ("next", "blue"), ("needs", "green")]):
    pu_analogy.box(150 + i * 150, 70, 138, 60, t, f, size=16)
pu_analogy.note(450, 200, "same order, important line first", "pen")

pu_how = Doodle(760, 400, "Grace's weekly update from 5 October 2026, sent Fridays at 16:00 in chat and email. Five short sections, always in the same order: outcomes, two numbers with their trend; shipped, at most three lines; learned, one thing; next, what's coming; asks, each with a name and a date. After six weeks: opened by 24 of 31 people, and every ask answered by Monday.",
                 "Outcomes first, then shipped, learned, next, and asks with names. Opened by 24 of 31.")
for i, (t, s, f) in enumerate([("outcomes", "swap refunds 2.7 % ↓ · perfect orders 85.5 %", "green"), ("shipped", "≤ 3 lines", "paper"), ("learned", "one thing", "y"),
                               ("next", "what's coming", "blue"), ("asks", "a name and a date each", "pink")]):
    y = 14 + i * 54
    pu_how.box(14, y, 732, 46, None, f, rx=6)
    pu_how.text(30, y + 30, t, "t-head", anchor="start", size=16)
    pu_how.text(730, y + 30, s, anchor="end", size=14)
pu_how.note(380, 310, "Fridays 16:00 · chat + email · one screen", "pen", size=16)
pu_how.note(380, 346, "6 → 24 of 31 open it · asks answered by Monday", "green", size=16)

UPDATE = dict(
    slug="product-update",
    kicker="a.k.a. “the captain's log”",
    tldr="A <b>product update</b> people read is <b>short</b> (one screen), <b>regular</b> (same day, same time), and always in the <b>same order</b>, with what matters most first: <b>outcomes</b> (the numbers you're trying to move), then <b>shipped</b>, <b>learned</b>, <b>next</b> and <b>asks</b>, each ask with a name and a date. A list of tickets tells people what the team did; a good update tells them what changed and what you need.",
    chips=[("Family", "communicating"), ("Origin", "product practice; “weekly snippets” and status-report habits"), ("Lives in", "a Friday message in chat and email"), ("Pairs with", "managing up, OKRs, dashboards that get used")],
    problem_side="Larder, 5 October 2026",
    problem="""  <p class="lead">Grace's weekly update is a <b>two-page email</b> listing every ticket shipped. It goes to <b>31 people</b>; <b>6</b> open it, nobody clicks a link, and Priya still asks in meetings <span class="hl-pink">what's going on with live updates</span>. Sam finds out about changes from customers.</p>
  <ul>
    <li>Lists of tickets don't say what changed for customers.</li>
    <li>Long updates are skipped, so the important line is missed.</li>
    <li>Asks buried at the end never get answered.</li>
  </ul>""",
    problem_figs=[pu_problem],
    analogy_side="the captain's log",
    analogy="""  <p>A ship's captain writes a <b>daily log</b>: position, weather, what happened, what's next, what's needed from the owners. <b>Short</b>, the <b>same order every day</b>, the important line first. The owners read it in a minute and know whether to worry.</p>""",
    analogy_figs=[pu_analogy],
    map=[("Position", "Outcomes: swap refunds, perfect orders"),
         ("What happened", "Shipped, at most three lines"),
         ("Weather ahead", "Next: what's coming"),
         ("What's needed from the owners", "Asks, each with a name and a date"),
         ("Every day, same order", "Fridays at 16:00, same five sections")],
    how_side="five sections, outcomes first",
    how="""  <p>From <b>5 October</b> Grace's update fits on one screen, Fridays at <b>16:00</b>, in chat and email, always in the same order: <b>outcomes</b> (two numbers with their trend), <b>shipped</b> (at most three lines), <b>learned</b> (one thing), <b>next</b>, and <b>asks</b>, each with a name and a date. After six weeks <b>24 of 31</b> people open it, and every ask is answered by Monday. Priya stopped asking in meetings.</p>""",
    how_figs=[pu_how],
    steps=[("Pick a fixed slot", "Same day and time every week."),
           ("Lead with outcomes", "The numbers you're moving, with the trend."),
           ("Keep shipped short", "Three lines, in customers' words."),
           ("Share one lesson", "Including what didn't work."),
           ("Make asks specific", "Who, what, by when."),
           ("Watch who reads it", "Opens and replies; cut what nobody uses.")],
    vocab=[("Product update", "A regular, short message about the product's progress."),
           ("Outcome", "A change in customer behaviour or a business number."),
           ("Output", "Something the team shipped."),
           ("Ask", "A specific request: who, what, by when."),
           ("Cadence", "The fixed rhythm of a message or meeting."),
           ("BLUF", "Bottom line up front.")],
    code=dict(file="product/updates/2026-11-13.md", note="the update, Friday 13 November 2026", plain=True, src="""
# Ordering & apps · week 46 · Grace

OUTCOMES   Swap refund tickets 2.6 % of orders (↓ from 2.7) · perfect orders 85.8 % (↑)
SHIPPED    Business standing orders: first test order picked at Noord 06:00 ✓
           Live timeline on the web shop (app since 21 Sep)
LEARNED    Office managers want a "skip this week" button more than editing (Mo's calls, 5 of 6)
NEXT       Korenwolf go-live prep (4 Jan) · order-editing pitch to Femke (30 Nov)
ASKS       Cho: invoice line per cost centre in billing test by 20 Nov?
           Joost: 2 pickers at Noord from 05:45 on Mondays from 4 Jan, yes/no by 18 Nov?
"""),
    tools="tools: chat and email; a template; the health page for the numbers; read counts if your email tool has them.",
    gains=["<b>Read</b>: 24 of 31 instead of 6.",
           "<b>Outcomes in view</b> every week.",
           "<b>Asks answered</b> quickly.",
           "<b>Fewer status meetings</b>.",
           "<b>Support and ops</b> hear first."],
    losses=["<b>A weekly habit</b> to keep.",
            "<b>Hard choices</b> about what to leave out.",
            "<b>Bad weeks</b> are visible too.",
            "<b>Not for discussion</b>: decisions need a conversation."],
    baseline="Each line compares <b>a long list of shipped tickets</b> to <b>a one-screen weekly update: outcomes, shipped, learned, next and asks</b>.",
    ratings=[(3, 3, "Indirect."),
             (2, 4, "The outcome numbers lead every week."),
             (2, 4, "Numbers, not adjectives."),
             (3, 4, "Lessons shared weekly."),
             (2, 4, "Three lines of shipped force choices."),
             (2, 5, "31 people know what changed and why."),
             (2, 5, "Priya stopped asking in meetings."),
             (3, 3, "Neutral."),
             (2, 4, "Twenty minutes on a Friday.")],
    pitfalls=[("A ticket list", "Forty lines of Jira titles.", "outcomes first, three lines shipped."),
              ("Vague asks", "“Any help welcome.”", "a name and a date."),
              ("Only good news", "Bad weeks skipped.", "the same format every week."),
              ("Different every week", "Readers can't scan it.", "same five sections, same order.")],
    use=["Any product with stakeholders outside the team.",
         "When people keep asking “what's the status?”",
         "Replacing status meetings.",
         "Alongside quarterly reviews."],
    skip=["Very small teams where everyone's in the room daily."],
    related=["<b>Managing up</b> (this volume)", "<b>The quarterly product review</b> (this volume)", "<b>Dashboards that get used</b> (Vol. 4)", "<b>OKRs</b> (Vol. 4)"],
    quiz=[("What comes first in the update?", "Outcomes: the numbers you're trying to move, with the trend."),
          ("What makes an ask work?", "A name, a specific request and a date."),
          ("What changed after six weeks?", "24 of 31 people opened it, and asks were answered by Monday."),
          ("Why the same order every week?", "So readers can scan it in a minute.")],
    try_it="Rewrite your last status update in five sections: outcomes, shipped (three lines), learned, next, asks with names and dates. Send it at the same time for four weeks and count who replies.",
    remember="Write the <span class=\"hl\">captain's log</span>: position first, needs last, every <span class=\"hl\">Friday</span>.",
    sources=["Barbara Minto, <i>The Pyramid Principle</i> (1987).",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018), on outcomes.",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), stakeholder communication.",
             "Joel Schwartzberg, <i>Get to the Point!</i> (2017)."],
)

# ------------------------------------------------------------------ 02 Demos that Land
dm_problem = Doodle(760, 280, "Doodle of the sprint review in October 2026: Ben shares his screen and clicks through Jira tickets in a meeting room. Four people attend, all from the team. The pickers and support agents whose work will change aren't there, and nobody asks anything.",
                    "Ben clicks through tickets for four teammates. The people whose work will change aren't in the room.")
dm_problem.icon("screen", 40, 40, 1.4)
dm_problem.box(160, 40, 260, 90, "tickets on a screen", "paper", sub="“and this one…”")
dm_problem.box(460, 40, 280, 90, "4 attendees", "pink", sub="all from the team", stroke="red")
dm_problem.note(380, 210, "shown, not seen", "red", size=20)

dm_analogy = Doodle(760, 250, "Doodle of an estate agent's viewing: not a list of the house's features on a screen, but a walk through it as if you lived there, morning coffee in the kitchen, the kids' room, the route to the station, with the people who'd live in it.",
                     "A house viewing: walk through it as if you lived there, with the people who would.")
dm_analogy.icon("door", 40, 60, 1.3)
dm_analogy.box(170, 50, 270, 90, "feature list", "pink", sub="on a screen")
dm_analogy.box(470, 50, 270, 90, "the walk-through", "green", sub="with the family")
dm_analogy.note(450, 205, "show the life, not the list", "pen")

dm_how = Doodle(760, 380, "Grace's demo for Korenwolf's standing orders, 2 November 2026, at the Noord store at 06:00. A story: Korenwolf's Amsterdam office manager sets a weekly order on Thursday; at 06:00 on Monday the picker's handheld shows it; the van leaves at 07:10. Real devices, realistic data. The people it changes: Tomás and two pickers, Sam, Mo and Eli. Twenty minutes, then one question: what would go wrong here? Tomás: the van's loading list is in picking order, not delivery order. Fixed before go-live.",
                 "A customer's story, on real devices, where the work happens, to the people it changes. Then: what would go wrong?")
for i, (t, s, f) in enumerate([("Thu", "office manager sets it", "y"), ("Mon 06:00", "picker's handheld", "blue"), ("07:10", "van leaves", "green")]):
    dm_how.box(14 + i * 248, 14, 236, 80, t, f, sub=s, size=17)
    if i:
        dm_how.arrow(14 + i * 248 - 10, 54, 14 + i * 248 - 2, 54)
dm_how.box(14, 116, 732, 50, "at Noord, 06:00, real handhelds · Tomás, 2 pickers, Sam, Mo, Eli", "paper", size=14)
dm_how.box(14, 186, 732, 60, "“what would go wrong here?”", "y", size=18)
dm_how.box(14, 266, 732, 50, "Tomás: loading list in picking order, not delivery order", "pink", size=14)
dm_how.note(380, 354, "fixed before go-live, 4 January", "green", size=17)

DEMOS = dict(
    slug="demos",
    kicker="a.k.a. “the house viewing”",
    tldr="A demo that lands tells a <b>customer's story</b> (someone, something they need, what happens now), uses <b>real devices and realistic data</b>, happens <b>where the work happens</b> if possible, and invites <b>the people it changes</b>, not just the team. Keep it short, then ask a real question (“what would go wrong here?”) and listen. A demo is for <b>learning</b>, not applause.",
    chips=[("Family", "communicating"), ("Origin", "Scrum's sprint review; product demo practice"), ("Lives in", "the sprint review, held where the work happens"), ("Pairs with", "operations feedback, user stories, the product trio")],
    problem_side="Larder, 2 November 2026",
    problem="""  <p class="lead">At the sprint review Ben shares his screen and <b>clicks through tickets</b>: “and this one adds a field…”. Four people attend, all from the team. <span class="hl-pink">The pickers and support agents whose work will change aren't there</span>, and nobody asks anything. Two weeks before, a picker-app change reached Noord as a surprise.</p>
  <ul>
    <li>Tickets show what was built, not what changes for anyone.</li>
    <li>The right audience isn't invited.</li>
    <li>Nobody is asked anything, so nothing is learned.</li>
  </ul>""",
    problem_figs=[dm_problem],
    analogy_side="the house viewing",
    analogy="""  <p>A good estate agent doesn't read out a <b>list of features</b>. They walk you through the house as if you lived there: morning coffee in the kitchen, the kids' room, the route to the station, <b>with the people who'd live in it</b>. That's when the family notices the stairs are too steep.</p>""",
    analogy_figs=[dm_analogy],
    map=[("The feature list", "Tickets on a shared screen"),
         ("Walking through as if you lived there", "A customer's Monday morning, step by step"),
         ("The family", "Tomás, the pickers, Sam and Mo"),
         ("In the house", "At the Noord store, at 06:00"),
         ("The stairs are too steep", "The van's loading list in the wrong order")],
    how_side="a story, real devices, the right people, a question",
    how="""  <p>Grace ran the standing-orders demo <b>at Noord at 06:00</b>: Korenwolf's office manager sets a weekly order on Thursday; on Monday the <b>picker's handheld</b> shows it; the van leaves at 07:10. Real devices, realistic data. She invited <b>Tomás and two pickers</b>, Sam, Mo and Eli. Twenty minutes, then: <b>“What would go wrong here?”</b> Tomás saw it at once: the van's <b>loading list was in picking order</b>, not delivery order. Fixed before go-live.</p>""",
    how_figs=[dm_how],
    steps=[("Pick a customer's story", "Someone, a need, what happens now."),
           ("Use real devices and data", "The phone, the handheld, realistic orders."),
           ("Go where the work happens", "The store, the support desk, a call with the client."),
           ("Invite the people it changes", "Operations, support, sales, a customer."),
           ("Keep it short", "Twenty minutes; one story beats ten features."),
           ("Ask, then listen", "“What would go wrong here?” and write it down.")],
    vocab=[("Sprint review", "The meeting where the team shows what it built and gets feedback."),
           ("Demo script", "The story and steps for a demo."),
           ("Realistic data", "Test data that looks like real use."),
           ("Stakeholder", "Anyone affected by or affecting the product."),
           ("Feedback", "Reactions that can change what's built next."),
           ("Dog-fooding", "Using your own product for real.")],
    code=dict(file="product/demos/2026-11-02-standing-orders.md", note="the demo plan, 2 November 2026", plain=True, src="""
# Demo · business standing orders · Mon 2 Nov 2026, 06:00, Noord · 20 min

Story      Korenwolf Amsterdam's office manager sets a weekly pantry order (Thu)
           → Monday 06:00 the order appears on the picker's handheld → packed in crates
           → van loading list → van leaves 07:10 → delivered by 09:00
Devices    office manager: laptop (admin tool for now) · pickers: two real handhelds · Eli: van app
Data       3 test offices, 48 lines each, realistic products and cost centres
Invited    Tomás + 2 pickers, Sam, Mo, Eli (Dispatch), Ben, Noor
Question   "What would go wrong here?"
Heard      Tomás: loading list in picking order, not delivery order → fixed 9 Nov
           Sam: who do office managers call at 07:30 if something's missing? → Mo's number on the note
"""),
    tools="tools: real devices, a staging environment with realistic data, a short script; record the session for those who can't come.",
    gains=["<b>Problems found</b> before go-live.",
           "<b>The right people</b> see it early.",
           "<b>Operations and support</b> prepared.",
           "<b>Shared understanding</b> of the change.",
           "<b>Shorter</b> than a ticket tour."],
    losses=["<b>More preparation</b>.",
            "<b>Early mornings</b> in the store.",
            "<b>Uncomfortable feedback</b> in front of others.",
            "<b>Realistic data</b> takes work."],
    baseline="Each line compares <b>a ticket tour for the team</b> to <b>a customer's story on real devices, where the work happens, with the people it changes</b>.",
    ratings=[(2, 4, "Office managers get a working delivery from day one."),
             (3, 4, "Korenwolf's go-live protected."),
             (2, 4, "Problems seen, not guessed."),
             (2, 5, "The loading-list bug found two months early."),
             (2, 4, "One story instead of ten tickets."),
             (2, 5, "Pickers, support and sales see the same thing."),
             (2, 4, "Mo and Sam trust what's coming."),
             (3, 4, "Fixes land before release."),
             (3, 3, "An hour of preparation.")],
    pitfalls=[("Ticket tours", "“This one adds a field.”", "a customer's story."),
              ("Team-only audience", "Nobody it affects.", "invite operations, support, sales."),
              ("Fake data", "“Test product 1”.", "realistic orders."),
              ("No question", "Applause, then nothing.", "ask what would go wrong.")],
    use=["Every sprint review.",
         "Before changing someone's daily work.",
         "Before launches and client go-lives.",
         "Showing progress to leaders."],
    skip=["Purely technical changes nobody outside the team will notice."],
    related=["<b>Feedback loops with operations</b> (Vol. 4)", "<b>Operations as a customer</b> (this volume)", "<b>User stories that aren't tasks</b> (Vol. 3)", "<b>Product update that gets read</b> (this volume)"],
    quiz=[("What makes a demo land?", "A customer's story, real devices, the right audience, and a question."),
          ("Who should be invited?", "The people whose work or experience the change affects."),
          ("What did Tomás find?", "The van's loading list was in picking order, not delivery order."),
          ("What's the point of a demo?", "Learning, not applause.")],
    try_it="For your next sprint review, pick one customer's story, run it on a real device, and invite two people outside the team whose work it changes. End with “what would go wrong here?” and note every answer.",
    remember="Give a <span class=\"hl\">house viewing</span>, not a <span class=\"hl\">feature list</span>.",
    sources=["Ken Schwaber and Jeff Sutherland, <i>The Scrum Guide</i> (2020), sprint review.",
             "Gojko Adzic, <i>Specification by Example</i> (2011).",
             "Jeff Patton, <i>User Story Mapping</i> (2014).",
             "Peter Coffee and others on “show, don't tell” in product demos."],
)

# ------------------------------------------------------------------ 03 The One-Page PRD
pr_problem = Doodle(760, 280, "Doodle of October 2026. Ruben has sent Mo a 14-page requirements document for Korenwolf's standing orders, written in procurement language. Ben's team asks Grace what they're actually building for January. Nobody has said what problem it solves or what's out of scope.",
                    "A 14-page requirements document, and the team still asks: what are we building, and what's out?")
pr_problem.icon("book", 40, 40, 1.4)
pr_problem.box(160, 40, 260, 90, "14 pages", "paper", sub="procurement language")
pr_problem.box(460, 40, 280, 90, "Ben's team", "pink", sub="“what's in for January?”")
pr_problem.note(380, 210, "lots of words, no problem statement", "red", size=19)

pr_analogy = Doodle(760, 250, "Doodle of a film's one-page pitch: who it's about, what they want, what stands in the way, what kind of film it is and isn't. Everyone on set, from director to caterer, knows what they're making.",
                     "A film's one-page pitch: who, what they want, what's in the way, what kind of film it is and isn't.")
pr_analogy.icon("camera", 40, 60, 1.3)
for i, (t, f) in enumerate([("who", "y"), ("wants", "blue"), ("in the way", "pink"), ("is / isn't", "green")]):
    pr_analogy.box(150 + i * 150, 70, 138, 60, t, f, size=16)
pr_analogy.note(450, 200, "everyone on set knows what they're making", "pen")

pr_how = Doodle(760, 400, "Grace's one-page PRD for business standing orders, 12 October 2026. Problem: Korenwolf's office managers order pantry stock by phoning Mo, who re-types it. Outcome: three offices ordering without phoning Mo, 98 percent complete deliveries by 09:00. Users: office managers, Mo, pickers at 06:00, van drivers. In scope for 4 January: weekly standing orders per office, cost centre on the invoice, skip a week. Out: self-service editing, an API, custom invoice layouts. Open questions with owners. Links: ADR 0014, the contract, the demo.",
                 "Problem, outcome, users, in, out, open questions, links. One page; the 14 pages became an appendix.")
for i, (t, s, f) in enumerate([("problem", "office managers phone Mo", "pink"), ("outcome", "3 offices, no phone · 98 % by 09:00", "green"),
                               ("users", "office managers · Mo · pickers · vans", "paper"), ("in (4 Jan)", "standing orders · cost centre · skip a week", "y"),
                               ("out", "self-service editing · API · custom invoices", "blue"), ("open", "3 questions, each with an owner", "paper")]):
    y = 14 + i * 54
    pr_how.box(14, y, 732, 46, None, f, rx=6)
    pr_how.text(30, y + 30, t, "t-head", anchor="start", size=16)
    pr_how.text(730, y + 30, s, anchor="end", size=14)
pr_how.note(380, 362, "links: ADR 0014 · the contract · the 14 pages as an appendix", "pen", size=15)

PRD = dict(
    slug="one-page-prd",
    kicker="a.k.a. “the film's one-page pitch”",
    tldr="A <b>one-page PRD</b> (product requirements document) says, on a single page: the <b>problem</b> and for whom, the <b>outcome</b> that shows it's solved, the <b>users</b>, what's <b>in scope</b> and, just as important, what's <b>out</b>, the <b>open questions</b> with owners, and <b>links</b> to everything else. It's the page everyone can read before a meeting and agree on; detail lives in stories, designs and ADRs.",
    chips=[("Family", "communicating"), ("Origin", "product practice; Amazon's PR/FAQ and “one-pager” traditions"), ("Lives in", "the product wiki, linked from the roadmap and the epic"), ("Pairs with", "problem statements, story mapping, working with the architect")],
    problem_side="Larder, 12 October 2026",
    problem="""  <p class="lead">Korenwolf's three-office contract starts in January. Ruben has sent Mo a <b>14-page requirements document</b> in procurement language; ADR 0014 says scheduled orders live in Ordering. Ben's team asks Grace: <b>what are we actually building for January?</b> <span class="hl-pink">Nobody has said what problem it solves, or what's out.</span></p>
  <ul>
    <li>Long documents get skimmed and read differently.</li>
    <li>Without “out of scope”, everything is in.</li>
    <li>The problem gets lost under the features.</li>
  </ul>""",
    problem_figs=[pr_problem],
    analogy_side="the film's one-page pitch",
    analogy="""  <p>Before a film is made, it's pitched on <b>one page</b>: who it's about, what they want, what stands in the way, what kind of film it <b>is</b> and what it <b>isn't</b>. Everyone on set, from the director to the caterer, knows what they're making. The script, the storyboards and the budget come after, and point back to it.</p>""",
    analogy_figs=[pr_analogy],
    map=[("Who it's about", "Office managers, Mo, pickers, van drivers"),
         ("What they want", "Order the pantry without phoning Mo"),
         ("What kind of film it isn't", "Out of scope: editing, API, custom invoices"),
         ("The script and storyboards", "Stories, designs and ADR 0014"),
         ("Everyone on set", "Ben's and Dee's teams, Mo, Joost, Cho")],
    how_side="one page, with what's out",
    how="""  <p>Grace wrote one page: <b>problem</b> (office managers order by phoning Mo, who re-types it), <b>outcome</b> (three offices ordering without phoning, <b>98 % complete by 09:00</b>), <b>users</b>, <b>in</b> for 4 January (weekly standing orders per office, cost centre on the invoice, skip a week), <b>out</b> (self-service editing, an API, custom invoice layouts), <b>open questions</b> with owners, and <b>links</b> to ADR 0014 and the contract. Ruben's 14 pages became an appendix. Ben: “first time I knew what <i>not</i> to build.”</p>""",
    how_figs=[pr_how],
    steps=[("State the problem", "Who, what's hard, from their side."),
           ("Name the outcome", "A number that shows it's solved."),
           ("List the users", "Everyone it touches, including operations."),
           ("Write in and out", "Out matters as much as in."),
           ("List open questions", "Each with an owner and a date."),
           ("Link the rest", "Stories, designs, ADRs, contracts.")],
    vocab=[("PRD", "Product requirements document."),
           ("Scope", "What the work includes."),
           ("Out of scope", "What it explicitly doesn't."),
           ("Open question", "Something not yet known, with an owner."),
           ("Appendix", "Detail kept, but not in the way."),
           ("Single source of truth", "The one page everything points to.")],
    code=dict(file="product/prd/business-standing-orders.md", note="the one-page PRD, 12 October 2026", plain=True, src="""
# Business standing orders · one page · owner: Grace · v3, 12 Oct 2026

Problem    Korenwolf's office managers order pantry stock by phoning or emailing Mo, who re-types
           it every week; mistakes reach the invoice (October: 3 items billed, never delivered).
Outcome    3 Korenwolf offices order without phoning Mo · ≥ 98 % complete deliveries by 09:00
Users      office managers · Mo · pickers (Noord, Rotterdam) from 06:00 · van drivers · Cho (billing)
In (4 Jan) weekly standing order per office · cost centre per line on the invoice · skip a week
Out        self-service editing (spring) · Business API (later) · Korenwolf-specific invoice layout
Open       Q1 who changes orders before the portal? → Mo, by email (Mo, 19 Oct)
           Q2 holiday weeks: skip or pause? (Grace, 26 Oct)
           Q3 picking at 06:00: staffing (Joost, 2 Nov)
Links      ADR 0014 · contract (Sep 2026) · Ruben's requirements (appendix) · demo 2 Nov
"""),
    tools="tools: the wiki or docs, one template; links to the backlog, designs and ADRs.",
    gains=["<b>One page</b> everyone reads.",
           "<b>“Out” made explicit</b>.",
           "<b>The problem stays visible</b>.",
           "<b>Open questions owned</b>.",
           "<b>Faster agreement</b> before work starts."],
    losses=["<b>Hard to write short</b>.",
            "<b>Clients may want</b> their long document honoured.",
            "<b>Needs updating</b> as answers arrive.",
            "<b>Not enough on its own</b> for complex details."],
    baseline="Each line compares <b>a long requirements document</b> to <b>a one-page PRD with problem, outcome, users, in, out, open questions and links</b>.",
    ratings=[(2, 4, "The office managers' problem is on top."),
             (2, 4, "The outcome is the contract's number."),
             (3, 4, "Grounded in Mo's calls and the contract."),
             (3, 3, "Neutral."),
             (1, 5, "Three things in, three explicitly out."),
             (1, 5, "Ben's and Dee's teams know what not to build."),
             (2, 4, "Mo and Ruben agree the page."),
             (2, 4, "Small scope ships on the date."),
             (2, 4, "One page, updated weekly.")],
    pitfalls=[("No “out”", "Everything implicitly in.", "write what's out, explicitly."),
              ("Features as the problem", "“Build standing orders.”", "who struggles with what."),
              ("Too long again", "Three pages creep in.", "link detail; keep one page."),
              ("Stale", "Answers never added.", "update it as questions close.")],
    use=["Any piece of work bigger than a few stories.",
         "Client work with long requirement documents.",
         "Before kick-offs and refinement.",
         "When teams ask “what are we building?”"],
    skip=["Tiny changes: the story is enough."],
    related=["<b>Problem statements</b> (Vol. 1)", "<b>Story mapping</b> (Vol. 3)", "<b>Negotiating scope</b> (this volume)", "<b>Working with account managers</b> (this volume)"],
    quiz=[("What sections does a one-page PRD have?", "Problem, outcome, users, in, out, open questions, links."),
          ("Why write what's out?", "Otherwise everything is assumed to be in."),
          ("What happened to Ruben's 14 pages?", "They became an appendix, linked from the page."),
          ("What was out for January?", "Self-service editing, the API and a custom invoice layout.")],
    try_it="Take the biggest thing on your roadmap and write its one page: problem, outcome, users, in, out, open questions with owners, links. Show it to one engineer and one stakeholder and ask what's missing.",
    remember="Pitch the <span class=\"hl\">film</span> on one page, including what it <span class=\"hl\">isn't</span>.",
    sources=["Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on product specs.",
             "Colin Bryar and Bill Carr, <i>Working Backwards</i> (2021), PR/FAQ.",
             "Kevin Yien, “Product Spec Template” (2018, widely shared).",
             "Ryan Singer, <i>Shape Up</i> (2019), pitches."],
)

# ------------------------------------------------------------------ 04 The Quarterly Product Review
qr_problem = Doodle(760, 280, "Doodle of the Q3 review in October 2026: a two-hour meeting with forty slides of features, screenshots and burndown charts. Femke leaves after an hour; Marco asks what any of it did for cost per order; the next quarter's bets aren't discussed at all.",
                    "Forty slides of features in two hours. Femke leaves early; next quarter's bets never come up.")
qr_problem.box(20, 40, 220, 90, "40 slides", "paper", sub="features, screenshots")
qr_problem.box(270, 40, 220, 90, "Femke", "pink", sub="leaves after an hour")
qr_problem.box(520, 40, 220, 90, "Marco", "y", sub="“what did it do?”")
qr_problem.note(380, 210, "a show-and-tell, not a review", "red", size=20)

qr_analogy = Doodle(760, 250, "Doodle of a sports team's half-time talk: the score, what's working, what isn't, the plan for the second half, and what the coach needs from the bench. Ten minutes, the same shape every match.",
                     "A half-time talk: the score, what's working, what isn't, the plan, and what's needed. Ten minutes.")
qr_analogy.icon("stopwatch", 40, 60, 1.3)
for i, (t, f) in enumerate([("the score", "y"), ("working", "green"), ("not working", "pink"), ("the plan", "blue")]):
    qr_analogy.box(150 + i * 150, 70, 138, 60, t, f, size=15)
qr_analogy.note(450, 200, "the same shape every match", "pen")

qr_how = Doodle(760, 400, "Grace's Q4 review, 11 January 2027, 45 minutes with a two-page pre-read sent three days before. One: goals against results: swap refund tickets 2.4 percent against a 2.0 target, perfect orders 86.1 percent, Korenwolf live on 4 January. Two: what we learned. Three: next quarter's bets and what they should move. Four: decisions needed today. No screenshots, no feature list. Decisions taken: Q1 bets agreed, the order-editing test confirmed, the 2.0 target moved to March.",
                 "A pre-read, then 45 minutes: results vs goals, lessons, next bets, decisions. Three decisions in the room.")
for i, (t, s, f) in enumerate([("results vs goals", "2.4 % vs 2.0 · 86.1 % · Korenwolf live", "y"), ("learned", "Rotterdam slots drive refunds", "paper"),
                               ("next bets", "order editing · refunds in Rotterdam", "blue"), ("decisions", "3 needed today", "green")]):
    y = 14 + i * 62
    qr_how.box(14, y, 732, 52, None, f, rx=6)
    qr_how.text(30, y + 33, t, "t-head", anchor="start", size=16)
    qr_how.text(730, y + 33, s, anchor="end", size=14)
qr_how.note(380, 288, "pre-read 2 pages, sent 3 days before · 45 minutes", "pen", size=16)
qr_how.note(380, 322, "no screenshots, no feature list", "red", size=16)
qr_how.note(380, 356, "decided: Q1 bets · editing test · 2.0 % by March", "green", size=16)

QUARTERLY = dict(
    slug="quarterly-review",
    kicker="a.k.a. “the half-time talk”",
    tldr="A <b>quarterly product review</b> is where leaders see whether the product did what it set out to do. Send a short <b>pre-read</b>; in the meeting, cover <b>results against goals</b> (honestly), <b>what you learned</b>, the <b>next quarter's bets</b> and what they should move, and the <b>decisions you need</b>. No feature tours. Done well, it's the meeting where strategy and the roadmap get adjusted on evidence.",
    chips=[("Family", "communicating"), ("Origin", "business reviews (e.g. QBRs); OKR grading; product operations practice"), ("Lives in", "a quarterly calendar slot with a pre-read"), ("Pairs with", "OKRs, bets not promises, delivering bad news")],
    problem_side="Larder, 11 January 2027",
    problem="""  <p class="lead">The Q3 review in October was <b>two hours and forty slides</b> of features, screenshots and burndown charts. Femke left after an hour; Marco asked what any of it did for cost per order; <span class="hl-pink">next quarter's bets were never discussed</span>. For Q4 Grace has harder news to bring, and a show-and-tell won't carry it.</p>
  <ul>
    <li>Feature tours hide whether goals were met.</li>
    <li>Leaders' time goes before the decisions come up.</li>
    <li>No pre-read means the meeting is spent catching up.</li>
  </ul>""",
    problem_figs=[qr_problem],
    analogy_side="the half-time talk",
    analogy="""  <p>At half-time a coach doesn't replay every pass. In ten minutes: <b>the score</b>, what's <b>working</b>, what <b>isn't</b>, the <b>plan for the second half</b>, and what's needed from the bench. The same shape every match, so the players know where to listen.</p>""",
    analogy_figs=[qr_analogy],
    map=[("The score", "Results against goals: 2.4 % vs 2.0 %"),
         ("What's working, what isn't", "What we learned this quarter"),
         ("The second-half plan", "Next quarter's bets and what they should move"),
         ("What's needed from the bench", "Decisions needed today"),
         ("Not replaying every pass", "No feature tour, no screenshots")],
    how_side="pre-read, then results, lessons, bets, decisions",
    how="""  <p>Grace sent a <b>two-page pre-read</b> three days before and kept the meeting to <b>45 minutes</b>: <b>results vs goals</b> (swap refund tickets <b>2.4 %</b> against a 2.0 % target, perfect orders 86.1 %, Korenwolf live on 4 January); <b>what we learned</b> (Rotterdam's slot orders drive most remaining refunds); <b>next bets</b>; <b>decisions needed</b>. No screenshots. Three decisions were taken in the room: the Q1 bets, the order-editing test, and the 2.0 % target moved to <b>March</b>.</p>""",
    how_figs=[qr_how],
    steps=[("Send a pre-read", "Two pages, three days before."),
           ("Start with results vs goals", "Including the misses."),
           ("Share what you learned", "Two or three lessons that change plans."),
           ("Propose next bets", "Each with the number it should move."),
           ("List the decisions needed", "And take them in the room."),
           ("Write down what was decided", "Same day, to everyone.")],
    vocab=[("Quarterly review", "A regular review of results, lessons and plans with leaders."),
           ("Pre-read", "A short document read before the meeting."),
           ("QBR", "Quarterly business review."),
           ("Bet", "A piece of work expected, not promised, to move an outcome."),
           ("Decision log", "A record of what was decided and why."),
           ("Show-and-tell", "A tour of features, without results.")],
    code=dict(file="product/reviews/2026-q4.md", note="the Q4 pre-read, sent 8 January 2027", plain=True, src="""
# Ordering & apps · Q4 2026 review · pre-read (2 pages) · meeting 11 Jan, 45 min

RESULTS vs GOALS
  Swap refund tickets   goal 2.0 % by December   result 2.4 %   ✗ (told Priya 7 Dec, Femke 8 Dec)
  Perfect orders        goal 86 %                result 86.1 %  ✓
  Korenwolf go-live     4 Jan                    live 4 Jan     ✓ (3 offices, first week 98.6 %)
LEARNED
  Most remaining swap refunds are Rotterdam slot orders (63 %): notifications off + longer windows
  Office managers want "skip a week" more than editing
NEXT BETS (Q1)
  Order editing for 10 min after checkout (test, Amsterdam) → second deliveries −50 %
  Rotterdam slot swaps: in-app banner + SMS fallback → swap refunds 2.0 % by March
DECISIONS NEEDED   1 Q1 bets · 2 editing test, 4 weeks of Dee's team · 3 move 2.0 % to March
"""),
    tools="tools: a two-page template; the health page and OKR sheet; a calendar slot booked a year ahead.",
    gains=["<b>Decisions taken</b> in the room.",
           "<b>Honest results</b>, misses included.",
           "<b>Leaders' time</b> respected.",
           "<b>Strategy adjusted</b> on evidence.",
           "<b>One shape</b> every quarter."],
    losses=["<b>The pre-read</b> takes a day.",
            "<b>Misses are visible</b>.",
            "<b>Leaders must read</b> it first.",
            "<b>Less room</b> for showing work."],
    baseline="Each line compares <b>a long feature show-and-tell</b> to <b>a pre-read and 45 minutes on results, lessons, next bets and decisions</b>.",
    ratings=[(3, 3, "Indirect."),
             (2, 5, "Every bet tied to a number leaders track."),
             (2, 5, "Results against goals, honestly."),
             (3, 4, "Lessons change the next quarter."),
             (2, 4, "Two bets for Q1, not five."),
             (2, 4, "Everyone hears the same results."),
             (2, 5, "The miss was already known; the plan was credible."),
             (3, 3, "Neutral."),
             (2, 4, "45 minutes instead of two hours.")],
    pitfalls=[("Feature tours", "Forty slides of screens.", "results vs goals."),
              ("Hiding misses", "Only green numbers.", "show every goal, honestly."),
              ("No decisions", "A pleasant meeting.", "list the decisions needed."),
              ("No pre-read", "Half the time spent catching up.", "two pages, three days before.")],
    use=["Every quarter, with leadership.",
         "Alongside OKR grading.",
         "Before planning the next quarter.",
         "When reviews have become show-and-tell."],
    skip=["Teams with continuous, deep leadership involvement (rare)."],
    related=["<b>OKRs</b> (Vol. 4)", "<b>Delivering bad news</b> (this volume)", "<b>Bets, not promises</b> (Vol. 2)", "<b>Presenting to executives</b> (Ana, book 1 vol. 3)"],
    quiz=[("What are the four parts of the review?", "Results vs goals, what we learned, next bets, decisions needed."),
          ("Why send a pre-read?", "So the meeting is spent deciding, not catching up."),
          ("What decisions came out of the Q4 review?", "The Q1 bets, the order-editing test, and moving the 2.0 % target to March."),
          ("What's left out?", "Feature tours and screenshots.")],
    try_it="Draft a two-page pre-read for your next quarterly review: every goal against its result, two lessons, two next bets with numbers, and three decisions you need. Ask for 45 minutes instead of two hours.",
    remember="Give the <span class=\"hl\">half-time talk</span>: the score, the plan, and what you need from the <span class=\"hl\">bench</span>.",
    sources=["Andy Grove, <i>High Output Management</i> (1983).",
             "John Doerr, <i>Measure What Matters</i> (2018), quarterly reviews.",
             "Colin Bryar and Bill Carr, <i>Working Backwards</i> (2021), six-page memos.",
             "Melissa Perri and Denise Tilles, <i>Product Operations</i> (2023)."],
)

NOTES = [UPDATE, DEMOS, PRD, QUARTERLY]
