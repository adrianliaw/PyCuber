from collections.abc import MutableSequence
from abc import ABCMeta
from functools import wraps, total_ordering


SKIP = "SKIP"
MOVE = "MOVE"
FORMULA = "FORMULA"

# This is for mirroring
STAYS_WHEN_MIRROR = {
    "LR": ["x", "M"],
    "UD": ["y", "E"],
    "FB": ["z", "S"],
}


class FormulaMeta(ABCMeta):

    def make_method(method_func, spec):
        inputs, output = spec

        @wraps(method_func)
        def func(self, *args):
            class_mapping = {MOVE: self._move,
                             FORMULA: self.__class__,
                             SKIP: lambda x: x}

            args = [class_mapping[tp](arg)
                    for tp, arg in zip(inputs, args)]

            args = [list(arg) if tp == FORMULA else arg
                    for tp, arg in zip(inputs, args)]

            return class_mapping[output](method_func(self._data, *args))

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
                new_method = FormulaMeta.make_method(method_f, spec)
                namespace[method] = new_method
        return super().__new__(cls, name, bases, namespace)


@total_ordering
class BaseFormula(MutableSequence, metaclass=FormulaMeta):
    __delitem__ = ([SKIP], SKIP)
    __len__ = ([], SKIP)
    __mul__ = ([SKIP], FORMULA)
    __add__ = ([FORMULA], FORMULA)
    insert = ([SKIP, MOVE], SKIP)
    copy = ([], FORMULA)

    def __init__(self, formula=""):
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

    def equals(self, formula):
        return self._data == self.__class__(formula)._data

    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i].inverse()

    def reverse(self):
        n = len(self)
        for i in range(n // 2 + 1):
            self[i], self[n-i-1] = self[n-i-1].inverse(), self[i].inverse()

    def mirror(self, on="LR"):
        assert on in ["LR", "RL", "UD", "DU", "FB", "BF"], \
            """"on" parameter must be one of LR, UD or FB"""

        if on in ["RL", "DU", "BF"]:
            on = on[::-1]
        stays = STAYS_WHEN_MIRROR[on]

        for i in range(len(self)):
            move = self[i]

            if move.symbol.upper() in on:
                new_symbol = on[1 - on.index(move.symbol.upper())]
                if move.symbol.islower():
                    new_symbol = new_symbol.lower()
                move = move.with_symbol(new_symbol)

            if move.symbol not in stays:
                move = move.inverse()
            self[i] = move
