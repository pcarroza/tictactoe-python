from python.utils.closed_interval import ClosedInterval
from src.main.python.models.coordinate import Coordinate
from src.main.python.models.direction import Direction
from src.main.python.models.subject import Subject
from src.main.python.models.color import Color
from src.main.python.models.turn import Turn


class Board(Subject):

    def __init__(self):
        super().__init__()
        self.flat: dict = {color: set() for color in Color.colors()}
        self.turn = Turn()

    def get_flat(self):
        return self.flat

    def put(self, target: Coordinate) -> None:
        Board.require(target)
        self.flat.get(self.turn.take()).add(target.clone())
        assert not self.is_empty(target)

    def remove(self, origin: Coordinate):
        Board.require(origin)
        self.flat.get(self.turn.take()).remove(origin)
        assert self.is_empty(origin)

    def get_color(self, target: Coordinate) -> Color:
        Board.require(target)
        return next((color for color in self.flat.keys() if target in self.flat[color]), Color.NONE)

    def is_empty(self, coordinate: Coordinate):
        Board.require(coordinate)
        return coordinate not in self.flat[Color.XS] and coordinate not in self.flat[Color.OS]

    def is_occupied_by_player(self, coordinate):
        Board.require(coordinate)
        return coordinate in self.flat[self.turn.take()]

    @classmethod
    def require(cls, coordinate):
        assert coordinate is not None
        assert isinstance(coordinate, Coordinate)
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

    def get_empty_coordinate(self):
        return self.get_coordinates(lambda target: self.get_color(target) == Color.NONE)

    def get_player_coordinate(self):
        return self.get_coordinates(lambda target: self.get_color(target) == self.turn.take())

    @classmethod
    def get_coordinates(cls, is_equals_color):
        return [Coordinate(row, column)
                for row in range(1, Coordinate.DIMENSION() + 1)
                for column in range(1, Coordinate.DIMENSION() + 1)
                if is_equals_color(Coordinate(row, column))]

    def is_complete(self):
        numbers_of_colors = sum(len(self.flat[color]) for color in self.flat.keys())
        return numbers_of_colors == Coordinate.DIMENSION * len(self.flat.keys())

    def is_exit_tictactoe(self):
        coordinates = list(self.flat.get(self.turn.take()))
        _: list[Coordinate] = list(coordinates)
        return (
            len(coordinates) == Coordinate.DIMENSION and
            all(_[i].in_direction(_[i + 1]) == direction for i in range(1, Coordinate.DIMENSION - 1))
            if (direction := _[0].in_direction(_[1])) != Direction.NON_EXISTENT else False)
