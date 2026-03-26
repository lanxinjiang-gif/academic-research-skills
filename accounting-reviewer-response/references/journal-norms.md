# Journal Norms for Top Accounting Journals

What editors, AEs, and senior reviewers at the top accounting journals expect. Calibrate your contribution claims, framing, and response strategy against these norms.

---

## The Five Top Journals at a Glance

| Journal | Abbrev. | Publisher | Scope emphasis |
|---------|---------|-----------|----------------|
| The Accounting Review | TAR | AAA | Broad; theory + empirics; foundational |
| Journal of Accounting Research | JAR | Wiley / Chicago | Rigorous empirics; broad methodology |
| Journal of Accounting and Economics | JAE | Elsevier | Capital markets, contracting, empirics |
| Journal of Accounting, Auditing & Finance | JAAF | SAGE | Broader scope; methodological variety |
| Contemporary Accounting Research | CAR | CPA Canada / Wiley | Canadian + international perspective; broad |
| Review of Accounting Studies | RAS | Springer | Theoretical + empirical; policy-relevant |

Also top-tier (finance-adjacent): *Journal of Finance*, *Journal of Financial Economics*, *Review of Financial Studies* (accept accounting papers on capital markets topics).

---

## Common Editorial Philosophies

### What all top journals share

1. **Contribution clarity** — The paper must answer a clearly stated, important question. "We do X because nobody has done X" is insufficient; "We answer Q, which matters because [economic/policy/social reason]" is what editors want.

2. **Tight identification** — Reviewers will probe the causal interpretation. The best papers either use a clean natural experiment or are explicit and careful about what is and isn't causal.

3. **Economic magnitude** — Statistical significance is not enough. Papers that show statistically significant but economically trivial effects face pushback.

4. **Honest engagement with limitations** — Top journals reward papers that clearly articulate their limitations. Trying to paper over limitations triggers skepticism.

5. **In-sample and out-of-sample consistency** — Results that only hold in-sample but not out-of-sample (for predictive papers) or in narrow samples face serious scrutiny.

---

## Journal-Specific Signals

### The Accounting Review (TAR)
- Traditional emphasis on theory-based hypotheses; empirics should be tightly linked to theory
- Value "fundamental" contributions — papers that change how we think about a phenomenon
- Heavy emphasis on measurement validity; if you introduce a new measure, validate it thoroughly
- Reviewers often request: additional theory-based predictions, tests of the mechanism, and evidence that the finding is not a measurement artifact
- **For ML/prediction papers at TAR**: practical implications are essential. Showing a model works statistically is not enough — you must demonstrate that the improved accuracy matters for real stakeholders. The standard approach is separate stakeholder-specific tests for investors (trading strategy), managers (internal controls), auditors (abnormal fees), and regulators (SEC investigations). See analysis-playbook.md Section 16.
- **Detection vs. prediction at TAR**: if your paper does something conceptually distinct from a close predecessor (e.g., prediction vs. detection of misstatements), TAR reviewers will push you to clarify the conceptual difference empirically — not just in theory. Show that the distinction matters by comparing performance or economic outcomes across tasks.

### Journal of Accounting Research (JAR)
- Broad methodological tolerance — experimental, archival, analytical, ML all welcome
- Strong emphasis on research design rigor and out-of-sample validity
- Editors often actively involved in revision process (more so than other journals)
- The "JAR Conference" model: papers sometimes invited to present at the annual conference as part of the review process
- Reviewers tend to push hard on: identification strategy, look-ahead bias, overfitting, and whether gains are economically meaningful

### Journal of Accounting and Economics (JAE)
- Strong emphasis on capital markets, contracting, and information economics
- Papers tend to be tightly focused — one main contribution, well-executed
- Very skeptical of overly speculative mechanism discussion; want direct evidence of the mechanism
- Commonly requested robustness: alternative proxies, sub-period analysis, industry effects, controlling for related constructs

### Contemporary Accounting Research (CAR)
- More receptive to international settings, auditing, and management accounting papers
- Empirical standards similar to TAR/JAR but slightly more flexible on identification
- AEs play an active advisory role

### Review of Accounting Studies (RAS)
- Mix of theory and empirics; both modeling and archival work welcome
- Good outlet for papers with important but subtle contributions
- Reviewers tend to be rigorous on: model assumptions, comparative statics, empirical implementation of theory

---

## The Associate Editor (AE) Role — How to Read and Respond

The AE is your most important reader during the revision process.

### What AEs do
- Synthesize reviewer concerns and translate them into actionable guidance
- Signal what is required for acceptance (as opposed to what would be "nice to have")
- Often push back on reviewers who they think are overreaching
- May disagree with reviewers and signal this; use this to calibrate your response

### Reading AE language

| AE says... | What it usually means |
|------------|----------------------|
| "I find it very confusing that..." | This needs to be rewritten from scratch |
| "I am more open than the reviewer..." | You have an ally; focus on satisfying the AE |
| "The paper would benefit from..." | Should-do (will strengthen, not required) |
| "The paper needs to address..." | Must-do |
| "I suggest moving X to the appendix" | Do exactly this |
| "I think the paper's contribution is X" | Adopt this framing |
| "I am not excited by this literature..." | Be transparent about limitations; don't oversell |
| "The revision is much clearer" (in R2) | You're close; don't break what's working |
| "Both referees appreciate X but have questions about Y" | Y is the gating issue for this round |

### Responding to the AE

- Thank the AE specifically and separately from reviewers
- Address AE comments first in the response memo (they carry the most weight)
- When the AE and reviewer disagree, you can note this explicitly and explain whose guidance you followed (usually the AE's)
- If the AE made an error or misunderstood something, correct it gently: "We appreciate the AE's reading of [X]. We would like to clarify that..."

---

## The Incremental Contribution Battle

One of the most common and frustrating reviewer patterns: the paper improves on a specific close predecessor, and reviewers question whether the improvement is meaningful, fairly measured, or worth a separate paper.

**What the reviewer is actually asking:**
1. *Is the literature on this topic truly limited?* (even if one major paper exists)
2. *Is your improvement substantial under the most conservative comparison?*
3. *Does the improvement matter for anyone?* (practical significance, not just statistical)

**The standard two-pronged response:**

### Prong 1: Frame the literature gap
Even if one close paper exists, the topic may be underexplored relative to its importance. Show that:
- The literature on [your topic] is small relative to related literature on [adjacent topic]
- The close predecessor "falls short in" or "focuses only on [detection/descriptive/one-year]"
- "Despite [paper X], [your topic] remains underexplored because [concrete reason]"

Do this in the Introduction and contribution section with specific language, not just a vague claim. Reference the actual papers and explain what each does and doesn't do.

### Prong 2: Quantify the improvement under conservative comparison
The reviewer often suggests the most optimistic reading of the benchmark. Match it:
- Identify the "optimistic benchmark" scenario the reviewer points to
- Show that *under that same optimistic benchmark*, your model still outperforms substantially
- Report the percentage improvement explicitly: "Our model improves ROC-AUC by X% over the optimistic benchmark"
- Then show the improvement under the proper apples-to-apples comparison (same information availability, same variable set) — this is usually even larger

See analysis-playbook.md Section 18 for the detailed technique.

### Prong 3: Show the improvement matters practically
For each claimed improvement in predictive accuracy, demonstrate that the improvement translates to real-world value for at least one stakeholder group. An improvement from AUC 0.65 to 0.83 means nothing unless you show what that difference implies for investor returns, audit fee prediction, or regulatory efficiency.

---

## Common Traps in Top-Journal Revisions

### Overclaiming causality
- Phrase results as "associated with" not "causes" unless you have clean identification
- If reviewers push on causality, acknowledge limitations honestly rather than defending a causal interpretation you can't support

### Kitchen-sink robustness checks
- Adding 15 robustness checks can obscure which ones actually matter
- Better: select 2–3 most important alternatives; note others in a footnote or IA table

### Responding to the letter but not the spirit
- If the AE asks you to reframe the contribution, actually reframe it — don't just add a paragraph saying "our contribution is now X" while leaving the rest of the paper unchanged
- Reviewers read the manuscript, not just the response memo; changes must be visible in the manuscript

### Defensive writing
- Every sentence defending a prior choice signals that you are not taking the concern seriously
- The correct posture: acknowledge the concern genuinely, explain your updated approach, point to the evidence

### Over-revising
- In R2+, the paper is nearly done; don't make sweeping changes that open new questions
- Focus on clarifying and strengthening; the AE will note if the paper has become less coherent

---

## Round-Specific Strategy

### R1 Strategy
- This is the major revision round — expect to do significant empirical work
- Prioritize: (1) AE's must-do items, (2) methodological concerns that threaten the identification story, (3) empirical completeness requests
- Don't sacrifice clarity for comprehensiveness — a cleaner, tighter paper often does better than a more comprehensive messy one
- Set a realistic timeline: top journals often allow 6–12 months for R1

### R2 Strategy
- You are now in the home stretch — don't break what's working
- Respond to every remaining comment carefully; small misses can delay acceptance
- Where the AE signals conditional acceptance, frame your response as "we have addressed all remaining concerns"
- Be explicit about the changes made: "In response to [comment], we have revised [specific location] to [specific change]"
- The response memo at R2 should be shorter and more targeted than at R1
- Use the R2 multi-round opening structure from response-language.md (appreciate prior assessment + bulleted list of improvements)

### R3 and Beyond
- Rare at top journals; signals that something fundamental is still unsatisfying
- If you receive an R3, step back and ask: what is the one thing they are still unsatisfied with?
- Consider asking a trusted colleague to read both the manuscript and the review history fresh

---

## On Framing "Limits" Findings

A paper that rigorously shows that a promising approach has limited gains is publishable and valuable — sometimes more so than a paper that overclaims improvement.

**How to frame this positively:**
> "We show that machine learning substantially improves the functional form specification of accrual models, but that detection of earnings management remains limited. This suggests the binding constraint is not model misspecification, but unobserved heterogeneity in accrual determinants — a finding that reorients future research toward collecting better data rather than building better models."

This framing:
- Answers a clear question
- Has a definitive, surprising finding
- Points to implications for future research
- Does not oversell the magnitude of improvement
