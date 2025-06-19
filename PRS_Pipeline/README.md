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

| Name      | Purpose |
|--------------------|---------|
| `steps/`           | Step-wise modules: `preprocess`, `run_pgsc_calc`, and `validate` |
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

- Step 1 - **preprocess**  
  Usage:
  ``` bash
  ./main.py --step preprocess
  ```
  This is to check and report whether the input genotype files follow the required formats to be used in the samplesheet.
  
- Step 2 - **run_pgsc_calc**  
  Usage:
  ```bash
  ./main.py --step run_pgsc_calc
  ```
  This is to run pgsc_calc on the target data. Inputs are:
  1. PGS ID
  2. Path to the samplesheet containing genotype information
  3. Intended target build (from ```config.yaml```)
  4. Profile to be used when running pgsc_calc (from ```config.yaml```; choose from Docker, Conda, Singularity)
  5. Output directory to store the produced score file and log files (from ```config.yaml```)
 
- Step 3 - **validate**  
  Usage:
  ```bash
  ./main.py --step validate
  ```
  This displays the validation metrics like ```Incremental R²```, ```AUC values (base and adjusted models)```, ```Odds ratio and 95% CI```, ```Cohen's d``` for case-controls, ```p-value``` for case-controls using T-test along with the distribution, gradient and AUC ROC plots.
  Inputs:
  1. A merged data file which has the PRS values, covariates and phenotype status (for binary traits)
  2. Path of an output directory to store the produced plots

*Note:* Any step can be executed as standalone. 
