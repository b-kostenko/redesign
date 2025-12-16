from abc import abstractmethod
from typing import Protocol

from app.domain import entities

__all__ = ["UserRepositoryInterface"]


class UserRepositoryInterface(Protocol):
    """Interface for user repository operations."""
    @abstractmethod
    async def create_user(self, user_entity: entities.User) -> entities.User:
        """Create a new user with the provided data."""
        raise NotImplementedError