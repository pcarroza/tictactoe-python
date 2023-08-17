from python.controllers.local.errors.ErrorReport import ErrorReport


class RepeatedCoordinateErrorReport(ErrorReport):

    def __int__(self, coordinates):
        super().__init__(coordinates)

    def accept(self, error_report_visitor):
        error_report_visitor.visit(self)
