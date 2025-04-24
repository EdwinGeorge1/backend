from fastapi import FastAPI,Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session  


models.Base.metadata.create_all(bind=engine)


app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="4321",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)



my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorate food", "content": "I LIKE PIZZA", "id": 2}
    ]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
    # return None
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# request get method url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my api !!!!"}  

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return {"data": post}

@app.get("/posts")
def get_post():
    cursor.execute("""SELECT * FROM post""")
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts }    


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO post (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post }

@app.get("/posts/latest")
def get_latest_post():
    return {"data": my_posts[-1]}

@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("""SELECT * FROM post WHERE id = %s""", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")

    return {"post_detail": post}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE FROM post WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    cursor.execute("""UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")
    return {"data": updated_post}

