# Series 4 · The Darkside of the Corporation · Act II: The Bestiary (difficult people).
# Rendered by scripts/grimoire.py. `note(text)` (the Annotator's margin note) is injected by the loader.
# Text is raw HTML. Stats follow grimoire.STATS: sanity, career XP, mana, armor, stealth, allies, soul, time, backfire safety.

ACT = dict(
    no=2,
    title="The Bestiary",
    sub="Know the creatures of the open plan",
    summary="Act II of The Darkside of the Corporation: twelve difficult-colleague creatures, their omens, counter-spells and the forbidden spells that backfire.",
    intro=f"""<p class="lead">Every office has a bestiary. Ours lives on floors 4 to 27 of <b>The Grid</b>, headquarters
of <b>MetroVolt Electric Corporation</b>: 6,200 souls who keep the lights on for 2.3 million homes and cannot,
between them, book a meeting room.</p>
<p>The creatures in this Act are not villains. Most are ordinary people who have learned that a certain bad
behaviour gets rewarded. That is good news: behaviour that was learned can be blocked, starved or redirected.
You cannot change the creature. You can change what it gets from you.</p>
{note("Rule zero: if a creature is harassing, threatening or discriminating, it is not a creature. It is a case. Write it down and go to HR or a lawyer. Spells are for annoying people, not dangerous ones.")}
<p>Our guide through the Act is <b>Pip</b>, a junior analyst in Grid Planning, level 3, full of hope. Watch what
happens to his hope. Learn from it.</p>""",
    cast=[
        ("Pip", "he/him", "junior analyst, Grid Planning. The apprentice. Makes the mistakes so you don't have to."),
        ("The Chronicler", "they/them", "nineteen years at MetroVolt. Writes the entries in the grand voice."),
        ("The Annotator", "she/her", "ex-MetroVolt, now freelance. Writes in the margins. Has no patience left, only advice."),
        ("Lord Varnish", "he/him", "VP of Strategic Synergy. Speaks only in frameworks. Appears when least wanted."),
        ("Dorian", "he/him", "Strategy. Presents beautifully. Mostly other people's work."),
        ("Gerald", "he/him", "Director of Alignment. Owner of the Weekly Sync on the Syncs."),
        ("Rhona", "she/her", "project lead, Project Lumen (the smart-meter rollout). Remembers differently."),
        ("Brett", "he/him", "Commercial. Has never finished a sentence that was not his own."),
        ("Felicity", "she/her", "Facilities. Writes emails with the temperature of a substation in January."),
        ("Neville", "he/him", "Asset Records, fourteen years. Has survived six reorgs without doing visible work."),
        ("Saskia", "she/her", "Pip's peer in Grid Planning. Lovely. Too lovely."),
        ("Morag", "she/her", "Network Operations. The busiest person in the building, as she will tell you."),
        ("Dr. Lionel Ashe", "he/him", "principal engineer. Was right once in 2011 and has not stopped."),
        ("Terrence", "he/him", "Control Room, here since the 2009 blackout. Has seen everything fail."),
        ("Kaylee", "she/her", "Head of Employee Joy. Has a gong."),
        ("Hugo", "he/him", "programme manager, Project Lumen. Lives on Slack. Never sleeps. Assumes you don't either."),
    ],
    entries=[
        # ------------------------------------------------------------------ 1
        dict(
            slug="credit-vampire", flagship=True,
            name="The Credit Vampire", sigil="☾",
            epithet="Feeds on your work by night. Presents it by day.",
            threat=4, habitat="steering committees, all-hands slides, any email that starts “great work team”",
            weakness="daylight: other people knowing what you did, before the meeting",
            summary="The Credit Vampire presents your work as theirs. How to spot it, the counter-spells that put your name in daylight, and the forbidden spells that backfire.",
            sighting=f"""<p>On the 3rd of March, Pip spent eleven evenings building the <b>Q3 load forecast</b>, a model that
predicted the heatwave peak to within 2% and saved MetroVolt an estimated €1.4 million in emergency power purchases.
On the 4th, at the all-hands in the atrium, Dorian from Strategy presented it. Slide 7 read <i>“Dorian's model.”</i>
Pip's name appeared nowhere. Not in the title, not in the footer, not even in the font.</p>
<p>Lord Varnish called it “exactly the kind of initiative we need.” Dorian looked humble. Pip clapped, because
everyone was clapping, and then went to the bathroom on floor 9 and stared at the hand dryer for some time.</p>""",
            know=f"""<p>The Vampire is rarely evil. It is <b>hungry</b>. It lives where work is invisible and only the
presenter is seen. In most companies, the person who stands in front of leadership gets the credit by default.
Nobody checks the git history of a slide deck.</p>
<p>So the Vampire does not need to lie. It only needs your work to stay in the dark until it can carry it into
a room you are not in. Feed it darkness and it grows fat. Sunlight kills it.</p>
{note("“Sunlight” means other people knowing what you did, before the meeting. Not literal sun. HR has asked me to stop saying this.")}
<p>The ones to watch are not the dramatic thieves. They are the gentle ones who say “we” about the work and
“I” about the idea, and who always, always offer to “take it from here.”</p>""",
            omens=[
                "“Send me the file, I'll take it from here.”",
                "You are not invited to the meeting where your work is presented.",
                "They say “I” about successes and “we” about problems.",
                "Your manager first hears about your work from them.",
                "Your name has quietly vanished from version 3 of the deck.",
            ],
            counters=[
                ("The Dawn Ward", "Announce the work before they can present it. A short note to your manager and the people who will use it, the moment it is done.",
                 "“Quick heads-up before Thursday: the Q3 load forecast is finished. Happy to walk anyone through how I built it.”"),
                ("The Name-Carving Rite", "Put your name in the artefact itself: the cover slide, the file name, the footer, the model's first tab. Vampires hate file names.",
                 "<code>Q3-load-forecast_Pip_v4.xlsx</code> · “Prepared by Pip, Grid Planning”"),
                ("The Invitation Hex", "Ask to present the part you built. Frame it as saving them effort, which it is.",
                 "“Could I take the five minutes on the model? It'll save you questions on the details.”"),
                ("The Grateful Reflection", "When credit is taken anyway, thank them publicly and generously for sharing your work. Polite. Accurate. Lethal.",
                 "“Thanks Dorian for presenting the forecast I built. Glad it helped. Shout if anyone wants the method.”"),
            ],
            forbidden=[
                ("The Public Staking", 4, "Calling them a thief at the all-hands. You look bitter; they look calm. The room remembers the scene, not the facts."),
                ("The Poisoned File", 5, "Sabotaging the next model you hand over. The heatwave comes, the forecast is wrong, the city browns out. And so does your career."),
                ("The Whisper Campaign", 3, "Complaining to everyone at the coffee machine. The coffee machine reports to Lord Varnish."),
            ],
            difficulty=dict(
                normal="A careless peer who forgot to mention you. A friendly word fixes it: “Mind adding my name on slide 7?” Most people are mortified and do.",
                nightmare="A habit. They do it every quarter. Cast the Dawn Ward every single time, keep the Weekly Deeds Scroll, and mention the pattern calmly to your manager with dates.",
                hell="It's your boss, and the culture rewards it. Your paper trail is now your shield: keep the scroll, build relationships with your skip-level, and read Act III, entry 12 (the Escape Portal).",
            ),
            stats=[4, 5, 4, 4, 4, 3, 5, 5, 4], stats_for="The Dawn Ward",
            loot=("The Weekly Deeds Scroll",
                  "A three-line Friday note to your manager. Five minutes a week. Your work is in daylight before anyone can carry it into a meeting.",
                  """Subject: Week 10 · Pip · Grid Planning

SHIPPED     Q3 load forecast v4 (heatwave peak within 2%). Shared with Ops + Trading.
IN PROGRESS Substation 14 capacity check, due 21 Mar.
NEED HELP   Access to the 2025 smart-meter data (waiting on IT, ticket #4471)."""),
            trial=[
                ("Dorian asks for your file “to tidy the formatting” the day before the steering committee. What do you do?",
                 "Send it, with your name already in the file name and on the cover, and copy your manager: “Here's the forecast for tomorrow. Happy to join for the method questions.” You helped, and you're in daylight."),
                ("Your manager praises Dorian for your model in a group chat. What's the best reply?",
                 "The Grateful Reflection, in the same chat: “Thanks! Glad the forecast I built is useful. Dorian did a great job presenting it.” No accusation, just the record."),
                ("Credit is stolen once, by someone new to the team. Which difficulty is this, and which spell?",
                 "Normal. Assume carelessness, not malice. A private, friendly word, then the Dawn Ward from now on."),
            ],
            last_word="The best time to claim credit is before the work is finished. The second best time is in writing.",
        ),
        # ------------------------------------------------------------------ 2
        dict(
            slug="meeting-lich",
            name="The Meeting Lich", sigil="⌛",
            epithet="Undead. Recurring. Spawns more of itself.",
            threat=3, habitat="the 27th floor meeting rooms, every Tuesday at 10:00, forever",
            weakness="a written agenda and a named decision",
            summary="The Meeting Lich runs meetings that never end and spawn more meetings. How to starve it with agendas, decisions and the polite decline.",
            sighting=f"""<p>Gerald, Director of Alignment, runs the <b>Weekly Sync on the Syncs</b>: a 90-minute meeting where
the leads of four other weekly meetings report on what was said in those meetings. It has met 112 times. It has
made one decision, in 2024, which was to move itself from Monday to Tuesday.</p>
<p>Pip was invited “for visibility” in week 2. By week 6 he had been made owner of a follow-up meeting to align the
actions from the sync. The Lich had reproduced. Pip now had four hours of meetings a week about one spreadsheet.</p>""",
            know=f"""<p>A Lich is a meeting that has lost its soul (its purpose) but keeps walking. Meetings are cheap to
create and expensive to kill: nobody wants to be the person who cancelled the thing the VP once attended.</p>
<p>The organiser usually means well. A recurring meeting <i>feels</i> like control. It looks like work on a
calendar. And for someone whose job title contains the word “Alignment”, a full calendar is the evidence that
they exist.</p>
{note("Do the maths out loud once. Twelve people, ninety minutes, weekly: that's 936 hours a year. MetroVolt bills a field engineer at €85 an hour. The Sync costs about €80,000. It has decided one thing.")}""",
            omens=[
                "No agenda, or an agenda that says “updates”.",
                "The meeting ends with “let's take that offline” and a new invite appears an hour later.",
                "More than eight people, and two of them are speaking.",
                "Nobody can say what was decided last week.",
                "It has outlived the project it was created for.",
            ],
            counters=[
                ("The Agenda Rune", "Before accepting, ask what decision the meeting needs from you. A Lich cannot survive a question about its purpose.",
                 "“Happy to help. What do you need me to decide or bring? Then I can prepare properly.”"),
                ("The Written Offering", "Replace your attendance with a written update. Most status meetings are a document read aloud.",
                 "“I can't make Tuesday, but here's my update in three lines. Shout if anything needs discussing.”"),
                ("The Last Rites", "At the end, say the decision and the owner out loud and write them down. Meetings that produce decisions stop needing to repeat themselves.",
                 "“Before we go: so we've decided X, Sam owns it, by Friday. Anything else, or can we give back the last ten minutes?”"),
                ("The Mercy Kill", "Propose ending the series, with a review date. People agree to “pause and see” more easily than to “cancel”.",
                 "“Shall we pause this for a month and switch to a written update? If we miss it, we bring it back.”"),
            ],
            forbidden=[
                ("Laptop Necromancy", 2, "Attending in body while openly working on something else. Everyone sees, nobody says, and you are now the person who doesn't care."),
                ("The Silent Decline", 3, "Just stop showing up without a word. You will be discussed in your absence, which is the one thing worse than being in the meeting."),
                ("The Rival Meeting", 4, "Fight the Lich by scheduling a meeting about the meeting. Congratulations. You are a Lich now."),
            ],
            difficulty=dict(
                normal="One drifting meeting. Ask for an agenda and suggest a shorter slot. Most organisers are relieved.",
                nightmare="A meeting culture: your week is 60% recurring invites. Audit your calendar, decline with written updates, and agree with your manager which meetings you truly own.",
                hell="Leadership measures commitment by attendance. Protect two focus blocks a week, keep your updates sharp so your absence looks efficient, not lazy, and pick your battles.",
            ),
            stats=[4, 3, 4, 2, 4, 4, 5, 5, 5], stats_for="The Agenda Rune",
            loot=("The Decline With Grace",
                  "A decline that keeps the relationship and the information flowing. Copy, paste, adjust.",
                  """Hi Gerald, thanks for the invite. I'm protecting focus time this
quarter for the Q3 forecast, so I'll skip the live session.

My update:
  • Forecast v4 shipped to Ops on 12 Mar
  • Next: Substation 14 capacity check (due 21 Mar)
  • Blocker: none

If there's a decision you need from me, send it my way and I'll
reply the same day."""),
            trial=[
                ("You're invited to a recurring 60-minute meeting “for visibility”. What do you send?",
                 "The Agenda Rune: ask what they need from you. If the answer is “nothing really, just to stay informed”, offer to read the notes instead."),
                ("Your own team meeting has started to drift. How do you tell?",
                 "Ask yourself: what did we decide last week? If nobody can answer, it's a Lich. Add a decisions section to the notes, or shorten it."),
                ("A VP attends the Sync once a quarter. Can you kill it?",
                 "Not on your own. Propose the Mercy Kill (pause with a review date) to the organiser and let them take it to the VP. Gerald gets to own the efficiency win."),
            ],
            last_word="A meeting without a decision is just a group call with extra steps.",
        ),
        # ------------------------------------------------------------------ 3
        dict(
            slug="gaslight-wraith",
            name="The Gaslight Wraith", sigil="☁",
            epithet="“I never said that.” (It did. You were there.)",
            threat=5, habitat="verbal agreements, hallway chats, calls with no notes",
            weakness="the written recap, sent within the hour",
            summary="The Gaslight Wraith denies agreements and rewrites history. The written-recap counter-spell, the paper trail, and when it stops being a creature and becomes a case.",
            sighting=f"""<p>On the 9th of April, in the lift, Rhona told Pip to “pause the substation analysis and put
everything on Lumen meter data.” Pip did. On the 23rd, in the Lumen review, Rhona asked in front of nine people
why the substation analysis was late. “I never said to pause it. I'd never say that.”</p>
<p>Pip opened his mouth and found nothing in it but the memory of a lift, and a lift is not evidence.</p>""",
            know=f"""<p>Some Wraiths do it on purpose, to dodge blame. Most don't: they change their mind, forget, and
then <b>sincerely</b> remember the version where they were right. Memory is not a recording; it is rewritten
every time we recall it, usually in our own favour.</p>
<p>It does not matter which kind you face. The cure is the same: <b>a shared written record</b>, made at the time,
that both of you saw. The Wraith is a creature of fog. Paper does not fog.</p>
{note("If someone repeatedly denies things you both know happened and it is making you doubt your own memory, that is not a quirk. Keep notes, tell someone you trust, and read the Hell difficulty below.")}""",
            omens=[
                "Big decisions are made in lifts, corridors and “quick calls”.",
                "They never put instructions in writing.",
                "“That's not what I meant” follows every problem.",
                "You start recording things in your head “just in case”.",
                "Colleagues tell you, quietly, “oh, she does that”.",
            ],
            counters=[
                ("The Binding Recap", "After any spoken instruction, send a short written recap within the hour. Make it friendly and ask them to correct it. Silence becomes agreement.",
                 "“Just to check I've got it right from our chat: pause the substation analysis, all hands on Lumen meter data until 30 April. Shout if I misunderstood!”"),
                ("The Shared Ledger", "Keep decisions in one shared place everyone can see: the project's decision log, the ticket, the meeting notes. Not your private notebook.",
                 "“I've added it to the Lumen decision log, item 14, so the team sees the change too.”"),
                ("The Gentle Mirror", "When it happens, show the record without accusing. Curious, not triumphant.",
                 "“I may have misread it. Here's my note from the 9th, I'll forward it. Shall we decide now which comes first?”"),
            ],
            forbidden=[
                ("The Secret Recording", 5, "Recording calls without consent. In many places it's illegal, everywhere it's a trust bomb, and you will be the story instead of them."),
                ("The Gotcha Reply-All", 4, "Forwarding the proof to the whole project with “as you can see below”. You win the argument and lose every future conversation."),
                ("Doubting Yourself Into Silence", 3, "Deciding you must have got it wrong, again. This is what feeds the Wraith. Write it down instead."),
            ],
            difficulty=dict(
                normal="A forgetful colleague. Recaps fix it within two weeks, and they will probably thank you for them.",
                nightmare="A pattern under pressure: they rewrite history whenever something slips. Recap everything, use the shared ledger, and raise the pattern with your manager using dates, not adjectives.",
                hell="Deliberate and targeted: it's making you doubt yourself, and it's affecting your review. Keep a private dated log, keep copies of the recaps, speak to your manager's manager or HR, and talk to someone outside work. This is a case, not a creature.",
            ),
            stats=[4, 3, 4, 5, 4, 3, 5, 4, 5], stats_for="The Binding Recap",
            loot=("The Binding Recap",
                  "Sent within the hour of any spoken instruction. Friendly tone, clear facts, an invitation to correct.",
                  """Subject: Quick recap: our chat this morning

Hi Rhona, thanks for the quick chat. Writing it down so I don't
get it wrong:

  1. Pause the substation analysis (back on it 1 May)
  2. Lumen meter data is top priority until 30 April
  3. I'll update the team board today

If I've misunderstood anything, just reply and I'll fix it.
Pip"""),
            trial=[
                ("Your manager gives you a new priority in passing at the coffee machine. What do you do next?",
                 "The Binding Recap, within the hour. Not because you distrust them, but because coffee-machine priorities are the first to be forgotten."),
                ("In a meeting, the Wraith says “I never said that.” You have the recap. What now?",
                 "The Gentle Mirror: “I may have misread it, my note says X, I'll forward it.” Then move the meeting on to deciding what happens now. Win the decision, not the argument."),
                ("The Wraith never replies to recaps. Does the recap still count?",
                 "Yes. A dated recap they received and didn't correct is a strong record. Keep it in the shared ledger as well, so it isn't just between the two of you."),
            ],
            last_word="Fog can't argue with a timestamp.",
        ),
        # ------------------------------------------------------------------ 4
        dict(
            slug="bulldozer-ogre",
            name="The Bulldozer Ogre", sigil="⚒",
            epithet="Speaks first, loudest and longest. Hears no one.",
            threat=3, habitat="brainstorms, workshops, any meeting with a whiteboard",
            weakness="structure: rounds, timers and the written word",
            summary="The Bulldozer Ogre talks over everyone and steamrolls meetings. Counter-spells for getting the floor back and for running meetings the Ogre can't flatten.",
            sighting=f"""<p>In the Lumen pricing workshop on the 14th of May, Brett from Commercial interrupted Pip four
times in eleven minutes. On the fifth attempt Pip got as far as “I think the off-peak data shows—” before Brett
said “Right, so what I'm hearing is,” and then described an idea that was not what he was hearing at all.</p>
<p>The workshop produced Brett's plan. Six people left with ideas they never said out loud. One of them was right.</p>""",
            know=f"""<p>The Ogre is often not trying to dominate. It thinks out loud, fast, and confuses
<b>volume with contribution</b>. It was probably rewarded for it: in many offices the confident talker gets
promoted, and the quiet expert gets “needs to speak up more” in their review.</p>
<p>Ogres are weak against <b>structure</b>. Open discussion is their home ground. Take the meeting off their
ground: written input first, rounds, timers, a facilitator. Ogres don't do well in a queue.</p>
{note("Interrupting is a habit, not a character. Habits respond to friction. Add friction.")}""",
            omens=[
                "“Sorry, just to jump in—” (they are not sorry, and they are not jumping, they live there).",
                "Your ideas come back to you in their voice, ten minutes later.",
                "Quiet people stop attending.",
                "Every meeting ends with their plan.",
            ],
            counters=[
                ("The Held Ground", "When interrupted, keep going calmly, slightly louder, with their name. Don't stop, don't apologise.",
                 "“Brett, let me finish this point, then I want your view.”"),
                ("The Circle of Turns", "If you run the meeting, use rounds: everyone gets two minutes, in order, no replies until the round ends.",
                 "“Let's go round the table first, two minutes each, no comments until everyone's spoken.”"),
                ("The Silent Scrolls", "Start with five minutes of silent writing. Ideas go on sticky notes or a shared doc before anyone speaks. The Ogre can't talk over a Post-it.",
                 "“Before we discuss, five minutes: write your top idea on a note.”"),
                ("The Pre-Meeting Ally", "Agree with an ally beforehand to hand the floor back to each other.",
                 "“I think Pip was in the middle of something about off-peak data?”"),
            ],
            forbidden=[
                ("The Ogre Duel", 3, "Out-shouting the Ogre. Now there are two Ogres and the meeting is a nature documentary."),
                ("The Sulk of Silence", 2, "Giving up and saying nothing for the rest of the quarter. Your review will say “needs to contribute more in meetings”."),
                ("The Mockery Rune", 3, "An eye-roll to the room. Ogres are bad at listening but excellent at noticing contempt."),
            ],
            difficulty=dict(
                normal="An enthusiastic talker. The Held Ground once or twice, and a private word (“I had more to say on Tuesday, can I finish next time?”) fixes it.",
                nightmare="A senior Ogre who runs the room. You can't set the format, so use the Silent Scrolls by sending your idea in writing before the meeting, with your name on it.",
                hell="The Ogre is your manager. Put key ideas in writing first, ask for 1:1 time where volume doesn't win, and find a sponsor who will hand you the floor.",
            ),
            stats=[3, 4, 3, 2, 3, 4, 5, 5, 4], stats_for="The Held Ground",
            loot=("The Meeting Charm",
                  "Four lines to paste at the top of any agenda you own. The Ogre cannot object to a rule that applies to everyone.",
                  """HOW WE RUN THIS (30 min)
  1. 5 min   silent writing: your top idea on a note
  2. 15 min  one round, 2 min each, no replies until the round ends
  3. 8 min   open discussion
  4. 2 min   decision + owner, read out loud"""),
            trial=[
                ("The Ogre interrupts you for the third time. What exactly do you say?",
                 "Use their name and keep going: “Brett, let me finish, then I want your view.” Calm, a bit louder, no apology."),
                ("You're running a workshop with two Ogres and four quiet engineers. What's your format?",
                 "The Meeting Charm: silent writing first, then rounds. The quiet engineers' ideas are on the wall before anyone can talk over them."),
                ("The Ogre repeats your idea as their own. Spell?",
                 "Link it back, warmly: “Yes, building on what I said earlier about off-peak data…” Then see the Credit Vampire, entry 1."),
            ],
            last_word="You don't have to be louder. You have to be harder to interrupt.",
        ),
        # ------------------------------------------------------------------ 5
        dict(
            slug="passive-aggressive-poltergeist",
            name="The Passive-Aggressive Poltergeist", sigil="✉",
            epithet="Rattles the inbox. Never appears in person.",
            threat=2, habitat="email, the kitchen noticeboard, shared calendars",
            weakness="a friendly, direct conversation in person",
            summary="The Passive-Aggressive Poltergeist haunts your inbox with “per my last email” and kitchen notes. How to move the fight from text to a real conversation.",
            sighting=f"""<p>On the 2nd of June, Pip booked meeting room 14B without the online form. At 09:04 he received an
email from Felicity in Facilities, copied to his manager, the floor warden and something called <i>FAC-ALL</i>:</p>
<p><i>“Hi Pip! 😊 Just a gentle reminder, as per the policy (attached again for convenience), that rooms are booked
via the form. I'm sure it was an oversight! Kind regards, Felicity.”</i></p>
<p>The smiley was the worst part. Pip felt it look at him.</p>""",
            know=f"""<p>The Poltergeist is angry and has decided it is not allowed to be. So the anger leaks out sideways:
through politeness that bites, CCs that sting, and notes in the kitchen about whose mug this is.</p>
<p>It usually comes from feeling unheard or powerless. Facilities is blamed for every cold room and broken lift;
email is the one place Felicity can be in charge. Understanding that won't make the smiley less sharp. It will
tell you what works: the Poltergeist <b>needs to be heard</b>, and it can't stand being treated like a person.</p>
{note("“Per my last email” means “read my emails, you fool”. “Kind regards” is 20% kind. “Thanks in advance” means you no longer have a choice.")}""",
            omens=[
                "“Per my last email…” “As previously mentioned…” “Just circling back…”",
                "Your manager is copied on something small.",
                "A smiley that does not reach the eyes.",
                "A laminated sign in the kitchen, in bold, about you.",
            ],
            counters=[
                ("The Summoning to the Flesh", "Move it off email. Walk over or call. Poltergeists are bold in text and gentle in person.",
                 "“Hi Felicity, I got your email, sorry about 14B. Have you got two minutes so I understand the booking problem?”"),
                ("The Literal Reply", "Reply only to the content, cheerfully, as if the tone weren't there. You can't fight with someone who doesn't take the bait.",
                 "“Thanks Felicity, my mistake, I'll use the form from now on. Have a good day!”"),
                ("The Uncopying", "When your manager was copied, reply to the sender only, with the friendly literal reply. Never reply-all to a poltergeist.",
                 None),
                ("The Name for It", "When it's a pattern with a peer, name it once, kindly, in private.",
                 "“I've noticed some of our emails get a bit tense. Can we just talk when something bugs you? I'd much rather know.”"),
            ],
            forbidden=[
                ("The Counter-Haunting", 3, "Replying in the same style. “Per YOUR last email.” It's satisfying for one second and screenshotted forever."),
                ("The Escalation Spiral", 3, "Adding your manager because they added yours. Now there are four managers reading about a meeting room."),
                ("The Anonymous Kitchen Note", 4, "Fighting the sign with a sign. You are now a Poltergeist too. The kitchen is lost."),
            ],
            difficulty=dict(
                normal="A bad day in text form. The Literal Reply ends it.",
                nightmare="A pattern: every slip gets a CC'd email. The Summoning to the Flesh, then the Name for It. Most of the time, the emails soften within weeks.",
                hell="The Poltergeist is building a paper case against you, CC'ing HR on trivia. Keep your own calm replies, never match the tone, and let your manager know early, so the CCs land on someone who's already heard your side.",
            ),
            stats=[4, 2, 5, 3, 5, 4, 5, 5, 5], stats_for="The Literal Reply",
            loot=("The Cool Water Reply",
                  "Reply to the content, never the tone. Sender only. Done in thirty seconds.",
                  """Hi Felicity,

Thanks for flagging, that's on me. I'll use the booking form
from now on.

Have a good day,
Pip"""),
            trial=[
                ("A colleague emails you with “as I mentioned twice before” and copies your manager. First move?",
                 "Reply to them only, with the facts and no tone. Then, if it matters, walk over or call. Never reply-all."),
                ("Your manager asks why Facilities is emailing about you. What do you say?",
                 "One line, calm: “I booked a room without the form, my mistake, I've apologised and it's sorted.” Owning a small slip makes you look bigger than the email."),
                ("Is a passive-aggressive kitchen sign ever worth answering?",
                 "Only by fixing the problem (wash the mug). Never by another sign."),
            ],
            last_word="The tone is their problem. The facts are yours. Answer the facts.",
        ),
        # ------------------------------------------------------------------ 6
        dict(
            slug="coasting-zombie",
            name="The Coasting Zombie", sigil="☕",
            epithet="Does nothing. Survives everything.",
            threat=2, habitat="shared projects, group tasks, any work with more than one owner",
            weakness="named owners and visible deadlines",
            summary="The Coasting Zombie does nothing and somehow survives every reorg. How to stop carrying their work, with clear owners, visible deadlines and no martyrdom.",
            sighting=f"""<p>Neville has been in Asset Records for fourteen years and has survived six reorgs. In March he
was given half of the Lumen asset clean-up: 40,000 meter records to check. In June, Pip noticed that his own
half was done and Neville's half was “in progress”, as it had been since March.</p>
<p>Pip quietly did 8,000 of Neville's records over two weekends. At the July review, the clean-up was praised as
“a real team effort”. Neville nodded wisely. He had, in a sense, been on the team.</p>""",
            know=f"""<p>Some Zombies are lazy. Many are not: they are <b>burnt out, bored, disengaged</b> or quietly
dealing with something at home. A few have learned that in a big company, work given to “the team” always gets
done by someone. Usually by someone like Pip.</p>
<p>The Zombie survives because nobody can see what it does or doesn't do. Shared ownership is its natural
habitat. Your job is not to judge or fix it. Your job is to <b>stop absorbing</b> its work silently.</p>
{note("Every weekend you spend doing a Zombie's work is a weekend that proves to the company the Zombie isn't a problem.")}""",
            omens=[
                "Their status is always “in progress”, never a number.",
                "Work given to “the team” lands on you.",
                "They are always busy, and nobody knows with what.",
                "You start doing their part “to be safe”.",
            ],
            counters=[
                ("The Naming of Owners", "Every task gets one named owner and a date, in a place everyone can see. “The team” cannot own anything.",
                 "“Shall we split it on the board? Neville: records 20,001 to 40,000, done by 30 April. Me: 1 to 20,000.”"),
                ("The Friendly Check-in", "Ask early, kindly and specifically. Sometimes the Zombie is stuck and ashamed to say so.",
                 "“How's your half going? If something's blocking you, I'm happy to look at it together for half an hour.”"),
                ("The Honest Status", "In status updates, report facts by owner. No covering, no blaming.",
                 "“My half is done. Neville's half is at 15%. At this pace we'll finish mid-August, not June.”"),
                ("The Escalation by Numbers", "If the date is at risk, tell your manager with numbers and a choice, not a complaint.",
                 "“The clean-up will miss June by about six weeks. Options: move the date, add someone, or cut scope. Which do you prefer?”"),
            ],
            forbidden=[
                ("The Silent Martyr", 3, "Doing their work in secret. You burn out, they get praised, and next time you'll get both halves officially."),
                ("The Public Shaming", 4, "“Some of us actually work” in the team chat. Now you're the problem."),
                ("The Zombie's Path", 3, "Deciding that if they can coast, so can you. Zombies who survive have fourteen years of relationships. You have eight months."),
            ],
            difficulty=dict(
                normal="A colleague who's overloaded or stuck. The Friendly Check-in solves it, and you may gain an ally.",
                nightmare="A known coaster the team works around. Named owners and Honest Status make it visible. Visibility is your whole job here; the rest is your manager's.",
                hell="The Zombie is protected (friend of the director, untouchable). Protect yourself: named owners, dated records, and never quietly take on their work. If the project fails, the record shows why.",
            ),
            stats=[4, 3, 4, 4, 4, 3, 5, 4, 4], stats_for="The Naming of Owners",
            loot=("The Owner Board",
                  "A five-column table for any shared task. Paste it at the top of the project page.",
                  """TASK                      OWNER     DUE      STATUS   BLOCKER
Asset records 1–20,000    Pip       30 Apr   100%     –
Asset records 20,001–40k  Neville   30 Apr   15%      ?
Exceptions report         Pip       15 May   0%       needs both halves
Sign-off                  Rhona     20 May   –        –"""),
            trial=[
                ("You're asked to “work with Neville on it”. What's your first move?",
                 "Split it into named halves with dates, on a board both of you and your manager can see. Today, not when it's late."),
                ("It's two weeks before the deadline and their half is at 15%. You could finish it over the weekend. Should you?",
                 "No, not silently. Report the facts and options to your manager first. If you then agree to help, it's visible help, not invisible rescue."),
                ("How do you tell a Zombie from a colleague who's struggling?",
                 "You usually can't from outside. That's why the Friendly Check-in comes first. Treat them as stuck until proven otherwise."),
            ],
            last_word="Help openly or not at all. Secret rescue is just unpaid overtime with extra resentment.",
        ),
        # ------------------------------------------------------------------ 7
        dict(
            slug="doppelganger",
            name="The Doppelgänger", sigil="⚭",
            epithet="Lovely to your face. A different creature in rooms you're not in.",
            threat=5, habitat="1:1s with your manager, calibration meetings, the pub after work",
            weakness="witnesses, consistency, and your own relationships",
            summary="The Doppelgänger is friendly to your face and undermines you behind your back. How to confirm it, protect yourself without paranoia, and make backstabbing expensive.",
            sighting=f"""<p>Saskia is Pip's peer and favourite person in Grid Planning. She brings him cardamom buns. She
says his forecast work is “honestly the best in the team”. On the 11th of September, Pip's manager mentioned,
gently, that “some people” felt Pip “didn't really collaborate” and was “a bit precious about his models”.</p>
<p>Pip had collaborated with exactly one person that quarter. She had brought buns.</p>""",
            know=f"""<p>The Doppelgänger is <b>competing</b> with you, usually for the same promotion, budget or
reputation, and has decided that open competition is too risky. So it is warm in public, where warmth is
rewarded, and undermining in private, where nobody checks.</p>
<p>Two cautions. First, <b>don't jump to it</b>: feedback that hurts is not proof of a traitor, and most
colleagues are exactly what they seem. Second, if it's real, you will not beat it by being a better spy. You beat
it by having <b>your own relationships</b>, so that when your name comes up, other people already know you.</p>
{note("The cure for whispering is not a louder whisper. It's people who know you well enough not to believe it.")}""",
            omens=[
                "Feedback about you arrives vague and second-hand: “some people feel…”.",
                "Your manager seems to know things you only told one person.",
                "Their praise is always private, their concerns always in groups.",
                "They are often in the room when your work is discussed and you are not.",
            ],
            counters=[
                ("The Clarifying Question", "When vague feedback arrives, ask for specifics. It tests whether it's real and whether it's fair.",
                 "“Thanks for telling me. Can you give me an example, so I can fix it? Which project was it?”"),
                ("The Wide Web", "Build direct relationships with your manager, skip-level and the people who use your work. Then nobody's opinion of you comes only through one voice.",
                 "“I'd love a monthly half-hour with you to hear how the forecasts are landing for Ops.”"),
                ("The Open Hand", "Bring collaboration into the open: invite them into your work visibly, credit them in writing. It's hard to call you precious when there's an email thread of you sharing.",
                 "“Saskia, want to co-present the model method at the team review? You know the data well.”"),
                ("The Quiet Test", "Tell them something harmless and specific, then see where it reappears. Use once. It's a test, not a hobby.",
                 None),
            ],
            forbidden=[
                ("The Counter-Whisper", 5, "Undermining them back. Now there are two Doppelgängers and your manager trusts neither."),
                ("The Confrontation Ambush", 4, "Accusing them in front of others with no evidence. They will be shocked and hurt, convincingly. You will look paranoid."),
                ("The Bunker", 3, "Trusting nobody, sharing nothing. You will become exactly what they said you were: precious and unco-operative."),
            ],
            difficulty=dict(
                normal="A misunderstanding: a peer gave honest, clumsy feedback. Ask for examples, fix what's fair, move on.",
                nightmare="A rival with a habit. Widen your web, collaborate in writing, keep your work in daylight. Over a few months the whispers stop matching what people see.",
                hell="A skilled operator who has your manager's ear. Build your skip-level relationship, ask your manager directly for specific examples, keep a record of your collaboration, and consider whether this team can be won.",
            ),
            stats=[3, 4, 3, 4, 4, 5, 5, 3, 4], stats_for="The Wide Web",
            loot=("The Map of Allies",
                  "A list you keep for yourself. Five names, one line each, reviewed monthly. If a column is empty, that's your next coffee.",
                  """PERSON          WHY THEY MATTER          LAST REAL CONVO   NEXT STEP
My manager      writes my review         3 Sep             monthly 1:1
Skip-level      calibration room         never!            ask for 20 min
Ops lead        uses my forecasts        28 Aug            demo v5
Trading desk    uses my forecasts        July              coffee
A peer outside  honest outside view      12 Sep            lunch"""),
            trial=[
                ("Your manager says “some people” find you hard to work with. What do you say first?",
                 "Thank them, then ask for a specific example. Don't guess who said it out loud; it makes you look defensive and is often wrong."),
                ("You're fairly sure who it is. Do you confront them?",
                 "Not with an accusation. You can say: “I heard there's a concern about how we work together. If anything bugs you, I'd rather hear it from you.” It tells them you know, without a scene."),
                ("What's the long-term cure?",
                 "The Wide Web. When your manager, skip-level and users know you directly, one voice behind your back loses most of its power."),
            ],
            last_word="You can't stop someone talking about you. You can make sure they're not the only one.",
        ),
        # ------------------------------------------------------------------ 8
        dict(
            slug="martyr-banshee",
            name="The Martyr Banshee", sigil="♫",
            epithet="Wails of overwork. Refuses all help.",
            threat=2, habitat="Network Operations, Slack status “drowning 🫠”, the late-night email",
            weakness="concrete offers of help, and saying yes to “no”",
            summary="The Martyr Banshee complains of overwork but refuses all help. How to respond without being dragged into the wailing, and how to tell it from real burnout.",
            sighting=f"""<p>Morag in Network Operations sends emails at 23:58. Her Slack status has said “drowning 🫠” since
February. In every meeting she mentions that she hasn't had lunch since 2023. When Pip offered to take the weekly
outage report off her plate, she said: “No, no, it's quicker if I do it. Nobody else knows the system.”</p>
<p>At the next team meeting she said nobody ever offers to help.</p>""",
            know=f"""<p>The Banshee's identity is built on being <b>indispensable</b>. Being overworked is proof she
matters. Letting go of a task would be a relief and a threat at the same time: if someone else can do it, what is
she for? So she wails, and refuses.</p>
<p>Be careful: <b>the Banshee may also be genuinely burning out</b>. The wailing is real pain dressed as
complaint. Treat the person kindly and the pattern firmly. You can't fix her workload. You can stop being part of
the chorus.</p>
{note("The Banshee's wail is contagious. Spend a month next to one and you'll start sending emails at midnight to prove you care too. Don't.")}""",
            omens=[
                "Late-night emails that are not urgent.",
                "“Nobody else can do it” about tasks that are written down somewhere.",
                "Offers of help refused, then lack of help complained about.",
                "The team starts competing over who is busiest.",
            ],
            counters=[
                ("The Specific Offer", "Vague help is easy to refuse. Offer one specific task with a time.",
                 "“I can do the outage report this Friday. You review it Monday, ten minutes. Want to try once?”"),
                ("The Teach-Me Spell", "Ask to learn the task, not take it. Being the teacher keeps her important.",
                 "“Could you show me how the outage report works? Then you've got backup when you're on leave.”"),
                ("The Kind Boundary", "Sympathise without joining the chorus or taking on everything.",
                 "“That sounds like a lot. I can't take on more this week, but I'm free Thursday afternoon if something specific would help.”"),
                ("The Wellbeing Flag", "If it looks like real burnout, say so kindly, in private, and point to support.",
                 "“You seem really stretched lately. Is it worth raising the workload with Hugo? I'd back you up.”"),
            ],
            forbidden=[
                ("The Busy Duel", 3, "Out-martyring the Banshee. “You think you're busy? I haven't seen daylight since March.” Now the whole team is competing in suffering."),
                ("The Eye-Roll Chorus", 3, "Mocking her behind her back. She might be one bad week from collapse. You'll feel terrible, and you'll deserve to."),
                ("The Rescue Fantasy", 2, "Taking over all her work to save her. She'll resent it, and you'll become the next Banshee."),
            ],
            difficulty=dict(
                normal="A busy colleague letting off steam. Listen for a minute, offer one specific thing, move on.",
                nightmare="A team pattern: overwork as status. Model the opposite: leave on time, share tasks visibly, praise people for handing over, not holding on.",
                hell="It's your manager, and the wail becomes an expectation for everyone. Protect your hours with clear availability, deliver well inside them, and read Act VIII, the Slow Hex of Burnout.",
            ),
            stats=[4, 2, 4, 2, 5, 4, 5, 4, 5], stats_for="The Specific Offer",
            loot=("The Specific Offer",
                  "Help that's hard to refuse: one task, one date, one small review. Adjust and send.",
                  """Hi Morag, I've got some room on Friday. Could I take this
week's outage report?

  • I'll draft it from the dashboard by Friday 3 pm
  • You check it Monday (10 min, I'll mark anything I'm unsure of)
  • If it works, we alternate weeks

If not this week, no worries, the offer stands."""),
            trial=[
                ("The Banshee says “nobody ever helps” right after refusing your help. What do you say?",
                 "Calmly, without scorekeeping: “I'd still love to take the outage report one week. Want to try this Friday?” Repeat the specific offer, not the grievance."),
                ("How do you tell a Banshee from real burnout?",
                 "Often you can't, and it can be both. Look for changes: more mistakes, withdrawal, illness, emotion. If you see them, use the Wellbeing Flag instead of a spell."),
                ("Your team has started competing over who works latest. What do you do?",
                 "Don't join. Leave on time, visibly, and say so: “Logging off, back at 8.” Someone has to go first. Others are often waiting for permission."),
            ],
            last_word="Busy is not a personality. Neither is tired. Go home.",
        ),
        # ------------------------------------------------------------------ 9
        dict(
            slug="know-it-all-basilisk",
            name="The Know-It-All Basilisk", sigil="◉",
            epithet="One glance at your idea and it turns to stone.",
            threat=3, habitat="architecture reviews, technical forums, the comments on your doc",
            weakness="data, questions, and being invited to own part of the answer",
            summary="The Know-It-All Basilisk dismisses every idea that isn't theirs. How to survive the stare with data, questions and by making the expert part of your idea.",
            sighting=f"""<p>Dr. Lionel Ashe, principal engineer, was right in 2011 about the transformer replacement
programme, and has been reminding people ever since. When Pip presented a simple machine-learning model for
predicting transformer failures, Lionel did not look up from his laptop. “That won't work. We've got thirty years
of physics for this. Next.”</p>
<p>The idea was turned to stone in four seconds. It had taken Pip three months.</p>""",
            know=f"""<p>The Basilisk is usually <b>genuinely expert</b>, and that's the problem. Its identity rests on
being the one who knows. New ideas from junior people are a threat to that identity, so it kills them on sight,
before they can grow.</p>
<p>The trick: <b>don't look it in the eye</b>. Don't challenge its expertise; use it. A Basilisk invited to
improve an idea will often defend it fiercely, because now it's partly theirs.</p>
{note("The Basilisk is right more often than you'd like. Listen for the 20% that's true before you dismiss the 80% that's rude.")}""",
            omens=[
                "“We tried that.” “That won't scale.” “Next.”",
                "They answer questions nobody asked, at length.",
                "Juniors stop proposing anything in their meetings.",
                "They reply to your 12-page doc after reading the title.",
            ],
            counters=[
                ("The Mirror Shield", "Answer with data, not opinion. Ask what evidence would change their mind.",
                 "“Fair challenge. On the 2018–2024 data the model caught 31 of 38 failures. What would you need to see to trust it?”"),
                ("The Apprentice's Question", "Ask for their expertise before the meeting. People rarely destroy what they helped build.",
                 "“Lionel, before I present, could you poke holes in this? You know the physics better than anyone.”"),
                ("The Small Pilot", "Propose a small, safe test instead of a big change. Basilisks hate risk more than they hate new ideas.",
                 "“Could we run it in shadow mode on twenty transformers for three months? No decisions on it, just a comparison.”"),
            ],
            forbidden=[
                ("The Stare-Down", 4, "Challenging their expertise in public. “Actually, physics models are outdated.” They have a doctorate and twenty years. You have a notebook."),
                ("The Workaround", 3, "Building it anyway behind their back. When it's discovered, the fight is no longer about the idea, it's about trust."),
                ("Turning to Stone", 2, "Giving up on all ideas. You'll be safe and invisible, which at MetroVolt is how people become Neville."),
            ],
            difficulty=dict(
                normal="A confident expert having a rushed day. Ask for specifics and offer data later. Usually fine on the second try.",
                nightmare="Kills every new idea on sight. The Apprentice's Question before every proposal, and Small Pilots to build a track record.",
                hell="The Basilisk owns the decision and won't move. Find a sponsor above them who cares about the outcome, run the safest possible pilot, and let the results argue for you.",
            ),
            stats=[3, 5, 3, 3, 4, 5, 5, 3, 4], stats_for="The Apprentice's Question",
            loot=("The Pre-Review Ask",
                  "Send to the expert a week before you present. It turns a judge into a co-author.",
                  """Hi Lionel,

I'm presenting a transformer-failure model at the asset review on
the 14th. Before I do, I'd really value your eyes on it:

  1. Is there a failure mode the data can't see? (you'll know)
  2. Where would you not trust it?
  3. What test would convince you?

20 minutes any day next week? Coffee's on me."""),
            trial=[
                ("The Basilisk says “that won't work” and moves on. What do you say?",
                 "“Fair. What's the main reason?” Then write it down. Either you learn something real, or they have to say something specific you can test."),
                ("You have a new idea in their area. Who do you talk to first?",
                 "The Basilisk, privately, with the Pre-Review Ask. Never let them see it for the first time in front of an audience."),
                ("They're partly right: the model misses one failure type. What now?",
                 "Say so, credit them, and add it. “Lionel spotted the moisture failure mode, so we've added it.” Your idea just got their name on it, and their defence."),
            ],
            last_word="Don't fight the expert. Recruit them. Then they fight for you.",
        ),
        # ------------------------------------------------------------------ 10
        dict(
            slug="doom-prophet",
            name="The Doom Prophet", sigil="☄",
            epithet="“We tried that in 2014. It failed.”",
            threat=2, habitat="the Control Room, kick-offs, the back row of every town hall",
            weakness="turning prophecy into a risk register",
            summary="The Doom Prophet predicts failure for every new idea. How to turn the pessimism into useful risk-spotting instead of letting it drain the room.",
            sighting=f"""<p>Terrence has worked in the Control Room since the 2009 blackout. When Pip proposed automated
alerts for substation overloads, Terrence sighed the sigh of a man who has seen empires fall. “We tried
automation in 2014. Alarms went off for three weeks straight. Nobody slept. It'll fail.”</p>
<p>Then he told the story of 2014 for nineteen minutes. It was, to be fair, a very good story.</p>""",
            know=f"""<p>The Prophet is not a pessimist by nature. It is a <b>survivor</b>. It has watched good ideas fail
for reasons nobody wrote down, and it remembers every one. Its doom is pattern-matching, done out loud, with
feeling.</p>
<p>That makes it <b>the most underused risk expert in the building</b>. The problem isn't the warning; it's that
the warning comes as a verdict (“it'll fail”) instead of a risk (“it failed because of X”). Convert the verdict,
and the Prophet becomes useful.</p>
{note("The Doom Prophet is wrong about the conclusion and often right about the reasons. Steal the reasons.")}""",
            omens=[
                "“We tried that.” “It never works here.” “Give it six months.”",
                "History lectures with no question at the end.",
                "New joiners stop suggesting things after week three.",
                "They are sometimes, annoyingly, right.",
            ],
            counters=[
                ("The Transmutation", "Turn the prophecy into specific risks. Ask what went wrong last time, and write each answer down as a risk.",
                 "“That's really useful. What exactly went wrong in 2014? I want to make sure we don't repeat it.”"),
                ("The Prophet's Seat", "Give them a role: official risk reviewer. Their doom now has a job.",
                 "“Terrence, would you be our devil's advocate at the design review? Nobody knows the failure modes like you.”"),
                ("The Pre-Mortem", "Run a session where the team imagines the project has failed and lists why. The Prophet will shine, and it's all on the whiteboard.",
                 "“Imagine it's a year from now and the alerts failed. What happened?”"),
            ],
            forbidden=[
                ("The Dismissal", 3, "“That was 2014, things are different now.” Maybe. But you've just told the person who knows where the bodies are buried that you don't want the map."),
                ("The Hype Shield", 2, "Answering doom with forced optimism. Now you're the Toxic Positivity Siren (entry 11), and the Prophet has a new story."),
                ("The Exclusion", 3, "Leaving them out of planning to avoid the negativity. They'll find out, and the prophecy becomes a mission."),
            ],
            difficulty=dict(
                normal="A cautious colleague. One Transmutation question and you have a list of useful risks.",
                nightmare="Kills momentum in every meeting. Give them the Prophet's Seat, a fixed time to raise risks, and the rest of the meeting moves.",
                hell="The Prophet is senior and their doom shapes decisions. Address each risk in writing, run a small pilot to beat the 2014 failure, and let the result update the story.",
            ),
            stats=[4, 4, 4, 4, 4, 5, 5, 4, 5], stats_for="The Transmutation",
            loot=("The Prophecy Register",
                  "Turn every “it'll fail” into a row. Show the Prophet the register: their warnings are in it, with owners.",
                  """WARNING (from Terrence)           RISK                         WHAT WE'LL DO
“Alarms ran 3 weeks straight”     alert flood, operators mute   thresholds tuned on 2 yrs data,
                                                                max 5 alerts/hr per desk
“Nobody owned the rules”          stale thresholds             monthly review, owner: Control Room
“Vendor vanished after go-live”   no support                   support clause in contract"""),
            trial=[
                ("In the kick-off, the Prophet says “this will fail like 2014”. What's your reply?",
                 "The Transmutation: “What went wrong in 2014? I want to avoid it.” Write the answers down where everyone can see them."),
                ("The Prophet's story runs 19 minutes. How do you keep the meeting on track?",
                 "Thank them, capture the key risks in one line each, and offer a separate session: “This is gold. Can we go deeper on Thursday so we can finish the agenda now?”"),
                ("Six months later the project succeeds. What do you do?",
                 "Thank the Prophet publicly for the risks they caught. Next time they'll warn you earlier and grumble less."),
            ],
            last_word="Every prophet of doom is a risk register that hasn't been asked nicely.",
        ),
        # ------------------------------------------------------------------ 11
        dict(
            slug="toxic-positivity-siren",
            name="The Toxic Positivity Siren", sigil="✺",
            epithet="Sings of opportunity as the ship goes down.",
            threat=3, habitat="town halls, wellbeing weeks, announcements with too many emojis",
            weakness="calm, specific questions, asked kindly",
            summary="The Toxic Positivity Siren treats every problem as an opportunity and every concern as negativity. How to raise real problems without being labelled negative.",
            sighting=f"""<p>The week after MetroVolt announced a hiring freeze, Kaylee, Head of Employee Joy, launched
<b>Gratitude Fortnight</b>. There was a gong. When Pip asked at the Q&amp;A how teams would cope with six unfilled
roles in Grid Planning, Kaylee smiled. “I love that energy! Let's reframe that as a growth opportunity. 🚀”</p>
<p>The gong was struck. Nobody asked another question.</p>""",
            know=f"""<p>The Siren is not lying. Often it's been <b>told to keep morale up</b>, and has no power to fix the
problem underneath. Positivity is the only tool it has. So it reaches for it, every time, even when the ship has a
hole in it.</p>
<p>The danger is to <b>you</b>: in a Siren culture, people who raise problems get labelled “negative”. The
counter is not to be negative louder. It's to raise problems in a form the song can't drown: <b>calm, specific,
and with a suggestion</b>.</p>
{note("You can be positive about the people and honest about the problem in the same sentence. That's not negativity, it's management.")}""",
            omens=[
                "“No problems, only opportunities!”",
                "Concerns are met with “let's stay positive”.",
                "Bad news arrives with a celebration attached.",
                "People share problems only in private chats.",
            ],
            counters=[
                ("The Both-And Chant", "Agree with the positive, then add the problem. You can't be dismissed as negative if you started with a yes.",
                 "“I'm genuinely glad we're investing in the team. And I'm worried about six open roles in Grid Planning. What can we drop?”"),
                ("The Specific Question", "Ask for a decision or a fact, not a feeling. Siren songs are about feelings.",
                 "“With the freeze, which of our Q4 projects should slow down first?”"),
                ("The Right Ear", "Take the real problem to the person who can fix it, not the one who runs the gong.",
                 "“Could I have 15 minutes with you on the Grid Planning workload? I have a proposal.”"),
            ],
            forbidden=[
                ("The Doom Counter-Song", 3, "Matching the Siren's cheer with gloom. You become the official Negative Person, and everything you say is discounted."),
                ("The Mocking Echo", 3, "“Growth opportunity 🚀” in the team chat, with a skull. It will be screenshotted. Kaylee has feelings and a direct line to the CEO."),
                ("The Swallowed Concern", 2, "Saying nothing. The problem grows, and when it bursts, someone will ask why nobody raised it."),
            ],
            difficulty=dict(
                normal="An upbeat colleague. The Both-And Chant gets you heard and keeps the relationship.",
                nightmare="A culture where concerns are career-limiting. Raise problems with data, with solutions, and to the right ear. Keep a short written record that you raised them.",
                hell="Leadership punishes bad news. Raise serious issues in writing to the person accountable, keep a copy, find allies who see the same thing, and remember Act VIII, the Dark Pact, if it's ever about safety or ethics.",
            ),
            stats=[4, 4, 4, 3, 4, 4, 5, 5, 4], stats_for="The Both-And Chant",
            loot=("The Problem-With-a-Path",
                  "How to raise a problem in a positive culture: good news, the problem, a proposal, an ask. Four lines.",
                  """GOOD      We hit the Q3 forecast within 2%. Team is strong.
PROBLEM   Six roles frozen: two Q4 projects will slip ~8 weeks.
PROPOSAL  Pause the substation dashboard; keep Lumen on track.
ASK       Can you confirm by Friday which one you'd rather keep?"""),
            trial=[
                ("At a town hall, you want to ask about workload after the freeze. How do you phrase it?",
                 "The Both-And Chant plus a Specific Question: “Glad we're keeping the team together. With six frozen roles, which projects should slow down?”"),
                ("You get labelled “a bit negative” in your review. What do you change?",
                 "Keep raising problems, but use the Problem-With-a-Path format, and to the person who can act. Ask your manager for an example of where the tone missed."),
                ("Is it ever right to just be positive?",
                 "Yes: when the problem is small, already known, or nobody can do anything. Pick the problems worth raising."),
            ],
            last_word="Optimism is a strategy. Ignoring the iceberg is not.",
        ),
        # ------------------------------------------------------------------ 12
        dict(
            slug="boundary-goblin",
            name="The Boundary Goblin", sigil="☏",
            epithet="“Quick question, no rush 🙂” (23:47, there is rush)",
            threat=3, habitat="Slack, WhatsApp, your phone at dinner, your holiday",
            weakness="clear, kind, repeated boundaries, and a reply that comes in the morning",
            summary="The Boundary Goblin messages at all hours and expects instant replies. How to set availability boundaries that stick, without looking uncommitted.",
            sighting=f"""<p>Hugo runs Project Lumen and has never been seen offline. His first message to Pip arrived on a
Sunday at 23:47: <i>“Quick q, no rush 🙂 where's the meter data?”</i>. At 23:52: <i>“?”</i>. At 07:10:
<i>“Morning! Any update on last night?”</i></p>
<p>Pip replied at 23:53, because he was awake and it was only a quick question. From then on, Hugo knew Pip was
always available. The Goblin had been fed after midnight. Everyone knows what happens then.</p>""",
            know=f"""<p>The Goblin is rarely a tyrant. It's usually <b>anxious and badly organised</b>: it thinks of things
at night and sends them before it forgets. It often genuinely means “no rush”. But every fast reply teaches it
that you're on call. You trained it. You can untrain it.</p>
<p>Boundaries are not about rules. They're about <b>what you reliably do</b>. If you always reply at 08:30, the
Goblin learns 08:30. Consistency beats speeches.</p>
{note("A boundary you explain but don't keep is just a speech. A boundary you keep without explaining is a habit, and habits are what people learn.")}""",
            omens=[
                "Messages after 21:00, before 07:00 or on holiday.",
                "“No rush” followed by “?” five minutes later.",
                "You feel anxious when you hear a notification at dinner.",
                "You've started replying fast to avoid the follow-up.",
            ],
            counters=[
                ("The Ward of Hours", "Set your hours visibly (Slack status, calendar working hours, email signature) and keep them. Reply at the start of your next working day.",
                 "Slack status: “🕯 Online 08:30–17:30 CET. Urgent outage? Call the Control Room.”"),
                ("The Morning Reply", "Answer late messages in the morning, warmly and fully. No apology for not replying at midnight.",
                 "“Morning Hugo! The meter data is in the Lumen folder, tab 3. Shout if anything's missing.”"),
                ("The Emergency Rune", "Agree with the Goblin what truly urgent means and how to reach you for it. Real emergencies get a call, not a message.",
                 "“If it's genuinely urgent outside hours, call me. Otherwise I'll pick up messages first thing.”"),
                ("Scheduled Send", "If you work late, schedule your own messages for the morning. Don't spawn Goblins of your own.",
                 None),
            ],
            forbidden=[
                ("The Midnight Feed", 3, "Replying at 23:53 “just this once”. Goblins don't remember exceptions. They remember precedents."),
                ("The Furious Lecture", 3, "A long message at 07:00 about respecting boundaries. True, but it reads as an attack, and the Goblin will feel wronged."),
                ("The Total Blackout", 2, "Turning everything off and refusing all contact, even for real emergencies. In a power company, outages happen at 3 a.m. Know which ones are yours."),
            ],
            difficulty=dict(
                normal="A night owl who means “no rush”. The Morning Reply for two weeks, and it learns.",
                nightmare="Expects fast replies and complains when it doesn't get them. Agree the Emergency Rune with them openly, and with your manager if needed.",
                hell="It's your manager, and the culture rewards being always-on. Agree core hours in writing, deliver excellently inside them, and read Act VIII: the Salt Circle and the Slow Hex of Burnout.",
            ),
            stats=[5, 3, 4, 3, 4, 3, 5, 5, 4], stats_for="The Ward of Hours",
            loot=("The Ward of Hours",
                  "Three pieces: a status, an email signature line, and one honest conversation.",
                  """SLACK STATUS
🕯 Online 08:30–17:30 CET · Urgent outage? Call Control Room x4400

EMAIL SIGNATURE
I work 08:30–17:30 CET. If you get this outside those hours,
no need to reply until yours.

THE TALK (once, in person)
“I'm switching off after 18:00 so I'm sharp in the day. If
something's truly urgent, call me. I'll always pick up a call.”"""),
            trial=[
                ("Sunday, 23:47: “Quick q, no rush 🙂”. What do you do?",
                 "Nothing until Monday at 08:30. Then the Morning Reply: warm, complete, no apology."),
                ("The Goblin says “I noticed you didn't reply last night”. Your answer?",
                 "Calmly: “I'm offline after 18:00. If it's urgent, call me and I'll always pick up.” Then keep doing it."),
                ("You're working late yourself and want to send the team a message. How?",
                 "Schedule it for 08:30. Leaders who message at midnight create Goblins, even when they say “no rush”."),
            ],
            last_word="You teach people how to treat you, one reply at a time.",
        ),
    ],
)
