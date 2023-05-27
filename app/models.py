from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str | None = 'default_description' # non required field with default value
    price: float
    category: 'Category'


class Category(BaseModel):
    name: str