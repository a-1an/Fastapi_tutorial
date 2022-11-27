from fastapi import FastAPI
from model import postschema
app= FastAPI()

all_posts=[{"id":1,"title": "My first post","desc": "This is my first post"},{ "id":2,"title": "My second post","desc": "This is my second post"}]
# def frozendict(d: dict):
#     return frozenset(d.keys()), frozenset(d.values())
@app.get("/")
def index():
    return {"name": "Alan"}

@app.get("/about")
def about():
    return {"data": "about page"}

@app.get("/get-students/{student_id}")
def get_students(student_id: int):
    return {"student_id_num": student_id}  

@app.get("/posts/all")
def all():
    return {"data": all_posts}

@app.get("/posts/{post_id}")
def blog(post_id : int):
    for i in all_posts:
        if i["id"]==post_id:
            return {"data":i}

@app.post("/posts/create")
def create(post: postschema):
    return {"data": post} 


