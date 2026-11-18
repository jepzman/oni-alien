# Series 4 · Act V · the long-form story fields, merged into content/darkside/act-5.py by scripts/grimoire.py.
# Spring and summer 2027: Project Horizon. Pip in Customer Ops (since 1 April) under Priya.

def beat(when):
    return f'<p class="beat"><span>{when}</span></p>'


STORY = {
    # ------------------------------------------------------------------ Reading the Omens
    "reading-the-omens": dict(
        sighting=f"""{beat("Monday 1 February · the off-site")}
<p>The leadership off-site in March was “postponed”. The Christmas party had already been “simplified” to drinks.
Nobody connected the two, except the Chronicler, who wrote both in a notebook.</p>
{beat("Monday 15 February · reception")}
<p>Six people with long-term visitor badges arrived on floor 27. Their lanyards said <i>Vexmoor Consulting</i>. They
were polite, wore excellent shoes and booked meeting rooms for eight weeks.</p>
{beat("Friday 26 February · the all-hands")}
<p>Asked about rumours, Dame Helena said there were “no plans to make large-scale changes at this time”. The Chronicler
underlined three words: <i>no plans to</i>, <i>large-scale</i>, <i>at this time</i>.</p>
{beat("Tuesday 9 March · the room")}
<p>Tamsin booked the biggest room on the ground floor for the first week of June: <i>HR, all day</i>. She said nothing.
Her face said everything. Pip, who was about to accept Priya's offer, noticed. He accepted anyway, and updated his CV the
same evening.</p>
{note("Famines are rarely a surprise. Every one of these signals was visible three months before the announcement. Write them down; the pattern is obvious on paper.")}""",
        origin=dict(
            title="How MetroVolt learned to read the sky",
            beats=[
                ("2017 · the layoffs", "MetroVolt cuts 300 jobs. Staff read about it in the newspaper two hours before the internal email (see Act I, the Rumour Mill)."),
                ("2017 · the post-mortem nobody wrote", "Afterwards, people compare notes. Every sign had been there: cancelled events, consultants, room bookings, careful phrasing. Nobody had put them together."),
                ("2018 to 2026 · the folk wisdom", "Long-serving staff quietly learn the signs and teach them to friends. The Chronicler keeps a list in a notebook, updated after each reorg."),
                ("2027 · the signs return", "When Horizon comes, the signs are exactly the same as in 2017. Only the newcomers don't know how to read them."),
            ],
            turning="A layoff where everyone saw the signs separately and nobody saw them together.",
            saved="Leaders being honest earlier. Failing that, someone writing the signs down in one place, which is what this entry is for.",
            note="The omens aren't secret. They're just scattered. The Chronicler's notebook was the only place they were ever in one list.",
        ),
        know=f"""<p>Organisations rarely announce cuts without warning. They prepare, and preparation leaves traces: spending
stops, consultants arrive, phrasing changes, rooms get booked. Reading them isn't paranoia. It's buying yourself time.</p>
<h3 class="kh">What the omens are</h3>
<p>Signals of preparation: money being saved, analysis being done, legal processes being planned, and leaders choosing
their words very carefully.</p>
<h3 class="kh">Why they're easy to miss</h3>
<p>Because each one alone has an innocent explanation. Off-sites get postponed. Consultants do all kinds of work. It's the
<b>combination</b>, over a few weeks, that tells you something.</p>
<h3 class="kh">What they don't tell you</h3>
<ul class="fears"><li>Who will be affected.</li><li>How many.</li><li>Whether it's you.</li><li>Exactly when.</li></ul>
<h3 class="kh">Three kinds of omen</h3>
<div class="breeds">
<div><b>The Money Omen</b><p>Spending stops: events, travel, hiring, training.</p></div>
<div><b>The Analysis Omen</b><p>Consultants, “activity analysis”, requests for headcount data.</p></div>
<div><b>The Process Omen</b><p>HR rooms booked, legal advisers visiting, careful phrasing at all-hands.</p></div>
</div>
{note("One omen is weather. Three omens in a month is a forecast. Five is a calendar.")}""",
        difficulty=dict(
            normal=dict(who="A slowdown: one or two money omens.",
                        know=["Spending is being trimmed.", "No consultants, no HR rooms.", "Leaders say “no” plainly."],
                        do=["Note it; don't panic.", "Keep your CV current anyway.", "Make your work's value visible."],
                        avoid="Prophecy by panic: alarming your team over a cancelled party.",
                        next="If analysis omens appear (consultants, headcount requests), you're at Nightmare."),
            nightmare=dict(who="Preparation: money and analysis omens together.",
                           know=["Consultants are on the executive floor.", "Hiring is frozen.", "Leaders say “no plans to”."],
                           do=["Start the Omen Ledger.", "Do the Quiet Preparation: CV, savings, achievements, network.", "Ask your manager a straight question.", "Light the Value Lantern on your work."],
                           avoid="The ostrich: ignoring it because it's frightening.",
                           next="If process omens appear (HR rooms, legal advisers), you're at Hell."),
            hell=dict(who="Imminent: all three kinds of omen.",
                      know=["HR has booked rooms for whole days.", "Legal advisers are visiting.", "Your manager can't meet your eye."],
                      do=["Make sure your go-bag is packed (see the Go-Bag Scroll).", "Learn your rights before the day (see the Day of the Calendar Invite).", "Keep doing good work; it matters for references.", "Look after yourself and your team."],
                      avoid="The early exit stampede: resigning before you know the terms. You may lose pay you're owed.",
                      next="When the invite comes, read the Day of the Calendar Invite before you go in."),
        ),
        mirror=dict(
            title="Are you reading the sky?",
            intro="Most people only look up when it's already raining. Tick honestly.",
            signs=["You'd only notice layoffs coming when they were announced.", "Your CV is more than a year old.", "You've dismissed signals because each one had an innocent explanation.",
                   "You've never asked your manager a straight question about the future.", "You assume it won't be you."],
            cure="Keep a simple list of signals and look at it monthly. And keep your CV current whatever the sky looks like.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 11 March, Pip's last 1:1 with Victor before he moves.",
            intro="The Straight Question: calm, direct, and easy to answer partially.",
            lines=[
                ("Pip", "Victor, I'm hearing a lot of rumours, and there are consultants on 27. Is there anything you can tell me, even if it's “I can't say”?"),
                ("Victor", "…I can't say much. There's a review. Strategy is in scope."),
                ("Pip", "Thank you. That's helpful. Is Customer Ops in scope too?"),
                ("Victor", "Everything's in scope. But Ops has numbers. Strategy has slides."),
                ("Pip", "Understood. I'll make sure the complaint model's numbers are visible before I go."),
                ("", "That evening Pip writes four lines in his Omen Ledger and sends Priya a one-line note about the model's value. In May, it's quoted in her Horizon submission."),
            ],
            note="Victor said almost nothing. “Ops has numbers, Strategy has slides” was the most useful sentence anyone said to Pip all year.",
        ),
    ),
    # ------------------------------------------------------------------ the Hiring Freeze Frost
    "hiring-freeze-frost": dict(
        sighting=f"""{beat("Monday 15 February · the email")}
<p>MetroVolt announced “a temporary pause on external hiring while we review our resourcing needs”. It had no end date.</p>
{beat("Thursday 1 April · Pip's first day")}
<p>Pip arrived in Customer Ops to find a team of three: himself, Asha and Tomasz. There should have been four. The fourth
role, a data engineer, had been approved in January and frozen in February.</p>
{beat("April and May · the absorption")}
<p>The data engineer's work did not freeze. Asha absorbed the data pipelines. Tomasz absorbed the weekly reports. Pip
absorbed the regulator dashboard at 21:00 on Thursdays. The work got done. Nobody upstairs noticed anything was missing,
which was, of course, the problem.</p>
{beat("Monday 7 June")}
<p>The Horizon template asked Pip to list his team. He listed three people. The fourth chair had been frozen so long it
had vanished from the spreadsheet entirely.</p>
{note("A frozen role that's quietly covered doesn't stay frozen. It disappears.")}""",
        origin=dict(
            title="How the frost settled on MetroVolt",
            beats=[
                ("March 2020 · the first freeze", "At the start of the pandemic, MetroVolt pauses all hiring “for three months”. It's sensible. Nobody knows what's coming."),
                ("2021 · the thaw that didn't come", "The freeze is never formally lifted. Hiring restarts by exception, with a director's approval, then a VP's, then a form."),
                ("2022 to 2026 · the habit", "Every vacancy now needs a fight. Managers learn it's easier to absorb the work than to ask. Teams quietly shrink."),
                ("February 2027 · the deep frost", "Horizon begins with a new freeze on top of the old one. The exception process now needs Rupert's signature. He's in London."),
            ],
            turning="A three-month emergency measure that nobody ever officially ended, so it became the culture.",
            saved="An end date on the first freeze. And managers who wrote down, every time, what the empty chair was costing.",
            note="Every freeze is temporary in the email. It's permanent in the spreadsheet unless someone keeps the empty chair visible.",
        ),
        know=f"""<p>Hiring freezes save money in the short term, often sensibly. The damage comes when they last, and teams quietly
absorb the work. The empty chair disappears, the overwork becomes normal, and the next budget round treats the smaller
team as the right size.</p>
<h3 class="kh">What a freeze is for</h3>
<p>To save money quickly while leaders decide what the organisation needs. It's a pause, in theory, not a plan.</p>
<h3 class="kh">Why the frost spreads</h3>
<p>Because absorbing is easier than asking. Each manager covers one gap; nobody adds up the gaps. From above, everything
looks fine.</p>
<h3 class="kh">What melts it</h3>
<ul class="fears"><li>Written trade-offs.</li><li>Payback numbers for specific roles.</li><li>Priorities agreed with your manager.</li><li>Making the empty chair visible.</li></ul>
<h3 class="kh">Three kinds of frost</h3>
<div class="breeds">
<div><b>The Pause</b><p>Genuinely temporary, with a date. Absorb carefully; track the cost.</p></div>
<div><b>The Drift</b><p>No end date, no review. Make the trade-offs visible now.</p></div>
<div><b>The Prelude</b><p>A freeze before cuts. Your empty chair is the first thing to go.</p></div>
</div>
{note("A freeze is only temporary if someone measures what it's costing.")}""",
        difficulty=dict(
            normal=dict(who="The Pause: a short freeze with an end date.",
                        know=["There's a review date.", "Exceptions are possible.", "Your team is only slightly stretched."],
                        do=["Agree what to pause with your manager.", "Track what the empty role costs.", "Ask for an exception if the payback is clear."],
                        avoid="The silent absorption: covering the gap without telling anyone.",
                        next="If the freeze has no end date, you're at Nightmare."),
            nightmare=dict(who="The Drift: no end date, no review.",
                           know=["The freeze is months old.", "Leavers aren't replaced.", "Your team is working evenings."],
                           do=["Write the Trade-off Scroll and send it.", "Agree a Priority Pact: what stops.", "Put in a Thaw Request for the role with the clearest payback.", "Protect working hours."],
                           avoid="The shadow hire: contractors through a side budget.",
                           next="If the freeze is the prelude to cuts, you're at Hell."),
            hell=dict(who="The Prelude: a freeze before layoffs.",
                      know=["Consultants are counting heads.", "Your empty roles are being removed from plans.", "Exceptions need the parent group's signature."],
                      do=["Make sure your submission shows the true workload, including frozen roles.", "Show what the work is worth in money.", "Re-plan honestly for the team you'll actually have.", "Look after your people's wellbeing."],
                      avoid="The martyr's spread: everyone doing a bit of the missing job, badly.",
                      next="Read the Budget Bloodletting before your submission."),
        ),
        mirror=dict(
            title="Are you feeding the frost?",
            intro="Good managers often make freezes worse. Tick honestly.",
            signs=["You've covered a vacancy without telling your manager what it costs.", "Your team works evenings to cover a frozen role.", "You've stopped asking for exceptions because it's too much hassle.",
                   "Your plan assumes the empty role will be filled “soon”.", "Your headcount sheet no longer shows the frozen role."],
            cure="Write down, this week, what each empty chair is costing. Send it to your manager. A visible gap can be argued for; an invisible one can't.",
        ),
        rehearsal=dict(
            title="Scene: Monday 12 April, Pip's 1:1 with Priya.",
            intro="The Trade-off Scroll and the Priority Pact: make the empty chair visible.",
            lines=[
                ("Pip", "Priya, the data engineer role's frozen. Asha, Tomasz and I are covering it, but it's costing us. Here's a one-page list of what's slipping."),
                ("Priya", "The regulator dashboard is on here."),
                ("Pip", "Yes. I'm doing it on Thursday nights. Of our six commitments, which two do we drop while we're one short?"),
                ("Priya", "Drop the weekly deep-dive and the board appendix. Keep the regulator dashboard; I'll ask for an exception for the role."),
                ("Pip", "Thank you. And I'll keep the frozen role in our headcount sheet so it doesn't disappear."),
                ("", "In June, Pip's Horizon submission shows four roles, one frozen, and what the frozen one costs. It's one of the few submissions that does."),
            ],
            note="The exception was refused. But the empty chair was in the spreadsheet, and that changed the next conversation.",
        ),
    ),
    # ------------------------------------------------------------------ the Budget Bloodletting
    "budget-bloodletting": dict(
        sighting=f"""{beat("Monday 10 May · the template")}
<p>A spreadsheet arrived from Vexmoor: <i>Horizon Zero-Based Budget Template v3</i>. Every team had to justify every pound
of its budget “from zero”, with a column headed <i>Savings Opportunity (%)</i>. The column was mandatory.</p>
{beat("Thursday 20 May · the Customer Ops review, 14:00")}
<p>Priya, Pip, Rupert Thorne, Oliver Thane from Vexmoor and Lena from Finance. Oliver opened with a benchmark:
“Peer utilities run customer analytics with two people.” Pip's team was three. Four, if you counted the frozen chair.</p>
{beat("14:12")}
<p>“What can you give up?” asked Oliver. Pip, who had read Act I, did not answer straight away. He let the silence sit for
four seconds, then put a single page on the table.</p>
{beat("14:20")}
<p>The page showed what the team's £310,000 bought: £1.1 million a year in avoided complaint costs and regulator penalties.
Then three tiers of cuts, and what each one broke. Lena from Finance nodded, very slightly. Rupert looked at his watch;
it was nearly time for the 14:05, which he had already missed.</p>
{note("The first team to volunteer a cut gets the deepest one. The team with a value ledger gets a conversation.")}""",
        origin=dict(
            title="How the bloodletting became a ritual",
            beats=[
                ("2019 · the voluntary rounds", "The CFO introduces voluntary savings rounds (see Act I, Plausible Silence). Volunteers get cut deepest; the silent keep their budgets."),
                ("2021 · the targets", "Finance switches to targets per department: everyone cuts 5%, regardless of size or value. Efficient teams suffer most."),
                ("2025 · zero-based", "Vexmoor sells the parent group “zero-based budgeting”: justify everything from zero, every year. It sounds rigorous. In practice it rewards the best storytellers."),
                ("2027 · Horizon", "Every team at MetroVolt fills in the template. Those with numbers survive better. Those with feelings, and those who volunteer, bleed."),
            ],
            turning="Budget processes that rewarded silence, then size, then storytelling, but never simply value.",
            saved="A process that asked “what is this worth?” before “what can you give up?”. Failing that, teams who answer the first question even when it isn't asked.",
            note="The template asks what you can give up. Answer what you're worth first. Then answer the template.",
        ),
        know=f"""<p>Cost-cutting reviews are designed to find money fast. Reviewers look for teams that can't explain their
value in pounds, volunteers who give things up easily, and duplication. Your defence is <b>value in numbers</b>,
<b>options in tiers</b>, and <b>allies in Finance</b>.</p>
<h3 class="kh">What the reviewers want</h3>
<p>Savings they can defend to the parent group, quickly, with numbers. They're not hunting you; they're hunting a total.</p>
<h3 class="kh">Why some teams bleed more</h3>
<p>Because they describe effort, not value; volunteer cuts in the room; or have no one in Finance who understands what they do.</p>
<h3 class="kh">What protects a budget</h3>
<ul class="fears"><li>A one-line value case in pounds.</li><li>Tiered options with consequences.</li><li>A Finance partner who's seen it before the review.</li><li>Not volunteering in the room.</li></ul>
<h3 class="kh">Three kinds of review</h3>
<div class="breeds">
<div><b>The Trim</b><p>Small, fair cuts across the board. Offer a tier; protect the core.</p></div>
<div><b>The Hunt</b><p>Looking for big savings in a few places. Value ledgers decide who's found.</p></div>
<div><b>The Decree</b><p>The number is decided above. Shape how it lands, not whether.</p></div>
</div>
{note("Bring numbers to a bloodletting. Feelings are what the knife is looking for.")}""",
        difficulty=dict(
            normal=dict(who="The Trim: modest, fair cuts.",
                        know=["Everyone's asked for a small percentage.", "The process is open.", "Finance is reasonable."],
                        do=["Offer the smallest tier with honest consequences.", "Protect the work that creates the most value.", "Thank Finance for the process."],
                        avoid="The padded budget. Credibility is your best asset next year.",
                        next="If reviewers are hunting big savings in a few places, you're at Nightmare."),
            nightmare=dict(who="The Hunt: big savings, in a few places.",
                           know=["Consultants run the reviews.", "Benchmarks are used against teams.", "Some teams will be cut deeply."],
                           do=["Write the Value Ledger: one line, in pounds.", "Offer the Three Tiers.", "See your Finance partner before the review.", "Question benchmarks politely: what's in the peer group?"],
                           avoid="The eager sacrifice in the room.",
                           next="If the number is decided above and your team is the target, you're at Hell."),
            hell=dict(who="The Decree: your cut is decided; only the shape is open.",
                      know=["You're told the number, not asked.", "Roles are included.", "There's little appeal."],
                      do=["Shape how it lands: which work stops, how people are treated.", "Push for redeployment and fair process for anyone affected.", "Record the risks of the cut in writing.", "Look after your team (see the Executioner's Burden)."],
                      avoid="The neighbour's throat: arguing another team should be cut instead.",
                      next="If roles in your team are cut, read the Executioner's Burden before any conversation."),
        ),
        mirror=dict(
            title="Do you bleed easily?",
            intro="Check how you defend your team's resources. Tick honestly.",
            signs=["You describe your team's work as effort, not value.", "You've volunteered savings in a meeting.", "You've never met your Finance partner.",
                   "You couldn't say in one line what your budget buys.", "You've padded a budget to survive a cut."],
            cure="Write one sentence this month: “Our budget of £X buys £Y of value, because Z.” If you can't write it, you've found your homework.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 20 May, 14:12. The Customer Ops review.",
            intro="The Held Pause, the Value Ledger and the Three Tiers.",
            lines=[
                ("Oliver", "Peer utilities run customer analytics with two people. What can you give up?"),
                ("", "Four seconds of silence. Pip counts them."),
                ("Pip", "Before that, one page. Our £310k buys about £1.1 million a year in avoided complaint costs and regulator penalties. The calculation's on the back."),
                ("Oliver", "Benchmarks still suggest two people."),
                ("Pip", "Could you share what the peer teams cover? Ours also runs regulator reporting, which most don't. Here's what 5, 10 and 15% would break."),
                ("Lena", "The regulator reporting isn't in the benchmark, Oliver. I checked."),
                ("", "Customer Ops analytics is cut by 5%: the weekly deep-dive and the board appendix go. The team stays. Pip buys Lena a coffee."),
            ],
            note="Pip didn't argue, plead or volunteer. He brought value, options and an ally. That's the whole spell.",
        ),
    ),
    # ------------------------------------------------------------------ the Curse of More with Less
    "more-with-less": dict(
        sighting=f"""{beat("Monday 6 September · the new year")}
<p>Horizon was done. Customer Operations had lost 12% of its people. The annual targets, published the same morning, were
identical to last year's, except one, which had gone up.</p>
{beat("09:30 · the kick-off")}
<p>Rupert Thorne opened the kick-off with a slide: a lightbulb, and the words <b>Do More With Less</b>. Below it, in
smaller type: <i>Work smarter, together</i>.</p>
{beat("September · the evenings")}
<p>By the third week, Asha was answering emails at 22:00. Tomasz, who had been redeployed to Field Ops, was still being
asked questions about the weekly report he no longer owned. Pip was doing the regulator dashboard on Thursday nights
again.</p>
{beat("Friday 1 October")}
<p>Pip added up the team's hours. They were doing the work of four people with three, using roughly the hours of five.
He looked at the lightbulb slide, which someone had printed and pinned up. Someone else had drawn a small skull on it.</p>
{note("Less is less. Anyone who says otherwise is selling a slide.")}""",
        origin=dict(
            title="How a slide became a curse",
            beats=[
                ("2019 · Rotterdam", "In his famous turnaround, Rupert Thorne cuts a bloated subsidiary by 20% and finds real waste: duplicate teams, unread reports. It works, because the waste was real."),
                ("2019 · the slide", "His closing presentation has a lightbulb and the words “Do More With Less”. The group loves it."),
                ("2020 to 2026 · the slide travels", "The slide appears in every turnaround Rupert leads. The waste isn't always there any more. The slide is."),
                ("2027 · MetroVolt", "After years of freezes, MetroVolt has little real waste left. Horizon cuts people and keeps targets. The slide does the rest."),
            ],
            turning="A true lesson from one place (there was waste) turned into a slogan for every place (there's always waste).",
            saved="Asking, every time, “where is the waste, specifically?” before cutting. Sometimes the answer is “nowhere”, and the right reply is to cut work, not just people.",
            note="Most slogans were true somewhere once. The curse is applying them where they aren't.",
        ),
        know=f"""<p>After cuts, organisations often keep the same targets and hope efficiency fills the gap. Sometimes it does, a
little: there's always some waste. Mostly, the gap is filled by unpaid overtime, until people break. The cure is an
<b>honest re-plan</b>: fewer people means less work, chosen deliberately.</p>
<h3 class="kh">What leaders want</h3>
<p>To keep promises they've made upwards, with the smaller team they now have. They hope the gap will close itself.</p>
<h3 class="kh">Why the curse holds</h3>
<p>Because teams cover the gap with evenings, and from above that looks like efficiency. Nobody adds up the hours.</p>
<h3 class="kh">What breaks it</h3>
<ul class="fears"><li>A written re-plan: deliver, slow, stop.</li><li>Real waste found and cut first.</li><li>Hours made visible.</li><li>Leaders agreeing what stops.</li></ul>
<h3 class="kh">Three kinds of “more with less”</h3>
<div class="breeds">
<div><b>The Genuine</b><p>Real waste exists; cutting it really helps. Find it first.</p></div>
<div><b>The Hopeful</b><p>Leaders hope it'll work out. Re-plan honestly and they'll usually agree.</p></div>
<div><b>The Denial</b><p>Leaders insist targets stay and hours don't count. Escalate the risk in writing.</p></div>
</div>
{note("If the only way to hit the plan is evenings, the plan is wrong. Say so while you still have the energy to.")}""",
        difficulty=dict(
            normal=dict(who="The Genuine: there's real waste to cut.",
                        know=["Reports nobody reads exist.", "Some meetings can go.", "The gap is small."],
                        do=["Run the Efficiency Hunt.", "Cut waste first, visibly.", "Re-plan the rest."],
                        avoid="The heroic fortnight: covering the gap with overtime “just for now”.",
                        next="If the waste is gone and targets haven't moved, you're at Nightmare."),
            nightmare=dict(who="The Hopeful: same targets, fewer people, no plan.",
                           know=["Targets unchanged after cuts.", "Overtime is creeping in.", "Nobody says what stops."],
                           do=["Write the Honest Re-plan: deliver, slow, stop.", "Get it agreed in writing.", "Protect working hours visibly.", "Report risks before they become failures."],
                           avoid="The quiet slide: letting quality drop without telling anyone.",
                           next="If leaders refuse to re-plan, you're at Hell."),
            hell=dict(who="The Denial: targets fixed, hours ignored.",
                      know=["Re-plans are rejected.", "Overtime is expected.", "People are burning out."],
                      do=["Escalate the risk in writing, with numbers.", "Protect your team's wellbeing.", "Raise workload formally if people's health is at risk.", "Decide how long you can sustain it (Act III, the Escape Portal)."],
                      avoid="The smarter slide: repeating “work smarter” to your own team.",
                      next="If people are burning out, it's a health issue. Treat it as one."),
        ),
        mirror=dict(
            title="Are you doing more with less?",
            intro="Check whether you've quietly accepted the curse. Tick honestly.",
            signs=["Your team works more hours than before the cuts.", "Nothing has been formally stopped since the cuts.", "You've said “work smarter” to your team.",
                   "You cover gaps yourself in the evenings.", "Your plan assumes the old capacity."],
            cure="List what your team delivers. Mark one thing to stop. Take it to your manager this week. One agreed stop is worth ten evenings.",
        ),
        rehearsal=dict(
            title="Scene: Friday 1 October. Pip takes the hours to Priya.",
            intro="The Honest Re-plan, with numbers.",
            lines=[
                ("Pip", "Priya, I added up our hours. We're delivering four people's plan with three people, using five people's hours. It won't last."),
                ("Priya", "The targets came from the group."),
                ("Pip", "Understood. Here's a re-plan: we deliver these four, slow these two, and stop the monthly appendix nobody opens. And I've found one real saving: the weekly pack, 30 pages, read by one person."),
                ("Priya", "Who reads it?"),
                ("Pip", "Rupert's assistant, to file it. I asked."),
                ("Priya", "…Stop the pack. I'll take the re-plan to the group with the hours on it."),
                ("", "The group agrees two of the three changes. Asha's 22:00 emails stop by November."),
            ],
            note="Pip did both halves: found real waste (the pack) and was honest about the rest (the re-plan). That's how you break the curse without breaking people.",
        ),
    ),
    # ------------------------------------------------------------------ the Reorg Ritual
    "reorg-ritual": dict(
        sighting=f"""{beat("Monday 12 July · the new structure")}
<p>Horizon's new structure arrived in a 60-slide deck. MetroVolt would now be organised into four <b>Value Streams</b>,
each containing <b>Squads</b>, supported by <b>Chapters</b> and coordinated by a <b>Guild</b>. Nobody at MetroVolt had ever
used any of these words about electricity.</p>
{beat("Wednesday 14 July · the mapping")}
<p>A spreadsheet called <i>Mapping_v4</i> listed every person and their new box. It listed people, not work. Pip's team
was mapped to <i>Customer Value Stream · Insight Squad</i>. The regulator dashboard, which Pip's team produced, was mapped
to nobody.</p>
{beat("July · the Chronicler's notebook")}
<p>The Chronicler added a page: Reorg #8. Previous names for the same work: Customer Analytics (2008), Insight Unit (2012),
Customer Intelligence (2016), Ops Analytics (2021), Customer Analytics again (2024).</p>
{beat("Wednesday 1 September · day one")}
<p>Squads went live. The regulator dashboard was due on the 3rd. Nobody knew whose it was. Pip did, because he had sent a
one-page Work Map in July. It was the only reason the dashboard went out.</p>
{note("Reorgs move boxes. Make sure someone remembers what was inside them.")}""",
        origin=dict(
            title="How the ritual became eight reorgs",
            beats=[
                ("2008 · reorg #1", "A new CEO reorganises MetroVolt into functions. It makes sense. People stay in their seats; their boxes get new names."),
                ("2012 to 2021 · reorgs #2 to #6", "Each new leader brings a new structure. Each one moves the boxes. The work underneath barely changes; only the names do."),
                ("2024 · reorg #7", "Customer Analytics goes back to being called Customer Analytics. The Chronicler laughs for the first time in a year."),
                ("2027 · reorg #8", "Horizon brings Value Streams and Squads from a consultant's playbook. The people designing it have never seen the work they're mapping."),
            ],
            turning="Treating structure as the answer to every problem, so every new leader reached for a new chart.",
            saved="Starting each reorg from the work (what flows where, who depends on what) instead of from the boxes.",
            note="Seven reorgs in nineteen years, and the same work done by the same people each time. Structure matters less than it looks. Work maps matter more.",
        ),
        know=f"""<p>Reorgs change who reports to whom. They rarely change what the work is. The danger is in the gaps: work that
doesn't fit a new box, dependencies nobody mapped, people who lose the manager who understood them. You can shape the
gaps if you speak <b>early</b>, with a <b>map of the work</b>.</p>
<h3 class="kh">What reorg designers want</h3>
<p>A clean structure, delivered on time, that meets the cost target. They don't know your work, and they're short of time.</p>
<h3 class="kh">Why work falls through</h3>
<p>Because mapping spreadsheets list people, not outputs. Anything shared between teams, or done quietly by one person,
is invisible to the designers.</p>
<h3 class="kh">What protects the work</h3>
<ul class="fears"><li>A one-page Work Map sent early.</li><li>Someone from your team in the design sessions.</li><li>A clear landing in writing.</li><li>Naming orphaned work before day one.</li></ul>
<h3 class="kh">Three kinds of reorg</h3>
<div class="breeds">
<div><b>The Rename</b><p>New names, same work. Learn the words; keep doing the job.</p></div>
<div><b>The Reshuffle</b><p>Boxes move, work splits. Map it; catch what falls.</p></div>
<div><b>The Cut in Disguise</b><p>A reorg that removes roles. Read the Famine entries for what comes next.</p></div>
</div>
{note("Learn the new words. Keep the old map. You'll need both.")}""",
        difficulty=dict(
            normal=dict(who="The Rename.",
                        know=["Your manager and work don't change.", "Only names and slides change.", "Nobody's role is at risk."],
                        do=["Learn the new language.", "Update your work map anyway.", "Help colleagues who are confused."],
                        avoid="The name mockery. It's your new team.",
                        next="If work is being split between new boxes, you're at Nightmare."),
            nightmare=dict(who="The Reshuffle: boxes move and work splits.",
                           know=["Mapping lists people, not work.", "Some outputs have no owner in the new structure.", "Your manager may change."],
                           do=["Send the Work Map to the designers early.", "Ask for an Early Voice in your area's design.", "Name orphaned work before day one.", "Get your Clear Landing in writing."],
                           avoid="The box hunt: lobbying for a bigger box instead of a good home for the work.",
                           next="If the reorg removes roles, you're at Hell."),
            hell=dict(who="The Cut in Disguise.",
                      know=["Fewer boxes than people.", "“Selection” is mentioned.", "Consultants run the mapping."],
                      do=["Read the Day of the Calendar Invite and know your rights.", "Make your value visible in numbers.", "Pack your go-bag.", "Support colleagues at risk."],
                      avoid="The old map: carrying on as if nothing happened.",
                      next="Follow the Famine entries in order: omens, go-bag, calendar invite."),
        ),
        mirror=dict(
            title="Do you know what's inside your box?",
            intro="Could you explain your team's work to a stranger designing your future? Tick honestly.",
            signs=["You couldn't list your team's outputs on one page.", "You don't know who depends on your work.", "You've never been involved in a reorg design.",
                   "You've lost work in a previous reorg without noticing.", "You care more about the name than the work."],
            cure="Write your Work Map now: outputs, who uses them, what breaks if they stop. It's useful in every reorg, and in every interview.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 15 July. Pip emails the Horizon design team.",
            intro="The Work Map and the Early Voice.",
            lines=[
                ("Pip", "Before Mapping_v4 is final: here's a one-page view of what Customer Analytics does and who depends on it. Item 3, the regulator dashboard, doesn't have an owner in the new structure."),
                ("Oliver", "Thanks. Which squad should own it?"),
                ("Pip", "Insight Squad, with a named backup in Network Assets. Could someone from our team join the Customer Value design session?"),
                ("Oliver", "Thursday, 10:00. Twenty minutes."),
                ("", "Thursday: Pip shows the map. Two more orphaned outputs are found. Mapping_v5 includes all three."),
            ],
            note="The designers weren't careless. They simply couldn't see the work. One page made it visible.",
        ),
    ),
    # ------------------------------------------------------------------ the Suits from Beyond
    "suits-from-beyond": dict(
        sighting=f"""{beat("Monday 15 February · arrival")}
<p>Six people from Vexmoor Consulting arrived on floor 27. They were polite, worked late and had remarkable shoes. Their
leader, Oliver Thane, spoke a language made almost entirely of nouns: spans, layers, levers, baselines, opportunities.</p>
{beat("Tuesday 30 March · the interview")}
<p>Pip was booked for a “day in the life” interview: 45 minutes with a junior consultant called Bea, who typed everything he
said into a spreadsheet with a column headed <i>Value-add (Y/N)</i>.</p>
{beat("March · the corridor")}
<p>Colleagues compared notes afterwards. Some had used the interview to complain about other teams. Some had exaggerated
their workload. One had refused to say anything at all. Morag had talked for 45 minutes about the 2009 blackout.</p>
{beat("May · the benchmarks")}
<p>Vexmoor's final deck compared every team to “peer utilities”. Most comparisons showed MetroVolt teams as too big. Pip's
had a footnote: <i>scope differs (regulator reporting)</i>. He had told Bea that. She had written it down.</p>
{note("Consultants leave. Their spreadsheets don't. Make sure yours says something true.")}""",
        origin=dict(
            title="How Vexmoor came to MetroVolt",
            beats=[
                ("2012 · the founding", "Three partners leave a big consultancy and start Vexmoor, specialising in “operating model efficiency” for utilities. Their method: benchmark headcount against peers, find gaps, recommend cuts."),
                ("2019 · Rotterdam", "Vexmoor supports Rupert Thorne's Rotterdam turnaround. It's a success. They become the parent group's preferred cost-cutters."),
                ("2021 · the spreadsheet", "Vexmoor's “spans and layers” spreadsheet becomes famous inside the group. It counts managers, layers and people per team. It does not measure what the work is worth."),
                ("2027 · MetroVolt", "Oliver Thane, partner, leads Horizon's analysis. His team has eight weeks, a target and a spreadsheet. Whatever people tell them is all they'll ever know about MetroVolt."),
            ],
            turning="A method that counts people quickly but can't see value, applied by smart strangers on a deadline.",
            saved="Nothing about Vexmoor needs saving. What helps is people inside giving them true, useful, specific information, since that's all they have.",
            note="Most consultants aren't villains. They're clever outsiders with eight weeks. Whatever you tell them becomes the truth about your team.",
        ),
        know=f"""<p>Cost-cutting consultants are hired to find savings quickly. They have little time and no context, so they rely on
benchmarks and interviews. What you say in their interviews becomes, for eight weeks, the official truth about your work.</p>
<h3 class="kh">What they want</h3>
<p>Savings they can defend, fast. Also, quietly, to be right: consultants remember the people who helped them avoid mistakes.</p>
<h3 class="kh">Why they're dangerous</h3>
<p>Because benchmarks compare headcount, not value. And because interviews capture complaints and exaggerations as data.</p>
<h3 class="kh">What helps you with them</h3>
<ul class="fears"><li>A one-page description of your work's value.</li><li>Calm, factual answers.</li><li>Genuinely useful insights about real waste.</li><li>Polite questions about benchmarks.</li></ul>
<h3 class="kh">Three kinds of consultant</h3>
<div class="breeds">
<div><b>The Analyst</b><p>Junior, overworked, typing. Make their spreadsheet accurate.</p></div>
<div><b>The Partner</b><p>Senior, persuasive, protective of the recommendation. Give them evidence, not opinions.</p></div>
<div><b>The Ally</b><p>Rare. Genuinely curious. Help them find the real waste.</p></div>
</div>
{note("Give the consultant something true and useful, and they'll quote you. Give them gossip, and they'll quote that too.")}""",
        difficulty=dict(
            normal=dict(who="A genuine review with open questions.",
                        know=["Interviews are about processes.", "Findings are shared with teams.", "Nothing is pre-decided."],
                        do=["Prepare one page on your work.", "Be the Factual Witness.", "Offer a Useful Insight."],
                        avoid="The stonewall: refusing to engage.",
                        next="If benchmarks are used to justify cuts, you're at Nightmare."),
            nightmare=dict(who="A cost-cutting review with targets.",
                           know=["Benchmarks drive conclusions.", "Interviews feel like audits.", "Teams are compared by size."],
                           do=["Ask the Benchmark Question politely.", "Show your scope, so like is compared with like.", "Put your value in pounds.", "Brief your manager on what you told them."],
                           avoid="The inflation: exaggerating your workload.",
                           next="If the conclusions are decided before the interviews, you're at Hell."),
            hell=dict(who="The decision is made; the review is cover.",
                      know=["The savings number existed before the review.", "Findings are never shared.", "Interviews are a formality."],
                      do=["Stay factual; your words may be quoted later.", "Focus on what you can shape: how cuts land.", "Keep your go-bag packed.", "Look after colleagues."],
                      avoid="The spill: complaining about colleagues. It'll be in a spreadsheet forever.",
                      next="Read the Budget Bloodletting and the Calendar Invite entries."),
        ),
        mirror=dict(
            title="What would the spreadsheet say about you?",
            intro="Imagine a stranger writing down your work in one row. Tick honestly.",
            signs=["You'd describe your work as busy rather than valuable.", "You'd be tempted to criticise another team.", "You don't know your work's value in pounds.",
                   "You'd exaggerate a little, just in case.", "You'd say nothing, hoping to stay invisible."],
            cure="Write your one row now: what you produce, who uses it, what it's worth. Practise saying it in two sentences. It's your answer to every consultant, and every interview.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 30 March, 14:00. Pip's “day in the life” with Bea.",
            intro="The Factual Witness and the Useful Insight.",
            lines=[
                ("Bea", "Could you walk me through a typical week?"),
                ("Pip", "Our main output is the complaint model. It feeds the regulator report and cut repeat calls by 9% last year, about £410k. I've put it on one page for you."),
                ("Bea", "Thank you. That's… unusually helpful."),
                ("Pip", "One more thing that might be useful: the biggest waste I've seen isn't in our team. Three teams count transformers differently. Fixing that would save real money."),
                ("Bea", "Can I quote you on that?"),
                ("Pip", "Please. And one note for your benchmark: we do regulator reporting, which most peer teams don't."),
                ("", "May: Vexmoor's final deck recommends unifying asset data. It credits “an interviewee in Customer Ops”. Pip's team has a footnote."),
            ],
            note="Pip gave the consultant two true, useful things. Both ended up in the final deck, one of them protecting his team.",
        ),
    ),
    # ------------------------------------------------------------------ the Day of the Calendar Invite
    "calendar-invite": dict(
        sighting=f"""{beat("Monday 2 June · 17:12 · the invite")}
<p>Marcus Bell, Head of Grid Planning, 23 years at MetroVolt, received an invite for Tuesday at 10:00: <i>Quick catch-up</i>,
15 minutes, room 4B, ground floor, with Rupert Thorne and someone called Karen from HR. Marcus had never been to room 4B.
Nobody he knew had ever been to room 4B.</p>
{beat("Tuesday 3 June · 09:40")}
<p>Marcus's system access stopped working. He told himself it was IT.</p>
{beat("10:00 · room 4B")}
<p>A glass of water. A box of tissues. An envelope. Rupert said “this is a difficult conversation” and then read from a
page. Marcus's role was at risk of redundancy as part of Horizon. Karen explained the consultation process. Marcus nodded
throughout, because nodding was what he had always done.</p>
{beat("10:14")}
<p>Karen slid a settlement agreement across the table and said it would be “simplest for everyone” if he signed today.
Marcus picked up the pen. Then he remembered something Pip had once forwarded him from this book, and put it down.</p>
{note("The meeting is fifteen minutes. The decisions you make in the next fifteen days matter far more. Don't make them in the room.")}""",
        origin=dict(
            title="How the fifteen-minute meeting was designed",
            beats=[
                ("2017 · the first big layoff", "MetroVolt's 2017 cuts go badly: a press leak, angry scenes, a tribunal claim. Lawyers are brought in to design “a safe process”."),
                ("2017 · the script", "The process they design is legally careful and humanly cold: short invites, neutral rooms, a script, HR present, access removed the same morning, a settlement offered at once."),
                ("2018 to 2026 · the template", "The process is never revisited. Managers aren't trained in it; they're handed it. Rupert reads from the page because he was given the page."),
                ("June 2027 · room 4B", "Marcus, who has run Grid Planning kindly for twelve years, walks into a process designed to minimise risk to the company, not harm to him. He doesn't know that he can slow it down."),
            ],
            turning="A process designed by lawyers to protect the company, which nobody ever redesigned to also protect people.",
            saved="A process with a human at its centre: a manager who knows the person, time to digest, advice offered, no pressure to sign. And Marcus knowing his rights before the day.",
            note="The script isn't evil. It's just designed for the company's safety, not yours. Your safety is your job: slow it down, get advice, sign nothing in the room.",
        ),
        know=f"""<p>Redundancy meetings are usually short, scripted and designed to be legally safe for the company. You're not
expected to respond on the day, and in most places you <b>don't have to sign anything on the day</b>. What you're owed
depends on your country, contract and length of service.</p>
<h3 class="kh">What the company wants</h3>
<p>A clean, quick, legally safe process, and ideally a signed settlement, which usually means you give up the right to make claims.</p>
<h3 class="kh">Why people sign too fast</h3>
<p>Shock, shame, and the wish for it to be over. And because the agreement is presented as “simplest for everyone”.</p>
<h3 class="kh">What protects you</h3>
<ul class="fears"><li>Taking everything away to read.</li><li>Independent advice (in some countries the company must pay for it).</li><li>Asking about notice, pay, pension, benefits, criteria, redeployment and references.</li><li>Your own records and contacts, never company data.</li></ul>
<h3 class="kh">Three kinds of day</h3>
<div class="breeds">
<div><b>The Consultation</b><p>“At risk”, with a process and time. Use the time.</p></div>
<div><b>The Offer</b><p>A settlement on the table. Never sign it in the room.</p></div>
<div><b>The Escort</b><p>Same-day exit, access cut. Stay calm; everything else can follow by email.</p></div>
</div>
{note("Nod if you must. Sign nothing. Ask for it in writing. Leave. Then call someone who knows employment law.")}""",
        difficulty=dict(
            normal=dict(who="The Consultation: a fair process with time.",
                        know=["You're “at risk”, not dismissed.", "There's a consultation period.", "Redeployment is offered."],
                        do=["Ask for everything in writing.", "Use the consultation: ask about criteria and alternatives.", "Apply for redeployment roles seriously.", "Get advice before agreeing anything."],
                        avoid="The scene. Your reference matters more than your exit line.",
                        next="If you're pushed to sign a settlement on the day, you're at Nightmare."),
            nightmare=dict(who="The Offer: pressure to sign quickly.",
                           know=["A settlement is offered in the meeting.", "You're told today's terms expire soon.", "HR says it's “simplest for everyone”."],
                           do=["Say you won't sign today, and ask the deadline.", "Get independent legal advice.", "Use the Question List.", "Negotiate: notice, pay, reference wording, timing."],
                           avoid="The instant signature.",
                           next="If the process feels unfair or discriminatory, you're at Hell."),
            hell=dict(who="The Escort, or an unfair process.",
                      know=["You're escorted out the same day.", "The selection looks unfair or targeted.", "You weren't consulted at all."],
                      do=["Stay calm and leave with dignity.", "Write down everything that happened, the same day.", "Get advice quickly; claims often have short time limits.", "Contact a union or advice service."],
                      avoid="The data heist. It can cost you your severance and your case.",
                      next="Look after yourself. Talk to people. This is a loss, and it's OK to treat it as one."),
        ),
        mirror=dict(
            title="Would you be ready?",
            intro="Nobody wants to read this entry. Tick honestly anyway.",
            signs=["You don't know your notice period or redundancy terms.", "You don't know whether your company would pay for legal advice.", "You'd sign whatever you were given to make it stop.",
                   "Your contacts live only in your work phone.", "You've never written down your achievements."],
            cure="Spend one hour this month: find your contract, note your notice and terms, save your personal contacts, and write your achievements list. You'll probably never need it. If you do, you'll be glad.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 3 June, 10:14, room 4B. Marcus puts the pen down.",
            intro="The Calm Witness and the Unsigned Scroll.",
            lines=[
                ("Karen", "It would be simplest for everyone if you signed today."),
                ("Marcus", "Thank you for telling me. I'm not going to sign anything today. When do you need my response by?"),
                ("Karen", "…The offer is open for two weeks."),
                ("Marcus", "Could I have all of this in writing, please? And the selection criteria, and details of any redeployment roles?"),
                ("Rupert", "Of course."),
                ("Marcus", "One more question: what reference will MetroVolt give?"),
                ("", "Marcus takes the envelope home. A lawyer, paid for by MetroVolt, gets him three more months' pay and an agreed reference. Pip writes him a LinkedIn recommendation the same week."),
            ],
            note="Marcus said almost nothing in the room. That was exactly right. Everything that mattered happened in the following two weeks.",
        ),
    ),
    # ------------------------------------------------------------------ the Executioner's Burden
    "executioners-burden": dict(
        sighting=f"""{beat("Friday 28 May · the decision")}
<p>Horizon's final structure for Customer Ops had one fewer analyst role. Priya fought it and lost. Pip had to choose,
using the published criteria, between Asha and Tomasz. The criteria pointed to Tomasz's role: it overlapped most with
work moving to Field Ops.</p>
{beat("Weekend · rehearsing")}
<p>Pip wrote four versions of what to say. All of them started with twenty minutes about the weather. He threw them away.</p>
{beat("Tuesday 1 June · 09:30 · the meeting")}
<p>HR had given Pip a script. It said “as you know, the organisation is going through a period of change”. Pip noticed it
took three paragraphs to reach the news.</p>
{beat("09:31")}
<p>Pip put the script down and said it in the first minute. Tomasz went very still. Then he asked about his children's
school fees. Pip didn't know the answer, said so, and wrote the question down. The meeting took forty minutes. Most of it
was silence. Pip let it be silence.</p>
{note("You can't make it painless. You can make it clear, kind and fast. That's the job.")}""",
        origin=dict(
            title="How managers learn to deliver bad news (they don't)",
            beats=[
                ("2017 · Gareth's first time", "Gareth, newly promoted, has to tell six engineers their roles are going. He's given a script and no training. He reads it, word for word, to each of them. Two cry. One never speaks to him again."),
                ("2017 · the lesson nobody shared", "Gareth learns, badly, what works: say it early, stop talking, help practically. He never tells anyone. Nobody asks."),
                ("2018 to 2026 · the scripts", "Every manager facing cuts gets the same script and no training. Each learns alone, usually by getting it wrong the first time."),
                ("2027 · Pip", "Pip, five weeks into his first management role, is handed the script. He has read this book. That's the only training he gets."),
            ],
            turning="Scripts handed out instead of skills taught, so every manager's first time is someone else's worst day.",
            saved="One afternoon of training. Or Gareth, in 2017, writing down what he learned and passing it on.",
            note="If you've had to do this, write down what you learned and give it to the next manager. It's the most useful thing nobody will ask you for.",
        ),
        know=f"""<p>Delivering redundancy news is one of the hardest things a manager does. The person will remember the conversation
for years: not the words, but whether they were treated with clarity and respect. The essentials are simple: <b>say it
early</b>, <b>stop talking</b>, <b>help practically</b>, <b>don't promise what you can't control</b>.</p>
<h3 class="kh">What the person needs</h3>
<p>To hear it clearly, to be given time to react, to know what happens next, and to be treated as a person, not a line in Horizon.</p>
<h3 class="kh">Why managers get it wrong</h3>
<p>Because they're frightened, so they delay. Because they want to be liked, so they promise. Because they feel guilty, so they talk about themselves.</p>
<h3 class="kh">What makes it bearable</h3>
<ul class="fears"><li>The news in the first minute.</li><li>Silence, allowed.</li><li>Facts in writing and next steps.</li><li>Real help: references, introductions, time.</li></ul>
<h3 class="kh">Three kinds of executioner</h3>
<div class="breeds">
<div><b>The Reader</b><p>Reads the script and hides behind it. Feels safe; lands cold.</p></div>
<div><b>The Apologiser</b><p>Makes it about their own pain. Feels kind; lands wrong.</p></div>
<div><b>The Steady</b><p>Clear, quiet, practical. Feels hard; lands with dignity.</p></div>
</div>
{note("Say the sentence you're dreading first. Everything after it is easier, for both of you.")}""",
        difficulty=dict(
            normal=dict(who="A fair process, and a person who may find another role.",
                        know=["There's consultation and redeployment.", "The criteria are clear.", "You can help practically."],
                        do=["Say it in the first minute.", "Let them react.", "Give facts in writing and next steps.", "Offer references and introductions."],
                        avoid="The long lead-in.",
                        next="If you disagree with the decision, you're at Nightmare."),
            nightmare=dict(who="You disagree with the decision you must deliver.",
                           know=["You argued and lost.", "The criteria aren't how you'd choose.", "You like the person."],
                           do=["Be honest that you argued and lost, without disowning the process.", "Don't suggest unfairness unless you'll say so formally.", "Focus on what you can do now.", "Get support for yourself afterwards."],
                           avoid="False hope: “I'm sure something will come up.”",
                           next="If the process itself seems unfair or unlawful, you're at Hell."),
            hell=dict(who="The process seems unfair, or you're told to do it badly.",
                      know=["Selection looks targeted.", "You're told to deliver it with no notice or support.", "HR wants signatures on the day."],
                      do=["Raise your concerns in writing before the meeting.", "Refuse to pressure anyone to sign on the day.", "Tell the person they can get advice.", "Take care of your own conscience; get advice yourself if needed."],
                      avoid="The self-pity: making it about how hard this is for you.",
                      next="If you're asked to do something wrong, read Act VIII, the Dark Pact."),
        ),
        mirror=dict(
            title="How would you deliver it?",
            intro="If you lead anyone, you may have to one day. Tick honestly.",
            signs=["You'd start with small talk to soften it.", "You'd read the script so you didn't have to find your own words.", "You'd fill the silence with reassurance.",
                   "You'd say “this is really hard for me too”.", "You've never thought about what you'd offer practically."],
            cure="Write the first sentence now, in your own words, and what you'd offer afterwards. Then hope you never need it.",
        ),
        rehearsal=dict(
            title="Scene: Tuesday 1 June, 09:30. Pip, Tomasz, and HR.",
            intro="The First Minute, the Steady Presence, the Practical Help, the Honest Limits.",
            lines=[
                ("Pip", "Tomasz, I've got difficult news, and I want to say it straight. Your role is at risk of redundancy as part of Horizon."),
                ("", "Silence. Pip waits. He does not fill it."),
                ("Tomasz", "…Why mine?"),
                ("Pip", "The criteria looked at overlap with work moving to Field Ops. Your role overlapped most. I argued for both roles and lost. I can't change the decision."),
                ("Tomasz", "What about my kids' school fees? We've just signed for September."),
                ("Pip", "I don't know the answer, and I won't guess. I'll find out today. What I can do: Field Ops are hiring, I'll introduce you to Sam this week, and I'll write you the strongest reference I've ever written."),
                ("", "Tomasz is redeployed to Field Ops in July. He sends Pip a message in December: “Thank you for saying it straight.”"),
            ],
            note="Pip didn't make it painless. He made it clear, honest and practical. Tomasz remembered exactly that.",
        ),
    ),
    # ------------------------------------------------------------------ Survivor's Haunting
    "survivors-haunting": dict(
        sighting=f"""{beat("Monday 2 August · after")}
<p>Horizon was done. 584 people had left MetroVolt. On floor 9, every fourth desk was empty. Some still had things on them:
a mug, a plant, a photograph someone hadn't come back for.</p>
{beat("Marcus's desk")}
<p>Marcus's desk in Grid Planning had his football scarf on the chair. Nobody moved it for three weeks. Nobody could
explain why.</p>
{beat("The team meeting")}
<p>Pip's first team meeting after Horizon began, by habit, with the week's priorities. Asha was looking at Tomasz's empty
chair. Pip stopped, put down his list, and said that this week was hard. Asha cried for a minute, then laughed at herself
for crying, then they talked about Tomasz and Marcus for twenty minutes. Then they talked about the work.</p>
{beat("September · the quiet")}
<p>People who had kept their jobs were quieter, more careful, more tired. Two of them told Pip they felt guilty for being
relieved. One said she was waiting for round two.</p>
{note("The ones who stay have work to do: for the people who left, and for themselves.")}""",
        origin=dict(
            title="How the Chronicler learned about the haunting",
            beats=[
                ("2017 · the first survival", "The Chronicler keeps their job in the 2017 cuts. Their closest colleague doesn't. They feel relief, then shame at the relief."),
                ("2017 · the silence", "Nobody talks about it. Leadership says “let's focus on the future”. Survivors keep their heads down. Productivity drops for a year; nobody connects it to the cuts."),
                ("2018 to 2026 · seven reorgs", "The Chronicler survives every round. Each time, the same guilt, the same silence, the same quiet year afterwards."),
                ("2027 · writing it down", "After Horizon, the Chronicler writes this entry, because nobody told them in 2017 that the haunting was normal, and that it lifts when you name it."),
            ],
            turning="An organisation that told survivors to move on, so nobody was allowed to grieve the people who left.",
            saved="One leader in 2017 saying, “This is hard. People we valued have gone. It's OK to feel that.”",
            note="I've survived seven rounds. The guilt never goes away entirely. It gets lighter every time you help someone who didn't.",
        ),
        know=f"""<p>Layoff survivors often feel guilt, fear and exhaustion: guilt at keeping their jobs, fear of the next round,
exhaustion from absorbing the work of people who left. It's so common it has a name: <b>survivor syndrome</b>. It lifts
faster when it's named, when the people who left are honoured, and when the work is honestly re-planned.</p>
<h3 class="kh">What survivors need</h3>
<p>Permission to feel strange, honesty about what's next, and a workload that fits the team that's left.</p>
<h3 class="kh">Why it lingers</h3>
<p>Because organisations want to “move forward” quickly, and silence lets fear grow. The empty desks speak louder than any memo.</p>
<h3 class="kh">What lifts it</h3>
<ul class="fears"><li>Naming it as a team.</li><li>Marking farewells properly.</li><li>Helping the people who left.</li><li>An honest re-plan of the work.</li></ul>
<h3 class="kh">Three kinds of haunting</h3>
<div class="breeds">
<div><b>The Guilt</b><p>“Why me and not them?” Helping the people who left eases it.</p></div>
<div><b>The Fear</b><p>“Am I next?” Honesty from leaders, and your go-bag, ease it.</p></div>
<div><b>The Weight</b><p>Their work on your desk. Only a re-plan eases it.</p></div>
</div>
{note("Move the scarf when you're ready. Not before. But do, eventually, move the scarf.")}""",
        difficulty=dict(
            normal=dict(who="A team that lost a colleague and feels it.",
                        know=["People are quiet and sad.", "Work continues.", "Leaders acknowledged it."],
                        do=["Name it in the team.", "Mark farewells.", "Check in with each person 1:1."],
                        avoid="The brave face.",
                        next="If fear of the next round is spreading, you're at Nightmare."),
            nightmare=dict(who="Fear and overload after deep cuts.",
                           know=["People expect a round two.", "Work is piling on survivors.", "Leaders say “move forward”."],
                           do=["Ask leaders for honesty about what's next, and pass it on.", "Re-plan the work honestly.", "Help the people who left: references, introductions.", "Encourage people to pack their go-bags; it reduces fear."],
                           avoid="The blame ghost: deciding the leavers were weaker.",
                           next="If people are burning out or deeply distressed, you're at Hell."),
            hell=dict(who="Burnout and distress after repeated rounds.",
                      know=["People are ill, anxious or withdrawn.", "Mistakes are rising.", "Good people are quietly leaving too."],
                      do=["Treat it as a wellbeing issue: point people to support (EAP, doctor).", "Reduce workload formally.", "Escalate the risk to leadership in writing.", "Look after yourself too."],
                      avoid="The bunker: everyone keeping their head down in silence.",
                      next="If you can't recover here, the Escape Portal (Act III) is a legitimate door."),
        ),
        mirror=dict(
            title="Are you haunted?",
            intro="Survivors often don't notice. Tick honestly.",
            signs=["You feel guilty for keeping your job.", "You're waiting for round two.", "You're doing a missing colleague's work without saying so.",
                   "You haven't contacted anyone who left.", "You've stopped speaking up in meetings since the cuts."],
            cure="Message one person who left this week: a reference, an introduction, or just “how are you?”. Then tell your manager one piece of work you can't carry. Both help.",
        ),
        rehearsal=dict(
            title="Scene: Monday 2 August, 09:30. Pip's first team meeting after Horizon.",
            intro="The Naming and the Farewell Rite.",
            lines=[
                ("Pip", "Before we start on priorities: this week is hard. Tomasz and Marcus were good colleagues and good people. It's fine to feel odd about it."),
                ("Asha", "I feel bad that I'm relieved."),
                ("Pip", "Me too. I think everyone who stayed does. It doesn't make us bad people."),
                ("Asha", "Is there going to be a round two?"),
                ("Pip", "I asked Priya. She says no further cuts are planned this year, and she'll tell us straight if that changes. I'll pass on whatever I hear."),
                ("Pip", "We're doing lunch for Tomasz on Friday. And I've written him a LinkedIn recommendation. Want to add one?"),
                ("", "Friday: eleven people come to Tomasz's lunch, including Gareth. On Monday, someone finally moves Marcus's scarf, folds it, and posts it to him."),
            ],
            note="Naming it took two minutes. The team was quicker, kinder and more honest for months afterwards.",
        ),
    ),
    # ------------------------------------------------------------------ the Quiet Culling
    "quiet-culling": dict(
        sighting=f"""{beat("April · the report")}
<p>The weekly outage report, which Morag had written by hand every week since 2009, was “automated to free up her capacity”.
The automated version had her name nowhere on it.</p>
{beat("May · the invites")}
<p>Morag stopped being invited to the operations review. Then to the incident planning group. Her manager said the meetings
had been “streamlined”.</p>
{beat("June · the plan")}
<p>After fifteen years of strong reviews, Morag was given a “performance improvement plan” citing “resistance to new ways of
working”. Her Slack status, for the first time since February 2025, did not say <i>drowning</i>. It said nothing at all.</p>
{beat("July · the coffee")}
<p>Pip, who still had coffee with Morag sometimes, noticed that nobody had told her anything directly. Everything had been
“capacity”, “streamlining” and “new ways of working”. Nobody had said the word they meant.</p>
{note("Quiet things deserve loud questions. Ask early, while there's still a choice.")}""",
        origin=dict(
            title="How MetroVolt learned to cull quietly",
            beats=[
                ("2017 · the bad press", "The 2017 layoffs make the newspapers. Leadership decides never again: future reductions will be “managed” quietly, wherever possible."),
                ("2018 to 2024 · the method", "People who don't fit new plans are sidelined slowly: work moved, invites dropped, performance plans introduced. Many leave on their own. No redundancy costs, no headlines."),
                ("2025 · the target", "Morag's hero status from 2009 makes her hard to cut openly. Her refusal of help (see Act II, the Martyr Banshee) and her single-person knowledge make her look, to Horizon, like a risk."),
                ("2027 · the culling", "Nobody decides to push Morag out in a meeting. It happens through a dozen small decisions, none of which anyone has to defend."),
            ],
            turning="A choice to avoid headlines by making departures look voluntary, which made them harder to see and harder to challenge.",
            saved="A direct conversation, early. If Morag's role was changing, someone owed her the words, and the redundancy terms that come with them.",
            note="Quiet culling saves the company money and saves managers from hard conversations. The cost lands on the person who's never told.",
        ),
        know=f"""<p>Sometimes organisations don't make people redundant; they make them <b>want to leave</b>. Work is moved, invites
stop, a performance process appears. Nobody says the real reason. It's cheaper and quieter than redundancy, and it can,
in some cases, be unlawful.</p>
<h3 class="kh">What the organisation wants</h3>
<p>A departure without redundancy costs, conflict or headlines.</p>
<h3 class="kh">Why it's hard to see</h3>
<p>Because each step has a reasonable explanation. Only the pattern tells you, and it's easy to deny a pattern.</p>
<h3 class="kh">What protects you</h3>
<ul class="fears"><li>A direct question, asked early.</li><li>A dated record of changes.</li><li>Proper advice if it looks like constructive dismissal.</li><li>Options you control.</li></ul>
<h3 class="kh">Three kinds of quiet</h3>
<div class="breeds">
<div><b>The Genuine Change</b><p>Your role really is changing. Ask, and you'll be told.</p></div>
<div><b>The Drift</b><p>Nobody's decided anything; you're just being forgotten. A direct question restarts things.</p></div>
<div><b>The Culling</b><p>A planned push out. Records, advice, and your own exit plan.</p></div>
</div>
{note("If everyone keeps saying “capacity” and “streamlining”, ask what word they actually mean.")}""",
        difficulty=dict(
            normal=dict(who="The Genuine Change, poorly communicated.",
                        know=["Your manager answers when asked.", "There's a new role for you.", "Nothing is hostile."],
                        do=["Ask the Direct Question.", "Agree your new role in writing.", "Ask what support you'll have."],
                        avoid="The denial: waiting six months to ask.",
                        next="If questions get vague answers and work keeps vanishing, you're at Nightmare."),
            nightmare=dict(who="The Drift, or the early culling.",
                           know=["Invites stop; work moves.", "Answers are vague.", "Your manager is suddenly formal."],
                           do=["Ask directly, in writing, what the plan is for your role.", "Keep the Record.", "Talk to your skip-level or HR.", "Prepare your options."],
                           avoid="The overwork rescue: working twice as hard to win it back.",
                           next="If a performance plan appears after years of good reviews, you're at Hell."),
            hell=dict(who="The Culling: a planned push out.",
                      know=["A sudden performance plan.", "Your role is being emptied.", "You're isolated from colleagues."],
                      do=["Get proper advice (union, lawyer): this may be constructive dismissal.", "Respond to any plan in writing, factually.", "Ask whether redundancy is on the table; it may be fairer to you.", "Plan your exit on your terms."],
                      avoid="The hallway campaign: complaining to everyone. It confirms the story.",
                      next="If you leave, negotiate. A quiet culling often has room for a better exit."),
        ),
        mirror=dict(
            title="Are you being culled, or culling?",
            intro="This one has two sides. Tick honestly.",
            signs=["Your projects have been moved “for capacity” this year.", "You're no longer invited to meetings you used to attend.", "Your manager has become formal with you.",
                   "Or: you've sidelined someone rather than telling them the truth.", "Or: you've said “streamlining” when you meant something else."],
            cure="If you're being culled: ask the direct question this week. If you're culling: have the honest conversation. Either way, someone has to say the real word.",
        ),
        rehearsal=dict(
            title="Scene: Thursday 15 July. Morag's 1:1 with her manager, after a coffee with Pip.",
            intro="The Direct Question, asked calmly.",
            lines=[
                ("Morag", "I've noticed my report, my meetings and the incident group have all moved away from me. Can you tell me honestly what the plan is for my role?"),
                ("Manager", "It's about capacity, and new ways of—"),
                ("Morag", "I understand. But in plain words: is my role being phased out?"),
                ("Manager", "…Network Ops is being restructured. Your role isn't in the September structure."),
                ("Morag", "Thank you for saying it. Then I'd like that confirmed in writing, and I'd like to discuss redundancy terms, not a performance plan."),
                ("", "Morag gets advice. The performance plan is withdrawn. She leaves in October with redundancy pay, a reference that mentions 2009, and a job offer from a rival utility's control room."),
            ],
            note="One plain question turned a quiet culling into an honest redundancy, with the money and dignity that come with it.",
        ),
    ),
    # ------------------------------------------------------------------ the Go-Bag Scroll
    "go-bag-scroll": dict(
        sighting=f"""{beat("2008 · the Chronicler's drawer")}
<p>In the 2008 financial crisis, the Chronicler watched colleagues lose jobs with no savings, no CV and no contacts outside
MetroVolt. They went home and packed a go-bag: not a physical one, but close.</p>
{beat("Every spring since")}
<p>Every April, the Chronicler updates a CV, adds the year's achievements to a running list, checks the savings account, and
has coffee with three people outside MetroVolt. It takes one afternoon. They have done it nineteen times.</p>
{beat("Tuesday 9 March 2027 · Pip")}
<p>The night he noticed Tamsin's room booking, Pip updated his CV for the first time since joining MetroVolt in 2022. It took
four hours, because he had to remember five years of achievements from scratch.</p>
{beat("June · Marcus")}
<p>When Marcus was told his role was at risk, he had no CV, no savings buffer and no contacts outside MetroVolt. He had been
loyal for 23 years. It took him five months to find work. He told Pip, afterwards, that the worst part wasn't losing the job.
It was having nothing ready.</p>
{note("The people who survive famines aren't the luckiest. They're the ones who packed.")}""",
        origin=dict(
            title="How the Chronicler learned to pack",
            beats=[
                ("2008 · the crisis", "MetroVolt cuts 150 jobs in the financial crisis. The Chronicler, five years in, keeps their job. Their friend, with twenty years' service and no CV, takes eleven months to find work."),
                ("2008 · the first bag", "The Chronicler writes a CV, a list of achievements, and a list of five people outside MetroVolt. They open a savings account labelled “just in case”."),
                ("2009 to 2026 · the ritual", "Every spring, one afternoon: update, add, check, call. Seven reorgs, three rounds of cuts. The bag is never needed. The Chronicler is calmer than anyone in every one."),
                ("2027 · passing it on", "The Chronicler writes this entry because the bag is the only counter-spell in this Act that works before the famine begins."),
            ],
            turning="Watching a loyal friend with nothing ready take eleven months to recover.",
            saved="Not needed: this is a habit, not a curse. The only thing to save is your future self an awful afternoon.",
            note="I've never used my go-bag. It has still been the most useful thing I've packed in nineteen years, because it let me stop being afraid.",
        ),
        know=f"""<p>A go-bag is everything you'd need if your job disappeared tomorrow, prepared while it hasn't: a current CV, a
list of achievements with numbers, savings, contacts outside your company, and a basic understanding of your rights. It
takes an afternoon a year. Its main effect is to make you less afraid.</p>
<h3 class="kh">What goes in it</h3>
<p>Your CV, your Brag Scroll (achievements with dates and numbers), a savings buffer, outside contacts, and your contract terms.</p>
<h3 class="kh">Why people don't pack</h3>
<p>Loyalty, optimism, and the feeling that preparing is disloyal or tempts fate. It does neither.</p>
<h3 class="kh">What it gives you</h3>
<ul class="fears"><li>Calm in uncertain times.</li><li>Speed if the worst happens.</li><li>Better negotiation (you have options).</li><li>Better reviews (you remember your achievements).</li></ul>
<h3 class="kh">Three kinds of bag</h3>
<div class="breeds">
<div><b>The Empty</b><p>Nothing ready. Start with the CV and the list tonight.</p></div>
<div><b>The Half-Packed</b><p>A CV from three years ago. Update it; add numbers.</p></div>
<div><b>The Ready</b><p>Packed and refreshed yearly. Carry it lightly.</p></div>
</div>
{note("Pack it in the good times. Unpack it never, if you're lucky.")}""",
        difficulty=dict(
            normal=dict(who="Good times, empty bag.",
                        know=["No omens.", "Your CV is old.", "You've never needed it."],
                        do=["Spend one afternoon: CV, achievements, contacts.", "Start a savings buffer, however small.", "Find your contract and note your terms."],
                        avoid="The loyalty vow: “they'll look after me”.",
                        next="If omens appear and your bag is empty, you're at Nightmare."),
            nightmare=dict(who="Omens are visible; the bag is half-packed.",
                           know=["Consultants are in.", "Your CV is out of date.", "Savings are thin."],
                           do=["Update your CV this week, with numbers.", "Write your achievements list now, while you still have access to the evidence.", "Warm three outside contacts.", "Trim spending where you can."],
                           avoid="Packing in panic at 2 a.m. Do it calmly, in daylight, this week.",
                           next="If the calendar invite arrives with an empty bag, you're at Hell."),
            hell=dict(who="The invite arrived; the bag is empty.",
                      know=["You're at risk now.", "Nothing is ready.", "You're frightened."],
                      do=["Don't panic-sign anything (see the Calendar Invite).", "Use the consultation period to pack: CV, achievements, references.", "Ask colleagues for LinkedIn recommendations now.", "Talk to people; ask for introductions."],
                      avoid="The company archive: copying company data “for your portfolio”.",
                      next="You'll get through it. Then pack the bag properly for next time."),
        ),
        mirror=dict(
            title="Is your bag packed?",
            intro="Tick honestly. Nobody's looking.",
            signs=["Your CV is more than a year old.", "You couldn't list five achievements with numbers right now.", "You have less than three months of essentials saved.",
                   "Every professional contact you have works at your company.", "You don't know your notice period."],
            cure="Book one afternoon this month in your calendar, titled “go-bag”. Do the CV, the list and three coffees. Then forget about it until next spring.",
        ),
        rehearsal=dict(
            title="Scene: Saturday 13 March, 14:00. Pip and the Chronicler, a café near The Grid.",
            intro="Packing, with someone who's done it nineteen times.",
            lines=[
                ("Pip", "I updated my CV on Tuesday. It took four hours. I couldn't remember anything I'd done."),
                ("Chronicler", "That's why you keep the list. Every Friday, one line. Then the CV takes twenty minutes."),
                ("Pip", "And savings?"),
                ("Chronicler", "Whatever you can. A month's essentials is a start. Three is calm. Six is sleep."),
                ("Pip", "Who should I call outside MetroVolt?"),
                ("Chronicler", "Your old manager from your first job. A recruiter you trust. Someone from your graduate intake who left. Coffee, not favours."),
                ("", "Pip sets a recurring Friday reminder: “one line”. By the time Horizon is announced in May, the list has eight new lines and the bag is packed."),
            ],
            note="The go-bag isn't about expecting the worst. It's about not having to be afraid of it.",
        ),
    ),
    # ------------------------------------------------------------------ the Ghost Ship
    "ghost-ship": dict(
        sighting=f"""{beat("April · the first lifeboat")}
<p>Benedict Crane, Director of Strategy, announced he was “leaving to pursue an exciting new chapter”. His farewell email
was three lines long. His calendar had been empty for two weeks before it.</p>
{beat("May · the second")}
<p>Victor Kraal, Head of Grid Analytics, updated his LinkedIn headline to “open to new opportunities” on a Sunday. On the
Monday he told his team nothing had changed. In June, he joined Vexmoor Consulting.</p>
{beat("June · the review")}
<p>Horizon placed Strategy under “strategic review”. Its projects were paused, not cancelled. Nobody could say what Strategy
would be for in 2028. The corner offices emptied one by one.</p>
{beat("July · the wheel")}
<p>Dorian stayed. He presented a 40-slide “Strategy 2028 Vision” to a meeting room with three people in it, one of whom was
there to collect the projector.</p>
{note("Ships rarely sink in an afternoon. Count the lifeboats while the band is still playing.")}""",
        origin=dict(
            title="How Strategy became a ghost ship",
            beats=[
                ("2020 · the launch", "Benedict builds the Strategy department to give MetroVolt “a long-term view”. It's fashionable, well-funded and close to the CEO."),
                ("2021 to 2025 · drifting", "Strategy produces slides. The business produces electricity. The two meet less and less. Benedict is always travelling (see Act III, the Absent Lord)."),
                ("2026 · the reorg", "Act I's reorg moves Grid Analytics into Strategy to give it substance. It helps, briefly."),
                ("2027 · Horizon", "Vexmoor's benchmark shows MetroVolt's Strategy is three times the size of peers'. Ops has numbers; Strategy has slides (see Reading the Omens). The ship takes on water. The officers take the lifeboats first."),
            ],
            turning="A department built around a leader and a fashion, not around work the business couldn't do without.",
            saved="A clear answer, every year, to “what would break if we disappeared?”. Strategy never had one.",
            note="Every department should be able to answer one question: what breaks if we're gone? If yours can't, start counting lifeboats.",
        ),
        know=f"""<p>Sometimes a whole department, or company, is going down. The signs are usually visible for months: leaders
leaving, work paused, purpose unclear. The question isn't whether to be loyal; it's <b>when to leave, and in what order</b>,
while you still have choices.</p>
<h3 class="kh">What keeps people aboard</h3>
<p>Loyalty, hope, sunk cost, and leaders who keep saying everything's fine (often while updating their own LinkedIn).</p>
<h3 class="kh">Why the officers leave first</h3>
<p>Because they see the waterline earliest, and they have the best networks. That's not a betrayal to copy; it's a signal to read.</p>
<h3 class="kh">What helps you</h3>
<ul class="fears"><li>An honest waterline check.</li><li>A lifeboat plan with an order.</li><li>A straight question to the most senior person left.</li><li>Your go-bag, packed.</li></ul>
<h3 class="kh">Three kinds of ship</h3>
<div class="breeds">
<div><b>The Listing Ship</b><p>In trouble but salvageable. Help fix it, with a plan B.</p></div>
<div><b>The Ghost Ship</b><p>Leaders gone, purpose gone. Lifeboats now.</p></div>
<div><b>The Wreck</b><p>Already sinking. Get the best terms you can and go.</p></div>
</div>
{note("Loyalty is owed to people, not to org charts. The org chart won't notice you've gone.")}""",
        difficulty=dict(
            normal=dict(who="The Listing Ship: trouble, but salvageable.",
                        know=["Leaders are still committed.", "Purpose is clear, if challenged.", "There's a recovery plan."],
                        do=["Help fix it; it can be a great experience.", "Keep your go-bag packed.", "Watch the waterline monthly."],
                        avoid="Going down with the ship out of stubbornness.",
                        next="If leaders start leaving and work is paused, you're at Nightmare."),
            nightmare=dict(who="The Ghost Ship: leaders gone, purpose fading.",
                           know=["Senior leaders have left.", "Projects are paused indefinitely.", "Nobody can say what the department is for next year."],
                           do=["Do the Waterline Check, in writing.", "Make the Lifeboat Plan: internal move, external, stay for terms.", "Ask the Honest Captain Question.", "If you lead people, tell them what you know."],
                           avoid="Playing on: pretending to your team that all is well.",
                           next="If the department is being closed, you're at Hell."),
            hell=dict(who="The Wreck: closure is coming.",
                      know=["Closure or merger is confirmed or obvious.", "Redundancies are certain.", "People are leaving weekly."],
                      do=["Find out the redundancy terms; they may be worth staying for.", "Apply for internal roles early.", "Ask for references now, while managers are still there.", "Leave well: handovers, thanks, no burned bridges."],
                      avoid="The first lifeboat in silence: leaving your team to find out you've gone.",
                      next="When you land, write down what you'd look for next time. Then pack a new go-bag."),
        ),
        mirror=dict(
            title="What would break if you were gone?",
            intro="Ask it of your team, and of your department. Tick honestly.",
            signs=["You can't say what would break if your department disappeared.", "Your best people have left in the last six months.", "Your leaders' LinkedIn profiles say “open to work”.",
                   "Your work has been “paused” for more than a quarter.", "You're staying mainly out of loyalty."],
            cure="Answer the question in one sentence: “If we were gone, ___ would break.” If you can't fill the blank, start your Lifeboat Plan this week.",
        ),
        rehearsal=dict(
            title="Scene: Monday 5 July. Dorian, alone in Strategy, asks Pip for advice.",
            intro="The Waterline Check and the Lifeboat Plan, from the outside looking in.",
            lines=[
                ("Dorian", "Benedict's gone, Victor's gone. They say nothing's changing. Should I be worried?"),
                ("Pip", "Honestly? What would break if Strategy disappeared tomorrow?"),
                ("Dorian", "…The 2028 Vision."),
                ("Pip", "Who's waiting for it?"),
                ("Dorian", "…Nobody, I suppose."),
                ("Pip", "Then make a lifeboat plan. Ops is hiring a planning lead. You present brilliantly. Use it for someone else's work, with their name on it this time."),
                ("", "Dorian applies. In September, he presents Customer Ops' quarterly review. He names Asha and Pip on slide 1. It's the first time he's ever done it."),
            ],
            note="Even the Credit Vampire deserved a lifeboat. Pip offered one, with a condition. That's how famines end: with people helping each other ashore.",
        ),
    ),
}
