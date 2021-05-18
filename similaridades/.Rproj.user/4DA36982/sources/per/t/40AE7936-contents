require(dendextend)
require(dplyr)

dendlist(dendInventario12, dendLidar12) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendInventario12, dendLidar12)

dendlist(dendInventario12, dendInventario14) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendInventario12, dendInventario14)

dendlist(dendLidar12, dendLidar14) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar12, dendLidar14)
