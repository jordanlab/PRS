# Ancestry Adjustment with pgsc_calc

## Overview

Ancestry-normalized PRS computation is critical for cross-population validity. This section focuses on:
- Understanding the built-in normalization used by `pgsc_calc`
- Replicating the adjustment logic manually on All of Us data
- Applying PCA-based regression models.

## Adjustment Logic

We replicated:
- `Empirical Methods`: Identifying the population an individual most similar to
- `Z_norm1`: Subtracting predicted PRS (based on PCs from reference panel) from raw PRS and dividing by reference SD
- `Z_norm2`: Incorporating squared PCs and polynomial terms for refined normalization

## Tools & Scripts
 - Add the R scripts for importing data/packages, replicating each of the 3 adjustments

