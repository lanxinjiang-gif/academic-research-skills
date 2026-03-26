# accounting-literature-search

Searches and retrieves accounting research papers from top academic journals on behalf of the user.

## What it does

Given a research topic or question, searches across the major accounting journals, retrieves relevant papers, and returns structured results with citations, abstracts, and methodology notes. Useful for scoping a new research area, building a literature review, or checking what prior work exists on a specific hypothesis.

## Target journals (search priority order)

1. Journal of Accounting Research (JAR)
2. Journal of Accounting and Economics (JAE)
3. The Accounting Review (TAR)
4. Contemporary Accounting Research (CAR)
5. Review of Accounting Studies (RAST)
6. Accounting, Organizations and Society (AOS)
7. Journal of Accounting and Public Policy (JAPP)
8. Auditing: A Journal of Practice & Theory (AJPT)
9. Accounting Horizons (AH)

## Example prompts

```
Find papers on discretionary accruals and earnings management after SOX
```

```
What does the literature say about internal control weaknesses and audit fees?
```

```
Search for recent papers on machine learning applied to misstatement detection
```

```
Literature review on comment letters and financial restatements
```

## How it works

1. Clarifies the query if needed (one focused question, not a form)
2. Runs 3–5 targeted web searches across Google Scholar and journal sites
3. Falls back to browser-based search if results are insufficient or paywalled
4. Returns results formatted for Chicago Author-Date citation

## Files

| Path | Contents |
|------|----------|
| `SKILL.md` | Full search workflow, journal list, output format |
| `evals.json` | Evaluation cases for testing search quality |
