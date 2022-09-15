from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {'key':'Hello World'}

@app.get('/{name}')
def name(name: str='Sasha') -> dict[str, str]:
    return {'your_name': name}