from fastapi import FastAPI
from .config.settings import settings
from .routes import auth_routes, order_routes, product_routes, vendor_routes

app = FastAPI(
    title="Marketplace API",
    version="0.1.0"
)

# Include your route modules
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(vendor_routes.router, prefix="/vendors", tags=["Vendors"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Marketplace API!"}
