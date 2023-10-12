from python.controllers.local.errors.NotEmptyErrorReport import NotEmptyErrorReport


class NotEmptyErrorReportGenerator:

    @classmethod
    def get_error_report(cls, game):
        return NotEmptyErrorReport(game.get_empty_coordinates())
