# Mango Launch Tracker

**Single source of truth for launch state.** Every session reads this first and
commits an update before finishing. Reconcile against KDP before any launch
decision — the 2026-08-13 audit (`AUDIT-2026-08-13.md`) found this file wrong
on almost every material point, and every decision downstream of it was noise.

**PRODUCTION IS FROZEN.** No new books until one live title hits the SCALE bar
below. The 13-book plan is dead as a default; the backlog survives only as a
contingency for a proven winner.

All figures below are per the 2026-08-13 audit — verify in KDP before acting.

## Live books

| # | Book | Feeling | Paperback live | Kindle live | KU | Price (pb/Kindle) | Lifetime sales | KENP | Reviews | BSR | Notes |
|---|------|---------|----------------|-------------|----|--------------------|----------------|------|---------|-----|-------|
| 1 | Mango and the Busy Brain | attention/ADHD | 2026-07-06 (Amazon date; KDP submitted Jul 15) | 2026-07-14 | yes | $12.99 / $3.99 | 1 paperback (July) | 0 | 1× 5.0★ DE Jul 26 — likely personal contact; never repeat | none | Quality notification resolved Aug 2 — content unread, Zaid to check |
| 2 | Mango and the Red-Hot Back | anger | 2026-07-26 | 2026-08-03 | yes | $12.99 / $3.99 | 0 | 0 | 0 | none | Series linking broken: title field lacks "2"; Amazon shows "Book 1 of 1" |

## Unpublished

| Book | Feeling | Status |
|------|---------|--------|
| Mango and the Wiggly Wait | patience | Coverless paperback draft in KDP, untouched since Jul 6. Not in the original 13-book plan. Decide: finish as part of fix window (no) or leave parked (yes — parked until SCALE) |
| Mango and the Worry Cloud | anxiety | **Never published.** Tracker previously listed it as shipped — wrong. Locate the manuscript/PDFs on Zaid's machine or write it off. |

## The 12-hour fix window (from the audit — complete before 60-day ad test)

| # | Action | Who | Status |
|---|--------|-----|--------|
| 1 | Verify AI-content disclosure on all 3 titles in KDP title setup | Zaid | ☐ HIGHEST PRIORITY |
| 2 | Read the Aug 2 resolved quality notification (Quality Notifications → Resolved) | Zaid | ☐ |
| 3 | Fix series linking: "(Mango the Crocodile 2)" in Book 2 title field; both books in series page | Zaid | ☐ |
| 4 | One consistent credential claim everywhere; name + credential on covers/title pages; Author Central; medical disclaimer in front matter | Zaid + factory (cover revisions) | ☐ |
| 5 | Upload 5–7 interior spread images per listing; A+ Content both books | Claude drafts / Zaid uploads | ☐ |
| 6 | Reprice paperbacks $9.99–$10.99; add hardcover editions $17.99–$19.99 | Zaid | ☐ |
| 7 | Re-band to ages 4–8; add ADHD / Special Needs / Disability categories | Zaid | ☐ |
| 8 | Rewrite Book 2 description benefit-led | Claude drafts / Zaid pastes | ☐ |
| 9 | Record exact print cost (Bookshelf → Edit paperback rights & pricing) and KENPC counts here | Zaid | ☐ if print cost >$3.50 → leans KILL; if KENPC <15 → drop KU from strategy |
| 10 | Start demand test: Amazon Ads €5/day exact-match (ADHD/focus/anger/big feelings), pointed at paperbacks; one honest email to MedMeister list | Zaid | ☐ starts the 60-day clock |

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
- 2026-07-06: Book 1 paperback live (per Amazon).
- 2026-07-14: Book 1 Kindle live, KU enrolled.
- 2026-07-26: Book 2 (Red-Hot Back) paperback live. Only sale + only review
  (Germany) land in this window.
- 2026-08-02: Book 1 quality notification resolved (content unread).
- 2026-08-03: Book 2 Kindle live, KU enrolled.
- 2026-08-13: External audit run (`AUDIT-2026-08-13.md`). Tracker rebuilt from
  KDP ground truth. Verdict: FIX (12h window) → 60-day ad test → decide
  2026-10-15. Production frozen; 13-book default killed.
