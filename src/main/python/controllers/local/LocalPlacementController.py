from python.controllers.local.LocalCoordinateController import LocalCoordinateController
from python.controllers.local.LocalOperationController import LocalOperationController
from python.controllers.local.errors.ErrorGeneratorType import ErrorGeneratorType
from python.models.Game import Game


class LocalPlacementController(LocalOperationController):

    def __init__(self, game: Game, local_coordinate_controller: LocalCoordinateController):
        super().__init__(game)
        self.__local_coordinate_controller = local_coordinate_controller

    def validate_target(self, target):
        if not self.is_empty(target):
            return ErrorGeneratorType.NOT_EMPTY.value.get_error_report()
        return None

    def getCoordinateController(self):
        return self.__local_coordinate_controller
