from python.utils.closed_interval import ClosedInterval
from src.main.python.controllers.OperationControllerVisitor import OperationControllerVisitor
from src.main.python.controllers.local.local_operation_controller import LocalOperationController


class LocalStartController(LocalOperationController):

    def __init__(self, game, builder):
        super().__init__(game)
        self.__local_operation_controller_builder = builder

    def build(self, user):
        assert ClosedInterval(0, self.game.NUMBER_MAX_OF_PLAYERS).included(user)
        self.__local_operation_controller_builder.build(user)
        self.begin()

    def accept(self, operation_controller_visitor: OperationControllerVisitor):
        operation_controller_visitor.visit(self)
