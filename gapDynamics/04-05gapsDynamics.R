require(raster)
require(sp)
require(ggplot2)
require(networkD3)
require(dplyr)
require(magrittr)

# Sankey plot
gapsDucke = shapefile('./dynamicsModeling/duckeGaps.shp')
links = gapsDucke@data %>%
  group_by(source, target) %>%
  summarise(area = sum(area))
nodes = data.frame(name = c(as.character(links$source), 
                            as.character(links$target)) %>% unique())
links$IDsource = match(links$source, nodes$name)-1 
links$IDtarget = match(links$target, nodes$name)-1
p = sankeyNetwork(Links = links, Nodes = nodes,
                  Source = "IDsource", Target = "IDtarget",
                  Value = "area", NodeID = "name", 
                  sinksRight=FALSE)
p