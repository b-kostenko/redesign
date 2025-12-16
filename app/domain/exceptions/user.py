from app.domain.exceptions import base

__all__ = ['UserAlreadyExists', 'UserNotFoundError']


class UserAlreadyExists(base.AlreadyExistsError):
    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' already exists")

class UserNotFoundError(base.NotFoundError):
    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' not found")