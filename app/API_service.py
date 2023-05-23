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
#     print(other.items())
#     return {'text': 'home_page'}, params, other

# If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use async def.

@app.get('/')
async def home():
	return {'text': 'home_page'}

# if __name__ == "__main__":
# 	import os
# 	command = 'uvicorn app.API_service:app --reload'
# 	os.system(command)    
