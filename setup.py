from setuptools import setup
import pycuber as pc

long_desc = """
PyCuber
=======

PyCuber is a Rubik's Cube package in Python 2/3.
--------------------------------------------------

The cube can be revealed as expanded view in the terminal, so it's easy
to visualise the cube, just inside the terminal. (Not tested on Windows)

.. code-block:: python


    >>> import pycuber as pc

    >>> # Create a Cube object
    >>> mycube = pc.Cube()

    >>> # Do something at the cube.
    >>> mycube("R U R' U'")

    >>> print(mycube)

.. image:: http://i.imgur.com/OI4kbn7.png

We also provided some useful tools to deal with Rubik's Cube formulae.

.. code-block:: python


    >>> import pycuber as pc

    >>> # Create a Formula object
    >>> my_formula = pc.Formula("R U R' U' R' F R2 U' R' U' R U R' F'")

    >>> # Reversing a Formula
    >>> my_formula.reverse()
    >>> print(my_formula)

    >>> # Mirroring a Formula
    >>> myalg.mirror("LR")
    >>> print(my_formula)


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
