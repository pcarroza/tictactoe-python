from python.models.coordinate import Coordinate
from python.utils.Terminal import Terminal


class BoardView:

    @classmethod
    def write(cls, presenter_controller):
        for i in range(1, Coordinate.DIMENSION + 1):
            for j in range(1, Coordinate.DIMENSION + 1):
                Terminal.instance().write(" ", presenter_controller.get_color(Coordinate(i, j)))
            Terminal.instance().write("")
