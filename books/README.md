# Finished books archive

One folder per produced book: `NN-short-slug/`. This directory is the ground
truth the factory's Step 0 scans to decide which book to produce next — a book
counts as done when its folder contains an `*_INTERIOR.pdf`.

Each folder should contain:

- `Mango_and_the_*_INTERIOR.pdf` — the 24-page KDP interior
- `Mango_and_the_*_COVER.pdf` — the full cover wrap
- `manuscript.md` — the story text (7 blocks) + closing message
- `parent_note.md` — the 2-page "A Note for Parents"
- `scene_prompts.md` — the 7 illustration prompts used (for reruns/translations)
- `metadata.md` — KDP title, subtitle, description, keywords, categories
  (added at launch time by the launch playbook)

The manuscripts and prompts are what the German translation gate consumes for
winner books — never discard them.
