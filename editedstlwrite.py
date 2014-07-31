#Written by ChocolateBubbles,edited by RobertABT 2014
#I strongly believe the .whatever format should be universal...

import region
from mayavi import mlab
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl
print 'Format required is as HP400000 not hp40'
usrselectedcoords = raw_input("Please enter desired Ordnance Survey map reference to be used: ")

r = region.Region()
r.readgr (usrselectedcoords)
print "Generating STL file from map data..."
print "Close viewer to generate STL"
#print displaying data


s = mlab.surf(r.grid[0:]/10) # divides height data by 10
mlab.show()
filename = str('GENERATED_' + usrselectedcoords +'.stl')
numpy2stl(r.grid/10,(filename), solid=True)

print ('Done!' + filename + ' is now ready to print!')
