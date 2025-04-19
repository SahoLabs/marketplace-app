from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)  # PK
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)

    # Optional: vendor created by user (if needed)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", backref="vendors")  # FK -> User.id
