from app.presentation.api.dependencies.services.auth import current_user_deps
from app.presentation.api.dependencies.services.client import client_service_deps
from app.presentation.api.dependencies.services.company import tenant_company_deps
from app.presentation.api.handlers.client.mapper import ClientMapper
from app.presentation.api.schemas.client import ClientCreateSchema, ClientResponseSchema
from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientResponseSchema, status_code=status.HTTP_201_CREATED)
async def create(
    payload: ClientCreateSchema,
    tenant_company: tenant_company_deps,
    client_service: client_service_deps,
    _: current_user_deps,
) -> ClientResponseSchema:
    client_dto = ClientMapper.schema_to_dto(schema=payload, company=tenant_company)
    created_client_dto = await client_service.create_client(client_dto=client_dto)
    return ClientMapper.dto_to_schema(dto=created_client_dto)
