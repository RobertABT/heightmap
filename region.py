from numpy import *
class Region:
    xllc = 0  #<--x
    yllc = 0  #<--y
    nrows = 3  #<-- b
    ncols = 3  #<-- a
    step = 50
    grid = [[1,2,3], [4,5,6], [3,8,9] ]
    def read (self, filename):
        file = open(filename,'r')
        a = file.readline().split()
        self.ncols = int(a[1])
        b = file.readline().split()
        self.nrows = int(b[1])
        x = file.readline().split()
        self.xllc = int(x[1])
        y = file.readline().split()
        self.yllc = int(y[1])
        z = file.readline().split()
        self.step = int(z[1])

        file.close
        self.grid = loadtxt(filename, skiprows=5)


thisone = Region()

thisone.read("ascii grid 5/SX99SW.asc")

print thisone.grid.size
print thisone.grid[0][0]

