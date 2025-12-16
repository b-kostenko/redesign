from enum import StrEnum
from dataclasses import dataclass

__all__ = ['TokenType', 'Token']


class TokenType(StrEnum):
    ACCESS = "access"
    REFRESH = "refresh"


@dataclass(kw_only=True)
class Token:
    access_token: str
    refresh_token: str
    token_type: str