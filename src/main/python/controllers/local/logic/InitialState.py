from src.main.python.controllers.local.LocalOperationControllerBuilder import LocalOperationControllerBuilder
from src.main.python.controllers.local.logic.State import State


class InitialState(State):

    def __init__(self, state_builder, builder: LocalOperationControllerBuilder):
        super().__init__(state_builder)
        self.__builder = builder

    def begin(self):
        return self.state_builder.get_in_game_state()

    def get_controller(self):
        return self.__builder.get_start_controller()
