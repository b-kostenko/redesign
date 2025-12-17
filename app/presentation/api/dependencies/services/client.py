from typing import Annotated

from app.application.use_cases.client.service import ClientService
from app.infrastructure.database.repositories.client.mapper import ClientMapper
from app.infrastructure.database.repositories.client.repository import ClientRepositorySQLAlchemy
from app.infrastructure.database.session import create_async_session
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession


def get_client_mapper() -> ClientMapper:
    return ClientMapper()


def get_client_repository(
    session: AsyncSession = Depends(create_async_session), client_mapper: ClientMapper = Depends(get_client_mapper)
) -> ClientRepositorySQLAlchemy:
    return ClientRepositorySQLAlchemy(session=session, mapper=client_mapper)


def get_client_service(
    client_repository: ClientRepositorySQLAlchemy = Depends(get_client_repository),
) -> ClientService:
    return ClientService(client_repository=client_repository)


client_service_deps = Annotated[ClientService, Depends(get_client_service)]
