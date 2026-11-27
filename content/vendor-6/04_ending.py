# Series 5 · On the Client's Floor · Vol. 6 · The Cost and the Ending · Endings (notes 13–15).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 6".
# The series ends open: note 15 stops at the door of room 27A. Do not resolve it.
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 13 How Do We Leave Well?
lw_problem = Doodle(760, 240, "Doodle of what's left in June 2029, whatever the phase 2 decision. Wave 1's contract ends on 30 June. The promises register still has 3 open lines out of 47. Room 19C is full of two years of paper. Bert retires in the autumn. And Lottie has been offered a job at MetroVolt.",
                    "3 promises open, two years of paper, Bert retiring, and Lottie's offer.", exact=True)
for i, (t, fill) in enumerate([("wave 1 ends 30 Jun", "y"), ("promises: 3 of 47 open", "pink"), ("room 19C: 2 years of paper", "paper"), ("Lottie: an offer", "blue")]):
    lw_problem.box(14 + (i % 2) * 374, 20 + (i // 2) * 90, 358, 70, t, fill, size=19)

lw_how = Doodle(760, 330, "Leaving well. Finish what you promised: the last 3 of 47 promises closed by 14 June. Leave the documents tidy: room 19C cleared, 2 years of paper archived or shredded under the confidentiality clause, the handbook and runbooks current. Thank people by name and in writing: 31 letters, to MetroVolt people and their managers. Keep the relationships: no bad words about anyone, Vexmoor included. And support your people's choices, even when they leave you.",
                "Finish the promises, tidy the paper, thank people by name, keep the relationships.", exact=True)
for i, (h, sub, fill) in enumerate([("promises", "47 of 47", "green"), ("paper", "archived, shredded", "paper"), ("thanks", "31 letters, by name", "y"), ("people", "their choices", "blue")]):
    lw_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=13)
lw_how.box(14, 160, 732, 70, "a thank-you letter to someone's manager is remembered for years", "y", size=17)
lw_how.note(380, 280, "leave the floor as if you'll be back", "red", size=19)

LEAVING_WELL = dict(
    slug="leaving-well", date=date(2029, 6, 11), meta=on_site(date(2029, 6, 11)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. finishing an engagement properly",
    tldr="However the next decision goes, this engagement is ending, and endings are remembered. <b>Finish what you promised</b>, <b>leave the documents tidy</b>, <b>thank people by name and in writing</b> (copied to their managers), say nothing bad about anyone, and <b>support your people's choices</b>, even when they choose the client. Leave the floor as if you'll be back.",
    chips=[("Family", "endings"), ("Lives in", "the promises register · 31 letters · room 19C, empty"), ("Pairs with", "the promises register (vol. 1), the case study")],
    problem_side="Floor 19, 11 June 2029",
    problem="""  <p class="lead">Wave 1's contract ends on <b>30 June</b>. The phase 2 decision is due on Friday. Whatever it is, this part of the engagement is over.</p>
  <ul>
    <li>The <b>promises register</b> (47 lines since the orals of May 2027) still has <b>3 open</b>.</li>
    <li>Room 19C, the goldfish bowl, holds two years of paper.</li>
    <li>Bert retires in the autumn.</li>
    <li>And this morning Lottie tells Ines, nervously, that <span class="hl-pink">MetroVolt has offered her a job</span> on Kemi's run team.</li>
  </ul>""",
    problem_figs=[lw_problem],
    sides=dict(client=("MetroVolt", "<p>MetroVolt will remember the last month more clearly than the middle year. A supplier that leaves tidily, keeps its promises to the end and thanks people properly is one it will want back, or recommend. One that disappears after the last invoice is remembered too.</p>", "How they leave is how we'll describe them."),
                vendor=("Ines", "<p>Ines is tired, proud and uncertain. The team is half packed. Lottie's news stings for an hour, then it doesn't: Lottie applied to a public advert, she's good, and she'd be good at MetroVolt. Wrenfield might lose phase 2 and Lottie in the same week.</p>", "Finish it properly. Whatever happens on Friday.")),
    sides_after="The end of an engagement is the part both sides remember. Make it the tidiest part.",
    analogy_side="leaving a holiday cottage",
    analogy="""  <p>Good guests leave a holiday cottage <b>cleaner than they found it</b>: beds stripped, bins emptied, a note in the visitors' book thanking the owner by name and mentioning the thing they loved. They didn't have to. It's why the owner gives them the good week next year, and tells friends about them.</p>""",
    map=[("Beds stripped, bins emptied", "Room 19C cleared, paper archived"),
         ("Things you said you'd fix", "The last 3 promises"),
         ("The note in the visitors' book", "31 thank-you letters, by name"),
         ("The good week next year", "A client who'd have you back"),
         ("Telling friends", "References, and Lottie's future")],
    how_side="promises, paper, thanks, relationships, people",
    how="""  <p><b>Finish what you promised.</b> The last three open lines: P-31 (a training session for Customer Ops team leaders, run Tuesday 12 June), P-40 (the data dictionary, delivered to Bilal's MetroVolt counterpart), P-44 (Bert's book reprinted and bound, three copies). <b>47 of 47 closed</b> by Thursday 14 June.</p>
  <p><b>Leave the documents tidy.</b> Room 19C is cleared: two years of paper either archived to MetroVolt's records team or shredded under §16 (confidentiality). The handbook and runbooks are checked for the last time. The whiteboard wall is photographed and wiped.</p>
  <p><b>Thank people by name, in writing.</b> Ines writes <b>31 letters</b>: Elaine, Hollis, Desmond, Anjali, Nkem, Kofi, Rosa, the run team, Yusuf from the service desk, Bert. Each names one specific thing they did. Each is copied to their manager. Gareth gets one too, for IA-02.</p>
  <p><b>Keep the relationships.</b> No bad words about anyone, on the floor or in the pub, Vexmoor included. Ines offers Oliver's team a walkthrough of the handbook, whoever wins.</p>
  <p><b>Support your people's choices.</b> Lottie applied to a public advert, so §17's non-solicitation doesn't apply. Ines tells her: “You'd be brilliant there. Take a week, decide for yourself, and whatever you choose, I'll write you the reference.” Lottie hasn't decided.</p>""",
    how_figs=[lw_how],
    steps=[("Close every promise", "Or say clearly why not."),
           ("Tidy the paper", "Archive or shred, per the contract."),
           ("Update what you leave behind", "Handbook, runbooks, contacts."),
           ("Thank people by name, in writing", "Copied to their managers."),
           ("Say nothing bad about anyone", "Including rivals."),
           ("Support your people's choices", "Even when they choose the client.")],
    vocab=[("Engagement close", "The formal end of a supplier's work for a client."),
           ("Promises register", "A list of every commitment made, and its status."),
           ("Records retention", "Rules on what documents are kept, and for how long."),
           ("Non-solicitation", "A clause stopping one party recruiting the other's staff."),
           ("Alumni", "Former staff, who often become clients or partners."),
           ("Goodwill", "The value of a good reputation and relationships.")],
    code=dict(file="delivery/lodestar/close.md", note="closed Thu 14 Jun 2029", src="""
ENGAGEMENT CLOSE · Lodestar wave 1 · contract ends 30 Jun 2029

promises     47 of 47 closed (P-31 training Tue 12 Jun · P-40 data dictionary ·
             P-44 Bert's book bound, 3 copies)
paper        room 19C cleared · archived to MetroVolt records (2 boxes) ·
             shredded under §16 (11 sacks) · whiteboard photographed, wiped
documents    handbook v1.1 · 11 runbooks · contact list · all current
thanks       31 letters, each naming one thing, each cc'd to their manager
rivals       walkthrough of the handbook offered to Vexmoor, whoever wins
people       Lottie: MetroVolt offer (public advert, §17.2) · her decision · reference promised
"""),
    contract=dict(side="what the contract says about leaving", doc="Lodestar SOW · §16.4 and §17.2", date="signed 30 June 2027", stamp="left tidy",
                  clauses=[("16.4", "On expiry, the Supplier shall return or securely destroy MetroVolt's Confidential Information.", "11 sacks. the shredding van came at 07:00."),
                           ("17.2", "Clause 17.1 does not prevent either Party employing a person who responds to a general advertisement.", "Lottie answered an advert. her choice, not a breach.")],
                  plain="exit clauses cover the paper; non-solicitation clauses usually allow staff to answer public adverts. Neither covers the thank-you letters, which matter most."),
    health=dict(now="g",
                g=("a tidy ending", ["All promises closed.", "Letters sent.", "Relationships intact."]),
                a=("loose ends", ["Close or explain each.", "Tidy the paper.", "Thank people anyway."]),
                r=("a bitter ending", ["Say nothing bad.", "Finish what you promised.", "Leave the door open."])),
    pressure=dict(level=3, title="the ending", cost="31 letters · 11 sacks of paper · maybe Lottie",
                  items=["Nobody checks whether the last three promises were kept. Everyone notices if they weren't.", "Lottie's offer is a compliment to the team that trained her. It's also her life."]),
    baseline="Each line compares <b>a last invoice and a quiet exit</b> with <b>every promise closed, tidy paper, 31 letters by name and a supplier that wishes its people well</b>.",
    ratings=[(3, 5, "MetroVolt remembers a tidy ending."),
             (3, 4, "The team leaves proud."),
             (3, 3, "A week of tidying."),
             (3, 3, "Neutral."),
             (3, 4, "Documents current for whoever follows."),
             (3, 4, "No loose promises."),
             (3, 5, "§16.4 met; the register closed."),
             (3, 3, "A week."),
             (3, 3, "Letters take an evening each week.")],
    pitfalls=[("Disappearing after the invoice", "Remembered.", "finish properly."),
              ("Open promises", "Someone was relying on one.", "close or explain."),
              ("Generic thanks", "Forgotten by Friday.", "by name, one thing, cc their manager."),
              ("Bitterness about a rival", "It reaches the client.", "say nothing bad."),
              ("Resenting a team member's choice", "You lose them twice.", "support it.")],
    grimoire=[(8, "life-after-dungeon", "Life After the Dungeon", "is the inside version: leaving a place well, and carrying the good parts with you.")],
    use=["The end of any engagement.", "Before a phase decision.", "When people move on."],
    skip=["Never skip it."],
    related=["<b>Who Remembers What We Promised?</b> (vol. 1)", "<b>Can We Tell Lodestar's Story?</b> (this volume)", "<b>What Did the Vendor Side Teach Me?</b> (next note)", "<b>What Does It Leave Behind?</b> (Sanne, vol. 6)"],
    quiz=[("How many promises were in the register, and how many closed?", "47; all 47 by 14 June."),
          ("What happened to the paper in room 19C?", "Archived to MetroVolt's records or shredded under §16."),
          ("What made the thank-you letters different?", "Each named one specific thing and was copied to the person's manager."),
          ("Why doesn't non-solicitation stop Lottie's offer?", "She answered a general advertisement (§17.2)."),
          ("What did Ines tell Lottie?", "That she'd be brilliant there, to decide for herself, and that she'd write the reference either way.")],
    quiz_sit=[("Graham asks Ines to “have a word with Lottie” and talk her out of it. What does she say?", "No: it's Lottie's decision, she answered a public advert, and pressure would cost Wrenfield more than losing her. Offer her a reason to stay if there is one, honestly, then respect her choice.")],
    try_it="Think of the last project you left. Was every promise closed? Who did you thank by name? Write one late thank-you letter this week, copied to their manager.",
    remember="Endings are remembered. <span class=\"hl\">Close every promise</span>, thank people by name, and <span class=\"hl\">leave the floor as if you'll be back</span>.",
    late=dict(when="Mon 11 June 2029 · 21:30 · hotel near The Grid",
              lines=["Lottie's been offered a job on Kemi's team. She told me before anyone else. I'm proud of her, and I minded for about an hour.",
                     "Wrote nine of the 31 letters. Bert's took longest. It's two pages; it should be ten.",
                     "Four days to the decision. Three promises to close. One of them is binding Bert's book."]),
    sources=["David Maister, <i>Managing the Professional Service Firm</i> (1993): alumni and reputation.",
             "Adam Grant, <i>Give and Take</i> (2013).",
             "UK Information Commissioner's Office, guidance on retention and secure disposal."],
)

# ------------------------------------------------------------------ 14 What Did the Vendor Side Teach Me?
wt_problem = Doodle(760, 240, "Doodle of Ines's notebook on Wednesday 13 June 2029: about 470 late notes since February 2027, from 15 years in-house at Aldermoor Water to two and a half years on the client's floor. Yesterday, MetroVolt announced Ascend 2030. Whatever happens on Friday, she wants to write down what she learned before it blurs.",
                    "470 late notes, and the lessons before they blur.", exact=True)
wt_problem.box(14, 30, 360, 120, "in-house", "paper", sub="15 years at Aldermoor Water", size=24, subsize=14)
wt_problem.arrow(380, 90, 424, 90)
wt_problem.box(430, 30, 316, 120, "the vendor side", "blue", sub="2½ years on floor 19", size=24, subsize=14)
wt_problem.note(380, 200, "write it down while it's fresh", "red", size=19)

wt_how = Doodle(760, 360, "Ines's ten rules for her younger self. 1 Read the contract before the code. 2 Bad news early, in writing. 3 Price what you know; say what you don't. 4 Every promise goes in a register. 5 Find the person who really knows: there's always a Bert. 6 The client's politics are weather: read them, don't make them. 7 Never change the numbers. 8 Your pace is your team's ceiling. 9 Decide what you won't accept before you want the deal. 10 Leave the floor as if you'll be back.",
                "Ten rules: contract, bad news, pricing, promises, Bert, weather, numbers, pace, walk-away, leaving.", exact=True)
rules = ["read the contract first", "bad news early, in writing", "price what you know", "every promise in a register", "there's always a Bert",
         "politics are weather", "never change the numbers", "your pace is their ceiling", "decide the walk-away early", "leave as if you'll be back"]
for i, t in enumerate(rules):
    wt_how.box(14 + (i % 2) * 374, 14 + (i // 2) * 66, 358, 54, f"{i + 1}. {t}", "y" if i % 2 == 0 else "paper", size=16)

WHAT_IT_TAUGHT = dict(
    slug="what-it-taught", date=date(2029, 6, 13), meta=on_site(date(2029, 6, 13)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. lessons from the vendor side",
    tldr="Lessons blur fast once the next project starts. At the end of a long engagement, <b>write down what you learned while it's fresh</b>, as rules you'd give your younger self: short, specific, each tied to a moment you can remember. Then <b>share them</b> with someone starting out. This note is Ines's list: ten rules from two and a half years on the client's floor.",
    chips=[("Family", "endings"), ("Lives in", "the back page of this notebook"), ("Pairs with", "every note in this series")],
    problem_side="Floor 19, 13 June 2029",
    problem="""  <p class="lead">Ines spent fifteen years in-house at Aldermoor Water before joining Wrenfield. She has now spent two and a half years on the other side of the table: <b>about 470 late notes</b> since February 2027.</p>
  <ul>
    <li>Yesterday MetroVolt published its <b>Ascend 2030</b> memo: “30 % more output with 20 % fewer people”. The lifts have talked of nothing else.</li>
    <li>The phase 2 decision is due in two days.</li>
    <li>Lottie asks: <span class="hl-pink">“If you could tell yourself one thing in 2027, what would it be?”</span> Ines can't answer in one.</li>
  </ul>""",
    problem_figs=[wt_problem],
    sides=dict(client=("the in-house Ines", "<p>The architect Ines used to be thought suppliers were slow, expensive and always selling. She wrote tenders full of “absorb” and fixed prices, and thought change requests were a trick.</p>", "Why can't they just deliver what we asked for?"),
                vendor=("the vendor Ines", "<p>The architect Ines is now knows what's behind the price, the change request and the status colour. She also knows which suspicions were right: some suppliers do sell first and think later. Vivian did, once.</p>", "Both sides were right about each other. Some of the time.")),
    sides_after="Anyone who has worked both sides of the table makes a better client and a better supplier.",
    analogy_side="the travel journal",
    analogy="""  <p>Travellers who keep a journal remember the trip; the others remember the photos. The best entries are written <b>on the last evening</b>, before the flight home: not what you saw, but what you'd tell a friend going next year. Pack light. Learn ten words. The cheap hotel near the station isn't worth it. That page is the one that gets photocopied.</p>""",
    map=[("The last evening", "This note, two days before the decision"),
         ("What you'd tell a friend", "Rules for her younger self"),
         ("The cheap hotel near the station", "Pricing below the floor"),
         ("Learn ten words", "Read the contract first"),
         ("The photocopied page", "The list Lottie takes to MetroVolt, or stays with")],
    how_side="ten rules, each from a moment",
    how="""  <ol>
    <li><b>Read the contract before the code.</b> (Vol. 2: the SOW clauses that later decided every argument.)</li>
    <li><b>Bad news early, in writing.</b> (Vol. 3: the 7.8 % data surprise; Elaine's quote.)</li>
    <li><b>Price what you know; say what you don't.</b> (Vol. 1: the assumptions page; vol. 6: £9.4m.)</li>
    <li><b>Every promise goes in a register.</b> (Vol. 1: Vivian's dinner; 47 of 47.)</li>
    <li><b>Find the person who really knows. There's always a Bert.</b> (Vol. 3: 64 pages of Bert's book.)</li>
    <li><b>The client's politics are weather: read them, don't make them.</b> (Vol. 5: Priya, Rupert, the lift.)</li>
    <li><b>Never change the numbers.</b> (Vol. 5: £210k, not £1.9m.)</li>
    <li><b>Your pace is your team's ceiling.</b> (Vol. 6: Hana, and the 23:30 notes.)</li>
    <li><b>Decide what you won't accept before you want the deal.</b> (Vol. 6: “absorb”, twice.)</li>
    <li><b>Leave the floor as if you'll be back.</b> (Vol. 6: 31 letters.)</li>
  </ol>
  <p>She gives Lottie a copy and tapes another inside the notebook's back cover. Lottie's question gets an answer after all: “Number eight. I learned it last.”</p>""",
    how_figs=[wt_how],
    steps=[("Write it at the end, while it's fresh", "Before the next project."),
           ("Make each lesson a rule", "Short enough to remember."),
           ("Tie each rule to a moment", "So it's believable."),
           ("Keep it to about ten", "Nobody reads fifty."),
           ("Share it with someone starting out", "That's where it's useful."),
           ("Reread it at the next start", "And add one.")],
    vocab=[("Reflective practice", "Deliberately reviewing your own work to learn from it."),
           ("Tacit knowledge", "Know-how that's hard to write down."),
           ("Personal retrospective", "A retrospective on your own work and habits."),
           ("Mentoring", "Passing experience to someone earlier in their career."),
           ("Both sides of the table", "Having worked as client and as supplier."),
           ("Rule of thumb", "A short, practical guide from experience.")],
    code=dict(file="notebook/back-cover.md", note="Wed 13 Jun 2029 · a copy for Lottie", src="""
TEN RULES FOR 2027-ME (from 2½ years on floor 19)

 1  read the contract before the code
 2  bad news early, in writing
 3  price what you know; say what you don't
 4  every promise goes in a register
 5  find the person who really knows (there's always a Bert)
 6  the client's politics are weather: read them, don't make them
 7  never change the numbers
 8  your pace is your team's ceiling          ← learned last
 9  decide what you won't accept before you want the deal
10  leave the floor as if you'll be back
"""),
    contract=dict(side="the clause I'd write if I were the client again", doc="Ines's ideal SOW · §1 (a wish)", date="13 Jun 2029", stamp="not in any contract",
                  clauses=[("1.1", "<s>The Supplier shall absorb all risks …</s> <i>The Parties shall share known risks openly, price them honestly, and tell each other bad news early.</i>", "no lawyer would sign it. both teams would work better under it."),
                           ("1.2", "Each Party shall treat the other's people as it would wish its own to be treated.", "Elaine did this without a clause.")],
                  plain="the best contracts don't create trust; they make it cheaper to keep. The rest is people."),
    health=dict(now="g",
                g=("lessons written down", ["Ten rules.", "Shared.", "Reread at the next start."]),
                a=("lessons in your head", ["Write them tonight.", "One moment each.", "Share one."]),
                r=("straight into the next project", ["Take an hour first.", "Ten lines.", "Then go."])),
    pressure=dict(level=1, title="reflection", cost="one evening · some honesty about rule 8",
                  items=["The hardest rule to write is the one you learned last. Write it first."]),
    baseline="Each line compares <b>moving straight on to the next project</b> with <b>ten written rules, each from a moment, shared with someone starting out</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 4, "Lottie and the team keep the list."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Lessons survive the project."),
             (3, 4, "The next engagement starts wiser."),
             (3, 3, "Neutral."),
             (3, 3, "An evening."),
             (3, 4, "One page.")],
    pitfalls=[("Not writing it down", "It blurs in a month.", "tonight."),
              ("Fifty lessons", "None remembered.", "ten."),
              ("Abstract lessons", "Nobody believes them.", "tie each to a moment."),
              ("Keeping it to yourself", "Wasted.", "share it."),
              ("Leaving out the uncomfortable one", "It's the useful one.", "write it first.")],
    grimoire=[(8, "quiet-thriving", "Quiet Thriving", "is the inside version: what's left when you've learned the dark arts and chosen not to use most of them.")],
    use=["At the end of any long engagement.", "When someone asks what you'd do differently.", "Before starting something similar."],
    skip=["Never skip it."],
    related=["<b>How Do We Leave Well?</b> (previous note)", "<b>What About My Own 23:00 Notes?</b> (this volume)", "<b>What If the Client Asks Us to Change the Numbers?</b> (vol. 5)", "<b>Growing Other Architects</b> (Ana, vol. 6)"],
    quiz=[("Where did Ines work before Wrenfield?", "Fifteen years in-house at Aldermoor Water."),
          ("What was announced the day before?", "MetroVolt's Ascend 2030 memo."),
          ("Which rule did she learn last?", "Number eight: your pace is your team's ceiling."),
          ("Why tie each rule to a moment?", "So it's believable and remembered."),
          ("What did she do with the list?", "Gave Lottie a copy and taped one inside the notebook's back cover.")],
    quiz_sit=[("A new graduate joining Wrenfield asks Ines for “the one thing”. What does she say?", "Rule 2: bad news early, in writing. Then give them the other nine.")],
    try_it="Write your own ten rules from your last long project, each tied to a moment. Which did you learn last? Give the list to someone starting out.",
    remember="Write it down <span class=\"hl\">while it's fresh</span>, ten rules, each from a moment, and <span class=\"hl\">give it away</span>.",
    late=dict(when="Wed 13 June 2029 · 21:40 · hotel near The Grid",
              lines=["Ten rules. Lottie has a copy. She read number eight twice and looked at me.",
                     "Ascend 2030: “30 % more output with 20 % fewer people”. Kemi asked if her team is safe. I said I don't know, and it isn't ours to guess. Rule 6.",
                     "Two days. The last hotel night but one."]),
    sources=["Donald Schön, <i>The Reflective Practitioner</i> (1983).",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "Gerald Weinberg, <i>The Secrets of Consulting</i> (1985)."],
)

# ------------------------------------------------------------------ 15 The Last Day on Floor 19
ld_problem = Doodle(760, 240, "Doodle of Friday 15 June 2029 on floor 19. The phase 2 decision is due today. Nothing has come through the portal by four o'clock. Room 19C is empty except for one box. The visitor pass, number V-0417, renewed 26 times, has to be handed back to reception on the ground floor.",
                    "Decision due today. Nothing by 16:00. One box, and pass V-0417 to hand back.", exact=True)
ld_problem.box(14, 20, 360, 120, "16:00", "y", sub="portal: nothing yet", size=34, subsize=15)
ld_problem.box(386, 20, 360, 120, "V-0417", "paper", sub="renewed 26 times", size=30, subsize=15)
ld_problem.note(380, 190, "room 19C: one box, a kettle, a pot plant", "pen", size=18)

ld_how = Doodle(760, 340, "The last afternoon. Return what you borrowed: the kettle to Yusuf, Bert's book to Bert, the pot plant to Rosa. Say goodbye properly, desk by desk: Kemi, Marta, Asif, Rosa, Kofi, Bert. Leave something useful: the handbook link on the 19C door. Hand back the badge. Then a call from Elaine at 17:05: “Before you go. A quick word, in room 27A?”",
                "Return what you borrowed, say goodbye properly, hand back the badge, and go to the room.", exact=True)
for i, (h, sub, fill) in enumerate([("return", "kettle · book · plant", "paper"), ("goodbye", "desk by desk", "y"), ("leave", "the handbook link", "green"), ("badge", "V-0417", "blue")]):
    ld_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=13)
ld_how.box(14, 160, 732, 80, "17:05 · Elaine: “Before you go. A quick word, in room 27A?”", "pink", size=19)
ld_how.note(380, 300, "and the door of room 27A, still closed", "red", size=19)

LAST_DAY = dict(
    slug="last-day", date=date(2029, 6, 15), meta=on_site(date(2029, 6, 15)), where="RM 27A", pass_kind="contractor", pass_no=417,
    kicker="a.k.a. the last day on the client's floor",
    tldr="The last day is short and matters more than it should. <b>Return what you borrowed</b>, <b>say goodbye properly</b>, desk by desk, <b>leave something useful</b> behind, and <b>hand back the badge</b> yourself. You won't control what happens next. Walk into whatever room you're asked to, <b>calmly, with your notebook</b>, ready for either answer.",
    chips=[("Family", "endings"), ("Lives in", "room 19C (empty) · visitor pass V-0417 · room 27A"), ("Pairs with", "leaving well, waiting for the decision")],
    problem_side="Floor 19, Friday 15 June 2029",
    problem="""  <p class="lead">It is <b>Friday 15 June 2029</b>, Ines's last day on site. The phase 2 decision is due today.</p>
  <ul>
    <li>By <b>16:00</b> the tender portal shows nothing. Callum has refreshed it eleven times from Leeds.</li>
    <li>Room 19C, the goldfish bowl, is empty except for one box, a kettle and a pot plant.</li>
    <li>Her visitor pass, <b>V-0417</b>, has been renewed <b>26 times</b>. It goes back to reception tonight.</li>
    <li>Nobody on floor 19 knows the decision. <span class="hl-pink">Or, if they do, nobody's saying.</span></li>
  </ul>""",
    problem_figs=[ld_problem],
    sides=dict(client=("MetroVolt", "<p>Floor 19 is half empty for the summer and full of Ascend rumours. Kemi's team is running Lodestar on its own. Elaine has been in meetings on floor 27 since lunch. Rupert's door has been closed all day.</p>", "(Nobody says anything.)"),
                vendor=("Ines", "<p>Ines has done everything the notes in this book say to do: the promises closed, the paper tidy, the letters sent, both plans written, the walk-away letter signed. What happens next isn't hers to decide. She notices she's calm, and is surprised by it.</p>", "Whatever it is, we did it properly.")),
    sides_after="At the end of a long engagement, the work you control is finished. What's left is how you walk out, and into what.",
    analogy_side="the last day of term",
    analogy="""  <p>On the last day of term, the classroom walls are bare and the desks are empty. Teachers hand back the last books, say goodbye to each child, and give the room one more look. Results come later, in an envelope. Nobody can change them now. <b>The last day is for leaving well</b>, and for being ready to open the envelope, whatever's in it.</p>""",
    map=[("Bare walls, empty desks", "Room 19C, one box"),
         ("Handing back the last books", "Bert's book, the kettle, the plant"),
         ("Goodbye to each child", "Desk by desk"),
         ("The envelope", "Room 27A"),
         ("Whatever's in it", "The phase 2 decision (not in this book)")],
    how_side="return, goodbye, leave something, the badge, the room",
    how="""  <p><b>Return what you borrowed.</b> The kettle goes back to Yusuf, who lent it on day 2 and pretends to have forgotten. Bert's book, bound, goes back to Bert, who turns the pages slowly and says, “Somebody will finally read it.” The pot plant goes to Rosa.</p>
  <p><b>Say goodbye properly.</b> Desk by desk, not an email. Kemi, Marta and Asif. Rosa. Kofi on floor 20. Hollis by the lifts, who shakes her hand and says “the template's working”. Lottie walks with her to the stairs and says she'll decide on Monday.</p>
  <p><b>Leave something useful.</b> A card on the door of 19C: the handbook link, the runbooks, the run team's phone number, and “ask Kemi”.</p>
  <p><b>The badge.</b> At <b>17:00</b> Ines is at the lift with her box and pass V-0417 in her hand, on the way to reception.</p>
  <p>At <b>17:05</b> her phone goes. Elaine.</p>
  <p><i>“Ines. Before you go. Have you got a minute? A quick word, in room 27A.”</i></p>
  <p>Elaine doesn't say what about. Her voice gives nothing away. Room 27A is on floor 27, where Rupert's office is, and where Desmond has been all afternoon.</p>
  <p>Ines puts the box down by the lift, keeps the pass, picks up the notebook, and presses 27.</p>""",
    how_figs=[ld_how],
    steps=[("Return what you borrowed", "Personally."),
           ("Say goodbye desk by desk", "Not by email."),
           ("Leave something useful", "A link, a name, a number."),
           ("Hand back the badge yourself", "When you're ready."),
           ("Go to the room you're asked to", "Calmly."),
           ("Take the notebook", "Either way, you'll want to write it down.")],
    vocab=[("Last day", "The final day on a client's site."),
           ("Offboarding", "Removing a person's access and returning equipment at the end."),
           ("Award notification", "The formal message telling bidders the procurement result."),
           ("Debrief", "A meeting explaining a decision, often to an unsuccessful bidder."),
           ("Standstill", "The pause after an award, before the contract is signed."),
           ("Open ending", "A story that stops before its final question is answered.")],
    code=dict(file="notebook/last-page.md", note="Fri 15 Jun 2029 · 17:06 · the lift, floor 19", src="""
LAST DAY · floor 19 · Fri 15 Jun 2029

returned    kettle → Yusuf · Bert's book (bound) → Bert · pot plant → Rosa
goodbyes    Kemi · Marta · Asif · Rosa · Kofi · Hollis · Lottie (decides Monday)
left        card on 19C door: handbook · runbooks · run team · "ask Kemi"
badge       V-0417 · renewed 26× · not yet returned
portal      16:00 nothing · 17:00 nothing
17:05       Elaine: "A quick word, in room 27A."
17:06       lift → 27
"""),
    contract=dict(side="the last clause that matters today", doc="Phase 2 invitation to tender · §8 (award)", date="issued 5 Mar 2029", stamp="pending",
                  clauses=[("8.1", "MetroVolt intends to notify all bidders of its decision by 15 June 2029.", "“intends”. it's 17:05."),
                           ("8.3", "Unsuccessful bidders will be offered a debrief.", "a debrief, or something else. Elaine didn't say.")],
                  plain="award notices come in writing, through the portal, to every bidder at once. A phone call first means something. It doesn't say what."),
    health=dict(now="a",
                g=("(not known yet)", ["—"]),
                a=("(not known yet)", ["—"]),
                r=("(not known yet)", ["—"])),
    pressure=dict(level=4, title="the door", cost="£9m · two and a half years · one corridor on floor 27",
                  items=["Everything Ines can control is done.", "The rest is behind a door."]),
    baseline="Each line compares <b>slipping out at lunchtime</b> with <b>returning everything, goodbyes desk by desk, something left behind, and walking into the room</b>.",
    ratings=[(3, 4, "Remembered as a supplier who left properly."),
             (3, 4, "The team's work handed on with care."),
             (3, 3, "(not known yet)"),
             (3, 3, "(not known yet)"),
             (3, 4, "The handbook link on the door."),
             (3, 3, "(not known yet)"),
             (3, 4, "Pass still in hand."),
             (3, 3, "An afternoon."),
             (3, 3, "One box.")],
    pitfalls=[("Slipping away early", "Nobody gets to say goodbye.", "desk by desk."),
              ("Keeping what you borrowed", "A small thing, remembered.", "return it, personally."),
              ("Leaving nothing behind", "The next question has nowhere to go.", "a card on the door."),
              ("Guessing what the call means", "It changes nothing.", "go and find out."),
              ("Going in without the notebook", "You'll want to write it down.", "take it.")],
    grimoire=[(4, "calibration-council", "The Calibration Council", "happened in this same room, room 27A, in December 2027, with Priya and Pip on the other side of a different door.")],
    use=["Every last day."],
    skip=["Never."],
    related=["<b>How Do We Leave Well?</b> (this volume)", "<b>How Do We Wait for the Decision?</b> (this volume)", "<b>What Did the Vendor Side Teach Me?</b> (this volume)", "<b>How Do We Read the Client's Politics from Outside?</b> (vol. 5)"],
    quiz=[("What was due on Friday 15 June 2029?", "The phase 2 decision."),
          ("What did Ines return, and to whom?", "The kettle to Yusuf, Bert's book to Bert, the pot plant to Rosa."),
          ("What did she leave on the door of 19C?", "A card with the handbook link, the runbooks, the run team's number and “ask Kemi”."),
          ("How many times was pass V-0417 renewed?", "26."),
          ("What did Elaine ask at 17:05?", "“A quick word, in room 27A.”")],
    quiz_sit=[("You're in the lift to floor 27. What do you expect?", "Nothing in particular. Either answer is possible, and both plans are written. Walk in calmly, listen, and write it down afterwards.")],
    try_it="On your next last day anywhere, return one borrowed thing personally, say goodbye to three people at their desks, and leave a card on the door with where to find what you made.",
    remember="Return what you borrowed, <span class=\"hl\">say goodbye properly</span>, and walk into <span class=\"hl\">whatever room you're asked to</span>.",
    late=dict(when="Fri 15 June 2029 · 17:09 · outside room 27A",
              lines=["Floor 27. The corridor is quiet. Rupert's door is closed. Desmond's coat is on the chair outside.",
                     "Through the glass of 27A: Elaine, standing. Someone else, sitting, with their back to the door. A folder on the table, closed.",
                     "I've still got the pass. I've got the notebook. I'm knocking."]),
    sources=["Ines Duarte, this notebook (February 2027 – June 2029).",
             "William Bridges, <i>Managing Transitions</i> (4th ed., 2017): endings first.",
             "The Lodestar casebook (every date and number in this book)."],
)

NOTES = [LEAVING_WELL, WHAT_IT_TAUGHT, LAST_DAY]
