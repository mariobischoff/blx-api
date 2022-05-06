from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    # products: List[Product]
    # sales: List[Order]
    # purchases: List[Order]


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    # user: User
    detail: str
    price: float
    available: bool = False

    class Config:
        orm_node = True


class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    amount: int
    delivery: bool = True
    address: str
    comments: str = "Sem observações"
