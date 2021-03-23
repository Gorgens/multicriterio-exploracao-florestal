## Agrupamento para 2012
inventario2012 = read.csv('./inventario_2012.csv')
inventario2012 = inventario2012[,-1]

inventario2012scaled = scale(inventario2012)                  # standardize variables
d = dist(inventario2012scaled, method = "euclidean")          # distance matrix
inventario2012groups = hclust(d, method="ward")
png('cluster2012.png', width = 14, height = 10, units = 'cm', res = 300)
plot(inventario2012groups)                                    # display dendogram
dev.off()

groups = cutree(inventario2012groups, k=5)                    # cut tree into 5 clusters
png('clusterGrupos2012.png', width = 14, height = 10, units = 'cm', res = 300)
plot(inventario2012groups)                                    # display dendogram
rect.hclust(inventario2012groups, k=5, border="red")          # draw dendogram with red borders around the 5 clusters
dev.off()

## Agrupamento para 2014
inventario2014 = read.csv('./inventario_2014.csv')
inventario2014 = inventario2014[,-1]

inventario2014scaled = scale(inventario2014)                  # standardize variables
d2 = dist(inventario2014scaled, method = "euclidean")         # distance matrix
inventario2014groups = hclust(d2, method="ward")
png('cluster2014a.png', width = 14, height = 10, units = 'cm', res = 300)
plot(inventario2014groups)                                    # display dendogram
dev.off()

groups = cutree(inventario2014groups, k=5)                    # cut tree into 5 clusters
png('clusterGrupos2014a.png', width = 14, height = 10, units = 'cm', res = 300)
plot(inventario2014groups)                                    # display dendogram
rect.hclust(inventario2014groups, k=5, border="red")          # draw dendogram with red borders around the 5 clusters
dev.off()
