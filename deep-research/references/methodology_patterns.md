# Research Methodology Patterns — Design Templates

## Purpose
Ready-to-use methodology templates for common research designs. Used by the research_architect_agent.

## Pattern 1: Systematic Literature Review

### When to Use
- Mapping the state of knowledge on a topic
- Identifying gaps in existing research
- Synthesizing evidence for policy/practice recommendations

### Design Template
```
Research Question: What is known about [topic] in [context]?

Protocol:
1. Register protocol (PROSPERO or similar)
2. Define search strategy (databases, keywords, Boolean operators)
3. Establish inclusion/exclusion criteria
4. Search execution + documentation
5. Two-pass screening (title/abstract → full text)
6. Quality appraisal of included studies
7. Data extraction
8. Synthesis (narrative, thematic, or meta-analytic)
9. Report per PRISMA guidelines

Quality Criteria:
- Comprehensive search (minimum 3 databases)
- Reproducible strategy
- Dual screening (2 reviewers or reviewer + verification)
- PRISMA checklist completed

Reporting Standard: PRISMA 2020 (see references/equator_reporting_guidelines.md)
```

### PRISMA Flow Template
```
Records identified through database searching (n = )
Additional records from other sources (n = )
         ↓
Records after duplicates removed (n = )
         ↓
Records screened (title/abstract) (n = )
Records excluded (n = )
         ↓
Full-text articles assessed for eligibility (n = )
Full-text excluded, with reasons (n = )
         ↓
Studies included in synthesis (n = )
```

## Pattern 2: Comparative Case Study

### When to Use
- Comparing policies, programs, or institutions
- Understanding how context shapes outcomes
- Generating theoretical propositions from multiple cases

### Design Template
```
Research Question: How does [phenomenon] vary across [cases]?

Protocol:
1. Case selection (theoretical or purposive sampling)
2. Define comparison framework (dimensions, variables)
3. Data collection per case (documents, interviews, data)
4. Within-case analysis
5. Cross-case analysis
6. Pattern identification and explanation

Quality Criteria:
- Explicit case selection rationale
- Consistent data collection across cases
- Both within-case and cross-case analysis
- Rival explanations considered
```

### Comparison Matrix Template
```
| Dimension | Case A | Case B | Case C | Pattern |
|-----------|--------|--------|--------|---------|
| Context   |        |        |        |         |
| Input     |        |        |        |         |
| Process   |        |        |        |         |
| Outcome   |        |        |        |         |
```

## Pattern 3: Policy Analysis

### When to Use
- Evaluating existing or proposed policies
- Comparing policy approaches across jurisdictions
- Assessing policy outcomes and unintended consequences

### Design Template
```
Research Question: How effective is [policy] in achieving [goal]?

Framework Options:
A. Bardach's Eightfold Path
B. Dunn's Policy Analysis Framework
C. SWOT Analysis
D. Logic Model (Input → Activity → Output → Outcome → Impact)

Protocol:
1. Problem definition
2. Evidence gathering (quantitative + qualitative)
3. Policy option identification
4. Criteria development (effectiveness, efficiency, equity, feasibility)
5. Option assessment against criteria
6. Recommendation with trade-offs

Quality Criteria:
- Multiple criteria (not just effectiveness)
- Stakeholder perspectives included
- Unintended consequences assessed
- Implementation feasibility addressed
```

## Pattern 4: Mixed Methods (Convergent Parallel)

### When to Use
- Complex phenomena requiring multiple data types
- Need to triangulate findings
- Quantitative data needs qualitative explanation (or vice versa)

### Design Template
```
Research Question: What is the nature and extent of [phenomenon]?

Protocol:
QUAN strand:                    QUAL strand:
1. Survey/data collection       1. Interviews/focus groups
2. Statistical analysis         2. Thematic analysis
3. Quantitative findings        3. Qualitative findings
                    ↓
            4. Integration
            5. Joint display
            6. Meta-inference

Quality Criteria:
- Both strands have independent rigor
- Integration strategy explicit (not just parallel reporting)
- Joint display or mixed methods matrix
- Meta-inferences draw on both strands

Reporting Standards: QUAL strand → COREQ; QUAN strand → STROBE/CONSORT (see references/equator_reporting_guidelines.md)
```

## Pattern 5: Content/Document Analysis

### When to Use
- Analyzing texts, policies, media, or documents
- Identifying patterns in communication
- Systematic examination of large document sets

### Design Template
```
Research Question: What themes/patterns emerge from [document set]?

Protocol:
1. Define corpus (which documents, inclusion criteria)
2. Develop coding framework (deductive, inductive, or hybrid)
3. Code systematically (inter-coder reliability if multiple coders)
4. Analyze codes → categories → themes
5. Report with exemplar quotes/excerpts

Quality Criteria:
- Corpus selection transparent
- Coding framework documented
- Inter-coder reliability reported (if applicable)
- Saturation discussed
```

## Pattern 6: Exploratory Research

### When to Use
- New or under-researched topics
- Generating hypotheses for future research
- Understanding phenomena from participant perspective

### Design Template
```
Research Question: How do [participants] experience/understand [phenomenon]?

Protocol:
1. Purposive sampling
2. Semi-structured interviews or observations
3. Iterative data collection and analysis
4. Open coding → axial coding → selective coding
5. Theory or framework development
6. Member checking / peer debriefing

Quality Criteria:
- Reflexivity statement
- Thick description
- Data saturation discussed
- Transferability criteria addressed

Reporting Standard: COREQ for interviews/focus groups (see references/equator_reporting_guidelines.md)
```

## Pattern 7: Benchmarking Study

### When to Use
- Comparing performance against standards or peers
- Identifying best practices
- Setting performance targets

### Design Template
```
Research Question: How does [entity] perform compared to [benchmark]?

Protocol:
1. Select benchmarking type (internal, competitive, functional, generic)
2. Identify indicators and metrics
3. Collect comparable data
4. Analyze gaps
5. Identify best practices from high performers
6. Develop improvement recommendations

Quality Criteria:
- Comparable metrics (apples to apples)
- Context factors acknowledged
- Multiple indicators (not single metric)
- Actionable recommendations
```

## Pattern 8: Technology Requirements Analysis

### When to Use
- Assessing feasibility, requirements analysis, and technology comparison for new technologies
- Technology selection decisions before system design
- Risk and benefit assessment of technology adoption
- When research questions involve "Which technology should be used?" or "Can this technology solve the problem?"

### Design Template
```
Research Question: What technology approach best addresses [need] given [constraints]?

Protocol:
1. Requirement Elicitation
   - Stakeholder interviews
   - Existing system/process analysis
   - Functional requirements vs non-functional requirements (performance, security, scalability)
2. Technology Scanning
   - Inventory of candidate technologies (at least 3 options)
   - Technology Readiness Level (TRL) assessment
   - Community activity, documentation completeness, long-term maintenance risk
3. Feasibility Assessment
   - Technical feasibility: Can it be done?
   - Economic feasibility: Is it worth doing?
   - Organizational feasibility: Does the team have the capability?
   - Schedule feasibility: Is there enough time?
4. Proof of Concept (PoC)
   - Construct minimal verification targeting key technical risks
   - Define success criteria (performance thresholds, integration test pass rates)
   - Document encountered problems and solutions
5. Requirement Specification
   - Produce formal requirements document
   - Define acceptance criteria
   - Establish traceability matrix (requirements ↔ design ↔ testing)

Quality Criteria:
- Requirements completeness: All stakeholder requirements have been collected
- Traceability: Each requirement is traceable to its source; each design decision maps to a corresponding requirement
- Technical feasibility verification: Key technical risks have been validated through PoC
- Fair comparison of options: Consistent evaluation framework used to compare different technology options
```

### Technology Comparison Matrix Template
```
| Evaluation Dimension | Option A | Option B | Option C | Weight |
|---------------------|----------|----------|----------|--------|
| Functional Fit      |          |          |          | 30%    |
| Technology Maturity  |          |          |          | 20%    |
| Adoption Cost        |          |          |          | 15%    |
| Maintenance Cost     |          |          |          | 10%    |
| Learning Curve       |          |          |          | 10%    |
| Scalability          |          |          |          | 10%    |
| Community/Ecosystem  |          |          |          | 5%     |
| Weighted Total       |          |          |          | 100%   |
```

## Pattern 9: Legal Case Analysis

### When to Use
- Legal and regulatory policy analysis, case law research, legal text interpretation
- Analyzing current regulations and judicial opinions on specific legal issues
- Comparing legal approaches across different jurisdictions
- When research questions involve statutory interpretation, rights and obligations analysis, or legal aspects of policy analysis

### Distinction from Pattern 3 (Policy Analysis)
- **Policy Analysis**: Focuses on evaluating policy effectiveness — "Is this policy working?" "Are there better policy options?"
- **Legal Case Analysis**: Focuses on analyzing legal texts and case law — "What does the law say?" "How do courts interpret it?" "Are there legal loopholes?"

### Design Template
```
Research Question: How does the law address [issue] and what are the implications for [context]?

Protocol:
1. Issue Identification
   - Translate research question into specific legal issues
   - Distinguish questions of fact vs questions of law
   - Define the relevant legal domains (public law / private law / international law)
2. Legal Framework Mapping
   - Constitutional-level provisions
   - Statutory / regulatory / administrative rule levels
   - International conventions / soft law
   - Legislative history and rationale for amendments
3. Case Law Analysis
   - Systematic case law search (court level, time range, keywords)
   - Extract key holdings from decisions
   - Analyze trends in case law evolution
   - Identify majority opinions vs dissenting opinions
4. Legal Reasoning
   - Textual interpretation, systematic interpretation, purposive interpretation, historical interpretation
   - Comparative law analysis (how other jurisdictions handle the issue)
   - Review and evaluate scholarly opinions
   - Interest balancing and value judgments
5. Recommendations
   - Interpretive recommendations under existing law
   - Legislative reform recommendations (if necessary)
   - Practical implementation recommendations
   - Risk warnings

Quality Criteria:
- Legal source accuracy: Cited regulations and cases must be current and effective versions
- Logical consistency: Legal reasoning process must not be self-contradictory
- Argumentation completeness: All possible interpretive paths have been considered
- Comparative law rigor: When comparing jurisdictions, differences in legal system backgrounds must be noted
```

### Legal Analysis Structure Template
```
I. Legal Issues
   [Specific legal issues in dispute]

II. Relevant Provisions
   1. Statutory level:
   2. Regulatory level:
   3. International norms:

III. Judicial Opinions
   1. Majority opinion: [Case number] [Key holding]
   2. Dissenting opinion: [Case number] [Key holding]
   3. Trends:

IV. Scholarly Opinions
   1. View A:
   2. View B:
   3. Author's view:

V. Comparative Law
   [How other jurisdictions handle the issue]

VI. Conclusions and Recommendations
```

## Pattern 10: Creative/Practice-Based Research

### When to Use
- Art-based research: Generating knowledge through artistic creation
- Design research / research through design: Generating knowledge through the design process
- Practice-based / practice-led research: Practice itself is the research method
- When research questions involve creative practice, design thinking, or artistic inquiry

### Differences from Traditional Academic Research
- **Output format**: Can be a creative work + dissertation (not just a dissertation)
- **Knowledge type**: Values practical knowledge (tacit knowledge) and embodied knowledge
- **Process as method**: The creative/design process itself is the research method, not merely the object of study
- **Subjectivity**: The researcher's subjective experience is a legitimate source of knowledge, but requires systematic reflection

### Design Template
```
Research Question: What knowledge emerges through the practice of [creative activity] in [context]?

Protocol:
1. Reflective Practice
   - Define research question and creative intention
   - Establish reflective framework (e.g., Schön's reflection-in-action / reflection-on-action)
   - Confirm researcher positioning (insider / practitioner-researcher)
2. Process Documentation
   - Studio journal / design diary
   - Process video/audio documentation
   - Iteration version records (sketches, drafts, prototypes)
   - Decision point documentation: Why this approach and not another?
3. Contextual Analysis
   - Situate the creative process within disciplinary/cultural/historical context
   - Engage in dialogue with existing works/theories
   - Identify themes and insights emerging from the creative process
4. Knowledge Articulation
   - Transform tacit knowledge into communicable forms
   - Build bridges from practice to concepts
   - Distill transferable principles or frameworks
5. Presentation of Findings
   - Work presentation (exhibition, performance, prototype demonstration)
   - Written discourse (exegesis / critical commentary)
   - Integrate the relationship between work and discourse

Quality Criteria:
- Depth of reflection: Not just describing "what was done," but analyzing "why it was done this way" and "what was learned"
- Creative process transparency: Readers can understand the complete path from problem to work
- Clarity of knowledge contribution: Clearly state what this research contributes to knowledge
- Contextualization quality: The work does not exist in isolation but engages with the discipline
- Methodological reflexivity: The researcher is aware of their own role and biases
```

### Practice-Based Research Documentation Template
```
Phase 1: Positioning
- Research question:
- Creative intention:
- Researcher positioning (practitioner / observer / participant):
- Theoretical framework:

Phase 2: Process
| Iteration | Date | Action | Reflection | Turning Point |
|-----------|------|--------|------------|---------------|
| v1        |      |        |            |               |
| v2        |      |        |            |               |
| v3        |      |        |            |               |

Phase 3: Outcomes
- Work description:
- Knowledge contribution:
- Transferable principles/frameworks:
- Recommendations for future practice/research:
```

## Pattern 11: Archival Empirical Research (Accounting / Finance)

### When to Use
- Research questions about financial reporting, audit quality, earnings management, disclosure, or executive compensation using large-sample accounting data
- Testing causal hypotheses using naturally occurring variation in financial databases (Compustat, CRSP, EDGAR, Audit Analytics)
- Exploiting regulatory events, accounting standard changes, or economic shocks as quasi-natural experiments

### Distinction from General Empirical Research
- **Data source**: Compustat, CRSP, EDGAR, Audit Analytics — not surveys or lab data
- **Identification**: Causal identification is the defining challenge; reviewers at top accounting journals demand it
- **Sample construction**: Explicit data merge steps (e.g., CRSP-Compustat CCM link); exclusion criteria must be justified
- **Standard controls**: Firm size (log assets), leverage, ROA, book-to-market, growth (sales change), loss indicator, firm age — omitting standard controls raises red flags

### Design Template
```
Research Question: Does [treatment/event] affect [accounting/financial outcome]?

Protocol:
1. Theory Development
   - Identify the economic mechanism linking treatment to outcome
   - Generate directional predictions (hypotheses) grounded in agency theory,
     information asymmetry, contracting theory, or institutional theory
   - Distinguish from prior literature: what is the incremental contribution?

2. Sample Construction
   - Define base sample (e.g., Compustat annual, 2000-2022, U.S. firms)
   - Apply standard exclusions: financial firms (SIC 6000-6999), utilities (SIC 4900-4999),
     missing data, outliers (winsorize at 1%/99%)
   - Document all exclusion criteria and resulting sample size at each step
   - Merge additional databases: CRSP (returns), Audit Analytics (audit data), EDGAR (textual)
   - Describe final sample: firm-year obs, number of unique firms, time period

3. Variable Measurement
   - Dependent variable: justify operationalization (e.g., discretionary accruals via
     modified Jones model, audit quality via Big 4 indicator, AQ via Dechow-Dichev model)
   - Treatment/independent variable: define precisely, address measurement error
   - Control variables: include standard set for the outcome domain; cite precedents

4. Identification Strategy
   - Main approach: OLS/logit/probit with firm, year, and industry fixed effects
   - Causal identification (choose one or more):
     a. Difference-in-differences (DID): identify treatment and control groups; verify
        parallel trends pre-treatment
     b. Regression Discontinuity (RDD): exploit regulatory or size thresholds
     c. Instrumental Variable (IV): identify valid instrument; test relevance + exclusion
     d. Natural experiment: law change, regulatory shock, accounting standard adoption
   - Address endogeneity: self-selection, reverse causality, omitted variables

5. Estimation
   - Primary regression: define the estimating equation explicitly
   - Standard errors: cluster by firm and year (Petersen 2009)
   - Fixed effects: firm FE, year FE (or industry × year FE for more demanding tests)
   - Report economic significance (effect size), not just statistical significance

6. Robustness and Sensitivity
   - Alternative variable operationalizations
   - Alternative sample periods or subsamples
   - Entropy balancing or PSM if selection is a concern
   - Placebo tests (pre-treatment periods, pseudo-treatments)
   - Addressing parallel trends violations (Sun & Abraham 2021 for staggered DID)

7. Cross-Sectional Analyses
   - Test whether the main effect is stronger/weaker in predicted subsamples
   - Provides evidence on the economic mechanism (not just whether, but why)

Quality Criteria:
- Identification clarity: Can the reader understand exactly why this is causal?
- Data transparency: Sample construction fully reproducible from the description
- Parallel trends: If DID, pre-treatment trend tests reported (event-study plot preferred)
- Robustness: Main inference holds across at least 3 alternative specifications
- Economic significance: Effect sizes translated to real-world magnitude
- Literature positioning: Contribution table showing how this extends at least 2 prior papers

Reporting Standards: No EQUATOR standard specific to archival accounting; follow conventions
of target journal (TAR, JAR, JAE) — typically Table 1 (descriptive stats), Table 2 (correlations),
Table 3 (main results), Table 4+ (robustness / cross-sectional)
```

### Standard Table Structure (Accounting Archival Paper)
```
Table 1: Sample Selection and Descriptive Statistics
Table 2: Pearson/Spearman Correlation Matrix (flag 5% significance)
Table 3: Main Regression Results (OLS/logit; multiple columns varying FE)
Table 4: Robustness Tests (alternative measures, alternative samples)
Table 5: Cross-Sectional Analysis (mechanism / heterogeneity tests)
[Optional] Table 6: Additional Tests / Supplementary Analysis
```

---

## Pattern 12: Design Science Research (DSR)

### When to Use
- Creating and evaluating purposeful IT artifacts (systems, models, frameworks, algorithms)
- Accounting Information Systems (AIS), audit analytics tools, XBRL implementations, decision support
- When the research goal is to solve a real-world problem by building something, not just describing it

### Distinction from Other Patterns
- **vs. Technology Requirements Analysis (Pattern 8)**: DSR produces a generalizable knowledge contribution (design theory or design principles), not just a system for a specific client
- **vs. Exploratory Research (Pattern 6)**: DSR has a normative (prescriptive) goal — how to build things better — not just descriptive
- **vs. Empirical Research**: The artifact itself is a research output; evaluation is built in, not added at the end

### Design Template
```
Research Question: How can [artifact] be designed to improve [outcome] in [context]?

Protocol (Hevner et al. 2004 / Peffers et al. 2007 DSRM):

1. Problem Identification and Motivation
   - Define the specific problem; justify its importance to practitioners and researchers
   - Establish that existing solutions are inadequate
   - Identify the knowledge gap (what design knowledge does not yet exist?)

2. Objectives of a Solution
   - Specify what a successful artifact must accomplish (functional and non-functional requirements)
   - Derive objectives from the problem definition and prior knowledge

3. Design and Development
   - Define artifact type: construct (vocabulary), model (abstraction), method (algorithm/process),
     instantiation (implemented system), or design theory
   - Apply relevant kernel theories (e.g., agency theory for fraud detection systems, information
     processing theory for dashboard design)
   - Document design decisions and trade-offs

4. Demonstration
   - Deploy the artifact in one or more use cases or case studies
   - Show that the artifact can solve the problem (proof of concept)

5. Evaluation
   - Assess how well the artifact solves the problem (effectiveness, efficiency, utility)
   - Methods: controlled experiment, case study, simulation, expert panel, field study
   - Map evaluation method to research question type

6. Communication
   - Generalize findings: what design principles or design theory emerge?
   - Articulate contribution to IS knowledge (not just "we built a system")

Quality Criteria:
- Design relevance: Does the artifact address a real, important problem?
- Design rigor: Is it grounded in kernel theories from reference disciplines?
- Design utility: Does evaluation demonstrate improvement over existing solutions?
- Generalizability: Are design principles transferable beyond the specific instantiation?
- Novelty: Does the artifact represent a new form of the solution?

Reporting Standards: DESRIST guidelines; AIS Transactions on Replication Studies for AIS context
```

---

## Pattern 13: Machine Learning Research

### When to Use
- Developing predictive models for accounting or auditing outcomes (fraud detection, bankruptcy, misstatement prediction)
- Building text analysis pipelines on financial disclosures (10-K, MD&A, earnings calls, comment letters)
- Comparing ML model performance against traditional statistical benchmarks
- Applying NLP, deep learning, or ensemble methods to accounting/finance problems

### Distinct Contribution Types
- **Methodological**: A new model or approach that outperforms existing methods on a benchmark task
- **Application**: Applying established ML methods to a new accounting domain with substantive findings
- **Theory-informed**: Using interpretable ML to uncover mechanisms (e.g., SHAP values explaining audit risk drivers)

### Design Template
```
Research Question: Can [ML approach] improve [prediction/classification] of [accounting outcome]?

Protocol:

1. Problem Framing
   - Define the prediction/classification target (e.g., fraud, going concern, material weakness,
     earnings management, credit rating)
   - Establish why ML is appropriate: large feature space, nonlinear relationships, textual data,
     or pattern detection at scale

2. Data Construction
   - Define sample and time window; justify train/test split (avoid look-ahead bias)
   - Feature engineering: financial ratios, text features (TF-IDF, word embeddings, FinBERT),
     audit variables, governance indicators
   - Address class imbalance: SMOTE, class weighting, or anomaly detection framing
   - Document all preprocessing steps for reproducibility

3. Model Selection and Baseline
   - Candidate models: logistic regression (baseline), Random Forest, XGBoost, LSTM, BERT/FinBERT
   - Always include a traditional accounting model as baseline (e.g., Beneish M-Score, Altman Z-Score,
     F-Score for earnings manipulation)
   - Justify model complexity relative to sample size and interpretability needs

4. Validation Strategy
   - Preferred: out-of-time validation (train on years T-n to T-k; test on T-k+1 to T)
   - If cross-validation: use time-series CV (not k-fold, which leaks future data)
   - Report: AUC-ROC, precision, recall, F1, accuracy — not just accuracy
   - Statistical significance testing: DeLong test for AUC comparison; bootstrap CIs

5. Interpretability and Mechanism
   - Variable importance: SHAP values (preferred), permutation importance, partial dependence plots
   - Connect top features to accounting theory (why should auditors care about feature X?)
   - Distinguish statistical prediction from causal claims

6. Robustness
   - Sensitivity to hyperparameter choices (grid search or Bayesian optimization)
   - Performance across sub-periods, industry groups, or firm size quartiles
   - Comparison to simpler models (does complexity justify marginal gain?)

7. Practical Implications
   - Decision threshold analysis: at what probability cutoff does the model add value?
   - False positive / false negative cost asymmetry (especially for audit risk applications)
   - Implementation constraints: data availability at decision time, auditor judgment integration

Quality Criteria:
- No data leakage: future information must not contaminate training data
- Proper baseline: comparison against established accounting models, not just naive benchmarks
- Interpretability: top predictors are explained in accounting terms, not just listed
- Reproducibility: code, data sources, and hyperparameters fully documented
- Economic significance: predictive improvement translates to meaningful decision value
- Honest evaluation: test-set performance reported, not tuned test-set performance

Reporting Standards: Checklist from Kapoor & Narayanan (2022) "Leakage and the Reproducibility
Crisis in ML-based Science" recommended; ACM FAccT principles for fairness-relevant applications
```

---

## Choosing the Right Pattern

```
What type of question?
├── "What is known?" → Systematic Literature Review (Pattern 1)
├── "How do cases compare?" → Comparative Case Study (Pattern 2)
├── "Is this policy working?" → Policy Analysis (Pattern 3)
├── "What's happening and why?" → Mixed Methods (Pattern 4)
├── "What do documents reveal?" → Content Analysis (Pattern 5)
├── "How is this experienced?" → Exploratory Research (Pattern 6)
├── "How do we compare?" → Benchmarking Study (Pattern 7)
├── "Which technology should we use?" → Technology Requirements Analysis (Pattern 8)
├── "What does the law say?" → Legal Case Analysis (Pattern 9)
├── "What knowledge emerges from practice?" → Creative/Practice-Based Research (Pattern 10)
├── "Does X affect earnings/audit quality/disclosure?" → Archival Accounting Research (Pattern 11)
├── "How can we build an artifact to solve this problem?" → Design Science Research (Pattern 12)
└── "Can ML predict/detect this accounting outcome?" → Machine Learning Research (Pattern 13)

More nuanced decision:
├── Technology assessment related
│   ├── Comparing different technology options → Pattern 8 (Technology Requirements Analysis)
│   ├── Comparing technology adoption across organizations → Pattern 2 (Comparative Case Study)
│   └── Building an AIS artifact with generalizable design theory → Pattern 12 (Design Science)
├── Law/policy related
│   ├── What legal texts prescribe and how courts interpret them → Pattern 9 (Legal Case Analysis)
│   └── Whether a policy is effective and how to improve it → Pattern 3 (Policy Analysis)
├── Creative/design related
│   ├── Generating knowledge through the creative process → Pattern 10 (Creative/Practice-Based Research)
│   ├── Understanding the experience of creators → Pattern 6 (Exploratory Research)
│   └── Analyzing creative texts/works → Pattern 5 (Content Analysis)
├── Accounting/auditing related
│   ├── Large-sample financial database research with causal claim → Pattern 11 (Archival Accounting)
│   ├── Building fraud detection or audit analytics tools → Pattern 12 (Design Science) or Pattern 13 (ML)
│   ├── Predicting restatements, going concern, or ICW → Pattern 13 (Machine Learning)
│   └── Analyzing SEC comment letters or 10-K text at scale → Pattern 13 (ML) or Pattern 5 (Content Analysis)
└── Uncertain
    ├── New topic with scarce literature → Pattern 6 (Exploratory Research)
    ├── Complex problem requiring multiple data types → Pattern 4 (Mixed Methods)
    └── First see how others have approached it → Pattern 1 (Systematic Literature Review)
```
