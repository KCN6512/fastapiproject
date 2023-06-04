import json
import os
from typing import Annotated, Any

import psycopg2
from decouple import config
from models import Product, Category

from fastapi import FastAPI, Query, Path, Body

app = FastAPI()

# try:
#     conn = psycopg2.connect(dbname='actordb', user='postgres', password=config('DB_PASSWORD')) #
# except:
#     print('Can`t establish connection to database')

# cursor = conn.cursor()
# cursor.execute('SELECT json_agg(actor_actor) FROM actor_actor;')
# all_actors = cursor.fetchall()
# cursor.execute('SELECT is_superuser, COUNT(is_superuser) FROM auth_user GROUP BY is_superuser;')
# count = cursor.fetchall()
# for i in count:
#      print(i)
# cursor.close()
# conn.close()
# print(all_actors[0][0][0]['content'])

# @app.get('/')
# def home(params: list[int] | None = Query(lt=10, default=None), **other: Any | None):
#     print(other.products())
#     return {'text': 'home_page'}, params, other

# If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def.

@app.get('/')
async def home():
	return {'text': 'home_page'}

@app.get('/product/{product}')
async def product(product: str, q: int, j: float = 15.7,integer: int | None = 0): #product required path, q required, j required with default value, integer non required
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
async def annotated_product(product: Annotated[str,
					        Query(max_length=10, deprecated=True)] = 'default_name'): # if Query need Annotated
	return {'product': product}


@app.get('/Ellipsis_required/')
async def annotated_product_ellipsis(product: Annotated[str,
					        Query(max_length=10)] = ...): # Ellipsis ... makes query required
	return {'product': product}


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.post('/multiple_bodies/{product_id}')
async def multiple_bodies(product_id: int, category: Category, product: Annotated[Product, Body(embed=False)], body: Annotated[float, Body(gt=10.0, embed=False)] = 10.3):
	return {'product': product, 'category': category}


# new test comment in a new test branch