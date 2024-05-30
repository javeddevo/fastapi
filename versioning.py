from fastapi import FastAPI,APIRouter
app = FastAPI()
version_v1 = APIRouter()
version_v2 = APIRouter()

@version_v1.get("/task")
def version1_task():
    return {"message":"this is version one task"}
@version_v2.get("/task")
def version2_task():
    return {"message":"this is teh version two task"}

app.include_router(version_v1,prefix="/v1",tags=["version_v1_api"])
app.include_router(version_v2,prefix="/v2",tags=["version_v2_api"])

    
