from dataclasses import dataclass

__all__ = ['Company']

@dataclass(kw_only=True)
class Company:
    id: int
    name: str
    slug: str
    description: str | None = None
    domain: str
    zip: str
    email: str





