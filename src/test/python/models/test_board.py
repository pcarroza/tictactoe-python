from unittest import TestCase

from python.models.Board import Board
from python.models.Coordinate import Coordinate


class TestBoard(TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_put(self):
        self.board.put(Coordinate(1, 2))

    def test_remove(self):
        pass

    def test_get_color(self):
        pass

    def test_change(self):
        pass

    def test_is_empty(self):
        pass

    def test_is_occupied_by_player(self):
        pass

    def test_is_complete(self):
        pass

    def test_is_exit_tictactoe(self):
        pass

    def test_take(self):
        pass

    def test_current_player(self):
        pass

    def test_clear(self):
        pass

    def test_empty_coordinate(self):
        self.board.put(Coordinate(1, 1))
        self.board.put(Coordinate(1, 2))
        self.board.put(Coordinate(1, 3))

    def test_player_coordinate(self):
        pass
