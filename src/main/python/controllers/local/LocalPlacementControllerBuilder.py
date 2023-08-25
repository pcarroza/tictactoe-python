from python.controllers.local.LocalPlacementController import LocalPlacementController
from python.controllers.local.LocalMoveController import LocalMoveController
from python.controllers.local.LocalPutController import LocalPutController
from python.models.Game import Game


class LocalPlacementControllerBuilder:

    def __init__(self, game):
        self.__game: Game = game
        self.controllers: list[LocalPlacementController] = []

    @property
    def game(self):
        return self.__game

    def build(self):
        pass

    def __build(self, controllers):
        assert self.controllers is not None
        assert all(controller is not None for controller in self.controllers)
        self.controllers = [
            LocalPutController(self.game, controllers[0]),
            LocalMoveController(self.game, controllers[1])
        ]

    def get_placement_controller(self):
        assert self.controllers is not None
        assert all(controller is not None for controller in self.controllers)
        if not self.game.is_complete():
            return self.controllers[0]
        return self.controllers[1]
