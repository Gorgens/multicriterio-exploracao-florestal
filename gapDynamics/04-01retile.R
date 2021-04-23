require(lidR)
require(raster)

# Load data and check extention
ctg = readLAScatalog("./jari_2017d/org/")
opt_select(ctg) <- "xyz"
opt_chunk_size(ctg) = 1000
opt_chunk_buffer(ctg) = 0
opt_chunk_alignment(ctg) = c(1000, 1000)
plot(ctg, chunk = TRUE)

# if necessary retile
opt_output_files(ctg) = "./jari_2017d/org2/NP_T-0523_tile{ID}"
catalog_retile(ctg)


