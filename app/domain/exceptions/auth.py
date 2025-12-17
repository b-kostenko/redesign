from app.domain.exceptions.base import AuthError

__all__ = ["InvalidCredentialsError", "TokenExpiredError"]


class InvalidCredentialsError(AuthError):
    """Exception raised for invalid authentication credentials."""

    def __init__(self) -> None:
        super().__init__("Invalid email or password")


class TokenExpiredError(AuthError):
    """Exception raised when an authentication token has expired."""

    def __init__(self) -> None:
        super().__init__("Token has expired")
