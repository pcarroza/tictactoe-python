from src.main.python.controllers.local.local_operation_controller_builder import LocalOperationControllerBuilder
from src.main.python.controllers.local.local.StateBuilder import StateBuilder
from src.main.python.models.observer import Observer
from src.main.python.models.game import Game
from src.main.python.Logic import Logic


class LocalLogic(Logic, Observer):

    def __init__(self):
        self.__game = Game(self)
        self.__builder = LocalOperationControllerBuilder(self.__game)
        self.__state_initial = StateBuilder(self.__builder).get_initial_state()

    def initialize(self):
        self.__state_initial = self.__state_initial.initialize()

    def begin(self):
        self.__state_initial = self.__state_initial.begin()

    def finalize(self):
        self.__state_initial = self.__state_initial.finalize()

    def end(self):
        self.__state_initial = self.__state_initial.end()

    def get_controller(self):
        return self.__state_initial.get_controller()
