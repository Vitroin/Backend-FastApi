# Loads variables from .env into os.environ, then validates them into a typed Settings object.
# Import `settings` from here instead of reading os.environ in other modules.
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


class Settings(BaseSettings):
    # Shared secret NestJS sends in the X-Service-Token header
    service_token: SecretStr = Field(min_length=32)


settings = Settings()
