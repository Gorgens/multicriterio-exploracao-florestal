'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\daad\\coding\\accCost.py')
'''

def opt(ELEVATION = "upa3_dtm.asc", SURFACECOST = "surfaceCost.tif", START = "start.shp", TREES = "emergentes2.shp", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True):
	
	import processing
	import subprocess
	import os
	from osgeo import ogr
	
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)
	
	# print "Loading digital terrain model."
	dtmlayer = QgsRasterLayer(INPATH+ELEVATION, "MDT temp")
	dtmlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(dtmlayer)
	extent = dtmlayer.extent()
	xmin = extent.xMinimum()
	xmax = extent.xMaximum()
	ymin = extent.yMinimum()
	ymax = extent.yMaximum()
	
	costlayer = QgsRasterLayer(INPATH+SURFACECOST, "Cost temp")
	costlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(costlayer)
	
	pointslayer = QgsVectorLayer(INPATH+START, "Start temp", "ogr")
	pointslayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(pointslayer)
	
	treeslayer = QgsVectorLayer(INPATH+TREES, "Trees temp", "ogr")
	treeslayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(treeslayer)
	
	print 'Computing accumulated cost'
	processing.runalg("grass7:r.walk.points", dtmlayer, costlayer, pointslayer, treeslayer, "0.72,6.0,1.9998,-1.9998", "1.0", "-0.212500", "0.0", "0.0", "300", False, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), "0", "-1.0", "0.000100",  OUTPATH+SURFACECOST[0:len(SURFACECOST)-4]+'_accCost.tif', OUTPATH+SURFACECOST[0:len(SURFACECOST)-4]+'_dir.tif') 
	
	QgsMapLayerRegistry.instance().removeMapLayer(dtmlayer.id())
	QgsMapLayerRegistry.instance().removeMapLayer(costlayer.id())
	QgsMapLayerRegistry.instance().removeMapLayer(pointslayer.id())
	
	accCost = QgsRasterLayer(OUTPATH+SURFACECOST[0:len(SURFACECOST)-4]+'_accCost.tif', SURFACECOST[0:len(SURFACECOST)-4]+' accCost')
	accCost.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(accCost)
	
	print 'Computing least cost path'	
	processing.runalg("grass7:r.drain", accCost, None, None, treeslayer, False, False, False, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), "0", "-1.0", "0.000100", "0", OUTPATH+SURFACECOST[0:len(SURFACECOST)-4]+'_leastCost.tif', OUTPATH+SURFACECOST[0:len(SURFACECOST)-4]+'_leastCost.shp')
	
	QgsMapLayerRegistry.instance().removeMapLayer(treeslayer.id())

		
	if OPEN:
		print "Loading surface cost to canvas."
		leastPath = QgsVectorLayer(OUTPATH+SURFACECOST[0:len(SURFACECOST)-4]+'_leastCost.shp', SURFACECOST[0:len(SURFACECOST)-4]+' LeastCost', "ogr")
		leastPath.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(leastPath)
	else:
		QgsMapLayerRegistry.instance().removeMapLayer(accCost.id())
		
