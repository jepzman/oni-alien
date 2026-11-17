# Series 4 · The Darkside of the Corporation · Act III: The Throne Room (bad managers).
# Rendered by scripts/grimoire.py. `note(text)` (the Annotator's margin note) is injected by the loader.
# Text is raw HTML. Stats follow grimoire.STATS: sanity, career XP, mana, armor, stealth, allies, soul, time, backfire safety.
# Plates exist for three entries: all-seeing-eye, seagull-overlord, escape-portal.

ACT = dict(
    no=3,
    title="The Throne Room",
    sub="You cannot slay your lord. But you can manage them",
    contents_title="The lords of the throne room",
    summary="Act III of The Darkside of the Corporation: bad managers as lords of the throne room. Micromanagers, absent bosses, seagulls, moody tyrants, credit-takers and the escape portal, with counter-spells that work.",
    intro=f"""<p class="lead">People don't leave companies. They leave managers. Pip did not leave MetroVolt in the winter
of 2026. But he looked at the door quite often.</p>
<p>After the reorg in Act I, Grid Analytics moved into Strategy, and Pip moved with it. His new lord was <b>Victor
Kraal</b>, recently arrived from a consultancy, who brought with him a 47-slide operating model and a habit of asking
for updates on the updates. Above Victor sat <b>Benedict Crane</b>, Director of Strategy, last seen in person in
October. Above them both, for one day each month, descended <b>Rupert Thorne</b> from the parent group.</p>
{note("A bad manager is the single biggest risk to your sanity at work. The good news: most bad managers are not evil. They're anxious, untrained, overloaded or badly managed themselves. That gives you a lot to work with.")}
<p>This Act is about the person who writes your review, approves your leave and decides which work you get. You
can't choose them. You can't fire them. But you can <b>manage them</b>: understand what drives them, give them what
they need, protect yourself where you must, and recognise when it's time to leave the throne room.</p>""",
    cast=[
        ("Pip", "he/him", "analyst, now in Grid Analytics (Strategy). Promoted to level 4. Wiser. Slightly."),
        ("The Chronicler", "they/them", "nineteen years at MetroVolt, eleven managers. Has notes on all of them."),
        ("The Annotator", "she/her", "ex-MetroVolt, now freelance. Left because of a manager. Will tell you which one, for a drink."),
        ("Victor Kraal", "he/him", "Pip's new manager, Head of Grid Analytics. Ex-consultant. Anxious, clever, everywhere."),
        ("Benedict Crane", "he/him", "Director of Strategy, Victor's boss. Mostly a calendar entry marked “travelling”."),
        ("Rupert Thorne", "he/him", "Interim Transformation Director from the parent group. Visits monthly. Leaves a mess."),
        ("Marcus Bell", "he/him", "Pip's old manager, Grid Planning. Kind. Avoids every hard conversation."),
        ("Gareth Pound", "he/him", "Director of Network Assets. Pip is seconded to his team for the meter fix. Moody."),
        ("Jules", "they/them", "Pip's friend and peer. Now, as of January, his team lead."),
        ("Ottoline Grey", "she/her", "Chief of Staff to the CEO. Still the hidden throne. Still drinking tea."),
        ("Priya Nair", "she/her", "Head of Customer Operations. Has an open role. Has noticed Pip."),
    ],
    entries=[
        # ------------------------------------------------------------------ 1
        dict(
            slug="all-seeing-eye", flagship=True,
            plate_caption="Tuesday, 09:00 to 17:30. Four check-ins, two screen-shares and a sticky note. The model was finished on Monday.",
            ring="ANY UPDATE ✠ JUST CHECKING IN ✠ CAN YOU SHARE YOUR SCREEN ✠", scrawl="it sees your drafts",
            name="The All-Seeing Eye", sigil="◉",
            epithet="Watches every keystroke. Trusts none of them.",
            threat=4, habitat="your Teams status, shared drafts, “quick check-ins” at 9, 11, 2 and 4",
            weakness="predictable, proactive updates, before it asks",
            summary="The All-Seeing Eye: the micromanager, why they hover, and how to trade regular updates for trust and room to work.",
            sighting=f"""<p>In his first week, Victor asked Pip for a status update four times a day. He edited Pip's emails
before they were sent. He asked Pip to share his screen “just to see where you are”. He moved a decimal point in the
load model himself, at 23:10, and left a comment: <i>“Fixed. Pls check before sending things.”</i></p>
<p>On Tuesday there was a sticky note on Pip's monitor: <i>“UPDATE PLS (3rd time today) — V.”</i> Victor sat
four metres away. He could have just asked. He had, in fact, asked. Twice.</p>""",
            know=f"""<p>Micromanagers are usually driven by <b>anxiety</b>, not contempt. They're new, or under
pressure from above, or they've been burned by someone who missed a deadline. Watching closely feels like control.
Not knowing feels like danger. Every unanswered question becomes a check-in.</p>
<p>So the cure is to <b>remove the not-knowing</b>. If they get regular, predictable information before they ask,
the anxiety drops, and the hovering usually follows. It's not fair that you have to do this. It works anyway.</p>
{note("Micromanagement is a trust problem wearing a productivity costume. Feed the trust and the costume falls off.")}""",
            omens=[
                "Several “quick check-ins” a day.",
                "They rewrite your work rather than comment on it.",
                "Requests to share your screen or copy them on everything.",
                "Decisions you used to make now need their approval.",
                "Sticky notes. On your monitor. From four metres away.",
            ],
            counters=[
                ("The Rhythm Ward", "Offer updates at fixed times before they ask: a short note at 10:00 and 16:00. Predictability kills anxiety.",
                 "“To keep you in the loop without interrupting, I'll send a three-line update at 10 and 4 every day. Does that work?”"),
                ("The Pre-emptive Strike", "Flag risks and decisions early. A micromanager hates surprises more than problems.",
                 "“Heads-up: the substation data is late, so the forecast moves to Thursday. Here's my plan B.”"),
                ("The Trust Ladder", "After two weeks of reliable updates, ask to step down to fewer: daily, then twice a week.",
                 "“The updates seem to be working. Could we try one at the end of each day, and see if that's enough?”"),
                ("The Working Agreement", "Agree, explicitly, which decisions you make alone and which need them.",
                 "“Can we agree: I decide model choices and formatting; you approve anything going to Benedict or above?”"),
            ],
            forbidden=[
                ("The Blackout", 4, "Going quiet to show you don't need watching. To an anxious manager, silence means disaster. The hovering doubles."),
                ("The Malicious Compliance", 3, "Asking permission for every tiny thing to make a point. They'll accept it, and you'll have trained them to need it."),
                ("The Public Rebuke", 4, "“Victor, I can do my job, you know” in a team meeting. True. Unforgettable. Not in a good way."),
            ],
            difficulty=dict(
                normal="A new or nervous manager. Two weeks of Rhythm Ward and it calms down.",
                nightmare="They're micromanaging because they're being micromanaged. Help them answer upwards: give them what their boss asks for, before they ask.",
                hell="Control is their personality and nothing reassures them. Keep the updates, protect your evenings, document decisions, and start reading the Escape Portal (entry 12).",
            ),
            stats=[4, 4, 4, 4, 4, 4, 5, 3, 5], stats_for="The Rhythm Ward",
            loot=("The Twice-Daily Update",
                  "Three lines, twice a day, for two weeks. Then negotiate down.",
                  """10:00 · Pip · Grid Analytics
TODAY    finish Q1 load model v2, send to Ops by 16:00
RISK     substation 14 data late (chasing IT)
NEED     your OK on the heatwave assumption (2 options attached)

16:00 · Pip
DONE     model v2 sent to Ops ✔
TOMORROW sensitivity runs
RISK     none new"""),
            trial=[
                ("Your new manager checks in four times a day. What do you propose?",
                 "The Rhythm Ward: two fixed updates a day, before they ask. Then ask to step down after two weeks."),
                ("They rewrite your emails before you send them. What do you say?",
                 "Ask what they're trying to get right: “What would you like these emails to do differently?” Then agree a standard, and stop needing the edits."),
                ("When is micromanagement a sign to leave?",
                 "When months of reliable updates change nothing, and it's affecting your health or growth. Then it's not anxiety; it's the job."),
            ],
            last_word="Answer the question before it's asked, and the eye starts to close.",
        ),
        # ------------------------------------------------------------------ 2
        dict(
            slug="absent-lord",
            ring="TRAVELLING ✠ CAN THIS WAIT ✠ WHY WASN'T I TOLD ✠", scrawl="decide, then inform",
            name="The Absent Lord", sigil="☽",
            epithet="Never there when you need them. Always there when it goes wrong.",
            threat=3, habitat="airports, board away-days, a calendar of solid purple",
            weakness="short written choices with a default and a deadline",
            summary="The Absent Lord: the manager who's never available and then angry they weren't consulted, and how to get decisions anyway.",
            sighting=f"""<p>Benedict Crane, Director of Strategy, had a calendar that looked like a bruise: solid purple, marked
“travelling”, from October to February. Pip needed one decision: whether the Q1 forecast should use the regulator's
heatwave scenario or MetroVolt's own. He emailed. He messaged. He booked a call, which moved three times.</p>
<p>After two weeks Victor decided, so the work could go on. At the board, Benedict asked, with real anger,
<i>“Why was I not consulted on the scenario?”</i> Victor looked at Pip. Pip looked at the email, which had six follow-ups.</p>""",
            know=f"""<p>Absent managers are usually <b>overloaded and badly organised</b>, not uncaring. They get hundreds of
messages; yours is one of them. Long questions get postponed. Open questions get ignored. Then, when it matters,
they suddenly care, because now someone above them is asking.</p>
<p>The fix is to make deciding <b>effortless</b>: one short message, two options, your recommendation, a default
if they don't reply, and a deadline. Silence becomes consent, and you have it in writing.</p>
{note("An absent boss is a boss who'll read the first two lines on their phone in a taxi. Write the first two lines for the taxi.")}""",
            omens=[
                "Meetings with them move three times.",
                "Your questions get “let's discuss” and never get discussed.",
                "Decisions stall, then they're angry about the delay.",
                "They seem surprised by work they assigned.",
            ],
            counters=[
                ("The Default Rune", "Send one short message: the decision, two options, your recommendation, and what you'll do by when if you hear nothing.",
                 "“Decision needed: Q1 scenario. A) regulator's, B) ours. I recommend A. If I don't hear by Thursday 12:00, I'll go with A.”"),
                ("The Taxi Summary", "Put the ask in the subject line and the first line. Assume they read nothing else.",
                 "Subject: “DECIDE BY THU: Q1 heatwave scenario (A or B, I recommend A)”"),
                ("The Standing Slot", "Ask for a regular 15 minutes, even fortnightly. Short, fixed meetings survive busy calendars; long ad-hoc ones don't.",
                 "“Could we have 15 minutes every other Monday? I'll bring a list of decisions and nothing else.”"),
            ],
            forbidden=[
                ("The Waiting Game", 3, "Doing nothing until they reply. The work stalls, and the delay becomes yours."),
                ("The Silent Override", 4, "Deciding without telling them. When they find out, it's insubordination, however sensible it was."),
                ("The Passive Reminder", 2, "“Just bumping this up 🙂” for the sixth time. It's a seventh unread message. Change the format, not the frequency."),
            ],
            difficulty=dict(
                normal="Busy, but reachable. The Default Rune works every time.",
                nightmare="Unreachable for weeks. Agree with them in advance which decisions you or your manager can make in their absence.",
                hell="Absent and then blaming. Every decision in writing, with defaults and dates, copied to your direct manager. Your record is your shield.",
            ),
            stats=[4, 4, 4, 5, 4, 3, 5, 5, 4], stats_for="The Default Rune",
            loot=("The Default Decision Email",
                  "The format that gets decisions out of the busiest people alive.",
                  """Subject: DECIDE BY THU 12:00: Q1 heatwave scenario (I recommend A)

Benedict,

One decision for the Q1 forecast:
  A) Regulator's heatwave scenario  ← I recommend (board expects it)
  B) MetroVolt's own scenario        (2% lower peak)

If I don't hear by Thursday 12:00, I'll use A.
Victor is copied and agrees.

Pip"""),
            trial=[
                ("Your director hasn't answered a key question in two weeks. What do you send?",
                 "The Default Rune: two options, your recommendation, a default and a deadline. In the subject line."),
                ("They're angry they weren't consulted, but you have six emails. What do you say?",
                 "Calmly, without “as per my emails”: “I'm sorry it didn't reach you in time. I'll forward the decision note from the 3rd. How would you like me to flag these in future?”"),
                ("Is it OK to decide without your boss?",
                 "Only with an agreed default or a clear mandate, and always in writing. Never silently."),
            ],
            last_word="If they won't decide, make not deciding a decision too. In writing. With a date.",
        ),
        # ------------------------------------------------------------------ 3
        dict(
            slug="seagull-overlord", flagship=True,
            plate_caption="Rupert's monthly visit. He flew in at 9, squawked at 10, and was on the 14:05 to London. The strategy board will need cleaning.",
            ring="I'VE SEEN THIS BEFORE ✠ QUICK THOUGHTS ✠ CHANGE EVERYTHING ✠", scrawl="he leaves at 14:05",
            name="The Seagull Overlord", sigil="⌒",
            epithet="Flies in, makes a lot of noise, craps on everything, flies out.",
            threat=4, habitat="monthly reviews, quarterly “deep dives”, the 14:05 train",
            weakness="context, delivered before he lands",
            summary="The Seagull Overlord: the senior leader who swoops in, overturns plans without context and leaves, and how to brief, absorb and survive the visit.",
            sighting=f"""<p>Rupert Thorne, Interim Transformation Director, arrived at The Grid once a month. In January he looked
at the Lumen plan for eleven minutes and announced: “This is too slow. Do the city centre first. And use the
new vendor. I've seen this work in Rotterdam.” Then he caught the 14:05 to London.</p>
<p>The city centre had been last on purpose (underground cabling, permits). The new vendor had failed a security review.
It took the team three weeks to un-change the plan. In February, Rupert came back, and asked why Lumen was three
weeks late.</p>""",
            know=f"""<p>The Seagull is a senior person with <b>little context and a lot of authority</b>. They visit
briefly, feel they must add value, and so they change things. Big, visible changes feel like leadership. They rarely
stay long enough to see the cost.</p>
<p>You can't stop the visits. But you can <b>shape what they see</b>: brief them before they land, show them the
reasons behind the plan, and give them something useful to say yes to. A Seagull with context is just a bird.</p>
{note("The Seagull isn't stupid. They're under-informed and over-powered. Fix the first one and the second matters less.")}""",
            omens=[
                "A senior visitor who's “seen this before” somewhere else.",
                "Plans change most in the week after a visit.",
                "Reviews where nobody explains why the plan is as it is.",
                "The team quietly undoes visit decisions for weeks.",
            ],
            counters=[
                ("The Pre-Landing Brief", "Send a one-page briefing two days before the visit: status, the three big decisions already made, and why.",
                 "“Ahead of Thursday: Lumen is on track. Three decisions you'll see, and why we made them: city centre last (permits), current vendor (security), phase 2 in May.”"),
                ("The Reason Reveal", "When they suggest a change, show the constraint calmly. Ask what problem they're trying to solve.",
                 "“Good thought. We put the city centre last because of the cabling permits. What's the worry behind going faster: the regulator date?”"),
                ("The Bone to Carry Home", "Give them a real, small improvement they can own. Seagulls need to leave with something.",
                 "“One thing you could help with: the security review for the new vendor is stuck at group. Could you unblock it?”"),
                ("The Written Echo", "After the visit, write down what was actually agreed, and send it to them and your director.",
                 None),
            ],
            forbidden=[
                ("The Instant Yes", 4, "Agreeing to every change in the room to keep him happy. Three weeks of un-doing, and the delay is yours."),
                ("The Hide-and-Seek", 3, "Avoiding the visit and hoping he talks to someone else. He will. Someone with less context."),
                ("The Eye-Roll Debrief", 3, "Mocking him to the team after he leaves. It feels great. It travels to London faster than he does."),
            ],
            difficulty=dict(
                normal="An occasional visitor with good intentions. A pre-landing brief turns him into an ally.",
                nightmare="Monthly disruption. Agree with your director who speaks for the plan in the visit, and always do the Written Echo.",
                hell="His changes override your director's. Escalate the pattern with facts (cost of each change), and get your director to agree a change process he must use.",
            ),
            stats=[4, 4, 3, 4, 3, 4, 5, 4, 4], stats_for="The Pre-Landing Brief",
            loot=("The Pre-Landing Brief",
                  "One page, sent two days before any senior visit.",
                  """LUMEN · brief for Rupert Thorne · visit Thu 16 Jan

STATUS        On track for the regulator date (31 Mar). 62% of meters done.
DECIDED       1. City centre last: cabling permits arrive in Feb
              2. Current vendor: new one failed group security review
              3. Phase 2 starts May, after winter peak
WHERE YOU     The group security review for the new vendor
COULD HELP    is stuck. Unblocking it would save ~3 weeks in phase 2.
ASK OF YOU    Confirm the phase 2 start date (May)."""),
            trial=[
                ("A senior visitor wants to change your plan in a meeting. What do you say?",
                 "The Reason Reveal: explain the constraint calmly, then ask what problem they're trying to solve."),
                ("How do you stop the monthly chaos?",
                 "Brief them before they land, give them a useful job, and write down what was really agreed afterwards."),
                ("He overrules your director. Whose instruction do you follow?",
                 "Raise it with your director straight away, in writing. Don't pick a side alone."),
            ],
            last_word="Feed the seagull before it lands, and it eats from your hand instead of your plan.",
        ),
        # ------------------------------------------------------------------ 4
        dict(
            slug="weather-tyrant",
            ring="WHAT MOOD IS HE IN ✠ NOT TODAY ✠ READ THE ROOM ✠", scrawl="check the forecast",
            name="The Weather Tyrant", sigil="☈",
            epithet="Sunshine on Monday. Thunder by Tuesday. No forecast.",
            threat=4, habitat="Monday mornings, budget weeks, the minutes after a call with his boss",
            weakness="patterns, written down, and a calm that doesn't move with the weather",
            summary="The Weather Tyrant: the moody, unpredictable manager, how to read the forecast, protect yourself and stay steady.",
            sighting=f"""<p>Seconded to Network Assets for the meter fix, Pip learned to read Gareth Pound like a barometer.
On good days Gareth was funny and generous and bought pastries. On bad days he slammed his laptop shut, said
“unacceptable” to slides he'd approved the week before, and once made a junior engineer cry over a font.</p>
<p>The team had a private chat called <i>☀️ / ⛈️</i>. Someone posted the forecast each morning after seeing him
in the lift. Nobody brought bad news on a ⛈️ day. Bad news therefore arrived in large, late piles.</p>""",
            know=f"""<p>Moody managers are usually <b>stressed and poorly regulated</b>: they bring pressure from above
straight into the room. Their moods have patterns (days, deadlines, meetings with their boss), even if they can't see
them themselves.</p>
<p>You are not responsible for their weather. But you can <b>forecast it</b>, time your asks, and keep your own
behaviour steady. And there is a line: shouting, humiliation or fear is not weather. It's <b>conduct</b>, and it has
a channel.</p>
{note("You can work for a moody manager for a while. You can't work for a cruel one. Learn the difference early: moods change; cruelty repeats.")}""",
            omens=[
                "The team checks “what mood is he in” before asking anything.",
                "Approved work gets rejected on a bad day.",
                "Bad news is held back and arrives late.",
                "You feel relief when they're out of the office.",
            ],
            counters=[
                ("The Barometer", "Notice the pattern (days, times, after which meetings). Time important asks for good windows.",
                 None),
                ("The Steady Hand", "Stay calm and consistent whatever the weather. Don't absorb the mood or reflect it back.",
                 "“I can see today's tough. Shall I come back with this at four, or do you want the two-minute version now?”"),
                ("The Written Approval", "Get approvals in writing on good days, so bad days can't quietly undo them.",
                 "“Great, so we're agreed on the layout. I'll note it in the project log.”"),
                ("The Line in the Sand", "If moods turn into shouting, humiliation or fear, name it calmly, privately, and take it to HR if it repeats.",
                 "“I want to do good work for you, but I'm not OK being shouted at. Can we talk about what went wrong?”"),
            ],
            forbidden=[
                ("Storm Chasing", 3, "Bringing everything on good days only. Urgent bad news on bad days is still urgent; delay makes it worse."),
                ("Becoming the Weather", 4, "Matching his mood: snapping back, sulking. Now there are two storm systems."),
                ("The Forecast Channel", 3, "The ☀️ / ⛈️ chat is funny. Until it's screenshotted. Then it's a disciplinary."),
            ],
            difficulty=dict(
                normal="Occasional bad days under pressure. Time your asks, stay steady, get things in writing.",
                nightmare="Frequent swings that affect decisions. Written approvals, and a quiet word with them on a good day about the impact.",
                hell="Shouting, humiliation, people in tears. That's not a mood, it's misconduct. Keep a dated record, support colleagues, go to HR or your skip-level.",
            ),
            stats=[3, 3, 4, 4, 4, 3, 5, 4, 4], stats_for="The Steady Hand",
            loot=("The Weather Log",
                  "Private. Dated. Factual. For spotting patterns, and for evidence if the line is crossed.",
                  """DATE    MOOD  TRIGGER?                  WHAT HAPPENED
13 Jan  ☀️    —                          approved meter-fix plan (in writing ✔)
14 Jan  ⛈️    call with ExCo at 9        rejected same plan, "unacceptable"
20 Jan  ⛈️    budget week                shouted at Sam in front of team  ← LINE
21 Jan  ☀️    —                          apologised to Sam? (no)

Pattern: storms after ExCo calls (Tue) + budget weeks."""),
            trial=[
                ("Your manager approved a plan yesterday and rejects it today, angrily. What do you do?",
                 "Stay calm, refer to yesterday's written approval, and ask what's changed: “Yesterday we agreed X. Has something changed I should know about?”"),
                ("You have urgent bad news and it's a ⛈️ day. Wait?",
                 "No. Deliver it short and calm, with a plan. Delayed bad news is worse news."),
                ("Your manager shouts at a colleague in front of the team. What now?",
                 "Support the colleague afterwards, note it with date and facts, and encourage them (or yourself) to raise it. That's conduct, not weather."),
            ],
            last_word="You can't control the weather. You can control whether you bring an umbrella, and a written record.",
        ),
        # ------------------------------------------------------------------ 5
        dict(
            slug="conflict-phantom",
            ring="LET'S NOT ROCK THE BOAT ✠ IT'LL SORT ITSELF OUT ✠ LATER ✠", scrawl="problems rot in the dark",
            name="The Conflict Phantom", sigil="⚲",
            epithet="Kind, warm, and gone the moment anything gets difficult.",
            threat=3, habitat="1:1s that end early, performance reviews that say “fine”",
            weakness="small problems raised early, with a suggested solution",
            summary="The Conflict Phantom: the kind manager who avoids every hard conversation, and how to get the decisions, feedback and protection you need.",
            sighting=f"""<p>Marcus Bell was the kindest manager Pip ever had. He remembered birthdays. He took the blame in
public. And for four years he let Neville (the Coasting Zombie, Act II) do almost nothing, because talking to Neville
would have been awkward.</p>
<p>The rest of the team carried Neville's work. Two good analysts left. When Pip asked Marcus for honest feedback,
Marcus said “you're doing great” and changed the subject to football. Pip found out at calibration that he was
“not quite ready for level 4”. Nobody had told him why.</p>""",
            know=f"""<p>Conflict-avoidant managers want to be <b>liked</b> and want people to be happy. Hard conversations
feel like cruelty to them. So problems are postponed, feedback is softened into nothing, and decisions that would
upset someone simply don't get made.</p>
<p>The cost lands on <b>you</b>: unclear expectations, unfair workloads, surprises in your review. You can't make
them brave. But you can make the hard thing <b>easier to say</b>: ask specific questions, raise problems small and
early, and bring solutions they can agree to without a fight.</p>
{note("“You're doing great” is not feedback. It's a hug. Hugs are nice. They don't get you promoted.")}""",
            omens=[
                "Feedback is always “great”, and reviews still go badly.",
                "Underperformers stay for years.",
                "Disagreements in the team are never addressed.",
                "1:1s drift to small talk whenever you raise a problem.",
            ],
            counters=[
                ("The Specific Question", "Don't ask “how am I doing?” Ask a question that's easy to answer honestly.",
                 "“What's one thing I'd need to do differently to be ready for level 4?”"),
                ("The Pre-Solved Problem", "Raise problems with a solution attached, so saying yes is easier than avoiding it.",
                 "“The data clean-up is uneven: I've done 80%. Could we split the rest by name, on the board, from Monday?”"),
                ("The Calibration Prep", "Before review season, ask what the people in calibration will say about you, and what evidence you should give them.",
                 "“When my name comes up at calibration, what will the concerns be? I'd like to address them now.”"),
            ],
            forbidden=[
                ("The Ambush Confrontation", 3, "A big, emotional confrontation about everything at once. They'll freeze, apologise, and nothing will change."),
                ("Going Around Them Too Early", 4, "Taking it straight to their boss without trying with them. It reads as betrayal to a manager who thought you were friends."),
                ("Accepting the Hug", 2, "Settling for “you're doing great”. Next year's review will say otherwise."),
            ],
            difficulty=dict(
                normal="A kind manager who softens feedback. Specific questions get you real answers.",
                nightmare="Problems are festering: unfair workloads, an underperformer. Bring pre-solved problems, one at a time, in writing.",
                hell="Avoidance is hurting people: bullying ignored, people burning out. Raise it formally with your skip-level; the kind manager can't protect you.",
            ),
            stats=[4, 4, 4, 3, 4, 4, 5, 4, 5], stats_for="The Specific Question",
            loot=("Five Questions a Nice Manager Can Answer",
                  "Easier to answer honestly than “how am I doing?”.",
                  """1. What's one thing I should start doing?
2. What's one thing I should stop doing?
3. If I left tomorrow, what would you miss least?
4. What would make you put me forward for level 4?
5. What will people in calibration say about me?"""),
            trial=[
                ("Your kind manager always says “great”. How do you get real feedback?",
                 "Ask specific, low-threat questions: “What's one thing I should do differently?”"),
                ("A coaster has been tolerated for years and you're carrying their work. What do you bring?",
                 "A pre-solved problem: a named split of the work, on a shared board, from a specific date."),
                ("When do you go over a conflict-avoidant manager's head?",
                 "After you've raised it clearly with them, or straight away if someone is being harmed."),
            ],
            last_word="Kindness that avoids the truth isn't kindness. Ask the question that makes the truth easy to say.",
        ),
        # ------------------------------------------------------------------ 6
        dict(
            slug="credit-taking-crown",
            ring="MY TEAM'S WORK ✠ I DELIVERED ✠ AS I PROPOSED ✠", scrawl="the vampire got promoted",
            name="The Credit-Taking Crown", sigil="♔",
            epithet="When the Credit Vampire is your boss.",
            threat=4, habitat="leadership updates, the board pack, Victor's LinkedIn",
            weakness="relationships above and around them that know your name",
            summary="The Credit-Taking Crown: when your own manager takes credit for your work, and how to stay visible without starting a war with the person who writes your review.",
            sighting=f"""<p>Pip's Q1 load model predicted the January cold snap to within 1.5%. Victor's update to the
board said: <i>“My team delivered a step-change in forecast accuracy, using an approach I introduced.”</i> The
approach was Pip's. It was in a document with Pip's name on it, dated before Victor joined.</p>
<p>Two weeks later, Victor posted on LinkedIn about “the power of data-driven leadership”. It had 412 likes.
Pip's mum liked it, not knowing.</p>""",
            know=f"""<p>In Act II you met the Credit Vampire, a peer. When the vampire is your <b>manager</b>, it's
harder: they write your review, and some credit-taking is normal (“my team delivered” is fair). It becomes a problem
when your <b>name disappears</b> and your manager becomes the only route to anyone senior.</p>
<p>You won't win by confronting them publicly. You win by making your name <b>known above and around them</b>, in
ways that also make them look good. A manager who gets credit for developing you is less likely to erase you.</p>
{note("Help your boss get credit for having you. It's the only credit war you can win.")}""",
            omens=[
                "“My team delivered”, with no names, ever.",
                "You're never invited to present your own work upwards.",
                "Your manager is the only person senior people hear from about you.",
                "Your ideas come back as “an approach I introduced”.",
            ],
            counters=[
                ("The Shared Spotlight", "Suggest you present the detail, framed as making them look good.",
                 "“For the board, would it help if I took the five minutes on the method? You'd have someone to field the technical questions.”"),
                ("The Wider Web", "Build direct relationships with the people who use your work (and your skip-level). Then your name doesn't depend on one route.",
                 "“I'd love to show Ops how the new model handles cold snaps. Could I book 20 minutes with their planners?”"),
                ("The Direct Word", "If it's a pattern, raise it privately and calmly, as a career request, not an accusation.",
                 "“I'd like more visibility for my work this year. When the model's discussed at the board, could my name be mentioned, or could I attend?”"),
            ],
            forbidden=[
                ("The Board Ambush", 5, "Telling the board it was your idea, in the meeting. You'll be right, and you'll be done."),
                ("The LinkedIn Correction", 4, "Commenting “Actually, I built this 😊” under his post. 412 people will remember you. None fondly."),
                ("The Quiet Strike", 3, "Doing worse work so he has less to steal. You'll just have worse work with your name on it."),
            ],
            difficulty=dict(
                normal="A manager who says “my team” without thinking. The Shared Spotlight fixes it.",
                nightmare="A consistent pattern. Widen your web, keep the Weekly Deeds Scroll (Act II), and have the Direct Word.",
                hell="They actively block your visibility. Build your skip-level relationship, document your work, and look at the Escape Portal, or an internal move.",
            ),
            stats=[3, 5, 3, 4, 4, 4, 5, 3, 3], stats_for="The Wider Web",
            loot=("The Visibility Request",
                  "For your 1:1. Framed as development, not grievance.",
                  """For my development this year, I'd like to:
  1. Present the forecast method at one board (with you)
  2. Meet the Ops planning leads monthly
  3. Write a short internal post on the cold-snap model

Which of these would you be comfortable with?
How can I make sure it reflects well on the team (and you)?"""),
            trial=[
                ("Your manager presents your work as their idea. First move?",
                 "Offer the Shared Spotlight for next time, and start building your Wider Web. Don't confront it in public."),
                ("Is “my team delivered” credit-taking?",
                 "Not on its own; it's often fair. It's a problem when your name never appears and you can't reach anyone senior."),
                ("Your manager blocks you from presenting anywhere. What now?",
                 "Have the Direct Word, then build relationships with your skip-level and users. If nothing changes, plan a move."),
            ],
            last_word="Your boss can take the credit. Make sure they can't take your name.",
        ),
        # ------------------------------------------------------------------ 7
        dict(
            slug="new-lord-arrives",
            ring="NEW BROOM ✠ FIRST 90 DAYS ✠ HOW DID WE GET HERE ✠", scrawl="the first impression lasts a year",
            name="The New Lord Arrives", sigil="⚑",
            epithet="A new manager is a new kingdom. The first 90 days decide your place in it.",
            threat=3, habitat="the first all-team meeting, the first 1:1, the first “operating model” deck",
            weakness="early, honest usefulness",
            summary="The New Lord Arrives: surviving and thriving when you get a new manager, in the first 90 days.",
            sighting=f"""<p>Victor arrived on the 2nd of December with a 47-slide operating model, three new acronyms and a
plan to “reset ways of working”. The team split into three camps by the second day: the eager (volunteering for
everything), the sceptical (folded arms, eyebrows) and the invisible (camera off, hoping to be forgotten).</p>
<p>Pip, unusually, did something sensible. He booked 30 minutes, brought a one-page “what you should know” about
the team's work, and asked Victor what he was being measured on. Victor, who was terrified, nearly hugged him.</p>""",
            know=f"""<p>A new manager is under pressure to <b>prove themselves fast</b>. They don't know who's good, what's
broken, or where the bodies are buried. They form impressions quickly, in the first few weeks, and those impressions
stick for a year.</p>
<p>Your best move is to be <b>early, honest and useful</b>: help them understand the landscape, find out what they
need, and show your value before the impressions set. Neither cheerleading nor resisting.</p>
{note("New managers are more scared than you are. They've just bet their reputation on a team they don't know. Be the person who makes that bet look smart.")}""",
            omens=[
                "A new manager is announced.",
                "An operating-model deck appears in week one.",
                "Colleagues split into the eager, the sceptical and the invisible.",
                "Old decisions are being quietly re-opened.",
            ],
            counters=[
                ("The Landscape Gift", "In week one, offer a one-page view of your work: what you do, what's working, what's broken, and the history they'd never guess.",
                 "“I've written one page on what Grid Analytics does and the three things I'd fix. Happy to walk you through it in 30 minutes.”"),
                ("The Measure Question", "Ask what they're measured on and what would make their first six months a success. Then help with that.",
                 "“What does a great first six months look like for you? I'd like to help with it.”"),
                ("The Honest Context", "When they propose changing something that was tried before, explain the history without defending it.",
                 "“We tried a shared queue in 2024. It failed because of X. If we try again, here's what I'd do differently.”"),
            ],
            forbidden=[
                ("The Old Guard", 3, "“That's not how we do things here.” It positions you as the obstacle on day one."),
                ("The Invisible", 3, "Keeping your head down until they settle. By the time they settle, they've decided who matters, without you."),
                ("The Courtier's Rush", 3, "Agreeing with every new idea to get in early. The team notices, and so will the manager, eventually."),
            ],
            difficulty=dict(
                normal="A thoughtful new manager. The Landscape Gift and the Measure Question make you a trusted guide.",
                nightmare="A manager with a mandate to change everything. Help them pick the right changes; argue only about the ones that will really hurt.",
                hell="A new manager bringing their own people and clearing out the old team. Be useful fast, keep your network warm, and know your options.",
            ),
            stats=[4, 5, 4, 3, 4, 5, 5, 3, 4], stats_for="The Landscape Gift",
            loot=("The First-Week Page",
                  "One page for a new manager. Facts, not complaints.",
                  """GRID ANALYTICS · what you should know (Pip)

WE DO       Load forecasts, outage analysis, Lumen meter data
WORKING     Forecast accuracy (within 2%), Ops trusts our numbers
BROKEN      1. Asset data has 3 owners, 3 versions
            2. Board asks reach us the night before
            3. No backup on the heatwave model (it's me)
HISTORY     Shared queue tried 2024, failed (no owner)
I CAN HELP  Intros to Ops + Network Assets; the meter data"""),
            trial=[
                ("A new manager arrives with a 47-slide operating model. What's your first move?",
                 "Book 30 minutes. Bring the Landscape Gift and ask the Measure Question."),
                ("They want to reintroduce something that failed before. What do you say?",
                 "Explain the history honestly, then help them try it better. Don't say “we tried that” and stop."),
                ("Your old manager was your champion. Does that carry over?",
                 "No. You start again with the new one. Earn it in the first 90 days."),
            ],
            last_word="A new lord remembers who helped them find the map. Be on the map.",
        ),
        # ------------------------------------------------------------------ 8
        dict(
            slug="ritual-circle-one-to-one",
            ring="SAME TIME NEXT WEEK ✠ ANYTHING FROM YOU ✠ QUICK ONE TODAY ✠", scrawl="it's your meeting",
            name="The Ritual Circle of the 1:1", sigil="◎",
            epithet="Thirty minutes a week that most people waste on status updates.",
            threat=2, habitat="Thursday afternoons, cancelled more often than held",
            weakness="an agenda you write, with decisions on it",
            summary="The Ritual Circle of the 1:1: turning your weekly one-to-one with your manager into the most useful meeting you have.",
            sighting=f"""<p>Pip's 1:1s with Victor went like this: Victor asked for status, Pip gave status, Victor gave four
new tasks, the meeting ended at 22 minutes. Twice a month it was cancelled for “something urgent”. Pip had never once
used it for anything he wanted.</p>
<p>The Annotator, over a drink, was appalled. “It's your meeting,” she said. “Not his. Write the agenda. Put the
status in an email. Use the time for the things that only he can do: decisions, blockers, your career.”</p>""",
            know=f"""<p>The 1:1 is the <b>only regular meeting where you set the agenda</b>, or could. Most people let it
become a status report, which wastes it: status belongs in writing. The 1:1 is for things that need a conversation:
decisions, problems, feedback, and your growth.</p>
<p>A manager with a good 1:1 rhythm feels informed (less micromanaging), makes decisions faster (less absence), and
knows what you want (less credit-taking). Many of this Act's creatures are tamed here.</p>
{note("If your 1:1 is all status, send the status the day before and walk in with a different list. Watch your manager relax.")}""",
            omens=[
                "Your 1:1 is a status report.",
                "It's cancelled more often than not.",
                "You've never discussed your career in it.",
                "You leave with more tasks than you came with, and no decisions.",
            ],
            counters=[
                ("The Shared Agenda", "Keep a running doc you both can edit. You fill it in before each 1:1. Status goes in writing; the meeting is for the rest.",
                 "“I've started a shared 1:1 doc. Status is at the top so we don't need to talk through it. The rest is decisions and questions.”"),
                ("The Monthly Career Slot", "Once a month, use the 1:1 for your development only.",
                 "“Could we use the last 1:1 each month for my development? This month: what level 5 would look like for me.”"),
                ("The Rescheduled, Not Cancelled", "When it's cancelled, ask for a new slot that week, even 10 minutes.",
                 "“No problem. Could we grab 10 minutes on Friday instead? I have one decision I need.”"),
            ],
            forbidden=[
                ("The Grievance Hour", 3, "Using every 1:1 to complain. Your manager will start cancelling, and you'll have earned it."),
                ("The Quiet Acceptance", 2, "Letting it die because they keep cancelling. No 1:1s means no relationship, and a surprise review."),
                ("The Status Monologue", 2, "Reading out your task list for 25 minutes. Send it. Nobody needs to hear a spreadsheet."),
            ],
            difficulty=dict(
                normal="A busy manager who's never thought about 1:1s. The Shared Agenda transforms it in two weeks.",
                nightmare="Constant cancellations. Ask for a shorter, fixed slot that's easier to keep.",
                hell="Your manager refuses 1:1s. Ask for a monthly one at least, and if that fails, build mentoring and skip-level relationships to fill the gap.",
            ),
            stats=[5, 5, 4, 4, 5, 4, 5, 4, 5], stats_for="The Shared Agenda",
            loot=("The 1:1 Doc",
                  "One running document. Newest on top. You fill it before each meeting.",
                  """1:1 · Pip / Victor · Thu 23 Jan
STATUS (read, don't discuss)  model v2 sent ✔ · sensitivity runs Fri
DECISIONS NEEDED              1. Heatwave scenario A or B (I recommend A)
BLOCKERS                      Substation 14 data: can you nudge IT?
FEEDBACK                      How did the board pack land?
FOR ME                        (monthly) what does level 5 look like?
AGREED / ACTIONS              ..."""),
            trial=[
                ("Your 1:1s are just status. What do you change first?",
                 "Send status in writing beforehand and bring a short list of decisions and questions."),
                ("Your manager cancels half your 1:1s. What do you ask for?",
                 "A shorter fixed slot, and a quick reschedule when it's cancelled."),
                ("How often should you talk about your career?",
                 "At least once a month, in a 1:1 set aside for it."),
            ],
            last_word="The 1:1 is the only throne room where you set the agenda. Sit in the chair.",
        ),
        # ------------------------------------------------------------------ 9
        dict(
            slug="skip-level-seance",
            ring="DOES YOUR MANAGER KNOW ✠ JUST CURIOUS ✠ MY DOOR IS OPEN ✠", scrawl="summon carefully",
            name="The Skip-Level Séance", sigil="✧",
            epithet="Summoning your boss's boss. Powerful. Dangerous. Read the instructions.",
            threat=4, habitat="skip-level 1:1s, open-door policies, the lift with the director",
            weakness="transparency: your manager knows you're summoning",
            summary="The Skip-Level Séance: when and how to go to your boss's boss, how to build that relationship safely, and the price of getting it wrong.",
            sighting=f"""<p>After three months of Victor, Pip booked a meeting with Benedict Crane (who, miraculously, was in
the building). He prepared a list of eleven problems with Victor. Halfway through, Benedict held up a hand. “Have you
raised these with Victor?” Pip had not. “Then do that first,” said Benedict, “and come back if it doesn't work.”</p>
<p>That evening, Victor knew. He didn't say how. He didn't need to. Their 1:1 the next day lasted four minutes.</p>""",
            know=f"""<p>Your boss's boss has <b>power over your manager</b> and, often, over your career: they're in your
calibration and promotion discussions. A good relationship with them is valuable. A complaint about your manager
delivered to them is <b>radioactive</b>: they must back their manager first, and the manager will almost always find out.</p>
<p>So: build the skip-level relationship <b>openly and regularly</b>, about work and ideas. Escalate problems only
after you've raised them with your manager, or when it's serious enough that you must (harm, ethics, safety).</p>
{note("A skip-level is a relationship, not an emergency exit. Visit when nothing's on fire, and they'll listen when something is.")}""",
            omens=[
                "You've never spoken to your boss's boss.",
                "You're tempted to “just mention” your manager's flaws to them.",
                "An “open door policy” that nobody seems to walk through.",
                "Calibration happens and you don't know who spoke for you.",
            ],
            counters=[
                ("The Open Summoning", "Ask your manager if you can have occasional skip-levels, and share what you'll discuss.",
                 "“Would you mind if I had a quarterly coffee with Benedict? I'd like to understand Strategy's priorities. I'll share what I learn.”"),
                ("The Idea Offering", "Bring the skip-level ideas and questions about the business, not complaints.",
                 "“What's the one thing you wish Grid Analytics did that we don't?”"),
                ("The Proper Escalation", "If you must escalate about your manager: raise it with them first, then tell them you're taking it further, then go with facts.",
                 "“Victor, I raised the workload twice and nothing changed. I'm going to talk to Benedict about it. I wanted you to hear it from me.”"),
            ],
            forbidden=[
                ("The Secret Séance", 5, "Complaining about your manager to their boss behind their back. Your manager will find out. Every manager finds out."),
                ("The Eleven Grievances", 4, "Bringing a long list. One problem, with facts and a request, is heard. Eleven is a rant."),
                ("The Name-Drop", 3, "“As I was saying to Benedict…” to your manager. You've just told them you're going over their head, as a threat."),
            ],
            difficulty=dict(
                normal="A healthy skip-level culture. Quarterly coffees, open and useful.",
                nightmare="Your manager is defensive about skip-levels. Keep it about the business, share notes, and build it slowly.",
                hell="Serious issues (harassment, safety, fraud) and your manager is part of it. Go to the skip-level, HR or the formal channel directly. Here, telling your manager first is not required.",
            ),
            stats=[3, 5, 3, 4, 3, 4, 5, 4, 3], stats_for="The Open Summoning",
            loot=("The Skip-Level Coffee Plan",
                  "Four quarterly questions that build the relationship without poisoning your manager's.",
                  """Q1  What are Strategy's top three priorities this year?
Q2  Where is Grid Analytics most / least useful to you?
Q3  What do you look for in people you promote?
Q4  What's one thing you'd change about how we work?

Share a 3-line summary with Victor after each one."""),
            trial=[
                ("You have serious frustrations with your manager. Do you go to their boss?",
                 "Not first. Raise them with your manager, clearly. If nothing changes, tell your manager you're escalating, then go with facts."),
                ("Is a regular skip-level coffee disloyal?",
                 "Not if it's open, agreed and about the business. It's how directors get to know the people they'll judge in calibration."),
                ("When can you go straight to the skip-level?",
                 "When it's serious (harm, harassment, safety, fraud), or when your manager is the problem in that sense."),
            ],
            last_word="Summon the higher power often, openly and for good reasons. Never in secret to curse your lord.",
        ),
        # ------------------------------------------------------------------ 10
        dict(
            slug="puppet-king",
            ring="I'LL TAKE IT UPSTAIRS ✠ NOT MY CALL ✠ LEAVE IT WITH ME ✠", scrawl="find the strings",
            name="The Puppet King", sigil="♙",
            epithet="Wears the crown. Can't sign anything.",
            threat=3, habitat="approval chains, “leave it with me”, decisions that never come back down",
            weakness="the strings: find out who really pulls them, and work with both",
            summary="The Puppet King: the manager with a title and no real power, and how to get things done anyway without humiliating them.",
            sighting=f"""<p>Victor approved Pip's plan for a second heatwave model. Then he “took it upstairs”. It came back
three weeks later, changed beyond recognition, approved by Ottoline. Victor had approved nothing; he had carried it.
He couldn't hire, couldn't spend more than £5,000, and couldn't move a deadline without asking Benedict, who asked
Ottoline.</p>
<p>Pip realised he had spent three months trying to persuade someone who could not say yes.</p>""",
            know=f"""<p>Some managers have <b>titles without authority</b>: new to the role, constrained by a central
team, or simply not trusted by their own boss. They can't make decisions, so they postpone them, carry them upwards
or quietly change them to please the real decider.</p>
<p>Don't humiliate them by going around them. Work <b>with</b> them to reach the real decider: help them build the
case, offer to join them upstairs, and make them look competent while you do it. A puppet who trusts you will show
you the strings.</p>
{note("Every puppet king knows exactly who holds the strings. Ask them gently and they'll usually tell you. They're relieved someone noticed.")}""",
            omens=[
                "“Leave it with me”, and it disappears.",
                "Approvals come back changed, from someone else.",
                "Your manager can't approve spend, hiring or deadlines.",
                "They're visibly nervous before meetings with their boss.",
            ],
            counters=[
                ("The Gentle Question", "Ask, kindly, who makes the final call and what they need to see.",
                 "“Who'll make the final decision on this? What do they need to see to say yes? I'd like to make it easy for you.”"),
                ("The Ammunition", "Prepare what your manager needs to win upstairs: a one-page case in the decider's language.",
                 "“I've written a one-page case for Ottoline, focused on billing complaints, since that's what she tracks.”"),
                ("The Joint Ascent", "Offer to go upstairs together, with them leading.",
                 "“Would it help if I came along when you present it to Benedict? You lead, I'll answer the data questions.”"),
            ],
            forbidden=[
                ("The Puppeteer's Bypass", 4, "Going straight to the real decider and cutting your manager out. They'll know, and they'll have nothing left to protect you with."),
                ("The Pity Glance", 3, "Treating them as powerless in front of the team. They'll feel it, and they'll resent you more than the strings."),
                ("The Eternal Wait", 2, "Waiting for decisions they can't make. Learn the strings or nothing moves."),
            ],
            difficulty=dict(
                normal="A new manager still earning authority. Help them build cases and it grows.",
                nightmare="A manager kept on a short leash. Use the Joint Ascent and give them the credit.",
                hell="A manager with no authority and no influence, who blocks you to look important. Build the skip-level relationship openly, and consider moving.",
            ),
            stats=[4, 4, 4, 3, 4, 5, 5, 3, 4], stats_for="The Ammunition",
            loot=("The Case in Their Language",
                  "One page for the person who really decides, written for what they care about.",
                  """FOR      Ottoline Grey (decides) · via Victor (owner)
ASK      Second heatwave model, £18k, 6 weeks
WHY SHE  Billing complaints in last heatwave: 2,400.
CARES    A better forecast cuts estimated bills by ~40%.
RISK     Without it: same complaints next summer, regulator review.
ASKED OF Decision by 14 Feb, so it's ready before May."""),
            trial=[
                ("Your manager keeps saying “leave it with me” and nothing happens. What do you ask?",
                 "Gently: who makes the final call, and what do they need to see? Then help your manager prepare it."),
                ("You've found out who really decides. Should you go straight to them?",
                 "No. Go with your manager, or prepare their case. Cutting them out burns the relationship you need."),
                ("How do you help a powerless manager gain power?",
                 "Make them look competent: give them strong cases, credit them, and help them win small decisions upstairs."),
            ],
            last_word="Don't cut the strings. Learn where they go, and help the king walk.",
        ),
        # ------------------------------------------------------------------ 11
        dict(
            slug="friend-became-boss",
            ring="NOTHING HAS CHANGED ✠ EVERYTHING HAS CHANGED ✠ STILL MATES ✠", scrawl="the pub is different now",
            name="The Friend Who Became Your Boss", sigil="⚯",
            epithet="Yesterday you shared complaints about the boss. Today they are the boss.",
            threat=3, habitat="the team you both used to be in, Friday drinks, the first awkward 1:1",
            weakness="an honest conversation, early, about how it'll work now",
            summary="The Friend Who Became Your Boss: when a peer or friend is promoted over you, and how to keep the friendship and the working relationship.",
            sighting=f"""<p>In January, Jules was made team lead of Grid Analytics. Pip found out in an email at 08:02. At
08:05 Jules messaged: <i>“Coffee? I want to talk before it gets weird.”</i> It was already a bit weird.</p>
<p>Over the next weeks Pip noticed things. Jules stopped joining the Friday moan about Victor. Jules asked about
deadlines in a new tone. Jules was, quite rightly, now in meetings about Pip. And Pip had applied for the same role,
which both of them knew and neither of them mentioned.</p>""",
            know=f"""<p>When a friend becomes your boss, <b>both of you lose something</b>: you lose an equal, they lose a
confidant. They now have duties to the company that may conflict with the friendship: reviewing you, deciding your
workload, keeping secrets about reorgs. It's awkward for them too, often more than for you.</p>
<p>Friendships survive this when both sides <b>name it early</b> and agree new rules: what you talk about at work,
what stays out of the pub, and how disagreements will happen. Unspoken, it rots.</p>
{note("If you also wanted the job, say so, once, kindly. “I wanted it, I'm a bit gutted, and I'm glad it's you.” Then it's said, and you can both move on.")}""",
            omens=[
                "A friend or peer is promoted over you.",
                "Conversations stop when they walk in.",
                "You're tempted to test them (“you've changed”).",
                "You both avoid the subject of the job you both wanted.",
            ],
            counters=[
                ("The Naming Rite", "Have the conversation early: congratulate, acknowledge the awkwardness, agree how you'll work.",
                 "“Congratulations, really. It's a bit strange for me, I'll admit. How do you want to handle the friend-and-boss thing?”"),
                ("The New Boundaries", "Agree what changes: no moaning about the team to them, no expecting favours, feedback at work, friendship outside it.",
                 "“Let's keep work at work. If I'm annoyed with a decision, I'll tell you in a 1:1, not at the pub.”"),
                ("The Visible Support", "Back them publicly in their first months. It helps them, and the team sees you're not a rival.",
                 None),
            ],
            forbidden=[
                ("The Insider Favour", 4, "Expecting easier treatment or inside information. They can't give it, and asking puts them in an impossible spot."),
                ("The Resentful Ally", 4, "Joining the people who resent their promotion. They'll know. Friendships rarely survive that."),
                ("The Old Moan", 3, "Still complaining about the team to them as if they were a peer. Now you're complaining to management."),
            ],
            difficulty=dict(
                normal="A good friend promoted fairly. The Naming Rite and clear boundaries make it work.",
                nightmare="You both wanted the job. Acknowledge it once, then support them visibly. Ask them to help you towards the next opportunity.",
                hell="They've changed for the worse with power, or they use the old friendship to pressure you. Treat them as a manager first, keep things in writing, and use the normal channels.",
            ),
            stats=[3, 4, 4, 3, 4, 5, 5, 4, 4], stats_for="The Naming Rite",
            loot=("The New Rules, Written Together",
                  "Agreed over coffee in week one. Not legally binding. Surprisingly effective.",
                  """AT WORK     Jules is my lead. Disagreements in 1:1s, not in public.
OUTSIDE     Friends. No work moaning at the pub.
FEEDBACK    Jules gives it straight. I take it as from a lead.
SECRETS     If Jules can't tell me something, Jules says so.
MY GROWTH   Jules helps me towards level 5 / the next lead role.
REVIEW      Check in on these rules in 3 months."""),
            trial=[
                ("Your friend is promoted to be your boss. What's your first move?",
                 "The Naming Rite: congratulate them, acknowledge it's strange, and agree how you'll work."),
                ("You both applied for the job. Do you mention it?",
                 "Once, kindly: “I wanted it, I'm a bit gutted, and I'm glad it's you.” Then let it go."),
                ("At Friday drinks, colleagues start moaning about your friend's decisions. What do you do?",
                 "Don't join in, and don't report it. Change the subject, or say: “I'd rather talk to Jules about it directly.”"),
            ],
            last_word="Say the awkward thing once, out loud, early. Then you get to keep the friend.",
        ),
        # ------------------------------------------------------------------ 12
        dict(
            slug="escape-portal", flagship=True,
            plate_caption="Floor 9, 19:40. The portal was always there. Most people only see it when the throne room gets dark enough.",
            ring="IS IT ME OR IS IT THEM ✠ STAY OR GO ✠ THE DOOR IS OPEN ✠", scrawl="leave well",
            name="The Escape Portal", sigil="⛩",
            epithet="Sometimes the best counter-spell is the door.",
            threat=5, habitat="Sunday evenings, LinkedIn notifications, a recruiter's “quick chat”",
            weakness="a plan, made calmly, before you need it",
            summary="The Escape Portal: recognising when it's time to leave a bad manager, choosing between an internal move and leaving, and leaving well.",
            sighting=f"""<p>By February Pip had tried most of this Act. The Rhythm Ward had calmed Victor's eye a little. The
1:1 doc helped. But Victor still took the credit, still changed his mind every Tuesday, and still sent messages at
23:00. Pip's Sunday evenings had developed a particular taste.</p>
<p>Then Priya Nair stopped him in the lift. “I've got an analytics lead role in Customer Ops,” she said. “You'd be
good at it. No pressure.” That evening, a recruiter also messaged. Pip sat on floor 9 after everyone had gone and
stared at the exit sign for a long time. It was, he thought, the only light in the building that told the truth.</p>""",
            know=f"""<p>Not every bad manager can be managed. Sometimes the job is <b>costing more than it gives</b>:
your health, your growth, your evenings. Signs that it's time: you've genuinely tried the counter-spells for months,
nothing has changed, and you're shrinking.</p>
<p>The portal has <b>several doors</b>. An internal move keeps your network, history and pension, and often changes
everything that matters (your manager). An external move resets more. Staying with a clear end date is also a
choice. What matters is that you choose, <b>calmly and with a plan</b>, rather than flee on a bad Tuesday.</p>
{note("Never resign on a bad day. Decide on a good day. If you still want to go on a good day, go.")}""",
            omens=[
                "Sunday evenings feel like dread.",
                "You've tried for months and nothing has changed.",
                "You're no longer learning, only coping.",
                "Your health, sleep or relationships are suffering.",
                "Someone good offers you a door, and you feel relief.",
            ],
            counters=[
                ("The Honest Ledger", "Write down what the job gives you and what it costs. Re-read it on a good day.",
                 None),
                ("The Inside Door", "Explore an internal move first: different manager, same company. Talk to the hiring manager before telling yours.",
                 "“Priya, I'm interested. Could we talk about what the role really involves before I mention it to Victor?”"),
                ("The Quiet Preparation", "Update your CV, talk to your network, and save some money before you need to. Options make you calmer, even if you stay.",
                 None),
                ("The Good Exit", "If you go, leave well: notice served properly, handover written, no burning of bridges. The company is smaller than you think.",
                 "“I've accepted a role in Customer Ops. I'll write a full handover for the heatwave model and train whoever takes it on.”"),
            ],
            forbidden=[
                ("The Rage Quit", 5, "Resigning in the middle of a bad meeting. It feels magnificent for an hour. Then there's rent."),
                ("The Scorched Exit", 5, "A farewell email listing everyone's failings. It will be forwarded. It will follow you to your next job."),
                ("The Haunting", 3, "Staying, miserable, and telling everyone how miserable you are, for years. You become the Doom Prophet (Act II)."),
            ],
            difficulty=dict(
                normal="A bad patch with a decent manager. Try the counter-spells for three months before deciding.",
                nightmare="A manager who won't change and a job that's stalling your growth. Explore an internal move seriously.",
                hell="Your health is suffering, or you're being harassed or bullied. Protect yourself first: talk to a doctor, HR or a lawyer, and leave as soon as you safely can.",
            ),
            stats=[5, 4, 5, 4, 4, 4, 5, 2, 4], stats_for="The Inside Door",
            loot=("The Stay-or-Go Ledger",
                  "Fill it in on a calm day. Score each 1–5. Compare in a month.",
                  """                    NOW (Victor)   CUSTOMER OPS (Priya)
Learning                 2               4
Manager                  2               4  (ask her team!)
Work I care about        4               4
Pay / level              3               4
Sunday evenings          1               ?
Network / history        5               5  (same company)
Risk                     low             medium

Decide on a GOOD day. Talk to Priya's team first."""),
            trial=[
                ("You've had a terrible meeting and want to resign today. What should you do?",
                 "Nothing today. Write the Honest Ledger. Decide on a good day."),
                ("You're offered an internal role. Who do you tell first?",
                 "Talk to the hiring manager first about the role. Tell your manager once it's real, before it's public."),
                ("How do you leave well?",
                 "Proper notice, a thorough handover, thanks where it's due, and no farewell essay. The industry is small."),
            ],
            last_word="Every throne room has a door. The trick is walking through it on a good day, with a plan.",
        ),
    ],
)
