# Vol. 2 · State & data: Global Store (Flux), Server-State Cache, Optimistic UI, State Machines.

# ------------------------------------------------------------------ 05 Global Store (Flux)
gs_problem = Doodle(760, 280, "Doodle of a component tree where the cart count is needed by the Header and the Checkout button, which are far apart. The cart state lives in App and is passed down through Layout, Page, Sidebar and other components that don't use it, while sibling components keep their own out-of-sync copies.",
                    "Shared state passed down through five layers that don't use it, and copies that drift apart.")
gs_problem.box(300, 10, 160, 44, "App · cart", "y", size=17)
for i, (name, x, y) in enumerate([("Layout", 300, 80), ("Page", 140, 150), ("Sidebar", 460, 150), ("Header", 40, 220), ("ProductGrid", 230, 220), ("Checkout", 480, 220)]):
    hot = name in ("Header", "Checkout")
    gs_problem.box(x, y, 160 if name != "ProductGrid" else 180, 44, name, "green" if hot else "paper", size=16)
gs_problem.arrow(380, 56, 380, 78, color="red")
gs_problem.arrow(340, 126, 240, 148, color="red")
gs_problem.arrow(420, 126, 520, 148, color="red")
gs_problem.arrow(200, 196, 130, 218, color="red")
gs_problem.arrow(540, 196, 560, 218, color="red")
gs_problem.note(650, 40, "props passed", "red")
gs_problem.note(650, 64, "through 4 layers", "red")
gs_problem.note(670, 120, "that don't use them", "red")

gs_analogy = Doodle(760, 260, "Doodle of a family calendar on the fridge. Everyone reads it. To change it you write a request on a sticky note, like add dentist Tuesday, and one person updates the calendar, so changes are tracked and nobody scribbles over each other.",
                    "One calendar everyone reads. Changes go through written requests, applied one at a time.")
gs_analogy.icon("fridge", 330, 40, 2.6)
gs_analogy.icon("calendar", 345, 70, 1.4, fill="y")
gs_analogy.note(395, 248, "the one calendar (store)")
for i, t in enumerate(["“add dentist, Tue”", "“move football to Sat”"]):
    gs_analogy.box(40, 50 + i * 80, 220, 50, t, "y", size=16, rx=3)
    gs_analogy.arrow(266, 75 + i * 80, 334, 120)
gs_analogy.note(150, 230, "requests = actions", "pen")
gs_analogy.note(620, 90, "everyone reads it", "pen")
gs_analogy.arrow(560, 100, 470, 120, dash=True)

gs_how = Doodle(760, 280, "Flux one-way data flow. A component dispatches an action like addItem. The store runs a reducer, a pure function from old state and action to new state. Subscribed components that select the changed slice re-render. The cycle always goes one way.",
                "Data flows one way: action → reducer → new state → subscribed components re-render.")
gs_how.box(20, 110, 170, 70, "component", "blue")
gs_how.arrow(196, 130, 300, 70, label="dispatch(addItem)", lx=24, ly=96, anchor="start")
gs_how.box(306, 30, 180, 70, "action", "y", sub="{ type, payload }")
gs_how.arrow(492, 65, 560, 110)
gs_how.box(560, 110, 180, 80, "reducer", "green", sub="(state, action) → state")
gs_how.arrow(640, 194, 520, 240)
gs_how.box(300, 210, 220, 60, "store (one state)", "y", size=18)
gs_how.arrow(296, 240, 110, 186, label="select → re-render", lx=24, ly=268, anchor="start")

STORE = dict(
    slug="global-store",
    kicker="a.k.a. “one calendar on the fridge”",
    tldr="Keep <b>truly shared client state</b> (cart, signed-in user, UI preferences) in <b>one store</b> outside the component tree. Components <b>select</b> the slice they need, and change it only by <b>dispatching named actions</b> handled by pure functions, so every change is predictable and traceable.",
    chips=[("Family", "state management"), ("Origin", "Flux (Facebook, 2014), Redux (2015)"), ("Modern options", "Redux Toolkit, Zustand, Pinia, signals"), ("Pairs with", "server-state cache, state machines")],
    problem="""  <p class="lead">Some state is needed in many places far apart in the tree: the cart count in the header and at checkout, the signed-in user everywhere. Passing it down by hand becomes <span class="hl-pink">prop drilling</span>, and keeping copies leads to <span class="hl-pink">out-of-sync UIs</span>.</p>
  <ul>
    <li>Props travel through layers that don't use them, so every refactor touches five files.</li>
    <li>Two components keep their own copy of “cart”, and the header says 3 while checkout says 2.</li>
    <li>Anything can change state from anywhere, so bugs are hard to trace: <i>who set this to null?</i></li>
  </ul>""",
    problem_figs=[gs_problem],
    analogy_side="the family calendar on the fridge",
    analogy="""  <p>A family keeps <b>one calendar</b> on the fridge. Everyone reads it. To change something you don't scribble over it: you leave a note (“add dentist on Tuesday”) and the changes are written in, one at a time.</p>
  <ul>
    <li>There's one truth, so nobody turns up on the wrong day: <b>single source of truth</b>.</li>
    <li>The notes are a history of what changed and why: <b>actions + devtools time travel</b>.</li>
    <li>But not everything belongs on the fridge. Your own homework stays in your room: <b>local state stays local</b>.</li>
  </ul>""",
    analogy_figs=[gs_analogy],
    map=[("The fridge calendar", "The global store"),
         ("A note: “add dentist Tuesday”", "An action: <code>{ type: \"cart/addItem\" }</code>"),
         ("Writing changes in, one at a time", "Reducers: pure (state, action) → new state"),
         ("Everyone reading the calendar", "Components selecting state"),
         ("Homework stays in your room", "Local UI state stays in components")],
    how_side="one-way data flow",
    how="""  <p>The Flux idea is a <b>one-way loop</b>: views dispatch actions, the store computes new state, views re-render. Modern libraries cut the boilerplate, but the loop is the same.</p>""",
    how_figs=[gs_how],
    steps=[("Decide what's global", "Only state needed by distant components: cart, session, feature flags, theme. Forms, toggles and server data usually aren't."),
           ("Model state and actions", "A slice like <code>cart</code> with actions <code>addItem</code>, <code>removeItem</code>, <code>clear</code>."),
           ("Write pure reducers", "Given the old state and an action, return the new state. No API calls, no randomness."),
           ("Select narrowly", "Components subscribe to the smallest slice they need (<code>s =&gt; s.cart.count</code>) so they re-render only when it changes."),
           ("Keep side effects at the edges", "API calls live in thunks, listeners or (better) a server-state cache, not in reducers.")],
    vocab=[("Store", "Object holding the shared state, outside components."),
           ("Action", "A plain object describing what happened."),
           ("Reducer", "Pure function: (state, action) → new state."),
           ("Selector", "Function that picks a slice of state for a component."),
           ("Prop drilling", "Passing props through components that don't use them."),
           ("Time-travel debugging", "Replaying actions to step through state changes.")],
    code=dict(file="cartSlice.ts", note="Redux Toolkit", src="""
const cartSlice = createSlice({
  name: "cart",
  initialState: { items: [] as { id: string; qty: number }[] },
  reducers: {
    addItem(state, action: PayloadAction<string>) {
      const line = state.items.find((i) => i.id === action.payload);
      if (line) line.qty += 1;                 // Immer makes this immutable
      else state.items.push({ id: action.payload, qty: 1 });
    },
    clear(state) { state.items = []; },
  },
});
export const { addItem, clear } = cartSlice.actions;
export const selectCount = (s: RootState) => s.cart.items.reduce((n, i) => n + i.qty, 0);

// anywhere in the tree, no prop drilling
function CartBadge() {
  const count = useSelector(selectCount);       // re-renders only when count changes
  return <span aria-label={`${count} items in cart`}>{count}</span>;
}
"""),
    tools="options: Redux Toolkit (+ DevTools), Zustand, Jotai, MobX, NgRx (Angular), Pinia (Vue), signals (Preact, Solid, Angular). For many apps, React context + useReducer is enough.",
    gains=["<b>One source of truth</b> for shared state.",
           "<b>No prop drilling</b> for distant components.",
           "<b>Predictable changes</b>: every update is a named action.",
           "<b>Great debugging</b>: action logs, time travel, state snapshots.",
           "<b>Reducers are trivial to test</b>: pure functions."],
    losses=["<b>Boilerplate and indirection</b> (less with modern tools).",
            "<b>Everything drifts into the store</b>, even local state.",
            "<b>Performance traps</b> with broad selectors.",
            "<b>A poor fit for server data</b> (caching, refetching) without extra tools."],
    baseline="Each line compares <b>shared state passed by props and duplicated in components</b> to the same app with a <b>global store</b> for the shared parts.",
    ratings=[(3, 3, "One clear model, but actions/selectors add indirection."),
             (3, 4, "Components read state without caring where they sit."),
             (3, 5, "Reducers and selectors are pure functions."),
             (2, 4, "One place to change shared logic; no drilling."),
             (3, 3, "Fine with narrow selectors; costly with broad ones."),
             (3, 2, "A state library adds some JS."),
             (3, 3, "Neutral."),
             (3, 4, "DevTools and time travel make bugs visible."),
             (2, 4, "Teams share a clear contract: state shape + actions.")],
    pitfalls=[("Putting everything in the store", "Form inputs, hover flags and modals all live globally; every keystroke dispatches an action.", "keep local state local; globalise only what's shared."),
              ("Caching server data by hand", "You write loading/error/refetch logic for every API call in reducers.", "use a server-state cache for API data (note 06)."),
              ("Broad selectors", "<code>useSelector(s =&gt; s)</code> re-renders the component on every change.", "select the smallest slice; memoise derived data."),
              ("Side effects in reducers", "A reducer calls the API or generates ids, so replays and tests break.", "keep reducers pure; effects in thunks/listeners.")],
    use=["State used by many distant components (session, cart, preferences, flags).",
         "Complex client-side state with many ways to change it.",
         "You need traceable, debuggable changes.",
         "Several teams touch the same shared state."],
    skip=["Small apps where context + useReducer is enough.",
          "State that's only used by one component or one subtree.",
          "Data that really belongs to the server (use a server-state cache)."],
    related=["<b>Server-state cache</b>", "<b>State machines</b>", "<b>Custom hooks</b>", "<b>Container &amp; presentational</b>"],
    quiz=[("What is the one-way data flow in Flux?", "View dispatches an action → the store/reducer computes new state → views that selected that state re-render."),
          ("Why must reducers be pure?", "So the same state and action always give the same result, which makes testing, replay and time-travel debugging possible."),
          ("Should API data live in the global store?", "Usually not. A server-state cache handles fetching, caching, deduping and refetching better."),
          ("How do you avoid needless re-renders with a store?", "Select the smallest slice a component needs and memoise derived values.")],
    remember="One <span class=\"hl\">calendar</span> for what everyone needs; your own <span class=\"hl\">notebook</span> for the rest. Change it with notes, not scribbles.",
    sources=["Facebook, “Flux: Application architecture for building user interfaces”.",
             "Redux docs, “Redux Essentials” and “Style Guide”.",
             "Kent C. Dodds, “Application State Management with React”.",
             "patterns.dev, “Provider Pattern”."],
)

# ------------------------------------------------------------------ 06 Server-State Cache
sc_problem = Doodle(760, 270, "Doodle of the same user profile fetched three times on one screen by the Header, Sidebar and Settings components, each with its own loading spinner. Going back to a page shows a spinner again, and data edited in one place stays stale in the others.",
                    "Every component fetches for itself: duplicate requests, spinners everywhere, stale copies.")
for i, name in enumerate(["Header", "Sidebar", "Settings"]):
    y = 30 + i * 74
    sc_problem.box(20, y, 160, 54, name, "paper", size=18)
    sc_problem.icon("hourglass", 196, y + 10, 1.0)
    sc_problem.arrow(230, y + 27, 470, 130, color="red", label="GET /me" if i == 0 else None, lx=340, ly=60)
sc_problem.box(476, 96, 160, 70, "API", "blue")
sc_problem.note(560, 210, "3 requests for the same user", "red")
sc_problem.note(560, 236, "back button → spinner again", "red")

sc_analogy = Doodle(760, 260, "Doodle of a newspaper on the doorstep. You read the copy you already have straight away, even if it's from this morning. Meanwhile a new edition is delivered, and you swap to it when it arrives. Everyone in the house reads the same copy.",
                    "Read the copy you have right away; swap in the new edition when it arrives.")
sc_analogy.icon("newspaper", 100, 50, 2.2)
sc_analogy.note(165, 220, "this morning's copy: read now")
sc_analogy.arrow(260, 120, 470, 120, dash=True, label="new edition on its way…", lx=365, ly=106)
sc_analogy.icon("truck", 480, 80, 1.8)
sc_analogy.note(560, 220, "swap when it arrives", "green")
sc_analogy.note(380, 252, "one copy for the whole house = one cache key", "pen")

sc_how = Doodle(760, 300, "Stale-while-revalidate flow. Three components ask the cache for the key user/me. The cache returns cached data immediately and sends a single deduplicated request to the API in the background. When the fresh data returns, the cache updates and all three components re-render. Mutations invalidate the key.",
                "One key, one request: cached data shows instantly, fresh data replaces it in the background.")
for i, name in enumerate(["Header", "Sidebar", "Settings"]):
    y = 30 + i * 74
    sc_how.box(20, y, 160, 54, name, "green", size=18)
    sc_how.arrow(186, y + 27, 300, 130)
sc_how.box(306, 80, 200, 110, "cache", "y", sub="key: [\"user\", \"me\"]")
sc_how.note(406, 70, "① show cached now", "green")
sc_how.arrow(512, 120, 600, 120, label="② 1 request", lx=550, ly=100)
sc_how.box(606, 90, 140, 64, "API", "blue")
sc_how.arrow(676, 158, 450, 196, dash=True, label="③ fresh → update all", lx=560, ly=214)
sc_how.box(286, 240, 250, 50, "mutation → invalidate", "pink", stroke="red", size=16)

SERVER = dict(
    slug="server-state-cache",
    kicker="a.k.a. “stale-while-revalidate”",
    tldr="Data from the server isn't really <i>your</i> state; it's a <b>cache of someone else's</b>. Fetch it by a <b>key</b> through a cache that <b>dedupes requests</b>, shows <b>cached data instantly</b>, <b>revalidates in the background</b>, and <b>invalidates</b> after mutations. Components just ask for the key.",
    chips=[("Family", "data fetching"), ("Libraries", "TanStack Query, SWR, RTK Query, Apollo"), ("Built on", "HTTP stale-while-revalidate idea"), ("Pairs with", "optimistic UI, global store")],
    problem="""  <p class="lead">Fetching in <code>useEffect</code> looks simple, but real apps need much more: loading and error states, caching, deduplication, retries, refetching on focus, pagination, invalidation. Doing it by hand <span class="hl-pink">everywhere</span> goes wrong.</p>
  <ul>
    <li>Three components fetch the same user, so three requests and three spinners.</li>
    <li>Navigating back shows a spinner again for data you had a second ago.</li>
    <li>After editing the profile, the header still shows the old name.</li>
    <li>Race conditions: a slow old response overwrites a newer one.</li>
  </ul>""",
    problem_figs=[sc_problem],
    analogy_side="the newspaper on the doorstep",
    analogy="""  <p>You read the <b>newspaper you already have</b>, right away, even though it's from this morning. A new edition is on its way, and when it arrives you swap it in. The whole house reads <b>one copy</b>; nobody orders their own.</p>
  <ul>
    <li>Instant reading, slightly old news: <b>stale-while-revalidate</b>.</li>
    <li>A paper older than a week goes in the recycling: <b>garbage collection</b> of unused cache entries.</li>
    <li>Big news (you changed the data)? Throw out today's copy and fetch a fresh one: <b>invalidation</b>.</li>
  </ul>""",
    analogy_figs=[sc_analogy],
    map=[("The paper you already have", "Cached data shown instantly"),
         ("The new edition arriving", "Background revalidation"),
         ("One copy for the house", "Deduplicated requests by cache key"),
         ("Recycling old papers", "Garbage-collecting unused entries"),
         ("Big news → fetch a fresh copy", "Invalidate the key after a mutation")],
    how_side="cache by key, revalidate in the background",
    how="""  <p>Every query has a <b>key</b> (<code>[\"user\", \"me\"]</code>, <code>[\"products\", { page: 2 }]</code>) and a <b>fetch function</b>. The cache decides when to use stored data and when to fetch.</p>""",
    how_figs=[sc_how],
    steps=[("Name queries by key", "Keys describe the data and its parameters, so identical requests share one cache entry."),
           ("Read through the cache", "<code>useQuery({ queryKey, queryFn })</code> returns data, status and errors; concurrent calls share one request."),
           ("Decide freshness", "<code>staleTime</code>: how long data counts as fresh. Stale data is still shown, then refetched on mount, focus or reconnect."),
           ("Mutate and invalidate", "After a POST/PUT, invalidate affected keys (or update the cache directly) so every screen refreshes."),
           ("Prefetch the next step", "Hover or route intent can prefetch data so the next screen opens without a spinner.")],
    vocab=[("Server state", "Data owned by the server that you only cache."),
           ("Query key", "The identity of a cached query."),
           ("Stale time", "How long cached data is considered fresh."),
           ("Revalidation", "Refetching in the background to update the cache."),
           ("Invalidation", "Marking cached data out of date after a change."),
           ("Deduplication", "Merging identical in-flight requests into one.")],
    code=dict(file="profile.tsx", note="TanStack Query", src="""
const userQuery = { queryKey: ["user", "me"], queryFn: () => api.get<User>("/me"), staleTime: 60_000 };

function Header() {
  const { data: user } = useQuery(userQuery);          // same key → same cache, 1 request
  return <Avatar name={user?.name} />;
}

function ProfileForm() {
  const qc = useQueryClient();
  const { data: user, isPending } = useQuery(userQuery);
  const save = useMutation({
    mutationFn: (patch: Partial<User>) => api.patch("/me", patch),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["user", "me"] }),   // all screens refresh
  });
  if (isPending) return <Skeleton />;
  return <Form initial={user} onSubmit={(v) => save.mutate(v)} />;
}
"""),
    tools="libraries: TanStack Query (React, Vue, Svelte, Solid), SWR (Vercel), RTK Query, Apollo Client / urql for GraphQL; frameworks: Next.js and Remix data caching, Angular resource().",
    gains=["<b>Instant screens</b> from cache; fewer spinners.",
           "<b>Fewer requests</b> through deduplication.",
           "<b>Fresh data</b> via background revalidation and invalidation.",
           "<b>Less code</b>: loading, error, retry and race handling built in.",
           "<b>Global store stays small</b> (only client state)."],
    losses=["<b>Stale data is shown</b> briefly; must be acceptable.",
            "<b>Cache keys must be designed</b> carefully.",
            "<b>Invalidation bugs</b> leave screens out of date.",
            "<b>Another library</b> and its mental model."],
    baseline="Each line compares <b>fetching in each component with useEffect</b> to the same app using a <b>server-state cache</b>.",
    ratings=[(2, 4, "Components declare what data they need; the cache does the rest."),
             (3, 4, "Queries are shared by key across screens."),
             (2, 4, "Query functions are plain; caches can be seeded in tests."),
             (2, 4, "One place for fetching rules instead of dozens of effects."),
             (2, 5, "Cached screens render instantly; fewer requests."),
             (3, 2, "Adds a library (roughly 10–15 kB gzipped)."),
             (3, 3, "Fewer jarring spinners; announce updates politely."),
             (2, 5, "Devtools, retries and race handling out of the box."),
             (3, 4, "Shared query definitions keep teams consistent.")],
    pitfalls=[("Copying query data into local state", "The form copies the user into useState and never sees updates.", "read from the query, or reset the form when data changes."),
              ("Keys missing parameters", "<code>[\"products\"]</code> for every page, so page 2 shows page 1.", "put every input in the key: <code>[\"products\", { page, filter }]</code>."),
              ("Forgetting to invalidate", "After saving, other screens show the old name until reload.", "invalidate (or update) affected keys in onSuccess."),
              ("Server data in the global store too", "Two caches disagree.", "server data in the query cache; client state in the store.")],
    use=["Most apps that read data from APIs.",
         "The same data is shown on several screens.",
         "You want instant back-navigation and fewer spinners.",
         "Data changes on the server and should refresh on focus or reconnect."],
    skip=["Real-time data streams (use websockets + a store or a subscription-aware cache).",
          "The framework's own data layer already caches (e.g. server components with fetch caching).",
          "A one-page app with one request."],
    related=["<b>Optimistic UI</b>", "<b>Global store</b>", "<b>Cache-aside</b> (Vol. 1)", "<b>Custom hooks</b>"],
    quiz=[("What does stale-while-revalidate mean?", "Show the cached (possibly stale) data immediately, then fetch fresh data in the background and update when it arrives."),
          ("Two components call useQuery with the same key at once. How many requests?", "One. The cache deduplicates identical in-flight queries."),
          ("Why invalidate after a mutation?", "So every screen using that data refetches and shows the change, instead of the old cached value."),
          ("What's the difference between server state and client state?", "Server state is owned by the backend and only cached locally; client state (theme, open dialogs, cart draft) is owned by the app.")],
    remember="Server data is a <span class=\"hl\">copy</span>. Show it fast, refresh it quietly, and throw it out when you know it changed.",
    sources=["TanStack Query docs, “Overview” and “Important Defaults”.",
             "Tanner Linsley, “It's Time to Break up with your Global State”.",
             "SWR docs and RFC 5861 (HTTP stale-while-revalidate).",
             "TkDodo's blog, “Practical React Query”."],
)

# ------------------------------------------------------------------ 07 Optimistic UI
op_problem = Doodle(760, 260, "Doodle of a like button. The user taps the heart and waits 800 milliseconds with a spinner before the heart turns red, so the app feels slow, and they tap again, sending two requests.",
                    "Waiting for the server on every small action makes the app feel slow and invites double taps.")
op_problem.box(30, 80, 160, 90, "♡ Like", "paper", size=24)
op_problem.arrow(196, 125, 300, 125, label="tap", lx=248, ly=112)
op_problem.icon("hourglass", 320, 90, 1.6)
op_problem.note(340, 178, "800 ms…", "red")
op_problem.arrow(370, 125, 470, 125, label="tap again?!", lx=420, ly=112, color="red")
op_problem.box(480, 80, 160, 90, "♥ Liked", "pink", size=24, stroke="red")
op_problem.note(560, 210, "finally… (2 requests sent)", "red")

op_analogy = Doodle(760, 250, "Doodle of a café counter. You order a flat white and the barista says coming right up, so you go and sit down. Almost always it arrives. Rarely they come over and say sorry, we're out of oat milk, and you choose something else.",
                    "“Coming right up!” You sit down straight away. Very rarely: “sorry, we're out of oat milk”.")
op_analogy.icon("cup", 60, 80, 1.8)
op_analogy.note(110, 210, "order a flat white")
op_analogy.arrow(160, 120, 330, 120, label="“coming right up!”", lx=245, ly=104)
op_analogy.box(340, 80, 180, 80, "sit down now", "green", size=19)
op_analogy.arrow(526, 120, 600, 80, color="green", label="99%: it arrives", lx=630, ly=64)
op_analogy.arrow(526, 130, 600, 180, color="red", dash=True, label="1%: “sorry, no oat milk”", lx=600, ly=214)

op_how = Doodle(760, 300, "Optimistic update flow. When the user taps like, the app saves a snapshot, updates the UI immediately, then sends the request. On success it keeps the change and reconciles with the server response. On error it rolls back to the snapshot and shows a message with a retry option.",
                "Update the screen first, remember how to undo, then confirm or roll back.")
op_how.box(20, 120, 140, 60, "tap ♡", "blue", size=19)
op_how.arrow(166, 150, 240, 150)
op_how.box(246, 40, 230, 60, "① snapshot old state", "y", size=16)
op_how.box(246, 120, 230, 60, "② show ♥ now", "green", size=18)
op_how.box(246, 200, 230, 60, "③ send POST /like", "paper", size=16)
op_how.arrow(482, 230, 570, 120, color="green", label="ok → keep, sync", lx=586, ly=166, anchor="start")
op_how.box(576, 80, 160, 60, "✓ done", "green", size=18)
op_how.arrow(482, 240, 570, 240, color="red", label="error", lx=526, ly=228)
op_how.box(576, 210, 160, 70, "roll back", "pink", sub="toast + retry", stroke="red")

OPTIMISTIC = dict(
    slug="optimistic-ui",
    kicker="a.k.a. “assume it worked”",
    tldr="For actions that <b>almost always succeed</b> (like, star, rename, reorder, send a message), <b>update the UI immediately</b> as if the server said yes. Send the request in the background. If it fails, <b>roll back</b> to the saved snapshot and tell the user, with a way to retry.",
    chips=[("Family", "data mutations / UX"), ("Seen in", "chat apps, likes, todo lists, Figma, Linear"), ("Built into", "React useOptimistic, TanStack Query"), ("Pairs with", "server-state cache, idempotency keys")],
    problem="""  <p class="lead">Network round trips take 100 ms to several seconds. If every tap waits for the server, the app <span class="hl-pink">feels sluggish</span>, even though the action almost never fails.</p>
  <ul>
    <li>A like button shows a spinner for 800 ms before turning red.</li>
    <li>Users tap again because nothing seemed to happen, sending duplicate requests.</li>
    <li>Reordering a list snaps back and forth while waiting.</li>
    <li>On slow mobile networks the whole app feels broken.</li>
  </ul>""",
    problem_figs=[op_problem],
    analogy_side="ordering at a café",
    analogy="""  <p>You order a flat white, the barista says <b>“coming right up!”</b>, and you go and sit down straight away. You don't stand at the counter until it's made. Almost always the coffee arrives. Very rarely, someone comes over: “sorry, we're out of oat milk, would you like something else?”</p>""",
    analogy_figs=[op_analogy],
    map=[("“Coming right up!”", "Updating the UI immediately"),
         ("Sitting down without waiting", "The user carries on interacting"),
         ("The coffee arrives", "The server confirms; keep the change"),
         ("“Sorry, no oat milk”", "The request fails; roll back and explain"),
         ("“Something else?”", "A retry or alternative action")],
    how_side="update, remember, confirm or undo",
    how="""  <p>The key is keeping a <b>snapshot</b> so you can undo, and making the request <b>safe to retry</b>. Many libraries handle the bookkeeping.</p>""",
    how_figs=[op_how],
    steps=[("Pick the right actions", "High success rate, low cost of being briefly wrong: likes, toggles, renames, reorder, messages. Not payments."),
           ("Snapshot", "Save the current cached value before changing it."),
           ("Apply the change locally", "Update the cache/state so the UI shows the new result instantly; mark it pending if useful (a faint “sending…”)."),
           ("Send the request", "With an idempotency key so retries are safe."),
           ("Settle", "On success, reconcile with the server's response (or invalidate). On error, restore the snapshot and show a clear message with retry.")],
    vocab=[("Optimistic update", "Show the expected result before the server confirms."),
           ("Pessimistic update", "Wait for the server, then update the UI."),
           ("Rollback", "Restoring the previous state after a failure."),
           ("Reconciliation", "Replacing the optimistic value with the server's truth."),
           ("Pending state", "Visual hint that a change isn't confirmed yet."),
           ("Idempotency key", "Lets a retried request be recognised as the same one.")],
    code=dict(file="useToggleLike.ts", note="TanStack Query optimistic mutation", src="""
export function useToggleLike(postId: string) {
  const qc = useQueryClient();
  const key = ["post", postId];
  return useMutation({
    mutationFn: (liked: boolean) =>
      api.put(`/posts/${postId}/like`, { liked }, { headers: { "Idempotency-Key": crypto.randomUUID() } }),
    onMutate: async (liked) => {
      await qc.cancelQueries({ queryKey: key });          // no stale refetch overwrites us
      const before = qc.getQueryData<Post>(key);           // ① snapshot
      qc.setQueryData<Post>(key, (p) => p && { ...p, liked, likes: p.likes + (liked ? 1 : -1) });  // ② show now
      return { before };
    },
    onError: (_err, _liked, ctx) => {
      qc.setQueryData(key, ctx?.before);                   // roll back
      toast.error("Couldn't save your like. Try again?");
    },
    onSettled: () => qc.invalidateQueries({ queryKey: key }),   // reconcile with the server
  });
}
"""),
    tools="built-in support: React 19 useOptimistic + actions, TanStack Query onMutate/rollback, SWR optimisticData, Apollo optimisticResponse, Remix/React Router fetcher.formData; local-first tools (Replicache, Zero, Automerge) take the idea further.",
    gains=["<b>Feels instant</b>, even on slow networks.",
           "<b>Fewer double taps</b> and duplicate requests.",
           "<b>Users keep flowing</b> instead of waiting.",
           "<b>Perceived performance</b> improves without backend changes."],
    losses=["<b>Briefly showing something untrue</b> when it fails.",
            "<b>Rollback logic</b> and edge cases (concurrent edits).",
            "<b>Harder testing</b>: success, failure and race paths.",
            "<b>Wrong for risky actions</b> (payments, deletes without undo)."],
    baseline="Each line compares <b>waiting for the server before updating the UI</b> to the same actions done <b>optimistically with rollback</b>.",
    ratings=[(4, 3, "Snapshot, rollback and reconciliation to understand."),
             (3, 3, "Neutral; usually per mutation."),
             (4, 3, "Must test success, failure and overlapping updates."),
             (4, 3, "More states to keep correct when features change."),
             (2, 5, "Interactions feel instant."),
             (3, 3, "Neutral."),
             (3, 3, "Announce failures; don't move focus unexpectedly on rollback."),
             (3, 3, "Libraries help, but it's more to wire up."),
             (3, 3, "Neutral.")],
    pitfalls=[("Optimistic payments or deletes", "The UI says “Paid!” and the card is declined a second later.", "only for safe, reversible actions; add undo for deletes instead."),
              ("Silent rollbacks", "The heart quietly turns grey again and the user never knows why.", "explain the failure and offer retry."),
              ("Refetch overwrites the optimistic value", "A background refetch lands mid-mutation and the like flickers.", "cancel in-flight queries before applying the change."),
              ("Not idempotent", "A retry after a timeout likes the post twice.", "idempotency keys or naturally idempotent requests (PUT liked=true).")],
    use=["Actions that succeed 99%+ of the time.",
         "Small, reversible changes: likes, toggles, renames, reorders, messages.",
         "Users on slow or mobile networks.",
         "Interactions where speed defines the experience (chat, editors, boards)."],
    skip=["Payments, bookings, irreversible actions.",
          "Actions that often fail validation on the server.",
          "Results that depend on server computation the client can't predict."],
    related=["<b>Server-state cache</b>", "<b>Idempotent consumer</b> (Vol. 1)", "<b>Retry with backoff</b> (Vol. 1)", "<b>State machines</b>"],
    quiz=[("What's the difference between optimistic and pessimistic updates?", "Optimistic updates show the result immediately and roll back on failure; pessimistic updates wait for the server before changing the UI."),
          ("What must you save before an optimistic update?", "A snapshot of the previous state, so you can roll back if the request fails."),
          ("Why cancel in-flight queries first?", "So a background refetch that started earlier can't overwrite the optimistic value with old data."),
          ("Name an action that should not be optimistic.", "A payment (or any irreversible or often-rejected action).")],
    remember="<span class=\"hl\">“Coming right up!”</span> Show it now, remember how to undo, and apologise clearly on the rare day it fails.",
    sources=["React docs, “useOptimistic”.",
             "TanStack Query docs, “Optimistic Updates”.",
             "Rauno Freiberg / Vercel, essays on perceived performance.",
             "Nielsen Norman Group, “Response Time Limits” (0.1 s / 1 s / 10 s)."],
)

# ------------------------------------------------------------------ 08 State Machines
sm_problem = Doodle(760, 270, "Doodle of a fetch component with four booleans: isLoading, isError, isSuccess and isRetrying. They allow 16 combinations, many impossible, such as loading and error at the same time, so the screen shows a spinner and an error message together.",
                    "Four booleans = 16 combinations, most of them impossible, and bugs live in the impossible ones.")
sm_problem.box(20, 40, 300, 180, None, "paper")
for i, t in enumerate(["isLoading = true", "isError = true", "isSuccess = false", "isRetrying = true"]):
    sm_problem.text(46, 82 + i * 34, t, anchor="start", size=18)
sm_problem.arrow(326, 130, 420, 130, color="red")
sm_problem.box(430, 50, 300, 170, None, "pink", stroke="red")
sm_problem.icon("hourglass", 470, 80, 1.2)
sm_problem.text(600, 100, "Loading…", size=18)
sm_problem.text(600, 150, "Something went wrong", size=18)
sm_problem.note(580, 250, "spinner AND error at once ✗", "red")
sm_problem.note(170, 250, "2⁴ = 16 combinations", "red")

sm_analogy = Doodle(760, 260, "Doodle of a traffic light. It can only be red, green or amber, never two at once, and it only moves in a fixed order: red to green, green to amber, amber to red. A pedestrian button is ignored while the light is already red.",
                    "A traffic light is in exactly one state, and only certain moves are allowed.")
sm_analogy.icon("traffic", 60, 40, 2.4)
sm_analogy.circle(380, 70, 40, "pink", stroke="red", label="red")
sm_analogy.circle(560, 160, 40, "green", stroke="green", label="green")
sm_analogy.circle(380, 220, 36, "y", label="amber")
sm_analogy.arrow(420, 80, 525, 135, label="timer", lx=505, ly=92)
sm_analogy.arrow(525, 180, 418, 214, label="timer", lx=505, ly=222)
sm_analogy.arrow(370, 184, 370, 112, label="timer", lx=340, ly=150, anchor="end")
sm_analogy.note(650, 60, "never two at once", "pen")

sm_how = Doodle(760, 320, "Statechart for a data request. From idle, FETCH goes to loading. From loading, RESOLVE goes to success and REJECT goes to failure. From failure, RETRY goes back to loading. From success, REFRESH goes to loading. Events not listed for a state are ignored.",
                "Explicit states + allowed events. Anything not drawn simply can't happen.")
sm_how.circle(90, 160, 56, "paper", label="idle")
sm_how.circle(330, 160, 62, "y", label="loading")
sm_how.circle(600, 70, 60, "green", label="success")
sm_how.circle(600, 260, 60, "pink", label="failure")
sm_how.arrow(148, 160, 266, 160, label="FETCH", lx=207, ly=148)
sm_how.arrow(388, 135, 540, 85, color="green", label="RESOLVE", lx=455, ly=92)
sm_how.arrow(388, 190, 540, 245, color="red", label="REJECT", lx=455, ly=242)
sm_how.arrow(560, 300, 330, 226, curve=(420, 320), label="RETRY", lx=420, ly=308)
sm_how.arrow(560, 30, 330, 96, curve=(420, 10), label="REFRESH", lx=440, ly=26)

MACHINES = dict(
    slug="state-machines",
    kicker="a.k.a. “make impossible states impossible”",
    tldr="Instead of a pile of booleans (<code>isLoading</code>, <code>isError</code>…), describe a UI as a <b>finite set of states</b> (<code>idle</code>, <code>loading</code>, <code>success</code>, <code>failure</code>) and the <b>events allowed in each</b>. The component is always in <b>exactly one state</b>, and transitions not drawn simply can't happen.",
    chips=[("Family", "state modelling"), ("Theory", "finite-state machines, Harel statecharts (1987)"), ("Libraries", "XState, Zag, Robot"), ("Pairs with", "headless components, global store")],
    problem="""  <p class="lead">UI state is often tracked with independent booleans. Four booleans allow 16 combinations, and most of them make no sense. The bugs live in <span class="hl-pink">impossible combinations</span>.</p>
  <ul>
    <li>A spinner and an error message show at the same time.</li>
    <li>The submit button is clickable while a request is already in flight, so the form is submitted twice.</li>
    <li>A late response arrives after the user cancelled and overwrites the screen.</li>
    <li>Nobody can say exactly which states the checkout flow has.</li>
  </ul>""",
    problem_figs=[sm_problem],
    analogy_side="the traffic light",
    analogy="""  <p>A <b>traffic light</b> is red, green or amber: never two at once, never purple. It moves in a fixed order. Pressing the pedestrian button while it's already red does nothing. That's a <b>state machine</b>.</p>
  <ul>
    <li>Exactly one state at a time: <b>no impossible combinations</b>.</li>
    <li>Only certain moves are allowed: <b>transitions</b>.</li>
    <li>Inputs that don't apply right now are <b>ignored</b>, not half-handled.</li>
  </ul>""",
    analogy_figs=[sm_analogy],
    map=[("Red, amber, green", "Finite states: idle, loading, success, failure"),
         ("Never two lights at once", "Exactly one current state"),
         ("Timer: red → green", "An event causing a transition"),
         ("Button ignored on red", "Events not allowed in a state are ignored"),
         ("The wiring diagram on the pole", "The statechart: documentation you can run")],
    how_side="states, events, transitions",
    how="""  <p>Draw the states and arrows first; the code follows the drawing. A plain <code>useReducer</code> with a <code>status</code> field already gets you most of the way; libraries like XState add nested and parallel states, guards, timers and a visualiser.</p>""",
    how_figs=[sm_how],
    steps=[("List the real states", "Replace booleans with one <code>status</code>: <code>\"idle\" | \"loading\" | \"success\" | \"failure\"</code>."),
           ("List the events", "<code>FETCH</code>, <code>RESOLVE</code>, <code>REJECT</code>, <code>RETRY</code>, <code>CANCEL</code>: things that happen, named in the past or imperative."),
           ("Define allowed transitions", "For each state, which events move where. Anything else is ignored."),
           ("Attach data to states", "Errors only exist in <code>failure</code>; results only in <code>success</code> (a TypeScript discriminated union enforces it)."),
           ("Render by state", "<code>switch (state.status)</code> renders exactly one view; the button is disabled because the state says so.")],
    vocab=[("Finite-state machine", "A model with a fixed set of states and transitions."),
           ("Statechart", "State machines with nesting, parallel regions and history."),
           ("Event", "Something that happened and may cause a transition."),
           ("Guard", "A condition that must be true for a transition."),
           ("Discriminated union", "A TS type where a tag field decides the shape."),
           ("Impossible state", "A combination of values that should never occur.")],
    code=dict(file="useRequest.ts", note="a tiny state machine with useReducer", src="""
type State =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: Order[] }
  | { status: "failure"; error: string };
type Event = { type: "FETCH" } | { type: "RESOLVE"; data: Order[] } | { type: "REJECT"; error: string } | { type: "RETRY" };

function machine(state: State, event: Event): State {
  switch (state.status) {
    case "idle":    return event.type === "FETCH" ? { status: "loading" } : state;
    case "loading": return event.type === "RESOLVE" ? { status: "success", data: event.data }
                         : event.type === "REJECT" ? { status: "failure", error: event.error } : state;
    case "failure": return event.type === "RETRY" ? { status: "loading" } : state;
    case "success": return event.type === "FETCH" ? { status: "loading" } : state;
  }
}

// render exactly one view per state
switch (state.status) {
  case "loading": return <Spinner />;
  case "failure": return <ErrorPanel message={state.error} onRetry={() => send({ type: "RETRY" })} />;
  case "success": return <OrderList orders={state.data} />;
  default:        return <button onClick={() => send({ type: "FETCH" })}>Load orders</button>;
}
"""),
    tools="tools: XState (+ Stately visual editor), Zag.js (state machines behind Ark UI widgets), Robot, @xstate/store; plain TypeScript discriminated unions + useReducer for small cases.",
    gains=["<b>Impossible states can't happen.</b>",
           "<b>Every flow is documented</b> as a diagram you can run.",
           "<b>Fewer race-condition bugs</b> (late events are ignored).",
           "<b>Easy to test</b>: given state + event, expect state.",
           "<b>Shared language</b> with designers and product."],
    losses=["<b>More upfront modelling</b> than a few booleans.",
            "<b>Unfamiliar</b> to many teams.",
            "<b>Library weight</b> if you use a full statechart engine.",
            "<b>Overkill</b> for a simple toggle."],
    baseline="Each line compares <b>UI state tracked with independent booleans</b> to the same UI modelled as an <b>explicit state machine</b>.",
    ratings=[(3, 3, "More upfront thinking, much simpler reading later."),
             (3, 4, "Machines are reusable across UIs (and frameworks)."),
             (2, 5, "Pure transition functions; even model-based testing."),
             (2, 4, "Adding a state or event is a visible, local change."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral by hand; a statechart library adds some kB."),
             (3, 4, "Focus and announcements can be tied to clear states."),
             (3, 4, "Visualisers and types catch mistakes early."),
             (3, 4, "Diagrams make complex flows easy to hand over.")],
    pitfalls=[("Booleans next to the machine", "A status field plus an extra <code>isSubmitting</code> flag that drifts out of sync.", "derive everything from the one state; no parallel flags."),
              ("A machine for every toggle", "An accordion open/closed gets a full XState setup.", "use a boolean or useReducer for trivial cases."),
              ("Handling every event in every state", "Defensive code reacts to events that shouldn't be possible, recreating the mess.", "let unlisted events be ignored by design."),
              ("Not drawing it", "The machine exists only in code and nobody can review it.", "keep a diagram (or use a visual editor) in the PR.")],
    use=["Multi-step flows: checkout, onboarding, wizards, uploads.",
         "Async UI with loading, error, retry and cancel.",
         "Complex widgets (comboboxes, date pickers, drag and drop).",
         "Bugs keep appearing in “weird” combinations."],
    skip=["A single toggle or open/closed flag.",
          "Static pages with no interaction.",
          "A server-state library already models loading/error for you (use its status)."],
    related=["<b>Headless components</b>", "<b>Global store</b>", "<b>Optimistic UI</b>", "<b>Saga</b> (Vol. 1, orchestration)"],
    quiz=[("Why are four independent booleans risky?", "They allow 2⁴ = 16 combinations, many of which are impossible (like loading and error together) and cause bugs."),
          ("What happens to an event not allowed in the current state?", "It's ignored; the machine stays in its current state."),
          ("How does TypeScript help?", "A discriminated union ties data to states (error only exists in failure), so invalid access fails to compile."),
          ("What do statecharts add to plain state machines?", "Nested (hierarchical) states, parallel regions, history and guards, which keep complex machines manageable.")],
    remember="If you can <span class=\"hl\">draw it</span>, you can trust it. One state at a time, and only the arrows you drew.",
    sources=["David Harel, “Statecharts: A Visual Formalism for Complex Systems” (1987).",
             "David Khourshid, XState docs and “No, disabling a button is not app logic”.",
             "Kent C. Dodds, “Stop using isLoading booleans”.",
             "Richard Feldman, “Making Impossible States Impossible” (talk)."],
)

NOTES = [STORE, SERVER, OPTIMISTIC, MACHINES]
