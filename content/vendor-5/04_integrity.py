# Series 5 · On the Client's Floor · Vol. 5 · Other People's Politics · Integrity under pressure (notes 13–15).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 13 What Do We Do with What We Overhear?
oh_problem = Doodle(760, 240, "Doodle of the lift at The Grid on 14 December 2028. Two MetroVolt directors, unaware Ines is behind them, discuss Ascend: Customer Operations will lose 40 roles in the spring, and phase 2's budget may be cut to fund it. Ines hears every word. Callum will be at dinner with Vivian that evening.",
                    "The lift, 08:52: forty roles, a phase 2 budget cut, and nobody knows Ines heard.", exact=True)
oh_problem.box(250, 20, 260, 200, None, "paper", rx=6)
oh_problem.circle(330, 110, 26, "y")
oh_problem.circle(430, 110, 26, "y")
oh_problem.circle(380, 180, 20, "blue")
oh_problem.note(630, 80, "“40 roles, spring”", "red", size=18)
oh_problem.note(630, 120, "“phase 2 budget cut?”", "red", size=18)
oh_problem.note(110, 110, "Ines, behind", "pen", size=18)

oh_how = Doodle(760, 320, "What Ines did with it. Don't repeat it, to anyone, including Callum, Vivian and Graham. Don't trade on it: no change to the phase 2 bid, no hints to Elaine. Don't act as if you know: wait for the announcement. If it raises a legal or ethical duty, get advice; this one didn't. And reduce the chance of hearing more: take the stairs when directors are talking. When the Ascend announcement comes in February, it says 36 roles, not 40.",
                "Don't repeat, don't trade, don't act on it, get advice if it matters legally, and wait.", exact=True)
for i, (h, sub, fill) in enumerate([("don't repeat", "not even to Callum", "pink"), ("don't trade", "bid unchanged", "pink"), ("don't act", "wait for the news", "pink"), ("advice?", "only if legal duty", "paper")]):
    oh_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=14)
oh_how.box(14, 150, 732, 70, "February announcement: 36 roles, not 40; phase 2 budget unchanged", "green", size=17)
oh_how.note(380, 280, "overheard news is often wrong, and always not yours", "pen", size=18)

OVERHEAR = dict(
    slug="what-you-overhear", date=date(2028, 12, 14), meta=on_site(date(2028, 12, 14)), where="LIFT", pass_kind="contractor",
    kicker="a.k.a. confidential information you weren't meant to hear",
    tldr="On a client's site you will overhear things: restructures, budgets, people's futures. Treat it as <b>confidential</b>: <b>don't repeat it</b> (not even inside your firm), <b>don't trade on it</b> (in bids, prices or negotiations), and <b>don't act as if you know</b>. If it creates a real legal or ethical duty, get advice. Otherwise, wait for the announcement. Overheard news is often wrong, and it is never yours.",
    chips=[("Family", "integrity under pressure"), ("Lives in", "nowhere (that's the point)"), ("Pairs with", "sharing a floor with the rival, staff fear")],
    problem_side="The Grid, the lift, 14 December 2028",
    problem="""  <p class="lead">At 08:52 on <b>Thursday 14 December</b>, two MetroVolt directors get into the lift on floor 2. They don't notice Ines behind them. They talk about <b>Ascend</b>.</p>
  <ul>
    <li>Customer Operations will lose <b>40 roles</b> in the spring.</li>
    <li>Phase 2's budget “may have to give” to fund other Ascend work.</li>
    <li>Callum and Vivian are finalising Wrenfield's phase 2 pricing strategy that evening. <span class="hl-pink">A smaller budget would change everything about it.</span></li>
  </ul>""",
    problem_figs=[oh_problem],
    sides=dict(client=("MetroVolt", "<p>Restructures are discussed for weeks before announcements; sometimes carelessly. The people affected (including Asif's colleagues) should hear it from their employer, properly, not from a rumour that started with a supplier.</p>", "That wasn't meant for you."),
                vendor=("Ines", "<p>The information could help Wrenfield price phase 2. It could also be wrong, it isn't Wrenfield's, using it would breach confidentiality, and repeating it would hurt people Ines works with every day. The only question is how completely to forget it.</p>", "I heard it. It isn't mine.")),
    sides_after="Information you weren't meant to have is a test of character with no witnesses. That's what makes it a real one.",
    analogy_side="the overheard phone call on the train",
    analogy="""  <p>On a train you overhear someone telling a colleague, loudly, that their company will make cuts next month. You happen to own shares in that company. You don't sell, and you don't tell your friends to sell: it would be <b>using information you had no right to</b>, and in some cases a crime. You put your headphones on.</p>""",
    map=[("The loud phone call", "The directors in the lift"),
         ("Shares in the company", "Wrenfield's phase 2 bid"),
         ("Selling on it", "Changing the bid price"),
         ("Telling friends", "Repeating it to Callum and Vivian"),
         ("Putting headphones on", "Taking the stairs when directors are talking")],
    how_side="don't repeat, don't trade, don't act, get advice if needed, wait",
    how="""  <p><b>Don't repeat it.</b> Not to Callum, Vivian or Graham, not even as “I heard something”. Inside Wrenfield, a rumour becomes a planning assumption within a day.</p>
  <p><b>Don't trade on it.</b> That evening, Callum asks whether there's anything that should change the phase 2 pricing strategy. Ines says: “Nothing I can share. Price it on the evidence, as agreed.” The strategy doesn't change.</p>
  <p><b>Don't act as if you know.</b> When Asif mentions Ascend rumours a week later, Ines says what she said in October: she doesn't know anything she can share, and the right people to ask are at MetroVolt. (True: what she overheard isn't knowledge she can share.)</p>
  <p><b>Get advice if it matters legally.</b> If she'd overheard something unlawful, or something that put people at risk, she would talk to Wrenfield's lawyer and, if needed, MetroVolt's whistleblowing route. This was neither.</p>
  <p><b>Wait.</b> In February, Ascend is announced: <b>36</b> roles in Customer Operations, not 40, and phase 2's budget <b>unchanged</b>. A bid priced on the lift would have been wrong.</p>""",
    how_figs=[oh_how],
    steps=[("Don't repeat it", "To anyone, inside or outside your firm."),
           ("Don't use it", "In bids, prices, negotiations or plans."),
           ("Don't act as if you know", "Behave exactly as before."),
           ("Ask: does it create a legal duty?", "If yes, get advice."),
           ("Reduce exposure", "Stairs, headphones, step away."),
           ("Wait for the announcement", "It's often different.")],
    vocab=[("Confidential information", "Information not meant to be shared outside a defined group."),
           ("Inadvertent disclosure", "Learning something by accident."),
           ("Insider information", "Non-public information that could give an unfair advantage."),
           ("Duty of confidence", "An obligation not to use or disclose confidential information."),
           ("Whistleblowing", "Reporting serious wrongdoing through protected routes."),
           ("Rumour", "Unconfirmed information that spreads; often wrong.")],
    code=dict(file="(none)", note="deliberately not written down", src="""
WHAT GOT WRITTEN DOWN ABOUT THE LIFT

(nothing)

What Ines did instead:
  · took the stairs on floor-2 mornings for the rest of December
  · told Callum: "price phase 2 on the evidence, as agreed"
  · told Asif: "nothing I can share; ask MetroVolt"
  · checked: unlawful? risk to people? → no → no advice needed
February 2029: Ascend announced. Customer Ops −36 roles. Phase 2 budget unchanged.
"""),
    contract=dict(side="the duty that applies even to accidents", doc="Lodestar SOW · §16 (confidentiality)", date="signed 30 June 2027", stamp="confidential",
                  clauses=[("16.1", "The Supplier shall keep confidential all information about MetroVolt which it obtains in connection with the Services, however obtained, and use it only for the Services.", "“however obtained”. a lift counts."),
                           ("Phase 2 ITT (draft), 7.3", "MetroVolt may exclude a bidder that has obtained confidential information that could give it an undue advantage.", "a bid priced on the lift could be excluded, if anyone ever knew.")],
                  plain="confidentiality clauses usually cover information however you came by it, including by accident. Using overheard information in a bid can breach the contract and the procurement rules, even if nobody finds out."),
    health=dict(now="g",
                g=("any client", ["Same rules.", "No exceptions for friends.", "Wait for the news."]),
                a=("a procurement coming", ["Especially careful with bid-relevant information.", "Price on evidence only.", "Brief the team: no rumours in bids."]),
                r=("you learn of wrongdoing", ["Get legal advice.", "Use protected routes.", "Write down facts, not rumours."])),
    pressure=dict(level=3, title="the secret", cost="a heavy evening · an unchanged pricing strategy",
                  items=["Not telling your own team something useful feels disloyal. It's the opposite: it keeps them clean.", "The temptation is strongest right before a bid. That's when the rule matters most."]),
    baseline="Each line compares <b>sharing what you overheard with your bid team</b> with <b>not repeating it, not using it, and waiting</b>.",
    ratings=[(3, 4, "MetroVolt's confidence is kept, without knowing it."),
             (3, 3, "One person carries the secret, briefly."),
             (3, 4, "The bid isn't priced on a wrong rumour."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "No exclusion risk for phase 2."),
             (3, 3, "Nothing to write; that's correct."),
             (4, 4, "Nothing to do."),
             (4, 4, "Nothing to keep.")],
    pitfalls=[("“Just between us”", "It's everyone's by Friday.", "don't repeat it at all."),
              ("Using it in a bid", "Breach, exclusion, and often wrong.", "price on evidence."),
              ("Acting as if you know", "People guess where you heard it.", "behave as before."),
              ("Ignoring a real legal duty", "Harm continues.", "get advice."),
              ("Staying where you'll hear more", "Temptation repeats.", "take the stairs.")],
    grimoire=[(1, "rumour-mill-familiar", "The Rumour Mill Familiar", "explains what happens to overheard news inside MetroVolt: it grows in four bubbles.")],
    use=["You overhear something confidential.", "You see a document left on a printer.", "Anything that could help your firm unfairly."],
    skip=["Never skip it."],
    related=["<b>How Do We Share a Floor with the Rival?</b> (this volume)", "<b>What If Client Staff Fear We'll Take Their Jobs?</b> (this volume)", "<b>How Do We Bid Against the Rival for the Next Phase?</b> (vol. 6)", "<b>What If the Client Asks Us to Change the Numbers?</b> (next note)"],
    quiz=[("What are the three don'ts?", "Don't repeat it, don't trade on it, don't act as if you know."),
          ("Why not tell your own bid team?", "A rumour becomes a planning assumption; using it can breach confidentiality and procurement rules."),
          ("When should you get advice?", "If what you overheard creates a legal or ethical duty, such as wrongdoing or risk to people."),
          ("What did the February announcement say?", "36 roles, not 40, and phase 2's budget unchanged."),
          ("What does “however obtained” in clause 16.1 mean?", "Confidentiality covers information you came by accidentally too.")],
    quiz_sit=[("Vivian says she heard a rumour that phase 2's budget will be cut, and asks Ines to confirm. What does Ines say?", "That she can't confirm or discuss rumours about MetroVolt's budgets, and that the bid should be priced on the evidence and the tender documents only.")],
    try_it="Write your own rule for overheard information: what you'll never do with it, and the one situation where you'd get advice. Share the rule (not any information) with your team.",
    remember="What you overhear <span class=\"hl\">isn't yours</span>. Don't repeat it, don't use it, and <span class=\"hl\">wait for the news</span>.",
    late=dict(when="Thu 14 December 2028 · 22:30 · hotel near The Grid",
              lines=["Forty roles in Customer Ops. Phase 2's budget “may have to give”. In a lift, at 08:52.",
                     "Callum asked at dinner if anything should change our pricing. “Nothing I can share.” He didn't push. Good man.",
                     "I'll take the stairs on floor-2 mornings until Christmas. It's six floors. I need the exercise anyway."]),
    sources=["UK Ministry of Justice, guidance on the Bribery Act and improper performance.",
             "Crown Commercial Service, guidance on conflicts of interest and confidential information in procurement.",
             "Institute of Business Ethics, guidance on confidentiality."],
)

# ------------------------------------------------------------------ 14 What If the Client Asks Us to Change the Numbers?
cn_problem = Doodle(760, 240, "Doodle of Rupert's request on 16 January 2029, for the Ascend board paper: state that Lodestar has realised 1.9 million pounds a year of mainframe savings. In fact wave 1 retired about 16 per cent of the batch load; the mainframe still runs; realised savings so far are about 210,000 pounds a year. He asks Ines to sign the benefits section.",
                    "“Lodestar has realised £1.9m a year.” Realised so far: about £210k.", exact=True)
cn_problem.box(24, 40, 330, 120, "the request", "pink", sub="“£1.9m/yr realised” · sign it", size=21, subsize=15)
cn_problem.box(406, 40, 330, 120, "the fact", "green", sub="≈ £210k/yr realised · £1.9m when all waves done", size=21, subsize=13)
cn_problem.note(380, 210, "a board paper, with Wrenfield's name under it", "red", size=19)

cn_how = Doodle(760, 340, "How Ines refused. Say no to the misstatement, clearly, privately, the same day. Offer an accurate way to say what Rupert wants to say: Lodestar is on track to remove 1.9 million a year when all waves complete, with 210,000 a year realised after wave 1. Put the refusal and the offer in writing to Rupert, copied to Elaine. Don't sign anything inaccurate. If pressed, escalate through Graham and the contract's accuracy clause. Rupert uses the accurate wording.",
                "Refuse the misstatement, offer an accurate version, write both down, and don't sign.", exact=True)
for i, (h, sub, fill) in enumerate([("refuse", "privately, same day", "pink"), ("offer", "an accurate version", "green"), ("in writing", "to Rupert, cc Elaine", "y"), ("don't sign", "anything untrue", "pink")]):
    cn_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=20, subsize=14)
cn_how.box(14, 150, 732, 80, "“on track to remove £1.9m a year when all waves complete; £210k a year realised after wave 1”", "green", size=16)
cn_how.note(380, 290, "Rupert used it. The board paper was true.", "pen", size=19)

CHANGE_NUMBERS = dict(
    slug="change-the-numbers", date=date(2029, 1, 16), meta=on_site(date(2029, 1, 16)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. being asked to misstate facts",
    tldr="Sooner or later a client will ask you to make the numbers say something they don't. <b>Refuse the misstatement</b>, clearly and privately, the same day. <b>Offer an accurate way</b> to say what they need to say; there's almost always one. Put <b>both in writing</b>. <b>Don't sign</b> anything untrue, whatever it costs the next contract. Most people who ask this are under pressure, not dishonest, and take the accurate version when it's offered.",
    chips=[("Family", "integrity under pressure"), ("Lives in", "email to Rupert, 16 Jan 2029 (cc Elaine)"), ("Pairs with", "an executive's slide, protecting margin (vol. 4)")],
    problem_side="The Grid, floor 27, 16 January 2029",
    problem="""  <p class="lead">Rupert is preparing the <b>Ascend board paper</b> for February. On <b>Tuesday 16 January</b> he asks Ines to <b>sign the Lodestar benefits section</b>, which says: <i>“Lodestar has realised £1.9m a year of mainframe savings.”</i></p>
  <ul>
    <li>£1.9m a year is MAVIS's total mainframe cost, saved <b>only when all four waves</b> are done (about 2031).</li>
    <li>Wave 1 retired about 16 % of the batch load; realised savings so far are about <b>£210k a year</b>.</li>
    <li>Phase 2's decision is Rupert's. <span class="hl-pink">Ines's signature would be under a number she knows is false.</span></li>
  </ul>""",
    problem_figs=[cn_problem],
    sides=dict(client=("Rupert", "<p>Rupert's Ascend targets are aggressive, and the board wants savings now. “£1.9m a year” is a real number; he's telling himself the tense doesn't matter. He wants the supplier's signature because it makes the claim look independent.</p>", "It's going to be true. Why not say it now?"),
                vendor=("Ines", "<p>Refusing a sponsor who decides phase 2, two months before the tender, could cost Wrenfield £9m. Signing would put Wrenfield's name under a false statement to a regulated company's board, and the board would find out by 2030. Ines decides in about a minute. The rest is how.</p>", "There's no version of this where I sign a false number.")),
    sides_after="The ask is rarely “lie for me”. It's “say it a bit more positively”, from someone under pressure. The answer is the same: the true version, said well.",
    analogy_side="the surveyor's valuation",
    analogy="""  <p>A seller asks the surveyor to value the house “as it will be” after the planned extension. A good surveyor says no to the false figure, and offers the true one: <b>“Current value £320,000; estimated £380,000 once the extension is built.”</b> Both numbers are useful to a buyer. Only one of them can carry her signature today.</p>""",
    map=[("The value “as it will be”", "“£1.9m a year realised”"),
         ("Current value", "£210k a year realised after wave 1"),
         ("Estimated after the extension", "£1.9m a year when all waves complete"),
         ("Her signature", "Wrenfield's sign-off on the benefits section"),
         ("Both numbers useful to a buyer", "The accurate wording is still a strong story")],
    how_side="refuse, offer, write it down, don't sign",
    how="""  <p><b>Refuse, privately, the same day.</b> Ines asks Rupert for ten minutes that afternoon, alone. <i>“I can't sign that sentence: £1.9m is what all four waves will save; wave 1 has realised about £210k a year. If the board reads it as realised, it will be wrong.”</i></p>
  <p><b>Offer an accurate version that still serves him.</b> <i>“Lodestar is on track to remove MAVIS's mainframe cost of £1.9m a year when all waves complete; wave 1 has already realised about £210k a year and retired 16 % of the batch load.”</i> It's a good story: it shows momentum and a big prize. Ines also offers the calculation, sourced, for the appendix.</p>
  <p><b>Write it down.</b> A short email to Rupert at 17:12, copied to Elaine: the original sentence, why Wrenfield can't sign it, the accurate wording, the calculation attached.</p>
  <p><b>Don't sign anything untrue, and know your escalation.</b> If Rupert had insisted, Ines would have told Graham the same day, cited the accuracy clause (§14.3), and declined to sign, whatever it did to phase 2. She didn't need to. Rupert replied at 19:40: <i>“Use your wording.”</i> The February board paper is accurate.</p>""",
    how_figs=[cn_how],
    steps=[("Decide quickly that you won't", "The how is harder than the whether."),
           ("Refuse privately, the same day", "No audience, no delay."),
           ("Offer an accurate version", "That still meets their need."),
           ("Write it down", "Original, reason, alternative, sources."),
           ("Don't sign anything untrue", "Whatever it costs."),
           ("Know your escalation", "Your own leadership, the contract's accuracy clause, advice if needed.")],
    vocab=[("Misstatement", "A statement that is false or misleading."),
           ("Realised benefit", "A benefit already achieved, not forecast."),
           ("Forecast benefit", "A benefit expected in future, with assumptions."),
           ("Sign-off", "A formal confirmation that something is correct."),
           ("Integrity", "Doing what's right when it costs you."),
           ("Escalation of an ethical concern", "Taking a refusal or concern to people with authority, in writing.")],
    code=dict(file="email/2029-01-16-benefits.md", note="Ines to Rupert, cc Elaine · Tue 16 Jan 2029, 17:12", src="""
Subject: Ascend board paper: Lodestar benefits

Rupert,
As discussed, we can't sign "Lodestar has realised £1.9m a year of mainframe savings".
£1.9m a year is the saving when all four waves are complete (≈ 2031). Wave 1 has
realised about £210k a year (16 % of MAVIS batch load retired, 24 Sep 2028).

Suggested wording, which we'd be glad to sign:
  "Lodestar is on track to remove MAVIS's mainframe cost of £1.9m a year when all
   waves complete; wave 1 has already realised about £210k a year and retired 16 %
   of the batch load."
Calculation and sources attached (mainframe cost model, batch statistics Oct–Dec).
Ines

Reply, 19:40: "Use your wording. R."
"""),
    contract=dict(side="the clause behind the refusal", doc="Lodestar SOW · §14.3", date="signed 30 June 2027", stamp="refused",
                  clauses=[("14.3", "Each Party shall ensure information it provides for the other's governance is accurate.", "a signature under £1.9m “realised” would breach this clause, and something much older than it."),
                           ("Wrenfield code of conduct, 2.1", "We do not sign, certify or present information we know or suspect to be inaccurate.", "Graham's own code. I'd have reminded him, if needed.")],
                  plain="an accuracy clause in the contract gives you a neutral, professional reason to refuse, so the conversation is about the clause and not about anyone's honesty."),
    health=dict(now="a",
                g=("the client accepts the accurate version", ["Thank them.", "Sign the true wording.", "Move on."]),
                a=("a sponsor under pressure", ["Private, same day.", "An accurate version that helps.", "In writing."]),
                r=("the client insists", ["Escalate inside your firm.", "Decline to sign, in writing.", "Take advice; consider protected routes."])),
    pressure=dict(level=5, title="the numbers", cost="£9m of phase 2 in the balance · one email at 17:12",
                  items=["Deciding not to sign takes a minute. Saying it to the person who decides your next contract takes nerve. Do it the same day, before the nerve goes.", "Most people who ask this take the accurate version. Offer it generously."]),
    baseline="Each line compares <b>signing “£1.9m realised”</b> with <b>refusing privately, offering an accurate version, and putting both in writing</b>.",
    ratings=[(3, 5, "Rupert's board paper is true, and still a good story."),
             (3, 3, "A hard afternoon."),
             (3, 3, "Neutral, as it turned out."),
             (3, 3, "Neutral."),
             (3, 4, "The benefits model stays honest."),
             (1, 5, "No false statement to a board."),
             (2, 5, "Refusal, wording and sources in writing."),
             (4, 4, "Two hours, start to finish."),
             (4, 4, "Nothing to keep up.")],
    pitfalls=[("Signing to keep the peace", "Your name under a false number.", "don't sign."),
              ("Refusing in public", "The sponsor loses face; the fight starts.", "privately, same day."),
              ("Refusing without an alternative", "They have to write something.", "offer an accurate version."),
              ("Not writing it down", "Later, nobody remembers you refused.", "an email with sources."),
              ("Waiting", "The paper goes to print.", "the same day.")],
    grimoire=[(8, "dark-pact", "The Dark Pact", "is the same request, inside MetroVolt, eighteen months later: Rupert asks Pip to show £14m instead of £9m. Pip refuses with an email at 17:12."), (8, "whistle-of-last-resort", "The Whistle of Last Resort", "is what to do if the refusal isn't enough.")],
    use=["Anyone asks you to state, sign or present something untrue.", "Benefits, progress or test results are being “rounded up”.", "Your signature is wanted to make a claim look independent."],
    skip=["Never skip it."],
    related=["<b>What If an Executive Wants a Slide?</b> (this volume)", "<b>How Do We Protect the Margin?</b> (vol. 4)", "<b>Why Is Everything Green Except the Truth?</b> (vol. 4)", "<b>What Do We Do with What We Overhear?</b> (previous note)"],
    quiz=[("What did Rupert ask Ines to sign?", "“Lodestar has realised £1.9m a year of mainframe savings.”"),
          ("What was true?", "About £210k a year realised after wave 1; £1.9m a year when all waves complete."),
          ("What four things did Ines do?", "Refused privately the same day, offered accurate wording, put both in writing, and didn't sign."),
          ("What would she have done if Rupert insisted?", "Told Graham, cited the accuracy clause, declined to sign in writing, and taken advice if needed."),
          ("Why offer an accurate version?", "It meets the client's need without the falsehood; most people take it.")],
    quiz_sit=[("Graham, hearing about it, says: “Couldn't you have just let him write it without our signature?” What does Ines answer?", "That's the client's paper and the client's responsibility, but Wrenfield would still have known the board was misled about our work. Offering the true wording was the right outcome, and it worked.")],
    try_it="Think of a number you've been asked to “present positively”. Write the accurate version that still meets the need. Then write the short email you'd send if asked to sign the inaccurate one.",
    remember="Refuse the false number <span class=\"hl\">the same day</span>, offer <span class=\"hl\">a true one that helps</span>, and put both in writing. Never sign.",
    late=dict(when="Tue 16 January 2029 · 22:00 · hotel near The Grid",
              lines=["Rupert wanted “£1.9m realised” with our signature. It's £210k. I said no in his office at 16:20 and in writing at 17:12.",
                     "19:40: “Use your wording. R.” I read it four times.",
                     "If he'd said no, we'd have lost phase 2 and kept everything that matters. I'm glad I didn't have to find out how that felt."]),
    sources=["Institute of Business Ethics, <i>Speak Up</i> guidance.",
             "UK Financial Reporting Council, guidance on fair, balanced and understandable reporting.",
             "Mary Gentile, <i>Giving Voice to Values</i> (2010)."],
)

# ------------------------------------------------------------------ 15 How Do We Build a Champion?
bc_problem = Doodle(760, 240, "Doodle of phase 2's coming evaluation panel, January 2029: Rupert as decider, Desmond running it, Hollis, Nkem, Gareth, and Elaine. Vexmoor has Rupert's ear. Wrenfield has nobody on the panel who will speak for it from their own experience, unless someone chooses to.",
                    "Phase 2's panel. Vexmoor has Rupert's ear. Who speaks from experience?", exact=True)
for i, n in enumerate(["Rupert", "Desmond", "Hollis", "Nkem", "Gareth", "Elaine"]):
    bc_problem.box(14 + i * 124, 60, 114, 60, n, "y" if n == "Elaine" else "paper", size=17)
bc_problem.note(380, 170, "a champion can't be bought, asked or flattered", "red", size=19)

bc_how = Doodle(760, 330, "How champions were made on Lodestar, over eighteen months. Evidence they can repeat: the 31 per cent story, zero wrong bills, the honest change request. Credit they can share: their teams named on every success. Promises kept where they could see them. And what never to do: ask a champion to lobby, leak, or bend a procurement. By January, Elaine, Rosa and Gareth would each say, unprompted, what Wrenfield did. That's all a champion is.",
                "Evidence they can repeat, credit they can share, promises they've watched kept. Never ask them to lobby.", exact=True)
for i, (h, sub, fill) in enumerate([("evidence", "stories they can repeat", "green"), ("credit", "their teams named", "green"), ("promises", "kept where they saw", "green")]):
    bc_how.box(14 + i * 250, 20, 232, 100, h, fill, sub=sub, size=21, subsize=15)
bc_how.box(14, 150, 732, 70, "never ask a champion to lobby, leak, or bend a procurement", "pink", size=18)
bc_how.note(380, 280, "by January: Elaine, Rosa and Gareth would each say it, unprompted", "pen", size=18)

CHAMPION = dict(
    slug="building-a-champion", date=date(2029, 1, 26), meta=on_site(date(2029, 1, 26)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. client champions and advocates",
    tldr="A champion is someone on the client side who will speak for you, from their own experience, when you're not in the room. You can't buy, ask or flatter one into existence. You make them over months with <b>evidence they can repeat</b>, <b>credit they can share</b> and <b>promises they've watched you keep</b>. And you protect them: <b>never ask a champion to lobby, leak, or bend a procurement</b>. If they speak for you, it must be because it's true.",
    chips=[("Family", "integrity under pressure"), ("Lives in", "the eighteen months before it"), ("Pairs with", "liked or trusted, the phase 2 bid (vol. 6)")],
    problem_side="The Grid, January 2029",
    problem="""  <p class="lead">Phase 2's tender opens in March. The panel will be <b>Rupert</b> (decider), <b>Desmond</b> (running it), <b>Hollis</b>, <b>Nkem</b>, <b>Gareth</b> and <b>Elaine</b>. Vexmoor has advised Rupert for two years.</p>
  <ul>
    <li>Vivian asks Ines to “have a quiet word” with Elaine about putting in a good word with Rupert.</li>
    <li>Graham asks whether Gareth could be “brought onside” before the tender.</li>
    <li><span class="hl-pink">Both requests would put good people in a terrible position.</span></li>
  </ul>""",
    problem_figs=[bc_problem],
    sides=dict(client=("Elaine", "<p>Elaine has worked beside Wrenfield for eighteen months and trusts it more than any supplier she's known. She'll be on the panel. She must score fairly, declare any conflict, and be able to look Desmond in the eye. A “quiet word” request would force her to choose between her integrity and a supplier she likes.</p>", "I'll say what's true when asked. Don't ask me for more."),
                vendor=("Ines", "<p>Ines knows Wrenfield has champions: Elaine, Rosa, and (surprisingly) Gareth. They became champions because of evidence, credit and kept promises. Asking them to lobby would turn that into something cheaper, and might get Wrenfield excluded.</p>", "Champions are made by the work. Then you leave them alone.")),
    sides_after="A champion who lobbies for you is a liability. A champion who simply tells the truth about you is the strongest asset a vendor can have.",
    analogy_side="the teacher's reference",
    analogy="""  <p>A student doesn't ask her teacher to “put in a good word” with a university. She works hard for two years, and when the university asks the teacher for a reference, the teacher writes, from <b>her own experience</b>, what the student did. A reference the student had pushed for would be worth less, and the teacher would resent it.</p>""",
    map=[("Two years of hard work", "Eighteen months of Lodestar"),
         ("The teacher's own experience", "Elaine's, Rosa's, Gareth's"),
         ("The university asks", "The panel evaluates, under its rules"),
         ("“Put in a good word”", "Vivian's “quiet word”"),
         ("A pushed reference is worth less", "A lobbying champion is a liability")],
    how_side="evidence, credit, kept promises, and never asking for more",
    how="""  <p>Looking back over eighteen months, Ines writes down what made Wrenfield's champions:</p>
  <ul>
    <li><b>Evidence they can repeat</b>: stories that are short, true and checkable. Elaine tells the 31 % story herself now: “they told us before we found out”. Rosa tells the defect triage story. Gareth tells the meter data service story.</li>
    <li><b>Credit they can share</b>: every success named their teams first: the exception desk on the board slide, Network Assets on the meter service, Rosa's testers in the go / no-go minutes.</li>
    <li><b>Promises they've watched kept</b>: the access tracker, the promises checklist, “no told-you-so” about MetroBus.</li>
  </ul>
  <p>And she writes down what never to do. She declines Vivian's and Graham's requests the same day: <b>“We don't ask anyone at MetroVolt to speak for us. If they're asked, they'll say what's true.”</b> In February Desmond asks every panel member to declare relationships with bidders; Elaine declares eighteen months of working with Wrenfield, and Desmond records that she'll score with a second marker. That's how it should work.</p>""",
    how_figs=[bc_how],
    steps=[("Do work worth talking about", "There's no shortcut."),
           ("Give people short, true stories", "With numbers they can check."),
           ("Share the credit", "Their teams first, always."),
           ("Keep promises where they can see", "Lists, trackers, dates."),
           ("Never ask a champion to lobby", "Or leak, or bend a procurement."),
           ("Let procurement rules protect them", "Declarations, second markers.")],
    vocab=[("Champion", "Someone on the client side who speaks for you from their own experience."),
           ("Advocacy", "Speaking up for someone; worthless if requested."),
           ("Declaration of interest", "Stating a relationship that might affect a decision."),
           ("Second marker", "Another evaluator who checks a panel member's scores."),
           ("Lobbying", "Trying to influence a decision outside its proper process."),
           ("Reputation", "What people say about you when you're not there.")],
    code=dict(file="notebook/champions-2029-01.md", note="Ines's notebook · Fri 26 Jan 2029 (private)", src="""
CHAMPIONS · what made them, and what we never ask

Elaine   story: "they told us about the 31 % before we found it" · seen: 34 mornings of
         the access tracker · credit: Customer Ops named on every success
Rosa     story: the triage board ("now my testers know what to write")
Gareth   story: the meter data service (his, on every slide since Nov)

never ask anyone at MetroVolt to: speak for us · share anything about phase 2 ·
         bend a procurement rule
declined (26 Jan): Vivian's "quiet word" · Graham's "bring Gareth onside"
Feb: Desmond's declarations · Elaine declares 18 months with Wrenfield → second marker
"""),
    contract=dict(side="the rule that protects champions", doc="Phase 2 ITT (draft) · §6.7 and §8.2", date="to be published 5 Mar 2029", stamp="hands off",
                  clauses=[("6.7", "Bidders may not contact MetroVolt staff about this procurement except through the clarification process.", "from 5 March, a “quiet word” isn't just unwise. it's exclusion."),
                           ("8.2", "Evaluators shall declare any relationship with a bidder; MetroVolt may assign a second marker.", "Elaine's declaration protects her and us.")],
                  plain="procurement rules exist partly to protect the client's staff from suppliers who'd ask them for favours. Respecting them is how you keep your champions."),
    health=dict(now="g",
                g=("champions already", ["Leave them alone during procurements.", "Keep doing the work.", "Thank them after."]),
                a=("no champions yet", ["Evidence, credit, kept promises.", "Months, not weeks.", "No shortcuts."]),
                r=("a hostile client", ["Champions are rare; do the work anyway.", "Let results speak.", "Never buy advocacy."])),
    pressure=dict(level=3, title="the temptation to ask", cost="two declined requests from your own side",
                  items=["Asking a friend at the client for help feels natural before a big bid. It's the fastest way to lose them.", "Trust the eighteen months. If they speak for you, it'll be because it's true."]),
    baseline="Each line compares <b>asking friends at the client to put in a good word</b> with <b>earning champions through evidence, credit and kept promises, and never asking</b>.",
    ratings=[(3, 5, "Elaine, Rosa and Gareth speak from experience."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 5, "No exclusion risk; champions protected."),
             (3, 4, "Declarations made properly."),
             (2, 2, "Eighteen months."),
             (4, 4, "Nothing to keep up but the work.")],
    pitfalls=[("Asking for a good word", "Puts your champion in a terrible position.", "never ask."),
              ("Flattery", "Seen through, and resented.", "evidence and credit."),
              ("Taking the credit", "Nobody repeats your stories.", "their teams first."),
              ("Contact during procurement", "Exclusion.", "the clarification process only."),
              ("Champions of one", "One move and they're gone.", "several, at different levels.")],
    grimoire=[(4, "sponsors-mark", "The Sponsor's Mark", "is the same idea inside MetroVolt: someone who says your name in rooms you're not in.")],
    use=["Before any decision you'll be judged on.", "Any long engagement.", "When your firm wants to “work the relationships”."],
    skip=["Never skip the work; always skip the asking."],
    related=["<b>Do They Like Us, or Trust Us?</b> (this volume)", "<b>How Do We Bid Against the Rival for the Next Phase?</b> (vol. 6)", "<b>Who Will Vouch for Us?</b> (vol. 1)", "<b>How Do We Earn the Programme Director's Trust?</b> (vol. 2)"],
    quiz=[("What is a champion?", "Someone on the client side who speaks for you from their own experience."),
          ("What three things make champions?", "Evidence they can repeat, credit they can share, promises they've watched kept."),
          ("What must you never ask a champion?", "To lobby, leak, or bend a procurement."),
          ("What did Elaine do in February?", "Declared her eighteen months with Wrenfield; Desmond assigned a second marker."),
          ("Why is a lobbying champion a liability?", "It compromises them and can get the bidder excluded.")],
    quiz_sit=[("Gareth offers, unprompted, to “mention Wrenfield's work to Rupert” before the tender. What does Ines say?", "Thank him warmly, and say that with the tender coming it's best if he says only what he'd say if asked, through the proper process. That protects him.")],
    try_it="Think of someone who'd speak for you from experience. What story would they tell? Now write the stories you'd want people to tell about your current work, and what you'd need to do to earn them.",
    remember="Champions are made by <span class=\"hl\">the work</span>, then <span class=\"hl\">left alone</span>. Never ask them for more than the truth.",
    late=dict(when="Fri 26 January 2029 · 21:15 · hotel near The Grid",
              lines=["Vivian wanted a quiet word with Elaine. Graham wanted Gareth “onside”. Declined both before lunch.",
                     "Elaine tells the 31 % story herself now. “They told us before we found out.” That's the whole bid, really.",
                     "Phase 2 opens in five weeks. Hana's tired. So am I. Next volume, apparently, is about that."]),
    sources=["David Maister, Charles Green and Robert Galford, <i>The Trusted Advisor</i> (2000).",
             "Crown Commercial Service, guidance on conflicts of interest for evaluators.",
             "Robert Cialdini, <i>Influence</i> (rev. ed., 2021): social proof."],
)

NOTES = [OVERHEAR, CHANGE_NUMBERS, CHAMPION]
