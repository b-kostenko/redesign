from dataclasses import dataclass

__all__ = ["Trial"]


@dataclass(kw_only=True)
class Trial:
    id: int | None = None
    name: str
    name_slug: str
    description: str | None = None
    compound_id: int
    client_id: int
