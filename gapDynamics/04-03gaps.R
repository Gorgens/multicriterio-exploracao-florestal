require(raster)
require(ForestGapR)
require(tools)
require(dplyr)
require(sf)
require(purrr)
require(rgeos)

# Extract gaps
chmList = list.files('./ducke_2020/chm/', pattern = '\\.tif$')
# chmList = chmList[61:71]

shapefileGaps = function(file,
                          inPath = './ducke_2020/chm/',
                          outPath = './ducke_2020/gaps/',
                          threshold = 10,
                          size = c(10, 10000)){
  gapsRaster = raster(paste0(inPath, file))
  gaps = getForestGaps(chm_layer=gapsRaster, 
                       threshold=threshold, size=size)
  gapsShape = GapSPDF(gap_layer=gaps)
  shapefile(gapsShape, filename=paste0(outPath, tools::file_path_sans_ext(file),'.shp'))
  return(paste0('Ready: ', file))
}

lapply(chmList, shapefileGaps)

# Merge gaps
list.files('./ducke_2020/gaps/', pattern = '\\.shp$', full.names = TRUE) %>% 
  map(read_sf) %>%
  do.call(rbind, .) %>%
  write_sf('./ducke_2020/ducke_2020gaps.shp')
shapefile('./ducke_2020/ducke_2020gaps.shp') %>%
  gBuffer(byid=TRUE, width=0) %>%
  aggregate() %>%
  disaggregate() %>%
  shapefile('./ducke_2020/ducke_2020gapsAggregated.shp', overwrite=TRUE)
