from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.dependencies.services.user import user_service_deps
from app.presentation.api.handlers.user.mapper import UserMapper
from app.presentation.api.schemas.user import UserCreate, UserResponse
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, description="Create user")
async def create(
    payload: UserCreate, user_service: user_service_deps, tenant_company: tenant_company_deps
) -> UserResponse:
    user_dto = UserMapper.schema_to_dto(user=payload)
    user = await user_service.create_user(user_data=user_dto, company=tenant_company)
    return UserMapper.dto_to_schema(user=user)


@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK, description="Get all users")
async def get_all(user_service: user_service_deps, tenant_company: tenant_company_deps) -> list[UserResponse]:
    users_dto = await user_service.get_all_users(company=tenant_company)
    if not users_dto:
        return []
    return [UserMapper.dto_to_schema(user=user) for user in users_dto]
