from python.models.Color import Color
from python.models.Board import Board
from python.models.Coordinate import Coordinate

if __name__ == '__main__':

    flat: dict = {color: set() for color in Color.colors()}

    flat[Color.OS.value].add(Coordinate(1, 1))
    flat[Color.OS.value].add(Coordinate(1, 2))
    flat[Color.OS.value].add(Coordinate(1, 3))

    print(Color.OS.value)
    print(flat)

    board = Board()
    board.put(Coordinate(1, 1))
    board.put(Coordinate(1, 2))
    board.put(Coordinate(1, 3))

    print(board.flat['OS'])
