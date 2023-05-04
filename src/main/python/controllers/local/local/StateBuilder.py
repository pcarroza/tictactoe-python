from src.main.python.controllers.local.local.EndState import EndState
from src.main.python.controllers.local.local.FinalState import FinalState
from src.main.python.controllers.local.local.InGameState import InGameState
from src.main.python.controllers.local.local.InitialState import InitialState


class StateBuilder:

    def __init__(self, local_operation_controller_builder):
        self.__initial_state = InitialState(self,local_operation_controller_builder)
        self.__in_game_state = InGameState(self, local_operation_controller_builder)
        self.__final_state = FinalState(self,local_operation_controller_builder)
        self.__end_state = EndState(self)

    def get_initial_state(self):
        return self.__initial_state

    def get_in_game_state(self):
        return self.__in_game_state

    def get_final_state(self):
        return self.__final_state

    def get_end_state(self):
        return self.__end_state
