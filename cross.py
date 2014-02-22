from sps import *
from cube import *

def fetch_edges(cube):
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
	for center in range(len(state[0])):
		for edge in state[1]:
			if edge[0][0] != state[0][3] or edge[0][1][0] != 3:
				return False
			if edge[1][0] != state[0][edge[1][1][0]]:
				return False
	return True

def cube_successors(state, last_action = None):
    successors = {}
    acts = ["F", "Fi", "F2", "U", "Ui", "U2", "R", "Ri", "R2", "L", "Li", "L2", "B", "Bi", "B2", "D", "Di", "D2"]
    if last_action:
        acts.remove(last_action[0])
        acts.remove(last_action[0] + "i")
        acts.remove(last_action[0] + "2")
    for action in acts:
        successors[action] = eval("%s(%s)" % (action, str(state)))
    return successors

def cross_state_value(state):
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
			print edge
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
	


from color_converter import color_convert as cc

#print path_actions(shortest_path_search(fetch_edges(cc("034005145340215131545321304422130405042542310122155332")), cross_successors, cross_goal))

#print a_star_search(fetch_edges(cc("666606636666616666666626636606532646666646636666656636")), cross_successors, cross_state_value, cross_goal)
show(cc("666606636666616666666626636606532646666646636666656636"))
#print fetch_edges(cc("626606636666316666666626636606536646666646666666656636"))