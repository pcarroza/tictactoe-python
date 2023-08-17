from python.controllers.local.errors.ErrorReport import ErrorReport


class NotEmptyErrorReport(ErrorReport):

    def __init__(self, coordinates):
        super().__init__(coordinates)

    def accept(self, error_report_visitor):
        error_report_visitor.visit(self)
