from python.views.console.PlacementCoordinateView import PlacementCoordinateView


class PutTargetCoordinateView(PlacementCoordinateView):

    def __init__(self, get_coordinate_controller):
        super().__init__(get_coordinate_controller)
