from python.controllers.local.LocalPlacementControllerBuilder import LocalPlacementControllerBuilder
from python.controllers.local.LocalUserCoordinateController import LocalUserCoordinateController
from python.models.Game import Game


class LocalUserPlacementControllerBuilder(LocalPlacementControllerBuilder):

    def __init__(self, game: Game):
        super().__init__(game)

    def build(self):
        controllers = [
            LocalUserCoordinateController(self.game),
            LocalUserCoordinateController(self.game)
        ]
        self._build_(controllers)
