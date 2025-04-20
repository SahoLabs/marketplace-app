# app/core/config.py

from pydantic_settings import BaseSettings  # ✅ Correct import in Pydantic v2
from typing import ClassVar  # Import ClassVar

class Settings(BaseSettings):
    PROJECT_NAME: str = "Marketplace"
    DATABASE_URL: ClassVar[str] = "sqlite:///app/db/app.db"  # Annotated as ClassVar
    JWT_SECRET: str = "SUPERSECRET"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"  # Load settings from .env file
        extra = "allow"  # Allow extra fields

settings = Settings()  # Instance of settings class
