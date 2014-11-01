PyCuber
====================

PyCuber is a Rubik's Cube simulator in Python 2/3.
--------------------

The cube can be revealed as expanded view in the terminal, 
so it's easy to visualise the cube, just inside the terminal.

```

import pycuber as pc

# Create a Cube object
mycube = pc.Cube()

# Do something at the cube.
mycube("R U R' U'")

print(mycube)

```
![alt tag](https://raw.github.com/adrianliaw/PyCuber/v0.1a/static/img/terminal.png)

We also provided some useful tools to deal with Rubik's Cube algorithms.

