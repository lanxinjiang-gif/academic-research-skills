# deep-research

A 13-agent pipeline for rigorous academic research on any topic, calibrated for accounting and AIS research.

## What it does

Runs a full research workflow — from question formulation through literature synthesis to a polished report — without requiring you to manage individual steps. Seven modes cover everything from a quick brief to a full PRISMA-compliant systematic review.

| Mode | Use when |
|------|----------|
| `full` | You need a comprehensive research report with synthesis and recommendations |
| `quick` | You need a fast literature brief |
| `paper-review` | You want a critical assessment of a specific paper |
| `lit-review` | You need a standalone literature review section for a manuscript |
| `fact-check` | You want to verify a specific claim or statistic |
| `socratic` | You're not sure what to research yet — guided dialogue mode |
| `systematic` | PRISMA-compliant review with optional meta-analysis |

## Accounting-specific calibration

This skill has been extended with three accounting research methodology patterns:

- **Archival empirical** — sample construction, identification strategies (DID, RDD, IV), standard table structure, clustering, robustness requirements
- **Design Science Research (DSR)** — Hevner et al. 2004 / Peffers DSRM framework for AIS artifact research
- **Machine Learning** — FinBERT, XGBoost, out-of-time validation, SHAP interpretability, data leakage prevention

Data sources recognized: Compustat, CRSP, EDGAR, Audit Analytics, I/B/E/S, BoardEx, ISS.

## Example prompts

```
Research the effect of material weaknesses in ICFR on audit fees — full mode
```

```
Literature review on discretionary accruals and earnings management since SOX
```

```
Guide my research — I'm interested in how auditors use machine learning but I'm not sure where to focus
```

```
Fact-check: does Audit Analytics cover 100% of SEC registrants?
```

## Files

| Path | Contents |
|------|----------|
| `SKILL.md` | Full workflow, agent roster, mode definitions |
| `references/methodology_patterns.md` | 13 methodology patterns including archival accounting, DSR, and ML |
| `agents/` | Individual agent instruction files |
| `templates/` | Output report templates |
