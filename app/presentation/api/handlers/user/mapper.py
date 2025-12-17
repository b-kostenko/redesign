from app.application.use_cases.user import dto
from app.presentation.api.schemas.user import UserCreate, UserResponse


class UserMapper:

    @staticmethod
    def schema_to_dto(user: UserCreate) -> dto.UserDTO:
        return dto.UserDTO(
            id=None,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            avatar_url=user.avatar_url or "",
        )

    @staticmethod
    def dto_to_schema(user: dto.UserDTO) -> UserResponse:
        return UserResponse(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            avatar_url=user.avatar_url,
        )
