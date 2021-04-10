require(raster)
require(ForestGapR)
require(tools)
require(dplyr)
require(sf)
require(purrr)
require(rgeos)

# Extract gaps
chmList = list.files('./tanguro_2018/chm/', pattern = '\\.tif$')

shapefileGaps = function(file,
                          inPath = './tanguro_2018/chm/',
                          outPath = './tanguro_2018/gaps/',
                          threshold = 10,
                          size = c(9, 100000)){
  gapsRaster = raster(paste0(inPath, file))
  gaps = getForestGaps(chm_layer=gapsRaster, 
                       threshold=threshold, size=size)
  gapsShape = GapSPDF(gap_layer=gaps)
  shapefile(gapsShape, filename=paste0(outPath, tools::file_path_sans_ext(file),'.shp'))
  return(paste0('Ready: ', file))
}

lapply(chmList, shapefileGaps)

# Merge gaps
list.files(inPath, pattern = '\\.shp$', full.names = TRUE) %>% 
  map(read_sf) %>%
  do.call(rbind, .) %>%
  write_sf('./tanguro_2018/tanguro_2018gaps.shp')
shapefile('./tanguro_2018/tanguro_2018gaps.shp') %>%
  gBuffer(tanguro_2018gaps, byid=TRUE, width=0) %>%
  aggregate(tanguro_2018gaps) %>%
  disaggregate(tanguro_2018gaps) %>%
  shapefile('./tanguro_2018/tanguro_2018gapsAggregated.shp', overwrite=TRUE)
