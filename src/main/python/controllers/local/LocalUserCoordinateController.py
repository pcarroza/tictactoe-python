from http import cookiejar

from python.controllers.local.LocalCoordinateController import LocalCoordinateController
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
        coordinate_controller_visitor.visit(self)
