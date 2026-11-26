# Handoff: Jef's Handbooks (Series 3). Draft for review

Status as of 2026-11-26: **approved and in progress.** Owner decisions: title OK, AWS as the main provider, Larder as
the running example, 25 chapters, labs may cost up to about $1 (with clean-up steps). Written: Parts I and II
(chapters 1–10). The book is on the landing page (Series 3 shelf) and in `journals.json` (chapter PDFs + whole-book PDF).

- Contents page: `public/handbooks/cloud-networking/index.html`
- Sample chapter: `public/handbooks/cloud-networking/08-inside-a-vpc.html`
- Preview: `npm run serve`, then open http://localhost:8080/handbooks/cloud-networking/
- Sources: `content/handbooks/cloud-networking/book.py` (outline), `…/<nn>-<slug>.html` (chapter bodies; a chapter is
  “written” when its file exists), `scripts/build_handbooks.py` (build; also run by `build_notes.py`),
  `public/assets/book.css` (skin)
- Build: `python3 scripts/build_notes.py` builds everything, including the handbooks, the landing shelf and `all.html`.
- IDs must be unique across the book (all chapters share `all.html`): prefix SVG markers `c<n>…`, sections `s<n>-<m>`,
  figures `fig<n>-<m>`, summary `sum<n>`. Cross-references are written `href="#ch<n>"`.

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

Company plan inside `10.0.0.0/8` (ch. 10): offices `10.0.0.0/13`, stores `10.8.0.0/13` (one /16 per city),
Frankfurt `10.16.0.0/12` (hub `10.16`, dev `10.17`, staging `10.18`, spare `10.19`, prod `10.20`), second region
`10.32.0.0/12`, pods `100.64.0.0/10`; Korenwolf also uses `10.20.0.0/16` → PrivateLink (ch. 10, 12).
Office Amsterdam `10.1.0.0/24`; Amsterdam stores `10.8.0.0/16` (Noord `10.8.3.0/24`,
router `10.8.3.1`); Rotterdam stores `10.9.0.0/16`; store VPNs use BGP after the Rotterdam missing-route incident (ch. 4).
Jasper's first VPC was `172.17.0.0/16` and clashed with Docker (ch. 2). Public API `api.larder.example` (TTL incident,
ch. 5); webhooks `hooks.larder.example` (missing intermediate, ch. 6); payment client resets via NAT idle timeout (ch. 3).
VPC `10.20.0.0/16`, eu-central-1 · public `10.20.0–2.0/24` · app `10.20.16.0/20`, `10.20.32.0/20`, `10.20.48.0/20` ·
data `10.20.64–66.0/24` · `10.20.128.0/17` spare · other Larder networks in `10.0.0.0/8` via a transit gateway ·
NAT Elastic IP `198.51.100.7` (StockPilot allow-lists it). Chapter 9 should retell the casebook's 29 Oct 2026 incident
(a network rule change cut Dispatch off from Postgres for 25 minutes). Add these to `docs/larder-casebook.md`.

## 4. Decisions (owner, 2026-11-26)

1. Title and series name: OK. 2. AWS main provider: OK. 3. Larder stays. 4. 25 chapters. 5. Labs up to ~$1.

## 5. Progress and checklist

1. [x] Landing page: Series 3 shelf; `journals.json` entries for chapter and whole-book PDFs.
2. [x] Part I: chapters 1–6. [x] Part II: chapters 7–10.
3. [ ] Part III (11–15), then Parts IV–VI in order, then the appendices. Forward references already promise:
   ch. 11 transit gateway appliance mode and SG referencing; ch. 12 builds Larder's PrivateLink endpoint service for
   Korenwolf (NLB + endpoint service); ch. 13 BGP for store VPNs and MTU; ch. 19 pods in `100.64.0.0/10`;
   ch. 22 flow logs and Reachability Analyzer; ch. 25 second region (`10.32.0.0/12`) and DNS failover.
4. Lab code: the Python labs (ch. 2, 4, 10) were run and print what the text says. The Terraform labs (ch. 8, 9)
   were not run or validated (Terraform wasn't available in the session); run `terraform validate` and one real apply.
5. Per chapter: figures checked at desktop and 375 px, light and dark (no horizontal overflow); labs not yet run in a
   real account (owner or a later session should run the AWS labs once); links checked.

## 6. Handbook 2 · Identity and Access in the Cloud (approved 2026-11-26)

**Approved by the owner on 2026-11-26** (all six decisions below: yes; sample = Chapter 9; on the shelf now as a
placeholder). Status, how the placeholder works, and the full Chapter 9 brief: **`docs/HANDOFF-handbook-2-identity.md`**.

Outline: `content/handbooks/cloud-identity/book.py` (same format as Handbook 1). Listed in `BOOKS`; until a chapter
is written, only its contents page is built (no PDF, not in `journals.json`).

Audience: developers, operators and new cloud engineers who copy IAM policies and hope. Outcome: design
least-privilege access for people and workloads on AWS, debug any “access denied”, and read the same on Azure/GCP.
Same style, blocks and look as Handbook 1 (§2). Labs are nearly free (IAM costs nothing); a few touch KMS
(~$1/key/month, delete at the end) or Secrets Manager (~$0.40/secret/month).

| Part | Chapters |
| --- | --- |
| I · How access works | 1 Who are you, and what may you do? · 2 Passwords, MFA and passkeys · 3 Sessions and tokens · 4 OAuth 2.0 and OpenID Connect · 5 SAML and federation · 6 Access models: roles, attributes and relationships |
| II · IAM on AWS | 7 The AWS account and its root user · 8 Users, groups and roles · **9 Reading and writing IAM policies (sample)** · 10 How AWS decides: policy evaluation logic · 11 Debugging “access denied” |
| III · Access for people | 12 Single sign-on with IAM Identity Center · 13 Joiners, movers and leavers · 14 Privileged access and break-glass |
| IV · Access for software | 15 Identities for workloads · 16 Kubernetes and workload identity · 17 CI/CD without long-lived keys · 18 Secrets and encryption keys · 19 Service-to-service and API access |
| V · Many accounts | 20 AWS Organizations and guardrails · 21 Cross-account access and resource sharing · 22 Data perimeters |
| VI · Running it | 23 Auditing and detecting misuse · 24 Identity as code and least privilege at scale · 25 Capstone: Larder's identity end to end |
| Appendices | A Policy cookbook · B AWS/Azure/GCP translation table · C Lab setup and safety · D Glossary · E Answers |

Links to the rest of the shelf: ch. 4 and 6 go deeper than the Security Patterns notebook (OAuth + PKCE, Least
Privilege, Short-Lived Tokens, Zero Trust) and cite it; ch. 16 pairs with Handbook 1 ch. 19; ch. 22 builds on
Handbook 1 ch. 12 (endpoint policies) and ch. 24 (landing zones); ch. 21 picks up the account layout from Handbook 1 ch. 10.

### Larder storyline (approved; now in `docs/larder-casebook.md`, “Series 3 · Identity and Access in the Cloud”)

Must not contradict the casebook: ADR 0021 (24 May 2027, staff tools SSO/SCIM) and the 11 Oct 2026 security review
(non-expiring business API keys, unsigned webhooks) are reused, not rewritten.

- **The starting point (Nov 2026 audit, ch. 7–8):** the original account Jasper opened in 2024 still has a root
  access key from that year and root MFA on a phone nobody can find; 11 IAM users with console passwords, 3 of them
  for people who have left; engineers share an `ops` user for production fixes.
- **The deploy key (ch. 17):** CI deploys with a long-lived access key for `deploy-bot` with `AdministratorAccess`,
  stored as a repository secret; replaced by GitHub OIDC with one role per environment.
- **Accounts (ch. 20–21):** the hub/dev/staging/prod accounts from Handbook 1 ch. 10 become OUs in one
  organisation; Jasper's account becomes the management account and runs no workloads.
- **People (ch. 12–14):** Identity Center with the company IdP; permission sets `ReadOnly`, `Developer`,
  `ProdOperator` (just-in-time, approved by a tech lead); two break-glass users in a safe. Ch. 13 links to ADR 0021.
- **Partners (ch. 19, 21):** StockPilot and the PSP use cross-account roles with external IDs or signed requests;
  Korenwolf's business API keys expire after 90 days (from the Oct 2026 review).

### Owner decisions (all approved 2026-11-26)

1. Title and subtitle. 2. 25 chapters in six parts, as above. 3. AWS main provider again. 4. The Larder storyline
facts above. 5. Sample chapter: **9** (policies). 6. On the Series 3 shelf now, as “coming soon”.
