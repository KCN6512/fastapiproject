from fastapi import *
from schemas import *

app = FastAPI()


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}

@app.post('/book/')
def create_book(item : Book):
    return 
    
@app.get('/book/')
def get_book(q: list[str] = Query(['testbook','testbook2'], min_length=2, max_length=10, description='search Book')): #первое значение = значвение по умолчанию| сделать его обязательным = ...| regex регулярка | deprecated=True пометить параметр как устаревший| query нужно для огарничений в get запросе
    return q



if __name__ == "__main__":
    import os
    command = 'uvicorn main:app --reload'
    os.system(command)    
