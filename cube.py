"""
This module is going to implement a Rubik's Cube

It implements like this
________________
|    |    |    |
| 00 | 01 | 02 |
|____|____|____|
|    |    |    |
| 07 |(08)| 03 |
|____|____|____|
|    |    |    |
| 06 | 05 | 04 |
|____|____|____|

"""

class Square:
    """
    Square(colour, face, index), implements a square (sticker) on a cube.
    """
    def __init__(self, colour):
        self._colour = colour
        #self._face = face
        #self._index = index
        #self._type = ["corner", "centre", "edge"][(index==8) or (index%2)*2]
        self.user_data = {}
    def __repr__(self):
        #return "[SQUARE {0._colour} {0._face}{0._index}]".format(self)
        return "[SQUARE {colour}]".format(colour = self._colour)
    #def set_position(self, index, face=None):
    #    """Reset the position (index) of the square in a cube."""
    #    self._face = face if face else self._face
    #    self._index = index
    #    self._type = ["corner", "centre", "edge"][(index==8) or (index%2)*2]
    #def set_by_2d(self, xy, face=None):
    #    """Reset the position (index) of the square by 2d position."""
    #    self._face = face
    #    if xy[0] == xy[1] == 1:
    #        self._index = 8
    #        self._type = "centre"
    #        return
    #    elif xy[0] < 2 and xy[1] > 0:
    #        self._index = 8 - sum(xy)
    #    else:
    #        self._index = sum(xy)
    #    self._type = ["corner", "edge"][index%2]
    #def set_colour(self, colour):
    #    """Reset the colour of the square."""
    #    self._colour = colour

class Face:
    """
    Face(face, (?:[01, 02, ..., 08])), implements a face on a cube.
    """
    def __init__():
        pass
    def __str__():
        pass
    def __repr__():
        pass
    def rotate():
        """Rotate this face clockwise or counter-clockwise."""
        pass
    def get_horz_row():
        """Get the horizontal row(s) of the face."""
        pass
    def get_vert_row():
        """Get the vertical row(s) of the face."""
        pass
    def get_by_index():
        """Get the square by the index."""
        pass
    def get_by_2d():
        """Get the square by 2d position."""
        pass
    def get_colour():
        """Get the centre square of the face."""
        pass

class Cube:
    """
    Cube([face * 6]), implements a whole cube.
    """
    def __init__():
        pass
    def __str__():
        pass
    def __repr__():
        pass
    def _outer_layer_rotate():
        """Perform the actions like U R' D2 L' """
        pass
    def _cube_rotation():
        """Perform the actions like x y' z2 """
        pass
    def _double_layers_rotate():
        """Perform the actions like u r' d2 l' """
        pass
    def _middle_layer_rotate():
        """Perform the actions like M S' E2"""
        pass
    def perform_action():
        """Perform an action."""
        pass

