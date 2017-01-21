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
