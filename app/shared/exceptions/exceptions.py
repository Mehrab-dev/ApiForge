

class AppException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class BadRequestException(AppException):
    def __init__(self, message: str = "bad request"):
        super().__init__(message=message, status_code=400)


class UnauthorizedException(AppException):
    def __init__(self, message: str = "unauthorized"):
        super().__init__(message=message, status_code=401)


class ForbiddenException(AppException):
    def __init__(self, message: str = "forbidden"):
        super().__init__(message=message, status_code=403)


class NotFoundException(AppException):
    def __init__(self, message: str = "resource not found"):
        super().__init__(message=message, status_code=404)


class ConflictException(AppException):

    def __init__(self, message: str = "conflict"):
        super().__init__(message=message, status_code=409)


class InternalServerException(AppException):
    def __init__(self, message: str = "internal server error"):
        super().__init__(message=message, status_code=500)