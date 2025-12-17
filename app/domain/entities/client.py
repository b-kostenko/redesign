from dataclasses import dataclass

__all__ = ["ClientEntity", "ClientCreateEntity"]


@dataclass(kw_only=True)
class ClientCreateEntity:
    name: str
    company_id: int


@dataclass(kw_only=True)
class ClientEntity(ClientCreateEntity):
    id: int
