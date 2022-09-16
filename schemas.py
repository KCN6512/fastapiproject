from datetime import date
from pydantic import *

class Genre(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    writer: str
    pages: int
    genres: list[Genre]
    date: date

