class LimitedIntDialog:
    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance is not None:
            pass

    def read(self, title, min, max):
        pass

    def read_(self, title, min):
        pass
