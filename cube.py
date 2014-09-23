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

from algorithm import *
from collections import namedtuple
Cuboid = namedtuple("Cuboid", ["x", "y", "z"])
Cuboid.type = "Cuboid"
Square = namedtuple("Square", ["face", "index", "colour"])
Square.type = "Square"


class Square:

    """
    Square(colour, face, index), implements a square (sticker) on a cube.
    """

    def __init__(self, colour):
        self.colour = colour
        self.user_data = {}

    def __repr__(self):
        return {"red":"\x1b[45m", "yellow":"\x1b[43m", "green":"\x1b[42m", "white":"\x1b[47m", "orange":"\x1b[41m", "blue":"\x1b[46m"}[self.colour] + "  \x1b[49m"

    def clone(self):
        """Clone a Square from another Square"""
        new = Square(self.colour)
        new.user_data = self.user_data.copy()
        return new



class Face:

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



class Cube:

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


    _olr_patterns = {
        "L": "UL FL DL BR", 
        "U": "BU RU FU LU", 
        "F": "LR UD RL DU", 
        "D": "LD FD RD BD", 
        "R": "DR FR UR BL", 
        "B": "RR UU LL DD"
    }

    def _outer_layer_rotate(self, symbol):
        """Perform the actions like U R' D2 L' """
        self[symbol[0]].rotate("'" in symbol)
        rows = [self[p[0]].get_row(p[1]) for p in self._olr_patterns[symbol[0]].split()]
        copy = [[sqr.clone() for sqr in a_row] for a_row in rows]
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                rows[i][j].colour = copy[(i + ("'" in symbol) * 2 - 1) % 4][j].colour
        if len(symbol) == 2 and symbol[1] == "2":
            self._outer_layer_rotate(symbol[0])

    _cr_patterns = {
        "x": (["F", 0, "U", 2, "B", 2, "D", 0, "F"], "RL"), 
        "y": (["L", 0, "B", 0, "R", 0, "F", 0, "L"], "UD"), 
        "z": (["U", 1, "R", 1, "D", 1, "L", 1, "U"], "FB")
    }

    def _cube_rotation(self, symbol):
        """Perform the actions like x y' z2 """
        self[self._cr_patterns[symbol[0]][1][0]].rotate("'" in symbol)
        self[self._cr_patterns[symbol[0]][1][1]].rotate("'" not in symbol)
        change = self._cr_patterns[symbol[0]][0][::("'" not in symbol)*2-1]
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

    _dlr_patterns = {
        "l": ["x'", "R"], 
        "u": ["y", "D"], 
        "f": ["z", "B"], 
        "d": ["y'", "U"], 
        "r": ["x", "L"], 
        "b": ["z'", "F"]
    }

    def _double_layers_rotate(self, symbol):
        """Perform the actions like u r' d2 l' """
        actions = self._dlr_patterns[symbol[0]][:]
        if "'" in symbol:
            if "'" in actions[0]: actions[0] = actions[0][0]
            else: actions[0] = actions[0] + "'"
            actions[1] += "'"
        elif "2" in symbol:
            for i in range(2): actions[i] = actions[i][0] + "2"
        self._cube_rotation(actions[0])
        self._outer_layer_rotate(actions[1])

    _mlr_patterns = {
        "M": "l", 
        "S": "f", 
        "E": "d"
    }

    def _middle_layer_rotate(self, symbol):
        """Perform the actions like M S' E2"""
        self._double_layers_rotate(self._mlr_patterns[symbol[0]] + symbol[1:])
        olr_adds = "" if "'" in symbol else "2" if "2" in symbol else "'"
        self._outer_layer_rotate(self._mlr_patterns[symbol[0]].upper() + olr_adds)

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

    def clone(self):
        """Clone this cube."""
        new = Cube([self[face].clone() for face in "LUFDRB"])
        new.user_data = self.user_data.copy()
        return new



class _CubeAsGraph(dict):
    """
    Cube in graph notation.
    """
    def __repr__(self):
        result = ""
        for key in self:
            result += "{0} -> {1}\n".format(key, self[key])
        return result
