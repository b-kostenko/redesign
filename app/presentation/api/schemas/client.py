from app.presentation.api.schemas.company import CompanyResponseSchema
from pydantic import BaseModel


class ClientBaseSchema(BaseModel):
    name: str


class ClientCreateSchema(ClientBaseSchema):
    pass


class ClientResponseSchema(ClientBaseSchema):
    id: int
    company: CompanyResponseSchema
