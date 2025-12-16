from fastapi import APIRouter
from starlette import status
from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.dependencies.services.user import user_service_deps
from app.presentation.api.handlers.user.mapper import UserMapper
from app.presentation.api.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, description="Create user")
async def create(payload: UserCreate, user_service: user_service_deps, tenant_company: tenant_company_deps):
    user_dto = UserMapper.schema_to_dto(user=payload)
    user = await user_service.create_user(user_data=user_dto, company=tenant_company)
    return UserMapper.dto_to_schema(user=user)