from numpy import *
class Region:
    xllc = 0  #<--x
    yllc = 0  #<--y
    nrows = 3  #<-- b
    ncols = 3  #<-- a
    step = 50
    grid = [[1,2,3], [4,5,6], [3,8,9] ]

    #Reading files, retrieving integers and creating an array.
    def read (self, filename):
        try:
            file = open(filename,'r')
        except:
            print("no such file")
            return False
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
        return True

    #Retrieving files according to grid references.
    def readgr(self, gridsqr):
        thepath = "data/"
        thepath = thepath + gridsqr[0:3] + gridsqr[5] + ".asc"
        self.read(thepath)

#Defining global variable.
region = Region()

#Users input
region.readgr("SN942935")

if __name__ == "__main__":
    #Printing values.
    print("------------")
    print(region.xllc)
    print("xllcorner")

    print("------------")

    print(region.yllc)
    print("yllcorner")

    print("------------")

    print(region.ncols)
    print("ncolumns")

    print("------------")

    print(region.nrows)
    print("nrows")

    print("------------")

