require(raster)
require(ForestGapR)
require(tools)
require(dplyr)
require(sf)
require(purrr)
require(rgeos)

# Extract gaps
chmList = list.files('./jari_2017d/chm/', pattern = '\\.tif$')
#chmList = chmList[58:61]

shapefileGaps = function(file,
                          inPath = './jari_2017d/chm/',
                          outPath = './jari_2017d/gaps/',
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
list.files('./jari_2017d/gaps/', pattern = '\\.shp$', full.names = TRUE) %>% 
  map(read_sf) %>%
  do.call(rbind, .) %>%
  write_sf('./jari_2017d/jari_2017dgaps.shp')
shapefile('./jari_2017d/jari_2017dgaps.shp') %>%
  gBuffer(byid=TRUE, width=0) %>%
  aggregate() %>%
  disaggregate() %>%
  shapefile('./jari_2017d/jari_2017dgapsAggregated.shp', overwrite=TRUE)
