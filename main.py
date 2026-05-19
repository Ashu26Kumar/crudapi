from fastapi import  FastAPI
from schemas.session import create_db_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def setup_on_start(app:FastAPI):
    await create_db_tables() 
    yield  app


app = FastAPI(lifespan= setup_on_start)



@app.get("/")
async def get_root():
    return {
        "message":"Api services are running"
    }

@app.get("/{id}")
async def get_user_by_id(id:int):
    return id