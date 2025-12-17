from dataclasses import dataclass
from enum import StrEnum

__all__ = ["UserRole", "User"]


class UserRole(StrEnum):
    ADMIN = "admin"
    MEMBER = "member"


@dataclass(frozen=True, slots=True, kw_only=True)
class User:
    id: int | None = None
    email: str
    password: str
    first_name: str
    last_name: str
    avatar_url: str
    company_id: int
    is_superuser: bool = False
