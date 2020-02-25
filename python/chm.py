'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\zf2\\julia\\lidar\\chm.py')
'''
def chm(INLAS = "upa3.laz", DTM = "upa3_dtm.dtm", LASPATH = "C:\\FUSION\\daad\\las\\", DTMPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", CHMCELL = "1", RULEVEGETATION = "ruleVegetation.txt", EPSG = 31982, BIOMASS = True, GAP = True, EMERGENT = True, RDM = True, OPEN = True):
	import processing
	import subprocess
	import math
	
	GND = "/ground:" + DTMPATH + DTM
	ASC = "/ascii"
	CHMFUN = "c:\\fusion\\canopymodel"
	
	print 'Computing CHM.'
	ch=subprocess.call([CHMFUN, GND, ASC, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm.dtm", CHMCELL, "m", "m", "1", "22", "0", "0", LASPATH+INLAS], shell=True)
	if ch == 0:
		print "CHM created."
	else:
		print "Check the code, and try again."
		return
	
	# print "Loading CHM to canvas."
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)
	chmlayer = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_chm.asc", "Canopy height model")
	chmlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(chmlayer)
	extent = chmlayer.extent()
	xmin = extent.xMinimum()
	xmax = extent.xMaximum()
	ymin = extent.yMinimum()
	ymax = extent.yMaximum()
	
	print "Computing vegetation surface cost."
	if RULEVEGETATION != None:
		# print 'rule based'
		processing.runalg("grass7:r.reclass", chmlayer, OUTPATH+RULEVEGETATION, "", "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_vegCost.tif")
	else:
		# print 'minmax based'
		extent = chmlayer.extent()
		provider = chmlayer.dataProvider()
		stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
		MAX = str(round(stats.maximumValue))
		if stats.minimumValue < 0:
			MIN = str(0)
		else:
			MIN = str(round(stats.minimumValue))
		processing.runalg("saga:rastercalculator", chmlayer, None, '"(a-'+MIN+')/('+MAX+'-'+MIN+')*100"', 3, False, 7, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_vegCost.tif")
	
	# print "Loading vegetation surface cost to canvas."	
	if OPEN:
		vegetationCost = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_vegCost.tif", "chmCost")
		vegetationCost.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(vegetationCost)

	if BIOMASS:
		print "Computing top canopy height model."
		processing.runalg('grass7:r.resamp.stats', chmlayer, 0, False, False, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 50, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_tch.tif")
		tchlayer = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_tch.tif", "Top canopy height model")
		tchlayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(tchlayer)
		
		print "Computing the biomass digital model."
		processing.runalg("saga:rastercalculator", tchlayer, None, "(0.054*((a)^1.76))*2", 3, False, 7, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_biomass.tif")	
		if OPEN:
			vollayer = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_biomass.tif", "Digital biomass model")
			vollayer.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(vollayer)
		else:
			QgsMapLayerRegistry.instance().removeMapLayer(tchlayer.id())
	

	if GAP:
		print "Computing gap model."
		HEIGHT = 10	
		CALC = "ifelse(a>"+str(HEIGHT)+",10,1)"
		processing.runalg("saga:rastercalculator", chmlayer, None, CALC, 3, False, 7, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_gap.tif")
		if OPEN:
			gapModel = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_gap.tif", "Digital GAPs model")
			gapModel.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(gapModel)

	if EMERGENT:
		print "Computing emergent canopy model."
		extent = chmlayer.extent()
		provider = chmlayer.dataProvider()
		stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
		HEIGHT = str(round(stats.mean + 2. * stats.stdDev))	
		CALC = "ifelse(a>"+str(HEIGHT)+",10,1)"
		processing.runalg("saga:rastercalculator", chmlayer, None, CALC, 3, False, 7, OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_emergent.tif")
		if OPEN:
			emergentModel = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_chm_emergent.tif", "Emergent canopy model")
			emergentModel.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(emergentModel)
			
	if RDM:	
		print 'Computing relative density model.'
		
		RDMFUN = "C:\\FUSION\\Cover"
		ALL = "/all"
		UPPER = "/upper:5"
		RDMFILE = OUTPATH+INLAS[0:len(INLAS)-4] + "_rdm.dtm"
		
		ch=subprocess.call([RDMFUN, ALL, UPPER, DTMPATH + DTM, RDMFILE, "1", "1", "m", "m", "1", "0", "0", "0", LASPATH+INLAS], shell=True)
		if ch == 0:
			print "RDM Computed."
		else:
			print "Check the code, and try again."
			return
		
		# print "Converting rdm to asc."
		ASCFUN = "c:\\fusion\\dtm2ascii"
		RDMASC = OUTPATH+INLAS[0:len(INLAS)-4] + "_rdm.asc"
		ch=subprocess.call([ASCFUN, RDMFILE, RDMASC], shell=True)
		if ch == 0:
			print "DTM conveted to ASCII."
		else:
			print "Check the code, and try again."
			return
		
		# print "Loading RDM to canvas."
		rdmlayer = QgsRasterLayer(RDMASC, "Relative density model")
		rdmlayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(rdmlayer)
			
		processing.runalg("saga:rastercalculator", rdmlayer, None, "a/10", 3, False, 7, OUTPATH+INLAS[0:len(INLAS)-4] + "_rdmCost.tif")
		rdmCost = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_rdmCost.tif", "rdmCost")
		rdmCost.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(rdmCost)
			
	if OPEN != True:
		QgsMapLayerRegistry.instance().removeMapLayer(chmlayer.id())
		QgsMapLayerRegistry.instance().removeMapLayer(rdmlayer.id())
		QgsMapLayerRegistry.instance().removeMapLayer(rdmCost.id())
		
	return