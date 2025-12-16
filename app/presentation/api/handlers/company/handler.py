from fastapi import APIRouter

from app.presentation.api.dependencies.services.company import company_service_deps, tenant_company_deps
from app.presentation.api.handlers.company.mapper import CompanyMapper
from app.presentation.api.schemas.company import CompanyCreateSchema, CompanyResponseSchema

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/", response_model=CompanyResponseSchema)
async def create(payload: CompanyCreateSchema, company_service: company_service_deps):
    company_dto = CompanyMapper.schema_to_dto(company_schema=payload)
    company_dto = await company_service.create_company(company_data=company_dto)
    return CompanyMapper.dto_to_schema(company_dto=company_dto)

@router.get("/", response_model=CompanyResponseSchema)
async def detail(tenant_company: tenant_company_deps):
    company = CompanyMapper.entity_to_schema(company_entity=tenant_company)
    return company