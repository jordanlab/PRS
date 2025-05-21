
# PRSice-2

PRSice-2 is a clumping and thresholding-based tool used for calculating Polygenic Risk Scores (PRS) across a range of p-value thresholds. 

In this project, PRSice-2 was applied to the **UK Biobank** dataset to:
- Benchmark PRS results alongside `pgsc_calc` and `PRScs`
- Generate scores across multiple p-value thresholds

## Installation

- Requirements: R and PLINK 2.0

Download the executable:

```bash
wget https://github.com/choishingwan/PRSice/releases/download/2.3.5/PRSice_linux.zip
unzip PRSice_linux.zip
chmod +x PRSice_linux
```

The following packages are needed in R:
```r
install.packages("data.table")
install.packages("ggplot2")
install.packages("pROC")
install.packages("optparse")
install.packages("broom")
```

## Input files:
1. **Base (GWAS) data**: Summary statistics file with SNPs and their effect sizes
2. **Target data**: Genotype data in PLINK Binary or BGEN format
3. **Phenotype** : Individual IDs with their case/control information

## Output files:
1. Bar Plot for various p-value thresholds
2. High Resolution Plot for various p-value thresholds
3. Quantile Plot with increasing PRS
4. `.prsice` file with the PRS Model fit
5. `.summary` file
6. `.log` file for each run
7. `.best` file with final PRS for each individual 

Sample Command:
```bash
Rscript PRSice.R \
--base <gwas> \
--target <genotypes> \
--pheno <phenotype file> \
--binary-target <T/F> \
--prsice PRSice_linux \
--out <output_dir>
```

Additional flags can be included depending on the phenotype, datasets and analysis goals.
