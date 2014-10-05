"""

This module is to represent the Rubik's Cube algorithms.

"""

from functools import wraps
import sys, random


class Step(object):

    """
    Representing a Rubik's Cube action.
    
    >>> r = Step("R")
    >>> r
    R

    >>> u_prime = Step("U'")
    >>> u_prime
    U'

    You can check if it's clockwise (ex: U), counter-clockwise (ex: U'), or 180 degrees (ex: U2)
    >>> r.is_standard
    True
    >>> r.is_inverse
    False
    >>> r.is_180
    False

    >>> u_prime.is_standard
    False
    >>> u_prime.is_inverse
    True
    >>> u_prime.is_180
    False

    Or you can inverse action like this:
    >>> s = Step("U'")
    >>> s.inverse()
    >>> s
    U

    You can reset the Step like this:
    >>> s.set("R2")
    >>> s
    R2

    Or just set the face of Step.
    >>> s.set_face("L")
    >>> s
    L2

    You can add two Steps together!
    >>> s + Step("L'")
    L
    >>> s + Step("L2")
    None

    And also multiply by numbers!
    >>> s.set("L")
    >>> s * 2
    L2
    >>> s * 5
    L
    """

    def __init__(self, name):
        """
        Initialize a Step object.

        >>> s = Step("R2")
        >>> s
        R2

        >>> s.__init__("L'")
        >>> s
        L'

        >>> s = Step("W'")
        ValueError: Invalid action name.
        """
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
        """
        Representing a Step, just print out the name.

        >>> s = Step("L'")

        >>> s.__repr__()
        "L'"
        """
        return self.name

    def __eq__(self, another):
        """
        Check if two Steps are the same.

        >>> s = Step("U'")
        >>> p = Step("U'")

        >>> s == p
        True

        >>> p = Step("U2")
        >>> s == p
        False

        >>> s == "U'"
        True

        >>> s == "U2"
        False
        """
        if type(another) == str:
            return self.name == another
        elif isinstance(another, Step):
            return self.name == another.name
        else:
            return False

    def __ne__(self, another):
        """
        Check if two Steps are different.

        >>> s = Step("R")
        >>> p = Step("R")
        >>> s != p
        False

        >>> p = Step("U'")
        >>> s != p
        True

        >>> s != "R'"
        True

        >>> s != "R"
        False
        """
        return not self.__eq__(another)

    def __add__(self, another):
        """
        Adding two Steps, these two have to be the same face action.

        >>> s = Step("R")
        >>> p = Step("R2")
        >>> s + p
        R'

        >>> s + "R'"
        None

        >>> s + "L"
        ValueError: Should be the same side action.
        """
        if type(another) == str:
            another = Step(another)
        if self.face == another.face:
            status = ((self.is_standard    + self.is_180*2    + self.is_inverse*3) + \
                      (another.is_standard + another.is_180*2 + another.is_inverse*3)) % 4
            try:
                return Step(self.face + [None, "", "2", "'"][status])
            except TypeError: return None
        raise ValueError("Should be the same side action.")

    def __mul__(self, i):
        """
        Multiply a Step by i times.
        The result will be as same as repeat this step for i times.

        >>> s = Step("U")
        >>> s * 2
        U2
        >>> s * 3
        U'

        >>> s = Step("U'")
        >>> s * 3
        U
        >>> s * 10
        U2
        """
        i = i % 4
        result = Step(self.name)
        for j in range(i-1):
            result += Step(self.name)
        return result

    def set(self, new):
        """
        Reset this Step.

        >>> s = Step("R2")
        >>> s
        R2

        >>> s.set("U'")
        >>> s
        U'
        """
        self.__init__(new)

    def set_face(self, new_face):
        """
        Reset the face of the action.

        >>> s = Step("R2")
        >>> s
        R2

        >>> s.set_face("L")
        >>> s
        L2
        """
        if new_face in list("LUFDRBlufdrbMSExyz"):
            self.face = new_face
            self.name = new_face + self.name[1:]
        else:
            raise ValueError("Invalid name")


    def inverse(self):
        """
        Inverse the Step.

        >>> s = Step("R")
        >>> s
        R

        >>> s.inverse()
        >>> s
        R'

        >>> s = Step("R2")
        >>> s.inverse()
        >>> s
        R2
        """
        new = self.name[0] + ("" if self.is_inverse else "'" if self.is_standard else "2")
        self.__init__(new)



class Algo(list):

    """
    Representing a Rubik's Cube algorithm.

    >>> a = Algo("R U R' U'")
    >>> a
    R U R' U'

    You can add two Algos together:
    >>> a + Algo("R' F R F'")
    R U R' U' R' F R F'
    >>> a + "F R' F' R"
    R U R' U' F R' F' R

    And also multiply by n times:
    >>> a * 3
    R U R' U' R U R' U' R U R' U'

    ==, >, >=, <, <=, != are a little bit different
    It only depends on the length
    >>> a
    R U R' U'
    >>> a == Algo("R' F R F'")
    True
    >>> a < Algo("R U R'")
    False

    If you want to check if two Algos are fully same, use |
    >>> a | Algo("R U R' U'")
    True
    >>> a | Algo("R' F R F'")
    False

    You can reverse an Algo simply like this:
    >>> a.reverse()
    >>> a
    U R U' R'

    You can also mirror it!
    >>> a.mirror()
    >>> a
    U' L' U L
    >>> a.mirror("UD")
    >>> a
    D L D' L'
    
    Also optimizing - only outer layer Steps.
    >>> a = Algo("R U r' x2 M' y' D D' L2 R L'")
    >>> a.optimize()
    >>> a
    R U R' F B

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

    def optimize(self):
        """
        Optimize the algorithm:
        - Only outer layers (LUFDRB)
        - No cube rotations (x y z)
        - No repeated steps
        """
        self._optimize_wide_actions()
        self._optimize_rotations()
        self._optimize_same_steps()

    def random(self, n=25, clear=True):
        """
        Random n steps.
        """
        opposite = {"U":"D", "L":"R", "F":"B", "D":"U", "R":"L", "B":"F"}
        if clear:
            self.clear()
        for i in range(n):
            self.append(random.choice("LUFDRB") + random.choice(["", "'", "2"]))
            try:
                while True:
                    if self[-1].face != self[-2].face and \
                            self[-1].face != self[-3].face and \
                            opposite[self[-1].face] != self[-2].face:
                        break
                    del self[-1]
                    self.append(random.choice("LUFDRB") + random.choice(["", "'", "2"]))
            except IndexError:
                pass

    def mirror(self, direction="LR"):
        """
        Mirror the algorithm.
        """
        opposite = {"U":"D", "L":"R", "F":"B", "D":"U", "R":"L", "B":"F"}
        direction = set(direction)
        specials = {
            frozenset("LR"): ("x", "M"), 
            frozenset("FB"): ("z", "S"), 
            frozenset("UD"): ("y", "E")
        }[frozenset(direction)]
        if direction not in (set("LR"), set("UD"), set("FB")):
            raise ValueError("There is only LR mirror, FB mirror, UD mirror")
        for step in self:
            if step.face.upper() in direction:
                if step.face.islower():
                    step.set_face(opposite[step.face.upper()].lower())
                else:
                    step.set_face(opposite[step.face])
            elif step.face in specials:
                continue
            step.inverse()

    del _stepify, _algify_input, _algify_output, _delattr


