from app.application.use_cases.auth.dto import LoginDTO, Token
from app.application.use_cases.auth.mapper import TokenMapper
from app.application.use_cases.company.dto import CompanyDTO
from app.application.use_cases.user.dto import UserDTO
from app.application.use_cases.user.mapper import UserMapper
from app.domain.exceptions.auth import InvalidCredentialsError
from app.domain.exceptions.company import CompanyMismatchError
from app.domain.exceptions.user import UserNotFoundError
from app.domain.interfaces import (
    CompanyRepositoryInterface,
    PasswordHasherInterface,
    TokenServiceInterface,
    UserRepositoryInterface,
)


class AuthService:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        company_repository: CompanyRepositoryInterface,
        password_hasher: PasswordHasherInterface,
        auth_security: TokenServiceInterface,
    ) -> None:
        self.user_repository: UserRepositoryInterface = user_repository
        self.company_repository: CompanyRepositoryInterface = company_repository
        self.password_hasher: PasswordHasherInterface = password_hasher
        self.auth_security: TokenServiceInterface = auth_security

    async def login(self, login_dto: LoginDTO, tenant_company: CompanyDTO) -> Token:
        user = await self.user_repository.get_user_by_email(email=login_dto.email)
        if not user:
            raise UserNotFoundError(email=login_dto.email)

        if user.company_id != tenant_company.id:
            raise InvalidCredentialsError()

        if not self.password_hasher.verify_password(plain_password=login_dto.password, hashed_password=user.password):
            raise InvalidCredentialsError()

        token = self.auth_security.generate_tokens_for_user(user)
        return TokenMapper.to_dto(token=token)

    async def get_current_user(self, token: str, current_company: CompanyDTO) -> UserDTO:
        payload = self.auth_security.decode_token(token)
        user_email = payload.get("sub")
        if not user_email:
            raise InvalidCredentialsError()

        user = await self.user_repository.get_user_by_email(email=user_email)
        if not user:
            raise InvalidCredentialsError()

        if user.company_id != current_company.id:
            raise CompanyMismatchError(user_company_id=user.company_id, current_company_id=current_company.id)

        return UserMapper.to_dto(user=user)
