# execfile('C:\\FUSION\\daad\\coding\\harzard.py')

ASCMDT = "upa3_dtm.asc"
resolution = 1
INPATH = "C:\\FUSION\\daad\\upa3\\"
OUTPATH = "C:\\FUSION\\daad\\upa3\\"
EPSG = 31982

print "Loading digital terrain model"
crs = QgsCoordinateReferenceSystem(EPSG, QgsCoordinateReferenceSystem.PostgisCrsId)
dtmlayer = QgsRasterLayer(INPATH+ASCMDT, "DTM")
dtmlayer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(dtmlayer)	
extent = dtmlayer.extent()
xmin = extent.xMinimum()
xmax = extent.xMaximum()
ymin = extent.yMinimum()
ymax = extent.yMaximum()

print "Loading flow accumulation map."
accumulation = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_accum.tif"
acclayer = QgsRasterLayer(accumulation, "Accumulation")
acclayer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(acclayer)

print "Loading slope map."
slope = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_slope.tif"
slplayer = QgsRasterLayer(slope, "Slope")
slplayer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(slplayer)
	
print "Processing the harzard flood model"
print "Step 1"
n = 0.016 * (resolution ** 0.46)
CALC = "log((pow(((a+1)*"+str(resolution)+") , "+str(n)+")) / (tan(b+0.001)))"
rmti = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_rmti.tif"
processing.runalg("saga:rastercalculator", acclayer, [slplayer], CALC, 3, False, 7, rmti)
rmtilayer = QgsRasterLayer(rmti, "RMTI")
rmtilayer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(rmtilayer)

print "Step 2"
rflood = OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_rflood.tif"
mti_th = 10.89 * n + 2.282
CALC = "ifelse(a>"+str(mti_th)+",1,0)"
processing.runalg("saga:rastercalculator", rmtilayer, None, CALC, 3, False, 7, rflood)
rfloodlayer = QgsRasterLayer(rflood, "RFLOOD")
rfloodlayer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(rfloodlayer)

print "Step 3"
title = "Flood"
rclump =  OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_clump.tif"
processing.runalg("grass7:r.clump", rmtilayer, title, "%f,%f,%f,%f"% (xmin, xmax, ymin, ymax), 0, rclump)  
rclumplayer = QgsRasterLayer(rclump, "RCLUMP")
rclumplayer.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(rclumplayer)

print "Step 4"
harzardFlood =  OUTPATH+ASCMDT[0:len(ASCMDT)-4] + "_harzFloof.tif"
extent = rclumplayer.extent()
provider = rclumplayer.dataProvider()
stats = provider.bandStatistics(1, QgsRasterBandStats.All, extent, 0)
MAX = str(round(stats.maximumValue))
if stats.minimumValue < 0:
	MIN = str(0)
else:
	MIN = str(round(stats.minimumValue))
processing.runalg("saga:rastercalculator", rclumplayer, None, '"(a-'+MIN+')/('+MAX+'-'+MIN+')*10"', 3, False, 7, harzardFlood)
harflood = QgsRasterLayer(harzardFlood, "Harzard flood")
harflood.setCrs(crs)
QgsMapLayerRegistry.instance().addMapLayer(harflood)