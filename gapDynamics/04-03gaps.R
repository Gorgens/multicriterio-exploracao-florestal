require(raster)
require(ForestGapR)
require(tools)
require(dplyr)
require(sf)
require(purrr)
require(rgeos)

# Extract gaps
chmList = list.files('./jari_2020/a/chm/', pattern = '\\.tif$')
# chmList = chmList[44:51]

shapefileGaps = function(file,
                          inPath = './jari_2020/a/chm/',
                          outPath = './jari_2020/a/gaps/',
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
list.files('./jari_2020/a/gaps/', pattern = '\\.shp$', full.names = TRUE) %>% 
  map(read_sf) %>%
  do.call(rbind, .) %>%
  write_sf('./jari_2020/a/jari_2020gaps.shp')
shapefile('./jari_2020/a/jari_2020gaps.shp') %>%
  gBuffer(byid=TRUE, width=0) %>%
  aggregate() %>%
  disaggregate() %>%
  shapefile('./jari_2020/a/jari_2020gapsAggregated.shp', overwrite=TRUE)
