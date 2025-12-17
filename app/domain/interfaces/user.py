from abc import abstractmethod
from typing import Protocol

from app.domain import entities

__all__ = ["UserRepositoryInterface"]


class UserRepositoryInterface(Protocol):
    """Interface for user repository operations."""

    @abstractmethod
    async def get_user_by_email(self, email: str) -> entities.User | None:
        """Get user by email."""
        raise NotImplementedError

    @abstractmethod
    async def get_all_users(self, company_id: int) -> list[entities.User] | None:
        """Get all users for a given company."""
        raise NotImplementedError

    @abstractmethod
    async def create_user(self, user_entity: entities.User) -> entities.User:
        """Create a new user with the provided data."""
        raise NotImplementedError
