"""

This module implements the Rubik's Cube formulae.
You can deal with Rubik's Cube formulae easily with Step and Formula.

Usage:
    >>> a = Formula("R U R' U'")
    >>> a
    R U R' U'

    >>> a.reverse()
    >>> a
    U R U' R'

    >>> a.mirror()
    >>> a
    U' L' U L

    >>> a *= 3
    >>> a
    U' L' U L U' L' U L U' L' U L

"""

from .step import *
from .formula import *

__all__ = ["Step", "Formula"]
