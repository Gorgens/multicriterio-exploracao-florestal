require(raster)
require(sp)
require(ggplot2)
require(networkD3)
require(dplyr)
require(magrittr)
require(poweRlaw)

## Primeiro sobrevoo ---------------------
gapsDucke2017 = shapefile('./ducke_2017/ducke_2017gapsAggregated.shp')
crs(gapsDucke2017) = '+proj=utm +zone=21 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
gapsDucke2017$area = area(gapsDucke2017)
gapsDucke2017$area %<>% floor()
gapsDucke2017 = subset(gapsDucke2017, area > 10)

ggplot(gapsDucke2017@data, aes(area)) +                                         # histograma do tamanhop de gaps
  geom_histogram(aes(y = stat(count / sum(count)))) +
  xlim(10, 250) + ylim(0, 0.3) + ggtitle('Ducke 2017') +
  labs(x = 'Area (m²)', y = "Frequency")

gapsDucke2017resume = gapsDucke2017@data %>%                                    # count number of gaps per area bins
  mutate(bin = floor(area/2)*2+1) %>%
  group_by(bin) %>%
  count(bin)
  
ggplot(gapsDucke2017resume) +                                                   # gráfico log-log da área pela frequência
  geom_point(aes(bin, n)) +
  ggtitle('Ducke 2017') +
  scale_x_log10() + scale_y_log10()

m = displ$new(gapsDucke2017$area)                                               # ajustes da função da potência em que Prob = c * areaGap ^ alpha
m$setXmin(10)
estimate_pars(m)[["pars"]]


## Segundo sobrevoo ---------------------
gapsDucke2020 = shapefile('./ducke_2020/ducke_2020gapsAggregated.shp')
crs(gapsDucke2020) = '+proj=utm +zone=22 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
gapsDucke2020 = spTransform(gapsDucke2020, crs(gapsDucke2017))
gapsDucke2020$area = area(gapsDucke2020)
gapsDucke2020$area %<>% floor()
gapsDucke2020 = subset(gapsDucke2020, area > 10)

ggplot(gapsDucke2020@data, aes(area)) +                                         # histograma do tamanhop de gaps
  geom_histogram(aes(y = stat(count / sum(count)))) +
  xlim(10, 250) + ylim(0, 0.3) + ggtitle('Ducke 2020') +
  labs(x = 'Area (m²)', y = "Frequency")

gapsDucke2020resume = gapsDucke2020@data %>%                                    # count number of gaps per area bins
  mutate(bin = floor(area/2)*2+1) %>%
  group_by(bin) %>%
  count(bin)

ggplot(gapsDucke2020resume) +                                                   # gráfico log-log da área pela frequência
  geom_point(aes(bin, n)) +
  ggtitle('Ducke 2020') +
  scale_x_log10() + scale_y_log10()

m = displ$new(gapsDucke2020$area)                                               # ajustes da função da potência em que Prob = c * areaGap ^ alpha
m$setXmin(10)
estimate_pars(m)[["pars"]]


