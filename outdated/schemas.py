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
    author: Author

class Author(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(max_length=30)
    age: int = Field(ge=18, description='Возраст должен быть 18 или больше')

    # @validator('age')
    # def check_age(cls, value):
    #     if value < 18:
    #         raise ValueError('Автор не может быть младше 18 ')
    #     return value