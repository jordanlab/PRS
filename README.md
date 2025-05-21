# Polygenic Risk Score (PRS) Pipeline

This repository hosts a reproducible pipeline for calculating and validating **Polygenic Risk Scores (PRS)** across three cohorts: **UK Biobank**, **All of Us**, and the **Lyday cohort**.

The pipeline is built using a combination of Python, R, and Nextflow workflows.

## Repo Structure

| Folder | Description |
|--------|-------------|
| `Data/` | Describes each cohort: Lyday, All of Us, and UK Biobank. Includes info on preprocessing. |
| `Tools/` | Contains usage notes for core tools like `pgsc_calc`, `PRSice-2`, `PRSCs`, `Beagle`, and more. |
| `Ancestry adjustment with pgsc_calc./` | Focuses on ancestry-normalized PRS and includes the logic replicated from the `pgsc_calc` framework. |
| `Validation/` | Scripts and results for statistical validation using R. |
| `prs_pipeline/` | (Coming soon) Python-based CLI pipeline to modularly run each step with checkpointing. |

---

## Datasets

- **UK Biobank**: Used for testing and benchmarking PRS tools (data already imputed and standardized)
- **All of Us**: PRS calculation in addition to ancestry-adjustment using `pgsc_calc`
- **Lyday**: Raw VCFs requiring genotype harmonization, imputation, and conversion prior to PRS calculation

Each dataset has its own documentation inside the `Data/` directory.

---

## Tools Utilised

- [`pgsc_calc`](https://www.pgscatalog.org/): Nextflow-based official PRS scoring pipeline
- [`PRSice-2`](https://www.prsice.info/): Clumping + thresholding tool
- [`PRSCs`](https://github.com/getian107/PRScs): Bayesian regression method for PRS
- [`Beagle`](https://faculty.washington.edu/browning/beagle/beagle.html): Imputation
- [`conform-gt`](https://faculty.washington.edu/browning/conform-gt.html): Genotype harmonization
- Python for pipeline scripting
- R for statistical validation (e.g., AUC, Odds Ratio, Cohen’s d)

---

##  Getting Started

This project is under development. To reproduce or test:
1. Navigate to the dataset of interest under `Data/`
2. Set up the tools required under `Tools/`
3. Run the PRS pipeline using `pgsc_calc` or the custom Python workflow
4. Validate the scores using the scripts in `Validation/`


---

## References

- [Lambert et al. (2021), *The Polygenic Score Catalog as an open database for reproducibility and systematic evaluation.*](https://rdcu.be/em0At)
- All of Us Research Program, *NIH*

---

## Maintained by

Valli Sree Lasya Pasumarthy  
Graduate Research – Jordan Lab  
Masters of Science in Bioinformatics 
School of Biological Sciences, Georgia Institute of Technology
