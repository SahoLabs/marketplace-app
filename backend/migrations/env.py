from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your database models here
from app.core.database import Base  # This will import the Base from the database.py file
from app import models  # 👈 this loads all models into Base.metadata
from app.core.config import settings  # Import your settings to fetch DATABASE_URL

# This is the Alembic Config object, which provides access to the values within the .ini file in use
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Here we set the target metadata for Alembic to use
# target_metadata should be the metadata of your Base
# This tells Alembic which models to include in migrations
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = settings.DATABASE_URL  # Use DATABASE_URL from config.py (or .env)
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
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine whether to run in offline or online mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
