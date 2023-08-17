from python.controllers.local.LocalCoordinateController import LocalCoordinateController
from python.controllers.RandomCoordinateController import RandomCoordinateController
from python.models.game import Game


class LocalRandomCoordinateController(RandomCoordinateController, LocalCoordinateController):

    def __init__(self, game: Game):
        super().__init__(game)

    def get_target(self):
        pass

    def get_origin(self):
        pass

    def get_target_(self, coordinate):
        pass

    def accept(self, coordinate_controller_visitor):
        pass
