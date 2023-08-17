from enum import Enum

from python.controllers.local.errors.NotEmptyErrorReportGenerator import NotEmptyErrorReportGenerator
from python.controllers.local.errors.NotPropertyErrorReportGenerator import NotPropertyErrorReportGenerator
from python.controllers.local.errors.RepeatedCoordinateErrorReportGenerator import \
    RepeatedCoordinateErrorReportGenerator


class ErrorGeneratorType(Enum):

    NOT_EMPTY = NotEmptyErrorReportGenerator()

    REPEATED_COORDINATE = RepeatedCoordinateErrorReportGenerator()

    NOT_PROPERTY = NotPropertyErrorReportGenerator()