from typing import Annotated

from fastapi import Depends

from session import dbRepository 
from schemas.database import UserInfoDataModel
from models.userinfo import UserInfoDto

class UserService:

    def __init__(self,db:dbRepository):
        self.db = db

    async def getUserById(self,id:int)->UserInfoDataModel:
        return await self.db.get(UserInfoDataModel,id)
    
    async def addUsers(self,user:UserInfoDto)-> UserInfoDataModel:
        data = UserInfoDataModel(
            firstName= user.firstName,
            lastName= user.lastName,
            age = user.age
        )

        self.db.add(data)
        await self.db.commit()
        await self.db.refresh(data)

        return data
        
    async def deleteUserById(self,id:int) -> None:
        data = await self.db.get(UserInfoDataModel,id)
        await self.db.delete(data)
        await self.db.commit()


def Create_User_Dependency(db:dbRepository):
    return UserService(db)


UserRepository = Annotated[UserService,Depends(Create_User_Dependency)]