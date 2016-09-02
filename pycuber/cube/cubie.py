import numpy as np


class Cubie(np.ndarray):

    def __new__(subtype, side_colour_map, **kwargs):
        if isinstance(side_colour_map, Cubie):
            return side_colour_map

        if not isinstance(side_colour_map, np.ndarray):
            side_colour_map = np.array(side_colour_map)

        if side_colour_map.shape == (6,):
            return side_colour_map

        ret = np.ndarray.__new__(subtype, (6, ), "int8", **kwargs)
        ret.fill(-1)
        ret[side_colour_map[:, 0]] = side_colour_map[:, 1]

        return ret


if __name__ == "__main__":
    mapping = np.array([[0, 0], [1, 1], [2, 2]])
    cubie = Cubie(mapping)
    print(cubie)
    print(Cubie(cubie))
    print(Cubie(np.array([0, 1, 2, -1, -1, -1])))
    print(Cubie([0, 1, 2, -1, -1, -1]))
