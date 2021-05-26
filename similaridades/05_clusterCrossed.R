require(dendextend)
require(dplyr)

dendlist(dendLidar12, dendInventario12) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar12, dendInventario12)

dendlist(dendLidar14, dendInventario14) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar14, dendInventario14)

dendlist(dendLidar14b, dendInventario14b) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar14b, dendInventario14b)

dendlist(dendLidar17, dendInventario18) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar17, dendInventario18)