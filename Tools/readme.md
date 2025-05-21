# Tools

This folder contains setup instructions and usage notes for key tools used in the PRS analysis pipeline.

## [PRSice-2](https://github.com/ikingjordan3/PRS/tree/main/Tools/PRSice-2)
- Fast and flexible tool for clumping + threshold-based PRS calculation
- Used for baseline PRS score generation

## [pgsc_calc](https://github.com/ikingjordan3/PRS/tree/main/Tools/pgsc_calc)
- Official pipeline from the [Polygenic Score Catalog](https://www.pgscatalog.org/)
- Run as a [Nextflow](https://www.nextflow.io/) workflow
- Core to ancestry-adjusted normalization (see separate section)

## Miscellaneous
- **Beagle 5.5**: Imputation tool used on Lyday VCFs
- **conform-gt**: Harmonizes genotype formats to match reference panel
- **bcftools**: For subsetting and filtering variants
- **PLINK 1.9/2.0**: Conversion and QC

Each tool folder contains setup commands and links to documentation.
