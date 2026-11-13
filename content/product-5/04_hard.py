# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 5 · Hard moments.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 Negotiating Scope
ns_problem = Doodle(760, 280, "Doodle of 23 November 2026. Ruben sends fourteen must-haves for Korenwolf's go-live on 4 January, including self-service editing, a custom invoice layout and real-time stock in the portal. Grace's team can do five well in the time. Mo wants to say yes to everything; Grace's instinct is to say no to nine.",
                    "Fourteen must-haves for 4 January; room for five. Mo wants yes to all; Grace wants no to nine.")
ns_problem.box(20, 40, 220, 90, "Ruben", "pink", sub="14 must-haves")
ns_problem.box(270, 40, 220, 90, "the team", "paper", sub="room for 5")
ns_problem.box(520, 40, 220, 90, "Mo", "y", sub="“yes to all”")
ns_problem.note(380, 200, "two lists, two positions, no deal", "red", size=19)

ns_analogy = Doodle(760, 250, "Doodle of two sisters arguing over one orange. Their mother cuts it in half; one sister eats the fruit and throws away the peel, the other uses the peel for a cake and throws away the fruit. Asking why each wanted it would have given both of them everything.",
                     "Two sisters, one orange: one wanted the fruit, the other the peel. Ask why before you split it.")
ns_analogy.icon("cup", 40, 60, 1.3)
ns_analogy.box(170, 50, 270, 90, "split in half", "pink", sub="both get half")
ns_analogy.box(470, 50, 270, 90, "ask why", "green", sub="fruit for one, peel for the other")
ns_analogy.note(450, 205, "interests, not positions", "pen")

ns_how = Doodle(760, 400, "Grace and Mo's meeting with Hanna and Ruben, 23 November 2026. First the interests: Hanna wants no complaints from staff and the board; Ruben wants costs booked per department and a service level he can measure. Then the options: for 4 January, standing orders per office, cost centre on every invoice line, skip a week, a monthly delivery report, and changes by email to Mo before 08:00. In spring: self-service changes in a portal. Not planned: the custom invoice layout. Written down and signed by both sides the same week.",
                 "Interests first, then a split by time: five for January, the portal in spring, one no. Signed the same week.")
ns_how.box(14, 14, 360, 90, None, "y")
ns_how.head(194, 44, "Hanna", size=16)
ns_how.text(194, 76, "no complaints from staff or board", size=14)
ns_how.box(386, 14, 360, 90, None, "blue")
ns_how.head(566, 44, "Ruben", size=16)
ns_how.text(566, 76, "costs per department · a measurable SLA", size=13)
for i, (t, s, f) in enumerate([("4 January", "standing orders · cost centres · skip · report · changes via Mo", "green"), ("spring", "self-service changes in a portal", "paper"), ("not planned", "custom invoice layout", "pink")]):
    y = 124 + i * 62
    ns_how.box(14, y, 732, 52, None, f, rx=6)
    ns_how.text(30, y + 33, t, "t-head", anchor="start", size=16)
    ns_how.text(730, y + 33, s, anchor="end", size=13)
ns_how.note(380, 350, "written down, signed by both sides that week", "pen", size=16)

NEGOTIATE = dict(
    slug="negotiating-scope",
    kicker="a.k.a. “the orange and the peel”",
    tldr="Scope negotiations stall when both sides trade <b>lists</b> (positions). Ask instead <b>why</b> each item matters (interests): often a smaller or different solution meets the same need. Then split by <b>time</b> (now, later, not planned) rather than yes or no, keep the account manager or client sponsor <b>in the room</b>, and <b>write the agreement down</b> the same week. Everyone gets what they actually need, if not everything they asked for.",
    chips=[("Family", "hard moments"), ("Origin", "Roger Fisher and William Ury, <i>Getting to Yes</i> (1981), principled negotiation"), ("Lives in", "the meeting notes and a signed scope page"), ("Pairs with", "MoSCoW, one-page PRD, working with account managers")],
    problem_side="Larder, 23 November 2026",
    problem="""  <p class="lead">Ruben sends <b>fourteen must-haves</b> for Korenwolf's go-live on 4 January, including self-service editing, a custom invoice layout and real-time stock in the portal. Grace's team can do <b>five</b> well in the time. Mo wants to say yes to everything; Grace's instinct is to say no to nine. <span class="hl-pink">Two lists, two positions, no deal.</span></p>
  <ul>
    <li>Lists hide why each item is wanted.</li>
    <li>Yes-to-all fails on the date; no-to-nine fails the relationship.</li>
    <li>Agreements made in a meeting are remembered differently.</li>
  </ul>""",
    problem_figs=[ns_problem],
    meanwhile=[("architect-3", "solution-design-document", "the following week, Ana answers Korenwolf IT's 40-section template in 14 pages, about the same January scope.",
                "The week before, Grace and Mo agreed Korenwolf's January scope with Hanna and Ruben: five things now, the portal in spring.")],
    analogy_side="the orange and the peel",
    analogy="""  <p>Two sisters argue over <b>one orange</b>. Their mother cuts it in half. One sister eats her half of the <b>fruit</b> and throws away the peel; the other grates her half of the <b>peel</b> into a cake and throws away the fruit. If anyone had asked <b>why</b> each wanted it, both would have had everything they needed.</p>""",
    analogy_figs=[ns_analogy],
    map=[("The orange", "Fourteen must-haves"),
         ("Cutting it in half", "Seven yes, seven no"),
         ("Asking why", "Hanna's and Ruben's interests"),
         ("The peel for the cake", "Costs per department: a cost centre on each line, not a custom layout"),
         ("The fruit", "No complaints: standing orders that just work")],
    how_side="interests first, then split by time",
    how="""  <p>Grace and Mo met <b>Hanna and Ruben</b> together. First the <b>interests</b>: Hanna wants <b>no complaints</b> from staff or the board; Ruben wants costs <b>booked per department</b> and a <b>service level he can measure</b>. That reshaped the list. For <b>4 January</b>: standing orders per office, cost centre on every invoice line, skip a week, a monthly delivery report, changes by email to Mo before 08:00. In <b>spring</b>: self-service changes in a portal. <b>Not planned</b>: the custom invoice layout (the cost centres met Ruben's need). Signed by both sides that week.</p>""",
    how_figs=[ns_how],
    steps=[("Meet the people with the interests", "The sponsor and the buyer, with the account manager."),
           ("Ask why for each item", "What problem, what happens without it."),
           ("Find smaller ways to meet needs", "The peel, not the orange."),
           ("Split by time", "Now, later, not planned."),
           ("Say what “not planned” means", "With the reason."),
           ("Write it down, same week", "Signed by both sides.")],
    vocab=[("Position", "What someone says they want."),
           ("Interest", "Why they want it."),
           ("BATNA", "Best alternative to a negotiated agreement."),
           ("Principled negotiation", "Negotiating on interests and fair criteria."),
           ("Scope", "What's included in a delivery."),
           ("Sponsor", "The client's senior person who owns the outcome.")],
    code=dict(file="product/korenwolf/scope-2027-01.md", note="the agreed scope, signed 26 November 2026", plain=True, src="""
# Korenwolf · scope for go-live 4 Jan 2027 · agreed 23 Nov, signed 26 Nov
With: Hanna (sponsor), Ruben (procurement), Mo, Grace

Interests   Hanna: no complaints from staff or the board
            Ruben: costs booked per department; a service level he can measure
4 JANUARY   weekly standing order per office · cost centre on every invoice line ·
            skip a week · monthly delivery report (complete by 09:00) ·
            changes by email to Mo before 08:00 the day before
SPRING      self-service changes for office managers (portal)
NOT PLANNED Korenwolf invoice layout: cost centres per line meet the need (Ruben agreed)
            real-time stock in the portal: standing orders are substituted like any order
"""),
    tools="tools: the one-page PRD, a shared scope page, the account manager in the room; MoSCoW or now/later/not planned.",
    gains=["<b>Needs met</b>, not lists.",
           "<b>A date the team can hit</b>.",
           "<b>The relationship kept</b>.",
           "<b>Smaller solutions</b> found.",
           "<b>Written agreement</b> ends re-arguing."],
    losses=["<b>Takes a meeting</b>, not an email.",
            "<b>Some asks</b> wait or never come.",
            "<b>Clients may push back</b> on “not planned”.",
            "<b>Needs the right people</b> in the room."],
    baseline="Each line compares <b>trading lists of yes and no</b> to <b>negotiating on interests, splitting by time and writing the agreement down</b>.",
    ratings=[(2, 4, "Office managers get what they need in January."),
             (2, 5, "The contract starts on time; renewal protected."),
             (2, 4, "Interests heard from Hanna and Ruben directly."),
             (3, 3, "Neutral."),
             (1, 5, "Five things for January, not fourteen."),
             (2, 5, "Mo, Grace, Hanna and Ruben signed one page."),
             (2, 5, "Ruben trusts the plan: needs met, reasons given."),
             (2, 4, "A small first release, then spring."),
             (3, 3, "A meeting and a page.")],
    pitfalls=[("Trading lists", "Seven yes, seven no.", "ask why for each."),
              ("Yes to everything", "A promise the date can't keep.", "split by time."),
              ("Without the account manager", "Mo surprised later.", "negotiate together."),
              ("Nothing written", "Remembered differently in January.", "a signed page, same week.")],
    use=["Client deadlines with long wish lists.",
         "Internal stakeholders with competing asks.",
         "Renewals and contract changes.",
         "Any “all of it, by Friday” moment."],
    skip=["Truly non-negotiable items (law, safety): explain, don't trade."],
    related=["<b>MoSCoW</b> (Vol. 2)", "<b>The one-page PRD</b> (this volume)", "<b>Working with account managers</b> (this volume)", "<b>Solution design document done right</b> (Ana, book 1 vol. 3)"],
    quiz=[("What's the difference between a position and an interest?", "What someone asks for vs why they want it."),
          ("What were Ruben's interests?", "Costs per department and a measurable service level."),
          ("How was the scope split?", "Five things for January, the portal in spring, the custom layout not planned."),
          ("Why write it down the same week?", "So nobody remembers it differently on the date.")],
    try_it="Take the longest wish list you've been handed. For each item, ask (or guess, then check) why it's wanted, find a smaller way to meet that need, and sort everything into now, later and not planned.",
    remember="Ask why before you cut the <span class=\"hl\">orange</span>: one wants the fruit, one the <span class=\"hl\">peel</span>.",
    sources=["Roger Fisher, William Ury and Bruce Patton, <i>Getting to Yes</i>, 3rd ed. (2011).",
             "Chris Voss, <i>Never Split the Difference</i> (2016).",
             "Mary Parker Follett, on integrative solutions (the orange story's origins, 1920s).",
             "Dai Clegg, MoSCoW prioritisation (Oracle, 1994)."],
)

# ------------------------------------------------------------------ 13 When the Date Is Fixed
fd_problem = Doodle(760, 280, "Doodle of 1 December 2026. Korenwolf's go-live on 4 January is in the contract. Christmas and the change freeze sit in between, and Ana's no-change windows are coming. The plan has every item at must-have, no buffer, and the first real order on the go-live morning.",
                    "4 January is in the contract. Christmas in between, every item a must, no buffer, first real order on the day.")
fd_problem.box(20, 40, 220, 90, "4 Jan", "pink", sub="in the contract", stroke="red")
fd_problem.box(270, 40, 220, 90, "Christmas", "paper", sub="+ change freeze")
fd_problem.box(520, 40, 220, 90, "the plan", "y", sub="all must · no buffer")
fd_problem.note(380, 200, "the first real order on the go-live morning", "red", size=18)

fd_analogy = Doodle(760, 250, "Doodle of a wedding day: the date is fixed and the guests are invited. If the florist is late, you don't move the wedding; you use simpler flowers. And you rehearse the day before, not on the morning itself.",
                     "A wedding: the date doesn't move. Simpler flowers if needed, and a rehearsal the day before.")
fd_analogy.icon("calendar", 40, 60, 1.3)
for i, (t, f) in enumerate([("fixed date", "pink"), ("simpler flowers", "y"), ("rehearsal", "green")]):
    fd_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
fd_analogy.note(450, 200, "flex what's on the table, not the day", "pen")

fd_how = Doodle(760, 400, "Grace's plan from 1 December 2026: fix the date, flex the scope. A cut line: above it, what Korenwolf needs on 4 January, built by 11 December; below it, what can follow, such as the automated monthly report, which Mo will send by hand for January. A buffer: two weeks between 11 December and the freeze. An early first release: Larder's own Amsterdam office orders through it from 14 December. The Christmas outage on 18 December cost two days; the buffer absorbed it. Korenwolf went live on 4 January.",
                 "A cut line, a buffer, an early release to ourselves. The Christmas outage cost two days; the buffer took it.")
fd_how.box(14, 14, 732, 50, "above: standing orders · cost centres · skip a week · changes via Mo", "green", size=14)
fd_how.line("M14 80 L746 80", color="red", dash=True)
fd_how.text(380, 98, "cut line", "t t-red", size=15)
fd_how.box(14, 112, 732, 46, "below: automated report (Mo by hand in Jan) · nicer emails", "paper", size=14)
for i, (t, s, f) in enumerate([("11 Dec", "above the line done", "y"), ("14 Dec", "our own office orders", "blue"), ("18 Dec", "outage: −2 days", "pink"), ("4 Jan", "Korenwolf live", "green")]):
    x = 14 + i * 184
    fd_how.box(x, 182, 174, 80, t, f, sub=s, size=17, subsize=13)
fd_how.note(380, 302, "buffer: 11 Dec → freeze; it absorbed the outage", "pen", size=16)
fd_how.note(380, 338, "first week: 98.6 % complete by 09:00", "green", size=16)

FIXED = dict(
    slug="fixed-date",
    kicker="a.k.a. “the wedding day”",
    tldr="When the <b>date is fixed</b> (a contract, a launch, a law), <b>flex the scope</b> instead. Draw a <b>cut line</b>: above it, what's truly needed on the date; below it, what can follow. Finish above the line <b>early</b>, keep a <b>buffer</b>, and release to yourselves first (a rehearsal) so the first real use isn't on the day. Tell everyone where the line is, and move items across it, never the date.",
    chips=[("Family", "hard moments"), ("Origin", "timeboxing (DSDM); fixed-date, flexible-scope planning"), ("Lives in", "the release plan, with the cut line drawn on it"), ("Pairs with", "negotiating scope, dependencies across teams, release plans")],
    problem_side="Larder, 1 December 2026",
    problem="""  <p class="lead">Korenwolf's go-live on <b>4 January</b> is in the contract. <b>Christmas</b> and a change freeze sit in between. The plan has <b>every item at must-have</b>, <b>no buffer</b>, and the first real order on the go-live morning. <span class="hl-pink">Any surprise moves the date</span>, and the date can't move.</p>
  <ul>
    <li>Fixed dates with fixed scope fail on the first surprise.</li>
    <li>Holidays and freezes shrink the real time.</li>
    <li>The first real use on the day is the riskiest moment.</li>
  </ul>""",
    problem_figs=[fd_problem],
    analogy_side="the wedding day",
    analogy="""  <p>A <b>wedding</b> date is fixed: the guests are invited, the venue booked. If the florist is late you don't move the wedding; you use <b>simpler flowers</b>. And you hold a <b>rehearsal the day before</b>, so the first walk down the aisle isn't the real one.</p>""",
    analogy_figs=[fd_analogy],
    map=[("The wedding date", "4 January, in the contract"),
         ("Simpler flowers", "Mo sends the January report by hand"),
         ("The rehearsal", "Larder's own office orders from 14 December"),
         ("A late florist", "The Christmas outage on 18 December"),
         ("Guests and venue", "Korenwolf's three offices")],
    how_side="cut line, buffer, an early release to ourselves",
    how="""  <p>Grace drew a <b>cut line</b>: above it, what Korenwolf needs on day one (standing orders, cost centres, skip a week, changes via Mo), finished by <b>11 December</b>; below it, the automated monthly report (Mo sends January's <b>by hand</b>) and nicer emails. A <b>buffer</b> ran from 11 December to the freeze, and <b>Larder's own Amsterdam office</b> ordered through it from 14 December. The <b>Christmas outage</b> on 18 December cost two days; the buffer absorbed them. Korenwolf went live on <b>4 January</b>: 98.6 % complete by 09:00 in the first week.</p>""",
    how_figs=[fd_how],
    steps=[("Confirm the date is really fixed", "Contract, law, event: and what moves if it slips."),
           ("Draw the cut line", "Above: needed on the day. Below: can follow."),
           ("Finish above the line early", "Weeks, not days, before the date."),
           ("Keep a buffer", "Holidays, freezes and surprises eat time."),
           ("Release to yourselves first", "A rehearsal with real use."),
           ("Move items, never the date", "Across the line, visibly.")],
    vocab=[("Fixed date", "A deadline that can't move without serious cost."),
           ("Flexible scope", "What's delivered adjusts to fit the date."),
           ("Cut line", "The line between what's needed on the date and what follows."),
           ("Buffer", "Time kept free for surprises."),
           ("Timebox", "A fixed period in which scope adjusts."),
           ("Dress rehearsal", "A real run before the real date.")],
    code=dict(file="product/korenwolf/release-plan.md", note="the plan with its cut line, 1 December 2026", plain=True, src="""
# Korenwolf go-live · 4 Jan 2027 (contract) · plan v2, 1 Dec · owner: Grace

ABOVE THE LINE (needed on 4 Jan)                    done by 11 Dec
  weekly standing order per office · cost centre per invoice line · skip a week
  changes by email to Mo before 08:00 · van loading list in delivery order
----------------------------------------------- cut line -----------------------------------------
BELOW (can follow)
  automated monthly report  → Mo sends January's by hand · February: automated
  nicer confirmation emails → March

Buffer      11 Dec → 18 Dec freeze (critical windows from ADR 0017 apply)
Rehearsal   Larder's own Amsterdam office orders through it from 14 Dec
Used        18 Dec outage (−2 days of testing) → absorbed by the buffer
Result      live 4 Jan · first week 98.6 % complete by 09:00 (contract measure)
"""),
    tools="tools: the release plan with a drawn cut line, a calendar with holidays and freezes, an internal pilot (your own office, your own staff).",
    gains=["<b>The date held</b>, despite an outage.",
           "<b>Clear priorities</b> above the line.",
           "<b>A rehearsal</b> found problems early.",
           "<b>A buffer</b> for the unexpected.",
           "<b>Honest expectations</b> for what follows."],
    losses=["<b>Some things wait</b>.",
            "<b>Manual work</b> covers the gaps for a while.",
            "<b>Pressure to move items</b> above the line.",
            "<b>Buffers look like slack</b> to others."],
    baseline="Each line compares <b>fixed date and fixed scope with no buffer</b> to <b>a fixed date with a cut line, early finish, a buffer and a rehearsal</b>.",
    ratings=[(2, 4, "Office managers got a working service on day one."),
             (1, 5, "The contract date held."),
             (3, 4, "The rehearsal showed what worked."),
             (2, 4, "Problems found from 14 December."),
             (1, 5, "Five things above the line."),
             (2, 4, "Everyone saw the same line."),
             (2, 5, "Mo and Korenwolf got what was promised, on time."),
             (2, 4, "Small release first, the rest after."),
             (3, 3, "Manual report for one month.")],
    pitfalls=[("Everything above the line", "No real cut.", "only what's needed on the day."),
              ("No buffer", "Finish the day before.", "weeks before; holidays count."),
              ("First use on the day", "Go-live is the test.", "rehearse with yourselves."),
              ("Moving the date quietly", "“Just one more week.”", "move items, not the date.")],
    use=["Contract go-lives, launches, legal deadlines.",
         "Events (holidays, campaigns, trade fairs).",
         "Anything with a date announced to customers.",
         "When the scope keeps growing near a date."],
    skip=["Dates that are really targets: then say so, and plan as bets."],
    related=["<b>Negotiating scope</b> (this volume)", "<b>Dependencies across teams</b> (this volume)", "<b>Roadmap vs release plan</b> (Vol. 2)", "<b>Launch checklist</b> (Vol. 3)"],
    quiz=[("What flexes when the date is fixed?", "The scope, using a cut line."),
          ("What was below Korenwolf's line?", "The automated monthly report (Mo sent January's by hand) and nicer emails."),
          ("What was the rehearsal?", "Larder's own Amsterdam office ordering through it from 14 December."),
          ("What absorbed the Christmas outage?", "The buffer between 11 December and the freeze.")],
    try_it="For your next fixed date, draw a cut line on the plan: above, only what's needed on the day; below, the rest. Plan to finish above the line two weeks early, and find a way to use it yourselves first.",
    remember="Don't move the <span class=\"hl\">wedding</span>; use simpler flowers, and <span class=\"hl\">rehearse</span>.",
    sources=["DSDM Consortium, <i>The DSDM Agile Project Framework</i> (2014), timeboxing and MoSCoW.",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005).",
             "Johanna Rothman, <i>Manage It!</i> (2007).",
             "Ryan Singer, <i>Shape Up</i> (2019), fixed time, variable scope."],
)

# ------------------------------------------------------------------ 14 Delivering Bad News
bn_problem = Doodle(760, 280, "Doodle of 7 December 2026. Grace's forecast shows swap refund tickets will end December at about 2.4 percent. The board was told 2 percent by December. The board meets on 14 December. The temptation: wait for the final number, hope for a good last fortnight, and let the slide say it.",
                    "The forecast says 2.4 %; the board was told 2 %. Board on 14 December. Tempted to wait and hope.")
bn_problem.box(20, 40, 220, 90, "promised", "paper", sub="2.0 % by December")
bn_problem.box(270, 40, 220, 90, "forecast", "pink", sub="≈ 2.4 %", stroke="red")
bn_problem.box(520, 40, 220, 90, "board", "y", sub="14 December")
bn_problem.note(380, 200, "wait, hope, and let the slide say it?", "red", size=19)

bn_analogy = Doodle(760, 250, "Doodle of a good doctor with a difficult diagnosis: they tell you in person, early, plainly; they say what they know and don't, what caused it, the options, and what happens next. You leave worried but with a plan.",
                     "A good doctor: in person, early, plainly. What's known, the cause, the options, the next step.")
bn_analogy.icon("check", 40, 60, 1.3)
for i, (t, f) in enumerate([("in person", "y"), ("plainly", "paper"), ("options", "blue"), ("next step", "green")]):
    bn_analogy.box(150 + i * 150, 70, 138, 60, t, f, size=16)
bn_analogy.note(450, 200, "worried, but with a plan", "pen")

bn_how = Doodle(760, 400, "How Grace delivered the news. 7 December: told Priya in person the same day. 8 December: with Priya, told Femke, a week before the board. Four parts: the fact, about 2.4 percent against 2.0; the cause, Rotterdam's slot orders, longer windows and notifications off, 63 percent of the remaining refunds; the options, accept and aim for 2.0 by March with an in-app banner and SMS fallback in Rotterdam, or force no-swap defaults, cutting refunds but losing sales; and what Grace would do. Femke took a range and the plan to the board. December ended at 2.4; March reached 2.0.",
                 "Early, in person, to Priya then Femke: fact, cause, options, recommendation. The board got a plan, not a surprise.")
for i, (t, s, f) in enumerate([("fact", "≈ 2.4 % vs 2.0 % promised", "pink"), ("cause", "Rotterdam slot orders: 63 % of refunds", "paper"),
                               ("options", "banner + SMS → 2.0 by March · or forced defaults", "blue"), ("recommend", "banner + SMS; report monthly", "green")]):
    y = 14 + i * 62
    bn_how.box(14, y, 732, 52, None, f, rx=6)
    bn_how.text(30, y + 33, t, "t-head", anchor="start", size=16)
    bn_how.text(730, y + 33, s, anchor="end", size=14)
bn_how.note(380, 290, "7 Dec Priya · 8 Dec Femke · 14 Dec board", "pen", size=16)
bn_how.note(380, 326, "December 2.4 % · March 2.0 %", "green", size=17)

BADNEWS = dict(
    slug="bad-news",
    kicker="a.k.a. “the good doctor”",
    tldr="Bad news gets worse with time. Deliver it <b>early</b> (as soon as the forecast is clear, not the final number), <b>in person</b>, to your manager first and with them to whoever must act on it. Say it in four parts: the <b>fact</b>, the <b>cause</b>, the <b>options</b> (with their costs), and <b>what you recommend</b>. Leaders forgive misses; they don't forgive surprises.",
    chips=[("Family", "hard moments"), ("Origin", "crisis communication; “no surprises” management practice"), ("Lives in", "a conversation first, then a short written follow-up"), ("Pairs with", "managing up, the quarterly product review, bets not promises")],
    problem_side="Larder, 7 December 2026",
    problem="""  <p class="lead">Grace's forecast shows <b>swap refund tickets</b> will end December at about <b>2.4 %</b>. In April the board was told <b>2 % by December</b>. The board meets on <b>14 December</b>. <span class="hl-pink">The temptation: wait for the final number</span>, hope for a good last fortnight, and let the slide say it.</p>
  <ul>
    <li>Waiting turns a miss into a surprise.</li>
    <li>Bad news without a cause or a plan sounds like failure.</li>
    <li>Your manager learning it in the board meeting costs trust.</li>
  </ul>""",
    problem_figs=[bn_problem],
    analogy_side="the good doctor",
    analogy="""  <p>A good doctor with a difficult diagnosis tells you <b>in person</b>, <b>early</b> and <b>plainly</b>: what they know and don't, what caused it, the <b>options</b>, and <b>what happens next</b>. You leave worried, but with a plan, and you trust them more, not less.</p>""",
    analogy_figs=[bn_analogy],
    map=[("Early", "On the forecast, a week before the board"),
         ("In person", "Priya the same day, then Femke with Priya"),
         ("What caused it", "Rotterdam's slot orders: 63 % of remaining refunds"),
         ("The options", "Banner and SMS fallback, or forced no-swap defaults"),
         ("The next step", "2.0 % by March, reported monthly")],
    how_side="early, in person: fact, cause, options, recommendation",
    how="""  <p>Grace told <b>Priya in person</b> the same day, and on <b>8 December</b> they told <b>Femke</b> together, a week before the board. Four parts: the <b>fact</b> (about 2.4 % against 2.0 %); the <b>cause</b> (Rotterdam's slot orders, with longer windows and notifications off, are 63 % of remaining refunds); the <b>options</b> (an in-app banner and SMS fallback in Rotterdam, aiming for 2.0 % by March; or forcing no-swap defaults, which cuts refunds but loses sales); and her <b>recommendation</b>. Femke took a range and the plan to the board. December ended at 2.4 %; <b>March reached 2.0 %</b>.</p>""",
    how_figs=[bn_how],
    steps=[("Tell as soon as it's likely", "On the forecast, not the final number."),
           ("Manager first, in person", "Then together to whoever must act."),
           ("State the fact plainly", "No softening adjectives."),
           ("Explain the cause", "With data, without blame."),
           ("Bring options with costs", "At least two, honestly."),
           ("Recommend and follow up", "What you'll do, and when you'll report.")],
    vocab=[("Forecast", "A projection of where a number will end up."),
           ("Miss", "A result short of a goal."),
           ("Root cause", "The underlying reason for a problem."),
           ("Range", "Telling a number as a span, with confidence."),
           ("Escalation", "Bringing a problem to people who can act."),
           ("No surprises", "Leaders hear important news early, from you.")],
    code=dict(file="product/notes/2026-12-08-femke.md", note="the follow-up note after telling Femke, 8 December 2026", plain=True, src="""
# Swap refund tickets: December will miss 2 %          Grace (with Priya) → Femke · 8 Dec 2026

FACT      Forecast for December ≈ 2.4 % of orders (Nov 2.6 %). Board was told 2 % by December.
CAUSE     63 % of remaining swap refunds are Rotterdam slot orders: longer windows,
          41 % of Rotterdam app users with notifications off. Amsterdam express is at 1.6 %.
OPTIONS   A  In-app banner + SMS fallback for Rotterdam slot swaps (3 weeks, Dee) → 2.0 % by March
          B  Default to "no swap" when there's no answer → refunds fall fast, ≈ 2 % fewer items sold
RECOMMEND A, with monthly reporting; B only if A misses February
FOR THE BOARD   "2.3–2.5 % in December; 2.0 % by March, with plan A"
"""),
    tools="tools: the forecast on the health page, a conversation, a short written follow-up with the same four parts.",
    gains=["<b>Trust kept</b>: no surprise at the board.",
           "<b>Time to act</b> a week earlier.",
           "<b>Options chosen</b> by the right people.",
           "<b>A plan</b> instead of an excuse.",
           "<b>Leaders defend you</b> when they're prepared."],
    losses=["<b>An uncomfortable conversation</b>.",
            "<b>The forecast might have been wrong</b>.",
            "<b>Some leaders</b> react badly at first.",
            "<b>Takes preparation</b>: cause and options."],
    baseline="Each line compares <b>waiting for the final number and letting the slide say it</b> to <b>telling early, in person, with fact, cause, options and a recommendation</b>.",
    ratings=[(3, 4, "Rotterdam customers get the fix sooner."),
             (2, 4, "The board saw a credible plan to 2 %."),
             (2, 5, "Cause shown with data."),
             (2, 4, "A week gained to act."),
             (3, 4, "One option chosen, one in reserve."),
             (2, 4, "Priya, Femke and the board share the facts."),
             (1, 5, "No surprises; trust grew."),
             (3, 3, "Neutral."),
             (3, 3, "An hour of preparation.")],
    pitfalls=[("Waiting for certainty", "“Let's see the final number.”", "tell on the forecast."),
              ("Email at night", "Read alone, without context.", "in person, then a note."),
              ("No cause, no plan", "Just the miss.", "fact, cause, options, recommendation."),
              ("Skipping your manager", "Straight to the CEO.", "manager first, then together.")],
    use=["Missed targets, slipping dates, failed tests.",
         "Incidents that affect customers or clients.",
         "When a promise made by someone else won't hold.",
         "Before any meeting where the news would surprise."],
    skip=["Never; only how early you can tell changes."],
    related=["<b>Managing up</b> (this volume)", "<b>The quarterly product review</b> (this volume)", "<b>Bets, not promises</b> (Vol. 2)", "<b>Presenting to executives</b> (Ana, book 1 vol. 3)"],
    quiz=[("When should bad news be delivered?", "As soon as it's likely, on the forecast."),
          ("In what order?", "Your manager first, in person; then together to whoever must act."),
          ("What are the four parts?", "Fact, cause, options with costs, recommendation."),
          ("What happened next?", "December ended at 2.4 %; March reached 2.0 % with the banner and SMS fallback.")],
    try_it="Think of one number or date you own that's likely to miss. Write the four parts (fact, cause, options, recommendation) in five lines, and book fifteen minutes with your manager this week.",
    remember="Be the <span class=\"hl\">good doctor</span>: early, in person, with a <span class=\"hl\">plan</span>.",
    sources=["Kim Scott, <i>Radical Candor</i> (2017).",
             "Douglas Stone, Bruce Patton and Sheila Heen, <i>Difficult Conversations</i> (1999).",
             "John Gabarro and John Kotter, “Managing Your Boss”, <i>HBR</i> (1980).",
             "Ben Horowitz, <i>The Hard Thing About Hard Things</i> (2014)."],
)

# ------------------------------------------------------------------ 15 Disagree and Commit
dc_problem = Doodle(760, 280, "Doodle of February 2027. Femke wants Larder Plus, a subscription with free delivery for 7.99 euros a month, launched before Antwerp. Grace thinks Antwerp in French and the remaining swap work matter more this spring. The decision is Femke's. Grace could argue forever, comply half-heartedly, or say it once and then make Plus work.",
                    "Femke wants Larder Plus before Antwerp; Grace disagrees. It's Femke's call. Argue forever, comply half-heartedly, or something better?")
dc_problem.box(20, 40, 320, 90, "Femke", "y", sub="Larder Plus, before Antwerp")
dc_problem.box(400, 40, 340, 90, "Grace", "blue", sub="Antwerp + swaps first")
dc_problem.note(380, 200, "argue forever, or sulk and comply?", "red", size=20)

dc_analogy = Doodle(760, 250, "Doodle of a rowing crew: in the boat, the cox decides the line. A rower who thinks the line is wrong says so once, clearly; then rows as hard as the rest. A rower who holds back half a stroke makes the boat slower than either line would.",
                     "In a rowing boat: say it once, clearly; then row as hard as the rest. Half a stroke slows everyone.")
dc_analogy.icon("ship", 30, 70, 1.1)
dc_analogy.box(150, 50, 280, 100, "say it once", "y", sub="clearly, with reasons")
dc_analogy.box(460, 50, 280, 100, "then row", "green", sub="as hard as the rest")
dc_analogy.note(450, 210, "half a stroke slows everyone", "pen")

dc_how = Doodle(760, 400, "How Grace disagreed and committed. 22 February: she made her case once, in writing, with numbers, at the decision meeting. 1 March: Femke decided for Plus. Grace committed: she planned Plus as her own bet, briefed the team without saying it was Femke's idea and not hers, and agreed with Femke how they'd know: Plus members order 30 percent more often than similar customers, and 5,000 members by September. A check-in date: 1 September. Antwerp's French work moved to May, with Femke's agreement.",
                 "Say it once, in writing. Once decided, commit fully, and agree how you'll know and when you'll look again.")
for i, (t, s, f) in enumerate([("22 Feb", "case made once, in writing", "y"), ("1 Mar", "Femke decides: Plus", "paper"), ("commit", "plan it as my own bet", "green")]):
    dc_how.box(14 + i * 248, 14, 236, 90, t, f, sub=s, size=17)
dc_how.box(14, 124, 732, 56, "how we'll know: +30 % order frequency · 5,000 members by Sep", "blue", size=15)
dc_how.box(14, 198, 732, 56, "check-in: 1 September 2027", "y", size=16)
dc_how.box(14, 272, 732, 56, "team briefed as our bet, not “Femke's idea”", "green", size=15)
dc_how.note(380, 366, "Antwerp in French moved to May, agreed", "pen", size=16)

DISAGREE = dict(
    slug="disagree-and-commit",
    kicker="a.k.a. “say it once, then row”",
    tldr="When a decision isn't yours to make and you disagree, <b>say so once, clearly</b>: in the decision meeting, ideally in writing, with your reasons and evidence. Once it's decided, <b>commit fully</b>: plan it as your own, brief your team without distancing yourself, and do your best work on it. Protect yourself and the company by agreeing <b>how you'll know</b> whether it worked and <b>when you'll look again</b>. Half-hearted compliance is worse than either option.",
    chips=[("Family", "hard moments"), ("Origin", "Intel (Andy Grove); popularised by Amazon's leadership principles"), ("Lives in", "a written case before the decision, and agreed success measures after"), ("Pairs with", "decision rights, bets not promises, OKRs")],
    problem_side="Larder, 1 March 2027",
    problem="""  <p class="lead">Femke wants <b>Larder Plus</b>, a subscription with free delivery for <b>€7.99 a month</b>, launched before Antwerp. Grace thinks <b>Antwerp in French</b> and the remaining swap work matter more this spring. <span class="hl-pink">The decision is Femke's.</span> Grace could argue forever, comply half-heartedly, or say it once and then make Plus work.</p>
  <ul>
    <li>Endless arguing stalls everyone.</li>
    <li>Half-hearted delivery makes any decision fail.</li>
    <li>Silence loses the information the decider needed.</li>
  </ul>""",
    problem_figs=[dc_problem],
    analogy_side="the rowing crew",
    analogy="""  <p>In a <b>rowing boat</b> the cox decides the line. A rower who thinks it's wrong <b>says so once</b>, clearly, with reasons. Then they <b>row as hard as the rest</b>. A rower who holds back half a stroke makes the boat slower than either line would have.</p>""",
    analogy_figs=[dc_analogy],
    map=[("The cox", "Femke, who owns the decision"),
         ("Saying it once", "Grace's written case on 22 February"),
         ("Rowing as hard as the rest", "Planning Plus as her own bet"),
         ("Half a stroke", "Briefing the team as “Femke's idea”"),
         ("Checking the line later", "Success measures and a 1 September check-in")],
    how_side="say it once, then commit, with a way to know",
    how="""  <p>On <b>22 February</b> Grace made her case <b>once</b>, in writing, with numbers, at the decision meeting. On <b>1 March</b> Femke decided for Plus. Grace <b>committed</b>: she planned Plus as her own bet, briefed the team <b>without</b> “it was Femke's idea”, and agreed with Femke <b>how they'd know</b>: Plus members order 30 % more often than similar customers, and 5,000 members by September, with a <b>check-in on 1 September</b>. Antwerp's French work moved to May, agreed with Femke.</p>""",
    how_figs=[dc_how],
    steps=[("Know who decides", "Decision rights first."),
           ("Make your case once", "In the decision meeting, in writing, with evidence."),
           ("Accept the decision", "Out loud, once it's made."),
           ("Commit fully", "Plan it as your own; brief the team without distance."),
           ("Agree how you'll know", "Success measures and a check-in date."),
           ("Revisit on evidence", "At the check-in, not in the corridor.")],
    vocab=[("Disagree and commit", "Stating disagreement, then fully supporting the decision."),
           ("Decision owner", "The person who makes the final call."),
           ("Malicious compliance", "Doing what was decided in a way designed to fail."),
           ("Success measure", "A number that shows whether a decision worked."),
           ("Check-in", "A date to look at the evidence again."),
           ("Escalation", "Taking a disagreement higher (rarely right after a decision).")],
    code=dict(file="product/decisions/2027-03-larder-plus.md", note="the decision note, 1 March 2027", plain=True, src="""
# Decision: Larder Plus before Antwerp's French release           owner: Femke · 1 Mar 2027

Options considered (Grace's case, 22 Feb)
  A  Larder Plus (free delivery, €7.99/month) in June, Antwerp French in May  ← chosen
  B  Antwerp French + Rotterdam swaps first, Plus in Q4
Grace's view   B: Antwerp is a board commitment; swaps still 2.0 %. Recorded, not repeated.
Decision       A (Femke). Grace owns the Plus plan.
How we'll know Plus members order ≥ 30 % more often than similar non-members (8 weeks)
               ≥ 5,000 members by 1 Sep 2027 · cost per order not above today's
Check-in       1 Sep 2027, with Femke, Priya, Marco, Grace
"""),
    tools="tools: a written case before the decision, a decision note with success measures, a check-in in the calendar.",
    gains=["<b>Decisions move</b>, not stall.",
           "<b>The decider hears</b> the counter-case.",
           "<b>Full effort</b> on what's chosen.",
           "<b>A fair test</b>: measures agreed in advance.",
           "<b>Trust</b> both ways."],
    losses=["<b>Working hard on something</b> you doubted.",
            "<b>Your view may be right</b>, later.",
            "<b>Needs genuine commitment</b>, not acting.",
            "<b>Not for ethical issues</b>: those need escalation."],
    baseline="Each line compares <b>arguing forever or complying half-heartedly</b> to <b>making the case once, committing fully, and agreeing how and when to judge it</b>.",
    ratings=[(3, 3, "Depends on the decision."),
             (2, 4, "Success measures tie Plus to business numbers."),
             (2, 4, "The counter-case was heard with data."),
             (2, 4, "A check-in date instead of corridor debates."),
             (2, 4, "One plan, fully staffed."),
             (2, 4, "The team knows the why and the measures."),
             (1, 5, "Femke trusts Grace with decisions she argued against."),
             (3, 4, "Work starts the next day."),
             (2, 4, "One written case, then on with it.")],
    pitfalls=[("Arguing after the decision", "Reopening it in every meeting.", "say it once; revisit at the check-in."),
              ("Silent disagreement", "Nodding, then doubting.", "say it in the meeting, in writing."),
              ("Distancing", "“Femke wants this.”", "brief it as our bet."),
              ("No measures", "Never knowing who was right.", "agree how you'll know.")],
    use=["Decisions owned by someone else that you doubt.",
         "Strategic choices between good options.",
         "When debate has stopped adding information.",
         "Teams that keep relitigating decisions."],
    skip=["Ethical, legal or safety concerns: escalate instead."],
    related=["<b>Decision rights</b> (Ana, book 1 vol. 2)", "<b>Bets, not promises</b> (Vol. 2)", "<b>OKRs</b> (Vol. 4)", "<b>Managing up</b> (this volume)"],
    quiz=[("When do you state your disagreement?", "Once, in the decision meeting, ideally in writing."),
          ("What does committing fully mean?", "Planning it as your own, briefing without distance, doing your best work."),
          ("How did Grace and Femke agree to judge Plus?", "Order frequency +30 % and 5,000 members by September, checked on 1 September."),
          ("When should you not disagree and commit?", "On ethical, legal or safety concerns: escalate instead.")],
    try_it="Think of a decision you disagreed with. Write your case in five lines as you would have before it was made. Then write how you'd know if the decision worked and when you'd look again, and share that, not the case.",
    remember="Say it <span class=\"hl\">once</span>, then <span class=\"hl\">row</span> as hard as the rest.",
    sources=["Andy Grove, <i>High Output Management</i> (1983).",
             "Jeff Bezos, Amazon shareholder letter (2016), “disagree and commit”.",
             "Patrick Lencioni, <i>The Five Dysfunctions of a Team</i> (2002).",
             "Annie Duke, <i>Thinking in Bets</i> (2018)."],
)

NOTES = [NEGOTIATE, FIXED, BADNEWS, DISAGREE]
