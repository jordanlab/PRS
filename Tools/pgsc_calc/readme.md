# pgsc_calc

[`pgsc_calc`](https://github.com/PGScatalog/pgsc_calc) is the official Nextflow-based pipeline developed by The Polygenic Score (PGS) Catalog to calculate Polygenic Risk Scores (PRS) using standardized scoring files.

It supports ancestry-adjusted scoring and is well-suited for high-throughput and reproducible PRS analysis.

## Installation

This pipeline requires:
- [Nextflow](https://www.nextflow.io/) (version ≥ 21.04)
- [Conda](https://docs.conda.io/) **or** Docker/Singularity (for environments)
- Java (version ≥ 8)

### Setup Steps

1. Install Java and Nextflow:

```bash
curl -s https://get.sdkman.io | bash
```
1.1 In a new terminal:
```bash
sdk install java 17.0.10-tem
java -version #confirm installation
curl -s https://get.nextflow.io | bash
chmod +x nextflow
mv nextflow $HOME/.local/bin/ #move nextflow to any executable PATH
```
2. Install Docker/Singularity/Conda
3. Run the test profile:
```bash
nextflow run pgscatalog/pgsc_calc -profile test,<docker/singularity/conda>
```

## Inputs
| Flag                  | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| `--target`            | PLINK genotype prefix                              |
| `--pgs_id`            | PGS Catalog ID                                |
| `--base` *(optional)* | Custom scoring file instead of automatic download                  |
| `--target_build`      | Genome build of genotype files (`GRCh37` or `GRCh38`)              |
| `--outdir`            | Output directory                                                   |
| `--min_overlap`       | Minimum % of overlapping SNPs between score file and genotype data |

**Notes**
- min_overlap by default is 0.75. The value should be adjusted accordingly
- the base and target data should be in the same genome build

## Outputs
After successfully executing, the scores and a summary report will be created in `results/score/` under the working directory. 
