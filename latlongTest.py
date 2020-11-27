import math
### https://stackoverflow.com/questions/7222382/get-lat-long-given-current-point-distance-and-bearing
R = 6378.1
brng = math.radians(131) # hdg * (pi/180) # Bearing is 90 degrees converted to radians
d = 6 / (0.53996) # distnace in km from nautical miles

currentLAT = 41.52909056    # in degs
currentLONG = -93.65032979  # in degs

#lat2  41.49530925 - the lat result I'm hoping for
#lon2 -93.60124208 - the long result I'm hoping for.

lat1 = math.radians(currentLAT) #Current lat point converted to radians
lon1 = math.radians(currentLONG) #Current long point converted to radians

lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(brng))

lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

lat2 = math.degrees(lat2)
lon2 = math.degrees(lon2)


print(lon2)
print(lat2)

import geopy
from geopy.distance import VincentyDistance

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
lat1 = 41.52909056
lon1 = -93.65032979
origin = geopy.Point(lat1, lon1)
d = 3 / 0.53996 # convert to nm to km
b = 131

destination = VincentyDistance(d).destination(origin, b)
lat2, lon2 = destination.latitude, destination.longitude


print("")
print(lon2)
print(lat2)
