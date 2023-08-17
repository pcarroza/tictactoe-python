from src.main.python.models.color import Color


class Turn:

    def __init__(self):
        self.__value = 0

    def current_player(self):
        return self.__value

    def reset(self):
        self.__value = 0

    def take(self):
        return Color.colors()[self.__value]

    def change_to_next_player(self):
        self.__value = (self.__value + 1) % (len(Color.colors()))
