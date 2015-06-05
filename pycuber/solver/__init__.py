"""
PyCuber solvers can be found here.

Usage: 
    >>> import pycuber as pc
    >>> from pycuber.solver import CFOPSolver
    >>> rand_alg = pc.Formula().random()
    >>> cube = pc.Cube()
    >>> cube(rand_alg)
    >>> solver = CFOPSolver(cube)
    >>> solver.solve()

"""

from .cfop import CFOPSolver
