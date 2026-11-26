# Handoff: Handbook 2 · Identity and Access in the Cloud

Status as of **2026-11-26**: **in progress, 14 of 25 chapters written: Parts I–III (1–14).** The owner approved
everything in `docs/HANDOFF-handbooks.md` §6 and picked Chapter 9 as the sample. **Next: Chapter 15** (Part IV),
then Parts V–VI in order (`BOOK["next"]` in `book.py` is 15).

Read first: `docs/HANDOFF-handbooks.md` §1–2 (what a handbook is, the voice, the building blocks, the look). This
book uses exactly the same style, blocks, CSS (`public/assets/book.css`) and build as Handbook 1. The best model to copy
from is `content/handbooks/cloud-networking/09-firewalls.html` (a chapter about rules and how they're evaluated).

## 1. Where things are

| What | Where |
| --- | --- |
| Outline (parts, chapters, summaries, topics, appendices) | `content/handbooks/cloud-identity/book.py` |
| Chapter bodies | `content/handbooks/cloud-identity/<nn>-<slug>.html`; written: 01–14 |
| Built contents page | `public/handbooks/cloud-identity/index.html` |
| Build | `python3 scripts/build_notes.py` (builds everything, including both handbooks and the landing shelf) |
| Preview | `npm run serve`, then http://localhost:8080/handbooks/cloud-identity/ |
| Story facts | `docs/larder-casebook.md`, section “Series 3 · Identity and Access in the Cloud” |

## 2. How the placeholder works (changed in this session)

- `scripts/build_handbooks.py`: `BOOKS` now lists `cloud-identity`. A book with **no written chapters** gets only its
  contents page: no `all.html`, no PDF, and **no `journals.json` entry** (so `npm run pdf` and the Pages workflow's
  “every page and PDF exists” check don't look for files that can't exist yet). `BOOK["next"]` (here `9`) shows a
  “next up” badge on that chapter and a sentence pointing to it.
- `scripts/build_notes.py` (`handbook_items`): an unstarted book's shelf card says “coming soon · 25 chapters planned”,
  its button reads “See the contents”, and there's no PDF button. Cards get `book--hb<no>`.
- `public/assets/bujo.css`: `.book--hb2` gives Handbook 2 its own cover (aubergine cloth `#2E2650`, violet band
  `#A08BE8`). The CSS hash changes every page's stylesheet link, so a build touches every page; that's expected.
- **When chapter 9 is written:** drop `09-policies.html` into the content folder and rebuild. Everything switches on
  by itself (chapter page, `all.html`, `journals.json` entries, PDF button, “1 of 25 chapters”). Then move `next` to
  the following chapter to write (suggest 1, then Part I in order), or delete it.

## 3. Chapter 9 (the sample): written 2026-11-26

What was built, against the brief below (kept for reference):
- 11 numbered sections (9.1–9.9 as briefed, 9.10 lab, 9.11 common mistakes), 3 figures (9.1 statement anatomy,
  9.2 ARN anatomy, 9.3 condition logic), 4 tables (9.1 ARNs, 9.2 condition operators, 9.3 managed/customer
  managed/inline, 9.4 across providers), 2 Azure/GCP boxes, 3 story boxes (opening, solved, rollout), quiz of 6.
- Final Dispatch policy has **four** statements (`ListOwnPrefixes` with an `s3:prefix` condition, `ReadConfig`,
  `WriteRoutePlans`, `ReadMapsKey` with the `-??????` secret suffix). TLS is enforced in the bucket policy, not here.
- Every JSON example in the chapter was parsed and is valid. Figures checked at 1280 px (light and dark) and 375 px
  (dark); no page-level horizontal overflow; all cross-references resolve to the contents page until those chapters exist.
- `public/assets/book.css`: code and diagram mono text now has ligatures switched off (JetBrains Mono drew
  `s3:::` as a ligature). Affects both handbooks, for the better.
  Also new: `table.wrap-code` lets long ARNs wrap inside a table; in print, long `pre` lines and table code wrap
  instead of being clipped (Handbook 1's PDFs had clipped lab commands too; they're fixed by the same rule).
- Chapter 9 printed to A4 for a check: 22 pages, nothing clipped.
- **Not done: the lab has not been run in a real AWS account** (no AWS credentials in the session). The commands are
  standard CLI v2, but run it once before calling the chapter final, especially step 7: the brief only promises an
  `ERROR` for the misspelled action and a `SECURITY_WARNING` for `iam:PassRole` on `*`; record what Access Analyzer
  says about `ListBucket` on an object ARN and tighten the text if it's definite.

### The original brief

Part II · IAM on AWS. Slug `policies`, file `09-policies.html`. 40–60 minutes. Lab: free (IAM is free; one S3 bucket
with a few small files costs well under $0.01; delete it at the end).

**Promise (opener):** by the end of the chapter, a policy is no longer a JSON blob you paste and hope about: you can read
any statement aloud as a sentence, write one that does exactly one job, and check it before it ships.

**Chapter card**
- By the end you can: *read* any IAM policy statement as a plain sentence; *write* an identity policy scoped to one
  bucket prefix and one secret; *narrow* a policy with conditions; *choose* between managed and inline policies;
  *validate* a policy with IAM Access Analyzer before you attach it.
- Before you start: Chapter 1 (principals, actions, resources), Chapter 6 (least privilege, default deny),
  Chapter 8 (roles and trust policies). Since those aren't written yet, cross-reference them as `href="#ch1"` etc.;
  the build links them to the contents page until they exist. Keep the chapter readable on its own: define every
  term it uses, even ones that Chapter 8 will define.
- Provider: AWS, with Azure and Google Cloud compared in §9.8.

**Story box (Larder, opening):** November 2026. Eli (platform tech lead) runs the account audit after Handbook 1's
network work. The Dispatch service's ECS task role (Dispatch moved to the managed container service under ADR 0010) has
one policy, copied from a blog post during the April move: `"Action": "s3:*", "Resource": "*"`. Dispatch actually needs
three things: read `config/` and write `routes/` in the bucket `larder-dispatch-prod` (Engine A's van route plans, ADR
0015), and read one secret, `dispatch/prod/maps-api-key`. Anyone who gets into a Dispatch container can read or delete
every bucket in the account, including the order exports. **Resolution (near the end):** a two-statement policy
plus one condition, validated with Access Analyzer, rolled out with a CloudTrail check that nothing Dispatch does is
now denied (that technique is taught properly in Chapter 11; promise it).

**Sections (numbered `9.1`…, ids `s9-1`…)**
1. **What a policy is.** A JSON document that grants or denies; where policies attach (identity vs resource: one
   paragraph, Chapter 10 does the rest). Default deny. *Key idea:* “Nothing is allowed until a statement allows it,
   and an explicit deny beats any allow.”
2. **Anatomy of a statement.** `Version` (always `2012-10-17`, and why: policy variables), `Statement`, `Sid`,
   `Effect`, `Action`, `Resource`, `Condition`, plus `Principal` (resource policies only). **Figure 9.1:** an annotated
   statement, each field labelled with the question it answers (who? may/may not, do what? to what? when?).
   Teach the habit: read a statement aloud as a sentence.
3. **Actions.** `service:Operation`, case-insensitive; wildcards (`s3:Get*`) and why they age badly (new actions get
   added later); `NotAction` and why it's a trap in allow statements. Where to look up actions: the Service
   Authorization Reference. Side note: an API call can need more than one action.
4. **Resources and ARNs.** ARN format `arn:partition:service:region:account:resource`; examples with empty region or
   account fields (S3, IAM); bucket ARN vs object ARN (**the most common S3 mistake**: `ListBucket` needs the
   bucket, `GetObject` needs `bucket/*`). **Table 9.1:** six ARNs taken apart. Resource-level support: some actions
   only accept `"*"`.
5. **Conditions.** Block structure (operator → key → values); AND between keys, OR between values; global keys
   (`aws:PrincipalOrgID`, `aws:SourceIp`, `aws:SecureTransport`, `aws:RequestedRegion`) vs service keys
   (`s3:prefix`); `…IfExists` and `ForAnyValue`/`ForAllValues` with a warning box on the empty-set trap.
   **Figure 9.2:** how a condition block evaluates (AND/OR tree).
6. **Policy variables and tags.** `${aws:username}`, `${aws:PrincipalTag/team}`, `${aws:ResourceTag/...}`; a first
   look at attribute-based access (ties back to Chapter 6; Chapter 12 uses it with SSO).
7. **Managed, inline, and how many.** AWS managed vs customer managed vs inline; versions and rollback; size limits
   (quote them “at the time of writing”); **Table 9.2:** when to use which. Warning box: `AdministratorAccess`,
   `PowerUserAccess` and the `*FullAccess` family in production.
8. **Across providers.** Azure: role definitions (`Actions`/`NotActions`/`DataActions`) + role assignments at a scope;
   conditions in ABAC. Google Cloud: predefined/custom roles bound to principals at a resource in the hierarchy; IAM
   Conditions in CEL. **Table 9.3:** policy vs role definition vs role binding, side by side. Key point: AWS attaches
   permission *documents* to principals; Azure and GCP *bind roles* to principals at a scope.
9. **Writing a least-privilege policy: a method.** `ol.steps`: list what the code calls → map to actions → narrow
   resources → add conditions → validate → test → watch CloudTrail. Worked through for Larder's Dispatch (resolution
   of the story box), ending with the final policy in a code block.

**Lab (`.box-lab`): “Give a role exactly one job”.** Needs: a sandbox account (Appendix C), the AWS CLI. Cost: free,
plus well under $0.01 for S3; clean-up commands at the end (delete objects, bucket, role, policy).
Steps: create bucket `<you>-iam-lab` with `config/` and `routes/` objects → create a role your user can assume →
attach the Dispatch-style policy → assume the role and try five calls (list, read config, write routes, write config,
read another bucket), predicting each result first → run `aws accessanalyzer validate-policy` on a deliberately
sloppy version and fix each finding. **Break it on purpose:** drop the `/*` from the object resource and watch
`GetObject` fail; use `s3:ListBucket` with `routes/*` as the resource and watch it fail. **Stretch:** add a condition
so writes need `aws:SecureTransport`; generate a policy from CloudTrail activity with Access Analyzer (preview of
Chapter 24). Run the lab once in a real account before publishing, and say so in the handoff (Handbook 1's Terraform
labs were never run; don't repeat that).

**Common mistakes (table):** bucket vs object ARN · `NotAction` in an allow · wildcard actions that grow · `"Resource":
"*"` for actions that support resources · condition on a key the action doesn't send (`…IfExists` confusion) ·
editing an AWS managed policy (you can't; copy it) · inline policies nobody can find.

**Summary (`sum9`), key terms, quiz:** 5–8 bullets; terms: policy, statement, effect, action, resource, ARN, condition,
condition key, policy variable, managed policy, inline policy, least privilege. Quiz of 6 (recall / apply / explain /
design / compare / debug), e.g. “read this statement aloud”, “why does this `ListBucket` fail?”, “write a policy for…”,
“compare an AWS policy with a GCP role binding”.

**Going further:** IAM User Guide (policy grammar, JSON element reference), Service Authorization Reference, IAM Access
Analyzer policy validation, Azure RBAC role definitions, Google Cloud IAM overview and IAM Conditions.

**Forward references to promise:** Chapter 8 (trust policies, the other half of a role), Chapter 10 (how all policy
types combine; explicit deny across policy types; SCPs), Chapter 11 (finding which statement denied), Chapter 18 (KMS
key policies), Chapter 21 (resource-based policies across accounts), Chapter 22 (`aws:PrincipalOrgID` perimeters),
Appendix A (policy cookbook: collect the chapter's final policies there).

**IDs:** prefix everything with 9: SVG markers `c9…`, sections `s9-<m>`, figures `fig9-<m>`, summary `sum9`. Figures
use the theme tokens (see the SVGs in Handbook 1 chapters 8–10) and have `<title>`/`<desc>`. Check figures at desktop
and 375 px, light and dark, with no horizontal overflow; check all links.

## 3a. Part I (chapters 1–6): written 2026-11-26

Provider-neutral foundations, each with a Larder story (Nov–Dec 2026, all in the casebook's identity section), two
figures, an “Across providers” section and a **stdlib-only Python lab that was run**; the outputs printed in the
chapters are the real outputs (ch. 2's timings are machine-dependent and say so; ch. 3–6 use fixed clocks or are
deterministic).

| Ch. | Story | Lab file (in the chapter) | Checked against |
| --- | --- | --- | --- |
| 1 | `ops` user shortens backup retention; nobody knows who | `access.py`, `access_personal.py` | run |
| 2 | credential stuffing, 310 accounts | `passwords.py`, `totp.py` | RFC 6238 test vectors |
| 3 | stolen phone keeps ordering after password change | `tokens.py` (HS256 JWT) | run; PyJWT decodes the same token |
| 4 | Spendwise wants a password → OAuth client | `oauth.py` (imports `tokens.py`) | RFC 7636 test vector |
| 5 | Korenwolf SAML SSO, live 18 Dec | `saml.py` (no signature check; says so) | run |
| 6 | stock tool roles, Tomás's leftover Zuid role | `models.py` (RBAC/ABAC/ReBAC) | run |

Every “break it on purpose” step was also run and behaves as described. Lab 3's `verify()` omits “may …” when a token
has no scope (needed by ch. 4); ch. 3's printed outputs are unchanged by that.

Checks: no duplicate ids or broken `aria-labelledby`/marker references across `all.html`; every page at 1280 px
(light, dark) and 375 px (dark) has no horizontal overflow; all 12 figures inspected; sequence-diagram step labels use
`halo-priv` so lifelines don't cross the text; print (A4) check: no `pre`, table or figure is clipped in either book
(the whole of Handbook 2 so far prints to 117 pages).

**Dates to respect:** the security review with “non-expiring business API keys” and “other office's orders by ID” is
**11 Oct 2027** (Ana, Vol. 5), not 2026; Part I avoids it (ch. 6 warns about object-level checks in general). Ch. 19
should move forward in time to tell it.

## 3b. Rest of Part II (chapters 7, 8, 10, 11): written 2026-11-26

| Ch. | Story (all in the casebook) | Lab | Run here? |
| --- | --- | --- | --- |
| 7 | root key from 2024, root email on Jasper's closed mailbox; recovery | CLI checks + `credcheck.py` on a sample credential report | Python part **run**; CLI part not |
| 8 | 11 IAM users, 3 leavers; `ops` becomes role `prod-operator` (MFA, source identity) | create, assume, inspect a role | **not run** (CLI only) |
| 10 | `protect-orders-db` guardrail; Ben's “I'm an admin”; `deploy-bot` gap; `team-boundary` | `evaluate.py` (Figure 10.1 in Python, 8 cases) + optional `simulate-custom-policy` | Python **run** (incl. every “break it” edit); CLI not |
| 11 | staging uploads denied on `kms:GenerateDataKey` via S3 | `denied.py` on sample CloudTrail events + CLI denials, decode, simulator | Python **run** (3 input formats); CLI not |

Checks run for this batch: every lab script and sample file printed in chapters 1–11 was extracted from the HTML and
compared byte for byte with the file that was executed (all match); every JSON example parses; no duplicate ids or
broken references; figures inspected at 1280 px light/dark and pages at 375 px (no overflow); print clip check clean.

Facts worth knowing for later chapters: Larder has **two standalone accounts** (prod `111122223333`, dev+staging
`444455556666`) and no organisation yet (ch. 7). FIDO2 keys don't work for MFA-protected CLI/API calls; Larder's
on-call engineers use an authenticator app for the CLI (ch. 8) until SSO (ch. 12). Ch. 12 must delete `ops` and the
remaining IAM users; ch. 14 defines `break-glass-*`; ch. 17 replaces `deploy-bot`; ch. 18 decides on customer managed
KMS keys; ch. 20 moves `protect-orders-db` into an SCP (the organisation itself, with a fresh management account
`777788889999`, is created in ch. 12; `111122223333` stays a member running production); ch. 23 covers root-sign-in alerts and the S3 data-event trail.

## 3c. Part III (chapters 12–14): written 2026-11-26

| Ch. | Story (all in the casebook) | Lab | Run here? |
| --- | --- | --- | --- |
| 12 | Jan 2027: new management account + organisation; Identity Center; IAM users gone by 1 Feb | `assignments.py` (access matrix + risky assignments) + sandbox-org CLI walkthrough | Python **run**; CLI not |
| 13 | May 2027: Pim kept helpdesk/billing 3 weeks; ADR 0021; Identity Center → IdP + SCIM on 7 Jun | `jml.py` (HR vs apps → SCIM-shaped actions) | **run** |
| 14 | 18 Dec 2026 near miss; TEAM elevation and break-glass in Feb 2027 | `jit.py` (elevation broker) + EventBridge break-glass alarm | Python **run**; AWS part not |

Every “change it” and “break it” step was run against the scripts; all 14 lab scripts printed in chapters 1–14 are
byte-identical to the executed files; JSON snippets (SCIM body, EventBridge pattern, topic policy) parse.

Decisions made in this batch (now in the casebook): the organisation is created in **ch. 12** from a **new, empty
management account `777788889999`**; Jasper's `111122223333` stays a member running production (ch. 7's forward
reference was updated). Identity Center can't revoke already-issued role credentials by itself: ch. 13 uses AWS's
documented `identitystore:UserId` deny method (the `AWSReservedSSO_` roles can't be edited). Dates: Christmas 2026 has
**no** change freeze (the 13 Dec–3 Jan freeze in the casebook is Christmas 2027, Ana Vol. 5); the 18 Dec 2026 outage's
cause is Ana's (slow DB failover) and ch. 14 adds only an access near miss to that evening.

For Part IV: ch. 15 workloads (Dispatch on ECS, Larder Core on 3 VMs → instance profiles + IMDSv2, SSM instead of
SSH), ch. 16 (Larder runs no Kubernetes as of early 2027; Handbook 1 ch. 19 mentions pods in `100.64.0.0/10` as a
plan; decide before writing), ch. 17 replaces `deploy-bot` with GitHub OIDC, ch. 18 decides customer managed KMS keys
(staging's leftover CMK from ch. 11), ch. 19 retells the Oct 2027 security review (move forward in time).

## 4. Order of work after Chapter 9

1. Chapter 9 (above). Update this file and `docs/HANDOFF-handbooks.md`.
2. Part I in order (1–6), then Part II (7, 8, 10, 11), then Parts III–VI in order, then the appendices, as with Handbook 1.
3. Keep the storyline consistent with the casebook section; add every new fact there.

## 5. Open checks

- [x] Chapter 9 written, built, checked (desktop + 375 px, light + dark, links).
- [ ] Chapter 9 lab run once in a real AWS account (see §3).
- [ ] Confirm the Pages workflow passes now that this book has PDFs (chapter 9 + whole book).
- [x] Part I (1–6) written and checked.
- [x] Rest of Part II (7, 8, 10, 11) written and checked.
- [ ] AWS labs (ch. 7–11) run once in a real sandbox account; none could be run here.
- [x] Part III (12–14) written and checked.
- [ ] Chapter 15 next.
