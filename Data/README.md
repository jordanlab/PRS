# Data

This directory contains descriptions for the three datasets used. Please note this section exists solely to describe the source, format, and preprocessing steps performed on each cohort.

## [1. UK Biobank](https://www.ukbiobank.ac.uk/)
- **Source**: Preprocessed and imputed data on teralab (`/home/sharedFolder/referenceData/ukb/`)
- **Format**: Binary PLINK files (`.bed/.bim/.fam`) and PCA projections
- Used as a benchmarking dataset to compare PRSice-2, PRScs, and pgsc_calc

## 2. Lyday
- **Source**: Raw VCF files from a collaborator.
- **Processing Steps**:
  - Chromosome-level VCF merging
  - Genotype harmonization using [`conform-gt`](../Tools/)
  - Imputation using [`Beagle 5.5`](../Tools/)
  - Conversion to PLINK format
- **Notes**: Output from these steps was used for PRS calculation with `pgsc_calc`.

## 3. All of Us
- **Source**: [All of Us](https://allofus.nih.gov/) genomic dataset
- **Processing Steps**:
  - Building Case-Control Cohort using the All of Us cohort builder (*Add the cohort image*)
  - Subsetting individuals by self-identified race/ethnicity (SIRE): EUR, AFR, AMR
  - Individuals with age & sex present in the reported data
  - Filtering variants to match those in scoring files (*Cromwell and ACAF*)
  - Extracting PCs for ancestry normalization

All analysis was conducted on a remote server; data was not transferred locally or externally.  
Please refer to the `Tools/`, `Ancestry adjustment with pgsc_calc./`, and `Validation/` directories for additional implementation details.


