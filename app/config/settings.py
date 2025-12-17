from app.config import AppSettings, DatabaseSettings, TokenSettings
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app: AppSettings = Field(default_factory=AppSettings)
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    token: TokenSettings = Field(default_factory=TokenSettings)


settings = Settings()
