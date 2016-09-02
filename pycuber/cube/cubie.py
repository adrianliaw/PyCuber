import numpy as np


U, L, F, R, B, D = range(6)

ROT = np.zeros((3, 6, 6), int)

X, Y, Z = range(3)

rotation_patterns = np.array([
    [[F, U], [U, B], [B, D], [D, F], [L, L], [R, R]],
    [[L, B], [B, R], [R, F], [F, L], [U, U], [D, D]],
    [[L, U], [U, R], [R, D], [D, L], [F, F], [B, B]],
])

for i, pattern in enumerate(rotation_patterns):
    ROT[i][pattern[:, 0], pattern[:, 1]] = 1


class Cubie(np.ndarray):

    def __new__(subtype, side_colour_map, **kwargs):
        if isinstance(side_colour_map, Cubie):
            return side_colour_map

        side_colour_map = np.array(side_colour_map)

        if side_colour_map.shape == (6,):
            return side_colour_map

        ret = np.ndarray.__new__(subtype, (6, ), "int8", **kwargs)
        ret.fill(-1)
        ret[side_colour_map[:, 0]] = side_colour_map[:, 1]

        return ret

    def rotate_on_X(self, n=1):
        ret = self
        for i in range(n % 4):
            ret = ret.dot(ROT[X])
        return ret


if __name__ == "__main__":
    # mapping = np.array([[0, 0], [1, 1], [2, 2]])
    cubie = Cubie([[0, 0], [1, 1], [2, 2]])
    print(cubie.rotate_on_X())
    # print(cubie)
    # print(Cubie(cubie))
    # print(Cubie(np.array([0, 1, 2, -1, -1, -1])))
    # print(Cubie([0, 1, 2, -1, -1, -1]))
