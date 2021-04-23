#setwd('/home/gorgens/Documents/R gap dynamics')

require(lidR)
require(raster)

# ground classification
ctg = readLAScatalog("./jari_2017d/org2/")
opt_select(ctg) <- "xyz"
opt_filter(ctg) = '-drop_z_below 0'
opt_chunk_buffer(ctg) = 30
opt_output_files(ctg) = "./jari_2017d/gnd/jari_2017d_gnd{ID}"
classified_ctg = classify_ground(ctg, csf())
rm(classified_ctg)

# digital terrain model creation
ctg = readLAScatalog("./jari_2017d/gnd/")
opt_chunk_buffer(ctg) = 30
opt_output_files(ctg) = "./jari_2017d/dtm/jari_2017d_dtm{ID}"
dtm_ctg = grid_terrain(ctg, res = 1, algorithm = tin())

# normalize cloud
ctg = readLAScatalog("./jari_2017d/gnd/")
opt_chunk_buffer(ctg) = 30
opt_stop_early(ctg) = FALSE
opt_output_files(ctg) = "./jari_2017d/norm/jari_2017d_norm{ID}"
# dtm_ctg = raster('./jari_2017d/a/dtm/grid_terrain.vrt')
norm_ctg = normalize_height(ctg, dtm_ctg)
rm(dtm_ctg, norm_ctg)

# canopy height model creation
ctg = readLAScatalog("./jari_2017d/norm/")
opt_stop_early(ctg) = FALSE
opt_chunk_buffer(ctg) = 30
opt_output_files(ctg) = "./jari_2017d/chm/jari_2017d_chm{ID}"
chm_ctg = grid_canopy(ctg, res = 0.5, p2r(0.2, na.fill = tin()))
rm(chm_ctg, ctg)
