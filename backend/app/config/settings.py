import os

from app import CONFIG_PATH
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_env():
    "Path to get enviorment variables and secrets"

    environment_name = os.getenv("ENVIRONMENT", "LOCAL").lower()

    candidate_files = [
        CONFIG_PATH / "env" / f".env.{environment_name}",
        CONFIG_PATH / "secrets" / f".secrets.{environment_name}",
    ]

    return [str(file_path) for file_path in candidate_files if file_path.exists()]


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file = get_env(),
        case_sensitive=True,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: SecretStr = Field(validation_alias = "DATABASE_URL")

    kalshi_url: str = Field(validation_alias = "KALSHI_URL")
