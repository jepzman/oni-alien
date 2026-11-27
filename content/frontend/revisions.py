# Revisions to Vol. 2 (November 2026): one situational quiz question and a “try it” per note.
# Merged into the notes by scripts/build_notes.py (load_content).

REVISION_NOTE = ("Nov 2026", "every note gains a “what would you do?” question and a try it; related notes are links now")

REVISIONS = {
    "container-presentational": dict(
        quiz_add=[("A designer wants to see the product card in Storybook with five price states, but the card fetches its own price and reads the cart from context. What do you change?",
                   "Split it: a presentational ProductCard that takes price, stock and an onAdd callback as props, and a small container that fetches and passes them in. Storybook and tests use the presentational part with any props they like.")],
        try_it="Take a component in your app that both fetches data and renders it. Split it into a container and a presentational component, then write one Storybook story or test for the presentational part with three different props. Note how many lines of setup the test no longer needs.",
    ),
    "compound-components": dict(
        quiz_add=[("Your Modal component has 23 props, including headerIcon, footerAlign and hideCloseOnMobile, and every new screen asks for one more. What do you offer instead?",
                   "A compound API: Modal, Modal.Header, Modal.Body, Modal.Footer and Modal.Close sharing open state through context. Screens compose the parts they need and put any content inside, so new layouts don't need new props.")],
        try_it="Build an Accordion with Accordion, Accordion.Item, Accordion.Button and Accordion.Panel sharing state through context in about 60 lines. Use it twice with different layouts. Then try to use Accordion.Button outside an Accordion and make it throw a clear error.",
    ),
    "custom-hooks": dict(
        quiz_add=[("Three screens copy the same 40 lines: read a query parameter, debounce it, fetch results, cancel the old request. A bug was fixed in one copy only. What do you do, and how do you check the fix applies everywhere?",
                   "Move the logic into one hook, such as useSearch(param), use it in all three screens, and test the hook on its own with renderHook (debounce, cancellation, error). The fix now lives in one place.")],
        try_it="Write useOnlineStatus() (listen to the online and offline events, clean up on unmount) and use it in two components. Test it with renderHook by firing the events. Then use it in a component rendered twice and confirm each copy has its own state.",
    ),
    "headless-components": dict(
        quiz_add=[("Your team built a custom dropdown. A screen-reader user reports it announces nothing and can't be opened from the keyboard. You have one week. What do you do?",
                   "Replace its behaviour with a headless library (Downshift, Radix, React Aria) and keep your own markup and styles. You get keyboard handling, focus and ARIA that have been tested with real assistive technology, without redesigning anything. If a native select is enough, use that.")],
        try_it="Rebuild one custom dropdown or menu in your app with a headless library, keeping your current CSS. Then test it with the keyboard only (Tab, arrows, Enter, Escape) and with your operating system's screen reader, before and after.",
    ),
    "global-store": dict(
        quiz_add=[("The global store holds the cart, the user, 14 lists of API data and a loading flag for each. Bugs come from stale lists after edits. Which state do you move out of the store, and where?",
                   "The API data and its loading flags: put them in a server-state cache (TanStack Query, SWR, RTK Query) that handles refetching and invalidation. Keep only real client state (cart, user preferences, UI state) in the store.")],
        try_it="Write a small cart store with Redux Toolkit or Zustand (add, remove, change quantity) and render the item count in two places. Use the browser devtools to step through the actions. Then subscribe a component to the whole store instead of a slice and count the re-renders.",
    ),
    "server-state-cache": dict(
        quiz_add=[("After a user renames a project, the sidebar still shows the old name until a full page reload. Both the sidebar and the settings page use useQuery. What is missing?",
                   "The mutation doesn't invalidate (or update) the cached queries that include the project. Invalidate ['projects'] and ['project', id] on success, or write the new name into the cache, and the sidebar refetches or updates by itself.")],
        try_it="Load the same user profile in two components with TanStack Query and check in the network tab that only one request goes out. Add a rename mutation and see the stale name; then add invalidateQueries in onSuccess and see both components update.",
    ),
    "optimistic-ui": dict(
        quiz_add=[("Product asks for optimistic updates everywhere, including “Place order” and “Delete account”. Which do you make optimistic, and what do you say?",
                   "Neither. Optimistic UI suits actions that almost always succeed and are cheap to undo (likes, renames, reordering). Placing an order and deleting an account have real consequences and can fail for business reasons; show a clear pending state and confirm only when the server agrees.")],
        try_it="Build a like button with an optimistic update, then make the API fail one call in three on purpose. Check that the count rolls back and the user sees a message with a retry. Then click quickly ten times and see whether the final count is right.",
    ),
    "state-machines": dict(
        quiz_add=[("A checkout form shows a spinner and an error message at the same time, and pressing Pay twice sends two payments. The component has isLoading, isError, isSuccess and isSubmitting. What do you do?",
                   "Replace the four flags with one state (editing, submitting, failed, paid) and define which events each state accepts. Pay is ignored while submitting, so no double charge, and spinner and error can't show together because they belong to different states.")],
        try_it="Draw your login or upload flow as states and arrows on paper first. Then implement it with useReducer (or XState) so unknown events are ignored, and add a test that sends “submit” twice in the submitting state and expects one request.",
    ),
    "ssr-hydration": dict(
        quiz_add=[("A server-rendered dashboard shows content in 0.8 s, but buttons do nothing until 4 s on mid-range phones. Users tap and think it's broken. What do you look at first?",
                   "The JavaScript that must download and hydrate before the page responds: the bundle size and the components that hydrate. Move non-interactive parts to server components, lazy-load heavy widgets, and hydrate below-the-fold parts later. SSR made it visible early, not usable early.")],
        try_it="Render one page with SSR, then throttle the CPU four times and the network to “Fast 3G” in devtools. Record when the content appears and when a button first responds. Put a Date.now() in the render to trigger a hydration mismatch and read the warning.",
    ),
    "islands": dict(
        quiz_add=[("A marketing site in a React SPA ships 400 KB of JavaScript for pages that are 95% text, with a newsletter form and an image carousel. What do you propose?",
                   "Islands: render the pages as HTML (Astro or similar) and hydrate only the form and the carousel, the carousel when it becomes visible. Most of the JavaScript disappears and the interactive parts keep working.")],
        try_it="Create an Astro page with mostly static text and two React components, one with client:load and one with client:visible. Check the network tab while scrolling to see when each script arrives. Then remove the directive from one and see it render as plain HTML.",
    ),
    "code-splitting": dict(
        quiz_add=[("The admin section (charts, a rich text editor) makes up 60% of the bundle, and 3% of users ever open it. What do you split, and what do you keep in the main chunk?",
                   "Lazy-load the admin routes with dynamic import() so only admins download that code, and prefetch them when an admin hovers the menu link. Keep the shell, routing, layout and the landing route in the entry chunk.")],
        try_it="Run a bundle analyser (rollup-plugin-visualizer or source-map-explorer) on your app and find the largest dependency. Move the route or feature that uses it behind a dynamic import, rebuild, and compare the entry chunk size and the load time on a throttled network.",
    ),
    "virtualization": dict(
        quiz_add=[("A transaction list with 20,000 rows freezes for 3 seconds on open. Users also use Ctrl+F to find a payee. What do you do?",
                   "Virtualize the list so only visible rows render, and since browser search can't find rows that aren't in the DOM, add your own search or filter box. Check keyboard navigation and screen-reader announcements of the row count.")],
        try_it="Render 20,000 rows plainly and measure the time to first render in the performance panel. Then virtualize with TanStack Virtual or react-window and measure again. Try Ctrl+F for a row far down the list in both versions.",
    ),
    "micro-frontends": dict(
        quiz_add=[("Two teams of five work on one React app and complain about merge conflicts and a slow release. Someone proposes micro-frontends. What do you suggest first?",
                   "A modular monolith in the frontend: clear folder ownership, CODEOWNERS, module boundaries enforced by lint rules, and a faster CI. Micro-frontends add a shell, shared dependencies and runtime integration; they pay off when many teams need independent deploys.")],
        try_it="Create a shell app and one remote with Vite and module federation, and load the remote's page from the shell at runtime. Change and redeploy only the remote and refresh the shell. Then load two different React versions and see what breaks.",
    ),
    "design-tokens": dict(
        quiz_add=[("A rebrand changes the primary blue. Engineers find the old hex value in 312 places, some in CSS, some in the iOS app. How do you make the next rebrand a one-line change?",
                   "Introduce tokens: primitives (blue.600) and semantic names (color.action.primary) in one JSON source, generated for web, iOS and Android, and replace raw values with semantic tokens. A lint rule can block new hard-coded colours.")],
        try_it="Write ten tokens (four colours, three spacings, three font sizes) in a JSON file and generate CSS variables from it with Style Dictionary. Replace the raw values in one component, then add a dark theme by changing only the semantic tokens.",
    ),
    "error-boundaries": dict(
        quiz_add=[("A third-party weather widget on your dashboard crashes when its API returns null, and the whole dashboard goes white. What do you change, and what still won't be caught?",
                   "Wrap the widget (and each dashboard card) in its own error boundary with a small fallback and a retry, and report the error. Errors in event handlers, async code and the server render are not caught by a boundary; handle those with try/catch and the data layer.")],
        try_it="Add a component that throws when a prop is missing, render it inside a dashboard, and watch the page go blank. Wrap it in react-error-boundary with a fallback and a reset button. Then throw from a click handler and see that the boundary doesn't catch it.",
    ),
}

for _rev in REVISIONS.values():
    _rev.setdefault("revised", ("Nov 2026", "a “what would you do?” question and a try it"))
