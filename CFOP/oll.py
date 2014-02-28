"""
Nothing fancy here, all OLL algorithms.

Algorithms from: http://www.cubewhiz.com/oll.php

"""

import _import
from cube import *

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
	r' R U R U R' U' r x R2 U R U'
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


