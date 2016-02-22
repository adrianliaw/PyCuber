import sys
import os
sys.path.insert(0, os.getcwd())
import pycuber as pc
c = pc.Cube()
alg = pc.Formula()
random_alg = alg.random()
c(random_alg)
#print(c)

from pycuber.solver import CFOPSolver

solver = CFOPSolver(c)

solution = solver.solve(suppress_progress_messages=True)

print(solution)