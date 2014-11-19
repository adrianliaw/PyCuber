from pycuber import *
from .. import f2l
import random
from collections import OrderedDict

class F2LTester(object):
    """
    Tester for F2LSolver.
    """
    def __init__(self):
        self.history = []
    @staticmethod
    def random_cube():
        result = Cube()
        algos = [
            "R U R'", "R U2 R'", "R U' R'", "R' U R", "R' U2 R", "R' U' R", 
            "L U L'", "L U2 L'", "L U' L'", "L' U L", "L' U2 L", "L' U' L", 
            "F U F'", "F U2 F'", "F U' F'", "F' U F", "F' U2 F", "F' U' F", 
            "B U B'", "B U2 B'", "B U' B'", "B' U B", "B' U2 B", "B' U' B", 
            ]
        for i in range(10):
            result(random.choice(algos))
        return result
    def test(self):
        cube = self.random_cube()
        record = (cube.copy(), OrderedDict())
        solver = f2l.F2LSolver(cube)
        for slot, res in solver.solve():
            record[1][slot] = res
        record += (solver.is_solved(), )
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
        print("TEST PASSED")
        return True


