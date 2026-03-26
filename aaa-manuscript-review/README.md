# aaa-manuscript-review

Reviews a Word (.docx) manuscript against AAA / The Accounting Review (TAR) submission guidelines and returns a compliance-marked document with tracked changes.

## What it does

Reads your manuscript, checks every element against the official AAA/TAR preparation guidelines, applies tracked changes (Word redline via `w:del`/`w:ins` XML) to flag each violation, and produces a compliance checklist. You review the output in Word and accept or reject each correction.

**What gets checked:**
- Anonymous submission (no author-identifying information)
- Manuscript length and word count limits
- Structured abstract format and length
- Heading hierarchy and numbering
- Table and figure formatting (placement, titles, notes)
- Reference list format (Chicago Author-Date)
- Footnote vs. endnote usage
- Font, margin, and spacing requirements
- Keywords and JEL classification codes

## Usage

```
Review this manuscript for TAR submission: [path/to/manuscript.docx]
```

Output file is saved in the same directory as the input, with ` - REVIEWED` appended before `.docx`.

## Requirements

- Input must be a `.docx` file (not PDF)
- Python 3.10+ with `python-docx` installed
- The `docx` skill must be installed (used for unpacking/repacking)

## Files

| Path | Contents |
|------|----------|
| `SKILL.md` | Full workflow and guideline checklist |
| `references/aaa_guidelines.md` | Extracted AAA/TAR manuscript preparation requirements |
| `scripts/tracked_changes.py` | Applies `w:del`/`w:ins` XML tracked changes to the unpacked docx |
