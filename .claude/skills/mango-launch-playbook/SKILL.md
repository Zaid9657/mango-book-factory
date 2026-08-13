---
name: mango-launch-playbook
description: Run the locked launch-and-growth process for every "Mango the Crocodile" book on Amazon KDP — metadata (search-query subtitles, categories, keywords), Kindle Unlimited setup, launch-week checklist with extension prompts, free-promo-day scheduling, the Day-30 market-vote check, and the winners-only German translation gate. ALWAYS use this skill whenever Zaid says "launch book N", "publish the next Mango book to KDP", "run the launch checklist", "day-30 check", "which books are winners", "should we translate this one", "write the KDP metadata", or any question about Mango marketing, reviews, categories, keywords, KU, free days, or German editions. Production of the book itself belongs to mango-book-factory; everything AFTER the PDFs exist belongs here. Never improvise launch steps from scratch — this skill holds the verified formula.
---

# Mango Launch Playbook

The locked, evidence-based launch process for the Mango the Crocodile series.
Built July 2026 from verified analysis of fast-winning indie SEL authors
(new books cracking category top-20 with 5–22 ratings, zero ad spend).

**North star: let the market vote across the series; concentrate translations,
collections, and any future ad budget on the 2–3 proven winners only.**

## The verified formula (never deviate without new evidence)

Search-query title → Kindle Unlimited → small-category #1 New Release badge →
free-promo newsletters for day-1 downloads → 3–5 fast reviews in launch week →
Day-30 market vote → double down on winners → translate winners to German.

Why each link works:
- Amazon boosts new titles for ~30 days (the "honeymoon"); a handful of early
  borrows/reviews inside that window outranks hundreds of late ones.
- Parents search problems, not authors. A subtitle that IS the search phrase
  ranks organically on long-tail terms with zero ads.
- KU borrows count toward rank and remove the price/trust barrier for an
  unknown author. Every winner analyzed was in KDP Select.
- Small subcategories hand out #1 New Release badges for a few launch-week
  sales; the orange badge then drives real clicks.
- Translation of a proven winner beats a new book: one analyzed author earns
  ~$2k/mo from 3 books (one concept, three languages) — the same as another
  earns from 27.

## State: the tracker file

All launch state lives in `LAUNCH_TRACKER.md` at the repo root of
`mango-book-factory` (create from `assets/launch_tracker_template.md` if
missing). Every session reads it first and commits an update before finishing.
Never rely on session memory. (The old copy at
`C:\Users\zaid1\OneDrive\Desktop\Mango Books\LAUNCH_TRACKER.md` is legacy —
the repo file wins.)

## Workflow 1 — Launch a book (run per book, weekly cadence)

Precondition: the book folder exists with interior PDF, cover PDF, and
KDP_paste_sheet.md (produced by mango-book-factory).

### Step 1: Metadata (generate, then hand to Zaid)
- **Subtitle** = exact parent search phrase + age + credential:
  "A Children's Book About [Problem] and [Skill] for Kids Ages 6–9 —
  by a Child Psychiatrist". The title is the traffic source.
- **Series**: "Mango the Crocodile" (KDP series page; every book joins it).
- **7 backend keywords**: long-tail variations of the subtitle phrase only.
  Never broad head terms ("kids emotions book", "children's feelings").
- **Categories**: 2 small subcategories + 1 medium. A subcategory is "small
  enough" when its current #1 New Release has fewer than ~20 ratings (check
  via a browser-extension prompt on the category's New Releases page).
- **Description**: benefit-led, opens with the parent's problem as a question,
  3–5 "Why parents love this book" bullets, credential paragraph near the end.
- Read `references/metadata_patterns.md` for the full templates and the
  extension prompt library before writing.

### Step 2: Formats
- Paperback $12.99 AND Kindle edition $3.99.
- Kindle MUST be enrolled in KDP Select (→ Kindle Unlimited). Non-negotiable;
  KU is the ranking engine.

### Step 3: Launch week checklist (give Zaid the dated checklist)
- Day 1: publish both formats together.
- Day 2–3: schedule 2 of the 5 KDP Select free days; submit the free promo to
  free-ebook newsletter sites (OHFB and similar free-listing sites).
- Day 1–7: 3–5 people from Zaid's network buy or borrow and review. Target:
  first review live by day 5–7. Speed beats volume inside the honeymoon.
- Log launch date and actions in LAUNCH_TRACKER.md.

## Workflow 2 — Day-30 market vote (run when any book hits day 30)

For each book at day 30+, record in LAUNCH_TRACKER.md: Kindle BSR, paperback
BSR, rating count, average stars (collected via a read-only extension prompt
on the product pages).

Verdicts (the number decides — no judgment calls, no rescue attempts):
- **WINNER**: Kindle BSR under ~50,000 → queue German edition, A+ Content,
  future collection/ads.
- **UNDECIDED**: between 50k and ~300k → wait 30 more days, no investment.
- **DONE**: drifting past ~300,000 → stop investing. It stays on the shelf
  (cross-sell + page-reads) but gets nothing more. Do not polish losers.

## Workflow 3 — German line (winners only)

Gate: a book must be a WINNER in English before any German work starts.
Then: mango-book-factory produces "Mango das Krokodil" from the same
illustrations; German search-query subtitle (same formula, German phrases);
launch on amazon.de with the identical Workflow-1 sequence. The German SEL
shelf is thinner — same effort, less competition.

## Workflow 4 — Monthly trend scan (optional accelerator)

Once a month, scan TikTok Shop / BookTok kids-book hashtags for a topic
spiking (the "Murphy's Law for kids" pattern: TikTok manufactures demand,
spillover lands as Amazon search within weeks, copycats swarm, window closes).
If a rising topic fits Mango's world, it jumps the production queue —
the factory can ship in days, faster than any competitor.

## Do-not list (each rule paid for with someone's money)

- No Amazon ads until a book has 10+ ratings.
- No broad keywords; never fight incumbents (e.g. "A Little SPOT") on head terms.
- No polishing losers after the market votes.
- No simultaneous multi-book dumps — each book needs its own honeymoon.
- No skipping KDP Select enrollment.

## Division of labor

Claude generates: metadata packs, extension prompts, checklists, tracker
updates, verdicts, German queue. Zaid does by hand: all KDP clicks (publish,
free days, Select enrollment), newsletter submissions, reviewer pings.
Always tell Zaid explicitly which is which, in order.
