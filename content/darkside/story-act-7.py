# Series 4 · Act VII · the long-form story fields, merged into content/darkside/act-7.py by scripts/grimoire.py.
# May 2029 to March 2030. Pip back at The Grid; Rupert Thorne's Ascend 2030; VoltMind (the AI assistant) for everyone;
# three office days from September 2029; floor 22 closes, floor 14 becomes hot-desks.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the Return-to-Office Decree
    "return-to-office-decree": dict(
        sighting=f"""{beat("Monday 14 May 2029 · the decree")}
<p>An email from Imogen Hale and Rupert Thorne, titled <b>“The way we work together”</b>: from 3 September, everyone in
the office three days a week, Tuesdays included (“Collaboration Tuesdays”). Badge data would be “shared with managers to
support conversations”. Floor 22 would close for “refurbishment”. It has not reopened.</p>
{beat("Tuesday 4 September · the first Collaboration Tuesday")}
<p>Pip left home at 06:00, seventy minutes each way. His team had all picked different days. He spent the day on video
calls with people at home, in a booth, wearing headphones. At 17:00 he worked out he'd spoken to one person in the room:
the man who refilled the coffee machine.</p>
{beat("Wednesday 5 September · the Overlap Pact")}
<p>Pip proposed that the team all come in Tuesdays and Thursdays, and save planning, workshops and lunch for those days.
Everyone agreed in under a minute. Nobody had asked before. Then he made the Honest Ask to Ruth about his third day:
fixed Tuesdays and Thursdays, the third when there was a workshop. Ruth said yes, and that he wasn't the first to ask.</p>
{beat("October · the badge report")}
<p>The first report said Pip averaged 2.6 days. Ruth looked at it, looked at the Overlap Pact, and filed it. In the same
report, three people in another team badged in at 08:58 and out at 09:20 every Friday. Everyone knew. Nobody said anything.
In November their manager did.</p>
{note("A mandate tells you how often to come in. It can't tell you why. Find a why, or make the honest case that there isn't one.")}""",
        origin=dict(
            title="How the decree came down from floor 27",
            beats=[
                ("2020 · the great scattering", "Like everyone, MetroVolt sends everyone home. Work mostly carries on. Some things (onboarding, mentoring, chance conversations) quietly get worse."),
                ("2022 · the hybrid truce", "Teams choose their own patterns. Some thrive. Some never meet. Nobody measures which."),
                ("2028 · the lease", "MetroVolt is paying for thirty floors and using fourteen. The parent group wants either fewer floors or fuller ones. Both, ideally."),
                ("May 2029 · the decree", "Rupert and Imogen combine three real problems (lonely new joiners, empty floors, a CEO who misses the buzz) into one rule for everyone."),
            ],
            turning="Three different problems, solved with one blunt rule, so it solves none of them well.",
            saved="Asking teams what they need the office for, and setting the rule around that.",
            note="Most mandates mix a real problem (people not meeting) with a cost problem (empty floors). Help with the first. Be honest about the second.",
        ),
        know=f"""<p>Return-to-office mandates require people to be in the office a set number of days. Behind them are usually several
reasons at once: collaboration, culture, new joiners, property costs, leadership instinct. The mandate is the same for
everyone; the reasons aren't. Knowing which reason applies to you changes how you should respond.</p>
<h3 class="kh">What it wants</h3>
<p>People together, visibly. Sometimes for collaboration; sometimes for the building; sometimes because leaders feel better seeing people.</p>
<h3 class="kh">Why it's enforced with badges</h3>
<p>Because it's easy to count. Collaboration isn't. So the measure becomes the goal.</p>
<h3 class="kh">What makes it bearable</h3>
<ul class="fears"><li>Team overlap days.</li><li>Office days planned for in-person work.</li><li>Honest, early exceptions.</li><li>Managers who look at work, not badges.</li></ul>
<h3 class="kh">Three kinds of decree</h3>
<div class="breeds">
<div><b>The Collaboration Decree</b><p>Genuinely about working together. Make the days count.</p></div>
<div><b>The Property Decree</b><p>About filling floors. Comply sensibly; don't pretend it's about you.</p></div>
<div><b>The Control Decree</b><p>About watching people. Do the work, keep records, and think about the long term.</p></div>
</div>
{note("If you have caring responsibilities, a disability or a health condition, ask about adjustments early. Many workplaces must consider them.")}""",
        difficulty=dict(
            normal=dict(who="The Collaboration Decree, sensibly applied.",
                        know=["The reasons are explained.", "Exceptions are possible.", "Managers are reasonable."],
                        do=["Agree the Overlap Pact.", "Plan in-person work for office days.", "Ask early if it doesn't fit."],
                        avoid="Commuting to sit on calls.",
                        next="If badges are counted and judged, you're at Nightmare."),
            nightmare=dict(who="The Badge-Counting Decree.",
                           know=["Badge data is reported monthly.", "Managers are told to “have conversations”.", "Exceptions are rare."],
                           do=["Comply where you can.", "Make the Honest Ask where you can't, in writing.", "Keep your outcomes visible.", "Ask your manager how they'll use the data."],
                           avoid="Coffee badging.",
                           next="If attendance becomes a performance issue, you're at Hell."),
            hell=dict(who="The Control Decree, with consequences.",
                      know=["Attendance affects reviews or pay.", "No exceptions are granted.", "People are being managed out over it."],
                      do=["Know your contract and rights.", "Document any adjustments you've asked for.", "Talk to HR or a union if needed.", "Decide honestly if this place still works for you."],
                      avoid="The loud rebellion.",
                      next="If it doesn't work for your life, read Act VIII's chapter on leaving."),
        ),
        mirror=dict(
            title="Are you making the decree worse?",
            intro="As a colleague or a manager. Tick honestly.",
            signs=["You come in on different days from your team and complain the office is pointless.", "You judge colleagues by how often you see them.",
                   "You book in-person days and spend them on calls.", "You've coffee-badged.",
                   "As a manager, you've looked at badge data before looking at work."],
            cure="Ask your team which two days you'll all be in, and make one of them the day you do your best thinking together.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 5 September 2029, Pip's 1:1 with Ruth.",
            intro="The Honest Ask.",
            lines=[
                ("Pip", "Can I be honest about the three days? I'm seventy minutes each way. Yesterday I came in and sat on calls."),
                ("Ruth", "I saw. Sorry. What would work?"),
                ("Pip", "The team's agreed Tuesdays and Thursdays. Could my third day be flexible, for workshops and planning?"),
                ("Ruth", "Yes. I'd rather you came in for a reason than to badge."),
                ("Pip", "And if the badge report flags me?"),
                ("Ruth", "Then I'll show them the Overlap Pact. You're not the first to ask, Pip."),
            ],
            note="Four other people asked Ruth the same thing that month. All got a version of yes.",
        ),
    ),
    # ------------------------------------------------------------------ the Green Dot of Doom
    "green-dot-of-doom": dict(
        sighting=f"""{beat("Tuesday 17 July 2029 · the remark")}
<p>In a programme review, Hugo said, lightly: “I never see Asha online on Mondays.” Asha, remote on Mondays and Fridays,
was not in the room. She was finishing GridSight's Northshire forecast, offline, so she could think.</p>
{beat("That week · Hugo's dot")}
<p>Hugo's dot was always green. At 06:12, at 23:40, on Sundays. People admired it. What they didn't know was that on his
desk sat a small grey box, rocking his mouse gently back and forth, all day and all night.</p>
{beat("Friday 20 July · the Friday Lantern")}
<p>Pip told Asha what Hugo had said. She didn't argue. She started a Friday note to Pip, Ruth and Hugo: finished, next,
stuck. Three lines. By September Hugo was forwarding them to Rupert as an example of “great visibility”.</p>
{beat("Thursday 11 October · the fire drill")}
<p>During the fire drill, someone knocked Hugo's desk. The grey box fell off and lay on the carpet, rocking the mouse
in the empty office, keeping his dot green for nobody. Thirty people walked past it on the way back in. Hugo now works
with his dot honestly set to “focus time”.</p>
{note("A green dot proves the computer is on. Show people what you did with it.")}""",
        origin=dict(
            title="How the green dot became a god",
            beats=[
                ("2014 · chat arrives", "MetroVolt adopts Slack. Status dots are a small courtesy: is someone around to answer?"),
                ("2020 · the scattering", "With everyone at home, the dot is the only sign a colleague exists. Managers start glancing at it."),
                ("2023 · the watching", "A manager in Billing mentions dots in a review. Word spreads. People keep their dots green to be safe."),
                ("2029 · the jiggler", "Hugo, anxious since the Lumen days, buys a mouse jiggler. His dot never goes out. Asha's does, because she's working."),
            ],
            turning="A courtesy signal turning into a performance measure, because it was the only thing managers could see.",
            saved="Managers agreeing outcomes with remote people, so the dot never had to mean anything.",
            note="When people can't see work, they watch whatever they can see. Make the work visible and the dot stops mattering.",
        ),
        know=f"""<p>The green dot is a status indicator in chat tools. It was meant to show whether someone was available. In remote
and hybrid work it's become a proxy for presence, effort and even commitment, which it measures badly. People game it;
managers misread it; good remote workers get judged by it.</p>
<h3 class="kh">What it wants</h3>
<p>Nothing. It's a light. The people watching it want reassurance that work is happening.</p>
<h3 class="kh">Why it's watched</h3>
<p>Because work is invisible when you can't see someone, and the dot is the one thing that isn't.</p>
<h3 class="kh">What replaces it</h3>
<ul class="fears"><li>A weekly written note.</li><li>Agreed outcomes.</li><li>Honest statuses.</li><li>Managers who ask, not watch.</li></ul>
<h3 class="kh">Three kinds of dot-watcher</h3>
<div class="breeds">
<div><b>The Anxious Watcher</b><p>A manager who doesn't know what you're doing. The Friday Lantern cures it.</p></div>
<div><b>The Gossip Watcher</b><p>A colleague who comments on dots. Ignore, kindly.</p></div>
<div><b>The Tracking Watcher</b><p>A company that monitors activity formally. Know the policy and your rights.</p></div>
</div>
{note("If your company formally monitors activity, it should tell you how. Ask for the policy; it's your data too.")}""",
        difficulty=dict(
            normal=dict(who="The Anxious Watcher.",
                        know=["Your manager mentions your status.", "They mean well.", "They don't know what you're working on."],
                        do=["Start the Friday Lantern.", "Use honest statuses.", "Have the Outcome Conversation."],
                        avoid="The instant-reply reflex.",
                        next="If colleagues use your dot against you, you're at Nightmare."),
            nightmare=dict(who="The Gossip Watcher, in rooms you're not in.",
                           know=["Comments about your availability, in meetings.", "You're remote; they're not.", "It's affecting how you're seen."],
                           do=["Keep the Friday Lantern going, to a wider group.", "Ask your manager to vouch for your outcomes.", "Be visibly present at key moments.", "Don't argue about the dot."],
                           avoid="The mouse jiggler.",
                           next="If your company tracks activity formally, you're at Hell."),
            hell=dict(who="The Tracking Watcher.",
                      know=["Activity is monitored formally.", "Keystrokes or screens are recorded.", "It's used in reviews."],
                      do=["Ask for the monitoring policy in writing.", "Know your rights about workplace monitoring.", "Keep your outcome record.", "Decide whether you can work like this."],
                      avoid="Gaming the system. It's usually a disciplinary matter.",
                      next="If it's making you ill, read Act VIII."),
        ),
        mirror=dict(
            title="Are you a dot-watcher?",
            intro="Tick honestly.",
            signs=["You've mentioned someone's status in a meeting.", "You've judged a colleague's effort by when they're online.",
                   "You keep your own dot green when you're not working.", "You reply instantly to show you're present.",
                   "As a manager, you know when people log on but not what they delivered."],
            cure="Next time you wonder whether someone's working, ask them what they're working on. Then believe the answer.",
        ),
        rehearsal=dict(
            title="Scene: Friday 20 July 2029, Pip calls Asha.",
            intro="The Friday Lantern.",
            lines=[
                ("Pip", "I want to tell you something Hugo said, so you hear it from me. He said he never sees you online on Mondays."),
                ("Asha", "Because I'm working. Offline. On his programme's forecast, actually."),
                ("Pip", "I know. I don't think arguing about the dot will help. What if you sent a three-line note every Friday?"),
                ("Asha", "Finished, next, stuck?"),
                ("Pip", "Exactly. To me, Ruth and Hugo. Then nobody needs to look at your dot."),
                ("Asha", "Fine. But if Hugo starts sending one, I want to read it."),
            ],
            note="Hugo started sending one in November. It was mostly meetings. By February it wasn't.",
        ),
    ),
    # ------------------------------------------------------------------ the AI Replacement Prophecy
    "ai-replacement-prophecy": dict(
        sighting=f"""{beat("Monday 4 June 2029 · the awakening")}
<p>MetroVolt launched <b>VoltMind</b>, an AI assistant, for every employee. It drafted emails, summarised meetings,
wrote code and, it turned out, produced Customer Insight's weekly churn report in thirty-eight seconds. That report took
an analyst most of a Monday.</p>
{beat("Tuesday 12 June · the memo")}
<p>Rupert Thorne's memo on Ascend 2030 said AI would let MetroVolt deliver <b>“30% more output with 20% fewer people
by 2031”</b>. It didn't say which people. Pip's five analysts read it at their desks in total silence. That evening two of
them updated their CVs. One of them was Pip.</p>
{beat("June · the Task Map")}
<p>Pip stopped reading predictions and made a list of everything his team did. About 40% (weekly reports, data pulls,
first drafts) VoltMind could already do. About 35% it helped with. About 25% was judgment: which question to ask, whether
a number was believable, what to tell Ruth. Nobody had ever measured that 25%. It was most of what made the team useful.</p>
{beat("Thursday 19 July · the heatwave")}
<p>VoltMind's demand forecast for the heatwave week was smooth, confident and wrong: it had never seen a heatwave with
heat pumps on this scale. Rafi, one of Pip's analysts, spotted it, reworked it, and the control room adjusted in time. Pip
wrote it up for Ruth: the machine drafted, the human caught. Ruth sent it to Rupert.</p>
{beat("March 2030 · the outcome")}
<p>Customer Insight wasn't cut in Ascend 2030. The weekly reports were automated, and the Monday they'd freed went on the
questions nobody had had time for. Rafi became the team's first “insight engineer”. Honestly told: elsewhere, two
report-production roles in Finance weren't replaced when their holders left. The prophecy wasn't false. It just wasn't
as simple as the memo.</p>
{note("The machine has no opinion about your job. Your manager does. Make sure they know what you add.")}""",
        origin=dict(
            title="How the prophecy was written",
            beats=[
                ("2023 · the demos", "Everyone sees AI write essays and code. Leaders at every company are asked by their boards: what's your AI strategy?"),
                ("2025 · the consultants", "Reports promise huge productivity gains. Numbers like “30%” start appearing in parent-group strategy decks."),
                ("2028 · the target", "The parent group sets Rupert a cost target for 2031. AI is the most convenient way to explain how it'll be met."),
                ("June 2029 · the memo", "A real technology, a real cost target and a confident number become one sentence. Every analyst reads it as being about them."),
            ],
            turning="Mixing a genuine new tool with a cost target, and announcing both in one number.",
            saved="Asking each team to map its own tasks first, then deciding what AI changes. Bottom-up instead of top-down.",
            note="AI changes jobs; that part is real. But a percentage in a memo is a hope about money, not a measurement of your work.",
        ),
        know=f"""<p>The AI replacement prophecy is the fear (and sometimes the plan) that AI will take your job. Some of it is real:
tasks that are routine, repeatable and text- or data-based are being automated. Some of it is hype. Most jobs are a mix
of tasks, and AI usually takes some of them and changes the rest.</p>
<h3 class="kh">What it wants</h3>
<p>The prophets want attention or savings. The machine wants nothing. Your leaders want to show they have a plan.</p>
<h3 class="kh">Why it terrifies</h3>
<p>Because it's vague. “20% fewer people” could be anyone. Uncertainty is worse than bad news.</p>
<h3 class="kh">What it can't easily replace</h3>
<ul class="fears"><li>Choosing the right question.</li><li>Knowing when a number is wrong.</li><li>Trust, relationships, persuasion.</li><li>Taking responsibility for a decision.</li></ul>
<h3 class="kh">Three kinds of prophecy</h3>
<div class="breeds">
<div><b>The Hype Prophecy</b><p>Loud predictions, no plan. Learn the tools; ignore the noise.</p></div>
<div><b>The Change Prophecy</b><p>Your job will change. Move towards the judgment parts.</p></div>
<div><b>The Cut Prophecy</b><p>Roles really will go. Read Act V; prepare honestly.</p></div>
</div>
{note("The people who learn the tools well early tend to become the people who decide how they're used. Be one of them.")}""",
        difficulty=dict(
            normal=dict(who="The Hype Prophecy.",
                        know=["Lots of talk, no specifics.", "Tools are new and optional.", "Nobody's role has changed yet."],
                        do=["Learn the tools properly.", "Do the Task Map for yourself.", "Share what works."],
                        avoid="The doom scroll.",
                        next="If parts of your job are being automated, you're at Nightmare."),
            nightmare=dict(who="The Change Prophecy.",
                           know=["A real chunk of your work is now automated.", "Your manager is asking what you'll do instead.", "Colleagues are anxious."],
                           do=["Do the Task Map with your manager.", "Propose what to do with the time freed.", "Do the Judgment Showcase.", "Help your team learn, not hide."],
                           avoid="The ostrich.",
                           next="If roles are actually being cut, you're at Hell."),
            hell=dict(who="The Cut Prophecy.",
                      know=["Headcount targets name AI.", "Roles like yours are going.", "Timelines are announced."],
                      do=["Ask directly how your role is affected.", "Build skills that move you towards judgment work.", "Update your CV quietly.", "Read Act V, the Famine."],
                      avoid="Pretending it isn't happening.",
                      next="If your role goes, read the Go-Bag Scroll."),
        ),
        mirror=dict(
            title="Are you feeding the prophecy?",
            intro="Tick honestly.",
            signs=["You haven't tried the AI tools your company offers.", "You read AI predictions late at night.",
                   "You can't say which parts of your job need your judgment.", "You've hidden how you do your work so nobody can automate it.",
                   "You've told someone “AI will take your job” as a joke, and they didn't laugh."],
            cure="This week, write your own Task Map: what the machine can do, what it helps with, what needs you. Then show your manager the last column.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 26 June 2029, Pip and his analysts.",
            intro="The Task Map, out loud.",
            lines=[
                ("Pip", "I read Rupert's memo too. I updated my CV. I'm saying that so you know I'm not pretending."),
                ("Rafi", "So are we going?"),
                ("Pip", "I don't know. But I've mapped what we do. VoltMind can do about forty percent of it already."),
                ("Rafi", "…That's the reports."),
                ("Pip", "Yes. And the other quarter is judgment, which nobody's ever measured. I want to measure it, and show Ruth."),
                ("Rafi", "Then let's give the reports to the machine and do the questions we never had time for."),
            ],
            note="Three weeks later Rafi caught the heatwave error. It was the best evidence Pip ever wrote up.",
        ),
    ),
    # ------------------------------------------------------------------ the Copilot Credit Grab
    "copilot-credit-grab": dict(
        sighting=f"""{beat("August 2029 · the prompt library")}
<p>Asha built a library of VoltMind prompts for customer analysis: churn, complaints, segmentation. They were brilliant.
She shared them in a channel. Within a month they'd been copied all over MetroVolt, mostly with her name taken off.</p>
{beat("Thursday 20 September · the deck")}
<p>Hugo presented an Ascend 2030 customer deep-dive to the steering group: forty slides, “six weeks of analysis”. Rupert
called it “exactly the kind of insight we need”. It had been made in an afternoon, with VoltMind and Asha's prompts.
Nobody mentioned either.</p>
{beat("Slide 14")}
<p>Pip, reading it afterwards, found slide 14 claimed complaints had fallen 40%. They'd fallen 4%. VoltMind had misread a
column; nobody had checked. Pip told Hugo privately, the same day, and asked, kindly, how the deck was made.</p>
{beat("Thursday 4 October · the correction")}
<p>Hugo, to his credit (eventually), sent a correction to the steering group: slide 14 fixed, and a line: “This analysis
used VoltMind and Asha's prompt library, which is excellent.” In November, Juno added a line to MetroVolt's AI guidance:
<i>Say what the machine did, what you did, and what you checked.</i></p>
{note("The machine doesn't want credit. The people behind it do. Give it to them.")}""",
        origin=dict(
            title="How the credit came to be grabbed",
            beats=[
                ("Always · the old grab", "People have always passed off others' work as theirs. See Act II, the Credit Vampire."),
                ("2029 · the new fog", "With AI, nobody knows how anything was made. An afternoon's prompting looks like six weeks' work."),
                ("The shame", "Many people feel AI use is cheating, so they hide it. Hiding it makes it easy to overclaim."),
                ("September · Hugo", "Under pressure to show Ascend progress, Hugo presents a deck without saying how it was made. He isn't a vampire. He's in a fog."),
            ],
            turning="AI making the effort behind work invisible, and nobody agreeing how to talk about it.",
            saved="A simple norm, from the start: say what the machine did, what you did, and what you checked.",
            note="AI didn't invent credit-grabbing. It just made the fog thicker. Clear it with honesty about method.",
        ),
        know=f"""<p>The copilot credit grab is the confusion over who should get credit when AI helped make something: the person who
presented it, the person who wrote the prompt, the person who checked it, or nobody. Without clear norms, effort gets
exaggerated, methods go uncredited, and unchecked errors get presented as analysis.</p>
<h3 class="kh">What it wants</h3>
<p>Usually, just to look good under pressure. Sometimes, to hide that the work was easy.</p>
<h3 class="kh">Why it spreads</h3>
<p>Because nobody can see how work was made any more, and saying “AI helped” still feels like admitting something.</p>
<h3 class="kh">What clears the fog</h3>
<ul class="fears"><li>Saying how it was made.</li><li>Crediting prompts and methods.</li><li>Checking before presenting.</li><li>Claiming your judgment, not your typing.</li></ul>
<h3 class="kh">Three kinds of grabber</h3>
<div class="breeds">
<div><b>The Fogbound</b><p>Didn't think to say. A kind question fixes it.</p></div>
<div><b>The Ashamed</b><p>Hides AI use out of embarrassment. Reassure them it's normal.</p></div>
<div><b>The Grabber</b><p>Knowingly claims others' methods. Treat as a Credit Vampire (Act II).</p></div>
</div>
{note("The most valuable thing you can claim now is your judgment: the question, the check, the decision. Claim that.")}""",
        difficulty=dict(
            normal=dict(who="The Fogbound.",
                        know=["Someone didn't mention AI use.", "No harm intended.", "Nobody's work was taken."],
                        do=["Model the Honest Recipe yourself.", "Ask kindly how things were made.", "Suggest a team norm."],
                        avoid="The shame hide.",
                        next="If your method was used without credit, you're at Nightmare."),
            nightmare=dict(who="Your prompt, their praise.",
                           know=["Your method or prompt was used.", "Someone else was credited.", "It's spreading."],
                           do=["Put your name on what you share.", "Mention your method, cheerfully, in the right room.", "Ask your manager to help make it visible.", "Read the Credit Vampire in Act II."],
                           avoid="A public fight.",
                           next="If unchecked AI output is being presented as fact, you're at Hell."),
            hell=dict(who="The Unchecked Paste, presented to leadership.",
                      know=["The numbers are wrong.", "Decisions might be made on them.", "The presenter doesn't know."],
                      do=["Tell the presenter privately, fast.", "Offer to help correct it.", "If they won't, tell your manager.", "Push for a checking norm."],
                      avoid="Correcting them publicly in the meeting.",
                      next="If nothing changes, raise it with whoever owns the AI guidance."),
        ),
        mirror=dict(
            title="Are you grabbing the machine's credit?",
            intro="Tick honestly.",
            signs=["You've presented AI output without saying it was AI.", "You've used someone's prompt without crediting them.",
                   "You've described an afternoon's work as weeks.", "You've presented AI numbers you didn't check.",
                   "You feel you'd look worse if people knew how you made something."],
            cure="Add one line to your next piece of work: “Drafted with VoltMind; I checked X and decided Y.” You'll look better, not worse.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 20 September 2029, Pip messages Hugo.",
            intro="The kind question, privately.",
            lines=[
                ("Pip", "Hugo, great deck. Quick one: slide 14 says complaints fell 40%. I think it's 4%. Could VoltMind have misread the column?"),
                ("Hugo", "…Possibly. It was quite quick to make, honestly."),
                ("Pip", "That's fine. Was it Asha's prompt library? It's brilliant for this."),
                ("Hugo", "It was. I should have said."),
                ("Pip", "Could you send a quick correction? Fix slide 14 and mention her library. It'll make the whole thing more believable."),
                ("Hugo", "Yes. Thanks for telling me privately."),
            ],
            note="Rupert replied to the correction: “Much more useful to know how it was made.” Asha's library got its own page on the intranet, with her name at the top.",
        ),
    ),
    # ------------------------------------------------------------------ the Cult of Family
    "cult-of-family": dict(
        sighting=f"""{beat("Monday 10 September 2029 · the banner")}
<p>A banner went up in the atrium, three storeys high: <b>“WE ARE THE METROVOLT FAMILY.”</b> Imogen launched the campaign
with a video: colleagues hugging, a cake, a line about “looking after each other like family”. Mugs followed.</p>
{beat("Friday 14 September · the weekend")}
<p>Ascend 2030's first systems went live on Saturday 22 September. Hugo asked Pip's team to “pull together like family”
and work the weekend, unpaid, “because that's what families do”. Pip offered Thursday evening until eight, and Monday
first thing. He declined Saturday. Hugo looked wounded. Pip felt guilty for a day. Then he read the next entry in the
diary.</p>
{beat("Tuesday 6 November · the restructure")}
<p>Retail announced a restructure: 120 roles. Calendar invites went out at 08:00. In the atrium, under the banner, people
from Retail walked to their meetings. The Chronicler, who'd seen this in 2009 under a banner that said “ONE BIG
FAMILY”, stood beside Pip and said, quietly: “Families don't send calendar invites.”</p>
{beat("January 2030 · the quiet replacement")}
<p>The banner came down. A new one went up: <b>“ONE METROVOLT TEAM.”</b> Nobody announced the change. Imogen, asked about it
by Pip at a skip-level, said: “Teams can be honest about change. Families can't.” She had, it turned out, argued for that
wording in August, and lost.</p>
{note("Love your colleagues. Remember that the company can restructure them, and you.")}""",
        origin=dict(
            title="How MetroVolt became a “family” (again)",
            beats=[
                ("1998 · the real family firm", "MetroVolt's founders really did know everyone's name. The word “family” started there, and was nearly true."),
                ("2009 · the first banner", "After the financial crisis, “ONE BIG FAMILY” goes up during a cost-cutting year. People remember the irony for a decade."),
                ("2027 · after Horizon", "Engagement scores fall after the Famine. Leadership wants warmth back. “Family” tests well in a focus group."),
                ("2029 · the campaign", "Imogen proposes “team”; the executive committee prefers “family”. The banner goes up two months before Retail's restructure."),
            ],
            turning="Using the warmest possible word to fix trust, during a year when trust was about to be tested again.",
            saved="Imogen's original wording: “team”. Warm, true, and honest about change.",
            note="“Family” at work usually means someone wants loyalty that a contract doesn't require. Give your care freely; keep your boundaries.",
        ),
        know=f"""<p>The cult of family is when an organisation describes itself as a family, usually sincerely, sometimes strategically.
The feeling it describes (care, belonging, loyalty) is often real between colleagues. The problem is that a company can't
be a family: it pays you, can restructure you, and expects you to leave one day. Calling it a family blurs those facts,
and makes boundaries feel like betrayal.</p>
<h3 class="kh">What it wants</h3>
<p>Loyalty and extra effort, freely given. Sometimes just warmth. Sometimes unpaid weekends.</p>
<h3 class="kh">Why it's dangerous</h3>
<p>Because it makes normal things (saying no, asking for pay, leaving) feel like disloyalty, and makes restructures feel like betrayal.</p>
<h3 class="kh">What's healthier</h3>
<ul class="fears"><li>Team, not family.</li><li>Care with boundaries.</li><li>Honesty about change.</li><li>Leaving well, without guilt.</li></ul>
<h3 class="kh">Three kinds of family cult</h3>
<div class="breeds">
<div><b>The Sincere Family</b><p>Leaders really mean it. Enjoy the warmth; keep your boundaries anyway.</p></div>
<div><b>The Weekend Family</b><p>“Family” is used to get unpaid work. Warm boundary, every time.</p></div>
<div><b>The Guilt Family</b><p>Leaving is called betrayal. Leave well, without apology.</p></div>
</div>
{note("A good team cares about you and still lets you go. That's not less than family. It's more honest.")}""",
        difficulty=dict(
            normal=dict(who="The Sincere Family.",
                        know=["Leaders mean it warmly.", "No unpaid extra work is expected.", "People do look after each other."],
                        do=["Enjoy the warmth.", "Keep the Team Lens.", "Look after colleagues on your own terms."],
                        avoid="The cynic's sneer.",
                        next="If “family” is used to ask for unpaid work, you're at Nightmare."),
            nightmare=dict(who="The Weekend Family.",
                           know=["Weekend and evening asks.", "Refusing feels disloyal.", "“Family” appears in the ask."],
                           do=["Use the Warm Boundary.", "Offer what you can, clearly.", "Track your extra hours.", "Talk to your manager if it becomes regular."],
                           avoid="The total devotion.",
                           next="If leaving or saying no is called betrayal, you're at Hell."),
            hell=dict(who="The Guilt Family.",
                      know=["Leavers are spoken of badly.", "Boundaries are treated as disloyalty.", "Restructures happen anyway."],
                      do=["Keep your boundaries.", "Keep your CV current.", "Find colleagues who see it too.", "Leave well if you need to."],
                      avoid="Staying out of guilt.",
                      next="Read Act VIII, the Inner Sanctum."),
        ),
        mirror=dict(
            title="Are you running the family cult?",
            intro="Especially if you manage people. Tick honestly.",
            signs=["You've said “we're a family” to your team.", "You've asked for weekend work by appealing to loyalty.",
                   "You've been hurt when someone resigned, and shown it.", "You've described a leaver as “disloyal”.",
                   "You feel guilty when you take all your holiday."],
            cure="Replace “family” with “team” in your vocabulary for a month. Notice what you can say honestly that you couldn't before.",
        ),
        rehearsal=dict(
            title="Scene: Friday 14 September 2029, Hugo asks Pip about the weekend.",
            intro="The Warm Boundary.",
            lines=[
                ("Hugo", "Go-live's Saturday. We need everyone. Families pull together, right?"),
                ("Pip", "I want it to go well too. I can do Thursday evening until eight, and be on first thing Monday."),
                ("Hugo", "But Saturday's the big day."),
                ("Pip", "I can't do Saturday. If something breaks that's mine, ring me and I'll help by phone for an hour."),
                ("Hugo", "…Okay. That's actually helpful. Thanks."),
            ],
            note="Nothing of Pip's broke on Saturday. Hugo worked fourteen hours. In January he asked Pip how he'd said no so easily.",
        ),
    ),
    # ------------------------------------------------------------------ the All-Hands Mass
    "all-hands-mass": dict(
        sighting=f"""{beat("Thursday 11 October 2029 · the questions")}
<p>Staff were invited to submit questions for the quarterly all-hands, “to make the best use of time”. Tamsin, on floor 27,
read all 214 of them a week early. Forty-one asked about Ascend and jobs. Six were chosen. None of the forty-one.</p>
{beat("Thursday 18 October · the mass")}
<p>The atrium, chairs in rows, a lectern, a screen of rising arrows. Dame Helena spoke for thirty-five minutes. “Exciting
times.” “Doubling down on networks.” “Our journey to 2030.” “Right-sizing our cost base.” Retail wasn't mentioned once.
Customer was mentioned twice, both times as “our customers”, not the teams.</p>
{beat("18 October · the Q&A")}
<p>Five pre-submitted questions were answered (one about parking). Then, unexpectedly, two live questions. Pip, who'd
prepared one in case, put his hand up: “Thanks, Helena. You mentioned doubling down on networks. What does that mean for
Customer teams this year?” A pause. Then a real answer: Customer headcount stable this year, AI tools to free capacity,
no further restructures planned in Customer “that I'm aware of today”.</p>
{beat("Tuesday 6 November · the silence explained")}
<p>Retail's restructure was announced. It had not been mentioned at the all-hands. The Chronicler, who'd noted the
silence on a napkin (“Retail: 0 mentions”), had told their friend in Retail to update her CV a fortnight earlier.</p>
{note("The liturgy is mostly noise. The silences are the sermon.")}""",
        origin=dict(
            title="How the all-hands became a mass",
            beats=[
                ("2005 · the old town hall", "MetroVolt's CEO takes open questions in the canteen. Some are angry. Some answers are honest. People remember it fondly."),
                ("2016 · the comms team", "An angry question goes viral internally. All-hands get scripted. Questions are submitted in advance."),
                ("2022 · the arrows", "Slides become strategy art. Nobody presents a number that could be wrong. The language becomes safe and empty."),
                ("2029 · the mass", "Dame Helena genuinely wants to connect. But the format, built to avoid risk, turns her sincerity into liturgy."),
            ],
            turning="One bad moment in 2016, which made every all-hands since a performance designed to avoid another.",
            saved="Keeping some live questions, and a CEO willing to say “I don't know yet”.",
            note="Most leaders hate the liturgy too. They're trapped in it. A good question is a key.",
        ),
        know=f"""<p>The all-hands is a regular meeting where leadership speaks to everyone. It's often heavily scripted and full of
leadership language that sounds meaningful and says little. But it isn't useless. What's said, what's emphasised and
especially what isn't mentioned can tell you a lot.</p>
<h3 class="kh">The decoder ring</h3>
<p><b>Exciting times:</b> change is coming. <b>Doubling down on X:</b> less of everything else. <b>Right-sizing:</b> fewer people.
<b>Our journey:</b> no end date. <b>No plans at this time:</b> not yet announced. <b>Efficiencies:</b> cuts.</p>
<h3 class="kh">Why it's scripted</h3>
<p>Because one bad answer can travel the whole company in an hour. Leaders protect themselves with vagueness.</p>
<h3 class="kh">What to listen for</h3>
<ul class="fears"><li>Areas not mentioned.</li><li>Promises from last quarter, missing.</li><li>New words repeated often.</li><li>Answers that change the subject.</li></ul>
<h3 class="kh">Three kinds of mass</h3>
<div class="breeds">
<div><b>The Real Town Hall</b><p>Live questions, honest answers. Ask well; it's rare.</p></div>
<div><b>The Liturgy</b><p>Scripted, safe, vague. Decode it and read the silences.</p></div>
<div><b>The Pre-Announcement</b><p>Unusually vague, moved at short notice. Something's coming; read Act V.</p></div>
</div>
{note("Ask your manager after every all-hands: “What did you hear that I might have missed?” They often know.")}""",
        difficulty=dict(
            normal=dict(who="The Real Town Hall.",
                        know=["Live questions are taken.", "Leaders answer directly.", "Numbers are shown."],
                        do=["Listen properly.", "Ask a specific question if you have one.", "Share what you learned with your team."],
                        avoid="The total tune-out.",
                        next="If it's all script and arrows, you're at Nightmare."),
            nightmare=dict(who="The Liturgy.",
                           know=["Pre-submitted questions only.", "Lots of jargon, few facts.", "Your area isn't mentioned."],
                           do=["Use the Decoder Ring.", "Note the silences.", "Ask your manager what they heard.", "Prepare one good question anyway."],
                           avoid="Taking the liturgy literally.",
                           next="If it's moved at short notice and unusually vague, you're at Hell."),
            hell=dict(who="The Pre-Announcement.",
                      know=["It was moved forward suddenly.", "Words like “right-sizing” appear.", "Leaders look tired."],
                      do=["Read Act V, Reading the Omens.", "Update your Go-Bag Scroll.", "Talk to your manager privately.", "Don't panic publicly."],
                      avoid="The ambush.",
                      next="If invites arrive, read the Day of the Calendar Invite."),
        ),
        mirror=dict(
            title="Do you preach the liturgy?",
            intro="If you ever present to a team. Tick honestly.",
            signs=["You've said “exciting times” instead of saying what's changing.", "You've avoided mentioning a team because the news was bad.",
                   "You only take questions you've seen in advance.", "Your slides have more arrows than numbers.",
                   "You've said “no plans at this time” knowing plans existed."],
            cure="In your next team update, replace one phrase with the plain fact. “We're cutting the budget by 10%” is scarier to say and kinder to hear.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 18 October 2029, the live Q&A.",
            intro="The Good Question.",
            lines=[
                ("Host", "We have time for two live questions."),
                ("Pip", "Thanks, Helena. You mentioned doubling down on networks. What does that mean for Customer teams this year?"),
                ("Dame Helena", "Good question. Honestly: Customer headcount is stable this year. We want AI tools to free up capacity, not remove people."),
                ("Pip", "Thank you."),
                ("Dame Helena", "And no further restructures are planned in Customer that I'm aware of today."),
            ],
            note="“That I'm aware of today” was, the Chronicler noted, the most honest phrase of the afternoon. Customer was not restructured that year.",
        ),
    ),
    # ------------------------------------------------------------------ the Engagement Survey Oracle
    "engagement-survey-oracle": dict(
        sighting=f"""{beat("Thursday 1 November 2029 · the oracle speaks")}
<p><b>Pulse</b>, MetroVolt's annual engagement survey, opened: forty questions, “two minutes”, “completely anonymous”. It
asked for team, grade, location and length of service. Results would be reported for any group of five or more. Ruth's
team had six people.</p>
{beat("November · the comments")}
<p>Pip wrote one comment, the kind he'd say in person: “We've been covering two roles since March. Agreeing priorities
would help more than anything.” Someone else in the team wrote four hundred furious words about Ascend, including a
phrase they used in every meeting.</p>
{beat("Monday 3 December · the reading")}
<p>Ruth read her team's results twice. She recognised every voice; with six people, how could she not? She did not try
to work out who wrote what. She told Pip later it took real effort not to. Hugo, in another team, asked two people
directly whether they'd written a comment. Imogen heard about it within the day and stopped it.</p>
{beat("Tuesday 4 December · the Manager's Rite")}
<p>Ruth shared the team's results in full. “Three of you said priorities are unclear. You're right. From January we'll
agree the top three each month, and I'll say no to anything else.” She also said: “Someone's very angry about Ascend.
I hear it. If you want to talk, my door's open; if not, that's fine.” The angry writer came to see her a week later.</p>
{note("Write what you'd say out loud. Then, if it's safe, say it out loud.")}""",
        origin=dict(
            title="How the oracle came to ask so much",
            beats=[
                ("2012 · the first survey", "MetroVolt runs its first engagement survey. Results are shared company-wide. Nothing changes. Response rates fall."),
                ("2018 · the drill-down", "To make results actionable, the survey starts reporting by team. Groups get smaller. Anonymity gets thinner."),
                ("2024 · the threshold", "The minimum reporting group is lowered from ten to five, “so managers have something to act on”."),
                ("2029 · the oracle", "Pulse is useful and dangerous at once: actionable for managers, and recognisable for small teams."),
            ],
            turning="Making results small enough to act on, without thinking about whether they were still anonymous.",
            saved="A reporting threshold of ten, and clear guidance for managers on what not to do with comments.",
            note="An anonymous survey is only as anonymous as its smallest group and its most curious manager.",
        ),
        know=f"""<p>Engagement surveys ask employees how they feel about their work, team and leaders. They can drive real change when
results are shared and acted on. But “anonymous” often means “not named”, not “unidentifiable”: in small teams, managers
can often guess, and comments in someone's usual phrasing are easy to recognise.</p>
<h3 class="kh">What it wants</h3>
<p>Honest data. And, often, a good score to show leadership.</p>
<h3 class="kh">Why it's mistrusted</h3>
<p>Because previous surveys changed nothing, and because people suspect (often rightly) that small teams aren't really anonymous.</p>
<h3 class="kh">What makes it useful</h3>
<ul class="fears"><li>Specific, kind comments.</li><li>Managers who share and act.</li><li>No author hunts.</li><li>One visible change.</li></ul>
<h3 class="kh">Three kinds of oracle</h3>
<div class="breeds">
<div><b>The True Oracle</b><p>Large groups, real action. Be honest.</p></div>
<div><b>The Thin Veil</b><p>Small teams, recognisable comments. Write what you'd say in person.</p></div>
<div><b>The Hollow Oracle</b><p>Nothing ever changes. Answer briefly, and say the important things directly.</p></div>
</div>
{note("If you manage people: the worst thing you can do with survey results is hunt for authors. The second worst is nothing.")}""",
        difficulty=dict(
            normal=dict(who="The True Oracle.",
                        know=["Large reporting groups.", "Last year's results were acted on.", "Managers share results."],
                        do=["Answer honestly.", "Write one useful comment.", "Join the follow-up conversation."],
                        avoid="The all-fives lie.",
                        next="If your team is small, you're at Nightmare."),
            nightmare=dict(who="The Thin Veil.",
                           know=["Your team is under ten.", "Comments are shown to your manager.", "Your phrasing is recognisable."],
                           do=["Do the Anonymity Check.", "Write the Useful Comment.", "Say important things in person too.", "Keep it kind."],
                           avoid="The venting essay.",
                           next="If your manager hunts for authors, you're at Hell."),
            hell=dict(who="The Author Hunt.",
                      know=["Your manager asks who wrote what.", "People are treated differently after.", "Trust is gone."],
                      do=["Don't confirm or deny.", "Tell HR; author hunts are usually against policy.", "Talk to your skip-level.", "Keep notes."],
                      avoid="Writing anything you'd regret being linked to.",
                      next="If it continues, read the Escape Portal in Act III."),
        ),
        mirror=dict(
            title="Are you misusing the oracle?",
            intro="As a respondent or a manager. Tick honestly.",
            signs=["You've written survey comments you'd never say in person.", "You've ticked everything positive to be safe.",
                   "As a manager, you've tried to guess who wrote a comment.", "You've never shared your team's results.",
                   "You've complained nothing changes but never said what should."],
            cure="Write one comment this year that you'd be happy to sign. Then, if it's safe, sign it, by saying it in your next 1:1.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 4 December 2029, Ruth's team meeting.",
            intro="The Manager's Rite.",
            lines=[
                ("Ruth", "Here are our full Pulse results. I'm not hiding any of it."),
                ("Ruth", "Three of you said priorities are unclear. You're right. That's on me."),
                ("Pip", "What changes?"),
                ("Ruth", "From January we agree the top three each month. Anything else, I say no to, on your behalf."),
                ("Ruth", "And someone's very angry about Ascend. I hear it. My door's open. If you'd rather not, that's fine too."),
            ],
            note="Engagement in Ruth's team rose eleven points the following year. She credits one sentence: “That's on me.”",
        ),
    ),
    # ------------------------------------------------------------------ the Hot-Desk Hunger Games
    "hot-desk-hunger-games": dict(
        sighting=f"""{beat("September 2029 · floor 14")}
<p>Floor 22 closed. Customer Insight moved to <b>floor 14</b>: two hundred people, a hundred and forty desks, one booking
app called DeskIt, which released the next week's desks at <b>00:00 on Sunday</b>. Lockers were provided. About a third
of them locked.</p>
{beat("Tuesday 18 September · the arena")}
<p>By 09:00 every window desk had a jumper on it. By 10:00 Pip's team was scattered across three zones and a booth. Rafi,
who has a bad back, had booked the one sit-stand desk at 00:01; someone without a booking was sitting at it. Pip worked
from a sofa with his laptop on a cushion.</p>
{beat("Wednesday 19 September · the Neighbourhood Claim")}
<p>Pip emailed Femi Adeyemi in facilities, politely: the team was in on Tuesdays and Thursdays; could they have a block of
eight desks on those days? Femi replied within an hour: yes, and why hadn't anyone asked before? Neighbourhoods existed;
they just weren't advertised.</p>
{beat("October · the kit and the right")}
<p>Pip assembled a Portable Kit in a tote bag: charger, mouse, headset, the good pen, a photo of his dog. Rafi asked for a
reasonable adjustment for his back and got a sit-stand desk booked permanently for his office days. The jumpers continued
elsewhere. Femi put up a cheerful sign. It didn't help.</p>
{note("A desk is not a home. Carry your home in a bag, and ask for a neighbourhood.")}""",
        origin=dict(
            title="How the Hunger Games began",
            beats=[
                ("2019 · assigned desks", "Everyone has a desk, a drawer and a plant. Utilisation, measured once, is 54%."),
                ("2021 · the closure plan", "With hybrid work, property teams see empty desks. Hot-desking is planned at a ratio of 7 desks per 10 people."),
                ("2029 · the squeeze", "Floor 22 closes just as the three-day mandate starts. Tuesdays and Thursdays are now at 115% of capacity."),
                ("The arena", "Nobody planned for everyone choosing the same days. The app opening at midnight makes it a contest."),
            ],
            turning="Two decisions (fewer floors, more office days) made by different people in the same year.",
            saved="Facilities and the mandate team talking to each other, and team neighbourhoods offered from day one.",
            note="Hot-desking works when there are enough desks on busy days. When there aren't, it's a game. Ask the people running it to change the rules.",
        ),
        know=f"""<p>Hot-desking means nobody has an assigned desk; you book one each day. It saves space when attendance is spread
out. When everyone comes in on the same days, it turns into a competition: early bookings, reserved-by-jumper desks,
scattered teams and the daily hunt for a working monitor.</p>
<h3 class="kh">What it wants</h3>
<p>Fewer desks, used more. It's a property decision, not a personal one.</p>
<h3 class="kh">Why it hurts</h3>
<p>Because it removes small comforts (a place, your things, your team nearby) without anyone deciding that's the goal.</p>
<h3 class="kh">What helps</h3>
<ul class="fears"><li>Team neighbourhoods.</li><li>A portable kit.</li><li>Reasonable adjustments.</li><li>Telling facilities what's broken.</li></ul>
<h3 class="kh">Three kinds of arena</h3>
<div class="breeds">
<div><b>The Spacious Arena</b><p>Enough desks. Mildly annoying. Pack a kit.</p></div>
<div><b>The Crowded Arena</b><p>Too few desks on busy days. Ask for neighbourhoods and staggered days.</p></div>
<div><b>The Broken Arena</b><p>No desks, broken kit, no lockers. Escalate, with numbers.</p></div>
</div>
{note("If you need a specific setup for a health condition or disability, ask for an adjustment formally. It's not a favour.")}""",
        difficulty=dict(
            normal=dict(who="The Spacious Arena.",
                        know=["Enough desks most days.", "Some kit issues.", "Teams can sit together if they try."],
                        do=["Build a Portable Kit.", "Book with your team.", "Report broken kit."],
                        avoid="The jumper claim.",
                        next="If there aren't enough desks on your days, you're at Nightmare."),
            nightmare=dict(who="The Crowded Arena.",
                           know=["Booking at midnight.", "Your team is scattered.", "People sit on sofas."],
                           do=["Make the Neighbourhood Claim.", "Suggest staggered team days to facilities.", "Count the problem, kindly, with dates.", "Ask for adjustments where needed."],
                           avoid="The midnight grab.",
                           next="If people can't work at all, you're at Hell."),
            hell=dict(who="The Broken Arena.",
                      know=["Not enough desks for the mandate.", "Kit is broken.", "Nothing changes when you report it."],
                      do=["Raise it with your manager, with numbers.", "Ask whether the mandate can flex.", "Use health and safety routes if needed.", "Keep your outcomes visible either way."],
                      avoid="The silent suffering.",
                      next="If the office makes your work impossible, make the Honest Ask (see the Decree)."),
        ),
        mirror=dict(
            title="Are you a Hunger Games tribute?",
            intro="Tick honestly.",
            signs=["You've left a jumper on a desk to hold it.", "You've booked desks for people who might come in.",
                   "You've sat at someone's booked desk.", "You've never asked facilities for anything.",
                   "You complain about hot-desking but never say what would help."],
            cure="Ask facilities one specific thing this month: a neighbourhood, a fixed monitor, a locker that locks. You may be the first to ask.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 19 September 2029, Pip emails Femi in facilities.",
            intro="The Neighbourhood Claim.",
            lines=[
                ("Pip", "Hi Femi, Customer Insight are all in on Tuesdays and Thursdays. Could we have a block of eight desks on those days?"),
                ("Femi", "Yes. We've got neighbourhoods. Nobody asks for them."),
                ("Pip", "Brilliant. And Rafi needs a sit-stand desk for his back. How does he ask properly?"),
                ("Femi", "Reasonable adjustment form; I'll fast-track it. Anything else?"),
                ("Pip", "Some lockers don't lock."),
                ("Femi", "I know. Two-thirds of them. I've asked for a budget since June."),
            ],
            note="The lockers were fixed in February 2030. Femi sent the team a photo of the receipt.",
        ),
    ),
    # ------------------------------------------------------------------ the Transformation Journey
    "transformation-journey": dict(
        sighting=f"""{beat("Monday 3 September 2029 · the pilgrimage begins")}
<p>Ascend 2030's centrepiece was a new <b>Product Operating Model</b>. Customer Insight became the “Insight Squad”, part of
the “Customer Value Stream”. Ruth became a “Value Stream Lead”. Pip became a “Principal Insight Practitioner”. Nothing
else about anyone's job changed on day one.</p>
{beat("The ghosts on the road")}
<p>The Chronicler had walked this road three times. <b>Lean, 2014:</b> kaizen boards, still on a wall on floor 9, last
updated in 2015. <b>Agile, 2018:</b> stand-ups, sprints and a team renamed “tribe” for a year. <b>SAFe, 2022:</b> release
trains and quarterly planning events in a hotel; the Chronicler was a “Release Train Engineer” for eight months and never
found out what it meant.</p>
{beat("Tuesday 11 September · the fourth guide")}
<p>Juno Ferrell, Head of Ways of Working, ran the Insight Squad's first session. Pip expected sticky notes. Juno asked one
question: “What takes too long here?” Pip did the Real Problem Hunt and found it: a piece of analysis took <b>eleven
weeks</b> from idea to approved work, mostly waiting for sign-offs. Juno's eyes lit up. “That. Let's fix that.”</p>
{beat("March 2030 · the destination")}
<p>Pip measured it monthly. Juno removed three sign-off steps and introduced a weekly decision meeting with Ruth. By March,
idea to approved work took <b>four weeks</b>. Pip had kept the Keep List: Ruth's monthly top three, the Friday notes, the
team's Tuesday lunch. All survived. The names didn't: by spring, everyone was quietly calling it Customer Insight again.
Juno didn't mind. “The names were never the point.”</p>
{note("Every transformation promises a new world. Ask which problem it solves, and help solve that one.")}""",
        origin=dict(
            title="How MetroVolt came to transform four times",
            beats=[
                ("2014 · Lean", "A manufacturing method applied to an office. Real improvements in billing; boards everywhere else. The CEO leaves; it fades."),
                ("2018 · Agile", "A new CTO brings agile from tech. It works in software teams. It's rolled out to Finance. It doesn't."),
                ("2022 · SAFe", "The parent group wants agile at scale. Consultants arrive. A great deal of planning happens. Rather less else."),
                ("2029 · the Product Operating Model", "Rupert brings the fourth. This time, by luck or design, the coach is good and asks about real problems."),
            ],
            turning="Each transformation being sold as the answer before anyone asked what the question was.",
            saved="Starting with a measured problem (eleven weeks from idea to work) rather than a method.",
            note="Transformations fail when the method is the goal. They work when a real problem is the goal, and the method is just a tool.",
        ),
        know=f"""<p>A transformation is a large programme to change how an organisation works: new structures, new roles, new rituals,
often a new vocabulary. Many fail, not because the methods are bad but because they're imposed as rituals rather than
used to fix specific problems. The fourth one is usually met with a sigh. Sometimes it's the one that works.</p>
<h3 class="kh">What it wants</h3>
<p>Faster, better work. Sometimes just the look of change, for a board or a parent company.</p>
<h3 class="kh">Why they repeat</h3>
<p>Because each one changes names and rituals but not decisions, so the problems stay, and the next one is announced.</p>
<h3 class="kh">What makes one work</h3>
<ul class="fears"><li>A specific, measured problem.</li><li>Good coaches with allies.</li><li>Keeping what already works.</li><li>Changing decisions, not just names.</li></ul>
<h3 class="kh">Three kinds of pilgrimage</h3>
<div class="breeds">
<div><b>The Real Journey</b><p>A real problem, measured. Join in and help.</p></div>
<div><b>The Renaming</b><p>New words, same work. Be polite; protect your Keep List.</p></div>
<div><b>The Consultant Crusade</b><p>Imported wholesale, at great expense. Find the real problem inside it anyway.</p></div>
</div>
{note("Ask the coach what problem they've been asked to solve. Good ones will tell you, and be grateful you asked.")}""",
        difficulty=dict(
            normal=dict(who="The Real Journey.",
                        know=["A clear problem is named.", "The coach asks good questions.", "Leaders change their own habits too."],
                        do=["Help measure the problem.", "Share your Keep List.", "Be the coach's ally."],
                        avoid="The eye-roll.",
                        next="If it's mostly new names, you're at Nightmare."),
            nightmare=dict(who="The Renaming.",
                           know=["New titles, same jobs.", "New rituals, same decisions.", "Nobody can say what problem it solves."],
                           do=["Do the Real Problem Hunt yourself.", "Propose a measure.", "Protect what works.", "Go along with the names politely."],
                           avoid="The true believer.",
                           next="If it's breaking what works, you're at Hell."),
            hell=dict(who="The Consultant Crusade.",
                      know=["A huge programme, imported wholesale.", "Teams that worked are being broken up.", "Dissent is called resistance."],
                      do=["Document what's working, with evidence.", "Take the Keep List to the most senior sponsor you can.", "Find allies inside the programme.", "Pick your battles."],
                      avoid="Open war with the programme.",
                      next="It will pass. Keep good records for the fifth one."),
        ),
        mirror=dict(
            title="Are you a transformation ghost?",
            intro="Tick honestly.",
            signs=["You roll your eyes whenever a change programme is mentioned.", "You've adopted a ritual without knowing why.",
                   "You can't say what problem the current change is solving.", "You've renamed something and called it change.",
                   "You've never helped a coach, only judged them."],
            cure="Ask the next coach you meet: “What problem are you here to fix?” Then offer to help measure it.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 11 September 2029, the Insight Squad's first session with Juno.",
            intro="The Real Problem Hunt.",
            lines=[
                ("Juno", "I'm the fourth agile coach you've had. I know. What takes too long here?"),
                ("Pip", "Honestly? Getting work approved. I measured it once: eleven weeks from idea to start."),
                ("Juno", "Eleven weeks. Where does it go?"),
                ("Pip", "Three sign-offs and a monthly committee."),
                ("Juno", "That's what we fix. Will you measure it every month with me?"),
                ("Pip", "If we can keep Ruth's monthly top three and the Tuesday lunch."),
                ("Juno", "Keep everything that works. I'm here for the eleven weeks."),
            ],
            note="Juno is the first coach the Chronicler has ever invited to lunch.",
        ),
    ),
    # ------------------------------------------------------------------ the Slack Channel Necropolis
    "slack-channel-necropolis": dict(
        sighting=f"""{beat("Wednesday 2 January 2030 · the census")}
<p>Back from Christmas, Pip had 1,402 unread messages. He counted his channels: <b>183</b>. Twelve had a message in the
last month that mattered to him. The rest were tombs: #proj-lumen-old-DO-NOT-USE, #random-2,
#ascend2030-announcements-official-v2, #cake-floor-22 (floor 22 had closed in September). Hugo was in 412.</p>
{beat("January · the missed decision")}
<p>Rafi spent a week building a forecast on May's data. The decision to use June's had been made in a thread in
#insight-squad-general on 19 December, at 17:48, by two people, and never written anywhere else.</p>
{beat("Friday 4 January · the Great Muting")}
<p>Pip left 160 channels in an afternoon. Nothing bad happened. He proposed to the team: every new channel gets a purpose
line and an end date; decisions in chat get written in the project log, with a link. Juno liked it so much they made it
part of Ascend's guidance.</p>
{beat("Friday 14 February · the day of the dead")}
<p>Juno and IT archived 2,600 dead channels across MetroVolt in one day. Hugo's @channel to 3,000 people about cake in
kitchen 14 was, by consensus, the last one. He has not used @channel since.</p>
{note("Most channels are tombs. Leave the dead in peace and spend your attention on the living.")}""",
        origin=dict(
            title="How the necropolis grew",
            beats=[
                ("2014 · the first channels", "Slack arrives. Ten channels, all lively. It's faster than email. Everyone loves it."),
                ("2018 · a channel per project", "Every project gets a channel. Projects end. Channels don't. Nobody has the job of closing them."),
                ("2022 · the sprawl", "Thousands of channels. People join everything, in case. Decisions happen in threads that half the team never sees."),
                ("2030 · the census", "Pip counts 183. Hugo counts 412. MetroVolt has 4,100. About 400 are alive."),
            ],
            turning="Making channels free and easy to create, and nobody's job to close.",
            saved="A purpose line and an end date on every channel from the start, and one person per project who archives.",
            note="Tools that are easy to start and nobody's job to end always become graveyards. Give endings an owner.",
        ),
        know=f"""<p>Chat tools make it easy to create channels for every project, team and topic. Over time most go quiet but stay
open, still notifying, still holding old decisions. People join everything for fear of missing out, then miss what
matters in the noise.</p>
<h3 class="kh">What it wants</h3>
<p>Your attention, constantly, in small pieces.</p>
<h3 class="kh">Why it grows</h3>
<p>Because creating a channel is free, closing one is nobody's job, and leaving one feels risky.</p>
<h3 class="kh">What tames it</h3>
<ul class="fears"><li>Leaving and muting freely.</li><li>A purpose and an end date.</li><li>Decisions written somewhere permanent.</li><li>Rare, careful @channel.</li></ul>
<h3 class="kh">Three kinds of channel</h3>
<div class="breeds">
<div><b>The Living</b><p>Active, purposeful. Stay.</p></div>
<div><b>The Undead</b><p>Quiet but still notifying. Mute.</p></div>
<div><b>The Tomb</b><p>Finished, abandoned. Leave, and suggest archiving.</p></div>
</div>
{note("If something matters to you, someone will tell you directly. If they won't, a channel won't save you.")}""",
        difficulty=dict(
            normal=dict(who="A few too many channels.",
                        know=["You're in dozens.", "Most are quiet.", "Notifications are manageable."],
                        do=["Do the Great Muting once a quarter.", "Turn off notifications for most.", "Keep a short list of the living."],
                        avoid="Living in the tombs.",
                        next="If you're missing decisions, you're at Nightmare."),
            nightmare=dict(who="Decisions in the noise.",
                           know=["Important things are decided in threads.", "People miss them.", "Work is redone."],
                           do=["Push for the Decision Rule.", "Write decisions in one permanent place.", "Ask for a weekly summary.", "Say when you've missed one, calmly."],
                           avoid="The channel spawn.",
                           next="If the noise is constant and expected, you're at Hell."),
            hell=dict(who="The Always-On Necropolis.",
                      know=["Instant replies are expected.", "Hundreds of channels, all “important”.", "Your focus time is gone."],
                      do=["Agree response-time norms with your manager.", "Block focus time.", "Batch chat twice a day.", "Read the Green Dot of Doom."],
                      avoid="The @channel curse.",
                      next="If it's damaging your health, read Act VIII."),
        ),
        mirror=dict(
            title="Are you building the necropolis?",
            intro="Tick honestly.",
            signs=["You've created a channel without a purpose line.", "You've never archived a channel you started.",
                   "You've used @channel for something that mattered to fewer than ten people.", "You've made a decision in a thread and not written it anywhere else.",
                   "You're in more channels than you can name."],
            cure="Archive one channel you created that's finished. Then leave five you haven't read this month.",
        ),
        rehearsal=dict(
            title="Scene: Friday 4 January 2030, the Insight Squad's Friday meeting.",
            intro="The Purpose Line and the Decision Rule.",
            lines=[
                ("Pip", "Rafi lost a week because the June-data decision was in a thread. That's not his fault. It's ours."),
                ("Rafi", "It was at 17:48 on the nineteenth of December. I checked."),
                ("Pip", "Proposal: decisions made in chat go in the project log, with a link. And every new channel gets a purpose and an end date."),
                ("Juno", "Can I steal that for all of Ascend?"),
                ("Pip", "Please."),
            ],
            note="On 14 February, 2,600 channels were archived. The Chronicler held a small wake for #cake-floor-22.",
        ),
    ),
    # ------------------------------------------------------------------ the Performative Busy-ness Dance
    "performative-busyness": dict(
        sighting=f"""{beat("November 2029 · the dance")}
<p>Hugo's week: 54 meetings. Emails timed to send at 06:12. A green dot (honest now, after the fire drill) from 07:00 to
22:00. Every conversation began with “crazy week”. He sighed audibly at every desk he passed. People said he was the
hardest-working person on floor 14.</p>
{beat("The quiet corner")}
<p>Asha, at GridSight, had shipped Northshire's phase-two forecasts three days early, run the client workshop, and left
at 16:30 every day to collect her son. Nobody said she was hard-working. Nobody said she wasn't. Nobody noticed.</p>
{beat("Thursday 12 December · calibration")}
<p>Rupert praised Hugo's “extraordinary commitment”. Ruth, in the room, asked one question: which of the programme's eleven
milestones had been delivered? Three. Asha's GridSight work had hit all of its, early. Ruth, who had read the Calibration
Council in Act IV, said so, with numbers.</p>
{beat("Tuesday 14 January 2030 · Hugo")}
<p>Hugo found Pip in the kitchen and said, quietly, that he was exhausted, and didn't know how to stop. Pip showed him his
Outcome Ledger: one line per week, what got finished. Hugo cancelled twenty meetings the next day. Two of his milestones
moved in a fortnight. He still says “crazy week”, but now he sounds surprised by it.</p>
{note("The dance is exhausting to do and to watch. Sit it out. Ship something.")}""",
        origin=dict(
            title="How Hugo learned to dance",
            beats=[
                ("2015 · his first boss", "Hugo's first manager judged people by who was in earliest and left latest. Hugo learned to be visible first, effective second."),
                ("2021 · the remote years", "With nobody to see him, Hugo fills his calendar and his chat with proof of life."),
                ("2026 · Lumen", "Act II's Hugo: always on Slack, never sleeping. It worked; he was promoted. The dance was rewarded."),
                ("2029 · the peak", "Fifty-four meetings a week. Three milestones of eleven. And, by January, a man who can't stop."),
            ],
            turning="A first boss who rewarded being seen, and every boss since who didn't ask what was delivered.",
            saved="One manager, at any point, asking “What did you finish this month?”",
            note="Most performative busy-ness isn't fakery. It's anxiety, trained by bosses who measured the wrong thing.",
        ),
        know=f"""<p>Performative busy-ness is the visible display of being busy (full calendars, early emails, constant availability,
talk about how busy you are) as a substitute for, or distraction from, results. It's often rewarded, because it's easy to
see, and it's contagious, because nobody wants to look less busy than the person next to them.</p>
<h3 class="kh">What it wants</h3>
<p>To be seen as committed. Usually from fear of being seen as lazy.</p>
<h3 class="kh">Why it's rewarded</h3>
<p>Because effort is visible and outcomes take effort to check. Busy people look valuable until someone counts.</p>
<h3 class="kh">What beats it</h3>
<ul class="fears"><li>Counting outcomes.</li><li>Protected focus time.</li><li>Leaders who leave on time.</li><li>Not joining the competition.</li></ul>
<h3 class="kh">Three kinds of dancer</h3>
<div class="breeds">
<div><b>The Anxious Dancer</b><p>Afraid to look idle. Show them the Outcome Ledger.</p></div>
<div><b>The Competitive Dancer</b><p>Out-busies everyone. Don't compete; ship.</p></div>
<div><b>The Exhausted Dancer</b><p>Can't stop. Needs help, not judgment. See Act VIII.</p></div>
</div>
{note("If you manage people, the most powerful thing you can do is leave on time, visibly, having finished something.")}""",
        difficulty=dict(
            normal=dict(who="The Anxious Dancer, nearby.",
                        know=["A colleague performs busy-ness.", "It doesn't affect you much.", "Your outcomes are visible."],
                        do=["Keep your Outcome Ledger.", "Use the Calm Answer.", "Protect your focus time."],
                        avoid="The busy competition.",
                        next="If busy-ness is what gets rewarded, you're at Nightmare."),
            nightmare=dict(who="The Rewarded Dance.",
                           know=["Leaders praise long hours.", "Quiet effective people are overlooked.", "You feel pressure to dance."],
                           do=["Make your outcomes visible weekly.", "Ask your manager to judge on outcomes.", "Find a sponsor (Act IV).", "Keep your hours sane."],
                           avoid="The scheduled send at 06:12.",
                           next="If the dancer is you, and you can't stop, you're at Hell."),
            hell=dict(who="The Exhausted Dancer is you.",
                      know=["You can't remember your last free evening.", "Your calendar runs your life.", "You're not sure what you've achieved."],
                      do=["Write down what you finished last month.", "Cancel a third of your meetings.", "Tell someone you trust.", "Read Act VIII, the Slow Hex of Burnout."],
                      avoid="The meeting hoard.",
                      next="If you can't stop on your own, get help. That's not weakness."),
        ),
        mirror=dict(
            title="Are you dancing?",
            intro="Tick honestly.",
            signs=["You've said “crazy week” more than twice this week.", "You've scheduled an email to send early to look keen.",
                   "You've accepted a meeting just to be seen in it.", "You feel guilty leaving on time.",
                   "You can list your meetings but not your outcomes."],
            cure="Write down three things you finished this month. If it's hard, cancel three meetings next week and finish something.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 14 January 2030, the kitchen on floor 14.",
            intro="The Outcome Ledger, offered kindly.",
            lines=[
                ("Hugo", "Can I ask you something? How do you leave at half five?"),
                ("Pip", "I finish things. I keep a list: one line a week, what got done. When the line's there, I go home."),
                ("Hugo", "I've got fifty-four meetings this week. I don't know what I've finished."),
                ("Pip", "Which three would you miss if they vanished?"),
                ("Hugo", "…Three. Out of fifty-four."),
                ("Pip", "Then try keeping those, and finishing one thing by Friday."),
            ],
            note="Hugo cancelled twenty meetings the next day. Nobody complained. Three people thanked him.",
        ),
    ),
    # ------------------------------------------------------------------ the Pivot Storm
    "pivot-storm": dict(
        sighting=f"""{beat("July 2029 · the first wind")}
<p>Ascend 2030's Q3 priority: <b>Customer First</b>. Pip's team built a roadmap around complaints, churn and satisfaction.
Ruth presented it in August. It was praised.</p>
{beat("October · the second wind")}
<p>Q4's priority: <b>Cost Leadership</b>. Every roadmap was to be rebuilt around savings. Pip's team rebuilt theirs in a
week. The complaints work was paused, half-finished. The churn model, half-built, was moved to “later”.</p>
{beat("January 2030 · the third wind")}
<p>Q1's priority: <b>AI First</b>. A third roadmap. Rafi asked, quietly, whether there was any point finishing anything.
Pip asked Ruth the What-Changed Question: of the team's seven projects, which actually stopped under AI First? They went
through it line by line. <b>One.</b> The slides had changed completely. The work had barely changed at all.</p>
{beat("February · the shelter")}
<p>Pip picked the work that mattered under all three winds: the churn model (customers, costs and AI, all at once). The
team finished it in five weeks, in small pieces. It was used in all three strategies' reports. Ruth stopped passing each
new slogan straight down; she started translating it first. In March, Dame Helena announced the 2030 strategy would
“stay stable for at least a year”. The Chronicler said they'd believe it in April 2031.</p>
{note("Find the work that matters in every wind. Finish it. Storms can't move finished things.")}""",
        origin=dict(
            title="How the storm began",
            beats=[
                ("2028 · the parent group", "The parent group reviews strategy quarterly, for every company it owns. Each review produces a new priority."),
                ("2029 · Rupert's slogans", "Rupert turns each quarter's priority into a slogan for MetroVolt: Customer First, Cost Leadership, AI First."),
                ("The cascade", "Every layer passes the slogan down unchanged. Teams rebuild roadmaps from scratch, each quarter."),
                ("The truth beneath", "The underlying work barely changes. Customers still leave; costs still matter; AI still needs data. Only the slides change."),
            ],
            turning="Treating every quarterly emphasis as a new strategy, and passing it down without translation.",
            saved="One manager at each level asking “What actually changes for our work?” before passing the wind on.",
            note="Most pivots change the words more than the work. Find the work that doesn't change, and protect it.",
        ),
        know=f"""<p>A pivot storm is when an organisation's priorities change so often that work is constantly restarted and rarely
finished. Sometimes the changes are real and necessary. Often they're changes of emphasis, amplified into full rewrites as
they pass down the layers. Teams lose faith in plans, and in finishing anything.</p>
<h3 class="kh">What it wants</h3>
<p>To look responsive. Sometimes it genuinely is responding to a changing world.</p>
<h3 class="kh">Why it's so damaging</h3>
<p>Because half-finished work in every direction delivers nothing, and teams that never finish stop believing.</p>
<h3 class="kh">What survives it</h3>
<ul class="fears"><li>Work that matters under every strategy.</li><li>Small pieces, finished.</li><li>Managers who translate, not relay.</li><li>Asking what really changed.</li></ul>
<h3 class="kh">Three kinds of storm</h3>
<div class="breeds">
<div><b>The Real Change</b><p>The world changed; so must you. Adapt, and finish what still matters.</p></div>
<div><b>The Slogan Storm</b><p>New words, mostly the same work. Translate it; protect the shelter work.</p></div>
<div><b>The Chaos Storm</b><p>Nobody knows what matters. Finish small things and ask for a priority in writing.</p></div>
</div>
{note("If you manage a team: you are the roof. Let some rain through, not all of it.")}""",
        difficulty=dict(
            normal=dict(who="The Real Change.",
                        know=["The reason for the pivot is clear.", "It happens rarely.", "Some work genuinely stops."],
                        do=["Ask what changes for you.", "Finish what still matters.", "Adapt the rest calmly."],
                        avoid="The cynical freeze.",
                        next="If it happens every quarter, you're at Nightmare."),
            nightmare=dict(who="The Slogan Storm.",
                           know=["A new priority every quarter.", "Roadmaps rewritten each time.", "Little gets finished."],
                           do=["Ask the What-Changed Question.", "Find the Shelter Work.", "Break work into small finishes.", "Show leaders what's been finished."],
                           avoid="The instant rebuild.",
                           next="If nobody knows what matters at all, you're at Hell."),
            hell=dict(who="The Chaos Storm.",
                      know=["Conflicting priorities at once.", "Nobody can say what matters most.", "Your team has stopped believing."],
                      do=["Ask your manager for the top three, in writing.", "Finish small things anyway.", "Protect your team from whiplash.", "Tell leaders kindly what it's costing."],
                      avoid="The team whiplash.",
                      next="If it never settles, ask whether this is a place you can do good work. Read Act VIII."),
        ),
        mirror=dict(
            title="Are you the wind?",
            intro="If you lead anything. Tick honestly.",
            signs=["You've passed a new priority to your team without translating it.", "Your team has rebuilt its plan more than twice this year.",
                   "You can't name what your team finished last quarter.", "You've changed direction because of a slide, not a fact.",
                   "Your team has stopped asking about long-term plans."],
            cure="Before passing on the next change, ask: “What actually changes for us?” Pass on that, and nothing else.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 7 January 2030, Pip's 1:1 with Ruth.",
            intro="The What-Changed Question.",
            lines=[
                ("Pip", "AI First. That's our third roadmap in six months. Rafi asked if there's any point finishing anything."),
                ("Ruth", "Fair question. What do you suggest?"),
                ("Pip", "Let's go through our seven projects. Which actually stop under AI First?"),
                ("Ruth", "…Only the satisfaction survey redesign, I think."),
                ("Pip", "So six carry on. And the churn model matters under all three strategies. Can we finish it, whatever?"),
                ("Ruth", "Yes. And from now on I'll translate the slogans before they reach you."),
            ],
            note="The churn model shipped on 21 February. It's the only piece of work cited in all three quarters' strategy reports.",
        ),
    ),
}
