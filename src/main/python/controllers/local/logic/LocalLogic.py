from python.controllers.local.logic.State import State
from src.main.python.controllers.local.LocalOperationControllerBuilder import LocalOperationControllerBuilder
from src.main.python.controllers.local.logic.StateBuilder import StateBuilder
from src.main.python.models.observer import Observer
from src.main.python.models.game import Game
from src.main.python.Logic import Logic


class LocalLogic(Logic, Observer):

    def __init__(self):
        game = Game(self)
        builder = LocalOperationControllerBuilder(game)
        self.actual_state: State = StateBuilder(builder).get_initial_state()

    def initialize(self):
        self.actual_state = self.actual_state.initialize()

    def begin(self):
        self.actual_state = self.actual_state.begin()

    def finalize(self):
        self.actual_state = self.actual_state.finalize()

    def end(self):
        self.actual_state = self.actual_state.end()

    def get_controller(self):
        return self.actual_state.get_controller()
