from src.main.python.controllers.local.local_controller import LocalController


class LocalOperationController(LocalController):

    def __init__(self, game):
        super().__init__(game)

    def accept(self, operation_controller_visitor):
        pass
