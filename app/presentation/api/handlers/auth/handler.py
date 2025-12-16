from fastapi import APIRouter
from starlette import status

from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.dependencies.services.auth import auth_service_deps
from app.presentation.api.handlers.auth.mapper import AuthMapper
from app.presentation.api.schemas.auth import TokenSchema, UserLoginSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenSchema, status_code=status.HTTP_200_OK, description="Login")
async def login(login_data: UserLoginSchema, auth_service: auth_service_deps, tenant_company: tenant_company_deps):
    from app.presentation.api.handlers.company.mapper import CompanyMapper
    login_dto = AuthMapper.schema_to_dto(login_data)
    company_dto = CompanyMapper.entity_to_dto(company_entity=tenant_company)
    token = await auth_service.login(login_dto=login_dto, tenant_company=company_dto)
    return AuthMapper.dto_to_schema(token)

