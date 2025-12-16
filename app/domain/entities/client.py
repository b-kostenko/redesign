from dataclasses import dataclass

__all__ = ['ClientEntity']

@dataclass(kw_only=True)
class ClientEntity:
    id: int | None = None
    name: str
    company_id: int
