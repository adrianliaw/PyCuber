"""

This module is to represent the Rubik's Cube algorithms.

"""

from functools import wraps


class Step:

    """
    Representing a Rubik's Cube action.
    """

    def __init__(self, name):
        if isinstance(name, Step):
            name = name.name
        try:
            if name[0] in "LUFDRBMSElufdrbxyz":
                if name[1:] in ["", "'", "2"]:
                    self.name = name
                    self.face = name[0]
                    self.is_inverse = (name[1:] == "'")
                    self.is_standard = (name[1:] == "")
                    self.is_180 = (name[1:] == "2")
                    return
            raise IndexError
        except IndexError:
            raise ValueError("Invalid action name.")

    def __repr__(self):
        return self.name

    def __eq__(self, another):
        if type(another) == str:
            return self.name == another
        elif isinstance(another, Step):
            return self.name == another.name
        else:
            return False

    def __ne__(self, another):
        return not self.__eq__(another)

    def __add__(self, another):
        """
        Step("U") + Step("U2") => Step("U'")
        Step("R2") + Step("R2") => None
        """
        if self.face == another.face:
            status = ((self.is_standard    + self.is_180*2    + self.is_inverse*3) + \
                      (another.is_standard + another.is_180*2 + another.is_inverse*3)) % 4
            try:
                return Step(self.face + [None, "", "2", "'"][status])
            except TypeError: return None
        raise ValueError("Should be the same side action.")

    def __mul__(self, i):
        i = i % 4
        result = Step(self.name)
        for j in range(i-1):
            result += Step(self.name)
        return result

    def set(self, new):
        """Reset the action name."""
        self.__init__(new)

    def inverse(self):
        """Inverse the action."""
        new = self.name[0] + ("" if "'" in self.name else "'" if not self.name[1:] else "2")
        self.__init__(new)



class Algo(list):

    """
    Representing a Rubik's Cube algorithm.
    | Algo(["R", "U", "R'", "U'"])
    | Algo([Step("R"), Step("U"), Step("R'"), Step("U'")])
    | Algo("R U R' U'")
    | -> Algo object (extends list)
    """

    def __init__(self, sequence=[]):
        if type(sequence) == str:
            sequence = sequence.split()
        for i in range(len(sequence)):
            sequence[i] = Step(sequence[i])
        list.__init__(self, sequence)

    def __repr__(self):
        return " ".join(map(lambda x: x.name, self))

    def __getitem__(self, item):
        if isinstance(item, slice):
            return Algo(list.__getitem__(self, item))
        return list.__getitem__(self, item)

    def __stepify(func):
        """Makes last input a Step object."""
        @wraps(func)
        def _func(*args):
            args = list(args[:-1]) + [Step(args[-1])]
            return eval("list.{0}(*args)".format(func.__name__))
        return _func

    def __algify_input(func):
        """Makes last input a Algo object."""
        def _func(*args):
            args = list(args[:-1]) + [Algo(args[-1])]
            return eval("list.{0}(*args)".format(func.__name__))
        _func.__doc__ = func.__doc__
        _func.__name__ = func.__name__ + " "
        return _func

    def __algify_output(func):
        """Makes output a Algo object."""
        @wraps(func)
        def _func(*args):
            if " " in func.__name__:
                return Algo(func(*args))
            return Algo(eval("list.{0}(*args)".format(func.__name__)))
        return _func

    def __delattr(func):
        """Raise error when calling some not needed method."""
        def _func(*args):
            raise AttributeError("'Algo' object has no attribute '{0}'".format(func.__name__))
        return _func

    @__algify_output
    @__algify_input
    def __add__(self, another): pass
    @__algify_output
    def __getslice__(self, i, j): pass
    @__algify_input
    def __setslice__(self, i, j, value): pass
    @__algify_output
    def __mul__(self, i): pass
    def __iadd__(self, another):
        return self.__add__(another)
    
    def __eq__(self, another): return len(self) == len(another)
    def __lt__(self, another): return len(self) < len(another)
    def __gt__(self, another): return len(self) > len(another)
    def __ge__(self, another): return len(self) >= len(another)
    def __le__(self, another): return len(self) <= len(another)
    def __ne__(self, another): return len(self) != len(another)

    @__stepify
    def __setitem__(self, index, new): pass
    @__stepify
    def __contains__(self, value): pass
    @__stepify
    def append(self, another): pass
    @__stepify
    def count(self, value): pass
    @__stepify
    def index(self, start, stop): pass
    @__stepify
    def insert(self, index, obj): pass
    @__stepify
    def remove(self, value): pass

    @__delattr
    def extend(*args): pass
    @__delattr
    def sort(*args): pass
    @__delattr
    def __dict__(*args): pass

    def __or__(self, another):
        """Algo(...) | Algo(...) => Two algorithms are fully same."""
        try:
            if type(another) == str:
                another = another.split()
            for i in range(len(self)):
                if self[i] != another[i]:
                    return False
            return True
        except:
            return False
    
    def reverse(self):
        """
        Reverse this algorithm
        Algo([R U R' U']) => Algo([U R U' R'])
        """
        if len(self) == 0: return
        for i in range(int((len(self)+1)/2)):
            self[i].inverse()
            if i != len(self)-i-1:
                self[-i-1].inverse()
            self[i], self[-i-1] = self[-i-1], self[i]

