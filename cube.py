"""

This module simulates the rubik's cube,
simulates every move, twisting a layer, twisting two layers, or cube rotations.

Every move is represented by a symbol:

	L is the left face,
	U is the top face,
	F is the front face,
	D is the bottom face,
	R is the right face,
	B is the back face

	Uppercase letters means to twist one layer, lowercase letters means to twist two layers.

	Nothing added in the end means to twist it clockwise. ex: L, U, F etc.
	Add "i" in the end means to twist it counter-clockwise. ex: Li, Ui, Fi etc.
	Add "2" in the end means to twist it 180 degrees. ex: L2, U2, F2 etc.

	The middle layers are the layers between U and D (E), F and B (S), L and R (M)
	M action's direction is as same as L,
	S action's direction is as same as F,
	E action's direction is as same as D.

	For the cube rotations, imagine there are xyz axis,
	x point towards right, y point towards up, z point towards front.
	So "x" is to turn the x axis of the cube clockwise, "xi" is to turn the x axis of the cube counter-clockwise etc.

	Every inverse action (action that named "-i"), will set the __name__ attribute to "-'",
	because of the official notation.

"""


def initial_cube():
	"""
	initial a solved cube, with:
		red on L face
		yellow on U face
		green on F face
		white on D face
		orange on R face
		blue on B face
	"""
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
	"""
	This function takes two arguments, algorithm and the cube,
	algorithm is a sequence of symbols like "R U Ri Ui".
	"""
	if isinstance(alg, str):
		alg = alg.split()
	for m in alg:
		cube = eval("%s(cube)" % m.replace("'", 'i', 1))
	return cube

def show(cube):
	"""
	This show function makes the cube object more readable.
	"""
	for i in range(len(cube)):
		for l in range(len(cube[i])):
			print cube[i][l]
		print "\n"
	print "--------------------------------"
