# PRS Validation & Evaluation

This directory contains scripts and metrics used to validate PRS performance.

## Statistical Metrics
- **AUC (Area Under Curve)**: Discriminative ability for binary traits
- **Incremental R²**: Additional variance explained by PRS (on top of covariates)
- **Odds Ratio (OR)**: Risk increase per standard deviation of PRS
- **Confidence Interval (CI)**: For interpreting statistical strength of OR/R²
- **Cohen’s d**: Effect size between cases and controls

## Covariates
Models optionally include:
- Age
- Sex
- Top 5 principal components (PCs)

## Outputs
- Density plots of PRS distributions
- Gradient plots of Prevalance of Disease vs Observed PRS 

All validation was performed in R. These scripts can be adapted for any cohort or phenotype.
