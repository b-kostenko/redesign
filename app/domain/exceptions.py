"""Domain exceptions."""

__all__ = ["ObjectNotFound", "InvalidCredentials"]


class ObjectNotFound(Exception):
    """Exception raised when an object is not found in the database."""

    def __init__(self, model_name: str, id_: str | int):
        self.model_name = model_name
        self.id_ = id_
        super().__init__(f"{model_name} with id '{id_}' not found")


class InvalidCredentials(Exception):
    """Exception raised when authentication credentials are invalid."""

    def __init__(self, message: str = "Invalid credentials provided"):
        self.message = message
        super().__init__(message)

