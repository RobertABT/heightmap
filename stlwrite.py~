#Written by ChocolateBubbles, 2014
#I strongly believe the .whatever format should be universal...

import region

from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl
print 'Format required is as HP400000 not hp40'
usrselectedcoords = raw_input("Please enter desired Ordnance Survey map reference to be used: ")

r = region.Region()
r.readgr (usrselectedcoords)

print "Generating STL file from map data..."
filename = str('GENERATED_' + usrselectedcoords + '.stl')
numpy2stl(r.grid,filename, solid=True)

print 'Done! ' + filename + '.stl is now ready to print!'
