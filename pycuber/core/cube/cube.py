from .cube_array import CubeArray
from .cube_abc import CubeABC


class Cube(CubeABC):

    def __init__(self):
        super().__init__()
        self.__data = CubeArray()

    def do_step(self, step):
        pass

    def do_formula(self, formula):
        for step in formula:
            self.do_step(step)
        return self
