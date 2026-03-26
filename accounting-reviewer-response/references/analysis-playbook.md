# Analysis Playbook for Accounting Journal Revisions

A menu of standard analyses organized by the type of concern raised. For each concern type, the playbook describes what the reviewer is really worried about, which approaches address it most effectively, and how to present the results.

---

## Table of Contents

1. [Out-of-Sample Validation](#1-out-of-sample-validation)
2. [Alternative Measures / Robustness Checks](#2-alternative-measures--robustness-checks)
3. [Endogeneity and Identification](#3-endogeneity-and-identification)
4. [Look-Ahead Bias](#4-look-ahead-bias)
5. [Overfitting / Model Complexity](#5-overfitting--model-complexity)
6. [Outlier Treatment](#6-outlier-treatment)
7. [Validation of a New Measure](#7-validation-of-a-new-measure)
8. [Framing: Showing Limits vs. Improvements](#8-framing-showing-limits-vs-improvements)
9. [Sample Construction Concerns](#9-sample-construction-concerns)
10. [Economic Magnitude](#10-economic-magnitude)
11. [Mechanism and Channel Tests](#11-mechanism-and-channel-tests)
12. [Persistence and Predictive Power Tests](#12-persistence-and-predictive-power-tests)
13. [Placebo / Falsification Tests](#13-placebo--falsification-tests)
14. [Comparison to Benchmark Models](#14-comparison-to-benchmark-models)
15. [Earnings Management Detection Tests](#15-earnings-management-detection-tests)
16. [Stakeholder-Specific Validation Tests](#16-stakeholder-specific-validation-tests)
17. [Threshold / Cutoff Sensitivity Analysis](#17-threshold--cutoff-sensitivity-analysis)
18. [Apples-to-Apples Benchmark Comparison](#18-apples-to-apples-benchmark-comparison)

---

## 1. Out-of-Sample Validation

**What the reviewer worries about:** The model performs well in-sample due to overfitting or data snooping, but would fail on new data.

**Standard approaches:**

### Rolling-window estimation
- Divide the sample into training (years t−K to t−1) and test (year t) windows
- Common window sizes: 10 years rolling (for ML models), 5 years (for simpler models)
- Report out-of-sample R², RMSE, AUC, or prediction accuracy
- Compare to in-sample fit metrics — if gap is large, overfitting is a concern

### Train / validation / test split
- Training set: used to fit the model and tune hyperparameters
- Validation set: used to select hyperparameters (no look-ahead bias if temporally prior to test)
- Test set: held out completely; evaluated once
- Temporal ordering is crucial — never use future data to train or validate

### Hold-out period
- Estimate model on pre-2000 data; evaluate on 2000–present (or similar split)
- Good for assessing whether results survive to a new economic regime

**What to report:**
- Side-by-side comparison: in-sample vs. out-of-sample fit
- Statistical tests for difference (Diebold-Mariano test for forecast accuracy)
- Confidence intervals for out-of-sample metrics

---

## 2. Alternative Measures / Robustness Checks

**What the reviewer worries about:** The result is specific to your particular measurement choice and does not generalize.

**Standard approaches:**

- Construct 2–3 alternative measures from different data sources or with different assumptions
- Report main regression with each alternative in separate columns or panels
- Include a summary table: "Results are consistent across all [N] alternative measures"

**For accrual-based earnings quality studies:**
- Jones model, modified Jones (Dechow et al. 1995), performance-matched (Kothari et al. 2005)
- Cash-flow based measures (Dechow and Dichev 2002)
- Balance-sheet vs. cash-flow-statement approaches
- Working capital accruals vs. total accruals

**For earnings management detection:**
- Restatements (Big R, little r)
- SEC Accounting and Auditing Enforcement Releases (AAERs)
- SEC comment letters related to financial reporting
- Meet-or-beat analysts' earnings forecasts (small positive earnings surprises)
- Out-of-period adjustments
- Discretionary revenue recognition

**Presentation tip:** A single Internet Appendix table with all alternative measures preserves space in the main text.

---

## 3. Endogeneity and Identification

**What the reviewer worries about:** The key independent variable is correlated with omitted variables or determined simultaneously with the outcome.

**Standard approaches by concern type:**

### Omitted variable bias
- Add fixed effects (firm, year, industry × year)
- Add control variables from prior literature; show coefficient stability
- Entropy balancing or propensity score matching to create comparable control groups
- Discuss direction of bias: is it toward or against your hypothesis?

### Reverse causality
- Lagged independent variables
- Granger causality tests
- Instrumental variable approach (if valid instrument available)
- Difference-in-differences around a shock that plausibly affects the RHS variable but not (directly) the outcome

### Instrumental variables
- Valid instrument: correlated with the endogenous variable, uncorrelated with the error term
- First-stage F-statistic should exceed 10 (Stock-Yogo critical values)
- Report first-stage results, second-stage estimates, and underidentification/overidentification tests
- Common instruments in accounting: geographic variation, industry-level shocks, regulatory changes

### Difference-in-differences
- Treatment and control group should have parallel pre-trends (test and report this)
- Event study design around a clear shock
- Staggered adoption designs require special estimators (Callaway-Sant'Anna, Sun-Abraham) in recent literature

---

## 4. Look-Ahead Bias

**What the reviewer worries about:** The model uses information from the future to predict the past, inflating apparent performance.

**Standard approach:**
- Ensure all training data is constructed using only information available at the time of prediction
- For annual data: if predicting year t accruals, use only years 1 to t−1 for parameter estimation
- For winsorization: winsorize by year (not across the full sample) to avoid using future observations to define cutoffs
- For standardization / scaling: use rolling-window statistics, not full-sample statistics

**Important subtlety — information availability in training labels:**
Beyond the training/test split and winsorization, a separate source of look-ahead bias arises when training labels incorporate information that was not yet known at construction time. For example, if training on restatements known as of 2017 to build a 2011 model, restatements disclosed in 2017 for 2010 fiscal years are included — but these were unknown in 2011. The fix: use only restatements disclosed on or before the model construction date. This reflects real-world applicability.

**Reporting:**
- Explicitly state: "We construct [X] using only information available at estimation time. Specifically, [precise description]."
- If original analysis had look-ahead bias: "We have corrected this in the revision. The results using the bias-corrected design are [qualitatively/quantitatively] similar: [key statistic]."

---

## 5. Overfitting / Model Complexity

**What the reviewer worries about:** A complex model (ML, high-dimensional regression) fits the training data well but does not generalize.

**Standard approaches:**
- Cross-validation (k-fold, leave-one-out) within the training sample
- Hyperparameter tuning on a validation set, not the test set
- Regularization (LASSO, Ridge, Elastic Net) to penalize complexity
- Comparing model performance to simpler benchmarks (OLS, random walk)
- Learning curves: plot training vs. validation error as a function of training set size

**For machine learning models specifically:**
- Report hyperparameters and how they were selected
- Describe the feature importance (top predictors) to aid interpretability
- Show that results are robust to reasonable changes in hyperparameters

---

## 6. Outlier Treatment

**What the reviewer worries about:** Results are driven by extreme observations; treatment of outliers introduces look-ahead bias or arbitrary choices.

**Standard approaches:**

### Winsorization
- Most common: 1% and 99% by year (avoids look-ahead bias from full-sample cutoffs)
- Alternative: 1% and 99% across the full sample (simpler but has look-ahead bias if used for future prediction)
- Report: "We winsorize all continuous variables at the 1st and 99th percentiles within each fiscal year."

### Trimming
- Exclude observations below 1st / above 99th percentile entirely
- More aggressive than winsorization; check that N is not dramatically reduced

### Rank-based methods
- Convert to ranks or percentile scores before estimation
- Robust to extreme values and distributional assumptions
- Common in ML literature

### Reporting:
- Show summary statistics before and after outlier treatment
- Report truncation rates: "Truncation rates range from X% to Y% across years."
- Run main analysis with and without winsorization; show results are similar

---

## 7. Validation of a New Measure

**What the reviewer worries about:** The new measure does not capture what it claims to measure; it may be noisy, mismeasured, or not economically meaningful.

**Standard validation tests:**

### Face validity
- Show the measure correlates in expected ways with known constructs
- Distribution: is the range / skewness / kurtosis plausible?
- Time-series pattern: does it move around economic events as expected?

### Predictive validity (concurrent)
- Show that high values of the measure predict outcomes consistent with the economic mechanism
- Example: if the measure proxies for earnings management, show it predicts future restatements

### Predictive validity (prospective)
- Show that the measure predicts future outcomes of interest (e.g., stock returns, audit fees, analyst forecast errors)

### Incremental validity
- Show that the measure adds explanatory power beyond existing measures (e.g., in a horse race regression)
- Report both R² with and without the new measure

### Restatement analysis
- Stratify restatements by severity: Big R (SEC-mandated restatements), little r (voluntary error corrections), AAERs
- Test whether the measure predicts each type; document sensitivity to classification
- Note: AAERs are rare and industry-concentrated, so low power is expected

---

## 8. Framing: Showing Limits vs. Improvements

**What the reviewer worries about:** The paper claims "ML improves X" but the evidence is modest or the improvement is mechanically expected.

**Strategic reframing:**

Rather than: "Our ML measure is better than existing measures"
Consider: "We provide a more accurate characterization of the accrual-generating process and show that, despite this improvement, the ability to detect earnings management remains limited — suggesting that the ceiling is set by unobserved heterogeneity, not functional form misspecification."

This reframing:
- Answers the AE's concern that you are overselling
- Turns a potential negative (modest improvement) into a positive finding
- Opens the door to a new conversation about what limits abnormal accruals as a construct

**Supporting analyses:**
- Compare R² gains across specifications (show where the gains come from)
- Quantify the ceiling effect: "Even with the correct functional form, detection rates for [EM proxy] increase from X% to Y% — modest improvement despite substantially better model fit"
- Show that the problem lies in unobserved heterogeneity using a simulation or seeding experiment

---

## 9. Sample Construction Concerns

**What the reviewer worries about:** The sample is selected in a way that introduces bias or limits generalizability.

**Standard checks:**
- Report detailed sample selection table with observations lost at each step
- Compare sample characteristics to the full Compustat/CRSP universe
- Survivorship bias: does excluding early-delistings affect results?
- Industry concentration: are results driven by one or two industries?
- Time-period sensitivity: run analysis in sub-periods (pre-2000, post-2000; pre-crisis, post-crisis)

---

## 10. Economic Magnitude

**What the reviewer worries about:** Results are statistically significant but economically trivial.

**Standard approaches:**
- Report coefficient scaled by standard deviation: "A one-standard-deviation increase in [X] is associated with a [Y]-standard-deviation change in [outcome]"
- Compare to benchmarks: "This magnitude is comparable to [prior study's estimate] / represents [X]% of the average [outcome]"
- Decision-relevance: "This difference in [measure] would lead an auditor to charge [X] more in fees / is equivalent to [X] days of earnings"

---

## 11. Mechanism and Channel Tests

**What the reviewer worries about:** The paper shows a correlation but does not explain why it exists.

**Standard approaches:**
- Mediation analysis: show that the effect works through an intermediate variable M
- Subsample tests: if the mechanism operates more strongly in some settings, show the effect is larger there
- Triple interactions: [Treatment] × [Mechanism proxy] — the coefficient on the triple interaction tests whether the mechanism amplifies the main effect

---

## 12. Persistence and Predictive Power Tests

**What the reviewer worries about:** The measure is noisy and does not capture a persistent economic phenomenon.

**Standard approach (following Sloan 1996):**
- Sort firms into quintiles by the measure in year t
- Regress future value of the measure (or the outcome) on year-t quintile indicators
- Plot or table the mean future values by quintile
- Test whether top and bottom quintiles have significantly different persistence coefficients
- Report: "Firms in quintile 5 show [direction] persistence: [coefficient, t-stat]; firms in quintile 1 show [coefficient, t-stat]."

---

## 13. Placebo / Falsification Tests

**What the reviewer worries about:** The result is spurious — driven by confounders rather than the hypothesized mechanism.

**Standard approaches:**

### Time shuffling
- Randomly shuffle the treatment timing across firms; re-estimate; show null result
- Repeat many times to build distribution; your actual coefficient should exceed the 95th percentile

### Pseudo-outcome
- Use a measure that should not be affected by the treatment; show null
- Example: if treatment affects accruals, show it does not affect unrelated financial ratios

### Pseudo-treatment
- Use a group that received a similar shock but not your hypothesized causal channel
- Show that they do not exhibit the effect

### Geographic / industry placebo
- Show that regions / industries not exposed to the treatment show no effect

---

## 14. Comparison to Benchmark Models

**What the reviewer worries about:** Your model is compared to weak baselines; comparison to stronger models would be more convincing.

**Standard comparators in accounting research:**

| Benchmark | When to use |
|-----------|-------------|
| Jones (1991) | Any study on discretionary accruals |
| Modified Jones (Dechow et al. 1995) | Default benchmark for accrual quality |
| Kothari et al. (2005) performance-matched | When performance-matching is an issue |
| Dechow & Dichev (2002) | Accrual quality / mapping to cash flows |
| Random walk (last year = this year) | Time-series forecasting |
| OLS with all theoretically relevant variables | Benchmark for ML studies |
| Bertomeu et al. (2021) | Nonlinear accrual models with ML |

**Reporting:**
- Side-by-side table: your model vs. each benchmark, on each evaluation metric
- Statistical test: Vuong test (non-nested models), likelihood ratio test (nested), DM test (forecasting)
- "Our model achieves R² of X vs. Y for the modified Jones model (difference significant at [level] using Vuong test)."

---

## 15. Earnings Management Detection Tests

**What the reviewer worries about:** The measure has good in-sample fit but cannot actually detect real earnings management.

**Standard seeding / simulation experiment:**
- Take a sample of clean firm-years (no known EM)
- Artificially seed a known amount of earnings management (e.g., add 1% of total assets to accruals)
- Test whether the measure detects the seeded manipulation
- Report detection rates at various seeding levels (power curve)
- Compare detection rates across measures (your measure vs. Jones, modified Jones, etc.)

**Restatement test:**
- For firms that later restated earnings: did the measure flag them at the time?
- Report Type I error (false positives) and Type II error (missed detections)
- ROC curve across threshold choices

**Note on AAERs:**
- AAERs are rare (~0.1% of firm-years), industry-concentrated (tech, pharma), and often involve large, sustained manipulation
- Low statistical power is expected; acknowledge this and focus on directional evidence
- Consider supplementing with broader restatement data

**Market test:**
- Long-short portfolio based on the measure (e.g., long low-accrual, short high-accrual firms)
- Report abnormal returns (Fama-French 5-factor or q-factor model)
- This tests whether the measure captures information beyond what markets price in

---

## 16. Stakeholder-Specific Validation Tests

**What the reviewer worries about:** The paper shows a model works statistically, but it's not clear who benefits practically or how.

This concern is especially common at TAR for prediction/ML papers. The standard response is to add **separate tests for each major stakeholder group**, each using the same pattern: sort observations by predicted risk quintile, plot or tabulate a real-world outcome by quintile, and show your model outperforms benchmarks at distinguishing high-risk from low-risk.

### The four-stakeholder structure

**1. Investors**
- Construct a value-weighted long-short portfolio: short the top 5% (highest predicted risk) firms, long the bottom 5%
- Hold each portfolio for a fixed period; use value-weighted returns
- Report: annualized Sharpe Ratio, Fama-French 5-factor alpha
- Key claim: prediction-based strategy outperforms detection-based strategy because prediction is proactive — you can short *before* the report is issued, not after

**2. Managers and Audit Committees**
- Sort firms by predicted risk quintile (one-year-ahead and two-year-ahead)
- Measure: reported material weaknesses in internal controls in the subsequent 1–2 years
- Expected result: high-risk quintile (quintile 5) should show significantly more internal control weaknesses than low-risk quintile (quintile 1)
- Interpretation: if managers had access to the model, they could take preventive action

**3. External Auditors**
- Same quintile sort
- Measure: abnormal audit fees in subsequent 1–2 years (using Blankley, Hurtt, and MacGregor 2012 or similar)
- Abnormal fees capture unanticipated risk premiums — if the model predicts risk the auditor doesn't yet see, abnormal fees should be higher for high-risk quintiles
- Expected result: high-risk firms pay higher abnormal fees in subsequent years

**4. Regulators**
- Same quintile sort
- Measure: SEC investigations (SEC comment letters, AAER actions) in subsequent 1–2 years
- Expected result: firms in higher-risk quintiles should face more SEC scrutiny; the model outperforms benchmarks in distinguishing which firms get investigated

### Reporting pattern

For each stakeholder, produce a figure showing the outcome (y-axis) by risk quintile (x-axis), with separate lines for your model and benchmark models. The key visual message: your model's high-risk quintile (5) has a materially higher/lower outcome than the low-risk quintile (1), and the spread is larger than for benchmark models.

**Language template:**
> Figure [X], Panel [Y] presents [outcome] rates sorted by predicted risk quintiles for one- and two-year horizons. As expected, high-risk quintiles show [greater/higher/lower] [outcome] than low-risk quintiles, with our models consistently outperforming benchmark models in distinguishing between high- and low-risk firms.

**Note on framing:** These tests serve double duty — they validate model accuracy indirectly (high-risk predictions materialize as bad outcomes) while simultaneously demonstrating practical value. Frame them as "demonstrating the implications of our improved predictive accuracy for [stakeholder group]."

---

## 17. Threshold / Cutoff Sensitivity Analysis

**What the reviewer worries about:** Your results are specific to the particular threshold (e.g., top 5%) you chose; a different threshold would tell a different story.

**Standard approach:**
- Test alternative thresholds: if your main analysis uses 5%, also test 10% (and potentially 3% or 1%)
- For investment strategies, varying the threshold changes the breadth vs. precision tradeoff
- Document where results hold and where they don't, and explain why

**What to say when results are mixed across thresholds:**
> In an untabulated test, we relaxed the threshold to the top [X]% instead of the top [Y]%. The results indicate that [describe what holds]. However, [describe what changes at the relaxed threshold]. This suggests that a broader threshold may dilute the precision of [the longer-horizon / the more complex] model in identifying firms at the highest risk, which is consistent with [economic intuition].

**Guidance on what to tabulate vs. mention in a footnote:**
- If results are robust: include in a footnote or Internet Appendix
- If results show meaningful variation: discuss in the text and explain economically why the variation makes sense
- Never omit mixed results — reviewers will ask about them

---

## 18. Apples-to-Apples Benchmark Comparison

**What the reviewer worries about:** Your model outperforms the benchmark, but the comparison is unfair because your model also has advantages in data, methodology, or information set that have nothing to do with your claimed contribution.

This concern is most common when your paper improves on a specific predecessor paper. The reviewer is asking: if we hold constant everything except your claimed innovation, does the improvement remain?

**Standard approach:**

### Step 1: Identify the "confounds"
List everything that differs between your model and the benchmark: different variable sets, different information availability adjustments, different sample periods, different estimation algorithms.

### Step 2: Strip out the confounds
Create a comparison that controls for each confound:
- Same information availability → both models adjusted identically
- Same variable set → use only the variables from the benchmark paper
- Same time period and sample

### Step 3: Report layered comparisons
Present a table or series of footnotes that shows:
- Your model vs. benchmark with *no* methodology adjustments (optimistic for your model)
- Your model vs. benchmark with methodology held constant (most conservative; your claimed contribution isolated)

**Example framing:**
> If we take the more optimistic view of [benchmark]'s model (which includes additional variables and as-reported data), the proper counterpart in our study would be [Table X, Panel Y], which achieves [metric of Z]. This comparison holds constant the [information availability / variable set] and shows that our improvement is [X]% even under the most conservative comparison.

**Response language for this concern:**
> Thank you for raising the issue of comparability. We agree that controlling for [X] provides a more conservative basis for comparison. To ensure an apples-to-apples analysis, we have [added / revised] [Table X / Footnote Y] to compare models under identical [information availability / variable set / methodology] conditions. Even under this conservative comparison, our model achieves [metric], representing an improvement of [X]% over [benchmark]. See [location].

**Where to report:**
- The most conservative comparison (methodology held constant) should be in the main text or a prominent footnote
- Sensitivity comparisons can go in footnotes or an Internet Appendix
- Being transparent about all comparisons is more persuasive than cherry-picking the most favorable one
