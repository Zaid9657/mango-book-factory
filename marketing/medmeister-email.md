# MedMeister email — the Mango books

**Status: DRAFT for Zaid to review and send. Nothing has been sent.**

This is the second half of fix-window action 10. The audit's finding: the
MedMeister list is German physicians — disproportionately parents of young
children, able to validate the credential instantly, and exactly who a
paediatrician gets asked "which book?" by. It costs one email and outweighs
every promo newsletter in the old playbook.

**Hard rule: this email must never ask for a review.** Soliciting reviews from
a list you control is precisely the Amazon review-abuse pattern that risks the
account. Announce the books, link them, stop.

---

## Betreff (pick one)

1. **Das hier ist keine Prüfungs-Mail.**
2. **Was ich Eltern sage, wenn die Sprechstunde vorbei ist**
3. **Zwei Kinderbücher — und warum ich sie geschrieben habe**

Recommendation: #1. It breaks the pattern of an inbox that expects exam
content, and it is honest about what follows.

---

## Body

> Kurz und ehrlich: Diese Mail hat nichts mit der Fachsprachprüfung, der
> Kenntnisprüfung oder telc zu tun. Wer nur dafür hier ist, kann sie
> überspringen — nächste Woche geht es wie gewohnt weiter.
>
> Ich bin Kinder- und Jugendpsychiater. In der Sprechstunde kommt fast immer
> dieselbe Frage, sobald die Diagnose ausgesprochen ist: „Und was machen wir
> zu Hause?"
>
> Sechsjährige lesen keine Ratgeber. Also habe ich zwei Bilderbücher
> geschrieben.
>
> Mango ist ein kleines Krokodil. Die Höcker auf seinem Rücken wechseln die
> Farbe, je nachdem, was er fühlt: grün, wenn er ruhig ist. Gelb bei Sorge.
> Rot-orange bei Wut. Kinder, die ein Gefühl noch nicht erklären können,
> zeigen auf die Farbe. Ab da lässt sich reden.
>
> **Band 1 — Der unruhige Kopf.** Mangos Gedanken sind schneller als der
> Unterricht. Er ist nicht faul und er strengt sich nicht zu wenig an. Er
> zielt auf alles gleichzeitig. (Aufmerksamkeit, ADHS)
>
> **Band 2 — Der rotglühende Rücken.** Mango wird wütend, und je mehr er
> dagegen ankämpft, desto größer wird es. (Wut, Impulskontrolle)
>
> In beiden Büchern scheitert Mango zuerst. Das ist Absicht — Kinder erleben
> es genauso. Am Ende steht jeweils eine Technik, die ein Kind wirklich
> anwenden kann, und zwei Seiten für Eltern: warum „Beruhig dich!" das
> Gegenteil bewirkt und was stattdessen hilft.
>
> Zwei Dinge, die Sie vorher wissen sollten: Die Bücher sind auf Englisch,
> für Kinder von 4 bis 8. Und die Illustrationen sind KI-generiert — der Text
> ist von mir. Das sage ich lieber vorher als hinterher.
>
> → [Band 1: Mango and the Busy Brain]
> → [Band 2: Mango and the Red-Hot Back]
>
> Falls Sie selbst Kinder in dem Alter haben — oder Eltern kennen, die gerade
> an genau dieser Stelle stehen: dafür sind die Bücher gemacht.
>
> Herzliche Grüße
> Zaid

---

## Notizen

- **Awareness level**: unaware. This list has never been told the books exist
  and did not subscribe for them, so the email opens by naming that directly
  instead of pretending it's a normal MedMeister send.
- **What's doing the work**: the clinic question ("und was machen wir zu
  Hause?") — it's the real reason the books exist, and every physician on that
  list has been asked it. The colour mechanic is the concrete detail that makes
  the book sound like a tool rather than a gift.
- **Toggles used**: Sie-form kept (brand default). **Team voice deliberately
  switched off** — this is personal, from Zaid, and a "wir vom MedMeister-Team"
  register would read as marketing and burn the trust the email depends on.
  Exam names spelled out per brand rule.
- **The AI-illustration line is deliberate.** German picture-book buyers are the
  least AI-tolerant market there is, and this list can and will notice. Saying
  it first costs a few readers; being found out later costs the list. Cut it
  only if Zaid decides otherwise — but recommend keeping it.
- **Anti-slop gate: NOT run.** Only `SKILL.md` is synced in this environment;
  `scripts/validate-german.py` and `references/banned-german-tells.txt` are not
  present, so the automated score could not be produced. The copy was written
  against the rules manually (no corporate register, verbs forward, fragments,
  no filler opener, no invented facts). **Re-run the validator before sending**
  if it's available on Zaid's machine.
- **Claims to verify before send**: that Zaid is content to state the
  child-and-adolescent-psychiatrist credential to this list, and that the two
  Amazon links are the correct marketplace for a German-based audience
  (amazon.de listings of the English editions).
- **No review request, no discount, no urgency.** Deliberate.
