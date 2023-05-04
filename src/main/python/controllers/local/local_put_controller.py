from python.controllers.local.local_coordinate_controller import LocalCoordinateController
from python.controllers.local.local_placement_controller import LocalPlacementController
from python.models.game import Game


class LocalPutController(LocalPlacementController):

    def __init__(self, game: Game, local_coordinate_controller: LocalCoordinateController):
        super().__init__(game, local_coordinate_controller)

