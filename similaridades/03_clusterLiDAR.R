#setwd('/home/gorgens/Documents/R julia pibic/')

require(dendextend)
require(dplyr)

metrics2012 = read.csv('./metrics2012.csv')
rownames(metrics2012) = metrics2012$transect
metrics2012 = metrics2012[,-1]

metrics2014 = read.csv('./metrics2014a.csv')
rownames(metrics2014) = as.character(metrics2014$transect)
metrics2014 = metrics2014[,-1]

metrics2014b = read.csv('./metrics2014b.csv')
metrics2014b = metrics2014b %>%
  group_by(transecto) %>%
  summarise(zmax = mean(zmax),
            zmean = mean(zmean),
            zsd = mean(zsd),
            zskew = mean(zskew),
            zkurt = mean(zkurt),
            zentropy = mean(zentropy),
            pzabovezmean = mean(pzabovezmean),
            pzabove2 = mean(pzabove2),
            zq5 = mean(zq5),
            zq10 = mean(zq10),
            zq15 = mean (zq15),
            zq20 = mean(zq20),
            zq25 = mean(zq25),
            zq30 = mean(zq30),
            zq35 = mean(zq35),
            zq40 = mean(zq40),
            zq45 = mean(zq45),
            zq50 = mean(zq50),
            zq55 = mean(zq55),
            zq60 = mean(zq60),
            zq65 = mean(zq65),
            zq70 = mean(zq70),
            zq75 = mean(zq75),
            zq80 = mean(zq80),
            zq85 = mean(zq85),
            zq90 = mean (zq90),
            zq95 = mean(zq95),
            zpcum1 = mean(zpcum1),
            zpcum2 = mean(zpcum2),
            zpcum3 = mean(zpcum3),
            zpcum4 = mean(zpcum4),
            zpcum5 = mean(zpcum5),
            zpcum6 = mean(zpcum6),
            zpcum7 = mean(zpcum7),
            zpcum8 = mean(zpcum8),
            zpcum9 = mean(zpcum9)) %>%
  as.data.frame()
rownames(metrics2014b) = as.character(metrics2014b$transecto)
metrics2014b = metrics2014b[,-1]

metrics2017 = read.csv('./metrics2017.csv')
metrics2017 = metrics2017 %>%
  group_by(transecto) %>%
  summarise(zmax = mean(zmax),
            zmean = mean(zmean),
            zsd = mean(zsd),
            zskew = mean(zskew),
            zkurt = mean(zkurt),
            zentropy = mean(zentropy),
            pzabovezmean = mean(pzabovezmean),
            pzabove2 = mean(pzabove2),
            zq5 = mean(zq5),
            zq10 = mean(zq10),
            zq15 = mean (zq15),
            zq20 = mean(zq20),
            zq25 = mean(zq25),
            zq30 = mean(zq30),
            zq35 = mean(zq35),
            zq40 = mean(zq40),
            zq45 = mean(zq45),
            zq50 = mean(zq50),
            zq55 = mean(zq55),
            zq60 = mean(zq60),
            zq65 = mean(zq65),
            zq70 = mean(zq70),
            zq75 = mean(zq75),
            zq80 = mean(zq80),
            zq85 = mean(zq85),
            zq90 = mean(zq90),
            zq95 = mean(zq95),
            zpcum1 = mean(zpcum1),
            zpcum2 = mean(zpcum2),
            zpcum3 = mean(zpcum3),
            zpcum4 = mean(zpcum4),
            zpcum5 = mean(zpcum5),
            zpcum6 = mean(zpcum6),
            zpcum7 = mean(zpcum7),
            zpcum8 = mean(zpcum8),
            zpcum9 = mean(zpcum9)) %>%
  as.data.frame()
rownames(metrics2017) = as.character(metrics2017$transecto)
metrics2017 = metrics2017[,-1]

metrics2012scaled = scale(metrics2012)                        # standardize variables
d = dist(metrics2012scaled, method = "euclidean")             # distance matrix
metrics2012groups = hclust(d, method="ward")
plot(metrics2012groups)                                       # display dendogram

metrics2014scaled = scale(metrics2014)                        # standardize variables
d = dist(metrics2014scaled, method = "euclidean")             # distance matrix
metrics2014groups = hclust(d, method="ward")
plot(metrics2014groups, xlab = "Parcelas 2014")               # display dendogram

metrics2014bscaled = scale(metrics2014b)                        # standardize variables
d = dist(metrics2014bscaled, method = "euclidean")             # distance matrix
metrics2014bgroups = hclust(d, method="ward")
plot(metrics2014bgroups, xlab = "Parcelas 2014b")               # display dendogram

metrics2017scaled = scale(metrics2017)                        # standardize variables
d = dist(metrics2017scaled, method = "euclidean")             # distance matrix
metrics2017groups = hclust(d, method="ward")
plot(metrics2017groups, xlab = "Parcelas 2017")               # display dendogram

# Comparação dos dendrogramas para inventário
dendLidar12 <- as.dendrogram(metrics2012groups)
dendLidar14 <- as.dendrogram(metrics2014groups)
dendLidar14b <- as.dendrogram(metrics2014bgroups)
dendLidar17 <- as.dendrogram(metrics2017groups)

dendlist(dendLidar12, dendLidar14) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar12, dendLidar14)

dendlist(dendLidar14b, dendLidar17) %>%
  untangle(method = "step1side") %>% # Find the best alignment layout
  tanglegram()                       # Draw the two dendrograms

cor_cophenetic(dendLidar14b, dendLidar17)
