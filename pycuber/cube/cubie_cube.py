import numpy as np
from colorama import Back
from .cube_array import CubeArray
from .cube_abc import CubeABC
from .constants import X, Y, Z, U, L, F, R, B, D
from .components import Face
from ..formula import GenericCubicFormula


rotations_on_axis = {
    X: ("L", "M", "R"),
    Y: ("D", "E", "U"),
    Z: ("F", "S", "B"),
}


class CubieCube(object):

    _formula_class = GenericCubicFormula

    def __init__(self, cube=None, layers=3):
        super().__init__()
        if isinstance(cube, CubieCube):
            cube = cube._copy_data()
        elif isinstance(cube, list):
            cube = np.array(cube)

        if isinstance(cube, np.ndarray):
            self.__data = CubeArray(cube)
        else:
            self.__data = CubeArray(layers=layers)

        self.layers = self.__data.layers

    def __repr__(self):
        faces = {f: repr(self.get_face(f)) for f in [U, L, F, R, B, D]}
        s = ""
        for row in faces[U].split("\n"):
            s += "  " * self.layers + row + "\n"
        for zipped_rows in zip(*(faces[f].split("\n") for f in [L, F, R, B])):
            s += "".join(zipped_rows) + Back.RESET + "\n"
        for row in faces[D].split("\n"):
            s += "  " * self.layers + row + "\n"
        return s

    def __call__(self, formula):
        self.do_formula(formula)
        return self

    def do_move(self, move):
        if not isinstance(move, self._formula_class._move):
            move = self._formula_class._move(move)
        if not move.is_rotate():

            for axis, (head, mid, bottom) in rotations_on_axis.items():
                if head == move.symbol.upper():
                    layer, k, increment = 0, -1, 1
                    break
                elif mid == move.symbol.upper():
                    layer, k, increment = self.layers // 2, 1, 0
                    if mid == "S":
                        k = -1
                    break
                elif bottom == move.symbol.upper():
                    layer, k, increment = self.layers - 1, 1, -1
                    break

            k *= move.sign

            if move.is_single():
                self.__data.twist(axis, layer + increment * (move.level-1), k)
            else:
                for i in range(move.level):
                    self.__data.twist(axis, layer + increment * i, k)

        else:
            axis = {"x": X, "y": Y, "z": Z}[move.symbol]
            for i in range(self.layers):
                self.__data.twist(axis, i, move.sign)

    def do_formula(self, formula):
        if not isinstance(formula, self._formula_class):
            formula = self._formula_class(formula)
        for move in formula:
            self.do_move(move)

    def get_face(self, face):
        if isinstance(face, str):
            face = ["U", "L", "F", "R", "B", "D"].index(face)
        return Face(self.__data.get_face(face), face)

    def _get_cubie(self, face_indexed_position):
        selector = [1, 1, 1]
        for face in face_indexed_position:
            if face in (L, R):
                selector[X] = [L, None, R].index(face)
            elif face in (D, U):
                selector[Y] = [D, None, U].index(face)
            elif face in (F, B):
                selector[Z] = [F, None, B].index(face)
        return self.__data[tuple(selector)].view(np.ndarray)

    def _copy_data(self):
        return self.__data.copy()


CubeABC.register(CubieCube)
