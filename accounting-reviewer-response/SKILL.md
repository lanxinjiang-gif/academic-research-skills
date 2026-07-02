---
name: accounting-reviewer-response
description: >
  Comprehensive workflow for responding to reviewer and Associate Editor (AE) comments
  at top accounting journals (JAR, TAR, JAE, JOAR, CAR, RAS). Use this skill whenever
  the user shares reviewer comments, an AE decision letter, or asks how to respond to
  academic reviewers in accounting or finance. Also trigger for tasks like: "help me
  think through what analyses to run for R1", "how should I frame my response to the AE",
  "the reviewer wants out-of-sample tests — what should I do?", "draft a response to this
  comment", "how do I show practical implications of my model?", "the reviewer says my
  contribution is incremental to [paper X]", or any request involving revision strategy,
  empirical design for a revision, or academic response memo writing. This skill covers
  all three phases: (1) analyzing and prioritizing reviewer concerns, (2) designing the
  empirical analyses needed to address them, and (3) drafting polished response language
  in the style of top accounting journals.
---

# Responding to Reviewer Comments at Top Accounting Journals

You are helping a researcher navigate the revision process at a top accounting journal. This skill covers three tightly linked activities:

1. **Analyze** — Read and interpret what reviewers and the AE actually want
2. **Design** — Plan the right empirical and framing responses
3. **Write** — Produce polished, professional response memo language

Always work in this order. Diagnosis before prescription; prescription before prose.

---

## Phase 1: Analyze the Comments

Before anything else, read all comments carefully and build a complete picture. The goal is to understand not just what reviewers *say*, but what they *mean* and what would satisfy them.

### Identify the commenters and their roles

| Role | Function | How to read them |
|------|----------|-----------------|
| **Editor** | Final decision-maker | Short letters signal key themes; read carefully for framing |
| **Associate Editor (AE)** | Gatekeeper and orchestrator | Carries the most weight; pedagogical tone means they want to help you succeed |
| **Reviewer(s)** | Anonymous experts | Focus on their core concerns; don't let minor stylistic requests distract |

The AE often synthesizes reviewer concerns and signals what is needed for acceptance. Treat AE comments as the highest-priority revision targets.

### Categorize every comment

For each comment, identify its type:

- **Framing / contribution** — Reviewer questions the research question, its novelty, or its importance
- **Incremental contribution vs. specific benchmark** — Reviewer identifies a close predecessor paper and questions whether your improvement is meaningful, fair, or apples-to-apples (e.g., "Bertomeu et al. already do this; what do you add?")
- **Econometric / methodology** — Concerns about endogeneity, identification, standard errors, sample construction
- **Empirical completeness** — Requests for additional analyses, robustness checks, alternative measures
- **Practical implications** — Requests to show that the paper's findings matter for real stakeholders (investors, managers, auditors, regulators)
- **Variable / data** — Concerns about measurement, sample period, data source
- **Presentation / writing** — Requests for clearer exposition, tables, figures
- **Theory / mechanism** — Requests to better connect findings to economic theory

### Triage by urgency

Distinguish between:
- **Must-do** — AE or reviewer explicitly demands; failure to address is a rejection signal
- **Should-do** — Reasonable requests that strengthen the paper
- **Can-explain-away** — Minor concerns where a clear explanation suffices without new analysis
- **Pushback territory** — Where the reviewer is wrong or the analysis would not change the paper's message; handle diplomatically

### Read between the lines

A reviewer who says "I am confused about X" often means "X is not sufficiently motivated." A reviewer who says "I struggle to understand the contribution" is asking you to reframe, not just add words. An AE who says "the reviewer is more open than in R0" is signaling conditional acceptance is near. When both reviewers raise the same concern, that concern is almost certainly a must-do.

For each key concern, write down in plain language: *What would fully satisfy this reviewer?*

---

## Phase 2: Design the Response

Once you understand what is needed, design the analytical and framing strategy before drafting prose.

### For framing/contribution concerns

- Identify the core economic question the paper can actually answer
- Reposition: what *is* the paper showing, stated precisely?
- Check: does the introduction make the right promise, and does the empirics deliver on it?
- Consider whether a reframing makes the contribution *stronger* (often it does)
- Distinguish between "improvement" framing and "limitation" framing — top journals often accept papers that rigorously document limits rather than claiming spurious improvements
- **Lead with ONE organizing economic frame**, not a list of results (e.g., "communication as a *third* solution to bank runs"). If the reviewer can't find the frame, that *is* the contribution problem.
- **Pre-empt the "replace the novel construct" test.** If the paper leans on a trendy construct (AI, ML, ESG, alternative data), a reviewer will ask: "would this survive with a mundane counterpart (AI summary → human summary)?" Answer it in the paper — state what is *uniquely* that construct, or the *enabling-condition* defense (it could be done manually in principle, but the technology is why the practice exists/scales).
- **Interrogate what your key variable *means*** (not just how it's measured): what does it bundle economically, and is the benchmark you compare against actually the right one? See `references/empirical_discussant_craft.md`.

### For "incremental vs. benchmark" concerns

This is one of the most common battles at top journals. The reviewer is asking: given that paper X exists, why does your paper matter?

The standard two-pronged response:
1. **Frame the literature gap**: "Despite paper X, [your topic] remains underexplored because [concrete reason]." Emphasize that the literature is limited, not just that one paper did something related.
2. **Quantify the improvement under a conservative comparison**: Define an "apples-to-apples" benchmark — holding constant everything that isn't your claimed contribution — and show the improvement is substantial. Be explicit about what changes when methodology is held constant.

See `references/analysis-playbook.md` Section 18 for the apples-to-apples benchmark comparison technique.

**When the paper is "factor N+1"** (adding one more item to a long list — e.g., "another auditor-expertise factor"), a strong reviewer will ask "why care about one more factor?" Two moves that convert this from a weakness into the contribution (see `references/empirical_discussant_craft.md`):
- **Reframe from a new *factor* to a new *understanding of the phenomenon*.** Don't argue "X also matters"; argue "X reveals the phenomenon works differently than we thought" (e.g., not "valuation expertise matters" but "audit is a continuous value-*co-creating* relationship, which is why auditors beat one-shot M&A intermediaries").
- **Isolate the active ingredient with a shared-function benchmark** — a comparison group that shares everything except your special ingredient (auditors vs. financial intermediaries who share the advisory function but lack the ongoing relationship). This is the "replace the novel construct" test run in reverse and is highly persuasive to referees.

### For econometric/methodology concerns

- Identify the specific threat to validity (endogeneity, selection, look-ahead bias, overfitting)
- Select the appropriate fix: instrumental variable, difference-in-differences, propensity score, placebo test, out-of-sample holdout, rolling-window estimation
- Assess feasibility: can this be done with available data in reasonable time?
- If you cannot fully address a concern, acknowledge the limitation explicitly and explain why it does not change the paper's conclusions

### For empirical completeness requests

See `references/analysis-playbook.md` for a full menu of standard analyses by concern type.

Common requests and their standard treatments:
- *Out-of-sample test* → Rolling window estimation; training/validation/test split; report out-of-sample R² or AUC
- *Alternative measure* → Construct alternative variable, report main results using it, show they are similar
- *Robustness to outliers* → Rank-based (winsorize by year vs. full sample), trimming, Huber robust regression
- *Placebo test* → Use future outcome variables, pseudo-treatment groups, or randomly assigned treatment
- *Subsample analysis* → Industry, size, time period, institutional environment splits

### For practical implications requests

When reviewers ask "who benefits from this and how?", organize your response around **stakeholder-specific validation tests**. For prediction/ML papers, the standard four-stakeholder structure works well:
- **Investors**: long-short portfolio performance (Sharpe ratio, Fama-French alpha)
- **Managers/Audit Committees**: internal control weaknesses in subsequent years
- **External Auditors**: abnormal audit fees in subsequent years
- **Regulators**: SEC investigations or comment letters in subsequent years

Each test follows the same pattern: sort observations into risk quintiles → plot or tabulate the outcome by quintile → compare your model vs. benchmarks. High-risk quintiles should show worse outcomes. See `references/analysis-playbook.md` Section 16.

### For variable/data concerns

- Address measurement error concerns with alternative data sources or instrumental variables
- For sample period concerns: extend if feasible; if not, explain why the period is appropriate
- For look-ahead bias: ensure all training data is constructed using only information available at estimation time

### Prioritize what goes in the main text vs. appendix

- Main analyses that support the core contribution → keep in the body
- Additional robustness and extensions → Internet Appendix or appendix
- AEs often signal explicitly what should move where; follow this exactly

### Make a revision plan

Before writing, produce a bulleted list:
```
Comment [X]:
  - Type: [framing / methodology / empirical / practical implications / etc.]
  - What is needed: [specific analysis or change]
  - Where in manuscript: [section / table / appendix]
  - Response stance: [accept / partial / explain]
```

---

## Phase 3: Write the Response Memo

Read `references/response-language.md` before drafting. The response memo is a formal academic document — it signals competence, seriousness, and collegiality all at once.

### Structure of the response memo

```
[Header]
Response to [Editor/AE/Reviewer] Comments on "[Paper Title]"
Manuscript ID: [ID]
[Date]

Dear Professor [Name],

[Opening paragraph — gratitude and brief summary of major changes]
[For R2+: include bulleted list of key improvements made]

---

RESPONSE TO ASSOCIATE EDITOR COMMENTS
[AE comment A in italics or blockquote]
Response: [your response]

[AE comment B in italics or blockquote]
Response: [your response]

---

RESPONSE TO REVIEWER 1 COMMENTS
[Comment 1 in italics or blockquote]
Response: [your response]

[Comment 2 in italics or blockquote]
Response: [your response]

---

[Continue for each reviewer]
```

### The anatomy of a good response

Every response has three parts, though their lengths vary:

1. **Acknowledge** — Thank the reviewer (genuine, not boilerplate) and show you understood the concern
2. **Act** — Describe specifically what you did (what analysis, what change, what reframing)
3. **Point** — Direct the reviewer to where they can see the change ("See Table X, Panel B" / "Page Y, paragraph Z")

For complex comments, break the response into labeled subpoints. When you have added a new analysis, include the key table or figure directly in the response memo body so the reviewer can evaluate it without flipping to the manuscript — then also give the manuscript location.

### Calibrating the stance

- **Full acceptance**: "We agree with [reviewer/AE] that... We have [done X]. The results show [key finding]. See Table Y."
- **Partial acceptance**: "We appreciate this concern. We have [done X as suggested]. However, we also maintain [Y] because [clear reason]. The new analysis in Table Z shows that [result, and it doesn't change the conclusion]."
- **Polite pushback**: "We thank the reviewer for this comment. [Acknowledge the concern is reasonable.] We believe the current approach is appropriate because [specific reason linked to the literature or data]. Specifically, [concise explanation]. We have added a discussion of this point on page X."

Never be defensive. Even when disagreeing, lead with understanding the concern.

### Tone and register

- Formal, collegial, and confident — not sycophantic, not defensive
- Gratitude is genuine: "Thank you for this insightful comment" > "We thank the reviewer"
- Use "we" throughout (even for sole-authored papers)
- Keep responses concise; reviewers value directness
- If a response is long, use subheadings or numbered steps to aid navigation

### Reporting new results

When an analysis was added in response to a comment:
- State what you did in one sentence
- Report the key coefficient/statistic and its significance
- Interpret the result in the context of the paper's argument
- Point to the table/figure/page

Example:
> We have added an out-of-sample validation following the rolling-window design suggested by the AE. Specifically, we train the model on years t-10 to t-1 and evaluate it on year t. The out-of-sample R-squared is 0.42 (vs. 0.31 for the Jones model), confirming that the improvement is not an artifact of overfitting. Results are reported in Table 5, Panel B, and discussed on page 18.

---

## Reference Files

- `references/response-language.md` — Exact phrases, opening sentences, structural templates; read before drafting any response
- `references/analysis-playbook.md` — Full menu of analyses for each type of concern; read when designing the empirical response
- `references/journal-norms.md` — What editors at JAR, TAR, JAE, JOAR, CAR expect; read when calibrating framing and contribution claims
- `references/empirical_discussant_craft.md` — Higher-altitude critiques top discussants/referees raise (organizing frame, "replace the novel construct" test, construct meaning, mechanism depth, incremental-factor reframing) and how to pre-empt them; read when responding to framing/contribution, incremental-vs-benchmark, or theory/mechanism comments
