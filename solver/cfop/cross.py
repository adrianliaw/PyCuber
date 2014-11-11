"""
Module for solving Rubik's Cube cross.
"""

from pycuber import *
from pycuber.helpers import fill_unknowns
from util import a_star_search, path_actions

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
    def cross_successors(state, last_action=None):
        """
        Successors function for solving the cross.
        """
        centres, edges = state
        cube = Cube(fill_unknowns(set(centres.values()) | edges))
        acts = sum([
            [s, s.inverse(), s * 2]
            map(Step, "RUFDRB".replace(last_action.face if last_action else "", "", 1))
            ], [])
        for step in acts:
            cube(step)
            yield step, (centres, cube.select_type("edge") - cube.has_colour(cube["D"].colour))
            cube(step.inverse())

    @staticmethod
    def cross_goal(state):
        """
        The goal function for cross solving search.
        """
        centres, edges = state
        for edge in edges:
            if "D" not in edge.facings:
                return False
            if edge["D"] != centres["D"]:
                return False
            k = "".join(edge.facings.keys()).replace("D", "")
            if edge[k] != centres[k]:
                return False
        return True

    @staticmethod
    def cross_state_value(state):
        """
        Compute the state value of the cross solving search.
        """
        _, edges = state
        value = 0

        

