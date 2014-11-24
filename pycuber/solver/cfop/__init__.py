import sys, time, pycuber
from .cross import CrossSolver
from .f2l import F2LSolver
from .oll import OLLSolver
from .pll import PLLSolver

class CFOPSolver(object):
    def __init__(self, cube=None):
        self.cube = cube
    def feed(self, cube):
        self.cube = cube
    def solve(self):
        if not self.cube.is_valid():
            raise ValueError("Invalid Cube.")
        result = pycuber.Algo()
        sys.stdout.write("Solver starts....")
        sys.stdout.write("\rSolving Cross ......")
        solver = CrossSolver(self.cube)
        cross = solver.solve()
        result += cross
        sys.stdout.write("\rCross: {0}\n".format(cross))
        solver = F2LSolver(self.cube)
        f2lall = solver.solve()
        for i in range(4):
            sys.stdout.write("\rSolving F2L#{0} ......".format(i))
            f2l = next(f2lall)
            result += f2l[1]
            sys.stdout.write("\rF2L{0}: {1}\n".format(*f2l))
        solver = OLLSolver(self.cube)
        sys.stdout.write("\rSolving OLL ......")
        oll = solver.solve()
        result += oll
        sys.stdout.write("\rOLL:  {0}\n".format(oll))
        solver = PLLSolver(self.cube)
        sys.stdout.write("\rSolving PLL ......")
        pll = solver.solve()
        result += pll
        sys.stdout.write("\rPLL:  {0}\n".format(pll))
        sys.stdout.write("\nFULL: {0}\n".format(result.optimise()))
        return result

