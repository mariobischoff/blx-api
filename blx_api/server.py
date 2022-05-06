from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from blx_api.schemas import schemas
from blx_api.infra.sqlachemy.repositories.product import ProductRepo
from blx_api.infra.sqlachemy.config.database import get_db, create_db

create_db()

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "welcome to blx"}


@app.post("/products")
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    new_product = ProductRepo(db).create(product)
    return new_product


@app.get("/products")
def list_product(db: Session = Depends(get_db)):
    produts = ProductRepo(db).list()
    return produts
