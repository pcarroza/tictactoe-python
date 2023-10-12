from python.models.Board import Board
from python.models.Coordinate import Coordinate


class Game:

    def __init__(self):
        self.board = Board()

    @property
    def NUMBER_OF_PLAYERS(self):
        return 2

    def get_flat(self):
        return self.board.get_flat()

    def put(self, coordinate):
        self.board.put(coordinate)

    def remove(self, coordinate):
        self.board.remove(coordinate)

    def get_player_coordinates(self):
        return self.board.get_player_coordinates()

    def get_empty_coordinates(self):
        return self.board.get_empty_coordinates()

    def get_color(self, coordinate):
        return self.board.get_color(coordinate)

    def take(self):
        self.board.take()

    def clear(self):
        self.board.clear()

    def is_empty(self, coordinate):
        return self.board.is_empty(coordinate)

    def is_occupied_current_by_player(self, coordinate):
        return self.board.is_occupied_current_by_player(coordinate)

    def exist_tictactoe(self):
        return self.board.is_exit_tictactoe()

    def is_complete(self):
        return self.board.is_complete()

    def initialize(self):
        self.board.initialize()

    def begin(self):
        self.board.begin()

    def finalize(self):
        self.board.finalize()

    def end(self):
        self.board.end()


if __name__ == '__main__':
    game = Game()
    game.put(Coordinate(1, 1))
    game.put(Coordinate(1, 2))
    game.put(Coordinate(1, 3))

    print(game.get_player_coordinates())

    print(game.is_occupied_current_by_player(Coordinate(1, 1)))
    print(game.is_complete())

    board = Board()
    board.put(Coordinate(1, 1))
    board.put(Coordinate(1, 2))
    board.put(Coordinate(1, 3))

    print(board.get_player_coordinates())





