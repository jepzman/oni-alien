# Refactoring · a laminated reference card in four pages: code smells, smell → refactoring map, the core
# refactorings (before → after, TypeScript), and how to refactor safely.
# Names follow Martin Fowler, Refactoring, 2nd ed. (2018). Smell families after Mäntylä (2003).
# Rendered by scripts/build_notes.py (render_cheatsheet); Diagram, code and box come from scripts/cheatsheet.py.
# Boxes flow into a 3-column grid (dense packing), so order them to fill rows: wide (2) + narrow (1).

SLUG = "refactoring"
TITLE = "Refactoring"
SUBTITLE = "code smells, the refactorings that fix them, and how to change code safely"
DESC = ("A four-page refactoring cheat sheet after Martin Fowler's Refactoring (2nd edition): the 24 code smells grouped "
        "by family, a smell-to-refactoring map, the core refactorings with before and after code, and habits for "
        "refactoring safely in small steps, including legacy code and IDE shortcuts.")
VERSION = "v1 · Nov 2026"
BLURB = ("Four laminated pages: the 24 code smells by family, which refactoring fixes which smell, the core refactorings "
         "before and after, and how to change code in small, safe steps.")
LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
        '<path d="M9 24l9-9" stroke="var(--b-dev)" stroke-width="2.6" stroke-linecap="round"/>'
        '<path d="M17 9a5 5 0 0 0 7 7l2 2-3 3-2-2a5 5 0 0 0-7-7z" fill="none" stroke="var(--b-feat)" stroke-width="2.2" stroke-linejoin="round"/>'
        '<circle cx="9" cy="24" r="2.4" fill="var(--b-rel)"/></svg>')


def smells(rows):
    """A list of smells: (name, what it looks like)."""
    return '<dl class="kv">' + "".join(f"<dt>{n}</dt><dd>{w}</dd>" for n, w in rows) + "</dl>"


# ---------------------------------------------------------------- page 1 · code smells
def families():
    d = Diagram("The 24 code smells from Fowler's Refactoring, second edition, grouped into five families: bloaters "
                "(code that grew too big), change preventers (one change, many edits), couplers (too much knowledge "
                "between parts), dispensables (code you could delete) and object-orientation abusers.", 880, 150)
    fam = [("Bloaters", "grew too big", "dev"), ("Change preventers", "one change, many edits", "bug"),
           ("Couplers", "know too much", "rel"), ("Dispensables", "could be deleted", "feat"), ("OO abusers", "misused types", "warn")]
    x = 14
    for i, (label, sub, tone) in enumerate(fam):
        d.node(f"f{i}", x, 36, 160, 54, label, sub, tone)
        x += 172
    d.text(14, 22, "A smell is a hint, not a rule: it says “look here”. Fix it only when it gets in the way of the change you're making.")
    d.text(14, 118, "Smells cluster: a Long Function often also has Mysterious Names, Duplicated Code and Feature Envy.")
    d.text(14, 138, "Start with the smell nearest the change you need to make, and stop when the change is easy.")
    return d.svg()


PAGE_SMELLS = dict(
    title="Code smells",
    kicker="24 hints that the code wants to change",
    figure=families(),
    boxes=[
        box("Bloaters", smells([
            ("Long Function", "you scroll to read it; comments label its sections"),
            ("Large Class", "too many fields and methods; several jobs in one"),
            ("Long Parameter List", "five arguments, some always passed together"),
            ("Data Clumps", "the same three fields travel together everywhere"),
            ("Primitive Obsession", "money as <code>number</code>, email as <code>string</code>"),
        ]), "dev"),
        box("Change preventers", smells([
            ("Divergent Change", "one module changed for many unrelated reasons"),
            ("Shotgun Surgery", "one change needs small edits in many modules"),
            ("Repeated Switches", "the same <code>switch</code> on a type in several places"),
            ("Global Data", "anyone can change it, nobody knows who did"),
            ("Mutable Data", "values change under you; bugs far from the cause"),
        ]), "bug"),
        box("Couplers", smells([
            ("Feature Envy", "a function uses another module's data more than its own"),
            ("Insider Trading", "two modules swap private details"),
            ("Message Chains", "<code>a.b().c().d()</code>: callers know the whole path"),
            ("Middle Man", "a class that only forwards calls"),
        ]), "rel"),
        box("Dispensables", smells([
            ("Duplicated Code", "the same logic in two places, slowly drifting"),
            ("Lazy Element", "a class or function that adds nothing"),
            ("Speculative Generality", "hooks and parameters “in case we need it”"),
            ("Dead code", "unreachable or unused; version control remembers it"),
            ("Comments", "explaining <i>what</i> unclear code does (fix the code)"),
            ("Mysterious Name", "you need the body to know what it does"),
        ]), "feat"),
        box("OO abusers", smells([
            ("Temporary Field", "a field set only in some situations"),
            ("Refused Bequest", "a subclass ignores what it inherits"),
            ("Data Class", "fields and getters, all logic elsewhere"),
            ("Alternative Classes", "two classes do one job with different method names"),
            ("Loops", "a loop where a pipeline (<code>filter</code>, <code>map</code>) reads better"),
        ]), "warn"),
        box("Sniff test: five questions", '''
<ul class="checks">
<li>Can I say what this function does <b>in one sentence</b>, without “and”?</li>
<li>Would a <b>new teammate</b> guess it from the name alone?</li>
<li>To make my change, how <b>many files</b> must I touch?</li>
<li>Is the same rule written <b>twice</b>?</li>
<li>Does this code use <b>someone else's data</b> more than its own?</li>
</ul>
<p class="fine">Tools help find candidates: ESLint complexity rules, SonarQube, CodeScene hotspots (complex code that changes often matters most).</p>''', "ink"),
    ],
)

# ---------------------------------------------------------------- page 2 · smell → refactoring
PAGE_MAP = dict(
    title="Smell → refactoring",
    kicker="what to try first for each smell",
    boxes=[
        box("The map", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>Smell</th><th>Try first</th><th>Then maybe</th></tr></thead>
<tbody>
<tr><td>Mysterious Name</td><td><b>Rename</b> (Change Function Declaration, Rename Variable)</td><td>Rename Field</td></tr>
<tr><td>Duplicated Code</td><td><b>Extract Function</b></td><td>Slide Statements, Pull Up Method</td></tr>
<tr><td>Long Function</td><td><b>Extract Function</b>, Decompose Conditional</td><td>Replace Temp with Query, Split Loop, Replace Function with Command</td></tr>
<tr><td>Long Parameter List</td><td><b>Introduce Parameter Object</b></td><td>Preserve Whole Object, Remove Flag Argument</td></tr>
<tr><td>Global / Mutable Data</td><td><b>Encapsulate Variable</b></td><td>Separate Query from Modifier, Change Reference to Value</td></tr>
<tr><td>Divergent Change</td><td><b>Split Phase</b></td><td>Move Function, Extract Class</td></tr>
<tr><td>Shotgun Surgery</td><td><b>Move Function</b>, Move Field</td><td>Combine Functions into Class, Inline Class</td></tr>
<tr><td>Feature Envy</td><td><b>Move Function</b></td><td>Extract Function first, then move the part that envies</td></tr>
<tr><td>Data Clumps</td><td><b>Introduce Parameter Object</b>, Extract Class</td><td>Preserve Whole Object</td></tr>
<tr><td>Primitive Obsession</td><td><b>Replace Primitive with Object</b></td><td>Replace Type Code with Subclasses</td></tr>
<tr><td>Repeated Switches</td><td><b>Replace Conditional with Polymorphism</b></td><td>a map of functions (strategy)</td></tr>
<tr><td>Loops</td><td><b>Replace Loop with Pipeline</b></td><td>Split Loop</td></tr>
<tr><td>Lazy Element</td><td><b>Inline Function</b>, Inline Class</td><td>Collapse Hierarchy</td></tr>
<tr><td>Speculative Generality</td><td><b>Remove Dead Code</b>, Inline</td><td>Change Function Declaration (drop unused params)</td></tr>
<tr><td>Temporary Field</td><td><b>Extract Class</b></td><td>Introduce Special Case</td></tr>
<tr><td>Message Chains</td><td><b>Hide Delegate</b></td><td>Extract Function + Move Function</td></tr>
<tr><td>Middle Man</td><td><b>Remove Middle Man</b></td><td>Inline Function</td></tr>
<tr><td>Insider Trading</td><td><b>Move Function</b>, Move Field</td><td>Hide Delegate, Replace Subclass with Delegate</td></tr>
<tr><td>Large Class</td><td><b>Extract Class</b></td><td>Extract Superclass, Replace Type Code with Subclasses</td></tr>
<tr><td>Data Class</td><td><b>Encapsulate Record</b>, Move Function</td><td>Remove Setting Method</td></tr>
<tr><td>Refused Bequest</td><td><b>Replace Subclass with Delegate</b></td><td>Push Down Method</td></tr>
<tr><td>Comments</td><td><b>Extract Function</b> (name it after the comment)</td><td>Introduce Assertion</td></tr>
</tbody></table></div>''', "dev", "full"),
        box("Big-step moves", '''
<ul class="checks">
<li><b>Split Phase</b>: parse → compute → render as separate steps, a data structure between</li>
<li><b>Replace Function with Command</b>: a long function becomes an object; temps become fields</li>
<li><b>Combine Functions into Transform</b>: enrich a record once, not derived values everywhere</li>
<li><b>Replace Superclass with Delegate</b>: stop inheriting what you don't want</li>
</ul>''', "feat"),
        box("Names of the moves", '''
<p>Every refactoring has an <b>inverse</b>: Extract ↔ Inline, Encapsulate ↔ expose, Move there ↔ move back. Pick by what makes the
<b>next change</b> easier, not by a rule.</p>
<p class="fine">Fowler's 2nd edition (2018) renamed several classics: Extract Method → <b>Extract Function</b>; Replace Method with Method Object →
<b>Replace Function with Command</b>; Rename Method → <b>Change Function Declaration</b>. Catalogue: refactoring.com/catalog.</p>''', "ink"),
        box("Code smells at a higher level", '''
<ul class="checks">
<li><b>God service</b>: split by actor or use case (vertical slices)</li>
<li><b>Anemic model, rich rules</b>: Move Function onto the entities</li>
<li><b>Leaky vendor types</b>: an adapter or anti-corruption layer at the border</li>
</ul>''', "rel"),
    ],
)

# ---------------------------------------------------------------- page 3 · the core refactorings
PAGE_CORE = dict(
    title="The core refactorings",
    kicker="before → after, the ones you'll use every week",
    boxes=[
        box("Extract Function", code('''
// before
function printOwing(invoice: Invoice) {
  let outstanding = 0;
  for (const o of invoice.orders) outstanding += o.amount;
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
// after
function printOwing(invoice: Invoice) {
  printDetails(invoice, totalOutstanding(invoice));
}
const totalOutstanding = (inv: Invoice) =>
  inv.orders.reduce((sum, o) => sum + o.amount, 0);
'''), "dev", "wide", "most used"),
        box("Inline Function", code('''
// before: the name adds nothing
const lateOften = (d: Driver) =>
  d.lateDeliveries > 5;
const rating = (d: Driver) =>
  lateOften(d) ? 2 : 1;
// after
const rating = (d: Driver) =>
  d.lateDeliveries > 5 ? 2 : 1;
'''), "feat"),
        box("Introduce Parameter Object", code('''
// before
function readingsOutside(s: Station, min: number, max: number) {}
// after
class NumberRange {
  constructor(readonly min: number, readonly max: number) {}
  contains(v: number) { return v >= this.min && v <= this.max; }
}
function readingsOutside(s: Station, range: NumberRange) {}
'''), "rel", "wide"),
        box("Encapsulate Variable", code('''
// before: anyone can write it
export let owner = { name: "Ana" };
// after: one door, easy to watch
let owner = { name: "Ana" };
export const getOwner = () =>
  ({ ...owner });
export const setOwner =
  (o: Owner) => { owner = o; };
'''), "bug"),
        box("Replace Primitive with Object", code('''
// before
if (order.priority === "high" || order.priority === "rush") {}
// after
const LEVELS = ["low", "normal", "high", "rush"];
class Priority {
  constructor(readonly value: string) {
    if (!LEVELS.includes(value)) throw new Error(value);
  }
  higherThan(o: Priority) {
    return LEVELS.indexOf(this.value) > LEVELS.indexOf(o.value);
  }
}
if (order.priority.higherThan(new Priority("normal"))) {}
'''), "warn", "wide"),
        box("Guard clauses", code('''
// before: nested
function pay(e: Employee) {
  let r;
  if (e.isSeparated) r = SEP;
  else {
    if (e.isRetired) r = RET;
    else r = normalPay(e);
  }
  return r;
}
// after: guard clauses
function pay(e: Employee) {
  if (e.isSeparated) return SEP;
  if (e.isRetired) return RET;
  return normalPay(e);
}
'''), "dev"),
        box("Replace Conditional with Polymorphism", code('''
// before: the same switch in several places
function speed(bird: Bird) {
  switch (bird.type) {
    case "european": return 35;
    case "african":  return 40 - 2 * bird.coconuts;
    case "norwegian": return bird.nailed ? 0 : 10 + bird.voltage / 10;
  }
}
// after: one map (or subclasses), one place per case
const speeds: Record<BirdType, (b: Bird) => number> = {
  european:  () => 35,
  african:   (b) => 40 - 2 * b.coconuts,
  norwegian: (b) => (b.nailed ? 0 : 10 + b.voltage / 10),
};
const speed = (b: Bird) => speeds[b.type](b);
'''), "feat", "wide"),
        box("Replace Loop with Pipeline", code('''
// before
const names: string[] = [];
for (const p of people)
  if (p.job === "dev")
    names.push(p.name);
// after
const names = people
  .filter((p) => p.job === "dev")
  .map((p) => p.name);
'''), "rel"),
    ],
)

# ---------------------------------------------------------------- page 4 · refactoring safely
def loop():
    d = Diagram("The refactoring loop. Start with all tests green. Make one small step. Run the tests. If they pass, commit "
                "and take the next step. If they fail, undo the step instead of debugging, and try a smaller step.", 880, 170)
    d.node("g", 14, 50, 150, 54, "Tests green", "start here", "feat")
    d.node("s", 214, 50, 150, 54, "One small step", "a rename, an extract", "dev")
    d.node("t", 414, 50, 150, 54, "Run the tests", "seconds, not minutes", "ink")
    d.node("c", 640, 14, 220, 50, "Green → commit", "then the next step", "main")
    d.node("u", 640, 92, 220, 50, "Red → undo", "smaller step, try again", "bug")
    d.arrow("g", "s", tone="feat")
    d.arrow("s", "t", tone="dev")
    d.arrow("t", "c", tone="main")
    d.arrow("t", "u", tone="bug")
    d.text(14, 156, "Never debug a refactoring: if a step breaks the tests, revert it and take a smaller one. Minutes between green bars, not hours.")
    return d.svg()


PAGE_SAFE = dict(
    title="Refactoring safely",
    kicker="small steps, two hats, and legacy code",
    figure=loop(),
    boxes=[
        box("Definition", '''
<p><b>Refactoring</b>: changing the structure of code <b>without changing its behaviour</b>, in small steps that each keep it working.</p>
<p>Not refactoring: rewriting, “refactoring sprints” that break the build for a week, or a behaviour change hidden in a cleanup.</p>
<p class="fine">Read: Fowler, <i>Refactoring</i>, 2nd ed. (2018) · Feathers, <i>Working Effectively with Legacy Code</i> (2004) ·
Beck, <i>Tidy First?</i> (2023) · Ellnestam &amp; Brolund, <i>The Mikado Method</i> (2014).</p>''', "ink"),
        box("The two hats", '''
<dl class="kv">
<dt>Adding a feature</dt><dd>new behaviour, new tests; no restructuring</dd>
<dt>Refactoring</dt><dd>same behaviour, tests unchanged; only restructuring</dd>
</dl>
<p class="fine">Wear one hat at a time. Swap often, but say which one you're wearing, in the commit message too.</p>''', "dev"),
        box("When to refactor", '''
<dl class="kv">
<dt>Preparatory</dt><dd>“make the change easy, then make the easy change” (Kent Beck)</dd>
<dt>Comprehension</dt><dd>rename and extract while you read, to record what you learned</dd>
<dt>Litter-pickup</dt><dd>leave it a little better than you found it</dd>
<dt>Rule of three</dt><dd>third time you write the same thing, extract it</dd>
<dt>Not when</dt><dd>the code works, nobody needs to change it, or a rewrite is cheaper</dd>
</dl>''', "feat"),
        box("Legacy code without tests", '''
<ul class="checks">
<li><b>Characterization tests</b> first: record what it does today, right or wrong</li>
<li>Find a <b>seam</b>: a place to substitute behaviour (a parameter, an interface)</li>
<li>Use <b>automated</b> refactorings only until tests exist (rename, extract, move)</li>
<li><b>Sprout</b> new code in a new, tested function; call it from the old</li>
<li>Big change? <b>Mikado method</b>: try, note blockers, revert, fix leaves first</li>
<li>Whole system? <b>Strangler fig</b>, not a big-bang rewrite</li>
</ul>''', "bug", "wide"),
        box("IDE moves", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>Move</th><th>VS Code</th><th>JetBrains</th></tr></thead>
<tbody>
<tr><td>Rename</td><td><code>F2</code></td><td><code>Shift+F6</code></td></tr>
<tr><td>Extract / quick fix menu</td><td><code>Ctrl+.</code> · <code>Ctrl+Shift+R</code></td><td><code>Ctrl+Alt+Shift+T</code></td></tr>
<tr><td>Extract function</td><td>select → <code>Ctrl+.</code></td><td><code>Ctrl+Alt+M</code></td></tr>
<tr><td>Extract variable</td><td>select → <code>Ctrl+.</code></td><td><code>Ctrl+Alt+V</code></td></tr>
<tr><td>Inline</td><td><code>Ctrl+.</code> → Inline</td><td><code>Ctrl+Alt+N</code></td></tr>
<tr><td>Change signature</td><td>(extension)</td><td><code>Ctrl+F6</code></td></tr>
</tbody></table></div>
<p class="fine">macOS: Ctrl → Cmd, Alt → Option. Automated refactorings are safer than hand edits.</p>''', "rel"),
        box("Pull requests", '''
<ul class="checks">
<li><b>Separate</b> refactor commits from behaviour commits</li>
<li>Big renames and moves in their <b>own PR</b>, merged fast</li>
<li>Tests unchanged in a refactor-only commit (a tell if not)</li>
<li>Prefix commits: <code>refactor:</code> vs <code>feat:</code></li>
</ul>''', "main"),
        box("At scale: codemods", code('''
# TypeScript / JavaScript
npx jscodeshift -t rename-prop.ts src/        # AST transform
npx ts-morph ...                               # scripted refactors with types
# Java / Kotlin
mvn rewrite:run                                # OpenRewrite recipes
# any language, structural search and replace
ast-grep run -p 'oldFn($A)' -r 'newFn($A)' -U src/
'''), "ink", "wide", "1,000 files"),
    ],
)

PAGES = [PAGE_SMELLS, PAGE_MAP, PAGE_CORE, PAGE_SAFE]
