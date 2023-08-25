from python.controllers.PlacementControllerVisitor import PlacementControllerVisitor
from python.controllers.local.LocalPlacementController import LocalPlacementController
from python.views.console.MoveOriginCoordinateView import MoveOriginCoordinateView
from python.views.console.MoveTargetCoordinateView import MoveTargetCoordinateView
from python.views.console.PlacementCoordinateView import PlacementCoordinateView
from python.views.console.PutTargetCoordinateView import PutTargetCoordinateView
from python.controllers.local.errors.ErrorReport import ErrorReport
from python.views.console.ErrorReportView import ErrorReportView
from python.views.console.ColorView import ColorView
from python.views.console.BoardView import BoardView
from python.models.Coordinate import Coordinate


class GameView(PlacementControllerVisitor):

    def __init__(self, board_view: BoardView):
        assert board_view is not None
        self.board_view = board_view
        self.error_report_view = ErrorReportView()
        self.origin = None

    def interact(self, placement_controller: LocalPlacementController):
        placement_controller.accept(self)

    def visit_put_controller(self, put):
        self.show_title("Pone", put.take())
        self.put(put, PutTargetCoordinateView(put.get_coordinate_controller()))
        self.show_game(put)

    def visit_move_controller(self, move):
        self.show_title("Move", move.take())
        self.remove(move, MoveOriginCoordinateView(move.get_coordinate_controller()))
        self._put(move, MoveTargetCoordinateView(move.get_coordinate_controller(), self.origin))
        self.show_game(move)

    @classmethod
    def show_title(cls, title, color):
        ColorView.instance().write(title + ' el jugador ', color)

    def put(self, put, placement_view: PlacementCoordinateView):
        target: Coordinate = placement_view.get_coordinate()
        error_report: ErrorReport = put.validateTarget(target)
        if error_report is not None:
            self.error_report_view.write(error_report)
            self.put(put, placement_view)
        put.put(target)

    def remove(self, move, placement_view):
        self.origin = placement_view.get_coordinate()
        error_report: ErrorReport = move.validateTarget(self.origin)
        if error_report is not None:
            self.error_report_view.write(error_report)
            self.remove(move, placement_view)
        move.remove(self.origin)

    def _put(self, move, placement_view: PlacementCoordinateView):
        target: Coordinate = placement_view.get_coordinate()
        error_report: ErrorReport = move.validateTarget(target)
        if error_report is not None:
            self.error_report_view.write(error_report)
            self.put(move, placement_view)
        move.put(target)

    def show_game(self, presenter_controller):
        self.board_view.write(presenter_controller)
        if presenter_controller.exist_tictactoe():
            ColorView.instance().writer_winner(presenter_controller.color())
