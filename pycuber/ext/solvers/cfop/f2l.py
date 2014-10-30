"""
Module for solving Rubik's Cube F2L.
"""

from ....cube import *
from ....algorithm import *
from ....util import a_star_search

class F2LPairSolver(object):
    """
    F2LPairSolver() => Solver for solving an F2L pair.
    """
    def __init__(self, cube=None, pair=None):
        self.cube = cube
        self.pair = pair

    def feed(self, cube, pair):
        """
        Feed Cube to the solver.
        """
        self.cube = cube
        self.pair = pair

    def get_pair(self):
        """
        Get the F2L pair (corner, edge).
        """
        colours = (
            self.cube[self.pair[0]].colour, 
            self.cube[self.pair[1]].colour, 
            self.cube["D"].colour
            )
        result_corner = self.cube.children
        for c in colours[:2]:
            result_corner &= self.cube.has_colour(c)
        result_edge = result_corner & self.cube.select_type("edge")
        result_corner &= self.cube.has_colour(colours[2])
        return (list(result_corner)[0], list(result_edge)[0])
        
