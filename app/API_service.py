from enum import Enum
import json
import os
from typing import Optional, Any
import psycopg2
from fastapi import FastAPI, Query
from decouple import config

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
async def product(product: str):
	return {'product': product}

class ProductName(str, Enum):
    smartphone = "smartphone"
    tv = "tv"
    cpu = "cpu"

@app.get("/products/{product_name}")
async def get_product(product_name: ProductName):
    if product_name is ProductName.smartphone:
        return {"product_name": product_name, "message": "smartphone"}

    if product_name.value == "tv":
        return {"product_name": product_name, "message": "tv"}

    return {"product_name": product_name, "message": "cpu"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    print(file_path)
    print(os.path.exists(file_path))
    return {"file_path": file_path}

