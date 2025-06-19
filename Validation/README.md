# PRS Validation & Evaluation

This directory contains scripts used to validate PRS performance.

## Statistical Metrics
- **AUC (Area Under Curve)**: Discriminative ability for binary traits
- **Incremental R²**: Additional variance explained by PRS (on top of covariates)
- **Odds Ratio (OR)**: Risk increase per standard deviation of PRS
- **Confidence Interval (CI)**: For interpreting statistical strength of OR/R²
- **Cohen’s d**: Effect size between cases and controls

The statistics are calculated for two models:
- Base Model - T2D ~ Age + Sex
- Fully Adjusted Model - T2D ~ PRS + Age + Sex

## Covariates
Models optionally include:
- Age
- Sex
- Top 'n' principal components (PCs)

## Visualisations
- Density plots of PRS distributions
- Gradient plots of Observed Prevalance of Disease vs PRS 

All validation was performed in R. These scripts can be adapted for any cohort or phenotype.
