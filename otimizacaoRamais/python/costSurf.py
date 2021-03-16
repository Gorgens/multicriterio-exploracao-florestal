'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\daad\\costSurf.py')
'''

def cost(LAYER1 = "upa3slopeCost.tif", LAYER2 = "upa3vegCost.tif", LAYER3 = None, LAYER4 = None, LAYER5 = None, LAYER6 = None, LAYER7 =None, LAYER8 = None, LAYER9 = None, OUTFILE = "SurfaceCost.tif", INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True):
	
	import processing
	import subprocess
	import os
	from osgeo import ogr
	
	SURFACE = OUTPATH+OUTFILE
	
	'define projecao a ser usada'
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)

	lay1 = QgsRasterLayer(INPATH+LAYER1, "surface1")
	lay1.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(lay1)
	
	lay2 = QgsRasterLayer(INPATH+LAYER2, "surface2")
	lay2.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(lay2)
	
	print "Computing the cost surface."
	if LAYER3 != None:
		lay3 = QgsRasterLayer(INPATH+LAYER3, "surface3")
		lay3.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay3)
		algebra = 'a + b + c'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3], algebra, 3, False, 7, SURFACE)
	else:
		algebra = 'a + b'
		processing.runalg("saga:rastercalculator", lay1, [lay2], algebra, 3, False, 7, SURFACE)
	
	if LAYER4 != None:
		lay4 = QgsRasterLayer(INPATH+LAYER4, "surface4")
		lay4.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay4)
		algebra = 'a + b + c + d'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3, lay4], algebra, 3, False, 7, SURFACE)
	
	if LAYER5 != None:
		lay5 = QgsRasterLayer(INPATH+LAYER5, "surface5")
		lay5.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay5)
		algebra = 'a + b + c + d + e'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3, lay4, lay5], algebra, 3, False, 7, SURFACE)
	
	if LAYER6 != None:
		lay6 = QgsRasterLayer(INPATH+LAYER6, "surface6")
		lay6.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay6)
		algebra = 'a + b + c + d + e + f'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3, lay4, lay5, lay6], algebra, 3, False, 7, SURFACE)

	if LAYER7 != None:
		lay7 = QgsRasterLayer(INPATH+LAYER7, "surface7")
		lay7.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay7)
		algebra = 'a + b + c + d + e + f + g'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3, lay4, lay5, lay6, lay7], algebra, 3, False, 7, SURFACE)

	if LAYER8 != None:
		lay8 = QgsRasterLayer(INPATH+LAYER8, "surface8")
		lay8.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay8)
		algebra = 'a + b + c + d + e + f + g + h'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3, lay4, lay5, lay6, lay7, lay8], algebra, 3, False, 7, SURFACE)

	if LAYER9 != None:
		lay9 = QgsRasterLayer(INPATH+LAYER9, "surface9")
		lay9.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(lay9)
		algebra = 'a + b + c + d + e + f + g + h + i'
		processing.runalg("saga:rastercalculator", lay1, [lay2, lay3, lay4, lay5, lay6, lay7, lay8, lay9], algebra, 3, False, 7, SURFACE)
		
	if OPEN == True:
		print "Loading surface cost to canvas."
		surfCost = QgsRasterLayer(SURFACE, OUTFILE[0:len(OUTFILE)-4])
		surfCost.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(surfCost)
	
	QgsMapLayerRegistry.instance().removeMapLayer(lay1.id())
	QgsMapLayerRegistry.instance().removeMapLayer(lay2.id())
	if LAYER3 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay3.id())
	if LAYER4 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay4.id())
	if LAYER5 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay5.id())
	if LAYER6 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay6.id())
	if LAYER7 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay7.id())
	if LAYER8 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay8.id())
	if LAYER9 != None:
		QgsMapLayerRegistry.instance().removeMapLayer(lay9.id())