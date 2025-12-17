from typing import Annotated

from app.application.use_cases.auth.service import AuthService
from app.application.use_cases.user.dto import UserDTO
from app.infrastructure.database.repositories.company.repository import CompanyRepositorySQLAlchemy
from app.infrastructure.database.repositories.user.repository import UserRepositorySQLAlchemy
from app.infrastructure.utils.hashing import BcryptPasswordHasher
from app.infrastructure.utils.security import JwtTokenService
from app.presentation.api.dependencies.services.company import get_company_repository, tenant_company_deps
from app.presentation.api.dependencies.services.user import get_password_hasher, get_user_repository
from fastapi.params import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

http_bearer = HTTPBearer()


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
        auth_security=auth_security,
    )


auth_service_deps = Annotated[AuthService, Depends(get_auth_service)]
token_deps = Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)]


async def get_current_user(
    auth_service: auth_service_deps, tenant_company: tenant_company_deps, token: token_deps
) -> UserDTO:

    return await auth_service.get_current_user(token.credentials, current_company=tenant_company)


current_user_deps = Annotated[UserDTO, Depends(get_current_user)]
