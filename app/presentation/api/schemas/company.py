from pydantic import BaseModel, EmailStr

class CompanySchema(BaseModel):
    name: str
    description: str | None = None
    zip: str
    email: EmailStr


class CompanyCreateSchema(CompanySchema):
    pass


class CompanyResponseSchema(CompanySchema):
    id: int
    slug: str
    domain: str

    class Config:
        orm_mode = True