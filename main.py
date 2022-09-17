from fastapi import *
from schemas import *

app = FastAPI()

#Query = /?skip=0&limit=10
#Path = /items/foo

@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}

@app.post('/book/')
def create_book(item : Book):
    return 
    
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
