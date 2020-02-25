'''
Computing Effect Size Cohen'd
execfile('C:\\FUSION\\daad\\coding\\cohen.py')
'''
def cohend(raster1 = 'SC2_accCost.tif', raster2 = 'SC2_accCost.tif', INPATH = 'c:\\fusion\\daad\\upa3\\'):

	from osgeo import gdal
	from osgeo import gdal_array
	import numpy as np
	import math as m

	# FILE1 = 'c:\\fusion\\daad\\upa3\\SC2_accCost.tif'
	FILE1 = INPATH + raster1
	# FILE2 = 'c:\\fusion\\daad\\upa3\\SC1_accCost.tif'
	FILE2 = INPATH + raster2
	
	crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)

	# Para RASTER1
	raster = gdal.Open(FILE1)
	# print 'Raster type: ' + str(type(raster))
	band = raster.GetRasterBand(1)
	# print 'Band type: ' + str(type(band))

	stat = band.ComputeStatistics(0)
	band.GetMetadata()
	mean1 = stat[2]
	sd1 = stat[3]
	rasterArray = raster.ReadAsArray()
	# print 'Raster type: ' + str(type(rasterArray))
	n1 = (rasterArray!=band.GetNoDataValue()).sum()
	# print mean1, sd1, n1

	# Para RASTER2
	raster = gdal.Open(FILE2)
	# print 'Raster type: ' + str(type(raster))
	band = raster.GetRasterBand(1)
	# print 'Band type: ' + str(type(band))

	stat = band.ComputeStatistics(0)
	band.GetMetadata()
	mean2 = stat[2]
	sd2 = stat[3]
	rasterArray = raster.ReadAsArray()
	# print 'Raster type: ' + str(type(rasterArray))
	n2 = (rasterArray!=band.GetNoDataValue()).sum()
	# print mean2, sd2, n2

	s = m.sqrt(((n1-1)*(sd1)**2 + (n2-1)*(sd2)**2)/(n1 + n2 - 2))
	# print s

	d = (mean1 - mean2) / s
	return abs(round(d, 2))