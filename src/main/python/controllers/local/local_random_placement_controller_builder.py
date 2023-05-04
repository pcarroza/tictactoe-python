from python.controllers.local.local_placement_controller_builder import LocalPlacementControllerBuilder
from python.controllers.local.local_random_coordinate_controller import LocalRandomCoordinateController
from python.models.game import Game


class LocalRandomCoordinateControllerBuilder(LocalPlacementControllerBuilder):

    def __init__(self, game: Game):
        super().__init__(game)

    def build(self):
        local_coordinate_controller = [
            LocalRandomCoordinateController(self.game),
            LocalRandomCoordinateController(self.game)
        ]
        self.__build(local_coordinate_controller)
