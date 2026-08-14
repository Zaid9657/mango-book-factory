---
name: mango-launch-playbook
description: Run the launch-and-growth process for every "Mango the Crocodile" book on Amazon KDP — metadata (search-query subtitles, categories, keywords), listing conversion (interior images, A+ Content, pricing, hardcover), the €5/day Amazon Ads demand test, KDP compliance checks, the paperback-units decision gate, and the MedMeister-audience German play. ALWAYS use this skill whenever Zaid says "launch book N", "publish the next Mango book to KDP", "run the launch checklist", "day-30 check" / "decision gate", "which books are winners", "should we translate this one", "write the KDP metadata", or any question about Mango marketing, reviews, categories, keywords, KU, ads, or German editions. Production of the book itself belongs to mango-book-factory; everything AFTER the PDFs exist belongs here. Never improvise launch steps from scratch.
---

# Mango Launch Playbook

Rebuilt 2026-08-13 after an investor-grade audit (`AUDIT-2026-08-13.md` at the
repo root) falsified several parts of the original "verified formula". Treat
this version as the working hypothesis, not gospel — every rule here is
downstream of the audit's evidence, and the decision gate exists precisely so
the market can overrule it.

**North star: one real demand channel pointed at two conversion-ready
listings, then a hard KILL/SCALE decision on 2026-10-15. Print royalties are
the business; everything else is instrumentation.**

## State: the tracker file

All launch state lives in `LAUNCH_TRACKER.md` at the repo root. Every session
reads it first and commits an update before finishing. **Reconcile against KDP
ground truth before any decision** — the audit found the tracker wrong on
almost every material point (wrong book live, unknown Kindle/KU status,
unrecorded sales). When Zaid reports KDP numbers, log them with the date.
Weekly KDP→tracker sync is part of any launch session.

## Compliance first (highest expected value in the playbook)

- **AI-content disclosure**: KDP requires disclosing AI-generated text and
  images at title setup. Verify it is answered accurately for every title
  before anything else. An inaccurate disclosure risks account-level
  termination — asymmetrically expensive versus anything Mango can earn.
  Current truth (2026-08-14): books 1–2 text is human-written (Zaid's
  attestation) — disclose **images only** (Gemini). Any future
  factory-produced book is Claude-drafted — disclose **"Yes, entire work"**
  for text as well. These two patterns must never be mixed up.
- **Reviews: genuine only.** Never solicit reviews from friends, family, or
  anyone with a material connection — regardless of verified-purchase status.
  This replaces the old "3–5 network reviews in launch week" step, which was
  Amazon review abuse and the single most account-endangering line in the old
  playbook. Legitimate paths: more buyers (ads), a review request line in the
  back matter, Author Central following.
- **Credential claim**: resolved 2026-08-14 — Zaid IS a child & adolescent
  psychiatrist and the author, so the one true claim, used verbatim
  everywhere (subtitle, description, cover, back cover, Author Central), is
  **"by a Child Psychiatrist"** (long form: "Dr. Zaid Alzureiqat — Child &
  Adolescent Psychiatrist"). Never "with the guidance of" — that was Book 1's
  back-cover error. Medical disclaimer in the front matter of every book.
- If ANY KDP notification arrives about AI content, quality, or review abuse:
  stop all Mango activity and protect the account. Do not appeal-and-continue.

## Workflow 1 — Make a listing conversion-ready (precondition for any traffic)

A listing that cannot convert makes every ad euro worthless. Checklist per book:

1. **Metadata**
   - Subtitle = exact parent search phrase + age band + credential:
     "A Children's Book About [Problem] and [Skill] for Kids Ages **4–8**…".
     Long-tail subtitles demonstrably rank (Book 1: #14 organic for
     "children's book about paying attention") — keep this.
   - **Series field**: every book in the "Mango the Crocodile" series with its
     number in the title field ("Mango the Crocodile N"). Numbering reality
     (2026-08-14): Book 1 = series #1, Red-Hot Back = series #3 with a
     permanent gap at #2 (Zaid's decision — reserved for the unmade Worry
     Cloud). The series widget shows "Book 1 of 1" until #2 is filled;
     accepted cost. Any future book must claim its number in BOTH the KDP
     series page and the title text before the 72h lock (below).
   - **Always click "Publish series" after any series edit.** KDP stages
     series changes behind a "your series has changes that have not been
     published" banner and they do nothing until published — this silently
     killed the cross-sell on both live books until 2026-08-14 (Book 1 read
     "Book 1 of 1", Book 2 showed no widget at all). The series has its own
     review state, separate from the books. Verify the banner clears.
   - **72-hour lock**: paperback title, subtitle, and author name become
     permanently uneditable ~72h after publish. Verify all three — and the
     series number in the title text — within the first day of publishing.
     Kindle fields stay editable; live-paperback fixes are limited to series
     field, reading age, categories, keywords, and description.
   - 7 backend keywords: long-tail variations only, never head terms.
   - **Categories**: must include an ADHD / Special Needs / Disability node
     where topical (use KDP's category request tool), plus Emotions &
     Feelings. Never Self-Esteem (owned by evergreen trade classics).
   - Description: benefit-led, opens with the parent's problem as a question,
     3–5 "why parents love it" bullets, credential paragraph near the end.
   - Templates: `references/metadata_patterns.md`.
2. **Listing assets**
   - 5–7 interior spread images uploaded to the listing. A parent will not buy
     an illustrated book they cannot see inside.
   - A+ Content: series banner, the color-chart mechanic, the credential.
   - Author name + "Dr." + series number ON the cover (factory revises).
3. **Formats & pricing**
   - Paperback **$9.99–$10.99** (audit: $12.99 was the most expensive
     per-page item in the category; competitors' hardcovers sell at $6–12;
     nearest direct competitor $9.99). Verify actual print cost first — if
     it exceeds ~$3.50, flag to Zaid before pricing.
   - **Hardcover $17.99–$19.99** — the format gift buyers and
     schools/counselors actually buy.
   - Kindle $3.99, **fixed-layout** (not reflowable — reflowable picture
     books render as text blocks and cap KENP at ~10–20 pages).
   - KDP Select/KU: keep enrollment, but treat KU as **discovery only** — a
     full read pays ≈$0.05. Never a revenue line, never the decision metric.

## Workflow 2 — The demand test (the actual experiment)

The audit's core finding: nothing was ever wrong with Book 1's launch —
**no launch was ever run**, so there is no demand data at all. The test:

- Amazon Ads, **€5/day**, exact-match keywords (ADHD, focus, anger, big
  feelings phrases), pointed at the **paperback**, both live books, 60 days,
  ~€300 budget.
- One honest email to the MedMeister physician list (see Workflow 3).
- No free-ebook newsletter promos — that's an adult-fiction mechanic
  (free download → binge → buy next); picture books are bought in print,
  as gifts, by adults, and a free ebook converts to ~nothing. (Removed from
  the old playbook.)
- Weekly during the test: log impressions, CTR, ACOS, paperback units, and
  royalties in the tracker.
- Early abort signal: >10,000 impressions at <0.2% CTR = the cover/price
  can't compete for attention — that's a KILL trigger, not an optimization
  target.

## Workflow 3 — The MedMeister audience (unused distribution asset)

MedMeister's list is German physicians: disproportionately parents of young
children, instantly able to validate the credential, and exactly who
paediatricians ask for book recommendations. One honest email costs nothing
and outweighs every promo newsletter. This also inverts the old German gate:
**German is where the audience already is** — an audience play now, not a
translation prize for English winners. Caveats: German buyers are the least
AI-tolerant picture-book market and the shelf is owned by Carlsen/Loewe/
Oetinger — sell on the clinician credential, not the art. Any German edition
still requires Zaid's explicit go.

## Workflow 4 — Decision gate (2026-10-15, no judgment calls)

Decision metrics: **paperback units/month and royalty/month.** Never Kindle
BSR — it conflates $0.05 borrows with sales and ignores print, where ~100% of
revenue is. (The old WINNER/UNDECIDED/DONE BSR thresholds are retired: <50k
was a top-percentile bar mislabeled as a pass, >300k described every new indie
book, and the range between had no rule.)

The KILL / immediate-KILL / SCALE criteria live in `LAUNCH_TRACKER.md` and are
binding. If SCALE is hit, the frozen backlog in the factory's series plan
reopens; otherwise archive the listings, keep the pipeline as a proven
capability, and return the hours to MedMeister.

## Do-not list

- No producing new books while the tracker says FROZEN.
- No review solicitation from anyone you know. Ever.
- No free-ebook newsletter promos.
- No head-term keywords; never fight incumbents (e.g. "A Little SPOT").
- No polishing losers after the gate decides.
- No German translation without Zaid's explicit go (audience email ≠ edition).
- No trusting this tracker without a KDP reconciliation date on it.

## Division of labor

Claude generates: metadata packs, A+ Content drafts, ad keyword lists,
descriptions, checklists, tracker updates, gate verdicts. Zaid does by hand:
all KDP clicks (disclosure check, series linking, pricing, hardcover setup,
category requests, image uploads, ads console), Author Central, the
MedMeister email send. Always tell Zaid explicitly which is which, in order.
