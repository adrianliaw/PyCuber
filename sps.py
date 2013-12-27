import cube, color_converter

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = [] # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        print frontier
        path = frontier.pop(0)
        s = path[-1]
        for (action, state) in successors(s, path_actions(path)[-1] if len(path) != 1 else None).items():
            if state not in explored:
                explored.append(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]
    
def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def solved(state):
    return state == [[[c, c, c], [[c, c, c], [c, c, c]]] for c in ["red", "yellow", "green", "white", "orange", "blue"]]

def cross(state):
    c = state[3][1][1]
    return state[3][0][1] == c and state[3][1][0] == c and state[3][1][2] == c and state[3][2][1] == c and state[0][2][1] == state[0][2][2] and state[2][2][1] == state[2][1][1] and state[4][2][1] == state[4][1][1] and state[5][2][1] == state[5][1][1]

def cube_successors(state, last_action = None):
    successors = {}
    acts = ["F", "Fi", "F2", "U", "Ui", "U2", "R", "Ri", "R2", "L", "Li", "L2", "B", "Bi", "B2", "D", "Di", "D2"]
    if last_action:
        acts.remove(last_action[0])
        acts.remove(last_action[0] + "i")
        acts.remove(last_action[0] + "2")
    for action in acts:
        successors[action] = eval("cube.%s(%s)" % (action, str(state)))
    return successors

print shortest_path_search(color_converter.color_convert("003003002115115000222222111444332332144144544355355355"), cube_successors, solved)
