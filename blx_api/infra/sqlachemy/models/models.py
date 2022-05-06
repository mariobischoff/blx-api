from sqlalchemy import Column, Integer, String, Float, Boolean
from ..config.database import Base


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Float)
    available = Column(Boolean)
