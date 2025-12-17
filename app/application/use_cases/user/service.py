from app.application.use_cases.company.dto import CompanyDTO
from app.application.use_cases.user.dto import UserDTO
from app.application.use_cases.user.mapper import UserMapper
from app.domain.exceptions.user import UserAlreadyExistsError
from app.domain.interfaces import PasswordHasherInterface, UserRepositoryInterface


class UserService:

    def __init__(self, user_repository: UserRepositoryInterface, password_hasher: PasswordHasherInterface):
        self.user_repository: UserRepositoryInterface = user_repository
        self.password_hasher: PasswordHasherInterface = password_hasher

    async def create_user(self, user_data: UserDTO, company: CompanyDTO) -> UserDTO:
        hashed_password = self.password_hasher.hash_password(user_data.password)
        user_data.password = hashed_password
        user_entity = UserMapper.to_entity(user_data, company_id=company.id)
        user_exists = await self.user_repository.get_user_by_email(email=user_entity.email)
        if user_exists:
            raise UserAlreadyExistsError(email=user_entity.email)

        user = await self.user_repository.create_user(user_entity)
        return UserMapper.to_dto(user=user)
