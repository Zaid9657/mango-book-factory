# Metadata Patterns & Extension Prompt Library

## Subtitle formula

`A Children's Book About [PROBLEM PHRASE] and [SKILL PHRASE] for Kids Ages 4–8 — [CREDENTIAL]`

**[CREDENTIAL]** = whichever claim is actually true, verbatim identical
everywhere (subtitle, description, cover, Author Central): "by a Child
Psychiatrist" only if Zaid authored as the psychiatrist; otherwise "with
Guidance from a Child Psychiatrist". The 2026-08-13 audit found the live
listings making both claims at once — a misrepresentation risk.
Age band is **4–8** (audit: the market for this format sits at 3–7/4–8, not 6–9).

The PROBLEM PHRASE must be a phrase parents actually type. Test: search it on
Amazon — if autocomplete suggests it, it's real. Examples of the pattern in
the wild (verified ranking organically with zero ads):
- "A Children's Book About Grumpiness, Big Emotions, and Emotional Regulation for Kids Ages 3–7"
- "Children's Book to Ease School Anxiety, Build Confidence, and Learn Social Skills"

Mango examples (with [CREDENTIAL] resolved per the rule above):
- Busy Brain → "A Children's Book About Focus, a Busy Mind, and Paying Attention for Kids Ages 4–8 — [CREDENTIAL]"
- Red-Hot Back → "A Children's Book About Anger, Big Feelings, and Calming Down for Kids Ages 4–8 — [CREDENTIAL]"

## 7 backend keywords (pattern)

Long-tail only, each a plausible search:
1. children's book about [problem]
2. [problem] book for kids ages 4-8
3. kids book about [skill]
4. [emotion] picture book for children
5. social emotional learning book [topic]
6. help child with [problem]
7. [topic] book written by psychiatrist

## Description skeleton

1. Hook question: the parent's problem ("Does your child's brain race ahead
   of the classroom?")
2. One paragraph: what happens in the story (Mango + Gogo + the technique).
3. "Why parents and therapists love this book:" 3–5 benefit bullets
   (emotional regulation, practical technique, read-aloud friendly,
   Note for Parents).
4. Credential paragraph: written by a child & adolescent psychiatrist;
   clinical Note for Parents in the back.
5. CTA line.

## Category selection

Must include an **ADHD / Special Needs / Disability** node where topical
(request via KDP's category tool) — the audit found the ADHD book filed with
no ADHD category at all. Then 1–2 small subcategories (small = current #1
New Release has < ~20 ratings; verify freshness each time) plus Emotions &
Feelings as the medium/discovery category. **Never Self-Esteem** — owned by
evergreen trade classics (its #1 has 36k+ reviews); no badge was ever
available there.

## Extension prompt library (Claude Chrome extension, read-only)

**Category size check:**
```
Open the Amazon New Releases page for category [NAME/URL]. Report the #1
New Release book's rating count and publication date. Read-only.
```

**Decision-gate data collection:**
```
Open my KDP Reports dashboard. Report per title, current month and lifetime:
paperback units, hardcover units, Kindle units, KENP pages read, royalties.
Then open the Ads console: impressions, clicks, CTR, spend, ACOS per campaign.
Read-only, no changes.
```
(Paperback units/month and royalty/month are the decision metrics — BSR and
ratings may be noted as secondary color only.)

**KDP metadata paste (per book):**
```
Go to my KDP Bookshelf → [book title] → edit Paperback (then Kindle) details.
Fill: subtitle, description, 7 keywords, categories exactly as pasted below.
Stop before Publish and hand back to me. [PASTE BLOCK]
```

**AI-disclosure + quality-notification check (run once, highest priority):**
```
KDP Bookshelf → for each title → Edit details: report exactly how the
AI-generated content questions are answered (text and images). Then open
Quality Notifications → Resolved and report the full content of the Aug 2
notification on Book 1. Read-only, change nothing.
```

**Print-cost + KENPC lookup:**
```
KDP Bookshelf → [book] → Edit paperback rights & pricing: report the exact
printing cost and royalty at the current price. Then in Reports → KENP,
report each Kindle edition's KENPC page count. Read-only.
```
