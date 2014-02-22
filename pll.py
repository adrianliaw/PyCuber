"""
Nothing fancy here, all PLL algorithms.

Algorithms from: http://www.cubewhiz.com/pll.php

"""

from cube import *


def Aa_perm(c):
	"""
	x R' U R' D2 R U' R' D2 R2
	"""
	return R2(D2(Ri(Ui(R(D2(Ri(U(Ri(x(c))))))))))

def Ab_perm(c):
	"""
	x R2 D2 R U R' D2 R U' R
	"""
	return R(Ui(R(D2(Ri(U(R(D2(R2(x(c))))))))))

def E_perm(c):
	"""
	x R' U R D' R' U' R D R' U' R D' R' U R D
	"""
	return D(R(U(Ri(Di(R(Ui(Ri(D(R(Ui(Ri(Di(R(U(Ri(x(c)))))))))))))))))

def Ua_perm(c):
	"""
	R U' R U R U R U' R' U' R2
	"""
	return R2(Ui(Ri(Ui(R(U(R(U(R(Ui(R(c)))))))))))

def Ub_perm(c):
	"""
	R2 U R U R' U' R' U' R' U R'
	"""
	return Ri(U(Ri(Ui(Ri(Ui(Ri(U(R(U(R2(c)))))))))))

def H_perm(c):
	"""
	M2 U M2 U2 M2 U M2
	"""
	return M2(U(M2(U2(M2(U(M2(c)))))))

def Z_perm(c):
	"""
	M2 U M2 U M' U2 M2 U2 M' U2
	"""
	return U2(Mi(U2(M2(U2(Mi(U(M2(U(M2(c))))))))))

def Ja_perm(c):
	"""
	R' U L' U2 R U' R' U2 L R U'
	"""
	return Ui(R(L(U2(Ri(Ui(R(U2(Li(U(Ri(c)))))))))))

def Jb_perm(c):
	"""
	L U' R U2 L' U L U2 L' R' U
	"""
	return U(Ri(Li(U2(L(U(Li(U2(R(Ui(L(c)))))))))))

def T_perm(c):
	"""
	R U R' U' R' F R2 U' R' U' R U R' F'
	"""
	return Fi(Ri(U(R(Ui(Ri(Ui(R2(F(Ri(Ui(Ri(U(R(c))))))))))))))

def Ra_perm(c):
	"""
	L U2 L' U2 L F' L' U' L U L F L2 U
	"""
	return U(L2(F(L(U(L(Ui(Li(Fi(L(U2(Li(U2(L(c))))))))))))))

def Rb_perm(c):
	"""
	R' U2 R U2 R' F R U R' U' R' F' R2 U'
	"""
	return Ui(R2(Fi(Ri(Ui(Ri(U(R(F(Ri(U2(R(U2(Ri(c))))))))))))))

def F_perm(c):
	"""
	R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R
	"""
	return R(U(Ri(U(R(Ui(Ri(Ui(R2(F(Ri(Ui(Ri(U(R(Fi(Ui(Ri(c))))))))))))))))))

def V_perm(c):
	"""
	R' U R' d' R' F' R2 U' R' U R' F R F
	"""
	return F(R(F(Ri(U(Ri(Ui(R2(Fi(Ri(di(Ri(U(Ri(c))))))))))))))

def Na_perm(c):
	"""
	z D R' U R2 D' R D U' R' U R2 D' R U' R
	"""
	return R(Ui(R(Di(R2(U(Ri(Ui(D(R(Di(R2(U(Ri(D(z(c))))))))))))))))

def Nb_perm(c):
	"""
	z U' R D' R2 U R' D U' R D' R2 U R' D R'
	"""
	return Ri(D(Ri(U(R2(Di(R(Ui(D(Ri(U(R2(Di(R(Ui(z(c))))))))))))))))

def Y_perm(c):
	"""
	F R U' R' U' R U R' F' R U R' U' R' F R F'
	"""
	return Fi(R(F(Ri(Ui(Ri(U(R(Fi(Ri(U(R(Ui(Ri(Ui(R(F(c)))))))))))))))))

def Ga_perm(c):
	"""
	R2 u R' U R' U' R u' R2 y' R' U R
	"""
	return R(U(Ri(yi(R2(ui(R(Ui(Ri(U(Ri(u(R2(c)))))))))))))

def Gb_perm(c):
	"""
	R' U' R y R2 u R' U R U' R u' R2
	"""
	return R2(ui(R(Ui(R(U(Ri(u(R2(y(R(Ui(Ri(c)))))))))))))

def Gc_perm(c):
	"""
	R2 u' R U' R U R' u R2 y R U' R'
	"""
	return Ri(Ui(R(y(R2(u(Ri(U(R(Ui(R(ui(R2(c)))))))))))))

def Gd_perm(c):
	"""
	R U R' y' R2 u' R U' R' U R' u R2
	"""
	return R2(u(Ri(U(Ri(Ui(R(ui(R2(yi(Ri(U(R(c)))))))))))))

def None_perm(c):
	""
	return c

