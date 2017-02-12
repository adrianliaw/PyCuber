from collections.abc import MutableSequence
from abc import ABCMeta

from .move import GenericCubicMove, Move


SKIP = 0
MOVE = 1
FORMULA = 2

class FormulaMeta(ABCMeta):

    def __new__(cls, name, bases, namespace, **kwargs):
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
