from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TokenSettings(BaseSettings):
    SECRET_KEY: str = Field(default=..., alias="SECRET_KEY")
    ALGORITHM: str = Field(default="HS256", alias="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=15, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 7, alias="REFRESH_TOKEN_EXPIRE_MINUTES")  # 7 days
    TOKEN_TYPE: str = Field(default="Bearer", alias="TOKEN_TYPE")

    model_config = SettingsConfigDict(env_file=".env", env_prefix="JWT_", extra="ignore")