from python.controllers.local.LocalCoordinateController import LocalCoordinateController
from python.controllers.local.LocalPlacementController import LocalPlacementController
from python.models.Coordinate import Coordinate
from python.models.Game import Game


class LocalPutController(LocalPlacementController):

    def __init__(self, game: Game, controller: LocalCoordinateController):
        super().__init__(game, controller)

    def put(self, coordinate: Coordinate):
        assert self.validate_target(coordinate) is not None
        super().put(coordinate)

    def accept_operation_controller(self, visitor):
        visitor.visit(self)

    def accept_placement_controller(self, visitor):
        visitor.visit(self)
