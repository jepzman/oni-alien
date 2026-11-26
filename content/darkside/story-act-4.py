# Series 4 · Act IV · the long-form story fields, merged into content/darkside/act-4.py by scripts/grimoire.py.
# October 2027 to May 2028. The Head of Customer Insight role; Pip acting from October; Ruth Calloway appointed in March.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the Promotion Prophecy
    "promotion-prophecy": dict(
        sighting=f"""{beat("Monday 4 October 2027 · the announcement")}
<p>Priya was promoted to Director of Customer. In the same email: a new role, <b>Head of Customer Insight</b>, would be
“advertised in the new year through our usual fair process”.</p>
{beat("Tuesday 5 October · floor 27")}
<p>Tamsin, bringing tea into Ottoline's office, overheard two names in the first minute: Priya said “Pip”, Ottoline said
“and the woman from Northgate Energy, if we can get her”. The formal process was three months away. The prophecy was
already being written.</p>
{beat("October to December · the visible slice")}
<p>Pip, who had read this entry, told Priya that week that he wanted the role. She made him acting head (see the Poisoned
Chalice). Dorian told nobody he wanted it, and spent October building a beautiful deck for an interview that wouldn't
happen until February.</p>
{beat("January · the advert")}
<p>The role was advertised. By then three people already knew who the real candidates were. None of them was on the
interview panel. All of them were in the room where the panel's recommendation would be discussed.</p>
{note("The job advert is the last page of the prophecy. Get into the first chapter.")}""",
        origin=dict(
            title="How MetroVolt's promotions came to be decided in advance",
            beats=[
                ("2012 · the open competition", "MetroVolt runs a fully open process for a senior role. The best interviewee wins, then fails within a year. Leadership decides interviews alone aren't enough."),
                ("2014 · talent reviews", "Twice a year, leaders discuss “who's ready for what”. It's sensible succession planning. It also means names are attached to roles long before they exist."),
                ("2019 · the CEO's circle", "Dame Helena and Ottoline start reviewing every senior appointment informally first. Formal processes continue, but their outcome is usually known."),
                ("2027 · the prophecy", "By the time Head of Customer Insight is advertised, it has been discussed in four talent reviews and two cups of tea. The process is real. It just isn't where the decision starts."),
            ],
            turning="A sensible fix (don't decide on interviews alone) that moved the real decision months earlier, where most candidates never see it.",
            saved="Nothing needs saving; succession planning is normal. What helps is candidates knowing it happens, and declaring early.",
            note="The process isn't fake. It's just the second half. The first half happens in talent reviews, sponsors' conversations and cups of tea.",
        ),
        know=f"""<p>Most organisations decide promotions in two stages: an informal one (talent reviews, sponsors, “who's ready?”)
months before, and a formal one (advert, interviews, panel) that mostly confirms it. You can't skip the formal stage. But
the informal one decides who's seriously considered.</p>
<h3 class="kh">What the deciders want</h3>
<p>Confidence. They want someone they've seen doing parts of the job already, recommended by someone they trust.</p>
<h3 class="kh">Why it works this way</h3>
<p>Because senior appointments are risky and interviews are poor predictors. People trust what they've seen over what they've heard in an hour.</p>
<h3 class="kh">What gets you into the prophecy</h3>
<ul class="fears"><li>Declaring your interest early.</li><li>Doing a visible slice of the next job.</li><li>A sponsor who says your name.</li><li>Evidence your manager can repeat.</li></ul>
<h3 class="kh">Three kinds of prophecy</h3>
<div class="breeds">
<div><b>The Open Field</b><p>Genuinely undecided. The process matters a lot.</p></div>
<div><b>The Favourite</b><p>A name is already attached. Make sure yours is too.</p></div>
<div><b>The Outsider</b><p>Leadership wants someone from outside. Know this early; it changes your odds.</p></div>
</div>
{note("Ask your manager: “Who else is being talked about?” Many will tell you, and it's the most useful thing you'll hear.")}""",
        difficulty=dict(
            normal=dict(who="The Open Field.",
                        know=["Nobody has been named.", "The process is new.", "Your manager is neutral."],
                        do=["Declare early.", "Ask what they'd need to see.", "Prepare well for the formal process."],
                        avoid="Waiting for the advert.",
                        next="If a favourite exists and it isn't you, you're at Nightmare."),
            nightmare=dict(who="The Favourite, and it's not you yet.",
                           know=["Another name keeps coming up.", "They're doing the future job's visible work.", "Your manager is vague."],
                           do=["Do the Early Declaration plainly.", "Ask for a visible slice of the job.", "Find a sponsor.", "Ask who else is being talked about."],
                           avoid="The rival's rumour.",
                           next="If leadership wants an outsider, you're at Hell."),
            hell=dict(who="The Outsider: leadership wants someone from outside.",
                      know=["An external candidate is being courted.", "Your sponsor says “it's complicated”.", "The role's description fits someone else's CV."],
                      do=["Go for it anyway; it's good evidence for next time.", "Ask your sponsor honestly about the odds.", "Plan what you'll learn either way.", "Read Passed Over before the decision."],
                      avoid="The self-coronation.",
                      next="If you're passed over, read Passed Over: The Resurrection."),
        ),
        mirror=dict(
            title="Are you in the prophecy?",
            intro="Check whether anyone deciding knows you want the next job. Tick honestly.",
            signs=["You've never told your manager which role you want next.", "You're waiting for roles to be advertised.", "No senior person has seen you do any part of the next job.",
                   "You don't know who decides promotions in your area.", "You think the formal process is the whole story."],
            cure="This week, tell your manager the next role you want, and ask what they'd need to see. That one sentence puts you in the first chapter.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 6 October 2027, Pip's 1:1 with Priya.",
            intro="The Early Declaration and the Future-Job Evidence.",
            lines=[
                ("Pip", "Priya, I'd like to be considered for Head of Customer Insight. Can we talk about what you'd need to see?"),
                ("Priya", "I'm glad you asked. Honestly, the gap is the planners. You've never led Dorian's team."),
                ("Pip", "Could I run the joint planning review next quarter? It's the part I haven't done."),
                ("Priya", "Better: act up as head from November while we recruit. You'd lead both teams."),
                ("Pip", "I'd love that. Can we agree terms? I've read about poisoned chalices."),
                ("Priya", "Of course you have. Send me what you need."),
            ],
            note="Pip's sentence put his name next to Priya's, in her talks with Ottoline, three months before the advert.",
        ),
    ),
    # ------------------------------------------------------------------ the Invisible Work Curse
    "invisible-work-curse": dict(
        sighting=f"""{beat("Every week · Asha")}
<p>Asha onboarded every new joiner. She kept the data dictionary up to date. She ran the team rota, took notes in every
meeting, and remembered birthdays. In 2027 she onboarded four people and answered, by her own count, 312 “quick
questions” about the data.</p>
{beat("Friday 10 December · her review")}
<p>Asha's review, written by Pip, said: <i>“Great team player. Solid analysis.”</i> It did not mention onboarding, the
dictionary or the 312 questions. Pip had written it in twenty minutes. He had not noticed what he hadn't written.</p>
{beat("Monday 13 December")}
<p>Asha asked, quietly, why the onboarding wasn't in her review. Pip opened his mouth and realised he had no idea how much
of the team's smoothness came from her. He'd thought it just… happened.</p>
{beat("That week")}
<p>Pip counted. Asha spent roughly a day a week on glue work. Without it, the four new joiners would have taken six weeks
each to get productive instead of two. Nobody had ever written that number down.</p>
{note("Glue holds everything together. That's exactly why it's invisible. Make it visible.")}""",
        origin=dict(
            title="How the glue came to stick to Asha",
            beats=[
                ("2025 · her first week", "Asha joins Customer Ops. The data dictionary is three years out of date. She fixes it, because she needs it. People thank her."),
                ("2026 · the default", "When someone new arrives, people say “ask Asha”. She's helpful, so she helps. Onboarding becomes hers without anyone deciding it."),
                ("2027 · the weight", "Asha does a day a week of glue work. Her objectives, written by a manager who never saw it, list only analysis."),
                ("December 2027 · the review", "Her review praises her as a “team player”, which is how reviews describe glue work they can't see."),
            ],
            turning="Fixing one thing because it needed fixing, and becoming the person who fixes everything, without it ever being agreed.",
            saved="One sentence from a manager in 2026: “You're doing the onboarding now; let's put it in your objectives.”",
            note="Glue work often falls on the most helpful people, and disproportionately on women. If you manage a team, go and look for it.",
        ),
        know=f"""<p>Glue work is the essential, unglamorous work that keeps a team running: onboarding, documentation, notes, rotas,
coordination. Everyone depends on it, but it rarely appears in objectives or reviews, so the people doing it get “team
player” instead of promotions.</p>
<h3 class="kh">What it is</h3>
<p>Work that makes everyone else's work possible: knowledge, coordination, care. Remove it and things quietly stop working.</p>
<h3 class="kh">Why it stays invisible</h3>
<p>Because it prevents problems instead of producing outputs. Nobody notices a crisis that didn't happen, or a new joiner who got productive fast.</p>
<h3 class="kh">What makes it count</h3>
<ul class="fears"><li>Writing it down with the time it takes.</li><li>Measuring its outcome.</li><li>Putting it in objectives.</li><li>Sharing it on a rota.</li></ul>
<h3 class="kh">Three kinds of glue</h3>
<div class="breeds">
<div><b>The Knowledge Glue</b><p>Documentation, dictionaries, answers. Measure questions answered and time saved.</p></div>
<div><b>The People Glue</b><p>Onboarding, mentoring, morale. Measure time-to-productive.</p></div>
<div><b>The Admin Glue</b><p>Notes, rotas, organising. Share it on a rota.</p></div>
</div>
{note("“Team player” in a review often means “did lots of things nobody measured”. Measure them.")}""",
        difficulty=dict(
            normal=dict(who="Glue work that's noticed but not counted.",
                        know=["People thank you.", "It's not in your objectives.", "Your manager would add it if asked."],
                        do=["Write it down with the time it takes.", "Ask for it in your objectives.", "Measure one outcome."],
                        avoid="The silent saint.",
                        next="If it's invisible and growing, you're at Nightmare."),
            nightmare=dict(who="Glue work that's invisible and growing.",
                           know=["It takes a day a week or more.", "Your review says “team player”.", "Others have stopped doing any."],
                           do=["Do the Naming with your manager.", "Propose a rota.", "Ask for the most valuable glue to count in your review.", "Drop or share the least valuable."],
                           avoid="The sudden strike.",
                           next="If it's holding back your promotion, you're at Hell."),
            hell=dict(who="Glue work blocking your career.",
                      know=["Peers with less impact are promoted.", "You're described as “supportive”, not “strong”.", "The glue keeps landing on you."],
                      do=["Raise it formally in your review, with numbers.", "Hand over glue work explicitly, with dates.", "Ask your sponsor to describe its value in calibration.", "Consider whether the culture can change."],
                      avoid="The martyr's ledger: reminding everyone constantly.",
                      next="If nothing changes, take your skills where they'll be counted."),
        ),
        mirror=dict(
            title="Do you see the glue?",
            intro="Especially if you manage people. Tick honestly.",
            signs=["You don't know who onboards new joiners in your team.", "Someone always takes the notes, and it's the same person.", "You've written “team player” in a review without saying what it meant.",
                   "You've never asked anyone how long their glue work takes.", "Things run smoothly and you're not sure why."],
            cure="Ask your team: who does the work that keeps us running? Then make sure it's in someone's objectives, or on a rota.",
        ),
        rehearsal=dict(
            title="Scene: Monday 13 December, Pip and Asha.",
            intro="The Naming and the Count, from the manager's side.",
            lines=[
                ("Asha", "Why isn't the onboarding in my review?"),
                ("Pip", "Because I didn't see it, and that's on me. I'm sorry. How much time does the glue work take?"),
                ("Asha", "About a day a week. Onboarding, the dictionary, the rota, notes."),
                ("Pip", "And the four new joiners got productive in two weeks instead of six. That's twenty weeks of time saved. I'm rewriting the review with that number in it."),
                ("Asha", "…Thank you."),
                ("Pip", "And from January, notes and the rota go on a rotation. The onboarding stays yours, as an objective."),
            ],
            note="One honest apology and one number turned “team player” into evidence for promotion.",
        ),
    ),
    # ------------------------------------------------------------------ the Book of Deeds
    "book-of-deeds": dict(
        sighting=f"""{beat("Every Friday since March · 17:55")}
<p>Since the Chronicler's advice (see Act V, the Go-Bag Scroll), Pip had written one line every Friday: what he'd done,
what it changed, and proof. Some weeks the line was small (“Fixed the dictionary join; Asha's report 4× faster”).
Some were big (“Horizon submission: kept the team; 5% cut instead of 15%”).</p>
{beat("Thursday 2 December · review season")}
<p>Pip's self-assessment took forty minutes instead of four evenings. It had numbers, dates and three thank-you emails.
Dorian's said “various strategic contributions”.</p>
{beat("Monday 6 December · before calibration")}
<p>Pip sent Priya one page: the year in eight lines. She used five of them, word for word, in the calibration meeting.</p>
{beat("January · the interview")}
<p>For the Head of Customer Insight interview, Pip's examples were dated, measured and true. He didn't have to remember
anything. He just had to read.</p>
{note("One line a week is fifty-two lines a year. That's a promotion case, already written.")}""",
        origin=dict(
            title="How the Book of Deeds was first written",
            beats=[
                ("2011 · the Chronicler's first calibration", "The Chronicler is rated “meets expectations” after their best year, because their manager could only remember the last two months."),
                ("2011 · the notebook", "The Chronicler starts a notebook: one line every Friday. It feels silly. It takes two minutes."),
                ("2012 · the next review", "The Chronicler hands their manager a page of twelve months, with numbers. The rating jumps. The manager asks to copy the idea for the whole team."),
                ("2027 · passing it on", "The Chronicler tells Pip about it in a café (Act V). Pip starts that Friday."),
            ],
            turning="A great year forgotten by a manager with a two-month memory.",
            saved="Nothing; this is the cure. The only thing to save is your future self's December.",
            note="Your manager has eight people, two hundred emails a day and a two-month memory. Help them.",
        ),
        know=f"""<p>Reviews, promotions and pay negotiations all run on evidence, and memory is terrible evidence. A Book of Deeds
(sometimes called a brag document) is a running record of what you did and what it changed, written weekly while it's fresh.</p>
<h3 class="kh">What goes in it</h3>
<p>One line a week: what you did, its result (with a number if possible), and proof (a link, an email, a metric).</p>
<h3 class="kh">Why it works</h3>
<p>Because recency bias is real: managers remember the last month. A year of lines corrects it, and gives them sentences they can use.</p>
<h3 class="kh">Where it pays off</h3>
<ul class="fears"><li>Self-assessments.</li><li>Calibration (via your manager).</li><li>Promotion interviews.</li><li>Pay negotiations and CVs.</li></ul>
<h3 class="kh">Three kinds of entry</h3>
<div class="breeds">
<div><b>The Delivery</b><p>Shipped something. Add the result.</p></div>
<div><b>The Rescue</b><p>Fixed something or prevented a problem. Add what would have happened.</p></div>
<div><b>The Multiplier</b><p>Helped others succeed. Add whose success, and how.</p></div>
</div>
{note("Write it on Friday at 17:55. It's the most valuable five minutes of the week, and the least glamorous.")}""",
        difficulty=dict(
            normal=dict(who="No book yet.",
                        know=["Your last self-assessment was painful.", "You can't remember the spring.", "You have evidence scattered in emails."],
                        do=["Start this Friday: one line.", "Backfill the last month from your sent items.", "Set a recurring reminder."],
                        avoid="The December scramble.",
                        next="If review season is close and the book is empty, you're at Nightmare."),
            nightmare=dict(who="Review season, empty book.",
                           know=["Reviews are in two weeks.", "You can't remember most of the year.", "Your manager is busy."],
                           do=["Mine your sent items, calendar and chats for the year.", "Write ten lines with numbers.", "Send your manager one page.", "Start the weekly habit afterwards."],
                           avoid="The inflated deed: rounding up when you're not sure.",
                           next="If your manager ignores your evidence, you're at Hell."),
            hell=dict(who="Your evidence is ignored.",
                      know=["Your review contradicts your book.", "Your manager won't discuss it.", "Calibration went badly."],
                      do=["Ask, in writing, how your evidence was considered.", "Share it with your skip-level or sponsor.", "Use the formal review appeal if there is one.", "Use the book for your CV: it's yours."],
                      avoid="The shared credit theft: claiming team results as yours to compensate.",
                      next="If your work is never recognised, the book is also your next job's evidence."),
        ),
        mirror=dict(
            title="Is your book open?",
            intro="Tick honestly.",
            signs=["You couldn't list ten things you did this year with numbers.", "Your last self-assessment took more than an evening.", "You rely on your manager to remember your work.",
                   "You've never sent your manager a summary before a review.", "You think writing it down is bragging."],
            cure="Set a reminder for Friday, 17:55: “one line”. Do it for a month. Then never stop.",
        ),
        rehearsal=dict(
            title="Scene: Monday 6 December, Pip emails Priya before calibration.",
            intro="The Shared Scroll: one page your manager can actually use.",
            lines=[
                ("", "Subject: Before calibration: my year in eight lines"),
                ("Pip", "Priya, in case it helps you in the room: 1) Complaint model: repeat calls −9% (£410k). 2) Horizon: team kept; 5% cut not 15%. 3) Acting head since November: joint planning review delivered. 4) Onboarded four people in two weeks each (with Asha). Full list attached."),
                ("Priya", "This is exactly what I needed. I'm using lines 1 to 4 word for word."),
                ("", "In calibration, Priya reads the four lines in under a minute. Ottoline writes one of them down."),
            ],
            note="Pip didn't argue for himself in the room. His book did, through the person who was there.",
        ),
    ),
    # ------------------------------------------------------------------ the Calibration Council
    "calibration-council": dict(
        sighting=f"""{beat("Tuesday 14 December · 09:00 · room 27A")}
<p>Twelve managers, one HR partner, Ottoline at the end of the table, and a nine-box grid on the screen. Sixty names. Four
hours. Four minutes a person, if nobody argued. Everybody argued.</p>
{beat("10:40 · Asha")}
<p>A manager from Network Ops said Asha seemed “quiet in meetings”. Pip, who had rewritten her review, said she'd onboarded
four people in two weeks each and answered 312 data questions. Asha's card stayed in its box.</p>
{beat("11:15 · Pip")}
<p>Priya read four lines about Pip, from his Book of Deeds. Gareth said Pip had been “very helpful on the meter fix”. Ottoline
said nothing, and wrote something down. Pip's card moved up one box.</p>
{beat("11:22 · Dorian")}
<p>Dorian's manager said he'd made “various strategic contributions”. Someone asked for an example. There was a pause long
enough to be noticed. Dorian's card moved down one box. Nobody in the room had seen his work. Several had seen his slides.</p>
{note("You won't be in the room. Make sure your evidence is, and that someone there has seen you.")}""",
        origin=dict(
            title="How the council came to sit",
            beats=[
                ("2015 · the inflation", "Every manager at MetroVolt rates their team highly. 70% of staff are “exceeds expectations”. The ratings mean nothing."),
                ("2016 · calibration", "HR introduces calibration: managers compare ratings across teams and agree a distribution. It's fairer in theory; nobody can inflate alone."),
                ("2017 to 2026 · the theatre", "In practice, the people who do well are those whose managers argue well, and whom senior people have seen. Quiet people and absent managers lose ground."),
                ("2027 · the council", "Sixty names, four hours, a grid. The judgement of a year depends on four minutes and who's in the room."),
            ],
            turning="A fix for inflated ratings that made ratings depend on advocacy and visibility as much as on work.",
            saved="Calibration based on written evidence, prepared in advance, rather than on who argues loudest in the room.",
            note="Calibration isn't random. It's a debate, and debates are won with evidence and witnesses.",
        ),
        know=f"""<p>Calibration is a meeting where managers compare their team's ratings and agree a final distribution. It's meant to
make ratings fair across teams. In practice, your outcome depends on your manager's evidence, how well they argue, and
whether senior people in the room know your work.</p>
<h3 class="kh">What the council wants</h3>
<p>A defensible distribution: not everyone can be top-rated. Clear examples make a rating easy to defend.</p>
<h3 class="kh">Why good people lose ground</h3>
<p>Because their managers are vague, absent or bad at arguing, and nobody senior has seen them. “Quiet” is often said, and rarely challenged.</p>
<h3 class="kh">What wins in the room</h3>
<ul class="fears"><li>Specific examples with numbers.</li><li>Senior people who've seen your work.</li><li>A manager who speaks up.</li><li>Corroboration from other managers.</li></ul>
<h3 class="kh">Three kinds of council</h3>
<div class="breeds">
<div><b>The Fair</b><p>Evidence-based, well-run. Prepare your manager and trust it.</p></div>
<div><b>The Loud</b><p>Wins go to the best arguers. Arm your manager; find corroborators.</p></div>
<div><b>The Fixed</b><p>Outcomes decided by a few. Build relationships with the few.</p></div>
</div>
{note("If anyone in calibration might say “quiet”, make sure someone else is ready to say what you actually did.")}""",
        difficulty=dict(
            normal=dict(who="The Fair council.",
                        know=["Calibration uses written evidence.", "Your manager prepares well.", "Outcomes are explained."],
                        do=["Give your manager three bullets with evidence.", "Ask for a debrief afterwards.", "Act on the feedback."],
                        avoid="The shrug.",
                        next="If the loudest arguers win, you're at Nightmare."),
            nightmare=dict(who="The Loud council.",
                           know=["Ratings depend on who argues.", "Quiet people drift down.", "Your manager isn't a strong advocate."],
                           do=["Arm your manager with sentences they can say out loud.", "Make sure two senior people have seen your work.", "Ask a peer manager who knows your work to corroborate.", "Get a sponsor (see the Sponsor's Mark)."],
                           avoid="The lobby: messaging council members yourself.",
                           next="If outcomes are fixed by a few, you're at Hell."),
            hell=dict(who="The Fixed council.",
                      know=["Ratings mirror a few people's opinions.", "Evidence doesn't change outcomes.", "The same names rise every year."],
                      do=["Build direct relationships with the few, openly.", "Keep your evidence for appeals and CVs.", "Ask for written reasons for your rating.", "Consider where your work would be judged fairly."],
                      avoid="The rating rage.",
                      next="If it's unfair in a way linked to protected characteristics, raise it formally."),
        ),
        mirror=dict(
            title="Would your name survive four minutes?",
            intro="Imagine the council reaching your card. Tick honestly.",
            signs=["Your manager couldn't name three things you did this year, with numbers.", "No senior person in calibration has seen your work.", "Someone might describe you as “quiet”.",
                   "You've never asked what was said about you.", "You've never given your manager anything before calibration."],
            cure="Before the next calibration, give your manager three sentences with evidence, and make sure one more senior person has seen your work this quarter.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 14 December, 10:40. Room 27A. Pip speaks for Asha.",
            intro="The Armed Advocate, from the manager's chair.",
            lines=[
                ("Manager", "Asha seems quite quiet in meetings. Meets expectations?"),
                ("Pip", "She's quiet in meetings and loud in results. She onboarded four people this year, each productive in two weeks instead of six. She answered 312 data questions. And she owns the regulator dashboard."),
                ("Gareth", "I can back that. Her dictionary saved my team a month on the meter fix."),
                ("HR", "So: exceeds?"),
                ("Ottoline", "Exceeds. And let's stop using “quiet” as a rating."),
                ("", "Asha's card moves up one box. Pip tells her the next day exactly what was said, including Gareth's sentence."),
            ],
            note="Two specific sentences and one corroborator beat “quiet”. That's calibration: evidence and witnesses.",
        ),
    ),
    # ------------------------------------------------------------------ the Raise Duel
    "raise-duel": dict(
        sighting=f"""{beat("November · the acting role")}
<p>Pip had been acting Head of Customer Insight since November, leading nine people, on his level-5 salary of £54,000.
The acting allowance he'd asked for “was being looked at”.</p>
{beat("January · the research")}
<p>Pip did what he'd never done: he researched his market. Salary surveys, six job adverts, two recruiters and one honest
conversation with Jules. Heads of insight at similar utilities earned £68,000 to £78,000. Analytics leads, his substantive
role, earned £58,000 to £64,000.</p>
{beat("Thursday 10 February 2028 · 14:00")}
<p>Pip met Priya and Karen from HR. He had a single page: his role, the market range, his results, and a number. His hands
were cold. He said the number. Then he said nothing. It was the longest eleven seconds of his career.</p>
{beat("14:00:11")}
<p>Karen said, “There's no budget for base pay changes this year.” Pip had prepared for that sentence too.</p>
{note("Say the number. Then be quiet. The silence is not your problem.")}""",
        origin=dict(
            title="How the Annotator learned to duel",
            beats=[
                ("2020 · the Annotator's first offer", "Joining MetroVolt, the Annotator accepts the first salary offered, gratefully, without asking. She learns later she was offered £8,000 less than the man hired the same week."),
                ("2021 · the apology", "Asking for a raise, she opens with “sorry, I know it's a bad time”. She gets 2%. The ask had negotiated against itself before it started."),
                ("2023 · freelance", "Self-employed, she has to name her price every week. She learns to say a number, explain it and stop talking."),
                ("2027 · the margins", "She writes this entry so Pip's first duel goes better than hers."),
            ],
            turning="Accepting the first number, and then apologising for asking for a second one.",
            saved="Market data and one sentence: “Based on the role and the market, I'm asking for £X.”",
            note="Nobody ever paid me more for being grateful. They paid me more when I showed them what the work was worth.",
        ),
        know=f"""<p>Pay negotiation is a normal business conversation, not a favour. Organisations expect it, budget for it, and
often pay more to those who ask well. Asking well means: <b>market data</b>, <b>evidence of value</b>, <b>a specific number</b>,
and <b>a plan B</b> if base pay can't move.</p>
<h3 class="kh">What HR wants</h3>
<p>To keep pay within bands and budgets, avoid unfairness between people, and keep good people. Help them do all three.</p>
<h3 class="kh">Why people don't ask</h3>
<p>Fear, gratitude, and the belief that good work will be noticed and rewarded automatically. It's usually noticed. It's rarely rewarded automatically.</p>
<h3 class="kh">What wins the duel</h3>
<ul class="fears"><li>A market range from several sources.</li><li>Your results, in numbers.</li><li>One specific number.</li><li>Silence after you say it.</li></ul>
<h3 class="kh">Three kinds of duel</h3>
<div class="breeds">
<div><b>The Review Duel</b><p>Annual pay review. Bring market data early.</p></div>
<div><b>The Promotion Duel</b><p>New role, new band. Ask before accepting.</p></div>
<div><b>The Retention Duel</b><p>You have an offer elsewhere. Only if you'd really go.</p></div>
</div>
{note("“No budget” usually means “no budget for base pay this year”. Ask about everything else.")}""",
        difficulty=dict(
            normal=dict(who="The Review Duel, with a fair manager.",
                        know=["Pay reviews happen yearly.", "Your manager supports you.", "Bands are published."],
                        do=["Research the market.", "Bring a one-page case and a number.", "Ask early, before budgets are set."],
                        avoid="The apology.",
                        next="If you hear “there's no budget”, you're at Nightmare."),
            nightmare=dict(who="“There's no budget.”",
                           know=["Base pay is frozen.", "Your role has grown.", "HR is sympathetic but stuck."],
                           do=["Plan B: allowance, bonus, title, training, flexibility.", "Ask for a dated review in writing.", "Ask where you sit in the band and why.", "Keep your market data current."],
                           avoid="The comparison with named colleagues.",
                           next="If you're significantly underpaid and nothing moves, you're at Hell."),
            hell=dict(who="Significantly underpaid, nothing moves.",
                      know=["You're well below market.", "Requests are ignored for years.", "New joiners earn more for the same work."],
                      do=["Put it in writing, with evidence.", "If it could be discriminatory, ask about pay equality formally.", "Test the market seriously.", "Decide your walk-away point calmly."],
                      avoid="The bluff.",
                      next="If you get a real offer, read the Escape Portal before deciding."),
        ),
        mirror=dict(
            title="Have you ever duelled?",
            intro="Tick honestly.",
            signs=["You've never asked for a raise.", "You don't know your market rate.", "You accepted your current salary without negotiating.",
                   "You'd start the conversation with “sorry”.", "You believe good work is rewarded automatically."],
            cure="Spend an hour finding three salary data points for your role. Write one sentence with a number. You don't have to use it yet. Just have it ready.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 10 February, 14:00. Pip, Priya and Karen from HR.",
            intro="The Number, the silence, and Plan B.",
            lines=[
                ("Pip", "I've been acting head for three months. Heads of insight at peer utilities earn £68,000 to £78,000. My results are on this page. I'm asking for an acting allowance of £10,000 a year, backdated to November."),
                ("", "Eleven seconds of silence. Pip counts them."),
                ("Karen", "There's no budget for base pay changes this year."),
                ("Pip", "Understood. The allowance isn't base pay. It's for the extra role, until it's filled."),
                ("Karen", "…That's possible. Not £10,000. Perhaps £7,500."),
                ("Pip", "£7,500, backdated to November, in writing, and a review of my base pay in July against the analytics lead band?"),
                ("Priya", "Agreed. Karen?"),
                ("Karen", "Agreed. I'll send it today."),
            ],
            note="Pip got 75% of his ask, backdated, plus a dated review. He'd have got none of it by being grateful.",
        ),
    ),
    # ------------------------------------------------------------------ the Rival for the Throne
    "rival-for-throne": dict(
        sighting=f"""{beat("Monday 10 January 2028 · the advert")}
<p>Head of Customer Insight was advertised. Pip applied that morning. Dorian applied that afternoon. By lunch the next day,
the whole floor knew.</p>
{beat("January · the careful weeks")}
<p>Conversations between them became very polite. Dorian started bringing two coffees again, and Pip, who knew exactly what
that meant from Act II, felt the old tension rise. Colleagues began, quietly, to pick sides: Pip's analysts, Dorian's planners.</p>
{beat("Friday 21 January · the corridor")}
<p>Pip stopped Dorian by the lifts. “We both want this,” he said. “Let's both go for it properly, and whoever doesn't get it,
we stay on good terms. Deal?” Dorian looked at him for a long moment. “Deal,” he said. “And Pip? I'm not doing the coffee
thing. I just like coffee now.”</p>
{beat("February · the interviews")}
<p>Asked about Dorian's weaknesses, Pip said, “He presents better than I do, and he'd be good at it. Here's what I'd bring.”
Asked about Pip, Dorian said, “He builds things. I'd make sure he's on slide one.” The panel looked at each other.</p>
{note("Compete like you'll have to work together afterwards. You will.")}""",
        origin=dict(
            title="How Pip and Dorian came to want the same chair",
            beats=[
                ("March 2026 · the theft", "Dorian presents Pip's forecast as his own (Act II, the Credit Vampire). Pip stares at a hand dryer."),
                ("2026 to 2027 · the distance", "Pip learns to work in daylight. Dorian's department sinks under him (Act V, the Ghost Ship)."),
                ("July 2027 · the lifeboat", "Pip offers Dorian a way into Customer Ops, on one condition: name the builders. Dorian accepts, and keeps the condition."),
                ("January 2028 · the chair", "Both want Head of Customer Insight. Both deserve to be considered. Their history makes the rivalry dangerous, and also makes a clean contest possible."),
            ],
            turning="Two people with a bad history choosing, out loud, to compete cleanly.",
            saved="Nothing needed saving here. The open conversation in the corridor was the saving.",
            note="The rivalry with the most history can be the cleanest, if someone names it first.",
        ),
        know=f"""<p>Competing with a colleague for a promotion is normal and can be healthy. It turns toxic when it goes underground:
undermining, side-taking, quiet sabotage. The cure is to compete <b>openly</b>, on <b>your own results</b>, and to decide in
advance how you'll behave <b>whatever happens</b>.</p>
<h3 class="kh">What both rivals want</h3>
<p>The role, a fair contest, and not to be humiliated. Underneath, usually, to keep working together.</p>
<h3 class="kh">Why rivalries go bad</h3>
<p>Because nobody names them. Silence breeds suspicion, teams pick sides, and every interaction becomes a move.</p>
<h3 class="kh">What keeps it clean</h3>
<ul class="fears"><li>Naming the rivalry openly.</li><li>Your own case, never their weaknesses.</li><li>Graciousness planned in advance.</li><li>Keeping your teams out of it.</li></ul>
<h3 class="kh">Three kinds of rival</h3>
<div class="breeds">
<div><b>The Sporting</b><p>Competes fairly. Match them; you'll both be stronger.</p></div>
<div><b>The Anxious</b><p>Competes nervously, may slip into whispering. Name it early.</p></div>
<div><b>The Ruthless</b><p>Will undermine. Stay in daylight; see Act II, the Doppelgänger.</p></div>
</div>
{note("Whatever happens, one of you will report to the winner, or work beside them. Behave accordingly.")}""",
        difficulty=dict(
            normal=dict(who="The Sporting rival.",
                        know=["You get on well.", "Both of you are open about applying.", "The process is fair."],
                        do=["Name it and agree to stay friends.", "Make your own case.", "Plan your graceful outcome."],
                        avoid="The sore winner.",
                        next="If tension grows and teams pick sides, you're at Nightmare."),
            nightmare=dict(who="The Anxious rival, and a split team.",
                           know=["Conversations are careful.", "Colleagues are taking sides.", "You hear second-hand comments."],
                           do=["Have the open conversation in private.", "Tell your team to stay out of it.", "Keep collaborating visibly.", "Talk about your plan, not their gaps, in interviews."],
                           avoid="The shadow campaign.",
                           next="If your rival is actively undermining you, you're at Hell."),
            hell=dict(who="The Ruthless rival.",
                      know=["Your work is being undermined.", "Comments about you reach the panel.", "Your rival controls something you need."],
                      do=["Stay in daylight: record, collaborate in writing.", "Raise specific interference with your manager.", "Make your case on evidence.", "Read Act II, the Doppelgänger."],
                      avoid="Sabotage in return.",
                      next="If the contest is unfair, ask HR about the process before the decision."),
        ),
        mirror=dict(
            title="How do you compete?",
            intro="Tick honestly.",
            signs=["You've hoped a rival's project would fail.", "You've mentioned a rival's weakness to someone deciding.", "You avoid your rival since the role was advertised.",
                   "Your team has picked a side and you haven't stopped them.", "You haven't thought about how you'd behave if you lost."],
            cure="Say it out loud to your rival: we both want this, let's compete fairly. Then plan your congratulations speech, for either outcome.",
        ),
        rehearsal=dict(
            title="Scene: Friday 21 January, by the lifts on floor 9.",
            intro="The Open Rivalry.",
            lines=[
                ("Pip", "Dorian. We both want this. Let's both go for it properly, and whoever doesn't get it, we stay on good terms. Deal?"),
                ("Dorian", "…Deal. Honestly, I've been dreading this."),
                ("Pip", "Me too. And let's tell our teams to stay out of it."),
                ("Dorian", "Agreed. And Pip? I'm not doing the coffee thing. I just like coffee now."),
                ("Pip", "I know. I've seen the slides. My name's on them."),
                ("", "Neither gets the job (see Passed Over). Both congratulate Ruth on the same morning, standing side by side."),
            ],
            note="The rivalry with the worst history became the cleanest contest on floor 9, because one sentence was said in a corridor.",
        ),
    ),
    # ------------------------------------------------------------------ the Title Without the Gold
    "title-without-gold": dict(
        sighting=f"""{beat("Friday 5 November 2027 · 16:40 · the email")}
<p>Jules was promoted to <b>Principal Analyst</b>, Grid Analytics. The email from Victor's successor praised Jules's
“strategic impact” and listed four new responsibilities. It did not mention pay.</p>
{beat("16:42")}
<p>Jules replied: “Thank you so much! Delighted to accept!” with two exclamation marks. Jules had wanted this for two years.</p>
{beat("Monday 8 November")}
<p>Jules asked about the salary. “It'll be reviewed in the next cycle,” said HR. The next cycle was in April. Principal sat
in a pay band that started £9,000 above Jules's salary.</p>
{beat("April 2028")}
<p>In the April cycle, Jules got 3%, the same as everyone. Jules was now a Principal paid below the Principal band, with four
new responsibilities. Jules told Pip over coffee, angry mostly at themself: “I said yes before I asked.”</p>
{note("Ask about the gold before you put on the crown.")}""",
        origin=dict(
            title="How titles came loose from their gold",
            beats=[
                ("2020 · the frozen budget", "During the hiring freeze (Act V), MetroVolt can't raise pay but wants to keep people. It starts promoting “in title”, with pay to follow."),
                ("2021 · the habit", "Title promotions are cheap and popular. Pay rarely catches up, because the next cycle has its own budget limits."),
                ("2024 · the gap", "HR notices dozens of staff paid below their own band. Fixing it would cost millions. It goes on a list."),
                ("2027 · Jules", "Jules is promoted in title, off-cycle, by email. The pay is “next cycle”. The list gets one name longer."),
            ],
            turning="Using titles as a cheaper substitute for pay, and promising the pay later.",
            saved="One question before accepting: “What's the salary?” Jules's leverage disappeared with the word “delighted”.",
            note="The moment of greatest leverage is between the offer and your yes. Spend it wisely.",
        ),
        know=f"""<p>A promotion without a raise is common, especially when budgets are tight. Sometimes it's a genuine stepping stone.
Often it's a cheaper way to keep you. Your leverage is highest <b>before you accept</b>; after that, pay depends on the next
cycle's budget and everyone else's needs.</p>
<h3 class="kh">What the organisation wants</h3>
<p>To recognise and keep you, at the lowest cost this year.</p>
<h3 class="kh">Why the gold doesn't follow</h3>
<p>Because “next cycle” has its own budget, and you're no longer a retention risk once you've said yes.</p>
<h3 class="kh">What gets you the gold</h3>
<ul class="fears"><li>Asking about pay before accepting.</li><li>Knowing the band for the new role.</li><li>A dated, written promise.</li><li>Raising it promptly if forgotten.</li></ul>
<h3 class="kh">Three kinds of crown</h3>
<div class="breeds">
<div><b>The Stepping Stone</b><p>A title now, pay agreed in writing for a date. Fine.</p></div>
<div><b>The Paper Crown</b><p>Title only, vague “next cycle”. Negotiate before yes.</p></div>
<div><b>The Crown of Thorns</b><p>Title, more work, no pay, no promise. Think carefully.</p></div>
</div>
{note("“Delighted to accept” is a lovely sentence. Say it after “what's the salary?”")}""",
        difficulty=dict(
            normal=dict(who="The Stepping Stone.",
                        know=["Pay is mentioned, with a date.", "The band is clear.", "Your manager supports it."],
                        do=["Get the date and amount in writing.", "Accept.", "Diary the date."],
                        avoid="The grateful yes before the details.",
                        next="If pay is vague (“next cycle”), you're at Nightmare."),
            nightmare=dict(who="The Paper Crown.",
                           know=["Pay isn't mentioned.", "“Next cycle” is the only promise.", "The new band starts above your salary."],
                           do=["Ask the salary and band before accepting.", "Ask for a dated minimum in writing.", "If needed, accept with a written review date.", "Raise it the day after the review if forgotten."],
                           avoid="The silent seethe.",
                           next="If you've accepted and pay never follows, you're at Hell."),
            hell=dict(who="The Crown of Thorns.",
                      know=["You're below your own band.", "Reviews pass with nothing.", "Your responsibilities keep growing."],
                      do=["Raise it formally with the band as evidence.", "Ask HR how being below band is being addressed.", "Test the market: your new title helps.", "Decide your timeline calmly."],
                      avoid="The title strike: refusing the new work.",
                      next="If nothing changes, your title is now a strong line on your CV."),
        ),
        mirror=dict(
            title="Would you take the crown without the gold?",
            intro="Tick honestly.",
            signs=["You'd accept a promotion before asking about pay.", "You don't know the pay band for your current role.", "You think asking about pay at promotion is ungrateful.",
                   "You've been promised a raise “next cycle” before.", "You're paid below your band and haven't said so."],
            cure="Find out your current band and where you sit. Then write the sentence you'll use at your next promotion: “Thank you. Before I accept, what's the salary?”",
        ),
        rehearsal=dict(
            title="Scene: Friday 5 November, 16:40. Jules, again, if Jules had read this entry.",
            intro="The Question Before Yes, and the Dated Promise.",
            lines=[
                ("", "Subject: RE: Promotion to Principal Analyst"),
                ("Jules", "Thank you, I'm delighted. Before I accept, could you confirm the salary for the Principal role, and the band?"),
                ("HR", "The band is £63k to £72k. Pay will be reviewed in the next cycle."),
                ("Jules", "Thank you. Could we agree in writing that I'll move to at least the band minimum, £63k, by 1 January? Then I'm happy to accept today."),
                ("HR", "…I'll check with Finance."),
                ("", "In this version, Jules gets £63k from January. In the real one, Jules got 3% in April. Same person, same promotion, one email."),
            ],
            note="The only difference between the two endings is the order of two sentences.",
        ),
    ),
    # ------------------------------------------------------------------ the Poisoned Chalice
    "poisoned-chalice": dict(
        sighting=f"""{beat("Monday 1 November 2027 · the cup")}
<p>Pip became acting Head of Customer Insight “while we recruit, just for a couple of months”. Nine people instead of two.
His old job didn't go anywhere. Neither did his salary.</p>
{beat("November to January")}
<p>Pip ran the joint planning review, the Horizon follow-ups and nine 1:1s a week, then did the regulator dashboard on
Thursday nights. His Friday lines were the best they'd ever been. So were the bags under his eyes.</p>
{beat("February · the extension")}
<p>The interviews slipped. “Could you carry on until March?” The allowance was “being looked at” (see the Raise Duel).
Pip noticed he'd been acting for longer than the original “couple of months” with no end date in writing.</p>
{beat("March · the result")}
<p>The permanent role went to someone else (see Passed Over). Pip handed back nine people on a Monday and returned to two.
It was the most valuable five months of his career, and the most exhausting, and nobody had agreed the terms first, except
for one thing: he'd asked, in October, whether acting would count in the process. It did. It just wasn't enough.</p>
{note("Read the label before you drink. If there isn't one, ask for one.")}""",
        origin=dict(
            title="How acting roles became a trial",
            beats=[
                ("2016 · a sensible practice", "When a manager leaves, someone acts up for a few weeks. It's a good development chance, and short."),
                ("2020 · the freeze", "During the hiring freeze, acting roles stretch to months, because recruiting is slow and acting is free."),
                ("2023 · the audition", "Leaders start using long acting periods as unpaid auditions: “let's see how they do before we decide”."),
                ("2027 · Pip", "Pip's “couple of months” becomes five. It's a real opportunity and an unpaid trial at the same time."),
            ],
            turning="A short development step that turned into a free, open-ended audition.",
            saved="Terms agreed on day one: an end date, an allowance, cover, and clarity on the permanent role.",
            note="Acting roles can be gifts. They're poisoned only when nobody writes down the terms.",
        ),
        know=f"""<p>Acting or interim roles can be great: you get experience and evidence for promotion. They become poisoned when they
have no end date, no extra pay, no cover for your old job, and no honest answer about whether you're a real candidate for
the permanent role.</p>
<h3 class="kh">What the organisation wants</h3>
<p>Continuity while it recruits, at no extra cost, and a chance to see you in the job.</p>
<h3 class="kh">Why the poison spreads</h3>
<p>Because recruitment slips, acting is free, and nobody revisits the terms once you've started.</p>
<h3 class="kh">The antidote</h3>
<ul class="fears"><li>An end date.</li><li>An acting allowance.</li><li>Cover for your old job.</li><li>An honest answer on the permanent role.</li></ul>
<h3 class="kh">Three kinds of chalice</h3>
<div class="breeds">
<div><b>The Honest Cup</b><p>Short, paid, clear odds. Drink and learn.</p></div>
<div><b>The Bottomless Cup</b><p>No end date. Ask for one before it's empty.</p></div>
<div><b>The Audition Cup</b><p>An unpaid trial for the real role. Know your odds.</p></div>
</div>
{note("It's still worth drinking sometimes. Just know what's in the cup.")}""",
        difficulty=dict(
            normal=dict(who="The Honest Cup.",
                        know=["There's an end date.", "There's an allowance.", "You know your odds."],
                        do=["Accept and learn.", "Record your results in the Book of Deeds.", "Ask for feedback at the end."],
                        avoid="The half-act.",
                        next="If there's no end date or pay, you're at Nightmare."),
            nightmare=dict(who="The Bottomless Cup.",
                           know=["“Just a couple of months” with no date.", "No allowance.", "You're doing both jobs."],
                           do=["Agree the Chalice Terms now, even mid-way.", "Ask for the allowance backdated.", "Hand over part of your old job.", "Ask the Honest Odds question."],
                           avoid="The presumption: acting as if the job is yours.",
                           next="If it's an unpaid audition and you're not a real candidate, you're at Hell."),
            hell=dict(who="The Audition Cup, with poor odds.",
                      know=["Leadership wants an outsider.", "You're holding the seat.", "Your health is suffering."],
                      do=["Ask directly about your odds.", "Set an end date yourself.", "Harvest the evidence for your next role.", "Protect your health."],
                      avoid="The bottomless cup: carrying on indefinitely because nobody stopped you.",
                      next="When it ends, read Passed Over before you decide anything."),
        ),
        mirror=dict(
            title="Is your cup labelled?",
            intro="If you're acting in a role, tick honestly.",
            signs=["Your acting role has no end date in writing.", "You're not paid extra for it.", "You're still doing all of your old job.",
                   "You don't know if you're a real candidate for the permanent role.", "It was meant to be “a couple of months” and it's been longer."],
            cure="Send one email this week asking for the four terms: end date, allowance, cover, and how the permanent role will be decided.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 28 October, Pip's 1:1 with Priya, before saying yes.",
            intro="The Chalice Terms and the Honest Odds.",
            lines=[
                ("Pip", "I'd love to act up. Can we agree four things? An end date, say 31 March. An acting allowance. Asha covering the analysis. And will acting count in the permanent process?"),
                ("Priya", "End date, yes. Asha, yes. Acting counts, yes. The allowance I'll have to fight for."),
                ("Pip", "And honestly: am I a realistic candidate, or holding the seat?"),
                ("Priya", "Realistic. But Ottoline wants to look outside too. I won't pretend otherwise."),
                ("Pip", "Thank you for being straight. I'll take it."),
            ],
            note="Pip got three of four terms and an honest answer. The fourth (the allowance) he won later in the Raise Duel.",
        ),
    ),
    # ------------------------------------------------------------------ Passed Over
    "passed-over": dict(
        sighting=f"""{beat("Monday 6 March 2028 · 08:30 · the email")}
<p>“We're delighted to announce that Ruth Calloway, currently Head of Insight at Northgate Energy, will join us as Head of
Customer Insight on Monday.” Pip read it twice, then a third time in case the name changed.</p>
{beat("08:31")}
<p>Pip's phone buzzed: Priya, asking for a call at nine. Dorian, a message: “Gutted for both of us. Coffee? Not that kind.”</p>
{beat("Monday 13 March · 09:00 · the welcome")}
<p>There were balloons by the lift on floor 9. Pip stood on the other side of the glass wall for a moment, in the rain-grey
light, watching people welcome Ruth. Then he walked in, held out his hand, and said, “Welcome. Let me know how I can help in
your first month.” His voice did not shake. Afterwards he went to the bathroom on floor 9, and did not stare at the hand dryer.</p>
{beat("That evening")}
<p>Pip drew a small bird rising in the corner of his notebook. He didn't know what it meant yet. The Annotator, when he told
her, said it was a phoenix, and that phoenixes need a fire first.</p>
{note("Being passed over is a moment. How you behave the day after is a reputation.")}""",
        origin=dict(
            title="How MetroVolt came to look outside",
            beats=[
                ("2019 · the CEO's view", "Dame Helena believes MetroVolt is too inward-looking: the same people, the same ideas. She asks for every senior role to consider external candidates."),
                ("2021 to 2026 · the outsiders", "Several senior roles go to outsiders. Some succeed; some leave in a year. Internal candidates learn that “strong field” often means “someone from Northgate”."),
                ("2027 · Ruth", "Ottoline has followed Ruth Calloway's work at Northgate for two years. When Head of Customer Insight appears, the prophecy includes an outsider before the advert."),
                ("March 2028 · the decision", "The panel picks Ruth: ten years leading insight teams, against Pip's five months acting. It's defensible. It still hurts."),
            ],
            turning="A sensible push for fresh ideas that sometimes meant internal candidates were measured against people they never had a chance to become.",
            saved="Nothing unfair happened. What matters is what Pip does next.",
            note="Sometimes you're passed over because someone better applied. That's the hardest and the most useful kind: it tells you exactly what to learn.",
        ),
        know=f"""<p>Being passed over hurts, especially if you acted in the role. The reasons are often reasonable (experience, an
external strategy, a stronger candidate), but it still feels personal. What happens next depends mostly on you: how you
behave publicly, what you learn, and whether your next step is here or elsewhere.</p>
<h3 class="kh">What the organisation watches</h3>
<p>Whether you're gracious. People who handle disappointment well are remembered for the next role.</p>
<h3 class="kh">Why it hurts more than it should</h3>
<p>Because you invested hope and evidence. Because colleagues know. Because, often, you were close.</p>
<h3 class="kh">What helps you rise</h3>
<ul class="fears"><li>A dignified first day.</li><li>Specific feedback, a week later.</li><li>A plan with dates.</li><li>Deciding calmly whether to stay.</li></ul>
<h3 class="kh">Three kinds of “no”</h3>
<div class="breeds">
<div><b>The Not Yet</b><p>Close, missing one thing. Learn it; you're next.</p></div>
<div><b>The Not Here</b><p>The organisation wanted something else. Consider other doors.</p></div>
<div><b>The Not This</b><p>The role wasn't right for you anyway. See the Peter Principle.</p></div>
</div>
{note("The phoenix needs a fire first. Make sure the fire teaches you something.")}""",
        difficulty=dict(
            normal=dict(who="The Not Yet: close, missing one thing.",
                        know=["Feedback is specific.", "Your sponsor still backs you.", "There's a clear gap."],
                        do=["Congratulate the winner.", "Ask for specific feedback.", "Close the gap with a dated plan."],
                        avoid="The public sulk.",
                        next="If the feedback is vague and the reasons unclear, you're at Nightmare."),
            nightmare=dict(who="The Not Here: an outsider won, or reasons are vague.",
                           know=["The winner came from outside.", "Feedback is “strong field”.", "You acted in the role."],
                           do=["Ask a precise question: what would have made the difference?", "Help the winner succeed; it's noticed.", "Talk to your sponsor about your next step.", "Give it a month before deciding anything."],
                           avoid="The rage application.",
                           next="If you're passed over repeatedly, you're at Hell."),
            hell=dict(who="Passed over again and again.",
                      know=["This is the second or third time.", "The feedback changes each time.", "Others with less evidence move up."],
                      do=["Ask, in writing, what specifically you need.", "If it might be unfair or discriminatory, raise it formally.", "Test the market: your evidence is valuable elsewhere.", "Use the Escape Portal (Act III) calmly."],
                      avoid="The sabotage welcome.",
                      next="Sometimes the resurrection happens somewhere else. That's still a resurrection."),
        ),
        mirror=dict(
            title="How would you take the fall?",
            intro="Tick honestly.",
            signs=["You'd be visibly upset in front of colleagues.", "You'd avoid the person who got the job.", "You'd apply elsewhere the same week.",
                   "You wouldn't ask for feedback because it would hurt.", "You'd quietly stop trying."],
            cure="Write your congratulations sentence now, for a role you want. If the day comes, you'll be glad it was already written.",
        ),
        rehearsal=dict(
            title="Scene: Monday 20 March, Pip's first 1:1 with Ruth.",
            intro="The Feedback Ask and the Rising Plan, with the person who got the job.",
            lines=[
                ("Ruth", "I know you wanted this role. I'd understand if this is awkward."),
                ("Pip", "It's a bit awkward. I'm also glad you're here; your Northgate model is brilliant. What do you think I'd need to be ready for a role like yours?"),
                ("Ruth", "Honestly? You're a better analyst than I am. You haven't yet led people through a bad year. And I'm not sure you want to."),
                ("Pip", "…What makes you say that?"),
                ("Ruth", "Your best Friday lines are all about models. None of them are about 1:1s."),
                ("", "Pip goes home and reads his Book of Deeds from the start. Ruth is right. Next entry: the Peter Principle."),
            ],
            note="The most useful feedback Pip ever got came from the person who beat him. It only happened because he welcomed her.",
        ),
    ),
    # ------------------------------------------------------------------ the Sponsor's Mark
    "sponsors-mark": dict(
        sighting=f"""{beat("2027 · three mentors")}
<p>Pip had mentors: the Chronicler, the Annotator, Jules. They gave him excellent advice. None of them was in the rooms
where decisions about him were made.</p>
{beat("Tuesday 14 December · calibration")}
<p>In room 27A, Priya read four lines from Pip's Book of Deeds and said, “He should be considered for the Head role. I've
seen him run the planning review. I'll vouch for him.” Pip was at his desk, three floors down, building a model.</p>
{beat("February · the shortlist")}
<p>When the panel shortlisted for Head of Customer Insight, Ottoline asked who would vouch for the internal candidates.
Priya spoke for Pip. Nobody spoke for Dorian. Dorian had several mentors.</p>
{beat("May · the new track")}
<p>When Pip proposed a Principal Analyst track (see the Peter Principle), it was Priya who took it to Ottoline, and Ottoline
who took it to Dame Helena. Pip never met Dame Helena. His idea did.</p>
{note("Find someone who'll say your name when you're not there. Then deserve it.")}""",
        origin=dict(
            title="How Priya became a sponsor",
            beats=[
                ("2014 · Priya's first big role", "Priya, then a team lead, is promoted to manager because a director she'd never met said her name in a talent review. She finds out a year later."),
                ("2014 · the debt", "She asks the director why. “You fixed my call-centre numbers in 2013. I remember people who make my life easier.”"),
                ("2015 to 2026 · paying it forward", "Priya decides to do the same: watch for people who deliver, then spend her reputation on them, in rooms they're not in."),
                ("2027 · Pip", "Pip gave her the Horizon submission that kept her team intact and a page that made calibration easy. She remembers people who make her life easier."),
            ],
            turning="Being sponsored once by a stranger, and deciding to become that stranger for others.",
            saved="Nothing needed saving. Sponsorship is a chain; Priya just kept it going.",
            note="Most sponsors were sponsored once. Ask yours who did it for them. It's a lovely conversation.",
        ),
        know=f"""<p>Mentors advise you. Sponsors <b>act</b> for you: they spend their reputation to put your name forward for
opportunities, often in rooms you'll never enter. Many talented people have mentors and no sponsor, and wonder why they
don't move.</p>
<h3 class="kh">What sponsors want</h3>
<p>People who make them look good: reliable, visible results, and no embarrassments after they've vouched.</p>
<h3 class="kh">Why sponsorship matters</h3>
<p>Because the decisive moments (calibration, shortlists, talent reviews) happen without you. Someone has to be there for you.</p>
<h3 class="kh">How to earn one</h3>
<ul class="fears"><li>Deliver something important for them.</li><li>Be reliable and visible.</li><li>Ask, specifically.</li><li>Give them sentences to say.</li></ul>
<h3 class="kh">Three kinds of supporter</h3>
<div class="breeds">
<div><b>The Mentor</b><p>Gives advice. Valuable. Not enough.</p></div>
<div><b>The Advocate</b><p>Speaks well of you when asked. Helpful.</p></div>
<div><b>The Sponsor</b><p>Puts your name forward unasked, and stakes their reputation. Rare.</p></div>
</div>
{note("Mentors give you a map. Sponsors open a door. You need both, but only one gets you through.")}""",
        difficulty=dict(
            normal=dict(who="You have a natural sponsor in your manager.",
                        know=["Your manager speaks up for you.", "They know your work.", "They're respected."],
                        do=["Give them ammunition (three sentences).", "Tell them what you want next.", "Never surprise them."],
                        avoid="The silent hope.",
                        next="If nobody senior would vouch for you, you're at Nightmare."),
            nightmare=dict(who="Mentors, but no sponsor.",
                           know=["You get good advice, but no doors open.", "Your manager is weak or absent.", "Senior people don't know your name."],
                           do=["Deliver something important for a senior person.", "Then ask them, specifically, for one opportunity.", "Give them the Ammunition.", "Keep your mentors too."],
                           avoid="The collector: asking everyone.",
                           next="If no senior person will engage with you at all, you're at Hell."),
            hell=dict(who="No access to anyone senior.",
                      know=["Your manager blocks contact upwards.", "Opportunities are decided in a closed circle.", "Nobody senior knows you exist."],
                      do=["Find cross-team projects with senior visibility.", "Build a skip-level relationship openly (Act III).", "Look for sponsors outside your line.", "Consider where you'd be seen."],
                      avoid="The embarrassed sponsor: overpromising to someone who vouches for you.",
                      next="If you can't be seen here, go where you can."),
        ),
        mirror=dict(
            title="Who says your name?",
            intro="Tick honestly.",
            signs=["You couldn't name one senior person who'd put you forward unasked.", "You've never asked anyone to sponsor you.", "You think mentors and sponsors are the same thing.",
                   "Your name never comes up in rooms you're not in.", "You've never sponsored anyone yourself."],
            cure="Name one senior person whose work you could make easier this quarter. Do it. Then, in a few months, ask them for one thing.",
        ),
        rehearsal=dict(
            title="Scene: Monday 6 December, Pip asks Priya directly.",
            intro="The Ask, and the Ammunition.",
            lines=[
                ("Pip", "Priya, I'd like to be considered for the Head role. Would you be willing to speak for me if my name comes up in calibration?"),
                ("Priya", "I was going to anyway. But I'm glad you asked; it tells me you want it."),
                ("Pip", "If it helps, here are three sentences: the complaint model, the Horizon submission, and onboarding four people."),
                ("Priya", "Perfect. And Pip? One day you'll do this for someone else. Ask me who did it for me, some time."),
            ],
            note="Priya would have spoken for Pip anyway. The ask still mattered: it told her what he wanted, and gave her the words.",
        ),
    ),
    # ------------------------------------------------------------------ Your First Minions
    "first-minions": dict(
        sighting=f"""{beat("Thursday 1 April 2027 · first day as a manager")}
<p>Pip became analytics lead in Customer Ops: his first team, Asha and Tomasz. He bought a management book. On his first
morning he held it, briefly, upside down. Nobody noticed except the Annotator, who later wrote this entry.</p>
{beat("April · the midnight redo")}
<p>Tomasz's weekly report wasn't how Pip would have done it. Pip redid it at midnight. Then he redid Asha's dashboard. By
the end of April he was working more hours than ever and his team had learned nothing, except that Pip would redo things.</p>
{beat("May · the avoided conversation")}
<p>Tomasz's summaries kept burying the main finding. Pip didn't say anything, because Tomasz had eight years at MetroVolt
and Pip had eight weeks as a manager. The summaries kept burying the finding.</p>
{beat("June · the turn")}
<p>Priya, in a 1:1, asked how many hours he was working. Pip said 55. She asked how many hours Asha and Tomasz were
learning from him. Pip didn't have an answer. That was the day he stopped redoing things.</p>
{note("You were promoted for being good at the work. Now your work is making them good at it.")}""",
        origin=dict(
            title="How MetroVolt makes first-time managers",
            beats=[
                ("Always · the promotion", "At MetroVolt, as almost everywhere, the best analyst gets promoted to manage the analysts. Skill at the work is the main qualification for leading it."),
                ("Always · the training", "There's a two-day course, usually six months after you start. By then the habits are formed."),
                ("Always · the reflex", "New managers do what made them successful: the work itself. They redo, check and hover. Some become All-Seeing Eyes (Act III)."),
                ("2027 · Pip", "Pip, a brilliant analyst, becomes a manager on a Thursday, with a book and no training. He does exactly what everyone does. Then he learns."),
            ],
            turning="Promoting people for doing the work, into a job that's mostly not doing it, with no training until it's too late.",
            saved="Training before the first day. Or a manager who asks, in week two, “how much are they learning from you?”",
            note="Every bad habit in Act III starts here, in someone's first month as a manager. This is where you stop it.",
        ),
        know=f"""<p>First-time managers are usually promoted for being good at the work, and then struggle because the new job is
different: enabling others, giving feedback, protecting the team. The commonest traps are doing the work yourself, avoiding
feedback, and wanting to be liked more than wanting people to grow.</p>
<h3 class="kh">What your team wants</h3>
<p>Clear goals, honest feedback, protection from chaos above, and room to do the work their way.</p>
<h3 class="kh">Why new managers struggle</h3>
<p>Because the habits that made them great individuals (doing, checking, perfecting) make them poor managers if they don't change.</p>
<h3 class="kh">What makes a good first year</h3>
<ul class="fears"><li>Delegating outcomes, not tasks.</li><li>Specific feedback, early.</li><li>Real 1:1s.</li><li>Shielding the team.</li></ul>
<h3 class="kh">Three kinds of new manager</h3>
<div class="breeds">
<div><b>The Doer</b><p>Keeps doing the work. Needs to let go.</p></div>
<div><b>The Friend</b><p>Avoids hard conversations. Needs to give feedback.</p></div>
<div><b>The Checker</b><p>Hovers and checks. Needs to trust. (Don't be Victor.)</p></div>
</div>
{note("If you're working more hours than before you were promoted, you're probably still doing your old job.")}""",
        difficulty=dict(
            normal=dict(who="A new manager with a good team.",
                        know=["Your team is capable.", "You're tempted to do things yourself.", "Your manager supports you."],
                        do=["Delegate whole outcomes.", "Start weekly 1:1s about them.", "Give one piece of specific feedback a week."],
                        avoid="The shadow doer.",
                        next="If you're avoiding hard feedback, you're at Nightmare."),
            nightmare=dict(who="Managing people more experienced than you.",
                           know=["They've been here longer.", "Feedback feels awkward.", "Problems are going unsaid."],
                           do=["Give feedback on outcomes, respectfully and specifically.", "Ask for their advice; it's not weakness.", "Set clear expectations together.", "Protect them from noise above."],
                           avoid="The best friend: avoiding hard conversations.",
                           next="If you're burning out and the team isn't growing, you're at Hell."),
            hell=dict(who="Drowning: doing two jobs, the team stuck.",
                      know=["You work far more hours than before.", "Your team waits for you to decide everything.", "Nobody's growing."],
                      do=["Stop doing the work. Hand it over, with support.", "Ask your manager for coaching or training.", "Agree what good looks like with each person.", "Read Act III to see what not to become."],
                      avoid="The mini-eye: checking everything.",
                      next="If you hate managing, read the Peter Principle. It might not be for you, and that's fine."),
        ),
        mirror=dict(
            title="Are you still doing your old job?",
            intro="If you manage anyone, tick honestly.",
            signs=["You've redone someone's work this month.", "You work more hours than before you were promoted.", "You've avoided giving feedback to someone more experienced.",
                   "Your team waits for you before deciding things.", "Your 1:1s are mostly status updates."],
            cure="Pick one thing you do that someone in your team could own. Hand it over this week, with what good looks like. Then don't touch it.",
        ),
        rehearsal=dict(
            title="Scene: Monday 7 June 2027, Pip and Asha.",
            intro="The Letting Go and the Clear Word.",
            lines=[
                ("Pip", "Asha, from today the regulator dashboard is yours. Here's what good looks like: on time, checked, and the main change on the first line. I won't check it daily."),
                ("Asha", "You redid my last one."),
                ("Pip", "I did, and I shouldn't have. It was fine. If something's wrong, I'll tell you, and you'll fix it."),
                ("Asha", "…OK. What would you have changed?"),
                ("Pip", "The summary buried the main finding. Lead with it. That's the only thing."),
                ("", "Asha owns the dashboard for the next year. It's never late. In December it's in her objectives, and in calibration."),
            ],
            note="Handing it over cost Pip a small, perfectionist pang. It gave Asha a year of growth and him forty evenings back.",
        ),
    ),
    # ------------------------------------------------------------------ the Peter Principle Curse
    "peter-principle": dict(
        sighting=f"""{beat("Monday 20 March 2028 · Ruth's question")}
<p>In their first 1:1, Ruth had said Pip's best Friday lines were all about models, none about 1:1s (see Passed Over). That
evening, Pip read his Book of Deeds from the start, and saw she was right.</p>
{beat("The Honest Inventory")}
<p>Pip wrote two lists. Days he loved: building the complaint model, finding the waste in Horizon, the cold-snap forecast.
Days he dreaded: the five months of nine 1:1s a week, the budget templates, the calibration room. He had wanted the Head
role because it was <i>up</i>. He had never asked whether it was <i>towards</i> anything.</p>
{beat("Tuesday 4 April · Lionel's workshop")}
<p>Pip asked Lionel, of all people, for advice. Lionel told him he'd been Head of Engineering in 2019, hated every minute,
and stepped back to principal engineer in 2021. “Best decision I ever made,” Lionel said. “I'm paid the same. I'm happy.
And people finally listen to me again.”</p>
{beat("Monday 8 May · the proposal")}
<p>Pip proposed a Principal Analyst track with its own pay band, no line management, and a seat in planning decisions. Ruth
backed it. Priya took it to Ottoline. In June, Pip became MetroVolt's first Principal Analyst in Customer Insight, with the
pay of a head and the job of a builder. He was, for the first time in a year, excited on Sunday evenings.</p>
{note("Climb towards the work you love, not just upwards. Ladders also go sideways.")}""",
        origin=dict(
            title="How Lionel climbed down",
            beats=[
                ("2011 · the transformer winter", "Lionel is proven right about the transformers (see Act II, the Know-It-All Basilisk). He's promoted quickly."),
                ("2019 · the top of the ladder", "Lionel becomes Head of Engineering: 60 people, budgets, HR cases. He stops doing engineering. He's bad at the new job and knows it. He becomes defensive."),
                ("2021 · the step down", "After two miserable years, Lionel asks to step back to principal engineer. MetroVolt has no such role at his pay. He takes a pay cut to do it."),
                ("2024 · the band", "MetroVolt creates a principal engineer band because of Lionel. He gets his pay back. He's the most respected engineer in the company, and somewhat less of a basilisk."),
            ],
            turning="A ladder with only one direction, and a brilliant engineer who climbed it to a job he hated.",
            saved="An expert track from the start, so being promoted didn't have to mean becoming a manager.",
            note="The Peter Principle says people rise to their level of incompetence. The cure is having more than one direction to rise in.",
        ),
        know=f"""<p>The Peter Principle: in hierarchies, people get promoted for doing their current job well until they reach a job
they don't do well, and stay there. The commonest version is the brilliant specialist promoted into management. The cure is
knowing what you love, and organisations offering more than one ladder.</p>
<h3 class="kh">What drives the curse</h3>
<p>Pay and status tied to managing people. If the only way up is to manage, specialists who want to grow have to stop specialising.</p>
<h3 class="kh">Why people climb anyway</h3>
<p>Because up looks like success, stepping back looks like failure, and nobody asks “do you actually want this?”</p>
<h3 class="kh">What breaks it</h3>
<ul class="fears"><li>An honest inventory of what you love.</li><li>An expert track with real pay.</li><li>Leaders who respect sideways moves.</li><li>Examples like Lionel's.</li></ul>
<h3 class="kh">Three kinds of climber</h3>
<div class="breeds">
<div><b>The Natural Leader</b><p>Loves the people work. Up is right.</p></div>
<div><b>The Reluctant Manager</b><p>Climbing because it's the only way up. Look for the other ladder.</p></div>
<div><b>The Stranded</b><p>Already in the wrong role, unhappy. Step sideways, without shame.</p></div>
</div>
{note("Ask yourself: if this paid exactly the same as my current job, would I still want it?")}""",
        difficulty=dict(
            normal=dict(who="The Natural Leader: you might genuinely want to manage.",
                        know=["You enjoy the people side.", "Your best days involve others' success.", "The work you'd lose doesn't feel like loss."],
                        do=["Go for it, with training.", "Read Your First Minions.", "Check in with yourself after six months."],
                        avoid="The status trap: choosing for title alone.",
                        next="If you'd only take it because it's up, you're at Nightmare."),
            nightmare=dict(who="The Reluctant Manager.",
                           know=["Your best days are the old work.", "You dread the management parts.", "The only pay rise is through managing."],
                           do=["Do the Honest Inventory.", "Ask whether an expert track exists.", "If not, propose one with examples.", "Talk to someone who stepped back (find your Lionel)."],
                           avoid="The ladder reflex.",
                           next="If you're already in a role you hate, you're at Hell."),
            hell=dict(who="The Stranded: already in the wrong role.",
                      know=["You're unhappy and not good at it.", "Your team can tell.", "Stepping back feels like failure."],
                      do=["Talk to your manager honestly.", "Plan a sideways or backwards step with dignity.", "Negotiate pay protection if you can.", "Remember Lionel: respected, happy, listened to."],
                      avoid="The miserable climb: staying because leaving the role feels like failing.",
                      next="If your organisation won't allow it, find one with more than one ladder."),
        ),
        mirror=dict(
            title="Which way are you climbing?",
            intro="Tick honestly.",
            signs=["You want the next promotion mainly because it's the next one.", "Your favourite days are doing work, not managing it.", "You'd take a role you'd dread for the title.",
                   "You think stepping back would be failure.", "You've never asked what the expert track looks like."],
            cure="Write two lists: days you loved, days you dreaded, this year. Look at them for a week. Then decide which direction is forwards.",
        ),
        rehearsal=dict(
            title="Scene: Monday 8 May 2028, Pip, Ruth and Priya.",
            intro="The Other Ladder, proposed.",
            lines=[
                ("Pip", "I've realised I don't want to manage nine people. I want to build things that nine people use. I'd like to propose a Principal Analyst track: no line management, a pay band equivalent to a head, a seat in planning decisions."),
                ("Ruth", "Northgate had one. It kept our best analysts."),
                ("Priya", "Engineering has one, because of Lionel. Why not insight?"),
                ("Pip", "I've written a page, with three examples from other utilities."),
                ("Priya", "Send it. I'll take it to Ottoline this week."),
                ("", "June: Pip becomes Principal Analyst, Customer Insight. On his first Friday, his line in the Book of Deeds is just: “Happy.”"),
            ],
            note="Pip's resurrection wasn't up. It was sideways, towards the work he loved, at the pay he deserved. That's the Ascension done right.",
        ),
    ),
}
