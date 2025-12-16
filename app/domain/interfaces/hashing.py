from abc import abstractmethod
from typing import Protocol


class PasswordHasherInterface(Protocol):
    """Protocol for password hashing operations."""

    @abstractmethod
    def hash_password(self, password: str) -> str:
        """Hash a plain text password.

        Args:
            password: Plain text password to hash.

        Returns:
            Hashed password string.
        """
        raise NotImplementedError

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password.

        Args:
            plain_password: Plain text password to verify.
            hashed_password: Hashed password to compare against.

        Returns:
            True if passwords match, False otherwise.
        """
        raise NotImplementedError
