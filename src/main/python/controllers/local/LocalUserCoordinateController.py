from python.controllers.CoordinateControllerVisitor import CoordinateControllerVisitor
from python.controllers.local.LocalCoordinateController import LocalCoordinateController
from python.models.Coordinate import Coordinate
from python.models.Game import Game


class LocalUserCoordinateController(LocalCoordinateController):

    def __init__(self, game: Game):
        super().__init__(game)

    def get_target(self):
        return Coordinate()

    def get_origin(self):
        return Coordinate()

    def accept(self, visitor: CoordinateControllerVisitor):
        visitor.visit_user_coordinate_controller(self)
