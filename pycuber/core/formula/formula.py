from collections.abc import MutableSequence
from abc import ABCMeta
from functools import wraps

from .move import GenericCubicMove, Move


SKIP = 0
MOVE = 1
FORMULA = 2


def formula_method_wrapper(method_func, spec):

    @wraps(method_func)
    def func(self, *args):
        inputs, output = spec
        class_mapping = {MOVE: self.__move__, FORMULA: self.__class__}
        args = list(args)

        for i, tp in enumerate(inputs):
            if tp in class_mapping and \
                    not isinstance(args[i], class_mapping[tp]):
                args[i] = class_mapping[tp](args[i])
                if tp == FORMULA:
                    args[i] = list(args[i])

        result = method_func(self._data, *args)
        if output in class_mapping:
            result = class_mapping[output](result)
        return result

    return func


class FormulaMeta(ABCMeta):

    def __new__(cls, name, bases, namespace, **kwargs):
        base = bases[0]
        for method, spec in list(namespace.items()):
            if isinstance(spec, tuple):
                if method in base.__abstractmethods__ or \
                        method not in dir(base):
                    method_func = getattr(list, method)
                else:
                    method_func = getattr(base, method)
                namespace[method] = formula_method_wrapper(method_func, spec)
        result = type.__new__(cls, name, bases, namespace)
        return result


class BaseFormula(MutableSequence, metaclass=FormulaMeta):
    __delitem__ = ([SKIP], SKIP)
    __len__ = ([], SKIP)
    __contains__ = ([MOVE], SKIP)
    __mul__ = ([SKIP], FORMULA)
    __add__ = ([FORMULA], FORMULA)
    index = ([MOVE], SKIP)
    count = ([MOVE], SKIP)
    insert = ([SKIP, MOVE], SKIP)
    extend = ([FORMULA], SKIP)
    copy = ([], FORMULA)

    def __init__(self, formula):
        if isinstance(formula, str):
            formula = formula.split()
        elif isinstance(formula, self.__move__):
            formula = [formula]
        self._data = [self.__move__(m) for m in formula]

    def __repr__(self):
        return " ".join(map(repr, self._data))

    def __getitem__(self, index):
        item = self._data[index]
        if isinstance(index, slice):
            return self.__class__(item)
        else:
            return self.__move__(item)

    def __setitem__(self, index, item):
        if item is None:
            del self._data[index]
        elif isinstance(index, slice):
            self._data[index] = self.__class__(item)
        else:
            self._data[index] = self.__move__(item)

    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i].inverse()

    def reverse(self):
        n = len(self)
        for i in range(n // 2):
            self[i], self[n-i-1] = self[n-i-1].inverse(), self[i].inverse()
        if n % 2 == 1:
            self[n // 2] = self[n // 2].inverse()


class GenericCubicFormula(BaseFormula):
    __move__ = GenericCubicMove


class Formula(BaseFormula):
    __move__ = Move
