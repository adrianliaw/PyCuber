from collections.abc import MutableSequence
from abc import ABCMeta
from functools import wraps, total_ordering

from .move import GenericCubicMove, Move


SKIP = 0
MOVE = 1
FORMULA = 2


class FormulaMeta(ABCMeta):

    @staticmethod
    def formula_method_wrapper(method_func, spec):

        @wraps(method_func)
        def func(self, *args):
            inputs, output = spec
            class_mapping = {MOVE: self._move, FORMULA: self.__class__}
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

    def __new__(cls, name, bases, namespace, **kwargs):
        base = bases[0]
        for method, spec in list(namespace.items()):
            if isinstance(spec, tuple):
                if method in base.__abstractmethods__ or \
                        getattr(base, method, None) is None:
                    method_f = getattr(list, method)
                else:
                    method_f = getattr(base, method)
                new_method = FormulaMeta.formula_method_wrapper(method_f, spec)
                namespace[method] = new_method
        return super().__new__(cls, name, bases, namespace)


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
        elif isinstance(formula, self._move):
            formula = [formula]
        self._data = [self._move(m) for m in formula]

    def __repr__(self):
        return " ".join(map(repr, self._data))

    def __getitem__(self, index):
        item = self._data[index]
        if isinstance(index, slice):
            return self.__class__(item)
        else:
            return self._move(item)

    def __setitem__(self, index, item):
        if item is None:
            del self._data[index]
        elif isinstance(index, slice):
            self._data[index] = self.__class__(item)
        else:
            self._data[index] = self._move(item)

    def __eq__(self, formula):
        return len(self) == len(self.__class__(formula))

    def __lt__(self, formula):
        return len(self) < len(self.__class__(formula))

    def __or__(self, formula):
        return self._data == self.__class__(formula)._data

    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i].inverse()

    def reverse(self):
        n = len(self)
        for i in range(n // 2 + 1):
            self[i], self[n-i-1] = self[n-i-1].inverse(), self[i].inverse()


class GenericCubicFormula(BaseFormula):
    _move = GenericCubicMove


class Formula(BaseFormula):
    _move = Move
