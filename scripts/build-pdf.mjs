// Builds the ready-made PDFs (public/<key>/pdf/) using the site's own print stylesheet.
// Usage: npm run pdf            render only the PDFs whose page changed since the last build
//        npm run pdf -- --all   render every PDF
//
// Incremental builds: each PDF has a fingerprint (a hash of its page's HTML and the local CSS/JS/images it loads; a
// whole-journal PDF also hashes every note it collects). Rendered PDFs and their fingerprints are kept in
// .pdf-cache/ (the deploy workflow restores and saves it with actions/cache). A PDF whose fingerprint matches the
// cache is copied from there instead of rendered again. Changing this script or the Playwright version changes every
// fingerprint, so everything is rebuilt.
//
// Environment: PDF_FORCE=1 (same as --all) · PDF_JOURNALS=key,key (only these journals; the cache isn't pruned)
//              CHROMIUM_PATH=/path/to/chromium (use an installed browser instead of Playwright's own)
import { createServer } from 'node:http';
import { createHash } from 'node:crypto';
import { readFile, writeFile, mkdir, copyFile, rm, readdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { dirname, extname, join, normalize, posix } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = fileURLToPath(new URL('../public/', import.meta.url));
const cacheDir = fileURLToPath(new URL('../.pdf-cache/', import.meta.url));
const manifestPath = join(cacheDir, 'manifest.json');
const force = process.argv.includes('--all') || process.env.PDF_FORCE === '1';
const only = (process.env.PDF_JOURNALS || '').split(',').map((s) => s.trim()).filter(Boolean);
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.pdf': 'application/pdf',
                '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.json': 'application/json' };

// ---------------------------------------------------------------- fingerprints
const recipe = createHash('sha256')
  .update(await readFile(fileURLToPath(import.meta.url)))
  .update(require('playwright/package.json').version)
  .digest('hex');

const fileHashes = new Map();
async function hashFile(rel) {
  if (!fileHashes.has(rel)) {
    fileHashes.set(rel, readFile(join(root, rel)).then((b) => createHash('sha256').update(b).digest('hex')).catch(() => 'missing'));
  }
  return fileHashes.get(rel);
}

// The page itself plus every local stylesheet, script and image it references (not links to other pages).
async function pageFingerprint(rel) {
  const html = await readFile(join(root, rel), 'utf8');
  const parts = [rel, await hashFile(rel)];
  const refs = new Set();
  for (const m of html.matchAll(/(?:href|src)="([^"#]+)"/g)) {
    const ref = m[1].split('?')[0];
    if (/^(?:[a-z]+:|\/\/|data:)/i.test(ref) || ref.endsWith('.html') || ref.endsWith('/') || ref.endsWith('.pdf')) continue;
    refs.add(posix.normalize(posix.join(posix.dirname(rel), ref)));
  }
  for (const ref of [...refs].sort()) parts.push(ref, await hashFile(ref));
  return parts.join('\n');
}

async function fingerprint(pages) {
  const h = createHash('sha256').update(recipe);
  for (const p of pages) h.update(await pageFingerprint(p));
  return h.digest('hex');
}

// ---------------------------------------------------------------- the jobs
// One PDF per note plus one per journal, from public/journals.json (written by scripts/build_notes.py).
const journals = JSON.parse(await readFile(join(root, 'journals.json'), 'utf8'))
  .filter((j) => !only.length || only.includes(j.key));
const jobs = [];
for (const j of journals) {
  for (const n of j.notes) jobs.push({ url: n.page, out: n.pdf, expect: 0, pages: [n.page] });
  // the whole-journal page collects every note in the browser, so its PDF changes when any note does
  jobs.push({ url: j.all, out: j.pdf, expect: j.notes.length, pages: [j.all, ...j.notes.map((n) => n.page)] });
}

const manifest = existsSync(manifestPath) ? JSON.parse(await readFile(manifestPath, 'utf8')) : {};
for (const job of jobs) job.fp = await fingerprint(job.pages);
const todo = jobs.filter((job) => force || manifest[job.out] !== job.fp || !existsSync(join(cacheDir, job.out)));
const reuse = jobs.filter((job) => !todo.includes(job));

// ---------------------------------------------------------------- copy what's unchanged
for (const job of reuse) {
  await mkdir(dirname(join(root, job.out)), { recursive: true });
  await copyFile(join(cacheDir, job.out), join(root, job.out));
}
console.log(`PDFs: ${reuse.length} unchanged (from the cache), ${todo.length} to render${force ? ' (forced)' : ''}`);

// ---------------------------------------------------------------- render what changed
if (todo.length) {
  const server = createServer(async (req, res) => {
    const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
    try {
      const body = await readFile(join(root, path || 'index.html'));
      res.writeHead(200, { 'content-type': types[extname(path)] || 'application/octet-stream' });
      res.end(body);
    } catch { res.writeHead(404); res.end(); }
  });
  await new Promise((ok) => server.listen(0, ok));
  const base = `http://localhost:${server.address().port}/`;
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  let done = 0;
  for (const job of todo) {
    const page = await browser.newPage({ colorScheme: 'light' });
    await page.goto(base + job.url, { waitUntil: 'networkidle' });
    if (job.expect) await page.waitForFunction((n) => document.querySelectorAll('article.sheet').length >= n, job.expect, { timeout: 90000 });
    await page.evaluate(async () => {
      await document.fonts.ready;
      document.querySelectorAll('.quiz details').forEach((d) => { d.open = true; });
    });
    await page.emulateMedia({ media: 'print' });
    await mkdir(dirname(join(root, job.out)), { recursive: true });
    await page.pdf({ path: join(root, job.out), format: 'A4', printBackground: true, preferCSSPageSize: true });
    await page.close();
    // keep a copy and its fingerprint for the next build
    await mkdir(dirname(join(cacheDir, job.out)), { recursive: true });
    await copyFile(join(root, job.out), join(cacheDir, job.out));
    manifest[job.out] = job.fp;
    console.log(`wrote ${job.out} (${++done}/${todo.length})`);
  }
  await browser.close();
  server.close();
}

// ---------------------------------------------------------------- tidy the cache
// Drop PDFs that no longer belong to any page (only on a full run, so a filtered run can't empty the cache).
if (!only.length) {
  const keep = new Set(jobs.map((job) => job.out));
  for (const out of Object.keys(manifest)) {
    if (!keep.has(out)) {
      delete manifest[out];
      await rm(join(cacheDir, out), { force: true });
    }
  }
}
await mkdir(cacheDir, { recursive: true });
await writeFile(manifestPath, JSON.stringify(Object.fromEntries(Object.entries(manifest).sort()), null, 1) + '\n');
