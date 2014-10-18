import csv
from ..algorithm import *
from ..cube import *

with open("pycuber/cfop/oll_algos.csv", "rb") as f:
    reader = csv.reader(f, delimiter=",")
    algo_dict = {}
    for line in reader:
        algo_dict[line[1]] = Algo(line[2])
        for i in range(1, 4):
            algo_dict[line[1][-3*i:] + line[1][:-3*i]] = Algo(line[2]).insert(0, Step("U") * i)
    algo_dict["000000000000"] = Algo()

class OLLSolver(object):
    def __init__(self, cube=None):
        self.cube = cube
    def feed(self, cube):
        self.cube = cube
    def recognise(self):
        if not isinstance(self.cube, Cube):
            raise ValueError("Use Solver.feed(cube) to feed the cube to solver.")
        result = ""
        for face in "LFRB":
            for square in self.cube[face].get_row("U"):
                result += str(int(square == self.cube["U"].centre))
        if result not in algo_dict:
            raise ValueError("Invalid Cube, probably didn't solve F2L, or wrong input value.\nUse Solver.feed(cube) to reset the cube.")
        self.case = result
        return result
    def solve(self):
        if not isinstance(self.cube, Cube):
            raise ValueError("Use Solver.feed(cube) to feed the cube to solver.")
        self.recognise()
        self.cube(algo_dict[self.case])
        return algo_dict[self.case]

