import os
from typing import Annotated

from database.db import engine
from database.models import Base, Users
from fastapi import Body, Depends, FastAPI, Path, Query

from .pydantic_schemas import Category, Product, User


app = FastAPI()


@app.get('/')
async def home():
    return {'text': 'home_page'}


@app.get('/product/{product}')
async def product(product: str, q: int, j: float = 15.7,
                  integer: int | None = 0):  # product required path, q required, j required with default value, integer non required
    return {'product': product}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    print(file_path)
    print(os.path.exists(file_path))
    return {"file_path": file_path}


@app.post('/product_model')
async def create_model_product(product: Product):
    return product


@app.get('/product_annotated/')
async def annotated_product(product: Annotated[list[int],
Query(deprecated=True)] = [1, 2, 3]):  # if Query need Annotated
    return {'product': product}


@app.get('/Ellipsis_required/')
async def annotated_product_ellipsis(product: Annotated[str,
Query(max_length=10)] = ...):  # Ellipsis ... makes query required
    return {'product': product}


@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get")],
        q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.post('/multiple_bodies/{product_id}')
async def multiple_bodies(product_id: int,
                          category: Category,
                          product: Annotated[Product, Body()],
                          body: Annotated[float, Body(gt=10.0)] = 10.3):
    return {'product': product, 'category': category}


@app.put('/items/{item_id}')
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str | None = None,
        item: Product | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


async def get_user():
    print('depends')
    return {'sasha': 'troshchy'}


@app.get('/user/items')
async def user_depends(user: User = Depends(get_user)):
    print(user)

async def get_db():
    engine.connect()
    return engine

@app.get('/dbtest')
async def database_test(db=Depends(get_db)):
    print(db)
    # Base.metadata.create_all(engine)
    from sqlalchemy import select
    s = select([Users])
    print(s)