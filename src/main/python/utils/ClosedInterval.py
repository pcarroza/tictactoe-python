class ClosedInterval:

    def __init__(self, minimum: int, maximum: int):
        self.__minimum = minimum
        self.__maximum = maximum

    def included(self, value):
        return self.__minimum <= value <= self.__maximum
