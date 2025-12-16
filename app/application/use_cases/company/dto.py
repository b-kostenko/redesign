from dataclasses import dataclass

__all__ = ['Company']

@dataclass(slots=True, kw_only=True)
class Company:
    id: int | None = None
    name: str
    slug: str | None = None
    description: str | None = None
    domain: str | None = None
    zip: str
    email: str
