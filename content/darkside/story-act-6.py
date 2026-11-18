# Series 4 · Act VI · the long-form story fields, merged into content/darkside/act-6.py by scripts/grimoire.py.
# July 2028 to April 2029. GridSight, MetroVolt's data-services arm; Pip seconded as delivery lead, with Asha.
# Clients: Wexley Borough Council (Gavin Pike, Nadia Sesay), Brackenfield Water (Moira Venn, Hamish Grant),
# Northshire Combined Authority (Bernard Quill), Castellan Homes (Rex Dunmore). Rival: Corvid Analytics (Zara Okafor).
# Partner/rival: Northgate Energy (Theo Blake). MetroVolt's billing vendor: Halvorsen Systems (Sven Aldous).

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ the Client Demon
    "client-demon": dict(
        sighting=f"""{beat("Saturday 1 July 2028 · the first client")}
<p>GridSight signed its first contract: a heat-pump and EV-charging demand map for <b>Wexley Borough Council</b>, due 31
August. The client lead was Gavin Pike, Head of Sustainability. He was charming at the kick-off. He gave Pip his mobile
number “for anything at all” and asked for Pip's.</p>
{beat("Tuesday 18 July · 22:07")}
<p>Pip's phone lit up on the kitchen table. Gavin. A “quick thought” about adding social housing. Then again at 22:31,
about bus depots. Then at 22:58: “Sorry, last one!” It wasn't. The goals document was on version 11. The deadline was
still 31 August.</p>
{beat("Thursday 20 July · the Rhythm Rite")}
<p>Pip, who had not slept well, read this entry. He proposed a Tuesday call, a Friday written update, and same-working-day
replies to email. Gavin said “absolutely, great idea”, and rang the following Monday at 21:40. Pip didn't answer. He
replied at 08:30, warmly, with a Change Ledger. Gavin rang at 21:40 once more, the next week. Then stopped.</p>
{beat("Tuesday 1 August · the fear")}
<p>On the Tuesday call Pip asked what would happen if the map slipped. A long pause. Gavin had to present it to the full
council on 12 September, and Nadia Sesay, his director, had told him his budget depended on it. The 22:00 calls weren't
about the map. They were about Gavin's job.</p>
{note("Difficult clients are usually frightened clients. Find what they're frightened of and you'll find what they actually need.")}""",
        origin=dict(
            title="How Gavin became the Client Demon",
            beats=[
                ("2019 · the first consultants", "Wexley hires a big consultancy for its climate plan. £400k, 200 slides, nothing usable. Gavin, newly appointed, is blamed for the bill he didn't sign."),
                ("2022 · the lesson", "Gavin decides vendors only deliver when watched. He starts checking in daily on every contract. It works, a bit. He becomes known as thorough."),
                ("2027 · the squeeze", "Council budgets are cut. Nadia tells Gavin his team's survival depends on showing results by autumn 2028."),
                ("July 2028 · GridSight", "A new, small vendor, eager to please, gives him a mobile number. Every fear Gavin has finds a phone that answers."),
            ],
            turning="One bad vendor in 2019 taught Gavin that watching is the only safety. Budget cuts turned watching into haunting.",
            saved="A clear rhythm on day one, and someone asking, early, “What happens to you if this slips?”",
            note="The demon isn't the client. It's the client's fear, wearing the client's phone number.",
        ),
        know=f"""<p>A difficult client is usually a client under pressure, from their boss, their budget or their last bad vendor,
who's found that pushing you is the one thing they can control. They change goals because their own goals keep changing.
They call late because they're worrying late.</p>
<h3 class="kh">What it wants</h3>
<p>Certainty. Proof the project won't fail them. Usually, protection from someone above them.</p>
<h3 class="kh">Why it haunts</h3>
<p>Because nobody set a rhythm, so every worry becomes a call. And because you answered the first one.</p>
<h3 class="kh">What it fears</h3>
<ul class="fears"><li>Being blamed for another failed vendor.</li><li>Surprises.</li><li>Looking foolish in front of their boss.</li><li>Losing control of the timeline.</li></ul>
<h3 class="kh">Three kinds of client demon</h3>
<div class="breeds">
<div><b>The Worrier</b><p>Frightened, not cruel. A rhythm and regular written updates calm it.</p></div>
<div><b>The Shape-Shifter</b><p>Goals change weekly. The Change Ledger makes the cost visible.</p></div>
<div><b>The Tyrant</b><p>Abusive, contemptuous, never satisfied. If it won't change, see Banishing a Client.</p></div>
</div>
{note("Most clients are Worriers. Treat a Worrier like a Tyrant and you'll create one.")}""",
        difficulty=dict(
            normal=dict(who="The Worrier.",
                        know=["They call often but they're polite.", "Their worry has a clear cause.", "They respond well to updates."],
                        do=["Set the Rhythm Rite in week one.", "Send a written update every Friday, even if nothing changed.", "Ask what they're worried about."],
                        avoid="Answering every late call.",
                        next="If the goals keep changing, you're at Nightmare."),
            nightmare=dict(who="The Shape-Shifter.",
                           know=["The goals change every week.", "The deadline never moves.", "Nothing is written down."],
                           do=["Start the Change Ledger today.", "Send it after every call.", "Ask them to choose: date, scope or cost.", "Tell your boss early."],
                           avoid="The silent absorb.",
                           next="If they become abusive, you're at Hell."),
            hell=dict(who="The Tyrant.",
                      know=["They're rude, especially to junior staff.", "Nothing is ever good enough.", "They threaten to leave, or to escalate, often."],
                      do=["Document every incident.", "Involve your boss and theirs.", "Protect your team: take their calls yourself.", "Read Banishing a Client."],
                      avoid="Sacrificing your team to keep them.",
                      next="If it doesn't change after a clear warning, banish."),
        ),
        mirror=dict(
            title="Are you the Client Demon?",
            intro="You probably are a client to someone: a vendor, an agency, another team. Tick honestly.",
            signs=["You've emailed or called a supplier after 21:00 about something non-urgent.", "Your requirements have changed since you signed, and you haven't asked what that costs.",
                   "You've never told a vendor what's really driving your deadline.", "You've threatened to “take this higher” before talking to their manager.",
                   "You think vendors only work when watched."],
            cure="Tell your vendor what you're worried about. One honest sentence about your real deadline saves weeks of late-night calls.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 1 August 2028, the weekly call with Gavin.",
            intro="The Fear Finder, then the Change Ledger.",
            lines=[
                ("Pip", "Before the updates, can I ask: what happens on your side if this slips?"),
                ("Gavin", "…I present to full council on the twelfth of September. Nadia's made it clear my budget rests on it."),
                ("Pip", "Thank you. That helps. Then let's make sure you have something great on the twelfth, even if not everything."),
                ("Gavin", "But I need the bus depots and social housing too."),
                ("Pip", "Then let's choose. Core map by 31 August for council. Depots and housing in phase two. I'll send it in writing today."),
                ("Gavin", "…Yes. That actually works. Sorry about the calls."),
            ],
            note="Gavin presented on 12 September. The council voted to fund phase two. He rang at 22:00 once more, to say thank you, and apologised for the time.",
        ),
    ),
    # ------------------------------------------------------------------ the Scope-Creep Swarm
    "scope-creep-swarm": dict(
        sighting=f"""{beat("August 2028 · the buzz")}
<p>Even with the Rhythm Rite, the additions kept coming, now politely, in writing, one at a time. “While you're at it,
could you add the school sites?” “Could you just colour the wards by deprivation?” “One small thing: could it work on an
iPad?”</p>
{beat("Friday 15 September · the count")}
<p>Asha, who had been quietly keeping a list, sent it to Pip: <b>twenty-three additions</b> since the contract was
signed. None more than two days' work. Together, thirty-one days. The project had been priced at forty.</p>
{beat("Monday 18 September · the reset")}
<p>Pip shared the Swarm Count with Gavin. Not as a complaint: as a table, with the original scope beside it. Gavin was
astonished. “I had no idea it was that much. Why didn't you say?” It was a fair question. Pip hadn't, because each one had
felt too small to mention.</p>
{beat("From October · the menu")}
<p>Every new request now came back with three options: in and later, instead of something, or in phase two. Gavin chose
phase two eleven times out of fourteen. He'd never been offered the choice before.</p>
{note("Scope creep isn't the client asking for too much. It's you never saying what anything costs.")}""",
        origin=dict(
            title="How the swarm was born",
            beats=[
                ("July 2028 · the eager vendor", "GridSight is new and wants a happy first client. Pip says yes to small things to build goodwill."),
                ("August · the habit", "Gavin learns that small requests are free. He's not greedy; he just has a long list and a vendor who never says “that costs”."),
                ("September · the plague", "Twenty-three small yeses, thirty-one days of work, a project nine days from overrun, and nobody had decided any of it."),
                ("The pattern everywhere", "Every project in history has died this way at least once. The swarm is not a client. It's the absence of a price."),
            ],
            turning="The first “sure, no problem” for something that was a problem, said to be nice.",
            saved="A change log from day one, and a trade-off menu offered with the very first “while you're at it”.",
            note="Goodwill isn't built by free work. It's built by delivering what you promised, on time.",
        ),
        know=f"""<p>Scope creep is the slow growth of a project through small, unpriced additions. Each one is reasonable. Together they
break the budget, the timeline and the team. The client rarely knows it's happening, because nobody told them.</p>
<h3 class="kh">What it wants</h3>
<p>More, because more is genuinely useful, and nobody has said it costs anything.</p>
<h3 class="kh">Why it swarms</h3>
<p>Because saying “that'll cost something” feels awkward, and each request seems too small for the awkwardness.</p>
<h3 class="kh">What kills it</h3>
<ul class="fears"><li>A visible log.</li><li>Choices, not refusals.</li><li>The original scope, cheerfully quoted.</li><li>Phase two.</li></ul>
<h3 class="kh">Three kinds of swarm</h3>
<div class="breeds">
<div><b>The Innocent Swarm</b><p>The client doesn't realise. Show them the count and they'll stop.</p></div>
<div><b>The Tactical Swarm</b><p>The client knows exactly what they're doing. The Trade-Off Menu, every time.</p></div>
<div><b>The Internal Swarm</b><p>Your own team keeps adding “nice to haves”. Same cure.</p></div>
</div>
{note("“Phase two” is the most powerful phrase in delivery. It's yes, with a date.")}""",
        difficulty=dict(
            normal=dict(who="The Innocent Swarm, caught early.",
                        know=["A few small requests.", "The client is reasonable.", "The project is still on track."],
                        do=["Start a log now.", "Offer the menu from the next request.", "Mention phase two early."],
                        avoid="The hero yes.",
                        next="If you've already absorbed lots, you're at Nightmare."),
            nightmare=dict(who="The swarm has already eaten a third of the budget.",
                           know=["Dozens of small changes.", "Nobody logged them.", "The deadline is at risk."],
                           do=["Reconstruct the Swarm Count.", "Share it as a table, not a complaint.", "Reset: what's in, what's phase two.", "Tell your boss before the client."],
                           avoid="The sudden wall.",
                           next="If the client refuses to reset, you're at Hell."),
            hell=dict(who="The Tactical Swarm, refusing to pay.",
                      know=["They know it's out of scope.", "They insist it's “implied”.", "They threaten to escalate."],
                      do=["Go back to the signed scope, line by line.", "Involve commercial and your boss.", "Offer a priced change request.", "Read the Escalation Summoning."],
                      avoid="The sneaky shrink.",
                      next="If it never stops, see Banishing a Client."),
        ),
        mirror=dict(
            title="Are you the Swarm?",
            intro="Whether you're a client or a colleague. Tick honestly.",
            signs=["You've started a request with “could you just”.", "You've added something to a project without asking what it would delay.",
                   "You can't remember what was in the original brief.", "You think small favours are free.",
                   "You've been surprised that a project took longer than planned, after you added to it."],
            cure="Next time you ask for something extra, add: “What would that move?” It's the most respectful sentence a client can say.",
        ),
        rehearsal=dict(
            title="Scene: Monday 18 September 2028, the reset call.",
            intro="The Swarm Count and the Trade-Off Menu.",
            lines=[
                ("Pip", "Gavin, I owe you an apology. I've said yes to twenty-three small things and never told you what they added up to."),
                ("Gavin", "Twenty-three? Really?"),
                ("Pip", "Thirty-one days, on a forty-day project. It's in the table I sent. That's my fault for not saying."),
                ("Gavin", "Well, I'd rather know. What do we do?"),
                ("Pip", "From now on, every addition comes with three options: in and later, instead of something, or phase two. You choose."),
                ("Gavin", "Phase two for the iPad thing, then. And the school sites. And… let me look at the rest."),
            ],
            note="Phase two was signed in November for £60,000. It contained nineteen of the twenty-three “small things”.",
        ),
    ),
    # ------------------------------------------------------------------ the Eleven-Headed Hydra
    "eleven-headed-hydra": dict(
        sighting=f"""{beat("Tuesday 26 September 2028 · the steering group")}
<p>Phase two's first steering group had eleven people in it. Planning wanted ward boundaries. Highways wanted road
segments. Housing wanted estates. Finance said nothing and took notes. Two councillors wanted their own wards on the
first page. Five others had opinions on the colour scheme.</p>
{beat("The next week")}
<p>The housing layer, agreed in the meeting, was reopened by email by highways, who hadn't been there. Then by a
councillor, who had. Gavin, in the middle, said “I'll need to take it to…” fourteen times in five days. Pip counted.</p>
{beat("Friday 29 September · the Body Finder")}
<p>Pip asked Gavin, kindly, who decided when the heads disagreed. Gavin didn't know. Neither did anyone else. Pip asked
whether they could find out, explaining that without one person, the project couldn't finish, and Gavin would be blamed.</p>
{beat("Tuesday 3 October · the body")}
<p>Gavin took it to Nadia Sesay, Director of Place. She'd assumed Gavin was deciding. She named herself the owner, with
Gavin running day to day. Decision 14, the housing layer, was approved that afternoon and stayed approved.</p>
{note("A hydra has many heads but one body. Most clients don't know who their body is until you ask.")}""",
        origin=dict(
            title="How Wexley grew eleven heads",
            beats=[
                ("2018 · the consultation duty", "After a planning row, Wexley adopts a rule: every project involving land consults every affected department. Sensible."),
                ("2021 · the steering habit", "Consultation becomes steering groups, and steering groups become places where anyone can raise anything. Nobody is given the final say."),
                ("2024 · the safety of many", "If eleven people decide, nobody is blamed. The hydra is comfortable for everyone inside it."),
                ("2028 · the vendor's problem", "GridSight arrives, needing decisions. The hydra gives it eleven opinions and no answer."),
            ],
            turning="A good rule (consult everyone) that quietly became a bad one (everyone decides).",
            saved="One sentence in the original project charter: “Final decisions: Director of Place.”",
            note="Consultation is asking everyone. Decision is one person choosing. Hydras grow when the two get mixed up.",
        ),
        know=f"""<p>The hydra is a client with many stakeholders and no clear decision maker. It isn't malicious. It's an organisation
where consulting has become deciding, so every head can veto and none can approve. Vendors get stuck in the middle,
building versions for each head.</p>
<h3 class="kh">What it wants</h3>
<p>To be heard. Each head wants its concern taken seriously. Most will accept a decision they disagree with, if someone with authority made it.</p>
<h3 class="kh">Why it regrows heads</h3>
<p>Because decisions aren't written down, so anyone who missed a meeting can reopen anything.</p>
<h3 class="kh">What tames it</h3>
<ul class="fears"><li>One named decision maker.</li><li>A decision log, shared after every meeting.</li><li>A stakeholder map.</li><li>A clear process for reopening.</li></ul>
<h3 class="kh">Three kinds of hydra</h3>
<div class="breeds">
<div><b>The Committee</b><p>A formal group, no chair with authority. Ask for one.</p></div>
<div><b>The Headless Body</b><p>The decider exists but doesn't know it. Help your contact find them.</p></div>
<div><b>The Warring Heads</b><p>Two departments using your project to fight each other. Escalate to their shared boss.</p></div>
</div>
{note("The quietest head is often finance. Talk to them early, before they surprise you at the end.")}""",
        difficulty=dict(
            normal=dict(who="The Committee with a likely chair.",
                        know=["Lots of stakeholders.", "Someone senior seems to lead.", "Decisions do get made, slowly."],
                        do=["Do the Head Count.", "Confirm the decider in writing.", "Start the Decision Log."],
                        avoid="Pleasing every head.",
                        next="If nobody can decide, you're at Nightmare."),
            nightmare=dict(who="The Headless Body.",
                           know=["Nobody can say yes.", "Decisions are reopened weekly.", "Your contact is stuck in the middle."],
                           do=["Do the Body Finder with your contact.", "Explain what it's costing them.", "Offer to help them write the case to their boss.", "Log everything."],
                           avoid="The back channel.",
                           next="If two heads are at war, you're at Hell."),
            hell=dict(who="The Warring Heads.",
                      know=["Two departments disagree on principle.", "Each briefs you against the other.", "Your project is their battlefield."],
                      do=["Refuse private promises.", "Put both options to the shared boss, in one document.", "Recommend one, with reasons.", "Pause work on the disputed part until it's decided."],
                      avoid="Choosing a side in secret.",
                      next="If nobody will decide at all, pause the project and say why."),
        ),
        mirror=dict(
            title="Are you a head of the Hydra?",
            intro="Think about the projects you're a stakeholder in. Tick honestly.",
            signs=["You've reopened a decision made in a meeting you didn't attend.", "You don't know who has the final say on a project you comment on.",
                   "You've briefed a vendor privately against a colleague.", "You've said “I'll need to check with…” without knowing who.",
                   "You attend a steering group and have never asked what it decides."],
            cure="Before your next comment on a shared project, ask: “Who decides this?” If nobody knows, help find out.",
        ),
        rehearsal=dict(
            title="Scene: Friday 29 September 2028, Pip and Gavin, after the steering group.",
            intro="The Body Finder, kindly.",
            lines=[
                ("Pip", "Gavin, can I ask something that might sound odd? When highways and housing disagree, who decides?"),
                ("Gavin", "…The steering group?"),
                ("Pip", "The steering group can't seem to. And I think you're getting the blame for that."),
                ("Gavin", "I am. Every week."),
                ("Pip", "Could we ask Nadia to name one person? Even her. I'll write a half-page on what it's costing, if that helps."),
                ("Gavin", "Please do. I've wanted to say this for a year."),
            ],
            note="Nadia read the half-page on Monday, named herself the owner on Tuesday, and said: “Why did nobody ask me this in 2024?”",
        ),
    ),
    # ------------------------------------------------------------------ the Unpaid Invoice Wraith
    "unpaid-invoice-wraith": dict(
        sighting=f"""{beat("Friday 1 September 2028 · the invoice")}
<p>GridSight finished a water-demand study for <b>Brackenfield Water</b>. Hamish Grant, their operations director, loved
it. Felix sent invoice 0047, <b>£84,000</b>, 30-day terms, to Hamish's email address, with a cheerful note.</p>
{beat("October and November · the drift")}
<p>Nothing. Hamish said it was “with finance”. Finance, it turned out, had never seen it: invoices without a PO number
went into a shared mailbox nobody read. Felix assumed delivery was chasing. Delivery assumed Felix was. Phase two was due
to start in December.</p>
{beat("Wednesday 6 December · day 97")}
<p>Asha noticed the invoice in the ledger, ninety-seven days old, and asked whose it was. Nobody's, it seemed. Pip rang
Hamish, kindly, and asked who in finance could help. Hamish gave him a name: <b>Moira Venn</b>, accounts payable.</p>
{beat("Thursday 7 December · Moira")}
<p>Moira was not the villain. She needed a PO number, the invoice addressed to “Accounts Payable, Brackenfield Water”, and
a PDF, not a link. Hamish raised the PO that afternoon. Pip resent the invoice. Moira confirmed receipt. It was paid on 19
December, in the next payment run, exactly as she'd said.</p>
{note("Most unpaid invoices aren't unpaid. They're lost, because nobody asked how this client pays.")}""",
        origin=dict(
            title="How invoice 0047 became a wraith",
            beats=[
                ("2015 · Brackenfield's controls", "After a fraud, Brackenfield Water rules that no invoice is paid without a purchase order number. Very sensible."),
                ("2020 · the shared mailbox", "Invoices without POs are routed to a mailbox for “manual review”. The person who reviewed it leaves in 2023. Nobody replaces them."),
                ("July 2028 · GridSight starts work", "Hamish is keen; the work starts on a handshake and an email. Nobody asks for a PO. Nobody knows to."),
                ("September 2028 · the invoice is sent", "To Hamish, who forwards it to the mailbox, where it lies for ninety-seven days, unread and unpaid."),
            ],
            turning="Starting work without asking the dullest question in business: “How do you pay suppliers?”",
            saved="The Paper Ward, at kick-off: PO number, invoice address, terms. Two minutes. £84,000.",
            note="Accounts payable aren't trying not to pay you. They're trying not to pay fraudsters. Help them tell the difference.",
        ),
        know=f"""<p>Unpaid invoices are rarely about the client refusing to pay. Usually the paperwork is wrong: no PO, the wrong
address, the wrong format, the wrong person. Sometimes it's cash flow, and sometimes it's tactics. Your job is to find out
which, quickly and politely.</p>
<h3 class="kh">What it wants</h3>
<p>The right paperwork. Finance teams pay what fits their process. Anything else drifts.</p>
<h3 class="kh">Why it haunts</h3>
<p>Because chasing feels awkward, nobody on your side owns it, and the client contact who loved your work has no idea how their own finance team works.</p>
<h3 class="kh">What lays it to rest</h3>
<ul class="fears"><li>A PO number before work starts.</li><li>One owner for chasing, on your side.</li><li>A named contact in their finance team.</li><li>A pause clause in the contract.</li></ul>
<h3 class="kh">Three kinds of wraith</h3>
<div class="breeds">
<div><b>The Lost Wraith</b><p>Paperwork problem. Fix the paperwork; it's paid.</p></div>
<div><b>The Slow Wraith</b><p>Cash-flow trouble. Agree a schedule, in writing.</p></div>
<div><b>The Tactical Wraith</b><p>They're using you as a free loan. Pause clause, then escalation.</p></div>
</div>
{note("Never let “who's chasing?” go unanswered. Write the owner's name next to every invoice.")}""",
        difficulty=dict(
            normal=dict(who="The Lost Wraith.",
                        know=["The client is happy.", "Nobody refuses to pay.", "Something's wrong with the paperwork."],
                        do=["Ask your contact who in finance can help.", "Ask finance exactly what they need.", "Resend it, and confirm receipt."],
                        avoid="The angry letter.",
                        next="If it's still unpaid at 60 days, you're at Nightmare."),
            nightmare=dict(who="The Slow Wraith.",
                           know=["The paperwork is right.", "Payment keeps slipping.", "Phase two is about to start."],
                           do=["Talk to your contact's boss, kindly.", "Agree a payment schedule in writing.", "Don't start new work until it's settled.", "Tell your finance team."],
                           avoid="Starting phase two anyway.",
                           next="If they're doing it on purpose, you're at Hell."),
            hell=dict(who="The Tactical Wraith.",
                      know=["They pay everyone late, on purpose.", "Excuses change every time.", "They want more work anyway."],
                      do=["Use the pause clause.", "Escalate formally, with dates.", "Consider late-payment interest (in the UK, the law allows it).", "Read Banishing a Client."],
                      avoid="The awkward silence.",
                      next="If they still don't pay, take advice on debt recovery."),
        ),
        mirror=dict(
            title="Are you the Wraith?",
            intro="Have you been the client who didn't pay, without meaning to? Tick honestly.",
            signs=["You've let a supplier start work before raising a PO.", "You don't know how your own finance team pays suppliers.",
                   "You've forwarded an invoice and never checked it was paid.", "A supplier has chased you and you felt annoyed, not sorry.",
                   "You've asked for more work from a supplier you haven't paid."],
            cure="Next time you bring in a supplier, send them the PO number and your finance contact on day one. It's the kindest thing a client can do.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 7 December 2028, Pip calls Moira Venn.",
            intro="The Paper Ward, ninety-seven days late.",
            lines=[
                ("Pip", "Hi Moira, I'm Pip from GridSight. Hamish suggested you. We've an invoice from September I think got lost. I'd love to know what you need."),
                ("Moira", "Have you got a PO number?"),
                ("Pip", "No, and I think that's the problem. What else do you need?"),
                ("Moira", "Addressed to Accounts Payable, as a PDF. With a PO, it'll be in the next run, on the nineteenth."),
                ("Pip", "Brilliant. I'll get the PO from Hamish today. Can I check it's arrived before I hang up next time?"),
                ("Moira", "You'd be the first. Yes, please."),
            ],
            note="Paid on 19 December. GridSight's kick-off checklist now starts with: “PO number. Invoice address. Finance contact.”",
        ),
    ),
    # ------------------------------------------------------------------ the Bake-Off Arena
    "bake-off-arena": dict(
        sighting=f"""{beat("October 2028 · the tender")}
<p><b>Northshire Combined Authority</b> went to tender for a regional demand forecast: eight councils, one model, a
budget of £240,000. Fourteen vendors applied. Three were shortlisted: GridSight, <b>Corvid Analytics</b>, and Vexmoor
Consulting, who had never built a forecast but had very good slides.</p>
{beat("Thursday 9 November · room 3")}
<p>Corvid went first. Zara Okafor, their founder, was excellent: sharp, funny, deeply technical. She promised the full
model in <b>six weeks</b>. The panel visibly relaxed. Vexmoor went second and said “transformational” nine times.</p>
{beat("Thursday 9 November · 15:00 · GridSight")}
<p>Felix had begged Pip to promise eight weeks. Pip had refused, and they'd argued about it in the car park. Pip's slide
said <b>sixteen weeks</b>, and below it: “Week 4: first council live. Week 8: four councils. Week 16: all eight.” Then
Asha showed Wexley's map, live, on her laptop. Then Pip asked the panel what would make this project a disaster for them.</p>
{beat("Thursday 30 November · the result")}
<p>The chair, it turned out, had been burned by a six-week promise in 2025. GridSight won. Bernard Quill, from
procurement, said privately: “Your sixteen weeks was the only number in the room anyone believed.”</p>
{note("Panels aren't buying speed. They're buying the absence of embarrassment. Show them you won't embarrass them.")}""",
        origin=dict(
            title="How bake-offs came to reward lies",
            beats=[
                ("The 1990s · the price war", "Public tenders are judged mostly on price. Vendors learn to bid low and charge for changes later."),
                ("The 2010s · the speed war", "Buyers want quick results. Vendors learn to promise fast and explain the delays later."),
                ("2025 · Northshire's scar", "The authority's last forecasting vendor promised six weeks and took eleven months. The chair still talks about it at dinner."),
                ("2028 · the arena", "Three vendors, one prize. The one with the most impressive number usually wins. Unless the panel has been burned."),
            ],
            turning="Buyers rewarding confidence over credibility, until they've been burned once.",
            saved="Every vendor asking, before the pitch: “What went wrong last time?”",
            note="Every panel has a scar. Find it, and pitch to the scar, not the scoring sheet.",
        ),
        know=f"""<p>A vendor bake-off is a competition where several suppliers pitch for the same work. The temptation is to win
by promising more, faster, cheaper. It works often enough to be dangerous. The vendors who last are the ones who win on
credibility, and lose gracefully when credibility isn't enough.</p>
<h3 class="kh">What the panel wants</h3>
<p>To choose someone they won't regret. Their fear of a bad choice is bigger than their wish for a perfect one.</p>
<h3 class="kh">Why rivals overpromise</h3>
<p>Because it often wins, and the consequences arrive after the contract, to someone else (usually delivery).</p>
<h3 class="kh">What wins honestly</h3>
<ul class="fears"><li>Understanding the buyer's fear.</li><li>A plan with early proof points.</li><li>A live demo.</li><li>A reference who'll take a call.</li></ul>
<h3 class="kh">Three kinds of arena</h3>
<div class="breeds">
<div><b>The Fair Fight</b><p>Clear criteria, honest panel. Credibility wins.</p></div>
<div><b>The Price War</b><p>Cheapest wins. Decide whether you want to be cheapest.</p></div>
<div><b>The Beauty Contest</b><p>Slides win. Bring proof anyway; some panel member will notice.</p></div>
</div>
{note("If you lose to an impossible promise, stay in touch. The buyer will need someone in about five months.")}""",
        difficulty=dict(
            normal=dict(who="The Fair Fight.",
                        know=["Clear scoring criteria.", "The panel asks good questions.", "Rivals are credible."],
                        do=["Find the buyer's fear.", "Show an honest plan.", "Bring proof."],
                        avoid="The generic deck.",
                        next="If a rival promises the impossible, you're at Nightmare."),
            nightmare=dict(who="The rival promises the impossible.",
                           know=["Their timeline is half yours.", "The panel liked it.", "Your sales team is panicking."],
                           do=["Don't match it.", "Show early proof points instead.", "Ask the panel what went wrong last time.", "Name the risk of speed, without naming the rival."],
                           avoid="The impossible promise.",
                           next="If your own side forces the promise, you're at Hell."),
            hell=dict(who="Your own sales team wants to promise it.",
                      know=["Your sales director has already hinted at the number.", "Your boss wants the win.", "You'll be the one delivering."],
                      do=["Put the real plan in writing.", "Tell your boss what the risk is.", "Offer a faster first phase instead.", "Refuse to sign what you can't deliver."],
                      avoid="Rubbishing the rival.",
                      next="If you're overruled, read the Overpromise Golem now."),
        ),
        mirror=dict(
            title="Are you the overpromiser in the arena?",
            intro="Whether you pitch to clients or to your own leadership. Tick honestly.",
            signs=["You've given a date in a pitch you weren't sure you could hit.", "You've criticised a competitor to a buyer.",
                   "You've used the same deck for three different clients.", "You've never asked a buyer what went wrong last time.",
                   "You think losing a pitch is always a failure."],
            cure="In your next pitch, include one honest risk and how you'll handle it. It's the most believable slide you'll ever show.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 9 November 2028, room 3, GridSight's pitch.",
            intro="The Fear Reading and the Honest Plan.",
            lines=[
                ("Panel chair", "Corvid have offered six weeks. You're saying sixteen. Why should we wait ten weeks longer?"),
                ("Pip", "May I ask a question first? What would make this project a disaster for you?"),
                ("Panel chair", "…Promises we can't report to eight councils. We had that in 2025."),
                ("Pip", "Then here's what you'd report: one council live in week four, four by week eight, all eight by sixteen. Each one real."),
                ("Asha", "And this is Wexley's version. It's live. You can click it."),
                ("Panel chair", "Can I speak to Wexley?"),
                ("Pip", "Gavin's expecting your call."),
            ],
            note="Gavin, once the Client Demon, gave GridSight a glowing reference. He mentioned the late-night calls, and how Pip had stopped them.",
        ),
    ),
    # ------------------------------------------------------------------ the Incumbent Dragon
    "incumbent-dragon": dict(
        sighting=f"""{beat("January 2029 · the renewal")}
<p>MetroVolt's billing contract with <b>Halvorsen Systems</b> was due to renew in April. It had renewed automatically in
2020 and 2024. Nobody remembered why Halvorsen had been chosen in 2016. Ruth asked Pip, as someone who now knew what
vendors were like from the other side, to sit on the evaluation.</p>
{beat("The hoard")}
<p>Pip did the Hoard Count. Halvorsen held: twelve years of billing data in a format only they could export, 34 custom
integrations nobody at MetroVolt had documented, and the only two people who understood the tariff engine. Every
internal conversation about switching ended with someone saying “far too risky”. Usually after a call with Sven.</p>
{beat("February · the real contest")}
<p>MetroVolt went to market, properly. Pip told Sven, plainly, that Halvorsen was welcome to bid and would be judged on
the same criteria as everyone. Sven, who had brought biscuits to every review meeting for twelve years, looked genuinely
startled. Then he went back to Halvorsen and, for the first time in years, they sharpened.</p>
{beat("March 2029 · the outcome")}
<p>Halvorsen won. Their bid was <b>18% cheaper</b> than their last renewal, included a full data-export clause and
documentation of all 34 integrations, and offered three new features. Pip's verdict: “The dragon is still here. It's just
not asleep any more.”</p>
{note("You don't have to slay the dragon. You just have to make it fly.")}""",
        origin=dict(
            title="How Halvorsen became a dragon",
            beats=[
                ("2016 · the good choice", "MetroVolt picks Halvorsen after a proper tender. They're genuinely the best. The project goes well."),
                ("2020 · the first renewal", "The contract renews automatically. Nobody reviews it; things work. Halvorsen quietly builds custom integrations."),
                ("2024 · the hoard", "Only Halvorsen understands the tariff engine. Switching would mean rebuilding twelve years of knowledge. The contract renews again."),
                ("2029 · the dragon", "Halvorsen isn't evil. It's comfortable. And comfort, over twelve years, becomes lock-in."),
            ],
            turning="The 2020 renewal, unexamined because things were working.",
            saved="An exit plan and a documentation clause in the 2016 contract, and an honest review at every renewal.",
            note="Most incumbent dragons were once the best choice. They became dragons because nobody asked again.",
        ),
        know=f"""<p>An incumbent vendor is one that's been there for years. They know your systems, hold your data and understand your
quirks. That makes them valuable and hard to replace. Over time it can make them complacent, expensive and the only
people who understand how your business works.</p>
<h3 class="kh">What it wants</h3>
<p>Renewal. Stability. Not to be put through the effort of a competition it might lose.</p>
<h3 class="kh">Why it grows</h3>
<p>Because every year without review adds more knowledge to its hoard, and makes switching seem scarier.</p>
<h3 class="kh">What weakens it</h3>
<ul class="fears"><li>Your own documentation.</li><li>A data-export clause.</li><li>A real competition.</li><li>A credible alternative.</li></ul>
<h3 class="kh">Three kinds of dragon</h3>
<div class="breeds">
<div><b>The Sleeping Dragon</b><p>Comfortable, not malicious. A real contest wakes it up.</p></div>
<div><b>The Hoarding Dragon</b><p>Keeps knowledge to itself on purpose. Demand documentation in the contract.</p></div>
<div><b>The Good Dragon</b><p>Still the best. Renew, with an exit plan anyway.</p></div>
</div>
{note("If you're the incumbent: the day your client stops asking for new ideas is the day they start planning to leave.")}""",
        difficulty=dict(
            normal=dict(who="The Good Dragon.",
                        know=["The vendor still performs well.", "Pricing is fair.", "You could leave if you had to."],
                        do=["Review at every renewal.", "Keep an exit plan current.", "Ask them for one new idea a year."],
                        avoid="The silent renewal.",
                        next="If you couldn't leave if you wanted to, you're at Nightmare."),
            nightmare=dict(who="The Sleeping Dragon, sitting on your hoard.",
                           know=["Only they understand key systems.", "Prices rise every renewal.", "Everyone says switching is too risky."],
                           do=["Do the Hoard Count.", "Start documenting in-house.", "Run a real competition.", "Add an export clause to the next contract."],
                           avoid="The slay-at-any-cost.",
                           next="If they're blocking you deliberately, you're at Hell."),
            hell=dict(who="The Hoarding Dragon.",
                      know=["They refuse to share documentation.", "They lobby your executives directly.", "Data exports are “not possible”."],
                      do=["Get legal to review data ownership.", "Brief your executives first, with facts.", "Plan a staged exit.", "Talk to other clients of theirs."],
                      avoid="Any switch without an exit plan.",
                      next="If you must leave, leave slowly, piece by piece."),
        ),
        mirror=dict(
            title="Are you the Dragon?",
            intro="As a vendor, a team, or a person who's been in a role for years. Tick honestly.",
            signs=["You're the only person who understands something important, and you like it that way.", "You haven't brought your client a new idea this year.",
                   "You assume your contract or role will renew.", "You describe every alternative to you as “risky”.",
                   "Your documentation lives mostly in your head."],
            cure="Write down one thing only you know, and share it. Dragons that share their hoard get renewed because they're good, not because they're stuck.",
        ),
        rehearsal=dict(
            title="Scene: Monday 5 February 2029, Pip calls Sven Aldous.",
            intro="The Real Contest, said plainly.",
            lines=[
                ("Pip", "Sven, I wanted to tell you directly: we're going to market for the billing renewal."),
                ("Sven", "Ah. After twelve years. Switching would be very risky, Pip."),
                ("Pip", "It might be. That's why we'd love you to bid. You'll be judged on the same criteria as everyone."),
                ("Sven", "…What would make our bid stand out?"),
                ("Pip", "Honestly? A data-export clause, documentation for the integrations, and something new. We haven't had something new since 2019."),
                ("Sven", "That's… fair. I'll take it back."),
            ],
            note="Sven took it back. Halvorsen's bid was their best in a decade. He still brings biscuits.",
        ),
    ),
    # ------------------------------------------------------------------ the Rigged RFP
    "rigged-rfp": dict(
        sighting=f"""{beat("Friday 15 December 2028 · the tender")}
<p><b>Ardmore County Council</b> published a tender for a grid capacity study, value £180,000, responses due 3
January. Felix forwarded it at 17:42 with three exclamation marks. Requirement 4.7, page 31: <i>“The supplier must
demonstrate at least five years' experience of the Corvid platform.”</i></p>
{beat("Monday 18 December · the Bid / No-Bid Rite")}
<p>Corvid's platform was five years old. Only Corvid had five years' experience of it. Pip and Asha scored the tender:
could we win (2/10), could we deliver (9/10), do we want it (7/10). Writing the bid would take three people most of the
holidays.</p>
{beat("Tuesday 19 December · the clarifying question")}
<p>Pip asked, formally, whether equivalent experience with a comparable platform would be accepted. The answer came on
the 22nd: “No.” Felix wanted to bid anyway (“they might not be strict”). Pip and Ruth said no.</p>
{beat("Wednesday 20 December, then the spring · the graceful decline")}
<p>Pip wrote a two-line note to Ardmore's procurement team declining, with the reason, and asking to talk about future
work. GridSight's team had a Christmas. In April, Ardmore's head of planning rang: they'd like GridSight to quote for a
different study. “You were the only firm that explained why you didn't bid.”</p>
{note("A no-bid isn't a loss. It's three weeks of your team's life, spent on something you could actually win.")}""",
        origin=dict(
            title="How a tender came to be written for Corvid",
            beats=[
                ("2023 · the pilot", "Ardmore runs a small pilot with Corvid. It goes well. Ardmore's analysts learn Corvid's platform and like it."),
                ("2028 · the rules", "Public procurement rules require an open tender for anything over the threshold. Ardmore must advertise."),
                ("December 2028 · the copying", "The analyst writing the requirements copies them from Corvid's pilot documentation. Not out of corruption; out of familiarity, and a deadline."),
                ("The result", "An open tender only one vendor can win. Nobody at Ardmore thinks of it as rigged. They think of it as specific."),
            ],
            turning="A buyer who already knew what they wanted being forced to pretend they didn't.",
            saved="A pre-market conversation, so other vendors could ask about requirement 4.7 before it was published.",
            note="Most rigged tenders aren't corrupt. They're written by people who already have a favourite and a deadline.",
        ),
        know=f"""<p>A rigged RFP (request for proposal) is a tender whose requirements favour one vendor so strongly that nobody else
can realistically win. Sometimes it's deliberate. More often the buyer already has a preferred supplier and has to run an
open process anyway. Either way, bidding costs you weeks.</p>
<h3 class="kh">What it wants</h3>
<p>Usually, to look open while choosing someone already chosen. Sometimes, a cheaper quote to push the favourite's price down.</p>
<h3 class="kh">Why it exists</h3>
<p>Because procurement rules require competition, and people's preferences don't disappear because a rule says they should.</p>
<h3 class="kh">How to spot it</h3>
<ul class="fears"><li>Requirements naming a product.</li><li>Absurdly short deadlines.</li><li>No pre-market engagement.</li><li>Oddly precise experience criteria.</li></ul>
<h3 class="kh">Three kinds of rigged scroll</h3>
<div class="breeds">
<div><b>The Familiar Scroll</b><p>Written around what they know. A clarifying question may open it up.</p></div>
<div><b>The Price-Check Scroll</b><p>They want your quote to negotiate with their favourite. Don't bid hard.</p></div>
<div><b>The Truly Rigged Scroll</b><p>Deliberately unfair. Decline, or challenge formally if it really matters.</p></div>
</div>
{note("Score every tender before you write a word. The best bid teams say no more often than yes.")}""",
        difficulty=dict(
            normal=dict(who="The Familiar Scroll.",
                        know=["One requirement looks odd.", "The rest is open.", "The buyer answers questions."],
                        do=["Ask the clarifying question.", "Score the tender.", "Bid only if the answer opens it up."],
                        avoid="Bidding everything.",
                        next="If the answer is “no”, you're at Nightmare."),
            nightmare=dict(who="The scroll that won't open.",
                           know=["The requirement stays.", "Your sales team wants to bid anyway.", "It would take weeks."],
                           do=["Do the Bid / No-Bid Rite with your boss.", "Decline gracefully, with a reason.", "Ask about future work.", "Spend the time on a tender you can win."],
                           avoid="The fake fit.",
                           next="If it's genuinely unfair to all bidders, you're at Hell."),
            hell=dict(who="The Truly Rigged Scroll.",
                      know=["It's public money.", "The unfairness is clear and serious.", "Other vendors have noticed too."],
                      do=["Take advice before acting.", "Raise it through the formal procurement challenge process.", "Stick to facts.", "Accept that it may cost you goodwill."],
                      avoid="The furious complaint.",
                      next="Choose your battles. Most aren't worth it."),
        ),
        mirror=dict(
            title="Have you written a rigged scroll?",
            intro="If you've ever written a job advert or a supplier brief. Tick honestly.",
            signs=["You've written requirements around someone you'd already chosen.", "You've run a process you knew the outcome of.",
                   "You've asked for quotes just to push down a favourite's price.", "You've set a deadline nobody new could meet.",
                   "You've copied requirements from a supplier's own documents."],
            cure="If you've already chosen, say so and use the right process for that. Don't make strangers write bids for a prize that's gone.",
        ),
        rehearsal=dict(
            title="Scene: Monday 18 December 2028, Pip, Asha and Felix.",
            intro="The Bid / No-Bid Rite.",
            lines=[
                ("Felix", "£180,000! We have to bid."),
                ("Pip", "Requirement 4.7. Five years on Corvid's platform. Only Corvid has that."),
                ("Felix", "They might not be strict."),
                ("Asha", "Can we win: two out of ten. Deliver: nine. Want it: seven. And it's three of us over Christmas."),
                ("Pip", "Let's ask the clarifying question. If they relax it, we bid. If not, we decline, nicely."),
                ("Felix", "…Fine. But I'm writing the nice decline."),
                ("Pip", "Deal. Keep it to two lines."),
            ],
            note="Felix's decline was three lines. It was still the one Ardmore remembered.",
        ),
    ),
    # ------------------------------------------------------------------ the Frenemy Pact
    "frenemy-pact": dict(
        sighting=f"""{beat("October 2028 · the partnership")}
<p>The regulator opened a regional flexibility competition: pay utilities to shift demand away from peak hours. Neither
GridSight nor <b>Northgate Energy</b> could win it alone. Theo Blake, Northgate's partnerships lead, proposed a joint
bid. Ruth, who used to work at Northgate, said yes, and then said: “Write everything down.”</p>
{beat("The Written Pact")}
<p>Pip drafted one page: the joint work, what each side shared (demand data for three regions), what each kept (pricing,
client lists, other bids), and who owned the model they built together. Theo signed it cheerfully. “Very thorough!”</p>
{beat("Thursday 18 January 2029 · the other hand")}
<p>At the end of a joint workshop, Theo asked Pip, casually, how GridSight priced Wexley's phase two. Pip smiled and said
that was outside the pact. Theo laughed: “Worth a try!” In February, Northgate bid against GridSight for Wexley's phase
three. Pip had known they would. It was in the Open Rivalry conversation, in October.</p>
{beat("March 2029 · both outcomes")}
<p>The joint flexibility bid won: £1.2 million across both firms. Wexley stayed with GridSight. Theo sent a bottle of
wine with a card: <i>“Good game. Partners again in the autumn?”</i> Pip said yes, and started drafting the next pact.</p>
{note("A frenemy isn't a traitor. They're a competitor who's honest enough to work with you. Be honest back, in writing.")}""",
        origin=dict(
            title="How Northgate became a frenemy",
            beats=[
                ("2010s · rivals", "MetroVolt and Northgate compete for the same customers, the same staff and the same regulators. They don't talk."),
                ("2024 · the regulator", "The regulator starts funding regional projects that need several utilities to share data. Rivals must now cooperate to compete."),
                ("2027 · Ruth moves", "Ruth Calloway leaves Northgate for MetroVolt. She knows exactly how Northgate thinks, and likes them anyway."),
                ("2028 · the pact", "A joint bid makes sense. So does competing elsewhere. Both are true at once. That's a frenemy."),
            ],
            turning="Markets where you must partner with your competitors to win anything big.",
            saved="Nothing needed saving. Frenemy pacts are normal and useful. What matters is writing the rules.",
            note="Most industries now run on frenemies. The ones that last are the ones with a one-page pact.",
        ),
        know=f"""<p>A frenemy is a partner who is also a competitor: you bid together for one thing and against each other for another.
This is normal in most industries, and it can work well. It goes wrong when nobody writes down what's shared, and
information from the partnership leaks into the competition.</p>
<h3 class="kh">What it wants</h3>
<p>To win the joint prize, and to learn anything useful along the way. Both are reasonable. Only one is in the pact.</p>
<h3 class="kh">Why it probes</h3>
<p>Because it's a competitor, and competitors are curious. It isn't personal. Don't take it personally, and don't answer.</p>
<h3 class="kh">What keeps it honest</h3>
<ul class="fears"><li>A written, one-page pact.</li><li>Separate people for joint and competing work, where possible.</li><li>Saying the rivalry out loud.</li><li>Competition law (yes, it applies).</li></ul>
<h3 class="kh">Three kinds of frenemy</h3>
<div class="breeds">
<div><b>The Honest Rival</b><p>Competes openly, partners fairly. Keep them.</p></div>
<div><b>The Prober</b><p>Always asking one question too many. Smile, and point to the pact.</p></div>
<div><b>The Raider</b><p>Uses what you share to beat you. End the partnership, and take advice.</p></div>
</div>
{note("Never share pricing with a competitor, even in a partnership. In many countries that's not just unwise, it's against competition law.")}""",
        difficulty=dict(
            normal=dict(who="The Honest Rival.",
                        know=["The rivalry is openly acknowledged.", "There's a written pact.", "Both sides stick to it."],
                        do=["Keep the pact current.", "Review what's shared each quarter.", "Congratulate them when they win."],
                        avoid="The paranoid freeze.",
                        next="If they keep probing, you're at Nightmare."),
            nightmare=dict(who="The Prober.",
                           know=["Casual questions about your other work.", "Friendly, persistent curiosity.", "Requests for “just a bit more” data."],
                           do=["Point to the pact, kindly.", "Tell your boss about each probe.", "Separate the people on joint and competing work.", "Check with legal what you may share."],
                           avoid="The trusting overshare.",
                           next="If they use what you shared against you, you're at Hell."),
            hell=dict(who="The Raider.",
                      know=["They've used your shared data to compete.", "They deny it.", "Your clients have heard your numbers."],
                      do=["Document what happened.", "Take legal advice.", "End or suspend the partnership.", "Tell affected clients what you can, honestly."],
                      avoid="The secret raid back.",
                      next="Never partner with them again without a much tighter pact."),
        ),
        mirror=dict(
            title="Are you the Frenemy?",
            intro="With other firms or other teams in your own company. Tick honestly.",
            signs=["You've asked a partner a question you knew was outside the agreement.", "You've used something learned in a partnership to compete.",
                   "You've never said the rivalry out loud.", "You've been friendly mainly to get information.",
                   "You think “worth a try” is a business ethic."],
            cure="Before your next joint project, write one page: what's shared, what isn't. Then keep to it, even when it would be easy not to.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 10 October 2028, Pip and Theo, before signing.",
            intro="The Written Pact and the Open Rivalry.",
            lines=[
                ("Pip", "Before we start, can we agree one page? What's joint, what stays ours, who owns the model."),
                ("Theo", "Very thorough. Sure."),
                ("Pip", "And just so it's said: you'll probably bid for Wexley's next phase. We'll probably bid for your water clients."),
                ("Theo", "Ha. Probably. Is that a problem?"),
                ("Pip", "Not if we keep it off this project entirely. Different people, no pricing, no client names."),
                ("Theo", "Agreed. Honestly, it's a relief to say it."),
            ],
            note="Theo's probe in January was, he admitted later, “a bit of a test”. Pip passed it. So the partnership continued.",
        ),
    ),
    # ------------------------------------------------------------------ the Overpromise Golem
    "overpromise-golem": dict(
        sighting=f"""{beat("Tuesday 26 September 2028 · the sale")}
<p>Felix, at lunch with Hamish Grant of Brackenfield Water, sold phase two: a <b>real-time AI forecasting module</b>,
live in six weeks, £120,000. He'd seen a mockup Asha had made for an internal demo. He believed, sincerely, it was
“basically done”. The contract was signed on the Friday.</p>
{beat("Monday 2 October · the discovery")}
<p>Pip read the contract on Monday. Real-time didn't exist. AI didn't exist, unless you counted a regression model Asha
had built in an afternoon. Six weeks meant 7 November. Asha said, very calmly, that the honest estimate was sixteen
weeks for hourly forecasts, and that real-time needed sensor data Brackenfield didn't collect.</p>
{beat("Tuesday 3 October · the Golem Audit")}
<p>Pip wrote one page: what was promised, what existed, the gap, and three options. He took it to Ruth first. Then to
Felix, who went pale, then defensive, then quiet. Then, with Ruth's backing, to Hamish.</p>
{beat("Wednesday 4 October · the Early Truth")}
<p>Hamish was angry for about four minutes. Then he asked what he'd get. Daily forecasts by 7 November. Hourly by
January. Real-time when Brackenfield installed the sensors. Price unchanged. Hamish, who had been oversold by vendors
before, said: “Nobody's ever told me this in week one. Usually it's week twenty.” He chose all three phases.</p>
{note("A golem made of promises falls apart on delivery day. Unmake it in week one, and you might keep the client.")}""",
        origin=dict(
            title="How Felix came to sell a golem",
            beats=[
                ("2014 · the commission", "Felix starts in sales at a software company. He's paid on contracts signed, not delivered. He's very good at it."),
                ("2020 · the habit", "He learns that clients rarely cancel when delivery slips; they just complain. Overpromising has no cost to him."),
                ("2028 · GridSight", "MetroVolt hires Felix to grow GridSight fast. His bonus is on bookings. Nobody asks delivery to sign off proposals."),
                ("26 September · lunch", "He sees Asha's mockup, believes it's nearly real, and sells it. He isn't lying. He just never asked."),
            ],
            turning="Paying salespeople for promises, and never asking delivery whether the promise was possible.",
            saved="A rule: nothing goes in a proposal without delivery's sign-off. And a bonus that depends on delivery, not just signature.",
            note="Most overpromising isn't dishonesty. It's an incentive that rewards the promise and never meets the delivery.",
        ),
        know=f"""<p>The overpromise golem is a commitment your own side made that you can't keep: a feature that doesn't exist, a date
that can't be met, a result nobody can guarantee. Usually sales made it, sincerely, under pressure. Delivery finds out
when the contract lands.</p>
<h3 class="kh">What it wants</h3>
<p>Nothing. It's a golem: it does what its maker's incentives told it to. Fixing it means changing the incentives.</p>
<h3 class="kh">Why it walks</h3>
<p>Because sales and delivery don't talk before contracts are signed, and because salespeople are rewarded for signing.</p>
<h3 class="kh">What unmakes it</h3>
<ul class="fears"><li>The truth, early.</li><li>Real options, not excuses.</li><li>One voice to the client.</li><li>Delivery sign-off on proposals.</li></ul>
<h3 class="kh">Three kinds of golem</h3>
<div class="breeds">
<div><b>The Optimistic Golem</b><p>Sold in good faith, slightly too big. A replan fixes it.</p></div>
<div><b>The Mockup Golem</b><p>Sold from a demo of something unbuilt. Needs the Early Truth.</p></div>
<div><b>The Fantasy Golem</b><p>Sold knowing it was impossible. Needs the Early Truth and your boss's boss.</p></div>
</div>
{note("Clients forgive a broken promise told early far more readily than one discovered late. Early is everything.")}""",
        difficulty=dict(
            normal=dict(who="The Optimistic Golem.",
                        know=["The promise is a bit too big.", "The date is tight but possible with changes.", "Sales will listen."],
                        do=["Do the Golem Audit.", "Replan with sales.", "Tell the client about any change early."],
                        avoid="The silent march.",
                        next="If what was sold doesn't exist, you're at Nightmare."),
            nightmare=dict(who="The Mockup Golem.",
                           know=["The feature doesn't exist.", "The client saw a demo.", "The date is weeks away."],
                           do=["Golem Audit within days.", "Tell your boss first.", "Go to the client with sales, in one voice, with options.", "Agree the Sales–Delivery Seal."],
                           avoid="Blaming sales to the client.",
                           next="If sales refuses to admit it, you're at Hell."),
            hell=dict(who="The Fantasy Golem, and its maker denies it.",
                      know=["Sales insists it's possible.", "Your boss wants to keep the deal.", "The client is excited."],
                      do=["Write it all down, with dates.", "Escalate to your boss's boss.", "Refuse to fake it.", "Offer the best real alternative."],
                      avoid="Faking it.",
                      next="If you're forced to deliver a lie, think about whether this is where you want to work."),
        ),
        mirror=dict(
            title="Are you the Golem-Maker?",
            intro="Whether you sell to clients or to your own leadership. Tick honestly.",
            signs=["You've promised something before checking it could be done.", "You've shown a mockup without saying it was a mockup.",
                   "You've given a date to please someone.", "You've said “basically done” about something not done.",
                   "You've never asked the person who'll deliver it."],
            cure="Before your next promise, ask the person who'll deliver it: “Can we do this, by then?” Then say what they say.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 4 October 2028, Pip, Felix and Ruth meet Hamish Grant.",
            intro="The Early Truth, with one voice.",
            lines=[
                ("Felix", "Hamish, I need to correct something I told you. I was wrong about what's ready."),
                ("Pip", "Real-time forecasting isn't built. I'm sorry. Here's what we can give you, and when."),
                ("Hamish", "…You're telling me this now? Week one?"),
                ("Pip", "Daily forecasts by 7 November. Hourly by January. Real-time once you've installed sensors. Same price."),
                ("Ruth", "And from now on, nothing goes into a GridSight proposal without delivery's sign-off. That's my commitment."),
                ("Hamish", "Nobody's ever told me this in week one. Usually it's week twenty. Fine. All three phases."),
            ],
            note="Felix asked Pip afterwards to review every proposal. His bonus scheme was changed in January to include delivery. He hated it, then didn't.",
        ),
    ),
    # ------------------------------------------------------------------ the Labyrinth of Procurement
    "procurement-labyrinth": dict(
        sighting=f"""{beat("Thursday 30 November 2028 · the win")}
<p>GridSight won Northshire. Felix popped a bottle of fizzy wine. Pip said they could start in two weeks. Bernard Quill,
from Northshire procurement, sent a polite email the next morning, with attachments.</p>
{beat("December · the forms")}
<p>Fourteen forms. A supplier registration. A modern slavery statement. Two insurance certificates (one of which GridSight,
being six months old, didn't have). A data-protection impact assessment. And a <b>security questionnaire of 412
questions</b>, including “Describe your physical controls for your data centre.” GridSight used MetroVolt's.</p>
{beat("Monday 11 December · the map")}
<p>Pip rang Bernard and asked for the full list of steps, owners and timings. Bernard was delighted: nobody ever asked.
He sent a spreadsheet. Pip ran legal, security and insurance in parallel instead of one after another, and borrowed
MetroVolt's security team's answers for 300 of the 412 questions.</p>
{beat("Wednesday 21 February 2029 · the centre")}
<p>Signed, twelve weeks after the win. Bernard said the average was twenty. Asha saved every answer in a folder called
“The Answer Vault”. The next labyrinth, from Ardmore in April, took five weeks.</p>
{note("Procurement isn't the enemy. It's a maze with a guide. The guide is usually lonely. Ask for the map.")}""",
        origin=dict(
            title="How Northshire's labyrinth was built",
            beats=[
                ("2011 · the first wall", "A public body elsewhere hires a vendor that turns out to have no insurance. Questions about insurance enter every form in the land."),
                ("2017 · the next walls", "A data breach, a modern slavery scandal, a supplier collapse. Each produces a new form. None is removed."),
                ("2023 · the security questionnaire", "A cyber attack on a council. Northshire's questionnaire grows from 40 questions to 412, mostly copied from a national template."),
                ("2028 · the labyrinth", "Every wall was built for a good reason. Together they make a maze that takes twenty weeks to walk through."),
            ],
            turning="Each scandal adding a new form, and nobody ever taking one away.",
            saved="Nothing in Northshire's power; it's national rules. What saves vendors is a map, a guide and a vault.",
            note="Every form in a procurement process exists because something once went badly wrong. Respect that, and fill it in quickly.",
        ),
        know=f"""<p>Procurement is the process a buyer uses to bring a supplier on board: registration, legal terms, security, insurance,
data protection. For public bodies and large firms it can take months. It exists to protect buyers from bad suppliers, so
it treats every supplier as a possible bad one, including you.</p>
<h3 class="kh">What it wants</h3>
<p>Evidence that you're safe: insured, secure, legal and solvent. Not opinions. Evidence.</p>
<h3 class="kh">Why it's slow</h3>
<p>Because steps run one after another, nobody owns the whole path, and every answer is written from scratch.</p>
<h3 class="kh">What speeds it</h3>
<ul class="fears"><li>The full map, up front.</li><li>Parallel paths.</li><li>A vault of reusable answers.</li><li>A friendly guide.</li></ul>
<h3 class="kh">Three kinds of labyrinth</h3>
<div class="breeds">
<div><b>The Simple Maze</b><p>A few forms, a quick sign-off. Fill them in fast.</p></div>
<div><b>The Public Labyrinth</b><p>National rules, many walls. Map, parallel, vault.</p></div>
<div><b>The Endless Labyrinth</b><p>The buyer keeps adding steps. Ask your sponsor in the buyer to push.</p></div>
</div>
{note("Your client's project sponsor wants you to start too. Tell them where you're stuck; they can often unlock it.")}""",
        difficulty=dict(
            normal=dict(who="The Simple Maze.",
                        know=["A short list of forms.", "A clear owner.", "A reasonable timeline."],
                        do=["Fill everything in within a week.", "Confirm receipt of each.", "Start the Answer Vault."],
                        avoid="The sequential shuffle.",
                        next="If it's dozens of steps over months, you're at Nightmare."),
            nightmare=dict(who="The Public Labyrinth.",
                           know=["Many forms, several teams.", "Security, legal and insurance all involved.", "No visible end."],
                           do=["Ask for the full map.", "Run paths in parallel.", "Track weekly with the procurement officer.", "Borrow answers from your wider company."],
                           avoid="Cursing the guide.",
                           next="If new steps keep appearing, you're at Hell."),
            hell=dict(who="The Endless Labyrinth.",
                      know=["Steps keep being added.", "Nobody can say what's left.", "The project is months late before it starts."],
                      do=["Ask your client sponsor to intervene.", "Get a letter of intent if they want you to start.", "Agree a date for signature, in writing.", "Know your walk-away point."],
                      avoid="Starting without signature.",
                      next="If it never ends, it may be a no in disguise. Ask directly."),
        ),
        mirror=dict(
            title="Are you building a labyrinth?",
            intro="If you've ever made other people fill in forms. Tick honestly.",
            signs=["You've added a step to a process and never removed one.", "You can't say how long your own process takes, end to end.",
                   "You ask suppliers questions you never read the answers to.", "You run steps one after another by habit.",
                   "You've never asked a supplier how your process felt."],
            cure="Pick one form you own. Ask what would happen if it disappeared. If the answer is “nothing”, remove it.",
        ),
        rehearsal=dict(
            title="Scene: Monday 11 December 2028, Pip rings Bernard Quill.",
            intro="The Map Request.",
            lines=[
                ("Pip", "Bernard, could you send me every step between now and signature, with who owns each one? I'll keep a tracker."),
                ("Bernard", "…Nobody's ever asked me that. Yes. Give me an hour."),
                ("Pip", "And can legal, security and insurance run at the same time?"),
                ("Bernard", "They can. Vendors usually do them one by one, then complain it's slow."),
                ("Pip", "We'd like to be the other kind. Weekly check-in, fifteen minutes?"),
                ("Bernard", "Thursdays. I'll bring biscuits."),
            ],
            note="Bernard and Sven, it later emerged, buy biscuits from the same shop. Pip did not pursue this.",
        ),
    ),
    # ------------------------------------------------------------------ the Escalation Summoning
    "escalation-summoning": dict(
        sighting=f"""{beat("Monday 16 October 2028 · 07:04")}
<p>Gavin's email arrived in Dame Helena's inbox, copying Ruth, Pip, Felix, Nadia and two councillors. Subject:
<b>“Unacceptable.”</b> The housing layer, approved on 3 October, had slipped nine days, because highways had reopened
it before Nadia was named owner. Gavin was presenting it to councillors that Thursday.</p>
{beat("07:12 · Ruth and Pip")}
<p>Ruth read it on the train. She wasn't surprised. Pip had told her, the previous Wednesday, that Gavin was unhappy about
the slip and might escalate. She'd already told Dame Helena's office there was a delay, why, and what they were doing.
The No-Surprise Rule had been followed. The summoning arrived; the CEO had been pre-warned.</p>
{beat("07:30 to 10:45 · the Calm Reply")}
<p>Pip drafted. Ruth cut it from 600 words to 140. No defence, no blame of highways. Acknowledge, facts, plan, owner:
“You're right that we missed the date. Here's what happened. You'll have the housing layer on Wednesday, before your
Thursday meeting. Pip will call you at noon.” Sent at 10:45.</p>
{beat("11:02 · the reply from the summoned")}
<p>Dame Helena replied all: “Thank you, Gavin, for raising this. Ruth has it in hand.” Seven words, to everyone. Gavin
rang Pip at noon, calmer. On Wednesday he got the layer. In November they agreed an escalation path: Pip, then Ruth,
then, if all else failed, Dame Helena. He never needed it again.</p>
{note("An escalation is a client shouting that they weren't heard. Answer the shout, then fix the hearing.")}""",
        origin=dict(
            title="How Gavin learned to summon CEOs",
            beats=[
                ("2019 · the consultants again", "Wexley's failed climate-plan vendor ignored Gavin for months. He emailed their CEO. The next day, everything moved."),
                ("The lesson", "Gavin learns that CEOs make things happen. He doesn't learn that it also makes enemies."),
                ("2028 · the slip", "The housing layer slips, through nobody's fault in particular. Gavin has a councillors' meeting on Thursday and a director watching."),
                ("16 October · the summoning", "He reaches for the tool that worked in 2019. Copying the CEO is the fastest way he knows to feel heard."),
            ],
            turning="An escalation that worked once, against a vendor that truly deserved it, becoming a habit.",
            saved="An agreed escalation path at the start of the contract, so Gavin knew who to go to before the CEO.",
            note="Clients escalate when they don't trust the normal route. Give them a route they trust.",
        ),
        know=f"""<p>An escalation over your head is when a client (or colleague) goes to your boss, or your boss's boss, instead of you.
It's alarming, but it's usually a sign that they felt unheard, or that they'd learned from someone else that it works.
How you respond in the first few hours matters far more than the original problem.</p>
<h3 class="kh">What it wants</h3>
<p>Action, fast. And proof that someone powerful has noticed.</p>
<h3 class="kh">Why it summons</h3>
<p>Because the normal route felt slow or deaf, or because it worked last time with another vendor.</p>
<h3 class="kh">What dispels it</h3>
<ul class="fears"><li>A boss who already knew.</li><li>A same-day, short, calm reply.</li><li>A named owner and a date.</li><li>An escalation path for next time.</li></ul>
<h3 class="kh">Three kinds of summoning</h3>
<div class="breeds">
<div><b>The Frightened Summoning</b><p>A worried client under pressure. Calm, fast, fixed.</p></div>
<div><b>The Habitual Summoning</b><p>They do it to everyone. Agree a path, and hold it.</p></div>
<div><b>The Political Summoning</b><p>Someone using the escalation to make a point internally. Facts, and your boss beside you.</p></div>
</div>
{note("The best response to an escalation is short. The CEO wants to know it's handled, not why it happened.")}""",
        difficulty=dict(
            normal=dict(who="The Frightened Summoning, pre-warned.",
                        know=["Your boss knew already.", "The problem is real but fixable.", "The client is anxious, not hostile."],
                        do=["Reply the same day.", "Acknowledge, facts, plan, owner.", "Call them, don't just email."],
                        avoid="The defensive essay.",
                        next="If your boss heard it first from the CEO, you're at Nightmare."),
            nightmare=dict(who="The surprise summoning.",
                           know=["Your boss didn't know.", "The CEO asked your boss what's going on.", "You're now explaining twice."],
                           do=["Tell your boss everything, immediately.", "Draft the Calm Reply together.", "Apologise to your boss for the surprise.", "Start the No-Surprise Rule today."],
                           avoid="The hidden problem.",
                           next="If the client is doing it to make a point, you're at Hell."),
            hell=dict(who="The Political Summoning.",
                      know=["The escalation is part of their internal fight.", "The facts don't really matter to them.", "Your CEO may know their CEO."],
                      do=["Stick strictly to facts.", "Keep your boss in front.", "Never counter-escalate.", "Agree a path in writing afterwards."],
                      avoid="The counter-summoning.",
                      next="If it repeats, read Banishing a Client."),
        ),
        mirror=dict(
            title="Are you a Summoner?",
            intro="Have you gone over someone's head? Tick honestly.",
            signs=["You've copied someone's boss to make them move faster.", "You've escalated before talking to the person directly.",
                   "You've written “unacceptable” in a subject line.", "You don't know the normal route for escalating with a supplier.",
                   "You felt good after the escalation, and didn't check how they felt."],
            cure="Before your next escalation, talk to the person first: “I'm worried about X; if it doesn't change by Friday, I'll need to involve your manager.” Then they get a chance.",
        ),
        rehearsal=dict(
            title="Scene: Monday 16 October 2028, 07:20, Ruth and Pip on the phone.",
            intro="The Calm Reply, cut to the bone.",
            lines=[
                ("Pip", "I've drafted a reply. It explains highways, the reopened decision, the steering group…"),
                ("Ruth", "How long is it?"),
                ("Pip", "Six hundred words."),
                ("Ruth", "Make it a hundred and forty. He's right we missed the date. Say that first. Then when he'll have it, and when you'll call."),
                ("Pip", "And highways?"),
                ("Ruth", "Not today. Today he needs to feel heard. We fix the hydra next week."),
            ],
            note="Dame Helena's seven-word reply was, Ruth said, the best feedback GridSight got all year.",
        ),
    ),
    # ------------------------------------------------------------------ Banishing a Client
    "banishing-client": dict(
        sighting=f"""{beat("August 2028 · the signing")}
<p><b>Castellan Homes</b>, a property developer, hired GridSight for grid-connection studies on new estates. Rex
Dunmore, their managing director, was charming to Felix, generous with lunches and very keen on discounts. The contract
was £90,000 a year.</p>
{beat("Autumn · the cost")}
<p>Castellan paid every invoice at 75 days on 30-day terms. Rex wanted calls at short notice and changes for free. With
Pip he was charming. With Asha he was not: he interrupted her, called her “the girl with the spreadsheet”, and on
<b>Thursday 11 January 2029</b> shouted at her on a call because a substation's capacity was lower than he'd hoped.</p>
{beat("January · the True Cost Ritual")}
<p>Asha told Pip, shaking. Pip told Ruth the same day. Then he counted: 410 hours of work for £90,000 in fees, minus
write-offs for free changes, meant GridSight was losing about <b>£11,000 a year</b> on Castellan. Plus Asha's
evenings. Plus two projects they'd turned down for lack of time. Felix argued for keeping them: “Revenue is revenue.”
Ruth didn't agree.</p>
{beat("24 January to 31 March · the banishing")}
<p>Ruth and Pip gave Rex the Last Warning, in person and in writing: how the team is spoken to must change, and invoices
paid in 30 days, or GridSight would end the contract on 31 March. Rex laughed. On 1 February he shouted at Asha again.
Ruth sent formal notice that afternoon. GridSight delivered every outstanding study, sent a full handover pack and a list
of three other firms, and left on 31 March. Asha breathed out. The two turned-down projects were won in April.</p>
{note("You can't choose your coworkers. You can choose your clients. And your team is watching which ones you choose.")}""",
        origin=dict(
            title="How Rex became a client worth banishing",
            beats=[
                ("1990s · the builder", "Rex builds his firm from nothing, by squeezing every supplier. It works. Margins are thin; he takes them from others."),
                ("2010s · the reputation", "Castellan becomes known for paying late and shouting. Good suppliers stop bidding. Rex hires the ones who'll put up with it."),
                ("2028 · the new vendor", "GridSight is new and wants revenue. Felix, on commission, signs Castellan without asking anyone who'd worked with them."),
                ("2029 · the pattern", "Rex treats GridSight as he's treated every supplier for thirty years. Charm upwards, contempt downwards, payment late."),
            ],
            turning="Rex learning, decades ago, that suppliers would tolerate anything for revenue. Most did.",
            saved="One reference call before signing. Three of Castellan's former suppliers would have told GridSight everything.",
            note="Clients who abuse suppliers have usually done it for years. Ask around before you sign.",
        ),
        know=f"""<p>Some clients cost more than they bring: in money, once you count all the hours; in stress; in the work you turn
down to serve them; and in how your team feels about you for putting up with it. Ending a client relationship is hard,
but sometimes it's the most important thing a leader can do.</p>
<h3 class="kh">What it wants</h3>
<p>More for less, always, and someone to blame. It's rarely personal; it's how it treats everyone.</p>
<h3 class="kh">Why it's tolerated</h3>
<p>Because revenue is visible and cost is hidden. Nobody counts the hours, the stress or the projects turned away.</p>
<h3 class="kh">What banishes it</h3>
<ul class="fears"><li>The true cost, written down.</li><li>A clear, fair warning.</li><li>A clean, professional exit.</li><li>A team that sees you choose them.</li></ul>
<h3 class="kh">Three kinds of client to consider banishing</h3>
<div class="breeds">
<div><b>The Unprofitable</b><p>Pleasant, but you lose money. Reprice, or part ways kindly.</p></div>
<div><b>The Draining</b><p>Profitable, but exhausting. Reset expectations, then decide.</p></div>
<div><b>The Abusive</b><p>Treats your people badly. One warning, then go.</p></div>
</div>
{note("Ending a client is not unprofessional. Ending it badly is. Give notice, finish what you owe, hand over cleanly.")}""",
        difficulty=dict(
            normal=dict(who="The Unprofitable client.",
                        know=["They're pleasant.", "The numbers don't work.", "They might accept a price rise."],
                        do=["Do the True Cost Ritual.", "Propose a new price or scope.", "If they decline, part ways warmly."],
                        avoid="The endless endurance.",
                        next="If they're exhausting your team, you're at Nightmare."),
            nightmare=dict(who="The Draining client.",
                           know=["Constant demands and changes.", "Late payment.", "Your team avoids their calls."],
                           do=["Count the true cost.", "Reset the rules: rhythm, change log, payment.", "Give a deadline for change.", "Take their calls yourself meanwhile."],
                           avoid="The rage quit.",
                           next="If they mistreat your people, you're at Hell."),
            hell=dict(who="The Abusive client.",
                      know=["They shout at or belittle your staff.", "They're charming to you.", "Someone senior wants to keep them."],
                      do=["Believe your team, and say so.", "Give one clear warning, in writing.", "If it happens again, give notice.", "Exit cleanly: deliver, hand over, leave."],
                      avoid="Sacrificing the team.",
                      next="Afterwards, tell your team what you did and why."),
        ),
        mirror=dict(
            title="Are you a client worth banishing?",
            intro="To your suppliers, agencies or internal service teams. Tick honestly.",
            signs=["You've been sharper with a supplier's junior staff than with their boss.", "You pay suppliers late because you can.",
                   "You expect changes for free.", "Suppliers stopped bidding for your work and you didn't ask why.",
                   "You think suppliers should be grateful for the work."],
            cure="Ask a supplier you work with: “What's it like working with us?” Then listen. The good ones are choosing their clients too.",
        ),
        rehearsal=dict(
            title="Scene: Wednesday 24 January 2029, Ruth and Pip meet Rex Dunmore.",
            intro="The Last Warning, then the Clean Exit.",
            lines=[
                ("Ruth", "Rex, we value the work. But two things have to change. How our team is spoken to, and invoices paid in 30 days."),
                ("Rex", "Is this about the girl with the spreadsheet? She needs a thicker skin."),
                ("Pip", "Her name's Asha. She's the reason your studies are right. It's about how she's spoken to."),
                ("Rex", "I've treated suppliers this way for thirty years."),
                ("Ruth", "Then I'll be clear. If it happens again, we'll end our work on 31 March, with a full handover. I'll put that in writing today."),
                ("Rex", "You won't. Nobody does."),
            ],
            note="It happened again on 1 February. Ruth sent notice that afternoon. Asha heard about it from Pip, in person, before anyone else.",
        ),
    ),
}
