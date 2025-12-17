from app.domain import entities
from app.infrastructure.database import models

__all__ = ["UserMapper"]


class UserMapper:

    @staticmethod
    def to_model(user_entity: entities.User) -> models.User:
        return models.User(
            id=user_entity.id,
            email=user_entity.email,
            password=user_entity.password,
            first_name=user_entity.first_name,
            last_name=user_entity.last_name,
            avatar_url=user_entity.avatar_url or None,
            company_id=user_entity.company_id,
            is_superuser=user_entity.is_superuser,
        )

    @staticmethod
    def to_entity(user: models.User) -> entities.User:
        return entities.User(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            avatar_url=user.avatar_url or "",
            company_id=user.company_id,
            is_superuser=user.is_superuser,
        )
