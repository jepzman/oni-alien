# Handoff: The Darkside of the Corporation (Series 4)

Status as of 2026-11-16: **Act II (The Bestiary) is written and built: 12 entries.** Owner's decisions (16 Nov):
the company is **MetroVolt Electric Corporation** (a modern city power utility) instead of the gothic placeholder;
start with Act II; 12 entries per Act; both looks, **candlelight** (default) and **parchment**, with a switch on
every page. Built pages: section 12. Remaining open decisions: section 10.

## 1. What the series is

*The Darkside of the Corporation: A Survival Grimoire for the Cursed Employed.*

A field guide to the parts of working life no onboarding deck mentions: politics, difficult people, bad managers,
layoffs, budget cuts, promotions, favouritism, rival vendors, impossible clients. It is dressed as a **dark-fantasy
grimoire** (gothic dungeon crawl, witchcraft, bestiaries, cursed loot) and written to be **funny**, but every page
has to be **genuinely useful**: the joke is the wrapper, the advice is real.

The frame: the book was found in the supply cupboard on Floor 13, half-burned, annotated in three different inks by
people who survived (and a few who did not). The office is a dungeon. You are an adventurer of modest level. Every
coworker, meeting and reorg is a creature, curse or ritual, and each has an entry.

How it differs from the other shelves:

| | Series 1–2 | Series 4 |
| --- | --- | --- |
| Subject | patterns and practices | people, power and survival |
| Voice | calm, plain study notes | gothic-pompous narrator, deflated by deadpan footnotes |
| A note is | one technique | **one creature, curse or ritual**, with counter-spells |
| Ratings | quality attributes | **survival stats** (section 5) |
| Dial | light / standard / heavy | **difficulty: Normal / Nightmare / Hell** |

## 2. Tone rules (the important part)

1. **Gothic voice, office facts.** The narrator writes like a doom-laden chronicler ("And lo, the Reply-All spread
   across the realm, and 340 souls received the cafeteria menu"). The comedy is the gap between the epic phrasing
   and the very small, very real horror.
2. **The footnotes deflate.** A second voice, the **Annotator**, scribbles sarcastic margin notes: *"This happened
   to me. It was a Tuesday. There were bagels."* The footnotes also carry the plainest version of the advice.
3. **Punch at systems and behaviours, never at groups.** Creatures are behaviours (the Credit Vampire), not kinds of
   people. No jokes about age, gender, nationality, disability or any protected group. HR, finance and procurement
   can be teased as *departments*, never as the people in them.
4. **The advice is sound.** Counter-spells must be things a sensible mentor would say: document, pre-wire, ask
   clarifying questions, build allies, negotiate with evidence, know your rights, leave when it is time. If the
   real answer is "talk to an employment lawyer", say so, in a scroll.
5. **The Forbidden Spells section is where the dark stuff goes**, and it is always shown *backfiring*. Sabotage,
   revenge, gossip and lying appear only as tempting moves with a soul cost. The book never teaches harm.
6. **Original world.** The look is generic gothic dark fantasy (skulls, candles, runes, blackletter, wax seals).
   No names, places, monsters, art or sounds from any existing game. All creatures and places are our own.
7. **Not legal or HR advice.** Every book carries a footer: satire with practical tips; for layoffs, contracts and
   discrimination, check local law and get proper advice.
8. **Same house rules as the other series:** short sentences, everyday English, dates and numbers in every scene.

## 3. The world (recurring cast)

The dungeon: **MetroVolt Electric Corporation**, a city power utility ("Powering Tomorrow, Today™"): 6,200 souls in **The Grid**, a 31-storey glass tower downtown, keeping the lights on for 2.3 million homes. Plus
a basement nobody goes to. Recurring characters (pronouns stated, keep them consistent):

| Character | Role | Notes |
| --- | --- | --- |
| **The Chronicler** (narrator, they/them) | 19 years at MetroVolt, survived 7 reorgs, 4 CEOs and 1 "transformation journey" | writes the entries in the grand voice |
| **The Annotator** (she/her) | ex-MetroVolt, now freelance, writes the margin notes | the deadpan voice of reason |
| **Pip** (he/him) | the apprentice: a junior analyst, level 3, full of hope | the reader stand-in; makes the mistakes |
| **Lord Varnish** (he/him) | the VP of Synergy | speaks only in frameworks; appears in every Act as a recurring boss |
| **The Council of the Third Floor** | the leadership team | decisions emerge from it like smoke |
| **Vexmoor Consulting** | the rival vendor guild | always cheaper on slide 4, never on invoice 9 |
| **Hargreave Foods** | the difficult client (a big industrial power customer) | 11 stakeholders, 0 decision makers |

## 4. Entry format (the grimoire page)

Every entry has the same ten parts, so the series reads like a bestiary and can be skimmed.

| # | Section | What it holds |
| --- | --- | --- |
| 1 | **Name, sigil and threat level** | creature or curse name, a doodled sigil, 1–5 skulls, habitat ("open-plan, Q4") |
| 2 | **A sighting** | a short MetroVolt scene: Pip meets the thing, with a date and a number |
| 3 | **Know thy enemy** | why this happens, the real mechanism (incentives, fear, structure), in plain words |
| 4 | **Signs and omens** | 4–6 early warning signs, as a checklist |
| 5 | **Counter-spells** | 3–5 moves that work, each with a short **incantation**: the exact words to say or send |
| 6 | **Forbidden spells** | the tempting dark moves, each with its **soul cost** and how it backfires |
| 7 | **Difficulty: Normal / Nightmare / Hell** | the same creature at three strengths and how the response changes (Hell usually ends in "update your CV") |
| 8 | **Survival stats** | nine ratings for the main counter-spell (section 5) |
| 9 | **Loot drop** | one reusable item: a template, script or checklist (the "CYA email", "the brag scroll") |
| 10 | **The trial** | three "what would you do?" questions with answers, plus the Annotator's last word |

Fields to add to the note data (when built): `threat` (1–5), `habitat`, `omens`, `counterspells=[(name, how,
incantation)]`, `forbidden=[(name, soul_cost, backfire)]`, `difficulty=dict(normal=, nightmare=, hell=)`, `loot`.

## 5. Survival stats: `DARKSIDE_ATTRS` (proposal)

Rated for the entry's main counter-spell. All are "high = good for you".

| Stat | Question | Meaning |
| --- | --- | --- |
| Sanity kept | does it cost you sleep? | Emotional toll. High = little toll. |
| Career XP | does it move you forward? | Visibility, skills and progress gained. |
| Mana saved | how much political capital does it burn? | High = cheap; you keep favours in the bank. |
| Armor | does it protect you later? | Paper trail, witnesses, written agreements. |
| Stealth | can you do it quietly? | High = low drama, little visibility risk. |
| Allies won | does it build your party? | Relationships gained, not spent. |
| Soul intact | could you explain it to your gran? | Ethics. Forbidden spells score 1 here. |
| Time drain | how long does it take? | High = quick. |
| Backfire safety | what if it goes wrong? | High = a failed attempt costs little. |

## 6. Skin proposal: `theme-grimoire`

- **Paper:** aged parchment with burn marks on the corners; dark mode is "by candlelight" (near-black page,
  bone text, ember glow on headings). Default to dark.
- **Type:** blackletter display for titles (*UnifrakturMaguntia* or *Pirata One*), *IM Fell English* for body,
  a handwritten face for the Annotator's margin notes (*Caveat* or *Reenie Beanie*). All Google Fonts.
- **Palette:** blood red, candle gold, bone, bruise purple, poison green for the "omens" checklist.
- **Furniture:** a wax seal stamp per Act; threat skulls; a rune border; dripping-ink section rules; a "soul cost"
  meter on Forbidden Spells; stats drawn as hand-inked bars, not game UI.
- **Doodles:** creatures drawn in the same doodle style as the other journals, just with horns. (Keep it silly,
  not scary: the Meeting Lich holds a laser pointer.)

## 7. The eight Acts (books) and their entries

Eight Acts, 12 entries each, about 96 entries. Your topics are marked ✦; the rest are suggestions.
★ marks a flagship entry (longer, with a deep-dive scroll).

### Act I · The Court of Whispers: Office Politics
*Where power really lives, and how to walk its halls without being eaten.*

1. **The Map of Hidden Thrones** ★ ✦: the org chart vs the real power chart; who actually decides
2. **The Meeting Before the Meeting**: pre-wiring decisions so the real meeting is a formality
3. **Blood Pacts**: building alliances before you need them
4. **The Ghost Decision**: decisions made in a room you weren't in, and how to get into the room
5. **The Rumour Mill Familiar**: whisper networks; what to feed it, what never to say near it
6. **The CC Inquisition**: email politics: CC, BCC, reply-all and the cursed "looping in my manager"
7. **The Turf Wars of the Two Towers**: departments fighting over who owns what
8. **The Empire Builder**: the colleague who collects headcount like dragon gold
9. **The Ring-Kissing Ritual** ✦: kissing ass vs managing up; where the line is and why it matters
10. **The Chosen One** ✦: favouritism, and what to do when you are not chosen (or are)
11. **The Sacrificial Lamb**: being set up to take the blame for a doomed project
12. **The Art of Plausible Silence**: when saying nothing is the most powerful move

### Act II · The Bestiary: Difficult People ✦
*Know the creatures of the open plan.*

1. **The Credit Vampire** ★: feeds on your work, presents it as theirs (sample in section 9)
2. **The Meeting Lich**: undead meetings that never end and spawn more meetings
3. **The Gaslight Wraith**: "I never said that." Defence: the written recap
4. **The Bulldozer Ogre**: talks over everyone; steamrolls meetings
5. **The Passive-Aggressive Poltergeist**: "Per my last email…" "Just circling back…"
6. **The Coasting Zombie**: does nothing, somehow survives every reorg
7. **The Doppelgänger**: lovely to your face, knife in the steering committee
8. **The Martyr Banshee**: wails about how busy they are; refuses all help
9. **The Know-It-All Basilisk**: one glance and your idea turns to stone
10. **The Doom Prophet**: "We tried that in 2014. It failed." Every idea, every time
11. **The Toxic Positivity Siren**: "No problems, only opportunities!" (as the ship sinks)
12. **The Boundary Goblin**: messages you at 23:47 "quick question, no rush" (there is rush)

### Act III · The Throne Room: Bad Managers ✦
*You cannot slay your lord. But you can manage them.*

1. **The All-Seeing Eye** ★: the micromanager; trading updates for trust
2. **The Absent Lord**: never available, then furious you didn't check with them
3. **The Seagull Overlord**: flies in, squawks, poops on the plan, flies out
4. **The Weather Tyrant**: mood decides the day; reading the forecast
5. **The Conflict Phantom**: avoids every hard conversation; problems rot
6. **The Credit-Taking Crown**: when the Credit Vampire is your boss
7. **The New Lord Arrives**: surviving the first 90 days of a new manager
8. **The Ritual Circle of the 1:1**: turning the 1:1 into your most useful meeting
9. **The Skip-Level Séance**: when and how to go over their head (and the price)
10. **The Puppet King**: a manager with no real power; how to get things done anyway
11. **The Friend Who Became Your Boss**: when a peer is promoted over you
12. **The Escape Portal** ★: recognising when it is time to leave a bad manager, and leaving well

### Act IV · The Ascension: Promotions and Recognition ✦
*The stairway to the next level is not where they told you it was.*

1. **The Promotion Prophecy** ★ ✦: how promotions really get decided (hint: before the review)
2. **The Invisible Work Curse**: glue work, admin, mentoring: valued by everyone, rewarded by no one
3. **The Book of Deeds**: the brag document, and keeping it all year
4. **The Calibration Council**: what happens in the room where ratings are compared
5. **The Raise Duel**: negotiating pay with evidence, not hope
6. **The Rival for the Throne** ✦: competing with a peer for the same promotion without becoming a monster
7. **The Title Without the Gold**: promoted, no raise; what to ask for
8. **The Poisoned Chalice**: the "stretch assignment" that is actually a trap
9. **Passed Over: The Resurrection**: what to do the day after you don't get it
10. **Sponsors, Not Just Mentors**: finding someone who says your name in rooms you're not in
11. **Your First Minions**: the first-time manager survival kit
12. **The Peter Principle Curse**: knowing when "up" is the wrong direction

### Act V · The Famine: Layoffs, Budget Cuts and Reorgs ✦
*Winter comes for every budget.*

1. **Reading the Omens** ★: early signs of layoffs (the freeze, the consultants, the cancelled offsite)
2. **The Hiring Freeze Frost**: doing the job of three people, and saying so in writing
3. **The Budget Bloodletting** ✦: defending your team's budget when the knives come out
4. **The Curse of "More with Less"**: re-scoping work when resources vanish
5. **The Reorg Ritual**: the boxes move, the work doesn't; finding your place in the new chart
6. **The Suits from Beyond**: the consultants arrive; talking to them without talking yourself out of a job
7. **The Day of the Calendar Invite** ★ ✦: if you are laid off: what to ask, sign, save and do that week
8. **The Executioner's Burden**: when you have to lay people off, doing it humanely
9. **Survivor's Haunting**: the guilt, the workload and the morale after the cuts
10. **The Quiet Culling**: being sidelined, reassigned or "managed out" slowly
11. **The Go-Bag Scroll**: keeping your CV, network and savings ready in good times
12. **The Ghost Ship**: the company is sinking; when to bail and in what order

### Act VI · The Outer Realms: Clients, Vendors and Rival Guilds ✦
*Beyond the castle walls there are worse things than coworkers.*

1. **The Client Demon** ★ ✦: the difficult client; expectations, boundaries, escalation
2. **The Scope-Creep Swarm**: "while you're at it, could you just…"
3. **The Eleven-Headed Hydra**: the client with many stakeholders and no decision maker
4. **The Unpaid Invoice Wraith**: getting paid without burning the relationship
5. **The Bake-Off Arena** ✦: competing vendors in a pitch; winning without promising the impossible
6. **The Incumbent Dragon**: displacing (or being) the vendor that's been there 12 years
7. **The Rigged RFP**: spotting a tender written for someone else, and deciding whether to bother
8. **The Frenemy Pact**: the partner who is also your competitor
9. **The Overpromise Golem**: when your own sales team sold something that doesn't exist
10. **The Labyrinth of Procurement**: surviving legal, security reviews and 14 forms
11. **The Escalation Summoning**: the client goes over your head to your CEO
12. **Banishing a Client**: when and how to fire a client

### Act VII · The New Plagues: The Modern Workplace
*Fresh horrors for a new age.*

1. **The Return-to-Office Decree**: navigating mandates, badge counts and "collaboration Tuesdays"
2. **The Green Dot of Doom**: remote politics: presence, status lights and being seen
3. **The AI Replacement Prophecy** ★: "AI will do your job". What to learn, what to show, what to ignore
4. **The Copilot Credit Grab**: who gets credit when the machine helped
5. **The Cult of Family**: "We're a family here" (families can't lay you off)
6. **The All-Hands Mass**: decoding leadership speak at the town hall
7. **The Engagement Survey Oracle**: anonymous? Really? What to write
8. **The Hot-Desk Hunger Games**: no desk, no locker, no dignity
9. **The Transformation Journey**: surviving the fourth agile transformation
10. **The Slack Channel Necropolis**: 400 channels, 12 alive; managing the noise
11. **The Performative Busy-ness Dance**: looking busy vs being effective
12. **The Pivot Storm**: when strategy changes every quarter

### Act VIII · The Inner Sanctum: Keeping Your Soul
*The final boss is you, at 2 a.m., checking email.*

1. **The Slow Hex of Burnout** ★: noticing it, naming it, getting out of it
2. **The Salt Circle**: setting boundaries that hold
3. **The Mimic of Imposter Syndrome**: the chest that looks like your inadequacy (it's furniture)
4. **The Phylactery of Paper**: documentation as protection: what to keep and where
5. **Reputation Is Your Hit Points**: how it's built, lost and healed
6. **The Word of Power: No**: declining work without career damage
7. **The Dark Pact**: when you're asked to do something unethical
8. **HR's True Allegiance**: what HR is for (the company), and when to go anyway
9. **The Whistle of Last Resort**: speaking up about serious wrongdoing, safely
10. **Quiet Quitting vs Quiet Thriving**: doing your job without donating your life
11. **The Exit Interview Trap**: what to say on the way out (less than you want)
12. **Life After the Dungeon**: leaving well; the boomerang employee; who you are without a badge

## 8. Extras (the Diablo-ish bonus pages, all original)

1. **The Bestiary index** (`/darkside/bestiary/`): every creature on one page, sorted by threat skulls, with habitat
   and "first counter-spell". Works like the PMBOK map page.
2. **Choose your class** (a short quiz): Paladin (principled, won't play politics), Rogue (networker), Necromancer
   (revives dead projects), Bard (communicator), Druid (keeps the team alive), Warlock (does it all in Excel).
   Each class gets a "strengths, weak against, recommended entries" card.
3. **The Skill Tree**: political and survival skills as a tree (Listening → Pre-wiring → Coalition Building →
   Sponsorship), each node linking to its entries.
4. **The Loot Chest**: every loot drop in one place: the CYA recap email, the brag scroll, the "no, but" script, the
   layoff week checklist, the raise case one-pager, the client boundary email.
5. **Boss Fights**: one per Act, a longer story where Pip faces Lord Varnish using that Act's skills, with branching
   "what would you do?" choices and endings (good, bad, and "you were reorged").
6. **Difficulty selector** on each entry: Normal / Nightmare / Hell toggles section 7.
7. **Cheat sheets** (the shelf exists): *The Bestiary on one page*, *Incantations for every occasion*, *Layoff week*.

## 9. Sample entry (tone reference): The Credit Vampire

> **The Credit Vampire** · ☠☠☠☠ · *Habitat: steering committees, all-hands slides, any email with "great work team"*

**A sighting.** On the 3rd of March, Pip spent eleven nights building the forecast model that saved the heatwave
account. On the 4th, at the all-hands, Dorian from Strategy presented it. Slide 7 said *"Dorian's model."* Pip's
name appeared nowhere, not even in the font.

**Know thy enemy.** The Vampire is rarely evil. It is hungry. It lives where work is invisible and only the
presenter is seen. Feed it darkness (work nobody knows is yours) and it grows fat. Sunlight kills it.

*Annotator: "Sunlight" means "other people knowing what you did, before the meeting." Not literal sun. HR has
asked me to stop saying this.*

**Signs and omens.**
- [ ] "Send me the file, I'll take it from here."
- [ ] You are not invited to the meeting where your work is presented.
- [ ] They say "I" about work and "we" about problems.
- [ ] Your manager first hears about your work from them.

**Counter-spells.**
1. **The Dawn Ward** (announce before they present). *Incantation:* "Quick heads-up before Thursday: the forecast
   model is done. Happy to walk anyone through how I built it."
2. **The Name-Carving Rite** (your name in the artefact). Put "Prepared by Pip" on the cover, in the file name, in
   the footer. Vampires hate file names.
3. **The Invitation Hex** (ask to present the part you built). *Incantation:* "Could I take the five minutes on the
   model? It'll save you questions on the details."
4. **The Grateful Reflection** (credit them back, publicly and generously). "Thanks Dorian for sharing the model I
   built; glad it helped." Polite. Lethal.

**Forbidden spells.**
- *The Public Staking*: calling them a thief at the all-hands. **Soul cost:** high. You look bitter; they look calm.
- *The Poisoned File*: sabotaging the next model you hand over. **Soul cost:** total. the city browns out, and so
  do you.
- *The Whisper Campaign*: complaining to everyone at the coffee machine. **Soul cost:** medium. The coffee machine
  reports to Lord Varnish.

**Difficulty.** *Normal:* a careless peer; a friendly word fixes it. *Nightmare:* a habit; you need the Dawn Ward
every time and a word with your manager. *Hell:* it's your boss, and the culture rewards it; protect your paper
trail and read Act III, entry 12.

**Survival stats (Dawn Ward).** Sanity 4 · Career XP 5 · Mana 4 · Armor 4 · Stealth 4 · Allies 3 · Soul 5 ·
Time 5 · Backfire safety 4.

**Loot drop: the Weekly Deeds Scroll.** A three-line Friday note to your manager: *shipped / in progress / need
help.* Your work is in daylight before anyone can carry it into a meeting.

**The trial.**
1. Dorian asks for your file "to tidy the formatting" the day before the steering committee. What do you do?
2. Your manager praises Dorian for your model in a group chat. What's the best reply?
3. Credit is stolen once, by someone new. Which difficulty is this, and which spell?

*Annotator's last word: "The best time to claim credit is before the work is finished. The second best time is
in writing."*

## 10. Open decisions

1. **Name:** *The Darkside of the Corporation* as the series title, with *A Survival Grimoire* as subtitle? Or
   *The MetroVolt Grimoire*?
2. **Volume order:** start with **Act II (The Bestiary)**. It's the most fun, every entry stands alone, and it
   sets the voice for the rest. Proposed order: II → I → III → V → IV → VI → VII → VIII.
3. **Size:** 12 entries per Act (96 total), or 8 per Act for a faster first season (64)?
4. **Separate world or Larder crossover?** Proposal: separate (MetroVolt), so it can be darker and sillier
   without spoiling the Larder story; a single "Meanwhile at Larder" easter egg per Act at most.
5. **Narrator:** one Chronicler plus the Annotator (proposed), or a different narrator per Act?
6. **Skin default:** dark ("by candlelight") or parchment light?
7. **Shelf:** a fourth shelf on the landing page, with a "planned" entry and a future-log line once the first Act
   is scheduled.

## 11. Build notes (when we start)

- Content: `content/darkside-<act>/` (e.g. `darkside-2/`), one `.py` per entry, same pattern as other volumes.
- Renderer: extend `scripts/build_notes.py` with the new fields (section 4) and `theme-grimoire`, or a small
  `scripts/grimoire.py` if the layout differs too much.
- New pages: `/darkside/` (series index with the eight Acts), `/darkside/bestiary/`, `/darkside/loot/`,
  `/darkside/class/`.
- Landing page: a `series=4` shelf, `PLANNED_DARKSIDE` list, future-log entry.

## 12. What was built (Act II, 16 Nov 2026)

- Renderer `scripts/grimoire.py` (called from `build_notes.py` main; `grimoire.build(asset)`), content
  `content/darkside/act-2.py` (an `ACT` dict; `note()` = the Annotator's margin note, injected by the loader).
- Pages: `/darkside/` (the eight Acts; unwritten ones show as sealed), `/darkside/act-2/` (contents + cast),
  `/darkside/act-2/<slug>.html` (12 entries). A shelf section on the landing page (`#darkside`, `.book--darkside` in
  `bujo.css`). Not in `journals.json`, so there are no PDFs yet.
- Skin: `public/assets/grimoire.css` (`html[data-look="candle"|"parch"]`) and `grimoire.js` (look switch saved in
  localStorage, difficulty tabs with a no-JS fallback that shows all three).
- Act II entries: Credit Vampire ★, Meeting Lich, Gaslight Wraith, Bulldozer Ogre, Passive-Aggressive Poltergeist,
  Coasting Zombie, Doppelgänger, Martyr Banshee, Know-It-All Basilisk, Doom Prophet, Toxic Positivity Siren,
  Boundary Goblin. Cast with pronouns is in the `cast` list of the content file; keep it consistent in later Acts.
- Checked: both looks at desktop, 375 px phone width (no horizontal scroll) on the series, Act and entry pages and the landing page.
- Next: Act I (The Court of Whispers), same format. Extras from section 8 (bestiary index across Acts, class quiz,
  loot chest) once two Acts exist.

## 13. The eerie pass and painted plates (16 Nov 2026)

- Owner approved the eerie design (preview first), then asked for **more realistic illustrations, serious and humorous at once**.
- Skin now has: a turning **sigil** per entry (the creature's catchphrases on the ring, `ring=` field; an eye that blinks),
  skulls with glowing sockets, blood-drop soul costs, blinking omen eyes, thorned dividers that drip, thorned corners,
  a torn page edge, tally marks and a margin scrawl (`scrawl=` field), fog, a vignette, a flickering title and, by
  candlelight, eyes that blink in the side margins. All motion stops under `prefers-reduced-motion`.
- **Plates:** `content/darkside/art/<slug>.svg` is inlined into the entry (with `plate_caption=`) when it exists.
  Style: a painted night scene with dramatic light (warm projector light against cool window light), a straight-faced
  pose, film grain and a vignette, with the jokes in the props (badge “AFTER DARK ONLY”, the bat pocket square, the
  USB stick tagged PIP_Q3_FORECAST_v4, the “World's best team player” mug). Prefix every id in an art file
  (e.g. `cv-`) so plates never clash. Done: Credit Vampire. To do: the other 11, after the owner signs off the style.
- Limit: hand-drawn SVG, not photo-realistic. If photo-realism is wanted, the owner could generate images
  elsewhere from prompts we write and drop them in as `<slug>.webp`.

## 14. Act II complete: all 12 plates (17 Nov 2026)

- Owner chose option 1 (painted SVG plates, no image generator). The Credit Vampire is hand-made
  (`content/darkside/art/credit-vampire.svg`); the other 11 are painted by `scripts/plates.py` (run it by hand:
  `python3 scripts/plates.py`, then the normal build). It shares one toolkit so every plate matches: `face()`
  (a lit, textured head: light from below/above/left/right, rim light, iris colours, brows, mouths, hair, ears,
  extras such as tusks, glasses, rot, wrinkles), `suit()`, `blouse()`, `hand()`, `window()`, `badge()`, `mug()`,
  and the grade (vignette + grain). Place a body with `body_y = face_y + 85*face_s - 43*body_s` so heads sit on necks.
- The Act contents page is now an illustrated bestiary: one card per creature with its plate, number, epithet and threat.
- Scenes (serious face, joke in the props): Lich at meeting #112 with “AGENDA: TBD”; Wraith in the lift on floor 13 with
  a gas lamp and a shredded sticky note; Ogre with a crushed talking stick under “MY PLAN!!!”; Poltergeist in the office
  kitchen with “PER MY LAST EMAIL” mugs; Zombie at 15% since 4 March; Doppelgänger with buns, and a knife in the
  reflection; Banshee at 23:58 with 412 unread; Basilisk with glasses and Pip turned to stone; Prophet in the alarm-red
  control room with the 2014 incident report; Siren under GOOD VIBES ONLY as the office floods; Goblin at the foot of the bed.
- Next: Act I (The Court of Whispers), same format, plates from the same toolkit.

## 15. Act I written (17 Nov 2026)

- `content/darkside/act-1.py`: The Court of Whispers, 12 entries: Map of Hidden Thrones ★, Meeting Before the Meeting,
  Blood Pacts, Ghost Decision, Rumour Mill Familiar, CC Inquisition, Turf Wars of the Two Towers, Empire Builder,
  Ring-Kissing Ritual ★, Chosen One, Sacrificial Lamb ★, Art of Plausible Silence.
- Owner asked for fewer illustrations: plates for the three flagships only (`hidden_thrones`, `ring_kissing_ritual`,
  `sacrificial_lamb` in `scripts/plates.py`). Entries without a plate show their turning sigil as card art.
- New cast (keep consistent): Marcus Bell (he/him, Pip's manager), Ottoline Grey (she/her, Chief of Staff, the hidden
  throne), Dame Helena Strand (she/her, CEO), Priya Nair (she/her, Customer Ops), Gareth Pound (he/him, Network Assets,
  the empire builder), Tamsin (she/her, EA on 27), Jules (they/them, the favourite). Lord Varnish's first name is Simon.
  Story facts used: Project Orion (billing integration, 18 months late, £2.4m over, lead #4 is Pip); 11,400 smart meters
  not reporting for 63 days on average; Grid Planning's budget cut 12% after Pip volunteered savings.
- Next by the plan's order: Act III (The Throne Room, bad managers).

## 16. Act III written (17 Nov 2026)

- `content/darkside/act-3.py`: The Throne Room, 12 entries: All-Seeing Eye ★ (micromanager), Absent Lord, Seagull
  Overlord ★, Weather Tyrant, Conflict Phantom, Credit-Taking Crown, New Lord Arrives, Ritual Circle of the 1:1,
  Skip-Level Séance, Puppet King, Friend Who Became Your Boss, Escape Portal ★. Plates for the three flagships only
  (`all_seeing_eye`, `seagull_overlord`, `escape_portal` in `scripts/plates.py`).
- Story (winter 2026–27, after Act I's reorg): Pip (now level 4) reports to Victor Kraal (he/him, Head of Grid Analytics,
  ex-consultant), under Benedict Crane (he/him, Director of Strategy, always travelling). Rupert Thorne (he/him,
  Interim Transformation Director from the parent group) visits monthly and leaves on the 14:05 to London. Pip is
  seconded to Gareth's Network Assets for the meter fix. Jules becomes Pip's team lead in January. In February Priya
  offers Pip an analytics lead role in Customer Ops; **he has not decided** (pick this up in Act IV or V).
- Deployed together with Act I.
