# L02 — Probability & Statistics for Machine Learning

> *Sarah Chen's second week at NorthStar Retail. Priya asked the hard question on Friday: "How sure are we?" Now Sarah has to learn to defend her number.*
> By the end of this lesson you will know how to read and describe any distribution of data, put a confidence interval around any estimate, and design and interpret an A/B test — the three statistical tools every ML result stands on.

---

## Before you start — environment setup

> **If this is your first time with this course, do this before anything else.**
>
> Follow the [**Setup Guide →**](./setup.md) to install the Python environment. It takes 10–15 minutes. The same environment works for all 10 lessons.
>
> **Already set up from L01?** Your `dsai-m3` environment should already have everything. If you get an `ImportError` for `scipy`, see the [Setup Guide](./setup.md) for a one-line fix.

---

## Where L02 fits

| Lesson | What you build | What you carry forward |
|---|---|---|
| **L01 — Intro to ML** | Run a sentiment model on 10,000 reviews; classify each as positive or negative | A working model — and Priya's unanswered question: *"How sure are we?"* |
| **L02 — Probability & Statistics** *(you are here)* | The formal tools to answer Priya's question: distributions, confidence intervals, A/B testing | The statistical lens you will use to judge every model from L03 onward |
| **L03 — Supervised Learning** | Train your first model from labelled data | Cross-validation and confusion matrices read in the statistical terms you learn here |

**The narrative thread:** Sarah produced a number in L01. In L02 she has to *defend* it — and learn to test whether interventions actually move outcomes.

---

## What you will be able to do by the end

- **Read** a distribution shape (normal, skewed, bimodal) and explain why it changes how a model is built and how a result is reported
- **Compute and interpret** a confidence interval around a sample statistic and articulate what it does and doesn't say
- **Design and read** a basic A/B test, including the p-value, confidence interval, effect size, its assumptions, and the most common mis-readings
- **Choose between** descriptive and inferential statistics for a given business question
- **Recognise** the Central Limit Theorem at work and use it to explain why sample means behave well even when the underlying data does not

---

## How class time is structured (~3 hrs)

| Phase | Time | Format |
|---|---|---|
| Concept walkthrough | ~90 min | Instructor presents core concepts; learners follow along on the [**interactive key-concepts page**](https://su-ntu-ctp.github.io/6m-data-3.2-Probability-Statistics-for-Machine-Learning/) |
| Hands-on code-alongs | ~90 min | Three notebooks (~20–30 min each) — Core sections only |
| (Self-study after class) | self-paced | Each notebook has a 🟡 Extension section for going deeper |

**Why this structure?** Realistic 3-hour pacing means ~1.5 hours of concepts + ~1.5 hours of coding *including Q&A and environment troubleshooting*. Each in-class notebook ends at a clearly marked 🟡 Extension boundary — anything below the line is for self-study, not class time.

---

## Your learning path

This lesson follows a three-phase flow. Work through the phases in order.

---

### Phase 1 — Before class: self-study (~30 min)

**Goal:** Experience the statistical problem first — *feel* why Sarah can't simply report "60% positive" and call it done. Arrive at class with a question.

**Start here →** [**pre-class.md**](./pre-class.md)

You will:
- Open and run [`notebooks/01_monday_morning.ipynb`](./notebooks/01_monday_morning.ipynb) (~15 min) — Sarah's Monday morning, Priya's pushback, mean vs median
- Reflect on what surprised you
- Watch two short videos and preview the key concepts
- Try three mini-exercises with sample answers

---

### Phase 2 — In class: concept review + hands-on notebooks (~3 hrs)

**Goal:** Deepen the concepts with the instructor and build real skill.

**Short reference & review →** [**lesson.md**](./lesson.md) (overview, key takeaways, honest-reporting checklist, 10-question review, L02→L10 course map)

**Interactive walkthrough →** the [**key concepts page**](https://su-ntu-ctp.github.io/6m-data-3.2-Probability-Statistics-for-Machine-Learning/) (hosted on GitHub Pages) gives an in-browser tour of the core ideas.

**Notebooks — run in order:**

| # | Notebook | Sarah's day | What you explore |
|---|---|---|---|
| 02 | [`02_distributions.ipynb`](./notebooks/02_distributions.ipynb) | Tuesday | Distribution shapes · normal vs skewed · Z-scores |
| 03 | [`03_confidence_intervals.ipynb`](./notebooks/03_confidence_intervals.ipynb) | Wednesday | Sampling · the CLT · confidence intervals |
| 04 | [`04_ab_testing.ipynb`](./notebooks/04_ab_testing.ipynb) | Thursday | A/B testing · p-values · effect size · the three mis-readings |

Each notebook opens with a business scenario, guides you through the code with **Pause & Predict** prompts, and ends with a summary table and reflection. Read every markdown cell, not just the code.

---

### Phase 3 — After class: assignment + further reading (self-paced)

**Goal:** Transfer what you learned to a completely new domain.

Sarah lends her skills to **Lakeside Bank**, where **Tom Bradley** (Head of Analytics) wants to know whether a new mobile-app onboarding flow reduces complaint rates. Same three lenses — distribution, confidence interval, A/B test — different data.

**Assignment →** [`notebooks/assignment.ipynb`](./notebooks/assignment.ipynb)

Three tiers of practice (guided → partial → open) followed by three independent exercises in a hospital satisfaction-survey scenario. Sample solutions are at the bottom — attempt each exercise yourself before checking them.

**Further reading →** [**reference.md**](./reference.md)

---

## Core vs Optional — what this lesson teaches

**🟢 Core (taught in class):**
- Distributions formalised — normal, skewed, Z-scores
- Confidence intervals + the Central Limit Theorem
- A/B testing with p-values and effect size

**🟡 Optional (self-study, not assessed):**
- Bayes' theorem math
- t-test formula derivation
- Bootstrapping theory
- CLT proof sketch

Optional material lives in [`notebooks/optional_extensions.ipynb`](./notebooks/optional_extensions.ipynb). Skipping it will not affect your understanding of later lessons.

---

## File map

```
README.md                           ← You are here
setup.md                            ← One-time environment setup (do this first)
pre-class.md                        ← Phase 1: 30-min self-study guide
lesson.md                           ← Short reference: overview, takeaways, honest-reporting checklist, review Q&A, course map
reference.md                        ← Phase 3: Further reading + glossary (~25 terms)
environment.yml                     ← Conda environment spec (scipy + statsmodels included)
docs/
  index.html                        ← Interactive key-concepts walkthrough (served at https://su-ntu-ctp.github.io/6m-data-3.2-Probability-Statistics-for-Machine-Learning/ via GitHub Pages)
notebooks/
  01_monday_morning.ipynb           ← Pre-class hook: Sarah's Monday (~15 min, before class)
  02_distributions.ipynb            ← Part 1: Distributions (Tuesday, in class)
  03_confidence_intervals.ipynb     ← Part 2: Confidence Intervals (Wednesday, in class)
  04_ab_testing.ipynb               ← Part 3: A/B Testing (Thursday, in class)
  assignment.ipynb                  ← After class: Lakeside Bank + hospital exercises
  optional_extensions.ipynb         ← 🟡 Optional: Bayes · t-test derivation · bootstrapping · CLT
```
