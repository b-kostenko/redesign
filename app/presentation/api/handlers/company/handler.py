from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.handlers.company.mapper import CompanyMapper
from app.presentation.api.schemas.company import CompanyResponseSchema
from fastapi import APIRouter

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("/", response_model=CompanyResponseSchema)
async def detail(tenant_company: tenant_company_deps) -> CompanyResponseSchema:
    company = CompanyMapper.dto_to_schema(dto=tenant_company)
    return company
