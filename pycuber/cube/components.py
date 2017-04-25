from colorama import Back
from .constants import U, D, L, R, F, B
from .settings import display_colours as colours


class Face(object):

    def __init__(self, data, face):
        self.__data = data
        self.face = "ULFRBD"[face]

    def __getitem__(self, index):
        return self.__data[index]

    def __repr__(self):
        rows = []
        for row in self.__data:
            rows.append("")
            for square in row:
                rows[-1] += colours[square] + "  "
        return (Back.RESET + "\n").join(rows) + Back.RESET
