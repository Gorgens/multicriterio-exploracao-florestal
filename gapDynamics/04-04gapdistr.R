require(raster)
require(sp)
library(ggplot2)

# Distribution gaps
gapsDucke2017 = shapefile('./ducke_2017/ducke_2017gapsAggregated.shp')
crs(gapsDucke2017) = '+proj=utm +zone=21 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
gapsDucke2017$area = area(gapsDucke2017) / 10000
# max(gapsDucke2017$area)
ggplot(gapsDucke2017@data, aes(area)) +
  geom_histogram(aes(y = stat(count / sum(count)))) +
  xlim(0, 0.05) + ylim(0, 0.5) + ggtitle('Ducke 2017')

gapsDucke2020 = shapefile('./ducke_2020/ducke_2020gapsAggregated.shp')
gapsDucke2020$area = area(gapsDucke2020) / 10000
# max(gapsDucke2020$area)
ggplot(gapsDucke2020@data, aes(area)) +
  geom_histogram(aes(y = stat(count / sum(count)))) + 
  xlim(0, 0.05) + ylim(0, 0.5) + ggtitle('Ducke 2020')

gapsTanguro2018 = shapefile('./tanguro_2018/tanguro_2018gapsAggregated.shp')
crs(gapsTanguro2018) = '+proj=utm +zone=22 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
gapsTanguro2018$area = area(gapsTanguro2018) / 10000
# max(gapsTanguro2018$area)
ggplot(gapsTanguro2018@data, aes(area)) +
  geom_histogram(aes(y = stat(count / sum(count)))) + 
  xlim(0, 0.05) + ylim(0, 0.5) + ggtitle('Tanguro 2018')

gapsTanguro2020 = shapefile('./tanguro_2020/tanguro_2020gapsAggregated.shp')
gapsTanguro2020$area = area(gapsTanguro2020) / 10000
# max(gapsTanguro2020$area)
ggplot(gapsTanguro2020@data, aes(area)) +
  geom_histogram(aes(y = stat(count / sum(count)))) +
  xlim(0, 0.05) + ylim(0, 0.5) + ggtitle('Tanguro 2020')

gapsTapajos2017 = shapefile('./tapajos_2017/tapajos_2017gapsAggregated.shp')
crs(gapsTapajos2017) = '+proj=utm +zone=21 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
gapsTapajos2017$area = area(gapsTapajos2017) / 10000
# max(gapsTapajos2017$area)
ggplot(gapsTapajos2017@data, aes(area)) +
  geom_histogram(aes(y = stat(count / sum(count)))) + 
  xlim(0, 0.05) + ylim(0, 0.5) + ggtitle('Tapajos 2017')

gapsTapajos2020 = shapefile('./tapajos_2020/tapajos_2020gapsAggregated.shp')
gapsTapajos2020$area = area(gapsTapajos2020) / 10000
# max(gapsTapajos2020$area)
ggplot(gapsTapajos2020@data, aes(area)) +
  geom_histogram(aes(y = stat(count / sum(count)))) + 
  xlim(0, 0.05) + ylim(0, 0.5) + ggtitle('Tapajos 2020')
