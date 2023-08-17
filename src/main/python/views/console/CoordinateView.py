from python.models.coordinate import Coordinate
from python.utils.LimitedIntDialog import LimitedIntDialog
from python.utils.Terminal import Terminal


class CoordinateView:

    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance is not None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def read(self, title, coordinate: Coordinate):
        assert title is not None
        assert coordinate is not None
        Terminal.instance().write("¿en qué casilla?")
        coordinate.row = LimitedIntDialog.instance().read("¿Fila?", Coordinate.DIMENSION)
        coordinate.column = LimitedIntDialog.instance().read("¿Columna?", Coordinate.DIMENSION)

    def write(self, title, coordinate: Coordinate):
        Terminal.instance().write(title + "[" + coordinate.row + ", " + coordinate.column + "]")
