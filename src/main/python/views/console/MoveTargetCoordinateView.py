from python.views.console.PlacementCoordinateView import PlacementCoordinateView


class MoveTargetCoordinateView(PlacementCoordinateView):

    def __init__(self, coordinate_controller, origin):
        super().__init__(coordinate_controller)
        self.__origin = origin
