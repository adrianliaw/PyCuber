"""

This module is to represent the Rubik's Cube algorithms.

"""


class Step:
    """
    Representing a Rubik's Cube action.
    """
    def __init__(self, name):
        pass
    def __repr__(self):
        pass
    def set(self, new):
        """Reset the action name."""
    def perform(self, cube):
        """Perform this action on the cube."""

class Algo(list):
    """
    Representing a Rubik's Cube algorithm.
    """
    def __init__(self, sequence, cube):
        pass
    def __repr__(self):
        pass
    def __setitem__(self, index, new):
        pass
    def __getitem__(self, index):
        pass
    def perform_index(self, i=0, pop=False):
        """Perform ith action of the sequence."""
    def perform_slice(self, i=0, j=None, pop=False):
        """Perform ith~jth actions of the sequence."""
    def perform_all(self, clear=False):
        """Perform whole algorithm."""
    def set_cube(self, cube):
        """Reset the cube."""
