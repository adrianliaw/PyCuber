# Intend to replace the original Step
import re
from operator import itemgetter


MOVE_RE = re.compile("([ULFRBD]w?|[MSEulfrbdxyz])(\'|i|2|2\'|)")

CLOCKWISE = 1
HALFTURN = 2
COUNTER = 3


class Move(tuple):

    __slots__ = ()

    def __new__(cls, representation):
        if isinstance(representation, Move):
            symbol = representation.symbol
            sign = representation.sign

        elif isinstance(representation, tuple) and len(representation) == 2:
            symbol, sign = representation
            assert symbol in "ULFRBDMSEulfrbdxyz" and sign in (1, 2, 3), \
                "Invalid Move initialisation: {}".format(representation)

        elif isinstance(representation, str):
            match = MOVE_RE.match(representation.strip())
            if match is None:
                raise ValueError("Invalid move: {}".format(representation))
            symbol, sign = match.groups()
            if "w" in symbol:
                symbol = symbol[0].lower()
            if sign == "2'":
                sign = "2"
            if sign == "i":
                sign = "'"
            sign = [None, "", "2", "'"].index(sign)

        else:
            raise ValueError("Can only accept Move, str, or 2-element tuple")

        return super().__new__(cls, (symbol, sign))

    symbol = property(itemgetter(0))
    sign = property(itemgetter(1))

    def __repr__(self):
        return self.symbol + [None, "", "2", "'"][self.sign]

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, move):
        if not isinstance(move, Move):
            move = Move(move)
        return self.symbol == move.symbol and self.sign == move.sign

    def __ne__(self, move):
        return not self.__eq__(move)

    def __add__(self, move):
        if not isinstance(move, Move):
            move = Move(move)
        assert self.symbol == move.symbol, "Can't operate addition on two " \
                                           "Moves with different symbols"
        sign = (self.sign + move.sign) % 4
        if sign == 0:
            return 0
        return Move((self.symbol, sign))

    def __mul__(self, i):
        assert isinstance(i, int), "Can only multiply with an integer"
        sign = (self.sign * i) % 4
        if sign == 0:
            return 0
        return Move((self.symbol, sign))

    def inverse(self):
        return Move((self.symbol, 4 - self.sign))


if __name__ == "__main__":
    m = Move("R")
    assert m * 3 == m.inverse() == Move("R'")
    assert m + Move("R'") == 0
    assert m + Move("R") == Move("R2")
    assert Move("l'") == Move("li") == Move(("l", 3)) == Move(Move("l'"))
