import sys
import time
import pycuber

if sys.version_info > (3,4):
    import io
else:
    import cStringIO as io

from .cross import CrossSolver
from .f2l import F2LSolver
from .oll import OLLSolver
from .pll import PLLSolver


class CFOPSolver(object):
    def __init__(self, cube=None):
        self.cube = cube

    def feed(self, cube):
        self.cube = cube

    def solve(self, suppress_progress_messages=False):
        if suppress_progress_messages:
            save_stdout = sys.stdout
            sys.stdout = io.StringIO()
        if not self.cube.is_valid():
            raise ValueError("Invalid Cube.")
        result = pycuber.Formula()
        sys.stdout.write("Solver starts....")

        sys.stdout.write("\rSolving Cross ......")
        solver = CrossSolver(self.cube)
        cross = solver.solve()
        result += cross
        sys.stdout.write("\x1b[2K\rCross: {0}\n".format(cross))

        solver = F2LSolver(self.cube)
        for i, f2l_single in enumerate(solver.solve(), 1):
            sys.stdout.write("Solving F2L#{0} ......".format(i))
            result += f2l_single[1]
            sys.stdout.write("\x1b[2K\rF2L{0}: {1}\n".format(*f2l_single))

        solver = OLLSolver(self.cube)
        sys.stdout.write("Solving OLL ......")
        oll = solver.solve()
        result += oll
        sys.stdout.write("\x1b[2K\rOLL:  {0}\n".format(oll))

        solver = PLLSolver(self.cube)
        sys.stdout.write("\rSolving PLL ......")
        pll = solver.solve()
        result += pll
        sys.stdout.write("\x1b[2K\rPLL:  {0}\n".format(pll))

        sys.stdout.write("\nFULL: {0}\n".format(result.optimise()))

        if suppress_progress_messages:
            sys.stdout = save_stdout
        return result
