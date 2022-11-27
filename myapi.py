from fastapi import FastAPI
app= FastAPI()

all_posts={{"id":"1","title": "My first post","desc": "This is my first post"},{ "id":"2","title": "My second post","desc": "This is my second post"}}

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

@app.get("/posts/{id}")
def blog(id: int):
    for i in all_posts:
        if i["id"]==id:
            return {"data":i}


