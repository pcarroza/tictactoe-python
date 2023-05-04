from python.controllers.local.local_coordinate_controller import LocalCoordinateController
from python.controllers.local.local_operation_controller import LocalOperationController
from python.models.game import Game


class LocalPlacementController(LocalOperationController):

    def __init__(self, game: Game, local_coordinate_controller: LocalCoordinateController):
        super().__init__(game)
        self.__local_coordinate_controller = local_coordinate_controller



