import pycuber as pc
from pycuber.solver import CFOPSolver

"""These two tests only make sure no uncaught errors get raised.
    They do not test the validity of the solve.
"""

def test_for_basic_ability_to_solve():
    c = pc.Cube()
    alg = pc.Formula()
    random_alg = alg.random()
    c(random_alg)
    solver = CFOPSolver(c)
    solver.solve()


def test_solving_a_solved_cube():
    c = pc.Cube()
    solver = CFOPSolver(c)
    solver.solve()