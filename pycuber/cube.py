from .formula import *
from .util import FrozenDict
from functools import reduce
from itertools import permutations


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
        self.children = set(children)

    def __repr__(self):
        """
        Print out two spaces with background colour.
        """
        return {
                   "red": "\x1b[45m",
                   "yellow": "\x1b[43m",
                   "green": "\x1b[42m",
                   "white": "\x1b[47m",
                   "orange": "\x1b[41m",
                   "blue": "\x1b[46m",
                   "unknown": "\x1b[40m",
               }[self.colour] + "  \x1b[49m"

    def __str__(self):
        """
        Return self as the raw color represented by a single character
        """
        return {
                "red": "[r]",
                "yellow": "[y]",
                "green": "[g]",
                "white": "[w]",
                "orange": "[o]",
                "blue": "[b]",
                "unknown": "[u]",
            }[self.colour]

    def __eq__(self, another):
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
            "red": 0xFF0000,
            "yellow": 0xFFFF00,
            "green": 0x00FF00,
            "white": 0xFFFFFF,
            "orange": 0xFFA500,
            "blue": 0x0000FF,
            "unknown": 0x000000
        }
        return hash(str(self)) + colour_to_hex[self.colour]

    def copy(self):
        """
        Copy this Square.
        """
        return Square(self.colour)


class Cubie(object):
    """
    Cubie(**kwargs), implements a cubie on the Cube.
    ex: Cubie(U=Square("yellow"), F=Square("green"), L=Square("red"))
    """

    def __init__(self, parent=None, children=[], **kwargs):
        super(Cubie, self).__init__()
        for kw in kwargs:
            if kw not in list("LUFDRB"):
                raise ValueError(
                    "Facings must be L U F D R B, not {0}."
                        .format(kw),
                )
            elif isinstance(kwargs[kw], str):
                kwargs[kw] = Square(kwargs[kw])
        self.facings = FrozenDict(kwargs)
        self.parent = parent
        self.children = set(children)
        self.location = "".join(kwargs)

    def __repr__(self):
        """
        Print out "Cubie(U:\x1b[43m ...)"
        """
        return "{0}({1})".format(
            self.__class__.__name__,
            ", ".join("{0}: {1}".format(k, v) for k, v in self.facings.items())
        )

    def __getitem__(self, face):
        """
        Cubie["L"] => Returns the square that positioned at L face.
        """
        if face in "LUFDRB":
            return self.facings[face]
        for k, sq in self:
            if sq in (face, Square(face)):
                return k
        raise KeyError(face)

    def __hash__(self):
        """
        Cubie object is hashable.
        """
        return reduce(
            lambda x, y: hash(x) + hash(y),
            self.facings.values(),
            list(self.facings.values())[0],
        ) // hash(self.__class__.__name__)

    def __eq__(self, another):
        """
        Check if two Cubies are the same.
        """
        if isinstance(another, Cubie):
            return self.facings == another.facings
        return False

    def __ne__(self, another):
        """
        Check if two Cubies are different.
        """
        return not self.__eq__(another)

    def __contains__(self, value):
        """
        Check if the Cubie uses that face.
        """
        return value in self.facings

    def __or__(self, value):
        """
        Check if the Cubie uses that colour.
        """
        try:
            return Square(value) in self.facings.values()
        except ValueError:
            return False

    def __and__(self, another):
        """
        Check if two Cubies have the same location.
        """
        if isinstance(another, str):
            return tuple(self.facings) in permutations(another, len(another))
        try:
            return self.facings.viewkeys() == another.facings.viewkeys()
        except AttributeError:
            return self.facings.keys() == another.facings.keys()

    def __iter__(self):
        """
        Iterate over every (face, square) pair.
        """
        return iter(self.facings.items())

    def copy(self):
        """
        Copy this Cubie.
        """
        try:
            new = {
                "centre": Centre,
                "edge": Edge,
                "corner": Corner,
            }[self.type](
                parent=self.parent,
                children=self.children,
                **self.facings
            )
        except AttributeError:
            new = Cubie(
                parent=self.parent,
                children=self.children,
                **self.facings
            )
        return new


class Centre(Cubie):
    """
    Centre(U=Square("yellow")) => Implements the "Centre Block" (has 1 sticker).
    """

    def __init__(self, parent=None, children=[], **kwargs):
        if len(kwargs) != 1:
            raise ValueError("A Centre has 1 Square, got {0}.".format(len(kwargs)))
        super(Centre, self).__init__(parent, children, **kwargs)
        self.type = "centre"
        self.face = list(kwargs.keys())[0]

    @property
    def colour(self):
        return list(self.facings.values())[0].colour


class Edge(Cubie):
    """
    Edge(U=Square("yellow"), F=Square("green")) => Implements the "Edge Block" (has 2 stickers).
    """

    def __init__(self, parent=None, children=[], **kwargs):
        if len(kwargs) != 2:
            raise ValueError("An Edge has 2 Squares, got {0}.".format(len(kwargs)))
        super(Edge, self).__init__(parent, children, **kwargs)
        self.type = "edge"


class Corner(Cubie):
    """
    Corner(
        U=Square("yellow"), 
        F=Square("green"), 
        R=Square("orange"), 
        ) => Implements the "Corner Block" (has 3 stickers).
    """

    def __init__(self, parent=None, children=[], **kwargs):
        if len(kwargs) != 3:
            raise ValueError("A Corner has 3 Squares, got {0}.".format(len(kwargs)))
        super(Corner, self).__init__(parent, children, **kwargs)
        self.type = "corner"


class Cube(object):
    """
    Cube([, {a set of Cubies}]) => Implements a Rubik's Cube.
    """

    def __init__(self, cubies=None):
        super(Cube, self).__init__()
        self.parent = None
        self.children = set()
        if not cubies:
            cubies = set()
            colours = {"L": "red", "U": "yellow", "F": "green", "D": "white", "R": "orange", "B": "blue"}
            for loc in [
                "LDB", "LDF", "LUB", "LUF", "RDB", "RDF", "RUB", "RUF",
                "LB", "LF", "LU", "LD", "DB", "DF", "UB", "UF", "RB", "RF", "RU", "RD",
                "L", "R", "U", "D", "F", "B",
            ]:
                if len(loc) == 3:
                    cubies.add(Corner(**{loc[i]: Square(colours[loc[i]]) for i in range(3)}))
                elif len(loc) == 2:
                    cubies.add(Edge(**{loc[i]: Square(colours[loc[i]]) for i in range(2)}))
                else:
                    cubies.add(Centre(**{loc[0]: Square(colours[loc[0]])}))
        cubies = set(cubies)
        if isinstance(cubies, set):
            for cubie in cubies:
                if isinstance(cubie, Cubie):
                    children = set()
                    for sqr in cubie.facings.values():
                        children.add(Square(sqr))
                    if len(cubie.location) == 3:
                        child_class = Corner
                    elif len(cubie.location) == 2:
                        child_class = Edge
                    elif len(cubie.location) == 1:
                        child_class = Centre
                    self.children.add(child_class(parent=self, children=children, **cubie.facings))
                else:
                    raise ValueError("Should use Cubie, not {0}.".format(cubie.__class__.__name__))

    def __repr__(self):
        """
        Draw the Cube as expanded view.
        """
        result = ""
        _ = {
            "L": self.L,
            "U": self.U,
            "F": self.F,
            "D": self.D,
            "R": self.R,
            "B": self.B,
        }
        for i in range(3):
            result += "      " + "".join(repr(square) for square in _["U"][i]) + "\n"
        for i in range(3):
            for side in "LFRB":
                result += "".join(repr(square) for square in _[side][i])
            result += "\n"
        for i in range(3):
            result += "      " + "".join(repr(square) for square in _["D"][i]) + "\n"
        return result

    def __str__(self):
        """
        Draw the Cube as expanded view using string representation of color.
        """
        result = ""
        _ = {
            "L": self.L,
            "U": self.U,
            "F": self.F,
            "D": self.D,
            "R": self.R,
            "B": self.B,
        }
        for i in range(3):
            result += "         " + "".join(str(square) for square in _["U"][i]) + "\n"
        for i in range(3):
            for side in "LFRB":
                result += "".join(str(square) for square in _[side][i])
            result += "\n"
        for i in range(3):
            result += "         " + "".join(str(square) for square in _["D"][i]) + "\n"
        return result

    def __getitem__(self, key):
        """
        Get specific Cubie by location.
        """
        for child in self.children:
            if child & key:
                return child
        raise KeyError(str(key))

    def __setitem__(self, key, value):
        """
        Reset a specific Cubie.
        """
        if self[key].type != value.type:
            raise ValueError(
                "Replacement of {0} must be {1}, not {2}."
                    .format(key, self[key].type, value.type),
            )
        if not self[key] & value:
            raise ValueError(
                "Location must be {0}, not {1}."
                    .format(key, value.location),
            )
        q = self[key]
        self.children.remove(q)
        q.facings = value.facings
        q.children = set(value.facings.values())
        self.children.add(q)

    def __getattr__(self, name):
        """
        Returns the face from Cube.get_face() if the name is L U F D R or B.
        """
        if name in list("LUFDRB"):
            return self.get_face(name)
        else:
            return super(Cube, self).__getattribute__(name)

    def __call__(self, algo):
        """
        A shortcut for Cube.perform_algo().
        """
        return self.perform_algo(algo)

    def __iter__(self):
        """
        Iterate over every Cubie in the Cube.
        """
        result = []
        for loc in [
            "BDL", "FDL", "ULF", "ULB", "RUF", "RUB", "RDB", "RDF",
            "LU", "FU", "RU", "BU", "LF", "LB", "RF", "RB", "FD", "LD", "BD", "RD",
            "F", "U", "R", "L", "D", "B"
        ]:
            result.append((loc, self[loc]))
        return iter(result)

    def __eq__(self, another):
        """
        Check if two Cubes are the same.
        """
        return dict(self) == dict(another)

    def __ne__(self, another):
        """
        Check if two Cubes aren't the same.
        """
        return not self.__eq__(another)

    def at_face(self, face):
        """
        Find all Cubies which have a Square on specific face.
        """
        return set(
            child for child in self.children
            if face in child.location
        )

    def has_colour(self, colour):
        """
        Find all Cubies which has a specific colour(s).
        """
        return set(
            child for child in self.children
            if colour in map(
                lambda x: x.colour,
                child.children,
            )
        )

    def select_type(self, tp):
        """
        Find all Cubies which has the specific type.
        """
        return set(
            child for child in self.children
            if tp == child.type
        )

    def get_face(self, face):
        """
        Getting specific face on a Cube.
        Returns as a 2D list.
        """
        if face not in [
            "L", "U", "F", "D", "R", "B",
            "left", "up", "front", "down", "right", "back"
        ]:
            raise ValueError("Face must be L U F D R B, not {0}.".format(face))
        elif face.islower():
            face = face[0].upper()
        result = [[None] * 3, [None] * 3, [None] * 3]
        ordering = {
            "L": "UDBF",
            "R": "UDFB",
            "U": "BFLR",
            "D": "FBLR",
            "F": "UDLR",
            "B": "UDRL",
        }[face]
        for cubie in self.at_face(face):
            loc = [None, None]
            for f in cubie.facings:
                if cubie.type == "centre":
                    loc = [1, 1]
                if f != face:
                    if cubie.type == "edge":
                        loc[ordering.index(f) // 2] = (ordering.index(f) % 2) * 2
                        loc[loc.index(None)] = 1
                    elif cubie.type == "corner":
                        loc[ordering.index(f) // 2] = (ordering.index(f) % 2) * 2
            result[loc[0]][loc[1]] = cubie.facings[face]
        return result

    def _single_layer(self, step):
        """
        Helper function for Cube.perform_step().
        Perform single layer steps.
        """
        step = Step(step)
        movement = {
            "U": "RFLB",
            "D": "LFRB",
            "R": "FUBD",
            "L": "FDBU",
            "F": "URDL",
            "B": "ULDR",
            "M": ("LR", "FDBU"),
            "S": ("FB", "URDL"),
            "E": ("UD", "LFRB"),
        }[step.face]
        if len(movement) == 2: slice_, movement = movement
        if step.is_counter_clockwise: movement = movement[::-1]
        if step.face not in "MSE":
            to_move = {c.copy() for c in self.at_face(step.face)}
        else:
            to_move = {
                c.copy()
                for c in (self.children - self.at_face(slice_[0]) - self.at_face(slice_[1]))
                }
        for cubie in to_move:
            new = {}
            for f in cubie.facings:
                if f != step.face:
                    new[movement[(movement.index(f) + step.is_180 + 1) % 4]] = cubie.facings[f]
                else:
                    new[f] = cubie.facings[f]
            new_cubie = {
                "centre": Centre,
                "edge": Edge,
                "corner": Corner,
            }[cubie.type](
                parent=self,
                children=new.values(),
                **new
            )
            self[new_cubie.location] = new_cubie
        return self

    def _other_rotations(self, step):
        """
        Helper function for Cube.perform_step().
        Perform wide rotations or cube rotations.
        """
        step = Step(step)
        movement = {
            "x": ["L'", "M'", "R"],
            "y": ["U", "E'", "D'"],
            "z": ["F", "S", "B'"],
            "r": ["R", "M'"],
            "l": ["L", "M"],
            "u": ["U", "E'"],
            "d": ["D", "E"],
            "f": ["F", "S"],
            "b": ["B", "S'"],
        }[step.face]
        for s in movement:
            step_ = Step(s)
            if step.is_counter_clockwise:
                step_ = step_.inverse()
            elif step.is_180:
                step_ = step_ * 2
            _single_layer(self, step_)
        return self

    _other_rotations.__globals__["_single_layer"] = _single_layer

    def perform_step(self, step):
        """
        Perform a Rubik's Cube step.
        Using "Singmaster Notation"
        L R U D F B
        l r u d f b
        M S E
        x y z
        """
        step = Step(step)
        if step.face in "LUFDRBMES":
            return _single_layer(self, step)
        else:
            return _other_rotations(self, step)

    perform_step.__globals__["_single_layer"] = _single_layer
    perform_step.__globals__["_other_rotations"] = _other_rotations
    del _single_layer, _other_rotations

    def perform_algo(self, algo):
        """
        Perform a Rubik's Cube Formula.
        Using "Singmaster notation".
        """
        formula = Formula(algo)
        for step in formula:
            self.perform_step(step)
        return self

    def which_face(self, colour):
        """
        Get the specific face (face name) which has that colour for the centre block.
        """
        for centre in [self[face] for face in "LUFDRB"]:
            if type(colour) == str:
                if centre.colour == colour:
                    return centre.face
            else:
                if centre.colour == colour.colour:
                    return centre.face
        raise KeyError(colour)

    def is_valid(self):
        """
        Check if Cube is solvable.
        """
        opposite = {self[f][f]: self[op_f][op_f] for f, op_f in zip("UDLRFB", "DURLBF")}
        if len(opposite) != 6 or Square("unknown") in opposite:
            return False
        checked_cubies = set()
        edge_total = corner_total = 0
        graph = {"edges": {}, "corners": {}}
        for c_loc, cubie in self:
            for face, square in cubie:
                for _face, _square in cubie:
                    if face != _face:
                        if square == _square: return False
                        if _square == opposite[square]: return False
            if len(c_loc) == 3:
                ordering = "LFRB"
                selected_face = "U"
                if "D" in cubie: ordering, selected_face = "BRFL", "D"
                if cubie[selected_face] not in (self["U"]["U"], self["D"]["D"]):
                    idx = sorted([f for f, s in cubie if f != selected_face], key=lambda x: ordering.index(x))
                    if "B" in idx and "L" in idx: idx = idx[::-1]
                    if cubie[idx[0]] in (self["U"]["U"], self["D"]["D"]):
                        corner_total += 2
                    else:
                        corner_total += 1
                graph["corners"][c_loc] = "".join([self.which_face(s) for f, s in cubie])
            elif len(c_loc) == 2:
                if "U" in cubie:
                    selected_square = "U"
                elif "D" in cubie:
                    selected_square = "D"
                elif "L" in cubie:
                    selected_square = "L"
                elif "R" in cubie:
                    selected_square = "R"
                if cubie[selected_square] not in (self["U"]["U"], self["D"]["D"]):
                    if cubie[c_loc.replace(selected_square, "", 1)] not in (self["U"]["U"], self["D"]["D"]):
                        if cubie[selected_square] not in (self["L"]["L"], self["R"]["R"]):
                            edge_total += 1
                    else:
                        edge_total += 1
                graph["edges"][c_loc] = "".join([self.which_face(s) for f, s in cubie])
            checked_cubies.add(frozenset(cubie.facings.values()))
        if len(checked_cubies) != 26: return False
        if corner_total % 3 != 0: return False
        if edge_total % 2 != 0: return False
        parities = 0
        for cubies in graph.values():
            path = []
            remainings = set(cubies)
            while True:
                if path:
                    next_one = cubies[path[-1]]
                    for p in permutations(next_one):
                        if "".join(p) in cubies:
                            next_one = "".join(p)
                            break
                    try:
                        remainings.remove(next_one)
                        path.append(next_one)
                    except KeyError:
                        if len(path) % 2 != 1:
                            parities += 1
                        path = []
                else:
                    if remainings:
                        path.append(remainings.pop())
                    else:
                        break
        if parities % 2 != 0: return False
        return True

    def copy(self):
        """
        Copy this Cube.
        """
        return Cube({c[1].copy() for c in self})
