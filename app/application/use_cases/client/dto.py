from dataclasses import dataclass
from app.application.use_cases import dtos

__all__ = ['ClientDTO']

@dataclass(kw_only=True)
class ClientDTO:
    id: int | None = None
    name: str
    company: dtos.Company
