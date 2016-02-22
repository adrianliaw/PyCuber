import sys
import os
import pycuber as pc
from pycuber.solver import CFOPSolver

c = pc.Cube()
alg = pc.Formula()
random_alg = alg.random()
c(random_alg)

solver = CFOPSolver(c)

solution = solver.solve(suppress_progress_messages=True)

print(solution)
