from typing import Protocol

from app.domain import entities


class AuthRepositoryInterface(Protocol):
    """Interface for authentication repository operations."""
    
    async def get(self, email: str) -> entities.User | None:
        """Get user by email."""
        ...
