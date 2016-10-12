import numpy as np
from itertools import product
from . import cubie_array as cubie
from .constants import U, L, F, R, B, D, Y


class CubeArray(np.ndarray):

    def __new__(subtype, *args, **kwargs):
        if len(args) > 0:
            cube = np.array(args[0])
            if cube.shape == (3, 3, 3, 6):
                return cube.view(CubeArray)

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
        self[selector] = cubie.rotate_on(axis, self[selector], k)
        if axis == Y:
            k *= -1
        self[selector] = np.rot90(self[selector], k)

    def get_face(self, face):
        if face == U:
            result = np.rot90(self[:, 2, :, U])
        elif face == L:
            result = np.rot90(self[0, :, :, L], 2)
        elif face == F:
            result = np.rot90(self[:, :, 0, F])
        elif face == R:
            result = np.flipud(self[2, :, :, R])
        elif face == B:
            result = np.fliplr(np.rot90(self[:, :, 2, B]))
        elif face == D:
            result = np.transpose(self[:, 0, :, D])
        return result.view(np.ndarray)

    def get_face_colours(self):
        return self[
            [1, 0, 1, 2, 1, 1],
            [2, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 2, 1],
            [0, 1, 2, 3, 4, 5],
        ].view(np.ndarray)
