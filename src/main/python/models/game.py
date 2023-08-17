from python.models.observer import Observer
from src.main.python.models.board import Board


class Game:

    def __init__(self, observer: Observer):
        self.__board: Board = Board()
        self.__board.subscribe(observer)

    @property
    def NUMBER_MAX_OF_PLAYERS(self):
        return 2

    def put(self, coordinate):
        self.__board.put(coordinate)

    def get_color(self, coordinate):
        self.__board.get_color(coordinate)

    def take(self):
        self.__board.take()

    def current_player(self):
        return self.__board.current_player()

    def remove(self, coordinate):
        return self.__board.remove(coordinate)

    def clear(self):
        self.__board.clear()

    def is_empty(self, coordinate):
        return self.__board.is_empty(coordinate)

    def is_occupied_current_by_player(self, coordinate):
        return self.__board.is_occupied_by_player(coordinate)

    def exist_tictactoe(self):
        return self.__board.is_exit_tictactoe()

    def is_complete(self):
        return self.__board.is_complete()

    def get_empty_coordinate(self):
        return self.__board.get_empty_coordinate()

    def get_player_coordinate(self):
        return self.__board.get_player_coordinate()

    def initialize(self):
        self.__board.initialize()

    def begin(self):
        self.__board.begin()

    def finalize(self):
        self.__board.finalize()

    def end(self):
        self.__board.end()
