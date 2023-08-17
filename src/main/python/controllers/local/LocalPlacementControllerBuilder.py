from python.controllers.local.LocalPlacementController import LocalPlacementController
from python.controllers.local.LocalMoveController import LocalMoveController
from python.controllers.local.LocalPutController import LocalPutController
from python.models.game import Game


class LocalPlacementControllerBuilder:

    def __init__(self, game):
        self.__game: Game = game
        self.__controllers: list[LocalPlacementController] = []

    @property
    def game(self):
        return self.__game

    def build(self):
        pass

    def __build(self, controllers):
        assert self.__controllers is not None
        assert all(controller is not None for controller in self.__controllers)
        self.__controllers = [
            LocalPutController(self.game, controllers[0]),
            LocalMoveController(self.game, controllers[1])
        ]

    def get_placement_controller(self):
        assert self.__controllers is not None
        assert all(controller is not None for controller in self.__controllers)
        return self.__controllers[0] if not self.__game.is_complete() else self.__controllers[1]
