from sqlalchemy.orm import Session

from blx_api.schemas import schemas
from blx_api.infra.sqlachemy.models import models


class ProductRepo:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(
            name=product.name,
            detail=product.detail,
            price=product.price,
            available=product.available,
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)

    def list(self):
        products = self.db.query(models.Product).all()
        return products

    def obtain(self):
        pass

    def remove(self):
        pass
