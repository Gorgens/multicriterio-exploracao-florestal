'''
PROCESSING UPA 3
execfile('C:\\FUSION\\daad\\coding\\upa3comparing.py')
'''

print "Starting... comparison."

from osgeo import gdal
from osgeo import gdal_array
import numpy as np
from matplotlib import pyplot as plt

PATH = 'c:\\fusion\\daad\\upa3\\'
step = 1

for l in range(26):
	for c in range(26):
		print 'Step ' + str(step) + ' of ' + str(26*26) + '.'
		FILE1 = 'SC'+str(l)+'.tif'
		FILE2 = 'SC'+str(c)+'.tif'

		raster1 = gdal.Open(PATH+FILE1)
		array1 = np.array(raster1.GetRasterBand(1).ReadAsArray())
		array1 = array1.flatten()
		filter1 = array1!=-99999.
		check1 = filter1[filter1]
		# print array1[0:6], array1.shape, check1.shape

		raster2 = gdal.Open(PATH+FILE2)
		array2 = np.array(raster2.GetRasterBand(1).ReadAsArray())
		array2 = array2.flatten()
		filter2 = array2!=-99999.
		check2 = filter2[filter2]
		# print array2[0:6], array1.shape, check2.shape

		if check1.shape < check2.shape:
			array1Net = array1[filter1]
			array2Net = array2[filter1]
		else:
			array1Net = array1[filter2]
			array2Net = array2[filter2]

		# print array1Net.shape, array2Net.shape

		idx = np.random.choice(np.arange(len(array1Net)), 1000, replace=False)
		x_sample = array1Net[idx]
		y_sample = array2Net[idx]
		plt.scatter(x_sample, y_sample, alpha=0.3, c='black')
		plt.minorticks_on()
		plt.savefig(PATH+FILE1[0:len(FILE1)-4]+'_'+FILE2[0:len(FILE2)-4]+'.png')
		step = step + 1
	
print "Done"