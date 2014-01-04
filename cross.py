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
		if cube[x][y][z] == D_face_color or cube[p][q][r] == D_face_color:
			result.add(((cube[x][y][z], (x, y, z)), (cube[p][q][r], (p, q, r))))
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




#from color_converter import color_convert as cc

#print path_actions(shortest_path_search(fetch_edges(cc("034005145340215131545321304422130405042542310122155332")), cross_successors, cross_goal))




#print cross_successors(fetch_edges(initial_cube()), "Fi")
#print cross_goal(fetch_edges(initial_cube()))