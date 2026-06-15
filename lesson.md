# Lesson — L02 Probability & Statistics for Machine Learning

> **Chapter 2 of the NorthStar Retail story.** *Sarah Chen · Customer Experience Analyst · January 2023.*
> Friday afternoon, Priya asked: *"Your model says 60% of reviews are positive. But are the positive ones actually positive? How do we know we can trust that number?"*
> Sarah didn't have an answer. This lesson is how she gets one.

This document is a **short reference** — the lesson itself is taught in the notebooks. Read it for orientation before class, then come back to it for the takeaways, the honest-reporting checklist, the review questions, and the course map.

---

## How L02 is taught

| Stage | Where to go |
|---|---|
| **Pre-class** | `pre-class.md` + `notebooks/01_monday_morning.ipynb` |
| **In-class — Part 1: Distributions** | `notebooks/02_distributions.ipynb` |
| **In-class — Part 2: CLT + Confidence Intervals** | `notebooks/03_confidence_intervals.ipynb` |
| **In-class — Part 3: Hypothesis Testing (A/B testing as worked example)** | `notebooks/04_ab_testing.ipynb` |
| **Self-study** | `notebooks/assignment.ipynb` + `notebooks/optional_extensions.ipynb` |
| **Reference & review** | This document |

The notebooks are the spine. Run them in order. Come back here for the consolidated takeaways and the review questions.

---

## Overview

Sarah's L01 model said "60% positive" — but that was a single number computed from one batch of 10,000 reviews. Priya's question, *how sure are we?*, is the question that probability and statistics exist to answer. By Friday Sarah will hold three new tools: **distributions** (to read the shape of any column of data), **confidence intervals** (to put an honest range around any number she reports), and **hypothesis testing with p-values and effect size** (to decide whether an intervention actually changed anything, or whether the apparent difference is just noise — with A/B testing as the worked example). Every model evaluation, every business experiment, every dashboard number for the rest of the course is read through these three lenses.

---

## Key takeaways

1. **A single number is never the whole story — the distribution behind it is.** Before you trust a mean, look at the shape. A right-skewed distribution makes the mean overstate the typical case; report the median or segment the data.
2. **Z-scores normalise "is this unusual?" across any scale.** `z = (value − mean) / sd`. |Z| > 3 is the working definition of an outlier worth investigating.
3. **The Central Limit Theorem is why statistics works on messy data.** Even when the underlying data is skewed, the *distribution of sample means* approaches normal as the sample grows. Rule of thumb: n ≥ 30 and you can use normal-based formulas safely.
4. **Every reported number from a sample needs a confidence interval.** "84% accuracy" is half a fact. "84% (95% CI: 78–89%)" is the honest version. To halve the CI width you must quadruple the sample size — uncertainty has a price.
5. **The 95% in "95% CI" is about the method, not this one interval.** If you computed CIs this way 100 times, ~95 of them would contain the true value. You cannot assign a probability to whether this specific interval does.
6. **A p-value answers a precise question: "could chance alone produce a difference this large?"** p < 0.05 → reject the no-effect story. p ≥ 0.05 → not enough evidence to reject; this is *not* the same as proving no effect.
7. **Statistical significance ≠ practical significance.** With a large enough sample, a 0.01% difference becomes "significant." Always report effect size alongside the p-value, and let the business decide whether the effect is worth acting on.

---

## Honestly reporting a number — a checklist

Before you cite a number from data — in a slide, an email, a dashboard — run it through this three-step check:

1. **What is the shape of the data behind this number?** If the distribution is skewed, the mean may mislead. Report the median, segment the data, or be explicit about which summary you chose and why.
2. **What range is the true value likely in?** Any number computed from a sample needs a confidence interval. "84% accuracy" alone is dishonest by omission. "84% (95% CI: 78–89%) on 200 hand-labelled reviews" is defensible.
3. **Could this difference be random variation?** If you are comparing two groups (with vs without an intervention), you owe the reader both a p-value *and* an effect size. Either one on its own can mislead.

Skip any of these and you have confident-sounding nonsense — the most expensive kind of mistake in business.

---

## <span style="color:green">[Opus 4.8]</span> Deep dive: "84% accuracy" vs "84% (95% CI: 78–89%)"

This unpacks Key Takeaway #4 line by line, because it is the single most important reporting habit in the course.

### Why "84% accuracy" is only half a fact

Sarah hand-labelled **200 reviews** and her model got **168 of them right**: 168 / 200 = **0.84 = 84%**. That 84% is a **point estimate** — one number computed from one sample.

The problem: those 200 reviews are just *one* draw from the millions Sarah could have picked. A *different* 200 reviews would have given a slightly different number — maybe 82%, maybe 86%. So 84% silently hides the question Priya actually cares about: *how close is this to the model's **true** accuracy on all reviews?* Reported alone, 84% **looks identical** whether it came from 20 reviews or 20,000 — yet those two deserve wildly different levels of trust. That missing precision is the "other half" of the fact.

### What the "(95% CI: 78–89%)" adds

The confidence interval is the **plausible range for the true accuracy**, given the sample size. "84% (95% CI: 78–89%)" reads as:

> *"My best single guess is 84%, and the true accuracy is most likely somewhere between 78% and 89%."*

The width of that range (about ±5 points) is a direct readout of **how much to trust the 84%**. Narrow CI → solid number. Wide CI → treat with caution. (For what the "95%" itself means — a property of the *method*, not this one interval — see Key Takeaway #5.)

### Where 78–89% comes from (the actual arithmetic)

For a proportion, the **standard error** (the typical sample-to-sample wobble) is:

```
SE = √( p·(1−p) / n )  =  √( 0.84 × 0.16 / 200 )  =  √0.000672  ≈  0.0259  =  2.59%
```

A 95% CI reaches out **1.96 standard errors** on each side (1.96 is the Z-score that brackets the middle 95% of a normal curve — the same standard-normal areas from the `02_distributions` notebook):

```
margin of error = 1.96 × SE = 1.96 × 2.59%  ≈  5.1%
95% CI = 84% ± 5.1%  =  78.9%  to  89.1%   →  rounded to 78–89%
```

So the interval is not a guess — it falls straight out of two inputs: **the estimate (84%)** and **the sample size (200)**.

### "Halve the width → quadruple the sample" — why uncertainty has a price

Notice `n` sits **under a square root** in the SE formula. That means the margin of error shrinks with `√n`, not with `n`. To make the interval **half as wide**, you must cut the SE in half, which needs **4× the data**:

| Sample size `n` | Margin of error (±) | 95% CI around 84% |
|---|---|---|
| 200 | ±5.1% | 78.9 – 89.1% |
| 800 (×4) | ±2.5% | 81.5 – 86.5% |
| 3,200 (×16) | ±1.3% | 82.7 – 85.3% |

Going from 200 → 800 reviews (4× the hand-labelling effort) only buys you *half* the uncertainty. This is the "diminishing returns" of data: the first few hundred labels are cheap and hugely informative; squeezing the interval tighter gets expensive fast. That trade-off — **precision costs effort, quadratically** — is exactly what Takeaway #4 means by "uncertainty has a price."

### The one-sentence version for an executive

> *"On 200 hand-checked reviews the model was right 84% of the time; allowing for the small sample, the true accuracy is most likely between 78% and 89%."*

---

## <span style="color:green">[Opus 4.8]</span> Deep dive: the p-value, and why the cut-off is 0.05

This unpacks Key Takeaway #6. We'll use Sarah's running example: NorthStar emails an **apology coupon** to some complaining customers (treatment) and not others (control), then compares complaint rates. The A/B test returns **p = 0.038**.

### What a p-value actually is

A p-value always starts from a deliberately boring assumption called the **null hypothesis (H₀): "there is no real effect — the coupon changes nothing, and any gap we see is just luck of the draw."**

The p-value then answers **one precise question:**

> *"If the coupon truly did nothing, how often would pure random chance still produce a difference at least as big as the one I measured?"*

So **p = 0.038 means: "If the coupon had zero effect, a result this large (or larger) would happen by chance only 3.8% of the time."** That is rare enough to make the "it was just luck" story hard to believe — so we doubt the null and conclude the coupon probably *does* something.

**Read the definition carefully — it is the most misread number in statistics:**
- ✅ p = P(data this extreme **given** the null is true).
- ❌ p is **not** the probability the null is true. "p = 0.038" does **not** mean "3.8% chance the coupon has no effect." It assumes the null and asks about the *data*, not the other way round.
- ❌ p is **not** the size of the effect. A tiny p can sit on a trivial effect (see Takeaway #7). It measures *evidence against "pure chance,"* not *importance*.

### How the number is computed (in one breath)

You measure the gap between the two groups, divide it by how much gap random sampling alone would typically produce (the standard error), and get a **test statistic**. The p-value is then the **tail area** of that statistic's distribution — literally the same "area in the tail of the curve" idea from the `02_distributions` notebook, just applied to the difference between two groups. Bigger measured gap, or bigger sample → statistic lands further into the tail → smaller p.

### Why 0.05? Convention, **not** calculation

This is the key thing to internalise: **0.05 is a chosen threshold, not a result the data computes.** It is the **significance level (α)** — a line *you* draw **before** running the test to decide how much "could be chance" risk you're willing to tolerate.

- Its origin is historical convenience, not mathematics: statistician **Ronald Fisher** popularised 0.05 in the 1920s simply as a round, reasonable "1 in 20" cut-off. There is no law of nature at 0.05.
- It is **arbitrary and context-dependent.** Particle physicists demand p < 0.0000003 (the "5-sigma" rule) before claiming a discovery; a low-stakes marketing test might accept 0.10. The right α depends on the **cost of a false alarm** versus the **cost of missing a real effect.**
- It must be fixed **in advance.** Picking the threshold *after* seeing the p-value (e.g. "0.07, let's just call the line 0.08") is a form of cheating called **p-hacking.**

So in our example the logic is: *we decided beforehand α = 0.05; the data produced p = 0.038; since 0.038 < 0.05, we cross the line we drew.*

### `p < 0.05` vs `p ≥ 0.05` — and the asymmetry that trips everyone up

| Outcome | Verdict | Plain English |
|---|---|---|
| **p < 0.05** (e.g. 0.038) | **Reject H₀** | "Chance alone is an unconvincing explanation. We have statistically significant evidence of an effect." |
| **p ≥ 0.05** (e.g. 0.12) | **Fail to reject H₀** | "Chance *could* plausibly explain this. We don't have enough evidence to claim an effect." |

The trap is the second row. **"Fail to reject" is not "prove there's no effect."** Absence of evidence ≠ evidence of absence. A p of 0.12 can happen because the coupon genuinely does nothing **or** because the effect is real but the sample was too small to detect it (an under-powered test). The honest sentence is:

> *"We did not find statistically significant evidence of an effect at the 0.05 level"* — never *"we proved the coupon does nothing."*

Note the deliberate wording in Takeaway #6: **"reject"** on one side, but only **"not enough evidence to reject"** on the other. Statistics can disconfirm the no-effect story; it can never fully confirm it.

### The one-sentence version for an executive

> *"If the coupon really did nothing, we'd see a swing this big only about 4% of the time — that's unlikely enough that we believe the coupon genuinely helps. (Next question: is the effect big enough to be worth it?)"*

---

## Check your understanding

Work through these after finishing the three Part notebooks. Attempt each question on your own first.

### Part 1 — Distributions

**Q1 — Which summary stat?** NorthStar's analysts report that the "average spend per order" is £85. You look at the data and notice the distribution is heavily right-skewed (a small number of very large corporate orders). Is £85 the right number to report to Priya? What would you suggest instead?

> **Sample answer:** No. Right-skewed data means a few large orders are pulling the mean up, making it unrepresentative of a typical customer. Report the *median spend per order* instead — it is resistant to those large outliers. Also consider segmenting: report the median for individual customers separately from corporate accounts. Give Priya both numbers with a sentence explaining why they differ.

**Q2 — Z-score intuition.** A product's daily return rate has a mean of 3.2% and a standard deviation of 0.8%. Today's return rate is 5.6%. Is this an anomaly worth investigating?

> **Sample answer:** Z = (5.6 − 3.2) / 0.8 = 3.0. A Z-score of 3.0 means today's rate is 3 standard deviations above the mean. In a normal distribution, only about 0.27% of days would fall this far out by chance — roughly 1 day per year. Yes, this is worth investigating: possible product defect, batch quality issue, or data error.

**Q3 — Distribution shape and the model.** You are training a fraud detection model. The transaction amounts in your dataset are extremely right-skewed (99% of transactions are under £500; 1% are very large). Why might this be a problem for training, and what could you do?

> **Sample answer:** The model may treat a £50,000 transaction as an extreme outlier in ways that distort learning — depending on the algorithm, one or two very large values can dominate the loss function. Common solutions: apply a log transformation to the amount (making the distribution more symmetric), or winsorise the data (cap extreme values at a threshold like the 99th percentile). Either approach reduces the influence of the long tail without discarding those transactions.

### Part 2 — Confidence Intervals

**Q4 — Narrow vs wide.** A model evaluated on 50 reviews has 80% accuracy (95% CI: 68–92%). Another model evaluated on 2,000 reviews also has 80% accuracy (95% CI: 78–82%). Which model evaluation do you trust more, and why?

> **Sample answer:** The second model's evaluation — not because the accuracy is different (both are 80%), but because the confidence interval is much narrower. The first CI (68–92%) spans 24 percentage points and includes both "barely acceptable" and "genuinely excellent" as possibilities. The second CI (78–82%) is tight enough to be useful for decisions. The only difference is sample size: 50 vs 2,000. This is why you should always report CIs alongside accuracy.

**Q5 — CLT application.** A colleague says: "The CLT only works if the original data is normally distributed." Is this correct?

> **Sample answer:** No — this is backwards. The CLT says that sample means approach a normal distribution regardless of the shape of the underlying data. The underlying data can be skewed, bimodal, or whatever else — as long as your samples are large enough (n ≥ 30 is the rule of thumb), the distribution of sample means will be approximately normal. That is precisely what makes the CLT so powerful.

**Q6 — Interpretation.** Sarah reports "84% (95% CI: 78–89%)." Priya asks: "If we ran this test again with 200 new reviews, would we get exactly 84% again?" How should Sarah answer?

> **Sample answer:** Probably not. The CI (78–89%) is Sarah's way of saying: with different samples, the accuracy would probably fall somewhere in this range. If Priya ran the test 100 times with different samples of 200 reviews, she'd expect about 95 of those tests to produce a CI that contains the true accuracy — and the point estimates would vary. The 84% is the best estimate from this particular sample; the CI tells her how much to trust it.

### Part 3 — Hypothesis Testing

**Q7 — Design the test.** NorthStar wants to test whether a new "easy returns" banner on the product page reduces returns (by setting better expectations before purchase). Design the A/B test: what are the control and treatment groups? What is the outcome metric? What would make you conclude the banner "works"?

> **Sample answer:** Control group: customers who see the product page without the banner. Treatment group: customers randomly assigned to see the product page with the "easy returns" banner. Outcome metric: return rate within 30 days of purchase (one metric — not revenue, satisfaction, and returns simultaneously). Conclusion: the banner "works" if the treatment group's return rate is lower than the control group's, with a p-value below 0.05. Also report the effect size: a 0.1pp reduction vs a 3pp reduction have very different business implications even if both are significant.

**Q8 — p-value quiz.** An A/B test produces p = 0.001. A colleague says "this is very statistically significant, so we should definitely roll out the change." What question should you ask before agreeing?

> **Sample answer:** "What is the actual size of the effect?" A p-value of 0.001 with a very large sample might correspond to a 0.01% difference in conversion rate — statistically rock-solid but practically worthless. Before rolling out, ask: how large was the measured improvement? Does it justify the development cost and any risks of the change? Statistical significance does not imply business significance.

**Q8b — Effect size check.** Two experiments both produce p < 0.05. Experiment A improves conversion from 10.0% to 10.1%. Experiment B improves conversion from 10.0% to 12.5%. Why is it misleading to treat these two results as equally important?

> **Sample answer:** Because statistical significance only tells us the difference is unlikely to be due to chance alone. It does not tell us whether the difference is large enough to matter. Experiment A shows a tiny effect that may be too small to justify action, while Experiment B shows a much larger effect that is more likely to matter in practice. This is why every p-value should be read together with an effect size.

**Q9 — Mis-reading check.** An experiment produces p = 0.12. Your manager says "the null hypothesis is confirmed — there's no effect." Correct their interpretation.

> **Sample answer:** The p-value of 0.12 means we failed to reject the null hypothesis — we don't have sufficient statistical evidence of an effect. But failure to find evidence is not evidence of no effect. The sample may have been too small, or the effect too small to detect at this sample size. The correct statement is: "We did not find statistically significant evidence of an effect at the 0.05 level. We cannot conclude the intervention does nothing — we conclude only that this test was not powerful enough to detect it."

**Q10 — End-to-end.** Sarah's Friday presentation has three numbers: (a) 60% sentiment positive rate, (b) 84% model accuracy (95% CI: 78–89%), (c) coupon A/B test p = 0.038. For each number, write one sentence that correctly interprets it for a non-technical executive audience.

> **Sample answer:**
> **(a)** "In this week's sample of 10,000 reviews, 60% were classified as positive — though this figure should be taken as an estimate, not a precise count, because the model occasionally misclassifies borderline reviews."
> **(b)** "When we checked the model against 200 reviews labelled by hand, it was correct 84% of the time; our statistical analysis suggests the true accuracy is most likely somewhere between 78% and 89%."
> **(c)** "We found strong statistical evidence that the apology coupon reduces complaint rates — results this large would occur by chance less than 4% of the time if the coupon had no effect — so we recommend proceeding with a cautious roll-out."

---

## Where L02 fits in the course

L02 is the lens every later lesson is read through — whenever you report a model number, claim a difference, or detect an anomaly, you are using L02 tools.

| Lesson | How L02 shows up |
|---|---|
| **L03 — Supervised Learning** | Train/validate split metrics are sample statistics — every accuracy/precision/recall number needs a CI. The threshold-choice exercise is an effect-size question. |
| **L04 — Supervised Learning (Advanced)** | Hyperparameter tuning compares many model variants; you'll use confidence intervals to decide whether one really beats another or just got a lucky split. |
| **L05 — Unsupervised Learning** | Anomaly detection extends the one-sample hypothesis test logic from L02 (Z-score generalisation). Cluster quality metrics are sample statistics with CIs. |
| **L06 — Time Series** | Forecast intervals are confidence intervals projected forward. Distributional shape determines whether your forecast is honest. |
| **L07 — Neural Networks** | Validation loss curves are noisy samples; you need CIs to tell whether one architecture genuinely beats another. Comparing two models on the same validation set uses a paired t-test — same hypothesis testing framework, different test statistic. |
| **L08 — Computer Vision** | Test-set accuracy on a held-out image set is a sample proportion — same CI math. Model comparison on the same test set uses a paired test. |
| **L09 — NLP & Embeddings** | Retrieval evaluation (precision@k, recall@k) is sampled and needs CIs. |
| **L10 — Transformers & GenAI** | Hypothesis testing of prompts and retrieval strategies is the *only* way to make rigorous claims about an LLM pipeline. If outcomes are binary (pass/fail per query), use a chi-square test; if using LLM-judge scores on the same prompt set, use a paired t-test. |

---

> *"OK, the sentiment model holds up. But you used a pre-trained one — off the shelf. Can you build us a model that predicts churn from our own customer data? Something we actually trained on NorthStar behaviour?"* — Marcus, after Sarah's Friday presentation.
>
> That question — *can I build a model?* — is the engine of **L03 (Supervised Learning)**.
