from pycuber import *
from .. import oll
import random

class OLLTester(object):
    def __init__(self):
        self.history = []
    @staticmethod
    def random_cube():
        result = Cube()
        algos = list(oll.algo_dict.values())
        for i in range(10):
            result(Algo(random.choice(algos)))
        return result
    def test(self):
        solver = oll.OLLSolver()
        record = ()
        cube = self.random_cube()
        record += (cube.copy(),)
        solver.feed(cube)
        record += (solver.solve(),)
        record += (solver.is_solved(),)
        try:
            assert record[-1]
            self.history.append(record)
        except AssertionError:
            print("TEST DIDN'T PASS : ")
            print(record[0])
            print(record[1])
            print(cube)
            raise AssertionError()
        return True
    def suite(self, n=100):
        for i in range(n):
            self.test()
        print("TEST PASSED")
        return True

