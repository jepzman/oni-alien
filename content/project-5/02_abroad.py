# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 5 · Abroad (the Stakeholders domain, part 2)
# Narrator: Sanne. Facts: docs/larder-casebook.md, "Book 3, Vol. 5"; numbers in the comment block of 01_involved.py.

STK = ["stakeholders"]

# ------------------------------------------------------------------ 05 Are We Being Understood?
mt_problem = Doodle(760, 260, "Doodle of Wednesday 3 February 2027 and Sanne's mistake for this collection. A ninety-minute meeting with Koen, sales manager of a produce wholesaler at Antwerp's early market, held in English with no agenda. Koen nods a lot. Sanne's notes say deliveries at 07:00 and crates returned free. Koen's proposal nine days later says deliveries at 05:30, as for all his shops, and a deposit on every crate.",
                    "Ninety minutes, in English, no agenda. Sanne heard 07:00 and free crates. Koen heard 05:30 and a deposit.", exact=True)
mt_problem.box(20, 24, 330, 140, None, "y")
mt_problem.head(185, 60, "Sanne's notes", size=19)
mt_problem.text(185, 94, "deliveries 07:00", size=16)
mt_problem.text(185, 122, "crates returned, free", size=16)
mt_problem.box(410, 24, 330, 140, None, "pink")
mt_problem.head(575, 60, "Koen's proposal, 12 Feb", size=19)
mt_problem.text(575, 94, "deliveries 05:30", size=16)
mt_problem.text(575, 122, "€2 deposit a crate", size=16)
mt_problem.note(380, 210, "a meeting that ended with two different decisions", "red", size=19)
mt_problem.note(380, 242, "nodding meant “I follow you”, not “I agree”", "pen", size=16)

mt_analogy = Doodle(760, 250, "Doodle of a pilot and a control tower. The tower says: climb to flight level two hundred. The pilot reads it back: climbing to flight level two hundred. Only then is it agreed. If the read-back is wrong, the tower corrects it at once. A message is not sent until it has been read back.",
                    "Tower and pilot: an instruction counts only when it's read back.", exact=True)
mt_analogy.box(14, 50, 300, 90, "tower", "blue", sub="“climb to two hundred”", size=18, subsize=14)
mt_analogy.box(446, 50, 300, 90, "pilot", "green", sub="“climbing to two hundred”", size=18, subsize=14)
mt_analogy.arrow(318, 80, 442, 80)
mt_analogy.arrow(442, 112, 318, 112)
mt_analogy.note(380, 186, "sent is not understood; read back is", "pen", size=19)
mt_analogy.note(380, 220, "a wrong read-back is corrected at once", "pen", size=16)

mt_how = Doodle(760, 430, "The second meeting with Koen, Wednesday 17 February 2027, rebuilt in five steps. Before: an agenda in Dutch two days ahead, with the three decisions needed: delivery time, crates, the weekly order cut-off. In the room: Larder's operations lead, a Flemish speaker, leads in Dutch; each decision is read back before moving on. After: a summary in Dutch within twenty-four hours, which Koen confirms by email. The decisions: deliveries at 05:30 at the back door, two euros deposit per crate, credited on return, orders by 14:00 the day before. The 05:30 delivery needs the permit's early hours: noted against risk R-07.",
                "Agenda before, read-back during, a written summary after, in Koen's language.", exact=True)
mt_how.row([("agenda", "in Dutch, 2 days ahead", "y"), ("the right voice", "ops lead, in Dutch", "blue"), ("read back", "each decision", "green"), ("summary", "Dutch, within 24 h", "y"), ("confirmed", "Koen, by email", "pink")], y=20, h=86, size=15, subsize=11, gap=10)
mt_how.box(14, 136, 732, 190, None, "paper")
mt_how.head(380, 168, "decided, 17 February", size=19)
for i, t in enumerate(["D1 deliveries 05:30, back door, Mon–Sat", "D2 crates: €2 deposit, credited on return", "D3 order by 14:00 the day before", "D4 a trial week before opening"]):
    mt_how.text(380, 204 + i * 30, t, size=16)
mt_how.box(14, 344, 732, 70, "D1 needs deliveries before 07:00", "pink", sub="→ the permit's early hours (risk R-07)", size=17, subsize=14, stroke="red")

MEETINGS = dict(
    slug="meetings-that-work",
    kicker="a.k.a. managing communications: making sure the message arrived and was understood",
    tldr="<b>Managing communications</b> means checking that a message was <b>received and understood</b>, not only sent. In meetings: an <b>agenda</b> naming the decisions needed, sent ahead in the other side's language; the <b>right voice</b> in the room; every decision <b>read back</b> before moving on; a short <b>written summary</b> within a day, which the other side confirms. Nodding means “I follow you”, not “I agree”. Across languages and cultures, assume nothing was agreed until it's written and confirmed.",
    chips=[("Family", "abroad"), ("Lives in", "agendas, read-backs and summaries"), ("Pairs with", "the communications plan, the decision log, stakeholders abroad")],
    pmbok=dict(covers="creating, sending and confirming project information so it is received and understood; running meetings that end in shared decisions",
               domains=STK, processes=["Manage Communications"], principles=["Be an accountable leader"], focus=["executing"],
               older="6th: “Manage Communications” (10.2), meeting management and communication skills. 7th: the Stakeholders domain."),
    problem_side="Antwerp, 3 February 2027",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. She meets <b>Koen</b>, sales manager of a produce wholesaler at Antwerp's early market, for ninety minutes, in English, with no agenda. Koen is friendly and nods a lot. Her notes say: deliveries at <b>07:00</b>, crates returned free. Nine days later his proposal arrives: deliveries at <b>05:30</b>, as for all his shops, and a <b>€2 deposit</b> on every crate. <span class="hl-pink">Neither of them was wrong about what they'd heard. Nothing had been agreed.</span> Two weeks are lost, and Koen, who thinks Larder is changing its mind, is now resistant.</p>
  <ul>
    <li>No agenda: nobody knew which decisions the meeting was for.</li>
    <li>English was Sanne's comfort, not Koen's.</li>
    <li>Nodding was taken for agreement; nothing was written down.</li>
  </ul>""",
    problem_figs=[mt_problem],
    analogy_side="the read-back",
    analogy="""  <p>When a control tower tells a pilot <b>“climb to flight level two hundred”</b>, the instruction doesn't count until the pilot <b>reads it back</b>: “climbing to flight level two hundred.” If the read-back is wrong, the tower corrects it at once. Aviation learned the hard way that a message sent is not a message understood, even between two professionals speaking the same language every day.</p>""",
    analogy_figs=[mt_analogy],
    map=[("The instruction", "A decision in a meeting: delivery time, crates, the order cut-off"),
         ("The read-back", "Each decision repeated, in Dutch, before moving on"),
         ("Correcting a wrong read-back", "Catching “07:00” vs “05:30” in the room, not nine days later"),
         ("Standard phrases", "An agenda naming the decisions needed"),
         ("The flight log", "A summary in Dutch within 24 hours, confirmed by Koen")],
    how_side="agenda, voice, read-back, summary, confirmation",
    how="""  <p>Sanne re-runs the meeting on <b>Wednesday 17 February</b>, in five steps. An <b>agenda in Dutch</b> goes out two days ahead with the three decisions needed: delivery time, crates, the weekly order cut-off. Larder's operations lead, a Flemish speaker, <b>leads in Dutch</b>; Sanne listens. Each decision is <b>read back</b> before the next one starts. A <b>summary in Dutch</b> goes out within 24 hours, and Koen <b>confirms it by email</b> the next morning. Four decisions: deliveries at <b>05:30</b> at the back door, Monday to Saturday; €2 deposit a crate, credited on return; orders by 14:00 the day before; a trial week before opening. Koen is supportive by the end of the month. Sanne notes one consequence: <b>05:30 deliveries need the store's early hours to be allowed</b>, and writes it against the permit risk, R-07.</p>""",
    how_figs=[mt_how],
    steps=[("Send an agenda that names the decisions", "In their language, ahead of time."),
           ("Bring the right voice", "Someone who speaks it as they do."),
           ("Read back each decision", "Before the next one starts."),
           ("Write a summary within a day", "Decisions, owners, dates."),
           ("Ask them to confirm it", "Silence isn't agreement."),
           ("Note what the decisions touch", "Risks, plan, contracts.")],
    vocab=[("Manage communications", "Making sure information is sent, received and understood."),
           ("Read-back", "Repeating a decision to confirm both sides mean the same."),
           ("Agenda", "The purpose and the decisions a meeting is for."),
           ("Meeting summary", "Decisions, owners and dates, sent after the meeting."),
           ("Noise", "Anything that distorts a message: language, jargon, assumptions."),
           ("High-context culture", "Where much of the meaning is left unsaid and read from the situation.")],
    code=dict(file="antwerp/05-supplier-meeting.md", note="Larder's operations lead and Sanne, Wednesday 17 February 2027", plain=True, src="""
# ANTWERP · MEETING WITH THE PRODUCE WHOLESALER (Koen)      Wed 17 Feb 2027 · 10:00–10:45
                                                           in Dutch · agenda sent Mon 15 Feb
DECISIONS NEEDED   delivery time · crates · order cut-off

DECIDED (read back in the room)                                        OWNER       BY
D1 deliveries 05:30 at the back door, Mon–Sat                          Koen        from opening
D2 crates: €2 deposit each, credited in full on return                 Koen / ops  first invoice
D3 orders by 14:00 the day before, through the wholesaler's portal     store mgr   from trial week
D4 a trial week of deliveries before opening                           both        2 weeks before

SUMMARY   sent Wed 17 Feb 16:00 (Dutch) · confirmed by Koen Thu 18 Feb 08:12
TOUCHES   D1 → deliveries before 07:00 → the store's permitted hours → risk R-07
LAST TIME 3 Feb: English, no agenda, no summary → 07:00 vs 05:30, free crates vs deposit
"""),
    tools="tools: an agenda that names decisions, the right speaker, a read-back habit, and a summary template.",
    dial=[("Light", "a quick call with a colleague", ["Say the decision aloud at the end.", "One line in chat after.", "Done."]),
          ("Standard", "Antwerp", ["Agenda with decisions, in their language.", "Read-back in the room.", "Summary in 24 h, confirmed."]),
          ("Heavy", "contracts, regulators", ["Formal minutes, signed.", "Interpreters for key meetings.", "Decisions only in writing."])],
    baseline="Each line compares <b>the meeting of 3 February (English, no agenda, no summary)</b> to <b>the meeting of 17 February (agenda in Dutch, read-backs, a confirmed summary)</b>.",
    ratings=[(3, 4, "The meeting produced decisions."),
             (2, 4, "Delivery terms are known, so the plan can rely on them."),
             (2, 4, "The 05:30 delivery was linked to a risk."),
             (2, 4, "Decisions are in writing, in both languages."),
             (1, 4, "Koen went from resistant to supportive."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Misunderstandings caught in the room."),
             (3, 3, "Fifteen minutes before, fifteen after.")],
    pitfalls=[("No agenda", "Nobody knows what to decide.", "name the decisions needed."),
              ("Your language, not theirs", "They follow; they don't agree.", "meet in their language, or with a voice who speaks it."),
              ("Nodding taken as yes", "Two versions of the meeting.", "read each decision back."),
              ("No summary", "Memory decides.", "write it within a day, ask them to confirm.")],
    use=["Any meeting that should end in a decision.", "Across languages or companies.", "With suppliers and authorities.", "When people later remember a meeting differently."],
    skip=["A daily stand-up within a team: a board already records it."],
    related=["<b>Who Hears What, and When?</b> (this volume)", "<b>Discovery Workshops</b> (Ana, vol. 6)", "<b>Different Country, Different Rules</b> (next note)", "<b>Is the Work Actually Happening?</b> (vol. 2)"],
    quiz=[("What does nodding mean in a meeting?", "Often “I follow you”, not “I agree”."),
          ("Name the five steps of the second meeting.", "Agenda in Dutch, the right voice, read-backs, summary in 24 h, confirmation."),
          ("What did decision D1 touch?", "The store's permitted hours: deliveries before 07:00 → the permit risk R-07."),
          ("A supplier's summary says something different from yours. What do you do?", "Call the same day, agree the wording, send one corrected summary both confirm."),
          ("Your sponsor wants to skip the agenda “to keep it informal” with a regulator. Answer them.", "Informal is fine; unclear isn't. An agenda with the questions to answer respects their time and gives a record.")],
    try_it="After your next meeting, write the decisions in three lines and send them to everyone who was there. Count how many replies correct something.",
    remember="Sent is not <span class=\"hl\">understood</span>. Read it <span class=\"hl\">back</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain, managing communications.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 10.2 Manage Communications.",
             "Edward T. Hall, <i>Beyond Culture</i> (1976): high- and low-context communication."],
)

# ------------------------------------------------------------------ 06 Different Country, Different Rules
ab_problem = Doodle(760, 260, "Doodle of Monday 8 February 2027. Lena, Maarten the Antwerp lawyer and Sanne walk through the launch plan rule by rule. Most of it Sanne knew: VAT, Bancontact, French and Dutch in the apps. One rule she didn't: in Antwerp a cooling plant of that size and lorries before seven need an environmental permit, decided after a public inquiry, and it can take months. In Rotterdam the cold room needed nothing.",
                    "Rotterdam's cold room needed nothing. Antwerp's needs a permit, after a public inquiry.", exact=True)
ab_problem.box(20, 24, 330, 140, None, "green")
ab_problem.head(185, 60, "Rotterdam, 2026", size=19)
ab_problem.text(185, 94, "cold room: no permit", size=16)
ab_problem.text(185, 122, "deliveries from 07:30", size=16)
ab_problem.box(410, 24, 330, 140, None, "pink")
ab_problem.head(575, 60, "Antwerp, 2027", size=19)
ab_problem.text(575, 94, "environmental permit", size=16)
ab_problem.text(575, 122, "public inquiry, months", size=16)
ab_problem.note(380, 210, "“the same launch” in a country with other rules", "red", size=19)
ab_problem.note(380, 242, "Maarten: “here it's a permit, with a public inquiry”", "pen", size=16)

ab_analogy = Doodle(760, 250, "Doodle of driving a hired car abroad. Same car, same driving. But the other side of the road, different speed limits, a sticker for the motorway, headlights on in daytime, priority from the right. The local who rents you the car spends five minutes listing them. Those five minutes are the cheapest part of the holiday.",
                    "Driving abroad: same car, other rules. Five minutes with a local is the cheapest part of the trip.", exact=True)
ab_analogy.row([("side of the road", "", "pink"), ("speed limits", "", "y"), ("motorway sticker", "", "y"), ("priority right", "", "pink")], y=40, h=70, size=16)
ab_analogy.note(380, 160, "same car, same driver, other rules", "pen", size=19)
ab_analogy.note(380, 200, "ask the person at the hire desk before you set off", "pen", size=16)

ab_how = Doodle(760, 470, "Antwerp's map of Belgian differences, Monday 8 February 2027, nine rows with an owner and a date. Environmental permit for the cooling plant and deliveries before seven: Sanne, then Hilde the permit agent, application by end of March. Food-safety registration before the first sale: Lena, September. VAT at six and twenty-one percent, Belgian invoices: Marco, March. Bancontact: Cho, July. Staff documents in Dutch: Joost, May. Sector pay scales for store staff: Joost, April. Courier contracts: Joost and Lena, May. Alcohol: beer and wine from sixteen, spirits from eighteen: Grace, May. Structured e-invoices for business customers: Ana, later. And three habits: formal letters, an early informal meeting with the city before applying, every decision confirmed in writing.",
                "Nine rules, each with an owner and a date, and three habits. Row 1 was new to everyone.", exact=True)
rules = [("environmental permit", "cooling + before 07:00", "Sanne → Hilde", "end Mar"),
         ("food-safety registration", "before first sale", "Lena", "Sep"),
         ("VAT 6 % / 21 %, invoices", "Belgian rules", "Marco", "Mar"),
         ("Bancontact", "first payment method", "Cho", "Jul"),
         ("staff documents in Dutch", "Flanders", "Joost", "May"),
         ("sector pay scales", "store staff", "Joost", "Apr"),
         ("courier contracts", "Belgian status rules", "Joost + Lena", "May"),
         ("alcohol 16 / 18", "beer, wine / spirits", "Grace", "May"),
         ("structured e-invoices", "business customers", "Ana", "later")]
for i, (a, b, c, d) in enumerate(rules):
    y = 14 + i * 40
    fill = "pink" if i == 0 else ("y" if i % 2 else "paper")
    ab_how.box(8, y, 744, 34, None, fill, rx=4)
    ab_how.text(18, y + 23, a, anchor="start", size=14)
    ab_how.text(270, y + 23, b, anchor="start", size=13)
    ab_how.text(470, y + 23, c, anchor="start", size=14)
    ab_how.text(680, y + 23, d, anchor="start", size=14)
ab_how.box(8, 384, 744, 76, None, "blue", rx=6)
ab_how.head(380, 410, "three habits", size=17)
ab_how.text(380, 440, "formal letters · meet the city before applying · confirm every decision in writing", size=14)

ABROAD = dict(
    slug="stakeholders-abroad",
    kicker="a.k.a. stakeholders abroad: regulators, local law, language and habits",
    tldr="A project in a new country meets <b>new regulators</b>, <b>new laws</b>, a <b>new language</b> and <b>new habits</b>, inside a plan that looks just like the last one. Map the differences early, rule by rule, with <b>someone who practises there</b> (a lawyer, an agent, a local manager): what the rule is, who at your organisation owns it, by when it must be met, and how long the authority takes. Treat regulators as stakeholders with their own procedures and calendars. The differences you don't know are the ones that set the date.",
    chips=[("Family", "abroad"), ("Lives in", "a map of differences, one row per rule, beside the register"), ("Pairs with", "the stakeholder register, the project environment, the risk register")],
    pmbok=dict(covers="finding the stakeholders, rules and habits a new country or culture brings, and planning how to work with regulators and local partners",
               domains=STK + ["risk"], processes=["Identify Stakeholders", "Plan Stakeholder Engagement"], principles=["Adopt a holistic view", "Integrate sustainability within all project areas"], focus=["planning"],
               older="6th: enterprise environmental factors (2.2) and cultural awareness (3.4.4). 7th: the Stakeholders domain and the project environment."),
    problem_side="Antwerp, 8 February 2027",
    problem="""  <p class="lead">Lena, <b>Maarten</b> (the Antwerp lawyer she has engaged) and Sanne walk through the launch plan <b>rule by rule</b>. Most of it Sanne knows: VAT, Bancontact, French and Dutch in the apps. Then Maarten reaches the cold room. <span class="hl-pink">“In Rotterdam your cold room needed nothing. Here, a cooling plant that size and lorries before seven need an environmental permit from the city, decided after a public inquiry. It can take months.”</span> The plan has no line for it. The register has the permit office in the wrong box, and the risk register has the permit at a score of 3, with no owner.</p>
  <ul>
    <li>The plan was Rotterdam's plan, translated.</li>
    <li>The authority's calendar wasn't in the schedule.</li>
    <li>The lawyer was asked about contracts, not about the plan.</li>
  </ul>""",
    problem_figs=[ab_problem],
    meanwhile=[("product-6", "localisation", "Grace's localisation for Belgium: French and Dutch by native writers, Belgian VAT shown correctly, Bancontact first, tested with forty Antwerp households.",
                "Sanne's map of Belgian differences covers the launch around the app: permits, food safety, staff documents, couriers and the habits of working with a Flemish city.")],
    analogy_side="the hired car abroad",
    analogy="""  <p>Hiring a car abroad, you drive the same way you always do, but the rules aren't the same: the <b>other side of the road</b>, different <b>speed limits</b>, a <b>sticker</b> for the motorway, <b>priority from the right</b>. The person at the hire desk can list them in five minutes. Those five minutes are the cheapest part of the holiday, and the only part most people skip.</p>""",
    analogy_figs=[ab_analogy],
    map=[("The same car", "The same launch plan: Rotterdam's"),
         ("The other side of the road", "An environmental permit for the cooling plant and early deliveries"),
         ("The motorway sticker", "Food-safety registration before the first sale"),
         ("Speed limits, priority from the right", "VAT rates, staff documents in Dutch, sector pay scales"),
         ("The person at the hire desk", "Maarten, and from March Hilde, the permit agent")],
    how_side="one row per rule, an owner and a date, and the authority's calendar in the plan",
    how="""  <p>The meeting ends with a <b>map of nine differences</b>, each with an <b>owner</b> and a <b>date</b>: the environmental permit (Sanne, then Hilde, a permit agent Maarten recommends, from 8 March); food-safety registration with FAVV-AFSCA before the first sale (Lena); VAT at 6 % and 21 % and Belgian invoices (Marco, March); Bancontact (Cho, July); staff documents in Dutch, as the law in Flanders requires (Joost); sector pay scales for store staff (Joost); courier contracts (Joost and Lena); beer and wine from 16, spirits from 18 (Grace); structured e-invoices for business customers (Ana, later). And <b>three habits</b> Maarten insists on: formal letters; an <b>informal meeting with the city before applying</b>, which is how things are done there; every decision confirmed in writing. The permit's calendar goes into the schedule the same week: an application, a completeness check, a 30-day public inquiry, a decision. Sanne re-places the permit office on the grid and takes the permit risk to the builder on Wednesday.</p>""",
    how_figs=[ab_how],
    steps=[("Walk the plan rule by rule with a local expert", "Not only the contracts."),
           ("Write each difference as a row", "The rule, the owner, the date."),
           ("Put each authority's calendar in the schedule", "Steps, durations, inquiries."),
           ("Ask about habits, not just law", "Letters, meetings, how decisions are confirmed."),
           ("Update the register and the risks", "The same day."),
           ("Hire local help where it pays", "An agent, a local manager.")],
    vocab=[("Regulator", "An authority whose permit, registration or inspection the project needs."),
           ("Environmental permit", "Permission from the authorities to run an installation or activity that may affect the surroundings."),
           ("Public inquiry", "A period when the public can see an application and object to it."),
           ("Pre-application meeting", "An informal meeting with an authority before applying."),
           ("Permit agent", "A specialist who prepares and follows applications for you."),
           ("Enterprise environmental factors", "Conditions outside the team's control (laws, culture, markets) that shape the project.")],
    code=dict(file="antwerp/06-belgian-differences.md", note="Lena, Maarten and Sanne, Monday 8 February 2027", plain=True, src="""
# ANTWERP · WHAT'S DIFFERENT IN BELGIUM                                 8 Feb 2027

RULE                              WHAT IT MEANS FOR US                     OWNER        BY
Environmental permit (city)       cooling plant + deliveries before 07:00; Sanne→Hilde  lodge end Mar
                                  public inquiry 30 days, then a decision
Food-safety registration          FAVV-AFSCA, before the first sale        Lena         Sep
VAT 6 % food / 21 % other         prices, invoices, refunds                Marco        Mar
Bancontact                        first payment method in the app          Cho          Jul
Staff documents in Dutch          contracts, rules, payslips (Flanders)    Joost        May
Sector pay scales                 store staff wages, the people line       Joost        Apr
Courier contracts                 Belgian status rules                     Joost + Lena May
Alcohol                           beer, wine 16+ · spirits 18+             Grace        May
Structured e-invoices             business customers                       Ana          later

HABITS  formal letters (Maarten's office checks) · meet the city informally before
        applying · confirm every decision in writing
NEW     the permit's steps in the schedule · permit office → "manage closely" ·
        risk R-07 to be re-scored with the builder, Wed 10 Feb
"""),
    tools="tools: the launch plan, a local lawyer or agent, a table of differences, and the authority's own procedure.",
    dial=[("Light", "a small job abroad", ["A call with a local partner.", "A list of rules that differ.", "Owners for each."]),
          ("Standard", "Antwerp", ["A rule-by-rule walk with a local lawyer.", "A map with owners and dates.", "Authorities' calendars in the schedule; a local agent."]),
          ("Heavy", "entering a regulated market", ["A formal regulatory assessment.", "Local entity, local staff, local counsel.", "A regulatory plan per authority."])],
    baseline="Each line compares <b>Rotterdam's plan translated</b> to <b>a rule-by-rule map with a local lawyer, owners, dates and the authorities' calendars in the schedule</b>.",
    ratings=[(3, 4, "The launch meets the country it's in."),
             (2, 4, "The authority's calendar is in the dates."),
             (1, 4, "The rule that would set the date, found in February."),
             (2, 4, "Every difference has an owner."),
             (2, 4, "Lena sees the whole picture."),
             (3, 3, "Neutral."),
             (3, 4, "New rules have a place to go."),
             (2, 4, "Compliance designed in, not discovered."),
             (3, 3, "A morning, and a lawyer's fee.")],
    pitfalls=[("The plan translated", "The last country's assumptions.", "walk it rule by rule with a local."),
              ("Lawyer for contracts only", "The plan never gets checked.", "ask them about the plan."),
              ("Regulators as forms", "Their calendar sets your date.", "treat them as stakeholders, schedule their steps."),
              ("Law without habits", "Right papers, wrong way.", "ask how things are done there.")],
    use=["Any project in a new country, region or sector.", "When an authority's permission is needed.", "Before the plan is baselined.", "When local partners behave unexpectedly."],
    skip=["Never skip it abroad; at home, a quick check for new rules."],
    related=["<b>Who Matters Most, and How Much?</b> (this volume)", "<b>Localisation for a New Country</b> (Grace, vol. 6)", "<b>What Was Here Before Me?</b> (vol. 1)", "<b>How Likely, and How Bad?</b> (this volume)"],
    quiz=[("What did Maarten find that Sanne didn't know?", "An environmental permit, with a public inquiry, for the cooling plant and deliveries before 07:00."),
          ("What goes in each row of the map?", "The rule, what it means for the project, the owner, the date."),
          ("Name two of Maarten's habits.", "Formal letters; meet the city informally before applying; confirm decisions in writing."),
          ("Your next project is in Germany. Your German colleague says “it's just like here.” What do you do?", "Still walk the plan rule by rule with a local expert; similar isn't the same."),
          ("Why put the authority's steps into the schedule?", "Their durations (inquiry, decision) can set the end date; outside the schedule they're invisible.")],
    try_it="Take your plan to someone who knows the place it will run in. Ask them to stop you at every line where the rules or habits differ. Put each into a table with an owner and a date.",
    remember="Same car, <span class=\"hl\">other rules</span>. Ask at the <span class=\"hl\">hire desk</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain; the project environment.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 2.2 Enterprise Environmental Factors.",
             "Geert Hofstede, Gert Jan Hofstede and Michael Minkov, <i>Cultures and Organizations</i> (3rd ed., 2010)."],
)

# ------------------------------------------------------------------ 07 Are They Still With Us?
mo_problem = Doodle(760, 260, "Doodle of June 2027. The engagement matrix of 7 May scored the neighbours neutral: nine people came to the April meeting, fewer than in January, and nobody had emailed. Sanne read that as calm. On 22 June the permit's public inquiry closes with fourteen objections from the street: lorries before seven and condenser noise.",
                    "Nine came in April, so the street was “calm”. The inquiry closed with fourteen objections.", exact=True)
mo_problem.box(20, 24, 330, 140, None, "green")
mo_problem.head(185, 60, "matrix, 7 May", size=19)
mo_problem.text(185, 94, "neighbours: neutral", size=16)
mo_problem.text(185, 122, "(9 came, no emails)", size=16)
mo_problem.box(410, 24, 330, 140, None, "pink")
mo_problem.head(575, 60, "inquiry, 22 June", size=19)
mo_problem.text(575, 94, "14 objections", size=16)
mo_problem.text(575, 122, "lorries, condenser noise", size=16)
mo_problem.note(380, 210, "silence was read as support", "red", size=19)
mo_problem.note(380, 242, "the score came from attendance, not from asking", "pen", size=16)

mo_analogy = Doodle(760, 250, "Doodle of a doctor and a patient who says I'm fine. The doctor still takes the pulse and the blood pressure, and asks how the patient slept. Not coming to the follow-up appointment is not a sign of health. A check-up uses evidence, on a schedule.",
                    "“I'm fine” isn't a pulse. A check-up uses evidence, on a schedule.", exact=True)
mo_analogy.row([("“I'm fine”", "what they say", "y"), ("pulse, pressure", "what you measure", "green"), ("missed visit", "not a sign of health", "pink")], y=40, h=96, size=17, subsize=13)
mo_analogy.note(380, 196, "check on a schedule, from evidence", "pen", size=19)

mo_how = Doodle(760, 470, "Antwerp's engagement matrix re-scored monthly, from 5 March 2027, for six stakeholders. Each cell is a level with a one-line piece of evidence. Femke: leading throughout. Landlord: supportive throughout. Permit office: unaware in February, neutral from March after the pre-application meeting, neutral in July. Food-safety agency: unaware, neutral from May when registration was lodged. Neighbours: neutral, scored neutral in May from attendance, resistant in June with fourteen objections, neutral again in September after door-to-door visits with the new delivery hours. Koen the wholesaler: resistant in February, supportive from March. The red cell is May's neighbours: scored from silence.",
                "Six rows, one score a month, each with its evidence. The red cell was scored from silence.", exact=True)
months = ["Feb", "Mar", "May", "Jun", "Jul", "Sep"]
for k, m in enumerate(months):
    mo_how.head(250 + k * 88, 30, m, size=15)
grid = [("Femke", ["L", "L", "L", "L", "L", "L"]),
        ("landlord", ["S", "S", "S", "S", "S", "S"]),
        ("permit office", ["U", "N", "N", "N", "N", "N"]),
        ("food agency", ["U", "U", "N", "N", "N", "S"]),
        ("neighbours", ["N", "N", "N?", "R", "R", "N"]),
        ("Koen", ["R", "S", "S", "S", "S", "S"])]
fillmap = {"L": "green", "S": "green", "N": "y", "U": "paper", "R": "pink", "N?": "pink"}
for i, (name, vals) in enumerate(grid):
    y = 46 + i * 50
    mo_how.text(16, y + 28, name, anchor="start", size=15)
    for k, v in enumerate(vals):
        mo_how.box(210 + k * 88, y + 4, 80, 40, v, fillmap[v], size=15, rx=4, stroke="red" if v == "N?" else "")
mo_how.text(16, 372, "evidence, not mood:", anchor="start", size=15)
for i, t in enumerate(["permit office N (Mar): pre-application meeting 11 Mar, “a complete file”",
                       "neighbours R (Jun): 14 objections in the inquiry · N (Sep): door-to-door, 7:00 deliveries",
                       "neighbours N? (May): 9 of 46 at the meeting, no emails: silence, not support"]):
    mo_how.text(16, 398 + i * 24, t, anchor="start", size=13)

MONITOR_ENG = dict(
    slug="monitoring-engagement",
    kicker="a.k.a. monitoring stakeholder engagement and communications",
    tldr="<b>Monitor</b> engagement on a rhythm: re-score each key stakeholder every month on the engagement matrix, and write the <b>evidence</b> beside each score: what they said, did, signed, objected to. Silence, low attendance and “no complaints” are not support; when evidence is thin, <b>ask</b>. Check communications the same way: were the messages read, understood and acted on? A score that moves the wrong way is an early warning; act on it that week.",
    chips=[("Family", "abroad"), ("Lives in", "the engagement matrix, re-scored monthly, with evidence"), ("Pairs with", "the engagement plan, the communications plan, the risk review")],
    pmbok=dict(covers="checking regularly whether stakeholders are where the project needs them and whether communications are working, and adjusting the approach",
               domains=STK, processes=["Monitor Stakeholder Engagement", "Monitor Communications"], principles=["Be an accountable leader"], focus=["monitoring and controlling"],
               older="6th: “Monitor Stakeholder Engagement” (13.4) and “Monitor Communications” (10.3). 7th: the Stakeholders and Measurement domains."),
    problem_side="Antwerp, May → June 2027",
    problem="""  <p class="lead">From March, Sanne re-scores the engagement matrix on the first Friday of each month. On <b>7 May</b> the neighbours are <b>neutral</b>: only nine people came to the April meeting, fewer than in January, and nobody has emailed. She reads that as calm. The permit application has been in the city's public inquiry since 24 May. <span class="hl-pink">It closes on 22 June with fourteen objections from the street: lorries before seven and condenser noise.</span> The neighbours hadn't gone quiet because they were happy. They were waiting for the inquiry, the place where their objections would count.</p>
  <ul>
    <li>Scores came from attendance and email, not from asking.</li>
    <li>“No complaints” was taken for support.</li>
    <li>The inquiry was a new channel the plan didn't watch.</li>
  </ul>""",
    problem_figs=[mo_problem],
    analogy_side="the check-up",
    analogy="""  <p>A patient says <b>“I'm fine.”</b> The doctor still takes the <b>pulse</b> and the <b>blood pressure</b>, and asks how they've been sleeping. A patient who skips the follow-up appointment isn't healthier for it. A good check-up runs <b>on a schedule</b>, measures something, and asks direct questions when the numbers are thin.</p>""",
    analogy_figs=[mo_analogy],
    map=[("“I'm fine”", "No complaints from the street"),
         ("The pulse", "Evidence: what each stakeholder said, did, signed or objected to"),
         ("The missed appointment", "Nine of forty-six households at the April meeting"),
         ("The scheduled check-up", "The matrix re-scored on the first Friday of each month"),
         ("Asking how they slept", "Door-to-door visits when evidence is thin")],
    how_side="a monthly score, with evidence, and action when it drops",
    how="""  <p>Each first Friday, Sanne re-scores the six stakeholders that matter most and writes <b>one line of evidence</b> per score. The permit office goes from unaware to <b>neutral</b> after the pre-application meeting of 11 March (“a complete file, please, and the noise study”); Koen to <b>supportive</b> after the second meeting. After June she adds a rule: <b>no evidence, no score</b>; silence is marked “?” and triggers a question. The neighbours' “resistant” in June turns into action: in the last week of July Sanne and <b>Inès</b>, the new store manager, go <b>door to door</b> on the street with the changed plan (deliveries from 07:00, an acoustic screen on the condenser). In September they're <b>neutral</b> again; nine of them come to the opening. Communications get the same check: the waitlist emails are opened by 58 % in Dutch and 31 % in French; Priya's team rewrites the French subject lines with Grace's writers and the gap halves.</p>""",
    how_figs=[mo_how],
    steps=[("Re-score key stakeholders monthly", "On a fixed day."),
           ("Write the evidence beside each score", "Said, did, signed, objected."),
           ("Treat silence as a question", "Ask, visit, call."),
           ("Watch every channel they can use", "Inquiries, complaints, the press."),
           ("Check messages were read and understood", "Not only sent."),
           ("Act the same week a score drops", "With an owner.")],
    vocab=[("Monitoring engagement", "Checking whether stakeholders are where the project needs them, and adjusting."),
           ("Evidence", "What a stakeholder actually said or did, not your impression."),
           ("Monitoring communications", "Checking that information reached people and was understood."),
           ("Leading indicator", "A sign that comes before the problem, like a falling score."),
           ("Channel", "A way stakeholders can be heard: meetings, emails, inquiries, the press."),
           ("Open rate", "The share of people who opened an email.")],
    code=dict(file="antwerp/07-engagement-review.md", note="Sanne, monthly from Friday 5 March 2027 (extract)", plain=True, src="""
# ANTWERP · ENGAGEMENT REVIEW                       first Friday of the month · from 5 Mar 2027

STAKEHOLDER     FEB  MAR  MAY  JUN  JUL  SEP  NEEDED  EVIDENCE (latest)
Femke           L    L    L    L    L    L    L       chairs every steering group
Landlord        S    S    S    S    S    S    S       keys handed over 1 Jun, works approved
Permit office   U    N    N    N    N    N    S*      decision 6 Sep after amended hours
Food agency     U    U    N    N    N    S    N       registration lodged May, visit 29 Sep
Neighbours      N    N    N?   R    R    N    S       14 objections (Jun) → door to door with
                                                      07:00 deliveries + screen (26-30 Jul)
Koen            R    S    S    S    S    S    S       trial week booked

RULE (from Jun)  no evidence, no score: "?" means ask this week
* a regulator stays neutral; "S" here means confident in a complete application
COMMS CHECK      waitlist emails opened: nl 58 % · fr 31 % → French subject lines
                 rewritten (Grace's writers), fr 44 % in Aug
"""),
    tools="tools: the engagement matrix, an evidence column, a calendar reminder, email open rates, and shoe leather.",
    dial=[("Light", "a few stakeholders you see often", ["Ask them how it's going.", "Note anything that changes.", "Monthly."]),
          ("Standard", "Antwerp", ["Matrix re-scored monthly with evidence.", "Silence triggers a question.", "Communications checked for reading and understanding."]),
          ("Heavy", "large public projects", ["Surveys and sentiment tracking.", "Complaint and objection logs.", "Independent engagement reviews."])],
    baseline="Each line compares <b>scoring from attendance and silence</b> to <b>a monthly score with written evidence, silence treated as a question</b>.",
    ratings=[(3, 4, "Effort goes to the stakeholders slipping away."),
             (2, 3, "Drops are seen a month earlier."),
             (2, 4, "Silence is no longer read as support."),
             (2, 4, "Each score shows its evidence."),
             (2, 4, "The street saw Larder come to them."),
             (3, 3, "Neutral."),
             (3, 4, "The approach changes when a score drops."),
             (3, 3, "Neutral."),
             (3, 3, "An hour a month, and some doorbells.")],
    pitfalls=[("Silence as support", "They may be waiting for a better channel.", "ask."),
              ("Scores from mood", "Optimism in a table.", "write the evidence."),
              ("Only your channels", "Objections arrive elsewhere.", "watch every channel they can use."),
              ("Sent = understood", "Nobody read it.", "check reading and understanding.")],
    use=["Monthly through the project.", "Before and during any formal consultation.", "When a stakeholder goes quiet.", "After every big message."],
    skip=["When nobody outside the team is affected."],
    related=["<b>Who Matters Most, and How Much?</b> (this volume)", "<b>How Do We Keep Them With Us?</b> (this volume)", "<b>Is the List Still True?</b> (this volume)", "<b>Where Are We, Really?</b> (vol. 2)"],
    quiz=[("What goes beside each score?", "One line of evidence: what they said, did, signed or objected to."),
          ("Why was May's “neutral” wrong?", "It came from low attendance and no emails; the neighbours were waiting for the inquiry."),
          ("What did the French open rate show?", "Messages sent weren't read: 31 % vs 58 %; subject lines rewritten."),
          ("A key supplier stops replying for two weeks. What does the matrix say to do?", "Mark it “?”, call or visit that week, and score from what you learn."),
          ("Femke asks why the neighbours are “resistant” in June when nobody complained to Larder. Explain.", "They objected in the public inquiry, a channel the plan didn't watch; silence to Larder wasn't support.")],
    try_it="For your three most important stakeholders, write their attitude and one piece of evidence from the last month. Where you have no evidence, call them this week.",
    remember="“I'm fine” isn't a <span class=\"hl\">pulse</span>. Silence is a <span class=\"hl\">question</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain, monitoring engagement and communications.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 13.4 Monitor Stakeholder Engagement; 10.3 Monitor Communications.",
             "Lynda Bourne, <i>Stakeholder Relationship Management</i> (2009)."],
)

NOTES = [MEETINGS, ABROAD, MONITOR_ENG]
