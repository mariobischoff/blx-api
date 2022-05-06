from sqlalchemy.orm import Session

from blx_api.schemas import schemas
from blx_api.infra.sqlachemy.models import models


class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.User):
        db_user = models.User(name=user.name, phone=user.phone)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

    def list(self):
        users = self.db.query(models.User).all()
        return users

    def obtain(self):
        pass

    def remove(self):
        pass
