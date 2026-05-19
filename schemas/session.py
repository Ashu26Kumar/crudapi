from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from settings import setting


engine = create_async_engine(
    url = setting.PROSTGRES_URL,
    echo = True
)


async def create_db_tables():
    async with engine.begin() as e :
        from database import UserInfoModel 
        await e.run_sync(SQLModel.metadata.create_all(bind=engine))

async def get_session():
    session = sessionmaker(
        engine, expire_on_commit=False,
        class_=AsyncSession
    )
    async with session() as s:
        yield s 


dbRepository = Annotated[AsyncSession,Depends(get_session)]