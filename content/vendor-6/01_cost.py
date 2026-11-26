# Series 5 · On the Client's Floor · Vol. 6 · The Cost and the Ending · The cost (notes 1–4).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 6".
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 01 How Do We Notice Stress on a Vendor Team?
ts_problem = Doodle(760, 240, "Doodle of Hana's signs in January 2029: code commits at one in the morning, sharp with Lottie twice in a week, lunch at her desk every day, no weekend off since August, worked nineteen hours on wave 1 night, and every answer to how are you is fine. The stairwell, in December.",
                    "Commits at 01:00, sharp with Lottie, no weekend since August, and always “fine”.", exact=True)
for i, t in enumerate(["commits at 01:00", "sharp with Lottie ×2", "lunch at her desk", "no weekend since Aug", "19 h on wave 1 night", "“fine”"]):
    ts_problem.box(14 + (i % 3) * 250, 20 + (i // 3) * 80, 232, 64, t, "pink" if i == 5 else "y", size=17)
ts_problem.note(380, 214, "each sign small; together, a person running out", "red", size=19)

ts_how = Doodle(760, 340, "What Ines did. Look at the quiet signs, not the words: hours, tone, silence, weekends. Ask directly, privately, with time: you've worked every weekend since August; I'm worried; how are you really? Listen without fixing. Then change the work, not just the mood: two weeks' leave now, then reduced hours, then rotating off Lodestar, agreed with Hana and with Elaine. And check on the rest of the team the same way.",
                "Watch the quiet signs, ask directly and privately, listen, then change the work.", exact=True)
for i, (h, sub, fill) in enumerate([("watch", "hours · tone · silence", "y"), ("ask", "directly, privately", "blue"), ("listen", "don't fix yet", "paper"), ("change the work", "leave · hours · rotation", "green")]):
    ts_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=13)
ts_how.box(14, 160, 732, 70, "Hana: 2 weeks' leave from 15 Jan · reduced hours · rotates off Lodestar 5 Feb", "green", size=16)
ts_how.note(380, 290, "and the same check-in for everyone else on the team", "pen", size=18)

TEAM_STRESS = dict(
    slug="team-stress", date=date(2029, 1, 10), meta=on_site(date(2029, 1, 10)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. noticing burnout on a vendor team",
    tldr="Vendor teams on fixed-price work hide stress well, because admitting it feels like letting the client down. Watch the <b>quiet signs</b>: hours, tone, silence, missed weekends, “fine”. <b>Ask directly and privately</b>, with time to listen. Then <b>change the work</b>, not just the mood: leave, hours, rotation. A team member who burns out on your account is your failure, not theirs.",
    chips=[("Family", "the cost"), ("Lives in", "private 1:1 notes · the rotation plan"), ("Pairs with", "protecting the team (vol. 5), rotating off")],
    problem_side="The Grid, January 2029",
    problem="""  <p class="lead"><b>Hana Sato</b> has been Lodestar's tech lead since the bid. She worked <b>nineteen hours</b> on wave 1 night. In December she cried in the stairwell and said she was fine. In January:</p>
  <ul>
    <li>Her code commits arrive at <b>01:00</b>, three nights a week.</li>
    <li>She's been <b>sharp with Lottie</b> twice in a week, which she has never been.</li>
    <li>She eats lunch at her desk every day and <b>hasn't had a weekend off since August</b>.</li>
    <li>Every “how are you?” gets <span class="hl-pink">“fine”</span>.</li>
  </ul>""",
    problem_figs=[ts_problem],
    sides=dict(client=("MetroVolt", "<p>MetroVolt sees Hana as Lodestar's best engineer: calm, brilliant, always available. Elaine has noticed she looks tired. Nobody at MetroVolt sees it as their place to say anything; Hana works for Wrenfield.</p>", "She's the one who always fixes it."),
                vendor=("Ines", "<p>Ines has known for weeks and done nothing beyond worry. Hana is named in the contract as key personnel, the phase 2 bid is in eight weeks, and Hana is the best engineer Wrenfield has. None of that matters more than Hana.</p>", "I've been treating her “fine” as an answer. It's a symptom.")),
    sides_after="Burnout isn't a personal weakness; it's what sustained overload does to anyone. On a vendor team it's usually the most committed person who goes first.",
    analogy_side="the warning lights on a long drive",
    analogy="""  <p>On a long drive, nobody wants to stop. The car keeps going while small warning lights come on: oil low, a tyre soft. A good driver doesn't wait for the engine to seize. She <b>pulls over</b>, checks, and changes something: oil, a tyre, a rest. Ignoring small lights is how a long journey ends at the side of the road.</p>""",
    map=[("Small warning lights", "01:00 commits, sharp words, no weekends"),
         ("“The car's fine”", "“I'm fine”"),
         ("Pulling over", "A private conversation"),
         ("Changing something", "Leave, reduced hours, rotation"),
         ("The engine seizing", "Burnout, illness, resignation")],
    how_side="watch, ask, listen, change the work",
    how="""  <p><b>Watch the quiet signs.</b> Ines looks at what's visible without prying: the timesheet strip (Hana's worked-to-booked ratio is 1.5 for five months), commit times, who she eats with, how she speaks to people.</p>
  <p><b>Ask directly, privately, with time.</b> On <b>Wednesday 10 January</b>, in a booked room, with an hour: <i>“You've worked every weekend since August, and I've let it happen. I'm worried about you. How are you, really?”</i></p>
  <p><b>Listen without fixing.</b> Hana talks for forty minutes. She isn't sleeping. She feels she's the only one who understands the back-feed and the MetroBus adapters. She's afraid of letting the team down before phase 2.</p>
  <p><b>Change the work, not just the mood.</b> They agree, with Hana leading: <b>two weeks' leave from 15 January</b>, phone off; then reduced hours for a week; then she <b>rotates off Lodestar on 5 February</b> (next note but two) to a smaller client in Leeds. Elaine agrees to the key-personnel change the same day. Hana asks one thing: to be asked, not told, about phase 2.</p>
  <p><b>Check on everyone else.</b> Ines has the same private conversation with each of the team that week. Oskar is tired but fine. Lottie says she's fine and means it. Callum admits he's not sleeping either.</p>""",
    how_figs=[ts_how],
    steps=[("Watch the quiet signs", "Hours, tone, silence, weekends."),
           ("Ask directly and privately", "With time; name what you've seen."),
           ("Listen without fixing", "Let them describe it."),
           ("Change the work", "Leave, hours, rotation; agreed with them."),
           ("Deal with the contract side", "Key personnel, client consent."),
           ("Check on everyone", "The quiet ones too.")],
    vocab=[("Burnout", "Exhaustion, cynicism and reduced effectiveness from prolonged work stress."),
           ("Presenteeism", "Working while unwell or exhausted, at reduced effectiveness."),
           ("Key-person risk", "Dependence on one person; it increases their load."),
           ("Worked-to-booked ratio", "Hours actually worked divided by hours booked."),
           ("Check-in", "A short private conversation about how someone is."),
           ("Duty of care", "An employer's responsibility for its people's health.")],
    code=dict(file="(private)", note="Ines's notes after the 1:1 · Wed 10 Jan 2029", src="""
1:1 · Hana · Wed 10 Jan 2029 · 14:00–15:10 · room 19C (private notes, not shared)

signs seen     worked/booked 1.5 since Aug · commits after midnight 3×/week ·
               no weekends since Aug · 19 h on wave 1 night · sharp with Lottie ×2
her words      not sleeping · "only I understand the back-feed" · afraid of letting us
               down before phase 2
agreed (Hana leading)
  15–26 Jan    leave, phone off (Tariq + Bilal cover; Ines on call for back-feed)
  29 Jan–2 Feb reduced hours, handover to Tariq
  5 Feb        rotates off Lodestar to a smaller Leeds client
  phase 2      she'll be asked, not told
contract       key personnel change: Elaine consented 10 Jan (§6.3)
next           same check-in with everyone this week
"""),
    contract=dict(side="the key-personnel clause, used kindly", doc="Lodestar SOW · §6.3", date="signed 30 June 2027", stamp="consent given",
                  clauses=[("6.3", "The Supplier shall not remove or replace Key Personnel without MetroVolt's prior written consent, not to be unreasonably withheld.", "Elaine consented within an hour. “Of course. Look after her.”"),
                           ("6.4", "Replacement Key Personnel shall have equivalent skills and a handover of at least five Working Days.", "Tariq: a week's handover, then Bilal and Ines behind him.")],
                  plain="key-personnel clauses can make overloaded people feel trapped. The clause allows replacement with consent; ask early, and most clients agree when wellbeing is the reason."),
    health=dict(now="a",
                g=("a healthy team", ["Regular check-ins anyway.", "Watch the ratios.", "Rotate before it's needed."]),
                a=("one person overloaded", ["Ask directly, change the work.", "Client consent for rotation.", "Check everyone."]),
                r=("several people exhausted", ["Stop and re-plan with the client.", "Time off, now.", "Escalate inside your firm for people."])),
    pressure=dict(level=5, title="someone you've let down", cost="eight weeks before a bid · your best engineer",
                  items=["Ines's hardest admission: she'd seen it for weeks. Say that to the person; it's part of the repair.", "The bid will cope without Hana. Hana wouldn't have coped without the change."]),
    baseline="Each line compares <b>accepting “fine” and pushing on to the bid</b> with <b>watching the signs, asking directly, listening and changing the work</b>.",
    ratings=[(3, 4, "Elaine sees a supplier that looks after its people."),
             (1, 4, "Hana rests; the team sees it's allowed."),
             (3, 3, "A replacement costs some overlap."),
             (3, 3, "Neutral."),
             (3, 3, "Knowledge moves to Tariq and Bilal."),
             (1, 4, "Key-person risk reduced before phase 2."),
             (3, 4, "Consent recorded."),
             (3, 3, "Weeks to change the work."),
             (3, 3, "Regular check-ins.")],
    pitfalls=[("Accepting “fine”", "The signs say otherwise.", "ask directly, with time."),
              ("Changing the mood, not the work", "Pizza doesn't fix overload.", "leave, hours, rotation."),
              ("Deciding for them", "They feel punished.", "agree it, with them leading."),
              ("Only checking on the obvious one", "Others hide it better.", "everyone."),
              ("Waiting for a quiet moment", "There isn't one.", "now.")],
    grimoire=[(8, "slow-hex-of-burnout", "The Slow Hex of Burnout", "is the same thing inside MetroVolt, a year later: Hugo in his car on 6 March 2030.")],
    use=["Long or fixed-price engagements.", "After peaks: bids, go-lives, incidents.", "When someone is always “fine”."],
    skip=["Never skip it."],
    related=["<b>How Do We Protect Our Team from the Client?</b> (vol. 5)", "<b>What About My Own 23:00 Notes?</b> (next note)", "<b>How Do We Rotate Someone Off an Account?</b> (this volume)", "<b>Who Gets Woken Up?</b> (Eli, vol. 1)"],
    quiz=[("Name three quiet signs Ines noticed.", "01:00 commits, being sharp with Lottie, no weekends since August (also lunch at her desk, “fine”)."),
          ("How did Ines start the conversation?", "Directly, privately, naming what she'd seen and her own part in it."),
          ("What changed in Hana's work?", "Two weeks' leave, reduced hours, then rotation off Lodestar on 5 February."),
          ("How did the contract allow it?", "Key personnel can be replaced with MetroVolt's consent (§6.3); Elaine consented the same day."),
          ("Why check on everyone?", "Others may be hiding it better; Callum was not sleeping either.")],
    quiz_sit=[("Graham says: “Can't Hana just push through until the bid is in?” What does Ines say?", "No: she's already past the point where pushing through is safe. The bid can be written without her; she can't be replaced if she burns out. Wellbeing first, and Elaine has already agreed.")],
    try_it="Pick one person on your team who's always “fine”. Look at what you can see: hours, weekends, tone. If you're worried, book an hour and ask directly. What could change in their work, not just their mood?",
    remember="“Fine” is <span class=\"hl\">not an answer</span>. Watch the quiet signs, ask directly, and <span class=\"hl\">change the work</span>.",
    late=dict(when="Wed 10 January 2029 · 21:45 · hotel near The Grid",
              lines=["Asked Hana properly. Forty minutes. She isn't sleeping. She thinks only she understands the back-feed. She's partly right, and that's my fault.",
                     "Two weeks' leave from Monday. Then Leeds. Elaine said “look after her” before I'd finished asking.",
                     "Callum isn't sleeping either. Neither, if I'm honest, am I. That's the next page."]),
    sources=["Christina Maslach and Michael Leiter, <i>The Burnout Challenge</i> (2022).",
             "UK Health and Safety Executive, <i>Management Standards for work-related stress</i>.",
             "World Health Organization, ICD-11: burn-out as an occupational phenomenon (2019)."],
)

# ------------------------------------------------------------------ 02 What About My Own 23:00 Notes?
ln_problem = Doodle(760, 240, "Doodle of Ines's notebook: about 400 late notes since February 2027. The times have crept later, from about 21:00 in 2027 to 23:30 in December 2028. Four nights a week in the hotel near The Grid for eighteen months. Her sister's birthday missed in November. She tells Hana to rest and doesn't.",
                    "Four hundred late notes. The times creep from 21:00 to 23:30.", exact=True)
ln_problem.line("M40 200 L700 60", color="red")
for x, y, t in [(40, 200, "Feb 2027 · 21:00"), (380, 130, "mid 2028 · 22:30"), (700, 60, "Dec 2028 · 23:30")]:
    ln_problem.circle(x, y, 6, "pink")
    ln_problem.note(x + (40 if x == 40 else 0), y + 28, t, "pen", size=16)
ln_problem.note(380, 226, "she tells Hana to rest. she doesn't.", "red", size=19)

ln_how = Doodle(760, 320, "What Ines changed for herself. Notice your own signs with the same honesty: the notebook times, the hotel nights, the missed birthday. Say them to someone: Callum and Graham, on 21 January. Set limits you'll keep, and make them visible: three hotel nights a week, not four; Fridays in Leeds; phone off at 21:00; the notebook closes at 22:00. Delegate: Callum leads the phase 2 commercial work; Bilal the data. The leader's pace is the team's ceiling.",
                "Notice your own signs, say them aloud, set visible limits, and delegate.", exact=True)
for i, (h, sub, fill) in enumerate([("notice", "times, nights, birthdays", "y"), ("say it", "to Callum and Graham", "blue"), ("limits", "visible, kept", "green"), ("delegate", "commercial, data", "paper")]):
    ln_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=13)
ln_how.box(14, 150, 732, 70, "3 hotel nights · Fridays in Leeds · phone off 21:00 · notebook closes 22:00", "green", size=16)
ln_how.note(380, 280, "the leader's pace is the team's ceiling", "red", size=18)

OWN_NIGHTS = dict(
    slug="own-late-nights", date=date(2029, 1, 21), meta=on_site(date(2029, 1, 21)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. the leader's own stress",
    tldr="A team's pace is set by its leader, whatever the leader says. If you work until midnight, your team learns that's the job. Notice <b>your own signs</b> with the same honesty you'd give anyone else, <b>say them out loud</b> to someone, set <b>limits you'll actually keep</b> and make them <b>visible</b>, and <b>delegate</b> what others can carry. You can't ask your team to rest while they watch you not resting.",
    chips=[("Family", "the cost"), ("Lives in", "this notebook (the late notes' times)"), ("Pairs with", "stress on a vendor team, sustainable pace")],
    problem_side="Leeds, Sunday 21 January 2029",
    problem="""  <p class="lead">On a Sunday in Leeds, Ines reads back through her own notebook. Since February 2027 she has written about <b>400 late notes</b>, the ones at the end of every note in this book.</p>
  <ul>
    <li>The times have crept: around <b>21:00</b> in early 2027, <b>22:30</b> by mid-2028, <b>23:30</b> in December.</li>
    <li>Eighteen months of <b>four hotel nights a week</b> near The Grid.</li>
    <li>She missed her sister's birthday in November for the hypercare review.</li>
    <li><span class="hl-pink">Eleven days ago she told Hana to rest.</span></li>
  </ul>""",
    problem_figs=[ln_problem],
    sides=dict(client=("Elaine", "<p>Elaine has noticed Ines's emails arriving at 23:00 and has started replying at 23:05. Neither of them asked for that. Clients copy the pace of the vendor's lead as surely as the vendor's team does.</p>", "If she's working at eleven, I'd better be too."),
                vendor=("Ines", "<p>Ines can see Hana's signs clearly and her own not at all, until she reads them back in her own handwriting. The team watches what she does, not what she says. Graham calls her “unstoppable” as a compliment.</p>", "I've been teaching the team that this is normal.")),
    sides_after="The most dangerous stress on a team is the leader's, because everyone copies it and nobody feels able to point it out.",
    analogy_side="the oxygen mask",
    analogy="""  <p>The safety card on a plane says: <b>put on your own oxygen mask before helping others</b>. Not because you matter more, but because if you pass out, you can't help anyone. A leader running on empty helps nobody for long, and teaches everyone that running on empty is the job.</p>""",
    map=[("Your own mask first", "Ines's own limits"),
         ("Passing out", "Burnout, mistakes, illness"),
         ("Helping others", "Leading the team and the bid"),
         ("Everyone watching the crew", "The team copying Ines's pace"),
         ("The safety card", "Saying it out loud to Callum and Graham")],
    how_side="notice, say it, set visible limits, delegate",
    how="""  <p><b>Notice, honestly.</b> Ines writes down her own signs as if they were Hana's: late-note times, hotel nights, the missed birthday, sleep. Worked-to-booked ratio: <b>1.4</b> for eighteen months.</p>
  <p><b>Say it aloud.</b> On Monday 22 January she tells Callum, then Graham: “I've been working at a pace I'd never accept for anyone on my team. I'm changing it, and I need your help to keep it changed.” Graham's reply, after a pause: “I've been calling that unstoppable. Sorry.”</p>
  <p><b>Set visible limits.</b> Three hotel nights a week, not four. <b>Fridays in Leeds</b>. Phone off at <b>21:00</b>, except severity 1. The notebook closes at <b>22:00</b>. She tells Elaine, who laughs and stops replying at 23:05.</p>
  <p><b>Delegate.</b> Callum leads the phase 2 commercial work; Bilal leads the data estimates; Lottie runs the joint lessons session. Ines keeps the architecture and the client.</p>
  <p>The late notes in the rest of this volume are written before 22:00. Mostly.</p>""",
    how_figs=[ln_how],
    steps=[("Read your own signs as if they were someone else's", "Times, nights, missed things."),
           ("Say them to someone who'll hold you to it", "Your deputy and your boss."),
           ("Set limits you can keep", "Specific: nights, times, days."),
           ("Make them visible", "Tell the client and the team."),
           ("Delegate real work", "Not just tasks: decisions."),
           ("Check back in a month", "Did the limits hold?")],
    vocab=[("Role modelling", "Others copy what leaders do more than what they say."),
           ("Self-awareness", "Noticing your own state and its effect on others."),
           ("Boundary", "A limit you set on your own availability."),
           ("Delegation", "Giving others real responsibility and decisions."),
           ("Sustainable leadership", "Leading at a pace you could keep for years."),
           ("Overwork culture", "A team norm that long hours equal commitment.")],
    code=dict(file="notebook/inside-cover.md", note="Ines's notebook · Sun 21 Jan 2029", src="""
INSIDE COVER · my own signs, written as if they were Hana's

late notes      ≈ 400 since Feb 2027 · median time: 21:10 (2027) → 23:30 (Dec 2028)
hotel           4 nights/week for 18 months
missed          sister's birthday (21 Nov 2028) · 3 weekends in Dec
worked/booked   1.4 for 18 months

limits (from 22 Jan, told to Callum, Graham, Elaine, the team)
  3 hotel nights a week · Fridays in Leeds · phone off 21:00 (sev 1 only)
  notebook closes at 22:00
delegated       Callum: phase 2 commercial · Bilal: data estimates · Lottie: lessons session
check           Fri 23 Feb: did they hold?
"""),
    contract=dict(side="what the contract didn't require", doc="Lodestar SOW · Schedule 9 and Wrenfield working-time policy", date="Jan 2029", stamp="never required",
                  clauses=[("Sch. 9, 4.1", "During warranty, the Supplier shall respond to Severity 1 defects within 1 hour …", "severity 1 only. nothing about 23:00 emails on a Tuesday."),
                           ("Wrenfield policy 3.2", "Staff should not regularly work more than 48 hours a week, averaged over 17 weeks.", "the UK limit. I'd been over it, on average, for 18 months.")],
                  plain="very little of a lead's overwork is required by the contract. It's habit, fear and example. Check what's actually promised; most of the rest can stop."),
    health=dict(now="a",
                g=("a sustainable lead", ["Keep the limits.", "Visible to the team.", "Check yearly."]),
                a=("a lead running hot", ["Notice, say it, set limits.", "Delegate decisions.", "Tell the client."]),
                r=("a lead near burnout", ["Step back now, with help.", "Your firm must cover.", "See a doctor."])),
    pressure=dict(level=4, title="yourself", cost="eighteen months of habit · an admission to your boss",
                  items=["Writing your own signs down feels self-indulgent. It's the most useful thing in this notebook.", "If you can't change your pace for yourself, change it for your team: they're copying you."]),
    baseline="Each line compares <b>leading at 23:30 and telling others to rest</b> with <b>noticing, saying it, visible limits and real delegation</b>.",
    ratings=[(3, 4, "Elaine stops replying at 23:05."),
             (1, 4, "The team sees rest is allowed."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Fewer tired decisions."),
             (2, 4, "Callum and Bilal carry real decisions."),
             (3, 3, "Neutral."),
             (3, 3, "A month to settle."),
             (3, 4, "Fewer hours, same outcomes.")],
    pitfalls=[("Seeing others' signs, not your own", "You're the last to know.", "write yours down as if they were theirs."),
              ("Private limits", "Nobody helps you keep them.", "tell the team and the client."),
              ("Delegating tasks, not decisions", "You're still the bottleneck.", "hand over decisions."),
              ("Calling overwork commitment", "Everyone copies it.", "call it what it is."),
              ("Waiting for the project to end", "It doesn't end; the next one starts.", "change now.")],
    grimoire=[(8, "salt-circle", "The Salt Circle", "is the same lesson inside MetroVolt: setting boundaries that hold."), (8, "slow-hex-of-burnout", "The Slow Hex of Burnout", "describes where the 23:30 notes were heading.")],
    use=["You're telling others to rest and not resting.", "Your working hours have crept.", "Your team copies your pace."],
    skip=["Never skip it."],
    related=["<b>How Do We Notice Stress on a Vendor Team?</b> (previous note)", "<b>Can a Fixed-Price Team Keep a Sustainable Pace?</b> (next note)", "<b>How Do We Manage Up in Our Own Firm?</b> (vol. 5)", "<b>Growing as a Product Owner</b> (Grace, vol. 6)"],
    quiz=[("What did the late-note times show?", "They crept from about 21:00 in 2027 to 23:30 in December 2028."),
          ("Why does a leader's pace matter so much?", "The team, and even the client, copy it."),
          ("What limits did Ines set?", "Three hotel nights, Fridays in Leeds, phone off at 21:00, notebook closed at 22:00."),
          ("What did she delegate?", "Phase 2 commercial work to Callum, data estimates to Bilal, the lessons session to Lottie."),
          ("Who did she tell, and why?", "Callum, Graham, Elaine and the team, so they'd help keep the limits.")],
    quiz_sit=[("Two weeks later, a severity 3 defect arrives at 21:30 and Ines feels the urge to look. What does she do?", "Leave it: severity 3 waits for morning under the warranty terms. Phone off. The limit only works if it holds when it's tempting.")],
    try_it="Look back at your own last month: when did you stop working each day? How many weekends? Write your signs as if they were a colleague's. Pick one limit, tell two people, and keep it for a month.",
    remember="Put your own mask on first. <span class=\"hl\">Your pace is your team's ceiling</span>.",
    late=dict(when="Sun 21 January 2029 · 21:50 · Leeds",
              lines=["Read my own notebook. 21:00 became 23:30. I told Hana to rest eleven days ago.",
                     "Tomorrow I tell Callum and Graham. Then Elaine. Then the team.",
                     "This note is at 21:50. That's the first time in a year. I'll try to keep it there."]),
    sources=["Christina Maslach and Michael Leiter, <i>The Burnout Challenge</i> (2022).",
             "Brené Brown, <i>Dare to Lead</i> (2018).",
             "UK Government, the Working Time Regulations 1998 (the 48-hour average)."],
)

# ------------------------------------------------------------------ 03 Can a Fixed-Price Team Keep a Sustainable Pace?
sp_problem = Doodle(760, 240, "Doodle of eighteen months of Wrenfield's Lodestar timesheets. Booked: 7.5 hours a day. Worked: an average of 9.1, peaks of 13 in bid week and cutover week. About 2,900 unpaid overtime hours across the team, roughly 390 working days, nearly two people for a year, given away inside the fixed price.",
                    "Booked 7.5 a day, worked 9.1. About 2,900 unpaid hours, inside the fixed price.", exact=True)
sp_problem.line("M40 190 H720", thin=True)
sp_problem.line("M40 150 H720", dash=True)
sp_problem.note(700, 140, "booked 7.5", "pen", size=15)
sp_problem.line("M40 120 L120 60 L200 110 L330 100 L420 70 L520 40 L600 100 L720 105", color="red")
sp_problem.note(110, 50, "bid", "red", size=15)
sp_problem.note(520, 30, "cutover", "red", size=15)
sp_problem.note(380, 226, "≈ 2,900 hours ≈ 390 days ≈ two people for a year", "red", size=18)

sp_how = Doodle(760, 330, "Wrenfield's pace policy, agreed in February 2029 and written into the phase 2 bid. Measure it: worked versus booked, every week, per person, on the status. Cap it: no more than 45 hours a week except planned peaks. Repay it: time off in lieu within a month. Recover after peaks: a light week after every bid, rehearsal or cutover. And plan for it: phase 2 velocity at 85 per cent of the team's capacity, not 100.",
                "Measure, cap, repay, recover, and plan at 85 % so the plan doesn't need heroes.", exact=True)
for i, (h, sub, fill) in enumerate([("measure", "worked vs booked", "y"), ("cap", "45 h/week", "pink"), ("repay", "TOIL in a month", "green"), ("recover", "light week after peaks", "blue"), ("plan", "at 85 %", "paper")]):
    sp_how.box(14 + i * 148, 20, 138, 100, h, fill, sub=sub, size=18, subsize=12)
sp_how.box(14, 150, 732, 70, "in the phase 2 bid: team plan at 85 % capacity · named recovery weeks", "green", size=17)
sp_how.note(380, 280, "a plan that needs heroes is a plan that's wrong", "red", size=18)

SUSTAINABLE_PACE = dict(
    slug="sustainable-pace", date=date(2029, 2, 2), meta=on_site(date(2029, 2, 2)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. sustainable pace on fixed-price work",
    tldr="On a fixed price, unpaid overtime is invisible: it doesn't appear on invoices, only in people. <b>Measure</b> it (worked versus booked, per person, weekly), <b>cap</b> it, <b>repay</b> it with time off, plan <b>recovery</b> after peaks, and <b>plan the work at less than full capacity</b>, so the plan doesn't need heroes. Then put the pace in the next bid, where the client can see it.",
    chips=[("Family", "the cost"), ("Lives in", "Wrenfield pace policy v1 · phase 2 bid §5.4"), ("Pairs with", "estimating in fog (vol. 1), re-planning (vol. 4)")],
    problem_side="Wrenfield, Leeds, 2 February 2029",
    problem="""  <p class="lead">Callum adds up eighteen months of Lodestar timesheets, the strip at the top of the early notes. <b>Booked</b>: 7.5 hours a day. <b>Worked</b>: an average of <b>9.1</b>, with peaks of 12–13 in bid week, rehearsal weekends and cutover.</p>
  <ul>
    <li>About <b>2,900 hours</b> of unpaid overtime across the team: roughly <b>390 working days</b>, nearly two people for a year.</li>
    <li>That's the real reason the margin held at 10 %: <span class="hl-pink">the team paid for it.</span></li>
    <li>Phase 2 is three times bigger.</li>
  </ul>""",
    problem_figs=[sp_problem],
    sides=dict(client=("MetroVolt", "<p>MetroVolt got a fixed price and a team that always delivered. It never saw the overtime and never asked for it. It also doesn't want phase 2's team to burn out halfway through wave 3.</p>", "We pay for the result. We'd rather the team lasted."),
                vendor=("Ines and Callum", "<p>Wrenfield's margin was partly built on people's evenings. For phase 2 (three waves, about 30 months) that can't continue: Hana has already rotated off, and others would follow. Pace has to be measured and planned, not hoped for.</p>", "We priced the work. We didn't price the people.")),
    sides_after="Overtime on a fixed price is a hidden discount the team gives the client, and the vendor gives itself credit for.",
    analogy_side="the marathon and the sprint",
    analogy="""  <p>Nobody runs a marathon at sprint pace. Runners <b>plan a pace they can hold</b>, check their watch every mile, and save effort for the hills. A runner who sprints the first ten miles because she feels good is the one walking at mile twenty. A long project is a marathon with a few hills in it.</p>""",
    map=[("Marathon pace", "Planning at 85 % capacity"),
         ("Checking the watch every mile", "Worked vs booked, weekly"),
         ("Saving effort for the hills", "Planned peaks: bids, cutovers"),
         ("Walking at mile twenty", "Burnout in wave 3"),
         ("Sprinting while feeling good", "18 months at 9.1 hours a day")],
    how_side="measure, cap, repay, recover, plan at 85 %",
    how="""  <p>Ines, Callum and Graham agree a <b>pace policy</b> in February, for all Wrenfield accounts:</p>
  <ul>
    <li><b>Measure</b>: worked versus booked, per person, weekly, on the internal status beside the margin. A ratio above 1.15 for three weeks triggers a conversation.</li>
    <li><b>Cap</b>: no more than <b>45 hours</b> a week except planned peaks agreed in advance.</li>
    <li><b>Repay</b>: time off in lieu, taken within a month.</li>
    <li><b>Recover</b>: a light week after every bid, rehearsal weekend or cutover, in the plan.</li>
    <li><b>Plan at 85 %</b>: phase 2's estimates assume the team delivers 85 % of its theoretical capacity, using wave 1's real velocity (38 points).</li>
  </ul>
  <p>Graham's worry: it makes the phase 2 price higher. By about 6 %. Ines's answer: the alternative is hiding 6 % in people's evenings, and losing them by wave 3. The phase 2 bid says so in §5.4, in plain words. Desmond later tells Elaine it was the only bid that mentioned the team's wellbeing.</p>""",
    how_figs=[sp_how],
    steps=[("Measure worked vs booked", "Per person, weekly, beside the margin."),
           ("Cap weekly hours", "With planned exceptions only."),
           ("Repay overtime", "Time off within a month."),
           ("Plan recovery after peaks", "In the schedule, not as a favour."),
           ("Plan at less than full capacity", "So the plan doesn't need heroes."),
           ("Price it honestly", "And say so in the bid.")],
    vocab=[("Sustainable pace", "A pace a team can keep indefinitely without harm."),
           ("Time off in lieu (TOIL)", "Paid time off given back for extra hours worked."),
           ("Capacity", "How much work a team can do in a period."),
           ("Planned peak", "An agreed period of extra effort, with recovery after."),
           ("Hidden discount", "Unpaid overtime that lowers the real cost of a fixed price."),
           ("Heroics", "Relying on individuals' extraordinary effort to hit a plan.")],
    code=dict(file="wrenfield/pace-policy-v1.md", note="agreed Fri 2 Feb 2029 · Ines, Callum, Graham", src="""
WRENFIELD PACE POLICY v1 (all accounts)

measure   worked ÷ booked, per person, weekly, on the internal status
          > 1.15 for 3 weeks → a conversation; > 1.3 → a change to the work
cap       45 h/week, except planned peaks agreed in advance
repay     time off in lieu within one month
recover   a light week after every bid, rehearsal weekend or cutover (in the plan)
plan      estimates at 85 % of team capacity (wave 1 velocity: 38 points)
Lodestar  18 months: average 9.1 h/day worked vs 7.5 booked ·
          ≈ 2,900 unpaid hours (≈ 390 days)
phase 2   price effect ≈ +6 % · stated in bid §5.4
"""),
    contract=dict(side="what the next bid says about pace", doc="Phase 2 bid · §5.4 (team and pace)", date="submitted 4 Apr 2029", stamp="priced in",
                  clauses=[("5.4", "Our plan assumes the team works at a sustainable pace: estimates use 85 % of capacity, with recovery after each wave's cutover. We have priced this in rather than relying on unplanned overtime.", "the first time we've written this in a bid."),
                           ("Lodestar SOW, 6.1", "The Supplier shall provide the Key Personnel … for the duration of Wave 1.", "a team that burns out can't keep this promise. pace protects it.")],
                  plain="saying in a bid that your plan assumes a sustainable pace is unusual, and honest. It explains part of your price and protects the key-personnel promises you're making."),
    health=dict(now="a",
                g=("a healthy pace already", ["Keep measuring.", "Recovery after peaks.", "Plan at 85 %."]),
                a=("hidden overtime discovered", ["Measure, cap, repay.", "Re-plan at real velocity.", "Price the next phase honestly."]),
                r=("the plan depends on heroics", ["Re-baseline with the client.", "Add people early or cut scope.", "Never ask for more evenings."])),
    pressure=dict(level=3, title="the hidden discount", cost="≈ 6 % on the next price · 2,900 hours you can't give back",
                  items=["Seeing 2,900 hours in one number is uncomfortable for everyone who signed off the timesheets. Use it to change the next plan, not to blame.", "A higher, honest price may lose the bid. A lower price built on evenings would lose the team."]),
    baseline="Each line compares <b>a fixed price quietly subsidised by overtime</b> with <b>measured hours, caps, repayment, recovery and planning at 85 %</b>.",
    ratings=[(3, 4, "MetroVolt sees a team that will last 30 months."),
             (1, 5, "Hours capped and repaid."),
             (3, 2, "≈ 6 % less competitive on price."),
             (3, 3, "Neutral."),
             (3, 4, "Rested people make fewer mistakes."),
             (2, 4, "Burnout risk in phase 2 reduced."),
             (3, 4, "Policy written and in the bid."),
             (3, 3, "A month to set up."),
             (3, 3, "A weekly measure.")],
    pitfalls=[("Not measuring", "Overtime is invisible on a fixed price.", "worked vs booked, weekly."),
              ("Celebrating long hours", "Everyone copies them.", "a cap, and recovery."),
              ("Planning at 100 %", "Every surprise becomes an evening.", "plan at 85 %."),
              ("Hiding the cost", "The price looks better than it is.", "price it, say so."),
              ("Unrepaid overtime", "Resentment and exits.", "time off within a month.")],
    grimoire=[(7, "performative-busyness", "The Performative Busy-ness Dance", "is the culture that makes long hours look like commitment.")],
    use=["Fixed-price or long engagements.", "Before pricing the next phase.", "When the margin looks better than it should."],
    skip=["Never skip measuring."],
    related=["<b>How Long Will It Really Take?</b> (vol. 1)", "<b>How Do We Re-plan Without Lying?</b> (vol. 4)", "<b>How Do We Notice Stress on a Vendor Team?</b> (this volume)", "<b>Why Am I Always Busy?</b> (Eli, vol. 1)"],
    quiz=[("How much unpaid overtime did Lodestar absorb?", "About 2,900 hours, roughly 390 working days."),
          ("What are the five parts of the pace policy?", "Measure, cap, repay, recover, plan at 85 %."),
          ("What ratio triggers a conversation?", "Worked ÷ booked above 1.15 for three weeks."),
          ("What did it cost on the phase 2 price?", "About 6 %."),
          ("Why put it in the bid?", "It explains the price and protects the key-personnel promises.")],
    quiz_sit=[("Graham asks to plan phase 2 at 100 % “and handle overruns as they come”. What does Ines answer?", "That's how Lodestar got 2,900 unpaid hours and lost Hana. At 100 %, every surprise becomes someone's evening. 85 % is the honest plan; if the price is too high, cut scope or add time, not people's evenings.")],
    try_it="Add up last month's hours worked versus booked for your team. What's the ratio? If you planned next month at 85 % of capacity, what would move?",
    remember="Overtime on a fixed price is <span class=\"hl\">a hidden discount paid by people</span>. Measure it, cap it, and <span class=\"hl\">plan at 85 %</span>.",
    late=dict(when="Fri 2 February 2029 · 20:30 · Leeds",
              lines=["2,900 hours. Two people for a year. Inside a fixed price. We called it margin.",
                     "Graham went quiet, then signed the pace policy. +6 % on phase 2. He said it's the right +6 %.",
                     "Friday in Leeds. 20:30. The limits are holding. Mostly."]),
    sources=["Kent Beck, <i>Extreme Programming Explained</i> (2nd ed., 2004): sustainable pace.",
             "Tom DeMarco, <i>Slack</i> (2001).",
             "Tom DeMarco and Timothy Lister, <i>Peopleware</i> (3rd ed., 2013)."],
)

# ------------------------------------------------------------------ 04 How Do We Rotate Someone Off an Account?
ro_problem = Doodle(760, 240, "Doodle of Hana's rotation off Lodestar, planned for 5 February 2029. She's named key personnel in the contract. She holds most of the knowledge of the back-feed and the MetroBus adapters. Phase 2 bids are due in April. Vivian worries the client will think Wrenfield is losing its best people.",
                    "Key personnel, most of the back-feed in her head, and a bid in eight weeks.", exact=True)
ro_problem.box(250, 30, 260, 110, "Hana", "y", sub="key personnel · back-feed · MetroBus", size=24, subsize=14)
ro_problem.box(14, 170, 360, 50, "contract: client consent", "paper", size=17)
ro_problem.box(386, 170, 360, 50, "Vivian: “they'll think we're leaving”", "pink", size=16)

ro_how = Doodle(760, 330, "The rotation plan. Agree it with the person first: Hana leads. Agree it with the client: Elaine's consent under the key personnel clause, given on 10 January. Hand over properly: Tariq Rahman shadows Hana for a week, then Hana shadows Tariq; Bert's-book-style pages for the back-feed. Tell the client and the team honestly: Hana is rotating to rest and grow, not leaving. Keep the door open: Hana's return to phase 2 is her decision, later.",
                "With the person, with the client, a real handover, an honest story, and an open door.", exact=True)
for i, (h, sub, fill) in enumerate([("with Hana", "she leads", "green"), ("with Elaine", "consent, §6.3", "y"), ("handover", "shadow, reverse-shadow", "blue"), ("honest story", "to rest and grow", "paper"), ("open door", "her decision", "green")]):
    ro_how.box(14 + i * 148, 20, 138, 100, h, fill, sub=sub, size=17, subsize=12)
ro_how.box(14, 150, 732, 70, "Tariq Rahman (he/him), senior engineer, Leeds · 29 Jan–2 Feb overlap · 14 handover pages", "paper", size=16)
ro_how.note(380, 280, "rotate people before they break, not after", "red", size=18)

ROTATING_OFF = dict(
    slug="rotating-off", date=date(2029, 2, 5), meta=on_site(date(2029, 2, 5)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. rotating people on long accounts",
    tldr="Long accounts wear people out, and the most important people wear out first. Rotate them <b>before they break</b>: agree it <b>with them</b> first, <b>with the client</b> (especially if they're named in the contract), plan a <b>real handover</b> with overlap, tell the story <b>honestly</b> (“to rest and grow”, not “leaving”), and keep the <b>door open</b> for their return. A planned rotation is a sign of a healthy supplier, not a weak one.",
    chips=[("Family", "the cost"), ("Lives in", "delivery/lodestar/rotation-hana.md"), ("Pairs with", "stress on a vendor team, knowledge transfer")],
    problem_side="The Grid, 5 February 2029",
    problem="""  <p class="lead">After two weeks' leave and a week of reduced hours, <b>Hana rotates off Lodestar on Monday 5 February</b> to a smaller client in Leeds.</p>
  <ul>
    <li>She's named <b>key personnel</b> in the contract (§6.1).</li>
    <li>She holds most of the knowledge of the <b>back-feed</b> and the <b>MetroBus adapters</b>.</li>
    <li>Vivian worries: <span class="hl-pink">“MetroVolt will think we're losing our best people before phase 2.”</span></li>
  </ul>""",
    problem_figs=[ro_problem],
    sides=dict(client=("Elaine and Hollis", "<p>MetroVolt's worry is continuity: who knows the back-feed now? Elaine also cares about Hana, and is relieved to see a supplier rotate someone before a crisis rather than after. What would worry her is a silent disappearance.</p>", "Who knows it now, and is she all right?"),
                vendor=("Ines", "<p>Ines has to protect three things: Hana's recovery, Lodestar's knowledge and MetroVolt's confidence before phase 2. The rotation has to be visible, planned and honest, with the knowledge moved, not just the person.</p>", "Move the person, keep the knowledge, tell the truth.")),
    sides_after="Clients worry about rotations they hear about late. A rotation explained early, with a handover they can see, increases confidence.",
    analogy_side="the relay runner's handover",
    analogy="""  <p>In a relay, the incoming runner doesn't stop and hand the baton to someone standing still. Both <b>run together through the exchange zone</b>, matching pace, until the new runner has it firmly. Then the first runner slows down and steps off the track, and nobody watching thinks she's quitting.</p>""",
    map=[("Running together through the zone", "A week of shadowing, then reverse-shadowing"),
         ("The baton firmly held", "Tariq running the back-feed alone, checked"),
         ("Stepping off the track", "Hana to a smaller Leeds client"),
         ("Nobody thinks she's quitting", "An honest story: to rest and grow"),
         ("The next leg", "Hana's return to phase 2, her decision")],
    how_side="with the person, with the client, a handover, honesty, an open door",
    how="""  <p><b>With Hana, first.</b> The rotation was her choice in the 10 January conversation; she chose the Leeds client and the timing.</p>
  <p><b>With the client.</b> Elaine consented under §6.3 on 10 January. Ines briefs Hollis and Rupert's office in person, before the team hears it from anyone else.</p>
  <p><b>A real handover.</b> <b>Tariq Rahman</b>, a senior Wrenfield engineer from Leeds, overlaps for a week (29 January to 2 February). Tariq shadows Hana for two days; Hana shadows Tariq for three. Hana writes <b>14 handover pages</b> in the style of Bert's book: the back-feed, the MetroBus adapters, the queue limit from wave 1 night, and “things I'd do differently”. Bilal becomes Tariq's backup.</p>
  <p><b>An honest story.</b> To MetroVolt and the team: <i>“Hana is rotating to a smaller client to rest and to lead something of her own. Tariq is taking over, with a week's overlap, and Bilal behind him.”</i> No euphemisms, no medical details.</p>
  <p><b>An open door.</b> Hana's role in phase 2 is her decision, later. The phase 2 bid will say so honestly (next notes). Elaine sends Hana a card. Bert sends her his last copybook printout, framed.</p>""",
    how_figs=[ro_how],
    steps=[("Let the person lead the decision", "Timing, destination."),
           ("Get the client's consent early", "Especially for key personnel."),
           ("Overlap, both directions", "Shadow, then reverse-shadow."),
           ("Write it down", "Pages in the team's handover style."),
           ("Tell an honest story, early", "Client first, then the team."),
           ("Keep the door open", "Their return is their choice.")],
    vocab=[("Rotation", "Moving someone off an account on purpose, with a plan."),
           ("Key personnel", "People named in the contract who can't be swapped without consent."),
           ("Shadowing", "The new person watches the old one work."),
           ("Reverse shadowing", "The old person watches the new one work."),
           ("Handover pages", "Written knowledge for the successor."),
           ("Continuity", "Keeping the work running across people changes.")],
    code=dict(file="delivery/lodestar/rotation-hana.md", note="agreed Wed 10 Jan · rotation Mon 5 Feb 2029", src="""
ROTATION · Hana Sato → Tariq Rahman

decided by     Hana (10 Jan) · client consent: Elaine, §6.3 (10 Jan)
told           Hollis + Rupert's office in person (11 Jan) · team (12 Jan)
story          "rotating to a smaller client to rest and lead something of her own"
overlap        29 Jan–2 Feb: Tariq shadows (2 days) · Hana shadows Tariq (3 days)
pages          14: back-feed · MetroBus adapters · queue limits (wave 1 night) ·
               contract tests · "things I'd do differently"
backup         Bilal Khan
phase 2        Hana's role: her decision, later; the bid will say so
"""),
    contract=dict(side="key personnel, changed properly", doc="Lodestar SOW · §6.3–6.4 · variation V-05", date="5 Feb 2029", stamp="replaced",
                  clauses=[("6.3", "The Supplier shall not remove or replace Key Personnel without MetroVolt's prior written consent, not to be unreasonably withheld.", "consent given before anyone else knew."),
                           ("V-05", "Schedule 6 is amended: Technical Lead, Tariq Rahman, from 5 February 2029.", "Hana's name leaves the schedule. Not the story.")],
                  plain="replacing a named key person is a contract change. Ask early, give the client a credible successor and a handover they can see, and record it as a variation."),
    health=dict(now="g",
                g=("planned rotation", ["Overlap and pages.", "Honest story.", "Client consent early."]),
                a=("a rotation for wellbeing", ["The person leads.", "No medical details.", "Extra backup for the successor."]),
                r=("a sudden departure", ["Tell the client the same day.", "Emergency handover from documents.", "Bring in senior cover fast."])),
    pressure=dict(level=3, title="letting your best person go", cost="two months before a bid · Vivian's worry",
                  items=["Rotating your best engineer before a bid feels reckless. Keeping her until she breaks would be.", "Vivian's worry was the wrong way round: MetroVolt's confidence went up."]),
    baseline="Each line compares <b>keeping Hana on until the bid</b> with <b>a rotation she led, client consent, a two-way handover and an honest story</b>.",
    ratings=[(3, 4, "Elaine's confidence went up, not down."),
             (1, 4, "Hana recovers; the team sees rotation is normal."),
             (3, 3, "A week's overlap."),
             (3, 3, "Neutral."),
             (3, 4, "Knowledge written down, not only in a head."),
             (2, 4, "Key-person risk spread to Tariq and Bilal."),
             (3, 5, "Variation V-05 recorded."),
             (3, 3, "Three weeks of planning."),
             (3, 3, "Pages to keep current.")],
    pitfalls=[("Rotating too late", "After the breakdown.", "before they break."),
              ("Deciding for them", "It feels like punishment.", "they lead."),
              ("No overlap", "Knowledge leaves with the person.", "shadow both ways."),
              ("Euphemisms", "Rumours fill the gap.", "an honest story, without private details."),
              ("Closing the door", "You lose them for good.", "their return is their choice.")],
    grimoire=[(3, "escape-portal", "The Escape Portal", "is the same move, inside MetroVolt: leaving a situation before it breaks you, and leaving well.")],
    use=["Long engagements.", "Key people showing signs of strain.", "Before a new phase, if someone needs a change."],
    skip=["Short engagements where nobody's overloaded."],
    related=["<b>How Do We Notice Stress on a Vendor Team?</b> (this volume)", "<b>How Do We Hand It Over So It Sticks?</b> (next note)", "<b>Who Knows How It Really Works?</b> (vol. 3)", "<b>Can Someone Else Run This?</b> (Sanne, vol. 6)"],
    quiz=[("Who led the decision to rotate Hana?", "Hana."),
          ("What did the contract require?", "MetroVolt's prior written consent for replacing key personnel."),
          ("How long was the overlap, and how did it work?", "A week: Tariq shadowed Hana, then Hana shadowed Tariq."),
          ("What was the story told?", "Hana is rotating to a smaller client to rest and lead something of her own."),
          ("Who decides Hana's role in phase 2?", "Hana, later.")],
    quiz_sit=[("Rupert's office asks whether Hana “couldn't stay until the phase 2 bid is in”. What does Ines say?", "No: the rotation is planned and agreed, Tariq has taken over with a full handover, and the bid will be stronger with a rested team. Offer Tariq for any technical questions.")],
    try_it="Who on your team has been on the same account longest? Ask them, privately, whether they'd like a change. If yes, sketch the rotation: overlap, pages, story, timing.",
    remember="Rotate people <span class=\"hl\">before they break</span>. Move the knowledge, tell the truth, <span class=\"hl\">keep the door open</span>.",
    late=dict(when="Mon 5 February 2029 · 21:00 · hotel near The Grid",
              lines=["Hana's desk is Tariq's now. Fourteen pages in her handwriting, including “things I'd do differently”. Number one: “ask for help sooner”.",
                     "Bert framed his last copybook printout for her. She laughed for the first time in months.",
                     "21:00. The limits hold. One fewer hotel night this week."]),
    sources=["Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019): cognitive load.",
             "UK Health and Safety Executive, <i>Management Standards</i>.",
             "Michael Watkins, <i>The First 90 Days</i> (2003): transitions, for the successor."],
)

NOTES = [TEAM_STRESS, OWN_NIGHTS, SUSTAINABLE_PACE, ROTATING_OFF]
