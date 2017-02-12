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

        for tp in class_mapping:
            if tp in inputs:
                i = inputs.index(tp)
                if not isinstance(args[i], class_mapping[tp]):
                    args[i] = class_mapping[tp](args[i])

        result = method_func(self, *args)
        if output in class_mapping:
            result = class_mapping[output](result)
        return result

    return func


class FormulaMeta(ABCMeta):

    def __new__(cls, name, bases, namespace, **kwargs):
        base = bases[0]
        for method, spec in list(namespace.items()):
            if isinstance(spec, tuple):
                if method in base.__abstractmethods__ or method not in dir(base):
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
    index = ([MOVE], SKIP)
    count = ([MOVE], SKIP)
    insert = ([SKIP, MOVE], SKIP)
    extend = ([FORMULA], SKIP)
    copy = ([], FORMULA)
    ### TODO: __init__, __setitem__, __getitem__, __reversed__, reverse

class GenericCubicFormula(BaseFormula):
    __move__ = GenericCubicMove

class Formula(BaseFormula):
    __move__ = Move
