from python.controllers.local.logic.LocalLogic import LocalLogic
from python.views.console.ConsoleView import ConsoleView


class TicTacToe:

    def __init__(self):
        self.__logic = LocalLogic()
        self.__view = ConsoleView()

    def run(self):
        controller = self.__logic.get_controller()
        while controller is not None:
            self.__view.interact(controller)
            controller = self.__logic.get_controller()

