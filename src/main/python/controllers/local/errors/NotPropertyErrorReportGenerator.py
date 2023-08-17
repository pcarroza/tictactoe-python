from python.controllers.local.errors.NotPropertyErrorReport import NotPropertyErrorReport


class NotPropertyErrorReportGenerator:

    @classmethod
    def get_error_report(cls, game):
        return NotPropertyErrorReport(game.get_player_coordinate())
