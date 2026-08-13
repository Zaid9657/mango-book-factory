# Metadata Patterns & Extension Prompt Library

## Subtitle formula

`A Children's Book About [PROBLEM PHRASE] and [SKILL PHRASE] for Kids Ages 6–9 — by a Child Psychiatrist`

The PROBLEM PHRASE must be a phrase parents actually type. Test: search it on
Amazon — if autocomplete suggests it, it's real. Examples of the pattern in
the wild (verified ranking organically with zero ads):
- "A Children's Book About Grumpiness, Big Emotions, and Emotional Regulation for Kids Ages 3–7"
- "Children's Book to Ease School Anxiety, Build Confidence, and Learn Social Skills"

Mango examples:
- Busy Brain → "A Children's Book About Focus, a Busy Mind, and Paying Attention for Kids Ages 6–9 — by a Child Psychiatrist"
- Worry Cloud → "A Children's Book About Worry, Anxiety, and Feeling Calm for Kids Ages 6–9 — by a Child Psychiatrist"
- Red-Hot Back → "A Children's Book About Anger, Big Feelings, and Calming Down for Kids Ages 6–9 — by a Child Psychiatrist"

## 7 backend keywords (pattern)

Long-tail only, each a plausible search:
1. children's book about [problem]
2. [problem] book for kids ages 6-9
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

Use 2 small + 1 medium. Small = current #1 New Release in that subcategory
has < ~20 ratings. Known useful small candidates (verify freshness each time):
Children's Short Stories, Children's Parent Books, specific emotion
subcategories under Growing Up & Facts of Life. Avoid the head category
"Emotions & Feelings" as a badge target (too big) — keep it only as the
medium/discovery category.

## Extension prompt library (Claude Chrome extension, read-only)

**Category size check:**
```
Open the Amazon New Releases page for category [NAME/URL]. Report the #1
New Release book's rating count and publication date. Read-only.
```

**Day-30 vote collection:**
```
Open [book product page URL]. Report: Kindle BSR, paperback BSR, number of
ratings, average stars, and any badges (Best Seller / #1 New Release).
Repeat for: [list all live books]. Read-only, no changes.
```

**KDP metadata paste (per book):**
```
Go to my KDP Bookshelf → [book title] → edit Paperback (then Kindle) details.
Fill: subtitle, description, 7 keywords, categories exactly as pasted below.
Stop before Publish and hand back to me. [PASTE BLOCK]
```

**Free-day scheduling:**
```
KDP Bookshelf → [book] → Kindle eBook → Promote and Advertise → Free Book
Promotion → schedule [dates]. Confirm what was scheduled, change nothing else.
```
