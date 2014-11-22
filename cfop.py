from pycuber.solver.cfop.cross import CrossSolver
from pycuber.solver.cfop.f2l import F2LSolver
from pycuber.solver.cfop.oll import OLLSolver
from pycuber.solver.cfop.pll import PLLSolver
import pycuber as pc

class CFOPSolver(object):
    """
    Implement another solver that yields every step.
    """
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        result = pc.Algo()
        solver = CrossSolver(self.cube)
        cross = solver.solve()
        yield "CROSS", cross
        result += cross
        solver = F2LSolver(self.cube)
        for pair in solver.solve():
            f2l = pair[1]
            yield "F2L {0}".format(pair[0]), f2l
            result += f2l
        solver = OLLSolver(self.cube)
        oll = solver.solve()
        yield "OLL", oll
        result += oll
        solver = PLLSolver(self.cube)
        pll = solver.solve()
        yield "PLL", pll
        result += pll
        return result
