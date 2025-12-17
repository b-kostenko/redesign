from app.domain import entities
from app.domain.interfaces import ClientRepositoryInterface
from app.infrastructure.database import models
from app.infrastructure.database.repositories.client.mapper import ClientMapper
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ClientRepositorySQLAlchemy(ClientRepositoryInterface):

    def __init__(self, session: AsyncSession, mapper: ClientMapper):
        self.session: AsyncSession = session
        self.mapper: ClientMapper = mapper

    async def create_client(self, client_entity: entities.ClientCreateEntity) -> entities.ClientEntity:
        """Create a new client with the provided data."""
        client_model = self.mapper.entity_to_model(entity=client_entity)
        self.session.add(client_model)
        await self.session.commit()
        await self.session.refresh(client_model)
        return self.mapper.model_to_entity(model=client_model)

    async def get_by_name(self, name: str, company_id: int) -> entities.ClientEntity | None:
        """Retrieve a client by its name."""
        query = select(models.Client).where(models.Client.name == name, models.Client.company_id == company_id)
        result = await self.session.execute(query)
        client_model = result.scalars().first()
        if not client_model:
            return None
        return self.mapper.model_to_entity(model=client_model)
