#Written by ChocolateBubbles, 2014
#I strongly believe the .whatever format should be universal...

import region

from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl

r = region.Region()
r.readgr ("SN400200")

print "Generating STL file from map data..."

numpy2stl(r.grid,"GENERATED.stl", solid=True)

print "Done! GENERATED.stl is now ready to print!"
