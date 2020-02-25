'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\daad\\coding\\slope.py')
'''
def slope(ASCDTM = "upa3_dtm.asc", RULESKIDDER = "ruleSkidder.txt", RULETRUCK = "ruleTruck.txt", RULEAPP45 = "ruleApp45.txt", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True):
	import processing
	import subprocess
	import os
	from osgeo import ogr
	
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)
	
	# print "Loading digital terrain model."
	dtmlayer = QgsRasterLayer(INPATH+ASCDTM, "MDT temp")
	dtmlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(dtmlayer)
	extent = dtmlayer.extent()
	xmin = extent.xMinimum()
	xmax = extent.xMaximum()
	ymin = extent.yMinimum()
	ymax = extent.yMaximum()
	
	print "Computing slope."
	processing.runalg("grass7:r.slope", dtmlayer, 0, False, 1, 0, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_slope.tif")
	slope = QgsRasterLayer(OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_slope.tif", "Digital slope model")
	slope.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(slope)
	
	# print "Creating cost surface based on slope."
	extent = slope.extent()
	provider = slope.dataProvider()
	stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
	MAX = str(round(stats.maximumValue))
	processing.runalg("saga:rastercalculator", slope, None, '"(1-(('+MAX+'-a)/'+MAX+'))*10"', 3, False, 7, OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_slopeCost.tif")
	slopeCost = QgsRasterLayer(OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_slopeCost.tif", "slopeCost")
	slopeCost.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(slopeCost)
	
	if RULESKIDDER != None:
		print "Computing skidder restriction."
		processing.runalg("grass7:r.reclass", slope, INPATH+RULESKIDDER, "", "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_logRestriction.tif")

		if OPEN:
			loggingcost = QgsRasterLayer(OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_logRestriction.tif", "Logging restriction model")
			loggingcost.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(loggingcost)

	if RULETRUCK != None:
		print "Computing load truck restriction."
		processing.runalg("grass7:r.reclass", slope, INPATH+RULETRUCK, "", "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_transRestriction.tif")

		if OPEN:
			transportCost = QgsRasterLayer(OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_transRestriction.tif", "Transportation restriction model")
			transportCost.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(transportCost)

	if RULEAPP45 != None:
		print "Computing slope greater than 45 restriction."
		processing.runalg("grass7:r.reclass", slope, INPATH+RULEAPP45, "", "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_slp45Restriction.tif")
		
		if OPEN:
			app45Cost = QgsRasterLayer(OUTPATH+ASCDTM[0:len(ASCDTM)-4] + "_slp45Restriction.tif", "Slope 45 restriction model")
			app45Cost.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(app45Cost)
	
	# print "Cleaning QGIS canvas."
	QgsMapLayerRegistry.instance().removeMapLayer(dtmlayer.id())
	if OPEN != True:
		QgsMapLayerRegistry.instance().removeMapLayer(slope.id())
		QgsMapLayerRegistry.instance().removeMapLayer(slopeCost.id())
		
	return