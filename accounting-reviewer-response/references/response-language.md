# Response Language Reference

Verbatim patterns and templates drawn from successful R1/R2 responses at top accounting journals (JAR, TAR, JOAR). Use these as starting points — adapt to your specific context rather than copy-pasting verbatim.

---

## Opening the Response Memo

### R1 Opening (first major revision)

The opening acknowledges the effort of reviewers and signals what the major changes are. Keep it to 3–5 sentences.

> Dear Professor [Name],
>
> We are deeply grateful to you, the Associate Editor, and the reviewers for your constructive guidance, which has substantially improved the overall framing and empirical findings of this paper. In response to your comments, we have [brief summary of the 2–3 most significant changes]. We believe the paper is now [significantly strengthened / better positioned / more clearly focused on X]. We discuss each comment in detail below.

> Dear Professor [Name],
>
> We thank you and the reviewers for your time and insightful comments. The revision addresses all concerns raised. The most substantive changes are: (1) [major change], (2) [major change], and (3) [minor change]. We address each comment in turn below.

### R2/R3 Opening (later rounds — after the paper has been through at least one revision)

At later rounds, the opening should: (1) acknowledge the editorial team's prior assessment, (2) express appreciation for continued feedback, (3) provide a bulleted list of the key improvements made in this round, and (4) signal that all remaining concerns have been addressed.

> Dear Professor [Name],
>
> We appreciate the editorial team's assessment of our previous revision. We also value the additional feedback, which provides constructive insights to further enhance the rigor and contribution of our study.
>
> In response to the reviewers' comments, we have made the following key improvements:
> - [Key improvement 1 — one sentence]
> - [Key improvement 2 — one sentence]
> - [Key improvement 3 — one sentence]
>
> Below, we provide detailed responses to each reviewer's comment. We hope these revisions fully address the editorial team's concerns and enhance the study's contribution to the accounting literature.

---

## Opening Lines for Individual Responses

### When you fully agree

- "We agree with [the AE / Reviewer X] that [restate concern in author's own words]. We have [specific action]. [Key result or change]. See [Table/Page]."
- "Thank you for this insightful point. We have [specific change] as suggested. [One-sentence description of what the analysis shows]."
- "We appreciate this suggestion and have adopted it in the revision. Specifically, [what was done]."
- "Thank you for raising this. We agree that [concern] and have [action]. The results are consistent with [main finding] and are reported in [location]."
- "Thank you for correcting our [statement / interpretation / framing]. We have revised [section/table/text] accordingly."
- "Thank you for pointing out this issue. The original [figure/table/section] presents [X] from the perspective of [Y], which may have created some ambiguity regarding [Z]. To clarify: [brief clarification]. To eliminate confusion, we have made the following clarifications..."

### When you partially agree or add nuance

- "We appreciate this concern. We have [done X as suggested]. However, we also note that [Y] because [reason]. The results in [Table Z] show that [conclusion is robust / qualitative findings unchanged]."
- "We thank [the reviewer / AE] for this comment. We have added [analysis]. While [the concern has some merit], we find that [key result]. This suggests [interpretation]. We discuss this further on page X."
- "We acknowledge that [concern]. We have [addressed it by doing X]. We note, however, that [Y], which [explains why the original approach is still defensible / does not materially affect our conclusions]."

### When you respectfully disagree

- "We thank the reviewer for this comment. We understand the concern that [restate concern clearly]. We believe the current approach is appropriate because [specific methodological or empirical reason]. Specifically, [brief explanation]. We have added a clarifying discussion on page X to make this point explicit."
- "We appreciate this suggestion. After careful consideration, we believe [original approach] is preferable because [clear reason grounded in the literature or data]. However, we have added [robustness check / footnote / discussion] to address this concern. The results are [similar to / consistent with] our main findings."
- "We thank [reviewer] for raising this concern. We note that [prior literature / data constraint / economic logic] suggests [X]. [Reviewer's alternative] would [reason why it is less appropriate here]. We have, however, added a footnote on page X discussing this point."

---

## Describing New Analyses

### Introducing a new test

- "In response to this comment, we have added [analysis name] using [method]. Specifically, [one sentence describing design]. The results indicate that [key finding], which [supports/is consistent with/does not affect] our main conclusions. These results are reported in [Table X / Appendix Y / page Z]."
- "Following the [AE's / reviewer's] suggestion, we have [action]. [Brief description of approach]. [Key statistic or result]."
- "We have conducted [analysis] as suggested. [Method in one sentence]. The coefficient on [key variable] is [estimate] ([t-stat / p-value]), [and its sign/magnitude / consistent with]."

### Rolling window / out-of-sample validation

> We have added an out-of-sample validation following the rolling-window design. We train the model using data from years t−10 through t−1 and evaluate predictions in year t, iterating forward to cover the full sample period. This design eliminates look-ahead bias because the distribution used for estimation is constructed using only information available at the time of prediction. The out-of-sample R² is [X], compared to [Y] for the Jones model, confirming that the improvement is not an artifact of in-sample overfitting. Results are in Table [X], Panel [B].

### Alternative measure

> We have constructed [alternative measure] as an additional robustness check. [Brief construction description]. The results using [alternative measure] are qualitatively similar to those in our main analysis: the coefficient on [key variable] is [estimate] and statistically significant at the [X]% level. These results appear in Table [X] / Internet Appendix Table [Y].

### Placebo / falsification test

> We have added a placebo test to address this concern. Specifically, we [replace treatment with a pseudo-treatment / use future values of the outcome / randomly assign treatment]. If [our identification is valid / the result is not spurious], we would expect [null / opposite result] in this test. [We find no significant effect, consistent with our identification assumption / The placebo coefficient is statistically indistinguishable from zero (t = X).] These results are in Table [X].

### Persistence test

> We follow [prior literature, e.g., Sloan 1996] and examine the persistence of [measure] across quintiles. Firms in the highest quintile exhibit [direction] persistence ([coefficient, t-stat]), while firms in the lowest quintile exhibit [direction] persistence ([coefficient, t-stat]). This pattern is consistent with [interpretation] and suggests that [conclusion].

### Stakeholder-specific validation test

> We added a new section, "[Section Name]" (Page [X]), to illustrate how our models [benefit managers / assist auditors / enable regulators / help investors]. [We posit that / If our models are effective,] [high-risk / low-risk] firms identified by our models should [exhibit more internal control weaknesses / incur higher abnormal fees / face more SEC investigations / generate higher returns] [one or two years later / before the report is released].
>
> Figure [X], Panel [Y] presents [outcome measure] sorted by predicted risk quintiles for one- and two-year horizons. As expected, high-[low-]risk quintiles show greater [lower] [outcome], with our models consistently outperforming benchmark models in distinguishing between high- and low-risk firms.

### Untabulated sensitivity analysis

> In an untabulated test, we [relaxed the threshold to the top X% / extended the sample period to / used alternative [measure/method]]. The results indicate that [key finding]. However, [where results change and why]. Although we do not tabulate this analysis in the manuscript, we provide the results below for your reference.

---

## Handling Framing / Contribution Concerns

### When the contribution is questioned

> Thank you for this comment, which helped us sharpen the paper's contribution. We agree that [prior framing] was unclear. The paper's core contribution is [restate precisely]. We have revised the introduction (pages X–Y) and abstract to reflect this. The key question we answer is: [precise question]. The evidence in [Table X] directly addresses this question by showing [finding].

### When the reviewer proposes an alternative framing

> We appreciate the suggestion to frame the paper as [alternative]. After reflection, we believe this framing [captures / is consistent with] what the paper shows. We have adopted [elements of the alternative framing] in the revision. Specifically, [what changed]. We believe this positions the paper's contribution more clearly as [reframed contribution].

### When the reviewer says your contribution is incremental to a specific paper

The standard two-pronged response:

> Thank you for your guidance on how to enhance the paper's contribution. We have implemented your advice from two perspectives.
>
> (1) Limited literature on [topic] despite its importance:
>
> We emphasized this gap in the [Introduction / Section X]: "[Exact text added to manuscript, with page reference]." While [Benchmark Paper] [does X], it [falls short in / does not fully explore / focuses on detection rather than prediction]. As we note on page [Y]: "[Exact text added]."
>
> (2) Substantial improvement in [metric] and its implications:
>
> [Describe the quantified improvement under apples-to-apples comparison.] Specifically, even when holding constant [methodology / variable set / information availability], our model achieves [metric of X] compared to [Y] for the benchmark, representing an improvement of [Z]%. See [Table / Footnote].

### When the reviewer questions the fairness of your benchmark comparison

> Thank you for raising the issue of comparability. We agree that controlling for [X] provides a more conservative basis for comparison. To ensure an apples-to-apples analysis, the proper counterpart in our study is [Table / Panel], which holds constant [the information availability adjustment / the variable set / the sample period]. Under this conservative comparison, our model achieves [metric], representing an improvement of [X]%. We have clarified this in [Footnote / Table note / Section] on page [Y].

### Acknowledging limitations

- "We acknowledge that [limitation] is a constraint of the current approach. We have added a discussion of this limitation in Section [X] on page [Y]."
- "We acknowledge that accurately estimating [X] requires [assumption], and this remains a limitation. We note, however, that [why the limitation does not undermine the main conclusions]."
- "This remains a limitation of our study. We discuss it explicitly in [section] and explain why [the main findings are still valid / this does not affect our interpretation]."

---

## When Both Reviewers Raise the Same Concern

When two reviewers flag the same issue, acknowledge this explicitly — it signals the concern is a must-do and that you treat both reviewers' input seriously.

- "Thank you for this valuable suggestion. Reviewer [X] also raised this same point. To address [both reviewers' concern / this], we have..."
- "Both you and Reviewer [X] highlighted the importance of [concern]. We agree that [action] will [further strengthen / better demonstrate] [aspect of the paper]. Accordingly, we have..."
- "This comment, together with [Reviewer X's] comment on [related issue], has led us to realize that [broader insight]. To address both concerns, we have [revised / added / reframed]..."

---

## Pointing to Changes in the Manuscript

### Page/table references

- "See Table [X], Panel [Y], Column [Z]."
- "These results are discussed on pages [X]–[Y]."
- "We have revised [Section/Table/Figure] [X] to reflect this."
- "The updated analysis appears in [Table X] (main text) and [Table IA-X] (Internet Appendix)."
- "We have added footnote [X] on page [Y] to clarify this point."
- "The revised introduction on pages [X]–[Y] now reads: '[brief excerpt]'."
- "(Page [X]) '[exact text from the revised manuscript]'" — use this format when quoting specific additions or revisions

### Including evidence in the response memo

When new analyses are added, show the key figure or table directly in the response memo (before the reviewer needs to look it up in the manuscript), then also cite the manuscript location. This makes reviewing easier and signals confidence in the new result.

> The updated results are presented in Table [X], which is presented below for your reference.
> [Include table or figure here]
> We have also updated the manuscript to reflect this change: (Page [Y]) "[text excerpt]"

---

## Closing the Response Memo

> We hope the above revisions fully address the concerns raised by you and the reviewers. We are grateful for the constructive feedback, which has significantly strengthened the paper. We look forward to your decision.

> We believe the revised manuscript addresses all concerns raised in the review process. The paper is substantially improved as a result of this feedback, and we hope the current version meets the journal's standards for publication. We look forward to hearing from you.

---

## Formatting Notes

- **Reviewer comment**: Display in *italics* or as a block quote (indented), or clearly labeled: `Reviewer 1, Comment 2:`
- **Author response**: Normal weight text, often labeled `Response:` or `Our Response:`
- **Manuscript changes**: Can be highlighted in a different color (blue is common) in the tracked response document
- **Cross-references**: Be precise — cite specific table numbers, panel letters, column numbers, and page numbers
- **Length calibration**: Short comments (writing, minor clarifications) → 2–4 sentence responses. Methodological concerns → full paragraph(s). Framing concerns → multiple paragraphs with clear structure.
- **Exact manuscript text**: When noting specific additions, quote the exact text added with page reference: "(Page X) 'The exact text inserted into the manuscript.'"
