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

    def decode_token(self, token: str) -> dict:
        """Decode a token and return its payload."""
        raise NotImplementedError

    def verify_token(self, token: str, token_type: entities.TokenType) -> dict:
        """Verify the validity of a token of a specific type."""
        raise NotImplementedError
