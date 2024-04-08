from typing import Union, Optional
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from bson import ObjectId
# from dotenv import load_dotenv, dotenv_values

import os

app = FastAPI()
# load_dotenv()
# Connect to MongoDB
# mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient("mongodb+srv://rahulkrgupta18032003:Rahul%402003@cluster0.ns3awbj.mongodb.net/")
db = client["school"]
collection = db["students"]


class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None



@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# Create student endpoint
@app.post('/students', status_code=201)
async def create_student(student: Student):
    result = collection.insert_one({
        "name": student.name,
        "age": student.age,
        "address": {
            "city": student.address.city,
            "country": student.address.country
        }
    })
    return {"id": str(result.inserted_id)}

@app.get("/students")
async def get_students(request: Request,  country: str = None, age: int = None):
    query = {}
    if country :
        query["address.country"] = country
    if age :
        query["age"] = {"$gte": age}
    res_students = list(collection.find(query))
    for student in res_students:
        student["_id"] = str(student["_id"])

    return {"data" : res_students}


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student :
        student["_id"] = str(student["_id"])
        return student
    else :
        raise HTTPException(status_code=404, detail="Student not found")


# Update student endpoint
@app.patch("/students/{student_id}")
async def update_student(student_id: str, student: Student):
    student_dict = student.dict(exclude_unset=True)
    updated_student = collection.update_one({"_id": ObjectId(student_id)}, {"$set": student_dict})
    if updated_student.modified_count == 1:
        # no content - as specified in the assignment document
        return {}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# Delete student endpoint
@app.delete("/students/{student_id}")
async def delete_student(student_id: str):
    deleted_student = collection.delete_one({"_id": ObjectId(student_id)})
    if deleted_student.deleted_count == 1:
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")



