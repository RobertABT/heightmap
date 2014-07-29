class Region:
    llx = 0
    lly = 0
    nrows = 3
    ncols = 3
    step = 50
    grid = [[1,2,3],[2,4,6],[3,6,9]]


    def read (self, filename):
            # set the variables from a file
            pass


thisone = Region()

print thisone.nrows
thatone = Region()
thatone.read("myfile.txt")
print ' grid [0]  + \n + grid[1] + \n grid[2] + \n '
print   thisone.grid[0]
print   thisone.grid[1]
print   thisone.grid[2]
print ('xyz')

x = thisone.grid[0] 
y = thisone.grid[1]
z = thisone.grid[2]

print x
print y
print z

# View it.
from mayavi import mlab
s = mlab.mesh(x, y, z)
mlab.show()
