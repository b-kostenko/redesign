from typing import Annotated

from app.application.use_cases.auth.service import AuthService

from fastapi.params import Depends

from app.infrastructure.database.repositories.company.repository import CompanyRepositorySQLAlchemy
from app.infrastructure.database.repositories.user.repository import UserRepositorySQLAlchemy
from app.infrastructure.utils.hashing import BcryptPasswordHasher
from app.infrastructure.utils.security import JwtTokenService
from app.presentation.api.dependencies.services.company import get_company_repository
from app.presentation.api.dependencies.services.user import get_user_repository, get_password_hasher


def get_auth_security() -> JwtTokenService:
    return JwtTokenService()


def get_auth_service(
        user_repository: UserRepositorySQLAlchemy = Depends(get_user_repository),
        company_repository: CompanyRepositorySQLAlchemy = Depends(get_company_repository),
        password_hasher: BcryptPasswordHasher = Depends(get_password_hasher),
        auth_security: JwtTokenService = Depends(get_auth_security),
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
        company_repository=company_repository,
        password_hasher=password_hasher,
        auth_security=auth_security
    )


auth_service_deps = Annotated[AuthService, Depends(get_auth_service)]
