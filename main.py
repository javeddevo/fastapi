from fastapi import FastAPI,HTTPException,Path # type: ignore
from typing import Optional
from pydantic import BaseModel
import uvicorn  # type: ignore
app=FastAPI()

class Item(BaseModel):  #pydantic model to validate the data 
    name: str
    no:int
class Updatestudent(BaseModel):
    name: Optional[str]= None
    no: Optional[int]= None
student={
    1:{
        "name":"javeed",
        "no":1234
      },
    2:{
        "name":"ravi",
        "no":123
      }
        }

@app.get("/")
async def hello():
    return {"body":"sample"}

@app.get("/home")
async def hi():
    return "helloworld"

#get
@app.get("/student/{student_id}")
def student_info(student_id:int):
    if student_id not in student:
        raise HTTPException(status_code=404,detail=f"student {student_id} not found")  ### exception imp 
    return student[student_id]


#query parameters
@app.get("/student_info")
def info(name:str):
    for i in student:
        if student[i]["name"]==name:
            return student[i]
    raise HTTPException(status_code=404,detail=f"student {name} not found")
#post
@app.post("/insert/{student_id}")
def insert_data(student_id:int,val:Item):
    if student_id in student:
         raise HTTPException(status_code=404,detail=f"student {student_id} is present")
    else:
        student[student_id]=val
        return {"success":f"{val}"}

#put
@app.put("/update_data/{student_id}")
def update_data(student_id:int,val: Updatestudent):
    if student_id not in student:
        raise HTTPException(status_code=404,detail=f"student {student_id} is not present")
    else:
        student[student_id]=val
        return {"update successfully":f"{val}"}


# delete
@app.delete("/delete_record/{strudent_id}")
def delete_record(student_id:int):
    if student_id not in student:
        raise HTTPException(status_code=404,detail=f"student {student_id} is not present")
    del student[student_id]
    return {"status":"success"}




@app.get("/book/{no}")
def book(no:int):
    return {"bookshelf":no}

@app.get("/demo")
def demo(name:str,age:int):
    var={"name":name,"age":age}
    return var