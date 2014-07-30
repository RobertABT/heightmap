#Written by ChocolateBubbles,edited by RobertABT 2014
#I strongly believe the .whatever format should be universal...

import region

from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl

usrselectedcoords = raw_input("Please enter desired Ordnance Survey map reference to be used: ")

r = region.Region()
r.readgr (usrselectedcoords + '.asc')
r.read (usrselectedcoords + '.asc')
print "Generating STL file from map data..."
print displaying data

from mayavi import mlab
s = mlab.surf(thatone.grid[0:]/10) # divides height data by 10
mlab.show()

numpy2stl(r.grid,"GENERATED.stl", solid=True)

print "Done! GENERATED.stl is now ready to print!"
