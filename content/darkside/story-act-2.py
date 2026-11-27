# Series 4 · Act II · the long-form story fields (format v2), merged into content/darkside/act-2.py by scripts/grimoire.py.
# Per entry: sighting (time-stamped beats), origin, know (thy enemy), difficulty (three levels), mirror, rehearsal.
# `note(text)` (the Annotator) is injected by the loader. Raw HTML.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the Credit Vampire
    "credit-vampire": dict(
        sighting=f"""<p class="beat"><span>Monday 24 February · 21:40</span></p>
<p>It started, as these things do, with a good piece of work. For eleven evenings Pip stayed late on floor 9, rebuilding the
<b>Q3 load forecast</b> from the raw meter data. He found a flaw in the old model (it ignored air-conditioning
in new-build flats), fixed it, and tested it against three past heatwaves. On the last night the model predicted the
2025 peak to within 2%. Pip sat alone under one buzzing light and allowed himself a small, private “yes”.</p>
<p class="beat"><span>Tuesday 25 February · 09:12</span></p>
<p>Dorian from Strategy appeared at Pip's desk with two coffees, which should have been the first warning. “I hear
you've built something special,” he said. “Send it over? I'll take it from here, get it in front of the right
people.” Pip, flattered, sent it. Dorian replied with a thumbs-up and the words <i>“legend, leave it with me”</i>.</p>
<p class="beat"><span>Tuesday 4 March · 10:02 · the atrium all-hands</span></p>
<p>Four hundred people, one big screen. Slide 7: <i>“Q3 forecast: Dorian's model.”</i> Dorian spoke beautifully
about “a fresh approach to air-conditioning load in new-build housing”. The fresh approach was Pip's. Pip's name
appeared nowhere: not in the title, not in the footer, not even in the font. Lord Varnish called it “exactly
the kind of initiative we need”. Dorian looked humble. Pip clapped, because everyone was clapping, then went to
the bathroom on floor 9 and stared at the hand dryer for some time.</p>
<p class="beat"><span>Tuesday 4 March · 14:30</span></p>
<p>Pip found Dorian by the lifts and said, carefully, that it would have been nice to be mentioned. Dorian looked
genuinely hurt. “Pip, we're one team. I said ‘we’ at least twice.” He had. Pip walked away feeling he had somehow
been the rude one. In June, it happened again, with the substation model.</p>
{note("Notice the pattern: the coffee, the “I'll take it from here”, the meeting you're not invited to, and the hurt face when you mention it. That's not one bad day. That's a feeding cycle.")}""",
        know=f"""<p>The Vampire is rarely evil. It is <b>hungry</b>. It lives where work is invisible and only the
presenter is seen. Feed it darkness and it grows fat. Sunlight kills it.</p>
<h3 class="kh">What it wants</h3>
<p>Visibility. A promotion case. The feeling of being the one with the good ideas. Most Vampires are under pressure
to look impressive to their own bosses, and your work is the quickest way to get there.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because the organisation lets it. In most companies, <b>the person who presents gets the credit by default</b>.
Leaders see slides, not spreadsheets, and nobody checks the history of a deck. Phrases like “great work, team”
blur who did what, and the people who build things are often busy building things instead of presenting them.
A Vampire doesn't even need to lie. It only needs your work to stay in the dark until it can carry it into a room
you're not in.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Your name on the work before it travels.</li><li>You in the room when the work is presented.</li>
<li>Detailed questions about the method, in public.</li><li>Written records with dates on them.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Careless</b><p>Forgot to mention you. Mortified when told. Fixes it at once. Most common breed.</p></div>
<div><b>The Opportunist</b><p>Takes credit when it's easy and safe. Backs off when you're visible. Needs daylight, not war.</p></div>
<div><b>The Feeder</b><p>Does it systematically, and hurt-faces you when challenged. Needs records, allies and, eventually, your manager.</p></div>
</div>
{note("“Sunlight” means other people knowing what you did, before the meeting. Not literal sun. HR has asked me to stop saying this.")}""",
        difficulty=dict(
            normal=dict(
                who="The Careless. A peer who forgot to mention you, once.",
                know=["It's the first time.", "They're new, rushed or junior.", "When you mention it, they're embarrassed, not defensive."],
                do=["Assume good intent and have a quick, friendly word in private.",
                    "Ask for a specific fix: “Could you add my name on slide 7 before it goes out?”",
                    "From now on, cast the Dawn Ward on anything you hand over."],
                avoid="Making a big thing of it. Careless people become allies when treated kindly.",
                next="If it happens again with the same person, you're at Nightmare."),
            nightmare=dict(
                who="The Opportunist. A habit: it happens every quarter, with you or with others.",
                know=["It's the second or third time.", "You're never invited to the meetings where your work appears.",
                      "Others have quietly told you the same thing happened to them."],
                do=["Cast the Dawn Ward every single time: your name and your manager in daylight before the work travels.",
                    "Keep the Weekly Deeds Scroll so your manager knows what you built.",
                    "Ask to present the part you built (the Invitation Hex).",
                    "Raise the pattern calmly with your manager, with dates, not adjectives."],
                avoid="Confronting them in public, or recruiting the others into a whisper campaign.",
                next="If your manager rewards it or does it too, you're at Hell."),
            hell=dict(
                who="The Feeder, protected. Or worse: it's your own manager (see Act III, the Credit-Taking Crown).",
                know=["The culture rewards it: presenters rise, builders don't.", "Your manager is the Vampire, or protects one.",
                      "Your work has disappeared from your review."],
                do=["Keep a private, dated record of what you built and where it went.",
                    "Build a direct relationship with your skip-level and with the people who use your work.",
                    "Put your name in every artefact, every time, without comment.",
                    "Decide how long you're willing to feed it (Act III, the Escape Portal)."],
                avoid="Sabotage, or going quiet. Both make you smaller; neither makes them smaller.",
                next="If it's affecting your pay or promotion, raise it formally with HR, with your record."),
        ),
        origin=dict(
            title="How a junior analyst became the Credit Vampire",
            beats=[
                ("2017 · floor 4, Grid Planning", "Dorian is 24, a junior analyst, and good at it. In his own time he builds MetroVolt's first proper winter-peak model. It's clever. He's proud of it. He shows his mum."),
                ("March 2018 · the leadership off-site", "His manager, Clive, presents it to the board as <i>“my winter model”</i>. Dorian isn't invited. He hears about it in the lift. He goes to the bathroom on floor 4 and stares at the hand dryer for some time."),
                ("Autumn 2018 · Clive's promotion drinks", "Clive becomes Head of Department. In his speech he thanks “the whole team”. Dorian, holding a warm prosecco, learns the only lesson MetroVolt has taught him so far: <b>the person who presents is the person who rises</b>."),
                ("2020 · a move to Strategy", "Dorian moves to a team that builds nothing and presents everything. He is extremely good at it. Two promotions in three years. Nobody asks where the slides come from."),
                ("2025 · the hunger", "Dorian hasn't built a model in six years. Lord Varnish wants “fresh thinking” every quarter. Dorian has none left of his own. The juniors on floor 9 do. He starts buying two coffees."),
            ],
            turning="The day he stopped building and started carrying. Nobody punished it. Everybody rewarded it.",
            saved="One sentence from Clive in 2018 (“Dorian built this”) might have done it. So might a company that celebrated builders as loudly as presenters. And it's not too late: Vampires who are named generously in daylight sometimes start naming others.",
            note="Every Vampire was once bitten. That explains them. It doesn't excuse them. Both are true, and you need both to deal with one.",
        ),
        mirror=dict(
            intro="Before you hunt a Vampire, check your own teeth. Tick honestly.",
            signs=["You've said “I” in a presentation about work that three people did.",
                   "You've forwarded someone's analysis upwards without their name on it.",
                   "You describe your team's results as “my” results in your review.",
                   "You've ever said “I'll take it from here” and meant it.",
                   "You can't name who built the last thing you presented."],
            cure="Name names. In every update, every deck, every review: who built it, specifically. It costs nothing, it makes you look like a leader, and it makes people want to work with you.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday, 09:12. Pip's desk. Dorian arrives with two coffees.",
            intro="The counter-spells, said out loud. Read it once, then practise it with a friend. The words matter less than the calm.",
            lines=[
                ("Dorian", "I hear you've built something special. Send it over? I'll take it from here."),
                ("", "Pip takes the coffee. Smiles. Does not open his laptop."),
                ("Pip", "Thanks! It's nearly ready. I'm sending it to Marcus and the Ops leads this afternoon, so everyone has the same version."),
                ("Dorian", "Great, great. I could present it on the 4th, save you the hassle?"),
                ("Pip", "That'd be brilliant, a bigger stage. Could I take the five minutes on the method? It'll save you the detailed questions."),
                ("Dorian", "…Sure. Of course. One team."),
                ("Pip", "One team. I'll put us both on the cover slide."),
                ("", "That afternoon, the file arrives in four inboxes as Q3-load-forecast_Pip_v4.xlsx. The Dawn Ward is cast. Nobody had to be rude."),
            ],
            note="Notice what Pip never says: “you're trying to steal my work”. He doesn't need to. Daylight does it for him.",
        ),
    ),
    # ------------------------------------------------------------------ the Meeting Lich
    "meeting-lich": dict(
        sighting=f"""{beat("Week 2 · Tuesday 10:00 · room 27B")}
<p>Pip was invited to the <b>Weekly Sync on the Syncs</b> “for visibility”. Twelve people, ninety minutes. Gerald,
Director of Alignment, opened with a slide titled <i>Alignment Status (Aligned)</i>. Four leads then reported, one by
one, what had been said in their own weekly meetings. Nobody decided anything. Gerald thanked everyone for their
alignment.</p>
{beat("Week 4 · 11:28")}
<p>Two leads disagreed about a data definition. “Let's take that offline,” said Gerald. At 12:41 a new invite
arrived: <i>Sync Prep (recurring)</i>, Mondays, 45 minutes, to “prepare the alignment points for Tuesday”.</p>
{beat("Week 6 · a calendar invite")}
<p>Pip was made owner of <i>Actions Alignment</i>, a follow-up to track the actions from the sync and the prep.
He now spent four hours a week in meetings about one spreadsheet. The spreadsheet had nine rows. Seven said
“to be aligned”.</p>
{beat("Week 9 · the archive")}
<p>Out of curiosity, Pip searched the notes of all 112 meetings for the word “decided”. It appeared once, in 2024:
the meeting had decided to move itself from Monday to Tuesday.</p>
{note("A Lich doesn't die. It reproduces. Sync, Sync Prep, Actions Alignment: that's three generations in seven weeks. Count your recurring invites. Some of them are grandchildren.")}""",
        origin=dict(
            title="How a project manager became the Meeting Lich",
            beats=[
                ("2019 · the billing migration", "Gerald is a capable project manager on MetroVolt's first billing migration. It fails. The post-mortem finds that four teams never knew what the others were doing. Its one recommendation: <i>“more alignment”</i>."),
                ("2021 · a new title", "Leadership creates a role to deliver the recommendation: Director of Alignment. It comes with no budget, no team and no decision rights. It comes with a calendar."),
                ("2022 · the only tool", "Gerald can't decide anything, fund anything or stop anything. He can invite people. So he does. Meetings become the only proof that alignment is happening, and that Gerald exists."),
                ("2024 · the VP visits", "Lord Varnish attends one sync and says “this is valuable”. From then on, cancelling it would be cancelling the VP's opinion. The Lich becomes immortal."),
            ],
            turning="The moment “more communication” was turned into “more meetings”, and a man was given a title instead of a tool.",
            saved="A written decision log instead of a sync. Or the authority to decide things, which would have made most of the meetings unnecessary.",
            note="Most Liches were good project managers once. They were given responsibility without power, and a calendar was all they had left.",
        ),
        know=f"""<p>A Lich is a meeting that has lost its soul (its purpose) but keeps walking. Behind most Liches is a person
who needs the meeting more than the meeting needs them.</p>
<h3 class="kh">What it wants</h3>
<p>To feel informed and in control, and to have visible proof of being useful. A full calendar looks like a full job.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Meetings are free to create and expensive to kill. Nobody wants to cancel the thing a VP once attended. Calendars are
public, so busyness is easy to show and output is not. And “let's take it offline” sounds like efficiency while
creating another meeting.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>The question “what do you need me to decide?”</li><li>Written updates that make the meeting unnecessary.</li>
<li>Someone asking what was decided last week.</li><li>Empty chairs.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Drifter</b><p>A meeting that once had a purpose and lost it. Usually happy to be shortened.</p></div>
<div><b>The Hoarder</b><p>Collects meetings as proof of importance. Needs a better way to feel useful.</p></div>
<div><b>The Necromancer</b><p>Revives cancelled meetings after every crisis. Needs a lighter alternative ready.</p></div>
</div>
{note("Do the maths out loud once. Twelve people, ninety minutes, weekly: 936 hours a year. At MetroVolt's rate for a field engineer, the Sync costs about £80,000. It has decided one thing.")}""",
        difficulty=dict(
            normal=dict(who="The Drifter. One meeting that has lost its way.",
                        know=["It used to be useful.", "The organiser seems a bit bored too.", "Nobody objects when you suggest a shorter slot."],
                        do=["Ask what decision the meeting needs from you.", "Suggest a written update plus a 15-minute slot for decisions only.", "Offer to write the decisions down at the end."],
                        avoid="Silently skipping it. Ask, and you'll usually be thanked.",
                        next="If the meeting spawns new meetings when challenged, you're at Nightmare."),
            nightmare=dict(who="The Hoarder. A meeting culture: your week is mostly recurring invites.",
                           know=["More than half your week is recurring meetings.", "New meetings appear to discuss old meetings.", "Your work happens after 17:00."],
                           do=["Audit your calendar: keep, shorten, replace with writing, decline.", "Agree with your manager which meetings you truly own.", "Use the Decline With Grace and always send your update in writing.", "Protect two focus blocks a week, visibly."],
                           avoid="Declining everything at once. Change one meeting a week; it's less threatening.",
                           next="If attendance is how leadership measures commitment, you're at Hell."),
            hell=dict(who="The Necromancer, blessed by leadership. Attendance is loyalty.",
                      know=["Absences are noticed and mentioned.", "A VP owns or attends the meetings.", "Proposals to cut meetings are seen as disloyalty."],
                      do=["Pick your battles: attend the ones senior people watch, decline the rest.", "Make your written updates excellent, so your absence looks efficient.", "Bring the cost (hours, euros) to someone who controls budgets.", "Protect your health: no meetings after 17:00."],
                      avoid="Laptop necromancy: attending in body and working on something else. It's worse than not attending.",
                      next="If you can't do your actual job any more, raise it with your manager as a workload problem, with numbers."),
        ),
        mirror=dict(
            intro="Before you hunt a Lich, check your own calendar. Tick honestly.",
            signs=["You own a recurring meeting that has no agenda.", "You've scheduled a meeting to avoid writing an email.", "You can't name last week's decision in your own team meeting.",
                   "You invite people “for visibility”.", "Your meetings always use the full time, never less."],
            cure="Put a decision line at the top of every meeting you own, end early when it's done, and cancel one recurring meeting this month. Nobody will notice except to thank you.",
        ),
        rehearsal=dict(
            title="Scene: Monday 14:02. A calendar invite. Pip replies to Gerald.",
            intro="The Agenda Rune and the Written Offering, said out loud. Warm, short, useful.",
            lines=[
                ("Gerald", "Pip! Added you to Sync Prep, Mondays. Great for visibility."),
                ("Pip", "Thanks Gerald, kind of you. What do you need me to decide or bring each week? Then I can prepare properly."),
                ("Gerald", "Oh, just updates, really. Stay aligned."),
                ("Pip", "In that case, could I send you my update in writing every Monday by 10? Three lines. You'd have it before the meeting, and I'd get two hours back for the forecast."),
                ("Gerald", "…I suppose that would work."),
                ("Pip", "And if there's ever a decision that needs me, send it my way and I'll answer the same day."),
                ("", "Monday 09:54: three lines arrive in Gerald's inbox. Gerald forwards them to the sync as an example of “excellent alignment”."),
            ],
            note="The trick isn't refusing the meeting. It's giving the Lich what it actually wants (to feel informed) in a cheaper form.",
        ),
    ),
    # ------------------------------------------------------------------ the Gaslight Wraith
    "gaslight-wraith": dict(
        sighting=f"""{beat("Wednesday 9 April · 08:47 · the lift to floor 12")}
<p>Rhona, project lead on Lumen, stepped into the lift with a coffee and a decision. “Pause the substation analysis,”
she said, between floors 4 and 9. “All hands on Lumen meter data until the end of April.” Pip nodded. The doors opened.
That was the whole meeting.</p>
{beat("Thursday 10 to Tuesday 22 April")}
<p>Pip did exactly as told. He moved two weeks of work to meter data and put the substation analysis on hold. He
mentioned it to nobody, because it had come from the project lead, in person, and that felt official enough.</p>
{beat("Wednesday 23 April · 14:10 · the Lumen review, nine people")}
<p>“Why is the substation analysis late?” asked Rhona. Pip said she'd asked him to pause it. Rhona looked genuinely
puzzled. “I never said to pause it. I'd never say that, it's on the critical path.” Nine people looked at Pip. Pip
opened his mouth and found nothing in it but the memory of a lift, and a lift is not evidence.</p>
{beat("That evening")}
<p>Pip lay awake wondering whether he had made the whole thing up. He hadn't. But for a few hours, he believed he might
have, and that was the worst part.</p>
{note("If someone repeatedly denies things you both know happened and you start doubting your own memory, that is not a quirk. Keep notes, tell someone you trust, and read the Hell level below.")}""",
        origin=dict(
            title="How a careful project lead became the Gaslight Wraith",
            beats=[
                ("2016 · her first big project", "Rhona's director tells her, in a corridor, to cut a testing phase to save time. The system fails at launch. At the review, the director says he'd never have approved that. Rhona carries the blame and a written warning."),
                ("2016 · the lesson", "Rhona learns that a spoken instruction protects the person who gave it, never the person who followed it. She decides she will never again be on record for a risky call."),
                ("2019 to 2024 · the habit", "She gives instructions in lifts, corridors and calls. Never in email. Never in the decision log. It isn't malicious. It's armour."),
                ("2025 · Lumen", "Under regulator pressure, Rhona changes her mind often, and remembers each new plan as the one she always had. Memory, under stress, rewrites itself in your favour. She sincerely believes she never said “pause”."),
            ],
            turning="The day she was blamed for her director's spoken order, and decided to become the person who never gets blamed.",
            saved="A director who owned his words in 2016. Or a project culture where every decision goes in a shared log, so nobody needs armour.",
            note="The Wraith is often a former victim of a Wraith. That's why the cure is paper, not punishment: paper protects both of you.",
        ),
        know=f"""<p>Some Wraiths do it on purpose, to dodge blame. Most don't: they change their minds, forget, and then
<b>sincerely</b> remember the version where they were right. It doesn't matter which kind you face. The cure is the same:
<b>a shared written record</b>, made at the time, that both of you saw. The Wraith is a creature of fog. Paper does not fog.</p>
<h3 class="kh">What it wants</h3>
<p>To be safe from blame, and to keep the freedom to change its mind without admitting it.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because big decisions at MetroVolt are often made in lifts and corridors, and nobody writes them down. Under deadline
pressure, plans change daily and memories change with them. And people rarely challenge a senior person's memory in
public, so the Wraith's version wins by default.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>A recap email sent within the hour.</li><li>A shared decision log.</li><li>Witnesses.</li><li>Calm, curious questions in front of others.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Forgetful</b><p>Genuinely doesn't remember. Grateful for recaps. Most common breed.</p></div>
<div><b>The Shifter</b><p>Rewrites history under pressure. Needs the shared log, every time.</p></div>
<div><b>The Deliberate</b><p>Denies on purpose to dodge blame. Needs records, witnesses and your manager.</p></div>
</div>
{note("“Gaslighting” is a strong word, and most forgetful colleagues aren't doing it. But the counter-spell is identical, so you don't need to decide which it is. Just write it down.")}""",
        difficulty=dict(
            normal=dict(who="The Forgetful. A busy colleague who genuinely forgets.",
                        know=["It's happened once or twice.", "When shown a note, they say “oh, right, sorry”.", "They're overloaded, not defensive."],
                        do=["Send a friendly recap within the hour of any spoken instruction.", "Ask them to correct it if you've misunderstood.", "Keep recaps short and warm, never accusing."],
                        avoid="Treating a forgetful person as a liar. You'll create an enemy where you had a busy colleague.",
                        next="If they deny things even after your recap, you're at Nightmare."),
            nightmare=dict(who="The Shifter. History gets rewritten whenever something slips.",
                           know=["Denials come when there's blame to hand out.", "Your recaps go unanswered, then are disputed later.", "Colleagues say “oh, she does that”."],
                           do=["Recap everything, and put decisions in the shared project log, not just your inbox.", "Ask for important instructions in writing: “Could you drop that in the log so the team sees it?”", "When it happens, show the record calmly and move to deciding what's next.", "Raise the pattern with your manager, with dates."],
                           avoid="The gotcha reply-all. You win the argument and lose every future conversation.",
                           next="If it's deliberate, targeted at you, and affecting your review, you're at Hell."),
            hell=dict(who="The Deliberate. Denial is a weapon, and it's making you doubt yourself.",
                      know=["You've started doubting your own memory.", "It's affecting your reputation or review.", "It happens to you more than to others."],
                      do=["Keep a private, dated log alongside the recaps.", "Talk to someone you trust outside the situation.", "Take it to your manager's manager or HR, with the record.", "Look after yourself: this is wearing, and it isn't your fault."],
                      avoid="Secret recordings. In many places they're illegal, and everywhere they turn you into the story.",
                      next="If the organisation won't act, protect your health and plan your exit (Act III, the Escape Portal)."),
        ),
        mirror=dict(
            intro="Before you hunt a Wraith, check your own memory. Tick honestly.",
            signs=["You give important instructions only out loud.", "You've said “that's not what I meant” more than once this month.", "You avoid putting your decisions in writing.",
                   "You've been surprised by a recap of something you said.", "You remember your own past decisions as better than they were."],
            cure="Write your own decisions down, in the shared place, as you make them. When you change your mind, say so: “I've changed my mind” is a strength, not an admission.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 23 April, 14:10. The Lumen review. Rhona has just denied it.",
            intro="The Gentle Mirror: show the record without a fight, then move the room forward.",
            lines=[
                ("Rhona", "I never said to pause it. I'd never say that, it's on the critical path."),
                ("Pip", "I may have misread it. My recap from the 9th says pause until the 30th. I'll forward it now so we're all looking at the same thing."),
                ("", "Pip forwards the email. Nine people glance at their laptops. Rhona reads it."),
                ("Rhona", "Well. That's not quite what I meant."),
                ("Pip", "Understood. Shall we decide now which comes first, so I can get the substation work back on track this week?"),
                ("Rhona", "…Substation first. Meter data can wait a week."),
                ("Pip", "Great. I'll put that in the decision log, item 15, so it's clear for everyone."),
            ],
            note="Pip never says “you're lying”. He doesn't need to. The recap does the talking, and the meeting moves on with the decision written down.",
        ),
    ),
    # ------------------------------------------------------------------ the Bulldozer Ogre
    "bulldozer-ogre": dict(
        sighting=f"""{beat("Wednesday 14 May · 10:00 · the Lumen pricing workshop")}
<p>Eight people, one whiteboard, a question: how should off-peak pricing work for smart-meter customers? Pip had spent
two days on the off-peak data. He had a chart. He was ready.</p>
{beat("10:04 to 10:15")}
<p>Brett from Commercial interrupted Pip four times in eleven minutes. Each time Pip got as far as “I think the off-peak
data shows—” before Brett said “Right, so what I'm hearing is,” and then described an idea that was not what he was
hearing at all. On the fifth attempt Pip stopped trying.</p>
{beat("10:15 to 11:30")}
<p>Brett drew his plan on the whiteboard in red, then in blue, then in red again for emphasis. Two engineers stopped
taking notes. A data scientist who had joined from Customer Ops turned her camera off. Someone said “good energy”.</p>
{beat("11:31")}
<p>The workshop produced Brett's plan. Six people left with ideas they never said out loud. One of them (Pip's off-peak
chart) would have saved Lumen £300,000 a year. It stayed in his laptop until October.</p>
{note("Interrupting is a habit, not a character. Habits respond to friction. Add friction.")}""",
        origin=dict(
            title="How a keen salesman became the Bulldozer Ogre",
            beats=[
                ("1990s · the youngest of five", "At Brett's family dinners, you talked loud and fast or you didn't get heard. He got very good at it."),
                ("2012 · a sales floor", "Brett joins a sales team where the loudest pitch wins the client. He wins a lot. Nobody ever asks what the quiet people would have said."),
                ("2022 · the promotion review", "Brett is promoted to lead Commercial at MetroVolt. His review praises his “executive presence” and “gravitas in meetings”. It means he talks over people. Nobody says so."),
                ("2025 · the workshops", "Brett runs workshops the way he ran dinners: whoever is loudest wins. He genuinely believes he's facilitating. Nobody has ever told him otherwise."),
            ],
            turning="The review that called interrupting “presence”, and turned a habit into a strength he was paid for.",
            saved="One honest piece of feedback (“you cut people off, and we lose their ideas”), from someone he respected, at any point in twenty years.",
            note="Most Ogres have never been told. They think the silence around them means agreement. It means surrender.",
        ),
        know=f"""<p>The Ogre is often not trying to dominate. It thinks out loud, fast, and confuses <b>volume with
contribution</b>. It was probably rewarded for it: in many offices the confident talker gets promoted, and the quiet
expert gets “needs to speak up more” in their review.</p>
<h3 class="kh">What it wants</h3>
<p>To be heard, to move fast, and to win. Most Ogres also want good ideas; they just don't notice they're flattening them.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because open discussion rewards the loudest voice, and most meetings at MetroVolt are open discussion. Confidence
looks like competence from the top table. And quiet people rarely complain; they simply stop coming.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Structure: rounds, timers, silent writing.</li><li>Being interrupted, calmly, by name.</li><li>Ideas written down before the meeting.</li><li>A facilitator who isn't them.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Enthusiast</b><p>Thinks out loud and gets carried away. Mortified when it's pointed out kindly.</p></div>
<div><b>The Dominator</b><p>Wants to win the room. Needs structure and a firm chair.</p></div>
<div><b>The Anxious Talker</b><p>Fills every silence because silence frightens them. Needs a calmer room.</p></div>
</div>
{note("You don't have to be louder. You have to be harder to interrupt, and to run meetings where volume doesn't count.")}""",
        difficulty=dict(
            normal=dict(who="The Enthusiast. A keen talker who gets carried away.",
                        know=["They interrupt everyone, not just you.", "They're friendly and well-meaning.", "When told, they apologise."],
                        do=["Hold your ground by name: “Brett, let me finish, then I want your view.”", "Have a quiet, friendly word afterwards.", "Put your key point in writing before the next meeting."],
                        avoid="Out-shouting them. Two Ogres make a nature documentary, not a meeting.",
                        next="If they run the room and keep steamrolling, you're at Nightmare."),
            nightmare=dict(who="The Dominator. A senior Ogre who runs the room.",
                           know=["Their plan always wins.", "Quiet people have stopped coming.", "You can't change the meeting format."],
                           do=["Send your idea in writing before the meeting, with your name on it.", "Agree with an ally to hand the floor back to each other.", "Suggest the Meeting Charm (silent writing, rounds) as a “new format to try”.", "Ask the chair for two uninterrupted minutes on your item."],
                           avoid="Sulking into silence. Your review will say “needs to contribute more”.",
                           next="If the Ogre is your manager, you're at Hell."),
            hell=dict(who="The Ogre is your manager, and volume is the culture.",
                      know=["Your manager talks over you in every meeting.", "Promotions go to the loudest.", "Ideas only count if they're shouted."],
                      do=["Put every important idea in writing first.", "Use 1:1s, where volume matters less.", "Find a sponsor who will hand you the floor in big meetings.", "Give your manager the feedback once, privately, with one example."],
                      avoid="Mockery. Eye-rolls are noticed even by people who notice nothing else.",
                      next="If your ideas never make it out, consider a team where they do (Act III, the Escape Portal)."),
        ),
        mirror=dict(
            intro="Before you hunt an Ogre, listen to yourself. Tick honestly.",
            signs=["You often finish other people's sentences.", "Your meetings usually end with your plan.", "You think quiet people simply don't have ideas.",
                   "You've said “what I'm hearing is” and then said your own idea.", "You can't remember the last time you asked the quietest person first."],
            cure="In your next three meetings, speak last. Ask the quietest person first. You'll be astonished by what you've been missing.",
        ),
        rehearsal=dict(
            title="Scene: the next workshop, 10:06. Brett interrupts for the second time.",
            intro="The Held Ground, then the Meeting Charm. Calm, a little louder, by name.",
            lines=[
                ("Pip", "I think the off-peak data shows that—"),
                ("Brett", "Right, so what I'm hearing is—"),
                ("Pip", "Brett, let me finish this point, then I really want your view."),
                ("", "A pause. Brett blinks. Nobody has done this before."),
                ("Pip", "The off-peak data shows a 14% shift is possible with a two-tier price. That's the chart on page 3 of what I sent yesterday."),
                ("Brett", "…OK. Interesting. What's the catch?"),
                ("Pip", "Good question. Could we go round the table on that? Two minutes each, then you sum up?"),
                ("", "Six people speak. Brett sums up. The plan on the whiteboard, for the first time, has other people's handwriting on it."),
            ],
            note="Notice the last move: Pip gives the Ogre a role (summing up). Ogres don't need silencing. They need a different job in the room.",
        ),
    ),
    # ------------------------------------------------------------------ the Passive-Aggressive Poltergeist
    "passive-aggressive-poltergeist": dict(
        sighting=f"""{beat("Monday 2 June · 08:55")}
<p>The booking system was down, so Pip wrote <i>Pip · 9:30 · forecast review</i> on the paper sign outside meeting room
14B and went to get a coffee.</p>
{beat("09:04 · an email")}
<p>From Felicity in Facilities, to Pip, copied to his manager, the floor warden and something called <i>FAC-ALL</i>:
<i>“Hi Pip! 😊 Just a gentle reminder, as per the policy (attached again for convenience), that rooms are booked via the
form. I'm sure it was an oversight! Kind regards, Felicity.”</i> The policy was attached. It was 14 pages long. The smiley
was the worst part. Pip felt it look at him.</p>
{beat("09:20")}
<p>Pip replied to all, explaining that the system had been down. Felicity replied to all: <i>“Thanks Pip! As per
section 4.2, paper bookings aren't valid. Happy to help with any questions! 😊”</i> Pip's manager replied to Pip only:
<i>“just use the form mate”</i>.</p>
{beat("Friday · the kitchen")}
<p>A laminated sign had appeared on the fridge: <b>PLEASE BOOK ROOMS VIA THE FORM. IT'S NOT DIFFICULT. THANK YOU :)</b>.
Pip was nearly sure it was about him. He was right.</p>
{note("“Per my last email” means “read my emails”. “Kind regards” is 20% kind. “Thanks in advance” means you no longer have a choice.")}""",
        origin=dict(
            title="How a helpful facilities officer became the Poltergeist",
            beats=[
                ("2012 · day one", "Felicity joins Facilities. She is cheerful, organised and helpful. In her first week she fixes the heating on floor 6 and nobody says thank you."),
                ("2013 to 2018 · the complaints", "Every cold room, broken lift and missing chair is her fault. People are rude to her face and ruder by email. She is told to stay “customer-friendly” at all times."),
                ("2019 · the review", "Felicity sends one honest email: “I'm frustrated that people keep ignoring the booking system.” Her review marks her down for “tone”. She learns that frustration must never be visible."),
                ("2020 onwards · the leak", "The frustration doesn't go away. It moves into punctuation. Smileys. Policies attached. CCs for “awareness”. Every email is perfectly polite and quietly furious."),
            ],
            turning="The review that punished one honest sentence, and taught her to hide anger inside politeness instead.",
            saved="A manager who let her say “I'm frustrated”. Or colleagues who, once in a while, said “thanks for fixing the heating”.",
            note="Passive aggression is anger that's been told it isn't allowed. Make it allowed to speak plainly, and it often stops needing punctuation.",
        ),
        know=f"""<p>The Poltergeist is angry and has decided it is not allowed to be. So the anger leaks out sideways: through
politeness that bites, CCs that sting, and notes in the kitchen. It usually comes from feeling <b>unheard or
powerless</b>. Email is the one place it's in charge.</p>
<h3 class="kh">What it wants</h3>
<p>To be taken seriously, to have its rules followed, and, underneath, a bit of respect for a thankless job.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt punishes visible frustration and tolerates invisible hostility. Email lets people be cold without
being rude. And copying someone's manager costs one click.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>A friendly face-to-face conversation.</li><li>Replies that ignore the tone and answer the facts.</li><li>Being thanked, sincerely.</li><li>Being asked “what's the real problem?”</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Bottled</b><p>Frustration leaking out. Softens fast when heard in person.</p></div>
<div><b>The Rule-Keeper</b><p>Uses policy as a weapon. Softens when you follow the rule and ask about the reason.</p></div>
<div><b>The Scorekeeper</b><p>Building a paper case against you. Needs calm replies and an early word with your manager.</p></div>
</div>
{note("The tone is their problem. The facts are yours. Answer the facts.")}""",
        difficulty=dict(
            normal=dict(who="The Bottled. A bad day, in text form.",
                        know=["One prickly email, not a pattern.", "It's about a real slip on your side.", "They're friendly in person."],
                        do=["Reply to the content only, cheerfully, sender only.", "Own the slip in one line.", "Say thanks. Mean it."],
                        avoid="Replying in the same tone. It's satisfying for a second and screenshotted forever.",
                        next="If every small slip gets a CC'd email, you're at Nightmare."),
            nightmare=dict(who="The Rule-Keeper. A pattern of CC'd reminders and kitchen signs.",
                           know=["Your manager is copied on small things.", "The emails always cite a policy.", "Other people get them too."],
                           do=["Walk over or call: “Have you got two minutes so I understand the problem?”", "Ask what the rule is protecting, and help fix that.", "Name it once, kindly, in private.", "Tell your manager briefly, so the CCs land on someone who's heard your side."],
                           avoid="Escalation spirals: adding your manager because they added yours.",
                           next="If they're building a case and copying HR, you're at Hell."),
            hell=dict(who="The Scorekeeper. Someone building a paper trail against you.",
                      know=["HR or senior people are copied on trivia.", "Your replies are quoted back at you.", "It's affecting how you're seen."],
                      do=["Keep every reply calm, factual and short.", "Keep your own copies.", "Brief your manager early and in person.", "If it becomes harassment, raise it formally."],
                      avoid="The anonymous counter-sign in the kitchen. You'll become what you're fighting.",
                      next="If your manager won't support you, take it to HR with your copies."),
        ),
        mirror=dict(
            intro="Before you hunt a Poltergeist, read your own sent items. Tick honestly.",
            signs=["You've written “per my last email” this month.", "You copy people's managers on small things.", "You use a smiley when you're annoyed.",
                   "You've left a note somewhere instead of talking to someone.", "You feel better after sending a perfectly polite, perfectly cold email."],
            cure="When you're annoyed, say so, plainly and kindly, to the person, in person: “I'm a bit frustrated about X. Can we sort it?” It's faster, and nobody gets haunted.",
        ),
        rehearsal=dict(
            title="Scene: Monday 09:30. Facilities, floor 2. Pip walks over instead of replying.",
            intro="The Summoning to the Flesh: move it off email, and listen.",
            lines=[
                ("Pip", "Hi Felicity, I got your email. Sorry about 14B, that's on me. Have you got two minutes so I understand the booking problem?"),
                ("Felicity", "Oh! Well. Yes. It's just… people never use the form, and then two teams turn up for one room, and they both shout at me."),
                ("Pip", "That sounds rubbish. The form was down this morning, which is why I used paper. Is there a backup when it's down?"),
                ("Felicity", "…There isn't, actually. I've asked IT twice."),
                ("Pip", "Want me to mention it to our IT partner? They owe me a favour."),
                ("Felicity", "That would be lovely. Thank you. Really."),
                ("", "The kitchen sign comes down on Wednesday. On Friday, Felicity books Pip's room for him before he asks."),
            ],
            note="Most Poltergeists have a real problem underneath the punctuation. Fix the problem, and the haunting stops.",
        ),
    ),
    # ------------------------------------------------------------------ the Coasting Zombie
    "coasting-zombie": dict(
        sighting=f"""{beat("Tuesday 4 March · the Lumen asset clean-up")}
<p>Pip and Neville from Asset Records were each given half of the clean-up: 40,000 meter records to check before the
regulator's audit. Twenty thousand each. Due 30 June. Neville nodded slowly, as if hearing about weather in another country.</p>
{beat("April and May")}
<p>Pip's half went steadily. Neville's status, in every update, was “in progress”. When asked for a number, Neville said
“getting there”. Neville was always busy. Nobody knew with what. He had been in Asset Records for fourteen years and had
survived six reorgs.</p>
{beat("Two weekends in June")}
<p>Pip checked the shared file. Neville's half was at 15%. Pip, afraid of missing the audit, quietly did 8,000 of
Neville's records over two weekends. He told nobody. His girlfriend asked why he was working on a Sunday. He said
“team effort”.</p>
{beat("Thursday 10 July · the review")}
<p>The clean-up was praised as “a real team effort”. Neville nodded wisely. He had, in a sense, been on the team.</p>
{note("Every weekend you spend doing a Zombie's work is a weekend that proves to the company the Zombie isn't a problem.")}""",
        origin=dict(
            title="How an eager engineer became the Coasting Zombie",
            beats=[
                ("2011 · the new joiner", "Neville joins Asset Records full of ideas. In his first year he proposes a proper asset database to replace eleven spreadsheets. Everyone agrees it's a great idea."),
                ("2012 · the first reorg", "The project is cancelled in a reorg before it starts. Neville proposes it again in 2014. Cancelled again. In 2016, a third time. Cancelled again."),
                ("2017 · his mentor leaves", "Neville's mentor, the hardest worker in the department, is made redundant. The people who kept their heads down all stay."),
                ("2018 onwards · the lesson", "Neville concludes that effort changes nothing, ideas get killed and visibility gets you cut. He does just enough. He survives every reorg. Nobody ever asks him why he stopped."),
            ],
            turning="The third time his idea died, and he decided caring was a risk he couldn't afford.",
            saved="One project of his own that survived. Or a manager who noticed the change in 2017 and asked what happened.",
            note="Many Zombies were the keenest person in the building once. Treat the coasting as a symptom. You may not fix it, but you'll stop taking it personally.",
        ),
        know=f"""<p>Some Zombies are lazy. Many are not: they are <b>burnt out, bored, disengaged</b>, or quietly dealing with
something at home. A few have learned that in a big company, work given to “the team” always gets done by someone.
Usually by someone like Pip.</p>
<h3 class="kh">What it wants</h3>
<p>To be left alone, to stay safe, and to get through the week. Often, underneath, to matter again, though it would never say so.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because shared ownership hides individual output. Managers avoid hard conversations (see Act III, the Conflict
Phantom). And conscientious colleagues quietly fill the gaps, so nothing ever visibly fails.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Named owners and dates on a shared board.</li><li>Numbers instead of “in progress”.</li><li>A manager who asks specific questions.</li><li>Colleagues who stop rescuing it.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Burnt-out</b><p>Running on empty. Needs kindness and, often, support from HR or a doctor.</p></div>
<div><b>The Disengaged</b><p>Stopped caring after being let down. Sometimes revived by work they own.</p></div>
<div><b>The Professional Coaster</b><p>Has learned the system. Needs visibility and a manager who acts.</p></div>
</div>
{note("Help openly or not at all. Secret rescue is just unpaid overtime with extra resentment.")}""",
        difficulty=dict(
            normal=dict(who="A colleague who's stuck or overloaded, not coasting.",
                        know=["The slip is recent.", "They seem stressed rather than relaxed.", "When asked, they admit they're stuck."],
                        do=["Check in early, kindly and specifically.", "Offer half an hour to look at the problem together.", "Agree a split of the work on a shared board."],
                        avoid="Judging. You might be talking to someone having the worst year of their life.",
                        next="If “in progress” lasts for months with no numbers, you're at Nightmare."),
            nightmare=dict(who="A known coaster the team works around.",
                           know=["Everyone knows, nobody says.", "Their status never has a number.", "Their work lands on you."],
                           do=["Name owners and dates for every shared task, on a board your manager can see.", "Report status by owner, with numbers.", "Escalate risks to deadlines with options, not complaints.", "Help only openly, and only once agreed."],
                           avoid="The silent martyr. You'll burn out and they'll be praised.",
                           next="If the coaster is protected by someone senior, you're at Hell."),
            hell=dict(who="The protected coaster: friend of the director, untouchable.",
                      know=["Escalations go nowhere.", "The coaster gets credit for shared work.", "You're getting both halves officially."],
                      do=["Keep named owners and dated records for everything shared.", "Never quietly absorb their work.", "Raise the workload problem with numbers, in writing.", "Protect your evenings."],
                      avoid="The Zombie's Path: deciding to coast too. They have fourteen years of relationships. You have eight months.",
                      next="If the workload is harming you, treat it as a wellbeing issue and say so formally."),
        ),
        mirror=dict(
            intro="Before you hunt a Zombie, check your own pulse. Tick honestly.",
            signs=["Your status has said “in progress” for more than a month.", "You're glad when shared work gets done by someone else.", "You've stopped suggesting ideas because they never go anywhere.",
                   "You do exactly enough to avoid attention.", "You can't remember the last piece of work you were proud of."],
            cure="Find one small piece of work you own completely and finish it this month. Coasting usually starts when nothing feels like yours.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 4 March, 15:00. The clean-up kick-off. Pip, Neville and Marcus.",
            intro="The Naming of Owners and the Friendly Check-in, on day one, before anything goes wrong.",
            lines=[
                ("Marcus", "So you two will work together on the clean-up. Great."),
                ("Pip", "Shall we split it on the board now? Neville, records 20,001 to 40,000, done by 30 June. Me, 1 to 20,000. Same date."),
                ("Neville", "…Sure. Fine."),
                ("Pip", "And let's both put a number on the board every Friday, so Marcus can see where we are without asking."),
                ("", "Three weeks later. Neville's number has been 4% for two Fridays."),
                ("Pip", "Neville, how's your half going? If something's blocking you, I'm happy to look at it together for half an hour."),
                ("Neville", "The old records have no install dates. I didn't know who to ask."),
                ("Pip", "Ah, that's the Field Ops archive. I know who has it. Let's go together on Thursday."),
            ],
            note="Notice that the stuck Zombie started moving the moment someone asked a specific question. Not all of them do. But you have to ask to find out.",
        ),
    ),
    # ------------------------------------------------------------------ the Doppelgänger
    "doppelganger": dict(
        sighting=f"""{beat("January to August · the friendship")}
<p>Saskia was Pip's peer in Grid Planning and, by summer, his favourite person at work. She brought cardamom buns on
Fridays. She said his forecast work was “honestly the best in the team”. They had lunch twice a week and shared
complaints about Gerald's meetings.</p>
{beat("Thursday 11 September · Pip's 1:1")}
<p>Pip's manager mentioned, gently, that “some people” felt Pip “didn't really collaborate” and was “a bit precious
about his models”. Pip had collaborated with exactly one person that quarter. She had brought buns.</p>
{beat("Friday 12 September · the kitchen")}
<p>Saskia arrived with buns. “You look tired,” she said, warmly. “Is everything OK?” Pip said he was fine. He ate a bun.
It tasted of nothing.</p>
{beat("October · calibration")}
<p>Saskia and Pip had both been nominated for level 4. Only one promotion was available. Saskia got it. Pip's file said
<i>“strong analyst; collaboration concerns raised by peers”</i>. Peers, plural. Pip counted his peers. There were two.</p>
{note("The cure for whispering is not a louder whisper. It's people who know you well enough not to believe it.")}""",
        origin=dict(
            title="How a warm colleague became the Doppelgänger",
            beats=[
                ("2021 · her first job", "Saskia works in a consultancy where her director publicly humiliates a colleague who challenged him in a meeting. The colleague is gone within a month."),
                ("2021 · the lesson", "Saskia learns that open disagreement is dangerous. You smile in public and do your fighting in private, where it can't be traced."),
                ("2023 · MetroVolt", "She joins Grid Planning and is genuinely kind to everyone. She also notices that promotions are rationed: one per team per year, decided at calibration by people who hear about you second-hand."),
                ("2025 · the race", "When she and Pip are both nominated for one level-4 slot, the old lesson takes over. She never lies. She just mentions, to the right people, that Pip can be “a bit precious”. She still likes him. That's the frightening part."),
            ],
            turning="Watching honesty get someone fired, and deciding that warmth in public and competition in private was the safe way to survive.",
            saved="A workplace where disagreeing openly was safe. Or a promotion process that wasn't a zero-sum race between friends.",
            note="Most Doppelgängers aren't evil twins. They're scared competitors in a game with one prize. Change the game if you can; protect yourself if you can't.",
        ),
        know=f"""<p>The Doppelgänger is <b>competing</b> with you, usually for the same promotion, budget or reputation,
and has decided that open competition is too risky. So it is warm in public, where warmth is rewarded, and undermining in
private, where nobody checks.</p>
<p>Two cautions. First, <b>don't jump to it</b>: feedback that hurts is not proof of a traitor. Second, if it's real,
you won't beat it by being a better spy. You beat it by having <b>your own relationships</b>.</p>
<h3 class="kh">What it wants</h3>
<p>To win something scarce (a promotion, a project, a reputation) without the risk of an open fight.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because calibration happens behind closed doors, and people there judge you through second-hand comments. One
vague remark from a peer (“a bit precious”) can travel further than a year of your results.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Requests for specific examples.</li><li>Your direct relationships with your manager and skip-level.</li><li>Collaboration that's visible and in writing.</li><li>Being asked, kindly, “if anything bugs you, will you tell me first?”</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Nervous Rival</b><p>Competing out of fear. Often stops when the competition is open or over.</p></div>
<div><b>The Political Operator</b><p>Undermines as strategy. Needs your wide web and visible track record.</p></div>
<div><b>The Two-Faced Friend</b><p>Genuinely likes you and undermines you anyway. The hardest to see, and to accept.</p></div>
</div>
{note("You can't stop someone talking about you. You can make sure they're not the only one.")}""",
        difficulty=dict(
            normal=dict(who="A misunderstanding: a peer gave honest, clumsy feedback.",
                        know=["The feedback has a specific example behind it.", "The peer would say it to your face.", "It's about your behaviour, not your character."],
                        do=["Ask your manager for a specific example.", "Fix what's fair.", "Tell the peer: “If anything bugs you, tell me first.”"],
                        avoid="Assuming betrayal. Most hard feedback is honest.",
                        next="If vague comments keep arriving and never come with examples, you're at Nightmare."),
            nightmare=dict(who="The Nervous Rival or the Operator. A pattern of vague, second-hand damage.",
                           know=["“Some people feel…” with no examples.", "It started when you became competitors.", "Your manager knows things you only told one person."],
                           do=["Widen your web: direct relationships with your manager, skip-level and the people who use your work.", "Collaborate visibly and in writing; credit others publicly.", "Ask your manager directly for examples each time.", "Use the Quiet Test once if you must know."],
                           avoid="The counter-whisper. Now there are two Doppelgängers and your manager trusts neither.",
                           next="If it's affecting your promotion or review, you're at Hell."),
            hell=dict(who="A skilled operator with your manager's ear, and your promotion at stake.",
                      know=["Your file mentions “concerns raised by peers”.", "You lost a promotion on vague grounds.", "Your manager won't give examples."],
                      do=["Ask formally for the evidence behind any review comment.", "Build your skip-level relationship openly.", "Keep a record of your collaboration (thank-you emails, joint work).", "Decide whether this team can be won."],
                      avoid="Public confrontation without evidence. They'll be shocked and hurt, convincingly. You'll look paranoid.",
                      next="If the process is unfair and won't be reviewed, consider an internal move (Act III, the Escape Portal)."),
        ),
        mirror=dict(
            intro="Before you hunt a Doppelgänger, check your own reflection. Tick honestly.",
            signs=["You've said something about a colleague to your manager that you haven't said to them.", "You're warmer to rivals in public than in private.", "You've used “some people feel” about someone.",
                   "You've quietly hoped a peer's project would struggle.", "You compete for promotions by comparison rather than by results."],
            cure="Say it to their face first, or don't say it. And win on your own results: they last longer than anyone's reputation does.",
        ),
        rehearsal=dict(
            title="Scene: Friday 12 September, the kitchen. Saskia, buns. Pip has decided to name it.",
            intro="Not an accusation: an open hand, and a clear signal that you know.",
            lines=[
                ("Saskia", "You look tired. Is everything OK?"),
                ("Pip", "Honestly, a bit thrown. Marcus said some people think I don't collaborate. It surprised me, because I mostly work with you."),
                ("Saskia", "Oh no. That's awful. I'm sure it's nothing."),
                ("Pip", "Probably. But if anything I do ever bugs you, I'd really rather hear it from you first. I'd do the same for you."),
                ("Saskia", "…Of course. Totally."),
                ("Pip", "Also, want to co-present the model method at the team review? You know the data really well."),
                ("", "The vague comments stop in October. Pip never finds out for certain. He doesn't need to."),
            ],
            note="Pip tells her he knows without saying it, and offers visible collaboration she can't call “precious”. It closes the space where whispers grow.",
        ),
    ),
    # ------------------------------------------------------------------ the Martyr Banshee
    "martyr-banshee": dict(
        sighting=f"""{beat("Every night · 23:58")}
<p>Morag in Network Operations sent her emails just before midnight. They weren't urgent. They were evidence. Her Slack
status had said <i>drowning 🫠</i> since February. In every meeting she mentioned that she hadn't had a lunch break since 2023.</p>
{beat("Monday 7 April · 11:15")}
<p>Pip offered to take the weekly outage report off her plate. Morag looked at him the way people look at someone
offering to hold their baby. “No, no,” she said. “It's quicker if I do it. Nobody else knows the system.”</p>
{beat("Wednesday 9 April · the team meeting")}
<p>Morag said, with real pain, that nobody ever offered to help. Three people looked at Pip. Pip looked at the table.</p>
{beat("June · the contagion")}
<p>Pip caught himself sending an email at 23:40 that could have waited until morning. He noticed he'd added
“sorry for the late one, crazy week!” He had become, for one evening, a small Banshee.</p>
{note("The Banshee's wail is contagious. Spend a month next to one and you'll start sending emails at midnight to prove you care too. Don't.")}""",
        origin=dict(
            title="How the hero of the 2009 blackout became the Martyr Banshee",
            beats=[
                ("October 2009 · the blackout", "Half the city goes dark. Morag, then a junior engineer, stays in the control room for 40 hours straight and helps bring the grid back. It was genuinely heroic."),
                ("November 2009 · the email", "The CEO sends Morag a personal thank-you email. She prints it. It is still framed on her desk. It is the only time anyone senior has ever thanked her by name."),
                ("2010 to 2024 · the pattern", "Every recognition since has been for overwork: covering, staying late, never taking leave. Nobody has ever been thanked for training a backup. So she never trains one."),
                ("2025 · the identity", "Morag is the one who never goes home. If someone else could do the outage report, who would she be? Help feels like a threat. Overwork feels like love."),
            ],
            turning="The framed email: proof that what MetroVolt values is exhaustion, not systems that don't need heroes.",
            saved="Recognition, just once, for building a team that could run without her. And a manager who sent her home.",
            note="Martyrs are made by organisations that only notice suffering. If you lead people, thank the ones who made the crisis unnecessary.",
        ),
        know=f"""<p>The Banshee's identity is built on being <b>indispensable</b>. Being overworked is proof she matters.
Letting go of a task would be a relief and a threat at the same time. So she wails, and refuses.</p>
<p>Be careful: <b>the Banshee may also be genuinely burning out</b>. Treat the person kindly and the pattern firmly.</p>
<h3 class="kh">What it wants</h3>
<p>To be needed, to be seen as working hard, and, underneath, to be told it's OK to rest.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt celebrates heroics (the 2009 story is told at every induction) and never celebrates the quiet work
that prevents them. Late emails look like commitment. Single points of failure look like expertise.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Being replaceable.</li><li>Specific offers of help it can't easily refuse.</li><li>Being asked to teach someone.</li><li>Going home on time and nothing falling over.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Hero</b><p>Was praised for overwork once and never stopped. Needs recognition for something else.</p></div>
<div><b>The Gatekeeper</b><p>Keeps knowledge to stay needed. Needs to be the teacher, not the replaced.</p></div>
<div><b>The Genuinely Drowning</b><p>Really overloaded, really burning out. Needs support, not spells.</p></div>
</div>
{note("Busy is not a personality. Neither is tired. Go home.")}""",
        difficulty=dict(
            normal=dict(who="A busy colleague letting off steam.",
                        know=["It's a bad week, not a lifestyle.", "They accept help when it's specific.", "They go home most days."],
                        do=["Listen for a minute.", "Offer one specific thing with a time.", "Move on without joining the chorus."],
                        avoid="The busy duel: “you think you're busy?” Nobody wins the suffering Olympics.",
                        next="If help is always refused and the wailing continues, you're at Nightmare."),
            nightmare=dict(who="The Hero or the Gatekeeper. Overwork is part of who they are.",
                           know=["Every offer of help is refused.", "Their knowledge is a single point of failure.", "Their late emails are setting a team norm."],
                           do=["Make the Specific Offer: one task, one date, a small review.", "Ask to learn the task, not take it.", "Raise the single-point-of-failure risk to your manager as a business risk.", "Model the opposite: leave on time, visibly."],
                           avoid="Mocking them behind their back. They might be one bad week from collapse.",
                           next="If it's your manager and the wail becomes everyone's expectation, you're at Hell."),
            hell=dict(who="The Banshee is your manager, or it's real burnout.",
                      know=["You're expected to match their hours.", "They make mistakes, withdraw, or get ill.", "The team is burning out with them."],
                      do=["Protect your hours with clear availability.", "Deliver well inside your hours.", "If you see burnout signs, use the Wellbeing Flag kindly and privately.", "Read Act VIII, the Slow Hex of Burnout."],
                      avoid="The rescue fantasy: taking over all their work. You'll become the next Banshee.",
                      next="If you're burning out too, talk to your manager's manager or HR. It's a health issue, not a weakness."),
        ),
        mirror=dict(
            intro="Before you hunt a Banshee, check your own sent items. Tick honestly.",
            signs=["You send emails after 22:00 that could wait.", "You mention how busy you are in most meetings.", "You've refused help because “it's quicker if I do it”.",
                   "Nobody else could do your job next week.", "You feel slightly proud of being exhausted."],
            cure="Teach one person one thing you do this month, and take a real lunch break on Friday. Being replaceable is what lets you take holidays.",
        ),
        rehearsal=dict(
            title="Scene: Monday 7 April, 11:15. Pip tries again, with a specific offer.",
            intro="The Specific Offer and the Teach-Me Spell: easy to say yes to, and no threat to who she is.",
            lines=[
                ("Pip", "Morag, could you show me how the outage report works? Then you've got backup when you're on leave."),
                ("Morag", "Oh, it's really complicated, honestly, it's quicker if—"),
                ("Pip", "I'm sure. That's why I'd want you to show me. Thursday, 30 minutes? Then I draft this week's and you check it Monday. Ten minutes."),
                ("Morag", "…I suppose I am on leave in August."),
                ("Pip", "Exactly. And you'd be able to actually switch off."),
                ("", "Thursday: Morag explains the report for 55 minutes. She is visibly proud of it. In August, she takes two weeks off. The report goes out on time. Nobody frames an email about it, but Morag tells three people that Pip did a good job."),
            ],
            note="Being the teacher keeps the Banshee important. That's what makes saying yes possible.",
        ),
    ),
    # ------------------------------------------------------------------ the Know-It-All Basilisk
    "know-it-all-basilisk": dict(
        sighting=f"""{beat("Three months · evenings and weekends")}
<p>Pip built a simple machine-learning model to predict transformer failures from temperature, load and age data. On
seven years of history it caught 31 of 38 failures before they happened. He was nervous and proud.</p>
{beat("Tuesday 14 October · 15:20 · the asset review")}
<p>Pip presented it to the asset review. Dr. Lionel Ashe, principal engineer, did not look up from his laptop. “That
won't work,” he said. “We've got thirty years of physics for this. Next.” The chair moved to the next item. The idea was
turned to stone in four seconds. It had taken Pip three months.</p>
{beat("15:40 · the corridor")}
<p>An engineer stopped Pip by the lifts. “For what it's worth, I liked it,” she whispered, and hurried off, as if
being seen to like it was dangerous. It was.</p>
{beat("November · the first failure")}
<p>Transformer T-114 failed in a cold snap. Pip's model had flagged it in September. Nobody had looked at the model,
because the model was stone.</p>
{note("The Basilisk is right more often than you'd like. Listen for the 20% that's true before you dismiss the 80% that's rude.")}""",
        origin=dict(
            title="How a brave engineer became the Know-It-All Basilisk",
            beats=[
                ("Spring 2011 · the warning", "Lionel, then a senior engineer, warns the board that a batch of transformers will fail in a cold winter. He has the physics. The board, led by people who don't understand it, says “interesting” and moves on."),
                ("Winter 2011 · proven right", "Two transformers fail. Part of the city loses power for a day. Lionel is proven right, in public. Nobody apologises. He is quietly promoted."),
                ("2012 to 2024 · the armour", "Being right becomes Lionel's identity, and his protection. He treats every new idea as the board treated his: something to dismiss before it can embarrass anyone."),
                ("2025 · the irony", "Junior people bring him new ideas, and he does to them exactly what was done to him in 2011. He doesn't see it. He sees physics."),
            ],
            turning="The winter he was right and nobody said sorry. He decided he would never again be the one who wasn't listened to, so he stopped listening.",
            saved="An apology in 2012. Or a role as mentor, where his expertise was used to grow other people's ideas instead of judging them.",
            note="Many Basilisks were dismissed once by people who knew less than they did. That's why recruiting them works: you're giving them the respect they never got.",
        ),
        know=f"""<p>The Basilisk is usually <b>genuinely expert</b>, and that's the problem. Its identity rests on being the
one who knows. New ideas from junior people threaten that identity, so it kills them on sight. The trick: <b>don't look
it in the eye</b>. Don't challenge its expertise; use it.</p>
<h3 class="kh">What it wants</h3>
<p>Respect for its knowledge, and protection from being wrong in public.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt is an engineering company with real risks, so caution is respected and new ideas are suspected.
Seniority settles arguments, and nobody wants to be the junior who contradicted the principal engineer.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Seeing an idea for the first time in public.</li><li>Data it hasn't checked.</li><li>Being wrong in front of juniors.</li><li>Being made irrelevant by a new method.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Burned Expert</b><p>Was dismissed once; dismisses others now. Softens when asked for help.</p></div>
<div><b>The Gatekeeper</b><p>Guards knowledge as power. Needs to be part of the new thing.</p></div>
<div><b>The Bored Genius</b><p>Has seen it all. Interested only in genuinely hard questions. Bring one.</p></div>
</div>
{note("Don't fight the expert. Recruit them. Then they fight for you.")}""",
        difficulty=dict(
            normal=dict(who="A confident expert on a rushed day.",
                        know=["They dismiss quickly but engage when asked.", "Their objections are specific.", "They respond to data."],
                        do=["Ask for the main reason: “What's the catch?”", "Write down the objection.", "Come back with data on that point."],
                        avoid="The stare-down: challenging their expertise in front of others.",
                        next="If every new idea dies on sight, you're at Nightmare."),
            nightmare=dict(who="The Burned Expert or the Gatekeeper. Kills ideas by reflex.",
                           know=["Juniors have stopped proposing anything.", "Objections are vague: “won't scale”, “we tried that”.", "They never read past the title."],
                           do=["The Apprentice's Question: show them privately first and ask them to poke holes.", "Use their expertise visibly: add their improvements and credit them.", "Propose a small, safe pilot (shadow mode).", "Ask what evidence would change their mind."],
                           avoid="Building it behind their back. Once discovered, the fight is about trust, not the idea.",
                           next="If they own the decision and won't move, you're at Hell."),
            hell=dict(who="The Basilisk owns the decision, and the decision is no.",
                      know=["They have a formal veto.", "Pilots are refused too.", "Leadership defers to them on everything."],
                      do=["Find a sponsor above them who cares about the outcome (cost, outages).", "Run the safest possible pilot, with their name on the risk controls.", "Let results argue for you over time.", "Keep a record of what the idea would have caught."],
                      avoid="“I told you so” when it's proven right. You'll win the moment and lose the expert forever.",
                      next="If the idea matters and can't move here, take it to a team that can use it."),
        ),
        mirror=dict(
            intro="Before you hunt a Basilisk, check your own gaze. Tick honestly.",
            signs=["You've said “we tried that” without asking what's different this time.", "You dismiss ideas from juniors faster than ideas from seniors.", "You enjoy finding the flaw more than the fix.",
                   "You can't remember the last time a junior changed your mind.", "You read the title, not the document."],
            cure="Next time someone brings an idea, ask “what would have to be true for this to work?” before you say what's wrong. Expertise is most useful when it builds.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 7 October, a week before the review. Lionel's office.",
            intro="The Apprentice's Question: show the expert first, in private, and ask for help.",
            lines=[
                ("Pip", "Lionel, I'm presenting a transformer-failure model next week. Before I do, would you poke holes in it? You know the physics better than anyone."),
                ("Lionel", "Machine learning. Hm. It'll miss the moisture failures. They don't show in load data."),
                ("Pip", "That's really useful. How would you detect those?"),
                ("Lionel", "Oil sample results. We have them since 2016, in a spreadsheet nobody reads."),
                ("Pip", "Could I add them, and say in the review that you spotted the gap?"),
                ("Lionel", "…If you must. And run it in shadow mode first. No decisions on it for three months."),
                ("", "At the review, Lionel says: “It's a reasonable start. I've suggested the oil data.” The model goes into shadow mode. In November it flags T-114."),
            ],
            note="The same expert who would have killed it in public helped build it in private. Same man, same idea, different first meeting.",
        ),
    ),
    # ------------------------------------------------------------------ the Doom Prophet
    "doom-prophet": dict(
        sighting=f"""{beat("Monday 3 March · 09:30 · the alerts kick-off")}
<p>Pip proposed automated alerts for substation overloads, so the Control Room would see trouble before customers did.
He had a demo. It flashed nicely.</p>
{beat("09:34")}
<p>Terrence, who has worked in the Control Room since the 2009 blackout, sighed the sigh of a man who has seen empires
fall. “We tried automation in 2014. Alarms went off for three weeks straight. Nobody slept. It'll fail.”</p>
{beat("09:34 to 09:53")}
<p>He then told the story of 2014 for nineteen minutes: the vendor, the alarm storm, the night someone muted everything
and nearly missed a real fault, the consultants who left. It was, to be fair, a very good story. When it ended, the room
had lost its enthusiasm, the demo had gone to sleep, and nobody could remember what Pip had proposed.</p>
{beat("Afterwards")}
<p>Two new joiners told Pip they'd had ideas too, but “there's no point, Terrence will say it failed in 2014”. They had
been at MetroVolt for six weeks.</p>
{note("The Doom Prophet is wrong about the conclusion and often right about the reasons. Steal the reasons.")}""",
        origin=dict(
            title="How a careful operator became the Doom Prophet",
            beats=[
                ("2009 · the blackout", "Terrence is on shift the night half the city goes dark. He learns, in one night, everything that can go wrong with a grid."),
                ("2014 · the warning", "A vendor sells MetroVolt an automated alarm system. Terrence warns that the thresholds are wrong. Nobody listens. For three weeks the alarms never stop. One night, an operator mutes them and nearly misses a real fault."),
                ("2014 · the review", "The post-incident review blames “operator error”. The vendor leaves. The consultants leave. Terrence's team cleans up. Nobody writes down what went wrong."),
                ("2015 onwards · the living archive", "Because nobody recorded the lessons, Terrence becomes the lessons. Every new idea reminds him of 2014, so he tells the story, every time, to protect the operators who'll pay if it goes wrong again."),
            ],
            turning="The review that blamed his team for a vendor's mistake, and recorded nothing. He became the record.",
            saved="A real lessons-learned document in 2014. Or someone asking him first, before the kick-off, instead of last.",
            note="Every Doom Prophet is protecting somebody. Find out who, and you'll find out how to bring them on board.",
        ),
        know=f"""<p>The Prophet is not a pessimist by nature. It is a <b>survivor</b>. It has watched good ideas fail for reasons
nobody wrote down, and it remembers every one. That makes it the most underused risk expert in the building. The problem
isn't the warning; it's that the warning comes as a verdict instead of a risk.</p>
<h3 class="kh">What it wants</h3>
<p>To stop the same disaster happening twice, and to protect the people who'll pay for it.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt doesn't record its lessons, so they live in people. And because failures in a power company hurt
real customers, caution earns respect that enthusiasm doesn't.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Being ignored again.</li><li>Its team paying for someone else's optimism.</li><li>Projects that skip the boring risks.</li><li>Consultants.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Survivor</b><p>Has real scars and real knowledge. Turns into your best ally when asked first.</p></div>
<div><b>The Cynic</b><p>Has stopped believing anything can improve. Needs a small win to see.</p></div>
<div><b>The Protector</b><p>Guards a team from change. Needs to see that the team is safe.</p></div>
</div>
{note("Every prophet of doom is a risk register that hasn't been asked nicely.")}""",
        difficulty=dict(
            normal=dict(who="A cautious colleague with a story.",
                        know=["The warning has specific reasons.", "They engage when you ask what went wrong.", "They don't block, they warn."],
                        do=["Ask what exactly went wrong last time.", "Write each answer down as a risk.", "Show how your plan handles each one."],
                        avoid="“That was 2014, things are different now.” You've just told them you don't want the map.",
                        next="If the warning kills every idea in every meeting, you're at Nightmare."),
            nightmare=dict(who="The Cynic or the Protector. Doom by reflex.",
                           know=["New joiners have stopped suggesting things.", "The same story is told every time.", "Meetings lose energy after they speak."],
                           do=["Talk to them before the kick-off, not in it.", "Give them the Prophet's Seat: official risk reviewer.", "Run a pre-mortem where their knowledge shines.", "Give them a fixed slot to raise risks, so the rest of the meeting moves."],
                           avoid="Leaving them out to avoid the negativity. They'll find out, and the prophecy becomes a mission.",
                           next="If the Prophet is senior and their doom decides things, you're at Hell."),
            hell=dict(who="A senior Prophet whose doom shapes decisions.",
                      know=["Ideas are killed by stories, not by data.", "Leadership defers to the Prophet's experience.", "Nothing has changed in years."],
                      do=["Answer each risk in writing.", "Run a small pilot designed to beat the old failure.", "Let the results update the story.", "Thank them publicly when the pilot works."],
                      avoid="The hype shield: answering doom with forced optimism. Now you're the Toxic Positivity Siren.",
                      next="If nothing can change at all, take your idea where it can."),
        ),
        mirror=dict(
            intro="Before you hunt a Prophet, check your own predictions. Tick honestly.",
            signs=["You've said “we tried that” in the last month.", "Your first reaction to new ideas is a risk.", "You tell the same cautionary story more than once a quarter.",
                   "New joiners stop talking when you start.", "You'd secretly be a little pleased if a new idea failed."],
            cure="Turn every warning into a risk and a fix: “It failed because X. If you do Y, it might not.” Same knowledge, opposite effect.",
        ),
        rehearsal=dict(
            title="Scene: Friday 28 February, the Control Room, before the kick-off.",
            intro="The Transmutation, done early: ask the Prophet first, and turn the story into a register.",
            lines=[
                ("Pip", "Terrence, I'm proposing substation alerts on Monday. I heard 2014 went badly. What exactly went wrong?"),
                ("Terrence", "Thresholds set by people who'd never sat a night shift. Two thousand alarms a day. No owner for the rules. And the vendor vanished."),
                ("Pip", "That's gold. Can I put each of those in the plan as a risk, with a fix next to it?"),
                ("Terrence", "…You can try."),
                ("Pip", "And would you review the thresholds before we switch anything on? Nobody knows the nights like you do."),
                ("", "Monday 09:34. Terrence says: “I've seen the plan. It's better than 2014.” The kick-off finishes in 40 minutes. The new joiners notice."),
            ],
            note="The Prophet came to the kick-off already part of the plan. That's the whole spell: ask first, and the doom becomes a register.",
        ),
    ),
    # ------------------------------------------------------------------ the Toxic Positivity Siren
    "toxic-positivity-siren": dict(
        sighting=f"""{beat("Monday 6 October · 09:00 · the email")}
<p>MetroVolt announced a hiring freeze. Grid Planning would not refill its six open roles. The email ended:
<i>“We're confident this is an opportunity to work smarter together.”</i></p>
{beat("Wednesday 8 October · the launch")}
<p>Kaylee, Head of Employee Joy, launched <b>Gratitude Fortnight</b>: a wall of thank-you notes, a mindfulness app,
and a gong in the atrium to be struck “whenever you feel grateful”. The gong was struck twice that week, both times
by Kaylee.</p>
{beat("Thursday 16 October · the town hall Q&amp;A")}
<p>Pip asked how teams would cope with six unfilled roles in Grid Planning. Kaylee smiled. “I love that energy! Let's
reframe that as a growth opportunity. 🚀” The gong was struck. Nobody asked another question.</p>
{beat("November")}
<p>Two of Grid Planning's projects slipped by eight weeks. In the post-mortem, someone asked why nobody had raised the
workload risk earlier. Pip looked at the gong.</p>
{note("You can be positive about the people and honest about the problem in the same sentence. That's not negativity, it's management.")}""",
        origin=dict(
            title="How an HR partner became the Toxic Positivity Siren",
            beats=[
                ("2024 · the hire", "Kaylee is hired to fix MetroVolt's engagement scores, the worst in the group. She is warm, energetic and genuinely wants people to be happy at work."),
                ("Week 3 · the brief", "Lord Varnish tells her: “Keep morale up. Don't open cans of worms.” She has a budget for events and no budget, or authority, to fix anything."),
                ("Month 1 · the town hall", "Asked about pay, Kaylee answers honestly: “That's a fair concern, I'll raise it.” She's called into Communications the next day and told to “stay on message”."),
                ("2025 · the song", "Kaylee learns that positivity is the only safe output. Every problem becomes an opportunity. She doesn't fully believe it. But she believes she'll be fired if she stops singing."),
            ],
            turning="The day she was told off for one honest answer, and learned that her job was to make problems sound nice, not to fix them.",
            saved="Authority to escalate real issues. Or a leader who said “thank you for being honest” after that first town hall.",
            note="Sirens usually aren't fools. They're messengers who were told what the message is. Take the real problem to whoever wrote the message.",
        ),
        know=f"""<p>The Siren is not lying. Often it's been <b>told to keep morale up</b>, and has no power to fix what's
underneath. Positivity is its only tool. The danger is to <b>you</b>: in a Siren culture, people who raise problems
get labelled “negative”.</p>
<h3 class="kh">What it wants</h3>
<p>Happy people, good engagement scores, and to stay out of trouble with the people who hired it.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because leaders prefer good news, and bad news has no channel. Morale campaigns are cheaper than fixing workload. And
anyone who names a problem in public is seen as “not a team player”, so problems go underground.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Calm, specific questions in public.</li><li>Problems that come with solutions.</li><li>Being asked to escalate something.</li><li>Silence after the gong.</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The True Believer</b><p>Really thinks attitude fixes everything. Responds to data, eventually.</p></div>
<div><b>The Messenger</b><p>Told to stay positive. Would love to escalate. Give them a way.</p></div>
<div><b>The Shield</b><p>Protects leadership from bad news. Go around, to the person who can act.</p></div>
</div>
{note("Optimism is a strategy. Ignoring the iceberg is not.")}""",
        difficulty=dict(
            normal=dict(who="An upbeat colleague who prefers good news.",
                        know=["They do listen when you're specific.", "The positivity is personal, not policy.", "Problems still get fixed, slowly."],
                        do=["Use the Both-And: agree with the positive, then add the problem.", "Ask for a decision, not a feeling.", "Bring a suggested fix."],
                        avoid="The doom counter-song. You'll become the official Negative Person.",
                        next="If raising concerns gets you labelled negative, you're at Nightmare."),
            nightmare=dict(who="A culture where concerns are career-limiting.",
                           know=["People share problems only in private chats.", "Reviews mention “attitude” after honest questions.", "Bad news arrives with a celebration."],
                           do=["Use the Problem-With-a-Path: good news, problem, proposal, ask.", "Take the real problem to the person who can fix it, not the one with the gong.", "Keep a short written record that you raised it.", "Find allies who see the same thing."],
                           avoid="Mockery. “Growth opportunity 🚀” with a skull in the team chat will be screenshotted.",
                           next="If leadership punishes bad news, you're at Hell."),
            hell=dict(who="Leadership punishes bad news.",
                      know=["Messengers are blamed.", "Problems are discovered only when they explode.", "Engagement surveys aren't anonymous in practice."],
                      do=["Raise serious issues in writing to the person accountable.", "Keep a copy.", "Pick the problems worth the cost.", "If it's about safety or ethics, use the formal channel (Act VIII, the Dark Pact)."],
                      avoid="Swallowing serious concerns. When it bursts, someone will ask why nobody spoke up.",
                      next="If you can't do your job honestly here, plan your exit."),
        ),
        mirror=dict(
            intro="Before you hunt a Siren, listen to your own songs. Tick honestly.",
            signs=["You've called a problem “an opportunity” this month.", "You avoid bringing bad news to your boss.", "You feel irritated when someone raises a risk in a meeting.",
                   "You've answered a hard question with enthusiasm instead of an answer.", "You think morale is mostly about attitude."],
            cure="Next time someone raises a problem, say “that's a fair concern” first. Then decide whether it's an opportunity. Usually it's just a problem, and that's fine.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 16 October, the town hall. Pip tries again, differently.",
            intro="The Both-And and the Specific Question: positive about the people, honest about the problem, asking for a decision.",
            lines=[
                ("Kaylee", "Any more questions? Let's keep the good vibes going!"),
                ("Pip", "I'm genuinely glad we're keeping the team together through the freeze. With six open roles in Grid Planning, which of our Q4 projects should slow down first?"),
                ("Kaylee", "Ooh, great question! I think we can all work smarter—"),
                ("Pip", "Definitely. Could someone from leadership confirm the priorities in writing this month? It'd help us plan."),
                ("", "A pause. Benedict Crane, at the side of the room, raises a hand. “Fair question. I'll send priorities by the 31st.”"),
                ("Kaylee", "Thank you, Benedict! Wonderful."),
                ("", "Kaylee finds Pip afterwards. “Thank you,” she says quietly. “I've been trying to get them to say that for weeks.”"),
            ],
            note="The Siren was the Messenger breed. Pip's specific, positive question gave her what she couldn't ask for herself.",
        ),
    ),
    # ------------------------------------------------------------------ the Boundary Goblin
    "boundary-goblin": dict(
        sighting=f"""{beat("Sunday 23 March · 23:47")}
<p>Pip was in bed. His phone lit the ceiling. Hugo, programme manager on Lumen: <i>“Quick q, no rush 🙂 where's the meter data?”</i></p>
{beat("23:52")}
<p><i>“?”</i></p>
{beat("23:53")}
<p>Pip replied, because he was awake and it was only a quick question. Hugo replied <i>“legend 🙏”</i>, and then
asked a second quick question. Pip answered that too. It was 00:20 when he put the phone down. He lay awake until two,
thinking about meter data.</p>
{beat("Monday 07:10 · and every week after")}
<p><i>“Morning! Any update on last night?”</i> From then on, Hugo messaged on Sunday nights, Tuesday nights, and once,
memorably, from a wedding. Hugo had learned that Pip was always available. The Goblin had been fed after midnight.
Everyone knows what happens then.</p>
{note("A boundary you explain but don't keep is just a speech. A boundary you keep without explaining is a habit, and habits are what people learn.")}""",
        origin=dict(
            title="How a nurse became the Boundary Goblin",
            beats=[
                ("2012 to 2018 · night shifts", "Hugo is an A&amp;E nurse. Nights are normal. Everything is urgent. His body clock never fully recovers."),
                ("2019 · a new career", "He retrains as a project manager. His first boss replies to messages at all hours, and Hugo copies him. In his first review he's praised for being “incredibly responsive”."),
                ("2023 · the promotion", "Hugo is promoted to programme manager. The review says “always available”. Being reachable at midnight has become his brand."),
                ("2025 · Lumen", "With a regulator deadline and 60,000 meters to install, Hugo is anxious all the time. He thinks of things at night and sends them before he forgets. He genuinely means “no rush”. He just can't stand not asking."),
            ],
            turning="The review that praised “always available”, and turned a nurse's habit into a manager's expectation of everyone else.",
            saved="Scheduled send, discovered early. Or a boss who modelled switching off, so “always available” never looked like a virtue.",
            note="Most Goblins are anxious, not cruel. Reply at 08:30, kindly and completely, for two weeks, and watch them learn.",
        ),
        know=f"""<p>The Goblin is rarely a tyrant. It's usually <b>anxious and badly organised</b>: it thinks of things at night
and sends them before it forgets. It often genuinely means “no rush”. But every fast reply teaches it that you're on call.
You trained it. You can untrain it.</p>
<h3 class="kh">What it wants</h3>
<p>To get the question out of its head, and to feel that things are moving.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because phones put work in everyone's bedroom, and MetroVolt praises “responsiveness” in reviews. A fast reply at
midnight looks like commitment. A reply at 08:30 looks like nothing at all, even though it's what a working day is.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Clear, visible working hours.</li><li>Morning replies that are warm and complete.</li><li>An agreed way to reach you for real emergencies.</li><li>Being asked “is this urgent, or can it wait until morning?”</li></ul>
<h3 class="kh">The three breeds</h3>
<div class="breeds">
<div><b>The Night Owl</b><p>Works late, means “no rush”. Learns from morning replies.</p></div>
<div><b>The Anxious Forgetter</b><p>Sends to empty their head. Needs scheduled send and a list.</p></div>
<div><b>The Always-On Tyrant</b><p>Expects replies, and punishes silence. Needs agreed hours, in writing.</p></div>
</div>
{note("You teach people how to treat you, one reply at a time.")}""",
        difficulty=dict(
            normal=dict(who="The Night Owl. A late worker who means “no rush”.",
                        know=["They don't chase if you reply in the morning.", "They work late themselves, by choice.", "They apologise if asked."],
                        do=["Reply at the start of your next working day, warmly and fully.", "No apology for not replying at midnight.", "Set your working hours in your status."],
                        avoid="The midnight feed: replying “just this once”. Goblins remember precedents, not exceptions.",
                        next="If they chase, complain or escalate when you don't reply, you're at Nightmare."),
            nightmare=dict(who="The Anxious Forgetter. Expects fast replies and chases.",
                           know=["“?” arrives five minutes after “no rush”.", "They mention that you didn't reply last night.", "Others in the team feel it too."],
                           do=["Agree the Emergency Rune: real emergencies get a call.", "Put your hours in your status, your signature and your calendar.", "Tell them once, kindly, in person, how you work.", "Suggest scheduled send for the whole team."],
                           avoid="The furious lecture at 07:00. True, but it reads as an attack.",
                           next="If it's your manager and always-on is the culture, you're at Hell."),
            hell=dict(who="The Always-On Tyrant: your manager, with a culture behind them.",
                      know=["Silence after hours is held against you.", "Reviews praise availability.", "Everyone is tired."],
                      do=["Agree core hours with your manager, in writing.", "Deliver excellently inside them.", "Be reachable for agreed emergencies only.", "Read Act VIII: the Salt Circle and the Slow Hex of Burnout."],
                      avoid="The total blackout: no contact even for real emergencies. In a power company, outages happen at 3 a.m.; know which ones are yours.",
                      next="If you're expected to be on call, it should be paid and rota'd. Ask for that."),
        ),
        mirror=dict(
            intro="Before you hunt a Goblin, check your own outbox. Tick honestly.",
            signs=["You message colleagues after 21:00.", "You write “no rush” and then follow up.", "You feel anxious until someone replies.",
                   "You've messaged someone on holiday “just quickly”.", "You've never used scheduled send."],
            cure="Write your night thoughts in a list, or schedule them for 08:30. Your question still gets asked. Your colleagues still get to sleep.",
        ),
        rehearsal=dict(
            title="Scene: Monday 08:30. Pip replies to Sunday night's message. Then a conversation.",
            intro="The Morning Reply and the Emergency Rune: warm, complete, and with a door for real emergencies.",
            lines=[
                ("Pip", "Morning Hugo! The meter data is in the Lumen folder, tab 3. Shout if anything's missing."),
                ("Hugo", "Thanks! Sorry, I know I messaged late."),
                ("Pip", "No worries. I'm switching off after six these days so I'm sharp in the day. If something's truly urgent, call me and I'll always pick up."),
                ("Hugo", "Oh. Right. Yes, of course. Totally fair."),
                ("Pip", "And if you think of things at night, scheduled send is brilliant. I've started using it."),
                ("", "Two weeks later, Hugo's messages arrive at 08:30. All of them. To everyone. He tells the programme board he's discovered “a game-changing productivity tool”."),
            ],
            note="Pip never says “stop messaging me at night”. He says how he works, offers a door for emergencies, and shows a better tool. Most Goblins just need permission to stop.",
        ),
    ),
}
