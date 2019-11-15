from sanic.exceptions import SanicException, add_status_code


class CustomException(SanicException):
    def __init__(self, message: str, code: int):
        super().__init__(message=message, status_code=code)


@add_status_code(401)
class ValidationErrorException(SanicException):
    def __init__(self):
        message = 'Validation error exception'
        super().__init__(message)
