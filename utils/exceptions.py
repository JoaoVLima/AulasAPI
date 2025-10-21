"""
Exceptions
- This file defines custom exception classes for the application.
- Custom exceptions help improve error handling and make error messages more meaningful.

Example:
    class InvalidDataError(Exception):
        def __init__(self, message="Invalid data provided"):
            self.message = message
            super().__init__(self.message)
"""


class ResponseError(Exception):
    def __init__(self,
                 message: str = None,
                 status_code: int = 400,
                 response: dict = None
                 ):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)
