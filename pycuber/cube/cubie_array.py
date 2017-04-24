import numpy as np
from .constants import U, L, F, R, B, D, \
                       X, Y, Z


ROT = np.zeros((3, 6, 6), int)

rotation_patterns = np.array([
    [[F, U], [U, B], [B, D], [D, F], [L, L], [R, R]],
    [[L, B], [B, R], [R, F], [F, L], [U, U], [D, D]],
    [[L, U], [U, R], [R, D], [D, L], [F, F], [B, B]],
])

for axis, pattern in enumerate(rotation_patterns):
    ROT[axis][pattern[:, 0], pattern[:, 1]] = 1


def make_cubie(side_colour_map, **kwargs):
    side_colour_map = np.array(side_colour_map)

    cubie = np.ndarray((6,), "int8", **kwargs)

    if side_colour_map.shape == (6,):
        cubie[:] = side_colour_map
    else:
        cubie.fill(-1)
        if side_colour_map.shape != (0,):
            cubie[side_colour_map[:, 0]] = side_colour_map[:, 1]

    assert_is_cubie(cubie)

    return cubie


def assert_is_cubie(cubie):
    assert cubie.shape == (6,)
    assert (cubie != -1).sum() <= 3

    cubie_values = cubie[cubie != -1]
    assert np.in1d(cubie_values, np.arange(6)).all()
    assert np.unique(cubie_values).shape == cubie_values.shape


def is_valid_cubie(cubie):
    if cubie.shape != (6,) or (cubie != -1).sum() > 3:
        return False

    cubie_values = cubie[cubie != -1]
    if np.in1d(cubie_values, np.arange(6)).any():
        return False
    if np.unique(cubie_values).shape != cubie_values.shape:
        return False

    return True


def rotate_on(axis, original, k=1):
    assert axis in (X, Y, Z)
    ret = original
    for i in range(k % 4):
        ret = ret.dot(ROT[axis])
    return ret
