from dataclasses import dataclass

__all__ = ["LoginDTO", "TokenType", "Token"]

from enum import StrEnum


class TokenType(StrEnum):
    ACCESS = "access"
    REFRESH = "refresh"



@dataclass(slots=True, kw_only=True)
class LoginDTO:
    email: str
    password: str


@dataclass(kw_only=True)
class Token:
    access_token: str
    refresh_token: str
    token_type: TokenType = TokenType.ACCESS