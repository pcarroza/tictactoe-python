from python.controllers.local.LocalRandomPlacementControllerBuilder import LocalRandomPlacementControllerBuilder
from python.controllers.local.LocalUserPlacementControllerBuilder import LocalUserPlacementControllerBuilder
from python.controllers.local.LocalContinueController import LocalContinueController
from python.controllers.local.LocalStartController import LocalStartController
from python.utils.ClosedInterval import ClosedInterval


class LocalOperationControllerBuilder:

    def __init__(self, game):
        self.game = game
        self.local_start_controller = LocalStartController(self.game, self)
        self.local_continue_controller = LocalContinueController(self.game)
        self.builders = []

    def build(self, users):
        assert ClosedInterval(1, self.game.NUMBER_MAX_OF_PLAYERS).included(users)
        for i in range(0, self.game.NUMBER_MAX_OF_PLAYERS):
            if i < users:
                self.builders.append(LocalUserPlacementControllerBuilder(self.game))
            else:
                self.builders.append(LocalRandomPlacementControllerBuilder(self.game))
            self.builders[i].build()

    def get_placement_controller(self):
        assert self.builders is not None
        assert self.builders[self.game.current_player()] is not None
        return self.builders[self.game.current_player()].get_placement_controller()

    def get_continue_controller(self):
        assert self.local_continue_controller is not None
        return self.local_continue_controller

    def get_start_controller(self):
        assert self.local_start_controller is not None
        return self.local_start_controller
