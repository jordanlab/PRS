#!/usr/bin/env python3

# step3_validate.py

import os
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve
from scipy.stats import ttest_ind
from statsmodels.tools import add_constant
from statsmodels.discrete.discrete_model import Logit
from math import sqrt
import matplotlib.pyplot as plt


def cohen_d(x, y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (np.mean(x) - np.mean(y)) / sqrt(((nx - 1) * np.std(x, ddof=1) ** 2 + (ny - 1) * np.std(y, ddof=1) ** 2) / dof)


def run(config):
    print("Step 3: Validating PRS")

    prs_file = input("Enter absolute path to merged (PRS + phenotype file): ").strip()

    if not os.path.isfile(prs_file):
        print("Error: File not found.")
        return

    data = pd.read_csv(prs_file, sep="\t" if prs_file.endswith(".txt") else ",")
    if "Sex" in data.columns and data["Sex"].dtype == "object":
         print("Converting 'Sex' from Male/Female to 0/1...")
         data["Sex"] = data["Sex"].map({"Male": 0, "Female": 1})

    print("Detected columns in dataset:")
    print(data.dtypes)
    prs_col = input("Enter the column name for Scores: ").strip()
    if prs_col not in data.columns:
        print("Column not found.")
        return

    covariates = input("\nEnter comma-separated covariate column names from dataset: ").strip()
    cov = [x.strip() for x in covariates.split(",") if x.strip() in data.columns]

    if not cov:
        print("Error: No covariates found.")
        return

    print(f"Using the covariates: {cov}")

    data["PRS"] = data[prs_col]

    X_base = add_constant(data[cov])
    X_full = add_constant(data[["PRS"] + cov])
    y = data["Status"]

    model_base = Logit(y, X_base).fit(disp=False)
    model_full = Logit(y, X_full).fit(disp=False)

    ll_base = model_base.llf
    ll_full = model_full.llf
    r2_base = 1 - (ll_base / model_base.llnull)
    r2_full = 1 - (ll_full / model_full.llnull)
    inc_r2 = r2_full - r2_base
    print("Incremental R^2:", round(inc_r2, 4))

    y_prob_base = model_base.predict(X_base)
    y_prob_full = model_full.predict(X_full)
    auc_base = roc_auc_score(y, y_prob_base)
    auc_full = roc_auc_score(y, y_prob_full)
    print("AUC (Base):", round(auc_base, 4))
    print("AUC (Full):", round(auc_full, 4))

    or_vals = np.exp(model_full.params)
    ci = np.exp(model_full.conf_int())
    print("Odds Ratios and 95% CI:\n", pd.DataFrame({"OR": or_vals, "CI Lower": ci[0], "CI Upper": ci[1]}))

    cases = data[data["Status"] == 1]["PRS"]
    controls = data[data["Status"] == 0]["PRS"]
    d = cohen_d(cases, controls)
    print("Cohen's d:", round(d, 4))

    t_stat, p_val = ttest_ind(cases, controls)
    print("t-test p-value:", round(p_val, 5))

    fpr_base, tpr_base, _ = roc_curve(y, y_prob_base)
    fpr_full, tpr_full, _ = roc_curve(y, y_prob_full)

    plt.plot(fpr_base, tpr_base, label=f"Base AUC = {auc_base:.2f}", color="blue")
    plt.plot(fpr_full, tpr_full, label=f"PRS + Cov AUC = {auc_full:.2f}", color="red")
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("AUC Curve")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("auc_comparison.png")
    plt.close()

    print("[STEP 3] Validation complete. Output saved to auc_comparison.png")
