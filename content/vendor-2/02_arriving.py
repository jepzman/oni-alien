# Series 5 · On the Client's Floor · Vol. 2 · Signing and Starting · Arriving (notes 6–10).
import math
from datetime import date

# ------------------------------------------------------------------ 06 What Do We Do on Day One?
d1_problem = Doodle(760, 250, "Doodle of Monday 5 July 2027, 08:30, the reception of The Grid. Six Wrenfield people with visitor passes. Nobody has booked desks. They are given room 19C, a glass meeting room nicknamed the goldfish bowl, with eight chairs and no screens, and an escort to the toilets.",
                    "Day one, 08:30: six visitor passes, room 19C, and an escort to the toilets.", exact=True)
d1_problem.box(24, 30, 420, 190, None, "blue", rx=4)
d1_problem.head(234, 60, "room 19C · “the goldfish bowl”", size=19)
for i in range(6):
    d1_problem.circle(80 + i * 62, 140, 20, "y")
d1_problem.note(234, 200, "8 chairs · no screens · glass walls", "pen", size=17)
d1_problem.box(480, 30, 260, 80, "visitor passes", "pink", sub="escort required", size=19, subsize=16)
d1_problem.box(480, 130, 260, 90, "desks booked", "paper", sub="0", size=19, subsize=20)

d1_how = Doodle(760, 320, "Wrenfield's first-week plan. Monday: inductions, meet Elaine, walk the building. Tuesday: meet the people who will judge the work, Hollis, Bert, Kofi, the MetroVolt test manager. Wednesday: listen, three customer service calls with Pip's team. Thursday: the access tracker, and the kick-off rehearsal. Friday: the first Friday note to Elaine, three lines. A rule written on the whiteboard: learn the building before trying to change anything.",
                "A plan for the first week: listen first, meet the judges, and send a three-line note on Friday.", exact=True)
days = [("Mon", "inductions · Elaine · walk the floors"), ("Tue", "meet the judges: Hollis, Bert, Kofi, test"), ("Wed", "listen: 3 calls with Customer Ops"),
        ("Thu", "access tracker · kick-off rehearsal"), ("Fri", "the Friday note: 3 lines to Elaine")]
for i, (d, t) in enumerate(days):
    y = 14 + i * 50
    d1_how.box(14, y, 80, 42, d, "y", size=18, rx=4)
    d1_how.box(104, y, 642, 42, t, "paper", size=17, rx=4)
d1_how.note(380, 300, "learn the building before you try to change anything", "red", size=19)

DAY_ONE = dict(
    slug="day-one", date=date(2027, 7, 5), meta="day 1 on site", where="FL 19",
    kicker="a.k.a. “mobilisation” and the first week on the client's site",
    tldr="On day one you're a visitor in someone else's house, and everyone is watching how you behave. Arrive with a <b>first-week plan</b>: meet the client's programme director, <b>meet the people who'll judge your work</b>, spend time <b>listening</b> to the business, start tracking what you're waiting for, and end the week with a <b>three-line note</b>. Learn the building before you try to change anything.",
    chips=[("Family", "arriving"), ("Lives in", "delivery/lodestar/first-week.md"), ("Pairs with", "access, the kick-off, mapping the client")],
    problem_side="The Grid, Monday 5 July 2027",
    problem="""  <p class="lead">The contract was signed on <b>Wednesday 30 June</b>. On <b>Monday 5 July</b> at 08:30, six people from Wrenfield arrive at The Grid's reception: Ines, Callum, Hana, Bilal, Oskar and Lottie. They get <b>visitor passes</b>. Nobody has booked desks.</p>
  <ul>
    <li>Facilities finds them <b>room 19C</b>, a glass meeting room everyone calls “the goldfish bowl”: eight chairs, no screens, visible from the whole floor.</li>
    <li>They need an escort to reach the toilets. <span class="hl-pink">Laptops “should be ready this week”.</span></li>
    <li>Lottie asks what they're supposed to do today. Hana suggests starting the design. Ines says no.</li>
  </ul>""",
    problem_figs=[d1_problem],
    sides=dict(client=("floor 19 watches", "<p>Thirty MetroVolt people on floor 19 have heard “Lodestar” for months and “Orion” for years. They're watching six strangers in a glass room. Are these the people who'll <b>replace their system</b>, or their <b>jobs</b>? Do they say good morning?</p>", "Here we go again."),
                vendor=("Ines and the team", "<p>Wrenfield has no laptops, no access and no desks. It does have five days of <b>first impressions</b> that can't be repeated, and people it can meet without any system at all.</p>", "No laptops. Perfect week for listening.")),
    sides_after="The first week is the only time nobody expects you to know anything. Use it to ask.",
    analogy_side="the new neighbour",
    analogy="""  <p>When you move into a new street, you don't start by redesigning your neighbour's garden. You learn <b>where the bins go and on which day</b>, say hello to the person who's lived there forty years, and find out who to ask when the water goes off. In a month, people listen to your ideas because they've met you.</p>""",
    map=[("Where the bins go", "How meetings, rooms and approvals really work on floor 19"),
         ("The neighbour of forty years", "Bert, 31 years on MAVIS"),
         ("Who to ask when the water goes off", "Who fixes access, rooms, passes"),
         ("Redesigning their garden on day one", "Starting the design before you've listened"),
         ("Saying hello", "The Friday note, and good morning to floor 19")],
    how_side="a first-week plan: listen, meet the judges, write three lines",
    how="""  <p>Ines arrived with a <b>first-week plan</b> on one page. <b>Monday</b>: inductions, an hour with Elaine, a walk around floors 19, 14 and 2 (where the customer service teams sit). <b>Tuesday</b>: meet the people who'll judge Wrenfield's work: Hollis (architecture), <b>Bert Ogundipe</b> (31 years on MAVIS), Kofi (metering), MetroVolt's test manager. Each meeting has one question: <i>“What would make Lodestar a success for you, and what are you worried about?”</i></p>
  <p><b>Wednesday</b>: listening. Bilal and Lottie sit with Customer Operations (Pip's analysts take them) and listen to three customer calls, two of which are about wrong addresses. <b>Thursday</b>: the access tracker (next note) and a rehearsal for the kick-off. <b>Friday</b>: the first <b>Friday note</b> to Elaine, three lines: <i>done / learned / need</i>.</p>
  <p>And one rule on the whiteboard in 19C: <b>learn the building before trying to change anything</b>. Hana's design stays in her notebook until she's met Bert.</p>""",
    how_figs=[d1_how],
    steps=[("Write the first-week plan before you arrive", "One page, day by day."),
           ("Meet the client lead on day one", "An hour, their agenda."),
           ("Meet the people who'll judge your work", "One question: success and worries."),
           ("Listen to the business", "Sit with the users of the system you're replacing."),
           ("Track what you're waiting for", "Access, desks, passes: from day one."),
           ("End the week with three lines", "Done, learned, need.")],
    vocab=[("Mobilisation", "Getting a team ready and in place to start."),
           ("Induction", "The client's introduction: building, safety, rules, systems."),
           ("Stakeholder interview", "A short conversation to learn someone's goals and worries."),
           ("Friday note", "A short weekly message: done, learned, need."),
           ("Goldfish bowl", "Working where everyone can see you; behave accordingly."),
           ("First impressions", "The few days when people decide what you're like.")],
    code=dict(file="delivery/lodestar/first-week.md", note="Ines · written Fri 2 Jul, used Mon 5 Jul 2027", src="""
FIRST WEEK · LODESTAR · 5–9 July 2027 · room 19C

Mon  08:30 reception · inductions · 11:00 Elaine (her agenda) · walk floors 19, 14, 2
Tue  meet the judges (30 min each, one question each):
     Hollis · Bert Ogundipe · Kofi Asante · MetroVolt test manager · Nkem
     "What would make Lodestar a success for you, and what worries you?"
Wed  listen: Bilal + Lottie with Customer Ops (3 calls) · Ines + Hana with Bert
Thu  access tracker (laptops, VPN, MAVIS, badges) · kick-off rehearsal
Fri  Friday note to Elaine, 3 lines: done / learned / need

rules  learn the building before changing anything · say good morning to floor 19
       no design until we've met Bert · write down every name
"""),
    contract=dict(side="what the contract says about arriving", doc="Lodestar SOW · §4 and Appendix C", date="signed 30 June 2027", stamp="day 1",
                  clauses=[("4.1", "The Services commence on 5 July 2027 (the Start Date). Milestone dates are measured from the Start Date.", "dates run from today, laptops or not."),
                           ("D-05", "MetroVolt provides 12 laptops, network accounts and VPN access within 10 Working Days of the Start Date.", "Friday 16 July. starting the tracker today.")],
                  plain="the clock starts on the start date, whether or not you can work. Day one is when you start recording what you're waiting for."),
    health=dict(now="a",
                g=("you've worked there before", ["Re-meet people; say what's new.", "Shorter first week.", "Still listen first."]),
                a=("new to the client", ["A day-by-day first week.", "Meet the judges, one question each.", "Three lines on Friday."]),
                r=("hostile floor", ["Over-invest in listening.", "Be visibly polite and visibly useful.", "No design until people have been heard."])),
    pressure=dict(level=2, title="the goldfish bowl", cost="a glass room · no laptops · thirty curious people",
                  items=["Doing nothing visible feels terrible. Listening is work; write down what you learn.", "Juniors feel it most. Give Lottie a job on day one (the names list) so she's not just sitting."]),
    baseline="Each line compares <b>starting the design on day one</b> with <b>a first-week plan: listen, meet the judges, three lines on Friday</b>.",
    ratings=[(2, 4, "Floor 19 meets people who ask before they change things."),
             (3, 4, "Everyone has a job, even without laptops."),
             (3, 3, "Neutral."),
             (3, 4, "The judges' success criteria are written down."),
             (2, 4, "The design waits for Bert."),
             (2, 4, "Worries collected in week one."),
             (2, 3, "The Friday note starts a paper trail."),
             (3, 3, "A week before any design work."),
             (4, 4, "A one-page plan.")],
    pitfalls=[("Designing on day one", "A solution before anyone's been heard.", "listen first; meet the judges."),
              ("Waiting for laptops", "Five days lost.", "people don't need laptops."),
              ("Only meeting the sponsor", "The judges are the people below.", "meet Hollis, Bert, Kofi, the tester."),
              ("Behaving like visitors", "Huddled in the glass room.", "walk the floors; say good morning."),
              ("Silence on Friday", "The client doesn't know what happened all week.", "three lines.")],
    use=["The first week on any client site.", "A new team joining an existing programme.", "When access is late (it usually is)."],
    skip=["Never skip it; shorten it if you know the client well."],
    related=["<b>Why Can't We Log In?</b> (next note)", "<b>Who Really Decides Here?</b> (this volume)", "<b>How Do We Set the Rules at Kick-off?</b> (this volume)", "<b>Forty New People on Monday</b> (Eli, vol. 1)"],
    quiz=[("What's the one question for each “judge”?", "What would make Lodestar a success for you, and what worries you?"),
          ("Why listen to customer calls in week one?", "To learn the business problem the system serves; two of three were about wrong addresses."),
          ("What are the three lines of a Friday note?", "Done, learned, need."),
          ("Why no design until the team had met Bert?", "He knows MAVIS best; designing before hearing him risks the wrong design and an offended expert."),
          ("When do milestone dates start counting?", "From the start date, whether or not the team can work.")],
    quiz_sit=[("By Wednesday the team is restless and Hana starts sketching the target architecture on the glass wall of 19C. What do you do?", "Ask her to move it to her notebook for now: the whole floor can see that glass. Book her time with Bert first, and promise the whiteboard after.")],
    try_it="Plan your first week on a new project or team, day by day. Who will judge your work? What one question would you ask each of them? What would your three-line Friday note say?",
    remember="On day one you're a guest. <span class=\"hl\">Listen first</span>, <span class=\"hl\">meet the judges</span>, and say what you learned on Friday.",
    late=dict(when="Mon 5 July 2027 · 21:45 · hotel near The Grid",
              lines=["Day one. Visitor passes. An escort to the toilets. A glass room the whole floor can see into.",
                     "Elaine gave us an hour and spent forty minutes on Orion. She needed to say it to someone.",
                     "Tomorrow: Bert. Hana's design stays in her notebook until then. She's counting the hours."]),
    sources=["Michael Watkins, <i>The First 90 Days</i> (2003).",
             "Peter Block, <i>Flawless Consulting</i> (3rd ed., 2011): entry and contracting.",
             "Gerald Weinberg, <i>The Secrets of Consulting</i> (1985)."],
)

# ------------------------------------------------------------------ 07 Why Can't We Log In?
ap_problem = Doodle(760, 250, "Doodle of the access tracker on 2 August 2027, day 29. Dependency D-05 promised laptops and VPN within ten working days, by 16 July. Laptops arrived on day 23, 27 July. VPN and contractor badges are expected on 4 August. MAVIS read access is still waiting. A counter shows eleven working days late and about 46,000 pounds of idle time.",
                    "D-05 said 10 working days. Laptops came on day 23. MAVIS access still waiting.", exact=True)
rows = [("laptops", "promised 16 Jul", "came 27 Jul", "pink"), ("VPN", "promised 16 Jul", "due 4 Aug", "pink"),
        ("badges", "—", "due 4 Aug", "y"), ("MAVIS read", "promised 16 Jul", "waiting", "pink")]
for i, (a, b, c, fill) in enumerate(rows):
    y = 20 + i * 46
    ap_problem.box(14, y, 160, 38, a, "paper", size=17, rx=4)
    ap_problem.box(184, y, 200, 38, b, "paper", size=16, rx=4)
    ap_problem.box(394, y, 160, 38, c, fill, size=16, rx=4)
ap_problem.box(574, 20, 172, 176, "11 days", "pink", sub="≈ £46k idle", size=26, subsize=17)
ap_problem.note(380, 232, "a dependency is only useful if someone counts it", "red", size=19)

ap_how = Doodle(760, 300, "Three moves for late access. Track it daily: a shared tracker with each request, the date promised, the date delivered, and who is chasing it at MetroVolt. Price it: every idle day costs about 4,200 pounds, written in the tracker. Claim it: a relief notice under clause 3.4 on 30 July, eleven working days. And work around it in public: interviews, document reading, workshops on paper, all listed in the Friday note.",
                "Track it daily, price it, claim it calmly, and show the work you did anyway.", exact=True)
for i, (h, sub, fill) in enumerate([("track", "daily, shared", "y"), ("price", "≈ £4.2k / idle day", "paper"), ("claim", "relief notice RN-01", "blue"), ("work around", "in public", "green")]):
    ap_how.box(14 + i * 186, 30, 172, 100, h, fill, sub=sub, size=22, subsize=16)
ap_how.box(14, 160, 732, 90, "meanwhile, without systems", "paper", sub="18 interviews · 40 MAVIS documents read · 3 paper workshops · the 02:10 job drawn by hand with Bert", size=19, subsize=15)
ap_how.note(380, 284, "the client should see the cost and the effort at the same time", "pen", size=18)

ACCESS = dict(
    slug="access-purgatory", date=date(2027, 8, 2), meta="day 29 on site", where="FL 19",
    kicker="a.k.a. “onboarding delays”, the first dependency to slip",
    tldr="Laptops, accounts, badges and system access are the first <b>dependency</b> on almost every client project, and the first to slip. Treat them like any other dependency: a <b>tracker</b> with dates promised and delivered, a <b>price</b> per idle day, a calm <b>relief notice</b> under the contract, and visible <b>work-arounds</b> so nobody thinks you were idle. Do it without blame: the person chasing your laptop isn't the person who lost it.",
    chips=[("Family", "arriving"), ("Lives in", "delivery/lodestar/access-tracker.md"), ("Pairs with", "assumptions, first status report, the baseline")],
    problem_side="The Grid, floor 19, 2 August 2027",
    problem="""  <p class="lead">Dependency <b>D-05</b> says MetroVolt provides <b>12 laptops, accounts and VPN within 10 working days</b> of the start date: by <b>Friday 16 July</b>. On <b>day 23, Tuesday 27 July</b>, the laptops arrive. VPN and contractor badges are promised for 4 August. Read access to MAVIS: no date.</p>
  <ul>
    <li>Discovery is a 14-week plan. Eleven working days are gone. <span class="hl-pink">Nobody has written down why.</span></li>
    <li>Graham asks from Leeds: “What have they been doing for three weeks?”</li>
    <li>MetroVolt's IT service desk lost the first laptop request in a queue reorganised by Horizon. The person now chasing it, Yusuf in IT, is apologetic and overloaded.</li>
  </ul>""",
    problem_figs=[ap_problem],
    sides=dict(client=("Elaine and MetroVolt IT", "<p>Elaine is embarrassed: Wrenfield's first weeks are being wasted by her own IT. She's also wary: a late dependency is how Orion's vendor started its change requests. She wants it fixed and <b>doesn't want it used as a weapon</b>.</p>", "Please don't make this into an Orion-style claim."),
                vendor=("Callum and Ines", "<p>Wrenfield is paying six people to wait, at a fixed price. The contract gives relief, day for day, for late dependencies, but only if Wrenfield <b>claims it promptly and shows the facts</b>. It also needs Graham to see that the team was working.</p>", "Count it, claim it, and keep working where we can.")),
    sides_after="A relief notice isn't an accusation. It's how both sides keep the plan honest when one of them is late.",
    analogy_side="the plumber who can't get into the flat",
    analogy="""  <p>A plumber booked for Monday finds the building's door code doesn't work, and the caretaker is off until Thursday. A good plumber <b>notes the time</b>, texts the customer a photo of the locked door, <b>moves the finish date</b> by the days lost, and meanwhile measures up from outside and orders the parts. Nobody argues on Thursday.</p>""",
    map=[("The door code that doesn't work", "Laptops, VPN, MAVIS access"),
         ("Noting the time", "The access tracker"),
         ("Texting a photo of the locked door", "The Friday note and the tracker, shared"),
         ("Moving the finish date by the days lost", "Relief notice RN-01, 11 working days"),
         ("Ordering parts from outside", "Interviews, documents, paper workshops")],
    how_side="track, price, claim, and work around",
    how="""  <p><b>Track it.</b> From day one Callum keeps an <b>access tracker</b> shared with Elaine: each request, the date promised, the date delivered, and who is chasing it at MetroVolt. It's updated every morning at 09:00 and takes four minutes.</p>
  <p><b>Price it.</b> Next to it, one line: six people waiting cost about <b>£4,200 per working day</b>. By 30 July that's about <b>£46k</b>. Wrenfield doesn't invoice it (it's a fixed price); the number is there so everyone understands why the dates must move.</p>
  <p><b>Claim it.</b> On <b>30 July</b>, Callum sends <b>relief notice RN-01</b> under clause 3.4: D-05 delivered 11 working days late; discovery end moves from 26 November to <b>10 December</b>; no extra charge. It's one page, factual, with the tracker attached, and Ines walks Elaine through it the day before it arrives.</p>
  <p><b>Work around, in public.</b> Without systems, the team does <b>18 interviews</b>, reads <b>40 MAVIS documents</b>, runs three workshops on paper, and draws the 02:10 batch job by hand with Bert. All of it is in the Friday notes, so Graham's question has an answer.</p>""",
    how_figs=[ap_how],
    steps=[("Start the tracker on day one", "Request, promised, delivered, who's chasing."),
           ("Share it with the client lead", "Daily, without commentary."),
           ("Put a price on idle days", "Not to invoice: to explain why dates move."),
           ("Claim relief promptly", "A short notice under the right clause, after a conversation."),
           ("Work around visibly", "List what you did without systems."),
           ("Thank the people chasing it", "They're usually as frustrated as you are.")],
    vocab=[("Dependency", "Something the client must provide, by a date, for you to deliver."),
           ("Relief", "A contractual right to move dates (or costs) when the client is late."),
           ("Relief notice", "A written claim for relief, with facts and dates."),
           ("Idle time", "Paid time when the team can't do planned work."),
           ("Onboarding", "Getting people accounts, devices and access."),
           ("Work-around", "Useful work that doesn't need the missing thing.")],
    code=dict(file="delivery/lodestar/access-tracker.md", note="updated Mon 2 Aug 2027, 09:00", src="""
ACCESS TRACKER · LODESTAR (D-05: within 10 working days, i.e. by Fri 16 Jul)

item               requested  promised  delivered   late (wd)  chasing (MetroVolt)
laptops ×6         28 Jun     16 Jul    27 Jul      7          Yusuf, IT service desk
network accounts   28 Jun     16 Jul    27 Jul      7          Yusuf
VPN                28 Jun     16 Jul    (4 Aug)     13         Yusuf → network team
contractor badges  05 Jul     —         (4 Aug)     —          facilities, floor 2
MAVIS read access  28 Jun     16 Jul    —           12+        Hollis's team

idle cost ≈ £4,200 per working day (6 people) · to 30 Jul ≈ £46,000 (not invoiced)
RN-01 sent 30 Jul: 11 working days' relief on discovery (26 Nov → 10 Dec), £0
meanwhile: 18 interviews · 40 MAVIS documents · 3 paper workshops · 02:10 job drawn
"""),
    contract=dict(side="the relief clause, used for the first time", doc="Lodestar SOW · §3.4 and relief notice RN-01", date="30 July 2027", stamp="relief claimed",
                  clauses=[("3.4", "Where a Dependency is late, the Supplier is entitled to relief day for day on affected Milestones, provided the Supplier notifies MetroVolt within 10 Working Days of becoming aware of the delay.", "“within 10 working days”. if we'd waited for the August steering, we'd have lost it."),
                           ("RN-01", "D-05 was delivered 11 Working Days late. The Supplier claims relief of 11 Working Days on the Discovery end date (26 November → 10 December 2027). No change to the Charges is claimed.", "£0. the point is the date, not the money.")],
                  plain="relief usually has a deadline for claiming it. Claim promptly, factually and without blame, and say clearly when you're not claiming money."),
    health=dict(now="a",
                g=("trust is high", ["A conversation and an agreed note.", "Often no formal notice needed.", "Still keep the tracker."]),
                a=("they've been burned by claims", ["Talk first, then a one-page notice.", "Claim time, not money, where you can.", "Show the work you did anyway."]),
                r=("dependencies used as weapons", ["Formal notices, every time, on time.", "Facts only; tracker attached.", "Keep copies of every request."])),
    pressure=dict(level=3, title="waiting to work", cost="three weeks without systems · one sceptical managing director",
                  items=["Idle teams get anxious and bored. Give everyone a work-around job with a visible output.", "Yusuf isn't the problem. Bring him biscuits. (Sven's trick works for everyone.)"]),
    baseline="Each line compares <b>waiting quietly, then arguing in month three</b> with <b>a daily tracker, a priced idle day, a prompt relief notice and visible work-arounds</b>.",
    ratings=[(3, 4, "Elaine gets facts, a conversation and no money claim."),
             (2, 3, "Work-arounds keep people busy, but it's still frustrating."),
             (2, 4, "Eleven days of relief protect the fixed price."),
             (3, 3, "Neutral."),
             (3, 4, "Paper workshops with Bert improve the design."),
             (2, 4, "The first slipped dependency is visible on day 12."),
             (2, 5, "Tracker, notice and Friday notes on file."),
             (4, 4, "Four minutes a day."),
             (4, 4, "Light.")],
    pitfalls=[("Waiting quietly", "Then the lost weeks are yours.", "track from day one."),
              ("Claiming late", "The notice deadline passes.", "claim within the contract's window."),
              ("Claiming with blame", "The client hears Orion.", "facts, a conversation first, time not money."),
              ("Looking idle", "Your own firm assumes nothing happened.", "list the work-arounds every Friday."),
              ("Blaming the person chasing it", "You lose your only ally in IT.", "thank them, help them escalate.")],
    use=["Any client site with accounts, devices or access to arrange.", "Any dependency with a date.", "Fixed-price work, especially."],
    skip=["Never skip the tracker. Skip the formal notice if a written agreement on the dates is reached anyway."],
    related=["<b>What Are We Assuming?</b> (vol. 1)", "<b>What Do We Do on Day One?</b> (previous note)", "<b>What Goes in the First Status Report?</b> (this volume)", "<b>Forty New People on Monday</b> (Eli, vol. 1)"],
    quiz=[("Why price idle days if you won't invoice them?", "To explain why dates must move, in numbers everyone understands."),
          ("What did RN-01 claim?", "Eleven working days' relief on the discovery end date, and no money."),
          ("Why does the relief clause's deadline matter?", "Relief must be claimed within 10 working days of becoming aware of the delay, or it may be lost."),
          ("What did the team do without systems?", "Interviews, document reading, paper workshops, and drawing the 02:10 job with Bert."),
          ("Why talk to Elaine before sending the notice?", "So it arrives as agreed facts, not as a surprise claim.")],
    quiz_sit=[("Graham wants RN-01 to claim the £46k as well. What do you advise?", "Not on a fixed price, and not as the first notice of the relationship. Claim time, which protects the dates; record the cost in the tracker in case delays continue and a bigger claim is ever needed.")],
    try_it="List what you're waiting for from others on your current project. For each: when it was promised, when it arrived, and who's chasing it. What does a day of waiting cost? Who should know that number?",
    remember="Access is a dependency. <span class=\"hl\">Track it, price it, claim it calmly</span>, and <span class=\"hl\">show the work you did anyway</span>.",
    late=dict(when="Mon 2 August 2027 · 20:30 · hotel near The Grid",
              lines=["Laptops on day 23. VPN on Wednesday, they say. MAVIS: “soon”.",
                     "Walked Elaine through RN-01 before Callum sent it. She read “£0” twice and relaxed.",
                     "Brought Yusuf biscuits. He found the VPN request in a queue that no longer exists."]),
    sources=["UK Government, <i>Model Services Contract</i>: relief events.",
             "NEC4: early warnings and compensation events.",
             "Gene Kim et al., <i>The Phoenix Project</i> (2013)."],
)

# ------------------------------------------------------------------ 08 Who Really Decides Here?
mc_problem = Doodle(760, 260, "Doodle of MetroVolt's official org chart for Lodestar: Priya at the top as sponsor, Elaine as programme director, Hollis, Nkem, Kofi. Ines draws over it in red pen: Rupert and the Horizon board above Priya, Vexmoor whispering to Rupert, Ottoline Grey off to the side with a dotted line to everyone, Gareth owning the meter data, and Bert at the bottom with a thick line meaning he decides whether MAVIS data can be trusted.",
                    "The org chart, and the same chart after two weeks of listening, in red pen.", exact=True)
mc_problem.box(300, 20, 160, 50, "Priya", "y", sub="sponsor", size=18, subsize=14)
mc_problem.box(300, 100, 160, 50, "Elaine", "y", sub="programme", size=18, subsize=14)
for i, n in enumerate(["Hollis", "Nkem", "Kofi"]):
    mc_problem.box(180 + i * 140, 180, 120, 44, n, "paper", size=17)
mc_problem.line("M380 70 V100 M380 150 V165 M240 165 H520 M240 165 V180 M380 165 V180 M520 165 V180", thin=True)
mc_problem.box(560, 10, 186, 50, "Rupert + board", "pink", stroke="red", size=17)
mc_problem.box(560, 74, 186, 44, "Vexmoor", "pink", stroke="red", size=17)
mc_problem.box(14, 10, 200, 50, "Ottoline Grey", "pink", stroke="red", size=17)
mc_problem.box(14, 100, 200, 50, "Gareth: meters", "pink", stroke="red", size=17)
mc_problem.box(14, 200, 140, 50, "Bert", "pink", stroke="red", size=18)
mc_problem.arrow(154, 225, 300, 205, color="red", label="trusts the data?", lx=230, ly=250)

mc_how = Doodle(760, 320, "Ines's power map, on two axes: how much each person can affect Lodestar, from low to high, and whether they're for it, neutral, or against. High and for: Priya, Elaine. High and neutral: Rupert, Hollis, Bert. High and against: Gareth, who wanted the meter data in his own programme. Lower down: Nkem, Kofi, Vexmoor's Oliver, Ottoline. Each has a note of what they need: Priya, a win for Customer Ops; Hollis, to be asked; Bert, respect and a successor; Gareth, credit for the meter data.",
                "Who can affect it, where they stand, and what each of them needs.", exact=True)
mc_how.line("M60 280 H740 M60 280 V20", thin=True)
mc_how.note(400, 310, "for  ←—  neutral  —→  against", "pen", size=17)
mc_how.note(30, 150, "influence", "pen", size=16)
pts = [("Priya", 130, 50, "green"), ("Elaine", 170, 100, "green"), ("Rupert", 400, 40, "y"), ("Hollis", 360, 100, "y"), ("Bert", 450, 130, "y"),
       ("Gareth", 640, 70, "pink"), ("Nkem", 200, 200, "paper"), ("Kofi", 300, 220, "paper"), ("Oliver", 560, 190, "pink"), ("Ottoline", 420, 220, "paper")]
for n, x, y, fill in pts:
    mc_how.box(x - 50, y - 18, 100, 36, n, fill, size=16, rx=18)

MAPPING = dict(
    slug="mapping-the-client", date=date(2027, 7, 16), meta="day 12 on site", where="FL 19",
    kicker="a.k.a. “stakeholder and power mapping”, from outside",
    tldr="As a vendor you can see the client's politics but not touch them. The <b>org chart</b> tells you who reports to whom; it doesn't tell you <b>who decides</b>, who can <b>block</b>, and who is <b>listened to</b>. Spend the first weeks listening, then draw the real map: each person's <b>influence</b> on your project, <b>where they stand</b>, and <b>what they need</b>. Keep it private, update it monthly, and use it to decide whom to talk to, never to play games.",
    chips=[("Family", "arriving"), ("Lives in", "Ines's notebook (never in a shared folder)"), ("Pairs with", "governance, the client counterpart, the kick-off")],
    problem_side="The Grid, 16 July 2027",
    problem="""  <p class="lead">The contract's governance schedule shows a neat chart: <b>Priya</b> (sponsor) → <b>Elaine</b> (programme director) → Hollis, Nkem, Kofi. Twelve days on floor 19 have shown Ines a different picture.</p>
  <ul>
    <li>Since Horizon, <b>Rupert Thorne's board</b> approves anything Priya wants, and <b>Vexmoor</b> advises Rupert.</li>
    <li><b>Ottoline Grey</b>, the Chief of Staff, isn't on any Lodestar chart, yet every senior meeting Ines hears about was “checked with Ottoline” first.</li>
    <li><b>Gareth Pound</b> owns the smart-meter data Lodestar needs, and wanted Lodestar in his own Network Assets programme.</li>
    <li><b>Bert Ogundipe</b> has no title worth mentioning. <span class="hl-pink">If Bert says MAVIS data can't be trusted, nobody will argue with him.</span></li>
  </ul>""",
    problem_figs=[mc_problem],
    sides=dict(client=("MetroVolt's people", "<p>Inside MetroVolt, everyone knows the real map, and nobody writes it down. People are cautious about what a supplier hears: in a Horizon year, <b>being seen to brief the vendor</b> can be held against them.</p>", "We'll tell you what you need to know. Eventually."),
                vendor=("Ines", "<p>Ines needs to know whom to brief before a decision, whose worry will sink a design, and whose support matters. She can't ask directly (“who really decides here?”) without sounding political. So she listens, and draws.</p>", "I don't want to play the politics. I need to not be run over by them.")),
    sides_after="A vendor who ignores the client's politics gets surprised. A vendor who plays them gets thrown out. The map is for not being surprised.",
    analogy_side="the new teacher's seating plan",
    analogy="""  <p>A new teacher gets the official class list on day one. By week two she has her own <b>seating plan</b> in pencil: who the class listens to, who'll derail a lesson, who's quiet but brilliant, who needs to be asked rather than told. She never shows it to the class. She uses it to decide whom to talk to first.</p>""",
    map=[("The official class list", "The governance chart in the contract"),
         ("Who the class listens to", "Ottoline; Bert, on MAVIS data"),
         ("Who'll derail a lesson", "Gareth, who wanted Lodestar for himself"),
         ("Quiet but brilliant", "Bert"),
         ("Never shown to the class", "The map stays in Ines's notebook")],
    how_side="listen, then map influence, stance and need",
    how="""  <p>For two weeks Ines just notices: who is mentioned before decisions (“have you checked with…?”), who arrives late and is waited for, whose objections end a discussion, who is copied on emails and who is quietly removed from them.</p>
  <p>Then she draws a <b>power map</b>: up the side, <b>influence on Lodestar</b>; along the bottom, <b>for, neutral or against</b>. Priya and Elaine: high, for. Rupert, Hollis, Bert: high, neutral. <b>Gareth: high, against</b>. Nkem, Kofi, Ottoline lower; Vexmoor's Oliver lower but leaning against.</p>
  <p>The useful part is the third column: <b>what each person needs</b>. Priya needs a visible win for Customer Ops in a cut year. Hollis needs to be <b>asked</b>, not informed. Bert needs respect and a successor before he retires. Gareth needs <b>credit</b> for the meter data. Each need becomes an action: Hollis gets design questions before the design authority; Bert gets Lottie as his apprentice; Gareth's team is named on every Lodestar slide that shows meter data.</p>
  <p>The map lives in Ines's own notebook, not in a shared folder. It's updated on the first Friday of each month.</p>""",
    how_figs=[mc_how],
    steps=[("Start with the official chart", "Then listen for two weeks."),
           ("Notice who's mentioned before decisions", "“Have you checked with…?”"),
           ("Map influence and stance", "Two axes; be honest about the againsts."),
           ("Write what each person needs", "The useful column."),
           ("Turn needs into actions", "Ask Hollis; credit Gareth; respect Bert."),
           ("Keep it private, update monthly", "A map in a shared folder becomes a scandal.")],
    vocab=[("Power map", "A drawing of who influences a decision and how."),
           ("Stakeholder", "Anyone who can affect, or is affected by, the work."),
           ("Influence", "How much someone can change the outcome, whatever their title."),
           ("Stance", "For, neutral or against, and why."),
           ("Informal power", "Influence that doesn't come from position: knowledge, trust, access."),
           ("Gatekeeper", "Someone whose approval or knowledge others must pass through.")],
    code=dict(file="notebook/power-map-2027-07.md", note="Ines's notebook · Fri 16 Jul 2027 (private)", src="""
POWER MAP · LODESTAR · July 2027                       (private · update monthly)

who            influence  stance     needs                         my action
Priya Nair     high       for        a visible win in a cut year   pilot story for Customer Ops
Elaine Corbett high       for (wary) no surprises; not Orion       Thursday 1:1s; bad news early
Rupert Thorne  high       neutral    cost out; Horizon's story     the £1.9m mainframe line
Hollis Wade    high       neutral    to be asked, not informed     questions before every DA
Bert Ogundipe  high*      neutral    respect; a successor          Lottie as apprentice
Gareth Pound   high       against    credit for the meter data     his team named on every slide
Ottoline Grey  medium     unknown    —                             ask Elaine, carefully
Oliver Thane   medium     leaning    a role in Horizon's success   answer fully, on time
Nkem, Kofi     medium     for        numbers; meters not forgotten  monthly figures; Kofi at DA
* on MAVIS data, Bert's view ends every argument
"""),
    contract=dict(side="what the contract says about who decides", doc="Lodestar SOW · §8 governance and Schedule 7", date="signed 30 June 2027", stamp="official only",
                  clauses=[("8.1", "MetroVolt's Sponsor is the Head of Customer Operations. MetroVolt's Programme Director is MetroVolt's authorised representative for the day-to-day management of the Contract.", "Elaine signs. Priya sponsors. Rupert approves. the contract only knows two of them."),
                           ("8.5", "Instructions to the Supplier are valid only if given by MetroVolt's Programme Director or the Steering Committee.", "so Gareth can ask. only Elaine can instruct.")],
                  plain="the contract names who can instruct you, which protects you from everyone else's requests. It doesn't tell you who has influence. You need both maps: one for instructions, one for influence."),
    health=dict(now="a",
                g=("open client", ["The map is mostly the org chart.", "People tell you who decides.", "Still note the needs."]),
                a=("politics you can see but not touch", ["Listen for two weeks, then map.", "Turn needs into actions.", "Keep it private."]),
                r=("factions fighting over your project", ["Only take instructions per §8.5.", "Be scrupulously neutral.", "Write everything down."])),
    pressure=dict(level=3, title="reading the room", cost="two weeks of noticing · one person openly against",
                  items=["Knowing someone powerful is against you is stressful. Knowing what they need makes it a task, not a threat.", "Never repeat what you learned to map someone. You're a guest in their politics."]),
    baseline="Each line compares <b>working from the official org chart</b> with <b>a private power map of influence, stance and needs, updated monthly</b>.",
    ratings=[(3, 4, "People feel asked and credited."),
             (3, 4, "Fewer surprises at meetings."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Bert's view shapes the design early."),
             (2, 4, "Gareth's opposition is seen and worked on."),
             (3, 3, "Neutral; the map itself must never be shared."),
             (3, 3, "Two weeks of listening."),
             (4, 4, "Monthly update.")],
    pitfalls=[("Trusting the org chart", "The real decider isn't on it.", "listen for who's mentioned before decisions."),
              ("Asking “who really decides?”", "You sound political.", "notice instead."),
              ("Playing the politics", "Taking sides in a client's fight.", "map to avoid surprises, never to win games."),
              ("Sharing the map", "A list of who's “against” leaks.", "your notebook only."),
              ("Ignoring the experts", "Bert has no title and all the influence on data.", "map influence, not rank.")],
    grimoire=[(1, "hidden-thrones", "The Map of Hidden Thrones", "is the same idea from inside MetroVolt: Pip's version, with Ottoline at the centre."), (1, "empire-builder", "The Empire Builder", "is Gareth, seen by his own colleagues.")],
    use=["Any client with more than a handful of decision makers.", "A reorganisation is underway.", "Someone powerful seems against the project."],
    skip=["A tiny client where you work directly with the owner."],
    related=["<b>Who Decides What, and Where?</b> (next note)", "<b>How Do We Earn the Programme Director's Trust?</b> (this volume)", "<b>Stakeholder Map</b> (Ana, vol. 1)", "<b>Who Matters Most, and How Much?</b> (Sanne, vol. 5)"],
    quiz=[("What does a power map show that an org chart doesn't?", "Who influences the decision, where they stand, and what they need."),
          ("Why is the “needs” column the useful one?", "Each need becomes an action that turns opposition into neutrality or support."),
          ("Why keep the map private?", "A list of who's “against” would damage relationships if it leaked."),
          ("Who can give Wrenfield instructions under the contract?", "Only Elaine (the programme director) or the steering committee."),
          ("Why does Bert rank high on influence?", "On MAVIS data, his view ends every argument, whatever his title.")],
    quiz_sit=[("Gareth asks Hana directly to add a meter-data report “while she's in there”. What happens?", "Hana thanks him and says she'll raise it with Elaine, who can instruct under §8.5. Ines makes sure Gareth's team is credited when it's assessed, since credit is what he needs.")],
    try_it="Draw the people around your project on two axes: influence and stance. Add a third column: what each of them needs. Pick the most influential person against you and write one action that meets their need.",
    remember="The org chart shows <span class=\"hl\">who reports to whom</span>. Listen until you can draw <span class=\"hl\">who decides, who blocks, and what each one needs</span>.",
    late=dict(when="Fri 16 July 2027 · 22:20 · hotel near The Grid",
              lines=["Drew the map. Gareth is against us. He wanted Lodestar for himself.",
                     "Ottoline isn't on any chart, and everyone checks with her. I've never met her.",
                     "Bert has no title and the final word on data. Asked if Lottie could sit with him. He said yes before I finished the sentence."]),
    sources=["Jeffrey Pfeffer, <i>Power: Why Some People Have It and Others Don't</i> (2010).",
             "Peter Block, <i>Flawless Consulting</i> (2011).",
             "Project Management Institute, <i>PMBOK Guide</i>: stakeholder engagement."],
)

# ------------------------------------------------------------------ 09 How Do We Set the Rules at Kick-off?
ko_problem = Doodle(760, 250, "Doodle of the kick-off on Tuesday 13 July 2027 in the floor 2 auditorium: 34 people. Lord Varnish opens, unannounced, with a slide called the Lodestar Value Pyramid, which has five layers and no dates. Twenty minutes of the ninety are gone. In the back row, Bert folds his arms.",
                    "34 people, 90 minutes, and a pyramid with no dates.", exact=True)
ko_problem.line("M60 220 L200 30 L340 220 Z")
for i, t in enumerate(["synergy", "value", "trust", "data", "people"]):
    y = 98 + i * 27
    ko_problem.text(200, y, t, size=15)
ko_problem.note(200, 244, "the Lodestar Value Pyramid", "pen", size=18)
ko_problem.icon("clock", 400, 40, 1.2)
ko_problem.note(480, 74, "20 of 90 minutes gone", "red", anchor="start", size=19)
for i in range(10):
    ko_problem.circle(420 + (i % 5) * 60, 140 + (i // 5) * 50, 16, "paper")
ko_problem.note(600, 244, "Bert, back row, arms folded", "pen", size=17)

ko_analogy = Doodle(760, 210, "Doodle of a climbing team at the foot of a mountain, agreeing before they start: who leads each section, the signals for stop and go, what to do if someone is hurt, and the turn-back time. On the mountain there's no time to agree these things.",
                    "Agree the signals at the bottom. There's no time on the mountain.", exact=True)
ko_analogy.line("M40 190 L200 40 L300 120 L420 20 L560 190 Z")
for i, t in enumerate(["who leads", "stop / go", "if hurt", "turn back"]):
    ko_analogy.box(580, 14 + i * 46, 166, 38, t, "y", size=17, rx=6)

ko_how = Doodle(760, 330, "The kick-off agenda, rebuilt for the remaining seventy minutes. Ten minutes: why Lodestar, by Priya, in Customer Operations' words. Ten: the plan and the pilot gate. Fifteen: the top eight assumptions, walked through, each owner standing up. Ten: how we work, the Friday note, the access tracker, the change pool. Ten: how we disagree, three steps: say it in the room, write it in the decision log, escalate within a week. Fifteen: questions. Bert asks the first one.",
                "Purpose, plan, assumptions, ways of working, and how we'll disagree. Then questions.", exact=True)
agenda = [("why", "Priya · 10′", "y"), ("plan + pilot gate", "Callum · 10′", "paper"), ("8 assumptions", "owners stand · 15′", "pink"),
          ("how we work", "Ines · 10′", "paper"), ("how we disagree", "3 steps · 10′", "blue"), ("questions", "15′", "green")]
for i, (h, sub, fill) in enumerate(agenda):
    ko_how.box(14 + i * 124, 20, 116, 100, h, fill, sub=sub, size=16, subsize=14)
ko_how.box(14, 160, 732, 110, None, "blue", rx=8)
ko_how.head(380, 190, "how we disagree", size=20)
ko_how.text(380, 222, "1 · say it in the room   2 · write it in the decision log   3 · escalate within a week", size=17)
ko_how.text(380, 252, "never in the corridor, never by email to someone's boss", size=16)
ko_how.note(380, 310, "first question: Bert", "pen", size=19)

KICK_OFF = dict(
    slug="the-kick-off", date=date(2027, 7, 13), meta="day 9 on site", where="FL 2",
    kicker="a.k.a. “the programme kick-off”, the rules of the game",
    tldr="A kick-off isn't a launch party. It's the one meeting where <b>everyone</b> is in the room, so use it to agree the rules you'll need later: <b>why</b> the project exists (in the client's words), <b>the plan</b> and its gates, <b>the assumptions</b> (with owners standing up), <b>how we work</b>, and <b>how we disagree</b>. When someone senior eats the time, cut the agenda, not the rules.",
    chips=[("Family", "arriving"), ("Lives in", "delivery/lodestar/kick-off.pdf (12 slides)"), ("Pairs with", "assumptions, governance, the baseline")],
    problem_side="The Grid, floor 2 auditorium, 13 July 2027",
    problem="""  <p class="lead">The Lodestar kick-off is on <b>Tuesday 13 July</b>, 10:00 to 11:30, in the floor 2 auditorium: <b>34 people</b> from MetroVolt, Wrenfield and Halvorsen. Elaine chairs. At 10:02 <b>Lord Varnish</b> arrives, unannounced, and asks to “set the vision”.</p>
  <ul>
    <li>His slide is the <b>“Lodestar Value Pyramid”</b>: five layers (people, data, trust, value, synergy), no dates, no names.</li>
    <li>He speaks for <b>twenty minutes</b>. Wrenfield's agenda had ninety minutes of content for ninety minutes.</li>
    <li>In the back row, Bert Ogundipe folds his arms. He's sat through the Orion kick-off too. <span class="hl-pink">It also had a pyramid.</span></li>
  </ul>""",
    problem_figs=[ko_problem],
    sides=dict(client=("the 34 in the room", "<p>Most of MetroVolt's people want to know three things: <b>what changes for me</b>, <b>when</b>, and <b>whether this one will be different</b>. Senior people want to be seen to own it. Old hands like Bert are deciding, in the first hour, whether to invest in it.</p>", "Is this real, or another pyramid?"),
                vendor=("Ines", "<p>For Wrenfield, the kick-off is the only time it can say the rules <b>to everyone at once</b>: the assumptions, the change pool, how to raise a disagreement. If those don't land today, they'll be news in month five, and sound like excuses.</p>", "Cut slides. Keep the rules.")),
    sides_after="A senior person opening a kick-off is a gift, even with a pyramid: it shows the room the project matters. The job is to make sure the rules still fit in the time that's left.",
    analogy_side="the climbers at the foot of the mountain",
    analogy="""  <p>A climbing team agrees the important things <b>at the bottom</b>: who leads each section, the signals for stop and go, what happens if someone is hurt, the turn-back time. On the mountain, in the wind, there's no time to discuss them. A team that skips this to start climbing sooner usually regrets it halfway up.</p>""",
    analogy_figs=[ko_analogy],
    map=[("Who leads each section", "Governance and owners"),
         ("Signals for stop and go", "The pilot gate in month 9"),
         ("If someone is hurt", "The assumptions and what happens if one is false"),
         ("The turn-back time", "Escalation within a week"),
         ("Agreed at the bottom", "Said to all 34 people at the kick-off")],
    how_side="cut the agenda, not the rules",
    how="""  <p>At 10:22, with 68 minutes left, Ines passes Callum a note: <b>“Cut slides 3–6. Keep 7–12.”</b> What's kept:</p>
  <ul>
    <li><b>Why (10 min)</b>: Priya, in Customer Operations' words: two of every ten complaint calls are about wrong addresses; MAVIS can't fix them; Lodestar can.</li>
    <li><b>The plan (10 min)</b>: discovery to December, pilot in March, wave 1 in June, and the <b>pilot gate</b>: nothing goes further until 20,000 customers are live and reconciled.</li>
    <li><b>The top eight assumptions (15 min)</b>: each read aloud, and <b>the owner stands up</b>. Hollis stands for D-03 (with Sven). Yusuf stands for D-05, a little embarrassed. The room laughs, kindly.</li>
    <li><b>How we work (10 min)</b>: the Friday note, the access tracker, the change pool and who can instruct Wrenfield.</li>
    <li><b>How we disagree (10 min)</b>: three steps. Say it in the room; write it in the decision log; escalate within a week. <b>Never in the corridor, never by email to someone's boss.</b></li>
  </ul>
  <p>Questions: Bert asks the first one. <i>“When you find something in MAVIS you don't understand, who do you ask?”</i> Ines: <i>“You. And Lottie will write down the answer so nobody has to ask you twice.”</i> Bert unfolds his arms.</p>""",
    how_figs=[ko_how],
    steps=[("Plan the rules, not the slides", "Purpose, plan, assumptions, ways of working, disagreement."),
           ("Let the client say why", "In their words, with their numbers."),
           ("Make assumption owners stand up", "A name in a room beats a line in an appendix."),
           ("Say how you'll disagree", "Three steps, written down."),
           ("When time is eaten, cut slides", "Have the cut list ready before you start."),
           ("Leave room for the hard question", "And answer it plainly.")],
    vocab=[("Kick-off", "The first meeting of everyone involved, to agree purpose and rules."),
           ("Pilot gate", "A point where the programme stops unless the pilot meets its criteria."),
           ("Decision log", "A dated record of decisions, who made them and why."),
           ("Escalation path", "The agreed route for a disagreement nobody can settle locally."),
           ("Ways of working", "The habits and tools a team agrees to use."),
           ("Cut list", "Slides you'll drop if you run out of time, decided in advance.")],
    code=dict(file="delivery/lodestar/kick-off.md", note="as run · Tue 13 Jul 2027", src="""
KICK-OFF · LODESTAR · 13 Jul 2027 · floor 2 auditorium · 34 people

planned (90′)                       as run (68′ after the Value Pyramid)
1  welcome, Elaine          5′      Lord Varnish, Value Pyramid       20′
2  why, Priya              10′      why, Priya                        10′
3–6 Wrenfield, team, method 20′     CUT (team slide on the handout)
7  plan + pilot gate       10′      plan + pilot gate, Callum         10′
8  top 8 assumptions       15′      assumptions, owners stand         15′
9  how we work             10′      how we work, Ines                  8′
10 how we disagree         10′      how we disagree                   10′
11–12 questions            20′      questions                         15′

how we disagree: 1 say it in the room · 2 decision log · 3 escalate within a week
                 never in the corridor · never by email to someone's boss
first question (Bert): "when you find something in MAVIS you don't understand,
                        who do you ask?"   answer: "you, and Lottie writes it down"
"""),
    contract=dict(side="what the kick-off puts on the record", doc="Lodestar SOW · §8.3 and Schedule 7", date="signed 30 June 2027", stamp="minuted",
                  clauses=[("8.3", "The Parties shall hold a programme kick-off within 10 Working Days of the Start Date, at which the Supplier shall present the Assumptions and Dependencies and the governance arrangements.", "13 July is day 7 working. in time."),
                           ("Sch. 7, 4", "Disputes that cannot be resolved by the Programme Director and the Supplier's Engagement Manager within 5 Working Days shall be referred to the Steering Committee.", "“escalate within a week”, in plain words.")],
                  plain="many contracts require a kick-off and say what must be presented. Use the minutes: once the room has heard the assumptions and the escalation path, nobody can later say they didn't know."),
    health=dict(now="a",
                g=("trust is high", ["A shorter, warmer kick-off.", "Still the assumptions and disagreement rules.", "Celebrate a little."]),
                a=("burned before, sceptical veterans", ["Purpose in their words, rules in yours.", "Owners stand up.", "Answer the veteran's question plainly."]),
                r=("factions in the room", ["Rules first, vision later.", "Minutes circulated the same day.", "Name the escalation path twice."])),
    pressure=dict(level=3, title="the room", cost="20 lost minutes · 34 pairs of eyes · one folded pair of arms",
                  items=["A senior person going over time isn't an attack. Have the cut list ready so you can adapt calmly.", "Watch the veterans, not the seniors. Bert unfolding his arms was the result of the day."]),
    baseline="Each line compares <b>a launch party with a vision slide</b> with <b>a kick-off that agrees purpose, plan, assumptions, ways of working and disagreement</b>.",
    ratings=[(2, 4, "34 people heard the same rules."),
             (3, 4, "Everyone knows how to raise a problem."),
             (3, 4, "Assumptions heard by everyone, owners named."),
             (2, 4, "The pilot gate is public."),
             (3, 3, "Neutral."),
             (2, 4, "Owners stood up for their dependencies."),
             (2, 5, "Minuted, as the contract requires."),
             (3, 3, "Ninety minutes and a lot of preparation."),
             (4, 4, "One meeting.")],
    pitfalls=[("A launch party", "Vision and no rules.", "purpose, plan, assumptions, ways of working, disagreement."),
              ("No cut list", "A senior person over-runs and the rules are dropped.", "decide in advance what to cut."),
              ("The vendor explains the why", "It sounds like a sales pitch.", "the client says why, in their words."),
              ("Assumptions in an appendix", "Nobody remembers them.", "read aloud, owners stand."),
              ("No disagreement rules", "Disagreements go to corridors and bosses.", "three steps, minuted.")],
    grimoire=[(2, "meeting-lich", "The Meeting Lich", "is what a kick-off becomes when it has no rules: meeting #112, agenda TBD.")],
    use=["The start of any programme with several teams or firms.", "When people have been burned by a previous kick-off.", "When the contract requires one."],
    skip=["A two-person engagement: a kick-off conversation and an email of the rules will do."],
    related=["<b>What Are We Assuming?</b> (vol. 1)", "<b>Who Decides What, and Where?</b> (next note)", "<b>Who Really Decides Here?</b> (this volume)", "<b>Should This Project Exist?</b> (Sanne, vol. 2)"],
    quiz=[("What five things should a kick-off agree?", "Why, the plan, the assumptions, how we work and how we disagree."),
          ("Why should the client explain the “why”?", "From the vendor it sounds like a pitch; from the client it's a purpose."),
          ("Why ask assumption owners to stand up?", "A name in a room is remembered; a line in an appendix isn't."),
          ("What are the three steps for disagreeing?", "Say it in the room, write it in the decision log, escalate within a week."),
          ("What did Ines cut when time ran short?", "Wrenfield's own slides about itself (3–6); the rules stayed.")],
    quiz_sit=[("Lord Varnish asks at the end: “Where does the Value Pyramid fit in your plan?” What do you say?", "Thank him, and connect it to something concrete: the pyramid's “data” and “trust” layers are what the pilot gate tests in March. Offer to show him the pilot results first.")],
    try_it="Plan a kick-off for your next project in five parts: why, plan, assumptions, how we work, how we disagree. Which slides would you cut if a senior person took twenty minutes? Write the cut list now.",
    remember="A kick-off is where <span class=\"hl\">everyone hears the rules once</span>. When time runs out, <span class=\"hl\">cut the slides, not the rules</span>.",
    late=dict(when="Tue 13 July 2027 · 21:00 · hotel near The Grid",
              lines=["A pyramid. Five layers. No dates. Twenty minutes.",
                     "Yusuf stood up for D-05 and everyone laughed, kindly. He's on our side now.",
                     "Bert unfolded his arms at 11:21. That's the only metric from today I care about."]),
    sources=["Patrick Lencioni, <i>The Five Dysfunctions of a Team</i> (2002): conflict norms.",
             "Project Management Institute, <i>PMBOK Guide</i>: kick-off and team charter.",
             "Priya Parker, <i>The Art of Gathering</i> (2018)."],
)

# ------------------------------------------------------------------ 10 Who Decides What, and Where?
gv_problem = Doodle(760, 240, "Doodle of the first steering committee on Wednesday 28 July 2027. Eleven people around a table for a decision about the discovery interview list, something that should have been decided by two people. Oliver Thane from Vexmoor attends as Horizon assurance, with no vote, and takes notes.",
                    "Eleven people deciding an interview list. One of them, from the rival, taking notes.", exact=True)
gv_problem.box(160, 80, 440, 90, None, "paper", rx=40)
for i in range(11):
    a = 2 * math.pi * i / 11
    gv_problem.circle(380 + 260 * math.cos(a), 125 + 90 * math.sin(a), 16, "pink" if i == 3 else "y")
gv_problem.head(380, 132, "steering #1", size=20)
gv_problem.note(560, 236, "Oliver Thane, no vote, notes", "red", size=17)

gv_how = Doodle(760, 340, "Lodestar's governance on one page. Steering committee, monthly, chaired by Priya: scope, money over 25,000 pounds, milestones, top risks; Vexmoor attends as assurance, no vote. Design authority, every other Wednesday, chaired by Hollis: architecture and standards. Working groups, weekly: data with Bert, billing with Sven, testing with Oskar. Elaine and Callum decide day-to-day items and the change pool. Everything goes in one decision log, DL-001 onwards. Escalation: working group, then Elaine and Callum within five days, then steering.",
                "Each decision has one home. Everything else is noise in a big room.", exact=True)
gv_how.box(14, 14, 480, 64, "steering · monthly · Priya", "y", sub="scope, money ≥ £25k, milestones, top risks", size=18, subsize=15)
gv_how.box(510, 14, 236, 64, "Vexmoor: assurance", "pink", sub="attends, no vote", size=17, subsize=14)
gv_how.box(14, 96, 480, 64, "design authority · fortnightly · Hollis", "blue", sub="architecture, standards, data model", size=17, subsize=15)
gv_how.box(14, 178, 480, 64, "Elaine + Callum · weekly", "green", sub="day-to-day, change pool, escalations", size=18, subsize=15)
for i, t in enumerate(["data (Bert)", "billing (Sven)", "testing (Oskar)"]):
    gv_how.box(14 + i * 162, 260, 152, 50, t, "paper", size=16)
gv_how.box(510, 96, 236, 214, "decision log", "y", sub="DL-001 onwards", size=20, subsize=16)
gv_how.note(380, 330, "escalate: working group → Elaine + Callum (5 days) → steering", "red", size=17)

GOVERNANCE = dict(
    slug="governance", date=date(2027, 7, 28), meta="day 24 on site", where="FL 27",
    kicker="a.k.a. “programme governance”: steering, design authority, working groups",
    tldr="Governance answers one question: <b>where does each kind of decision get made?</b> Give every decision <b>one home</b>: a <b>steering committee</b> for scope, money and milestones; a <b>design authority</b> for architecture; <b>working groups</b> for detail; the two leads for day-to-day. Write the decisions in <b>one log</b>, and agree an <b>escalation path with deadlines</b>. A big room that decides everything decides nothing well.",
    chips=[("Family", "arriving"), ("Lives in", "Schedule 7 (governance) · delivery/lodestar/decision-log.md"), ("Pairs with", "mapping the client, the kick-off, the baseline")],
    problem_side="The Grid, room 27A, 28 July 2027",
    problem="""  <p class="lead">The first <b>steering committee</b> meets on <b>Wednesday 28 July</b> in room 27A. Eleven people: Priya (chair), Elaine, Hollis, Nkem, Rupert's delegate, Graham, Ines, Callum, two people from Priya's team, and <b>Oliver Thane</b> of Vexmoor, attending as “Horizon assurance” under the board's condition.</p>
  <ul>
    <li>The first 40 minutes are spent on <b>which people Wrenfield should interview in discovery</b>. Two people could have decided it in ten minutes.</li>
    <li>The decision that matters (approving relief notice RN-01) gets eight minutes at the end.</li>
    <li>Oliver doesn't speak. <span class="hl-pink">He writes four pages of notes.</span></li>
  </ul>""",
    problem_figs=[gv_problem],
    sides=dict(client=("Priya chairs", "<p>Priya wants <b>to be seen to be in control</b> in a Horizon year, so everything comes to her steering. But she has 90 minutes a month, and she can't judge interview lists. She needs the right decisions brought to her, prepared, and the rest kept away.</p>", "Bring me the decisions only I can make."),
                vendor=("Ines and Callum", "<p>Wrenfield needs decisions <b>fast and in the right place</b>: architecture with people who understand it, money with people who can approve it. And with Vexmoor in the room, it needs every decision <b>written down</b>, with reasons.</p>", "One home per decision. One log for all of them.")),
    sides_after="Governance isn't bureaucracy when it's the right size. It's how a sponsor stays in control without being in every meeting.",
    analogy_side="a hospital's decisions",
    analogy="""  <p>A hospital doesn't send every decision to the board. The <b>board</b> decides budgets and strategy. A <b>clinical committee</b> decides treatments. The <b>ward sister</b> decides who's on shift. Each has a rule for when to pass a problem up, and a timeline. If the board discussed shift rotas, nothing important would ever be decided.</p>""",
    map=[("The hospital board", "Steering: scope, money, milestones"),
         ("The clinical committee", "Design authority: architecture"),
         ("The ward sister", "Elaine and Callum, day to day"),
         ("Specialist teams", "Working groups: data, billing, testing"),
         ("The rule for passing it up", "Escalation: 5 days, then steering")],
    how_side="one home per decision, one log, one escalation path",
    how="""  <p>After the first steering, Ines and Elaine write <b>a one-page decision map</b>, which Priya approves in five minutes:</p>
  <ul>
    <li><b>Steering</b> (monthly, Priya): scope, money of £25k or more, milestone acceptance, top risks, relief and changes to the baseline. Vexmoor attends; no vote.</li>
    <li><b>Design authority</b> (every other Wednesday, Hollis): architecture, data model, standards. Kofi attends for metering.</li>
    <li><b>Elaine and Callum</b> (weekly): day-to-day, the change pool, interview lists, access.</li>
    <li><b>Working groups</b> (weekly): data (with Bert), billing (with Sven), testing (with Oskar).</li>
  </ul>
  <p>Everything decided anywhere goes in <b>one decision log</b>: number, date, decision, who, why, and what was rejected. <b>DL-001</b> (28 July): relief RN-01 approved. With Oliver in the room, the log is Wrenfield's best friend: every decision has a reason someone signed.</p>
  <p>The <b>escalation path</b> has deadlines: a working group that can't agree passes it to Elaine and Callum, who have <b>five working days</b>; then it goes to the next steering. Nothing waits more than a month.</p>""",
    how_figs=[gv_how],
    steps=[("List the kinds of decision", "Scope, money, architecture, day-to-day, detail."),
           ("Give each one home", "A forum with a chair and a frequency."),
           ("Keep the steering small and senior", "Only decisions only they can make."),
           ("One decision log for everything", "Number, date, decision, who, why, rejected options."),
           ("Escalation with deadlines", "Five days, then steering."),
           ("Prepare every steering decision", "A one-page paper, sent two days before.")],
    vocab=[("Steering committee", "The senior group that owns scope, money and milestones."),
           ("Design authority", "The group that approves architecture and standards."),
           ("Working group", "A small team that works out detail and recommends."),
           ("Decision log", "The dated record of all decisions and their reasons."),
           ("Assurance", "An independent check on how the programme is run, for the sponsor."),
           ("Terms of reference", "A forum's purpose, members, decisions and frequency.")],
    code=dict(file="delivery/lodestar/decision-log.md", note="from Wed 28 Jul 2027", src="""
DECISION LOG · LODESTAR

id      date    where     decision                                 by       why / rejected
DL-001  28 Jul  steering  relief RN-01: discovery end → 10 Dec     Priya    D-05 11 wd late;
                          no change to charges                              rejected: no relief
DL-002  28 Jul  steering  decision map v1 (one page) approved      Priya    40 min on interviews
DL-003  29 Jul  E + C     discovery interview list (31 people)     Elaine   moved from steering
DL-004  04 Aug  DA #1     C4 context diagram v0.2 accepted;        Hollis   rejected: reuse of
                          change detection: 3 options to test               Orion hub as-is
DL-005  11 Aug  billing   interface agreement IA-01 signed          Sven,    see RACI
                                                                   Hollis
escalation: working group → Elaine + Callum (5 wd) → next steering
"""),
    contract=dict(side="the governance schedule", doc="Lodestar SOW · Schedule 7 (governance)", date="v1.1 · 2 Aug 2027", stamp="amended",
                  clauses=[("2.1", "The Steering Committee meets monthly, chaired by the Sponsor, and decides matters reserved to it in the Decision Map (Annex A).", "Annex A is the one-page map. added 2 Aug."),
                           ("2.6", "<ins>A representative of Horizon Assurance may attend the Steering Committee and receive its papers, without a vote.</ins>", "Vexmoor, written in, with no vote. read every word of every paper as if they will."),
                           ("3.2", "All decisions are recorded in the Decision Log, which is a Contract document.", "the log is contractual. good.")],
                  plain="governance belongs in the contract: who decides what, and that the decision log counts. If a third party attends, write down its role and that it doesn't vote."),
    health=dict(now="a",
                g=("trust is high", ["Light governance; the log still matters.", "Steering can be quarterly.", "Decide most things in working groups."]),
                a=("new sponsor, an outside assurer", ["One-page decision map.", "Small steering, prepared papers.", "Everything in the log."]),
                r=("everything is escalated", ["Escalation deadlines, enforced.", "Papers with options and a recommendation.", "The log as your record."])),
    pressure=dict(level=3, title="the big room", cost="40 wasted minutes · one rival taking notes",
                  items=["Being watched by a rival's partner is unnerving. Write papers you'd be happy to see quoted, because they will be.", "Don't make the decision map look like you're taking power from Priya. Make it look like you're giving her time back."]),
    baseline="Each line compares <b>one big steering for everything</b> with <b>a one-page decision map, one log and an escalation path with deadlines</b>.",
    ratings=[(3, 4, "Priya's time goes to her decisions."),
             (2, 4, "Fewer meetings for the team."),
             (3, 3, "Neutral."),
             (2, 4, "Decisions have one home."),
             (3, 4, "Architecture decided by the design authority, not the room."),
             (2, 4, "Nothing waits more than a month."),
             (2, 5, "The log is contractual, with reasons."),
             (3, 4, "Decisions in days, not months."),
             (3, 3, "A log to keep.")],
    pitfalls=[("Everything to steering", "Senior time spent on detail.", "a decision map."),
              ("Too many forums", "Six committees, nobody knows which.", "four homes, one page."),
              ("Decisions without reasons", "Re-argued every month.", "log why, and what was rejected."),
              ("No escalation deadline", "Disagreements wait forever.", "five days, then steering."),
              ("Unprepared papers", "Discussion instead of decision.", "options and a recommendation, sent two days before.")],
    grimoire=[(1, "ghost-decision", "The Ghost Decision", "is what happens when decisions are made in rooms nobody logged.")],
    use=["Any programme with a sponsor and more than one team.", "When a steering committee is drowning in detail.", "When an outside party watches the programme."],
    skip=["A small project with one decision maker: a log is still worth it."],
    related=["<b>Who Really Decides Here?</b> (this volume)", "<b>How Do We Set the Rules at Kick-off?</b> (previous note)", "<b>Architecture Decision Records</b> (Ana, vol. 2)", "<b>Who Decides What?</b> (Sanne, vol. 2)"],
    quiz=[("What question does governance answer?", "Where each kind of decision gets made."),
          ("What does Lodestar's steering decide?", "Scope, money of £25k or more, milestone acceptance, top risks, relief and baseline changes."),
          ("What goes in a decision log entry?", "Number, date, decision, who, why, and what was rejected."),
          ("What's the escalation path?", "Working group → Elaine and Callum within five working days → the next steering."),
          ("Why write Vexmoor's role into Schedule 7?", "So its attendance, access and lack of a vote are clear.")],
    quiz_sit=[("Oliver Thane emails Priya directly, after a steering, questioning a design authority decision. What do you do?", "Nothing behind his back. Ask Elaine to put it on the next design authority agenda, where the decision belongs, with the log entry and its reasons. Answer the substance there.")],
    try_it="List the last ten decisions on your project. Where was each one made? Write a one-page decision map: which kinds of decision belong where, and how long an escalation may take.",
    remember="Every decision needs <span class=\"hl\">one home</span>, and every decision <span class=\"hl\">a line in the log</span>.",
    late=dict(when="Wed 28 July 2027 · 22:10 · hotel near The Grid",
              lines=["First steering. Forty minutes on an interview list. Eight on the thing that mattered.",
                     "Oliver wrote four pages. I don't know what's in them. I know what's in our log.",
                     "Priya approved the decision map in five minutes. I think she was relieved."]),
    sources=["UK Office of Government Commerce, <i>Managing Successful Programmes</i> (MSP).",
             "Project Management Institute, <i>The Standard for Program Management</i>.",
             "Michael Nygard, “Documenting Architecture Decisions” (2011)."],
)

NOTES = [DAY_ONE, ACCESS, MAPPING, KICK_OFF, GOVERNANCE]
