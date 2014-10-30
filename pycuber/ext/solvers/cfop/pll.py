import csv
from ....algorithm import *
from ....cube import *

with open("pycuber/ext/solvers/cfop/pll_algos.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    algo_dict = {}
    for name, rec_id, algo in reader:
        for i in range(4):
            algo_dict[rec_id[-3*i:] + rec_id[:-3*i]] = Algo(algo).insert(0, Step("U") * i)
    rec_id = "LLLFFFRRRBBB"
    algo = []
    for i in range(4):
        algo_dict[rec_id[-3*i:] + rec_id[:-3*i]] = Algo(algo).insert(0, Step("U") * i)

class PLLSolver(object):
    def __init__(self, cube=None):
        self.cube = cube
    def feed(self, cube):
        self.cube = cube
    def recognise(self):
        result = ""
        for side in "LFRB":
            for square in self.cube.get_face(side)[0]:
                for _side in "LFRB":
                    if square.colour == self.cube[_side].colour:
                        result += _side
                        break
        return result
    def solve(self):
        if not isinstance(self.cube, Cube):
            raise ValueError("Use Solver.feed(cube) to feed the cube to solver.")
        for i in range(4):
            rec_id = self.recognise()
            if rec_id in algo_dict:
                self.cube(algo_dict[rec_id])
                return Algo((Step("y") * i) or []) + algo_dict[rec_id]
            self.cube(Step("y"))
        raise ValueError("Invalid cube.")
    def is_solved(self):
        for side in "LUFDRB":
            sample = self.cube[side].facings[side]
            for square in sum(self.cube.get_face(side), []):
                if square != sample:
                    return False
        return True

