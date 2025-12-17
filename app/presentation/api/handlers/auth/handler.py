from app.presentation.api.dependencies.services.auth import auth_service_deps
from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.handlers.auth.mapper import AuthMapper
from app.presentation.api.schemas.auth import TokenSchema, UserLoginSchema
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenSchema, status_code=status.HTTP_200_OK, description="Login")
async def login(
    login_data: UserLoginSchema, auth_service: auth_service_deps, tenant_company: tenant_company_deps
) -> TokenSchema:
    login_dto = AuthMapper.schema_to_dto(login_data)
    token = await auth_service.login(login_dto=login_dto, tenant_company=tenant_company)
    return AuthMapper.dto_to_schema(token)
