from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from blx_api.schemas import schemas
from blx_api.infra.sqlachemy.repositories.user import UserRepo
from blx_api.infra.sqlachemy.repositories.product import ProductRepo
from blx_api.infra.sqlachemy.config.database import get_db, create_db

create_db()

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "welcome to blx"}


# Product
@app.post("/products")
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    new_product = ProductRepo(db).create(product)
    return new_product


@app.get("/products")
def list_product(db: Session = Depends(get_db)):
    produts = ProductRepo(db).list()
    return produts


# User
@app.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = UserRepo(db).create(user)
    return new_user


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    users = UserRepo(db).list()
    return users
