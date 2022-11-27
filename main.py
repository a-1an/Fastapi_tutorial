from fastapi import FastAPI
app= FastAPI()

@app.get("/")
def index():
    return {"name": "Alan"}

@app.get("/about")
def about():
    return {"data": "about page"}

@app.get("/get-students/{student_id}")
def get_students(student_id: int):
    return {"student_id_num": student_id}  
