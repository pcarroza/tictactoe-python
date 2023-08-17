from src.main.python.controllers.local.logic.State import State


class EndState(State):

    def __init__(self, state_builder):
        super().__init__(state_builder)

    def get_controller(self):
        return None
