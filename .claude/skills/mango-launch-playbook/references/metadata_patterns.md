# Metadata Patterns & Extension Prompt Library

## Subtitle formula

`A Children's Book About [PROBLEM PHRASE] and [SKILL PHRASE] for Kids Ages 4–8 — [CREDENTIAL]`

**[CREDENTIAL]** = **"by a Child Psychiatrist"** — resolved 2026-08-14:
Zaid is a child & adolescent psychiatrist and the author. Verbatim identical
everywhere (subtitle, description, cover, Author Central); long form
"Dr. Zaid Alzureiqat — Child & Adolescent Psychiatrist". Never "with the
guidance of" (Book 1's back-cover error).
Age band is **4–8** (audit: the market for this format sits at 3–7/4–8, not 6–9).

The PROBLEM PHRASE must be a phrase parents actually type. Test: search it on
Amazon — if autocomplete suggests it, it's real. Examples of the pattern in
the wild (verified ranking organically with zero ads):
- "A Children's Book About Grumpiness, Big Emotions, and Emotional Regulation for Kids Ages 3–7"
- "Children's Book to Ease School Anxiety, Build Confidence, and Learn Social Skills"

Mango examples (Kindle editions only — paperback subtitles are permanently
locked at their published values):
- Busy Brain → "A Children's Book About Focus, a Busy Mind, and Paying Attention for Kids Ages 4–8 — by a Child Psychiatrist"
- Red-Hot Back → "A Children's Book About Anger, Big Feelings, and Calming Down for Kids Ages 4–8 — by a Child Psychiatrist"

## 7 backend keywords (pattern)

Long-tail only, each a plausible search, each under 50 characters:
1. children's book about [problem]
2. [problem] book for kids ages 4-8
3. kids book about [skill]
4. [emotion] picture book for children
5. social emotional learning book [topic]
6. help child with [problem]
7. [topic] book by a child psychiatrist

Live sets (submitted 2026-08-14, both formats per book):
- **Busy Brain**: adhd book for kids · children's book about paying
  attention · children's book about focus for kids ages 4-8 · busy mind
  picture book for children · help child focus and concentrate at school ·
  focus and attention book by a child psychiatrist · social emotional
  learning book about focus
- **Red-Hot Back**: anger management book for kids · calm down book for
  kids · children's book about anger for kids ages 4-8 · big feelings
  picture book for children · children's book about calming down and
  breathing · anger book by a child psychiatrist · social emotional
  learning book about anger

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

Verified against KDP's live picker 2026-08-14. **There is no children's-books
ADHD node.** The useful nodes for this series:

| Node | ID | Use for |
|------|-----|---------|
| Parenting & Relationships › Disabilities & Hyperactivity › Hyperactivity | 157625011 | The ADHD intent node — Amazon's ADD/ADHD shelf. ADHD titles only |
| Children's › Growing Up & Facts of Life › Difficult Discussions › Disability › Fiction | 155871011 | Children's-side neighbour for ADHD/neurodiversity titles |
| Children's › …Friendship, Social Skills & School Life › Emotions & Feelings › Fiction | 155884011 | The core SEL node — correct shelf for a picture book |
| Children's › Growing Up & Facts of Life › Health › Mindfulness & Meditation | — | Calm-down/breathing titles (anger, anxiety). Small node |

Rules:
- **Topical honesty wins.** Never put a non-disability title in a disability
  node to chase traffic — a mismatch costs CTR and conversion, which are the
  metrics the demand test measures. (Book 2, an anger book, deliberately has
  no ADHD/Disability node.)
- Keep at least one children's *fiction* node per format. A picture book
  filed only under Parenting shelves competes with adult guides.
- All 3 slots are always full, so every addition displaces something. Drop
  generic nodes first (Short Stories) — they carry no topical signal and are
  full of trade classics.
- **Never Self-Esteem & Self-Respect** or Inspirational & Personal Growth —
  owned by evergreen classics (Self-Esteem's #1 has 36k+ reviews); no badge
  was ever available there. Both were removed from the live books.
- Formats need not match exactly; diversifying nodes across paperback and
  Kindle covers more browse traffic.

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
