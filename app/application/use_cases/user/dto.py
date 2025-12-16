from dataclasses import dataclass

__all__ = ['User']


@dataclass(slots=True, kw_only=True)
class User:
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    avatar_url: str
    is_superuser: bool = False