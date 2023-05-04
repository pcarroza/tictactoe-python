from python.controllers.local.local_placement_controller import LocalPlacementController
from python.controllers.local.local_move_controller import LocalMoveController
from python.controllers.local.local_put_controller import LocalPutController
from python.models.game import Game


class LocalPlacementControllerBuilder:

    def __init__(self, game):
        self.__game: Game = game
        self.__placement_controllers: list[LocalPlacementController] = []

    @property
    def game(self):
        return self.__game

    def build(self):
        pass

    def __build(self, coordinate_controllers):
        assert self.__placement_controllers is not None
        for controller in self.__placement_controllers:
            assert controller is not None
        self.__placement_controllers.append(LocalPutController(self.game, coordinate_controllers[0]))
        self.__placement_controllers.append(LocalMoveController(self.game, coordinate_controllers[1]))

    def get_placement_controller(self):
        assert self.__placement_controllers is not None
        for controller in self.__placement_controllers:
            assert controller is not None
        if not self.__game.is_complete():
            return self.__placement_controllers[0]
        else:
            return self.__placement_controllers[1]
