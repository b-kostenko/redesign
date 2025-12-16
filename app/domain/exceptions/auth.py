from app.domain.exceptions.base import AuthError

__all__ = ['InvalidCredentials', 'TokenExpired']

class InvalidCredentials(AuthError):
    """Exception raised for invalid authentication credentials. """
    def __init__(self):
        super().__init__("Invalid email or password")


class TokenExpired(AuthError):
    """Exception raised when an authentication token has expired."""
    def __init__(self):
        super().__init__("Token has expired")