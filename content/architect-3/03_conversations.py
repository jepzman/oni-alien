# Series 2 · The Solution Architect's Notebook · Vol. 3 · Conversations.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Whiteboard Sessions
wb_problem = Doodle(760, 280, "Doodle of a whiteboard session on 13 October 2026 about Korenwolf's vans: eight people, five markers, ninety minutes. Everyone draws at once in different styles, arrows cross, and the session ends with a photo of a messy board and no decision.",
                    "Eight people, five markers, ninety minutes, one photo of a mess and no decision.")
wb_problem.box(20, 20, 420, 220, None, "paper")
for d in ["M60 60 L200 140 L120 200", "M240 50 Q 320 120 380 60", "M90 180 L380 190", "M300 200 L180 70", "M70 100 Q 260 30 400 150"]:
    wb_problem.line(d, color="pen", thin=True)
for x, y, t in [(90, 80, "vans?"), (330, 110, "cron!"), (200, 220, "SaaS?"), (360, 210, "??")]:
    wb_problem.text(x, y, t, "t-s", size=17)
wb_problem.box(480, 40, 260, 70, "5 markers", "y", sub="8 people")
wb_problem.box(480, 140, 260, 70, "90 minutes", "pink", sub="no decision", stroke="red")
wb_problem.note(590, 260, "a photo nobody can read", "red")

wb_analogy = Doodle(760, 250, "Doodle of a newspaper's morning editorial meeting. The question is what goes on the front page. One editor holds the pen, the meeting lasts twenty minutes, options are listed side by side, and it ends with a decision and who writes what.",
                     "The newsroom's morning meeting: one question, one pen, twenty minutes, a front page decided.")
wb_analogy.icon("newspaper", 40, 50, 1.5)
for i, (t, s, f) in enumerate([("one question", "“what's on page 1?”", "y"), ("one pen", "the editor", "blue"), ("20 minutes", "then decide", "green")]):
    x = 170 + i * 196
    wb_analogy.box(x, 60, 180, 84, t, f, sub=s, size=17, subsize=14)
wb_analogy.note(450, 210, "it ends with a decision and owners", "pen")

wb_how = Doodle(760, 370, "The second session, 20 October 2026. The board is set up before people arrive: the question at the top, should vans be part of Dispatch?, a legend in the corner, three options drawn side by side: vans scheduled by hand, vans in Dispatch as a courier type, a separate van-routing service. Ana holds the only marker; others talk. Sixty minutes. It ends with a decision box: vans become a courier type in Dispatch; owner Eli; ADR 0015 by 2 November. The photo goes into the ADR.",
                 "Question on top, legend in the corner, options side by side, one marker, a decision box at the bottom.")
wb_how.box(14, 14, 732, 50, "Q: should Korenwolf's vans be part of Dispatch?", "y", size=16)
wb_how.box(620, 76, 126, 80, "legend", "paper", sub="□ ○ → ⇢", subsize=14, size=14)
for i, (t, s, f) in enumerate([("by hand", "Joost's team, a sheet", "paper"), ("in Dispatch", "a courier type", "green"), ("own service", "van routing", "paper")]):
    x = 14 + i * 200
    wb_how.box(x, 76, 186, 150, t, f, sub=s, size=17, subsize=14, stroke="green" if i == 1 else "")
wb_how.box(14, 244, 732, 70, None, "green")
wb_how.text(380, 272, "DECISION: vans are a courier type in Dispatch", "t-head", size=16)
wb_how.text(380, 300, "owner: Eli · ADR 0015 by 2 Nov · photo goes into the ADR", size=15)
wb_how.note(380, 348, "one marker (Ana) · 60 minutes · 8 people", "pen", size=17)

WHITEBOARD = dict(
    slug="whiteboard-sessions",
    kicker="a.k.a. “the newsroom's morning meeting”",
    tldr="A whiteboard session is the fastest way to design together, and the easiest to waste. Prepare the board: write <b>the question at the top</b>, a <b>legend</b> in the corner, room for <b>options side by side</b>. One person <b>holds the marker</b> and draws what the room says. <b>Timebox</b> it (60 minutes), end with a <b>decision box</b> (what, who, by when) and turn the <b>photo into a record</b>: an ADR, an RFC or a line in the decision log.",
    chips=[("Family", "conversations"), ("Origin", "facilitation practice; Dave Gray et al., <i>Gamestorming</i> (2010); visual meetings"), ("Lives in", "a photo attached to the ADR or decision log line"), ("Pairs with", "options analysis, ADRs, RFCs, event storming")],
    problem_side="Larder, 13 October 2026",
    problem="""  <p class="lead">Korenwolf's three offices start in January, with vans every morning. Today Joost's team plans the vans <b>by hand</b> on a sheet. Ana calls a whiteboard session: should vans be part of Dispatch? <b>Eight people</b>, <b>five markers</b>, <b>ninety minutes</b>. Everyone draws at once, in their own style; arrows cross; two side debates start. It ends with <span class="hl-pink">a photo of a messy board and no decision</span>.</p>
  <ul>
    <li>No written question, so people solve different problems.</li>
    <li>Several markers mean several diagrams on top of each other.</li>
    <li>No decision box, so the session ends when time runs out.</li>
  </ul>""",
    problem_figs=[wb_problem],
    analogy_side="the newsroom's morning meeting",
    analogy="""  <p>A newspaper decides its front page every morning in a short meeting. There's <b>one question</b> (what's on page one?), <b>one editor</b> with the pen listing the candidates side by side, and <b>twenty minutes</b>. It ends with a decision and who writes what. Nobody grabs the pen to sketch their own front page.</p>""",
    analogy_figs=[wb_analogy],
    map=[("“What's on page one?”", "The question at the top of the board"),
         ("The editor's pen", "One marker, held by the facilitator"),
         ("Candidates side by side", "Options drawn next to each other"),
         ("Twenty minutes", "A sixty-minute timebox"),
         ("Who writes what", "The decision box: what, owner, by when")],
    how_side="prepare the board, hold the marker",
    how="""  <p>The second session, a week later, took <b>sixty minutes</b>. Ana wrote the question and a legend before anyone arrived, drew three options side by side as people described them, and kept the only marker. Joost explained the morning van routes, Eli the courier model, Mo the Korenwolf windows. Decision: <b>vans become a courier type in Dispatch</b>; Eli writes ADR 0015, with the photo attached.</p>""",
    how_figs=[wb_how],
    steps=[("Write the question first", "On the board before people arrive, as one sentence that can be answered."),
           ("Add a legend", "What boxes, circles and arrow styles mean today."),
           ("Invite the right few", "The people who know the facts and the people who'll build it; six to eight."),
           ("Hold the marker", "One facilitator draws; others talk. Hand it over on purpose, not by grabbing."),
           ("Options side by side", "At least two, drawn the same way, so they can be compared."),
           ("End with a decision box", "What, who, by when; photo into the ADR or decision log.")],
    vocab=[("Facilitator", "The person running the session and holding the marker."),
           ("Timebox", "A fixed length; when it ends, decide or schedule the next step."),
           ("Legend", "What the shapes and lines on the board mean."),
           ("Parking lot", "A corner for side topics, to handle later."),
           ("Decision box", "What was decided, the owner and the date."),
           ("Record", "The ADR, RFC or log line the photo becomes.")],
    code=dict(file="docs/sessions/2026-10-20-vans.md", note="session card, prepared before the second session", plain=True, src="""
# Whiteboard session · vans and Dispatch                   20 Oct 2026, 10:00–11:00

Question     Should Korenwolf's morning vans be planned by Dispatch?
Why now      Three offices from January; today Joost's team plans vans on a sheet.
Who          Ana (marker), Eli, Ben, Joost, Sanne, Mo, Dee, Tomás
Legend       □ system · ○ person/team · → event · ⇢ manual step
Options      A by hand (today) · B a courier type in Dispatch · C a van-routing service
Parking lot  van leasing, driver contracts (→ Joost)

Decision     B. Vans are a courier type in Dispatch: capacity in crates, time
             windows 07:00–09:00, routes planned the evening before by Engine A.
Owner        Eli · ADR 0015 by 2 Nov · photo attached
"""),
    tools="tools: a real whiteboard and good markers; for remote sessions, Miro, FigJam or Excalidraw with one person drawing. A phone camera and the ADR folder.",
    gains=["<b>Decisions in an hour</b> instead of a messy afternoon.",
           "<b>Everyone sees the same picture</b>, drawn one way.",
           "<b>Options compared fairly</b>, side by side.",
           "<b>A record</b>: the photo and the ADR.",
           "<b>Quiet experts get heard</b>: the facilitator asks them."],
    losses=["<b>Preparation</b> takes half an hour.",
            "<b>The facilitator can steer</b> too much.",
            "<b>Some people need to draw</b> to think.",
            "<b>Remote sessions</b> are harder to keep focused."],
    baseline="Each line compares <b>an open whiteboard free-for-all</b> to <b>a prepared session: question, legend, one marker, options side by side, a timebox and a decision box</b>.",
    ratings=[(2, 4, "One clear drawing instead of five layered ones."),
             (2, 5, "Operations, product and engineering agree in the room."),
             (1, 5, "Sixty minutes to a decision."),
             (3, 4, "Joost's facts reach the design early."),
             (3, 3, "Neutral."),
             (2, 4, "The photo and the ADR record the reasoning."),
             (3, 3, "Neutral."),
             (3, 4, "Half an hour of preparation saves hours."),
             (3, 4, "Teams can run sessions with the same card.")],
    pitfalls=[("No question", "Everyone solves a different problem.", "write one answerable question on the board first."),
              ("Many markers", "Five diagrams on top of each other.", "one marker, held by the facilitator."),
              ("No timebox", "It ends when the room is booked.", "sixty minutes, then decide or schedule."),
              ("The photo is the record", "A blurry board nobody can read later.", "write the decision up as an ADR, with the photo attached.")],
    use=["Design questions with several people who know part of the answer.",
         "Comparing options quickly.",
         "Kick-offs for RFCs.",
         "When chat threads go round in circles."],
    skip=["Decisions one person can make with an ADR.",
          "Big domain discovery: use event storming."],
    related=["<b>Options analysis</b> (Vol. 2)", "<b>RFCs &amp; design docs</b> (Vol. 2)", "<b>Domain discovery (event storming)</b> (Vol. 1)", "<b>Architecture decision records</b> (Vol. 2)"],
    quiz=[("What goes on the board before anyone arrives?", "The question, a legend, and space for options side by side."),
          ("Why one marker?", "So there's one drawing, made in one style, of what the room agrees."),
          ("How should a session end?", "With a decision box: what, who, by when."),
          ("What happens to the photo?", "It's attached to the ADR, RFC or decision log line that records the decision.")],
    try_it="For your next design discussion, prepare the board: one question, a legend, three empty option boxes. Hold the only marker, set a 60-minute timer, and end with a decision box. Write the ADR within a day with the photo attached.",
    remember="One <span class=\"hl\">question</span>, one <span class=\"hl\">marker</span>, a decision box at the bottom.",
    sources=["Dave Gray, Sunni Brown and James Macanufo, <i>Gamestorming</i> (2010).",
             "David Sibbet, <i>Visual Meetings</i> (2010).",
             "Sam Kaner et al., <i>Facilitator's Guide to Participatory Decision-Making</i>, 3rd ed. (2014).",
             "Simon Brown, “The Art of Visualising Software Architecture” (talks and workshops)."],
)

# ------------------------------------------------------------------ 10 Presenting to Executives
pe_problem = Doodle(760, 280, "Doodle of Ana's first presentation on the warehouse system on 2 December 2026: twenty-two slides starting with API rate limits and cache design. At slide six Femke stops her: what do you want from us?",
                    "Slide 6 of 22, still on API rate limits, when Femke asks: “what do you want from us?”")
for i in range(5):
    pe_problem.box(30 + i * 14, 30 + i * 12, 240, 150, None, "paper", rx=4)
pe_problem.text(220, 140, "6 / 22", "t-head", size=18)
pe_problem.text(220, 170, "API rate limits…", size=15)
pe_problem.box(400, 50, 340, 90, "Femke", "pink", sub="“what do you want from us?”", stroke="red")
pe_problem.note(570, 220, "the answer was on slide 21", "red")

pe_analogy = Doodle(760, 250, "Doodle of a pilot's announcement: we're landing twenty minutes late because of headwinds; you'll make connections after 15:30; crew will help those before. The answer first, then what it means for you, then what to do. No talk of jet streams.",
                     "A pilot's announcement: the answer, what it means for you, what to do. No lecture on jet streams.")
pe_analogy.icon("ship", 30, 70, 1.0)
for i, (t, s, f) in enumerate([("20 min late", "the answer", "y"), ("after 15:30: fine", "what it means", "blue"), ("crew will help", "what to do", "green")]):
    x = 160 + i * 196
    pe_analogy.box(x, 60, 180, 84, t, f, sub=s, size=16, subsize=14)
pe_analogy.note(450, 210, "nobody needs the jet stream", "pen")

pe_how = Doodle(760, 370, "Ana's second presentation, 9 December 2026, five slides in ten minutes. Slide one, the answer: give StockPilot notice and move to WMS B by September 2027. Slide two, three options compared on money, risk and time: renew at about 252,000 euros a year; WMS B at about 118,000 a year plus 90,000 to migrate; build our own stock service, about six months of a team. Slide three, the recommendation and why. Slide four, the main risk and how it's handled: migration during the Utrecht launch, so move store by store. Slide five, the ask: approve the 90,000 euros and Eli's and Ben's teams for three months, decide today.",
                 "Five slides: the answer, options in money, risk and time, the recommendation, the main risk, the ask.")
for i, (t, s, f) in enumerate([("1 · answer", "WMS B by Sep 2027", "green"), ("2 · options", "€ · risk · time", "y"), ("3 · why", "≈ ½ the renewal", "blue"), ("4 · risk", "store by store", "pink"), ("5 · ask", "€90k + 3 months", "green")]):
    x = 8 + i * 150
    pe_how.box(x, 20, 144, 90, t, f, sub=s, size=15, subsize=12)
pe_how.head(20, 156, "option", anchor="start", size=15)
pe_how.head(360, 156, "€ a year", size=15)
pe_how.head(520, 156, "one-off", size=15)
pe_how.head(660, 156, "risk", size=15)
for i, (o, y1, one, r, f) in enumerate([("renew StockPilot", "≈ 252k", "0", "low", "paper"), ("WMS B ★", "≈ 118k", "90k", "medium", "green"), ("own stock service", "≈ 60k", "≈ 300k", "high", "paper")]):
    y = 196 + i * 40
    pe_how.text(20, y, o, "t-head" if "★" in o else "t", anchor="start", size=15)
    pe_how.text(360, y, y1, size=15)
    pe_how.text(520, y, one, size=15)
    pe_how.text(660, y, r, size=15)
pe_how.note(380, 340, "decided in the meeting · ADR 0016 on 15 Dec", "green", size=18)

PRESENTING = dict(
    slug="presenting-to-executives",
    kicker="a.k.a. “the pilot's announcement”",
    tldr="Executives decide many things a day with little time for each. Give them <b>the answer first</b>, then the <b>options in their terms</b> (money, risk, time, customers), your <b>recommendation and why</b>, the <b>main risk</b> and how you'll handle it, and the <b>ask</b>: exactly what you need them to decide, today. Five slides, ten minutes, and the technical detail in the appendix for anyone who asks.",
    chips=[("Family", "conversations"), ("Origin", "Barbara Minto, <i>The Pyramid Principle</i> (1987); military BLUF (bottom line up front)"), ("Lives in", "five slides and a one-page memo, with an appendix"), ("Pairs with", "architecture one-pager, exit plans, explaining trade-offs")],
    problem_side="Larder, 2 December 2026",
    problem="""  <p class="lead">StockPilot's renewal decision is due by <b>31 December</b> (the exit plan from July). Ana presents to Femke, Marco and Joost with <b>22 slides</b>, starting from StockPilot's API rate limits and the stock cache design. At slide six, Femke stops her: <span class="hl-pink">“what do you want from us?”</span> The answer was on slide 21. The meeting ends without a decision, with four weeks left.</p>
  <ul>
    <li>Architects present in the order they worked: problem, analysis, conclusion.</li>
    <li>Executives need the conclusion first, then just enough to trust it.</li>
    <li>Without a clear ask, a good analysis ends in “let's discuss next week”.</li>
  </ul>""",
    problem_figs=[pe_problem],
    analogy_side="the pilot's announcement",
    analogy="""  <p>A good pilot says: <b>“We'll land 20 minutes late.”</b> Then <b>what it means for you</b>: connections after 15:30 are fine. Then <b>what to do</b>: the crew will help everyone else. Nobody explains the jet stream unless a passenger asks. The passengers can decide what to do in ten seconds.</p>""",
    analogy_figs=[pe_analogy],
    map=[("“We'll land 20 minutes late”", "The answer: move to WMS B by September 2027"),
         ("Connections after 15:30 are fine", "The options in money, risk and time"),
         ("The crew will help", "The main risk and how it's handled"),
         ("“Please stay seated”", "The ask: €90k and two teams for three months"),
         ("The jet stream", "API rate limits and cache design: the appendix")],
    how_side="answer, options, why, risk, ask",
    how="""  <p>A week later Ana came back with <b>five slides</b> and a one-page memo sent the day before. Slide one was the answer. Slide two compared renewing (≈ €252k a year), <b>WMS B</b> (≈ €118k a year plus €90k to migrate) and building their own (≈ six months of a team). The risk slide addressed Joost's worry: migrate <b>store by store</b>, not during the Utrecht launch week. Marco had already negotiated a three-month bridge with StockPilot using the alternative. Approved in the meeting; ADR 0016 followed on 15 December.</p>""",
    how_figs=[pe_how],
    steps=[("Start with the answer", "One sentence: what you recommend, by when."),
           ("Compare options in their terms", "Money, risk, time, customers; two to four options including “do nothing”."),
           ("Say why, briefly", "The two or three reasons that decide it."),
           ("Name the main risk and the plan", "The thing they'll worry about, answered before they ask."),
           ("Make the ask precise", "What decision, what money or people, by when: “decide today”."),
           ("Send a memo first; keep an appendix", "One page the day before; technical detail at the back.")],
    vocab=[("BLUF", "Bottom line up front: the conclusion first."),
           ("Pyramid principle", "Answer first, then grouped supporting arguments."),
           ("The ask", "The specific decision or resources you need."),
           ("Pre-read", "A short memo sent before the meeting."),
           ("Appendix", "Detail kept for questions, not presented."),
           ("Decision meeting", "A meeting that ends with a decision, not a discussion.")],
    code=dict(file="docs/decisions/2026-12-warehouse-memo.md", note="the pre-read sent on 8 December 2026", plain=True, src="""
# Warehouse system: decision needed by 31 December              Ana · pre-read, 8 Dec

ANSWER     Give StockPilot notice and move to WMS B by September 2027.
OPTIONS    (12 stores by end 2027)       € a year     one-off     risk
           Renew StockPilot              ≈ 252k        –           low, but 3× today
           Move to WMS B                 ≈ 118k        ≈ 90k       medium
           Build our own stock service   ≈ 60k + team  ≈ 300k      high, 6+ months
WHY        Half the cost of renewing within a year; our Stock module already
           hides the vendor (ADR 0005), so only one adapter changes.
RISK       Migrating during the Utrecht launch. Plan: store by store, Utrecht
           opens on StockPilot; a 3-month bridge to Sep 2027 (Marco agreed it
           with StockPilot on 4 Dec at today's price).
ASK        Approve ≈ €90k and Eli's and Ben's teams for 3 months (Mar–May).
           Decide on 9 December.            Appendix: API limits, cache, data export.
"""),
    tools="tools: five slides or a one-page memo; Amazon-style written pre-reads; the architecture one-pager and exit plan as sources. No tool fixes the order of the argument.",
    gains=["<b>Decisions in the meeting</b>, not next week.",
           "<b>Executives trust the analysis</b> because it's in their terms.",
           "<b>Shorter meetings</b>: ten minutes plus questions.",
           "<b>The risk is pre-empted</b>, not discovered.",
           "<b>Architects get invited back</b>."],
    losses=["<b>Feels backwards</b> to engineers at first.",
            "<b>Detail is hidden</b>: some executives want it.",
            "<b>Translating to money</b> takes work.",
            "<b>A wrong answer up front</b> is very visible."],
    baseline="Each line compares <b>presenting the analysis in the order it was done</b> to <b>answer first, options in money, risk and time, the main risk, and a precise ask, with a pre-read</b>.",
    ratings=[(2, 5, "The answer fits in one sentence."),
             (2, 5, "Femke, Marco and Joost decided together."),
             (1, 5, "Decided in the meeting, three weeks before the deadline."),
             (2, 4, "The migration risk was answered up front."),
             (3, 3, "Neutral."),
             (2, 4, "The memo and ADR 0016 record the decision."),
             (2, 5, "Every option in euros a year and one-off."),
             (2, 4, "Five slides instead of twenty-two."),
             (3, 3, "Neutral.")],
    pitfalls=[("Chronological story", "Rate limits first, recommendation last.", "answer first."),
              ("Technical terms", "“Bulk endpoint throughput.”", "money, risk, time, customers."),
              ("No ask", "“Thoughts?”", "say exactly what you need decided, and by when."),
              ("No pre-read", "Executives see the numbers for the first time in the room.", "send one page the day before.")],
    use=["Any decision that needs executive approval.",
         "Board and investor updates on architecture.",
         "Budget requests for technical work.",
         "Vendor and platform decisions."],
    skip=["Design reviews with engineers: there, the reasoning is the point.",
          "Status updates with no decision needed."],
    related=["<b>Architecture one-pager</b> (this volume)", "<b>Explaining trade-offs to non-engineers</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)", "<b>Pitching to the CEO</b> (Grace, book 2)"],
    quiz=[("What goes on the first slide?", "The answer: the recommendation in one sentence."),
          ("In what terms should options be compared?", "Money, risk, time and customers."),
          ("What's “the ask”?", "Exactly what decision or resources you need, by when."),
          ("Where does the technical detail go?", "In an appendix, for questions.")],
    try_it="Take a technical decision you need approved. Write the first slide as one sentence: what you recommend, by when. Then fill four more: options in money, risk and time; why; the main risk; the ask. Send it as a one-page memo the day before the meeting.",
    remember="Land the plane <span class=\"hl\">first</span>. The jet stream goes in the <span class=\"hl\">appendix</span>.",
    sources=["Barbara Minto, <i>The Pyramid Principle</i> (1987).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Nancy Duarte, <i>DataStory</i> (2019) and <i>Resonate</i> (2010).",
             "Jeff Bezos, Amazon shareholder letter (2017), on six-page memos."],
)

# ------------------------------------------------------------------ 11 Explaining Trade-offs to Non-Engineers
et_problem = Doodle(760, 280, "Doodle of Femke in January 2027, after a 38-minute checkout outage during the Christmas peak, asking for 99.99 percent uptime. Ana starts explaining regions, failover and replication lag. Femke's eyes glaze over; she hears only no.",
                    "Femke asks for 99.99 %. Ana answers with failover and replication lag. Femke hears “no”.")
et_problem.box(20, 40, 300, 90, "Femke", "y", sub="“99.99 %, please”")
et_problem.box(380, 30, 360, 120, None, "paper")
for i, t in enumerate(["multi-region failover…", "replication lag…", "RPO and RTO…"]):
    et_problem.text(560, 64 + i * 30, t, size=16)
et_problem.note(380, 200, "after 38 minutes down at the Christmas peak", "pen")
et_problem.note(380, 254, "what Femke hears: “no”", "red")

et_analogy = Doodle(760, 250, "Doodle of a family deciding about a second car just in case the first one breaks down. The second car costs 4,000 euros a year. A spare tyre and roadside assistance cost 120 euros a year and cover most of the real cases. The question is what breakdowns you actually care about.",
                     "A second car “just in case” costs €4,000 a year; a spare tyre and roadside help cover most real cases for €120.")
et_analogy.icon("chassis", 30, 60, 1.5)
et_analogy.box(190, 50, 260, 90, "a second car", "pink", sub="€4,000 a year")
et_analogy.box(480, 50, 260, 90, "spare tyre + help", "green", sub="€120 a year")
et_analogy.note(450, 210, "which breakdowns do we actually care about?", "pen")

et_how = Doodle(760, 360, "Ana's second explanation, 12 January 2027, in Femke's terms. 99.9 percent means about 43 minutes down a month; 99.99 percent means about 4 minutes. Getting to 99.99 everywhere needs a second region: about 9,000 euros a month and two more engineers, ready in about six months. The alternative: protect the minutes that matter, the Friday evening peak and Korenwolf's 07:00 to 09:00 window, with a faster database failover, no changes in those windows and orders picked the night before: about 1,500 euros a month, ready in six weeks. Femke chose the second.",
                 "Translate “nines” into minutes and euros, then ask which minutes matter. Femke chose to protect those.")
for i, (t, s, f) in enumerate([("99.9 %", "≈ 43 min down a month", "y"), ("99.99 %", "≈ 4 min down a month", "blue")]):
    et_how.box(14 + i * 250, 14, 234, 76, t, f, sub=s, size=20, subsize=14)
et_how.box(530, 14, 216, 76, "Christmas 2026", "pink", sub="38 min, at peak", subsize=14)
et_how.box(14, 110, 360, 160, None, "paper")
et_how.head(194, 140, "99.99 % everywhere", size=16)
for i, t in enumerate(["second region", "≈ €9,000 a month + 2 engineers", "about 6 months"]):
    et_how.text(194, 176 + i * 28, t, size=15)
et_how.box(386, 110, 360, 160, None, "green", stroke="green")
et_how.head(566, 140, "protect the minutes that matter", size=15)
for i, t in enumerate(["Fri peak · Korenwolf 07:00–09:00", "≈ €1,500 a month", "about 6 weeks"]):
    et_how.text(566, 176 + i * 28, t, size=15)
et_how.note(566, 300, "Femke chose this one", "green", size=18)
et_how.note(194, 300, "the “nines” in minutes and euros", "pen", size=17)

EXPLAIN = dict(
    slug="explaining-trade-offs",
    kicker="a.k.a. “the spare tyre or the second car”",
    tldr="When a non-engineer asks for something expensive (“99.99 % uptime”), a technical answer sounds like “no”. Translate the trade-off into <b>what they care about</b>: <b>minutes, euros, customers, dates</b>. Show <b>what each option buys and costs</b>, find out <b>which part of the request really matters</b> to them, and offer a <b>cheaper option that protects that part</b>. Use an everyday comparison, then the numbers. Then let them choose.",
    chips=[("Family", "conversations"), ("Origin", "architecture practice; Gregor Hohpe, “the architect elevator”"), ("Lives in", "a conversation and a one-page comparison"), ("Pairs with", "presenting to executives, availability maths, trade-off sliders")],
    problem_side="Larder, 12 January 2027",
    problem="""  <p class="lead">On <b>18 December</b>, during the Christmas peak, a database failover took checkout down for <b>38 minutes</b>. In January Femke asks Ana for <b>“99.99 % uptime”</b> before Korenwolf's renewal talks in 2027. Ana starts explaining multi-region failover, replication lag and recovery objectives. Femke's eyes glaze over; <span class="hl-pink">what she hears is “no”</span>, and she starts wondering if she needs a different architect.</p>
  <ul>
    <li>Technical explanations answer the engineer's question, not the asker's.</li>
    <li>Requests like “99.99 %” stand in for a real worry (here: peaks and Korenwolf's mornings).</li>
    <li>Without costs in their terms, people can't make the trade-off themselves.</li>
  </ul>""",
    problem_figs=[et_problem],
    analogy_side="the second car",
    analogy="""  <p>A family worried about breakdowns could buy <b>a second car</b>, just in case: €4,000 a year. Or a <b>spare tyre and roadside assistance</b>: €120 a year, covering most of the breakdowns that actually happen. The right answer depends on <b>which breakdowns they care about</b>: getting to work every day, or never being stranded on a holiday drive.</p>""",
    analogy_figs=[et_analogy],
    map=[("A second car", "A second cloud region for 99.99 % everywhere"),
         ("€4,000 a year", "≈ €9,000 a month and two more engineers"),
         ("A spare tyre and roadside help", "Faster failover, no changes in key windows, orders picked the night before"),
         ("“Which breakdowns matter?”", "Friday evening and Korenwolf's 07:00–09:00"),
         ("The family decides", "Femke chooses, with the costs in front of her")],
    how_side="minutes, euros, and which minutes matter",
    how="""  <p>Ana came back with one page. <b>99.9 %</b> is about <b>43 minutes</b> down a month; <b>99.99 %</b> about <b>4</b>. Getting there everywhere means a <b>second region</b>: ≈ €9,000 a month, two more engineers, six months. Then she asked which minutes Femke really meant. The answer: <b>Friday evenings</b> and <b>Korenwolf's mornings</b>. Protecting those (faster failover, no changes in those windows, Korenwolf's orders picked the night before) costs ≈ €1,500 a month and takes six weeks. Femke chose it in five minutes.</p>""",
    how_figs=[et_how],
    steps=[("Hear the worry behind the request", "“99.99 %” usually means “never again like Christmas”."),
           ("Translate into their units", "Minutes down a month, euros a month, customers affected, weeks to build."),
           ("Use one everyday comparison", "Spare tyre vs second car; then the real numbers."),
           ("Show two or three options", "Including one that protects the part that matters, cheaply."),
           ("Make the costs honest", "Running costs and people, not just the bill."),
           ("Let them choose", "Then record it as an ADR with their name as approver.")],
    vocab=[("Nines", "Availability as a percentage: 99.9 % is “three nines”."),
           ("Downtime budget", "Minutes of outage a month a target allows."),
           ("Critical window", "A time when outages hurt most (Friday peak, 07:00–09:00)."),
           ("Failover", "Switching to a standby when the main component fails."),
           ("Multi-region", "Running in two cloud regions to survive a region failing."),
           ("Trade-off", "Getting more of one thing by accepting less of another.")],
    code=dict(file="docs/decisions/2027-01-availability-options.md", note="the page Ana gave Femke, 12 January 2027", plain=True, src="""
# How available should Larder be?                            for Femke · 12 Jan 2027

What happened   18 Dec 2026, 18:05: database failover, checkout down 38 minutes
                at the Christmas peak (≈ 900 orders lost or late).
In minutes      99.9 %  ≈ 43 minutes down a month   (where we are, roughly)
                99.99 % ≈ 4 minutes down a month

Option A        99.99 % everywhere: a second cloud region
                ≈ €9,000 a month + 2 engineers · about 6 months
Option B        Protect the minutes that matter:
                Friday 17:00–20:00 and Korenwolf's 07:00–09:00
                - faster database failover (under 2 minutes, tested monthly)
                - no deploys or changes inside those windows
                - business orders picked the evening before
                ≈ €1,500 a month · about 6 weeks
Chosen          B, by Femke, 12 Jan. Revisit when Antwerp opens.  → ADR 0017
"""),
    tools="tools: a one-page comparison; availability tables (minutes per nine); for the maths, Vol. 5's availability note. Analogies are tools too: choose one from the listener's world.",
    gains=["<b>The real worry gets solved</b>, not the literal request.",
           "<b>Decisions by the right person</b>, with real costs.",
           "<b>Cheaper, faster options</b> appear.",
           "<b>Trust</b>: the architect sounds like a partner, not a blocker.",
           "<b>Shared vocabulary</b>: minutes and euros."],
    losses=["<b>Simplifies</b>: some nuance is lost.",
            "<b>Analogies can mislead</b> if stretched.",
            "<b>Needs good numbers</b> ready.",
            "<b>Takes a second conversation</b> after the first goes wrong."],
    baseline="Each line compares <b>answering a business request with technical detail</b> to <b>translating it into minutes, euros and customers, and offering an option that protects what matters</b>.",
    ratings=[(2, 5, "Femke understood the options in five minutes."),
             (2, 5, "The CEO and the architect agreed on what matters."),
             (2, 4, "Decided in one meeting."),
             (2, 4, "The real risk (peaks, Korenwolf's mornings) is addressed."),
             (3, 4, "Option B can grow into A later."),
             (2, 4, "The choice and the costs are in ADR 0017."),
             (2, 5, "€1,500 vs €9,000 a month, side by side."),
             (3, 4, "One page, one conversation."),
             (3, 3, "Neutral.")],
    pitfalls=[("Answering in jargon", "Replication lag and RPO.", "minutes, euros, customers, weeks."),
              ("Taking the request literally", "Building 99.99 % everywhere.", "ask which minutes matter."),
              ("Saying no", "“That's not possible.”", "show what it costs, and a cheaper option."),
              ("Stretching the analogy", "Arguing about cars instead of Larder.", "one comparison, then the real numbers.")],
    use=["Requests for “more” from executives or clients: uptime, speed, security.",
         "After an incident, when demands run high.",
         "Any trade-off a non-engineer must decide.",
         "Contract and service-level talks."],
    skip=["Purely technical choices inside the team.",
          "When the listener wants the technical depth: then give it."],
    related=["<b>Presenting to executives</b> (this volume)", "<b>Trade-off sliders</b> (Vol. 2)", "<b>Availability maths</b> (Vol. 5)", "<b>When to go multi-region</b> (Vol. 5)"],
    quiz=[("How many minutes a month is 99.9 % and 99.99 %?", "About 43 minutes and about 4 minutes."),
          ("What was the worry behind Femke's request?", "Outages at the Friday peak and in Korenwolf's 07:00–09:00 window."),
          ("What did option B do?", "Protected the critical windows: faster failover, no changes in them, business orders picked the night before."),
          ("Why use an everyday comparison?", "It makes the shape of the trade-off clear before the numbers.")],
    try_it="Pick a request you've recently answered with “that's hard”. Write the worry behind it, then two options in minutes, euros and weeks, one of which protects just the part that matters. Take it back to the person as one page.",
    remember="Ask which <span class=\"hl\">breakdowns</span> matter. A spare tyre may beat a <span class=\"hl\">second car</span>.",
    sources=["Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), on availability targets.",
             "Chip and Dan Heath, <i>Made to Stick</i> (2007), on concrete explanations.",
             "Neal Ford and Mark Richards, <i>Fundamentals of Software Architecture</i> (2020), soft skills chapters."],
)

# ------------------------------------------------------------------ 12 Architecture Katas
ka_problem = Doodle(760, 280, "Doodle of Ana in January 2027 as Larder's only architect, with eighteen engineers and four cities coming. Every design question queues for her. The tech leads have never practised designing a whole system.",
                    "One architect, eighteen engineers, four cities coming, and every design question in one queue.")
ka_problem.box(300, 30, 160, 80, "Ana", "y", sub="the only architect")
for i in range(6):
    ka_problem.box(30 + i * 120, 170, 100, 50, "?", "paper", size=18)
    ka_problem.arrow(80 + i * 120, 166, 380, 114, dash=True)
ka_problem.note(380, 262, "tech leads who've never designed a whole system", "red")

ka_analogy = Doodle(760, 250, "Doodle of chess players solving puzzles: a set position, a time limit, find the best move, then compare answers with a coach. Players get better by practising positions, not only by playing whole games.",
                     "Chess players train on puzzles: a set position, a time limit, then compare with a coach.")
ka_analogy.icon("dice", 40, 60, 1.4)
for i, (t, s, f) in enumerate([("a position", "set up for you", "paper"), ("15 minutes", "find the move", "y"), ("the coach", "compare, discuss", "green")]):
    x = 170 + i * 196
    ka_analogy.box(x, 60, 180, 84, t, f, sub=s, size=17, subsize=14)
ka_analogy.note(450, 210, "practise positions, not whole games", "pen")

ka_how = Doodle(760, 360, "Larder's first architecture kata, 19 January 2027. The brief: Larder in Antwerp, with French and Dutch, Belgian VAT, Bancontact and stock across the border. Three teams of three, each with a tech lead, have 90 minutes to design and 10 minutes each to present. Judges: Ana, Eli, and Grace playing the customer. Feedback on the requirements each team found, the trade-offs they named and how clearly they explained them. Monthly from now on, each time a different brief.",
                 "A brief, small teams, 90 minutes, short presentations, feedback on trade-offs. Monthly.")
ka_how.box(14, 14, 732, 70, "brief: Larder in Antwerp", "y", sub="French + Dutch · Belgian VAT · Bancontact · stock across the border", subsize=14)
for i, t in enumerate(["team A", "team B", "team C"]):
    x = 14 + i * 250
    ka_how.box(x, 110, 232, 80, t, "blue", sub="3 people · 90 min")
for i, (t, s, f) in enumerate([("present", "10 min each", "paper"), ("judges", "Ana · Eli · Grace", "green"), ("feedback", "trade-offs, clarity", "pink")]):
    x = 14 + i * 250
    ka_how.box(x, 216, 232, 80, t, f, sub=s, subsize=13)
ka_how.note(380, 336, "monthly · a new brief each time", "pen", size=18)

KATAS = dict(
    slug="architecture-katas",
    kicker="a.k.a. “chess puzzles”",
    tldr="Architects get good by designing systems, and most engineers rarely get to. An <b>architecture kata</b> is a short practice: a <b>brief</b> (a made-up or future system with a few requirements and constraints), <b>small teams</b>, <b>90 minutes</b> to design, <b>ten minutes</b> to present, and <b>feedback</b> on the requirements they found, the <b>trade-offs</b> they named and how clearly they explained them. Run it monthly with a new brief, and the next architects grow inside the team.",
    chips=[("Family", "conversations"), ("Origin", "Ted Neward, Architectural Katas (2010s); “code katas” (Dave Thomas)"), ("Lives in", "a monthly session and a folder of briefs"), ("Pairs with", "whiteboard sessions, growing other architects, explaining trade-offs")],
    problem_side="Larder, 19 January 2027",
    problem="""  <p class="lead">Larder has <b>18 engineers</b> and <b>one architect</b>. In 2027 four cities open, and Antwerp brings a new country. Every design question queues for Ana. The four tech leads are good engineers, but <span class="hl-pink">none of them has ever designed a whole system</span> from requirements to trade-offs, and there's no safe place to practise.</p>
  <ul>
    <li>Design skills grow only by designing, and real projects come rarely.</li>
    <li>The architect becomes a bottleneck and a single point of failure.</li>
    <li>Engineers learn trade-offs from incidents, the expensive way.</li>
  </ul>""",
    problem_figs=[ka_problem],
    analogy_side="chess puzzles",
    analogy="""  <p>Chess players don't only improve by playing whole games. They solve <b>puzzles</b>: a set position, a time limit, find the best move, then compare with a <b>coach</b>. Hundreds of positions a year, each short and safe to get wrong. The whole games get better because the positions are familiar.</p>""",
    analogy_figs=[ka_analogy],
    map=[("A set position", "The brief: Larder in Antwerp"),
         ("The time limit", "90 minutes to design"),
         ("Finding the move", "Choosing an architecture and naming the trade-offs"),
         ("The coach", "Judges: Ana, Eli, and Grace as the customer"),
         ("Hundreds of puzzles", "A new brief every month")],
    how_side="brief, teams, 90 minutes, feedback",
    how="""  <p>The first kata used a real future problem: <b>Antwerp</b>. Three teams found different things: one spotted that Belgian VAT on business invoices needed the billing service early; one chose separate stock per country and named the cost; one forgot Bancontact refunds entirely, and learned more than the others. The feedback was about <b>trade-offs and clarity</b>, not right answers. Now it's monthly, and the tech leads take turns writing briefs.</p>""",
    how_figs=[ka_how],
    steps=[("Write a brief", "One page: the business, users, a few requirements and constraints, and something deliberately unclear."),
           ("Form small teams", "Three people, mixed teams and levels, one tech lead each."),
           ("Design for 90 minutes", "Whiteboard or paper; questions to the “customer” allowed."),
           ("Present for 10 minutes", "Context, the main choices, the trade-offs, the risks."),
           ("Give feedback, not grades", "On requirements found, trade-offs named and clarity. What would you ask in a real review?"),
           ("Repeat monthly", "A new brief each time; let others write them.")],
    vocab=[("Kata", "A short, repeated practice exercise."),
           ("Brief", "The made-up or future system to design."),
           ("Customer role", "Someone who answers questions as the client would."),
           ("Trade-off", "What each choice gains and gives up."),
           ("Feedback", "Comments on reasoning and clarity, not a single right answer."),
           ("Growing architects", "Building design skills across the team.")],
    code=dict(file="docs/katas/2027-01-antwerp.md", note="the first kata brief, 19 January 2027", plain=True, src="""
# Architecture kata · Larder in Antwerp                 90 min design · 10 min present

The business  Larder opens in Antwerp (planning date Sep 2027): express and slots,
              consumers first, offices later. Two stores to start.
Users         customers (French and Dutch), pickers, couriers, Larder for Business
Requirements  - the apps in French and Dutch
              - Belgian VAT on invoices; Bancontact payments and refunds
              - stock and prices per country; a product can exist in one country only
              - customer data stays in the EU (it does today)
Constraints   18 engineers; no new database types without an ADR; modular monolith
Unclear       Will Dutch stores ever serve Belgian customers? (ask the customer: Grace)

Present       context · 3 main decisions · the trade-off you're least sure of · top risk
Judges        Ana, Eli; Grace plays the customer
"""),
    tools="tools: a room, a whiteboard per team, a timer. Ted Neward's kata list (nealford.com/katas) and the O'Reilly Architectural Katas competitions for ready-made briefs.",
    gains=["<b>Design practice</b> without real-world risk.",
           "<b>More people who can design</b>: less architect bottleneck.",
           "<b>Shared vocabulary</b> for trade-offs.",
           "<b>Real insights</b> when the brief is a real future problem.",
           "<b>Fun</b>: teams like it."],
    losses=["<b>Two hours a month</b> for nine to twelve people.",
            "<b>Made-up briefs</b> can feel artificial.",
            "<b>Feedback needs skill</b> to be useful, not judgemental.",
            "<b>Doesn't replace real projects</b>."],
    baseline="Each line compares <b>design skills learned only on real projects, with one architect</b> to <b>monthly katas with briefs, small teams, short presentations and feedback</b>.",
    ratings=[(3, 4, "Teams practise explaining designs clearly."),
             (3, 3, "Indirect."),
             (2, 4, "More people can make design decisions."),
             (3, 4, "Antwerp risks surfaced months early."),
             (3, 3, "Neutral."),
             (3, 3, "Briefs and notes kept, lightly."),
             (3, 3, "Teams name costs as trade-offs."),
             (3, 3, "Two hours a month."),
             (1, 5, "Tech leads grow into designers; Ana stops being the only one.")],
    pitfalls=[("Grading", "A winner and two losers.", "feedback on reasoning; no single right answer."),
              ("Briefs too big", "A whole bank in 90 minutes.", "a few requirements and one thing unclear."),
              ("Same people every time", "The tech leads only.", "mix levels; let juniors present."),
              ("Once only", "A great afternoon, never repeated.", "monthly, with rotating brief writers.")],
    use=["Teams growing faster than their architects.",
         "Preparing for a known future problem (a new country).",
         "Building design skills in tech leads.",
         "Team-building with a real purpose."],
    skip=["Teams in crisis: fix the crisis first.",
          "As a substitute for involving engineers in real designs."],
    related=["<b>Whiteboard sessions</b> (this volume)", "<b>Explaining trade-offs to non-engineers</b> (this volume)", "<b>Growing other architects</b> (Vol. 6)", "<b>Last responsible moment</b> (Vol. 2)"],
    quiz=[("What are the parts of a kata?", "A brief, small teams, a timebox to design, short presentations, feedback."),
          ("What should the feedback focus on?", "Requirements found, trade-offs named, and clarity, not a single right answer."),
          ("Why use a real future problem?", "Practice and real insight at the same time, like Antwerp's VAT and Bancontact."),
          ("How often?", "Monthly, with a new brief and rotating brief writers.")],
    try_it="Write a one-page brief for a problem your team will face next year. Run a 90-minute kata with two teams of three, ten-minute presentations and 20 minutes of feedback. Note one insight you'll use for real.",
    remember="Practise <span class=\"hl\">positions</span>, not just whole games. A new <span class=\"hl\">puzzle</span> every month.",
    sources=["Ted Neward, “Architectural Katas” (architecturalkatas.com).",
             "Neal Ford, Architectural Katas list (nealford.com/katas).",
             "Dave Thomas, “Code Kata” (codekata.com, 2007).",
             "Mark Richards and Neal Ford, <i>Fundamentals of Software Architecture</i> (2020), on katas."],
)

NOTES = [WHITEBOARD, PRESENTING, EXPLAIN, KATAS]
