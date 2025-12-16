from app.application.use_cases import dtos

from app.domain import entities

__all__ = ["ClientMapper"]


class ClientMapper:

    @staticmethod
    def to_entity(dto_obj: dtos.ClientDTO) -> entities.ClientEntity:
        return entities.ClientEntity(
            id=dto_obj.id,
            name=dto_obj.name,
            company_id=dto_obj.company.id
        )

    @staticmethod
    def to_dto(entity: entities.ClientEntity, company: entities.Company) -> dtos.ClientDTO:
        return dtos.ClientDTO(
            id=entity.id,
            name=entity.name,
            company=dtos.Company(
                id=company.id,
                slug=company.slug,
                name=company.name,
                description=company.description,
                domain=company.domain,
                zip=company.zip,
                email=company.email
            )
        )
