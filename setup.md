# L02 Setup — Environment Guide

This guide gets you from zero to running L02 on your machine in about 15 minutes. The same environment works for every lesson in the DSAI M3 series — if you already set up `dsai-m3` for L01, you can skip straight to the **Verify** step.

**Supported environments:**
- **macOS** (Apple Silicon — M1 or later)
- **Windows 10/11 with WSL2** (Ubuntu 22.04 recommended)
- **Google Colab** (handy fallback if local install gives trouble)

**Supported IDE / runtime:**
- **VS Code + Jupyter extension** (recommended)
- **Google Colab** (browser-based fallback)

---

## TL;DR — fastest path

```bash
# 1. Clone the repo
git clone https://github.com/su-ntu-ctp/6m-data-3.2-Probability-Statistics-for-Machine-Learning.git
cd 6m-data-3.2-Probability-Statistics-for-Machine-Learning

# 2. Create the conda environment (skip if you already have dsai-m3 from L01)
conda env create -f environment.yml
conda activate dsai-m3

# 3. L02 uses scipy + statsmodels — already in environment.yml, but if you
#    upgraded from an older L01 env, install/update them:
pip install -U scipy statsmodels

# 4. Launch VS Code in the repo root
code .
```

Then in VS Code:
1. Open `notebooks/01_monday_morning.ipynb`
2. Top-right → **Select Kernel** → `dsai-m3` (Python 3.11)
3. **Run All**

If a notebook hangs or errors, scroll down to **Troubleshooting**.

---

## 1. Install Python via Miniconda

We use conda to manage a self-contained Python environment for the course. This avoids polluting your system Python.

### macOS (Apple Silicon)

```bash
curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda3
$HOME/miniconda3/bin/conda init "$(basename $SHELL)"

# Restart your terminal, then verify
conda --version
```

### Windows WSL (Ubuntu)

Open Ubuntu in WSL, then:

```bash
curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda3
$HOME/miniconda3/bin/conda init bash

# Restart your terminal, then verify
conda --version
```

> **Windows users — do NOT install Miniconda on Windows directly.** Use WSL.

---

## 2. Clone the repo

```bash
mkdir -p ~/repos
cd ~/repos
git clone https://github.com/su-ntu-ctp/6m-data-3.2-Probability-Statistics-for-Machine-Learning.git
cd 6m-data-3.2-Probability-Statistics-for-Machine-Learning
```

On WSL, clone **inside WSL** (`~/repos/...`), not on `/mnt/c/...` — notebooks run 5–10× faster on the Linux filesystem.

---

## 3. Create the conda environment

From the cloned repo root:

```bash
conda env create -f environment.yml
conda activate dsai-m3
```

This creates an environment named `dsai-m3` with Python 3.11 and the L02 baseline packages (`numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `jupyter`, `ipykernel`).

### Already have `dsai-m3` from L01?

You probably already have everything. If you get `ImportError: No module named scipy` (or `statsmodels`), install the L02 extras:

```bash
conda activate dsai-m3
pip install -U scipy statsmodels
```

Versions known to work:
- `scipy >= 1.11`
- `statsmodels >= 0.14`

---

## 4. Install VS Code + Jupyter extension

### macOS

Download from https://code.visualstudio.com/Download. Drag to Applications.

### Windows WSL

Install VS Code **on Windows** (not in WSL). VS Code connects to WSL through the Remote-WSL extension. Download from https://code.visualstudio.com/Download.

### Required extensions

In VS Code, **Cmd/Ctrl+Shift+X** opens the Extensions sidebar. Install:

1. **Python** (Microsoft) — required
2. **Jupyter** (Microsoft) — required
3. **WSL** (Microsoft) — **only for Windows WSL users**

---

## 5. Open the repo in VS Code

```bash
cd ~/repos/6m-data-3.2-Probability-Statistics-for-Machine-Learning
code .
```

On WSL you'll see a green `WSL: Ubuntu` indicator in the bottom-left.

---

## 6. Verify your setup

Open `notebooks/01_monday_morning.ipynb`.

1. **Top-right of the notebook → "Select Kernel"** → pick `dsai-m3` (Python 3.11)
2. Run the **first code cell**
3. The notebook should run end-to-end in under 2 minutes — no model downloads, just `numpy` / `pandas` / `scipy`.

L02 uses no external datasets; all numbers are generated in the notebooks themselves.

---

## When to use Google Colab instead

If local install is giving you trouble, you can run any notebook in **Google Colab** (free tier). Use **File → Open notebook → GitHub** and paste this repo's URL.

For L02, CPU is fine; you don't need a GPU.

---

## Troubleshooting

### "`ImportError: No module named scipy` (or `statsmodels`)"

```bash
conda activate dsai-m3
pip install -U scipy statsmodels
```

### "Kernel `dsai-m3` doesn't appear in the kernel picker"

VS Code's Python extension caches kernels. Reload VS Code:
**Cmd/Ctrl+Shift+P → "Developer: Reload Window"**

If still missing:

```bash
conda activate dsai-m3
python -m ipykernel install --user --name dsai-m3 --display-name "Python (dsai-m3)"
```

### "VS Code keeps using my system Python, not `dsai-m3`"

Click the kernel name in the top-right of the notebook → **Select Another Kernel → Python Environments → dsai-m3**.

### "WSL is slow"

You're probably running notebooks from `/mnt/c/...`. Move them to `~/repos/...` inside WSL.

### Something else broke

Open an issue: https://github.com/su-ntu-ctp/6m-data-3.2-Probability-Statistics-for-Machine-Learning/issues. Include:
- macOS or WSL? (and version)
- Output of `conda --version`, `python --version`, `pip show scipy statsmodels`
- The full error traceback
- Which notebook + which cell

---

## Quick reference

| Task | Command |
|---|---|
| Activate the env | `conda activate dsai-m3` |
| Update L02 deps | `pip install -U scipy statsmodels` |
| Launch VS Code in repo | `code .` (from the repo root) |
| Reload VS Code | `Cmd/Ctrl+Shift+P → "Developer: Reload Window"` |
