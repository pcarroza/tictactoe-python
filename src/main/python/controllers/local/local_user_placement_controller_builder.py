from python.controllers.local.local_placement_controller_builder import LocalPlacementControllerBuilder
from python.controllers.local.local_user_coordinate_controller import LocalUserCoordinateController
from python.models.game import Game


class LocalUserPlacementControllerBuilder(LocalPlacementControllerBuilder):

    def __init__(self, game: Game):
        super().__init__(game)

    def build(self):
        local_coordinate_controller = [LocalUserCoordinateController(self.game),
                                       LocalUserCoordinateController(self.game)]
        self.__build(local_coordinate_controller)
