from cube import *

def fetch_edges(cube):
	"""
	Fetch all four edges for the cross into the following notation:
	([L, U, F, D, R, B], set([(D, pos), (color, pos)*4]))
	"""
	D_face_color = cube[3][1][1]
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
	result = set()
	for ((x, y, z), (p, q, r)) in all_edges:
		if cube[x][y][z] == D_face_color:
			result.add(((cube[x][y][z], (x, y, z)), (cube[p][q][r], (p, q, r))))
		elif cube[p][q][r] == D_face_color:
			result.add(((cube[p][q][r], (p, q, r)), (cube[x][y][z], (x, y, z))))
	return ([cube[0][1][1], cube[1][1][1], cube[2][1][1], cube[3][1][1], cube[4][1][1], cube[5][1][1]], result)

def cross_successors(state, last_action=None):
	"""
	All successors for the solving the cross, 
	if the action doesn't dominate four white edges, it won't be the successor.
	"""
	cube = [[["unknown" for i in range(3)] for j in range(3)] for h in range(6)]
	(colors, edges) = state
	for edge in edges:
		for (color, (x, y, z)) in edge:
			cube[x][y][z] = color
	for center in range(len(colors)):
		cube[center][1][1] = colors[center]
	actions = "LUFDRB".replace(last_action[0] if last_action else "", "", 1)
	results = {}
	for layer in actions:
		for notation in ["", "i", "2"]:
			new = eval("%s(%s)" % (layer + notation, str(cube)))
			if new != cube:
				results[layer+notation] = fetch_edges(new)
	return results

def cross_goal(state):
	"""
	The goal function for finding the shortest path of cross.
	"""
	for center in range(len(state[0])):
		for edge in state[1]:
			if edge[0][0] != state[0][3] or edge[0][1][0] != 3:
				return False
			if edge[1][0] != state[0][edge[1][1][0]]:
				return False
	return True

def cross_state_value(state):
	"""
	Compute the state value of the cross solving.
	1. The orientation cost.
	2. Is in the relative position.
	"""
	edgeset = state[1]
	value = 0
	relative_pos = [state[0][i] for i in [0, 2, 4, 5]]
	for edge in edgeset:
		white_pos = edge[0][1]
		if white_pos[0] in [0, 2, 4, 5]:
			if white_pos[1] == 1:
				value += 1
			if white_pos[1] == 0:
				value += 2
			if white_pos[1] == 2:
				value += 3
		if white_pos[0] == 1:
			value += 1
	edgeposes = []
	ngedges = []
	for edge in edgeset:
		if edge[0][1][0] in [1, 3]:
			edgeposes.append((edge[1][1][0], edge[1][0]))
		else:
			if edge[0][1][1] == 1:
				edgeposes.append((edge[1][1][0], edge[1][0]))
			else:
				ngedges.append(edge)
	sides = [0, 2, 4, 5]
	for edge in ngedges:
		idx = sides.index(edge[0][1][0])
		for i in [-1, 1]:
			if sides[(idx+i)%4] not in dict(edgeposes):
				edgeposes.append((sides[(idx+i)%4], edge[1][0]))
				break
		else:
			counterclockwise = [x[0] for x in edgeposes].count(sides[(idx+1)%4])
			clockwise = [x[0] for x in edgeposes].count(sides[(idx-1)%4])
			if counterclockwise > clockwise:
				edgeposes.append((sides[(idx+1)%4], edge[1][0]))
			else:
				edgeposes.append((sides[(idx-1)%4], edge[1][0]))
	edgeposes.sort()
	colorpos = [x[1] for x in edgeposes]
	indexes = [x[0] for x in edgeposes]
	def shift(l, n):
		new = [None] * len(l)
		for i in range(len(l)):
			new[(i+n)%len(l)] = l[i]
		return new
	if all([indexes.count(x) == 1 for x in [0, 2, 4, 5]]):
		for i in range(4):
			if shift(colorpos, i) == relative_pos:
				break
		else:
			value += 5
	else:
		value += 3
	return value
