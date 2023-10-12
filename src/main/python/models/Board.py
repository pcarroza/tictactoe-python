from python.utils.ClosedInterval import ClosedInterval
from src.main.python.models.Coordinate import Coordinate
from src.main.python.models.Direction import Direction
from src.main.python.models.Subject import Subject
from src.main.python.models.Color import Color
from src.main.python.models.Turn import Turn


class Board(Subject):

    def __init__(self):
        super().__init__()
        self.flat: dict = {color: set() for color in Color.colors()}
        self.turn = Turn()

    def get_flat(self):
        return self.flat

    def put(self, target: Coordinate):
        Board.require(target)
        self.flat[self.take()].add(target)
        assert not self.is_empty(target)

    def remove(self, origin: Coordinate):
        Board.require(origin)
        self.flat[self.take()].remove(origin)
        assert self.is_empty(origin)

    def get_color(self, target: Coordinate) -> Color:
        Board.require(target)
        for color in self.flat.keys():
            if target in self.flat[color]:
                return color
        return Color.NONE

    def is_empty(self, coordinate: Coordinate):
        Board.require(coordinate)
        return coordinate not in self.flat[Color.XS.value] and coordinate not in self.flat[Color.OS.value]

    def is_occupied_current_by_player(self, coordinate):
        Board.require(coordinate)
        return coordinate in self.flat[self.turn.take()]

    @classmethod
    def require(cls, coordinate):
        assert coordinate is not None
        assert ClosedInterval(1, Coordinate.DIMENSION).included(coordinate.row)
        assert ClosedInterval(1, Coordinate.DIMENSION).included(coordinate.column)

    def change_to_next_player(self):
        self.turn.change_to_next_player()

    def take(self):
        return self.turn.take()

    def current_player(self):
        return self.turn.current_player()

    def clear(self):
        self.flat = {color: set() for color in self.flat.keys()}
        self.turn.reset()

    def get_empty_coordinates(self):
        return self.get_coordinates(lambda target: self.get_color(target) == Color.NONE)

    def get_player_coordinates(self):
        return self.get_coordinates(lambda target: self.get_color(target) == self.turn.take())

    @classmethod
    def get_coordinates(cls, is_equals):
        coordinates = []
        for i in range(1, Coordinate.DIMENSION + 1):
            for j in range(1, Coordinate.DIMENSION + 1):
                coordinate: Coordinate = Coordinate(i, j)
                if is_equals(coordinate):
                    coordinates.append(coordinate)
        return coordinates

    def is_complete(self):
        numbers_of_colors = sum(len(self.flat[color]) for color in self.flat.keys())
        return numbers_of_colors == Coordinate.DIMENSION * len(self.flat.keys())

    def is_exit_tictactoe(self):
        coordinates = list(self.flat[self.take()])
        _: list[Coordinate] = list(coordinates)
        return (
            len(coordinates) == Coordinate.DIMENSION and
            all(_[i].in_direction(_[i + 1]) == direction for i in range(1, Coordinate.DIMENSION - 1))
            if (direction := _[0].in_direction(_[1])) != Direction.NON_EXISTENT else False)


if __name__ == '__main__':
    board = Board()
    board.put(Coordinate(1, 2))
    print(board.get_player_coordinates())
