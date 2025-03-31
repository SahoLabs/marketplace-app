#!/bin/bash

# Create main directory tree
mkdir -p marketplace-app/{apps/{customer-app,vendor-portal/src,admin-panel/src},backend/marketplace_api/{config,database/{models,migrations/versions},routes,schemas,services,utils,tests},shared/{utils,constants,types,assets},scripts}

# Create customer-app files
touch marketplace-app/apps/customer-app/{App.js,package.json}

# Create vendor-portal files
touch marketplace-app/apps/vendor-portal/src/{main.js,App.vue}
touch marketplace-app/apps/vendor-portal/package.json

# Create admin-panel files
touch marketplace-app/apps/admin-panel/src/{main.js,App.vue}
touch marketplace-app/apps/admin-panel/package.json

# Backend FastAPI structure
touch marketplace-app/backend/{requirements.txt,pyproject.toml,Dockerfile}
touch marketplace-app/backend/marketplace_api/__init__.py
touch marketplace-app/backend/marketplace_api/main.py

# Backend config
touch marketplace-app/backend/marketplace_api/config/{__init__.py,settings.py,logging.conf}

# Backend models
touch marketplace-app/backend/marketplace_api/database/models/{__init__.py,user_model.py,vendor_model.py,product_model.py,order_model.py}
touch marketplace-app/backend/marketplace_api/database/migrations/alembic.ini

# Backend routes
touch marketplace-app/backend/marketplace_api/routes/{__init__.py,auth_routes.py,order_routes.py,product_routes.py,vendor_routes.py}

# Backend schemas
touch marketplace-app/backend/marketplace_api/schemas/{__init__.py,user_schema.py,order_schema.py}

# Backend services
touch marketplace-app/backend/marketplace_api/services/{__init__.py,order_service.py,vendor_service.py}

# Backend utils
touch marketplace-app/backend/marketplace_api/utils/{__init__.py,security.py,validators.py}

# Backend tests
touch marketplace-app/backend/marketplace_api/tests/{__init__.py,test_auth.py,test_orders.py}

# Shared modules
touch marketplace-app/shared/utils/.gitkeep
touch marketplace-app/shared/constants/.gitkeep
touch marketplace-app/shared/types/.gitkeep
touch marketplace-app/shared/assets/.gitkeep

# Scripts
touch marketplace-app/scripts/seed_data.py

# Root-level files
touch marketplace-app/{.env,docker-compose.yml,package.json,README.md}

echo "New marketplace-app directory structure created successfully."