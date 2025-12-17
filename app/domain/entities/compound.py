from dataclasses import dataclass

__all__ = ["Compound"]


@dataclass(kw_only=True)
class Compound:
    id: int | None = None
    name: str
    name_slug: str
    description: str | None = None
    client_id: int
