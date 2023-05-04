from python.utils.closed_interval import ClosedInterval
from src.main.python.models.coordinate import Coordinate
from src.main.python.models.direction import Direction
from src.main.python.models.subject import Subject
from src.main.python.models.color import Color
from src.main.python.models.turn import Turn


class Board(Subject):

    def __init__(self):
        super().__init__()
        self.__flat: dict = {}
        for color in Color.colors():
            self.__flat[color] = set()
        self.__turn = Turn()

    def get_flat(self):
        return self.__flat

    def put(self, target: Coordinate) -> None:
        Board.require(target)
        self.__flat.get(self.__turn.take()).add(target)
        assert not self.is_empty(target)

    def remove(self, origin: Coordinate):
        Board.require(origin)
        self.__flat.get(self.__turn.take()).remove(origin)
        assert self.is_empty(origin)

    def get_color(self, coordinate: Coordinate) -> Color:
        Board.require(coordinate)
        color_ = Color.NONE
        for color in self.__flat.keys():
            if coordinate in self.__flat.get(color):
                color_ = color
        return color_

    def is_empty(self, coordinate: Coordinate):
        Board.require(coordinate)
        return coordinate not in self.__flat.get(Color.XS) and coordinate not in self.__flat.get(Color.OS)

    def is_occupied_by_player(self, coordinate):
        Board.require(coordinate)
        return coordinate in self.__flat.get(self.__turn.take())

    @classmethod
    def require(cls, coordinate):
        assert coordinate is not None
        assert isinstance(coordinate, Coordinate)
        assert ClosedInterval(1, Coordinate.DIMENSION()).included(coordinate.row)
        assert ClosedInterval(1, Coordinate.DIMENSION()).included(coordinate.column)

    def change(self):
        self.__turn.change()

    def take(self):
        return self.__turn.take()

    def current_player(self):
        return self.__turn.current_player()

    def clear(self):
        for color in self.__flat.keys():
            self.__flat.get(color).clear()
        self.__turn.reset()

    def empty_coordinate(self):
        return self.get_coordinates(lambda target: self.get_color(target) == Color.NONE)

    def player_coordinate(self):
        return self.get_coordinates(lambda target: self.get_color(target) == self.__turn.take())

    @classmethod
    def get_coordinates(cls, is_equals_color):
        coordinates = []
        for row in range(1, Coordinate.DIMENSION() + 1):
            for column in range(1, Coordinate.DIMENSION() + 1):
                target = Coordinate(row, column)
                if is_equals_color(target):
                    coordinates.append(target)
        return coordinates

    def is_complete(self):
        numbers_of_colors = 0
        for color in self.__flat.keys():
            numbers_of_colors += len(self.__flat.get(color))
        return numbers_of_colors == Coordinate.DIMENSION() * len(self.__flat.keys())

    def is_exit_tictactoe(self):
        coordinates = self.__flat.get(self.__turn.take())
        if len(coordinates) != Coordinate.DIMENSION:
            return False
        coordinates_ = list(coordinates)
        direction = coordinates_[0].inDirectoin(coordinates_[1])
        if direction == Direction.NON_EXISTENT:
            return False
        for i in range(1, Coordinate.DIMENSION()):
            if coordinates_[i].in_direction(coordinates_[i + 1]) != direction:
                return False
        return True


if __name__ == '__main__':

    board = Board()











