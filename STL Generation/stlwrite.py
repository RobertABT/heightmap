#Written by ChocolateBubbles, 2014
#I strongly believe the .whatever format should be universal...
import sys

def write():
    print "Generating STL file from map data..."

    name = 'MAPDATA.stl'

    try:
            with open('MAPDATA.stl', 'a') as f2:               
                f2.write("solid model" + '\n' + ("facet normal 0.0 0.0 -1.0" + '\n' "outer loop" + '\n' + "vertex 100.0 0.0 0.0" + '\n' + "vertex 0.0 0.0 0.0" + '\n' + "vertex 0.0 0.0 100.0" + '\n' + "endloop" + '\n' + "endfacet") + '\n' + "endsolidmodel")

    except:
        print('File creation error. Closing Python.')
        sys.exit(0)

write()


print "Done!"
