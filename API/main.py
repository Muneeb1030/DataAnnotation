from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    title:str
    content:str
    rating: Optional[int] = None

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"new": "data"}

@app.post("/posts")
def create_posts(post:Post):
    print(post.dict())
    return {"data": "Hello"}