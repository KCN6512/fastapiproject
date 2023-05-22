import psycopg2
from fastapi import FastAPI
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

@app.get('/')
def home():
    return {'text': 'home_page'}

if __name__ == "__main__":
	import os
	command = 'uvicorn app.API_service:app --reload'
	os.system(command)    
