from .cube_array import CubeArray
from .cube_abc import CubeABC
from .constants import X, Y, Z
from ..formula import Step


rotation_parameters = {
    Step("L"): (X, 0, -1),
    Step("M"): (X, 1, -1),
    Step("R"): (X, 2, 1),

    Step("D"): (Y, 0, -1),
    Step("E"): (Y, 1, -1),
    Step("U"): (Y, 2, 1),

    Step("F"): (Z, 0, -1),
    Step("S"): (Z, 1, -1),
    Step("B"): (Z, 2, 1),
}

combinations = {
    Step("l"): [Step("L"), Step("M")],
    Step("r"): [Step("M'"), Step("R")],
    Step("x"): [Step("L'"), Step("M'"), Step("R")],

    Step("d"): [Step("D"), Step("E")],
    Step("u"): [Step("E'"), Step("U")],
    Step("y"): [Step("D'"), Step("E'"), Step("U")],

    Step("f"): [Step("F"), Step("S")],
    Step("b"): [Step("S'"), Step("B")],
    Step("z"): [Step("F"), Step("S"), Step("B'")],
}


class CubieCube(CubeABC):

    def __init__(self):
        super().__init__()
        self.__data = CubeArray()

    def do_step(self, step):
        if step.face.isupper():
            axis, layer, k = rotation_parameters[Step(step.face)]
            if step.is_counter_clockwise:
                k *= -1
            elif step.is_180:
                k *= 2
            self.__data.twist(axis, layer, k)
        else:
            separated = combinations[Step(step.face)]
            k = -1 * step.is_counter_clockwise + \
                2 * step.is_180 + \
                1 * step.is_clockwise
            for individual_step in separated:
                self.do_step(individual_step * k)
        return self

    def do_formula(self, formula):
        for step in formula:
            self.do_step(step)
        return self
