

from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

class UserInfoDataModel(SQLModel,table = True):
    __tablename__ = "AppUsers"
    id : int = Field(default=None,primary_key=True)
    firstName : str
    lastName:str
    age : int
    lastModifiedOn : datetime= Field(default=datetime.now())
    created_On : datetime= Field(default=datetime.now())


