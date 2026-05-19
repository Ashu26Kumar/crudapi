from fastapi import  FastAPI,HTTPException
from session import create_db_tables,dbRepository
from schemas.database import UserInfoDataModel
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from rich import print,panel

@asynccontextmanager
async def setup_on_start(app:FastAPI):
    await create_db_tables() 
    yield  


app = FastAPI(lifespan= setup_on_start)
@app.get("/")
def get_root():
    return {
        "message":"Api services are running"
    }

@app.get("/scalar",include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url =app.openapi_url,
        title = "Scalar Docs"
    )






@app.get("/{id}",status_code=200)
async def get_user_by_id(id:int,db:dbRepository):
    try:
        data = await  db.get(UserInfoDataModel,id)
        if data is None:
            raise HTTPException(status_code=404, detail="No users found")
        return data
    except Exception as e:
        print("Getting Exception while connection to database", e)






