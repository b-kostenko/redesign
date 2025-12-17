__all__ = ["AlreadyExistsError", "NotFoundError", "AuthError"]


class DomainError(Exception):
    """Base class for all domain errors"""

    pass


class AlreadyExistsError(DomainError):
    """Base class for 'already exists' domain errors"""

    pass


class ValidationError(DomainError):
    """Base class for validation errors in the domain layer"""

    pass


class NotFoundError(DomainError):
    """Base class for 'not found' domain errors"""

    pass


class AuthError(DomainError):
    """Base class for all authentication errors"""

    pass
