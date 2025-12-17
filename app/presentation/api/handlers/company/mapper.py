from app.application.use_cases.company.dto import CompanyCreateDTO, CompanyDTO
from app.presentation.api.schemas.company import CompanyCreateSchema, CompanyResponseSchema


class CompanyMapper:

    @staticmethod
    def schema_to_dto(schema: CompanyCreateSchema) -> CompanyCreateDTO:
        return CompanyCreateDTO(
            name=schema.name,
            description=schema.description,
            zip=schema.zip,
            email=schema.email,
        )

    @staticmethod
    def dto_to_schema(dto: CompanyDTO) -> CompanyResponseSchema:
        return CompanyResponseSchema(
            id=dto.id,
            name=dto.name,
            description=dto.description,
            slug=dto.slug,
            domain=dto.domain,
            zip=dto.zip,
            email=dto.email,
        )
