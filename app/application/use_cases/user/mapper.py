from app.domain import entities
from app.application.use_cases.user import dto
__all__ = ["UserMapper"]


class UserMapper:

    @staticmethod
    def to_entity(user: dto.User, company_id: int) -> entities.User:
        return entities.User(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
            email=user.email,
            avatar_url=user.avatar_url,
            company_id=company_id
        )

    @staticmethod
    def to_dto(user: entities.User) -> dto.User:
        return dto.User(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
            email=user.email,
            avatar_url=user.avatar_url,
        )
