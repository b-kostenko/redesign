from app.presentation.api.schemas.client import ClientCreateSchema, ClientResponseSchema
from app.application.use_cases import dtos
from app.presentation.api.schemas.company import CompanyResponseSchema


class ClientMapper:

    @staticmethod
    def schema_to_dto(schema: ClientCreateSchema, company: dtos.Company) -> dtos.ClientDTO:
        return dtos.ClientDTO(
            id=None,
            name=schema.name,
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

    @staticmethod
    def dto_to_schema(dto_obj: dtos.ClientDTO) -> ClientResponseSchema:
        return ClientResponseSchema(
            id=dto_obj.id,
            name=dto_obj.name,
            company=CompanyResponseSchema(
                id=dto_obj.company.id,
                slug=dto_obj.company.slug,
                name=dto_obj.company.name,
                description=dto_obj.company.description,
                domain=dto_obj.company.domain,
                zip=dto_obj.company.zip,
                email=dto_obj.company.email
            )
        )