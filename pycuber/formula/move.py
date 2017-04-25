import re
from operator import itemgetter


GENERIC_MOVE_RE = re.compile(
    "([1-9][0-9]*|)([ULFRBD]w?|[MSEulfrbdxyz])(\'|i|2|2\'|)")
MOVE_RE = re.compile("()([ULFRBD]w?|[MSEulfrbdxyz])(\'|i|2|2\'|)")

CLOCKWISE = 1
HALFTURN = 2
COUNTER = 3


class GenericCubicMove(tuple):

    __slots__ = ()
    __regex__ = GENERIC_MOVE_RE

    def __new__(cls, representation):
        if isinstance(representation, GenericCubicMove):
            symbol = representation.symbol
            sign = representation.sign
            level = representation.level

        elif isinstance(representation, tuple) and len(representation) == 3:
            level, symbol, sign = representation
            assert isinstance(level, int) and level > 0 and \
                symbol in "ULFRBDMSEulfrbdxyz" and sign in (1, 2, 3), \
                "Invalid move: {}".format(representation)

        elif isinstance(representation, str):
            match = cls.__regex__.match(representation.strip())
            if match is None:
                raise ValueError("Invalid move: {}".format(representation))
            level, symbol, sign = match.groups()
            if "w" in symbol:
                symbol = symbol[0].lower()
            if level == "":
                if symbol in "ulfrbd":
                    level = "2"
                else:
                    level = "1"
            level = int(level)
            if sign == "2'":
                sign = "2"
            if sign == "i":
                sign = "'"
            sign = [None, "", "2", "'"].index(sign)

        else:
            raise ValueError("Can only accept Move, str, or 3-element tuple")

        if symbol in "ulfrbd" and level == 1:
            symbol = symbol.upper()
        if symbol in "MSExyz":
            level = 1

        return super().__new__(cls, (level, symbol, sign))

    level = property(itemgetter(0))
    symbol = property(itemgetter(1))
    sign = property(itemgetter(2))

    def __repr__(self):
        level = self.level
        if level == 1 or (self.symbol in "ulfrbd" and level == 2):
            level = ""
        return str(level) + self.symbol + [None, "", "2", "'"][self.sign]

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, move):
        if not isinstance(move, self.__class__):
            move = self.__class__(move)
        return super().__eq__(move)

    def __ne__(self, move):
        return not self.__eq__(move)

    def __add__(self, move):
        if not isinstance(move, self.__class__):
            move = self.__class__(move)
        assert self.symbol == move.symbol and self.level == move.level, \
            "Can't operate addition on two Moves with different symbols"
        sign = (self.sign + move.sign) % 4
        if sign == 0:
            return 0
        return self.__class__((self.level, self.symbol, sign))

    def __mul__(self, i):
        assert isinstance(i, int), "Can only multiply with an integer"
        sign = (self.sign * i) % 4
        if sign == 0:
            return 0
        return self.__class__((self.level, self.symbol, sign))

    def inverse(self):
        return self.__class__((self.level, self.symbol, 4 - self.sign))

    def with_level(self, level=1):
        return self.__class__((level, self.symbol, self.sign))

    def with_symbol(self, symbol):
        return self.__class__((self.level, symbol, self.sign))

    def with_sign(self, sign=1):
        return self.__class__((self.level, self.symbol, sign))

    def is_single(self):
        return self.symbol.isupper()

    def is_face(self):
        return self.is_single() and self.level == 1

    def is_slice(self):
        return (self.level > 1 and self.is_single()) or self.is_middle()

    def is_rotate(self):
        return self.symbol in ("x", "y", "z")

    def is_middle(self):
        return self.symbol in ("M", "E", "S")

    def is_wide(self):
        return not self.is_single() and self.level > 1 and not self.is_rotate()


class Move(GenericCubicMove):
    __regex__ = MOVE_RE

    def __new__(cls, representation):
        if isinstance(representation, tuple):
            if len(representation) == 3:
                level, symbol, sign = representation
                if (symbol in "ULFRBDMSExyz" and level != 1) or \
                        (symbol in "ulfrbd" and level != 2):
                    raise ValueError("Bad Move: {}"
                                     .format(representation))
            elif len(representation) == 2:
                if symbol in "ULFRBDMSExyz":
                    representation = (1, *representation)
                else:
                    representation = (2, *representation)
        return super().__new__(cls, representation)
