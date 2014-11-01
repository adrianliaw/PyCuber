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

```

import pycuber as pc

# Create an Algo object
myalg = pc.Algo("R U R' U' R' F R2 U' R' U' R U R' F'")

# Reversing an Algo
myalg.reverse()
print(myalg)

# Mirroring an Algo object
myalg.mirror("LR")
print(myalg)

```
```
F R U' R' U R U R2 F' R U R U' R'
F' L' U L U' L' U' L2 F L' U' L' U L
```

I'll add some documentations later.

