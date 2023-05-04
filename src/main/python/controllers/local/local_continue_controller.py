from src.main.python.controllers.local.local_operation_controller import LocalOperationController


class LocalContinueController(LocalOperationController):

    def __init__(self, game):
        super().__init__(game)

    def accept(self, operation_controller_visitor):
        operation_controller_visitor.visit(self)
