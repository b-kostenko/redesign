from fastapi import APIRouter
from starlette import status

from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.handlers.client.mapper import ClientMapper
from app.presentation.api.handlers.company.mapper import CompanyMapper
from app.presentation.api.schemas.client import ClientResponseSchema, ClientCreateSchema

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientResponseSchema, status_code=status.HTTP_201_CREATED)
async def create(payload: ClientCreateSchema, tenant_company: tenant_company_deps, client_service: client_service_deps):
    company_dto = CompanyMapper.entity_to_dto(company_entity=tenant_company)
    client_dto = ClientMapper.schema_to_dto(schema=payload, company=company_dto)
    created_client_dto = await client_service.create_client(client_data=client_dto)
    return ClientMapper.dto_to_schema(dto_obj=created_client_dto)


