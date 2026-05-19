from fastapi import  FastAPI
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from api.Users import router
from session import create_db_tables
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

app.include_router(router=router,prefix="/user",tags=["users"])

