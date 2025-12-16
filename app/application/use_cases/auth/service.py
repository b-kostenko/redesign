from app.application.use_cases.auth.mapper import TokenMapper
from app.domain.interfaces import CompanyRepositoryInterface, PasswordHasherInterface
from app.domain.interfaces.auth import AuthRepositoryInterface
from app.domain.exceptions import ObjectNotFound, InvalidCredentials
from app.application.use_cases.auth import dto
from app.application.use_cases.company import dto as company_dto
from app.domain.interfaces.security import TokenServiceInterface


class AuthService:
    def __init__(
            self,
            user_repository: AuthRepositoryInterface,
            company_repository: CompanyRepositoryInterface,
            password_hasher: PasswordHasherInterface,
            auth_security: TokenServiceInterface,
    ) -> None:
        self.user_repository: AuthRepositoryInterface = user_repository
        self.company_repository: CompanyRepositoryInterface = company_repository
        self.password_hasher: PasswordHasherInterface = password_hasher
        self.auth_security: TokenServiceInterface = auth_security

    async def login(self, login_dto: dto.LoginDTO, tenant_company: company_dto.Company):
        user = await self.user_repository.get(login_dto.email)
        if not user:
            raise ObjectNotFound(model_name="User", id_=login_dto.email)

        if user.company_id != tenant_company.id:
            raise InvalidCredentials("User does not belong to this company")

        if not self.password_hasher.verify_password(plain_password=login_dto.password, hashed_password=user.password):
            raise InvalidCredentials("Invalid credentials provided")

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