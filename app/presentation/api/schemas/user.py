from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar_url: str | None = None


class UserCreate(UserSchema):
    password: str = Field(..., min_length=8)


class UserUpdate(UserSchema):
    first_name: str | None = None
    last_name: str | None = None
    avatar_url: str | None = None
    password: str | None = Field(None, min_length=8)

class UserResponse(UserSchema):
    id: int

    class Config:
        from_attributes = True

