from fastapi import *
from schemas import *
#docs_url=None, redoc_url=None отключить документацию docs и redoc
app = FastAPI() #docs_url=None, redoc_url=None

#Query = /?skip=0&limit=10
#Path = /items/foo
# Path url путь
# Query гет запрос в url
# Body отправить параметр как тело body 
# body embed = True значит добавить в json тело имя параметра

@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}

@app.post('/book/')
def create_book(item : Book, author: Author, quantity: int = Body(..., embed=True)): #Body делает параметр передаваевым в теле а не в url
    return {'item': item, 'author': author, 'quantity': quantity}
    
@app.post('/author/')
def create_author(author: Author):
    '''
    {
  "author": {
    "first_name": "string",
    "last_name": "string"
  }
} с включенным Body embed True

{
  "first_name": "string",
  "last_name": "string"
} без embed
    '''
    return {'author': author}

@app.get('/book/')
def get_book(q: list[str] = Query(['testbook','testbook2'], min_length=2, max_length=10, description='search Book')): #первое значение = значвение по умолчанию| сделать его обязательным = ...| regex регулярка | deprecated=True пометить параметр как устаревший| query нужно для параметров в get запросе
    return q

@app.get('/book/{pk}')
def get_book_id(pk: int = Path(..., gt=1, le=20), pages: int=Query(gt=10, le=500)):
    return {'pk': pk, 'pages':pages}

if __name__ == "__main__":
    import os
    command = 'uvicorn main:app --reload'
    os.system(command)    
