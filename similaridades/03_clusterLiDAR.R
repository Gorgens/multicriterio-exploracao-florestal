#setwd('/home/gorgens/Documents/R julia pibic/')

require(dendextend)
require(dplyr)

metrics2012 = read.csv('./2012/metrics2012.csv')
rownames(metrics2012) = metrics2012$transect
metrics2012 = metrics2012[,-1]

metrics2014 = read.csv('./2014/metrics2014a.csv')
rownames(metrics2014) = metrics2014$transect
metrics2014 = metrics2014[,-1]

metrics2012scaled = scale(metrics2012)                        # standardize variables
d = dist(metrics2012scaled, method = "euclidean")             # distance matrix
metrics2012groups = hclust(d, method="ward")
plot(metrics2012groups)                                       # display dendogram

metrics2014scaled = scale(metrics2014)                        # standardize variables
d = dist(metrics2014scaled, method = "euclidean")             # distance matrix
metrics2014groups = hclust(d, method="ward")
plot(metrics2014groups)                                       # display dendogram

# Comparação dos dendrogramas para inventário
dendLidar12 <- as.dendrogram(metrics2012groups)
dendLidar14 <- as.dendrogram(metrics2014groups)
dend_list <- dendlist(dendLidar12, dendLidar14)

dendlist(dendLidar12, dendLidar14) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

dendlist(dendLidar12, dendLidar14) %>% entanglement
