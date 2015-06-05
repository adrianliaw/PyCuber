"""
Module for solving Rubik's Cube cross.
"""

from pycuber import *
from .util import a_star_search, path_actions

class CrossSolver(object):
    """
    CrossSolver() => A Cross Solver.
    """
    def __init__(self, cube=None):
        self.cube = cube

    def feed(self, cube):
        """
        Feed Cube to the solver.
        """
        self.cube = cube

    @staticmethod
    def _rotate(edges, step):
        """
        Simulate the cube rotation by updating four edges.
        """
        step = Step(step)
        result = set()
        movement = {
            "U": "RFLB", 
            "D": "LFRB", 
            "R": "FUBD", 
            "L": "FDBU", 
            "F": "URDL", 
            "B": "ULDR", 
            }[step.face]
        movement = {
            movement[i]: movement[(i + step.is_clockwise + (-1 * step.is_counter_clockwise) + (2 * step.is_180)) % 4]
            for i in range(4)
            }
        for edge in edges:
            if step.face not in edge:
                result.add(edge.copy())
            else:
                k = (set(edge.facings.keys()) - {step.face}).pop()
                new_edge = Edge(**{
                    step.face: edge[step.face], 
                    movement[k]: edge[k], 
                    })
                result.add(new_edge)
        return result

    @staticmethod
    def cross_successors(state, last_action=None):
        """
        Successors function for solving the cross.
        """
        centres, edges = state
        acts = sum([
            [s, s.inverse(), s * 2] for s in
            map(Step, "RUFDRB".replace(last_action.face if last_action else "", "", 1))
            ], [])
        for step in acts:
            yield step, (centres, CrossSolver._rotate(edges, step))

    @staticmethod
    def cross_goal(state):
        """
        The goal function for cross solving search.
        """
        centres, edges = state
        for edge in edges:
            if "D" not in edge.facings:
                return False
            if edge["D"] != centres["D"]["D"]:
                return False
            k = "".join(edge.facings.keys()).replace("D", "")
            if edge[k] != centres[k][k]:
                return False
        return True

    @staticmethod
    def cross_state_value(state):
        """
        Compute the state value of the cross solving search.
        """
        centres, edges = state
        value = 0
        for edge in edges:
            if "U" in edge:
                if edge["U"] == centres["D"]["D"]:
                    value += 1
                else:
                    value += 2
            elif "D" in edge:
                if edge["D"] != centres["D"]["D"]:
                    value += 3
            else:
                value += 1
        edgeposes = {}
        counts = {f: 0 for f in "LFRB"}
        ngedges = []
        for edge in edges:
            if "U" in edge and edge["U"] == centres["D"]["D"]:
                k = "".join(edge.facings.keys()).replace("U", "")
                edgeposes[k] = edge[k]
                counts[k] += 1
            elif "D" in edge and edge["D"] == centres["D"]["D"]:
                k = "".join(edge.facings.keys()).replace("D", "")
                edgeposes[k] = edge[k]
                counts[k] += 1
            elif "U" in edge or "D" in edge:
                ngedges.append(edge)
            else:
                for k, s in edge:
                    if s != centres["D"]["D"]:
                        edgeposes[k] = s
                        counts[k] += 1
                        break
        for edge in ngedges:
            idx = "LFRB".index(edge[centres["D"].colour])
            for i in [-1, 1]:
                if "LFRB"[(idx+1)%4] not in edgeposes:
                    k = "".join(edge.facings.keys()).replace("LFRB"[idx], "")
                    edgeposes["LFRB"[(idx+1)%4]] = edge[k]
                    counts["LFRB"[(idx+1)%4]] += 1
                    break
            else:
                k = "".join(edge.facings.keys()).replace("LFRB"[idx], "")
                if counts["LFRB"[(idx-1)%4]] > counts["LFRB"[(idx+1)%4]]:
                    edgeposes["LFRB"[(idx-1)%4]] = edge[k]
                else:
                    edgeposes["LFRB"[(idx+1)%4]] = edge[k]
        relative_pos = {f: centres[f][f] for f in "LFRB"}
        if len(edgeposes) == 4:
            for i in range(4):
                edgeposes["L"], edgeposes["F"], edgeposes["R"], edgeposes["B"] = \
                    edgeposes["F"], edgeposes["R"], edgeposes["B"], edgeposes["L"]
                if edgeposes == relative_pos:
                    break
            else:
                value += 5
        else:
            value += 3
        return value

    def solve(self):
        """
        Solve the cross.
        """
        result = Formula(path_actions(a_star_search(
            ({f: self.cube[f] for f in "LUFDRB"}, 
             self.cube.select_type("edge") & self.cube.has_colour(self.cube["D"].colour)), 
            self.cross_successors, 
            self.cross_state_value, 
            self.cross_goal, 
            )))
        self.cube(result)
        return result

    def is_solved(self):
        """
        Check if the cross of Cube is solved.
        """
        return self.cross_goal(({f: self.cube[f] for f in "LUFDRB"}, 
            self.cube.select_type("edge") & self.cube.has_colour(self.cube["D"].colour)))
        
