# fast API that consoles everything
import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    print("Hello World")
    return {"message": "Hello World"}

@app.post("/{name}")
def home(name):
    print("Hello ", name)
    return {"message": "Hello " + name}