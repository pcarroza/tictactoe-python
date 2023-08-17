from python.controllers.CoordinateControllerVisitor import CoordinateControllerVisitor
from python.models.coordinate import Coordinate


class PlacementCoordinateView(CoordinateControllerVisitor):

    def __init__(self, coordinate_controller):
        self.__coordinate_controller = coordinate_controller

    def get_coordinate(self):
        pass

    def show(self, title, coordinate: Coordinate):
        pass

    def get_coordinate_controller(self):
        return self.__coordinate_controller
