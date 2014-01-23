def color_convert(l):
	"""
	0 : red
	1 : yellow
	2 : green
	3 : white
	4 : orange
	5 : blue
	(6 : unknown)
	"""
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