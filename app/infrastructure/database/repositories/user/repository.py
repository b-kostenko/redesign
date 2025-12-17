from app.domain import entities
from app.domain.interfaces.user import UserRepositoryInterface
from app.infrastructure.database.models import User as UserModel
from app.infrastructure.database.repositories.user.mapper import UserMapper
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepositorySQLAlchemy(UserRepositoryInterface):

    def __init__(self, session: AsyncSession, mapper: UserMapper):
        self.session: AsyncSession = session
        self.mapper: UserMapper = mapper

    async def get_user_by_email(self, email: str) -> entities.User | None:
        """Get user by email."""
        query = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(query)
        user_model = result.scalars().first()
        if not user_model:
            return None
        return self.mapper.to_entity(user_model)

    async def create_user(self, user_entity: entities.User) -> entities.User:
        user_model = self.mapper.to_model(user_entity)
        self.session.add(user_model)
        await self.session.commit()
        await self.session.refresh(user_model)
        return self.mapper.to_entity(user_model)
