"""
This is the module for solving the F2L.
"""

import _import
from cube import *
from solve import scramble, solve_cross, solve_ll
from color_converter import color_convert as cc
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
	data = get_pair(cube, colors)

print get_pair(initial_cube(), set(['red', 'green']))

