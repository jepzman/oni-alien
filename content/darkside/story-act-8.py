# Series 4 · Act VIII · the long-form story fields, merged into content/darkside/act-8.py by scripts/grimoire.py.
# March 2030 to January 2031, the last Act. Hugo's burnout (Mar 2030); Asha Head of GridSight (Jun); Rupert's request
# (9 Sep); Pip removed from the steering group (2 Oct) and goes to Karen; Tomasz's concern (Nov); Rafi leaves (Nov);
# Rupert's contract ends (Dec); the Chronicler retires (31 Jan 2031) and hands Pip the grimoire.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the Slow Hex of Burnout
    "slow-hex-of-burnout": dict(
        sighting=f"""{beat("January and February 2030 · the signs")}
<p>After the kitchen conversation in Act VII, Hugo cancelled twenty meetings. It helped for a fortnight. Then Ascend's
second phase began and the meetings grew back, like weeds. He stopped going to the Tuesday lunch. He snapped at Rafi over
a typo, then apologised for twenty minutes. He told Pip he couldn't remember the last book he'd finished.</p>
{beat("Thursday 6 March · 08:40")}
<p>Hugo drove to The Grid, parked, turned off the engine, and could not get out of the car. He sat there for an hour and
ten minutes with his badge in his hand, while it rained. Then he rang Pip, the one person who'd once asked how he was.</p>
{beat("That morning · the Naming")}
<p>Pip came down to the car park with two coffees and got in the passenger seat. Hugo said: “I think something's wrong
with me.” Pip said: “I think you might be burning out. You're not the first. Will you see a doctor today?” Hugo's GP
signed him off for four weeks. Ruth told Hugo's manager, kindly and quickly, and the programme was reassigned for a month.</p>
{beat("April to June · the Condition Change")}
<p>Occupational health recommended a phased return: three days a week for a month, one programme instead of three,
no meetings after 16:00. Hugo agreed, and asked for it in writing (he'd read the Phylactery). By June he was back full
time, with one programme, a Friday Outcome Ledger and a Salt Circle. He still says “crazy week”. Now he means it as a joke.</p>
{note("Burnout isn't weakness. It's what happens to strong people who carried too much for too long. Name it, get help, and change the load.")}""",
        origin=dict(
            title="How the hex was cast on Hugo, over three years",
            beats=[
                ("2026 · Lumen (Act II)", "Hugo lives on Slack and never sleeps. It works. He's praised for commitment. The first thread of the hex."),
                ("2027 · Horizon (Act V)", "He survives the Famine by being indispensable. Fear joins exhaustion. He stops taking holidays."),
                ("2029 · Ascend (Act VII)", "Fifty-four meetings a week, a mouse jiggler, three programmes. Cynicism arrives. He calls it “realism”."),
                ("March 2030 · the car park", "The hex completes. His body refuses what his mind kept agreeing to."),
            ],
            turning="Every year, being rewarded for the very habits that were wearing him down.",
            saved="A manager in 2027 asking “When did you last take a full week off?”, and acting on the answer.",
            note="Burnout is rarely one bad month. It's years of small overloads, each one praised.",
        ),
        know=f"""<p>Burnout is a state of chronic work stress that hasn't been managed: exhaustion, cynicism or detachment about work,
and a sense of being ineffective. It builds slowly. It overlaps with depression and anxiety, and can affect sleep, health
and relationships. It's caused mostly by conditions (load, control, fairness, recognition), not by personal weakness.</p>
<h3 class="kh">What it feeds on</h3>
<p>Unending demands, little control, no recovery time, and caring deeply about work that never finishes.</p>
<h3 class="kh">Why it's missed</h3>
<p>Because it arrives slowly, and because its early signs (long hours, always available) are often praised.</p>
<h3 class="kh">The three marks of the hex</h3>
<ul class="fears"><li>Exhaustion that rest doesn't fix.</li><li>Cynicism and distance from work you used to care about.</li><li>Feeling you achieve nothing.</li><li>Often: poor sleep, irritability, getting ill more.</li></ul>
<h3 class="kh">Three stages of the hex</h3>
<div class="breeds">
<div><b>The Smouldering</b><p>Tired and stretched, still functioning. The best time to act.</p></div>
<div><b>The Burning</b><p>Cynical, exhausted, slipping. Needs real changes and probably a doctor.</p></div>
<div><b>The Ash</b><p>Can't function. Needs time off, medical support and a different return.</p></div>
</div>
{note("If you ever feel hopeless or have thoughts of harming yourself, talk to a doctor or a crisis line today. That's not a work problem; it's a health emergency.")}""",
        difficulty=dict(
            normal=dict(who="The Smouldering.",
                        know=["You're tired most of the time.", "Work feels heavier than it used to.", "You still function well."],
                        do=["Do the Naming, to yourself and one person.", "Take real time off.", "Cut one thing from your load now."],
                        avoid="Pushing through.",
                        next="If cynicism and exhaustion stay after a break, you're at Nightmare."),
            nightmare=dict(who="The Burning.",
                           know=["Rest doesn't help.", "You're cynical about everything.", "Your work is slipping."],
                           do=["See a doctor.", "Tell your manager what you need changed.", "Ask about occupational health.", "Protect sleep above everything."],
                           avoid="The holiday cure.",
                           next="If you can't function, you're at Hell."),
            hell=dict(who="The Ash.",
                      know=["You can't face work.", "Your health is affected.", "Small tasks are impossible."],
                      do=["Stop. See a doctor today.", "Take the time off you're signed off for.", "Plan a phased return, in writing.", "Change the conditions before you go back."],
                      avoid="The shame hide.",
                      next="If the job can't change, read Life After the Dungeon."),
        ),
        mirror=dict(
            title="Is the hex on you?",
            intro="Tick honestly. This one matters.",
            signs=["You're exhausted after a weekend or holiday.", "You feel cynical about work you used to care about.",
                   "You feel you achieve nothing, however hard you work.", "You can't remember your last full week off.",
                   "People close to you have said you seem different."],
            cure="If you ticked three or more, tell one person this week: “I think I might be burning out.” Then book a doctor's appointment. Naming it is the first counter-spell.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 6 March 2030, 09:55, Hugo's car.",
            intro="The Naming.",
            lines=[
                ("Pip", "Coffee. Can I sit in?"),
                ("Hugo", "I've been here an hour. I can't make myself go in. I think something's wrong with me."),
                ("Pip", "I think you might be burning out. You're not the first, and it's not a weakness."),
                ("Hugo", "There's the programme board at eleven…"),
                ("Pip", "Ruth can cover it. Will you call your doctor this morning? I'll sit here while you do."),
                ("Hugo", "…Yes. Okay. Thank you."),
            ],
            note="Hugo says now that the most important thing anyone did was sit in the car. Not fix it. Just sit there.",
        ),
    ),
    # ------------------------------------------------------------------ the Salt Circle
    "salt-circle": dict(
        sighting=f"""{beat("March 2030 · the warning")}
<p>Watching Hugo, Pip noticed his own habits: email in bed, replies at 21:31 to messages sent at 21:30, a laptop on
holiday “just in case”. Nothing was wrong yet. That, the Annotator wrote in the margin, is exactly when to draw the circle.</p>
{beat("Monday 7 April · the Drawn Line")}
<p>Pip told Ruth and his team: offline after 19:00 and all weekend; if something's genuinely urgent, ring. He agreed with
Ruth what counted as urgent (the control room, a regulator, a board paper due next morning). Everything else would wait
until 08:00. Ruth said: “Good. Will you nag me to do the same?”</p>
{beat("Thursday 22 May · 21:34 · the test")}
<p>Rupert messaged: “Quick one: can you send the churn numbers tonight?” It wasn't on the urgent list. Pip's phone was
face down on the hall shelf. At 08:00 he sent the numbers with a warm note. Rupert replied: “Thanks, perfect.” He hadn't
looked at them until 10:00 anyway.</p>
{beat("Summer · the Unbroken Ring")}
<p>The messages after 19:00 dropped from a dozen a week to one or two. Nobody said anything about it. They'd just learned.
Pip slept better, read four books, and was noticeably less irritable on Tuesday mornings, according to Rafi.</p>
{note("A boundary is a circle drawn where everyone can see it. Draw it once. Keep it always.")}""",
        origin=dict(
            title="How Pip's circle was broken in the first place",
            beats=[
                ("2025 · the eager start", "New and keen, Pip replies to everything instantly. People notice and appreciate it."),
                ("2027 · the Famine", "During Horizon, being always available feels like safety. He never turns his phone off."),
                ("2029 · the habit", "Back at HQ with a long commute, he works on the train both ways, then again at night. It's just how it is."),
                ("March 2030 · the mirror", "He sees Hugo in the car park, and sees where his own road leads."),
            ],
            turning="Fear during the Famine turning availability from a courtesy into armour.",
            saved="Drawing the line in his first year, when it would have seemed normal rather than a change.",
            note="Boundaries are easiest to set at the start of a job. The next easiest time is now.",
        ),
        know=f"""<p>A boundary is a limit on when, how and how much you're available for work. Good boundaries are specific, known to
others and consistently kept. Without them, work expands to fill every hour you allow, not out of malice but because
everyone else's urgency reaches you directly.</p>
<h3 class="kh">What tests it</h3>
<p>“Quick” messages, late requests from senior people, deadlines, guilt.</p>
<h3 class="kh">Why it breaks</h3>
<p>Because nobody knew it was there, or because it was kept only sometimes, which teaches people to keep trying.</p>
<h3 class="kh">What makes it hold</h3>
<ul class="fears"><li>Specific times.</li><li>An agreed emergency route.</li><li>Telling people once, kindly.</li><li>Keeping it every time.</li></ul>
<h3 class="kh">Three kinds of circle</h3>
<div class="breeds">
<div><b>The Time Circle</b><p>Hours you're offline. The most common, and the most tested.</p></div>
<div><b>The Scope Circle</b><p>Work you won't take on. See the Word of Power: No.</p></div>
<div><b>The Self Circle</b><p>Things you won't do or accept, however asked. See the Dark Pact.</p></div>
</div>
{note("If you manage people, your boundaries are permission for theirs. Send late emails, and your team will reply to them.")}""",
        difficulty=dict(
            normal=dict(who="A reasonable workplace, an undrawn circle.",
                        know=["Nobody expects instant replies.", "You do it anyway.", "Your manager would support a boundary."],
                        do=["Draw the line specifically.", "Tell people once.", "Turn off notifications after hours."],
                        avoid="The invisible line.",
                        next="If people keep testing it, you're at Nightmare."),
            nightmare=dict(who="The tested circle.",
                           know=["Late messages keep coming.", "Some are from senior people.", "You feel guilty not replying."],
                           do=["Agree the Emergency Gate with your manager.", "Reply warmly in the morning.", "Keep it every time.", "Restate it once if needed."],
                           avoid="The just-this-once.",
                           next="If out-of-hours replies are demanded, you're at Hell."),
            hell=dict(who="The always-on culture.",
                      know=["Instant replies are expected at all hours.", "Boundaries are seen as lack of commitment.", "Others are burning out."],
                      do=["Talk to your manager about expectations and pay.", "Know your contract and working-time rights.", "Find allies.", "Read the Slow Hex."],
                      avoid="The angry ring.",
                      next="If it never changes, read Life After the Dungeon."),
        ),
        mirror=dict(
            title="Do you break other people's circles?",
            intro="Tick honestly.",
            signs=["You send work messages late at night.", "You expect quick replies outside hours.",
                   "You've said “sorry to message late” and messaged anyway.", "You've been irritated when someone didn't reply on a weekend.",
                   "Your team replies to you at 22:00."],
            cure="Use scheduled send. Write your late-night message, schedule it for 08:00. You keep your thought; they keep their evening.",
        ),
        rehearsal=dict(
            title="Scene: Monday 7 April 2030, Pip's team meeting.",
            intro="The Drawn Line, said once.",
            lines=[
                ("Pip", "A small thing. From today I'm offline after seven and at weekends."),
                ("Rafi", "What if something breaks?"),
                ("Pip", "If it's the control room, a regulator or a board paper due next morning, ring me. Anything else, I'll pick up at eight."),
                ("Ruth", "Good. And you should all do the same."),
                ("Pip", "Will you?"),
                ("Ruth", "…Remind me in a month."),
            ],
            note="Pip reminded her in May. Ruth's last late email was sent on 2 May 2030.",
        ),
    ),
    # ------------------------------------------------------------------ the Mimic of Imposter Syndrome
    "imposter-mimic": dict(
        sighting=f"""{beat("Monday 2 June 2030 · the appointment")}
<p>Asha was appointed <b>Head of GridSight</b>: twelve people, eight clients, a budget of £2.4 million. Ruth announced it.
Everyone was delighted. Asha went home and told her partner she'd fooled them all, and it was only a matter of time.</p>
{beat("June · the mimic")}
<p>She worked until midnight preparing for meetings she'd have aced unprepared. She explained away every compliment
(“the team did it”, “I got lucky with Northshire”). In her first leadership meeting she said nothing for an hour because
everyone else seemed to know things she didn't.</p>
{beat("Friday 20 June · the Spoken Fear")}
<p>She told Pip, over lunch, quietly: “I think I'm a fraud.” Pip laughed, then saw she meant it, and stopped. He said he'd
felt exactly the same as acting head in 2027. Then she asked Ruth, who said: “Every single week of my first year at
Northgate.” Then she asked the Chronicler, who said: “Twenty-two years. Still sometimes.”</p>
{beat("The Evidence Chest")}
<p>Pip suggested she open her own files. Asha had kept Friday notes since the Green Dot episode, three years of them: the
Northshire win, the Brackenfield rescue, 312 data questions, four junior analysts trained. She read them on a Sunday
evening. The chest wasn't full of inadequacy. It was full of her.</p>
{note("The mimic looks like proof you don't belong. Open it. It's full of proof you do.")}""",
        origin=dict(
            title="How the mimic came to live in Asha's office",
            beats=[
                ("Childhood · the high bar", "Asha grows up being told she has to be twice as good to be considered equal. She becomes very, very good."),
                ("2025 · the glue years", "Her work at MetroVolt is invisible (see Act IV's Invisible Work Curse). Nobody says she's excellent, so she doesn't believe it."),
                ("2028 · GridSight", "She does the hardest work and gets the least credit (see Act VI). Success feels like luck because it was never named."),
                ("2030 · the promotion", "Finally named, she can't believe it. Years of unrecognised work became years of doubting herself."),
            ],
            turning="Years of excellent work that nobody named, so she never learned to name it herself.",
            saved="Managers saying, specifically and often: “That was excellent, and here's why.”",
            note="Imposter feelings are common in people whose work has been undervalued. They're a symptom of the room, not a verdict on you.",
        ),
        know=f"""<p>Imposter syndrome is the persistent feeling that you aren't as capable as others think, and that you'll be found out.
It's very common, especially in new roles and among people from groups who've been underestimated. It's not a diagnosis;
it's a pattern of thinking, and it often coexists with genuine competence.</p>
<h3 class="kh">What it whispers</h3>
<p>“You got lucky.” “They'll find out.” “Everyone else knows what they're doing.”</p>
<h3 class="kh">Why it lies</h3>
<p>Because you compare your inside (doubts, effort) with everyone else's outside (confidence, results).</p>
<h3 class="kh">What quietens it</h3>
<ul class="fears"><li>Written evidence.</li><li>Saying the fear out loud.</li><li>Hearing others admit it.</li><li>Calling it learning, not failing.</li></ul>
<h3 class="kh">Three kinds of mimic</h3>
<div class="breeds">
<div><b>The New-Role Mimic</b><p>Appears in the first months of anything. Fades with evidence.</p></div>
<div><b>The Room Mimic</b><p>Appears around senior people. Remember they're often feeling it too.</p></div>
<div><b>The Lifelong Mimic</b><p>Never quite leaves. Learn to hear it and do the work anyway.</p></div>
</div>
{note("If you manage someone, praise specifically. “Great job” bounces off the mimic. “Your Northshire plan won the contract because it was credible” sticks.")}""",
        difficulty=dict(
            normal=dict(who="The New-Role Mimic.",
                        know=["You've just started something new.", "You feel out of your depth.", "Your results are fine."],
                        do=["Open your Evidence Chest.", "Use the Learning Frame.", "Ask questions; it's allowed."],
                        avoid="Dismissing praise.",
                        next="If the feeling makes you overwork, you're at Nightmare."),
            nightmare=dict(who="The overworking imposter.",
                           know=["You over-prepare everything.", "You work late from fear.", "You never feel ready."],
                           do=["Do the Spoken Fear with someone senior.", "Set a limit on preparation.", "Read your evidence weekly.", "Draw a Salt Circle."],
                           avoid="The over-preparation spiral.",
                           next="If it stops you taking opportunities, you're at Hell."),
            hell=dict(who="The paralysing mimic.",
                      know=["You turn down roles.", "You stay silent in meetings.", "You've stopped trying new things."],
                      do=["Talk to a mentor or coach.", "Take one small stretch on purpose.", "Consider talking to a professional if anxiety is constant.", "Keep the chest open."],
                      avoid="Refusing the stretch.",
                      next="Remember: nobody feels ready. The ready-feeling comes after."),
        ),
        mirror=dict(
            title="Are you feeding someone else's mimic?",
            intro="Especially if you manage people. Tick honestly.",
            signs=["You rarely praise people specifically.", "You assume confident people are competent and quiet ones aren't.",
                   "You've never told your team you felt out of your depth once.", "You correct in public and praise in private, or not at all.",
                   "You've attributed someone's success to luck."],
            cure="This week, tell one person exactly what they did well and why it mattered. You may be quietening a mimic you didn't know was there.",
        ),
        rehearsal=dict(
            title="Scene: Friday 20 June 2030, lunch on floor 14.",
            intro="The Spoken Fear.",
            lines=[
                ("Asha", "Can I tell you something embarrassing? I think I'm a fraud. As Head of GridSight."),
                ("Pip", "…You won Northshire. You rescued Brackenfield. You trained half the team."),
                ("Asha", "I got lucky with Northshire."),
                ("Pip", "I felt exactly the same as acting head. Every day. Have you still got your Friday notes?"),
                ("Asha", "Three years of them."),
                ("Pip", "Read them on Sunday. Then tell me who wrote them."),
            ],
            note="On Monday Asha spoke first in the leadership meeting. She said later the mimic was still there. It just wasn't in charge.",
        ),
    ),
    # ------------------------------------------------------------------ the Phylactery of Paper
    "phylactery-of-paper": dict(
        sighting=f"""{beat("Tuesday 9 September 2030 · 16:30 · floor 27")}
<p>Rupert asked Pip, in a meeting with no one else present, to change the churn model's assumptions so that Ascend's
savings showed £14m rather than £9m for the parent board (see the Dark Pact). Pip said no and offered an alternative.
Rupert said: “Let's not put any of this in writing.”</p>
{beat("17:12 · the Confirming Email")}
<p>Pip wrote anyway. Short, factual, friendly: <i>“Thanks for today. To confirm what we discussed: you asked for the savings
to show £14m; I explained the model supports £9m. I'll send both the base case and a clearly labelled upside scenario,
with assumptions, by Friday.”</i> He copied Ruth. He saved it in his own folder, alongside his Book of Deeds.</p>
{beat("Thursday 2 October · the test")}
<p>Rupert removed Pip from the Ascend steering group and told Ruth Pip “wasn't a team player on the board paper”. When
Ruth asked what that meant, Rupert said Pip had “misunderstood the request”. Pip's email, sent the same day and never
disputed, said otherwise.</p>
{beat("October · the folder speaks")}
<p>When Pip went to Karen in HR (see HR's True Allegiance), he brought a timeline, the email, his Book of Deeds (three
years of Fridays) and his last three reviews, all excellent. Karen said, after reading it: “This is the clearest file I've
been given all year.” The phylactery held.</p>
{note("Words fade, memories change, people leave. Paper stays. Keep your soul in writing.")}""",
        origin=dict(
            title="How Pip's phylactery was built, without his knowing",
            beats=[
                ("2028 · the Book of Deeds (Act IV)", "Pip starts writing one line every Friday, to make his reviews easier. It becomes a habit."),
                ("2028 · the Change Ledger (Act VI)", "With Gavin, he learns to confirm every change in writing, the same day. It becomes a reflex."),
                ("2029 · the Decision Rule (Act VII)", "He pushes for decisions to be written down. He starts doing it for his own 1:1s too."),
                ("2030 · the phylactery", "By the time he needs protection, he's been building it for three years, for other reasons."),
            ],
            turning="Good habits adopted for ordinary reasons, which turned out to be armour.",
            saved="Nothing needed saving. This is how it should go: write things down long before you need to.",
            note="Documentation isn't paranoia when it's a habit. It only looks paranoid when you start the day you're in trouble.",
        ),
        know=f"""<p>Documentation protects you because memories differ and change, especially under pressure. A short written record of
decisions, requests and your achievements, made at the time and kept somewhere you control, is often the deciding factor
in disputes, reviews and investigations. Done as a habit, it also just makes you better at your job.</p>
<h3 class="kh">What to keep</h3>
<p>Decisions and requests (especially unusual ones), your achievements, your reviews, your contract and pay letters, and any concerns you've raised.</p>
<h3 class="kh">Where to keep it</h3>
<p>Your own notes and copies of your own documents, somewhere you control, following company policy. Never confidential company data.</p>
<h3 class="kh">How to write it</h3>
<ul class="fears"><li>Same day.</li><li>Facts, not feelings.</li><li>Short and friendly.</li><li>Copy the right people.</li></ul>
<h3 class="kh">Three kinds of phylactery</h3>
<div class="breeds">
<div><b>The Deed Book</b><p>Your achievements. For reviews, promotions and CVs.</p></div>
<div><b>The Decision Scroll</b><p>What was agreed. For disputes and changing memories.</p></div>
<div><b>The Concern Record</b><p>What you raised and when. For the rare day it really matters.</p></div>
</div>
{note("Secretly recording conversations is illegal or against policy in many places. A friendly confirming email is legal everywhere and far more useful.")}""",
        difficulty=dict(
            normal=dict(who="The ordinary habit.",
                        know=["Nothing is wrong.", "Decisions are sometimes verbal.", "Reviews rely on memory."],
                        do=["Start the Book of Deeds.", "Confirm big decisions by email.", "Keep copies of your reviews."],
                        avoid="The memory gamble.",
                        next="If someone senior avoids writing things down, you're at Nightmare."),
            nightmare=dict(who="The unwritten request.",
                           know=["You're asked for something unusual, verbally.", "“Let's not put this in writing.”", "You feel uneasy."],
                           do=["Send the Confirming Email the same day.", "Copy your manager.", "Save it in your own folder.", "Stick to facts."],
                           avoid="The paranoid record.",
                           next="If the record is disputed or used against you, you're at Hell."),
            hell=dict(who="The disputed record.",
                      know=["Someone denies what was said.", "Your role or review is affected.", "HR or an investigation is involved."],
                      do=["Assemble a timeline with documents.", "Go to HR with the folder.", "Get independent advice if it's serious.", "Stay factual and calm."],
                      avoid="Stealing the vault.",
                      next="Read HR's True Allegiance."),
        ),
        mirror=dict(
            title="Is your soul unprotected?",
            intro="Tick honestly.",
            signs=["You don't have copies of your last three reviews.", "Your achievements live only in your memory.",
                   "Important decisions with your manager are never written down.", "You couldn't build a timeline of last year if you needed to.",
                   "You've been told “I never said that” and had nothing to show."],
            cure="Tonight, start a document. One line: what you did this week. Then one line every Friday. In three years, it'll be your best friend.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 9 September 2030, 17:05, Pip at his desk.",
            intro="The Confirming Email.",
            lines=[
                ("Pip (draft)", "Rupert, thanks for today. You asked me to change the assumptions so savings show £14m, and that I mustn't put anything in writing. I was appalled."),
                ("Pip (to himself)", "Too much. Facts, not feelings."),
                ("Pip (draft 2)", "Thanks for today. To confirm what we discussed: you asked for the savings to show £14m; I explained the model supports £9m."),
                ("Pip (draft 2)", "I'll send both the base case and a clearly labelled upside scenario, with assumptions, by Friday."),
                ("Pip (to himself)", "Copy Ruth. Save a copy. Send."),
            ],
            note="Rupert never replied to it. Silence, Karen observed later, is also a kind of agreement.",
        ),
    ),
    # ------------------------------------------------------------------ Reputation Is Your Hit Points
    "reputation-hit-points": dict(
        sighting=f"""{beat("2026 · the drain")}
<p>In Act II, Dorian was the Credit Vampire: he presented Pip's outage model as his own, twice. When it came out, his
reputation dropped like a health bar hit by a boss. For a year, people checked his work twice, left him out of meetings,
and said “Dorian?” with a particular tone.</p>
{beat("2027 to 2029 · the Steady Heal")}
<p>Dorian did the small things, every time. He named his builders in every presentation (“Asha's data, Tomasz's model”).
He delivered what he said, when he said. When he got something wrong in 2028, he owned it in the same meeting: “That was
my error; here's the fix.” Nobody noticed any single one of these. Everybody noticed the pattern, eventually.</p>
{beat("Monday 14 April 2030 · the test")}
<p>A new director, who'd never met Dorian, asked around about him before giving him a big planning role. The answers came
back: “reliable”, “gives credit”, “owns his mistakes”. One person said: “He used to be a bit of a credit-taker, years
ago. Not now.” The director gave him the role.</p>
{beat("Later that week")}
<p>Dorian told Pip about it over coffee, and then said something he'd never said before: “I'm sorry about the outage model.
In 2026. I should have said it then.” Pip said: “You've been saying it every week for four years.”</p>
{note("Hit points drain in a moment and heal one tick at a time. Keep ticking.")}""",
        origin=dict(
            title="How Dorian lost his hit points, and got them back",
            beats=[
                ("2024 · the old school", "Dorian's first manager taught him that whoever presents the work owns it. He believed it."),
                ("2026 · the big hit", "Caught presenting Pip's model as his own. In one meeting, years of reputation drain away."),
                ("2027 · the choice", "He could leave and start again elsewhere, or stay and rebuild. He stays. It's harder."),
                ("2027–2030 · the ticks", "Hundreds of small, reliable, credit-giving acts. By 2030, the bar is full again, and stronger for being rebuilt."),
            ],
            turning="Choosing to stay and rebuild, slowly, rather than run from a damaged reputation.",
            saved="Nothing saved him from the first hit. What saved his career was consistency afterwards.",
            note="A reputation can be rebuilt. Not with an apology tour. With years of being reliably the person you want to be known as.",
        ),
        know=f"""<p>Your reputation at work is what people say about you in rooms you're not in. It's built from many small
experiences: did you deliver, were you fair, did you give credit, were you the same with juniors as with seniors? It's lost
much faster than it's built, usually through a single visible act of unreliability or unfairness, and it's healed only by
consistent behaviour over time.</p>
<h3 class="kh">What builds it</h3>
<p>Reliability, fairness, credit given, mistakes owned. Boring, repeated, unglamorous.</p>
<h3 class="kh">What drains it</h3>
<p>Broken promises, credit taken, mistakes hidden, two faces. One big hit or many small cuts.</p>
<h3 class="kh">What heals it</h3>
<ul class="fears"><li>Consistency over months and years.</li><li>Owning mistakes fast.</li><li>Giving credit visibly.</li><li>Patience.</li></ul>
<h3 class="kh">Three kinds of reputation damage</h3>
<div class="breeds">
<div><b>The Scratch</b><p>A small mistake. Owned fast, healed in weeks.</p></div>
<div><b>The Wound</b><p>A visible failure or unfairness. Healed in a year or two of consistency.</p></div>
<div><b>The Curse</b><p>A betrayal of trust. Heals slowly, if ever, and only with years of change.</p></div>
</div>
{note("Juniors become seniors. The way you treat someone in their first year is the reputation they'll carry about you for thirty.")}""",
        difficulty=dict(
            normal=dict(who="The Scratch.",
                        know=["A small, visible mistake.", "People noticed.", "Your record is otherwise good."],
                        do=["Do the Fast Own.", "Fix it visibly.", "Carry on being reliable."],
                        avoid="The slow cover-up.",
                        next="If people now doubt you, you're at Nightmare."),
            nightmare=dict(who="The Wound.",
                           know=["People check your work more.", "You're left out of rooms.", "An old mistake keeps coming up."],
                           do=["Do the Steady Heal, every day.", "Give credit visibly.", "Ask a trusted colleague what people say.", "Be patient: a year, maybe two."],
                           avoid="The big gesture heal.",
                           next="If it was a betrayal of trust, you're at Hell."),
            hell=dict(who="The Curse.",
                      know=["You did something genuinely unfair.", "People don't trust you.", "It's your reputation's defining story."],
                      do=["Acknowledge it, once, sincerely, to the person affected.", "Change the behaviour permanently.", "Accept it'll take years.", "Consider whether a fresh start is wiser."],
                      avoid="The two faces.",
                      next="Ask Dorian. It can be done."),
        ),
        mirror=dict(
            title="How full is your bar?",
            intro="Tick honestly.",
            signs=["You've missed a deadline without warning someone first.", "You've taken credit that wasn't fully yours.",
                   "You're nicer to seniors than juniors.", "You've hidden a mistake and hoped nobody noticed.",
                   "You don't know what people say about you."],
            cure="Ask one trusted colleague: “What's my reputation here, honestly?” Then listen without defending.",
        ),
        rehearsal=dict(
            title="Scene: Friday 18 April 2030, Dorian and Pip, coffee.",
            intro="The apology, four years late, and already made.",
            lines=[
                ("Dorian", "The new director asked about me. People said I give credit. Me."),
                ("Pip", "You do. Every presentation."),
                ("Dorian", "I'm sorry about the outage model. In 2026. I should have said it then."),
                ("Pip", "You've been saying it every week for four years. Just not in words."),
                ("Dorian", "…Can I say it in words anyway?"),
                ("Pip", "You just did. Thank you."),
            ],
            note="Dorian's planning team has the lowest staff turnover in Customer. He credits Act II. Literally: he's read it.",
        ),
    ),
    # ------------------------------------------------------------------ the Word of Power: No
    "word-of-power-no": dict(
        sighting=f"""{beat("Tuesday 10 June 2030 · the great opportunity")}
<p>Rupert offered Pip “a fantastic opportunity”: to lead the new Ascend Data Office, alongside the churn model, his team,
and two GridSight reviews. It would be his fifth major commitment. Rupert said he was “the only person who could do it”.</p>
{beat("That evening · the inventory")}
<p>Pip wrote down what he was protecting: the churn model (due September, used by three strategies), Rafi's development,
his Salt Circle, and, if he was honest, his sleep. The Data Office would take half his week. Something would break.</p>
{beat("Wednesday 11 June · the Word")}
<p>Pip went to Ruth first, then Rupert. He said no, early, with a priority and an alternative: he'd protect the churn
model; he'd review the Data Office plan in an hour; and he named Rafi as someone who'd be excellent on the data side, with
support. Rupert was briefly annoyed. Ruth backed Pip.</p>
{beat("September · the outcome")}
<p>The churn model shipped on time and became the base of every Ascend savings estimate. Rafi took a role in the Data
Office and thrived (it later helped him get his start-up job). The Data Office was led by someone else, who had the time.
Rupert, in his September review of Pip, wrote: “Clear about priorities.” Which was true.</p>
{note("No is a complete sentence. At work, add a priority and an alternative, and it becomes a career skill.")}""",
        origin=dict(
            title="How Pip learned the word",
            beats=[
                ("2025 · the yes years", "Pip says yes to everything. He's rewarded with more of everything."),
                ("2027 · the Poisoned Chalice (Act IV)", "He learns to negotiate terms before accepting. The first step towards no."),
                ("2028 · the Trade-Off Menu (Act VI)", "With clients, he learns to say “yes, if”. It works better than yes or no."),
                ("2030 · the word", "After watching Hugo burn out with three programmes, he finally says it plainly to someone senior."),
            ],
            turning="Seeing what “yes” to everything did to Hugo.",
            saved="Learning, early, that the people who say no well are often more respected, not less.",
            note="A good no protects your yeses. Every yes you can't deliver well is a broken promise in disguise.",
        ),
        know=f"""<p>Saying no at work is a skill. Done badly (late, bare, resentful) it damages relationships. Done well (early, with
reasons and alternatives) it builds trust: people learn your yes means yes. Most requests aren't orders; they're asks
made by people who don't know your load.</p>
<h3 class="kh">What makes a good no</h3>
<p>Early, specific, linked to a priority, with an alternative.</p>
<h3 class="kh">Why it's hard</h3>
<p>Fear of seeming unhelpful, flattery (“you're the only one”), and the sense that opportunities won't come again.</p>
<h3 class="kh">The shapes of a good no</h3>
<ul class="fears"><li>“No, because I'm protecting X.”</li><li>“Not now, but in October.”</li><li>“Not all of it; I could do this part.”</li><li>“Not me, but here's who.”</li></ul>
<h3 class="kh">Three kinds of request</h3>
<div class="breeds">
<div><b>The Genuine Ask</b><p>They don't know your load. Tell them; they'll often withdraw it.</p></div>
<div><b>The Flattering Ask</b><p>“You're the only one.” You aren't. Name someone.</p></div>
<div><b>The Disguised Order</b><p>It's not really optional. Then negotiate what drops.</p></div>
</div>
{note("If you can't say no to your boss, say “yes, and what should I drop?” It's the same spell in a politer robe.")}""",
        difficulty=dict(
            normal=dict(who="The Genuine Ask.",
                        know=["A reasonable request.", "The asker doesn't know your load.", "Your manager would back you."],
                        do=["Say no early.", "Name your priority.", "Offer an alternative."],
                        avoid="The maybe fog.",
                        next="If it's flattery from someone senior, you're at Nightmare."),
            nightmare=dict(who="The Flattering Ask from above.",
                           know=["A senior person.", "“You're the only one who can.”", "Framed as an opportunity."],
                           do=["Talk to your manager first.", "Use the Priority Shield.", "Offer a part, or a name.", "Thank them for thinking of you."],
                           avoid="The resentful yes.",
                           next="If it's not really optional, you're at Hell."),
            hell=dict(who="The Disguised Order.",
                      know=["Refusing isn't really allowed.", "Your load is already too high.", "Something will break."],
                      do=["Say “yes, and what should I drop?”", "Get the answer in writing.", "Tell your manager what's at risk.", "Protect your Salt Circle."],
                      avoid="The bare no.",
                      next="If it's constant, read the Slow Hex."),
        ),
        mirror=dict(
            title="Do you make it hard for others to say no?",
            intro="Tick honestly.",
            signs=["You've told someone they're “the only one” who can do something.", "You ask for things without asking what's on their plate.",
                   "You've been annoyed when someone declined.", "You frame extra work as an opportunity.",
                   "Your team never says no to you."],
            cure="Next time you ask for something, add: “Say no if you're full; I'd rather know.” Then mean it.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 11 June 2030, Pip and Rupert.",
            intro="The Priority Shield and the Offered Alternative.",
            lines=[
                ("Rupert", "So, the Data Office. You're the only one who can do it."),
                ("Pip", "Thank you. I've thought hard. I need to say no to leading it."),
                ("Rupert", "That's disappointing."),
                ("Pip", "I'm protecting the churn model till September. Every Ascend savings number depends on it."),
                ("Pip", "I could review the Data Office plan in an hour this week. And Rafi would be brilliant on the data side, with support."),
                ("Rupert", "…Fine. Send me the review."),
            ],
            note="Three months later, Rupert needed the churn model for the board. It was ready. Then he asked Pip to change it.",
        ),
    ),
    # ------------------------------------------------------------------ the Dark Pact
    "dark-pact": dict(
        sighting=f"""{beat("Tuesday 9 September 2030 · 16:30 · floor 27")}
<p>Rupert called Pip to his office. The parent group's board met on 30 September. Ascend's savings, based on Pip's churn
model, came to <b>£9m</b>. The target in Rupert's 2029 memo had implied £14m. Rupert slid a page across the table: four
assumptions, changed. “Just use these. Everyone adjusts assumptions. The board expects £14m.”</p>
{beat("The pact, examined")}
<p>Pip read the page. Churn reduction doubled with no evidence. A cost saving counted twice. Two programmes' benefits
claimed by both. It wasn't an assumption; it was a story. He felt sick. Then he remembered: there's always an honest
alternative.</p>
{beat("16:45 · the refusal")}
<p>Pip said, calmly: he couldn't change the assumptions; the data didn't support it. He could show the £9m base case and
a clearly labelled upside scenario, with what would have to be true for it. Rupert said “Let's not put this in writing”
and “I'd hoped you were a team player”. Pip went back to his desk, wrote the Confirming Email (see the Phylactery), and
rang Ruth.</p>
{beat("30 September · the board")}
<p>Ruth backed him, took it to the CFO, and the board paper showed £9m with a labelled upside of £11m. The board asked
sensible questions and approved Ascend's next phase anyway. The pact was never signed. It did, however, have a price,
which arrived on 2 October (see HR's True Allegiance).</p>
{note("Every dark pact is offered as a small favour. Read the price: it's always your name.")}""",
        origin=dict(
            title="How Rupert came to offer the pact",
            beats=[
                ("2028 · the target", "The parent group gives Rupert a cost target. His bonus and next role depend on it."),
                ("June 2029 · the memo (Act VII)", "He announces “30% more with 20% fewer”. The number becomes a promise he has to keep."),
                ("2030 · the gap", "The real savings come in at £9m. The promise was £14m. He's seen others “adjust” before. Nobody was caught."),
                ("9 September · the pact", "He asks the person whose name is on the model. Not out of evil. Out of fear, and habit, and a deadline."),
            ],
            turning="A public number, promised before the work was done, that became impossible to walk back.",
            saved="Rupert saying to his own boss in June: “The real number is £9m. Here's why.” It would have cost him less than the pact did.",
            note="Most people who offer dark pacts aren't villains. They're frightened people with a deadline. That doesn't make the pact less dark.",
        ),
        know=f"""<p>A dark pact is a request to do something unethical or dishonest at work: change numbers, hide a problem, mislead a
customer or regulator, skip a safety step. It's usually framed as small, normal or necessary, and comes from someone with
power over you. Refusing is frightening. Agreeing is usually worse, because the work has your name on it.</p>
<h3 class="kh">How it's offered</h3>
<p>Verbally, under time pressure, with “everyone does it”, “it's just an assumption”, “be a team player”.</p>
<h3 class="kh">Why people sign</h3>
<p>Fear of the boss, wanting to be liked, believing it's small, and not seeing an alternative.</p>
<h3 class="kh">How to refuse</h3>
<ul class="fears"><li>Say no clearly and calmly.</li><li>Offer an honest alternative.</li><li>Write it down the same day.</li><li>Tell your manager.</li></ul>
<h3 class="kh">Three kinds of pact</h3>
<div class="breeds">
<div><b>The Grey Pact</b><p>Spin, emphasis, optimism. Argue for honesty; label scenarios clearly.</p></div>
<div><b>The Dark Pact</b><p>Falsifying, misleading, hiding. Refuse, document, escalate.</p></div>
<div><b>The Black Pact</b><p>Illegal or dangerous. Refuse, take advice, and see the Whistle of Last Resort.</p></div>
</div>
{note("If you're asked to do something that might be illegal, take independent advice before you do anything else, including refusing in a way that could be used against you.")}""",
        difficulty=dict(
            normal=dict(who="The Grey Pact.",
                        know=["Pressure to present things optimistically.", "No falsification yet.", "Your manager is reasonable."],
                        do=["Offer clearly labelled scenarios.", "Show what would have to be true.", "Discuss it openly."],
                        avoid="The small signature.",
                        next="If you're asked to change facts, you're at Nightmare."),
            nightmare=dict(who="The Dark Pact, from someone senior.",
                           know=["You're asked to change numbers or hide facts.", "It's verbal and urgent.", "You're told to keep it quiet."],
                           do=["Refuse calmly.", "Offer the Honest Alternative.", "Send the Confirming Email.", "Tell your manager the same day."],
                           avoid="The silent refusal.",
                           next="If there's retaliation or it's illegal, you're at Hell."),
            hell=dict(who="The Black Pact, or retaliation for refusing.",
                      know=["It may be illegal or unsafe.", "You're being punished for refusing.", "Your manager can't or won't help."],
                      do=["Get independent legal advice.", "Go to HR with your file.", "Use the speak-up route.", "Read the Whistle of Last Resort."],
                      avoid="The public accusation.",
                      next="Read HR's True Allegiance."),
        ),
        mirror=dict(
            title="Have you offered a pact?",
            intro="Especially if you manage people. Tick honestly.",
            signs=["You've asked someone to make numbers “look better”.", "You've said “let's not put this in writing”.",
                   "You've promised a number before the work was done.", "You've told someone refusing wasn't being a team player.",
                   "You've adjusted something you'd be embarrassed to explain."],
            cure="If you've promised a number you can't hit, tell your boss now. The truth costs less today than it will on board day.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 9 September 2030, 16:40, Rupert's office.",
            intro="The Honest Alternative.",
            lines=[
                ("Rupert", "Just use these assumptions. Everyone adjusts. The board expects fourteen."),
                ("Pip", "I can't change them. The data doesn't support doubling the churn reduction, and one saving's counted twice."),
                ("Rupert", "It's an assumption, Pip. Not a crime."),
                ("Pip", "What I can do: the £9m base case, and a clearly labelled upside, with exactly what would have to be true to reach it."),
                ("Rupert", "Let's not put any of this in writing. I'd hoped you were a team player."),
                ("Pip", "I'll send both scenarios by Friday."),
            ],
            note="Pip's hands were shaking when he left. He wrote the email anyway. Then he rang Ruth from the stairwell.",
        ),
    ),
    # ------------------------------------------------------------------ HR's True Allegiance
    "hr-true-allegiance": dict(
        sighting=f"""{beat("Thursday 2 October 2030 · the price")}
<p>Three weeks after Pip refused the Dark Pact, Rupert removed him from the Ascend steering group and told Ruth he “wasn't
a team player on the board paper”. Pip's September review, due that month, was suddenly “under discussion”.</p>
{beat("Friday 3 October · the doubt")}
<p>Pip didn't want to go to HR. Everyone said HR protected managers. The Annotator, in the margin: <i>“HR protects the
company. A senior manager punishing someone for refusing to falsify a board paper is a very large risk to the company.
Go.”</i></p>
{beat("Tuesday 7 October · Karen")}
<p>Pip brought the Facts Folder: a one-page timeline, the 9 September email, the board paper, his Book of Deeds, his last
three reviews. He asked for two things: his review to be completed on its merits, and the steering-group decision to be
looked at. Karen read everything twice, asked careful questions, and explained what would happen next and what she could
and couldn't keep confidential.</p>
{beat("October to December · the allegiance")}
<p>Karen opened a formal review. The CFO confirmed the board-paper history. Pip's review was completed by Ruth: “exceeds
expectations”. He was reinstated to the steering group in November. Rupert's contract with MetroVolt ended in December;
the parent group said only that Ascend was “moving to a new phase”. Karen told Pip, carefully: “I work for the company.
This time, that meant working for you.”</p>
{note("HR serves the company. Bring them a problem that's also the company's risk, with the facts, and you'll find an ally.")}""",
        origin=dict(
            title="How HR came to be mistrusted",
            beats=[
                ("1990s · Personnel", "HR is “personnel”: payroll, hiring, policies. It's seen as admin."),
                ("2000s · the business partner", "HR becomes a partner to managers, helping them deliver. Employees start to see it as management's side."),
                ("2010s · the stories", "Everyone hears of someone who went to HR and was managed out. The stories spread faster than the good outcomes."),
                ("Karen · 2027 onwards", "Karen (Act IV's pay-band owner) has seen it all. She knows exactly whose side she's on, and when that's you."),
            ],
            turning="A role that serves the company being mistaken, by everyone, for one that serves either managers or employees.",
            saved="Understanding from the start: HR's job is to protect the company, including from bad managers.",
            note="HR isn't your friend or your enemy. It's the company's immune system. Bring it a genuine infection, with evidence.",
        ),
        know=f"""<p>HR exists to protect and serve the organisation: to hire, pay, develop and manage people, and to keep the company
out of legal and reputational trouble. That means HR is not your advocate. But it also means HR has strong reasons to act
when a manager's behaviour (retaliation, discrimination, harassment, unsafe or unlawful requests) exposes the company to
risk.</p>
<h3 class="kh">What HR is for</h3>
<p>The company's people processes, and its legal and reputational safety.</p>
<h3 class="kh">When your interests align</h3>
<p>When your problem is also a risk: discrimination, harassment, retaliation, safety, legal breaches, serious misconduct.</p>
<h3 class="kh">How to go well</h3>
<ul class="fears"><li>A one-page timeline.</li><li>Documents, not just feelings.</li><li>A clear ask.</li><li>Independent advice if serious.</li></ul>
<h3 class="kh">Three kinds of HR visit</h3>
<div class="breeds">
<div><b>The Advice Visit</b><p>Questions about policy or options. Usually low risk.</p></div>
<div><b>The Concern Visit</b><p>A problem with a manager or colleague. Bring facts; ask what's confidential.</p></div>
<div><b>The Formal Complaint</b><p>A grievance or whistleblowing. Get advice; follow the process exactly.</p></div>
</div>
{note("Ask HR, before you share details: “What can you keep confidential, and what would you have to act on?”")}""",
        difficulty=dict(
            normal=dict(who="The Advice Visit.",
                        know=["A question about policy.", "No conflict yet.", "HR is approachable."],
                        do=["Ask clearly.", "Ask what's confidential.", "Keep notes of the answer."],
                        avoid="The confession booth.",
                        next="If your manager is the problem, you're at Nightmare."),
            nightmare=dict(who="The Concern Visit.",
                           know=["Your manager or a senior person is the problem.", "It's affecting your work or review.", "You're unsure HR will help."],
                           do=["Bring the Facts Folder.", "Make a clear ask.", "Frame it as a risk: retaliation, fairness.", "Follow up in writing."],
                           avoid="The emotional complaint.",
                           next="If it's retaliation, discrimination or illegal, you're at Hell."),
            hell=dict(who="The Formal Complaint.",
                      know=["Serious wrongdoing or retaliation.", "Your job may be at risk.", "Lawyers may get involved."],
                      do=["Get independent advice first.", "Follow the formal process exactly.", "Keep every document.", "Don't discuss it widely."],
                      avoid="The total distrust.",
                      next="If internal routes fail on something serious, read the Whistle of Last Resort."),
        ),
        mirror=dict(
            title="Are you giving HR reasons to doubt you?",
            intro="Tick honestly.",
            signs=["You've gone to HR angry with no facts.", "You've expected HR to take your side automatically.",
                   "You've told HR things you assumed were confidential, without asking.", "You've never read your company's grievance policy.",
                   "You've avoided HR on something serious because of rumours."],
            cure="Read your company's grievance and speak-up policies once, on a calm day. You'll know the map before you need it.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 7 October 2030, Karen's office, floor 6.",
            intro="The Facts Folder.",
            lines=[
                ("Pip", "Before I start: what can you keep confidential, and what would you have to act on?"),
                ("Karen", "Good question. If it's a serious allegation, I'll have to act. I'll tell you before I do anything."),
                ("Pip", "Here's a one-page timeline. On 9 September I refused to change the board-paper assumptions, in writing. On 2 October I was removed from the steering group."),
                ("Karen", "And what are you asking for?"),
                ("Pip", "My review completed on its merits, and the steering-group decision looked at."),
                ("Karen", "That's clear. This is the clearest file I've been given all year."),
            ],
            note="Karen kept her word on every point. Pip now tells anyone who says “HR always sides with management” about floor 6.",
        ),
    ),
    # ------------------------------------------------------------------ the Whistle of Last Resort
    "whistle-of-last-resort": dict(
        sighting=f"""{beat("Monday 3 November 2030 · the discovery")}
<p>Tomasz, in Field Ops since Act V, was matching substation inspection records to van location data for a
route-planning project. Forty inspections by <b>Ironvale Services</b>, MetroVolt's maintenance contractor, couldn't have
happened: two signed at the same hour, sixty miles apart; vans that never left the depot. Substation inspections exist so
that faults are found before they hurt someone.</p>
{beat("Tuesday 4 November · “not your problem”")}
<p>Tomasz showed his manager. His manager said inspections were “the contractor's responsibility, not ours”, and that
Tomasz should “stick to the routing project”. Tomasz went home and didn't sleep.</p>
{beat("Wednesday 5 November · the Advisor")}
<p>He rang Pip, who'd once sat next to him, and Pip listened and said two things: write down exactly what you found, and
get independent advice before you do anything else. Tomasz called an independent whistleblowing advice line. They
explained his protections, and that the right first step was MetroVolt's own speak-up process, in writing.</p>
{beat("6 to 27 November · the Proper Route, then the Higher Gate")}
<p>He raised it formally through the Speak Up line, with a short factual summary and the evidence he'd legitimately used
for his project. He got an acknowledgement, then nothing for three weeks. On 27 November, following the policy, he wrote
again, to the Speak Up team and the Chair of the Audit Committee.</p>
{beat("December · the inspections")}
<p>The Audit Committee chair commissioned an independent check within days. All forty substations were inspected by 12
December. Two had faults; one was a serious oil leak. Ironvale's contract was suspended, then ended. MetroVolt reported
it to the regulator itself, so Tomasz never had to. His manager was spoken to. Tomasz was thanked, in writing, by Dame
Helena. He still hasn't fully slept well since November, but he says he'd do it again.</p>
{note("The whistle is a last resort, not a first. But when it's needed, it's needed. Blow it carefully, with advice, in the right order.")}""",
        origin=dict(
            title="How the inspections came to be invented",
            beats=[
                ("2027 · Horizon (Act V)", "The Famine cuts MetroVolt's own inspection team. The work goes to Ironvale, a contractor, on a fixed price per inspection."),
                ("2028 · the squeeze", "Ironvale's margins shrink. Its engineers are told to hit their numbers. Nobody at MetroVolt checks the records against anything."),
                ("2030 · the shortcut", "Some Ironvale crews start signing inspections they didn't do. The paperwork is perfect. The substations aren't inspected."),
                ("3 November · the match", "Tomasz joins two datasets for an unrelated project. The lie becomes visible, because two facts can't both be true."),
            ],
            turning="Outsourcing safety work without anyone checking it actually happened.",
            saved="One routine check, from 2027: match a sample of inspection records against independent data.",
            note="Serious wrongdoing is usually found by accident, by someone ordinary, doing something else. That someone might be you.",
        ),
        know=f"""<p>Whistleblowing means reporting serious wrongdoing (danger to health and safety, crime, fraud, environmental
damage, cover-ups) usually after normal routes have failed or aren't safe. In many countries whistleblowers have legal
protection from retaliation, but often only if they report in the right way, to the right people, in the right order.
Getting independent advice early is the single most protective thing you can do.</p>
<h3 class="kh">The usual order</h3>
<p>Write down what you know. Get advice. Raise it internally through the proper route, in writing. Escalate internally if ignored. Then, if serious and still ignored, a regulator. Going public is a last resort, and can remove your protection.</p>
<h3 class="kh">What protects you</h3>
<p>Following the process, acting in good faith and in the public interest, raising it in writing, and taking advice.</p>
<h3 class="kh">What to keep</h3>
<ul class="fears"><li>Your own notes and timeline.</li><li>Copies of what you raised and when.</li><li>Only the evidence you need, and advice on what you may keep.</li><li>Every reply, or the lack of one.</li></ul>
<h3 class="kh">Three gates of the whistle</h3>
<div class="breeds">
<div><b>The Inner Gate</b><p>Your company's speak-up process. Often enough.</p></div>
<div><b>The Higher Gate</b><p>Audit committee, board, or group compliance. When the inner gate fails.</p></div>
<div><b>The Outer Gate</b><p>The regulator. When serious and ignored. With advice.</p></div>
</div>
{note("Laws differ by country. Many have independent charities or advice lines for whistleblowers; call one before you act.")}""",
        difficulty=dict(
            normal=dict(who="The Inner Gate works.",
                        know=["Something serious is wrong.", "Your company has a speak-up process.", "It's taken seriously."],
                        do=["Write down what you found.", "Get advice.", "Raise it in writing through the process."],
                        avoid="Looking away.",
                        next="If nothing happens, you're at Nightmare."),
            nightmare=dict(who="The silence after raising it.",
                           know=["You raised it properly.", "No meaningful response.", "Your manager told you to drop it."],
                           do=["Follow up in writing.", "Escalate to the Higher Gate per policy.", "Keep every document.", "Stay in touch with your advisor."],
                           avoid="The social media blast.",
                           next="If you face retaliation or it's still ignored, you're at Hell."),
            hell=dict(who="Ignored, or punished.",
                      know=["The risk is serious and ongoing.", "Internal routes have failed.", "You're being treated differently."],
                      do=["Take legal advice now.", "Consider the regulator, with advice.", "Document any retaliation.", "Look after yourself; this is hard."],
                      avoid="The evidence raid.",
                      next="Protections exist for this. Use them, carefully."),
        ),
        mirror=dict(
            title="Would you look away?",
            intro="Tick honestly.",
            signs=["You've noticed something seriously wrong and said nothing.", "You don't know your company's speak-up process.",
                   "You've told someone it's “not our problem” when it might be.", "As a manager, you've discouraged someone from raising a concern.",
                   "You think whistleblowers are troublemakers."],
            cure="Find your company's speak-up policy today and read it. If you ever need it, you'll be glad you know the way.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 5 November 2030, Pip and Tomasz, on the phone.",
            intro="The Advisor, before anything else.",
            lines=[
                ("Tomasz", "Forty inspections that couldn't have happened. My manager says it's not our problem."),
                ("Pip", "It might be someone's life. First: write down exactly what you found, today. Facts, dates."),
                ("Tomasz", "Then go to the press?"),
                ("Pip", "No. Get independent advice first. There are advice lines for exactly this. Then the speak-up process, in writing."),
                ("Tomasz", "And if they ignore it?"),
                ("Pip", "Then there's a next gate, and your advisor will tell you which. You're not alone in this."),
            ],
            note="Tomasz kept the whole folder. The oil leak was at a substation two streets from a primary school.",
        ),
    ),
    # ------------------------------------------------------------------ Quiet Quitting vs Quiet Thriving
    "quiet-thriving": dict(
        sighting=f"""{beat("2015 · the Chronicler's decision")}
<p>After their third reorg, the Chronicler made a decision they never announced. They would do excellent work, in their
hours, with care. They'd mentor anyone who asked. They'd leave at 17:30 with the work done. They'd stop volunteering for
things that fed other people's ambitions. They called it, privately, <b>enough</b>.</p>
{beat("2015 to 2030 · the quiet thriving")}
<p>For fifteen years, the Chronicler's work was reliable and good. They trained Pip, Asha and a dozen others. They
gardened, sang in a choir and read everything. Some people thought they'd given up. The ones who worked with them knew
otherwise.</p>
{beat("Wednesday 15 October 2030 · Neil")}
<p>Neil, in Billing, had been passed over three times. In 2024 he'd stopped caring: minimum effort, camera off, resentful
silence. He asked the Chronicler, over coffee, how they'd done the same thing for so long without hating it. The Chronicler
said gently: “I didn't do the same thing. You stopped caring. I chose what to care about. They look alike from the
corridor.”</p>
{beat("That winter · the Honest Conversation")}
<p>Neil thought about it for a month. Then he asked Field Ops if they needed someone who understood billing data. They
did. In January he moved. He still leaves at 17:30. Now he leaves having done something he's proud of.</p>
{note("Enough is not a failure. Enough, chosen and done well, is a kind of freedom.")}""",
        origin=dict(
            title="How two people came to leave at 17:30",
            beats=[
                ("The Chronicler · 2015", "After a reorg that undid two years of their work, they decide work will be part of life, not all of it. They choose what to give."),
                ("Neil · 2019–2024", "Passed over three times, without explanation. Each time, he gives a little less. Nobody notices until he gives nothing extra at all."),
                ("2024–2030 · the two paths", "The Chronicler thrives quietly: good work, mentoring, a full life. Neil coasts resentfully: minimum work, a small grey life at his desk."),
                ("2030 · the conversation", "Neil notices they leave at the same time, and asks why one of them seems happy."),
            ],
            turning="Neil drifting into giving less, from hurt, rather than choosing it, from clarity.",
            saved="Neil, in 2019, being told honestly why he'd been passed over, and what would change it.",
            note="Quiet quitting is usually a wound. Quiet thriving is usually a decision. Both look like leaving on time.",
        ),
        know=f"""<p>“Quiet quitting” describes doing only what your job requires and no more. Sometimes it's a healthy correction to
overwork: doing your job, not donating your life. Sometimes it's a sign of deep disengagement: someone who's given up but
hasn't left. The behaviour can look identical. The difference is inside: resentment and emptiness, or clarity and peace.</p>
<h3 class="kh">Quiet thriving</h3>
<p>Good work, in your hours, with care, by choice, and a life outside that fills you.</p>
<h3 class="kh">Quiet quitting (the wounded kind)</h3>
<p>Minimum work, with resentment, because you've stopped believing anything will change.</p>
<h3 class="kh">How to tell which you are</h3>
<ul class="fears"><li>Are you proud of your work?</li><li>Do you leave feeling calm or bitter?</li><li>Is your life outside full?</li><li>Did you choose this, or drift into it?</li></ul>
<h3 class="kh">Three kinds of quiet</h3>
<div class="breeds">
<div><b>The Thriving Quiet</b><p>Chosen, peaceful, good work. Keep it.</p></div>
<div><b>The Resting Quiet</b><p>Recovering from overwork or burnout. Healthy, for a while.</p></div>
<div><b>The Wounded Quiet</b><p>Resentful, empty. Needs the Honest Conversation.</p></div>
</div>
{note("If you manage someone who's gone quiet, don't judge it. Ask, kindly, whether they chose it or were wounded into it.")}""",
        difficulty=dict(
            normal=dict(who="The Thriving Quiet.",
                        know=["You do your job well.", "You leave on time.", "You're content."],
                        do=["Keep the Deliberate Enough.", "Find a Chosen Extra.", "Ignore anyone who calls it quitting."],
                        avoid="The martyr's return.",
                        next="If you feel resentful, you're at Nightmare."),
            nightmare=dict(who="The Wounded Quiet.",
                           know=["You do the minimum.", "You feel bitter.", "You've stopped hoping."],
                           do=["Have the Honest Conversation with yourself.", "Ask why you were passed over, or what hurt.", "Look for a role you could care about.", "Talk to someone."],
                           avoid="The resentful coast.",
                           next="If it's become your whole life, you're at Hell."),
            hell=dict(who="The Hollow Years.",
                      know=["Years of resentful minimum.", "Work feels meaningless.", "It's affecting the rest of your life."],
                      do=["Consider whether it's burnout or depression; see a doctor.", "Decide: rekindle, move, or leave.", "Read Life After the Dungeon.", "Find meaning outside work."],
                      avoid="Staying out of inertia.",
                      next="You can leave. People do, and are glad."),
        ),
        mirror=dict(
            title="Which quiet are you?",
            intro="Tick honestly.",
            signs=["You leave on time feeling bitter rather than calm.", "You've stopped caring about work you used to enjoy.",
                   "You haven't had a conversation about your future here in years.", "Your life outside work feels thin.",
                   "You judge colleagues who still care."],
            cure="Ask yourself the Chronicler's question: “Did I choose this, or did I drift into it?” If you drifted, choose now.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 15 October 2030, the Chronicler and Neil.",
            intro="The Honest Conversation, prompted kindly.",
            lines=[
                ("Neil", "How have you done the same thing as me for fifteen years without hating it?"),
                ("The Chronicler", "I don't think we do the same thing."),
                ("Neil", "We both leave at half five. We both stopped volunteering."),
                ("The Chronicler", "You stopped caring. I chose what to care about. They look alike from the corridor."),
                ("Neil", "…What would you care about, if you were me?"),
                ("The Chronicler", "Something you'd be proud of at half five. Is there anything here like that?"),
            ],
            note="Neil found it in Field Ops. The Chronicler sent him a card on his first day: “Enough, chosen.”",
        ),
    ),
    # ------------------------------------------------------------------ the Exit Interview Trap
    "exit-interview-trap": dict(
        sighting=f"""{beat("October 2030 · the offer")}
<p>Rafi was offered a role at Kestrel, a small energy-data start-up. Better pay, smaller team, no hot-desks. He accepted,
gave a month's notice, and handed over beautifully. His last day was 28 November.</p>
{beat("The list")}
<p>Rafi had a list for the exit interview. Twenty-three items. Rupert's pact. The three roadmaps. The hot-desks. The
badge reports. The banner. The time VoltMind got the heatwave wrong and someone senior blamed the analysts. The list was
true. It was also, the Annotator noted, a crater, not a door.</p>
{beat("Monday 24 November · the interview")}
<p>Rafi said one useful thing: that the team had rebuilt its roadmap three times in a year, and that stable priorities
would help those who stayed more than anything. He thanked Ruth and Pip specifically: for the heatwave write-up, the Data
Office role, and the Salt Circle. Asked “anything else?”, he said: “No, thank you. I've learned a lot here.”</p>
{beat("Friday 28 November · the friend's ear")}
<p>That evening, at the pub, Rafi read all twenty-three items out loud to Pip and Asha. They laughed, agreed with most and
argued about two. In March 2031, MetroVolt's planning guidance included a new principle: “priorities stable for at least
two quarters”, citing exit-interview themes. Kestrel, it turned out, works with GridSight. Rafi is now Asha's client.</p>
{note("Leave a door, not a crater. Say one useful thing, thank them, and save the rest for friends.")}""",
        origin=dict(
            title="How the exit interview became a trap",
            beats=[
                ("The intention", "Exit interviews exist so companies can learn why people leave. It's a good idea."),
                ("The reality", "The answers go into a file. Patterns are sometimes acted on. Individual complaints rarely are."),
                ("The temptation", "Leavers feel free at last to say everything. It feels like justice. It mostly becomes a reputation."),
                ("The small world", "Leavers come back, become clients, need references. Rafi became Asha's client within a year."),
            ],
            turning="A useful listening tool being mistaken for a place to settle scores.",
            saved="Knowing, before the interview, what one point you want to make.",
            note="Exit interviews change things through patterns, not single complaints. Add one clear point to the pattern.",
        ),
        know=f"""<p>An exit interview is a conversation (or form) when you leave, asking why you're going and what could be better.
Companies use them to spot patterns. They're rarely fully confidential, rarely acted on individually, and sometimes read
by people who'll later give or receive references about you. Used well, they let you leave one useful thing behind.</p>
<h3 class="kh">What it's for</h3>
<p>Spotting patterns in why people leave. Sometimes, ticking a box.</p>
<h3 class="kh">Why it's a trap</h3>
<p>Because you feel free to say everything, and “everything” is rarely useful and often remembered.</p>
<h3 class="kh">What to say</h3>
<ul class="fears"><li>One specific, constructive point.</li><li>Specific thanks.</li><li>Serious concerns through the proper route, before you go.</li><li>Nothing you'd mind being quoted.</li></ul>
<h3 class="kh">Three kinds of leaver</h3>
<div class="breeds">
<div><b>The Graceful Leaver</b><p>One point, specific thanks. Remembered well.</p></div>
<div><b>The Crater Leaver</b><p>Everything, angrily. Remembered for that.</p></div>
<div><b>The Silent Leaver</b><p>Nothing at all. Safe, but leaves nothing for those who stay.</p></div>
</div>
{note("If you're leaving because of harassment or discrimination, raise it formally before you leave, with advice, not just in the exit interview.")}""",
        difficulty=dict(
            normal=dict(who="A happy-enough leaving.",
                        know=["You're leaving for something better.", "Few grievances.", "Good relationships."],
                        do=["Make one useful point.", "Thank people specifically.", "Hand over well."],
                        avoid="The pointless lie.",
                        next="If you're leaving because of problems, you're at Nightmare."),
            nightmare=dict(who="Leaving with a list.",
                           know=["Many grievances.", "Some are serious, most aren't.", "You're tempted to say it all."],
                           do=["Choose the one most useful point.", "Write the full list for a friend.", "Stay calm and factual.", "Keep your references in mind."],
                           avoid="The scorched earth.",
                           next="If something serious happened, you're at Hell."),
            hell=dict(who="Leaving because of something serious.",
                      know=["Harassment, discrimination or wrongdoing.", "You're leaving because of it.", "Others may still be affected."],
                      do=["Raise it formally before you leave.", "Get independent advice.", "Keep records.", "Use the exit interview to confirm it was raised."],
                      avoid="Naming names angrily.",
                      next="See HR's True Allegiance and the Whistle of Last Resort."),
        ),
        mirror=dict(
            title="Will you leave a door or a crater?",
            intro="Tick honestly.",
            signs=["You have a mental list of everything you'll say when you leave.", "You've imagined the exit interview as revenge.",
                   "You haven't raised serious problems because “I'll say it when I go”.", "You don't know who'd give you a reference.",
                   "You've never thanked your manager specifically."],
            cure="Raise the serious things now, properly. Save the exit interview for one useful point and a real thank-you.",
        ),
        rehearsal=dict(
            title="Scene: Monday 24 November 2030, Rafi's exit interview.",
            intro="The One Useful Thing, and the Gracious Close.",
            lines=[
                ("HR", "Why are you leaving, and what could we do better?"),
                ("Rafi", "A great opportunity. And one thing: we rebuilt our roadmap three times in a year. Stable priorities would help everyone who stays."),
                ("HR", "That's useful. Thank you."),
                ("Rafi", "And I'd like to thank Ruth and Pip specifically. The heatwave write-up and the Data Office role changed my career."),
                ("HR", "Anything else?"),
                ("Rafi", "No, thank you. I've learned a lot here."),
            ],
            note="Item 24 on the list, added later at the pub: “The biscuits at Thursday procurement meetings are excellent.” This is not about MetroVolt.",
        ),
    ),
    # ------------------------------------------------------------------ Life After the Dungeon
    "life-after-dungeon": dict(
        sighting=f"""{beat("March 2030 · the decision")}
<p>The Chronicler booked a meeting with HR called “Retirement: options”. Twenty-two years at MetroVolt, eight reorgs,
four transformations, two return-to-office decrees and one notebook, begun in 2008, of everything they'd learned about
surviving it. They chose a date: <b>31 January 2031</b>. They told Ruth in April, nine months ahead, “so the handover can
be boring”.</p>
{beat("Autumn 2030 · the Good Ending")}
<p>They documented everything, trained two people, and said thank you, specifically, to forty-one colleagues. They left
every Slack channel but three. They unpacked the go-bag from Act V: the CV went in the recycling, the five names became
five coffees, the six months' savings in the pink pig became a train ticket to somewhere warm.</p>
{beat("Thursday 30 January 2031 · the boomerang")}
<p>At the leaving drinks was Marcus, made redundant in Act V in 2027, back since September 2030 as a contractor on Ascend's
data work. Better paid, three days a week, and visibly happier. “Best thing that ever happened to me,” he said, “though I
wouldn't have said so in room 4B.” Boomerangs, the Chronicler observed, need a runway, and Marcus had left one.</p>
{beat("Friday 31 January · the last day")}
<p>At the turnstile, the Chronicler handed in their badge. Then they handed Pip a battered notebook. On the first page, in
2008 handwriting: <i>“Rule 1: the org chart lies.”</i> On the last page, in fresh ink: <i>“Rule 96: the dungeon was never the
whole world.”</i> And beneath it: <i>“Your turn. Keep it honest. Keep it kind. Keep it funny.”</i></p>
{beat("Monday 3 February 2031 · the first Monday after")}
<p>The Chronicler was on an allotment in the rain, very happy. Pip, at his desk on floor 14, opened the notebook to a
fresh page, and began a new line.</p>
{note("The dungeon was never the whole world. Leave well, keep your people, and walk out into the daylight.")}""",
        origin=dict(
            title="How the Chronicler came to keep the grimoire",
            beats=[
                ("2008 · the first page", "In their first month at MetroVolt, the Chronicler watches someone brilliant get sidelined by someone political. They write it down: Rule 1."),
                ("2008–2026 · the notes", "Every reorg, every creature, every lord: written down, with what worked. A survival guide for an audience of one."),
                ("2026–2030 · the apprentice", "Pip arrives. The Chronicler sees themselves in him, and starts sharing the notes. The Annotator adds the margins."),
                ("2031 · the handing over", "The notes become this grimoire. The badge goes back. The book goes on."),
            ],
            turning="One person deciding, in 2008, to write down what they learned, for no reason except that someone might need it.",
            saved="Nothing needed saving. This is the ending: someone leaves well, and leaves something behind.",
            note="Everyone leaves eventually. The question is what you leave: a crater, a door, or a book.",
        ),
        know=f"""<p>Everyone leaves a job eventually: by choice, by retirement, by redundancy. How you leave shapes your reputation,
your relationships, and sometimes whether you can come back. And for people whose job has become their whole identity,
leaving can feel like losing themselves. The answer is to build a self outside work long before you need it.</p>
<h3 class="kh">Leaving well</h3>
<p>Good notice, a clean handover, specific thanks, and no burnt bridges.</p>
<h3 class="kh">The boomerang</h3>
<p>Many people return to former employers, often in better roles. It only works if you left a runway.</p>
<h3 class="kh">The unbadged self</h3>
<ul class="fears"><li>People who know you outside work.</li><li>Interests that aren't your job.</li><li>A sense of purpose that doesn't need a title.</li><li>Rest, without guilt.</li></ul>
<h3 class="kh">Three kinds of leaving</h3>
<div class="breeds">
<div><b>The Chosen Leaving</b><p>Resignation or retirement. Do the Good Ending.</p></div>
<div><b>The Forced Leaving</b><p>Redundancy or dismissal. Read Act V; leave with dignity anyway.</p></div>
<div><b>The Returning</b><p>The boomerang. Go back only if something real has changed.</p></div>
</div>
{note("You are not your job title. You are the person who did the job, and will do the next thing, and has a life beyond both.")}""",
        difficulty=dict(
            normal=dict(who="The Chosen Leaving.",
                        know=["You're leaving on your terms.", "Relationships are good.", "You have something next."],
                        do=["Give generous notice.", "Hand over properly.", "Say thank you, specifically."],
                        avoid="The ghost haunting.",
                        next="If leaving makes you feel lost, you're at Nightmare."),
            nightmare=dict(who="The lost leaving.",
                           know=["Your job was your identity.", "You don't know who you are without it.", "The first Monday after feels empty."],
                           do=["Build routines outside work.", "Keep the fellowship.", "Try things you never had time for.", "Be patient with yourself."],
                           avoid="The badge identity.",
                           next="If you were forced out, you're at Hell."),
            hell=dict(who="The Forced Leaving.",
                      know=["Redundancy or dismissal.", "It wasn't your choice.", "You're angry or ashamed."],
                      do=["Read Act V's Go-Bag Scroll.", "Leave with dignity; it protects you.", "Get advice on your rights.", "Remember Marcus."],
                      avoid="The burnt bridge.",
                      next="Many people say, later, it was the best thing that happened. You don't have to believe that yet."),
        ),
        mirror=dict(
            title="Who are you without the badge?",
            intro="The last mirror in the grimoire. Tick honestly.",
            signs=["You describe yourself mainly by your job.", "You can't imagine a month without work.",
                   "Most of your friends are colleagues.", "You've no interests that aren't connected to work.",
                   "You've been planning to leave for years but can't picture after."],
            cure="This month, do one thing that has nothing to do with your job, with someone who has nothing to do with your job. It's the first page of your next chapter.",
        ),
        rehearsal=dict(
            title="Scene: Friday 31 January 2031, 17:30, the turnstile.",
            intro="The Good Ending.",
            lines=[
                ("The Chronicler", "Badge. Twenty-two years. It's lighter than I thought."),
                ("Pip", "What will you do on Monday?"),
                ("The Chronicler", "Allotment. Rain, probably. I'm looking forward to it."),
                ("The Chronicler", "And this is yours now. Begun in 2008. Ninety-six rules."),
                ("Pip", "…I can't take this."),
                ("The Chronicler", "You've been writing in the margins for years. Keep it honest. Keep it kind. Keep it funny."),
            ],
            note="This is the end of the grimoire, and the beginning of Pip's. The doors opened. It was raining. The Chronicler didn't mind at all.",
        ),
    ),
}
