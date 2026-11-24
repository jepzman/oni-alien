# Handoff: The IT Operations Notebook (Series 2, Book 5)

Status as of 2026-11-24: **planned, nothing written yet.** Owner's decisions (24 Nov): IT operations (not business
operations), narrated by whichever character fits, starting where it fits the story's timeline. Open questions: section 9.

Story facts: `docs/larder-casebook.md` (source of truth) and the public case file `/larder/`.
Earlier plans, for format: `docs/HANDOFF-project-manager.md` (closest model: a book with a spine standard and a map page).

## 1. What the book is

Book 5 of Series 2. Narrator: **Eli** (he/him, as in Books 1 and 3), Larder's platform and operations engineer. He was
there before Series 2 began (one of the 14 engineers in October 2025), and the casebook already shows the job outgrowing him:

- Larder Core runs on 3 VMs he **patches by hand** (Ana, 2026).
- Week of 23 March 2026: Sanne's levelling shows him at **160 %** (platform 2½ days, RFC-003 1½, on call 1, internet
  line 1, extras 1½, alert fix ½). Ana takes over his on-call week.
- Rotterdam opens **27 April 2026** on a 4G router; its internet line (issue I-07, raised by Eli) is live on 13 May.
- **29 Oct 2026**: a network rule change cuts Dispatch off from Postgres for 25 minutes.
- **18 Dec 2026, 18:05**: a database failover takes checkout down for 38 minutes (≈ 900 orders lost or late).
- **31 Aug 2027**: billing webhooks silent for 9 hours; Korenwolf shown as unpaid.
- **17 Dec 2027**: PSP A slow for 22 min, switched in 40 s, no failed orders.
- **10 Jan 2028**: first full restore takes 3 h 40; drill on 18 Apr: 22 min.
- **Autumn 2028**: a reliability team exists; game days 14 and 21 Sep, pager 1 Oct, first incident 9 Oct (18 min).

Ana asks *"how do we build it?"*, Grace *"should we, and for whom?"*, Sanne *"by when, for how much?"*, Mo *"what did
we promise the client?"*. Eli asks ***"how do we keep it running, and what do we do when it breaks?"***

**Arc:** from the one person who knows where everything is, to the lead of a reliability team that doesn't need him at
3 a.m. Each volume removes one way the company depends on Eli's memory.

**Timeline:** **Mon 30 March 2026** (the week after the 160 % levelling) to **October 2028** (the reliability team's
first incident). The book runs alongside Books 1–4 and ends a few weeks after them. It retells several of their events
from the operations side, which is where the "meanwhile" links come in.

## 2. The spine: ITIL 4 practices plus SRE

Book 3 covered PMBOK. Book 5 covers **ITIL 4** the same way, with **site reliability engineering (SRE)** practices
where ITIL says what to do and SRE says how small teams actually do it (SLOs, error budgets, toil, blameless reviews).

- ITIL 4: the service value system, **7 guiding principles** (focus on value; start where you are; progress
  iteratively with feedback; collaborate and promote visibility; think and work holistically; keep it simple and
  practical; optimise and automate), **4 dimensions** (organisations and people; information and technology; partners
  and suppliers; value streams and processes), and **34 practices** (14 general, 17 service, 3 technical management).
- An **ITIL & SRE map** page (`/itil/`, data in `content/itil/map.py`), like the PMBOK map: every principle, dimension
  and practice → the note that covers it. Practices that belong to other books (project management, portfolio,
  architecture, business analysis, software development) link there instead.

**Check before writing:** practice names come from public sources. Check them against the current ITIL guide, and
check whether a newer ITIL edition has replaced ITIL 4 by the time we write. If one has, use the newer edition as the spine
and keep ITIL 4 as the "in older editions" tag.

**Copyright:** ITIL is a registered trademark of PeopleCert. Everything is written in our own words and drawn from scratch,
with no copied definitions or figures. Practice names are used as names only. Footer on every page: independent study
notes, not affiliated with or endorsed by PeopleCert or AXELOS.

## 3. Note format

Kept from Books 1–3: the Larder scene, the analogy with doodles, how it works, the template card, "try it", the quiz,
"meanwhile" boxes, the case file timeline, nine ratings, one PDF per volume. Like Book 3: the title is a question, and a
tag under it gives the ITIL practice, the SRE term and older names.

New for Book 5:

- **Maturity ladder** (replaces Book 3's light / standard / heavy dial): four rungs for the practice,
  **by hand → written down → scripted → self-service / automatic**, with what Larder does at each rung and when to
  climb. Eli climbs one rung per note, never four.
- **Pager log** box on incident notes: the real page as it arrived (time, alert text, who answered, minutes to
  acknowledge), so the reader sees the moment before the lesson.
- **Deep dives** on key notes (3–5 per volume), as in Book 3.

## 4. Nine ratings (`OPS_ATTRS`)

user impact · reliability · recovery speed · change safety · visibility · toil reduction · cost awareness ·
sustainable on-call · low overhead

(Series 1 Vol. 6's ratings score *patterns*; these score *practices*, as Books 1–3 do.)

## 5. Skin: `theme-ops`, the incident logbook

Carbon-copy duplicate forms: a perforated tear-off edge, a timestamp column in the margin (`14:05`), a **SEV** stamp
in place of the "LGTM" stamp, and form fields under the title (service, owner, rung). Palette: incident red, signal
amber, graphite, a soft phosphor green for "resolved". Fonts: IBM Plex Mono for labels and times, the usual handwriting
font for Eli's notes. Must read well in print and in both themes.

## 6. Volumes (6 × 15 notes)

### Vol. 1 · Keeping the Lights On (`ops-1`, Mar → Jun 2026)
Rotterdam opens on 4G; Eli at 160 %; nothing is written down.

1. What is IT operations for? (service value system, value, outcomes, guiding principles)
2. What do we actually run? (service catalogue)
3. What is connected to what? (service configuration, dependency map)
4. What do we own, and where is it? (IT asset management: handhelds, routers, laptops, licences)
5. Who owns each service? (service owners)
6. Who gets woken up? (the first on-call rota)
7. How do we know it's broken? (monitoring and event management)
8. Which alerts deserve a human? (alert hygiene: the ½-day alert fix)
9. What do I do at 3 a.m.? (runbooks)
10. Where do people report problems? (service desk for stores and office)
11. Can I have a new handheld? (service requests)
12. Something is broken: now what? (incident basics)
13. How does a new store get its IT? (store IT kit; Rotterdam on 4G)
14. Where is that written down? (knowledge management; Jasper's missing reasons)
15. Why am I always busy? (toil, and the 160 % week)

### Vol. 2 · When Things Break (`ops-2`, Jun → Dec 2026)
Ends with the Christmas failover.

1. How bad is it? (severity levels)
2. Who is in charge? (incident commander and roles)
3. Who needs to know? (incident communication with Sam, Femke and the stores)
4. Do we need a status page?
5. The vendor is down at peak (supplier escalation)
6. Writing it down while it happens (incident timeline)
7. What did we learn? (blameless post-incident review)
8. Why did it really happen? (problem management, causal analysis)
9. We know the bug, now what? (known errors and workarounds)
10. Why do action items never close?
11. Which incident numbers mean anything? (MTTA, MTTR and their traps)
12. The network rule change of 29 Oct (meanwhile: Ana's deployment view)
13. Telling a business client (Korenwolf incident reports, with Mo)
14. The Christmas failover of 18 Dec (a major incident, end to end)
15. What about the near misses?

### Vol. 3 · Changing Things Safely (`ops-3`, Jan → Jun 2027)
The warehouse move to WMS B (Zuid 19 Apr, Noord 24 May); Utrecht (12 Apr) and The Hague (14 Jun) open.

1. Which changes need a second look? (change enablement: standard, normal, emergency)
2. Do we need a change board? (peer review instead of a CAB)
3. When must we not change anything? (change calendar and freezes)
4. Release or deploy? (release management vs deployment management)
5. How risky is this change? (change risk scoring)
6. How do we undo it? (rollback plans; links Series 1 Vol. 6)
7. Is it really ready? (service validation and testing)
8. Why do the environments differ? (configuration drift)
9. Cutting over a store (the WMS B cutover plan)
10. A new city by checklist (city set-up runbook; meanwhile: Sanne's playbook)
11. Which changes fail? (change failure rate, DORA metrics)
12. The urgent fix at 17:00 on a Friday (emergency changes)
13. Who may touch production? (production access, break-glass)
14. Patching without fear (patch and vulnerability routine)
15. Retiring what we no longer need (decommissioning; StockPilot off in Sep 2027)

### Vol. 4 · Promises & Measures (`ops-4`, Jul → Dec 2027)
Billing webhooks go silent; Antwerp (18 Oct) and Eindhoven (22 Nov) open; Christmas 2027 goes well.

1. What do users count as working? (SLIs)
2. How good is good enough? (SLOs)
3. When do we stop shipping features? (error budgets)
4. What did we sign? (SLAs; Korenwolf's 99.8 %, with Mo)
5. What do teams promise each other? (OLAs and internal agreements)
6. How available are we, really? (availability management; meanwhile: Ana's availability note)
7. Will Christmas fit? (capacity and performance management; meanwhile: Ana's capacity plan)
8. The vendor went quiet (supplier management; billing webhooks on 31 Aug)
9. The monthly service report (measurement and reporting)
10. The service review meeting (relationship management)
11. Dashboards people actually open
12. Who decides when the budget is spent? (error budget policy)
13. A foreign city (Antwerp: languages, a second PSP, support hours)
14. Running a peak (Christmas 2027 war room; PSP switch on 17 Dec)
15. Asking the users (user satisfaction beyond uptime)

### Vol. 5 · Ready for the Worst (`ops-5`, Jan → Jun 2028)
The 3 h 40 restore, DR tiers, the pilot light in Paris, the Korenwolf supplier questionnaire.

1. What matters most if everything fails? (business impact analysis)
2. Can we actually restore? (backup and restore tests)
3. How fast must each service return? (continuity tiers, RTO and RPO)
4. A second region? (pilot light; meanwhile: Ana's ADR 0026)
5. Breaking things on purpose (game days and chaos experiments)
6. When the incident is a security incident (security operations)
7. Who still has access? (access reviews, leavers)
8. Rotating the keys (secrets and certificates)
9. What does it cost to run? (service financial management, cloud bill €78k → €58k)
10. Which risks keep us up at night? (operational risk register)
11. Prove it to the auditor (evidence for the Korenwolf questionnaire, with Lena)
12. Leaving a vendor (exit plans)
13. When the office is the outage (laptops, SSO, the office network)
14. Crisis communication beyond IT
15. The plan nobody has read (keeping continuity plans alive)

### Vol. 6 · Building the Reliability Team (`ops-6`, Jul → Oct 2028)
Ghent and Haarlem; the reliability team forms; the pager handover on 1 Oct.

1. Who runs what? (you build it, you run it vs a reliability team)
2. Is this service ready for production? (production readiness review; meanwhile: Ana's handover to operations)
3. Hiring the first SREs (workforce and talent)
4. On-call people can live with (load, pay, rest)
5. Handing over the pager (game days 14 and 21 Sep, pager 1 Oct)
6. The first incident without Eli (9 Oct, 18 min)
7. What to automate next (automation strategy and toil budget)
8. A platform for the other teams (golden path, from the ops side)
9. Where are we weak? (an operations maturity check)
10. The operations roadmap
11. Continual improvement that continues (improvement register)
12. Leading change in how teams work (organisational change management)
13. AI in operations: where it helps, where it lies (with Lena's rules from Book 3)
14. Growing operations engineers (career path)
15. Making it yours

## 7. Extras

- **The runbook binder** (`/runbooks/`): every template card in order (rota, runbook, incident timeline, review,
  change record, SLO sheet, service report, DR test), like Sanne's project file.
- **Cheat sheets:** Incident response on one page (roles, severities, comms, review); SLOs and error budgets (the maths,
  burn-rate alerts).
- **Deep dives** (Series 3) already planned: *Observability & SLOs* fits this book; add *Incident Response*.

## 8. Rules

- Don't repeat Series 1 Vol. 6 (Cloud & DevOps patterns) or Ana's quality notes. Link to them: Eli's notes are about the
  practice and the people, and their notes are about the mechanism.
- Every new fact goes into the casebook under "Book 5". Never contradict existing facts, and check the dates above against
  the casebook before writing each volume.
- Add each note to the case file `TIMELINE` (new tag `"5"`), add meanwhile links where a scene is shared, and
  update the future log.
- Same house style: short sentences, everyday English, dates and numbers in every scene.

## 9. Open questions for the owner

1. Is the title *The IT Operations Notebook* or *The SRE's Notebook*? (Recommendation: the first. It reads more widely
   and matches the ITIL spine.)
2. Should we write it before or after Book 4 (Mo)? This plan doesn't depend on Book 4, apart from three shared scenes
   (Korenwolf incident reports, the SLA, the questionnaire).
3. Check the ITIL practice names against the current guide (see section 2).
