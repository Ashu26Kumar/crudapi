


from fastapi import APIRouter, HTTPException

from data.CreateNewUserRequet import CreateNewUserRequest
from schemas.database import UserInfoDataModel
from services.UserService import UserRepository

router = APIRouter()


@router.get("/{id}",status_code=200)
async def get_user_by_id(id:int,user:UserRepository)->UserInfoDataModel:
    '''
        Calling the postgres sql database (crudapi) to get data by id
        `Params`: Id
        'Returns': UserInfoDataModel (User with given id)

    '''
    try:
        data = await  user.getUserById(id)
        if data is None:
            raise HTTPException(status_code=404, detail="No users found")
        return data
    except Exception as e:
        print("Getting Exception while connection to database", e)

@router.post("/createUser",status_code= 201)
async def create_new_user(req:CreateNewUserRequest,user:UserRepository)-> UserInfoDataModel:
    try:
        data = UserInfoDataModel(
            firstName= req.firstName,
            lastName=req.lastName,
            age=req.age
        )

        result = await user.addUsers(data)

        return result

    except Exception as e:
        print("Unable to save data to database :" ,e)

@router.delete("/{id}",status_code=200)
async def delete_user_by_id(id:int, user:UserRepository)->None:
    try:
        await user.deleteUserById(id)
        print("User with id {} has been deleted successfully".format(id))
        
    except Exception as e:
        print("Unable to delete the data : ", e)
        raise HTTPException(status_code=500)

