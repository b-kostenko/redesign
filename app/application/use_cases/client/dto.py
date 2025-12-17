from dataclasses import dataclass

from app.application.use_cases.company.dto import CompanyDTO

__all__ = ["ClientDTO", "ClientCreateDTO"]


@dataclass(kw_only=True)
class ClientCreateDTO:
    name: str
    company: CompanyDTO


@dataclass(kw_only=True)
class ClientDTO(ClientCreateDTO):
    id: int
