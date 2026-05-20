from typing import Annotated

from fastapi import Depends

from session import dbRepository 
from schemas.database import UserInfoDataModel
from models.userinfo import UserInfoDto,UserUpdateDTO

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
    
    async def updateUserData(self,userDto:UserInfoDataModel,id:int)->UserInfoDataModel:
        # get user to be updated
        user = await self.db.get(UserInfoDataModel, id)
        user_Data = userDto.model_dump(exclude_unset=True)
        # update the data model with incoming change
        user_new =user.sqlmodel_update(user_Data)

        #add changes to db repository and flush and commit changes and update the user object
        self.db.add(user_new)
        await self.db.commit()
        await self.db.refresh(user_new)
        #returning the updated object
        return user_new



def Create_User_Dependency(db:dbRepository):
    return UserService(db)


UserRepository = Annotated[UserService,Depends(Create_User_Dependency)]