# Series 4 · Act I · the long-form story fields (format v2), merged into content/darkside/act-1.py by scripts/grimoire.py.
# Act I's entries are rituals and places as much as creatures, so origins often tell how a habit or culture formed.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the Map of Hidden Thrones
    "hidden-thrones": dict(
        sighting=f"""{beat("Monday 1 September · the proposal")}
<p>Pip wrote two pages: move the Lumen smart-meter rollout to the districts with the worst outage history first. Fewer
estimated bills, fewer complaints, happier regulator. It was obviously right. He sent it, as the org chart said he should,
up the line to Lord Varnish, whose box was the biggest on the page.</p>
{beat("September and most of October · silence")}
<p>Nothing happened for five weeks. Pip followed up twice. Lord Varnish's assistant said it was “with Simon”. Simon, it
turned out, was Lord Varnish.</p>
{beat("Tuesday 7 October · the announcement")}
<p>The plan was approved, almost word for word, as <i>“Ottoline's sequencing idea”</i>. Pip had never heard of Ottoline.
He looked her up: Chief of Staff to the CEO. A small box, off to the side of the chart, with a dotted line.</p>
{beat("Wednesday 8 October · Tamsin")}
<p>Pip asked Tamsin, the assistant on floor 27, how this had happened. Tamsin smiled the smile of someone who has
watched this happen many times. “Simon forwards everything good to Ottoline,” she said. “Ottoline decides what reaches
Dame Helena. You sent your idea to the biggest box. It walked, by itself, to the smallest one.”</p>
{note("Power = information + access + trust. Titles are just where the building keeps the furniture.")}""",
        origin=dict(
            title="How a small box became the hidden throne",
            beats=[
                ("2019 · a new CEO", "Dame Helena Strand arrives at MetroVolt from the parent group. She doesn't know anyone, doesn't trust the existing VPs, and needs one person she can rely on."),
                ("2019 · the hire", "She brings Ottoline Grey from her previous company as Chief of Staff: no team, no budget, a small box on the chart. And the CEO's diary, inbox and ear."),
                ("2020 to 2023 · the drift", "Every VP learns that the fastest way to the CEO is through Ottoline. Briefings, ideas and bad news all route through her office. Decisions follow the information."),
                ("2025 · two maps", "The org chart still shows VPs at the top. The real map shows a small office on floor 27 with a teapot. Nobody ever announced the change. It simply happened, one forwarded email at a time."),
            ],
            turning="The CEO's decision to trust one person more than the hierarchy. Not sinister, just human. But it rewired how the whole building decides.",
            saved="Nothing needed saving: hidden thrones are normal. What needed changing was Pip's map, not Ottoline's power.",
            note="Most hidden thrones were built by trust, not ambition. Respect that, and the throne-holders tend to respect you back.",
        ),
        know=f"""<p>Every organisation has two maps. The <b>formal map</b> (the org chart) shows reporting lines. The <b>real
map</b> shows influence: who decision makers listen to, who controls the calendar, who has been right before, who can say
no quietly. The two overlap, but less than you'd think.</p>
<h3 class="kh">What the throne-holders want</h3>
<p>Usually, to protect the person they serve: no surprises, no wasted time, no embarrassment. Bring them that, and you're welcome.</p>
<h3 class="kh">Why hidden thrones thrive</h3>
<p>Because information is power, and senior people can't read everything. Whoever filters what reaches them shapes what
they decide. Long service, trust and access count for more than a box on a chart.</p>
<h3 class="kh">What they dislike</h3>
<ul class="fears"><li>People who only appear when they want something.</li><li>Surprises for the person they protect.</li><li>Being bypassed or used as a back door.</li><li>Long documents.</li></ul>
<h3 class="kh">The three kinds of throne</h3>
<div class="breeds">
<div><b>The Gatekeeper</b><p>Controls the calendar and the inbox. Tamsin. Never underestimate an executive assistant.</p></div>
<div><b>The Advisor</b><p>The chief of staff or right hand who shapes the leader's view. Ottoline.</p></div>
<div><b>The Old Oak</b><p>The long-serving expert everyone quietly checks with. Lionel. Terrence.</p></div>
</div>
{note("Don't ask who's in charge. Ask who they call before they decide.")}""",
        difficulty=dict(
            normal=dict(who="A healthy organisation with a few informal influencers.",
                        know=["The chart mostly matches reality.", "Influencers are open about their role.", "Your manager can explain how decisions get made."],
                        do=["Ask how decisions were made after they're made.", "Learn who the key advisors are.", "Keep them informed, briefly, with useful things."],
                        avoid="Treating informal influence as illegitimate. It's how organisations work.",
                        next="If power is far from the chart and nobody admits it, you're at Nightmare."),
            nightmare=dict(who="Real power is far from the chart, and unspoken.",
                           know=["Decisions arrive from somewhere you can't see.", "Proposals vanish for weeks.", "Your manager is as surprised as you."],
                           do=["Draw your own Real Map and update it monthly.", "Introduce yourself to the throne-holders with something useful.", "Use the Double Route: formal line plus the real decider, openly, with your manager's OK.", "Ask “who else should see this?” every time."],
                           avoid="The secret back door: going round your manager to the throne. Your manager will hear it from the throne.",
                           next="If favour decides everything and can be withdrawn overnight, you're at Hell."),
            hell=dict(who="A court where proximity beats competence.",
                      know=["The same few people get everything.", "Good work goes nowhere without the right patron.", "People fall from favour suddenly."],
                      do=["Protect your record: document your work and its impact.", "Build relationships with several thrones, not one.", "Stay useful and honest.", "Keep your exit options warm."],
                      avoid="The throne-hunter: befriending gatekeepers only for access. They can smell it; it's their whole job.",
                      next="If merit truly doesn't matter here, take your merit elsewhere."),
        ),
        mirror=dict(
            title="Are you on the map?",
            intro="Hidden thrones are fine. Being invisible on the real map isn't. Tick honestly.",
            signs=["You've never spoken to the people who shape your boss's decisions.", "You don't know who your director's assistant is.", "You only send work up the formal line.",
                   "You've had an idea vanish and never found out where it went.", "You think politics is beneath you."],
            cure="This month, have one coffee with someone who advises a decision maker in your area. Bring something useful, ask nothing, and listen.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 9 October, floor 27. Pip knocks on Ottoline's open door.",
            intro="The Courteous Approach: introduce yourself with value, not a request.",
            lines=[
                ("Pip", "Hi Ottoline, I'm Pip from Grid Planning. I built the outage data behind the Lumen sequencing."),
                ("Ottoline", "Ah. The two pages. They were good."),
                ("Pip", "Thank you. I keep that data updated weekly. If it's ever useful for Dame Helena's briefings, I'm happy to send a one-page version before each board."),
                ("Ottoline", "That would be useful. She hates surprises about complaints."),
                ("Pip", "I'll copy Marcus so he's in the loop too. First one on Monday?"),
                ("Ottoline", "Monday. Tea?"),
                ("", "Pip leaves 20 minutes later having learned more about how MetroVolt works than in two years of all-hands meetings."),
            ],
            note="Notice that Pip copies his own manager. The Courteous Approach plus the Double Route: open, useful, and nobody's been bypassed.",
        ),
    ),
    # ------------------------------------------------------------------ the Meeting Before the Meeting
    "meeting-before-the-meeting": dict(
        sighting=f"""{beat("Tuesday 14 October · 10:00 · the Network Investment Board")}
<p>Pip presented his capacity plan. Seven directors, forty minutes, eighteen slides. He had rehearsed. He was ready.</p>
{beat("10:06 · slide 3")}
<p>Gareth Pound asked why nobody had consulted Network Assets. Pip said he'd been planning to. Gareth said “I see” in
the voice people use when they've decided something.</p>
{beat("10:11 · slide 5")}
<p>Priya Nair asked how it affected call-centre volumes. Pip didn't know. Lord Varnish said “interesting” in the voice
people use for a dead bird. The board asked Pip to “take it away and come back with more alignment”.</p>
{beat("10:41 · the corridor")}
<p>Priya caught him by the lifts. “Next time, show me first,” she said kindly. “I'd have said yes.” Then she added, “So
would Gareth, probably, if you'd asked him before the meeting instead of during it.”</p>
{note("The rule is: no one should hear an important idea for the first time in a meeting. Especially not the person who can kill it.")}""",
        origin=dict(
            title="How MetroVolt's board meetings became theatre",
            beats=[
                ("2013 · the Kessler incident", "A director presents a major investment to the board. Another director, unwarned, produces data showing it's based on a wrong assumption. In front of everyone. The first director never recovers."),
                ("2013 · the lesson", "Every director learns the same thing that week: never let anything surprise you in the board, and never surprise anyone else. The safest board meeting is one where everything was agreed in advance."),
                ("2014 to 2024 · the habit", "Real decisions move to corridors, coffees and 15-minute calls the day before. The board becomes a place where decisions are confirmed, not made. Everyone who's been here long enough knows."),
                ("2025 · the newcomers", "Nobody tells new people. They arrive at the board with eighteen slides and an open question, and walk straight into the old ambush."),
            ],
            turning="One public humiliation in 2013, after which no director ever again walked into the board without knowing the answer.",
            saved="It doesn't need saving: pre-wiring is a good habit. What needs fixing is that nobody tells the newcomers.",
            note="Pre-wiring is not sneaky if you do it openly. It's how sensible people make sure nobody is ambushed, including you.",
        ),
        know=f"""<p>Formal meetings are bad places to make decisions. People feel exposed and nobody wants to agree in public
to something they haven't thought through. So sensible people decide <b>before</b>, in private, and the meeting confirms it.
That's <b>pre-wiring</b>.</p>
<h3 class="kh">What decision makers want</h3>
<p>No surprises, time to think, and the chance to shape an idea before they have to defend it in public.</p>
<h3 class="kh">Why it works</h3>
<p>Because people support what they helped shape. A concern raised privately gets fixed; the same concern raised in a
meeting becomes a position that must be defended.</p>
<h3 class="kh">What kills proposals</h3>
<ul class="fears"><li>A powerful person hearing it first in the room.</li><li>An unanswered concern from someone with a veto.</li><li>Surprising someone's boss.</li><li>Eighteen slides.</li></ul>
<h3 class="kh">Three kinds of meeting</h3>
<div class="breeds">
<div><b>The Formality</b><p>Everything agreed beforehand. Ten minutes and a nod. The goal.</p></div>
<div><b>The Ambush Arena</b><p>Nobody pre-wired. Every concern becomes a fight. Where Pip went.</p></div>
<div><b>The Rubber Stamp</b><p>Decided by one person beforehand, without anyone else. Pre-wire that person's advisors.</p></div>
</div>
{note("Meetings don't make decisions. People do. Usually on Tuesday, near the coffee machine.")}""",
        difficulty=dict(
            normal=dict(who="A few stakeholders and a simple decision.",
                        know=["You know everyone who can say no.", "Nobody has a strong prior position.", "The decision is reversible."],
                        do=["See each key person for ten minutes beforehand.", "Ask what would worry them.", "Adjust and thank them in the meeting."],
                        avoid="Selling. Ask questions; listen; change things.",
                        next="If stakeholders have conflicting needs, you're at Nightmare."),
            nightmare=dict(who="Many stakeholders with conflicting needs.",
                           know=["Different directors want different things.", "Someone has a veto.", "There's history between departments."],
                           do=["Do the Walkabout with everyone who can block it.", "Use the Concern Harvest: change what's fair, credit them.", "Bring options, not one answer.", "Do the Quiet Count: don't go until the veto-holder is at least neutral."],
                           avoid="The secret alliance: pre-wiring everyone except your opponent to outvote them.",
                           next="If one person's mood decides everything, you're at Hell."),
            hell=dict(who="A board where one person decides, and their mood varies.",
                      know=["Proposals live or die on one person's reaction.", "Pre-wiring them directly isn't possible.", "Their advisors matter more than the papers."],
                      do=["Pre-wire their trusted advisors (see the Map of Hidden Thrones).", "Time your proposal for a good day.", "Keep it to one page.", "Be ready to wait."],
                      avoid="The promise sprinkle: telling each person what they want to hear. They compare notes in the meeting.",
                      next="If nothing can get through, find a smaller first step that can."),
        ),
        mirror=dict(
            title="Are you an ambusher?",
            intro="Pre-wiring is a skill. Ambushing (even by accident) costs trust. Tick honestly.",
            signs=["You've presented an idea to a group without showing the key person first.", "You've been surprised by an objection you could have predicted.", "You've raised a concern about someone's proposal for the first time in a meeting.",
                   "You think pre-wiring is “politics”.", "Your proposals often get “take it away and align”."],
            cure="Before your next important meeting, list everyone who can say no and see each one for ten minutes. And when you have concerns about someone else's proposal, tell them before the meeting, too.",
        ),
        rehearsal=dict(
            title="Scene: Monday 10 November, Gareth's office, the day before Pip's second attempt.",
            intro="The Walkabout and the Concern Harvest: ask, don't sell.",
            lines=[
                ("Pip", "Gareth, I'm bringing the capacity plan back on Tuesday. Before I do, I want to know what would worry you."),
                ("Gareth", "Nobody asked Network Assets last time. Half your capacity numbers come from our data."),
                ("Pip", "That's fair, and I'm sorry. Would you check the asset numbers on slide 4? And could we present that part together?"),
                ("Gareth", "…Fine. Joint review Thursday."),
                ("", "Tuesday, 10:00. Pip presents seven slides. Gareth says “we've checked the asset data together”. Priya says “I've seen the call-centre impact on slide 5”. Lord Varnish says “good”. It takes eleven minutes."),
            ],
            note="Same plan, same board. The difference was four conversations and one apology, all before the meeting.",
        ),
    ),
    # ------------------------------------------------------------------ Blood Pacts
    "blood-pacts": dict(
        sighting=f"""{beat("Tuesday 30 September · the rumour")}
<p>Word spread that a reorg list was being drawn up. Pip realised, with a slow chill, that every useful person he knew in
MetroVolt was in Grid Planning. Outside his own team he knew the barista, the IT helpdesk queue and Dorian
(unfortunately).</p>
{beat("Thursday 2 October · the comparison")}
<p>Jules, meanwhile, had lunch with someone new every Thursday for two years. Field Ops, Finance, Customer Ops, even
Facilities. Jules had helped Priya's team with a dashboard, helped Felicity with a booking report, and fixed Tamsin's
spreadsheet macro once, at 17:55 on a Friday.</p>
{beat("Friday 10 October · the leaked list")}
<p>When the rumoured reorg list leaked, three different directors had already asked for Jules by name. Nobody had asked
for Pip. Nobody outside Grid Planning knew what Pip did.</p>
{beat("That evening")}
<p>Pip asked Jules how. Jules shrugged. “I helped people. Then they remembered.”</p>
{note("Networking is a horrible word for a lovely thing: being useful to people you like, before you need anything.")}""",
        origin=dict(
            title="How Jules learned to dig the well",
            beats=[
                ("2021 · Jules's first job", "Jules works at a small energy start-up, heads down, brilliant, known only to their own team."),
                ("2022 · the layoff", "The start-up runs out of money. Jules is laid off on a Tuesday with no warning and no network. Three months of job applications go nowhere."),
                ("2022 · two phone calls", "Jules finally gets a job because two people they'd once helped (a former client, a peer from a course) put their name forward. Nobody else did."),
                ("2022 onwards · the vow", "Jules joins MetroVolt and decides never to be invisible again. One lunch a week. One favour a week. Asking nothing. It isn't strategy any more. It's just who they are."),
            ],
            turning="Three months of silence after a layoff, broken only by the two people Jules had helped without being asked.",
            saved="Nothing needed saving. This is the origin of a good habit, the opposite of a curse. Pip is the one who needs one.",
            note="Most people with great networks learned it the hard way. You can learn it the easy way: start this Thursday.",
        ),
        know=f"""<p>Alliances at work are built on <b>reciprocity</b>: people help those who helped them. But the help has to
come <b>first</b> and without strings, or it feels like a transaction. The best allies are <b>outside your own team</b>:
they see different information and can speak for you in rooms you'll never enter.</p>
<h3 class="kh">What allies want</h3>
<p>Someone reliable, useful and pleasant, who doesn't only appear when they need something.</p>
<h3 class="kh">Why it matters here</h3>
<p>Because at MetroVolt, reorgs, projects and promotions are decided by people who mostly know you second-hand. Your
name needs to come up in rooms you're not in, said by people who've seen you be helpful.</p>
<h3 class="kh">What breaks pacts</h3>
<ul class="fears"><li>Keeping score out loud.</li><li>Disappearing when an ally is out of favour.</li><li>Broken promises, even small ones.</li><li>Asking for big favours before giving small ones.</li></ul>
<h3 class="kh">Three kinds of ally</h3>
<div class="breeds">
<div><b>The Weak Tie</b><p>Someone you know slightly. Surprisingly powerful: they hear things you don't.</p></div>
<div><b>The Ally</b><p>Someone who'd help you and whom you'd help. Five to ten is plenty.</p></div>
<div><b>The Sponsor</b><p>Someone senior who says your name in rooms you're not in. The rarest. Earned by results.</p></div>
</div>
{note("Dig the well before you're thirsty. Nobody lends a bucket during a drought.")}""",
        difficulty=dict(
            normal=dict(who="You're new or quiet, and the organisation is friendly.",
                        know=["People are open to coffee.", "Cross-team work exists.", "You simply haven't started."],
                        do=["One coffee a week with someone outside your team.", "Make one small, useful offer a week.", "Keep every small promise."],
                        avoid="Networking only when you need something. People notice the timing.",
                        next="If teams are siloed and suspicious, you're at Nightmare."),
            nightmare=dict(who="A siloed organisation where teams compete.",
                           know=["Teams guard their data.", "Cross-team help is rare.", "People are suspicious of offers."],
                           do=["Start with shared problems (data, outages, customers), not friendship.", "Help with something concrete and small.", "Credit other teams publicly.", "Keep an Ally Garden list and water it monthly."],
                           avoid="Forming a cabal. Secret groups get found out.",
                           next="If any ally can become a liability overnight, you're at Hell."),
            hell=dict(who="A blame culture where alliances are risky.",
                      know=["People are punished for who they're seen with.", "Favour shifts suddenly.", "Allies get dropped when they fall."],
                      do=["Build many light alliances rather than a few deep ones.", "Keep your own record clean.", "Help in the open.", "Stay loyal to people, quietly, when they fall."],
                      avoid="The fair-weather pact. If you drop allies when they're out of favour, you're next.",
                      next="If you can't build trust anywhere here, build it outside, for your next job."),
        ),
        mirror=dict(
            title="Is your well dry?",
            intro="Most people only find out when they're thirsty. Tick honestly.",
            signs=["Everyone you know well at work is in your own team.", "You last helped someone in another team months ago.", "You only contact people when you need something.",
                   "Nobody outside your team would recognise your name.", "You learned about the last reorg from the announcement email."],
            cure="Pick one person outside your team this week. Find out what's hard for them. Help with one small thing. Ask for nothing. Repeat next week.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 16 October, 12:30, the canteen. Pip asks Priya to lunch for the first time.",
            intro="The Thursday Rite and the First Gift: curious, useful, asking nothing.",
            lines=[
                ("Pip", "Thanks for coming. I realised I don't really know how Customer Ops works. What drives you mad?"),
                ("Priya", "Estimated bills. We get 2,000 complaints a month and I can't tell which meters are actually broken."),
                ("Pip", "Oh, I have a cleaned list of non-reporting meters. I made it for the forecast. Want it?"),
                ("Priya", "You have what?"),
                ("Pip", "I'll send it this afternoon. No strings. Happy to update it weekly if it helps."),
                ("", "Three months later, in Act III, Priya stops Pip in a lift with a job offer. She remembers who sent the list."),
            ],
            note="Pip didn't plan the job offer. He just helped first. That's the only way blood pacts work.",
        ),
    ),
    # ------------------------------------------------------------------ the Ghost Decision
    "ghost-decision": dict(
        sighting=f"""{beat("Monday 20 October · 08:31 · a calendar invite")}
<p>The Grid Planning team learned from a calendar invite titled <i>“Transition: Grid Analytics to Strategy”</i> that half
their work was moving to Dorian's team. Nobody had asked them. Nobody could say who had decided.</p>
{beat("09:15 · the team meeting")}
<p>“It came out of the off-site,” said Marcus, who had not been at the off-site. He looked as surprised as everyone else.
The decision was already in a deck called <code>FINAL_v7</code>. Six earlier versions existed. None had been shared.</p>
{beat("11:00 · the private chat")}
<p>The team's private chat lit up: “who decided this??”, “is this about the budget?”, “are we next?” Someone suggested
refusing to hand over the data. Someone else suggested a strongly worded email to all.</p>
{beat("17:30")}
<p>Pip, who had read the Map of Hidden Thrones entry by now, did neither. He went home and wrote down three questions to
ask in the morning. They turned out to be the right three.</p>
{note("Being angry about not being consulted is fair. Staying angry is expensive. Spend the anger on getting invited next time.")}""",
        origin=dict(
            title="How MetroVolt learned to decide in small rooms",
            beats=[
                ("2020 · the leak", "A planned reorganisation leaks to the local press before staff are told. It's humiliating for leadership and frightening for staff. The CEO orders an investigation. It finds nothing."),
                ("2020 · the new rule", "Leadership decides that sensitive decisions will be made in small rooms, with as few people as possible, and announced only when final."),
                ("2021 to 2024 · the creep", "The rule spreads. Not just sensitive decisions, but ordinary ones are made at off-sites and announced as done. Small rooms are faster. Nobody argues with a calendar invite."),
                ("2025 · the ghost", "Decisions appear from nowhere, fully formed. Even the managers affected are surprised. Secrecy, introduced for one good reason, has become a habit for every reason."),
            ],
            turning="A sensible rule for sensitive decisions that slowly became the default for all decisions.",
            saved="A simple distinction: secret for genuinely sensitive things, consulted for everything else. And someone checking the difference each time.",
            note="Most ghost decisions aren't malicious. They're habits of speed and secrecy. That's why asking calmly for a seat next time often works.",
        ),
        know=f"""<p>Ghost decisions happen when decision making is <b>informal and invisible</b>: leaders decide in small groups,
often for good reasons (speed, confidentiality), and forget to explain. You usually can't reverse one. But you can learn
<b>how it was made</b>, influence <b>how it's carried out</b>, and get into the room for the <b>next one</b>.</p>
<h3 class="kh">What leaders want</h3>
<p>Speed, no leaks, and no long arguments. Consultation feels slow and risky.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because off-sites are where leaders feel most free to decide, and nobody below them is there. And because once a
decision is in a deck called FINAL, challenging it looks like resistance.</p>
<h3 class="kh">What it doesn't survive</h3>
<ul class="fears"><li>Calm questions about the problem it solves.</li><li>People who volunteer to make it work.</li><li>A reasonable request to be involved next time.</li><li>Implementation that reveals the gaps.</li></ul>
<h3 class="kh">Three kinds of ghost</h3>
<div class="breeds">
<div><b>The Secret</b><p>Genuinely confidential. Accept it; help with the transition.</p></div>
<div><b>The Shortcut</b><p>Made fast to save time. Ask to be in the room next time.</p></div>
<div><b>The Dodge</b><p>Made in private to avoid argument. Build allies in the room.</p></div>
</div>
{note("If you can't be in the room, be the person the room calls.")}""",
        difficulty=dict(
            normal=dict(who="The Shortcut. Leaders moved fast and forgot to explain.",
                        know=["It's a one-off.", "Leaders explain when asked.", "There's room to shape the details."],
                        do=["Ask calmly what problem the decision solves.", "Volunteer for the transition team.", "Ask to be involved next time, with a reason."],
                        avoid="The martyr email to all. True, maybe. Career-limiting, certainly.",
                        next="If decisions keep arriving this way, you're at Nightmare."),
            nightmare=dict(who="A pattern of decisions without consultation.",
                           know=["Every big change arrives as a calendar invite.", "Your manager is never consulted either.", "Teams are angry and talking about resistance."],
                           do=["Use the Ghost Decision Debrief (five calm questions).", "Get into the implementation, where details are decided.", "Help your manager write a calm note on risks and needs.", "Build links to people who do get invited."],
                           avoid="The rebellion: organising the team to slow-walk it. Leadership will hear “resistance”.",
                           next="If decisions are made against your team on purpose, you're at Hell."),
            hell=dict(who="The Dodge, aimed at you. Decisions are made against your team deliberately.",
                      know=["Your team is shrinking, decision by decision.", "Questions are treated as disloyalty.", "Nobody in the room speaks for you."],
                      do=["Protect your people's work in writing.", "Find a sponsor who is in the room.", "Make your team's value visible in numbers.", "Decide whether this is still your place."],
                      avoid="The leak hunt: digging for who said what at the off-site. You'll get gossip and a reputation.",
                      next="If your team is being dismantled, look after your people first, then yourself."),
        ),
        mirror=dict(
            title="Do you make ghosts?",
            intro="Anyone with a bit of authority can make a ghost decision. Tick honestly.",
            signs=["You've announced a decision to people it affected without asking them first.", "You've used “it was decided” without saying by whom.", "You've made a team decision in a 1:1 with one person.",
                   "You've had a deck called FINAL that nobody else saw.", "You think consulting people slows things down."],
            cure="Before your next decision that affects others, ask two of them one question: “What would I be missing?” It takes ten minutes and saves weeks.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 21 October, 09:30. Marcus's office. Pip has three questions.",
            intro="The Calm Inquiry and the Implementation Seat: understand, then help shape it.",
            lines=[
                ("Pip", "Marcus, I know you weren't at the off-site either. Do we know what problem the move solves?"),
                ("Marcus", "Benedict thinks Strategy needs its own analysts. They keep waiting for our numbers."),
                ("Pip", "That's fair, actually. What's fixed, and what's still open?"),
                ("Marcus", "The move's fixed. Who moves, and how, isn't."),
                ("Pip", "Then I'd like to be on the transition team. I know where the data and the gotchas are. And could we ask to join for twenty minutes next time Grid Analytics comes up?"),
                ("Marcus", "…That's a much better email than the one the team wanted to send."),
                ("", "Pip joins the transition team. In Act III he moves to Strategy with the work, on terms he helped write."),
            ],
            note="The decision didn't change. Pip's place in it did. That's usually the win available.",
        ),
    ),
    # ------------------------------------------------------------------ the Rumour Mill Familiar
    "rumour-mill-familiar": dict(
        sighting=f"""{beat("Wednesday 22 October · 09:10 · the kitchen")}
<p>Pip mentioned to one person that Marcus had “looked stressed after the budget meeting”. Just that. Seven words.</p>
{beat("11:30 · Customer Ops")}
<p>Customer Ops believed Grid Planning was being shut down. The version that reached them included “Marcus is
devastated” and “they're moving everyone to Strategy”.</p>
{beat("13:00 · lunch")}
<p>Two people asked Pip whether he was being made redundant. One offered him a hug. He accepted it, confused.</p>
{beat("15:00 · Marcus's office")}
<p>Marcus had heard that Pip was spreading rumours about him. He was very kind about it, which was worse. Marcus had,
in fact, been stressed because the coffee machine on floor 9 was broken.</p>
{note("A rumour needs three things: an anxious audience, a silent leadership, and you, saying “I probably shouldn't say this, but…”. Remove yourself from the recipe.")}""",
        origin=dict(
            title="How the grapevine became MetroVolt's real news service",
            beats=[
                ("2017 · the layoffs", "MetroVolt cuts 300 jobs. Staff learn about it from a newspaper website, two hours before the internal email. Trust in official channels collapses in an afternoon."),
                ("2018 · the replacement", "If the news won't come from the top, people find it themselves: the kitchen, the smoking area, private chats with names like <i>the real team</i>. Tamsin on floor 27 becomes the unofficial news desk (though she says almost nothing)."),
                ("2019 to 2024 · faster than email", "The grapevine is often right, and always faster. Leadership responds by saying even less, which makes the grapevine stronger."),
                ("2025 · the familiar", "Every budget season the Familiar wakes up, hungry. It feeds on silence and half-sentences. Seven words about a stressed manager become a department closure by lunchtime."),
            ],
            turning="The day staff read about their own layoffs in the newspaper, and decided never again to rely on official news.",
            saved="Leaders who shared what they knew early, and said what they didn't. Silence is the Familiar's food.",
            note="The grapevine isn't the problem. It's the symptom of leadership silence. You can't fix the silence, but you can stop feeding the symptom.",
        ),
        know=f"""<p>The rumour mill grows in the dark: <b>uncertainty plus silence from leadership</b>. People fill gaps with
guesses, and guesses travel faster than facts because they're more interesting. The grapevine is also genuinely useful:
it often knows things weeks before the announcement. The skill is to <b>listen without feeding it</b>.</p>
<h3 class="kh">What it wants</h3>
<p>Certainty. People repeat rumours to make sense of an anxious situation, and to feel included.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt's leaders say little until everything is final, and staff stopped trusting official news in 2017.
Every silence is filled with the most interesting available guess.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Facts, shared early.</li><li>Leaders who say “here's what I don't know yet”.</li><li>People who answer “I'll wait to hear it from my manager”.</li><li>Direct questions to the person concerned.</li></ul>
<h3 class="kh">Three kinds of rumour</h3>
<div class="breeds">
<div><b>The Gossip</b><p>About people. Never repeat it.</p></div>
<div><b>The Signal</b><p>An early warning about real change. Listen, check, prepare quietly.</p></div>
<div><b>The Weaponised</b><p>Planted to hurt someone. Never touch it; protect the target.</p></div>
</div>
{note("Hear everything. Repeat nothing you couldn't sign.")}""",
        difficulty=dict(
            normal=dict(who="An anxious week. Rumours, but no harm.",
                        know=["There's real uncertainty (budget, reorg).", "Rumours are about change, not people.", "Leaders are quiet but not hostile."],
                        do=["Listen; treat rumours as weak signals.", "Don't repeat them.", "Ask your manager directly what they know."],
                        avoid="Feeding the Familiar to seem interesting. You become the source.",
                        next="If the grapevine is faster than every official channel, you're at Nightmare."),
            nightmare=dict(who="The grapevine runs the building.",
                           know=["People believe the private chats over official emails.", "Rumours get personal.", "Leaders are silent for weeks."],
                           do=["Build a few trusted sources and check before acting.", "Use the Rumour Filter before repeating anything.", "If you lead people, run weekly fact updates, even “nothing new”.", "Correct personal rumours kindly when you hear them."],
                           avoid="The total denial: ignoring the grapevine. You'll be the last to know what matters.",
                           next="If rumours are being planted about people, you're at Hell."),
            hell=dict(who="Rumours are weaponised: stories planted about rivals.",
                      know=["Rumours target specific people.", "They appear before key decisions.", "The stories are traceable to someone who benefits."],
                      do=["Keep your own conduct spotless.", "Talk directly to the people a rumour is about.", "Keep a record if you're targeted.", "Raise planted rumours with HR if they're harming someone."],
                      avoid="The strategic leak. It's traceable, unethical, and it's how careers end quietly.",
                      next="If you're the target, document it and talk to your manager or HR early."),
        ),
        mirror=dict(
            title="Do you feed the Familiar?",
            intro="Everyone has, at some point. Tick honestly.",
            signs=["You've said “I probably shouldn't say this, but…” this month.", "You've passed on something you hadn't checked.", "You've repeated something about a person you wouldn't say to their face.",
                   "You enjoy being the one who knows first.", "You've heard your own words come back, changed."],
            cure="Before you repeat anything, ask: do I know it, would I say it with them here, and does repeating it help anyone? If not, let it end with you.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 22 October, 15:05. Marcus's office. Pip owns it.",
            intro="Owning a rumour you started: first, directly, briefly.",
            lines=[
                ("Pip", "Marcus, I said something careless this morning and it grew. I said you looked stressed after the budget meeting. That's all I said. I'm sorry."),
                ("Marcus", "Ah. I heard I was devastated and the department was closing."),
                ("Pip", "That's how it came back to me too. Do you want me to correct it with anyone?"),
                ("Marcus", "No, I'll send the team a short note. Honestly, I should have said something after the budget meeting. People are anxious."),
                ("Pip", "What can you tell us?"),
                ("Marcus", "That budgets are being reviewed, we don't know the outcome, and I'll update everyone Friday, either way."),
                ("", "Friday: Marcus sends a four-line update. The kitchen goes quiet for the first time in a week."),
            ],
            note="Two things killed this rumour: Pip owning his part fast, and Marcus filling the silence with facts. You can do the first one every time.",
        ),
    ),
    # ------------------------------------------------------------------ the CC Inquisition
    "cc-inquisition": dict(
        sighting=f"""{beat("Monday 27 October · 10:02 · a simple question")}
<p>Pip asked Gareth's team a question about one column in the asset data: did “in service date” mean install date or
commissioning date?</p>
{beat("10:41 · the reply")}
<p>Gareth replied, copying Pip's manager, his own director and Lord Varnish: <i>“Looping in leadership for visibility,
as this seems to be a recurring misunderstanding.”</i> It was not recurring. It was the first time.</p>
{beat("Monday to Thursday · the thread")}
<p>Pip replied to all, explaining at length. Gareth replied to all, at greater length. Others joined “for awareness”. By
Thursday there were fourteen people on a thread about one spreadsheet column.</p>
{beat("Friday 31 October · 16:58")}
<p>Lord Varnish replied with a single line: <i>“Can we take this offline?”</i> which, at MetroVolt, means “you have both
embarrassed me”.</p>
{note("BCC is the single most dangerous button in Outlook. Someone always replies-all from the BCC line. Always.")}""",
        origin=dict(
            title="How Gareth learned to copy everyone",
            beats=[
                ("2018 · the warning", "Gareth, then an asset engineer, spots a failing cable joint. He emails one person in Network Operations. That person is on leave. The email sits unread."),
                ("2018 · the outage", "The joint fails. Twelve thousand homes lose power for a night. The review asks why nobody warned anyone. Gareth's email is found, but only one person had received it, so the review says the warning was “not escalated appropriately”."),
                ("2019 onwards · the armour", "Gareth never sends an important email to one person again. He copies managers, directors, anyone who might later ask “why wasn't I told?” It's armour, not aggression."),
                ("2025 · the habit", "The armour is now on every email, even about spreadsheet columns. To others it looks like escalation. To Gareth it looks like safety."),
            ],
            turning="An outage where a warning existed but only one person had seen it, and the blame landed on the person who wrote it.",
            saved="A shared risk log in 2018, so warnings went somewhere visible instead of into one inbox.",
            note="Most compulsive CC-ers were burned once by a warning nobody saw. Give them a shared place to put things, and the CC line often shrinks.",
        ),
        know=f"""<p>The CC line is <b>power made visible</b>. Adding someone's boss turns a question into an escalation. Adding your
own boss says “I have a witness”. BCC says “I'm showing someone this behind your back”. Reply-all on a dispute turns a
disagreement into theatre.</p>
<h3 class="kh">What it wants</h3>
<p>Cover. Most CC escalations come from anxiety, not malice: people want proof that they told someone.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt reviews ask “who was told?” after every incident, so people over-tell. And because copying a
manager costs one click, while walking over costs five minutes and some courage.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>A phone call.</li><li>A short, generous resolution email to the same audience.</li><li>Shared logs that make CC armour unnecessary.</li><li>Being asked, kindly, “shall we sort this between us?”</li></ul>
<h3 class="kh">Three kinds of CC</h3>
<div class="breeds">
<div><b>The Armourer</b><p>Copies people for cover. Calm down the thread; give them a log.</p></div>
<div><b>The Escalator</b><p>Copies your boss to pressure you. Call them; solve it.</p></div>
<div><b>The Audience Builder</b><p>Copies everyone to perform. Take the show off the stage.</p></div>
</div>
{note("Fourteen people on a thread is not a discussion. It's a crowd watching a fight.")}""",
        difficulty=dict(
            normal=dict(who="The Armourer. An anxious colleague copying managers for cover.",
                        know=["It's their habit with everyone.", "The tone is defensive, not aggressive.", "They're friendly on the phone."],
                        do=["Call them and solve it.", "Send one short resolution email to the same audience, crediting them.", "Copy only who needs to act on your own emails."],
                        avoid="The essay of righteousness: a long reply-all proving you were right.",
                        next="If CC escalation is the house style, you're at Nightmare."),
            nightmare=dict(who="The Escalator. CC wars are how teams fight.",
                           know=["Every disagreement gets managers copied.", "Threads reach ten people regularly.", "Your manager is tired of being copied."],
                           do=["Move disputes off email within one reply.", "Start new, smaller threads for escalations.", "Agree with your manager how you'll handle CC'd disputes.", "Propose a shared log for warnings and decisions."],
                           avoid="The counter-escalation: copying even more senior people back.",
                           next="If someone is building a case against you in CC lines, you're at Hell."),
            hell=dict(who="Someone using CC lines to build a case against you.",
                      know=["Your mistakes are copied to senior people.", "Your good work isn't.", "HR appears on threads."],
                      do=["Stay factual, short and calm on every reply.", "Keep copies.", "Brief your manager before the threads reach them.", "If it's targeted, raise it formally."],
                      avoid="The BCC snare: secretly showing your boss their behaviour. One reply-all and you're the snake.",
                      next="If it continues, treat it as a conduct issue and take it to HR with your copies."),
        ),
        mirror=dict(
            title="Are you an Inquisitor?",
            intro="Check your sent items. Tick honestly.",
            signs=["You've copied someone's manager on a first, small issue.", "You've used “for visibility” or “looping in” this month.", "You've used BCC to show someone a conversation.",
                   "You've replied-all to a disagreement.", "Your average email has more than five people on it."],
            cure="On your next five emails, remove everyone who doesn't need to act. And when something heats up, pick up the phone before you pick up the CC line.",
        ),
        rehearsal=dict(
            title="Scene: Monday 27 October, 10:45. Pip calls instead of replying.",
            intro="The Phone Exorcism, then the Clean Report.",
            lines=[
                ("Pip", "Gareth, it's Pip. Rather than fill everyone's inbox, can we sort the asset question in five minutes?"),
                ("Gareth", "…Sure. Look, it's commissioning date. We've had people get it wrong before and it caused problems."),
                ("Pip", "Makes sense. Thanks, that's all I needed. I'll send a quick note to everyone you copied so they know it's sorted."),
                ("Gareth", "Fine. Good."),
                ("", "10:52. To all fourteen: “Gareth and I spoke. ‘In service date’ is the commissioning date. I'll update the model by Thursday. Thanks Gareth for the quick help.”"),
                ("", "Lord Varnish replies with a thumbs-up. It is the shortest thread in MetroVolt history."),
            ],
            note="The resolution went to the same audience as the escalation. That's what turns a public fight into a public fix.",
        ),
    ),
    # ------------------------------------------------------------------ the Turf Wars
    "turf-wars": dict(
        sighting=f"""{beat("Monday 3 November · the spreadsheet")}
<p>While checking forecast data, Pip found 11,400 smart meters that had stopped reporting. On average they had been
silent for 63 days. Their customers were getting estimated bills.</p>
{beat("Tuesday to Friday · four slides")}
<p>Pip asked who owned the problem. Grid Planning said it was a Customer Ops problem (customers complained). Customer Ops
said it was a Network Assets problem (the meters were broken). Network Assets said it was a Lumen problem (the project
installed them). Lumen said it was a Grid Planning problem (it was data). Each department produced a slide proving it
was someone else's.</p>
{beat("Monday 10 November · the tickets")}
<p>Pip looked at the ticket system. The problem had been opened as a ticket 37 times since August. Each ticket had been
reassigned between the four teams an average of five times, then closed as “not our remit”.</p>
{beat("That week")}
<p>2,100 customers complained about estimated bills. One of them was Pip's aunt.</p>
{note("Nothing ends a turf war like a number with a currency sign next to it, and a newspaper headline next to that.")}""",
        origin=dict(
            title="How four departments built a no-man's-land",
            beats=[
                ("2021 · the restructure", "MetroVolt reorganises into clear departments, each with its own target: complaints for Customer Ops, uptime for Network Assets, install schedule for Lumen, forecast accuracy for Grid Planning."),
                ("2022 · the budgets", "Budgets become fixed per department. Every hour spent on someone else's target is an hour stolen from your own. Helping becomes expensive."),
                ("2023 · the gap", "Problems that touch several targets belong to nobody. Fixing them costs your budget and improves someone else's number. Owning them is pure cost and possible blame."),
                ("2025 · the war", "Each department is behaving perfectly rationally. Together they've built a no-man's-land, and 11,400 customers are living in it."),
            ],
            turning="The day every department got its own target and its own budget, and nobody got the space between them.",
            saved="One shared target (say, customer complaints) across all four departments. Or a leader above them who owned the gaps.",
            note="Turf wars are usually a design problem, not a people problem. That's why the fix is a shared number and a shared owner, not a fight.",
        ),
        know=f"""<p>Turf wars happen when <b>ownership is unclear</b> and <b>incentives differ</b>: each department is measured on
its own targets, so a shared problem is pure cost. You can't settle a turf war from the middle, but you can make the
<b>customer problem impossible to ignore</b>, and offer a way for both towers to win.</p>
<h3 class="kh">What each tower wants</h3>
<p>To hit its own target, protect its own budget, and not be blamed for the problem in the gap.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because MetroVolt measures departments separately and rewards them separately. The gap has no target, no budget and
no owner. Rational departments leave it alone.</p>
<h3 class="kh">What ends it</h3>
<ul class="fears"><li>A customer number with a cost on it.</li><li>A small, time-boxed joint fix.</li><li>A leader above both towers who has to decide.</li><li>Shared credit.</li></ul>
<h3 class="kh">Three kinds of turf</h3>
<div class="breeds">
<div><b>The Orphan</b><p>Nobody's problem. Needs a number and an owner.</p></div>
<div><b>The Hot Potato</b><p>Passed around fast. Needs a joint fix nobody can pass.</p></div>
<div><b>The Land Dispute</b><p>Everybody wants it (budget, status). Needs a decision from above both.</p></div>
</div>
{note("In a turf war, the only safe flag to wave is the customer's.")}""",
        difficulty=dict(
            normal=dict(who="The Orphan. Two teams who've simply never talked.",
                        know=["Nobody has a strong position.", "The teams are friendly.", "It's a new problem."],
                        do=["Get both teams in one room with the customer data.", "Agree a named person each.", "Report the fix to both leads, crediting both."],
                        avoid="Picking a tower to blame.",
                        next="If it's a long-running rivalry, you're at Nightmare."),
            nightmare=dict(who="The Hot Potato. A long-running rivalry over a shared problem.",
                           know=["Each side has a slide blaming the other.", "Tickets bounce between teams.", "Customers are suffering in the gap."],
                           do=["Frame it as a Shared Wound: customers and cost, with numbers.", "Propose a small Joint Pact: one person each, four weeks.", "Keep it small enough to say yes to.", "Give both leaders equal credit."],
                           avoid="The land grab: quietly taking over the area to build your own empire.",
                           next="If the leaders above both towers are rivals too, you're at Hell."),
            hell=dict(who="The Land Dispute, all the way up.",
                      know=["The directors above both towers are rivals.", "Joint fixes are refused on principle.", "The problem is reaching the press or the regulator."],
                      do=["Write the Orphan Problem Brief with numbers.", "Take it to the first leader above both (often the chief of staff).", "Ask for a decision on an owner by a date.", "Keep a record of the cost of delay."],
                      avoid="The sigh and shrug. The customers in the gap disagree.",
                      next="If nobody will own it, the regulator eventually will. Make sure your brief is on record."),
        ),
        mirror=dict(
            title="Are you defending a tower?",
            intro="Departments are made of people. Tick honestly.",
            signs=["You've said “that's not our remit” this month.", "You've reassigned a ticket without talking to anyone.", "You have a slide about why a problem is someone else's.",
                   "You know of a customer problem nobody owns, and you've done nothing.", "You'd rather a problem stay unsolved than be solved by another team."],
            cure="Next time something lands in the gap, ask “what would it take to fix this together?” before “whose is it?”",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 12 November, 14:00. Room 9C. Priya and Gareth, together for the first time.",
            intro="The Shared Wound and the Joint Pact: customers first, small ask, both towers win.",
            lines=[
                ("Pip", "Thanks for coming. One slide: 11,400 meters, 63 days silent, 2,100 complaints, about £1.2 million in disputed bills."),
                ("Gareth", "The hardware's fine. It's a data issue."),
                ("Priya", "My agents can't tell which customers to call back."),
                ("Pip", "I don't think it matters whose it is yet. Could each of you lend one person for four weeks? I'll run the data side. We report back to you both."),
                ("Priya", "…Four weeks. One person. Fine."),
                ("Gareth", "Fine. But the report says Network Assets helped."),
                ("Pip", "It'll say both teams fixed it. Because you will have."),
            ],
            note="Pip never decided whose problem it was. He made it small enough, and shared enough, that nobody needed to win the argument.",
        ),
    ),
    # ------------------------------------------------------------------ the Empire Builder
    "empire-builder": dict(
        sighting=f"""{beat("January 2024 · forty people")}
<p>Gareth Pound began 2024 with 40 people in Network Assets, one deputy and one slide titled <i>Our Purpose</i>.</p>
{beat("Autumn 2026 · 112 people")}
<p>By autumn he had 112, a “Centre of Excellence for Asset Intelligence”, two deputies and a slide titled <i>Our
Expanding Footprint</i>, in which the footprint was drawn as a map with his department's colour spreading across it.</p>
{beat("Meanwhile · the data")}
<p>Asset data quality had not improved. It had, in fact, got worse: there were now three teams cleaning it, each in a
different way, and the CEO's dashboard showed three different counts of transformers.</p>
{beat("Tuesday 18 November · the proposal")}
<p>Gareth proposed absorbing Grid Planning's data work. “Synergies,” he explained. Pip asked which problem it would
solve. Gareth looked at him as a dragon looks at someone asking why it needs so much gold.</p>
{note("A centre of excellence is a team that has not yet been asked what it's excellent at.")}""",
        origin=dict(
            title="How a small team leader became the Empire Builder",
            beats=[
                ("2015 · a team of six", "Gareth leads six asset engineers. They're good. They're also small, and in the 2015 reorg small teams are merged away. Gareth's team survives by one vote."),
                ("2017 · the lesson repeated", "In the layoffs, the departments with the most people lose the smallest share. Size, Gareth notices, is safety."),
                ("2021 · the restructure", "Department heads are given status by headcount and budget. Gareth's title, pay band and seat at the table all depend on how big Network Assets is."),
                ("2024 onwards · the hoard", "Gareth grows the department relentlessly. Each new team makes him safer and more important. Whether it makes asset data better is a question nobody asks him."),
            ],
            turning="Surviving a reorg by one vote, and concluding that the only safe team is a big one.",
            saved="A company that measured departments on outcomes rather than size, and didn't punish small, excellent teams in every reorg.",
            note="Empire builders are often frightened people. Size feels like armour. Offer them a different kind (outcomes they can show) and some will put the gold down.",
        ),
        know=f"""<p>In many companies, <b>size is status</b>: bigger teams mean bigger titles, bigger budgets and a louder voice.
Empire builders aren't always bad managers; some genuinely believe in their area. The test is simple: <b>does the empire
produce better outcomes, or just more empire?</b></p>
<h3 class="kh">What it wants</h3>
<p>Safety, status and a seat at the top table. Headcount delivers all three at MetroVolt.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because pay bands and influence are tied to team size, and reorgs punish small teams. Proposals to “consolidate” sound
efficient. Nobody measures what happens after the consolidation.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Questions about outcomes.</li><li>Budget owners spotting duplication.</li><li>Service offers that keep work where it is.</li><li>Results that can't be absorbed.</li></ul>
<h3 class="kh">Three kinds of empire</h3>
<div class="breeds">
<div><b>The Believer</b><p>Really thinks centralising is better. Responds to outcome evidence.</p></div>
<div><b>The Fortress Builder</b><p>Grows for safety. Responds to a different kind of security.</p></div>
<div><b>The Status Collector</b><p>Grows for status. Needs finance and leadership to ask hard questions.</p></div>
</div>
{note("Ask a dragon what the gold is for. It hates that.")}""",
        difficulty=dict(
            normal=dict(who="The Believer. An ambitious manager with a genuine idea.",
                        know=["Their proposal names a real problem.", "They welcome questions.", "They'll agree to measures."],
                        do=["Ask the Outcome Question: what will be better, by when?", "Agree measures together.", "Support it if the case holds."],
                        avoid="Opposing everything they propose on principle.",
                        next="If work keeps flowing to them without results, you're at Nightmare."),
            nightmare=dict(who="The Fortress Builder. They're winning, and nothing's improving.",
                           know=["Every problem is solved by moving it into their team.", "Their slides show headcount, not results.", "Work is being duplicated."],
                           do=["Offer a service instead of a takeover.", "Track and publish outcomes, theirs and yours.", "Show finance the duplication.", "Use the Outcome Test on every proposal."],
                           avoid="The rival empire: building your own to fight theirs.",
                           next="If leadership rewards size above all, you're at Hell."),
            hell=dict(who="The Status Collector, rewarded from the top.",
                      know=["Size is explicitly rewarded.", "Your team is next on their list.", "Leadership loves consolidation slides."],
                      do=["Protect your team's core work in writing.", "Build a reputation on results that can't be absorbed.", "Make allies in finance.", "Help your people stay visible."],
                      avoid="The sabotage hoard: withholding data so their team fails. They'll fail loudly, and point at you.",
                      next="If your team is absorbed anyway, negotiate the terms (see the Ghost Decision)."),
        ),
        mirror=dict(
            title="Are you building an empire?",
            intro="It starts small. Tick honestly.",
            signs=["You've asked for headcount without saying what would improve.", "You've proposed moving work into your team “for synergies”.", "Your slides show your team's size.",
                   "You feel safer with a bigger team.", "You've never proposed giving work away."],
            cure="Next time you want more people, write the case in outcomes only: what will be better, by how much, by when. If you can't, you don't need them yet.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 18 November, the proposal meeting. Pip asks the question.",
            intro="The Outcome Question and the Service Offer: polite, specific, and an alternative they can accept.",
            lines=[
                ("Gareth", "Moving Grid Planning's data work into Network Assets gives us synergies across the asset estate."),
                ("Pip", "That could be good. What will be measurably better in six months, and how will we know?"),
                ("Gareth", "Data quality, obviously."),
                ("Pip", "Great. Today three teams count transformers differently. Would success be one count, agreed by March?"),
                ("Gareth", "…Something like that."),
                ("Pip", "What if we keep the model where it is, and give your team a weekly feed with an agreed quality bar? You'd get the single count without the move."),
                ("", "Benedict, chairing, says: “Let's try the feed first and review in March.” Gareth agrees. In March, there is one count."),
            ],
            note="Pip didn't fight the dragon. He asked what the gold was for, then offered a cheaper way to get it.",
        ),
    ),
    # ------------------------------------------------------------------ the Ring-Kissing Ritual
    "ring-kissing-ritual": dict(
        sighting=f"""{beat("Every Monday · 09:00 · the leadership stand-up")}
<p>Dorian opened with praise for Lord Varnish. “Great point in your email.” “Love how you framed that.” “As you said
last week…” Lord Varnish glowed. Dorian got the good projects. This had been going on for two years.</p>
{beat("Monday 1 December · 09:03")}
<p>Pip tried it once. “Great framing, Lord— er, Simon.” It came out like a man reading a hostage statement. Lord Varnish
looked at him with mild alarm and asked if he was feeling all right.</p>
{beat("09:40 · the corridor")}
<p>Marcus took Pip aside. “Don't do that,” he said gently. “It doesn't suit you. Just be useful to him. It lasts longer.”</p>
{beat("Friday 5 December")}
<p>Pip sent Lord Varnish a two-line heads-up: the meter numbers would look bad at Monday's board, here's why, here's the
fix. Lord Varnish replied in four minutes: <i>“Thank you. Nobody tells me these things.”</i> Dorian had flattered him for
two years. Nobody had told him things.</p>
{note("Kissing up: making the boss feel good. Managing up: making the boss do well. The first gets you noticed. The second gets you trusted. Trusted lasts.")}""",
        origin=dict(
            title="How the ritual began on floor 27",
            beats=[
                ("2022 · passed over", "Lord Varnish is a candidate for CEO. The parent group chooses Dame Helena instead. He is told he “lacks presence”. He takes it very hard, and tells no one."),
                ("2022 · the wound", "From then on, Simon Varnish is quietly insecure. He needs to feel that his ideas are good and that he is respected. Nobody at MetroVolt knows this. Dorian notices."),
                ("2023 · the courtier", "Dorian starts every meeting with praise. Simon visibly relaxes. Dorian's projects get approved faster. Others notice, and copy."),
                ("2025 · the court", "Floor 27 now runs on a daily ritual of praise. Bad news never reaches the top, because nobody wants to be the one who breaks the spell. Simon is surrounded by agreement and starved of information."),
            ],
            turning="A senior man who was told he wasn't good enough, and a junior who found out that soothing that wound was the fastest route up.",
            saved="One honest adviser who was also kind. Leaders who are insecure need truth delivered gently, not flattery delivered daily.",
            note="Behind most rings that get kissed is a leader who doesn't feel secure. That's why honest, respectful help works better than flattery: it's what they actually lack.",
        ),
        know=f"""<p>Flattery works because <b>leaders are human</b>: insecure, under pressure, and rarely praised. But it has a
short shelf life and a long cost: peers resent it, and the leader learns nothing true from you. <b>Managing up</b> is
different: you understand your boss's goals and pressures, and help them succeed, honestly.</p>
<h3 class="kh">What the ring-wearer wants</h3>
<p>Reassurance that they're doing well, and no nasty surprises. Flattery gives the first. Only honesty gives the second.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because promotions on floor 27 depend on one man's opinion, and that man is insecure. Praise is the fastest way to
his good mood. Bad news has no reward.</p>
<h3 class="kh">What the courtiers fear</h3>
<ul class="fears"><li>Someone who brings bad news early and is thanked for it.</li><li>Results that speak for themselves.</li><li>The leader noticing he's been told nothing true.</li><li>Specific, honest praise, which makes theirs look cheap.</li></ul>
<h3 class="kh">Three kinds of courtier</h3>
<div class="breeds">
<div><b>The Flatterer</b><p>Constant, vague praise. Gets noticed, isn't trusted.</p></div>
<div><b>The Mirror</b><p>Agrees with everything. Blamed when the idea fails.</p></div>
<div><b>The Honest Adviser</b><p>Specific praise, early warnings, kind truth. Becomes indispensable.</p></div>
</div>
{note("Kiss the ring and you'll get a seat. Help the king and you'll get a voice.")}""",
        difficulty=dict(
            normal=dict(who="A boss who likes praise but values results.",
                        know=["Good work still gets noticed.", "Honest feedback is accepted.", "Flatterers don't always win."],
                        do=["Learn their goals and make your work serve them.", "Praise specifically, when it's true.", "Bring bad news early, with a fix."],
                        avoid="The full prostration: agreeing with everything. When the idea fails, you said “brilliant”.",
                        next="If flatterers are clearly winning, you're at Nightmare."),
            nightmare=dict(who="A court where flatterers win.",
                           know=["The same courtiers get the good projects.", "Bad news never reaches the top.", "Honest people stay quiet."],
                           do=["Keep delivering and make results visible.", "Become the person who tells the truth kindly.", "Use the Manage-Up Card to aim your work at their real goals.", "Build sponsors elsewhere too."],
                           avoid="The public grovelling: liking every one of the CEO's posts within four minutes.",
                           next="If honesty is punished, you're at Hell."),
            hell=dict(who="A court where only loyalty is rewarded, and honesty punished.",
                      know=["People who disagreed have been sidelined.", "Promotions follow flattery.", "You feel pressure to praise things you know are wrong."],
                      do=["Protect yourself; document your work.", "Find a sponsor outside this court.", "Speak up only on what truly matters.", "Ask whether you want to rise in this court at all."],
                      avoid="Kissing up, kicking down. The people below talk, eventually upwards.",
                      next="If staying requires you to lie, use the Escape Portal (Act III)."),
        ),
        mirror=dict(
            title="Are you kissing the ring?",
            intro="Everyone has flattered a boss once. Tick honestly.",
            signs=["You've said “great point” before they finished the point.", "You've praised a decision you privately thought was wrong.", "You've never brought your boss bad news first.",
                   "You treat people above you better than people below you.", "You like the CEO's posts on reflex."],
            cure="This month, give your boss one specific, true compliment and one early warning. Then notice which one they remember.",
        ),
        rehearsal=dict(
            title="Scene: Friday 5 December, 16:20. Pip sends Lord Varnish a message.",
            intro="The Honest Warning and the Specific Praise: what managing up actually sounds like.",
            lines=[
                ("Pip", "Simon, heads-up before Monday's board: the meter-failure numbers will look bad (11,400 silent). It's a data backlog, not new failures. The joint fix with Ops and Assets clears it by January."),
                ("Lord Varnish", "Thank you. Nobody tells me these things."),
                ("Pip", "Also, the way you framed Lumen as a billing fix last month got Finance on board. That made the joint fix possible."),
                ("Lord Varnish", "…That's kind. Could you brief me for ten minutes on Monday at 8:30?"),
                ("", "Monday 08:30. Pip briefs him. At the board, Lord Varnish explains the meter numbers before anyone asks. Dorian, who had planned to say “great point”, says nothing at all."),
            ],
            note="One warning and one true, specific compliment did more in a week than two years of “great point”.",
        ),
    ),
    # ------------------------------------------------------------------ the Chosen One
    "chosen-one": dict(
        sighting=f"""{beat("September · the board presentation")}
<p>Jules got the Lumen board presentation. Pip had built half the slides.</p>
{beat("October · the regulator")}
<p>Jules went to the regulator meeting in London. Pip found out from the photo on the intranet.</p>
{beat("November · the programme")}
<p>Jules was selected for the “high potential” programme, which nobody had told Pip existed. Every time Lord Varnish
needed someone, he said “ask Jules”.</p>
{beat("December · the worst part")}
<p>Jules was good. Kind, fast, clear. Pip couldn't even hate them properly. He tried once, for an afternoon, and Jules
brought him a coffee and asked how his model was going. It was exhausting.</p>
{note("Most favourites aren't chosen for being brilliant. They're chosen for being reliable in front of the person choosing. You can learn that.")}""",
        origin=dict(
            title="How Jules became the Chosen One",
            beats=[
                ("March 2023 · Lord Varnish's first big project", "Simon Varnish launches his first flagship at MetroVolt: a dashboard for the CEO. The night before the launch, it breaks."),
                ("March 2023 · 23:00", "Jules, then a junior analyst, happens to be working late, notices, and fixes it by 02:00. Nobody asked them to. The launch goes perfectly."),
                ("2023 onwards · “ask Jules”", "Simon never forgets. Jules becomes his safe pair of hands. Each success brings another chance; each chance brings another success. It compounds."),
                ("2025 · the circle", "Jules is genuinely good, but also simply first in line. Others, just as good, never got their 02:00 moment in front of the person who decides."),
            ],
            turning="One late night, in front of exactly the right person, at exactly the right time.",
            saved="Nothing here is a curse for Jules. For Pip, it's a lesson: favour often begins with being visibly reliable for the decider, once, when it counts.",
            note="Favouritism is usually not a plot. It's a leader's memory of who saved them. You can't manufacture that night, but you can make sure they know you're reliable too.",
        ),
        know=f"""<p>Favouritism is partly <b>human nature</b>: leaders trust people who are like them, who've succeeded before, or
who make their lives easier. Once someone is chosen, they get more chances, so they succeed more, so they get chosen
more. Sometimes it's unfair. Sometimes it's earned, and simply <b>more visible</b> than your work.</p>
<h3 class="kh">What the chooser wants</h3>
<p>Safety. A leader under pressure picks the person who won't let them down. It's a bet on certainty, not a judgement on everyone else.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because opportunities at MetroVolt are handed out informally, by one person's memory. There's no open process for the
board presentation or the regulator trip. Whoever is top of mind gets it.</p>
<h3 class="kh">What breaks the spell</h3>
<ul class="fears"><li>Asking, directly, for specific opportunities.</li><li>Your own visible, reliable results.</li><li>A sponsor of your own.</li><li>Open processes for opportunities.</li></ul>
<h3 class="kh">Three kinds of favourite</h3>
<div class="breeds">
<div><b>The Earned</b><p>Chosen for real reliability. Learn from them; ask for your turn.</p></div>
<div><b>The Mirror</b><p>Chosen for being like the boss. Build visibility beyond the boss.</p></div>
<div><b>The Convenient</b><p>Chosen for being nearby. Make yourself nearby, too.</p></div>
</div>
{note("Don't wait to be chosen. Ask to be considered. It's shocking how often that works.")}""",
        difficulty=dict(
            normal=dict(who="The Earned. A leader who leans on one reliable person.",
                        know=["The favourite is genuinely good.", "Your manager supports you when asked.", "Nobody has ever said no to you; you've never asked."],
                        do=["Ask what the favourite does that you could do more of.", "Ask for a specific opportunity, by name.", "Deliver it reliably and visibly."],
                        avoid="The copycat: imitating the favourite's style.",
                        next="If there's a clear inner circle you can't enter, you're at Nightmare."),
            nightmare=dict(who="An inner circle.",
                           know=["The same few names come up for everything.", "Opportunities are never advertised.", "Your direct asks get vague answers."],
                           do=["Find your own sponsor, in another part of the business.", "Build visibility beyond your manager.", "Keep asking for specific things, in writing.", "Keep delivering."],
                           avoid="The usurper's plot: undermining the favourite. You'll look bitter and the leader will protect their choice.",
                           next="If favouritism is tied to personal relationships or protected traits, you're at Hell."),
            hell=dict(who="Favouritism that's unfair, or discriminatory.",
                      know=["It affects pay or promotion.", "It follows personal relationships, not work.", "It seems linked to gender, age, background or similar."],
                      do=["Keep a factual record of opportunities and who got them.", "Raise it with HR or a formal channel.", "Get advice if it's discrimination.", "Look after yourself; this isn't a career tip, it's a fairness issue."],
                      avoid="The sulk: withdrawing to the minimum. It confirms the leader's choice.",
                      next="If the organisation won't address it, protect your career elsewhere."),
        ),
        mirror=dict(
            title="Do you play favourites?",
            intro="If you lead anyone, you probably do, a little. Tick honestly.",
            signs=["You give the same person most of the visible opportunities.", "You think of the same name first, every time.", "You've never advertised an opportunity within your team.",
                   "Some team members have never presented to your boss.", "You're more patient with people who remind you of yourself."],
            cure="Next time an opportunity comes up, ask: who hasn't had a turn? Give it to them, and back them. You'll find new favourites.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 11 December, Pip's 1:1 with Marcus.",
            intro="The Honest Mirror and the Direct Ask: specific, positive, about the future.",
            lines=[
                ("Pip", "Jules gets a lot of the visible work, and honestly, they're good. What would I need to show for you to put me forward too?"),
                ("Marcus", "Hm. Jules always tells Simon what's coming before he asks. You do great work, but he only hears about it from me."),
                ("Pip", "That's useful. Could I present the meter data at the January board?"),
                ("Marcus", "I'll ask. Send Simon a short heads-up before it, like you did last week. He liked that."),
                ("Pip", "And is the high-potential programme open to nominations?"),
                ("Marcus", "…I didn't know you wanted it. I'll nominate you for the next intake."),
            ],
            note="Marcus had never thought of Pip for these things. Not because he didn't rate him: because Pip had never asked.",
        ),
    ),
    # ------------------------------------------------------------------ the Sacrificial Lamb
    "sacrificial-lamb": dict(
        sighting=f"""{beat("Monday 17 November · 15:00 · floor 27")}
<p>Lord Varnish called Pip to floor 27 for the first time. There was coffee. There was warmth. There was a chair that
was more comfortable than Pip's own.</p>
{beat("15:05 · the offer")}
<p>There was <b>Project Orion</b>: a new billing integration, eighteen months late, £2.4 million over budget, already on
its third project lead. “It needs fresh eyes,” said Lord Varnish. “Real visibility for you. A great opportunity.”</p>
{beat("15:20")}
<p>Tamsin walked past the glass door with a folder and met Pip's eye for exactly one second. In that second, Pip learned
more than in the whole meeting.</p>
{beat("15:45 · the corridor")}
<p>Pip looked up Orion's previous leads on the intranet. The first had been “moved to a strategic role”. The second was
on long-term sick leave. The third had “left to pursue other opportunities”. Their photos were still on the project page,
smiling, like a memorial.</p>
{note("If you're offered a project with unusual warmth, read the project's obituary first. Ask who led it before you, and where they are now.")}""",
        origin=dict(
            title="How Project Orion became an altar",
            beats=[
                ("January 2024 · the promise", "To impress Dame Helena, Lord Varnish launches Orion: a new billing system in twelve months, for £3 million. Engineers say 24 months and £5 million. The engineers aren't in the room."),
                ("2024 · the first lead", "Lead #1 reports that the plan is impossible. She is moved to a “strategic role” within a month."),
                ("2025 · leads two and three", "Lead #2 tries to deliver the impossible and burns out. Lead #3 resets the plan honestly, which makes Lord Varnish look bad; he “leaves to pursue other opportunities”."),
                ("November 2026 · the fourth lamb", "Orion now needs someone junior, eager and new enough not to know the history. Someone who'll carry the old date and the old budget, and the blame. Someone like Pip."),
            ],
            turning="A promise made to impress a CEO, with the engineers out of the room, which nobody senior was ever willing to take back.",
            saved="Lord Varnish resetting the plan himself in 2024. One honest re-baseline would have saved three careers.",
            note="Sacrifices happen when a senior person can't admit a mistake. The cure is a reset in writing, with their name on it, not yours.",
        ),
        know=f"""<p>When a project is failing, leaders need someone to <b>own</b> it, and sometimes to <b>be blamed</b> for it. The task
goes to someone junior and eager, who can't refuse and won't know the history. Not every hard assignment is a trap. The
difference is in the <b>terms</b>: authority, resources, a reset plan, and a sponsor who'll stand next to you.</p>
<h3 class="kh">What the priests want</h3>
<p>Someone else's name on the failure, or a miracle. Ideally both: if it succeeds, it was their vision.</p>
<h3 class="kh">Why it thrives here</h3>
<p>Because admitting a project's original plan was wrong would embarrass its sponsor. It's cheaper, for them, to replace
the lead than the plan.</p>
<h3 class="kh">What protects the lamb</h3>
<ul class="fears"><li>Asking for time to understand before saying yes.</li><li>Talking to the previous leads.</li><li>A published baseline on day one.</li><li>Terms in writing, with the sponsor's name on them.</li></ul>
<h3 class="kh">Three kinds of offer</h3>
<div class="breeds">
<div><b>The Rescue</b><p>A hard project with a real sponsor. A genuine career chance, on the right terms.</p></div>
<div><b>The Scapegoat</b><p>A doomed project needing someone to blame. Decline, or demand written terms.</p></div>
<div><b>The Holding Pattern</b><p>Nobody expects success; they need a name on it until it's cancelled. Know which it is.</p></div>
</div>
{note("Before you pick up the knife, check whose neck the ceremony is for.")}""",
        difficulty=dict(
            normal=dict(who="The Rescue. A hard project with a real sponsor.",
                        know=["The sponsor will put terms in writing.", "Previous leads left for normal reasons.", "There's budget for a reset."],
                        do=["Ask for a few days to understand it.", "Agree the Terms of Sacrifice in writing.", "Publish the honest baseline on day one."],
                        avoid="The eager yes in the room.",
                        next="If the sponsor is vague and terms are dodged, you're at Nightmare."),
            nightmare=dict(who="A failing project with a vague sponsor.",
                           know=["Nobody can tell you the real date or budget.", "The sponsor says “let's not get bogged down in details”.", "Previous leads won't talk about it."],
                           do=["Talk to the previous leads before deciding.", "Insist on the baseline and terms in writing.", "Report honestly every fortnight.", "Copy your own manager on everything."],
                           avoid="The silent takeover: taking over without publishing the baseline. In six months the delay will be yours.",
                           next="If everyone knows it's a sacrifice but you, you're at Hell."),
            hell=dict(who="The Scapegoat. A political sacrifice.",
                      know=["Three leads have already gone.", "The sponsor won't put anything in writing.", "People look at you with pity."],
                      do=["Decline gracefully, with reasons.", "Or accept only with written terms and a sponsor who has something to lose.", "Keep a private, dated record.", "Line up allies before you start."],
                      avoid="The blame return: spending your time blaming previous leads in public.",
                      next="If you accepted and the terms are broken, raise it immediately, in writing, to your manager and the sponsor."),
        ),
        mirror=dict(
            title="Have you ever lit the candles?",
            intro="If you lead anything, you may have offered a lamb. Tick honestly.",
            signs=["You've handed a failing project to someone junior with “great opportunity”.", "You've kept a plan you knew was wrong to avoid admitting it.", "You've replaced a person instead of a plan.",
                   "You've praised someone's “fresh eyes” on something you'd given up on.", "You weren't in the room when the original promise was made, but you've defended it."],
            cure="If a plan is wrong, reset it yourself, publicly, with your name on the reset. It costs a bit of face. It saves people.",
        ),
        rehearsal=dict(
            title="Scene: Monday 17 November, 15:10. Floor 27. Lord Varnish has just made the offer.",
            intro="The Autopsy First and the Terms of Sacrifice: grateful, calm, and never yes in the room.",
            lines=[
                ("Lord Varnish", "So, Orion. Real visibility. What do you say?"),
                ("Pip", "I'm honoured, genuinely. Before I commit, could I spend a few days understanding where it stands? I want to do it properly."),
                ("Lord Varnish", "Of course, of course. But we need someone by the end of the month."),
                ("Pip", "Understood. If I take it on, I'd need a reset plan by mid-December for your sign-off, authority over scope, two engineers, and you as visible sponsor at the steering group. Could we agree that in writing?"),
                ("Lord Varnish", "…Let's discuss the details next week."),
                ("", "Pip spends Thursday with Orion's three previous leads. Friday, he sends the Terms of Sacrifice email. It is never answered. Pip declines, politely, with reasons. In January, Orion is quietly cancelled."),
            ],
            note="The unanswered email was the answer. Pip learned what he needed without becoming the fourth photo on the memorial page.",
        ),
    ),
    # ------------------------------------------------------------------ the Art of Plausible Silence
    "plausible-silence": dict(
        sighting=f"""{beat("Wednesday 26 November · 14:00 · the budget review")}
<p>Twelve managers, one CFO, one Lord Varnish. A slide titled <i>Efficiency Opportunities</i>, with nothing on it yet.</p>
{beat("14:22 · the question")}
<p>Lord Varnish asked the room: “Which team could give up 10% of its budget?” Gareth studied his pen. Priya looked at her
laptop. The CFO looked at the ceiling. The silence lasted four seconds, which in a budget review is about a week.</p>
{beat("14:22 · second five")}
<p>Pip, eager, filled it. “Grid Planning could probably find some savings in the—” He hadn't finished the sentence. The CFO
had already written it down.</p>
{beat("Friday 28 November")}
<p>Grid Planning's budget was 12% smaller. Marcus found out from Finance. He was very kind about it, which was somehow worse.</p>
{note("Juniors fill silences. Seniors let them sit. The person who speaks first in an awkward silence usually just volunteered for something.")}""",
        origin=dict(
            title="How MetroVolt's budget review became an auction",
            beats=[
                ("2019 · the voluntary rounds", "A new CFO introduces “voluntary savings rounds”: managers are asked, in the room, to offer cuts. The idea is to reward initiative."),
                ("2019 · the first volunteers", "The first managers who volunteer savings are thanked, and then cut further, because they've shown there was room. The silent ones keep their budgets."),
                ("2020 to 2024 · the lesson", "Every experienced manager learns the same thing: in a budget review, the first voice pays. Silence becomes a skill passed from manager to manager, quietly."),
                ("2025 · the newcomers", "Nobody tells juniors. They're invited “for development”, hear an open question, and answer it, because answering questions is what good employees do."),
            ],
            turning="A process that rewarded honesty with deeper cuts, and taught everyone that silence was the safest answer.",
            saved="A budget process based on data rather than volunteers. And a manager briefing Pip beforehand: “Don't commit anything in the room.”",
            note="Silence is often a learned response to a process that punishes candour. Learn the silence, but also notice the process.",
        ),
        know=f"""<p>In politics, <b>what you say is on record</b> and what you don't say mostly isn't. Every offhand remark can
become a commitment, a quote or a weapon. Experienced people pause, ask questions and say “let me come back to you” far
more than juniors do. It isn't evasion. It's <b>thinking before committing</b>.</p>
<p>Silence is not lying, and it's not cowardice. But if you know something serious (harm, fraud, danger), silence is wrong.</p>
<h3 class="kh">What the question wants</h3>
<p>A commitment. Open questions to a room are often designed to get someone to volunteer.</p>
<h3 class="kh">Why silence works here</h3>
<p>Because at MetroVolt, anything said in a senior meeting is written down and acted on. The first answer becomes the decision.</p>
<h3 class="kh">What silence protects</h3>
<ul class="fears"><li>Your team's resources.</li><li>Your manager's authority.</li><li>Your ability to give a considered answer.</li><li>You, from being quoted out of context.</li></ul>
<h3 class="kh">Three kinds of silence</h3>
<div class="breeds">
<div><b>The Thoughtful Pause</b><p>Three seconds to think. Always useful.</p></div>
<div><b>The Strategic Silence</b><p>Not volunteering what isn't yours to give. Often wise.</p></div>
<div><b>The Complicit Silence</b><p>Saying nothing about real harm. Never acceptable.</p></div>
</div>
{note("Silence can't be quoted. Use that, but never to hide harm.")}""",
        difficulty=dict(
            normal=dict(who="An eager habit of answering too fast.",
                        know=["You often fill silences.", "You've volunteered things you regretted.", "Nobody's punished you badly yet."],
                        do=["Count to three before answering loaded questions.", "Answer vague questions with a clarifying one.", "Practise the Time Charm."],
                        avoid="The stone wall: saying nothing, ever. You'll seem evasive or uninterested.",
                        next="If leadership fishes for commitments in public, you're at Nightmare."),
            nightmare=dict(who="Leadership fishes for commitments in public.",
                           know=["Open questions in meetings lead to cuts or extra work.", "Volunteers pay.", "Experienced people go quiet in certain meetings."],
                           do=["Use the Time Charm and the Manager's Seal every time.", "Agree with your manager beforehand what you can commit.", "Ask clarifying questions to slow the room down.", "Write down what you did and didn't agree to."],
                           avoid="The mysterious hint: implying you know more than you say. People will assume you're the leak.",
                           next="If anything you say is used against you, you're at Hell."),
            hell=dict(who="A culture where every word is a weapon.",
                      know=["Your remarks are quoted back out of context.", "Casual conversations end up in reviews.", "People speak only in writing, carefully."],
                      do=["Say less and write carefully.", "Save your voice for what matters most.", "Keep a record of what you said.", "Speak up on harm through proper channels, always."],
                      avoid="The silent witness: staying quiet about real wrongdoing to stay safe. That's not strategy, it's complicity.",
                      next="If you can't speak honestly about anything, it's time to look for a place where you can."),
        ),
        mirror=dict(
            title="Do you fill every silence?",
            intro="Or the opposite. Tick honestly.",
            signs=["You've volunteered your team's time or budget without asking your manager.", "You answer every question immediately.", "You feel physically uncomfortable in a pause.",
                   "You've later regretted something you said in a senior meeting.", "Or: you've stayed silent about something that was genuinely wrong."],
            cure="Practise the pause: three seconds, then a question or “let me come back to you”. And keep your voice for the moments that need it most.",
        ),
        rehearsal=dict(
            title="Scene: the next budget review, 14:22. The same question.",
            intro="The Held Pause, the Question Back, the Manager's Seal.",
            lines=[
                ("Lord Varnish", "Which team could give up 10% of its budget?"),
                ("", "Four seconds of silence. Pip counts them. He says nothing."),
                ("Lord Varnish", "Pip? Grid Planning?"),
                ("Pip", "Good question. When you say 10%, do you mean this year's budget or next year's plan?"),
                ("Lord Varnish", "Next year's."),
                ("Pip", "That's Marcus's call. I'll make sure he has the numbers by Friday, including where savings would hurt the forecast."),
                ("", "Friday: Marcus sends a one-page note. Grid Planning's budget is reduced by 3%, on terms Marcus chose. Marcus buys Pip a coffee."),
            ],
            note="Pip didn't refuse, evade or lie. He clarified, deferred to the right person and promised facts. That's plausible silence done well.",
        ),
    ),
}
