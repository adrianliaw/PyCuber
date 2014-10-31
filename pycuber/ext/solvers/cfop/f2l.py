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
        result_corner = self.cube.children.copy()
        for c in colours[:2]:
            result_corner &= self.cube.has_colour(c)
        result_edge = result_corner & self.cube.select_type("edge")
        result_corner &= self.cube.has_colour(colours[2])
        return (list(result_corner)[0], list(result_edge)[0])

    def estimated_position(self):
        """
        Get the estimated cuboid of solved pair.
        """
        corner = {"D":self.cube["D"]["D"]}
        edge = {}
        for cuboid in (corner, edge):
            for face in self.pair:
                cuboid.update({face:self.cube[face][face]})
        return (Corner(**corner), Edge(**edge))

    def get_slot(self):
        """
        Get the slot position of this pair.
        """
        corner, edge = self.get_pair()
        corner_slot, edge_slot = corner.location.replace("D", "", 1), edge.location
        if "U" in corner_slot and "U" in edge_slot:
            return ("SLOTFREE", (None, None), (corner, edge))
        if "U" in corner_slot:
            return ("CSLOTFREE", (None, edge_slot), (corner, edge))
        if "U" in edge_slot:
            return ("ESLOTFREE", (corner_slot, None), (corner, edge))
        if corner_slot not in [edge_slot, edge_slot[::-1]]:
            return ("DIFFSLOT", (corner_slot, edge_slot), (corner, edge))
        if (corner, edge) == self.estimated_position():
            return ("SOLVED", (corner_slot, edge_slot), (corner, edge))
        return ("WRONGSLOT", (corner_slot, edge_slot), (corner, edge))

