# Vol. 2 · Components: Container & Presentational, Compound Components, Custom Hooks, Headless Components.
# Ratings order: Simplicity, Reusability, Testability, Maintainability, Performance, Bundle size,
#                Accessibility, Developer experience, Team scalability.

# ------------------------------------------------------------------ 01 Container & Presentational
cp_problem = Doodle(760, 280, "Doodle of one giant ProductPage component, 600 lines long, that fetches data, tracks loading and errors, filters and sorts, sends analytics and draws every card and button. The product card inside it can't be reused on the search page or tested without mocking the network.",
                    "One component doing everything: you can't reuse its looks or test them without the network.")
cp_problem.box(30, 30, 330, 230, None, "pink", stroke="red")
cp_problem.head(195, 60, "ProductPage.tsx · 600 lines", size=19)
for i, t in enumerate(["fetch('/api/products')", "loading / error flags", "filter + sort state", "analytics events", "<div className=card>…", "<button>Add to cart</button>"]):
    cp_problem.text(56, 96 + i * 26, t, anchor="start", size=16)
cp_problem.box(450, 40, 270, 60, "Search page", "paper", sub="wants the same card")
cp_problem.box(450, 150, 270, 60, "Storybook / tests", "paper", sub="need the network mocked")
cp_problem.arrow(366, 140, 444, 74, dash=True, color="red")
cp_problem.note(585, 126, "can't reuse ✗", "red")
cp_problem.arrow(366, 190, 444, 180, dash=True, color="red")
cp_problem.note(585, 236, "hard to test ✗", "red")

cp_analogy = Doodle(760, 250, "Doodle of a restaurant kitchen passing a finished dish to a plate. The kitchen buys ingredients, cooks and decides; the plate only presents what it's given. The same plate design can hold any dish.",
                    "The kitchen sources and cooks. The plate just presents whatever it's handed.")
cp_analogy.icon("kitchen", 40, 70, 2.0)
cp_analogy.note(110, 220, "kitchen: buys, cooks, decides")
cp_analogy.arrow(200, 120, 420, 120, label="hands over the dish", lx=310, ly=106)
cp_analogy.icon("plate", 440, 80, 2.4)
cp_analogy.note(520, 220, "plate: just presents it")
cp_analogy.note(640, 60, "same plate,", "pen")
cp_analogy.note(640, 84, "any dish", "pen")

cp_how = Doodle(760, 300, "A ProductListContainer fetches products, holds filter state and defines handlers, then passes plain props to a ProductList presentational component. The same ProductList is used by the search page container and in Storybook with fake data.",
                "Containers own data and decisions; presentational components get props and draw.")
cp_how.box(20, 30, 260, 110, "ProductListContainer", "y", sub="fetch · filters · onAddToCart")
cp_how.arrow(286, 85, 440, 140, label="props: items, onAdd", lx=330, ly=96, anchor="start")
cp_how.box(446, 110, 290, 90, "<ProductList />", "green", sub="pure UI: props in, markup out")
cp_how.box(20, 180, 260, 60, "SearchContainer", "y", size=19)
cp_how.arrow(286, 210, 440, 176)
cp_how.box(470, 240, 240, 50, "Storybook (fake data)", "blue", size=17)
cp_how.arrow(590, 236, 590, 204, dash=True)

CONTAINER = dict(
    slug="container-presentational",
    kicker="a.k.a. “smart and dumb components”",
    tldr="Split UI code into <b>containers</b> that fetch data, hold state and decide what happens, and <b>presentational components</b> that only receive props and render markup. The looks become <b>reusable and easy to test</b>; the logic lives in one obvious place.",
    chips=[("Family", "component design"), ("Popularised by", "Dan Abramov, 2015"), ("Modern form", "hooks + server components"), ("Pairs with", "custom hooks, design tokens")],
    problem="""  <p class="lead">Components tend to grow. A page component starts small, then gains fetching, loading flags, error handling, filters, analytics and all the markup. Soon it's <span class="hl-pink">600 lines that do everything</span>.</p>
  <ul>
    <li>The search page needs the same product card, but it's tangled up with the product page's fetching.</li>
    <li>Testing the card means mocking the network, the router and the analytics client.</li>
    <li>Designers can't preview states (empty, loading, error) in Storybook without a running backend.</li>
    <li>Every change risks breaking both the logic and the layout.</li>
  </ul>""",
    problem_figs=[cp_problem],
    analogy_side="the kitchen and the plate",
    analogy="""  <p>In a restaurant the <b>kitchen</b> buys ingredients, cooks, and decides what goes out. The <b>plate</b> just presents what it's handed. It doesn't know where the fish came from.</p>
  <ul>
    <li>The same plate design works for any dish: <b>reuse</b>.</li>
    <li>You can photograph a plate with plastic food for the menu: <b>Storybook with fake data</b>.</li>
    <li>Changing suppliers changes the kitchen, not the plates.</li>
  </ul>""",
    analogy_figs=[cp_analogy],
    map=[("The kitchen", "Container: fetches, holds state, handles events"),
         ("The plate", "Presentational component: props in, markup out"),
         ("Handing over the dish", "Passing data and callbacks as props"),
         ("Same plate for any dish", "Reusing the component on other screens"),
         ("Plastic food for the menu photo", "Storybook stories with fake props")],
    how_side="split the deciding from the drawing",
    how="""  <p>Ask of every component: <b>does it know where data comes from?</b> If yes, it's a container. If it only uses its props, it's presentational. Today the “container” is often a custom hook or a server component rather than a class.</p>""",
    how_figs=[cp_how],
    steps=[("Find the pure UI", "Pull out the markup that only needs data and callbacks: cards, lists, forms, empty and error states."),
           ("Give it a props interface", "<code>items</code>, <code>isLoading</code>, <code>onAddToCart</code>. No fetch, no global store, no router inside."),
           ("Keep logic in the container", "The container (or a custom hook it uses) fetches, transforms, and passes plain props down."),
           ("Story every state", "Write Storybook stories for loading, empty, error and long-content states using fake props."),
           ("Don't overdo it", "Small components that are used once don't need splitting. Split when reuse or testing hurts.")],
    vocab=[("Container", "Knows how things work: data, state, side effects."),
           ("Presentational", "Knows how things look: renders props."),
           ("Props interface", "The typed inputs a component accepts."),
           ("Pure component", "Same props in → same output, no side effects."),
           ("Storybook", "A workshop for rendering components in isolation."),
           ("Server component", "Runs on the server, can fetch data, sends rendered UI.")],
    code=dict(file="ProductList.tsx", note="React + TypeScript", src="""
// presentational: props in, markup out
type Props = { items: Product[]; isLoading: boolean; onAdd: (id: string) => void };

export function ProductList({ items, isLoading, onAdd }: Props) {
  if (isLoading) return <Skeleton rows={6} />;
  if (items.length === 0) return <EmptyState title="No products yet" />;
  return (
    <ul className="grid">
      {items.map((p) => (
        <li key={p.id}><ProductCard product={p} onAdd={() => onAdd(p.id)} /></li>
      ))}
    </ul>
  );
}

// container: data and decisions
export function ProductListContainer({ category }: { category: string }) {
  const { data = [], isLoading } = useProducts(category);   // custom hook
  const addToCart = useAddToCart();
  return <ProductList items={data} isLoading={isLoading} onAdd={addToCart} />;
}
"""),
    tools="where you see it today: hooks as the “container” part, React Server Components fetching on the server and passing props to client components, Storybook for the presentational side.",
    gains=["<b>Reusable UI</b> across pages and apps.",
           "<b>Easy tests and stories</b>: render with props, no network.",
           "<b>Clear ownership</b>: logic in one place, looks in another.",
           "<b>Designers and developers</b> can work on looks independently.",
           "<b>Simpler refactors</b>: swap the data source without touching markup."],
    losses=["<b>More files and props</b> to pass around.",
            "<b>Prop drilling</b> when containers sit far above the UI.",
            "<b>Over-splitting</b> tiny components adds noise.",
            "<b>Rules blur</b>: hooks let any component fetch, so teams must agree."],
    baseline="Each line compares <b>one big component that fetches and renders</b> to the same feature split into a <b>container + presentational components</b>.",
    ratings=[(3, 4, "Each part does one job and is easier to read."),
             (2, 5, "Presentational components drop into any screen."),
             (2, 5, "Render with props; no network mocks."),
             (2, 4, "Logic and looks change independently."),
             (3, 3, "Neutral; pure components are easy to memoise."),
             (3, 3, "Neutral."),
             (3, 4, "Shared UI pieces get accessibility fixed once."),
             (3, 4, "Storybook-driven work is fast and visual."),
             (2, 4, "UI and data work can be split between people.")],
    pitfalls=[("Splitting everything by rule", "Every component gets a “Container” twin, even a 10-line button.", "split when reuse or testing actually hurts."),
              ("Prop drilling five levels deep", "Data travels through components that don't use it.", "put containers close to where data is used, or use context / a custom hook."),
              ("Presentational components that fetch “just once”", "A card calls an API for its avatar, and now it can't be storied.", "pass the URL or data in as props."),
              ("Leaking server shapes into UI props", "The card takes the raw API response, so an API change breaks the UI.", "map to a small UI-friendly type in the container.")],
    use=["A piece of UI is (or will be) used on several screens.",
         "You want Storybook stories and fast component tests.",
         "A component mixes data fetching with a lot of markup.",
         "Several people work on the same feature's logic and looks."],
    skip=["Tiny components used once.",
          "The split would only move code around without making anything easier.",
          "The framework already separates them (server components fetching, client components drawing)."],
    related=["<b>Custom hooks</b>", "<b>Compound components</b>", "<b>Server-state cache</b>", "<b>Design tokens</b>"],
    quiz=[("How do you tell a presentational component from a container?", "A presentational component only uses its props to render; a container knows where data comes from (fetches, reads stores, handles side effects)."),
          ("Why are presentational components easy to test?", "You render them with props and assert on output; no network, store or router needs mocking."),
          ("Has the pattern died with hooks?", "The class-based form faded, but the idea lives on: hooks or server components hold the logic, pure components draw."),
          ("What's a sign you've over-applied it?", "Lots of one-line containers that only forward props to a single component.")],
    remember="Kitchens <span class=\"hl\">decide</span>, plates <span class=\"hl\">present</span>. Keep the drawing pure and the data somewhere obvious.",
    sources=["Dan Abramov, “Presentational and Container Components” (2015, with a 2019 update).",
             "patterns.dev, “Container/Presentational Pattern”.",
             "React docs, “Thinking in React” and “Server Components”.",
             "Storybook docs, “Why Storybook?”."],
)

# ------------------------------------------------------------------ 02 Compound Components
cc_problem = Doodle(760, 280, "Doodle of a Tabs component with a long list of props: items, titles, icons, disabled, badges, renderTab, renderPanel, tabClassName, panelClassName, orientation and more. Every new design request adds another prop.",
                    "One component, one giant props list. Every new request adds a prop, and nobody can read it.")
cc_problem.box(30, 30, 330, 230, None, "pink", stroke="red")
cc_problem.head(195, 62, "<Tabs", size=22)
for i, t in enumerate(["items titles icons badges", "disabledTabs tooltips", "renderTab renderPanel", "tabClassName panelClassName", "orientation lazyPanels …"]):
    cc_problem.text(60, 100 + i * 28, t, anchor="start", size=17)
cc_problem.head(195, 246, "/>  (23 props)", size=19, color="red")
cc_problem.note(560, 80, "“can we put a badge", "pen")
cc_problem.note(560, 106, "on tab 2?”", "pen")
cc_problem.note(560, 150, "→ prop #24", "red")
cc_problem.note(560, 200, "“icon right of the title?”", "pen")
cc_problem.note(560, 226, "→ prop #25", "red")

cc_analogy = Doodle(760, 250, "Doodle of a bento box. The box sets the compartments and holds the lid; you choose what goes in each compartment and in what order, and the pieces only make sense inside the box.",
                    "The box keeps things together and shares one lid; you arrange what goes inside.")
cc_analogy.icon("bento", 270, 50, 3.0)
cc_analogy.note(150, 70, "box = <Tabs>", "pen")
cc_analogy.note(150, 96, "shares the lid (state)", "pen")
cc_analogy.note(640, 70, "you choose the", "pen")
cc_analogy.note(640, 96, "pieces + order", "pen")
cc_analogy.note(380, 240, "a compartment on its own is just… a tray", "red")

cc_how = Doodle(760, 300, "A Tabs component provides shared state through context: the active index and a setter. Inside it, Tabs.List holds three Tabs.Tab children, followed by Tabs.Panel children. Each child reads the shared state from context, so the parent doesn't need a prop for every detail.",
                "The parent shares state through context; children are composed freely in markup.")
cc_how.box(20, 20, 720, 270, None, "y")
cc_how.head(120, 52, "<Tabs>", size=20)
cc_how.note(520, 50, "context: activeIndex, setActive", "pen")
cc_how.box(50, 76, 660, 76, None, "paper")
cc_how.head(120, 98, "<Tabs.List>", size=17)
for i, t in enumerate(["Overview", "Reviews · 12", "Specs"]):
    cc_how.box(80 + i * 205, 108, 185, 36, t, "green" if i == 0 else "blue", size=16, rx=6)
cc_how.box(50, 172, 660, 96, None, "paper")
cc_how.head(130, 196, "<Tabs.Panel>", size=17)
cc_how.text(380, 236, "only the active panel shows", size=17)

COMPOUND = dict(
    slug="compound-components",
    kicker="a.k.a. “like &lt;select&gt; and &lt;option&gt;”",
    tldr="Instead of one component with dozens of props, offer a <b>family of small components</b> that are used together (<code>&lt;Tabs&gt;</code>, <code>&lt;Tabs.List&gt;</code>, <code>&lt;Tabs.Tab&gt;</code>, <code>&lt;Tabs.Panel&gt;</code>). The parent <b>shares state through context</b>, and users compose the children however their design needs.",
    chips=[("Family", "component API design"), ("Seen in", "Radix, Reach UI, Headless UI"), ("Mechanism", "React context"), ("Pairs with", "headless components, design tokens")],
    problem="""  <p class="lead">A shared component starts simple: <code>&lt;Tabs items={...} /&gt;</code>. Then the requests arrive, and every one becomes <span class="hl-pink">another prop</span>.</p>
  <ul>
    <li>“A badge on one tab” → <code>badges</code>. “An icon on the right” → <code>iconPosition</code>. “Custom panel markup” → <code>renderPanel</code>.</li>
    <li>After a year: 25 props, some contradicting each other, and a component nobody dares to change.</li>
    <li>Users who need something unplanned fork the component or hack around it with CSS.</li>
  </ul>""",
    problem_figs=[cc_problem],
    analogy_side="the bento box",
    analogy="""  <p>A <b>bento box</b> gives you compartments and a lid that covers them all. You decide what goes in each compartment and in what order. The pieces belong together: a compartment on its own isn't much use.</p>
  <ul>
    <li>The box keeps everything in sync (one lid): <b>shared state</b>.</li>
    <li>You arrange the contents yourself: <b>composition</b> instead of configuration.</li>
    <li>HTML already works like this: <code>&lt;select&gt;</code> with <code>&lt;option&gt;</code>, <code>&lt;table&gt;</code> with <code>&lt;tr&gt;</code>.</li>
  </ul>""",
    analogy_figs=[cc_analogy],
    map=[("The bento box", "The parent component (<code>&lt;Tabs&gt;</code>)"),
         ("The shared lid", "Shared state in React context"),
         ("Compartments", "Child components (<code>Tabs.Tab</code>, <code>Tabs.Panel</code>)"),
         ("You choose what goes where", "Users compose children in JSX"),
         ("A compartment alone is useless", "Children throw if used outside the parent")],
    how_side="share state through context, compose in markup",
    how="""  <p>The parent owns the state and puts it in a context. Each child reads only what it needs. Users write normal JSX, so badges, icons and custom markup need <b>no new props</b>.</p>""",
    how_figs=[cc_how],
    steps=[("Create a context", "<code>TabsContext</code> holds <code>activeIndex</code> and <code>setActive</code>, plus ids for ARIA wiring."),
           ("Parent provides it", "<code>&lt;Tabs&gt;</code> owns the state (or accepts it as controlled props) and renders the provider."),
           ("Children consume it", "<code>Tabs.Tab</code> knows if it's active and how to activate; <code>Tabs.Panel</code> shows itself only when active."),
           ("Guard misuse", "Children throw a clear error if rendered outside <code>&lt;Tabs&gt;</code>."),
           ("Handle accessibility once", "Roles (<code>tablist</code>, <code>tab</code>, <code>tabpanel</code>), <code>aria-selected</code>, arrow-key navigation live in the family, not in every usage.")],
    vocab=[("Composition", "Building UI by nesting components instead of configuring one."),
           ("Context", "React's way to share values with deep children without props."),
           ("Controlled", "The parent's state is passed in from outside."),
           ("Uncontrolled", "The component keeps its own state."),
           ("Prop explosion", "A component with too many configuration props."),
           ("Slot", "A place in a component where users supply their own content.")],
    code=dict(file="Tabs.tsx", note="compound API with context", src="""
const TabsCtx = createContext<{ active: number; setActive: (i: number) => void } | null>(null);
const useTabs = () => {
  const ctx = useContext(TabsCtx);
  if (!ctx) throw new Error("Tabs.* must be used inside <Tabs>");
  return ctx;
};

export function Tabs({ children, defaultIndex = 0 }: { children: ReactNode; defaultIndex?: number }) {
  const [active, setActive] = useState(defaultIndex);
  return <TabsCtx.Provider value={{ active, setActive }}>{children}</TabsCtx.Provider>;
}
Tabs.Tab = function Tab({ index, children }: { index: number; children: ReactNode }) {
  const { active, setActive } = useTabs();
  return <button role="tab" aria-selected={active === index} onClick={() => setActive(index)}>{children}</button>;
};
Tabs.Panel = function Panel({ index, children }: { index: number; children: ReactNode }) {
  return useTabs().active === index ? <div role="tabpanel">{children}</div> : null;
};

// usage: badges and icons need no new props
<Tabs>
  <div role="tablist"><Tabs.Tab index={0}>Overview</Tabs.Tab><Tabs.Tab index={1}>Reviews <Badge>12</Badge></Tabs.Tab></div>
  <Tabs.Panel index={0}><Overview /></Tabs.Panel>
  <Tabs.Panel index={1}><Reviews /></Tabs.Panel>
</Tabs>
"""),
    tools="libraries built this way: Radix UI primitives, Reach UI, Headless UI, Ark UI, React Aria Components; native examples: select/option, details/summary, table/tr/td.",
    gains=["<b>Flexible layouts</b> without new props for every request.",
           "<b>Readable usage</b> that looks like the UI it creates.",
           "<b>Smaller, focused pieces</b> that are easier to maintain.",
           "<b>Accessibility handled once</b> inside the family.",
           "<b>Fewer forks</b> of shared components."],
    losses=["<b>More to learn</b>: users must know which pieces exist and how they nest.",
            "<b>Context re-renders</b> if the shared value changes often.",
            "<b>Easier to misuse</b> (wrong nesting, missing pieces) without guards.",
            "<b>Typing and docs</b> take more effort than a single props list."],
    baseline="Each line compares <b>one component configured by many props</b> to the same component offered as a <b>compound family</b>.",
    ratings=[(3, 3, "Usage reads well, but there are more pieces to know."),
             (2, 5, "Fits designs nobody planned for."),
             (3, 4, "Small pieces with clear jobs are easier to test."),
             (2, 4, "New needs rarely touch the core."),
             (3, 3, "Neutral; watch context re-renders."),
             (3, 3, "Neutral."),
             (3, 4, "ARIA wiring lives in one family, not every usage."),
             (3, 4, "Usage is close to plain JSX."),
             (3, 4, "Design-system teams stop being a bottleneck for small tweaks.")],
    pitfalls=[("No guard outside the parent", "Someone renders <code>Tabs.Panel</code> alone and gets a cryptic “cannot read property of null”.", "throw a clear error from the context hook."),
              ("Index-based wiring everywhere", "Users must keep tab and panel indexes in sync by hand.", "register children automatically, or use string values (<code>value=\"reviews\"</code>)."),
              ("One huge context value", "Every child re-renders when anything changes.", "split contexts or memoise the value."),
              ("Forgetting ARIA and keyboard", "Tabs look right but arrow keys and screen readers don't work.", "follow the WAI-ARIA Authoring Practices pattern or use a headless library.")],
    use=["Shared design-system components with many layout variations.",
         "Components with natural parts: tabs, menus, accordions, selects, dialogs.",
         "You keep adding props for one-off layouts.",
         "Accessibility wiring between parts is non-trivial."],
    skip=["Simple components with a handful of stable props (a Button).",
          "One-off components used in a single place.",
          "Users need a quick “just give me tabs from this array” API (offer both)."],
    related=["<b>Headless components</b>", "<b>Custom hooks</b>", "<b>Design tokens</b>", "<b>Container &amp; presentational</b>"],
    quiz=[("Which HTML elements already follow this pattern?", "select/option, table/tr/td, details/summary, ul/li, dl/dt/dd."),
          ("How do children get the shared state?", "Through a React context provided by the parent component."),
          ("What's the main problem it solves?", "Prop explosion: endless configuration props for every layout variation."),
          ("Why throw an error when a child is used outside the parent?", "So misuse fails loudly with a clear message instead of a confusing null error.")],
    remember="Don't add a <span class=\"hl\">prop</span> for every wish. Give people the <span class=\"hl\">pieces</span> and let them arrange the box.",
    sources=["Kent C. Dodds, “Compound Components with React Hooks”.",
             "patterns.dev, “Compound Pattern”.",
             "Radix UI docs, “Composition”.",
             "W3C WAI-ARIA Authoring Practices, “Tabs Pattern”."],
)

# ------------------------------------------------------------------ 03 Custom Hooks
ch_problem = Doodle(760, 270, "Doodle of three components, SearchBox, CommandPalette and UserPicker, each with its own copy of debounced search logic: state, a timer, a fetch and cleanup. One copy forgot to clear the timer and another forgot to cancel stale requests, so they behave differently.",
                    "The same logic copy-pasted three times, and each copy has drifted with its own bugs.")
for i, (name, bug) in enumerate([("SearchBox", "✓ ok"), ("CommandPalette", "forgot clearTimeout ✗"), ("UserPicker", "stale results ✗")]):
    x = 20 + i * 248
    bad = i > 0
    ch_problem.box(x, 30, 228, 180, None, "pink" if bad else "paper", stroke="red" if bad else "")
    ch_problem.head(x + 114, 60, name, size=18)
    for k, t in enumerate(["useState(query)", "useEffect(timer…)", "fetch(results)", "cleanup?"]):
        ch_problem.text(x + 114, 94 + k * 26, t, size=16)
    ch_problem.note(x + 114, 240, bug, "red" if bad else "green")

ch_analogy = Doodle(760, 250, "Doodle of one recipe card for a tomato sauce, used by two different dishes: pasta and pizza. Each cook makes their own pot from the same recipe; the dishes look different.",
                    "One recipe card, many dishes. Each cook makes their own pot from it.")
ch_analogy.icon("recipe", 320, 30, 2.0)
ch_analogy.note(370, 182, "tomato sauce recipe", "pen")
ch_analogy.arrow(310, 100, 180, 130)
ch_analogy.arrow(430, 100, 560, 130)
ch_analogy.icon("plate", 60, 140, 1.6)
ch_analogy.note(115, 236, "pasta (own pot)")
ch_analogy.icon("plate", 570, 140, 1.6)
ch_analogy.note(625, 236, "pizza (own pot)")

ch_how = Doodle(760, 280, "A custom hook useDebouncedSearch contains the state, timer, fetch, cancellation and cleanup once. SearchBox, CommandPalette and UserPicker each call it and get their own independent query, results and loading values.",
                "Write the logic once in a hook; every component that calls it gets its own copy of the state.")
ch_how.box(240, 20, 280, 110, "useDebouncedSearch()", "y", sub="state · timer · abort · cleanup")
for i, name in enumerate(["SearchBox", "CommandPalette", "UserPicker"]):
    x = 20 + i * 250
    ch_how.box(x, 190, 220, 60, name, "green", size=18)
    ch_how.arrow(x + 110, 186, 380, 134)
ch_how.note(380, 274, "each call = its own state", "pen")
ch_how.note(650, 60, "tested once", "green")

HOOKS = dict(
    slug="custom-hooks",
    kicker="a.k.a. “share the logic, not the looks”",
    tldr="When several components need the same <b>stateful logic</b> (debounced search, media queries, form handling, online status), move it into a function whose name starts with <code>use</code>. Each component that calls the hook gets <b>its own state</b>, and the logic is written, fixed and tested <b>once</b>.",
    chips=[("Family", "logic reuse"), ("Replaced", "mixins, HOCs, render props"), ("Framework", "React (Vue: composables)"), ("Pairs with", "container/presentational, headless components")],
    problem="""  <p class="lead">Components often need the same behaviour, not the same markup. Without a way to share it, logic gets <span class="hl-pink">copy-pasted</span>, and the copies drift apart.</p>
  <ul>
    <li>Three search inputs each implement debounce, fetch and cleanup slightly differently.</li>
    <li>A bug fixed in one copy (cancelling stale requests) stays in the other two.</li>
    <li>Older sharing tools had costs: mixins clashed, higher-order components and render props created deep “wrapper hell”.</li>
  </ul>""",
    problem_figs=[ch_problem],
    analogy_side="one recipe card, many dishes",
    analogy="""  <p>A good tomato-sauce <b>recipe card</b> can be used for pasta and for pizza. Each cook follows the same steps but makes <b>their own pot</b>; nobody shares a pot by accident. Improve the recipe once and every dish gets better.</p>""",
    analogy_figs=[ch_analogy],
    map=[("The recipe card", "The custom hook (<code>useDebouncedSearch</code>)"),
         ("Each cook's own pot", "Each component's own state from the hook"),
         ("Pasta and pizza look different", "Components keep their own markup"),
         ("Improving the recipe once", "Fixing a bug in one place"),
         ("Recipe names start with “Sauce:”", "Hook names start with <code>use</code>")],
    how_side="extract, name, reuse",
    how="""  <p>A custom hook is just a function that calls other hooks. It returns values and callbacks, never markup. Calls are independent: two components using it don't share state unless the hook reads a shared store.</p>""",
    how_figs=[ch_how],
    steps=[("Spot repeated stateful logic", "The same <code>useState</code> + <code>useEffect</code> combination in more than one component."),
           ("Extract to a use-function", "Move state, effects and handlers into <code>useSomething()</code>; return what callers need."),
           ("Design a small API", "Return an object (<code>{ query, setQuery, results, isLoading }</code>) or a tuple for two values."),
           ("Clean up properly", "Clear timers, abort requests and remove listeners in effect cleanups, once, inside the hook."),
           ("Test the hook alone", "Use <code>renderHook</code> to test behaviour without any markup.")],
    vocab=[("Hook", "A function that lets components use React state and lifecycle."),
           ("Custom hook", "Your own function built from other hooks."),
           ("Rules of hooks", "Call hooks at the top level, only from components or hooks."),
           ("Effect cleanup", "Code that undoes an effect (timers, listeners, requests)."),
           ("Composable (Vue)", "Vue's equivalent of a custom hook."),
           ("renderHook", "Testing helper that runs a hook without UI.")],
    code=dict(file="useDebouncedSearch.ts", note="one hook, many search boxes", src="""
export function useDebouncedSearch<T>(search: (q: string, s: AbortSignal) => Promise<T[]>, delayMs = 250) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<T[]>([]);
  const [isLoading, setLoading] = useState(false);

  useEffect(() => {
    if (!query) { setResults([]); return; }
    const ctrl = new AbortController();
    const timer = setTimeout(async () => {
      setLoading(true);
      try { setResults(await search(query, ctrl.signal)); }
      catch (e) { if ((e as Error).name !== "AbortError") throw e; }
      finally { setLoading(false); }
    }, delayMs);
    return () => { clearTimeout(timer); ctrl.abort(); };   // cleanup, written once
  }, [query, search, delayMs]);

  return { query, setQuery, results, isLoading };
}

// any component: its own state, shared behaviour
const { query, setQuery, results } = useDebouncedSearch(searchUsers);
"""),
    tools="ready-made collections: usehooks-ts, react-use, TanStack Query (useQuery), React Hook Form (useForm); Vue: VueUse composables.",
    gains=["<b>Logic written and fixed once.</b>",
           "<b>Components stay small</b> and focused on markup.",
           "<b>Testable without UI</b> via renderHook.",
           "<b>No wrapper hell</b> compared with HOCs and render props.",
           "<b>Composable</b>: hooks can use other hooks."],
    losses=["<b>Hidden complexity</b> behind a friendly name.",
            "<b>Rules of hooks</b> to learn (no conditional calls).",
            "<b>Dependency arrays</b> are easy to get wrong.",
            "<b>Over-abstraction</b>: hooks for logic used only once."],
    baseline="Each line compares <b>logic copy-pasted into each component</b> to the same logic in a <b>shared custom hook</b>.",
    ratings=[(3, 4, "Components read as markup; logic has a name."),
             (1, 5, "One hook serves any component that needs it."),
             (2, 4, "Test the hook alone with renderHook."),
             (2, 5, "Fix once, fixed everywhere."),
             (3, 3, "Neutral; watch effects running too often."),
             (3, 4, "Less duplicated code in the bundle."),
             (3, 3, "Neutral (a hook can also share focus/keyboard logic)."),
             (3, 4, "Less boilerplate per component."),
             (3, 4, "Teams share a library of well-tested hooks.")],
    pitfalls=[("Assuming hooks share state", "Two components call <code>useCart()</code> and expect the same cart, but each gets its own.", "put shared state in context or a store and read it from the hook."),
              ("Missing cleanup", "Timers fire after unmount and set state on a gone component; old requests overwrite new results.", "clear timers and abort requests in the effect's cleanup."),
              ("Wrong dependency arrays", "The effect uses a stale value or loops forever.", "follow the exhaustive-deps lint rule; memoise callbacks."),
              ("A hook for everything", "<code>useButtonColor()</code> wraps one line of logic.", "extract when logic is reused or complex enough to test.")],
    use=["The same stateful logic appears in two or more components.",
         "Logic is complex enough to deserve its own tests.",
         "You're replacing HOCs or render props.",
         "Wrapping a browser API (resize, media queries, online status, storage)."],
    skip=["Pure calculations: a plain function is simpler.",
          "Logic used once and easy to read in place.",
          "State that must be shared between components (use context or a store)."],
    related=["<b>Container &amp; presentational</b>", "<b>Headless components</b>", "<b>Server-state cache</b>", "<b>Global store</b>"],
    quiz=[("Two components call the same custom hook. Do they share state?", "No. Each call has its own state, unless the hook reads from a shared store or context."),
          ("Why must hooks be called at the top level?", "React tracks hooks by call order; calling them conditionally would change the order between renders."),
          ("What did custom hooks replace?", "Mixins, higher-order components and render props for sharing stateful logic."),
          ("How do you test a hook without a component?", "With a helper like renderHook from Testing Library.")],
    remember="Share the <span class=\"hl\">recipe</span>, not the pot. A hook is logic with a name, and every caller cooks their own state.",
    sources=["React docs, “Reusing Logic with Custom Hooks”.",
             "Dan Abramov, “Making Sense of React Hooks”.",
             "patterns.dev, “Hooks Pattern”.",
             "Vue docs, “Composables”."],
)

# ------------------------------------------------------------------ 04 Headless Components
hl_problem = Doodle(760, 270, "Doodle of two bad options. Option one: a styled UI library dropdown that doesn't match the brand, patched with important CSS overrides. Option two: a hand-built dropdown that matches the brand but has no keyboard support, no ARIA roles and breaks with screen readers.",
                    "Use a styled library and fight its looks, or build your own and miss the hard parts.")
hl_problem.box(20, 30, 330, 190, None, "paper")
hl_problem.head(185, 60, "styled library", size=19)
hl_problem.text(185, 100, "looks like someone else's brand", size=16)
hl_problem.text(185, 130, "!important × 40", size=16)
hl_problem.text(185, 160, "breaks on every upgrade", size=16)
hl_problem.note(185, 250, "fighting the looks ✗", "red")
hl_problem.box(410, 30, 330, 190, None, "pink", stroke="red")
hl_problem.head(575, 60, "hand-built dropdown", size=19)
hl_problem.text(575, 100, "on brand ✓", size=16)
hl_problem.text(575, 130, "no arrow keys, no Esc", size=16)
hl_problem.text(575, 160, "no ARIA, focus lost", size=16)
hl_problem.note(575, 250, "screen readers lost ✗", "red")

hl_analogy = Doodle(760, 300, "Doodle of a car chassis with wheels, engine mount and steering column but no body. The factory provides the tested mechanics and safety; you design and paint the body yourself.",
                    "You get the tested engine, steering and brakes. You design the body.")
hl_analogy.icon("chassis", 220, 50, 3.6)
hl_analogy.note(380, 40, "engine · steering · brakes: done and safety-tested", "pen")
hl_analogy.note(380, 290, "the body (looks) is up to you", "green")

hl_how = Doodle(760, 300, "A headless useCombobox hook returns state such as isOpen and highlightedIndex, plus prop getters: getInputProps, getMenuProps and getItemProps. These props include ARIA attributes and keyboard handlers. You spread them onto your own markup and style it with your design tokens.",
                "The hook gives behaviour + ARIA through prop getters; you spread them onto your own markup.")
hl_how.box(20, 30, 300, 230, None, "y")
hl_how.head(170, 66, "useCombobox()", size=20)
for i, t in enumerate(["isOpen, highlightedIndex", "getInputProps()", "getMenuProps()", "getItemProps(item)", "→ aria-*, role, onKeyDown"]):
    hl_how.text(40, 110 + i * 28, t, anchor="start", size=16)
hl_how.arrow(326, 145, 440, 145, label="spread props", lx=383, ly=133)
hl_how.box(446, 30, 290, 230, None, "green")
hl_how.head(591, 62, "your markup + styles", size=18)
hl_how.box(470, 82, 240, 36, "input · brand style", "paper", size=15, rx=6)
for i, t in enumerate(["Apple", "Apricot", "Avocado"]):
    hl_how.box(470, 130 + i * 38, 240, 32, t, "y" if i == 1 else "paper", size=15, rx=4)

HEADLESS = dict(
    slug="headless-components",
    kicker="a.k.a. “behaviour without the looks”",
    tldr="A <b>headless</b> component (or hook) provides <b>state, keyboard handling and ARIA</b> for a tricky widget (combobox, menu, dialog, table) but <b>no markup or styles</b>. You render your own elements, spread the props it gives you, and style them with your design system.",
    chips=[("Family", "component design / design systems"), ("Examples", "Radix, React Aria, Headless UI, TanStack Table"), ("Mechanism", "hooks + prop getters"), ("Pairs with", "compound components, design tokens")],
    problem="""  <p class="lead">Widgets like comboboxes, menus, date pickers and dialogs are <span class="hl-pink">hard to build accessibly</span>: focus management, keyboard shortcuts, ARIA roles, typeahead, screen-reader announcements.</p>
  <ul>
    <li><b>Styled libraries</b> solve the hard parts but bring their own look, so you fight them with overrides.</li>
    <li><b>Hand-built widgets</b> match the brand but usually miss keyboard support and ARIA, failing users and audits.</li>
    <li>Each team re-solves the same accessibility bugs in its own dropdown.</li>
  </ul>""",
    problem_figs=[hl_problem],
    analogy_side="the car chassis",
    analogy="""  <p>Car makers often share one <b>chassis</b> across several models: the engine, steering, brakes and crash structure are engineered and safety-tested once. Each model gets its <b>own body</b> and paint on top.</p>
  <ul>
    <li>You don't re-engineer brakes for every new car: the risky, hard part is done properly once.</li>
    <li>The bodies can look completely different: a family car and a sports car on one platform.</li>
  </ul>""",
    analogy_figs=[hl_analogy],
    map=[("The shared chassis", "The headless hook/component"),
         ("Engine, steering, brakes", "State, keyboard handling, focus management"),
         ("Crash-test safety", "ARIA roles and screen-reader support"),
         ("The car body and paint", "Your markup and styles"),
         ("Many models, one platform", "Many brands or products, one behaviour layer")],
    how_side="behaviour in, markup out (yours)",
    how="""  <p>Headless libraries usually expose <b>prop getters</b>: functions that return the props an element needs (roles, ids, aria attributes, event handlers). You call them on your own elements, merging in your own props.</p>""",
    how_figs=[hl_how],
    steps=[("Pick the hard widget", "Combobox, menu, listbox, dialog, tabs, date picker, data table."),
           ("Use a headless primitive", "A hook (<code>useCombobox</code>) or unstyled components (Radix, React Aria Components)."),
           ("Render your own elements", "Use your design-system components and tokens for every visual detail."),
           ("Spread the prop getters", "<code>&lt;input {...getInputProps()} /&gt;</code> wires ARIA, ids and keyboard handlers."),
           ("Test like a user", "Keyboard-only walkthrough and a screen-reader check; let the library own the hard cases.")],
    vocab=[("Headless", "Logic and accessibility without markup or styles."),
           ("Prop getter", "A function returning the props an element needs."),
           ("ARIA", "Attributes that describe widgets to assistive tech."),
           ("Focus management", "Moving keyboard focus correctly as the UI changes."),
           ("Roving tabindex", "Only one item in a group is tabbable at a time."),
           ("WAI-ARIA APG", "The W3C guide for accessible widget patterns.")],
    code=dict(file="FruitPicker.tsx", note="Downshift-style combobox", src="""
export function FruitPicker({ items }: { items: string[] }) {
  const [input, setInput] = useState("");
  const shown = items.filter((i) => i.toLowerCase().includes(input.toLowerCase()));
  const { isOpen, highlightedIndex, getLabelProps, getInputProps, getMenuProps, getItemProps } =
    useCombobox({ items: shown, onInputValueChange: ({ inputValue }) => setInput(inputValue ?? "") });

  return (
    <div className="field">
      <label {...getLabelProps()}>Fruit</label>
      <input {...getInputProps()} className="input" />           {/* ARIA + keys wired */}
      <ul {...getMenuProps()} className="menu" hidden={!isOpen}>
        {shown.map((item, index) => (
          <li key={item} {...getItemProps({ item, index })}
              className={index === highlightedIndex ? "option is-active" : "option"}>
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
}
"""),
    tools="headless libraries: Radix UI primitives, React Aria (Adobe), Headless UI (Tailwind Labs), Ark UI / Zag (state machines), Downshift, TanStack Table and TanStack Form, Floating UI for positioning.",
    gains=["<b>Accessibility done right</b> by specialists, once.",
           "<b>Total control of looks</b>; fits any design system.",
           "<b>Smaller CSS</b>: no library styles to override.",
           "<b>Reusable across brands</b> and products.",
           "<b>Upgrades don't break your styles.</b>"],
    losses=["<b>You write all the markup and styles</b>, so more upfront work.",
            "<b>Easy to undo the a11y</b> by not spreading props or changing elements.",
            "<b>More concepts</b>: prop getters, controlled state, render order.",
            "<b>A dependency</b> for core interactions."],
    baseline="Each line compares a <b>hand-built styled widget</b> to the same widget built on a <b>headless primitive</b> with your own styles.",
    ratings=[(3, 3, "Less tricky code to write, but prop getters take learning."),
             (2, 5, "Same behaviour behind any brand or theme."),
             (2, 4, "Behaviour is tested by the library; you test looks."),
             (2, 4, "Library upgrades fix bugs without touching styles."),
             (3, 3, "Neutral; logic libraries are usually small."),
             (3, 3, "Adds a small dependency, saves custom code."),
             (2, 5, "Keyboard, focus and ARIA done properly."),
             (3, 4, "Hard edge cases are someone else's problem."),
             (3, 4, "Every team builds on the same accessible base.")],
    pitfalls=[("Not spreading every getter", "The input gets its props but the list items don't, so screen readers can't read the options.", "spread every prop getter on the element it's meant for."),
              ("Swapping elements", "Replacing a button with a div breaks keyboard support the library assumed.", "keep the element types the docs expect, or pass <code>as</code> props correctly."),
              ("Overriding handlers", "Your onKeyDown replaces the library's, so arrow keys stop working.", "pass your handlers through the getter so they're merged."),
              ("Skipping the visual focus state", "Keyboard users can't see which option is active.", "style the highlighted/focused state clearly.")],
    use=["Building a design system or a branded component library.",
         "Complex widgets: combobox, menu, dialog, tabs, date picker, data grid.",
         "Several products or brands share behaviour but not looks.",
         "Accessibility is a requirement (it should be)."],
    skip=["A styled library already matches your design closely.",
          "Simple elements where native HTML is enough (button, details, select).",
          "Prototypes where speed matters more than polish (temporarily)."],
    related=["<b>Compound components</b>", "<b>Custom hooks</b>", "<b>Design tokens</b>", "<b>State machines</b> (Zag, XState under the hood)"],
    quiz=[("What does a headless component give you, and what doesn't it?", "It gives state, behaviour, keyboard handling and ARIA; it doesn't give markup or styles."),
          ("What is a prop getter?", "A function (like getInputProps) that returns the props an element needs, which you spread onto your own element."),
          ("Why not just build the dropdown yourself?", "Accessible widgets have many edge cases (focus, keys, ARIA, screen readers) that are easy to get wrong and costly to maintain."),
          ("When is native HTML better than a headless library?", "For simple controls like button, select, details/summary or dialog where the native element already behaves accessibly.")],
    remember="Borrow the <span class=\"hl\">engine</span>, build the <span class=\"hl\">body</span>. The hard, invisible parts should be done once, properly.",
    sources=["Adobe, React Aria docs, “Why React Aria?”.",
             "Radix UI docs, “Introduction” and “Accessibility”.",
             "Kent C. Dodds, Downshift and “prop getters”.",
             "W3C WAI-ARIA Authoring Practices Guide."],
)

NOTES = [CONTAINER, COMPOUND, HOOKS, HEADLESS]
