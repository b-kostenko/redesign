from app.presentation.api.dependencies.services.company import company_service_deps
from app.presentation.api.handlers.company.mapper import CompanyMapper
from app.presentation.api.schemas.company import CompanyCreateSchema, CompanyResponseSchema
from fastapi import APIRouter

router = APIRouter(
    prefix="/public/companies",
    tags=["Public / Companies"],
)


@router.post("/", response_model=CompanyResponseSchema)
async def create(payload: CompanyCreateSchema, company_service: company_service_deps) -> CompanyResponseSchema:
    company_dto = CompanyMapper.schema_to_dto(schema=payload)
    company = await company_service.create_company(company_data=company_dto)
    return CompanyMapper.dto_to_schema(dto=company)
