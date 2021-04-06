#setwd('/home/gorgens/Documents/R julia pibic/')

library(forestmangr)
library(fpc)

metrics2012 = read.csv('./2012/metrics2012.csv')
metrics2012 = metrics2012[,-1]

metrics2012scaled = scale(metrics2012)                        # standardize variables
d = dist(metrics2012scaled, method = "euclidean")             # distance matrix
metrics2012groups = hclust(d, method="ward")
plot(metrics2012groups)                                       # display dendogram

#groups = cutree(metrics2012groups, k=5)                      # cut tree into 5 clusters
#rect.hclust(metrics2012groups, k=5, border="red")            # draw dendogram with red borders around the 5 clusters

cluster.stats(d, metrics2012groups$cluster, fit2$cluster)     # validar agrupamentos
