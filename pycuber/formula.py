"""

This module is to implement the Rubik's Cube formulae.
You can deal with Rubik's Cube formulae easily with Step and Formula.

Usage:
    >>> a = Formula("R U R' U'")
    >>> a
    R U R' U'

    >>> a.reverse()
    >>> a
    U R U' R'

    >>> a.mirror()
    >>> a
    U' L' U L

    >>> a *= 3
    >>> a
    U' L' U L U' L' U L U' L' U L

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
    >>> r.is_clockwise
    True
    >>> r.is_counter_clockwise
    False
    >>> r.is_180
    False

    >>> u_prime.is_clockwise
    False
    >>> u_prime.is_counter_clockwise
    True
    >>> u_prime.is_180
    False

    Or you can inverse action like this:
    >>> s = Step("U'")
    >>> s.inverse()
    U

    Reset the face of Step:
    >>> s = s.set_face("L")
    >>> s
    L2

    You can add two Steps together!
    >>> s + Step("L'")
    L
    >>> s + Step("L2")
    None

    And also multiply by numbers!
    >>> s = Step("L")
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
            if len(name) >= 2 and name[1] == "w":
                name = name[0].lower() + name[2:]
            if "i" in name:
                name = name.replace("i", "'")
            if name[1:] == "2'":
                name = name[0] + "2"
            if name[0] in "LUFDRBMSElufdrbxyz":
                if name[1:] in ["", "'", "2"]:
                    self.__name = lambda: name
                    self.__face = lambda: name[0]
                    self.__is_counter_clockwise = lambda: name[1:] == "'"
                    self.__is_clockwise = lambda: name[1:] == ""
                    self.__is_180 = lambda: name[1:] == "2"
                    return
            raise IndexError
        except IndexError:
            raise ValueError("Invalid action name {0}".format(name))

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
            status = ((self.is_clockwise + self.is_180 * 2 + self.is_counter_clockwise * 3) + \
                      (another.is_clockwise + another.is_180 * 2 + another.is_counter_clockwise * 3)) % 4
            try:
                return Step(self.face + [None, "", "2", "'"][status])
            except TypeError:
                return None
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
        i %= 4
        if i == 0:
            return None
        result = Step(self.name)
        for j in range(i - 1):
            result += Step(self.name)
        return result

    def set_face(self, new_face):
        """
        Reset the face of the action.

        >>> s = Step("R2")
        >>> s
        R2

        >>> s = s.set_face("L")
        >>> s
        L2
        """
        if new_face in list("LUFDRBlufdrbMSExyz"):
            return Step(new_face + "'" * self.is_counter_clockwise + "2" * self.is_180)
        else:
            raise ValueError("Invalid name")

    def inverse(self):
        """
        Inverse the Step.

        >>> s = Step("R")
        >>> s
        R

        >>> s.inverse()
        R'

        >>> s = Step("R2")
        >>> s.inverse()
        R2
        """
        return Step(self.name[0] + ("" if self.is_counter_clockwise else "'" if self.is_clockwise else "2"))

    def __hash__(self):
        """
        Step object is hashable.
        """
        return hash(self.name)

    @property
    def name(self):
        """
        Name of the Step object (B', R, U2)
        """
        return self.__name()

    @property
    def is_counter_clockwise(self):
        """
        True if direction is counter-clockwise (not including 180 degrees)
        False otherwise
        """
        return self.__is_counter_clockwise()

    @property
    def is_clockwise(self):
        """
        True if direction is clockwise (not including 180 degrees)
        False otherwise
        """
        return self.__is_clockwise()

    @property
    def is_180(self):
        """
        True if the action is to turn 180 degrees
        False otherwise
        """
        return self.__is_180()

    @property
    def face(self):
        """
        Face of the step (R, U, l, x, M)
        """
        return self.__face()


class Formula(list):
    """
    Representing a Rubik's Cube formula.

    >>> a = Formula("R U R' U'")
    >>> a
    R U R' U'

    You can add two Formulae together:
    >>> a + Formula("R' F R F'")
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
    >>> a == Formula("R' F R F'")
    True
    >>> a < Formula("R U R'")
    False

    If you want to check if two Formulae are fully same, use |
    >>> a | Formula("R U R' U'")
    True
    >>> a | Formula("R' F R F'")
    False

    You can reverse an Formula simply like this:
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
    
    Also optimising - only outer layer Steps.
    >>> a = Formula("R U r' x2 M' y' D D' L2 R L'")
    >>> a.optimise()
    >>> a
    R U R' F B

    """

    def __init__(self, sequence=[]):
        if type(sequence) == str:
            sequence = sequence.split()
        elif isinstance(sequence, Step):
            sequence = [sequence]
        for i in range(len(sequence)):
            sequence[i] = Step(sequence[i])
        super(Formula, self).__init__(sequence)

    def __repr__(self):
        """
        Representing a Formula object, just print out every move

        >>> a = Formula("R U R' U'")
        >>> a
        R U R' U'
        """
        return " ".join(map(lambda x: x.name, self))

    def __getitem__(self, index):
        """
        Get ith item of Formula.

        >>> a = Formula("R U R' U'")
        >>> a[1]
        U
        """
        result = super(Formula, self).__getitem__(index)
        if isinstance(index, slice):
            return Formula(result)
        return result

    def __setitem__(self, index, item):
        """
        Set ith item of Formula.

        >>> a = Formula("R U R' U'")
        >>> a[0] = Step("L")
        >>> a
        L U R' U'
        >>> a[0] = "R'"
        >>> a
        R' U R' U'
        """
        if None is item:
            del self[index]
            return
        if isinstance(index, slice):
            super(Formula, self).__setitem__(index, Formula(item))
        else:
            super(Formula, self).__setitem__(index, Step(item))

    def __setattr__(self, name, value):
        """
        We don't allow user to set attribute.
        """
        if name in dir(self) and name != "sort":
            raise AttributeError("'Formula' object attribute '{}' is read-only".format(name))
        else:
            raise AttributeError("'Formula' object has no attribute '{}'".format(name))

    def _stepify(func):
        """Makes last input a Step object."""

        @wraps(getattr(list, func.__name__), assigned=("__name__", "__doc__"))
        def _func(*args, **kwargs):
            args = list(args[:-1]) + [Step(args[-1])]
            return getattr(list, func.__name__)(*args, **kwargs)

        return _func

    def _formulaize_input(func):
        """Makes last input a Formula object."""

        def _func(*args, **kwargs):
            args = list(args[:-1]) + [Formula(args[-1])]
            return getattr(list, func.__name__)(*args, **kwargs)

        _func.__doc__ = getattr(list, func.__name__).__doc__
        _func.__name__ = func.__name__ + " "
        return _func

    def _formulaize_output(func):
        """Makes output a Formula object."""

        @wraps(getattr(list, func.__name__.strip()), assigned=("__name__", "__doc__"))
        def _func(*args, **kwargs):
            if " " in func.__name__:
                return Formula(func(*args, **kwargs))
            return Formula(getattr(list, func.__name__)(*args, **kwargs))

        return _func

    def _delattr(func):
        """Raise error when calling some not needed method."""

        def _func(*args, **kwargs):
            raise AttributeError("'Formula' object has no attribute '{0}'".format(func.__name__))

        return _func

    def _return_self(func):
        """Make function returns self."""

        @wraps(func, assigned=("__name__", "__doc__"))
        def _func(*args, **kwargs):
            if args[-1] != None:
                func(*args, **kwargs)
            return args[0]

        return _func

    @_formulaize_output
    @_formulaize_input
    def __add__(self, another):
        pass

    if sys.version_info.major == 2:
        @_formulaize_output
        def __getslice__(self, i, j): pass

        @_formulaize_input
        def __setslice__(self, i, j, value): pass

    @_formulaize_output
    def __mul__(self, i):
        pass

    def __iadd__(self, another):
        return self.__add__(another)

    @_return_self
    @_formulaize_input
    def extend(self, another):
        pass

    def __eq__(self, another):
        """
        Check if length of this Formula is equal to another.
        
        >>> a = Formula("R U R' U'")
        >>> a == Formula("R' F R F'")
        True
        >>> a == "U R U' R'"
        True
        >>> a == Formula("R U R'")
        False
        """
        return len(self) == len(Formula(another))

    def __lt__(self, another):
        """
        Check if length of this Formula is less than another.

        >>> a = Formula("R U R' U'")
        >>> a < Formula("R' F R F' R'")
        True
        >>> a < Formula("R U R'")
        False
        >>> a < "R' F R F' R'"
        True
        """
        return len(self) < len(Formula(another))

    def __gt__(self, another):
        """
        Check if length of this Formula is greater than another.

        >>> a = Formula("R U R' U'")
        >>> a > Formula("R U R'")
        True
        >>> a > Formula("R' F R F' R'")
        False
        >>> a > "R U R'"
        True
        """
        return len(self) > len(Formula(another))

    def __ge__(self, another):
        """
        Check if length of this Formula is greater than or equal to another.

        >>> a = Formula("R U R' U'")
        >>> a >= Formula("R U R'")
        True
        >>> a >= Formula("R' F R F' R'")
        False
        >>> a >= "R U R' U"
        True
        """
        return len(self) >= len(Formula(another))

    def __le__(self, another):
        """
        Check if length of this Formula is less than or equal to another.

        >>> a = Formula("R U R' U'")
        >>> a <= Formula("R U R'")
        False
        >>> a <= Formula("R' F R F' R'")
        True
        >>> a <= "R U R' U"
        True
        """
        return len(self) <= len(Formula(another))

    def __ne__(self, another):
        """
        Check if length of this Formula is'n equal to another.

        >>> a = Formula("R U R' U'")
        >>> a <= Formula("R U R'")
        False
        >>> a <= Formula("R' F R F' R'")
        True
        >>> a <= "R U R' U"
        True
        """
        return len(self) != len(Formula(another))

    def __reversed__(self):
        """
        Reversed list iterator.
        """
        return self.copy().reverse()

    @_stepify
    def __contains__(self, value):
        pass

    @_return_self
    @_stepify
    def append(self, another):
        pass

    @_stepify
    def count(self, value):
        pass

    @_stepify
    def index(self, start, stop):
        pass

    @_return_self
    @_stepify
    def insert(self, index, obj):
        pass

    @_return_self
    @_stepify
    def remove(self, value):
        pass

    @_delattr
    def sort(*args):
        pass

    def __or__(self, another):
        """
        Check if two Formulae are fully same.

        >>> a = Formula("R U R' U'")
        >>> a == Formula("R' F R F'")
        True
        >>> a | "R' F R F'"
        False
        >>> a | "R U R' U'"
        True
        """
        another = Formula(another)
        if len(self) == len(another):
            for i in range(len(self)):
                if self[i] != another[i]:
                    break
            else:
                return True
        return False

    def reverse(self):
        """
        Reverse this Formula.

        >>> a = Formula("R U R' U'")
        >>> a.reverse()
        >>> a
        U R U' R'
        """
        if len(self) == 0: return self
        for i in range(int((len(self) + 1) / 2)):
            self[i] = self[i].inverse()
            if i != len(self) - i - 1:
                self[-i - 1] = self[-i - 1].inverse()
            self[i], self[-i - 1] = self[-i - 1], self[i]
        return self

    def clear(self):
        """L.clear() -> None -- remove all items from L"""
        self[:] = ""
        return self

    def copy(self):
        """L.copy() -> Formula -- a shallow copy of L"""
        return Formula(self)

    def _optimise_wide_actions(self):
        """
        Helper function for Formula.optimise()
        Reduce the wide actions (double layers)

        >>> a = Formula("r u' M2")
        >>> a._optimise_wide_actions()
        >>> a
        L x D' y' R2 L2 x2
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
        _self = Formula(self)
        index = 0
        for step in _self:
            if step.name[0] in pattern:
                replacement = Formula(pattern[step.name[0]])
                if step.name[1:] != "":
                    for i in range(len(replacement)):
                        if step.name[1] == "'":
                            replacement[i] *= -1
                        else:
                            replacement[i] *= 2
                self[index:index + 1] = replacement
                index += len(replacement)
            else:
                index += 1
        return self

    def _optimise_rotations(self):
        """
        Helper function for Formula.optimise()
        Reduce the rotations (whole cube rotations).

        >>> a = Formula("L x D' y' R2 L2 x2")
        >>> a._optimise_rotations()
        >>> a
        L B' D2 U2
        """
        pattern = {
            "x": "UFDB",
            "y": "FRBL",
            "z": "ULDR"
        }
        _self = Formula(self)
        self.clear()
        for i in range(len(_self) - 1, -1, -1):
            if _self[i].face not in pattern:
                self.insert(0, _self[i])
            else:
                cr_pattern = pattern[_self[i].face]
                if _self[i].is_counter_clockwise:
                    cr_pattern = cr_pattern[::-1]
                for j in range(len(self)):
                    if self[j].face in cr_pattern:
                        if _self[i].is_180:
                            self[j] = self[j].set_face(cr_pattern[(cr_pattern.index(self[j].face) + 2) % 4])
                        else:
                            self[j] = self[j].set_face(cr_pattern[(cr_pattern.index(self[j].face) + 1) % 4])
        return self

    def _optimise_same_steps(self, is_root=True):
        """
        Helper function for Formula.optimise()
        Reduce repeated steps.

        >>> a = Formula("R R2 U'")
        >>> a._optimise_same_steps()
        >>> a
        R' U'

        >>> a = Formula("R L' R U2")
        >>> a._optimise_same_steps()
        >>> a
        R2 L' U2
        """
        opposite = {"U": "D", "L": "R", "F": "B", "D": "U", "R": "L", "B": "F"}
        if len(self) < 2:
            return self
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
                if self[0] + self[2] is None:
                    self[0] += self[2]
                    del self[1]
                    if len(self) == 1:
                        return self
                    flag = False
                else:
                    self[0] += self[2]
                    del self[2]
            if self[0].face == self[1].face:
                if self[0] + self[1] is None:
                    self[0] += self[1]
                    del self[0]
                    flag = False
                else:
                    self[0] += self[1]
                    del self[1]
            rhs = self[flag:]
            _optimise_same_steps(rhs, is_root=False)
            self[flag:] = rhs
        if is_root:
            while not self.copy() | _optimise_same_steps(self, is_root=False):
                pass
        return self

    def optimise(self):
        """
        Optimize the formula:
        - Only outer layers (LUFDRB)
        - No cube rotations (x y z)
        - No repeated steps

        >>> a = Formula("R U r' x2 M' y' D D' L2 R L'")
        >>> a.optimise()
        >>> a
        R U R' F B
        """
        _optimise_same_steps(_optimise_rotations(_optimise_wide_actions(self)))
        return self

    optimise.__globals__["_optimise_wide_actions"] = _optimise_wide_actions
    optimise.__globals__["_optimise_rotations"] = _optimise_rotations
    optimise.__globals__["_optimise_same_steps"] = _optimise_same_steps
    del _optimise_wide_actions, _optimise_rotations, _optimise_same_steps

    def random(self, n=25, clear=True):
        """
        Random n Steps. (default 25)

        >>> a = Formula()
        >>> a.random()
        >>> a
        D' L' U B' D' F2 R D2 L2 F2 U' L' D F2 R' B D R2 B2 D R' U F2 R D

        >>> a.random(15)
        >>> a
        F' R D B2 R' F' L2 D2 F2 L2 D2 B' U F2 L
        """
        opposite = {"U": "D", "L": "R", "F": "B", "D": "U", "R": "L", "B": "F"}
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
        return self

    def mirror(self, direction="LR"):
        """
        Mirror the formula.

        >>> a = Formula("R U R' U'")
        >>> a.mirror()
        >>> a
        L' U' L U
        >>> a.mirror("LR")
        >>> a
        R U R' U'

        >>> a.mirror("UD")
        >>> a
        R' D' R D

        >>> a = Formula("R' F R F'")
        >>> a.mirror("FB")
        >>> a
        R B' R' B
        """
        opposite = {"U": "D", "L": "R", "F": "B", "D": "U", "R": "L", "B": "F"}
        direction = set(direction)
        specials = {
            frozenset("LR"): ("x", "M"),
            frozenset("FB"): ("z", "S"),
            frozenset("UD"): ("y", "E")
        }[frozenset(direction)]
        if direction not in (set("LR"), set("UD"), set("FB")):
            raise ValueError("There is only LR mirror, FB mirror, UD mirror")
        for i in range(len(self)):
            step = self[i]
            if step.face.upper() in direction:
                if step.face.islower():
                    self[i] = self[i].set_face(opposite[step.face.upper()].lower())
                else:
                    self[i] = self[i].set_face(opposite[step.face])
            elif step.face in specials:
                continue
            self[i] = self[i].inverse()
        return self

    del _stepify, _formulaize_input, _formulaize_output, _delattr, _return_self
