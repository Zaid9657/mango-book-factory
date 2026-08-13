# Mango Book Factory

Production pipeline and launch system for the **Mango the Crocodile** children's
picture book series (Amazon KDP). One feeling/skill per book. Two books live;
**production is frozen pending the 2026-10-15 market decision** — see
`AUDIT-2026-08-13.md` and `LAUNCH_TRACKER.md`.

## Repo map

| Path | What it is |
|------|-----------|
| `.claude/skills/mango-book-factory/` | Production pipeline: story → Gemini illustrations → interior PDF → cover wrap |
| `.claude/skills/mango-launch-playbook/` | KDP launch process: metadata, KU, launch week, Day-30 vote, German gate |
| `books/` | Archive of finished books (PDFs + manuscripts + prompts) — ground truth for what's shipped |
| `LAUNCH_TRACKER.md` | Single source of truth for launch state, fix checklist, kill/scale criteria |
| `AUDIT-2026-08-13.md` | The investor-grade audit behind the current strategy |
| `fonts/Baloo2.ttf` | Title font (OFL licensed) |
| `CLAUDE.md` | Project brief + hard-won environment notes |

## Produce the next book

Open a Claude Code session in this repo and say **"make the next Mango book"**.
The factory skill picks the first unshipped book from the series plan, writes
the story, generates the 7 illustrations, and builds both KDP-ready PDFs.

Requires the Gemini API key in
`.claude/skills/mango-book-factory/assets/gemini_key.txt` (gitignored — see the
`.example` file) or as `GEMINI_API_KEY`.

## Launch a book

Say **"launch book N"** — the launch playbook handles metadata, KU enrollment,
the launch-week checklist, and updates `LAUNCH_TRACKER.md`.
