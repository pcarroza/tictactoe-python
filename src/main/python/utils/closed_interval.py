class ClosedInterval:

    def __init__(self, min: int, max: int):
        self.__min = min
        self.__max = max

    def included(self, value):
        return self.__min <= value <= self.__max
