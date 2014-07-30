class Region:
	llx = 0
	lly = 0
	nrows = 3
	ncols = 3
	step = 50
	gridx = [1,2,3]
	gridy = [2,3,4]
	gridz = [3,4,5]
	def read (self, filename):
		# set the variables from a file
		pass


thisone = Region()

print thisone.nrows
thatone = Region()
thatone.read("myfile.txt")

print 'x'
print   thisone.gridx
print 'y'
print   thisone.gridy
print 'z'
print   thisone.gridz

x = thisone.gridx
y = thisone.gridy
z = thisone.gridz

# View it.
from mayavi import mlab
s = mlab.surf(thisone.gridx , thisone.gridy , thisone.gridz)
mlab.show()
