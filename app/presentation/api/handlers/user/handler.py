from fastapi import APIRouter
from starlette import status
from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.dependencies.services.user import user_service_deps
from app.presentation.api.handlers.user.mapper import UserMapper
from app.presentation.api.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, description="Create user")
async def create(payload: UserCreate, user_service: user_service_deps, tenant_company: tenant_company_deps):
    from app.presentation.api.handlers.company.mapper import CompanyMapper
    user_dto = UserMapper.schema_to_dto(user=payload)
    company_dto = CompanyMapper.entity_to_dto(company_entity=tenant_company)
    user = await user_service.create_user(user_data=user_dto, company=company_dto)
    return UserMapper.dto_to_schema(user=user)