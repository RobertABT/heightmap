class Region:
    xllc = 0
    yllc = 0
    nrows = 3
    ncols = 3
    step = 50
    grid = [[1,2,3], [4,5,6], [3,8,9]]

    def read (self, filename):
        file = open(filename,'r')
        x = file.readline().split()
        self.ncols = int(x[1])
            # set the variables from a file
            


thisone = Region()

thisone.read("ascii grid 5/SX99SW.asc")

print(thisone.ncols)
