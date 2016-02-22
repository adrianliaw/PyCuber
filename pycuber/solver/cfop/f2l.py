"""
Module for solving Rubik's Cube F2L.
"""

from pycuber import *
from pycuber.helpers import fill_unknowns
from .util import a_star_search, path_actions

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
        Get the estimated cubie of solved pair.
        """
        corner = {"D":self.cube["D"]["D"]}
        edge = {}
        for cubie in (corner, edge):
            for face in self.pair:
                cubie.update({face:self.cube[face][face]})
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
        Check if two Cubies are combined on the U face.
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
    def _rotate(pair, step):
        """
        Simulate the cube rotation by updating the pair.
        """
        step = Step(step)
        movement = {
            "U": "RFLB", 
            "D": "LFRB", 
            "R": "FUBD", 
            "L": "FDBU", 
            "F": "URDL", 
            "B": "ULDR", 
            }[step.face]
        movement = {
            movement[i]: movement[(i + step.is_clockwise + (-1 * step.is_counter_clockwise) + (2 * step.is_180)) % 4]
            for i in range(4)
            }
        for cubie in pair:
            if step.face not in cubie:
                if cubie.type == "edge":
                    result_edge = cubie.copy()
                else:
                    result_corner = cubie.copy()
            else:
                result = {}
                for face, square in cubie:
                    if face not in movement:
                        result[face] = square
                    else:
                        result[movement[face]] = square
                if len(result) == 2:
                    result_edge = Edge(**result)
                else:
                    result_corner = Corner(**result)
        return (result_corner, result_edge)

    @staticmethod
    def combining_successors(state, last_action=()):
        """
        Successors function for finding path of combining F2L pair.
        """
        ((corner, edge), (L, U, F, D, R, B)) = state
        U_turns = [Formula("U"), Formula("U'"), Formula("U2")] if len(last_action) != 1 else []
        R_turns = [Formula("R U R'"), Formula("R U' R'"), Formula("R U2 R'")] if "R" not in last_action else []
        F_turns = [Formula("F' U F"), Formula("F' U' F"), Formula("F' U2 F")] if "F" not in last_action else []
        for act in (U_turns + R_turns + F_turns):
            new = (corner, edge)
            for q in act:
                new = F2LPairSolver._rotate(new, q)
            yield act, (new, (L, U, F, D, R, B))

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
        return sum(path_actions(a_star_search(start, 
                       self.combining_successors, 
                       lambda x: len(x), 
                       self.combining_goal)), Formula())

    def combining_setup(self):
        """
        Setup for some special F2L cases.
        """
        (slot_type, (corner_slot, edge_slot), (corner, edge)) = self.get_slot()
        cycle = ["FR", "RB", "BL", "LF"]
        if slot_type == "SLOTFREE":
            return ("FR", Formula(Step("y") * cycle.index(self.pair) or []))
        elif slot_type == "CSLOTFREE":
            return (cycle[-(cycle.index(edge_slot) - cycle.index(self.pair))], 
                    Formula(Step("y") * cycle.index(edge_slot) or [])) 
        elif slot_type in ("ESLOTFREE", "WRONGSLOT"):
            return (cycle[-(cycle.index(corner_slot) - cycle.index(self.pair))], 
                    Formula(Step("y") * cycle.index(corner_slot) or [])) 
        elif slot_type == "DIFFSLOT":
            if corner_slot != self.pair: corner_slot, edge_slot = edge_slot, corner_slot
            result = Formula(Step("y") * cycle.index(edge_slot) or [])
            result += Formula("R U R'")
            result += Formula(Step("y'") * cycle.index(edge_slot) or [])
            result += Formula(Step("y") * cycle.index(corner_slot) or [])
            if result[-1].face == "y" and result[-2].face == "y":
                result[-2] += result[-1]
                del result[-1]
            return (cycle[-(cycle.index(corner_slot) - cycle.index(self.pair))], result)
        else:
            return (cycle[-cycle.index(self.pair)], Formula())

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
        put = Formula(Step("y") * cycle.index(self.pair) or [])
        self.cube(put)
        self.pair = "FR"
        estimated = self.estimated_position()
        for U_act in [Formula(), Formula("U"), Formula("U2"), Formula("U'")]:
            self.cube(U_act)
            for put_act in [Formula("R U R'"), Formula("R U' R'"), Formula("R U2 R'"), 
                            Formula("F' U F"), Formula("F' U' F"), Formula("F' U2 F")]:
                self.cube(put_act)
                if self.get_pair() == estimated:
                    return combine + put + U_act + put_act
                self.cube(put_act.reverse())
            self.cube(U_act.reverse())

    def is_solved(self):
        """
        Check if the cube is solved.
        """
        return self.get_pair() == self.estimated_position()


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
        Solve the entire F2L. (Generator)
        """
        for i in range(4):
            for slot in ["FR", "RB", "BL", "LF"]:
                solver = F2LPairSolver(self.cube, slot)
                if not solver.is_solved():
                    yield tuple([self.cube[slot[i]].colour for i in range(2)]), solver.solve()
                    break

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

