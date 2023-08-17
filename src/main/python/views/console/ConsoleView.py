from python.View import View
from python.views.console.BoardView import BoardView
from python.views.console.ContinueView import ContinueView
from python.views.console.GameView import GameView


class ConsoleView(View):

    def __init__(self):
        board_view = BoardView()
        self.__game_view = GameView(board_view)
        self.__continue_view = ContinueView(board_view)

    def interact(self, operation_controller):
        print(operation_controller)
        # operation_controller.accept(self)

    def visit_start_controller(self, start_controller):
        start_controller.interact(self)

    def visit_placement_controller(self, placement_controller):
        placement_controller.interact(self)

    def visit_continue_controller(self, continue_controller):
        continue_controller.interact(self)
