from python.controllers.local.LocalOperationControllerBuilder import LocalOperationControllerBuilder
from src.main.python.controllers.local.logic.State import State


class InGameState(State):

    def __init__(self, state_builder, builder: LocalOperationControllerBuilder):
        super().__init__(state_builder)
        self.__builder = builder

    def finalize(self):
        return self.state_builder.get_final_state()

    def get_controller(self):
        return self.__builder.get_placement_controller()
