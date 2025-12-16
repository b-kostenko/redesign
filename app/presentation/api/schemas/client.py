from pydantic import BaseModel

from app.presentation.api.schemas.company import CompanyResponseSchema


class ClientBaseSchema(BaseModel):
    name: str


class ClientCreateSchema(ClientBaseSchema):
    pass


class ClientResponseSchema(ClientBaseSchema):
    id: int
    company: CompanyResponseSchema
