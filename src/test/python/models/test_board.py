from unittest import TestCase

from python.models.board import Board
from python.models.coordinate import Coordinate


class TestBoard(TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_put(self):
        self.board.put(Coordinate(1,1))
        self.assertIsInstance(self.board, Board, "self.board is Board")

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
        pass

    def test_player_coordinate(self):
        pass