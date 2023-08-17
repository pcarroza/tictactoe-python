from python.controllers.local.errors.ErrorReport import ErrorReport
from python.controllers.local.errors.ErrorReportVisitor import ErrorReportVisitor


class ErrorReportView(ErrorReportVisitor):

    def write(self, error_report: ErrorReport):
        error_report.accept(self)

