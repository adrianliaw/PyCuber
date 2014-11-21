"""

Utility functions.
Most are path searching functions.

"""

def shortest_path_search(start, successors, is_goal):
    """
    Find the shortest path from start state to a state
    such that is_goal(state) is true.
    """
    if is_goal(start):
        return [start]
    explored = [] # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (action, state) in successors(s, path_actions(path)[-1] if len(path) != 1 else []):
            if state not in explored:
                explored.append(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def a_star_search(start, successors, state_value, is_goal):
    """
    This is a searching function of A*
    """
    if is_goal(start):
        return [start]
    explored = []
    g = 1
    h = state_value(start)
    f = g + h
    p = [start]
    frontier = [(f, g, h, p)]
    while frontier:
        f, g, h, path = frontier.pop(0)
        s = path[-1]
        for (action, state) in successors(s, path_actions(path)[-1] if len(path) != 1 else []):
            if state not in explored:
                explored.append(state)
                path2 = path + [action, state]
                h2 = state_value(state)
                g2 = g + 1
                f2 = h2 + g2
                if is_goal(state):
                    return path2
                else:
                    frontier.append((f2, g2, h2, path2))
                    frontier.sort(key=lambda x:x[:3])
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]
    
def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

