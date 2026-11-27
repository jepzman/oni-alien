# Series 5 · On the Client's Floor · Vol. 2 · Signing and Starting · Two firms, one team (notes 11–15).
from datetime import date

# ------------------------------------------------------------------ 11 Who Does What When Three Firms Share a Project?
rc_problem = Doodle(760, 250, "Doodle of the 02:10 file between MAVIS and Halvorsen billing. Three firms touch it: MetroVolt IT runs the batch scheduler, Halvorsen ingests the file, and Wrenfield will build a new extract for migrated customers. When the file fails at 02:10, each of the three thinks someone else owns it. Question marks over each.",
                    "One file at 02:10, three firms, and three people who each think it's someone else's.", exact=True)
rc_problem.box(24, 60, 180, 100, "MAVIS", "paper", sub="MetroVolt IT", size=22, subsize=16)
rc_problem.arrow(208, 110, 300, 110)
rc_problem.box(304, 60, 150, 100, "02:10 file", "y", size=20)
rc_problem.arrow(458, 110, 550, 110)
rc_problem.box(554, 60, 180, 100, "billing", "paper", sub="Halvorsen", size=22, subsize=16)
rc_problem.box(304, 180, 150, 50, "new extract", "blue", sub="Wrenfield", size=17, subsize=14)
for x in (114, 379, 644):
    rc_problem.note(x, 40, "not mine?", "red", size=18)

rc_how = Doodle(760, 340, "The responsibility chart for the 02:10 interface, written together on 21 July. Rows: file format, the extract for migrated customers, the batch schedule, ingestion into billing, monitoring at night, and a failed file at 02:10. Columns: Wrenfield, MetroVolt IT, Halvorsen. For each row exactly one A, accountable. A failed file: MetroVolt IT's on-call is accountable for the first response, and runs joint triage with the others by evidence within four hours.",
                "Every row has exactly one A. A failed file has an owner at 02:15, not at the steering.", exact=True)
cols = ["Wrenfield", "MV IT", "Halvorsen"]
rows = [("file format", ["C", "C", "A"]), ("new extract", ["A", "C", "C"]), ("batch schedule", ["I", "A", "I"]),
        ("ingest into billing", ["I", "I", "A"]), ("night monitoring", ["I", "A", "R"]), ("failed file, 02:10", ["R", "A", "R"])]
fills = {"A": "pink", "R": "y", "C": "blue", "I": "paper"}
rc_how.box(14, 14, 250, 36, "interface 02:10", "paper", size=17, rx=4)
for c, name in enumerate(cols):
    rc_how.box(274 + c * 158, 14, 150, 36, name, "paper", size=17, rx=4)
for r, (name, cells) in enumerate(rows):
    y = 58 + r * 40
    rc_how.box(14, y, 250, 34, name, "paper", size=16, rx=4)
    for c, v in enumerate(cells):
        rc_how.box(274 + c * 158, y, 150, 34, v, fills[v], size=18, rx=4)
rc_how.note(380, 318, "A accountable · R responsible · C consulted · I informed", "pen", size=18)

RACI = dict(
    slug="multi-vendor-raci", date=date(2027, 7, 21), meta="day 17 on site", where="FL 19",
    kicker="a.k.a. “RACI for multi-supplier interfaces”",
    tldr="When several firms share a system, failures fall into the gaps between them. For every <b>shared interface</b>, write a <b>responsibility chart</b> with <b>all the firms in the room</b>: what has to happen, and for each row exactly <b>one accountable owner</b>. Include the unhappy rows (“the file fails at 02:10”), agree <b>joint triage by evidence</b>, and get the client to sign it, because only the client has a contract with everyone.",
    chips=[("Family", "two firms, one team"), ("Lives in", "delivery/lodestar/IA-01-raci.md (interface agreement IA-01)"), ("Pairs with", "the incumbent, governance")],
    problem_side="The Grid, 21 July 2027",
    problem="""  <p class="lead">Every night at <b>02:10</b>, MAVIS sends a file to Halvorsen billing. Once wave 1 starts, migrated customers will come from <b>Wrenfield's new extract</b> instead. Three firms will touch one file: <b>MetroVolt IT</b> runs the batch scheduler, <b>Halvorsen</b> ingests the file, <b>Wrenfield</b> builds the new extract.</p>
  <ul>
    <li>Bert tells Ines that in 2024 the file failed three nights running. <span class="hl-pink">Each team spent the mornings proving it wasn't theirs.</span> Customers got wrong bills for a month.</li>
    <li>Sven's one request at the café in March: don't blame Halvorsen for MAVIS's data.</li>
    <li>The contract says who Wrenfield works for. It says nothing about who answers the phone at 02:15.</li>
  </ul>""",
    problem_figs=[rc_problem],
    sides=dict(client=("Hollis and MetroVolt IT", "<p>MetroVolt has <b>contracts with each firm</b>, and no contract between them. When something fails between suppliers, MetroVolt is the only party who can make them work together, and it's tired of refereeing blame.</p>", "I don't care whose fault it is. I care who picks up the phone."),
                vendor=("Ines, with Sven", "<p>Wrenfield is new and the obvious suspect for any failure near its code. It needs a written, shared answer to “who owns what” <b>before</b> the first failure, signed by MetroVolt so it binds Halvorsen too.</p>", "Write the 02:10 night down now, while we're all friends.")),
    sides_after="A blame war is just a responsibility chart written after the failure, by angry people.",
    analogy_side="a relay race handover",
    analogy="""  <p>In a relay, races are lost at the <b>handover</b>, not on the straights. Teams practise the exchange zone: who reaches, who grabs, what the signal is, and what happens if the baton drops. <b>Everyone knows who picks it up.</b> Nobody stands over a dropped baton arguing about whose hand it fell from.</p>""",
    map=[("The exchange zone", "The 02:10 file between MAVIS and billing"),
         ("Who reaches, who grabs", "R and A on each row"),
         ("The signal", "The file format and checks, owned by Halvorsen"),
         ("Who picks up a dropped baton", "MetroVolt IT on-call, at 02:15"),
         ("Practising the handover", "Interface testing, joint, before wave 1")],
    how_side="one chart, all firms in the room, one A per row",
    how="""  <p>On <b>Wednesday 21 July</b>, Ines runs a two-hour workshop with <b>Sven</b> and a Halvorsen engineer, <b>Hollis's integration lead</b> and the MetroVolt IT on-call manager, and Hana. One whiteboard, one question per row: <i>what has to happen, and who is accountable?</i></p>
  <p>They list the happy rows (file format, the new extract, the schedule, ingestion) and then the <b>unhappy rows</b>: the file is late, the file is malformed, the totals don't match. Each row gets <b>exactly one A</b>. Arguing about which firm gets the A is the useful part: it takes forty minutes for “a failed file at 02:10”. The answer: <b>MetroVolt IT on-call is accountable</b> for the first response (it runs the scheduler and is awake), and starts a <b>joint triage</b> with the others, by evidence, within four hours.</p>
  <p>Sven gets what he asked for in March: interface defects are assigned <b>after</b> evidence, not before. The chart becomes <b>interface agreement IA-01</b>, signed by all three firms and by Hollis for MetroVolt on <b>11 August</b>, and logged as DL-005.</p>""",
    how_figs=[rc_how],
    steps=[("List every shared interface", "Files, APIs, schedules, data handovers."),
           ("Get every firm in the room", "Engineers, not just account managers."),
           ("Write the happy rows, then the unhappy ones", "Late, malformed, mismatched, silent."),
           ("Exactly one A per row", "Argue until there is one."),
           ("Agree joint triage by evidence", "Who starts it, how fast, what evidence."),
           ("Get the client to sign it", "Only the client has a contract with everyone.")],
    vocab=[("RACI", "Responsible, accountable, consulted, informed: who does what for each task."),
           ("Accountable", "The one person or team who answers for a task being done."),
           ("Interface agreement", "A written agreement on how two systems and their owners connect."),
           ("Joint triage", "Investigating a cross-supplier problem together, by evidence."),
           ("Service integration", "Coordinating several suppliers as one service (often called SIAM)."),
           ("Hand-off", "The moment work or data passes from one owner to another.")],
    code=dict(file="delivery/lodestar/IA-01-raci.md", note="workshop Wed 21 Jul · signed Wed 11 Aug 2027", src="""
INTERFACE AGREEMENT IA-01 · the 02:10 customer file

row                                   Wrenfield  MetroVolt IT  Halvorsen
file format and checks (totals)       C          C             A
new extract (migrated customers)      A          C             C
batch schedule and dependencies       I          A             I
ingest into billing                   I          I             A
night monitoring and first alert      I          A             R
file late / malformed / totals wrong  R          A (on-call)   R
  → joint triage within 4 hours, by evidence (logs, totals, file sample)
  → defect assigned after evidence, not before
change to the file format             R          C             A (30 days' notice)

signed: Sven Aldous (Halvorsen) · Hollis Wade (MetroVolt) · Ines Duarte (Wrenfield)
decision log: DL-005, 11 Aug 2027
"""),
    contract=dict(side="how a third party's role becomes binding", doc="Lodestar SOW · §3.6 and IA-01", date="11 Aug 2027", stamp="countersigned",
                  clauses=[("3.6", "Where a Dependency is to be provided by a third-party supplier of MetroVolt, MetroVolt shall use reasonable endeavours to procure its provision.", "MetroVolt signing IA-01 is how it “procures” Halvorsen's part."),
                           ("IA-01, 4", "Defects at the interface are assigned to a party only after joint triage on the evidence listed in section 3.", "Sven's sentence. it protects us just as much.")],
                  plain="you can't contract with the other vendor, but the client can. A responsibility chart the client countersigns turns a friendly workshop into something every firm can be held to."),
    health=dict(now="g",
                g=("the vendors get on", ["Write it anyway, while they do.", "Include the unhappy rows.", "Client countersigns."]),
                a=("old blame between suppliers", ["Start from a past failure everyone remembers.", "Evidence before blame, in writing.", "One A per row, however long it takes."]),
                r=("vendors refuse to cooperate", ["Ask the client to require it.", "Write your own side and send it.", "Log every refusal."])),
    pressure=dict(level=2, title="three firms, one whiteboard", cost="forty minutes on one row",
                  items=["The argument about the A is uncomfortable and essential. Let it run.", "Thank Halvorsen publicly for coming. They didn't have to."]),
    baseline="Each line compares <b>sorting it out when it fails</b> with <b>a signed responsibility chart for each shared interface, unhappy rows included</b>.",
    ratings=[(3, 4, "Hollis stops refereeing."),
             (2, 4, "Nobody on Wrenfield's team is blamed by default."),
             (3, 4, "Interface defects are assigned by evidence."),
             (2, 5, "Every row has one owner."),
             (3, 4, "The format has an owner and a change notice."),
             (2, 4, "The 02:10 failure is planned for."),
             (2, 5, "Signed by all three firms and MetroVolt."),
             (3, 3, "Two hours and three weeks to sign."),
             (4, 4, "One page per interface.")],
    pitfalls=[("Happy rows only", "The chart is silent when it matters.", "write the failure rows."),
              ("Two As", "Shared accountability means none.", "argue until there's one."),
              ("Account managers only", "The people at 02:15 weren't asked.", "engineers and on-call in the room."),
              ("Blame before evidence", "Each firm defends itself.", "joint triage by agreed evidence."),
              ("Not signed by the client", "Nothing binds the other vendor.", "the client countersigns.")],
    grimoire=[(6, "frenemy-pact", "The Frenemy Pact", "shows the same deal from MetroVolt's GridSight side, with Northgate.")],
    use=["Several suppliers share a system or interface.", "An incumbent and a newcomer meet at a boundary.", "Past failures were spent assigning blame."],
    skip=["A single supplier owns everything end to end."],
    related=["<b>What About the Vendor Already Here?</b> (vol. 1)", "<b>Who Decides What, and Where?</b> (this volume)", "<b>How Do Two Companies Work as One Team?</b> (this volume)", "<b>The Vendor Went Quiet</b> (Eli, vol. 4)"],
    quiz=[("Why does each row need exactly one A?", "Shared accountability means nobody answers when it fails."),
          ("What are “unhappy rows”?", "The failure cases: late, malformed or mismatched files, silence."),
          ("Who is accountable for a failed file at 02:10, and why?", "MetroVolt IT on-call: it runs the scheduler and is awake; it starts joint triage."),
          ("What did Sven get from IA-01?", "Defects assigned after evidence, not before."),
          ("Why must MetroVolt sign?", "Only MetroVolt has a contract with every firm.")],
    quiz_sit=[("Two months later, Halvorsen changes the file format with a week's notice. What do you do?", "Point to IA-01: format changes need 30 days' notice. Raise it with Hollis, log it, and assess the impact; don't absorb it quietly or argue directly with Sven first.")],
    try_it="Pick one interface between your team and another team or firm. Write the rows, happy and unhappy, and put one A on each. Who would you need in the room to agree it?",
    remember="Blame wars happen in the gaps. For every shared interface, <span class=\"hl\">one A per row</span>, <span class=\"hl\">unhappy rows included</span>, signed by the client.",
    late=dict(when="Wed 21 July 2027 · 21:40 · hotel near The Grid",
              lines=["Forty minutes on one row: who picks up the phone at 02:15. MetroVolt IT, in the end. They're awake.",
                     "Sven brought biscuits again. The on-call manager ate four.",
                     "Bert told the 2024 story at the start. Nobody wanted to be in that story again. That did most of the work."]),
    sources=["AXELOS, <i>ITIL 4</i>: service integration and supplier management.",
             "Kevin Holland, <i>An Introduction to Service Integration and Management (SIAM)</i> (2015).",
             "Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003)."],
)

# ------------------------------------------------------------------ 12 How Do We Earn the Programme Director's Trust?
ct_problem = Doodle(760, 240, "Doodle of Elaine Corbett on the left with a thick folder labelled Orion: three years, four leads, four assumptions she paid for. On the right, Ines with an empty folder labelled Lodestar. Between them, a gap labelled trust, with a small bridge being built out of planks: Thursday 8 a.m., no surprises, small promises kept.",
                    "Elaine has three years of Orion in her folder. Ines has six weeks.", exact=True)
ct_problem.box(24, 40, 240, 150, "Orion", "pink", sub="3 years · 4 leads", size=24, subsize=16)
ct_problem.box(496, 40, 240, 150, "Lodestar", "blue", sub="6 weeks", size=24, subsize=16)
for i, t in enumerate(["Thu 08:00", "no surprises", "small promises"]):
    ct_problem.box(290 + i * 62, 110 - i * 0, 56, 30, None, "y", rx=3)
ct_problem.note(380, 90, "trust", "red", size=22)
ct_problem.note(380, 220, "a bridge, one plank at a time", "pen", size=19)

ct_how = Doodle(760, 320, "Four habits with Elaine. One: a weekly hour, Thursday 8 a.m., café on floor 2, her agenda first. Two: the no surprises pact agreed on 15 July: anything she'd want to know, she hears from Ines before anyone else. Three: bad news early and small, with a proposed fix. Four: small promises kept and visible: the access tracker updated every morning at 9. The test: on 12 August Ines tells Elaine that Bert is only assigned one day a week, not three, before it reaches the steering. Elaine fixes it herself.",
                "A weekly hour, no surprises, bad news early, small promises kept.", exact=True)
for i, (h, sub, fill) in enumerate([("weekly hour", "Thu 08:00 · her agenda first", "y"), ("no surprises", "pact, 15 July", "blue"),
                                    ("bad news early", "small, with a fix", "pink"), ("small promises", "tracker at 09:00, daily", "green")]):
    ct_how.box(14 + (i % 2) * 372, 14 + (i // 2) * 100, 360, 86, h, fill, sub=sub, size=20, subsize=16)
ct_how.box(14, 220, 732, 70, "the test, 12 Aug: D-09 · Bert 1 day a week, not 3", "paper", sub="Elaine hears it from Ines first, and fixes it herself", size=18, subsize=15)

COUNTERPART = dict(
    slug="client-counterpart", date=date(2027, 8, 19), meta="day 46 on site", where="FL 2", pass_kind="contractor",
    kicker="a.k.a. “managing the client relationship”, one person at a time",
    tldr="Your most important relationship on a client project is with the client's <b>programme director</b>, and if they've been burned before, they'll start by expecting the worst. Trust is built in <b>small, repeated proofs</b>: a <b>weekly hour</b> on their agenda, a <b>no-surprises pact</b>, <b>bad news early and small, with a fix</b>, and <b>small promises kept where they can see them</b>. You can't speed it up; you can only start it on day one.",
    chips=[("Family", "two firms, one team"), ("Lives in", "Thursdays, 08:00, the café on floor 2"), ("Pairs with", "mapping the client, the first status report")],
    problem_side="The Grid, July and August 2027",
    problem="""  <p class="lead">Elaine Corbett was <b>Orion's last programme manager</b>. She watched four project leads come and go, signed off change requests for four assumptions, and spent forty minutes of her first hour with Ines on day one talking about it.</p>
  <ul>
    <li>She reads every Wrenfield email twice, looking for the exit Wrenfield is building.</li>
    <li>She copies Priya on everything, “just so it's on record”.</li>
    <li>On <b>12 August</b> Ines learns that MetroVolt has assigned Bert to Lodestar <b>one day a week</b>, not the three in dependency <b>D-09</b>. <span class="hl-pink">It's exactly the kind of thing Orion's supplier would have saved for a steering committee.</span></li>
  </ul>""",
    problem_figs=[ct_problem],
    sides=dict(client=("Elaine", "<p>For Elaine, every supplier is guilty until proven otherwise. She's not hostile; she's <b>careful</b>, because the last time she trusted a supplier's reports, she had to explain three years to the board. She'll trust what she sees repeatedly, not what she's told.</p>", "Show me, every week, for months."),
                vendor=("Ines", "<p>Ines needs Elaine as a partner: someone who'll fix MetroVolt's side of problems, defend the plan in Horizon meetings and tell Ines what's coming. She can't ask for trust. She can only <b>earn it in small amounts, often</b>.</p>", "Trust is a habit, not a speech.")),
    sides_after="A wary counterpart isn't an obstacle. They're the person whose trust, once earned, protects the project more than any clause.",
    analogy_side="the new dog walker",
    analogy="""  <p>A family hires a new dog walker after the last one lost the dog. They don't trust her on day one, and they're right not to. She texts a photo <b>after every walk</b>, says straight away when the dog cut its paw, and is there <b>at 8:00 exactly</b>, every day. After two months they give her a key. She never asked for it.</p>""",
    map=[("The last walker lost the dog", "Orion"),
         ("A photo after every walk", "The access tracker at 09:00, the Friday note"),
         ("“The dog cut its paw”", "Bad news early: D-09, Bert's days"),
         ("There at 8:00 exactly", "Thursday 08:00, every week"),
         ("The key, unasked", "Elaine fixing MetroVolt's side herself")],
    how_side="four habits, repeated",
    how="""  <p><b>A weekly hour, her agenda first.</b> From 15 July: Thursdays, 08:00, the café on floor 2. Elaine talks first. Ines brings one page: what happened, what's coming, what she needs. Ines has never cancelled one.</p>
  <p><b>A no-surprises pact.</b> At the second Thursday they agree: anything Elaine would want to know, she hears from Ines before she hears it anywhere else, including from Wrenfield's own reports. Elaine adds her side: she'll tell Ines about Horizon decisions before they're announced, when she can.</p>
  <p><b>Bad news early, small, with a fix.</b> On <b>Thursday 12 August</b>, Ines tells Elaine about D-09 over coffee: Bert is assigned one day a week; the plan assumes three; the data workstream will slip about two weeks by October unless it changes; here's a proposal (Bert three days through November, Lottie as his apprentice so the load falls later). No notice, no email to Priya.</p>
  <p><b>Small promises, kept where she can see them.</b> The access tracker, updated at 09:00, every day, for six weeks. It's trivial, and Elaine checks it every morning.</p>
  <p>The test comes a week later: on <b>19 August</b> Elaine tells Ines she has <b>moved Bert to three days</b> herself, by talking to his manager. She didn't copy Priya.</p>""",
    how_figs=[ct_how],
    steps=[("Book a weekly hour, and keep it", "Their agenda first."),
           ("Agree a no-surprises pact", "Both ways, out loud."),
           ("Tell bad news early, small, with a fix", "In person before in writing."),
           ("Keep small promises visibly", "Daily, boringly, without fail."),
           ("Let them fix their side", "Give them the chance before escalating."),
           ("Notice when trust arrives", "Stop copying their boss on everything, if they have.")],
    vocab=[("Counterpart", "The person on the other side responsible for the same thing."),
           ("Trust equation", "Trust grows with credibility, reliability and intimacy, and shrinks with self-interest."),
           ("No-surprises rule", "Agreeing that important news is always told first, directly."),
           ("Early warning", "Raising a likely problem while it's small and fixable."),
           ("Escalation", "Taking an issue to someone more senior; a last resort between partners."),
           ("Relationship capital", "Goodwill you build up and can spend when things go wrong.")],
    code=dict(file="notebook/elaine-thursdays.md", note="Ines's notebook · Thu 19 Aug 2027", src="""
THURSDAYS WITH ELAINE · 08:00 · café, floor 2          (6 of 6 held)

15 Jul  her agenda: Orion, again · mine: the first-week plan
        agreed: no surprises, both ways
22 Jul  her: Horizon headcount · mine: RACI workshop went well
29 Jul  her: steering was too long · mine: RN-01 (before it was sent) · £0
05 Aug  her: Rupert wants a cost slide · mine: access fixed, VPN works
12 Aug  her: Priya's under pressure · mine: D-09, Bert 1 day not 3
        → +2 weeks on data by Oct · proposal: 3 days to Nov, Lottie apprentice
19 Aug  her: "I moved Bert to three days. Talked to his manager." (no cc to Priya)
        mine: thank you. data plan back on track.

promises kept, visible: access tracker 09:00 daily (34 of 34 days)
"""),
    contract=dict(side="the contract says who; habits say how", doc="Lodestar SOW · §8.1 and Appendix C (D-09)", date="signed 30 June 2027", stamp="fixed in a café",
                  clauses=[("D-09", "MetroVolt provides a named MAVIS expert for three days per week from the Start Date.", "Bert, one day. fixed by Elaine, not by a notice."),
                           ("Sch. 7, 4", "Disputes … shall be referred to the Steering Committee.", "the path exists. the point of Thursdays is to rarely use it.")],
                  plain="the contract gives you the right to claim when the client's side slips. A good relationship lets the client fix it before you ever need to. Use the right sparingly; build the relationship every week."),
    health=dict(now="a",
                g=("trust earned", ["Keep the habits; they're what made it.", "Fewer formal notices.", "Don't take it for granted."]),
                a=("burned before, watching", ["Weekly hour, no surprises.", "Bad news early, with a fix.", "Visible small promises."]),
                r=("they're hostile", ["Keep the habits anyway, and write everything down.", "Use formal routes when needed.", "Ask whether someone else should be counterpart."])),
    pressure=dict(level=3, title="the wary partner", cost="six early mornings · one piece of bad news delivered",
                  items=["Telling a wary client bad news feels risky. Not telling them is riskier: they'll find out, and you'll be Orion.", "Trust grows slower than you'd like. Count the Thursdays, not the feelings."]),
    baseline="Each line compares <b>formal notices and reports only</b> with <b>a weekly hour, a no-surprises pact, early bad news and visible small promises</b>.",
    ratings=[(1, 4, "Elaine stops copying Priya on everything."),
             (3, 4, "Problems are fixed earlier, with less drama."),
             (3, 4, "D-09 fixed without a claim or a delay."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Bad news arrives while it's small."),
             (3, 3, "The habits are noted, not contractual."),
             (3, 3, "Weeks before it pays off."),
             (3, 3, "An hour a week, every week.")],
    pitfalls=[("Asking to be trusted", "Words don't move a burned client.", "small proofs, repeated."),
              ("Cancelling the weekly hour", "The habit breaks.", "never cancel; shorten if you must."),
              ("Bad news in writing first", "It reads like a claim.", "in person, then in writing."),
              ("Escalating before they can fix it", "They look weak to their boss.", "give them the chance first."),
              ("Surprising them through your own reports", "They read it in the status report first.", "the pact covers your reports too.")],
    grimoire=[(3, "conflict-phantom", "The Conflict Phantom", "is what a programme director becomes when bad news always arrives too late to fix.")],
    use=["Any client relationship that will last months.", "A counterpart burned by a previous supplier.", "From day one."],
    skip=["Never skip it. Shorten it when trust is solid."],
    related=["<b>Who Really Decides Here?</b> (this volume)", "<b>What Goes in the First Status Report?</b> (next note but one)", "<b>Managing Up</b> (Grace, vol. 5)", "<b>How Do We Keep Them With Us?</b> (Sanne, vol. 5)"],
    quiz=[("What are the four habits?", "A weekly hour on their agenda, a no-surprises pact, bad news early with a fix, and small promises kept visibly."),
          ("Why tell bad news in person first?", "In writing first it reads like a claim; in person it's a shared problem."),
          ("How was D-09 resolved?", "Ines told Elaine early with a proposal; Elaine moved Bert to three days herself."),
          ("Why let the client fix their side first?", "Escalating makes them look weak to their boss and costs trust."),
          ("What showed that trust had grown?", "Elaine fixed D-09 herself and stopped copying Priya.")],
    quiz_sit=[("Elaine asks Ines, off the record, whether Vexmoor's assurance notes are “fair”. What do you say?", "Stay factual and generous: point to the decision log and the evidence behind each decision, and offer to answer any specific point. Don't criticise Vexmoor; it would break the trust you're building with her too.")],
    try_it="Name your most important counterpart. Write down one weekly habit, one pact, one piece of bad news you should share early, and one small promise you could keep visibly every day.",
    remember="Trust isn't asked for. It's <span class=\"hl\">small promises kept, often</span>, and <span class=\"hl\">bad news told early</span>.",
    late=dict(when="Thu 19 August 2027 · 21:15 · hotel near The Grid",
              lines=["Elaine moved Bert to three days herself. Didn't copy Priya. Didn't tell me until it was done.",
                     "Six Thursdays. Thirty-four mornings of the access tracker. That's what it cost.",
                     "She said, “The last lot would have saved this for a steering.” I said, “I know.”"]),
    sources=["David Maister, Charles Green and Robert Galford, <i>The Trusted Advisor</i> (2000): the trust equation.",
             "Peter Block, <i>Flawless Consulting</i> (2011).",
             "Stephen M. R. Covey, <i>The Speed of Trust</i> (2006)."],
)

# ------------------------------------------------------------------ 13 How Do Two Companies Work as One Team?
ot_problem = Doodle(760, 240, "Doodle of floor 19 in August 2027. Wrenfield's six in room 19C on one side of the glass; MetroVolt's Lodestar people, Bert, two business analysts and a tester, at desks on the other side. Two task boards: Wrenfield's own, and MetroVolt's Jira. Two chats. Lunch at different times. A sticky note on the glass: us and them.",
                    "Two task boards, two chats, two lunchtimes, and a pane of glass.", exact=True)
ot_problem.box(24, 30, 300, 160, "Wrenfield · 19C", "blue", size=19)
ot_problem.box(436, 30, 300, 160, "MetroVolt · desks", "y", size=19)
ot_problem.line("M380 20 V200", dash=True)
ot_problem.note(174, 130, "own board · own chat", "pen", size=16)
ot_problem.note(586, 130, "Jira · Teams", "pen", size=16)
ot_problem.box(316, 90, 128, 50, "“us” / “them”", "pink", size=16)
ot_problem.note(380, 226, "one programme, two teams pretending", "red", size=19)

ot_how = Doodle(760, 330, "The team agreement of 9 August. Mixed squads: data (Bilal, Bert, a MetroVolt analyst), platform (Hana, a MetroVolt engineer), testing (Oskar, MetroVolt's tester). One board, MetroVolt's Jira. One chat channel. One stand-up at 09:30. Wrenfield moves out of 19C to mixed desks. And an honest line: who is paid by whom, who can instruct whom, and what each firm owns: Wrenfield owns delivery of the fixed scope, MetroVolt owns decisions and its data.",
                "Mix the squads, share the tools, and stay honest about who is paid by whom.", exact=True)
for i, (h, who) in enumerate([("data squad", "Bilal · Bert · MV analyst"), ("platform squad", "Hana · MV engineer"), ("testing squad", "Oskar · MV tester")]):
    ot_how.box(14 + i * 248, 14, 236, 90, h, "green", sub=who, size=19, subsize=15)
for i, t in enumerate(["one board (Jira)", "one channel", "stand-up 09:30", "mixed desks"]):
    ot_how.box(14 + i * 186, 124, 174, 50, t, "y", size=16)
ot_how.box(14, 194, 732, 90, "stay honest", "paper", sub="Wrenfield owns the fixed scope · MetroVolt owns decisions and data · only Elaine instructs", size=19, subsize=15)
ot_how.note(380, 314, "one team in how we work; two firms in what we owe", "pen", size=19)

ONE_TEAM = dict(
    slug="one-team", date=date(2027, 8, 9), meta="day 36 on site", where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “blended teams” across client and vendor",
    tldr="A programme fails when the vendor's team and the client's team work <b>side by side but apart</b>. Mix them into <b>squads</b> around the work, share <b>one board, one chat and one stand-up</b>, and sit together. But stay <b>honest about the contract</b>: who's paid by whom, who can instruct whom, and what each firm owns. One team in how you work; two firms in what you owe.",
    chips=[("Family", "two firms, one team"), ("Lives in", "delivery/lodestar/team-agreement.md"), ("Pairs with", "the RACI, the client counterpart")],
    problem_side="The Grid, floor 19, 9 August 2027",
    problem="""  <p class="lead">Five weeks in, floor 19 has <b>two Lodestar teams</b>. Wrenfield's six work in room 19C with their own task board and their own chat. MetroVolt's people (Bert, two business analysts, a tester and an engineer) sit at desks outside the glass and use MetroVolt's Jira and Teams.</p>
  <ul>
    <li>Questions cross the glass by email. Answers take a day.</li>
    <li>Lunch is at different times. Someone has stuck a note on the glass: <i>“us / them”</i>. Nobody admits to it.</li>
    <li>MetroVolt's analysts have heard Horizon will cut 600 roles. <span class="hl-pink">Some of them think Wrenfield is here to replace them.</span></li>
  </ul>""",
    problem_figs=[ot_problem],
    sides=dict(client=("MetroVolt's Lodestar staff", "<p>MetroVolt's people know the system and the customers. They also know that suppliers come and go and <b>they stay</b>, and that in a Horizon year, the people who “helped the supplier replace the old system” may be next. Being asked their opinion matters more than any tool.</p>", "Are we your team, or your users?"),
                vendor=("Ines and Hana", "<p>Wrenfield needs MetroVolt's knowledge daily, not by email. It also needs to stay clear about its contract: Wrenfield is accountable for the fixed scope, can't be directed by anyone except Elaine, and can't quietly take on MetroVolt's work.</p>", "Sit together. Owe separately.")),
    sides_after="Blending teams is easy to say and hard to do because two employers, two pay scales and two futures don't disappear when you share a board.",
    analogy_side="the hospital and the agency nurses",
    analogy="""  <p>On a busy ward, agency nurses and staff nurses work <b>one shift, one handover, one patient board</b>. Nobody treats a patient differently because of who pays their nurse. But everyone knows that the <b>ward sister decides</b>, and the agency nurse's contract says what she can and can't do. One team on the ward; two employers on paper.</p>""",
    map=[("One handover, one patient board", "One stand-up, one Jira board"),
         ("Agency and staff nurses side by side", "Mixed squads: data, platform, testing"),
         ("The ward sister decides", "Only Elaine instructs Wrenfield"),
         ("The agency nurse's contract", "Wrenfield's fixed scope"),
         ("Staff nurses stay after the agency leaves", "MetroVolt's people run Lodestar after wave 4")],
    how_side="mixed squads, shared tools, honest lines",
    how="""  <p>On <b>Monday 9 August</b>, Ines and Elaine run a one-hour session with everyone on the programme and write a <b>team agreement</b> together.</p>
  <ul>
    <li><b>Squads around the work</b>, each mixed: <b>data</b> (Bilal, Bert, a MetroVolt analyst), <b>platform</b> (Hana and a MetroVolt engineer), <b>testing</b> (Oskar and MetroVolt's tester).</li>
    <li><b>One of everything</b>: MetroVolt's Jira (Wrenfield drops its own board), one Teams channel, one stand-up at 09:30. Wrenfield moves out of 19C to mixed desks.</li>
    <li><b>Honest lines</b>, said out loud: Wrenfield owns delivery of the fixed scope; MetroVolt owns decisions, its data and running Lodestar afterwards; only Elaine can instruct Wrenfield; MetroVolt's people are <b>learning the new platform as it's built</b>, because they'll run it.</li>
  </ul>
  <p>The last line answers the unspoken fear: MetroVolt's people aren't being replaced by Wrenfield; they're the ones Wrenfield is building it for, and handing it to. Bert says it better: “So the kid learns my COBOL, and I learn her platform.” Lottie and Bert have been doing that since July.</p>""",
    how_figs=[ot_how],
    steps=[("Build squads around the work", "Each with people from both firms."),
           ("One board, one chat, one stand-up", "The client's tools, usually."),
           ("Sit together", "Leave the glass room."),
           ("Say who owns what, out loud", "Scope, decisions, data, running it later."),
           ("Address the unspoken fear", "Whose jobs, whose future."),
           ("Write it down together", "A one-page team agreement, signed by both leads.")],
    vocab=[("Blended team", "A team with people from client and vendor working as one."),
           ("Squad", "A small cross-functional team around one area of work."),
           ("Team agreement", "A short, shared set of rules for how a team works."),
           ("Knowledge transfer", "Moving know-how from one group to another, ideally all along, not at the end."),
           ("Instruction", "A contractual direction; only named people can give it."),
           ("Disguised employment", "Treating a supplier's staff like your own employees; a legal and contractual risk.")],
    code=dict(file="delivery/lodestar/team-agreement.md", note="agreed Mon 9 Aug 2027 · signed by Elaine and Ines", src="""
LODESTAR TEAM AGREEMENT · v1

squads        data      Bilal · Bert Ogundipe · MetroVolt analyst (Asif)
              platform  Hana · MetroVolt engineer (Marta)
              testing   Oskar · MetroVolt tester (Rosa)
tools         one board: MetroVolt Jira (LODE) · one channel: #lodestar · stand-up 09:30
seating       mixed desks, floor 19 (19C becomes the workshop room)

honest lines
  Wrenfield owns delivery of the fixed scope (Schedule 2)
  MetroVolt owns decisions, its data, and running Lodestar after wave 4
  only Elaine (or steering) instructs Wrenfield; anyone can ask
  MetroVolt staff learn the platform as it's built: they will run it
pairs         Bert ↔ Lottie (MAVIS ↔ platform), Marta ↔ Hana
"""),
    contract=dict(side="where “one team” stops", doc="Lodestar SOW · §8.5 and §11 (exit)", date="signed 30 June 2027", stamp="two firms",
                  clauses=[("8.5", "Instructions to the Supplier are valid only if given by MetroVolt's Programme Director or the Steering Committee.", "so a MetroVolt squad member can ask Hana; only Elaine can instruct her."),
                           ("11.2", "The Supplier shall transfer knowledge to MetroVolt staff throughout the Services, so that MetroVolt can operate the solution at the end of Wave 1.", "mixed squads aren't a nicety. they're §11.2.")],
                  plain="the contract usually supports blended teams (knowledge transfer) and limits them (who can instruct). Say both out loud, so a friendly team doesn't drift into unpriced work or blurred responsibilities."),
    health=dict(now="a",
                g=("trust is high", ["Blend fully.", "Still say the honest lines.", "Celebrate together."]),
                a=("staff fear for their jobs", ["Mixed squads, client's tools.", "Say who'll run it afterwards.", "Pair experts with learners."]),
                r=("hostile staff", ["Start with one pair, not a reorg.", "Make knowledge transfer visible.", "Never let your people be instructed around the contract."])),
    pressure=dict(level=3, title="us and them", cost="a note on the glass · one reorganisation of desks",
                  items=["People are anxious about their jobs in a cut year. The honest line about who runs it afterwards matters more than any team-building.", "Giving up your own board and chat feels like losing control. It's gaining a team."]),
    baseline="Each line compares <b>two teams side by side</b> with <b>mixed squads, shared tools and honest lines about the contract</b>.",
    ratings=[(3, 4, "MetroVolt staff are part of the work, not watching it."),
             (2, 4, "Answers in minutes, not by email."),
             (3, 3, "Neutral; risk of drifting into unpriced work is managed by §8.5."),
             (3, 4, "Who owns what is said out loud."),
             (3, 4, "Bert's knowledge is in the squad, daily."),
             (2, 4, "Problems are seen at stand-up."),
             (3, 3, "Neutral."),
             (3, 4, "A one-hour session."),
             (3, 3, "One set of rituals to run.")],
    pitfalls=[("Side by side but apart", "Two boards, two chats, two lunches.", "one of everything."),
              ("Pretending there's one employer", "Blurred instructions, unpriced work.", "honest lines about the contract."),
              ("Ignoring the job fear", "Quiet resistance.", "say who'll run it afterwards, and mean it."),
              ("Vendor tools by default", "The client can't see the work.", "use the client's tools."),
              ("Knowledge transfer at the end", "A handover nobody can absorb.", "pairs from the start.")],
    grimoire=[(7, "cult-of-family", "The Cult of Family", "is the opposite mistake: pretending everyone is family, and forgetting the contract.")],
    use=["Vendor and client staff work on the same system.", "The client will run what you build.", "A cut or reorg makes staff anxious."],
    skip=["A fully outsourced job with no client staff involved: still share one board with the client lead."],
    related=["<b>Who Does What When Three Firms Share a Project?</b> (this volume)", "<b>How Do We Earn the Programme Director's Trust?</b> (this volume)", "<b>Dependencies across Teams</b> (Grace, vol. 5)", "<b>Why Is the Team Arguing?</b> (Sanne, vol. 4)"],
    quiz=[("What does “one team in how we work, two firms in what we owe” mean?", "Share squads, tools and rituals, but be clear about scope, instructions and responsibilities."),
          ("Why use the client's tools?", "The client can see the work, and will own it afterwards."),
          ("Who can instruct Wrenfield?", "Only Elaine or the steering committee; anyone can ask."),
          ("What fear did the honest lines address?", "That Wrenfield was there to replace MetroVolt's staff."),
          ("Why pair Bert with Lottie?", "MAVIS knowledge moves to Wrenfield and platform knowledge to MetroVolt, all along.")],
    quiz_sit=[("A MetroVolt analyst in the data squad asks Bilal to also fix a report for her other team. What should Bilal do?", "Say he'll help her raise it with Elaine; it's outside the fixed scope and outside what anyone but Elaine can instruct. Offer to show her how, if it's quick, and record it.")],
    try_it="Look at a team you share with another firm or department. Count the boards, chats and stand-ups. Write a one-page agreement: squads, tools, seating, and three honest lines about who owns what.",
    remember="Mix the squads, share <span class=\"hl\">one board, one chat, one stand-up</span>, and say out loud <span class=\"hl\">who owes what</span>.",
    late=dict(when="Mon 9 August 2027 · 20:40 · hotel near The Grid",
              lines=["Moved out of the goldfish bowl. 19C is a workshop room now. The note on the glass came down by itself.",
                     "Bert: “So the kid learns my COBOL, and I learn her platform.” Best summary of the programme so far.",
                     "Asif asked me quietly if his job was safe. I said they'll run Lodestar after us. I hope Horizon agrees."]),
    sources=["Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019).",
             "Amy Edmondson, <i>The Fearless Organization</i> (2018).",
             "UK HMRC, guidance on off-payroll working and disguised employment."],
)

# ------------------------------------------------------------------ 14 What Goes in the First Status Report?
sr_problem = Doodle(760, 240, "Doodle of two drafts of the first status report, due Friday 30 July 2027. Callum's draft is green: Wrenfield is on track, delays are MetroVolt's fault. Ines's draft is amber, and its first line says discovery is nine working days behind because the team cannot log in. A thought bubble over Callum: but it isn't our fault.",
                    "Callum's draft: green, because it isn't our fault. Ines's: amber, because it's true.", exact=True)
sr_problem.box(24, 30, 320, 150, "draft 1 · Callum", "green", sub="“on track; delays are MetroVolt's”", size=19, subsize=15)
sr_problem.box(416, 30, 320, 150, "draft 2 · Ines", "y", sub="“9 working days behind: no logins”", size=19, subsize=15)
sr_problem.note(380, 220, "the colour is about the project, not the blame", "red", size=20)

sr_how = Doodle(760, 320, "The first status report, one page. Top line: the colour, amber, and the one sentence that explains it. Then four boxes: done this week, next week, the risks and issues with owners, and decisions needed. At the bottom, the rules: colours by agreed definitions, facts before adjectives, bad news in the first line, no blame, same format every week.",
                "One page: the colour and why, done, next, risks, decisions. Same every Friday.", exact=True)
sr_how.box(14, 14, 732, 64, "AMBER · discovery 9 working days behind: the team can't log in", "y", size=18)
for i, (h, sub) in enumerate([("done", "18 interviews · RACI"), ("next", "VPN · MAVIS · DA #1"), ("risks + issues", "D-05 (RN-01) · D-09"), ("decisions", "approve RN-01")]):
    sr_how.box(14 + i * 186, 90, 174, 110, h, "paper", sub=sub, size=18, subsize=14)
sr_how.box(14, 216, 732, 64, "rules", "blue", sub="defined colours · facts first · bad news in line 1 · no blame · same format", size=18, subsize=15)
sr_how.note(380, 306, "Elaine read it on Thursday, before it was sent", "pen", size=18)

FIRST_STATUS = dict(
    slug="first-status-report", date=date(2027, 7, 30), meta="day 26 on site", where="FL 19",
    kicker="a.k.a. “status reporting”: the first one sets the tone",
    tldr="The first status report teaches the client how to read every report after it. Make the <b>colour</b> follow <b>agreed definitions</b>, not blame: if the project is behind, it's amber, whoever caused it. Put the <b>bad news in the first line</b>, <b>facts before adjectives</b>, owners next to every risk, and the decisions you need. Same format every week. A green report that turns red in month six is how Orion ended.",
    chips=[("Family", "two firms, one team"), ("Lives in", "delivery/lodestar/status/2027-07-30.md"), ("Pairs with", "access purgatory, the baseline, the client counterpart")],
    problem_side="The Grid, Friday 30 July 2027",
    problem="""  <p class="lead">The first weekly status report is due on <b>Friday 30 July</b>. Discovery is <b>nine working days behind</b>: the laptops arrived on day 23, and MAVIS access hasn't.</p>
  <ul>
    <li>Callum's draft is <b>green</b>: “Wrenfield is on track against its own activities. Delays are due to MetroVolt dependencies.”</li>
    <li>His reasoning: amber looks like Wrenfield is failing, and <span class="hl-pink">it isn't Wrenfield's fault</span>.</li>
    <li>Elaine has read Orion's status reports. They were green for 22 months.</li>
  </ul>""",
    problem_figs=[sr_problem],
    sides=dict(client=("Elaine reads it", "<p>Elaine will read the first report for one thing: <b>does this supplier tell the truth when it's inconvenient?</b> A green report while her own team can't hand over laptops would tell her Wrenfield's colours mean nothing.</p>", "If it's green now, I can't trust green later."),
                vendor=("Callum and Ines argue", "<p>Callum's worry is real: Graham, Priya and Vexmoor will all read the colour without the sentence. Ines's answer: <b>the colour describes the project, not the fault</b>. The sentence underneath says whose dependency it is, without blame. Amber now buys belief later.</p>", "Our colours have to mean something from week one.")),
    sides_after="A status report has one job: make the next decision easier. The colour only helps if everyone agrees what it means.",
    analogy_side="the weather forecast",
    analogy="""  <p>A weather forecaster says “70 % chance of rain” because that's what the data says, not because rain would be someone's fault. A forecaster who said “sunny” to avoid upsetting people would be right some days, and <b>never believed again</b> after the first wedding washed out.</p>""",
    map=[("70 % chance of rain", "Amber: nine working days behind"),
         ("Not someone's fault", "The colour describes the project, not the blame"),
         ("The data behind it", "The access tracker"),
         ("Saying “sunny” to be nice", "A green report while nobody can log in"),
         ("Never believed again", "Orion's 22 green months")],
    how_side="defined colours, bad news first, one page, every Friday",
    how="""  <p>Ines and Callum agree <b>colour definitions</b> with Elaine first (they go in the governance schedule): <b>green</b>, on track for the next milestone; <b>amber</b>, at risk but recoverable with actions already planned; <b>red</b>, won't make the milestone without a decision from steering. By that definition, discovery is amber, whoever caused it.</p>
  <p>The report is <b>one page</b>. Line one: <b>AMBER. Discovery is 9 working days behind because the team cannot log in.</b> Then four boxes: <b>done</b> (18 interviews, the RACI workshop, the kick-off), <b>next</b> (VPN, MAVIS access, the first design authority), <b>risks and issues</b> with owners (D-05 late, relief notice RN-01; D-09 at risk), and <b>decisions needed</b> (approve RN-01 at steering).</p>
  <p>No adjectives without facts (“excellent progress” is deleted). No blame (“due to MetroVolt failures” becomes “D-05, delivered 27 July, promised 16 July”). Ines shows it to Elaine on Thursday, under the no-surprises pact. Elaine changes one word and says: <i>“Amber. Good. Orion was green for 22 months.”</i></p>""",
    how_figs=[sr_how],
    steps=[("Agree colour definitions first", "With the client, in writing."),
           ("Colour the project, not the blame", "Whose fault goes in the sentence, not the colour."),
           ("Bad news in line one", "The reader may read nothing else."),
           ("Facts before adjectives", "Dates and numbers, not “excellent”."),
           ("Owners and decisions", "Every risk has a name; every report asks for something."),
           ("Same format every week", "So changes stand out.")],
    vocab=[("RAG status", "Red, amber, green: a colour summarising progress."),
           ("Watermelon report", "Green on the outside, red inside: a report hiding problems."),
           ("Status report", "A regular summary of progress, risks and decisions needed."),
           ("Issue", "A problem happening now; a risk is one that might."),
           ("Colour definitions", "Agreed meanings for each status colour."),
           ("Exception reporting", "Reporting mainly what's off-plan, not everything.")],
    code=dict(file="delivery/lodestar/status/2027-07-30.md", note="weekly status #4 · Fri 30 Jul 2027", src="""
LODESTAR · WEEKLY STATUS #4 · Fri 30 Jul 2027                         AMBER
Discovery is 9 working days behind because the team cannot log in.

done        18 discovery interviews · RACI workshop (02:10 file) · kick-off
            · 40 MAVIS documents read · first-week plan complete
next        VPN (4 Aug) · contractor badges (4 Aug) · MAVIS read access (?)
            · design authority #1 (4 Aug)
risks / issues                                  owner         action
  I-01  D-05 delivered 27 Jul (promised 16 Jul) Yusuf (MV IT)  RN-01 sent, 11 wd
  R-03  D-09 Bert at 1 day/week, not 3          Elaine        to discuss Thu
decisions   steering 28 Jul approved RN-01 (DL-001) → discovery end 10 Dec

colours: green = on track for next milestone · amber = at risk, recoverable with
planned actions · red = needs a steering decision
"""),
    contract=dict(side="what the contract says about reporting", doc="Lodestar SOW · Schedule 7 (governance), §5", date="v1.1 · 2 Aug 2027", stamp="defined",
                  clauses=[("5.1", "The Supplier shall provide a weekly status report by 17:00 each Friday in the format in Annex B.", "promise P-12, now a clause."),
                           ("5.2", "<ins>Status colours have the meanings in Annex B and describe progress against the next Milestone, irrespective of cause.</ins>", "“irrespective of cause”. Callum's sentence, in the end. he wrote it.")],
                  plain="if status colours are defined in the contract, “irrespective of cause”, nobody can argue the colour to avoid blame. The cause goes in the sentence underneath."),
    health=dict(now="a",
                g=("trust is high", ["Shorter reports.", "Same honest colours.", "Fewer surprises to report."]),
                a=("burned by green reports", ["Defined colours, bad news first.", "Show it to the counterpart before sending.", "Facts, not adjectives."]),
                r=("reports used as evidence", ["Facts and dates only.", "Every cause referenced to a document.", "Same format, always on time."])),
    pressure=dict(level=3, title="the first colour", cost="one argument with a colleague · one amber the managing director will see",
                  items=["Callum's fear (amber looks like failure) is common and reasonable. Agree the definitions together and the argument goes away.", "Graham will see amber and call. Tell him first, with the sentence."]),
    baseline="Each line compares <b>a green report that blames the client</b> with <b>an amber report by agreed definitions, bad news first, causes as facts</b>.",
    ratings=[(1, 5, "Elaine: “Amber. Good.”"),
             (3, 4, "Nobody has to keep a story straight."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Risks have owners and dates."),
             (2, 5, "Causes recorded as facts, weekly."),
             (4, 4, "An hour on Friday."),
             (4, 4, "One page, same format.")],
    pitfalls=[("Colouring the blame", "Green, because it's not your fault.", "colours describe the project."),
              ("No definitions", "Everyone's amber means something different.", "define them, in writing."),
              ("Bad news at the bottom", "The reader stops at line two.", "line one."),
              ("Adjectives", "“Excellent progress”, nine days late.", "facts and dates."),
              ("Surprising the client lead", "They read it with their boss.", "show them first.")],
    grimoire=[(2, "toxic-positivity-siren", "The Toxic Positivity Siren", "sings “no problems, only opportunities” as the ship sinks. Status reports are where she lives.")],
    use=["Every regular report on a project.", "The first one, especially.", "A client burned by green reports."],
    skip=["Never skip it; shrink it if the project is small."],
    related=["<b>Why Can't We Log In?</b> (this volume)", "<b>How Do We Earn the Programme Director's Trust?</b> (this volume)", "<b>What Are We Measured Against?</b> (next note)", "<b>Status Reports That Tell the Truth</b> (Sanne, vol. 2)"],
    quiz=[("What do Lodestar's colours describe?", "Progress against the next milestone, irrespective of cause."),
          ("Where does the cause go?", "In the sentence and the risks, as facts with dates, not in the colour."),
          ("What is a watermelon report?", "Green outside, red inside: a report that hides problems."),
          ("Why show the report to Elaine before sending?", "The no-surprises pact: she shouldn't read bad news first with her boss."),
          ("What's in the four boxes?", "Done, next, risks and issues with owners, decisions needed.")],
    quiz_sit=[("Graham phones: “Why are we amber? It's their fault!” What do you say?", "Amber describes the project: it's nine days behind. The report says plainly it's D-05 and that relief was claimed and approved. An honest amber now is why Elaine will believe a green later.")],
    try_it="Write next week's status report for your work in one page: a colour by a definition you'd agree with your client, the bad news in line one, then done, next, risks with owners and decisions needed. Who should see it before it's sent?",
    remember="Colour the <span class=\"hl\">project, not the blame</span>. Bad news <span class=\"hl\">in line one</span>.",
    late=dict(when="Fri 30 July 2027 · 19:30 · the train home",
              lines=["Amber. Callum didn't like it. He wrote the “irrespective of cause” sentence himself in the end.",
                     "Elaine: “Amber. Good. Orion was green for 22 months.”",
                     "Graham called at 17:20. I said the sentence. He said “fine” and asked about the VPN."]),
    sources=["Project Management Institute, <i>PMBOK Guide</i>: performance reporting.",
             "Tom DeMarco and Timothy Lister, <i>Waltzing with Bears</i> (2003).",
             "UK Infrastructure and Projects Authority, delivery confidence assessment guidance."],
)

# ------------------------------------------------------------------ 15 What Are We Measured Against?
bl_problem = Doodle(760, 250, "Doodle of what has changed since the bid. The start moved from June to 5 July. Discovery moved to 10 December after relief. Training changed to train-the-trainer in the final offer. Bert's days changed. The sample showed 7.8 per cent, not 5. Five things, and no single document that holds the current version of the deal.",
                    "Five things have moved since the bid. No single page says what the deal is now.", exact=True)
moved = [("start", "1 Jun → 5 Jul"), ("discovery end", "26 Nov → 10 Dec"), ("training", "→ train-the-trainer"), ("Bert", "1 → 3 days"), ("A1-07", "5 % → 7.8 % sample")]
for i, (h, sub) in enumerate(moved):
    bl_problem.box(14 + i * 148, 40, 140, 100, h, "pink", sub=sub, size=18, subsize=14)
bl_problem.note(380, 200, "so what are we measured against?", "red", size=21)

bl_analogy = Doodle(760, 210, "Doodle of a ship's chart with the planned route drawn in pencil and a position fix marked at the start of the voyage. Every later position is compared with that line. If the route changes, the navigator draws a new line, dates it, and keeps the old one visible.",
                    "A navigator's planned line, dated. Every later position is measured against it.", exact=True)
bl_analogy.box(30, 20, 700, 170, None, "blue", rx=6)
bl_analogy.line("M80 160 C 250 150 400 80 680 50", dash=True)
bl_analogy.circle(80, 160, 10, "y")
bl_analogy.note(120, 186, "fix, 28 Sep", "pen", size=18)
bl_analogy.circle(420, 108, 10, "pink")
bl_analogy.note(430, 140, "where are we vs the line?", "red", size=18)

bl_how = Doodle(760, 390, "Baseline version 1.0, signed at steering on 28 September 2027. Scope: Schedule 2 version 1.0 and the change register. Plan: discovery ends 10 December, report 14 December, pilot of 20,000 accounts live on 6 March 2028, wave 1 of 380,000 on 24 June 2028. Money: 5.0 million pounds, 380,000 discovery and 4.62 million fixed. Risks: top ten, with A1-07 marked at risk. Assumptions: 41, two updated. Vexmoor's assurance note: data migration plan optimistic. Every later change is measured against this page.",
                "One page, signed: scope, plan, money, risks, assumptions. Version 1.0, and a rule for 1.1.", exact=True)
blocks = [("scope", "Schedule 2 v1.0 · change register", "y"), ("plan", "pilot 6 Mar 2028 · wave 1 24 Jun 2028", "blue"),
          ("money", "£5.0m = £380k + £4.62m", "green"), ("risks", "top 10 · A1-07 at risk (7.8 %)", "pink"), ("assumptions", "41 · 2 updated", "paper")]
for i, (h, sub, fill) in enumerate(blocks):
    bl_how.box(14, 14 + i * 60, 480, 56, h, fill, sub=sub, size=17, subsize=14)
bl_how.box(510, 14, 236, 296, "v1.0", "y", sub="steering · 28 Sep 2027", size=28, subsize=15)
bl_how.note(380, 344, "Vexmoor's note: “data migration plan optimistic”", "red", size=18)
bl_how.note(380, 372, "changes → v1.1, only through steering", "pen", size=18)

BASELINE = dict(
    slug="the-baseline", date=date(2027, 9, 28), meta="day 86 on site", where="FL 27", pass_kind="contractor",
    kicker="a.k.a. “the baseline”: scope, plan, cost and risk, signed",
    tldr="By the time a project has really started, the deal has already moved: a late start, relief, traded scope, an assumption that looks shaky. Before the work gets serious, agree a <b>baseline</b>: <b>one page</b> (plus its documents) with the current <b>scope</b>, <b>plan</b>, <b>money</b>, <b>risks</b> and <b>assumptions</b>, <b>signed at steering</b>. Every later change, delay or argument is then measured against the same thing, and changes to the baseline only happen through steering.",
    chips=[("Family", "two firms, one team"), ("Lives in", "delivery/lodestar/baseline-v1.0.pdf · DL-014"), ("Pairs with", "change control, the first status report, acceptance")],
    problem_side="The Grid, room 27A, 28 September 2027",
    problem="""  <p class="lead">Twelve weeks in, the deal Wrenfield is delivering isn't quite the one it bid. The start moved from 1 June to <b>5 July</b>. Discovery now ends on <b>10 December</b> (relief RN-01). Training became <b>train-the-trainer</b> in the final offer. <b>Bert</b> moved from one day a week to three. And MetroVolt's sample showed <b>7.8 %</b> of addresses failing, not the 5 % in A1-07.</p>
  <ul>
    <li>Each change is recorded somewhere: the change register, the decision log, the BAFO letter, a relief notice.</li>
    <li>Nobody has a single page that says <b>what the deal is now</b>.</li>
    <li>Vexmoor's first assurance note, due at the September steering, will compare Wrenfield's progress against <span class="hl-pink">something</span>. Ines would like it to be the right thing.</li>
  </ul>""",
    problem_figs=[bl_problem],
    sides=dict(client=("Priya and Nkem", "<p>MetroVolt needs <b>one set of numbers</b> for Horizon: what Lodestar costs, when the pilot goes live, what's at risk. Finance can't report against five documents. Priya wants the September steering to sign something she can show Rupert.</p>", "Give me the one page I'll be measured against too."),
                vendor=("Ines and Callum", "<p>Wrenfield wants every later conversation, especially with Vexmoor, to start from <b>an agreed starting line</b>, not from the bid or a memory. A signed baseline also records, in public, that A1-07 is already “at risk”, three months before discovery tests it.</p>", "Measure us against what we agreed, all of it, on one page.")),
    sides_after="A baseline isn't a plan you promise never to change. It's the plan you agree to change only in the open.",
    analogy_side="the navigator's planned line",
    analogy="""  <p>A ship's navigator draws the <b>planned route</b> in pencil and marks a <b>fix</b> at the start of the voyage. Every later position is compared with that line: ahead, behind, off course. If the route changes, the navigator <b>draws a new line, dates it</b>, and keeps the old one visible. Nobody argues about where the ship should be, because the line is on the chart.</p>""",
    analogy_figs=[bl_analogy],
    map=[("The planned route", "The plan: pilot 6 March, wave 1 24 June 2028"),
         ("The starting fix", "Baseline v1.0, 28 September 2027"),
         ("Ahead, behind, off course", "Status against the baseline"),
         ("A new dated line", "Baseline v1.1, only through steering"),
         ("The old line kept visible", "Earlier versions kept and referenced")],
    how_side="one page, five parts, signed, versioned",
    how="""  <p>Callum and Ines assemble <b>baseline v1.0</b> from the documents that already exist, so nothing is new and everything is in one place:</p>
  <ul>
    <li><b>Scope</b>: Schedule 2 v1.0 (approved at the design authority on 15 September) plus the change register (CR-001; CN-001).</li>
    <li><b>Plan</b>: discovery ends <b>10 December</b>, report on <b>14 December</b>; pilot (20,000 accounts) live <b>Monday 6 March 2028</b>; wave 1 (380,000) go-live <b>Saturday 24 June 2028</b>.</li>
    <li><b>Money</b>: <b>£5.0m</b> (£380k discovery, £4.62m fixed); £142k left in the change pool.</li>
    <li><b>Risks</b>: the top ten, each with an owner. Number one: <b>A1-07 at risk</b>: the sample shows 7.8 %; full profiling in discovery.</li>
    <li><b>Assumptions</b>: all 41; two updated (D-09 met at three days; X-04 is now train-the-trainer).</li>
  </ul>
  <p>At steering on <b>Tuesday 28 September</b> in room 27A, Priya signs it; it's logged as <b>DL-014</b>. Oliver Thane presents Vexmoor's first assurance note. Its main finding: <b>“the data migration plan is optimistic”</b>. Ines thanks him, and points to risk 1 on the baseline: <i>“We agree. It's the first thing discovery tests, and it's priced in A1-07.”</i> From now on, changes to the baseline happen only at steering, as v1.1, v1.2.</p>""",
    how_figs=[bl_how],
    steps=[("Collect what has already changed", "Start date, relief, traded scope, assumptions."),
           ("Assemble one page from existing documents", "Scope, plan, money, risks, assumptions."),
           ("Mark what's already at risk", "Say it now, publicly."),
           ("Sign it at steering", "Logged, versioned, v1.0."),
           ("Report against it every week", "Status compares with the baseline, not with the bid."),
           ("Change it only through steering", "New version, dated, old one kept.")],
    vocab=[("Baseline", "The agreed version of scope, plan, cost and risk that progress is measured against."),
           ("Re-baseline", "Formally agreeing a new baseline after a significant change."),
           ("Variance", "The difference between where you are and the baseline."),
           ("Schedule 2", "Lodestar's solution description, now version 1.0."),
           ("Assurance note", "An independent reviewer's written findings."),
           ("Version control", "Keeping each version dated and the old ones visible.")],
    code=dict(file="delivery/lodestar/baseline-v1.0.md", note="signed at steering · Tue 28 Sep 2027 · DL-014", src="""
LODESTAR BASELINE v1.0                       signed: Priya Nair · 28 Sep 2027 · DL-014

scope        Schedule 2 v1.0 (DA, 15 Sep) · change register: CR-001 £8k · CN-001
plan         start 5 Jul 2027 · discovery ends 10 Dec (RN-01) · report 14 Dec
             M2 design approved  Jan 2028
             M3 pilot 20,000     Mon 6 Mar 2028
             M4 wave 1 380,000   Sat 24 Jun 2028
money        £5.0m = discovery £380k (T&M, capped) + wave 1 £4.62m (fixed)
             change pool £150k, used £8k
risks (top)  R-01 A1-07 at risk: sample 7.8 % fail (limit 5 %) → full profile in discovery
             R-02 change detection unproven (3 options) · R-03 Halvorsen spec (D-03, 30 Jul ✓)
assumptions  41 · updated: D-09 (3 days, met) · X-04 (train-the-trainer, BAFO)
assurance    Horizon assurance note #1 (Vexmoor): "data migration plan optimistic"
             → agreed; = R-01
changes      only through steering, as v1.1, v1.2 …
"""),
    contract=dict(side="what the baseline does to the contract", doc="Lodestar SOW · §4.2.4 and Schedule 4", date="as amended 28 Sep 2027", stamp="baselined",
                  clauses=[("4.2.4", "Milestone dates will be re-baselined at the end of discovery by agreement.", "and we'll be back here in December. A1-07 will decide how."),
                           ("Sch. 4, 1.3", "<ins>Baseline v1.0 (DL-014) sets the Milestone dates for the purposes of this Schedule until amended under clause 7.</ins>", "now there's one set of dates, signed.")],
                  plain="a signed baseline becomes the reference the contract measures you against. Put in it everything that has already changed, and every risk you already see, so the next argument starts from the truth."),
    health=dict(now="a",
                g=("trust is high", ["A short baseline, signed quickly.", "Re-baseline calmly when needed.", "Still versioned."]),
                a=("an outside assurer watching", ["Everything already changed, in one page.", "Name the risks the assurer will find, first.", "Signed and logged."]),
                r=("arguments about what was agreed", ["Baseline everything, with sources.", "Never report against anything else.", "Change only through steering."])),
    pressure=dict(level=3, title="the starting line", cost="a long week of paperwork · one critical assurance note",
                  items=["Hearing a rival call your plan “optimistic” in front of the sponsor stings. Having already written it down as risk 1 takes the sting out.", "The baseline is where A1-07 becomes public. December will be easier for it."]),
    baseline="Each line compares <b>being measured against the bid and memory</b> with <b>a signed, one-page baseline that includes every change and the known risks</b>.",
    ratings=[(3, 4, "Priya has one page for Rupert."),
             (3, 4, "Everyone knows the dates that count."),
             (3, 4, "Relief and traded scope are in the baseline."),
             (3, 5, "Scope = Schedule 2 v1.0 + the register."),
             (3, 4, "Risks are stated, not hidden in the design."),
             (2, 4, "A1-07 is risk 1, in public, before discovery tests it."),
             (2, 5, "Signed, logged, versioned."),
             (3, 3, "A week to assemble."),
             (3, 3, "Versions to keep.")],
    pitfalls=[("Measuring against the bid", "The deal has moved since.", "a baseline with every change in it."),
              ("A baseline in ten documents", "Nobody can see it.", "one page that points to the documents."),
              ("Hiding known risks", "An assurer finds them first.", "name them in the baseline."),
              ("Changing it quietly", "Nobody knows which version counts.", "only through steering, versioned."),
              ("Treating it as a promise never to change", "Then it's ignored when reality moves.", "agree to change it openly.")],
    grimoire=[(5, "suits-from-beyond", "The Suits from Beyond", "explains how to talk to consultants who review your work without talking yourself out of a job.")],
    use=["Once a project's start has settled.", "After any big change (end of discovery, a major CR).", "When someone independent will measure you."],
    skip=["A small, short piece of work where the contract is the baseline."],
    related=["<b>How Do We Change the Deal Without a War?</b> (this volume)", "<b>What Goes in the First Status Report?</b> (previous note)", "<b>How Will We Know It's Done?</b> (this volume)", "<b>What Exactly Did We Promise?</b> (Sanne, vol. 2)"],
    quiz=[("What five parts does Lodestar's baseline have?", "Scope, plan, money, risks and assumptions."),
          ("Why assemble it from existing documents?", "Nothing new needs agreeing; it just puts the current deal on one page."),
          ("Why mark A1-07 as risk 1 publicly?", "It was already likely; naming it first means the assurer's finding agrees with Wrenfield instead of exposing it."),
          ("How can the baseline change?", "Only through steering, as a new dated version."),
          ("What are the milestone dates in v1.0?", "Pilot Monday 6 March 2028; wave 1 go-live Saturday 24 June 2028.")],
    quiz_sit=[("Oliver suggests the baseline should say “wave 1 by June 2028, guaranteed”. What do you say?", "No: the baseline records the agreed plan and its risks, and the contract already says dates are re-baselined after discovery. Adding “guaranteed” would hide risk 1, which his own note found.")],
    try_it="Write a one-page baseline for your current work: scope, plan, money, risks, assumptions, each pointing to where it's recorded. What has already changed since the start? Who would sign it?",
    remember="Agree <span class=\"hl\">the starting line</span>, sign it, and change it <span class=\"hl\">only in the open</span>.",
    late=dict(when="Tue 28 September 2027 · 23:05 · hotel near The Grid",
              lines=["Baseline v1.0. Signed. DL-014. Pilot on 6 March, wave 1 on 24 June.",
                     "Oliver said “optimistic”. I said “risk 1”. Priya looked at both of us and wrote something down.",
                     "Discovery starts properly next week. MAVIS access, finally. A1-07 is waiting for us in the data. I can feel it."]),
    sources=["Project Management Institute, <i>PMBOK Guide</i>: baselines and performance measurement.",
             "UK Infrastructure and Projects Authority, <i>Gateway review</i> guidance.",
             "NEC4: the accepted programme."],
)

NOTES = [RACI, COUNTERPART, ONE_TEAM, FIRST_STATUS, BASELINE]
