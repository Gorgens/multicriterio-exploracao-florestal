require(dendextend)
require(dplyr)

## Agrupamento para 2012
inventario2012 = read.csv('./inventario_2012.csv')
rownames(inventario2012) = inventario2012$transect
inventario2012 = inventario2012[,-1]

inventario2012scaled = scale(inventario2012)                  # standardize variables
d = dist(inventario2012scaled, method = "euclidean")          # distance matrix
inventario2012groups = hclust(d, method="ward")
plot(inventario2012groups)                                    # display dendogram

## Agrupamento para 2014
inventario2014 = read.csv('./inventario_2014.csv')
rownames(inventario2014) = inventario2014$transect
inventario2014 = inventario2014[,-1]

inventario2014scaled = scale(inventario2014)                  # standardize variables
d2 = dist(inventario2014scaled, method = "euclidean")         # distance matrix
inventario2014groups = hclust(d2, method="ward")
plot(inventario2014groups)                                    # display dendogram

## Agrupamento para 2014b
inventario2014b = read.csv('./inventario_2014b.csv')
inventario2014b = inventario2014b %>%
  group_by(transecto) %>%
  summarise(Shannon = mean(Shannon),
            Simpson = mean(Simpson),
            EqMaxima = mean(EqMaxima),
            Pielou = mean(Pielou),
            Jentsch = mean(Jentsch),
            DBH = mean(DBH),
            q = mean(q),
            IndvHA = mean(IndvHA),
            G_HA = mean(G_HA),
            VCC_HA = mean(VCC_HA)) %>%
  as.data.frame()
rownames(inventario2014b) = inventario2014b$transect
inventario2014b = inventario2014b[,-1]

inventario2014bscaled = scale(inventario2014b)                 # standardize variables
d = dist(inventario2014bscaled, method = "euclidean")          # distance matrix
inventario2014bgroups = hclust(d, method="ward")
plot(inventario2014bgroups)                                    # display dendogram

## Agrupamento para 2018
inventario2018 = read.csv('./inventario_2018.csv')
inventario2018 = inventario2018 %>%
  group_by(transecto) %>%
  summarise(Shannon = mean(Shannon),
            Simpson = mean(Simpson),
            EqMaxima = mean(EqMaxima),
            Pielou = mean(Pielou),
            Jentsch = mean(Jentsch),
            DBH = mean(DBH),
            q = mean(q),
            IndvHA = mean(IndvHA),
            G_HA = mean(G_HA),
            VCC_HA = mean(VCC_HA)) %>%
  as.data.frame()
rownames(inventario2018) = inventario2018$transect
inventario2018 = inventario2018[,-1]

inventario2018scaled = scale(inventario2018)                 # standardize variables
d = dist(inventario2018scaled, method = "euclidean")          # distance matrix
inventario2018groups = hclust(d, method="ward")
plot(inventario2018groups)    

# Comparação dos dendrogramas para inventário
dendInventario12 = as.dendrogram(inventario2012groups)
dendInventario14 = as.dendrogram(inventario2014groups)
dendInventario14b = as.dendrogram(inventario2014bgroups)
dendInventario18 = as.dendrogram(inventario2018groups)

dendlist(dendInventario12, dendInventario14) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendInventario12, dendInventario14)

dendlist(dendInventario14b, dendInventario18) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendInventario14b, dendInventario18)
