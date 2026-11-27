# Deep dive 05 · Caching. Builds on Vol. 1 note 17 (cache-aside) and Vol. 2 server-state cache.
# Example, from the cache-aside note: the product page for product 42 (the mug, $24.50), key product:42,
# a 40 ms database query, a 5-minute TTL. The shop serves 2,000 product reads a second; the database can do 400.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
layers_svg = '''
  <rect class="bx" x="10" y="50" width="110" height="64" rx="8"/><text class="lbl" x="65" y="78" text-anchor="middle">browser</text><text class="soft" x="65" y="100" text-anchor="middle">one shopper</text>
  <rect class="bx" x="160" y="50" width="110" height="64" rx="8"/><text class="lbl" x="215" y="78" text-anchor="middle">CDN</text><text class="soft" x="215" y="100" text-anchor="middle">everyone nearby</text>
  <rect class="bx" x="310" y="50" width="110" height="64" rx="8"/><text class="lbl" x="365" y="78" text-anchor="middle">app memory</text><text class="soft" x="365" y="100" text-anchor="middle">one instance</text>
  <rect class="bx-y" x="460" y="50" width="110" height="64" rx="8"/><text class="lbl" x="515" y="78" text-anchor="middle">Redis</text><text class="soft" x="515" y="100" text-anchor="middle">all instances</text>
  <rect class="bx-g" x="630" y="50" width="120" height="64" rx="8"/><text class="lbl" x="690" y="78" text-anchor="middle">database</text><text class="soft" x="690" y="100" text-anchor="middle">the truth · 40 ms</text>
  <path class="ln" d="M120 82 H158" marker-end="url(#a)"/><path class="ln" d="M270 82 H308" marker-end="url(#a)"/><path class="ln" d="M420 82 H458" marker-end="url(#a)"/><path class="ln" d="M570 82 H628" marker-end="url(#a)"/>
  <text class="soft" x="290" y="26" text-anchor="middle">a request stops at the first layer that has a copy</text>
  <text class="soft" x="65" y="140" text-anchor="middle">0 ms</text><text class="soft" x="215" y="140" text-anchor="middle">~20 ms</text><text class="soft" x="365" y="140" text-anchor="middle">~0 ms</text><text class="soft" x="515" y="140" text-anchor="middle">~1 ms</text>
  <path class="ln-d" d="M440 150 V172 H590 V150"/><text class="soft" x="515" y="192" text-anchor="middle">the cache-aside note lived here</text>
'''
recap = '''
<p>The cache-aside note was about a fridge. Product 42, the mug, is read thousands of times a minute and changes about once a month, so the app keeps a copy in Redis under <code>product:42</code> for five minutes. A read checks Redis first. A write updates the database and deletes the key.</p>
''' + tbl(["Note", "In one line"], [
    ["Cache-Aside", "check the cache; on a miss read the database and keep a copy with an expiry; on a write, delete the copy"],
    ["Server-State Cache", "the browser shows the copy it has at once and fetches a fresh one in the background"],
]) + fig(760, 200, "The caches a product page passes on its way to the database: the browser, which serves one shopper; the CDN, which serves everyone nearby; the app's own memory, one instance; Redis, shared by all instances; and the database, the truth, which takes 40 milliseconds. A request stops at the first layer that has a copy. The cache-aside note covered only the step between Redis and the database.",
          layers_svg, "Five places hold a copy of the mug's price. Four of them can be wrong.") + mn("Both notes are the same idea at different distances from the database.") + '''
<p class="full">The notes showed the happy path and named the famous problem, invalidation. This deep dive is about what a cache does to a system once it is there: the database gets sized for the traffic the cache lets through, copies in five places expire at five different times, and a fix deployed at noon is still invisible to some shoppers at a quarter past. A cache is easy to add and hard to remove, so it is worth knowing the cost first.</p>
'''

# ------------------------------------------------------------------ 2 what a cache is
bet = '''
<p>A cache is a bet: this answer will be asked for again before it changes. When the bet wins, you skip the work. When it loses, you either did extra work for nothing, or you served an answer that is no longer true. Every cached thing needs three decisions.</p>
''' + tbl(["Question", "For <code>product:42</code>"], [
    ["How old may the copy be?", "a description may be hours old; a price, a minute; the price used to charge a card, zero"],
    ["How do we learn that it changed?", "wait for it to expire, or be told"],
    ["What happens when the copy is missing?", "one 40 ms query, or five hundred of them at once"],
]) + mn("If nobody can answer question 1 for a piece of data, it is not ready to be cached.") + '''
<h3>The number that matters is the miss rate</h3>
<p>People quote the hit ratio. The database only feels the misses.</p>
''' + tbl(["Hit ratio", "Typical read", "Reads reaching the database, of 2,000 a second"], [
    ["0 % (no cache)", "40 ms", "2,000. It can do 400"],
    ["90 %", "about 5 ms", "200"],
    ["95 %", "about 3 ms", "100"],
    ["99 %", "about 1.4 ms", "20"],
], hot=(0,)) + '''
<p>From 95 % to 99 % looks like a small step. It is five times less load on the database. And the first row is the important one: without the cache, this shop does not work at all.</p>
''' + full('''<h3>When a cache becomes load-bearing</h3>
<p>A cache starts as an optimisation. Traffic grows, and nobody resizes the database, because the cache is absorbing the growth. One day the database can serve a fifth of the read traffic, and the cache is no longer an optimisation. It is a part the system cannot run without, and it was never designed as one: it has no backup, it starts empty, and the code treats it as optional.</p>
<p>Two honest positions exist.</p>
''' + tbl(["Position", "Means"], [
    ["<b>The cache is optional</b>", "the database can carry all the traffic, slowly. Losing the cache is a bad afternoon"],
    ["<b>The cache is required</b>", "treat it like a database: replicas, a warm-up plan, load shedding for when it is empty (drill 3)"],
]) + '''<p>The dangerous place is in between: required in fact, optional in everyone's head. A yearly test that switches the cache off in a load-test environment tells you which position you are really in.</p>
<h3>What a cache does not fix</h3>
<p>If a query takes 40 ms because an index is missing, the cache hides the slow query from most users and leaves it in place for the rest, including every user after a restart. Fix the query first. Cache what is still too slow or too frequent after that.</p>''')

# ------------------------------------------------------------------ 3 patterns
patterns = '''
<p>Cache-aside is one of five arrangements. They differ in who talks to the database and when the copy is written.</p>
''' + tbl(["Pattern", "Read", "Write", "Main risk"], [
    ["<b>Cache-aside</b>", "app checks cache, then database, then fills the cache", "app writes database, deletes the key", "the app must remember every key it affects"],
    ["<b>Read-through</b>", "app asks the cache; the cache loads from the database itself", "as cache-aside", "the cache needs to know how to load each kind of data"],
    ["<b>Write-through</b>", "from the cache", "app writes the cache; the cache writes the database before answering", "every write pays for both; the cache fills with data nobody reads"],
    ["<b>Write-behind</b>", "from the cache", "app writes the cache; the database is updated later, in batches", "a cache crash loses writes that were already confirmed"],
    ["<b>Refresh-ahead</b>", "from the cache", "as cache-aside", "the cache reloads popular keys before they expire; wasted work on keys that stop being popular"],
], hot=(3,)) + mn("Write-behind makes the cache the source of truth for a while. Only for data you can afford to lose, like view counters.") + '''
<h3>Which to use</h3>
''' + tbl(["Situation", "Choose"], [
    ["Most application data", "cache-aside, or read-through if your library offers it. Only data that is asked for gets cached, and a cache failure leaves the database correct"],
    ["A few very hot keys that are slow to rebuild", "add refresh-ahead for those keys (chapter 6)"],
    ["Counters, “last seen”, statistics", "write-behind is acceptable; say so in the code"],
    ["Money, stock, anything a decision is based on", "do not read it from a cache when deciding (chapter 5)"],
]) + full('''<h3>Why “delete”, not “update”, on a write</h3>
<p>The note said to delete the key after a write and not to set the new value. The reason is two writers.</p>
''' + tbl(["Time", "Writer A (price 25)", "Writer B (price 26)", "Cache holds"], [
    ["1", "updates database to 25", "", "24.50"],
    ["2", "", "updates database to 26", "24.50"],
    ["3", "", "sets cache to 26", "26"],
    ["4", "sets cache to 25", "", "<b>25</b>, and the database says 26"],
], hot=(3,)) + '''<p>The cache writes arrived in a different order from the database writes, and the wrong value stays until the TTL. A delete has no value to get wrong: whoever deletes last, the key is gone and the next read loads the truth. Deleting does leave one smaller race, between a reader and a writer. That is drill 1.</p>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Guess first. Each of these has happened to a shop like ours.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · stale put-back</a></li><li><a href="#drill-2">2 · stampede</a></li><li><a href="#drill-3">3 · cold start</a></li>
  <li><a href="#drill-4">4 · lost delete</a></li><li><a href="#drill-5">5 · missing things</a></li><li><a href="#drill-6">6 · wrong key</a></li>
</ul>
''' + drill(1, "The reader puts the old price back", [
    ("Timeline", "The key has just expired. A reader misses and reads the price from the database: 24.50. Before it can fill the cache, an admin changes the price to 26 and deletes the key, which is already empty. Then the reader writes its 24.50 into the cache."),
    ("What you see", "The database says 26 and the product page says 24.50 for the next five minutes. The delete happened, the logs say so, and the page is still wrong.", True),
    ("What saves you", "The TTL is the safety net: it bounds the damage to five minutes, which is why every key has one. To narrow the race further, delete the key a second time about a second after the write, or store the row's version with the value and let the cache accept a write only if its version is newer."),
], "delete-on-write still has a race. A TTL on every key is what makes it a small problem.") + drill(2, "Five hundred requests rebuild the same thing", [
    ("Timeline", "The home page shows “bestsellers”, a query that takes 2 seconds. It is cached for ten minutes and requested 500 times a second. The key expires. For the next two seconds every request misses, and each one starts the 2-second query."),
    ("What you see", "A thousand copies of the heaviest query in the system, all at once. The database slows down, so the queries take longer, so more requests pile in. Every ten minutes the site stutters.", True),
    ("What saves you", "Let <b>one</b> request rebuild the value while the others wait for it or are given the old value. This is called single flight. Combine it with a soft expiry, so the old value is still there to serve, and with a random spread on TTLs so that many keys do not expire in the same second (chapter 6)."),
], "a miss on a hot key must cause one rebuild, not one per waiting request.") + drill(3, "The cache restarts empty", [
    ("Timeline", "Redis is restarted for an upgrade and comes back with nothing in it. The hit ratio is zero. All 2,000 reads a second go to a database that can serve 400."),
    ("What you see", "The database is overloaded. Queries time out, so nothing is written to the cache, so the cache stays empty. The system cannot warm itself up: a metastable failure, as in the Resilience Stack deep dive.", True),
    ("What saves you", "Plan for an empty cache as a normal event. Keep a replica so a restart does not empty it. Warm the top few thousand keys from a script before taking traffic. And put a limit on concurrent cache-miss queries, so that the database serves 400 a second well and the rest get a fast “try again” while the cache fills."),
], "if the system cannot start with an empty cache, the cache is a database and needs to be run like one.") + drill(4, "The delete never arrived", [
    ("Timeline", "The admin changes the price. The database commits. The <code>DEL product:42</code> that follows hits a two-second network blip and fails. The request has already told the admin “saved”."),
    ("Why", "Two systems were written one after the other with no transaction around them. It is the dual-write problem from the outbox note, with a cache where the broker was.", True),
    ("What saves you", "The TTL, again, limits it to five minutes. To do better, take the delete out of the request: write an invalidation record in the same transaction as the price, or let change data capture read the database's log, and have a small worker delete keys with retries. That also covers changes made by scripts and by hand, which never ran your application code."),
], "invalidation that happens after the commit can be lost. Make it retryable, and keep the TTL.") + drill(5, "Asking for things that do not exist", [
    ("Timeline", "A crawler requests <code>/product/900001</code>, <code>/product/900002</code> and so on. None exist. Each request misses the cache, queries the database, finds nothing, and stores nothing. The next request for the same id does it all again."),
    ("What you see", "Database load that grows with junk traffic. The hit ratio falls and nobody changed anything. A related case: a real lookup fails with an error, and the error page is cached for five minutes.", True),
    ("What saves you", "Cache the answer “not found” too, with a short TTL such as 30 seconds. Reject ids that cannot be valid before any lookup. And never cache a failure as if it were data: a timeout or a 500 is not an answer."),
], "“nothing” is an answer worth caching briefly. An error is not an answer at all.") + drill(6, "The right value under the wrong key", [
    ("Timeline", "Trade customers get the mug for 19.00. The page for product 42 is rendered for a logged-in trade customer and stored under <code>product:42</code>. For the next five minutes every shopper sees the trade price. The same thing at the CDN is worse: a page containing “Hello, Sam” and Sam's saved address, served to strangers."),
    ("Why", "The key named less than the value depended on. Anything that changes the answer and is missing from the key is a leak waiting for the right request order.", True),
    ("What saves you", "The key lists everything the value depends on: <code>product:42:price-list:trade</code>. Cache the shared parts and the personal parts separately. Mark personal responses <code>Cache-Control: private</code> or <code>no-store</code> so that no shared cache keeps them."),
], "a cache key must contain everything that can change the answer. Personal data never goes in a shared cache.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Decision", "Drill"], [
    ["every key has a TTL, with a random spread", "1, 2, 4"],
    ["one rebuild per key at a time; the old value served meanwhile", "2"],
    ["a plan for an empty cache: replica, warm-up, a cap on miss queries", "3"],
    ["invalidation that survives a failed delete", "4"],
    ["“not found” is cached briefly; errors are never cached", "5"],
    ["keys name everything the value depends on", "6"],
]))

# ------------------------------------------------------------------ 5 invalidation
invalidation = '''
<p>The old joke says there are two hard things in computing, and cache invalidation is one of them. It is hard for a plain reason: the code that changes the data has to know about every copy of it, and the copies were added later, by other people, for other screens.</p>
<h3>One price change, five copies</h3>
''' + tbl(["Where the mug's price appears", "Key"], [
    ["its product page", "<code>product:42</code>"],
    ["the “Mugs” category list", "<code>category:mugs:page:1</code>"],
    ["search results for “mug”", "<code>search:mug:page:1</code>"],
    ["bestsellers on the home page", "<code>bestsellers</code>"],
    ["baskets that contain it", "<code>basket:c-7</code>, and many more"],
]) + mn("The first key is obvious. The other four are how stale prices actually reach customers.") + '''
<h3>Five ways to invalidate</h3>
''' + tbl(["Strategy", "How", "Good for", "Weak at"], [
    ["<b>Expiry only</b>", "a TTL and nothing else", "data where “a few minutes old” is fine: bestsellers, counts", "anything that must change quickly"],
    ["<b>Delete on write</b>", "the code that writes also deletes the keys", "single-item keys such as <code>product:42</code>", "derived keys; writers that bypass the code"],
    ["<b>Events</b>", "a worker hears “price of 42 changed” (outbox or CDC) and deletes keys, with retries", "many keys per change; changes from anywhere", "you still need to know which keys"],
    ["<b>Versioned keys</b>", "the key contains a version: <code>product:42:v17</code>. A change makes a new key; the old one is never read again and expires", "immutable content; build assets; avoiding the races entirely", "readers must learn the current version from somewhere"],
    ["<b>Tags</b>", "each entry is labelled with what it contains: this list page “contains 42”. Invalidate everything tagged 42", "lists, search results, rendered pages", "needs a cache or CDN that supports it"],
]) + full('''<p>Real systems mix them. For the shop: the product page is deleted on write through an event worker. List and search pages carry tags, or simply a short TTL of a minute. Bestsellers expire on their own. Static files such as scripts and images get versioned names and are cached for a year, because a new version is a new name.</p>
<h3>Decide the staleness, then the mechanism</h3>
<p>The useful conversation is with the business, about question 1 from chapter 2.</p>
''' + tbl(["Data", "May be stale for", "So"], [
    ["Product description, photos", "an hour", "long TTL, delete on write"],
    ["Price shown on a page", "a minute", "short TTL plus event-driven delete"],
    ["“In stock” label", "a minute, and it may be wrong", "short TTL; the label is a hint"],
    ["Bestsellers", "ten minutes", "expiry only"],
    ["Price and stock <b>at checkout</b>", "not at all", "read from the database, inside the transaction"],
], hot=(4,)) + '''<h3>The rule that removes most of the fear</h3>
<p><mark>Cache what is shown. Never decide on a cached value.</mark> The product page may show 24.50 from a copy that is forty seconds old. The checkout reads the price from the database when it creates the order, and if it has changed, tells the shopper. With that one rule, a stale cache can produce a surprised customer, and it cannot produce a wrong charge. Stock works the same way: the page says “in stock” from a cache, and the reservation is made against the real number.</p>''')

# ------------------------------------------------------------------ 6 ttl and numbers
ttl_svg = '''
  <text class="lbl" x="20" y="26">one cached value over time</text>
  <rect class="bx-g" x="20" y="44" width="430" height="46" rx="6"/><text class="lbl" x="235" y="73" text-anchor="middle">fresh: serve it</text>
  <rect class="bx-y" x="450" y="44" width="170" height="46" rx="6"/><text class="lbl" x="535" y="64" text-anchor="middle">stale: serve it,</text><text class="lbl" x="535" y="82" text-anchor="middle">refresh once</text>
  <rect class="bx-r" x="620" y="44" width="120" height="46" rx="6"/><text class="lbl" x="680" y="73" text-anchor="middle">gone: miss</text>
  <path class="ln" d="M20 104 H740"/>
  <text class="soft" x="20" y="126">0</text><text class="soft" x="450" y="126" text-anchor="middle">5 min</text><text class="soft" x="620" y="126" text-anchor="middle">7 min</text>
  <text class="soft" x="450" y="148" text-anchor="middle">soft TTL</text><text class="soft" x="620" y="148" text-anchor="middle">hard TTL</text>
'''
numbers = '''
<p>A TTL is usually picked by feel: “five minutes sounds right”. It can be worked out, from how often the key is read.</p>
<p><mark>Hit ratio of one key ≈ 1 − 1 ÷ (reads per second × TTL in seconds)</mark></p>
<p>In each TTL period the first read misses and the rest hit.</p>
''' + tbl(["Key", "Reads", "TTL", "Reads per TTL", "Hit ratio"], [
    ["product 42, the popular mug", "80 a second", "5 min", "24,000", "99.996 %"],
    ["the same", "80 a second", "10 s", "800", "99.9 %"],
    ["a typical product", "1 a minute", "5 min", "5", "80 %"],
    ["a rarely viewed product", "1 an hour", "5 min", "0.08", "about 0 %"],
], hot=(1, 3)) + mn("Row 2 is the surprise: for a hot key, ten seconds is plenty.") + '''
<p>Two lessons. For a hot key a very short TTL already gives nearly all the benefit, so you can have fresh data and a high hit ratio together. For a cold key no reasonable TTL helps: it is written to the cache, never read and evicted. Most catalogues have a few hot items and a long tail of cold ones, and the cache earns its keep on the hot few.</p>
<h3>Soft and hard expiry</h3>
''' + fig(760, 160, "The life of one cached value. From zero to five minutes it is fresh and is served. Between the soft TTL at five minutes and the hard TTL at seven minutes it is stale: it is still served, and one background refresh is started. After seven minutes it is gone and a read is a miss.",
          ttl_svg, "Between the two expiries, readers get the old value at once and one of them triggers a refresh.") + code("get-product.ts", "serve stale, refresh once", '''
const inFlight = new Map<string, Promise<Product>>();      // single flight, per instance

export async function getProduct(id: string): Promise<Product> {
  const key = `product:${id}`;
  const hit = await cache.get(key);                        // { value, softExpiry }
  if (hit && Date.now() < hit.softExpiry) return hit.value;  // fresh
  if (hit) { refresh(key, id); return hit.value; }           // stale: serve, refresh behind
  return refresh(key, id);                                   // gone: wait for the load
}

function refresh(key: string, id: string) {
  if (!inFlight.has(key)) {
    inFlight.set(key, loadAndStore(key, id).finally(() => inFlight.delete(key)));
  }
  return inFlight.get(key)!;                                 // everyone shares one load
}
''') + full('''<p>This is the fix for drill 2, and it is the same idea as the browser's stale-while-revalidate from the server-state cache note. No shopper waits for a rebuild unless the value is entirely gone, and there is one rebuild however many are asking. Across several app instances, a short lock in Redis keeps it to one rebuild in total.</p>
<h3>Spread the expiries</h3>
<p>If ten thousand keys are written in the same minute, for instance after a deploy or a warm-up script, they expire in the same minute too. Add a random part to every TTL, such as five minutes plus or minus thirty seconds, so the reloads arrive as a trickle.</p>
<h3>Sizing the memory</h3>
''' + tbl(["Quantity", "Reasoning", "Value"], [
    ["Entries worth caching", "the products that get most of the views; not all 200,000", "about 20,000"],
    ["Size of one entry", "the product as JSON", "about 2 KB"],
    ["Memory needed", "20,000 × 2 KB, plus overhead", "about 60 MB"],
    ["When full", "evict what was used least recently", "LRU"],
]) + '''<p>A cache that is too small evicts entries that would have been hits. The sign is a rising eviction count together with a falling hit ratio. A cache that is far too big only costs money, with one exception: very large single values, such as a 5 MB list under one key, slow every read of that key and are better split up.</p>''')

# ------------------------------------------------------------------ 7 layers
layers = '''
<p>Chapter 1 showed five places that hold a copy. Each is a cache with its own expiry, its own key and its own way of being wrong.</p>
''' + tbl(["Layer", "Shared by", "Who can clear it", "Typical risk"], [
    ["<b>Browser</b>", "one person", "nobody but that person", "you cannot take back what you allowed it to keep"],
    ["<b>CDN</b>", "everyone in a region", "you, with a purge call", "personal pages cached for all (drill 6)"],
    ["<b>App memory</b>", "one app instance", "a restart, or its own TTL", "two instances disagree; a refresh flips the price back and forth"],
    ["<b>Redis</b>", "all app instances", "your code", "the drills in chapter 4"],
    ["<b>Database</b>", "", "", "its own internal caches. Leave them to it"],
]) + mn("The further a cache is from the database, the less control you have over it. Give the far ones the shortest lives.") + '''
<h3>The staleness adds up</h3>
<p>Five minutes in Redis, five at the CDN and five in the browser is not five minutes. A copy can be read from Redis at the end of its life, stored by the CDN for five more, and then kept by the browser for five more.</p>
''' + tbl(["Layer", "TTL", "Worst-case age when the shopper sees it"], [
    ["Redis", "5 min", "5 min"],
    ["+ CDN", "5 min", "10 min"],
    ["+ browser", "5 min", "<b>15 min</b>"],
], hot=(2,)) + '''
<p>If the business said “one minute” in chapter 5, the three TTLs together must fit in one minute, or the outer layers must be invalidated as well.</p>
''' + full('''<h3>Speaking to the outer layers</h3>
<p>The browser and the CDN are controlled by response headers. A handful covers most needs.</p>
''' + tbl(["Header", "Meaning"], [
    ["<code>Cache-Control: max-age=60</code>", "anyone may keep this for 60 seconds"],
    ["<code>s-maxage=300</code>", "shared caches such as the CDN may keep it for 300; overrides max-age for them"],
    ["<code>stale-while-revalidate=30</code>", "after expiry, serve the old copy for up to 30 s more while fetching a new one"],
    ["<code>private</code>", "only the person's own browser may keep it; no shared cache"],
    ["<code>no-store</code>", "nobody keeps it. For anything personal or secret"],
    ["<code>ETag</code> with <code>If-None-Match</code>", "“has it changed since version abc?” The server answers 304 with no body if not"],
]) + '''<p>A good pattern for a product page: a short <code>max-age</code> for browsers, a longer <code>s-maxage</code> for the CDN, and a purge of the CDN when the price changes. The CDN is the outer layer you can clear, so let it hold the page longest, and give the browser, which you cannot clear, very little.</p>
<h3>Files that never change</h3>
<p>Scripts, styles and images are the easy case, if they are named by their content: <code>app.3f9a1c.js</code>. The file under that name never changes, so it can be cached for a year with <code>immutable</code>. A new build produces a new name. This is the versioned-key strategy from chapter 5, and it is the only kind of invalidation with no race in it.</p>
<h3>The cache inside the app</h3>
<p>A small in-memory cache in each app instance, in front of Redis, removes even the 1 ms network hop and protects Redis from a very hot key. Keep its TTL tiny, one to five seconds. Each instance expires on its own schedule, so for those seconds two instances can give different answers, and a shopper who refreshes may see the price change and change back.</p>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>A cache fails in two ways. Loudly, when it is down. And quietly, when it is up and serving the wrong thing, or serving very little. The quiet failures need graphs.</p>
''' + tbl(["Metric", "Healthy", "It means trouble when"], [
    ["<b>Hit ratio</b>, per kind of key", "steady, high for hot data", "it drops: keys changed, TTLs shortened, junk traffic (drill 5), or the cache is too small"],
    ["<b>Miss queries</b> reaching the database", "a small, steady stream", "spikes on a regular beat: stampedes (drill 2)"],
    ["<b>Evictions</b>", "few", "many, with a falling hit ratio: not enough memory"],
    ["<b>Stale serves</b> and refresh failures", "some stale serves, no failures", "refreshes failing: the cache is hiding a database problem"],
    ["<b>Cache response time</b>", "about a millisecond", "it rises: a huge value, a hot key, or the cache server is saturated"],
    ["<b>Age of served data</b>, where you can measure it", "within what was agreed", "older than the business said was acceptable"],
]) + mn("Split the hit ratio by key family. One overall number hides a broken family behind a healthy one.") + '''
<h3>Runbook: “customers still see the old price”</h3>
<ol class="keep">
  <li><b>Check the truth.</b> What does the database say? If it is wrong there, this is not a cache problem.</li>
  <li><b>Walk outward.</b> Read the key in Redis. Request the page from an app instance directly. Request it through the CDN and look at its <code>Age</code> header. The first layer that shows the old value is where the copy is stuck.</li>
  <li><b>Clear from the inside out.</b> Redis first, then the CDN. Clearing the CDN first only makes it refill from a stale Redis.</li>
  <li><b>Accept what you cannot clear.</b> Browsers keep their copy until it expires. That is why their TTL was short.</li>
  <li><b>Find the missed key.</b> Which copy was not invalidated, and why did the writer not know about it? That is the real fix (chapter 5).</li>
</ol>
''' + full('''<h3>Runbook: the cache is down or slow</h3>
<ol>
  <li><b>The app must not hang on it.</b> Cache calls have a short timeout, tens of milliseconds, and a circuit breaker. A slow cache is worse than no cache, exactly as in the Resilience Stack deep dive.</li>
  <li><b>Fall back with a limit.</b> On a cache failure the app reads the database, through the cap on miss queries from drill 3. Without the cap, the fallback is what takes the database down.</li>
  <li><b>Bring it back warm.</b> Run the warm-up script for the hottest keys before sending full traffic.</li>
</ol>
<h3>Hot keys and big keys</h3>
<p>Two shapes cause trouble at scale. A <b>hot key</b> takes a large share of all reads: the home page, or one product in a television advert. In a cache split over several servers, that one server gets the whole load. The cure is the tiny in-memory layer from chapter 7 for those keys. A <b>big key</b> holds megabytes: a whole category in one value. Every read moves all of it. Split it into pages, or cache ids and fetch the items separately.</p>
<h3>Flushing everything</h3>
<p>“Just flush the cache” fixes a stale-data incident and starts drill 3. If you must, do it by key family, one at a time, with the miss cap in place, at a quiet hour.</p>''')

# ------------------------------------------------------------------ 9 testing
testing = '''
<p>Cache bugs hide from ordinary tests, because a test usually reads once and writes once, and a cache only misbehaves on the second read, or when two things happen at once.</p>
''' + tbl(["Test", "How", "Catches"], [
    ["<b>Read after write</b>", "read, change the price, read again: the second read shows the new price", "a forgotten invalidation"],
    ["<b>Every copy</b>", "after a price change, read the product page, the category list and the search result", "derived keys nobody invalidates (chapter 5)"],
    ["<b>One rebuild</b>", "100 concurrent reads of a cold key: the database sees one query", "stampedes (drill 2)"],
    ["<b>Reader against writer</b>", "pause a reader between its database read and its cache write; run a write; resume", "the stale put-back (drill 1)"],
    ["<b>Not found</b>", "ask twice for a missing id: one database query", "drill 5"],
    ["<b>Two audiences</b>", "read as a trade customer, then as a guest", "keys missing a dimension (drill 6)"],
    ["<b>Cache off</b>", "run the whole test suite with the cache disabled", "code that only works because of what is cached"],
    ["<b>Cache down</b>", "make every cache call time out: pages still load, within the time limit", "a missing timeout or fallback"],
]) + mn("“Cache off” is the cheapest and finds the most. The app must be correct with no cache at all.") + code("product-cache.test.ts", "the stampede, as a test", '''
test("a cold hot key causes one database query", async () => {
  await cache.delete("product:42");
  db.resetQueryCount();

  await Promise.all(Array.from({ length: 100 }, () => getProduct("42")));

  expect(db.queryCount("products")).toBe(1);
});
''') + full('''<h3>Test with a cold cache under load</h3>
<p>Load tests are nearly always run warm, because the test has been running for a while by the time anyone looks. Add one run that starts with an empty cache at full traffic. It answers the question from chapter 2: is the cache optional or required? If the system does not recover by itself, you have found drill 3 on a quiet afternoon instead of during an upgrade.</p>
<h3>Make stale data visible</h3>
<p>In test and staging environments, have responses say where they came from: a header such as <code>X-Cache: hit, age=212</code>. The runbook in chapter 8 becomes a matter of reading headers, and testers can tell a caching bug from a data bug without asking a developer.</p>''')

# ------------------------------------------------------------------ 10 when not, lab, checklist
tools = '''
<h3>Before you add a cache</h3>
<p>A cache adds a second copy of the truth and every problem in this deep dive. Try the cheaper things first.</p>
''' + tbl(["Symptom", "Try first"], [
    ["one slow query", "an index, or a better query"],
    ["many reads, the database is busy", "a read replica"],
    ["an expensive sum or join, read often", "a materialised view or a summary table, updated on write"],
    ["the same data fetched many times in one request", "load it once per request"],
    ["still too slow or too frequent after those", "now a cache"],
]) + '''
<h3>What not to cache</h3>
''' + tbl(["Data", "Why not"], [
    ["anything a decision is made on: balance, stock at checkout, permissions being changed", "a stale value becomes a wrong action"],
    ["data read less often than it changes", "the bet from chapter 2 loses every time"],
    ["rarely read data", "hit ratio near zero (chapter 6)"],
    ["personal data, in a shared cache", "drill 6"],
    ["results that are cheap to compute", "the cache round trip costs more than the work"],
]) + mn("Permissions are the classic trap: revoke someone's access, and the cache keeps letting them in for five minutes.") + full('''<h3>Tools</h3>
''' + tbl(["Layer", "Examples", "Note"], [
    ["Shared cache", "Redis, Valkey, Memcached", "Redis and Valkey add data structures, locks and replication; Memcached is simpler"],
    ["In-process", "Caffeine (Java), an LRU map in most languages", "always bounded in size and with a TTL"],
    ["HTTP", "a CDN; a reverse proxy such as Varnish or nginx", "tags and purge calls differ by product"],
    ["Browser data", "TanStack Query, SWR", "the server-state cache note"],
])) + '''
<h3>Lab</h3>
<p>The “Mugs” category page lists 24 products with names, photos and prices. It is requested 300 times a second. Its query takes 400 ms. Prices change a few times a day and the business wants a change visible within one minute. Trade customers see different prices.</p>
<ol class="keep">
  <li>What is the cache key?</li>
  <li>How is the page invalidated when one mug's price changes?</li>
  <li>What TTLs do you set in Redis, at the CDN and in the browser?</li>
  <li>What happens when the key expires at 300 requests a second?</li>
  <li>A shopper adds a mug to the basket at the listed price. Where does the checkout get the price?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The key</summary><p><code>category:mugs:page:1:prices:retail</code>. It names the category, the page and the price list. Without the price list in the key, trade prices leak to everyone (drill 6). Better still, cache the list of product ids and names once, and the prices per price list separately.</p></details>
<details><summary>2 · Invalidation</summary><p>The writer of a price does not know which lists contain the product, so delete-on-write is not enough. Either tag the entry with the product ids it contains and invalidate by tag from an event worker, or rely on a short TTL. With “within one minute” as the requirement, a 30-second TTL alone is acceptable and much simpler.</p></details>
<details><summary>3 · TTLs</summary><p>They must add up to under a minute. For example Redis 20 s, CDN 20 s for the retail page, browser 10 s. The trade version is marked <code>private</code> and is not stored by the CDN at all. At 300 requests a second, a 20-second TTL still gives a hit ratio of 99.98 %.</p></details>
<details><summary>4 · Expiry under load</summary><p>Without protection, 400 ms × 300 a second is about 120 copies of the query at once. With single flight and a soft expiry, shoppers keep getting the old page for those 400 ms and exactly one query runs.</p></details>
<details><summary>5 · Checkout</summary><p>From the database, inside the transaction that creates the order. If it differs from what the page showed, the shopper is told before paying. The cached price was for display only.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Before caching", ["The slow query was fixed or indexed first", "Someone has said how stale this data may be", "No decision is made on the cached value; checkout and permissions read the source", "It is known whether the system can run without the cache"]),
    ("Keys and values", ["The key names everything the answer depends on", "Shared and personal data are cached separately", "Personal responses are private or no-store", "“Not found” is cached briefly; errors are never cached", "No single value is megabytes in size"]),
    ("Expiry and rebuild", ["Every key has a TTL with a random spread", "Hot keys use a soft expiry and one rebuild at a time", "TTLs across layers add up to less than the agreed staleness", "The browser gets the shortest TTL; static files have versioned names"]),
    ("Invalidation", ["Writes delete keys; they do not set them", "Every copy of the data is listed: item, lists, search, pages", "Invalidation is retried, through an outbox or the database's log", "Changes made outside the application also invalidate"]),
    ("Failure", ["Cache calls have a short timeout and a breaker", "Miss queries to the database are capped", "There is a warm-up script and a replica", "Nobody flushes everything during business hours"]),
    ("Tests and operations", ["The test suite passes with the cache switched off", "A test shows one database query for many concurrent misses", "A load test starts from an empty cache", "Hit ratio per key family, miss queries and evictions are on a dashboard", "Responses can say which layer served them and how old the copy is"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="caching", no=5, title="Caching",
    sub="A copy of the truth in five places: how stale each may be, how each finds out it is wrong, and what happens the day they are all empty.",
    summary="A deep dive on caching: the cache as a bet, read and write patterns, six failure drills, invalidation, TTL maths and stale-while-revalidate, browser, CDN and in-process layers, operations and testing.",
    builds_on="Vol. 1, note 17 and Vol. 2, note 06",
    builds_on_links=[("Cache-Aside", "../../distributed/notes/cache-aside.html"), ("Server-State Cache", "../../frontend/notes/server-state-cache.html")],
    notes=[("distributed", "cache-aside"), ("frontend", "server-state-cache")],
    facts=[("Example", "the product page for product 42, key <code>product:42</code>")],
    blurb="The cache as a bet, five read and write patterns, six failure drills, invalidation, TTL maths, the layers from browser to database.",
    chapters=[
        dict(id="recap", nav="Recap", title="Two notes in sixty seconds",
             gist="Cache-aside keeps a copy of hot data next to the database, with an expiry, and deletes it on a write. The server-state cache does the same in the browser. This deep dive is about what the copies do to the whole system: the database shrinks to fit, five layers expire at five different times, and some of them you cannot clear.",
             body=recap),
        dict(id="bet", nav="The bet", title="A cache is a bet",
             gist="Caching bets that an answer will be asked for again before it changes. Every cached item needs three decisions: how old it may be, how it learns it changed, and what a miss costs. The database feels the miss rate, not the hit ratio, and a system that cannot run without its cache has turned it into a database.",
             body=bet,
             check=[("The hit ratio improves from 98 % to 99 %. What happens to database load from reads?", "It halves: misses go from 2 % to 1 % of reads."),
                    ("How do you find out whether your cache is optional or required?", "Switch it off, or start it empty, under realistic load in a test environment, and see whether the database carries the traffic.")]),
        dict(id="patterns", nav="Patterns", title="Five ways to read and write",
             gist="Cache-aside and read-through load on a miss and leave the database as the truth. Write-through and write-behind send writes through the cache, and write-behind can lose confirmed data. Refresh-ahead reloads popular keys before they expire. For most data, use cache-aside and delete the key on a write.",
             body=patterns,
             check=[("Why does cache-aside delete the key on a write and not set the new value?", "Two writers can update the cache in a different order from the database, leaving the older value cached. A delete has no value to get wrong."),
                    ("Page-view counters are written through the cache and flushed every minute. What is the risk, and is it acceptable?", "A cache crash loses up to a minute of counts. For view counters that is usually fine; for orders it would not be.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six things that will happen: a reader puts an old value back after a write, hundreds of requests rebuild the same key at once, the cache restarts empty, a delete is lost, requests for things that do not exist bypass the cache, and a value is stored under a key that says too little.",
             body=drills,
             check=[("A key has no TTL “because we always delete on write”. Which drills make that dangerous?", "Drills 1 and 4. A stale put-back or a lost delete then stays wrong for ever, with nothing to correct it."),
                    ("After a cache restart the database is overloaded and the hit ratio stays near zero. Why does it not recover by itself?", "Queries time out under the load, so no results are written to the cache, so every read stays a miss.")]),
        dict(id="invalidation", nav="Invalidation", title="Invalidation: the hard problem",
             gist="One change has many copies: the item, the lists that contain it, search results, rendered pages. Combine five strategies: expiry, delete on write, events, versioned keys and tags. Agree with the business how stale each kind of data may be, and never make a decision on a cached value.",
             body=invalidation,
             check=[("The product page shows the new price and the category page shows the old one. What kind of key was missed?", "A derived key: a list that contains the product. The writer only invalidated the item's own key."),
                    ("Why can static files be cached for a year?", "Their names contain a version or content hash. A change produces a new name, so the old copy is never asked for again.")]),
        dict(id="numbers", nav="TTL & numbers", title="TTLs, worked out",
             gist="A key's hit ratio is about one minus one over its reads per TTL. Hot keys reach 99.9 % with a TTL of seconds, and cold keys gain nothing from any TTL. Use a soft expiry so stale values are served while one request refreshes, spread expiries randomly, and size the cache for the hot few.",
             body=numbers,
             check=[("A key is read 10 times a second with a 30-second TTL. Hit ratio?", "1 − 1/300, about 99.7 %."),
                    ("Product wants prices at most 10 seconds old. Does that ruin the hit ratio for popular products?", "No. At 80 reads a second a 10-second TTL still gives 99.9 %. It only costs anything on rarely read products, which were not benefiting anyway.")]),
        dict(id="layers", nav="Layers", title="The layers, from browser to database",
             gist="Browser, CDN, app memory and Redis each hold a copy with its own expiry. Their staleness adds up, so the TTLs together must fit what the business agreed. You can clear Redis and the CDN but not a browser, so the browser gets the shortest life. Files named by version can be cached for a year.",
             body=layers,
             check=[("Redis 60 s, CDN 60 s, browser 60 s. How old can the price on screen be?", "Up to three minutes."),
                    ("Two app instances each cache the price in memory for 5 seconds. What might a shopper notice?", "Refreshing the page can show the new price, then the old one again, as requests land on different instances.")]),
        dict(id="running", nav="Running it", title="Running it: graphs and runbooks",
             gist="Watch the hit ratio per key family, the miss queries reaching the database, evictions and refresh failures. For stale data, walk outward from the database to find the layer holding the old copy, and clear from the inside out. For a cache outage: short timeouts, a capped fallback, and a warm start.",
             body=running,
             check=[("Why clear Redis before the CDN?", "The CDN refills from the app. If Redis still holds the old value, the CDN caches the old page again."),
                    ("Miss queries spike every ten minutes exactly. What is happening?", "A hot key with a ten-minute TTL expires and many requests rebuild it together: a stampede.")]),
        dict(id="testing", nav="Testing", title="Testing a cache",
             gist="Cache bugs need a second read or two things at once. Test read-after-write for every copy of the data, one database query for many concurrent misses, and two audiences on the same key. Run the whole suite with the cache switched off, and run one load test from an empty cache.",
             body=testing,
             check=[("The suite fails with the cache switched off. What does that tell you?", "Some code depends on a cached value being there, for correctness. The cache has become a source of truth by accident."),
                    ("Why does a normal load test miss drill 3?", "By the time results are read, the cache is warm. Only a run that starts empty at full traffic shows whether the system can recover.")]),
        dict(id="tools", nav="When & lab", title="When not to cache, a lab and the checklist",
             gist="Fix the query, add a replica or build a summary table before adding a cache. Do not cache what decisions are made on, what is rarely read or what is personal in a shared cache. The lab designs caching for a category page with a one-minute freshness rule, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="Nishtala and others, “Scaling Memcache at Facebook” (2013), for leases, stampedes and cold clusters. Vattani, Chierichetti and Lowenstein, “Optimal Probabilistic Cache Stampede Prevention” (2015). Matt Brinkley and Jas Chhabra, “Caching challenges and strategies”, Amazon Builders' Library. RFC 9111, “HTTP Caching”, and RFC 5861 for stale-while-revalidate. Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, chapters 5 and 11, on derived data.",
)
