from python.controllers.local.LocalPlacementControllerBuilder import LocalPlacementControllerBuilder
from python.controllers.local.LocalRandomCoordinateController import LocalRandomCoordinateController
from python.models.Game import Game


class LocalRandomPlacementControllerBuilder(LocalPlacementControllerBuilder):

    def __init__(self, game: Game):
        super().__init__(game)

    def build(self):
        controllers = [
            LocalRandomCoordinateController(self.game),
            LocalRandomCoordinateController(self.game)
        ]
        self.__build(controllers)
