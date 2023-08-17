from python.controllers.local.LocalCoordinateController import LocalCoordinateController
from python.controllers.local.LocalPlacementController import LocalPlacementController
from python.controllers.local.errors.ErrorGeneratorType import ErrorGeneratorType
from python.models.coordinate import Coordinate
from python.models.game import Game


class LocalMoveController(LocalPlacementController):

    def __init__(self, game: Game, local_coordinate_controller: LocalCoordinateController):
        super().__init__(game, local_coordinate_controller)
        self.origin = None

    def put(self, target):
        assert target is not None
        assert self.origin is not None
        assert self.validate_target_(self.origin, target) is not None
        super().put(target)
        self.origin = None

    def remove(self, origin: Coordinate):
        assert origin is not None
        assert self.validate_target(origin) is not None
        self.origin = origin
        super().remove(origin)

    def validate_target(self, origin):
        assert origin is not None
        if not self.is_occupied_by_current_player(origin):
            return ErrorGeneratorType.NOT_PROPERTY.value.get_error_report(self.game)
        return None

    def validate_target_(self, origin, target):
        assert origin is not None
        assert target is not None
        errorReports = super().validate_target(target)
        if errorReports is not None:
            return errorReports
        if origin == target:
            return ErrorGeneratorType.REPEATED_COORDINATE.value.get_error_report(self.game)
        return None

    def accept_operation_controller(self, visitor):
        visitor.visit(self)

    def accept_placement_controller(self, visitor):
        visitor.visit(self)
