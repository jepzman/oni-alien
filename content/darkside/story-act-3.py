# Series 4 · Act III · the long-form story fields (format v2), merged into content/darkside/act-3.py by scripts/grimoire.py.
# Winter 2026–27, after Act I's reorg: Pip in Grid Analytics (Strategy) under Victor Kraal.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the All-Seeing Eye
    "all-seeing-eye": dict(
        sighting=f"""{beat("Monday 2 December · Victor's first week")}
<p>Victor asked Pip for a status update at 09:00, 11:00, 14:00 and 16:00. Pip gave four updates. Nothing had changed
between them except the time.</p>
{beat("Wednesday · the edits")}
<p>Victor began editing Pip's emails before they were sent. He asked Pip to share his screen “just to see where you are”.
He moved a decimal point in the load model himself, at 23:10, and left a comment: <i>“Fixed. Pls check before sending
things.”</i> The decimal had been right. Victor had moved it to the wrong place.</p>
{beat("Tuesday 10 December · 16:02")}
<p>There was a sticky note on Pip's monitor: <i>“UPDATE PLS (3rd time today) — V.”</i> Victor sat four metres away. He
could have just asked. He had, in fact, asked. Twice.</p>
{beat("Friday · the team")}
<p>Two analysts had started copying Victor on every email “to be safe”. One had stopped making any decision at all
without asking. The team's output had dropped by a third in a fortnight. Victor, noticing, increased the check-ins.</p>
{note("Micromanagement is a trust problem wearing a productivity costume. Feed the trust and the costume falls off.")}""",
        origin=dict(
            title="How a consultant became the All-Seeing Eye",
            beats=[
                ("2014 · a junior consultant", "Victor joins a consultancy where time is billed in 15-minute blocks and every slide is checked by a partner. Checking everything is the job."),
                ("2021 · the decimal", "One of Victor's analysts sends a client a model with a misplaced decimal. The client cancels a £2 million contract. Victor, as the manager, is nearly fired. He keeps his job by promising it will never happen again."),
                ("2021 to 2025 · the promise", "Victor keeps the promise the only way he knows: by checking everything, personally, at all hours. His teams never make that mistake again. They also never grow."),
                ("December 2026 · MetroVolt", "Victor arrives with a new team he doesn't know, a boss who's never there and a reputation to make. Every unanswered question feels like 2021 again. So he asks, and asks."),
            ],
            turning="One decimal point that nearly ended his career, and a promise that he'd never trust anyone's work unchecked again.",
            saved="A partner who said in 2021: “That was a process failure, not yours. Let's fix the review process.” Instead, the lesson he took was “trust no one”.",
            note="Behind most micromanagers is a mistake that once cost them dearly. Predictable updates heal it slowly, because they prove, week by week, that nothing is being missed.",
        ),
        know=f"""<p>Micromanagers are usually driven by <b>anxiety</b>, not contempt. They're new, under pressure from above, or
they've been burned. Watching closely feels like control. Not knowing feels like danger. The cure is to <b>remove the
not-knowing</b>: regular, predictable information before they ask.</p>
<h3 class="kh">What it wants</h3>
<p>Certainty that nothing will go wrong without it knowing. Above all, no surprises from below reaching anyone above.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because Victor is new, his boss is absent, and Rupert Thorne visits monthly to find faults. Every error in Grid Analytics
lands on Victor. Checking feels like his only protection.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Silence from the team.</li><li>Surprises in front of its own boss.</li><li>Errors it didn't catch.</li><li>Losing control of what goes upwards.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The New &amp; Nervous</b><p>Doesn't know the team yet. Calms down in weeks with good updates.</p></div>
<div><b>The Squeezed</b><p>Micromanaged from above, passing it down. Help them answer upwards.</p></div>
<div><b>The Controller</b><p>Control is personality. Updates help a little; boundaries help more.</p></div>
</div>
{note("Answer the question before it's asked, and the eye starts to close.")}""",
        difficulty=dict(
            normal=dict(who="The New &amp; Nervous. A new manager learning the team.",
                        know=["It started when they arrived.", "They relax when they get information.", "They're anxious, not hostile."],
                        do=["Offer the Rhythm Ward: updates at fixed times, before they ask.", "Flag risks early with a plan B.", "After two weeks, ask to step down to fewer updates."],
                        avoid="The blackout: going quiet to prove you don't need watching.",
                        next="If updates change nothing because they're being squeezed from above, you're at Nightmare."),
            nightmare=dict(who="The Squeezed. Micromanaged by their own boss.",
                           know=["The checking spikes before their own meetings.", "They ask for things their boss asked them.", "They seem scared, not controlling."],
                           do=["Find out what their boss asks them, and supply it before they ask.", "Agree a Working Agreement: what you decide alone, what needs them.", "Keep the Rhythm Ward going.", "Make them look good upwards."],
                           avoid="Malicious compliance: asking permission for every tiny thing to make a point.",
                           next="If months of reliable updates change nothing, you're at Hell."),
            hell=dict(who="The Controller. Nothing reassures them.",
                      know=["Months of updates have changed nothing.", "They redo your work, always.", "It's affecting your health or growth."],
                      do=["Keep the updates; protect your evenings.", "Document decisions and their edits.", "Talk to your skip-level about development.", "Start planning a move (the Escape Portal)."],
                      avoid="The public rebuke. True and unforgettable, in the wrong way.",
                      next="If it's damaging your health, it's no longer a management style; it's a reason to leave."),
        ),
        mirror=dict(
            title="Are you the Eye?",
            intro="If you lead anyone, check your own gaze. Tick honestly.",
            signs=["You've asked for the same update twice in a day.", "You redo other people's work rather than giving feedback.", "You need to approve things your team could decide.",
                   "You feel anxious when you don't know what someone's doing.", "Your team copies you on everything “to be safe”."],
            cure="Agree with each person what they decide alone, and what you need to hear about. Then let them. If something goes wrong, fix the process, not the trust.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 10 December, 16:05. Pip walks the four metres to Victor's desk.",
            intro="The Rhythm Ward and the Working Agreement: give the anxiety what it needs, on a schedule.",
            lines=[
                ("Pip", "Victor, I found your note. Can I suggest something? I'll send you a three-line update at 10 and 4 every day, so you're never wondering where things are."),
                ("Victor", "…That would help, actually."),
                ("Pip", "And could we agree what I decide alone? Model choices and formatting with me; anything going to Benedict or above, you approve."),
                ("Victor", "Fine. But tell me if anything changes between updates."),
                ("Pip", "Deal. Risks I'll flag straight away, with a plan B."),
                ("", "Two weeks of updates, on the minute. In week three, Victor says: “Let's try once a day.” In week five, the sticky notes stop."),
            ],
            note="Pip never told Victor he was micromanaging. He gave him the certainty he was desperate for, on a schedule. The hovering faded by itself.",
        ),
    ),
    # ------------------------------------------------------------------ the Absent Lord
    "absent-lord": dict(
        sighting=f"""{beat("October to February · the calendar")}
<p>Benedict Crane, Director of Strategy, had a calendar that looked like a bruise: solid purple, marked “travelling”.
In four months he was in The Grid for nine days.</p>
{beat("Monday 6 January · the question")}
<p>Pip needed one decision for the Q1 forecast: the regulator's heatwave scenario, or MetroVolt's own? He emailed. He
messaged. He booked a call, which moved three times, then disappeared.</p>
{beat("Monday 20 January")}
<p>After two weeks of silence, Victor decided (the regulator's) so the work could continue. Pip noted it in the project log.</p>
{beat("Thursday 6 February · the board")}
<p>Benedict, back for one day, asked at the board with real anger: <i>“Why was I not consulted on the scenario?”</i>
Victor looked at Pip. Pip looked at the email thread, which contained six follow-ups, a meeting request and a message
that began “Sorry to chase again”.</p>
{note("An absent boss is a boss who'll read the first two lines on their phone in a taxi. Write the first two lines for the taxi.")}""",
        origin=dict(
            title="How a sharp analyst became the Absent Lord",
            beats=[
                ("2015 · the best analyst", "Benedict is the best analyst in MetroVolt's strategy team. He's promoted, then promoted again, each time for being “strategic”."),
                ("2020 · the committees", "At MetroVolt, “strategic” means being in rooms. Benedict joins one committee, then five, then fourteen. Each one wants him in person."),
                ("2023 · the inbox", "Benedict now gets 400 emails a day. He reads the subject lines, answers what's on fire, and plans to come back to the rest. He never does."),
                ("2026 · the ghost of himself", "His team sees him nine days in four months. He cares about them. He just has nothing left for them by the time he gets back. Then, at the board, his own boss asks a question, and suddenly everything matters at once."),
            ],
            turning="Being rewarded for being in every room, until there was no time left for his own.",
            saved="A boss who measured him on his team's output, not his committee count. Or a chief of staff to do for him what Ottoline does for the CEO.",
            note="Most absent bosses aren't uncaring. They're drowning in a job designed to make them absent. Short, decidable messages are a kindness to them, too.",
        ),
        know=f"""<p>Absent managers are usually <b>overloaded and badly organised</b>, not uncaring. Long questions get postponed.
Open questions get ignored. Then, when it matters, they suddenly care, because someone above them is asking. The fix is to
make deciding <b>effortless</b>: one short message, two options, your recommendation, a default and a deadline.</p>
<h3 class="kh">What it wants</h3>
<p>To stay informed without effort, and not to be embarrassed in front of its own boss.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt rewards senior people for being in meetings, not for being reachable. And their teams, too polite to
decide without them, wait.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Being surprised by its own boss.</li><li>Decisions made without it, silently.</li><li>Long emails it can't answer from a taxi.</li><li>Being shown, in writing, how long it took to reply.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Overloaded</b><p>Too many rooms. Grateful for short, decidable messages.</p></div>
<div><b>The Strategist</b><p>Thinks detail is beneath them. Needs to know what's above the detail.</p></div>
<div><b>The Ghost</b><p>Has checked out. Decide with your direct manager and keep a record.</p></div>
</div>
{note("If they won't decide, make not deciding a decision too. In writing. With a date.")}""",
        difficulty=dict(
            normal=dict(who="The Overloaded. Busy, but reachable.",
                        know=["They reply to short messages.", "They're apologetic about delays.", "They do read subject lines."],
                        do=["Use the Default Rune: two options, your recommendation, a default, a deadline.", "Put the ask in the subject line.", "Ask for a 15-minute standing slot."],
                        avoid="The waiting game: doing nothing until they reply.",
                        next="If they're unreachable for weeks, you're at Nightmare."),
            nightmare=dict(who="The Strategist or the Ghost. Unreachable for weeks.",
                           know=["Decisions stall for weeks.", "Your manager can't reach them either.", "They're angry about delays they caused."],
                           do=["Agree in advance which decisions your manager can make in their absence.", "Default decisions, in writing, copied to your manager.", "Keep a decision log they can read in five minutes.", "Book their assistant, not them."],
                           avoid="The silent override: deciding without telling them.",
                           next="If they're absent and then blame you, you're at Hell."),
            hell=dict(who="Absent, then blaming.",
                      know=["You're blamed for decisions you couldn't get.", "Your follow-ups are ignored, then disputed.", "Your manager is caught in the middle."],
                      do=["Every decision in writing, with defaults and dates.", "Copy your direct manager on all of it.", "Keep calm records; never “as per my six emails”.", "Ask, once things calm down, how they'd like decisions flagged."],
                      avoid="The passive reminder: “just bumping this 🙂” for the sixth time. Change the format, not the frequency.",
                      next="If blame lands on you regardless, raise the pattern with your manager and skip-level, with the record."),
        ),
        mirror=dict(
            title="Are you absent?",
            intro="Busy people become absent without noticing. Tick honestly.",
            signs=["Someone in your team is waiting for a decision from you right now.", "You've rescheduled the same 1:1 three times.", "You have more than 50 unread emails from your own team.",
                   "You've been surprised by work you assigned.", "You've been angry about a delay you caused."],
            cure="Give your team a written list of what they can decide without you, and a default rule: if you haven't replied in three days, they proceed and tell you.",
        ),
        rehearsal=dict(
            title="Scene: Monday 6 January, 09:12. Pip writes the email again.",
            intro="The Default Rune and the Taxi Summary: one decision, decidable from a phone.",
            lines=[
                ("", "Subject: DECIDE BY THU 12:00: Q1 heatwave scenario (I recommend A)"),
                ("Pip", "Benedict, one decision for the Q1 forecast. A) regulator's heatwave scenario (I recommend; the board expects it). B) our own (2% lower peak). If I don't hear by Thursday 12:00, I'll use A. Victor is copied and agrees."),
                ("", "Thursday, 11:48. A reply arrives from an airport."),
                ("Benedict", "A. Thanks for making it easy."),
                ("", "February's board: nobody asks why Benedict wasn't consulted. He was. In four words, from Gate 22."),
            ],
            note="Same question as before. The only change was the format: subject line, two options, a default, a deadline. The busiest man in MetroVolt answered in under three days.",
        ),
    ),
    # ------------------------------------------------------------------ the Seagull Overlord
    "seagull-overlord": dict(
        sighting=f"""{beat("Thursday 16 January · 09:00 · arrival")}
<p>Rupert Thorne, Interim Transformation Director from the parent group, arrived at The Grid for his monthly visit. He
had a coffee (flat white), a train ticket (14:05 to London) and opinions.</p>
{beat("10:20 · eleven minutes")}
<p>He looked at the Lumen plan for eleven minutes and announced: “This is too slow. Do the city centre first. And use
the new vendor. I've seen this work in Rotterdam.” Nobody explained why the city centre was last (underground cabling,
permits not due until February) or why the current vendor had been chosen (the new one had failed a security review).
Rupert didn't ask.</p>
{beat("14:05 · departure")}
<p>Rupert caught the 14:05 to London. Behind him: a strategy board covered in his “quick thoughts”, two changed
priorities and a team that spent the next three weeks un-changing the plan.</p>
{beat("Thursday 13 February · the next visit")}
<p>Rupert returned and asked why Lumen was three weeks late.</p>
{note("The Seagull isn't stupid. It's under-informed and over-powered. Fix the first one and the second matters less.")}""",
        origin=dict(
            title="How a turnaround expert became the Seagull Overlord",
            beats=[
                ("2019 · Rotterdam", "Rupert is sent to a failing subsidiary in Rotterdam. He makes bold changes in 90 days. It works, partly because Rotterdam needed exactly those changes."),
                ("2020 · the reputation", "The parent group makes him its “turnaround” man. He's sent to subsidiaries that look slow. He's measured on visible change within 90 days."),
                ("2021 to 2025 · the formula", "In every new place, Rupert does what worked in Rotterdam. Big, visible changes feel like leadership. He's always on the train before the cost of the changes arrives."),
                ("2026 · MetroVolt", "Rupert visits monthly. He has eleven minutes per project, no context and a mandate to change things. So he changes things. Each visit, he sees only the delay from the last one."),
            ],
            turning="One success in Rotterdam that became a formula, applied everywhere, by someone who never stayed to see the results.",
            saved="Being measured on outcomes six months later, not visible change in 90 days. Or someone briefing him properly before every visit.",
            note="A Seagull has usually been right somewhere, once. That's why it's so confident. Show it why here is different, before it lands.",
        ),
        know=f"""<p>The Seagull is a senior person with <b>little context and a lot of authority</b>. It visits briefly, feels it
must add value, and so it changes things. You can't stop the visits. But you can <b>shape what it sees</b>: brief it before
it lands, show the reasons behind the plan, and give it something useful to say yes to.</p>
<h3 class="kh">What it wants</h3>
<p>To leave a visible mark, quickly, and to report progress to the group.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because the parent group measures Rupert on visible change, not on outcomes, and because nobody at MetroVolt briefs him
before he arrives. Into an empty head, any idea fits.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Context it didn't have.</li><li>Being shown the cost of its last visit.</li><li>Leaving with nothing to report.</li><li>A director who speaks for the plan with confidence.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Visitor</b><p>Well-meaning, under-informed. A pre-landing brief turns it into an ally.</p></div>
<div><b>The Fixer</b><p>Measured on change. Give it a real thing to fix.</p></div>
<div><b>The Tourist</b><p>Wants a show. Give it a short demo and a bone to carry home.</p></div>
</div>
{note("Feed the seagull before it lands, and it eats from your hand instead of your plan.")}""",
        difficulty=dict(
            normal=dict(who="The Visitor. An occasional senior visitor with good intentions.",
                        know=["They ask questions when given context.", "Their ideas are reasonable, just uninformed.", "Your director supports the current plan."],
                        do=["Send a one-page brief two days before the visit.", "Explain constraints calmly when they suggest changes.", "Write down what was really agreed afterwards."],
                        avoid="The instant yes: agreeing to every change in the room.",
                        next="If every visit brings disruption, you're at Nightmare."),
            nightmare=dict(who="The Fixer. Monthly disruption.",
                           know=["Plans change most in the week after a visit.", "The team quietly undoes visit decisions.", "Nobody speaks for the plan in the room."],
                           do=["Agree with your director who speaks for the plan in the visit.", "Give the Seagull a real problem to fix (the Bone to Carry Home).", "Always do the Written Echo afterwards.", "Track the cost of each change."],
                           avoid="Hide-and-seek: avoiding the visit. It'll talk to someone with less context.",
                           next="If its changes override your director's, you're at Hell."),
            hell=dict(who="The Seagull outranks your director and overrules them.",
                      know=["Your director's plans are overturned monthly.", "Nobody can say no to the visitor.", "Delays are blamed on the team."],
                      do=["Document the cost of each change (weeks, money).", "Help your director escalate the pattern with facts.", "Propose a simple change process the visitor must use.", "Keep your own records of what was decided."],
                      avoid="The eye-roll debrief: mocking him after he leaves. It reaches London before he does.",
                      next="If the plan is never stable, raise the delivery risk formally, in writing."),
        ),
        mirror=dict(
            title="Are you a Seagull?",
            intro="Anyone who visits a team can become one. Tick honestly.",
            signs=["You've changed a plan in a meeting without asking why it was that way.", "You've said “I've seen this work elsewhere” this year.", "You rarely see the results of your suggestions.",
                   "You feel you must add something in every review.", "Teams go quiet when you arrive."],
            cure="Before you suggest a change, ask “why is it this way?” and listen to the whole answer. Then ask what would help, not what should change.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 13 February, 10:20. Rupert's next visit. This time he's been briefed.",
            intro="The Reason Reveal and the Bone to Carry Home.",
            lines=[
                ("Rupert", "This is still too slow. Why isn't the city centre first?"),
                ("Pip", "Good question. It's last because the cabling permits arrive in February. It's on page 1 of the brief we sent Tuesday. What's the worry behind going faster: the regulator date?"),
                ("Rupert", "…Yes. The group wants to see Lumen on track."),
                ("Pip", "It is: 62% done, on track for 31 March. One thing you could genuinely help with: the group security review for the new vendor is stuck. Unblocking it would save three weeks in phase 2."),
                ("Rupert", "Leave that with me. I know the CISO."),
                ("", "14:05: Rupert leaves with one job and no changes to the plan. Pip's Written Echo arrives in his inbox by 15:00. Three weeks later, the security review is approved."),
            ],
            note="The Seagull still needed to do something. Pip gave it something useful to do, and the plan survived the visit.",
        ),
    ),
    # ------------------------------------------------------------------ the Weather Tyrant
    "weather-tyrant": dict(
        sighting=f"""{beat("Monday 13 January · ☀️")}
<p>Seconded to Network Assets for the meter fix, Pip met good-day Gareth. Gareth bought pastries, told funny stories about
the 2009 blackout, and approved the meter-fix plan in four minutes.</p>
{beat("Tuesday 14 January · ⛈️")}
<p>Bad-day Gareth slammed his laptop shut, called the same plan “unacceptable”, and made a junior engineer cry over a
font. Nothing had changed except that Gareth had had a call with the executive committee at nine.</p>
{beat("Every morning · the forecast")}
<p>The team had a private chat called <i>☀️ / ⛈️</i>. Someone posted the forecast each morning after seeing Gareth in the
lift. Nobody brought bad news on a ⛈️ day. Bad news therefore arrived in large, late piles on ☀️ days, which made them ⛈️ days.</p>
{beat("Monday 20 January · the line")}
<p>In budget week, Gareth shouted at Sam from Field Ops in front of the whole team. Sam left the room. Pip wrote the date
down. That was no longer weather.</p>
{note("You can work for a moody manager for a while. You can't work for a cruel one. Learn the difference early: moods change; cruelty repeats.")}""",
        origin=dict(
            title="How a decent engineer became the Weather Tyrant",
            beats=[
                ("2009 · the blackout", "Gareth is a young engineer on the night of the blackout. He sees his director scream at people for hours. Everyone remembers that night as the night the director “took control”."),
                ("2015 to 2021 · climbing", "Gareth rises through Network Assets. He's never trained to manage people. He manages the way he was managed: calm when things are fine, loud when they aren't."),
                ("2022 · the Tuesday calls", "Gareth joins the weekly executive committee call. His own boss criticises him on it, often in front of peers. He leaves every Tuesday call humiliated and furious."),
                ("2026 · the forecast", "The pressure goes straight into his team. Tuesdays are storms. Budget weeks are hurricanes. Gareth doesn't see the pattern. His team can predict it to the hour."),
            ],
            turning="A blackout night when shouting looked like leadership, and the Tuesday calls that taught him to pass pressure downwards.",
            saved="Management training, any time in fifteen years. And a boss who didn't humiliate him on Tuesdays.",
            note="Moody managers usually pass on weather from above. That explains the storms. It doesn't excuse shouting at Sam.",
        ),
        know=f"""<p>Moody managers are usually <b>stressed and poorly regulated</b>: they bring pressure from above straight into the
room. Their moods have patterns. You're not responsible for their weather, but you can <b>forecast it</b>, time your asks
and keep your own behaviour steady. And there is a line: shouting, humiliation or fear is not weather. It's <b>conduct</b>.</p>
<h3 class="kh">What it wants</h3>
<p>Relief from pressure it can't control. Bad moods are how it discharges that pressure.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt promotes engineers into management without training them, and because the culture at the top is
harsh. Pressure flows downhill, and nobody stops it at Gareth's door.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Its own boss.</li><li>Bad news on a bad day.</li><li>Being shown its pattern.</li><li>Formal complaints.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Pressure Cooker</b><p>Stressed from above. Better with early news and calm.</p></div>
<div><b>The Mood-Driven</b><p>Swings with no clear trigger. Needs written approvals.</p></div>
<div><b>The Bully</b><p>Shouts, humiliates, frightens. Not weather: conduct. Use the formal channel.</p></div>
</div>
{note("You can't control the weather. You can control whether you bring an umbrella, and a written record.")}""",
        difficulty=dict(
            normal=dict(who="The Pressure Cooker. Occasional bad days under pressure.",
                        know=["Storms follow obvious triggers.", "They apologise afterwards.", "Good days are genuinely good."],
                        do=["Notice the pattern; time big asks for good windows.", "Stay steady whatever the weather.", "Get approvals in writing on good days."],
                        avoid="Storm chasing: holding urgent bad news for a good day.",
                        next="If swings affect decisions often, you're at Nightmare."),
            nightmare=dict(who="The Mood-Driven. Frequent swings that change decisions.",
                           know=["Approved work gets rejected on bad days.", "The team runs a mood forecast.", "Bad news arrives late, in piles."],
                           do=["Written approvals, always.", "Deliver bad news early and short, with a plan.", "On a good day, tell them calmly about the impact of the swings.", "Keep a private Weather Log."],
                           avoid="Becoming the weather: snapping back or sulking.",
                           next="If moods turn into shouting or humiliation, you're at Hell."),
            hell=dict(who="The Bully. Shouting, humiliation, tears.",
                      know=["People have been shouted at in public.", "Colleagues are scared.", "It repeats."],
                      do=["Support the person targeted, afterwards.", "Keep a dated, factual record.", "Raise it with HR or the skip-level, or help the target do so.", "If it's you: “I'm not OK being shouted at. Can we talk about what went wrong?”"],
                      avoid="The forecast channel. Funny until it's screenshotted, then it's a disciplinary, for you.",
                      next="If HR won't act, protect yourself and plan your exit. You don't have to wait for it to happen to you."),
        ),
        mirror=dict(
            title="Are you the weather?",
            intro="Pressure travels. Check whether it travels through you. Tick honestly.",
            signs=["Your team checks your mood before asking you things.", "You've rejected something you'd approved, after a bad meeting.", "You've raised your voice at someone at work this year.",
                   "People bring you bad news late.", "You feel better after letting off steam at someone junior."],
            cure="After a bad meeting, wait 20 minutes before talking to your team. And when you snap, apologise the same day, specifically. The forecast improves fast.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 14 January, 10:05. A ⛈️ day. Pip has urgent news.",
            intro="The Steady Hand and the Written Approval: calm, short, and with a record.",
            lines=[
                ("Gareth", "What now?"),
                ("Pip", "I can see today's tough. Two-minute version: the meter vendor's delivery slips a week. Plan B is attached, and it keeps us on track."),
                ("Gareth", "And the plan you showed me yesterday? It's unacceptable."),
                ("Pip", "Yesterday we agreed that plan; I noted it in the log. Has something changed I should know about?"),
                ("Gareth", "…ExCo wants it faster."),
                ("Pip", "Understood. Shall I bring you two options for faster, at four, when you've had a breather?"),
                ("Gareth", "…Four. Fine."),
            ],
            note="Pip didn't absorb the storm or reflect it. He stayed level, pointed calmly to the record, found the real trigger (ExCo) and picked a better time.",
        ),
    ),
    # ------------------------------------------------------------------ the Conflict Phantom
    "conflict-phantom": dict(
        sighting=f"""{beat("2022 to 2026 · the kindest manager")}
<p>Marcus Bell was the kindest manager Pip ever had. He remembered birthdays. He took the blame in public. He once drove
an analyst to hospital at midnight.</p>
{beat("Four years · Neville")}
<p>For four years he let Neville (the Coasting Zombie, Act II) do almost nothing, because talking to Neville would have
been awkward. The rest of the team carried Neville's work. Two good analysts left. Their exit interviews mentioned “workload
fairness”. Marcus read them, felt terrible and did nothing.</p>
{beat("Every 1:1 · the hug")}
<p>When Pip asked Marcus for honest feedback, Marcus said “you're doing great” and changed the subject to football. Pip
asked again in a different way. Marcus said “honestly, nothing major” and asked about Pip's weekend.</p>
{beat("October · calibration")}
<p>Pip found out at calibration that he was “not quite ready for level 4”. The reasons were in a document Marcus had
helped write. Nobody had told Pip any of them.</p>
{note("“You're doing great” is not feedback. It's a hug. Hugs are nice. They don't get you promoted.")}""",
        origin=dict(
            title="How a kind boy became the Conflict Phantom",
            beats=[
                ("1980s · a loud house", "Marcus grows up with a father who shouts. Every disagreement at home is a frightening one. He learns to keep the peace, to make people laugh, to smooth things over."),
                ("1990s · a promise", "As a teenager, Marcus promises himself he will never make anyone feel the way his father made him feel."),
                ("2012 · a manager", "Marcus becomes a manager and keeps the promise. He's warm, generous and safe. His team adores him."),
                ("2016 onwards · the cost", "But to Marcus, every hard conversation feels like shouting. So he doesn't have them. Problems are postponed, feedback is softened into nothing, and his kindness quietly becomes avoidance. The people who pay are the ones he most wants to protect."),
            ],
            turning="A childhood promise to never be cruel that, over the years, became a rule never to be honest.",
            saved="Someone teaching him that clear feedback, kindly given, is the opposite of shouting. The kindest managers are clear ones.",
            note="Conflict Phantoms usually avoid conflict because, somewhere, they learned it was dangerous. Specific, gentle questions make honesty feel safe for them, too.",
        ),
        know=f"""<p>Conflict-avoidant managers want to be <b>liked</b> and want people to be happy. Hard conversations feel like
cruelty to them. So problems are postponed, feedback is softened into nothing, and decisions that would upset someone
don't get made. The cost lands on <b>you</b>. You can make the hard thing <b>easier to say</b>.</p>
<h3 class="kh">What it wants</h3>
<p>Harmony. Everyone happy, nobody upset, no raised voices.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt rewards managers with high engagement scores and few complaints, and conflict-avoidant managers have
both, right up until the good people leave.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Upsetting anyone.</li><li>Big, emotional confrontations.</li><li>Being seen as unfair.</li><li>Having to deliver bad news.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Peacekeeper</b><p>Avoids conflict to protect people. Responds to specific, gentle questions.</p></div>
<div><b>The People-Pleaser</b><p>Wants to be liked. Responds to pre-solved problems that please everyone.</p></div>
<div><b>The Absentee</b><p>Avoids by disappearing. Needs things in writing and the skip-level.</p></div>
</div>
{note("Kindness that avoids the truth isn't kindness. Ask the question that makes the truth easy to say.")}""",
        difficulty=dict(
            normal=dict(who="The Peacekeeper. A kind manager who softens feedback.",
                        know=["Feedback is always “great”.", "They answer specific questions honestly.", "Problems do get fixed, slowly."],
                        do=["Ask specific, low-threat questions.", "Ask for one thing to start, one to stop.", "Thank them for honest answers, so honesty feels safe."],
                        avoid="Accepting the hug. Next year's review will say otherwise.",
                        next="If problems are festering (workload, an underperformer), you're at Nightmare."),
            nightmare=dict(who="The People-Pleaser. Problems festering for years.",
                           know=["Unfair workloads are tolerated.", "Good people leave.", "1:1s drift to small talk whenever you raise a problem."],
                           do=["Bring pre-solved problems, one at a time, in writing.", "Prepare for calibration: ask what will be said about you.", "Make the hard thing a small, concrete step.", "Thank them when they act."],
                           avoid="The ambush confrontation about everything at once. They'll freeze and nothing will change.",
                           next="If avoidance is hurting people (bullying ignored, burnout), you're at Hell."),
            hell=dict(who="The Absentee. Avoidance that harms people.",
                      know=["Bullying or harassment is being ignored.", "People are burning out.", "Your manager won't act even when asked directly."],
                      do=["Raise it clearly with them once, in writing.", "Then take it to your skip-level or HR.", "Support colleagues who are affected.", "Don't wait for the kind manager to protect you; they can't."],
                      avoid="Going around them before trying with them. It reads as betrayal to a manager who thought you were friends.",
                      next="If nobody acts, use the formal channel. It exists for exactly this."),
        ),
        mirror=dict(
            title="Are you a Phantom?",
            intro="Kind people are often Phantoms. Tick honestly.",
            signs=["You've told someone “you're doing great” when you had concerns.", "You've put off a hard conversation for more than a month.", "You've let someone underperform because talking about it felt cruel.",
                   "Your team found out about a problem in their review, not from you.", "You change the subject when things get tense."],
            cure="This week, give one person one piece of clear, kind feedback: what you saw, why it matters, what you'd like instead. It's the kindest thing you'll do all month.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 2 October, Pip's 1:1 with Marcus, before calibration.",
            intro="The Specific Question and the Calibration Prep: easy to answer honestly.",
            lines=[
                ("Pip", "Marcus, what's one thing I'd need to do differently to be ready for level 4?"),
                ("Marcus", "Oh, honestly, you're doing great—"),
                ("Pip", "Thank you. Pretend you had to name one. What would it be?"),
                ("Marcus", "…You don't present your own work. People don't know what you do."),
                ("Pip", "That's really useful. And when my name comes up at calibration, what will the concerns be?"),
                ("Marcus", "That. And that you said yes to everything in the budget review."),
                ("Pip", "Thank you. Genuinely. Can we check in on both monthly?"),
                ("", "Marcus looks relieved. He's wanted to say this for months. He just needed someone to ask in a way that didn't feel like shouting."),
            ],
            note="Two specific questions got Pip more honest feedback than two years of “how am I doing?”",
        ),
    ),
    # ------------------------------------------------------------------ the Credit-Taking Crown
    "credit-taking-crown": dict(
        sighting=f"""{beat("Tuesday 7 January · the cold snap")}
<p>A cold snap hit the city. Pip's Q1 load model had predicted the peak to within 1.5%. Network Ops bought power at the
right time and saved an estimated €600,000.</p>
{beat("Thursday 16 January · the board")}
<p>Victor's update to the board said: <i>“My team delivered a step-change in forecast accuracy, using an approach I
introduced.”</i> The approach was Pip's. It was in a document with Pip's name on it, dated November, before Victor joined.</p>
{beat("Monday 27 January · LinkedIn")}
<p>Victor posted about “the power of data-driven leadership”, with a photo of the forecast chart. It had 412 likes. Pip's
mum liked it, not knowing.</p>
{beat("February · the review")}
<p>Pip's mid-year review, written by Victor, said: <i>“Solid contributor to team successes.”</i></p>
{note("Help your boss get credit for having you. It's the only credit war you can win.")}""",
        origin=dict(
            title="How a consultant learned to wear the crown",
            beats=[
                ("2014 · the partner presents", "At Victor's consultancy, analysts build, managers polish, and the partner presents. The client sees one face. That face gets the credit and the bonus."),
                ("2017 · the training", "Promoted to manager, Victor is trained to “own the narrative”: present the team's work as one coherent story, in his voice. Naming every analyst is considered “messy”."),
                ("2021 · the decimal", "After the decimal disaster (see the All-Seeing Eye), Victor also learns that whoever presents is whoever is blamed. If he's taking the risk, he reasons, he takes the credit."),
                ("2026 · MetroVolt", "Victor arrives needing quick wins to prove himself. Pip's model is the best thing in his new team. “My team delivered” feels, to Victor, like generosity. Pip's name never crosses his mind."),
            ],
            turning="A career in a world where the presenter owns the work, and naming the builders was called “messy”.",
            saved="A culture where leaders were praised for growing visible people. Victor would have named Pip in every slide if it had made him look good.",
            note="Many credit-taking bosses don't know they're doing it; they were trained in places where it's normal. That's why framing visibility as something that makes them look good works.",
        ),
        know=f"""<p>When the Credit Vampire is your <b>manager</b>, it's harder: they write your review, and some credit-taking is normal
(“my team delivered” is fair). It becomes a problem when your <b>name disappears</b> and your manager becomes the only route
to anyone senior. You win by making your name <b>known above and around them</b>, in ways that also make them look good.</p>
<h3 class="kh">What it wants</h3>
<p>To look good to its own boss, especially when it's new. Your work is the best material it has.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because at MetroVolt the manager writes the board paper and the review. If they don't mention you, nobody senior ever hears your name.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Your direct relationships with senior people.</li><li>Your name on artefacts that travel without them.</li><li>Being seen as a manager who doesn't develop people.</li><li>A calm, direct conversation about visibility.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Unaware</b><p>Says “my team” out of habit. Fixed by the Shared Spotlight.</p></div>
<div><b>The Insecure</b><p>Needs the wins. Fixed by helping them look good for developing you.</p></div>
<div><b>The Climber</b><p>Takes credit as strategy. Needs your Wider Web, and maybe your exit.</p></div>
</div>
{note("Your boss can take the credit. Make sure they can't take your name.")}""",
        difficulty=dict(
            normal=dict(who="The Unaware. “My team” out of habit.",
                        know=["They say “we” and “my team”, never “I did”.", "They're happy when you ask to present.", "Your name is in the detail, just not the headline."],
                        do=["Offer the Shared Spotlight: you present the method.", "Put your name on the artefacts.", "Thank them publicly for the chance."],
                        avoid="The LinkedIn correction. 412 people will remember you, none fondly.",
                        next="If your name never appears and you can't reach anyone senior, you're at Nightmare."),
            nightmare=dict(who="The Insecure. A pattern of erasure.",
                           know=["“An approach I introduced” about your approach.", "You're never invited upwards.", "Your review doesn't mention your biggest work."],
                           do=["Build the Wider Web: the people who use your work, your skip-level.", "Keep the Weekly Deeds Scroll (Act II).", "Have the Direct Word, framed as development.", "Make it easy for them to look good by naming you."],
                           avoid="The quiet strike: doing worse work so there's less to steal.",
                           next="If they actively block your visibility, you're at Hell."),
            hell=dict(who="The Climber. Actively blocking your visibility.",
                      know=["They stop you meeting senior people.", "They rewrite your documents without your name.", "Your review contradicts your results."],
                      do=["Document your work and its impact, with dates.", "Build your skip-level relationship openly.", "Ask for the review to include specific evidence.", "Plan an internal move or exit."],
                      avoid="The board ambush: telling the board it was your idea, in the meeting.",
                      next="If your review is unfair, challenge it formally with your record."),
        ),
        mirror=dict(
            title="Do you wear the crown?",
            intro="If you lead anyone, check your slides. Tick honestly.",
            signs=["Your board papers name no one in your team.", "You've said “an approach I introduced” about someone else's idea.", "Your team never presents to your boss.",
                   "You post about your team's wins without naming them.", "You'd struggle to say who built your last success."],
            cure="Name the builder on every slide. Bring them to present. Your boss will see a leader who grows people, which is exactly what gets leaders promoted.",
        ),
        rehearsal=dict(
            title="Scene: Monday 3 February, Pip's 1:1 with Victor.",
            intro="The Direct Word, framed as development, and as a way for Victor to look good.",
            lines=[
                ("Pip", "Victor, I'd like more visibility for my work this year. When the forecast's discussed at the board, could I present the method with you?"),
                ("Victor", "The board likes one voice."),
                ("Pip", "Understood. It might also show them you're building a strong team. Benedict mentioned wanting to see more of the analysts."),
                ("Victor", "…He did say that."),
                ("Pip", "And I'd love to meet the Ops planning leads monthly. They use the model most. It'd keep the team's work in front of them."),
                ("Victor", "Fine. Five minutes at the March board. Make it sharp."),
                ("", "March board: Pip presents for five minutes. Benedict asks him two questions. Victor says “Pip leads our forecasting”. It's the first time anyone has said so."),
            ],
            note="Pip never accused Victor of anything. He made naming Pip the thing that would make Victor look good.",
        ),
    ),
    # ------------------------------------------------------------------ the New Lord Arrives
    "new-lord-arrives": dict(
        sighting=f"""{beat("Monday 2 December · 09:00 · day one")}
<p>Victor arrived with a 47-slide operating model, three new acronyms (GAOM, DART, and something called “the Spine”)
and a plan to “reset ways of working”.</p>
{beat("Day two · three camps")}
<p>The team split into three camps: the eager (volunteering for everything, nodding at every acronym), the sceptical
(folded arms, eyebrows, “we tried that”) and the invisible (camera off, hoping to be forgotten).</p>
{beat("Day three · Pip")}
<p>Pip, unusually, did something sensible. He booked 30 minutes, brought a one-page “what you should know” about the
team's work, and asked Victor what he was being measured on.</p>
{beat("Day three · 30 minutes later")}
<p>Victor, who was terrified, nearly hugged him. He'd been at MetroVolt for three days, knew nobody, and had a director
who'd told him the team was “too comfortable” and then left for a conference in Lisbon.</p>
{note("New managers are more scared than you are. They've just bet their reputation on a team they don't know. Be the person who makes that bet look smart.")}""",
        origin=dict(
            title="How Victor came to arrive with 47 slides",
            beats=[
                ("October 2026 · the hiring", "Benedict hires Victor to “shake things up” in Grid Analytics, which he calls “too comfortable”. He's never actually watched the team work."),
                ("November 2026 · the brief", "Victor is given a target (faster, more strategic analytics), no history and a 90-day deadline to show change."),
                ("November · the slides", "With no knowledge of the team, Victor builds what consultants build: an operating model. 47 slides. Three acronyms. It's how he proves he has a plan."),
                ("2 December · arrival", "Victor walks in convinced the team needs fixing, because that's what he was told, and terrified it won't work, because he doesn't know them."),
            ],
            turning="Being told a team needed fixing by someone who'd never watched it work.",
            saved="A director who introduced him properly, explained the history and said “understand before you change”.",
            note="Most new managers arrive with a brief written by someone else. Help them see the real team, and they'll often rewrite the brief themselves.",
        ),
        know=f"""<p>A new manager is under pressure to <b>prove themselves fast</b>. They don't know who's good, what's broken, or
where the bodies are buried. They form impressions quickly, and those impressions stick for a year. Your best move: be
<b>early, honest and useful</b>.</p>
<h3 class="kh">What it wants</h3>
<p>Early wins, a reliable picture of the team, and allies who'll make its first 90 days work.</p>
<h3 class="kh">Why the first weeks matter</h3>
<p>Because impressions formed in the first month shape who gets the good work, who gets trusted and who gets “managed”, often for years.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Failing publicly in its first 90 days.</li><li>A team that resists everything.</li><li>Not knowing what it doesn't know.</li><li>Its own boss's verdict.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Listener</b><p>Learns first, changes later. Give it the landscape.</p></div>
<div><b>The New Broom</b><p>Mandated to change things. Help it pick the right changes.</p></div>
<div><b>The Clearer</b><p>Brings its own people. Be useful fast; keep your options warm.</p></div>
</div>
{note("A new lord remembers who helped them find the map. Be on the map.")}""",
        difficulty=dict(
            normal=dict(who="The Listener. A thoughtful new manager.",
                        know=["They ask questions before changing things.", "They meet everyone 1:1.", "They admit what they don't know."],
                        do=["Give them the Landscape Gift in week one.", "Ask the Measure Question.", "Explain history honestly when they propose something old."],
                        avoid="The invisible: keeping your head down until they settle.",
                        next="If they're mandated to change everything, you're at Nightmare."),
            nightmare=dict(who="The New Broom. A mandate to change everything.",
                           know=["An operating model appears in week one.", "Old decisions are reopened.", "The team splits into camps."],
                           do=["Help them choose which changes matter most.", "Argue only about changes that will really hurt.", "Volunteer for the first change that's actually good.", "Stay out of the camps."],
                           avoid="The old guard: “that's not how we do things here.”",
                           next="If they're bringing in their own people and clearing out the team, you're at Hell."),
            hell=dict(who="The Clearer. Bringing their own people.",
                      know=["Former colleagues of theirs arrive.", "Long-serving people are sidelined.", "Reorg rumours start."],
                      do=["Be useful fast and visibly.", "Keep your network warm (Act I, Blood Pacts).", "Know your options inside and outside.", "Don't take it personally; it rarely is."],
                      avoid="The courtier's rush: agreeing with everything to survive. They'll notice, eventually.",
                      next="If you're on the list anyway, negotiate well (and read Act V, The Famine)."),
        ),
        mirror=dict(
            title="When you're the new lord",
            intro="One day you'll arrive somewhere new. Check your first-week instincts. Tick honestly.",
            signs=["You'd present a plan before meeting the team.", "You'd assume the team is the problem because you were told so.", "You'd change things in your first month to show impact.",
                   "You'd judge people on your first impression.", "You'd skip the history because it slows you down."],
            cure="In your first 30 days, ask everyone the same three questions: what's working, what's broken, what would you change? Then decide. Your plan will be better, and so will your welcome.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 4 December, 11:00. Pip's first 1:1 with Victor.",
            intro="The Landscape Gift and the Measure Question.",
            lines=[
                ("Pip", "Welcome! I've written one page on what Grid Analytics does: what works, what's broken, and history you'd never guess. Want me to walk you through it?"),
                ("Victor", "…Yes. Please. Nobody's given me anything like this."),
                ("Pip", "And what does a great first six months look like for you? I'd like my work to help with it."),
                ("Victor", "Faster answers for the board. Benedict says we're slow."),
                ("Pip", "That's fair. The main reason is the board asks reach us the night before. Could we get them a week earlier? That would fix half of it."),
                ("Victor", "…That's not in my operating model."),
                ("Pip", "It could be slide 48."),
            ],
            note="Victor's first useful change came from Pip's one page, not his 47 slides. He remembered that for a long time.",
        ),
    ),
    # ------------------------------------------------------------------ the Ritual Circle of the 1:1
    "ritual-circle-one-to-one": dict(
        sighting=f"""{beat("Every Thursday · 15:00")}
<p>Pip's 1:1s with Victor went like this. Victor asked for status. Pip gave status. Victor gave four new tasks. The meeting
ended at 22 minutes.</p>
{beat("Twice a month")}
<p>It was cancelled for “something urgent”. The cancellation arrived at 14:58.</p>
{beat("Three months")}
<p>In thirteen weeks, Pip had used the 1:1 for exactly zero things he wanted. He had never mentioned level 5, his workload
or the fact that he hated the Spine.</p>
{beat("Friday · the pub")}
<p>The Annotator, over a drink, was appalled. “It's your meeting,” she said. “Not his. Write the agenda. Put the status in an
email. Use the time for things only he can do: decisions, blockers, your career. And never, ever let it be cancelled without
asking for another slot.”</p>
{note("If your 1:1 is all status, send the status the day before and walk in with a different list. Watch your manager relax.")}""",
        origin=dict(
            title="How MetroVolt's 1:1s died",
            beats=[
                ("2022 · the policy", "An engagement survey shows that staff feel unsupported. HR introduces mandatory weekly 1:1s for every manager. There's a policy, a calendar template and no training."),
                ("2022 · the default", "Nobody tells managers what a 1:1 is for. Most fill it with the only thing they know: status. “Where are we on X?”"),
                ("2023 to 2025 · the decline", "Status 1:1s feel pointless, so they're cancelled whenever anything comes up. Staff learn to expect nothing from them. Managers learn they're a box to tick."),
                ("2026 · the ritual", "The 1:1 survives as a ritual with no magic left in it: a weekly calendar entry, mostly cancelled, mostly status, almost never about the person in it."),
            ],
            turning="A good idea introduced as a policy, without anyone explaining what it was for.",
            saved="One page from HR in 2022: “The 1:1 is for the employee's agenda: decisions, blockers, feedback and growth. Status goes in writing.”",
            note="Most dead 1:1s were never alive. Nobody explained the ritual. You can explain it to your manager by running it well.",
        ),
        know=f"""<p>The 1:1 is the <b>only regular meeting where you set the agenda</b>, or could. Most people let it become a status
report, which wastes it: status belongs in writing. The 1:1 is for things that need a conversation: decisions, problems,
feedback, and your growth. Many of this Act's creatures are tamed here.</p>
<h3 class="kh">What your manager wants from it</h3>
<p>To know what's going on without effort, and to spot problems early. A good 1:1 does both in half the time.</p>
<h3 class="kh">Why it dies here</h3>
<p>Because it was introduced as a policy, not a practice. Nobody knows what it's for, so it becomes status, then a
cancellation, then nothing.</p>
<h3 class="kh">What brings it to life</h3>
<ul class="fears"><li>A shared agenda you fill in beforehand.</li><li>Status in writing, not in the meeting.</li><li>A monthly slot for your career.</li><li>Rescheduling, never cancelling.</li></ul>
<h3 class="kh">Three kinds of 1:1</h3>
<div class="breeds">
<div><b>The Status Report</b><p>The default. Send the status; repurpose the time.</p></div>
<div><b>The Cancelled</b><p>Always “something urgent”. Ask for shorter, fixed slots.</p></div>
<div><b>The Real 1:1</b><p>Decisions, blockers, feedback, growth. Rare, and powerful.</p></div>
</div>
{note("The 1:1 is the only throne room where you set the agenda. Sit in the chair.")}""",
        difficulty=dict(
            normal=dict(who="A busy manager who's never thought about 1:1s.",
                        know=["The 1:1 happens but it's all status.", "Your manager is open to suggestions.", "Nobody's against it; nobody's tried."],
                        do=["Start a Shared Agenda doc.", "Put status at the top, in writing.", "Bring decisions and questions to the meeting."],
                        avoid="The status monologue: reading out your task list.",
                        next="If it's cancelled more often than held, you're at Nightmare."),
            nightmare=dict(who="The Cancelled. Constant cancellations.",
                           know=["Half your 1:1s are cancelled.", "Cancellations come at the last minute.", "You haven't discussed your career in months."],
                           do=["Ask for a shorter, fixed slot that's easier to keep.", "When cancelled, ask for 10 minutes later that week.", "Send the agenda anyway, so decisions can happen by email.", "Book a monthly career slot separately."],
                           avoid="The quiet acceptance: letting it die. No 1:1s means a surprise review.",
                           next="If your manager refuses 1:1s altogether, you're at Hell."),
            hell=dict(who="No 1:1s at all.",
                      know=["Your manager says they're a waste of time.", "You only see them in group meetings.", "Your review is written without a conversation."],
                      do=["Ask for at least a monthly one.", "Find a mentor and a skip-level relationship to fill the gap.", "Keep your own written record of your work.", "Raise it with HR if reviews happen without conversations."],
                      avoid="The grievance hour: if you do get one, don't spend it all complaining.",
                      next="A manager who won't talk to you is a reason to look at the Escape Portal."),
        ),
        mirror=dict(
            title="Are your 1:1s alive?",
            intro="If you run 1:1s for others, check them. Tick honestly.",
            signs=["Your 1:1s are mostly status.", "You've cancelled more than you've held this quarter.", "You set the agenda, not them.",
                   "You haven't talked about anyone's career this month.", "Your 1:1s end with more tasks for them, not decisions from you."],
            cure="Ask each person to bring the agenda next time, and make status written. Then ask one question, every time: what's getting in your way?",
        ),
        rehearsal=dict(
            title="Scene: Thursday 23 January, 15:00. The first 1:1 with a shared agenda.",
            intro="The Shared Agenda: status in writing, the meeting for the rest.",
            lines=[
                ("Pip", "I've started a shared 1:1 doc. Status is at the top so we don't need to talk through it. The rest is two decisions and one question."),
                ("Victor", "…OK. Decisions?"),
                ("Pip", "Heatwave scenario A or B. I recommend A. And can you nudge IT on the substation data? It's my only blocker."),
                ("Victor", "A. And yes, I'll email the IT director today. The question?"),
                ("Pip", "From next month, could we use the last 1:1 of each month for my development? I'd like to talk about level 5."),
                ("Victor", "…Nobody's asked me that before. Yes."),
                ("", "The meeting ends at 14 minutes. Victor says it's the most useful 1:1 he's had at MetroVolt. It's also the shortest."),
            ],
            note="Same 30 minutes. Status moved to writing, and the time went to decisions, a blocker and Pip's career.",
        ),
    ),
    # ------------------------------------------------------------------ the Skip-Level Séance
    "skip-level-seance": dict(
        sighting=f"""{beat("Tuesday 11 February · the preparation")}
<p>After ten weeks of Victor, Pip booked a meeting with Benedict Crane, who, miraculously, was in the building. He prepared
a list of eleven problems with Victor. He rehearsed it in the bathroom mirror.</p>
{beat("Wednesday 12 February · 11:00 · problem six")}
<p>Halfway through the list, Benedict held up a hand. “Have you raised these with Victor?” Pip had not. “Then do that first,”
said Benedict, not unkindly, “and come back if it doesn't work.” The meeting ended at 11:14.</p>
{beat("Wednesday · 17:30")}
<p>Victor knew. He didn't say how. He didn't need to.</p>
{beat("Thursday 13 February · the 1:1")}
<p>The 1:1 the next day lasted four minutes. It was very polite. It was the coldest four minutes of Pip's year.</p>
{note("A skip-level is a relationship, not an emergency exit. Visit when nothing's on fire, and they'll listen when something is.")}""",
        origin=dict(
            title="How Benedict's open door closed",
            beats=[
                ("January 2024 · the policy", "Benedict announces an “open door policy”: anyone in Strategy can book time with him, about anything."),
                ("February 2024 · the first visitor", "The first person who walks through the door brings a complaint about their manager. Benedict, unsure what to do, mentions it to the manager to “sort it out”."),
                ("February 2024 · the lesson", "The manager confronts the complainer. The story spreads. Everyone in Strategy learns that the open door leads straight back to your boss."),
                ("2024 to 2026 · the empty doorway", "Nobody walks through again. The door stays open. Benedict wonders why nobody uses it. And newcomers, like Pip, walk through with eleven grievances, not knowing the history."),
            ],
            turning="One complaint, handled clumsily, that taught a whole department the door was a trap.",
            saved="Benedict saying, in 2024: “I'll keep this confidential unless someone's at risk. Have you raised it with your manager? Would you like help doing that?”",
            note="Skip-levels work best as a relationship built in calm weather. Most open doors were closed by the first storm that came through them.",
        ),
        know=f"""<p>Your boss's boss has <b>power over your manager</b> and over your career: they're in calibration and promotion
discussions. A good relationship with them is valuable. A complaint about your manager delivered to them is
<b>radioactive</b>: they must back their manager first, and the manager will almost always find out.</p>
<h3 class="kh">What the skip-level wants</h3>
<p>Insight into the business, early warning of real problems, and not to be dragged into every disagreement between a manager and their team.</p>
<h3 class="kh">Why it's dangerous here</h3>
<p>Because MetroVolt's skip-levels pass complaints back down, and managers find out. A relationship built on ideas is
safe. One built on grievances isn't.</p>
<h3 class="kh">What makes it work</h3>
<ul class="fears"><li>Your manager knowing about it.</li><li>Ideas and questions, not complaints.</li><li>Regular, light contact.</li><li>Escalating only after trying with your manager.</li></ul>
<h3 class="kh">Three kinds of séance</h3>
<div class="breeds">
<div><b>The Coffee</b><p>Regular, open, about the business. Safe and valuable.</p></div>
<div><b>The Escalation</b><p>A problem raised after trying with your manager, with them told. Legitimate.</p></div>
<div><b>The Secret Complaint</b><p>Behind your manager's back. Radioactive.</p></div>
</div>
{note("Summon the higher power often, openly and for good reasons. Never in secret to curse your lord.")}""",
        difficulty=dict(
            normal=dict(who="A healthy skip-level culture.",
                        know=["Skip-level coffees are normal.", "Your manager encourages them.", "Conversations are about the business."],
                        do=["Ask your manager for a quarterly skip-level coffee.", "Bring ideas and questions.", "Share a short summary with your manager afterwards."],
                        avoid="The name-drop: “as I was saying to Benedict” to your manager.",
                        next="If your manager is defensive about skip-levels, you're at Nightmare."),
            nightmare=dict(who="A defensive manager and a closed door.",
                           know=["Your manager discourages direct contact upwards.", "Past complaints were passed back down.", "Nobody uses the open door."],
                           do=["Keep skip-level contact about the business only.", "Share notes with your manager every time.", "Build it slowly, over quarters.", "If you must escalate, raise it with your manager first and tell them you're going further."],
                           avoid="The eleven grievances: one problem with facts is heard; eleven is a rant.",
                           next="If your manager is part of something serious, you're at Hell."),
            hell=dict(who="Serious issues, and your manager is part of them.",
                      know=["Harassment, safety or fraud is involved.", "Your manager is involved or protecting it.", "Raising it with them could put you at risk."],
                      do=["Go to the skip-level, HR or the formal channel directly.", "Bring facts and dates.", "Ask how confidentiality will be handled.", "Keep your own record."],
                      avoid="The secret séance for ordinary problems. Save direct escalation for when it's truly needed.",
                      next="If the formal channel fails, there are external ones (Act VIII, the Whistle of Last Resort)."),
        ),
        mirror=dict(
            title="How do you summon?",
            intro="Check how you use the people above your manager. Tick honestly.",
            signs=["You've complained about your manager to their boss before raising it with them.", "You've never met your skip-level outside a big meeting.", "You've used your skip-level relationship as a threat.",
                   "You've brought a list of grievances to a senior person.", "You'd be uncomfortable if your manager saw your skip-level notes."],
            cure="Book one skip-level coffee this quarter about the business, with your manager's blessing. Share what you learn. Build the relationship before you ever need it.",
        ),
        rehearsal=dict(
            title="Scene: Monday 17 February. Pip tries again, the right way.",
            intro="The Proper Escalation: with your manager first, then openly.",
            lines=[
                ("Pip", "Victor, I want to raise something properly. The late-night emails and weekend requests are wearing me down. I've mentioned it twice. Can we agree core hours?"),
                ("Victor", "…I didn't realise it was that bad."),
                ("Pip", "And separately, would you mind if I had a quarterly coffee with Benedict about Strategy's priorities? I'll share what I learn with you."),
                ("Victor", "After last week?"),
                ("Pip", "Last week I went about it wrong, and I'm sorry. This would be about the business, and open."),
                ("Victor", "…Fine. Quarterly."),
                ("", "Core hours are agreed that week. In April, Pip has coffee with Benedict and asks what he looks for in people he promotes. He sends Victor a three-line summary. Victor replies: “Useful. Thanks.”"),
            ],
            note="An apology, a direct conversation and an open request repaired what one secret meeting had broken.",
        ),
    ),
    # ------------------------------------------------------------------ the Puppet King
    "puppet-king": dict(
        sighting=f"""{beat("Monday 13 January · approved")}
<p>Victor approved Pip's plan for a second heatwave model: £18,000, six weeks. “Great,” he said. “I'll take it upstairs.”</p>
{beat("January and most of February · upstairs")}
<p>It went upstairs. It stayed there. Victor said “leave it with me” on four occasions.</p>
{beat("Tuesday 4 February · down again")}
<p>The plan came back down three weeks later, changed beyond recognition: £9,000, four weeks, no new data. It had been
approved by Ottoline. Victor had approved nothing; he had carried it.</p>
{beat("That evening · the discovery")}
<p>Pip looked up the delegation rules. Victor couldn't hire, couldn't spend more than £5,000 and couldn't move a deadline
without asking Benedict, who asked Ottoline. Pip realised he had spent three months trying to persuade someone who could
not say yes.</p>
{note("Every puppet king knows exactly who holds the strings. Ask them gently and they'll usually tell you. They're relieved someone noticed.")}""",
        origin=dict(
            title="How the crown came off its strings",
            beats=[
                ("2023 · the scandal", "A manager in Strategy signs a £400,000 consultancy contract without proper approval. The work is useless. The story reaches the parent group."),
                ("2023 · the clampdown", "Ottoline centralises approvals. Managers in Strategy keep their titles and lose their spending power. Anything over £5,000 goes through Benedict, then through her."),
                ("2024 to 2025 · the hollow crowns", "Strategy managers learn to “take things upstairs” and wait. They can't say yes, and they're embarrassed to admit it."),
                ("December 2026 · Victor", "Victor arrives expecting a manager's authority. He discovers, quietly, that he has a manager's title and an analyst's budget. He hides it, and says “leave it with me”."),
            ],
            turning="One bad contract in 2023 that turned every manager in Strategy into a messenger.",
            saved="Proportionate controls: tighter limits for contracts, not for £18,000 of analysis. And honesty with new managers about what they can approve.",
            note="Most puppet kings are embarrassed, not malicious. Make the strings visible, kindly, and help them pull together.",
        ),
        know=f"""<p>Some managers have <b>titles without authority</b>: new, constrained by a central team, or simply not trusted by
their own boss. They can't decide, so they postpone, carry decisions upward or quietly change them to please the real
decider. Don't humiliate them by going around them. Work <b>with</b> them to reach the real decider.</p>
<h3 class="kh">What it wants</h3>
<p>To look like a real manager, and not to have its lack of power exposed.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because after 2023, MetroVolt centralised power without changing titles. Managers have the crown and none of the strings.</p>
<h3 class="kh">What helps it</h3>
<ul class="fears"><li>A one-page case written in the real decider's language.</li><li>Someone to go upstairs with.</li><li>Small wins that build its authority.</li><li>Gentle questions about who decides.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The New King</b><p>Still earning authority. Help them build cases and it grows.</p></div>
<div><b>The Leashed</b><p>Kept on a short leash from above. Use the Joint Ascent.</p></div>
<div><b>The Hollow Crown</b><p>No authority and blocks you to feel important. Build your own routes, openly.</p></div>
</div>
{note("Don't cut the strings. Learn where they go, and help the king walk.")}""",
        difficulty=dict(
            normal=dict(who="The New King. Still earning authority.",
                        know=["Decisions are slow but they come.", "Your manager is open about the limits.", "Strong cases get approved."],
                        do=["Ask gently who makes the final call.", "Prepare cases in the decider's language.", "Credit your manager when it works."],
                        avoid="The eternal wait: waiting for decisions they can't make.",
                        next="If they're kept on a short leash and decisions come back changed, you're at Nightmare."),
            nightmare=dict(who="The Leashed. On a short leash from above.",
                           know=["“Leave it with me”, and it disappears.", "Approvals come back changed, from someone else.", "They're nervous before meetings with their boss."],
                           do=["Write the Case in Their Language for the real decider.", "Offer the Joint Ascent: go upstairs together, them leading.", "Help them win small decisions to build authority.", "Keep it all visible to them."],
                           avoid="The puppeteer's bypass: going straight to the real decider and cutting them out.",
                           next="If they have no authority and block you to look important, you're at Hell."),
            hell=dict(who="The Hollow Crown. Powerless, and blocking.",
                      know=["They block your access upwards.", "They take credit for carrying decisions.", "Nothing you need ever gets decided."],
                      do=["Build your skip-level relationship openly.", "Document what's stalled and its cost.", "Ask your manager directly how decisions can move faster.", "Consider moving to where decisions happen."],
                      avoid="The pity glance: treating them as powerless in front of the team.",
                      next="If nothing moves, take your work where it can."),
        ),
        mirror=dict(
            title="Is your crown hollow?",
            intro="If you manage anyone, check your strings. Tick honestly.",
            signs=["You've said “leave it with me” about something you can't approve.", "Your team doesn't know what you can and can't decide.", "You've changed a team decision to please your boss without telling them why.",
                   "You hide your lack of authority from your team.", "You've blocked someone's direct contact upwards."],
            cure="Tell your team plainly what you can approve and what needs your boss. Then help them build cases that go upstairs well. Honesty about limits earns more respect than pretending.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 5 February. Pip's 1:1 with Victor.",
            intro="The Gentle Question, the Ammunition and the Joint Ascent.",
            lines=[
                ("Pip", "Victor, who'll make the final decision on the heatwave model? What do they need to see to say yes? I'd like to make it easy for you."),
                ("Victor", "…Ottoline. Honestly, I can't approve anything over five thousand."),
                ("Pip", "That's useful to know, thank you. What does Ottoline care about most?"),
                ("Victor", "Complaints reaching the CEO."),
                ("Pip", "Then let me write a one-page case for her about billing complaints. 2,400 in the last heatwave. Would it help if I came with you when you take it up? You lead, I'll answer the data questions."),
                ("Victor", "…Yes. Thursday."),
                ("", "Thursday: Victor presents, Pip answers two questions, Ottoline approves £18,000 in six minutes. Victor tells the team he “got it through”. Pip lets him."),
            ],
            note="Pip let Victor have the win. That's the point: a puppet king who wins with you becomes a king who fights for you.",
        ),
    ),
    # ------------------------------------------------------------------ the Friend Who Became Your Boss
    "friend-became-boss": dict(
        sighting=f"""{beat("Friday 10 January · 08:02")}
<p>An email: Jules had been made team lead of Grid Analytics. Pip found out from the email, like everyone else.</p>
{beat("08:05")}
<p>Jules messaged: <i>“Coffee? I want to talk before it gets weird.”</i> It was already a bit weird.</p>
{beat("January and February · small things")}
<p>Jules stopped joining the Friday moan about Victor. Jules asked about deadlines in a new tone. Jules was, quite rightly,
now in meetings about Pip. One Friday, Pip told a joke about a decision Jules had made, at the pub, and Jules laughed a
fraction too late.</p>
{beat("The unspoken thing")}
<p>Pip had applied for the same role. Both of them knew. Neither mentioned it. It sat at every coffee like a third person.</p>
{note("If you also wanted the job, say so, once, kindly. “I wanted it, I'm a bit gutted, and I'm glad it's you.” Then it's said, and you can both move on.")}""",
        origin=dict(
            title="How two friends became a boss and a report",
            beats=[
                ("September 2022 · the graduate intake", "Pip and Jules join MetroVolt on the same day. At the induction drinks they discover a shared hatred of pie charts. Friends by midnight."),
                ("2023 to 2025 · two paths", "Pip builds brilliant models in silence. Jules builds good models and helps everyone (Act I, Blood Pacts). By 2025, three directors know Jules's name."),
                ("December 2026 · the opening", "Victor needs a team lead. Both apply. Jules gets it, mostly because more people know what Jules does. Pip's work is as good; it's just less visible."),
                ("January 2027 · the new rules", "Nobody gives either of them guidance on what happens to a friendship when one becomes the other's boss. They work it out alone, awkwardly, over coffee."),
            ],
            turning="One promotion between two equals, decided by visibility, with no guidance on what came after.",
            saved="Nothing broken, yet. What helps is an honest conversation early, before the unspoken thing grows.",
            note="Friendships survive this when they're named and given new rules. Unspoken, they rot. Both of you lose something; say so.",
        ),
        know=f"""<p>When a friend becomes your boss, <b>both of you lose something</b>: you lose an equal; they lose a confidant. They
now have duties that may conflict with the friendship: reviewing you, deciding your workload, keeping secrets about reorgs.
It's often more awkward for them than for you. Friendships survive when both sides <b>name it early</b> and agree new rules.</p>
<h3 class="kh">What the new boss wants</h3>
<p>To be fair, to be taken seriously by the team, and to keep the friend. All three at once is hard.</p>
<h3 class="kh">Why it's hard here</h3>
<p>Because MetroVolt promotes from within teams and offers no guidance on this. New leads are expected to switch from peer
to boss overnight.</p>
<h3 class="kh">What protects the friendship</h3>
<ul class="fears"><li>An early, honest conversation.</li><li>New rules, agreed together.</li><li>Visible support in their first months.</li><li>Saying the unspoken thing once.</li></ul>
<h3 class="kh">Three kinds of new boss</h3>
<div class="breeds">
<div><b>The Graceful</b><p>Names it, sets rules, stays a friend. Support them.</p></div>
<div><b>The Overcorrector</b><p>Becomes strict to prove fairness. Give them time; tell them kindly.</p></div>
<div><b>The Pal</b><p>Avoids being the boss. Help them lead; don't take advantage.</p></div>
</div>
{note("Say the awkward thing once, out loud, early. Then you get to keep the friend.")}""",
        difficulty=dict(
            normal=dict(who="The Graceful. A good friend, promoted fairly.",
                        know=["They raised the awkwardness first.", "They're fair to everyone.", "Nothing's been said that can't be fixed."],
                        do=["Have the Naming Rite: congratulate, acknowledge, agree how to work.", "Write the new rules together.", "Back them visibly."],
                        avoid="The insider favour: expecting easier treatment.",
                        next="If you both wanted the job and it's sitting between you, you're at Nightmare."),
            nightmare=dict(who="You both wanted it, and it's unspoken.",
                           know=["The job sits at every coffee like a third person.", "Conversations stop when they arrive.", "You're tempted to test them."],
                           do=["Acknowledge it once: “I wanted it, I'm gutted, I'm glad it's you.”", "Ask them to help you towards the next opportunity.", "Support them visibly in their first months.", "Keep work moans away from them."],
                           avoid="The resentful ally: joining people who resent the promotion.",
                           next="If they've changed for the worse, or use the friendship to pressure you, you're at Hell."),
            hell=dict(who="Power has changed them, or they use the friendship against you.",
                      know=["They expect favours because you're friends.", "They share your confidences with others.", "They're harder on you than on others."],
                      do=["Treat them as a manager first.", "Keep important things in writing.", "Use normal channels for problems.", "Grieve the friendship if you must, and protect your career."],
                      avoid="The old moan: still complaining to them as if they were a peer.",
                      next="If it's unworkable, an internal move protects both the career and what's left of the friendship."),
        ),
        mirror=dict(
            title="When you're the friend who got promoted",
            intro="One day it might be you. Check your instincts. Tick honestly.",
            signs=["You'd avoid the awkward conversation and hope it fades.", "You'd be extra strict with your friend to prove you're fair.", "You'd share team secrets with them “because they're a friend”.",
                   "You'd keep moaning about leadership with them, now that you're leadership.", "You'd let them get away with things you wouldn't let others."],
            cure="In the first week, have the conversation: name it, agree rules, and promise to tell them hard things straight. Friends can take honesty. They can't take silence.",
        ),
        rehearsal=dict(
            title="Scene: Friday 10 January, 08:30. Coffee, as Jules asked.",
            intro="The Naming Rite and the New Boundaries.",
            lines=[
                ("Pip", "Congratulations. Really. I'll be honest: I wanted it, I'm a bit gutted, and I'm glad it's you."),
                ("Jules", "Thank you for saying that. I was dreading this coffee."),
                ("Pip", "How do you want to handle the friend-and-boss thing?"),
                ("Jules", "Work at work. If you disagree with something, tell me in a 1:1, not at the pub. And no work moaning at the pub, in either direction."),
                ("Pip", "Deal. And will you help me towards the next lead role?"),
                ("Jules", "That's the first thing I want to do as a lead."),
                ("", "They write the rules on a napkin. Jules keeps it. In March, at their three-month check-in, it's still in Jules's wallet."),
            ],
            note="One honest sentence (“I wanted it”) took the third person out of the room.",
        ),
    ),
    # ------------------------------------------------------------------ the Escape Portal
    "escape-portal": dict(
        sighting=f"""{beat("December to February · the counter-spells")}
<p>Pip tried most of this Act. The Rhythm Ward calmed Victor's eye a little. The 1:1 doc helped. Core hours were agreed.
But Victor still took the credit, still changed his mind every Tuesday, and still sent messages at 23:00 that started
with “sorry, one more thing”.</p>
{beat("Sunday evenings")}
<p>Pip's Sunday evenings had developed a particular taste. He'd start feeling it around four. By nine, he'd be checking
email “just to see”.</p>
{beat("Thursday 20 February · the lift")}
<p>Priya Nair stopped him in the lift. “I've got an analytics lead role in Customer Ops,” she said. “You'd be good at it.
No pressure.” That evening, a recruiter also messaged him on LinkedIn about a role at a rival utility, “with a very
competitive package”.</p>
{beat("19:40 · floor 9")}
<p>Pip sat on floor 9 after everyone had gone and stared at the exit sign for a long time. It was, he thought, the only light
in the building that told the truth.</p>
{note("Never resign on a bad day. Decide on a good day. If you still want to go on a good day, go.")}""",
        origin=dict(
            title="How the Annotator found the portal",
            beats=[
                ("2020 · the Annotator joins MetroVolt", "Before she was the Annotator, she was a data lead in Network Assets: talented, loud, happy."),
                ("2021 to 2023 · the storm years", "She works for a Weather Tyrant (not Gareth; another one, long gone). Three years of ⛈️ days. She tries every counter-spell in this book, some of which she invented."),
                ("March 2023 · a bad Tuesday", "After a storm in a meeting, she resigns on the spot. No plan, no savings, no job. She's right to leave. She leaves the wrong way."),
                ("2023 to now · the margins", "It takes six months to find work. She builds a freelance career, and writes in the margins of this book so others can find the portal on a good day, with a plan."),
            ],
            turning="Leaving was right. Leaving on a bad Tuesday, with no plan, was the mistake she's spent three years warning people about.",
            saved="A Stay-or-Go Ledger, written on a calm Sunday. And six months of savings. She'd still have left; she'd just have landed softer.",
            note="I'd leave again. I'd just do it on a Thursday, with a plan, a reference and a pension transfer form. Learn from my Tuesday.",
        ),
        know=f"""<p>Not every bad manager can be managed. Sometimes the job is <b>costing more than it gives</b>: your health, your growth,
your evenings. The portal has <b>several doors</b>: an internal move keeps your network and history; an external move resets
more; staying with an end date is also a choice. What matters is that you choose <b>calmly, with a plan</b>.</p>
<h3 class="kh">What keeps people in the throne room</h3>
<p>Fear of the unknown, loyalty, sunk cost (“I've put so much in”), and the hope that next quarter will be different.</p>
<h3 class="kh">Why the portal matters here</h3>
<p>Because some managers won't change, and MetroVolt doesn't always move them. Your career can't wait for the organisation to notice.</p>
<h3 class="kh">What makes leaving go well</h3>
<ul class="fears"><li>Deciding on a good day.</li><li>Options prepared before you need them.</li><li>Talking to the new team before deciding.</li><li>A proper handover and no burnt bridges.</li></ul>
<h3 class="kh">Three kinds of door</h3>
<div class="breeds">
<div><b>The Internal Move</b><p>New manager, same company, same pension. Often the best first door.</p></div>
<div><b>The Leap</b><p>A new company. More reset, more risk, sometimes more reward.</p></div>
<div><b>The Stay With an End Date</b><p>Stay, deliberately, until a set date or goal. A choice, not a trap.</p></div>
</div>
{note("Every throne room has a door. The trick is walking through it on a good day, with a plan.")}""",
        difficulty=dict(
            normal=dict(who="A bad patch with a decent manager.",
                        know=["It's been weeks, not months.", "Counter-spells are working a bit.", "You still learn things."],
                        do=["Try the counter-spells for three months.", "Write the Honest Ledger on a good day.", "Keep your network warm anyway."],
                        avoid="The rage quit: resigning in the middle of a bad meeting.",
                        next="If months of trying have changed nothing, you're at Nightmare."),
            nightmare=dict(who="A manager who won't change, and growth that's stalled.",
                           know=["You've tried for months.", "You're coping, not learning.", "Sunday evenings feel like dread."],
                           do=["Explore an internal move seriously.", "Talk to the hiring manager before telling yours.", "Talk to people in the new team.", "Update your CV and save some money."],
                           avoid="The haunting: staying miserable and telling everyone, for years. You'll become the Doom Prophet.",
                           next="If your health is suffering or you're being harassed, you're at Hell."),
            hell=dict(who="Your health is suffering, or you're being harassed or bullied.",
                      know=["You're not sleeping.", "You're anxious or ill.", "You're scared of your manager."],
                      do=["Protect yourself first: talk to a doctor.", "Talk to HR or get legal advice if there's harassment.", "Leave as soon as you safely can.", "Lean on people outside work."],
                      avoid="The scorched exit: a farewell email listing everyone's failings. It will follow you.",
                      next="Your health comes first. No job is worth more than that."),
        ),
        mirror=dict(
            title="Are you stuck in the throne room?",
            intro="Check honestly how you're doing. Tick what's true.",
            signs=["Sunday evenings feel like dread.", "You've tried for months and nothing has changed.", "You're no longer learning, only coping.",
                   "Your health, sleep or relationships are suffering.", "Someone has offered you a door, and you felt relief."],
            cure="If you ticked three or more, write the Stay-or-Go Ledger this weekend, on a calm day. Then talk to one person about one door. You don't have to walk through it. You just have to know it's there.",
        ),
        rehearsal=dict(
            title="Scene: Monday 24 February, 12:30. Coffee with Priya, before telling anyone.",
            intro="The Inside Door: explore first, decide later, and tell your manager before it's public.",
            lines=[
                ("Pip", "Priya, I'm interested. Could we talk about what the role really involves before I mention it to Victor?"),
                ("Priya", "Of course. Honestly? Messy data, angry customers, a great team, and a manager who goes home at six. That's me."),
                ("Pip", "Could I talk to someone on the team?"),
                ("Priya", "Talk to Sam. Tell him I said to be brutally honest."),
                ("Pip", "Thank you. I'll decide by the end of March, and I'll tell Victor myself before anything's announced."),
                ("", "Pip writes the Stay-or-Go Ledger on Sunday afternoon, on a calm day. He hasn't decided. But for the first time in months, Sunday evening tastes of nothing in particular."),
            ],
            note="He hasn't walked through the door. He's just checked it opens. That alone changes how the throne room feels.",
        ),
    ),
}
