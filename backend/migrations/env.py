import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✅ Fix path issues by appending project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your database setup and models
from app.core.database import Base
from app.core.config import settings

# 👇 Import all models here to register them with Base.metadata
from app.models import user  # Example: import your model modules

# Alembic Config
config = context.config

# Logging config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# This tells Alembic which tables to track
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = settings.DB_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Run it
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
