from python.controllers.local.LocalPlacementControllerBuilder import LocalPlacementControllerBuilder
from python.controllers.local.LocalUserCoordinateController import LocalUserCoordinateController
from python.models.game import Game


class LocalUserPlacementControllerBuilder(LocalPlacementControllerBuilder):

    def __init__(self, game: Game):
        super().__init__(game)

    def build(self):
        local_user_placement_controllers = [
            LocalUserCoordinateController(self.game),
            LocalUserCoordinateController(self.game)
        ]
        self.__build(local_user_placement_controllers)
