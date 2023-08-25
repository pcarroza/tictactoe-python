from python.models.Observer import Observer
from src.main.python.models.Board import Board


class Game:

    def __init__(self, observer: Observer):
        self.board: Board = Board()
        self.board.subscribe(observer)

    @property
    def NUMBER_MAX_OF_PLAYERS(self):
        return 2

    def put(self, coordinate):
        self.board.put(coordinate)

    def get_color(self, coordinate):
        self.board.get_color(coordinate)

    def take(self):
        self.board.take()

    def current_player(self):
        return self.board.current_player()

    def remove(self, coordinate):
        return self.board.remove(coordinate)

    def clear(self):
        self.board.clear()

    def is_empty(self, coordinate):
        return self.board.is_empty(coordinate)

    def is_occupied_current_by_player(self, coordinate):
        return self.board.is_occupied_by_player(coordinate)

    def exist_tictactoe(self):
        return self.board.is_exit_tictactoe()

    def is_complete(self):
        return self.board.is_complete()

    def get_empty_coordinate(self):
        return self.board.get_empty_coordinate()

    def get_player_coordinate(self):
        return self.board.get_player_coordinate()

    def initialize(self):
        self.board.initialize()

    def begin(self):
        self.board.begin()

    def finalize(self):
        self.board.finalize()

    def end(self):
        self.board.end()
