from dataclasses import dataclass

__all__ = ["CompanyCreateDTO", "CompanyDTO"]


@dataclass(slots=True, kw_only=True)
class CompanyCreateDTO:
    name: str
    description: str | None = None
    zip: str
    email: str


@dataclass(slots=True, kw_only=True)
class CompanyDTO(CompanyCreateDTO):
    id: int
    slug: str
    domain: str
