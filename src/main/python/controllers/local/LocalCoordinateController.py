from python.controllers.CoordinateController import CoordinateController
from python.controllers.local.LocalController import LocalController
from python.models.game import Game


class LocalCoordinateController(LocalController, CoordinateController):

    def __init__(self, game: Game):
        super().__init__(game)

    def get_target(self):
        pass

    def get_origin(self):
        pass
