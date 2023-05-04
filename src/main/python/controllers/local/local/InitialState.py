from src.main.python.controllers.local.local_operation_controller_builder import LocalOperationControllerBuilder
from src.main.python.controllers.local.local.State import State


class InitialState(State):

    def __init__(self, state_builder, builder: LocalOperationControllerBuilder):
        super().__init__(state_builder)
        self.__start_controller = builder.get_start_controller

    def begin(self):
        return self.state_builder.get_in_game_state()

    def get_controller(self):
        return self.__start_controller
