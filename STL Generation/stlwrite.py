#Written by ChocolateBubbles, 2014
#I strongly believe the .whatever format should be universal...
import sys

def write():
    print "Generating STL file from map data..."

    name = 'MAPDATA.stl'

    try:
            with open('MAPDATA.stl', 'a') as f2:
#Convert map data to .stl format here, need the map data to start working.
                f2.write("solid model\n" + file.read() +"\n" + "endsolidmodel")

    except:
        print('File creation error. Closing Python.')
        sys.exit(0)

write()


print "Done!"
