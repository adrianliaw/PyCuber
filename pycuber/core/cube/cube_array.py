import numpy as np
from itertools import product
from . import cubie_array as cubie
from .constants import U, L, F, R, B, D, Y


class CubeArray(np.ndarray):

    def __new__(subtype, *args, layers=3, **kwargs):
        if len(args) > 0:
            cube = np.array(args[0])
            if cube.shape == (layers, layers, layers, 6):
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

    def get_face(self, face):
        first, last = 0, self.layers - 1
        if face == U:
            result = np.flipud(np.rot90(self[:, last, :, U]))
        elif face == L:
            result = np.rot90(np.transpose(self[first, :, :, L]))
        elif face == F:
            result = np.rot90(self[:, :, last, F])
        elif face == R:
            result = np.rot90(self[last, :, :, R], 2)
        elif face == B:
            result = np.fliplr(np.rot90(self[:, :, first, B]))
        elif face == D:
            result = np.rot90(self[:, first, :, D])
        return result.view(np.ndarray)

    # def get_face_colours(self):
    #     return self[
    #         [1, 0, 1, 2, 1, 1],
    #         [2, 1, 1, 1, 1, 0],
    #         [1, 1, 2, 1, 0, 1],
    #         [U, L, F, R, B, D],
    #     ].view(np.ndarray)
