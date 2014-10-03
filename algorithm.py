"""

This module is to represent the Rubik's Cube algorithms.

"""

from functools import wraps
import sys


class Step(object):

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

    def set_face(self, new_face):
        """
        Reset the face of the action.
        ex: r = Step("R2")
            r.set_face("U")
            r => U2
        """
        if new_face in list("LUFDRBlufdrbMSExyz"):
            self.face = new_face
            self.name = new_face + self.name[1:]
        else:
            raise ValueError("Invalid name")


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
        super(Algo, self).__init__(sequence)

    def __repr__(self):
        return " ".join(map(lambda x: x.name, self))

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Algo(list.__getitem__(self, index))
        return list.__getitem__(self, index)

    def __setitem__(self, index, item):
        if item == None:
            del self[index]
            return
        if isinstance(index, slice):
            list.__setitem__(self, index, Algo(item))
        else:
            list.__setitem__(self, index, Step(item))

    def __setattr__(self, name, value):
        if name in dir(self) and name not in ["sort", "extend"]:
            raise AttributeError("'Algo' object attribute '{}' is read-only".format(name))
        else:
            raise AttributeError("'Algo' object has no attribute '{}'".format(name))

    def _stepify(func):
        """Makes last input a Step object."""
        @wraps(eval("list.{0}".format(func.__name__)), assigned=("__name__", "__doc__"))
        def _func(*args):
            args = list(args[:-1]) + [Step(args[-1])]
            return eval("list.{0}(*args)".format(func.__name__))
        return _func

    def _algify_input(func):
        """Makes last input a Algo object."""
        def _func(*args):
            args = list(args[:-1]) + [Algo(args[-1])]
            return eval("list.{0}(*args)".format(func.__name__))
        _func.__doc__ = eval("list.{0}".format(func.__name__)).__doc__
        _func.__name__ = func.__name__ + " "
        return _func

    def _algify_output(func):
        """Makes output a Algo object."""
        @wraps(eval("list.{0}".format(func.__name__)), assigned=("__name__", "__doc__"))
        def _func(*args):
            if " " in func.__name__:
                return Algo(func(*args))
            return Algo(eval("list.{0}(*args)".format(func.__name__)))
        return _func

    def _delattr(func):
        """Raise error when calling some not needed method."""
        def _func(*args):
            raise AttributeError("'Algo' object has no attribute '{0}'".format(func.__name__))
        return _func

    @_algify_output
    @_algify_input
    def __add__(self, another): pass
    if sys.version_info.major == 2:
        @_algify_output
        def __getslice__(self, i, j): pass
        @_algify_input
        def __setslice__(self, i, j, value): pass
    @_algify_output
    def __mul__(self, i): pass
    def __iadd__(self, another):
        return self.__add__(another)
    
    def __eq__(self, another): return len(self) == len(another)
    def __lt__(self, another): return len(self) < len(another)
    def __gt__(self, another): return len(self) > len(another)
    def __ge__(self, another): return len(self) >= len(another)
    def __le__(self, another): return len(self) <= len(another)
    def __ne__(self, another): return len(self) != len(another)

    @_stepify
    def __contains__(self, value): pass
    @_stepify
    def append(self, another): pass
    @_stepify
    def count(self, value): pass
    @_stepify
    def index(self, start, stop): pass
    @_stepify
    def insert(self, index, obj): pass
    @_stepify
    def remove(self, value): pass

    @_delattr
    def extend(*args): pass
    @_delattr
    def sort(*args): pass

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
    
    def clear(self):
        """L.clear() -> None -- remove all items from L"""
        self[:] = ""

    def copy(self):
        """L.copy() -> Algo -- a shallow copy of L"""
        return Algo(self)

    def _optimize_wide_actions(self):
        """
        Reduce the wide actions (double layers)
        ex: R u -> R D y
            L M -> L L' R x'
        """
        pattern = {
            "r": "L x", 
            "l": "R x'", 
            "u": "D y", 
            "d": "U y'", 
            "f": "B z", 
            "b": "F z'", 
            "M": "R L' x'", 
            "S": "F' B z", 
            "E": "U D' y'"
        }
        _self = Algo(self)
        index = 0
        for step in _self:
            if step.name[0] in pattern:
                replacement = Algo(pattern[step.name[0]])
                if step.name[1:] != "":
                    for i in range(len(replacement)):
                        if step.name[1] == "'":
                            replacement[i] *= -1
                        else:
                            replacement[i] *= 2
                self[index:index+1] = replacement
                index += len(replacement)
            else:
                index += 1
    
    def _optimize_rotations(self):
        """
        Reduce the rotations (whole cube rotations).
        ex: x R U   -> R F
            y' L' F -> B' L
        """
        pattern = {
            "x": "UFDB", 
            "y": "FRBL", 
            "z": "ULDR"
        }
        _self = Algo(self)
        self.clear()
        for i in range(len(_self)-1, -1, -1):
            if _self[i].face not in pattern:
                self.insert(0, _self[i])
            else:
                cr_pattern = pattern[_self[i].face]
                if _self[i].is_inverse:
                    cr_pattern = cr_pattern[::-1]
                for j in range(len(self)):
                    if self[j].face in cr_pattern:
                        if _self[i].is_180:
                            self[j].set_face(cr_pattern[(cr_pattern.index(self[j].face) + 2) % 4])
                        else:
                            self[j].set_face(cr_pattern[(cr_pattern.index(self[j].face) + 1) % 4])

    def _optimize_same_steps(self):
        """
        Reduce repeated steps.
        ex: R R2 U U' -> R'
            L' R L2   -> L R
        """
        opposite = {"U":"D", "L":"R", "F":"B", "D":"U", "R":"L", "B":"F"}
        if len(self) < 2:
            return
        elif len(self) == 2:
            if self[0].face == self[1].face:
                if self[0] + self[1] == None:
                    self[0] += self[1]
                    del self[0]
                else:
                    self[0] += self[1]
                    del self[1]
        else:
            flag = True
            if self[0].face == self[2].face and opposite[self[0].face] == self[1].face:
                if self[0] + self[2] == None:
                    self[0] += self[2]
                    del self[1]
                    flag = False
                else:
                    self[0] += self[2]
                    del self[2]
            if self[0].face == self[1].face:
                if self[0] + self[1] == None:
                    self[0] += self[1]
                    del self[0]
                    flag = False
                else:
                    self[0] += self[1]
                    del self[1]
            rhs = self[flag:]
            rhs._optimize_same_steps()
            self[flag:] = rhs

    del _stepify, _algify_input, _algify_output, _delattr


