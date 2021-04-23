require(raster)
require(sp)
require(ggplot2)
require(dplyr)
require(magrittr)
require(poweRlaw)

## Primeiro sobrevoo ---------------------
areaYear1 = shapefile('./ducke_2017/ducke_2017gapsExtracted31981.shp')
# crs(areaYear1) = '+proj=utm +zone=22 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
areaYear1$ano17 = 'gap'
areaYear1$area = area(areaYear1)
areaYear1$area %<>% floor()
areaYear1 = subset(areaYear1, area > 10)
areaYear1 %>% shapefile('./ducke_2017/ducke_2017gapsClean.shp', overwrite=TRUE)

ggplot(areaYear1@data, aes(area)) +                                         # histograma do tamanhop de gaps
  geom_histogram(aes(y = stat(count / sum(count)))) +
  xlim(10, 250) + ylim(0, 0.3) + ggtitle('ducke_2017') +
  labs(x = 'Area (m²)', y = "Frequency")

areaYear1resume = areaYear1@data %>%                                    # count number of gaps per area bins
  mutate(bin = floor(area/2)*2+1) %>%
  group_by(bin) %>%
  count(bin)
  
ggplot(areaYear1resume) +                                                   # gráfico log-log da área pela frequência
  geom_point(aes(bin, n)) +
  ggtitle('ducke_2017') +
  scale_x_log10() + scale_y_log10()

m = displ$new(areaYear1$area)                                               # ajustes da função da potência em que Prob = c * areaGap ^ alpha
m$setXmin(10)
estimate_pars(m)[["pars"]]


## Segundo sobrevoo ---------------------
areaYear2 = shapefile('./ducke_2020/ducke_2020gapsExtracted31981.shp')
# crs(areaYear2) = '+proj=utm +zone=22 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
#areaYear2 = spTransform(areaYear2, crs(areaYear1))
areaYear2$ano20 = 'gap'
areaYear2$area = area(areaYear2)
areaYear2$area %<>% floor()
areaYear2 = subset(areaYear2, area > 10)
areaYear2 %>% shapefile('./ducke_2020/ducke_2020gapsClean.shp', overwrite=TRUE)

ggplot(areaYear2@data, aes(area)) +                                         # histograma do tamanhop de gaps
  geom_histogram(aes(y = stat(count / sum(count)))) +
  xlim(10, 250) + ylim(0, 0.3) + ggtitle('ducke_2020') +
  labs(x = 'Area (m²)', y = "Frequency")

areaYear2resume = areaYear2@data %>%                                    # count number of gaps per area bins
  mutate(bin = floor(area/2)*2+1) %>%
  group_by(bin) %>%
  count(bin)

ggplot(areaYear2resume) +                                                   # gráfico log-log da área pela frequência
  geom_point(aes(bin, n)) +
  ggtitle('ducke_2020') +
  scale_x_log10() + scale_y_log10()

m = displ$new(areaYear2$area)                                               # ajustes da função da potência em que Prob = c * areaGap ^ alpha
m$setXmin(10)
estimate_pars(m)[["pars"]]


