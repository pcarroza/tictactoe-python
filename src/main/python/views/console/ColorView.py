from python.models.color import Color
from python.utils.Terminal import Terminal


class ColorView:

    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    __COLORS = {Color.XS: "x", Color.OS: "o", Color.NONE: "-"}

    def write(self, title, color: Color):
        Terminal.instance().write(title + self.to_char(color))

    def writer_winner(self, color):
        victory = "Victory!!!"
        Terminal.instance().write(victory)
        for _ in range(0, 3):
            Terminal.instance().write(self.to_char(color) + "! ")
        Terminal.instance().write(victory)

    def to_char(self, color: Color):
        return self.__COLORS[color]

