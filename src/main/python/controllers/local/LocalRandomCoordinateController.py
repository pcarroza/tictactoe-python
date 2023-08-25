from python.controllers.CoordinateControllerVisitor import CoordinateControllerVisitor
from python.controllers.local.LocalCoordinateController import LocalCoordinateController
from python.controllers.RandomCoordinateController import RandomCoordinateController
from python.models.Coordinate import Coordinate
from python.models.Game import Game


class LocalRandomCoordinateController(RandomCoordinateController, LocalCoordinateController):

    def __init__(self, game: Game):
        super().__init__(game)

    def get_origin(self):
        origin = Coordinate()
        ok = True
        while ok:
            origin.random()
            if self.is_occupied_by_current_player(origin):
                ok = False
        return origin.clone()

    def get_target(self):
        target = Coordinate()
        ok = True
        while ok:
            target.random()
            if self.is_empty(target):
                ok = False
        return target.clone()

    def get_target_(self, origin: Coordinate):
        target = None
        ok = True
        while ok:
            target = self.get_target()
            ok = origin != target
        return target.clone()

    def accept(self, visitor: CoordinateControllerVisitor):
        visitor.visit_random_coordinate(self)
