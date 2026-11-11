# Margin Notes

A student's illustrated notebook on distributed design patterns. Static site in `public/`, deployed with Cloudflare Workers static assets (`wrangler.jsonc`).

- `public/index.html`: cover and contents
- `public/notes/*.html`: one note per pattern (problem, analogy, doodles, how it works, gains vs losses, nine ratings, pitfalls, when to use, quiz)
- `public/all.html`: every note on one page for "Export as PDF" (`all.html?print` opens the print dialog)
- `public/pdf/`: ready-made PDFs. Rebuild after editing a note with `node scripts/build-pdf.mjs` (needs Playwright + Chromium)

To add a note: copy a file in `public/notes/`, add it to the contents in `index.html`, to `data-collect` and the contents in `all.html`, and to the jobs in `scripts/build-pdf.mjs`.

## Publishing (GitHub Pages)

`.github/workflows/pages.yml` runs on every push to `main` (and to the current working branch). It installs Playwright, rebuilds the PDFs, checks every page exists, and deploys `public/` to GitHub Pages. You can also run it by hand from the Actions tab ("Run workflow").

One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

Live site: https://jepzman.github.io/oni-alien/
