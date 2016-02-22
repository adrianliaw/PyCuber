def fill_unknowns(s):
    """
    Take a set of Cubies as an input, 
    adds "unknown Cubies" to the set.
    """
    from .cube import Centre, Corner, Edge, Square
    new = set()
    for loc in [
        "LBD", "LBU", "LFD", "LFU", "RBD", "RBU", "RFD", "RFU", 
        "DB", "DL", "DF", "DR", "LB", "FL", "FR", "RB", "UB", "UL", "UF", "UR", 
        "L", "R", "U", "D", "F", "B", 
        ]:
        for cubie in s:
            if cubie & loc:
                new.add(cubie)
                break
        else:
            new.add([Centre, Edge, Corner][len(loc) - 1](**{
                face: Square("unknown") for face in loc
                }))
    return new


def extract(l):
    """
    extract([[1, 2, 3], [[2, 3, 4], [5, 6, 7]], 4])
    => [1, 2, 3, 2, 3, 4, 5, 6, 7, 4]
    """
    result = []
    for element in l:
        if type(element) == list:
            result += extract(element)
        else:
            result.append(element)
    return result


def array_to_cubies(l):
    """
    Translate 3x3x6 array into a set cubies.
    array_to_cubies("LLLLLLLLLUUUUUUUUUFFFFFFFFFDDDDDDDDDRRRRRRRRRBBBBBBBBB")
    array_to_cubies("000000000111111111222222222333333333444444444555555555")
    array_to_cubies(["red", "red", "red", ... , "blue", "blue", "blue"])
    array_to_cubies([[["red", "red", "red"], ["red", ...], [...]], [...], [...], [...], [...], [...]])
    => {
        Centre('B': \x1b[46m  \x1b[49m),
        Centre('R': \x1b[41m  \x1b[49m),
        Centre('D': \x1b[47m  \x1b[49m),
        ...
        Corner('U': \x1b[43m  \x1b[49m, 'L': \x1b[45m  \x1b[49m, 'F': \x1b[42m  \x1b[49m),
        Corner('R': \x1b[41m  \x1b[49m, 'B': \x1b[46m  \x1b[49m, 'D': \x1b[47m  \x1b[49m),
        Corner('B': \x1b[46m  \x1b[49m, 'U': \x1b[43m  \x1b[49m, 'L': \x1b[45m  \x1b[49m),
        ...
        Edge('B': \x1b[46m  \x1b[49m, 'L': \x1b[45m  \x1b[49m),
        Edge('U': \x1b[43m  \x1b[49m, 'F': \x1b[42m  \x1b[49m),
        Edge('B': \x1b[46m  \x1b[49m, 'D': \x1b[47m  \x1b[49m),
        ...
        }
    """
    from .cube import Square, Centre, Edge, Corner
    l = extract(l)
    index = [
        "LBU LU LFU LB L LF LBD LD LFD", 
        "LBU BU RBU LU U RU LFU FU RFU", 
        "LFU FU RFU LF F RF LFD FD RFD", 
        "LFD FD RFD LD D RD LBD BD RBD", 
        "RFU RU RBU RF R RB RFD RD RBD", 
        "RBU BU LBU RB B LB RBD BD LBD", 
        ]
    colours = {
        "L": "red", "0": "red", "red": "red", 
        "U": "yellow", "1": "yellow", "yellow": "yellow", 
        "F": "green", "2": "green", "green": "green", 
        "D": "white", "3": "white", "white": "white", 
        "R": "orange", "4": "orange", "orange": "orange", 
        "B": "blue", "5": "blue", "blue": "blue", 
        }
    result = {}
    for face, cubies in zip("LUFDRB", index):
        for c in cubies.split():
            if c not in result:
                result[c] = {}
            result[c][face] = Square(colours[l.pop(0)])
    return {
        [Centre, Edge, Corner][len(cubie) - 1](**cubie) 
        for cubie in result.values()
        }




