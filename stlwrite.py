#Written by ChocolateBubbles, 2014
#I strongly believe the .whatever format should be universal...

import region

from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl
usrselectedcoords = raw_input("Please enter desired Ordnance Survey map reference to be used: ")
usrselectedcoords = usrselectedcoords.replace(" ","")
usrselectedcoords = usrselectedcoords.upper()

r = region.Region()
r.readgr (usrselectedcoords)

print "Generating STL file from map data..."
filename = str('GENERATED_' + usrselectedcoords + '.stl')
numpy2stl(r.grid, 'generatedstl/' + filename, solid=True)
print 'Done! ' + filename + ' is now ready to print!'
