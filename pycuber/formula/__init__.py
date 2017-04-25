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

from .move import GenericCubicMove, Move
from .formula import BaseFormula


class GenericCubicFormula(BaseFormula):
    _move = GenericCubicMove


class Formula(GenericCubicFormula):
    _move = Move


__all__ = ["GenericCubicMove", "Move", "GenericCubicFormula", "Formula"]
