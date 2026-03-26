# academic-paper-reviewer

Simulates a complete journal peer review process with 5 independent reviewer personas, calibrated for accounting and AIS journals.

## What it does

Reads your manuscript, automatically identifies the field and methodology type, then convenes 5 reviewers who evaluate the paper from non-overlapping perspectives. Produces individual review reports plus an Editorial Decision Letter and Revision Roadmap.

**Reviewer lineup:**

| Reviewer | Role |
|----------|------|
| Editor-in-Chief | Evaluates fit, contribution, and overall quality |
| Peer Reviewer 1 | Methodology specialist |
| Peer Reviewer 2 | Domain expert |
| Peer Reviewer 3 | Cross-disciplinary viewpoint |
| Devil's Advocate | Challenges core arguments, identifies weaknesses |

## Accounting-specific calibration

The review criteria framework includes a dedicated archival accounting section covering:

- Identification strategy (DID, RDD, IV) and parallel trends test
- Endogeneity and reverse causality concerns
- Standard error clustering (two-way by firm and year)
- Cross-sectional and channel tests
- Auditing sub-criteria: Audit Analytics data quality, comment letter extraction, PCAOB inspection coding

**Automatic red flags** (triggers Major Revision or Reject at Big 3 journals):
- No endogeneity discussion
- OLS with standard errors not clustered by firm
- Sample stops before 2012 without justification
- Missing alternative accrual measures
- Hand-collected data with no inter-rater reliability

**Journal calibration:** TAR, JAR, JAE, CAR, RAST, AOS, AJPT, JMAR, EAR, JFR, JIS, IJAIS

## Modes

| Mode | Use when |
|------|----------|
| `full` | First-round review of a complete manuscript |
| `re-review` | Verifying whether revisions addressed prior comments |
| `quick` | Fast screening (contribution + fatal flaws only) |
| `methodology` | Deep focus on research design and identification |
| `socratic` | Guided dialogue to strengthen the paper before submission |

## Example prompts

```
Review this paper: [paste manuscript or provide file path]
```

```
Re-review this paper — here are the original comments and my revision: [attach both]
```

```
Quick assessment: is this paper ready to submit to TAR?
```

## Files

| Path | Contents |
|------|----------|
| `SKILL.md` | Full workflow, reviewer configuration, mode definitions |
| `references/top_journals_by_field.md` | Journal tiers and EIC calibration notes for accounting + AIS |
| `references/review_criteria_framework.md` | Review dimensions including archival accounting red flags and auditing sub-criteria |
| `agents/field_analyst_agent.md` | Detects discipline and methodology to configure reviewers |
| `agents/` | Other reviewer agent instruction files |
