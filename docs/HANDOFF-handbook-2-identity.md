# Handoff: Handbook 2 · Identity and Access in the Cloud

Status as of **2026-11-26**: **in progress, 1 of 25 chapters written: Chapter 9 (the sample).** The owner approved
everything in `docs/HANDOFF-handbooks.md` §6 (title, 25 chapters in six parts, AWS as main provider, the Larder
storyline, show it on the shelf now) and picked Chapter 9 as the sample. **Next: Chapter 1**, then Part I in order
(`BOOK["next"]` in `book.py` is set to 1, which puts the “next up” badge on the contents page).

Read first: `docs/HANDOFF-handbooks.md` §1–2 (what a handbook is, the voice, the building blocks, the look). This
book uses exactly the same style, blocks, CSS (`public/assets/book.css`) and build as Handbook 1. The best model to copy
from is `content/handbooks/cloud-networking/09-firewalls.html` (a chapter about rules and how they're evaluated).

## 1. Where things are

| What | Where |
| --- | --- |
| Outline (parts, chapters, summaries, topics, appendices) | `content/handbooks/cloud-identity/book.py` |
| Chapter bodies | `content/handbooks/cloud-identity/<nn>-<slug>.html`; written: `09-policies.html` |
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

## 4. Order of work after Chapter 9

1. Chapter 9 (above). Update this file and `docs/HANDOFF-handbooks.md`.
2. Part I in order (1–6), then Part II (7, 8, 10, 11), then Parts III–VI in order, then the appendices, as with Handbook 1.
3. Keep the storyline consistent with the casebook section; add every new fact there.

## 5. Open checks

- [x] Chapter 9 written, built, checked (desktop + 375 px, light + dark, links).
- [ ] Chapter 9 lab run once in a real AWS account (see §3).
- [ ] Confirm the Pages workflow passes now that this book has PDFs (chapter 9 + whole book).
- [ ] Chapter 1 next, then Part I in order.
