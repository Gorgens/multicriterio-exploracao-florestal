#setwd('/home/gorgens/Documents/R gap dynamics')

require(lidR)
require(raster)

# ground classification
ctg = readLAScatalog("./tanguro_2018/org/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 500
opt_output_files(ctg) = "./tanguro_2018/gnd/tanguro_2018_gnd{ID}"
classified_ctg = classify_ground(ctg, csf())
rm(classified_ctg)

# digital terrain model creation
ctg = readLAScatalog("./tanguro_2018/gnd/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 500
opt_output_files(ctg) = "./tanguro_2018/dtm/tanguro_2018_dtm{ID}"
dtm_ctg = grid_terrain(ctg, res = 1, algorithm = tin())

# normalize cloud
ctg = readLAScatalog("./tanguro_2018/gnd/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 500
opt_output_files(ctg) = "./tanguro_2018/norm/tanguro_2018_norm{ID}"
#dtm_ctg = raster('./tanguro_2018/a/dtm/grid_terrain.vrt')
norm_ctg = normalize_height(ctg, dtm_ctg)
rm(dtm_ctg, norm_ctg)

# canopy height model creation
ctg = readLAScatalog("./tanguro_2018/norm/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 500
opt_output_files(ctg) = "./tanguro_2018/chm/tanguro_2018_chm{ID}"
chm_ctg = grid_canopy(ctg, res = 0.5, p2r(0.2, na.fill = tin()))
rm(chm_ctg, ctg)
