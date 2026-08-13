---
name: mango-book-factory
description: Produce a complete, KDP-ready "Mango the Crocodile" children's picture book end to end — story, AI illustrations via Gemini, 24-page interior PDF, and full cover wrap. Use this skill whenever Zaid says "make the next Mango book", "book factory", "run the daily book", "produce book N", "Mango book on [topic]", or any request to draft, illustrate, or assemble a book in the Mango series. Also trigger when a scheduled routine asks to produce the day's book. Always use this skill for Mango series work — never improvise the pipeline from scratch.
---

# Mango Book Factory

Produces one finished book per run: story → images → interior PDF → cover wrap PDF. Book 1 ("Mango and the Busy Brain") shipped already; the series plan in `references/series_plan.md` defines books 2–13.

## The character (never deviate)

Mango: small, round, cute baby crocodile — chubby body, stubby legs, big round head, huge friendly brown eyes, mint-green skin, soft pale belly, one tiny snaggle-tooth, a row of bumps along the back that **change color with feelings** (calm = soft green, worried = yellow, sad/embarrassed = gray, angry = red-orange, proud/excited = bright green; each new book may add its feeling's color per the series plan). Supporting cast: **Gogo** the wise old turtle (calm, never rushes), **Mr. Heron** the teacher. World: warm sunny riverbank, lily pads, dragonflies.

## Workflow (run in this order)

### Step 0 — Which book?
Read `references/series_plan.md`. Determine the next book **by checking the repo's `books/` directory** — a book is done if its `books/NN-slug/` folder exists (with an `*_INTERIOR.pdf` or a shipped-marker note). Produce the first book in the plan that has no folder yet. Books marked ✅ SHIPPED in the plan are always treated as done even if no PDF is found. If Zaid names a specific book or topic in his message, that overrides the automatic choice. State which book you're producing in one line, then go — do not ask for confirmation on scheduled runs.

### Step 1 — Draft the story
Write the story yourself (no external model call). Spec:
- Ages 6–9, read-alone or read-together. **1,200–1,400 words** before page-splitting.
- Arc (mandatory): happy opening → the feeling's trigger → back-ridge color changes → Mango struggles → **a failed first attempt** (trying the "obvious" fix makes it worse) → Gogo reframes with one sticky line (see plan for each book's line) → Mango applies it under real pressure → earned win, back-ridge glows → quiet night reflection → closing message "For every kid who…".
- Never preachy. Show, don't lecture. Gogo gets ONE memorable line per book, like book 1's "Don't trap it — aim it."
- End matter text: write the 2-page "A Note for Parents" from a child & adolescent psychiatrist's perspective for this book's topic: what the feeling is, why the intuitive parental response backfires, 4 concrete home strategies, and a calm "when to seek support" paragraph. Same warm, non-clinical register as book 1.

### Step 2 — Quality pass (self-review before images)
Check: failed-attempt beat present? Gogo line sticky and short? No psychiatric jargon in the story? Color logic consistent with the chart? Word count in range? Fix before proceeding.

### Step 3 — Generate the 7 illustrations (fully automated)
- The script `scripts/gen_images.py` calls Gemini (`gemini-3-pro-image`). The Mango reference image AND the API key are bundled in `assets/` (`mango_reference.jpg`, `gemini_key.txt`) — nothing to ask Zaid for. If the key file errors (quota/invalid), tell Zaid to update `assets/gemini_key.txt` and stop.
- Edit the SCENES list in the script to this book's 7 beats (opening / trigger / low point / Gogo talk / failed attempt / the win / calm night), each specifying the back-ridge color. Style prefix stays fixed; **no text or signs in images**.
- Run it, then **Claude performs the QC itself — do not ask Zaid**: `view` every generated image and check (a) Mango on-model: mint-green, round, snaggle-tooth, ridge bumps present; (b) ridge color matches the scene's emotion; (c) no text/signs/watermarks; (d) no anatomical glitches (extra limbs, fused faces); (e) scene matches its beat. Regenerate any failing image (tweak the prompt if needed), max 2 retries each; if one still fails, use the best attempt and note it in the delivery message.

### Step 4 — Build interior (24 pages)
Run `scripts/build_interior.py` after editing its STORY list (7 text blocks, split from the draft) and back-matter strings (parent note, this book's color chart row if new, activity page themed to this book's skill). Layout is locked: title page, dedication/copyright, 7 × (full-page image + facing text page), closing message, 2-page parent note, feeling-colors chart, activity, series teaser, "this book belongs to", blank — exactly 24 pages. Verify by rendering 2–3 pages with `pdftoppm` before presenting.

### Step 5 — Build cover wrap
- Create the titled front cover: take this book's strongest image (or a dedicated cover render), composite the title in Baloo 2 (bundled at `fonts/Baloo2.ttf` in the repo — no download needed), cream fill + dark-green outline, placed in empty sky area — **never a white box**.
- Run `scripts/build_cover.py` after setting TITLE, blurb hook line, and blurb body. Geometry is locked for 8.5×8.5", 24 pages, premium color (spine 0.0563"); includes barcode safe zone.

### Step 6 — Deliver
Present both PDFs (`*_INTERIOR.pdf`, `*_COVER.pdf`) with a one-line KDP reminder: paperback, 8.5×8.5, premium color, white paper, bleed ON. Then archive the book in the repo: commit a `books/NN-slug/` folder containing both PDFs, `manuscript.md`, `parent_note.md`, and `scene_prompts.md` (see `books/README.md`), and tell Zaid which book is next in the plan.

## Environment notes (hard-won, do not rediscover)
- This container has network access: Gemini API calls run here directly. `pip install google-genai pillow reportlab --break-system-packages`.
- On Zaid's Windows machine (fallback): use `py -m pip`, and `$env:GEMINI_API_KEY="..."` (session-scoped).
- ReportLab Frame.addFromList silently drops text that doesn't fit — make frames generous and always render-check pages.
- KDP interior must NOT contain the cover. Cover is a separate wrap file.
- If page count or paper type ever changes, recompute spine: pages × 0.002347" (premium color).

## Communication rules for this pipeline
Answer first, keep it short, one question at a time, no strategy detours unless asked. The only approval gate is Step 0 (book choice) — and if the run comes from a scheduled routine that names the book (or says "next"), skip even that and just produce. Everything else: execute and deliver both PDFs.
