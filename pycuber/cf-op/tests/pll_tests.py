from ..pll import PLLSolver, Cube, Algo
import random

class PLLTester(object):
    def __init__(self):
        self.history = []
    @staticmethod
    def random_cube():
        result = Cube()
        choices = ["R U' R U R U R U' R' U' R2",
                "R2 U R U R' U' R' U' R' U R'", 
                "R B' R F2 R' B R F2 R2", 
                "L' B L' F2 L B' L' F2 L2", 
                ]
        for i in range(10):
            result(random.choice([None, "U", "U2", "U'"]) or [])
            result(random.choice([None, "y", "y2", "y'"]) or [])
            result(random.choice(choices))
        return result
    def test(self):
        solver = PLLSolver()
        record = ()
        cube = self.random_cube()
        record += (cube.copy(), )
        solver.feed(cube)
        record += (solver.solve(), )
        record += (solver.is_solved(), )
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


