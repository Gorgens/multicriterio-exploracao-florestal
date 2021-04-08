require(raster)
library(plotly)

# Distribution gaps
gaps.shp = shapefile('./zf2a_gaps/zf2a_gaps.shp')
fig = plot_ly(x = ~gaps.shp$area, 
               type = "histogram",
               histnorm = "probability")
fig = layout(fig, bargap=0.1)
fig
