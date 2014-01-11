from cube import *
from pll import *
from pll_recog import *
from oll import *
from oll_recog import *
from color_converter import color_convert as cc

def look_around(cube, goal, f):
	for cube_rotate in [None, y, yi, y2]:
		for U_orient in [None, U, Ui, U2]:
			if U_orient:
				if cube_rotate:
					new = U_orient(cube_rotate(cube))
				else:
					new = U_orient(cube)
			else:
				if cube_rotate:
					new = cube_rotate(cube)
				else:
					new = [[[p for p in q] for q in r] for r in cube]
			if goal(new):
				cr_notation = cube_rotate.__name__ if cube_rotate else ""
				uo_notation = (" " if cr_notation and U_orient else "") + (U_orient.__name__ if U_orient else "")
				algo = (" " if cr_notation + uo_notation else "") + f.__doc__.replace("\n\t", "", 2)
				return cr_notation + uo_notation + algo, f(new)

def is_solved_cube(cube):
	for i in range(len(cube)):
		for j in range(len(cube[i])):
			for q in range(len(cube[i][j])):
				if cube[i][j][q] != cube[i][1][1]:
					return False
	return True

def is_solved_cross(state):
	c = state[3][1][1]
   	return state[3][0][1] == c and state[3][1][0] == c and state[3][1][2] == c and state[3][2][1] == c and state[0][2][1] == state[0][2][2] and state[2][2][1] == state[2][1][1] and state[4][2][1] == state[4][1][1] and state[5][2][1] == state[5][1][1]

def is_solved_f2l(cube):
	for p in cube[3]:
		for q in p:
			if q != cube[3][1][1]:
				return False
	for p in [cube[0], cube[2], cube[4], cube[5]]:
		if [p[1], p[2]] != [[p[1][1]] * 3] * 2:
			return False
	return True

def is_solved_oll(cube):
	if is_solved_f2l(cube):
		if cube[1] == [[cube[1][1][1]] * 3] * 3:
			return True
	return False

def scramble(cube):
	import random
	last_move = ""
	actions = []
	

	

def solve_oll(c):
	if is_solved_f2l(c):
		for i in range(58):
			result = eval("look_around(%s, O%02d_recog, O%02d)" % (str(c), i, i))
			if result: return result
		raise ValueError("Not a solvable OLL case.")
	raise ValueError("Non-solved F2L.")

def solve_pll(cube):
	if not is_solved_oll(cube):
		raise ValueError("Non-solved OLL or F2L")
	for p in ["None", "Aa", "Ab", "E", "Ua", "Ub", "H", "Z", "Ja", "Jb", "T", "Ra", "Rb", "F", "V", "Na", "Nb", "Y", "Ga", "Gb", "Gc", "Gd"]:
		result = eval("look_around(%s, %s_recog, %s_perm)" % (str(cube), p, p))
		if result:
			return result
	raise ValueError("Not a solvable pll case.")

def solve_ll(cube):
	try:
		oll_solved = solve_oll(cube)
		pll_solved = solve_pll(oll_solved[1])
		return oll_solved[0] + " " + pll_solved[0]
	except:
		raise Exception("Wrong in the solving.")

print solve_ll(cc("011000000242015525410222222333333333114444444111555555"))