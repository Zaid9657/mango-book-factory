# Amazon Ads — the 60-day demand test

**Status: DRAFT for Zaid to set up. Nothing has been spent.** This is action 10
in `LAUNCH_TRACKER.md` — the only step in the whole fix window that can produce
a real market signal before the 2026-10-15 decision.

## Campaign structure

Two campaigns, one per book. Sponsored Products → **Manual targeting → Keyword
targeting → Exact match only**. Broad and phrase burn budget on a €5/day test.

| Setting | Value |
|---|---|
| Marketplace | **amazon.com** — the English-language market. (amazon.de is where the one sale came from, but English picture books are a thin shelf there; revisit only if .com shows life.) |
| Format targeted | **Paperback** — print is ~100% of the revenue. Never point the ads at the Kindle edition or KU. |
| Budget | €5/day per campaign is the plan's total — if running both at once, €2.50 each, or alternate one book per 30 days. Alternating gives cleaner per-book data. |
| Starting bid | $0.45 exact. Children's-book keywords typically clear $0.30–0.75. |
| Duration | 60 days, ~€300 total. |

## Book 1 — Mango and the Busy Brain (ADHD/attention)

High intent first — these are parents typing a problem, not browsing:

```
adhd books for kids
adhd book for children
childrens book about adhd
adhd picture book
books for kids with adhd
child cant sit still book
childrens book about focus
book about paying attention for kids
help child focus book
childrens book about concentration
adhd books for kids age 5
adhd books for kids age 6
social emotional learning books adhd
neurodiversity childrens book
```

## Book 2 — Mango and the Red-Hot Back (anger)

```
anger management for kids book
childrens book about anger
kids book about big feelings
calm down book for kids
childrens book about temper tantrums
book about angry feelings for children
teaching kids to manage anger
emotional regulation books for kids
childrens book about self control
big feelings picture book
anger books for kids age 5
anger books for kids age 6
social emotional learning book anger
kids book about calming down
```

## Negative keywords (add to both campaigns at launch)

Stops the budget leaking to adult, academic and toy traffic:

```
free
pdf
workbook
textbook
toy
toys
game
games
adult adhd
adhd for adults
medication
dsm
teacher edition
curriculum
spanish
```

## What to log weekly in LAUNCH_TRACKER.md

Impressions · clicks · CTR · spend · ACOS · **paperback units** · royalties.
Paperback units and royalty per month are the decision metrics — never BSR,
never KU borrows.

## Stop rules (from the tracker — these are binding)

- **Kill immediately** if ads deliver **>10,000 impressions at <0.2% CTR**.
  That means the cover and price cannot compete for attention, and no
  downstream optimisation fixes it.
- At the 2026-10-15 gate, blended **ACOS >100% with no month-over-month
  improvement** is one of the KILL triggers.
- Do not raise budget above €5/day to "give it a chance". The test is designed
  to be cheap; a bigger budget buys a more expensive version of the same answer.

## Before switching the campaign on

The listing must be able to convert or the spend is wasted. Required first:
interior spread images uploaded, A+ Content live (`marketing/aplus-content.md`),
price at $9.99–10.99, and the submitted metadata (ages 4–8, new categories)
actually propagated.
