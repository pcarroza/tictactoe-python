from enum import Enum


class Color(Enum):
    XS = "XS"
    OS = "OS"
    NONE = "NONE"

    @classmethod
    def colors(cls):
        return list([Color.OS, Color.XS])
