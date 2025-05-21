# Data

This directory contains descriptions and metadata for the three cohorts used:

## [UK Biobank](#UKBiobank)
- **Source**: Preprocessed and imputed data on remote lab server
- **Format**: Binary PLINK files (`.bed/.bim/.fam`) and PCA projections
- **Purpose**: Used as a benchmarking dataset to compare PRSice-2, PRS-CS, and pgsc_calc

## [Lyday](#Lyday)
- **Source**: Raw VCF files from a collaborator.
- **Processing Steps**:
  - Chromosome-level VCF merging
  - Genotype harmonization using `conform-gt`
  - Imputation using Beagle 5.5
  - Conversion to PLINK format
- **Notes**: Output from these steps was used for PRS calculation with `pgsc_calc`.

## [All of Us](#AllofUs)
- **Source**: [All of Us genomic dataset](https://allofus.nih.gov/) 
- **Processing Steps**:
  - Subsetting individuals by self-identified race/ethnicity (SIRE): EUR, AFR, AMR
  - Filtering variants to match those in scoring files
  - Extracting PCs for ancestry normalization

Each subfolder contains documentation on how the data was prepared and which scripts/tools were used.
