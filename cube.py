"""
This module is to implement a Rubik's Cube

The data structure of a Rubik's Cube is like this:
           
    Cube - | L face
           | U face
           | F face
           | D face
           | R face
           | B face

    Face - | centre
           | list of 8 stickers around centre sticker
            ________________
            |    |    |    |
            | 00 | 01 | 02 |
            |____|____|____|
            |    |    |    |
            | 07 |    | 03 |
            |____|____|____|
            |    |    |    |
            | 06 | 05 | 04 |
            |____|____|____|

Easy to use and easy to visualise.

>>> c = Cube()
>>> c
      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m

>>> a = Algo("R U R' U' R' F R2 U' R' U' R U R' F'") # T-perm
>>> c(a) # Perform T-perm on c.
>>> c
      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[41m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m

>>> a.reverse() # Reverse the T-perm algorithm.
>>> c(a) # Perform reversed T-perm.
>>> c
      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n      \x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\x1b[43m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[45m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[42m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[41m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\x1b[46m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\n      \x1b[47m  \x1b[49m\x1b[47m  \x1b[49m\x1b[47m  \x1b[49m

"""

from .algorithm import *
from collections import namedtuple
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

_Cuboid = namedtuple("Cuboid", ["x", "y", "z"])
_Cuboid.type = "Cuboid"
_Square = namedtuple("Square", ["face", "index", "colour"])
_Square.type = "Square"


class Square(object):

    """
    Square(colour, face, index), implements a square (sticker) on a cube.

    >>> s = Square("green")
    >>> s
    \x1b[42m  \x1b[49m

    Notice: Only use red, yellow, green, white, orange and blue.
    """

    def __init__(self, colour):
        self.colour = colour

    def __repr__(self):
        """
        Print out two spaces with background colours.

        >>> s = Square("red")
        >>> s
        \x1b[45m  \x1b[49m
        >>> s.__repr__()
        '\\x1b[45m  \\x1b[49m'
        """
        return {"red":"\x1b[45m", "yellow":"\x1b[43m", "green":"\x1b[42m", "white":"\x1b[47m", "orange":"\x1b[41m", "blue":"\x1b[46m"}[self.colour] + "  \x1b[49m"
    
    def __eq__(self, another):
        """
        Check if the colour is as same as another.

        >>> s = Square("red")
        >>> p = Square("red")
        >>> s == p
        True
        """
        return self.colour == another.colour

    def __ne__(self, another):
        """
        Check if the colours are different.
        
        >>> s = Square("red")
        >>> p = Square("green")
        >>> s != p
        True
        """
        return self.colour != another.colour

    def clone(self):
        """
        Clone this square.

        >>> s = Square("yellow")
        >>> p = s.clone()
        >>> s == p
        True
        """
        new = Square(self.colour)
        return new
    
    def __hash__(self):
        """
        Square object is hashable.

        >>> s = Square("red")
        >>> hash(s)
        505081555585376768
        """
        colour_to_hex = {"red":0xFF0000, "yellow":0xFFFF00, "green":0x00FF00, "white":0xFFFFFF, "orange":0xFFA500, "blue":0x0000FF}
        return hash(str(self)) + colour_to_hex[self.colour]



class Face(object):

    """
    Face(face, colour_or_list_of_squares), implements a face on a cube.
    """

    def __init__(self, squares):
        if type(squares) == str:
            squares = [Square(squares) for i in range(9)]
        self.centre = squares[8]
        self.arounds = squares[:8]
        self.user_data = {}

    def __repr__(self):
        return (''.join(str(self.arounds[i]) for i in range(3)) + "\n" + 
                str(self.arounds[7]) + str(self.centre) + str(self.arounds[3]) + "\n" + 
                ''.join(str(self.arounds[i]) for i in range(6, 3, -1)))
    
    def __getitem__(self, index):
        return (self.arounds + [self.centre])[index]
        

    def rotate(self, cc=False):
        """Rotate this face clockwise or counter-clockwise."""
        for i in range(2):
            square = self.arounds.pop(cc-1)
            self.arounds.insert(cc*8, square)

    def get_row(self, pos):
        """Get the row by URDL on a face."""
        idx = "URDL".index(pos)*2
        if pos != "L":
            return self.arounds[idx:][:3]
        else:
            return self.arounds[idx:] + [self.arounds[0]]

    def get_by_2d(self, xy):
        """Get the square by 2d position."""
        if xy[0] == xy[1] == 1:
            return self.centre
        elif xy[0] < 2 and xy[1] > 0:
            return self.arounds[8-sum(xy)]
        else:
            return self.arounds[sum(xy)]

    def clone(self):
        """Clone a face."""
        new = Face([self.arounds[i].clone() for i in range(8)] + [self.centre.clone()])
        new.user_data = self.user_data.copy()
        return new



class Cube(object):

    """
    Cube([face * 6 L,U,F,D,R,B]), implements a whole cube.
    """

    def __init__(self, faces=None):
        if not faces:
            for pair in zip("LUFDRB", ["red", "yellow", "green", "white", "orange", "blue"]):
                self[pair[0]] = Face(pair[1])
        else:
            for pair in enumerate("LUFDRB"):
                self[pair[1]] = faces[pair[0]]
        self.user_data = {}

    def __repr__(self):
        result = ["      ", "      ", "      ", "", "", "", "      ", "      ", "      "]
        for i in range(3):
            for j in range(3):
                result[i] += str(self["U"])[i+(3*i+j)*12:i+(3*i+j)*12+12]
        for side in "LFRB":
            for i in range(3):
                for j in range(3):
                    result[3+i] += str(self[side])[i+(3*i+j)*12:i+(3*i+j)*12+12]
        for i in range(3):
            for j in range(3):
                result[6+i] += str(self["D"])[i+(3*i+j)*12:i+(3*i+j)*12+12]
        return "\n".join(result)

    def __getitem__(self, key):
        for side in ["left", "up", "front", "down", "right", "back"]:
            if key == side or key == side[0].upper():
                return eval("self.%s" % side)

    def __setitem__(self, key, value):
        if key == "left" or key == "L": self.left = value
        elif key == "up" or key == "U": self.up = value
        elif key == "front" or key == "F": self.front = value
        elif key == "down" or key == "D": self.down = value
        elif key == "right" or key == "R": self.right = value
        elif key == "back" or key == "B": self.back = value

    def _outer_layer_rotate(self, symbol):
        """Perform the actions like U R' D2 L' """
        _olr_patterns = {
            "L": "UL FL DL BR", 
            "U": "BU RU FU LU", 
            "F": "LR UD RL DU", 
            "D": "LD FD RD BD", 
            "R": "DR FR UR BL", 
            "B": "RR UU LL DD"
        }
        self[symbol[0]].rotate("'" in symbol)
        rows = [self[p[0]].get_row(p[1]) for p in _olr_patterns[symbol[0]].split()]
        copy = [[sqr.clone() for sqr in a_row] for a_row in rows]
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                rows[i][j].colour = copy[(i + ("'" in symbol) * 2 - 1) % 4][j].colour
        if len(symbol) == 2 and symbol[1] == "2":
            self._outer_layer_rotate(symbol[0])

    def _cube_rotation(self, symbol):
        """Perform the actions like x y' z2 """
        _cr_patterns = {
            "x": (["F", 0, "U", 2, "B", 2, "D", 0, "F"], "RL"), 
            "y": (["L", 0, "B", 0, "R", 0, "F", 0, "L"], "UD"), 
            "z": (["U", 1, "R", 1, "D", 1, "L", 1, "U"], "FB")
        }
        self[_cr_patterns[symbol[0]][1][0]].rotate("'" in symbol)
        self[_cr_patterns[symbol[0]][1][1]].rotate("'" not in symbol)
        change = _cr_patterns[symbol[0]][0][::("'" not in symbol)*2-1]
        if "'" in symbol:
            for i in range(1, 8, 2):
                if change[i] == 1: change[i] = -1
        old = [self[change[i]].clone() for i in range(0, 7, 2)]
        for i in range(4):
            if change[i*2+1] == 2:
                for j in range(2): old[i].rotate()
            elif change[i*2+1] != 0:
                old[i].rotate(int((-change[i*2+1]+1)/2))
            self[change[i*2+2]] = old[i]
        if "2" in symbol:
            self._cube_rotation(symbol[0])

    def _double_layers_rotate(self, symbol):
        """Perform the actions like u r' d2 l' """
        _dlr_patterns = {
            "l": ["x'", "R"], 
            "u": ["y", "D"], 
            "f": ["z", "B"], 
            "d": ["y'", "U"], 
            "r": ["x", "L"], 
            "b": ["z'", "F"]
        }
        actions = _dlr_patterns[symbol[0]][:]
        if "'" in symbol:
            if "'" in actions[0]: actions[0] = actions[0][0]
            else: actions[0] = actions[0] + "'"
            actions[1] += "'"
        elif "2" in symbol:
            for i in range(2): actions[i] = actions[i][0] + "2"
        self._cube_rotation(actions[0])
        self._outer_layer_rotate(actions[1])

    def _middle_layer_rotate(self, symbol):
        """Perform the actions like M S' E2"""
        _mlr_patterns = {
            "M": "l", 
            "S": "f", 
            "E": "d"
        }
        self._double_layers_rotate(_mlr_patterns[symbol[0]] + symbol[1:])
        olr_adds = "" if "'" in symbol else "2" if "2" in symbol else "'"
        self._outer_layer_rotate(_mlr_patterns[symbol[0]].upper() + olr_adds)

    def perform_step(self, step):
        """Perform an action (step)."""
        step = Step(step)
        if step.name.isupper():
            if any([a in step.name for a in "MSE"]):
                self._middle_layer_rotate(step.name)
            else:
                self._outer_layer_rotate(step.name)
        else:
            if any([a in step.name for a in "xyz"]):
                self._cube_rotation(step.name)
            else:
                self._double_layers_rotate(step.name)

    def perform_algo(self, algo):
        """Perform an algorithm."""
        algo = Algo(algo)
        for step in algo:
            self.perform_step(step)

    def __call__(self, algo_or_step):
        """Perform Step or Algo on this cube."""
        algo = Algo(algo_or_step)
        self.perform_algo(algo)
    
    def as_graph(self):
        """Convert cube into graph. \nGraphics: http://pycuber.appspot.com/cubegraph/main.html"""
        return _CubeAsGraph(self)

    def clone(self):
        """Clone this cube."""
        new = Cube([self[face].clone() for face in "LUFDRB"])
        new.user_data = self.user_data.copy()
        return new



_relations = {
    (-1, -1, -1) : [("L", 6), ("D", 6), ("B", 4)], 
    (-1, -1,  0) : [("L", 5), ("D", 7)], 
    (-1, -1,  1) : [("L", 4), ("F", 6), ("D", 0)], 
    (-1,  0, -1) : [("L", 7), ("B", 3)], 
    (-1,  0,  0) : [("L", 8)], 
    (-1,  0,  1) : [("L", 3), ("F", 7)], 
    (-1,  1, -1) : [("L", 0), ("U", 0), ("B", 2)], 
    (-1,  1,  0) : [("L", 1), ("U", 7)], 
    (-1,  1,  1) : [("L", 2), ("U", 6), ("F", 0)], 
    ( 0, -1, -1) : [("D", 5), ("B", 5)], 
    ( 0, -1,  0) : [("D", 8)], 
    ( 0, -1,  1) : [("F", 5), ("D", 1)], 
    ( 0,  0, -1) : [("B", 8)], 
    ( 0,  0,  0) : [], 
    ( 0,  0,  1) : [("F", 8)], 
    ( 0,  1, -1) : [("U", 1), ("B", 1)], 
    ( 0,  1,  0) : [("U", 8)], 
    ( 0,  1,  1) : [("U", 5), ("F", 1)], 
    ( 1, -1, -1) : [("D", 4), ("R", 4), ("B", 6)], 
    ( 1, -1,  0) : [("D", 3), ("R", 5)], 
    ( 1, -1,  1) : [("F", 4), ("D", 2), ("R", 6)], 
    ( 1,  0, -1) : [("R", 3), ("B", 7)], 
    ( 1,  0,  0) : [("R", 8)], 
    ( 1,  0,  1) : [("F", 3), ("R", 7)], 
    ( 1,  1, -1) : [("U", 2), ("R", 2), ("B", 0)], 
    ( 1,  1,  0) : [("U", 3), ("R", 1)], 
    ( 1,  1,  1) : [("U", 4), ("F", 2), ("R", 0)]
}

class _CubeAsGraph(dict):

    """
    Cube in graph notation.
    """

    def __init__(self, cube):
        super(_CubeAsGraph, self).__init__()
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    node = _Cuboid(x, y, z)
                    self[node] = set()
                    for axis in "xyz":
                        for _ in [-1, 1]:
                            val = node._asdict()[axis] + _
                            if abs(val) <= 1:
                                self[node].add(node._replace(**{axis:val}))
                    for face, index in _relations[node]:
                        sqr_nbr = _Square(face, index, cube[face][index].colour)
                        self[node].add(sqr_nbr)
                        self[sqr_nbr] = {node}
                        if len(_relations[node]) != 1:
                            for _ in [-1, 1]:
                                self[sqr_nbr].add( sqr_nbr._replace( index = (index + _)%8, colour = cube[face][(index + _)%8].colour ) )
                            if len(_relations[node]) == 2:
                                self[sqr_nbr].add( sqr_nbr._replace( index=8, colour=cube[face].centre.colour ) )
                        else:
                            for _ in range(1, 8, 2):
                                self[sqr_nbr].add( sqr_nbr._replace(index=_, colour=cube[face][index].colour) )

    def __repr__(self):
        result = ("=" * 70 + "\n") * 2
        cuboids = filter(lambda x:x.type == "Cuboid", self.keys())
        squares = filter(lambda x:x.type == "Square", self.keys())
        for cos in [cuboids, squares]:
            for key in sorted(cos):
                value = self[key]
                result += "{0}:\n".format(key)
                _cuboids = filter(lambda x:x.type == "Cuboid", value)
                _squares = filter(lambda x:x.type == "Square", value)
                for c, s in zip_longest(_cuboids, _squares, fillvalue=""):
                    result += "    {0!s: <25} {1!s: <45}\n".format(c, s)
                result += "\n"
        return result


