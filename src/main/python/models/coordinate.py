import src.main.python.utils.coordinate
import random

from src.main.python.models.direction import Direction
from src.main.python.utils.closed_interval import ClosedInterval


class Coordinate:

    def __init__(self, row=0, column=0):
        self.__coordinate = src.main.python.utils.coordinate.Coordinate(row, column)

    @classmethod
    def DIMENSION(cls):
        return 2

    @property
    def coordinate(self):
        return self.__coordinate

    @property
    def row(self):
        return self.coordinate.row

    @property
    def column(self):
        return self.coordinate.column

    @row.setter
    def row(self, row):
        assert ClosedInterval(1, self.DIMENSION()).included(row)
        self.coordinate.row = row

    @column.setter
    def column(self, column):
        assert ClosedInterval(1, self.DIMENSION()).included(column)
        self.coordinate.column = column

    def clone(self):
        return Coordinate(self.row, self.column)

    def random(self):
        self.coordinate.row = random.randint(1, self.DIMENSION())
        self.coordinate.column = random.randint(1, self.DIMENSION())

    def inDirection(self, target):
        assert target is not None
        assert isinstance(target, Coordinate)
        direction = self.coordinate.direction(target.coordinate)
        if direction == Direction.NON_EXISTENT:
            if self.inInverse() and target.inInverse():
                return Direction.INVERSE
        return direction

    def inInverse(self):
        return self.row + self.column == self.DIMENSION

    def __repr__(self):
        return "Coordinate({},{})".format(self.row, self.column)

    def __hash__(self):
        return self.coordinate.__hash__()

    def __eq__(self, other):
        return isinstance(other, Coordinate) and self.coordinate == other


if __name__ == '__main__':
    coordinates = set()
    coordinates.add(Coordinate(1, 1))
    coordinates.add(Coordinate(1, 2))
    coordinates.add(Coordinate(1, 3))