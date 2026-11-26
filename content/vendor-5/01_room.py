# Series 5 · On the Client's Floor · Vol. 5 · Other People's Politics · Reading the room (notes 1–4).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 5".
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 01 How Do We Read the Client's Politics from Outside?
rp_problem = Doodle(760, 240, "Doodle of small signals on floor 19 in October 2028: a new meeting series called Ascend readiness that Priya isn't invited to; Gareth's team moving to floor 20, next to Rupert; a budget paper that mentions customer data under Network Assets; Vexmoor's people in the lift with Rupert's badge colour. None of them is news. Together they are a story.",
                    "None of these is news. Together, they're a story.", exact=True)
for i, t in enumerate(["“Ascend readiness” · no Priya", "Gareth's team → floor 20", "budget paper: “customer data · Network Assets”", "Vexmoor in Rupert's lift"]):
    rp_problem.box(14 + (i % 2) * 372, 20 + (i // 2) * 80, 360, 64, t, "y", size=16)
rp_problem.note(380, 210, "dots, not yet a line", "red", size=20)

rp_how = Doodle(760, 330, "Ines's monthly reading of MetroVolt's politics. Collect signals: meeting series, invitations, seating, budget papers, announcements, who waits for whom. Write each as a fact, without interpretation. Once a month, update the power map from the facts. Ask one question: what does this change for Lodestar? Act only on that: who to brief, what to put in writing. And three things never to do: repeat, take sides, or trade on it.",
                "Collect facts, update the map monthly, ask what it changes for Lodestar, act only on that.", exact=True)
for i, (h, sub, fill) in enumerate([("collect", "facts, not guesses", "y"), ("map", "monthly update", "blue"), ("ask", "what changes for us?", "green"), ("act", "brief, write down", "paper")]):
    rp_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=20, subsize=14)
    if i:
        rp_how.arrow(14 + i * 186 - 10, 70, 14 + i * 186 - 2, 70)
rp_how.box(14, 150, 732, 70, "never", "pink", sub="repeat it · take sides · trade on it", size=20, subsize=16)
rp_how.note(380, 280, "October's answer: brief Rupert's office directly, before Priya has to", "pen", size=17)

READING_POLITICS = dict(
    slug="reading-client-politics", date=date(2028, 10, 10), meta=on_site(date(2028, 10, 10)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. political awareness for suppliers",
    tldr="From the vendor's desk you see the client's politics in small signals: who's invited, who moves floors, what budget papers say, who waits for whom. <b>Collect them as facts</b>, update your <b>power map monthly</b>, and ask only one question: <b>what does this change for our project?</b> Then act on that, by briefing the right people and writing things down. Never repeat what you see, never take sides, never trade on it.",
    chips=[("Family", "reading the room"), ("Lives in", "Ines's notebook: “signals” pages"), ("Pairs with", "mapping the client (vol. 2), the sponsor moves on")],
    problem_side="The Grid, October 2028",
    problem="""  <p class="lead">Three weeks after wave 1, hypercare is going well: the exception queue is down to 140 accounts. But floor 19 has started to feel different.</p>
  <ul>
    <li>A new weekly meeting, <b>“Ascend readiness”</b>, chaired by Rupert. Priya isn't on the invitation. Elaine is.</li>
    <li><b>Gareth's</b> Network Assets team moves to floor 20, next to Rupert's office.</li>
    <li>A Horizon budget paper Elaine shares for another reason mentions “customer data services (Network Assets)”.</li>
    <li><span class="hl-pink">None of it is announced. All of it could matter to phase 2.</span></li>
  </ul>""",
    problem_figs=[rp_problem],
    sides=dict(client=("MetroVolt", "<p>Inside MetroVolt, people know far more than they say. Rupert is preparing the next phase of transformation; Gareth sees an opportunity; Priya is defending her area. Nobody will tell a supplier, and nobody should have to.</p>", "Not your business. Yet."),
                vendor=("Ines", "<p>Wrenfield isn't part of MetroVolt's politics, but its next contract depends on them. Ines needs to notice changes early enough to brief the right people and protect what's been agreed, without ever looking like she's playing a game she has no right to play.</p>", "I can't change it. I mustn't be surprised by it.")),
    sides_after="Reading politics is about not being surprised. Playing politics is about changing outcomes. A vendor should only ever do the first.",
    analogy_side="the sailor reading the weather",
    analogy="""  <p>A sailor can't change the weather. She watches the <b>clouds, the wind and the barometer</b>, writes them in the log every few hours, and asks one question: what does this mean for my boat? Then she reefs the sail or changes course. She doesn't argue with the sky, and she doesn't tell other boats what to do.</p>""",
    map=[("Clouds, wind, barometer", "Invitations, seating, budget papers"),
         ("Writing them in the log", "Signals as facts in a notebook"),
         ("What does it mean for my boat?", "What does it change for Lodestar?"),
         ("Reefing the sail", "Briefing Rupert's office; writing decisions down"),
         ("Not arguing with the sky", "Not taking sides in MetroVolt's politics")],
    how_side="collect facts, map monthly, ask what changes, act narrowly",
    how="""  <p><b>Collect facts, not interpretations.</b> Ines keeps a “signals” page: “6 Oct: Ascend readiness series, chair Rupert; invitees include Elaine, Gareth, Oliver; not Priya.” No adjectives, no guesses.</p>
  <p><b>Update the power map monthly</b> (the one from August 2027). October's changes: Rupert's influence on Lodestar up; Gareth's up; Priya's down; Vexmoor's assurance role close to Rupert.</p>
  <p><b>Ask one question: what does this change for Lodestar?</b> Two things. Phase 2 decisions may move from Priya to Rupert, so Rupert's office needs to hear about wave 1 from Wrenfield directly, not only through Vexmoor. And the meter data could change owner, so every decision about it should be in writing now.</p>
  <p><b>Act only on that.</b> Ines asks Elaine (not Rupert) whether a one-page wave 1 summary for Rupert's office would help; Elaine says yes and sends it herself. She doesn't speculate with anyone about Ascend, and when Callum asks “is Priya on the way out?”, she says: “I don't know, and it isn't ours to guess.”</p>""",
    how_figs=[rp_how],
    steps=[("Keep a signals page", "Facts with dates; no interpretations."),
           ("Update the power map monthly", "Influence, stance, needs."),
           ("Ask what it changes for you", "Usually one or two things."),
           ("Act narrowly", "Brief the right person, put things in writing."),
           ("Go through your counterpart", "Not around them."),
           ("Never speculate aloud", "Not even inside your own team.")],
    vocab=[("Political awareness", "Understanding how influence works in an organisation, without exploiting it."),
           ("Signal", "A small observable fact that may indicate a change."),
           ("Power map", "A drawing of influence, stance and needs around a decision."),
           ("Neutrality", "Not taking sides in the client's internal disputes."),
           ("Proxy briefing", "Briefing a senior person through your counterpart."),
           ("Speculation", "Guessing aloud about others' motives or futures; harmful when repeated.")],
    code=dict(file="notebook/signals-2028-10.md", note="Ines's notebook · Tue 10 Oct 2028 (private)", src="""
SIGNALS · October 2028                                              (facts only)

06 Oct  "Ascend readiness" weekly, chair Rupert; Elaine, Gareth, Oliver invited; not Priya
09 Oct  Network Assets team moves to floor 20 (next to Rupert)
09 Oct  Horizon budget paper p.4: "customer data services (Network Assets)"
10 Oct  Vexmoor team badges: transformation office (same as Rupert's)

power map changes   Rupert ↑ · Gareth ↑ · Priya ↓ · Vexmoor (assurance) close to Rupert
what changes for Lodestar
  1 phase 2 decisions may move to Rupert → wave 1 summary to his office (via Elaine)
  2 meter data may change owner → every meter-data decision in writing now
don't   speculate · repeat · take sides
"""),
    contract=dict(side="who the contract still says decides", doc="Lodestar SOW · §8.1 and §8.5", date="signed 30 June 2027", stamp="unchanged (for now)",
                  clauses=[("8.1", "MetroVolt's Sponsor is the Head of Customer Operations.", "a reorg can change the person before it changes the clause."),
                           ("8.5", "Instructions to the Supplier are valid only if given by MetroVolt's Programme Director or the Steering Committee.", "whoever gains influence, instructions still come through Elaine. say so, politely, if needed.")],
                  plain="politics changes who has influence faster than contracts change who has authority. Keep taking instructions from the people the contract names until the contract changes."),
    health=dict(now="a",
                g=("stable client", ["A light monthly look.", "Nothing to act on most months.", "Keep the map current."]),
                a=("a reorganisation is coming", ["Signals page, monthly map.", "Brief new centres of power via your counterpart.", "Decisions in writing."]),
                r=("factions fighting over your project", ["Only contractual instructions.", "Strict neutrality.", "Everything minuted."])),
    pressure=dict(level=3, title="the weather changing", cost="uncertainty about phase 2 · a team asking questions",
                  items=["When the client's politics shift, your team will want to gossip. Give them the line: “I don't know, and it isn't ours to guess.”", "Uncertainty is tiring. Write down what you can act on; let the rest go."]),
    baseline="Each line compares <b>ignoring the signals, or speculating about them</b> with <b>collecting facts, a monthly map and narrow action</b>.",
    ratings=[(3, 4, "Elaine sees a supplier that helps, not one that plays."),
             (3, 3, "Less gossip, more calm."),
             (3, 3, "Neutral now; phase 2 later."),
             (3, 4, "Meter-data decisions written down early."),
             (3, 3, "Neutral."),
             (2, 4, "The sponsor change won't be a surprise."),
             (2, 4, "Decisions in writing before owners change."),
             (3, 3, "Thirty minutes a month."),
             (4, 4, "One notebook page.")],
    pitfalls=[("Ignoring the signals", "Surprised by a new decider.", "a signals page, monthly map."),
              ("Speculating aloud", "Rumours traced back to you.", "facts only, never repeated."),
              ("Taking sides", "The losing side remembers.", "strict neutrality."),
              ("Going around your counterpart", "Trust broken.", "brief through them."),
              ("Over-reacting", "Changing plans on rumours.", "act only on what changes for you.")],
    grimoire=[(1, "rumour-mill-familiar", "The Rumour Mill Familiar", "explains what to feed the whisper network, and what never to say near it.")],
    use=["Any long engagement in a large organisation.", "A reorganisation or transformation is underway.", "The next contract depends on who decides."],
    skip=["A small client where the owner decides everything."],
    related=["<b>Who Really Decides Here?</b> (vol. 2)", "<b>What If Our Sponsor Moves On?</b> (next note)", "<b>Who Matters Most, and How Much?</b> (Sanne, vol. 5)", "<b>Stakeholder Map</b> (Ana, vol. 1)"],
    quiz=[("What goes on the signals page?", "Facts with dates, without interpretation."),
          ("What's the one question to ask of the signals?", "What does this change for our project?"),
          ("What did Ines do about Rupert's growing influence?", "Offered Elaine a one-page wave 1 summary for Rupert's office, sent by Elaine."),
          ("What are the three never-dos?", "Repeat it, take sides, trade on it."),
          ("Whose instructions count while politics shift?", "Still Elaine's and the steering committee's, as the contract says.")],
    quiz_sit=[("Gareth asks Ines over coffee what she thinks of “Priya's position” now. What does she say?", "Something true and neutral: Priya has been a strong sponsor for Lodestar, and Wrenfield works with whoever MetroVolt asks it to. Then change the subject to the meter data.")],
    try_it="Start a signals page for your main client or stakeholder group. Write five facts from the last month, without interpretation. What do they change for your work, and what one action follows?",
    remember="Read the weather; <span class=\"hl\">don't argue with the sky</span>. Facts, a monthly map, and act only on <span class=\"hl\">what changes for you</span>.",
    late=dict(when="Tue 10 October 2028 · 21:30 · hotel near The Grid",
              lines=["Ascend readiness. Priya not invited. Gareth moving upstairs. Vexmoor wearing Rupert's badge colour.",
                     "Callum asked if Priya's on the way out. I said I don't know, and it isn't ours to guess. True on both counts.",
                     "Elaine sent our wave 1 summary to Rupert's office herself. That's the move: through her, not around her."]),
    sources=["Jeffrey Pfeffer, <i>Power</i> (2010).",
             "Peter Block, <i>The Empowered Manager</i> (1987): positive political skills.",
             "Gerald Weinberg, <i>The Secrets of Consulting</i> (1985)."],
)

# ------------------------------------------------------------------ 02 What If Our Sponsor Moves On?
sm_problem = Doodle(760, 240, "Doodle of the email of 7 November 2028: as part of Ascend, Lodestar moves under the transformation office; Rupert Thorne becomes sponsor; Priya Nair will focus on customer service. Priya championed Lodestar for eighteen months. Rupert's office has heard about Lodestar mostly from Vexmoor.",
                    "7 November: “Lodestar moves to the transformation office. Rupert Thorne becomes sponsor.”", exact=True)
sm_problem.box(24, 30, 300, 120, "Priya", "green", sub="sponsor, 18 months", size=24, subsize=16)
sm_problem.arrow(330, 90, 430, 90)
sm_problem.box(436, 30, 300, 120, "Rupert", "y", sub="sponsor from 7 Nov", size=24, subsize=16)
sm_problem.note(586, 180, "heard about Lodestar mostly from Vexmoor", "red", size=17)

sm_how = Doodle(760, 330, "The first two weeks with a new sponsor. Day one: thank the old sponsor in person, and ask to stay in touch; Priya is still a director. Within a week: a one-page what you've inherited for Rupert, written in his language: cost, risk, dates. Within two weeks: a meeting to learn what he measures and what he fears. Then re-confirm the decisions that matter: the baseline, the change pool, the phase 2 timetable, in writing.",
                "Thank the old sponsor, brief the new one in a page, learn what they measure, re-confirm in writing.", exact=True)
for i, (h, sub, fill) in enumerate([("day 1", "thank Priya, in person", "green"), ("week 1", "a one-page brief", "y"), ("week 2", "what does he measure?", "blue"), ("then", "re-confirm in writing", "paper")]):
    sm_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=20, subsize=13)
sm_how.box(14, 160, 732, 70, "Rupert measures: cost out · Ascend targets · no surprises at the board", "pink", size=17)
sm_how.note(380, 280, "re-confirmed: baseline v2.0 · change pool rules · phase 2 timetable", "pen", size=17)

SPONSOR_MOVES = dict(
    slug="sponsor-moves", date=date(2028, 11, 7), meta=on_site(date(2028, 11, 7)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. a change of sponsor",
    tldr="When your sponsor moves on, the project's support can quietly go with them. <b>Thank the old sponsor</b> in person and keep them as an ally. Within a week, give the new one a <b>one-page “what you've inherited”</b> in <b>their language</b>. Within two, learn <b>what they measure and fear</b>. Then <b>re-confirm in writing</b> the decisions that matter. A new sponsor isn't obliged to keep their predecessor's promises unless they've made them their own.",
    chips=[("Family", "reading the room"), ("Lives in", "governance/sponsor-handover-2028-11.md"), ("Pairs with", "reading the client's politics, the stalled signature (vol. 2)")],
    problem_side="The Grid, 7 November 2028",
    problem="""  <p class="lead">On <b>Tuesday 7 November</b>, an all-staff email: as part of Rupert Thorne's “Ascend” programme, <b>Lodestar moves under the transformation office</b>, with Rupert as sponsor. <b>Priya Nair</b> will “focus on customer service excellence”.</p>
  <ul>
    <li>Priya sponsored Lodestar for eighteen months: through Horizon, CR-007, the ambush, the go / no-go.</li>
    <li>Rupert has heard about Lodestar mostly from <b>Vexmoor</b>, his advisers.</li>
    <li>Phase 2's tender is planned for March. <span class="hl-pink">The person who'll approve it has never had a meeting with Wrenfield.</span></li>
  </ul>""",
    problem_figs=[sm_problem],
    sides=dict(client=("Rupert", "<p>Rupert inherits a programme he didn't choose, run by a supplier he didn't pick, with a history he knows second-hand. He'll judge it by Ascend's measures: cost out, targets met, no surprises at the board. He has no obligation to honour understandings he wasn't part of.</p>", "Show me why this is a good use of Ascend's money."),
                vendor=("Ines", "<p>For Wrenfield, a new sponsor is a fresh start or a quiet end. Ines needs Rupert to see wave 1 with his own eyes, in his own measures, before Vexmoor's version sets. And she owes Priya a proper thank-you; she's still a director, and still a friend of the programme.</p>", "Earn the new sponsor without forgetting the old one.")),
    sides_after="A sponsor change resets trust to zero. The only thing that carries over automatically is what was written down.",
    analogy_side="the new head teacher",
    analogy="""  <p>A school gets a new head teacher. The good teachers don't complain that the old head promised them a new lab. They <b>thank the old head</b>, give the new one a short note on what each class is doing and why, find out what the new head cares about (exam results, say), and ask her to confirm the lab, in writing, in her own words.</p>""",
    map=[("The old head", "Priya, still a director"),
         ("The new head", "Rupert"),
         ("A short note on each class", "One page: what you've inherited"),
         ("What the new head cares about", "Cost out, Ascend targets, no board surprises"),
         ("Confirm the lab, in her own words", "Re-confirm baseline, change pool, phase 2 timetable")],
    how_side="thank, brief in their language, learn, re-confirm",
    how="""  <p><b>Day one: thank Priya.</b> Ines asks for fifteen minutes. She thanks Priya for specific things (the telling order in December, the go / no-go decision) and asks if she'd be willing to stay in touch. Priya: “Of course. And tell Rupert about the 31 %. He thinks it was your mistake.”</p>
  <p><b>Week one: one page, his language.</b> “What you've inherited” for Rupert, through Elaine: cost (£5.7m of £5.7m committed, milestones paid to M4), what it saves (wave 1 retired 16 % of MAVIS's batch load), what's left (warranty to January, phase 2 tender in March), risks, and the 31 % story told in two lines, with the contract clause that priced it.</p>
  <p><b>Week two: what does he measure?</b> At their first meeting, Ines asks more than she tells: “What would make Lodestar a success for Ascend? What would worry you?” Answer: cost out, a credible phase 2 price, no surprises at the board.</p>
  <p><b>Then re-confirm in writing.</b> Elaine puts three items on the next steering for Rupert to confirm as his own: baseline v2.0 to the end of warranty, the change-pool rules, and the phase 2 timetable. All three confirmed (DL-071).</p>""",
    how_figs=[sm_how],
    steps=[("Thank the old sponsor, specifically", "And ask to stay in touch."),
           ("Write a one-page handover", "In the new sponsor's measures."),
           ("Send it through your counterpart", "Not directly."),
           ("Ask before you tell", "What does success look like for them?"),
           ("Re-confirm key decisions", "As the new sponsor's own, in writing."),
           ("Correct second-hand stories gently", "With facts, once.")],
    vocab=[("Sponsor", "The senior person accountable for a programme's success."),
           ("Sponsor change", "When accountability moves to someone new."),
           ("Inherited commitments", "Promises made by a predecessor; not binding on the successor unless re-made."),
           ("Re-confirmation", "Asking a new decider to adopt earlier decisions explicitly."),
           ("Second-hand story", "What someone has heard about you from others."),
           ("Sponsor briefing", "A short document to bring a new sponsor up to speed.")],
    code=dict(file="governance/sponsor-handover-2028-11.md", note="for Rupert Thorne, via Elaine · Tue 14 Nov 2028", src="""
LODESTAR · WHAT YOU'VE INHERITED (1 page)

cost        committed £5.7m (discovery £380k · wave 1 £4.62m · CR-007 £700k)
            paid to M4 (wave 1 live); M5 hypercare (Nov) and M6 warranty (Jan) to come
saving      wave 1 retired ≈ 16 % of MAVIS batch load; all waves ≈ £1.9m/yr mainframe cost
results     379,997 customers moved 24 Sep · exceptions 0.32 % → 140 · no billing complaints
the 31 %    the bid assumed ≤ 5 % bad addresses (A1-07); discovery found 31 %; the
            contract priced it; CR-007 agreed at £700k with MetroVolt cleansing ≈ 40 %
next        warranty ends 18 Jan 2029 · phase 2 (waves 2–4) tender planned March 2029
risks       meter-data ownership (Network Assets) · Halvorsen re-tender (April)
to confirm  baseline v2.0 to warranty end · change-pool rules · phase 2 timetable
"""),
    contract=dict(side="what changes when the sponsor changes", doc="Lodestar SOW · §8.1 (as amended 14 Nov 2028)", date="variation V-04", stamp="sponsor changed",
                  clauses=[("8.1", "<del>MetroVolt's Sponsor is the Head of Customer Operations.</del> <ins>MetroVolt's Sponsor is the Director of Transformation.</ins>", "a variation, signed by both sides. the clause caught up with the email."),
                           ("DL-071", "The Sponsor confirms baseline v2.0 to the end of warranty, the change-pool rules in clause 7.4, and the phase 2 timetable.", "Rupert's decisions now. not Priya's.")],
                  plain="a sponsor change should be a formal variation to the contract, and the new sponsor should re-confirm the key decisions. Otherwise you're relying on a predecessor's word."),
    health=dict(now="a",
                g=("the new sponsor knows you", ["A short handover.", "Re-confirm anyway.", "Thank the old sponsor."]),
                a=("the new sponsor heard about you second-hand", ["One page in their measures.", "Ask before you tell.", "Correct stories with facts, once."]),
                r=("the new sponsor favours a rival", ["Everything in writing.", "Deliver the contract perfectly.", "Prepare for both outcomes."])),
    pressure=dict(level=4, title="a new boss you didn't choose", cost="18 months of trust reset to zero",
                  items=["Losing a sponsor who believed in you is sad. Say thank you properly; it's also the right thing.", "Rupert isn't against Wrenfield. He just hasn't met it. Make the first meeting about him."]),
    baseline="Each line compares <b>carrying on as if nothing changed</b> with <b>thanking Priya, a one-page handover, learning Rupert's measures and re-confirming decisions</b>.",
    ratings=[(2, 4, "Rupert hears Wrenfield's version from Wrenfield."),
             (3, 3, "Uncertainty, but a plan for it."),
             (3, 3, "Neutral."),
             (3, 4, "Key decisions re-confirmed."),
             (3, 3, "Neutral."),
             (2, 4, "The 31 % story corrected early."),
             (2, 5, "Variation V-04 and DL-071."),
             (3, 3, "Two weeks."),
             (4, 4, "One page.")],
    pitfalls=[("Assuming continuity", "The new sponsor doesn't feel bound.", "re-confirm in writing."),
              ("Forgetting the old sponsor", "You lose an ally and look ungrateful.", "thank them specifically."),
              ("Your language, not theirs", "The handover isn't read.", "their measures."),
              ("Going around your counterpart", "Elaine looks bypassed.", "send it through her."),
              ("Arguing with second-hand stories", "You sound defensive.", "facts, once, briefly.")],
    grimoire=[(3, "new-lord-arrives", "The New Lord Arrives", "is the same event from inside MetroVolt: surviving the first 90 days of a new boss.")],
    use=["Your sponsor changes.", "A reorganisation moves your project.", "A new decision maker for your next contract."],
    skip=["Never skip it."],
    related=["<b>How Do We Read the Client's Politics from Outside?</b> (previous note)", "<b>What If the Signature Stalls?</b> (vol. 2)", "<b>Who Really Decides Here?</b> (vol. 2)", "<b>How Do We Keep Them With Us?</b> (Sanne, vol. 5)"],
    quiz=[("What does Ines do on day one?", "Thanks Priya in person, specifically, and asks to stay in touch."),
          ("What's in the one-page handover?", "Cost, savings, results, the 31 % story, what's next, risks, and what to confirm."),
          ("Why ask before telling at the first meeting?", "To learn what the new sponsor measures and fears."),
          ("What did Rupert re-confirm?", "Baseline v2.0 to the end of warranty, the change-pool rules and the phase 2 timetable."),
          ("Why make the sponsor change a contract variation?", "So the contract names the person who now decides.")],
    quiz_sit=[("Rupert says in the first meeting: “Vexmoor tells me your 31 % was a bidding mistake.” What do you say?", "Calmly, once: the bid assumed 5 % in writing (A1-07), MetroVolt's own sample showed 7.8 %, the full data showed 31 %, and the contract priced the difference. Offer the documents. Then ask what he'd like Lodestar to achieve.")],
    try_it="Imagine your sponsor leaves tomorrow. Write the one page you'd give their successor, in the successor's likely measures. Which three decisions would you ask them to re-confirm?",
    remember="A new sponsor starts at zero. <span class=\"hl\">Thank the old one</span>, brief the new one in <span class=\"hl\">their language</span>, and re-confirm in writing.",
    late=dict(when="Tue 7 November 2028 · 22:15 · hotel near The Grid",
              lines=["Priya's moved off Lodestar. Rupert's our sponsor. He's heard about us mostly from Oliver.",
                     "Thanked Priya for the telling order and the go / no-go. She said: “Tell Rupert about the 31 %. He thinks it was your mistake.”",
                     "One page for Rupert by Tuesday. In pounds, not in pride."]),
    sources=["Michael Watkins, <i>The First 90 Days</i> (2003): seen from the other side.",
             "UK Infrastructure and Projects Authority, guidance on senior responsible owners.",
             "Project Management Institute, <i>The Standard for Program Management</i>: sponsorship."],
)

# ------------------------------------------------------------------ 03 What About the Stakeholder Who Holds the Budget?
bh_problem = Doodle(760, 240, "Doodle of Gareth Pound with a new title under Ascend: budget holder for customer data services, including the meter data that Lodestar's phase 2 depends on. In 2027 he wanted Lodestar in his own programme. Now he controls money phase 2 needs.",
                    "In 2027 Gareth wanted Lodestar. In 2028 he controls the budget phase 2 needs.", exact=True)
bh_problem.box(250, 40, 260, 120, "Gareth", "pink", sub="customer data services budget", size=24, subsize=15)
bh_problem.box(14, 60, 200, 80, "phase 2", "y", sub="needs meter data", size=19, subsize=15)
bh_problem.arrow(218, 100, 246, 100)
bh_problem.note(380, 210, "the old opponent now holds the purse", "red", size=20)

bh_how = Doodle(760, 330, "What Ines did. Meet him alone, early, and ask what he needs: credit for the meter data and a seat at phase 2's design. Find the shared win: a meter data service that both Lodestar and Network Assets use, owned by Network Assets, designed together. Give credit publicly: every Lodestar slide that shows meter data names Network Assets. Keep everything in writing: an interface agreement for the meter service, signed by Gareth.",
                "Ask what they need, find the shared win, give credit in public, and write it down.", exact=True)
for i, (h, sub, fill) in enumerate([("meet alone", "early, ask first", "y"), ("his need", "credit + a seat", "pink"), ("shared win", "meter data service", "green"), ("in writing", "IA-02, signed", "blue")]):
    bh_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=20, subsize=14)
bh_how.box(14, 150, 732, 70, "meter data service: owned by Network Assets, used by Lodestar, designed together", "green", size=16)
bh_how.note(380, 280, "an opponent with a stake becomes a co-owner", "pen", size=18)

BUDGET_HOLDER = dict(
    slug="budget-holder", date=date(2028, 11, 16), meta=on_site(date(2028, 11, 16)), where="FL 20", pass_kind="contractor",
    kicker="a.k.a. a powerful opponent gains budget control",
    tldr="When someone who opposed your project gains control of money it needs, don't avoid them and don't go around them. <b>Meet them early, alone</b>, and ask what they need. Look for a <b>shared win</b> that gives them ownership of something real. Give <b>credit in public</b>, and put the arrangement <b>in writing</b>. An opponent with a stake in your success is the strongest supporter you'll have.",
    chips=[("Family", "reading the room"), ("Lives in", "integration/IA-02-meter-data-service.md"), ("Pairs with", "mapping the client (vol. 2), quoting the contract (vol. 4)")],
    problem_side="The Grid, floor 20, 16 November 2028",
    problem="""  <p class="lead">Under Ascend, <b>Gareth Pound</b>'s Network Assets becomes the budget holder for <b>“customer data services”</b>, including the meter data and the meter feed (COPYMTR's replacement) that phase 2 depends on.</p>
  <ul>
    <li>Gareth wanted Lodestar in his own programme in 2027. In August he emailed Rupert that Lodestar was “refusing essential data”.</li>
    <li>Phase 2 can't be designed without his budget, and Rupert listens to him.</li>
    <li>Callum's suggestion: “keep our heads down and go through Elaine”. <span class="hl-pink">That's how an opponent stays an opponent.</span></li>
  </ul>""",
    problem_figs=[bh_problem],
    sides=dict(client=("Gareth", "<p>Gareth has spent years building Network Assets and believes the meter data is the heart of MetroVolt's future (he's not wrong). He resents a supplier from Leeds being the face of “customer data”. Credit and control matter to him more than any particular design.</p>", "My team built the meter data. Lodestar gets the headlines."),
                vendor=("Ines", "<p>Wrenfield needs Gareth's budget for phase 2 and his team's cooperation for the meter feed. It can't buy his support and mustn't flatter him. It can offer something he genuinely wants: ownership, credit and a seat at the design table.</p>", "Make him a co-owner, not a hurdle.")),
    sides_after="Most opponents aren't against your project; they're for something your project threatens. Find that thing.",
    analogy_side="the neighbour who owns the access road",
    analogy="""  <p>You want to build on your land, and the only access road belongs to a neighbour who objected to your plans. You could fight him through lawyers for years. Or you visit, ask what <b>he</b> needs (the road resurfaced, his name on the new sign), agree to <b>share the road and its upkeep</b>, and write it into a deed. Next year he's showing visitors round.</p>""",
    map=[("The access road", "The meter data and its budget"),
         ("The neighbour who objected", "Gareth, 2027–28"),
         ("What he needs", "Credit, control, a seat at the table"),
         ("Sharing the road", "A meter data service owned by Network Assets"),
         ("The deed", "Interface agreement IA-02, signed by Gareth")],
    how_side="meet early, ask, share the win, credit, write it down",
    how="""  <p><b>Meet early, alone.</b> Ines asks for 30 minutes on floor 20 on <b>16 November</b>, through Elaine. She brings no slides. Her first question: “What would make phase 2 good for Network Assets?”</p>
  <p><b>Listen for the need.</b> Gareth talks for twenty minutes: his team built the meter register; Lodestar's slides show “Lodestar” next to meter data; Network Assets is treated as a feed, not a partner. Underneath: <b>credit</b> and <b>a seat at the design table</b>.</p>
  <p><b>Find the shared win.</b> Ines proposes a <b>meter data service</b>, owned and run by Network Assets, that Lodestar and other systems use, designed jointly for phase 2. It replaces COPYMTR's file drop with something Gareth's team owns. It's also good architecture.</p>
  <p><b>Credit in public, and in writing.</b> From that week, every Lodestar slide showing meter data says “Network Assets meter data service”. The arrangement becomes <b>interface agreement IA-02</b>, signed by Gareth on 30 November. At the December steering, Gareth presents the meter data service himself. Rupert notices.</p>""",
    how_figs=[bh_how],
    steps=[("Meet early, alone, without slides", "Through your counterpart."),
           ("Ask what they need", "Then listen for twenty minutes."),
           ("Find the shared win", "Ownership of something real."),
           ("Give credit in public", "On every slide, in every meeting."),
           ("Write it down", "An agreement they sign."),
           ("Let them present it", "Their win, their stage.")],
    vocab=[("Budget holder", "The person who controls the money for an area."),
           ("Shared win", "An outcome good for both sides' goals."),
           ("Co-ownership", "Giving another party real ownership of part of the solution."),
           ("Interface agreement", "A written agreement on how two systems and teams connect."),
           ("Credit", "Public recognition of who did or owns something."),
           ("Opponent", "Someone working against your project, usually for reasons of their own.")],
    code=dict(file="integration/IA-02-meter-data-service.md", note="signed Thu 30 Nov 2028", src="""
INTERFACE AGREEMENT IA-02 · Meter data service

owner        Network Assets (Gareth Pound) · runs and funds the service
consumers    Lodestar (waves 1–4), billing (via Halvorsen), forecasting (Network Assets)
replaces     COPYMTR file drop (02:10 job, step 12) for migrated customers
design       joint: Network Assets + Wrenfield, for phase 2 (Jan–Mar 2029)
credit       all Lodestar materials: "Network Assets meter data service"
history      10 years readable via the service (replaces CR-019)
signed       Gareth Pound (Network Assets) · Hollis Wade (MetroVolt IT) · Ines Duarte (Wrenfield)
"""),
    contract=dict(side="how the new arrangement fits the contract", doc="Lodestar SOW · §3.6 and IA-02", date="30 Nov 2028", stamp="co-owned",
                  clauses=[("3.6", "Where a Dependency is to be provided by another part of MetroVolt or a third party, MetroVolt shall use reasonable endeavours to procure its provision.", "the meter service is now a dependency with an owner who wants it to work."),
                           ("IA-02, 2", "Network Assets owns and operates the Meter Data Service. Lodestar consumes it under the service levels in Annex A.", "Gareth's name, Gareth's service, Gareth's SLAs.")],
                  plain="turning a hidden feed into a service owned by the stakeholder who cares most about it improves both the architecture and the politics, and the agreement makes it last."),
    health=dict(now="a",
                g=("the budget holder is friendly", ["Brief them early.", "Co-design.", "Credit."]),
                a=("an old opponent with new power", ["Meet alone, ask first.", "A shared win.", "In writing, signed by them."]),
                r=("they're blocking deliberately", ["Contractual dependencies and dates.", "Escalate the dependency, not the person.", "Keep offering the shared win."])),
    pressure=dict(level=3, title="the old opponent", cost="one uncomfortable meeting · some pride",
                  items=["Walking into the office of someone who complained about you to Rupert takes nerve. Go anyway, and ask first.", "Giving away the credit for meter data costs Wrenfield nothing it needed."]),
    baseline="Each line compares <b>keeping heads down and going through Elaine</b> with <b>meeting Gareth, a shared win, public credit and a signed agreement</b>.",
    ratings=[(3, 4, "Gareth presents with Wrenfield, not against it."),
             (3, 3, "Neutral."),
             (3, 4, "CR-019 replaced by Gareth's own service."),
             (3, 4, "Who owns meter data is written."),
             (3, 5, "A proper service instead of a file drop."),
             (2, 4, "Phase 2's biggest dependency has a willing owner."),
             (3, 4, "IA-02 signed."),
             (3, 3, "Two weeks."),
             (3, 3, "One more agreement to keep.")],
    pitfalls=[("Avoiding the opponent", "They stay an opponent, with power.", "meet early."),
              ("Going around them", "They escalate again.", "through your counterpart, then directly."),
              ("Flattery", "They see through it.", "ask what they need."),
              ("Keeping the credit", "You win the slide, lose the budget.", "give it away."),
              ("Verbal deals", "Forgotten at the next reorg.", "signed, by them.")],
    grimoire=[(1, "empire-builder", "The Empire Builder", "explains Gareth from the inside: headcount, data and territory as dragon gold."), (1, "blood-pacts", "Blood Pacts", "is building alliances before you need them.")],
    use=["An opponent gains budget or authority over something you need.", "Before a tender they'll influence.", "A dependency owned by a reluctant team."],
    skip=["The budget holder is already a supporter: keep them informed."],
    related=["<b>Who Really Decides Here?</b> (vol. 2)", "<b>When Do We Quote the Contract?</b> (vol. 4)", "<b>What Does the 02:10 Job Really Do?</b> (vol. 3)", "<b>Negotiating with Stakeholders</b> (Ana, vol. 6)"],
    quiz=[("What did Ines ask Gareth first?", "What would make phase 2 good for Network Assets?"),
          ("What did Gareth actually need?", "Credit and a seat at the design table."),
          ("What was the shared win?", "A meter data service owned by Network Assets, used by Lodestar and others."),
          ("How did credit change?", "Every Lodestar slide showing meter data names the Network Assets meter data service."),
          ("Why get Gareth to sign IA-02?", "So the arrangement survives the next reorganisation.")],
    quiz_sit=[("At steering, Rupert praises “Lodestar's meter data integration”. Gareth is in the room. What does Ines say?", "Thank Rupert and correct it warmly: it's the Network Assets meter data service; Gareth's team built it, and Lodestar uses it.")],
    try_it="Think of someone powerful who's been against your work. Write down what they're for (not against). What shared win could give them real ownership? What credit could you give them in public?",
    remember="An opponent with <span class=\"hl\">a stake in your success</span> is your strongest supporter. Ask, share the win, <span class=\"hl\">give the credit</span>.",
    late=dict(when="Thu 16 November 2028 · 21:00 · hotel near The Grid",
              lines=["Thirty minutes on floor 20. Gareth talked for twenty of them. I learned more than in a year of meetings about him.",
                     "He doesn't hate Lodestar. He hates the meter data being called ours.",
                     "So it isn't ours anymore. It's his service. Better architecture too."]),
    sources=["Robert Cialdini, <i>Influence</i> (rev. ed., 2021): reciprocity.",
             "Roger Fisher and William Ury, <i>Getting to Yes</i> (1981): interests behind positions.",
             "Adam Grant, <i>Give and Take</i> (2013)."],
)

# ------------------------------------------------------------------ 04 What If an Executive Wants a Slide?
es_problem = Doodle(760, 240, "Doodle of Lord Varnish's request on 20 November 2028: a single slide for the board on 30 November titled Lodestar: the Orion foundation delivers. It credits Orion's hub, which Lodestar didn't use, and names nobody who did the work.",
                    "“Lodestar: the Orion foundation delivers.” For the board, in ten days.", exact=True)
es_problem.box(150, 30, 460, 140, "Lodestar:", "y", sub="“the Orion foundation delivers”", size=26, subsize=18)
es_problem.note(380, 210, "Lodestar didn't use Orion's hub. Nobody who did the work is named.", "red", size=17)

es_how = Doodle(760, 330, "The slide Ines sent. One page, facts only: 379,997 customers moved on 24 September; 0.32 per cent exceptions; no billing complaints; MAVIS batch load down 16 per cent. A credits line: Customer Operations, MetroVolt IT, Network Assets, Halvorsen, Wrenfield. A neutral history line: built on lessons from earlier programmes. Lord Varnish adds his own title. He keeps the facts.",
                "Give the executive a slide built from facts, with credit to the people, and let them choose the title.", exact=True)
es_how.box(14, 14, 520, 230, None, "paper", rx=6)
es_how.head(274, 46, "Lodestar wave 1 · 24 Sep 2028", size=19)
for i, t in enumerate(["379,997 customers moved", "0.32 % exceptions → cleared", "no billing complaints", "MAVIS batch load −16 %"]):
    es_how.text(34, 84 + i * 30, "• " + t, anchor="start", size=16)
es_how.text(34, 212, "built on lessons from earlier programmes", anchor="start", size=15)
es_how.box(550, 14, 196, 230, None, "green")
es_how.text(648, 60, "credits", size=19)
for k, t in enumerate(["Customer Ops", "MetroVolt IT", "Network Assets", "Halvorsen", "Wrenfield"]):
    es_how.note(648, 100 + k * 28, t, "pen", size=15)
es_how.note(380, 290, "the title is his. the facts are ours.", "pen", size=19)

EXEC_SLIDE = dict(
    slug="executive-slide", date=date(2028, 11, 23), meta=on_site(date(2028, 11, 23)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. credit politics and the board slide",
    tldr="Senior people need slides that make them look good to their board. Give them one, built from <b>facts</b>, with <b>credit to the people who did the work</b>, and let them choose the <b>title</b>. Don't fight over who gets praised; do refuse anything <b>untrue</b>. A slide that's accurate and generous survives the board, and the people named on it remember.",
    chips=[("Family", "reading the room"), ("Lives in", "governance/board-2028-11-30-slide.pptx"), ("Pairs with", "changing the numbers, the sponsor moves on")],
    problem_side="The Grid, floor 27, 23 November 2028",
    problem="""  <p class="lead">On <b>20 November</b> Lord Varnish's assistant asks Ines for a slide for MetroVolt's board on <b>30 November</b>, with a title already chosen: <b>“Lodestar: the Orion foundation delivers.”</b></p>
  <ul>
    <li>Lodestar didn't use Orion's hub. The design authority decided that in 2027.</li>
    <li>The draft names nobody: not Customer Ops' exception desk, not Bert, not MetroVolt IT.</li>
    <li>Hana's view: “Tell him Orion failed.” <span class="hl-pink">Lord Varnish founded Orion, and sits on the board.</span></li>
  </ul>""",
    problem_figs=[es_problem],
    sides=dict(client=("Lord Varnish", "<p>Lord Varnish launched Orion in 2024 and watched it fail. A successful Lodestar is a chance to tell the board the investment wasn't wasted. That's human. It's also partly true: Lodestar learned a lot from Orion's mistakes.</p>", "Let the board see Orion wasn't for nothing."),
                vendor=("Ines", "<p>Wrenfield doesn't need credit on the slide; it needs the slide to be <b>true</b>. A board paper claiming Lodestar was built on Orion's hub would be wrong, and could matter in phase 2. And the people who did the work deserve to be named.</p>", "His title. Our facts. Their names.")),
    sides_after="Credit is cheap to give and expensive to fight for. Accuracy is the one thing you can't give away.",
    analogy_side="the speech at the wedding",
    analogy="""  <p>The bride's uncle wants to say in his speech that he introduced the couple. He didn't, quite: he invited them both to a party where they met. A wise best man doesn't argue. He gives the uncle a <b>true version</b> (“it all started at Uncle Simon's party”), thanks the people who organised the wedding by name, and lets the uncle enjoy his moment.</p>""",
    map=[("The uncle's speech", "Lord Varnish's board slide"),
         ("“I introduced them”", "“The Orion foundation delivers”"),
         ("“It started at his party”", "“Built on lessons from earlier programmes”"),
         ("Thanking the organisers by name", "The credits line"),
         ("Letting him enjoy it", "Letting him choose the title")],
    how_side="facts, credit, a true history line, and his title",
    how="""  <p>Ines doesn't argue about the title. She sends a slide through Elaine on <b>23 November</b> with three parts:</p>
  <ul>
    <li><b>Facts</b>: 379,997 customers moved on 24 September; 0.32 % exceptions, cleared within a day; no billing complaints; MAVIS's batch load down 16 %.</li>
    <li><b>Credits</b>: Customer Operations (the exception desk), MetroVolt IT, Network Assets, Halvorsen, Wrenfield. People first, supplier last.</li>
    <li><b>A true history line</b>: “Built on lessons from earlier programmes, including Orion.” True, generous, and not a claim about the hub.</li>
  </ul>
  <p>The covering note says: “Title as you prefer; we've kept the facts to what the board can verify.” Lord Varnish's office changes the title to <b>“Lodestar: lessons from Orion deliver”</b>. It keeps every fact and every credit. Hana says that's still not true. Ines says it's close enough to be fair, and the facts underneath are exact.</p>""",
    how_figs=[es_how],
    steps=[("Don't argue about the title", "It's theirs."),
           ("Build the body from verifiable facts", "Numbers the board can check."),
           ("Credit people before suppliers", "By team, by name if possible."),
           ("Offer a true version of their story", "Generous, not false."),
           ("Say what you kept to, politely", "“Facts the board can verify.”"),
           ("Refuse only what's untrue", "Not what's flattering.")],
    vocab=[("Board paper", "A document presented to a company's board of directors."),
           ("Credit politics", "Competition over who is recognised for success."),
           ("Verifiable fact", "A statement someone else can check."),
           ("Narrative", "The story told around facts; flexible within truth."),
           ("Attribution", "Naming who did or contributed to something."),
           ("Executive sponsor", "A senior person whose reputation is attached to a programme.")],
    code=dict(file="governance/board-2028-11-30-slide.md", note="sent via Elaine · Thu 23 Nov 2028", src="""
BOARD SLIDE · 30 Nov 2028 (title: Lord Varnish's office)
"Lodestar: lessons from Orion deliver"            ← title chosen by his office

Wave 1 went live on Sunday 24 September 2028
  • 379,997 customers moved from MAVIS to the new platform
  • 0.32 % needed manual handling; all resolved within a day
  • no billing complaints from moved customers
  • MAVIS nightly batch load reduced by 16 %
Built on lessons from earlier programmes, including Orion.
With thanks to Customer Operations (exception desk) · MetroVolt IT · Network Assets
· Halvorsen Systems · Wrenfield Digital

covering note: "Title as you prefer; we've kept the facts to what the board can verify."
"""),
    contract=dict(side="what the supplier may and may not publish", doc="Lodestar SOW · §14 (publicity)", date="signed 30 June 2027", stamp="MetroVolt's slide",
                  clauses=[("14.1", "The Supplier shall not make public statements about the Services without MetroVolt's prior written consent.", "the board slide is MetroVolt's. we provide facts; they present."),
                           ("14.3", "Each Party shall ensure information it provides for the other's governance is accurate.", "the one line that lets us say no to a false claim.")],
                  plain="the client owns its board papers; you supply facts. An accuracy clause gives you a firm, polite reason to keep the facts right while leaving the story to them."),
    health=dict(now="a",
                g=("trust is high", ["Suggest the slide before they ask.", "Credits as standard.", "Let them present."]),
                a=("an executive with a story to tell", ["Facts, credits, a true history line.", "Their title.", "Refuse only what's untrue."]),
                r=("the slide misrepresents your work", ["Correct it in writing, through your counterpart.", "Facts with sources.", "Escalate inaccuracy, never credit."])),
    pressure=dict(level=3, title="someone else's story", cost="a team that wants recognition · a founder's pride",
                  items=["Hana wanted the slide to say Orion failed. Don't let the team's frustration write board papers.", "Credit Customer Ops' desk first. They worked through the night and through Sunday."]),
    baseline="Each line compares <b>arguing about the title, or sending what was asked</b> with <b>facts, credits, a true history line and their title</b>.",
    ratings=[(3, 4, "Lord Varnish got his moment; the board got facts."),
             (2, 3, "The team named, though not as the headline."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "No false claim about the Orion hub."),
             (2, 4, "Board record accurate for phase 2."),
             (2, 4, "Facts on file with a covering note."),
             (4, 4, "An afternoon."),
             (4, 4, "One slide.")],
    pitfalls=[("Fighting for credit", "You lose the executive and gain nothing.", "credit people, let them have the title."),
              ("Sending what was asked", "A false claim in a board paper.", "facts the board can verify."),
              ("Naming only the supplier", "Client teams feel used.", "people first, supplier last."),
              ("Mocking the old programme", "The founder sits on the board.", "a generous, true history line."),
              ("Going around your counterpart", "Politics you can't win.", "through Elaine.")],
    grimoire=[(2, "credit-vampire", "The Credit Vampire", "is what this looks like when it's about a colleague's work, not a programme's."), (3, "credit-taking-crown", "The Credit-Taking Crown", "is the same creature wearing a senior title.")],
    use=["Senior people ask for success slides.", "A programme's history is politically sensitive.", "Credit could go to the wrong people."],
    skip=["The client already writes its own accurate summaries: just check the facts."],
    related=["<b>What If the Client Asks Us to Change the Numbers?</b> (this volume)", "<b>What If Our Sponsor Moves On?</b> (this volume)", "<b>How Do We Compete with a Big Consultancy?</b> (vol. 1)", "<b>Presenting to Executives</b> (Ana, vol. 3)"],
    quiz=[("What three parts did the slide have?", "Verifiable facts, credits (people first), and a true history line."),
          ("Why not argue about the title?", "It's the executive's; credit is cheap to give and expensive to fight for."),
          ("What would Ines refuse?", "Anything untrue, such as claiming Lodestar used Orion's hub."),
          ("Why “built on lessons from earlier programmes, including Orion”?", "It's true and generous without a false claim."),
          ("Which clause supports accuracy?", "14.3: information for the other's governance must be accurate.")],
    quiz_sit=[("The final board pack, sent after the meeting, says “Lodestar reused the Orion data hub”. What do you do?", "Tell Elaine the same day with the design authority decision (2027) and ask for a one-line correction to the minutes. Politely, in writing, once; it matters for phase 2.")],
    try_it="Write a one-slide summary of a recent success for a senior audience: three verifiable facts, a credits line with people first, and a true sentence about its history. Who chooses the title?",
    remember="Give away <span class=\"hl\">the credit</span>, never <span class=\"hl\">the facts</span>. Their title, your numbers, everyone's names.",
    late=dict(when="Thu 23 November 2028 · 20:40 · hotel near The Grid",
              lines=["“The Orion foundation delivers.” Hana wanted to write “Orion failed” in 40-point font.",
                     "Sent facts, credits and “built on lessons from earlier programmes, including Orion”. Their title, our numbers.",
                     "His office kept every fact and every name. Customer Ops' exception desk is on a board slide. That's the bit I'm proud of."]),
    sources=["Nancy Duarte, <i>Resonate</i> (2010).",
             "Adam Grant, <i>Give and Take</i> (2013).",
             "Chip Heath and Dan Heath, <i>Made to Stick</i> (2007)."],
)

NOTES = [READING_POLITICS, SPONSOR_MOVES, BUDGET_HOLDER, EXEC_SLIDE]
