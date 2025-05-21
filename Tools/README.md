# Tools

This folder contains setup instructions for key tools used in the PRS analysis pipeline.

## [PRSice-2](./PRSice-2)
- Fast and flexible tool for LD clumping and threshold-based PRS calculation
- Used for baseline PRS score generation

## [pgsc_calc](./pgsc_calc)
- [Nextflow](https://www.nextflow.io/)-based pipeline from the [Polygenic Score Catalog](https://www.pgscatalog.org/)
- Core to ancestry-adjusted normalization (see separate section)
- **Notes**: Requires conda or Docker environment. Outputs include raw and ancestry-adjusted scores.

## Miscellaneous
- **Beagle 5.5**: Java-based imputation tool used on Lyday VCFs
- **conform-gt**: Harmonizes genotype formats to match reference panel
- **bcftools**: For subsetting and filtering variants
- **PLINK 2.0**: Conversion and QC

Each tool folder contains installation instructions, links to documentation, and sample commands used in this project.
