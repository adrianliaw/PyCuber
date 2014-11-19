from pycuber import *
from .. import cross
import sys

class CrossTester(object):
    """
    Tester for CrossSolver.
    """
    def __init__(self):
        self.history = []

    def test(self):
        scramble = Algo().random()
        cube = Cube()(scramble)
        solver = cross.CrossSolver(cube)
        record = (cube.copy(), )
        result = solver.solve()
        record += (result, solver.is_solved())
        try:
            assert record[-1]
        except AssertionError:
            print("TEST DIDN'T PASS : ")
            print(record[0])
            print(record[1])
            print(cube)
            raise AssertionError()
        self.history.append(record)
        return True

    def suite(self, n=10):
        for i in range(n):
            self.test()
            print("TEST#{0} PASSED".format(n+1))
        print("TEST PASSED")
        return True
