#setwd('/home/gorgens/Documents/R julia pibic/')

require(lidR)
require(raster)

# ground classification
ctg = readLAScatalog("./2014/org/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 500
opt_output_files(ctg) = "./2014/gnd/cau2014_gnd{ID}"
classified_ctg = classify_ground(ctg, csf())
rm(classified_ctg)

# digital terrain model creation
ctg = readLAScatalog("./2014/gnd/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 500
opt_output_files(ctg) = "./2014/dtm/cau2014_dtm{ID}"
dtm_ctg = grid_terrain(ctg, res = 1, algorithm = tin())

# normalize cloud
dtm_ctg = raster('./2014/dtm/grid_terrain.vrt')
ctg = readLAScatalog("./2014/gnd/")
opt_chunk_buffer(ctg) = 30
opt_chunk_size(ctg) = 250
opt_output_files(ctg) = "./2014/norm/cau2014_norm{ID}"
norm_ctg = normalize_height(ctg, dtm_ctg)
rm(dtm_ctg, norm_ctg)
