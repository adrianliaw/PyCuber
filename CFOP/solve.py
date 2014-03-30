"""
This is the module of solving the cube.

Every step of solving the cube are in this module.
"""

import _import
from cube import *
from pll import *
from pll_recog import *
from oll import *
from oll_recog import *
from cross import *
from sps import *
from color_converter import color_convert as cc

def look_around(cube, goal, f):
	"""
	This function is to perform the algorithm if it's the given case, return None otherwise.

	Walk through every cube rotation(y) and the U face turning,
	and check if the given cube is "goal", which is the recognize function,
	if it is, perform the algorithm, return the full action and the cube after performing the alg,
	the function f is the function of the algorithm.

	This function is to use in solving the last layer, so recognize it and perform algorithm.
	"""
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
				cr_notation = [cube_rotate.__name__] if cube_rotate else []
				uo_notation = [U_orient.__name__] if U_orient else []
				algo = f.__doc__.replace("\n\t", "", 2).replace("'", "i", 1000).split()
				return cr_notation + uo_notation + algo, f(new)

def is_solved_cube(cube):
	"""
	Check if the cube is solved.
	"""
	for i in range(len(cube)):
		for j in range(len(cube[i])):
			for q in range(len(cube[i][j])):
				if cube[i][j][q] != cube[i][1][1]:
					return False
	return True

def is_solved_cross(state):
	"""
	Check if the cross is solved (cross on D face).
	"""
	c = state[3][1][1]
   	return state[3][0][1] == c and state[3][1][0] == c and state[3][1][2] == c and state[3][2][1] == c and state[0][2][1] == state[0][2][2] and state[2][2][1] == state[2][1][1] and state[4][2][1] == state[4][1][1] and state[5][2][1] == state[5][1][1]

def is_solved_f2l(cube):
	"""
	check if the first two layers are solved.
	"""
	for p in cube[3]:
		for q in p:
			if q != cube[3][1][1]:
				return False
	for p in [cube[0], cube[2], cube[4], cube[5]]:
		if [p[1], p[2]] != [[p[1][1]] * 3] * 2:
			return False
	return True

def is_solved_oll(cube):
	"""
	Check if the OLL is solved.
	"""
	if is_solved_f2l(cube):
		if cube[1] == [[cube[1][1][1]] * 3] * 3:
			return True
	return False

def scramble():
	"""
	Randomly scramble a cube (25 steps), returns a string (sequence of the actions).
	"""
	import random
	before2_move = ""
	last_move = ""
	actions = ["%s%s" % (name, direction) for name in "LUFDRB" for direction in ["", "i", "2"]]
	opposite = {'L':'R', 'U':'D', 'F':'B', 'D':'U', 'R':'L', 'B':'F'}
	shuffled = []
	for i in range(25):
		last_act_removed = actions[:]
		if last_move:
			last_act_removed.remove(last_move[0])
			last_act_removed.remove(last_move[0]+"i")
			last_act_removed.remove(last_move[0]+"2")
		if before2_move:
			if opposite[before2_move[0]] == last_move[0]:
				last_act_removed.remove(before2_move[0])
				last_act_removed.remove(before2_move[0]+"i")
				last_act_removed.remove(before2_move[0]+"2")
		act = random.choice(last_act_removed)
		last_move, before2_move = act, last_move
		shuffled.append(act)
	return ' '.join(shuffled)


def solve_cross(c):
    """
    Solve the cross by A* searching algorithm.
    """
    return path_actions(a_star_search(fetch_edges(c), cross_successors, cross_state_value, cross_goal))


def solve_oll(c):
	"""
	Solve the OLL by look_around function (loop over every 57 OLL cases).
	"""
	if is_solved_f2l(c):
		for i in range(58):
			result = eval("look_around(%s, O%02d_recog, O%02d)" % (str(c), i, i))
			if result: return result
		raise ValueError("Not a solvable OLL case.")
	raise ValueError("Non-solved F2L.")

def solve_pll(cube):
	"""
	Solve the PLL by look_around function (loop over every 21 cases).
	"""
	if not is_solved_oll(cube):
		raise ValueError("Non-solved OLL or F2L")
	for p in ["None", "Aa", "Ab", "E", "Ua", "Ub", "H", "Z", "Ja", "Jb", "T", "Ra", "Rb", "F", "V", "Na", "Nb", "Y", "Ga", "Gb", "Gc", "Gd"]:
		result = eval("look_around(%s, %s_recog, %s_perm)" % (str(cube), p, p))
		if result:
			return result
	raise ValueError("Not a solvable pll case.")

def solve_ll(cube):
	"""
	Solve the last layer, which is OLL and PLL.
	"""
	try:
		oll_solved = solve_oll(cube)
		pll_solved = solve_pll(oll_solved[1])
		return oll_solved[0] + pll_solved[0]
	except:
		raise Exception("Wrong in the solving.")
