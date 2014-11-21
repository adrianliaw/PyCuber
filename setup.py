from setuptools import setup

long_desc = """
PyCuber
=======

PyCuber is a Rubik’s Cube simulator in Python 2/3.
--------------------------------------------------

The cube can be revealed as expanded view in the terminal, so it’s easy
to visualise the cube, just inside the terminal.

.. code:: python


    import pycuber as pc

    # Create a Cube object
    mycube = pc.Cube()

    # Do something at the cube.
    mycube("R U R' U'")

    print(mycube)

.. figure:: https://raw.github.com/adrianliaw/PyCuber/v0.1b/static/img/terminal.png
   :alt: alt tag

   alt tag
We also provided some useful tools to deal with Rubik’s Cube algorithms.

.. code:: python


    import pycuber as pc

    # Create an Algo object
    myalg = pc.Algo("R U R' U' R' F R2 U' R' U' R U R' F'")

    # Reversing an Algo
    myalg.reverse()
    print(myalg)

    # Mirroring an Algo object
    myalg.mirror("LR")
    print(myalg)

::

    F R U' R' U R U R2 F' R U R U' R'
    F' L' U L U' L' U' L2 F L' U' L' U L

I’ll add some documentations later.
"""

setup(
    name = "pycuber", 
    version = "0.1b3", 
    description = "Rubik's Cube in Python",
    long_description = long_desc, 
    url = "http://github.com/adrianliaw/PyCuber", 
    license = "MIT", 
    author = "Adrian Liaw", 
    author_email = "adrianliaw2000@gmail.com", 
    packages = ["pycuber"], 
    package_dir = {"pycuber":"pycuber"}, 
    classifiers = [
        "Development Status :: 4 - Beta", 
        "Environment :: Console", 
        "Intended Audience :: Science/Research", 
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python", 
        "Programming Language :: Python :: 2", 
        "Programming Language :: Python :: 3", 
        "Topic :: Scientific/Engineering :: Mathematics", 
        ], 
    )
