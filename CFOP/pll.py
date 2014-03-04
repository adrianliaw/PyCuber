"""
Nothing fancy here, all PLL algorithms.

Algorithms from: http://www.cubewhiz.com/pll.php

"""

import _import
from cube import *


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

