class State:

    def __init__(self, state_builder):
        self.state_builder = state_builder

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
