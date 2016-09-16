import abc


class CubeABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_step(self, step):
        return NotImplemented

    @abc.abstractmethod
    def do_formula(self, formula):
        return NotImplemented

    def __call__(self, formula):
        return self.do_formula(formula)
