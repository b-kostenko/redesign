from app.application.use_cases.client.dto import ClientCreateDTO, ClientDTO
from app.application.use_cases.company.dto import CompanyDTO
from app.domain import entities

__all__ = ["ClientMapper"]


class ClientMapper:

    @staticmethod
    def dto_to_entity(dto: ClientCreateDTO) -> entities.ClientCreateEntity:
        return entities.ClientCreateEntity(name=dto.name, company_id=dto.company.id)

    @staticmethod
    def entity_to_dto(entity: entities.ClientEntity, company: CompanyDTO) -> ClientDTO:
        return ClientDTO(
            id=entity.id,
            name=entity.name,
            company=company,
        )
