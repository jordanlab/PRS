# metrics.R
# This script computes statistical evaluation metrics and plots for PRS

# ----Load Libraries----
#library(dplyr)
#library(readr)
#library(pROC)
#library(MASS)
#library(car)
#library(pscl)
#library(effsize)

#----Load data----

#Required: PRS, Status (0/1), Covariates (eg. age, sex etc.), PC1-PC5 
data <- read.table("<scores_file>", header = TRUE)
#If covariates and PCs are in different files, merge them with <scores_file> and proceed

#----Scale the scores if necessary----
data <- data %>%
  mutate(Z_scores = scale(PRS))

#----Incremental R²----

#Fitting logistic regression models
model_base <- glm(Status ~ covariates + PCs, data = data, family = binomial)
model_adjusted <- glm(Status ~ PRS + covariates + PCs, data = data, family = binomial)

r2_base <- pR2(model_base)["McFadden"]
r2_adjusted <- pR2(model_adjusted)["McFadden"]
delta_r2 <- r2_adjusted - r2_base

print(delta_r2)

#----AUC + Plot----
prob_base <- predict(model_base,type = "response")
prob_adjusted - predict(model_adjusted, type = "response")

#Computing ROC values
roc_base <- roc(data$Status, model_base)
roc_adjusted <- roc(data$Status, model_adjusted)

#Plot
plot(roc_base, col = "#1c61b6", main = "AUC Comparison", legacy.axes = TRUE,
     xlab = "False Positive Rate", ylab = "True Positive Rate")
lines(roc_adjusted, col = "#e94e77")
legend("bottomright", legend = c(
  paste("AUC (Cov only):", round(auc(roc_base), 2)),
  paste("AUC (PRS + Cov):", round(auc(roc_cov), 2))
), col = c("#1c61b6", "#e94e77"), lwd = 2)

#----Odds Ratio + Confidence Interval----

or <- exp(coef(model_adjusted)
ci <- exp(confint(logit_model)

#View them as a dataframe
stats <- data.frame(
	OR = or,
	CI_lower = ci[,1],
	CI_upper = ci[,2]
)

#----Cohen's d----

cases <- data$PRS[data$Status == 1]
controls <- data$PRS[data$Status == 0]
d <- cohen.d(cases, controls)
print(d)
