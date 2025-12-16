from app.application.use_cases.auth.mapper import TokenMapper
from app.domain.exceptions.auth import InvalidCredentials
from app.domain.exceptions.user import UserNotFoundError
from app.domain.interfaces import (
    CompanyRepositoryInterface,
    PasswordHasherInterface,
    UserRepositoryInterface,
    TokenServiceInterface
)
from app.application.use_cases.auth import dto
from app.application.use_cases.company import dto as company_dto


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

    async def login(self, login_dto: dto.LoginDTO, tenant_company: company_dto.Company):
        user = await self.user_repository.get_user_by_email(email=login_dto.email)
        if not user:
            raise UserNotFoundError(email=login_dto.email)

        if user.company_id != tenant_company.id:
            raise InvalidCredentials()

        if not self.password_hasher.verify_password(plain_password=login_dto.password, hashed_password=user.password):
            raise InvalidCredentials()

        token = self.auth_security.generate_tokens_for_user(user)
        return TokenMapper.to_dto(token=token)

    # def generate_tokens_for_user(self, user: User) -> TokenSchema:
    #     access_token = create_token(
    #         payload={"sub": user.email},
    #         token_type=TokenType.ACCESS,
    #         expire_minutes=settings.token.ACCESS_TOKEN_EXPIRE_MINUTES,
    #     )
    #     refresh_token = create_token(
    #         payload={"sub": user.email},
    #         token_type=TokenType.REFRESH,
    #         expire_minutes=settings.token.REFRESH_TOKEN_EXPIRE_MINUTES,
    #     )
    #
    #     return TokenSchema(access_token=access_token, refresh_token=refresh_token, token_type=settings.token.TOKEN_TYPE)
