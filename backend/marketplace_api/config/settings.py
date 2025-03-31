import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Example environment variables
    PROJECT_NAME: str = "Marketplace"
    DB_URL: str = "sqlite:///./test.db"
    JWT_SECRET: str = "SUPERSECRET"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"   # read from .env file at project root

settings = Settings()
