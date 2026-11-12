# Handoff: The Product Owner's Notebook (Series 2, Book 2)

Status as of 2026-11-12: **planned; open questions in section 7 waiting for the owner. Nothing built.**

Story facts: `docs/larder-casebook.md` (source of truth) and the public case file `/larder/`.
Book 1's plan, for comparison: `docs/HANDOFF-solution-architect.md`.

## 1. What the book is

Book 2 of Series 2. Narrator: **Grace**, product owner for ordering and the customer apps at Larder, who joins on
13 October 2025, a week after Ana. Same company, same months, same meetings as Ana's notebook, seen from the other side:
Ana's notebook asks *“how do we build it?”*, Grace's asks *“should we, for whom, and how will we know?”*

Same eight-section note format and the same shared pieces as Book 1 (title block, “try it” box, template card, the
nine ratings), with its own skin (section 5).

Rule (as in Book 1): don't repeat notes from other books. Link instead: Grace's note on concierge tests links Ana's
spike/prototype/PoC note; Grace's backlog notes link the walking skeleton.

## 2. Volumes and topics (★ = write first)

| Vol. | Title | Story period | Collections → notes |
| --- | --- | --- | --- |
| 1 | Discovering the Problem | Oct 2025 → Jan 2026 | **Understanding customers**: Customer Interviews ★, Jobs to Be Done ★, Proto-Personas, Customer Journey Map · **Framing the problem**: Problem Statements, Opportunity Solution Tree ★, Assumption Mapping, Outcomes over Outputs · **Measuring what matters**: North Star Metric ★, Leading vs Lagging Indicators, Baseline Before You Build · **Testing ideas cheaply**: Fake Door Test ★, Concierge & Wizard-of-Oz MVP ★, Prototype Testing with Users |
| 2 | Deciding What to Build | Jan → Apr 2026 | **Prioritising**: RICE & ICE Scoring ★, Cost of Delay, Kano Model, MoSCoW and Its Traps · **Saying no**: Saying No Without Burning Bridges ★, Handling the HiPPO, Opportunity Cost · **Strategy & roadmaps**: Product Strategy on a Page ★, Now / Next / Later Roadmap ★, Outcome-Based Roadmaps, Roadmap vs Release Plan · **Making the case**: Business Case One-Pager, Bets Not Promises |
| 3 | From Idea to Backlog | Feb → Jun 2026 | **Shaping work**: Story Mapping ★, Thin Slices of Value ★, MVP vs MLP · **Writing it down**: User Stories that Work, Example Mapping ★, Definition of Ready & Done · **Working with the team**: The Product Trio, Sprint Goals, Refinement that Isn't a Meeting Marathon, Talking Tech Debt with Engineers ★ · **Shipping**: Release Planning, Launch Checklist (Rotterdam) ★, Dark Launches & Rollouts |
| 4 | Measuring & Learning | May → Oct 2026 | **Instrumenting**: Event Tracking Plan ★, Funnels ★, Cohorts & Retention Curves · **Experimenting**: A/B Tests ★, Guardrail Metrics, Reading Results Honestly · **Listening**: Support Tickets as Data, Feedback Loops with Operations, Customer Advisory Panel · **Goals**: OKRs ★, Vanity vs Actionable Metrics, Post-Launch Review, Killing a Feature |
| 5 | Stakeholders & Influence | all year | **Communicating**: Product Update that Gets Read ★, Demos that Land ★, The One-Page PRD · **Managing up and across**: Managing Up (Priya), Pitching to the CEO ★, Dependencies across Teams · **Partners inside**: Operations as a Customer (Joost) ★, Working with Legal & Privacy (Lena), Working with the Architect (Ana) ★ · **Hard moments**: Negotiating Scope, When the Date Is Fixed, Delivering Bad News, Disagree and Commit |
| 6 | Growing the Product | Sep 2026 → 2027 | **New markets**: Launching a New City ★, Localisation for Antwerp, Pricing Experiments · **Business customers**: B2B vs B2C Products (Korenwolf) ★, Account Needs vs Product Vision, Service Levels as Features · **Scaling the product**: Platform Thinking, Accessibility as Product Quality, Product-Led Growth · **Growing yourself**: Product Sense, Writing Product Principles, Growing as a PO ★, Handing Over a Product Area |

Each volume: 4 collections, 15 notes, like Book 1.

## 3. Vol. 1 story spine (Grace, October 2025 → January 2026)

| Note | Grace's scene | Meanwhile, in Ana's notebook |
| --- | --- | --- |
| Customer Interviews | 12 customers in her first two weeks. Surprise: they don't mind substitutes, they mind **not being asked**. | Stakeholder Map |
| Jobs to Be Done | Two jobs: “get tonight's dinner sorted without a trip out” (express) vs “do the weekly shop without losing a Saturday” (slots). Substitutions hurt each job differently. | Business Drivers |
| Proto-Personas / Journey Map | The express parent, the slot planner, the office manager (seed for Korenwolf). The journey breaks at “item unavailable”. | System Context |
| Opportunity Solution Tree ★ sample | Outcome: refund tickets **6 % → 2 %**. Opportunities: “I want a say”, “I want to know before the courier arrives”, “never substitute this”. Solutions: substitute approval in the app (2-minute window), a “no substitutes” flag, better stock data. | Event Storming (the substitutions hot spot), ASRs |
| Assumption Mapping | Riskiest assumption: customers answer within 2 minutes. | Constraints vs Assumptions |
| North Star Metric | **Perfect orders per week**: complete, on time, no refund ticket. | Quality Attribute Scenarios |
| Baseline Before You Build | Measuring today's 6 % properly: support tags were unreliable; Sam and Grace re-tag 400 tickets. | NFR Checklist |
| Concierge MVP ★ | Two weeks at Noord: Sam's team phones customers about substitutes by hand. 81 % answer within 2 minutes, 74 % accept. Evidence before code. | Spike vs Prototype vs PoC |
| Fake Door Test ★ | A “Larder for your office?” link in the app: 140 clicks in two weeks. Femke takes the number to the trade fair where she meets Korenwolf (January 2026). | Risk-Storming |
| Prototype Testing | A clickable substitution flow tested with 6 customers and 3 pickers (Tomás). | Walking Skeleton |
| Outcomes over Outputs | Femke's ML recipe idea (from an investor) is measured against the outcome and parked. Seeds “Saying No” in Vol. 2. | ASRs (recipes “not significant”) |

The two books share meetings: event storming on 21 October, the drivers meeting on 24 October, risk-storming on 4 December.
Write those scenes so the facts match exactly.

## 4. Note format

Same data shape as Book 1 (`content/architect-1/*.py`), with these options:

| Option | Value for Book 2 |
| --- | --- |
| `key` | `product-1` … `product-6` (flat, like `architect-N`) |
| `series`, `book` | `2`, `"The Product Owner's Notebook"` |
| `problem_h2` | “The situation” (a scene from Larder) |
| `map_caption`, `map_col` | “Translating it to the job” / “On the product” |
| `related_h3` | “Related notes” |
| `title_block`, `story` | as Book 1 |
| note `code` (`plain=True`) | template card: interview guide, opportunity tree, one-pager, story map… |
| note `try_it` | as Book 1 |
| **new** note `meanwhile` | list of `(journal key, slug, one line)`: a “Meanwhile, in Ana's notebook” box. The generator should also add the reverse box to the linked architect note automatically. |

**Ratings: `PRODUCT_ATTRS`** (proposal, see section 7):

| Rating | Question | Meaning |
| --- | --- | --- |
| Customer value | solves a real problem? | Customers would notice, and miss it if it went. |
| Business impact | moves a driver? | Shows up in a number the business tracks. |
| Evidence | based on facts? | Decided on what we learned, not on opinion or rank. |
| Learning speed | find out fast? | How soon we know if we're wrong. |
| Focus | fewer, better things? | The team works on few things at once. |
| Shared understanding | team knows why? | Everyone can explain what we're building and why. |
| Stakeholder trust | they believe us? | Leaders and partners trust the plan and the updates. |
| Flow | small steps to customers? | Value reaches customers in small, frequent steps. |
| Low overhead | light to run? | Time and ceremony it takes. High = light. |

## 5. Style proposal: the product board

Each book has its own skin; Book 2 should feel like a **product team's wall**:

- Desk: kraft-paper brown (#D9C29C) with a cork texture hint; sheets are **index cards** (#FFFDF5) with a red top rule.
- Palette: tomato red accent (#E4572E), teal (#1F9E89), marker blue (#2B59C3), sticky yellow (#FFD84D), sticky pink.
- Font: **Permanent Marker** for titles and section heads (a Sharpie on sticky notes); body fonts unchanged.
- Marks: section numbers on **push-pinned sticky notes**; TL;DR as an index card pinned at the corner; figures pinned
  with a pin instead of tape; the template card as a **story card**; a “Now / Next / Later” lane motif on the index page.
- Shared with Book 1: title block, “try it” box, “story so far”, layout and print rules.
- Cover on the shelf: tomato red (#C8432B), mustard band (#F2B33D).

## 6. Build checklist

1. [ ] Owner answers section 7.
2. [ ] `PRODUCT_ATTRS` and the `product-1` journal entry (copy `architect-1`).
3. [ ] `.theme-product` skin + cover colours; Permanent Marker font.
4. [ ] `meanwhile` field: render the box in both directions; add CSS.
5. [ ] Sample note: Opportunity Solution Tree; owner reviews look and voice.
6. [ ] Write the other 14 Vol. 1 notes; add each to the case file `TIMELINE` (book tag "2") and the casebook.
7. [ ] Book 2 on the case file: status and link; future log update.
8. [ ] Verify like Vol. 1 (figures contact sheets, 375 px, light/dark, PDFs, the exists check), PR, deploy when asked.

## 7. Open questions for the owner

1. **Six volumes × 15 notes** like Book 1, or a shorter book (for example four volumes)?
2. **The skin**: the product board (kraft, index cards, push pins, Permanent Marker), or something else?
3. **The ratings**: the nine above?
4. **Sample note**: Opportunity Solution Tree (it carries the substitutions story and pairs with Ana's event storming)?
5. **Order of work**: Grace's Vol. 1 next, then alternate volumes between the books? Or finish Ana's Vol. 2 first?
