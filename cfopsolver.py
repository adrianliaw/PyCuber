from handler import *
import json
import solver_programs.CFOP.solve as solve

class CFOPHandler(Handler):
	def get(self):
		a = scramble()
		JSON = {"scramble":a}
		c = solve.sequence(a, solve.initial_cube())
		JSON["cube"] = c
		JSON["full_solve"] = solve.full_solve(c)