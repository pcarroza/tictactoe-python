import random


class Coordinate:
    DIMENSION = 3

    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

    def clone(self):
        return Coordinate(self.row, self.column)

    def random(self):
        self.row = random.randint(1, self.DIMENSION)
        self.column = random.randint(1, self.DIMENSION)

    def in_direction(self, target):
        pass

    def in_inverse(self):
        return self.row + self.column == self.DIMENSION

    def __repr__(self):
        return "Coordinate({}, {})".format(self.row, self.column)

    def __hash__(self):
        return hash(self.row + self.column)

    def __eq__(self, other):
        return (isinstance(other, Coordinate) and
                self.row == other.row and
                self.column == other.column)


if __name__ == '__main__':
    coordinate1 = Coordinate(1, 2)
    coordinate2 = Coordinate(1, 2)
    print(coordinate1 == coordinate2)
