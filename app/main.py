from typing import Optional
from fastapi import Body, FastAPI, Depends, status, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
import time
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)



@app.get("/")
def root():
    return {"message": "API testing!"}


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