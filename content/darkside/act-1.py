# Series 4 · The Darkside of the Corporation · Act I: The Court of Whispers (office politics).
# Rendered by scripts/grimoire.py. `note(text)` (the Annotator's margin note) is injected by the loader.
# Text is raw HTML. Stats follow grimoire.STATS: sanity, career XP, mana, armor, stealth, allies, soul, time, backfire safety.
# Plates (content/darkside/art/<slug>.svg) exist for three entries only: hidden-thrones, ring-kissing-ritual, sacrificial-lamb.

ACT = dict(
    no=1,
    title="The Court of Whispers",
    sub="Where power really lives, and how to walk its halls without being eaten",
    contents_title="The rites, the rulers and the traps",
    summary="Act I of The Darkside of the Corporation: office politics as a court of whispers. Hidden thrones, the meeting before the meeting, ring-kissing, favouritism, the sacrificial lamb and more, with counter-spells that work.",
    intro=f"""<p class="lead">You were told that MetroVolt is run by an org chart. It is not. The org chart is a map of
where the chairs are. Power lives somewhere else: in who gets a meeting on short notice, whose email gets a reply in
four minutes, and who was in the corridor when the decision was made.</p>
<p>Many good people refuse to “play politics”. That is like refusing to “play weather”. It rains on you anyway.
Politics is simply how decisions get made when there are more people than chairs. You can take part in it
<b>cleanly</b>: by understanding it, building real relationships and being useful. That is all this Act asks.</p>
{note("Clean politics: help people get what they need, in the open, and keep your promises. Dirty politics: everything in the Forbidden Spells sections. One builds a career. The other builds a story people tell about you after you leave.")}
<p>This is the Act where <b>Pip</b> learns that being right is the beginning of the work, not the end of it.
It is autumn at MetroVolt. Budget season. A reorg is rumoured. The corridors on 27 are very quiet, which is how
you know something is happening.</p>""",
    cast=[
        ("Pip", "he/him", "junior analyst, Grid Planning. Right about many things. Influential about none of them. Yet."),
        ("The Chronicler", "they/them", "nineteen years at MetroVolt. Has watched four CEOs arrive and three leave."),
        ("The Annotator", "she/her", "ex-MetroVolt, now freelance. Writes in the margins."),
        ("Marcus Bell", "he/him", "Pip's manager, Head of Grid Planning. Decent, tired, overloaded."),
        ("Lord Varnish", "he/him", "VP of Strategic Synergy. Large box on the org chart. Smaller than it looks."),
        ("Ottoline Grey", "she/her", "Chief of Staff to the CEO. A small box on the chart. Every road runs through her office."),
        ("Dame Helena Strand", "she/her", "the CEO. Seen mostly in all-hands videos and in the fear of others."),
        ("Priya Nair", "she/her", "Head of Customer Operations. Rival tower. Not, it turns out, an enemy."),
        ("Gareth Pound", "he/him", "Director of Network Assets. Collects headcount the way dragons collect gold."),
        ("Tamsin", "she/her", "executive assistant on floor 27. Knows everything. Says almost nothing."),
        ("Jules", "they/them", "Pip's peer. Lord Varnish's favourite. Mostly deserves it, which makes it worse."),
        ("Dorian", "he/him", "Strategy. You met him in Act II. He remembers you too."),
    ],
    entries=[
        # ------------------------------------------------------------------ 1
        dict(
            slug="hidden-thrones", flagship=True,
            plate_caption="Floor 27, after hours. The org chart says Lord Varnish. The red string says Ottoline. The red string is right.",
            ring="WHO REALLY DECIDES ✠ ASK OTTOLINE ✠ RUN IT PAST 27 ✠", scrawl="follow the red string",
            name="The Map of Hidden Thrones", sigil="♛",
            epithet="The org chart shows the chairs. Not who sits on them.",
            threat=4, habitat="floor 27, the CEO's calendar, the space between two boxes on the chart",
            weakness="curiosity: asking how decisions actually got made",
            summary="The Map of Hidden Thrones: the difference between the org chart and the real power map, how to draw your own, and how to use it without becoming a schemer.",
            sighting=f"""<p>In September Pip wrote a two-page proposal: move the Lumen smart-meter rollout to the districts with
the worst outage history first. It was obviously right. He sent it, as the org chart said he should, up the line to
Lord Varnish, whose box was the biggest on the page.</p>
<p>Nothing happened for five weeks. Then, on a Tuesday, the plan was approved, almost word for word, as
<i>“Ottoline's sequencing idea”</i>. Pip had never heard of Ottoline. He looked her up. Chief of Staff. A small box,
off to the side, with a dotted line. He had sent his idea to the biggest box and it had walked, by itself, to the
smallest one, because that was where decisions lived.</p>""",
            know=f"""<p>Every organisation has two maps. The <b>formal map</b> (the org chart) shows reporting lines. The
<b>real map</b> shows influence: who the decision makers listen to, who controls the calendar, who has been right
before, who can say no quietly. The two overlap, but less than you'd think.</p>
<p>Hidden thrones are usually not sinister. Chiefs of staff, long-serving engineers, the finance partner who
builds the budget model, the assistant who decides which emails reach the CEO: they hold power because they hold
<b>information, access or trust</b>. Learn who they are, treat them well, and the building starts to make sense.</p>
{note("Power = information + access + trust. Titles are just where the building keeps the furniture.")}""",
            omens=[
                "Decisions arrive from somewhere you can't see on the chart.",
                "A senior person always says “let me run it past someone” and you never learn who.",
                "A junior-looking person is in every important meeting.",
                "Your proposal comes back approved under someone else's name.",
                "People are noticeably nicer to one assistant than to their own boss.",
            ],
            counters=[
                ("The Cartographer's Question", "After any decision, ask how it was made. People love explaining how things work, and you learn the map.",
                 "“That decision landed really quickly. Out of curiosity, who shaped it? I'm trying to learn how things work up there.”"),
                ("The Hand-Drawn Map", "Draw the real map for your area: decision makers, the people they listen to, and the gatekeepers. Update it monthly. Keep it to yourself.",
                 None),
                ("The Courteous Approach", "Introduce yourself to the hidden throne with something useful, not a request. Gatekeepers remember who brought them value.",
                 "“Hi Ottoline, I built the outage data behind the Lumen sequencing. If it's ever useful for the CEO's briefings, I'm happy to keep it updated.”"),
                ("The Double Route", "Send important ideas up the formal line <i>and</i> make sure the real decision makers hear about them, openly, with your manager's knowledge.",
                 "“Marcus, I'd like to walk Ottoline through the proposal too, since she's shaping Lumen. OK with you if I copy you in?”"),
            ],
            forbidden=[
                ("The Secret Back Door", 4, "Going round your manager to the throne without telling them. It works once. Then your manager learns of it from the throne, which is worse than any rejection."),
                ("The Throne-Hunter", 3, "Befriending gatekeepers only for access. They can smell it. Their whole job is smelling it."),
                ("The Cynic's Map", 3, "Deciding that because power is informal, merit doesn't matter. Merit is the entry ticket. The map is how you use it."),
            ],
            difficulty=dict(
                normal="A healthy organisation with a few informal influencers. Learn who they are and keep them informed.",
                nightmare="Real power is far from the chart and nobody admits it. Your hand-drawn map is essential; ask “who else should see this?” every time.",
                hell="A court where proximity beats competence and favour can be withdrawn overnight. Protect your record, build relationships across several thrones, and keep your exit options warm.",
            ),
            stats=[4, 5, 4, 3, 4, 4, 5, 3, 4], stats_for="The Hand-Drawn Map",
            loot=("The Real Map",
                  "A private page. Fill it in for the decisions that affect your work. Review monthly.",
                  """DECISION AREA: Lumen rollout order

DECIDES (formally)   Lord Varnish, VP Strategic Synergy
DECIDES (actually)   Ottoline Grey, Chief of Staff (shapes the CEO's view)
LISTENED TO BY THEM  Priya Nair (customer complaints data)
                     Marcus Bell (only if asked)
GATEKEEPER           Tamsin, EA floor 27 (controls the calendar)
WHAT THEY CARE ABOUT Ottoline: no surprises for the CEO. Varnish: credit.
MY LAST CONTACT      Ottoline: never. -> fix this month"""),
            trial=[
                ("Your proposal has sat with a VP for five weeks. What do you do?",
                 "Ask your manager who else shapes this decision, and offer to brief them openly. Don't send it round the VP in secret."),
                ("You discover the CEO's chief of staff makes most rollout decisions. First move?",
                 "Bring her something useful (data, a clear summary), not a request. Introduce yourself with value."),
                ("Is drawing a power map manipulative?",
                 "No. Understanding how decisions are made is part of the job. It becomes manipulative only when you use it to deceive."),
            ],
            last_word="Don't ask who's in charge. Ask who they call before they decide.",
        ),
        # ------------------------------------------------------------------ 2
        dict(
            slug="meeting-before-the-meeting",
            ring="PRE-WIRED ✠ NO SURPRISES ✠ WALK ME THROUGH IT FIRST ✠", scrawl="the meeting is a formality",
            name="The Meeting Before the Meeting", sigil="⚿",
            epithet="By the time the meeting starts, the decision has already been made.",
            threat=3, habitat="corridors, coffee queues, 15-minute 1:1s the day before",
            weakness="nothing. This one is a tool. Learn it.",
            summary="The Meeting Before the Meeting: why big decisions are made before the formal meeting, and how to pre-wire your proposals honestly.",
            sighting=f"""<p>On the 14th of October Pip presented his capacity plan at the Network Investment Board. Seven
directors, forty minutes, eighteen slides. He had rehearsed. He was ready.</p>
<p>Gareth Pound asked on slide 3 why nobody had consulted Network Assets. Priya Nair asked on slide 5 how it affected
call centre volumes. Lord Varnish said “interesting” in the voice people use for a dead bird. The board asked Pip to
“take it away and come back with more alignment”. On the way out, Priya said kindly: “Next time, show me first.
I'd have said yes.”</p>""",
            know=f"""<p>Formal meetings are bad places to make decisions. People feel exposed. Nobody wants to agree to
something in public that they haven't thought through, or that surprises their boss. So the sensible ones decide
<b>before</b>, in private, and the meeting confirms it.</p>
<p>This is called <b>pre-wiring</b>, and it is not sneaky if you do it openly. You walk each key person through
the idea, hear their concerns, adjust, and arrive with no surprises. The meeting becomes ten minutes and a nod.</p>
{note("The rule is: no one should hear an important idea for the first time in a meeting. Especially not the person who can kill it.")}""",
            omens=[
                "Meetings where nothing new is ever decided.",
                "Directors who arrive already knowing the answer.",
                "Your proposals get “take it away and align”.",
                "Someone says “I wish I'd seen this earlier”.",
            ],
            counters=[
                ("The Walkabout", "List everyone who can say yes, no or “not yet”. See each one, briefly, before the meeting. Ask, don't sell.",
                 "“I'm bringing a capacity plan to the board on the 14th. Could I show you in ten minutes first? I want to know what would worry you.”"),
                ("The Concern Harvest", "Write down each concern and change the proposal where it's fair. Then credit them in the meeting.",
                 "“Priya raised call-centre volumes, so slide 5 now shows the impact by week.”"),
                ("The Quiet Count", "Before the meeting, know who supports, who's neutral and who objects. If an objector holds a veto, don't go yet.",
                 None),
            ],
            forbidden=[
                ("The Ambush", 3, "Surprising a powerful person with your idea in public, hoping momentum will carry it. It won't. You've made them look uninformed, and they'll remember."),
                ("The Secret Alliance", 3, "Pre-wiring everyone except your opponent, to outvote them. They'll know, and they'll fight everything you bring from now on."),
                ("The Promise Sprinkle", 4, "Telling each person what they want to hear. In the meeting they compare notes."),
            ],
            difficulty=dict(
                normal="A few stakeholders. Two coffees and a short email fix it.",
                nightmare="Many stakeholders with conflicting needs. Use the Concern Harvest and bring options, not one answer.",
                hell="A board where one person's mood decides. Pre-wire that person's trusted advisors too, and be ready to wait for a better day.",
            ),
            stats=[4, 5, 3, 4, 4, 5, 5, 2, 5], stats_for="The Walkabout",
            loot=("The Pre-Wire Tracker",
                  "One row per person who can block you. Fill it in before every important meeting.",
                  """PERSON          STANCE       CONCERN                     CHANGED?
Priya Nair      neutral -> + call-centre volume         added slide 5
Gareth Pound    against      Network Assets not asked    joint review, Thu
Lord Varnish    ?            credit                      named sponsor
Ottoline Grey   +            no surprises for the CEO    1-page summary sent
VERDICT: go on the 14th? -> NO, wait for Gareth (veto)"""),
            trial=[
                ("Your proposal goes to the board in a week. Three directors haven't seen it. What now?",
                 "The Walkabout: ten minutes with each, this week, asking what would worry them."),
                ("One director hates the idea and has a veto. Should you present anyway?",
                 "Usually not. Hear the objection properly, change what's fair, or find a smaller first step they can live with."),
                ("Isn't pre-wiring just politics?",
                 "It's preparation. Done openly, it gives every decision maker time to think, which leads to better decisions."),
            ],
            last_word="Meetings don't make decisions. People do. Usually on Tuesday, near the coffee machine.",
        ),
        # ------------------------------------------------------------------ 3
        dict(
            slug="blood-pacts",
            ring="I OWE YOU ONE ✠ HAPPY TO HELP ✠ LET'S STAY CLOSE ✠", scrawl="dig the well before you're thirsty",
            name="Blood Pacts", sigil="⚭",
            epithet="Alliances are made in peacetime. In war, it's too late.",
            threat=2, habitat="lunches, cross-team projects, the favour nobody asked for",
            weakness="generosity, given early and kept up",
            summary="Blood Pacts: building alliances at work before you need them, by helping first and keeping your promises.",
            sighting=f"""<p>When the reorg rumours started, Pip realised that every useful person he knew in MetroVolt was
in Grid Planning. Outside his own team, he knew the barista, the IT helpdesk queue and Dorian (unfortunately).</p>
<p>Jules, meanwhile, had lunch with someone new every Thursday for two years. When the rumoured reorg list leaked,
three different directors had already asked for Jules by name. Pip asked how. Jules shrugged: “I helped people.
Then they remembered.”</p>""",
            know=f"""<p>Alliances at work are built on <b>reciprocity</b>: people help those who helped them. But the
help has to come <b>first</b> and without strings, or it feels like a transaction. A favour with a price tag is a
purchase, and people remember purchases differently.</p>
<p>The best allies are <b>outside your own team</b>: they see different information, sit in different meetings,
and can speak for you in rooms you'll never enter.</p>
{note("Networking is a horrible word for a lovely thing: being useful to people you like, before you need anything.")}""",
            omens=[
                "Everyone you know at work is in your own team.",
                "You only contact people when you need something.",
                "You learn about reorgs from the announcement email.",
                "Nobody outside your team would recognise your name.",
            ],
            counters=[
                ("The First Gift", "Help someone in another team with something small and useful. Ask nothing back.",
                 "“I saw your team's struggling with the outage data. I've got a cleaned version. Want it?”"),
                ("The Thursday Rite", "One coffee or lunch a week with someone outside your team. Ask what they're working on and what's hard.",
                 "“I'm trying to understand how Customer Ops works. Could I buy you a coffee and hear what drives you mad?”"),
                ("The Kept Word", "Do exactly what you said, by when you said. Trust compounds faster than anything else.",
                 None),
            ],
            forbidden=[
                ("The Favour Ledger", 3, "Keeping score out loud. “After everything I did for you…” turns an ally into a debtor, and debtors avoid you."),
                ("The Fair-Weather Pact", 3, "Dropping allies when they're out of favour. The building notices, and you'll be next."),
                ("The Cabal", 4, "Forming a secret group to control decisions. Cabals get found out. They always get found out."),
            ],
            difficulty=dict(
                normal="You're new or quiet. One coffee a week for three months changes everything.",
                nightmare="Teams are siloed and suspicious. Start with shared problems (data, outages, customers), not friendship.",
                hell="A blame culture where any ally can become a liability. Build many light alliances rather than a few deep ones, and keep your own record clean.",
            ),
            stats=[5, 4, 5, 4, 5, 5, 5, 3, 5], stats_for="The First Gift",
            loot=("The Ally Garden",
                  "A short list you water monthly. One line each.",
                  """NAME         TEAM            HOW I HELPED      LAST CONTACT   NEXT
Priya        Customer Ops    outage data       12 Oct         coffee
Tamsin       floor 27 EA     fixed her macro   3 Oct          say hi
Sam          Field Ops       site visit        Sep            invite to demo
Lena         Finance         —                 never          ask about budget model"""),
            trial=[
                ("Rumours of a reorg start tomorrow. Is now the time to network?",
                 "It's late, but not too late. Help first, ask nothing. In panic season, the person who gives instead of asks stands out."),
                ("A colleague helped you once. They now ask for a big favour you can't do. What do you say?",
                 "Be honest and offer what you can: “I can't do the whole thing, but I can do the data part by Friday.”"),
                ("How many allies do you need?",
                 "Enough that your name comes up in rooms you're not in. For most people, five to ten real relationships outside their team."),
            ],
            last_word="Dig the well before you're thirsty. Nobody lends a bucket during a drought.",
        ),
        # ------------------------------------------------------------------ 4
        dict(
            slug="ghost-decision",
            ring="IT WAS DECIDED ✠ BY WHOM ✠ NOBODY KNOWS ✠ IT IS DONE ✠", scrawl="who was in the room?",
            name="The Ghost Decision", sigil="☁",
            epithet="Made in a room you weren't in. By people who won't say.",
            threat=4, habitat="leadership off-sites, “quick calls”, decks marked FINAL_v7",
            weakness="asking to be in the room next time, with a reason they can accept",
            summary="The Ghost Decision: decisions that appear from nowhere, how to find out where they came from, and how to get into the room next time.",
            sighting=f"""<p>On a Monday in October, the Grid Planning team learned from a calendar invite titled
<i>“Transition: Grid Analytics to Strategy”</i> that half their work was moving to Dorian's team. Nobody had asked
them. Nobody could say who had decided.</p>
<p>“It came out of the off-site,” said Marcus, Pip's manager, who had not been at the off-site. The decision was
already in a deck called <code>FINAL_v7</code>. Six earlier versions existed. None had been shared.</p>""",
            know=f"""<p>Ghost decisions happen when decision making is <b>informal and invisible</b>: leaders decide in
small groups, often for good reasons (speed, confidentiality), and forget to explain. Sometimes they avoid
consulting on purpose, because consultation would mean argument.</p>
<p>You usually can't reverse a ghost decision. But you can learn <b>how it was made</b>, influence <b>how it's
carried out</b>, and get into the room for the <b>next one</b>. Those three are worth more than one reversed decision.</p>
{note("Being angry about not being consulted is fair. Staying angry is expensive. Spend the anger on getting invited next time.")}""",
            omens=[
                "Big changes arrive as calendar invites.",
                "Nobody can name who decided.",
                "A deck is called FINAL and has a version number above five.",
                "Your manager is as surprised as you are.",
            ],
            counters=[
                ("The Calm Inquiry", "Ask, without accusation, what problem the decision solves and how it was made. Understand before you object.",
                 "“Help me understand the problem this solves. Then I can make the transition work as well as possible.”"),
                ("The Implementation Seat", "Volunteer to help carry it out. The people who implement a decision shape most of what it becomes.",
                 "“I'd like to be on the transition team. I know where the data and the gotchas are.”"),
                ("The Next-Room Request", "Ask to be involved next time, with a reason that helps them.",
                 "“Next time Grid Analytics is discussed, could Marcus or I join for twenty minutes? We'd catch the data issues early.”"),
            ],
            forbidden=[
                ("The Rebellion", 4, "Organising your team to refuse or slow-walk the decision. Leadership hears “resistance”, and the next decision will be about you."),
                ("The Leak Hunt", 3, "Digging for who said what at the off-site. You'll get gossip, not facts, and a reputation for digging."),
                ("The Martyr Email", 4, "A long email to all about how disrespectful this was. True, maybe. Career-limiting, certainly."),
            ],
            difficulty=dict(
                normal="Leaders moved fast and forgot to explain. A calm question gets you the reasons and a seat in the transition.",
                nightmare="A pattern of decisions without consultation. Get into the implementation, and build a link to the people who do get invited.",
                hell="Decisions are made against your team on purpose. Protect your people's work in writing, find a sponsor in the room, and decide whether this is still your place.",
            ),
            stats=[3, 4, 4, 3, 4, 4, 5, 3, 4], stats_for="The Implementation Seat",
            loot=("The Ghost Decision Debrief",
                  "Five questions to ask (calmly) after any decision you weren't part of.",
                  """1. What problem does this decision solve?
2. What options were considered?
3. What's fixed, and what's still open?
4. Who will carry it out, and can I help?
5. How can our team be involved next time?"""),
            trial=[
                ("Half your team's work moves to another team without consultation. First reaction?",
                 "The Calm Inquiry: understand the problem it solves. Then ask for the Implementation Seat."),
                ("Your team wants to protest. Do you join?",
                 "Channel it: help your manager write a calm, factual note on risks and what the team needs. Protest becomes input."),
                ("How do you avoid the next ghost decision?",
                 "Make your team useful to the people in the room, and ask openly for a seat when your area is discussed."),
            ],
            last_word="If you can't be in the room, be the person the room calls.",
        ),
        # ------------------------------------------------------------------ 5
        dict(
            slug="rumour-mill-familiar",
            ring="DID YOU HEAR ✠ DON'T SAY I TOLD YOU ✠ APPARENTLY ✠", scrawl="the walls have Teams",
            name="The Rumour Mill Familiar", sigil="☊",
            epithet="Small, fast, everywhere. Feeds on half a sentence.",
            threat=3, habitat="the kitchen, the smoking area, private chats with names like “the real team”",
            weakness="facts, shared early, by the people who know them",
            summary="The Rumour Mill Familiar: how office rumours spread, what to say and never say near them, and how to use the grapevine without feeding it.",
            sighting=f"""<p>At 09:10 on a Wednesday, Pip mentioned to one person that Marcus had “looked stressed after the
budget meeting”. By 11:30, Customer Ops believed Grid Planning was being shut down. By lunch, two people had asked
Pip whether he was being made redundant. By three, Marcus had heard that Pip was spreading rumours about him.</p>
<p>Marcus had, in fact, been stressed because the coffee machine on 9 was broken.</p>""",
            know=f"""<p>The rumour mill grows in the dark: <b>uncertainty plus silence from leadership</b>. People fill gaps
with guesses, and guesses travel faster than facts because they're more interesting. Each retelling adds a little.</p>
<p>The grapevine is also genuinely useful: it often knows things weeks before the announcement. The skill is to
<b>listen without feeding it</b>. Hear everything. Repeat nothing you haven't checked. Never be the source.</p>
{note("A rumour needs three things: an anxious audience, a silent leadership, and you, saying “I probably shouldn't say this, but…”. Remove yourself from the recipe.")}""",
            omens=[
                "“I probably shouldn't say this, but…”",
                "Leadership has been quiet for weeks during a budget season.",
                "Private chats are busier than team channels.",
                "You hear your own words back, changed.",
            ],
            counters=[
                ("The Listening Ear", "Listen to rumours, thank people, and treat them as weak signals, not facts. Check with someone who knows.",
                 "“Interesting, thanks. I'll wait to hear it from Marcus before I believe it.”"),
                ("The Sealed Lips", "Never repeat anything about a person you wouldn't say with them in the room.",
                 None),
                ("The Fact Lantern", "If you lead people, share what you know early and say what you don't. Silence is the rumour mill's food.",
                 "“Here's what I know: budgets are being reviewed. Here's what I don't: whether it affects us. I'll update you on Friday either way.”"),
            ],
            forbidden=[
                ("Feeding the Familiar", 3, "Passing on a juicy rumour to be interesting. You become the source, and sources get remembered."),
                ("The Strategic Leak", 5, "Planting a rumour on purpose to shape a decision. It's traceable, it's unethical, and it's how careers end quietly."),
                ("The Total Denial", 2, "Ignoring the grapevine entirely. You'll be the last to know everything, including the things that matter."),
            ],
            difficulty=dict(
                normal="An anxious week. Listen, don't repeat, ask your manager.",
                nightmare="The grapevine is faster than every official channel. Build trusted sources, and if you lead people, run weekly fact updates.",
                hell="Rumours are weaponised: people plant stories about rivals. Keep your own conduct spotless, keep records, and talk directly to the people involved.",
            ),
            stats=[4, 3, 5, 4, 5, 4, 5, 5, 5], stats_for="The Sealed Lips",
            loot=("The Rumour Filter",
                  "Three questions before you repeat anything.",
                  """1. Do I KNOW it, or did I hear it?
2. Would I say it with the person it's about standing here?
3. Does repeating it help anyone except my need to be interesting?

If any answer is no: don't."""),
            trial=[
                ("A colleague says your team will be cut next month. What do you do?",
                 "Thank them, don't repeat it, and ask your manager directly: “I've heard this. Is there anything you can tell me?”"),
                ("You let slip that your manager looked stressed and it's grown into a story. Now what?",
                 "Go to your manager first and own it: “I said something careless and it grew. I'm sorry. Here's what I actually said.”"),
                ("You manage a team during a budget review and know very little. What do you tell them?",
                 "The Fact Lantern: what you know, what you don't, and when you'll update them. Even “nothing new” beats silence."),
            ],
            last_word="Hear everything. Repeat nothing you couldn't sign.",
        ),
        # ------------------------------------------------------------------ 6
        dict(
            slug="cc-inquisition",
            ring="LOOPING IN ✠ ADDING MY MANAGER ✠ FOR VISIBILITY ✠ REPLY ALL ✠", scrawl="the CC line is a weapon",
            name="The CC Inquisition", sigil="✉",
            epithet="Every name on the CC line is a witness. Or a threat.",
            threat=3, habitat="email, especially Friday at 16:58",
            weakness="the phone call, and the courage to take people off the thread",
            summary="The CC Inquisition: email politics, from CC and BCC to reply-all and “looping in my manager”, and how to keep threads clean and fair.",
            sighting=f"""<p>Pip asked Gareth's team a simple question about asset data. Gareth replied, copying Pip's manager,
his own director and Lord Varnish: <i>“Looping in leadership for visibility, as this seems to be a recurring
misunderstanding.”</i> It was not recurring. It was the first time.</p>
<p>Pip replied to all, explaining at length. Gareth replied to all. By Friday there were fourteen people on a thread
about one spreadsheet column, and Lord Varnish had replied with a single line: <i>“Can we take this offline?”</i>
which, in MetroVolt, means “you have both embarrassed me”.</p>""",
            know=f"""<p>The CC line is <b>power made visible</b>. Adding someone's boss turns a question into an escalation.
Adding your own boss says “I have a witness”. BCC says “I'm showing someone this behind your back”. Reply-all on a
dispute turns a disagreement into theatre.</p>
<p>Most CC escalations come from <b>anxiety</b>, not malice: people want cover. The counter is to lower the
temperature: take it off the thread, solve it, then report the solution to the same audience.</p>
{note("BCC is the single most dangerous button in Outlook. Someone always replies-all from the BCC line. Always.")}""",
            omens=[
                "Your boss appears on a thread you started.",
                "“For visibility.” “Looping in.” “Adding X for awareness.”",
                "Long replies-to-all on a disagreement.",
                "You're BCC'd on something. (Don't reply.)",
            ],
            counters=[
                ("The Phone Exorcism", "When a thread heats up, call or walk over. Solve it in person.",
                 "“Gareth, rather than fill everyone's inbox, can I call you for five minutes? I think we can sort this quickly.”"),
                ("The Clean Report", "After solving it, reply once to the full audience with the outcome, crediting the other person.",
                 "“Quick update for everyone: Gareth and I spoke, the column means X, all sorted. Thanks Gareth.”"),
                ("The Gentle Uncopy", "When you start a thread, copy only who needs to act. Move escalations to a new, smaller thread.",
                 None),
            ],
            forbidden=[
                ("The Counter-Escalation", 4, "Copying even more senior people back. Now it's a war with an audience. Everyone loses, especially the audience."),
                ("The BCC Snare", 5, "Secretly BCC'ing your boss to show them someone's bad behaviour. One accidental reply-all, and you're the snake."),
                ("The Essay of Righteousness", 3, "A long reply-all proving you were right. Nobody reads past line three. Everyone remembers the length."),
            ],
            difficulty=dict(
                normal="An anxious colleague copying their boss for cover. Call them, solve it, report it.",
                nightmare="CC escalation is the house style. Keep threads small, solve things by phone, and agree with your manager how to handle it.",
                hell="Someone uses CC lines to build a case against you. Stay factual, keep copies, never match the tone, and brief your manager before the threads reach them.",
            ),
            stats=[4, 3, 4, 3, 4, 5, 5, 5, 5], stats_for="The Phone Exorcism",
            loot=("The De-Escalation Email",
                  "Use after a call. Same audience as the angry thread. Short, factual, generous.",
                  """Subject: RE: Asset data question (resolved)

Hi all,

Gareth and I spoke this morning. Summary:
  • "In service date" = commissioning date, not install date
  • I'll update the model by Thursday
  • No other changes needed

Thanks Gareth for the quick help.
Pip"""),
            trial=[
                ("Someone copies your manager and theirs on a small issue. What's your first move?",
                 "Call them. Solve it off the thread. Then send one short, generous resolution to the same audience."),
                ("You're BCC'd on a dispute between two colleagues. What do you do?",
                 "Nothing on the thread. If it matters, talk to the person who BCC'd you, in person."),
                ("Should you ever copy your own manager?",
                 "Yes, when they need to act or decide, and openly. Not as a shield."),
            ],
            last_word="Fourteen people on a thread is not a discussion. It's a crowd watching a fight.",
        ),
        # ------------------------------------------------------------------ 7
        dict(
            slug="turf-wars",
            ring="THAT'S OUR AREA ✠ NOT YOUR REMIT ✠ WHO OWNS THIS ✠", scrawl="both towers are on fire",
            name="The Turf Wars of the Two Towers", sigil="♜",
            epithet="Two departments. One problem. Neither will touch it, both will own it.",
            threat=4, habitat="the gap between two teams, RACI charts nobody agreed",
            weakness="a shared customer problem with numbers on it",
            summary="The Turf Wars: departments fighting over ownership, and how to get work done between two towers without becoming the next casualty.",
            sighting=f"""<p>Smart meters that failed to report were, according to Grid Planning, a Customer Ops problem
(customers complained). According to Customer Ops, a Network Assets problem (the meters were broken). According to
Network Assets, a Lumen problem (the project installed them). According to Lumen, a Grid Planning problem
(it was data).</p>
<p>By November, 11,400 meters had been failing for an average of 63 days. Each department had a slide proving it
was someone else's. Pip had a spreadsheet proving that 11,400 customers were getting estimated bills.</p>""",
            know=f"""<p>Turf wars happen when <b>ownership is unclear</b> and <b>incentives differ</b>: each department is
measured on its own targets, so a shared problem is pure cost. Owning it means budget, effort and blame. Not
owning it is free. Until it's on the front page.</p>
<p>You can't settle a turf war from the middle. But you can make the <b>customer problem impossible to ignore</b>,
with numbers, and offer a way for both towers to win.</p>
{note("Nothing ends a turf war like a number with a pound sign next to it and a newspaper headline next to that.")}""",
            omens=[
                "“That's not our remit.”",
                "Problems bounce between teams in the ticket system.",
                "Every department has a slide about why it's someone else's.",
                "Customers are suffering in the gap.",
            ],
            counters=[
                ("The Shared Wound", "Frame the problem around the customer and the cost, not the org chart. Put a number on it.",
                 "“11,400 customers have had estimated bills for two months. That's about £1.2m in disputed billing. Who can we put on it together?”"),
                ("The Joint Pact", "Propose a small, time-boxed joint fix with a named person from each side. Small is easier to say yes to.",
                 "“Could Ops and Assets each give one person for four weeks? I'll run the data side.”"),
                ("The Escalation Above Both", "If it stays stuck, take it, together with both sides, to the first leader above both towers.",
                 "“Priya and Gareth both agree this needs an owner. Could you decide who, by Friday?”"),
            ],
            forbidden=[
                ("Picking a Tower", 4, "Joining one side to win the war. The other tower now treats you as an enemy combatant, permanently."),
                ("The Land Grab", 4, "Quietly taking over the disputed area to build your own empire. See entry 8. Don't be entry 8."),
                ("The Sigh and Shrug", 2, "Deciding it's not your problem either. The 11,400 customers disagree."),
            ],
            difficulty=dict(
                normal="Two teams who've never talked. Get them in a room with the customer data. Usually it's sorted in a week.",
                nightmare="Long-running rivalry. Use the Joint Pact, keep it small, and give both leaders credit.",
                hell="Leaders above both towers are rivals too. Escalate in writing with numbers, keep a record, and let the cost do the arguing.",
            ),
            stats=[3, 5, 3, 4, 3, 4, 5, 2, 4], stats_for="The Shared Wound",
            loot=("The Orphan Problem Brief",
                  "One page that makes a gap between teams visible and fixable.",
                  """PROBLEM    11,400 smart meters not reporting, avg 63 days
IMPACT     estimated bills, ~£1.2m disputed, 2,100 complaints
TOUCHES    Customer Ops (complaints), Network Assets (hardware),
           Lumen (install), Grid Planning (data)
OWNER      none today
ASK        one person each from Ops + Assets for 4 weeks;
           decision on long-term owner by 30 Nov
DECIDER    Ottoline Grey (above both towers)"""),
            trial=[
                ("A problem sits between two departments and both say it isn't theirs. What's your first move?",
                 "Make the customer impact and cost visible, with numbers, to both sides at once."),
                ("One department lead asks you to help prove it's the other team's fault. Do you?",
                 "No. Offer to help fix it instead. The moment you pick a tower, you lose the other one."),
                ("The joint fix works. Who gets credit?",
                 "Both towers, publicly and equally. That's what makes them say yes next time."),
            ],
            last_word="In a turf war, the only safe flag to wave is the customer's.",
        ),
        # ------------------------------------------------------------------ 8
        dict(
            slug="empire-builder",
            ring="MORE HEADCOUNT ✠ BIGGER REMIT ✠ REPORT TO ME ✠", scrawl="headcount is not output",
            name="The Empire Builder", sigil="♚",
            epithet="Collects headcount like dragon gold. Sleeps on it.",
            threat=3, habitat="budget season, reorg slides, anything with “centre of excellence” in the title",
            weakness="questions about outcomes, not size",
            summary="The Empire Builder: the colleague who grows their team for status, how to work with them, and how not to become one.",
            sighting=f"""<p>Gareth Pound began 2024 with 40 people in Network Assets. By autumn 2026 he had 112, a
“Centre of Excellence for Asset Intelligence”, two deputies and a slide titled <i>Our Expanding Footprint</i>.
Asset data quality had not improved. It had, in fact, got worse: there were now three teams cleaning it, each in a
different way.</p>
<p>In October, Gareth proposed absorbing Grid Planning's data work. “Synergies,” he explained. Pip asked which
problem it would solve. Gareth looked at him as a dragon looks at someone asking why it needs so much gold.</p>""",
            know=f"""<p>In many companies, <b>size is status</b>: bigger teams mean bigger titles, bigger budgets and a
louder voice. So some managers grow teams because growth itself is rewarded, not because the work needs it.</p>
<p>Empire builders aren't always bad managers. Some genuinely believe in their area. The test is simple:
<b>does the empire produce better outcomes, or just more empire?</b> Ask about outcomes, every time, politely.</p>
{note("A centre of excellence is a team that has not yet been asked what it's excellent at.")}""",
            omens=[
                "Every problem is solved by moving it into their team.",
                "Their slides show headcount, not results.",
                "“Centre of excellence”, “hub”, “one front door”.",
                "Their team duplicates work done elsewhere.",
            ],
            counters=[
                ("The Outcome Question", "Ask what will be measurably better, and by when, if the work moves.",
                 "“If the data work moves to Network Assets, what will be better in six months, and how will we know?”"),
                ("The Service Offer", "Offer a clear service instead of a takeover: you keep the work, they get what they need.",
                 "“What if we keep the model, and give your team a weekly data feed with an agreed quality bar?”"),
                ("The Ally in Finance", "Budget owners care about duplication. Show them the three teams doing the same thing.",
                 None),
            ],
            forbidden=[
                ("The Rival Empire", 4, "Building your own empire to fight theirs. Now there are two dragons and the gold is still dirty data."),
                ("The Sabotage Hoard", 5, "Withholding data or help to make their team fail. They'll fail loudly, and point at you."),
                ("The Mocking Song", 3, "Sneering about “Gareth's kingdom” in meetings. Dragons have long memories and senior friends."),
            ],
            difficulty=dict(
                normal="An ambitious manager. The Outcome Question keeps proposals honest.",
                nightmare="They're winning: work keeps flowing to them. Offer services, track outcomes, and make results visible.",
                hell="Leadership rewards size above all. Protect your team's core work in writing, and build your reputation on results that can't be absorbed.",
            ),
            stats=[4, 4, 4, 4, 4, 3, 5, 4, 4], stats_for="The Outcome Question",
            loot=("The Outcome Test",
                  "Five questions for any proposal to move work or people. Ask them about your own proposals too.",
                  """1. What problem gets solved, for whom?
2. What will be measurably better, by when?
3. What does it cost (people, money, disruption)?
4. What gets duplicated, and what gets dropped?
5. How will we know in 6 months if it worked?"""),
            trial=[
                ("An empire builder proposes absorbing your team's work. What's your reply in the meeting?",
                 "The Outcome Question: what will be measurably better, by when? Then offer a service instead."),
                ("Your own manager wants more headcount. Is that empire building?",
                 "Only if it's not tied to outcomes. Help them write the case in outcomes, not size."),
                ("Is it ever right to grow a team fast?",
                 "Yes, when demand is real and results follow. The test is outcomes, not intentions."),
            ],
            last_word="Ask a dragon what the gold is for. It hates that.",
        ),
        # ------------------------------------------------------------------ 9
        dict(
            slug="ring-kissing-ritual", flagship=True,
            plate_caption="The ritual, as performed daily on floor 27. Note the queue. Note the ring. Note who isn't in the queue.",
            ring="GREAT POINT ✠ LOVE THAT ✠ AS YOU SAID ✠ BRILLIANT AS ALWAYS ✠", scrawl="managing up is not kneeling",
            name="The Ring-Kissing Ritual", sigil="⚜",
            epithet="Some kneel. Some manage up. Learn the difference before your knees go.",
            threat=4, habitat="leadership meetings, LinkedIn comments under the CEO's posts, the lift with Lord Varnish",
            weakness="usefulness: the boss who has a choice between flattery and help picks help, eventually",
            summary="The Ring-Kissing Ritual: kissing ass versus managing up, why flattery works (for a while), and how to build influence with powerful people without losing your soul.",
            sighting=f"""<p>Every Monday at the leadership stand-up, Dorian opened with praise for Lord Varnish. “Great point
in your email.” “Love how you framed that.” “As you said last week…” Lord Varnish glowed. Dorian got the good projects.</p>
<p>Pip tried it once. “Great framing, Lord— er, Simon.” It came out like a man reading a hostage statement. Lord
Varnish looked at him with mild alarm. Afterwards Marcus took Pip aside. “Don't do that,” he said gently. “Just be
useful to him. It lasts longer.”</p>""",
            know=f"""<p>Flattery works because <b>leaders are human</b>: they're insecure, under pressure, and rarely praised
themselves. Someone who makes them feel good gets their attention. That's why the ritual exists.</p>
<p>But flattery has a short shelf life and a long cost. People notice it, peers resent it, and the leader learns
nothing true from you. <b>Managing up</b> is different: you understand your boss's goals and pressures, and help
them succeed, honestly. That includes telling them things they don't want to hear, kindly.</p>
{note("Kissing up: making the boss feel good. Managing up: making the boss do well. The first gets you noticed. The second gets you trusted. Trusted lasts.")}""",
            omens=[
                "Every meeting starts with praise for the most senior person.",
                "Bad news never reaches the top.",
                "The same few people always get the good projects.",
                "You feel tempted to say “great point” before they've finished the point.",
            ],
            counters=[
                ("The Goal Reading", "Learn what your boss's boss is measured on and worried about. Then make your work help with that.",
                 "“What's the one thing that would make this quarter a win for you? I'd like my work to help with it.”"),
                ("The Specific Praise", "Praise is fine when it's true and specific. It's flattery when it's vague and constant.",
                 "“The way you reframed Lumen as a customer-billing fix got Finance on board. That was smart.”"),
                ("The Honest Warning", "Bring bad news early, with a suggestion. Leaders remember who warned them.",
                 "“Heads-up before the board: the meter numbers will look bad. Here's why, and here's what we're doing.”"),
            ],
            forbidden=[
                ("The Full Prostration", 4, "Agreeing with everything the boss says. When their idea fails, you'll be the one who said “brilliant”."),
                ("The Public Groveling", 3, "Liking every one of the CEO's posts within four minutes. Everyone can see it. Everyone."),
                ("Kissing Up, Kicking Down", 5, "Charming to those above, cruel to those below. The people below talk. Eventually upwards."),
            ],
            difficulty=dict(
                normal="A boss who likes praise but values results. Be specific, be useful, be honest.",
                nightmare="Flatterers are winning. Keep delivering, make your results visible, and build a reputation as the person who tells the truth kindly.",
                hell="Only loyalty is rewarded, and honesty is punished. Protect yourself, document your work, find a sponsor elsewhere, and consider whether you want to rise in this court.",
            ),
            stats=[4, 5, 4, 3, 4, 4, 5, 4, 3], stats_for="The Goal Reading",
            loot=("The Manage-Up Card",
                  "Five lines about your boss (and your boss's boss). Update them every quarter.",
                  """THEIR TOP GOAL      Lumen rollout on time for the regulator (Mar)
THEIR WORRY         billing complaints reaching the CEO
HOW THEY LIKE NEWS  short, early, with a fix
WHAT I CAN DO       weekly meter-failure numbers before the board
WHAT I MUST NOT DO  surprise them in front of Dame Helena"""),
            trial=[
                ("Your peer flatters the VP and gets the best projects. Should you do the same?",
                 "No. Learn the VP's goals and make your work help with them. Specific, honest praise when it's earned."),
                ("The VP's pet idea has a real flaw. What do you do?",
                 "Tell them privately, early, with respect and a suggestion: the Honest Warning."),
                ("Is it OK to praise your boss at all?",
                 "Yes, when it's true and specific. Leaders get little real feedback; good, honest praise is rare and valued."),
            ],
            last_word="Kiss the ring and you'll get a seat. Help the king and you'll get a voice.",
        ),
        # ------------------------------------------------------------------ 10
        dict(
            slug="chosen-one",
            ring="THEY'RE ONE TO WATCH ✠ HIGH POTENTIAL ✠ OBVIOUSLY ✠", scrawl="it's not about you (mostly)",
            name="The Chosen One", sigil="✶",
            epithet="Every court has a favourite. It is rarely you.",
            threat=3, habitat="talent reviews, stretch assignments, the VP's “quick coffee”",
            weakness="your own visible results, and a sponsor of your own",
            summary="The Chosen One: favouritism at work, what to do when you're not the favourite (or when you are), and how to tell favouritism from fair recognition.",
            sighting=f"""<p>Jules got the Lumen board presentation. Then the trip to the regulator. Then the “high potential”
programme, which nobody had told Pip existed. Every time Lord Varnish needed someone, he said “ask Jules”.</p>
<p>The worst part was that Jules was good. Kind, fast, clear. Pip couldn't even hate them properly. He tried once,
for an afternoon, and Jules brought him a coffee and asked how his model was going. It was exhausting.</p>""",
            know=f"""<p>Favouritism is partly <b>human nature</b>: leaders trust people who are like them, who've succeeded
before, or who make their lives easier. Once someone is chosen, they get more chances, so they succeed more, so they
get chosen more. It compounds.</p>
<p>Sometimes it's unfair. Sometimes it's earned, and simply <b>more visible</b> than your work. Before you decide which,
ask honestly: what does the favourite do that you don't? Visibility? Speed? Making the leader's life easier?</p>
{note("Most favourites aren't chosen for being brilliant. They're chosen for being reliable in front of the person choosing. You can learn that.")}""",
            omens=[
                "The same name comes up for every opportunity.",
                "Programmes and trips you hear about after they're full.",
                "Your work is praised; theirs is rewarded.",
                "You catch yourself counting their wins.",
            ],
            counters=[
                ("The Honest Mirror", "Ask your manager what the favourite does that you could do more of. Listen without defending.",
                 "“Jules gets a lot of the visible work. What would I need to show for you to put me forward too?”"),
                ("The Direct Ask", "Ask for specific opportunities, by name. Leaders often simply don't think of the quiet ones.",
                 "“I'd like to present the meter data at the next board. Could I take that one?”"),
                ("The Own Sponsor", "Find someone senior who values your work and will put your name forward. Different courts have different favourites.",
                 None),
                ("The Fairness Check", "If favouritism crosses into unfair treatment (pay, promotion, protected traits), document it and raise it formally.",
                 None),
            ],
            forbidden=[
                ("The Usurper's Plot", 4, "Undermining the favourite to take their place. You'll be seen as bitter, and the leader will protect their choice."),
                ("The Sulk", 3, "Withdrawing and doing the minimum because it's unfair. It confirms the leader's choice."),
                ("The Copycat", 2, "Imitating the favourite's style. You'll be a weaker version of someone who's already there."),
            ],
            difficulty=dict(
                normal="A leader who leans on one reliable person. Make yourself visible and ask directly.",
                nightmare="A clear inner circle. Find your own sponsor, build visibility outside your manager's view, and keep delivering.",
                hell="Favouritism tied to personal relationships, or to things like gender, age or background. Keep records and use formal channels; this is a fairness issue, not a career tip.",
            ),
            stats=[3, 5, 4, 3, 4, 4, 5, 4, 4], stats_for="The Direct Ask",
            loot=("The Visibility Ask",
                  "A short note to your manager. Specific, positive, about the future.",
                  """Hi Marcus,

I'd like to grow my visibility this year. Three things I'd love
to do:
  1. Present the meter-failure data at the Jan board
  2. Join the regulator prep for Lumen
  3. Be considered for the high-potential programme

What would you need to see from me to put me forward?

Pip"""),
            trial=[
                ("The favourite gets an opportunity you wanted. What's your first move?",
                 "Ask your manager what you'd need to show to be considered next time, and ask for a specific opportunity."),
                ("You become the favourite. Is that a problem?",
                 "Enjoy it, and share it: bring others into the work and credit them. Courts change; allies stay."),
                ("When is favouritism a formal issue?",
                 "When it affects pay, promotion or treatment unfairly, especially linked to protected characteristics. Document and raise it."),
            ],
            last_word="Don't wait to be chosen. Ask to be considered. It's shocking how often that works.",
        ),
        # ------------------------------------------------------------------ 11
        dict(
            slug="sacrificial-lamb", flagship=True,
            plate_caption="The handover of Project Orion. Seven candles, one lamb, a lanyard that says PROJECT LEAD.",
            ring="GREAT OPPORTUNITY ✠ HIGH VISIBILITY ✠ YOU'LL OWN IT ✠", scrawl="read the project's obituary first",
            name="The Sacrificial Lamb", sigil="♈",
            epithet="“A great opportunity for you.” (It is doomed. You are the opportunity.)",
            threat=5, habitat="failing projects, stretch assignments offered with unusual warmth",
            weakness="questions asked before you say yes, and agreements in writing",
            summary="The Sacrificial Lamb: being set up to take the blame for a doomed project, how to spot it, and how to accept (or decline) without being sacrificed.",
            sighting=f"""<p>In November, Lord Varnish called Pip to floor 27 for the first time. There was coffee. There was
warmth. There was <b>Project Orion</b>: a new billing integration, eighteen months late, £2.4 million over budget,
already on its third project lead. “It needs fresh eyes,” said Lord Varnish. “Real visibility for you.”</p>
<p>Tamsin, walking past with a folder, met Pip's eye for exactly one second. In that second, Pip learned more than in
the whole meeting.</p>""",
            know=f"""<p>When a project is failing, leaders need someone to <b>own</b> it, and sometimes to <b>be blamed</b>
for it. The most senior people step back. The task goes to someone junior and eager, who can't refuse and won't know
the history. If it fails, it was the lead. If it succeeds, it was the sponsor's vision.</p>
<p>Not every hard assignment is a trap. Rescuing a failing project can make a career. The difference is in the
<b>terms</b>: authority, resources, a reset plan, and a sponsor who'll stand next to you when it gets bad.</p>
{note("If you're offered a project with unusual warmth, read the project's obituary first. Ask who led it before you, and where they are now.")}""",
            omens=[
                "Unusual warmth from someone senior who's never spoken to you.",
                "“Fresh eyes”, “real visibility”, “a great opportunity for you”.",
                "Previous leads have left, been moved, or gone quiet.",
                "No one can tell you the real budget or the real date.",
                "The sponsor's name is nowhere on the project.",
            ],
            counters=[
                ("The Autopsy First", "Before you answer, learn the history: previous leads, real status, why it failed. Ask them.",
                 "“I'm honoured. Before I commit, could I spend a few days understanding where it stands? I want to do it properly.”"),
                ("The Terms of Sacrifice", "Agree, in writing, what you need: a reset of date and budget, decision rights, people, and a named sponsor.",
                 "“I'll take it on with a reset plan by the 15th, authority over scope, two engineers, and you as visible sponsor. Can we agree that in writing?”"),
                ("The Honest Baseline", "On day one, publish the true state of the project. Anything that was broken before you is now on record as before you.",
                 "“Status on taking over: 18 months late, £2.4m over, three open blockers. Recovery plan to follow in two weeks.”"),
                ("The Graceful No", "If the terms aren't given, decline politely, with reasons.",
                 "“I'd love to help, but without a reset of date and budget I couldn't succeed, and I don't want to fail you.”"),
            ],
            forbidden=[
                ("The Eager Yes", 5, "Saying yes on the spot, flattered. You've just signed up for the old date, the old budget and all the old blame."),
                ("The Silent Takeover", 4, "Taking over without publishing the baseline. In six months, the delay will be yours."),
                ("The Blame Return", 3, "Spending your time blaming previous leads in public. True or not, it looks like excuse-making."),
            ],
            difficulty=dict(
                normal="A hard project with a real sponsor. Agree the terms and it's a genuine opportunity.",
                nightmare="A failing project with a vague sponsor. Insist on the baseline and terms in writing, and report honestly every fortnight.",
                hell="The project is a political sacrifice and everyone knows it but you. Decline gracefully, or accept only with written terms and a sponsor who has something to lose.",
            ),
            stats=[2, 4, 3, 5, 3, 3, 5, 2, 3], stats_for="The Terms of Sacrifice",
            loot=("The Terms of Sacrifice",
                  "Send after any “great opportunity” meeting. If they won't confirm it, you have your answer.",
                  """Subject: Project Orion: confirming what we agreed

Hi Simon,

Thanks for the chance to lead Orion. As agreed today:
  1. I'll publish the current status (as-is) on day 1
  2. A reset plan (date + budget) by 15 Dec, for your sign-off
  3. Decision rights over scope, within the reset budget
  4. Two engineers from Grid Analytics from 1 Dec
  5. You as named sponsor, at the fortnightly steering

Shout if I've got any of that wrong.
Pip"""),
            trial=[
                ("A VP offers you a failing project with great warmth. What do you say in the meeting?",
                 "Thank them and ask for a few days to understand it: the Autopsy First. Never say yes in the room."),
                ("You agree to take it on. What's the first thing you publish?",
                 "The Honest Baseline: the true state on the day you took over."),
                ("The VP won't put the terms in writing. What does that tell you?",
                 "That they want the option to blame you. Decline gracefully, or proceed knowing exactly what you're risking."),
            ],
            last_word="Before you pick up the knife, check whose neck the ceremony is for.",
        ),
        # ------------------------------------------------------------------ 12
        dict(
            slug="plausible-silence",
            ring="NO COMMENT ✠ I'LL THINK ABOUT IT ✠ GOOD QUESTION ✠", scrawl="silence is a full sentence",
            name="The Art of Plausible Silence", sigil="☉",
            epithet="Sometimes the most powerful thing you can say is nothing. For now.",
            threat=2, habitat="heated meetings, the after-meeting drink, a VP's leading question",
            weakness="the pause, held calmly",
            summary="The Art of Plausible Silence: when not speaking is the strongest move in office politics, and how to buy time without looking evasive.",
            sighting=f"""<p>At the budget review, Lord Varnish asked the room: “Which team could give up 10% of its budget?”
Gareth said nothing. Priya said nothing. Pip, eager, said: “Grid Planning could probably find some savings in
the—”</p>
<p>By Friday, Grid Planning's budget was 12% smaller. Marcus found out from Finance. He was very kind about it,
which was somehow worse.</p>""",
            know=f"""<p>In politics, <b>what you say is on record</b> and what you don't say mostly isn't. Every
offhand remark can become a commitment, a quote or a weapon. Experienced people pause, ask questions and say
“let me come back to you” far more than juniors do. It isn't evasion. It's <b>thinking before committing</b>.</p>
<p>Silence is not lying, and it's not cowardice. If you know something serious (harm, fraud, danger), silence is
wrong. But for most questions, a short pause and a considered answer beats a fast, regrettable one.</p>
{note("Juniors fill silences. Seniors let them sit. The person who speaks first in an awkward silence usually just volunteered for something.")}""",
            omens=[
                "A senior person asks an open question to the room.",
                "You feel an urge to fill an awkward pause.",
                "“Off the record…” “Just between us…”",
                "A question that would commit your team or your manager.",
            ],
            counters=[
                ("The Held Pause", "Count to three before answering a loaded question. Often someone else answers, or the question changes.",
                 None),
                ("The Time Charm", "Buy time without looking evasive: promise a considered answer by a specific time.",
                 "“Good question. I'd rather give you a proper answer than a quick one. Can I come back by Thursday?”"),
                ("The Manager's Seal", "Don't commit your team or your manager's resources without them. Say so plainly.",
                 "“That's Marcus's call. I'll make sure he has the numbers today.”"),
                ("The Question Back", "Answer a vague question with a clarifying one.",
                 "“When you say savings, do you mean this year's budget or next year's plan?”"),
            ],
            forbidden=[
                ("The Stone Wall", 3, "Saying nothing, ever, about anything. You'll seem evasive or uninterested, and people stop asking you."),
                ("The Silent Witness", 5, "Staying quiet about real wrongdoing to stay safe. That's not strategy, it's complicity. See Act VIII, the Dark Pact."),
                ("The Mysterious Hint", 3, "Hinting that you know more than you say, to seem important. People will assume you're the leak."),
            ],
            difficulty=dict(
                normal="An eager habit of answering too fast. Practise the Held Pause for a month.",
                nightmare="Leadership fishes for commitments in public. Use the Time Charm and the Manager's Seal every time.",
                hell="Anything you say is used against you. Say less, write carefully, and save your voice for the things that truly matter.",
            ),
            stats=[5, 3, 5, 4, 5, 3, 4, 5, 5], stats_for="The Time Charm",
            loot=("Five Ways to Say Nothing (Politely)",
                  "For when the honest answer is “not yet”.",
                  """1. "Good question. Let me come back to you by Thursday."
2. "That's Marcus's call. I'll get him the numbers today."
3. "When you say X, do you mean A or B?"
4. "I don't know yet, and I'd rather not guess."
5. "Can I think about that and send you something short?\""""),
            trial=[
                ("A VP asks the room which team could cut 10%. What do you say?",
                 "Nothing, or a clarifying question. Never volunteer your team's budget without your manager."),
                ("Someone says “off the record, what do you think of your manager?” What now?",
                 "Nothing off the record exists. Say something true and fair you'd be happy to see quoted."),
                ("When is silence wrong?",
                 "When you know about serious harm, fraud or danger. Then speaking up (carefully, in the right channel) is the duty."),
            ],
            last_word="Silence can't be quoted. Use that, but never to hide harm.",
        ),
    ],
)
