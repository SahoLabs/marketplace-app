# app/core/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Marketplace"
    DB_URL: str = "sqlite:///./test.db"  # Default to file-based SQLite DB (overridden by .env if needed)
    JWT_SECRET: str = "SUPERSECRET"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"  # Load settings from .env file

settings = Settings()  # Instance of settings class
