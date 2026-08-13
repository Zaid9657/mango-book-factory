# Mango Launch Tracker

**Single source of truth for launch state.** Every session reads this first and
commits an update before finishing. Reconcile against KDP before any launch
decision — the 2026-08-13 audit (`AUDIT-2026-08-13.md`) found this file wrong
on almost every material point, and every decision downstream of it was noise.

**PRODUCTION IS FROZEN.** No new books until one live title hits the SCALE bar
below. The 13-book plan is dead as a default; the backlog survives only as a
contingency for a proven winner.

Figures verified 2026-08-14 by a read-only browser session inside KDP
(Phase 1–2 of the fix run), except where marked BLOCKED.

## Live books

| # | Book | Feeling | Paperback | Kindle | KU | Price (pb/Kindle) | Lifetime sales | KENP | Reviews | BSR |
|---|------|---------|-----------|--------|----|--------------------|----------------|------|---------|-----|
| 1 | Mango and the Busy Brain | attention/ADHD | live Jul 15 (pub date Jul 6) — ASIN B0H9166W5V, KDP GXGJMBQB50Z, ISBN 979-8181331785 | live Jul 14 — ASIN B0H8TWCK3R, KDP A2LJ9IWTTI63H6 | yes | $12.99 / $3.99 | 1 paperback (Jul, amazon.de, €3.64 royalty) | 0 | 1× 5.0★ DE Jul 26 — likely personal contact; never repeat | none |
| 2 | Mango and the Red-Hot Back | anger | live Jul 26 — ASIN B0HBN42QLB, KDP G9KYC9F4WG4, ISBN 979-8185934852 | live Aug 3 — ASIN B0HCP1C8TF, KDP A1NY4R54K15TVN | yes | $12.99 / $3.99 | 0 | 0 | 0 | none |

**Per-unit economics (verified):** Kindle $3.99 on 70% plan → $2.70/unit
(amazon.com) / €2.18 (amazon.de). Paperback royalty & print cost: **BLOCKED**
— the print-setup app requires a fresh password sign-in (Zaid). Only observed
data point: the one amazon.de sale paid €3.64 net. Lifetime total revenue:
**€3.64**. KENPC: not surfaced anywhere (Promotion Manager errors; 0 KENP
lifetime, both books). Promotions/free days: none ever. Ads: none visible in
KDP (Ads console unchecked).

## Unpublished

| Book | Status |
|------|--------|
| Mango and the Wiggly Wait (patience) | Coverless paperback draft, KDP 6BRVGEHGNTB, untouched since Jul 6; no Kindle format. Disclosure state unreadable until print-app sign-in. Parked until SCALE. |
| Mango and the Worry Cloud (anxiety) | Never published. Its reserved series slot (#2) stays empty per Zaid's 2026-08-14 decision. Locate manuscript or write off. |

## Decisions locked 2026-08-14 (Zaid, via Q&A)

1. **Credential**: Zaid is a **child & adolescent psychiatrist** and the
   author. The claim "by a Child Psychiatrist" is true and is used verbatim
   everywhere. Book 1's back cover ("with the guidance of…") is the WRONG
   wording — fix in any future cover revision; never reuse.
2. **AI disclosure (live books)**: Zaid attests the TEXT of books 1–2 was
   written by him personally, without AI — **only the illustrations are
   AI-generated** (Gemini). Both Kindle disclosures get aligned to: master
   answer Yes (images), Images = "Many AI-generated images, minimal or no
   editing" (Gemini), Texts = none/not AI. Recorded here as Zaid's
   attestation of authorship. ⚠️ **Future factory-produced books are
   Claude-drafted — their text disclosure MUST be "Yes, entire work". Never
   copy books 1–2's pattern forward.**
3. **Series numbering**: Book 2 keeps series number **3** (gap at #2 for the
   unmade Worry Cloud). Accepted consequence: Amazon's series widget stays
   broken ("Book 1 of 1") until a book occupies #2 — which is frozen.
4. **Paperback strategy**: Kindle-only for the locked fields; edit the
   paperback fields that remain editable. No new editions before the market
   test proves the listing converts.
5. **Author names**: do NOT touch (Book 1 "Zaid Alzureiqat" vs Book 2
   "Dr. Zaid Alzureiqat"; locked on paperbacks, editable on Kindle — but a
   Kindle-only change risks unlinking the format pairing on Amazon). The
   credential lives in subtitles/descriptions/A+ instead. Revisit only with
   new editions.

## Hard constraints learned 2026-08-14

- **Paperback title, subtitle, and author name lock permanently ~72h after
  publish.** Only a new edition (new ASIN, loses reviews/listing age) can
  change them. Get metadata right BEFORE publishing. Kindle fields stay
  editable. Still editable on live paperbacks: series field, reading age,
  categories, keywords, description.
- The paperback "Content" and "Rights & Pricing" steps live in a separate
  print-setup app that forces a password re-login — automation stops there;
  Zaid must sign in or fetch those values himself.
- Aug 2 quality notification (Book 1 Kindle): **benign** — a recommendation
  to add the missing reading-age range. Zaid replied "I will fix it" on
  Aug 2 but it was never fixed; setting reading age 4–8 closes it. Not
  AI-related. Account health: 0 suppressed, 0 warnings, 0 open items.

## The fix window (status 2026-08-14)

| # | Action | Who | Status |
|---|--------|-----|--------|
| 1 | Verify AI disclosures | ext + Zaid | ◐ Kindle ×2 verified; align both to decision 2 (ext, pending). Paperbacks ×2 + draft BLOCKED on print-app sign-in (Zaid) |
| 2 | Read Aug 2 quality notification | ext | ☑ benign age-range recommendation; closes via action 7 |
| 3 | Series linking | — | ☑-by-decision: keep #3, gap stays; verify both books sit in the series page (ext) |
| 4 | Consistent credential claim | ext (subtitles/descriptions) + factory (covers later) | ◐ claim resolved ("by a Child Psychiatrist"); Kindle subtitles pending; covers/Author Central/medical disclaimer open |
| 5 | Interior spread images + A+ Content | Claude drafts / Zaid uploads | ☐ needs interior PDFs from Zaid |
| 6 | Reprice $9.99–10.99 + hardcover editions | Zaid sign-in, then ext | ☐ BLOCKED on print-app sign-in; hardcover needs new cover files (factory) |
| 7 | Reading age 4–8 (all four format entries) + ADHD/Special-Needs categories, remove Self-Esteem/Inspirational | ext | ☐ ready to execute (also closes the Aug 2 notification) |
| 8 | Book 2 benefit-led description | ext | ☐ ready to execute (draft in continuation prompt) |
| 9 | Print cost + KENPC recorded here | Zaid | ☐ print cost BLOCKED on sign-in; KENPC not surfaced (0 KENP anyway — KU already demoted to discovery-only) |
| 10 | Demand test: Ads €5/day + MedMeister email | Zaid | ☐ starts the 60-day clock after 1–8 done |

## Decision gate — 2026-10-15 (no judgment calls)

**KILL** if, after the fix window and ≥€300 ad spend, ANY of:
- Combined paperback units < 20/month, or
- Combined royalties < €100/month, or
- Fewer than 8 genuine, unaffiliated reviews across both books, or
- Blended ACOS > 100% with no month-over-month improvement.

**KILL IMMEDIATELY, any date**, if:
- Any KDP notification about AI content, content quality, or review abuse
  (do not appeal — shut down, protect the account), or
- Ads deliver >10,000 impressions at <0.2% CTR (cover/price can't compete), or
- Book 4 is being produced before Book 1 has sold 10 organic units.

**SCALE** only if one title reaches: **30+ paperback units/month, ACOS < 50%,
15+ genuine reviews.** Then, and only then, the backlog reopens.

Decision metrics are **paperback units/month and royalty/month** — never
Kindle BSR (it conflates $0.05 KU borrows with sales and ignores print,
where ~100% of the revenue is).

## Action log
- 2026-07-06: Book 1 paperback pub date (live on KDP Jul 15).
- 2026-07-14: Book 1 Kindle live, KU enrolled.
- 2026-07-26: Book 2 (Red-Hot Back) paperback live. Only sale + only review
  (Germany) land in this window.
- 2026-08-02: Book 1 Kindle quality notification (missing reading age)
  marked "I will fix it" — not actually fixed until action 7 runs.
- 2026-08-03: Book 2 Kindle live, KU enrolled.
- 2026-08-13: External audit (`AUDIT-2026-08-13.md`). Tracker rebuilt.
  Verdict: FIX (12h window) → 60-day ad test → decide 2026-10-15.
  Production frozen; 13-book default killed.
- 2026-08-14: Extension Phase 1–2 complete (read-only): ASINs/economics
  verified, notification read (benign), paperback metadata found permanently
  locked, print app password-blocked, Book 2 series number found to be 3.
  Zaid locked decisions 1–5 above. Phase 3–5 continuation prompt issued.
