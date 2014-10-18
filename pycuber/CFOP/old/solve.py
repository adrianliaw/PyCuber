"""
This is the module of solving the cube.

Every step of solving the cube are in this module.
"""

import _import
from cube import *
from sps import *
from pll import *
from pll_recog import *
from oll import *
from oll_recog import *
from cross import *
from f2l import *

def look_around(cube, goal, f):
    """
    This function is to perform the algorithm if it's the given case, return None otherwise.

    Walk through every cube rotation(y) and the U face turning,
    and check if the given cube is "goal", which is the recognize function,
    if it is, perform the algorithm, return the full action and the cube after performing the alg,
    the function f is the function of the algorithm.

    This function is to use in solving the last layer, so recognize it and perform algorithm.
    """
    for cube_rotate in [None, y, yi, y2]:
        for U_orient in [None, U, Ui, U2]:
            if U_orient:
                if cube_rotate:
                    new = U_orient(cube_rotate(cube))
                else:
                    new = U_orient(cube)
            else:
                if cube_rotate:
                    new = cube_rotate(cube)
                else:
                    new = [[[p for p in q] for q in r] for r in cube]
            if goal(new):
                cr_notation = [cube_rotate.__name__] if cube_rotate else []
                uo_notation = [U_orient.__name__] if U_orient else []
                algo = f.__doc__.replace("\n\t", "", 2).replace("'", "i", 1000).split()
                return cr_notation + uo_notation + algo

def is_solved_cube(cube):
    """
    Check if the cube is solved.
    """
    for i in range(len(cube)):
        for j in range(len(cube[i])):
            for q in range(len(cube[i][j])):
                if cube[i][j][q] != cube[i][1][1]:
                    return False
    return True

def is_solved_cross(state):
    """
    Check if the cross is solved (cross on D face).
    """
    c = state[3][1][1]
    return state[3][0][1] == c and state[3][1][0] == c and state[3][1][2] == c and state[3][2][1] == c and state[0][2][1] == state[0][2][2] and state[2][2][1] == state[2][1][1] and state[4][2][1] == state[4][1][1] and state[5][2][1] == state[5][1][1]

def is_solved_f2l(cube):
    """
    check if the first two layers are solved.
    """
    for p in cube[3]:
        for q in p:
            if q != cube[3][1][1]:
                return False
    for p in [cube[0], cube[2], cube[4], cube[5]]:
        if [p[1], p[2]] != [[p[1][1]] * 3] * 2:
            return False
    return True

def is_solved_oll(cube):
    """
    Check if the OLL is solved.
    """
    if is_solved_f2l(cube):
        if cube[1] == [[cube[1][1][1]] * 3] * 3:
            return True
    return False

def scramble():
    """
    Randomly scramble a cube (25 steps), returns a string (sequence of the actions).
    """
    import random
    before2_move = ""
    last_move = ""
    actions = ["%s%s" % (name, direction) for name in "LUFDRB" for direction in ["", "i", "2"]]
    opposite = {'L':'R', 'U':'D', 'F':'B', 'D':'U', 'R':'L', 'B':'F'}
    shuffled = []
    for i in range(25):
        last_act_removed = actions[:]
        if last_move:
            last_act_removed.remove(last_move[0])
            last_act_removed.remove(last_move[0]+"i")
            last_act_removed.remove(last_move[0]+"2")
        if before2_move:
            if opposite[before2_move[0]] == last_move[0]:
                last_act_removed.remove(before2_move[0])
                last_act_removed.remove(before2_move[0]+"i")
                last_act_removed.remove(before2_move[0]+"2")
        act = random.choice(last_act_removed)
        last_move, before2_move = act, last_move
        shuffled.append(act)
    return shuffled


def solve_cross(c):
    """
    Solve the cross by A* searching algorithm.
    """
    return path_actions(a_star_search(fetch_edges(c), cross_successors, cross_state_value, cross_goal))

def solve_f2l(cube):
    result = []
    c = [[[z for z in y] for y in x] for x in cube]
    for i in range(4):
        _ord = order(c)
        pair = _ord[i]
        alg = solve_f2l_pair(c, pair)
        result += alg
        c = sequence(alg, c)
    return result

def solve_oll(c):
    """
    Solve the OLL by look_around function (loop over every 57 OLL cases).
    """
    if is_solved_f2l(c):
        for i in range(58):
            result = eval("look_around(%s, O%02d_recog, O%02d)" % (str(c), i, i))
            if result != None: return result
        raise ValueError("Not a solvable OLL case.")
    raise ValueError("Non-solved F2L.")

def solve_pll(cube):
    """
    Solve the PLL by look_around function (loop over every 21 cases).
    """
    if not is_solved_oll(cube):
        raise ValueError("Non-solved OLL or F2L")
    for p in ["None", "Aa", "Ab", "E", "Ua", "Ub", "H", "Z", "Ja", "Jb", "T", "Ra", "Rb", "F", "V", "Na", "Nb", "Y", "Ga", "Gb", "Gc", "Gd"]:
        result = eval("look_around(%s, %s_recog, %s_perm)" % (str(cube), p, p))
        if result != None:
            return result
    raise ValueError("Not a solvable pll case.")

def solve_cube(cube):
    """
    Solve the scrambled cube by CFOP method.
    """
    _cube = [[[z for z in y] for y in x] for x in cube]
    result = []
    C = solve_cross(_cube)
    result += C
    _cube = sequence(C, _cube)
    F = solve_f2l(_cube)
    result += F
    _cube = sequence(F, _cube)
    O = solve_oll(_cube)
    result += O
    _cube = sequence(O, _cube)
    P = solve_pll(_cube)
    result += P
    _cube = sequence(P, _cube)
    return result

wide_action = {
    "l":["R", "xi"], 
    "r":["L", "x"], 
    "u":["D", "y"], 
    "d":["U", "yi"], 
    "f":["B", "z"], 
    "b":["F", "zi"], 
    "M":["R", "Li", "xi"], 
    "S":["Fi", "B", "z"], 
    "E":["U", "Di", "yi"]
}

def optimize_wide_action(alg):
    """
    Optimize the wide action (lowercase letter action) and middle layer action 
    into single layer and cube rotation.
    """
    result = []
    for act in alg:
        if act[0] in "lrudfbMSE":
            new_action = wide_action[act[0]][:]
            for i in range(len(new_action)):
                if not act[1:]:
                    pass
                elif act[1] == "i":
                    if len(new_action[i]) == 2:
                        new_action[i] = new_action[i][0]
                    elif len(new_action[i]) == 1:
                        new_action[i] += "i"
                elif act[1] == "2":
                    new_action[i] = new_action[i][0] + "2"
            result += new_action
        else:
            result.append(act)
    return result

rotationless = {
    "x": {
        "U":"F", 
        "D":"B", 
        "R":"R", 
        "L":"L", 
        "F":"D", 
        "B":"U"
    }, 
    "y": {
        "U":"U", 
        "D":"D", 
        "F":"R", 
        "B":"L", 
        "R":"B", 
        "L":"F"
    }, 
    "z": {
        "U":"L", 
        "D":"R", 
        "F":"F", 
        "B":"B", 
        "R":"U", 
        "L":"D"
    }
}

def optimize_rotationless(alg):
    """
    Make the solving rotationless, so in the full solve we won't see any x, y, or z.
    """
    result = []
    for i in range(len(alg)-1, -1, -1):
        if alg[i][0] in "xyz":
            for q in range(len(result)):
                if not alg[i][1:]:
                    result[q] = rotationless[alg[i]][result[q][0]] + result[q][1:]
                elif alg[i][1:] == "i":
                    for (key, value) in rotationless[alg[i][0]].items():
                        if value == result[q][0]:
                            result[q] = key + result[q][1:]
                            break
                elif alg[i][1:] == "2":
                    result[q] = rotationless[alg[i][0]][rotationless[alg[i][0]][result[q][0]]] + result[q][1:]
        else:
            result.append(alg[i])
    result.reverse()
    return result

def optimize_same_side(alg):
    """
    Optimize the repeated action, 
    ex: ["R", "R2", "U", "Di", "U"] => ["Ri", "U2", "Di"]
    """
    result = []
    last_move = " "
    before2_move = " "
    opposite = {'L':'R', 'U':'D', 'F':'B', 'D':'U', 'R':'L', 'B':'F'}
    for i in range(len(alg)):
        if alg[i][0] == last_move[0]:
            val = 0
            for act in (alg[i], last_move):
                if not act[1:]:
                    val += 1
                elif act[1:] == "i":
                    val += 3
                else:
                    val += 2
            if val % 4 == 0:
                del result[-1]
                if result:
                    last_move = result[-1]
            elif val % 4 == 1:
                result[-1] = result[-1][0]
                last_move = result[-1]
            elif val % 4 == 2:
                result[-1] = result[-1][0] + "2"
                last_move = result[-1]
            else:
                result[-1] = result[-1][0] + "i"
                last_move = result[-1]
        elif alg[i][0] == before2_move[0] and alg[i][0] == opposite[last_move[0]]:
            val = 0
            for act in (alg[i], before2_move):
                if not act[1:]:
                    val += 1
                elif act[1:] == "i":
                    val += 3
                else:
                    val += 2
            if val % 4 == 0:
                del result[-2]
                if len(result) == 1:
                    last_move = result[-1]
                    before2_move = " "
                else:
                    last_move, before2_move = result[-1], result[-2]
            elif val % 4 == 1:
                result[-2] = result[-2][0]
                before2_move = result[-2]
            elif val % 4 == 2:
                result[-2] = result[-2][0] + "2"
                before2_move = result[-2]
            else:
                result[-2] = result[-2][0] + "i"
                before2_move = result[-2]
        else:
            result.append(alg[i])
            last_move, before2_move = result[-1], last_move
    return result

def optimize(alg):
    """
    Optimize the algorithm, including three steps.
    """
    return optimize_same_side(optimize_rotationless(optimize_wide_action(alg)))

def full_solve(cube):
    """
    The optimized CFOP solution.
    """
    return optimize(solve_cube(cube))

def structured_solving(cube):
    """
    Solve a cube and returns a dictionary, 
    {"C" : [ cross solving ], 
     "F" : [ { "colors" : [ color1, color2 ] , "solve" : [ pair solving ] }... ], 
     "O" : [ OLL solving ], 
     "P" : [ PLL solving ]}
    """
    _cube = [[[z for z in y] for y in x] for x in cube]
    solving = {}
    C = solve_cross(_cube)
    _cube = sequence(C, _cube)
    solving["C"] = C
    solving["F"] = []
    for i in range(4):
        solving["F"].append({})
        _ord = order(_cube)
        pair = _ord[i]
        solving["F"][i]["colors"] = list(pair)
        alg = solve_f2l_pair(_cube, pair)
        solving["F"][i]["solve"] = alg
        _cube = sequence(alg, _cube)
    O = solve_oll(_cube)
    _cube = sequence(O, _cube)
    solving["O"] = O
    P = solve_pll(_cube)
    solving["P"] = P
    return solving

def scramble_and_solve(structure=False):
    """
    This function is for testing and look prettier, scramble and solving are in this function.
    """
    a = ' '.join(scramble())
    print "SCRAMBLE:", a.replace("i", "'", 25)
    print
    if structure:
        s = structured_solving(sequence(a, initial_cube()))
        print "CROSS:   ", ' '.join(s["C"]).replace("i", "'", 10)
        for i in range(4):
            print "F2L#%d:   " % (i+1), ' '.join(s["F"][i]["solve"]).replace("i", "'", 10)
        print "OLL:     ", ' '.join(s["O"]).replace("i", "'", 20)
        print "PLL:     ", ' '.join(s["P"]).replace("i", "'", 20)
        s = full_solve(sequence(a, initial_cube()))
        print
        print "FULL:    ", ' '.join(s[:36]).replace("i", "'", 40)
        print "         ", ' '.join(s[36:]).replace("i", "'", 40)
    else:
        s = full_solve(sequence(a, initial_cube()))
        print "SOLVE:   ", ' '.join(s[:36]).replace("i", "'", 40)
        print "         ", ' '.join(s[36:]).replace("i", "'", 40)

def input_and_solve(cube, structure=False):
    """
    This function is for testing and look prettier, only includes solving, this cube is the perameter.
    """
    if type(cube) == str:
        from color_converter import color_convert
        cube = color_convert(cube)
    if structure:
        s = structured_solving(cube)
        print "CROSS:   ", ' '.join(s["C"]).replace("i", "'", 10)
        for i in range(4):
            print "F2L#%d:   " % (i+1), ' '.join(s["F"][i]["solve"]).replace("i", "'", 10)
        print "OLL:     ", ' '.join(s["O"]).replace("i", "'", 20)
        print "PLL:     ", ' '.join(s["P"]).replace("i", "'", 20)
        s = full_solve(cube)
        print
        print "FULL:    ", ' '.join(s[:36]).replace("i", "'", 40)
        print "         ", ' '.join(s[36:]).replace("i", "'", 40)
    else:
        s = full_solve(cube)
        print "SOLVE:   ", ' '.join(s[:36]).replace("i", "'", 40)
        print "         ", ' '.join(s[36:]).replace("i", "'", 40)

if __name__ == "__main__":
    while True:
        a = raw_input("Do you need a scramble? (y/n)")
        if a == "q":
            exit()
        if a not in "yn":
            print "Please answer \"y\" or \"n\".\n\"q\" to quit."
        else: break
    while True:
        b = raw_input("Do you need the structure of the solving? (y/n)")
        if b == "q":
            exit()
        if b not in "yn":
            print "Please answer \"y\" or \"n\".\n\"q\" to quit."
        else: break
    if a == "y":
        if b == "y":
            scramble_and_solve(True)
        else:
            scramble_and_solve(False)
    else:
        while True:
            c = raw_input("Please enter the state of the cube:")
            if c == "q":
                exit()
            try:
                if b == "y":
                    input_and_solve(c, True)
                else:
                    input_and_solve(c, False)
                break
            except:
                print "Invalid input.\nPlease enter a string of 54 characters by [0-5] or [LUFDRB].\n\"q\" to quit."
