import numpy as np
from itertools import product
from . import cubie


U, L, F, R, B, D = range(6)
X, Y, Z = range(3)


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
        self[selector] = np.rot90(self[selector], k)
        self[selector] = cubie.rotate_on(axis, self[selector], k)


if __name__ == "__main__":
    cube = Cube()
    print(cube)
    cube.twist(X, 0)
    print(cube)
