#

"""
Exceptions which can be raised by py-Ultroid Itself.
"""


class pyUltroidError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...
