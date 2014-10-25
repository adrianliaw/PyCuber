from .algorithm import *

class Square(object):
    """Square(colour, face, index), implements a square (sticker) on a cube."""
    def __init__(self, colour):
        super(Square, self).__init__()
        self.colour = colour

    def __repr__(self):
        """
        Print out two spaces with background colour.
        """
        return {"red":"\x1b[45m", "yellow":"\x1b[43m", "green":"\x1b[42m", "white":"\x1b[47m", "orange":"\x1b[41m", "blue":"\x1b[46m", "unknown":"\x1b[40m"}[self.colour] + "  \x1b[49m"

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
        colour_to_hex = {"red":0xFF0000, "yellow":0xFFFF00, "green":0x00FF00, "white":0xFFFFFF, "orange":0xFFA500, "blue":0x0000FF}
        return hash(str(self)) + colour_to_hex[self.colour]

    def copy(self):
        """
        Copy this Square.
        """
        return Square(self.colour)


        
