# app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create a database engine using the DB_URL from the settings
engine = create_engine(settings.DB_URL, connect_args={"check_same_thread": False})  # SQLite-specific setting

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()  # All models will inherit from this base class
