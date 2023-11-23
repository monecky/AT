class AtError(Exception):
    """
    An error that occurs while manipulating a `Attack tree`
    """

    def __init__(self, message: str):
        """
        Constructor
        :param message: The error message
        :type message: str
        """
        super(AtError, self).__init__(message)
