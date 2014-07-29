*WIP*

Python script for converting Ordnance Survey maps to .stl 3D printable files.

To add the .dbf files together we used this command:

    cat *.dbf | sed 's/os/\'$'\nos/g' | sed '/q/d' | sed '/^$/d' > test.whatever
