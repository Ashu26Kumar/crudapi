

from datetime import datetime, timezone

from sqlalchemy.sql.annotation import Annotated
from sqlmodel import Field, SQLModel
from settings import setting

class UserInfoDataModel(SQLModel,table = True):
    __tablename__ = "AppUsers"
    id : int = Field(default=None,primary_key=True)
    firstName : str
    lastName:str
    age : int
    lastModifiedOn : datetime= Field(default=datetime.now(timezone.utc))
    created_On : datetime= Field(default=datetime.now(timezone.utc))


