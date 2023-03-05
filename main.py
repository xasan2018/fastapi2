from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():

    return {"key":"Salom"}

@app.get('/{pk}')
def get_item(pk:int,q: float = None):
    q=q+1000
    return {"key":pk,"q":q}