from app.application.use_cases.client.dto import ClientCreateDTO, ClientDTO
from app.application.use_cases.client.mapper import ClientMapper
from app.domain.exceptions.client import ClientAlreadyExists
from app.domain.interfaces import ClientRepositoryInterface


class ClientService:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository: ClientRepositoryInterface = client_repository

    async def create_client(self, client_dto: ClientCreateDTO) -> ClientDTO:
        client = ClientMapper.dto_to_entity(dto=client_dto)
        client_exists = await self.client_repository.get_by_name(name=client.name, company_id=client.company_id)
        if client_exists:
            raise ClientAlreadyExists(name=client.name)

        client_data = await self.client_repository.create_client(client)

        return ClientMapper.entity_to_dto(entity=client_data, company=client_dto.company)
