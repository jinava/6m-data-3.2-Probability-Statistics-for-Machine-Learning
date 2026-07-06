# Before Class — L02 — Probability & Statistics for ML

**Estimated time: ~30 minutes.** Complete this before class.

This is the simplest version of "show up prepared": watch a short intro video, run one notebook, answer a few questions. You'll come to class having seen the idea in action.

| Step | Time | What you do |
|---|---|---|
| **1. Watch the intro video** | ~5 min  | [L02 intro video on YouTube](https://youtu.be/HNuzkM8quzA) — sets up Sarah's "how sure are we?" problem |
| **2. Try it** | ~20 min | Open and run `notebooks/01_monday_morning.ipynb` |
| **3. Reflect** | ~5 min  | Three short questions below |

---

## Step 0 — Watch the intro video (~5 min)

Before you open the notebook, watch the short intro video: **[L02 The Analyst's Defense](https://youtu.be/HNuzkM8quzA)**. It's under 5 minutes and frames the problem you're about to solve. Watching this first makes the notebook click faster.

🕹️ **After the video:** open the [interactive key-concepts page](https://su-ntu-ctp.github.io/6m-data-3.2-Probability-Statistics-for-Machine-Learning/) and play with it for 10–15 minutes. Drag the sliders, click the buttons — you can't break anything. Arriving in class having *seen* these ideas move makes the session far easier.

---

## Step 1 — Try it (~20 min)

Open **`notebooks/01_monday_morning.ipynb`** in VS Code with the `dsai-m3` kernel. Run every cell top to bottom. Read the markdown between cells. Don't skip any cell.

Sarah's positivity number from L01 (~60%) lands on Marcus's desk. He asks the question every senior leader asks: *"How sure are you?"* The notebook walks you through what "sure" means — confidence intervals, hypothesis testing, and the painful truth that 84% accuracy on 200 reviews could be 78% or 89% on the real population.

If this is your first time running a notebook in this repo, see [setup.md](./setup.md) once — you only need to do this for the first lesson.

---

## Step 2 — Quick reflection (~5 min)

Write a sentence or two for each. You can scribble in a notebook, in a journal, or just hold the answer in your head — what matters is that you *tried*.

**Q1. Why is one number never enough?**

Sarah reported "60% positive" without an uncertainty range. What's the practical danger of telling Marcus 60% if the real number is anywhere from 45% to 75%?

**Q2. Same data, two summaries.**

If a feature is highly skewed (e.g., spending: most £10, a few £5,000), is the mean or the median more honest? Why?

**Q3. Pick your CI: 95% or 99%?**

When would you prefer a 99% confidence interval over a 95% one? When would you prefer the opposite?

---

## Bring to class

- Your one-sentence answer to Q1.
- One business decision from your work that *should* have come with error bars and didn't.

---

**Want to go deeper before class?** See **[reference.md](./reference.md) → *Further reading & watching*** at the bottom — videos and recommended readings that used to live in this guide.

**Ran out of time?** Doing just Step 1 (running the notebook) is enough. The class builds on having felt what the lesson teaches; the reflection questions get re-asked live.
