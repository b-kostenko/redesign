from typing import Annotated

from app.application.use_cases.user.service import UserService
from app.infrastructure.database.repositories.user.mapper import UserMapper
from app.infrastructure.database.repositories.user.repository import UserRepositorySQLAlchemy
from app.infrastructure.database.session import create_async_session
from app.infrastructure.utils.hashing import BcryptPasswordHasher
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession


def get_user_mapper() -> UserMapper:
    return UserMapper()


def get_user_repository(
    session: AsyncSession = Depends(create_async_session),
    mapper: UserMapper = Depends(get_user_mapper),
) -> UserRepositorySQLAlchemy:
    return UserRepositorySQLAlchemy(session=session, mapper=mapper)


def get_password_hasher() -> BcryptPasswordHasher:
    return BcryptPasswordHasher()


def get_user_service(
    user_repository: UserRepositorySQLAlchemy = Depends(get_user_repository),
    password_hasher: BcryptPasswordHasher = Depends(get_password_hasher),
) -> UserService:
    return UserService(user_repository=user_repository, password_hasher=password_hasher)


user_service_deps = Annotated[UserService, Depends(get_user_service)]
