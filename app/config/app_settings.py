from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application core settings."""

    DOMAIN: str = Field(default="localhost", alias="DOMAIN")

    HOST: str = Field(default="0.0.0.0", alias="HOST")
    PORT: int = Field(default=8000, alias="PORT")
    PROJECT_NAME: str = Field(default="SubdomainNexus", alias="PROJECT_NAME")
    PROJECT_VERSION: str = Field(default="1.0.0", alias="PROJECT_VERSION")
    DEBUG: bool = Field(default=False, alias="DEBUG")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")
