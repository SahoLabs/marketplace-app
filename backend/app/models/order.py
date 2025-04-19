from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)   # FK -> User.id
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)  # FK -> Product.id
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", backref="orders")       # Many orders by one user
    
    product = relationship("Product", backref="orders") # Many orders for one product
