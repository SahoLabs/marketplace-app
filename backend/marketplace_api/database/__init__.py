from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config.settings import settings

engine = create_engine(settings.DB_URL, echo=True)  # echo=True for SQL logs
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For Alembic migrations, you'll reference the same DB URL from settings
