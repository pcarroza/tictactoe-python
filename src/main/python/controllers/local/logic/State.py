class State:

    def __init__(self, state_builder):
        self.__state_builder = state_builder

    @property
    def state_builder(self):
        return self.__state_builder

    def initialize(self):
        assert False

    def begin(self):
        assert False

    def finalize(self):
        assert False

    def end(self):
        assert False

    def get_controller(self):
        pass
