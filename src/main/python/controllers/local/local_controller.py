from src.main.python.models.coordinate import Coordinate
from src.main.python.models.game import Game


class LocalController:

    def __init__(self, game: Game):
        self.__game: Game = game

    @property
    def game(self):
        return self.__game

    def number_of_max_players(self):
        return self.__game.NUMBER_MAX_OF_PLAYERS

    def color(self, coordinate: Coordinate):
        return self.__game.get_color(coordinate)

    def take(self):
        return self.__game.take()

    def put(self, coordinate: Coordinate):
        self.__game.put(coordinate)

    def remove(self, coordinate: Coordinate):
        self.__game.remove(coordinate)

    def clear(self):
        self.__game.clear()

    def is_empty(self, coordinate: Coordinate):
        self.__game.is_empty(coordinate)

    def is_occupied_by_player(self, coordinate: Coordinate):
        return self.__game.is_occupied_by_player(coordinate)

    def exist_tictactoe(self):
        return self.__game.exist_tictactoe()

    def is_complete(self):
        self.__game.is_complete()

    def initialize(self):
        self.__game.initialize()

    def begin(self):
        self.__game.begin()

    def finalize(self):
        self.__game.finalize()

    def end(self):
        self.__game.end()
