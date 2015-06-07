PyCuber
====================

### `pip install pycuber`

PyCuber is a Rubik's Cube package in Python 2/3
--------------------

The cube can be revealed as expanded view in the terminal, 
so it's easy to visualise the cube, just inside the terminal.
(Not tested on Windows)

``` python

import pycuber as pc

# Create a Cube object
mycube = pc.Cube()

# Do something at the cube.
mycube("R U R' U'")

print(mycube)

```
![alt tag](http://i.imgur.com/OI4kbn7.png)

We also provided some useful tools to deal with Rubik's Cube formulae.

``` python

import pycuber as pc

# Create a Formula object
my_formula = pc.Formula("R U R' U' R' F R2 U' R' U' R U R' F'")

# Reversing a Formula
my_formula.reverse()
print(my_formula)

# Mirroring a Formula object
my_formula.mirror("LR")
print(my_formula)

```
```
F R U' R' U R U R2 F' R U R U' R'
F' L' U L U' L' U' L2 F L' U' L' U L
```

I'll add some documentations later.

