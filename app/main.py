from typing import Optional
from fastapi import Body, FastAPI, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

my_posts = [{"title": "title of post 1"}]

class Post(BaseModel):
    title: str
    content: str
    publishied: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "API testing!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is a post"}

@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post.dict())
    return {"data": "new post"}

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    return {'success'}


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='apidev', user='postgres',
                        password='235711', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)