from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)  # PK
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)

    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)  # FK -> Vendor.id

    vendor = relationship("Vendor", backref="products")  # Many-to-one: many products -> one vendor
