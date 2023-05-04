from src.main.python.controllers.local.local_operation_controller_builder import LocalOperationControllerBuilder
from src.main.python.controllers.local.local.State import State


class FinalState(State):

    def __init__(self, state_builder, builder: LocalOperationControllerBuilder):
        super().__init__(state_builder)
        pass

    def initialize(self):
        pass

    def get_controller(self):
        return None
