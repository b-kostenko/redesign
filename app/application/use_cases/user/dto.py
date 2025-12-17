from dataclasses import dataclass

__all__ = ["UserDTO", "UserCreateDTO"]


@dataclass(slots=True, kw_only=True)
class UserCreateDTO:
    email: str
    password: str
    first_name: str
    last_name: str
    avatar_url: str


@dataclass(slots=True, kw_only=True)
class UserDTO(UserCreateDTO):
    id: int | None = None
    is_superuser: bool = False
