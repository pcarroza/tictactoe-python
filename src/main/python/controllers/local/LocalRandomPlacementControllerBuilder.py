from python.controllers.local.LocalPlacementControllerBuilder import LocalPlacementControllerBuilder
from python.controllers.local.LocalRandomCoordinateController import LocalRandomCoordinateController
from python.models.game import Game


class LocalRandomCoordinateControllerBuilder(LocalPlacementControllerBuilder):

    def __init__(self, game: Game):
        super().__init__(game)

    def build(self):
        local_random_coordinate_controllers = [
            LocalRandomCoordinateController(self.game),
            LocalRandomCoordinateController(self.game)
        ]
        self.__build(local_random_coordinate_controllers)
