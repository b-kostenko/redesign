from app.application.use_cases.client.dto import ClientCreateDTO, ClientDTO
from app.application.use_cases.company.dto import CompanyDTO
from app.presentation.api.schemas.client import ClientCreateSchema, ClientResponseSchema
from app.presentation.api.schemas.company import CompanyResponseSchema


class ClientMapper:

    @staticmethod
    def schema_to_dto(schema: ClientCreateSchema, company: CompanyDTO) -> ClientCreateDTO:
        return ClientCreateDTO(
            name=schema.name,
            company=company,
        )

    @staticmethod
    def dto_to_schema(dto: ClientDTO) -> ClientResponseSchema:
        return ClientResponseSchema(
            id=dto.id,
            name=dto.name,
            company=CompanyResponseSchema(
                id=dto.company.id,
                slug=dto.company.slug,
                name=dto.company.name,
                description=dto.company.description,
                domain=dto.company.domain,
                zip=dto.company.zip,
                email=dto.company.email,
            ),
        )
