from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database engine using the DB_URL from the settings
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})  # SQLite-specific setting

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()  # All models will inherit from this base class
