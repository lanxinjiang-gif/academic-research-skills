# academic-pipeline

Orchestrator for the full academic research pipeline: from initial research through final submission-ready manuscript.

## What it does

Coordinates `deep-research`, `academic-paper`, and `academic-paper-reviewer` into a single end-to-end workflow with mandatory checkpoints, integrity verification, and two-stage peer review. It does not do the substantive work itself — it manages stage transitions, tracks state, and ensures quality gates are passed before moving forward.

## Pipeline stages

```
Stage 1:   RESEARCH      → deep-research (full mode)
Stage 2:   WRITE         → academic-paper (direct or plan mode)
Stage 2.5: INTEGRITY     → 100% reference and data verification
Stage 3:   REVIEW        → academic-paper-reviewer (full mode, 5 reviewers)
Stage 4:   REVISE        → academic-paper (revise mode)
Stage 4.5: RE-INTEGRITY  → Re-verify all citations and data
Stage 5:   RE-REVIEW     → academic-paper-reviewer (re-review mode)
Stage 6:   RE-REVISE     → Final revisions
Stage 7:   INTEGRITY     → Final integrity check
Stage 8:   FINALIZE      → Submission package + process record PDF
```

**Mandatory checkpoints:** User confirmation required before each stage transition — no silent auto-progression.

**Process record:** After completion, generates a PDF documenting the full human-AI collaboration history (inputs, decisions, outputs at each stage).

## Entry points

You do not need to start from Stage 1. The pipeline detects where you are and enters at the right stage.

| Situation | Pipeline entry |
|-----------|---------------|
| Starting from scratch | Stage 1 (RESEARCH) |
| You have a draft, need review | Stage 2.5 (INTEGRITY) |
| You received reviewer comments | Stage 4 (REVISE) |
| Paper was revised, need re-review | Stage 5 (RE-REVIEW) |

## Example prompts

```
I want to write a paper on how comment letters affect earnings management — run the full pipeline
```

```
I already have a draft on internal control weaknesses and audit fees — help me review it
```

```
I received R1 comments from JAE — help me revise and then re-review
```

## Dependencies

Requires all three core skills to be installed:
- `deep-research`
- `academic-paper`
- `academic-paper-reviewer`

## Files

| Path | Contents |
|------|----------|
| `SKILL.md` | Full orchestration logic, stage definitions, checkpoint rules |
| `agents/` | Stage management agent instruction files |
| `templates/` | Process record and handoff document templates |
