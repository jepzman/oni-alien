# Series 5 · On the Client's Floor · Vol. 5 · Other People's Politics · Holding your ground (notes 5–8).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 05 How Do We Say No to a Client?
sn_problem = Doodle(760, 240, "Doodle of a request from Rupert's office on 2 October 2028, one week into hypercare: start designing wave 2 now, in parallel with hypercare, as goodwill, at no cost, so the phase 2 tender can say design is already under way. Wave 2 isn't contracted. Hypercare needs the whole team.",
                    "“Start wave 2 now, in parallel, as goodwill.” Not contracted, not paid, not possible.", exact=True)
sn_problem.box(150, 30, 460, 110, "“start wave 2 design now”", "pink", sub="free · parallel with hypercare", size=21, subsize=16)
sn_problem.box(14, 170, 360, 50, "hypercare: whole team", "y", size=17)
sn_problem.box(386, 170, 360, 50, "wave 2: not contracted", "paper", size=17)

sn_how = Doodle(760, 330, "The no-but. No to the request: no free design work, and none during hypercare. Yes to the need: Rupert's real need is a phase 2 tender that looks ready. What Wrenfield offers: a two-week paid planning sprint after hypercare ends, from the change pool, producing a wave 2 readiness pack that MetroVolt can give every bidder. Written in one email, with the reason in one sentence.",
                "No to the request, yes to the need, and an offer they can say yes to.", exact=True)
sn_how.box(14, 20, 230, 110, "no", "pink", sub="free work · during hypercare", size=26, subsize=14)
sn_how.box(264, 20, 230, 110, "the need", "y", sub="a tender that looks ready", size=21, subsize=14)
sn_how.box(514, 20, 232, 110, "the offer", "green", sub="2-week paid sprint, Dec", size=21, subsize=14)
sn_how.box(14, 160, 732, 70, "a wave 2 readiness pack, given to every bidder", "blue", sub="so it can't be seen as an advantage for Wrenfield", size=18, subsize=14)
sn_how.note(380, 290, "one email · the reason in one sentence", "pen", size=18)

SAYING_NO = dict(
    slug="saying-no", date=date(2028, 10, 2), meta=on_site(date(2028, 10, 2)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. the “no, but”",
    tldr="Saying no to a client is part of serving them, if you do it well. Say <b>no to the request</b>, <b>yes to the need</b> behind it, and make an <b>offer</b> they can say yes to. Give the <b>reason in one sentence</b>, and put it <b>in writing</b>. Free work to win future work is the most expensive gift a vendor can give, especially when it compromises a fair procurement.",
    chips=[("Family", "holding your ground"), ("Lives in", "email to Elaine, 2 Oct 2028 · CR-021"), ("Pairs with", "the honest change request (vol. 3), gifts and the register")],
    problem_side="The Grid, 2 October 2028",
    problem="""  <p class="lead">One week into hypercare, Rupert's office asks Elaine to ask Ines: could Wrenfield <b>start designing wave 2 now</b>, in parallel with hypercare, “as goodwill”, at no cost? The phase 2 tender in March could then say “design already under way”.</p>
  <ul>
    <li>Wave 2 isn't contracted. Phase 2 will be tendered, and Vexmoor will bid.</li>
    <li>Hypercare has the whole team on 380,000 newly moved customers. <span class="hl-pink">Hana is still working weekends.</span></li>
    <li>Graham, from Leeds: “Do it. It'll help us win phase 2.”</li>
  </ul>""",
    problem_figs=[sn_problem],
    sides=dict(client=("Rupert's office", "<p>Rupert wants Ascend to look fast. A tender that says “design already under way” sounds like momentum. Asking the current supplier for goodwill work is normal; most say yes, hoping to win.</p>", "Show some goodwill. You want phase 2, don't you?"),
                vendor=("Ines", "<p>Free design work would take people off hypercare, cost money Wrenfield won't recover, and, worst, give Wrenfield an unfair head start in a tender: Desmond would have to exclude it or share it. A yes would hurt everyone it was meant to help.</p>", "A yes here is bad for hypercare, bad for margin and bad for the tender.")),
    sides_after="Goodwill work is never free. Someone pays: your team, your margin, or the fairness of the next procurement.",
    analogy_side="the doctor and the prescription",
    analogy="""  <p>A patient asks a doctor for antibiotics for a cold. A good doctor says no to the <b>prescription</b> and yes to the <b>need</b> (feeling better, getting back to work), explains why in a sentence, and offers what will actually help. The patient leaves without what they asked for, and better looked after.</p>""",
    map=[("Antibiotics for a cold", "Free wave 2 design during hypercare"),
         ("The need: feeling better", "A tender that looks ready"),
         ("Why, in a sentence", "“It would compromise hypercare and the tender's fairness.”"),
         ("What will actually help", "A paid two-week readiness sprint in December"),
         ("Better looked after", "A readiness pack for every bidder")],
    how_side="no to the request, yes to the need, an offer",
    how="""  <p><b>Find the need.</b> Ines asks Elaine one question: “What does Rupert need the tender to show?” Answer: that phase 2 is <b>ready to start</b> in May, not in October.</p>
  <p><b>Say no to the request, with the reason in one sentence.</b> Her email to Elaine: <i>“We can't start wave 2 design during hypercare, or for free: it would take people off 380,000 newly moved customers, and it would give us an advantage in the phase 2 tender that Desmond would have to exclude.”</i></p>
  <p><b>Say yes to the need, with an offer.</b> <i>“What we can do: a two-week planning sprint in early December, after hypercare ends, paid from the change pool (£42k), producing a wave 2 readiness pack (data profile for wave 2's districts, lessons from wave 1, a migration timeline) that MetroVolt owns and gives to every bidder.”</i></p>
  <p>Desmond is delighted: a readiness pack for all bidders makes the tender stronger and fairer. Rupert approves CR-021. Graham isn't delighted; Ines explains that the pack goes to Vexmoor too, which is exactly why it doesn't disqualify Wrenfield.</p>""",
    how_figs=[sn_how],
    steps=[("Ask what the need is", "Behind the request."),
           ("Say no to the request", "Clearly, without hedging."),
           ("Give the reason in one sentence", "About them, not you."),
           ("Make an offer that meets the need", "Specific, priced, dated."),
           ("Put it in writing", "One short email."),
           ("Check the offer is fair to others", "Especially near a procurement.")],
    vocab=[("No, but", "Refusing a request while offering something that meets the need."),
           ("Goodwill work", "Free work offered to please a client, often hoping for future business."),
           ("Unfair advantage", "Knowledge or work one bidder has that others don't."),
           ("Readiness pack", "Material given to all bidders so they start equal."),
           ("Need versus request", "What someone wants underneath what they ask for."),
           ("Exclusion", "Removing a bidder from a procurement because of a conflict or advantage.")],
    code=dict(file="email/2028-10-02-wave2-request.md", note="Ines to Elaine · Mon 2 Oct 2028, 16:10", src="""
Subject: Wave 2 design request

Elaine,
We can't start wave 2 design during hypercare, or for free: it would take people
off 380,000 newly moved customers, and it would give us an advantage in the
phase 2 tender that Desmond would have to exclude.

What we can do: a two-week planning sprint, 4–15 Dec (after hypercare), from the
change pool (≈ £42k, CR-021), producing a wave 2 readiness pack owned by MetroVolt:
  • data profile for wave 2's districts  • wave 1 lessons  • a migration timeline
MetroVolt can give the pack to every phase 2 bidder, including us.

Happy to talk it through on Thursday.
Ines
"""),
    contract=dict(side="why free work would have been a problem", doc="Lodestar SOW · §7 and the phase 2 procurement rules", date="Oct 2028", stamp="no, but",
                  clauses=[("7.6", "No Change is binding unless recorded in the Change Register and approved under this clause.", "free work outside the register isn't goodwill. it's an untracked change."),
                           ("Phase 2 ITT (draft), 3.2", "Information provided to one bidder about the requirement shall be provided to all bidders.", "Desmond's rule. the readiness pack follows it.")],
                  plain="free work near a procurement can create an unfair advantage the client must remove. Offering paid work that produces something every bidder receives keeps the tender fair and your bid eligible."),
    health=dict(now="g",
                g=("trust is high", ["A quick “no, but” conversation.", "The offer usually lands.", "Write it down anyway."]),
                a=("pressure from a new sponsor", ["One-sentence reason about them.", "A priced offer.", "Fair to other bidders."]),
                r=("the client insists", ["Restate in writing.", "Escalate the trade-off, not the person.", "Never do untracked work."])),
    pressure=dict(level=3, title="saying no to the new sponsor", cost="a disappointed managing director · a sponsor's first impression",
                  items=["Saying no to a new sponsor in his first month feels risky. A thoughtful no with an offer is a better first impression than a tired yes.", "Graham's “it'll help us win” is the trap: it would have got Wrenfield excluded."]),
    baseline="Each line compares <b>free wave 2 design during hypercare</b> with <b>a clear no, a paid sprint after hypercare, and a pack for every bidder</b>.",
    ratings=[(3, 4, "Desmond and Rupert get something better than asked."),
             (2, 4, "Hypercare stays fully staffed."),
             (1, 4, "Paid, from the pool."),
             (3, 4, "The sprint's outputs are defined."),
             (3, 3, "Neutral."),
             (2, 4, "No procurement conflict for phase 2."),
             (3, 4, "Email and CR-021 on file."),
             (3, 3, "A day to agree."),
             (4, 4, "Nothing to keep up.")],
    pitfalls=[("A tired yes", "Free work, burned team, procurement risk.", "no to the request, yes to the need."),
              ("A bare no", "The client feels refused.", "an offer that meets the need."),
              ("Reasons about you", "“We're too busy.”", "reasons about them: their customers, their tender."),
              ("A verbal no", "Forgotten, or misquoted.", "one short email."),
              ("Ignoring fairness", "Your bid gets excluded.", "something every bidder receives.")],
    grimoire=[(8, "word-of-power-no", "The Word of Power: No", "is the same skill inside MetroVolt: declining work without career damage.")],
    use=["Requests for free or out-of-scope work.", "Requests during critical phases.", "Anything near a procurement."],
    skip=["The request is small, in scope and harmless: just do it, and record it."],
    related=["<b>How Do We Change the Deal Without a War?</b> (vol. 2)", "<b>Can We Take the Client to the Football?</b> (this volume)", "<b>How Do We Bid Against the Rival for the Next Phase?</b> (vol. 6)", "<b>Where Did This Extra Work Come From?</b> (vol. 4)"],
    quiz=[("What are the three parts of a “no, but”?", "No to the request, yes to the need, an offer."),
          ("What was Rupert's real need?", "A phase 2 tender that looks ready to start."),
          ("Why would free design work have hurt Wrenfield's bid?", "It's an unfair advantage Desmond would have to remove, possibly by excluding Wrenfield."),
          ("What was offered instead?", "A paid two-week sprint after hypercare, producing a readiness pack for every bidder."),
          ("Why should the reason be about them?", "It's more persuasive and more honest than “we're busy”.")],
    quiz_sit=[("Rupert replies: “Fine, but could your team at least share their wave 2 ideas informally with my office?” What do you say?", "Not informally: anything shared about phase 2 should go into the readiness pack so all bidders see it. Offer to include their questions in the sprint.")],
    try_it="Think of a request you said yes to and regretted. Write the “no, but” you could have sent: the need, the no, the reason in one sentence, and an offer.",
    remember="No to <span class=\"hl\">the request</span>, yes to <span class=\"hl\">the need</span>, and an offer they can say yes to.",
    late=dict(when="Mon 2 October 2028 · 21:20 · hotel near The Grid",
              lines=["Rupert's first request as our sponsor-to-be, and I said no. With an offer.",
                     "Desmond loved the readiness pack. Graham didn't. Graham will, when we're not excluded in March.",
                     "Hana asked if she'd have to work on wave 2 during hypercare. No. That was half the reason."]),
    sources=["William Ury, <i>The Power of a Positive No</i> (2007).",
             "Roger Fisher and William Ury, <i>Getting to Yes</i> (1981).",
             "Crown Commercial Service, guidance on pre-market engagement and equal treatment."],
)

# ------------------------------------------------------------------ 06 Do They Like Us, or Trust Us?
lt_problem = Doodle(760, 240, "Doodle of two kinds of relationship. Customer Ops loves the Wrenfield team: Callum brings cake on Fridays, Lottie knows everyone's name. Rupert's office doesn't trust Wrenfield's numbers: Vexmoor's assurance notes have taught it to check everything twice. A thermometer for liked, full. One for trusted, half.",
                    "Liked by the floor. Not yet trusted by the top.", exact=True)
lt_problem.box(80, 40, 120, 160, None, "paper", rx=40)
lt_problem.box(96, 60, 88, 124, None, "pink", rx=30)
lt_problem.note(140, 226, "liked", "pen", size=19)
lt_problem.box(300, 40, 120, 160, None, "paper", rx=40)
lt_problem.box(316, 124, 88, 60, None, "y", rx=30)
lt_problem.note(360, 226, "trusted", "pen", size=19)
lt_problem.box(480, 60, 266, 120, "Rupert's office", "y", sub="checks every number twice", size=19, subsize=15)

lt_how = Doodle(760, 320, "What builds trust, from the trust equation: credibility, are the numbers right; reliability, do we do what we said; intimacy, can they tell us bad news; divided by self-orientation, are we in it for ourselves. Wrenfield's actions: every number with its source; a promises list Rupert's office can check; bad news first; and saying no to work that only helps Wrenfield.",
                "Trust = (credibility + reliability + intimacy) ÷ self-orientation.", exact=True)
for i, (h, sub, fill) in enumerate([("credibility", "numbers with sources", "green"), ("reliability", "promises, checkable", "green"), ("intimacy", "bad news first", "green")]):
    trust_x = 14 + i * 186
    lt_how.box(trust_x, 20, 174, 100, h, fill, sub=sub, size=19, subsize=14)
lt_how.box(572, 20, 174, 100, "÷ self-interest", "pink", sub="no to self-serving work", size=17, subsize=14)
lt_how.box(14, 150, 732, 70, "cake is nice. a number that's right every time is trust.", "y", size=18)
lt_how.note(380, 280, "after 3 months: Rupert's office stopped re-checking the weekly figures", "pen", size=17)

LIKED_TRUSTED = dict(
    slug="liked-or-trusted", date=date(2028, 10, 13), meta=on_site(date(2028, 10, 13)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. likeability and trust",
    tldr="Being liked and being trusted are different things, and vendors often confuse them. <b>Liked</b> opens doors: people answer your calls. <b>Trusted</b> keeps them open when things go wrong: people believe your numbers. Trust comes from <b>credibility</b> (right numbers), <b>reliability</b> (kept promises), <b>intimacy</b> (they can tell you bad news), and low <b>self-interest</b>. Build trust deliberately; liking usually follows.",
    chips=[("Family", "holding your ground"), ("Lives in", "delivery/lodestar/promises-checklist.md"), ("Pairs with", "the client counterpart (vol. 2), the watermelon report (vol. 4)")],
    problem_side="The Grid, October 2028",
    problem="""  <p class="lead">Customer Operations <b>loves</b> the Wrenfield team. Callum brings cake on Fridays. Lottie knows the exception desk's children's names. Bert has asked Lottie to his retirement party in March.</p>
  <ul>
    <li><b>Rupert's office</b>, Lodestar's new home, re-checks every Wrenfield figure. Vexmoor's assurance notes have taught it to.</li>
    <li>On 13 October Rupert's analyst asks for the source of every number in the weekly status, “for assurance”.</li>
    <li>Callum is hurt: <span class="hl-pink">“Everyone here likes us.”</span> Not everyone who decides phase 2.</li>
  </ul>""",
    problem_figs=[lt_problem],
    sides=dict(client=("Rupert's analyst", "<p>Rupert's office has heard two years of Lodestar history through Vexmoor. It doesn't dislike Wrenfield; it doesn't know Wrenfield. Its job is to check, and it can't check “the team is lovely”.</p>", "Liking you isn't my job. Checking you is."),
                vendor=("Ines and Callum", "<p>Callum built goodwill on the floor, and it's real and valuable. But phase 2 will be decided by people who weren't there for the cake. Ines needs trust that survives a hostile reading: numbers with sources, promises anyone can check.</p>", "Cake for the floor. Sources for the top.")),
    sides_after="Liking is about how you make people feel. Trust is about whether they can rely on what you say when you're not in the room.",
    analogy_side="the friendly mechanic and the honest one",
    analogy="""  <p>You might like the mechanic who chats and gives you coffee. You <b>trust</b> the one who shows you the worn part, tells you what can wait, and whose estimate is right every time. The best mechanics are both, and when you have to choose, you take your car to the one you trust.</p>""",
    map=[("Coffee and a chat", "Cake on Fridays"),
         ("Showing you the worn part", "Every number with its source"),
         ("The estimate that's always right", "Promises kept, checkably"),
         ("“This can wait”", "Saying no to work that only helps Wrenfield"),
         ("Where you take your car", "Who wins phase 2")],
    how_side="credibility, reliability, intimacy, low self-interest",
    how="""  <p>Ines uses the <b>trust equation</b> from <i>The Trusted Advisor</i> as a checklist, not a slogan.</p>
  <ul>
    <li><b>Credibility</b>: from 20 October every number in the weekly status carries its <b>source</b> (report, query, date). Rupert's analyst can check any of them in a minute.</li>
    <li><b>Reliability</b>: a <b>promises checklist</b>, shared with Rupert's office: what Wrenfield said it would do in hypercare, by when, and whether it did. 31 of 31 kept by mid-November.</li>
    <li><b>Intimacy</b>: Rupert's analyst gets Ines's direct number and an invitation to ask anything. The first time she reports a data error, Ines thanks her publicly.</li>
    <li><b>Low self-interest</b>: the readiness-pack decision (the previous note) is the clearest proof: Wrenfield chose a fair tender over an advantage.</li>
  </ul>
  <p>Callum keeps bringing cake. By January, Rupert's analyst has stopped re-checking the weekly figures. She tells Elaine: “Their numbers are the only ones I don't have to.”</p>""",
    how_figs=[lt_how],
    steps=[("Ask who needs to trust you", "Not only who likes you."),
           ("Source every number", "Checkable in a minute."),
           ("Keep a visible promises list", "Done or not, by date."),
           ("Make it easy to bring you bad news", "And thank them when they do."),
           ("Show low self-interest", "Choose fairness over advantage, visibly."),
           ("Keep the warmth", "Liking still matters.")],
    vocab=[("Trust equation", "Trust = (credibility + reliability + intimacy) ÷ self-orientation."),
           ("Credibility", "Whether what you say is accurate."),
           ("Reliability", "Whether you do what you say."),
           ("Intimacy", "Whether people feel safe telling you difficult things."),
           ("Self-orientation", "How much you seem to act for yourself rather than the client."),
           ("Rapport", "A friendly connection; helpful, but not the same as trust.")],
    code=dict(file="delivery/lodestar/promises-checklist.md", note="shared with Rupert's office · from 20 Oct 2028", src="""
HYPERCARE PROMISES · checkable by anyone           31 made · 31 kept (to 17 Nov)

id    promise                                          by       status   evidence
H-01  exception queue < 200 by 6 Oct                   6 Oct    kept     report EQ-1006
H-07  every weekly figure with its source              20 Oct   kept     status #61 onward
H-12  daily reconciliation report to Elaine by 09:00   daily    kept     54 of 54 days
H-19  root cause for each sev 2 within 5 days          ongoing  kept     4 of 4
H-26  wave 1 lessons pack draft                        24 Nov   kept     lessons-v0.9
…
"""),
    contract=dict(side="the contract can require accuracy, not trust", doc="Lodestar SOW · §14.3 and Schedule 7", date="signed 30 June 2027", stamp="checkable",
                  clauses=[("14.3", "Each Party shall ensure information it provides for the other's governance is accurate.", "the minimum. trust is what you build on top."),
                           ("Sch. 7, 5.4", "<ins>Figures in the weekly status shall state their source.</ins>", "added on 20 Oct, at our suggestion.")],
                  plain="a contract can require accurate information; it can't make anyone trust you. Volunteering clauses that make your work checkable is one of the fastest ways to build trust."),
    health=dict(now="a",
                g=("liked and trusted", ["Keep both.", "Don't get casual with numbers.", "Stay checkable."]),
                a=("liked by some, doubted by others", ["Sources on every number.", "A visible promises list.", "Fairness over advantage."]),
                r=("distrusted", ["Evidence for everything.", "Small promises, kept visibly.", "Patience: it takes months."])),
    pressure=dict(level=2, title="being checked", cost="a hurt engagement manager · an extra column of sources",
                  items=["Being re-checked feels insulting. It's an invitation to prove something.", "Don't stop the cake. Liking still opens doors; it just doesn't keep them open."]),
    baseline="Each line compares <b>relying on being liked</b> with <b>sourced numbers, a visible promises list, safe bad news and low self-interest</b>.",
    ratings=[(2, 5, "“The only numbers I don't have to check.”"),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Errors found and thanked for."),
             (3, 4, "Figures checkable in a minute."),
             (2, 5, "Sources and promises on record."),
             (3, 3, "Three months to change minds."),
             (3, 3, "A sources column and a list to maintain.")],
    pitfalls=[("Confusing liked with trusted", "Surprised when the top doubts you.", "ask who needs to trust you."),
              ("Unsourced numbers", "Every figure re-checked.", "a source on each."),
              ("Hidden promises", "Nobody can see you keep them.", "a visible list."),
              ("Defensiveness about errors", "People stop telling you.", "thank them publicly."),
              ("Visible self-interest", "Every number looks like a sales pitch.", "choose fairness over advantage.")],
    grimoire=[(8, "reputation-hit-points", "Reputation Is Your Hit Points", "explains how trust is built, lost and healed inside MetroVolt.")],
    use=["New stakeholders who weren't there for the good times.", "Assurance or audit is checking your work.", "Before a competitive decision."],
    skip=["Never skip it."],
    related=["<b>How Do We Earn the Programme Director's Trust?</b> (vol. 2)", "<b>Why Is Everything Green Except the Truth?</b> (vol. 4)", "<b>How Do We Say No to a Client?</b> (previous note)", "<b>How Do We Build a Champion?</b> (this volume)"],
    quiz=[("What's the difference between liked and trusted?", "Liked: people want to work with you. Trusted: they rely on what you say."),
          ("What is the trust equation?", "(Credibility + reliability + intimacy) ÷ self-orientation."),
          ("What did Wrenfield add to every weekly figure?", "Its source."),
          ("What was on the promises checklist?", "Each hypercare promise, its date, whether kept, and evidence."),
          ("How did the readiness pack help trust?", "It showed low self-interest: fairness over advantage.")],
    quiz_sit=[("Rupert's analyst finds a wrong figure in the weekly status. What does Ines do?", "Thank her publicly, correct it the same day with the cause, and add a check so it can't recur. That turns one error into evidence of reliability.")],
    try_it="Score yourself on credibility, reliability, intimacy and self-interest with one stakeholder. Which is weakest? Pick one action that would raise it this month.",
    remember="Liked opens doors; <span class=\"hl\">trusted keeps them open</span>. Source every number, keep every promise <span class=\"hl\">where people can see</span>.",
    late=dict(when="Fri 13 October 2028 · 21:00 · hotel near The Grid",
              lines=["Callum: “Everyone here likes us.” Yes. Not the people deciding phase 2.",
                     "Every number gets a source from next week. It's tedious. It's the point.",
                     "Kept the cake. Some things work on everyone."]),
    sources=["David Maister, Charles Green and Robert Galford, <i>The Trusted Advisor</i> (2000).",
             "Stephen M. R. Covey, <i>The Speed of Trust</i> (2006).",
             "Frances Frei and Anne Morriss, “Begin with Trust”, <i>Harvard Business Review</i> (2020)."],
)

# ------------------------------------------------------------------ 07 Can We Take the Client to the Football?
gd_problem = Doodle(760, 240, "Doodle of Vivian's plan for December 2028: a hospitality box at a football match for Elaine, Desmond and Hollis, worth about 450 pounds a head, to say thank you for wave 1. The phase 2 tender opens in March. Desmond runs it.",
                    "A box at the football, £450 a head, for the people running the next tender.", exact=True)
gd_problem.box(150, 30, 460, 110, "football box · Dec 2028", "y", sub="Elaine · Desmond · Hollis · ≈ £450 each", size=20, subsize=15)
gd_problem.box(250, 170, 260, 50, "phase 2 tender: March", "pink", size=17)

gd_how = Doodle(760, 330, "The rules check. MetroVolt's gifts and hospitality policy: anything over 50 pounds must be declared in the register and approved; nothing at all from suppliers bidding in a live or planned procurement. Wrenfield's own policy says the same. Outcome: the football box is declined. Instead: a thank-you letter to Customer Ops' exception desk, copied to their director, and a team lunch Wrenfield pays for its own people.",
                "Know both policies, keep a register, and during a procurement, say no to everything but thank-you letters.", exact=True)
gd_how.box(14, 20, 360, 110, "MetroVolt policy", "paper", sub="> £50 declared · none from bidders", size=20, subsize=14)
gd_how.box(386, 20, 360, 110, "Wrenfield policy", "paper", sub="register · nothing during procurement", size=20, subsize=14)
gd_how.box(14, 160, 360, 70, "football box", "pink", sub="declined", size=20, subsize=15)
gd_how.box(386, 160, 360, 70, "thank-you letters", "green", sub="to the exception desk, cc their director", size=19, subsize=13)
gd_how.note(380, 290, "a gift that needs explaining isn't a gift", "pen", size=18)

GIFTS = dict(
    slug="gifts-and-dinners", date=date(2028, 12, 4), meta=on_site(date(2028, 12, 4)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. gifts, hospitality and the register",
    tldr="Hospitality can be a genuine thank-you or something that looks like a bribe, and the difference is often <b>timing</b>, <b>value</b> and <b>who's deciding what</b>. Know <b>both companies' policies</b>, keep a <b>register</b>, and during any procurement, offer <b>nothing</b> to the people involved beyond coffee. Thank people with words, in writing, copied to their boss. If a gift needs explaining, it isn't a gift.",
    chips=[("Family", "holding your ground"), ("Lives in", "Wrenfield gifts and hospitality register"), ("Pairs with", "saying no, the phase 2 bid (vol. 6)")],
    problem_side="Wrenfield and MetroVolt, December 2028",
    problem="""  <p class="lead">Vivian wants to say thank you for wave 1. Her plan: a <b>hospitality box at a football match</b> in December for Elaine, Desmond and Hollis, about <b>£450 a head</b>, with Graham and Ines.</p>
  <ul>
    <li>MetroVolt's <b>phase 2 tender</b> opens in March. <b>Desmond</b> runs it; Elaine and Hollis will be on the panel.</li>
    <li>Vivian: “It's just a thank-you. Everyone does it.”</li>
    <li><span class="hl-pink">Vexmoor's assurance team sits on the same floor and notices everything.</span></li>
  </ul>""",
    problem_figs=[gd_problem],
    sides=dict(client=("Desmond", "<p>Desmond would have to declare a £450 box, then explain to auditors why he accepted hospitality from a bidder three months before evaluating its bid. Saying yes would put him in a terrible position; saying no would feel rude. He'd rather not be asked.</p>", "Please don't put me in that position."),
                vendor=("Ines and Vivian", "<p>Vivian means it kindly. But a box for the tender panel from a bidder, months before the tender, is exactly what anti-bribery rules are written about. It could disqualify Wrenfield and embarrass three people who've been good to it.</p>", "A thank-you shouldn't need explaining to an auditor.")),
    sides_after="The question isn't “is it a bribe?” but “would it look like one to someone who doesn't know us?”",
    analogy_side="the referee and the club dinner",
    analogy="""  <p>A football club wants to thank a referee for a well-run season. It doesn't invite him to the directors' box the week before he referees their cup final. It sends a <b>letter</b>, copied to the referees' association, saying what he did well. The referee can frame it, and nobody has to wonder about the final.</p>""",
    map=[("The referee", "Desmond, Elaine and Hollis: the tender panel"),
         ("The directors' box before the final", "A football box before phase 2"),
         ("A letter, copied to the association", "A thank-you letter, copied to their director"),
         ("The cup final", "The phase 2 evaluation"),
         ("Nobody has to wonder", "Nothing to declare, nothing to explain")],
    how_side="both policies, a register, nothing during procurement",
    how="""  <p><b>Check both policies.</b> MetroVolt's: gifts and hospitality over <b>£50</b> must be declared and approved; <b>nothing</b> may be accepted from a supplier taking part in a live or planned procurement. Wrenfield's own policy (written after the UK Bribery Act guidance): register everything offered or received; no hospitality to people involved in a procurement Wrenfield is bidding in.</p>
  <p><b>Decide.</b> Phase 2 is a planned procurement; the three guests are on its panel. The box is <b>declined</b>, by Ines, with Graham's agreement, before anyone at MetroVolt is asked.</p>
  <p><b>Thank people properly instead.</b> Ines writes <b>thank-you letters</b>: to Customer Ops' exception desk (who worked through the night and Sunday), to MetroVolt IT's on-call team, to Bert. Each is specific, and copied to the person's director. Wrenfield pays for its <b>own team's</b> lunch. Elaine gets nothing but a card. She pins it to her screen.</p>
  <p><b>Keep the register.</b> Everything offered or received goes in it, including the box that wasn't, with the reason it wasn't.</p>""",
    how_figs=[gd_how],
    steps=[("Read both companies' policies", "Thresholds, approvals, procurement rules."),
           ("Check timing", "Is a procurement live or planned?"),
           ("Check who decides what", "Are guests on a panel?"),
           ("When in doubt, don't", "Decide before asking the client."),
           ("Thank with words", "Specific, written, copied to their boss."),
           ("Register everything", "Offered, received, declined.")],
    vocab=[("Hospitality", "Entertainment, meals or events offered to business contacts."),
           ("Gifts register", "A record of gifts and hospitality offered and received."),
           ("Anti-bribery policy", "Rules preventing improper influence through gifts or payments."),
           ("Conflict of interest", "When personal benefit could influence a professional decision."),
           ("Procurement freeze", "A period when contact and hospitality with bidders are restricted."),
           ("Proportionality", "Whether hospitality is reasonable in size and purpose.")],
    code=dict(file="register/gifts-2028-12.md", note="Wrenfield gifts and hospitality register · Dec 2028", src="""
GIFTS & HOSPITALITY REGISTER · Lodestar · December 2028

date    offered by   to                          what                 value    decision
04 Dec  Wrenfield    Elaine, Desmond, Hollis     football box         ≈ £1,350 DECLINED
        reason: phase 2 procurement planned (Mar 2029); guests on the panel
05 Dec  Wrenfield    exception desk (12), MV IT  thank-you letters,   £0       sent
                     on-call (6), Bert           cc their directors
12 Dec  Halvorsen    Ines                        tin of biscuits      ≈ £12    accepted,
                                                                               shared on 19
15 Dec  Wrenfield    Wrenfield team (8)          team lunch           £360     own team
"""),
    contract=dict(side="what the contract and the law expect", doc="Lodestar SOW · §15 (anti-bribery) · MetroVolt supplier code", date="signed 30 June 2027", stamp="declined",
                  clauses=[("15.1", "The Supplier shall comply with applicable anti-bribery laws and MetroVolt's Supplier Code of Conduct, including its gifts and hospitality rules.", "the code says: nothing from a bidder during a planned procurement."),
                           ("15.3", "Breach of this clause entitles MetroVolt to terminate the Contract and exclude the Supplier from future procurements.", "a £450 box against a £9m phase 2. and Desmond's reputation.")],
                  plain="anti-bribery clauses and supplier codes usually cover hospitality explicitly, with tougher rules during procurements. Breaching them can end the current contract and the next one."),
    health=dict(now="g",
                g=("no procurement near", ["Modest hospitality, declared.", "Both policies followed.", "Register it."]),
                a=("a procurement planned", ["Nothing beyond coffee for the panel.", "Thank with letters.", "Decide before asking them."]),
                r=("a live tender", ["No hospitality at all.", "Contact only through procurement.", "Register even refusals."])),
    pressure=dict(level=2, title="the kind gesture", cost="a disappointed account director",
                  items=["Vivian meant well. Explain the policy, not her mistake.", "Declining before asking the client spares them an awkward no."]),
    baseline="Each line compares <b>a football box for the tender panel</b> with <b>declining it and sending specific thank-you letters, all registered</b>.",
    ratings=[(3, 4, "Elaine pinned the card to her screen."),
             (3, 4, "The exception desk heard thanks, in writing."),
             (3, 4, "£1,350 not spent."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 5, "No conflict before phase 2."),
             (2, 5, "Everything registered, including the refusal."),
             (4, 4, "An afternoon of letters."),
             (4, 4, "A register.")],
    pitfalls=[("“Everyone does it”", "The rules disagree.", "read both policies."),
              ("Ignoring timing", "Hospitality before a tender.", "check for planned procurements."),
              ("Asking the client to decide", "You put them in a bad position.", "decide first."),
              ("Unregistered gifts", "Hard to explain later.", "register everything."),
              ("No thanks at all", "People feel unappreciated.", "specific letters, copied to their boss.")],
    grimoire=[(6, "procurement-labyrinth", "The Labyrinth of Procurement", "shows the rules from MetroVolt's side: legal, security reviews and fourteen forms.")],
    use=["Any hospitality or gift to a client.", "Near any procurement.", "Thanking people after a big milestone."],
    skip=["Never skip the register."],
    related=["<b>How Do We Say No to a Client?</b> (this volume)", "<b>How Do We Bid Against the Rival for the Next Phase?</b> (vol. 6)", "<b>How Do I Read a Tender?</b> (vol. 1)", "<b>Who Remembers What We Promised?</b> (vol. 1)"],
    quiz=[("What does MetroVolt's policy say about bidders?", "Nothing may be accepted from a supplier in a live or planned procurement."),
          ("Why was the timing a problem?", "Phase 2 was a planned procurement and the guests were on its panel."),
          ("Why decide before asking the client?", "So they aren't put in the position of refusing."),
          ("What replaced the box?", "Specific thank-you letters copied to directors, and a lunch for Wrenfield's own team."),
          ("What goes in the register?", "Everything offered, received or declined, with the decision and reason.")],
    quiz_sit=[("Sven sends Ines a tin of biscuits at Christmas. Accept or decline?", "Accept: it's small, Halvorsen isn't a bidder against MetroVolt's panel through Ines, and it's shared with the team. Register it anyway.")],
    try_it="Find your company's gifts and hospitality policy and your client's. What's the threshold? What happens during a procurement? Write one thank-you letter you've been meaning to send.",
    remember="If a gift <span class=\"hl\">needs explaining</span>, it isn't a gift. During a procurement: <span class=\"hl\">letters, not boxes</span>.",
    late=dict(when="Mon 4 December 2028 · 20:15 · hotel near The Grid",
              lines=["Declined Vivian's football box before anyone at MetroVolt saw the invitation. Desmond will never know he was spared.",
                     "Wrote twelve thank-you letters to the exception desk. Took longer than the football would have. Meant more.",
                     "Sven's biscuits, however, are fine. Registered and eaten."]),
    sources=["UK Ministry of Justice, <i>The Bribery Act 2010: guidance</i> (hospitality and promotional expenditure).",
             "Transparency International UK, <i>Gifts and Hospitality</i> guidance (2018).",
             "Crown Commercial Service, supplier code of conduct."],
)

# ------------------------------------------------------------------ 08 How Do We Share a Floor with the Rival?
sf_problem = Doodle(760, 240, "Doodle of floor 19 in December 2028. Vexmoor's Ascend team of twelve moves into the desks next to Wrenfield's. Same kitchen, same printer, same meeting rooms. Wrenfield's whiteboard shows wave 2 estimates. Phase 2's tender opens in March and both firms will bid.",
                    "Twelve Vexmoor desks next to ours. One kitchen, one printer, and our whiteboard.", exact=True)
sf_problem.box(14, 30, 340, 160, "Wrenfield", "blue", sub="6 desks · whiteboard: wave 2 estimates", size=21, subsize=14)
sf_problem.box(406, 30, 340, 160, "Vexmoor (Ascend)", "pink", sub="12 desks", size=21, subsize=15)
sf_problem.box(310, 200, 140, 36, "kitchen · printer", "y", size=14)

sf_how = Doodle(760, 330, "Floor rules agreed by the Wrenfield team on 11 December. Clean desks and whiteboards every evening; bid material never on the floor, only in Leeds. Screens: privacy filters. Calls about the bid: from a booked room, never the kitchen. Printing: nothing about the bid. No poaching, no fishing, no gossip. Be warm and ordinary: share the kettle, say good morning, help when asked.",
                "Clean desks, private screens, no corridor talk, no poaching, and a shared kettle.", exact=True)
for i, (h, sub, fill) in enumerate([("clean", "desks, whiteboards", "y"), ("screens", "privacy filters", "y"), ("calls", "booked rooms only", "y"), ("printing", "nothing about the bid", "y")]):
    sf_how.box(14 + i * 186, 20, 174, 90, h, fill, sub=sub, size=19, subsize=14)
sf_how.box(14, 140, 360, 80, "never", "pink", sub="poach · fish · gossip", size=21, subsize=15)
sf_how.box(386, 140, 360, 80, "always", "green", sub="kettle · good morning · help", size=21, subsize=15)
sf_how.note(380, 280, "bid work happens in Leeds", "pen", size=18)

SHARING_FLOOR = dict(
    slug="sharing-a-floor", date=date(2028, 12, 11), meta=on_site(date(2028, 12, 11)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. working beside a competitor",
    tldr="Sharing a client's floor with a rival is normal in big organisations, and it needs discipline, not hostility. <b>Clean desks and whiteboards</b>, <b>private screens</b>, <b>calls in booked rooms</b>, nothing confidential on the shared printer, and bid work <b>off site</b>. Never poach, fish or gossip. And be warm and ordinary: share the kettle. The rival's people are colleagues today and possibly yours tomorrow.",
    chips=[("Family", "holding your ground"), ("Lives in", "Wrenfield floor-19 rules (one page, pinned)"), ("Pairs with", "the rival adviser (vol. 4), the phase 2 bid (vol. 6)")],
    problem_side="The Grid, floor 19, December 2028",
    problem="""  <p class="lead">On <b>Monday 11 December</b>, Vexmoor's <b>Ascend</b> team, twelve people, moves into the desks next to Wrenfield's on floor 19. Same kitchen, same printer, same meeting rooms.</p>
  <ul>
    <li>Wrenfield's whiteboard shows the <b>wave 2 estimates</b> from the readiness sprint.</li>
    <li>Phase 2's tender opens in March. Both firms will bid.</li>
    <li>Lottie, chatting at the kettle on day one, mentions Wrenfield's new test tool. <span class="hl-pink">Bea writes it down.</span></li>
  </ul>""",
    problem_figs=[sf_problem],
    sides=dict(client=("MetroVolt facilities", "<p>MetroVolt has more suppliers than desks on floor 19. Putting two of them side by side is a seating decision, not a strategy. MetroVolt expects both to behave professionally.</p>", "You're both suppliers. Please share nicely."),
                vendor=("Ines and the team", "<p>For Wrenfield, a competitor at the next desk means every whiteboard, screen and kettle chat is visible. Hostility would look petty and could be reported to Rupert. Carelessness could hand Vexmoor the phase 2 bid. The answer is boring, consistent discipline.</p>", "Friendly at the kettle, careful at the desk.")),
    sides_after="Most information leaks to competitors aren't espionage. They're whiteboards, printers and kitchens.",
    analogy_side="the shared office kitchen in an open-plan building",
    analogy="""  <p>Two law firms share a floor in a serviced office. Neither hates the other. Both keep <b>files locked</b>, <b>discuss cases in their own rooms</b>, never leave papers on the shared printer, and are perfectly pleasant in the kitchen. Nobody thinks the discipline is unfriendly. It's simply professional.</p>""",
    map=[("Locked files", "Clean desks and whiteboards"),
         ("Cases discussed in their own rooms", "Bid calls in booked rooms only"),
         ("Nothing on the shared printer", "No bid material printed on floor 19"),
         ("Pleasant in the kitchen", "Share the kettle, say good morning"),
         ("Two firms, one floor", "Wrenfield and Vexmoor on 19")],
    how_side="floor rules: clean, private, off-site, never, always",
    how="""  <p>On the first evening Ines writes <b>floor rules</b> on one page, discusses them with the team the next morning, and pins them inside a cupboard (not on the wall):</p>
  <ul>
    <li><b>Clean</b>: desks and whiteboards wiped every evening. The wave 2 estimates go back to Leeds.</li>
    <li><b>Screens</b>: privacy filters on every laptop, from Wednesday.</li>
    <li><b>Calls</b>: anything about the bid, only from a booked room or from Leeds.</li>
    <li><b>Printing</b>: nothing about the bid on floor 19's printer.</li>
    <li><b>Never</b>: poach Vexmoor's people, fish for their plans, or gossip about them.</li>
    <li><b>Always</b>: share the kettle, say good morning, help if they ask where things are.</li>
  </ul>
  <p>Lottie is mortified about the test tool. Ines tells her it was a good lesson cheaply learned: the tool is public anyway. In January, Bea asks Lottie where the good coffee is. Lottie tells her. That's the right answer too.</p>""",
    how_figs=[sf_how],
    steps=[("Write simple floor rules", "One page, discussed with the team."),
           ("Clean every evening", "Desks, whiteboards, printer trays."),
           ("Move sensitive work off site", "Bids in your own office."),
           ("Use privacy filters and booked rooms", "For screens and calls."),
           ("Ban poaching, fishing and gossip", "In both directions."),
           ("Stay warm", "Professional, not hostile.")],
    vocab=[("Information hygiene", "Habits that stop confidential information leaking."),
           ("Clean desk policy", "Leaving no confidential material visible when away."),
           ("Non-solicitation", "Agreeing not to recruit another firm's or the client's staff."),
           ("Competitive intelligence", "Legitimately gathered information about competitors."),
           ("Privacy filter", "A screen cover that limits viewing angles."),
           ("Co-located competitors", "Rival suppliers working in the same client space.")],
    code=dict(file="wrenfield/floor-19-rules.md", note="agreed with the team · Tue 12 Dec 2028", src="""
FLOOR 19 RULES (pinned inside the cupboard, not on the wall)

clean     desks + whiteboards wiped by 18:00 · nothing about phase 2 on floor 19
screens   privacy filters on all laptops (from Wed 13 Dec)
calls     anything about the bid: booked room or Leeds, never the kitchen or the lift
printing  nothing about the bid on the floor 19 printer
never     poach · fish · gossip  (and we don't answer questions about our bid)
always    share the kettle · say good morning · help if asked
if unsure: ask Ines; assume it's visible
"""),
    contract=dict(side="what protects both firms", doc="Lodestar SOW · §16 (confidentiality) and §17 (non-solicitation)", date="signed 30 June 2027", stamp="both ways",
                  clauses=[("16.2", "The Supplier shall protect MetroVolt's Confidential Information, including information about other suppliers obtained in the course of the Services.", "what we see of Vexmoor's work is MetroVolt's confidential information. we don't use it."),
                           ("17.1", "Neither Party shall solicit the other's staff involved in the Services for 12 months.", "and we don't poach from Vexmoor either. as a rule, not a clause.")],
                  plain="your contract usually treats what you learn about other suppliers as the client's confidential information. Using it would breach the contract as well as good manners."),
    health=dict(now="g",
                g=("friendly rivals", ["Rules anyway.", "Warmth is fine.", "No shop talk."]),
                a=("a live competition ahead", ["Bid work off site.", "Clean desks nightly.", "Brief juniors kindly."]),
                r=("a rival hunting for information", ["Strict rules, no exceptions.", "Report inappropriate fishing to the client.", "Still polite."])),
    pressure=dict(level=2, title="the next desk", cost="one awkward kettle conversation · a lot of whiteboard wiping",
                  items=["Lottie's slip was small and public. Use it to teach, not to blame.", "Being cold to Vexmoor's analysts would look petty to MetroVolt. Be ordinary."]),
    baseline="Each line compares <b>carrying on as before</b> with <b>one page of floor rules: clean, private, off-site, never, always</b>.",
    ratings=[(3, 4, "MetroVolt sees two professional suppliers."),
             (3, 3, "A little friction, mostly habit."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 5, "Bid information stays in Leeds."),
             (3, 4, "Rules written and followed."),
             (4, 4, "One evening to set up."),
             (3, 3, "Daily cleaning.")],
    pitfalls=[("Whiteboards left up", "Estimates visible to the rival.", "wipe every evening."),
              ("Bid calls in the kitchen", "Overheard.", "booked rooms or off site."),
              ("Hostility", "Looks petty to the client.", "share the kettle."),
              ("Fishing", "Breaches confidentiality and trust.", "never ask about their bid."),
              ("Blaming juniors for slips", "They hide the next one.", "teach kindly.")],
    grimoire=[(7, "hot-desk-hunger-games", "The Hot-Desk Hunger Games", "is the same floor, a year later, from MetroVolt's side: 200 people, 140 desks.")],
    use=["Rival suppliers share a client's space.", "A competitive procurement is coming.", "Shared kitchens, printers and rooms."],
    skip=["Never skip the clean desks."],
    related=["<b>What Do We Do When Our Rival Advises the Client?</b> (vol. 4)", "<b>How Do We Bid Against the Rival for the Next Phase?</b> (vol. 6)", "<b>What Do We Do with What We Overhear?</b> (this volume)", "<b>How Do We Compete with a Big Consultancy?</b> (vol. 1)"],
    quiz=[("Where does most information leak to competitors?", "Whiteboards, printers, screens and kitchens, not espionage."),
          ("Where does bid work happen?", "Off site, in Leeds."),
          ("What are the three nevers?", "Poach, fish, gossip."),
          ("What's the right attitude to the rival's people?", "Warm and ordinary: share the kettle, say good morning."),
          ("What does clause 16.2 say about other suppliers?", "Information about them obtained during the work is MetroVolt's confidential information.")],
    quiz_sit=[("Bea leaves a printed Vexmoor document on the shared printer. What does Lottie do?", "Not read it; put it in an envelope, and hand it back to Bea or to MetroVolt facilities. Tell Ines what she did, so it's on record.")],
    try_it="Walk around your workspace as if you were your competitor. What could you learn from desks, whiteboards, screens and the printer? Write three floor rules that would close the gaps.",
    remember="Friendly <span class=\"hl\">at the kettle</span>, careful <span class=\"hl\">at the desk</span>. Bid work happens somewhere else.",
    late=dict(when="Mon 11 December 2028 · 21:10 · hotel near The Grid",
              lines=["Twelve Vexmoor desks next to ours. Our whiteboard had wave 2 estimates on it until 17:40.",
                     "Lottie told Bea about the test tool at the kettle. She looked as if she'd confessed to a crime. It's public. Lesson learned for free.",
                     "Floor rules pinned inside the cupboard. Not on the wall: that would be its own message."]),
    sources=["UK Information Commissioner's Office, guidance on clean desk and information security.",
             "Crown Commercial Service, guidance on supplier conflicts of interest.",
             "Gerald Weinberg, <i>The Secrets of Consulting</i> (1985)."],
)

NOTES = [SAYING_NO, LIKED_TRUSTED, GIFTS, SHARING_FLOOR]
