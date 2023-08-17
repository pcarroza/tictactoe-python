from python.models.coordinate import Coordinate


class ErrorReport:

    def __init__(self, coordinates):
        self.__coordinates: list[Coordinate] = coordinates

    def iterator(self):
        return self.__coordinates

    def accept(self, visitor):
        pass
