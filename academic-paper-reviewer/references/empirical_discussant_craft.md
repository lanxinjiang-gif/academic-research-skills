# Empirical Discussant Craft — Reviewing Beyond the Validity Audit

**Purpose.** This reference raises the ceiling on reviews of *empirical* papers (economics, accounting, finance, and adjacent quantitative social science). A competent validity audit — identification, measurement, confounds, inference — is table stakes; any careful referee produces it. The comments that distinguish a **top-school discussant** operate one altitude higher: they reframe the paper, interrogate what its central variable *means*, test whether its headline contribution is what actually drives the result, and push the mechanism to its deepest defensible level.

Distilled from expert discussant sessions at a top accounting/finance research conference. Applies primarily to `methodology_reviewer_agent`, `domain_reviewer_agent`, `perspective_reviewer_agent`, `devils_advocate_reviewer_agent`, and `eic_agent`.

---

## The core gap: "referee" vs. "discussant"

| The audit (table stakes) | The higher-altitude move (what to add) |
|--------------------------|----------------------------------------|
| Is the effect causal? (endogeneity, selection) | What single **economic frame** reorganizes the whole paper? |
| Is the key variable measured with error? | What does the key variable **mean economically** — what does it bundle? |
| Are there confounds / alternative explanations? | If you swap the **headline construct** for a mundane one, does the result survive? |
| Is the mechanism plausible? | What is the **deepest theory-grounded** mechanism, not the first plausible one? |
| Are standard errors right? | Which **specific institutional fact or canonical theory** makes the critique bite? |

The reviewer's recurring failure mode is stopping at the left column. Every empirical review should spend deliberate effort on the right column.

---

## Eight principles (apply to empirical papers)

### 1. Lead with one organizing economic frame
Don't deliver a checklist of unconnected threats. Find the single lens that reorganizes the paper and generates predictions, tests, and interpretation.
- *Example:* a paper on bank communication during a crisis is best framed as "communication as a **third** solution to bank runs, after suspending convertibility and deposit insurance." That frame, not a list of robustness worries, is the contribution.

### 2. Interrogate what the key variable *means*, not just how well it's measured
Construct validity has two layers: (a) measurement noise, and (b) economic interpretation. The second is deeper and more often missed.
- *Example:* "sales growth" as an outcome **bundles a demand shock and a supply shock** — which have different predictions (a supply shock also raises costs / compresses margins) and different policy implications. Critiquing it only as "imputed / noisy" misses this.
- *Example:* an ESG **credit-relevance/exposure** indicator is not an ESG **performance** score; a low correlation with a performance-based benchmark is then almost mechanical, and that benchmark may be the wrong comparison entirely.
- *Ask:* "What does this variable economically represent? What competing forces does it combine? Given that, is the chosen benchmark/comparison the right one?"

### 3. Test the CONTRIBUTION, not just the effect — the "replace the novel construct" test
For any paper built on a trendy or novel construct (AI, ML, ESG, blockchain, alternative data), ask the decisive counterfactual:
> "Replace the novel construct with a mundane one — does the result still hold? If yes, what is uniquely [AI/ML/…] here?"
- *Example:* "If you replace the **AI**-generated summary with a **human** summary, does the market reaction change? If not, this is a summarization paper, not an AI paper."
- Always pair the attack with the author's **best defense** (e.g., "the novel technology is the *enabling* condition that made this scale — humans could have, but didn't, until the technology existed"). A strong review anticipates both.

### 4. Don't stop shallow on mechanism — reach the canonical theory
When you conclude "the effect is NOT [information / channel X]," push to the richest theory-grounded alternative rather than the first plausible one.
- *Example:* if bank tweets convey no new fundamental information, the channel is not "salience/confidence" but **higher-order beliefs / coordination** (Diamond–Dybvig, Morris–Shin global games): depositors act on what they believe *others* will do. That deeper mechanism is also the sharpest test (belief/topic **dispersion should narrow** after the disclosure if coordination is the channel).
- Ground the paper in its subfield's canonical theory to both frame the contribution and derive tests.
- **"Strategic behavior" papers — force the full mechanism chain.** For any "the agent does X strategically" claim (managers hide covenant strictness, firms solicit reviews, banks time disclosure), don't stop at "they do X." Require every link: **motive** (benefit vs. cost of X) → **target** (who is actually fooled?) → **efficacy** (does X *work*?) → **consequence** (does it *matter*?). A paper that documents only the first link has shown a correlation, not a mechanism.

### 5. Bring the SPECIFIC institutional fact or canonical theory — never the generic worry
"Temporal drift" is generic; "the platform's October-2016 rule change that banned incentivized reviews and reweighted its algorithm" is specific and actionable. "Control for backlash" is generic; "competitor rating agencies kept their numerical scores over the same window" reframes the event. Reach for the exact policy, event, peer behavior, or theorem.

### 6. Flip a validity threat into the identification strategy
Don't just patch a threat or drop contaminated data — turn the contaminating event into the design.
- *Example:* a rule change that breaks your measure is itself a **cost shock**: predict a *weaker* effect after it, and test that. The best comment converts a diagnosis into a research design.
- **Flip a "noisy measure" worry into support for the premise.** If a variable is genuinely hard for *the economic agents themselves* to compute (e.g., covenant strictness: find the covenant → non-GAAP definition → recalculate → forecast the metric), that difficulty is precisely *why the disclosure / summary / intermediary is valuable* — not merely a measurement caveat. Flip the threat toward the paper's motivation, not just its identification.

### 7. Validate constructs with theory-driven heterogeneity, motive-isolating placebos, and the data's internal structure — not only external benchmarks
- **Theory-driven heterogeneity:** the effect should be stronger where theory says it must be (e.g., "experience goods," where buyers rely on reviews, vs. "search goods," where they don't). Finding it there validates the construct.
- **Motive-isolating placebo:** a group that shares the mundane motive but lacks the hypothesized one (e.g., private firms have a marketing motive but no capital-market/benchmark-beating motive) should show no effect.
- **Internal structure:** exploit the data's own geometry (e.g., bunching just above a rounding threshold as regression-discontinuity evidence of manipulation).
- Apply **selection-on-unobservables bounds (Oster; Altonji–Elder–Taber)** consistently to any selection-on-treatment / selection-on-disclosure design.

### 8. Turn every critique into a constructive save, and know the subfield's canonical objections
Pair each "this threatens X" with "here is how to strengthen or reframe it." And come armed with the standard referee objections of the paper's subfield — e.g., for AI papers: (a) a human baseline would do the same, (b) results won't generalize across AI models (high- vs. low-capability), (c) there is a human-in-the-loop.

---

## Reviewer checklist (append to any empirical review)

- [ ] Stated the **one economic frame** that reorganizes the paper.
- [ ] Named what the **key outcome/treatment variable bundles** economically, and whether the benchmark fits.
- [ ] Ran the **"replace the novel construct with a mundane one"** test and stated the author's best defense.
- [ ] Pushed the mechanism to its **deepest theory-grounded** form (not the first plausible alternative); for a "strategic behavior" claim, checked the full **motive → target → efficacy → consequence** chain.
- [ ] Anchored the two most important critiques in a **specific institutional fact or canonical theorem**.
- [ ] Tried to **flip at least one threat into an identification** opportunity.
- [ ] Proposed at least one **theory-driven heterogeneity / motive-isolating placebo / internal-structure** validation, and named a **selection-bound** (Oster/AET) where selection is a concern.
- [ ] Every weakness carries a **constructive save**.
