# gradient_plot.R

#library(dplyr)
#library(tidyverse)
#library(ggplot2)

#----Load data---- 
#Make sure columns include: FID, IID, PRS, Status (0/1), AVG. If the FID and status are in another file, merge them before proceeding

data <- read.table("<scores_file>", header = TRUE) 

#<scores_file> - .best for PRSice-2, .txt for pgsc_calc


#----Group individuals by PRS percentiles----
data <- data %>%
  mutate(percentile = ntile(AVG, 100))

#----Calculate prevalence by percentiles----
risk_gradient <- data %>%
  group_by(percentile) %>%
  summarize(prevalence = mean(Status) * 100, .groups = "drop")

#----Plot----
ggplot(risk_gradient, aes(x = percentile, y = prevalence)) +
  geom_point(color = "darkblue", size = 2) +
  labs(
    title = "PRS vs Observed Prevalence",
    x = "Percentile of PRS",
    y = "Observed Prevalence (%)"
  ) +
  theme_minimal()

#Additional features can be added as per user's requirement