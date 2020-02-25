'''
TO CALL ON PYTHON SHELL
execfile('C:\\FUSION\\daad\\coding\\dtm.py')
Adicionar:
-
'''
def dtm(INLAS = "upa3.laz", FILTERCELL = "8", DTMCELL = "1", LASPATH = "C:\\FUSION\\daad\\las\\", OUTPATH = "C:\\FUSION\\daad\\upa3\\", EPSG = 31982, OPEN = True):
	
	import processing
	import subprocess
	
	GNDFUN = "c:\\fusion\\groundfilter"
	DTMFUN = "c:\\fusion\\gridsurfacecreate"
	ASCFUN = "c:\\fusion\\dtm2ascii"
	
	#print "Filtering ground points."
	ch=subprocess.call([GNDFUN, OUTPATH+INLAS[0:len(INLAS)-4] + "_gnd.laz", FILTERCELL, LASPATH+INLAS], shell=True)
	if ch == 0:
		print "Ground filtered."
	else:
		print "Check the code, and try again."
		return
	
	#print "Creating DTM."
	ch=subprocess.call([DTMFUN, OUTPATH+INLAS[0:len(INLAS)-4] + "_dtm.dtm", DTMCELL, "m", "m", "1", "22", "0", "0", OUTPATH+INLAS[0:len(INLAS)-4] + "_gnd.laz"], shell=True)
	if ch == 0:
		print "DTM Computed."
	else:
		print "Check the code, and try again."
		return
	
	#print "Converting dtm to asc."
	ch=subprocess.call([ASCFUN, OUTPATH+INLAS[0:len(INLAS)-4] + "_dtm.dtm", OUTPATH+INLAS[0:len(INLAS)-4] + "_dtm.asc"], shell=True)
	if ch == 0:
		print "DTM converted to ASCII"
	else:
		print "Check the code, and try again."
		return
	
	if OPEN:
		crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)
		dtmlayer = QgsRasterLayer(OUTPATH+INLAS[0:len(INLAS)-4] + "_dtm.asc", "Digital terrain model")
		dtmlayer.setCrs(crs)
		QgsMapLayerRegistry.instance().addMapLayer(dtmlayer)
	
	return