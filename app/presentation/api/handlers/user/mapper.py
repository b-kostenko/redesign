from app.presentation.api.schemas.user import UserCreate, UserResponse
from app.application.use_cases.user import dto


class UserMapper:

    @staticmethod
    def schema_to_dto(user: UserCreate) -> dto.User:
        return dto.User(
            id=None,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            avatar_url=user.avatar_url or "",
        )

    @staticmethod
    def dto_to_schema(user: dto.User) -> UserResponse:
        return UserResponse(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            avatar_url=user.avatar_url,
        )
