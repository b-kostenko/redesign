from app.domain.exceptions import base

__all__ = ["ClientAlreadyExists"]


class ClientAlreadyExists(base.AlreadyExistsError):
    def __init__(self, name: str):
        super().__init__(f"Client with name '{name}' already exists.")
