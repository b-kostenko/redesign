import hashlib
from typing import final

from app.domain.interfaces.hashing import PasswordHasherInterface
from passlib.context import CryptContext


@final
class BcryptPasswordHasher(PasswordHasherInterface):
    """Bcrypt implementation of PasswordHasherInterface.

    This is an infrastructure concern - the actual implementation
    of the domain service interface.
    """

    def __init__(self) -> None:
        """Initialize the password hasher with bcrypt context."""
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _pre_hash(self, password: str) -> str:
        """
        bcrypt limitation: 72 bytes max
        -> pre-hash with sha256
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def hash_password(self, password: str) -> str:
        """Hash a plain text password using bcrypt.

        Args:
            password: Plain text password to hash.

        Returns:
            Hashed password string.
        """
        pre_hashed = self._pre_hash(password)
        return self._pwd_context.hash(pre_hashed)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password.

        Args:
            plain_password: Plain text password to verify.
            hashed_password: Hashed password to compare against.

        Returns:
            True if passwords match, False otherwise.
        """
        pre_hashed = self._pre_hash(plain_password)
        return self._pwd_context.verify(pre_hashed, hashed_password)
