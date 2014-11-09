"""
Module for solving Rubik's Cube F2L.
"""

from pycuber import *
from pycuber.helpers import fill_unknowns
from .util import shortest_path_search, path_actions

class F2LPairSolver(object):
    """
    F2LPairSolver() => Solver for solving an F2L pair.
    """
    def __init__(self, cube=None, pair=None):
        self.cube = cube
        if pair and pair not in ["FR", "RB", "BL", "LF"]:
            pair = ["FR", "RB", "BL", "LF"][["RF", "BR", "LB", "FL"].index(pair)]
        self.pair = pair

    def feed(self, cube, pair):
        """
        Feed Cube to the solver.
        """
        self.cube = cube
        if pair not in ["FR", "RB", "BL", "LF"]:
            pair = ["FR", "RB", "BL", "LF"][["RF", "BR", "LB", "FL"].index(pair)]
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
        return sum(path_actions(shortest_path_search(start, 
                       self.combining_successors, 
                       self.combining_goal)), Algo())

    def combining_setup(self):
        """
        Setup for some special F2L cases.
        """
        (slot_type, (corner_slot, edge_slot), (corner, edge)) = self.get_slot()
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
            if corner_slot != self.pair: corner_slot, edge_slot = edge_slot, corner_slot
            result = Algo(Step("y") * cycle.index(edge_slot) or [])
            result += Algo("R U R'")
            result += Algo(Step("y'") * cycle.index(edge_slot) or [])
            result += Algo(Step("y") * cycle.index(corner_slot) or [])
            if result[-1].face == "y" and result[-2].face == "y":
                result[-2] += result[-1]
                del result[-1]
            return (cycle[-(cycle.index(corner_slot) - cycle.index(self.pair))], result)
        else:
            return (cycle[-cycle.index(self.pair)], Algo())

    def combine(self):
        """
        Combine the pair.
        """
        self.pair, setup = self.combining_setup()
        self.cube(setup)
        actual = self.combining_search()
        self.cube(actual)
        return setup + actual

    def solve(self):
        """
        Solve the pair.
        """
        cycle = ["FR", "RB", "BL", "LF"]
        combine = self.combine()
        put = Algo(Step("y") * cycle.index(self.pair) or [])
        self.cube(put)
        self.pair = "FR"
        estimated = self.estimated_position()
        for U_act in [Algo(), Algo("U"), Algo("U2"), Algo("U'")]:
            self.cube(U_act)
            for put_act in [Algo("R U R'"), Algo("R U' R'"), Algo("R U2 R'"), 
                            Algo("F' U F"), Algo("F' U' F"), Algo("F' U2 F")]:
                self.cube(put_act)
                if self.get_pair() == estimated:
                    return combine + put + U_act + put_act
                self.cube(put_act.reverse())
            self.cube(U_act.reverse())

    def is_solved(self):
        """
        Check if the cube is solved.
        """


class F2LSolver(object):
    """
    F2LSolver(cube) => An F2L solver.
    """
    def __init__(self, cube):
        self.cube = cube

    def feed(self, cube):
        """
        Feed a cube to the solver.
        """
        self.cube = cube

    def solve(self):
        """
        Solve the entier F2L. (Generator)
        """
        times = 0
        for i in range(4):
            for slot in ["FR", "RB", "BL", "LF"]:
                if times == 4: raise StopIteration()
                solver = F2LPairSolver(self.cube, slot)
                if not solver.is_solved():
                    yield tuple([self.cube[slot[i]].colour for i in range(2)]), solver.solve()
                    times += 1

    def is_solved(self):
        """
        Check if Cube's F2L is solved.
        """
        if self.cube.D == [[Square(self.cube["D"].colour)] * 3] * 3:
            for face in "LFRB":
                if self.cube.get_face(face)[1:] != [[Square(self.cube[face].colour)] * 3] * 2:
                    return False
            return True
        return False

