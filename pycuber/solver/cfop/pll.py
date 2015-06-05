"""
Module for solving Rubik's Cube PLL.
"""

import csv, os
from pycuber import *

with open(os.path.join(os.path.dirname(__file__), "pll_algos.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    algo_dict = {}
    for name, rec_id, algo in reader:
        for i in range(4):
            algo_dict[rec_id[-3*i:] + rec_id[:-3*i]] = Formula(algo).insert(0, Step("U") * i)
    rec_id = "LLLFFFRRRBBB"
    algo = []
    for i in range(4):
        algo_dict[rec_id[-3*i:] + rec_id[:-3*i]] = Formula(algo).insert(0, Step("U") * i)

class PLLSolver(object):
    """
    PLLSolver() => A PLL solver.
    """
    def __init__(self, cube=None):
        self.cube = cube

    def feed(self, cube):
        """
        Feed a Cube to the solver.
        """
        self.cube = cube

    def recognise(self):
        """
        Recognise the PLL case of Cube.
        """
        result = ""
        for side in "LFRB":
            for square in self.cube.get_face(side)[0]:
                for _side in "LFRB":
                    if square.colour == self.cube[_side].colour:
                        result += _side
                        break
        return result

    def solve(self):
        """
        Solve PLL of Cube.
        """
        if not isinstance(self.cube, Cube):
            raise ValueError("Use Solver.feed(cube) to feed the cube to solver.")
        for i in range(4):
            rec_id = self.recognise()
            if rec_id in algo_dict:
                self.cube(algo_dict[rec_id])
                return Formula((Step("y") * i) or []) + algo_dict[rec_id]
            self.cube(Step("y"))
        raise ValueError("Invalid cube.")

    def is_solved(self):
        """
        Check if Cube is solved.
        """
        for side in "LUFDRB":
            sample = self.cube[side].facings[side]
            for square in sum(self.cube.get_face(side), []):
                if square != sample:
                    return False
        return True

