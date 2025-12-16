from typing import Protocol

from app.domain import entities

__all = ["TokenServiceInterface"]


class TokenServiceInterface(Protocol):
    """Interface for token service operations."""

    def generate_tokens_for_user(self, user: entities.User) -> entities.Token:
        """Generate access and refresh tokens for a given user."""
        raise NotImplementedError

    def create_token(self, payload: dict, token_type: entities.TokenType, expire_minutes: int) -> str:
        """Create a token of a specific type for a given user ID."""
        raise NotImplementedError
