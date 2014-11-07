"""
Module for solving Rubik's Cube F2L.
"""

from pycuber import *
from pycuber.helpers import fill_unknowns
from util import shortest_path_search, path_actions

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
        if "U" not in corner_slot and corner_slot not in ["FR", "RB", "BL", "LF"]:
            corner_slot = ["FR", "RB", "BL", "LF"][["RF", "BR", "LB", "FL"].index(corner_slot)]
        if "U" not in edge_slot and edge_slot not in ["FR", "RB", "BL", "LF"]:
            edge_slot = ["FR", "RB", "BL", "LF"][["RF", "BR", "LB", "FL"].index(edge_slot)]
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

    @staticmethod
    def combining_goal(state):
        """
        Check if two Cuboids are combined on the U face.
        """
        ((corner, edge), (L, U, F, D, R, B)) = state
        if "U" not in corner or "U" not in edge: return False
        if set(edge).issubset(set(corner)): return True
        elif set(edge.facings.keys()).issubset(set(corner.facings.keys())): return False
        opposite = {"L":"R", "R":"L", "F":"B", "B":"F"}
        edge_facings = list(edge)
        for i, (face, square) in enumerate(edge_facings):
            if face == "U":
                if square != corner[opposite[edge_facings[(i+1)%2][0]]]:
                    return False
            else:
                if square != corner["U"]:
                    return False
        return True
    
    @staticmethod
    def combining_successors(state, last_action=()):
        """
        Successors function for finding path of combining F2L pair.
        """
        ((corner, edge), (L, U, F, D, R, B)) = state
        U_turns = [Algo("U"), Algo("U'"), Algo("U2")] if len(last_action) != 1 else []
        R_turns = [Algo("R U R'"), Algo("R U' R'"), Algo("R U2 R'")] if "R" not in last_action else []
        F_turns = [Algo("F' U F"), Algo("F' U' F"), Algo("F' U2 F")] if "F" not in last_action else []
        cube = Cube(fill_unknowns(set([corner, edge, L, U, F, D, R, B])))
        for act in (U_turns + R_turns + F_turns):
            cube(act)
            new_corner = (cube.select_type("corner") - cube.has_colour("unknown")).pop().copy()
            new_edge = (cube.select_type("edge") - cube.has_colour("unknown")).pop().copy()
            cube(act.reverse())
            yield act.reverse(), ((new_corner, new_edge), (L, U, F, D, R, B))

    def combining_search(self):
        """
        Searching the path for combining the pair.
        """
        start = (
            self.get_pair(), 
            (
                self.cube["L"], 
                self.cube["U"], 
                self.cube["F"], 
                self.cube["D"], 
                self.cube["R"], 
                self.cube["B"], 
                ), 
            )
        return sum(
            path_actions(
                shortest_path_search(start, 
                                     self.combining_successors, 
                                     self.combining_goal),
                ), 
            Algo(), 
            )

    def combining_setup(self):
        """
        Setup for some special F2L cases.
        """
        (slot_type, (corner_slot, edge_slot), (corner, edge)) = self.get_slot()
        print(slot_type)
        cycle = ["FR", "RB", "BL", "LF"]
        if slot_type == "SLOTFREE":
            return ("FR", Algo(Step("y") * cycle.index(self.pair) or []))
        elif slot_type == "CSLOTFREE":
            return (cycle[-(cycle.index(edge_slot) - cycle.index(self.pair))], 
                    Algo(Step("y") * cycle.index(edge_slot) or [])) 
        elif slot_type in ("ESLOTFREE", "WRONGSLOT"):
            return (cycle[-(cycle.index(corner_slot) - cycle.index(self.pair))], 
                    Algo(Step("y") * cycle.index(corner_slot) or [])) 
        elif slot_type == "DIFFSLOT":
            for s in (corner_slot, edge_slot):
                if self.pair in [s, s[::-1]]:
                    return ("FR", Algo(Step("y") * cycle.index(s) or []))
            return (cycle[-(cycle.index(edge_slot) - cycle.index(self.pair))], 
                    Algo(Step("y") * cycle.index(edge_slot) or []))

