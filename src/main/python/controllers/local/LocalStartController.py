from python.utils.closed_interval import ClosedInterval
from src.main.python.controllers.OperationControllerVisitor import OperationControllerVisitor
from src.main.python.controllers.local.LocalOperationController import LocalOperationController


class LocalStartController(LocalOperationController):

    def __init__(self, game, local_operation_controller_builder):
        super().__init__(game)
        self.builder = local_operation_controller_builder

    def build(self, users):
        assert ClosedInterval(0, self.game.NUMBER_MAX_OF_PLAYERS).included(users)
        self.builder.build(users)
        self.begin()

    def accept(self, visitor: OperationControllerVisitor):
        visitor.visit(self)
