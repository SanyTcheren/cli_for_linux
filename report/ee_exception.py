"""Exception for eereport package."""

class NotGdataFile(Exception):
    """Exception for general_data file."""

    def __init__(self):
        message='Отсутствует или поврежден файл с общими данными.'
        super().__init__(message)

class NotPowerFile(Exception):
    """Exception for power profile file."""

    def __init__(self):
        message='Отсутствует или поврежден файл с профилем мощности.'
        super().__init__(message)
