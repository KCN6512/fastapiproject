import os

from sqlalchemy import create_engine

user = os.getenv('POSTGRES_USER')
db_name = os.getenv('POSTGRES_DB')
db_pass = os.getenv('POSTGRES_PASSWORD')
DATABASE_URL = f'postgresql+psycopg2://{user}:{db_pass}@database:5432/{db_name}'

engine = create_engine(DATABASE_URL, echo=True)