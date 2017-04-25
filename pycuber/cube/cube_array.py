import numpy as np
from itertools import product
from . import cubie_array as cubie
from .constants import U, L, F, R, B, D, Y


class CubeArray(np.ndarray):

    def __new__(subtype, *args, layers=3, **kwargs):
        if len(args) > 0:
            cube = np.array(args[0])
            assert cube.shape[0] == cube.shape[1] == cube.shape[2]
            assert cube.shape[3] == 6
            layers = cube.shape[0]
            return cube.view(CubeArray)

        cube = np.ndarray.__new__(subtype, (layers, layers, layers, 6), "int8")
        cube.layers = layers

        mid_layers = [None] * (layers - 2)
        poses = zip(
            product((L, *mid_layers, R),
                    (D, *mid_layers, U),
                    (B, *mid_layers, F)),
            product(*[range(layers)] * 3)
        )

        for faces, (x, y, z) in poses:
            faces = [[f, f] for f in faces if f is not None]
            cube[x, y, z] = cubie.make_cubie(faces)

        return cube

    def twist(self, axis, layer, k=1):
        selector = [slice(0, self.layers)] * 3
        selector[axis] = layer
        self[selector] = cubie.rotate_on(axis, self[selector], k)
        if axis != Y:
            k *= -1
        self[selector] = np.rot90(self[selector], k)

    def get_face(self, face, transform=True):
        first, last = 0, self.layers - 1

        if face == L:
            result = self[first, :, :, L]
            if transform:
                result = np.rot90(np.transpose(result))
        elif face == R:
            result = self[last, :, :, R]
            if transform:
                result = np.rot90(result, 2)

        elif face == D:
            result = self[:, first, :, D]
            if transform:
                result = np.rot90(result)
        elif face == U:
            result = self[:, last, :, U]
            if transform:
                result = np.flipud(np.rot90(result))

        elif face == B:
            result = self[:, :, first, B]
            if transform:
                result = np.fliplr(np.rot90(result))
        elif face == F:
            result = self[:, :, last, F]
            if transform:
                result = np.rot90(result)

        return result.view(np.ndarray)
