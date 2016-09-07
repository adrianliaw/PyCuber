import numpy as np
from itertools import product
from . import cubie
from .constants import U, L, F, R, B, D, Y


class Cube(np.ndarray):

    def __new__(subtype, *args, **kwargs):
        if len(args) > 0:
            cube = np.array(args[0])
            if cube.shape == (3, 3, 3, 6):
                return cube.view(Cube)

        cube = np.ndarray.__new__(subtype, (3, 3, 3, 6), "int8")
        poses = zip(
            product((L, None, R), (D, None, U), (F, None, B)),
            product(*[range(3)]*3)
        )
        for faces, (x, y, z) in poses:
            faces = [[f, f] for f in faces if f is not None]
            cube[x, y, z] = cubie.make_cubie(faces)

        return cube

    def twist(self, axis, layer, k=1):
        selector = [slice(0, 3), slice(0, 3), slice(0, 3)]
        selector[axis] = layer
        if axis == Y:
            k *= -1
        self[selector] = np.rot90(self[selector], k)
        self[selector] = cubie.rotate_on(axis, self[selector], k)

    def get_face_colours(self):
        return self[
            [1, 0, 1, 2, 1, 1],
            [2, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 2, 1],
            [0, 1, 2, 3, 4, 5],
        ].view(np.ndarray)
