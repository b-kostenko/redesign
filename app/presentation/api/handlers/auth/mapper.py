from app.application.use_cases.auth import dto
from app.presentation.api.schemas.auth import TokenSchema, UserLoginSchema


class AuthMapper:

    @staticmethod
    def schema_to_dto(login_schema: UserLoginSchema) -> dto.LoginDTO:
        return dto.LoginDTO(email=login_schema.email, password=login_schema.password)

    @staticmethod
    def dto_to_schema(token: dto.Token) -> TokenSchema:
        return TokenSchema(
            token_type=token.token_type, access_token=token.access_token, refresh_token=token.refresh_token
        )
