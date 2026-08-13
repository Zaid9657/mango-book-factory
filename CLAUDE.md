# Mango Book Factory — project brief

This repo is the single source of truth for the "Mango the Crocodile" KDP
children's book series: production pipeline, launch state, and finished books.

## Repo map

- `.claude/skills/mango-book-factory/` — production pipeline (story → Gemini
  illustrations → 24-page interior PDF → cover wrap). Start here for any
  "make the next book" request.
- `.claude/skills/mango-launch-playbook/` — everything after the PDFs exist:
  KDP metadata, KU, launch week, Day-30 market vote, German translation gate.
- `books/` — one folder per finished book (PDFs, manuscript, parent note,
  scene prompts). **This is the ground truth for which books exist** — the
  factory's Step 0 scans it to pick the next book.
- `LAUNCH_TRACKER.md` — single source of truth for launch state. Read it at
  the start of any launch work, update it before finishing. (The old OneDrive
  copy at `C:\Users\zaid1\OneDrive\Desktop\Mango Books\LAUNCH_TRACKER.md` is
  legacy — this file wins.)
- `fonts/Baloo2.ttf` — the title font (variable; use the ExtraBold variation
  for covers: `font.set_variation_by_name("ExtraBold")` in PIL). OFL licensed.
- `requirements.txt` — installed automatically by the SessionStart hook.

## Secrets

The Gemini API key lives ONLY in
`.claude/skills/mango-book-factory/assets/gemini_key.txt` (gitignored) or the
`GEMINI_API_KEY` env var. Never commit it. If it's missing in a fresh session,
ask Zaid to provide it — see `gemini_key.txt.example`.

## Hard-won environment notes (do not rediscover)

- `pip install -r requirements.txt --break-system-packages` (the SessionStart
  hook does this already).
- ReportLab `Frame.addFromList` silently drops text that doesn't fit — make
  frames generous and always render-check pages with `pdftoppm`.
- KDP interior must NOT contain the cover; the cover is a separate wrap file.
- Spine width = pages × 0.002347" (premium color). 24 pages → 0.0563".
- Book spec: paperback, 8.5×8.5", 24 pages, premium color, white paper, bleed ON.

## Working rules

- Never improvise the pipeline — the skills hold the locked process.
- After finishing a book, commit its `books/NN-slug/` folder and update
  `LAUNCH_TRACKER.md` in the same change.
