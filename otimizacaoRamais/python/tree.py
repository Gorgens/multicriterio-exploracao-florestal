'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\daad\\tree.py')
'''
def tree(CHMASC = "upa3_chm.asc", COPA = 9, TOPMASK = "crownMask.tif", EPSG = 31982, export = True, INPATH = "C:\\FUSION\\daad\\upa3\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\"):

	import processing
	import os
	from osgeo import ogr

	TOPCROWN = "crown.shp"
	EMERGENT = "emergent.shp"

	# define projecao a ser usada
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)

	
	'''
	Importa o modelo digital de altura de dossel sobre a qual todo o calculo sera realizado.
	1. importa CHM salvo no computador em formato ASC para dentro de uma variavel
	2. define a projecao da camada importada na etapa 1
	3. carrega a camada no canvas do qgis
	'''
	print "Locating and extracting emergent trees."
	chmlayer = QgsRasterLayer(INPATH+CHMASC, "CHM temp")
	chmlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(chmlayer)

	'''
	Extrair valor maximo da camada CHM e utilizar como referencia para o parametro HEIGHT
	'''
	# print "Computing reference height."
	extent = chmlayer.extent()
	provider = chmlayer.dataProvider()
	stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
	#HEIGHT = str(round(stats.maximumValue - 10))
	HEIGHT = str(round(stats.mean + 2. * stats.stdDev))

	'''
	A partir do CHM importado anteriormente, filtra os pixels acima de uma determianda altura criando
	uma raster chamado de modelo digital de copas emergentes (MDCE).
	1. cria a string que define o filtro a ser aplicado no rastercalculator
	2. cria o MDCE aplicando o filtro via rastercalculator do SAGA sobre o CHM
	3. importa o MDCE para uma variavel
	4. define a projecao da camada MDCE
	5. carrega a camada no canvas qgis
	CALC1 = "ifelse(a<"+HEIGHT+",-99999,a)"
	processing.runalg("saga:rastercalculator", chmlayer, None, CALC1, 3, False, 7, OUTPATH+TOPCROWN)
	toplayer = QgsRasterLayer(OUTPATH+TOPCROWN, "top crowns")
	toplayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(toplayer)
	'''
	'''
	A partir do CHM importado anteriormente, cria uma mascada para os pixels acima de uma
	determianda altura criando.
	1. cria a string que define o filtro a ser aplicado no rastercalculator
	2. cria a mascara aplicando o filtro via rastercalculator do SAGA sobre o CHM
	3. importa a mascara para uma variavel
	4. define a projecao da mascara
	5. extrai a extensao da mascara
	6. carrega a mascara no canvas qgis
	'''
	# print "Creating mask of emergent crown"
	CALC2 = "ifelse(a<"+HEIGHT+",-99999,1)"
	processing.runalg("saga:rastercalculator", chmlayer, None, CALC2, 3, False, 7, OUTPATH+TOPMASK)
	msklayer = QgsRasterLayer(OUTPATH+TOPMASK, "mascara")
	msklayer.setCrs(crs)
	extent = msklayer.extent()
	xmin = extent.xMinimum()
	xmax = extent.xMaximum()
	ymin = extent.yMinimum()
	ymax = extent.yMaximum()
	QgsMapLayerRegistry.instance().addMapLayer(msklayer)

	
	'''
	A partir mascara de copas emergentes cria uma camada vetorial de poligonos.
	1. chama o comando grass para vetorizar uma mascara
	2. importa a camada de poligonos para uma variavel
	3. define a projecao da camada de poligonos
	4. carrega a camada no canvas qgis
	'''
	# print "Creating crown layer 1 of 3 steps"
	TEMP1 = TOPCROWN[0:len(TOPCROWN)-4] + "Temp1.shp"
	processing.runalg("grass7:r.to.vect", msklayer, 2, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, OUTPATH+TEMP1)
	vlayer = QgsVectorLayer(OUTPATH+TEMP1, "crownTemp1", "ogr")
	vlayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(vlayer)

	
	'''
	A partir camada vetorial de poligonos, cria uma nova camada contendo o atributo de area. Esta camada
	indica uma aproximacao das copas das arvores emergentes.
	1. cria o nome da nova camada acrescido do indice 2
	2. roda o comando fieldcalculador para obter area de cada poligono
	3. importa a camada de poligonos para uma variavel
	4. define a projecao da camada de poligonos
	5. extrai a extensao da mascara
	6. carrega a camada no canvas qgis
	'''
	# print "Creating crown layer 2 of 3 steps"
	TEMP2 = TOPCROWN[0:len(TOPCROWN)-4] + "Temp2.shp"
	processing.runalg('qgis:fieldcalculator', vlayer, 'area', 0, 10, 2, True, '$area', OUTPATH+TEMP2)
	vlayer2 = QgsVectorLayer(OUTPATH+TEMP2, "crownTemp2", "ogr")
	vlayer2.setCrs(crs)
	extent = vlayer2.extent()
	xmin = extent.xMinimum()
	xmax = extent.xMaximum()
	ymin = extent.yMinimum()
	ymax = extent.yMaximum()
	QgsMapLayerRegistry.instance().addMapLayer(vlayer2)

	'''
	A partir do vetor de copas, com as informacoes de area, filtra apenas as copas maiores que area
	especificada pelo usuario.
	1. chama o comando grass para filtrar poligonos com area acima do limite espeficicado
	2. importa a camada de poligonos das copas emergente maiores que limite
	3. define a projecao da camada de poligonos
	4. carrega a camada no canvas qgis
	'''
	# print "Creating crown layer 3 of 3 steps"
	CROWN = "area>"+str(COPA)
	processing.runalg("grass7:v.extract", vlayer2, CROWN, False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), -1, 0, 0, OUTPATH+TOPCROWN)
	crownLayer = QgsVectorLayer(OUTPATH+TOPCROWN, "crown", "ogr")
	crownLayer.setCrs(crs)
	QgsMapLayerRegistry.instance().addMapLayer(crownLayer)
			
	'''
	1. calcula o centroid de cada poligono extraido como arvore
	2. salva num shape de pontos chamado centroid.shp
	3. esctrai as coordenadas x e y de cada ponto
	4. exporta as coordenadas num csv
	'''
	if export:
		ogr.UseExceptions()
		os.chdir(OUTPATH)
		
		print "Extracting crown centroids 1 of 3 steps"
		ds = ogr.Open(OUTPATH+TOPCROWN)
		ly = ds.ExecuteSQL('SELECT ST_Centroid(geometry), * FROM crown', dialect='sqlite')
		drv = ogr.GetDriverByName('Esri shapefile')
		ds2 = drv.CreateDataSource('emergentesTemp1.shp')
		ds2.CopyLayer(ly, '')
		ly = crownLayer = ds2 = None # save, close
		pointslayer = QgsVectorLayer(OUTPATH+'emergentesTemp1.shp', "temp1", "ogr")
		pointslayer.setCrs(crs)
		
		print "Extracting crown centroids 2 of 2 steps"
		processing.runalg('qgis:fieldcalculator', pointslayer, 'xcoord', 0, 10, 2, True, '$x', OUTPATH+'emergentesTemp2.shp')
		pointslayer = QgsVectorLayer(OUTPATH+'emergentesTemp2.shp', "temp2", "ogr")
		pointslayer.setCrs(crs)
		
		print "Extracting crown centroids 3 of 3 steps"
		processing.runalg('qgis:fieldcalculator', pointslayer, 'ycoord', 0, 10, 2, True, '$y', OUTPATH+'emergentes.shp')
		pointslayer = QgsVectorLayer(OUTPATH+'emergentes.shp', "emergentes", "ogr")
		pointslayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(pointslayer)
		
		print "Exporting centroids."
		QgsVectorFileWriter.writeAsVectorFormat(pointslayer, OUTPATH+"xy.csv", "utf-8", None, "CSV", layerOptions ='GEOMETRY=AS_WKT')
	
		# print "Cleaning temporary files."
		driver = ogr.GetDriverByName("ESRI Shapefile")
		if os.path.exists(OUTPATH+'emergentesTemp1.shp'):
			driver.DeleteDataSource(OUTPATH+'emergentesTemp1.shp')
		if os.path.exists(OUTPATH+'emergentesTemp2.shp'):
			driver.DeleteDataSource(OUTPATH+'emergentesTemp2.shp')
		
		# print "Extracting emergent trees height."
		processing.runalg("grass7:v.what.rast.points", pointslayer, chmlayer, "value", "area > 0", False, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), -1, 0.0001, 0, OUTPATH+'emergentes2.shp')
		pointslayer2 = QgsVectorLayer(OUTPATH+'emergentes2.shp', "emergentes", "ogr")
		pointslayer2.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(pointslayer2)
	
	# print "Cleaning temporary files."
	QgsMapLayerRegistry.instance().removeMapLayer(chmlayer.id())
	QgsMapLayerRegistry.instance().removeMapLayer(msklayer.id())
	QgsMapLayerRegistry.instance().removeMapLayer(vlayer.id())
	QgsMapLayerRegistry.instance().removeMapLayer(vlayer2.id())
	QgsMapLayerRegistry.instance().removeMapLayer(pointslayer.id())
	driver = ogr.GetDriverByName("ESRI Shapefile")
	if os.path.exists(OUTPATH+TEMP2):
		driver.DeleteDataSource(OUTPATH+TEMP2)
	if os.path.exists(OUTPATH+TEMP1):
		driver.DeleteDataSource(OUTPATH+TEMP1)
	if os.path.exists(OUTPATH+'emergentes.shp'):
		driver.DeleteDataSource(OUTPATH+'emergentes.shp')		
	
	return