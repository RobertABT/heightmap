class Region:
	llx = 0
	lly = 0
	nrows = 3
	ncols = 3
	step = 50
	gridx = [[1,2,3], [1,2,3], [1,2,3]]
	gridy = [[1,2,3], [4,5,6], [3,8,9]]
	gridz = [[1,2,3], [4,5,6], [3,8,9]]
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
s = mlab.surf([0,1], [0,1], [[1,1],[1,1],[2,2],[2,2]])
mlab.show()
