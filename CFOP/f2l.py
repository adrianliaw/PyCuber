"""
This is the module for solving the F2L.
"""

import _import
from cube import *

def get_3d_pos(poses):
	"""
	Get the cubie position in 3D.
	(0, 0, 0) is the position of center of the cube.
	X position is from left to right
	Y position is from bottom to top
	Z position is from back to front
	"""
	checking_pos, face = list(poses)[0][::2]
	if face in "UD":
		if face == "U":
			x, y, z = 0, 1, 0
		else:
			x, y, z = 0, -1, 0
		x = checking_pos[2] - 1
		z = checking_pos[1] - 1
		if face == "D": z *= -1
	elif face in "RL":
		if face == "R":
			x, y, z = 1, 0, 0
		else:
			x, y, z = -1, 0, 0
		y = (checking_pos[1] - 1) * -1
		z = checking_pos[2] - 1
		if face == "R": z *= -1
	else:
		if face == "F":
			x, y, z = 0, 0, 1
		else:
			x, y, z = 0, 0, -1
		y = (checking_pos[1] - 1) * -1
		x = checking_pos[2] - 1
		if face == "B": x *= -1
	return (x, y, z)

def get_edge(cube, colors):
	"""
	(set([((x, y, z), color, face, face_color), ((p, q, r), color, face, face_color)]), 3d_pos)
	"""
	all_edges = [((1, 2, 1), (2, 0, 1)),
				 ((1, 1, 0), (0, 0, 1)),
				 ((1, 0, 1), (5, 0, 1)),
				 ((1, 1, 2), (4, 0, 1)),
				 ((0, 1, 2), (2, 1, 0)),
				 ((0, 1, 0), (5, 1, 2)),
				 ((4, 1, 2), (5, 1, 0)),
				 ((4, 1, 0), (2, 1, 2)),
				 ((3, 2, 1), (5, 2, 1)),
				 ((3, 1, 0), (0, 2, 1)),
				 ((3, 0, 1), (2, 2, 1)),
				 ((3, 1, 2), (4, 2, 1))]
	faces = {0:"L", 1:"U", 2:"F", 3:"D", 4:"R", 5:"B"}
	for ((x, y, z), (p, q, r)) in all_edges:
		if set([cube[x][y][z], cube[p][q][r]]) == colors:
			colorpair = set([((x, y, z), cube[x][y][z], faces[x], cube[x][1][1]), ((p, q, r), cube[p][q][r], faces[p], cube[p][1][1])])
			return (colorpair, get_3d_pos(colorpair))

def get_corner(cube, colors):
	"""
	(set([((x, y, z), color, face, face_color), ((a, b, c), color, face, face_color), ((p, q, r), color, face, face_color)]), 3d_pos)
	"""
	all_corners = [((0, 0, 2), (1, 2, 0), (2, 0, 0)), 
				   ((0, 0, 0), (1, 0, 0), (5, 0, 2)), 
				   ((4, 0, 2), (1, 0, 2), (5, 0, 0)), 
				   ((2, 0, 2), (1, 2, 2), (4, 0, 0)), 
				   ((5, 2, 2), (3, 2, 0), (0, 2, 0)), 
				   ((3, 0, 0), (0, 2, 2), (2, 2, 0)), 
				   ((2, 2, 2), (3, 0, 2), (4, 2, 0)), 
				   ((3, 2, 2), (4, 2, 2), (5, 2, 0))]
	faces = {0:"L", 1:"U", 2:"F", 3:"D", 4:"R", 5:"B"}
	for ((x, y, z), (a, b, c), (p, q, r)) in all_corners:
		if set([cube[x][y][z], cube[a][b][c], cube[p][q][r]]) == colors:
			colorpair = set([((x, y, z), cube[x][y][z], faces[x], cube[x][1][1]), ((a, b, c), cube[a][b][c], faces[a], cube[a][1][1]), ((p, q, r), cube[p][q][r], faces[p], cube[p][1][1])])
			return (colorpair, get_3d_pos(colorpair))

def get_slot(cube, colors):
	"""
	Get the "slot" of a cubie, 
	can be any slot of the F2L, or slot free.
	"""
	if len(colors) == 2:
		edge, pos = get_edge(cube, colors)
		if pos[1] == 1:
			return None
		else:
			return set([e[3] for e in edge])
	elif len(colors) == 3:
		corner, pos = get_corner(cube, colors)
		if pos[1] == 1:
			return None
		else:
			return set([c[3] for c in corner if c[3] != cube[3][1][1]])

def get_orientation(cube, colors):
	"""
	Get the orientation code of the cubie.
	(Only for F2L edges and corners)

	Corner:
		In D layer:
			correct orientation     : 0
			turned clockwise        : 1
			turned counter-clockwise: 2
		In U layer:
			cross color on U        : 3
			turned clockwise        : 4
			turned counter-clockwise: 5
	Edge:
		In middle layer:
			correct orientation     : 0
			opposite orientation    : 1
		In U layer:
			T on left side          : 2
			T on right side         : 3
	"""
	slots = [(0, 2), (2, 4), (4, 5), (5, 0)]
	if len(colors) == 2:
		colorpair, threeDpos = get_edge(cube, colors)
		if threeDpos[1] == 0:
			orient = sorted(colorpair, key=lambda x:x[0][0])
			if orient[0][0][0] == 0 and orient[1][0][0] == 5:
				orient = orient[::-1]
			orient = tuple([x[1] for x in orient])
			for s in slots:
				correct_orient = (cube[s[0]][1][1], cube[s[1]][1][1])
				incorrect_orient = correct_orient[::-1]
				if orient in (correct_orient, incorrect_orient):
					if orient == correct_orient: return 0
					else: return 1
		else:
			for s in slots:
				slot_color = (cube[s[0]][1][1], cube[s[1]][1][1])
				if all(x[1] in slot_color for x in colorpair):
					for piece in colorpair:
						if piece[2] == "U":
							if piece[1] == slot_color[0]: return 3
							else: return 2
	else:
		colorpair, threeDpos = get_corner(cube, colors)
		if threeDpos[1] == -1:
			for x in colorpair:
				if x[1] == cube[3][1][1]:
					if x[0][0] == 3:
						return 0
					elif x[0][2] == 2:
						return 1
					elif x[0][2] == 0:
						return 2
		else:
			for x in colorpair:
				if x[1] == cube[3][1][1]:
					if x[0][0] == 1:
						return 3
					elif x[0][2] == 0:
						return 4
					elif x[0][2] == 2:
						return 5

def get_pair(cube, colors):
	"""
	Get the data from the F2L pair.
	Included:
		colorpair (set([((x, y, z), color, face, face_color)] * 2(3) ))
		3D position
		Slot location
		Orientation code
	"""
	pair = {'edge':{}, 'corner':{}}
	edge, pos = get_edge(cube, colors)
	pair['edge']['colorpair'] = edge
	pair['edge']['3dpos'] = pos
	pair['edge']['slot'] = get_slot(cube, colors)
	pair['edge']['orientation'] = get_orientation(cube, colors)
	corner, pos = get_corner(cube, colors | set([cube[3][1][1]]))
	pair['corner']['colorpair'] = corner
	pair['corner']['3dpos'] = pos
	pair['corner']['slot'] = get_slot(cube, colors | set([cube[3][1][1]]))
	pair['corner']['orientation'] = get_orientation(cube, colors | set([cube[3][1][1]]))
	return pair

def solve_combined(cube, colors):
	"""
	Solve the combined F2L pair.
	Included push-right, push-left, pull-right, pull-left cases.
	"""
	for cube_rotation in [None, "y", "yi", "y2"]:
		if cube_rotation:
			rotatedcube = eval(cube_rotation+"(cube)")
		else:
			rotatedcube = [[[p for p in q] for q in r] for r in cube]
		for U_rotation in [None, "U", "Ui", "U2"]:
			if U_rotation:
				Urotatedcube = eval(U_rotation+"(rotatedcube)")
			else:
				Urotatedcube = [[[p for p in q] for q in r] for r in rotatedcube]
			data = get_pair(Urotatedcube, colors)
			if set([Urotatedcube[0][1][1], Urotatedcube[2][1][1]]) == colors:
				if data['corner']['3dpos'] == (1, 1, 1) and data['corner']['orientation'] == 4 and data['edge']['3dpos'] == (0, 1, 1) and data['edge']['orientation'] == 2:
					result = ['Li', 'U', 'L']
				elif data['corner']['3dpos'] == (-1, 1, 1) and data['corner']['orientation'] == 5 and data['edge']['3dpos'] == (0, 1, -1) and data['edge']['orientation'] == 2:
					result = ['Li', 'Ui', 'L']
			elif set([Urotatedcube[2][1][1], Urotatedcube[4][1][1]]) == colors:
				if data['corner']['3dpos'] == (-1, 1, 1) and data['corner']['orientation'] == 5 and data['edge']['3dpos'] == (0, 1, 1) and data['edge']['orientation'] == 3:
					result = ['R', 'Ui', 'Ri']
				elif data['corner']['3dpos'] == (1, 1, 1) and data['corner']['orientation'] == 4 and data['edge']['3dpos'] == (0, 1, -1) and data['edge']['orientation'] == 3:
					result = ['R', 'U', 'Ri']
			try:
				result.insert(0, U_rotation)
				result.insert(0, cube_rotation)
				while None in result:
					result.remove(None)
				return result
			except NameError:
				continue

def recog_type(cube, colors):
	"""
	Recognize 7 types of F2L pair:
	1. DIFSLOT, edge and corner are in diffrent slots.
	2. SOLVED, the piar is solved.
	3. WRONGSLOT, the pair is combined and solved, but not in the correct slot.
	4. WRONGORIENT, both edge and corner are in the same slot, but have incorrect orientation.
	5. BOTHSLOTFREE, both edge and corner are slot-free.
	6. ESLOTFREE, only edge is slot-free.
	7. CSLOTFREE, only corner is slot-free.
	"""
	data = get_pair(cube, colors)
	if data['corner']['slot'] != data['edge']['slot'] and None not in (data['corner']['slot'], data['edge']['slot']):
		return "DIFSLOT"
	elif data['corner']['slot'] == data['edge']['slot'] == colors and data['corner']['orientation'] == data['edge']['orientation'] == 0:
		return "SOLVED"
	elif data['corner']['slot'] == data['edge']['slot'] and data['corner']['orientation'] == data['edge']['orientation'] == 0:
		return "WRONGSLOT"
	elif data['corner']['slot'] == data['edge']['slot'] != None:
		return "WRONGORIENT"
	elif data['corner']['slot'] == data['edge']['slot'] == None:
		return "BOTHSLOTFREE"
	elif data['edge']['slot'] == None:
		return "ESLOTFREE"
	elif data['corner']['slot'] == None:
		return "CSLOTFREE"

def order(cube):
	"""
	Order four F2L pairs to decide which pair gonna solve first.
	"""
	p = {"SOLVED":7, "WRONGSLOT":6, "ESLOTFREE":5, "CSLOTFREE":4, "BOTHSLOTFREE":3, "WRONGORIENT":2, "DIFSLOT":1}
	return sorted([set([cube[0][1][1], cube[2][1][1]]), set([cube[2][1][1], cube[4][1][1]]), set([cube[4][1][1], cube[5][1][1]]), set([cube[5][1][1], cube[0][1][1]])], key=lambda x:p[recog_type(cube, x)], reverse=True)

def empty_slots(cube):
	"""
	Returns a list of empty slots.
	"""
	slots = []
	for (face1, face2) in [(0, 2), (2, 4), (4, 5), (5, 0)]:
		slot = set([cube[face1][1][1], cube[face2][1][1]])
		_type = recog_type(cube, slot)
		if _type != "SOLVED":
			slots.append(slot)
	return slots

def difslot(cube, colors):
	"""
	Solve the pair that is in diffrent slots, 
	the way to do this is to pick up one of the edge and the corner, 
	and then solve it by "ESLOTFREE" or "CSLOTFREE".
	"""
	data = get_pair(cube, colors)
	if data['edge']['slot'] == colors:
		for cube_rotation in ["", "y", "yi", "y2"]:
			rotatedcube = eval(cube_rotation + "(cube)")
			if set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) == data['corner']['slot']:
				result = cube_rotation.split() + ["R", "Ui", "Ri"]
				result += cslotfree(sequence(result, cube), colors)
				return result
	else:
		for cube_rotation in ["", "y", "yi", "y2"]:
			rotatedcube = eval(cube_rotation + "(cube)")
			if set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) == data['edge']['slot']:
				result = cube_rotation.split() + ["R", "U", "Ri"]
				result += eslotfree(sequence(result, cube), colors)
				return result


"""
solved(cube, colors), nothing to solve, but is one of the cases.
"""
solved = lambda x, y: []

def wrongslot(cube, colors):
	"""
	Solve the F2L pair which is solved but in the incorrect slot, 
	the way to do this is to take the pair out of slot and put it into the correct slot.
	"""
	data = get_pair(cube, colors)
	for cube_rotation in ["", "y", "yi", "y2"]:
		rotatedcube = eval(cube_rotation + "(cube)")
		if set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) == data['corner']['slot']:
			result = cube_rotation.split() + ["R", "U", "Ri"]
	result += solve_combined(sequence(result, cube), colors)
	return result

_wrongorient = {
	"right-handed":{
		"01":['R', 'Ui', 'Ri', 'd', 'Ri', 'U2', 'R'], 
		"10":['R', 'Ui', 'Ri', 'Ui', 'R', 'U', 'Ri'], 
		"11":['R', 'Ui', 'Ri', 'Ui', 'R', 'Ui', 'Ri']
	}, 
	"left-handed":{
		"20":['Li', 'U', 'L', 'U', 'Li', 'Ui', 'L'], 
		"21":['Li', 'U', 'L', 'U', 'Li', 'U', 'L']
	}
}

def wrongorient(cube, colors):
	"""
	Solve the F2L pair that both of the edge and the corner are in the same slot, 
	but have the incorrect orientation, 
	_wrongorient has all these cases and algorithms.
	"""
	data = get_pair(cube, colors)
	slot = data['corner']['slot']
	for cube_rotation in ["", "y", "yi", "y2"]:
		rotatedcube = eval(cube_rotation + "(cube)")
		if set([rotatedcube[0][1][1], rotatedcube[2][1][1]]) == slot:
			alg = _wrongorient['left-handed'].get(str(data['corner']['orientation'])+str(data['edge']['orientation']))
			if alg:
				result = cube_rotation.split() + alg
				break
		elif set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) == slot:
			alg = _wrongorient['right-handed'].get(str(data['corner']['orientation'])+str(data['edge']['orientation']))
			if alg:
				result = cube_rotation.split() + alg
				break
	result += solve_combined(sequence(result, cube), colors)
	return result

_bothslotfree = {
	'right-handed': {
		"-1 -1 3 1 0 3" : ['R', 'U', 'Ri'], #F19
		"1 1 3 1 0 3"   : ['R', 'U2', 'Ri'], #F20
		"1 1 3 1 0 2"   : ['R', 'Ui', 'Ri', 'di', 'Li', 'Ui', 'L'], #F21
		"-1 1 3 1 0 3"  : ['R', 'U2', 'Ri'], #F22
		"1 -1 4 0 -1 3" : ['R', 'Ui', 'Ri'], #F29
		"1 1 4 1 0 2"   : ['R', 'Ui', 'Ri'], #F30
		"1 1 4 0 -1 3"  : [], #F31
		"1 -1 5 0 1 3"  : ['R', 'U2', 'Ri'], #F37
		"-1 1 5 0 1 3"  : [], #F38
		"1 -1 5 0 -1 2" : ['R', 'U2', 'Ri'], #F39
		"1 -1 5 -1 0 3" : ['R', 'U', 'Ri'], #F40
		"1 -1 5 -1 0 2" : ['R', 'Ui', 'Ri'] #F41
	}, 
	'left-handed': {
		"-1 1 3 -1 0 2" : ['Li', 'U2', 'L'], #F16
		"-1 1 3 -1 0 3" : ['Li', 'U', 'L', 'd', 'R', 'U', 'Ri'], #F17
		"1 1 3 -1 0 2"  : ['Li', 'U2', 'L'], #F18
		"1 -1 3 -1 0 2" : ['Li', 'Ui', 'L'], #F23
		"1 1 4 0 1 2"   : [], #F25
		"-1 -1 4 0 -1 3": ['Li', 'U2', 'L'], #F26
		"-1 -1 4 1 0 2" : ['Li', 'Ui', 'L'], #F27
		"-1 -1 4 1 0 3" : ['Li', 'U', 'L'], #F28
		"-1 -1 4 0 1 2" : ['Li', 'U2', 'L'], #F32
		"-1 -1 5 0 -1 2": ['Li', 'U', 'L'], #F34
		"-1 1 5 -1 0 3" : ['Li', 'U', 'L'], #F35
		"-1 1 5 0 -1 2" : [] #F36
	}
}

def bothslotfree(cube, colors):
	"""
	Solve the F2L pair that both edge and corner are slot-free, 
	_bothslotfree has all these cases and algorithms.
	"""
	empties = empty_slots(cube)
	flag = False
	for cube_rotation in ["", "y", "yi", "y2"]:
		rotatedcube = eval(cube_rotation + "(cube)")
		if set([rotatedcube[0][1][1], rotatedcube[2][1][1]]) in empties:
			for U_rotation in ["", "U", "Ui", "U2"]:
				Urotatedcube = eval(U_rotation + "(rotatedcube)")
				data = get_pair(Urotatedcube, colors)
				keydata = list(data['corner']['3dpos'][::2]) + [data['corner']['orientation']] + list(data['edge']['3dpos'][::2]) + [data['edge']['orientation']]
				alg = _bothslotfree['left-handed'].get(' '.join(map(lambda x:str(x), keydata)))
				if alg != None:
					result = cube_rotation.split() + U_rotation.split() + alg
					flag = True
					break
		if set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) in empties:
			for U_rotation in ["", "U", "Ui", "U2"]:
				Urotatedcube = eval(U_rotation + "(rotatedcube)")
				data = get_pair(Urotatedcube, colors)
				keydata = list(data['corner']['3dpos'][::2]) + [data['corner']['orientation']] + list(data['edge']['3dpos'][::2]) + [data['edge']['orientation']]
				alg = _bothslotfree['right-handed'].get(' '.join(map(lambda x:str(x), keydata)))
				if alg != None:
					result = cube_rotation.split() + U_rotation.split() + alg
					flag = True
					break
		if flag: break
	result += solve_combined(sequence(result, cube), colors)
	return result

_eslotfree = {
	'right-handed': {
		"0 -1 0 2" : ['R', 'Ui', 'Ri'], #F02
		"1 1 0 3"  : ['R', 'Ui', 'Ri'], #F10
		"2 1 0 3"  : ['R', 'U', 'Ri'] #F14
	}, 
	'left-handed': {
		"0 1 0 3"  : ['Li', 'U', 'L'], #F03
		"1 -1 0 2" : ['Li', 'Ui', 'L'], #F09
		"2 -1 0 2" : ['Li', 'U', 'L'] #F13
	}
}

def eslotfree(cube, colors):
	"""
	Solve the F2L pair which only the edge is slot-free, 
	_eslotfree has all these cases and algorithms.
	"""
	_data = get_pair(cube, colors)
	slot = _data['corner']['slot']
	flag = False
	for cube_rotation in ["", "y", "yi", "y2"]:
		rotatedcube = eval(cube_rotation + "(cube)")
		for U_rotation in ["", "U", "Ui", "U2"]:
			Urotatedcube = eval(U_rotation + "(rotatedcube)")
			data = get_pair(Urotatedcube, colors)
			if set([rotatedcube[0][1][1], rotatedcube[2][1][1]]) == slot:
				keydata = [data['corner']['orientation']] + list(data['edge']['3dpos'][::2]) + [data['edge']['orientation']]
				alg = _eslotfree['left-handed'].get(' '.join(map(lambda x:str(x), keydata)))
				if alg:
					result = cube_rotation.split() + U_rotation.split() + alg
					flag = True
					break
			elif set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) == slot:
				keydata = [data['corner']['orientation']] + list(data['edge']['3dpos'][::2]) + [data['edge']['orientation']]
				alg = _eslotfree['right-handed'].get(' '.join(map(lambda x:str(x), keydata)))
				if alg:
					result = cube_rotation.split() + U_rotation.split() + alg
					flag = True
					break
		if flag: break
	result += solve_combined(sequence(result, cube), colors)
	return result

_cslotfree = {
	'right-handed': {
		"0 1 -1 3"  : ['R', 'U', 'Ri', 'Ui', 'R', 'U', 'Ri'], #F04
		"0 1 -1 5"  : ['R', 'Ui', 'Ri'], #F06
		"1 1 1 3"   : ['R', 'Ui', 'Ri'], #F15
		"1 1 -1 5"  : ['R', 'U', 'Ri'] #F33
	}, 
	'left-handed' : {
		"0 -1 -1 4" : ['Li', 'U', 'L'], #F05
		"1 -1 -1 4" : ['Li', 'Ui', 'L'] #F24
	}
}

def cslotfree(cube, colors):
	"""
	Solve the F2L pair which only the corner is slot-free, 
	_cslotfree has all these cases and algorithms.
	"""
	_data = get_pair(cube, colors)
	slot = _data['edge']['slot']
	flag = False
	for cube_rotation in ["", "y", "yi", "y2"]:
		rotatedcube = eval(cube_rotation + "(cube)")
		for U_rotation in ["", "U", "Ui", "U2"]:
			Urotatedcube = eval(U_rotation + "(rotatedcube)")
			data = get_pair(Urotatedcube, colors)
			if set([rotatedcube[0][1][1], rotatedcube[2][1][1]]) == slot:
				keydata = [data['edge']['orientation']] + list(data['corner']['3dpos'][::2]) + [data['corner']['orientation']]
				alg = _cslotfree['left-handed'].get(' '.join(map(lambda x:str(x), keydata)))
				if alg:
					result = cube_rotation.split() + U_rotation.split() + alg
					flag = True
					break
			elif set([rotatedcube[2][1][1], rotatedcube[4][1][1]]) == slot:
				keydata = [data['edge']['orientation']] + list(data['corner']['3dpos'][::2]) + [data['corner']['orientation']]
				alg = _cslotfree['right-handed'].get(' '.join(map(lambda x:str(x), keydata)))
				if alg:
					result = cube_rotation.split() + U_rotation.split() + alg
					flag = True
					break
		if flag: break
	result += solve_combined(sequence(result, cube), colors)
	return result

def solve_f2l_pair(cube, colors):
	"""
	Given the cube and the colors of the pair, to solve a F2L pair.
	"""
	_type = recog_type(cube, colors)
	return eval(_type.lower() + "(cube, colors)")
