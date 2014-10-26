from .algorithm import *
from functools import reduce

class Square(object):
    """Square(colour), implements a square (sticker) on a cube."""
    def __init__(self, colour, parent=None, children=[]):
        super(Square, self).__init__()
        if isinstance(colour, Square):
            colour = colour.colour
        if not isinstance(colour, str):
            raise TypeError("Square.__init__() argument must be Square or str, got {0}."
                    .format(colour.__class__.__name__))
        if colour not in ["red", "yellow", "green", "white", "orange", "blue", "unknown"]:
            raise ValueError("Square colour must be "
                    "red, yellow, green, white, orange, blue or unknown, "
                    "not {0}.".format(colour))
        self.colour = colour
        self.parent = parent
        self.children = children

    def __repr__(self):
        """
        Print out two spaces with background colour.
        """
        return {
            "red":"\x1b[45m", 
            "yellow":"\x1b[43m", 
            "green":"\x1b[42m", 
            "white":"\x1b[47m", 
            "orange":"\x1b[41m", 
            "blue":"\x1b[46m", 
            "unknown":"\x1b[40m", 
            }[self.colour] + "  \x1b[49m"

    def  __eq__(self, another):
        """
        Check if the colour is as same as another.
        """
        if isinstance(another, Square):
            return self.colour == another.colour
        return False
    
    def __ne__(self, another):
        """
        Check if the colours are different.
        """
        return not self.__eq__(another)
    
    def __hash__(self):
        """
        Square object is hashable.
        """
        colour_to_hex = {
            "red":0xFF0000, 
            "yellow":0xFFFF00, 
            "green":0x00FF00, 
            "white":0xFFFFFF, 
            "orange":0xFFA500, 
            "blue":0x0000FF, 
            }
        return hash(str(self)) + colour_to_hex[self.colour]

    def copy(self):
        """
        Copy this Square.
        """
        return Square(self.colour)


class Cuboid(object):
    """
    Cuboid(**kwargs), implements a cuboid on the Cube.
    ex: Cuboid(U=Square("yellow"), F=Square("green"), L=Square("red"))
    """
    def __init__(self, parent=None, children=[], **kwargs):
        super(Cuboid, self).__init__()
        for kw in kwargs:
            if kw not in list("LUFDRB"):
                raise ValueError("Facings must be L U F D R B, not {0}.".format(kw))
            elif isinstance(kwargs[kw], str):
                kwargs[kw] = Square(kwargs[kw])
        self._facings = kwargs
        self.parent = parent
        self.children = children

    def __repr__(self):
        """
        Print out "Cuboid(U:\x1b[43m ...)"
        """
        return "Cuboid(" + \
            " , ".join([
                "{0}:{1}".format(key, value)
                for key, value in self._facings.items()
                ]) + \
            ")"

    def __getitem__(self, face):
        """
        Cuboid["L"] => Returns the square that positioned at L face.
        """
        return self._facings[face]

    def __hash__(self):
        """
        Cuboid object is hashable.
        """
        return reduce(lambda x, y:x + hash(y), self._facings.values())

    def __eq__(self, another):
        """
        Check if two Cuboids are the same.
        """
        return self._facings == another._facings

    def __ne__(self, another):
        """
        Check if two Cuboids are different.
        """
        return not self.__eq__(another)
    

