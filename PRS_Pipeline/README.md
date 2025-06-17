#  Polygenic Risk Score (PRS) Pipeline  ![Status](https://img.shields.io/badge/Status-in%20progress-yellow)

This repository contains a reproducible pipeline for computing and validating Polygenic Risk Scores (PRS) using diverse genomic cohorts, including:

- **UK Biobank**
- **All of Us Research Program**
- **Lyday dataset (VCF-based input)**

The pipeline is built using:
- Python CLI (with support for interactive inputs and `config.yaml`)
- Nextflow (`pgsc_calc` integration)
- R and Python for statistical validation

---

## Repo Structure

| Folder / File      | Purpose |
|--------------------|---------|
| `steps/`           | Python step-wise modules: `preprocess`, `run_pgsc_calc`, and `validate` |
| `main.py`          | Entry-point CLI script to run any step interactively |
| `config.yaml`      | User-editable configuration |
| `requirements.txt` | Python dependencies |

---

## Getting Started

### 1️. Clone the repository
```bash
git clone https://github.com/jordanlab/PRS_Pipeline.git
cd PRS_Pipeline/
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
Any additional dependencies and profiles can be set up by the user.

### 3. Run the steps

Add relevant file paths to ```config.yaml``` and run any step as follows:
```bash
./main.py --step <preprocess/run_pgsc_calc/validate>
```
