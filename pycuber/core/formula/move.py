# Intend to replace the original Step
import re


MOVE_RE = re.compile("([ULFRBD]w?|[MSEulfrbdxyz])(\'|i|2|2\'|)")

CLOCKWISE = 0
COUNTER = 1
HALFTURN = 2


class Move(object):

    __slots__ = ()

    def __new__(cls, representation):
        self = super().__new__(cls)
        if isinstance(representation, Move):
            symbol = representation.symbol
            sign = representation.sign
        else:
            match = MOVE_RE.match(representation.strip())
            if match is None:
                raise ValueError("Invalid move: {}".format(representation))
            symbol, sign = match
            if "w" in symbol:
                symbol = symbol[0].lower()
            if sign == "2'":
                sign = "2"

        self.symbol = symbol
        self.sign = ["", "'", "2"].index(sign)

        return self

    def __repr__(self):
        return self.symbol + ["", "'", "2"][self.sign]

    def __hash__(self):
        return hash(str(self))
