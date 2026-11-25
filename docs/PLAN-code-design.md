# Plan: the code-design volumes (Series 1, Vols. 7 and 8)

Agreed with the owner on 18 Nov 2026: continue Series 1 (the design pattern journals) rather than start a new series,
with two volumes on how to structure the code inside one service. AI App Patterns moves from Vol. 7 to Vol. 9.

| Vol. | Journal key | Title | State |
| --- | --- | --- | --- |
| 7 | `ddd` | Domain-Driven Design | **written** (18 notes, branch `ccr-9390f8f0-wl14yb`) |
| 8 | `inside-app` | Inside the Application | **written** (18 notes, same branch, section 4) |
| 9 | — | AI App Patterns | planned, after Vol. 8 |

## 1. Why these volumes, and the honest question

The classic sources (Evans 2003, Fowler's *Patterns of Enterprise Application Architecture* 2002, the GoF book 1994,
SOLID as named around 2000–2004) are twenty years old or more. They did not age evenly: some ideas matter more now
(bounded contexts, value objects), some are built into every framework (repository, unit of work), some were rethought
(services, specifications) and a few are best retired (Singleton, server session state). The volumes say so openly.

## 2. The “then & now” box (new, for both volumes)

Every note in Vols. 7 and 8 carries a `then_now` field, rendered just before “Gains vs losses”:

```python
then_now=dict(src="Evans, 2003", verdict="core",
              then="what the original book said",
              now="what changed by 2026",
              take="one-line verdict"),
```

- Verdicts (`VERDICTS` in `scripts/build_notes.py`): `core` (still core), `grown` (matters more now), `built-in`
  (built in now), `rethought` (rethought), `retired` (mostly retired).
- The journal sets `then_now=True`: the index shows a verdict tag on every note, and a **Then & now** key with counts.
- Styles: `.thennow`, `.verdict-*`, `.verdict-tag` in `public/assets/bujo.css` (shared by every skin, light and dark,
  stacks to one column on phones, never splits across a printed page).
- Any other volume can use it later; a note without `then_now` renders as before.

## 3. Vol. 7 · Domain-Driven Design (written)

Skin `theme-ddd`: a surveyor's field map (cream paper, faint contour lines, forest green, sea blue pen, ochre tape),
a dashed frontier under titles, a compass stamp on the TL;DR, round survey-marker section numbers. Cover: map
sticker on contour cloth, `--cover-ddd` / `--band-ddd`. Ratings: `CODE_ATTRS` (simplicity, domain clarity,
correctness, changeability, testability, low coupling, performance, low ceremony, team scalability), shared with Vol. 8.
Running example: an online shop (catalogue, pricing, ordering, shipping, billing). Code in TypeScript.

| # | Note | Collection | Verdict |
| --- | --- | --- | --- |
| 01 | Ubiquitous Language | Finding the domain | still core |
| 02 | Core, Supporting & Generic Subdomains | Finding the domain | matters more now |
| 03 | Bounded Context | Finding the domain | matters more now |
| 04 | Event Storming | Finding the domain | matters more now |
| 05 | Context Map | Between contexts | still core |
| 06 | Customer–Supplier & Conformist | Between contexts | still core |
| 07 | Shared Kernel & Partnership | Between contexts | rethought |
| 08 | Anti-Corruption Layer | Between contexts | still core |
| 09 | Open Host Service & Published Language | Between contexts | built in now |
| 10 | Value Object | Building blocks | matters more now |
| 11 | Entity | Building blocks | still core |
| 12 | Aggregate | Building blocks | matters more now |
| 13 | Domain Events | Building blocks | matters more now |
| 14 | Repository | Building blocks | built in now |
| 15 | Domain & Application Services | Building blocks | rethought |
| 16 | Specification | Keeping it honest | rethought |
| 17 | Make Illegal States Unrepresentable | Keeping it honest | matters more now |
| 18 | Anemic Domain Model | Keeping it honest | rethought |

Every note has the full Series 1 layout plus `quiz_sit` (a “what would you do?” question) and `try_it`, so it matches
the revised earlier volumes. Overlaps with Series 2 (Ana's Bounded Contexts, Domain Discovery, Anti-Corruption Layer)
are linked both ways through related notes; Ana's notes tell the Larder story, these give the pattern.

Not yet done for Vol. 7 (candidates for a later pass, like the earlier volumes got): four going-deeper chapters
(`content/ddd/deeper.py`; suggested: Aggregate, Bounded Context, Domain Events, Anti-Corruption Layer), and a deep dive
“Designing Aggregates” for Series 3.

## 4. Vol. 8 · Inside the Application (written)

SOLID, the patterns inside your ORM, how to shape an application, and the classic object patterns that still earn
their place. Same ratings (`CODE_ATTRS`) and the then & now box. Skin `theme-app`: a green engineering pad (5 mm grid,
heavier every fifth line), rust accent, a ruler under titles, a code-review “✓ LGTM” stamp on the TL;DR, square
section numbers. Cover: hexagon sticker (new `hexagon` icon in `scripts/doodle.py`) on brick-red grid cloth, mint band.
Running example: the same online shop, now inside the Ordering service. Final verdicts: 6 still core, 4 matters more
now, 4 built in now, 3 rethought, 1 mostly retired (the museum).

| # | Note | Collection | Source | Expected verdict |
| --- | --- | --- | --- | --- |
| 01 | Single Responsibility | SOLID | Martin, 2000s | rethought (“one reason to change” = one actor, not one method) |
| 02 | Open–Closed | SOLID | Meyer 1988, Martin | rethought (extend by composition and functions, not inheritance) |
| 03 | Liskov Substitution | SOLID | Liskov 1987 | still core |
| 04 | Interface Segregation | SOLID | Martin | still core |
| 05 | Dependency Inversion | SOLID | Martin | matters more now (ports and adapters, testing) |
| 06 | Active Record vs Data Mapper | Inside your ORM | Fowler, PoEAA | built in now (Rails, Laravel vs Hibernate, EF Core) |
| 07 | Unit of Work & Identity Map | Inside your ORM | Fowler, PoEAA | built in now (DbContext, Session) |
| 08 | Lazy Loading | Inside your ORM | Fowler, PoEAA | built in now, use sparingly (N+1, link to Vol. 3) |
| 09 | Offline Locks & ETags | Inside your ORM | Fowler, PoEAA | still core (optimistic offline lock = ETag / If-Match) |
| 10 | DTOs & Remote Facade | Inside your ORM | Fowler, PoEAA | rethought (API contracts, GraphQL, BFF) |
| 11 | Transaction Script vs Domain Model | Shaping the app | Fowler, PoEAA | still core (the real choice behind “anemic”) |
| 12 | Ports & Adapters (Hexagonal) | Shaping the app | Cockburn, 2005 | matters more now |
| 13 | Vertical Slices | Shaping the app | Bogard, 2018 | matters more now (vs layered and clean/onion) |
| 14 | Functional Core, Imperative Shell | Shaping the app | Bernhardt, 2012 | matters more now |
| 15 | Strategy & Command as Functions | Classic patterns | GoF, 1994 | built in now (first-class functions, lambdas) |
| 16 | Decorator & Middleware | Classic patterns | GoF | still core (HTTP middleware, interceptors) |
| 17 | Adapter & Facade | Classic patterns | GoF | still core |
| 18 | The Pattern Museum | Classic patterns | GoF, PoEAA | mostly retired (Singleton, Visitor outside compilers, Page/Front Controller, Template View, Table Module, Row Data Gateway, server session state) |

Decisions taken with defaults (the owner said “let's build volume 8” without answering the three questions):
1. The GoF patterns stay at the four notes above; a volume of their own remains possible later.
2. Fowler's *Refactoring* as a cheat sheet: **done** (18 Nov 2026, `content/cheatsheets/refactoring.py`, `/cheatsheets/refactoring/`),
   linked from SRP, Open–Closed, Liskov, Transaction Script, Strategy & Command, Value Object, Anemic Domain Model and
   Characterization Tests through `CARD_LINKS`. Cards as planned: smells by family (bloaters, change preventers, couplers, dispensables), the smell → refactoring
   map, the most-used refactorings with before/after code, and safe-refactoring habits (tests first, tiny steps).
3. Skin: the green engineering pad described above; easy to change in `bujo.css` (`theme-app`).

## 5. How a code-design volume was added (the routine Vol. 9 · Data Pipelines followed, and later ones)

1. Add the journal to `JOURNALS` after the previous one with `attrs=CODE_ATTRS`, `then_now=True`, a new `theme`, and move its
   entry out of `PLANNED`.
2. Content in `content/<key>/01_*.py` … `04_*.py`, each note with `then_now`, `quiz_sit` and `try_it`.
3. Theme CSS next to `theme-ddd` (light, dark, print), `--cover-*` / `--band-*`, `.book--<key>`, `COVER_ART`.
4. Build, check that the `[links]` count did not grow, contact-sheet every figure, 375 px check, light and dark,
   `PDF_JOURNALS=<key>` PDF run. Update the README, `docs/HANDOFF.md` and the future log.
