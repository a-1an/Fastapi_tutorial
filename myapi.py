
import os
from fastapi import FastAPI
from model import postschema
from pymongo import MongoClient
CONNECTION_STRING = os.getenv(secretone) 
myclient = MongoClient(CONNECTION_STRING)
mydb = myclient["Erudite"]

app= FastAPI()
@app.get("/")
def index():
    return {"name": "Alan"}

@app.get("/build/{cname}")
def build_company(cname):
    mydb.create_collection(cname)
    return {"company": cname}

@app.get("/addto/{cname}/{sid}/{loc}")
def add_data(cname,sid,loc):
   document = {
    "serialid": sid,
    "location": loc,
   }
   mydb[cname].insert_one(document)

@app.get("/query/{cname}/{sid}/{loc}")
def query_data(cname,sid,loc):
   query= {"serialid": sid,"location": loc }
   document = mydb[cname].find_one(query)
   if document:
      return {"value":1}
   else:
      return {"value":0}
 



