'''
PROCESSING UPA 3
execfile('C:\\FUSION\\daad\\coding\\upa3processing.py')
'''
STEP1 = False
STEP2 = False
STEP3 = False
STEP4 = False
STEP5 = False
STEP6 = False
STEP7 = True

print "Starting... 0 of 7."

'''
1. Criar modelo digital de terreno.
'''
execfile('C:\\FUSION\\daad\\coding\\dtm.py')
if STEP1:
	dtm(INLAS = "upa3.laz", FILTERCELL = "8", DTMCELL = "1", LASPATH = "C:\\FUSION\\daad\\las\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
print "Done 1 of 7."

'''
2. Superficies de custos relacionada ao terreno.
'''
execfile('C:\\FUSION\\daad\\coding\\slope.py')
if STEP2:
	slope(ASCDTM = "upa3_dtm.asc", RULESKIDDER = "ruleSkidder.txt", RULETRUCK = "ruleTruck.txt", RULEAPP45 = "ruleApp45.txt", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
print "Done 2 of 7."

'''
3. Superficie de custo relacionada a vegetacao
'''
execfile('C:\\FUSION\\daad\\coding\\chm.py')
if STEP3:
	chm(INLAS = "upa3.laz", DTM = "upa3_dtm.dtm", LASPATH = "C:\\FUSION\\daad\\las\\", DTMPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", CHMCELL = "1", RULEVEGETATION = None, EPSG = 31982, BIOMASS = True, GAP = True, EMERGENT = True, RDM = True, OPEN = True)
print "Done 3 of 7."

'''
4. Superficies de custos relacionada a recursos hidricos.
'''
execfile('C:\\FUSION\\daad\\coding\\drainage.py')
if STEP4:
	drainage(ASCMDT = "upa3_dtm.asc", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", MINFLOW = 55000, RES = 1, APP=True, EPSG = 31982, OPEN = True)
print "Done 4 of 7."

'''
5. Compor superficie de custo com layers de interesse.
'''
execfile('C:\\FUSION\\daad\\coding\\costSurf.py')
if STEP5:
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3="upa3_dtm_tciCost.tif", LAYER4="upa3_dtm_hdistCost.tif", LAYER5="upa3_rdmCost.tif", LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC1.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)

	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3="upa3_dtm_tciCost.tif", LAYER4="upa3_dtm_hdistCost.tif", LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC2.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3="upa3_dtm_tciCost.tif", LAYER4="upa3_rdmCost.tif", LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC3.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3="upa3_rdmCost.tif", LAYER4="upa3_dtm_hdistCost.tif", LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC4.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_rdmCost.tif", LAYER3="upa3_dtm_tciCost.tif", LAYER4="upa3_dtm_hdistCost.tif", LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC5.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3="upa3_dtm_tciCost.tif", LAYER4="upa3_dtm_hdistCost.tif", LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC6.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_dtm_tciCost.tif", LAYER3="upa3_dtm_slopeCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC7.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)	
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_dtm_tciCost.tif", LAYER3="upa3_dtm_hdistCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC8.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3="upa3_dtm_hdistCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC9.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_dtm_slopeCost.tif", LAYER3="upa3_dtm_hdistCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC10.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_dtm_tciCost.tif", LAYER3="upa3_chm_vegCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC11.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_dtm_slopeCost.tif", LAYER3="upa3_chm_vegCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC12.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_tciCost.tif", LAYER2="upa3_dtm_hdistCost.tif", LAYER3="upa3_chm_vegCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC13.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_dtm_tciCost.tif", LAYER3="upa3_dtm_hdistCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC14.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_dtm_hdistCost.tif", LAYER3="upa3_chm_vegCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC15.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_dtm_tciCost.tif", LAYER3="upa3_chm_vegCost.tif", LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC16.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_dtm_tciCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC17.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_rdmCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC18.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_dtm_hdistCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC19.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_slopeCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC20.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_tciCost.tif", LAYER2="upa3_rdmCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC21.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_tciCost.tif", LAYER2="upa3_dtm_hdistCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC22.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_tciCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC23.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_dtm_hdistCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC24.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_rdmCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC25.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	cost(LAYER1="upa3_dtm_hdistCost.tif", LAYER2="upa3_chm_vegCost.tif", LAYER3=None, LAYER4=None, LAYER5=None, LAYER6=None, LAYER7=None, LAYER8=None, LAYER9=None, OUTFILE = "SC26.tif", INPATH="C:\\FUSION\\daad\\upa3\\", OUTPATH="C:\\FUSION\\daad\\upa3\\", EPSG=31982, OPEN=True)
	
	print "Done 5 of 7."
	
'''
6. Extrair coordenadas das arvores emergentes.
'''
execfile('C:\\FUSION\\daad\\coding\\tree.py')
if STEP6:
	tree(CHMASC = "upa3_chm.asc", COPA = 9, TOPMASK = "crownMask.tif", EPSG = 31982, export = True, INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\")
print "Done 6 of 7."

'''
7. Criar superficie de custo acumulado.
'''
execfile('C:\\FUSION\\daad\\coding\\opt.py')
if STEP7:

	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC1.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC2.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC3.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC4.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC5.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC6.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC7.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC8.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC9.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC10.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC11.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC12.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC13.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC14.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC15.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC16.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC17.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC18.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC19.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC20.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC21.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC22.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC23.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC24.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC25.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
	opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "SC26.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True)
	
print "Done 7 of 7. Ready!"
