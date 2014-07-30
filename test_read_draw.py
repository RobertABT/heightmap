import region
thatone = region.Region()
thatone.read("data/SN81.asc")
#print 'x'
#print   thisone.gridx
#print 'y'
#print   thisone.gridy
#print 'z'
#print   thisone.gridz

#x = thisone.gridx
#y = thisone.gridy
#z = thisone.gridz
print thatone.ncols
print thatone.nrows
print thatone.step
#print thatone.grid[0][:] #gets first coloumn of height values
#print thatone.grid[thatone.nrows-1][:] #gets last cloumn


# View it.
from mayavi import mlab
s = mlab.surf(thatone.grid[0:]/10)
print thatone.grid[0:]/10
mlab.show()
