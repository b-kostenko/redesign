from app.application.use_cases.user import dto
from app.domain import entities

__all__ = ["UserMapper"]


class UserMapper:

    @staticmethod
    def to_entity(user: dto.UserDTO, company_id: int) -> entities.User:
        return entities.User(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
            email=user.email,
            avatar_url=user.avatar_url,
            company_id=company_id,
        )

    @staticmethod
    def to_dto(user: entities.User) -> dto.UserDTO:
        return dto.UserDTO(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
            email=user.email,
            avatar_url=user.avatar_url,
        )
