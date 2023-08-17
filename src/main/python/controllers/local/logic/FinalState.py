from src.main.python.controllers.local.LocalOperationControllerBuilder import LocalOperationControllerBuilder
from src.main.python.controllers.local.logic.State import State


class FinalState(State):

    def __init__(self, state_builder, builder: LocalOperationControllerBuilder):
        super().__init__(state_builder)
        self.__builder = builder

    def initialize(self):
        return self.state_builder.get_initial_state()

    def end(self):
        return self.state_builder.get_end_state()

    def get_controller(self):
        return self.__builder.get_start_controller()
