from python.controllers.local.local_coordinate_controller import LocalCoordinateController
from python.models.coordinate import Coordinate
from python.models.game import Game


class LocalUserCoordinateController(LocalCoordinateController):

    def __init__(self, game: Game):
        super().__init__(game)

    def get_target(self):
        return Coordinate()

    def get_origin(self):
        return Coordinate()

    def accept(self, coordinate_controller_visitor):
        pass
