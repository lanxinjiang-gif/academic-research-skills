# academic-paper

A 12-agent pipeline for writing complete academic manuscripts, calibrated for accounting and AIS journals.

## What it does

Takes you from a research idea (or existing draft) to a submission-ready manuscript. The pipeline handles structure design, argumentation, full-text drafting, citation formatting, and output in LaTeX, DOCX, or Markdown.

**Supported paper types:** IMRaD (empirical), literature review, theoretical, case study, policy brief, conference paper

**Supported citation formats:** Chicago Author-Date (default for accounting), APA 7.0, MLA, IEEE, Vancouver

**Output formats:** LaTeX (apa7 class), DOCX, PDF, Markdown

## Accounting-specific calibration

- Chicago Author-Date set as citation default (standard for TAR, JAR, JAE)
- Funding examples default to NSF, NIH, AICPA, IMA
- Writing register examples include archival empirical accounting and AIS/Design Science styles
- Journal submission guide covers TAR, JAR, JAE, CAR, RAST, AOS, AJPT, JMAR, JIS, IJAIS
- Terminology glossary: misstatement, restatement, discretionary accruals, Audit Analytics, comment letters, internal control weakness, material weakness, ICFR, earnings management, RAM

## Modes

| Mode | Trigger |
|------|---------|
| Direct | "Write a paper on X" — produces a full draft |
| Plan (Socratic) | "Guide me through writing a paper on X" — chapter-by-chapter dialogue |
| Revise | "Help me revise based on reviewer comments" — generates revision roadmap |

## Example prompts

```
Write an empirical paper on internal control weaknesses and earnings management post-SOX
```

```
Guide me through writing a paper on FinBERT for misstatement detection in 10-K filings
```

```
I received R1 comments from JAR — help me build a revision roadmap
```

```
Convert my manuscript to Chicago Author-Date citations
```

## Files

| Path | Contents |
|------|----------|
| `SKILL.md` | Full workflow, agent roster, configuration options |
| `references/journal_submission_guide.md` | Formatting and submission requirements for top accounting/AIS journals |
| `references/academic_writing_style.md` | Register examples for accounting/auditing, AIS/DSR, and social science writing |
| `references/hei_domain_glossary.md` | Accounting terminology: financial reporting, auditing, data sources, research design, regulatory |
| `agents/` | Individual agent instruction files |
| `templates/` | LaTeX and DOCX output templates |
