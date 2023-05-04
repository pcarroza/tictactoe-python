from src.main.python.controllers.local.local.State import State


class InGameState(State):

    def __init__(self, state_builder, local_operation_controller_builder):
        super().__init__(state_builder)

    def finalize(self):
        pass

    def end(self):
        pass

    def get_controller(self):
        return self.state_builder.get_controller()
