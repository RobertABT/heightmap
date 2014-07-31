*WIP*
The modules you need for stlwrite.py are:

pylab
numpy
stl_tools

The modules you need for modifiedstlwrite.py are (this adds ability to view in terminal):

pylab
numpy
stl_tools
mayavi

Python script for converting Ordnance Survey maps to .stl 3D printable files.

To add the .dbf files together we used this command:

    cat *.dbf | sed 's/os/\'$'\nos/g' | sed '/q/d' | sed '/^$/d' > test.whatever
