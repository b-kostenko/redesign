from app.application.use_cases.auth import dto
from app.domain import entities

__all__ = ["TokenMapper"]


class TokenMapper:

    @staticmethod
    def to_entity(token: dto.Token) -> entities.Token:
        return entities.Token(
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            token_type=token.token_type
        )

    @staticmethod
    def to_dto(token: entities.Token) -> dto.Token:
        return dto.Token(
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            token_type=token.token_type
        )
