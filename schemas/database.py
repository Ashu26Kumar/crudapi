
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone 
from sqlmodel import Field, SQLModel
from ..settings import setting

class UserInfoModel(SQLModel):
    id : int = Field(default=None,primary_key=True)
    firstName : str
    lastName:str
    age : int
    lastModifiedOn : datetime= Field(default=datetime.now(timezone.utc))
    created_On : datetime= Field(default=datetime.now(timezone.utc))


engine = create_async_engine(
    url = setting.PROSTGRES_URL,
    echo = True
)


async def get_session():
    session = sessionmaker(
        bind = engine,
        class_= AsyncSession,
        expire_on_commit= False
    )

    async with session() as s:
        yield s 

