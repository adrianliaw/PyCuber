from setuptools import setup
import pycuber as pc

long_desc = """
PyCuber
=======

PyCuber is a Rubik's Cube simulator in Python 2/3.
--------------------------------------------------

The cube can be revealed as expanded view in the terminal, so it's easy
to visualise the cube, just inside the terminal.

.. code-block:: python


    >>> import pycuber as pc

    >>> # Create a Cube object
    >>> mycube = pc.Cube()

    >>> # Do something at the cube.
    >>> mycube("R U R' U'")

    >>> print(mycube)

.. image:: https://camo.githubusercontent.com/906f83f4933fe1d0741b7d3ff43bda66fb464cdd/68747470733a2f2f7261772e6769746875622e636f6d2f61647269616e6c6961772f507943756265722f76302e31622f7374617469632f696d672f7465726d696e616c2e706e67

We also provided some useful tools to deal with Rubik's Cube algorithms.

.. code-block:: python


    >>> import pycuber as pc

    >>> # Create an Algo object
    >>> myalg = pc.Algo("R U R' U' R' F R2 U' R' U' R U R' F'")

    >>> # Reversing an Algo
    >>> myalg.reverse()
    >>> print(myalg)

    >>> # Mirroring an Algo object
    >>> myalg.mirror("LR")
    >>> print(myalg)


    F R U' R' U R U R2 F' R U R U' R'
    F' L' U L U' L' U' L2 F L' U' L' U L

I'll add some documentations later."""

setup(
    name = "pycuber", 
    version = pc.__version__, 
    description = "Rubik's Cube in Python",
    long_description = long_desc, 
    url = "http://github.com/adrianliaw/PyCuber", 
    license = "MIT", 
    author = "Adrian Liaw", 
    author_email = "adrianliaw2000@gmail.com", 
    keywords = ["Rubik's Cube", "rubik", "cube", "solver"], 
    packages = ["pycuber", "pycuber.solver", "pycuber.solver.cfop"], 
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
    package_data = {
        "pycuber.solver.cfop": ["*.csv"], 
        }, 
    )
