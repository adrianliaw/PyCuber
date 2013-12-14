def initial_cube():
	return [[[c, c, c], [c, c, c], [c, c, c]] for c in ["red", "yellow", "green", "white", "orange", "blue"]]

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

def show(cube):
	for i in range(len(cube)):
		for l in range(len(cube[i])):
			print cube[i][l]
		print "\n"
	print "--------------------------------"



show(U2(M(U(M(U(M(U2(Mi(U(Mi(U(Mi(initial_cube())))))))))))))