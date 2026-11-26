# Handoff: Jef's Handbooks (Series 3). Draft for review

Status as of 2026-11-26: **proposal.** The style, the outline of Handbook 1 (*Networking in the Cloud*) and one
sample chapter (Chapter 8) are written. Nothing is linked from the landing page yet: the owner reviews first.

- Contents page: `public/handbooks/cloud-networking/index.html`
- Sample chapter: `public/handbooks/cloud-networking/08-inside-a-vpc.html`
- Preview: `npm run serve`, then open http://localhost:8080/handbooks/cloud-networking/
- Sources: `content/handbooks/cloud-networking/book.py` (outline), `…/08-inside-a-vpc.html` (chapter body),
  `scripts/build_handbooks.py` (build), `public/assets/book.css` (skin)

## 1. What the series is, and how it differs from the notebooks

| | Series 1–2 · Notebooks | Series 3 · Handbooks |
| --- | --- | --- |
| Unit | a note: one pattern or practice, 1–2 screens | a chapter: one topic in depth, 30–60 minutes |
| Shape | the same eight sections in every note | a toolbox of parts; each chapter uses the ones its topic needs |
| Voice | a student's or practitioner's journal, doodles | a patient teacher writing a book; precise diagrams |
| Goal | recognise and compare patterns | **competence**: the reader can design, build and debug it |
| Reader | already in the field | knows a little; finishes the book able to do the work |
| Sequence | notes stand alone | chapters build on each other; Part I is the foundation |

## 2. The style

### Voice

- Comprehensive, but **easy to digest**: one idea at a time, in the order a learner needs them. Concept → picture → worked
  example → hands-on → check.
- Plain, direct sentences. Second person (“you”). Define every term the first time, and mark it with `.term`.
- Concrete before abstract: real addresses (`10.20.17.8`), real prices (“about $0.05 an hour, at the time of writing”),
  real commands. Use documentation ranges (`198.51.100.0/24`, `203.0.113.0/24`) for public IPs.
- Explain **why**, not only what: every rule of thumb carries its reason.
- No hype, no filler, no unexplained acronyms. Cross-reference instead of repeating (“Chapter 9 covers this”).
- Provider-neutral concepts first; then **AWS as the main worked provider**, with Azure and Google Cloud compared in an
  “Across providers” section in every chapter where they differ.

### Building blocks (pick per chapter)

| Block | Class | Use |
| --- | --- | --- |
| Chapter opener | `.opener` | part, big chapter number, title, a one-paragraph promise |
| Chapter card | `.chapter-card` | “By the end you can” (3–5 verbs a reader can check), “Before you start” (linked prerequisites), time, lab, provider |
| Story box | `.box-story` | the running example (Larder): a problem at the start, solved near the end |
| Numbered sections | `h2.sec` with `.n` | `8.1`, `8.2`… sections are a real sequence, so they're numbered |
| Side note | `aside.side` | names, rules of thumb, asides; in the margin on wide screens, inline on phones |
| Key idea | `.box-key` | the one sentence to remember; at most 2–3 per chapter |
| Watch out | `.box-warn` | a trap that costs money, security or an outage |
| On &lt;provider&gt; | `.box-provider` | how Azure or Google Cloud differ |
| Figure | `figure` + inline SVG `.dg` | precise diagrams that use the theme's tokens; numbered “Figure 8.1”, with `<title>`/`<desc>` |
| Table | `.table-wrap` + `caption` | numbered “Table 8.2”; comparisons, sizes, worked examples |
| Steps | `ol.steps` | procedures and checklists, where order matters |
| Lab | `.box-lab` + code | build it: goal, needs, **cost and clean-up**, steps, “break it on purpose”, stretch goals |
| Common mistakes | table | mistake → what happens → instead |
| Summary, key terms, quiz | `.summary`, `.terms`, `.quiz` | 5–8 bullets; glossary; 5–6 questions tagged recall / apply / explain / design / compare, answers in `<details>` |
| Going further | list | official docs first |

Rules: one job per box (don't use a warning box for emphasis); every figure and table earns its place; a chapter that
isn't hands-on can skip the lab and use a worked design exercise instead.

### Look

- Printed technical book, not a notebook: cool paper, ink, a cable blue-green accent, signal orange for warnings, green
  for labs, violet for key ideas. Literata (body), Archivo (headings, diagrams), JetBrains Mono (code).
- One ~68-character reading column plus a margin column for side notes (≥ 1100 px).
- Light and dark themes from tokens; prints to A4 (answers shown, navigation hidden).

## 3. Handbook 1 · Networking in the Cloud

Audience: developers, operators and new cloud engineers who use the cloud but find networking a black box.
Outcome: design, build and debug a production network on AWS, and read one on Azure or Google Cloud.
Running example: **Larder** (one region, Frankfurt, three zones; stores on Wi-Fi + 4G VPN; external PSP and StockPilot).

| Part | Chapters |
| --- | --- |
| I · How networks work | 1 What happens when you open a web page · 2 IP addresses and CIDR without fear · 3 TCP, UDP and ports · 4 Routing · 5 DNS · 6 HTTP, TLS and certificates |
| II · Your network in the cloud | 7 Regions, zones and the shape of a cloud network · **8 Inside a VPC (sample)** · 9 Firewalls: security groups and NACLs · 10 Planning your IP address space |
| III · Connecting networks | 11 Peering, transit gateways and hubs · 12 Private access to cloud services · 13 Site-to-site VPN and BGP · 14 Dedicated connections · 15 DNS across clouds and data centres |
| IV · Traffic in and out | 16 Load balancers · 17 CDNs, WAF and DDoS · 18 Controlling egress |
| V · Modern workloads | 19 Containers and Kubernetes · 20 Serverless and managed services · 21 Service mesh and zero trust |
| VI · Running it | 22 Observing and troubleshooting · 23 The cost of moving bytes · 24 Networks as code and landing zones · 25 Capstone: Larder's network end to end |
| Appendices | A CIDR cheat sheet · B AWS/Azure/GCP translation table · C Lab setup and cost safety · D Glossary · E Answers |

Full chapter summaries and topic lists: `content/handbooks/cloud-networking/book.py`.

### New Larder facts (Series 3)

VPC `10.20.0.0/16`, eu-central-1 · public `10.20.0–2.0/24` · app `10.20.16.0/20`, `10.20.32.0/20`, `10.20.48.0/20` ·
data `10.20.64–66.0/24` · `10.20.128.0/17` spare · other Larder networks in `10.0.0.0/8` via a transit gateway ·
NAT Elastic IP `198.51.100.7` (StockPilot allow-lists it). Chapter 9 should retell the casebook's 29 Oct 2026 incident
(a network rule change cut Dispatch off from Postgres for 25 minutes). Add these to `docs/larder-casebook.md` once approved.

## 4. Open questions for the owner

1. Series name (“Jef's Handbooks”) and book title (“Networking in the Cloud: from packets to landing zones”)?
2. AWS as the main provider, with Azure and Google Cloud compared, or equal weight to all three?
3. Keep Larder as the running example?
4. Length: 25 chapters at ~45 minutes each. Shorter (≈18, merging Part V into others)?
5. Labs that cost a little money (with clean-up steps), or console-free/free-tier-only labs?
6. Next handbooks to plan (e.g. Kubernetes, Databases, Security)?

## 5. Build checklist once approved

1. [ ] Owner answers section 4; adjust the style and outline.
2. [ ] Landing page: a Series 3 shelf (`build_notes.py`), and `journals.json` entries so the PDF workflow covers chapters.
3. [ ] Write Part I, then Part II in order (chapters depend on each other).
4. [ ] Per chapter: diagrams checked at desktop and 375 px, light and dark; labs run once in a real account; links checked.
