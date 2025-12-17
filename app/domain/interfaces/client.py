from abc import abstractmethod
from typing import Protocol

from app.domain import entities

__all__ = ["ClientRepositoryInterface"]


class ClientRepositoryInterface(Protocol):
    """Interface for client repository operations."""

    @abstractmethod
    async def create_client(self, client_entity: entities.ClientCreateEntity) -> entities.ClientEntity:
        """Create a new client with the provided data."""
        raise NotImplementedError

    @abstractmethod
    async def get_by_name(self, name: str, company_id: int) -> entities.ClientEntity | None:
        """Retrieve a client by its name."""
        raise NotImplementedError
