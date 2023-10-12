class Coordinate:

    def __init__(self, row=0, column=0):
        self.__row = row
        self.__column = column

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column

    @row.setter
    def row(self, row):
        self.__row = row

    @column.setter
    def column(self, column):
        self.__column = column

    def direction(self, coordinate):
        pass

    def __repr__(self):
        return "Coordinate({},{})".format(self.row, self.column)

    def __hash__(self):
        return hash((self.__row, self.__column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
