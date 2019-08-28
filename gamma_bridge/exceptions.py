"""
Exception types for Gamification operations.
"""
class GammaException(Exception):
    """
    Base exception class for Gamma application.
    """

    def __init__(self, message=None, *args):
        if message is None:
            self.message = 'An GammaException occurred without a specific message'
        super(GammaException, self).__init__(message, *args)


class GammaConnectionError(GammaException):
    """
    Exception class for errors connecting to external Gamma service.
    """

    def __init__(self, message=None, *args):
        self.message = "External connection error to the rg-gamification-traking application. {}".format(message)
        super(GammaConnectionError, self).__init__(self.message, *args)
