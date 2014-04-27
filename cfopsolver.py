from handler import *
from CFOP import scramble, sequence, full_solve, structured_solving, initial_cube, color_convert
import json


class CFOPHandler(Handler):
	def get(self):
		if self.request.get("cube"):
			try:
				c = color_convert(str(self.request.get("cube")))
				_json = {"cube":c}
				_json["full_solve"] = full_solve(c)
				_json["structure"] = structured_solving(c)
			except ValueError:
				_json = {}
		else:
			a = scramble()
			_json = {"scramble":a}
			c = sequence(a, initial_cube())
			_json["cube"] = c
			_json["full_solve"] = full_solve(c)
			_json["structure"] = structured_solving(c)
		self.response.headers["Content-Type"] = "application/json"
		self.write(json.dumps(_json))

app = webapp2.WSGIApplication([("/CFOPsolve", CFOPHandler)])