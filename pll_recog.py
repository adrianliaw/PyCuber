from cube import *
from pll import *
from color_converter import color_convert as cc

def look_around(cube, goal, f):
	#notations = {"U":"U", "Ui":"U'", "U2":"U2", "x":"x", "xi":"x'", "x2":"x2"}
	for U_orient in [None, U, Ui, U2]:
		for cube_rotate in [None, y, y2, yi]:
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
				pll_algo = (" " if cr_notation + uo_notation else "") + f.__doc__.replace("\n\t", "", 2)
				#print cr_notation + uo_notation + pll_algo
				return cr_notation + uo_notation + pll_algo

def recog_pattern(cube, **matchset):
	states = {'L':0, 'U':1, 'F':2, 'D':3, 'R':4, 'B':5}
	for side in matchset:
		color_pos = matchset[side]
		if [cube[color_pos[x][0]][0][color_pos[x][1]] for x in range(len(color_pos))] != [cube[states[side]][1][1]] * 3:
			return False
	return True

def None_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (0, 1), (0, 2)], F=[(2, 0), (2, 1), (2, 2)], R=[(4, 0), (4, 1), (4, 2)], B=[(5, 0), (5, 1), (5, 2)])

def Aa_recog(cube):
	return recog_pattern(cube, L=[(2, 0), (0, 1), (2, 2)], F=[(4, 0), (2, 1), (5, 2)], R=[(0, 0), (4, 1), (4, 2)], B=[(5, 0), (5, 1), (0, 2)])

def Ab_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (0, 1), (4, 2)], F=[(5, 0), (2, 1), (0, 2)], R=[(2, 0), (4, 1), (2, 2)], B=[(4, 0), (5, 1), (5, 2)])

def E_recog(cube):
	return recog_pattern(cube, L=[(2, 0), (0, 1), (5, 2)], F=[(0, 0), (2, 1), (4, 2)], R=[(5, 0), (4, 1), (2, 2)], B=[(4, 0), (5, 1), (0, 2)])

def Ua_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (4, 1), (0, 2)], F=[(2, 0), (0, 1), (2, 2)], R=[(4, 0), (2, 1), (4, 2)], B=[(5, 0), (5, 1), (5, 2)])

def Ub_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (2, 1), (0, 2)], F=[(2, 0), (4, 1), (2, 2)], R=[(4, 0), (0, 1), (4, 2)], B=[(5, 0), (5, 1), (5, 2)])

def H_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (4, 1), (0, 2)], F=[(2, 0), (5, 1), (2, 2)], R=[(4, 0), (0, 1), (4, 2)], B=[(5, 0), (2, 1), (5, 2)])

def Z_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (5, 1), (0, 2)], F=[(2, 0), (4, 1), (2, 2)], R=[(4, 0), (2, 1), (4, 2)], B=[(5, 0), (0, 1), (5, 2)])

def Ja_recog(cube):
	return recog_pattern(cube, L=[(5, 0), (5, 1), (0, 2)], F=[(2, 0), (2, 1), (2, 2)], R=[(4, 0), (4, 1), (5, 2)], B=[(0, 0), (0, 1), (4, 2)])

def Jb_recog(cube):
	return recog_pattern(cube, L=[(5, 0), (0, 1), (0, 2)], F=[(2, 0), (2, 1), (2, 2)], R=[(4, 0), (5, 1), (5, 2)], B=[(0, 0), (4, 1), (4, 2)])

def T_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (4, 1), (0, 2)], F=[(2, 0), (2, 1), (4, 2)], R=[(5, 0), (0, 1), (2, 2)], B=[(4, 0), (5, 1), (5, 2)])

def Ra_recog(cube):
	return recog_pattern(cube, L=[(5, 0), (2, 1), (0, 2)], F=[(2, 0), (0, 1), (2, 2)], R=[(4, 0), (4, 1), (5, 2)], B=[(0, 0), (5, 1), (4, 2)])

def Rb_recog(cube):
	return recog_pattern(cube, L=[(5, 0), (0, 1), (0, 2)], F=[(2, 0), (4, 1), (2, 2)], R=[(4, 0), (2, 1), (5, 2)], B=[(0, 0), (5, 1), (4, 2)])

def F_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (0, 1), (0, 2)], F=[(2, 0), (5, 1), (4, 2)], R=[(5, 0), (4, 1), (2, 2)], B=[(4, 0), (2, 1), (5, 2)])

def V_recog(cube):
	return recog_pattern(cube, L=[(4, 0), (0, 1), (0, 2)], F=[(2, 0), (2, 1), (5, 2)], R=[(0, 0), (5, 1), (4, 2)], B=[(5, 0), (4, 1), (2, 2)])

def Na_recog(cube):
	return recog_pattern(cube, L=[(4, 0), (0, 1), (0, 2)], F=[(2, 0), (5, 1), (5, 2)], R=[(0, 0), (4, 1), (4, 2)], B=[(5, 0), (2, 1), (2, 2)])

def Nb_recog(cube):
	return recog_pattern(cube, L=[(0, 0), (0, 1), (4, 2)], F=[(5, 0), (5, 1), (2, 2)], R=[(4, 0), (4, 1), (0, 2)], B=[(2, 0), (2, 1), (5, 2)])

def Y_recog(cube):
	return recog_pattern(cube, L=[(4, 0), (5, 1), (0, 2)], F=[(2, 0), (2, 1), (5, 2)], R=[(0, 0), (4, 1), (4, 2)], B=[(5, 0), (0, 1), (2, 2)])

def Ga_recog(cube):
	return recog_pattern(cube, L=[(2, 0), (5, 1), (4, 2)], F=[(5, 0), (2, 1), (2, 2)], R=[(4, 0), (0, 1), (5, 2)], B=[(0, 0), (4, 1), (0, 2)])

def Gb_recog(cube):
	return recog_pattern(cube, L=[(4, 0), (2, 1), (5, 2)], F=[(0, 0), (5, 1), (0, 2)], R=[(2, 0), (4, 1), (4, 2)], B=[(5, 0), (0, 1), (2, 2)])

def Gc_recog(cube):
	return recog_pattern(cube, L=[(4, 0), (2, 1), (5, 2)], F=[(0, 0), (4, 1), (0, 2)], R=[(2, 0), (0, 1), (4, 2)], B=[(5, 0), (5, 1), (2, 2)])

def Gd_recog(cube):
	return recog_pattern(cube, L=[(2, 0), (5, 1), (4, 2)], F=[(5, 0), (0, 1), (2, 2)], R=[(4, 0), (4, 1), (5, 2)], B=[(0, 0), (2, 1), (0, 2)])

def solve_pll(cube):
	for p in ["None", "Aa", "Ab", "E", "Ua", "Ub", "H", "Z", "Ja", "Jb", "T", "Ra", "Rb", "F", "V", "Na", "Nb", "Y", "Ga", "Gb", "Gc", "Gd"]:
		result = eval("look_around(%s, %s_recog, %s_perm)" % (str(cube), p, p))
		if result:
			return result
	raise ValueError("Not a solvable pll case.")

print solve_pll(cc("502222222111111111450444444333333333225555555044000000"))