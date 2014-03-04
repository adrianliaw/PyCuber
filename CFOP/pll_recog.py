"""

This module is to recognize all the PLL patterns.
Every recognize function is named by "--_recog", 
take a cube as an input, return True if it is the --_perm pattern, False otherwise.

"""


def recog_pattern(cube, matchset):
	"""
	This function is to recognize the PLL patterns, 

	The matchset is a string of 12 numbers, which can break down as four lists of three numbers, 
	ex:
	matchset -> "000222444555"
	-> [0, 0, 0](L face) [2, 2, 2](F face) [4, 4, 4](R face) [5, 5, 5](B face)
	Every number tells the function where is the cubie(color).
	"""
	matchset, _matchset = {}, matchset
	for i in range(12):
		if i % 3 == 0:
			face = []
		face.append((int(_matchset[i]), i % 3))
		if i % 3 == 2:
			matchset['LFRB'[i // 3]] = face
	states = {'L':0, 'F':2, 'R':4, 'B':5}
	for side in matchset:
		color_pos = matchset[side]
		if [cube[color_pos[x][0]][0][color_pos[x][1]] for x in range(len(color_pos))] != [cube[states[side]][1][1]] * 3:
			return False
	return True

def None_recog(cube):
	return recog_pattern(cube, "000222444555")

def Aa_recog(cube):
	return recog_pattern(cube, "400224545052")

def Ab_recog(cube):
	return recog_pattern(cube, "500225042454")

def E_recog(cube):
	return recog_pattern(cube, "205024542450")

def Ua_recog(cube):
	return recog_pattern(cube, "040202424555")

def Ub_recog(cube):
	return recog_pattern(cube, "020242404555")

def H_recog(cube):
	return recog_pattern(cube, "040252404525")

def Z_recog(cube):
	return recog_pattern(cube, "050242424505")

def Ja_recog(cube):
	return recog_pattern(cube, "550222445004")

def Jb_recog(cube):
	return recog_pattern(cube, "500222455044")

def T_recog(cube):
	return recog_pattern(cube, "040224502455")

def Ra_recog(cube):
	return recog_pattern(cube, "520202445054")

def Rb_recog(cube):
	return recog_pattern(cube, "500242425054")

def F_recog(cube):
	return recog_pattern(cube, "000254542425")

def V_recog(cube):
	return recog_pattern(cube, "400225054542")

def Na_recog(cube):
	return recog_pattern(cube, "400255044522")

def Nb_recog(cube):
	return recog_pattern(cube, "004552440225")

def Y_recog(cube):
	return recog_pattern(cube, "450225044502")

def Ga_recog(cube):
	return recog_pattern(cube, "254522405040")

def Gb_recog(cube):
	return recog_pattern(cube, "425050244502")

def Gc_recog(cube):
	return recog_pattern(cube, "425040204552")

def Gd_recog(cube):
	return recog_pattern(cube, "254502445020")

