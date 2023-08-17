from python.controllers.local.logic.EndState import EndState
from python.controllers.local.logic.FinalState import FinalState
from python.controllers.local.logic.InGameState import InGameState
from python.controllers.local.logic.InitialState import InitialState


class StateBuilder:

    def __init__(self, builder):
        self.__initial_state = InitialState(self, builder)
        self.__in_game_state = InGameState(self, builder)
        self.__final_state = FinalState(self, builder)
        self.__end_state = EndState(self)

    def get_initial_state(self):
        return self.__initial_state

    def get_in_game_state(self):
        return self.__in_game_state

    def get_final_state(self):
        return self.__final_state

    def get_end_state(self):
        return self.__end_state
