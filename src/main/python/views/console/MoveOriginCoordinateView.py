from python.views.console.PlacementCoordinateView import PlacementCoordinateView


class MoveOriginCoordinateView(PlacementCoordinateView):

    def __init__(self, coordinate_controller):
        super().__init__(coordinate_controller)
