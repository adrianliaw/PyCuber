"""
Module for solving Rubik's Cube OLL.
"""

import csv, os
from pycuber import *

with open(os.path.join(os.path.dirname(__file__), "oll_algos.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    algo_dict = {}
    for line in reader:
        algo_dict[line[1]] = Formula(line[2])
        for i in range(1, 4):
            algo_dict[line[1][-3*i:] + line[1][:-3*i]] = Formula(line[2]).insert(0, Step("U") * i)
    algo_dict["000000000000"] = Formula()

class OLLSolver(object):
    """
    OLLSolver() => An OLL solver.
    """
    def __init__(self, cube=None):
        self.cube = cube

    def feed(self, cube):
        """
        Feed Cube to the solver.
        """
        self.cube = cube

    def recognise(self):
        """
        Recognise which is Cube's OLL case.
        """
        if not isinstance(self.cube, Cube):
            raise ValueError("Use Solver.feed(cube) to feed the cube to solver.")
        result = ""
        for face in "LFRB":
            for square in self.cube.get_face(face)[0]:
                result += str(int(square == self.cube["U"]["U"]))
        if result not in algo_dict:
            raise ValueError("Invalid Cube, probably didn't solve F2L, or wrong input value.\nUse Solver.feed(cube) to reset the cube.")
        self.case = result
        return result

    def solve(self):
        """
        Solve the OLL. Returns an Formula.
        """
        if not isinstance(self.cube, Cube):
            raise ValueError("Use Solver.feed(cube) to feed the cube to solver.")
        self.recognise()
        self.cube(algo_dict[self.case])
        return algo_dict[self.case]

    def is_solved(self):
        """
        Check if Cube is solved.
        """
        return self.cube.U == [[Square(self.cube["U"].colour)] * 3] * 3

