def initial_cube():
	return [[[c, c, c], [c, c, c], [c, c, c]] for c in "LUFDRB"]

def U(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[1] = [[cube[1][2][0], cube[1][1][0], cube[1][0][0]], [cube[1][2][1], cube[1][1][1], cube[1][0][1]], [cube[1][2][2], cube[1][1][2], cube[1][0][2]]]
	result[0][0] = cube[2][0]
	result[2][0] = cube[4][0]
	result[4][0] = cube[5][0]
	result[5][0] = cube[0][0]
	return result

def Ui(cube):
	return U(U(U(cube)))

def U2(cube):
	return U(U(cube))

def F(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[2] = [[cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[2][2][1], cube[2][1][1], cube[2][0][1]], [cube[2][2][2], cube[2][1][2], cube[2][0][2]]]
	result[1][2] = [cube[0][2][2], cube[0][1][2], cube[0][0][2]]
	(result[4][0][0], result[4][1][0], result[4][2][0]) = tuple(cube[1][2])
	result[3][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
	(result[0][0][2], result[0][1][2], result[0][2][2]) = tuple(cube[3][0])
	return result

def Fi(cube):
	return F(F(F(cube)))

def F2(cube):
	return F(F(cube))

def L(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[0] = [[cube[0][2][0], cube[0][1][0], cube[0][0][0]], [cube[0][2][1], cube[0][1][1], cube[0][0][1]], [cube[0][2][2], cube[0][1][2], cube[0][0][2]]]
	(result[1][2][0], result[1][1][0], result[1][0][0]) = (cube[5][0][2], cube[5][1][2], cube[5][2][2])
	(result[2][0][0], result[2][1][0], result[2][2][0]) = (cube[1][0][0], cube[1][1][0], cube[1][2][0])
	(result[3][0][0], result[3][1][0], result[3][2][0]) = (cube[2][0][0], cube[2][1][0], cube[2][2][0])
	(result[5][2][2], result[5][1][2], result[5][0][2]) = (cube[3][0][0], cube[3][1][0], cube[3][2][0])
	return result

def Li(cube):
	return L(L(L(cube)))

def L2(cube):
	return L(L(cube))

def R(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[4] = [[cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[4][2][1], cube[4][1][1], cube[4][0][1]], [cube[4][2][2], cube[4][1][2], cube[4][0][2]]]
	(result[1][2][2], result[1][1][2], result[1][0][2]) = (cube[2][2][2], cube[2][1][2], cube[2][0][2])
	(result[2][0][2], result[2][1][2], result[2][2][2]) = (cube[3][0][2], cube[3][1][2], cube[3][2][2])
	(result[3][2][2], result[3][1][2], result[3][0][2]) = (cube[5][0][0], cube[5][1][0], cube[5][2][0])
	(result[5][2][0], result[5][1][0], result[5][0][0]) = (cube[1][0][2], cube[1][1][2], cube[1][2][2])
	return result

def Ri(cube):
	return R(R(R(cube)))

def R2(cube):
	return R(R(cube))

def B(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[5] = [[cube[5][2][0], cube[5][1][0], cube[5][0][0]], [cube[5][2][1], cube[5][1][1], cube[5][0][1]], [cube[5][2][2], cube[5][1][2], cube[5][0][2]]]
	result[1][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
	(result[4][2][2], result[4][1][2], result[4][0][2]) = tuple(cube[3][2])
	result[3][2] = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
	(result[0][2][0], result[0][1][0], result[0][0][0]) = tuple(cube[1][0])
	return result

def Bi(cube):
	return B(B(B(cube)))

def B2(cube):
	return B(B(cube))

def D(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[3] = [[cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[3][2][1], cube[3][1][1], cube[3][0][1]], [cube[3][2][2], cube[3][1][2], cube[3][0][2]]]
	result[0][2] = cube[5][2]
	result[5][2] = cube[4][2]
	result[4][2] = cube[2][2]
	result[2][2] = cube[0][2]
	return result

def Di(cube):
	return D(D(D(cube)))

def D2(cube):
	return D(D(cube))

def M(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	(result[1][0][1], result[1][1][1], result[1][2][1]) = (cube[5][2][1], cube[5][1][1], cube[5][0][1])
	(result[2][0][1], result[2][1][1], result[2][2][1]) = (cube[1][0][1], cube[1][1][1], cube[1][2][1])
	(result[3][0][1], result[3][1][1], result[3][2][1]) = (cube[2][0][1], cube[2][1][1], cube[2][2][1])
	(result[5][0][1], result[5][1][1], result[5][2][1]) = (cube[3][2][1], cube[3][1][1], cube[3][0][1])
	return result

def Mi(cube):
	return M(M(M(cube)))

def M2(cube):
	return M(M(cube))

def S(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	(result[0][0][1], result[0][1][1], result[0][2][1]) = cube[3][1]
	result[1][1] = [cube[0][2][1], cube[0][1][1], cube[0][0][1]]
	(result[4][0][1], result[4][1][1], result[4][2][1]) = cube[1][1]
	result[3][1] = [cube[4][2][1], cube[4][1][1], cube[4][0][1]]
	return result

def Si(cube):
	return S(S(S(cube)))

def S2(cube):
	return S(S(cube))

def E(cube):
	result = [[[z for z in y] for y in x] for x in cube]
	result[0][1] = cube[5][1]
	result[2][1] = cube[0][1]
	result[4][1] = cube[2][1]
	result[5][1] = cube[4][1]
	return result

def Ei(cube):
	return E(E(E(cube)))

def E2(cube):
	return E(E(cube))

def f(cube):
	return S(F(cube))

def fi(cube):
	return f(f(f(cube)))

def f2(cube):
	return f(f(cube))

def b(cube):
	return Si(B(cube))

def bi(cube):
	return b(b(b(cube)))

def b2(cube):
	return b(b(cube))

def l(cube):
	return M(L(cube))

def li(cube):
	return l(l(l(cube)))

def l2(cube):
	return l(l(cube))

def r(cube):
	return Mi(R(cube))

def ri(cube):
	return r(r(r(cube)))

def r2(cube):
	return r(r(cube))

def u(cube):
	return Ei(U(cube))

def ui(cube):
	return u(u(u(cube)))

def u2(cube):
	return u(u(cube))

def d(cube):
	return E(D(cube))

def di(cube):
	return d(d(d(cube)))

def d2(cube):
	return d(d(cube))

def x(cube):
	return li(R(cube))

def xi(cube):
	return x(x(x(cube)))

def x2(cube):
	return x(x(cube))

def y(cube):
	return u(Di(cube))

def yi(cube):
	return y(y(y(cube)))

def y2(cube):
	return y(y(cube))

def z(cube):
	return f(Bi(cube))

def zi(cube):
	return z(z(z(cube)))

def z2(cube):
	return z(z(cube))

def sequence(alg, cube):
	if isinstance(alg, str):
		alg = alg.split()
	for m in alg:
		cube = eval("%s(cube)" % m.replace("'", 'i', 1))
	return cube

def shortest_path_search(start, successors, is_goal):
    if is_goal(start):
        return [start]
    explored = [] # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (action, state) in successors(s, path_actions(path)[-1] if len(path) != 1 else None).items():
            if state not in explored:
                explored.append(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def a_star_search(start, successors, state_value, is_goal):
    if is_goal(start):
        return [start]
    explored = []
    g = 1
    h = state_value(start)
    f = g + h
    p = [start]
    frontier = [(f, g, h, p)]
    while frontier:
        f, g, h, path = frontier.pop(0)
        s = path[-1]
        for (action, state) in successors(s, path_actions(path)[-1] if len(path) != 1 else None).items():
            if state not in explored:
                explored.append(state)
                path2 = path + [action, state]
                h2 = state_value(state)
                g2 = g + 1
                f2 = h2 + g2
                if is_goal(state):
                    return path2
                else:
                    frontier.append((f2, g2, h2, path2))
                    frontier.sort()
    return []

def path_states(path):
    return path[0::2]
    
def path_actions(path):
    return path[1::2]

def color_convert(l):
	colors = ["red", "yellow", "green", "white", "orange", "blue", "unknown"]
	result = []
	index = 0
	for i in range(6):
		result.append([])
		for j in range(3):
			result[i].append([])
			for k in range(3):
				if isinstance(l, str):
					result[i][j].append(colors[int(l[index])])
				else:
					result[i][j].append(colors[l[index]])
				index += 1
	return result

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

def get_3d_pos(poses):
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
	p = {"SOLVED":7, "WRONGSLOT":6, "ESLOTFREE":5, "CSLOTFREE":4, "BOTHSLOTFREE":3, "WRONGORIENT":2, "DIFSLOT":1}
	return sorted([set([cube[0][1][1], cube[2][1][1]]), set([cube[2][1][1], cube[4][1][1]]), set([cube[4][1][1], cube[5][1][1]]), set([cube[5][1][1], cube[0][1][1]])], key=lambda x:p[recog_type(cube, x)], reverse=True)

def empty_slots(cube):
	slots = []
	for (face1, face2) in [(0, 2), (2, 4), (4, 5), (5, 0)]:
		slot = set([cube[face1][1][1], cube[face2][1][1]])
		_type = recog_type(cube, slot)
		if _type != "SOLVED":
			slots.append(slot)
	return slots

def difslot(cube, colors):
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

solved = lambda x, y: []

def wrongslot(cube, colors):
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
	_type = recog_type(cube, colors)
	return eval(_type.lower() + "(cube, colors)")

def side_recog(cube, ll):
	side_ll = cube[0][0] + cube[2][0] + cube[4][0] + cube[5][0]
	for i in range(len(side_ll)):
		if int(ll[i]) != (side_ll[i] == cube[1][1][1]):
			return False
	return True


def O00_recog(c): return side_recog(c, "000000000000")

def O01_recog(c): return side_recog(c, "111010111010")

def O02_recog(c): return side_recog(c, "111011010110")

def O03_recog(c): return side_recog(c, "011010011011")

def O04_recog(c): return side_recog(c, "110110110010")

def O05_recog(c): return side_recog(c, "011000001011")

def O06_recog(c): return side_recog(c, "110110100000")

def O07_recog(c): return side_recog(c, "000011011001")

def O08_recog(c): return side_recog(c, "000100110110")

def O09_recog(c): return side_recog(c, "100110010100")

def O10_recog(c): return side_recog(c, "001001010011")

def O11_recog(c): return side_recog(c, "010001001011")

def O12_recog(c): return side_recog(c, "100100010110")

def O13_recog(c): return side_recog(c, "000011001011")

def O14_recog(c): return side_recog(c, "100110000110")

def O15_recog(c): return side_recog(c, "001011001010")

def O16_recog(c): return side_recog(c, "100110100010")

def O17_recog(c): return side_recog(c, "011010010110")

def O18_recog(c): return side_recog(c, "010010010111")

def O19_recog(c): return side_recog(c, "011010110010")

def O20_recog(c): return side_recog(c, "010010010010")

def O21_recog(c): return side_recog(c, "000101000101")

def O22_recog(c): return side_recog(c, "101001000100")

def O23_recog(c): return side_recog(c, "000101000000")

def O24_recog(c): return side_recog(c, "000100000001")

def O25_recog(c): return side_recog(c, "100001000000")

def O26_recog(c): return side_recog(c, "100100100000")

def O27_recog(c): return side_recog(c, "000001001001")

def O28_recog(c): return side_recog(c, "010000000010")

def O29_recog(c): return side_recog(c, "001000110010")

def O30_recog(c): return side_recog(c, "011000100010")

def O31_recog(c): return side_recog(c, "000001010110")

def O32_recog(c): return side_recog(c, "010100000011")

def O33_recog(c): return side_recog(c, "000110000011")

def O34_recog(c): return side_recog(c, "100010001010")

def O35_recog(c): return side_recog(c, "010100001010")

def O36_recog(c): return side_recog(c, "011010000100")

def O37_recog(c): return side_recog(c, "000110011000")

def O38_recog(c): return side_recog(c, "000010110001")

def O39_recog(c): return side_recog(c, "000010100011")

def O40_recog(c): return side_recog(c, "001010000110")

def O41_recog(c): return side_recog(c, "010101000010")

def O42_recog(c): return side_recog(c, "000101010010")

def O43_recog(c): return side_recog(c, "000000111010")

def O44_recog(c): return side_recog(c, "111000000010")

def O45_recog(c): return side_recog(c, "101010000010")

def O46_recog(c): return side_recog(c, "010000111000")

def O47_recog(c): return side_recog(c, "010110101001")

def O48_recog(c): return side_recog(c, "101011010100")

def O49_recog(c): return side_recog(c, "111011000100")

def O50_recog(c): return side_recog(c, "000110111001")

def O51_recog(c): return side_recog(c, "101011000110")

def O52_recog(c): return side_recog(c, "010100111001")

def O53_recog(c): return side_recog(c, "111000101010")

def O54_recog(c): return side_recog(c, "111010101000")

def O55_recog(c): return side_recog(c, "111000111000")

def O56_recog(c): return side_recog(c, "010101010101")

def O57_recog(c): return side_recog(c, "000010000010")

def O00(c):
	""
	return c

def O01(c):
	"""
	R U2 R2 F R F' U2 R' F R F'
	"""
	return sequence("R U2 R2 F R Fi U2 Ri F R Fi", c)

def O02(c):
	"""
	F R U R' U' S R U R' U' f'
	"""
	return sequence("F R U Ri Ui S R U Ri Ui fi", c)

def O03(c):
	"""
	f R U R' U' f' U' F R U R' U' F'
	"""
	return sequence("f R U Ri Ui fi Ui F R U Ri Ui Fi", c)

def O04(c):
	"""
	f R U R' U' f' U F R U R' U' F'
	"""
	return sequence("f R U Ri Ui fi U F R U Ri Ui Fi", c)

def O05(c):
	"""
	r' U2 R U R' U r
	"""
	return sequence("ri U2 R U Ri U r", c)

def O06(c):
	"""
	r U2 R' U' R U' r'
	"""
	return sequence("r U2 Ri Ui R Ui ri", c)

def O07(c):
	"""
	r U R' U R U2 r'
	"""
	return sequence("r U Ri U R U2 ri", c)

def O08(c):
	"""
	r' U' R U' R' U2 r
	"""
	return sequence("ri Ui R Ui Ri U2 r", c)

def O09(c):
	"""
	R U R' U' R' F R2 U R' U' F'
	"""
	return sequence("R U Ri Ui Ri F R2 U Ri Ui Fi", c)

def O10(c):
	"""
	R U R' U R' F R F' R U2 R'
	"""
	return sequence("R U Ri U Ri F R Fi R U2 Ri", c)

def O11(c):
	"""
	M R U R' U R U2 R' U M'
	"""
	return sequence("M R U Ri U R U2 Ri U Mi", c)

def O12(c):
	"""
	M U2 R' U' R U' R' U2 R U M'
	"""
	return sequence("M U2 Ri Ui R Ui Ri U2 R U Mi", c)

def O13(c):
	"""
	r U' r' U' r U r' y' R' U R
	"""
	return sequence("r Ui ri Ui r U ri yi Ri U R", c)

def O14(c):
	"""
	l' U l U l' U' l y L U' L'
	"""
	return sequence("li U l U li Ui l y L Ui Li", c)

def O15(c):
	"""
	l' U' l L' U' L U l' U l
	"""
	return sequence("li Ui l Li Ui L U li U l", c)

def O16(c):
	"""
	r U r' R U R' U' r U' r'
	"""
	return sequence("r U ri R U Ri Ui r Ui ri", c)

def O17(c):
	"""
	R U R' U R' F R F' U2 R' F R F'
	"""
	return sequence("R U Ri U Ri F R Fi U2 Ri F R Fi", c)

def O18(c):
	"""
	F R U R' U y' R' U2 R' F R F'
	"""
	return sequence("F R U Ri U yi Ri U2 Ri F R Fi", c)

def O19(c):
	"""
	r' R U R U R' U' r x R2 U R U' x'
	"""
	return sequence("ri R U R U Ri Ui r x R2 U R Ui xi", c)

def O20(c):
	"""
	M U R U R' U' M2 U R U' r'
	"""
	return sequence("M U R U Ri Ui M2 U R Ui ri", c)

def O21(c):
	"""
	R U2 R' U' R U R' U' R U' R'
	"""
	return sequence("R U2 Ri Ui R U Ri Ui R Ui Ri", c)

def O22(c):
	"""
	R U2 R2 U' R2 U' R2 U2 R
	"""
	return sequence("R U2 R2 Ui R2 Ui R2 U2 R", c)

def O23(c):
	"""
	R2 D R' U2 R D' R' U2 R'
	"""
	return sequence("R2 D Ri U2 R Di Ri U2 Ri", c)

def O24(c):
	"""
	r U R' U' r' F R F'
	"""
	return sequence("r U Ri Ui ri F R Fi", c)

def O25(c):
	"""
	F' r U R' U' r' F R
	"""
	return sequence("Fi r U Ri Ui ri F R", c)

def O26(c):
	"""
	R U2 R' U' R U' R'
	"""
	return sequence("R U2 Ri Ui R Ui Ri", c)

def O27(c):
	"""
	R U R' U R U2 R'
	"""
	return sequence("R U Ri U R U2 Ri", c)

def O28(c):
	"""
	M' U M U2 M' U M
	"""
	return sequence("Mi U M U2 Mi U M", c)

def O29(c):
	"""
	L2 U' L B L' U L2 U' r' U' r
	"""
	return sequence("L2 Ui L B Li U L2 Ui ri Ui r", c)

def O30(c):
	"""
	R2 U R' B' R U' R2 U l U l'
	"""
	return sequence("R2 U Ri Bi R Ui R2 U l U li", c)

def O31(c):
	"""
	L' d' R d L U' r' U' r
	"""
	return sequence("Li di R d L Ui ri Ui r", c)

def O32(c):
	"""
	R d L' d' R' U l U l'
	"""
	return sequence("R d Li di Ri U l U li", c)

def O33(c):
	"""
	R U R' U' R' F R F'
	"""
	return sequence("R U Ri Ui Ri F R Fi", c)

def O34(c):
	"""
	R U R2 U' R' F R U R U' F'
	"""
	return sequence("R U R2 Ui Ri F R U R Ui Fi", c)

def O35(c):
	"""
	R U2 R2 F R F' R U2 R'
	"""
	return sequence("R U2 R2 F R Fi R U2 Ri", c)

def O36(c):
	"""
	L' U' L U' L' U L U L F' L' F
	"""
	return sequence("Li Ui L Ui Li U L U L Fi Li F", c)

def O37(c):
	"""
	F R U' R' U' R U R' F'
	"""
	return sequence("F R Ui Ri Ui R U Ri Fi", c)

def O38(c):
	"""
	R U R' U R U' R' U' R' F R F'
	"""
	return sequence("R U Ri U R Ui Ri Ui Ri F R Fi", c)

def O39(c):
	"""
	L F' L' U' L U F U' L'
	"""
	return sequence("L Fi Li Ui L U F Ui Li", c)

def O40(c):
	"""
	R' F R U R' U' F' U R
	"""
	return sequence("Ri F R U Ri Ui Fi U R", c)

def O41(c):
	"""
	R U' R' U2 R U y R U' R' U' F'
	"""
	return sequence("R Ui Ri U2 R U y R Ui Ri Ui Fi", c)

def O42(c):
	"""
	L' U L U2 L' U' y' L' U L U F
	"""
	return sequence("Li U L U2 Li Ui yi Li U L U F", c)

def O43(c):
	"""
	f' L' U' L U f
	"""
	return sequence("fi Li Ui L U f", c)

def O44(c):
	"""
	f R U R' U' f'
	"""
	return sequence("f R U Ri Ui fi", c)

def O45(c):
	"""
	F R U R' U' F'
	"""
	return sequence("F R U Ri Ui Fi", c)

def O46(c):
	"""
	R' U' R' F R F' U R
	"""
	return sequence("Ri Ui Ri F R Fi U R", c)

def O47(c):
	"""
	F' L' U' L U L' U' L U F
	"""
	return sequence("Fi Li Ui L U Li Ui L U F", c)

def O48(c):
	"""
	F R U R' U' R U R' U' F'
	"""
	return sequence("F R U Ri Ui R U Ri Ui Fi", c)

def O49(c):
	"""
	R' F R' F' R2 U2 y R' F R F'
	"""
	return sequence("Ri F Ri Fi R2 U2 y Ri F R Fi", c)

def O50(c):
	"""
	L F' L F L2 U2 y' L F' L' F
	"""
	return sequence("L Fi L F L2 U2 yi L Fi Li F", c)

def O51(c):
	"""
	f R U R' U' R U R' U' f'
	"""
	return sequence("f R U Ri Ui R U Ri Ui fi", c)

def O52(c):
	"""
	R U R' U R d' R U' R' F'
	"""
	return sequence("R U Ri U R di R Ui Ri Fi", c)

def O53(c):
	"""
	r' U' R U' R' U R U' R' U2 r
	"""
	return sequence("ri Ui R Ui Ri U R Ui Ri U2 r", c)

def O54(c):
	"""
	r U R' U R U' R' U R U2 r'
	"""
	return sequence("r U Ri U R Ui Ri U R U2 ri", c)

def O55(c):
	"""
	R U2 R2 U' R U' R' U2 F R F'
	"""
	return sequence("R U2 R2 Ui R Ui Ri U2 F R Fi", c)

def O56(c):
	"""
	f R U R' U' S' R U R' U' R U R' U' F'
	"""
	return sequence("f R U Ri Ui Si R U Ri Ui R U Ri Ui Fi", c)

def O57(c):
	"""
	R U R' U' M' U R U' r'
	"""
	return sequence("R U Ri Ui Mi U R Ui ri", c)

def recog_pattern(cube, matchset):
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

def Aa_perm(c):
	"""
	x R' U R' D2 R U' R' D2 R2
	"""
	return sequence("x Ri U Ri D2 R Ui Ri D2 R2", c)

def Ab_perm(c):
	"""
	x R2 D2 R U R' D2 R U' R
	"""
	return sequence("x R2 D2 R U Ri D2 R Ui R", c)

def E_perm(c):
	"""
	x R' U R D' R' U' R D R' U' R D' R' U R D
	"""
	return sequence("x Ri U R Di Ri Ui R D Ri Ui R Di Ri U R D", c)

def Ua_perm(c):
	"""
	R Ui R U R U R Ui Ri Ui R2
	"""
	return sequence("R Ui R U R U R Ui Ri Ui R2", c)

def Ub_perm(c):
	"""
	R2 U R U R' U' R' U' R' U R'
	"""
	return sequence("R2 U R U Ri Ui Ri Ui Ri U Ri", c)

def H_perm(c):
	"""
	M2 U M2 U2 M2 U M2
	"""
	return sequence("M2 U M2 U2 M2 U M2", c)

def Z_perm(c):
	"""
	M2 U M2 U M' U2 M2 U2 M' U2
	"""
	return sequence("M2 U M2 U Mi U2 M2 U2 Mi U2", c)

def Ja_perm(c):
	"""
	R' U L' U2 R U' R' U2 L R U'
	"""
	return sequence("Ri U Li U2 R Ui Ri U2 L R Ui", c)

def Jb_perm(c):
	"""
	L U' R U2 L' U L U2 L' R' U
	"""
	return sequence("L Ui R U2 Li U L U2 Li Ri U", c)

def T_perm(c):
	"""
	R U R' U' R' F R2 U' R' U' R U R' F'
	"""
	return sequence("R U Ri Ui Ri F R2 Ui Ri Ui R U Ri Fi", c)

def Ra_perm(c):
	"""
	L U2 L' U2 L F' L' U' L U L F L2 U
	"""
	return sequence("L U2 Li U2 L Fi Li Ui L U L F L2 U", c)

def Rb_perm(c):
	"""
	R' U2 R U2 R' F R U R' U' R' F' R2 U'
	"""
	return sequence("Ri U2 R U2 Ri F R U Ri Ui Ri Fi R2 Ui", c)

def F_perm(c):
	"""
	R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R
	"""
	return sequence("Ri Ui Fi R U Ri Ui Ri F R2 Ui Ri Ui R U Ri U R", c)

def V_perm(c):
	"""
	R' U R' d' R' F' R2 U' R' U R' F R F
	"""
	return sequence("Ri U Ri di Ri Fi R2 Ui Ri U Ri F R F", c)

def Na_perm(c):
	"""
	z D R' U R2 D' R D U' R' U R2 D' R U' R
	"""
	return sequence("z D Ri U R2 Di R D Ui Ri U R2 Di R Ui R", c)

def Nb_perm(c):
	"""
	z U' R D' R2 U R' D U' R D' R2 U R' D R'
	"""
	return sequence("z Ui R Di R2 U Ri D Ui R Di R2 U Ri D Ri", c)

def Y_perm(c):
	"""
	F R U' R' U' R U R' F' R U R' U' R' F R F'
	"""
	return sequence("F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi", c)

def Ga_perm(c):
	"""
	R2 u R' U R' U' R u' R2 y' R' U R
	"""
	return sequence("R2 u Ri U Ri Ui R ui R2 yi Ri U R", c)

def Gb_perm(c):
	"""
	R' U' R y R2 u R' U R U' R u' R2
	"""
	return sequence("Ri Ui R y R2 u Ri U R Ui R ui R2", c)

def Gc_perm(c):
	"""
	R2 u' R U' R U R' u R2 y R U' R'
	"""
	return sequence("R2 ui R Ui R U Ri u R2 y R Ui Ri", c)

def Gd_perm(c):
	"""
	R U R' y' R2 u' R U' R' U R' u R2
	"""
	return sequence("R U Ri yi R2 ui R Ui Ri U Ri u R2", c)

def None_perm(c):
	""
	return c

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
				cr_notation = [cube_rotate.__name__] if cube_rotate else []
				uo_notation = [U_orient.__name__] if U_orient else []
				algo = f.__doc__.replace("\n\t", "", 2).replace("'", "i", 1000).split()
				return cr_notation + uo_notation + algo

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

def scramble():
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
	return shuffled


def solve_cross(c):
    return path_actions(a_star_search(fetch_edges(c), cross_successors, cross_state_value, cross_goal))

def solve_f2l(cube):
	result = []
	c = [[[z for z in y] for y in x] for x in cube]
	for i in range(4):
		_ord = order(c)
		pair = _ord[i]
		alg = solve_f2l_pair(c, pair)
		result += alg
		c = sequence(alg, c)
	return result

def solve_oll(c):
	if is_solved_f2l(c):
		for i in range(58):
			result = eval("look_around(%s, O%02d_recog, O%02d)" % (str(c), i, i))
			if result != None: return result
		raise ValueError("Not a solvable OLL case.")
	raise ValueError("Non-solved F2L.")

def solve_pll(cube):
	if not is_solved_oll(cube):
		raise ValueError("Non-solved OLL or F2L")
	for p in ["None", "Aa", "Ab", "E", "Ua", "Ub", "H", "Z", "Ja", "Jb", "T", "Ra", "Rb", "F", "V", "Na", "Nb", "Y", "Ga", "Gb", "Gc", "Gd"]:
		result = eval("look_around(%s, %s_recog, %s_perm)" % (str(cube), p, p))
		if result != None:
			return result
	raise ValueError("Not a solvable pll case.")

def solve_cube(cube):
	_cube = [[[z for z in y] for y in x] for x in cube]
	result = []
	C = solve_cross(_cube)
	result += C
	_cube = sequence(C, _cube)
	F = solve_f2l(_cube)
	result += F
	_cube = sequence(F, _cube)
	O = solve_oll(_cube)
	result += O
	_cube = sequence(O, _cube)
	P = solve_pll(_cube)
	result += P
	_cube = sequence(P, _cube)
	return result

wide_action = {
	"l":["R", "xi"], 
	"r":["L", "x"], 
	"u":["D", "y"], 
	"d":["U", "yi"], 
	"f":["B", "z"], 
	"b":["F", "zi"], 
	"M":["R", "Li", "xi"], 
	"S":["Fi", "B", "z"], 
	"E":["U", "Di", "yi"]
}

def optimize_wide_action(alg):
	result = []
	for act in alg:
		if act[0] in "lrudfbMSE":
			new_action = wide_action[act[0]][:]
			for i in range(len(new_action)):
				if not act[1:]:
					pass
				elif act[1] == "i":
					if len(new_action[i]) == 2:
						new_action[i] = new_action[i][0]
					elif len(new_action[i]) == 1:
						new_action[i] += "i"
				elif act[1] == "2":
					new_action[i] = new_action[i][0] + "2"
			result += new_action
		else:
			result.append(act)
	return result

rotationless = {
	"x": {
		"U":"F", 
		"D":"B", 
		"R":"R", 
		"L":"L", 
		"F":"D", 
		"B":"U"
	}, 
	"y": {
		"U":"U", 
		"D":"D", 
		"F":"R", 
		"B":"L", 
		"R":"B", 
		"L":"F"
	}, 
	"z": {
		"U":"L", 
		"D":"R", 
		"F":"F", 
		"B":"B", 
		"R":"U", 
		"L":"D"
	}
}

def optimize_rotationless(alg):
	result = []
	for i in range(len(alg)-1, -1, -1):
		if alg[i][0] in "xyz":
			for q in range(len(result)):
				if not alg[i][1:]:
					result[q] = rotationless[alg[i]][result[q][0]] + result[q][1:]
				elif alg[i][1:] == "i":
					for (key, value) in rotationless[alg[i][0]].items():
						if value == result[q][0]:
							result[q] = key + result[q][1:]
							break
				elif alg[i][1:] == "2":
					result[q] = rotationless[alg[i][0]][rotationless[alg[i][0]][result[q][0]]] + result[q][1:]
		else:
			result.append(alg[i])
	result.reverse()
	return result

def optimize_same_side(alg):
	result = []
	last_move = " "
	before2_move = " "
	opposite = {'L':'R', 'U':'D', 'F':'B', 'D':'U', 'R':'L', 'B':'F'}
	for i in range(len(alg)):
		if alg[i][0] == last_move[0]:
			val = 0
			for act in (alg[i], last_move):
				if not act[1:]:
					val += 1
				elif act[1:] == "i":
					val += 3
				else:
					val += 2
			if val % 4 == 0:
				del result[-1]
				if result:
					last_move = result[-1]
			elif val % 4 == 1:
				result[-1] = result[-1][0]
				last_move = result[-1]
			elif val % 4 == 2:
				result[-1] = result[-1][0] + "2"
				last_move = result[-1]
			else:
				result[-1] = result[-1][0] + "i"
				last_move = result[-1]
		elif alg[i][0] == before2_move[0] and alg[i][0] == opposite[last_move[0]]:
			val = 0
			for act in (alg[i], before2_move):
				if not act[1:]:
					val += 1
				elif act[1:] == "i":
					val += 3
				else:
					val += 2
			if val % 4 == 0:
				del result[-2]
				if len(result) == 1:
					last_move = result[-1]
					before2_move = " "
				else:
					last_move, before2_move = result[-1], result[-2]
			elif val % 4 == 1:
				result[-2] = result[-2][0]
				before2_move = result[-2]
			elif val % 4 == 2:
				result[-2] = result[-2][0] + "2"
				before2_move = result[-2]
			else:
				result[-2] = result[-2][0] + "i"
				before2_move = result[-2]
		else:
			result.append(alg[i])
			last_move, before2_move = result[-1], last_move
	return result

def optimize(alg):
	return optimize_same_side(optimize_rotationless(optimize_wide_action(alg)))

def full_solve(cube):
	return optimize(solve_cube(cube))

def structured_solving(cube):
	_cube = [[[z for z in y] for y in x] for x in cube]
	solving = {}
	C = solve_cross(_cube)
	_cube = sequence(C, _cube)
	solving["C"] = C
	solving["F"] = []
	for i in range(4):
		solving["F"].append({})
		_ord = order(_cube)
		pair = _ord[i]
		solving["F"][i]["colors"] = list(pair)
		alg = solve_f2l_pair(_cube, pair)
		solving["F"][i]["solve"] = alg
		_cube = sequence(alg, _cube)
	O = solve_oll(_cube)
	_cube = sequence(O, _cube)
	solving["O"] = O
	P = solve_pll(_cube)
	solving["P"] = P
	return solving