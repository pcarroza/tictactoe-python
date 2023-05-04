from python.controllers.local.local_random_placement_controller_builder import LocalRandomCoordinateControllerBuilder
from python.controllers.local.local_user_placement_controller_builder import LocalUserPlacementControllerBuilder
from python.controllers.local.local_placement_controller_builder import LocalPlacementControllerBuilder
from python.controllers.local.local_continue_controller import LocalContinueController
from python.controllers.local.local_start_controller import LocalStartController
from python.utils.closed_interval import ClosedInterval
from python.models.game import Game


class LocalOperationControllerBuilder:

    def __init__(self, game: Game):
        self.__game: Game = game
        self.__local_start_controller = LocalStartController(self.__game, self)
        self.__local_continue_controller = LocalContinueController(self.__game)
        self.__builders: list[LocalPlacementControllerBuilder] = []

    def build(self, users):
        assert ClosedInterval(1, self.__game.NUMBER_MAX_OF_PLAYERS).included(users)
        for i in range(0, self.__game.NUMBER_MAX_OF_PLAYERS):
            if i < users:
                self.__builders.append(LocalUserPlacementControllerBuilder(self.__game))
            else:
                self.__builders.append(LocalRandomCoordinateControllerBuilder(self.__game))
            self.__builders[i].build()

    def get_placement_controller(self):
        return self.__builders[self.__game.current_player()].get_placement_controller()

    def get_continue_controller(self):
        return self.__local_continue_controller

    @property
    def get_start_controller(self):
        return self.__local_start_controller
