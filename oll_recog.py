
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

def O06_recog(c): return side_recog(c, "110110001000")

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

def O26_recog(c): return side_recog(c, "000100100100")

def O27_recog(c): return side_recog(c, "001001000001")

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



