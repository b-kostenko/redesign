from dataclasses import dataclass

__all__ = ["Company", "CompanyCreate"]


@dataclass(kw_only=True)
class CompanyCreate:
    name: str
    slug: str
    description: str | None = None
    domain: str
    zip: str
    email: str


@dataclass(kw_only=True)
class Company:
    id: int
    name: str
    slug: str
    description: str | None = None
    domain: str
    zip: str
    email: str
