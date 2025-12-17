from abc import abstractmethod
from typing import Protocol

from app.domain import entities

__all__ = ["CompanyRepositoryInterface"]


class CompanyRepositoryInterface(Protocol):
    """Interface for company repository operations."""

    @abstractmethod
    async def get_company_by_name(self, name: str) -> entities.Company | None:
        """Retrieve a company by its name."""
        raise NotImplementedError

    @abstractmethod
    async def get_company_by_domain(self, domain: str) -> entities.Company | None:
        """Retrieve a company by its domain."""
        raise NotImplementedError

    @abstractmethod
    async def create_company(self, company_entity: entities.CompanyCreate) -> entities.Company:
        """Create a new company with the provided data."""
        raise NotImplementedError
