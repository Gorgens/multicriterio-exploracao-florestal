require(raster)
require(ForestGapR)
require(tools)
require(dplyr)

# Extract gaps
chmList = list.files('./ducke_2017/chm/', pattern = '\\.tif$')

threshold = 10
size = c(9, 100000)

for(i in chmList){
  gapsRaster = raster(paste0('./ducke_2017/chm/', i))
  gaps = getForestGaps(chm_layer=gapsRaster, 
                       threshold=threshold, size=size)
  gapsShape = GapSPDF(gap_layer=gaps)
  gapsStats = GapStats(gap_layer=gaps, chm_layer=gapsRaster)
  gapsStats = as.data.frame(as.matrix(gapsStats))
  gapsShape<-merge(gapsShape,gapsStats, by="gap_id")
  shapefile(gapsShape, filename=paste0('./ducke_2017/gaps/', 
                                       tools::file_path_sans_ext(i),'.shp'))
}