from app.application.use_cases.company import dto
from app.application.use_cases.company.mapper import CompanyMapper as ApplicationCompanyMapper
from app.domain import entities
from app.presentation.api.schemas.company import CompanyCreateSchema, CompanyResponseSchema


class CompanyMapper:

    @staticmethod
    def schema_to_dto(company_schema: CompanyCreateSchema) -> dto.Company:
        return dto.Company(
            id=None,
            name=company_schema.name,
            description=company_schema.description,
            zip=company_schema.zip,
            email=company_schema.email,
        )

    @staticmethod
    def entity_to_dto(company_entity: entities.Company) -> dto.Company:
        """Convert domain entity to application DTO."""
        return ApplicationCompanyMapper.to_dto(company=company_entity)

    @staticmethod
    def dto_to_schema(company_dto: dto.Company) -> CompanyResponseSchema:
        return CompanyResponseSchema(
            id=company_dto.id,
            name=company_dto.name,
            description=company_dto.description,
            slug=company_dto.slug,
            domain=company_dto.domain,
            zip=company_dto.zip,
            email=company_dto.email,
        )

    @staticmethod
    def entity_to_schema(company_entity: entities.Company) -> CompanyResponseSchema:
        return CompanyResponseSchema(
            id=company_entity.id,
            name=company_entity.name,
            description=company_entity.description,
            slug=company_entity.slug,
            domain=company_entity.domain,
            zip=company_entity.zip,
            email=company_entity.email,
        )