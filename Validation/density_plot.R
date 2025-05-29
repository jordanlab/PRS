# density_plot.R
# This script plots PRS density distributions for cases and controls

#library(dplyr)
#library(ggplot2)
#library(tidyverse)

#----Load data----
#Make sure columns include: FID, IID, PRS, Status (0 = control, 1 = case)
data <- read.table("<scores_file>", header = TRUE)

#----Plot density----
ggplot(data, aes(x = PRS, fill = as.factor(Status))) +
  geom_density(alpha = 0.5) +
  labs(
    title = "PRS Distribution by Case/Control",
    x = "Polygenic Risk Score (PRS)",
    y = "Density",
    fill = "Group"
  ) +
  scale_fill_manual(
    values = c("0" = "blue", "1" = "red"),
    labels = c("Controls", "Cases")
  ) 
  theme_minimal()

# Optional: save the plot
# ggsave("density_plot.png", width = 7, height = 5)
