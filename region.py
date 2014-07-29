class Region:
    llx = 0
    lly = 0
    nrows = 3
    ncols = 3
    step = 50
    grid = [[1,2,3], [4,5,6], [3,8,9]]

    def read (self, filename):
            # set the variables from a file
            pass


thisone = Region()

print thisone.nrows
thatone = Region()
thatone.read("myfile.txt")
print   thisone.grid[0]
print   thisone.grid[1]
print   thisone.grid[2]
