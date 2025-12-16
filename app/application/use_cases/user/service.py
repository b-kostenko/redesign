from app.application.use_cases.user import dto
from app.application.use_cases.company import dto as company_dto
from app.domain import entities
from app.application.use_cases.user.mapper import UserMapper
from app.domain.interfaces import PasswordHasherInterface, UserRepositoryInterface


class UserService:

    def __init__(self, user_repository: UserRepositoryInterface, password_hasher: PasswordHasherInterface):
        self.user_repository: UserRepositoryInterface = user_repository
        self.password_hasher: PasswordHasherInterface = password_hasher

    async def create_user(self, user_data: dto.User, company: company_dto.Company) -> dto.User:
        hashed_password = self.password_hasher.hash_password(user_data.password)
        user_data.password = hashed_password

        user_entity = UserMapper.to_entity(user_data, company_id=company.id)
        user = await self.user_repository.create_user(user_entity)
        return UserMapper.to_dto(user=user)
