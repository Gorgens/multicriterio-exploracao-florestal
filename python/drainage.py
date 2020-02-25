'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\daad\\drainage.py')
'''
def drainage(ASCMDT = "upa3_dtm.asc", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", MINFLOW = 55000, RES = 1, APP = True, FLOOD = True, EPSG = 31982, OPEN = True):
	
	import processing
	import subprocess
	import os
	from osgeo import ogr
	import math
	
	'define projecao a ser usada'
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)
	
	# print "Loading the digital terrain model."
	dtmlayer = QgsRasterLayer(INPATH+ASCMDT, "mdt temp")
	dtmlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(dtmlayer)
	extent = dtmlayer.extent()
	xmin = extent.xMinimum()
	xmax = extent.xMaximum()
	ymin = extent.yMinimum()
	ymax = extent.yMaximum()
	
	print "Computing topographic moisture index."
	processing.runalg("grass7:r.terraflow", dtmlayer, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_filled.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_direc.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_watershed.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_accum.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_tci.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_stats.txt")
	tci = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_tci.tif", "Topographic wetness model")
	tci.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(tci)
	
	# print "Creating cost surface based on topographic moisture index."
	extent = tci.extent()
	provider = tci.dataProvider()
	stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
	MAX = str(round(stats.maximumValue))
	MIN = str(abs(math.floor(stats.minimumValue)))
	if stats.minimumValue < 0:
		processing.runalg("saga:rastercalculator", tci, None, '"((a+'+MIN+')/('+MAX+'+'+MIN+'))*10"', 3, False, 7, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_tciCost.tif")
	else:
		processing.runalg("saga:rastercalculator", tci, None, '"((a-'+MIN+')/('+MAX+'-'+MIN+'))*10"', 3, False, 7, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_tciCost.tif")
	if OPEN:
		tciCost = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_tciCost.tif", "tciCost")
		tciCost.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(tciCost)
	else:
		QgsMapLayerRegistry.instance().removeMapLayer(tci.id())
		
	print "Extracting drainage network."
	processing.runalg("grass7:r.stream.extract", dtmlayer, "", "", MINFLOW, 0, 0, 0, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, 0, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_stream.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_idstream.shp", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_direc2.tif")
	streamlayer = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_stream.tif", "Digital drainage network")
	streamlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(streamlayer)
	
	# print "Converting drainage raster to vector."
	processing.runalg("grass7:r.to.vect", streamlayer, 0, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_vstream.shp")
	if OPEN:
		vstreamlayer = QgsVectorLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_vstream.shp", "Drainage network", "ogr")
		vstreamlayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(vstreamlayer)
		
	print "Computing horizontal distance to drainage."
	processing.runalg("grass7:r.grow.distance", streamlayer, 0, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_hdist.tif", OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_vdist.tif")
	hdist = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_hdist.tif", "Digital horizontal distance model")
	hdist.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(hdist)
	if OPEN:
		vdist = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_vdist.tif", "Digital vertical distance model")
		vdist.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(vdist)
	else:
		QgsMapLayerRegistry.instance().removeMapLayer(streamlayer.id())

	
	# print "Creating cost surface based on to horizontal distance."
	extent = hdist.extent()
	provider = hdist.dataProvider()
	stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
	MAX = str(round(stats.maximumValue))
	processing.runalg("saga:rastercalculator", hdist, None, '"(('+MAX+'-a)/'+MAX+')*10"', 3, False, 7, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_hdistCost.tif")
	if OPEN:
		hdistcost = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_hdistCost.tif", "hdistCost")
		hdistcost.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(hdistcost)
	
	if APP:
		print "Computing stream restrictions."
		DIST = 50	
		CALC = "ifelse(a>"+str(DIST)+",1,10)"
		processing.runalg("saga:rastercalculator", hdist, None, CALC, 3, False, 7, OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_hdist_app.tif")
		if OPEN:
			appModel = QgsRasterLayer(OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_hdist_app.tif", "Stream restriction model")
			appModel.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(appModel)
		else:
			QgsMapLayerRegistry.instance().removeMapLayer(hdist.id())

	
	if FLOOD:
		print "Computing the harzard flood model"
		accumulation = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_accum.tif"
		acclayer = QgsRasterLayer(accumulation, "Digital accumulation model")
		acclayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(acclayer)

		slope = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_slope.tif"
		slplayer = QgsRasterLayer(slope, "Slope temp")
		slplayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(slplayer)
			
		n = 0.016 * (RES ** 0.46)
		CALC = "log((pow(((a+1)*"+str(RES)+") , "+str(n)+")) / (tan(b+0.001)))"
		rmti = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_rmti.tif"
		processing.runalg("saga:rastercalculator", acclayer, [slplayer], CALC, 3, False, 7, rmti)
		rmtilayer = QgsRasterLayer(rmti, "RMTI")
		rmtilayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(rmtilayer)

		rflood = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_rflood.tif"
		mti_th = 10.89 * n + 2.282
		CALC = "ifelse(a>"+str(mti_th)+",1,0)"
		processing.runalg("saga:rastercalculator", rmtilayer, None, CALC, 3, False, 7, rflood)
		rfloodlayer = QgsRasterLayer(rflood, "RFLOOD")
		rfloodlayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(rfloodlayer)
		QgsMapLayerRegistry.instance().removeMapLayer(rmtilayer.id())

		title = "Flood"
		rclump =  OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_clump.tif"
		processing.runalg("grass7:r.clump", rfloodlayer, title, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, rclump)  
		rclumplayer = QgsRasterLayer(rclump, "RCLUMP")
		rclumplayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(rclumplayer)
		QgsMapLayerRegistry.instance().removeMapLayer(rfloodlayer.id())

		harzardFlood =  OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_harzFlood.tif"
		extent = rclumplayer.extent()
		provider = rclumplayer.dataProvider()
		stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
		MAX = str(round(stats.maximumValue))
		if stats.minimumValue < 0:
			MIN = str(0)
		else:
			MIN = str(round(stats.minimumValue))
		processing.runalg("saga:rastercalculator", rclumplayer, None, '"(a-'+MIN+')/('+MAX+'-'+MIN+')*10"', 3, False, 7, harzardFlood)
		if OPEN:
			harzflood = QgsRasterLayer(harzardFlood, "Digital flood model")
			harzflood.setCrs(crs)
			QgsMapLayerRegistry.instance().addMapLayer(harzflood)
		else:
			QgsMapLayerRegistry.instance().removeMapLayer(acclayer.id())
			
		QgsMapLayerRegistry.instance().removeMapLayer(rclumplayer.id())	
		QgsMapLayerRegistry.instance().removeMapLayer(slplayer.id())
	
	QgsMapLayerRegistry.instance().removeMapLayer(dtmlayer.id())

	return