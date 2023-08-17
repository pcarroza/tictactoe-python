class Subject:

    def __init__(self):
        self.__observer = None

    def subscribe(self, observer):
        self.__observer = observer

    def initialize(self):
        self.__observer.initialize()

    def begin(self):
        self.__observer.begin()

    def finalize(self):
        self.__observer.finalize()

    def end(self):
        self.__observer.end()