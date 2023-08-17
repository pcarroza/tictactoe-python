from python.controllers.local.errors.RepeatedCoordinateErrorReport import RepeatedCoordinateErrorReport


class RepeatedCoordinateErrorReportGenerator:

    @classmethod
    def get_error_report(cls, game):
        return RepeatedCoordinateErrorReport(game.get_empty_coordinate())
