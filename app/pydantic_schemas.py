from pydantic import BaseModel, Field


class Category(BaseModel):
    name: str = 'default_name'


class User(BaseModel):
    name: str
    surname: str


class Product(BaseModel):
    name: str = Field(title='item name', default='default_name', max_length=100)
    description: str | None = 'default_description'  # non required field with default value
    price: float = Field(gt=1.0)
    category: Category  # set[Category] = set() non
