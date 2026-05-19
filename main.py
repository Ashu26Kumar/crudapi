from fastapi import  FastAPI,HTTPException
from data import CreateNewUserRequest
from session import create_db_tables,dbRepository
from schemas.database import UserInfoDataModel
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from rich import print

@asynccontextmanager
async def setup_on_start(app:FastAPI):
    await create_db_tables() 
    yield  


app = FastAPI(lifespan= setup_on_start)
@app.get("/")
def get_root():
    '''
        Root api just to check if server is running or not 
    '''
    return {
        "message":"Api services are running"
    }

@app.get("/scalar",include_in_schema=False)
def get_scalar_docs():
    '''
        Scalar docs for more interactive Api documentation
    '''
    return get_scalar_api_reference(
        openapi_url =app.openapi_url,
        title = "Scalar Docs"
    )

@app.get("/{id}",status_code=200)
async def get_user_by_id(id:int,db:dbRepository)->UserInfoDataModel:
    '''
        Calling the postgres sql database (crudapi) to get data by id
        `Params`: Id
        'Returns': UserInfoDataModel (User with given id)

    '''
    try:
        data = await  db.get(UserInfoDataModel,id)
        if data is None:
            raise HTTPException(status_code=404, detail="No users found")
        return data
    except Exception as e:
        print("Getting Exception while connection to database", e)

@app.post("/createUser",status_code= 201)
async def create_new_user(req:CreateNewUserRequest,db:dbRepository)->None:
    try:
        data = UserInfoDataModel(
            firstName= req.firstName,
            lastName=req.lastName,
            age=req.age
        )

        db.add(data)
        await db.commit()
        await db.refresh(data)

    except Exception as e:
        print("Unable to save data to database :" ,e)

@app.delete("/{id}",status_code=200)
async def delete_user_by_id(id:int, db:dbRepository)->None:
    try:
        data = await db.get(UserInfoDataModel,id)           
        await db.delete(data)
        await db.commit()
        print("User with id {} has been deleted successfully".format(id))
        
    except Exception as e:
        print("Unable to delete the data : ", e)
        raise HTTPException(status_code=500)



