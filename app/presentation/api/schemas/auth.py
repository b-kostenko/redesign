from pydantic import BaseModel, EmailStr


class UserLoginSchema(BaseModel):
    """Schema for user login data."""

    email: EmailStr
    password: str

    class Config:
        str_min_length = 1


class TokenSchema(BaseModel):
    token_type: str
    access_token: str
    refresh_token: str
